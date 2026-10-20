---
layout: post
title: "Pipes in #Angular2"
date: 2016-12-27
description: "Pipe is a mechanism for transforming and formatting data within HTML templates in an Angular2 application."
image: https://cdn-images-1.medium.com/max/800/1*4hhei-6UcZ1OFUG7-Z_vjw.jpeg
---

### Pipes in #Angular2

![](https://cdn-images-1.medium.com/max/800/1*4hhei-6UcZ1OFUG7-Z_vjw.jpeg)

Pipe is a mechanism for transforming and formatting data within HTML templates in an Angular2 application.

The pipe `|` character is used to apply filters in AngularJS. Filters are used to to transform the data into a specified format.

### Built-in Pipes in Angular 2

Below table has the most common ones:

![](https://cdn-images-1.medium.com/max/800/1*lhBRnAVwVGazYseLDvZ4DQ.png)

There are more built-in pipes that you can find in the [Angular API reference](https://angular.io/docs/ts/latest/api/#!?apiFilter=pipe).

**Example:**

Below is how you use the pipe in the html template:

The output will look like:

```
Welcome back JOE schmoOn Jun 26, 2016 at 7:18 you reserved room 205 for Nov 14, 2025 for a total cost of $99.99.
```

Pipes can also be chained:

```
<p>Today is {{ today | date:'fullDate' | uppercase}}.</p>
```

### Custom Pipes

You can also implement your custom pipe to do your own transformation logic.

The following code snippet shows how you can create a custom pipe called: “MyPipe”

In the following code snippet, we use the pipe in the angular component:

And you need the following code to declare and include your custom pipe in your angular module:

For more information about pipes visit the [Angular2 API reference.](https://angular.io/docs/ts/latest/guide/pipes.html)
