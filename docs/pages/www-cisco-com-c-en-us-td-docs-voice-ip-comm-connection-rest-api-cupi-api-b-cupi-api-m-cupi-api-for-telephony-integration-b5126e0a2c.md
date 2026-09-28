---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-api-for-telephony-integration-b5126e0a2c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m-cupi-api-for-telephony-integration.html
retrieved_at: 2026-08-17T03:50:20.033912+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API for Telephony Integrations

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API for Telephony Integrations

# Cisco Unity Connection Provisioning Interface (CUPI) API for Telephony Integrations

## Cisco Unity Connection Provisioning Interface (CUPI) API -- Phone Systems

### About Phone Systems

This page contains information on how to use the API to create, list, modify, and delete Phone Systems. The phone system pages
                              in Cisco Unity Connection Administration identify the phone systems that Cisco Unity Connection integrates with. In Connection
                              Administration, a phone system has one or more port groups, which in turn have voice messaging ports. You can manage the phone
                              systems to meet the changing needs of your system.

### Listing Phone Systems

Example 1

The following is an example of the GET request that lists the Phone Systems:

```
https://<connection_server>/vmrest/phonesystems
```

The following is an example of the response from the above *GET* request and the actual response will depend upon the information
                                 given by you:

```
<PhoneSystems total="1">
 <PhoneSystem>
   <URI>/vmrest/phonesystems/aa6d3f45-ccdf-4fa2-8170-e5c94b51813a</URI>
   <ObjectId>aa6d3f45-ccdf-4fa2-8170-e5c94b51813a</ObjectId>
   <DisplayName>PhoneSystem</DisplayName>
   <MwiAlwaysUpdate>false</MwiAlwaysUpdate>
   <MwiPortMemory>false</MwiPortMemory>
   <CallLoopSupervisedTransferDetect>false</CallLoopSupervisedTransferDetect>
   <CallLoopForwardNotificationDetect>false</CallLoopForwardNotificationDetect>
   <CallLoopDTMF>A</CallLoopDTMF>
   <CallLoopGuardTimeMs>2500</CallLoopGuardTimeMs>
   <PortCount>0</PortCount>
   <EnablePhoneApplications>false</EnablePhoneApplications>
   <DefaultTRaPSwitch>true</DefaultTRaPSwitch>
   <MwiForceOff>false</MwiForceOff>
   <RestrictDialUnconditional>false</RestrictDialUnconditional>
   <RestrictDialScheduled>false</RestrictDialScheduled>
   <RestrictDialStartTime>0</RestrictDialStartTime>
   <RestrictDialEndTime>0</RestrictDialEndTime>
   <CallLoopExtensionDetect>true</CallLoopExtensionDetect>
   <AXLServerURI>/vmrest/phonesystems/aa6d3f45-ccdf-4fa2-8170-e5c94b51813a/axlservers</AXLServerURI>
   <PhoneSystemAssociationURI>/vmrest/phonesystems/aa6d3f45-ccdf-4fa2-8170-e5c94b51813a/phonesystemassociations</PhoneSystemAssociationURI>
 </PhoneSystem>
</PhoneSystems>
```

```
Response Code: 200
```

Example 2

The following is an example of the GET request that lists a particular phone system represented by <phonesystemId>:

```
https:/<connection_server>/vmrest/phonesystem/<objectId>
```

The following is an example of the response from the above *GET* request and the actual response will depend upon the information
                                 given by you:

```
<PhoneSystem>
 <URI>/vmrest/phonesystems/aa6d3f45-ccdf-4fa2-8170-e5c94b51813a</URI>
 <ObjectId>aa6d3f45-ccdf-4fa2-8170-e5c94b51813a</ObjectId>
 <DisplayName>PhoneSystem</DisplayName>
 <MwiAlwaysUpdate>false</MwiAlwaysUpdate>
 <MwiPortMemory>false</MwiPortMemory>
 <CallLoopSupervisedTransferDetect>false</CallLoopSupervisedTransferDetect>
 <CallLoopForwardNotificationDetect>false</CallLoopForwardNotificationDetect>
 <CallLoopDTMF>A</CallLoopDTMF>
 <CallLoopGuardTimeMs>2500</CallLoopGuardTimeMs>
 <PortCount>0</PortCount>
 <EnablePhoneApplications>false</EnablePhoneApplications>
 <DefaultTRaPSwitch>true</DefaultTRaPSwitch>
 <MwiForceOff>false</MwiForceOff>
 <RestrictDialUnconditional>false</RestrictDialUnconditional>
 <RestrictDialScheduled>false</RestrictDialScheduled>
 <RestrictDialStartTime>0</RestrictDialStartTime>
 <RestrictDialEndTime>0</RestrictDialEndTime>
 <CallLoopExtensionDetect>true</CallLoopExtensionDetect>
 <AXLServerURI>/vmrest/phonesystems/aa6d3f45-ccdf-4fa2-8170-e5c94b51813a/axlservers</AXLServerURI>
 <PhoneSystemAssociationURI>/vmrest/phonesystems/aa6d3f45-ccdf-4fa2-8170-e5c94b51813a/phonesystemassociations</PhoneSystemAssociationURI>
</PhoneSystem>
```

```
Response Code: 200
```

### Adding a New Phone System

The following is an example of the POST request that adds the Phone Systems:

```
https://<connection_server>/vmrest/phonesystems
```

The actual response will depend upon the information given by you.

```
<PhoneSystem>
 <DisplayName>PhoneSystem1</DisplayName>
</PhoneSystem>
```

```
Response Code: 201
```

To create a phone system, only the <DisplayName> parameter is mandatory.

### Modifying a Phone System

The following is an example of the PUT request that modifies the Phone System as represented by <phonesystemid>:

```
https:/<Connection_server>/vmrest/phonesystem/<objectId>
```

The following is an example of the response from the above *PUT* request and the actual response will depend upon the information
                                 given by you:.

```
<PhoneSystem>
 <MwiAlwaysUpdate>false</MwiAlwaysUpdate>
 <MwiPortMemory>false</MwiPortMemory>
 <CallLoopSupervisedTransferDetect>false</CallLoopSupervisedTransferDetect>
 <CallLoopForwardNotificationDetect>false</CallLoopForwardNotificationDetect>
 <CallLoopDTMF>A</CallLoopDTMF>
 <CallLoopGuardTimeMs>2500</CallLoopGuardTimeMs>
 <PortCount>2</PortCount>
</PhoneSystem>
```

```
Response Code: 204
```

You can also update the following in a phone system:

AXL Servers

Phone System Associations

#### AXL Servers

This page contains information on how to use the API to create, list, modify, and delete Phone Systems AXL Servers. AXL servers
                                 are supported only for Cisco Unified Communications Manager phone systems and are needed when Cisco Unity Connection must
                                 have access to the Cisco Unified CM database for importing Cisco Unified CM users and for changing certain phone settings
                                 for users of Connection personal call transfer rules.

With Unity Connection 11.5(1) and later, a new field, IsPinSyncEnabled is introduced in this API, which enables synchronization of phone PIN for Cisco Unity Connection with the PIN for Cisco Unified
                                 CM. By default, the value of this field is set to false. To enable PIN synchronization, set the value of the field to true.

Note: The IsPinSyncEnabled field is applicable only for primary AXL server.

##### Listing AXL Servers

The following is an example of the GET request that lists the AXL Servers:

```
https://<connection_server>/vmrest/phonesystems/<objectId>/axlservers
```

The following is an example of the response from the above *GET* request and the actual response will depend upon the information
                                       given by you:

```
<AXLServers total="2">
<AXLServer>
<URI>
/vmrest/phonesystems/a560c009-e802-466f-b42d-4c64e8ea8260/axlservers/59daf270-3e88-4d81-8dae-a3b0a5fbebb1
</URI>
<ObjectId>59daf270-3e88-4d81-8dae-a3b0a5fbebb1</ObjectId>
<MediaRemoteServiceEnum>103</MediaRemoteServiceEnum>
<HostOrIPAddress>0:0:0:0:0:1</HostOrIPAddress>
<Port>443</Port>
<TlsPort>443</TlsPort>
<Precedence>1</Precedence>
<MediaSwitchObjectId>a560c009-e802-466f-b42d-4c64e8ea8260</MediaSwitchObjectId>
<PhoneSystemURI>
/vmrest/phonesystems/a560c009-e802-466f-b42d-4c64e8ea8260
</PhoneSystemURI>
<SkinnyStateMachineEnum>10</SkinnyStateMachineEnum>
<IsPinSyncEnabled>false</IsPinSyncEnabled>
<CcmAXLUser>admin</CcmAXLUser>
<CcmAXLPassword/>
<CcmVersion>5</CcmVersion>
</AXLServer>
<AXLServer>
<URI>
/vmrest/phonesystems/a560c009-e802-466f-b42d-4c64e8ea8260/axlservers/59daf270-3e88-4d81-8dae-a3b0a5fbebb1
</URI>
<ObjectId>59daf270-3e88-4d81-8dae-a3b0a5fbebb1</ObjectId>
<MediaRemoteServiceEnum>103</MediaRemoteServiceEnum>
<HostOrIPAddress>0.0.0.1</HostOrIPAddress>
<Port>443</Port>
<TlsPort>443</TlsPort>
<Precedence>1</Precedence>
<MediaSwitchObjectId>a560c009-e802-466f-b42d-4c64e8ea8260</MediaSwitchObjectId>
<PhoneSystemURI>
/vmrest/phonesystems/a560c009-e802-466f-b42d-4c64e8ea8260
</PhoneSystemURI>
<SkinnyStateMachineEnum>10</SkinnyStateMachineEnum>
<IsPinSyncEnabled>false</IsPinSyncEnabled>
<CcmAXLUser>admin</CcmAXLUser>
<CcmAXLPassword/>
<CcmVersion>5</CcmVersion>
</AXLServer>
</AXLServers>
```

```
Response Code: 200
```

##### Adding New AXL Server

The following is an example of the POST request that adds the AXL servers in the Phone Systems:

```
https://<connection_server>/vmrest/phonesystems/<objectId>/axlservers
```

The actual response will depend upon the information given by you.

```
<AXLServer>
 <MediaSwitchObjectId>24f1171f-27b3-4ad3-a94c-66d1fb2e448b</MediaSwitchObjectId>
 <MediaRemoteServiceEnum>103</MediaRemoteServiceEnum>
 <HostOrIPAddress>10.105.255.1</HostOrIPAddress>
 <Port>2001</Port>
 <TlsPort>2000</TlsPort>
 <Precedence>1</Precedence>
 <CcmAXLUser>abcd</CcmAXLUser>
 <CcmAXLPassword/>
 <CcmVersion>5</CcmVersion>
 <IsPinSyncEnabled>false</IsPinSyncEnabled>
</AXLServer>
```

```
Response Code: 201
```

##### Modifying AXL Server

The following is an example of the PUT request that modifies the AXL Server as represented by <axlserverid>:

```
https://<connection_server>/vmrest/phonesystems/<objectId>/axlservers/<objectId>
```

The following is an example of the response from the above *PUT* request and the actual response will depend upon the information
                                       given by you:.

```
<AXLServer>
 <MediaSwitchObjectId>24f1171f-27b3-4ad3-a94c-66d1fb2e448b</MediaSwitchObjectId>
 <CcmAXLUser>CiscoCCM</CcmAXLUser>
 <CcmAXLPassword/> 
 <CcmVersion>5</CcmVersion>
</AXLServer>
```

```
Response Code: 204
```

##### Deleting AXL Server

The following is an example of the DELETE request that deletes an AXL Server as represented by < axlserverid >:

```
https:/<connection_server>/vmrest/phonesystems/<objectId>/axlservers/<objectId>
```

The input for the PUT request will be. The output for this request returns the successful response code.

```
Response Code: 204
```

#### Phone System Associations

This page contains information on how to use the API to list Phone Systems Associations. Phone Systems Associations are required
                                 to view a list of all of the Cisco Unity Connection users who are associated with your phone system. Listing Phone System
                                 Associations

##### Listing Phone Systems Associations

The following is an example of the GET request that lists the Phone Systems Associations:

```
https://<connection_server>/vmrest/phonesystems/<objectId>/phonesystemassociations
```

