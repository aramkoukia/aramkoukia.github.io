---
layout: post
title: "Azure Powershell commands — Part 2"
date: 2016-12-09
description: "You can have multiple subscriptions under one account in Azure, and when you use the Azure portal you have the option to select one or many…"
image: /assets/img/2016-12-09-azure-powershell-commands-part-2/1.png
tags: ["Azure"]
---

### Azure Powershell commands — Part 2

![](/assets/img/2016-12-09-azure-powershell-commands-part-2/1.png)

You can have multiple subscriptions under one account in Azure, and when you use the Azure portal you have the option to select one or many subscriptions when dealing with Azure resources.

You can also select a specific subscription using the Azure Powershell commands, and after that all the commands that you use in Powershell will be executed against that selected Subscription.

**In Classic mode:**

```
Set-AzureSubscriptionSelect-AzureSubscription
```

**In Resource Manager (ARM) mode:**

```
Select-AzureRmSubscription
```

Both commands above, will ask you to specify the Subscription (like Subscription Id or something), but if you are not sure what are all the subscriptions that you have access to you can use the following command to get a list of all of them:

```
Get-AzureSubscription
```

**Found this post useful? Kindly tap the ❤ button below! :)**
