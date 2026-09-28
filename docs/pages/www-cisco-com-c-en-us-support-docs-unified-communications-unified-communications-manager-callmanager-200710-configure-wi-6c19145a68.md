---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-200710-configure-wi-6c19145a68
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/200710-Configure-Wireless-Endpoint-Tracking-Fea.html
retrieved_at: 2026-08-21T13:55:38.561045+00:00
---

Configure Wireless Endpoint Tracking Feature on UCM 11.5.

# Configure Wireless Endpoint Tracking Feature on UCM 11.5.

### Download Options

Updated: October 6, 2016

Document ID: 200710

Contents

## Contents

## Introduction

This document describes the wireless endpoint tracking feature introduced in Cisco Unified Call Manager (CUCM) 11.5. By this feature CUCM will be able to track wireless endpoint's physical location and know the access point it is associated to. This information will then be pulled out by applications like Cisco Emergency Responder (CER) to track endpoint's physical location and route the call accordingly and make for a scalable solution.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Call Routing and C omputer Telephony Integration (CTI) Route Points

- Integrating CER with CUCM

- Configuring IP Phones on CUCM

### Components Used

The information in this document is based on these software versions:

- CUCM 11.5

- Cisco Wireless Controller Synchronization Service on CUCM

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

Traditionally CER routes the call based on calling device's IP address range and routing the call to the specific emergency department that belongs to the same IP block. This solution works well for wired endpoints as they are not mobile and their IP address defines their exact location. However, the problem arises with wireless endpoints as they will retain the IP address but are not bound to one specific physical location. This causes incorrect routing and hence requires a way to track wireless endpoint's physical location and make CUCM aware to which access point it is currently associated to so that this information can later be used by applications like CER for more efficient routing.

Currently this feature is available for these components:

1. CUCM 11.5 Release

2. 7925/7926 IP phones firmware 1.4.7.2 and above

Note: As of now, this feature is not supported for Jabber endpoints.

Note: Support for third party WLC and Access Points is not supported in CUCM 11.5 Release.

## Configure

There are two types of Deployment models for Access points:

1. Access Points managed by a Wireless LAN Controller (WLC):

In this deployement model, Access point information is pulled out by CUCM from WLC using SNMP v1/2c/3.

2. Standalone Access Point deployement:

In this deployement model Access point information needs to be manually updated in CUCM using Bulk Administration Tool (BAT).

Use the approriate section as per your deployement to configure the wireless endpoint tracking feature.

## 1. Access Points Managed by WLC

a.  Turn the feature on by selecting the option Cisco Wireless Controller Synchronisation service under Location

based Tracking Services from serviceability page of CUCM.

b.  Three Service parameters have been introduced for this feature which helps in SNMP attributes. These attributes must

match to the attributes configured under WLC as it will be used to pull up Access point information from WLC.

c. After you start the services and add SNMP details from a. and b., go ahead and add WLC details under: Wireless Access Point Controllers.

d. Add controller Hostname/IP and SNMP version /Community string details. Add the re-syncronization time and interval

under Synchronization Schedule.

e. Post these steps you will see that the Access point information is populated under the option Switches and Access Points.

f. Under every access point you will see access point details and the phones that are associated to it.

- Phones update CUCM with StationLocationInfo message to notify about the access point they are connected to.

Everytime the phone roams to a new Access Point or re-registers, CUCM is updated by the endpoint by a StationLocationInfo message notifying about the Access point it is now associated to.

## 2. Standalone Access Point Configuration

In case of a deployment where the access points are not controlled by a WLC, you can add Access point details manually by using BAT.

As of now, you do not have an option other than BAT to add Access point information manually into CUCM.

a. Create a CSV file that adheres to the these specifications and upload it to CUCM under the option: Bulk Administration > Upload/Download files.

Columns:

ACCESS POINT NAME,IPV4 ADDRESS,IPV6 ADDRESS,BSSID,DESCRIPTION Sample string defined:

```
ABC,10.77.29.28,FE80::0202:B3FF:FE1E:8329,11:1F:CA:83:82:F0,Bangalore |__||_________| |_______________________| |_______________| |_______| |      |                |                     |               | |      |                |                     |               | |      |                |                     |               WAPLocation can contain up to 63 characters. All characters except double quotes, backslash and non-printable characters. |      |                |                     | |      |                |                   BSSIDwithMask can contain from 1 to 20 characters. It can be formatted as needed but may only contain Hexadecimal digits (0-9, A-F), colons. |      |                | |      |              IPv6 address can contain from 1 to 50 characters. It can be formatted as needed but may only contain Hexadecimal digits (0-9, A-F), colons and dots. |      | |     IPv4 address can contain from 7 to 15 characters. It must be in dotted decimal format (digits and dots only) | Access Point Name(Can contain 1 to 63 characters. All characters except double quotes, backslash and non-printable characters.)
```

Instructions:

1. Either the IPv4, IPv6 or BSSID should be provided. They cannot all be empty, and you might provide more than one.

2. An IPv4 address, IPv6 address, or BSSID may be associated with only one infrastructure device. Two devices cannot have the same IP address or BSSID.

