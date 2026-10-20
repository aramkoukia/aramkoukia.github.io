---
layout: post
title: "Setting the browser page Title in an Angular app"
date: 2017-03-21
description: "Single page applications are great, but search engines aren’t a big fan of them, when it comes to indexing and etc. because the page title…"
image: https://cdn-images-1.medium.com/max/1200/1*O3bdH0eYgK2c7nqgrgggsw.png
---

### Setting the browser page Title in an Angular app

![](https://cdn-images-1.medium.com/max/1200/1*O3bdH0eYgK2c7nqgrgggsw.png)

Single page applications are great, but search engines aren’t a big fan of them, when it comes to indexing and etc. because the page title and the URL are not set properly, and people just use “ResourceId” which is normally a number or a Guid, and that doesn’t help search engines to index the deep pages in a single page application.

There are 2 basic things that needs to be done to begin with: 1. Set the url (uisng Url Rewrite or other techniques). 2. Set the page title to something meaningful.

In this post you will see how to set the page title in Angular applications.

There is a built-in service in ‘@angular/platform-browser’ package calles “TitleService” that we can leverage.

First of all, we need to import the TitleService as a provider in our app.module “providers”:

```
import { BrowserModule, Title } from ‘@angular/platform-browser’;
```

```
@NgModule({
```

```
declarations: [],
```

```
imports: [],
```

```
providers: [Title],
```

```
bootstrap: [AppComponent]
```

```
})
```

```
export class AppModule { }
```

Then, you just import that service in your component class:

```
import { Title } from ‘@angular/platform-browser’;
```

Then inject the service in the constructor of your component:

```
public constructor(private titleService: Title ) { }
```

The “Title” class has 2 members:

```
class Title {
```

```
getTitle() : string
```

```
setTitle(newTitle: string)
```

```
}
```

So you can simply call the ‘setTitle” method to set the title of the page:

```
export class AppComponent { public constructor(private titleService: Title ) { }
```

```
public setTitle( newTitle: string) { this.titleService.setTitle( newTitle ); }}
```

Cheers!
