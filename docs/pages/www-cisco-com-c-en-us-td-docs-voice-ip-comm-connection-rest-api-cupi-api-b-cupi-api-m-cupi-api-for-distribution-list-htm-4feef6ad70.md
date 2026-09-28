---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-api-for-distribution-list-htm-4feef6ad70
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m-cupi-api-for-distribution-list.html
retrieved_at: 2026-08-17T03:49:28.032128+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API for Distribution List

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API for Distribution List

# Cisco Unity Connection Provisioning Interface (CUPI) API for Distribution List

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Distribution List APIs

### Distribution List
                           	 APIs

Administrator can use this API to
                              		create/update/delete/fetch the distribution lists. You can update various
                              		attributes of distribution list using this API. Also members in a distribution
                              		list can be added/deleted/fetched using this API.

#### Listing the
                              	 Distribution Lists

The following is an example of
                                    		  the GET request that fetch the list of distribution list:

```
GET https://<connection-server>/vmrest/distributionlists
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<DistributionLists total="3">
  <DistributionList>
    <URI>/vmrest/distributionlists/24865f76-fa95-412d-bc56-a48ef9e1531a</URI>
    <ObjectId>24865f76-fa95-412d-bc56-a48ef9e1531a</ObjectId>
    <Alias>undeliverablemessages</Alias>
    <DisplayName>Undeliverable Messages</DisplayName>
    <LocationObjectId>bbf3e6ed-0278-479c-9a6e-2da8756eeb6f</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/bbf3e6ed-0278-479c-9a6e-
    2da8756eeb6f</LocationURI>
    <PartitionObjectId>d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b</PartitionObjectId>
    <TenantObjectId>fe6541fb-b42c-44f2-8404-ded14cbf7438</TenantObjectId>
    <PartitionURI>/vmrest/partitions/d50e9d0b-656e-416d-b5b7-
    43c4d2e2fd0b</PartitionURI>
    <DistributionListMembersURI>/vmrest/distributionlists/24865f76-fa95-412d-bc56-
    a48ef9e1531a/distributionlistmembers</DistributionListMembersURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%2
    024865f76-fa95-412d-bc56-a48ef9e1531a)</AlternateNamesURI>
  </DistributionList>
  <DistributionList>
    <URI>/vmrest/distributionlists/f3e492dc-822b-43fb-be2f-416b972fb642</URI>
    <ObjectId>f3e492dc-822b-43fb-be2f-416b972fb642</ObjectId>
    <Alias>allvoicemailusers</Alias>
    <DisplayName>All Voice Mail Users</DisplayName>
    <LocationObjectId>bbf3e6ed-0278-479c-9a6e-2da8756eeb6f</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/bbf3e6ed-0278-479c-9a6e-
    2da8756eeb6f</LocationURI>
    <DtmfAccessId>99991</DtmfAccessId>
    <PartitionObjectId>d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/d50e9d0b-656e-416d-b5b7-
    43c4d2e2fd0b</PartitionURI>
    <DistributionListMembersURI>/vmrest/distributionlists/f3e492dc-822b-43fb-be2f-
    416b972fb642/distributionlistmembers</DistributionListMembersURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%2
    0f3e492dc-822b-43fb-be2f-416b972fb642)</AlternateNamesURI>
  </DistributionList>
  <DistributionList>
    <URI>/vmrest/distributionlists/c34b145e-b1f4-40de-9031-bc83703f0b1c</URI>
    <ObjectId>c34b145e-b1f4-40de-9031-bc83703f0b1c</ObjectId>
    <Alias>allvoicemailenabledcontacts</Alias>
    <DisplayName>All Voicemail-Enabled Contacts</DisplayName>
    <LocationObjectId>bbf3e6ed-0278-479c-9a6e-2da8756eeb6f</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/bbf3e6ed-0278-479c-9a6e-
    2da8756eeb6f</LocationURI>
    <DtmfAccessId>99992</DtmfAccessId>
    <PartitionObjectId>d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/d50e9d0b-656e-416d-b5b7-
    43c4d2e2fd0b</PartitionURI>
    <DistributionListMembersURI>/vmrest/distributionlists/c34b145e-b1f4-40de-9031-
    bc83703f0b1c/distributionlistmembers</DistributionListMembersURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%20c34b145e-b1f4-40de-9031-bc83703f0b1c)</AlternateNamesURI>
  </DistributionList>
  </DistributionLists>
```

```
Response Code: 204
```

JSON Example

To get distribution lists, do the following:

```
Request URI:
GET https://<connection-server>/vmrest/distributionlists
Accept: application /json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
  "@total":"2"
  "DistributionList":[
{
    "URI":"/vmrest/distributionlists/d9e61ace-3ece-4722-b331-ed57a73ef9eb"
    "ObjectId":"d9e61ace-3ece-4722-b331-ed57a73ef9eb"
    "Alias":"undeliverablemessages"
    "DisplayName":"Undeliverable Messages"
    "LocationObjectId":"830e1a2d-8e90-459f-88f7-700497ba975c"
    "LocationURI":"/vmrest/locations/connectionlocations/830e1a2d-8e90-459f-88f7-700497ba975c"
    "PartitionObjectId":"9c010254-1493-4e1a-9e47-fe2494792744"
    "TenantObjectId":"fe6541fb-b42c-44f2-8404-ded14cbf7438"
    "PartitionURI":"/vmrest/partitions/9c010254-1493-4e1a-9e47-fe2494792744"
    "DistributionListMembersURI":"/vmrest/distributionlists/d9e61ace-3ece-4722-b331-ed57a73ef9eb/distributionlistmembers"
    "AlternateNamesURI":"/vmrest/alternatenames?query=(DistributionListObjectId%20is%20d9e61ace-3ece-4722-b331-ed57a73ef9eb)"
}
{
    "URI":"/vmrest/distributionlists/a1fcfd8b-8749-465b-abe1-b578a8565107"
    "ObjectId":"a1fcfd8b-8749-465b-abe1-b578a8565107"
    "Alias":"allvoicemailusers"
    "DisplayName":"All Voice Mail Users"
    "LocationObjectId":"830e1a2d-8e90-459f-88f7-700497ba975c"
    "LocationURI":"/vmrest/locations/connectionlocations/830e1a2d-8e90-459f-88f7-700497ba975c"
    "DtmfAccessId":"99991"
    "PartitionObjectId":"9c010254-1493-4e1a-9e47-fe2494792744"
    "PartitionURI":"/vmrest/partitions/9c010254-1493-4e1a-9e47-fe2494792744"
    "DistributionListMembersURI":"/vmrest/distributionlists/a1fcfd8b-8749-465b-abe1-b578a8565107/distributionlistmembers"
    "AlternateNamesURI":"/vmrest/alternatenames?query=(DistributionListObjectId%20is%20a1fcfd8b-8749-465b-abe1-b578a8565107)"
}
]
}
```

```
Response Code: 200
```

##### Listing Specific
                                 	 Tenant Related Distribution Lists by System Administrator

In Cisco Unity Connection 10.5(2)
                                       		  and later, the system administrator can use TenantObjectID to list the specific
                                       		  tenant related distribution lists using the following URI:

```
GET https://<connection-server>/vmrest/distributionlists?query=(TenantObjectId is <Tenant-ObjectId>)
```

To get the TenantObjectID, use the following URI:

```
GET https://<connection-server>/vmrest/tenants
```

#### Viewing the
                              	 Specific Distribution List

The following is an example of
                                    		  the GET request that lists the details of specific distribution list
                                    		  represented by the provided value of distribution list object ID:

```
GET https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId>
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<DistributionList>
    <URI>/vmrest/distributionlists/c34b145e-b1f4-40de-9031-bc83703f0b1c</URI>
    <ObjectId>c34b145e-b1f4-40de-9031-bc83703f0b1c</ObjectId>
    <Alias>allvoicemailenabledcontacts</Alias>
    <CreationTime>2013-02-14T05:05:42Z</CreationTime>
    <DisplayName>All Voicemail-Enabled Contacts</DisplayName>
    <DtmfName>2558642362453622</DtmfName>
    <IsPublic>true</IsPublic>
    <Undeletable>true</Undeletable>
    <VoiceName>d5814a39-94df-4498-acfd-93728a607be7.wav</VoiceName>
    <VoiceFileURI>/vmrest/voicefiles/d5814a39-94df-4498-acfd-93728a607be7.wav</VoiceFileURI>
    <VoiceNameURI>/vmrest/distributionlists/c34b145e-b1f4-40de-9031-
    bc83703f0b1c/voicename</VoiceNameURI>
    <LocationObjectId>bbf3e6ed-0278-479c-9a6e-2da8756eeb6f</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/bbf3e6ed-0278-479c-9a6e-
    2da8756eeb6f</LocationURI>
    <DtmfAccessId>99992</DtmfAccessId>
    <AllowContacts>true</AllowContacts>
    <AllowForeignMessage>false</AllowForeignMessage>
    <PartitionObjectId>d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b</PartitionURI>
    <DistributionListMembersURI>/vmrest/distributionlists/c34b145e-b1f4-40de-9031-
    bc83703f0b1c/distributionlistmembers</DistributionListMembersURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%20c34b14
    5e-b1f4-40de-9031-bc83703f0b1c)</AlternateNamesURI>
</DistributionList>
```

