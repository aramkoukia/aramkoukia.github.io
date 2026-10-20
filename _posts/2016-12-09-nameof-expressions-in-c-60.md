---
layout: post
title: "nameof Expressions in C# 6.0"
date: 2016-12-09
description: "There is a very nice feature in C# 6.0 which will help us to remove a lot of “Magic Strings“ from our code."
image: /assets/img/2016-12-09-nameof-expressions-in-c-60/1.png
medium_url: https://medium.com/@aramkoukia/nameof-expressions-in-c-6-0-1e36859d4a7b
---

### nameof Expressions in C# 6.0

![](/assets/img/2016-12-09-nameof-expressions-in-c-60/1.png)

There is a very nice feature in C# 6.0 which will help us to remove a lot of “Magic Strings“ from our code.

I’m sure you use a lot of magic strings and it is completely normal to have them in cases like throwing an ArgumentNullException to mention the argument name. so the issue with that is when your argument is changed in the method, and you forget to update the magic string that represents the changed argument, your error will show an argument is null that does not exist in the code!

```
void MyFunction(string argument) {   // Handle null argument.  if (argument == null) {     throw new ArgumentNullException("argument"); }}
```

And some other samples where raising OnPropertyChanged events where you have to call out what is the property that has changed and I bet you don’t like to do it with a magic string, because that property name could change and you might easily forget to update the magic string because the compiler will not complain about it. (You can find out about the miss match if you have unit tests for the body of your POCO classes which I doubt it!)

```
public string PersonName {    get { return name; }    set { name = value;          // Call OnPropertyChanged whenever the property is updated      OnPropertyChanged("PersonName");       } }
```

Now, with introducing the “nameof” expression in C# 6.0, you can remove the magic stings and let the compiler take care of the refactoring that you do!

Here is how the above code snippet will look like using the nameof expression:

```
void MyFunction(string argument) {    // Handle null argument.   if (argument == null) {        throw new ArgumentNullException(nameof(argument);   } }
```

The nameof expression only retrieves the final identifier, even if you use the fully qualified names. Also, in the case of attributes, the “Attribute” suffix isn’t implied. Instead, it’s required for compilation.

I think we can use this feature to to clean up some messy code.
