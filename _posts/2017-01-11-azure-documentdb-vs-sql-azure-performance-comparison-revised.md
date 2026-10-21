---
layout: post
title: "#Azure #DocumentDB vs SQL Azure performance comparison — Revised"
date: 2017-01-11
description: "THE STORY"
image: https://cdn-images-1.medium.com/max/800/1*Nr0odbynwhHrS134WSXsgA.jpeg
tags: ["Azure", "Data"]
---

### #Azure #DocumentDB vs SQL Azure performance comparison — Revised

![](https://cdn-images-1.medium.com/max/800/1*Nr0odbynwhHrS134WSXsgA.jpeg)

### THE STORY

A while ago [I wrote some code](https://koukia.ca/azure-documentdb-vs-sql-azure-a-performance-comparison-da5feec95b72#.8n9bdwpzd) to compare the performance of Azure [DocumentDb](https://koukia.ca/microsoft-and-nosql-data-store-for-your-modern-cloud-application-e57885b18a5f#.62uc96x14) and SQL Azure and the conclusion was:

![](https://cdn-images-1.medium.com/max/800/1*mGwvdm4d_vDE5-TyVZlWkw.gif)

### WAIT … BACKUP

In [this post](https://koukia.ca/microsoft-and-nosql-data-store-for-your-modern-cloud-application-e57885b18a5f#.u8l5xlmv8) a while a go, I introduced the Azure DocumentDB and showed how you can connect to it, create documents there and read documents with queries.

In terms of SQL Azure there is nothing special involved and it works exactly how on-premise SQL Server works, and you can use ADO.NET, Entity Framework or any other technique that you might want to use for SQL Azure.

[Then, I compared](https://koukia.ca/azure-documentdb-vs-sql-azure-a-performance-comparison-da5feec95b72#.oecb3sghc) the performance on these two data stores and see which one will do better!

### BUT I WAS WRONG

Turns out, I was not following the best practices for using Azure DocumentDB, and DocumentDB can work much faster if you code it right!

So, [@arkramac](https://twitter.com/arkramac) made a PR and fixed the code issues.

[**Some performance improvement suggestions by arramac · Pull Request #1 · aramkoukia…**  
*@aramkoukia thanks for the blog on performance! I made some edits based on best practices for DocumentDB performance…*github.com](https://github.com/aramkoukia/DocumentDbvsSQLAzure/pull/1 "https://github.com/aramkoukia/DocumentDbvsSQLAzure/pull/1")

Now, after merging those changes I ran the tests available in the project on [Github](https://github.com/aramkoukia/DocumentDbvsSQLAzure) again.

The following table shows the results:

![](https://cdn-images-1.medium.com/max/800/1*Ll4c0GgYrenMJsFtUQslnA.png)

One thing to note here is that these numbers are, the time spent on network lag (mostly) , plus the actual database call.

### INSERT PERFORMANCE

So, looks like for insert operations, DocumentDb dominates for sure and SQL Azure cannot come even close!

![](https://cdn-images-1.medium.com/max/800/1*kBGQmdmky5ARl-i8ZNetgQ.gif)

### **READ PERFORMANCE**

When comparing the read operation of a single document vs read of a single record from SQL Azure, DocumentDb performs slightly better.

**Note:** when you read one document from DocumentDb, everything you need will be there so there in the document you get back, and you don’t need any additional calls needed to get the complete data, but in case of SQL Azure, because of normalization and foreign keys, normally you will need additional calls to get that data or at least have SQL joins which will make the Read operation slower.

But looks like reading several documents from DocumentDB, is slightly slower that SQL Azure, and again we should remember in case of SQL Azure there will be *SQL Joins* involved in real projects that we didn’t consider here, which will slow down the SQL Azure results.

### LATEST CODE

you can find the latest code and the tests in Github here:

[**aramkoukia/DocumentDbvsSQLAzure**  
*Contribute to DocumentDbvsSQLAzure development by creating an account on GitHub.*github.com](https://github.com/aramkoukia/DocumentDbvsSQLAzure "https://github.com/aramkoukia/DocumentDbvsSQLAzure")

> Over all, I believe the winner is Azure Document DB.

### ANYTHING ELSE?

The SQL Azure instance that I use in this sample is the Standard trier, and looks like the Premium tier is much faster than the Standard, and of course will cost you more.

Take a look at the below post on MSDN to compare the Standard and Premium tier of the SQL Azure:

[**Azure SQLDB Basic, Standard and Premium Tiers - Quick glimpse and first impressions**  
*After the recent BUILD conference, Microsoft team responsible for SQL Database development clearly accelerated on…*blogs.msdn.microsoft.com](https://blogs.msdn.microsoft.com/igorpag/2014/04/28/azure-sqldb-basic-standard-and-premium-tiers-quick-glimpse-and-first-impressions/ "https://blogs.msdn.microsoft.com/igorpag/2014/04/28/azure-sqldb-basic-standard-and-premium-tiers-quick-glimpse-and-first-impressions/")
