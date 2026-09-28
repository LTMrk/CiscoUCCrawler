---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-broadworks-application-server-220164-configure-broadworks-ocis-20e4e74d50
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/broadworks-application-server/220164-configure-broadworks-ocisendertool.html
retrieved_at: 2026-09-07T13:00:52.547490+00:00
---

Configure Broadworks OCISenderTool

# Configure Broadworks OCISenderTool

### Download Options

Updated: January 27, 2023

Document ID: 220164

Contents

## Contents

## Introduction

This document describes the usage of a demonstration client provided by Cisco that can be used to test OCI-P commands and connectivity.

## Prerequisites

### Requirements

- The asociclient can be installed on either your PC or server.

- The IP address of the incoming request source needs to be added to the BroadWorks Network Access List.

- A valid OCI-P command is required.

### BroadWorks Configuration

In this instance the OCISenderTool is hosted on server 172.16.30.3.

Ensure this IP is added in the OCI-P Network Access List AS_CLI/System/NetworkAccessLists/OCI/Provisioning>.

```
AS_CLI/System/NetworkAccessLists/OCI/Provisioning> get Address    Description ============================ ... 172.16.30.3  OCISenderTool
```

### OCI-P Command

In this instance use the command ' GroupAccessDeviceGetListRequest ' for Enterprise pws_ent and Group pws_grp .

This file is called ' pws_GroupAccessDeviceGetListRequest.xml '.

```
<?xml version="1.0" encoding="ISO-8859-1"?> <BroadsoftDocument protocol="OCI" xmlns="C" xmlns:xsi=" http://www.w3.org/2001/XMLSchema-instance "> <sessionId xmlns="">%%%OCI_SESSION_ID%%%</sessionId> <command xsi:type=" GroupAccessDeviceGetListRequest " xmlns=""> <serviceProviderId> pws_ent </serviceProviderId> <groupId> pws_grp </groupId> </command> </BroadsoftDocument>
```

## Usage Options

To run this command, you need to select the relevant parameters.

```
[bwadmin@bwtaclab ASOCICLIENT]$ ./startASOCIClient.sh **** OCI Client Build Version: 1.1.2 **** Usage: startOCIClient configFile startOCIClient loginId password [-i inputXMLFile] [-o outputXMLFile] [-h host] [-p port] [-m {un}secure/{s}ecure] [-c BCCT/OCS] [-t timeOut] [-s sessionID] [-l loginRequestName] [-f tabSize] loginId           LoginId of the user (mandatory) password          Password of the user (mandatory) -i inputXMLFile   File containing the XML Request -o outputXMLFile  File to write the XML Response. File is over-written. If not provided will default to: inputXMLFile.response.xml) -h host           HostName to connect to.  Default is localhost -p port           Port to connect to.  Default is 31000 -m mode           Unsecure/Secure mode for login -c connection     BCCT or OCS -t timeOut        Timeout in seconds to pause for a response from the server. (Default is 30 seconds, if set to -1 will never timeout) -s sessionID      session ID -l loginRequest   name of the login request, i.e. LoginRequest or LoginRequest22 -f tab size       formats the response XML to make it pretty (off by default)
```

## Lab Example

### Provision on AS

- Setup example if you want to push the request via the AS (172.16.30.127) and use BCCT (port 2220).

```
loginId - admin password - admin inputXMLFile - /Commands/pws_GroupAccessDeviceGetListRequest.xml host - 172.16.30.127 port - 2220 connection - BCCT
```

