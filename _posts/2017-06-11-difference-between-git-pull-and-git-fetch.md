---
layout: post
title: "Difference between ‘git pull’ and ‘git fetch’"
date: 2017-06-11
description: "Which one do you use? ‘pull’ or ‘fetch’?"
image: https://cdn-images-1.medium.com/max/800/1*ODQUZPiwWu04XxKX4f2jbg.jpeg
medium_url: https://medium.com/@aramkoukia/difference-between-git-pull-and-git-fetch-16e30c3849c9
---

### Difference between ‘git pull’ and ‘git fetch’

![](https://cdn-images-1.medium.com/max/800/1*ODQUZPiwWu04XxKX4f2jbg.jpeg)

Which one do you use? ‘pull’ or ‘fetch’?

To be honest, I used to just ignore ‘fetch’ and didn’t even know what it is and ‘pull’ all the time, but then I thought let’s see what the hell is this ‘fetch’ thing.

**Simply put,** `git pull` **is a** `git fetch` **followed by a** `git merge`**.**

#### When do you use ‘git fetch’?

‘fetch’ can be useful, when you want to get the stuff from a remote branch, but don’t want to merge it to your local branch!

You can do a `git fetch` at any time to update your remote-tracking branches under `refs/remotes/<remote>/`.

This command does not change any of your own local branches under `refs/heads`, and is safe to do without changing your working copy. Every now and then I I have seen people running `git fetch` periodically in a cron job in the background, though it sounds something that might make you really confused!

#### When do you use ‘git pull’?

A `git pull` is what you would do to bring a local branch up-to-date with its remote version, while also updating your other remote-tracking branches.

In other words: `git pull` will always merge into the **current branch**. So you select which branch you want to pull *from*, and it pulls it into the current branch. The *from* branch can be local or remote; it can even be a remote branch that's not a registered `git remote` (meaning you pass a URL on the `git pull` command line).

#### Can I do ‘git fetch’ and ‘git merge’ instead of ‘git pull’ then?

No. I mean not in all possible circumstances, though it *can* be emulated by a fetch and a merge.

I quote from one of the [folk’s comments on reddit](https://www.reddit.com/r/git/comments/6gmv5l/difference_between_git_pull_and_git_fetch/):

> *‘git pull’* *can* be emulated by a fetch and a merge. You just have to know which remote-tracking branch your local branch is tracking and then merge that specific branch into the local branch.

lol, yeah welcome to the GIT club!

![](https://cdn-images-1.medium.com/max/800/1*Ofazbh7yKD65Ny7O70ZGJw.jpeg)

`pull` can't actually be emulated by a `fetch` plus a `merge`. When you just fetch a change, only a remote branch pointer changes, and `merge` would refuse to do anything.

On the other hand `pull`, fast-forwards your tracking branch, so there is a actually a difference!

So, as an alternative to ‘git pull’, you can do a ‘git fetch’ followed by ‘git rebase origin/master’

Cheers!
