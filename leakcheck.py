"""Leak check for the public site. Run before every commit.

Clients are named openly on this site — that was authorised on 2026-09-06 and
this script no longer treats company names as secrets. What it still catches is
the stuff that would be a mistake in any repo: credentials, API keys, bearer
tokens, personal email addresses, individual contact names, local filesystem
paths, and internal workspace or campaign ids.

The person blocklist lives in leakcheck_private.py, which is gitignored — so
this file is safe in a public repo without being the roster it exists to catch.

Run:  python leakcheck.py
Exit: 0 clean, 1 leak found, 2 the private blocklist is missing.
"""
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
SCAN_DIRS = ["content", "public"]
SCAN_EXT = {".md", ".html", ".txt", ".json", ".css", ".js", ".svg", ".toml", ".csv"}

# Client names and client domains are NO LONGER BLOCKED. On 2026-09-06 the owner
# confirmed that naming clients and publishing their results is authorised, so
# the anonymise-by-type rule is retired and these lists are empty.
#
# What this file still guards is everything that was never anonymisation:
# credentials, internal ids, and personal contact data belonging to individuals
# who did not agree to anything. Naming a company you worked for is your call.
# Publishing the name and inbox of a person at that company is theirs.
NAMES = []
DOMAINS = []

# Named individuals from client onboarding. Still blocked: these are third
# parties, and the authorisation covers client companies, not their staff.
# Kept in leakcheck.private.py so this file can live in a public repo without
# itself becoming the directory of names it exists to catch.
try:
    from leakcheck_private import PEOPLE
except ImportError:  # pragma: no cover - the guard must fail loudly, not quietly
    print("leakcheck: leakcheck_private.py not found — the PEOPLE blocklist is\n"
          "  unavailable, so this run cannot verify that no individual is named.\n"
          "  Restore it (it is gitignored, so it lives outside the repo) or set\n"
          "  LEAKCHECK_ALLOW_NO_PEOPLE=1 if you genuinely have no list.",
          file=sys.stderr)
    if not os.environ.get("LEAKCHECK_ALLOW_NO_PEOPLE"):
        sys.exit(2)
    PEOPLE = []

PATTERNS = [
    (re.compile(r"\b\d{2,4}\|[A-Za-z0-9]{20,}"), "bearer token"),
    (re.compile(r"\bwl_[A-Za-z0-9]{12,}"), "verification api key"),
    (re.compile(r"\b(?:sk|pk)-[A-Za-z0-9\-_]{20,}"), "api key"),
    (re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"), "email address"),
    (re.compile(r"[A-Za-z]:\\(?:Users|Professional)"), "local filesystem path"),
    (re.compile(r"\bEMAILBISON_TOKEN_\w+"), "env var name"),
    (re.compile(r"\bSERPER_API_KEY|WIZLEADS_API_KEY|STORELEADS_API_KEY\b"), "env var name"),
    (re.compile(r"\bworkspace \d{2,3}\b", re.I), "internal workspace id"),
    (re.compile(r"\bcampaign 1[0-4]\d\d\b", re.I), "internal campaign id"),
]

# Allowed in prose because they name a public standard or a public dataset, not a client.
ALLOWLIST = {"AS9100", "IPEDS", "USAspending", "EDGAR", "FDIC", "NCUA", "CMS", "NAICS"}

# The site owner's own published contact address. The email rule exists to stop
# OTHER people's inboxes reaching a public repo; the one the site deliberately
# invites replies to is not a leak. Kept as an explicit set rather than a
# loosened pattern, so any address that is not on this line still trips.
OWN_EMAILS = {"shubhamsharma220802@gmail.com"}

# Vestigial: NAMES is empty, so nothing consults this any more. Kept only so
# the literals() signature stays stable if a name ever needs blocking again.
PUBLIC_CLIENTS = set()


def literals():
    for group, kind in ((NAMES, "client name"), (PEOPLE, "person"), (DOMAINS, "domain")):
        for term in group:
            if term in ALLOWLIST or (kind == "client name" and term in PUBLIC_CLIENTS):
                continue
            if kind == "domain" and "." not in term:
                # A bare company name in DOMAINS would also match the authorised
                # wordmark. Require a TLD so "HoloGrowth" passes but
                # "hologrowth.com" is still caught.
                pat = rf"(?<![\w.-]){re.escape(term)}(?=\.[a-z]{{2,}})"
            else:
                pat = rf"(?<![\w.-]){re.escape(term)}(?![\w-])"
            yield re.compile(pat, re.I), kind, term


LITERALS = list(literals())


def scan(path):
    hits = []
    text = path.read_text(encoding="utf-8", errors="replace")
    for line_no, line in enumerate(text.splitlines(), 1):
        for pat, kind, term in LITERALS:
            if pat.search(line):
                hits.append((line_no, kind, term, line.strip()[:90]))
        for pat, kind in PATTERNS:
            for m in pat.finditer(line):
                if kind == "email address" and m.group(0).lower() in OWN_EMAILS:
                    continue
                hits.append((line_no, kind, m.group(0)[:40], line.strip()[:90]))
                break
    return hits


def main():
    files = [p for d in SCAN_DIRS for p in (ROOT / d).rglob("*")
             if p.is_file() and p.suffix.lower() in SCAN_EXT]
    if not files:
        print("nothing to scan — run build.py first")
        return 0

    total = 0
    for f in sorted(files):
        hits = scan(f)
        if hits:
            total += len(hits)
            rel = f.relative_to(ROOT)
            print(f"\n{rel}")
            for line_no, kind, term, ctx in hits:
                print(f"  line {line_no}  [{kind}] {term}")
                print(f"      {ctx}")

    print(f"\nscanned {len(files)} files")
    if total:
        print(f"BLOCKED — {total} leak(s) found. Fix before committing.")
        return 1
    print("clean — no client names, people, domains, keys or internal ids")
    return 0


if __name__ == "__main__":
    sys.exit(main())
