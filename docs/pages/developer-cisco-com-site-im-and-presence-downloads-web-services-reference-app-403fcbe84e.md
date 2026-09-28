---
doc_id: developer-cisco-com-site-im-and-presence-downloads-web-services-reference-app-403fcbe84e
source_url: https://developer.cisco.com/site/im-and-presence/downloads/web_services_reference_app/
retrieved_at: 2026-08-25T21:05:41.730365+00:00
---

# Cisco Unified Presence Reference Application

Presence exchange and user preference information (presence rules, contact list, etc) on  Cisco Unified Presence have been made available to Third Party Applications through two web services, the Presence Web Service and the Client Configuration Web Service .

The Presence Web Service provides the functionality to manage user presence on a Cisco Unified Presence server. Users can set their own presence states and receive notifications of changes to the presence states of their contacts; the client application registers a HTTP endpoint and sets up a subscription for presence notifications.

The Client Configuration Web Service is an interface that allows client applications to manage user preference information on Cisco Unified Presence. The Client Configuration Web Service provides the functionality to provision information such as contacts, contact groups, presence rules, access control lists, and calendaring options.

Both these interfaces are described in detail in the Developer Guide for Cisco Unified Presence . This document describes what methods are in the API, and the contents of method requests and responses.

A Reference Application is provided with the web services to demonstrate the functionality opened up by the web services. The objective of the Reference Application is not to be of production quality, but to aid developer understanding of how best to use the interfaces. The Reference Application also provides a method for testing that the web services have been correctly set up, and are fully operational.

Provided with the Reference Application is the Developer Cookbook for Cisco Unified Presence. This document describes the functionality of the Reference Application, and outlines how it is built and configured. It also describes the implementation, includes source code examples, and provides guidelines on the using the web services.

Both the Reference Application and Developer Cookbook for Cisco Unified Presence can be downloaded via the links below.

Please ensure that you download the version of the Reference Application and Developer Cookbook for Cisco Unified which is applicable to the release of Cisco Unified Presence that you are developing against.

## Developer Cookbook Version

## Reference Application Version

| Developer Cookbook Version | Reference Application Version |
|---|---|
| CUP 10.5 Developer Cookbook | CUP 10.5 Reference Application |
| CUP 9.0 Reference Application |
| CUP 8.5 Developer Cookbook | CUP 8.5 Reference Application |
| CUP 8.0.2 Reference Application |
| CUP 8.0 Developer Cookbook | CUP 8.0 Reference Application |
| CUP 7.0  Developer Cookbook | CUP 7.0 Reference Application |