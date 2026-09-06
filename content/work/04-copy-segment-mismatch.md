---
title: Byte-identical copy. One audience converted, one returned zero.
client: InterviewFocus
year: 2026
onboarded: 2026-06-26
tag: Diagnosis
summary: A 79,000-send account was running at half its target. The instinct in the room was to buy more market. Two campaigns running the same bytes said otherwise.
exhibit: exhibit-2-copy-segment-mismatch.svg
featured: true
metric: 0
metric_label: positives from 4,422 sends, and the reason why
problem: An 86,290-send account was hitting half its positive-lead target. Reply rate was the highest in the book and bounce was clean, so the instinct in the room was to buy more addressable market.
system: Ruled out triage bias by hand-sampling 375 replies, then found two campaigns running byte-identical copy to different audiences: an accidental controlled experiment sitting in the account. Split all volume by title bucket to find the second lever.
output: Isolated a copy/segment mismatch rather than a list or infrastructure problem, and showed that a 4,200-account market expansion was worth three extra positives per cycle against a copy rewrite worth far more.
---


## The account

AI mock-interview software that scores both content and delivery, face tracking, eye
contact, speech pacing, filler words. The delivery half is the real differentiator; no
competitor in the set does it.

Two cold-addressable segments: higher-education career services at small professional schools
plus athletic departments, and private and boarding school college counsellors. Target of 20
positive leads a month. The account needed entirely new sending infrastructure, from zero.

## The state I found it in

**86,290 sent. 2,780 unique replies at 3.22%. 75 positive at 0.087%. Bounce 0.62%.**

The reply rate was the highest of any account I ran. Deliverability was not the problem. The
client wanted 20 positives a month and was getting roughly half.

Before blaming the copy I ruled out the cheap explanation. **Triage was not the gap.** I
sampled 375 replies, of which 129 were genuine human inbox replies, and found *zero*
positive-signal replies left untagged. The human reply mix was roughly 37% hard decline,
0.8% positive. The copy genuinely was not converting.

## The finding

Two campaigns in the account were running **byte-identical copy.**

| Campaign | Audience | Sent | Replies | Positive |
|---|---|--:|--:|--:|
| Look-a-likes | higher-ed career centres | 9,244 | 800 | **18** |
| Admin titles | private K-12 administrators | 4,422 | 195 | **0** |

Same bytes. One converts. One returns zero across 4,422 sends and 195 replies.

The shared email opens on the recipient's *career centre* and proves with a college
**athletics** case study. **A K-8 head of school has no career centre and no use for a college
athletics reference.** The recurring reply said so almost verbatim, some version of *our
existing career-and-technical program already has a community partnership, they have
everything covered.*

That is not a copy-quality problem. It is a copy/segment mismatch, and it was only visible
because the two campaigns were identical. An accidental controlled experiment had been
sitting in the account for weeks and nobody had read it as one.

## The second lever

Splitting all account volume by the title bucket it was addressed to:

| Title bucket | Sent | Positive | Rate |
|---|--:|--:|--:|
| Career-readiness / career-centre | 19,784 | 30 | **0.152%** |
| Administrator | 24,950 | 18 | 0.072% |

Career-readiness titles converted **2.1x better**, and administrator titles were taking 56%
of total volume.

Three more findings fell out of the same pass. The lead magnet, a free simulated mock
interview and a two-minute demo, appeared in **zero live calls-to-action**; every one was a
cold meeting ask. The "we're already covered" objection was never pre-empted anywhere in the
sequence. And the delivery-scoring differentiator, the one thing no competitor had, was
buried mid-paragraph.

## The call that cost the client money and saved them more

When positives were low, the instinct was to buy more addressable market. That is how a
Canadian universe of 4,193 accounts got built.

Canada adds roughly 10–15% to a ~29,000-account US base. At the account's measured positive
rate, that projects to **three or four extra positives per cycle.** Fixing one campaign's copy
was worth more than the entire build.

I built Canada because it was asked for, then put the arithmetic in writing. More market does
not fix a conversion problem, and a bigger list is the most expensive way to avoid rewriting
an email.

The Canada work did produce something worth keeping, a set of five ways a US school scraper
is silently wrong north of the border. Quebec schools are not called "high schools." An
accented search token does not match its unaccented form, which cost 47 of 48 institutions on
the first run. Publicly funded Catholic school boards are not private schools, which
mislabelled 358 of them. And a shared web domain means "one institution, many campuses" in
higher education but "many schools, one school board" in secondary, collapsing on it
destroyed 589 real accounts.

None of those failed loudly. Each one produced a plausible list that was badly incomplete.

I also flagged the thing that stops it shipping at all: **Canada's anti-spam law is stricter
than CAN-SPAM**, with penalties into eight figures, and the account had no handling for it.
Nothing sends north of the border until the client signs off.

## What I would do differently

**The zero-positive campaign should have been caught before it sent, not 4,422 emails later.**
The check is trivial: does the audience named in this campaign actually have the thing the
copy assumes they have? I built the audit that found it. I should have built the gate that
prevented it.

**The title-mix skew ran for weeks unmeasured.** More than half of volume went to the
worse-converting bucket and nothing surfaced it until someone went looking.

**The lead magnet never made it into a CTA.** That is an execution failure, not an analysis
one, the asset existed the entire time.

## The transferable lesson

**Deliverability, market size and conversion are three different problems that fail at three
different points in the funnel.** This account had an excellent reply rate, a clean bounce
rate, and a positive rate at half target. Every instinct in the room said *get more leads.*
The data said the copy was addressed to the wrong people.

The diagnostic that settled it is also the standard take-home format for this job: find the
one place where a single variable differs, and read what it tells you.
