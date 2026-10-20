---
layout: post
title: "Asp.Net Web Api is dead, long live Asp.Net Core"
date: 2017-05-06
description: ".NET community (Yeah, it is open source now) decided to have ONE controller for both MVC and WEB API when ASP.NET core was released."
image: https://cdn-images-1.medium.com/max/2560/1*jujefnOsXMzvh0KIDgKX4w.png
---

### Asp.Net Web Api is dead, long live Asp.Net Core

![](https://cdn-images-1.medium.com/max/2560/1*jujefnOsXMzvh0KIDgKX4w.png)

.NET community (Yeah, it is open source now) decided to have **ONE** controller for both MVC and WEB API when ASP.NET core was released.

Side exciting news :

> [**.Net Core 2.0, is targeted for ZBB milestone on May 10, so pretty exciting**](https://github.com/dotnet/corefx/issues/17619)

The MVC controller and WEB API controller were technically the same (I ask the difference between the two in my technical interview questions!) now with .Net Core they are absolutely the same, now you can decide to serve Html or Json.

In this post, I will briefly touch on, how to make a RESTful API using Asp.Net Core Web API.

### What is the difference between ASP.NET Web API Controller and MVC Controller ?

Nothing much. Only difference is that the Asp.Net Web Api does not have a view engine like the MVC Controller (Razor View Engine) and was designed to be used to build REST APIs to serve Json data.

Also the Web API’s purpose was to replace WCF, SOAP and even older APIs solutions Microsoft had (ASMX services — Not sure if you have even heard about these).

Asp.Net Web Api, also supports [OData](https://docs.microsoft.com/en-us/aspnet/web-api/overview/odata-support-in-aspnet-web-api/odata-v4/create-an-odata-v4-endpoint) to enable the client to do some basic queries on the data which MVC controllers did not have this support.

### Port your existing Asp.Net Web API Controllers by Using a Compatibility Shim

Asp.Net Web Api controllers inherit from ApiController class, which no longer exists in ASP.NET Core. Now to get around that we need to include a nuget package called WebApiCompatShip [Microsoft.AspNetCore.Mvc.WebApiCompatShim](https://www.nuget.org/packages/Microsoft.AspNetCore.Mvc.WebApiCompatShim/) and keep using the ApiController.

The WebApiCompatShip code is opensource on [GitHub](https://github.com/aspnet/Mvc/tree/master/src/Microsoft.AspNetCore.Mvc.WebApiCompatShim) in case you want to see what it does.

If you are using HttpResponseMessage in your Web API controllers, you need to make one small code change in your Startup class to call AddWebApiConventions().

This will hook up the HttpResponseMessageOutputFormatter to help and hint the Json serializer to do it’s serialization magic properly.

Also there is a change needed in your routing. In the following code snippet I show how to register a route in your startup class.

That’s it! Now you can move the rest of your code to the Asp.Net Core project and it will work just fine!

Here is a sample controller with two controller action that return an Enumerable and HttpResponseMessage within ASP.NET Core using the compatibility shim.

### Using the New ASP.NET MVC 6 Controllers to Act as a RESTful Web API

The new MVC 6 that comes with ASP.NET Core has the best of both MVC and Web API worlds from ASP.NET.

Now you can serve a View or a Json response to a client from the same Api Controller. From any controller, you can return a View or object and MVC will take care of serializing it for you. Multiple [different routing styles](https://docs.microsoft.com/en-us/aspnet/core/mvc/controllers/routing) enable you to implement basic MVC web applications or more REST-style APIs.

#### Web API project is not available for ASP.NET Core projects, but you can use your existing Web API code with the compatibility shim.

Now, go ahead and add your Web Api components as “Technical Debt” user stories in your backlog, and start planning on the migration to .Net Core and as your business case you can pitch this with, the great performance of the .Net Core code.

Cheers!
