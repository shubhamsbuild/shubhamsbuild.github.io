---
title: Sixty thousand companies no data vendor sells
client: HavenStone Advisory
year: 2026
onboarded: 2026-07-07
tag: Data acquisition
summary: Eight verticals of owner-operated trades, built from map grids, directories and manufacturer locators. Zero spent on list vendors, and four data-quality traps caught before they reached a send.
featured: true
metric: 44
metric_label: interested replies from 51,333 sends into a list no vendor sells
problem: A tax advisory firm sells to owner-operated trades businesses at $1M to $10M revenue. No data vendor covers them: they exist in map data, business bureau directories and manufacturer locators, in four inconsistent forms.
system: Eight verticals built from scratch. Adaptive densification for capped locators, TLS-fingerprint impersonation through rotating residential exits for a hard Cloudflare block, and manufacturer certification indexes that carry email addresses directly.
output: Roughly 60,000 trade companies and 27,000 attorneys, plus four data-quality traps caught before they reached a send, including 30% of a supposedly net-new list that had already been contacted.
---


## The account

A CPA-led proactive tax-strategy practice. The buyer is an **owner-operated trades or
home-services business, $1M–$10M in revenue, 1–50 employees.** Titles are owner, CEO, founder,
partner. Named verticals: HVAC, plumbing, roofing, water restoration, with attorneys as a
secondary track.

It is a **regulated engagement**, tax copy carries no numeric savings guarantees. Savings are
tied to a named client's result, never promised to the reader.

Two operational facts shaped everything. There was **no booking link**, so every call to
action had to be reply-based. And the ICP is local SMB, which means map data and directories,
not the standard B2B databases. **A $3M family-run restoration company in a mid-size Texas
city is not in any vendor's database.** It is in Google Maps, in a business bureau directory,
in Yellow Pages, and on a manufacturer's certification locator, in four inconsistent forms,
and it is your job to work out that they are the same business.

So the engagement is a data-acquisition problem wearing a copywriting problem's clothes.

## What was built

Eight campaigns, each with its own sourcing strategy. **No paid list vendor on any of them.**

| Vertical | Geography | Companies | Email-ready |
|---|---|--:|--:|
| HVAC | two states | 5,360 + 5,465 net-new | 2,396 |
| Water restoration | two states | 4,487, then +4,330 | **4,796** |
| Water restoration | all 50 states | **11,252** | **4,464** |
| Attorneys | one state | 26,928 rows → **21,095 unique** | 21,095 verified |
| Roofing | two states | **22,173** | **10,242** |
| Attorneys | second state | 8,148 rows → **6,474 unique** | 6,242 verified |
| Plumbing | two states | **14,584** | 5,658 net-new |

**Roughly 60,000 trade companies and 27,000 attorneys, at effectively zero list cost.** The
only spend was search credits and per-lead verification.

## Four techniques worth showing

**Adaptive densification, for locators with a result cap.** A trade-association contractor
locator caps a single zip-and-radius query at roughly 316 nearest results. Brute-forcing all
41,000 US zip codes is 41,000 requests, 95% redundant. Instead: run a coarse national grid at
100-mile range. Any query returning under ~300 is *provably complete for its disk*. Densify
only the cells that capped, by re-querying the zip codes of the businesses that query actually
returned, one radius step finer, 100 to 25 to 10 to 5, until nothing caps. **Full national
coverage in about 480 requests instead of 41,000.** The pattern transfers to any dealer
finder, service-area map or franchise locator.

**Getting past a hard Cloudflare block.** A major directory hard-blocks datacenter IPs at the
edge. Everything IP- or fingerprint-based failed: plain HTTP libraries return 403, the
in-app browser gets an unambiguous block page, and headless automation pins one residential IP
per session, so once it is flagged, everything blocks. What worked was **a real Chrome TLS
fingerprint through a rotating residential proxy** that hands out a fresh exit IP per TCP
connection. The edge lets roughly **8%** of residential exits through, so the pattern is: retry
each page against fresh IPs until one returns 200 *with real content*, verified by checking for
an expected element in the body rather than trusting the status code. Counter-intuitive tuning:
**three workers beat six**, because threads compete for the same small pool of unflagged exits.

**The bug that looked like a broken proxy.** This is the one I would tell in an interview. A
scrape returned 1,746 rows with 19 of 49 metros reported blocked. The obvious conclusion was
that the proxy had degraded. The tell was a suspiciously consistent +60 per metro, exactly two
pages of thirty listings. **The harness aborted an entire metro on a single blocked page.** At
a ~40% per-page block rate, most metros died at page two. The proxy was fine the whole time.
Treating a blocked page as *skippable*, give up only after three consecutive blocks, returned
**9,038 rows at a 2% block rate. Same proxy, same day. A 5.2x recovery.**

