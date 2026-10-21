---
layout: post
title: "Select COUNT behavior in TSQL"
date: 2016-12-08
description: "A while a go I was trying to query a pretty big table to get the COUNT of the rows, and it was taking forever:"
tags: ["Data"]
---

### Select COUNT behavior in TSQL

A while a go I was trying to query a pretty big table to get the COUNT of the rows, and it was taking forever:

I was Using this:

```
SELECT COUNT(*) FROM [dbo].[EventLog]
```

It was taking around 10 seconds to give me the result which was 12,332,516, so I thought may be because it has too many columns it is like that, so let’s try it with a specific column:

```
SELECT COUNT(EventLogID) FROM [dbo].[EventLog]
```

Wow, this one takes around 1 Second to run, this is awesome…But wait, why is the result a little different?!Ah, this one takes the rows that are null for this column, so the result is 12,332,510, since I have 6 rows that EventLogId is null!Interesting, now let’s try something else, just put a number there, like this:

```
SELECT COUNT(1) FROM [dbo].[EventLog]
```

Ah, 1 second and the result is still the same as COUNT(\*)…

Yeah, This is what I want… I’ll use this one instead of COUNT(\*) or Count(ColumnName) from now on..

Or if you really want to count the rows that a specific column sets are NOT null, this might be a nice way for doing it…
