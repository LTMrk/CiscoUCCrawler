---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-common-ag-desk-mpp-6800-7800-8800-tpcc-b-cisco-ip-desk-phone-mult-857503dcfb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/common/ag_desk_mpp_6800_7800_8800/tpcc_b_cisco-ip-desk-phone-multiplatform/p881_m_monitoring-phone-systems-1131.html
retrieved_at: 2026-08-21T13:47:22.231729+00:00
---

Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

# Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

Updated: November 19, 2025

Chapter: Monitoring Phone Systems

## Chapter: Monitoring Phone Systems

# Monitoring Phone Systems

## Monitoring Phone Systems Overview

You can view a variety of information about the phone using the phone status menu on the phone and the phone web pages. This
                              information includes:

Device information

Network setup information

Network statistics

Device logs

Streaming statistics

This chapter describes the information that you can obtain from the phone web page. You can use this information to remotely
                              monitor the operation of a phone and to assist with troubleshooting.

## Cisco IP Phone Status

The following sections describes how to view model information, status messages, and network statistics on the Cisco IP Phone.

Model Information: Displays hardware and software
                                    			 information about the phone.

Status menu: Provides access to screens that display the status
                                    			 messages, network statistics, and statistics for the current call.

You can use the information that displays on these screens to
                              		monitor the operation of a phone and to assist with troubleshooting.

You can also obtain much of this information, and obtain other
                              		related information, remotely through the phone web page.

### Display the Phone Information Window

Step 1

Press Applications .

Step 2

Select Phone Information .

When a user password is set, a corresponding icon (lock or certificate) displays at the top-right corner of the phone screen.

Step 3

To exit the Model Information screen, press Exit .

### View Phone Information

To check the current status of the Cisco IP Phone, click the Info tab.

The Info tab shows information about all phone extensions, including phone statistics and the registration status.

### View the Phone Status

Step 1

Press Applications .

Step 2

Select Status > Phone status > Phone status .

You can view the following information:

Elapsed time —Total time elapsed since the last reboot of the system

Tx (Packets) —Transmitted packets from the phone.

Rx (Packets) —Received packets from the phone.

### View Download Status

You can view the download status from the phone web page when your user has difficulties with phone registration.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Info > Download Status .

Step 2

View the firmware upgrade, provisioning, and custom CA status details as described in the Firmware Upgrade Status , Provisioning Status , Custom CA Status , and Screen Status .

Step 3

View the Manufacture Installed Certificate (MIC) renewal status details in the MIC Cert Refresh Status section.

### Determine the IP Address of the Phone

A DHCP server assigns the IP address, so the phone must be booted up and connected to the subnetwork.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Info > Status .

Step 2

Scroll to IPv4 Information . Current IP displays the IP address.

Step 3

Scroll to IPv6 Information . Current IP displays the IP address.

### Voice Quality
                           	 Monitoring

To
                                 		  measure the voice quality of calls that are sent and received within the
                                 		  network, Cisco IP Phones use these statistical metrics that are based on
                                 		  concealment events. The DSP plays concealment frames to mask frame loss in the
                                 		  voice packet stream.

Concealment Ratio metrics—Show the ratio of concealment frames over total speech frames. An interval conceal ratio is calculated
                                       every 3 seconds.

Concealed Second metrics—Show the number of seconds in which the DSP plays concealment frames due to lost frames. A severely "concealed second" is a second in which the DSP plays more than five percent concealment frames.

Concealment
                                             			 ratio and concealment seconds are primary measurements based on frame loss. A
                                             			 Conceal Ratio of zero indicates that the IP network is delivering frames and
                                             			 packets on time with no loss.

You can
                                 		  access voice quality metrics from the Cisco IP Phone using the Call Statistics
                                 		  screen or remotely by using Streaming Statistics.

### Display Call Statistics Screen

You can access the Call statistics menu on the phone to display detailed information of the recent calls. For example, call type, caller name, caller number.

Step 1

Press Applications .

Step 2

Select Admin Settings > Status > Call Statistics .

Step 3

To exit the Status menu, press Back .

#### Call Statistics Fields

The following table describes the items on the Call Statistics screen.

Item

Description

Call type

Peer name

The name of the person who made or answered the call.

Peer phone

The phone number of the person who made or answered the call.

Encode codec

The method used to compress the outgoing audio.

Decode codec

The method used to decompress the incoming audio.

Call time

The time a call was made or answered.

Call ID

An identifier of the caller.

## Reboot Reasons

The phone stores the most recent five reasons that the phone was refreshed or rebooted. When the phone is reset to factory
                              defaults, this information is deleted.

