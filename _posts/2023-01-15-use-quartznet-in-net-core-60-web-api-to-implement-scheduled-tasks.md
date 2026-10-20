---
layout: post
title: "Use quartz.net in .net core 6.0 web api to implement scheduled tasks"
date: 2023-01-15
description: "To use Quartz.NET in a .NET Core 6.0 Web API, you’ll need to first install the Quartz.NET package in your project. You can do this by…"
image: https://cdn-images-1.medium.com/max/800/0*J52KVDHQADEOjS0R.png
---

### Use quartz.net in .net core 6.0 web api to implement scheduled tasks

![](https://cdn-images-1.medium.com/max/800/0*J52KVDHQADEOjS0R.png)*Logo from <https://www.quartz-scheduler.net/>*

To use Quartz.NET in a .NET Core 6.0 Web API, you’ll need to first install the Quartz.NET package in your project. You can do this by adding the following line to your project’s `.csproj` file:

```
<PackageReference Include="Quartz" Version="3.0.7" />
```

Then, in the Startup class of your Web API, you’ll need to configure Quartz.NET by adding the following code to the `ConfigureServices` method:

```
services.AddQuartz(typeof(MyJob));
```

Where `MyJob` is the class that contains the code for the job you want to schedule.

You will also have to add Quartz.NET’s services to your container.

```
services.AddSingleton<IJobFactory, SingletonJobFactory>();services.AddSingleton<ISchedulerFactory, StdSchedulerFactory>();
```

Once that’s done, you can schedule jobs in your Web API using the `IScheduler` interface, which you can inject into your controllers or other classes using the `AddQuartz` method in Startup.

You will also need to start the scheduler, you can do this by calling the `Start` method on the scheduler in the `Configure` method of the `Startup` class after you configure the services.

```
app.ApplicationServices.GetService<IScheduler>().Start();
```

You can also schedule jobs using the `IJobDetail` and `ITrigger` interfaces.

You should also keep in mind that Quartz is a library for scheduling jobs, it does not handle the job execution itself, for that you have to create a class that implements the IJob interface, this class is what you will pass to the AddJob method.
