---
layout: post
title: "How do I undo ‘git add’ before commit and push?"
date: 2019-09-18
description: "Ever happened to you that you do a “git add” and you noticed you don’t want to commit the file you added?"
tags: ["Git"]
---

### How do I undo ‘git add’ before commit and push?

Ever happened to you that you do a “*git add*” and you noticed you don’t want to commit the file you added?

Yep, that happens to me sometimes! maybe a bit more than sometimes!

You can do that with the following command:

```
git reset <file>
```

If you don’t specify the file name, it will “unstage” all the files that you added like the following:

```
git reset
```

I hope this saves you some time!

Cheers!
