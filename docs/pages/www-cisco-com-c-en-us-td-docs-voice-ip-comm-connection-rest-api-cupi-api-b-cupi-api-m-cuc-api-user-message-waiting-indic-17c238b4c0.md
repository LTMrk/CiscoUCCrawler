---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cuc-api-user-message-waiting-indic-17c238b4c0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_cuc-api-user-message-waiting-indicators.html
retrieved_at: 2026-08-17T03:48:09.136729+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Message Waiting
	 Indicators

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Message Waiting
	 Indicators

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- User Message Waiting
                     	 Indicators

Links to Other API pages: Cisco_Unity_Connection_APIs

## Message Waiting
                        	 Indicator (MWI) Settings API

### Listing All
                           	 MWIs

```
GET https://<connection-server>/vmrest/users/<user-objectid>/mwis
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
<Mwis total="1">
  <Mwi>
   <URI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/mwis/2c07a9ca-c041-4dfa-b0d1-7f633883a1b7</URI>   
   <SubscriberObjectId>4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1</SubscriberObjectId>
   <UserURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1</UserURI>
   <ObjectId>2c07a9ca-c041-4dfa-b0d1-7f633883a1b7</ObjectId>
   <DisplayName>MWI-1</DisplayName>
   <MwiExtension>99999</MwiExtension>
   <MwiOn>false</MwiOn>
   <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150</MediaSwitchObjectId>
   <PhoneSystemURI>/vmrest/phonesystems/ec1e2636-fc14-44fc-8cda-d6c1a3d61150</PhoneSystemURI>
   <IncludeTextMessages>false</IncludeTextMessages>
   <IncludeVoiceMessages>true</IncludeVoiceMessages>
   <IncludeFaxMessages>false</IncludeFaxMessages>
   <Active>true</Active>
   <UsePrimaryExtension>true</UsePrimaryExtension>
   <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
   </Mwi>
</Mwis>
```

```
Response Code: 200
```

### Listing Details of
                           	 a Specific MWI

```
GET https://<connection-server>/vmrest/users/<user-objectid>/mwis/<mwi-objectid>
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
<Mwi>
  <URI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/mwis/1a231793-7168-44aa-8657-aa40eda67481</URI>
  <SubscriberObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</SubscriberObjectId>
  <UserURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8</UserURI>
  <ObjectId>1a231793-7168-44aa-8657-aa40eda67481</ObjectId>
  <DisplayName>MWI</DisplayName>
  <MwiExtension>99934</MwiExtension>
  <MwiOn>false</MwiOn>
  <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150</MediaSwitchObjectId>
  <PhoneSystemURI>/vmrest/phonesystems/ec1e2636-fc14-44fc-8cda-d6c1a3d61150</PhoneSystemURI>
  <IncludeTextMessages>false</IncludeTextMessages>
  <IncludeVoiceMessages>true</IncludeVoiceMessages>
  <IncludeFaxMessages>false</IncludeFaxMessages>
  <Active>true</Active>
  <UsePrimaryExtension>true</UsePrimaryExtension>
  <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
</Mwi>
```

```
Response Code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/users/<user-objectid>/mwis/<mwi-objectid>
Accept: application/json
Connection: keep-alive
{
  "URI":"/vmrest/users/53c84cf9-c8fe-4dd5-a295-b648b72b5a2c/mwis/810ce62e-eeec-4f47-85bd-68c69a7bca66"
  "SubscriberObjectId":"53c84cf9-c8fe-4dd5-a295-b648b72b5a2c"
  "UserURI":"/vmrest/users/53c84cf9-c8fe-4dd5-a295-b648b72b5a2c"
  "ObjectId":"810ce62e-eeec-4f47-85bd-68c69a7bca66"
  "DisplayName":"MWI-1"
  "MwiExtension":"99999"
  "MwiOn":"false"
  "MediaSwitchObjectId":"e912b134-1bd0-45f9-baae-9f1e096ae3b9"
  "PhoneSystemURI":"/vmrest/phonesystems/e912b134-1bd0-45f9-baae-9f1e096ae3b9"
  "IncludeTextMessages":"false"
  "IncludeVoiceMessages":"true"
  "IncludeFaxMessages":"false"
  "Active":"true"
  "UsePrimaryExtension":"true"
  "MediaSwitchDisplayName":"PhoneSystem"
}
```

```
Response Code: 200
```

### Create a New
                           	 MWI

The mandatory fields for creation
                                 		  of a MWI are DisplayName, MediaSwitchObjectId, and MWIExtension. URI for
                                 		  getting MediaswitchObjectId:

```
GET https://<connection-server>/vmrest/phonesystems
```

```
POST https://<connection-server>/vmrest/users/<user-objectid>/mwis
```

```
<Mwi>
  <DisplayName>MWI-1</DisplayName>
  <MwiExtension>9997</MwiExtension>
  <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150</MediaSwitchObjectId>
</Mwi>
```

