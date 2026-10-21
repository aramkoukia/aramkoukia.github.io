---
layout: post
title: "GIT: Some Commit best practices and How to undo your recent Commits"
date: 2017-12-31
description: "One of the practices that we follow, when using GIT, or any distributed source control systems, is to “commit often”. Though these commits…"
image: https://cdn-images-1.medium.com/max/800/1*MUleaN6PZpHWitwk8ug2FQ.gif
tags: ["Git", "Architecture"]
---

### GIT: Some Commit best practices and How to undo your recent Commits

![](https://cdn-images-1.medium.com/max/800/1*MUleaN6PZpHWitwk8ug2FQ.gif)*“Holly shit, committed all that stupid stuff. The fuck do i do now? ”*

One of the practices that we follow, when using GIT, or any distributed source control systems, is to “**commit often**”. Though these commits need to have certain quality, it is still possible that you commit something stupid on your local branch and you want to revert it. Now how do you do that?

**Side node:** Commit/Check-in practices for Centralized Source Control systems might be slightly different, because you don’t really have local branches.

### Git Commit Best Practices

#### Commit Often

White it is considered good to commit often, you should try and commit stuff that are related together, so if you wanted to revert some you know which commit they are in.

What I do to make sure I have only related stuff in my commit is, I look at the message and see if I can use a message in one simple sentence. If no, that means I am mixing stuff in one commit.

Also, if you follow this rule since you have all things related in a commit, then you can share those changes with others more frequently and have them integrate their code with yours more often and avoid conflicts as early as possible.

Having big commits with a mix of stuff, will make it hard for everyone to merge changes.

#### **Commit when main scenarios are completed**

Though we recommend to commit often, we shouldn’t commit stuff that doesn’t compile or is not complete! That will create lots of churn and noise in the GIT history, and makes it really hard for people to understand what has happened in the code history.

That doesn’t mean you don’t commit anything until you finish your whole week’s work and then do one commit, but it means you break up your work into small enough pieces that you can commit and share with others, during one working day.

Ideally you should be able to break you work apart into 3 or 4 pieces ([If you commit more than 2.5 times a day, it would be more than industry average globally](http://help.gitprime.com/fundamentals-reports/industry-benchmarks))

If you really want to commit, not because you work is finished, but because you want a clean working directory, [you should consider using “stash” instead](https://git-scm.com/docs/git-stash).

For “stash” documentation, see the following link:

[**Git - git-stash Documentation**  
*Git is a member project of Software Freedom Conservancy, which handles legal and financial needs for the project…*git-scm.com](https://git-scm.com/docs/git-stash "https://git-scm.com/docs/git-stash")

### Test Your Code Before You Commit

Of course, if commit code, doesn’t necessarily mean, it is going to production directly (some places it actually does!), you should test your code before you commit. Why? Same reason as the incomplete work.

Then your history will be like:

*commit 1 :“Implemented this awesome feature”*

*commit 3:“Some fixes to this awesome feature”*

*commit 4:“Some MORE fixes to this awesome feature”*

*commit 5:“MORE and MORE fixes”*

*commit 5:“fixes”*

Now, if you want to pass these changes to someone, they should get all these commits, and if you wanted to take out this “awesome feature” you might miss some of the other commits that goes with it, to work properly!

**So, please resist this “Commit” temptation before you test your code properly!**

### How do I my revert latest commits?

While we hopefully consider all the “commit” practices mentioned before, we happen to screw up (a lot), and commit stupid stuff that we don’t want.

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