```
Response Code: 200
```

JSON Example

To get a distribution list for a particular partitions, do the
                                    		  following:

```
Request URI:
GET https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId>
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
    "URI":"/vmrest/distributionlists/d9e61ace-3ece-4722-b331-ed57a73ef9eb"
    "ObjectId":"d9e61ace-3ece-4722-b331-ed57a73ef9eb"
    "Alias":"undeliverablemessages"
    "CreationTime":"2013-02-21T11:39:08Z"
    "DisplayName":"Undeliverable Messages"
    "DtmfName":"8633548372253637"
    "IsPublic":"true"
    "Undeletable":"true"
    "VoiceName":"487e3db3-3782-4d30-a000-ef0d03ae22a2.wav"
    "VoiceFileURI":"/vmrest/voicefiles/487e3db3-3782-4d30-a000-ef0d03ae22a2.wav"
    "VoiceNameURI":"/vmrest/distributionlists/d9e61ace-3ece-4722-b331-
    ed57a73ef9eb/voicename"
    "LocationObjectId":"830e1a2d-8e90-459f-88f7-700497ba975c"
    "LocationURI":"/vmrest/locations/connectionlocations/830e1a2d-8e90-459f-88f7-
    700497ba975c"
    "AllowContacts":"false"
    "AllowForeignMessage":"false"
    "PartitionObjectId":"9c010254-1493-4e1a-9e47-fe2494792744"
    "PartitionURI":"/vmrest/partitions/9c010254-1493-4e1a-9e47-fe2494792744"
    "DistributionListMembersURI":"/vmrest/distributionlists/d9e61ace-3ece-4722-b331-
    ed57a73ef9eb/distributionlistmembers"
    "AlternateNamesURI":"/vmrest/alternatenames?query=(DistributionListObjectId%20is%20d9e61
    ace-3ece-4722-b331-ed57a73ef9eb)"
}
```

```
Response Code: 200
```

#### Getting the
                              	 Distribution List Based on an Query

The following is an example of
                                    		  the GET request that lists the details of specific distribution list
                                    		  represented by the provided value of partition object ID:

```
GET https://<connection-
  server>/vmrest/distributionlists?query=(PartitionObjectId%20is%20<objectId of the partition>)
```

Where the partition object Id can be fetched using the following
                                    		  request

```
GET https://<connection-server>/vmrest/partitions
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<DistributionLists total="3">
  <DistributionList>
     <URI>/vmrest/distributionlists/2fe64511-1b69-4d97-b27b-ef383af4b194</URI>
     <ObjectId>2fe64511-1b69-4d97-b27b-ef383af4b194</ObjectId>
     <Alias>undeliverablemessages</Alias>
     <DisplayName>Undeliverable Messages</DisplayName>
     <LocationObjectId>42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationObjectId>
     <LocationURI>/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-
     8ddce4f430ff</LocationURI>
     <PartitionObjectId>da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionObjectId>
     <PartitionURI>/vmrest/partitions/da2114bf-cde7-43d8-9709-
     cd3895a9d41b</PartitionURI>
     <DistributionListMembersURI>/vmrest/distributionlists/2fe64511-1b69-4d97-b27b-
     ef383af4b194/distributionlistmembers</DistributionListMembersURI>
     <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%2
     02fe64511-1b69-4d97-b27b-ef383af4b194)</AlternateNamesURI>
  </DistributionList>
  <DistributionList>
    <URI>/vmrest/distributionlists/d37dfc67-04c2-48d3-9a7a-f2b316a09840</URI>
    <ObjectId>d37dfc67-04c2-48d3-9a7a-f2b316a09840</ObjectId>
    <Alias>allvoicemailusers</Alias>
    <DisplayName>All Voice Mail Users</DisplayName>
    <LocationObjectId>42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-
    8ddce4f430ff</LocationURI>
    <DtmfAccessId>99991</DtmfAccessId>
    <PartitionObjectId>da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/da2114bf-cde7-43d8-9709-
    cd3895a9d41b</PartitionURI>
    <DistributionListMembersURI>/vmrest/distributionlists/d37dfc67-04c2-48d3-9a7a-
    f2b316a09840/distributionlistmembers</DistributionListMembersURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%2
    0d37dfc67-04c2-48d3-9a7a-f2b316a09840)</AlternateNamesURI>
  </DistributionList>
  <DistributionList>
    <URI>/vmrest/distributionlists/160da8fe-2171-4bf7-9009-e95db94f823e</URI>
    <ObjectId>160da8fe-2171-4bf7-9009-e95db94f823e</ObjectId>
    <Alias>allvoicemailenabledcontacts</Alias>
    <DisplayName>All Voicemail-Enabled Contacts</DisplayName>
    <LocationObjectId>42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-
    8ddce4f430ff</LocationURI>
    <DtmfAccessId>99992</DtmfAccessId>
    <PartitionObjectId>da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/da2114bf-cde7-43d8-9709-
    cd3895a9d41b</PartitionURI>
    <DistributionListMembersURI>/vmrest/distributionlists/160da8fe-2171-4bf7-9009-
    e95db94f823e/distributionlistmembers</DistributionListMembersURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%2
    0160da8fe-2171-4bf7-9009-e95db94f823e)</AlternateNamesURI>
  </DistributionList>
  </DistributionLists>
```

```
Response Code: 200
```

JSON Example

To get a particular distribution list, do the following:

```
Request URI:
GET https://<connection-server>/vmrest/distributionlists?query=(PartitionObjectId%20is%20<objectId  of the partition>)
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
  "@total":"3"
  "DistributionList":[
  {
    "URI":"/vmrest/distributionlists/2fe64511-1b69-4d97-b27b-ef383af4b194"
    "ObjectId":"2fe64511-1b69-4d97-b27b-ef383af4b194"
    "Alias":"undeliverablemessages"
    "DisplayName":"Undeliverable Messages"
    "LocationObjectId":"42a9ab40-490d-4819-9bfb-8ddce4f430ff"
    "LocationURI":"/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-
    8ddce4f430ff"
    "PartitionObjectId":"da2114bf-cde7-43d8-9709-cd3895a9d41b"
    "PartitionURI":"/vmrest/partitions/da2114bf-cde7-43d8-9709-cd3895a9d41b"
    "DistributionListMembersURI":"/vmrest/distributionlists/2fe64511-1b69-4d97-b27b-
    ef383af4b194/distributionlistmembers"
    "AlternateNamesURI":"/vmrest/alternatenames?query=(DistributionListObjectId%20is%20
    2fe64511-1b69-4d97-b27b-ef383af4b194)"
  }
  {
    "URI":"/vmrest/distributionlists/d37dfc67-04c2-48d3-9a7a-f2b316a09840"
    "ObjectId":"d37dfc67-04c2-48d3-9a7a-f2b316a09840"
    "Alias":"allvoicemailusers"
    "DisplayName":"All Voice Mail Users"
    "LocationObjectId":"42a9ab40-490d-4819-9bfb-8ddce4f430ff"
    "LocationURI":"/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-
    8ddce4f430ff"
    "DtmfAccessId":"99991"
    "PartitionObjectId":"da2114bf-cde7-43d8-9709-cd3895a9d41b"
    "PartitionURI":"/vmrest/partitions/da2114bf-cde7-43d8-9709-cd3895a9d41b"
    "DistributionListMembersURI":"/vmrest/distributionlists/d37dfc67-04c2-48d3-9a7a-
    f2b316a09840/distributionlistmembers"
    "AlternateNamesURI":"/vmrest/alternatenames?query=(DistributionListObjectId%20is%2
    0d37dfc67-04c2-48d3-9a7a-f2b316a09840)"
  }
  {
    "URI":"/vmrest/distributionlists/160da8fe-2171-4bf7-9009-e95db94f823e"
    "ObjectId":"160da8fe-2171-4bf7-9009-e95db94f823e"
    "Alias":"allvoicemailenabledcontacts"
    "DisplayName":"All Voicemail-Enabled Contacts"
    "LocationObjectId":"42a9ab40-490d-4819-9bfb-8ddce4f430ff"
    "LocationURI":"/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-
    8ddce4f430ff"
    "DtmfAccessId":"99992"
    "PartitionObjectId":"da2114bf-cde7-43d8-9709-cd3895a9d41b"
    "PartitionURI":"/vmrest/partitions/da2114bf-cde7-43d8-9709-cd3895a9d41b"
    "DistributionListMembersURI":"/vmrest/distributionlists/160da8fe-2171-4bf7-9009-
    e95db94f823e/distributionlistmembers"
    "AlternateNamesURI":"/vmrest/alternatenames?query=(DistributionListObjectId%20is%2
    0160da8fe-2171-4bf7-9009-e95db94f823e)"
  }
  }
}
```