The following is an example of the response from the above *GET* request and the actual response will depend upon the information
                                    given by you:

```
<PhoneSystemAssociations total="2">
 <PhoneSystemAssociation>
   <URI>/vmrest/phonesystems/24f1171f-27b3-4ad3-a94c-66d1fb2e448b/phonesystemassociations/219ce340-a3a5-428c-8dc6-4776690b69ee</URI>
   <Alias>undeliverablemessagesmailbox</Alias>
   <DisplayName>Papa Recommended Web Application Authentication Rule</DisplayName>
   <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
   <MediaSwitchObjectId>24f1171f-27b3-4ad3-a94c-66d1fb2e448b</MediaSwitchObjectId>
   <PhoneSystemURI>/vmrest/phonesystems/24f1171f-27b3-4ad3-a94c-66d1fb2e448b</PhoneSystemURI>
   <numNotificationDevice>4</numNotificationDevice>
   <numNotificationMWI>1</numNotificationMWI>
   <numPrimaryCallHandler>1</numPrimaryCallHandler>
   <ObjectId>219ce340-a3a5-428c-8dc6-4776690b69ee</ObjectId>
 </PhoneSystemAssociation>
 <PhoneSystemAssociation>
   <URI>/vmrest/phonesystems/24f1171f-27b3-4ad3-a94c-66d1fb2e448b/phonesystemassociations/6b455973-13d1-4b10-871e-1d1d55f160d2</URI>
   <Alias>operator</Alias>
   <DisplayName>Operator</DisplayName>
   <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
   <MediaSwitchObjectId>24f1171f-27b3-4ad3-a94c-66d1fb2e448b</MediaSwitchObjectId>
   <PhoneSystemURI>/vmrest/phonesystems/24f1171f-27b3-4ad3-a94c-66d1fb2e448b</PhoneSystemURI>
   <numNotificationDevice>4</numNotificationDevice>
   <numNotificationMWI>1</numNotificationMWI>
   <numPrimaryCallHandler>1</numPrimaryCallHandler>
   <ObjectId>6b455973-13d1-4b10-871e-1d1d55f160d2</ObjectId>
 </PhoneSystemAssociation>	 
</PhoneSystemAssociations>>
```

```
Response Code: 200
```

### Deleting a Phone System

The following is an example of the DELETE request that deletes Phone System as represented by <phonesystemid>:

```
https://<server-ip>/vmrest/phonesystems/<objectId>
```

The input for the PUT request will be. The output for this request returns the successful response code.

```
Response Code: 204
```

## Cisco Unity Connection Provisioning Interface (CUPI) API -- Port Groups and Ports

### About Port Groups and Ports

This page contains information on how to use the API to:

List, view, and update port groups

List and view ports

Port groups cannot be created or deleted via the API, and only two fields (MwiOnCode & MwiOffCode) can be updated by using
                                          the PUT method.

### Listing and Viewing

The following is an example of a GET that lists all port groups:

```
GET http://<connection-server>/vmrest/portgroups
```

The following is the response from the above GET request:

```
200
OK
<?xml version="1.0" encoding="UTF-8"?>
<PortGroups total="1">
  <PortGroup>
    <URI>/vmrest/portgroups/035853ce-f4e6-4de2-bda2-84acf827a555</URI>
    <MediaPortGroupTemplateObjectId>90dd306f-b8af-46b6-8289-f13437cc1e5e</MediaPortGroupTemplateObjectId>
    <MediaSwitchObjectId>05186ad4-572c-48d1-aaa6-ac22280c8702</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/05186ad4-572c-48d1-aaa6-ac22280c8702</PhoneSystemURI>
    <TelephonyIntegrationMethodEnum>1</TelephonyIntegrationMethodEnum>
    <EnableMWI>true</EnableMWI>
    <DisplayName>PhoneSystem-1</DisplayName>
    <CcmDoAutoFailback>true</CcmDoAutoFailback>
    <MwiOnCode/>
    <MwiOffCode/>
    <MwiRetryCountOnSuccess>0</MwiRetryCountOnSuccess>
    <MwiRetryIntervalOnSuccessMs>5</MwiRetryIntervalOnSuccessMs>
    <ObjectId>035853ce-f4e6-4de2-bda2-84acf827a555</ObjectId>
    <SipTransportProtocolEnum>10</SipTransportProtocolEnum>
    <SipRegisterWithProxyServer>false</SipRegisterWithProxyServer>
    <SipDoAuthenticate>false</SipDoAuthenticate>
    <SkinnyDevicePrefix>test-VI</SkinnyDevicePrefix>
    <MwiMinRequestIntervalMs>0</MwiMinRequestIntervalMs>
    <MwiMaxConcurrentRequests>0</MwiMaxConcurrentRequests>
    <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
    <PortCount>2</PortCount>
    <SipDoSRTP>true</SipDoSRTP>
    <SipTLSModeEnum>11</SipTLSModeEnum>
    <ResetStatusEnum>0</ResetStatusEnum>
  </PortGroup>
</PortGroups>
```

Sorting can be done on columns that are indexed, such as display name. To retrieve a sorted list of all port groups, add the
                                 following query parameter: sort=(column [asc|desc])

For example, to retrieve a list of all port groups sorted by display name in descending order:

```
GET http://<connection-server>/vmrest/portgroups?sort=(DisplayName%20desc)
```

To retrieve a specific port group by its object ID:

```
GET http://<connection-server>/vmrest/portgroups/<objectid>
```

Similarly, to retrieve a list of all ports, use:

```
GET http://<connection-server>/vmrest/ports
```

The following is the response from the above GET request:

```
200
OK
<?xml version="1.0" encoding="UTF-8"?>
<Ports total="2">
  <Port>
    <URI>/vmrest/ports/2806ecdc-0a3d-43f3-a2c8-93d786fa506b</URI>
    <ObjectId>2806ecdc-0a3d-43f3-a2c8-93d786fa506b</ObjectId>
    <MediaPortGroupObjectId>035853ce-f4e6-4de2-bda2-84acf827a555</MediaPortGroupObjectId>
    <PortGroupURI>/vmrest/portgroups/035853ce-f4e6-4de2-bda2-84acf827a555</PortGroupURI>
    <TelephonyIntegrationMethodEnum>1</TelephonyIntegrationMethodEnum>
    <PortNumInGroup>1</PortNumInGroup>
    <SkinnySecurityModeEnum>0</SkinnySecurityModeEnum>
    <SkinnyDoMediaEncryption>false</SkinnyDoMediaEncryption>
    <VmsServerObjectId>a7ba129e-6420-4d44-b060-93b638ba866a</VmsServerObjectId>
    <HuntOrder>0</HuntOrder>
    <DisplayName>PhoneSystem-1-001</DisplayName>
    <SkinnyDeviceName>test-VI1</SkinnyDeviceName>
    <PimgPortNumber>1</PimgPortNumber>
    <CapAnswer>true</CapAnswer>
    <CapNotification>true</CapNotification>
    <CapMWI>true</CapMWI>
    <CapEnabled>true</CapEnabled>
    <CapDeliverAmis>false</CapDeliverAmis>
    <CapTrapConnection>true</CapTrapConnection>
    <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
    <MediaSwitchObjectId>05186ad4-572c-48d1-aaa6-ac22280c8702</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/05186ad4-572c-48d1-aaa6-ac22280c8702</PhoneSystemURI>
    <MediaPortGroupDisplayName>PhoneSystem-1</MediaPortGroupDisplayName>
    <MediaPortGroupEnableMWI>true</MediaPortGroupEnableMWI>
    <MediaPortGroupMwiReqPortSpecific>true</MediaPortGroupMwiReqPortSpecific>
    <SipSendPort>0</SipSendPort>
    <VmsServerName>cuc-install-55</VmsServerName>
  </Port>
  <Port>
    <URI>/vmrest/ports/f87ad180-7d06-48c9-b9bd-e6b5cd2311bc</URI>
    <ObjectId>f87ad180-7d06-48c9-b9bd-e6b5cd2311bc</ObjectId>
    <MediaPortGroupObjectId>035853ce-f4e6-4de2-bda2-84acf827a555</MediaPortGroupObjectId>
    <PortGroupURI>/vmrest/portgroups/035853ce-f4e6-4de2-bda2-84acf827a555</PortGroupURI>
    <TelephonyIntegrationMethodEnum>1</TelephonyIntegrationMethodEnum>
    <PortNumInGroup>2</PortNumInGroup>
    <SkinnySecurityModeEnum>0</SkinnySecurityModeEnum>
    <SkinnyDoMediaEncryption>false</SkinnyDoMediaEncryption>
    <VmsServerObjectId>a7ba129e-6420-4d44-b060-93b638ba866a</VmsServerObjectId>
    <HuntOrder>0</HuntOrder>
    <DisplayName>PhoneSystem-1-002</DisplayName>
    <SkinnyDeviceName>test-VI2</SkinnyDeviceName>
    <PimgPortNumber>2</PimgPortNumber>
    <CapAnswer>true</CapAnswer>
    <CapNotification>true</CapNotification>
    <CapMWI>true</CapMWI>
    <CapEnabled>true</CapEnabled>
    <CapDeliverAmis>false</CapDeliverAmis>
    <CapTrapConnection>true</CapTrapConnection>
    <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
    <MediaSwitchObjectId>05186ad4-572c-48d1-aaa6-ac22280c8702</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/05186ad4-572c-48d1-aaa6-ac22280c8702</PhoneSystemURI>
    <MediaPortGroupDisplayName>PhoneSystem-1</MediaPortGroupDisplayName>
    <MediaPortGroupEnableMWI>true</MediaPortGroupEnableMWI>
    <MediaPortGroupMwiReqPortSpecific>true</MediaPortGroupMwiReqPortSpecific>
    <SipSendPort>0</SipSendPort>
    <VmsServerName>cuc-install-55</VmsServerName>
  </Port>
</Ports>
```

Finally, to retrieve a specific port by its object ID, use:

```
GET http://<connection-server>/vmrest/ports/<objectid>
```

### Searching

To retrieve a list of port groups or ports that meet a specified search criteria, add the following query parameter to a GET:
                                 query=(column [is|startswith] value)

Note that the search column must either be an indexed column or contain boolean values.

For example, to find all port groups with a display name that starts with "PhoneSystem":

```
GET http://<connection-server>/vmrest/portgroups?query=(displayname%20startswith%20PhoneSystem)
```

The next example finds all port groups with a EnableMwi that is set to 1 (i.e., enabled):

```
GET http://<connection-server>/vmrest/portgroups?query=(EnableMWI%20is%201)
```

### Updating

Ports are read-only resources and cannot be updated. Port groups, however, contain two fields, MwiOnCode and MwiOffCode, that
                                 can be updated.

The following is an example of a PUT request that modifies these fields of an existing port group:

```
PUT https://<connection-server>/vmrest/portgroups/<objectid>

<PortGroup>
	<MwiOnCode>678</MwiOnCode>
	<MwiOffCode>876</MwiOffCode>
</PortGroup>
```

The following is the response from the above PUT request:

```
204
No Content
null
```

## Cisco Unity Connection Provisioning Interface (CUPI) API -- Ports

### About Ports

This page contains information on how to use the API to create, list, modify, and delete Ports. The voice messaging ports
                              let Cisco Unity Connection receive calls (for example, to record a message) and let Connection make calls (for example to
                              send message notifications or to set MWIs). Each voice messaging port can belong to only one port group. Port groups, when
                              there are several, each have their own voice messaging ports. The total voice messaging ports belonging to all port groups
                              must not exceed the maximum number of voice messaging ports that are enabled by the Connection license files.

### Listing Ports

Example 1

The following is an example of the GET request that lists the Ports:

```
https://<connection_server>/vmrest/ports
```

The following is an example of the response from the above *GET* request and the actual response will depend upon the information
                                 given by you:

```
<Ports total="2">
 <Port>
   <URI>/vmrest/ports/ec664876-5879-4cff-a022-4929b37bd575</URI>
   <ObjectId>ec664876-5879-4cff-a022-4929b37bd575</ObjectId>
   <MediaPortGroupObjectId>1edf504a-e9a1-4876-bcfc-bb674da8e385</MediaPortGroupObjectId>
   <PortGroupURI>/vmrest/portgroups/1edf504a-e9a1-4876-bcfc-bb674da8e385</PortGroupURI>
   <TelephonyIntegrationMethodEnum>2</TelephonyIntegrationMethodEnum>
   <VmsServerObjectId>574ca5d3-9041-4ff9-8e7d-727c32d80dab</VmsServerObjectId>
   <DisplayName>PhoneSystem-1-001</DisplayName>
   <CapAnswer>true</CapAnswer>
   <CapNotification>true</CapNotification>
   <CapMWI>true</CapMWI>
   <CapEnabled>true</CapEnabled>
   <CapTrapConnection>true</CapTrapConnection>
   <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
   <MediaSwitchObjectId>a8eb65f5-795b-41cd-98b1-934f6b987313</MediaSwitchObjectId>
   <PhoneSystemURI>/vmrest/phonesystems/a8eb65f5-795b-41cd-98b1-934f6b987313</PhoneSystemURI>
   <MediaPortGroupDisplayName>PhoneSystem-1</MediaPortGroupDisplayName>
   <VmsServerName>ucbu-aricent-vm413</VmsServerName>
 </Port>
 <Port>
   <URI>/vmrest/ports/761fa322-63ae-47d9-9fbf-b35142b11eef</URI>
   <ObjectId>761fa322-63ae-47d9-9fbf-b35142b11eef</ObjectId>
   <MediaPortGroupObjectId>1edf504a-e9a1-4876-bcfc-bb674da8e385</MediaPortGroupObjectId>
   <PortGroupURI>/vmrest/portgroups/1edf504a-e9a1-4876-bcfc-bb674da8e385</PortGroupURI>
   <TelephonyIntegrationMethodEnum>2</TelephonyIntegrationMethodEnum>
   <VmsServerObjectId>574ca5d3-9041-4ff9-8e7d-727c32d80dab</VmsServerObjectId>
   <DisplayName>PhoneSystem-1-002</DisplayName>
   <CapAnswer>true</CapAnswer>
<CapNotification>true</CapNotification>
   <CapMWI>true</CapMWI>
   <CapEnabled>true</CapEnabled>
   <CapTrapConnection>true</CapTrapConnection>
   <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
   <MediaSwitchObjectId>a8eb65f5-795b-41cd-98b1-934f6b987313</MediaSwitchObjectId>
   <PhoneSystemURI>/vmrest/phonesystems/a8eb65f5-795b-41cd-98b1-934f6b987313</PhoneSystemURI>
   <MediaPortGroupDisplayName>PhoneSystem-1</MediaPortGroupDisplayName>
   <VmsServerName>ucbu-aricent-vm413</VmsServerName>
 </Port>
```

```
Response Code: 200
```

Example 2

The following is an example of the GET request that lists the Ports configuration:

```
<Port>
  <URI>/vmrest/ports/e4a48f12-d22b-438c-89eb-0b25f2f73d12</URI>
  <ObjectId>e4a48f12-d22b-438c-89eb-0b25f2f73d12</ObjectId>
  <MediaPortGroupObjectId>668e5869-7c16-48d6-8858-cd0e00fdd47c</MediaPortGroupObjectId>
  <PortGroupURI>/vmrest/portgroups/668e5869-7c16-48d6-8858-cd0e00fdd47c</PortGroupURI>
  <TelephonyIntegrationMethodEnum>2</TelephonyIntegrationMethodEnum>
  <VmsServerObjectId>d190d99e-e9e8-4d63-8c6c-9aca4956afff</VmsServerObjectId>
  <DisplayName>PhoneSystem-1-002</DisplayName>
  <CapAnswer>true</CapAnswer>
  <CapNotification>false</CapNotification>
  <CapMWI>true</CapMWI>
  <CapEnabled>true</CapEnabled>
  <CapTrapConnection>true</CapTrapConnection>
  <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
  <MediaSwitchObjectId>0d15753c-e1b4-4865-b00b-999a1ccf56ce</MediaSwitchObjectId>
  <PhoneSystemURI>/vmrest/phonesystems/0d15753c-e1b4-4865-b00b-999a1ccf56ce</PhoneSystemURI>
  <MediaPortGroupDisplayName>PhoneSystem-1</MediaPortGroupDisplayName>
  <VmsServerName>ucbu-aricent-vm413</VmsServerName>
</Port>
```

### Adding Ports

This section contains information on how to add ports:

Adding SCCP Ports

Adding SIP Ports

Adding PIMGTIMG Ports

Note: Before adding ports to port group, you need to know the id of the vmservers. The vmservers id is required as you need
                                 to mention the machine on which the ports need to be added.

The following is an example of the GET request that lists the vmservers:

```
https://<connection_server>/vmrest/vmsservers
```

The following is an example of the response from the above *GET* request and the actual response will depend upon the information
                                 given by you:

```
<VmsServers total="1">
 <VmsServer>
   <URI>/vmrest/vmsservers/574ca5d3-9041-4ff9-8e7d-727c32d80dab</URI>
   <ServerName>ucbu-aricent-vm413</ServerName>
   <VmsServerObjectId>574ca5d3-9041-4ff9-8e7d-727c32d80dab</VmsServerObjectId>
 </VmsServer>
</VmsServers>
```

Make sure that you always add ports in even number and not in odd number.

#### Adding SCCP Ports

The following is an example of the POST request that lists the SCCP Ports:

```
https:/<server_ip>/vmrest/ports
```

The following is an example of the response from the above *POST* request and the actual response will depend upon the information
                                    given by you:

```
<Port>   
   <MediaPortGroupObjectId>3c011243-e3e2-42f7-b658-d9fbdc966f26</MediaPortGroupObjectId>       
   <VmsServerObjectId>574ca5d3-9041-4ff9-8e7d-727c32d80dab</VmsServerObjectId>
   <HuntOrder>0</HuntOrder>
   <CapAnswer>true</CapAnswer>
   <CapNotification>true</CapNotification>    
   <NumberOfPorts>10</NumberOfPorts>
   <CapEnabled>true</CapEnabled>
   <CapTrapConnection>true</CapTrapConnection>   
   <VmsServerName>ucbu-aricent-vm413</VmsServerName>
</Port>
```

```
RESPONSE Code: 201
```

#### Adding SIP Ports

The following is an example of the POST request that lists the SIP Ports:

```
https:/<server_ip>/vmrest/ports
```

The following is an example of the response from the above *POST* request and the actual response will depend upon the information
                                    given by you:

```
<Port>   
   <MediaPortGroupObjectId>575f43be-f5d0-4af7-a689-06d968227ff7</MediaPortGroupObjectId>      <VmsServerObjectId>574ca5d3-9041-4ff9-8e7d-727c32d80dab</VmsServerObjectId>
   <HuntOrder>0</HuntOrder>
   <DisplayName>PhoneSystem-Rohit-001</DisplayName>
   <CapAnswer>true</CapAnswer>
   <CapNotification>true</CapNotification>    
   <NumberOfPorts>4</NumberOfPorts>
   <CapEnabled>true</CapEnabled>
   <CapTrapConnection>true</CapTrapConnection>   
   <VmsServerName>ucbu-aricent-vm413</VmsServerName>
</Port>
```

```
RESPONSE Code: 201
```

#### Adding PIMGTIMG Ports

The following is an example of the POST request that create the PIMGTIMG Ports:

```
https:/<server_ip>/vmrest/ports
```

The following is an example of the response from the above *POST* request and the actual response will depend upon the information
                                    given by you:

```
<Port> 
  <MediaPortGroupObjectId>2c24f5a9-fb22-47fe-a74b-da9c72d6e7f3</MediaPortGroupObjectId>
  <HuntOrder>0</HuntOrder>
  <DisplayName>PhoneSystem-Rohit-002</DisplayName>
  <CapAnswer>true</CapAnswer>
  <CapNotification>true</CapNotification> 
  <NumberOfPorts>2</NumberOfPorts>
  <CapEnabled>true</CapEnabled>
  <CapTrapConnection>true</CapTrapConnection> 
</Port>
```

```
RESPONSE Code: 201
```

The number of ports should be in even number and not in odd number.

### Modifying Ports

This section contains information on how to modify Ports:

Modifying SCCP Ports

Modifying SIP Port

#### Modifying SCCP Ports

The following is an example of the PUT request that modifies the SCCP Ports:

```
https://<connection_server>/vmrest/ports/<sccpobjectId>
```

The actual response will depend upon the information given by you.

```
<Port>   
 <CapAnswer>true</CapAnswer>
 <CapNotification>true</CapNotification>
 <CapMWI>true</CapMWI>
 <CapTrapConnection>true</CapTrapConnection>
<HuntOrder>0</HuntOrder>
<SkinnySecurityModeEnum>0</SkinnySecurityModeEnum>
<CapEnabled>true</CapEnabled>
</Port>
```

```
RESPONSE Code: 204
```

#### Modifying SIP Ports

The following is an example of the PUT request that modifies the SIP Ports:

```
https://<connection_server>/vmrest/ports/<sipobjectId>
```

The actual response will depend upon the information given by you.

```
<Port>   
 <CapAnswer>true</CapAnswer>
 <CapNotification>true</CapNotification>
 <CapMWI>true</CapMWI>
 <CapTrapConnection>true</CapTrapConnection>
 <HuntOrder>0</HuntOrder>
 <SkinnySecurityModeEnum>0</SkinnySecurityModeEnum>
 <CapEnabled>true</CapEnabled>
</Port>
```

```
RESPONSE Code: 204
```

### Deleting ports

The following is an example of the DELETE request that deletes a Port as represented by <portId>:

```
https://<connection_server>/vmrest/ports/<objectId>
```

The output for this request returns the successful response code.

```
RESPONSE Code: 204
```

## Cisco Unity Connection Provisioning Interface (CUPI) API – SIP Certificates

### About SIP Certificates

This section contains information on how to list, modify, and delete SIP Certificates. The SIP certificate is used only by
                              SIP trunk integrations with Cisco Unified CM 7.0 and later, and is required for authentication of the Cisco Unity Connection
                              voice messaging ports.

### Listing SIP Certificates

Example 1

The following is an example of the GET request that lists the SIP Certificates:

```
https://<connection_server>/vmrest/sipcertificates
```

The following is an example of the response from the above *GET* request and the actual response will depend upon the information
                                 given by you:

