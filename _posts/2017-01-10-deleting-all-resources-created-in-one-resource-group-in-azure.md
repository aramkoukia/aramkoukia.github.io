---
layout: post
title: "Deleting all resources, created in one Resource Group in #Azure"
date: 2017-01-10
description: "When you deploy a big system with a hand full or even more of resources in Azure, and put them all in one resource group, you have a lot of…"
image: https://cdn-images-1.medium.com/max/800/1*A5TE9cItH27lh6WKl1Y4Xw.png
medium_url: https://medium.com/@aramkoukia/deleting-all-resources-created-in-one-resource-group-in-azure-29ddfe11e2d2
---

### Deleting all resources, created in one Resource Group in #Azure

![](https://cdn-images-1.medium.com/max/800/1*A5TE9cItH27lh6WKl1Y4Xw.png)

When you deploy a big system with a hand full or even more of resources in Azure, and put them all in one resource group, you have a lot of power to manage and control all those resources as a group.

[Recently](https://koukia.ca/create-a-private-ethereum-consorium-blockchain-in-azure-3667185276b5#.ajr30h9sl), I deployed an Ethereum Consortium Blockchain network in my Azure subscription, but I don’t need it for now, so I wanted to clean my subscription a bit as it deployed 21 various resources in my subscription.

Since this template creates all the resources in 1 Resource Group I can delete them all together by simply just deleting the Resource Group.

### Delete Resource Group from Azure Portal

First option is to open the Azure portal, select the Resource Groups menu, select the Resource Group you want to delete and select the “Delete” menu:

![](https://cdn-images-1.medium.com/max/1200/1*oxxqh06ZlNgg0cF4T78Q3g.png)

As you see in the picture above, there are 21 items in this resource group and it would have been a nightmare to delete them one by one, so using Resource Groups comes to rescue here.

### Delete Resource Group using Azure Powershell

The other option is to use Azure Powershell.

You can simply call the following command to delete the Resource Group and all the resources in it:

```
Remove-AzureRmResourceGroup -Name EthereumAram
```

If you want to delete a specific resource from a Resource Group you can use the following Powershell command:

```
Remove-AzureRmResource -ResourceName mystoragename -ResourceType Microsoft.Storage/storageAccounts -ResourceGroupName EthereumAram
```

Using Resource Groups have [other benefits](https://koukia.ca/what-is-azure-resource-manager-d08d8f3e801d#.cin2cmyyg) too, but I would try to utilize them just for this purpose.
