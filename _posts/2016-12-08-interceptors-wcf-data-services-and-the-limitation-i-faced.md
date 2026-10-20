---
layout: post
title: "Interceptors (WCF Data Services) and the limitation I faced"
date: 2016-12-08
description: "Say we have a list of Orders that we need to return to the client, but we only want to return the rows that are related to that specific…"
image: /assets/img/2016-12-08-interceptors-wcf-data-services-and-the-limitation-i-faced/1.png
medium_url: https://medium.com/@aramkoukia/interceptors-wcf-data-services-and-the-limitation-i-faced-7387bbc598c4
---

### Interceptors (WCF Data Services) and the limitation I faced

Say we have a list of Orders that we need to return to the client, but we only want to return the rows that are related to that specific client/customer and that means, we somehow identify the caller of the method in the interceptor and inside the interceptor method, we retrieve the Accounts that the caller has access to and then filter the returned data with an IN kind of query like

Select \* from Orders where AccountId in ( blah )

```
[QueryInterceptor("AssetAggregations")] public Expression<Func<AssetAggregation, bool>> AssetAggregationInterceptor() { var accounts = GetCustomerAccounts(); return row => accounts.Any(accountNumber => accountNumber == row.PurchasingAccountNumber); }
```

now what will happen if you open up the sql profiler and see what is actually being executed by this, is that you will see something like this there if you have more than 32 Accounts :

![](/assets/img/2016-12-08-interceptors-wcf-data-services-and-the-limitation-i-faced/1.png)

and since 32 is the limit for nested subquery in sql server (<http://msdn.microsoft.com/en-us/library/ms143432.aspx> ) it is going to complain that: SQL Statement is nested too deeply, rewrite the query or break it up into simillar queries.  
using Interceptors are fairly easy to implement, but with this limitation for specific scenario we might need to come up with a workaround.  
there are couple ways I can think of just now:  
- get rid of the Interceptor and use stored procedures and pass in the items to need to be filtered and expose the returning result of the stored procedure.  
- add webgets instead of exposing entities directly and inside the webget get the data from the Entity Framework and use a Contains operator there like :

```
return _db.Orders().where(m=>Accounts.Contains(Accountnumber));
```
