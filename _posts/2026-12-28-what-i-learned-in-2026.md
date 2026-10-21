---
layout: post
title: "What I Learned in 2026, and What I'm Betting On for 2027"
date: 2026-12-28
description: "A look back at leading engineering teams through the AI shift: what held up, what I got wrong, and a few bets for the year ahead."
tags: ["Leadership", "AI"]
---

The last week of the year is the only week my calendar is quiet enough to think, so I'm going to use some of it to look back.

Since I picked the blog back up this fall, I've mostly written about one question from different directions: what happens to engineering leadership when writing code gets cheap? If you've been reading along, thank you. If you just found this, it works as a rough index to the rest.

## What held up

At the start of the year I assumed the main effect of AI would be that teams go faster. That was about half right. Teams did get faster at producing code, and then the work piled up somewhere else: in [code review](/2026/11/code-review-is-the-new-critical-path/), in testing, in deployments, and in the older question of whether we were building the right thing at all. Each time we cleared one of those, the next one showed up. If I had to compress the year into one habit, it's going and looking at where work is actually sitting and waiting, because it's rarely where it was last quarter.

The idea I'm most confident about is the one I called [taste](/2026/10/taste-is-the-new-bottleneck/). When anyone can generate working code, the scarce thing is knowing which version to keep and being able to explain why. It ended up changing how I review, how I interview, and how I [think about performance](/2026/12/telling-great-from-good-when-everyone-ships-a-lot/).

I didn't expect writing to matter as much as it did. Teams that wrote clear specs and design docs got far more out of the tools than teams that didn't, which is what [the spec is the code](/2026/11/the-spec-is-the-code/) was about. In hindsight this probably should have been obvious, since a vague description gets you a vague result whether a person or a model is reading it.

And most of the job didn't change at all. Ownership, clear goals, growing people, honest feedback, keeping production healthy. More change going out means [more chances to break things](/2026/11/operational-excellence-when-you-ship-twice-as-much/), so the operational basics count for more than before, and the people side hasn't moved. If anything, [1:1s](/2026/12/how-i-run-one-on-ones-now/) took up more of my attention this year than they used to.

## What I got wrong

A few things I'd do differently.

I was slow to change how we measured things. For the first part of the year I was still glancing at activity charts and feeling good about them, and it took me longer than it should have to move fully to [outcomes over activity](/2026/11/measure-outcomes-not-activity/).

I underestimated the review load on senior engineers. By the time I noticed that some of the most experienced people on the team were spending most of their week reviewing, a couple of them were already worn down. We fixed it, but I should have caught it earlier.

And I waited too long to talk about the fear. People were worried about what AI meant for their jobs well before I started raising it in 1:1s. Next time I'll bring it up sooner.

## Bets for 2027

I'm calling these bets rather than predictions, mostly so it's easier to admit which ones were wrong next December.

**Teams get smaller and change shape.** I don't think this is about companies wanting fewer engineers so much as a small, experienced team with good tools covering ground that used to need a much bigger one. My guess is we'll see more teams built around a few people with strong judgment, a lot of agent-driven implementation, and (if they're smart about it) deliberate investment in the next generation.

Related to that, I think companies that keep [growing junior engineers on purpose](/2026/11/growing-junior-engineers-when-ai-does-the-junior-work/) will be glad they did. The short-term math makes it tempting to hire fewer juniors. In three or four years, when experienced engineers are even harder to find, I expect that to look like a mistake.

I also expect some backlash against over-built systems. Generating complexity costs almost nothing now, so 2027 will probably produce a lot of designs with more moving parts than anyone needs, followed by a renewed appreciation for [boring architecture](/2026/12/in-defense-of-boring-architecture/) that people can actually debug.

Reliability will be what separates teams. When everyone ships quickly, the ones customers notice will be the ones whose releases don't break things: gradual rollouts, rollbacks that happen automatically, alarms people trust.

The last bet is that good managers get more technical again. The old advice to gradually let go of the details is going to age badly when so much of the work comes down to judging what got produced. I'd just add the same caveat as before, that being able to build the prototype yourself is a reason to ask better questions, not a reason to take the work away from your team.

## Next year on the blog

I plan to keep writing weekly, mostly about leadership, systems, and how teams actually work day to day. I'd also like to do more hands-on technical posts with real examples, since this fall leaned heavily toward ideas. If there's something you want me to write about, tell me. A few of this season's posts started as reader questions.

Happy new year, and see you in 2027.
