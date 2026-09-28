---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-for-end-user-b-cupi-api-for-end-user-b-cupi-api-70b636fcb5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API_for_End_User/b_CUPI_API_for_End_User/b_CUPI_API_for_End_User_chapter_01001.html
retrieved_at: 2026-08-21T08:04:55.154469+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

Updated: January 18, 2019

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- System Configuration

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- System Configuration

- Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- System Configuration

- About SMTP Proxy Addresses

- Listing and Viewing

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- System Configuration

## About SMTP Proxy Addresses

This page contains information on how to use the API to list SMTP Proxy Addresses for a user.

## Listing and Viewing

The following is an example of a GET that lists all SMTP Proxy Addresses for a user:

```
GET http://<connection-server>/vmrest/user/smtpproxyaddresses
```

The following is the response from the above GET request:

```
200
OK
<?xml version="1.0" encoding="UTF-8"?>
<SmtpProxyAddresses>
  <SmtpProxyAddress>
    <URI>/vmrest/user/smtpproxyaddresses/9fd21b87-1509-42f1-88ce-3f36122c68ee</URI>
    <ObjectId>9fd21b87-1509-42f1-88ce-3f36122c68ee</ObjectId>
    <SmtpAddress>somedude@somewhere.com</SmtpAddress>
  </SmtpProxyAddress>
  <SmtpProxyAddress>
    <URI>/vmrest/user/smtpproxyaddresses/fc107ad8-b9e5-409e-b0bc-62e295c7532e</URI>
    <ObjectId>fc107ad8-b9e5-409e-b0bc-62e295c7532e</ObjectId>
    <SmtpAddress>someotherdude@somewhereelse.com</SmtpAddress>
  </SmtpProxyAddress>
</SmtpProxyAddresses>
```

To retrieve a specific SMTP Proxy Address for a user by its object ID:

```
GET http://<connection-server>/vmrest/user/smtpproxyaddresses/<objectid>
```

| GET http://<connection-server>/vmrest/user/smtpproxyaddresses |
|---|

| 200
OK
<?xml version="1.0" encoding="UTF-8"?>
<SmtpProxyAddresses>
  <SmtpProxyAddress>
    <URI>/vmrest/user/smtpproxyaddresses/9fd21b87-1509-42f1-88ce-3f36122c68ee</URI>
    <ObjectId>9fd21b87-1509-42f1-88ce-3f36122c68ee</ObjectId>
    <SmtpAddress>somedude@somewhere.com</SmtpAddress>
  </SmtpProxyAddress>
  <SmtpProxyAddress>
    <URI>/vmrest/user/smtpproxyaddresses/fc107ad8-b9e5-409e-b0bc-62e295c7532e</URI>
    <ObjectId>fc107ad8-b9e5-409e-b0bc-62e295c7532e</ObjectId>
    <SmtpAddress>someotherdude@somewhereelse.com</SmtpAddress>
  </SmtpProxyAddress>
</SmtpProxyAddresses> |
|---|

| GET http://<connection-server>/vmrest/user/smtpproxyaddresses/<objectid> |
|---|