---
layout: post
title: "Create a Kubernetes Cluster in Azure Container Service"
date: 2017-10-20
description: "In the previous post, we built a Docker image and then pushed it to Azure Container Registry to host. Now in this one, I am going to show…"
image: https://cdn-images-1.medium.com/max/800/1*q1NNYakYCvrNQr0JCCBucA.png
medium_url: https://medium.com/@aramkoukia/create-a-kubernetes-cluster-in-azure-container-service-28e281896
---

### Create a Kubernetes Cluster in Azure Container Service

![](https://cdn-images-1.medium.com/max/800/1*q1NNYakYCvrNQr0JCCBucA.png)

In the previous post, we built a Docker image and then pushed it to Azure Container Registry to host. Now in this one, I am going to show you how to create a Kubernetes Cluster in Azure Container Service.

> Azure Container Service allows you to quickly deploy a production ready Kubernetes, DC/OS, or Docker Swarm cluster. Learn how to use Azure Container Service with these quickstarts, tutorials, and samples.

Kubernetes on-premises seems to get bad press about it being hard to setup, though I haven’t tried to configure it my self from scratch, it seems to be pretty straight-forward when we create Kubernetes Cluster in Azure Container Service.

### Creating the Kubernetes Cluster

We can use the “az acs create” Azure CLI command to create the Azure Container Service with a Kubernetes Cluster in it.

```
az acs create --orchestrator-type kubernetes --resource-group azurecontainerservicepoc --name AramK8SClusterPoc --generate-ssh-keys
```

The `azurecontainerservicepoc` is the resource group we generated in our Azure subscription in the previous post.

The `AramK8SClusterPoc`is Kubernetes Cluster name.

![](https://cdn-images-1.medium.com/max/2560/1*X90UfD5vh47vQJkLVzcT1Q.png)

This command might take few minutes to finish and will return a json result with some information about the Azure Container Service that it created.

### Get the Kubernetes CLI going

To be able to connect to this Kubernetes cluster we created in Azure from our client computer we need to install the Kubernetes CLI or command-line interface or [kubectl](https://kubernetes.io/docs/user-guide/kubectl/). You can find more information about the kubectl from the following link:

[**kubectl**  
*Production-Grade Container Orchestration*kubernetes.io](https://kubernetes.io/docs/user-guide/kubectl/ "https://kubernetes.io/docs/user-guide/kubectl/")

If you are using the Azure Command Shell then the kubectl is already installed. And if not you can install it with the following command (you need to run your command prompt in elevated permission or Administration mode):

```
az acs kubernetes install-cli
```

![](https://cdn-images-1.medium.com/max/1200/1*ikJ55ZaOmBaG8W0cuWMpeA.png)

Note the path where this command downloads the kubectl.exe file because you are going to need it for the next steps.

### Connect to the Kubernetes Cluster

Now we can use the kubectl commands to connect to the Kuberetes Cluster we created in Azure Container Service.

To setup our kubectl to connect to the Kubernetes cluster on ACS, we can use the following command:

```
az acs kubernetes get-credentials --resource-group azureContainerServiceEast --name AramK8SClusterPoc
```

To verify the connection to your cluster, run the [kubectl get nodes](https://kubernetes.io/docs/user-guide/kubectl/v1.6/#get) command.

To do that navigate to the path (shown in the previous step) and run the following command:

```
kubectl get nodes
```

And you can see the list of nodes in this Kubernetes Cluster:

![](https://cdn-images-1.medium.com/max/800/1*bztVYftgkuo-hfe8Kt8k7A.png)

Now our Kubernetes with 4 nodes are ready to put our code in them.

[In the next post](https://koukia.ca/run-your-application-in-kubernetes-cluster-in-azure-container-service-85f87edceee3) I will show you how you can deploy your images to this cluster and manage them with Kubernetes in Azure Container Service.

Cheers!
