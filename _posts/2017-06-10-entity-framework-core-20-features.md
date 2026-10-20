---
layout: post
title: "Entity Framework Core 2.0 Features"
date: 2017-06-10
description: "Entity Framework Core 2.0 is now available."
image: https://cdn-images-1.medium.com/max/800/1*19hDux91qpoShfe7tXE5xg.png
medium_url: https://medium.com/@aramkoukia/entity-framework-core-2-0-features-cf5afe96476f
---

### Entity Framework Core 2.0 Features

![](https://cdn-images-1.medium.com/max/800/1*19hDux91qpoShfe7tXE5xg.png)

Entity Framework Core 2.0 is [now available](https://github.com/aspnet/EntityFramework/wiki/Roadmap).

I think the biggest catch about Entity Framework Core (EF Core) is it is Cross Platform! And second of all, it is light and extensible. But the 2.0 version is even better and has some great improvements compared to EF Core 1.0 version

### Visual Studio requirements

To get access to .NET Core tooling (and EF Core 2.0) in Visual Studio, you need to install Visual Studio 2017 15.3 Preview, Visual Studio for Mac or Visual Studio Code.

### What’s new in EF Core 2.0

The most interesting thing about this new EF Core 2.0 is the LINQ implementation, which is more robust and efficient compared to 1.0, and some major simplifications has been applied to EF Core’s provider model and the way it uses dependency injection.

#### Improved LINQ translation

The following are the few things that was wrong with EF Core 1.0 which is improved now:

- Unnecessarily create nested sub-queries
- Switch prematurely to client-side evaluation
- Retrieve all columns of a table when only a few were requested
- Translate a single LINQ query into N+1 queries, sometimes without appropriate filters

#### EF.Functions property for database operations and functions

EF.Functions property is introduced, that maps to database functions or operators, which will be invoked in LINQ queries. The first example of such a method is `Like()` operator.

```
var aUserss =    from u in context.Users    where EF.Functions.Like(c.Name, "aram%");    select u;
```

#### Global query filters to filter data verticlly, for specific entity types

The new version also address a common need to apply “vertical filters” when querying for data of specific entity types.

These filters are defined in the EF Core model and can reference properties in entities as well as be parameterized by capturing custom members of the derived `DbContext` class:

```
public class BloggingContext : DbContext{    public DbSet<Blog> Blogs { get; set; }    public DbSet<Post> Posts { get; set; }
```

```
public int TenantId {get; set; }
```

```
protected override void OnModelCreating(ModelBuilder modelBuilder)    {        modelBuilder.Entity<Post>()            .HasQueryFilter(p => !p.IsDeleted &&                  p.TenantId == this.TenantId );    }}
```

Filters are applied automatically when queries retrieve data of specific types directly as well as through navigation properties, e.g. using the `Include()` method.

Filters can also be disabled in individual LINQ queries using the `IgnoreQueryFilters()` operator.

#### Manual compiled queries

Manual or explicitly compiled query APIs have been available in previous versions of EF and also in LINQ to SQL to allow applications to cache the translation of queries so that they can be computed only once and executed many times.

Although in general EF Core can automatically compile and cache queries based on a hashed representation of the query expressions, this mechanism can be used to obtain a small performance gain by bypassing the computation of the hash and the cache lookup,  
allowing the application to use an already compiled query through the invocation of a delegate.

```
private static Func<CustomerContext, int, Customer> _customerById =    EF.CompileQuery((CustomerContext db, int id) =>        db.Customers            .Include(c => c.Address)            .Single(c => c.Id == id));
```

```
...
```

```
using (var db = new CustomerContext()){   var customer = _customerById(db, 147);   ...}
```

Cheers!
