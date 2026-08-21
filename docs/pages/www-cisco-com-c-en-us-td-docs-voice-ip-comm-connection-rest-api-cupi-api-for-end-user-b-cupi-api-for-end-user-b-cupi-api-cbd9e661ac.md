---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-for-end-user-b-cupi-api-for-end-user-b-cupi-api-cbd9e661ac
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API_for_End_User/b_CUPI_API_for_End_User/b_CUPI_API_for_End_User_chapter_011.html
retrieved_at: 2026-08-21T08:04:30.005982+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

Updated: December 21, 2018

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Alternate Devices

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Alternate Devices

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Alternate Devices

## About Alternate Devices

The level of access a user has to his or her Alternate Devices (or Alternate Extensions) is determined by the user's class
                           of service. The four levels of access are:

No access

Read access to administrator-defined alternate devices only

Read/Write access to user-defined alternate devices only

Full access (read access to administrator-defined alternate devices and read/write access to user-defined alternate devices)

## Listing and Viewing

To retrieve a list of one's alternate devices, use the GET method with URI /vmrest/user/alternatedevices. Note that only alternate
                              devices visible to the user (determined by the user's access level defined in his or her Class of Service) are returned. In
                              the example below, the user has full access to his or her alternate devices, and the GET request yields a response that indicates
                              the user has three alternate devices, two of which are administrator-defined and one user-defined:

```
GET http://<connection-server>/vmrest/user/alternatedevices
```

The following is the response from the GET request above:

```
200
OK
<?xml version="1.0" encoding="UTF-8"?>
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

To retrieve a specific Alternate Device by its object ID:

```
GET http://<connection-server>/vmrest/user/alternatedevices/2d7e426d-4e43-4d5e-8c3e-eb498856dcfc
```

The following is the response from the GET request above:

```
200
OK
<?xml version="1.0" encoding="UTF-8"?>
<AlternateDevice>
  <DisplayName>User-Defined Home Phone</DisplayName>
  <DtmfAccessId>5551234</DtmfAccessId>
  <ObjectId>2d7e426d-4e43-4d5e-8c3e-eb498856dcfc</ObjectId>
  <UserDefined>true</UserDefined>
</AlternateDevice>
```

## Searching

To retrieve only the user-defined alternate devices or only the administrator-defined ones, append the query parameter "userDefined=true"
                              or "userDefined=false" respectively. For example, the following GET returns only the administrator-defined devices (assuming
                              the user has access to administrator-defined devices):

```
GET http://<connection-server>/vmrest/user/alternatedevices?userDefined=false
```

The following is the response from the GET request above:

```
200
OK
<?xml version="1.0" encoding="UTF-8"?>
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

## Creating

To create a new Alternate Device, use the POST method. The only required field for creating an alternate device is the DtmfAccessId.
                              In addition to the DtmfAccessId, you can also specify the device's Display Name. For example, assuming a user's Class of Service
                              allows access to user-defined Alternate Devices, the user can create a new one as follows:

```
POST http://<connection-server>/vmrest/user/alternatedevices

<AlternateDevice>
  <DisplayName>New Device</DisplayName>
  <DtmfAccessId>1001</DtmfAccessId>
</AlternateDevice>
```

The following is the response from the POST request above:

```
201
Created
/vmrest/user/alternatedevices/f4fd32c2-e6b7-48ff-8836-4ac2c100f9fc
```

## Updating and Deleting

Users are not allowed to update or delete administrator-defined alternate devices. They can, however, update or delete user-defined
                              ones, assuming their Class of Service allows them access to user-defined alternate devices.

For example, to change the DtmfAccessId of the user-defined alternate device in the Creating example above, use the PUT method
                              as follows:

```
PUT http://<connection-server>/vmrest/user/alternatedevices/f4fd32c2-e6b7-48ff-8836-4ac2c100f9fc

<AlternateDevice>
  <DtmfAccessId>1002</DtmfAccessId>
</AlternateDevice>
```

Similarly, to delete this user-defined alternate device, use the DELETE method as follows:

```
DELETE http://<connection-server>/vmrest/user/alternatedevices/f4fd32c2-e6b7-48ff-8836-4ac2c100f9fc
```

| GET http://<connection-server>/vmrest/user/alternatedevices |
|---|

| 200
OK
<?xml version="1.0" encoding="UTF-8"?>
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
</AlternateDevices> |
|---|

| GET http://<connection-server>/vmrest/user/alternatedevices/2d7e426d-4e43-4d5e-8c3e-eb498856dcfc |
|---|

| 200
OK
<?xml version="1.0" encoding="UTF-8"?>
<AlternateDevice>
  <DisplayName>User-Defined Home Phone</DisplayName>
  <DtmfAccessId>5551234</DtmfAccessId>
  <ObjectId>2d7e426d-4e43-4d5e-8c3e-eb498856dcfc</ObjectId>
  <UserDefined>true</UserDefined>
</AlternateDevice> |
|---|

| GET http://<connection-server>/vmrest/user/alternatedevices?userDefined=false |
|---|

| 200
OK
<?xml version="1.0" encoding="UTF-8"?>
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
</AlternateDevices> |
|---|

| POST http://<connection-server>/vmrest/user/alternatedevices

<AlternateDevice>
  <DisplayName>New Device</DisplayName>
  <DtmfAccessId>1001</DtmfAccessId>
</AlternateDevice> |
|---|

| 201
Created
/vmrest/user/alternatedevices/f4fd32c2-e6b7-48ff-8836-4ac2c100f9fc |
|---|

| PUT http://<connection-server>/vmrest/user/alternatedevices/f4fd32c2-e6b7-48ff-8836-4ac2c100f9fc

<AlternateDevice>
  <DtmfAccessId>1002</DtmfAccessId>
</AlternateDevice> |
|---|

| DELETE http://<connection-server>/vmrest/user/alternatedevices/f4fd32c2-e6b7-48ff-8836-4ac2c100f9fc |
|---|