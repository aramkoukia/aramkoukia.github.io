---
layout: post
title: "How to pass parameters or querystring from API Gateway to AWS Lambda?"
date: 2023-04-16
description: "Amazon API Gateway is a service that allows you to create, manage and secure APIs for your applications. One of the common use cases for…"
image: https://cdn-images-1.medium.com/max/800/1*A5kIemGtjMaAcxs3lZIYxQ.png
tags: ["AWS"]
---

### How to pass parameters or querystring from API Gateway to AWS Lambda?

![](https://cdn-images-1.medium.com/max/800/1*A5kIemGtjMaAcxs3lZIYxQ.png)

Amazon API Gateway is a service that allows you to create, manage and secure APIs for your applications. One of the common use cases for API Gateway is to invoke AWS Lambda functions as backend services for your APIs. In this article, we will learn how to pass querystring or route parameters from your API requests to your Lambda functions using two different types of integrations: proxy and non-proxy.

#### Proxy integration

Proxy integration is the recommended approach for invoking Lambda functions from API Gateway, as it simplifies the configuration and reduces the latency of your API responses. With proxy integration, you can pass the raw request from the client to the Lambda function as-is, without having to define any mapping templates or transformations. The Lambda function can access the request parameters such as headers, query strings, path parameters and body from the event object that is passed as an argument.

#### To enable proxy integration for your API method, follow these steps:

1. Open the API Gateway console and choose your API.
2. Choose the resource and the HTTP method that you want to configure.
3. Choose Integration Request from the method execution panel.
4. Select Lambda Function as the integration type and check the box for Use Lambda Proxy integration.
5. Select the region and the name of your Lambda function and choose Save.

Now you can test your API method using the Test button on the method execution panel. You can enter any querystring or path parameters in the URL and see how they are passed to the Lambda function in the event object.

For example, if you have a GET method for /user/{name} resource and you invoke it with /user/bob?age=25, you will see something like this in the event object:

```
{  "resource": "/user/{name}",  "path": "/user/bob",  "httpMethod": "GET",  "headers": {    // ...  },  "queryStringParameters": {    "age": "25"  },  "pathParameters": {    "name": "bob"  },  // ...}
```

You can access these parameters in your Lambda function code using dot notation, such as event.queryStringParameters.age or event.pathParameters.name.

#### Non-proxy integration

Non-proxy integration is another option for invoking Lambda functions from API Gateway, but it requires more configuration and adds some overhead to your API responses. With non-proxy integration, you have to define mapping templates that transform the request parameters into a JSON payload that is sent to the Lambda function. The Lambda function can access these parameters from the JSON payload that is passed as an argument.

#### To enable non-proxy integration for your API method, follow these steps:

1. Open the API Gateway console and choose your API.
2. Choose the resource and the HTTP method that you want to configure.
3. Choose Method Request from the method execution panel.
4. Expand the URL Query String Parameters section and add any querystring parameters that you want to pass to your Lambda function. For example, if you want to pass a name parameter, enter name in the Name field and check the box for Required.
5. Choose Integration Request from the method execution panel.
6. Select Lambda Function as the integration type and uncheck the box for Use Lambda Proxy integration.
7. Select the region and the name of your Lambda function and choose Save.
8. Expand the Mapping Templates section and click on Add mapping template.
9. Enter application/json in the Content-Type field and choose Method Request Passthrough from the Generate template dropdown menu.
10. Modify the template code to include any querystring or path parameters that you want to pass to your Lambda function. For example, if you want to pass a name parameter, add this line in the template code: `"name": "$input.params('name')"`
11. Choose Save and deploy your API.

Now you can test your API method using the Test button on the method execution panel. You can enter any querystring or path parameters in the URL and see how they are passed to the Lambda function in a JSON payload.

For example, if you have a GET method for /user resource and you invoke it with /user?name=bob, you will see something like this in the JSON payload:

```
{  "name": "bob"}
```

You can access these parameters in your Lambda function code using dot notation or bracket notation, such as event.name or event[‘name’].

#### More details on Proxy and Non-Proxy integrations:

Proxy integration is a type of integration where API Gateway passes the raw request from the client to the backend service (such as Lambda or HTTP endpoint) as-is, without any modifications or transformations. This means that you do not have to define any mapping templates or data mappings between the request and response parameters. The backend service can access the request parameters such as headers, query strings, path parameters and body from the event object (for Lambda) or the HTTP request object (for HTTP endpoint). Proxy integration simplifies the configuration and reduces the latency of your API responses. It also allows your backend service to evolve without having to change your API Gateway setup.

Non-proxy integration is a type of integration where API Gateway transforms the request from the client to a JSON payload that is sent to the backend service (such as Lambda or HTTP endpoint). This means that you have to define mapping templates and data mappings between the request and response parameters. The backend service can access the request parameters from the JSON payload that is passed as an argument. Non-proxy integration gives you more control and flexibility over your API design and behavior. It also allows you to reuse configured mapping templates for different backend services that have similar data formats.

**The following table summarizes some of the key differences between proxy and non-proxy integration:**

![](https://cdn-images-1.medium.com/max/800/1*Cjpk68Vlt05LSjS1O38f3w.png)

I hope this helps you understand the difference between proxy and non-proxy integration better.
