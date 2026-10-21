---
layout: post
title: "Operational Excellence When You Ship Twice as Much"
date: 2026-11-23
description: "More change, more often, means more chances to break production. AI didn't change how operations work, it just turned up the volume. Notes on keeping systems reliable when the team is shipping faster than ever."
tags: ["Architecture", "Leadership", "AI"]
---

A sentence I wrote a few weeks ago keeps coming back to me: a team that ships twice as much code also ships twice as many chances to break something.

That isn't a knock on AI. It's arithmetic. Most production incidents are caused by change, so more change, more often, means more incidents, unless you also get better at shipping change safely. And when something does break at night, it's still a person who gets paged, opens the dashboards, and talks to the customer the next morning.

So this one is about the unglamorous side of moving fast.

## The rules are the same, the margin isn't

If you've read [Seeking SRE](/2023/04/summary-of-seeking-sre/) or spent any real time on-call, none of the fundamentals here will be new: small changes, gradual rollouts, monitoring that tells you something, fast rollback, and actually learning from incidents.

What's different is how much slack you have when you skip them. When a team shipped a few changes a week, you could get away with a manual deploy step, a dashboard someone checked when they remembered, or a rollback plan that amounted to "we'll figure it out." People covered the gaps. At higher volume every gap gets hit, regularly, and the shortcuts you used to get away with turn into the things that page you.

## Where I'd put the effort

### Deployments that expect some changes to be bad

At enough volume, some changes will be bad. Your engineers aren't careless, it's just probability. So design for it. Roll out in stages (one host, one availability zone, one region, then wider) so each step catches problems while the blast radius is still small. Let each stage bake for a while, because a memory leak or a slow-burning retry storm often takes an hour or two to show up. And roll back automatically when the key metrics go bad, instead of waiting for someone to notice.

Rollback should also be boring. If it's slow or scary, people hesitate, and hesitation is expensive. Practice it until nobody thinks twice.

### Alarms

Noisy alarms teach people to ignore alarms, which is arguably worse than having none. The rule I like is page on customer impact, ticket on everything else. Elevated 5xx rates or latency that customers can feel should wake someone up. A disk at 70% should open a ticket. Every so often, go through the alarm list and delete the ones nobody has acted on in months.

### Tests people actually trust

In the post on [code review being the new critical path](/2026/11/code-review-is-the-new-critical-path/) I argued that reviewers can't read every line carefully anymore. That only works if the automated tests are good enough to lean on, which means integration tests that hit real paths, tests for failure modes and not just the happy path, and treating a flaky test as a bug rather than background noise. If nobody trusts the test suite, every review turns back into manual verification, and that doesn't scale.

### Knowing what changed

The first question in any incident is "what changed?" With more changes in flight, it gets harder to answer. Put deployments on the same graphs as your health metrics. Count config pushes and feature flag flips as changes too, because the flag someone flipped at 4:55pm on a Friday is a deployment whether or not it went through the pipeline. If on-call needs twenty minutes to work out what shipped in the last hour, that's twenty extra minutes of impact.

### Systems you can hold in your head

This is more architecture than tooling. Generated code tends to be generous: an extra layer here, a wrapper there, a retry loop with no backoff "just in case." Each piece is reasonable on its own, and together they make something nobody can reason about during an incident. Push back on complexity in review, even when the code works. I want to write more about this one soon.

## Incident reviews when there are more incidents

A good post-incident review (we call them COEs) is one of the most valuable things a team does. The point is never blame. It's understanding what happened, why it was possible, and what we'll change so it can't happen the same way again.

For teams moving fast I'd add two things. First, look across incidents for patterns, not just within each one for a cause. If most of your recent incidents came from config changes, or from one service, or from changes that skipped a stage, that tells you where to invest. Second, ask honestly about the review when an AI-assisted change causes an incident. Was the change too big to review well? Did the reviewer understand it, or approve it because the tests were green? The goal isn't to blame the reviewer, it's to find out whether review is keeping up with output.

## What this means for managers

Operational work doesn't show up as features, so it's easy to starve. Nobody gets excited about a better rollback mechanism in a roadmap review. Protecting it falls to you.

In practice that means reserving real capacity for it every planning cycle and not letting features eat it. It means calling it out when an automatic rollback catches a bad change, because that's the system doing its job and people should see it. Keep an eye on on-call load too. If the rotation gets worse as output goes up, treat that as an early warning before it turns into burnout. And read the COEs, all of them. I learn more about my teams and our systems from those documents than from almost anything else.

The teams I expect to do well over the next few years aren't the ones that slow down. They're the ones that make shipping safe enough that going fast doesn't keep hurting them.
