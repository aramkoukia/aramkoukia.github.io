---
layout: post
title: "Implementing Single Sign-On Part 3: Connecting the Application to Windows Azure AD"
date: 2016-12-08
description: "So now we have done setup our WAAD setup and we are ready to create a simple web application with Microsoft Visual Studio to use the users…"
tags: [".NET", "Architecture", "Azure"]
---

### Implementing Single Sign-On Part 3: Connecting the Application to Windows Azure AD

So now we have done setup our WAAD setup and we are ready to create a simple web application with Microsoft Visual Studio to use the users inside the WAAD for authentication.

all you need is a version of Visual studio 2012 or 2013 and Asp.Net MVC 4 project template there and select the Intranet Application while creating your new MVC4 project and make sure you check the Razor View engine check box.

Basically you can do these steps that we are going to do in any existing Web Forms or MVC application since we are not using anything that is specific to ASP.NET MVC 4.

By default, Visual Studio configures your application to serve content through HTTP and as you know that is no what you want for secure sessions, since it would leave communications unprotected and allow potential threads to steal cookies and tokens. This is not mandatory during the build phase, and WAAD will not push you to use of HTTPS.

so to enable HTTPS from within Visual studio go to the properties of your project **and**switch **SSL Enabled** to**True**and Copy the SSL URL property into clipboard.

Now again go to Properties of the project and this time in the Web tab, in the Local IIS web server, paste the value that you just copied from the SSL URL and Save and Close the properties window.

Now it is time to introduce your application to WAAD:

Go to Windows Azure portal and go to the **Integrated Apps**tab.

In this tab, you will see all the applications that are introduced to WAAD to use this directory and we say it is “Registered” in a tenant .

This area is dedicated to listing all the applications that are registered in your directory tenant. We say that an application is “registered” in a tenant when:

- The application has an entry in the directory, which describes its main coordinates: name, associated endpoints, and so on. More details later.
- The application itself has been granted permission to perform some operation on the current directory tenant: the operations range from requesting a sign-on token to the ability to query the directory. Once again, more details later.

Sine this is our First application that we are registering here, we will start with clicking the Add link in the Windows Azure portal and you will see the below dialog.

it is a simple wizard that you need to go through.

The picture above shows the first of such screens. The options offered are straightforward:

- **Display name**: the text entered here is used as human-readable moniker to refer to the app whenever a user — be it an administrator managing the registered apps list or a customer deciding to grant directory access to the app — needs to do something about it. There is more info about this in the [Developing Multi-Tenant Web Applications with Windows Azure AD](http://msdn.microsoft.com/en-US/library/windowsazure/dn151789.aspx) paper.
- **Access type**: this set of radio buttons allows you to specify what operations the app should be allowed to perform against the directory tenant. For the purposes of this tutorial, in which our goal is to simply configure web sign-on with our app, the proper choice is **Single sign-on**.

After entering your application name and checking the **Single sign-on**option click on the arrow to move to the next page.

In this What you need to enter in this window:

**APP URL**: This is the URL of your website. when you are using the IIS Express you can use the one the IIS is giving you which is something like [**https://localhost:44341/.**this](https://localhost:44341/.this) will work until your development is done and after deployment to your actual production server, you can come here and change this to the actual URL that you want.

this is important and the WAAD needs it so that after authentication and being successful it redirects the user to this URL.

**APP ID URI**: this is the ID of your application that you want the users to be authenticated on. I personally always use the same value as I entered for the APP URL.

after entering these values you can click on the check box at the lower right corner.

That

Now you have registered your application with the Windows Azure AD tenant.

in this screen you can see 2 settings that we are going to paste in our Visual Studio project so you might want to keep this page open for a while.

Connecting to Windows Azure Active Directory

now that we are registered with the WAAD tenant we need to setup our application to be able to handle the security token that the WAAD is sending back to us after the authentication.

We are going to connect the application to Windows Azure AD via the WS-Federation protocol as it is only one of the possible choices for implementing Web SSO, SAML-P being the other most common choice.

The .NET Framework 4.5 supports WS-Federation natively: all the classes needed for enforcing the protocol flow, processing authentication and handling sessions in the context of ASP.NET applications are present in the box.

Now we will use the Identity and Access Tool to configure your application. In **Solution Explorer**, right-click on your applications’ project, then click **Identity and Access…** from the context menu.

You will see the dialog below:

here you can see a list of authority types that you can use to outsource authentication. In our specific case, we are interested in using a **Business Identity Provider**so click on the second one.

with selecting that, you are going to enter these 2 values:

**Enter the APP ID URI (realm) of your application**: This is the identifier of your application, as you defined it during the registration. Switch back to the browser window showing the Management Portal, copy the corresponding value from the **Update your code with your App ID URI** field and paste it here.

**Enter the path to the STS metadata document**: The “STS metadata document” is a file containing a machine-readable description of the authority you want to connect to: the tool will consume it to determine the value of parameters that are essential to the sign-on flow (more details below). Every Windows Azure AD tenant exposes one such document; its location is provided at the end of the registration process. Switch to the Management Portal, copy the corresponding value from the app registration page, switch back to the tool and paste the path in this field.

click on **OK**. The tool will generate and add some configuration lines to your web.config file.

these are the lines that will be added to you config file:

- **<section> entries for system.identityModel and system.identityModel.services**: These are necessary for the config to understand the identity-specific config settings.
- **<authorization> settings in <system.web>**: The tool automatically change the existing ASP.NET authentication settings to require that every request to the app must be authenticated.
- **WSFederationAuthenticationModule (FAM) and SessionAuthenticationModule (SAM) in <system.webServer/modules>**: Those entries add in the application’s HTTP pipeline the HttpModules which take care of enforcing the use of WS-Federation for authentication. The FAM is the module responsible for protocol enforcement: sign-on requests, token validation sign out management are the main flows it is responsible for.
- **The <system.identitymodel/identityConfiguration> section**: This element determines the behavior of the app during the authentication phase.
- **The <system.identitymodel.services/federationConfiguration> section**: This section provides the coordinates that are necessary for driving WS-Federation flows: the address of the authority to be used for sign-on requests, the identifier of the app itself to be included in requests.

The auto-generated config is all you need for taking advantage of Windows Azure AD for web sign-on: you don’t need to write any authentication-specific code in the application itself.   
If you want to access user identity’s information you can easily do so by querying the claims in the current principal. For example, say that you’d like to access the first and last names of your current user. You will be able to do so using the following code, without the need of knowing anything about how authentication took place:

```
//...using System.Security.Claims;namespace ExpenseReport.Controllers{ public class HomeController : Controller { public ActionResult Index() { ClaimsPrincipal cp = ClaimsPrincipal.Current; string fullname = string.Format("{0} {1}", cp.FindFirst(ClaimTypes.GivenName).Value, cp.FindFirst(ClaimTypes.Surname).Value); ViewBag.Message = string.Format("Dear {0}, welcome to the Expense Note App", fullname); return View(); }//...
```

Starting from .NET 4.5, every identity in .NET is represented with a *ClaimsPrincipal*. In this case, the current *ClaimsPrincipal* has been constructed during the validation of an authentication token generated by Windows Azure AD and presented by the user at sign-on time.

Every *ClaimsPrincipal* contains a collection of claims, attributes describing the current user as asserted by the authority that authenticated him/her. In our walkthrough, the claims in the principal are the ones issued in the token by Windows Azure Active Directory: for a complete list of the available claims please refer to the online documentation.

Windows Azure AD issues a fixed set of claims for the authenticated users. Below there’s a quick reference of all the claims you can expect from Windows Azure AD; you can find a complete description in the documentation.

At this point your application has all you need to demonstrate web sign-on with Windows Azure AD, however it is not complete yet.   
There are at least other two important features you’ll want to add: support for sign out and automatic refresh of the authority’s protocol coordinates.
