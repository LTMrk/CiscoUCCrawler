---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-trouble-12-5-1-cucm-b-troubleshooting-guide-1251-cucm-b-troubleshooting-ce10b804c6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/trouble/12_5_1/cucm_b_troubleshooting-guide-1251/cucm_b_troubleshooting-guide-1251_chapter_0110.html
retrieved_at: 2026-08-16T18:15:40.344780+00:00
---

Troubleshooting Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Troubleshooting Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: November 24, 2023

Chapter: Cisco Unified Communications Manager Services Issues

## Chapter: Cisco Unified Communications Manager Services Issues

# Cisco Unified Communications Manager Services Issues

This section covers the solutions for the most common issues that relate to Unified Communications Manager services.

## No Available
                        	 Conference Bridge

### Symptom

The
                              		  following message displays: No Conference Bridge Available.

### Possible
                              		  Cause

This could
                              		  indicate either a software or a hardware problem.

### Recommended
                              		  Action

Check to see whether you have any available software or hardware conference bridge resources that are registered with Unified Communications Manager .

Use the Unified Communications Manager Cisco Unified Real-Time Monitoring Tool to check the number of Unicast AvailableConferences.

The Cisco IP
                                    				Voice Media Streaming application performs the conference bridge function. One
                                    				software installation of Cisco IP Voice Media Streaming will support 16 Unicast
                                    				Available Conferences (three people/conference), as shown in the following
                                    				trace.

The number of supported devices may vary with different Unified Communications Manager releases. Refer to the appropriate version of Unified Communications Manager documentation at the following location:

http://www.cisco.com/en/US/products/sw/voicesw/ps556/products_documentation_roadmaps_list.html

```
10:59:29.951 CCM CallManager|UnicastBridgeControl - wait_capabilities_StationCapRes - Device= CFB_kirribilli - Registered - ConfBridges= 16, Streams= 48, tcpHandle=4f12738 10:59:29.951 CCM CallManager|UnicastBridgeManager - UnicastBridgeRegistrationReq - Device Registration Complete for Name= Xoð ô%ð - DeviceType= 50, ResourcesAvailable= 16, deviceTblIndex= 0
```

One E1 port
                                    				(WS-X6608-E1 card contains 8x E1 ports) provides five Unicast Available
                                    				Conferences (max conference size = 6), as shown in the following trace.

```
11:14:05.390 CCM CallManager|UnicastBridgeControl - wait_capabilities_StationCapRes - Device= CFB00107B000FB0 - Registered - ConfBridges= 5, Streams= 16, tcpHandle=4f19d64 11:14:05.480 CCM CallManager|UnicastBridgeManager - UnicastBridgeRegistrationReq - Device Registration Complete for Name= Xoð ô%ð - DeviceType= 51, ResourcesAvailable= 5, deviceTblIndex= 0
```

The following hardware trace on the Cisco Catalyst 6000 8 Port Voice T1/E1 and Services Module indicates that the E1 port
                                    4/1 in the card registered as a Conference Bridge with Unified Communications Manager .

```
greece-sup (enable) sh port 4/1Port  Name               Status     Vlan       Duplex Speed Type
----- ------------------ ---------- ---------- ------ ----- ----------
 4/1                     enabled    1            full     -Conf Bridge
 
Port     DHCP    MAC-Address       IP-Address      Subnet-Mask
-------- ------- ----------------- --------------- ---------------
 4/1     disable 00-10-7b-00-0f-b0 10.200.72.31    255.255.255.0   
 
Port     Call-Manager(s)   DHCP-Server     TFTP-Server     Gateway
-------- ----------------- --------------- --------------- -----------
 4/1     10.200.72.25      -               10.200.72.25    -               
 
Port     DNS-Server(s)     Domain
-------- ----------------- -------------------------------------------
 4/1     -                 0.0.0.0
 
Port     CallManagerState DSP-Type
-------- ---------------- --------
4/1     registered       C549
 
Port  NoiseRegen NonLinearProcessing
----- ---------- -------------------
 4/1  disabled   disabled
```

