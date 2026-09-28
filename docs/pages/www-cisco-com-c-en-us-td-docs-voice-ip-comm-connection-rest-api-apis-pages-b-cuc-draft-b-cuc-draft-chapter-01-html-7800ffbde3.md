---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-apis-pages-b-cuc-draft-b-cuc-draft-chapter-01-html-7800ffbde3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/APIs_Pages/b_CUC_Draft/b_CUC_Draft_chapter_01.html
retrieved_at: 2026-08-21T08:08:04.222899+00:00
---

Cisco Unity Connection Draft

# Cisco Unity Connection Draft

Updated: January 2, 2019

Chapter: Cisco Unity Connection API List Examples

## Chapter: Cisco Unity Connection API List Examples

- Cisco Unity Connection API List Examples

- Cisco Unity Connection API List Examples

# Cisco Unity Connection API List Examples

## Cisco Unity Connection API List Examples

Examples for /vmrest/version

Example 1: GET

HTTP GET:

```
https://10.10.10.10:8443/vmrest/version
```

HTTP RESPONSE:

```
<VersionInformation>
    <name>vmrest</name>
    <version>8.6.2.0ES3</version>
</VersionInformation>
```

Examples for /vmrest/distributionlist

Example 1: GET

HTTP GET:

```
https://10.10.10.10:8443/vmrest/distributionlists
```

HTTP RESPONSE:

```
<DistributionLists total="2">
  <DistributionList>
    <URI>/vmrest/distributionlists/92fa35cc-a72e-4f59-83e5-ccf6fce07f1e</URI>
    <ObjectId>92fa35cc-a72e-4f59-83e5-ccf6fce07f1e</ObjectId>
    <Alias>undeliverablemessages</Alias>
    <DisplayName>Undeliverable Messages</DisplayName>
    <LocationObjectId>3b05f7ec-2398-4e43-b23c-03535ab9afc9</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/3b05f7ec-2398-4e43-b23c-03535ab9afc9</LocationURI>
    <PartitionObjectId>e886836c-f61b-4bc2-ba37-12d06b446abd</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/e886836c-f61b-4bc2-ba37-12d06b446abd</PartitionURI>
    <DistributionListMembersURI>/vmrest/distributionlists/92fa35cc-a72e-4f59-83e5-ccf6fce07f1e/distributionlistmembers</DistributionListMembersURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%2092fa35cc-a72e-4f59-83e5-ccf6fce07f1e)</AlternateNamesURI>
  </DistributionList>
  <DistributionList>
    <URI>/vmrest/distributionlists/24f444c9-34ce-4072-9270-672933c7bb3a</URI>
    <ObjectId>24f444c9-34ce-4072-9270-672933c7bb3a</ObjectId>
    <Alias>allvoicemailusers</Alias>
    <DisplayName>All Voice Mail Users</DisplayName>
    <LocationObjectId>3b05f7ec-2398-4e43-b23c-03535ab9afc9</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/3b05f7ec-2398-4e43-b23c-03535ab9afc9</LocationURI>
    <DtmfAccessId>99991</DtmfAccessId>
    <PartitionObjectId>e886836c-f61b-4bc2-ba37-12d06b446abd</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/e886836c-f61b-4bc2-ba37-12d06b446abd</PartitionURI>
    <DistributionListMembersURI>/vmrest/distributionlists/24f444c9-34ce-4072-9270-672933c7bb3a/distributionlistmembers</DistributionListMembersURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%2024f444c9-34ce-4072-9270-672933c7bb3a)</AlternateNamesURI>
  </DistributionList>
 </DistributionLists>
```

Example 2: GET

HTTP GET:

```
https://10.10.10.10:8443/vmrest/distributionlists?query=(alias startswith F)&sort=(alias desc)
```

HTTP RESPONSE:

