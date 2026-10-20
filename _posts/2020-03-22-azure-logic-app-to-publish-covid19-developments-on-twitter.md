---
layout: post
title: "Azure Logic App to publish COVID19 developments on Twitter"
date: 2020-03-22
description: "Yesterday I shared this Open-Source and Public API here that serves the latest COVID19 development around the world:"
image: https://cdn-images-1.medium.com/max/800/0*DM_Ca7BWUcsOMmmQ.jpg
---

### Azure Logic App to publish COVID19 developments on Twitter

![](https://cdn-images-1.medium.com/max/800/0*DM_Ca7BWUcsOMmmQ.jpg)*Image from <https://www.fsb.org.uk/>*

Yesterday I shared this Open-Source and Public API here that serves the latest COVID19 development around the world:

[**Public and Open-Source API to track development of COVID19 or Corona Virus live!**  
*Unless you have been living under some rock or in long meditation sessions, you have not missed this nasty COVID19…*koukia.ca](https://koukia.ca/public-and-open-source-api-to-track-development-of-covid19-or-corona-virus-live-c297526f8b44 "https://koukia.ca/public-and-open-source-api-to-track-development-of-covid19-or-corona-virus-live-c297526f8b44")

Today I put together an Azure Logic App to publish the latest development statistics that comes from the following API on Twitter with the new Twitter account that I created for this purpose.

The following is the API that I am using in the Azure Logic App which returns the total number of Confirmed, Recovered and Deaths around the world:

<https://coronavirus-tracker-api.herokuapp.com/v2/latest>

The JSON Response for this API looks like the following:

```
{"latest":{"confirmed":304524,"deaths":12973,"recovered":91499}}
```

And the following API is another alternative that update the cases more frequently:

<https://corona.lmao.ninja/all>

And here is the Twitter Account and a sample Tweet that I sent using this Logic App:

**Make sure you follow it so you don’t miss out on things ;)**

What does the Azure Logic App look like?

There are 4 steps in the Logic App:

1. Step one is the trigger, which for now I have set it to run every 30 minutes

![](https://cdn-images-1.medium.com/max/800/1*0durvtsVIPAxEPUEZco9tg.png)

2. Step two is the HTTP call to the public COVID19 API that I mentioned above. The API is pretty simple, so I don’t need any headers or parameters to make a call

![](https://cdn-images-1.medium.com/max/800/1*lrnKUIb_UyFYys6aOMx7ug.png)

3. Step three is to parse the JSON output that comes out of the API call from the previous step. To do that I use the Pars JSON Action. This step needs the JSON schema to parse the Body from the previous step. You can either build the schema manually, or paste a sample response there and it will create the schema for you.

![](https://cdn-images-1.medium.com/max/800/1*v0SoSrk075GO7NR1V_KPww.png)

4. And the last step is to Tweet some text using the parsed response from the previous step. To make this Tweet step happen, you would need to authenticate with twitter using the twitter account that you want to post these messages.

![](https://cdn-images-1.medium.com/max/800/1*0cJtQXRBs4JYh4TtcOWArg.png)

This is how the whole Logic App Workflow looks like in the end:

![](https://cdn-images-1.medium.com/max/800/1*QOj4RSTm04-rifE8W0Z-Sg.png)

That’s it! you can do similar things if you have other ideas. You can put such thing together in as little as 20 minutes!

You can find the source code of the Azure Logic App here on Github:

[**aramkoukia/covid19-development-twitter-azure-logic-app**  
*An Azure Logic App that makes API calls to get latest statistics on COVID19 developments around the world and publishes…*github.com](https://github.com/aramkoukia/covid19-development-twitter-azure-logic-app "https://github.com/aramkoukia/covid19-development-twitter-azure-logic-app")

If like me need a lot if distraction these days, here is a very good coloring book for adults that helps a lot:

<https://amzn.to/2wqgE64>

[![](https://cdn-images-1.medium.com/max/800/0*E7dutayGae3I_56-.jpg)](https://amzn.to/2wqgE64)*A Swear Word Coloring Book for Adults: Sweary AF: F\*ckity F\*ck F\*ck F\*ck*

> If you liked this article, click the👏 below so other people will see it here on Medium.

> Let’s be friends on [Twitter](https://twitter.com/aramkoukia). Happy Coding :)

Cheers and #StaySafeStayHome everyone!
