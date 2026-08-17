---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-examples-of-basic-operations-html-950b3b7acd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_examples-of-basic-operations.html
retrieved_at: 2026-08-17T03:47:19.481856+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- Examples of Basic
	 Operations

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- Examples of Basic
	 Operations

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- Examples of Basic
                     	 Operations

Links to Other API pages: Cisco_Unity_Connection_APIs

## Reading a User's
                        	 Information

To read a user's information, do
                           		the following GET request:

```
GET http://<connection-server>/vmrest/users/{objectid}
```

## Creating a
                        	 User

To create a user account, do the
                           		following POST request:

```
POST http://<connection-server>/vmrest/users?templateAlias=voicemailusertemplate
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<User>
<Alias>jdoe</Alias>
<DtmfAccessId>7890</DtmfAccessId>
</User>
```

The following is the result of the above POST request:

```
201 Created
```

The HTTP response will include the full URI to the newly created user in
                           		the Location header.

## Modifying a
                        	 User

To modify a user account, do the
                           		following PUT request:

```
PUT http://<connection-server>/vmrest/users/{objectid}
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<User>
<DisplayName>johnd</DisplayName>
</User>
```

The following is the result of the above PUT request:

```
204 Accepted
```

## Deleting a
                        	 User

To delete a user account, do the
                           		following DELETE request:

```
DELETE http://<connection-server>/vmrest/users/{objectid}
```

The following is the result of the above DELETE request:

```
200 OK
```

## Searching for a
                        	 User

To search for a user account, do
                           		the following GET request:

```
GET http://<connection-server>/vmrest/users?query=(alias%20startswith%20ab)
```

## Reset the MWI for
                        	 a User

The reset the MWI for a user:

```
POST http://<connection-server>/vmrest/users/{objectid}?method=resetmwi
```