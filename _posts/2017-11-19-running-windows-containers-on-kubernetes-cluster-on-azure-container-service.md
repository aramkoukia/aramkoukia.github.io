---
layout: post
title: "Running Windows Containers on Kubernetes Cluster on Azure Container Service"
date: 2017-11-19
description: "Creating the Resource Group"
image: https://cdn-images-1.medium.com/max/800/1*FRQCLwm25omfQLR4qxcmNQ.jpeg
tags: ["Containers", "Azure"]
---

### Running Windows Containers on Kubernetes Cluster on Azure Container Service

![](https://cdn-images-1.medium.com/max/800/1*FRQCLwm25omfQLR4qxcmNQ.jpeg)

### Creating the Resource Group

So to begin with we create a Resource Group to put all the resources that the Container Service creates in it, so we can manage them together more effectively.

You can either use the Azure Portal UI or use the Cloud shell to do so. Today I will try the Cloud Shell with the following command:

```
az group create --name acs-kubernetes-rg --location westus
```

You should see a “Succeeded” message like the following:

![](https://cdn-images-1.medium.com/max/800/1*e6lZINcbLL2YDUmzHwIOWA.png)

### Creating the Kubernetes Cluster on Azure Container Service

I will continue with the Cloud Shell to create the Kubernetes Cluster. I will try the following command:

```
az acs create --orchestrator-type=kubernetes --resourcce-group acs-kubernetes-rg --name=myK8sCluster --agent-count=2 --generate-ssh-keys --windows --admin-username yourusername --admin-password YourPassword
```

This will create a Kubernetes Cluster with a Linux master node (Currently Kubernetes does not support Windows Master nodes) and 2 Windows nodes as agents.

As this cluster would need to create few VMs, and some more resources, it will take several minutes to complete (For me it took around 6 minutes) and at the end your should see an output like the following:

![](https://cdn-images-1.medium.com/max/800/1*XMFrBrZu9ORybTdbhKMfjA.png)

Now if you navigate to the Azure Portal resources, you should see all the stuff that was created for you in that Resource Group:

![](https://cdn-images-1.medium.com/max/1200/1*zT2tctSufdPuQ6cQI3tf4w.png)

As you can see in the following picture, the Azure Container service, with Kubernetes Orchestrator has been created with 2 agent nodes:

![](https://cdn-images-1.medium.com/max/1200/1*exM3lPzhRvf7d4pel5p8Pg.png)

### Connecting to the Cluster on Azure from your client computer

I assume, you have Azure CLI and Kubectl installed on your computer. You can verify that you got it with the following command:

```
az --version
```

![](https://cdn-images-1.medium.com/max/800/1*5P_RREghBwtFPd31zCeORw.png)

If you don’t have the Azure CLI you can use the following link to download it:

[**Install the Azure CLI 2.0**  
*Install the new version of the Azure CLI today! We've improved and updated it to provide a great native command-line…*docs.microsoft.com](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest "https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest")

And to check your Kubectl version you can try the following command:

```
kubectl version
```

And you should see the following input.

![](https://cdn-images-1.medium.com/max/800/1*rK2qHu0ztgH35vk5FtBnuQ.png)

If you don’t have Kubectl installed, you can simply install it with the following command:

```
az acs kubernetes install-cli
```

### Opening the Kubernetes dashboard

Now that the Kubernetes Cluster is up and running, you can use the following command to open the Kubernetes Web UI dashboard:

```
az acs kubernetes browse -g acs-kubernetes-rg -n myK8sCluster
```

The name after “-g” is the Resource Group that we used to create the Cluster. and the name after the “-n” is the name of the Cluster that you can also see in the picture above.

The above command should open a web browser configured to interact with talk to a secure proxy connecting your local machine to the Kubernetes web interface.

### Pushing Windows Image to Kubernetes Cluster

You can use the following command in the Cloud Bash to pull your Windows Container Image from Azure Container Registry (assuming it is there already) to the Kubernetes Cluster and Create a Deployment:

```
kubectl run kubernetes-hubapi — image=lgmimages.azurecr.io/hubapi/hubapi:latest — port=8080
```

You should see the deployment created message like the following picture:

![](https://cdn-images-1.medium.com/max/800/1*r-jk2SMbekI6tYZgFkAmOg.png)

To check the deployment status you can use the following command:

```
kubectl get deployments
```

And then you should see the following output:

![](https://cdn-images-1.medium.com/max/800/1*XQiQNIA59vMRoNQjE59_oQ.png)

### Exposing the Service in the Kubernetes Cluster

You can use the following command to expose the service that we just pushed to the Cluster with the deployment:

```
kubectl expose deployment/kubernetes-hubapi --type="NodePort" --port 8080
```

Then you should see the following output:

![](https://cdn-images-1.medium.com/max/800/1*_0Sb4-VeBkqQd159QbgaOA.png)

If you want to see the status and the port of the service, you can use the following command:

```
kubectl get services
```

And you should see the IP of the exposed service and its port number like the following:

![](https://cdn-images-1.medium.com/max/800/1*ChQ8IfXbk6e1swdujC9rLA.png)

If you wait a little bit, the EXTERNAL-IP will show up and then you can use that IP address to access your service.

Cheers!
