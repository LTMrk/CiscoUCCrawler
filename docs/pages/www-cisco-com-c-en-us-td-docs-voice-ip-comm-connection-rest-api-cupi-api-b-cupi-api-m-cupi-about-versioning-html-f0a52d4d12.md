---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-about-versioning-html-f0a52d4d12
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_cupi_about_versioning.html
retrieved_at: 2026-08-17T03:47:06.951833+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- About Versioning

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- About Versioning

- Cisco Unity                              	 Connection Provisioning Interface (CUPI) API -- About Versioning

- About                              	 Versioning

- Getting Unity Connection Version

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- About Versioning

Links to Other API pages: Cisco_Unity_Connection_APIs

## About
                        	 Versioning

Cisco Unity Connection REST
                           		interfaces essentially are not versioned. There are several mechanisms in place
                           		to ease forward and backward compatibility:

```
<VersionInformation>
  <name>vmrest</name>
  <version>8.0.0.229</version>
</VersionInformation>
```

This means that if we add a field to a resource in a future release,
                                 			 and the new resource is sent to an older server, the operation will complete
                                 			 (with the exception of updating the field that it does not have).

Clients ignore new fields.

The XML schema files that are provided for clients include a
                                 			 provision for arbitrary fields to be added at the end. This means that when a
                                 			 new field is added to a resource exposed by the server, it will not affect
                                 			 client code.

New resources are added at new URLs.

Adding a new resource means adding a new URL, not changing existing
                                 			 URLs. This means that existing client code can continue to run against the new
                                 			 version without change.

## Getting Unity Connection Version

To get the active master version of Cisco Unity Connection, do the following GET request:

```
GET http://<connection-server>/vmrest/version/product/
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                           by you:

```
<VersionInformation>
<name>Cisco Unity Connection Version</name>
<version>11.5.1.17108-2</version>
</VersionInformation>
```

```
Response Code: 200
```

| GET http://<connection-server>/vmrest/version/product/ |
|---|

| <VersionInformation>
<name>Cisco Unity Connection Version</name>
<version>11.5.1.17108-2</version>
</VersionInformation> |
|---|

| Response Code: 200 |
|---|