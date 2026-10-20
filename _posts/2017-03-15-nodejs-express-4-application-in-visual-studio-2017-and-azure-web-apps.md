---
layout: post
title: "Node.Js Express 4 Application in Visual Studio 2017 and Azure Web Apps"
date: 2017-03-15
description: "I’ve been playing with Node.js for one of our clients and this happened to be at the same time with Visual Studio 2017 release, so I though…"
image: https://cdn-images-1.medium.com/max/1200/1*-Nq1fQSPq9aeoWxn4WFbhg.png
---

### Node.Js Express 4 Application in Visual Studio 2017 and Azure Web Apps

![](https://cdn-images-1.medium.com/max/1200/1*-Nq1fQSPq9aeoWxn4WFbhg.png)

I’ve been playing with Node.js for one of our clients and this happened to be at the same time with Visual Studio 2017 release, so I though I’d give it a try with the new Visual Studio see what are my options there.

So to start with looks like there are few templates in Visual Studio to build Node.js apps, with both TypeScript or JavaScript options.

You also have the choice of making it an Azure Node.js web app (which is what I’m interested in) or a normal Node.js web app.

Also you have the option to include Express package to it or not, which I will go with Express package for this demo.

About hosting in Azure, the application will be hosted in a normal Azure Web App, and will use [***iisnode***](https://github.com/tjanczuk/iisnode) for processing the requests.

The following picture shows are all the options you got for Node.js apps and I pick the one that says: “Basic Azure Node.js Express 4 Application (TypeScript)”

![](https://cdn-images-1.medium.com/max/800/1*IPi-avlLMf7cL8RPVwwkLA.png)*Node.js project templates in Visual Studio 2017*

That’s basically it, now you can just press F5, just like any .Net application, and it will run the app in the browser for you with all the break point, debugging features, etc.

![](https://cdn-images-1.medium.com/max/800/1*ubfPWSiFr6KPNcMQV4qWjQ.png)

Now, here comes the hard part, to deploy this to Azure.

Nah, jokes, jokes, that’s the easiest part. Just right click on the project and click on “Publish”.

![](https://cdn-images-1.medium.com/max/800/1*jUJe1-M2HkzEX7LmYL0Ppw.png)

And follow the standard stuff that you do for Publishing a normal .Net Web Application or Web Service to Azure, like selecting your Azure Subscription, Service Plan, App name etc, and click “Publish”.

![](https://cdn-images-1.medium.com/max/800/1*l1YzHFjQ5i_YW2K-WL6d1w.png)

This will compile your TypeScript file, and get all the js files needed from your node\_modules and publish them all to your Azure Web App for you.

And here is our Node.js app running on Azure:

![](https://cdn-images-1.medium.com/max/800/1*5XQZ3H-6nXD-bU_8GDnlmQ.png)

Cheers!