```
Response Code: 200
```

#### Creating a
                              	 Distribution List

The following is an example of
                                    		  the POST request that creates a new distribution list where the mandatory field
                                    		  is alias:

```
POST https://<connection-server>/vmrest/distributionlists
```

The following is the response from the above *POST* request and the
                                    		  actual response will depend upon the information given by you:

```
Request Body:
<DistributionList>
    <Alias>Texoma_allvoicemailusersDL_1 </Alias>
    <DisplayName>Texoma_allvoicemailusersDL_1</DisplayName>
</DistributionList>
```

The following is the response from the above *POST* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 201
/vmrest/distributionlists/3049a03c-108d-40aa-a989-0b008f07656c
```

JSON Example

To create distribution list, do the following:

```
Request URI:
POST https://<connection-server>/vmrest/distributionlists
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "Alias":"Texoma1"
    "DisplayName": "Texoma 1"
}
```

The following is the response from the above *POST* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 201
/vmrest/distributionlists/dd043e9a-3f34-47eb-a72a-1b4b41e5f9d7
```

#### Delete the
                              	 Distribution List

This request can be used to
                                    		  delete a distribution list.

```
DELETE: https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId>
```

The following is the response from the above *DELETE* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To delete a distribution list, do the following:

```
DELETE https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId>
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *DELETE* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

#### Updating the
                              	 Distribution List

The following is an example of
                                    		  the PUT request that can be used to update the distribution list by replicating
                                    		  remote sites over inter-site links, adding contacts in distribution list, and
                                    		  accepting messages from foreign systems.

```
PUT https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId>
```

Example 1: Replicate to remote sites over inter-site links is
                                    		  enabled, disable add contacts in distribution list, and disallow messages from
                                    		  users on remote voice messaging systems that are configured as VPIM locations.

```
Request Body:
<DistributionList>
    <AllowContacts>false</AllowContacts>
    <AllowForeignMessage>false</AllowForeignMessage>
</DistributionList>
```

```
Response Code: 204
```

JSON Example:

```
PUT https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "AllowContacts":"false",
    "AllowForeignMessage":"false"
}
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

Example 2: Replicate to remote sites over inter-site links is
                                    		  disabled, enable add contacts in distribution list, and disallow messages from
                                    		  users on remote voice messaging systems that are configured as VPIM locations.

```
Request Body:
<DistributionList>
    <AllowContacts>true</AllowContacts>
    <AllowForeignMessage>false</AllowForeignMessage>
</DistributionList>
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

```
PUT https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId>
Accept: application/json
Content-Type: application/json
Connection: keep-alive 
Request Body:
{
    "AllowContacts":"false",
    "AllowForeignMessage":"false"
}
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

Example 3: Replicate to remote sites over inter-site links is
                                    		  enabled, enable add contacts in distribution list, and accept messages from
                                    		  users on remote voice messaging systems that are configured as VPIM locations.

```
Request Body:
<DistributionList>
    <AllowContacts>false</AllowContacts>
    <AllowForeignMessage>true</AllowForeignMessage>
</DistributionList>
The following is the response from the above *PUT* request and the actual response will depend upon the information given by you:
Response Code: 204
JSON Example:
Request URI:
PUT https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "AllowContacts":"false",
    "AllowForeignMessage":"true"
}
The following is the response from the above *PUT* request and the actual response will depend upon the information given by you:
Response Code: 204
```

#### Updating the
                              	 Distribution List for Tenant

The following is an example of
                                    		  the PUT request that can be used to update the distribution list for Tenants.

```
PUT https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId>
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Request Body:
<DistributionList>
              <TenantObjectId>fe6541fb-b42c-44f2-8404-ded14cbf7438</TenantObjectId>
</DistributionList>
```

The following is the response from the above *PUT* request:

```
Response Code: 204
```

JSON Example :

```
PUT https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
"TenantObjectId":"fe6541fb-b42c-44f2-8404-ded14cbf7438"
}
```

#### Updating the
                              	 Alternate Names of Distribution Lists

The mandatory fields for creation of an alternate name are FirstName and DistributionListObjectId. The URI to get DistributionListObjectId:
                                    https://<connection server>/vmrest/distributionlists.

Example 1: Adding an alternate name for a distribution list

```
POST https://<connection-server>/vmrest/alternatenames?query=(DistributionListObjectId%20is%20ef4aa84e-97c3-456e-848e-b162a04c9631)  
Request Body:
<AlternateName>
    <FirstName>Taxoma_list1</FirstName>
    <DistributionListObjectId>ef4aa84e-97c3-456e-848e-b162a04c9631</DistributionListObjectId>
</AlternateName>
```

The following is the response from the above *POST* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 201
/vmrest/alternatenames/e091a0f6-031e-440d-abd2-783e5f62511b
```

```
Request URI:
POST https://<connection-
server>/vmrest/alternatenames?query=(DistributionListObjectId%20is%20ef4aa84e-97c3-456e-848e-
b162a04c9631)
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "FirstName":"Taxoma_list1",
    "DistributionListObjectId":"ef4aa84e-97c3-456e-848e-b162a04c9631"
}
```

The following is the response from the above *POST* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 201
/vmrest/alternatenames/e091a0f6-031e-440d-abd2-783e5f62511b
```

```
GET https://<connection-server>/vmrest/ alternatenames?query=(DistributionListObjectId%20is%20ef4aa84e-97c3-456e-848e-b162a04c9631)
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                    by you:

```
<AlternateNames total="2">
  <AlternateName>
    <URI>/vmrest/alternatenames/865615e9-1c00-4121-acf4-36ee00adb09c</URI>
    <FirstName>Texoma_Alternane Name 1</FirstName>
    <ObjectId>865615e9-1c00-4121-acf4-36ee00adb09c</ObjectId>
    <DistributionListObjectId>e703511f-fa9b-41f2-8662-
    23de75fffc96</DistributionListObjectId>
    <DistributionListURI>/vmrest/distributionlists/e703511f-fa9b-41f2-8662-
    23de75fffc96</DistributionListURI>
  </AlternateName>
  <AlternateName>
    <URI>/vmrest/alternatenames/af735ef8-b3f3-4c97-a8ec-667e416cfde2</URI>
    <FirstName>Texoma_Alternate Name 2</FirstName>
    <ObjectId>af735ef8-b3f3-4c97-a8ec-667e416cfde2</ObjectId>
    <DistributionListObjectId>e703511f-fa9b-41f2-8662-
    23de75fffc96</DistributionListObjectId>
    <DistributionListURI>/vmrest/distributionlists/e703511f-fa9b-41f2-8662-
    23de75fffc96</DistributionListURI>
  </AlternateName>
</AlternateNames>
```

```
Response Code: 200
```

```
GET https://<connection-server>/vmrest/alternatenames?query=(DistributionListObjectId%20is%20c238c2bf-4037-494d-951b-090468c95dc4)
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                    by you:

```
{
  "@total":"1","AlternateName":
  {
    "URI":"/vmrest/alternatenames/e091a0f6-031e-440d-abd2-783e5f62511b",
    "FirstName":"Taxoma_list1",
    "ObjectId":"e091a0f6-031e-440d-abd2-783e5f62511b",
    "DistributionListObjectId":"c238c2bf-4037-494d-951b-090468c95dc4",
    "DistributionListURI":"/vmrest/distributionlists/c238c2bf-4037-494d-951b-
    090468c95dc4"
  }
}
```

```
Response Code: 200
```

