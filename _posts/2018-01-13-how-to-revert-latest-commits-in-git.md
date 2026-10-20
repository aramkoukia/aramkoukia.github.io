---
layout: post
title: "How to revert latest commits in GIT?"
date: 2018-01-13
description: "While we hopefully consider all the “commit” best practices I talked about in a previous post, we happen to screw up (a lot), and commit…"
image: https://cdn-images-1.medium.com/max/800/1*4ELxxiHfVPtjnux4ER7ygg.gif
medium_url: https://medium.com/@aramkoukia/how-to-revert-latest-commits-in-git-fd86a1b2944a
---

### How to revert latest commits in GIT?

![](https://cdn-images-1.medium.com/max/800/1*4ELxxiHfVPtjnux4ER7ygg.gif)*How to undo my latest commits in GIT?*

While we hopefully consider all the [“commit” best practices I talked about in a previous post](https://koukia.ca/git-some-commit-best-practices-and-how-to-undo-your-recent-commits-d13c9dc3144f), we happen to screw up (a lot), and commit stupid stuff that we don’t want.

Now, I ideally we want a clear history (we don’t want the incomplete or wrong commit appear in the history), so we can use the following commands:

```
git reset --soft
```

With this command, all the stuff you changed in your latest commit will be uncommitted.

Then, you can use the ‘clean’ command to remove the bad files from your working directory:

```
git clean -f
```

**Note :If you want to process directories as well as files use “-d” command along with “-f”.**

Now, as if you haven’t commit yet, go ahead and make your fixes and commit again:

```
git commit -m "this awesome feature implementation, without the extra crap"
```

#### Using — soft vs — hard when doing reset

If you are don’t know the difference beween `--soft and --hard` use soft please. Why ?

If you choose `--hard` all the things that you have done in that commit will be **GONE**! as if you never did any of that. so be carefull when you use reset with `--hard` argument.

#### Using Graphical GIT Tools

Most of the graphical GIT tools have something similar that you can use to reset. For example with [SourceTree](https://www.sourcetreeapp.com/), one of the popular GIT tools, you can right click on any commit in a branch history and click “Reset the current branch to this commit” option.

![](https://cdn-images-1.medium.com/max/800/1*3EQ33lfLiDgUgvMIKhwm0g.png)*SourceTree reset branch option*

If you use GIT regularly, I recommend to get this book and have it on your desk:

[![](https://cdn-images-1.medium.com/max/800/1*ZoGu8n3MF1M9bD9XQkmirQ.png)](https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1484200772&linkCode=as2&tag=aramkoukia-20&linkId=177b8e586149cbc1cd2599b9579e750b)

[**Pro Git**  
*Pro Git (Second Edition) is your fully-updated guide to Git and its usage in the modern world. Git has come a long way…*www.amazon.com](https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484200772&linkId=96c14a6ac18c484f2aa2f1106abeef58 "https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484200772&linkId=96c14a6ac18c484f2aa2f1106abeef58")

Cheers!
