---
layout: post
title: "Sorting an array of objects with Jquery"
date: 2016-12-08
description: "Imagine you have an array of objects like below and you want to sort them:"
medium_url: https://medium.com/@aramkoukia/sorting-an-array-of-objects-with-jquery-d01e12047ce4
---

### Sorting an array of objects with Jquery

Imagine you have an array of objects like below and you want to sort them:

```
{ TagId: 1, TagName: "C#", }, { TagId: 2, TagName: "Single Page Application", }, { TagId: 3, TagName: "Visual Studio", }, { TagId: 4, TagName: "Fakes", },
```

Now, you need 2 functions to sort these objects, one for Desc and one for Asc sort like this:

```
function sortByKeyDesc(array, key) {        return array.sort(function (a, b) {            var x = a[key]; var y = b[key];            return ((x > y) ? -1 : ((x < y) ? 1 : 0));        });    }    function sortByKeyAsc(array, key) {        return array.sort(function (a, b) {            var x = a[key]; var y = b[key];            return ((x < y) ? -1 : ((x > y) ? 1 : 0));        });    }
```

And when you want to sort your objects you can pass in the original collection and the Column that you need to sort based on like this:

```
function querySucceeded(data) {     posts = [];     posts = sortByKeyDesc(data, "TagName");  }
```

This is really handy for me while working with Knockout and MVVM or manipulating JSON Object.