Example 3: Deleting an alternate name

```
DELETE https://<connection-server>/vmrest /alternatenames/<AlternateNameObjectId>
```

The following is the response from the above *DELETE* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 204
```

```
DELETE https://<connection-server>/vmrest/alternatenames/<AlternateNameObjectId>
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *DELETE* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 204
```

Example 4: Editing an Alternate Name

Note that only first name is editable.

```
PUT https://<connection-server>/vmrest/alternatenames/<AlternateNameObjectId>
Request Body:
<AlternateName>
    <FirstName>Texoma_Alternane Name1</FirstName>
</AlternateName>
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 204
```

```
PUT https://<connection-server>/vmrest/alternatenames/<AlternateNameObjectId>
Accept: application/json
Connection: keep-alive
Request Body:
{
    "FirstName":"Texoma1"
}
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 204
```

#### Explanation of the
                              	 Data Fields for Distribution List

Possible values:

- true: allow
                                                         						  contacts (system, VPIM,virtual) are allowed to be members of this Distribution
                                                         						  List

- false: Do not
                                                         						  allow contacts (system, VPIM,virtual) are allowed to be members of this
                                                         						  Distribution List

Default: false

Possible Values:

- true: allow
                                                         						  remote voice messaging

- false: Do not
                                                         						  allow remote voice messaging.

Default: False

#### Explanation of
                              	 the Data Fields for Alternate Names of Distribution List

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Distribution List Members
                        	 APIs

### Distribution List
                           	 Members APIs

Administrator can use this API to
                                 		  create/update/delete/fetch the distribution list members. You can update
                                 		  various attributes of distribution list members using this API.

#### Listing the
                              	 Distribution List Members

```
Request URI:
GET https://<connection-
server>/vmrest/distributionlists/<distributionlistObjectId>/distributionlistmember
```

The following is an example of the GET request that fetch the list of
                                    		  distribution list members:

```
GET https://<connection server>/vmrest/distributionlists/ef4aa84e-97c3-456e-848e-
  b162a04c9631/distributionlistmembers
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<DistributionListMembers total="1">
  <DistributionListMember>
    <URI>/vmrest/distributionlists/ef4aa84e-97c3-456e-848e-
  b162a04c9631/distributionlistmembers/f6712058-3409-49eb-a616-517614766594</URI>
    <DistributionListObjectId>ef4aa84e-97c3-456e-848e-
  b162a04c9631</DistributionListObjectId>
    <DistributionListURI>/vmrest/distributionlists/ef4aa84e-97c3-456e-848e-
  b162a04c9631</DistributionListURI>
    <MemberUserObjectId>34cc862e-19e4-4689-a4ee-
  ee98d83b8319</MemberUserObjectId>
    <MemberUserURI>/vmrest/users/34cc862e-19e4-4689-a4ee-
  ee98d83b8319</MemberUserURI>
    <ObjectId>f6712058-3409-49eb-a616-517614766594</ObjectId>
    <Alias>Texoma_UserTemplate_1</Alias>
    <DisplayName>Texoma_UserTemplate_1</DisplayName>
    <AllowForeignMessage>false</AllowForeignMessage>
    <MemberGlobalUserObjectId>34cc862e-19e4-4689-a4ee-
  ee98d83b8319</MemberGlobalUserObjectId>
    <MemberGlobalUserURI>/vmrest/globalusers/34cc862e-19e4-4689-a4ee-
  ee98d83b8319</MemberGlobalUserURI>
    <MemberLocationObjectId>0eba1e8b-7e39-47a3-865f-ee6a34113f67</MemberLocationObjectId>
    <MemberLocationURI>/vmrest/locations/connectionlocations/0eba1e8b-7e39-47a3-865f-ee6a34113f67</MemberLocationURI>
    <MemberGlobalUserDignetObjectId>34cc862e-19e4-4689-a4ee-
  ee98d83b8319</MemberGlobalUserDignetObjectId>
    <IsUserTemplate>true</IsUserTemplate>
    <LocationObjectId>0eba1e8b-7e39-47a3-865f-ee6a34113f67</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/0eba1e8b-7e39-47a3-865f-
  ee6a34113f67</LocationURI>
  </DistributionListMember>
</DistributionListMembers>
```

```
Response Code: 200
```

JSON Example

To get distribution list members:

```
GET https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId>/distributionlistmembers
Accept: application /json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
  "@total":"1"
  "DistributionListMember":
  {
    "URI":"/vmrest/distributionlists/dd043e9a-3f34-47eb-a72a-
    1b4b41e5f9d7/distributionlistmembers/dadd5c1c-1666-486a-94fa-bc681d99bfdb"
    "DistributionListObjectId":"dd043e9a-3f34-47eb-a72a-
    1b4b41e5f9d7"
    "DistributionListURI":"/vmrest/distributionlists/dd043e9a-3f34-47eb-a72a-
    1b4b41e5f9d7"
    "MemberUserObjectId":"216c1a3e-7c0e-4527-aa9c-32b2683f04be"
    "MemberUserURI":"/vmrest/users/216c1a3e-7c0e-4527-aa9c-
    32b2683f04be"
    "ObjectId":"dadd5c1c-1666-486a-94fa-bc681d99bfdb"
    "Alias":"kapil1_Operator_1"
    "DisplayName":"kapil1_Operator_1"
    "AllowForeignMessage":"false"
    "MemberGlobalUserObjectId":"216c1a3e-7c0e-4527-aa9c-32b2683f04be"
    "MemberGlobalUserURI":"/vmrest/globalusers/216c1a3e-7c0e-4527-aa9c-32b2683f04be"
    "MemberLocationObjectId":"830e1a2d-8e90-459f-88f7-700497ba975c"
    "MemberLocationURI":"/vmrest/locations/connectionlocations/830e1a2d-8e90-459f-
    88f7-700497ba975c"
    "MemberGlobalUserDignetObjectId":"216c1a3e-7c0e-4527-aa9c-32b2683f04be"
    "IsUserTemplate":"false"
    "LocationObjectId":"830e1a2d-8e90-459f-88f7-700497ba975c"
    "LocationURI":"/vmrest/locations/connectionlocations/830e1a2d-8e90-459f-88f7-
    700497ba975c"
  }
}
```

```
Response Code: 200
```

#### Creating a
                              	 Distribution List Member

You can create a new distribution list member by adding a user or user
                                    		  template or can add another distribution list as a member.

Example 1: Adding a user or user template to a distribution list To get user or user template object ID, you can use the following URIs:

```
GET https://<connection-server>/vmrest/users
GET https://<connection-server>/vmrest/usertemplates
```

The following is an example of the POST request that creates a new
                                    		  distribution list member by adding a user or user template:

```
POST https://<connection-server>/vmrest/distributionlists/ef4aa84e-97c3-456e-848e-
  b162a04c9631/distributionlistmembers
Request Body:
<DistributionListMember>
    <MemberUserObjectId>6202095f-606b-40d8-889d-f32e2d822f54</MemberUserObjectId>
</DistributionListMember>
```

```
Response Code: 201
```

Example 2: Adding another distribution list as a member The
                                    		  following is an example of the POST request that creates a new distribution
                                    		  list member by adding another distribution list as a member:

```
POST https://<connection-server>/vmrest/ distributionlists/ef4aa84e-97c3-456e-848e-b162a04c9631/distributionlistmembers
Request Body:
<DistributionListMember>
    <MemberDistributionListObjectId>e030d111-d29e-4d11-93fa-4abe73bd50a0</MemberDistributionListObjectId>
</DistributionListMember>
```

```
Response Code: 201
```

JSON Example:

To add a user or user template, do the following:

```
Request URI:
POST https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId>/distributionlistmembers
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "MemberUserObjectId": "216c1a3e-7c0e-4527-aa9c-32b2683f04be"
}
The following is the response from the above *POST* request and the actual response will depend upon the information given by you:
Response Code: 201
To add another distribution list as a member:
POST https://<connection-server>/vmrest/distributionlists/ef4aa84e-97c3-456e-848e-b162a04c9631/distributionlistmembers
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "MemberDistributionListObjectId":"e030d111-d29e-4d11-93fa-4abe73bd50a0"
}
```

The following is the response from the above *POST* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 201
```

#### Delete a Member
                              	 from the Distribution List

The following request can be used
                                    		  to delete a member from the distribution list:

```
DELETE: https://<connection-server>/vmrest/distributionlists/<DistributionListObjectId>/distributionlistmembers/<distributionlistmemberObjectId>
```

```
Response Code: 204
```

