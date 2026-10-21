---
layout: post
title: "SQL Server Foreign Key Update and Delete Rules"
date: 2017-04-17
description: "The Story"
image: https://cdn-images-1.medium.com/max/800/1*VVi038EBGPH2xNTdAeEa1g.jpeg
tags: ["Data"]
---

### SQL Server Foreign Key Update and Delete Rules

![](https://cdn-images-1.medium.com/max/800/1*VVi038EBGPH2xNTdAeEa1g.jpeg)

### The Story

Foreign key constraints are very important in SQL Server or any Relational Database Design and are play a key role in data integrity.

When we write Update and Delete queries on parent tables, we need to pay attention to the impact those commands will have on the data in the child tables(if there is any)

SQL Server has various rules for you to specify, what should happen to the data in the child table, when something is updated or deleted from the parent table. You need to decide wisely based on your requirements to make sure your data integrity is intact.

### Delete and Update Rules

You can create Foreign key constraints by referencing a primary or unique key from a parent table.

With Foreign key constraints, we make sure the relational integrity of data in the parent and child tables.

A foreign key value could be “NULL”, which means that particular record has no record in the parent table. But if it has a value, then it should have an associated record in the parent table.

Now when we run an update or delete command on parent table, we might need that command to have different effects on the data in child tables.

There are four available options in SQL Server 2005 and later versions (SQL Server 2016 as of today) as follows:

- No Action
- Cascade
- SET NULL
- SET Default

**Note: You can select different rules for update and delete, or pick the same rule.**

The following table summarizes the way each of the above rule will operate:

![](https://cdn-images-1.medium.com/max/1200/1*q5jfVpmGyDjxnQRjsvO44A.png)

Cheers!
