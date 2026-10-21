---
layout: post
title: "#Microsoft Windows #Azure #WebJobs and How to keep them awake"
date: 2016-12-09
description: "In case you have come across Microsoft Azure WebJobs (if not you can take a look at what it is here) you know that they are basically…"
image: /assets/img/2016-12-09-microsoft-windows-azure-webjobs-and-how-to-keep-them-awake/1.png
tags: ["Azure"]
---

### #Microsoft Windows #Azure #WebJobs and How to keep them awake

In case you have come across Microsoft Azure WebJobs (if not you can take a look at what it is [here](http://azure.microsoft.com/en-us/documentation/articles/web-sites-create-web-jobs/)) you know that they are basically background processes that you want to run them on a Azure hosted website, and you can make them to run continuously, on demand or based on a specific schedule.

In our latest project we had a WebJob in our Azure website that was supposed to listen to some messages on [Azure Service Bus (ASB)](http://azure.microsoft.com/en-us/services/service-bus/), so based on that we were expecting to run a process continuously so that it can listen to bus messages and process them as soon as they arrive. so with this background we chose “Run continuously” as WebJobs’s schedule at deployment time.

After some time, test team reported that the WebJob does not work! and as usual we checked the Azure portal in that environment and checked the status of the job and noticed that it is running!

But the observation was, as soon as we open the WebJob tab in the azure portal we could see that it says “Web Job Starting” and after a few seconds it says “Web job Running”!

So basically, after some time the WebJob, which is set to run continuously, goes to sleep regardless of the Schedule settings.

Here are how Azure portal looks like, when you first select your Azure Website:

![](/assets/img/2016-12-09-microsoft-windows-azure-webjobs-and-how-to-keep-them-awake/1.png)

Now when you click on the WebJob link, you will see this:

![](/assets/img/2016-12-09-microsoft-windows-azure-webjobs-and-how-to-keep-them-awake/2.png)

And after a few seconds, you will see it starts running:

![](/assets/img/2016-12-09-microsoft-windows-azure-webjobs-and-how-to-keep-them-awake/3.png)

So what’s the trick? there is a setting in the Configure tab called “ALWAYS ON“ which it has a very bold message on top of it that says “Should be turned on if you have a job that runs continuously”.

Here is how this setting looks like:

![](/assets/img/2016-12-09-microsoft-windows-azure-webjobs-and-how-to-keep-them-awake/4.png)

When you set your WebJob, make sure you set this to ON from your deployment script or the Azure portals.
