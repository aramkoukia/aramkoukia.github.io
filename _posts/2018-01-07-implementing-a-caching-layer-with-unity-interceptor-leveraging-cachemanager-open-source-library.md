---
layout: post
title: "Implementing a Caching layer, with Unity Interceptor, leveraging CacheManager open source library"
date: 2018-01-07
description: "Recently I started looking into improving some of our Caching code, and we decided to implement it using some Aspect Oriented Programming…"
image: https://cdn-images-1.medium.com/max/800/1*M8iRf-agb7RrZj5TngdFbg.png
tags: [".NET", "Architecture"]
---

### Implementing a Caching layer, with Unity Interceptor, leveraging CacheManager open source library

![](https://cdn-images-1.medium.com/max/800/1*M8iRf-agb7RrZj5TngdFbg.png)

Recently I started looking into improving some of our Caching code, and we decided to implement it using some [Aspect Oriented Programming (AOP)](https://en.wikipedia.org/wiki/Aspect-oriented_programming) approach.

Looking at different options, like [PostSharp](https://www.postsharp.net/), [CastleWinsdor](http://www.castleproject.org/projects/windsor/), [SimpleInjector](https://simpleinjector.org/index.html), and [Unity Interceptor](https://msdn.microsoft.com/en-us/library/dn178466%28v=pandp.30%29.aspx), the decision was (I’m not going to go through all the decision points in this post, but it was mainle because we were already using Unity Interceptor for other purposes) to use Unity Interceptor to build our Caching as a piece of cross-cutting code.

We also looked at different options we have to do the actual caching, and we ended up using an Open Source library called [CacheManager](http://cachemanager.michaco.net), that supports multiple caching mechanisms, like [Redis Cache](https://redis.io/), m[emcached](https://memcached.org/), etc.

For more details about CacheManager and all its features, take a look at the following link:

[**Cache Manager - Caching Framework for C# .NET**  
*CacheManager is an open source caching framework for .NET written in C# and is available via NuGet. It supports various…*cachemanager.michaco.net](http://cachemanager.michaco.net/ "http://cachemanager.michaco.net/")

Now, In this post I will explain how you can implement a Cache layer using Unity Interceptor and CacheManager in a simple ASP.NET Web API project.

### Getting Started

To get started, open Visual Studio and create a new ASP.Net Web API Project. Then, Add the Unity.AspNet.WebApi package, which will add all the required classes to configure our Unity Container

![](https://cdn-images-1.medium.com/max/800/1*pFGOaP7VvyjWIXrNDt6HXw.png)

And then we need the Unity Interceptor Nuget package.

![](https://cdn-images-1.medium.com/max/1200/1*wEEqIG7-e-X4hEox-D-IeQ.png)

This package will install both Unity.Abstractions and Unity.Interception for you.

Then we need the CacheManager dlls. and we can get them by installing CacheManager.SystemRuntimeCaching nuget package.

![](https://cdn-images-1.medium.com/max/1200/1*m7kGUdf9gECdpBfpSQeDug.png)

At this point, we have all the dlls we need to start writing some code.

For testing purposes, I am going to rename one of the Controller classes that are added by default (ValueController.cs) to be UserController and add a couple of classes to test the actual caching code (UsersRepository and IUserRepository)

You can find the code for all these classes, in the github repository mentioned at the end of this post.

### Unity Configuration to start method interception

The first step is to configure our unity container to specify which “types” need to be intercepted for our caching purposes.

Under the App\_Start folder in your solution, if you open your UnityConfig.cs file, it should look like the following.

As you can see in the above code, I have added a DefaultInterceptor for the IUserRepository interface. This lets the Unity Interceptor know that we want to intercept methods defined in this interface.

### Introducing Cache Attribute and Cache Attribute Handler

Now, we don’t want to intercept or cache all the methods that exist in that interface that we configured in the Unity Container, so we define some Attribute that we will put on top of some of the methods, and that will tell the interceptor which one of the methods to intercept.

And then we will add an Attribute handler for the attribute to trigger when that method is called, and that is where we actually do the Caching operation.

For that I added a class for CacheAttribute.cs that looks like the following:

And now we need to implement the class that will do the Cache Handling used in the above Cache Attribute class.

For that I add a new class called CacheAttributeHandler.cs and it will look like the following:

### **Cache Manager configuration**

As you can see in the above snippet, the Cache Manager is configured and instantiated! Yes, it is very simple to set it up and you can start using it with the few lines of code:

```
var config = new ConfigurationBuilder() .WithSystemRuntimeCacheHandle() .Build(); _cache = new BaseCacheManager<object>(config);
```

```
var result = _cache.Get(KeyPrefix);
```

### Using the Cache Attribute

Now what is left is to decorate the methods that we are interested in, with the Cache attribute and we are good to go.

For instance, our UserRepository.cs class with the Attributes will look like the following:

**Note: You can put the Attributes on top of the methods in the class implementation or in the interface.**

**As a good general practice it is better to put them on the interface methods.** Because if you change the actual implementation at any point, or have a different implementation of the same interface, you dont need to worry about the attributes, because they will apply to the new implementation automatically.

This might happen specially when using Repository pattern and for example you want to switch from Entity Framework to Dapper or something.

If you decide to put your Attributes on the Interface methods, it will look like the followig:

### Adding Invalidate Cache Attribute

Now, we keep coding and basically copy and paste CacheAttribute.cs and CacheAttributeHandler.cs and rename them to be InvalidateCacheAttribute.cs and InvalidateCacheAttributeHandler.cs

This is how my InvalidateCacheAttribue.cs looks like:

And then similar changes to the InvalidateCacheAttributeHandler and this is how it looks like:

That’s it, you got a Caching layer implemented that intercepts any method that is decorated with your attribute, to Cache or Invalidate cache.

Now if you want to continute to extend this code, you probably need to consider the input arguments for each method to be as part of your Cache Key (In addition to the CachePrefix that is being passed in to the attribute).

### **Complete Solution**

As always, if you didn’t follow the steps and just want the final project, you can find it on github:

[**aramkoukia/CachingAspectOrientedImplemetation-With-CacheManager**  
*CachingAspectOrientedImplemetation-With-CacheManager - Caching Aspect Oriented Implementation With Unity Interceptor…*github.com](https://github.com/aramkoukia/CachingAspectOrientedImplemetation-With-CacheManager "https://github.com/aramkoukia/CachingAspectOrientedImplemetation-With-CacheManager")

Cheers!
