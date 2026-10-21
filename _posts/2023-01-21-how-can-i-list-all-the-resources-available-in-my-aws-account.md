---
layout: post
title: "How can I list all the resources available in my AWS account?"
date: 2023-01-21
description: "This used to be a really hard problem on AWS but not anymore (At least for most of the resource types)."
image: https://cdn-images-1.medium.com/max/800/0*f6U7Z5d-HOPL-y_4.png
tags: ["AWS"]
---

### How can I list all the resources available in my AWS account?

![](https://cdn-images-1.medium.com/max/800/0*f6U7Z5d-HOPL-y_4.png)

This used to be a really hard problem on AWS but not anymore (At least for most of the resource types).

AWS Resource Explorer is a tool that allows you to explore and discover the resources in your AWS account. It allows you to view, search, and filter the resources across all regions and services in your AWS account.

You can use the Resource Explorer to list all the resources available in your AWS account by following these steps:

1. Go to the AWS Resource Explorer website (<https://aws.amazon.com/resource-explorer/>)
2. Sign in to your AWS account if prompted.
3. On the homepage, you will see a list of all the services that are supported by Resource Explorer.
4. Select the service that you want to view resources for.
5. You can use the search bar or filter options to narrow down the list of resources.
6. The resources will be displayed in a tree-like structure, you can click on a resource to view more information about it.

You can also use the AWS CLI or SDKs to access the Resource Explorer.

`aws resource-explorer list-resources` command in the AWS CLI can be used to list all the available resources in the account.

To use the AWS SDK, you can use the SDK’s API calls to list the resources available in your account.

It’s important to note that the Resource Explorer is a relatively new service and not all resources and services are available on it yet.
