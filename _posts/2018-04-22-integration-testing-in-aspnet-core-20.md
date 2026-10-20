---
layout: post
title: "Integration Testing in Asp.Net Core 2.0"
date: 2018-04-22
description: "When you are building an API, and doing all the right unit tests and ad-hoc tests and etc, the next type of test in the test pyramid is…"
image: https://cdn-images-1.medium.com/max/800/1*hRCR2q2OF7cPjIi1ZZbHPg.jpeg
---

### Integration Testing in Asp.Net Core 2.0

![](https://cdn-images-1.medium.com/max/800/1*hRCR2q2OF7cPjIi1ZZbHPg.jpeg)

When you are building an API, and doing all the right unit tests and ad-hoc tests and etc, the next type of test in the test pyramid is Integration Test of API Tests, as in you make HTTP calls to your API and inspect the result.

Ideally you want a change to your code base to trigger all your unit tests as well as your integration tests to let the code change to be committed.

Now, one of the issues for API testing could be, you would need to deploy the code change to some environment and use an actual database and verify if the changes has broken anything.

But with .Net Core 2.0 and later, you don’t need to host your API (with the new code changes) to an actual web server, and also you don’t even need a real database and you can just run your tests as if they are unit tests!

### Using Asp.Net Core Test Host

How? With Asp.Net Core Test Host package.

ASP.NET Core includes a test host that can be added to integration test projects and used to host ASP.NET Core applications, serving test requests without the need for a real web host.

#### Show me some code

Open your .Net Core solution and add a new test project.

Then add a reference to your .Net Core API project that has your Controller classes to the test project you just created.

In the test project, install the “Microsoft.AspNetCore.TestHost” nuget package.

![](https://cdn-images-1.medium.com/max/800/1*iHssKJfiwco-XZv8vCEs7A.png)

This is going to give us access to Test Server class.

After you installed the `Microsoft.AspNetCore.TestHost` package in the test project, you can create and configure a `TestServer` to use in your integraion tests.

Now we are going to add a simple helper class to give us a Test Server instance. Let’s call it Test Server Fixture. Here is how it will look like:

Now that we have our Test Server Fixture in place, we can go ahead and use it to build our first Integration Test.

Here is the actual Controller action that we want to add integration test for:

Now it is time for the actual Integration/API test to test the simple API that we created above.

The following test class is the integration test that will test the *“Ping”* endpoint from the controller we created earlier:

You can see, that the Test Server creates an instance of our API without the need to deploy the API to a particular QA or Dev environment to verify the code changes.

Now you can setup your source control build definition to run these integration tests as part of the build to make sure changes are not merged before these integration/API tests are passes.

Cheers!

**Software engineer jobs** — <https://jooble.org/jobs-software-engineer>
