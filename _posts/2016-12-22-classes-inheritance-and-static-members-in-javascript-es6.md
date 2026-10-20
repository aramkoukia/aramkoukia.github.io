---
layout: post
title: "Classes, Inheritance and Static members in #JavaScript #ES6"
date: 2016-12-22
description: "Class definition syntax and Class Constructor"
image: /assets/img/2016-12-22-classes-inheritance-and-static-members-in-javascript-es6/1.jpg
---

### Classes, Inheritance and Static members in #JavaScript #ES6

![](/assets/img/2016-12-22-classes-inheritance-and-static-members-in-javascript-es6/1.jpg)

### Class definition syntax and Class Constructor

So first things first; The constructor, which sets up each instance’s initial state and handles any parameters that were passed when calling `new`.

Just like other object oriented languages Constructor is defined in a `class` block and is `constructor`, though it's actually handled as a special case.

Note is that a class constructor cannot be made static in JavaScript via the `static` keyword, but you can make class members as static using the keyword.

### Class Inheritance in JavaScript

Inheritance is also very similar to other object-oriented languages:

methods defined on the base are accessible in the child class.

If the child class declares its own constructor then it must invoke the parents constructor via `super()` before it can access `this`.

### Static Methods in JavaScript

Static methods and properties are defined on *the class/constructor itself*, not on instance objects. These are specified in a class definition by using the `static` keyword.

### Repeat after me…

- Support for “class” was only added to JavaScript as part of the [2015 ES6](http://es6-features.org) standard.
- JavaScript classes are just wrappers around JavaScript’s already existing [prototype-based inheritance](http://www.w3schools.com/js/js_object_prototypes.asp).
- This new syntax is not a new implementation in JavaScript that handles inheritance in JavaScript, and it is just a simpler syntax to do the same thing that we used to do with prototypes.

![](/assets/img/2016-12-22-classes-inheritance-and-static-members-in-javascript-es6/2.gif)
