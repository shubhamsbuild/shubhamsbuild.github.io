---
title: The best campaign in the account was 80% out-of-office
client: An automation agency
year: 2026
tag: Measurement
summary: Fifteen campaigns and no idea which worked. Every one of 315 replies was read by hand. The ranking inverted almost completely — and a campaign about to relaunch at 3x volume got stopped.
exhibit: exhibit-3-mx-split.svg
featured: true
metric: 80%
metric_label: of the account's best campaign's replies were out-of-office
problem: Fifteen campaigns, ten of which had sent, and nobody could say which had worked. The account was being steered by reply rate.
system: Found that every campaign counted auto-replies in its statistics. Read and hand-labelled all 315 inbound replies after automated classification scored an unsubscribe request as a positive, then re-ranked on positives per contacted.
output: The ranking inverted almost completely, and a draft with 6,838 leads queued, reusing copy that had gone 0-for-2,334, was stopped before it launched.
---


## The brief

Fifteen campaigns, ten of which had actually sent. Nobody could say which had worked. The
account had reply rates in front of it and no idea what they meant.

The deliverable: rank the campaigns by something real, and say why the losers lost.

## The finding

Every campaign in the account had auto-replies counted in its statistics.

That single setting means out-of-office messages and auto-responders are counted as replies.
The consequence, once you look:

**The best campaign in the account by reply rate — 6.6%, on a tax-advisory list — was 80%
out-of-office. 61 of its 76 replies.** It had produced exactly one genuine positive.

The metric everyone was steering by was measuring the recipients' holiday schedules.

**All 315 inbound replies were read and labelled by hand.** Automated classification was tried
and abandoned: it scored *"you can drop us from your mailing list"* as a positive. That is not a
tuning problem. Intent in cold-email replies is not carried by vocabulary, and a rules engine
reading for polite words gets it backwards.

One methodological note that made the audit possible at all: the replies endpoint is undocumented
but works, and it returns **both** folders — so inbound has to be filtered by excluding the sent
folder, or you end up analysing your own emails.

## The re-ranking

Ranked by **hand-labelled positives per contacted**, which is the only number that means
anything:

| Segment | Contacted | Replies | Reply % | **True positives** | **Positive %** |
|---|--:|--:|--:|--:|--:|
| Roofing (v1) | 403 | 4 | 1.0% | **2** | **0.50%** |
| Followers list | 721 | 15 | 2.1% | 2 | 0.28% |
| SEO list | 1,225 | 14 | 1.1% | 3 | 0.24% |
| Roofing (v2) | 1,094 | 39 | 3.6% | 2 | 0.18% |
| **Tax advisory** | 1,014 | 67 | **6.6%** | **1** | **0.10%** |
| Cold-email agencies | 1,587 | 18 | 1.1% | 1 | 0.06% |
| **Marketing agencies** | **2,334** | 37 | 1.6% | **0** | **0.00%** |

**The ranking inverts almost completely.** The campaign with the best reply rate is fifth by
positive rate. The campaign with nearly the worst reply rate is first.

Aggregated by vertical the picture is clearer still. **Roofing: 4 positives from 1,497 contacted,
0.27%. Agencies of any kind: 4 positives from 5,666 contacted, 0.07%** — four times worse. The
tax list produced one positive but it was the account's **only booked call.**

## Why the losers lost

**2,334 contacted, zero positives** on the marketing-agency campaign. Two causes, and they
compound.

**The list was broken.** Titles included things like *website partner and platform consultant*
and *board member*. Not buyers. Compare the tax list: president, CEO, owner, managing member at
small accounting firms — **every one a decision-maker.** Same sender, same infrastructure, and one
list is simply addressed to people who can say yes.

**The copy asked for nothing concrete.** The opening email named the tools it would use rather
than the outcome it would produce. Rejections came back on-message: some version of *that has not
been a problem for us, and we are perfectly capable of adopting these tools ourselves.*

And the structural finding, which is the one worth carrying:

> **Selling automation to agencies is selling to people who build automation.** They are the
> competition, not the buyer.

The replies said so directly. One respondent noted they could build the same thing themselves
with the same tools. Another sent two words. No rewrite fixes this — the ICP is wrong at the root,
and 5,666 sends went into finding that out.

**One campaign shipped a template placeholder.** The opening email body of a 1,587-lead campaign
was an unfilled copy token. That went to 1,587 people.

## The live risk

A draft campaign with **6,838 leads queued** was sitting ready to launch, reusing — verbatim — the
opening copy from the campaign that had gone 0-for-2,334.

That went into the post-mortem as a stop-ship, at the top, in bold. **The audit's most valuable
output was not the ranking of what had already happened. It was catching the thing about to
happen again at three times the volume.**

## The pattern that showed up twice

A related finding from a different account, which is why the exhibit above is on this page. One
insurance-agency list, split by the recipient's receiving mail platform, same copy and same
window: one half ran a 2.3% reply rate, the other **0.19%.** A **twelvefold gap on identical
copy.**

The same gap appeared independently in a third account's year-end review — one provider's
recipients at 0.4–1.6% against another's at 6–8%.

That is not a copy signal. It is a deliverability signal, it is invisible inside a blended number,
and it is the empirical basis for splitting every campaign by recipient mail provider and pacing
them separately.

## What I would do differently

**The auto-reply setting should have been checked on day one, not at post-mortem.** It is one
field. It invalidated every historical number in the account.

**Hand-labelling 315 replies does not scale.** It was correct at this volume, but the right build
is a classifier validated *against* a hand-labelled set — with the hand labels as ground truth
rather than as the product.

**The placeholder that shipped to 1,587 people should have been caught by a pre-send check.** A
single assertion that no email body contains a template token would have caught it, and costs
nothing.

## The transferable lesson

**Pick the metric before you read the numbers, and make sure it is one the recipient has to
consciously choose.** Opens are inflated by scanners. Replies are inflated by out-of-office.
Positive replies require a human to read your email and decide to answer it, which is exactly why
it is the only one worth optimising.

And the blunt one: **if your prospects can build what you sell, they are not prospects.** No
amount of copy iteration converts an audience whose objection is "I could do that myself" —
because they are right.
