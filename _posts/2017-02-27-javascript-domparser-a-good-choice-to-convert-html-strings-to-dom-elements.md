---
layout: post
title: "JavaScript DOMParser, a good choice to convert HTML strings to DOM Elements"
date: 2017-02-27
description: "If you have done some web development, you probably have been in a situation where, you had some HTML content stored in some string…"
image: https://cdn-images-1.medium.com/max/800/1*jUIMvD4K-TSK5BbQQ9ZPkw.jpeg
tags: ["JavaScript"]
---

### JavaScript DOMParser, a good choice to convert HTML strings to DOM Elements

![](https://cdn-images-1.medium.com/max/800/1*jUIMvD4K-TSK5BbQQ9ZPkw.jpeg)

If you have done some web development, you probably have been in a situation where, you had some HTML content stored in some string (Probably coming from a database table or even hard coded in the <script> tag) and then shortly after you realized you need to do some processing on that HTML content, like add some text to it, wire up some events to some elements in there or read some of the content of that HTML, etc.

So next step is to convert that “HTML string” into proper DOM elements to be able to traverse through the nodes and do your thing.

Using jQuery you could do something like the following to return the nodes, but then obviously you need to reference jQuery in the page.

Though some might argue that having jQuery is fine in any web page, and the code below is nice enough.

```
$('<div>Boom!</div>')
```

But now seems to be a good time in almost all browsers if you want to convert a string into DOM elements with just JavaScript code and no extra libraries.

### Meet the DOMParser

Yeah, DOMParser class is your guy. All you need to do is to create a new instance of this class and call the `parseFromString`

As you can see, this returns a ‘document’, and you can use standard JavaScript methods to traverse nodes in it, like displayed in the above snippet.

### Bugs/Known Issues

Currently, there is an issue in Firefox, when you pass in an invalid HTML string, it does not throw an exception and instead it returns an “Error Document” which you can probably parse its elements and find out that there has been an error in parsing your string.

**Bug:** <https://bugzilla.mozilla.org/show_bug.cgi?id=45566>

### Parsing an SVG

You can also use `DOMParser` to parse a SVG document . All you need to do is to set the MIME type to be `image/svg+xml`, and the returned type will be `SVGDocument`.

How cool is that?

### Browser Compatibility

The following table is the compatibility table of this class as of today for desktop browsers:

![](https://cdn-images-1.medium.com/max/800/1*TEmcCLwtCWxIAJBmiofOxA.png)

I find DOMParser a good alternative to all other complicated stuff I used to user before (jQuery was the best one, but trying to get away from it as browsers are getting more and more mature!)

So it’s time to dig into the code and do some refactoring!
