---
layout: post
title: "Code Review Is the New Critical Path"
date: 2026-11-02
description: "AI made code generation fast and quietly turned review into the slowest, most overloaded step in delivery. Some thoughts on fixing that without lowering the bar."
tags: ["Leadership", "AI"]
---

I've now seen this pattern on more than one team.

The team adopts AI tooling and everyone gets faster at producing changes. The number of open pull requests goes up. Then, a few weeks later, the time it takes to get anything merged goes *up*, not down, and people are confused. We're writing code twice as fast, so why are we shipping slower?

Usually because the work didn't disappear, it moved. It's sitting in a review queue, waiting on the same three senior engineers who were already busy.

In the [last two](/2026/10/engineering-managers-in-the-age-of-ai/) [posts](/2026/10/taste-is-the-new-bottleneck/) I said the bottleneck moved from writing code to judging it. This one is the practical follow-up. If review is now the critical path, how do you run it like one?

## Review used to be a side job

For most of my career, code review was something you did between "real" work. You wrote code in the morning, reviewed a couple of PRs after lunch, and the ratio roughly worked out, because each engineer produced about as much as they reviewed.

That ratio doesn't hold anymore. One engineer with good tooling can produce far more change than one engineer can carefully review, and if you do nothing about it a few things tend to happen at once. Reviews get shallow: people skim, see green checks, and approve, and nobody ever decides to lower the bar, it just erodes. Your seniors drift into being full-time reviewers who stop designing and mentoring (and eventually, if it goes on long enough, start interviewing elsewhere). And the queue grows. Changes sit for days, merge conflicts pile up, and whatever speed you gained at the keyboard gets spent waiting.

None of this shows up on a dashboard labeled "review problem." It shows up as burnout, slow delivery, and a slightly mysterious rise in production incidents.

## Treat it as part of the system

The mindset shift is that review is the work, not overhead on top of it. Once you accept that, most of what follows is ordinary engineering applied to your own process.

### Small changes, again

AI will happily generate a 2,000-line change. That doesn't mean you should accept one.

Change size is probably the single biggest lever on review quality. Small changes get real reviews, and big ones get a skim and an "LGTM." I ask teams to keep the discipline they had before AI and, if anything, tighten it: one logical change per PR, refactors separate from behavior changes, generated boilerplate separate from the interesting part. A 1,400-line diff that's half generated mocks hides the 40 lines that actually matter.

The author's job is to make the reviewer's job easy. That was always true, it just matters a lot more now.

### Not every change deserves the same review

Treating a typo fix and a change to your billing logic the same way wastes everyone's time, so I like to be explicit about tiers. Docs, tests, internal tooling, and config with good validation can get a quick look, or sometimes automated checks alone. Most feature work gets a real review from someone who knows the area. Anything touching security, money, data deletion, customer-facing contracts, or deployment safety gets two reviewers, one of them senior, and an actual conversation about how it fails.

Write the tiers down. If they only live in people's heads, everything defaults to "normal," and normal slowly drifts toward skimming.

### Push the scrutiny upstream

The most expensive review is the one where you realize on line 800 that the whole approach is wrong.

For anything non-trivial I'd much rather see a short written plan before the code exists: the problem, the approach, what we considered and rejected, and how we'll know it works. Ten minutes on a half-page doc can save hours on code that shouldn't have been written. This matters more with AI, because producing the wrong thing is now cheap enough that people skip the "should we?" step entirely.

### Let machines catch what machines can catch

Humans shouldn't spend review time on formatting, obvious null checks, or a missing test for a new branch. Linters, static analysis, type checkers, coverage gates, and AI-assisted review tools can all take a first pass. I'd just be honest about what they're for. Automated review filters out noise so a human can focus on the questions that need one: is this the right design, what happens on the worst day, will we understand this in a year?

### Spread the load

If three people do 80% of your team's reviews, you have a single point of failure, and it's as much a people problem as a process one. What's worked for me is rotating a weekly "review lead" whose main job is keeping the queue healthy, pairing mid-level engineers with seniors on reviews until the mid-level can take the lead, and keeping an eye on review load per person. Not to rank anyone, just to notice when someone is drowning.

Reviewing well is a skill, and if only your seniors get to practice it, you won't end up with more seniors.

## What I look for now

When I review AI-assisted code, my questions have shifted. I spend less time on whether a given line is correct and more on whether it matches the intent, since models are good at solving a slightly different problem than the one you had. I look for what the change quietly added: an extra dependency, a new abstraction layer, a "helpful" try/catch that swallows the exact error you needed to see. Generated code tends to be generous, and generous isn't always good. I spend a lot of time on how it fails (timeouts, retries, partial failures, bad input), because the happy path is usually fine. And I check that the author can talk me through it, whoever or whatever typed it.

I'm also happy when a change is boring. Clever code is expensive to own.

## A note for managers

If your team's cycle time got worse after adopting AI, I wouldn't blame the tools or the engineers. Go look at the review queue first; in my experience that's almost always where the time went.

And protect your reviewers. **Count review as real work, in planning and in performance conversations.** If the only things that get recognized are the things people ship, nobody will want to do the work that makes shipping safe.

The teams that get the most out of AI probably won't be the ones that generate the most code. They'll be the ones that rebuilt how they review it, and it's a less glamorous project than adopting the tools in the first place, but I suspect it's the one that actually pays for them.
