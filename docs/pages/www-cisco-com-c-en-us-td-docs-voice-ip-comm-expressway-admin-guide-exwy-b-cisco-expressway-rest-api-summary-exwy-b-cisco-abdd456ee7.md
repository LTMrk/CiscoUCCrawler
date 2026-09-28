---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-admin-guide-exwy-b-cisco-expressway-rest-api-summary-exwy-b-cisco-abdd456ee7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/admin_guide/exwy_b_cisco-expressway-rest-api-summary/exwy_b_cisco-expressway-rest-api-summary_chapter_01.html
retrieved_at: 2026-08-16T15:32:03.718562+00:00
---

Cisco Expressway REST API Summary Guide

# Cisco Expressway REST API Summary Guide

Book Contents

- Book Title Page

- Preface

- Using the Expressway REST API

Find Matches in This Book

## Results

Updated: June 3, 2020

Chapter: Using the Expressway REST API

## Chapter: Using the Expressway REST API

- Using the Expressway REST API

- Using the Expressway REST API

# Using the Expressway REST API

## Using the Expressway REST API

The Expressway REST API is compliant with RAML version 0.8 ( raml.org/spec.html ). Although the API is fully compliant, it does not support nested APIs.

The API is self-documented using RESTful API Modeling Language (RAML). You can access the RAML definitions for your system
                           at https://<Expressway FQDN or IP address>/api/raml. An experimental schema browser is embedded in the web user interface,
                           and can be accessed from the Experimental menu.

### Schemas

All request and response schema on the Expressway REST API use JSON Schema version 4 ( json-schema.org/documentation.html ). Request parameters are not supported and only JSON schemas are used.

### Authentication

The API is only accessible via HTTPS and requires authentication. The authentication credentials are the administrator credentials
                              on the Expressway node.

### Base URL

The base URL to access the Expressway REST API is http://<external_address>/api. For example, to access the system information,
                              use https://10.0.0.1/api/provisioning/sysinfo.

The REST API is published in the following categories:

Cisco Expressway-E

