---
layout: post
title: "Tips on Azure Resource Groups"
date: 2017-04-30
description: "Azure Resource Groups are a logical containers to keep related resources for an application or group of applications together."
image: https://cdn-images-1.medium.com/max/800/0*ufJt-1L32YpHevwC.png
---

### Tips on Azure Resource Groups

Azure Resource Groups are a logical containers to keep related resources for an application or group of applications together.

You can decide how to assign your resources to resource groups based on what is the most appropriate for you and your organization and this decision is very pragmatic and is up to your team.

![](https://cdn-images-1.medium.com/max/800/0*ufJt-1L32YpHevwC.png)

Here are some tips that you should consider when making the decision of the Resource Groups that you need and which Resources you want to put in a which Resource Group:

- You should have in mind that all the resources in a group should have the same life-cycle.
- An Azure Resource can only be assigned to one Azure Resource Group.
- A resource can be added to or removed from an Azure Resource Group. Something to keep in mind is that each Resource should belong to an Azure Resource Group, so if you remove it from one Resource Group, you should add it to another one.
- Almost all types of resource can be moved to different resource groups any time you want.
- Regions are not going to restrict you. i.e.: resources in a resource group can be in different Azure regions.
- One of the best things you get out of Azure resource groups is: you should use resource groups to control access to your resources.

After you get more familiar with Azure Resource groups you will have a more complete list of how you create and organize your Resource Groups that makes the most sense for your needs.