Note : If you use BAT.xlt to create the CSV files then there is no need to enclose the value in the quotes since the BAT.xlt automatically handles it.

2. Use the option Insert Infrastructure Device under Bulk Administration > Infrastructure Device.

3. Choose the CSV file and select the option Run immediately or Run later as per the requirement. If you choose to Run Later, ensure you use Job Scheduler page to schedule and activate the job.

4. Post these steps, Go to Advanced features > Device Location Tracking services > Switches and Access points to check if the device mentioned is added.

Note: Ensure the BSSID matches with the access point information as the phones send that information in the StationLocationInfo message and this is how CUCM maps the access points to the devices.

This is how CUCM maintains the wireless endpoints and tracks its physical location by mapping them to the access point been added manually or synchronized with a WLC.

## Log Analysis

This log analysis has been taken from a lab environment with a 2 node 11.5 UCM cluster and a 7925 phone that registers to the publisher node. There is a Access point been used which is controlled by a Wireless LAN controller using 802.11 b/g/n radio.

1. A StationLocationInfo message from the phone when it registers:

```
|09:54:41.102 |AppInfo |StationInit: (0005195) InboundStim - StationLocationInfoMessageID Line 2364: 23469039.000 |09:54:41.102 |SdlSig  |StationLocationInfo |restart0 |StationD(1,100,64,5195) |StationInit(1,100,63,1) |1,100,14,5210.26^10.105.132.116^SEP10F311B680E2 |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0] LocationInfo=A8:0C:0D:DB:C5:23test1111234test-7510-2702i Line 2364: 23469039.000 |09:54:41.102 |SdlSig |StationLocationInfo |restart0 |StationD(1,100,64,5195) |StationInit(1,100,63,1) |1,100,14,5210.26^10.105.132.116^SEP10F311B680E2 |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0] LocationInfo=A8:0C:0D:DB:C5:23test1111234Maib-7510-2702i
```

2. You see that this information is propogated by the phone when it registers or connects to a different access point:

- BSSID: A8:0C:0D:DB:C5:23

- SSID: test1111234

- AP Name: test-7510-2702i

3. The values are updated in the registrationdynamic table. The locationdetails column in registrationdynamic table is populated from infrastructuredevice table by referencing BSSID, SSID and AP Name. Once found it will populate thelocationdetails column in registrationdynamic with the PKID of the Access point. If the entry is not found, the locationdetails column will be entered as UNIDENTIFIED.

```
admin:run sql select * from registrationdynamic pkid                                 lastknownipaddress lastknownucm fkdevice datetimestamp lastknownconfigversion locationdetails tkendpointconnection portorssid   lastseen ==================================== ================== ============ ==================================== ============= ====================== ==================================== ==================== ============ ========== b366c291-bbd7-4464-b02c-e3f6d83c7cac 10.106.127.155 292a2ea3-dbee-43d7-9906-ff3dc42985a5 1449389815 0d30deab-febc-4f76-8fce-99a140978f18 2                    WLANPersonal 1449389815
```

```
admin:run sql select * from infrastructuredevice pkid                                 name       ipv4address    ipv6address bssidwithmask     waplocation       datetimestamp isactive ==================================== ========== ============== =========== ================= ================= ============= ======== 0d30deab-febc-4f76-8fce-99a140978f18 MAIB3502 10.105.132.111 NULL        24:b6:57:5a:b1:e0 Lab-BGL-14-Rack-K 1454041756    t
```

Note: fkdevice will be the PKID for the Wireless phone. This is how the wireless phone is associated with the Access point.

4. Once these tables are updated, the entry is updated in Switches and Access points under advanced features.

5. These entries are dynamic and are updated once the RegistrationDynamic table is updated.

An additional entry Lastseen is added to registrationdynamic that tells the last seen information of the wireless phone.

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

This section provides information you can use in order  to troubleshoot your configuration.

Compatibility

To start with it is essential to know the support for the feature on Wireless end points and the firmware version this has been included:

- 7925 and 7926 IP Phones with Firmware 1.4.7.2 and above is required for this feature

- As of now, Jabber end points are not supported by this feature

If the firmware version 1.4.7.2 is used, the phones would not be able to propogate the access point information to CUCM.

## Common Checkpoints to Troubleshoot

- If the phone is not associated with an Access point, check if the StationLocationInfo message is recieved by CUCM or not. Cross verify the phone model and firmware version used as well.

- Verify the exact Access point Name and BSSID and check if it is correctly configured (in case Access points are manually added).

- Cross verify if the Wireless LAN controller information is in sync and the status is shown as Successful. This can be checked by navigating to Advanced features > Device Location Tracking Services > Wireless LAN controllers.

- Cross verify the service parameters for SNMP attributes and ensure it matches with the Wireless LAN controller's SNMP attributes.

- Cross verify if Access Points are populated. This can be checked by navigating to Advanced features > Device Location Tracking Services > Switches and Access Points. If they are not populated, check the configuration on the LAN controller and ensure they are configured correctly.

## Logs to Collect

If the issue still persists, collect these logs for further scrutiny:

- Cisco CM traces set to detailed.

- Cisco Wireless Controller Syncronisation Service