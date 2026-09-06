---
title: The list source was worth 9.1x the copy
client: BlackTern Capital
year: 2026
onboarded: 2026-07-01
tag: Measurement
summary: One client, one offer, the same warmed inboxes and the same sending window. Only the list source changed. It moved the positive-reply rate by a factor of 9.1.
exhibit: exhibit-1-list-source.svg
featured: true
metric: 9.1x
metric_label: lift in positive-reply rate over the incumbent data vendor
problem: An investment bank's outbound was qualified on headcount, which is the wrong gate for a firm that sells on revenue and raise size. Three list sources were running and nobody could say which was working.
system: Mined 13,011 positive replies out of a sister account's sending platform through an undocumented API parameter, rebuilt them into an 11,497-lead intent list carrying each person's original reply, then held offer, copy and inboxes constant and varied only the source.
output: 0.482% positive rate against 0.053% for ZoomInfo and 0.089% for Clay, across 155,403 sends. The account became the highest-converting in the book.
---


## The client

A boutique investment bank raising growth capital (equity, debt, private credit,
structured) in the $5M to $100M+ range, for revenue-generating founder-led and mid-market
companies. Senior advisors out of four bulge-bracket banks, with cumulative transaction
volume in the hundreds of billions behind them. The offer is a free 30-minute capital
strategy session.

**The ICP as written on the onboarding form was wrong in a specific, expensive way.** It
described the target by headcount. An investment bank does not care how many people a
company employs; it cares about revenue and raise size. A 20-person SaaS company at $12M ARR
seeking $20M is a perfect fit. A 300-person logistics firm at $8M is not.

I re-cut the gate to **revenue of $5M+ and raise size of $5M+**, industry-agnostic with a
priority tilt toward B2B SaaS, healthtech, AI, fintech, cybersecurity and logistics tech.
That change turned qualification from something you can filter for in a list tool into an
enrichment step, which is the whole reason the experiment below was worth running.

It is also a **regulated engagement**. Securities-adjacent copy cannot promise a raise will
close, cannot promise returns, and does not quote fees. Every angle had to carry the
authority without implying an outcome.

## The problem

The client arrived with a shortcut already in mind. He had been told we ran a similar motion
for another capital-markets account, and his instruction was: *model my campaign on theirs.*

That was a useful instruction and a trap at the same time. Copying the other account's copy
was the obvious reading of it. What actually made that account work turned out to be
somewhere else entirely.

## What I did

The sister account ran on its own instance of the sending platform. Scale: 505 campaigns,
3.1 million leads, 498,000 replies. Sitting inside it was the thing nobody had asked for, **every prospect who had ever raised a hand to a capital-markets pitch.**

The platform's API has no documented way to filter replies by disposition. It does have an
undocumented status parameter on the replies endpoint. Fixed page size of 15, roughly nine
seconds per page, so a naive serial pull is a multi-hour job. Parallelised, it became
something you could run over lunch.

**Output: 13,011 interested replies, 11,497 unique leads, spanning fifteen months.**

Not just names. Each row carried the lead's name, title, company, the cleaned text of what
they had actually replied, the campaign that produced it, and 24 custom-variable columns
holding industry, employee count, funding stage, and the personalised lines that had been
sent to them originally.

That last part is what made it a *list* rather than an export. Every row came with the
evidence of why that person had responded, and to what.

Then I ran it as a proper experiment. Same client, same offer, same warmed inboxes, same
sending window, same regulated-copy constraints. **The only variable was where the list came
from.**

## The result

| List source | Campaigns | Sent | Replies | Positive | Rate |
|---|--:|--:|--:|--:|--:|
| **Mined positive-repliers** | 6 | 54,803 | 1,823 | **264** | **0.482%** |
| Clay-sourced | 8 | 55,949 | 476 | 50 | 0.089% |
| ZoomInfo-sourced | 4 | 38,030 | 195 | 20 | 0.053% |
| Prospeo-sourced | 28 | 2,862 | 23 | 1 | 0.035% |

**The mined list beat ZoomInfo by 9.1x and Clay by 5.4x on positive rate.** It also beat them on raw reply rate, 3.22% against 0.51% and 0.87%, which matters,
because a lift that appears only in the positive flag can be dismissed as triage bias. A lift
that shows up in raw replies too means the audience is genuinely responding differently.

Across the whole account: **155,403 sent, 2,695 unique replies, 425 positive.** At 0.273%
that is roughly three times the blended average across the thirteen accounts I ran.

## The part that undercuts my own headline

An earlier, smaller high-intent batch of three campaigns, run before the mined list existed,
at **2.332%** on 3,474 sends. Five times better than the scaled version of the same idea.

So the honest conclusion is not "intent lists are 9.1x better." It is:

> **Intent quality decays as you scale it.** The first 3,000 rows of a hand-tight intent list
> convert at 2.3%. Stretch the same idea across 50,000 sends and it settles at 0.46%. Still a
> large multiple over cold, but the decay is real, it is steep, and anyone forecasting off
> the pilot number will miss badly.

I would rather say that than have someone find it in the table themselves.

## What I would do differently

**I never A/B tested copy inside the winning segment.** Once the list source proved out, all
four campaigns ran essentially one message. There is an unmeasured amount of headroom sitting
there.

**The 24 custom-variable columns went mostly unused.** I had funding stage, industry, and each
person's original stated situation in hand, and personalised off very little of it.

**Recency was never modelled.** A hand raised fifteen months ago and one raised last month
were treated identically. Segmenting by reply age is an hour of work and would likely explain
a meaningful slice of the decay above.

## The transferable lesson

Everyone in outbound argues about copy. Here, holding copy constant and moving only the list
source produced a larger swing than any copy test I ran on any account all year.

The reusable move is not "mine your replies." It is that **the highest-intent list a company
owns is usually already sitting inside its own sending platform, unqueried**, and it takes
an undocumented API parameter and an afternoon to get it out. Most teams buy a third list
before they have read the two they already have.
