---
layout: post
title: "Hot to remove tracked file from Git"
date: 2020-02-17
description: "It has happened to the best of us that we add something to git by mistake, and even commit it (test result folder, log files, etc) but…"
image: https://cdn-images-1.medium.com/max/800/1*7OT7PnqQfHk08X4JlKVCFA.png
tags: ["Git"]
---

### How to remove tracked file from Git?

![](https://cdn-images-1.medium.com/max/800/1*7OT7PnqQfHk08X4JlKVCFA.png)*Image from dynamicuser.net*

It has happened to the best of us that we add something to git by mistake, and even commit it (test result folder, log files, etc) but then we realized we shouldn’t have done that.

Next move is to add it to “.gitignore” file and then if it changed, you won’t need to commit those changes.

However, that file keeps showing up in `git status` after it's edited.

**NOTE: While this will not remove the file from your local disk, it will remove the files from other developers machines on next** `git pull`**.**

Adding the file to `.gitignore` file will prevent this file from being added (without an `add -f`) to the set of files tracked by git, however git will continue to track any files that are already being tracked.

To stop tracking a file you need to remove it from the index. You can do that by the following command:

```
git rm --cached <file>
```

This command can be used to remove a folder as well like the following

`git rm -r --cached <folder>`

The removal of the file from the head will happen when you do your next commit.

If you use GIT regularly, I recommend to get this book and have it on your desk:

[![](https://cdn-images-1.medium.com/max/800/1*ZoGu8n3MF1M9bD9XQkmirQ.png)](https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1484200772&linkCode=as2&tag=aramkoukia-20&linkId=177b8e586149cbc1cd2599b9579e750b)

[**Pro Git**  
*Pro Git (Second Edition) is your fully-updated guide to Git and its usage in the modern world. Git has come a long way…*www.amazon.com](https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484200772&linkId=96c14a6ac18c484f2aa2f1106abeef58 "https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484200772&linkId=96c14a6ac18c484f2aa2f1106abeef58")

> If you liked this article, click the👏 below so other people will see it here on Medium.

> Let’s be friends on [Twitter](https://twitter.com/aramkoukia). Happy Coding :)

Cheers!
