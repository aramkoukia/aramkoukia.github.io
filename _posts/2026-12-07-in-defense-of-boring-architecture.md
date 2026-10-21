---
layout: post
title: "In Defense of Boring Architecture"
date: 2026-12-07
description: "When generating code is nearly free, it's tempting to build the clever, flexible, future-proof version of everything. Boring architecture is cheaper to own, easier to debug, and kinder to the people on call."
tags: ["Architecture", "Leadership", "AI"]
---

One of the best compliments I can give a design is "this is boring."

I mean it. Boring means I understand it in five minutes. It means the on-call engineer can debug it in the middle of the night without reading a wiki page first, and that two years from now, after the original authors have moved on, someone new can change it without being scared.

I've been thinking about boring a lot lately, because AI tools are very good at producing the opposite.

## The new temptation

Ask a model to design a system and you'll often get something impressive. Event-driven, a couple of queues, a caching layer, a plugin system "for extensibility," an abstraction over the database in case you want to switch later. Each piece is defensible. The whole thing shows up in seconds.

The cost of building complexity dropped to almost nothing, but the cost of owning it didn't move. Every component you add can fail, needs monitoring, needs someone who understands it during an incident, and needs patching, upgrading, and eventually migrating off. I think of complexity as a loan you pay interest on every day the system runs.

When complexity was expensive to build, that cost worked as a natural brake. People added a queue when they really needed one, because adding it was a week of work. That brake is mostly gone, so now we have to apply it deliberately.

## What I mean by boring

Boring doesn't mean old, and it definitely doesn't mean bad. Mostly it means well-understood technology, ideally something your team already operates well (the best database is often the one you already run). It means few moving parts, where every extra component has to justify itself. You should be able to sketch the data flow on a whiteboard in a minute and have a new hire follow it. When it fails, it fails in ways you've seen before and have a runbook for.

The hardest part is skipping speculative flexibility. "What if we need a second payment provider?" "What if traffic grows 100x?" Those feel like responsible questions, and sometimes they are. Most of the time, though, the flexibility you build for an imagined future never gets used, and in the meantime it makes today's code harder to read and change.

## Questions I ask in design reviews

I wrote about how I [evaluate a distributed system architecture in 30 minutes](/2025/11/how-to-evaluate-a-distributed-system-architecture-in-30-minutes/) last year. When it comes to complexity, a few of those questions do most of the work.

**What happens if we remove this?** For each component, ask what breaks without it. If the answer is "nothing yet, but maybe later," it probably doesn't belong in v1.

Who's going to operate it? Usually the answer is the same handful of people who already operate everything else, which means every new technology is one more thing they need to be good at during an outage.

What's the simplest version that would work, and why aren't we building that one? Sometimes there's a good reason. Often there isn't, and the conversation gets quiet for a second.

How does it fail? Clever systems tend to fail in clever ways: a cache stampede after a deploy, two consumers racing on the same message, a circuit breaker that never closes again. Boring systems tend to fail in boring ways, which are a lot easier to fix.

And can we add it later? A lot of complexity can wait until you actually need it and have real data about what "need" means. Deferring a decision is often the cheapest option on the table.

## "But we'll need it eventually"

Maybe. If you're confident you'll need something soon, and it's expensive to add later (a core data model decision, say, or how you partition data across shards), design for it now. That's not speculation, it's just good engineering.

If it's a guess, and it's reasonably easy to add later, I'd wait. Ship the simple version, learn from real usage, then evolve it. You'll make a better call with data than with guesses, and you won't have paid interest on the extra parts in the meantime. It's the same idea as [planning to build less](/2020/03/best-kept-secrets-of-product-development-plan-to-build-less/), applied to architecture instead of features.

## Where AI fits

I'm not saying don't use AI for design. I use it constantly. It's a good sparring partner: it lists options I hadn't considered, pokes at my reasoning, and sketches out tradeoffs faster than I can.

I just treat its suggestions roughly the way I'd treat a very well-read, very enthusiastic new hire. Lots of good ideas, not much feel for what it's like to own them for five years. My job is to keep the one or two that matter and politely decline the rest. One small thing that helps: tell the model up front to prefer the simplest approach, to avoid adding components unless they're needed, and to explain what each one is for. The answers get noticeably more boring, which is what I wanted.

## The people side

There's a team health angle to all this that I think gets overlooked. Complex systems concentrate knowledge. Only a couple of people really understand them, those people end up on every incident call, and that wears them down. It's a quiet but real reason good engineers burn out.

Simpler systems spread the knowledge around. More people can operate them and change them, on-call gets lighter, onboarding gets faster, and the team copes fine when someone goes on vacation. If you want a team that lasts, it helps a lot to build systems a normal person can keep in their head.

So in your next design review, it's worth being the one who asks whether this could be a bit more boring. It's not an exciting question, but in my experience it's one of the more useful ones.
