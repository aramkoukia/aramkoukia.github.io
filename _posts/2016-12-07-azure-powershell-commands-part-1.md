---
layout: post
title: "#Azure #Powershell commands (Part 1)"
date: 2016-12-07
description: "Login to Azure"
---

### #Azure #Powershell commands (Part 1)

### Login to Azure

**Classic Mode:**

First you start with bellow command to authenticate using Azure Active Directory which will be good for 12 hours:

`Add-AzureAccount`

You can also use below cmdlet instead of the one above:

`Get-AzurePublishSettingsFile`

This will open a browser window and you you can download a publish settings file. The downloaded file contains a certificate that allows PowerShell to authenticate. Then you should import that publish settings file using the following command:

`Import-AzurePublishSettingsFile`

***NOTE:*** *Remember that the publish settings file contains a certificate with effectively admin privileges in your subscription. Keep it secure or delete it after using it.*

**ARM (Resource manager) mode:**

Using the ARM (Azure Resource Manager) model, you can only use Azure Active Directory authentication that will work for 12 hour after you authenticate and after 12 hours you need to enter credentials again to renew the token. Currently you have two options that you can use:

`Login-AzureRmAccount  
Add-AzureRmAccount`

I will continue documenting other Powershell commands that you can use to manage your Azure Resources, but for now you are logged in successfully to your Azure account.
