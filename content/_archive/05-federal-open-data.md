---
title: A 5,229-company government-contractor universe for $2.40
client: A knowledge-management consultancy
year: 2026
tag: Data acquisition
summary: Federal open data is a serious, free B2B data source and almost nobody in go-to-market uses it. Contract awards, subaward relationships, acquisition dates and real headcounts — all keyless.
featured: true
metric: $2.40
metric_label: total spend for a 5,229-company mail-confirmed universe
problem: A knowledge-management consultancy targets 500+ employee regulated organisations. The brief contradicted itself on company size, and the named targets were federal agencies that do not buy through an inbox.
system: Built the universe from keyless federal open data: spending records for contractor and subcontractor relationships, securities filings for acquisition timing, and three federal regulators for real employee counts.
output: 5,229 mail-confirmed companies for $2.40, a second campaign whose firmographics cost nothing, and a classifier gap that was misrouting 415 government-cloud tenants, caught before the government send.
---


## The account

Knowledge-management and enterprise content consulting: turning documents scattered across a
dozen internal systems into a governed single source of truth in 30 to 90 days. The buyer is a
500+ employee regulated or public-sector organisation. The cold call to action is a fixed-fee
assessment at $5K–$10K, leading to implementation at $25K–$50K+.

## Two things I flagged before any work started

**The size and revenue statement contradicted itself.** The onboarding form specified 500+
employees, named several household-name defense and healthcare giants as targets, and also
stated a revenue band that describes a company two orders of magnitude smaller. Those are
different companies, and it changes the source entirely.

**Federal agencies are not a cold-email ICP.** Government addresses are hard to reach and, more
to the point, federal buying happens through contract vehicles, not through an inbox. The
realistic cold audience is contractors, healthcare, financial services and commercial aerospace.
That was raised as a question rather than asserted as a decision.

I also noted plainly that the proof bench was thin — the flagship case study was qualitative
only.

## Campaign one: the govcon universe

**5,229 mail-provider-confirmed companies, ready for contact enrichment. Total spend: $2.40.**

Composition: 4,272 from federal spending data, tiered by obligation size; 830 from a defense
industry association member roll; 127 from a government IT association.

The core source is the **federal spending API, which is keyless.** No vendor, no contract, no
per-record cost. Association member rolls filled the rest — with the practical note that one
association's paywall is only on its main host and the member directory is reachable on its
membership host, while another association's site was simply down.

**The launch plan's industry-code list was incomplete, and it mattered.** As specified, the six
codes yielded **569 companies** against a plan estimate of roughly 6,000. It omitted the largest
federal IT-services code entirely, and the defense R&D code — where most document-heavy contract
work actually lives, worth **+2,641 rows** on its own. Twelve codes were added. Two of the
original six contribute almost nothing.

That is the kind of finding that only comes from running a spec rather than reading it.

## Campaign two: where the firmographics were free

**1,225 confirmed organisations** — 540 hospitals, 449 banks, 236 credit unions. Spend about
$1.30.

**No paid firmographic enrichment was needed at all**, because all three sources publish real
employee counts. The banking regulator publishes them for banks, the credit-union regulator for
credit unions, and the healthcare agency for hospitals. **The headcount filter runs free at step
two instead of as a paid enrichment at step five.** That is the entire reason this campaign cost
a dollar thirty.

The gotcha, because it silently returns nothing: headcount lives on the financials endpoint, not
the institutions endpoint, which is where you would look first.

**The plan's asset band was mis-calibrated** and this was reported without changing anything.
Two-thirds of institutions in the plan's stated asset band have under 200 employees and fail the
plan's *own* headcount filter. The headcount filter does the real work; the asset band should
not be read as the ICP.

## The decision I escalated instead of resolving quietly

House rule is to drop leads behind the three hardest email security gateways.

On this account that is not a detail, it is a strategy decision, and the two campaigns sit at
opposite ends of it. Campaign one is roughly 25% gateway-fronted. **Campaign two is 60%** —
regulated industries buy email security by default. **If the founder rules them out, campaign two
drops from 1,225 to 489.**

The important part is *how* they were identified: sender-policy and autodiscover evidence proving
a Microsoft tenant sitting behind the gateway, **not by switching the drop rule off.** A gateway
mail record *masks* the tenant behind it, which means the house rule discards some of the
best-qualified prospects on a regulated list.

That was measured and put to the founder as a decision, rather than settled by whoever happened
to be writing the script.

## The classifier gap caught before a government send