The following is the response from the above *POST* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 201
/vmrest/users/f82b301d-1ec8-44c6-a3ee-0012269439bf/mwis/a9159ac7-3857-480c-917d-0c599a32fc03
```

JSON Example:

To create MWI

```
POST https://<connection-server>/vmrest/users/<user-objectid>/mwis
Accept: application/json
Content-type:  application/json
Connection: keep-alive
Request Body:-
{
  "DisplayName":"MWI-1",
  "MwiExtension":9997",
  "MediaSwitchObjectId":"ec1e2636-fc14-44fc-8cda-d6c1a3d61150"
}
```

```
Response Code: 201
/vmrest/users/f82b301d-1ec8-44c6-a3ee-0012269439bf/mwis/a9159ac7-3857-480c-917d-0c599a32fc03
```

### Update a
                           	 MWI

```
PUT https://<connection-server>/vmrest/users/<user-objectid>/mwis/<mwi-objectid>
```

```
<Mwi>
  <Active>true</Active>
  <DisplayName>MWI</DisplayName>
  <MwiExtension>9997</MwiExtension>
  <MwiOn>false</MwiOn>
  <UsePrimaryExtension>true</UsePrimaryExtension>
</Mwi>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example:

To Update MWI

```
PUT https://<connection-server>/vmrest/users/<user-objectid>/mwis/<mwi-objectid>
Accept: application/json
Content-type:  application/json
Connection: keep-alive
Response Body:
{
  "DisplayName":"NEW_MWI",
  "UsePrimaryExtension":true"
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Delete a MWI

```
DELETE https://<connection-server>/vmrest/users/<user-objectid>/mwis/<mwi-objectid>
```

The following is the response from the above *DELETE* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

```
DELETE https://<connection-server>/vmrest/users/<user-objectid>/mwis/<mwi-objectid>
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *DELETE* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Explanation of
                           	 Data Fields

Possible values:

- true means that
                                                      						  it is active and the MWI will be turned on/off by the notifier.

- false

Default value: false (except the default MWI)

Possible values:

- false: MWI is
                                                      						  off

- true: MWI is on

Default value: false

- true: Use
                                                      						  Inherit Extension

- false: Do not
                                                      						  use Inherit Extension

Default value: false (but its true for default MWI)

Possible values:

- false: Do not
                                                      						  set MWI for text message.

- true: Set MWI
                                                      						  for text message.

Default value: false

Possible values: false: Do not set MWI for voice message.
                                                						true: Set MWI for voice message. Default Value: true

Possible values:

- false: Do not
                                                      						  set MWI for fax message.

- true: Set MWI
                                                      						  for fax message.

Default value: false

| GET https://<connection-server>/vmrest/users/<user-objectid>/mwis |
|---|

| <Mwis total="1">
  <Mwi>
   <URI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/mwis/2c07a9ca-c041-4dfa-b0d1-7f633883a1b7</URI>   
   <SubscriberObjectId>4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1</SubscriberObjectId>
   <UserURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1</UserURI>
   <ObjectId>2c07a9ca-c041-4dfa-b0d1-7f633883a1b7</ObjectId>
   <DisplayName>MWI-1</DisplayName>
   <MwiExtension>99999</MwiExtension>
   <MwiOn>false</MwiOn>
   <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150</MediaSwitchObjectId>
   <PhoneSystemURI>/vmrest/phonesystems/ec1e2636-fc14-44fc-8cda-d6c1a3d61150</PhoneSystemURI>
   <IncludeTextMessages>false</IncludeTextMessages>
   <IncludeVoiceMessages>true</IncludeVoiceMessages>
   <IncludeFaxMessages>false</IncludeFaxMessages>
   <Active>true</Active>
   <UsePrimaryExtension>true</UsePrimaryExtension>
   <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
   </Mwi>
</Mwis> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/users/<user-objectid>/mwis/<mwi-objectid> |
|---|

| <Mwi>
  <URI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/mwis/1a231793-7168-44aa-8657-aa40eda67481</URI>
  <SubscriberObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</SubscriberObjectId>
  <UserURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8</UserURI>
  <ObjectId>1a231793-7168-44aa-8657-aa40eda67481</ObjectId>
  <DisplayName>MWI</DisplayName>
  <MwiExtension>99934</MwiExtension>
  <MwiOn>false</MwiOn>
  <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150</MediaSwitchObjectId>
  <PhoneSystemURI>/vmrest/phonesystems/ec1e2636-fc14-44fc-8cda-d6c1a3d61150</PhoneSystemURI>
  <IncludeTextMessages>false</IncludeTextMessages>
  <IncludeVoiceMessages>true</IncludeVoiceMessages>
  <IncludeFaxMessages>false</IncludeFaxMessages>
  <Active>true</Active>
  <UsePrimaryExtension>true</UsePrimaryExtension>
  <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
