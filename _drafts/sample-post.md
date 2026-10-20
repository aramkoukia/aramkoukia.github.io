---
layout: post
title: "Sample post: how your writing will look"
date: 2026-10-19
description: "Headings, code, quotes, lists, and tables, so you can check the theme before importing your real posts."
---

This is a throwaway post for previewing the theme. Run `bundle exec jekyll serve --drafts`
and open it from the home page. Delete this file when you're done; drafts never publish.

## Start with the failure modes

Most architecture reviews go wrong because they begin with the boxes instead of the
failures. Ask what happens when each dependency is slow, wrong, or gone, and the diagram
tends to explain itself.

> A system is only as reliable as its least-understood dependency.

### Questions to ask in the first ten minutes

- What is the blast radius if this service fails?
- Which calls are synchronous, and which could be queued?
- Where is state kept, and who owns it?

## Show the code

A retry with exponential backoff and jitter is a good first defense:

```python
import random, time

def call_with_retry(fn, attempts=5, base=0.2):
    for i in range(attempts):
        try:
            return fn()
        except TimeoutError:
            if i == attempts - 1:
                raise
            time.sleep(base * 2 ** i + random.random() * base)
```

## Compare the options

| Approach | Latency | Consistency |
|----------|---------|-------------|
| Read replica | Low | Eventual |
| Primary only | Higher | Strong |

That's enough to judge spacing, color, and code styling. See the [Jekyll docs](https://jekyllrb.com/) for more.
