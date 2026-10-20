---
layout: post
title: "Blazor — SPA framework on .Net via WebAssembly"
date: 2018-07-11
description: "Today we are going to look at a new WebAssembly project called Blazor!"
image: https://cdn-images-1.medium.com/max/2560/1*Lyg6rI-Fs0CdzEHjttc02A.jpeg
medium_url: https://medium.com/@aramkoukia/blazor-spa-framework-on-net-via-webassembly-b7a0046e7f21
---

### Blazor — SPA framework on .Net via WebAssembly

![](https://cdn-images-1.medium.com/max/2560/1*Lyg6rI-Fs0CdzEHjttc02A.jpeg)*Image from: <https://www.youtube.com/watch?v=qDoSAnwNgQI>*

Today we are going to look at a new WebAssembly project called Blazor!

What it let’s you do is to build a website in C#, compile that into WebAssembly and then have the WebAssembly render your page on the website!

What’s the big deal about it? you work with C# only! bye bye JavaScript!

Don’t attack me yet folks, I am a fan of JavaScript myself and I don’t think it is going to go anywhere anytime soon.

*(image from: <https://gph.is/2GLQPhk>)*

### Wait, what’s this WebAssembly thingy?

Here is the definition from <https://webassembly.org/>

> WebAssembly (abbreviated *Wasm*) is a binary instruction format for a stack-based virtual machine. Wasm is designed as a portable target for compilation of high-level languages like C/C++/Rust, enabling deployment on the web for client and server applications.

**Do browsers support this yet?**

Good question, and yes, most major browsers support WASM 1.0 at the moment.

![](https://cdn-images-1.medium.com/max/800/1*XvgxJGQqj9rsmogjF8NhUg.png)*WebAssembly 1.0 has shipped in 4 major browser engines. (That Icon is Edge btw ;))*

### What does WebAssembly mean for Web Platform?

In short, this is HUGE!

![](https://cdn-images-1.medium.com/max/800/1*5sL74EouPVy2IeOpSNXptA.gif)*WebAssembly has “HUGE” implications for the web platform (image from: <https://gph.is/1URUQiq>)*

WebAssembly has huge implications for the web platform

It gives us the possibility to run code of multiple languages on the web, with **Native Speed!**

As of now, WebAssembly is not intending to be a JavaScript competition, and it is designed to be a complement and run side by side with JavaScript using WebAssembly’s API’s that provide access to JavaScript APIs.

### What’s this Blazor framewrok?

Blazor is basically a SPA framework, but not a typical one like Angular or React that uses JavaScript or TypeScript. **This one is built on .Net that runs in the browser!**

![](https://cdn-images-1.medium.com/max/800/1*0J8EiGg4IdfqLEmFgomNXg.gif)*You can now run .Net in the browser! (image from: <https://gph.is/1brOPam>)*

**Wait what? How can you run .Net in the browser?**

It is all done using WebAssembly. Basically we use a .Net runtime that you might have heard of called [**Mono**](http://www.mono-project.com/news/2017/08/09/hello-webassembly/)and compile it to WebAssembly, and then run the compiled binary in the browser**!**

### Show me some code!

Alright enough with the into, now let’s get to it.

To create your first Blazor project you need to install the follwing tools and SDKs:

1. Download and install [.NET Core 2.1 SDK](https://go.microsoft.com/fwlink/?linkid=873092) (get whatever is the latest).
2. Download and install [Visual Studio 2017](https://go.microsoft.com/fwlink/?linkid=873093) (get whatever is the latest version) and make sure you select the web development stuff while going through the installation wizard.
3. Download and install the [Blazor Language Services extension](https://go.microsoft.com/fwlink/?linkid=870389) from the Visual Studio Marketplace.

![](https://cdn-images-1.medium.com/max/800/1*OGa4x4WO101L-myIc1eXLg.png)*ASP.NET Core Blazor Language Services*

After installing all that, you can open Visual Studio and go File > New Project and select Asp.Net Core Web Applicant.

Then in the next dialog you should be able to see “**Blazor**” along with other web projects. So select that one!

![](https://cdn-images-1.medium.com/max/800/1*9BkPiN9xEK8ifw-HGNlwZA.png)*Select “Blazor” as your Web Application project type*

That’s it. this should create your first Blazor WebAssembly project.

If you look at your solution explorer you should see something like the following:

Now can you just press F5 and you should be able to see the project running in your browser like the following:

![](https://cdn-images-1.medium.com/max/800/1*ArlygOttPbfWWjTPhPbqYg.png)*Running the Blazor project in the browser!*

### A quick tour in the code

If you click around in this basic scaffolding project, you will see that it does a couple of basic things.

It has a Counter page that simply just adds to a counter value and displays it and the other page is rendering a grid on the page. Now let’s look at what is on the Counter page.

#### The Counter page:

If you open the Counter page, you will see how this project is doing the same thing JavaScript used to do with C#:

The front end for this Counter component is just regular Html stuff.

Also the logic is added using the good old Razor syntax. All this Html and the C# stuff is converted into a component class when we build the project.

When we build the project, the name of the generated .Net class with be the same as the name of the **.cshtml** file.

All the members of this “Counter” component class are in the `@functions`block, component state (properties, fields) and methods can be specified for event handling or for defining other component logic.

### How does Routing Work?

If you look at the top of the “Counter.cshtml” you can see the `@page` directive that specifies that this component is a page to which requests can be routed.

That means any requests that are sent to “/Counter” will be handled by this “Counter” component . If you don’t have this “page” directive at the top of the component, that component will not handle any requests at all on its own but that component can be used by other components as a sub component.

A good example for components without routes would be the components under the “shared” folder in this project.

### How do I add a new component?

It is super easy…

Under the pages folder, create a new .cshtml file and add the route you like at the top of the page like the following:

This means that our route for the new component is “/test”

Then under the “shared” folder, just open the NavMenu.cshtml to add a new menu item for this new component like the following:

That’s it! now if you press Ctrl + F5, you should be able to see the new Menu and navigate to the new component you created:

![](https://cdn-images-1.medium.com/max/800/1*wKCx6K9Q48BN27e-7sdaAw.png)*Adding a new Component in Blazor*

### How do I deploy this Application?

Deployment for this application is not any different than any regular Asp.Net Core application.

Just right click on the project, select “Publish” and follow the wizard to deploy your application to Azure.

![](https://cdn-images-1.medium.com/max/800/1*E5HhUe_cjzGq0TDBkrafqg.png)*Deploying Blazor WebAssembly application to Azure*

And there we have our first Blazor WebAssembly project built and deployed to Azure.

#### Project Source Code:

You can find the source code of this project on the following github repository if you want to clone and play around:

[**aramkoukia/blazor-webassembly-sample**  
*Contribute to blazor-webassembly-sample development by creating an account on GitHub.*github.com](https://github.com/aramkoukia/blazor-webassembly-sample "https://github.com/aramkoukia/blazor-webassembly-sample")

Originally I published this at:

[**Blazor-SPA Framework on .NET | Getting Started with Building Blazor WebAssembly Projects**  
*Blazor is a typical .NET web framework that runs in the browser with WebAssembly. Learn how to build a Blazor…*www.zeolearn.com](https://www.zeolearn.com/magazine/blazor-building-a-faster-web-application-using-webassembly "https://www.zeolearn.com/magazine/blazor-building-a-faster-web-application-using-webassembly")

Cheers!
