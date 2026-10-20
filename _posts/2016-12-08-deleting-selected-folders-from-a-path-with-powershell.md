---
layout: post
title: "Deleting selected folders from a path with #Powershell"
date: 2016-12-08
description: "I think many of you have experienced the pain that your project have problems, and even “Clean”ing the solution from Visual Studio does not…"
image: /assets/img/2016-12-08-deleting-selected-folders-from-a-path-with-powershell/1.png
---

### Deleting selected folders from a path with #Powershell

![](/assets/img/2016-12-08-deleting-selected-folders-from-a-path-with-powershell/1.png)

I think many of you have experienced the pain that your project have problems, and even “Clean”ing the solution from Visual Studio does not work and you have to go and delete the bin and obj files manually from all projects in your solution.

Well, there has been times that I wish I could simply run a script and delete whatever I want from a specific folder.

With this Powershell script, you can just give it the Current Directory and it will delete all bin and obj folders available in that folder …

```
param ($currentDir = $(throw “Current directory to start deleting obj and bin files from is required”))
```

```
dir $currentDir -include bin,obj -recurse | foreach($_) { rd $_.fullname –Recurse –Force}
```

Enjoy…
