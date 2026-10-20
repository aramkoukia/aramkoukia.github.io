---
layout: post
title: "STUFF vs COALESCE in TSQL for Concatenating row values"
date: 2016-12-08
description: "Say you have a result set that looks like the following table:"
image: /assets/img/2016-12-08-stuff-vs-coalesce-in-tsql-for-concatenating-row-values/1.png
---

### STUFF vs COALESCE in TSQL for Concatenating row values

![](/assets/img/2016-12-08-stuff-vs-coalesce-in-tsql-for-concatenating-row-values/1.png)

Say you have a result set that looks like the following table:

![](/assets/img/2016-12-08-stuff-vs-coalesce-in-tsql-for-concatenating-row-values/2.png)

Now what you want is, to have the result set to look like below:

![](/assets/img/2016-12-08-stuff-vs-coalesce-in-tsql-for-concatenating-row-values/3.png)

In the old days of SQL Server 7.0 and SQL Server 2000, I Used to do this with a variable and using COALESCE like the following:

But after SQL Server 2005 and XPATH appearance, I prefer to use STUFF and XPATH as below:

Cheers…
