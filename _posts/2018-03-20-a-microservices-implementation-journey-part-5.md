---
layout: post
title: "A Microservices implementation journey — Part 5"
date: 2018-03-20
description: "If you have followed me recently I have been writing a series of articles around Microservices Architecture and Implementation. I hope you…"
image: https://cdn-images-1.medium.com/max/1200/1*vfuvTl2YvXe7vSTbNqlHMw.png
tags: ["Architecture"]
---

### A Microservices implementation journey — Part 5

![](https://cdn-images-1.medium.com/max/1200/1*vfuvTl2YvXe7vSTbNqlHMw.png)*Useful Patterns for Resilient Microservices*

If you have followed me recently I have been writing a series of articles around Microservices Architecture and Implementation. I hope you read the [First](https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917), [Second](https://koukia.ca/a-microservices-implementation-journey-part-2-10c422a4d402), [Third](https://koukia.ca/a-microservices-implementation-journey-part-3-50f030ba6bb5) and [Forth](https://koukia.ca/a-microservices-implementation-journey-part-4-9c19a16385e9) part of this [Microservices](https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917) I[mplementation Journey](https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917) and found them useful and if you didn’t I recommend you do!

Here are the links for the previous parts:

**Part 1:** <https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917>

**Part 2:** <https://koukia.ca/a-microservices-implementation-journey-part-2-10c422a4d402>

**Part 3:** <https://koukia.ca/a-microservices-implementation-journey-part-3-50f030ba6bb5>

**Part 4:** <https://koukia.ca/a-microservices-implementation-journey-part-4-9c19a16385e9>

### Resilient Microservices

Now that we are breaking up our system into more granular pieces, though based on the definition, if one of these services fails, only some of our functionality will be degraded, we still need to make sure that we implement each service as resilient as possible.

If you are not familiar with the term “Resiliency”, it means our system needs to handle failures gracefully and be able to recover from them.

Based on the nature of Microservices architecture that our applications might share platforms, or even compete for resources in some cases, or compete with bandwidth or internet, we might experience transient failures or event permanent errors that we can not recover from. Detecting such issues as early as possible and handling them in the code is very important for our services to be resilient.

There are several patterns out there that you might have heard about them, that leveraging them will help us to have more resilient services.

*Of course this doesn’t mean that, you cannot or should not use these patterns if you don’t have a Microservices architecture. These patterns are very useful in general and it is a good idea to use them in any sort of software.*

### Resiliency Patterns

- **Retry:** If you think it is a temporary failure, you can try one or more time.
- **Timeout:** After some period of time, there is no point to wait more!
- **Bulkhead Isolation:** If parts of an app starts to fail, it should be isolated in a way that it does not cause wider failure with swamping resources (CPU/Memory)
- **Circuit Breaker:** When parts of our app is experiencing serious failure, we should fail quick so we don’t swamp resources for other parts of our system.
- **Fallback:** Think of a “Plan B” for when things fail!

There are definitely more known patterns out there that some might argue that are related to resiliency, like “**Leader Election**”, “**Compensating Transactions**”, “**Queue-Based Load Leveling**”, “**Scheduler Agent Supervisor**”, but for now I am just going to cover the one I explained above and leave the other one on you to go and investigate how you can implement them.

### Introducing The Polly Project

Although you can totally implement all these patterns for yourself, but I have come across “[The Polly Project](http://www.thepollyproject.org/)”, which is part of the [.Net Foundation](https://www.dotnetfoundation.org/about) now, and .Net Team is leveraging a lot of their code in implementing .Net Core stuff.

![](https://cdn-images-1.medium.com/max/800/1*VhyhGoxWxaWgTz7UBwyIsQ@2x.png)*The Polly Project*

#### What is Polly?

> Polly is a .NET resilience and transient-fault-handling library that allows developers to express policies such as Retry, Circuit Breaker, Timeout, Bulkhead Isolation, and Fallback in a fluent and thread-safe manner.

Polly is Open Source and is licensed under the terms of the [New BSD License](http://opensource.org/licenses/BSD-3-Clause).

The following link is the Github repo, home of Polly:

[**App-vNext/Polly**  
*Polly is a .NET resilience and transient-fault-handling library that allows developers to express policies such as…*github.com](https://github.com/App-vNext/Polly "https://github.com/App-vNext/Polly")

### Adding Polly to our solution

Polly comes in a nuget package and is very straight forward to add:

```
Install-Package Polly
```

Then you can go ahead and use it.

#### Sample Retry Policy

The following snippet shows how you can retry a call to your function, 3 times when a certain type of exception occurs:

And if you want to retry forever you can use the following code:

All the above Retry policies will try calling your function without any time between them, but if you want to wait for a while until your next try you can use the following sample:

#### Sample Circuit Breaker Policy

To break the circuit after a number of exceptions and keep it broken for a period of time, you can use the following sample:

Now, if the state of the circuit changes and you want your code to try again, you can use the following sample:

#### Sample Fallback Policy

If you want to provide a substitute value when an exception occurs you can use the following sample:

#### Sample Timeout Policy

If you want to call an action if some operation times out you can use the following sample:

There are a ton of other cool APIs that you can read all about them in the [Poly project’s Github page](https://github.com/App-vNext/Polly) and [their website](http://www.thepollyproject.org/). Please take a look at everything that Poly has to offer and hopefully by leveraging this or similar libraries you can build more resilient Microservices.

In the [next part of this series](https://koukia.ca/a-microservices-implementation-journey-part-6-9b818e491336), I will demonstrate how to use install and configure Apache Kafka on Azure, and use it as an Event Source or Service Bus component in your Microservices Architecture.

[**A Microservices implementation journey — Part 6**  
*If you have followed me recently I have been writing a series of articles around Microservices Architecture and…*koukia.ca](https://koukia.ca/a-microservices-implementation-journey-part-6-9b818e491336 "https://koukia.ca/a-microservices-implementation-journey-part-6-9b818e491336")

If you are interested in reading more about Microservices Architecture topic, here are some relevant books:

[![](https://cdn-images-1.medium.com/max/800/1*TmXYeiITDomYKHKB4hLFRA.jpeg)](https://www.amazon.com/gp/product/1491950358/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491950358&linkId=363e9cf9c6a5a697a73b4fe159f37fda)*Building Microservices, Designing fine-grained systems*

[![](https://cdn-images-1.medium.com/max/800/1*M2r6FPQWHiiMN4CwwKcWpg.jpeg)](https://www.amazon.com/gp/product/1491965975/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491965975&linkId=ff04688c2c60121309905c5e0117b145)*Production Ready Microservices, Building Standardized systems across an engineering organization*

[![](https://cdn-images-1.medium.com/max/800/1*sNGTvyO3HCE2KjuaDycQnQ.jpeg)](https://www.amazon.com/gp/product/1491956259/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491956259&linkId=dd181a962e6fe756e0a81861258eb9c2)*Microservices Architecture, Aligning Principles, Practices and Culture*

[![](https://cdn-images-1.medium.com/max/800/1*3ufEsBu_Ajg_VpTLuTKHgg.jpeg)](https://www.amazon.com/gp/product/B0758YB73N/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B0758YB73N&linkId=9b1df16a450d563f1f9b905ae533d9d1)*Building Microservices with Asp.Net Core*

Cheers!