Check the
                                    				maximum number of users that are configured in your ad hoc or meet-me
                                    				conference to determine whether the problem occurred because this number was
                                    				exceeded.

Check the setting of the Audio Bandwidth field on the Location Configuration window. If the call bandwidth exceeds this configured
                                    limit, the conferencing fails. To resolve this issue, choose the Unlimited Bandwidth radio button. For more information on
                                    the Location Configuration window, refer to the System Configuration Guide for Cisco Unified Communications Manager .

## Hardware Transcoder Not Working As Expected

You have installed a hardware transcoder in the Cisco Catalyst 6000 8 Port Voice T1/E1 and Services Module, and it does not
                           work as expected (you cannot make calls between two users with no common codec).

Possible Cause

You may not have any available transcoder resources that are registered with Unified Communications Manager (must be hardware).

Recommended Action

Use the Unified Communications Manager Cisco Unified Real-Time Monitoring Tool to check the number of available resources by viewing the ResourceAvailable counter
                           in the Cisco MTP Device object.

One E1 port (WS-X6608-E1 card contains 8x E1 ports) provides transcoder/MTP resources for 16 calls, as shown in the following
                           trace.

The number of supported devices may vary with different Unified Communications Manager releases. Refer to the appropriate version of Unified Communications Manager documentation at the following location: http://www.cisco.com/en/US/products/sw/voicesw/ps556/products_documentation_roadmaps_list.html

```
11:51:09.939 CCM CallManager|MediaTerminationPointControl - Capabilities Received - Device= MTP00107B000FB1 - Registered - Supports 16 calls
```

The following hardware trace on the Cisco Catalyst 6000 8 Port Voice T1/E1 and Services Module indicates that the E1 port
                           4/2 in the card registered as an MTP/transcoder with Unified Communications Manager .

```
greece-sup (enable) sh port 4/2Port  Name               Status     Vlan       Duplex Speed Type
----- ------------------ ---------- ---------- ------ ----- ----------
 4/2                     enabled    1            full     - MTP
 
Port     DHCP    MAC-Address       IP-Address      Subnet-Mask
-------- ------- ----------------- --------------- ---------------
 4/2     disable 00-10-7b-00-0f-b1 10.200.72.32    255.255.255.0   
 
Port     Call-Manager(s)   DHCP-Server     TFTP-Server     Gateway
-------- ----------------- --------------- --------------- -----------
 4/2     10.200.72.25      -               10.200.72.25    -               
 
Port     DNS-Server(s)     Domain
-------- ----------------- -------------------------------------------
 4/2     -                 0.0.0.0
 
Port     CallManagerState DSP-Type
-------- ---------------- --------
 4/2     registered       C549
 
Port  NoiseRegen NonLinearProcessing
----- ---------- -------------------
 4/2  disabled   disabled
```

You cannot configure the same E1 port for both Conference Bridge and Transcoder/MTP

To make a call between two devices that are using a low bit rate code (such as G.729 and G.723) that do not support the same
                           codec, you need a transcoder resource.

Assume Unified Communications Manager has been configured such that the codec between Region1 and Region2 is G.729. The following scenarios apply:

If caller on Phone A initiates a call, Unified Communications Manager realizes it is a Cisco Unified IP Phone model 7960, which supports G.729. After the digits are collected, the Unified Communications Manager determines that the call is destined for User D who is in Region2. Because the destination device also supports G.729, the
                                 call gets set up, and the audio flows directly between Phone A and Phone D.

If a caller on Phone B, initiates a call to Phone D, this time the Unified Communications Manager would realize that the originating phone only supports G.723 or G.711. Unified Communications Manager would need to allocate a transcoding resource so audio would flow as G.711 between Phone B and the transcoder but as G.729
                                 between the transcoder and Phone D. If no transcoder were available, Phone D would ring, but as soon as the call was answered,
                                 the call would disconnect.

