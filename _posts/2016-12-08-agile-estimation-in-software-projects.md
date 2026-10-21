---
layout: post
title: "Agile Estimation in software projects"
date: 2016-12-08
description: "Agile Estimate is really just an approach or a framework for estimating effort in a software project."
image: /assets/img/2016-12-08-agile-estimation-in-software-projects/1.jpg
tags: ["Product & Agile"]
---

### Agile Estimation in software projects

Agile Estimate is really just an approach or a framework for estimating effort in a software project.

What you might want to know before reading this is, this approach is independent of your methodology. i.e: if you are using Scrum, or XP or Kanban or etc, you will still be able to use Agile Estimation for your project estimates.

First let’s talk about what is it that we are trying to accomplish or improve here. Right, “the Estimation”, which is always off the target, and it is always the case not just in the software development world, but even in the weather forecasts, so WE ARE NOT ALONE!

![](/assets/img/2016-12-08-agile-estimation-in-software-projects/1.jpg)

**Remember our last project that we estimated the project like this:**

- 4 Weeks Design and Architecture.
- 16 Weeks Development.
- 4 Weeks Test.

Let’s say we blew the estimate and the design took 5 weeks instead of 4. Sounds familiar? Remember what happens next?

Most probably the business or product owner will say: “OK, make up the time, CODE FASTER or BUILD SMARTER(not really sure what that actually means!) and instead of doing the development in 16 weeks do it in 15 weeks!”

One approach is to re-adjust the estimate based on the more accurate data that we have, just like the forecast guys(meaning change your mind the day before and forget about what you told yesterday about tomorrow!). Meaning keep your 16 weeks Develop and Test cycles and just start them one week late.

But the fact is, actually your estimate has been 25% off, so instead of your 16 month you are going to need 16 month + 25% which is 20 weeks and your test cycle should be 4 weeks + 25% which is 5 week.

Unfortunately none of us work in an organization that does this! Do you? The problem is this happens every day and we don’t re-adjust and the first date that the business or product owner gets from us, is the most concrete date ever and no matter what, they want the software at that time, even though they have agreed that the requirements are not clear and things might change in the process.

**We face this all the time for all the projects:**

- When we start a project and they want us to give them estimates, we do not have enough information
- First estimates that we announce becomes the unbreakable schedule of the delivery
- Any deviation is considered BAD !

Traditionally we used to spend a lot of time to come up with more and more design in the very beginning of the projects (known as waterfall method) to be able to estimate more accurately but still we don’t have enough details. And as the time progresses the more details come to light and you can do the estimates better and that is called **Cone of Uncertainty.**This is a fact, so why fight it? It exists….

![](/assets/img/2016-12-08-agile-estimation-in-software-projects/2.jpg)

**So what is Agile Estimation suggesting?**

Agile Estimation is suggesting to re-estimate again after each iteration, since you definitely have more information, this time your estimate will be more accurate(this is the Cone of Uncertainty, Remember?)

So let’s talk a little bit about the steps we should take to come up with the estimates:

**First: User Stories**

- first thing to do is, the Users or product owners should break down the functionality that are looking for in to “User Stories”. User Stories are just short descriptions of the functionality we want to implement.
- Try to keep the User Stories small and make them look like this template:
- As a <Role>, , I want <goal/desire> so that <benefit>
- Here is some samples:
- As a User, I want to search for my Eligible Products by their Product Family, Product Edition and Product Version.
- As a non-administrator user, I want to modify my own profile information but not the profile of other users
- As a user closing the order page, I want to be prompted to save the order that has changed since last save so that I can preserve order changes and discard erroneous work.

In the waterfall methodologies, and traditionally we put a lot of effort to generate design documents like Functional Specs, but I think in agile it is not that necessary and the User Stories are going to be enough for estimates, and I have seen some cases that they generate the functional specs(we are still doing this in our current project with Microsoft) and based on them try to extract the user stories which seems like a little over kill to me!

**Second: Assign Story Points to User Stories**

- Next thing we need to do is to break down user stories to unit of relative size so you can compare features and these units will be our alternatives to time.
- Story points are not measurement of duration, but rather a measurement of size/complexity. and we do it by considering a certain fairly easy task and come up with a number for a story point number comparing to the base line user story.
- Start with one standard feature (a baseline, like a login page or a simple data entry page with two text fields, which everyone knows how much work it needs to be done)
- after having a base like, we know that all other stories are either 1x, 2x, etc. larger or smaller than the baseline in size/complexity
- Since story points are relative size, the actual number of the story points assigned are meaningless different teams will have different baselines, so different points, we might be inaccurate but as long as all the story point are based on a baseline it is fine.

**Third: Negotiation**

