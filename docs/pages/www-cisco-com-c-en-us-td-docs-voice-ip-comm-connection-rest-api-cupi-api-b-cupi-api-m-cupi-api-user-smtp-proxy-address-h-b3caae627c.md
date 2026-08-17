---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-api-user-smtp-proxy-address-h-b3caae627c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_cupi-api-user-smtp-proxy-address.html
retrieved_at: 2026-08-17T03:48:38.260668+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User SMTP Proxy Address

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User SMTP Proxy Address

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- User SMTP Proxy Address

## SMTP Proxy Address
                        	 API

### Listing the SMTP
                           	 proxy Address

```
GET https://<connection-server>/vmrest/smtpproxyaddresses?query=(GlobalUserObjectId%20is%20<user-objectid>)
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
<SmtpProxyAddresses total="2">
  <SmtpProxyAddress>
    <URI>/vmrest/smtpproxyaddresses/3d71d2ed-5baf-48c4-bf25-875bca56e30e</URI>
    <ObjectId>3d71d2ed-5baf-48c4-bf25-875bca56e30e</ObjectId>
    <SmtpAddress>chhavi@we.com</SmtpAddress>
    <ObjectGlobalUserObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</ObjectGlobalUserObjectId>
    <ObjectGlobalUserURI>/vmrest/globalusers/9375d893-c8eb-437b-90bf-7de4b1d0c3e8</ObjectGlobalUserURI>
   </SmtpProxyAddress>
  <SmtpProxyAddress>
   <URI>/vmrest/smtpproxyaddresses/062fc8cc-a0aa-4ad7-b74c-9589dd95cb1c</URI>
   <ObjectId>062fc8cc-a0aa-4ad7-b74c-9589dd95cb1c</ObjectId>
   <SmtpAddress>chhavi@5.co</SmtpAddress>
   <ObjectGlobalUserObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</ObjectGlobalUserObjectId>
   <ObjectGlobalUserURI>/vmrest/globalusers/9375d893-c8eb-437b-90bf-7de4b1d0c3e8</ObjectGlobalUserURI>
  </SmtpProxyAddress>
</SmtpProxyAddresses>
```

```
Response Code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/smtpproxyaddresses?query=(GlobalUserObjectId%20is%20<user-objectid>)
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
{
  "@total": "2",
  "SmtpProxyAddress":
  [
  {
   "URI": "/vmrest/smtpproxyaddresses/3d71d2ed-5baf-48c4-bf25-875bca56e30e",
   "ObjectId": "3d71d2ed-5baf-48c4-bf25-875bca56e30e",
   "SmtpAddress": "john@we.com",
   "ObjectGlobalUserObjectId": "9375d893-c8eb-437b-90bf-7de4b1d0c3e8",
   "ObjectGlobalUserURI": "/vmrest/globalusers/9375d893-c8eb-437b-90bf-7de4b1d0c3e8"
  },
  {
   "URI": "/vmrest/smtpproxyaddresses/062fc8cc-a0aa-4ad7-b74c-9589dd95cb1c",
   "ObjectId": "062fc8cc-a0aa-4ad7-b74c-9589dd95cb1c",
   "SmtpAddress": "mary@5.co",
   "ObjectGlobalUserObjectId": "9375d893-c8eb-437b-90bf-7de4b1d0c3e8",
   "ObjectGlobalUserURI": "/vmrest/globalusers/9375d893-c8eb-437b-90bf-7de4b1d0c3e8"
  }
]
}
```

```
Response Code: 200
```

### Create an SMTP
                           	 Proxy Address

The mandatory fields for creation
                                 		  are SmtpAddress and ObjectGlobalUserObjectId

```
POST https://<connection-server>vmrest/smtpproxyaddresses
```

```
<SmtpProxyAddress>
  <SmtpAddress>Texoma@cisco.com</SmtpAddress>
  <ObjectGlobalUserObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</ObjectGlobalUserObjectId>
</SmtpProxyAddress>
```

The following is the response from the above *POST* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 201
/vmrest/smtpproxyaddresses/8375d893-c8eb-437b-90bf-7de4b1d0c3e8
```

JSON Example

```
POST https://<connection-server>vmrest/smtpproxyaddresses
Accept: application/json
Content-type:  application/json
Connection: keep-alive
```

```
{
  "SmtpAddress":"Texoma@cisco.com",
  "ObjectGlobalUserObjectId":"9375d893-c8eb-437b-90bf-7de4b1d0c3e8"
}
```

The following is the response from the above *POST* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 201
/vmrest/smtpproxyaddresses/8375d893-c8eb-437b-90bf-7de4b1d0c3e8
```

### Update SMTP proxy
                           	 Address

```
PUT https://<connection-server>/vmrest/smtpproxyaddresses/<objectid>
```

