---
layout: post
title: "Microservices Architecture vs Service Oriented Architecture (SOA)"
date: 2017-08-03
description: "If you ask 10 people, “what are Microservices?” you will get 10 different answers. Even if you ask “ME” this question 10 times, chances are…"
image: https://cdn-images-1.medium.com/max/1200/1*TBU1yLasGjhEqWTucVdq-g.jpeg
tags: ["Architecture"]
---

### Microservices Architecture vs Service Oriented Architecture (SOA)

![](https://cdn-images-1.medium.com/max/1200/1*TBU1yLasGjhEqWTucVdq-g.jpeg)*Microservices Architecture vs Service Oriented Architecture*

If you ask 10 people, “what are Microservices?” you will get 10 different answers. Even if you ask “ME” this question 10 times, chances are you would still get 10 different answers! depending on what I was reading that day!

![](https://cdn-images-1.medium.com/max/800/1*5uuIBHU-gYSPMNo66dXPxg.gif)

### The story

I have an extensive experience with SOA, and from my readings around Microservices Architecture, I thought I summarize what I think is different between Microservices Architecture and Service Oriented Architecture so at least I know what is different between the two in principles.

### Microservices Architecture guidelines that are different than SOA guidelines

- In Microservices Architecture, it is not encouraged to “re-use”. Why? because it creates dependency between Microservice components. Though in SOA, if a piece of functionality exists in one of the services, you just call that service to do the job, but in Microservices Architecture, you might even duplicate the code/logic just to decouple.
- Synchronous API calls should not happen where possible in Microservices because it creates dependencies. Messaging should be used instead wherever possible (ie: Azure Service Bus or other technologies)
- In Microservices Architecture, Components can be unpredictable, so the client need to do “[discovery](https://www.nginx.com/blog/service-discovery-in-a-microservices-architecture/)” at runtime. Clients would also do load balancing where needed.
- Since Microservices Architecture uses “[Event Sourcing](http://microservices.io/patterns/data/event-sourcing.html)”, we end up with different “views” of data, and hence we end up with duplicate data across the system, which is embraced in Microservices Architecture.

### Microservices Architecture vs. Service Oriented Architecture

It seems like both of these architectures are trying to do the same thing, which is:

> They both let us to create pieces of functionality as isolated components.

> Service Oriented Arcitecture, has been mainly been used and focused on big enterprise scale, and from what I have observed Microservice Architecture is more at the application scale with approaches like Domain Driven Design .

### Microservice vs. SOA

Microservices are components, SOA is an architecture, so we cannot really compare these. So make sure you keep the “Microserices” with “Architecture” when comparing with SOA.

### Summary

Microservices Architecure is mainly a concept at application scale. Some of the guidelines might work in an enterprise level, but I think that depends on the scale and shape of the enterprise.

Service Oriented Architecture is a concept that is more seen in enterprise architectures. This architecture is mainly used for better integration between numerous applications in an enterprise. Having said that, we can obviously leverage some of the principles of Microservices Architecture into SOA to guide us develop the components in more modern ways. We should just be aware that some of the principals of the two architecture are opposing as I mentioned above.

I hope I did not confuse more that before!

Please don’t hesitate to comment or ask follow up questions, and don’t be surprised if I answered something that completely contradicts my own article.

Cheers
