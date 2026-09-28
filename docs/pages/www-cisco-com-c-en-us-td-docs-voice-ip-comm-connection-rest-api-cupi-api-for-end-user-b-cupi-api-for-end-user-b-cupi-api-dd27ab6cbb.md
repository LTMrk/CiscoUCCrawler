---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-for-end-user-b-cupi-api-for-end-user-b-cupi-api-dd27ab6cbb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API_for_End_User/b_CUPI_API_for_End_User/b_CUPI_API_for_End_User_chapter_010000.html
retrieved_at: 2026-08-21T08:05:24.522478+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

Updated: January 24, 2019

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- Directory API

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- Directory API

# Cisco Unity Connection Provisioning Interface (CUPI) API -- Directory API

## Directory API

A URI is provided for users to allow them to search the directory and find addressable objects that can be used to send messages,
                              be added to a private list, and so on. The directory can be searched several different ways. The example below searches for
                              names that start with "user". Only name and extension fields can be used as a search filter. Searching the Directory This
                              request can be used to search for a user in the directory. Note that the maximum number of objects that can be returned from
                              a search is 100 objects.

```
GET https://<connection-server>/vmrest/directory/addressable?query=(name%20startswith%20user)
```

The following is the response from the *GET* request and the actual response will depend upon the information given by you:

```
<Addresses total="2">
 <Address>
  <ObjectId>8dd65570-a1e8-4c85-95bc-0a8160877238</ObjectId>
  <Type>SUBSCRIBER</Type>
  <DisplayName>UserG</DisplayName>
  <SmtpAddress>userg@cuc-install-43.cisco.com</SmtpAddress>
  <DtmfAccessId>1019</DtmfAccessId>
 </Address>
 <Address>
  <ObjectId>7c897859-282f-43b0-9cab-1933e9b844f3</ObjectId>
  <Type>SUBSCRIBER</Type>
  <DisplayName>UserD</DisplayName>
  <SmtpAddress>userd@cuc-install-43.cisco.com</SmtpAddress>
  <DtmfAccessId>1018</DtmfAccessId>
 </Address>
</Addresses>
```

```
Response Code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/directory/addressable?query=(name%20startswith%20user)
Accept: application/json
Connection: keep-alive
```

The following is the response from the *GET* request and the actual response will depend upon the information given by you:

```
{
"@total": "2","Address": 
[
  {
  "ObjectId": "8dd65570-a1e8-4c85-95bc-0a8160877238",
  "Type": "SUBSCRIBER",
  "DisplayName": "UserG",
  "SmtpAddress": "userg@cuc-install-43.cisco.com",
  "DtmfAccessId": "1019"
  },
  {
  "ObjectId": "7c897859-282f-43b0-9cab-1933e9b844f3",
  "Type": "SUBSCRIBER",
  "DisplayName": "UserD",
  "SmtpAddress": "userd@cuc-install-43.cisco.com",
  "DtmfAccessId": "1018"
  }
]
}
```

```
Response Code: 200
```

## Searching the Directory for a Particular User

To search the directory for names that exactly match "user", the following query is used:

```
GET https://<connection-server>/vmrest/directory/addressable?query=(name%20is%20user)
```

The following is the response from the *GET* request and the actual response will depend upon the information given by you:

```
<Address>
  <ObjectId>7c897859-282f-43b0-9cab-1933e9b844f3</ObjectId>
  <Type>SUBSCRIBER</Type>
  <DisplayName>user</DisplayName>
  <SmtpAddress>user@cuc-install-43.cisco.com</SmtpAddress>
  <DtmfAccessId>1018</DtmfAccessId>
</Address>
```

```
Response Code: 200
```

The following is the response from the *GET* request and the actual response will depend upon the information given by you:

```
{
  “ObjectId”: “7c897859-282f-43b0-9cab-1933e9b844f3”
  “Type”: “SUBSCRIBER”
  “DisplayName”: “user”
  “SmtpAddress”: “user@cuc-install-43.cisco.com”
  “DtmfAccessId”: “1018”
}
```

```
Response Code: 200
```

## Explanation of Data Field

Parameter

Operation

Data Type

Comments

ObjectId

Read Only

String

Unique identifier of the directory entry.

Type

Read Only

String

Indicates type of user. Value is SUBSCRIBER for end users.

DisplayName

Read Only

String

SmtpAddress

Read Only

String

SMTP address of the end user.

DtmfAccessId

Read Only

String

Extension number of the end user.

Read Only

String

| GET https://<connection-server>/vmrest/directory/addressable?query=(name%20startswith%20user) |
|---|

| <Addresses total="2">
 <Address>
  <ObjectId>8dd65570-a1e8-4c85-95bc-0a8160877238</ObjectId>
  <Type>SUBSCRIBER</Type>
  <DisplayName>UserG</DisplayName>
  <SmtpAddress>userg@cuc-install-43.cisco.com</SmtpAddress>
  <DtmfAccessId>1019</DtmfAccessId>
 </Address>
 <Address>
  <ObjectId>7c897859-282f-43b0-9cab-1933e9b844f3</ObjectId>
  <Type>SUBSCRIBER</Type>
  <DisplayName>UserD</DisplayName>
  <SmtpAddress>userd@cuc-install-43.cisco.com</SmtpAddress>
  <DtmfAccessId>1018</DtmfAccessId>
 </Address>
</Addresses> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/directory/addressable?query=(name%20startswith%20user)
Accept: application/json
Connection: keep-alive |
|---|

| {
"@total": "2","Address": 
[
  {
  "ObjectId": "8dd65570-a1e8-4c85-95bc-0a8160877238",
  "Type": "SUBSCRIBER",
  "DisplayName": "UserG",
  "SmtpAddress": "userg@cuc-install-43.cisco.com",
  "DtmfAccessId": "1019"
  },
  {
  "ObjectId": "7c897859-282f-43b0-9cab-1933e9b844f3",
  "Type": "SUBSCRIBER",
  "DisplayName": "UserD",
  "SmtpAddress": "userd@cuc-install-43.cisco.com",
  "DtmfAccessId": "1018"
  }
]
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/directory/addressable?query=(name%20is%20user) |
|---|

| <Address>
  <ObjectId>7c897859-282f-43b0-9cab-1933e9b844f3</ObjectId>
  <Type>SUBSCRIBER</Type>
  <DisplayName>user</DisplayName>
  <SmtpAddress>user@cuc-install-43.cisco.com</SmtpAddress>
  <DtmfAccessId>1018</DtmfAccessId>
</Address> |
|---|

| Response Code: 200 |
|---|

| {
  “ObjectId”: “7c897859-282f-43b0-9cab-1933e9b844f3”
  “Type”: “SUBSCRIBER”
  “DisplayName”: “user”
  “SmtpAddress”: “user@cuc-install-43.cisco.com”
  “DtmfAccessId”: “1018”
} |
|---|

| Response Code: 200 |
|---|

| Parameter | Operation | Data Type | Comments |
|---|---|---|---|
| ObjectId | Read Only | String | Unique identifier of the directory entry. |
| Type | Read Only | String | Indicates type of user. Value is SUBSCRIBER for end users. |
| DisplayName | Read Only | String | Display name of the end user. |
| SmtpAddress | Read Only | String | SMTP address of the end user. |
| DtmfAccessId | Read Only | String | Extension number of the end user. |
|  | Read Only | String |  |