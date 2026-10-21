---
layout: post
title: "A Microservices implementation journey — Part 4"
date: 2018-02-25
description: "I hope you read the First , Second and Third part of this Microservices Implementation Journey and found them useful and if you didn’t I…"
image: https://cdn-images-1.medium.com/max/1200/1*ezLkH8bj_59SICLI5Yv4xw.png
tags: ["Architecture", "AWS", "Product & Agile"]
---

### A Microservices implementation journey — Part 4

![](https://cdn-images-1.medium.com/max/1200/1*ezLkH8bj_59SICLI5Yv4xw.png)*Azure API Management as API Gateway. Picture from: <https://docs.microsoft.com>*

I hope you read the [First](https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917), [Second](https://koukia.ca/a-microservices-implementation-journey-part-2-10c422a4d402) and [Third](https://koukia.ca/a-microservices-implementation-journey-part-3-50f030ba6bb5) part of this [Microservices Implementation Journey](https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917) and found them useful and if you didn’t I recommend you do!

Here are the links for the previous parts:

**Part 1:** <https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917>

**Part 2:** <https://koukia.ca/a-microservices-implementation-journey-part-2-10c422a4d402>

**Part 3:** <https://koukia.ca/a-microservices-implementation-journey-part-3-50f030ba6bb5>

### Do we need this “API Gateway” thing at all?

Well, Netflix is doing it, so …

[**Optimizing the Netflix API**  
*how we redesigned our API to help UI teams meet their needs*medium.com](https://medium.com/netflix-techblog/optimizing-the-netflix-api-5c9ac715cf19 "https://medium.com/netflix-techblog/optimizing-the-netflix-api-5c9ac715cf19")

But on a more serious note, I think such a layer is required to abstract away some of the complexity and concerns that a Microservices Architecture creates.

I compiled a list of drivers for us to have an API Gateway in a Microservices Architecture:

- The way the APIs would provide the data is probably going to be very different from the way the client would need it. Usually Microservices will have very chatty APIs, and for the client to complete one scenario, they need to make several API calls possibly across multiple services. So API Gateway can address this issue for the client.
- The data itself is something that might be an issue. For example the data that a Web Application needs or expects from a Mobile App might be different. In some cases we could force different kinds of clients use the same APIs but as you could imagine, it will be the “one-size-fits-all” situation and it is not going to be very efficient for some clients. With API Gateway we can customize the existing API outputs and serve the data that each client needs.
- Network could also be an issue, if we use the same API responses for all kinds of clients. Generally mobile networks are much slower that WAN networks and also WAN is slower than LAN. So if we are making multiple API calls in a LAN based application, the performance impact might not be as obvious, but if we do the same thing in a mobile app, the user experience will be degraded.
- The number of Microservice instances and their physical host information could change over time and having an API Gateway could hide all those changes from the consumers.
- If things change in our Microservices environment, for example we decide that one functionality does not belong to one Microservice, and decide to move it to another one, we could still abstract that change from the clients using an API Gateway.
- Some of the Microservices might use protocols that are not web friendly, so communicating directly with web or mobile client can be tricky, but having an API gateway could address this issue.
- You could use this layer to make sure your API stays backward compatible. Having backward compatible APIs are very important specially when you have Mobile clients, where you don’t really have much power to force them to upgrade their app if you make breaking changes to your API.

### Any drawbacks for using API Gateways?

Obviously there are drawbacks using this pattern. Here are some for you to think about:

- We are adding this additional component to the architecture which potentially adds some overhead in terms of management, monitoring, implementing, etc. Basically it is one more thing to worry about!
- Any change in the Microservices, would need a change in the API Gateway. Basically we have abstracted away the changes in our Microservices from our Clients perspective, but we still need to make modifications to the API Gateway to accommodate any Microservice change.
- Could potentially be a single point of failure. If you look at the Architecture diagram again, it is obvious that every request would go through this component, so if that goes south, we have a serious problem! So we need to make sure that it is the highest available component that we have (Same with our Service Bus!)
- Also some might worry that it might not perform very well under load. So we should make sure we do proper benchmark before piking a tool as our API Gateway to be sure that it can handle the scale that we expect from it.

### What are my options for an API Gateway?

If you are convinced that having an API Gateway is something you want in your Architecture, let’s go through some of the products that are available out there for us:

1. [Azure API Management](https://azure.microsoft.com/en-us/services/api-management/)

> Use Azure API Management as a turnkey solution for publishing APIs to external and internal customers. Quickly create consistent and modern API gateways for existing back-end services hosted anywhere, secure and protect them from abuse and overuse, and get insights into usage and health. Plus, automate and scale developer onboarding to help get your API program up and running.

[2. Google Apigee API Platform](https://cloud.google.com/apigee-api-management/)

> Apigee is a full lifecycle API management platform that enables API providers to design, secure, deploy, monitor, and scale APIs. Apigee sits in-line with runtime API traffic and enforces a set of out-of-the-box API policies, including key validation, quota management, transformation, authorization, and access control. API providers use the customizable developer portal to enable developers to consume APIs easily and securely, and to measure API performance and usage.

[3. Graphql](http://graphql.org/)

> GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. GraphQL provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need and nothing more, makes it easier to evolve APIs over time, and enables powerful developer tools.

4. [Netflix Hystrix](https://github.com/Netflix/Hystrix)

> Hystrix is a latency and fault tolerance library designed to isolate points of access to remote systems, services and 3rd party libraries, stop cascading failure and enable resilience in complex distributed systems where failure is inevitable.

[5. Amazon API Gateway](https://aws.amazon.com/api-gateway/)

> Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. With a few clicks in the AWS Management Console, you can create an API that acts as a “front door” for applications to access data, business logic, or functionality from your back-end services, such as workloads running on Amazon Elastic Compute Cloud (Amazon EC2), code running on AWS Lambda, or any Web application.

Each of these tools (and many more are out there for sure) have some cool features, and based on your requirements and your special needs I guess you could investigate them and with some POC pick your poison!

Now for this article I am going to demonstrate the [Azure API Management](https://azure.microsoft.com/en-us/services/api-management/) and use expose some of APIs through it.

### Setting up Azure API Management

Azure API Management is a very fast to get up and running solution for publishing APIs to external and internal clients. It enables you to create API gateways for existing Micoservices hosted on Azure or your own data center.

From the Azure portal, here are some of the API Management features:

- *Provide API documentation and an interactive console*
- *Throttle, rate limit and quota your APIs*
- *Monitor health of your APIs and quickly identify errors*
- *Bring modern formats like JSON and REST to existing APIs*
- *Connect to APIs hosted anywhere on the Internet or on-premises and publish globally*
- *Gain analytic insights on how your APIs are being used*
- *Manage your service via the Azure portal, REST API, PowerShell, or Git repository*

To get started, you can login to Azure Portal: <https://portal.azure.com> , clink on New, and search for “API Management”, and select the first one from the result, just like the following picture and click “Create”

![](https://cdn-images-1.medium.com/max/800/1*k8xv55xQc6Q5WCCegtRJMw.png)

In the next screen, you can enter the name for your API Gateway, and most importantly the “SLA” or “Service Level Agreement” which is the availability of your API Gateway.

As we discussed earlier, since this component could be our “single point of failure” we should make sure the SLA that we select is aligned with our expectations in terms of high availability.

![](https://cdn-images-1.medium.com/max/800/1*ffo3SYMRfvOjwJpeF_eXiA.png)

And that’s it, our API Gateway is deployed to Azure and there is already monitoring in place for it. If you navigate to the service in the Azure portal you will see the service status and the monitoring widget:

![](https://cdn-images-1.medium.com/max/800/1*bykcXIrx_hD8OEZw2Zjvow.png)

### Configuring our API Gateway

Now that out API Gateway is up and running, let’s take a look and try to integrate it with some APIs.

If you click on the “APIs” menu in the left pane, you can see that first thing you need to do is to add an API to the Gateway to start playing around.

![](https://cdn-images-1.medium.com/max/800/1*n8dyU7PYaZEpT5t9q23BAg.png)

As you can see in the above picture, you can add an Empty API (for cases where you don’t have a public API available yet), or an API with Open API Specification (formerly known as Swagger enabled API), a REST or SOAP API with WSDL, an Azure Logic App API, API App or an Azure Function.

So you pretty much can mix and match all sort of API that you might have in your system, consolidate them all and provide your clients with a good experience with dealing with just your API Gateway.

### Azure API Management Developer Portal

One of the very cool features of Azure API Management is the Developer Portal. With this you can point all consumers of your APIs to that, have them sign up, see documentation and start building their code.

You as the administrator of the Developer Portal can totally customize the look and feel of this portal to make it look like your own company’s theme and brandings.

The following is the default UI that is deployed when you create your Azure API Management:

![](https://cdn-images-1.medium.com/max/1200/1*1CU-5TIHBg-9Wz0Mad3M8g.png)*Azure API Management — Default Developer Portal*

### Adding your first API to the Gateway

For testing purposes I am going to use a publicly available API that has OpenAPI specification, so you can see how it works.

I am going to use the following public API, but you can use your own Swagger/OpenAPI enabled API.

<http://conferenceapi.azurewebsites.net/?format=json>

So from the APIs menu, click on the “OpenAPI Specification”, and enter the above URL in the “Open API Specification” field, and it will populate the name from the Specification, though you can change the name if you wish.

![](https://cdn-images-1.medium.com/max/800/1*breybqU-5vo-LrAXEus-sg.png)*Adding an API to Azure API Management using OpenAPI Specification*

At this point you can choose to add versioning to this API or not. Azure API management can handle versioning with “Path”, “Request Header” or “Query String”:

![](https://cdn-images-1.medium.com/max/800/1*7Se9Bfd08QCF_8CJJ8L5sA.png)*Azure API Management Versioning options*

When you click Create, it will create all your APIs for you just like the following picture as a good starting point:

![](https://cdn-images-1.medium.com/max/1200/1*1n2xWN6XQogRssZl7G_BHQ.png)*All Available APIs from the OpenAPI Specifications*

If you click on any of the APIs on the left, for each one you have some stuff on the right that you can do.

#### Frontend:

In this section you can see what is being returned to the client. and you can also modify the body that is being returned, add some headers etc.

![](https://cdn-images-1.medium.com/max/800/1*A77QiOrTrrd0FsOo7-Cspw.png)*Azure API Management — Frontend*

#### Inbound Processing:

In this section, you can intercept the calls that comes to this API from the client, and do some manipulations or run some policies, and then send the request to the backend service or not!

![](https://cdn-images-1.medium.com/max/800/1*0iXaT0xLe0qWAaSEJdp5jQ.png)*Azure API Management — Inbound Processing*

There are some built in Policies that you can apply, but if you want something specific you can build it yourself:

![](https://cdn-images-1.medium.com/max/800/1*hTdVax5qdVlJWCb7U9XikA.png)*Some Available Policies to pick from*

**Caching, Authentication, Retry or Mocking policies are some good built-in ones that you can consider.**

#### Outbound Processing:

Similar to Inbound Processing, with Outbound Processing we can intercept the responses that are being returned to the client and after any manipulation return the response to the Client or not.

![](https://cdn-images-1.medium.com/max/800/1*fiU6xRR7yAMKiL5-bSS1uw.png)*Azure API Management — Outbound Processing*

Again for this interception we can use some existing Policies or add our own policies.

#### **Backend:**

Backend section is the URL to your backend service for this API. Initially it is set to the same Url from your OpenAPI specification, but you can override it in this section.

![](https://cdn-images-1.medium.com/max/800/1*PtbnaKR8ccwZm0h2fb7qxA.png)*Azure API Management — Backend Settings*

### Products in Azure API Management

Products the approach we use to expose our AIPs to our consumers or clients.

Each Product in Azure API management can have one or more of our APIs in it. When we create Products, we can set them as “Open” or “Protected”. When we define a Product as Protected, for consumers to be able to use it, they need to subscribe to it through the “Developer Portal” of our API that I mentioned earlier, and if it is defined as Open, anyone can access those APIs without subscription.

In the Subscription model, you can also configure it to be “Auto Approval” or you can require an Administrator to approve new clients.

When you create the Azure API Management by default it creates 2 Products: Starter and Unlimited:

![](https://cdn-images-1.medium.com/max/800/1*JYzw3OkILsbZ0fLZOUlSvw.png)*Default Products available in Azure API Management*

After adding your APIs, you can add them to one of these products or create a new products.

Products have really cool features in order to manage your APIs:

The following is the page with all the Settings related to Products:

![](https://cdn-images-1.medium.com/max/800/1*0Fwmhs9KC4UpipgJHOWfXQ.png)*Azure API Management — Product Setting page*

The following is the page with all the Policies related to Products:

![](https://cdn-images-1.medium.com/max/800/1*sgR-D3wH42YdycWCjVnXqw.png)*Azure API Management — Product Policies page*

As you can see you can set some limits on the number of calls to the API for each subscription, and many more policies.

Now when your clients go to YOUR developer portal they will be able to see all the products, and all the APIs and features available for each product, they can subscribe, get API Keys and much more.

The following image is what your client will see in the developer portal, when they navigate to Products page:

![](https://cdn-images-1.medium.com/max/800/1*1Xn3vVLW63u7KzgfoXpxcA.png)*Your API’s Developer Portal — Products Page*

Also when they click on the API link (the one we just created), they can see the list of all available APIs, and even try them out with full documentation:

![](https://cdn-images-1.medium.com/max/800/1*itPcb6uJlW-U2hIMo3qmQw.png)*API Documentation that is exposed to your consumers*

There are much more features in Azure API Management which I let you go and explore.

Azure API Management is one of my favorite Azure features just because it gives you so much out of the box through settings, with just importing one OpenAPI Specification file!

#### What’s next?

In the [next part](https://koukia.ca/a-microservices-implementation-journey-part-5-d7d1b9d441e7), I will go through some useful patterns and libraries to build more resilient Microservices:

[**A Microservices implementation journey — Part 5**  
*I hope you read the First , Second, Third and Forth part of this Microservices*koukia.ca](https://koukia.ca/a-microservices-implementation-journey-part-5-d7d1b9d441e7 "https://koukia.ca/a-microservices-implementation-journey-part-5-d7d1b9d441e7")

If you are interested in reading more about Microservices Architecture topic, here are some relevant books:

[![](https://cdn-images-1.medium.com/max/800/1*TmXYeiITDomYKHKB4hLFRA.jpeg)](https://www.amazon.com/gp/product/1491950358/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491950358&linkId=363e9cf9c6a5a697a73b4fe159f37fda)*Building Microservices, Designing fine-grained systems*

[![](https://cdn-images-1.medium.com/max/800/1*M2r6FPQWHiiMN4CwwKcWpg.jpeg)](https://www.amazon.com/gp/product/1491965975/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491965975&linkId=ff04688c2c60121309905c5e0117b145)*Production Ready Microservices, Building Standardized systems across an engineering organization*

[![](https://cdn-images-1.medium.com/max/800/1*sNGTvyO3HCE2KjuaDycQnQ.jpeg)](https://www.amazon.com/gp/product/1491956259/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491956259&linkId=dd181a962e6fe756e0a81861258eb9c2)*Microservices Architecture, Aligning Principles, Practices and Culture*

[![](https://cdn-images-1.medium.com/max/800/1*3ufEsBu_Ajg_VpTLuTKHgg.jpeg)](https://www.amazon.com/gp/product/B0758YB73N/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B0758YB73N&linkId=9b1df16a450d563f1f9b905ae533d9d1)*Building Microservices with Asp.Net Core*

Cheers!
