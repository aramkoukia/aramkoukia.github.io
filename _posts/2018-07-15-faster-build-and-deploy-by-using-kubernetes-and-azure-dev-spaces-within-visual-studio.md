---
layout: post
title: "Faster build and deploy, by using Kubernetes and Azure Dev Spaces within Visual Studio"
date: 2018-07-15
description: "One of the issues that you will have while working with container images and Kubernetes, is the build process when you are coding."
image: https://cdn-images-1.medium.com/max/800/1*9zUAAdF5hEf15vMPVV_rMQ.png
tags: ["Containers", "Azure", ".NET"]
---

### Faster build and deploy, by using Kubernetes and Azure Dev Spaces within Visual Studio

![](https://cdn-images-1.medium.com/max/800/1*9zUAAdF5hEf15vMPVV_rMQ.png)

One of the issues that you will have while working with container images and Kubernetes, is the build process when you are coding.

Like when you have everything running in a Kubernetes Cluster in Azure and you just want to make some changes and push it to the cluster, normally you would have to compile the code, build a new docker image, and then push it to the cluster, which can take some time.

But today what we want to do is, to make some code changes and push the change directly to an already running Kubernetes cluster without the need to build and push a new docker image, by using Azure Dev Spaces.

#### What’s this Azure Dev Spaces?

Azure Dev Spaces is built to improve the developer teams experience working in a Kubernetes environment in Azure.

With a little bit of setup you will be able to start debugging your code that is running in an Azure Kubernetes Cluster (AKS).

Azure Dev Spaces is basically there to make our life as developers that work with Kubernetes clusters easier. With Azure Dev Space you can share a Kubernetes cluster with the team you are working with and do your end to end integration testings without the need to mock all the dependencies.

#### What do I do to use Azure Dev Spaces?

I bet this already sounds like something you want for sure!

Before we get started, we need a running Kubernetes cluster in Azure that has Http Routing enabled.

You can **enable** the ***Http Routing*** in the Networking configuration tab in the Azure Portal.

![](https://cdn-images-1.medium.com/max/800/0*e_0W4iIO8BU3l1VM.png)*Enabling Http Routing in your Azure AKS*

And then obviously you have your Visual Studio installed and on top of that make sure you install the [Visual Studio Tools for Kubernetes](https://aka.ms/get-azds-visualstudio) that will give us the features to interact with our AKS cluster from our Visual Studio.

#### Let’s start coding

Now that we have all the tools installed, we can create a new application and set it up for our Azure Dev Spaces.

Lets go File => New Project and select an ASP.Net Core Web Application with .Net Core 2.0 target framework.

Now we can enable Dev Spaces for our Azure Kubernetes Cluster. To do that click in the Launch settings dropdown and select the “Azure Dev Spaces” menu.

![](https://cdn-images-1.medium.com/max/800/1*95EIzKouZXAFgE7Q4h916Q.png)

In the dialog, you login with the right user account and select the AKS cluster, and check the “Publicly Accessible” checkbox so that our web application will be accessible as a public endpoint and then click OK.

![](https://cdn-images-1.medium.com/max/800/1*nItQVlYGUWREsr-f5z5fgQ.png)

In case the Cluster you selected is not properly configured to be used with Azure Dev Spaces, you will get a message to configure the cluster like the following:

![](https://cdn-images-1.medium.com/max/800/0*oct7mso6RyavU1XQ.png)

After this, a bunch of files are added to our project.

Look at the files added to project.

- First of all a `charts` folder. The files in there are used to deploy our application into the AKS Cluster via the Azure Dev Spaces.
- `Dockerfile` also is added that has all the information it needs to package the application and build a docker image for us.
- `azds.yaml` is also added that contains contains development-time configuration that is needed by the Azure Dev Space.

![](https://cdn-images-1.medium.com/max/800/1*ykIhjVL8GZNw1167TJmy2A.png)

That’s pretty much it. Your Azure Dev Space is successfully created at this point and you can start debugging.

If you put a break point in one of the controllers now, and press F5, Visual Studio will talk to the Azure Dev Space, build and deploy your application to the AKS cluster, and will hit your breakpoint!

At first it might look like the container is running on your local computer, but it is not and it is actually running in the Azure Dev Space in Azure!

The reason that you see the “localhost” address is because Azure Dev Space creates a temporary SSH ctunner to the container that is running in Azure Kubernetes Cluster.

#### How do I make a code change and deploy to the Kubernetes Cluster?

It’s easy! you just do what you used to do as if you are using your local IIS express.

Like if you change an Html or Css file, you can just change it and without restarting the debug session, just refresh the browser and you should see your change right away!

Remember what you see in the browser is being served from the AKS cluster in Azure!

And if you want to change any C# code, you stop debugging, make the change and press F5 again and then new code is deployed to the AKS cluster now!

Pretty amazing, isn’t it?

**Without this, the alternative would be to build a new docker image each time the code is changed and push the image to a docker image store and deploy it to the Kubernetes Cluster, but with Azure Dev Spaces, you can do that by pressing F5 from Visual Studio.**

This is an amazing feature if you are using Kubernetes in Azure and will save you a ton of time for sure!

If you are interested in learning a bit more about Kubernetes, here are a couple books for you:

[![](https://cdn-images-1.medium.com/max/800/1*0Vg1dSnYv_GYFck5Cvhwuw.jpeg)](https://amzn.to/2NPS56t)*Kubernetes Up & Running: <https://amzn.to/2NPS56t>*

[![](https://cdn-images-1.medium.com/max/800/1*g-hXYt-cMnThdBnttWiU_Q.jpeg)](https://amzn.to/2NTPkBo)*Mastering Kubernetes: <https://amzn.to/2NTPkBo>*

Cheers!
