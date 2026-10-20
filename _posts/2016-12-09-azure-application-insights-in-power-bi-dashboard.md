---
layout: post
title: "Azure Application Insights in Power BI dashboard"
date: 2016-12-09
description: "Azure Application Insights has become one of the best tools to collect telemetry data for all sort of application from Web to Mobile and…"
image: /assets/img/2016-12-09-azure-application-insights-in-power-bi-dashboard/1.png
---

### Azure Application Insights in Power BI dashboard

Azure Application Insights has become one of the best tools to collect telemetry data for all sort of application from Web to Mobile and Desktop apps, because it is so easy to integrate with (just needs a [Nuget package](https://www.nuget.org/packages/Microsoft.ApplicationInsights.Web) and an Instrumentation key) and it is so fast to query data out of it and drill into all sort of trace details.

Now another amazing product that is trending which is in the Reporting and Business Intelligence tools is the [Microsoft Power BI](https://powerbi.microsoft.com/en-us/) which I’d like to use it to show some of the data that is stored in the Azure Application Insights.

So first of all what you need is to create an Application Insights resource in your Azure subscription and then once you have some data there you can create the Power BI dashboard from it.

Here is a link where you can follow to setup your Azure Application Insights if you don’t have it already: <https://azure.microsoft.com/en-us/documentation/articles/app-insights-get-started/>

This is what your Application Insight dashboard will look like inside of the [Azure Portal](https://portal.azure.com/):

![](/assets/img/2016-12-09-azure-application-insights-in-power-bi-dashboard/1.png)

### How to create the Azure Application Insights Dashboard in Power BI

The first step is to connect to the [Application Insights content pack for Power BI](https://app.powerbi.com/getdata/services/application-insights).

When you click on the above link you see a big yellow Connect button which you should click on:

![](/assets/img/2016-12-09-azure-application-insights-in-power-bi-dashboard/2.png)

Then you will get a popup dialog which you are asked to enter your Application Insights information like: Application Name, Resource Group of your App Insights resource and the Subscription ID that you have the Application Insights on (You can find the Resource Group and Subscription ID in the URL too when you are on the Azure Portal)

![](/assets/img/2016-12-09-azure-application-insights-in-power-bi-dashboard/3.png)

When you enter that information and click Next, you are taken to the authentication page when you click Sign In you should enter the same account information that you login to Azure portal.

![](/assets/img/2016-12-09-azure-application-insights-in-power-bi-dashboard/4.png)

Then the Power BI starts to pull the data from the Azure Application Insights and build your dashboard like below:

![](/assets/img/2016-12-09-azure-application-insights-in-power-bi-dashboard/5.png)

As you can see there are pretty cool information taken out for your Application Insights for you to analyze.

How cool was that?

Now you can click on the Dashboard on the Power BI website and share this with anyone you want.