JSON Example:

```
DELETE https://<connection-server>/vmrest/distributionlists/<DistributionListObjectId>/distributionlistmembers/<distributionlistmemberObjectId>
Accept: application/json
Connection: keep-alive
```

```
Response Code: 204
```

#### Explanation of the
                              	 Data Fields for Distribution List Member

Possible values:

- true: allow
                                                         						  remote voice messaging

- false: Do not
                                                         						  allow remote voice messaging.

Default: false

| GET https://<connection-server>/vmrest/distributionlists |
|---|

| <DistributionLists total="3">
  <DistributionList>
    <URI>/vmrest/distributionlists/24865f76-fa95-412d-bc56-a48ef9e1531a</URI>
    <ObjectId>24865f76-fa95-412d-bc56-a48ef9e1531a</ObjectId>
    <Alias>undeliverablemessages</Alias>
    <DisplayName>Undeliverable Messages</DisplayName>
    <LocationObjectId>bbf3e6ed-0278-479c-9a6e-2da8756eeb6f</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/bbf3e6ed-0278-479c-9a6e-
    2da8756eeb6f</LocationURI>
    <PartitionObjectId>d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b</PartitionObjectId>
    <TenantObjectId>fe6541fb-b42c-44f2-8404-ded14cbf7438</TenantObjectId>
    <PartitionURI>/vmrest/partitions/d50e9d0b-656e-416d-b5b7-
    43c4d2e2fd0b</PartitionURI>
    <DistributionListMembersURI>/vmrest/distributionlists/24865f76-fa95-412d-bc56-
    a48ef9e1531a/distributionlistmembers</DistributionListMembersURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%2
    024865f76-fa95-412d-bc56-a48ef9e1531a)</AlternateNamesURI>
  </DistributionList>
  <DistributionList>
    <URI>/vmrest/distributionlists/f3e492dc-822b-43fb-be2f-416b972fb642</URI>
    <ObjectId>f3e492dc-822b-43fb-be2f-416b972fb642</ObjectId>
    <Alias>allvoicemailusers</Alias>
    <DisplayName>All Voice Mail Users</DisplayName>
    <LocationObjectId>bbf3e6ed-0278-479c-9a6e-2da8756eeb6f</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/bbf3e6ed-0278-479c-9a6e-
    2da8756eeb6f</LocationURI>
    <DtmfAccessId>99991</DtmfAccessId>
    <PartitionObjectId>d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/d50e9d0b-656e-416d-b5b7-
    43c4d2e2fd0b</PartitionURI>
    <DistributionListMembersURI>/vmrest/distributionlists/f3e492dc-822b-43fb-be2f-
    416b972fb642/distributionlistmembers</DistributionListMembersURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%2
    0f3e492dc-822b-43fb-be2f-416b972fb642)</AlternateNamesURI>
  </DistributionList>
  <DistributionList>
    <URI>/vmrest/distributionlists/c34b145e-b1f4-40de-9031-bc83703f0b1c</URI>
    <ObjectId>c34b145e-b1f4-40de-9031-bc83703f0b1c</ObjectId>
    <Alias>allvoicemailenabledcontacts</Alias>
    <DisplayName>All Voicemail-Enabled Contacts</DisplayName>
    <LocationObjectId>bbf3e6ed-0278-479c-9a6e-2da8756eeb6f</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/bbf3e6ed-0278-479c-9a6e-
    2da8756eeb6f</LocationURI>
    <DtmfAccessId>99992</DtmfAccessId>
    <PartitionObjectId>d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/d50e9d0b-656e-416d-b5b7-
    43c4d2e2fd0b</PartitionURI>
    <DistributionListMembersURI>/vmrest/distributionlists/c34b145e-b1f4-40de-9031-
    bc83703f0b1c/distributionlistmembers</DistributionListMembersURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%20c34b145e-b1f4-40de-9031-bc83703f0b1c)</AlternateNamesURI>
  </DistributionList>
  </DistributionLists> |
|---|

| Response Code: 204 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/distributionlists
Accept: application /json
Connection: keep-alive |
|---|

| {
  "@total":"2"
  "DistributionList":[
{
    "URI":"/vmrest/distributionlists/d9e61ace-3ece-4722-b331-ed57a73ef9eb"
    "ObjectId":"d9e61ace-3ece-4722-b331-ed57a73ef9eb"
    "Alias":"undeliverablemessages"
    "DisplayName":"Undeliverable Messages"
    "LocationObjectId":"830e1a2d-8e90-459f-88f7-700497ba975c"
    "LocationURI":"/vmrest/locations/connectionlocations/830e1a2d-8e90-459f-88f7-700497ba975c"
    "PartitionObjectId":"9c010254-1493-4e1a-9e47-fe2494792744"
    "TenantObjectId":"fe6541fb-b42c-44f2-8404-ded14cbf7438"
    "PartitionURI":"/vmrest/partitions/9c010254-1493-4e1a-9e47-fe2494792744"
    "DistributionListMembersURI":"/vmrest/distributionlists/d9e61ace-3ece-4722-b331-ed57a73ef9eb/distributionlistmembers"
    "AlternateNamesURI":"/vmrest/alternatenames?query=(DistributionListObjectId%20is%20d9e61ace-3ece-4722-b331-ed57a73ef9eb)"
}
{
    "URI":"/vmrest/distributionlists/a1fcfd8b-8749-465b-abe1-b578a8565107"
    "ObjectId":"a1fcfd8b-8749-465b-abe1-b578a8565107"
    "Alias":"allvoicemailusers"
    "DisplayName":"All Voice Mail Users"
    "LocationObjectId":"830e1a2d-8e90-459f-88f7-700497ba975c"
    "LocationURI":"/vmrest/locations/connectionlocations/830e1a2d-8e90-459f-88f7-700497ba975c"
    "DtmfAccessId":"99991"
    "PartitionObjectId":"9c010254-1493-4e1a-9e47-fe2494792744"
    "PartitionURI":"/vmrest/partitions/9c010254-1493-4e1a-9e47-fe2494792744"
    "DistributionListMembersURI":"/vmrest/distributionlists/a1fcfd8b-8749-465b-abe1-b578a8565107/distributionlistmembers"
    "AlternateNamesURI":"/vmrest/alternatenames?query=(DistributionListObjectId%20is%20a1fcfd8b-8749-465b-abe1-b578a8565107)"
}
]
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/distributionlists?query=(TenantObjectId is <Tenant-ObjectId>) |
|---|

| GET https://<connection-server>/vmrest/tenants |
|---|

| GET https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId> |
|---|

| <DistributionList>
    <URI>/vmrest/distributionlists/c34b145e-b1f4-40de-9031-bc83703f0b1c</URI>
    <ObjectId>c34b145e-b1f4-40de-9031-bc83703f0b1c</ObjectId>
    <Alias>allvoicemailenabledcontacts</Alias>
    <CreationTime>2013-02-14T05:05:42Z</CreationTime>
    <DisplayName>All Voicemail-Enabled Contacts</DisplayName>
    <DtmfName>2558642362453622</DtmfName>
    <IsPublic>true</IsPublic>
    <Undeletable>true</Undeletable>
    <VoiceName>d5814a39-94df-4498-acfd-93728a607be7.wav</VoiceName>
    <VoiceFileURI>/vmrest/voicefiles/d5814a39-94df-4498-acfd-93728a607be7.wav</VoiceFileURI>
    <VoiceNameURI>/vmrest/distributionlists/c34b145e-b1f4-40de-9031-
    bc83703f0b1c/voicename</VoiceNameURI>
    <LocationObjectId>bbf3e6ed-0278-479c-9a6e-2da8756eeb6f</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/bbf3e6ed-0278-479c-9a6e-
    2da8756eeb6f</LocationURI>
    <DtmfAccessId>99992</DtmfAccessId>
    <AllowContacts>true</AllowContacts>
    <AllowForeignMessage>false</AllowForeignMessage>
    <PartitionObjectId>d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b</PartitionURI>
    <DistributionListMembersURI>/vmrest/distributionlists/c34b145e-b1f4-40de-9031-
    bc83703f0b1c/distributionlistmembers</DistributionListMembersURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%20c34b14
    5e-b1f4-40de-9031-bc83703f0b1c)</AlternateNamesURI>
</DistributionList> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId>
Accept: application/json
Connection: keep-alive |
|---|