If a user on Phone B calls Phone F, the two phones would actually use G.723, even though G.729 is configured as the codec
                                 to use between the regions. G.723 gets used because both endpoints support it, and it uses less bandwidth than G.729.

## No Supplementary Services Are Available on an Established Call

### Symptom

A call gets established, but supplementary services are not available.

### Possible 
                              
                              Cause

An MTP resource problem could provide the source of the transcoding problem if a call is established, but supplementary services
                              are not available on an H.323 device that does not support H323v2.

### Recommended 
                              
                              Action

Determine whether you have any available software or hardware MTP resources that are registered with Unified Communications Manager .

Use Performance monitoring in the Unified Communications Manager Cisco Unified Real-Time Monitoring Tool to check the number of MTP devices available.

Using MTP to support supplementary services with H.323 devices that do not support H.323v2 allows one MTP software application
                                    to support 24 calls as shown in the following trace.

The number of supported devices may vary with different Unified Communications Manager releases. Refer to the appropriate version of Unified Communications Manager documentation at the following location:

http://www.cisco.com/en/US/products/sw/voicesw/ps556/products_documentation_roadmaps_list.html

```
10:12:19.161 CCM CallManager|MediaTerminationPointControl - Capabilities Received - Device= MTP_kirribilli. - Registered - Supports 24 calls
```

One E1 port (WS-X6608-E1 card contains 8x E1 ports) provides MTP resources for 16 calls, as shown in the following trace.

```
11:51:09.939 CCM CallManager|MediaTerminationPointControl - Capabilities Received - Device= MTP00107B000FB1 - Registered - Supports 16 calls
```

The following hardware trace from the Cisco Catalyst 6000 8 Port Voice T1/E1 and Services Module indicates that the E1 port
                                    4/2 in the card has registered as an MTP/transcoder with Unified Communications Manager .

```
greece-sup (enable) sh port 4/2Port  Name               Status     Vlan       Duplex Speed Type
----- ------------------ ---------- ---------- ------ ----- ----------
 4/2                     enabled    1            full     - MTP
 
Port     DHCP    MAC-Address       IP-Address      Subnet-Mask
-------- ------- ----------------- --------------- ---------------
 4/2     disable 00-10-7b-00-0f-b1 10.200.72.32    255.255.255.0   
 
Port     Call-Manager(s)   DHCP-Server     TFTP-Server     Gateway
-------- ----------------- --------------- --------------- -----------
 4/2     10.200.72.25      -               10.200.72.25    -               
 
Port     DNS-Server(s)     Domain
-------- ----------------- -------------------------------------------
 4/2     -                 0.0.0.0
 
Port     CallManagerState DSP-Type
-------- ---------------- --------
 4/2     registered       C549
 
Port  NoiseRegen NonLinearProcessing
----- ---------- -------------------
 4/2  disabled   disabled
```

In the Gateway Configuration window of Cisco Unified Communications Manager Administration , check to see whether the Media Termination Point Required check box is checked.

Verify that Unified Communications Manager allocated the required number of MTP devices.

| Note | The number of supported devices may vary with different Unified Communications Manager releases. Refer to the appropriate version of Unified Communications Manager documentation at the following location: http://www.cisco.com/en/US/products/sw/voicesw/ps556/products_documentation_roadmaps_list.html |
|---|---|

| Note | The number of supported devices may vary with different Unified Communications Manager releases. Refer to the appropriate version of Unified Communications Manager documentation at the following location: http://www.cisco.com/en/US/products/sw/voicesw/ps556/products_documentation_roadmaps_list.html |
|---|---|

| Note | You cannot configure the same E1 port for both Conference Bridge and Transcoder/MTP |
|---|---|

| Note | The number of supported devices may vary with different Unified Communications Manager releases. Refer to the appropriate version of Unified Communications Manager documentation at the following location: http://www.cisco.com/en/US/products/sw/voicesw/ps556/products_documentation_roadmaps_list.html |
|---|---|