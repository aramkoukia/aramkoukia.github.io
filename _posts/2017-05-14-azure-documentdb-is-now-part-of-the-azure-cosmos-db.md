---
layout: post
title: "Azure DocumentDB is now part of the Azure Cosmos DB"
date: 2017-05-14
description: "When Microsoft introduced Azure DocumentDB, it was just a Document database, and Microsoft’s NoSQL Solution in the cloud."
image: https://cdn-images-1.medium.com/max/1200/1*AXmFA3fmAiHjS59yCE0ZXQ.png
---

### Azure DocumentDB is now part of the Azure Cosmos DB

![](https://cdn-images-1.medium.com/max/1200/1*AXmFA3fmAiHjS59yCE0ZXQ.png)

When Microsoft introduced [Azure DocumentDB](https://koukia.ca/microsoft-and-nosql-data-store-for-your-modern-cloud-application-e57885b18a5f), it was just a Document database, and Microsoft’s NoSQL Solution in the cloud.

Now recently, DocumentDB was moved to Azure’s new service: “[Cosmos DB](https://docs.microsoft.com/en-us/azure/documentdb/documentdb-introduction)”

> Azure Cosmos DB is Microsoft’s globally distributed, multi-model database service for mission-critical applications.

Azure Cosmos DB provides [turn-key global distribution](https://docs.microsoft.com/en-us/azure/documentdb/documentdb-distribute-data-globally), [elastic scaling of throughput and storage](https://docs.microsoft.com/en-us/azure/cosmos-db/partition-data)worldwide, single-digit millisecond latencies at the 99th percentile, [five well-defined consistency levels](https://docs.microsoft.com/en-us/azure/documentdb/documentdb-consistency-levels), and guaranteed high availability, all backed by [industry-leading SLAs](https://azure.microsoft.com/support/legal/sla/documentdb/v1_1/).

Azure Cosmos DB [automatically indexes data](http://www.vldb.org/pvldb/vol8/p1668-shukla.pdf)without requiring you to deal with schema and index management. It is multi-model and supports document, key-value, graph, and columnar data models.

As of now, if you go to Azure portal and try to create an Azure Cosmos DB, you have to select one of the 4 APIs available there:

- Gremlin (Graph)
- MongoDB
- SQL (DocumentDB)
- Table (key-value)

![](https://cdn-images-1.medium.com/max/800/1*HV86UDce5-QV0V8ceQi-FQ.png)

As you can see, even table storage, which used to be a separate storage service is now under the Azure Cosmos DB’s cloud.

Also, if you have existing DocumentDB resources in your Azure subscription, Microsoft is transitioning all of those and their data to Azure Cosmos DB for no additional charge. **So nothing to worry about there and your existing stuff should still work!**

I hope with this, you don’t get surprised when you login to Azure portal and see that your DocumentDB resources have been renamed!

Cheers!