```
bwadmin@bwtaclab ASOCICLIENT]$ ./startASOCIClient.sh admin admin -i ./Commands/pws_GroupAccessDeviceGetListRequest.xml -h 172.16.30.127 -p 2220 -c BCCT **** OCI Client Build Version: 1.1.2 **** Start OCIClient initialization --> 2022.05.12 04:06:14:540 EDT **** Sending request at: 2022.05.12 04:06:14:566 EDT ==========> <?xml version="1.0" encoding="UTF-8"?> <BroadsoftDocument protocol = "OCI" xmlns="C" xmlns:xsi=" http://www.w3.org/2001/XMLSchema-instance "> <sessionId xmlns="">172.16.30.3,460141958,1652342774546</sessionId> <command xsi:type="LoginRequest22V3" xmlns=""> <userId>admin</userId> <password>admin</password> </command> </BroadsoftDocument> <========================== **** Received response (Request process time: 176 ms) ==========> <?xml version="1.0" encoding="UTF-8"?> <BroadsoftDocument protocol="OCI" xmlns="C" xmlns:xsi=" http://www.w3.org/2001/XMLSchema-instance "> <sessionId xmlns="">172.16.30.3,460141958,1652342774546</sessionId> <command echo="" xsi:type="LoginResponse22V3" xmlns=""> <loginType>System</loginType> <locale>en_US</locale> <encoding>ISO-8859-1</encoding> <isEnterprise>false</isEnterprise> <passwordExpiresDays>2147483647</passwordExpiresDays> <userDomain>calo.cisco.com</userDomain> <tokenRevocationTime>1616017564343</tokenRevocationTime> </command> </BroadsoftDocument> <========================== LoginRequest command successful **** Reading request(s) from file: ./Commands/pws_GroupAccessDeviceGetListRequest.xml **** Writing response to file: ./Commands/pws_GroupAccessDeviceGetListRequest.xml.response.xml **** Sending request from file: ./Commands/pws_GroupAccessDeviceGetListRequest.xml at: 2022.05.12 04:06:14:745 EDT ==========> <?xml version="1.0" encoding="ISO-8859-1"?> <BroadsoftDocument protocol="OCI" xmlns="C" xmlns:xsi=" http://www.w3.org/2001/XMLSchema-instance "> <sessionId xmlns="">172.16.30.3,460141958,1652342774546</sessionId> <command xsi:type="GroupAccessDeviceGetListRequest" xmlns=""> <serviceProviderId>pws_ent</serviceProviderId> <groupId>pws_grp</groupId> </command> </BroadsoftDocument> <========================== **** Received response (Request process time: 1304 ms) ==========> <?xml version="1.0" encoding="ISO-8859-1"?> <BroadsoftDocument protocol="OCI" xmlns="C" xmlns:xsi=" http://www.w3.org/2001/XMLSchema-instance "> <sessionId xmlns="">172.16.30.3,460141958,1652342774546</sessionId> <command echo="" xsi:type="GroupAccessDeviceGetListResponse" ....<snipped_response>...
```

### Provision on XSP/ADP

Setup exa m ple if you want to push the request via the XSP/ADP (172.16.30.71) and use OCS (port 2208).

```
loginId - admin password - admin inputXMLFile - /Commands/pws_GroupAccessDeviceGetListRequest.xml host - 172.16.30.71 port - 2208 connection - OCS
```

```
./startASOCIClient.sh admin admin -i ./Commands/pws_GroupAccessDeviceGetListRequest.xml -h 172.16.30.71 -p 2208 -c OCS
```

## Log Example

Log example for this request type seen from the PSLog.

```
2022.05.12 03:43:05:463 EDT | FieldDebug | Generic | BCCT Worker #1 OCI Transaction com.broadsoft.oci.transactions.group.GroupAccessDeviceGetListTransaction read38257 executed. User: Default Administrator (admin)   Authorization Level: System Start Time: 2022.05.12 03:43:03:616 EDT End Time:   2022.05.12 03:43:05:463 EDT Duration: 1847 ms
```

## Related Information

### Documentation

BW-ASProvisioningInterfaceSpec

### Software

Release Independant - Rel_2022_08_asociclient Release 24 - Rel_24_0_asociclient Release 23 - Rel_23_asociclient Relesse 22 - Rel_22_asociclient

### Revision History

1.0

27-Jan-2023

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 27-Jan-2023 | Initial Release |