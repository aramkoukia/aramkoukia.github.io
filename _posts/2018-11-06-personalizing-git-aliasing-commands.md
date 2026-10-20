---
layout: post
title: "Personalizing GIT: Aliasing commands"
date: 2018-11-06
description: "One of the most powerful features available with git config is aliasing."
image: https://cdn-images-1.medium.com/max/800/1*tIlbC_ggkdPLBgR0SfbwXQ.png
---

### Personalizing GIT: Aliasing commands

![](https://cdn-images-1.medium.com/max/800/1*tIlbC_ggkdPLBgR0SfbwXQ.png)

One of the most powerful features available with git config is aliasing.

Aliases allow you to create your own Git commands from combinations of other Git commands or by renaming them.

This may be useful for making commands that are more memorable or easier to type. These are set as configuration values in the alias section.

#### **Problem**

You wish to create a shorter alias for the “***git commit -m***” command and instead just type ***git c -m “your message”*** and and commit your changes. Or run “***git a”*** instead of “***git add .***”

#### Solution

You don’t need to change to the directory of a particular or any Git repository.

Run:

```
git config --global alias.c "commit"git config --global alias.a "add ."git config --global alias.p "push"git config --global alias.s "status"
```

There will be no output.

![](https://cdn-images-1.medium.com/max/1200/1*22dI_dTKuMMU6WoyvfGb6A.png)

You can verify that this has worked by viewing the relevant section of the ***~/.gitconfig*** file using ***grep***.

Now you can run the following aliases instead of the full commands:

```
git s
```

```
git a
```

```
git c -m “commit message”
```

```
git p
```

### Chaining Multiple Commands with Aliases

In addition to aliasing and shortening commands, you can also use the alias functionality to chain multiple commands together.

Any alias that starts with a **!** is run as a command in the root of the repository’s working directory.

Let’s create a command that does a fetch and then an interactive rebase.

Run:

```
git config --global alias.fr ‘!git fetch && git rebase -i origin/master’.
```

Now you can run instead of the above 2 git commands:

```
git fr
```

This tells Git to go to the root of the working directory (the directory containing the .git directory), run git fetch, and, if it succeeds, run ***git rebase -i origin/master***.

This can be useful in doing something similar to ***git pull — rebase*** but doing an interactive ***rebase*** instead.

I often use this when I know some changes have been made upstream and I want to squash and reorder my commits based on these changes.

For example, if I know changes have been made to the *origin/master* remote branch, this alias will fetch them and interactive-rebase the current branch on top of the *origin/ master* remote branch

PS: When I posted this article on reddit some folks took some time and gave me feedback and ideas, and I thought I should share their thought with you here:

Here some aliases they use:

```
git config — global alias.ap “add — patch”git config — global alias.amend “commit — amend”git config — global alias.g “grep”git config — global alias.master “checkout master”git config — global alias.pushf “push — force-with-lease”  git config --global alias.hist "log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short"
```

> I think making “a” an alias for “add .” is also super-dangerous, and is easy enough to type that it needn’t be shortened. Just make it alias “add”; in general “git add .” should be discouraged.

> Don’t alias “push” to “p”, you want to think before pushing, and it’s not frequent enough to try and save three characters. Same with “commit”, making it “c” is too short, it’s better to think one extra second about what you are committing while typing the 4 characters

Also some more others shared:

```
git config - global alias.showconflicted !git ls-files --unmerged | cut -f2 | sort -u git config - global alias.editconflicted !f() { git ls-files --unmerged | cut -f2 | sort -u ; }; $EDITOR `f` git config - global alias.details cat-file -p git config - global alias.root rev-parse --show-cdup git config - global alias.path rev-parse --show-toplevel git config - global alias.unmerged !git ls-files --unmerged | cut -f2 | sort -u git config - global alias.standup !git log --all --no-merges --graph --date=relative --committer=$(git config --get user.email) --pretty=format:'%C(cyan) %ad %C(yellow)%h %Creset %s %Cgreen%d' --since=$(if [[ Mon == $(date +%a) ]]; then echo last friday; else echo yesterday; fi) git config - global alias.today log --pretty=format:"%Cred%h %Cgreen%cd%Creset | %s%C(auto)%d %Cgreen[%an]%Creset" --date=local --since=midnight git config - global alias.upstream rev-parse --symbolic-full-name --abbrev-ref=strict HEAD@{u}
```

Also my favorite “**git fuckit**”:

```
git config — global alias.fuckit reset — hard
```

And to see all the aliases:

```
git config — global alias.alias config — get-regexp ^alias\.
```

Cheers!
