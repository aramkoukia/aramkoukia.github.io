---
layout: post
title: "Measure Outcomes, Not Activity: How to Tell If Your Team Is Actually Doing Well"
date: 2026-11-30
description: "Lines of code, PR counts, and story points were never great signals. With AI generating code on demand, they're actively misleading. What I look at instead."
tags: ["Leadership", "Product & Agile", "AI"]
---

A while back someone showed me a dashboard with a big, happy chart on it. Pull requests merged per engineer per week, nearly doubled since the team started using AI tools.

"Great news, right?"

I asked three questions. Did customers notice anything? Did the system get more reliable? Did on-call get easier or harder?

Nobody knew. The chart was accurate, it just wasn't measuring anything we cared about.

## Activity metrics were weak, and now they mislead

I wrote about [improving a team's velocity](/2017/10/how-to-improve-a-software-teams-velocity/) almost ten years ago, and even then I was uneasy about how easily "velocity" turns into "look busy." Commits, lines of code, PRs merged, story points, tickets closed: all loose proxies for value. They sort of worked when producing code was the expensive part, because more output usually meant more progress.

That link is mostly gone. An engineer can generate thousands of lines before lunch, and a team can double its PR count in a month. None of that tells you whether the business moved forward, and some of it may point the other way, toward more code to maintain and more surface area for bugs.

The part that worries me is that **when you measure activity, people optimize for activity**, usually without meaning to. It's just what gets noticed. And with AI, producing activity is easier than it's ever been, so the gap between looking productive and being productive can get wide pretty fast.

## What I look at instead

There's no single number. But a handful of questions, asked consistently over time, get you most of the way.

The first one matters more than the rest put together: did a customer's life get better? What did we ship this quarter that someone outside the team actually noticed? Did adoption go up, did a specific class of support tickets drop, did a pain point go away? If a team can't answer that, it's the most important finding, regardless of how busy they've been.

Then reliability. Fewer incidents, shorter incidents, fewer pages, better availability and tail latency. Customers feel reliability even when they never see it. If output went up and reliability went down, you didn't get faster, you borrowed against next quarter.

I also want to know how long it takes to get a change safely to customers, from "we decided to do this" to "it's live and working." That covers the whole system (design, review, testing, deployment), which makes it the place where AI's gains either show up or get swallowed by the bottlenecks I've been writing about. Right next to it I look at how often changes go wrong, meaning what fraction of deployments end in a rollback or an incident. If that climbs as output climbs, your safety mechanisms aren't keeping up.

Two more that are easy to forget. Cost and toil, because removing a manual runbook step or an expensive batch job never makes the roadmap but keeps paying off for years. And the team itself: on-call load, signs of burnout, attrition, whether people are growing. A team that hits every goal while quietly burning out is about to stop hitting goals.

## Using them without ruining them

Even good metrics go bad if you use them badly. Look at trends over a quarter rather than one bad week. Use the numbers to ask questions about the system, not to grade people, because the moment a metric shows up as a target in someone's review, it starts to lie. Never look at speed without looking at quality next to it, since speed alone is easy to fake. And talk to customers and to the team. The numbers tell you that something changed, and the conversations usually tell you why.

## And for individuals

This gets harder at the individual level, and I don't think anyone has fully figured it out. I'll write about calibration separately, but the short version is that when everyone can produce a lot, I pay much more attention to judgment (did they pick the right problems and approaches), to impact (what changed because of their work), to ownership in production, including the boring parts, and to whether the people around them got better. None of that shows up in a PR count. All of it shows up if you're paying attention.

So the next time someone shows you a chart that's up and to the right, it's worth asking what it would look like if the team were doing worse. If the answer is "about the same," the chart isn't telling you much.