```
<SipCertificates total="1">
<SipCertificate>
 <URI>
  /vmrest/sipcertificates/c55ef2c3-2475-4505-9566-bcea04a6bb6e
 </URI>
 <ObjectId>c55ef2c3-2475-4505-9566-bcea04a6bb6e</ObjectId>
 <Certificate>
 -----BEGIN CERTIFICATE----- MIICVzCCAcCgAwIBAgIQQmAlZbMuRhSQnNHI4sqpDjANBgkqhkiG9w0BAQUFADA6  MTgwNgYDVQQDEy9DaXNjb1VuaXR5LWJlMjc5NzZjLTZlNmUtNDE5Zi04NTNkLWIz NzY0ODgxZGZiMDAeFw0xMjA3MTgxMzE1MTdaFw0xOTA3MTAwOTAwNThaMDsxGzAZ BgNVBAoTEkNpc2NvIFN5c3RlbXMgSW5jLjEOMAwGA1UECxMFRUNTQlUxDDAKBgNV BAMTA2FhYTCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAwslps1QPmb/mtfSD mHQ8tdnAPcIWriAqF283p7eQcGKdj9ji+YpDGmMFbaKG5NyPBzVCA2EXgNSrh2tX 8PTTUDUOlfGeqrol0H3kT1viFPxNIVVfnn6fuq4A8thoH54+QGlnOWqfuR6+Y4EZ yT4yhygh5yhRIDW6PTHCyhUnMuUCAwEAAaNdMFswHQYDVR0OBBYEFJ2AaJ5nN36z W6BaE5jVTEmAj54/MAsGA1UdDwQEAwIDqDAdBgNVHSUEFjAUBggrBgEFBQcDAQYI KwYBBQUHAwIwDgYDVR0RBAcwBYYDYWFhMA0GCSqGSIb3DQEBBQUAA4GBAJffZqLV 7pmQ+1HEBUO3dVnNdDr7V6izeh3KgoUHW7cEzUuM5wjsRLV7Mh8H9YvGyQP2sMMc iDRpJp4oNpnXZtwd8WEQcToaXvDOR9TfMr5tX9NdkAQGvb8pvt3kPd5cv3s79/Zy DRhjKYIr7A0dKZEpNAFUhTTHbTeNQiOibaGF -----END  CERTIFICATE-----
 </Certificate>

 <PrivateKey>
USkzHb9O2SAH6sofOA1sM91H+Whkpxl+/Sit7MF4+IfPE7u1shotouuFFO9lT11ouADtbjYp2WsqzndpjPRUZ5I4na9nc4uBqLkrQQ6FZ9r2POBgX5EkoA4l5oYUNhJyNIbdqND54Kn1iO6uIKV/NIngQBSGWM0i2Yh+HezEjP2TY9orxD0v6MHtBTsmZvcbWScwpzIAVE6dP2/OeI2+21zG82m+xLmJnfuyiZc/RcmZ2MqOqQYL3IV9Gmo8l09ocQhst2TYBCEsvI6+hId5YujfO1iyL//1rr8GD7lQVBzicFPChR0rqUnGzlilrIpnEEbenUs2HpLw/F+lg1awgGRwe3S5moYClBEor1b5g8UIPXAi0QJNF0PPm4P+ImLCfERghinxz/DSiuE5IVkwfdPUPzPknZt+4SjcX0/VU0zIg42lZ5Xl7rJRonA8a2bnFQkg9Vm8D/TTqrzAy+tdawOGdlnuAN+Hoov1prRZnR5zjkpJaImK3zE0WZyqJsyEQdVaMZEK0irb/fePw5nujRxNJi0eF/AsyDkKEazz5YrjDBZ8QuYAFOr1k9IJI0J8ZkU8krRRQCztWdY63k89XqCRzkN0SxEwu39UDajCbFOq7dbDmkalvKfp6lcrRMZy0OtpB3XgzbBvdAb6H3YZquQdCrdtwSKb/VovNssqqgWXbeocqf0vv2SSbJC+tdJIbZlDOMt7x/glz6z0GabyGb6w8SjYGN0xSUZ+ioVlmhZ8qMOZ33fwW87ctXaRo68jBDcQJHHI2aeYDABMTe3MoMI0R5A4pWUkNWGCjWhyq52kXvY8mjIRhYCEkDxEsvd6l+XRm2A02PCPpX01eeXZ5neZ30jApWkdEzfcQfV57DtEtn8NXv3GCiL59qjiABuAA0aHtUmA36m6mfuh8QWqMRRoZHI5eXUUNjeTt3kyV4jINutEu8dVAujShai/e+wNEulE4clWjh6LaoHjjjfg3MR28f0/bbv2yTPRyy/z5zW4/7z8QwKDh20fnLsLt7VatD1HcKjV2sXB50DBkLz4izVrmkLebLaIUs5pYorAVGf7MpPgVkqcbaE+A4qxpllnl2eQuQGe6a9IioFaY0UVmN3SCBke6lCDqB5qhWkqTOlJGHwV6LBz2hTnjhd62CP8668clvL3YZsC6tdA7CxJPpQZ0b36iS6CclJge2mLVa+CQNnBK68HCP+9y0YddGewEiK+8+D+x6fZC7ng+SYn2iQYHYm9BP7nYdP0YWy/aMy/ga39oHRSyjWv8GfsQNcdFdgEUMCxVx+fUK0Ao8tQKiamJjm8xyCM27UK0RBvy98=
 </PrivateKey>
 <SubjectName>test</SubjectName>
 <DisplayName>test</DisplayName>
</SipCertificate>
</SipCertificates>
```

```
Response code: 200
```

Example 2

The following is an example of the GET request that lists a specified SIP Certificate:

```
https://<connection_server>/vmrest/sipcertificate/<objectId>
```

The following is an example of the response from the above *GET* request and the actual response will depend upon the information
                                 given by you:

```
<SipCertificate>
 <URI>
  /vmrest/sipcertificates/c55ef2c3-2475-4505-9566-bcea04a6bb6e
 </URI>
 <ObjectId>c55ef2c3-2475-4505-9566-bcea04a6bb6e</ObjectId>
 <Certificate>
 -----BEGIN CERTIFICATE----- MIICVzCCAcCgAwIBAgIQQmAlZbMuRhSQnNHI4sqpDjANBgkqhkiG9w0BAQUFADA6 MTgwNgYDVQQDEy9DaXNjb1VuaXR5LWJlMjc5NzZjLTZlNmUtNDE5Zi04NTNkLWIz NzY0ODgxZGZiMDAeFw0xMjA3MTgxMzE1MTdaFw0xOTA3MTAwOTAwNThaMDsxGzAZ BgNVBAoTEkNpc2NvIFN5c3RlbXMgSW5jLjEOMAwGA1UECxMFRUNTQlUxDDAKBgNV BAMTA2FhYTCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAwslps1QPmb/mtfSD mHQ8tdnAPcIWriAqF283p7eQcGKdj9ji+YpDGmMFbaKG5NyPBzVCA2EXgNSrh2tX 8PTTUDUOlfGeqrol0H3kT1viFPxNIVVfnn6fuq4A8thoH54+QGlnOWqfuR6+Y4EZ yT4yhygh5yhRIDW6PTHCyhUnMuUCAwEAAaNdMFswHQYDVR0OBBYEFJ2AaJ5nN36z W6BaE5jVTEmAj54/MAsGA1UdDwQEAwIDqDAdBgNVHSUEFjAUBggrBgEFBQcDAQYI KwYBBQUHAwIwDgYDVR0RBAcwBYYDYWFhMA0GCSqGSIb3DQEBBQUAA4GBAJffZqLV 7pmQ+1HEBUO3dVnNdDr7V6izeh3KgoUHW7cEzUuM5wjsRLV7Mh8H9YvGyQP2sMMc iDRpJp4oNpnXZtwd8WEQcToaXvDOR9TfMr5tX9NdkAQGvb8pvt3kPd5cv3s79/Zy DRhjKYIr7A0dKZEpNAFUhTTHbTeNQiOibaGF -----END CERTIFICATE-----
 </Certificate>
 <PrivateKey>
USkzHb9O2SAH6sofOA1sM91H+Whkpxl+/Sit7MF4+IfPE7u1shotouuFFO9lT11ouADtbjYp2WsqzndpjPRUZ5I4na9nc4uBqLkrQQ6FZ9r2POBgX5EkoA4l5oYUNhJyNIbdqND54Kn1iO6uIKV/NIngQBSGWM0i2Yh+HezEjP2TY9orxD0v6MHtBTsmZvcbWScwpzIAVE6dP2/OeI2+21zG82m+xLmJnfuyiZc/RcmZ2MqOqQYL3IV9Gmo8l09ocQhst2TYBCEsvI6+hId5YujfO1iyL//1rr8GD7lQVBzicFPChR0rqUnGzlilrIpnEEbenUs2HpLw/F+lg1awgGRwe3S5moYClBEor1b5g8UIPXAi0QJNF0PPm4P+ImLCfERghinxz/DSiuE5IVkwfdPUPzPknZt+4SjcX0/VU0zIg42lZ5Xl7rJRonA8a2bnFQkg9Vm8D/TTqrzAy+tdawOGdlnuAN+Hoov1prRZnR5zjkpJaImK3zE0WZyqJsyEQdVaMZEK0irb/fePw5nujRxNJi0eF/AsyDkKEazz5YrjDBZ8QuYAFOr1k9IJI0J8ZkU8krRRQCztWdY63k89XqCRzkN0SxEwu39UDajCbFOq7dbDmkalvKfp6lcrRMZy0OtpB3XgzbBvdAb6H3YZquQdCrdtwSKb/VovNssqqgWXbeocqf0vv2SSbJC+tdJIbZlDOMt7x/glz6z0GabyGb6w8SjYGN0xSUZ+ioVlmhZ8qMOZ33fwW87ctXaRo68jBDcQJHHI2aeYDABMTe3MoMI0R5A4pWUkNWGCjWhyq52kXvY8mjIRhYCEkDxEsvd6l+XRm2A02PCPpX01eeXZ5neZ30jApWkdEzfcQfV57DtEtn8NXv3GCiL59qjiABuAA0aHtUmA36m6mfuh8QWqMRRoZHI5eXUUNjeTt3kyV4jINutEu8dVAujShai/e+wNEulE4clWjh6LaoHjjjfg3MR28f0/bbv2yTPRyy/z5zW4/7z8QwKDh20fnLsLt7VatD1HcKjV2sXB50DBkLz4izVrmkLebLaIUs5pYorAVGf7MpPgVkqcbaE+A4qxpllnl2eQuQGe6a9IioFaY0UVmN3SCBke6lCDqB5qhWkqTOlJGHwV6LBz2hTnjhd62CP8668clvL3YZsC6tdA7CxJPpQZ0b36iS6CclJge2mLVa+CQNnBK68HCP+9y0YddGewEiK+8+D+x6fZC7ng+SYn2iQYHYm9BP7nYdP0YWy/aMy/ga39oHRSyjWv8GfsQNcdFdgEUMCxVx+fUK0Ao8tQKiamJjm8xyCM27UK0RBvy98=
 </PrivateKey>
 <SubjectName>test</SubjectName>
 <DisplayName>test</DisplayName>
</SipCertificate>
```

```
Response code: 200
```

### Modifying SIP Certificates

The following is an example of the PUT request that modifies the SIP Certificates:

```
https://<connection_server>/vmrest/ sipcertificates/<objectid>
```

The actual response will depend upon the information given by you.

```
<SipCertificate>
 <SubjectName>test2</SubjectName>
 <DisplayName>test2</DisplayName>
</SipCertificate>
```

```
Response code: 204
```

### Deleting SIP Certificates

The following is an example of the DELETE request that deletes a specified SIP Certificates as represented by <sipcertificateid>:

```
https://<connection_server>/vmrest/sipcertificates/<objectId>
```

The output for this request returns the successful response code.

```
Response code: 204
```

## Cisco Unity Connection Provisioning Interface (CUPI) API -- SIP Profiles

### Listing SIP Profiles

Generic Examples to List SIP Profiles

Example 1

The following is an example of the GET request that lists the SIP Profiles:

```
https:/<server_ip>/vmrest/sipsecurityprofiles
```

The following is an example of the response from the above *GET* request and the actual response will depend upon the information
                                 given by you:

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<SipSecurityProfiles total="2"><SipSecurityProfile>
 <URI>/vmrest/sipsecurityprofiles/87cab9a5-c68d-447a-ab4f-7cd2837aa240</URI>
 <ObjectId>87cab9a5-c68d-447a-ab4f-7cd2837aa240</ObjectId><Port>5069</Port>
 <DoTLS>false</DoTLS><DisplayName>5069</DisplayName>
 </SipSecurityProfile><SipSecurityProfile>
 <URI>/vmrest/sipsecurityprofiles/4d7e055a-cdcf-43ff-a922-4ce743939a23</URI>
 <ObjectId>4d7e055a-cdcf-43ff-a922-4ce743939a23</ObjectId><Port>5066</Port>
 <DoTLS>true</DoTLS><DisplayName>5066/TLS</DisplayName>
</SipSecurityProfile></SipSecurityProfiles>

<Pre> RESPONSE Code: 200
```

Example 2

The following is an example of the GET request that lists a specified SIP Profile:

```
https://<connection_server>/vmrest/sipsecurityprofiles/<objectId>
```

The following is an example of the response from the above *GET* request and the actual response will depend upon the information
                                 given by you:

```
<SipSecurityProfile>
 <URI>/vmrest/sipsecurityprofiles/87cab9a5-c68d-447a-ab4f-7cd2837aa240</URI>
 <ObjectId>87cab9a5-c68d-447a-ab4f-7cd2837aa240</ObjectId><Port>5069</Port>
 <DoTLS>false</DoTLS><DisplayName>5069</DisplayName>
</SipSecurityProfile><SipSecurityProfile>

