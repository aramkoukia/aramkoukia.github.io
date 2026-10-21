---
layout: post
title: "Using an Interceptor for a cleaner code (AOP)"
date: 2016-12-09
description: "When it comes to real world software, I think at the end of the day for the development team what is important is to be able to…"
image: /assets/img/2016-12-09-using-an-interceptor-for-a-cleaner-code-aop/1.jpg
tags: ["Architecture"]
---

### Using an Interceptor for a cleaner code (AOP)

![](/assets/img/2016-12-09-using-an-interceptor-for-a-cleaner-code-aop/1.jpg)

When it comes to real world software, I think at the end of the day for the development team what is important is to be able to troubleshoot problems effectively when things go wrong in production and you don’t really have your Visual Studio or any other development environment to be able to debug it, so what we do is that we rely on logs that we do in our code, and we try to have very extensive logs and try to be verbose and log the method calls and what happens in the code as much as we can.

But after doing that you will realize that there is logging statements all over the code and the actual functionality that does the job is lost in between the logging logic there, and that’s the point that we start thinking about [Aspect Oriented Programming](http://en.wikipedia.org/wiki/Aspect-oriented_programming), which in this case basically means to take out the cross cutting concerns (which is logging statements in this case, and you can think of caching and security as some other instances) out of the actual codes!

Here is a very simple pattern that I put together in a console app with a function in it that we have a lot of them in most of our projects(before taking out the confusing log statements) if we want to log all the events that happens in the code we run:

```
public string GetUserName(){ try {   LogWriter("Start Getting the Users...");   Console.WriteLine("Actual logic to get the users is being executed    here.");   LogWriter("Successfully retrieved user information..."); } catch (Exception ex) {    LogWriter("Failed to get user information, with exception: ex...");    throw ex; } finally {    LogWriter("Finished getting the user information... "); } return "Aram Koukia"; }
```

As you see, we have 4 lines of code to log the events there and there is only one line of real functional code and that is the Console.WriteLine(in many cases you don’t need to put the try/catch block in all functions like that, and you might want to let the exception bubble up and catch it in some upper layers of the code, but since you want to log it! you are going to add this kind of block there and throw the exception if you want it to be catched in some other layer).

```
public string GetUserName(){    Console.WriteLine("Actual logic to get the users is being executed here.");    return "Aram Koukia"; }
```

To get rid of all those logs (Having your logging blocks as a separate “Aspect” in your project) one of the options to include your cross cutting concerns in your existing classes is using IoC and Interception using one of the available IoC (Inversion of Control) frameworks.

One of the IoCs that are mature enough and have a powerful Interception implementation is [Castle Windsor](http://docs.castleproject.org/Windsor.MainPage.ashx) and you can get the latest references from Nuget by searching for Castle Windsdor:

Or open Package Manager Console in Visual Studio and run this command:  
PM> Install-Package Castle.Windsor

So as you know from previous experience with any IoC framework, we should have interfaces and implement the interfaces and have some IoC containers and map our Interfaces to our Concrete classes and all that, and so we still have to do the same thing it here (we are probably doing these now), so what we are going to have is something like this:

**Interface for the User class:**

```
public interface IUser {   string GetUserName(); }
```

**Concrete Implementation of the User Class:**

```
public class User : IUser {    public string GetUserName()    {         Console.WriteLine("Actual logic of getting a UserName executing here.");         return "Aram Koukia";    } }
```

**LoggingInterceptor:**

```
public void Intercept(IInvocation invocation) {    try    {       Console.WriteLine("Logging: Function call started");         invocation.Proceed();       Console.WriteLine("Logging: Function call was successful");    }    catch (Exception e)    {        Console.WriteLine("Logging: An exception has occurred");       throw e;    }    finally    {        Console.WriteLine("Logging: Exiting the function call");    } }
```

This is where the actual method interception is happening, and as you can see, the invocation.Proceed() is the actual function call, and you can put your logging (or caching code or any other interception) around it.

As you can see, we can add logging at certain point that we wish, and we can even get some information related to the invocation function, like input params and etc.

If you look at the implementation of the IInvocation interface in Castle.Core.dll you’ll see that it gives you some power to be able to do tons of cool things with it.

**IoC mappings:**

```
public void Intercept(IInvocation invocation) {   try   {     Console.WriteLine("Logging: Function call started");    invocation.Proceed();     Console.WriteLine("Logging: Function call was successful");   }   catch (Exception e)   {     Console.WriteLine("Logging: An exception has occurred");    throw e;   }   finally   {     Console.WriteLine("Logging: Exiting the function call");   } }
```

As you can see in the above snippet, the last line is the part that is actually attaching the Interceptor to the Interface, and Castle has a lot of flexibility here and if you have different Interceptors that you want to attach, you can add them here, or if you have different interfaces and you want to attach all of them to the same Interceptor, you don’t need to mention them one by one and you can use the interface’s Namespace and say, attach your Interceptor to all the interfaces inside a specific Namespace you want.

And if you look at the documentation of the Castle, you can see that you can have the same mapping and resolving done through configuration as well, which is the way I’d do it.

**IoC container resolver:**

```
var user = _container.Resolve<IUser>();
```

In real applications you will put your IoC container codes in one separate class and call them in the application start up point, but in our little console application, it will look like this at the end:

```
public class Program {    private static IWindsorContainer _container;    public static void Main(string[] args)    {        // This part is the IoC Container that just maps the Interface to the Concrete implementation of it        _container = new WindsorContainer();             _container.Register(Component.For<LoggingInterceptor>  ().ImplementedBy<LoggingInterceptor>());         _container.Register(Component.For<IUser>().ImplementedBy<User>().Interceptors(InterceptorReference.ForType<LoggingInterceptor>()).Anywhere); // Getting an instance of the User class          var user = _container.Resolve<IUser>(); user.GetUserName();           Console.ReadKey();     } }
```

That’s it, and now when you run the application, you will see all 3–4 lines of logs in the output and still your actual GetUsers method is clean:

I’ll put this little project in [Github](https://github.com/BitsCorner/Castle-Windsor-Interception), so you can [Clone](https://github.com/BitsCorner/Castle-Windsor-Interception) the final code from there and take a look.

The other way of doing this sort of thing is to use a technique called, IL Weaving, which basically means that, you will use some tool (one of the most famous ones is [PostSharp](http://visualstudiogallery.msdn.microsoft.com/a058d5d3-e654-43f8-a308-c3bdfdd0be4a)) and what it does, is that it will add the logging statements (or any other cross cutting code that you wish) in the ultimate dll or exe file after your compilation is done.
