---
title: This site is one of the systems
layout: prose
---

Every number on this page is pulled from a live API, not typed from memory. So are the charts.

```
pull_bison.py     hits all 15 workspaces, writes a JSON snapshot
build_facts.py    turns the snapshot into a citable number sheet
build_charts.py   renders the exhibits as theme-aware SVG from that same snapshot
build.py          content + assets -> the static site you are reading
leakcheck.py      refuses the commit if anything private got through
```

Two parts of that are worth a sentence each.

**The charts are generated, not drawn.** When an account's numbers move, the exhibit moves with
them on the next build. There is no version of this site where the chart and the table disagree,
because they read the same file.

**`leakcheck.py` runs as a pre-commit hook.** These are a current employer's clients, so the site
is written anonymised by hand, I tried machine substitution first and it produced unreadable
prose and still missed a bare domain. The leak check is the net underneath: it scans the whole
published tree and fails the commit on any client name, named individual, client domain, API key,
email address, local filesystem path, or internal workspace or campaign identifier. It has caught
two real leaks so far.

The generator is about 300 lines of Python with no dependencies, including a small markdown
renderer, pulling in a library for six content files was not worth the supply chain. The
[source is on GitHub](https://github.com/iamdopecode).
