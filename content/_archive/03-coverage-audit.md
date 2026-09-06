---
title: An afternoon's audit killed the campaign's best angle
client: A performance-guaranteed PR firm
year: 2026
tag: Diagnosis
summary: Five versions of copy had been written around one assumption. A hundred-company sample showed it was true for 4% of the list, not 60%.
featured: true
metric: 4%
metric_label: of the list the hero angle actually applied to, against a projected 60%
problem: A PR firm's trial campaign had five versions of copy built on one assumption: that the prospect had no earned media coverage. The plan projected that as true for roughly 60% of the list.
system: Extracted a 5,002-company bot-walled list from the React fiber tree, resolved 93% of domains with a two-pass founder-disambiguated resolver, then ran a 100-company coverage audit against the real send list before writing version six.
output: 96% already had coverage, so the gap was tier and not existence. The campaign was rewritten diagnosis-led before a single send, and 446 competitor firms were excluded from the list.
---


## The account

A PR firm selling performance-guaranteed earned media — the client pays for placements, with
results in month one. It was a trial engagement with a specific shape: book quality logos
fast, convert to a retainer. A trial is judged on speed to first meeting, not on pipeline
built over a quarter.

The client arrived with their own go-to-market playbook as a written document. **That document
was the plan.** I did not author a replacement, which was the right call and worth saying out
loud — a client who has done the thinking deserves to have it executed, not overwritten.

## Getting the list

The target audience was a well-known annual list of 5,000 fast-growing US companies. That
list is not downloadable.

The site is behind a commercial bot-detection product. Direct requests return 403. The old
REST endpoint that used to serve the data is dead. Neither of the usual escape hatches worked
either — the dataset is not in the page's server-rendered props and not in its streamed
payload.

What worked: open the page in a real browser so the challenge clears itself, then read the
data out of **the React fiber tree.** Take any table row, read its fiber property, and walk up
roughly seven parent hops checking the memoized props and state at each level for an array of
5,002 company objects. Export via an in-browser blob download.

The fiber payload is richer than the rendered table: industry, real revenue figures, employee
count, founding year, growth rate, city, state, revenue band, rank — and **leadership names.**

One field is absent for every row: **website.** So a second pass resolved domains across all
5,002 via a search API, about 6,800 queries in 24 minutes.

**The resolver is the part I would defend in an interview.** Two passes. First the company
name with city and state. Then, only for rows not already high-confidence, the company name
with the *founder's name* from the leadership field — because a founder's name disambiguates
generic company names, and that second pass is what corrected several one-word brands to their
real domains.

The accuracy rule that matters: an exact match, an affix match, and a domain-contains-company
match are all strong. *Company name buried inside a longer domain* is weak and routes to
review rather than acceptance. A "high" verdict requires a strong match plus at least one
independent corroboration. **The resolver never emits a non-matching guess. It emits a blank.**

Result: **93% domain fill**, tiered to 1,569 core-ICP and 1,501 borderline, with 1,932
excluded — including 446 advertising and PR firms, which would have been an own-goal for a PR
firm's outbound.

## The audit

Every copy pack for this campaign — versions one through five — was built around one line, in
various phrasings: *I could not find a single earned feature on you.* The plan projected that
as true for roughly **60%** of the list.

Before writing version six, I tested it. A random sample of 100 companies from the actual send
list, news search per company, every result classified by outlet type.

| Coverage state | Share |
|---|--:|
| Trade press only | 40% |
| Local press only | 30% |
| **Already tier-one** | **26%** |
| Wire only | 1% |
| Genuinely invisible | 3% |

**96% of the list already had editorial coverage. The gap was tier, not existence.**

The campaign's hero angle was addressable to **4% of the list, not 60%** — and actively harmful
on the 26% who already had tier-one coverage, because "you're invisible" is *factually false*
to a quarter of recipients and burns the sender the moment they read it.

The consequence was a rewrite, not a tweak. Copy became **diagnosis-led**: four different
emails routed by the recipient's actual coverage state, rather than one angle asserted at
everybody.

## Two gotchas that generalise to any enrichment job

**Name collisions are lethal.** A legal-tech company whose name is a common bureaucratic phrase
returns government bulletins. An apparel brand whose name is also a song title returns the
song. An identity gate is mandatory before any observation is merged into copy — because the
failure mode is not an empty variable, it is a confidently wrong sentence in a cold email.

**Ranking-list syndication is not coverage.** "Ranked No. X on the list" reappears via a dozen
aggregators, regional business journals and foreign wire services. It has to be classified as
syndication and never cited as a placement, or you congratulate someone on press they never
earned.

## The copy rules

Guarantee in email one. Named outlet and named angle in every email. Founder-led voice, A/B
across the two principals. Three touches, under 65 words each.

Two course corrections landed mid-engagement and both were right:

**Outcome before mechanism.** Prospects do not care how the machine works until they care
about the result. The mechanism moves to email two, where "yeah but how" actually gets asked.

**Press on the problem harder than anything else.** This killed the compliment opener outright
— congratulations lines are the most pattern-matched sentence in a saturated inbox. Open on
the pain, ideally a test the reader can run on themselves in ten seconds. The identity line
lands *after* the problem, as its answer.

## The numbers

**1,878 sent, 32 unique replies at 1.70%, 2 positive, bounce 0.91%.**

Both campaigns launched late and are early. That is a genuinely small sample and I quote it as
one. The real deliverable on this engagement was the list and the audit, not the send.

## What I would do differently

**The audit should have run before copy pack one, not before pack six.** Five versions of copy
were written against an unvalidated premise. The audit cost an afternoon. The copy cost five
rounds.

**Contacts were never finished.** The source carried founder names, but per-title email
enrichment never got built, so the actual send universe was far smaller than the 2,744 rows
that were ready at the company layer.

**Half the stated geography was never sourced.** The ICP covered two countries; the list
source covers one.

## The transferable lesson

**Validate the premise of a campaign before you write copy against it — and validate it on a
sample of the actual send list, not on intuition.** A hundred companies and one afternoon
falsified an assumption that had survived five copy revisions and was about to go to 2,744
people, a quarter of whom would have known immediately that it was wrong about them.

The cheapest thing in outbound is the audit you run before the send. The most expensive is the
one you run after.
