---
layout: post
title: "Factory #DesignPattern with #Composition in #JavaScript"
date: 2016-12-18
description: "In object oriented programming, happens a lot when you want an object to have some behavior, and first thing that comes to mind is to find…"
image: /assets/img/2016-12-18-factory-designpattern-with-composition-in-javascript/1.png
medium_url: https://medium.com/@aramkoukia/factory-designpattern-with-composition-70a82ad850e
---

### Factory #DesignPattern with #Composition in #JavaScript

![](/assets/img/2016-12-18-factory-designpattern-with-composition-in-javascript/1.png)

In object oriented programming, happens a lot when you want an object to have some behavior, and first thing that comes to mind is to find another class that implements that behavior, and let the new object inherit from the one that has that behavior.

However, common behavior can be provided to the new object through interfaces and a behavioral composite. So you can avoid inheritance to stop giving the behaviors to the objects that you don’t need.

The following code snippet implements the Behavior Factories. Then you can assign these behaviors to the objects you define.

Following code snippet shows you how to implement Object factories and assign behaviors to objects without inheritance:

The following code snippet demonstrates how you use the objects defined above:

Using *Composition instead of Inheritance* is a popular pattern, used to assign behaviors to objects, to avoid unnecessary inheritance that could cause inheriting behaviors that are not needed.