The following table describes the reboot and refresh reasons for the Cisco IP Phone.

Reason

Description

Upgrade

The reboot was a result of an upgrade operation (regardless whether the upgrade completed or failed).

Provisioning

The reboot was the result of changes made to parameter values by using the IP phone screen or phone web user interface, or
                                          as a result of synchronization.

SIP Triggered

The reboot was triggered by a SIP request.

RC

The reboot was triggered as a result of remote customization.

User Triggered

The user manually triggered a cold reboot.

IP Changed

The reboot was triggered after the phone IP address changed.

You can view the reboot history as follows:

From the phone web user interface

From the IP phone screen

From the phone Status Dump file (http:// phoneIP /status.xml or http:// phoneIP /admin/status.xml)

### Reboot History on the Phone Web User Interface

On the Info > System Status page, the Reboot History section displays the device reboot history, the five most recent reboot dates and times, and a reason for the reboot. Each
                                 field displays the reason for the reboot and a time stamp that indicates when the reboot took place.

For example:

```
Reboot Reason 1: [08/13/14 06:12:38] User Triggered
Reboot Reason 2: [08/10/14 10:30:10] Provisioning
Reboot Reason 3: [08/10/14 10:28:20] Upgrade
```

The reboot history displays in reverse chronological order; the reason for the most recent reboot displays in Reboot Reason 1 .

### Reboot History on the Cisco IP Phone Screen

Reboot History is located under Apps > Admin Settings > Status menu. In the Reboot History window, the reboot entries displays in reverse chronological order, similar to the sequence that
                                 displays on the phone web user interface.

### Reboot History in the Status Dump File

The reboot history is stored in the Status Dump file  (http:// <phone_IP_address> /admin/status.xml).

In this file, tags Reboot_Reason_1 to Reboot_Reason_3 store the reboot history, as shown in this example:

```
<Reboot_History>
<Reboot_Reason_1>[08/10/14 14:03:43]Provisioning</Reboot_Reason_1>
<Reboot_Reason_2>[08/10/14 13:58:15]Provisioning</Reboot_Reason_2>
<Reboot_Reason_3>[08/10/14 12:08:58]Provisioning</Reboot_Reason_3>
<Reboot_Reason_4>
<Reboot_Reason_5>
<Reboot_History/>
```

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Phone Information . When a user password is set, a corresponding icon (lock or certificate) displays at the top-right corner of the phone screen. |
| Step 3 | To exit the Model Information screen, press Exit . |

| To check the current status of the Cisco IP Phone, click the Info tab. The Info tab shows information about all phone extensions, including phone statistics and the registration status. |
|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Status > Phone status > Phone status . You can view the following information: Elapsed time —Total time elapsed since the last reboot of the system Tx (Packets) —Transmitted packets from the phone. Rx (Packets) —Received packets from the phone. |

| Step 1 | Select Info > Download Status . |
|---|---|
| Step 2 | View the firmware upgrade, provisioning, and custom CA status details as described in the Firmware Upgrade Status , Provisioning Status , Custom CA Status , and Screen Status . |
| Step 3 | View the Manufacture Installed Certificate (MIC) renewal status details in the MIC Cert Refresh Status section. |

| Step 1 | Select Info > Status . |
|---|---|
| Step 2 | Scroll to IPv4 Information . Current IP displays the IP address. |
| Step 3 | Scroll to IPv6 Information . Current IP displays the IP address. |

| Note | Concealment
                                             			 ratio and concealment seconds are primary measurements based on frame loss. A
                                             			 Conceal Ratio of zero indicates that the IP network is delivering frames and
                                             			 packets on time with no loss. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Admin Settings > Status > Call Statistics . |
| Step 3 | To exit the Status menu, press Back . |

| Item | Description |
|---|---|
| Call type | An outbound or inbound call. |
| Peer name | The name of the person who made or answered the call. |
| Peer phone | The phone number of the person who made or answered the call. |
| Encode codec | The method used to compress the outgoing audio. |
| Decode codec | The method used to decompress the incoming audio. |
| Call time | The time a call was made or answered. |
| Call ID | An identifier of the caller. |

| Reason | Description |
|---|---|
| Upgrade | The reboot was a result of an upgrade operation (regardless whether the upgrade completed or failed). |
| Provisioning | The reboot was the result of changes made to parameter values by using the IP phone screen or phone web user interface, or
                                          as a result of synchronization. |
| SIP Triggered | The reboot was triggered by a SIP request. |
| RC | The reboot was triggered as a result of remote customization. |
| User Triggered | The user manually triggered a cold reboot. |
| IP Changed | The reboot was triggered after the phone IP address changed. |