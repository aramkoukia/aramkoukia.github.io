---
layout: post
title: "Deploy a Docker Container to your local Service Fabric Cluster"
date: 2017-11-05
description: "In the previous post, I demonstrated how you can create a standalone Service Fabric Cluster on your local Windows Server. So the next step…"
image: https://cdn-images-1.medium.com/max/1200/1*56bRd5eeIaPfP41RkRexGA.png
tags: ["Containers", "Azure"]
---

### Deploy a Docker Container to your local Service Fabric Cluster

![](https://cdn-images-1.medium.com/max/1200/1*56bRd5eeIaPfP41RkRexGA.png)

In the previous post, I demonstrated how you can create a standalone Service Fabric Cluster on your local Windows Server. So the next step is to develop and deploy your application in your Cluster nodes.

You have various options to develop services to run on Service Fabric. Service Fabric’s default deployment and activation model is “processes”.

Though “Processes” provide the highest density usage of the resources in a cluster and the fastest activation, you have the option to deploy your application as container images as well. I believe this option is for people who want to build their ecosystem somehow independent on Service Fabric, so they can move their images to other orchestrations like Kubernetes.

Using Service Fabric we also have the option to have our services in processes and in containers in the same application.

### Build and Publish your Docker image

So the first step, is to build a Docker image, and publish it to a Docker registry. You can use any docker registry you like. I have some posts [here](https://koukia.ca/push-docker-images-to-azure-container-registry-ed21facefd0c) and [here](https://koukia.ca/create-docker-container-images-to-host-in-azure-container-service-d7b8542f3642) that explains how you can create Docker Images and publish them to Docker Registries.

Or we can just use some ready to use Docker images from [docker hub](https://hub.docker.com/r/microsoft/aspnet/).

I will just use the Microsoft Asp.Net image from the Docker hub for simplicity:

<https://hub.docker.com/r/microsoft/aspnet/>

### Create the containerized service in Visual Studio

The Service Fabric SDK will add some Service Fabric Project Templates in the Visual studio that will facilitate to build our guest containerized application for Service Fabric.

If you don’t have the Service Fabric SDK and tools you can download them from the following link:

[**Set up a Windows development environment for Azure microservices**  
*Install the runtime, SDK, and tools and create a local development cluster. After completing this setup, you will be…*docs.microsoft.com](https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-get-started "https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-get-started")

So, open Visual Studio 2017 and go File — New Project

Select “Service Fabric” template and give it a name and click OK.

![](https://cdn-images-1.medium.com/max/800/1*xYXIDuxwR_TsMIUd5FvDng.png)

Then select “Container” from the list of service templates.

In the “Image Name” section enter the path to the image you published to the Container registry. in our case it will be “[hub.docker.com/r/microsoft/aspnet](https://hub.docker.com/r/microsoft/aspnet/)”

Enter a service name, and click OK.

![](https://cdn-images-1.medium.com/max/800/1*n4zEpzqpQGSLFFh9urMr1g.png)

This should create your Serice Fabric project and open the service manifest file:

![](https://cdn-images-1.medium.com/max/1200/1*11i687Wtjyrgjp_Wib7JgQ.png)

### **Configuring Container for communication**

To be able to communicate with the containerized service, we need an endpoint.

To set the endpoint, you can open the ServiceManifest.xml file and add an `Endpoint` element with the protocol, port, and type and a a fixed port 8081. If you don’t specify a port, a random port will be assigned to the containerized service.

```
<Resources>  <Endpoints>    <Endpoint Name="GuestContainerEndpoint" UriScheme="http" Port="8081" Protocol="http"/>  </Endpoints></Resources>
```

When we add this endpoint, Service Fabric will publish this endpoint to one of the services in our Cluster called: “Naming service”, so that other components in the cluster will be able to resolve this service’s address and communicate with it. There are also other ways to communicate from one container to another one by using [reverse proxy](https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/service-fabric/service-fabric-reverseproxy.md) or some other options.

### Setting the Environment Variables

You can set Environment variables in the service Manifest file. We can do this for any type of service in Service Fabric cluster, and it is not specific to Container applications. As you can imaging you can override these variables at the time of deployment as well.

This sample service manifest shows how you can set an Environment Variable:

```
<CodePackage Name="Code" Version="1.0.0">  ...  <EnvironmentVariables>    <EnvironmentVariable Name="HttpGatewayPort" Value=""/>      </EnvironmentVariables></CodePackage>
```

If you want to override these variables in the service application manifest you can use the following snippet:

```
<ServiceManifestImport>  <ServiceManifestRef ServiceManifestName="Guest1Pkg" ServiceManifestVersion="1.0.0" />    <EnvironmentVariable Name="HttpGatewayPort" Value="19080"/>  </EnvironmentOverrides>  ...</ServiceManifestImport>
```

### Container Port to Host Port mapping

Just like any other containerized application, we should be able to map the application port in the container to the Host’s port, so that requests coming to the Host port will be redirected to the correct Container port, which our application is listening to.

To do this port mapping we can use a `PortBinding` element in `ContainerHostPolicies` element of the ApplicationManifest.xml file.

The `ContainerPort` is as you can see below is 80 and `EndpointRef` is "Guest1TypeEndpoint" (this endpoint was previously defined in the service manifest above).

This means all the Incoming requests to the service on port 8081 are redirected to 80 on the container.

```
<Policies>  <ContainerHostPolicies CodePackageRef="Code">    <PortBinding ContainerPort="80" EndpointRef="Guest1TypeEndpoint"/>  </ContainerHostPolicies></Policies>
```

### Container registry authentication

In this post I am using a public docker registry, but If your container registry is private, like you are using Azure Container Registry you need to configure the authentication arguments in the service manifest.

The following snippet is a sample configuration for authenticating against Azure Container Registry:

```
<Policies>    <ContainerHostPolicies CodePackageRef="Code">        <RepositoryCredentials AccountName="YOUR_AZURE_CONTAINER_REGISTRY_ACCOUNT" Password="YOUR_PASSWORD" PasswordEncrypted="false"/>        <PortBinding ContainerPort="80" EndpointRef="Guest1TypeEndpoint"/>    </ContainerHostPolicies></Policies>
```

You can find the latest ApplicationManifest.xml and ServiceManifest.xml with all the above changes from the following Github repository:

[**aramkoukia/local-servicefabric-poc**  
*Contribute to local-servicefabric-poc development by creating an account on GitHub.*github.com](https://github.com/aramkoukia/local-servicefabric-poc "https://github.com/aramkoukia/local-servicefabric-poc")

### Deploy the Docker image to Service Fabric Cluster

Now that we have it all configured, it is time to deploy our image to the Service Fabric.

You can right click on the Project and click “Publish”.

![](https://cdn-images-1.medium.com/max/800/1*01anKrrT61XaAZM7mMqyiA.png)

In the “Connection Endpoint” you need the local Service Fabric address. in our case if you remember from the [previous post](https://koukia.ca/create-an-azure-service-fabric-cluster-on-your-local-windows-server-54a23962e465) was:

[10.1.210.110:19000](http://10.1.210.110:19080)

But this address is readonly on this page and it reads it from the Local.1Node.xml file. You can set the above address in the Local.1Node.xml file in your solution and in the publish page, select that local.1node.xml file, then you should see this above address in the Connection Endpoint.

![](https://cdn-images-1.medium.com/max/800/1*4FOt1NrpGPrHo5GNzpt3Wg.png)

Now, when you click publish it will start the publish operation. At this point if you navigate to your local Service Fabric Url ([from the previous post](https://koukia.ca/create-an-azure-service-fabric-cluster-on-your-local-windows-server-54a23962e465), our Url was: <http://10.1.210.110:19080>)

![](https://cdn-images-1.medium.com/max/1200/1*kvHShT3afGwhohxjQ_sYlQ.png)

Until service fabric downloads and runs the Docker image you will see the “Health State” as Error. After few minutes that it completes the image download and ran the application you should see the Status as “Ready”:

![](https://cdn-images-1.medium.com/max/1200/1*Xu8fpaOZptxgnYaTdqGmZA.png)

Since our Host exposed port as we set it up above was 8081, you can open a browser to this address: [http://10.1.210.110:808](http://10.1.210.110:19080)1

![](https://cdn-images-1.medium.com/max/800/1*9tD7B73lTP_zQmD0XjZ_sQ.png)

Now, you have your application running in a Docker Container, inside your Local Service Fabric.

Cheers!