<pre> Response code: 200
```

JSON Examples to List SIP Profiles

Example 1

The following is a JSON example of the GET request that lists the SIP Profiles:

```
https:/<connection_server>/vmrest/sipsecurityprofiles
```

The following is an example of the response from the above *GET* request and the actual response will depend upon the information
                                 given by you:

```
{
  "@total": "6",
  "SipSecurityProfile":    
  {
    "URI": "/vmrest/sipsecurityprofiles/08aef04e-8775-4ea5-916b-f7e36cbdb3d4",
    "ObjectId": "08aef04e-8775-4ea5-916b-f7e36cbdb3d4",
    "Port": "5065",
    "DoTLS": "true",
    "DisplayName": "5065/TLS"
  },
  {
    "URI": "/vmrest/sipsecurityprofiles/b3c533a4-bc28-4c70-9912-c22edf81910e",
    "ObjectId": "b3c533a4-bc28-4c70-9912-c22edf81910e",
    "Port": "5062",
    "DoTLS": "true",
    "DisplayName": "5062/TLS"
   },
   {
     "URI": "/vmrest/sipsecurityprofiles/e667342c-3ce2-49f7-ae2b-27daf850b159",
     "ObjectId": "e667342c-3ce2-49f7-ae2b-27daf850b159",
     "Port": "5088",
     "DoTLS": "true",
     "DisplayName": "5088/TLS"
   },
   {
     "URI": "/vmrest/sipsecurityprofiles/9062519a-05d4-42f2-933e-250d5a24efb5",
     "ObjectId": "9062519a-05d4-42f2-933e-250d5a24efb5",
     "Port": "5067",
     "DoTLS": "false",
     "DisplayName": "5067"
   },
   {
     "URI": "/vmrest/sipsecurityprofiles/9adbf7ac-c882-4ad1-84d5-d67d56d44d6d",
     "ObjectId": "9adbf7ac-c882-4ad1-84d5-d67d56d44d6d",
     "Port": "5077",
     "DoTLS": "false",
     "DisplayName": "5077"
   },
   {
     "URI": "/vmrest/sipsecurityprofiles/15a3a4d9-65a0-456a-be38-4a4aff36554c",
     "ObjectId": "15a3a4d9-65a0-456a-be38-4a4aff36554c",
     "Port": "5060",
     "DoTLS": "false",
     "DisplayName": "5060"
   }
   
}

<pre> RESPONSE Code: 200
```

Example 2

The following is a example of the GET request that lists a specified SIP Profile:

```
https://<connection_server>/vmrest/sipsecurityprofiles/<objectId>
```

The following is an example of the response from the above *GET* request and the actual response will depend upon the information
                                 given by you:

```
{
   "URI": "/vmrest/sipsecurityprofiles/9adbf7ac-c882-4ad1-84d5-d67d56d44d6d",
   "ObjectId": "9adbf7ac-c882-4ad1-84d5-d67d56d44d6d",
   "Port": "5077",
   "DoTLS": "false",
   "DisplayName": "5077"
}
```

```
RESPONSE Code: 200
```

### Adding a new SIP Profiles

Example 1

The following is an example of the POST request that lists the SIP Profiles:

```
https://<connection_server>/vmrest/sipsecurityprofiles
```

The following is an example of the response from the above *POST* request and the actual response will depend upon the information
                                 given by you:

```
<SipSecurityProfile>
 <Port>5070</Port>
 <DoTLS>true</DoTLS>
</SipSecurityProfile>
```

```
Response code: 201
```

Example 2

```
https://<connection_server>/vmrest/sipsecurityprofiles
```

The following is an example of the response from the above *POST* request and the actual response will depend upon the information
                                 given by you:

```
{
   "Port": "5080",
   "DoTLS": "true"
}
```

```
Response code: 201
```

### Modifying SIP Profiles

Example 1

The following is an example of the PUT request that modifies the SIP Profile:

```
https://<connection_server>/vmrest/sipsecurityprofiles/<objectId>
```

The actual response will depend upon the information given by you.

```
<SipSecurityProfile>
 <Port>5070</Port>
 <DoTLS>true</DoTLS>
 </SipSecurityProfile>
