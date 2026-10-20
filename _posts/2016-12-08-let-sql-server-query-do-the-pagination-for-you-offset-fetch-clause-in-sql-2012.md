---
layout: post
title: "Let SQL Server Query do the pagination for you (OFFSET FETCH Clause in SQL 2012)"
date: 2016-12-08
description: "If you have done some Web programming or any similar scenario that needs to read data from database in chunks for performance reasons, you…"
image: /assets/img/2016-12-08-let-sql-server-query-do-the-pagination-for-you-offset-fetch-clause-in-sql-2012/1.png
---

### Let SQL Server Query do the pagination for you (OFFSET FETCH Clause in SQL 2012)

![](/assets/img/2016-12-08-let-sql-server-query-do-the-pagination-for-you-offset-fetch-clause-in-sql-2012/1.png)

If you have done some Web programming or any similar scenario that needs to read data from database in chunks for performance reasons, you definitely have came across implementing the pagination to fetch data from database page by page.

After introducing the ROW\_NUMBER() function by SQL Server I Used to do it using that, with adding where Clauses for the ROW\_NUMBER column to skip certain number of IDs and TAKE certain number of rows that I want like this:

```
SELECT ROW_NUMBER() OVER( ORDER BY AgreementNUmber) , * FROM [Agreement] ORDER BY [AgreementNumber] OFFSET 10 ROWS FETCH NEXT 50 ROWS ONLY;
```

Or sometimes I do expose the whole view or table and then in the application I’d use the SKIP and TAKE commands of the C# LINQ for implementing the pagination like this in C#:

```
var myPage = AgreementList.Skip(10).Take(5);
```

but now I can see that SQL SERVER 2012 has introduced these OFFSET FETCH commands which basically you can do it much simpler with these.

Here is how you can do it:

```
SELECT * FROM [Agreement] ORDER BY [AgreementNumber] OFFSET 10 ROWS FETCH NEXT 50 ROWS ONLY;
```

As you can easily guess, number **10** is the SKIP number and the number **5** is the TAKE number or the PAGE SIZE.

And then what I did was to do a simple SQL STATISTICS VIEW to see which one is better performance wise and i found the OFFSET FETCH twice faster than the ROW\_NUMBER one!

I tried the same Query on a table with 10,000 rows and I got these sql server execution times! but still it might be different in different sets of data

**SQL Server Execution Times: (with ROW\_NUMBER())**  
 CPU time = **31**ms, elapsed time = **28**ms.  
**SQL Server Execution Times: ( with OFFSET and FETCH)**  
 CPU time = **16**ms, elapsed time = **15**ms.

So I really think that I should review my existing pagination codes and try to replace them with this new one If possible since it is much simpler to implement and much faster(at least with this data set that I tested with)
