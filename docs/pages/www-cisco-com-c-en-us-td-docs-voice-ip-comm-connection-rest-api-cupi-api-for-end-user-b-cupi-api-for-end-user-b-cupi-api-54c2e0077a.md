---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-for-end-user-b-cupi-api-for-end-user-b-cupi-api-54c2e0077a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API_for_End_User/b_CUPI_API_for_End_User/b_CUPI_API_for_End_User_chapter_010110.html
retrieved_at: 2026-08-21T08:05:45.474843+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

Updated: January 24, 2019

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- Private List API

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- Private List API

# Cisco Unity Connection Provisioning Interface (CUPI) API -- Private List API

## Listing All the Private Lists

End User can get the list of all private lists or a particular private list. The request below can be used to get the list
                              of private lists:

```
GET https://<connection-server>/vmrest/user/privatelists
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                              by you:

```
<PrivateLists>
  <PrivateList>
  <URI>/vmrest/user/privatelists/3277f872-b899-45f2-9056-8a786e28b694</URI>
  <ObjectId>3277f872-b899-45f2-9056-8a786e28b694</ObjectId>
  <DisplayName>Texoma_PrivateList</DisplayName>
  <NumericId>1</NumericId>
  <PrivateListMembersURI>/vmrest/user/privatelists/3277f872-b899-45f2-9056-  8a786e28b694/privatelistmembers</PrivateListMembersURI>
  </PrivateList>
</PrivateLists>
```

```
Response Code: 200
```

## Listing a Particular Private List

### JSON Example

```
GET https://<connection-server>/vmrest/user/privatelists/<privatelist-objectid>
```

```
The following is the response from the above *GET* request and the actual response will depend upon the information given by you:
```

```
<PrivateList>
  <URI>/vmrest/user/privatelists/3277f872-b899-45f2-9056-8a786e28b694</URI>
  <ObjectId>3277f872-b899-45f2-9056-8a786e28b694</ObjectId>
  <DisplayName>Texoma_PrivateList</DisplayName>
  <NumericId>1</NumericId>
  <PrivateListMembersURI>/vmrest/user/privatelists/3277f872-b899-45f2-9056-8a786e28b694/privatelistmembers</PrivateListMembersURI>
</PrivateList>
```

```
GET https://<connection-server>/vmrest/user/privatelists
Accept: application/json
Content-type: application/json
Connection: keep-alive 
{
"PrivateLists":
{
  "PrivateList":
  {
  "URI": "/vmrest/user/privatelists/3277f872-b899-45f2-9056-8a786e28b694",
  "ObjectId": "3277f872-b899-45f2-9056-8a786e28b694",
  "DisplayName": "Texoma_PrivateList",
  "NumericId": "1",
  "PrivateListMembersURI": "/vmrest/user/privatelists/3277f872-b899-45f2-9056-8a786e28b694/privatelistmembers"
  }
}
}
```

```
Response Code: 200
```

## Create a Private list

### JSON Example

The mandatory field for creation is DisplayName.

```
POST https://<connection-server>/vmrest/user/privatelists
```

```
<PrivateList>
  <DisplayName>Test1</DisplayName>
</PrivateList>
```

```
The following is the response from the above *POST* request and the actual response will depend upon the information given by you:
```

```
Response Code: 201
/vmrest/user/privatelists/3277f872-b899-45f2-9056-8a786e28b694
```

```
POST https://<connection-server>/vmrest/user/privatelists
Accept: application/json
Content-type: application/json
Connection: keep-alive
{  
  "PrivateList": 
  { 
  "DisplayName": "Texoma_PrivateList" 
  }
}
```

The following is the response from the above *POST* request and the actual response will depend upon the information given
                              by you:

```
Response code: 201
/vmrest/user/privatelists/3277f872-b899-45f2-9056-8a786e28b694
```

## Update Private List

### JSON Example

```
PUT https://<connection-server>/vmrest/user/privatelists/<privatelist-objectid>
```

```
<PrivateList>
  <DisplayName>Test11</DisplayName>
  <NumericId>2</NumericId>
</PrivateList>
```

Duplicate values are not allowed for both DisplayName and NumericId fields." The following is the response from the above
                              *PUT* request and the actual response will depend upon the information given by you:

```
Response Code: 204
```

```
PUT https://<connection-server>/vmrest/user/privatelists/<privatelist-objectid>
```

```
Accept: application/json
Content-type:  application/json
Connection: keep-alive
{
  "DisplayName":"Test11",
  “NumericId”:”2”
}
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                              by you:

```
Response Code: 204
```

## Delete Private List

### JSON Example

```
DELETE https://<connection-server>/vmrest/user/privatelists/<privatelist-objectid>
```

The following is the response from the above *DELETE* request and the actual response will depend upon the information given
                              by you:

```
Response Code: 204
```

```
DELETE https://<connection-server>/vmrest/user/privatelists/<privatelist-objectid>
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *DELETE* request and the actual response will depend upon the information given
                              by you:

```
Response code: 204
```

## Adding Voice Names for Private Lists

To add the voice names for private lists, use the PUT request given below, where the HTTP content type is "audio/wav" and
                              the payload content is the audio data that adds the audio as a voice name to the private list:

```
PUT https://<connection-server>/vmrest/user/privatelists/<privatelist-objectid>/voicename
```

A wav file needs to be added as the payload with audio/wav as the content type.

```
Response Code: 204
```

The voice name can always be retrieved through the URI below. It will return the audio of the voice name as an "audio/wav"
                              media type.

```
GET https://<connection-server>/vmrest/user/privatelists/<privatelist-objectid>/voicename
```

```
Response Code: 200
```

## Explanation of Data Fields

URI

Read Only

String

URI of the private list.

ObjectId

Read Only

String(36)

Unique identifier of the private list.

DisplayName

Read/Write

Display name of the private list.

NumericId

Read/Write String

Integer(4)

The numeric identifier for the personal group. From conversations, the private lists are referenced by number, so this is
                                          essentially an index.

PrivateListMembersURI

Read Only

String

URI to get members of the private list.

| Parameter | Operations | Data Type | Comments |
|---|---|---|---|
| URI | Read Only | String | URI of the private list. |
| ObjectId | Read Only | String(36) | Unique identifier of the private list. |
| DisplayName | Read/Write | String(64) | Display name of the private list. |
| NumericId | Read/Write String | Integer(4) | The numeric identifier for the personal group. From conversations, the private lists are referenced by number, so this is
                                          essentially an index. |
| PrivateListMembersURI | Read Only | String | URI to get members of the private list. |