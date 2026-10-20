---
layout: post
title: "How do I “git pull” and overwrite my local changes?"
date: 2020-02-17
description: "Has it happened to you that you have a really old git repository, that is not in sync with the remote repository and you also may or may…"
image: https://cdn-images-1.medium.com/max/800/1*LnaAe0o0ZtiXCYV71VphPw.png
---

### How do I “git pull” and overwrite my local changes?

![](https://cdn-images-1.medium.com/max/800/1*LnaAe0o0ZtiXCYV71VphPw.png)*image from jlord.us*

Has it happened to you that you have a really old git repository, that is not in sync with the remote repository and you also may or may not have some local commits, but now you want to “pull” remote changes and don’t care about your local changes?

well, one way is to delete the repo and clone again but the problem with this is, you will also lose any untracked files that exists in your git repo folder! So here is what you can do about it:

**WARNING: If you have any local commits or uncommitted changes, they will be gone by doing this!**

First you start with a “fetch — all” like the following

```
git fetch --all
```

Then, if you are on the “master” branch you can do the following:

```
git reset --hard origin/master
```

OR If you are on any other branch you can use the branch name like below:

```
git reset --hard origin/<branch_name>
```

### How does all this work?

Well first of all `git fetch` downloads the latest from remote without trying to merge or rebase anything.

Then the `git reset` resets the master branch to what you just fetched.

The `--hard` option changes all the files in your working tree to match the files in `origin/master` branch

### Can I keep local commits?

You can! one simple approach is, to make a local branch from the branch you are on before running the “reset” command like the following:

```
git checkout mastergit branch new-backup-branchgit fetch --allgit reset --hard origin/master
```

### What happens to my Uncommitted changes?

“Uncommited” or even “staged” changes will be lost when you run the “reset” command!

If you want to keep those you can use the “stash” command before running the reset, and after doing the “pull”, you can “apply” or “pop” the stashed changes on top of your changes.

For that you can run the following stash command:

```
git stash
```

And after you finished the reset and pull, to reapply these stashed changes you can use the following command:

```
git stash pop
```

If you use GIT regularly, I recommend to get this book and have it on your desk:

[![](https://cdn-images-1.medium.com/max/800/1*ZoGu8n3MF1M9bD9XQkmirQ.png)](https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1484200772&linkCode=as2&tag=aramkoukia-20&linkId=177b8e586149cbc1cd2599b9579e750b)

[**Pro Git**  
*Pro Git (Second Edition) is your fully-updated guide to Git and its usage in the modern world. Git has come a long way…*www.amazon.com](https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484200772&linkId=96c14a6ac18c484f2aa2f1106abeef58 "https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484200772&linkId=96c14a6ac18c484f2aa2f1106abeef58")

> If you liked this article, click the👏 below so other people will see it here on Medium.

> Let’s be friends on [Twitter](https://twitter.com/aramkoukia). Happy Coding :)

Cheers!
