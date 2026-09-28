---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-api-alternat-names-api-html-4d89de4273
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_cupi-api-alternat-names-api.html
retrieved_at: 2026-08-17T03:47:44.520308+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- Alternate Names API

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- Alternate Names API

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- Alternate Names API

Links to Other API pages: Cisco_Unity_Connection_APIs

## Alternate Names
                        	 API

### Listing the
                           	 Alternate Names

```
GET https://<connection-server>/vmrest/alternatenames?query=(GlobalUserObjectId%20is%20<user-objectid>)
```

The following is the response from the above *GET* request and the
                              		actual response will depend upon the information given by you:

```
<AlternateNames total="3">
   <AlternateName>
   <URI>/vmrest/alternatenames/5fa9e143-d9d3-42ea-9370-e763d8ee319d</URI>
   <FirstName>sd</FirstName>
   <LastName>asd</LastName>
   <ObjectId>5fa9e143-d9d3-42ea-9370-e763d8ee319d</ObjectId>
   <GlobalUserObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</GlobalUserObjectId>
   <GlobalUserURI>/vmrest/globalusers/9375d893-c8eb-437b-90bf-7de4b1d0c3e8</GlobalUserURI>
  </AlternateName>
   <AlternateName>
   <URI>/vmrest/alternatenames/89b0a8b9-68d7-445c-acb9-aaf2a569d5ef</URI>
   <FirstName>sqdas</FirstName>
   <LastName>asqd</LastName>
   <ObjectId>89b0a8b9-68d7-445c-acb9-aaf2a569d5ef</ObjectId>
   <GlobalUserObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</GlobalUserObjectId>
   <GlobalUserURI>/vmrest/globalusers/9375d893-c8eb-437b-90bf-7de4b1d0c3e8</GlobalUserURI>
  </AlternateName>
  <AlternateName>
   <URI>/vmrest/alternatenames/dc03dec6-a9df-4d2b-8972-78c3bceec987</URI>
   <FirstName>sdwds</FirstName>
   <LastName>asd</LastName>
   <ObjectId>dc03dec6-a9df-4d2b-8972-78c3bceec987</ObjectId>
   <GlobalUserObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</GlobalUserObjectId>
   <GlobalUserURI>/vmrest/globalusers/9375d893-c8eb-437b-90bf-7de4b1d0c3e8</GlobalUserURI>
  </AlternateName>
</AlternateNames>
```

```
Response Code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/alternatenames?query=(GlobalUserObjectId%20is%20<user-objectid>)
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                              		actual response will depend upon the information given by you:

```
Response Code: 200
```

### Create a new
                           	 Alternate Name

The mandatory fields for creation
                              		of an alternate name are: FirstName, LastName, and GlobalUserObjectId. The URI
                              		for getting partition object ID use:

```
GET https://<connection-server>/vmrest/partitions
```

The following URI is fetched from the response body of above URI:

```
https://<connection-server>/vmrest/users/<user-objectid>
```

The Request URI:

```
POST https://<connection-server>/vmrest/alternatenames
```

```
<AlternateName>
  <FirstName>sdwds</FirstName>
  <LastName>asd</LastName>
  <GlobalUserObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</GlobalUserObjectId>
</AlternateName>
```

The following is the response from the above *POST* request and the
                              		actual response will depend upon the information given by you:

```
Response Code: 201
/vmrest/alternatenames/f375d893-c8eb-437b-90bf-7de4b1d0c3e8
```

JSON Example

```
POST https://<connection-server>/vmrest/alternatenames
Accept: application/json
Content-type:  application/json
Connection: keep-alive
Request body:
{
  "FirstName":"and",
  "LastName":"gupta",
  "GlobalUserObjectId":"9375d893-c8eb-437b-90bf-7de4b1d0c3e8"
}
```

The following is the response from the above *POST* request and the
                              		actual response will depend upon the information given by you:

```
Response Code: 201
/vmrest/alternatenames/f375d893-c8eb-437b-90bf-7de4b1d0c3e8
```

### Update Alternate
                           	 Names

```
PUT https://<connection-server>/vmrest/alternatenames/<objectid>
```

```
<AlternateName>
  <FirstName>kapil</FirstName>
  <LastName>gupta</LastName>
</AlternateName>
```

The following is the response from the above *PUT* request and the
                              		actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

```
PUT https://<connection-server>/vmrest/alternatenames/<objectid>
Accept: application/json
Content-type:  application/json
Connection: keep-alive
{
"FirstName":"John",
"LastName":"gupta"
}
```

The following is the response from the above *PUT* request and the
                              		actual response will depend upon the information given by you:

```
Response code: 204
```

### Delete Alternate
                           	 Names

```
DELETE https://<connection-server>/vmrest/alternatenames/<objectid>
```

The following is the response from the above *DELETE* request and the
                              		actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

```
DELETE https://<connection-server>/vmrest/alternatenames/<objectid>
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *DELETE* request and the
                              		actual response will depend upon the information given by you:

```
Response code: 204
```

### Reference