---
layout: post
title: "Configuring Docker Swarm as Container Orchestrator on Windows"
date: 2017-11-30
description: "I have been looking into different Container Orchestrator options like Kubernetes and Azure Service Fabric recently, and now I want to see…"
image: https://cdn-images-1.medium.com/max/2560/1*dybB9cpWGPfRB5y_E6Upxw.jpeg
tags: ["Containers", "Azure"]
---

### Configuring Docker Swarm as Container Orchestrator on Windows

![](https://cdn-images-1.medium.com/max/2560/1*dybB9cpWGPfRB5y_E6Upxw.jpeg)

I have been looking into different Container Orchestrator options [like Kubernetes](https://koukia.ca/running-windows-containers-on-kubernetes-cluster-on-azure-container-service-99e8de0d9cf4) and [Azure Service Fabric](https://koukia.ca/create-an-azure-service-fabric-cluster-on-your-local-windows-server-54a23962e465) recently, and now I want to see how I can do the same thing with Docker Swarm.

### What is Docker Swarm or Swarm Mode

Docker Swarm, is a feature by the Docker team that enables us to have a Cluster of Docker containers and schedule and manage them from the Swarm APIs.

When a group of Docker containers are running together (as a Cluster) they are referred to as “Swarm Mode” in the Docker echo-system.

### **Docker Swarm Architecture**

There are 2 types of nodes in Docker Swarm. Manager nodes and Worker nodes.

The names are kind of self explanatory. Manager nodes are the nodes that control the cluster and worker nodes are the ones that run our application.

A cluster should have at least one Manager node (it is recommended to have more than one), and all the Docker CLI commands that you want to run, should go through these nodes. Manager nodes are aware of the state of the cluster and are constantly monitoring all the nodes.

If a worker node wants to join the Cluster, they have to provide a Join Token (which is provided by Manager nodes) to the Manager node to join the cluster.

### Creating a Docker Swarm Cluster

As I mentioned earlier, I am going to use Windows 10 to create the Swarm Cluster.

Now to get started, open a command prompt and use the following command to create your first Swarm Cluster.

```
C:\> docker swarm init --advertise-addr=<HOST-IP-ADDRESS> --listen-addr <HOST-IP-ADDRESS>:2377
```

<HOST-IP-ADDRESS> is the IPv4 of the computer you are initializing the Cluster on.

**Note:** TCP port 2377 needs to be open for cluster management communications on the Host computer.

At this point the Docker engine on your computer will start a Docker Swarm Cluster and you should see the following output:

![](https://cdn-images-1.medium.com/max/1200/1*dBCIAPGex3kSELCiOB3Xhw.png)

As you can see above, the Manager node has provided us a “Join Token” which we will use to add Worker nodes to this Cluster in the next section.

### **Adding a Worker node to our Swarm Cluster**

Now that the Swarm Cluster is running and we got the “Join Token” we can add our first worker node to our Cluster using the following command:

```
C:\> docker swarm join --token <JOIN-TOKEN> <NODE-IP-ADDRESS>
```

Again the <NODE-IP-ADDRESS> is the IPv4 of the other Docker host that you want to join the Cluster. And the <JOIN-TOKEN> is the token that the Manager node provided when we initialized the Swarm Cluster in the previous section.

***One big difference that you can see right away compared to Kubernetes is that, you actually have to have nodes (Docker hosts) in the network and join them one by one to the cluster, where as in Kubernetes or Service Fabric, it is all virtualization and they create the Cluster for you based on the number of the nodes you ask, on ONE computer.***

If you somehow missed to pick up the “join token” from the “Docker Swarm Init” command, you can use the following command to get it again:

```
C:\> docker swarm join-token worker -q
```

### Adding Manager nodes to Swarm Cluster

If you need to add a another Manager node to to the cluster, this above token is no good! and you would need a “Manager Join Token” which you can get using the following command:

```
C:\>   docker swarm join-token manager -q
```

![](https://cdn-images-1.medium.com/max/1200/1*C1V9tH9XNH9rxKKZ5oMnRA.png)

Now you can use the above token in the following command to add your new Manager Node to the Swarm Cluster:

```
C:\> docker swarm join --token <MANAGER-JOIN-TOKEN> <MANAGER-IP-ADDRESS>
```

### Overlay Network

Another concept that you need to be familiar with is this “Overlay Network”, which is basically a virtual network that is created between the nodes in the Swam Cluster that connects them all together so they can communicate.

The following command will create an Overlay Network in the Cluster for you:

```
C:\> docker network create --driver=overlay <NETWORK-NAME>
```

<NETWORK-NAME> is just an alias we give to this network and later on, when we create services in the Cluster, we specify this alias for those services.

![](https://cdn-images-1.medium.com/max/800/1*X5v3v2r9vkX1_2Rd0IFi8g.png)

This is one of the approaches that Docker Swarm uses to create isolations between nodes in the Swarm Mode.

***ie: If you want some services to be able to communicate, put them in one network and if not, well, then put them in a different network.***

### Deploy your services to Docker Swarm Cluster

At this point all the nodes (Managers and Workers) are added to the Swarm Cluster and we have also created an Overlay network in the Cluster so they can communicate with each other. Now it is time to deploy our services to the Cluster.

You can use the following command to create a service, with specifying its Overlay Network and Container Image:

```
C:\> docker service create --name=<SERVICE-NAME> --endpoint-mode dnsrr --network=<NETWORK-NAME> <CONTAINER-IMAGE>
```

<SERVICE-NAME> is just an alias for the service name

<NETWORK-NAME> is the name of the Overlay Network we created in the previous section

<CONTAINER-IMAGE> is the Docker image what we want to deploy to this node.

And you should see the following output:

![](https://cdn-images-1.medium.com/max/800/1*WBG6oerM4Xf4-qdjoBGLJg.png)

The `--endpoint-mode dnsrr` argument is setting the policy that will be used for balancing the requests between the services in the Swarm Cluster.

***Currently on Windows dnsrr which is DNS Round Robin is the only supported load balancing policy.***

And to see a summary of what is going on on the Cluster you can use the following commands:

```
C:\> docker nodes ls
```

```
C:\> docker network ls
```

```
C:\> docker service ls
```

And you should see list of Nodes, Networks and Services on the Swarm Cluster like below:

![](https://cdn-images-1.medium.com/max/800/1*Wl3GnJXJyMUQx2wzWBlOsQ.png)

### Scaling your Services

One of the basic features that you would expect from a Container Orchestrator is to be able to scale up easily, and of course this is something Swarm Does easily.

When you create Service in Docker Swarm, by default it creates one instance (replica) of it, though you could change the default with “— replicas” argument in the “docker create service” command.

But if need to have more instances running on the Cluster after you creaated the Service, you can use the following command:

```
C:\> docker service scale <SERVICE-NAME>=<REPLICAS>
```

<SERVICE-NAME> is the name of the service and <REPLICAS> is the number of instances you want to have.

And you should see the following output:

![](https://cdn-images-1.medium.com/max/800/1*YT22J4OlKrOo7TyYl4pS6g.png)

Overall in my opinion, Docker Swarm seems to be pretty easy to setup and very straight forward to get started with!

Cheers!