The house mail-provider classifier had two holes that only matter on government-adjacent lists.

**It missed Microsoft's government cloud entirely.** The classifier covered the commercial mail
hostnames but government and defense tenants use a **separate top-level domain**. On this list
that silently misclassified **415 companies** and routed them into the wrong send batch.

**Two security-gateway signatures were missing** — one vendor's small-business product and one
acquired brand still running under its original hostname. Both fell into "other" and would have
been sent to as though clean. **142 companies on this one list.**

Government tenants are kept as their **own batch** rather than merged into the commercial one,
because their inbound filtering is far more aggressive and should not share warmup or send pacing.

Found **before** the government send, not after. That distinction is the whole value of it.

## The intent campaigns that did not work

Three campaigns depended on hiring signals scraped from applicant tracking systems. A shared
harness was built across six platforms, fully keyless once a job board is discovered.

| Campaign | Signal | Postings scanned | Companies found |
|---|---|--:|--:|
| One | platform rollout | 18,893 | **6** |
| Two | records/KM roles | 29,348 | **20** |
| Three | scanning overlay | — | **0** |

**The first failed structurally, and that is the more interesting failure.** The companies hiring
for that platform rollout are overwhelmingly *the partners who sell that platform's services.*
The signal fires on competitors. No amount of volume fixes it.

**The second failed on volume, not on logic.** The signal is sound — nobody sells that role as a
service, and only 2 of 24 sampled postings were consultancies. The arithmetic says it is
reachable: the signal appears on **6.7% of boards**, and the addressable board universe is roughly
37,000, projecting to **~2,470 companies** — above the plan's own estimate. The blocker is that
search engines sample site-scoped queries hard, returning three to ten usable rows regardless of
parameters, so *discovery* plateaus at a few hundred boards.

The better architecture, specified: take the 6,454 companies already qualified in campaigns one
and two, find each one's job board, and monitor only those. **Intent becomes an overlay on a
qualified base rather than a discovery mechanism.**

Two false-positive classes worth remembering: a same-named developer tool was the largest source
of noise in campaign one, and in healthcare, "imaging" and "scanning" mean radiology — which was
admitting 669 bogus postings into campaign three.

## The campaign revived by reading contracts instead of job posts

One campaign targeting organisations running twenty-year-old document systems was parked, because
the obvious signal does not exist: **job posts naming those four legacy platforms returned 0, 0, 3
and 16 across 48,241 postings.** Teams running a legacy platform do not hire for it. They hire to
get *off* it, in the destination platform's language.

Contract *descriptions* worked instead. Eleven platform aliases, contracts and delivery vehicles
as separate passes, keyless. **625 hits, 438 kept awards, 63 agency buckets.**

**Then the finding that reshaped it: every award recipient is a reseller.** The organisation
actually running the document estate is the **awarding agency**, not the company on the contract.
So the contact layer moved to agency records officers — a free source already built for another
campaign. Cost: **$0.00.**

Best false positive, and it is a good one: one vendor acquired another in 2023, so four unrelated
security and analytics products ride in on a keyword search for the parent's name.

## Why nothing has launched

**The infrastructure is built and warming: 100 connected inboxes across 50 domains, two per
domain — roughly 1,500 sends a day at full ramp.** 98 of 100 are still warming.

The blocker is an identity problem, not a technical one. **Every inbox is registered to one
person.** The approved copy set has a *second* person sending two of the campaigns. There are zero
inboxes for that second identity, and new domains plus warmup is a multi-week lead time. That is a
hard blocker on half the approved set and it was reported as one.

Worth recording: I had previously told the founder this account had no sending infrastructure,
because there was no credential in the environment file. **That was wrong — it was already built
and warming.** The correction is in the record.

## The transferable lesson

**Federal open data is a serious, free B2B data source and almost nobody in go-to-market uses
it.** Spending data gives contract *and subcontract* relationships. Securities filings give
acquisition dates precise enough to time an outreach window. Banking, credit-union and healthcare
regulators give real headcounts for every institution in the country — the exact firmographic
everyone otherwise pays a vendor for.

A 5,229-company, mail-confirmed, tier-segmented universe cost **$2.40.** The equivalent vendor
list is four figures a year and worse, because it does not know who subcontracts to whom.

The second lesson: **when a signal returns almost nothing, work out whether it is a volume problem
or a structural one before you try to scale it.** Two campaigns both returned single digits. One
was fixable and one was aimed at the wrong population entirely, and telling them apart saved a
month.