So at the point that we want to assign story point to user stories, it is possible that for example for a certain user story that you think it is around 2 story points, someone comes into the meeting and bangs his head in to the table and says this super complicated and it is at least 25 story points, and now the situation becomes awkward and for overcoming this problem we use a tool called Planning Poker

**Negotiation Facilitator: Planning Poker**

We need to get all the team members together around a table and they are each given a set of a planning poker cards with the numeric values on them and then the facilitator will read out the user story, and everyone then will holding out their card without showing everyone else their card and after a little bit of time for everyone to think about it, everyone will show their card.

What usually happens at this point is everyone is pretty far apart. Planning poker then Used to facilitate a discussion over why people chose their levels of effort.

For example if there are two cards one 2 and one 20, you put down your cards and can talk about the reasons why you picked that level of effort for that story and usually if the team cannot agree on a story point on that session, there will be another planning poker meeting and what will usually happen is that, you can see that the card numbers are pretty much closer together this time and if you are still far apart it might make sense to put that user story aside and do a different user story.

![](/assets/img/2016-12-08-agile-estimation-in-software-projects/3.jpg)

And sometimes after discussions you do a second vote and if the values are still different, a lot of teams will just do an average, however if the team is really far apart the average will not be that accurate.

And if the numbers are far apart and you tried another user stories and you see that you are still far apart, means that maybe some people don’t know the rules of the game and maybe don’t know that the number that they give is the total number of efforts like the design, the development and the test. And if you see that one specific user story is the problem you may want to sit with the business again and try to make the user stories more clear for the team members.

Just remember that the Planning Poker is just a tool to have safe discussion about the estimates and in a sense takes the intimidation away so everyone will get to vote about the estimates without actually being influenced by other people. It might not actually solve the intimidation problem, but I think it really mitigates it well. And also gives us the ability to set our anchors. Sometimes we are not able to meet in the middle because we are being so far apart.

There is a website you can use to facilitate a planning poker meeting: <http://www.planningpoker.com>

**Forth: Product Backlog**

At this point what we do is we put all of the user stories are put into bucket. this will represent all the tasks that needs to be done for the project (Work Items)

Our Product Backlog will have rows that contains the Work Item, its Estimate(based on the Story point not time) and a Priority column(to be set by the Business/Product owner)

![](/assets/img/2016-12-08-agile-estimation-in-software-projects/4.png)

Now its time for the team to take out the high priority items that they can work on first and start their cycle.

What happens in your first Iteration or Sprint is, the Developers and the team will commit to a certain number of story points or a certain number of Backlog Items and the problem will be if the team has not worked together before or assembled and working on something that’s brand new to them, they probably OVER COMMIT in the first sprint but that’s OK.

After the first Sprint or Iteration is complete, what will happen is, you have what’s called your **Velocity Number.**This is a very important number when you are going to estimate how long a project is going to take.

**Fifth: Calculate Team Velocity:**

After the team has completed its first iteration, you now have the **Velocity Number**.

Velocity is the number of the story points that the team can complete per iteration.

It is easy to calculate velocity. What you do, is you take the total number of completed story points and divided it by the number of iterations that the team has done. It is very important to have a consistent velocity number, because it is then used to predict how much Work effort is going to be used in the next iteration.

Let’s say your team’s velocity is 35 story point, you would know in the next iteration you should only commit to 35 story points. In addition if there were approximately 500 items in the product backlog, you would then know, it would take approximately 14 to 15 sprints, until your project is complete, assuming you are not adding a lot more features, and bugs and user stories to your product back log.

Over time, your team velocity, will start to smooth out and it will stay about the same. What typically happens is the team velocity starts at one number and then the team works really hard to bring that number up and it shoots up in the second and third iteration, and then by the third, and fourth and fifth iterations, it starts to smooth out.

Here is a sample Velocity chart:

![](/assets/img/2016-12-08-agile-estimation-in-software-projects/5.png)

**Sixth: Re-estimation:**

If your story point estimates are very accurate, and your team always works at the same pace, your velocity will be identical, and usually velocity will stabilize after 3 to 6 iterations.

So what you do, is at the end of every iteration, you take stock of the product backlog, and you have a new velocity number, and then at the same time you are going to add new user stories and their associated story points to the product back log, and at the same time, some of the user stories will no longer be valid, or not that important anymore because you discovered more during the process of each iteration, and in addition to that, we WILL create some bugs, and bugs typically are just added in to the user stories of the product backlog.

So it is now time to re-prioritize the user stories again by the business after each iteration, because items priority will change.

Following is a sample table for the data we need to collect for re-estimation:

![](/assets/img/2016-12-08-agile-estimation-in-software-projects/6.png)

This way, you can calculate how many sprints you will need to go after each sprint.
