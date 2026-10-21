---
layout: post
title: "Growing Junior Engineers When AI Does the Junior Work"
date: 2026-11-09
description: "The small, well-scoped tasks juniors used to learn on are exactly what AI does best. If we're not deliberate about it, we'll stop producing senior engineers. Some notes on what I'm trying."
tags: ["Leadership", "AI", "Career"]
---

I've mentioned this worry in my last few posts and a lot of you wrote back about it, so it seems worth a post of its own.

The short version: the tasks that used to turn junior engineers into senior engineers are the tasks AI is best at.

Fix this small bug. Add a field to this API. Write tests for this module. Wire up the new endpoint. For decades that was the on-ramp. You did a hundred small things, got some of them wrong, someone patiently explained why in code review, and slowly you built the instincts that make you good at the job. Now an agent can do most of those tasks in a few minutes, which is great for throughput and, if we're not careful, pretty bad for how we grow people.

## The risk isn't that juniors become useless

I see a lot of doom on this topic and I don't really buy it. Junior engineers with AI tools are more productive than junior engineers have ever been. They can ship real things in their first week.

The problem is that productivity and growth aren't the same thing. You can produce a lot of working code without ever building the judgment to know when it's wrong, and judgment is most of what makes someone senior. I wrote about this as [taste](/2026/10/taste-is-the-new-bottleneck/) a couple of weeks ago. You build it by being wrong, noticing, and remembering, and if the AI is never visibly wrong in front of you (or you never notice when it is), you don't build much of it.

The failure mode I worry about is five years from now: lots of engineers with five years of experience who can prompt fluently but have never really debugged anything hard, never designed anything from scratch, and never owned a system through a bad week in production.

## Learning happens in the struggle

There's a reason the old way worked, slow as it was.

If you spend two hours figuring out why a test is flaky, you don't just fix one test. You learn how the test framework handles setup and teardown, how the system deals with time, what a race between two goroutines looks like in the logs, and how to approach the next weird bug. Those two hours were the lesson.

AI removes a lot of that struggle, and most of the time that's a gift. For someone still building their mental models, though, some of the struggle is the point. I think our job as leaders is to work out which struggle is useful and protect it, and which is just friction we can safely remove. I don't always get that call right.

## What I'm trying on my teams

None of this is settled, and I'm still learning. But a few things have worked well enough to keep doing.

### Explain it or it doesn't ship

This is the rule I keep coming back to. If a junior engineer opens a PR with AI-generated code, they need to be able to walk the reviewer through it: why this approach, what happens if that call fails, why these tests are enough. It's not meant as a gotcha. It turns each PR into a small learning moment, and people start reading generated code a lot more carefully once they know they'll be asked about it.

### Real debugging, early, and real on-call

Debugging is the skill AI helps with least and teaches the most, so I route real bugs (especially the weird ones) to people who need to grow. Not alone, with a senior nearby, and with the expectation that the goal is understanding rather than just a fix. Same with on-call: shadow early, join the incident calls, read the COEs. Production is still a very good teacher and still mostly AI-proof.

### Design that's actually theirs

When juniors only ever implement someone else's design, they don't learn to design. So I try to hand them small design problems they own end to end: write the one-page plan, lay out the options, defend the choice. A senior reviews the thinking, not just the code. An agent can generate the implementation, but "why this and not that?" is much harder to outsource.

### A few reps without the tool

This one is a bit controversial and I don't use it much. Occasionally, for a learning task, I'll suggest doing it without AI first and then comparing the two versions. It's not a purity test, more like a musician practicing scales. The fluency sticks around even when you're mostly playing with a band.

### Pairing on purpose

Mentorship used to happen partly by accident, in hallway conversations and long review threads. With fewer small tasks and more async work, those accidents happen less, so it helps to pair people deliberately and ask seniors to narrate their thinking out loud during design and debugging. I wrote about the [three levels a mentor should operate at](/2023/01/3-levels-that-you-should-operate-at-as-a-mentor/) a while ago and all three still apply. The tactical one ("here's how to fix this") is the one AI increasingly covers; the other two, growing someone's judgment and their career, matter more than they used to.

## A note on hiring

Some companies are responding to all of this by hiring fewer juniors. I understand the math and I think it's a mistake. Every senior engineer you'll want to hire in 2031 is a junior somewhere today, and if the whole industry stops investing in the on-ramp, we'll all end up competing for a shrinking pool of experienced people.

Juniors also bring something seniors often don't. They're native to these tools and they'll find ways of working the rest of us won't, so it's worth letting them teach you something too.

It does cost something. A junior who spends an afternoon on a bug that an agent would have fixed in ten minutes is slower that day, and you'll feel it in the sprint. I've come to think of that afternoon as an investment rather than lost time, and so far it's been one of the better ones I make.
