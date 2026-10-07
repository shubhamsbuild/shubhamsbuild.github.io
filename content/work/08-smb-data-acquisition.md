---
title: 15 meetings from a list that did not exist
client: a CPA firm serving skilled trades
year: 2026
onboarded: 2026-07-07
tag: Data acquisition
sector: Skilled trades
summary: Eight trades built from map data, public directories and manufacturer dealer-locators. Nothing spent with list vendors, and four data problems caught before they reached anyone's inbox.
badge: Zero vendor spend
featured: true
metric: 15
metric_label: meetings from a list that did not exist
card: 60,000 companies from maps and registries, nothing spent.
problem: The firm sells to owner-operated trades businesses at $1M to $10M revenue. No vendor covers them, they exist in map data, business directories and manufacturer locators, in four inconsistent forms with nothing linking them.
system: Eight trades built from scratch, with a grid that subdivides itself where results are capped, a workaround for a site that blocks ordinary scraping, and manufacturer certification registers that carry email addresses directly.
output: Roughly 60,000 trade companies and 27,000 attorneys, 44 interested replies from 51,333 sends, and four data problems caught before sending, including 30% of a supposedly new list that had already been contacted.
---

| | |
|---|---|
| **Meetings booked** | **15** |
| Raw booking rows | 21 |
| Excluded: rows with no meeting time | 6 |
| Most recent booking | today |
| Trade companies built | **~60,000** |
| Attorneys | ~27,000 |
| Trades, from scratch | 8 |
| Spent with list vendors | **nothing** |
| Sends | 51,333 |
| Interested replies | 44 |

## The problem

The client is an accountancy firm selling to owner-operated trades businesses,
roofers, electricians, that kind of company, doing between $1M and $10M a year.

Those companies are not in B2B databases. They do not have LinkedIn pages, nobody
there has a job title worth filtering on, and the vendors that claim to cover them
mostly do not.

They do exist publicly, just scattered: in map listings, in business directories,
and in the "find a certified installer" pages that manufacturers publish. Four
different places, four different formats, and nothing linking a record in one to
the same company in another.

## How I approached it

Build it rather than buy it, and treat each source as its own problem.

**Maps return a capped number of results per search**, regardless of how many
businesses are really there. Search a dense city and you get the cap; search a
sparse county and you get everything. So the search grid subdivides itself, where
results come back at the cap, it splits that area and searches again; where they
come back short, it leaves it alone. The map tells you where to look harder.

**One source blocked ordinary scraping outright**, the kind of protection that
rejects anything not coming from a real browser. Getting past it needed requests
that look the way a browser's actually do, routed through ordinary residential
connections.

**Manufacturer certification registers turned out to carry email addresses
directly**, which removed a whole enrichment step for that trade, and cost nothing.

## The part that mattered most

Four data problems got caught before anything was sent. The one worth naming:

**30% of a list supplied as brand new had already been contacted.**

Nothing in the file said so. Sending it would have burned a third of that month's
new volume on people who had already said no, and the client would have seen a
collapsing reply rate with no explanation for it.

The checks that catch that are as much the deliverable as the 60,000 records are.
A list nobody verified is a liability that happens to look like an asset.

## What it did

**Roughly 60,000 trade companies and 27,000 attorneys**, built from public sources
for nothing spent with vendors, producing 44 interested replies across 51,333 sends.
