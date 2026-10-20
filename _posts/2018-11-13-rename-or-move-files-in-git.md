---
layout: post
title: "Rename or Move files in GIT"
date: 2018-11-13
description: "Git keeps track of changes to files in the working directory of a repository by their name. When you move or rename a file, Git doesn’t…"
image: https://cdn-images-1.medium.com/max/800/1*-l3Qrum9oPMiiM0yW7v_Ng.png
medium_url: https://medium.com/@aramkoukia/rename-or-move-files-in-git-e7259bf5a0b7
---

### Rename or Move files in GIT

![](https://cdn-images-1.medium.com/max/800/1*-l3Qrum9oPMiiM0yW7v_Ng.png)

Git keeps track of changes to files in the working directory of a repository by their name. When you move or rename a file, Git doesn’t see that a file was moved; it sees that there’s a file with a new filename, and the file with the old filename was deleted (even if the contents remain the same).

As a result, **renaming or moving a file in Git is essentially the same operation**; both tell Git to look for an existing file in a new location.

This may happen if you’re working with tools (such as IDEs) that move files for you and aren’t aware of Git (and so don’t give Git the correct move instruction).

Sometimes you’ll still need to manually rename or move files in your Git repository, and want to preserve the history of the files after the rename or move operation.

**As you know, readable history is one of the key benefits of a version control system, so it’s important to avoid losing it whenever possible.**

If a file has had 100 small changes made to it with good commit messages, it would be a shame to undo all that work just by renaming or moving a file.

### Problem

In your Git working directory, you wish to rename a previously committed file named *mycoolclass.cs* to *myCoolClass.cs* and commit the newly renamed file.

### Solution

Solution

1. Change to the directory containing your repository: for example,

```
cd /Repo/MyProject/.
```

2. Run the following git command:

```
git mv mycoolclass.cs myCoolClass.cs
```

There will be no output.

3. Run the following command to commit the change:

```
git commit --message 'Rename the cool class'
```

The output will like the following:

```
# git commit --message ‘Rename the cool class’[master c6eed66] Rename the coolclass1 file changed, 0 insertions(+), 0 deletions(-)rename thecoolclass.cs => theCoolClass.cs (100%)
```

You’ve renamed *thecoolclass.cs* to *theCoolClass.cs* and committed it.

### Discussion

Moving and renaming files in version control systems rather than deleting and re-creating them is done to preserve their history.

For example, when a file has been moved into a new directory, you’ll still be interested in the previous versions of the file before it was moved.

In Git’s case, it will try to auto-detect renames or moves on *git add* or *git commit*; if a file is deleted and a new file is created, and those files have a majority of lines in common, Git will automatically detect that the file was moved and *git mv* isn’t necessary.

Despite this handy feature, it’s good practice to use git mv so you don’t need to wait for a *git add* or *git commit* for Git to be aware of the move and so you have consistent behavior across different versions of Git (which may have differing move auto-detection behavior).

After running *git mv*, the move or rename will be added to Git’s index staging area, which, if you remember from technique 2, means the change has been staged for inclusion in the next commit.

It’s also possible to rename files or directories and move files or directories into other directories in the same Git repository using the *git mv* command and the same syntax as earlier.

If you want to move files into or out of a repository, you must use a different, non-Git command (such as a Unix *mv* command), because Git doesn’t handle moving files between different repositories with *git mv*.

#### What if the new file name already exists?

If the filename you move to already exists, you’ll need to use the following command

```
git mv -f
```

or

```
git mv --force
```

to request that Git overwrite whatever file is at the destination. If the destination file hasn’t already been added or committed to Git, then it won’t be possible to retrieve the contents if you erroneously asked Git to overwrite it.

If you use GIT regularly, I recommend to get this book and have it on your desk:

[![](https://cdn-images-1.medium.com/max/800/1*ZoGu8n3MF1M9bD9XQkmirQ.png)](https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1484200772&linkCode=as2&tag=aramkoukia-20&linkId=177b8e586149cbc1cd2599b9579e750b)

[**Pro Git**  
*Pro Git (Second Edition) is your fully-updated guide to Git and its usage in the modern world. Git has come a long way…*www.amazon.com](https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484200772&linkId=96c14a6ac18c484f2aa2f1106abeef58 "https://www.amazon.com/gp/product/1484200772/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484200772&linkId=96c14a6ac18c484f2aa2f1106abeef58")

> If you liked this article, click the👏 below so other people will see it here on Medium.

> Let’s be friends on [Twitter](https://twitter.com/aramkoukia). Happy Coding :)

Cheers!
