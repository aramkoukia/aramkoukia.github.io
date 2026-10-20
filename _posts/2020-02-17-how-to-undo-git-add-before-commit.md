---
layout: post
title: "How to undo “git add” before commit?"
date: 2020-02-17
description: "Have you ever done a “git add” or “staged” a file and then just before committing realized you don’t want to commit those?"
image: https://cdn-images-1.medium.com/max/800/1*Dor1DqiHjQ6F6YEZ85RDkQ.png
---

### How to undo “git add” before commit?

![](https://cdn-images-1.medium.com/max/800/1*Dor1DqiHjQ6F6YEZ85RDkQ.png)*Image from slideshare ( <https://www.slideshare.net/chrisma0/git-tricks-49753542>)*

Have you ever done a “git add” or “staged” a file and then just before committing realized you don’t want to commit those?

How do you undo that?

There are few options:

If you want to undo or “unstage” a particular file you can do:

```
git reset <file name to unstage>
```

This will remove the file from the current index (the “about to be committed” list of files) without changing anything.

If you want to unstage all the staged changes or all added files, you can use the reset command without any arguments, which can be useful if you have added a lot of files.

```
git reset
```

One thing to pay attention to here is, if your “git add” has overwritten a previously added file, this “reset” will not recover that previous file for you!

If the file that you mistakenly added was a really big one, you’ll probably notice that, even after removing it from the index with ‘`git reset`', it still seems to take space in the `.git` directory.

The added filed files stays in the repository, but only as a “loose object”. It will not be copied to other repositories (using clone or push commands), and this taken space in the .git folder will be eventually be freed up.

But if you need the space rightaway you can use the following command “gc” to clean it up:

```
git gc --prune=now
```

If you use GIT regularly, I recommend to get this book and have it on your desk:

[![](https://cdn-images-1.medium.com/max/800/1*ZoGu8n3MF1M9bD9XQkmirQ.png)](https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1484200772&linkCode=as2&tag=aramkoukia-20&linkId=177b8e586149cbc1cd2599b9579e750b)

[**Pro Git**  
*Pro Git (Second Edition) is your fully-updated guide to Git and its usage in the modern world. Git has come a long way…*www.amazon.com](https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484200772&linkId=96c14a6ac18c484f2aa2f1106abeef58 "https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484200772&linkId=96c14a6ac18c484f2aa2f1106abeef58")

> If you liked this article, click the👏 below so other people will see it here on Medium.

> Let’s be friends on [Twitter](https://twitter.com/aramkoukia). Happy Coding :)

Cheers!