```
<SmtpProxyAddress>
  <SmtpAddress>Texoma@cisco.com</SmtpAddress>
</SmtpProxyAddress>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

```
PUT https://<connection-server>vmrest/smtpproxyaddresses/<object_id>
Accept: application/json
Content-type:  application/json
Connection: keep-alive
```

```
{
  "SmtpAddress":"Texoma@cisco.com"
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Delete SMTP Proxy
                           	 Address

```
DELETE https://<connection-server>/vmrest/smtpproxyaddresses/<objectid>
```

The following is the response from the above *DELETE* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

```
DELETE https://<connection-server>vmrest/smtpproxyaddresses/<objectid>
Accept: application/json
Content-type:  application/json
Connection: keep-alive
```

The following is the response from the above *DELETE* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Explanation of
                           	 Data Fields

| GET https://<connection-server>/vmrest/smtpproxyaddresses?query=(GlobalUserObjectId%20is%20<user-objectid>) |
|---|

| <SmtpProxyAddresses total="2">
  <SmtpProxyAddress>
    <URI>/vmrest/smtpproxyaddresses/3d71d2ed-5baf-48c4-bf25-875bca56e30e</URI>
    <ObjectId>3d71d2ed-5baf-48c4-bf25-875bca56e30e</ObjectId>
    <SmtpAddress>chhavi@we.com</SmtpAddress>
    <ObjectGlobalUserObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</ObjectGlobalUserObjectId>
    <ObjectGlobalUserURI>/vmrest/globalusers/9375d893-c8eb-437b-90bf-7de4b1d0c3e8</ObjectGlobalUserURI>
   </SmtpProxyAddress>
  <SmtpProxyAddress>
   <URI>/vmrest/smtpproxyaddresses/062fc8cc-a0aa-4ad7-b74c-9589dd95cb1c</URI>
   <ObjectId>062fc8cc-a0aa-4ad7-b74c-9589dd95cb1c</ObjectId>
   <SmtpAddress>chhavi@5.co</SmtpAddress>
   <ObjectGlobalUserObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</ObjectGlobalUserObjectId>
   <ObjectGlobalUserURI>/vmrest/globalusers/9375d893-c8eb-437b-90bf-7de4b1d0c3e8</ObjectGlobalUserURI>
  </SmtpProxyAddress>
</SmtpProxyAddresses> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/smtpproxyaddresses?query=(GlobalUserObjectId%20is%20<user-objectid>)
Accept: application/json
Connection: keep-alive |
|---|

| {
  "@total": "2",
  "SmtpProxyAddress":
  [
  {
   "URI": "/vmrest/smtpproxyaddresses/3d71d2ed-5baf-48c4-bf25-875bca56e30e",
   "ObjectId": "3d71d2ed-5baf-48c4-bf25-875bca56e30e",
   "SmtpAddress": "john@we.com",
   "ObjectGlobalUserObjectId": "9375d893-c8eb-437b-90bf-7de4b1d0c3e8",
   "ObjectGlobalUserURI": "/vmrest/globalusers/9375d893-c8eb-437b-90bf-7de4b1d0c3e8"
  },
  {
   "URI": "/vmrest/smtpproxyaddresses/062fc8cc-a0aa-4ad7-b74c-9589dd95cb1c",
   "ObjectId": "062fc8cc-a0aa-4ad7-b74c-9589dd95cb1c",
   "SmtpAddress": "mary@5.co",
   "ObjectGlobalUserObjectId": "9375d893-c8eb-437b-90bf-7de4b1d0c3e8",
   "ObjectGlobalUserURI": "/vmrest/globalusers/9375d893-c8eb-437b-90bf-7de4b1d0c3e8"
  }
]
} |
|---|

| Response Code: 200 |
|---|

| POST https://<connection-server>vmrest/smtpproxyaddresses |
|---|

| <SmtpProxyAddress>
  <SmtpAddress>Texoma@cisco.com</SmtpAddress>
  <ObjectGlobalUserObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</ObjectGlobalUserObjectId>
</SmtpProxyAddress> |
|---|

| Response Code: 201
/vmrest/smtpproxyaddresses/8375d893-c8eb-437b-90bf-7de4b1d0c3e8 |
|---|

| POST https://<connection-server>vmrest/smtpproxyaddresses
Accept: application/json
Content-type:  application/json
Connection: keep-alive |
|---|

| {
  "SmtpAddress":"Texoma@cisco.com",
  "ObjectGlobalUserObjectId":"9375d893-c8eb-437b-90bf-7de4b1d0c3e8"
} |
|---|

| Response Code: 201
/vmrest/smtpproxyaddresses/8375d893-c8eb-437b-90bf-7de4b1d0c3e8 |
|---|

| PUT https://<connection-server>/vmrest/smtpproxyaddresses/<objectid> |
|---|

| <SmtpProxyAddress>
  <SmtpAddress>Texoma@cisco.com</SmtpAddress>
</SmtpProxyAddress> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>vmrest/smtpproxyaddresses/<object_id>
Accept: application/json
Content-type:  application/json
Connection: keep-alive |
|---|

| {
  "SmtpAddress":"Texoma@cisco.com"
} |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/smtpproxyaddresses/<objectid> |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>vmrest/smtpproxyaddresses/<objectid>
Accept: application/json
Content-type:  application/json
Connection: keep-alive |
|---|

| Response Code: 204 |
|---|

| Field Name | Data Type | Operation | Description |
|---|---|---|---|
| ObjectId | String(36) | Read Only | The primary key for this table. |
| SmtpAddress | String(320) | Read/Write | The full SMTP proxy address for this
                                             					 object. |
| ObjectGlobalUserObjectId | String(36) | Read/Write | The unique identifier of the Global User to
                                             					 which this SMTP address belongs. |