/provisioning/edge/ <remaining path> (for example, https://10.0.0.1/api/provisioning/edge/zone/traversalserver)

Cisco Expressway-C

/provisioning/controller/ <remaining path> (for example, https://10.0.0.1/api/provisioning/controller/zone/traversalclient)

Common between Cisco Expressway-E and Cisco Expressway-C

/provisioning/common/<remaining path> (for example, https://10.0.0.1/api/provisioning/common/adminaccount/changepassword)

Some maintenance-related items like restart and system information are standalone calls and do not apply to any of the categories.

You can also filter Get requests to find a specific entry. For example, /controller/zone/traversalclient/name/myzone returns
                                    the traversal client zone called "myzone".

REST APIs which get the status of functionalities as status/common/<remaining path> (for example, http://10.0.0.1/api/status/common/smartlicensing/licensing

### Sample requests and responses

This section provides examples on how to use Expressway API methods. The examples relate to API methods for the DNS server
                              and NTP server.

Retrieve DNS Server information

This example retrieves the DNS server information using JSON API.

URL

GET https://<Expressway FQDN or IP address>/api/v1/provisioning/common/dns/dnsserver

Request body

This operation does not require a request body.

Response body

```
{ 
"DefaultDNSServers": 
 {
 "index": 2, 
"address": "10.0.0.2" 
 }
 }
```

This example retrieves the DNS server information using cURL.

Add DNS server

This example adds a DNS server with an IP address 10.0.0.2 and index value 2 using JSON API.

URL

```
POST https://<Expressway FQDN or IP address>/api/v1/provisioning/common/dns/dnsserver'
```

Request body

```
{ 
"DefaultDNSServers": 
 {
 "index": 2, 
"address": "10.0.0.2" 
 }
 }
```

Response body

```
{
"Message": "The operation was successful"
}
```

This example adds a DNS server with an IP address 10.0.0.2 and index value 2 using cURL.

```
curl -X POST -k -i 'https://<Expressway FQDN or IP address>/api/v1/provisioning/common/dns/dnsserver' --data '{"DefaultDNSServers": {"index": 2, "address": "10.0.0.2"}}'
```

Modify DNS server

This example modifies the IP address of the DNS server with the index value 2 using JSON API.

URL

PUT https://<Expressway FQDN or IP address>/api/v1/provisioning/common/dns/dnsserver

Request body

```
{ 
"DefaultDNSServers": 
 {
 "index": 2, 
"address": "10.0.0.3" 
 }
 }
```

Response body

```
{
"Message": "The operation was successful"
}
```

This example modifies the IP address of the DNS server with the index value 2 using cURL.

```
curl -X PUT -k -i 'https://<Expressway FQDN or IP address>/api/v1/provisioning/v1/common/dns/dnsserver' --data '{"DefaultDNSServers": {"index": 2, "address": "10.0.0.3"}}'
```

Delete DNS server

This example deletes the DNS server with the index value of 2 using JSON API.

URL

DELETE https://<Expressway FQDN or IP address>/api/v1/provisioning/common/dns/dnsserver

Request body

```
{
 "index": 2 
 }
```

Response body

```
{
"Message": "The operation was successful"
}
```

This example deletes the DNS server with the index value of 2 using cURL.

```
curl -X DELETE -k -i 'https://<Expressway FQDN or IP address>/api/v1/provisioning/common/dns/dnsserver' --data '{"index": 2}'}'
```

Example: USING API FOR NTP SERVER

Retrieve NTP Server information

This example retrieves the NTP server information using JSON API.

URL

GET https://<Expressway FQDN or IP address>/api/v1/provisioning/common/time/ntpserver

Request body

This operation does not require a request body.

Response body

```
{
"index": 5,
"KeyId": 1,
"Hash": "sha1",
"Authentication": "disabled",
"Address": "10.0.0.1"
}
```

This example retrieves the NTP server information using cURL.

```
curl -X GET -k -i '<Expressway FQDN or IP address>/api/v1/provisioning/common/time/ntpserver'
```

Add NTP Server

This example adds an NTP server with an IP address 10.0.0.2 using JSON API.

URL

POST https://<Expressway FQDN or IP Address>/api/v1/provisioning/common/time/ntpserver

Request body

```
{
"index": 6,
"Address": "10.0.0.2",
"KeyId": 1,
"Hash": "sha1",
"Authentication": "disabled"
}
```

Response body

```
{
"Message": "The operation was successful"
}
```

This example adds an NTP server with an IP address 10.0.0.2 using cURL.

```
curl -X POST -k -i 'https://<Expressway FQDN or IP address>/api/v1/provisioning/common/time/ntpserver' --data '{"index": 6, "Address": "10.0.0.2", "KeyId": 1, "Hash": "sha1", "Authentication": "disabled"}'
```

Modify NTP Server information

This example modifies the IP address of the NTP server with the index value 6 using JSON API.

URL

PUT https://<Expressway FQDN or IP address>/api/v1/provisioning/common/time/ntpserver

Request body

```
{
"index": 6,
"Address": "10.0.0.3",
"KeyId": 1,
"Hash": "sha1",
"Authentication": "disabled"
}
```

Response body

```
{
"Message": "The operation was successful"
}
```

This example modifies IP address of the NTP server with the index value 6 using cURL.

```
curl -X POST -k -i 'https://<Expressway FQDN or IP address>/api/v1/provisioning/common/time/ntpserver' --data '{"index": 6, "Address": "10.0.0.3", "KeyId": 1, "Hash": "sha1", "Authentication": "disabled"}'
```

Delete NTP Server

This example deletes the NTP server with the index value of 6 using JSON API.

URL

DELETE https://<Expressway FQDN or IP address>/api/v1/provisioning/common/time/ntpserver

Request body

```
{
 "index": 6 
 }
```

Response body

```
{
"Message": "The operation was successful"
}
```

This example deletes the DNS server with the index value of 6 using cURL.

```
curl -X DELETE -k -i 'https://<Expressway FQDN or IP address>/api/v1/provisioning/common/time/ntpserver' --data '{"index": 6}'}'
```

Retrieve Smart Licensing Status

This example retrieves Smart Licensing Status.

URL

GET https://<Expressway FQDN or IP address>/api/v1/status/common/smartlicensing/licensing

Request body

This operation does not require a request body.

Response body

```
{
"ExportControlledFunctionality": "True",
"VirtualAccount": "Expressway",
"SmartAccount": "testaccount.cisco.com",
"Authorization": {
"LicenseAuthorizationStatus": "OUT OF COMPLIANCE",
"AuthorizationExpires": "May, 05 May 2020 06:13:06 GMT",
"NextAuthorizationAttempt": "February, 05 Feb 2020 18:18:07 GMT",
"LastAuthorizationAttempt": "February, 05 Feb 2020 06:18:07 GMT"
},
"Registration": {
"RegistrationStatus": "REGISTERED",
"InitialRegistration": "February, 05 Feb 2020 05:59:04 GMT",
"RegistrationExpires": "February, 04 Feb 2021 05:54:03 GMT",
"NextRenewalAttempt": "August, 03 Aug 2020 05:59:04 GMT"
}
}
```

This example retrieves the Smart Licensing Status information using cURL.

```
curl -X GET -k -i 'https://<Expressway FQDN or IP address>/api/v1/status/common/smartlicensing/licensing’
```

| URL | GET https://<Expressway FQDN or IP address>/api/v1/provisioning/common/dns/dnsserver |
|---|---|
| Request body | This operation does not require a request body. |
| Response body | { 
"DefaultDNSServers": 
 {
 "index": 2, 
"address": "10.0.0.2" 
 }
 } |

| URL | POST https://<Expressway FQDN or IP address>/api/v1/provisioning/common/dns/dnsserver' |
|---|---|
| Request body | { 
"DefaultDNSServers": 
 {
 "index": 2, 
"address": "10.0.0.2" 
 }
 } |
| Response body | {
"Message": "The operation was successful"
} |

| URL | PUT https://<Expressway FQDN or IP address>/api/v1/provisioning/common/dns/dnsserver |
|---|---|
| Request body | { 
"DefaultDNSServers": 
 {
 "index": 2, 
"address": "10.0.0.3" 
 }
 } |
| Response body | {
"Message": "The operation was successful"
} |

| URL | DELETE https://<Expressway FQDN or IP address>/api/v1/provisioning/common/dns/dnsserver |
|---|---|
| Request body | {
 "index": 2 
 } |
| Response body | {
"Message": "The operation was successful"
} |

| URL | GET https://<Expressway FQDN or IP address>/api/v1/provisioning/common/time/ntpserver |
|---|---|
| Request body | This operation does not require a request body. |
| Response body | {
"index": 5,
"KeyId": 1,
"Hash": "sha1",
"Authentication": "disabled",
"Address": "10.0.0.1"
} |

| URL | POST https://<Expressway FQDN or IP Address>/api/v1/provisioning/common/time/ntpserver |
|---|---|
| Request body | {
"index": 6,
"Address": "10.0.0.2",
"KeyId": 1,
"Hash": "sha1",
"Authentication": "disabled"
} |
| Response body | {
"Message": "The operation was successful"
} |

| URL | PUT https://<Expressway FQDN or IP address>/api/v1/provisioning/common/time/ntpserver |
|---|---|
| Request body | {
"index": 6,
"Address": "10.0.0.3",
"KeyId": 1,
"Hash": "sha1",
"Authentication": "disabled"
} |
| Response body | {
"Message": "The operation was successful"
} |

| URL | DELETE https://<Expressway FQDN or IP address>/api/v1/provisioning/common/time/ntpserver |
|---|---|
| Request body | {
 "index": 6 
 } |
| Response body | {
"Message": "The operation was successful"
} |

| URL | GET https://<Expressway FQDN or IP address>/api/v1/status/common/smartlicensing/licensing |
|---|---|
| Request body | This operation does not require a request body. |
| Response body | {
"ExportControlledFunctionality": "True",
"VirtualAccount": "Expressway",
"SmartAccount": "testaccount.cisco.com",
"Authorization": {
"LicenseAuthorizationStatus": "OUT OF COMPLIANCE",
"AuthorizationExpires": "May, 05 May 2020 06:13:06 GMT",
"NextAuthorizationAttempt": "February, 05 Feb 2020 18:18:07 GMT",
"LastAuthorizationAttempt": "February, 05 Feb 2020 06:18:07 GMT"
},
"Registration": {
"RegistrationStatus": "REGISTERED",
"InitialRegistration": "February, 05 Feb 2020 05:59:04 GMT",
"RegistrationExpires": "February, 04 Feb 2021 05:54:03 GMT",
"NextRenewalAttempt": "August, 03 Aug 2020 05:59:04 GMT"
}
} |