---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-for-end-user-b-cupi-api-for-end-user-b-cupi-api-2d597ddbc0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API_for_End_User/b_CUPI_API_for_End_User/b_CUPI_API_for_End_User_chapter_01110.html
retrieved_at: 2026-08-21T08:05:16.301200+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

Updated: January 24, 2019

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- Alternate Devices

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- Alternate Devices

# Cisco Unity Connection Provisioning Interface (CUPI) API -- Alternate Devices

## Alternate Devices API

The level of access a user has to his or her Alternate Devices (or Alternate Extensions) is determined by the user's class
                           of service. The four levels of access are:

No access

Read access to administrator-defined alternate devices only

Read/Write access to user-defined alternate devices only

Full access (read access to administrator-defined alternate devices and read/write access to user-defined alternate devices)

## Listing the Alternate Devices

Only alternate devices visible to the user (determined by the user's access level defined in his or her Class of Service)
                              are returned. In the example below, the user has full access to his or her alternate devices, and the GET request yields a
                              response that indicates the user has three alternate devices, two of which are administrator-defined and one user-defined:

```
GET http://<connection-server>/vmrest/user/alternatedevices
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                              by you:

```
<AlternateDevices total="3">
  <AlternateDevice>
   <URI>/vmrest/user/alternatedevices/e14bc9ef-57af-401c-a826-3e7603a36106</URI>
   <DisplayName>Alt Ext</DisplayName>
   <DtmfAccessId>3232</DtmfAccessId>
   <ObjectId>e14bc9ef-57af-401c-a826-3e7603a36106</ObjectId>
   <UserDefined>false</UserDefined>
  </AlternateDevice>
  <AlternateDevice>
   <URI>/vmrest/user/alternatedevices/4960bf32-6c4e-4a6a-97e1-dfe2858f89a6</URI>
   <DisplayName>Work Fax</DisplayName>
   <DtmfAccessId>0329</DtmfAccessId>
   <ObjectId>4960bf32-6c4e-4a6a-97e1-dfe2858f89a6</ObjectId>
   <UserDefined>false</UserDefined>
  </AlternateDevice>
  <AlternateDevice>
   <URI>/vmrest/user/alternatedevices/2d7e426d-4e43-4d5e-8c3e-eb498856dcfc</URI>
   <DisplayName>User-Defined Home Phone</DisplayName>
   <DtmfAccessId>5551234</DtmfAccessId>
   <ObjectId>2d7e426d-4e43-4d5e-8c3e-eb498856dcfc</ObjectId>
   <UserDefined>true</UserDefined>
  </AlternateDevice>
</AlternateDevices>
```

```
Response Code: 200
```

JSON Example

```
GET http://<connection-server>/vmrest/user/alternatedevices
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                              by you:

```
{
"@total": "3",
"AlternateDevice": 
[
  {
  "URI": "/vmrest/user/alternatedevices/e14bc9ef-57af-401c-a826-3e7603a36106",
  "DisplayName": "Alt Ext",
  "DtmfAccessId": "3232",
  "ObjectId": "e14bc9ef-57af-401c-a826-3e7603a36106",
  "UserDefined": "false"
  },
  {
  "URI": "/vmrest/user/alternatedevices/4960bf32-6c4e-4a6a-97e1-dfe2858f89a6",
  "DisplayName": "Work Fax",
  "DtmfAccessId": "0329",
  "ObjectId": "4960bf32-6c4e-4a6a-97e1-dfe2858f89a6",
  "UserDefined": "false"
  },
  {
  "URI": "/vmrest/user/alternatedevices/2d7e426d-4e43-4d5e-8c3e-eb498856dcfc",
  "DisplayName": "User-Defined Home Phone",
  "DtmfAccessId": "5551234",
  "ObjectId": "2d7e426d-4e43-4d5e-8c3e-eb498856dcfc",
  "UserDefined": "true"
  }
]
}
```

```
Response Code: 200
```

## Listing Details of a Specific Alternate Device

To retrieve a specific alternate device by its object ID:

```
GET http://<connection-server>/vmrest/user/alternatedevices/<alternate-device-objectid>
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                              by you:

```
<AlternateDevice>
  <DisplayName>User-Defined Home Phone</DisplayName>
  <DtmfAccessId>5551234</DtmfAccessId>
  <ObjectId>2d7e426d-4e43-4d5e-8c3e-eb498856dcfc</ObjectId>
  <UserDefined>true</UserDefined>
</AlternateDevice>
```

```
Response Code: 200
```

To retrieve only the user-defined alternate devices or only the administrator-defined ones, append the query parameter "userDefined=true"
                              or "userDefined=false" respectively. For example, the following GET returns only the administrator-defined devices (assuming
                              the user has access to administrator-defined devices):

```
GET https://<connection-server>/vmrest/user/alternatedevices?userDefined=false
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                              by you:

```
<AlternateDevices total="2"> 
  <AlternateDevice>
   <URI>/vmrest/user/alternatedevices/e14bc9ef-57af-401c-a826-3e7603a36106</URI>
   <DisplayName>Alt Ext</DisplayName>
   <DtmfAccessId>3232</DtmfAccessId>
   <ObjectId>e14bc9ef-57af-401c-a826-3e7603a36106</ObjectId>
   <UserDefined>false</UserDefined>
  </AlternateDevice>
  <AlternateDevice>
   <URI>/vmrest/user/alternatedevices/4960bf32-6c4e-4a6a-97e1-dfe2858f89a6</URI>
   <DisplayName>Work Fax</DisplayName>
   <DtmfAccessId>0329</DtmfAccessId>
   <ObjectId>4960bf32-6c4e-4a6a-97e1-dfe2858f89a6</ObjectId>
   <UserDefined>false</UserDefined>
  </AlternateDevice>
</AlternateDevices>
```

```
Response Code: 200
```

## Create an Alternate Device

To create a new Alternate Device, use the POST method. The only required field for creating an alternate device is the DtmfAccessId.
                              In addition to the DtmfAccessId, you can also specify the device's Display Name. For example, assuming a user's Class of Service
                              allows access to user-defined Alternate Devices, the user can create a new one as follows:

```
POST https://<connection-server>/vmrest/user/alternatedevices
```

```
<AlternateDevice> 
  <DisplayName>New Device</DisplayName>
  <DtmfAccessId>1001</DtmfAccessId>
</AlternateDevice>
```

The following is the response from the above *POST* request and the actual response will depend upon the information given
                              by you:

```
Response Code: 201
/vmrest/user/alternatedevices/f4fd32c2-e6b7-48ff-8836-4ac2c100f9fc
```

JSON Example

```
POST http://<connection-server>/vmrest/user/alternatedevices 
Accept: application/json 
Content-type: application/json 
Connection: keep-alive
```

```
{
  "DisplayName": "New Device",
  "DtmfAccessId": "1001"
}
```

The following is the response from the above *POST* request and the actual response will depend upon the information given
                              by you:

```
Response Code: 201
/vmrest/user/alternatedevices/f4fd32c2-e6b7-48ff-8836-4ac2c100f9fc
```

## Update an Alternate Device

Users are not allowed to update or delete administrator-defined alternate devices. They can, however, update or delete user-defined
                              ones, assuming their Class of Service allows them access to user-defined alternate devices. For example, to change the DtmfAccessId
                              of the user-defined alternate device in the creation example above, use the PUT method as follows:

```
PUT http://<connection-server>/vmrest/user/alternatedevices/<alternate-device-objectid>
```

```
<AlternateDevice> 
  <DisplayName>New Device</DisplayName>
  <DtmfAccessId>1002</DtmfAccessId>
</AlternateDevice>
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                              by you:

```
Response Code: 204
```

JSON Example

```
PUT http://<connection-server>/vmrest/user/alternatedevices/<alternate-device-objectid> 
Accept: application/json 
Content-type: application/json 
Connection: keep-alive
```

```
{
  
  "DtmfAccessId": "1002"
}
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                              by you:

```
Response Code: 204
```

## Delete an Alternate Device

This request can be used to delete an alternate device.

```
DELETE http://<connection-server>/vmrest/user/alternatedevices/<alternate-device-objectid>
```

The following is the response from the above *DELETE* request and the actual response will depend upon the information given
                              by you:

```
Response Code: 204
```

JSON Example

```
DELETE http://<connection-server>/vmrest/user/alternatedevices/<alternate-device-objectid> 
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *DELETE* request and the actual response will depend upon the information given
                              by you:

```
Response Code: 204
```

## Explanation of Data Fields

Parameter

Operation

Data Type

Comments

URI

Read Only

String

URI of the Alternate Device

ObjectId

Read Only

String(36)

Display Name of the Alternate Device

DisplayName

Read/Write

String(64)

Unique identifier of the Alternate Device.

DtmfAccessId

Read/Write

Integer

Extension number for the Alternate Device.

UserDefined

Read Only

Boolean

Flag to indicate whether its a user defined Alternate Device or is an administrator defined Alternate Device.

true: the alternate device is user defined

false: the alternate device is administrator defined

Default value is false.

| GET http://<connection-server>/vmrest/user/alternatedevices |
|---|

| <AlternateDevices total="3">
  <AlternateDevice>
   <URI>/vmrest/user/alternatedevices/e14bc9ef-57af-401c-a826-3e7603a36106</URI>
   <DisplayName>Alt Ext</DisplayName>
   <DtmfAccessId>3232</DtmfAccessId>
   <ObjectId>e14bc9ef-57af-401c-a826-3e7603a36106</ObjectId>
   <UserDefined>false</UserDefined>
  </AlternateDevice>
  <AlternateDevice>
   <URI>/vmrest/user/alternatedevices/4960bf32-6c4e-4a6a-97e1-dfe2858f89a6</URI>
   <DisplayName>Work Fax</DisplayName>
   <DtmfAccessId>0329</DtmfAccessId>
   <ObjectId>4960bf32-6c4e-4a6a-97e1-dfe2858f89a6</ObjectId>
   <UserDefined>false</UserDefined>
  </AlternateDevice>
  <AlternateDevice>
   <URI>/vmrest/user/alternatedevices/2d7e426d-4e43-4d5e-8c3e-eb498856dcfc</URI>
   <DisplayName>User-Defined Home Phone</DisplayName>
   <DtmfAccessId>5551234</DtmfAccessId>
   <ObjectId>2d7e426d-4e43-4d5e-8c3e-eb498856dcfc</ObjectId>
   <UserDefined>true</UserDefined>
  </AlternateDevice>
</AlternateDevices> |
|---|

| Response Code: 200 |
|---|

| GET http://<connection-server>/vmrest/user/alternatedevices
Accept: application/json
Connection: keep-alive |
|---|

| {
"@total": "3",
"AlternateDevice": 
[
  {
  "URI": "/vmrest/user/alternatedevices/e14bc9ef-57af-401c-a826-3e7603a36106",
  "DisplayName": "Alt Ext",
  "DtmfAccessId": "3232",
  "ObjectId": "e14bc9ef-57af-401c-a826-3e7603a36106",
  "UserDefined": "false"
  },
  {
  "URI": "/vmrest/user/alternatedevices/4960bf32-6c4e-4a6a-97e1-dfe2858f89a6",
  "DisplayName": "Work Fax",
  "DtmfAccessId": "0329",
  "ObjectId": "4960bf32-6c4e-4a6a-97e1-dfe2858f89a6",
  "UserDefined": "false"
  },
  {
  "URI": "/vmrest/user/alternatedevices/2d7e426d-4e43-4d5e-8c3e-eb498856dcfc",
  "DisplayName": "User-Defined Home Phone",
  "DtmfAccessId": "5551234",
  "ObjectId": "2d7e426d-4e43-4d5e-8c3e-eb498856dcfc",
  "UserDefined": "true"
  }
]
} |
|---|

| Response Code: 200 |
|---|

| GET http://<connection-server>/vmrest/user/alternatedevices/<alternate-device-objectid> |
|---|

| <AlternateDevice>
  <DisplayName>User-Defined Home Phone</DisplayName>
  <DtmfAccessId>5551234</DtmfAccessId>
  <ObjectId>2d7e426d-4e43-4d5e-8c3e-eb498856dcfc</ObjectId>
  <UserDefined>true</UserDefined>
</AlternateDevice> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/user/alternatedevices?userDefined=false |
|---|

| <AlternateDevices total="2"> 
  <AlternateDevice>
   <URI>/vmrest/user/alternatedevices/e14bc9ef-57af-401c-a826-3e7603a36106</URI>
   <DisplayName>Alt Ext</DisplayName>
   <DtmfAccessId>3232</DtmfAccessId>
   <ObjectId>e14bc9ef-57af-401c-a826-3e7603a36106</ObjectId>
   <UserDefined>false</UserDefined>
  </AlternateDevice>
  <AlternateDevice>
   <URI>/vmrest/user/alternatedevices/4960bf32-6c4e-4a6a-97e1-dfe2858f89a6</URI>
   <DisplayName>Work Fax</DisplayName>
   <DtmfAccessId>0329</DtmfAccessId>
   <ObjectId>4960bf32-6c4e-4a6a-97e1-dfe2858f89a6</ObjectId>
   <UserDefined>false</UserDefined>
  </AlternateDevice>
</AlternateDevices> |
|---|

| Response Code: 200 |
|---|

| POST https://<connection-server>/vmrest/user/alternatedevices |
|---|

| <AlternateDevice> 
  <DisplayName>New Device</DisplayName>
  <DtmfAccessId>1001</DtmfAccessId>
</AlternateDevice> |
|---|

| Response Code: 201
/vmrest/user/alternatedevices/f4fd32c2-e6b7-48ff-8836-4ac2c100f9fc |
|---|

| POST http://<connection-server>/vmrest/user/alternatedevices 
Accept: application/json 
Content-type: application/json 
Connection: keep-alive |
|---|

| {
  "DisplayName": "New Device",
  "DtmfAccessId": "1001"
} |
|---|

| Response Code: 201
/vmrest/user/alternatedevices/f4fd32c2-e6b7-48ff-8836-4ac2c100f9fc |
|---|

| PUT http://<connection-server>/vmrest/user/alternatedevices/<alternate-device-objectid> |
|---|

| <AlternateDevice> 
  <DisplayName>New Device</DisplayName>
  <DtmfAccessId>1002</DtmfAccessId>
</AlternateDevice> |
|---|

| Response Code: 204 |
|---|

| PUT http://<connection-server>/vmrest/user/alternatedevices/<alternate-device-objectid> 
Accept: application/json 
Content-type: application/json 
Connection: keep-alive |
|---|

| {
  
  "DtmfAccessId": "1002"
} |
|---|

| Response Code: 204 |
|---|

| DELETE http://<connection-server>/vmrest/user/alternatedevices/<alternate-device-objectid> |
|---|

| Response Code: 204 |
|---|

| DELETE http://<connection-server>/vmrest/user/alternatedevices/<alternate-device-objectid> 
Accept: application/json
Connection: keep-alive |
|---|

| Response Code: 204 |
|---|

| Parameter | Operation | Data Type | Comments |
|---|---|---|---|
| URI | Read Only | String | URI of the Alternate Device |
| ObjectId | Read Only | String(36) | Display Name of the Alternate Device |
| DisplayName | Read/Write | String(64) | Unique identifier of the Alternate Device. |
| DtmfAccessId | Read/Write | Integer | Extension number for the Alternate Device. |
| UserDefined | Read Only | Boolean | Flag to indicate whether its a user defined Alternate Device or is an administrator defined Alternate Device. true: the alternate device is user defined false: the alternate device is administrator defined Default value is false. |