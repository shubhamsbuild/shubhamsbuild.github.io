---
title: The list that ignores job titles
client: a B2B selling to founders and creator teams
year: 2026
onboarded: 2025-03-10
tag: Data acquisition
sector: Creator tooling
summary: A list built continuously from people who reacted to a post, feeding four sender accounts. Its audience is deliberately scattered across job titles, and that scatter is the proof it is working.
badge: Signal against cold
featured: true
metric: 31 vs 4
metric_label: interested, from engagement against cold
card: 307 connections out-pulled 775, same account and window.
problem: The account ran title-filtered lists at volume. A filter finds people who resemble the customer. It cannot find people who are in the market this week, because interest is not a field anyone sells.
system: A continuous scrape of people who reacted to a relevant post, feeding four sender accounts, plus a job-posting list on email, run against the account's existing cold campaigns in the same window, through the same senders.
output: 31 interested from 307 connections built on engagement. The cold campaigns, at two and a half times the volume, returned 4 from 775.
---

| Source, same account & window | Campaigns | Sent | Interested |
|---|---|---|---|
| Built from engagement | 5 | 307 | **31** |
| Cold, title-filtered | 4 | 775 | **4** |
| The reactor system alone | 4 senders | 249 | **28** |

| LinkedIn | | Email | |
|---|---|---|---|
| Connections sent | 2,874 | Emails sent | 9,301 |
| Accepted | 656 | Leads contacted | 7,959 |
| Conversations started | 575 | Unique replies | 66 |
| Replies | 105 | Marked interested | 27 |

## The problem

The account was buying lists the normal way: pick the job titles, pick the company
sizes, send to everyone who matches.

That finds people who **resemble** the customer. It cannot find people who are
thinking about the problem this week, because no database has a column for that,
and nobody is going to sell you one.

## How I approached it

If interest cannot be bought, it has to be observed. People leave traces of what
they are paying attention to, and the clearest one on LinkedIn is simple: they react
to a post about it.

Someone who liked a post about the exact problem this product solves has told you
something a job title never will. It is public, it is dated, and it happened this
week.

## What I built

A scrape of those reactions that runs **continuously**, feeding four different
sender accounts, rather than a batch somebody assembles once a month.

That difference matters more than it sounds. A batch is a thing you built and then
start using up. This one has new people in it tomorrow whether anybody touches it
or not, it is a machine, not a list.

On email, a second signal: companies posting job ads. A company advertising for a
role has a gap and a budget, and the ad is public, so you can mention it without
being creepy about where you got it.

## The counter-intuitive part

I deliberately did almost no filtering on top.

When I audited who was actually in these campaigns, the job titles were all over
the place, operations, marketing, engineering, at companies with nothing obvious
in common. That looks like a mistake. It is the opposite: it is the proof the list
is built on behaviour. A title filter returns page after page of near-identical
titles, which is exactly what this account's cold lists do.

Filtering the engagement list by seniority would have thrown away the only signal
that put anyone on it.

## What it did

**31 interested replies from 307 connections**, against **4 from 775** on the cold
lists, same account, same weeks, same sender accounts. Two and a half times the
volume returned an eighth of the result.

## What broke

Scrapes that run continuously drift. People who engage a lot keep re-entering the
list, so without a check you contact your best prospects over and over, the fault
lands hardest on exactly the people you least want to annoy.

Four retired campaigns sit in the account, renamed rather than deleted, marking
where that was caught and fixed.

## The honest limit

The wording was not held identical between the two groups, so this compares *list
built from engagement plus its copy* against *cold list plus its copy*. It shows
the combination is worth roughly an order of magnitude. It does not isolate the
list on its own.

*Figures from the sending-platform API, 2026-09-26. This account is not on the
client-facing dashboard, so no meeting count exists for it.*
