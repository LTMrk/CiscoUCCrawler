---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-for-end-user-b-cupi-api-for-end-user-b-cupi-api-d68b301af3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API_for_End_User/b_CUPI_API_for_End_User/b_CUPI_API_for_End_User_chapter_01100.html
retrieved_at: 2026-08-21T08:05:08.083044+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

Updated: January 18, 2019

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- SSL Connection Check API

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- SSL Connection Check API

- Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- SSL Connection Check API

- Introduction

- Listing the SSL Connection Check API

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- SSL Connection Check API

## Introduction

By default, the TCP/IP port 7443 is disabled. To enable or disable the port 7443, the following CLI command is used:

utils cuc jetty ssl enable/disable

This API is created to ensure SSL connection is allowed through the Jetty SSL port 7443.

## Listing the SSL Connection Check API

This API request is initiated to check if port 7443 is enabled to allow SSL connections.

RequestURI :

```
GET https://<connection-hostname>/vmrest/sslconnectioncheck
```

Sample Response:

```
<sslconnectioncheck>
    <Response>true</Response>
   </sslconnectioncheck>
```

JSON Example

```
https://<connection-hostname>/vmrest/sslconnectioncheck?jsonp=1
  Sample Response : 
 (

   {

     "Response":"true"

   }

 )
```

| GET https://<connection-hostname>/vmrest/sslconnectioncheck |
|---|

| <sslconnectioncheck>
    <Response>true</Response>
   </sslconnectioncheck> |
|---|

| https://<connection-hostname>/vmrest/sslconnectioncheck?jsonp=1
  Sample Response : 
 (

   {

     "Response":"true"

   }

 ) |
|---|