---
layout: post
title: "How can I remove a specific item from an array in JavaScript?"
date: 2021-11-12
description: "To do this we can find the index of the array we want to remove with indexOf, and remove that item with splice"
image: https://cdn-images-1.medium.com/max/800/0*rXEw3UTGyszrau10.png
medium_url: https://medium.com/@aramkoukia/how-can-i-remove-a-specific-item-from-an-array-in-javascript-db0c0c21fe50
---

### How can I remove a specific item from an array in JavaScript?

![](https://cdn-images-1.medium.com/max/800/0*rXEw3UTGyszrau10.png)*Image from codeburst.io*

To do this we can find the `index` of the array we want to remove with `indexOf`, and remove that item with `splice`

The splice() function changes the contents of an array by removing existing elements and/or adding new elements.

Here is an example:

```
const array = [1, 3, 5, 7];const index = array.indexOf(5);if (index > -1) {  array.splice(index, 1);}// array = [1, 3, 7]
```

In `splice` the second argument is the number of elements to remove. `splice` modifies the array in place and returns a new array containing the elements that have been removed.

If you use TypeScript and want to have a Type-Safe function with type parameter, you can use something like the following:

```
function remove<T>(arr: Array<T>, value: T): Array<T> {   const index = arr.indexOf(value);  if (index > -1) {    arr.splice(index, 1);  }  return arr;}
```

Hope this comes handy for you when dealing with JavaScript arrays.
