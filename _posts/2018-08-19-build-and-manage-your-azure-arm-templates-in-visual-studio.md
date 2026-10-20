---
layout: post
title: "Build and Manage your Azure ARM templates in Visual Studio"
date: 2018-08-19
description: "One of the buzz words in the DevOps words is this “Infrastructure as Code” thing, and the Azure ARM Templates are a good example of how it…"
image: https://cdn-images-1.medium.com/max/2560/1*cvmhSKjr96MPgjHQLAuLNA.png
medium_url: https://medium.com/@aramkoukia/build-and-deploy-to-azure-using-azure-arm-templates-from-visual-studio-987b21d215ed
---

### Build and Manage your Azure ARM templates in Visual Studio

![](https://cdn-images-1.medium.com/max/2560/1*cvmhSKjr96MPgjHQLAuLNA.png)*Image from: <https://azurecitadel.github.io/workshops/arm/theoryTemplates/>*

One of the buzz words in the DevOps words is this “Infrastructure as Code” thing, and the Azure ARM Templates are a good example of how it would look like.

The basic idea is you use a template (in this case it would be a *.json* file) for deployment and that template will be used to deploy your component to different environments such as testing, staging, and production.

Not if you keep these template in Source Control, boom, you have your *Infrastructure as Code!*

#### Shoe me how to create an Azure ARM templates

There are several ways, you can do this. You can [export these templates from Azure portal](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-quickstart-create-templates-use-the-portal) if you have already have them deployed to Azure, or you can start from scratch using the [Azure Resource Manager documentation](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-authoring-templates), or use the [hundreds of samples available on github](https://github.com/Azure/azure-quickstart-templates) and take it from there.

However today I would like to show you how to make these ARM templates from Visual Studio and a project template that is provided by the Azure development tools for Visual Studio.

For this demo, I will use the Visual Studio 2017 Community edition, so if you don’t have it installed already you can download and install it from [here](https://visualstudio.microsoft.com/downloads/).

While installing the Visual Studio, make sure you check the Azure development section like the following picture.

![](https://cdn-images-1.medium.com/max/1200/1*2IrQKJp2IgBIBjVoHtHtrA.png)

If you already have Visual Studio and you did not select this section, you can do it by going to windows “Add/Remove programs” and *modify* your Visual Studio instance and add this in.

Now open Visual Studio, and select File > New Project and under the C# branch, select “Cloud”, and “Azure Resource Group” project template.

![](https://cdn-images-1.medium.com/max/800/1*UVE8-QoeU02VbJLj6dhhlA.png)*Azure Resource Group Project Template*

> This template creates an Azure Resource Group deployment project. The deployment project will contain artifacts needed to provision Azure resources using Azure Resource Manager that will create an environment for your application.

In the next screen, you can select the Resource template that you like. You can start blank or select from numerous templates available from Github or just this project template.

![](https://cdn-images-1.medium.com/max/800/1*90R_QjFW6rF3GulJhYhFAQ.png)

To see what I get from this project, I select the “Web app” to get started.

What this does is, it creates 3 files

![](https://cdn-images-1.medium.com/max/800/1*ctzn3Z7t5OjACarV_oPRDg.png)

1. A powershell script that I can use/run using Azure CLI or VSTS to deploy the Resource Group based on the template
2. An ARM Template that can deploy an Azure Web app for me
3. An ARM Template Parameters that I can use to define any variables that are used in the main website ARM template.

#### How can I use this to deploy my resources?

It is pretty simple from here. All we need to do is:

- Open the *Website.parametes.json* file,
- Update all the values that are missing and save it.
- Right click on the project and click Deploy.
- Select your subscription and done!

![](https://cdn-images-1.medium.com/max/800/1*Wdzh4CDa0DmFc-jgULkeLg.png)*Deploying to Azure using Azure Resource Group project*

![](https://cdn-images-1.medium.com/max/800/1*ccBCw4atg4G-bsqIo9oQ3Q.png)*Selecting your Azure Subscription*

Even if you didn’t want to update the parameters.json file, you make any updates in the above “Deploy to Resource Group” window by clicking the “Edit parameters” button.

Hope this helps you to manage and organize your Azure ARM templates better.

Cheers!
