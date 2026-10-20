---
layout: post
title: "Deploying Docker Containers to Azure App Service"
date: 2017-10-07
description: "When you containerize your application and want to use Azure to host it, there are 3 main options out there right now that you can use. And…"
image: https://cdn-images-1.medium.com/max/800/1*lRlfF0Tx8hD53ZYniVFmKg.png
medium_url: https://medium.com/@aramkoukia/deploying-docker-containers-to-azure-app-services-672d587c5c39
---

### Deploying Docker Containers to Azure App Service

![](https://cdn-images-1.medium.com/max/800/1*lRlfF0Tx8hD53ZYniVFmKg.png)

When you containerize your application and want to use Azure to host it, there are 3 main options out there right now that you can use. And each one comes with its own features and level of management and administration.

Different options to host Containers in Azure are:

1. Azure Container service
2. Azure Service Fabric
3. Azure App Service

In this post I have eliminated the CI/CD aspect of a real workflow and will just demonstrate how to publish your containerized application, directly from your Visual Studio to Azure App Service through Azure Container Registry.

The following image shows the workflow that we are about to see.

![](https://cdn-images-1.medium.com/max/1200/1*SVsIlP5f7AGVlWVvM0iclw.png)

Now with Visual Studio 2017, when you install the Web Workload, you are going to get the container tools which includes the “Publish” to Azure App Services.

Let’s get started.

Open up Visual Studio 2017 and go File > New Project and select ASP.NET Core Web Application, just like the following image:

![](https://cdn-images-1.medium.com/max/800/1*DGWLOxSYuFo_wm0keI4jqw.png)

Then you enter your Solution and Project name and click OK, and on the next screen select the Web Application MVC project template.

Make sure you check the “Enable Docker Support” at the bottom of the screen just like bellow and select the Linux as OS just for fun! **Yup, .Net runs on Linux now!**

![](https://cdn-images-1.medium.com/max/800/1*l2LfgpjRts544By8_G9_IQ.png)

Now you have a .Net Core Web Application ready to go. Right click on the project and select “Publish”. Then you should see different publish options like the screen below. Now you select the “Azure App Service Linux” option and click “Publish”

![](https://cdn-images-1.medium.com/max/1200/1*MOR6rW9SMUdGpx74rjWThw.png)

Then you will see the publish dialog which is essentially the same Publish screen we used to see for regular App Service deployment without container. This one just has an extra item there which is the “Container Registry” that is our resource in Azure that keeps our application’s docker image in Azure that contains our compiled code.

At this point you just select your App Name, Subscription, Resource Group, App Service Plan, Container Registry and click “Create”

![](https://cdn-images-1.medium.com/max/800/1*6b4ArsorfIAMc0jc1IHB1g.png)

Once all those resources are created, your docker image will be deployed to Azure.

In the Publish summary window you can see the Url of your web application just like the following image:

![](https://cdn-images-1.medium.com/max/800/1*v8arN9xv6XdS69Bk-HxSSw.png)

Now you click on the your applications link, and Wallaaaa!

> At this point your .Net Core Web Application is running in a Linux Docker Container, on Azure App Service!

![](https://cdn-images-1.medium.com/max/1200/1*VeE9B83L0a4E7z8FNnhwWQ.png)

Now if you open the Azure portal (<https://portal.azure.com>) and select your Web Application, you can see all the options that a regular Web Application settings used to have plus one that is specific to Docker.

![](https://cdn-images-1.medium.com/max/1200/1*AF9PO8D2jlULnUvu1HOe5Q.png)

If you click on the “Docker Container” menu, you can see some information about your Docker image there, like your image name, the source of your image (in this case it is “Azure Container Registry”), the version of your image (tag) and some Continuous Deployment settings.

![](https://cdn-images-1.medium.com/max/1200/1*dMDkIj8HyOxJ5b3HQ2DzVg.png)

I believe enabling users to host Docker containers in Azure App Service is one of the biggest moves that Azure has released in the pas year.

Cheers!
