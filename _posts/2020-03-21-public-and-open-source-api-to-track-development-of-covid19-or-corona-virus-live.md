---
layout: post
title: "Public and Open-Source API to track development of COVID19 or Corona Virus live!"
date: 2020-03-21
description: "Unless you have been living under some rock or in long meditation sessions, you have not missed this nasty COVID19 virus pandemic!"
image: https://cdn-images-1.medium.com/max/800/0*KR4Uk_ECjaOBZMiT
---

### Public and Open-Source API to track development of COVID19 or Corona Virus live!

![](https://cdn-images-1.medium.com/max/800/0*KR4Uk_ECjaOBZMiT)

Unless you have been living under some rock or in long meditation sessions, you have not missed this nasty COVID19 virus pandemic!

People have been putting together all kinds of websites and visualizations online to get us informed! And me being a nerd, looked into things a bit to see what are all the public APIs available to use for visualizing the situation and of course there is a ton of opensource stuff out there!

One of the more easy to use ones is hosted in this URL:

<https://coronavirus-tracker-api.herokuapp.com/v2/locations>

And here is another alternative that update the cases more frequently:

<https://corona.lmao.ninja/all>

This is an Opensource project with really fast responses (responds under 200 milliseconds!) implemented with Python using the 🍼 Flask framework!

The code is in this Repo on Github if you wanted to contribute to it:

[**ExpDev07/coronavirus-tracker-api**  
*This is a fast (< 200ms) and basic API for tracking development of the new coronavirus (COVID-19, SARS-CoV-2). It's…*github.com](https://github.com/ExpDev07/coronavirus-tracker-api "https://github.com/ExpDev07/coronavirus-tracker-api")

The data is provided by **Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)** the which this very popular visualization dashboard is made based on that:

[**Operations Dashboard for ArcGIS**  
*Edit description*www.arcgis.com](https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6 "https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6")

Here is the Github repository for the data that this API is serving:

<https://github.com/CSSEGISandData/COVID-19>

### Getting latest amount of total confirmed cases, deaths, and recoveries.

```
GET /v2/latest
```

```
{  "latest": {    "confirmed": 197146,    "deaths": 7905,    "recovered": 80840  }}
```

### Getting all locations.

```
GET /v2/locations
```

```
{  "locations": [    {      "id": 0,      "country": "Thailand",      "country_code": "TH",      "province": "",      "last_updated": "2020-03-21T06:59:11.315422Z",      "coordinates": {        "latitude": "15",        "longitude": "101"      },      "latest": {        "confirmed": 177,        "deaths": 1,        "recovered": 41      }    },    {      "id": 39,      "country": "Norway",      "country_code": "NO",      "province": "",      "last_updated": "2020-03-21T06:59:11.315422Z",      "coordinates": {        "latitude": "60.472",        "longitude": "8.4689"      },      "latest": {        "confirmed": 1463,        "deaths": 3,        "recovered": 1      }    }  ]}
```

Additionally, you can also filter by country ([alpha-2 country\_code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

```
GET /v2/locations?country_code=US
```

Include timelines.

```
GET /v2/locations?timelines=1
```

### Getting a specific location (includes timelines by default).

```
GET /v2/locations/:id
```

```
{  "location": {    "id": 39,    "country": "Norway",    "country_code": "NO",    "province": "",    "last_updated": "2020-03-21T06:59:11.315422Z",    "coordinates": { },    "latest": { },    "timelines": {      "confirmed": {        "latest": 1463,        "timeline": {          "2020-03-16T00:00:00Z": 1333,          "2020-03-17T00:00:00Z": 1463        }      },      "deaths": { },      "recovered": { }    }  }}
```

Exclude timelines.

```
GET /v2/locations?timelines=0
```

### Data

The data comes from the [2019 Novel Coronavirus (nCoV) Data Repository, provided by JHU CCSE](https://github.com/CSSEGISandData/2019-nCoV). It is programmatically retrieved, re-formatted and stored in the cache for one hour.

If like me need a lot if distraction these days, here is a very good coloring book for adults that helps a lot:

<https://amzn.to/2wqgE64>

[![](https://cdn-images-1.medium.com/max/800/0*E7dutayGae3I_56-.jpg)](https://amzn.to/2wqgE64)*A Swear Word Coloring Book for Adults: Sweary AF: F\*ckity F\*ck F\*ck F\*ck*

> If you liked this article, click the👏 below so other people will see it here on Medium.

> Let’s be friends on [Twitter](https://twitter.com/aramkoukia). Happy Coding :)

Cheers and #StaySafeStayHome everyone!
