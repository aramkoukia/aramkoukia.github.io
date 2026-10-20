---
layout: post
title: "Null-Conditional Operation in C# 6.0"
date: 2016-12-09
description: "Looks like with C# 6.0 we can finally get rid of all those check for Nulls in our code."
image: /assets/img/2016-12-09-null-conditional-operation-in-c-60/1.png
medium_url: https://medium.com/@aramkoukia/null-conditional-operation-in-c-6-0-8fa047b76981
---

### Null-Conditional Operation in C# 6.0

![](/assets/img/2016-12-09-null-conditional-operation-in-c-60/1.png)

Looks like with C# 6.0 we can finally get rid of all those check for Nulls in our code.

Does this snippet of code look familiar?

```
private List<DtoDomain> Map(List<Domains> domains) {    if (domains == null)       return null;
```

```
return domains.Select(domain => new DtoDomain() { DomainName = domain.name, DomainStatus = domain.DomainStatus }); }
```

I’m sure there are tons of this kind of code in your project, now C# 6.0 has a feature to check for Nulls in the same return statement.

This feature is called “Null-Conditional Operation” and the operator looks like: “ ?. ”

And here is how you use it:

```
private List<DtoDomain> Map(List<Domains> domains) {    return domains?.domains.Select(domain => new DtoDomain()    {      DomainName = domain.name, DomainStatus = domain.DomainStatus      }); }
```

This operator works very simply and basically what it does is it proceeds to the right hand of the .? if the left hand of the .? is not null, and if it is null then the statement will return null.

Another common code pattern that you see in your code is when you are invoking a Delegate, say your existing code looks like this:

```
class Employee {    event EventHandler<float> OnStatusChanged;    private int _Salary;    public int _Salary {       get { return _Salary; }       set {              // If there are any subscribers, then notify them of changes in salary             EventHandler<float> localOnChanged = OnSalaryChanged;             if (localOnChanged != null)             { _Salary = value;               // Call subscribers               localOnChanged(this, value);             }           }    } }
```

Once you start using the Null-Conditional Operation, your code will look like this:

```
OnTemperatureChanged?.Invoke(this, value)
```

The Null-Conditional Operation has another syntax that is just with a “?” which is for checking for Nulls in collection index operator. the usage for that is in case where you want to check if an element in a collection is Null.

Here is a sample code that does Null check in a collection:

```
foreach (int index in indexes) {  var item = collection?[index]; // Do something with item }
```

I hope we can have our code cleaned with this feature of C# 6.0.
