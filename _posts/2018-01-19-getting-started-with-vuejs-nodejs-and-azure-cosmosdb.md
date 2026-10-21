---
layout: post
title: "Getting started with VueJs, NodeJs and Azure CosmosDB"
date: 2018-01-19
description: "Looking at the Frontend frameworks that showed up in the past few years, it seems like we are down to very few main frameworks that people…"
image: https://cdn-images-1.medium.com/max/1200/1*HZv3XwUmdOuvl-qydTGReQ.png
tags: ["JavaScript", "Azure", "Data"]
---

### Getting started with VueJs, NodeJs and Azure CosmosDB

![](https://cdn-images-1.medium.com/max/1200/1*HZv3XwUmdOuvl-qydTGReQ.png)

Looking at the Frontend frameworks that showed up in the past few years, it seems like we are down to very few main frameworks that people are talking about.

I believe, for the enterprise solutions, it seems like the battle is between [Angular](http://angular.io) and [React](https://reactjs.org/). Of course there are other ones out there that have their community and market (like EmberJs, or BackboneJs, etc), but I wanted to try out [VueJs](https://vuejs.org/) that I see here and there and it seems like it is getting a lot of attention.

### **Vue.js on Google trends**

Take a look at google trends comparing Angular, React, Vue in the following picture:

![](https://cdn-images-1.medium.com/max/1200/1*0aGb63qDDdLKyRwhk-gNOw.png)

Though, this is not a particularly accurate or scientific metric to see what’s going on in the front-end community, but it is still nice to see that searches for “vuejs” and “reactjs” are very close.

### Vue.js on Stakoverflow

I also looked at the community around Vue.js on [Stackoverflow](https://stackoverflow.com/questions/tagged/vue.js?mixed=1), and comparing it to React (considering all the marketting effort coming from Facebook, etc, and the age of React compared to Vue) I find it really impressive!

Less than 10% of all the questions are unanswered, which means, there are tons of people out there helping you if you are stuck.

**vue.js tag on Stackoverflow:**

![](https://cdn-images-1.medium.com/max/800/1*hbm-6fAVjV8CWlG0NxH7jA.png)

**reactjs tag on Stackoverflow:**

![](https://cdn-images-1.medium.com/max/800/1*m0Am04AxtI00eIOkGCOZCA.png)

### What is Vue?

Vue, is an Approachable (All you need to know is Html, Css and JavaScript), Versatile (You don’t need to adopt to it in a big-bang. you can start using it incrementally) and High Performance **(20KB min+gzip Runtime)** JavaScript framework, that helps you create more maintainable and testable code base.

![](https://cdn-images-1.medium.com/max/800/1*vYKA-nnA_hvBZil2TTq37g.jpeg)

> Vue.js is a Progressive Framework!

**What do you mean by: “Vue.js is a Progressive Framework”?**

That means, if you have an existing application, that uses any other front-end framework like Angular or React, you can still introduce Vue to your application, and use it in just part of your application, without the need to rewrite the whole thing using Vue. So it is very suitable for “brown field” projects.

**What if I have a green field project?**

Vue is useful for “green field” projects as well. It has the Core libraries you will need to build a full enterprise application (Vue Core, VueX, Vue-Router etc).

Similar to other JavaScript frameworks, you can split up your application/page into components, and each component will have its own JS, CSS and Html for render that part of the page/application, which will be critical when building large scale application in medium to large development teams.

### Browser Support

The following is the list of supported browsers by Vue.js as of today:

![](https://cdn-images-1.medium.com/max/800/1*CfGDOascOV_UbjppwjHJpA.png)

As you can see, Vue supports almost all descent browsers (Sorry ie 6 users!)

### “Hello World” using Vue

One of the main “pros” of Vuejs that everyone is so impressed with (though some suggest it reminds them of early Angularjs days or even knockout but I’m not sure if I agree with them) is the simplicity of booting up a new application.

Compared to other famous frameworks (Specially Angular) that need a lot of plumbing work to get going (though with Angular CLI things are much smoother now), Vue will boot up with minimum effort.

So let’s jump in.

First, we just create a simple html and reference the Vuejs library from a public CDN.

Now, lets add our App.js file and populate the {{ message }} to be displayed on the page:

That’s it! now if you open the html you should see a page with the message displayed in it:

![](https://cdn-images-1.medium.com/max/800/1*jJzM5XcDmldq6OLEaJrlDg.png)

Though Vue has also support for some CLI, but as you can see it is not really needed for booting up an app, since the effort is very little.

### Let’s build something real

Now that we have this not so impressive “hello world” app running, let’s get our hands dirty and build something real!

#### **What are we building?**

We are building a simple client application using Vue.js, which calls back a Node.js (including Express.js) REST Api. And out Node server, will use Azure CosmosDB APIs, to Save and Retrieve data from a MongoDB database.

So instead of the famous [MEAN s](https://en.wikipedia.org/wiki/MEAN_%28software_bundle%29)tack (MongoDb, ExpressJs, Angular and Node), we will build a simple CRUD web application using “**MEVN**” stack (**don’t look that up, I just came up with it!**)

I know, sounds a bit too much but if you follow me closely, you will see that it is not that complex.

If you don’t know much about Nodejs, Expressjs, or Azure CosmosDB, don’t worry about it. I will explain things as we face them.

Wondering what is Azure CosmosDB all about? keep reading…

#### What is Azure CosmosDB?

When Microsoft introduced [Azure DocumentDB](https://koukia.ca/microsoft-and-nosql-data-store-for-your-modern-cloud-application-e57885b18a5f), it was just a Document database, and Microsoft’s NoSQL Solution in the cloud.

Now recently, DocumentDB was moved to Azure’s new service: “[Cosmos DB](https://docs.microsoft.com/en-us/azure/documentdb/documentdb-introduction)”

> Azure Cosmos DB is Microsoft’s globally distributed, multi-model database. With the click of a button, Azure Cosmos DB enables you to elastically and independently scale throughput and storage across any number of Azure’s geographic regions.

**Supported Data Models and APIs**

The following list is the data models that CosmosDB support at the moment (more to come):

[SQL API](https://docs.microsoft.com/en-us/azure/cosmos-db/sql-api-introduction) , [MongoDB API](https://docs.microsoft.com/en-us/azure/cosmos-db/mongodb-introduction) , [Cassandra API](https://docs.microsoft.com/en-us/azure/cosmos-db/cassandra-introduction), [Graph (Gremlin) API](https://docs.microsoft.com/en-us/azure/cosmos-db/graph-introduction) and [Table API](https://docs.microsoft.com/en-us/azure/cosmos-db/table-introduction)

### Why would I use CosmosDB, rather than a relational database or other NoSQL Databases?

Azure CosmosDB gives you the best of the both world of relational database and non-relational databases.

As a high level the following table will give you an idea that what CosmosDB will give you that others don’t:

![](https://cdn-images-1.medium.com/max/1200/1*Cdu6RFCY5Y0ehprGcipefg.png)

Read up all the documentation around it from the following link if you are interested:

[**Azure Cosmos DB Documentation - Tutorials, API Reference**  
*Learn how to use Azure Cosmos DB to build globally distributed multi-model databases. Tutorials show you how to build…*docs.microsoft.com](https://docs.microsoft.com/en-us/azure/cosmos-db/ "https://docs.microsoft.com/en-us/azure/cosmos-db/")

#### Prerequisites:

First of all you need to install Node.js with npm if you don’t have it installed already.

Nodejs download: <https://nodejs.org/en/download/>

Then we will install all the packages that we need as we move forward.

You will also need an Azure Subscription with some credit to create your CosmosDB there. If you don’t have an account, you can use the following link to get one with 200$ Azure Credit:

[**Create your Azure free account today | Microsoft Azure**  
*Start free with $200 in credit. Create your free account today with Microsoft Azure.*azure.microsoft.com](https://azure.microsoft.com/en-ca/free/?&WT.srch=1&wt.mc_id=AID631261_SEM_MnaZhNFw "https://azure.microsoft.com/en-ca/free/?&WT.srch=1&wt.mc_id=AID631261_SEM_MnaZhNFw")

### Startup code

So to get started, we define our root html and JavaScript in the following index.html file:

Note: the “server/www/build.js” file referenced above is not something we write ourselves. We are using webpack to bundle our code, and that build.js is the name of the file we have specified in our webpack config.

You can find the webpack.config.js file in the github repo mentioned at the end of this post.

And the following is the index.js file which will start our Node application:

That’s all we need for our root folder.

### Client Code

For our client code, we have 2 main parts (except for the bootstrap part where we initialize our Vue application).

**Services**

These are typically the classes where we connect to our API (in this case our Express REST APIs) and do our CRUD operations.

Here is what the service class looks like to do Create, Delete, Get and Update operations:

The other classes that are needed are simple POCO classes, and the actual Vue components:

And here is how the “TodoList.vue” component code will looks like:

For now, for simplicity I have put the JavaScript and the Html in the same file, but if I had to do it again, I would separate them.

### **Server Code:**

On the server side, we have a bunch of stuff.

First is the routes.js which is the entry point to our API, that looks like the following:

Then we have the main piece of code which is our todoService (referenced above in the routes.js), where the actual call to our Azure CosmosDB (in this case MongoDB) is happening:

And then we have the JavaScript class that defines our “todo” schema and collection configuration in our MongoDB, like below (todo.model.js):

And finally, there is the configuration file to connect to our MongoDB database through the Azure CosmosDB API (mongo.js):

That’s all you need!

Now you can run “npm install” to install all your missing packages, and then “npm run build” to run the application.

```
# build for production with minificationnpm run build# serve on http://localhost:8080# and run the api on http://localhost:3001npm run debug
```

Note: you can get the package.json file you need for this from the github repository available below.

In case you didn’t follow all the steps, you can find the complete solution on the following github repository:

[**aramkoukia/mongodb-express-view-node-cosmosdb**  
*Contribute to mongodb-express-view-node-cosmosdb development by creating an account on GitHub.*github.com](https://github.com/aramkoukia/mongodb-express-view-node-cosmosdb "https://github.com/aramkoukia/mongodb-express-view-node-cosmosdb")

\*\* Originally published at: <https://www.zeolearn.com/magazine/getting-started-with-vuejs-nodejs-and-azure-cosmosdb> \*\*

Cheers!
