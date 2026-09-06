---
title: Nine more engagements, briefly
client: Various
year: 2026
tag: Index
summary: The rest of the book of work — an honest year-end retrospective, an AI personalisation rebuild, three directory scrapes with two negative verdicts, and the marketplace project that stopped at a bot wall.
featured: false
metric: 9
metric_label: further engagements, each with the finding worth keeping
---


The six case studies above carry the most weight. These are the rest of the book, each with the
finding worth keeping.

---

## An enterprise loyalty platform

**201,525 sent · 2,439 replies · 80 positive**

The account had been sending for months across six verticals when I took it. The strategic call
was to move the CPG segment from **customer loyalty to channel loyalty** — rewarding
distributors and wholesale accounts rather than consumers — because roughly 80% of those brands
already ran a consumer points app, and the list was 100% wholesale-present.

**The data trap:** the source list carried a marketing-apps column and the obvious angle was
"you don't have a loyalty programme." That column does not detect loyalty platforms. I sampled
ten brands and **eight already ran one**, invisible in the data. A blank field is not evidence
of absence; it is evidence your source does not carry that field.

**The deliverable was an honest year-end retrospective.** Full-history export: 60 campaigns,
37,706 unique people contacted across 62,768 touches, 806 genuine human replies, 75 flagged
positive — **of which 55 were genuinely interested.** The rest were out-of-office, tagged as
such rather than quietly counted.

**The headline had to lead with 55, not 62,768.** The bigger number is touches. The smaller one
is the truth, and leading with it is the only version of the report that survives a follow-up
question.

Three failure themes, each evidenced from real replies: offer friction, weak proof, and ICP
gaps. The second one mattered most — **68 replies asked for case studies**, which was a direct
consequence of a proof constraint that only the client could change. When a compliance rule is
costing you conversions, that is a finding to escalate, not a limitation to write around.

---

## A DTC conversion-rate agency

**132,460 sent · 1,546 replies · 88 positive**

Their flagship AI-personalisation campaign had failed. An agent reviewed a prospect's whole
store and returned five observations that could have been written about any store — so
prospects read it as a template, because functionally it was one.

**The rebuild narrowed the scope until the output had to be specific.** Render the homepage at
390px mobile width, return exactly *one* weakness, quoting their real hero text. There is only
one hero headline; the agent either has something concrete to say about it or it does not.

Three details carried it. **Mobile rendering is not window resizing** — a resized desktop
browser still renders the desktop layout, so you produce confident observations about a page
the prospect has never seen. **The agent gets permission to return nothing**, hitting roughly
80% send and 20% skip, and is explicitly forbidden from manufacturing a nitpick — which is
precisely what killed version one. And **skipped leads route to a guarantee-led sequence** that
needs no personalisation, so nothing is wasted.

I also built them a Slack bot: one command turns any store URL into conversion-optimised
desktop and mobile hero mockups, in-thread, rendering **the prospect's actual product image**
rather than a generic template. It runs with no API key — a founder cost constraint — by
shelling out to a locally authenticated CLI on the same server.

**The honest tension:** across the account, offer-led angles outperformed observation-led ones
roughly four to one. Specificity earns the read; the offer earns the reply. The first-fold work
optimised only one of the two.

---

## A speed-to-lead SaaS company

**99,168 sent · 1,864 replies · 38 positive**

Three landmines in the onboarding form, all reported before a single lead was sourced. **The
stated monthly lead target was 100,000** — roughly 6,600x every other client, almost certainly a
market-size figure typed into a monthly-target field. **All six case studies were AI-drafted
placeholders**, several literally prefixed "estimated." And **there was no suppression list**, so
the client's own customers were about to receive a cold pitch.

The copy therefore quoted no figures at all and sold speed, simplicity and price — all three
real and verifiable at a $99 price point. That is the correct call, and it produced better copy
than a fabricated case study would have.

