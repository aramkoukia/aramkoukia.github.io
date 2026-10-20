---
layout: post
title: "Search for a string in all Tables and all Fields of a database with #TSQL"
date: 2016-12-08
description: "With below stored procedure, you can search for a string across all the tables in your database in Sql Server:"
image: /assets/img/2016-12-08-search-for-a-string-in-all-tables-and-all-fields-of-a-database-with-tsql/1.png
medium_url: https://medium.com/@aramkoukia/search-for-a-string-in-all-tables-and-all-fields-of-a-database-with-tsql-b6f8a1bfda37
---

### Search for a string in all Tables and all Fields of a database with #TSQL

![](/assets/img/2016-12-08-search-for-a-string-in-all-tables-and-all-fields-of-a-database-with-tsql/1.png)

With below stored procedure, you can search for a string across all the tables in your database in Sql Server:

And then you can call The procedure like this:

```
EXEC SearchAllTables 'Computer'
```

This will give you the list of tables and the column that has the string you passed into the stored procedure.
