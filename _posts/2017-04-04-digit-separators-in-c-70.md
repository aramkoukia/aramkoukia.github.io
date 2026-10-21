---
layout: post
title: "Digit separators in C# 7.0"
date: 2017-04-04
description: "In C# 7.0, the underscore _ may be used as a digit separator. The benefit of this is to improve the code readability when dealing with…"
image: https://cdn-images-1.medium.com/max/800/1*YW_1ZyOQ5FAxkPUokyhqDw.jpeg
tags: [".NET"]
---

### Digit separators in C# 7.0

![](https://cdn-images-1.medium.com/max/800/1*YW_1ZyOQ5FAxkPUokyhqDw.jpeg)

In C# 7.0, the underscore `_` may be used as a digit separator. The benefit of this is to improve the code readability when dealing with numbers.

**Though some might argue that, what the hell is a “*magic number*” is even doing in the code anyways!**

The underscore may occur anywhere in a numeric literal except as noted below. Different groupings may make sense in different scenarios or with different numeric bases.

Any sequence of digits may be separated by one or more underscores. The `_` is allowed in decimals as well as exponents. The separators have no semantic impact - they are simply ignored.

```
int bin = 0b1001_1010_0001_0100;int hex = 0x1b_a0_44_fe;int dec = 33_554_432;int weird = 1_2__3___4____5_____6______7_______8________9;double real = 1_000.111_1e-1_000;
```

**Where the** `_` **digit separator may not be used:**

- at the beginning of the value (`_121`)
- at the end of the value (`121_` or `121.05_`)
- next to the decimal (`10_.0`)
- next to the exponent character (`1.1e_1`)
- next to the type specifier (`10_f`)
- immediately following the `0x` or `0b` in binary and hexadecimal literals ([might be changed to allow e.g. 0b\_1001\_1000](https://github.com/dotnet/roslyn/issues/12680))

Cheers!
