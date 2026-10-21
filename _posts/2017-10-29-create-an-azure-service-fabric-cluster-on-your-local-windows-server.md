---
layout: post
title: "Create an Azure Service Fabric Cluster on your local Windows Server"
date: 2017-10-29
description: "When you are doing R&D around Container Orchestrators and your technology choices for managing your Microserices ecosystem, Azure Service…"
image: https://cdn-images-1.medium.com/max/2560/1*Rbw6iypOV4AoGThYLarFjQ.png
tags: ["Azure", "Containers"]
---

### Create an Azure Service Fabric Cluster on your local Windows Server

![](https://cdn-images-1.medium.com/max/2560/1*Rbw6iypOV4AoGThYLarFjQ.png)

When you are doing R&D around Container Orchestrators and your technology choices for managing your Microserices ecosystem, Azure Service Fabric is one of the options that stands out.

Azure Service Fabric has proven to do the job.

> Service Fabric is the technology that enables Microsoft Cloud!

In case you are curious to see how scalable service Fabric is, watch this video and see Service Fabric Orchestrates ***1 million containers***:

### Do I have to use Azure to use Service Fabric?

Not really! **but,** there are certain features that you will not have if you have your Service Fabric Cluster on your local Servers. And generally those are the features that are provided by some other Azure components, like Auto-Scaling and some other stuff.

This means you can install and run a Service Fabric Cluster in your own on-prem servers that contains a set of Windows Server computers connected in a network.

**Interesting thing is, since it just requires a bunch of windows servers that are connected, you can basically use any OTHER cloud provider like AWS and then install Service Fabric there!**

So in this post, I am going to demonstrate how you can install a Service Fabric Cluster on your local Windows server.

### Installing a local Service Fabric

To build the Service Fabric Cluster, we can use its package from the following link.

Note: you can install this package in any Windows Server 2012 R2 or newer.

<http://go.microsoft.com/fwlink/?LinkId=730690>

When you download this zip file and extract it, you will see some Powershell files as well as some sample Service Fabric configuration files that we can use as starting point:

![](https://cdn-images-1.medium.com/max/800/1*bO1I6i43AOzIjOMAd5PuWQ.png)

As you can see the runtime dlls for the Service Fabric are not here, and they will be downloaded when the Cluster is being created, so you basically need internet connection on the box that you are installing the Cluster.

But if that box doesn’t have internet connection you can download the runtime from the following link:   
<https://go.microsoft.com/fwlink/?linkid=839354>

So to get started we will use this *ClusterConfig.Unsecure.DevCluster.json* from the sample files.

You can use the *CreateServiceFabricCluster.ps1* file to create the cluster based on the top sample config file:

So you can open Powershell, as Administrator and run the following command:

```
.\CreateServiceFabricCluster.ps1 -ClusterConfigFilePath .\ClusterConfig.Unsecure.DevCluster.json -AcceptEULA
```

If it is the first time you are running this command you should see the following output:

![](https://cdn-images-1.medium.com/max/2560/1*JxtlfEOVFfC54J8XR8IkCA.png)

That’s it, your one-machine Service Fabric Cluster is created.

### Connect to Service Fabric Cluster

After you created the cluster you can use the following command to connect to the Cluster:

```
Connect-ServiceFabricCluster -ConnectionEndpoint <*IPAddressofaMachine*>:<Client connection end point port>
```

In my case it looks like the following:

```
Connect-ServiceFabricCluster -ConnectionEndpoint 10.1.210.110:19000
```

### Service Fabric Web UI

You can also navigate to the following url to see the Service fabric Web UI, to see the nodes, applications, etc:

<http://localhost:19080/Explorer/index.html#/>

![](https://cdn-images-1.medium.com/max/800/1*TLAc4OBasVT5vkxLC4Wyuw.png)

If you navigate to the Applications tab, you will see that there are no applications in our cluster yet. In the next post I will demonstrate how to deploy you application to this Cluster Nodes.

### Removing Service Fabric Cluster

If you wanted to clear your Service Fabric Cluster, you can use the *RemoveServiceFabricCluster.ps1* in the extracted folder like the following command:

```
.\RemoveServiceFabricCluster.ps1 -ClusterConfigFilePath .\ClusterConfig.json -Force
```

[In the next post](https://koukia.ca/deploy-a-docker-container-to-your-local-service-fabric-cluster-cb95eb22b376) I will demonstrate how to deploy your application to these Service Fabric Cluster nodes.

Cheers!
