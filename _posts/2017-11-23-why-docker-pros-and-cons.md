---
layout: post
title: "Why Docker? Pros and Cons"
date: 2017-11-23
description: "What are Containers?"
image: https://cdn-images-1.medium.com/max/1200/1*9eqkIxHnho9ny2Tym5-I-w.jpeg
---

### Why Docker? Pros and Cons

![](https://cdn-images-1.medium.com/max/1200/1*9eqkIxHnho9ny2Tym5-I-w.jpeg)

### What are Containers?

Well, I guess the best I can do is to quote from Docker team:

> A container image is a lightweight, stand-alone, executable package of a piece of software that includes everything needed to run it: code, runtime, system tools, system libraries, settings.

So I guess developers got pissed off by the whole “Linux” or “Windows” thing, and they where like: “Let’s build something that can run both Windows and Linux applications, regardless of the operating system or environment”, then containers were invented!

The idea is Containers will isolate “our code” from what is “not our code”, to make sure the “works on my machine” situation doesn’t happen.

![](https://cdn-images-1.medium.com/max/800/1*Aa-BckHlka-9aPF8LLFQtg.jpeg)

### From Virtual Machines to Containers

So before Containers showed up, we used to use VMs to host our application, and I guess people liked it, because we were able to get a big server and slice it up to several VMs and have multiple computers and simulate a network. now that Containers showed up, it seems like VMs aren’t a good idea anymore, because it seems like Containers give us a better level of abstraction than VMs.

Though some people might argue that, we might not even need docker, if we choose a right Cloud platform, and use PaaS (Platform as a Service) offerings which will give us a higher level of abstraction, but again other might argue that, that way you are kind of tight to that Cloud Provider, which again might not necessarily be a bad thing, considering what they offer these days!

Also, even some of the Cloud providers does not natively support Linux or Windows, so now with Containers, you can put your code in some container and then move your container into your cloud provider if you like.

#### Remind me what Virtual Machines are!

Virtual machines (VMs) are an abstraction of physical hardware, that would slice your one giant physical server into multiple ones. The “[hypervisor](https://en.wikipedia.org/wiki/Hypervisor)” or “VMM (Virtual Machine Monitor)” provides the capability to run multiple Virtual Machines on one set of hardwar and each one of these VMs with have an OS (you need to have licenses, update and patch them and everything IT related you do with all of your regular computers).

#### Tell me again about Containers!

Containers are an abstraction at the app layer that packages code and dependencies together. Multiple containers can run on the same machine and share the OS kernel with other containers, each running as isolated processes in user space. Since Containers does not have a full blown Operating System they take up less space compared to VMs.

The following image from Docker website explains the differences Between Containers and VMs:

![](https://cdn-images-1.medium.com/max/1200/1*xNGfejkg9pQ16orB7VAIjA.png)

### **Deeper** dive **into Virtualization**

As mentioned before Virtualization is handled by Hypervisor, and it basically manages the CPU’s “root mode” and by some sort of interception, manages to create an illusion for the VM’s Operation System as if it has its own hardware. I f you are interested to know who did this first to send them a “Thank You” note, it was “[VMWare](http://web.archive.org/web/20160324005530/https://www.vmware.com/files/pdf/VMware_paravirtualization.pdf)”.

So ultimately, the hypervisor, facilitates to run multiple seperate operation systems on the same hardware. All the VM operating system (known as Guest OS) go through the boot process to load the kernel and all the other OS modules, just like regular computers, hence the slowness! And if you are curious about the isolation between the guests and hosts, I should say, you can have pretty strict security between them.

### Deeper dive into Containers

A bit more than 10 years ago, some folks from Google came up with [*namespaces*](https://differential.com/insights/the-story-behind-meteors-next-big-move/)concept*.* Yeah, exactly as developers are familiar with, the idea is, we want to put hardware resources into namespaces, and only give permission to use resources to other resources or software, only if they belong to a specific namespace. So you basically can tell processes, what is their namespace, and what hardware namespaces they can access.

So this basically creates a level of isolation, where each process has only access to the resources that are in their own namespace.

This is how Docker works! Each container runs in its own namespace and all containers use the same kernel to manage the namespaces.

Now because kernel is the control plane here and knows the namespace that was assigned to the process, it makes sure that process can only access resources in its own namespace.

As you can see the isolation level in Docker is not as strong as VMs as they all share the same kernel, also because of the same reason they are much lighter than VMs.

### Docker and Other alternative Containers

As you have seen above, I might use “Container” and “Docker” interchangeably, because I guess Docker has become the industry de facto standard, and lot of people including myself use these words interchangeably.

But if you are interested on other alternatives here are some that are out there:

Although Docker is the most popular container technology, but there many other container solutions out there:

- [BSD Jails](https://www.freebsd.org/doc/handbook/jails.html)
- [LXD](https://linuxcontainers.org/lxd/introduction/)
- [LXC](https://linuxcontainers.org/lxc/introduction/)
- [Solaris Zones](http://www.oracle.com/technetwork/server-storage/solaris/containers-169727.html)
- [RKT](https://coreos.com/rkt/)

Here what google trends shows comparing these:

![](https://cdn-images-1.medium.com/max/2560/1*08dIa0o7ptCWiDRvX49pvA.png)

### Docker, the good parts

Here are some advantages when you are looking into VMs or Bare-bone servers

- **Containers are small compared to VMs**

Though they are bigger than Functions, if you compare them with AWS Lambda, or Azure Functions, or even Azure App services! They tend to start somewhere from tens of megabytes up, where VMs start from Gigabytes. So your current server can host way more containers compared to VMs.

- **Containers uses less resources**

Since you don’t have a full OS and they all share the same kernel, they are pretty light.

- **Fast boot.**

Takes seconds to start a container, so if things go south and you need to restart or deploy new versions, you new instance is up in seconds.

- **Eliminating the “Works on My Machine” situation**

Bug bounces around issues where you test in one environment, and then code doesn’t work in other environment because of config issues will not happen as often because local and QA environment would be identical.

- **They work well in DevOps and CI/CD**

Container-based virtualization are a great option for Microservices, DevOps, and continuous deployment since it is easy to manage them (if you have the right tools!)

### Docker, the dark side

Though there are very good benefits of using Containers there are things to watch for!

- **Security**

Since there is no full operating system people tend to overlook the security aspect of containers, but if you look up online, you will see that hackers are targeting systems that are hosted in containers and not secured properly.

- **Isolation**

Since the containers use the same kernel, they are not 100 isolated, so you should be aware of the risks if you are using multiple containers in one server, and make sure you know what you are doing and which containers are running on the same kernel along with your stuff!

- **Networking**

Networking can be tricky in containers world when you want to limit the access within containers and also have proper network communications where required.

### Summary

I don’t think Containers are going to make VMs disappear anytime soon, as I also have seen companies like Netflix use both Containers and VMs in their architecture where appropriate:

[**Scheduling a Fuller House: Container Mgmt @Netflix**  
*Andrew Spyker and Sharma Podila talk about the motivations and the technology powering container deployment on top of…*www.infoq.com](https://www.infoq.com/presentations/container-management-netflix?utm_source=medium&utm_medium=flow.ciweekly&utm_campaign=flow.ci%20says%20hi "https://www.infoq.com/presentations/container-management-netflix?utm_source=medium&utm_medium=flow.ciweekly&utm_campaign=flow.ci%20says%20hi")

Cheers!
