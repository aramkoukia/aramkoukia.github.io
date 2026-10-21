---
layout: post
title: "Engineering Managers in the Age of AI: What Changed, What Didn't, and What's Next"
date: 2026-10-20
description: "AI made writing code cheap. It didn't make knowing what to build, or owning what you shipped, any cheaper. Some honest notes on the SDM job right now."
tags: ["Leadership", "AI"]
---

About once a week, someone asks me some version of the same question: "So… do we still need engineering managers?"

Sometimes it's an engineer half joking. Sometimes it's a new manager who's genuinely worried. Once it was my own reflection in a dark laptop screen at 11pm, after an AI agent had finished a task in 20 minutes that I had estimated at two days.

Short answer: yes. But the job is shifting under our feet, and if you manage it the same way you did three years ago, you're going to have a hard time.

So here are my notes. What has actually changed, what hasn't changed at all (and probably never will), what I think is coming next, and what I'd do if I were an SDM trying to stay relevant. Which, to be clear, I am.

⸻

## What has changed

### Writing code got cheap. Knowing what to build didn't.

This is the big one, and everything else follows from it.

The cost of producing code has dropped dramatically. A decent engineer with good AI tooling can produce a working first version of almost anything in a fraction of the time it used to take.

But the expensive parts of software were never really the typing. They were:

- figuring out what the customer actually needs,
- deciding what *not* to build,
- getting the design right before it gets expensive to change,
- and owning the thing in production for years.

None of those got cheaper. Some of them got harder, because now you can build the wrong thing much faster.

### The bottleneck moved

On most teams I see, the constraint used to be "how fast can we write it." Now it's "how fast can we review it, test it, and safely ship it."

Pull requests are bigger and there are more of them. Senior engineers spend a big chunk of their week reviewing code that nobody on the team typed by hand. If you're not paying attention, your best people quietly turn into full-time code reviewers, and they will not thank you for it.

**Your job as a manager is to notice where the bottleneck moved, and move the team's attention with it.**

### Output stopped meaning much

Commit counts, lines of code, number of PRs. Honestly, these were never good signals. Now they're useless. An engineer can generate 3,000 lines before lunch. That tells you nothing about whether they moved the business forward.

If your performance conversations still lean on activity metrics, even a little, this is the year to stop.

### Managers can build things again

This one I love.

For years, the deal was: you move into management, your hands slowly come off the keyboard, and you become "technical-ish." Now I can sit down on a Saturday morning and have a working prototype of an idea before my coffee gets cold. Okay, before my second coffee.

That changes the conversation with your team. You can show instead of tell. You can test an assumption before asking someone to spend a sprint on it. That's a real superpower, as long as you don't abuse it (more on that below).

⸻

## What hasn't changed

Here's the thing a lot of the hot takes miss. Most of the job is exactly the same.

### People are still people

Nobody has an AI model for "my mom is sick and I can't focus this month." People still want to grow, to be challenged, to be recognized, to know their work matters, and to not get burned out. I wrote about [why star players quit](/2017/12/why-your-teams-star-players-quit/) back in 2017, and every single reason on that list still applies. If anything, the "not enough challenge" one is getting worse, because AI is eating the easy wins people used to grow on.

### Someone still owns the outage

The pager still goes off at 3am. The AI doesn't join the call, doesn't write the COE, and doesn't explain to the customer what went wrong.

**Ownership doesn't get delegated to a tool.** A team that ships twice as much code also ships twice as many chances to break something. Operational excellence, good alarms, safe deployments, real rollback plans… these matter more now, not less.

### Clarity is still the job

Teams still need to know *why* they're doing what they're doing. Where we're going, what we're not doing, and how we'll know we got there. AI can help you write the doc. It can't decide what the doc should say.

### Judgment, hiring, and trust

Who to hire. Who to promote. When to push back on a deadline. When to kill a project the team loves. When to have the hard conversation. These were the hard parts of the job before AI, and they're still the hard parts.

⸻

## What I think is coming next

These are my bets for the next year or two. I could be wrong on the timing, but I'd be surprised if I'm wrong on the direction.

### 1. You'll be managing a mix of humans and agents

We're already seeing agents take on multi-step work: pick up a ticket, write the change, run the tests, open the PR. Very soon, a good chunk of the "work" on a team will be done by agents that engineers direct and review.

That raises questions most of us haven't thought through yet. How do you plan capacity? Who's accountable when an agent ships a bug? How do you review work at that volume without lowering the bar? The managers who think about this early will have a big advantage.

