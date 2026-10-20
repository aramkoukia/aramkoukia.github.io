---
layout: post
title: "Have a cleaner Web API code with DataAnnotations"
date: 2016-12-09
description: "Dealing with validations and testing them properly exists in all different layers of an application, from the browser level validation all…"
image: /assets/img/2016-12-09-have-a-cleaner-web-api-code-with-dataannotations/1.jpg
---

### Have a cleaner Web API code with DataAnnotations

![](/assets/img/2016-12-09-have-a-cleaner-web-api-code-with-dataannotations/1.jpg)

Dealing with validations and testing them properly exists in all different layers of an application, from the browser level validation all the way to SQL constraints, and when you don’t use the right way to handle validations you will end up with a whole lot of code that will get out of control and hard to track.

Once ASP.NET MVC was introduced by Microsoft, its Model State Validation was one of the most favourite features of it between MVC developers where on your Model that is coming from the browser to the controller action, you can add decorations and the Model Validator of the framework will check them for us.

Now that ASP.NET MVC and ASP.NET Web API are getting aligned together, we can have the same Model State Validation in ASP.NET Web API too and keep your code clean and have all your validations in a centralized location (inside your class that you receive from the client).

Now let’s get into code and see what it takes to have Model State Validation in ASP.NET Web API.

This is the namespace that you are going to use:

```
using System.ComponentModel.DataAnnotations;
```

Let’s create a User class that has some attributes that we’d like to validate, some required, one a valid email format and one is a social security number that uses a Regular Expression to validate the value. so here is how the class will look like:

```
public class User
```

```
{
```

```
[Required, MaxLength(100)]  public string FirstName {get;set; }
```

```
[Required, MaxLength(150)]  public string LastName {get;set; }
```

```
[Required, EmailAddress]  public int Email {get;set; }
```

```
[RegularExpression(@"^\d{3}-\d{2}-\d{4}$")]  public string SocialSecurityNumber {get;set; }
```

```
}
```

Now we are going to add a controller action to the project for creating a User object, so I’ll add a User controller with a POST method in it that takes in a User object defined above.

Here is how this controller and its action look like:

```
namespace DataAnnotationsSample.Controllers{   public class UserController : ApiController   {         public IHttpActionResult Post(User user)        {           return Ok();         }    }}
```

With this, Web API will not automatically return a Bad Request status code to the client and we need to check the Validation status of the Model and return the proper status code. For that there are some options.

First option is to check the ModelState object and see if it is Valid in the controller like:

```
public IHttpActionResult Post(User user){   if (ModelState.IsValid)      return Ok();   else      return BadRequest
```

The other option is to add a ValidateModelAttribute action filter so that it gets executed before the controller action is called and from there we can decide of we want to continue to the controller action code or return a BadRequest to the client.

Here is how our action filter will look like:

```
namespace DataAnnotationsSample.Filters{     public class ValidateModelAttribute : ActionFilterAttribute    {         public override void OnActionExecuting(HttpActionContext actionContext)        {            if (actionContext.ModelState.IsValid ==false)           {                actionContext.Response = actionContext.Request.CreateErrorResponse(HttpStatusCode.BadRequest, actionContext.ModelState);           }       }    }}
```

Now one last step for this to work is just like any other action filter we need to register this in our API’s Register function like this:

```
config.Filters.Add(new ValidateModelAttribute());
```

With this we should not really need to check the ModelState object IsValid property on each controller actions (there might be some cases that you might still need them though but most cases you won’t).

As you can see DataAnnotations cleaned up a lot of code for us and put all the validation logic into each entity itself so that when you look at the entity you know the conditions for each attribute.

Another amazing thing that you will gain with using data annotations is that most of the Web API explorers work with these annotations and once you have these on top of your attribute these information will show up on your API’s online help page and the client can see them there easily.

DataAnnotations has a lot of power, you can have validation cross attributes (say you want to check at least one of three attributes of an entity is provided or things like that) or you could have complete customer annotation attributes for your class members(I will have another post just to describe these two options)

Hope this makes your life a bit easier in making your Web API.