| {
    "URI":"/vmrest/distributionlists/d9e61ace-3ece-4722-b331-ed57a73ef9eb"
    "ObjectId":"d9e61ace-3ece-4722-b331-ed57a73ef9eb"
    "Alias":"undeliverablemessages"
    "CreationTime":"2013-02-21T11:39:08Z"
    "DisplayName":"Undeliverable Messages"
    "DtmfName":"8633548372253637"
    "IsPublic":"true"
    "Undeletable":"true"
    "VoiceName":"487e3db3-3782-4d30-a000-ef0d03ae22a2.wav"
    "VoiceFileURI":"/vmrest/voicefiles/487e3db3-3782-4d30-a000-ef0d03ae22a2.wav"
    "VoiceNameURI":"/vmrest/distributionlists/d9e61ace-3ece-4722-b331-
    ed57a73ef9eb/voicename"
    "LocationObjectId":"830e1a2d-8e90-459f-88f7-700497ba975c"
    "LocationURI":"/vmrest/locations/connectionlocations/830e1a2d-8e90-459f-88f7-
    700497ba975c"
    "AllowContacts":"false"
    "AllowForeignMessage":"false"
    "PartitionObjectId":"9c010254-1493-4e1a-9e47-fe2494792744"
    "PartitionURI":"/vmrest/partitions/9c010254-1493-4e1a-9e47-fe2494792744"
    "DistributionListMembersURI":"/vmrest/distributionlists/d9e61ace-3ece-4722-b331-
    ed57a73ef9eb/distributionlistmembers"
    "AlternateNamesURI":"/vmrest/alternatenames?query=(DistributionListObjectId%20is%20d9e61
    ace-3ece-4722-b331-ed57a73ef9eb)"
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-
  server>/vmrest/distributionlists?query=(PartitionObjectId%20is%20<objectId of the partition>) |
|---|

| GET https://<connection-server>/vmrest/partitions |
|---|

| <DistributionLists total="3">
  <DistributionList>
     <URI>/vmrest/distributionlists/2fe64511-1b69-4d97-b27b-ef383af4b194</URI>
     <ObjectId>2fe64511-1b69-4d97-b27b-ef383af4b194</ObjectId>
     <Alias>undeliverablemessages</Alias>
     <DisplayName>Undeliverable Messages</DisplayName>
     <LocationObjectId>42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationObjectId>
     <LocationURI>/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-
     8ddce4f430ff</LocationURI>
     <PartitionObjectId>da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionObjectId>
     <PartitionURI>/vmrest/partitions/da2114bf-cde7-43d8-9709-
     cd3895a9d41b</PartitionURI>
     <DistributionListMembersURI>/vmrest/distributionlists/2fe64511-1b69-4d97-b27b-
     ef383af4b194/distributionlistmembers</DistributionListMembersURI>
     <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%2
     02fe64511-1b69-4d97-b27b-ef383af4b194)</AlternateNamesURI>
  </DistributionList>
  <DistributionList>
    <URI>/vmrest/distributionlists/d37dfc67-04c2-48d3-9a7a-f2b316a09840</URI>
    <ObjectId>d37dfc67-04c2-48d3-9a7a-f2b316a09840</ObjectId>
    <Alias>allvoicemailusers</Alias>
    <DisplayName>All Voice Mail Users</DisplayName>
    <LocationObjectId>42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-
    8ddce4f430ff</LocationURI>
    <DtmfAccessId>99991</DtmfAccessId>
    <PartitionObjectId>da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/da2114bf-cde7-43d8-9709-
    cd3895a9d41b</PartitionURI>
    <DistributionListMembersURI>/vmrest/distributionlists/d37dfc67-04c2-48d3-9a7a-
    f2b316a09840/distributionlistmembers</DistributionListMembersURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%2
    0d37dfc67-04c2-48d3-9a7a-f2b316a09840)</AlternateNamesURI>
  </DistributionList>
  <DistributionList>
    <URI>/vmrest/distributionlists/160da8fe-2171-4bf7-9009-e95db94f823e</URI>
    <ObjectId>160da8fe-2171-4bf7-9009-e95db94f823e</ObjectId>
    <Alias>allvoicemailenabledcontacts</Alias>
    <DisplayName>All Voicemail-Enabled Contacts</DisplayName>
    <LocationObjectId>42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-
    8ddce4f430ff</LocationURI>
    <DtmfAccessId>99992</DtmfAccessId>
    <PartitionObjectId>da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/da2114bf-cde7-43d8-9709-
    cd3895a9d41b</PartitionURI>
    <DistributionListMembersURI>/vmrest/distributionlists/160da8fe-2171-4bf7-9009-
    e95db94f823e/distributionlistmembers</DistributionListMembersURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%2
    0160da8fe-2171-4bf7-9009-e95db94f823e)</AlternateNamesURI>
  </DistributionList>
  </DistributionLists> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/distributionlists?query=(PartitionObjectId%20is%20<objectId  of the partition>)
Accept: application/json
Connection: keep-alive |
|---|

| {
  "@total":"3"
  "DistributionList":[
  {
    "URI":"/vmrest/distributionlists/2fe64511-1b69-4d97-b27b-ef383af4b194"
    "ObjectId":"2fe64511-1b69-4d97-b27b-ef383af4b194"
    "Alias":"undeliverablemessages"
    "DisplayName":"Undeliverable Messages"
    "LocationObjectId":"42a9ab40-490d-4819-9bfb-8ddce4f430ff"
    "LocationURI":"/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-
    8ddce4f430ff"
    "PartitionObjectId":"da2114bf-cde7-43d8-9709-cd3895a9d41b"
    "PartitionURI":"/vmrest/partitions/da2114bf-cde7-43d8-9709-cd3895a9d41b"
    "DistributionListMembersURI":"/vmrest/distributionlists/2fe64511-1b69-4d97-b27b-
    ef383af4b194/distributionlistmembers"
    "AlternateNamesURI":"/vmrest/alternatenames?query=(DistributionListObjectId%20is%20
    2fe64511-1b69-4d97-b27b-ef383af4b194)"
  }
  {
    "URI":"/vmrest/distributionlists/d37dfc67-04c2-48d3-9a7a-f2b316a09840"
    "ObjectId":"d37dfc67-04c2-48d3-9a7a-f2b316a09840"
    "Alias":"allvoicemailusers"
    "DisplayName":"All Voice Mail Users"
    "LocationObjectId":"42a9ab40-490d-4819-9bfb-8ddce4f430ff"
    "LocationURI":"/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-
    8ddce4f430ff"
    "DtmfAccessId":"99991"
    "PartitionObjectId":"da2114bf-cde7-43d8-9709-cd3895a9d41b"
    "PartitionURI":"/vmrest/partitions/da2114bf-cde7-43d8-9709-cd3895a9d41b"
    "DistributionListMembersURI":"/vmrest/distributionlists/d37dfc67-04c2-48d3-9a7a-
    f2b316a09840/distributionlistmembers"
    "AlternateNamesURI":"/vmrest/alternatenames?query=(DistributionListObjectId%20is%2
    0d37dfc67-04c2-48d3-9a7a-f2b316a09840)"
  }
  {
    "URI":"/vmrest/distributionlists/160da8fe-2171-4bf7-9009-e95db94f823e"
    "ObjectId":"160da8fe-2171-4bf7-9009-e95db94f823e"
    "Alias":"allvoicemailenabledcontacts"
    "DisplayName":"All Voicemail-Enabled Contacts"
    "LocationObjectId":"42a9ab40-490d-4819-9bfb-8ddce4f430ff"
    "LocationURI":"/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-
    8ddce4f430ff"
    "DtmfAccessId":"99992"
    "PartitionObjectId":"da2114bf-cde7-43d8-9709-cd3895a9d41b"
    "PartitionURI":"/vmrest/partitions/da2114bf-cde7-43d8-9709-cd3895a9d41b"
    "DistributionListMembersURI":"/vmrest/distributionlists/160da8fe-2171-4bf7-9009-
    e95db94f823e/distributionlistmembers"
    "AlternateNamesURI":"/vmrest/alternatenames?query=(DistributionListObjectId%20is%2
    0160da8fe-2171-4bf7-9009-e95db94f823e)"
  }
  }
} |
|---|

| Response Code: 200 |
|---|

| POST https://<connection-server>/vmrest/distributionlists |
|---|

| Request Body:
<DistributionList>
    <Alias>Texoma_allvoicemailusersDL_1 </Alias>
    <DisplayName>Texoma_allvoicemailusersDL_1</DisplayName>
</DistributionList> |
|---|

| Response Code: 201
/vmrest/distributionlists/3049a03c-108d-40aa-a989-0b008f07656c |
|---|

