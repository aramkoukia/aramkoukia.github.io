---
layout: post
title: "Proactive Auto Heal, on Azure App Services"
date: 2017-08-20
description: "Azure App Services has had this Auto Heal feature for while when you could set it to make a decision when certain things happen like: When…"
image: https://cdn-images-1.medium.com/max/800/1*WXj7xR24CTCOiYBNcVSpjg.png
---

### Proactive Auto Heal, on Azure App Services

![](https://cdn-images-1.medium.com/max/800/1*WXj7xR24CTCOiYBNcVSpjg.png)

Azure App Services has had this [Auto Heal](https://blogs.msdn.microsoft.com/waws/2015/11/04/auto-heal-your-azure-web-app/) feature for while when you could set it to make a decision when certain things happen like: When request count surpasses a certain limit or when requests are running slower usual or other situations. But to do that you needed to setup some rules and then when those rules were met, you could restart your application or things like that.

And now there is another option available which is basically and extension of the Auto Heal.

### Proactive Auto Heal

Proactive Auto Heal will only kick in when your sites are totally busted!

In other words when they are in a situation where the only way to recover is to restart the application, this service will do it for you. For example, If you have multiple instances of a web site and one of the instances has a memory leak and is consuming most of the memory of that instance, or is consuming more than 90% of that instance’s CPU, then Proactive Auto Heal will kick in and restart that instance.

### How does Proactive Auto Heal know it is time to act?

Proactive Auto Heal has 2 rules:

#### 1. Percent Request

All the requests are being monitors and if 80% or more of total requests are taking more than 200 seconds, then the instance will undergo a restart.

#### 2. Percent Memory

Your Web App’s process’s private bytes are being monitored so when an instance’s memory consumption exceeds *90%* of that instance memory limit it will start the restart process.

Also if there are too many restarts, this rule will be disabled for 3 hours to avoid too many restarts.

Now, the good news is, **this feature is turned on by default** for all the code you have hosted in Azure App Services.

So if you don’t want it (for any reason) you can navigate to Azure portal, select your Application and go to the App Settings section and add this key there:

**WEBSITE\_PROACTIVE\_AUTOHEAL\_ENABLED** and set the value to be “false”.

Then if you changed your mind you can set this value to “true”

Cheers!
