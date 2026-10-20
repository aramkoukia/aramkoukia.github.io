---
layout: post
title: "How do I give access to a third party application to access my AWS account in a read-only mode?"
date: 2023-01-31
description: "To give a third-party application read-only access to your AWS account information, you can use the AWS Identity and Access Management…"
image: https://cdn-images-1.medium.com/max/800/0*K2xa6s0s_8JxD37E.png
---

### How do I give access to a third party application to access my AWS account in a read-only mode?

![](https://cdn-images-1.medium.com/max/800/0*K2xa6s0s_8JxD37E.png)*Image from [mps360.com](https://www.msp360.com/)*

To give a third-party application read-only access to your AWS account information, you can use the AWS Identity and Access Management (IAM) service. Here are the steps:

1. Create an IAM user for the third-party application with read-only permissions.
2. Attach a policy to the user that grants read-only access to the AWS resources you want the third-party application to access.
3. Generate an AWS Access Key ID and Secret Access Key for the user, which the third-party application can use to authenticate API requests.
4. Provide the third-party application with the AWS Access Key ID, Secret Access Key, and the AWS region to be used.

Note: Be cautious when granting access to a third-party application and make sure to review the permissions you are granting and the data that will be accessible.
