---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-api-user-private-list-api-htm-f864ac7478
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_cupi-api-user-private-list-api.html
retrieved_at: 2026-08-17T03:48:29.966460+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Private List API

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Private List API

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- User Private List API

Links to Other API pages: Cisco_Unity_Connection_APIs

## Private List API

### Listing All the
                           	 Private Lists

```
GET https://<connection-server>/vmrest/users/<user-objectid>/privatelists
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
<PrivateLists total="1">
  <PrivateList>
  <URI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/privatelists/8465e5d7-f0d2-4d32-81b1-634a2315db9c</URI>
  <ObjectId>8465e5d7-f0d2-4d32-81b1-634a2315db9c</ObjectId>
  <DisplayName>Test1</DisplayName>
  <UserObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</UserObjectId>
  <UserURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8</UserURI>
  <DtmfName>83781</DtmfName>
  <Alias>Texoma_8465e5d7-f0d2-4d32-81b1-634a2315db9c</Alias>
  <NumericId>1</NumericId>
  <IsAddressable>true</IsAddressable>
  <PrivateListMembersURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/privatelists/8465e5d7-f0d2-4d32-81b1-634a2315db9c/privatelistmembers</PrivateListMembersURI>
  <AlternateNamesURI>/vmrest/alternatenames?query=(PersonalGroupObjectId%20is%208465e5d7-f0d2-4d32-81b1-634a2315db9c)        
  </AlternateNamesURI>
  </PrivateList>
</PrivateLists>
```

```
Response Code: 200
```

### Listing a
                           	 Particular Private List

```
GET https://<connection-server>/vmrest/users/<user-objectid>/privatelists/<objectid>
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
<PrivateList>
  <URI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/privatelists/8465e5d7-f0d2-4d32-81b1-634a2315db9c</URI>
  <ObjectId>8465e5d7-f0d2-4d32-81b1-634a2315db9c</ObjectId>
  <DisplayName>Test1</DisplayName>
  <UserObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</UserObjectId>
  <UserURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8</UserURI>
  <DtmfName>83781</DtmfName>
  <Alias>Texoma_8465e5d7-f0d2-4d32-81b1-634a2315db9c</Alias>
  <NumericId>1</NumericId>
  <IsAddressable>true</IsAddressable>
  <PrivateListMembersURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/privatelists/8465e5d7-f0d2-4d32-81b1-  634a2315db9c/privatelistmembers</PrivateListMembersURI>
  <AlternateNamesURI>/vmrest/alternatenames?query=(PersonalGroupObjectId%20is%208465e5d7-f0d2-4d32-81b1-634a2315db9c)          
  </AlternateNamesURI>
</PrivateList>
```

```
Response Code: 200
```

JSON Example

```
GET https://<connection-server>vmrest/users/<user-objectid>/privatelists/<objectid>
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
{
  “URI”: “/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/privatelists/8465e5d7-f0d2-4d32-81b1-634a2315db9c”
  “ObjectId”: “8465e5d7-f0d2-4d32-81b1-634a2315db9c”
  “DisplayName”: “Test1”
  “UserObjectId”: “9375d893-c8eb-437b-90bf-7de4b1d0c3e8”
  “UserURI”: “/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8”
  “DtmfName”: “83781”
  “Alias”: “Texoma_8465e5d7-f0d2-4d32-81b1-634a2315db9c”
  “NumericId”: “1”
  “IsAddressable”: “true”
  “PrivateListMembersURI”: “/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/privatelists/8465e5d7-f0d2-4d32-81b1-  634a2315db9c/privatelistmembers”
  “AlternateNamesURI”: “/vmrest/alternatenames?query=(PersonalGroupObjectId%20is%208465e5d7-f0d2-4d32-81b1-634a2315db9c)”
}
```

```
Response Code: 200
```

### Create a Private
                           	 list

The mandatory field for creation
                                 		  is DisplayName.

```
POST https://<connection-server>/vmrest/users/<user-objectid>/privatelists
```

```
<PrivateList>
  <DisplayName>Test1</DisplayName>
</PrivateList>
```

The following is the response from the above *POST* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 201
/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/privatelists/2375d893-c8eb-437b-90bf-7de4b1d0c3e5
```

JSON Example

```
POST https://<connection-server>vmrest/users/<user-objectid>/privatelists/<objectid>
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

```
{
  "DisplayName":"Test1"
}
```

The following is the response from the above *POST* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 201
/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/privatelists/2375d893-c8eb-437b-90bf-7de4b1d0c3e5
```

### Update Private
                           	 List

```
PUT https://<connection-server>vmrest/users/<user-objectid>/privatelists/<objectid>
```

```
<PrivateList>
  <DisplayName>Test11</DisplayName>
</PrivateList>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

```
PUT https://<connection-server>vmrest/users/<user-objectid>/privatelists/<objectid>
Accept: application/json
Content-type:  application/json
Connection: keep-alive
```

```
{
  "DisplayName":"Test11"
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Delete Private
                           	 List

```
DELETE https://<connection-server>/vmrest/users/<user-objectid>/privatelists/<objectid>
```

The following is the response from the above *DELETE* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

```
DELETE https://<connection-server>vmrest/users/<user-objectid>/privatelists/<objectid>
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

Possible Values:

- false: The
                                                      						  entity is not addressable

- true: The entity
                                                      						  is addressable.

Default value: true

| GET https://<connection-server>/vmrest/users/<user-objectid>/privatelists |
|---|

