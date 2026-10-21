---
layout: post
title: "Amazon SQS vs Amazon SNS"
date: 2021-10-14
description: "Amazon SQS and Amazon SNS are the two popular tools when engineers design distributed systems in the AWS echo-system."
image: https://cdn-images-1.medium.com/max/800/1*F6BSGn5fN3fY7KWeptm9OA.png
tags: ["AWS", "Architecture"]
---

### Amazon SQS vs Amazon SNS

![](https://cdn-images-1.medium.com/max/800/1*F6BSGn5fN3fY7KWeptm9OA.png)*Image from: <https://beabetterdev.com/>*

Amazon SQS and Amazon SNS are the two popular tools when engineers design distributed systems in the AWS echo-system.

It can be useful if we understand what are the similarities and differences between these tools, so I thought I put this together to use when you are making a decision on which service fits your use-case better.

Event Bridge is also a third tool within AWS which can be used for messaging technologies in distributed systems. So I have compiled a list of their differences below:

#### Amazon SQS:

- Used for Application to Application messaging
- Communication Channel: Queue
- Pull/Poll mechanism
- Typical queueing, producer/consumer paradigm
- 14 days message retention
- Two variants, Standard and FIFO
- Guarantees exactly delivery
- Maximum Message Size: 256 KB.
- Provides no message filtering
- Supports Cross-Region messaging
- Does not support Message Schema Registry

#### Amazon SNS:

- Used for Application to Application messaging as well as application to Person notification
- Communication Channel: Queue
- Push mechanism with retry
- Publisher/Subscriber messaging
- 14 days message retention
- Two variants, Standard and FIFO
- Guarantees at least once delivery
- Maximum Message Size: 256 KB.
- Provides some message filtering
- Supports Cross-Region messaging
- Does not support Message Schema Registry

#### Event Bridge:

- Used for Application to Application integration
- Communication Channel: Event Bus
- Rule Based routing for pushed events
- Application Integration Framework
- Events can be retained and archived forever
- Does not guarantee ordering
- Guarantees at least once delivery
- Maximum Message Size: 256 KB.
- Provides some message filtering
- Supports Cross-Region messaging
- Supports Message Schema Registry

Hope this short summary helps you to select the right tool.

Cheers!
