---
layout: post
title: "I agree about the fields and events AmirAli SobhGol, I guess it depends on the requirements."
date: 2018-01-26
description: "Though Event Source has lot of other features than the ones you mentioned, I don’t think Event Source is needed for all services. Out of…"
---

I agree about the fields and events AmirAli SobhGol, I guess it depends on the requirements. People can decide to have 1 or more events based on changes to their domain objects.

Though Event Source has lot of other features than the ones you mentioned, I don’t think Event Source is needed for all services. Out of several services that you might have, some of them (The ones that handle Financial transactions are obvious candidates) could use this data store.

Yes return the response to user when event is saved and published. Obviously Events would not be available on the “Read Model” side and you will have “Eventual Constancy” in the system and you might want to reflect that in the UX some how for the user, so they know that things are in progress in the background.

I’m not sure what you mean by “Workers”. If by “Workers” you mean Domain Model Services, you can definitely have multiple instances and the API Gateway will make sure that only one instance will receive the incoming Command. If you are asking about the Read Model services, they are not constantly checking for events, and they just “Subscribe” to events, and get notified when a message is arrived in the Bus. Even those can be multiple instances as when one instance picks up the message, the other will not get it anymore.

Hope this helps :)
