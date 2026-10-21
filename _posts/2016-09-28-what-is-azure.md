---
layout: post
title: "What is Azure"
date: 2016-09-28
description: "I have been talking about Azure in detail in my blog in the past and I got this feedback from some people that they need to know a little…"
image: /assets/img/2016-09-28-what-is-azure/1.png
tags: ["Azure"]
---

### What is Azure

I have been talking about Azure in detail in my blog in the past and I got this feedback from some people that they need to know a little bit of high level information about Azure and its services to they can decide what kind of Microsoft’s cloud computing platform is going to suit them.

### What is cloud computing?

Cloud computing is the alternative to classic on-premises or in-house data centers that we used to have. So in the cloud computing world a different company other than your IT department will be responsible for the hardware and maintenance, backup and more services that you can use. You are basically renting the hardware and software that you need (when you need them) use them and release them when you don’t want them anymore and you only pay for what you have used. Now this suggests that you don’t need a capital expense for hardware purchase in your IT department also just because of the expense you might just don’t buy a piece of hardware that you really needed nut you didn’t buy it because you only needed it for a short period of time.

All cloud computing providers will offer you a website that you can login and “lease” the hardware or software you need. Of course you are limited to the type of hardware that they offer and you don’t get exactly what you want but you can definitely find something close enough that suits you.

Back to Azure, your IT guy can create Virtual Machines, SQL Server Databases, Network configurations through the Azure portal in minutes and if you compare that to the old way of doing things, that would have taken days if not months to provision.

### Comparison of on-premises versus Azure

![](/assets/img/2016-09-28-what-is-azure/1.png)

There are probably more differences between On-Premises and Azure that we can list but the above table will give you a general idea about the main differences.

### Cloud offering

Cloud computing usually is known in three categories: SaaS, PaaS, and IaaS. Although looks like the distinction between these are getting harder and harder because a lot of services are being like a mixture of 2 or 3 categories mentioned above.

![](/assets/img/2016-09-28-what-is-azure/2.png)

### SaaS or Software as a service

SaaS the clearest and the most familiar cloud service and it is basically a software that is hosted in the cloud service provided data centers and consumers just use that instance. So all the users use the same version and Azure will take care of everything for us (from hardware, to deployment, backups, security etc) and we are just simple users of the software.

SaaS software typically is licensed through a monthly or annual subscription. Microsoft Office 365 is a famous SaaS software that almost everyone has heard about it which is offered as SaaS which you just pay a monthly of annual fee and good to go.

### PaaS or Platform as a service

In PaaS, you bring your software and host it in the Azure’s hosting environment. So in this case Azure provides us with the Hardware, and the Hosting environment (Like IIS or other web servers). So in this case we will be responsible for patches and security of our software, deployments, backups etc. But you can still use Azure feature to scale up or scale out easily and host the same instance of the software in multiple data centers.

### IaaS or Infrastructure as a service

An IaaS cloud provider runs and administers server farms running virtualization software, enabling you to create virtual machines that run on the provider’s hardware infrastructure. Azure provides the ability to set up virtual networks, storage and load balancers and to use many other services that run on its infrastructure. We don’t have control over the hardware or virtualization software, but we do have control over almost everything else. In fact, unlike PaaS, you are completely responsible for it. Azure Virtual Machines, the Azure IaaS offering, is a popular choice when migrating services to Azure because it enables us to just cut our on-premises data center and migrate them to Azure to start with cloud computing.
