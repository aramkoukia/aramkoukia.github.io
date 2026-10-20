---
layout: post
title: "Using IL Weaving (PostSharp) for a cleaner code (AOP)"
date: 2016-12-09
description: "You might have read this post that I wrote a while back about Clean Code and using Interceptors to do some aspect oriented programming…"
image: /assets/img/2016-12-09-using-il-weaving-postsharp-for-a-cleaner-code-aop/1.jpg
---

### Using IL Weaving (PostSharp) for a cleaner code (AOP)

![](/assets/img/2016-12-09-using-il-weaving-postsharp-for-a-cleaner-code-aop/1.jpg)

You might have read [this post](https://koukia.ca/using-an-interceptor-for-a-cleaner-code-aop-c3c1f5e9d411) that I wrote a while back about Clean Code and using Interceptors to do some aspect oriented programming (AOP). Today I wanted to show you how to do the same thing with a different approach which is called IL Weaving technique. That means you are going to use some tool to attach your cross cutting code to the assembly when you build your assembly. this way your code will be added to the places you want inside of your function while you build your project and your base like code will stay clean.

There are number of tools for IL Weaving in .Net world like PostSharp, Loom.net and Wicca, but now I’m going to use PostSharp to show you how it works and what you can accomplish with it.

IL Weaving has 2 main steps.

First we are going to compile our application into a dll or exe file and then run the exe or dll through the AOP processor and the processor will figure out where these aspects should be appended within your code. Then it generates the new code base at an IL level and inserts the codes where you have configured them to be.

The output of the AOP Post processor is again a dll or exe with the exact same name that you passed to it. The difference is that it has all your aspect related code around the original code that you passed in.

There are 2 main steps for this to be done:

Step 1: Create a class to contain our aspect code. This class will inherit from a base class provided by the AOP framework we use (in my case it is [PostSharp](https://www.postsharp.net/)).

Step 2: Attach this aspect class to the original code.

For example let’s say we have this simple console app which has a main function that looks like this:

```
namespace PostSharpSample { class Program {     static void Main(string[] args)     {        try        {           var obj = new MyClass();           obj.DoSomething("test AOP");        }        catch (Exception) { }
```

```
Console.ReadKey();     } } }
```

Now we can create our Aspect class and I’ll call it LoggingAspect.cs. To do that, first I’m going to add a reference to PostSharp dll to my project. (you can download PostSharp from [here](https://www.postsharp.net/download) or get it from nuget packages)

This class is going to inherit from “OnMethodBoundaryAspect” that looks like a decorator pattern. This class is in PostSharp.Aspects namespace.

And within this aspect there are number of hook points that you might be interested in. So you can simply override the methods for those hook points that you want to use.

These are the hook points that you can use (PostSharp v 4.0.41)

```
public virtual void OnEntry(MethodExecutionArgs args);
```

Method executed before the body of methods to which this aspect is applied.

```
public virtual void OnException(MethodExecutionArgs args);
```

Method executed after the body of methods to which this aspect is applied, in case that the method resulted with an exception.

```
public virtual void OnExit(MethodExecutionArgs args);
```

Method executed after the body of methods to which this aspect is applied.

```
public virtual void OnResume(MethodExecutionArgs args);
```

Method executed when a state machine resumes execution after an yield return or await statement.

```
public virtual void OnSuccess(MethodExecutionArgs args);
```

Method executed after the body of methods to which this aspect is applied, but only when the method successfully returns (i.e. when no exception flies out the method.).

```
public virtual void OnYield(MethodExecutionArgs args);
```

Method executed when a state machine yields, as the result of an yield return or await statement.

In all of these methods the args parameter will give you information about the method that is getting called from your code base, or the exception and many more info that you might need inside your aspect class.

Here is how our Aspect class will look like in the first cut, overriding 4 of the methods mentioned above:

```
namespace PostSharpSample { [Serializable] [MulticastAttributeUsage(MulticastTargets.Method, TargetExternalMemberAttributes = MulticastAttributes.Instance)] public class LoggingAspect : OnMethodBoundaryAspect {     public override void OnEntry(MethodExecutionArgs args)     {         Console.WriteLine("On Entry");     }     public override void OnExit(MethodExecutionArgs args)     {         Console.WriteLine("On Exit");     }     public override void OnException(MethodExecutionArgs args)     {         Console.WriteLine("On Exception");     }     public override void OnSuccess(MethodExecutionArgs args)     {         Console.WriteLine("On Success");     } } }
```

Note that for this to work the aspect class needs to be serializable, so we add the Serializable attribute to the Aspect class as you can see in the above code.

Now we can attach this logging aspect to any code we want in the project.

Before you do that if you run the application nothing will happen and this is what you will see:

Since we are using IL Weaving it will be hard to tell if our aspect code is attached to our baseline code or not. for that we could use decompilers like ILSpy and check out our assembly code there.

The OnMethodBoundaryAspect class inherits from Attribute class, and because we inherited from OnMethodBoundaryAspect class, so our LoggingAspect class is already an attribute.

So attaching our aspect class to our functional code is as easy as adding [LoggingAspect] attribute to any class that we want in our project.

```
namespace PostSharpSample { public class MyClass {    [LoggingAspect]     public void DoSomething(string param1)     {        Console.WriteLine(param1);     } } }
```

Now if you compile your application, you will see this as the output:

If you check the output assembly with ILSpy you will see that your aspect code is injected into the places that you hooked into in the aspect class:

You can add this attribute at the method level, class level, but again adding this to all your classes in a large project will be a pain, but there is a way to do it using assembly reference in assemblyinfo.

If you add this attribute at a class level it will be attached to all members including functions, properties and constructors, which might not be what you want, so you can explicitly define which member types you want it to be attached to with a different attribute called “MultiCastAttributeUsage”. say if you want it to be attached only to methods your aspect class decoration will look like this:

```
[Serializable] [MulticastAttributeUsage(MulticastTargets.Method, TargetExternalMemberAttributes = MulticastAttributes.Instance)] public class LoggingAspect : OnMethodBoundaryAspect {
```

Now, in the assepmblyinfo.cs class we can add this line to target the types that we want to attach this aspect class to like this:

```
[assembly: LoggingAspect(AttributeTargetTypes = "PostSharpSample.*")]
```

This will attach our aspect class to all classes in the PostSharpSample namespace.

You can find this sample project on Github here:

<https://github.com/BitsCorner/AOP-PostSharp>

PostSharp has a lot of cool features, which I’ll try to go over and write some of them for your reference, although they have video, and nice documentation in their website too but this might be more practical to have it implemented in a step by step way.
