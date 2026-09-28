---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-6901-6911-10-0-english-admin-guide-p691-bk-af85a164-00-admin-guide-69-cf95d1a373
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/6901_6911/10_0/english/admin_guide/P691_BK_AF85A164_00_admin-guide-6901-6911-10_0/P691_BK_AF85A164_00_admin-guide-6901-6911-10_0_chapter_011.html
retrieved_at: 2026-08-21T14:27:23.657020+00:00
---

Cisco Unified IP Phone 6901 and 6911 Administration Guide for Cisco Unified Communications Manager 10.0 (SCCP and SIP)

# Cisco Unified IP Phone 6901 and 6911 Administration Guide for Cisco Unified Communications Manager 10.0 (SCCP and SIP)

Updated: May 9, 2025

Chapter: Cisco Unified IP Phone Installation

## Chapter: Cisco Unified IP Phone Installation

# Cisco Unified IP Phone Installation

## Phone Installation Overview

This chapter helps you install the Cisco Unified IP Phone on an
                           		IP telephony network.

Before you install a Cisco Unified IP Phone, you must decide how to
                                       		  configure the phone in your network. Then you can install the phone and verify
                                       		  the  functionality. For more information, see Cisco Unified IP Phone and Telephony Networks .

## Before You Begin

Before installing the CiscoUnifiedIPPhone, review the requirements in the following sections.

### Network Requirements

For the CiscoUnified IP Phone to successfully operate as a
                              		CiscoUnified IP Phone endpoint in your network, your network must meet the
                              		following requirements:

VoIP network:

VoIP configured on your Cisco routers and gateways

CiscoUnifiedCommunications Manager installed in your network
                                          				  and configured to handle call processing

IP network that supports DHCP or manual assignment of IP address,
                                    			 gateway, and subnet mask

### Cisco Unified Communications Manager Setup

The CiscoUnifiedIPPhone requires
                              		CiscoUnifiedCommunications Manager to handle call processing. See Cisco UnifiedCommunications Manager Administration Guide or
                              		refer to the context-sensitive help in the CiscoUnifiedCommunications Manager
                              		application to ensure that CiscoUnifiedCommunications Manager is set up
                              		properly to manage the phone and to properly route and process calls.

If you plan to use autoregistration, verify that it is enabled
                              		and properly configured in Cisco Unified Communications Manager before
                              		connecting any CiscoUnifiedIPPhone to the network. For information about
                              		enabling and configuring autoregistration, see Cisco UnifiedCommunications Manager Administration Guide .

You must use CiscoUnifiedCommunications Manager
                              		Administration to configure and assign telephony features to the CiscoUnified
                              		IP Phones.

In CiscoUnifiedCommunications Manager Administration, you can
                              		add users to the database, add users to user groups, and associate users to
                              		specific phones. In this way, users gain access to  their Cisco Unified CM User
                              		Option page to configure items such as call forwarding, speed dialing, and
                              		voice messaging system options.

## Cisco Unified IP Phone 6901 and 6911 Components

The following sections describe the components and accessories for the Cisco Unified IP Phone 6901 and 6911.

### Network and Access Ports

The back of the CiscoUnified IP Phone 6901 includes a network
                              		port, which the phone uses to connect to the network.

The back of the CiscoUnified IP Phone 6911 includes these
                              		ports:

Network port: Labeled Network

Access port: Labeled Computer (also known as the PC port)

Only the Cisco Unified IP Phone 6911 has a PC port. The Cisco Unified IP Phone 6901 does not have a PC port.

The network port supports 10/100 megabits per second (Mb/s)
                              		half- or full-duplex connections to external devices. You can use either
                              		Category 3, 5, or 5e cabling for 10 Mbps connections, but you must use Category 5 or 5e
                              		for 100 Mb/s connections.

Use the network port to connect the phone to the network. You
                              		must use a straight-through cable on this port. The phone can also obtain
                              		inline power from a switch over this connection. For more information, see Cisco Unified Communications Manager Phone Addition Methods .

Use the PC access port to connect a network device, such as a
                              		computer, to the phone. You must use a straight-through cable on this port.

### Handset

The Cisco Unified IP Phone uses a handset that is designed especially for the phone. The handset includes a light strip to
                              indicate incoming calls and voice messages waiting.

To connect a handset to the CiscoUnified IP Phone, plug the cable into the handset and into the Handset port on the back of
                              the phone.

### Disable Speakerphone (Cisco Unified IP Phone 6911 Only)

By default, the speakerphone is enabled on the CiscoUnified
                                 		  IP Phone.

You can disable the speakerphone using CiscoUnified
                                 		  Communications Manager.

Step 1

Select Device > Phone .

Step 2

Select the phone you want to modify.

Step 3

In the 
                                          			 Phone Configuration window for the phone, check
                                          			 the Disable Speakerphone check box.

## Install Cisco Unified IP Phone

You must connect the CiscoUnified IP Phone to the network and to a power source before using it.

To install a Cisco Unified IP Phone, perform the following steps.

Step 1

Connect the handset to the Handset port.

Step 2

Connect the power supply to your phone. For guidelines, see Cisco Unified IP Phone Power for guidelines.

Step 3

Connect a straight-through Ethernet cable from the switch to the network port labeled Network on the Cisco Unified IP Phone 6901 and 6911 .

Each Cisco Unified IP Phone ships with one Ethernet cable in the box.

