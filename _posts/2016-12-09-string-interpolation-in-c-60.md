---
layout: post
title: "String Interpolation in C# 6.0"
date: 2016-12-09
description: "When it comes to “String.Format”, we have always suffered the fact that it is so unreadable and error prone. When the string that you want…"
---

### String Interpolation in C# 6.0

When it comes to “String.Format”, we have always suffered the fact that it is so unreadable and error prone. When the string that you want to generate is long and has more than two or three variables, String class makes it very hard for us to have a readable text that you can find out what it is building.

Take a look at this string:

```
var myString = string.Format("The invitation is {0}. InvitationKey: {1}, UserKey: {2}, TenantKey: {3}", Invitation.InvitationStatusKey.ToString(), Invitation.InvitationKey, Invitation.UserKey, Invitation.TenantKey);
```

Yes, I know, it is very hard to track down which variable is going to be put where! and will it even make sense!

But now looks like C# “String Interpolation” is going to clean this up for us. take a look at the simplified version of the above code in C# 6.0:

```
var myString = $"The invitation is {Invitation.InvitationKey}. InvitationKey: {Invitation.UserKey}, UserKey: {Invitation.TenantKey}, TenantKey: {Invitation.InvitationStatusKey.ToString()}";
```

And right after you make that change, you realize that you have been logging wrong information in to the place holders in your String.Format statement before, because you could not see what you are putting in the {0} placeholder! and now you can actually SEE what is it you are building!

I think this is one of the best features of C# 6.0 and for sure I’m going to spend some time removing all String.Format statements from out code as soon as we upgrade to it.
