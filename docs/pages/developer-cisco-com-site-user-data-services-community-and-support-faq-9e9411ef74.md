---
doc_id: developer-cisco-com-site-user-data-services-community-and-support-faq-9e9411ef74
source_url: https://developer.cisco.com/site/user-data-services/community-and-support/faq/
retrieved_at: 2026-09-01T17:35:11.149363+00:00
---

# User Data Services FAQs

General

Error Responses

- The client receives a 401 response when it attempts to access a UDS resource .

- The client receives a 409 response when it attempts to add a service or a device .

- The client receives a 415 response when it attempts to modify an item .

General

What type of applications can be integrated with the UDS API resources?

Because UDS is implemented via REST transactions over HTTP, any HTTP-savvy application can potentially access the API. A suitable application could be a native PC program, a mobile OS app with network/HTTP request capability, or a browser-based web app using Javascript.

Note, however, that browser apps are likely to encounter security restrictions when making REST requests due to 'same origin/cross origin resource' policies implemented in recent browsers, which prevent script-initiated HTTP requests from being sent to a domain (i.e. CUCM) different from the host which served the original web page. A typical architecture for implementing cross-origin restricted requests involves 'proxying' external requests (i.e. to UDS) from the web server itself.

Emerging standards-based mechanisms for safely managing cross-origin requests (e.g. 'cross origin resource sharing' or CORS) are not currently supported by UDS, but are being considered for a future release.

What security measures does the UDS APIs provide?

UDS resources that manage user-specific information and device configuration require authentication prior to their use. UDS resources that provide general information, such as UDS server features, time zone and supported locales, do not require authentication. Note that the restricted resources use HTTP Basic authentication, where the username and password information are sent essentially in the clear (base64 encoded.) Cisco strongly recommends that all UDS transactions be performed through a secure session via HTTPS and/or within a secure intranet.

Why are some of the API names nearly identical? 'Devices' versus 'device', and 'users' versus 'user', for example?

In general, a 'plural' UDS resource name (that is, ends with an 's' character) provides general information. This information can then be used with the 'singular' API name to drill down for more detailed information. For example, a user might access the 'devices' resource to obtain a list of the devices that he can manage. He would then use information on the list, along with the 'device' resource, to manage the settings and configuration of a specific device.

Does the UDS API support XML and JSON requests and responses?

The Cisco UDS API supports only the XML format for all requests and responses.

ErrorResponses

The client receives a 401 response when it attempts to access a UDS resource.

An attempt was made to access a restricted resource with missing or valid credentials. The resource might have been accessed by accident, or an invalid username and password may have been provided. The client should obtain the correct credentials and retry the request.

The client receives a 409 response when it attempts to add a service or a device.

An attempt was made to add an information item – for example a service or device - that already exists in the UDS system. This message is possible when the POST method is used with a resource. Note, to update existing items in the UDS system, the PUT method must be used.

The client receives a 415 response when it attempts to modify an item.

There was an error in one of the parameters in the request body. Correct the parameter information and try again.

Forums