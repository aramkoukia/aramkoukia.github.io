---
layout: post
title: "Push Docker images to Azure Container Registry"
date: 2017-10-15
description: "In the previous post I demonstrated how to create docker images using docker-compose. Now I will show you how you can push those images…"
image: https://cdn-images-1.medium.com/max/800/1*c9mvlJQ0o-zQbHM3SL8zkg.png
tags: ["Containers", "Azure"]
---

### Push Docker images to Azure Container Registry

![](https://cdn-images-1.medium.com/max/800/1*c9mvlJQ0o-zQbHM3SL8zkg.png)

[In the previous post](https://koukia.ca/create-docker-container-images-to-host-in-azure-container-service-d7b8542f3642) I demonstrated how to create docker images using docker-compose. Now I will show you how you can push those images into [Azure Container Registry](https://azure.microsoft.com/en-ca/services/container-registry/).

### Azure CLI

I will be using Azure CLI version 2.0 to interact with Azure from the command prompt.

To make sure you have it installed and it is the right version run `az --version` in your command prompt to see if it is installed and what is the version.

![](https://cdn-images-1.medium.com/max/800/1*-7hfal5G6ZuxPygljIzp7Q.png)

You can download it from the following Url if you don’t have it:

<https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest>

### Create Azure Container Registry

Though you can create Azure Container Registry through the Azure portal, I’m going to do it using the Azure CLI, because the idea is, we are going to automate these processes and save these scripts and run them when we need them.

Just like any other Azure Resource, to create one, we need to put them in a resource group so it is easier to us to manage later on.

We will use the “az group create” Azure CLI command.

In the following example we are creating a Resource Group called “azurecontainerservicepoc” and located in “westus”

```
az group create --name azurecontainerservicepoc --location westus
```

**NOTE: if you have not logged in with Azure CLI, you can use the “az login” CLI command to authenticate to your Azure Account.**

![](https://cdn-images-1.medium.com/max/800/1*jXm74ZKsffr8IHJXxmOMKA.png)

Now, we can create the Azure Container Registry with the [az acr create](https://docs.microsoft.com/en-us/cli/azure/acr#create) and put it in the Resource Group we just created

```
az acr create --resource-group azurecontainerservicepoc --name acrarampoc --sku Basic --admin-enabled true
```

`acrarampoc` will be the name of the Azure Container Registry that will be created. This command mind take few minutes to complete.

![](https://cdn-images-1.medium.com/max/1200/1*sGb6M0HJfJr-N8XEhcm0vw.png)

**NOTE: This command will also create a Blob Storage Account in your Azure Subscription that will be used to host our Docker image files.**

### Login to Azure Container Registry

You can login to your Azure Container Registry with the following command:

```
az acr login --name acrarampoc
```

![](https://cdn-images-1.medium.com/max/800/1*TLhHknI8jpL7BiFemS--9Q.png)

When you see the above message, you are logged in.

### Tag the Docker images

To be able to push Docker images to Azure Container Registry, they need to be tagged with the loginServer name of the Registry. These tags are used for routing purposes when we push these Docker images to Azure.

To figure out the loginServer name of the Azure Container Registry we just created you can use the following command:

```
az acr list --resource-group azurecontainerservicepoc --query "[].{acrLoginServer:loginServer}" --output table
```

![](https://cdn-images-1.medium.com/max/1200/1*F7isr733PovCiwjj9-XL9A.png)

Then we can tag the “azurecontainerservicepoc” that we build in the previous post. with the following command.

The `:dev` at the end of the image name will be our image version.

```
docker tag azurecontainerservicepoc acrarampoc/azurecontainerservicepoc:dev
```

Then you can run the “docker images” command and see the output.

![](https://cdn-images-1.medium.com/max/800/1*Gha1rp5kIwvVA-mkokfYug.png)

### Push Docker Images to Azure Container Registry

Now that the image is tagged, we can use the “docker push” command to push this image to Azure Container Registry;

```
docker push acrarampoc.azurecr.io/azurecontainerservicepoc:dev
```

This operation might take a few minutes and you will se the image being uploaded to Azure Container Registry in the console.

![](https://cdn-images-1.medium.com/max/1200/1*o0ASUs8vYLIIG9ErRVsBfA.png)

### See which Docker images are in Azure Container Registry

Now to see the list of images that are available in your Azure Container Registry you can use the following command:

```
az acr repository list --name acrarampoc --output table
```

And you can see the Docker image we just pushed in Azure Container Registry Library:

![](https://cdn-images-1.medium.com/max/800/1*7g5tkUWSAPxp2IJKHeNYCg.png)

Also if you login to <https://portal.azure.com> you should be able to see the Azure Container Registry and this Docker image in there:

![](https://cdn-images-1.medium.com/max/1200/1*JW6wo0srMerz6gtHn1lFbw.png)

### Next Steps

[In the next post](https://koukia.ca/create-a-kubernetes-cluster-in-azure-container-service-28e281896), I will be using this Docker image that we pushed to Azure Container Registry, to host in a Kubernetes Cluster in Azure Container Service. [Stay tuned](https://koukia.ca/create-a-kubernetes-cluster-in-azure-container-service-28e281896)!

Cheers!
