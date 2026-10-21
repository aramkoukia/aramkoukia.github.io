---
layout: post
title: "Using Microsoft Unity Interceptor for a cleaner code (AOP)"
date: 2016-12-09
description: "If you have read the past 2 posts of mine here and here, they are about some techniques to have a Cleaner Code. This post is yet another…"
image: /assets/img/2016-12-09-using-microsoft-unity-interceptor-for-a-cleaner-code-aop/1.jpg
tags: ["Architecture", ".NET"]
---

### Using Microsoft Unity Interceptor for a cleaner code (AOP)

![](/assets/img/2016-12-09-using-microsoft-unity-interceptor-for-a-cleaner-code-aop/1.jpg)

If you have read the past 2 posts of mine [here](https://koukia.ca/using-il-weaving-postsharp-for-a-cleaner-code-aop-b909aae2bcd3) and [here](https://koukia.ca/using-an-interceptor-for-a-cleaner-code-aop-c3c1f5e9d411), they are about some techniques to have a Cleaner Code. This post is yet another way to accomplish a similar thing( implementing some cross cutting components) Using Microsoft Unity Interceptor application block.

The good thing about this approach is, it does not need any third party component that the other two ways required (I tried [PostSharp](https://www.postsharp.net/) IL Weaving and [CastleWindsor](http://docs.castleproject.org/Default.aspx?Page=MainPage&NS=Windsor&AspxAutoDetectCookieSupport=1) in the previous posts and they both need licenses) but with Microsoft Unity Interceptor all you need is the Unity and Unity Interception dlls from Nuget packages that you can get them for free.

When you create your project, you need to add Nuget package for Unity Interceptor package like this:

For starters just like my previous demos, I will use one simple console application and as normal IoC(Inversion of Control) patterns that we ALWAYS write our code against interfaces(for so many reasons), our functional code and it’s interface will look like this:

```
namespace AOP_UnityInterceptor { class Program {    static void Main(string[] args)    {       var myClassInstance = new MyClass();       var result = myClassInstance.DoSomething("input1", "input2");       Console.WriteLine(result);       Console.ReadLine();    } } }
```

Now, we really don’t want to have a hard dependency on a concrete class (the line that says: new MyClass();) so we are going to use Unity Container here to create an instance of the class like this:

```
var myClassInstance = container.Resolve<IMyClass>(); var result = myClassInstance.DoSomething("input1" , "input2");
```

And here is the class that actual magic happens in it: the Aspect class, where we can intercept all the requests to the members of the interface that we want to intercept:

```
namespace AOP_UnityInterceptor { public class LoggingAspect : IInterceptionBehavior {     public IMethodReturn Invoke(IMethodInvocation input, GetNextInterceptionBehaviorDelegate getNext)     {       // Before invoking the method on the original target.         WriteLog(String.Format("Invoking method {0} at {1}",   input.MethodBase, DateTime.Now.ToLongTimeString()));
```

```
// Invoke the next behavior in the chain.       var result = getNext()(input, getNext);
```

```
// After invoking the method on the original target.       if (result.Exception != null)       {           WriteLog(String.Format("Method {0} threw exception {1} at {2}", input.MethodBase, result.Exception.Message, DateTime.Now.ToString()));        }        else        {           WriteLog(String.Format("Method {0} returned {1} at {2}", input.MethodBase, result.ReturnValue, DateTime.Now.ToString()));        }               return result;     }         public IEnumerable GetRequiredInterfaces()     {        return Type.EmptyTypes;     }     public bool WillExecute  { get { return true; } }         private void WriteLog(string message)     {         Console.WriteLine("LOG:" + message);     }   } }
```

As you noticed our Aspect class need to implement the IInterceptionBehavior interface which has these 3 members:

```
container.AddNewExtension(); container.RegisterType( new Interceptor(), new InterceptionBehavior() );
```

Now the final look of the Program class of the Console app will be like this:

```
namespace AOP_UnityInterceptor { class Program {   static void Main(string[] args)   {       var container = new UnityContainer();          container.AddNewExtension<Interception>();        container.RegisterType<IMyClass, MyClass>( new Interceptor<InterfaceInterceptor>(), new InterceptionBehavior<LoggingAspect>());
```

```
var myClassInstance = container.Resolve<IMyClass>();       var result = myClassInstance.DoSomething("input1" , "input2");              Console.WriteLine(result);       Console.ReadLine();    } } }
```

And the final output of the application will look like below image and as you can see, there is the rows that starts with word LOG and they are being printed out from the Aspect class and the other last line is the actual class output.

You can find and download the source code of this sample in Github here: <https://github.com/BitsCorner/AOP-UnityInterceptor>