You can use either Category 3, 5, or 5e cabling for 10 Mbps connections, but you must use Category 5 or 5e for 100 Mbps connections.

Fr guidelines, see the Network and Access Ports .

Step 4

(Cisco Unified IP Phone 6911 only) Connect a straight-through Ethernet cable from another network device, such as a desktop
                                       computer, to the access port labeled Computer.

You can connect another network device later if you do not connect one now.

You can use either Category 3, 5, or 5e cabling for 10 Mbps connections, but you must use Category 5 or 5e for 100 Mbps connections.

For guidelines, see the Network and Access Ports .

### Cisco Unified IP Phone 6901 Installation

Use the diagram and table in Phone Connections to attach cables to
                              		the phone.

### Cisco Unified IP Phone 6911 Installation

Use the diagram and table in Phone Connections to attach cables to
                              		the phone.

### Phone Wall Mount

You can mount the CiscoUnified IP Phone 6901 on the wall
                              		using a standard telephone wall plate with an opening for an RJ-45 connector.
                              		Cisco recommends that you use Leviton Wall Mount plate (Leviton type number:
                              		4108W-0SP) to wall mount the CiscoUnified IP Phone 6901.

You can mount the CiscoUnified IP Phone 6911 on the wall
                              		using special brackets available in the CiscoUnified IP Phone wall mount kit.

The phone does not include wall mount kits. Wall mount kits must be ordered separately.

## Phone Startup Verification

The message waiting  (MWI) LED on the handset and the Mute button LED light during boot up. After successful completion of
                           the boot up process, the LEDs turn off, and the phone is ready for calls. If the phone successfully boots up, it has started
                           up properly. If the phone does not start up properly, the user receives a reorder tone.

## Network Settings

If you are not using DHCP in your network, you must configure the Cisco Unified IP Phone after installing the phone on the
                           network. You configure the following network settings:

IP address (IPv4)

IP subnet information

IPv6 address: you only configure the IPv6 address if the phone is in an IPv6 network. Other IPv6 parameters include the IPv6
                                 prefix, IPv6 default gateway, and IPv6 TFTP server.

Default Router

TFTP server IP address

Collect this information and see the instructions in Cisco Unified IP Phone Settings .

## Cisco Unified IP Phone Security

The security features protect against several threats,
                           		including threats to the identity of the phone and to data. These features
                           		establish and maintain authenticated communication streams between the phone
                           		and the CiscoUnifiedCommunications Manager server, and digitally sign files
                           		before they are delivered.

For more information about the security features, see the
                           		related topics and the Cisco UnifiedCommunications Manager Security Guide .

### Locally Significant Certificate Manual Setup

You initiate the installation of a locally significant
                              		certificate (LSC) from the Security Configuration menu on the phone. This menu
                              		also lets you update or remove an LSC.

#### Before You Begin

Make sure that the appropriate CiscoUnified Communications
                              		Manager and the Certificate Authority Proxy Function (CAPF) security
                              		configurations are complete:

The CTL file should have a CAPF certificate.

On Cisco Unified Communications Operating System Administration,
                                    			 verify that the CAPF certificate has been installed.

The CAPF is running and configured.

For more information, see Cisco Unified Communications Manager Security Guide .

| Note | Before you install a Cisco Unified IP Phone, you must decide how to
                                       		  configure the phone in your network. Then you can install the phone and verify
                                       		  the  functionality. For more information, see Cisco Unified IP Phone and Telephony Networks . |
|---|---|

| Note | The CiscoUnified IP Phone displays the date and time from Cisco
                                       		Unified Communications Manager. The time displayed on the phone can differ from the Cisco Unified Communications Manager
                                       time by up to 10 seconds. If the Cisco Unified Communications Manager
                                       		server is located in a different time zone than the phones, the phones do not
                                       		display the correct localtime. |
|---|---|

| Note | Only the Cisco Unified IP Phone 6911 has a PC port. The Cisco Unified IP Phone 6901 does not have a PC port. |
|---|---|

| Step 1 | Select Device > Phone . |
|---|---|
| Step 2 | Select the phone you want to modify. |
| Step 3 | In the 
                                          			 Phone Configuration window for the phone, check
                                          			 the Disable Speakerphone check box. |

| Step 1 | Connect the handset to the Handset port. |
|---|---|
| Step 2 | Connect the power supply to your phone. For guidelines, see Cisco Unified IP Phone Power for guidelines. |
| Step 3 | Connect a straight-through Ethernet cable from the switch to the network port labeled Network on the Cisco Unified IP Phone 6901 and 6911 . Each Cisco Unified IP Phone ships with one Ethernet cable in the box. You can use either Category 3, 5, or 5e cabling for 10 Mbps connections, but you must use Category 5 or 5e for 100 Mbps connections. Fr guidelines, see the Network and Access Ports . |
| Step 4 | (Cisco Unified IP Phone 6911 only) Connect a straight-through Ethernet cable from another network device, such as a desktop
                                       computer, to the access port labeled Computer. You can connect another network device later if you do not connect one now. You can use either Category 3, 5, or 5e cabling for 10 Mbps connections, but you must use Category 5 or 5e for 100 Mbps connections. For guidelines, see the Network and Access Ports . |

| Note | The phone does not include wall mount kits. Wall mount kits must be ordered separately. |
|---|---|