---
layout: post
title: "What is Azure Resource Manager"
date: 2016-10-04
description: "The Azure Resource Manager is the new way of deploying your resources in Azure."
image: /assets/img/2016-10-04-what-is-azure-resource-manager/1.png
---

### What is Azure Resource Manager

The Azure Resource Manager is the new way of deploying your resources in Azure.

Previously we were using Azure Service Management (ASM) for deployments to Azure. The ASM deployment is now known as “Classic” between Azure people. Then around 2015 Microsoft release Resource Manager model as the next generation of deployment models in Azure and this new model is recommended for all kind of workloads.

![](/assets/img/2016-10-04-what-is-azure-resource-manager/1.png)*Azure Resource Group*

Some people refer to this new deployment strategy are not just used to deploy your services but you can also control your resources with them as well.

The of the Azure Resource Manager (ARM) idea is when we deploy some resources to Azure, some of them are somehow related to each other. Imagine a web application, which will have a Web site, some web services and some databases, now ideally we want to have all these resources in one resource group so we can deploy and control and monitor them together. This way you can deploy, update or remove all the pieces in one resource group in one shot.

In the example, above, the resource group would contain the following:

1. A website application that hosts the front-end application

2. Web services applications that host the back-end services

3. Azure SQL Database instance that contains the data for the application.

With ARM, you can create templates to exactly define all the Resource Manager resources in a deployment. Then you publish this template into a Resource Group as a single operation to make sure they are deployed properly.

Azure Resource Manager also has features for Security, Auditing, and tagging features that you can use after you deployed your components which are basically the control and monitoring features of the Azure Resource Manager.

For an overview and more details on Azure Resource Manager visit the Azure blog:

<https://azure.microsoft.com/en-us/documentation/articles/resource-group-overview/>
