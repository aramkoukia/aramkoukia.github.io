---
layout: post
title: "C# String Interpolation, Performance test"
date: 2017-05-20
description: "C# 6.0 introduced a cool feature called String Interpolation, which is an awesome replacement for confusing String.Format syntax, to make…"
image: https://cdn-images-1.medium.com/max/800/1*MMX1cc8OyZ6ddbNpVMwNSg.gif
medium_url: https://medium.com/@aramkoukia/c-string-interpolation-performance-test-73ae6ab27276
---

### C# String Interpolation, Performance test

![](https://cdn-images-1.medium.com/max/800/1*MMX1cc8OyZ6ddbNpVMwNSg.gif)

C# 6.0 introduced a cool feature called [String Interpolation](https://koukia.ca/string-interpolation-in-c-6-0-b049439f6727), which is an awesome replacement for confusing String.Format syntax, to make them more readable.

Then, I came to realize in some code that it makes it much readable when I use this syntax for string concatenations as well.

But then I thought, let me try and compare the performance of this, and the good old String Builder and also normal string Concat using ‘+’ to make sure it is fast enough.

> Though, the String Interpolation, is really supposed to be an alternative to String.Format, if you happen to consider using it as String Concat , or like String Builder to build big dynamic strings, make sure this syntax is scalable enough for your need.

Again, you might think, why would someone want to use String Interpolation for building big Dynamic String, and I totally agree with that, but believe it or not some people just use things just because they are new

**Remember the guy who had a hammer and tries to build everything with that? I know a few of them! In this case the String Interpolation is the hammer…**

The following is a simple code I have, with a bunch of “for loops” with 100,000 iterations for each test:

And I was really surprised to see that interpolation is the **slowest of all**.

Here is the result for 100,000 iterations:

**String Interpolation took: 4,578 milliseconds**

**String concat with ‘+’ took: 2,090 milliseconds.**

**String Builder took: 1 milliseconds.**

So, if you have iterations, or building big strings, make sure you don’t use the “*good looking”* String Interpolation syntax.

UPDATE: I got a lot of responses on [reddit](https://www.reddit.com/r/csharp/comments/6cckob/c_string_interpolation_performance_test/) about the “Proper Benchmark”, or “Why would you even want to use String.Format to build big dynamic strings” which I agree with almost all of them. Also lots of people mentioned that the conclusion is right, though the results might not be as accurate, which I agree again.

While I will try to use a proper benchmark to get more accurate result and publish it here, the bottom line conclusion here is:

> String Interpolation (Good looking version of String.Format) is not suitable for building big blocks of strings (Using String.Concat or String Builder), with lots of iterations, and make sure you limit the use of it to replace String.Format.

Cheers!
