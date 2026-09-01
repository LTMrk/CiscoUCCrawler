---
doc_id: developer-cisco-com-site-user-data-services-discover-how-does-uds-work-9dd9877f3b
source_url: https://developer.cisco.com/site/user-data-services/discover/how-does-uds-work/
retrieved_at: 2026-09-01T17:49:43.454203+00:00
---

# How does UDS work?

## REST APIs

The first release of our APIs provides a developer entry to the core concepts of users, devices, and extenstions in User Data Services. Through the API, a developer is able to access and update these concepts as well as some of the concepts related to them. Now developers can build custom applications and widgets to quickly update user and device data through standard REST protocols.

The Cisco UDS REST APIs utilize standard formats and all APIs will return results in XML format.

As a RESTful interface, all UDS APIs are accessed as resources (typically URLs). In addition, UDS implements four common HTTP request methods to carry out client requests. These are:

GET - queries the CUCM database for information. UDS supports requests for information about users, phone services, and device configurations. This verb is non-destructive: that is, it does not modify any information.

POST - adds users, services, and devices to the CUCM database.

PUT - updates or modify existing user information in the CUCM database.

DELETE - removes information from the CUCM database.

Below is the request and response to get a user's speed dials.

To learn more about sending a REST-based API request, check out the the UDS "Hello World" page .

New to UDS? Checkout these steps to get started.

Get Started

We've put together a whole load of hints, tips, code samples and code snippets to help you benefit from User Data Services.

Learn More