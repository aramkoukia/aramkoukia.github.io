---
layout: post
title: "Cache-Aside Pattern — From #Cloud #DesignPatterns"
date: 2016-12-14
description: "Caching is a common technique to improve the performance and scalability problems by copying high demand data to a fast storage as close as…"
image: /assets/img/2016-12-14-cache-aside-pattern-from-cloud-designpatterns/1.png
medium_url: https://medium.com/@aramkoukia/cache-aside-pattern-from-cloud-designpatterns-904a39e8eb5d
---

### Cache-Aside Pattern — From #Cloud #DesignPatterns

Caching is a common technique to improve the performance and scalability problems by copying high demand data to a fast storage as close as possible to the application that needs that data.

Obviously you want to cache the stuff that are read a lot and at the same time, are not changing as much. Also we cache when reading from the original data source is expensive/slow or there is a network hop that we want to avoid.

One problem that we want to pay attention to is, we need to make sure the data between the cache and the original source is consistent.

### Problems with caching

Keeping the cached data consistent with the underlying data source is the biggest challenge and sometimes it is considered impractical to keep them consistent all the time.

We should just implement strategies to ensure our cache is up to date as much as possible. We also need to handle situations where data is not updated in the cache so we need to update the cache once we detect such things.

### Implementation

Following image displays the steps needed when using a cache.

![](/assets/img/2016-12-14-cache-aside-pattern-from-cloud-designpatterns/1.png)

1. Check if the item is in the cache.
2. If item is not in the cache, read it from data store.
3. Put a copy of the item into the cache.

If the underlying data gets changed, the corresponding item in the cache will be invalidated, so in the next read operation, since it is not in the cache, it will be read from the data store and will be updated in the cache as displayed above.

A lot of third party caching system, will do these read and write operations behind the senses, so that you just deal with the cache and it the item is not in the cache, it will read it from the original source and update the cache. If the caching system does not have this feature, then we can just implement this logic in our application.

### Things to watch out for

- **Cached Data expiration.** Choosing a proper expiration policy is important. You don’t want the cache to expire too often so the application is constantly reading from the original data source. Also you don’t want to have a long expiration date so that your cached data is stale. For cache-aside to be effective, make sure that the expiration policy matches the frequency that application accesses the data. Caching is most effective for relatively static data, or data that is read frequently.
- **Data Clean up.** Your cache size is normally less than your data source, that means you cannot cache everything you have in the database in your cache so they will evict data if necessary. Most caches use a least-recently-used policy for selecting items to clean up, but you might be able to customize this policy. Also you don’t need to have the same eviction policy for all items in the cache and you can think and design different policies for different object that you are caching.
- **Cache Hydration.** Many solutions prepopulate or hydrate the cache before the application starts, or when the application starts the first time or when we deploy the application. The Cache-Aside pattern may still be useful if some of this data expires or is evicted.
- **Consistency.** Implementing the Cache-Aside pattern does not guarantee consistency between the data store and the cache. Any change in the data source will create inconsistency, and it will stay like that in the cache until the next time that data is loaded into the cache or it is expired. This will happen if there is a miss to invalidate the cache somewhere in the code, or the data is changed in the data source directly without using the application that invalidates the cache properly.
- **Local (In-Memory) Caching.** A cache could be local to an application instance and stored in-memory. Cache-aside can be useful in this environment if an application accesses the same data frequently. However, a local cache is private and so different application instances could each have a copy of the same cached data. This data could quickly become inconsistent between caches, so it may be necessary to expire data held in a private cache and refresh it more frequently. In these scenarios it may be appropriate to investigate the use of a shared or a [distributed caching](https://en.wikipedia.org/wiki/Distributed_cache) mechanism.

### Use cases for this pattern

#### This pattern is suitable when:

- The cache system you use cache does not provide native read-through and write-through operations.
- Resource demand is unpredictable. This pattern enables applications to load data on demand.

#### This pattern is **not** suitable when:

- When the cached data source not changing (static data). In this case you can use approaches like [CDN (Content Delivery Network)](https://en.wikipedia.org/wiki/Content_delivery_network) or If the data will fit into the available cache space, hydrate the cache with the data on startup and set the expiry date of it to “*Never”.*
- Don’t cache session state information in a web application hosted in a web farm. In this environment, you should avoid introducing dependencies based on client-server affinity.

### Popular cloud caching systems:

[**Azure Redis Cache - Redis cache cloud service | Microsoft Azure**  
*Learn about Azure Redis Cache, a cloud service based on the popular open-source Redis cache. Keep your applications…*azure.microsoft.com](https://azure.microsoft.com/en-us/services/cache/ "https://azure.microsoft.com/en-us/services/cache/")

[**AWS | Amazon ElastiCache - in-memory data store and cache**  
*Amazon ElastiCache is a web service that makes it easy to set up, manage and scale a distributed in-memory data store…*aws.amazon.com](https://aws.amazon.com/elasticache/ "https://aws.amazon.com/elasticache/")

[**Memcache Overview | App Engine standard environment for Java | Google Cloud Platform**  
*com.google.appengine.api.prospectivesearch.dev*cloud.google.com](https://cloud.google.com/appengine/docs/java/memcache/ "https://cloud.google.com/appengine/docs/java/memcache/")

[**IBM Bluemix Trial: Sign up**  
*Sign up for the IBM Bluemix Trial. The Bluemix cloud platform gives you the flexibility to fully integrate development…*developer.ibm.com](https://developer.ibm.com/sso/bmregistration?lang=en_US&ca=dw-_-bluemix-_-cl-cacheservices-app-_-article "https://developer.ibm.com/sso/bmregistration?lang=en_US&ca=dw-_-bluemix-_-cl-cacheservices-app-_-article")