```

```
Response code: 204
```

Example 2

The following is a JSON example of the PUT request that modifies the SIP Profile:

```
https://<connection_server>/vmrest/sipsecurityprofiles/<objectId>
```

The actual response will depend upon the information given by you.

```
{
   "Port": "5077",
   "DoTLS": "true"
}
```

```
Response code: 204
```

### Deleting SIP Profiles

The following is an example of the DELETE request that deletes a specified SIP Profiles as represented by <sipsecurityprofileid>:

```
https://<server-ip>/vmrest/ sipsecurityprofiles/<objectId>
```

The output for this request returns the successful response code.

```
Response Code: 204
```

| https://<connection_server>/vmrest/phonesystems |
|---|

| <PhoneSystems total="1">
 <PhoneSystem>
   <URI>/vmrest/phonesystems/aa6d3f45-ccdf-4fa2-8170-e5c94b51813a</URI>
   <ObjectId>aa6d3f45-ccdf-4fa2-8170-e5c94b51813a</ObjectId>
   <DisplayName>PhoneSystem</DisplayName>
   <MwiAlwaysUpdate>false</MwiAlwaysUpdate>
   <MwiPortMemory>false</MwiPortMemory>
   <CallLoopSupervisedTransferDetect>false</CallLoopSupervisedTransferDetect>
   <CallLoopForwardNotificationDetect>false</CallLoopForwardNotificationDetect>
   <CallLoopDTMF>A</CallLoopDTMF>
   <CallLoopGuardTimeMs>2500</CallLoopGuardTimeMs>
   <PortCount>0</PortCount>
   <EnablePhoneApplications>false</EnablePhoneApplications>
   <DefaultTRaPSwitch>true</DefaultTRaPSwitch>
   <MwiForceOff>false</MwiForceOff>
   <RestrictDialUnconditional>false</RestrictDialUnconditional>
   <RestrictDialScheduled>false</RestrictDialScheduled>
   <RestrictDialStartTime>0</RestrictDialStartTime>
   <RestrictDialEndTime>0</RestrictDialEndTime>
   <CallLoopExtensionDetect>true</CallLoopExtensionDetect>
   <AXLServerURI>/vmrest/phonesystems/aa6d3f45-ccdf-4fa2-8170-e5c94b51813a/axlservers</AXLServerURI>
   <PhoneSystemAssociationURI>/vmrest/phonesystems/aa6d3f45-ccdf-4fa2-8170-e5c94b51813a/phonesystemassociations</PhoneSystemAssociationURI>
 </PhoneSystem>
</PhoneSystems> |
|---|

| Response Code: 200 |
|---|

| https:/<connection_server>/vmrest/phonesystem/<objectId> |
|---|

| <PhoneSystem>
 <URI>/vmrest/phonesystems/aa6d3f45-ccdf-4fa2-8170-e5c94b51813a</URI>
 <ObjectId>aa6d3f45-ccdf-4fa2-8170-e5c94b51813a</ObjectId>
 <DisplayName>PhoneSystem</DisplayName>
 <MwiAlwaysUpdate>false</MwiAlwaysUpdate>
 <MwiPortMemory>false</MwiPortMemory>
 <CallLoopSupervisedTransferDetect>false</CallLoopSupervisedTransferDetect>
 <CallLoopForwardNotificationDetect>false</CallLoopForwardNotificationDetect>
 <CallLoopDTMF>A</CallLoopDTMF>
 <CallLoopGuardTimeMs>2500</CallLoopGuardTimeMs>
 <PortCount>0</PortCount>
 <EnablePhoneApplications>false</EnablePhoneApplications>
 <DefaultTRaPSwitch>true</DefaultTRaPSwitch>
 <MwiForceOff>false</MwiForceOff>
 <RestrictDialUnconditional>false</RestrictDialUnconditional>
 <RestrictDialScheduled>false</RestrictDialScheduled>
 <RestrictDialStartTime>0</RestrictDialStartTime>
 <RestrictDialEndTime>0</RestrictDialEndTime>
 <CallLoopExtensionDetect>true</CallLoopExtensionDetect>
 <AXLServerURI>/vmrest/phonesystems/aa6d3f45-ccdf-4fa2-8170-e5c94b51813a/axlservers</AXLServerURI>
 <PhoneSystemAssociationURI>/vmrest/phonesystems/aa6d3f45-ccdf-4fa2-8170-e5c94b51813a/phonesystemassociations</PhoneSystemAssociationURI>
</PhoneSystem> |
|---|

| Response Code: 200 |
|---|

| https://<connection_server>/vmrest/phonesystems |
|---|

| <PhoneSystem>
 <DisplayName>PhoneSystem1</DisplayName>
</PhoneSystem> |
|---|

| Response Code: 201 |
|---|

| Note | To create a phone system, only the <DisplayName> parameter is mandatory. |
|---|---|

| https:/<Connection_server>/vmrest/phonesystem/<objectId> |
|---|

| <PhoneSystem>
 <MwiAlwaysUpdate>false</MwiAlwaysUpdate>
 <MwiPortMemory>false</MwiPortMemory>
 <CallLoopSupervisedTransferDetect>false</CallLoopSupervisedTransferDetect>
 <CallLoopForwardNotificationDetect>false</CallLoopForwardNotificationDetect>
 <CallLoopDTMF>A</CallLoopDTMF>
 <CallLoopGuardTimeMs>2500</CallLoopGuardTimeMs>
 <PortCount>2</PortCount>
</PhoneSystem> |
|---|

| Response Code: 204 |
|---|

| https://<connection_server>/vmrest/phonesystems/<objectId>/axlservers |
|---|

| <AXLServers total="2">
<AXLServer>
<URI>
/vmrest/phonesystems/a560c009-e802-466f-b42d-4c64e8ea8260/axlservers/59daf270-3e88-4d81-8dae-a3b0a5fbebb1
</URI>
<ObjectId>59daf270-3e88-4d81-8dae-a3b0a5fbebb1</ObjectId>
<MediaRemoteServiceEnum>103</MediaRemoteServiceEnum>
<HostOrIPAddress>0:0:0:0:0:1</HostOrIPAddress>
<Port>443</Port>
<TlsPort>443</TlsPort>
<Precedence>1</Precedence>
<MediaSwitchObjectId>a560c009-e802-466f-b42d-4c64e8ea8260</MediaSwitchObjectId>
<PhoneSystemURI>
/vmrest/phonesystems/a560c009-e802-466f-b42d-4c64e8ea8260
</PhoneSystemURI>
<SkinnyStateMachineEnum>10</SkinnyStateMachineEnum>
<IsPinSyncEnabled>false</IsPinSyncEnabled>
<CcmAXLUser>admin</CcmAXLUser>
<CcmAXLPassword/>
<CcmVersion>5</CcmVersion>
</AXLServer>
<AXLServer>
<URI>
/vmrest/phonesystems/a560c009-e802-466f-b42d-4c64e8ea8260/axlservers/59daf270-3e88-4d81-8dae-a3b0a5fbebb1
</URI>
<ObjectId>59daf270-3e88-4d81-8dae-a3b0a5fbebb1</ObjectId>
<MediaRemoteServiceEnum>103</MediaRemoteServiceEnum>
<HostOrIPAddress>0.0.0.1</HostOrIPAddress>
<Port>443</Port>
<TlsPort>443</TlsPort>
<Precedence>1</Precedence>
<MediaSwitchObjectId>a560c009-e802-466f-b42d-4c64e8ea8260</MediaSwitchObjectId>
<PhoneSystemURI>
/vmrest/phonesystems/a560c009-e802-466f-b42d-4c64e8ea8260
</PhoneSystemURI>
<SkinnyStateMachineEnum>10</SkinnyStateMachineEnum>
<IsPinSyncEnabled>false</IsPinSyncEnabled>
<CcmAXLUser>admin</CcmAXLUser>
<CcmAXLPassword/>
<CcmVersion>5</CcmVersion>
</AXLServer>
</AXLServers> |
|---|

| Response Code: 200 |
|---|

| https://<connection_server>/vmrest/phonesystems/<objectId>/axlservers |
|---|

| <AXLServer>
 <MediaSwitchObjectId>24f1171f-27b3-4ad3-a94c-66d1fb2e448b</MediaSwitchObjectId>
 <MediaRemoteServiceEnum>103</MediaRemoteServiceEnum>
 <HostOrIPAddress>10.105.255.1</HostOrIPAddress>
 <Port>2001</Port>
 <TlsPort>2000</TlsPort>
 <Precedence>1</Precedence>
 <CcmAXLUser>abcd</CcmAXLUser>
 <CcmAXLPassword/>
 <CcmVersion>5</CcmVersion>
 <IsPinSyncEnabled>false</IsPinSyncEnabled>
</AXLServer> |
|---|

| Response Code: 201 |
|---|

| https://<connection_server>/vmrest/phonesystems/<objectId>/axlservers/<objectId> |
|---|

| <AXLServer>
 <MediaSwitchObjectId>24f1171f-27b3-4ad3-a94c-66d1fb2e448b</MediaSwitchObjectId>
 <CcmAXLUser>CiscoCCM</CcmAXLUser>
 <CcmAXLPassword/> 
 <CcmVersion>5</CcmVersion>
</AXLServer> |
|---|

| Response Code: 204 |
|---|

| https:/<connection_server>/vmrest/phonesystems/<objectId>/axlservers/<objectId> |
|---|

| Response Code: 204 |
|---|

| https://<connection_server>/vmrest/phonesystems/<objectId>/phonesystemassociations |
|---|

| <PhoneSystemAssociations total="2">
 <PhoneSystemAssociation>
   <URI>/vmrest/phonesystems/24f1171f-27b3-4ad3-a94c-66d1fb2e448b/phonesystemassociations/219ce340-a3a5-428c-8dc6-4776690b69ee</URI>
   <Alias>undeliverablemessagesmailbox</Alias>
   <DisplayName>Papa Recommended Web Application Authentication Rule</DisplayName>
   <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
   <MediaSwitchObjectId>24f1171f-27b3-4ad3-a94c-66d1fb2e448b</MediaSwitchObjectId>
   <PhoneSystemURI>/vmrest/phonesystems/24f1171f-27b3-4ad3-a94c-66d1fb2e448b</PhoneSystemURI>
   <numNotificationDevice>4</numNotificationDevice>
   <numNotificationMWI>1</numNotificationMWI>
   <numPrimaryCallHandler>1</numPrimaryCallHandler>
   <ObjectId>219ce340-a3a5-428c-8dc6-4776690b69ee</ObjectId>
 </PhoneSystemAssociation>
 <PhoneSystemAssociation>
   <URI>/vmrest/phonesystems/24f1171f-27b3-4ad3-a94c-66d1fb2e448b/phonesystemassociations/6b455973-13d1-4b10-871e-1d1d55f160d2</URI>
   <Alias>operator</Alias>
   <DisplayName>Operator</DisplayName>
   <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
   <MediaSwitchObjectId>24f1171f-27b3-4ad3-a94c-66d1fb2e448b</MediaSwitchObjectId>
   <PhoneSystemURI>/vmrest/phonesystems/24f1171f-27b3-4ad3-a94c-66d1fb2e448b</PhoneSystemURI>
   <numNotificationDevice>4</numNotificationDevice>
   <numNotificationMWI>1</numNotificationMWI>
   <numPrimaryCallHandler>1</numPrimaryCallHandler>
   <ObjectId>6b455973-13d1-4b10-871e-1d1d55f160d2</ObjectId>
 </PhoneSystemAssociation>	 
</PhoneSystemAssociations>> |
|---|

| Response Code: 200 |
|---|

| https://<server-ip>/vmrest/phonesystems/<objectId> |
|---|

| Response Code: 204 |
|---|

| Note | Port groups cannot be created or deleted via the API, and only two fields (MwiOnCode & MwiOffCode) can be updated by using
                                          the PUT method. |
|---|---|

| GET http://<connection-server>/vmrest/portgroups |
|---|

| 200
OK
<?xml version="1.0" encoding="UTF-8"?>
<PortGroups total="1">
  <PortGroup>
    <URI>/vmrest/portgroups/035853ce-f4e6-4de2-bda2-84acf827a555</URI>
    <MediaPortGroupTemplateObjectId>90dd306f-b8af-46b6-8289-f13437cc1e5e</MediaPortGroupTemplateObjectId>
    <MediaSwitchObjectId>05186ad4-572c-48d1-aaa6-ac22280c8702</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/05186ad4-572c-48d1-aaa6-ac22280c8702</PhoneSystemURI>
    <TelephonyIntegrationMethodEnum>1</TelephonyIntegrationMethodEnum>
    <EnableMWI>true</EnableMWI>
    <DisplayName>PhoneSystem-1</DisplayName>
    <CcmDoAutoFailback>true</CcmDoAutoFailback>
    <MwiOnCode/>
    <MwiOffCode/>
    <MwiRetryCountOnSuccess>0</MwiRetryCountOnSuccess>
    <MwiRetryIntervalOnSuccessMs>5</MwiRetryIntervalOnSuccessMs>
    <ObjectId>035853ce-f4e6-4de2-bda2-84acf827a555</ObjectId>
    <SipTransportProtocolEnum>10</SipTransportProtocolEnum>
    <SipRegisterWithProxyServer>false</SipRegisterWithProxyServer>
    <SipDoAuthenticate>false</SipDoAuthenticate>
    <SkinnyDevicePrefix>test-VI</SkinnyDevicePrefix>
    <MwiMinRequestIntervalMs>0</MwiMinRequestIntervalMs>
    <MwiMaxConcurrentRequests>0</MwiMaxConcurrentRequests>
    <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
    <PortCount>2</PortCount>
    <SipDoSRTP>true</SipDoSRTP>
    <SipTLSModeEnum>11</SipTLSModeEnum>
    <ResetStatusEnum>0</ResetStatusEnum>
  </PortGroup>
</PortGroups> |
|---|

| GET http://<connection-server>/vmrest/portgroups?sort=(DisplayName%20desc) |
|---|

| GET http://<connection-server>/vmrest/portgroups/<objectid> |
|---|

| GET http://<connection-server>/vmrest/ports |
|---|

| 200
OK
<?xml version="1.0" encoding="UTF-8"?>
<Ports total="2">
  <Port>
    <URI>/vmrest/ports/2806ecdc-0a3d-43f3-a2c8-93d786fa506b</URI>
    <ObjectId>2806ecdc-0a3d-43f3-a2c8-93d786fa506b</ObjectId>
    <MediaPortGroupObjectId>035853ce-f4e6-4de2-bda2-84acf827a555</MediaPortGroupObjectId>
    <PortGroupURI>/vmrest/portgroups/035853ce-f4e6-4de2-bda2-84acf827a555</PortGroupURI>
    <TelephonyIntegrationMethodEnum>1</TelephonyIntegrationMethodEnum>
    <PortNumInGroup>1</PortNumInGroup>
    <SkinnySecurityModeEnum>0</SkinnySecurityModeEnum>
    <SkinnyDoMediaEncryption>false</SkinnyDoMediaEncryption>
    <VmsServerObjectId>a7ba129e-6420-4d44-b060-93b638ba866a</VmsServerObjectId>
    <HuntOrder>0</HuntOrder>
    <DisplayName>PhoneSystem-1-001</DisplayName>
    <SkinnyDeviceName>test-VI1</SkinnyDeviceName>
    <PimgPortNumber>1</PimgPortNumber>
    <CapAnswer>true</CapAnswer>
    <CapNotification>true</CapNotification>
    <CapMWI>true</CapMWI>
    <CapEnabled>true</CapEnabled>
    <CapDeliverAmis>false</CapDeliverAmis>
    <CapTrapConnection>true</CapTrapConnection>
    <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
    <MediaSwitchObjectId>05186ad4-572c-48d1-aaa6-ac22280c8702</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/05186ad4-572c-48d1-aaa6-ac22280c8702</PhoneSystemURI>
    <MediaPortGroupDisplayName>PhoneSystem-1</MediaPortGroupDisplayName>
    <MediaPortGroupEnableMWI>true</MediaPortGroupEnableMWI>
    <MediaPortGroupMwiReqPortSpecific>true</MediaPortGroupMwiReqPortSpecific>
    <SipSendPort>0</SipSendPort>
    <VmsServerName>cuc-install-55</VmsServerName>
  </Port>
  <Port>
    <URI>/vmrest/ports/f87ad180-7d06-48c9-b9bd-e6b5cd2311bc</URI>
    <ObjectId>f87ad180-7d06-48c9-b9bd-e6b5cd2311bc</ObjectId>
    <MediaPortGroupObjectId>035853ce-f4e6-4de2-bda2-84acf827a555</MediaPortGroupObjectId>
    <PortGroupURI>/vmrest/portgroups/035853ce-f4e6-4de2-bda2-84acf827a555</PortGroupURI>
    <TelephonyIntegrationMethodEnum>1</TelephonyIntegrationMethodEnum>
    <PortNumInGroup>2</PortNumInGroup>
    <SkinnySecurityModeEnum>0</SkinnySecurityModeEnum>
    <SkinnyDoMediaEncryption>false</SkinnyDoMediaEncryption>
    <VmsServerObjectId>a7ba129e-6420-4d44-b060-93b638ba866a</VmsServerObjectId>
    <HuntOrder>0</HuntOrder>
    <DisplayName>PhoneSystem-1-002</DisplayName>
    <SkinnyDeviceName>test-VI2</SkinnyDeviceName>
    <PimgPortNumber>2</PimgPortNumber>
    <CapAnswer>true</CapAnswer>
    <CapNotification>true</CapNotification>
    <CapMWI>true</CapMWI>
    <CapEnabled>true</CapEnabled>
    <CapDeliverAmis>false</CapDeliverAmis>
    <CapTrapConnection>true</CapTrapConnection>
    <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
    <MediaSwitchObjectId>05186ad4-572c-48d1-aaa6-ac22280c8702</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/05186ad4-572c-48d1-aaa6-ac22280c8702</PhoneSystemURI>
    <MediaPortGroupDisplayName>PhoneSystem-1</MediaPortGroupDisplayName>
    <MediaPortGroupEnableMWI>true</MediaPortGroupEnableMWI>
    <MediaPortGroupMwiReqPortSpecific>true</MediaPortGroupMwiReqPortSpecific>
    <SipSendPort>0</SipSendPort>
    <VmsServerName>cuc-install-55</VmsServerName>
  </Port>
</Ports> |
|---|

| GET http://<connection-server>/vmrest/ports/<objectid> |
|---|

| GET http://<connection-server>/vmrest/portgroups?query=(displayname%20startswith%20PhoneSystem) |
|---|

| GET http://<connection-server>/vmrest/portgroups?query=(EnableMWI%20is%201) |
|---|

| PUT https://<connection-server>/vmrest/portgroups/<objectid>

<PortGroup>
	<MwiOnCode>678</MwiOnCode>
	<MwiOffCode>876</MwiOffCode>
</PortGroup> |
|---|

| 204
No Content
null |
|---|

| https://<connection_server>/vmrest/ports |
|---|

| <Ports total="2">
 <Port>
   <URI>/vmrest/ports/ec664876-5879-4cff-a022-4929b37bd575</URI>
   <ObjectId>ec664876-5879-4cff-a022-4929b37bd575</ObjectId>
   <MediaPortGroupObjectId>1edf504a-e9a1-4876-bcfc-bb674da8e385</MediaPortGroupObjectId>
   <PortGroupURI>/vmrest/portgroups/1edf504a-e9a1-4876-bcfc-bb674da8e385</PortGroupURI>
   <TelephonyIntegrationMethodEnum>2</TelephonyIntegrationMethodEnum>
   <VmsServerObjectId>574ca5d3-9041-4ff9-8e7d-727c32d80dab</VmsServerObjectId>
   <DisplayName>PhoneSystem-1-001</DisplayName>
   <CapAnswer>true</CapAnswer>
   <CapNotification>true</CapNotification>
   <CapMWI>true</CapMWI>
   <CapEnabled>true</CapEnabled>
   <CapTrapConnection>true</CapTrapConnection>
   <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
   <MediaSwitchObjectId>a8eb65f5-795b-41cd-98b1-934f6b987313</MediaSwitchObjectId>
   <PhoneSystemURI>/vmrest/phonesystems/a8eb65f5-795b-41cd-98b1-934f6b987313</PhoneSystemURI>
   <MediaPortGroupDisplayName>PhoneSystem-1</MediaPortGroupDisplayName>
   <VmsServerName>ucbu-aricent-vm413</VmsServerName>
 </Port>
 <Port>
   <URI>/vmrest/ports/761fa322-63ae-47d9-9fbf-b35142b11eef</URI>
   <ObjectId>761fa322-63ae-47d9-9fbf-b35142b11eef</ObjectId>
   <MediaPortGroupObjectId>1edf504a-e9a1-4876-bcfc-bb674da8e385</MediaPortGroupObjectId>
   <PortGroupURI>/vmrest/portgroups/1edf504a-e9a1-4876-bcfc-bb674da8e385</PortGroupURI>
   <TelephonyIntegrationMethodEnum>2</TelephonyIntegrationMethodEnum>
   <VmsServerObjectId>574ca5d3-9041-4ff9-8e7d-727c32d80dab</VmsServerObjectId>
   <DisplayName>PhoneSystem-1-002</DisplayName>
   <CapAnswer>true</CapAnswer>
<CapNotification>true</CapNotification>
   <CapMWI>true</CapMWI>
   <CapEnabled>true</CapEnabled>
   <CapTrapConnection>true</CapTrapConnection>
   <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
   <MediaSwitchObjectId>a8eb65f5-795b-41cd-98b1-934f6b987313</MediaSwitchObjectId>
   <PhoneSystemURI>/vmrest/phonesystems/a8eb65f5-795b-41cd-98b1-934f6b987313</PhoneSystemURI>
   <MediaPortGroupDisplayName>PhoneSystem-1</MediaPortGroupDisplayName>
   <VmsServerName>ucbu-aricent-vm413</VmsServerName>
 </Port> |
|---|

| Response Code: 200 |
|---|

| <Port>
  <URI>/vmrest/ports/e4a48f12-d22b-438c-89eb-0b25f2f73d12</URI>
  <ObjectId>e4a48f12-d22b-438c-89eb-0b25f2f73d12</ObjectId>
  <MediaPortGroupObjectId>668e5869-7c16-48d6-8858-cd0e00fdd47c</MediaPortGroupObjectId>
  <PortGroupURI>/vmrest/portgroups/668e5869-7c16-48d6-8858-cd0e00fdd47c</PortGroupURI>
  <TelephonyIntegrationMethodEnum>2</TelephonyIntegrationMethodEnum>
  <VmsServerObjectId>d190d99e-e9e8-4d63-8c6c-9aca4956afff</VmsServerObjectId>
  <DisplayName>PhoneSystem-1-002</DisplayName>
  <CapAnswer>true</CapAnswer>
  <CapNotification>false</CapNotification>
  <CapMWI>true</CapMWI>
  <CapEnabled>true</CapEnabled>
  <CapTrapConnection>true</CapTrapConnection>
  <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
  <MediaSwitchObjectId>0d15753c-e1b4-4865-b00b-999a1ccf56ce</MediaSwitchObjectId>
  <PhoneSystemURI>/vmrest/phonesystems/0d15753c-e1b4-4865-b00b-999a1ccf56ce</PhoneSystemURI>
  <MediaPortGroupDisplayName>PhoneSystem-1</MediaPortGroupDisplayName>
  <VmsServerName>ucbu-aricent-vm413</VmsServerName>
</Port> |
|---|

| https://<connection_server>/vmrest/vmsservers |
|---|

| <VmsServers total="1">
 <VmsServer>
   <URI>/vmrest/vmsservers/574ca5d3-9041-4ff9-8e7d-727c32d80dab</URI>
   <ServerName>ucbu-aricent-vm413</ServerName>
   <VmsServerObjectId>574ca5d3-9041-4ff9-8e7d-727c32d80dab</VmsServerObjectId>
 </VmsServer>
</VmsServers> |
|---|

| Note | Make sure that you always add ports in even number and not in odd number. |
|---|---|

| https:/<server_ip>/vmrest/ports |
|---|

| <Port>   
   <MediaPortGroupObjectId>3c011243-e3e2-42f7-b658-d9fbdc966f26</MediaPortGroupObjectId>       
   <VmsServerObjectId>574ca5d3-9041-4ff9-8e7d-727c32d80dab</VmsServerObjectId>
   <HuntOrder>0</HuntOrder>
   <CapAnswer>true</CapAnswer>
   <CapNotification>true</CapNotification>    
   <NumberOfPorts>10</NumberOfPorts>
   <CapEnabled>true</CapEnabled>
   <CapTrapConnection>true</CapTrapConnection>   
   <VmsServerName>ucbu-aricent-vm413</VmsServerName>
</Port> |
|---|

| RESPONSE Code: 201 |
|---|

| https:/<server_ip>/vmrest/ports |
|---|

| <Port>   
   <MediaPortGroupObjectId>575f43be-f5d0-4af7-a689-06d968227ff7</MediaPortGroupObjectId>      <VmsServerObjectId>574ca5d3-9041-4ff9-8e7d-727c32d80dab</VmsServerObjectId>
   <HuntOrder>0</HuntOrder>
   <DisplayName>PhoneSystem-Rohit-001</DisplayName>
   <CapAnswer>true</CapAnswer>
   <CapNotification>true</CapNotification>    
   <NumberOfPorts>4</NumberOfPorts>
   <CapEnabled>true</CapEnabled>
   <CapTrapConnection>true</CapTrapConnection>   
   <VmsServerName>ucbu-aricent-vm413</VmsServerName>
</Port> |
|---|

| RESPONSE Code: 201 |
|---|

| https:/<server_ip>/vmrest/ports |
|---|

| <Port> 
  <MediaPortGroupObjectId>2c24f5a9-fb22-47fe-a74b-da9c72d6e7f3</MediaPortGroupObjectId>
  <HuntOrder>0</HuntOrder>
  <DisplayName>PhoneSystem-Rohit-002</DisplayName>
  <CapAnswer>true</CapAnswer>
  <CapNotification>true</CapNotification> 
  <NumberOfPorts>2</NumberOfPorts>
  <CapEnabled>true</CapEnabled>
  <CapTrapConnection>true</CapTrapConnection> 
</Port> |
|---|

| RESPONSE Code: 201 |
|---|

| https://<connection_server>/vmrest/ports/<sccpobjectId> |
|---|

| <Port>   
 <CapAnswer>true</CapAnswer>
 <CapNotification>true</CapNotification>
 <CapMWI>true</CapMWI>
 <CapTrapConnection>true</CapTrapConnection>
<HuntOrder>0</HuntOrder>
<SkinnySecurityModeEnum>0</SkinnySecurityModeEnum>
<CapEnabled>true</CapEnabled>
</Port> |
|---|

| RESPONSE Code: 204 |
|---|

| https://<connection_server>/vmrest/ports/<sipobjectId> |
|---|

| <Port>   
 <CapAnswer>true</CapAnswer>
 <CapNotification>true</CapNotification>
 <CapMWI>true</CapMWI>
 <CapTrapConnection>true</CapTrapConnection>
 <HuntOrder>0</HuntOrder>
 <SkinnySecurityModeEnum>0</SkinnySecurityModeEnum>
 <CapEnabled>true</CapEnabled>
</Port> |
|---|

| RESPONSE Code: 204 |
|---|

| https://<connection_server>/vmrest/ports/<objectId> |
|---|

| RESPONSE Code: 204 |
|---|

| https://<connection_server>/vmrest/sipcertificates |
|---|

| <SipCertificates total="1">
<SipCertificate>
 <URI>
  /vmrest/sipcertificates/c55ef2c3-2475-4505-9566-bcea04a6bb6e
 </URI>
 <ObjectId>c55ef2c3-2475-4505-9566-bcea04a6bb6e</ObjectId>
 <Certificate>
 -----BEGIN CERTIFICATE----- MIICVzCCAcCgAwIBAgIQQmAlZbMuRhSQnNHI4sqpDjANBgkqhkiG9w0BAQUFADA6  MTgwNgYDVQQDEy9DaXNjb1VuaXR5LWJlMjc5NzZjLTZlNmUtNDE5Zi04NTNkLWIz NzY0ODgxZGZiMDAeFw0xMjA3MTgxMzE1MTdaFw0xOTA3MTAwOTAwNThaMDsxGzAZ BgNVBAoTEkNpc2NvIFN5c3RlbXMgSW5jLjEOMAwGA1UECxMFRUNTQlUxDDAKBgNV BAMTA2FhYTCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAwslps1QPmb/mtfSD mHQ8tdnAPcIWriAqF283p7eQcGKdj9ji+YpDGmMFbaKG5NyPBzVCA2EXgNSrh2tX 8PTTUDUOlfGeqrol0H3kT1viFPxNIVVfnn6fuq4A8thoH54+QGlnOWqfuR6+Y4EZ yT4yhygh5yhRIDW6PTHCyhUnMuUCAwEAAaNdMFswHQYDVR0OBBYEFJ2AaJ5nN36z W6BaE5jVTEmAj54/MAsGA1UdDwQEAwIDqDAdBgNVHSUEFjAUBggrBgEFBQcDAQYI KwYBBQUHAwIwDgYDVR0RBAcwBYYDYWFhMA0GCSqGSIb3DQEBBQUAA4GBAJffZqLV 7pmQ+1HEBUO3dVnNdDr7V6izeh3KgoUHW7cEzUuM5wjsRLV7Mh8H9YvGyQP2sMMc iDRpJp4oNpnXZtwd8WEQcToaXvDOR9TfMr5tX9NdkAQGvb8pvt3kPd5cv3s79/Zy DRhjKYIr7A0dKZEpNAFUhTTHbTeNQiOibaGF -----END  CERTIFICATE-----
 </Certificate>

 <PrivateKey>
USkzHb9O2SAH6sofOA1sM91H+Whkpxl+/Sit7MF4+IfPE7u1shotouuFFO9lT11ouADtbjYp2WsqzndpjPRUZ5I4na9nc4uBqLkrQQ6FZ9r2POBgX5EkoA4l5oYUNhJyNIbdqND54Kn1iO6uIKV/NIngQBSGWM0i2Yh+HezEjP2TY9orxD0v6MHtBTsmZvcbWScwpzIAVE6dP2/OeI2+21zG82m+xLmJnfuyiZc/RcmZ2MqOqQYL3IV9Gmo8l09ocQhst2TYBCEsvI6+hId5YujfO1iyL//1rr8GD7lQVBzicFPChR0rqUnGzlilrIpnEEbenUs2HpLw/F+lg1awgGRwe3S5moYClBEor1b5g8UIPXAi0QJNF0PPm4P+ImLCfERghinxz/DSiuE5IVkwfdPUPzPknZt+4SjcX0/VU0zIg42lZ5Xl7rJRonA8a2bnFQkg9Vm8D/TTqrzAy+tdawOGdlnuAN+Hoov1prRZnR5zjkpJaImK3zE0WZyqJsyEQdVaMZEK0irb/fePw5nujRxNJi0eF/AsyDkKEazz5YrjDBZ8QuYAFOr1k9IJI0J8ZkU8krRRQCztWdY63k89XqCRzkN0SxEwu39UDajCbFOq7dbDmkalvKfp6lcrRMZy0OtpB3XgzbBvdAb6H3YZquQdCrdtwSKb/VovNssqqgWXbeocqf0vv2SSbJC+tdJIbZlDOMt7x/glz6z0GabyGb6w8SjYGN0xSUZ+ioVlmhZ8qMOZ33fwW87ctXaRo68jBDcQJHHI2aeYDABMTe3MoMI0R5A4pWUkNWGCjWhyq52kXvY8mjIRhYCEkDxEsvd6l+XRm2A02PCPpX01eeXZ5neZ30jApWkdEzfcQfV57DtEtn8NXv3GCiL59qjiABuAA0aHtUmA36m6mfuh8QWqMRRoZHI5eXUUNjeTt3kyV4jINutEu8dVAujShai/e+wNEulE4clWjh6LaoHjjjfg3MR28f0/bbv2yTPRyy/z5zW4/7z8QwKDh20fnLsLt7VatD1HcKjV2sXB50DBkLz4izVrmkLebLaIUs5pYorAVGf7MpPgVkqcbaE+A4qxpllnl2eQuQGe6a9IioFaY0UVmN3SCBke6lCDqB5qhWkqTOlJGHwV6LBz2hTnjhd62CP8668clvL3YZsC6tdA7CxJPpQZ0b36iS6CclJge2mLVa+CQNnBK68HCP+9y0YddGewEiK+8+D+x6fZC7ng+SYn2iQYHYm9BP7nYdP0YWy/aMy/ga39oHRSyjWv8GfsQNcdFdgEUMCxVx+fUK0Ao8tQKiamJjm8xyCM27UK0RBvy98=
 </PrivateKey>
 <SubjectName>test</SubjectName>
 <DisplayName>test</DisplayName>
</SipCertificate>
</SipCertificates> |
|---|

| Response code: 200 |
|---|

| https://<connection_server>/vmrest/sipcertificate/<objectId> |
|---|

| <SipCertificate>
 <URI>
  /vmrest/sipcertificates/c55ef2c3-2475-4505-9566-bcea04a6bb6e
 </URI>
 <ObjectId>c55ef2c3-2475-4505-9566-bcea04a6bb6e</ObjectId>
 <Certificate>
 -----BEGIN CERTIFICATE----- MIICVzCCAcCgAwIBAgIQQmAlZbMuRhSQnNHI4sqpDjANBgkqhkiG9w0BAQUFADA6 MTgwNgYDVQQDEy9DaXNjb1VuaXR5LWJlMjc5NzZjLTZlNmUtNDE5Zi04NTNkLWIz NzY0ODgxZGZiMDAeFw0xMjA3MTgxMzE1MTdaFw0xOTA3MTAwOTAwNThaMDsxGzAZ BgNVBAoTEkNpc2NvIFN5c3RlbXMgSW5jLjEOMAwGA1UECxMFRUNTQlUxDDAKBgNV BAMTA2FhYTCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAwslps1QPmb/mtfSD mHQ8tdnAPcIWriAqF283p7eQcGKdj9ji+YpDGmMFbaKG5NyPBzVCA2EXgNSrh2tX 8PTTUDUOlfGeqrol0H3kT1viFPxNIVVfnn6fuq4A8thoH54+QGlnOWqfuR6+Y4EZ yT4yhygh5yhRIDW6PTHCyhUnMuUCAwEAAaNdMFswHQYDVR0OBBYEFJ2AaJ5nN36z W6BaE5jVTEmAj54/MAsGA1UdDwQEAwIDqDAdBgNVHSUEFjAUBggrBgEFBQcDAQYI KwYBBQUHAwIwDgYDVR0RBAcwBYYDYWFhMA0GCSqGSIb3DQEBBQUAA4GBAJffZqLV 7pmQ+1HEBUO3dVnNdDr7V6izeh3KgoUHW7cEzUuM5wjsRLV7Mh8H9YvGyQP2sMMc iDRpJp4oNpnXZtwd8WEQcToaXvDOR9TfMr5tX9NdkAQGvb8pvt3kPd5cv3s79/Zy DRhjKYIr7A0dKZEpNAFUhTTHbTeNQiOibaGF -----END CERTIFICATE-----
 </Certificate>
 <PrivateKey>
USkzHb9O2SAH6sofOA1sM91H+Whkpxl+/Sit7MF4+IfPE7u1shotouuFFO9lT11ouADtbjYp2WsqzndpjPRUZ5I4na9nc4uBqLkrQQ6FZ9r2POBgX5EkoA4l5oYUNhJyNIbdqND54Kn1iO6uIKV/NIngQBSGWM0i2Yh+HezEjP2TY9orxD0v6MHtBTsmZvcbWScwpzIAVE6dP2/OeI2+21zG82m+xLmJnfuyiZc/RcmZ2MqOqQYL3IV9Gmo8l09ocQhst2TYBCEsvI6+hId5YujfO1iyL//1rr8GD7lQVBzicFPChR0rqUnGzlilrIpnEEbenUs2HpLw/F+lg1awgGRwe3S5moYClBEor1b5g8UIPXAi0QJNF0PPm4P+ImLCfERghinxz/DSiuE5IVkwfdPUPzPknZt+4SjcX0/VU0zIg42lZ5Xl7rJRonA8a2bnFQkg9Vm8D/TTqrzAy+tdawOGdlnuAN+Hoov1prRZnR5zjkpJaImK3zE0WZyqJsyEQdVaMZEK0irb/fePw5nujRxNJi0eF/AsyDkKEazz5YrjDBZ8QuYAFOr1k9IJI0J8ZkU8krRRQCztWdY63k89XqCRzkN0SxEwu39UDajCbFOq7dbDmkalvKfp6lcrRMZy0OtpB3XgzbBvdAb6H3YZquQdCrdtwSKb/VovNssqqgWXbeocqf0vv2SSbJC+tdJIbZlDOMt7x/glz6z0GabyGb6w8SjYGN0xSUZ+ioVlmhZ8qMOZ33fwW87ctXaRo68jBDcQJHHI2aeYDABMTe3MoMI0R5A4pWUkNWGCjWhyq52kXvY8mjIRhYCEkDxEsvd6l+XRm2A02PCPpX01eeXZ5neZ30jApWkdEzfcQfV57DtEtn8NXv3GCiL59qjiABuAA0aHtUmA36m6mfuh8QWqMRRoZHI5eXUUNjeTt3kyV4jINutEu8dVAujShai/e+wNEulE4clWjh6LaoHjjjfg3MR28f0/bbv2yTPRyy/z5zW4/7z8QwKDh20fnLsLt7VatD1HcKjV2sXB50DBkLz4izVrmkLebLaIUs5pYorAVGf7MpPgVkqcbaE+A4qxpllnl2eQuQGe6a9IioFaY0UVmN3SCBke6lCDqB5qhWkqTOlJGHwV6LBz2hTnjhd62CP8668clvL3YZsC6tdA7CxJPpQZ0b36iS6CclJge2mLVa+CQNnBK68HCP+9y0YddGewEiK+8+D+x6fZC7ng+SYn2iQYHYm9BP7nYdP0YWy/aMy/ga39oHRSyjWv8GfsQNcdFdgEUMCxVx+fUK0Ao8tQKiamJjm8xyCM27UK0RBvy98=
 </PrivateKey>
 <SubjectName>test</SubjectName>
 <DisplayName>test</DisplayName>
</SipCertificate> |
|---|

| Response code: 200 |
|---|

| https://<connection_server>/vmrest/ sipcertificates/<objectid> |
|---|

| <SipCertificate>
 <SubjectName>test2</SubjectName>
 <DisplayName>test2</DisplayName>
</SipCertificate> |
|---|

| Response code: 204 |
|---|

| https://<connection_server>/vmrest/sipcertificates/<objectId> |
|---|

| Response code: 204 |
|---|

| https:/<server_ip>/vmrest/sipsecurityprofiles |
|---|

| <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<SipSecurityProfiles total="2"><SipSecurityProfile>
 <URI>/vmrest/sipsecurityprofiles/87cab9a5-c68d-447a-ab4f-7cd2837aa240</URI>
 <ObjectId>87cab9a5-c68d-447a-ab4f-7cd2837aa240</ObjectId><Port>5069</Port>
 <DoTLS>false</DoTLS><DisplayName>5069</DisplayName>
 </SipSecurityProfile><SipSecurityProfile>
 <URI>/vmrest/sipsecurityprofiles/4d7e055a-cdcf-43ff-a922-4ce743939a23</URI>
 <ObjectId>4d7e055a-cdcf-43ff-a922-4ce743939a23</ObjectId><Port>5066</Port>
 <DoTLS>true</DoTLS><DisplayName>5066/TLS</DisplayName>
</SipSecurityProfile></SipSecurityProfiles>

<Pre> RESPONSE Code: 200 |
|---|

| https://<connection_server>/vmrest/sipsecurityprofiles/<objectId> |
|---|

| <SipSecurityProfile>
 <URI>/vmrest/sipsecurityprofiles/87cab9a5-c68d-447a-ab4f-7cd2837aa240</URI>
 <ObjectId>87cab9a5-c68d-447a-ab4f-7cd2837aa240</ObjectId><Port>5069</Port>
 <DoTLS>false</DoTLS><DisplayName>5069</DisplayName>
</SipSecurityProfile><SipSecurityProfile>

<pre> Response code: 200 |
|---|

| https:/<connection_server>/vmrest/sipsecurityprofiles |
|---|

| {
  "@total": "6",
  "SipSecurityProfile":    
  {
    "URI": "/vmrest/sipsecurityprofiles/08aef04e-8775-4ea5-916b-f7e36cbdb3d4",
    "ObjectId": "08aef04e-8775-4ea5-916b-f7e36cbdb3d4",
    "Port": "5065",
    "DoTLS": "true",
    "DisplayName": "5065/TLS"
  },
  {
    "URI": "/vmrest/sipsecurityprofiles/b3c533a4-bc28-4c70-9912-c22edf81910e",
    "ObjectId": "b3c533a4-bc28-4c70-9912-c22edf81910e",
    "Port": "5062",
    "DoTLS": "true",
    "DisplayName": "5062/TLS"
   },
   {
     "URI": "/vmrest/sipsecurityprofiles/e667342c-3ce2-49f7-ae2b-27daf850b159",
     "ObjectId": "e667342c-3ce2-49f7-ae2b-27daf850b159",
     "Port": "5088",
     "DoTLS": "true",
     "DisplayName": "5088/TLS"
   },
   {
     "URI": "/vmrest/sipsecurityprofiles/9062519a-05d4-42f2-933e-250d5a24efb5",
     "ObjectId": "9062519a-05d4-42f2-933e-250d5a24efb5",
     "Port": "5067",
     "DoTLS": "false",
     "DisplayName": "5067"
   },
   {
     "URI": "/vmrest/sipsecurityprofiles/9adbf7ac-c882-4ad1-84d5-d67d56d44d6d",
     "ObjectId": "9adbf7ac-c882-4ad1-84d5-d67d56d44d6d",
     "Port": "5077",
     "DoTLS": "false",
     "DisplayName": "5077"
   },
   {
     "URI": "/vmrest/sipsecurityprofiles/15a3a4d9-65a0-456a-be38-4a4aff36554c",
     "ObjectId": "15a3a4d9-65a0-456a-be38-4a4aff36554c",
     "Port": "5060",
     "DoTLS": "false",
     "DisplayName": "5060"
   }
   
}

<pre> RESPONSE Code: 200 |
|---|

| https://<connection_server>/vmrest/sipsecurityprofiles/<objectId> |
|---|

| {
   "URI": "/vmrest/sipsecurityprofiles/9adbf7ac-c882-4ad1-84d5-d67d56d44d6d",
   "ObjectId": "9adbf7ac-c882-4ad1-84d5-d67d56d44d6d",
   "Port": "5077",
   "DoTLS": "false",
   "DisplayName": "5077"
} |
|---|

| RESPONSE Code: 200 |
|---|

| https://<connection_server>/vmrest/sipsecurityprofiles |
|---|

| <SipSecurityProfile>
 <Port>5070</Port>
 <DoTLS>true</DoTLS>
</SipSecurityProfile> |
|---|

| Response code: 201 |
|---|

| https://<connection_server>/vmrest/sipsecurityprofiles |
|---|

| {
   "Port": "5080",
   "DoTLS": "true"
} |
|---|

| Response code: 201 |
|---|

| https://<connection_server>/vmrest/sipsecurityprofiles/<objectId> |
|---|

| <SipSecurityProfile>
 <Port>5070</Port>
 <DoTLS>true</DoTLS>
 </SipSecurityProfile> |
|---|

| Response code: 204 |
|---|

| https://<connection_server>/vmrest/sipsecurityprofiles/<objectId> |
|---|

| {
   "Port": "5077",
   "DoTLS": "true"
} |
|---|

| Response code: 204 |
|---|

| https://<server-ip>/vmrest/ sipsecurityprofiles/<objectId> |
|---|

| Response Code: 204 |
|---|