---
layout: post
title: "How do I rename a local Git branch?"
date: 2019-09-18
description: "Ever happened to you that you made a branch and has a typo and you are itching to fix it?"
tags: ["Git"]
---

### How do I rename a local Git branch?

Ever happened to you that you made a branch and has a typo and you are itching to fix it?

Yeah, I hate it when that happens!

If the branch that you want to rename is not checked out you can use the following command:

```
git branch -m <old-branch-name> <new-branch-name>
```

If the branch that you want to rename is already checked out, you can use the following command:

```
git branch -m <new-branch-name>
```

For windows systems you need to use `-M`, for this command to work or you would get a “***branch already exists”***

Here is a sample command you can use on Windows:

```
git branch -M <new-branch-name>
```

I hope this saves you some time and you can fix your annoying typos!

Cheers!