The build: **3,580 genuinely net-new leads, deduplicated against all 36,625 already in the
account** rather than against the files on disk. Catch-all addresses were kept — catch-all is a
property of the *domain*, not a verdict on the address, and rejecting on it discards a third of a
valid list.

**Reply rate 1.88%, one of the highest here. Positive rate 0.038%, one of the lowest.** That gap
is the diagnosis: the message gets read and does not convert, which points straight back at the
six unverified case studies flagged on day one.

---

## A ringless-voicemail SaaS company

**130,175 sent · 877 replies · 59 positive**

In the portfolio mostly for what I told the client *not* to send.

Three directory scrapes. The first worked: **1,339 agencies**, a strict superset of an earlier
508-row list that had been a six-page undershoot. Two structural findings saved real time — the
same 30 premium listings are pinned to *every* page, so deduplicating by listing slug is
mandatory or you triple-count them; and all four subcategories turned out to be subsets of one
pool, so crawling three of them separately returned zero new rows from ~1,700 page fetches.

**The second scrape produced a negative verdict.** 1,278 firms in a public-affairs category, of
which **60% failed the client's own 10-employee floor** and 462 listed the relevant service at 0%
of their mix. **Tier A: 107 firms.** That is the honest deliverable from 1,278 rows, and it came
with a recommendation to use a different source class entirely.

**The third raised a compliance flag rather than a list.** 6,867 recruiting and staffing firms,
4,121 clearing the fit bar — the best-fitting list built for this client. But recruiters dial
*candidates*, which is consumer contact, and this client's ICP excludes consumer contact partly
for regulatory reasons. Their hiring-manager dialing is genuinely B2B. The list mixes both
motions and the distinction is a legal one, not a preference.

**The account data vindicated the pre-send scoring.** The hiring-signal campaign and the
qualified agency list carried it. The two large campaigns built on the weak-scoring lists
produced **zero positives across 13,050 sends.**

---

## A B2B marketing agency

**147,029 sent · 1,557 replies · 51 positive**

The assignment was a list of small independent insurance agencies, target 5,000+ emails. Genuinely
hard to buy — they are two-to-ten-person local businesses, and the ones that *are* in standard
databases tend to be captive branches of national carriers, which are exactly the wrong prospects.

**17,455 agencies across all 50 states, 14,268 with domains, for about $3 in API spend.** A
metro-grid map scrape, then a second expansion pass. The scrapers dedupe on both place ID and
domain, write incrementally, and resume from the existing file — which is what made the expansion
a re-run rather than a rebuild.

**The independence filter is what made it usable.** A blocklist and classifier strip the national
carriers, aggregators and franchise networks that otherwise dominate the top of every metro query.

The segment I built outperformed the account's inherited work **three to five times** on positive
rate. And the same list split by mail provider produced the **twelvefold reply-rate gap** that
appears as an exhibit elsewhere on this site.

---

## An automotive analytics SaaS company

**6,021 sent · 74 replies · 6 positive**

Finding franchise dealers sounds trivial and is not — searching maps for "car dealership" buries
franchise rooftops under used-car lots and service centres.

**The fix was to change the query axis rather than the filter.** Query by manufacturer brand and
metro instead of by generic category. And **the map platform's own business-type field is the
franchise signal** — a result typed as a specific brand's dealer is, by the platform's own
classification, a franchise rooftop. Twenty brands across 78 metros in nine states.

**I deliberately excluded the independent dealers** the client's ICP also named, because unit
volume cannot be determined from a map listing. There was no honest way to apply their own
50-unit gate to that data, so those rows would have been unqualified guesses shipped as
qualified ones.

Small account, all campaigns paused. Single-rooftop targeting beat dealer groups 6 positives to
0, which fits the product — one dealer principal can approve a four-figure monthly spend; a group
executive cannot without a process.

---

## A DTC profit advisory

**44,450 sent · 320 replies · 12 positive**

