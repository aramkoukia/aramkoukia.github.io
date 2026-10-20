---
layout: post
title: "Create Docker container images to host in Azure Container Service"
date: 2017-10-15
description: "Azure Container Service is one of the solutions that Azure provides for us, to host our containerized software components without having to…"
image: https://cdn-images-1.medium.com/max/800/1*wZl2fkDHEU2YI2FwZ1uWUQ.jpeg
---

### Create Docker container images to host in Azure Container Service

![](https://cdn-images-1.medium.com/max/800/1*wZl2fkDHEU2YI2FwZ1uWUQ.jpeg)

Azure Container Service is one of the solutions that Azure provides for us, to host our containerized software components without having to worry about provisioning VMs (low level solution with a lot of management overhead) or using Azure App service which is a very high level PaaS platform. It is almost something between an IaaS and a PaaS service.

In this post I’m going to show you how to use Docker Compose to build some images from your application, then later on, you can push that image to Azure Container Registry and Azure Container Service.

### Create your application

So to get started, you can Open Visual Studio 2017, go File -> New -> Project and select the Asp.Net Core Web Application project template.

Make sure you check the “Enable Docker Support” check box on the wizard, and select Windows or Linux.

![](https://cdn-images-1.medium.com/max/800/1*dGsKZmrziNfwd0-YPEKePw.png)

Then you can add your solution to a GIT repository, and push it to Github or Visual Studio Team Services.

I have pushed the code to this repo in case you want to see the docker files etc:

<https://github.com/aramkoukia/Azure-Container-Service-Poc>

### Create a Container Image from Application Source

Now we are going to use [Docker Compose](https://docs.docker.com/compose/) can to build Docker images and then later on deploy these images to our Azure Container Service.

To build the Docker image you can run the `docker-compose.yml` file with the following command:

```
docker-compose up -d -f "C:\ACSPoc\Azure ContainerServicePoc\docker-compose.yml"
```

![](https://cdn-images-1.medium.com/max/800/1*bpT6ik3eHkWf7MZS3IKOHg.png)

When completed, use the [docker images](https://docs.docker.com/engine/reference/commandline/images/) command to see the created images.

```
docker images
```

![](https://cdn-images-1.medium.com/max/800/1*Np-YoEK_iz7-QE-dSmBYww.png)

Then you can run the [docker ps](https://docs.docker.com/engine/reference/commandline/ps/) command to see the running images:

```
docker ps
```

![](https://cdn-images-1.medium.com/max/2560/1*2h0zPDwn9yJLddzpG_-0Aw.png)

As you can see our azurecontainerservicepoc image is running after we ran the docker-compose command.

### Running the Application in local Docker environment

Now you can just open this app at address: <http://localhost:32769> and you should see the .Net Core Web App in the browser.

### Cleaning up

If you want to stop this image from running you can use the following command:

```
docker-compose stop
```

Also if you want to remove the image you can use the following command:

```
docker-compose down
```

### Next Steps

[In the next post](https://koukia.ca/push-docker-images-to-azure-container-registry-ed21facefd0c) I will demonstrate how you can push this Docker image to Azure Container Service. Stay tuned

Cheers!
