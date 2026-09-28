---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-getting-the-object-count-without-g-1bfaa58236
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_getting-the-object-count-without-getting-the-objects.html
retrieved_at: 2026-08-17T03:47:23.462025+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- Getting the Object Count
	 Without Getting the Objects

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- Getting the Object Count
	 Without Getting the Objects

- Cisco Unity                              	 Connection Provisioning Interface (CUPI) API -- Getting the Object Count                              	 Without Getting the Objects

- Getting the Object                              	 Count Without Getting the Objects

- Examples

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- Getting the Object Count
                     	 Without Getting the Objects

Links to Other API pages: Cisco_Unity_Connection_APIs

## Getting the Object
                        	 Count Without Getting the Objects

For performance reasons, you can
                           		retrieve an object count without retrieving the objects. For example, you might
                           		have over 1000 users and you want to know the exact user count. To speed up the
                           		query, you can retrieve only the count of users, without retrieving the
                           		payload, by using and setting the query parameter "pageNumber" or "rowsPerPage"
                           		to 0, as follows:

## Examples

The following example returns the
                           		number of users:

```
GET http://<connection-server>/vmrest/users?rowsPerPage=0
```

The following example returns the number of users whose alias starts
                           		with "John":

```
GET http://<connection-server>/vmrest/users?query=(alias%20startswith%20John)&pageNumber=0
```