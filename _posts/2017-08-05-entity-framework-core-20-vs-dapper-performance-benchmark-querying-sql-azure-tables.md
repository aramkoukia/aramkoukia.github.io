---
layout: post
title: "Entity Framework Core 2.0 vs. Dapper performance benchmark, querying SQL Azure tables"
date: 2017-08-05
description: "While the .Net Core 2.0 is still being baked (Preview 3 is out now!), I thought I’d give the Entity Framework Core 2.0 a try and do a…"
image: https://cdn-images-1.medium.com/max/800/1*9UzjAlppKGnIAUpzMtWuYA.png
medium_url: https://medium.com/@aramkoukia/entity-framework-core-2-0-vs-dapper-net-performance-benchmark-querying-sql-azure-tables-7696e8e3ed28
---

### Entity Framework Core 2.0 vs. Dapper performance benchmark, querying SQL Azure tables

![](https://cdn-images-1.medium.com/max/800/1*9UzjAlppKGnIAUpzMtWuYA.png)

While the .Net Core 2.0 is still being baked (Preview 3 is out now!), I thought I’d give the Entity Framework Core 2.0 a try and do a benchmark and compare it to Dapper.Net.

So without further rant, lets get to it:

### Database Setup:

I used SQL Azure, just because it is easy to setup the AdventureWorks sample DB there quickly. For this benchmark I will only use the Product and Product category tables.

### Entity Framework Core 2.0 Repository

Here how the Entity Framework Core 2.0 query looks like:

### Dapper.Net Repository

Here is how the Dapper.Net query looks like:

### Benchmark Class

For the benchmark, I usually use the [Benchmarkdotnet.org](http://benchmarkdotnet.org/Overview.htm). So here is how my benchmark class looks like:

### Running the Benckmark

Here is how I run the benchmark in my .Net Core 2.0 Console Application:

### Benchmark result

Aaaaand the winner is: **Dapper.net** (barely!)

![](https://cdn-images-1.medium.com/max/800/1*4TEvwLDa9mvha8_FB9ilhQ.png)

As you see in the above window, dapper’s number is better by 0.05 milliseconds in Standard deviation of all measurements.

### Source Code

If you want to play with the benchmark and add some more comparisons to it you can find it here:

[**aramkoukia/efcore2-vs-dapper-benchmark**  
*Contribute to efcore2-vs-dapper-benchmark development by creating an account on GitHub.*github.com](https://github.com/aramkoukia/efcore2-vs-dapper-benchmark "https://github.com/aramkoukia/efcore2-vs-dapper-benchmark")

### Book Recommendation

Here are some books around these subjects:

[![](https://cdn-images-1.medium.com/max/800/1*pzKXEmwnxVDrmY_BNcgSZA.png)](https://www.amazon.com/gp/product/B076WTH3FT/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B076WTH3FT&linkId=6074ed5b3a46e8b31c83f639ba70f497)

> If you liked this article, click the👏 below so other people will see it here on Medium.

> Let’s be friends on [Twitter](https://twitter.com/aramkoukia). Happy Coding :)

Cheers!
