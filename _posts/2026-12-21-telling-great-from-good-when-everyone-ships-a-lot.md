---
layout: post
title: "Telling Great from Good When Everyone Ships a Lot"
date: 2026-12-21
description: "Performance conversations used to lean, at least a little, on how much someone produced. With AI, almost everyone produces a lot. How I think about evaluating engineers when volume stops being a signal."
tags: ["Leadership", "Career", "AI"]
---

It's the end of the year, which at a lot of companies means performance reviews.

This year I've run into a problem in those conversations that I didn't have before, or at least not this badly. Almost everyone had a productive year. Lots of projects, lots of PRs, lots of launches. Looking only at what got shipped, the whole team looks about the same, and about the same is great.

They're not the same, though. A few people had a genuinely great year and several had a solid, good one. The difference is real and it matters, but it isn't showing up where we used to look for it.

## Volume stopped telling us anything

Nobody serious ever said "this person wrote the most code, so they're the best." But volume crept into reviews anyway, as a tiebreaker or a supporting point. "They delivered a lot this year." "They closed a huge number of tickets." It made a write-up feel well-evidenced.

With AI tools, a good engineer and a great engineer can produce roughly the same amount. Sometimes the good one produces more, since they're less picky about what they build. So leaning on volume, even a little, now tilts calibration in the wrong direction. You end up rewarding more output and less judgment, which is pretty much the opposite of what I argued for in [taste is the new bottleneck](/2026/10/taste-is-the-new-bottleneck/).

## What I see in the great years

When I look back at the people who had standout years, the common threads have very little to do with how much they typed.

They picked the right problems. They noticed the thing nobody else had noticed, or pushed back on a project that shouldn't have happened, or moved effort toward what customers actually needed. A fair amount of their impact came from work that never got built, which is invisible in a review unless you go looking. So one question I now ask is: what did this person decide *not* to do, and were they right?

Their work changed something. I care less about "they shipped X" and more about what was different afterward, whether that's a class of outage going away, another team getting unblocked, or costs going down. I wrote about [measuring outcomes, not activity](/2026/11/measure-outcomes-not-activity/) for teams, and the same thinking works for individuals.

Their judgment held up over time. Did the designs survive production? Did the risks they raised turn out to be real? When they said something was fine, was it? Over twelve months you develop a sense of whose judgment you trust and whose you quietly double-check, and that gap is getting more valuable every quarter.

They stayed with their work after it shipped. They fixed the bugs, tuned the alarms, wrote the runbook, did the unexciting follow-ups. They joined the incident call for their system even on weeks they weren't on-call.

And, for senior people especially, they made others better. Reviews that taught something, a design discussion that got someone unstuck, a junior engineer walked through a hard problem. **Someone who makes five colleagues better is usually worth more than someone who does excellent work alone.** This is the one I weigh most heavily at senior levels.

## Gathering better evidence

Since volume doesn't help, I need other evidence, and most of it has to be collected during the year rather than in December.

I keep notes when things happen: a great call in a design review, a serious bug caught in someone else's change, an incident handled well. I write it down that week, because by December my memory is unreliable and heavily biased toward the last couple of months. When I ask peers for input, I ask specific questions, like "can you think of a time their judgment changed how a project turned out?", because vague questions get vague answers. I read people's code reviews and design docs, since the comments someone leaves on other people's work say a lot about how they think. And I look at what happened later. Six months after a launch, is the system stable, and can other people change it safely? It's a lagging signal but a very honest one.

## The fairness problem

There's a risk here I don't want to skip over. Judgment, impact, and ownership are harder to measure than volume, which makes them easier to evaluate with bias. The person who talks a lot in meetings can come across as having better judgment than the quiet person who is right more often.

What helps me is asking "what's the example?" every time someone makes a claim about a person's performance, including when that someone is me. I also try to pay extra attention to the steady, quiet people whose best work is mostly invisible: the problems that never happened, the bad designs that got fixed in week one, the colleagues who got better because they were around. Those people have been undervalued for a long time. Done carefully, this shift could actually help them.

## If you're the one being reviewed

The practical advice is to help your manager see what matters. Skip the list of everything you shipped. Write a short list of the decisions you made, what changed because of them, and who you helped along the way. "I shipped 14 features" is fine. "I talked us out of a project that would have eaten a quarter and put that effort into a fix that cut customer-facing errors in half" is the kind of sentence that changes a calibration discussion.

Volume was always a shaky way to tell great from good, but it was convenient, and we leaned on it more than we admitted. Without it the job gets harder. I think it also gets fairer, if we're careful.

If you're a manager changing how you run reviews this year, I'd be curious what you're trying. I'm on [LinkedIn](https://www.linkedin.com/in/aram-koukia/).
