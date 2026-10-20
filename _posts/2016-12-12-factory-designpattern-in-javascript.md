---
layout: post
title: "Factory #DesignPattern in #JavaScript"
date: 2016-12-12
description: "Factory is a popular design pattern that we use a lot for creating objects. In Factory pattern, we create object without exposing the…"
image: /assets/img/2016-12-12-factory-designpattern-in-javascript/1.gif
medium_url: https://medium.com/@aramkoukia/factory-designpattern-in-javascript-2a1ec45ff461
---

### Factory #DesignPattern in #JavaScript

F[actory](https://en.wikipedia.org/wiki/Factory_%28object-oriented_programming%29) is a popular design pattern that we use a lot for creating objects. In Factory pattern, we create object without exposing the creation logic to the client and refer to newly created object using a common interface.

Using this pattern, to create a new object we use a factory function. **A factory function is simply a function that returns an object.**

You don’t need to use the `new` keyword when using factory methods, but it still can be used just like a [constructor](https://en.wikipedia.org/wiki/Constructor_%28object-oriented_programming%29).

The following is a simple implementation of a factory function which takes in some arguments and uses them to instantiate a new object:

```
function userFactory(name) {    return {        name: name,        login: function () {            console.log('user ' + name + ' logged in.');        },    };}
```

And this is how you can use this factory method to create a new *user* object and call a public method from *user* object*:*

```
var user = userFactory('Aram');  // create a user named Aramuser.login();  // "user Aram logged in."
```

When you want to make some of your [properties or methods private](https://en.wikipedia.org/wiki/Private_class_data_pattern), you can simply just take them out of the returned object. This keeps your implementation details encapsulated, and it will only expose the public interface to your object.

```
function userFactory(name) {    function completeName() {        return 'Mr or Mrs ' + name;    }    return {        name: name,        login: function () {             console.log('user ' + completeName() + ' logged in.');        },    };}
```

Cool, Eh?

![](/assets/img/2016-12-12-factory-designpattern-in-javascript/1.gif)

And similarly, following snippet is how you use this factory method:

```
var user = userFactory('Aram');  // create a user named Aramuser.login();  // "user Mr or Mrs Aram logged in."user.completeName()  // ERROR: user.completeName is not a function
```

Also if you are interested to practice [Functional Programming](https://en.wikipedia.org/wiki/Functional_programming) in JavaScript, the Factory pattern will be your friend for that purpose.

**Found this post useful? Kindly tap the ❤ button below! :)**
