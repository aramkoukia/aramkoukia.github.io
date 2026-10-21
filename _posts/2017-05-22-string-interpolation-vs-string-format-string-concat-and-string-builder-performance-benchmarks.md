---
layout: post
title: "String Interpolation vs String Format, String Concat and String Builder performance benchmarks"
date: 2017-05-22
description: "I recently did a simple test without using any benchmark framework and wrote about it here, and it turned to a liberal vs conservative…"
image: https://cdn-images-1.medium.com/max/1200/1*WmVaOVTSYvSuQmnUmC6P8g.png
tags: [".NET"]
---

### String Interpolation vs String Format, String Concat and String Builder performance benchmarks

![](https://cdn-images-1.medium.com/max/1200/1*WmVaOVTSYvSuQmnUmC6P8g.png)

I recently did a simple test without using any benchmark framework and [wrote about it here](https://koukia.ca/c-string-interpolation-performance-test-73ae6ab27276), and it turned to a liberal vs conservative debate kind of discussion [on reddit](https://www.reddit.com/r/csharp/comments/6cckob/c_string_interpolation_performance_test/)!

Lots of people commented that, the result might be off because of the test being naive, so here I am spending some time over the long weekend to do this comparison using [benchmarkdotnet.org](http://benchmarkdotnet.org/index.htm).

I wrote 3 classes to compare, String Format, String Concat and String Builder with String Interpolation.

The following are the 3 classes:

### String Interpolation vs. String Format

This class is to compare the String Format with String Interpolation:

Here is the summary of the result:

![](https://cdn-images-1.medium.com/max/800/1*19T_XK8_aoZVpsWGO8sl7g.png)

### String Interpolation vs. String Concat

This class is to compare the String Concat with String Interpolation:

Here is the summary of the result:

![](https://cdn-images-1.medium.com/max/800/1*71VoGwkbXdbZu02HZ3LI3Q.png)

### String Interpolation vs. String Builder

This class is to compare the String Builder with String Interpolation:

Here is the summary of the result:

![](https://cdn-images-1.medium.com/max/800/1*PlfNX2Vl6gCDmMy_Zbdjtw.png)

#### Running the Benchmarks:

And finally, the following is the console app that runs the 3 benchmark classes:

#### Benchmark environment:

The following is the environment in which I run the test on.

> NOTE: It is important to realize that, result will be different if you run the test in a different environment.

```
BenchmarkDotNet=v0.10.6OS=Windows 10 Redstone 1 (10.0.14393)Processor=Intel Core i5–6200U CPU 2.30GHz (Skylake)ProcessorCount=4Frequency=2343755 HzReso+lution=426.6658 ns Timer=TSC[Host] : Clr 4.0.30319.42000, 32bit LegacyJIT-v4.6.1648.0DefaultJob : Clr 4.0.30319.42000, 32bit LegacyJIT-v4.6.1648.0
```

**Result Legends:**  
Mean : Arithmetic mean of all measurements  
Error : Half of 99.9% confidence interval  
StdDev : Standard deviation of all measurements

> Though the test I ran in the [previous post](https://koukia.ca/c-string-interpolation-performance-test-73ae6ab27276) is very much different than this one (it was supposed to test the String Interpolation to see if it can be used effectively in scenarios where we are dealing with large strings), this test is to do benchmark on normal scenarios, to build strings with limited number of variables.

Here is the test project code on [github](https://github.com/aramkoukia/StringInterpolationPerformance/tree/master), in case you want to play with it:

[**aramkoukia/StringInterpolationPerformance**  
*Contribute to StringInterpolationPerformance development by creating an account on GitHub.*github.com](https://github.com/aramkoukia/StringInterpolationPerformance/tree/master "https://github.com/aramkoukia/StringInterpolationPerformance/tree/master")

Cheers!
