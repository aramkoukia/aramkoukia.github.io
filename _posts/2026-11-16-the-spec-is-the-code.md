---
layout: post
title: "The Spec Is the Code: Why Writing Is Now a Core Engineering Skill"
date: 2026-11-16
description: "When an agent can turn a clear description into working software, the description matters a lot more than it used to. Some notes on writing as an engineering skill, and how I try to coach it."
tags: ["Leadership", "AI", "Product & Agile"]
---

A few months ago two people on my team asked an AI agent to build basically the same internal tool. Same agent, same codebase, same afternoon.

The first person typed one sentence. The second person spent about twenty minutes writing half a page: what problem the tool solves, who uses it, what it must never do, the edge cases they cared about, and what "done" looks like.

You can guess how it went. The first result technically worked and was wrong in five different ways. The second was close to shippable.

It wasn't about prompt tricks. The second person had actually thought about the problem first, and then wrote that thinking down.

## Writing used to be hidden work

I've worked at a place that runs on written documents for a long time, so I'm biased. But I've always believed that writing is thinking. If you can't write down what you're building and why, there's a decent chance you don't understand it yet.

The cost of fuzzy thinking used to be mostly invisible. A vague ticket went to an engineer, and the engineer filled in the gaps with hallway questions, a Slack thread or two, and their own judgment. The ambiguity got resolved by people, slowly, along the way, and nobody really counted it.

Now the vague ticket often goes to an agent, and the agent fills in the gaps with guesses. Plausible, confident, fast guesses. What comes back is a clean implementation of something slightly different from what you meant.

In my post on [engineering managers in the age of AI](/2026/10/engineering-managers-in-the-age-of-ai/) I said, almost in passing, that the spec is becoming the code. I've thought about it more since then and I'm more convinced, not less. Not literally, of course. But how clearly the problem is described now decides a big chunk of how good the output is.

## What goes in a good spec

I don't mean a 30-page requirements document. Most of the good ones I see are a page or two. They usually start with the problem in the customer's words (what's hurting, and for whom), and then say what success looks like in a way you could actually check. "p99 latency under 200ms for the search endpoint" is checkable. "Fast" isn't.

After that come the constraints that aren't up for negotiation: security, cost, backward compatibility with the clients still on the old API version, that kind of thing. Then the tricky parts, like what happens when the upstream service times out, or when the same request arrives twice. And finally an honest list of open questions.

There's one more section I care about more than all of those, which is **non-goals**: what we're explicitly not doing. It's the section people skip, and in my experience it saves the most time, because it's exactly the information an agent (or a new person on the team) needs to not wander off.

None of this is about AI, really. It's a normal design doc. The difference is that for small pieces of work it used to be optional, and now it's often the main input to the building.

## Why engineers push back

I get it. A lot of us got into software because we liked building things, not writing about them. Docs feel like overhead, and for years an engineer who was great at code and mediocre at writing did fine.

That's getting harder. When an agent can write a lot of the code, an engineer's leverage comes from understanding the problem, describing it precisely, and judging whether what came back is right. Two of those are basically writing and reading. I expect the engineers who get good at this to get a lot more out of the tools than the ones who don't, and I think we're already seeing it.

## How I coach it

You can't just tell people to "write better," any more than you can tell them to "code better." A few things have helped.

We review docs the way we review code, with real comments and real push back. A sentence like "the system should be fast" gets a comment asking how fast, measured how, for which requests. If docs never get serious feedback, people quietly stop putting effort into them.

I also go after weasel words. "Robust error handling." "Should scale." "Handle edge cases appropriately." These sound like content and say nothing, so I ask people to replace each one with something specific. Does "robust error handling" mean retry three times with exponential backoff, or fail fast and alert? Those are very different systems.

A trick I like: write the non-goals before the goals. It forces the scope conversation early, when it's cheap.

Specs should live in the repo, next to the code, and get reviewed when they change. The ones sitting in a wiki page from two years ago don't get read by anyone, human or agent.

And this one sounds silly, but read it out loud. If a paragraph is hard to say, it's probably hard to understand. (I'm trying to follow that here, with mixed results.)

## Managers write specs too

Most of what a manager produces is direction: goals, priorities, decisions, context. If mine is vague, the team either burns time figuring out what I meant, or builds the wrong thing quickly, and AI makes the second one a lot more likely.

So when I write a team goal now, I try to hold it to the same bar as a spec. What's the problem, what does success look like, what's out of scope, what are we unsure about. It's humbling how often I find out I don't actually have an answer until I try to write it down.

If I had to pick one skill to invest in over the next few years, as an engineer or as a manager, it would probably be this one. Learn to say precisely what you want before anyone, or anything, starts building it.

*If you have a spec template or a writing habit that works for your team, I'd like to see it. I'm on [LinkedIn](https://www.linkedin.com/in/aram-koukia/).*
