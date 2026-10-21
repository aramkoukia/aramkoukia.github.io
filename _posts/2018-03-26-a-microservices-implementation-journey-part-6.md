---
layout: post
title: "A Microservices implementation journey — Part 6"
date: 2018-03-26
description: "If you have followed me recently I have been writing a series of articles around Microservices Architecture and Implementation. I hope you…"
image: https://cdn-images-1.medium.com/max/800/1*8GbrXbHdH5uPGMb5epWhrg.png
tags: ["Architecture", ".NET"]
---

### A Microservices implementation journey — Part 6

![](https://cdn-images-1.medium.com/max/800/1*8GbrXbHdH5uPGMb5epWhrg.png)*How to use Apache Kafka on Azure in a Microservices Architecture. Image from: [www.arctiq.ca](http://www.arctiq.ca)*

If you have followed me recently I have been writing a series of articles around Microservices Architecture and Implementation. I hope you read the [First](https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917), [Second](https://koukia.ca/a-microservices-implementation-journey-part-2-10c422a4d402), [Third](https://koukia.ca/a-microservices-implementation-journey-part-3-50f030ba6bb5), [Forth](https://koukia.ca/a-microservices-implementation-journey-part-4-9c19a16385e9) and [Fifth](https://koukia.ca/a-microservices-implementation-journey-part-5-d7d1b9d441e7) part of this [Microservices](https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917) I[mplementation Journey](https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917) and found them useful and if you didn’t I recommend you do!

Here are the links for the previous parts:

**Part 1:** <https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917>

**Part 2:** <https://koukia.ca/a-microservices-implementation-journey-part-2-10c422a4d402>

**Part 3:** <https://koukia.ca/a-microservices-implementation-journey-part-3-50f030ba6bb5>

**Part 4:** <https://koukia.ca/a-microservices-implementation-journey-part-4-9c19a16385e9>

**Part 5:** <https://koukia.ca/a-microservices-implementation-journey-part-5-d7d1b9d441e7>

If you followed along, [one of the main components of a Microservices Architecture](https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917), is ***Service Bus*** or ***Event Store*** components that enables our decoupled services to interact with each other in an asynchronous way.

There are several alternative technologies out there that we can use for this purpose, that I mentioned them [in the first part of this Microservices series](https://koukia.ca/a-microservices-implementation-journey-part-1-9f6471fe917).

The focus of this part of the series will be to show case Apache Kafka and use it as our Pub/Sub communication channel in our Microservices echo-system.

**And to make things even more interesting I will use Azure to host my Apache Kafka instance and will use an Asp.Net Web API to publish and subscribe to events from this Kafka cluster hosted in Azure.**

![](https://cdn-images-1.medium.com/max/800/1*os1hoijFv6Iupb11uKAKIA.gif)

If you are interested, get your cup of coffee or whatever your poison is and read on!

### What is Apache Kafka?

Before we get started with installation and other fun stuff, let’s see what Kafka is.

> **Apache Kafka® is a distributed streaming platform.**

![](https://cdn-images-1.medium.com/max/800/1*Jw-coW5Y9AqpiMzwZm4I3w.png)*Kafka® is used for building real-time data pipelines and streaming apps. It is horizontally scalable, fault-tolerant, wicked fast, and runs in production in thousands of companies. Image from: <https://kafka.apache.org/>*

#### Tell me more about Apache Kafka

Kafka has 3 main features:

- A publisher and Subscriber mechanism for streams of data, similar to an Event Store or an Enterprise Service Bus (Though Kafka’s approach for doing Event Sourcing it is somewhat different than Service Bus or some Event Stores)
- Kafka stores the streams of events/data in a very fault tolerant and durable way.
- Kafka processes streams of data as they occur in the Kafka cluster.

#### Can I use Kafka for any kind of application?

I think it can be used for any system that needs some sort of Messaging or Event Streaming but it is typically used in two types of architectures:

- If you need to move streams of data around in your system in real-time between applications Kafka is your technoly.
- If you need to identify events that happens in your system and then do something or trigger some workflow based on those events or streams of data, Kafka is your technology.

### How to use Apache Kafka on Azure in a Microservices Architecture

Without further due, let’s jump into Azure and stand up our Kafka Cluster.

In Azure Kafka cluster is deployed as part of the [Azure HDInsight](https://azure.microsoft.com/en-us/services/hdinsight/) service.

**Side note to see what else Azure HDInsight can do:**

> Azure HDInsight is a fully-managed cloud service that makes it easy, fast, and cost-effective to process massive amounts of data. Use popular open-source frameworks such as Hadoop, Spark, Hive, LLAP, Kafka, Storm, R & more. Azure HDInsight enables a broad range of scenarios such as ETL, Data Warehousing, Machine Learning, IoT and more.

So to get started, I sign in to Azure portal, and from the “create a Resource” menu search for “HDInsight”, and select the first result from the Marketplace and click “Create”:

![](https://cdn-images-1.medium.com/max/1200/1*Y3uS5QJMK44BCerIgGGb3w.png)*Creating Azure HDInsight on Azure portal*

Then you just need to enter the “Cluster Name”, “Cluster Type” (in this case we select Kafka, and as of today Azure just supports Linux operation system to host the cluster).

Then you enter the Cluster username and password, pick a “Resource Group” and click “Next”

![](https://cdn-images-1.medium.com/max/1200/1*nV9eIyqmQCPbfOdUcMi-Yw.png)*Configuring Apache Kafka on Azure HDInsight*

Next step is to select your storage. You can either select or create an Azure Storage account from the same Subscription that you are creating the HDInsights and Kafka cluster on, or use an Azure Storage Access key to use an storage from a different subscription.

![](https://cdn-images-1.medium.com/max/800/1*mErbnRcPdND8FuOnI8nScg.png)*Selecting Azure Storage for Kafka Cluster in HDInsight*

In the next step you can optionally select a third party application to be added to your HDInsight Cluster. Note that if you select any application that needs licenses, you need to bring your own license to be able to use the application. For now we don’t need any other applications so you can skip this step.

![](https://cdn-images-1.medium.com/max/800/1*ZC703POPm04G1t2rBZk32Q.png)*Selecting third party applications on Azure HDInsight*

Next step is to select the Kafka Cluster size and the number of Worker Nodes on the Cluster. In this step you can also select the Zookeeper node sizes.

As a minimum you need to have 3 worker nodes.

![](https://cdn-images-1.medium.com/max/800/1*7q3YA94EmotVfl6ua4QIag.png)*Configuring the size of the Kafka Cluster nodes*

When you select the number of the nodes and Cores for each node, you will see an estimate of your costs on the screen.

### **What is this** [**Zookeper**](https://zookeeper.apache.org/)**thing?**

![](https://cdn-images-1.medium.com/max/800/1*EpeacgGdYza4uC1-0EnjDA.png)*Apache ZooKeeper is an effort to develop and maintain an open-source server which enables highly reliable distributed coordination.*

> ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. All of these kinds of services are used in some form or another by distributed applications.

That’s pretty much it for setting up the Kafka cluster. just click next, and you will see a summary of all the configuration and an estimate of your cost. Once you reviewed everything and everything is all good to you, select “Create”.

![](https://cdn-images-1.medium.com/max/800/1*guM3SDA6NhrdYnYEcVFVYQ.png)*Kafka Cluster configuration review*

It will take few minutes to deploy your HDInsight and Kafka cluster. The time it takes to deploy depends on the size of the cluster, number of nodes and other settings.

![](https://cdn-images-1.medium.com/max/800/1*rb_H5L_mVmUqg9Zf2GtkzA.png)*HDInsight Cluster overview page*

As you can see HDInsight takes a lot of processing cores. In the subscription that I have the limit is 60 Cores, and only this HDInsight resource is taking 32 Cores alone. So if you are not using it make sure you delete it.

If you click on the “Cluster Dashboard” it will open the Kafka Cluster dashboard .

You will need to enter the username and password you entered while setting up the cluster.

![](https://cdn-images-1.medium.com/max/800/1*102bhtCBmgxuJBDHE2f63A.png)*Apache Kafka Dashboard*

### Integrating with the Kafka Cluster using C#

Now that the Kafka cluster is up and running, it is time to integrate our C# application with the Kafka Cluster and Publish messages to it and also Subscribe to receive the data streams that we publish.

There are a lot of open source .Net clients available to integrate with Kafka Cluster, but looks like [confluent.io](https://docs.confluent.io/current/) is one of more used ones for this purpose.

For simplicity, I use Console application to demonstrate Publish and Subscribe operations.

[**Step by step: Kafka Pub/Sub with Docker and .Net Core**  
*Last week I attended to a Kafka workshop and this is my attempt to show you a simple Step by step: Kafka Pub/Sub with…*carlos.mendible.com](https://carlos.mendible.com/2017/05/08/step-by-step-kafka-pub-sub-with-docker-and-net-core/ "https://carlos.mendible.com/2017/05/08/step-by-step-kafka-pub-sub-with-docker-and-net-core/")

### Code Time

I just create two new .Net Core Console Applications and add the Confluent.Kafka nuget package to them.

One of the applications will be our Producer application and the other one will be our Consumer to listen to the Events we publish to Kafka cluster.

![](https://cdn-images-1.medium.com/max/800/1*1n_oNwucXS0wFuiJbPRDSw.png)*Adding Confluent Kafka nuget package*

#### Kafka Producer Application Sample

The following snippet shows how a simple Kafka Producer would look like:

Now if you run this Console app, it will produce 10 messages and will publish them to your Kafka Cluster.

#### Kafka Consumer Application Sample

The following snippet shows how a simple Kafka Consumer would look like:

Now if you run this Console app, since it is listening to the same topic we published the messages earlier, it will receive the 10 messages we published to the Kafka Cluster.

You can find the code for the two Console applications above on github from the following link:

[**aramkoukia/kafka-dotnet-sample**  
*Contribute to kafka-dotnet-sample development by creating an account on GitHub.*github.com](https://github.com/aramkoukia/kafka-dotnet-sample "https://github.com/aramkoukia/kafka-dotnet-sample")

Stay tuned for the next parts of this Microservices Implementation Journey!

If you are interested in reading more about Microservices Architecture topic, here are some relevant books:

[![](https://cdn-images-1.medium.com/max/800/1*TmXYeiITDomYKHKB4hLFRA.jpeg)](https://www.amazon.com/gp/product/1491950358/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491950358&linkId=363e9cf9c6a5a697a73b4fe159f37fda)*Building Microservices, Designing fine-grained systems*

[![](https://cdn-images-1.medium.com/max/800/1*M2r6FPQWHiiMN4CwwKcWpg.jpeg)](https://www.amazon.com/gp/product/1491965975/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491965975&linkId=ff04688c2c60121309905c5e0117b145)*Production Ready Microservices, Building Standardized systems across an engineering organization*

[![](https://cdn-images-1.medium.com/max/800/1*sNGTvyO3HCE2KjuaDycQnQ.jpeg)](https://www.amazon.com/gp/product/1491956259/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491956259&linkId=dd181a962e6fe756e0a81861258eb9c2)*Microservices Architecture, Aligning Principles, Practices and Culture*

[![](https://cdn-images-1.medium.com/max/800/1*3ufEsBu_Ajg_VpTLuTKHgg.jpeg)](https://www.amazon.com/gp/product/B0758YB73N/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B0758YB73N&linkId=9b1df16a450d563f1f9b905ae533d9d1)*Building Microservices with Asp.Net Core*

Cheers!
