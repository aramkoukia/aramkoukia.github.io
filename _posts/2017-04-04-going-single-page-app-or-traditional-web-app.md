---
layout: post
title: "Going Single Page App or Traditional Web App"
date: 2017-04-04
description: "With all the trending front-end frameworks being discussed these days, like Angular, ReactJs, VueJs, EmberJs, which most of them make our…"
image: https://cdn-images-1.medium.com/max/800/1*DZ1fC82UQ9wVxYqaxwUvWA.jpeg
medium_url: https://medium.com/@aramkoukia/going-single-page-app-or-traditional-web-app-cedb10041b50
---

### Going Single Page App or Traditional Web App

![](https://cdn-images-1.medium.com/max/800/1*DZ1fC82UQ9wVxYqaxwUvWA.jpeg)

With all the trending front-end frameworks being discussed these days, like Angular, ReactJs, VueJs, EmberJs, which most of them make our life easier to make Single Page Application, seems like the bigger question of, “Should we even build our web app, a SPA or not” is being ignored

I believe it is important to understand that traditional web application approach might be still a better approach in some cases, so I decided to write about these two approaches and their use-cases.

Today, there are two general approaches when you build a web applications: traditional web apps, that means we do most of the logic on the server side, and single page applications (SPAs) that most of the UI code is in the browser and we make some API calls for CRUD operations.

Here are the summary of each approach and use cases for each one as a quick reference:

### Traditional web applications use cases

- Our web application is supposed to run on browsers that does not support JavaSctipt! (This is very important)
- Our web application is very simple and is mostly read only stuff.
- Resources (Developers) in our team aren’t familiar with JavaScript or TypeScript or Front-end development.

![](https://cdn-images-1.medium.com/max/800/1*hsXIPyBqqI7ZTh2QyLfizw.gif)

### Single Page Application use cases

- Our UI is rich in features and has complicated logic.   
  SPAs can load more quickly, fetching data in the background, and individual user actions are more responsive since full page reloads are rare.   
  SPAs can support incremental updates, saving partially completed forms or documents without the user having to click a button to submit a form.   
  SPAs can support rich client-side behaviors, such as drag-and-drop, much more readily than traditional applications.
- You already need a Web API to be exposed to be used by other applications or other Interfaces (like Alexa, Phone Apps, Chat Bots, etc.).   
  If you’re already building a web API for other clients to use, it will definitely be less effort to create a SPA application since you will have all the back-end requirements already.
- Our Peeps should be Familiar with JavaScript/TypeScript. Writing SPAs requires familiarity with JavaScript and/or TypeScript and font-end programming skills.   
  Our peeps should be confident in writing modern JavaScript using a SPA framework like Angular or ReactJs.

### Traditional Web Application or Single Page Application

To sum up, here is a decision matrix to help you decide which way to go:

![](https://cdn-images-1.medium.com/max/800/1*IyQQ8FQ74NVefoDe5-ysCA.png)

Cheers!