| Request URI:
POST https://<connection-server>/vmrest/distributionlists
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "Alias":"Texoma1"
    "DisplayName": "Texoma 1"
} |
|---|

| Response Code: 201
/vmrest/distributionlists/dd043e9a-3f34-47eb-a72a-1b4b41e5f9d7 |
|---|

| DELETE: https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId> |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId>
Accept: application/json
Connection: keep-alive |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId> |
|---|

| Request Body:
<DistributionList>
    <AllowContacts>false</AllowContacts>
    <AllowForeignMessage>false</AllowForeignMessage>
</DistributionList> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "AllowContacts":"false",
    "AllowForeignMessage":"false"
} |
|---|

| Response Code: 204 |
|---|

| Request Body:
<DistributionList>
    <AllowContacts>true</AllowContacts>
    <AllowForeignMessage>false</AllowForeignMessage>
</DistributionList> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId>
Accept: application/json
Content-Type: application/json
Connection: keep-alive 
Request Body:
{
    "AllowContacts":"false",
    "AllowForeignMessage":"false"
} |
|---|

| Response Code: 204 |
|---|

| Request Body:
<DistributionList>
    <AllowContacts>false</AllowContacts>
    <AllowForeignMessage>true</AllowForeignMessage>
</DistributionList>
The following is the response from the above *PUT* request and the actual response will depend upon the information given by you:
Response Code: 204
JSON Example:
Request URI:
PUT https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "AllowContacts":"false",
    "AllowForeignMessage":"true"
}
The following is the response from the above *PUT* request and the actual response will depend upon the information given by you:
Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId> |
|---|

| Request Body:
<DistributionList>
              <TenantObjectId>fe6541fb-b42c-44f2-8404-ded14cbf7438</TenantObjectId>
</DistributionList> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
"TenantObjectId":"fe6541fb-b42c-44f2-8404-ded14cbf7438"
} |
|---|

| POST https://<connection-server>/vmrest/alternatenames?query=(DistributionListObjectId%20is%20ef4aa84e-97c3-456e-848e-b162a04c9631)  
Request Body:
<AlternateName>
    <FirstName>Taxoma_list1</FirstName>
    <DistributionListObjectId>ef4aa84e-97c3-456e-848e-b162a04c9631</DistributionListObjectId>
</AlternateName> |
|---|

| Response Code: 201
/vmrest/alternatenames/e091a0f6-031e-440d-abd2-783e5f62511b |
|---|

| Request URI:
POST https://<connection-
server>/vmrest/alternatenames?query=(DistributionListObjectId%20is%20ef4aa84e-97c3-456e-848e-
b162a04c9631)
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "FirstName":"Taxoma_list1",
    "DistributionListObjectId":"ef4aa84e-97c3-456e-848e-b162a04c9631"
} |
|---|

| Response Code: 201
/vmrest/alternatenames/e091a0f6-031e-440d-abd2-783e5f62511b |
|---|

| GET https://<connection-server>/vmrest/ alternatenames?query=(DistributionListObjectId%20is%20ef4aa84e-97c3-456e-848e-b162a04c9631) |
|---|

| <AlternateNames total="2">
  <AlternateName>
    <URI>/vmrest/alternatenames/865615e9-1c00-4121-acf4-36ee00adb09c</URI>
    <FirstName>Texoma_Alternane Name 1</FirstName>
    <ObjectId>865615e9-1c00-4121-acf4-36ee00adb09c</ObjectId>
    <DistributionListObjectId>e703511f-fa9b-41f2-8662-
    23de75fffc96</DistributionListObjectId>
    <DistributionListURI>/vmrest/distributionlists/e703511f-fa9b-41f2-8662-
    23de75fffc96</DistributionListURI>
  </AlternateName>
  <AlternateName>
    <URI>/vmrest/alternatenames/af735ef8-b3f3-4c97-a8ec-667e416cfde2</URI>
    <FirstName>Texoma_Alternate Name 2</FirstName>
    <ObjectId>af735ef8-b3f3-4c97-a8ec-667e416cfde2</ObjectId>
    <DistributionListObjectId>e703511f-fa9b-41f2-8662-
    23de75fffc96</DistributionListObjectId>
    <DistributionListURI>/vmrest/distributionlists/e703511f-fa9b-41f2-8662-
    23de75fffc96</DistributionListURI>
  </AlternateName>
</AlternateNames> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/alternatenames?query=(DistributionListObjectId%20is%20c238c2bf-4037-494d-951b-090468c95dc4)
Accept: application/json
Connection: keep-alive |
|---|

| {
  "@total":"1","AlternateName":
  {
    "URI":"/vmrest/alternatenames/e091a0f6-031e-440d-abd2-783e5f62511b",
    "FirstName":"Taxoma_list1",
    "ObjectId":"e091a0f6-031e-440d-abd2-783e5f62511b",
    "DistributionListObjectId":"c238c2bf-4037-494d-951b-090468c95dc4",
    "DistributionListURI":"/vmrest/distributionlists/c238c2bf-4037-494d-951b-
    090468c95dc4"
  }
} |
|---|

| Response Code: 200 |
|---|

| DELETE https://<connection-server>/vmrest /alternatenames/<AlternateNameObjectId> |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/alternatenames/<AlternateNameObjectId>
Accept: application/json
Connection: keep-alive |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/alternatenames/<AlternateNameObjectId>
Request Body:
<AlternateName>
    <FirstName>Texoma_Alternane Name1</FirstName>
</AlternateName> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/alternatenames/<AlternateNameObjectId>
Accept: application/json
Connection: keep-alive
Request Body:
{
    "FirstName":"Texoma1"
} |
|---|

| Response Code: 204 |
|---|

| Parameter | Operation | Data Type | Comments |
|---|---|---|---|
| Alias | Read/Write | String(64) | Unique name for a distribution List |
| AllowContacts | Read/Write | Boolean | A flag indicating whether contacts (system,
                                                					 VPIM,virtual) are allowed to be members of this Distribution List. Purpose of
                                                					 this flag is to enable administrators to create a Distribution List whose
                                                					 members are Contacts. Possible values: true: allow
                                                         						  contacts (system, VPIM,virtual) are allowed to be members of this Distribution
                                                         						  List false: Do not
                                                         						  allow contacts (system, VPIM,virtual) are allowed to be members of this
                                                         						  Distribution List Default: false |
| AllowForeignMesssage | Read/Write | Boolean | Allow users on remote voice messaging
                                                					 systems that are configured as VPIM locations to send messages to this
                                                					 distribution list. Only valid if the list is for subscribers only (i.e. does
                                                					 not allow contacts) Possible Values: true: allow
                                                         						  remote voice messaging false: Do not
                                                         						  allow remote voice messaging. Default: False |
| CreationTime | Read Only | Datetime | The date and time the system distribution
                                                					 list was created in UTC |
| DisplayName | Read/Write | String(64) | The unique text name of the system
                                                					 distribution. |
| DtmfAccessId | Read/Write | String(40) | Extension that the phone system uses to
                                                					 connect to the distribution list.It is an optional field. |
| DtmfName | Read Only | String(64) | The series of digits corresponding to the
                                                					 numeric keypad mapping on a standard touchtone phone representing the display
                                                					 name of the system distribution list. These digits are used for searching the
                                                					 distribution list by name via the phone. |
| LocationObjectId | Read Only | String(16) | The unique identifier of the LocationVMS
                                                					 object to which this system distribution list belongs. |
| ObjectId | Read Only | String(36) | Object Id of the distribution list created. |
| PartitionObjectId | Read Only | String(36) | The unique identifier of the Partition to
                                                					 which the DistributionList is assigned. |
| TenantObjectId | Read/Write | String(36) | The unique identifier of the tenant to
                                                					 which the distribution list belongs. This field is reflected in the response
                                                					 only if the distribution list belongs to a particular tenant. |
| VoiceName | Read/Write | String(40) | The voicename of the distribution List |
| URI | Read Only | String | URI of the Distribution list |
| VoiceFileURI | Read Only | String | URI of Voice File |
| VoiceNameURI | Read Only | String | Voice Name URI |
| LocationURI | Read Only | String | Location URI |
| PartitionURI | Read Only | String | Partition URI |
| PartitionURI | Read Only | String | Distribution List URI |
| AlternameNamesURI | Read Only | String | Alternate Names URI |

| Parameter | Operation | Data Type | Comments |
|---|---|---|---|
| First Name | Read/Write | String (64) | Specifies the alternate name of a
                                                					 distribution list. |
