---
doc_id: developer-cisco-com-site-im-and-presence-discover-api-overviews-platform-soap-service-9bf9d24a24
source_url: https://developer.cisco.com/site/im-and-presence/discover/api_overviews/platform_soap_service/
retrieved_at: 2026-09-01T17:45:56.252132+00:00
---

# About the Platform SOAP Service

Cisco Unified Presence 8.6.1 supports automated upgrade deployments using the Platform SOAP Service. The Platform SOAP Service provides a web-based interface integrated with the existing Cisco Unified Presence upgrade framework.

The purpose of the Platform SOAP Service is to allow system upgrades and install of COP files for large scale deployments of Cisco Unified Presence, to be initiated and monitored from a single management client.

To successfully develop an application that uses the Platform SOAP Services, you need to understand how the upgrade operates and how your application fits into the upgrade process.

### Administration

Platform SOAP services MUST be activated from Cisco Unified Serviceability administration and will not be turned on or activated upon install of or upgrade to Cisco Unified Presence 8.6.1. This is a feature service and MUST be activated on all nodes within the Cisco Unified Presence cluster. For more information on feature services and Cisco Unified Serviceability administration, please refer to the Serviceability Configuration and Maintenance Guide for Cisco Unified Presence

### Service URL and WSDL URL

### Overview of APIs and their functions

### Login Authentication

Every time a service is invoked, authentication needs to be performed. Since the services invoke Cisco Unified Presence functionality, the application MUST use an Cisco Unified Presence Operating System Administrator account.

### Synchronous and Asynchronous SOAP Services

A given SOAP service can be invoked in a synchronous or asynchronous manner with no change to the service, itself. Axis2 provides synchronous behavior if:

No call back URL (ReplyTo) or transaction ID (MessageID) are provided in the SOAP request header.

A MessageID and ReplyTo are provided, but the ReplyTo is the anonymous URL.

### SOAP Service Throttling

SOAP services are throttled if too many requests arrive at once. A maximum of 3 concurrent threads running is allowed. Certain services are denied access based on the Platform API lock, before throttling can occur. Services that are throttled will wait for up to 60 seconds for the throttling semaphore. If the timeout elapses, the service returns a result of internal.request.failed with a messageKey error.remote.throttled

# More Information on Platform SOAP Service

For more information on the Cisco Unified Presence Platform SOAP Service, including protocol messaging flows and protocol syntax examples, please refer to the "Developer Guide for Cisco Unified Presence" for the particular version of Cisco Unified Presence which you have deployed.

Download Developer Guide