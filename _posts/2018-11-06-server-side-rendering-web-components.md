---
layout: post
title: "Server Side Rendering Web Components"
date: 2018-11-06
description: "In this article I want to talk about Server Side Rendering Web Component. But for those of you who aren’t sure what is Server Side…"
image: https://cdn-images-1.medium.com/max/800/1*YyJH5w2rOU3SWngmXDug5A.jpeg
---

### Server Side Rendering Web Components

![](https://cdn-images-1.medium.com/max/800/1*YyJH5w2rOU3SWngmXDug5A.jpeg)

In this article I want to talk about Server Side Rendering Web Component. But for those of you who aren’t sure what is Server Side Rendering and why one would consider using it, let’s get some background information out of the way first:

### What is Server Side Rendering (SSR)?

In a high level, you are doing Server Side Rendering (SSR) if your web server delivers meaningful, render-able and route-specific Html to browsers or other user agents.

So for example for a given Url like this: *https://koukia.ca/happiest-countries*

If your server send something like the following to the browser, then you are doing SSR.

![](https://cdn-images-1.medium.com/max/800/1*66WSqRvhpQPguIri1QXl1Q.png)*This is SSR*

On the other hand, if you are only sending an empty Html shell like the following, then that is not SSR:

![](https://cdn-images-1.medium.com/max/800/1*OypRRCJXhkzGk_MwfhJrRA.png)*This is not SSR*

So this may seem so high level, but hang in there and you’ll get more details soon.

### Why would I want to use Server Side Rendering (SSR)?

Turns our there are two major reasons.

#### 1. Search and Share

The single biggest reason is to maximize your reach. To have any kind of impact, your app of course needs to have users, and the best way to reach users today are search and link sharing, both of which rely on non-browser user agents called “bots”.

“Search bots” crawl the web and populate search indexes, while “Link bots” visit Urls and produce appealing visual snippet to encourage sharing.

Sadly, many of these bots, don’t run your client-side code. If you don’t serve any meaningful Html, your site might as well be invisible.

This might sound weird but the truth is, this is the status of the web right now!

#### 2. Performance

The second reason to use SSR, is to maximize loading performance. We all know that performance is a critical component of user experience, and in particular, in the Mobile era, loading is almost certainly the most important aspect of performance.

The performance-based argument for SSR is pretty simple. Serving render-able Html is generally the fastest way to get something on screen, since the browser can paint right away, before loading, parsing or executing any of your JavaScript.

### Do I need Server Side Rendering (SSR) for Search and Sharing?

I think this might be a case by case basis and depends on the nature of your site and your business. But I am just going to say, Most likely, Yes!

Let’s note one exception first though. If you don’t heavily on sharing and you are satisfied with the reach that Google search gives you, you may not need SSR. That’s because Google Bot, uses a rendering service used on Chrome, therefore sees your site very much like your users do. With the caveat that, the Google Bot version on Chrome should be up to date.

If you like more detail information about this checkout the following links:

[**Understand rendering on Google Search | Search | Google Developers**  
*Googlebot is designed to be a good citizen of the web. Crawling is its main priority, while making sure it doesn't…*developers.google.com](https://developers.google.com/search/docs/guides/rendering "https://developers.google.com/search/docs/guides/rendering")

[**Debug Rendering Problems | Search | Google Developers**  
*window.addEventListener('error', function(e) { var errorText = [ e.message, 'URL: ' + e.filename, 'Line: ' + e.lineno +…*developers.google.com](https://developers.google.com/search/docs/guides/debug-rendering "https://developers.google.com/search/docs/guides/debug-rendering")

But the problem is, Google Bot is not at all typical and many bots don’t try to run your browser code at all, and many that do, do so in very limited ways.

So if you care about non-google search sharing, you probably want to use some sort of SSR.

### Do I need Server Side Rendering (SSR) for loading Performance?

My answer to this one might piss some off, but I’ll just say it: No!

Using patterns like [PRPL](https://developers.google.com/web/fundamentals/performance/prpl-pattern/) you can deliver a great loading experience without SSR.

> PRPL is a pattern for structuring and serving Progressive Web Apps (PWAs), with an emphasis on the performance of app delivery and launch.

But while it is nice to know that you can build a fast loading site without SSR, what’s more important is actually the converse, that is using SSR by no means guarantees that your loading performance is going to be good or even adequate.

The bottom line is, SSR should not be considered as a magic bullet for loading performance.

But can SSR help in loading performance? **Absolutely (might)**

Now we can talk about Server Side Rendering and Web Component specifically.

### How do I use Server Side Rendering with Web Components?

If you have looked around on internet, you see a lot of confusion around Web Components and SSR, and some people think that these are not compatible which isn’t true. Web Components are completely compatible with SSR.

Let’s see how, starting with a common pattern that works with any sort of server side rendering:

#### Components for UI and Presentation

Specifically, UI components and widgets can be used in any Server Side Rendering Scheme.

The same goes for the class of component called “Presentation Components”. These are components you build yourself for different purposes like Presentation or Navigation. Each component has its own semantics and encapsulates styling and behavior to ensure consistency across your site.

This works great.

**But what if you don’t have an SSR solution to lean on or your entire app is based on Web Components?**

In this case you need something more! Let’s look at two possibilities:

**Option 1:** Delegate bot rendering to a standalone service.

**Option 2:** [Isomorphic JavaScript](https://en.wikipedia.org/wiki/Isomorphic_JavaScript).

Each option mentioned have their pros and cons which I am not going to go through them right now and that’s something you can research on your own.

Cheers!