**The reusable finding is about the list source's API, and it is a nasty one.** It supports five
parameters and **silently ignores every other one.** Not rejected — ignored, with a 200 response.
So a request that looks filtered by country, platform and revenue returns a plausible result set
that is actually slices of the entire 3.67-million-row universe. Unknown parameters are accepted
without complaint.

**A silently ignored filter produces a plausible-looking result set that is entirely
unfiltered** — precisely the class of error that reaches a client deliverable before anyone
notices. The only reliable check is whether the total count moves when you add the filter.

Two more traps in the same API: revenue is reported **monthly, in cents**, so getting it wrong by
two orders of magnitude is easy; and because sort is descending, a banded pull collects at the
band's top edge, so "$1M–$5M brands" is really a "$5M brands" list unless you sample across it.

**Bounce rate 0.27% — the cleanest in the portfolio**, a third of the blended average. That is
what a curated database looks like next to scraped directory data.

**The strategic mistake is visible in the campaign table.** One campaign was working at 0.082%.
The response was to build vertical variants, which collectively produced 2 positives on 20,753
sends, with two of them returning zero. When something works, **scale it before you vary it.**
Vertical variants feel like segmentation and can just as easily be dilution — and you only find
out by running the control alongside them.

---

## A retail-media agency

**Deliverable: a brand and holding-company universe across ten retail marketplaces**

Mostly a map of a bot-protection landscape, because that is what the engagement turned out to be.

**Won two.** One retailer's internal search API exposes a brand facet per category, returning
3,941 brands filtered to 2,357 clean — using the retailer's *public front-end key*, not a
purchased one. A second retailer's protection was defeated with the same TLS-impersonation and
residential-proxy technique used elsewhere in this portfolio: **2,772 brands.**

**Lost two, and said so.** Two large retailers sit behind a protection product that detects the
browser-automation protocol itself and requires a JavaScript-validated sensor. Plain HTTP,
warmed sessions, headless automation and *headful* automation all returned 403 on the pages that
matter. A residential proxy is not sufficient — the block is on automation, not on the IP. The
honest conclusion, delivered as one: **this requires a commercial unlocker service, which is a
purchase decision for the client.**

**The finding that stopped the biggest piece of work.** The plan's next step was resolving 2,357
brands to parent companies, about 6,229 queries. **I ran a 25-brand sample first.** The resolver
returned ten "probable" parents. **All ten were false positives** — a furniture brand matched to
an unrelated veterinary acquisition, another to an Indian fintech, a third to its own e-commerce
platform.

Root cause: the long tail of a marketplace brand list is dominated by generic import and
direct-to-consumer seller names that **have no corporate parent at all** — and are not targets for
this client either. The resolver had been tuned on well-known brands with clean search results.
Pointed at generic names it matches unrelated acquisition news, confidently.

**Sample before you scale, especially when the pipeline "works."** It ran without errors and
returned confidently formatted results. Ten out of ten were wrong, and nothing in the output
signalled it.

---

## An identity-infrastructure startup

**Deliverable: two print-quality tracking setup guides, ten pages each**

Analytics and ad-platform conversion tracking on a no-code site, documented so a marketer could
do it — and re-do it — without a developer. That second half is the actual brief.

The one production decision worth explaining: **the interface panels are recreated vector
illustrations, not screenshots.** They stay sharp in print where a screenshot goes soft at
exactly the labels that matter; numbered callouts stay anchored to the element they point at; and
they do not capture whatever banner happened to be live that day. The tradeoff is honest — a
recreation is an idealisation, so it has to be accurate or it is worse than a screenshot.

The guides regenerate from source with a single command, which is what makes them maintainable:
when the interface changes, the fix is an edit and a rebuild, not a re-layout.

They ship with a deliberate list of the client-specific values still to be filled in, rather than
plausible-looking fake ones. **A guide containing a realistic fake tracking ID will be followed
literally by someone**, and then the tracking silently does not work — the same failure mode as
every other silent data error in this portfolio.
