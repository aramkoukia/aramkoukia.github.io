---
layout: post
title: "How to programmatically navigate using react router?"
date: 2020-03-27
description: "This is a quick one about “react-router”, a problem I faced and the solution I found, so just wanted to share with you!"
image: https://cdn-images-1.medium.com/max/800/0*Jc3Yjgc6wGlBMayY.jpeg
---

### How to programmatically navigate using react router?

![](https://cdn-images-1.medium.com/max/800/0*Jc3Yjgc6wGlBMayY.jpeg)*Image from medium.com*

This is a quick one about “react-router”, a problem I faced and the solution I found, so just wanted to share with you!

Using `react-router` I am able to use a `Link` element and create links which by default react router handles the navigation for them!

But what if I don’t have a “Link” and I want to navigate? Can I write code to navigate instead?

There might be lots of solutions but I think this one is a good one:

#### Using Hooks in React Router v5.1.0 and higher!

In React Router version 5.1.0 and after that there is a new `useHistory` hook (I think that is in React version 16.8.0 and higher) which does this for me!

How? here is a snippet of code that does it:

```
import { useHistory } from "react-router-dom";
```

```
function HomeButton() {  const history = useHistory();
```

```
function handleClick() {    history.push("/home");  }
```

```
return (    <button type="button" onClick={handleClick}>      Go home    </button>  );}
```

That’s it! easy eh!

If you are learning and working on React, I recommend you this book to take you to next level React development:

<https://amzn.to/2WSJ1VD>

[![](https://cdn-images-1.medium.com/max/800/0*LIM7IHo-ugXQlW6N.jpg)](https://amzn.to/2WSJ1VD)*[Pro React 16](https://amzn.to/2WSJ1VD)*

> If you liked this article, click the👏 below so other people will see it here on Medium.

> Let’s be friends on [Twitter](https://twitter.com/aramkoukia). Happy Coding :)

Cheer!