```
<DistributionLists total="2">
  <DistributionList>
    <URI>/vmrest/distributionlists/de9cb6c5-873c-454b-8fd3-58b7aaf62dd0</URI>
    <ObjectId>de9cb6c5-873c-454b-8fd3-58b7aaf62dd0</ObjectId>
    <Alias>FSTDK02</Alias>
    <DisplayName>FSTDK02</DisplayName>
    <LocationObjectId>3b05f7ec-2398-4e43-b23c-03535ab9afc9</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/3b05f7ec-2398-4e43-b23c-03535ab9afc9</LocationURI>
    <DtmfAccessId>4445</DtmfAccessId>
    <PartitionObjectId>e886836c-f61b-4bc2-ba37-12d06b446abd</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/e886836c-f61b-4bc2-ba37-12d06b446abd</PartitionURI>
    <DistributionListMembersURI>/vmrest/distributionlists/de9cb6c5-873c-454b-8fd3-58b7aaf62dd0/distributionlistmembers</DistributionListMembersURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%20de9cb6c5-873c-454b-8fd3-58b7aaf62dd0)</AlternateNamesURI>
  </DistributionList>
  <DistributionList>
    <URI>/vmrest/distributionlists/d3e0c786-0be4-4b72-a27b-c745d1504180</URI>
    <ObjectId>d3e0c786-0be4-4b72-a27b-c745d1504180</ObjectId>
    <Alias>FSTDK01</Alias>
    <DisplayName>FSTDK01</DisplayName>
    <LocationObjectId>3b05f7ec-2398-4e43-b23c-03535ab9afc9</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/3b05f7ec-2398-4e43-b23c-03535ab9afc9</LocationURI>
    <DtmfAccessId>4444</DtmfAccessId>
    <PartitionObjectId>e886836c-f61b-4bc2-ba37-12d06b446abd</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/e886836c-f61b-4bc2-ba37-12d06b446abd</PartitionURI>
    <DistributionListMembersURI>/vmrest/distributionlists/d3e0c786-0be4-4b72-a27b-c745d1504180/distributionlistmembers</DistributionListMembersURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%20d3e0c786-0be4-4b72-a27b-c745d1504180)</AlternateNamesURI>
  </DistributionList>
</DistributionLists>
```

Example 3: POST

HTTP POST:

```
https://10.10.10.10:8443/vmrest/distributionlists
```

HTTP BODY:

```
<DistributionList>
  <Alias>FSTDK03</Alias> 
  <DisplayName>FSTDK03</DisplayName> 
  <DtmfAccessId>4446</DtmfAccessId>
</DistributionList>
```

HTTP RESPONSE:

```
/vmrest/distributionlists/5f038b49-5840-4974-b555-fadfaa327024
```

Example 4: PUT

HTTP PUT:

```
https://10.10.10.10:8443/vmrest/distributionlists/{objectid}
```

HTTP BODY:

```
<DistributionList>
  <DtmfAccessId>4447</DtmfAccessId>
</DistributionList>
```

HTTP RESPONSE:

```
{empty response}  Return Code = HTTP/1.1 204 No Content
```

| https://10.10.10.10:8443/vmrest/version |
|---|

| <VersionInformation>
    <name>vmrest</name>
    <version>8.6.2.0ES3</version>
</VersionInformation> |
|---|

| https://10.10.10.10:8443/vmrest/distributionlists |
|---|

| <DistributionLists total="2">
  <DistributionList>
    <URI>/vmrest/distributionlists/92fa35cc-a72e-4f59-83e5-ccf6fce07f1e</URI>
    <ObjectId>92fa35cc-a72e-4f59-83e5-ccf6fce07f1e</ObjectId>
    <Alias>undeliverablemessages</Alias>
    <DisplayName>Undeliverable Messages</DisplayName>
    <LocationObjectId>3b05f7ec-2398-4e43-b23c-03535ab9afc9</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/3b05f7ec-2398-4e43-b23c-03535ab9afc9</LocationURI>
    <PartitionObjectId>e886836c-f61b-4bc2-ba37-12d06b446abd</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/e886836c-f61b-4bc2-ba37-12d06b446abd</PartitionURI>
    <DistributionListMembersURI>/vmrest/distributionlists/92fa35cc-a72e-4f59-83e5-ccf6fce07f1e/distributionlistmembers</DistributionListMembersURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%2092fa35cc-a72e-4f59-83e5-ccf6fce07f1e)</AlternateNamesURI>
  </DistributionList>
  <DistributionList>
    <URI>/vmrest/distributionlists/24f444c9-34ce-4072-9270-672933c7bb3a</URI>
    <ObjectId>24f444c9-34ce-4072-9270-672933c7bb3a</ObjectId>
    <Alias>allvoicemailusers</Alias>
    <DisplayName>All Voice Mail Users</DisplayName>
    <LocationObjectId>3b05f7ec-2398-4e43-b23c-03535ab9afc9</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/3b05f7ec-2398-4e43-b23c-03535ab9afc9</LocationURI>
    <DtmfAccessId>99991</DtmfAccessId>
    <PartitionObjectId>e886836c-f61b-4bc2-ba37-12d06b446abd</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/e886836c-f61b-4bc2-ba37-12d06b446abd</PartitionURI>
    <DistributionListMembersURI>/vmrest/distributionlists/24f444c9-34ce-4072-9270-672933c7bb3a/distributionlistmembers</DistributionListMembersURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%2024f444c9-34ce-4072-9270-672933c7bb3a)</AlternateNamesURI>
  </DistributionList>
 </DistributionLists> |
