---
layout: post
title: "Taste Is the New Bottleneck"
date: 2026-10-26
description: "When code is nearly free to produce, the scarce thing isn't typing or even reviewing. It's taste: knowing what good looks like and why. Some notes on the one skill AI made more valuable, not less."
---

A few weeks ago I watched two engineers solve the same problem with the same tool in the same afternoon. Same model, same prompt quality, roughly the same experience on paper. One of them shipped something clean, boring, and correct. The other shipped twice as much code that technically worked and that I did not want anywhere near production.

The tool wasn't the difference. The taste was.

I keep coming back to this because it reframes a lot of the anxiety floating around right now. We spent the last couple of years asking "will AI replace engineers?" I think that's the wrong question. The better one is: *when everyone can generate working code in seconds, what's actually scarce?* And the answer, increasingly, is taste. The judgment to look at ten plausible options and know which one is right, and to be able to say why.

⸻

## What I mean by taste

Taste is a fuzzy word, so let me be concrete. On an engineering team, taste is the thing that lets someone:

- Look at a working solution and feel that it's wrong anyway.
- Choose the boring design over the clever one, on purpose.
- Know which 20% of the edge cases actually matter and which are theater.
- Tell the difference between code that passes the tests and code that's actually correct.
- Delete three of the four things the model offered, and keep the fourth.

It's not style. It's not bikeshedding about tabs and semicolons. Taste is calibrated judgment about what *good* looks like in a specific context, built from having shipped things and watched them break. It's the compressed memory of every bad 3am page you ever got.

For a long time, taste was a nice-to-have on top of the real skill, which was building the thing. Now the building is cheap, and the taste is the whole game.

⸻

## Why the bottleneck moved here

In my [last post](/2026/10/engineering-managers-in-the-age-of-ai/) I argued that writing code got cheap while knowing what to build didn't. Taste is the sharp edge of that same idea, and the data is starting to back it up.

The Faros AI 2026 engineering report, built on telemetry from 22,000 developers, found that under heavy AI adoption, code churn — lines deleted relative to lines added — jumped 861%. Pull requests merged with no review at all, human or automated, were up over 30%. Not because anyone decided review didn't matter. Because the volume outran the humans.

That's the whole story in one statistic. Generation became free. Verification did not. And verification is mostly taste wearing a work badge.

People call this the "senior engineer tax": the output looks clean, the tests are green, and buried inside is a misread requirement or a quietly wrong edge case that only an experienced person catches. The model is very good at producing code that *looks* right. Knowing whether it *is* right is a different muscle, and AI didn't give us more of it. It just made us need it on ten times the surface area.

⸻

## The trap: mistaking volume for progress

Here's where I watch good teams go wrong.

AI makes it feel incredibly productive. You open twelve PRs in a day. The graphs go up and to the right. Everyone feels fast. And three months later you're drowning in a codebase nobody fully understands, because the constraint was never how much you could produce. It was how much you could responsibly keep.

A team without taste and with great tools doesn't ship better software. It ships more software, faster, in more directions, and then spends the next two quarters paying for it. I've seen it. The acceleration is real. So is the mess at the end of it if no one is applying judgment at the gate.

The uncomfortable version of this: the same tools that made writing free made reviewing harder. Bigger diffs, more of them, less local understanding per change. If your team's only answer to that is "review faster," you're going to lower the bar without ever deciding to.

⸻

## So where does taste come from?

This is the part that worries me as a manager, because taste has always been built the slow way: by building things, shipping them, and then owning the consequences. You develop taste by being wrong in production and remembering it.

But the small, well-scoped tasks that juniors used to learn on are exactly the tasks AI now does best. If we're not deliberate, we get a generation that can prompt fluently and generate endlessly, but never built the internal "that smells wrong" detector, because they never sat with their own bad decisions long enough to feel them.

Taste doesn't download. It accrues. And right now the industry is quietly removing the on-ramp.

⸻

## What I'm actually doing about it

Opinions are easy. Here's what this looks like in practice on my teams.

**Make the standard explicit and put it in the repo.** The most durable form of taste isn't in someone's head — it's written down where the code lives, as review guidelines, lint rules, and design principles under version control, right next to the thing they govern. If "good" only exists in your senior engineers' instincts, it doesn't scale and it walks out the door when they do.

**Review intent, not just output.** The highest-leverage review question is no longer "is this code correct?" It's "was this the right thing to build, and do we understand it?" Move the scrutiny upstream to the spec and the design, where a ten-minute conversation saves a thousand lines.

**If you can't explain it, it doesn't ship.** Simple rule, especially for AI-generated changes. You don't have to have typed it. You do have to be able to walk me through why it's correct and what happens on the worst day. This single rule does more to build taste than any training program I've tried.

**Protect the learning reps.** Deliberately route some debugging, some on-call shadowing, some design work to the people who need to build judgment — even when the AI could have done it faster. The speed you give up is tuition. Pay it on purpose.

**Hire and promote for it.** The interview question that matters now isn't "can you write this function." It's "here are three working solutions — which one would you ship, and why?" Watching someone reason about tradeoffs tells you more than any whiteboard syntax ever did.

⸻

## The part that's actually good news

I want to end somewhere other than doom, because I'm genuinely optimistic about this one.

For years, taste was underpriced. We rewarded the people who typed the most, closed the most tickets, produced the most visible output. The quiet engineer with impeccable judgment, who prevented ten disasters you never saw and shipped half the lines of everyone else, was chronically undervalued because their best work was invisible.

That era is ending. When anyone can generate, the person who knows *which* generation to keep becomes the most valuable one in the room. Judgment is finally getting repriced to what it was always worth.

Taste was always the job. AI just made it impossible to pretend otherwise.

⸻

*If this resonated, I'd love to hear how your team is thinking about it — come find me on [LinkedIn](https://www.linkedin.com/in/aramkoukia/).*
