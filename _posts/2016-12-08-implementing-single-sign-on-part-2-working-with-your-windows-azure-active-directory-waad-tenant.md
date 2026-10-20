---
layout: post
title: "Implementing Single Sign-On Part 2: Working with Your Windows Azure Active Directory (WAAD) Tenant"
date: 2016-12-08
description: "So now that you read my previous post about the Single Sign-on experience, it is time to do some real job and start playing with Windows…"
medium_url: https://medium.com/@aramkoukia/implementing-single-sign-on-part-2-working-with-your-windows-azure-active-directory-waad-tenant-8e372db109fa
---

### Implementing Single Sign-On Part 2: Working with Your Windows Azure Active Directory (WAAD) Tenant

So now that you read my previous post about the Single Sign-on experience, it is time to do some real job and start playing with Windows Azure AD tenant.

First of all you need to create an account here(you can use your existing Microsoft accounts like Hotmail, MSN or Live etc …):  
<http://www.windowsazure.com/en-us/pricing/free-trial/>right now they offer a 30 days trial access with 200$ credit to use different service, so enjoy your free WAAD for now…Windows Azure Active Directory is nothing but a Cloud directory of users instead of the on-premises one that you already have ion your local network in the domain controller and if you already have an Office 365 account, all the users that you have there, exist here as well and you can use them here.It basically is the service that provides the Identity provider service and even services like Office 365 and InTune is using this as their identity backbone.

If you want to reuse that tenant, as of today you can do by creating a new Windows Azure subscription and using ad administrator user from that tenant at sign up time. I will not go through that process for now but you can find guideline in the Windows Azure website for that.

I will go through the process that you don’t have an existing tenant in WAAD.  
Create your Cloud Directory Tenant and Add a Users

first go to <http://manage.windowsazure.com> and login and you will see the page below with some tiles on your left hand side. and what we are interested in is the Active Directory one, which is 0 right now.

What you see up here is the Active directory list in WAAD.

what you should do is just go to the **Directory** tab there and click on the **Create Your Directory** Link and fill in the Directory information in the dialog that pops up like below.

here is what you need to fill:

1. **Domain Name:**here is the place you give your tenant on WAAD and need to be a unique name. After creation it is possible to register additional domains that you own. For more information, see [domain management](http://technet.microsoft.com/en-us/library/hh969248.aspx). you can use some part of your company name or something for that.
2. **Country or Region**: in this drop down you pick the place your company exists.
3. **Company Name:**this column is your company name and will be displayed in some places.

After filling that up, you will go to the Create a directory tenant. click on the check on the lower right corner and your WAAD tenant is created!

So now you have your Cloud directory in WAAD tenant, and next thing you might want to do is so move your on-premises users in your Windows Server active directory there and you can find the instructions for that from [here](http://technet.microsoft.com/library/jj151781.aspx).  
When a directory tenant is created, it is configured to store users and credentials in the cloud. If you want to integrate your directory tenant with your on-premises deployment of Windows Server Active Directory, you can find detailed instructions .

Now it is time to click in the Directory you just created and go to User Management page.

the directory should be empty except for the MS Account that created the Windows Azure subscription.  
One thing that is good to point out is, That Microsoft account that created the tenant is the Global Administrator of the actions inside the WAAD tenant and cannot be used for scenarios for Single Sign-on or authenticate into the systems you have.

Now let’s add a user to the directory, so that we will be able to use it for authentication in our next posts for the single sign-on implementation .  
Click the Add User link and you will see a pretty straightforward dialog to fill in the user information

You can add a new User or add an existing Microsoft account which will act as the existing Microsoft account inside the WAAD tenant.

fill in everything and click on the Arrow on the right lower corner.

In the next page, fill in some pore properties and add the Roles you wish to give to the user.

Fill them in and again click the Arrow.

Finally, the Portal creates a temporary password for the user and the user has to change it on the first log on to your system.

Now we are all set for our first implementation of our single sign on experience that I will write about in the next post.
