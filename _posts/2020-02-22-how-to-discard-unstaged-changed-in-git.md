---
layout: post
title: "How to discard unstaged changed in GIT?"
date: 2020-02-22
description: "Have you ever tried to discard changes in your working directory that are not staged yet?"
image: https://cdn-images-1.medium.com/max/800/0*vye3KM0YU691TmLO.png
---

### How to discard unstaged changed in GIT?

![](https://cdn-images-1.medium.com/max/800/0*vye3KM0YU691TmLO.png)*image from dev.to*

Have you ever tried to discard changes in your working directory that are not staged yet?

One way to do that is to use the following command:

```
git stash save --keep-index --include-untracked
```

If you don’t need to e thorough about it you can drop the `--include-untracked` argument.

Later on, if you wanted to remove that stash, you can use the `git stash drop` command to do so!

If you use GIT regularly, I recommend to get this book and have it on your desk:

[![](https://cdn-images-1.medium.com/max/800/1*ZoGu8n3MF1M9bD9XQkmirQ.png)](https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1484200772&linkCode=as2&tag=aramkoukia-20&linkId=177b8e586149cbc1cd2599b9579e750b)

[**Pro Git**  
*Pro Git (Second Edition) is your fully-updated guide to Git and its usage in the modern world. Git has come a long way…*www.amazon.com](https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484200772&linkId=96c14a6ac18c484f2aa2f1106abeef58 "https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484200772&linkId=96c14a6ac18c484f2aa2f1106abeef58")

> If you liked this article, click the👏 below so other people will see it here on Medium.

> Let’s be friends on [Twitter](https://twitter.com/aramkoukia). Happy Coding :)

Cheers!
