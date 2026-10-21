---
layout: post
title: "#Azure Application Insights Analytic or Kusto"
date: 2016-12-09
description: "Azure Application Insights is a great tool that I find super useful when I need to get some insights about what’s going on with my…"
image: /assets/img/2016-12-09-azure-application-insights-analytic-or-kusto/1.png
tags: ["Azure", "Data"]
---

### #Azure Application Insights Analytic or Kusto

Azure Application Insights is a great tool that I find super useful when I need to get some insights about what’s going on with my application (It can be a Website, Web App, WEB API, Windows/Desktop App) and the good point is, your application doesn’t even need to be hosted in Azure, and you can just collect instrumentation data in your Azure Application Insights.

In this post we are going to move even further and use Azure Application Insights Analytic or Kusto to dig deeper into out telemetry data.It is very easy to setup the Azure Application Insights and you can go through this article on how to get started because my focus is not the setup of the Application Insights in this post:

<https://azure.microsoft.com/en-us/documentation/articles/app-insights-get-started/>

When you setup your Application Insights you can go to Azure Portal and see the Dashboard of your app which by default will have some charts and some high level info about the status of your application:

![](/assets/img/2016-12-09-azure-application-insights-analytic-or-kusto/1.png)

And then you can even drill down into any of the sections in the App Insights dashboad to see more details about the requests, slow responses and errors etc:

![](/assets/img/2016-12-09-azure-application-insights-analytic-or-kusto/2.png)

To get into the Azure Application Insights Analytic tool or Kusto, there is a button on the dashboard that says “Analytic” so you just simply click on that and you are taken to the Kusto page which looks like this:

![](/assets/img/2016-12-09-azure-application-insights-analytic-or-kusto/3.png)

In this page on the top is the place where you can add your queries and run them and at the bottom there are some samples that can give you some jump start queries to get an idea about the Kusto query language (Yeah you gotta learn a new query language, but don’t worry it is very simple and there are good documentation as far as I can tell).

So yes, there you have it. you can start digging into your telemetry data and for sure you will be very impressed by the performance of the results you get back! yeah it is super fast…

You can start by simple queries like below and click on GO to test them. When you run the query you will see the result in the grid below and for the cases where the columns are Json objects you can expand them and see the details (comes very handy in cases where you are looking at exception information).

![](/assets/img/2016-12-09-azure-application-insights-analytic-or-kusto/4.png)

If you notice, there is a little chart icon on top of the results pane on the middle of the page, where you can switch the view to show you a chart if your query is in a way that show a chart makes sense of course. So I just make a little modification to the query to be able to show the result as a chart and there you see it like this:

![](/assets/img/2016-12-09-azure-application-insights-analytic-or-kusto/5.png)

It’s for sure one of the best features Azure has added so far which will be very useful when you are going to dig into historical data and this will come really handy because it is really fast.

If you need more information about the Kusto query language you can find the documentation here:

<https://azure.microsoft.com/en-us/documentation/articles/app-insights-analytics/>
