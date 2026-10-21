---
layout: post
title: "How to remove a property from a JavaScript object?"
date: 2020-02-22
description: "There are times that you have a javascript object and you want to delete some properties from it."
image: https://cdn-images-1.medium.com/max/800/0*jHFeHYcdYz1GrhU5.png
tags: ["JavaScript"]
---

### How to remove a property from a JavaScript object?

![](https://cdn-images-1.medium.com/max/800/0*jHFeHYcdYz1GrhU5.png)*Image from <https://flaviocopes.com/>*

There are times that you have a javascript object and you want to delete some properties from it.

> A JavaScript object is essentially a hashtable of name-value pairs where the names (i.e., keys) are strings. And they are *always* strings.

> Source: <https://www.toptal.com/javascript#hiring-guide>

One common use case that I have seen is in Unit Testing, when you create a full object as your “mock” data that is your complete object, but in your tests you want to verify the behavior if some of the properties were missing.

For that, instead of creating multiple objects that would cover different test cases, you could define one object and in each test case delete the properties you want to be removed, then use that object in the test.

Imagine you create an object like the following:

```
let user = {    "firstName": "Aram",    "lastName": "Koukia",    "website": "https://koukia.ca"};
```

And you want to delete the “website” property from this object to have:

```
let user = {    "firstName": "Aram",    "lastName": "Koukia"};
```

To do that you can use this command:

```
delete user.website;
```

or

```
delete user['website'];
```

or

```
var prop = "website";delete user[prop];
```

Any of the above commands will remove the property from the object!

If you use JavaScript regularly, I recommend to get this book and have it on your desk:

### [JavaScript: The Good Parts](http://amzn.to/2onH2Dz)

![](https://cdn-images-1.medium.com/max/800/1*cyXcEKLILYozIuZu0QRuMw.jpeg)*JavaScript: The Good Parts*

Get it now:

[**JavaScript: The Good Parts**  
*Edit description*amzn.to](http://amzn.to/2onH2Dz "http://amzn.to/2onH2Dz")

> If you liked this article, click the👏 below so other people will see it here on Medium.

> Let’s be friends on [Twitter](https://twitter.com/aramkoukia). Happy Coding :)

Cheers!
