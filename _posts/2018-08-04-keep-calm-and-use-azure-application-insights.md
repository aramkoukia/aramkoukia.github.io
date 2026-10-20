---
layout: post
title: "Keep Calm and use Azure Application Insights"
date: 2018-08-04
description: "If you have been following me here, I started writing about Azure Application insights 4 or 5 years ago on my blog when it first came out…"
image: https://cdn-images-1.medium.com/max/800/1*wpL7UdybtpENsATgFDjtpQ.png
medium_url: https://medium.com/@aramkoukia/keep-calm-and-use-azure-application-insights-ff38e04a43fd
---

### Keep Calm and use Azure Application Insights

![](https://cdn-images-1.medium.com/max/800/1*wpL7UdybtpENsATgFDjtpQ.png)*Azure Application Insights (Image from MSDN blog)*

If you have been following me here, I started writing about Azure Application insights 4 or 5 years ago on my blog when it first came out and I was really impressed by its power even then, but now after several years, I think it has made a lot more improvements so it’s time for another closer look and some of the new features it has.

#### Setting up Azure Application Insight is Simple

Azure Application Insights provides a **SIMPLE** way for engineering teams to gather live telemetry from web apps and services for real time monitoring and diagnostics.

Let me say it again:

**Application Insights is so SIMPLE to setup and use! it’s unbelievable:**

[**Set up web app analytics for ASP.NET with Azure Application Insights**  
*Configure performance, availability, and user behavior analytics tools for your ASP.NET website, hosted on-premises or…*docs.microsoft.com](https://docs.microsoft.com/en-us/azure/application-insights/app-insights-asp-net "https://docs.microsoft.com/en-us/azure/application-insights/app-insights-asp-net")

I am going to show you how you can proactively detect and diagnose issues, get actionable insights by machine learning and ad-hoc analytics and how to setup monitoring for your apps.

Traditionally application monitoring has been an after thought. We used to not think about monitoring before issues start popping up! But with the current modern architectures like Microservices or so many multi-tier applications out there, we need to infuse monitoring into our application development life-cycle from the get go, starting from planning, to development, test and release.

That way you can identify issues and optimizations required as part of the pre and post production process and iterate your tuning continuously, and incidentally, that’s what DevOps is all about!

**How does Application Insights makes all of this easier?**

You can create very advanced Azure Dashboard with various metrics pinned into it from your Azure Application Insights.

![](https://cdn-images-1.medium.com/max/1200/1*SMndLY4LvQXMpPZTpH5Iqw.png)*A sample Azure Dashboard with various Azure App Insight metrics*

Such a dashboard can help you detect and discover issues that impacts your production environment as well as subsequently your customers. Now we are targeting engineering teams rather than IT ops team so see how engineering teams can benefit from this, because we want to give monitoring and diagnostics capabilities to developers as they are building their apps and services.

Now as an example, in the following metric, you can see both client side and server side performance metrics as well as failures in one single view:

![](https://cdn-images-1.medium.com/max/800/1*x4WO8o53epXnIZgJtTfRlw.png)

We also want to make sure that product owners get that useful telemetry while they are working on their feature prioritization. As an example here they can see the usage of their application and they can also discover what their most popular pages.

![](https://cdn-images-1.medium.com/max/800/1*XDHKMj_fdF9vaJpGRvVJbQ.png)*Application and Feature Usage metrics*

![](https://cdn-images-1.medium.com/max/800/1*g7b4vZNO8lAteeR4ONIyog.png)*Slowest pages metrics*

![](https://cdn-images-1.medium.com/max/800/1*hlKPnBFdU1B5SZxFMnlLog.png)*Most Popular Pages metrics*

One more important thing here is you can easily adopt Application Insights with all the SDKs available for different kind of applications that you might have in .Net, .Net Core, Java, Python or Nodejs.

So the Operations team no longer need to go and install an agent on a server to get monitoring up and running.

With all this you can be sure that both your development team and IT are ahead of issues that come up in your production environments.

**How would I use all of this?**

Alright let’s see how we can detect and fix issues in production using this dashboard using the Application Map on our dashboard.

This Application Map gives us a topology view of our entire system and shows all the server side and client side dependencies in one single view.

![](https://cdn-images-1.medium.com/max/1200/1*vy4d0AntWThD9SsyY4JtWw.png)*Application Map from the dashboard*

In this view you can see that some of the service dependencies are not in a healthy state (*that little red icon on the bottom left of each box on the above image*). If I want to dig deeper I can click on the box and see the issues.

In this case let’s click on the Azure Table and see what’s going on:

![](https://cdn-images-1.medium.com/max/800/1*5TxKQxWvCdVbhwgfK_nVMg.png)*Details of the Azure Table components*

As you can see there are 3 errors that has happened that you can see in the above image. Now you cant to see what’s going on with the first error from the list. Just click on it to see more details.

![](https://cdn-images-1.medium.com/max/800/1*chND6M0wGTsLMi2Ez5NMlA.png)

Ah, I see a *409 error* happening but why? Ok let’s click on the “*All available telemetry for this operation*” to see why we are getting this error.

![](https://cdn-images-1.medium.com/max/800/1*a-2NiU486pA6Fh6Taw8tOg.png)*Looking at all the telemetry or an operation in Application Insights*

Here we go, we can see all the related traces and errors related to that API call and you can see the exception right at the top what is a validation exception around Zip Codes, but why is this happening?

Lets click on the exception to see if we can get more details:

![](https://cdn-images-1.medium.com/max/800/1*zXHPF2R2iFQ06MckMGD60A.png)*Error Details and Stack Trace in Application Insights*

Cool, I can see where exactly the error is happening (**in which page, and what’s the line number**)

Awesome, now I have the stack trace and everything, let’s create a bug for the team to fix this issue. How? easy, just click on the “New Work Item” and create the work item with all the details and assign it to the respective team to fix it!

![](https://cdn-images-1.medium.com/max/800/1*XArrHqtgJKJiRhcnUazbHA.png)*Creating a bug from an Exception in Azure Application Insights*

#### Can this help me find performance problems?

Yes! If you go back to the dashboard and look at the section that shows server side and client side performance and say you notice that the service is performing slower than expected.

![](https://cdn-images-1.medium.com/max/800/1*x4WO8o53epXnIZgJtTfRlw.png)*Looks like Server Response time is slow!*

Seems like Server Response times are slow (~ 900 ms) and we want to know if we can identify the root cause.

Let’s click on the Server Response to see more details.

![](https://cdn-images-1.medium.com/max/800/1*jPUjZxZ5p0AdIN3_VXgj5w.png)

As you can see the most popular operation is *GET Home/Index* that is some cases it takes just under 2 seconds to respond. now if we click on it, we can go to the profiler and see what’s going on there:

![](https://cdn-images-1.medium.com/max/1200/1*N1I-sybpreqtn_3b_h747A.png)*Method Profiling in Auzre Application Insights*

From the profiler it is obvious that one particular line was blocked most of the time and also on top of the page you might even get some performance tips to make you code faster in these areas!

I hope you enjoy working with Application Insights as much as I do!

Cheers!
