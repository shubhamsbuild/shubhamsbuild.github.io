---
title: One sentence about the first fold beat five about the store
client: WeConvert
year: 2026
onboarded: 2026-06-23
tag: Personalisation
summary: An AI agent reviewing a prospect's whole store produced five observations that fitted any store. Narrowing it to one weakness in the mobile first fold, quoting their real headline, is what made the output specific.
featured: true
metric: 88
metric_label: positive replies from 132,460 sends, at 0.81% bounce
problem: The account's flagship personalisation was a full store teardown. It failed because asking an agent to find problems with an entire store returns five vague observations that could have been written about any Shopify site, and prospects read them as a template, because functionally they were one.
system: Rebuilt the personalisation around a single verifiable observation: render the prospect's homepage at 390px mobile width, return exactly one weakness quoting their real hero text, and give the agent explicit permission to return nothing.
output: Roughly 80% send and 20% skip on live dry runs, with the skipped fifth routed to an offer that needs no personalisation at all, so no lead is wasted and nobody is told about a flaw the agent invented.
---


## The client

A conversion-rate-optimisation agency for DTC Shopify brands doing $100K+ a month. Their
entire pitch is that the first fold of a store makes or breaks cold paid traffic, so the
outbound had to demonstrate that claim, not assert it.

## The problem: personalisation that signalled nobody looked

The earlier flagship campaign was a **full store teardown**, an AI agent reviewing a
prospect's whole store and returning a list of conversion issues as the personalised opener.

**It failed, and it failed for an instructive reason.** Asked to find problems with an entire
store, the agent produced five vague observations that could have been written about any
Shopify site. Prospects read them as a template because functionally they were one.

The diagnosis: **a single sharp, verifiable observation beats five vague ones**, and the
generic version is worse than no personalisation at all, it actively signals that nobody
looked.

## What I built instead

The **first-fold teardown.** An agent renders the prospect's homepage at **390px mobile
width** and returns exactly one specific weakness, **quoting their real hero text.** That
sentence becomes the opener.

Narrowing the scope from "the store" to "the first fold at mobile width" is what forced
specificity. There is only one hero headline. The agent either has something concrete to say
about it or it does not.

Three implementation details carried the whole thing.

**Mobile rendering is not window resizing.** Resizing a desktop browser does not change the
render viewport, so a desktop-rendered "mobile" screenshot shows the desktop layout at a narrow
width. It needs a genuine mobile render, mobile user agent, real device emulation. Getting
this wrong produces confident observations about a layout the prospect has never seen.

**A skip path, and permission to use it.** Live dry-run hit rate was roughly **80% send, 20%
skip.** The agent skips when the fold is already strong, scoring at or above four, with
clarity, an offer and trust signals present. **It is explicitly forbidden from manufacturing a
nitpick**, because manufacturing nitpicks is precisely what killed the previous version.

**Nothing gets wasted.** Skipped leads route to a separate guarantee-led sequence, a
10%-lift-in-90-days-or-free offer that needs no personalisation at all. Every lead is touched,
and the fifth with genuinely good first folds get an offer that does not insult them by
inventing a flaw.

Manual QA ran on the first twenty AI rows before every launch, checking for sameness. The
finding must quote each store's actual hero text. If twenty rows read alike, the agent has
drifted back into templating and the campaign does not go out.

## The Slack bot

A related tool for the same client: a Slack command that returns conversion-optimised desktop
and mobile hero mockups of any e-commerce site, in thread, with the reasoning attached.

**It renders the prospect's actual product.** The scrape pulls the real hero or Open Graph
image, so the mockup shows *their* product in a better layout, not a generic template. That is
the difference between a mockup that gets a reply and one that gets ignored.

**It runs on no API key, by founder constraint.** The instruction was to use the existing
server rather than add a metered key, so the generator shells out to a local CLI in headless
mode on the same droplet and strips the API-key variable from the child environment so
subscription auth is used instead.

That is a small piece of engineering, but it is the kind that matters commercially: the
founder's constraint was a cost one, and the answer was an architecture that respected it
rather than a request to relax it.

## The numbers

**132,460 sent, 1,546 unique replies at 1.17%, 88 positive at 0.066%, bounce 0.81%.**

| Campaign | Sent | uReply | Interested | Pos rate |
|---|--:|--:|--:|--:|
| CRO audit angle | 9,615 | 127 | **10** | **0.104%** |
| Cheapest-revenue angle, 3rd batch | 8,713 | 177 | **7** | 0.080% |
| Page-speed angle, 3rd batch | 9,154 | 152 | 2 | 0.022% |

The pattern across the account is consistent: **offer-led angles outperformed observation-led
ones roughly four to one.** The page-speed observation is verifiable and specific and still
converted worse than simply naming the outcome.

That is a genuine tension with the first-fold work and it belongs in the write-up rather than
being smoothed over. The best reading is that **specificity earns the read and the offer earns
the reply**, and the first-fold campaign put its effort into only one of the two.

## What I would do differently

**The first-fold observation was never tested against a strong offer in the same email.** The
account's own data says the winning combination was available and never assembled.

**The 20% skip cohort was never measured separately.** Whether the guarantee fallback
outperformed the personalised path is knowable and was not checked, and given the pattern
above, it might well have.

**Re-runs were used heavily and decayed hard**, and that was not instrumented until late.

## The transferable lesson

**Narrow the scope of an AI personalisation task until the output has to be specific.**
"Review this store" produces five sentences that fit any store. "Look at the first fold at
390px and name one weakness, quoting their headline" produces one sentence that fits exactly
one store.

And the guardrail that makes it safe to run at volume: **give the agent permission to return
nothing, and route those leads somewhere useful.** An AI personalisation step without a skip
path is a machine that manufactures fake observations for the fifth of prospects who are
doing fine, which is the same fifth most likely to be worth talking to.
