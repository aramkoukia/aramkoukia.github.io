---
layout: post
title: "Hi Todd Hilehoffer"
date: 2018-01-24
description: "I get that it might look like a lot of change compared to a monolith, but we should always think about the reasons “why” we want to have…"
medium_url: https://medium.com/@aramkoukia/hi-todd-hilehoffer-518f4efa61f8
---

Hi [Todd Hilehoffer](https://medium.com/u/4adfa0345776)

I get that it might look like a lot of change compared to a monolith, but we should always think about the reasons “why” we want to have Microservices. You can refer to the first part of this article and see if you have such requirements. If not, then I guess this is not for you :)

About reporting, there are different approaches and recommendations. One way is to have Listeners/Event Handler services that listens/subscribes to ALL/Relevant events in the system and populates some datawarehouse based on those events. Or you could build your reports on top of all the “Read Models” of all services, which would be considered a more coupled solution.

About debugging and pressing F5 again I explained how things would change in Microservises and developers searing around the office :D. With Microservices you need to rely more in logs and diagnostics for debugging and things would be a bit more complex to debug for sure, compared to monolith. But if service boundaries are defined correctly, then hopefully you could pin down the issue quicker because you know which service does what function, and what is failing, so you just get right to it.

About developer cheating and breaking the architecture, I guess you should have code reviews in the team to stop that kind of coding that is not inline with the overall software architecture.
