---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unity-connection-200852-configuration-example-for-cucm-non-sec-cad3769c4b
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-connection/200852-Configuration-Example-for-CUCM-non-secur.html
retrieved_at: 2026-08-19T00:10:43.938901+00:00
---

Configuration Example for CUCM Non-Secure SCCP Integration with CUC

# Configuration Example for CUCM Non-Secure SCCP Integration with CUC

### Download Options

Updated: February 21, 2017

Document ID: 200852

Contents

## Contents

## Introduction

This document describes the procedure to integrate Cisco Unified Communication Manager (CUCM) with Cisco Unity Connection (CUC) with the use of Skinny Call Control Protocol (SCCP). In this example, the SCCP integration is non-secure.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CUCM

- CUC

### Components Used

The information in this document is based on these software and hardware versions:

- CUCM 8.x and higher

- CUC 8.x and higher

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

### Configuration on CUCM

CUCM has an inbuilt wizard to create ports for Unity Connection. Complete these steps in order to create ports on CUCM:

Step 1. On CUCM Administration page, navigate to Advanced Features > Voicemail > Cisco Voice Mail Port Wizard.

Step 2. Choose a device name. The default is CiscoUM1 .

Note : Use the same device name on Unity Connection. CUCM appends '-VI' along with the port number. For example, CiscoUM1-VI1, CiscoUM1-VI2, etc. On Unity Connection, configure device name as CiscoUM1-VI . CUC does not append '-VI' to the device name.

Step 3. From the drop down menu, select the number of ports. Unity Connection can handle up to 255 ports on a single server.

Note : Unity Connection 8.x requires port license. Select the number of ports here based on the available ports in Unity Connection license.

Note : Unity Connection 9.x and higher does not have port license. The maximum number of ports depends on the hardware (Physical & Virtual Machine (VM)) configuration. Refer to the Unity Connection Supported Platforms List document. For a VM, the OVA template number of Users option determines the available ports on Unity Connection. Select the number of ports here based on the Unity Connection hardware configuration.

Step 4. Provide the Device Information such as Description, Device Pool, Calling Search Space and Location . Set Device Security Profile to Non Secure Voice Mail Port.

Step 5. Enter the directory number of the first port. The port number of the subsequent ports increments by one. For example, the Beginning Directory Number is set to 2001. The port numbers are 2001 to 2005. Assign an appropriate Partition and Calling Search Space .

Step 6. Select the appropriate option on the next page. In the example, this is a new integration and a Line Group does not exist. Select Yes. Add directory numbers to a new Line Group.

Step 7. Provide a Line Group name.

Step 8. The next page provides a summary of the configuration provided in the previous steps. If there are any issues, go back to the previous page and make changes. Click Finish after verification.

Step 9. The port creation result shows on the next page.

Step 10. Add the Line Group to a Hunt List. Click on the Hunt List option to create a new Hunt List or choose an existing one. Add the Line Group CiscoUM1-LG to the Hunt List Unity-HL . On the Hunt List enable the two options as shown in the image.

Step 11. Configure a Hunt Pilot number. Either go to the wizard and click on Hunt Pilot or navigate to Call Routing > Route/Hunt > Hunt Pilot to create a Hunt Pilot. Select the Hunt List Unity-HL from the drop down list.

Step 12. Configure a Voicemail Pilot number. The VM Pilot number is same as the Hunt Pilot number. Navigate to Advanced Features > Voicemail > Voicemail Pilot to add a new VM Pilot number.  Users can dial the VM Pilot / Hunt Pilot number to reach Unity Connection.

Step 13. Configure a Voicemail Profile. The VM Pilot is associated with the VM Profile. Navigate to Advanced Features > Voicemail > Voicemail Profile to add a new VM Profile. The VM Profile is associated with a Line Directory Number (DN) on a user's phone. Users can press the message button on the phone to reach Unity Connection.

Step 14. Configure Message Waiting Indicator (MWI) On and Off number. Navigate to Advanced Features > Voicemail > Message Waiting to create MWI numbers.

### Configuration on Cisco Unity Connection

Complete these steps in order to create ports on CUC:

Step 1. On CUC Administration page, navigate to Telephony Integrations > Phone System . Click Add and provide a Phone System name.

Step 2. The defaults are used on the Phone System Basics page. In order to view information about the additional configuration for the Phone System, navigate to Help > This page.

Step 3. [Optional] In order to import CUCM users to CUC, configure AXL servers on the Phone System. Navigate to Edit > Cisco Unified Communications Manager AXL server .

Add the CUCM Publisher and the Subscribers that run the AXL service. Use port 8443/443. The username is an application user (on CUCM) with AXL roles assigned to it. In this example, the CUCM Admin user is used. This user has all the roles by default.

Step 4. Navigate back to the Phone System basic page. On the top right corner, select Add a Port Group from the related links menu.

Step 5. Create a Port Group. Provide a Display Name for the Port Group. The Device Prefix here should match the name of the Voice Mail server provided in Step 3. of the CUCM configuration with a suffix of VI. In this example, the Voice Mail server name is CiscoUM1 on CUCM. On CUC, the Device Prefix is CiscoUM1-VI.

Step 6. Provide the MWI On and Off numbers. The MWI numbers on CUCM and CUC match.

Step 7. Provide the CUCM Publisher’s IP address/Hostname in the IPv4 address or Host Name field and click Save .

Step 8 . Navigate to Edit > Server on the same page and add the additional CUCM servers in the same cluster for failover. Assign a preference with the help of Order number. Order 0 has highest preference followed by 1, 2 and so on. The ports register to the CUCM server with Order 0. If this server is not available, the ports register to the subsequent servers in the list.

Check the Reconnect to a Higher-Order Cisco Unified Communications Manager When Available for the ports to fall back to the higher order CUCM server once it becomes available. Otherwise, the ports remain registered to the lower preference server.

Step 9. Navigate to Add Ports from the Related Links menu on the top right corner.

Step 10. Configure number of ports. This matches the ports on CUCM.

Step 11. Select the appropriate Phone System , Port Group and Server.

Note : From the Server drop down menu, select the Publisher CUC server and create ports. To add ports for the Subscriber CUC server, navigate to the same Port Group SCCP-PortGroup and choose Add Ports from the Related Links menu on the top right corner. On the New Phone System Port page, choose the Subscriber server from the Server drop down menu. With this method, both Publisher and Subscriber Unity ports register with the same Device Name prefix. Alternatively, create a new port group in the same Phone System with a different device name prefix for the Subscriber ports.

## Verify

Use this section to confirm that your configuration works properly.

On CUCM Administration page, navigate to Advanced feature > Voicemail > Voicemail Ports to confirm port registration.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

1.0

10-Nov-2016

Initial Release

### Contributed by Cisco Engineers

Antara Sargam

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager (CallManager)

- Unity Connection

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 10-Nov-2016 | Initial Release |