---
layout: post
title: "Installing Redis on Windows using Docker Containers"
date: 2017-09-06
description: "I have started to look into Redis to use it as a memory cache in our systems, and while we are not hosting our components in Azure, I…"
image: https://cdn-images-1.medium.com/max/800/1*MgdgqhwAZOKoOTCyqswaJA.png
---

### Installing Redis on Windows using Docker Containers

![](https://cdn-images-1.medium.com/max/800/1*MgdgqhwAZOKoOTCyqswaJA.png)

I have started to look into Redis to use it as a memory cache in our systems, and while we are not hosting our components in Azure, I thought I look into our options to host Redis on our on-prem windows servers.

While doing this investigation, I noticed that, Redis itself does not officially support Windows: <https://redis.io/download>

From the Redis.io download page:

> The Redis project does not officially support Windows. However, the Microsoft Open Tech group develops and maintains this Windows port targeting Win64. [Learn more](https://github.com/MSOpenTech/redis)

So I thought, it is a good opportunity to see if we can use Docker as our Redis container to host Redis on our Windows servers.

### Installing Docker for windows

So the first step is to install Docker on the windows machine that we want to host our Redis on.

> **Note:** You need to [enable Hyper-V](https://blogs.technet.microsoft.com/canitpro/2015/09/08/step-by-step-enabling-hyper-v-for-use-on-windows-10/) on your Windows. and the Hyper-V role **cannot** be installed on Windows 10 Home and you need Windows 10 Professional for that.  
> **Windows Build requirements:** Docker for Windows requires Windows 10 Pro or Enterprise version 10586, or Windows server 2016 RTM to run

From the Docker download page you can get the latest stable version of Docker for windows:

[**Install Docker for Windows**  
*Docker for Windows is a Docker Community Edition (CE) app. The Docker for Windows install package includes everything…*docs.docker.com](https://docs.docker.com/docker-for-windows/install/#download-docker-for-windows "https://docs.docker.com/docker-for-windows/install/#download-docker-for-windows")

Just click on the “Get Docker for Windows (Stable)” link and follow the wizard.

![](https://cdn-images-1.medium.com/max/800/1*eg44PFDeQb17-MHEvki3NA.png)

Once the installation is done you should see the below screen and you are almost done with the installation.

![](https://cdn-images-1.medium.com/max/800/1*qvJ_iYD7P1FmMhDYNCrCrw.png)

Once you close that setup wizard, you will see the following screen that indicates the “Docker is up and running”

![](https://cdn-images-1.medium.com/max/800/1*VsHTLX0GjIXNfwxgMvQT7A.png)

If you open a powershell or command prompt window and type “docker version” you will see the version information about your Docker that you just installed, just like screen below:

![](https://cdn-images-1.medium.com/max/800/1*UeEisKe7To-1omktJVe47w.png)

### Getting the Redis image:

Now that you have successfully installed Docker, you can just run `docker pull redis` and it will start downloading the latest Redis image, and you should see something like the following screen on your command prompt.

```
c:\> docker pull redis
```

![](https://cdn-images-1.medium.com/max/800/1*k5R2dLpejyThQX3Kf0iGFQ.png)

> For more information about all the available imaged for Docker you can go to <https://store.docker.com> (it used to be <https://hub.docker.com/>)

For instance this is what you get if you go to <https://store.docker.com/redis> page:

![](https://cdn-images-1.medium.com/max/800/1*gKVAHgeyvbokcEBW7gBSCQ.png)

Now that the Redis image is downloaded on your computer, you can use the following command to start a new Redis instance with name “some-redis” on the default `6379` port.

```
c:\> docker run --name some-redis -d redis
```

This image includes `EXPOSE 6379` (the redis port), so standard container linking will make it automatically available to the linked containers (as the following examples illustrate).

### Connect to the Redis server

In order to connect to this instance that we just setup, you need to install Redis Client for windows. You can get it from the following link:

[**MicrosoftArchive/redis**  
*redis - Redis is an in-memory database that persists on disk. The data model is key-value, but many different kind of…*github.com](https://github.com/MicrosoftArchive/redis/releases "https://github.com/MicrosoftArchive/redis/releases")

Once you installed the Redis Client, you can go to that directory “program files\Redis” and type: “redis-cli” and you see that you are connected to Redis just like the following screen.

![](https://cdn-images-1.medium.com/max/800/1*HkfasivxTzCky0MIa1TQVQ.png)

Then you can try Redis commands to save values in Redis and get them.

Try commands like the following:

```
c:\> redis-cli127.0.0.1:6379> set yourkey "your test value"OK127.0.0.1:6379> get yourkey"your test value"127.0.0.1:6379>
```

For full list of redis cli commands see this page:

[**redis-cli, the Redis command line interface - Redis**  
*However redis-cli is not just that. There are options you can use to launch the program in order to put it into special…*redis.io](https://redis.io/topics/rediscli "https://redis.io/topics/rediscli")

Cheers!
