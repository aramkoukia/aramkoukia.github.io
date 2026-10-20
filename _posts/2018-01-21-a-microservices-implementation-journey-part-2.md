---
layout: post
title: "A Microservices implementation journey — Part 2"
date: 2018-01-21
description: "In the first part of this Microservices implementation journey, I explained some of the details of a Microservices Architecture as I…"
image: https://cdn-images-1.medium.com/max/1200/1*RT7LV0doS1Ue7o7Yu9sdYQ.png
medium_url: https://medium.com/@aramkoukia/a-microservices-implementation-journey-part-2-10c422a4d402
---

### A Microservices implementation journey — Part 2

![](https://cdn-images-1.medium.com/max/1200/1*RT7LV0doS1Ue7o7Yu9sdYQ.png)*Image from “.NET Microservices — Architecture for Containerized .NET Applications” book: <http://aka.ms/MicroservicesEbook>*

In the [first part of this Microservices implementation journey](https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917), I explained some of the details of a Microservices Architecture as I understand it, and I got really good feedback from around the world, a lot of people liked it a lot, so If you didn’t read it already, I highly recommend you do it now:

[**A Microservices implementation journey — Part 1**  
*Well, it’s that time where everyone is talking about Microservice, what they are, how they work, etc, and here I am…*koukia.ca](https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917 "https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917")

In this second part, I will show you how you can implement a set of simple Microservices considering the architecture I recommended in the [previous post](https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917). To refresh your mind, here is the high level Architecture diagram we talked about:

![](https://cdn-images-1.medium.com/max/800/1*pVMJsM6m4bzuSZzoGitSKQ.png)

In this part I am going to show you some code that will live inside a Domain Microservice and Read Model Microservice.

So without further rant, let’s get to implementation.

### Software and Libraries you need

In terms of the language and framework, I will use C# and Asp.Net Web API.

The following are the software and nuget package libraries that I use for this implementation. Though for each one of these pieces there are other alternatives, I chose these ones because it helped me to implement what I wanted a bit quicker.

#### [1. Redis](https://redis.io/)

I will use Redis as our Read Model and NoSQL Storage. It is very easy to install and configure. You can follow the configuration documentation on their website from the following link.

> Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker.

[**Redis**  
*Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker…*redis.io](https://redis.io/ "https://redis.io/")

As far as the Nuget package goes, for interacting with Redis from C#, I use the StackExchange.Redis nuget package as Redis client.

#### [2. RabitMQ](https://www.rabbitmq.com/)

For our “Message Bus” component I will use RabitMQ. It is a very famous, widely used, Open Source Message Broker, and it is one of the simplest ones in terms of configuration.

Note: [Azure Service Bus](https://azure.microsoft.com/en-ca/services/service-bus/) is another alternative, that will probably be your better option if you are planning to use Microsoft Azure as your cloud infrastructure.

> With more than 35,000 production deployments of RabbitMQ world-wide at small startups and large enterprises, RabbitMQ is the most popular open source message broker.

For download and configuration of RabitMQ you can follow the instructions from the following link:

[**RabbitMQ - Messaging that just works**  
*RabbitMQ is lightweight and easy to deploy on premises and in the cloud. It supports multiple messaging protocols…*www.rabbitmq.com](https://www.rabbitmq.com/#getstarted "https://www.rabbitmq.com/#getstarted")

As far as the Nuget library to interact with RabbitMQ goes, I use the EasyNetQ library as RabbitMQ client that provided very good APIs for our purposes.

#### [3. EventStore](https://eventstore.org/)

EventStore as a tool, has done a very good job on picking up a name for their tool … turns out it is an Event Store!

I am going to use this as our Event Store, to keep our event history used by our Domain Microservice.

> Event Store stores your data as a series of immutable events over time, making it easy to build event-sourced applications

To configure your Event Store, use follow the instructions from the following link:

[**Getting Started - Event Store**  
*The open-source, functional database with Complex Event Processing in JavaScript.*eventstore.org](https://eventstore.org/docs/introduction/4.0.2/ "https://eventstore.org/docs/introduction/4.0.2/")

### Implementation

Alright, first things first, let’s talk about the features we need and the components that will provide these functionalities.

#### First set of Microservices:

1. **Products Domain Microservice**

As discussed in the [Architecture part of these Microservices series](https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917) and [CQRS Principles](https://martinfowler.com/bliki/CQRS.html), Domain Microservices are supposed to only handle Commands, so this Product Domain Microservice will handle “Create” and “Update” commands related to Products that our system will ultimately be able to sell.

Commands to be implemented:

- CreateProduct Command
- AlterProduct Command

And based on these commands this Product Domain Microservice will also publish 4 types of Events to our Event Store as well as the Service Bus for other Microservices to pick up:

- ProductCreated event
- ProductNameChanged event
- ProductDescriptionChanged event
- ProductPriceChanged event

**2. Products Read Model Microservice**

Again [as discussed earlier](https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917) and [CQRS Principles](https://martinfowler.com/bliki/CQRS.html), Read Model Microservices will only be able to handle Queries and so in the Products Read Model Microservice we will implement methods to handle the following Queries:

- Get All Products
- Get Product by Id

#### Second Set of Microservices

1. **Sales Domain Microservice**

Same as the Product Domain Microservice, Sales Domain Microservice only handles “Commands” as well. This Microservice only handles one command.

Commands to be implemented:

- Start New Order Command

And based on this command this Sales Domain Microservice will also publish 2 types of Events to our Event Store as well as the Service Bus for other Microservices to pick up (Maybe Shipment Microservice, and Finance Microservice):

- OrderPlaced event
- OrderPaidFor event

**2. Sales Read Model Microservice**

Similar to the Product Ream Model Microservice, Sales Read Model Microservice will only be able to handle Queries and so we will implement methods to handle the following Queries:

- Get All Orders
- Get Order by Id

#### **Microservices Common Code**

Just like any software we are always dealing with common and/or crosscutting code, and Microservices architecture is no exception.

Though some argue that coupling even at helper libraries can be a big deal and should be avoided, for sake of simplicity I am going to use some shared code that will be used in all Microservices.

The pieces that are common (I will go through the reason why this is not a good idea to share any functionality at all in the next part) are the following:

- Service Bus (RabitMQ) Publisher and Subscriber code, to Publish messages to Service bus based on the Commands that are being handled, and to listen to “Topics” that the Read Model Service is subscribed to.
- Redis Repository to be used by Read Models to read the data, and to be used by Event Handlers to update Redis data when Events that the service is subscribed to are received.
- Aggregate classes to find out the final state of objects from the Event Store based on all the Events that is logged in the Event Store for that object.

### Sharing Code or Functionality among Microservices

Having all these cross cutting code and libraries, and forcing every Microservice team to use them (Stuff like: Security, Client Contracts, Logging, Caching, Generic Data Access layers) will force the teams to stick with a specific technology. Microservice teams are supposed to be free to use the greatest technology that they think fits their service purposes.

Providing Client Libraries will hold the teams back to freely (As it is one of the points of having Microservices Architecture) move on to the next great technology stack out there.

Also any change to these dlls would cause a “Force Redeploy” of the components that are supposed to be “Independently Deployable” by the Microservices Architecture definition.

This might sound like a violation of [DRY principal](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) (Don’t repeat yourself), which I guess as far as Microservices Architecture is concerned, it is recommended not to worry about this one at all, because independence and autonomy is more important for us in this architecture.

To summarize this last piece:

> MICROSERVICES DO NOT SHARE FUNCTIONALITY, CODE OR DATA.

The moment Microservices share functionality, that architecture turns into a traditional Service Oriented Architecture (SOA) with an unacceptable level of coupling.

![](https://cdn-images-1.medium.com/max/800/1*8XlfA9PZbAm7vUSPjwGFbA.gif)*Microservices do not share functionality and/or data.*

### Product Domain Microservice Implementation

The following code map diagram shows the pieces inside our Products Domain Microservice, which is responsible for handling Product Commands:

![](https://cdn-images-1.medium.com/max/800/1*KNcN2e764YAAWbY3S4FtRA.png)*Products Domain Data Service Code Map (Generated with Visual Studio 2017 Code Map tool)*

**Show me the ProductsController**

Now let’s see the code for each one of these boxes, starting with the Product Controller. The following code is what goes inside the Product Controller to handle the commands:

As you can see all this controller does is to Create Commands, Populate Each Command’s properties based on the passed in values, and pass the populated Command to the Command Handler.

#### Show me the Product Commands

Product Commands are just simple POCO classes and there is no business logic in them. The following code snippet is how our two CreateProduct and AlterProduct Commands look like:

**Show me the Product Command Handlers**

Product Command Handler is the piece that figures out what is happening to the product and calls the proper Domain method in the Product Domain Class.

As you saw in the controller, based on the End Point that is called by the client, the Products Controller decides which type of Command (Create or Alter) to instantiate, and then it passes that Command object to the handler.

The following snippet shows what happens inside the Product Command Handlers:

As you can see, we have different overloads of the “Handle” method that each one works with a specific command type. One to handle commands of type “CreateProduct” and one to handle commands of type “AlterProduct”.

These handlers are also good candidates to do validations around the passed in values for each command.

Inside of each handler after validating the inputs, you instantiate the “Product” domain object and call the appropriate method on the product object to do the operation.

As you can see, the implementation is following Object Oriented principal properly, as all these methods/operations are defined inside the Business Object which is the Product in this case.

**Show me the Product Domain Class**

Now let’s see the implementation of the Product Domain class, which basically has all the business logic related to Products. The nice thing about this is that you don’t have one layer that all the business logic related to different classes are there. Instead each Domain class contains business logic related to itself and these Domain classes are pretty self contained.

Just by looking at the Product Domain object you can understand all the things you can do with a products.

The following code snippet is what is happening in the Product Domain Class:

If you look closely to all the public methods available, they all do the same thing: Validate the input, and ApplyEvent, and pass in the proper event to the ApplyEvent method.

Then in the calling code which is the “Hander”, the “repository.Save” method is called that will persist these events in the Event Store and also publish them to the Service Bus.

That’s pretty much it for the Product Domain Microservice. Though there are some bits of code that I didn’t go into much detail about them ([You can find the full code on github](https://github.com/aramkoukia/microservices-prototype)), the way you implement those pieces, like EventStore Repository, or RabitMQ handlers, should not affect the overall design of your Microservice.

The idea is, those integration with Event Store or RabitMQ should be easily replaceable with some other technology if you want, so how I write them or the details around dealing with RabitMQ or EventStore is not relevant to our Microservices Architecture.

### Product Read Model Microservice Implementation

The following code map diagram shows the pieces inside our Products Read Model Microservice, which is responsible for handling Product Queries:

![](https://cdn-images-1.medium.com/max/800/1*dwmdJ-3hYkZRJLfoYxkmnw.png)*Products Domain Data Service Code Map (Generated with Visual Studio 2017 Code Map tool)*

**Show me the Read Model Product Controller**

Let’s see what’s happening inside of each of these classes, starting with the Product Controller.

[As discussed in the Microservices Architecture article](https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917), the Read Model controller will only be able to handle Queries. In our service we support Get All Products and Get Product By Id queries. The following code is what we need in our Read Model Product Controller:

This is pretty simple and nothing much going on here as it is just a pass through to our ProductView class using a ServiceLocator static class.

ProductView is simply a static member in the ServiceLocator class to decouple the View classes from the Read Model Controllers.

Imagine if you had multiple views in this service, now with introducing this “Service Locator” class, we don’t have to reference them all in our controller and we just reference the “Service Locator” in the controller.

**Show me the ProductView class**

Product view class has two different set of functionality in it which potentially can be split if you need to.

1. First piece is the Get calls to the Redis repository to get the product information.
2. Second piece is the Event handlers where it is listening to events related to products in order to update our Read Model (insert or update or delete stuff from our Redis read model)

If you wanted to scale your Event handling piece separate from your Read Model logic and put them in separate Microservices it is totally fine and a lot of people design their services like that.

The following is what is going on in the ProductView class:

The Get calls in this class are pretty straightforward as they are direct calls to Redis to get the data like: repository.Get(id).

If you look at the signature of the class, it implements the Handlers for different Event types. By implementing those handlers we are subscribing to Events published to RabitMQ and those handlers will raise relevant events when those events happen in the system.

In this case we are listening to the following events:

```
IHandle<ProductCreated>
```

```
IHandle<ProductDescriptionChanged>
```

```
IHandle<ProductNameChanged>
```

```
IHandle<ProductPriceChanged>
```

And for each one of these we implement the relevant “Apply” code to update our Read Model. For instance if the Event is Product Created we add the Product to ReadModel, and if the Name has changed we update the Read Model with the updated entity.

**Solution Structure**

Here is how I have organized my projects inside the Products Microservices that has my Domain Product Service and Read Model Product Service:

![](https://cdn-images-1.medium.com/max/800/1*JoCZgYzlOssMF30faAtcog.png)*Domain Product Service and Read Model Product Service solution structure*

### Sales Domain Microservice Implementation

The second set of services that we are going to look at are the Sales ones.

The following code map diagram shows the pieces inside our Sales Domain Microservice, which is responsible for handling Sales Commands:

![](https://cdn-images-1.medium.com/max/800/1*IZQJO-k7T7kEcGqnaG7Swg.png)*Sales Domain Microservice code map diagram, generated by Visual Studio Code Map tool*

**Show me the Orders Controller**

Now let’s see the code for each one of these boxes, starting with the Orders Controller. The following code is what goes inside the Sales Controller to handle the command:

Similar to the Products Controller in Products Domain Service, as you can see all this Orders Controller does is to create a new StartNewOrder command, populate its properties (Id, ProductId, Quantity) based on the passed in values, and pass the populated Command to the Command Handler.

#### Show me the Order Commands

Order Commands are just simple POCO classes and there is no business logic in them. The following code snippet is how the StartNewOrder Command look like:

**Show me the Order Command Handlers**

Order Command Handler is the class that figures out what is happening to the Order and calls the proper Domain method in the Order Domain Class.

As you saw in the controller, based on the End Point that is called by the client, the Orders Controller decides which type of Command (New Order or OrderPaid) to instantiate, and then it passes that Command object to the handler.

The following snippet shows what happens inside the Order Command Handlers:

Again very similar to the Product Command Handler class, we have different overloads of the “Handle” method that each one works with a specific command type. One to handle commands of type “StartNewOrder” and one to handle commands of type “PayForOrder”.

These handlers are also good candidates to do validations around the passed in values for each command.

Inside of each handler after validating the inputs, you instantiate the “Order” domain object and call the appropriate method on the product object to do the operation.

Again the lovely part is the relevant methods for Order objects, like “Start New Order” or “Pay For Order” methods live within the Order Domain object, following some of the basics of Object Oriented properly.

**Show me the Order Domain Class**

Now let’s see the implementation of the Order Domain class, which basically has all the business logic related to Orders. The nice thing about this is that you don’t have one layer that all the business logic related to different classes are there. Instead each Domain class contains business logic related to itself and these Domain classes are pretty self contained. i.e: You “Create New” Orders and you “Pay” orders, and in order to do that in the code you go:

orderObject.CreateNew(The Arguments), or orderObject.Pay(arguments)

I think it is really nice, compared to what you are used to using a regular Repository pattern, where the repository layer is just a data access layer that doesn’t do much!

Just by looking at the Order Domain object you can understand all the things you can do with an Order.

The following code snippet is what is happening in the Order Domain Class:

If you look closely to all the public methods available, they all do the same thing: Validate the input, and ApplyEvent, and pass in the proper event to the ApplyEvent method.

Then in the calling code which is the “Hander”, the “repository.Save” method is called that will persist these events in the Event Store and also publish them to the Service Bus.

That’s pretty much it for the Sales Domain Microservice, plus some of the shared pieces that I explained in the Product Domain Service section.

### Sales Read Model Microservice Implementation

The following code map diagram shows the pieces inside our Sales Read Model Microservice, which is responsible for handling Order Queries:

![](https://cdn-images-1.medium.com/max/800/1*fq2FJn06r7t9M3nTFLlvBw.png)*Sales Read Model Microservice code map, generated by Visual Studio Code Map tools*

**Show me the Read Model Orders Controller**

Let’s see what’s happening inside of each of these classes, starting with the Orders Controller.

Similar to any Read Model Microservice, this Read Model controller will also only be able to handle Queries. In our service we support Get All Orders and Get Order By Id queries. The following code is what we need in our Read Model Orders Controller:

This is pretty simple and nothing much going on here as it is just a pass through to our OrderView class using a ServiceLocator static class.

OrderView (similar to ProductView) is simply a static member in the ServiceLocator class to decouple the View classes from the Read Model Controllers.

Imagine if you had multiple views in this service, now with introducing this “Service Locator” class, we don’t have to reference them all in our controller and we just reference the “Service Locator” in the controller.

**Show me the OrderView class**

Order View class has two different set of functionality in it which potentially can be split if you need to.

1. First piece is the Get calls to the Redis repository to get the product information.
2. Second piece is the Event handlers where it is listening to events related to orders in order to update our Read Model (insert or update or delete stuff from our Redis read model)

If you wanted to scale your Event handling piece separate from your Read Model logic and put them in separate Microservices it is totally fine and a lot of people design their services like that.

The following is what is going on in the OrderView class:

The Get calls in this class are pretty straightforward as they are direct calls to Redis to get the data like: repository.Get(id).

If you look at the signature of the class, it implements the Handlers for different Event types. By implementing those handlers we are subscribing to Events published to RabitMQ and those handlers will raise relevant events when those events happen in the system.

In this case we are listening to the following events:

```
IHandle<OrderPlaced>
```

```
IHandle<OrderPaidFor>
```

And for each one of these we implement the relevant “Apply” code to update our Read Model. For instance if the Event is “New Order Created” we add the new Order to ReadModel, and if the Order is “Paid” we update the Read Model with the updated status of the Order.

#### Integration Point and Coupling Smell

In this OrderView class the “IHandle<OrderPlaced>” method there is something to think about and debate different possible integration approaches.

The requirement here has been, when an Order is placed, we need to get the Product Name and Product Description From Product Id.

What I have done here is basically having a direct integration/call to Product Read Model Microservice, and getting the missing pieces of information.

Since we are using Redis as our read model some people argue that it is Ok, but I believe it is sort of tight coupling.

Another approach would be, in Orders Read Model, we could Handle the Product Created events raised by Product Domain Service and update Order Read Model Service with the Product information, so we are basically completely separated ourselves from the Product Service Availability. If we do this then orders can go through even if the Product Service Read Model is completely offline!

**I would really like to here more ideas about this sort of scenario from you all, so please send them my way!**

#### **Solution Structure**

Here is how I have organized my projects inside the Sales Microservices that has my Domain Sales Service and Read Model Sales Service:

![](https://cdn-images-1.medium.com/max/800/1*-SBA_SeH9JV9NdTu-y9u0A.png)

And that’s the end of our 4th Microservice.

You can find the complete solution so far on github:

[**aramkoukia/microservices-prototype**  
*Contribute to microservices-prototype development by creating an account on GitHub.*github.com](https://github.com/aramkoukia/microservices-prototype/tree/master "https://github.com/aramkoukia/microservices-prototype/tree/master")

Next steps:

In the next part of this series, I will explain the reasons behind using Event Sourcing, and Service Bus, and when we need to use one or the other or both:

[**A Microservices implementation journey — Part 3**  
*I hope you read the First and Second part of this Microservices Implementation Journey and found them useful and if you…*koukia.ca](https://koukia.ca/a-microservices-implementation-journey-part-3-50f030ba6bb5 "https://koukia.ca/a-microservices-implementation-journey-part-3-50f030ba6bb5")

integrate these services with an API Gateway so we can orchestrate calls into multiple Microservices from a web client.

If you are interested in reading more about Microservices Architecture topic, here are some relevant books:

[![](https://cdn-images-1.medium.com/max/800/1*TmXYeiITDomYKHKB4hLFRA.jpeg)](https://www.amazon.com/gp/product/1491950358/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491950358&linkId=363e9cf9c6a5a697a73b4fe159f37fda)*Building Microservices, Designing fine-grained systems*

[![](https://cdn-images-1.medium.com/max/800/1*M2r6FPQWHiiMN4CwwKcWpg.jpeg)](https://www.amazon.com/gp/product/1491965975/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491965975&linkId=ff04688c2c60121309905c5e0117b145)*Production Ready Microservices, Building Standardized systems across an engineering organization*

[![](https://cdn-images-1.medium.com/max/800/1*sNGTvyO3HCE2KjuaDycQnQ.jpeg)](https://www.amazon.com/gp/product/1491956259/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491956259&linkId=dd181a962e6fe756e0a81861258eb9c2)*Microservices Architecture, Aligning Principles, Practices and Culture*

[![](https://cdn-images-1.medium.com/max/800/1*3ufEsBu_Ajg_VpTLuTKHgg.jpeg)](https://www.amazon.com/gp/product/B0758YB73N/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B0758YB73N&linkId=9b1df16a450d563f1f9b905ae533d9d1)*Building Microservices with Asp.Net Core*

> If you liked this article, click the👏 below so other people will see it here on Medium.

> Let’s be friends on [Twitter](https://twitter.com/aramkoukia). Happy Coding :)

Cheers!