</Mwi> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/users/<user-objectid>/mwis/<mwi-objectid>
Accept: application/json
Connection: keep-alive
{
  "URI":"/vmrest/users/53c84cf9-c8fe-4dd5-a295-b648b72b5a2c/mwis/810ce62e-eeec-4f47-85bd-68c69a7bca66"
  "SubscriberObjectId":"53c84cf9-c8fe-4dd5-a295-b648b72b5a2c"
  "UserURI":"/vmrest/users/53c84cf9-c8fe-4dd5-a295-b648b72b5a2c"
  "ObjectId":"810ce62e-eeec-4f47-85bd-68c69a7bca66"
  "DisplayName":"MWI-1"
  "MwiExtension":"99999"
  "MwiOn":"false"
  "MediaSwitchObjectId":"e912b134-1bd0-45f9-baae-9f1e096ae3b9"
  "PhoneSystemURI":"/vmrest/phonesystems/e912b134-1bd0-45f9-baae-9f1e096ae3b9"
  "IncludeTextMessages":"false"
  "IncludeVoiceMessages":"true"
  "IncludeFaxMessages":"false"
  "Active":"true"
  "UsePrimaryExtension":"true"
  "MediaSwitchDisplayName":"PhoneSystem"
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/phonesystems |
|---|

| POST https://<connection-server>/vmrest/users/<user-objectid>/mwis |
|---|

| <Mwi>
  <DisplayName>MWI-1</DisplayName>
  <MwiExtension>9997</MwiExtension>
  <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150</MediaSwitchObjectId>
</Mwi> |
|---|

| Response Code: 201
/vmrest/users/f82b301d-1ec8-44c6-a3ee-0012269439bf/mwis/a9159ac7-3857-480c-917d-0c599a32fc03 |
|---|

| POST https://<connection-server>/vmrest/users/<user-objectid>/mwis
Accept: application/json
Content-type:  application/json
Connection: keep-alive
Request Body:-
{
  "DisplayName":"MWI-1",
  "MwiExtension":9997",
  "MediaSwitchObjectId":"ec1e2636-fc14-44fc-8cda-d6c1a3d61150"
} |
|---|

| Response Code: 201
/vmrest/users/f82b301d-1ec8-44c6-a3ee-0012269439bf/mwis/a9159ac7-3857-480c-917d-0c599a32fc03 |
|---|

| PUT https://<connection-server>/vmrest/users/<user-objectid>/mwis/<mwi-objectid> |
|---|

| <Mwi>
  <Active>true</Active>
  <DisplayName>MWI</DisplayName>
  <MwiExtension>9997</MwiExtension>
  <MwiOn>false</MwiOn>
  <UsePrimaryExtension>true</UsePrimaryExtension>
</Mwi> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/users/<user-objectid>/mwis/<mwi-objectid>
Accept: application/json
Content-type:  application/json
Connection: keep-alive
Response Body:
{
  "DisplayName":"NEW_MWI",
  "UsePrimaryExtension":true"
} |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/users/<user-objectid>/mwis/<mwi-objectid> |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/users/<user-objectid>/mwis/<mwi-objectid>
Accept: application/json
Connection: keep-alive |
|---|

| Response Code: 204 |
|---|

| Field Name | Data Type | Operations | Description |
|---|---|---|---|
| Active | Boolean | Read/Write | Flag indicate whether MWI is enabled or
                                             					 not. Possible values: true means that
                                                      						  it is active and the MWI will be turned on/off by the notifier. false Default value: false (except the default MWI) |
| Display Name | String(64) | Read/Write | The unique text name of this notification
                                             					 MWI to be used when displaying entries in the administrative console, e.g.
                                             					 Cisco Unity Connection Administration. For example, "Office Phone" or " Lab
                                             					 Phone". |
| MwiExtension | String | Read/Write | The phone number (extension) of the MWI to
                                             					 activate.NULL means use the subscriber's extension. |
| MediaSwitchObjectId | String(36) | Read/Write | The unique identifier of the MediaSwitch
                                             					 object to use for activating/deactivating the MWI. |
| MwiOn | Boolean | Read/Write | A flag indicating whether the MWI is on or
                                             					 off. This is the state of the MWI from the perspective of Cisco Unity
                                             					 Connection. Possible values: false: MWI is
                                                      						  off true: MWI is on Default value: false |
| UsePrimaryExtension | Boolean | Read/Write | A flag indicating that the primary
                                             					 extension of the subscriber should be used. true: Use
                                                      						  Inherit Extension false: Do not
                                                      						  use Inherit Extension Default value: false (but its true for default MWI) |
| IncludeTextMessages | Boolean | Read/Write | A flag indicating whether the MWI should be
                                             					 set for a text message. Possible values: false: Do not
                                                      						  set MWI for text message. true: Set MWI
                                                      						  for text message. Default value: false |
| IncludeVoiceMessages | Boolean | Read/Write | A flag indicating whether the MWI should be
                                             					 set for a voice message. Possible values: false: Do not set MWI for voice message.
                                                						true: Set MWI for voice message. Default Value: true |
| IncludeFaxMessages | Boolean | Read/Write | A flag indicating whether the MWI should be
                                             					 set for a FAX message. Possible values: false: Do not
                                                      						  set MWI for fax message. true: Set MWI
                                                      						  for fax message. Default value: false |
| MediaSwitchDisplayName | String | Read/Write | Name of phone system associated with the
                                             					 user. |
| ObjectId | String(36) | Read Only | A globally unique, system-generated
                                             					 identifier for a MWI object. |