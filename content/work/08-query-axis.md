---
title: The buyer was buried until I changed the query axis
client: VIN IQ
year: 2026
onboarded: 2026-08-03
tag: Data acquisition
summary: Searching maps for "car dealership" buries franchise rooftops under used-car lots. Querying by manufacturer brand instead makes the platform do the classification for you, and its own type field becomes the franchise signal.
featured: true
metric: 6
metric_label: positive replies at 0.100%, against a 0.085% portfolio average
problem: The ICP bullseye was franchise dealer rooftops. Searching a metro for the obvious category buries them under dozens of small used-car lots, buy-here-pay-here operations and service centres, and no name-based filter reliably separates them.
system: Queried by manufacturer brand crossed with metro rather than by generic category: 20 brands across 78 metros in the nine best-fit states, roughly 1,560 queries, and read franchise status off the platform's own type field instead of guessing it from the business name.
output: A geo-fenced, deduplicated franchise universe with brand recorded per rooftop, and the half of the stated ICP that could not be honestly qualified from this source scoped out rather than shipped as guesses.
---


## The client

An automotive analytics platform sold at the **VIN level**, it tells a dealer whether a
*specific vehicle* actually got seen in advertising before they mark it down. $1,200 a month
per rooftop, month to month.

The ICP: US dealerships, franchise at any size or independents doing 50+ units, spending $10K+
a month on digital advertising, across nine best-fit states. Dealer Principal, Owner, General
Manager and General Sales Manager as the bullseye; marketing and digital directors secondary;
group executives for multi-rooftop groups.

The cold call to action is a free inventory blind-spot report, which is a genuinely good lead
magnet because it is a **demonstration** of the product rather than a description of it.

## The sourcing problem, and the field that solved it

Finding franchise dealers sounds trivial and is not. Searching maps for the generic category
in a metro buries the franchise rooftops, the ICP bullseye, under a long tail of small
used-car lots, buy-here-pay-here operations and service centres. Filtering that tail out by
business name is a losing battle.

**The fix was to change the query axis: manufacturer brand crossed with metro, not category.**
"Toyota dealer" at a given coordinate, rather than "car dealership".

And the insight that made it clean: **the platform's own `type` field is the franchise
signal.** A result typed as a given brand's dealer is, by the platform's classification, a
franchise rooftop. So brand is recorded from the type field and franchise status is *derived*
from it rather than inferred from a company name.

The run: **20 core manufacturer brands across 78 metros in the nine best-fit states**, roughly
1,560 queries, one page each. Geo-fenced by state code parsed from the address. Non-dealer
types dropped (service, repair, parts, rental, collision, used-car, truck, motorcycle, RV), plus a name-token blocklist for commercial-truck and powersports brands that share showroom
space. Deduplicated by place ID, then by root domain. Resume-safe.

**Independent dealers at 50+ units were deliberately excluded from this pass**, and the reason
is worth stating. Unit volume cannot be determined from a maps listing. There is no honest way
to apply the client's own 50-unit gate from this data, so those rows would have been
unqualified guesses. They were scoped as a separate pass against a different source rather
than quietly folded in.

Suppression was flagged at onboarding: the client supplied a do-not-contact list and a prior
active-contacts list, and both are deduplicated against every list before send.

## The shared classifier that lived in the wrong place

Worth recording because it matters beyond this account. The house mail-provider classifier, the code deciding whether a lead goes into the Microsoft campaign or the Google one, had its
**canonical copy inside this client's assembly script**, and was reused across every account.

Its two gaps, a missing government cloud and two missing gateway signatures, were found later
on a government-adjacent list and corrected there. The gaps did not matter on car dealerships.
They mattered enormously on federal contractors.

That is the argument for keeping shared infrastructure in a shared place: **a classifier living
inside one client's campaign folder gets tested only against that client's data.**

## The numbers

**6,021 sent, 74 unique replies at 1.23%, 6 positive at 0.100%, bounce 1.30%.**

| Campaign | Sent | uReply | Interested | Pos% |
|---|--:|--:|--:|--:|
| Single-rooftop franchise, Microsoft | 2,514 | 40 | **6** | **0.239%** |
| Single-rooftop franchise, Google & CMS | 2,051 | 27 | 0 | 0.000% |
| Dealer groups, Microsoft | 901 | 5 | 0 | 0.000% |
| Dealer groups, Google & CMS | 555 | 2 | 0 | 0.000% |

A small account. At **0.100%** it sits above the 0.085% portfolio average, and the
single-rooftop Microsoft split at **0.239%** is one of the better individual campaign results
in this set. Two observations, both held loosely because the sample is small.

**Single rooftops beat dealer groups**, six positives to zero across roughly triple the volume.
That is consistent with the product: a dealer principal at one store can decide to spend $1,200
a month. A group executive cannot, without a process.

**Microsoft outperformed Google here**, which inverts the pattern on two other accounts in this
portfolio. Dealers run heavily on Microsoft tenancy, and the Google split on this list is
disproportionately the small independents and vanity domains. A useful reminder that the
provider split is a **segmentation tool, not a rule** about which provider is better.

## What I would do differently

**Four campaigns, all paused, on a client wanting 15 leads a month.** The account never got the
send volume it needed to prove or disprove anything. 6,021 sends is not a test.

**The independent-dealer pass never happened.** It was correctly scoped out of the first run
and never scheduled back in, which leaves a chunk of the stated ICP unaddressed.

**Several onboarding questions stayed open**, size and revenue brackets, an unverified claim
in the client's own material, and the sending-domain decision. Open questions on a small
account are easy to leave open. They should have been closed at kickoff.

## The transferable lesson

**When a search returns the wrong population, change the query axis rather than the filter.**
Filtering a generic category down to franchise rooftops is a losing battle against a long tail.
Querying by brand makes the platform do the classification for you, and the type field it
returns is a cleaner signal than anything derivable from a company name.

The second, smaller one: **do not fake a qualification you cannot source.** The stated ICP
included independents at 50+ units. Unit count is not in maps data. Shipping those rows as
qualified would have been the easy call and the wrong one.
