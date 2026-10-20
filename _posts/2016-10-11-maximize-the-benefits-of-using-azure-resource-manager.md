---
layout: post
title: "Maximize the benefits of using Azure Resource Manager"
date: 2016-10-11
description: "Microsoft Azure team has a hand full of guidelines to help you get the most out of the Azure Resource Manager model when working with your…"
image: /assets/img/2016-10-11-maximize-the-benefits-of-using-azure-resource-manager/1.png
medium_url: https://medium.com/@aramkoukia/maximize-the-benefits-of-using-azure-resource-manager-c6f2a1eb7ee
---

### Maximize the benefits of using Azure Resource Manager

Microsoft Azure team has a hand full of guidelines to help you get the most out of the Azure Resource Manager model when working with your applications and components.

- Use templates rather than using scripting like PowerShell or the Azure Command-Line Interface (CLI). Using a template allows resources to be deployed in parallel, making it much faster than using a script executed sequentially.
- Automate as much as possible by leveraging templates. You can include configurations for various extensions like PowerShell DSC and Web Deploy. This way, you don’t need any manual steps to create and configure the resources.
- Use PowerShell or the Azure CLI to manage the resources, such as to start or stop a virtual machine or application.
- Put resources with the same life cycle in the same resource group. In our example, above, what if the database is used by multiple applications? If that’s true, or if the database is going to live on even after the application is retired or removed, you don’t want to re-create the database every time you redeploy the application and its components. In that case, put the database in its own resource group.

You can find more Best Practices for creating Azure Resource Manager templates in this page:

[**Best practices for creating Azure Resource Manager templates**  
*The following guidelines will help you create Resource Manager templates that are reliable and easy-to-use. These…*azure.microsoft.com](https://azure.microsoft.com/en-us/documentation/articles/resource-manager-template-best-practices/ "https://azure.microsoft.com/en-us/documentation/articles/resource-manager-template-best-practices/")

![](/assets/img/2016-10-11-maximize-the-benefits-of-using-azure-resource-manager/1.png)

Hope these tips will help you when working with Azure Resource Manager (ARM).
