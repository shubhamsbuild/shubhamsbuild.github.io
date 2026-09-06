# Portfolio

Source for my GTM engineering portfolio. Static site, no framework, no dependencies.

**Live:** _(Netlify URL goes here once linked)_

---

## What this is

Case studies from eighteen months running the go-to-market data layer for thirteen B2B
accounts — building lists that no vendor sells, the enrichment that makes them usable, the
sending infrastructure underneath, and the measurement that says which half of it worked.

Every number on the site is pulled live from the sending platform's API rather than typed
from memory. The charts in `assets/` are generated from that same snapshot, so they can be
regenerated whenever the numbers move.

Clients are anonymised by type. They are a current employer's clients and naming them is
their call, not mine. The numbers are unchanged.

## Layout

```
content/
  index.md            home page copy
  work/*.md           one case study per file, front matter + markdown
assets/               generated SVG exhibits
build.py              the generator: content/ + assets/ -> public/
leakcheck.py          fails the build if anything private appears in the output
field-guide.html      a separate research directory, carried through as-is
public/               generated output — what Netlify serves
```

## Build

```bash
python build.py && python leakcheck.py
```

No dependencies — standard library only, Python 3.9+. `build.py` includes a small markdown
renderer (headings, tables, lists, blockquotes, inline formatting) because pulling in a
markdown library for six files was not worth the supply chain.

Preview locally:

```bash
python -m http.server 8899 --directory public
```

## leakcheck.py

The site is written anonymised by hand rather than machine-substituted — substitution
produces bad prose and misses things like bare domains. `leakcheck.py` is the safety net. It
scans the whole published tree and exits non-zero if it finds a client name, a named
individual, a client domain, an API key or bearer token, an email address, a local
filesystem path, or an internal workspace or campaign identifier.

**It runs before every commit.** If it fails, the commit does not happen.

## Deploying

Netlify builds from `main` on push. `netlify.toml` sets the publish directory to `public/`
and the build command to `python build.py`. The generated output is committed as well, so
the site is servable even if the build step is ever skipped.
