---
layout: post
title: "Build your first Web API with F#, Giraffe and host it on Azure Cloud"
date: 2018-09-15
description: "Today I am going to talk to you about programming Web APIs using F# programming language."
image: https://cdn-images-1.medium.com/max/800/1*XpTQJt9MCpEmfaf0RcPImw.png
---

### Build your first Web API with F#, Giraffe and host it on Azure Cloud

![](https://cdn-images-1.medium.com/max/800/1*XpTQJt9MCpEmfaf0RcPImw.png)*Building a Web API using F# and Giraffe, hosting on Azure Cloud*

Today I am going to talk to you about programming Web APIs using F# programming language.

F# has been around for a while now, but what I would like to talk about is F# in .Net Core because it has a lot of cool features specially for Web Programming and building Web APIs and with playing around with it building some Web API, so far I personally think F# is a really great fit for building Web APIs.

#### Options for Web Programming with .Net Core and F#

At the moment there are various options to do web programming with F# and .Net Core. You can do **Giraffe**, **Asp.Net Core MVC**, **Freya**, **Suave or Saturn** and many more frameworks, but for today I will show you how you can use Giraffe to build a Web API with F#.

Some of these frameworks are more low level and some more high level. Some are more functional and some more Object Oriented. If you are interested you can look them up and see what are the differences between them.

#### What is this Giraffe about?

Giraffe in short is **a** **Functional Asp.Net Core,** whereas Asp.Net Core MVC is Object Oriented Asp.Net Core!

It’s also very light weight because it is just a library and not a full framework and because it is not much opinionated, at first it might feel a bit more low level when you are using it, and that is a big deal for a lot of developers to have such low level control over every single detail. And obviously for some other developers, specially people who are used to full opinionated frameworks like Asp.Net Core MVC, Giraffe would be too low level and a bit awkward to get started.

Giraffe uses [***Kleisli composition***](https://typelevel.org/cats/datatypes/kleisli.html) to define API routes. Functional Programming fans know what this is and I don’t need to say no more!

But for the rest of us, what it means is, it uses this little operators that look like arrows, and those arrows conceptually mean, The thing on the left is passed to the thing on the right! so you can actually read code left to right.

Oh, and by the way it is Open Source as well:

[**giraffe-fsharp/Giraffe**  
*Giraffe - A native functional ASP.NET Core web framework for F# developers.*github.com](https://github.com/giraffe-fsharp/Giraffe "https://github.com/giraffe-fsharp/Giraffe")

And of course Giraffe has this really cool logo!

![](https://cdn-images-1.medium.com/max/800/1*i-PaYAfXX2cndwUOl4BjDg.png)

#### Show me some code

First of all, if you don’t have the Giraffe template, the easiest way is to install it from command prompt with the following command:

```
dotnet new -i "giraffe-template::*"
```

![](https://cdn-images-1.medium.com/max/800/1*eLhILo4efO6FFzcriG3lLg.png)

This will pull and install the [giraffe-template NuGet package](https://www.nuget.org/packages/giraffe-template/) in your .NET environment.

Now you can run `dotnet new giraffe -h` command to see all the options with the Giraffe template.

![](https://cdn-images-1.medium.com/max/2560/1*sVduwNPpL51VRq4bmdDWnQ.png)

Right now since we want to build a Web API, I will select the “none” view engine which is API Only template. So we can run the following command to create the project:

```
dotnet new giraffe -lang F# -V none -I true -o firstGiraffe
```

![](https://cdn-images-1.medium.com/max/800/1*wSAYkcKSGOvyTRQCTTlgYw.png)

That’s it. Our first Giraffe project is created. You can navigate to the “src” folder and open the “.fsproj” file open with Visual Studio, or Visual Studio Code! And yes you can use both of these editors in Mac, or Windows!

There are some stuff here in the project that are generated for us.

***Models.fs***

It is basically a type called “Message”, and this type has a thing called “Text” in it.

This is what we want to return as a response to the client.

***Program.fs***

This module is wiring stuff up. It is actually very similar to how Asp.Net Core MVC app sets thing up in start up.

There are some sections in there, like “Exception handler” where your global exception handler lives.

Also there is a section called “Web App” where the routing for the API is going to be and also if you look closely, for each route, it is specified what function should be called.

If you are using Visual Studio, you can select the “handleGetHello” in the “Web App” section and press F12, and it will take you to the definition of this function, which is in the HttpHandler.fs

***HttpHandler.fs***

This module is where the route is going to be handled. At the moment we only have one function in there that is this “handleGetHello”

This function, just builds a response and returns a json version of if with a hard coded text in it.

Now, to tun this Web API, you can use the command prompt and run the following command to run the application

```
dotnet watch run
```

![](https://cdn-images-1.medium.com/max/1200/1*1-3iR8R8bi7SvCGN6q4yaA.png)

As you can see, our API is running on localhost port: 53525. So let’s open a browser and call the hello world API.

![](https://cdn-images-1.medium.com/max/800/1*GUzXBgiYCUT_JuFTD9w_Gw.png)

As you can see the API is working and it is returning the Json file.

### How do I host this API on Azure?

Publishing this F# / Giraffe Web API on Azure is super easy and it is just like any other C# Web API.

If you are using Visual Studio, you can just right click on the Solution and press “Publish” and from there you can just follow the wizard.

![](https://cdn-images-1.medium.com/max/800/1*9wJu44hsRx6UOB3zOUr2bQ.png)

In the first screen, you can select the App Service.

Since this is .Net Core and cross platform, you can select Windows or Linux. And click “Publish” again.

![](https://cdn-images-1.medium.com/max/800/1*3y9-U4Gs7xY_glUgJ9YcMw.png)

On the next screen, enter your Azure Resource Group information and click “Create”. This will take a minute or two to be deployed and once it is done, it will automatically open a browser to your hosted Web API, and then you can try your API like the following:

![](https://cdn-images-1.medium.com/max/800/1*b-MI5WjqhSXTaFf-NgCcug.png)

That’s it. Our first F# Web API is up and running in Azure.

As always, you can find the complete solution in the following github repository:

[**aramkoukia/fsharp-giraffe-sample**  
*GitHub is where people build software. More than 28 million people use GitHub to discover, fork, and contribute to over…*github.com](https://github.com/aramkoukia/fsharp-giraffe-sample "https://github.com/aramkoukia/fsharp-giraffe-sample")

Cheers!
