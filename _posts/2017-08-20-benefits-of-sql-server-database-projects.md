---
layout: post
title: "Benefits of SQL Server Database Projects"
date: 2017-08-20
description: "Since Entity Framework has been released, for new projects many people have used EF Code-First approach to handle database schema changes…"
image: https://cdn-images-1.medium.com/max/800/1*OHdMMcaun7xJI2ons2s-vA.png
tags: ["Data", ".NET"]
---

### Benefits of SQL Server Database Projects

![](https://cdn-images-1.medium.com/max/800/1*OHdMMcaun7xJI2ons2s-vA.png)

Since Entity Framework has been released, for new projects many people have used EF Code-First approach to handle database schema changes (mostly for pre-production environments, because if you have a DBA team, they won’t allow you to run scripts that they don’t know what it does!) and I admit, it is pretty convinient and fast for developers when you start coding, when you want to add a table, add a column, create a foreign key, a primary key and etc … but!

I have been working with this EF Migration thing for a while recently, and I feel like the Database development skills and principals that are very helpful on many sides (Performance tuning, Clustered Indexes, Keys, Non Clustered Indexes, Naming Conventions, Constraints, Filtered Indexes, Partitions, Stored Procedures, Functions etc) are being overlooked, simply because EF Migration can only handle very little features that SQL Server has.

Now after few years of using Entity Framework and Code First in projects, a lot of junior developers don’t even know what a database index is and most often when some query is slow, they blame Entity Framework for it! Some people don’t even know how to check for missing indexes and how to add them. Basically developers think that they don’t need to have SQL Server knowledge or skills anymore, because they think Entity Framework is supposed to do everything for us!

So I thought I bring up some of the benefits of using SQL Server Databases

### 1. Developers will learn SQL Server development

I think as a developer that your system is dealing with a database, you need to have the database development skills. You cannot be building information systems, without knowing what is non-clustered index, or filtered index, materialized view and so many other useful things that a massive tool like SQL Server provides. Basically, a relational database is not just a bunch of tables that are linked together, and there is more to it. So using SQL Server Database project will give us the opportunity to learn and brush up our database skills.

### 2. Source Control

Database is code! just like our C# and JavaScript code, we need to use source control and keep it there. Won’t you freak out if I told you some of your C# code is not in GIT? How about your stored procedures, or filtered indexes or views? Yeah, so if we use Database Projects, our database code will be treated as real code as it is and we can keep a history!

> You can do proper code review for your database code.

### 3:Validate your database schema

With database projects you can use SQL Style Cops to enforce any database standard you might have, from naming conventions, missing indexes, etc.

> You will instantly know if any schema change broke any existing View or Stored procedure or any other database object

### 4: Test your database

Database projects / Data Tools let you add database “unit tests” to a new or existing test project. When you create a database test, you get a designer that lets you edit some SQL that runs the test and outputs results, then a pane that lets you define test conditions that operate on the results returned by the SQL of the test. You can test on the some conditions like Data Checksum, Empty ResultSet, Execution Time, Expected Schema, Not Empy ResultSet, Row Count and etc.

### 5. Independent database deployment

When you are using EF Code first, assuming you enable automatic migrations(which in most cases is not the case for Production environments) you cannot really deploy just database changes because it is part of your code. But if you had a separate Database Project you would be able to release your schema change anytime you want.

### 6. Easy to deploy

When you build a database project, it outputs a .dacpac file which contains a description of the desired schema to migrate to. This file can be applied to a production database on it’s own. Or you can use Octopus or other tools to build an MSI package and deploy this to any environment.

Cheers!
