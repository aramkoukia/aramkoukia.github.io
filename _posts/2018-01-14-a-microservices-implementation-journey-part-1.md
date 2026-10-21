---
layout: post
title: "A Microservices implementation journey — Part 1"
date: 2018-01-14
description: "Well, it’s that time where everyone is talking about Microservice, what they are, how they work, etc, and here I am putting my thoughts out…"
image: https://cdn-images-1.medium.com/max/1200/1*MMPsASQw6VIypEa1Y5o6lw.png
tags: ["Architecture", "Data", "Git"]
---

### A Microservices implementation journey — Part 1

![](https://cdn-images-1.medium.com/max/1200/1*MMPsASQw6VIypEa1Y5o6lw.png)*Image from “.NET Microservices — Architecture for Containerized .NET Applications” book: <http://aka.ms/MicroservicesEbook>*

Well, it’s that time where everyone is talking about Microservice, what they are, how they work, etc, and here I am putting my thoughts out there.

### Article Overview

I am going to cover 3 main areas, plus several not very “main” areas.

#### 1. Architecture

I will be talking about Architecture considerations around Microservices and how those considerations fit together to shape our solution.

We will also be looking at some of the patterns to consider more than anything else, but obviously you will need to tweak these patterns and recommendations for your own particular needs.

#### 2. Implementation

I will show you some simple implementations using .Net to give you a better understanding of how things will probably look like.

#### 3. Deployment

This part is where Docker comes to the picture, and we will take a look a the technologies available around DevOps and we will see where we are going as an industry, and how we are going to deal with deployments in a Miroservices environment.

This might be a rather long one, so I recommend go get a cup of coffee (or whatever your poison is), buckle up and let me take you through this journey!

![](https://cdn-images-1.medium.com/max/800/1*yz8cElfIkHET-93dbth0Xw.gif)

### Caveats

#### **1. Maturity level in Software Industry**

We as an industry are still on try and error phase, and constantly learning and coming up with new solutions, and sometimes even decide to go back to what we used to do a while ago.

And Microservices approach is no different. Most of the concepts that are used in Microservices, were introduced 10, or maybe 20 years ago, and we thought they didn’t make sense, or didn’t care and now, here we are, looking back at those and saying, “Yeah, that’s actually a good idea!”.

![](https://cdn-images-1.medium.com/max/800/1*zb0-aOn7mhAdMl6Rp0rXOA.gif)

#### 2. People still debating what a “real” Microservices implementation is

I don’t know if anyone has got Microservices 100% right as of today, and that’s fine, but in the path we are in and with this momentum of changes in this area, I believe all of those will have to revisit their implementations in a year or so anyways!

When you talk to people who claim they have built several Microservices, when you get into some details, you would probably easily find some points that are kind of “single point of failure”, which with Microservices implementation should have been eliminated.

**Let’s review the typical Microservices definition again:**

> Small, independent applications, loosely coupled, communicating with each other in an asynchronous manner, and can fail independently, and if one or some fails, the system as a whole still works, though the functionality might be downgraded when there are failures.

Architecture, just like anything else that we have in our industry, **is just there to solve a business problem.** That’s why it is OK to to get a not perfect Microservices implementation, and if we can solve the business problem, with even a “not perfect” Microservices implementation, in a “good enough” way, then that’s a good Architecture.

#### 3. Docker works on windows, but only in few Windows OS Versions

Good news is, Docker has now native support for Windows Server 2016 and Windows 10. So if you want to use it, you need to use Windows Service 2016 or Windows 10.

> Native Windows apps can now be built, shipped and run in containers that work on both Windows Server 2016 and Windows 10, making them more portable, easier to work on and simpler to run.

> Native Windows apps also have access to the same advanced container management features as Linux-based apps including image scanning, overlay networking, and Secrets management.

### Why you should build Microservices?

So the first and the most important reason for it is the most obvious one.

> It is cool, and it is this shiny new thing!

![](https://cdn-images-1.medium.com/max/800/1*bVwxUeJ1hjAOCVwx8739sA.gif)

Right? I mean we use it a lot to hire talented people to work on the cool new thing, and we also use it as a motivation, for learning, and experiencing cool new stuff for our current developers. So I guess it is a very important reason to consider.

**I mean, Netflix uses Microservices, so should we!**

But there are also other reasons why we should consider Microservices:

#### **1. Easier to understand Small services**

When you have small services, and you are responsible for them, it is easier to understand the boundaries of your services, and it will be easier for you to learn what the service does, as oppose to a monolith, where you will never know where your service ends, and where the other service starts

#### **2. Services are independently deployable**

You can deploy services independently. So if you have a feature, that is ready and tested and all, you don’t have to wait for some other components to finish something that is not related to your stuff at all. So you can go live without having to wait for anyone.

#### **3. Easier to adopt to newer technology (retire vs rewrite)**

When you have small little Microservices, and if a new technology comes up that is a very good fit for your service purposes, you can easily ditch the service and rewrite it with the new technology, without the need to rewrite the whole system which could cost you a fortune.

The classic case of Monolith applications is that, it is such a hard job to move them forward. That’s why there are still a ton of applications still running in .Net Framework 1.1 in production, and they can’t even move it a bit forward to 2.0, let alone more modern frameworks or technologies.

#### **4. Easier to scale small services**

If one or more features in your system are used more than the others, you can just scale up those specific services, and not the whole system or other services that aren’t used as much. This Microservices specification will become more important when you are using Cloud providers like Azure or AWS, where if you scale your whole system up, you are basically wasting money because it is not efficient.

#### 5. **No single point of failure**

In theory, the services should be completely independent, **and all the data and code that they need to execute an operation should be embedded in them,** so if some of the services fail, or their database is offline, other services are fully functional.

**This is very important, and people seem to overlook this by creating coupling between services because they don’t want to have duplicate data.** Some people tend to build “data services”, where each service, if it needs some data that is originated from other services, will access that data through some service interface, which is a essentially what you do in a traditional SOA architecture. **Watch out for these anti-patterns!**

#### 6. Freedom of technology stack choices

When we build these independent Microservices, we can give decision power to each team and let them decide what technology best fits their needs to deliver the business requirement. i.e. might make sense for one service to use NodeJs and Azure CosmosDb, and the other one should use an Azure table storage.

Though we should be careful, when introducing new technologies, we are adding overhead to our administration and learning, because now our DBA need to know about all the different data store techniques that are used in each service.

#### 7. It is quicker to evolve and release business features

Because we have all these independent services, we are able to evolve each one quicker as independently, because they are smaller and easier to analyze and add features to, without the need to have a big bang release. So hopefully, we will be able to release our business feature more frequently compared to a Monolith.

#### 8. Gives you a path to move away from your legacy code

With the Microservices architecture in mind, when we have a Monolith already, we can start carving off small pieces of functionality and put them into it’s specific dedicated Microservice gradually, without the need to do a big bang rewrite of the whole system.

> How you do eat an elephant? One bite at a time.

![](https://cdn-images-1.medium.com/max/800/1*7Xh4e4Iu-hGulIOED6dn5A.gif)*That’s me trying to add a feature to a Monolith!*

### The Microservices journey

So let me take you through some steps that will probably happen, when you decide as an organization that, you want to move towards a Microservices architecture:

#### **1. Everyone Reads some articles**

First step is, people start reading some articles (Some don’t, cause they know everything or they simply don’t care). More specifically people read the one about [Netflix architecture](https://www.nginx.com/blog/microservices-at-netflix-architectural-best-practices/), and you come across [Microservices.io](http://microservices.io/) website, read just the intoduction and few more pages, and then you are a master!

#### 2. **Everyone Reads some books**

Reading(mostly just buying though) books will be the second step. Again some people don’t read books, because they know everything or they don’t care, **or they have already a “magic” solution in mind, and don’t give a shit about anything anyone else has to say based on their findings in any article or any book!**

[![](https://cdn-images-1.medium.com/max/800/1*TmXYeiITDomYKHKB4hLFRA.jpeg)](https://www.amazon.com/gp/product/1491950358/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491950358&linkId=d300c7b9fadce34f91d6ad048b634f67)

#### 3. **Some meetings to come up with a plan**

Now that we are all ready, we start having these meetings to see if we are on the same page about “what a Microservices implementation mean”, and then we come out of the meetings, without anything changed in anyone’s mind!

That means, people who were confused and didn’t know what the hell they are supposed to do, still don’t have a clue, others that had some implementation in mind, still think their “code” will work, **and might also “IMAGINE” that all the books and articles agree with their approach (without actually reading the books or articles).**

#### 4. **Some very high level planning might happen (not really)**

At this point we have a high level plan, as high level as: “[WEEEE WILL, WEEEEE WILL, BUILD YOU! WEEEE WILL, WEEEEE WILL, BUILD YOU!](https://www.youtube.com/watch?v=-tJYN-eG1zk)”. (Sing like with us like Queen!)

![](https://cdn-images-1.medium.com/max/800/1*Unnmh-EMlfn41C0JRY6HCA.gif)

#### 5. **Some people start coding!**

At this point, some people are still confused, and some are excited and also confused, and some people are writing code! I’m not sure what part of the code, for what service, but they are writing something, that everyone will definitely need, and it is a good idea to have that piece of code or piece of service.

Anyways, if you figured out how to stop them, let me know how you did it!

### How MOST people are thinking / feeling after this

When we get into some action, and start planning properly (These other guys that I mentioned were coding… still coding by the way!), you will start understanding the service boundaries, and start designing events, and interfaces for the services to communicate.

At this point this is what people are thinking or how they are feeling, in no particular order:

- *WHAT THE F\*CK!*
- *OH MY F\*CING GOD! GEEZ!*
- *Ugh! Why are we doing this again?*
- “BEEEEEEP” (That one was totally censored, sorry, this is a workplace!)
- *This is gonna be so complex, I can’t even press F5 anymore to run my application*
- *Wasn’t this supposed to be easy?*
- *I don’t think it is going to work!*
- *I bet it used to be less brittle with monolith!*
- *Performance sucks!*
- ***I WILL UPDATE MY RESUME TONIGHT!***

![](https://cdn-images-1.medium.com/max/800/1*QKrp9lYtChH8sthjgGxStw.gif)

Yeah, I know. These people in Netflix and Uber and Amazon, talk about how they do things in Microservices way and they make it sound so easy!

The reality is, in a Monolith, all the crap code and complexity is combined in one spot, **now with the Microservices, we are basically taking this big ball of crap and distributing it all over the place.** So at the first glance, it looks like it is worse, but it is not, it is the same amount of complexity, but just distributed and broken down, now it is more obvious.

Of course, there will be issues which you didn’t have to deal with before, because it was a monolith. Like network calls all over the place, and the bottleneck it creates for you, and you didn’t have such issues before, but overall it is the same can of worms, it is just now open.

### Why people feel like that?

Well there are several reasons, but again with no particular order, here are some:

#### **1. Distributed systems are complex**

Yeah, they are. Definitely way more complex to design compared to monoliths and people coming from a monolith environment, will face a huge difference, and hence all the “what the f\*ck!” that you hear around the office from most of the developer desks.

#### 2. **Complexity is all over the place**

Before, people used to have this one application, that some parts of it were complex, and now this complexity is all over the system in different services and distributed between multiple services.

#### 3. **It is hard to debug and troubleshoot**

This one is a big change too. People used to just press F5 and run the whole thing and debug their sh\*t, but now when some call happens, one service is called, it sends a message to the “Service Bus”, gets picked up by another “Message Broker”, then does some data updates, and then some other service is notified and does some other stuff, and then posts another message to the “Service Bus” and then … Yeah, things are definitely different now.

#### 4. Multiple Repositories and Multiple Pull Requests

With Monolith, there are very limited number of code repositories, so if you are building a feature, that touches 4 different areas of the system, you used to make all the changes, test it locally and make 1 pull request to merge your changes to the proper code branch. But now, these 4 different areas that you touched, might belong to different services, so you have to make 4 different pull requests for each service, and also make sure the order that they are merged and deployed and etc.

#### 5. **Eventual Consistency needs a paradigm shift**

With the whole Asynchronous communication between the Microservices and using the Service Bus and Events, you will have to educate almost everyone from end user to the UX designers and managers in the organization, to be familiar with this concept and accept it. Eventual Consistency changes the way the user experience works a lot.

This also means that you need to forget about distributed transactions, and two phase commits, atomic database operations and etc and essentially, just implement workflows that you are able to execute them in reverse order.

### What else do we need to deal with?

Obviously there are lots of things going on and it is hard to consider everything, but here are some stuff that people will bring up and we need to deal with, when starting to move our Monolith to a Microservices architecture:

#### **1. What happens to the database?**

Yes, this is a big deal (if not the biggest problem to solve, it is definitely one of the complex ones). Do we want to let our database be our single point of failure? Now we have nicely decoupled services, what do we do with our database? If we separate them, them what happens if we need to share some data with some other service? Do we call other services to get the data or do we publish the data and duplicate it in every service that needs to use it?

![](https://cdn-images-1.medium.com/max/800/1*JD56h6PWBRGQlEtF9JvgVw.gif)

#### 2. **Do we need Distributed transactions or two phase commits?**

Distributed transactions and two phase commits is also something to deal with. Do we need them? How to implement them? Do we rely on some technology to give us these sort of feature, or do we build reversible workflows, so that if a workflow that has 2 phase commit failed at some point, it executes the flow in reverse to fix the state of our objects?

#### 3. **What’s the Current version of the system?**

Now that we deploy each service independently, and each team can release whenever they want, and the version they want, what is the version of our system? What if we deploy 2 different versions of the same service at the same time? Do we need to version our Events and Messages that we publish to “Service Bus”?

Yes, these are some of the questions that we need to deal with in a Microservices environment.

#### 4. **How do we handle authentication and authorization?**

Should each Mircoservice do security check on all of the incoming calls? Or do we implement a “[Trusted Sub System](https://docs.microsoft.com/en-us/dotnet/framework/wcf/feature-details/trusted-subsystem)” approach and basically let the calls from other Microservices go through using this “[Service to Service Authentication](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-protocols-oauth-service-to-service)” approach.

I hope you enjoyed the ride so far, have not changed your mind about building Microservices and you are ready to jump in to the Architecture.

### Microservices Architecture

When you look at different implementations of Microservices out there, they all use a combination of certain patterns for building an individual Microservice, as well as patterns for Microservices Integrations.

I will explain some of the most common patterns that people recommend in the industry these days. What you need to pay attention to is, we are not supposed to have a hard rule to use all these patterns for all of our Microservices and all of our requirements.

**Note:** *Some of these patterns and tools are meant to address certain issues when we build Microservices, so trying to use these patterns for “everything” might not be necessary and could possibly add complexity where it is not needed.*

#### Design Patterns and Components

The following patterns, and components, simply support the idea of distributed and loosely coupled systems.

- [**CQRS Pattern**](https://docs.microsoft.com/en-us/azure/architecture/patterns/cqrs)**: Command and Query Responsibility Separation**

with [CQRS Pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/cqrs), the idea is we treat our queries and commands as two separate problems to handle, so in our code we send queries and commands into separate paths to take care of them.

With this definition alone, if you have both commands and queries in one service, it doesn’t help us at all with our Microservices implementation as it is internal to what happens in a service, but if we ever want to separate the commands and queries into two different Microservices, in a way that one service handles the queries and the other one handles the commands, then if we use this pattern the separation will be really easy, because in theory the queries and commands should have separate code paths.

- **Event Sourcing Pattern**

With [Event Sourcing Pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/event-sourcing), the idea is we don’t save object’s final state in our data store, instead, we use this “Append Only” approach where we just record the events as a sequence in a stream of events, and every time we want to know what is the current state of an object, we start from the beginning of the event stream, execute them all, and find out the final state.

To be honest with you, this pattern has been called out as a good pattern that will be useful when building Microservices, but I still don’t fully understand, how this helps us in building a distributed decoupled application.

I get the idea of the read only stream of events that you can only add to it, and I get that there are tons of business use cases for it like in Financial Systems etc, but still don’t follow how does that help with Microservices Architecture.

Some people are suggesting, we put these events in a the Event Store, and if other Microservices needed the state of these objects, they could look into these event streams and find out what the state of the object is without the need to go to the original service to get it. Which this to me is again another single point of failure, where before in our Monolith, everyone was looking into this shared table to figure out the state, now we all look into the Event Store.

Anyways, I think at this point I think I rather use the Service Bus (Explained next) and have each service persist and embed (even if it is duplicate data) the data they need in their own data store.

- [**Enterprise Service Bus**](https://en.wikipedia.org/wiki/Enterprise_service_bus)

[Service Bus](https://en.wikipedia.org/wiki/Enterprise_service_bus) is a very important part of the Microservices implementation, and that’s the tool we will use to make the asynchronous communication between the Microservices possible using the Publisher and Subscriber model. Using this Publisher and Subscriber model is what forces us into adopting into the Eventual Consistency paradigm.

![](https://cdn-images-1.medium.com/max/800/1*D6vGZFPsvK2SBfcNFNIBjA.gif)*South Park Service Bus*

- **Optimistic Concurrency**

When moving to Microservices, we shouldn’t worry too much about concurrency as lots of things are asynchronous, similar to the two phase commit situation. As mentioned earlier for Two phase commits, we should just try and build workflows that we can execute in reverse if something went wrong because of concurrency.

![](https://cdn-images-1.medium.com/max/800/1*INtXLC7bKy5baNlMh4B5Cg.gif)

- [**Domain Driven Design (DDD)**](https://en.wikipedia.org/wiki/Domain-driven_design)**: Align Microservices to Domain Context**

DDD is an old subject. If you haven’t read the “Blue book”, I recommend you do, as it is the most famous book around this subject.

[![](https://cdn-images-1.medium.com/max/800/1*V6nt4xzGqYP18ZdAJozQFA.jpeg)](https://www.amazon.com/gp/product/0321125215/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=0321125215&linkId=17ce72da99f7b75e324f6c5ce479807b)

Basically, how DDD and some technique called “[Event Sourcing](http://microservices.io/patterns/data/event-sourcing.html)” helps when it comes to Microservices is, it helps us to understand where one service ends and where the other service starts. It basically helps us to understand our services based on their business capabilities and also helps us to understand the boundaries of each service.

DDD and Event Sourcing, will also help us to build a language called “[Ubiquitous Language](https://martinfowler.com/bliki/UbiquitousLanguage.html)”, which is a common, rigorous language between developers and users.

- **NoSQL: Read Model**

As mentioned earlier Event Sourcing, is recommended by most of the books as a pattern to store Events in our system (handled by the command path of our CQRS pattern). Now that is going to be very slow for querying purposes, so the recommendation is to have a “[Read Model](http://cqrs.nu/tutorial/cs/03-read-models)”, which is essentially a model of our data. But for performance reasons, there are recommendations to use NoSQL or In-Memory cache as our “Read Models” in Microservices.

- **API Gateway: Optimized for UI**

In a Monolith, the UI part was easy. Your 1 service would prepare everything the UI needs and sends it back, but in Microservices, UI would need to make multiple calls to different services, and collect the data and put it together to present to the user. This is also our “Trusted Subsystem” boundary in terms of Authentication and Authorization.

To fix this problem, there are different tools available that will take care of making the multiple calls and aggregating the data (as if it is a Monolth).

API Gateway and GraphQL are the two technologies used to fix this problem. But again to me this API Gateway or the GraphQL will be the single point of bottle neck and failure, where it has to be changed and in sync with ALL of the changes in Microservices. I am still not clear if this is actually a good thing or not!

On the other hand, if you don’t have this layer, and have your UI talk to your Microservices directly, then anytime you move you Microservice around, or you split it, then you need to keep changing the UI, which might not make a lot of sense!

- **Versioning: API, Database**

In Microservices, we need to think about versioning ahead of the time, because things change and we need to be able to handle them properly.

### Show me some Architecture Diagram

Of course it is not an Architecture without diagrams, so here you are:

![](https://cdn-images-1.medium.com/max/1200/1*MoHu_N-i2AdlAox8JKnhKA.png)

So here is a simple walk through on how things work with this Architecture:

1. UI Application (for example an Angular application) makes a request to API Gateway over Http.
2. This request is either a “Command” or a “Query”.
3. Commands will be passed to a Domain Microservice, which only accepts commands. Domain Microservice does not accept queries at all.
4. Domain Microservice receives the Command, persists the event in memory and sends the event to be persisted to the Event Store database.
5. Domain Microservice will also publish those events to the Service Bus.
6. As Read Model Microservice is interested in this event, it is Subscribed to this event, so it will receive this Event through the Service Bus, and updates its version of denormalized data and having ready for queries.
7. If the request is a “Query”, it will be sent to the Read Model Microservice.

### What’s inside Domain Microservice?

So now, let’s take a closer look inside the Domain Microservice, and see the different pieces that are needed there:

![](https://cdn-images-1.medium.com/max/800/1*_wErMHJdGLtWo7CG8lTX5w.png)

Here is a simple flow of events inside the Domain Microservice:

1. Web API Controller accepts only Commands, and when it gets one, it just forwards it to the Command Handler.
2. Then Command Handler will send the commands to the Aggregate to run the business logic related to the command.
3. Once that is completed, the Command Handler will be notified that the Aggregate operation is finished and, Events are ready to be persisted.
4. And then the Events will be persisted to the Event Store through the repository, and also the same Events will be published to the Service Bus for other services to consume.

#### Two Phase commit situation

It is possible here that we persist message to Event Store but the Message Bus message publishing fails, now, all we need to do here is to identify the failure, and go back to the event store and replay the message which will publish the message for us.

### What’s inside the Query Microservice?

Now, let’s zoom into the Query Microservice and see what are all the parts that are needed in there:

![](https://cdn-images-1.medium.com/max/800/1*SPB_mq9GtYx-EOWaYaCcAw.png)

The flow of events in the Query Microservice are pretty straightforward.

1. A Query is received by the Web API Controller (This controller can only handle Queries and not Commands)
2. Controller will pass the Query to the Query Handler, and Query Handler will simply execute the query reading from the Data Model and returns the data (Ideally, the Query Handler should not need to do any joins and the data should be already pre-populated and ready to consume in the Read Model)

On the other flow, if the Query Service is Subscribed to a specific Topic, and that Event appears on the Message Bus, the Event Handler will get notified, and it will update the Read Model accordingly.

**Note:** As you can see the Event Handling and the Query Handling parts of this service are completely separate, so if for any reason, like Scalability, you wanted to separate this service into two, you can easily do that.

At this point, we should have a fairly good understanding of the Microservices Architecture that I have in mind. Next up “Implementation”

Stay tuned for the next part of this article where I continue with the Implementation of the Architecture we went through.

**Looking for part 2? Continue reading:**

[**A Microservices implementation journey — Part 2**  
*In the first part of this Microservices implementation journey, I explained some of the details of a Microservices…*koukia.ca](https://koukia.ca/a-microservices-implementation-journey-part-2-10c422a4d402 "https://koukia.ca/a-microservices-implementation-journey-part-2-10c422a4d402")

If you are interested in reading more about Microservices Architecture topic, here are some relevant books:

[![](https://cdn-images-1.medium.com/max/800/1*TmXYeiITDomYKHKB4hLFRA.jpeg)](https://www.amazon.com/gp/product/1491950358/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491950358&linkId=363e9cf9c6a5a697a73b4fe159f37fda)*Building Microservices, Designing fine-grained systems*

[![](https://cdn-images-1.medium.com/max/800/1*M2r6FPQWHiiMN4CwwKcWpg.jpeg)](https://www.amazon.com/gp/product/1491965975/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491965975&linkId=ff04688c2c60121309905c5e0117b145)*Production Ready Microservices, Building Standardized systems across an engineering organization*

[![](https://cdn-images-1.medium.com/max/800/1*sNGTvyO3HCE2KjuaDycQnQ.jpeg)](https://www.amazon.com/gp/product/1491956259/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491956259&linkId=dd181a962e6fe756e0a81861258eb9c2)*Microservices Architecture, Aligning Principles, Practices and Culture*

[![](https://cdn-images-1.medium.com/max/800/1*3ufEsBu_Ajg_VpTLuTKHgg.jpeg)](https://www.amazon.com/gp/product/B0758YB73N/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B0758YB73N&linkId=9b1df16a450d563f1f9b905ae533d9d1)*Building Microservices with Asp.Net Core*

> If you liked this article, click the👏 below so other people will see it here on Medium.

> Let’s be friends on [Twitter](https://twitter.com/aramkoukia). Happy Coding :)

Cheers!