|---|

| https://10.10.10.10:8443/vmrest/distributionlists?query=(alias startswith F)&sort=(alias desc) |
|---|

| <DistributionLists total="2">
  <DistributionList>
    <URI>/vmrest/distributionlists/de9cb6c5-873c-454b-8fd3-58b7aaf62dd0</URI>
    <ObjectId>de9cb6c5-873c-454b-8fd3-58b7aaf62dd0</ObjectId>
    <Alias>FSTDK02</Alias>
    <DisplayName>FSTDK02</DisplayName>
    <LocationObjectId>3b05f7ec-2398-4e43-b23c-03535ab9afc9</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/3b05f7ec-2398-4e43-b23c-03535ab9afc9</LocationURI>
    <DtmfAccessId>4445</DtmfAccessId>
    <PartitionObjectId>e886836c-f61b-4bc2-ba37-12d06b446abd</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/e886836c-f61b-4bc2-ba37-12d06b446abd</PartitionURI>
    <DistributionListMembersURI>/vmrest/distributionlists/de9cb6c5-873c-454b-8fd3-58b7aaf62dd0/distributionlistmembers</DistributionListMembersURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%20de9cb6c5-873c-454b-8fd3-58b7aaf62dd0)</AlternateNamesURI>
  </DistributionList>
  <DistributionList>
    <URI>/vmrest/distributionlists/d3e0c786-0be4-4b72-a27b-c745d1504180</URI>
    <ObjectId>d3e0c786-0be4-4b72-a27b-c745d1504180</ObjectId>
    <Alias>FSTDK01</Alias>
    <DisplayName>FSTDK01</DisplayName>
    <LocationObjectId>3b05f7ec-2398-4e43-b23c-03535ab9afc9</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/3b05f7ec-2398-4e43-b23c-03535ab9afc9</LocationURI>
    <DtmfAccessId>4444</DtmfAccessId>
    <PartitionObjectId>e886836c-f61b-4bc2-ba37-12d06b446abd</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/e886836c-f61b-4bc2-ba37-12d06b446abd</PartitionURI>
    <DistributionListMembersURI>/vmrest/distributionlists/d3e0c786-0be4-4b72-a27b-c745d1504180/distributionlistmembers</DistributionListMembersURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(DistributionListObjectId%20is%20d3e0c786-0be4-4b72-a27b-c745d1504180)</AlternateNamesURI>
  </DistributionList>
</DistributionLists> |
|---|

| https://10.10.10.10:8443/vmrest/distributionlists |
|---|

| <DistributionList>
  <Alias>FSTDK03</Alias> 
  <DisplayName>FSTDK03</DisplayName> 
  <DtmfAccessId>4446</DtmfAccessId>
</DistributionList> |
|---|

| /vmrest/distributionlists/5f038b49-5840-4974-b555-fadfaa327024 |
|---|

| https://10.10.10.10:8443/vmrest/distributionlists/{objectid} |
|---|

| <DistributionList>
  <DtmfAccessId>4447</DtmfAccessId>
</DistributionList> |
|---|

| {empty response}  Return Code = HTTP/1.1 204 No Content |
|---|