### 2. Teams get smaller, and expectations go up

I don't think engineering teams are going away. I do think a team of five will be expected to own what a team of ten owned a few years ago. That means more scope per person, more systems per team, and a lot more need for crisp ownership boundaries.

### 3. The junior engineer pipeline gets weird

This is the one that keeps me up at night a bit.

Junior engineers used to learn by doing the small, well-scoped tasks. Those are exactly the tasks AI does best. If we're not deliberate, we'll end up with a generation of engineers who can prompt but can't debug, and in five years we'll be wondering where all the senior engineers went.

### 4. Performance evaluation gets harder

When everyone can produce a lot, telling great from good gets harder. Calibration conversations will need to focus much more on judgment, impact, and ownership, and much less on volume. Most of our current performance processes aren't built for this yet.

⸻

## What SDMs need to do to stay relevant

Okay, the practical part. If I had to give a new (or not so new) manager a list, this would be it.

### 1. Use the tools. Yourself. Every week.

Not a demo. Not a slide deck about "our AI strategy." Actually use them, on real problems, until you hit their limits.

You can't make good decisions about how your team should work with AI if you don't have a feel for where it's brilliant and where it confidently makes things up. And believe me, your engineers can tell when you don't.

### 2. Get more technical, not less

The old advice was "as you grow, let go of the details." I think that's backwards now.

When code is cheap, the value is in judgment: Is this design sound? Will this scale? What happens on the worst day? If you can't evaluate the work, you can't lead the team that produces it. If you need a starting point, here's how I [evaluate a distributed system architecture in 30 minutes](/2025/11/how-to-evaluate-a-distributed-system-architecture-in-30-minutes/).

But don't abuse it. Just because you *can* prototype the thing on Saturday doesn't mean you should show up Monday and hand it to the team as the answer. Use it to ask better questions, not to take over.

### 3. Redesign how your team works around the new bottleneck

Look at where work actually waits today. For most teams it's review, testing, and deployment. So invest there:

- Smaller, more reviewable changes, even if the AI could generate a giant one.
- Better automated tests, so reviewers can trust what they're looking at.
- Clear rules for what needs a deep human review and what doesn't.
- Deployment safety that assumes more change, more often.

### 4. Make writing a core skill on your team

Here's a slightly spicy take: **the spec is becoming the code.** The quality of what an agent produces depends heavily on how clearly someone described the problem, the constraints, and what "done" looks like.

Teams that write well (clear requirements, clear design docs, clear acceptance criteria) are going to get way more out of AI than teams that don't. Coach this like you'd coach any other engineering skill.

### 5. Grow your juniors on purpose

Don't let AI quietly take away every learning opportunity. Some ideas that have worked for me:

- Have juniors explain the AI-generated code in review. If they can't explain it, it doesn't ship.
- Give them real debugging and on-call shadowing early. Production is the best teacher there is.
- Pair them with senior engineers on design, not just on implementation.

### 6. Measure outcomes, not activity

Ask: did the customer's experience get better? Did the system get more reliable? Did we reduce cost or toil? Those questions were always the right ones. Now they're the only ones that mean anything.

### 7. Talk about the fear, out loud

Your team is reading the same headlines you are. Some of them are worried about their jobs, and most won't bring it up in a 1:1.

Bring it up yourself. Be honest about what you know and what you don't. Help them see how their role is evolving, and what skills will matter. People can handle uncertainty. What they can't handle is silence from their manager while everyone pretends everything is fine.

And keep it human. Laugh together when the AI does something hilariously wrong (it will). The teams that trust each other enough to laugh are the ones that adapt fastest.

### 8. Don't lower the bar

When things get easier to produce, it's tempting to accept "it works" as good enough. Don't. Correctness, security, operability, and maintainability still matter, and someone has to keep holding that line. That someone is usually you.

⸻

## Wrapping up

AI didn't make engineering managers obsolete. It made the lazy version of the job obsolete: the version that was mostly status updates, sprint ceremonies, and forwarding emails.

What's left is the good stuff. Clarity, judgment, technical depth, growing people, and owning outcomes. Honestly, that's the part of the job I always enjoyed the most anyway.

So no, I don't think we're going anywhere. But we do have some homework.

If you're an SDM navigating this right now, I'd love to hear what's working for you, and what isn't. Find me on [LinkedIn](https://www.linkedin.com/in/aram-koukia/).
