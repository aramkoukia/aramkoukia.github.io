---
layout: post
title: "Top 6 ways to search for a string in JavaScript — And performance benchmarks"
date: 2017-06-18
description: "Searching for a sub-string in a string, is one of the most basic operations, that we come across every now and then, and what I usually do…"
image: https://cdn-images-1.medium.com/max/1200/1*japg1CGeoRmskOc5yD0-Xg.jpeg
---

### Top 6 ways to search for a string in JavaScript — And performance benchmarks

![](https://cdn-images-1.medium.com/max/1200/1*japg1CGeoRmskOc5yD0-Xg.jpeg)

Searching for a sub-string in a string, is one of the most basic operations, that we come across every now and then, and what I usually do is, to look into other places in the code and see what others have done and just do the same thing!

Now, I just wanted to bring up some of the most used options that are out there, as well as a performance comparison between them, in case you care about performance, so when it comes to choosing in the future, you know which one is a better choice!

### Show me some code

The following are 6 different ways that I have seen a lot when searching for strings:

### Performance Benchmark

In case you are wondering which one will perform better if the string is too big, **‘regex.test’ is the fastest**, followed by ‘string.search’ from ES6 libraries, and the third place belongs to string.indexof:

![](https://cdn-images-1.medium.com/max/800/1*nDitW4SVYAcSXA7UxHlzIg.png)

The following is the Url for the JavaScript benchmark if you are interested to play with it:

[**JSBEN.CH Benchmarking for JavaScript - is string in string. indexOf vs. regex vs. match vs…**  
*Online JavaScript benchmark tool / playground. Find the best performance and speed up your code!*jsben.ch](http://jsben.ch/5qRcU "http://jsben.ch/5qRcU")

When I changed the benchmark a bit and made the main string 10 times bigger, with the ‘sub-string’ bein repeated 10 times, I see that the regex.test still wins, followed really closely by the string.indexof, and string.search.

[**JSBEN.CH Benchmarking for JavaScript - is string in string. indexOf vs. regex vs. match vs…**  
*Online JavaScript benchmark tool / playground. Find the best performance and speed up your code!*jsben.ch](http://jsben.ch/dNADO "http://jsben.ch/dNADO")

### What happens if you scale it up?

I scale the string, and make it 1000 times bigger (1 million characters, or even 10 million characters), I see that string.indexof is a winner, not by much though!

Here is the result followed by the benchmark, when I made the string, **1 to 10 million characters**:

![](https://cdn-images-1.medium.com/max/800/1*EiqIvI9S9XlvEd2OmMt_og.png)

Benchmark for a very big string and repeating the sub-string 1000 times:

[**JSBEN.CH Benchmarking for JavaScript - is string in string. indexOf vs. regex vs. match vs…**  
*Online JavaScript benchmark tool / playground. Find the best performance and speed up your code!*jsben.ch](http://jsben.ch/bcpVW "http://jsben.ch/bcpVW")

Cheers!
