---
layout: post
title: "Using Synonyms in Azure Search"
date: 2018-11-05
description: "Azure Search is a SaaS solution that gives 
 developers APIs for adding a rich search experience over content in web, mobile, and…"
image: https://cdn-images-1.medium.com/max/800/1*6etLB3oJZnmA2XwCoO86cA.png
medium_url: https://medium.com/@aramkoukia/using-synonyms-in-azure-search-1fd47e0776eb
---

### Using Synonyms in Azure Search

![](https://cdn-images-1.medium.com/max/800/1*6etLB3oJZnmA2XwCoO86cA.png)*Azure Search. Image from: <https://azure.microsoft.com/en-us/services/search/>*

Azure search has been around for years now:

> Azure Search is a search-as-a-service cloud solution that gives developers APIs and tools for adding a rich search experience over private, heterogenous content in web, mobile, and enterprise applications. Query execution is over a user-defined index.

> \* Build a search corpus containing only your data, sourced from multiple content types and platforms.

> \* Leverage AI-powered indexing to extract text and features from image files, or entities and key phrases from raw text.

> \* Create intuitive search experiences with facet navigation and filters, synonyms, auto-complete, and text analysis for “did you mean” auto-corrected search terms.

> \* Add geo-search for “find near me”, language analyzers for non-English full text search, and scoring logic for search rank.

But it is getting better everyday! Recently there a cool new feature available in Azure Search called **Synonyms.**

With [Synonyms](https://docs.microsoft.com/en-us/azure/search/search-synonyms) you can allow Azure Search to link equivalent terms that implicitly expand the scope of a query, without the you having to provide the synonym terms.

It does exactly what you guessed it does. You can define synonyms for certain terms and the query would return regardless of which one of the synonyms are searched for.

#### Synonym Maps

In Azure Search, synonym support is based on synonym maps that user defines and uploads to their search service.

These maps constitute an independent resource, such as indexes or data sources, and you can use them by any searchable field in any index in your search service.

Synonym maps use the [**Apache Solr**](https://lucene.apache.org/solr/guide/6_6/choosing-an-output-format.html)format as outlined in the example synonym map below:

```
POST https://[servicename].search.windows.net/synonymmaps?api-version=2017-11-11	api-key: [admin key]	{	   "name":"mysynonymmap",	   "format":"solr",	   "synonyms": "		USA, United States, United States of America\n		Washington, Wash., WA => WA\n"	}
```

In the above snippet, you can see there are two types of synonyms that are used.

The first example is a set of synonyms which indicate that a user could search using any of the three terms (“USA”, “United States”, or “United States of America”) in their query and any document that contains either of these terms will become viable search results.

The second example is an explicit mapping and is denoted by an arrow “=>” that states that a search query that matches the left hand side of “=>” will be replaced with the alternatives on the right hand side.

Given the rule below, search queries “Washington”, “Wash.”, or “WA” will all be rewritten to “WA”.

*Explicit mapping only applies in the direction specified and does not rewrite the query “WA” to “Washington” in this case.*

#### Which approach do I use?

**The first option** is useful in situations where you have multiple ways of referring to the same thing in the index.

**The second** is good when the data is normalized to single value in the index, but people would refer to the same thing by multiple terms in a query.

Once the synonym map has been created, you can then associate it with any fields within your indexes. Afterwards, the synonym map can be updated with new synonyms that will instantly be incorporated into subsequent searches. For example, if you were using the REST API to create your Azure Search index, you could apply it to a field called “description” as follows:

```
POST https://[servicename].search.windows.net/indexes?api-version=2017-11-11	api-key: [admin key]	{	    "name":"myindex",	    "fields":[	    {	        "name":"id",	        "type":"Edm.String",	        "key":true	    },	    {	        "name":"description",	        "type":"Edm.String",	        "searchable":true,	        "synonymMaps":[	            "mysynonymmap"	        ]	    }	    ]	}
```

Cheers!