**Manufacturer locators beat consumer directories.** For roofing, the highest-yield source was
not a directory at all. A major manufacturer's contractor locator runs on a hosted search index
that **contains email addresses directly**: 1,802 contractors, 1,794 with an email, and 82% of
those are personal local-parts rather than generic inboxes. A second manufacturer's sitemaps
added 1,000 more plus a certification stamp on 2,460 companies already in the master. That one
insight lifted email-ready coverage **+33%** and produced 1,704 rows needing no enrichment at
all.

## Four traps caught before they reached a send

**A directory's "website" field was inflated.** It reported 11,933 websites for one vertical.
**4,554 of them pointed at the directory's own hosted-microsite product**, and 974 more at
internal redirect pages. Only 6,054 rows had a real company domain. Taken at face value, that
would have poisoned 19,000 rows and burned enrichment credit on microsites with no mail server.

**A locator's company ID is not a dedupe key.** One source returned 20,348 rows containing only
**~2,745 unique companies**, overlapping queries return the same business once per query that
reaches it, and the site issues a *different* ID each time. One contractor appeared 73 times in
a downstream export. Dedupe on normalised domain, or company plus city plus state.

**The obvious directory category was a decoy.** The intuitive category name for one vertical
tops out around 532 companies across two states. The correct category returns **five to six
times more**. Two separate builds used the narrow one and under-scraped by roughly 4x. Always
probe result totals across candidate categories before committing to a scrape.

**Host normalisation before enrichment.** On one rebuild, 213 rows were subdomains. Most parents
were site builders with no mail server at all, plus lead-generation networks running city
microsites. Enriching those burns credits for nothing. The rest were real-company subdomains and
had to be re-rooted to the registrable domain or email lookup fails outright.

## The dedupe pass that actually mattered

One rebuild ran four passes the earlier merge never did. The one that changed the outcome:
**deduplicating against the live sending platform, not just against the files on disk.**

**2,934 companies by domain plus 52 by email, roughly 30% of the "net-new" list had already
been contacted.** An earlier list had been loaded and sent months before, and nothing in a
file-level merge knew that.

Two judgement calls from the same pass, both about *not* over-collapsing. **Do not collapse on
brand root**, two similarly named roofing companies in different cities are different
companies. And **keeper scoring must rank has-domain above has-email**, or the email-only row
wins the merge, demotes the real domain to a secondary column, and leaves the record
un-enrichable.

On a later vertical the same baseline pass found the opposite and it was worth reporting: **only
4.2% overlapped**, despite an expected heavy overlap with an adjacent trade. Worth not
over-discounting adjacent verticals in future.

## The copy

The house format is an **angle bank, not a sequence**, many distinct opening angles, each
mapped to an existing lead magnet from the client's 57-asset library. **The variable under test
is the angle. Nothing new gets produced.**

Nothing is attached or linked in email one. **The reply is both the conversion event and the
attribution event.**

Founder feedback reshaped it three times, and the corrections are the useful part. *Never make
the copy about us, always about them*, every self-frame flips to the prospect's point of view.
*Nobody cares about cleaner books; add profit and now we're talking.* And open with a question
rather than a statement, press on the problem, keep it under five lines.

## The failures

Two shipped, which is why they are here.

**A merge variable rendered as nonsense.** A directory's category column is always phrased
`<State> <Practice> Attorney`. Dropped raw into a sentence, it rendered the state twice plus a
stray noun. And an earlier loader lowercased the value, destroying acronyms. **Always render a
sample sentence before loading.**

**Directory staff got into the list.** 84 leads were employees of the directories themselves, scraped where the listing's website field pointed at the listing rather than the firm. They
verify as valid because the mailboxes are real. 28 went live, and 56 more were skipped only
because they were already in an earlier campaign, meaning this shipped there too. A
directory-domain blocklist belongs in any future build of this kind.

## The numbers

**51,333 sent, 896 unique replies at 1.75%, 44 positive, bounce 1.35%.**

Attorneys outperformed trades on this account, which validated the founder's instruction to
treat them as the workhorse, and which is mildly awkward given that trades are the stated ICP
and where all the hard data work went. Both things are true and both belong in the report.

Bounce at 1.35% is the highest of any account here, and it is a direct consequence of the source
mix: scraped SMB directory data carries more dead mailboxes than a purchased list, even after
verification.

## The transferable lesson

**Local SMB is the hardest B2B list to build, the least well served by vendors, and therefore
the most worth being good at.** Every technique here transfers to any market where the buyer is
a business owner rather than a job title at a company with a corporate web presence.

And the honest one: **the failures on this account were list-hygiene and merge-variable failures,
not scraping failures.** Getting the data was the part that worked. Getting it into an email
correctly is where it broke.
