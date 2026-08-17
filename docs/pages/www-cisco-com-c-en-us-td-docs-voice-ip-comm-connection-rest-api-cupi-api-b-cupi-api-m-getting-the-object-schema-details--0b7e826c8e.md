---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-getting-the-object-schema-details--0b7e826c8e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_getting-the-object-schema-details.html
retrieved_at: 2026-08-17T03:47:03.042068+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- Getting the Object Schema
	 Details

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- Getting the Object Schema
	 Details

- Cisco Unity                              	 Connection Provisioning Interface (CUPI) API -- Getting the Object Schema                              	 Details

- Getting the Schema                              	 Details

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- Getting the Object Schema
                     	 Details

Links to Other API pages: Cisco_Unity_Connection_APIs

## Getting the Schema
                        	 Details

All the schema details for all supported object types can be obtained by
                           		going to the REST schema page using the URL:

```
http://{server name}/vmrest/schema
```

All the objects supported will come up in a list, each as a link that
                           		will take you to a page detailing which items of information will be returned
                           		when fetching that object.

```
http://{server name}/vmrest/users/{object_id}
```

If, however, you are getting a list of users or searching for one or
                           		more users with a query parameter like this:

```
http://{server name}/vmrest/users?query=(alias%20is%20operator)
```

Then you will get a subset of user properties on each user returned in
                           		the list. This is an optimization since users have such a large amount of data
                           		associated with them that returning all of those properties for each user on a
                           		potentially large list is very inefficient. Make sure your application accounts
                           		for this.

| Note | In the case of users the schema shows what will come back when
                                       		  fetching the full user data using a URL like this: |
|---|---|