---
layout: post
title: "A Microservices implementation journey — Part 3"
date: 2018-01-28
description: "I hope you read the First and Second part of this Microservices Implementation Journey and found them useful."
image: https://cdn-images-1.medium.com/max/800/1*oSOTEY5OOcyjFvJ4utjiYw.jpeg
medium_url: https://medium.com/@aramkoukia/a-microservices-implementation-journey-part-3-50f030ba6bb5
---

### A Microservices implementation journey — Part 3

![](https://cdn-images-1.medium.com/max/800/1*oSOTEY5OOcyjFvJ4utjiYw.jpeg)*Event Sourcing Diagram. Picture from: <https://www.confluent.io>*

I hope you read the [First](https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917) and [Second](https://koukia.ca/a-microservices-implementation-journey-part-2-10c422a4d402) part of this [Microservices Implementation Journey](https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917) and found them useful.

And if you didn’t I recommend you do, because in this article I will get a bit deeper in some of the subjects I brought up earlier.

Here are the links for the previous parts:

**Part 1:** <https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917>

**Part 2:** <https://koukia.ca/a-microservices-implementation-journey-part-2-10c422a4d402>

In this article I will get into some of the details around Event Sourcing and different tools available for it, as well some of the trade-offs around using Event Sourcing vs. Just a regular Service Bus and regular Database.

### What people said

If you remember the Architecture diagram from the [Part 1 of these Microservices Implementation series](https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917), it looked like the following:

![](https://cdn-images-1.medium.com/max/800/1*MoHu_N-i2AdlAox8JKnhKA.png)*<https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917>*

Here are some of the questions and comments people had when they read Part 1 of this article:

1. *Why are we using Event Store?*
2. *What does Event Store give us other than an audit trail?*
3. *Why are we using Service Bus when we can just subscribe to Event Store events?*
4. *Why is the Read Model Event Handler listening to the Service Bus and not subscribing to the Event Store?*

I think these are very good questions and it makes sense to discuss them before we move further.

### Why are we using Event Store?

Any Event Store we use, comes with its own set of features and functionalities, but when it comes to using Event Stores as a Data Store in Microservices, there is one main reason:

**Eliminating the need to handle “Two Phase Commits”.**

Imagine if we don’t use Event Store and use a regular SQL database as well as a Service Bus to publish the Events for other services to Subscribe to. In this case there is a “2 Phase Commit” situation that we need to handle properly.

#### Tell me more

What if you saved some record in some database tables and then try to publish the relevant Events to Service Bus and you can’t? Now you have to retry for some time with an “[Exponential Back-off](https://en.wikipedia.org/wiki/Exponential_backoff)” algorithm (that causes delay in the system for the Event to be propagated properly), if you weren’t successful at the end to publish the Event, you have to roll back the changes that you made to the database.

![](https://cdn-images-1.medium.com/max/800/1*y1dray95zzNWfjXrNctYkQ.png)*One of the use cases of Event Sourcing*

#### Can we do this with a regular databases?

Short answer is Yes, if the database has Publisher Subscriber features.

The most famous NoSQL database that can give us Pub/Sub feature as well as regular storage is [Redis](https://redis.io/topics/pubsub):

[**Pub/Sub - Redis**  
*unsubscribe: means that we successfully unsubscribed from the channel given as second element in the reply. The third…*redis.io](https://redis.io/topics/pubsub "https://redis.io/topics/pubsub")

#### Can we do this with a database that doesn’t have Pub/Sub features?

Again the answer is Yes, but then you need to have some sort of “[Compensating Transaction](https://en.wikipedia.org/wiki/Compensating_transaction)” that spans across a database transaction, and publishing a message to Service Bus, and only complete the transaction if both operations where successful. Though it won’t be an atomic operation, it will work but as you can imagine, if we are able to do this without a transaction it would be more efficient.

From Wikipedia:

> **Compensating transactions** are also used in case where a transaction is long lived (commonly called [Saga Transactions](https://en.wikipedia.org/wiki/Long-running_transaction "Long-running transaction")), for instance in a business process requiring user input. In such cases data will be committed to permanent storage, but may subsequently need to be rolled back, perhaps due to the user opting to cancel the operation.

Even when we use Redis, we would still need a Redis transaction, and we just put our two operations (1. Add data to Redis 2. Publish an event) in a transaction scope.

#### Atomic Transactions With Azure Service Bus

The following is from the [Azure Service Bus Github page](https://github.com/Azure/azure-service-bus/tree/master/samples/DotNet/Microsoft.ServiceBus.Messaging/AtomicTransactions) that explains what it currently supports when it comes to Compensating or Saga Transactions:

> Azure Service Bus currently does not support enlistment into distributed 2-phase-commit transactions via MS DTC or other transaction coordinators, so you cannot perform an operation against SQL Server or Azure SQL DB and Service Bus from within the same transaction scope.

> Azure Service Bus does support .NET Framework transactions [which enlist volatile participants](https://msdn.microsoft.com/en-us/library/ms172153%28v=vs.85%29.aspx) into a transaction scope. Whether a set of Service Bus operations will become effective can therefore be made dependent on the outcome of independently enlisted, parallel local work.

You can take a look at more detailed documentation around Transaction Support in Azure Service bus in the following page:

[**Azure/azure-service-bus**  
*azure-service-bus - ☁️ Azure Service Bus service issue tracking and samples*github.com](https://github.com/Azure/azure-service-bus/tree/master/samples/DotNet/Microsoft.ServiceBus.Messaging/AtomicTransactions "https://github.com/Azure/azure-service-bus/tree/master/samples/DotNet/Microsoft.ServiceBus.Messaging/AtomicTransactions")

#### Using Event Sourcing is Atomic

With Event Store, we don’t need to worry about Compensating or Saga Transaction as we are just doing ONE thing, which is saving the Event into the Event Store, so it is an atomic operation anyways and hence no need for a transaction at all.

#### Any other reason to use Event Sourcing?

Well, yes there are some features that Event Stores provide that are useful:

1. **Accurate Audit Trails**

As we log each event separately in the Event Store, by looking at the streams, it is very obvious what is the history of each stream, and why we are in the current state.

**Can’t we do this with SQL?** Yes, we can use custom implementations or SQL CDC (Change Data Capture) to do the exact same thing, but Event Store does this more easily.

2. **Easy to make** [**temporal**](http://desktop.arcgis.com/en/arcmap/10.3/map/time/what-is-temporal-data.htm) **queries**

Because we are keeping a complete trail of events for each business object, it is easy to query the past and know what was the state of that object at any time in the past.

**Can’t we do this with SQL?** Yes we can, but it is much easier to implement such queries with Event Stores.

### Do we need both Event Store and Service Bus?

Short answer is no. But then if you have implemented a proper Saga or Compensating Transaction handling between your Microservice’s regular database and publishing message to Service Bus, and you don’t have requirements for querying temporal data or very accurate audit log trails, and you don’t care if things change in your historical data, you can just use Service Bus, and you don’t need the Event Store.

### Why should I publish events to both Event Store and Service Bus?

You don’t have to. You only need to do that if your service has some requirements that using Event Store is a good fit, and then and the same time you have some other services in your echo-system that don’t need Event Store and they just use a Service Bus and they have their own local SQL databases, so in that case, you publish events to Event Store for the service that uses Event Store, and then another event to Service Bus for the services that Don’t use Event Store and just use Service Bus and a regular SQL or NoSQL database.

### Can we skip the Event Sourcing all together?

Short answer is yes, but only if you considered all the benefits and use cases of it and you don’t have any of those requirements, and you also have implemented a proper “Saga” for cross service transaction handling.

From my experience, in most enterprise software there are business requirements that completely fit to what Event Sourcing has to offer, so I guess you will probably end up either using an Event Store OR implement a similar thing yourself using a regular SQL or NoSQL Database.

Financial components are the first ones that come to mind to be a good fit for using Event Stores for them.

### Any problems with using Event Sourcing for all of our Microservices?

Using Event Sourcing comes with it’s own considerations, like Reporting, fewer community support or less mature tools compared to regular data sources, awkward queries compared to what people are used to, etc.

So considering all that, I don’t think every single Microservice in an enterprise architecture needs to use Event Sourcing, and just like any other pattern in software engineering, we should be pragmatic and just use the tool and pattern where it makes the most sense.

Going back to the definition of Microserices, the idea was that each service or team will decide what makes the most sense to deliver the business requirements in the most efficient way, and I believe using or not using Event Sourcing in a particular Microservice is a similar decision that needs to be made by the team based on the business requirements.

### Some Event Sourcing tools

The following are some of the tools that are used for Event Sourcing:

#### 1. Event Store ([Open Source](https://github.com/EventStore/EventStore))

> Event Store stores your data as a series of immutable events over time, making it easy to build event-sourced applications.

> Event Store has a native HTTP interface based on the AtomPub protocol which is plenty fast enough for the majority of use cases. For high-performance use, there are native drivers for .NET, Akka and Erlang.

[**Event Store**  
*The open-source, functional database with Complex Event Processing in JavaScript.*eventstore.org](https://eventstore.org/ "https://eventstore.org/")

#### 2. Eventuate ([Open Source](https://github.com/RBMHTechnology/eventuate))

> The Eventuate™ Platform provides a simple yet powerful event-driven programming model that solves the distributed data management problems inherent in a microservice architecture.

[**Eventuate**  
*The Eventuate™ Platform provides a simple yet powerful event-driven programming model that solves the distributed data…*eventuate.io](http://eventuate.io/ "http://eventuate.io/")

#### 3. Akka, Akka.Net ([Open Source](https://github.com/akka/akka))

> Akka is a toolkit for building highly concurrent, distributed, and resilient message-driven applications for Java and Scala

[**Akka | Akka**  
*Build powerful reactive, concurrent, and distributed applications in Java and Scala*akka.io](https://akka.io/ "https://akka.io/")

> Akka.NET is a toolkit and runtime for building highly concurrent, distributed, and fault tolerant event-driven applications on **.NET**& **Mono**.

[**Akka.NET Documentation | Akka.NET Documentation**  
*As a parent, the actor is responsible for handling its children's failures (so-called supervision), forming a chain of…*getakka.net](http://getakka.net/ "http://getakka.net/")

#### 4. Apache Kafka ([Open Source](https://www.apache.org/dyn/closer.cgi?path=/kafka/1.0.0/kafka-1.0.0-src.tgz))

> Apache Kafka® is a distributed streaming platform. We think of a streaming platform as having three key capabilities:

> It lets you publish and subscribe to streams of records. In this respect it is similar to a message queue or enterprise messaging system.

> It lets you store streams of records in a fault-tolerant way.

> It lets you process streams of records as they occur.

[**Apache Kafka**  
*Apache Kafka: A Distributed Streaming Platform.*kafka.apache.org](https://kafka.apache.org/ "https://kafka.apache.org/")

And many more …

**Next Steps:**

In the next part of this series, I will integrate some Microservies we build in [part 2 of this series](https://koukia.ca/a-microservices-implementation-journey-part-2-10c422a4d402), with an API Gateway so we can orchestrate calls into multiple Microservices from a web client.

**Looking for part 4 ? Continue reading:**

[**A Microservices implementation journey — Part 4**  
*I hope you read the First , Second and Third part of this Microservices Implementation Journey and found them useful…*koukia.ca](https://koukia.ca/a-microservices-implementation-journey-part-4-9c19a16385e9 "https://koukia.ca/a-microservices-implementation-journey-part-4-9c19a16385e9")

If you are interested in reading more about Microservices Architecture topic, here are some relevant books:

[![](https://cdn-images-1.medium.com/max/800/1*TmXYeiITDomYKHKB4hLFRA.jpeg)](https://www.amazon.com/gp/product/1491950358/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491950358&linkId=363e9cf9c6a5a697a73b4fe159f37fda)*Building Microservices, Designing fine-grained systems*

[![](https://cdn-images-1.medium.com/max/800/1*M2r6FPQWHiiMN4CwwKcWpg.jpeg)](https://www.amazon.com/gp/product/1491965975/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491965975&linkId=ff04688c2c60121309905c5e0117b145)*Production Ready Microservices, Building Standardized systems across an engineering organization*

[![](https://cdn-images-1.medium.com/max/800/1*sNGTvyO3HCE2KjuaDycQnQ.jpeg)](https://www.amazon.com/gp/product/1491956259/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491956259&linkId=dd181a962e6fe756e0a81861258eb9c2)*Microservices Architecture, Aligning Principles, Practices and Culture*

[![](https://cdn-images-1.medium.com/max/800/1*3ufEsBu_Ajg_VpTLuTKHgg.jpeg)](https://www.amazon.com/gp/product/B0758YB73N/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B0758YB73N&linkId=9b1df16a450d563f1f9b905ae533d9d1)*Building Microservices with Asp.Net Core*

Cheers!
