---
layout: post
title: "What does the “yield” keyword do in python?"
date: 2023-01-19
description: "In Python, the “yield” keyword is used in the body of a function definition. When a function is called with a “yield” statement, it returns…"
image: https://cdn-images-1.medium.com/max/800/0*B1rQIcFPUzcv9vku.png
---

### What does the “yield” keyword do in python?

![](https://cdn-images-1.medium.com/max/800/0*B1rQIcFPUzcv9vku.png)*Image from <https://betterprogramming.pub/>*

In Python, the “yield” keyword is used in the body of a function definition. When a function is called with a “yield” statement, it returns a generator object, but does not start execution immediately. The code in the function is executed only when the generator’s next() method is called. Each time the yield statement is executed, the function’s state is saved and the function is suspended, so that when the function is later resumed, execution continues from the point at which it was suspended. This allows the function to produce a series of values over time, rather than computing them all at once and returning them in a list, for example.

Here’s an example of a simple function that uses the “yield” keyword:

```
def simple_generator():    yield 1    yield 2    yield 3for i in simple_generator():    print(i)
```

This will output:

```
123
```

Here’s another example that uses a loop to generate a sequence of numbers:

```
def count_up_to(max):    count = 1    while count <= max:        yield count        count += 1for num in count_up_to(5):    print(num)
```

This will output:

```
12345
```

It’s important to note that when a generator function is called, it returns a generator object, but does not start execution immediately. The code in the function is only executed when the generator’s next() method is called. In the above examples, the for loop called the generator’s next() method behind the scene and that’s why the code inside the function was executed.
