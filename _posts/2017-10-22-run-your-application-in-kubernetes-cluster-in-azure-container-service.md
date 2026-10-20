---
layout: post
title: "Run your application in Kubernetes Cluster in Azure Container Service"
date: 2017-10-22
description: "In a series of blogs, we built Docker container images, pushed those Docker images to Azure Container Registry and then Created a…"
image: https://cdn-images-1.medium.com/max/800/1*gBCQs2axJ0YEcp3X8FoWcw.png
medium_url: https://medium.com/@aramkoukia/run-your-application-in-kubernetes-cluster-in-azure-container-service-85f87edceee3
---

### Run your application in Kubernetes Cluster in Azure Container Service

![](https://cdn-images-1.medium.com/max/800/1*gBCQs2axJ0YEcp3X8FoWcw.png)

In a series of blogs, we [built Docker container images](https://koukia.ca/create-docker-container-images-to-host-in-azure-container-service-d7b8542f3642), [pushed those Docker images to Azure Container Registry](https://koukia.ca/push-docker-images-to-azure-container-registry-ed21facefd0c) and then [Created a Kubernetes Cluster in Azure container service](https://koukia.ca/create-a-kubernetes-cluster-in-azure-container-service-28e281896). Now it is time to run that Docker image we built in the Kubernetes cluster from the previous post.

### Build the Kubernetes manifest file

The following is the sample Kubernetes manigest file I have. I have also commited it to the github repo from our Docker image post:

[**aramkoukia/Azure-Container-Service-Poc**  
*Contribute to Azure-Container-Service-Poc development by creating an account on GitHub.*github.com](https://github.com/aramkoukia/Azure-Container-Service-Poc/blob/master/Azure%20ContainerServicePoc/azure-container-service-poc.yml "https://github.com/aramkoukia/Azure-Container-Service-Poc/blob/master/Azure%20ContainerServicePoc/azure-container-service-poc.yml")

Before running the application, the ACR login server name needs to be updated in the Kubernetes manifest file.

You can get the Azure Container Registry login server name with the following command:

```
az acr list --resource-group azurecontainerservicepoc --query "[].{acrLoginServer:loginServer}" --output table
```

![](https://cdn-images-1.medium.com/max/1200/1*Iya_e0jF3DKTs9fx4Wso0g.png)

Then in the Kubernetes Manifest file above you can change the ACS\_LOGIN\_Server with the AcsLoginServer name returned from the above command:

![](https://cdn-images-1.medium.com/max/800/1*QHOVVHqs1NgHQdnANDsMDg.png)

### Deploy to Kubernetes Cluster

Now that we have the Kubernetes Manifest file all set, we can deploy our application to the Cluster.

We can use the kubecctl (the Kubernetes CLI tool that we used in the previous post) to run the application.

This command processes the the Kubernetes manifest file and creates the defined Kubernetes objects defined in it.

So now in the command prompt you just navigate to the path you have your Manifest file and run the following command:

```
kubectl create -f azure-container-service-poc.yml
```

Then you should see the following output:

![](https://cdn-images-1.medium.com/max/1200/1*vSv80k1EgQKiz0eBnqgMcw.png)

### Checkout the Container Service in Azure portal

If you go to portal.azure.com now, and check out the resource group you should see all the resources related to your Kubernetes Cluster in there, like Load Balancers, Route Table Public IP Address etc.

![](https://cdn-images-1.medium.com/max/2560/1*zYcRnsEpN01tM8jOlhDJsg.png)

And if you select the Azure Container Service from the list, you should see the List of agents that are involed in our Kubernetes Cluster. In this case it would be 3 nodes, which 2 are our application and 1 is the Load Balancer.

![](https://cdn-images-1.medium.com/max/1200/1*osVr0bU0Ps1od1fUfxUMNg.png)

### Testing the Application in Kubernetes Cluster

After running the above command a [Kubernetes service](https://kubernetes.io/docs/concepts/services-networking/service/) is created which makes your application accessible from the internet. This process might take a few minutes to complete.

To check out the progress you can use the following kubectl command to watch what’s going on…

Use the following command to see the progress:

```
kubectl get service azure-container-service-poc --watch
```

If you type the above command quickly, you will see the **EXTERNAL-IP** for the for the `azure-container-service-poc` service displayed as `pending`. And after few minutes that Pending should change to an actual IP address, then you can press Ctrl +C to stop watching that process.

![](https://cdn-images-1.medium.com/max/800/1*XA1f1GCaEoUkCVTTUqP0Dg.png)

At this point you should be able to access your application using the EXTERNAL IP in a browser

![](https://cdn-images-1.medium.com/max/800/1*uSCL4cHdUim3fi6dTN8P6w.png)

Now you can see your application is running behind a Load Balancer, in a Kubernetes Cluster, hosted in Azure Container Service.

In the next post, I will demonstrate how you can manage your application that is hosted in Kubernetes Cluster in terms of Scaling them, or Monitoring them. Stay tune

Cheers!
