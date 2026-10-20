---
layout: post
title: "Web Components Should Work Everywhere!"
date: 2018-11-05
description: "I have been looking into ways to build more abstract Web Component for our project where I work and it has been an amazing journey so far."
image: https://cdn-images-1.medium.com/max/800/1*aIuPqDswFqVT0hMs3lzCNA.png
medium_url: https://medium.com/@aramkoukia/web-components-should-work-everywhere-545f52acd0fb
---

### Web Components Should Work Everywhere!

![](https://cdn-images-1.medium.com/max/800/1*aIuPqDswFqVT0hMs3lzCNA.png)*Image from <https://www.carlrippon.com/are-web-components-finally-a-thing/>*

I have been looking into ways to build more abstract Web Component for our project where I work and it has been an amazing journey so far.

From a very high level and the concepts of Web Components, it seems like: **Custom Elements work in all JavaScript Frameworks and All of our problems are solved!**

What you see from all the documentation and people who have built full applications using Web Component, this is what’s pretty much most experienced folks in the Web Component area believe:

> Custom Elements, **should** work everywhere!

So, why don’t they?

It looks like a lot of it goes back to how we implement our Custom Elements and how “**good”** our Custom Element is!

#### What is a “good” Custom Element?

The best place I have found to look when building Custom Elements is a set of components called “How-To” Components, implemented by Google.

#### **What are** HowTo-Components:

HowTo-Components are a set of elements which demonstrate Custom Element and Shadow DOM best practices. These elements are not intended to be used in production, but are instead presented as a teaching aide to help map best practice suggestions to actual implementations.

Examples are meant to be read, interpreted and ported to your own elements.

You can check out the source code for these on Github:

[**GoogleChromeLabs/howto-components**  
*Literate code examples for common UI patterns. Contribute to GoogleChromeLabs/howto-components development by creating…*github.com](https://github.com/GoogleChromeLabs/howto-components "https://github.com/GoogleChromeLabs/howto-components")

#### Custom Element Best Practices:

To help us create the best possible experiences, Google devs have put together this checklist which breaks down all the things we think it takes to be a well behaved custom element.

You can find the check list from the following Google Developers page:

[**Custom Element Best Practices | Web Fundamentals | Google Developers**  
*Custom elements let you construct your own HTML tags. This checklist covers best practices to help you build high…*developers.google.com](https://developers.google.com/web/fundamentals/web-components/best-practices "https://developers.google.com/web/fundamentals/web-components/best-practices")

Now that we built a “good” Web Component, how should **frameworks act?**

#### Does my Web Component work in Frameworks?

If you want to know how well Web Components work in a particular JavaScript framework, you can check out the [custom-elements-everywhere.com](https://custom-elements-everywhere.com/) website:

[**Custom Elements Everywhere**  
*Making sure frameworks and custom elements can be BFFs 🍻*custom-elements-everywhere.com](https://custom-elements-everywhere.com/ "https://custom-elements-everywhere.com/")

Every framework on this website has a little section, and in that section, it indicates how many tests are passing or failing and check out the details of the failed tests so you can have a more real expectation.

I hope this helps you to write more standard and consistent Web Component that work in all major JavaScript Frameworks.

Cheers!
