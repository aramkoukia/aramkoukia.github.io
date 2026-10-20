---
layout: post
title: "Introduction to Azure Event Grid"
date: 2018-08-04
description: "What is Azure Event Grid about?"
image: https://cdn-images-1.medium.com/max/800/1*kEaYN5XatnG4_tcJ1vR2Jw.png
medium_url: https://medium.com/@aramkoukia/introduction-to-azure-event-grid-87b058408c70
---

### Introduction to Azure Event Grid

![](https://cdn-images-1.medium.com/max/800/1*kEaYN5XatnG4_tcJ1vR2Jw.png)*Azure Event Grid (Image from MSDN Blog)*

#### What is Azure Event Grid about?

Azure Event Grid is a managed event routing platform which enables you to react in real-time to changes that are happening in your applications hosted in Azure or any Azure resources that you own.

Today to get notified of a stage change in a resource, such as a new record in a database, or when someone creates a Virtual Machine, you typically think of scheduled or continuous polling. That means that we are constantly consuming computing power (CPU and Network resources) to monitor all these changes.

But now with Azure Event Grids you can forget about all that. You can have your applications to send events when a change in state happens just like push notifications! Those are only engaged once actionable events are sent.

Any component which is interested in those events can subscribe and get notified without polling, reducing the previous required computing resources.

Event Grid, handles built-in Azure Events from Azure Services as well as Custom Events from your applications and publishes them in real-time. It can dynamically scale and handle millions of events every second and Azure offers 99.99 SLA for production work loads.

As events are received, Event Grid facilitates the triggering of programmatic actions via Event Handlers such as Azure Automation, Event Hubs, Azure Functions, Azure Logic Apps or custom web hooks.

#### Integrate with any Service or Application

Because everything is based on HTTP, Event Grid can virtually integrate with any service or application.

Where this becomes powerful, is in simplifying ops and on security automation through easier policy enforcement, expanding server-less compute scenarios with no eventing sources and enabling better communication and integration between your event-based services and applications.

#### Pricing Model

Azure Event Grid has a Pay Per Event Pricing model, so you only pay for what you consume. At the moment the first 100,000 operations per months is free, and after that you pay 60 cents per million operations after that.

#### Getting started on Azure Event Grid

If you want to get started, there are some Management And Runtime SDKs on [.NET](https://www.nuget.org/packages/Microsoft.Azure.Management.EventGrid), [Go](https://github.com/Azure/azure-sdk-for-go), [Java](https://search.maven.org/#search%7Cga%7C1%7Cazure-mgmt-eventgrid), [Node](https://www.npmjs.com/package/azure-arm-eventgrid), [Python](https://pypi.python.org/pypi/azure-mgmt-eventgrid) and [Ruby](https://rubygems.org/gems/azure_mgmt_event_grid) to publish and subscribe to events from your applications.

And if you are looking for some sample scripts and tutorials here are some to help you get started:

[**Route Azure Blob storage events to a custom web endpoint**  
*Use Azure Event Grid to subscribe to Blob storage events.*docs.microsoft.com](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-event-quickstart?toc=%2fazure%2fevent-grid%2ftoc.json "https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-event-quickstart?toc=%2fazure%2fevent-grid%2ftoc.json")

[**Monitor virtual machine changes - Azure Event Grid & Logic Apps**  
*Check for config changes in virtual machines (VMs) by using Azure Event Grid and Logic Apps*docs.microsoft.com](https://docs.microsoft.com/en-us/azure/event-grid/monitor-virtual-machine-changes-event-grid-logic-app "https://docs.microsoft.com/en-us/azure/event-grid/monitor-virtual-machine-changes-event-grid-logic-app")

[**Use Azure Event Grid to automate resizing uploaded images**  
*Azure Event Grid can trigger on blob uploads in Azure Storage. You can use this to send image files uploaded to Azure…*docs.microsoft.com](https://docs.microsoft.com/en-us/azure/event-grid/resize-images-on-storage-blob-upload-event?tabs=net "https://docs.microsoft.com/en-us/azure/event-grid/resize-images-on-storage-blob-upload-event?tabs=net")

[**Azure Event Grid and Event Hubs integration**  
*Describes how to use Azure Event Grid and Event Hubs to migrate data to a SQL Data Warehouse*docs.microsoft.com](https://docs.microsoft.com/en-us/azure/event-grid/event-grid-event-hubs-integration "https://docs.microsoft.com/en-us/azure/event-grid/event-grid-event-hubs-integration")

Cheers!
