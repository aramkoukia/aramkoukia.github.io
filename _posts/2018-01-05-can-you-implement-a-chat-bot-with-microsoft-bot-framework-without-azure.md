---
layout: post
title: "Can you implement a Chat Bot with Microsoft Bot Framework without Azure?"
date: 2018-01-05
description: "Microsoft Bot Framework is an amazing framework that people are using it more and more to build Bots these days, because it is so simple to…"
image: https://cdn-images-1.medium.com/max/800/1*QoCscxdXl2mkWqL7mGfALA.png
medium_url: https://medium.com/@aramkoukia/can-you-implement-a-chat-bot-with-microsoft-bot-framework-without-azure-1446ce8333bf
---

### Can you implement a Chat Bot with Microsoft Bot Framework without Azure?

![](https://cdn-images-1.medium.com/max/800/1*QoCscxdXl2mkWqL7mGfALA.png)

Microsoft Bot Framework is an amazing framework that people are using it more and more to build Bots these days, because it is so simple to put together a Bot very quick.

I have also published a post here a while ago, that you can go through and learn a bit more about this Microsoft Bot Framework if you are not familiar with it, but today, I am writing this to answer a different question.

[**Creating Bots in the Microsoft Bot Framework using Node.js**  
*I came across this great Microsoft Bot Introduction Course a while ago and thought to share it with you.*koukia.ca](https://koukia.ca/creating-bots-in-the-microsoft-bot-framework-using-node-js-69d27d55bb92 "https://koukia.ca/creating-bots-in-the-microsoft-bot-framework-using-node-js-69d27d55bb92")

### The story

So, when you first start going through the tutorials, somehow most people get the impression that they need to use Azure to host their Chat Bot API.

Though, using Azure to host your Chat Bot service will be very convenient and a good choice, but you don’t have to use Azure!

If you need to know how, keep reading…

#### What does a basic Chat Bot Application Architecture look like?

If you look at the following picture, you will see a basic Chat Bot Application architecture, built using Microsoft Bot Framework:

![](https://cdn-images-1.medium.com/max/800/1*X8OMPKY2vf7VREX6Nn6wwA.png)*A basic Microsoft Bot Framework Architecture*

As you can see, the first thing that happens, when a user interacts with your Bot, through one of the Channels (Skype, Slack, etc), those channels make some API call to your Chat Bot.

Now, as you can imagine, all those connectors are on public internet, and for them to be able to communicate to your Chat Bot API, your API also needs to be publicly accessible on the Internet.

Also, because they want to make sure the message or communication is secure, they require your Bot API to have SSL Certificate.

Now with that, you see that hosting the Bot API in Azure makes a lot of sense, because first of all, it is publicly available, and also all Azure websites come with SSL Certificate, so you don’t need to worry about that part.

#### What About LUIS or Other Cognitive Services that are used?

In terms of LUIS (Most chat Bots would probably use such services to language understanding), there is no problem, as long as your Bot API is connected to the internet, so we are good there, because there is no call back from LUIS to your API, and you just call LUIS APIs and get the data back, and LUIS will not push anything to your Bot API.

### Certificate Requirement For your Bot API

If you decided for any reason, that you don’t want to host your Bot on Azure, then first of all as mentioned earlier you need to make sure it is accessible through internet, and second is the Certificate.

The following is the Certificate requirement, if you want to host your API outside of Azure:

> The Bot Framework requires that the x.509v3 certificate exposed by your endpoint be current and valid. Most of the checks for “current and valid” are standard checks for server certs: the CN must match the hostname, it must not be expired, it must not be listed in a CRL, it must have the correct set of EKUs, etc.

> Most importantly, your cert must chain to a root certificate authority trusted by Microsoft. The latest list of these CAs is available [here](http://social.technet.microsoft.com/wiki/contents/articles/31634.microsoft-trusted-root-certificate-program-participants-v-2016-april.aspx).

I hope this helps you in making a decision to pick a Bot Framework.

Cheers!