| ObjectId | Read Only | String (36) | Specifies the objectid of the alternate
                                                					 name. |
| DistributionListObjectId | Read Only | String (36) | Specifies the object ID of the distribution
                                                					 list. |
| URI | Read Only | String | Specifies the URI of the alternate name. |
| DistributionListURI | Read Only | String | Specifies the URI of distribution list. |

| Request URI:
GET https://<connection-
server>/vmrest/distributionlists/<distributionlistObjectId>/distributionlistmember |
|---|

| GET https://<connection server>/vmrest/distributionlists/ef4aa84e-97c3-456e-848e-
  b162a04c9631/distributionlistmembers |
|---|

| <DistributionListMembers total="1">
  <DistributionListMember>
    <URI>/vmrest/distributionlists/ef4aa84e-97c3-456e-848e-
  b162a04c9631/distributionlistmembers/f6712058-3409-49eb-a616-517614766594</URI>
    <DistributionListObjectId>ef4aa84e-97c3-456e-848e-
  b162a04c9631</DistributionListObjectId>
    <DistributionListURI>/vmrest/distributionlists/ef4aa84e-97c3-456e-848e-
  b162a04c9631</DistributionListURI>
    <MemberUserObjectId>34cc862e-19e4-4689-a4ee-
  ee98d83b8319</MemberUserObjectId>
    <MemberUserURI>/vmrest/users/34cc862e-19e4-4689-a4ee-
  ee98d83b8319</MemberUserURI>
    <ObjectId>f6712058-3409-49eb-a616-517614766594</ObjectId>
    <Alias>Texoma_UserTemplate_1</Alias>
    <DisplayName>Texoma_UserTemplate_1</DisplayName>
    <AllowForeignMessage>false</AllowForeignMessage>
    <MemberGlobalUserObjectId>34cc862e-19e4-4689-a4ee-
  ee98d83b8319</MemberGlobalUserObjectId>
    <MemberGlobalUserURI>/vmrest/globalusers/34cc862e-19e4-4689-a4ee-
  ee98d83b8319</MemberGlobalUserURI>
    <MemberLocationObjectId>0eba1e8b-7e39-47a3-865f-ee6a34113f67</MemberLocationObjectId>
    <MemberLocationURI>/vmrest/locations/connectionlocations/0eba1e8b-7e39-47a3-865f-ee6a34113f67</MemberLocationURI>
    <MemberGlobalUserDignetObjectId>34cc862e-19e4-4689-a4ee-
  ee98d83b8319</MemberGlobalUserDignetObjectId>
    <IsUserTemplate>true</IsUserTemplate>
    <LocationObjectId>0eba1e8b-7e39-47a3-865f-ee6a34113f67</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/0eba1e8b-7e39-47a3-865f-
  ee6a34113f67</LocationURI>
  </DistributionListMember>
</DistributionListMembers> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId>/distributionlistmembers
Accept: application /json
Connection: keep-alive |
|---|

| {
  "@total":"1"
  "DistributionListMember":
  {
    "URI":"/vmrest/distributionlists/dd043e9a-3f34-47eb-a72a-
    1b4b41e5f9d7/distributionlistmembers/dadd5c1c-1666-486a-94fa-bc681d99bfdb"
    "DistributionListObjectId":"dd043e9a-3f34-47eb-a72a-
    1b4b41e5f9d7"
    "DistributionListURI":"/vmrest/distributionlists/dd043e9a-3f34-47eb-a72a-
    1b4b41e5f9d7"
    "MemberUserObjectId":"216c1a3e-7c0e-4527-aa9c-32b2683f04be"
    "MemberUserURI":"/vmrest/users/216c1a3e-7c0e-4527-aa9c-
    32b2683f04be"
    "ObjectId":"dadd5c1c-1666-486a-94fa-bc681d99bfdb"
    "Alias":"kapil1_Operator_1"
    "DisplayName":"kapil1_Operator_1"
    "AllowForeignMessage":"false"
    "MemberGlobalUserObjectId":"216c1a3e-7c0e-4527-aa9c-32b2683f04be"
    "MemberGlobalUserURI":"/vmrest/globalusers/216c1a3e-7c0e-4527-aa9c-32b2683f04be"
    "MemberLocationObjectId":"830e1a2d-8e90-459f-88f7-700497ba975c"
    "MemberLocationURI":"/vmrest/locations/connectionlocations/830e1a2d-8e90-459f-
    88f7-700497ba975c"
    "MemberGlobalUserDignetObjectId":"216c1a3e-7c0e-4527-aa9c-32b2683f04be"
    "IsUserTemplate":"false"
    "LocationObjectId":"830e1a2d-8e90-459f-88f7-700497ba975c"
    "LocationURI":"/vmrest/locations/connectionlocations/830e1a2d-8e90-459f-88f7-
    700497ba975c"
  }
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/users
GET https://<connection-server>/vmrest/usertemplates |
|---|

| POST https://<connection-server>/vmrest/distributionlists/ef4aa84e-97c3-456e-848e-
  b162a04c9631/distributionlistmembers
Request Body:
<DistributionListMember>
    <MemberUserObjectId>6202095f-606b-40d8-889d-f32e2d822f54</MemberUserObjectId>
</DistributionListMember> |
|---|

| Response Code: 201 |
|---|

| POST https://<connection-server>/vmrest/ distributionlists/ef4aa84e-97c3-456e-848e-b162a04c9631/distributionlistmembers
Request Body:
<DistributionListMember>
    <MemberDistributionListObjectId>e030d111-d29e-4d11-93fa-4abe73bd50a0</MemberDistributionListObjectId>
</DistributionListMember> |
|---|

| Response Code: 201 |
|---|

| Request URI:
POST https://<connection-server>/vmrest/distributionlists/<distributionlistObjectId>/distributionlistmembers
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "MemberUserObjectId": "216c1a3e-7c0e-4527-aa9c-32b2683f04be"
}
The following is the response from the above *POST* request and the actual response will depend upon the information given by you:
Response Code: 201
To add another distribution list as a member:
POST https://<connection-server>/vmrest/distributionlists/ef4aa84e-97c3-456e-848e-b162a04c9631/distributionlistmembers
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "MemberDistributionListObjectId":"e030d111-d29e-4d11-93fa-4abe73bd50a0"
} |
|---|

| Response Code: 201 |
|---|

| DELETE: https://<connection-server>/vmrest/distributionlists/<DistributionListObjectId>/distributionlistmembers/<distributionlistmemberObjectId> |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/distributionlists/<DistributionListObjectId>/distributionlistmembers/<distributionlistmemberObjectId>
Accept: application/json
Connection: keep-alive |
|---|

| Response Code: 204 |
|---|

| Parameter | Operations | Data Type | Comments |
|---|---|---|---|
| URI | Read Only | String | Specifies the URI of the distribution list
                                                					 member. |
| ObjectId | Read Only | String (36) | Specifies the Object Id of the distribution
                                                					 list member. |
| DistributionListObjectId | Read Only | String (36) | Specifies the distribution list object ID. |
| DistributionListURI | Read Only | String | Specifies the URI of the distribution list. |
| MemberUserObjectId | Read Only | String (36) | Specifies the object ID of user or user
                                                					 template. |
| MemberGlobalUserObjectId | Read Only | String (36) | Specifies the object ID of the user or user
                                                					 template. |
| MemberDistributionListObjectId | Read Only | String (36) | Specifies the object ID of the member's
                                                					 distribution list. |
| MemberGlobalUserDiginetObjectId | Read Only | String (36) | Specifies the object ID of the user. |
| MemberLocationObjectId | Read Only | String (36) | Specifies the object ID of the member
                                                					 location. |
| Alias | Read/Write | String (64) | Specifies the unique name to identify a
                                                					 distribution list. |
| AllowForeignMessage | Read Only | Boolean | Allow users on remote voice messaging
                                                					 systems that are configured as VPIM locations to send messages to this
                                                					 distribution list. Possible values: true: allow
                                                         						  remote voice messaging false: Do not
                                                         						  allow remote voice messaging. Default: false |
| DisplayName | Read/Write | String (64) | Specifies name of the member. |
| IsUserTemplate | Read Only | Boolean | Specifies if a member is a user template. |
| MemberLocationURI | Read Only | String | Specifies URI of the location. |
| MemberGlobalUserURI | Read Only | String | Specifies URI of the user. |
| LocationObjectId | Read Only | String (36) | Specifies location object ID. |
| LocationURI | Read Only | String | Specifies URI of the location. |