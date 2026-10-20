---
layout: post
title: "Delete a local and a remote GIT branch"
date: 2017-11-16
description: "Have you ever gone through a few sprints of work, created several local and remote branches and wondering how to get rid of them (both…"
image: https://cdn-images-1.medium.com/max/800/1*zhYQt3quMouCIzJrROdUBQ.jpeg
---

### Delete a local and a remote GIT branch

![](https://cdn-images-1.medium.com/max/800/1*zhYQt3quMouCIzJrROdUBQ.jpeg)

Have you ever gone through a few sprints of work, created several local and remote branches and wondering how to get rid of them (both local and remote branches)?

Here some tips to do that:

### Delete a Local GIT branch

To delete the *local* GIT branch we can try one of the following commands:

```
git branch -d branch_namegit branch -D branch_name
```

as you can see above, we have 2 different argument, one with ‘d’ and one with ‘D’.

The `-d` option stands for `--delete`, which would delete the local branch, only if you have already pushed and merged it with your remote branches.

The `-D` option stands for `--delete --force`, which deletes the branch regardless of its push and merge status, so be careful using this one!

### Delete a remote GIT branch

To delete a remote branch you can use the following command:

```
git push <remote_name> --delete <branch_name>
```

Alternatively, there is this other following option too, which might be just a bit hard to remember:

```
$ git push <remote_name> :<branch_name>
```

These top options can also be used if you want to delete a “tag”.

### Push to remote branch and delete

If you ever want to push your local branch to remote and delete your local, you can use `git push` with the `-d` option as an alias for `--delete`.

If you use GIT regularly, I recommend to get this book and have it on your desk:

[![](https://cdn-images-1.medium.com/max/800/1*ZoGu8n3MF1M9bD9XQkmirQ.png)](https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1484200772&linkCode=as2&tag=aramkoukia-20&linkId=177b8e586149cbc1cd2599b9579e750b)

[**Pro Git**  
*Pro Git (Second Edition) is your fully-updated guide to Git and its usage in the modern world. Git has come a long way…*www.amazon.com](https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484200772&linkId=96c14a6ac18c484f2aa2f1106abeef58 "https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484200772&linkId=96c14a6ac18c484f2aa2f1106abeef58")

> If you liked this article, click the👏 below so other people will see it here on Medium.

> Let’s be friends on [Twitter](https://twitter.com/aramkoukia). Happy Coding :)

Cheers!
