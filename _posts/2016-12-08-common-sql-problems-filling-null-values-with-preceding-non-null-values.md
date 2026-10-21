---
layout: post
title: "Common SQL Problems: Filling NULL values with Preceding Non-NULL values"
date: 2016-12-08
description: "The problem that I want to address here is Filling NULL or Empty values with Preceding Non-NULL values. let me show you some sample data…"
image: /assets/img/2016-12-08-common-sql-problems-filling-null-values-with-preceding-non-null-values/1.png
tags: ["Data"]
---

### Common SQL Problems: Filling NULL values with Preceding Non-NULL values

![](/assets/img/2016-12-08-common-sql-problems-filling-null-values-with-preceding-non-null-values/1.png)

The problem that I want to address here is Filling NULL or Empty values with Preceding Non-NULL values. let me show you some sample data and what is the ask so that you can have a better understanding of the question:

Imagine you have a table in excel that has below columns and some of the columns are null, but you want to fill them in with the last not-null value from the table:

**ID, ProductName, OrderDate, OrderQuantity**

This sort of data can come on your way for many reasons, one of the reasons that I have seen a lot is when you are dealing with imported data from Excel files or some data-warehouse system or export some other reports where they do not repeat the groups and just put the first one for better readability in their document, but you need to import it to some SQL table to generate some other reports out of it.

And now when you import this into SQL Server you will have NULLs for the blank ProductNames, now you want to update the ProductName column with the Non-NULL value before.

There are many ways for doing this, first and the worst( Performance wise, specially when you are dealing with huge amount of data which is very possible since you imported the data from a data-warehouse report) is a simple Cursor to just order by ID go through the list and Update the NULLs one by one until gets to the next None-NULL and so on and you know how to do it but that is not how SQL developers like to do their job!

the second way that I have experienced is using the CTEs

There are many other ways that you can address this, like using a CROSS APPLY join or Dense\_Rank and many other interesting ways, but today i think this one that you are going to see is the best way of doing it.

After introducing the new features of Windows Functions in SQL Server 2012 I think this is the way to deal with this problem with the Magic of the First\_Value function in the Windows Functions of SQL Server 2012 like this:
