---
layout: post
title: "How to remove local untracked files from the current Git branch"
date: 2017-08-14
description: "Well, the short answer as per the Git Documents is git clean"
image: https://cdn-images-1.medium.com/max/800/1*SptUKxY2gmxa4XC3W1_nRw.jpeg
tags: ["Git"]
---

### How to remove local untracked files from the current Git branch

![](https://cdn-images-1.medium.com/max/800/1*SptUKxY2gmxa4XC3W1_nRw.jpeg)

Well, the short answer as per the Git Documents is [git clean](https://git-scm.com/docs/git-clean)

If you want to see which files will be deleted you can use the `-n` option before you run the actual command:

```
git clean -n
```

Then when you are comfortable (because it will delete the files for real!) use the **-f** option:

```
git clean -f
```

Here are some more options for you to delete directories, files, ignored and non-ignored files

- To remove directories, run `git clean -f -d` or `git clean -fd`
- To remove ignored files, run `git clean -f -X` or `git clean -fX`
- To remove ignored and non-ignored files, run `git clean -f -x` or `git clean -fx`

**Note the case difference on the** `X` **for the two latter commands.**

If you use GIT regularly, I recommend to get this book and have it on your desk:

[![](https://cdn-images-1.medium.com/max/800/1*ZoGu8n3MF1M9bD9XQkmirQ.png)](https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1484200772&linkCode=as2&tag=aramkoukia-20&linkId=177b8e586149cbc1cd2599b9579e750b)

[**Pro Git**  
*Pro Git (Second Edition) is your fully-updated guide to Git and its usage in the modern world. Git has come a long way…*www.amazon.com](https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484200772&linkId=96c14a6ac18c484f2aa2f1106abeef58 "https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484200772&linkId=96c14a6ac18c484f2aa2f1106abeef58")

> If you liked this article, click the👏 below so other people will see it here on Medium.

> Let’s be friends on [Twitter](https://twitter.com/aramkoukia). Happy Coding :)

Cheers!