| <PrivateLists total="1">
  <PrivateList>
  <URI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/privatelists/8465e5d7-f0d2-4d32-81b1-634a2315db9c</URI>
  <ObjectId>8465e5d7-f0d2-4d32-81b1-634a2315db9c</ObjectId>
  <DisplayName>Test1</DisplayName>
  <UserObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</UserObjectId>
  <UserURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8</UserURI>
  <DtmfName>83781</DtmfName>
  <Alias>Texoma_8465e5d7-f0d2-4d32-81b1-634a2315db9c</Alias>
  <NumericId>1</NumericId>
  <IsAddressable>true</IsAddressable>
  <PrivateListMembersURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/privatelists/8465e5d7-f0d2-4d32-81b1-634a2315db9c/privatelistmembers</PrivateListMembersURI>
  <AlternateNamesURI>/vmrest/alternatenames?query=(PersonalGroupObjectId%20is%208465e5d7-f0d2-4d32-81b1-634a2315db9c)        
  </AlternateNamesURI>
  </PrivateList>
</PrivateLists> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/users/<user-objectid>/privatelists/<objectid> |
|---|

| <PrivateList>
  <URI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/privatelists/8465e5d7-f0d2-4d32-81b1-634a2315db9c</URI>
  <ObjectId>8465e5d7-f0d2-4d32-81b1-634a2315db9c</ObjectId>
  <DisplayName>Test1</DisplayName>
  <UserObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</UserObjectId>
  <UserURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8</UserURI>
  <DtmfName>83781</DtmfName>
  <Alias>Texoma_8465e5d7-f0d2-4d32-81b1-634a2315db9c</Alias>
  <NumericId>1</NumericId>
  <IsAddressable>true</IsAddressable>
  <PrivateListMembersURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/privatelists/8465e5d7-f0d2-4d32-81b1-  634a2315db9c/privatelistmembers</PrivateListMembersURI>
  <AlternateNamesURI>/vmrest/alternatenames?query=(PersonalGroupObjectId%20is%208465e5d7-f0d2-4d32-81b1-634a2315db9c)          
  </AlternateNamesURI>
</PrivateList> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>vmrest/users/<user-objectid>/privatelists/<objectid>
Accept: application/json
Connection: keep-alive |
|---|

| {
  “URI”: “/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/privatelists/8465e5d7-f0d2-4d32-81b1-634a2315db9c”
  “ObjectId”: “8465e5d7-f0d2-4d32-81b1-634a2315db9c”
  “DisplayName”: “Test1”
  “UserObjectId”: “9375d893-c8eb-437b-90bf-7de4b1d0c3e8”
  “UserURI”: “/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8”
  “DtmfName”: “83781”
  “Alias”: “Texoma_8465e5d7-f0d2-4d32-81b1-634a2315db9c”
  “NumericId”: “1”
  “IsAddressable”: “true”
  “PrivateListMembersURI”: “/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/privatelists/8465e5d7-f0d2-4d32-81b1-  634a2315db9c/privatelistmembers”
  “AlternateNamesURI”: “/vmrest/alternatenames?query=(PersonalGroupObjectId%20is%208465e5d7-f0d2-4d32-81b1-634a2315db9c)”
} |
|---|

| Response Code: 200 |
|---|

| POST https://<connection-server>/vmrest/users/<user-objectid>/privatelists |
|---|

| <PrivateList>
  <DisplayName>Test1</DisplayName>
</PrivateList> |
|---|

| Response Code: 201
/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/privatelists/2375d893-c8eb-437b-90bf-7de4b1d0c3e5 |
|---|

| POST https://<connection-server>vmrest/users/<user-objectid>/privatelists/<objectid>
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| {
  "DisplayName":"Test1"
} |
|---|

| Response Code: 201
/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/privatelists/2375d893-c8eb-437b-90bf-7de4b1d0c3e5 |
|---|

| PUT https://<connection-server>vmrest/users/<user-objectid>/privatelists/<objectid> |
|---|

| <PrivateList>
  <DisplayName>Test11</DisplayName>
</PrivateList> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>vmrest/users/<user-objectid>/privatelists/<objectid>
Accept: application/json
Content-type:  application/json
Connection: keep-alive |
|---|

| {
  "DisplayName":"Test11"
} |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/users/<user-objectid>/privatelists/<objectid> |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>vmrest/users/<user-objectid>/privatelists/<objectid>
Accept: application/json
Connection: keep-alive |
|---|

| Response Code: 204 |
|---|

| Field Name | Data Type | Operation | Description |
|---|---|---|---|
| DisplayName | String | Read/Write | The preferred text name of the list to be
                                             					 used when displaying entries such as in the administrative console, e.g. Cisco
                                             					 Unity Connection Administration. |
| UserObjectId | String(36) | Read Only | The unique identifier of the User object to
                                             					 which this list belongs. |
| DtmfName | String | Read Only | The digits corresponding to the numeric
                                             					 keypad mapping on a standard touchtone phone representing the group name. These
                                             					 digits would need to be dialed to address a message to this list via the phone. |
| Alias | String | Read Only | The unique text name for either a list |
| NumericId | String | Read Only | If being used as a personal voicemail list
                                             					 (i.e., "private" voicemail list), the numeric identifier for the personal
                                             					 group,(Value 0-4) |
| IsAddressable | Boolean | Read Only | A flag indicating whether the entity to
                                             					 which the alias belongs is addressable. Possible Values: false: The
                                                      						  entity is not addressable true: The entity
                                                      						  is addressable. Default value: true |
| ObjectId | String(36) | Read Only | Unique identifier of private List |