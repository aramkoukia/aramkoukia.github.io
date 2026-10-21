---
layout: post
title: "Can we use comments in a JSON file?"
date: 2021-11-12
description: "Well the short answer is: No!"
image: https://cdn-images-1.medium.com/max/800/0*Wqnbr_4djUu6GCtg.png
tags: ["JavaScript"]
---

### Can we use comments in a JSON file?

![](https://cdn-images-1.medium.com/max/800/0*Wqnbr_4djUu6GCtg.png)*Image from <https://www.nylas.com/blog/the-complete-guide-to-working-with-json/>*

Well the short answer is: No!

Comments of the form `//…` or `/*…*/` are not allowed in JSON. This answer is based on the official JSON documentation below:

- [https://www.json.org](https://www.json.org/)
- [RFC 4627](http://www.ietf.org/rfc/rfc4627.txt): The `application/json` Media Type for JavaScript Object Notation (JSON)
- [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259) The JavaScript Object Notation (JSON) Data Interchange Format (supercedes RFCs 4627, 7158, 7159)

However if you really need to nothing stops you from putting the comment in the JSON like `"_comment"` and have your application to ignore it when parsing the JSON data.

Here is an example:

```
{   "_comment": "this is a very useful comment ...",   "glossary": {      "title": "example glossary",      "GlossDiv": {         "title": "S"      }   }}
```

Cheers!
