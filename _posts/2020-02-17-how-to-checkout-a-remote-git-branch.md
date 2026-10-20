---
layout: post
title: "How to checkout a remote git branch"
date: 2020-02-17
description: "Ever happened to you that someone in the team pushes a new branch to the remote git repository and they you want to checkout their branch?"
image: https://cdn-images-1.medium.com/max/800/1*F6ETgzl5vAnFxNNwtyHK9g.jpeg
---

### How to checkout a remote git branch

![](https://cdn-images-1.medium.com/max/800/1*F6ETgzl5vAnFxNNwtyHK9g.jpeg)*Image from unity3d.college*

Ever happened to you that someone in the team pushes a new branch to the remote git repository and they you want to checkout their branch?

If you have you should have experienced that a simple “git checkout branchname” will not work!

To do that, if you have only one remote repository, you can do the following:

```
git fetchgit checkout branch_name
```

Not if you have multiple “remotes” the above command will not work and you need to use the following command instead:

```
git checkout -b branch_name <remote repo name>/branch_name
```

or a shorter version would be

```
git checkout -t <remote repo name>/branch_name
```

If you use GIT regularly, I recommend to get this book and have it on your desk:

[![](https://cdn-images-1.medium.com/max/800/1*ZoGu8n3MF1M9bD9XQkmirQ.png)](https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1484200772&linkCode=as2&tag=aramkoukia-20&linkId=177b8e586149cbc1cd2599b9579e750b)

[**Pro Git**  
*Pro Git (Second Edition) is your fully-updated guide to Git and its usage in the modern world. Git has come a long way…*www.amazon.com](https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484200772&linkId=96c14a6ac18c484f2aa2f1106abeef58 "https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484200772&linkId=96c14a6ac18c484f2aa2f1106abeef58")

> If you liked this article, click the👏 below so other people will see it here on Medium.

> Let’s be friends on [Twitter](https://twitter.com/aramkoukia). Happy Coding :)

Cheers!
