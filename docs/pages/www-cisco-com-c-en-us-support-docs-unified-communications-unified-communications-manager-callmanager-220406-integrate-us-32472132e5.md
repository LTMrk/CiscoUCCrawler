---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-220406-integrate-us-32472132e5
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/220406-integrate-users-from-cucm-to-unity-conne.html
retrieved_at: 2026-08-21T13:59:50.031624+00:00
---

Integrate Users from CUCM to Unity Connection with AXL

# Integrate Users from CUCM to Unity Connection with AXL

Updated: April 20, 2023

Document ID: 220406

Contents

## Contents

## Introduction

This document describes how to add users from Cisco Unified Communications Manager (CUCM) to Unity Connection with AXL.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CUCM

- Unity Integration.

### Components Used

The information in this document is based on these software and hardware versions:

- CUC

- CUCM

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

To configure, create an application user and add the Standard AXL API Access Role to it.

You can create a new Access Group and add only the AXL API Access role to avoid interference with other applications and have a specific user and Access Group for this task.

Log into CUCM:

- Navigate to User Management > User Settings > Access Control Group .

- Click on add new, name the Group and click on save.

- Click on Related Links and select Assign Role to Access Control Group and click Go .

- Click on Assign Role to Group and select the Standard AXL API Access Role , click Add selected then save.

- Navigate to User Management > Application User and click Add New , set the user ID and the password. Click Add to Access Control Group and select the one created previously.

- Navigate to System > Application Server .

7. Click on Add New and create a new application server. Select the type of server, in this case use Cisco Unity Connection , and click Next .

- Name the application server, type the CUC IP address and add the application user that you created previously.

Configure the unity server:

- Navigate to your Phone System and select the desired one.

- Then Navigate to Edit and select Cisco Unified Communication Manager AXL servers.

- Type the IP address of the CUCM server you specified on the Application Server in CUCM, set the port as 8443 and the application user and password that you created in CUCM, click Test to check the connectivity and then Save .

4. Navigate to Import Users > Select your Phone System and click on Find , the users to be imported can be listed in there (ensure that the end user in CUCM has assigned a device as well as a primary extension otherwise the user cannot be listed).

5. Once the uses are listed, select the checkbox next to them and click on Import Selected .

6. Click on Users at the left side to check the newly imported ones.

## Troubleshoot

To troubleshoot the configurations:

- Make sure the AXL web service runs on CUCM.

- As mentioned before ensure users have a primary extension assigned. This field in found in CUCM under User Management > End User > . From there select the user and look for the Primary Extension option. This field is populated when the user is set to control the phone it uses.

- To continue to troubleshoot, you can gather the Cisco AXL Web Service logs via RTMT for CUCM and Tomcat logs for Unity connection,

- For AXL messages to show up on the Tomcat Unity logs you need to Navigate to Cisco Unity Connection Serviceability > Trace > Micro and choose AXL access .Then enable all levels.

Log Samples

Error Failed to send message to remote AXL server. Please check error log for more details appears when you try to test connection AXL connection to CUCM;

You can enable th trace AXL Access on Unity as mentioned previously and get the Tomcat logs. This error can lead to an authentication issue and you can see the next error on the logs:

[ParamFilteredRequest]: getParameterNames(); Collections[op, org.apache.struts.taglib.html.TOKEN, axlRemoteServices[0].precedence, axlRemoteServices[0].hostOrIPAddress, axlRemoteServices[0].port, axlRemoteServices[0].objectId, ccmAXLUser, encryptedAxlPassword, ccmVersion, ignoreAxlCertErr, objectId, axlRemoteServicesCount]

Apr 21, 2017 2:56:16 PM com.sun.xml.internal.messaging.saaj.client.p2p.HttpSOAPConnection post

SEVERE: SAAJ0008: Bad Response; Unauthorized

This error is caused due to an incorrect password or a password with special characters that the system does not accept:

- Error Error encountered. Check the Application Server Settings on CUCM for CUC shows up when you try to import the users.

Ensure the IP address you set on the application server in CUCM is the Unity connection IP address.

Useful Bugs

Cisco bug ID CSCug64397 — CUCM 10.0 AXL backward compatibility with Unity Connection

Cisco bug ID CSCuo97876 — CUC 9.X, AXL integration fails with CUCM 7.X

Note : Only registered Cisco users can access internal Cisco tools and information.

## Related Information

- Cisco Technical Support & Downloads

### Revision History

1.0

20-Apr-2023

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 20-Apr-2023 | Initial Release |