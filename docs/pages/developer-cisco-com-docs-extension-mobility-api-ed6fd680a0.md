---
doc_id: developer-cisco-com-docs-extension-mobility-api-ed6fd680a0
source_url: https://developer.cisco.com/docs/extension-mobility-api/
retrieved_at: 2026-08-24T22:12:13.892664+00:00
---

# Overview

## Cisco Extension Mobility API

The Cisco Unified Communications Manager (Unified CM) Extension Mobility feature (E/M) allows end-users to access their personal Cisco Unified IP Phone configuration, including directory number, line appearances, phone services, and speed dials, from any other E/M-enabled phone on the UCM system via a simple login user interface on the phone.

For more on the Cisco Unified CM Extension Mobility feature, including setup and configuration steps, refer to the Cisco Unified Communications Manager Administration Guide or the Cisco Unified Communications Manager Features and Services Guide.

The Cisco Extension Mobility API (E/M API) provides an HTTP/XML interface enabling applications to automate E/M actions, including:

- Logging a user into a specific phone

- Logging out a user

- Forcing E/M logout for all users

- Querying for the E/M login status of specific users or devices

The E/M API can be used in conjunction with the on-phone E/M login service, or customers may choose to remove the default E/M login service from user phones in favor of using a custom developed IP Phone Services API appliction which uses the E/M API to manage or automate logins.

This Developer Guide provides information for developers building applications that extend the functionality of the Cisco Extension Mobility service. Developers should be familiar with Extensible Markup Language (XML) and secure HTTP network requests.

## Use Cases

Examples of applications which can be developed using the E/M API include:

- “Hot desk seating” for visiting employees in office situations

- Providing personalized phone service to patients’ rooms in a hospital or clinic

- Hotel/hospitality solutions, which can automate customized phone settings for guest rooms

- Scheduling conference calls for specific rooms/phones via an automated reservation system

Note: The Extension Mobility API does not support the Extension Mobility Cross Cluster feature.

Note: Extension Mobility logouts performed via an E/M API logout request will not automatically remove call history entries from the phone.  See the Cisco Extension Mobility service parameter Clear Call Logs on Intra-Cluster EM for more info.

If removing call history entries is desired, entries can be removed from the phone after an E/M API logout operation by using either the AXL or IP Phone Services APIs:

- Reset the device via the AXL SOAP <doDeviceReset> request, specifying the isHardReset parameter as true . See Cisco AXL Developer Site .

- POST a <CiscoIPPhoneExecute> XML request object to the phone's onboard web server, specifying a URI of Init:CallHistory . See Cisco IP Phone Service Developer .

## Cisco Product Security Overview

This product contains cryptographic features and is subject to United States and local country laws governing import, export, transfer and use.

Note: Delivery of Cisco cryptographic products does not imply third-party authority to import, export, distribute or use encryption. Importers, exporters, distributors, and users are responsible for compliance with U.S. and local country laws. By using this product you agree to comply with applicable laws and regulations. If you are unable to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at http://www.cisco.com/wwl/export/crypto/tool/stqrg.html . If you need further assistance, contact us by sending e-mail to export@cisco.com.

Next