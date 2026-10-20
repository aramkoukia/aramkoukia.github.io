---
layout: post
title: "Upgrading your Angular App to latest version (4.0.0)"
date: 2017-04-10
description: "Angular version 4.0.0 is released (March 2017) and your Angular 2.X application will not break when you upgrade!"
image: https://cdn-images-1.medium.com/max/1200/1*Sj9GmC-vkFPRsqp53T3oAA.jpeg
medium_url: https://medium.com/@aramkoukia/upgrading-your-angular-app-to-latest-version-4-0-0-b39c2fbdf24
---

### Upgrading your Angular App to latest version (4.0.0)

![](https://cdn-images-1.medium.com/max/1200/1*Sj9GmC-vkFPRsqp53T3oAA.jpeg)

Angular version 4.0.0 is released (March 2017) and your Angular 2.X application will not break when you upgrade!

The upgrade is pretty straightforward. The following are the list of npm packages that you need to get the latest and you are good to go:

*@angular/common@latest   
@angular/compiler@latest   
@angular/compiler-cli@latest   
@angular/core@latest   
@angular/forms@latest   
@angular/http@latest   
@angular/platform-browser@latest   
@angular/platform-browser-dynamic@latest   
@angular/platform-server@latest   
@angular/router@latest   
@angular/animations@latest   
typescript@latest*

Here is the npm command to do that:

### What’s new?

Most of the changes are under the hood and related to some modules decoupling (Specifically, Anumation package is decoupled from angular/core), performance, and making packages smaller.

#### Improved directives: **\*ngIf and \*ngFor**

You can now use an if/else style syntax, and assign local variables such as when unrolling an observable.

I did this upgrade myself in a couple of my projects and things seems to be working fine so far as promised.

Cheers!
