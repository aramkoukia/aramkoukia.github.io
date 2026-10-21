---
layout: post
title: "How to make Git “forget” about a file that was committed but is now in .gitignore?"
date: 2020-03-28
description: "Ever happened to you that you intentional or not, committed a file to git and then changed your mind and wanted git to forget about it?"
image: https://cdn-images-1.medium.com/max/800/0*GnXhp8UIwoe46rYV
tags: ["Git"]
---

### How to make Git “forget” about a file that was committed but is now in .gitignore?

![](https://cdn-images-1.medium.com/max/800/0*GnXhp8UIwoe46rYV)*Image from http://perforce.com*

Ever happened to you that you intentional or not, committed a file to git and then changed your mind and wanted git to forget about it?

Well, if we didn’t commit it yet, we normally add it to the `.gitignore` list and so git will ignore it even if you make changes to it, it won’t show up as part of your changes when you do `git status`.

But, if you forget to add it to `.gitignore` How do you make `git` to forget about it?

To stop tracking a file you need to remove it from the index. You can do this by running the following command:

```
git rm --cached <file-name>
```

If you want to remove a folder, you can use the -r argument that removes all filed in that folder recursively for you, like the following command:

```
git rm -r --cached <folder-name>
```

After you did this, on your next commit, the file will be removed from the head revision, so it won’t be in git anymore!

**NOTE: When you do this, it will not remove the physical file from your local (the computer that ran the command), but it WILL remove the files from other developers machines on next** `git pull`**.**

If you use GIT regularly, I recommend to get this book and have it on your desk:

[![](https://cdn-images-1.medium.com/max/800/1*ZoGu8n3MF1M9bD9XQkmirQ.png)](https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1484200772&linkCode=as2&tag=aramkoukia-20&linkId=177b8e586149cbc1cd2599b9579e750b)

[**Pro Git**  
*Pro Git (Second Edition) is your fully-updated guide to Git and its usage in the modern world. Git has come a long way…*www.amazon.com](https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484200772&linkId=96c14a6ac18c484f2aa2f1106abeef58 "https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484200772&linkId=96c14a6ac18c484f2aa2f1106abeef58")

> If you liked this article, click the👏 below so other people will see it here on Medium.

> Let’s be friends on [Twitter](https://twitter.com/aramkoukia). Happy Coding :)

Cheers!
