---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-6901-6911-10-0-english-admin-guide-p691-bk-af85a164-00-admin-guide-69-1be159d25d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/6901_6911/10_0/english/admin_guide/P691_BK_AF85A164_00_admin-guide-6901-6911-10_0/P691_BK_AF85A164_00_admin-guide-6901-6911-10_0_chapter_0111.html
retrieved_at: 2026-08-21T14:27:36.643018+00:00
---

Cisco Unified IP Phone 6901 and 6911 Administration Guide for Cisco Unified Communications Manager 10.0 (SCCP and SIP)

# Cisco Unified IP Phone 6901 and 6911 Administration Guide for Cisco Unified Communications Manager 10.0 (SCCP and SIP)

Updated: May 9, 2025

Chapter: Remote Monitoring

## Chapter: Remote Monitoring

# Remote Monitoring

## Remote Monitoring Overview

Each Cisco Unified IP Phone has a web page from which you can
                           		view information about the phone, that  includes:

Device information

Network setup information

Network statistics

Device logs

Streaming statistics

This chapter describes the information that you can obtain from
                           		the phone web page. You can use this information to remotely monitor the
                           		operation of a phone and to assist with troubleshooting.

For more information about troubleshooting the Cisco Unified IP
                           		Phone, 
                           		see Troubleshooting and Maintenance .

## Cisco Unified IP Phone Web Pages

The web page for a CiscoUnified IP Phone includes these
                           		topics:

Device Information : Displays device settings and related
                                 			 information for the phone.

Network Setup : Displays network configuration information
                                 			 and information about other phone settings.

Network Statistics : Displays information about network traffic using hyperlinks to the following windows:

Ethernet Information : Displays information about
                                       				  Ethernet traffic.

Network (Port) : Displays information about network
                                       				  traffic to and from the network port on the phone.

Device Logs : Displays information about troubleshooting using hyperlinks to the following windows:

Console Logs : Displays hyperlinks to individual log files.

Core Dumps : Displays hyperlinks to individual core dump files.

Status Messages : Displays up to 30 of the most recent status messages that the phone generated since it last powered up.

Streaming Statistics : Displays information about stream statistics using hyperlinks to the following window:

Stream : Displays
                                       				a variety of streaming statistics.

## Access Web Page for Phone

To access the web page for a CiscoUnifiedIPPhone, perform
                              		  these steps.

If you cannot access the web page, it may be disabled. For more information, see the Disable and Enable Web Page Access .

Step 1

Obtain the IP address of the CiscoUnified IP Phone using one of
                                       			 these methods:

- Search for the
                                          				phone in CiscoUnifiedCommunications Manager by choosing Device > Phone .
                                          				Phones registered with CiscoUnifiedCommunications Manager display the IP
                                          				address on the 
                                          				Find and List Phones window and at the top of
                                          				the 
                                          				Phone Configuration window.

- On the
                                          				CiscoUnified IP Phone, press the *, #, and 0 buttons simultaneously, enter the password, and
                                          				then follow the voice prompts to review the network setting.

Step 2

Open a web browser and enter the following URL, where IP_address is the IPaddress of the CiscoUnified IP Phone:

http://IP_address

## Disable and Enable Web Page Access

For security purposes, you may choose to prevent access to
                              		  the phone web pages. If you prevent access, the web pages
                              		  described in this chapter and the CiscoUnified CM User Options web pages
                              		  cannot display.

To disable access to the web pages for a phone, perform these
                              		  steps from Cisco Unified Communications Manager.

Step 1

Choose Device > Phone .

Step 2

Specify the criteria to find the phone and click Find , or click Find to display a list of all phones.

Step 3

Click the device name to open the 
                                       			 Phone Configuration window for the device.

Step 4

Scroll down to the Product Specific Configuration section.

Step 5

To disable access, from the Web Access drop-down list, choose 
                                       			 Disabled.

Step 6

To enable access, from the Web Access drop-down list,
                                       			 choose Enabled.

Step 7

Click Save .

Step 8

Click Apply Config .

## Device Information Area

The Device Information area on a phone web page displays
                              		  device settings and related information. The following table
                              		  describes these items.

To display the Device Information area, access the web page
                              		  for the phone as described in the Access Web Page for Phone ,
                              		  and then click the Device Information hyperlink.

Item

Description

MAC Address

Media Access Control (MAC) address of the phone

Host Name

Unique, fixed name that is automatically assigned to the phone
                                          					 based on the MAC address

Phone DN

Directory number assigned to the phone

App Load ID

Identifier of the firmware running on the phone

Boot Load ID

Identifier of the factory-installed load running on the phone

Hardware Revision

Revision value of the phone hardware

Serial Number

Unique serial number of the phone

Model Number

Model number of the phone

Message Waiting

Indicates if there is a voice message waiting on the primary
                                          					 line for this phone

UDI

Displays the following Cisco Unique Device Identifier (UDI)
                                          					 information about the phone:

- Device Type:
                                             						Indicates hardware type. For example, phone displays for all phone models

- Device Description: Displays the name of the phone associated with the indicated model type

- Product Identifier: Specifies the phone model

- Version Identifier: Represents the hardware version of the phone

- Serial Number:
                                             						Displays the unique serial number of the phone

Time

Time obtained from the Date/Time Group in CiscoUnified
                                          					 Communications Manager to which the phone belongs

Time Zone

Time zone obtained from the Date/Time Group in CiscoUnified
                                          					 Communications Manager to which the phone belongs

Date

Date obtained from the Date/Time Group in CiscoUnified
                                          					 Communications Manager to which the phone belongs

## Network Setup Area

The Network Setup on a phone web page displays network setup
                              		  information and information about other phone settings. The following table
                              		  describes these items.

You can view and set many of these items from the Network
                              		  Setup Menu and the Phone Information Menu on the CiscoUnified IP Phone. For
                              		  more information, see Cisco Unified IP Phone Settings .

To display the Network Setup area, access the web page for
                              		  the phone as described in the Access Web Page for Phone ,
                              		  and click the Network Configuration hyperlink.

Item

Description

DHCP Server

IP address of the Dynamic Host Configuration Protocol (DHCP)
                                          					 server that assigns the phone IP address.

MAC Address

Media Access Control (MAC) address of the phone.

Host Name

Host name that the DHCP server assigned to the phone.

Domain Name

Name of the Domain Name System (DNS) domain in which the phone
                                          					 resides.

IP Address

Internet Protocol (IP) address of the phone.

Subnet Mask

Subnet mask used by the phone.

TFTP Server 1

Primary Trivial File Transfer Protocol (TFTP) server used by
                                          					 the phone.

TFTP Server 2

Backup Trivial File Transfer Protocol (TFTP) server used by
                                          					 the phone.

Default Router 1

Default router used by the phone.

DNS Server 1 through 5

Primary DNS server (DNS Server 1) and
                                          					 optional backup DNS servers  (DNS Server 2 - 5) used by the phone.

Operational VLAN ID

Auxiliary Virtual Local Area Network (VLAN) configured on a
                                          					 Cisco Catalyst switch in which the phone is a member.

Admin. VLAN ID

Auxiliary VLAN in which the phone is a member.

CallManager 1–5

Host names or IP addresses, in prioritized order, of the
                                          					 CiscoUnifiedCommunications Manager servers with which the phone can register.

For an available server, an item shows the
                                          					 CiscoUnifiedCommunications Manager server IP address and one of the following
                                          					 states:

- Active:
                                             						CiscoUnifiedCommunications Manager server from which the phone is currently
                                             						receiving call processing services.

- Standby:
                                             						CiscoUnifiedCommunications Manager server to which the phone switches if the
                                             						current server becomes unavailable.

- Blank: No current
                                             						connection to the CiscoUnifiedCommunications Manager server.

An item may also include the Survivable Remote Site Telephony
                                          					 (SRST) designation, which identifies an SRST router capable of providing
                                          					 CiscoUnifiedCommunications Manager functionality with a limited feature set.
                                          					 This router assumes control of call processing if all other
                                          					 CiscoUnifiedCommunications Manager servers become unreachable. The SRST
                                          					 CiscoUnifiedCommunications Manager always appears last in the list of
                                          					 servers, even if it is active. You configure the SRST router address in the
                                          					 Device Pool section in CiscoUnifiedCommunications Manager Configuration
                                          					 window.

DHCP Enabled

Indicates whether the phone uses DHCP.

DHCP Address Released

Indicates the setting of the DHCP Address Released option on
                                          					 the phone Network Configuration menu.

Alternate TFTP

Indicates whether the phone uses an alternative TFTP server.

Automatic Port Synchronization

(Cisco Unified IP Phone 6911 only)

Indicates if the automatic port synchronization is enabled or
                                          					 disabled. When automatic port synchronization is enabled, Cisco recommends
                                          					 that you configure both ports to autonegotiate. If one port is enabled for
                                          					 autonegotiate and the other is at a fixed speed, the phone synchronizes to the
                                          					 fixed port speed.

SW Port Remote Configuration

Indicates if the software port configuration of the speed and
                                          					 duplex mode for the SW port is enabled or disabled.

PC Port Remote Configuration

(Cisco Unified IP Phone 6911 only)

Indicates if the remote port configuration of the speed and
                                          					 duplex mode for the PC port is enabled or disabled.

SW Port Setup

Speed and duplex of the switch port, where:

- A: Auto Negotiate

- 10H:
                                             						10-BaseT/half duplex

- 10F:
                                             						10-BaseT/full duplex

- 100H:
                                             						100-BaseT/half duplex

- 100F:
                                             						100-BaseT/full duplex

- No Link: No
                                             						connection to the switch port

PC Port Setup

(Cisco Unified IP Phone 6911 only)

Speed and duplex of the switch port, where:

- A: Auto Negotiate

- 10H:
                                             						10-BaseT/half duplex

- 10F:
                                             						10-BaseT/full duplex

- 100H:100-BaseT/half duplex

- 100F:
                                             						100-BaseT/full duplex

- No Link: No
                                             						connection to the PC port

User Locale

User locale associated with the phone user. Identifies a set
                                          					 of detailed information to support users, including language, font, date and
                                          					 time formatting, and alphanumeric keyboard text information.

Network Locale

Network locale associated with the phone user. Identifies a
                                          					 set of detailed information to support the phone in a specific location,
                                          					 including definitions of the tones and cadences used by the phone.

User Locale Version

Version of the user locale loaded on the phone.

Network Locale Version

Version of the network locale loaded on the phone.

PC Port Disabled

(Cisco Unified IP Phone 6911 only)

Indicates whether the PC port on the phone is enabled or
                                          					 disabled.

Speaker Enabled

(Cisco Unified IP Phone 6911 only)

Indicates whether the speakerphone is enabled on the phone.

GARP Enabled

Indicates whether the phone learns MAC addresses from
                                          					 Gratuitous ARP (GARP) responses.

Video Capability Enabled

(Cisco Unified IP Phone 6911 only)

Indicates whether the phone can participate in video calls
                                          					 when connected to an appropriately equipped PC.

Voice VLAN Enabled

Indicates whether the phone allows a device attached to the PC
                                          					 port to access the Voice VLAN.

DSCP for Call Control

Digital Signal Control Processing (DSCP) classification for call control signaling.

DSCP for Configuration

DSCP classification for any phone configuration transfer.

DSCP for Services

DSCP classification for phone-based services.

Security Mode

Displays the security mode for the phone.

Web Access Enabled

Indicates whether web access is enabled or disabled
                                          					 for the phone.

Span to PC Port

(Cisco Unified IP Phone 6911 only)

Indicates whether the phone will forward packets transmitted
                                          					 and received on the network port to the access port.

CDP: PC Port

(Cisco Unified IP Phone 6911 only)

Indicates whether CDP is supported on the PC port (default is
                                          					 enabled).

Enable CDP on the PC port when Cisco VT Advantage/Unified
                                          					 Video Advantage (CVTA) is connected to the PC port. CVTA does not work without
                                          					 CDP interaction with the phone.

When CDP is disabled in Cisco Unified Communications Manager,
                                          					 a warning displays to indicate that disabling CDP on the PC port prevents CVTA
                                          					 from working.

The current PC and switch port CDP values display on the
                                          					 Settings menu.

CDP: SW Port

Indicates whether CDP is supported on the switch port (default
                                          					 is enabled).

Enable CDP on the switch port for VLAN assignment for the
                                          					 phone, power negotiation, QoS management, and 802.1x security.

Enable CDP on the switch port when the phone is connected to a
                                          					 Cisco switch.

When CDP is disabled in Cisco Unified Communications Manager,
                                          					 a warning displays to, indicate that CDP should be disabled on the switch
                                          					 port only if the phone is connected to a non-Cisco switch.

The current PC and switch port CDP values are shown on the
                                          					 Settings menu.

SSH Access Enabled

Indicates whether the phone accepts or blocks the SSH
                                          					 connections.

EnergyWise Level

Indicates the EnergyWise Level.

EnergyWise Domain

The EnergyWise domain that the phone is in.

Federal Information Processing Standard (FIPS) Mode Enabled

Indicates whether FIPS mode is enabled.

IP Addressing Mode

Displays the IP addressing mode that is available on the
                                          					 phone.

IP Preference Mode Control

Indicates the IP address version that the phone uses during
                                          					 signaling with Cisco Unified Communications Manager when both IPv4 and IPv6 are
                                          					 both available on the phone.

IPv6 Auto Configuration

Displays whether the autoconfiguration is enabled or disabled
                                          					 on the phone.

IPv6 CAPF Server

Common Name (from the Cisco Unified Communications Manager
                                          					 Certificate) of the CAPF used by the phone.

DHCPv6

Dynamic Host Configuration Protocol version 6 (DHCPv6) automatically
                                          					 assigns IPv6 address to devices when you connect them to the network. Cisco
                                          					 Unified IP Phones enable DHCP by default.

IPv6 Default Router 1

Default router used by the phone (Default Router 1).

IPv6 Address

The 128 bit IPv6 address of the phone.

IPv6 Prefix Length

Subnet prefix length that is used by the phone. The subnet
                                          					 prefix length is a decimal value from 1-128, that specifies the portion of the
                                          					 IPv6 address that comprises the subnet.

IPv6 TFTP Server

Indicates whether the phone is using the IPv6 Alternate TFTP
                                          					 server.

## Network Statistics Area

The Network Statistics area on a phone web
                           		page provides information about network traffic on the phone. To display a
                           		network statistics area, access the web page for the phone as described in the Access Web Page for Phone .

Ethernet Information: Displays information about Ethernet traffic.

Network Information (Cisco Unified IP Phone 6901): Displays
                                 			 information about network traffic to and from the network port (10/100 SW) on
                                 			 the phone.

Network and Access Information (Cisco Unified IP Phone 6911):
                                 			 Displays information about network traffic to and from the network port (10/100
                                 			 SW) on the phone.

The following sections describe the Ethernet Information and the Network Information areas.

### Ethernet Information Area

The following table describes the fields in the Ethernet Information area.

Item

Description

Tx Frames

Total number of packets transmitted by the phone

Tx broadcast

Total number of broadcast packets transmitted by the phone

Tx multicast

Total number of multicast packets transmitted by the phone

Tx unicast

Total number of unicast packets transmitted by the phone

Rx Frames

Total number of packets received by the phone

Rx broadcast

Total number of broadcast packets received by the phone

Rx multicast

Total number of multicast packets received by the phone

Rx unicast

Total number of unicast packets received by the phone

RxPacketNoDes

Total number of shed packets caused by no Direct Memory Access
                                             					 (DMA) descriptor

### Network Information Area

The following table describes the fields in the Network Information area.

Item

Description

Tx Frames

Total number of packets transmitted by the phone

Tx broadcast

Total number of broadcast packets transmitted by the phone

Tx unicast

Total number of unicast packets transmitted by the phone

Rx Frames

Total number of packets received by the phone

Rx broadcast

Total number of broadcast packets received by the phone

Rx unicast

Total number of unicast packets received by the phone

Neighbor Device ID

Identifier of a device connected to this port discovered by
                                             					 CDP protocol or Link Layer Discovery Protocol (LLDP)

Neighbor IP Address

IP address of the neighbor device discovered by CDP protocol

Neighbor Port

Neighbor device port to which the phone is connected
                                             					 discovered by CDP protocol

LLDP AgeoutsTotal

Total number of LLDP frames that have been time out in cache

LLDP FramesDiscardedTotal

Total number of LLDP frames that are discarded when any of the
                                             					 mandatory TLVs is missing or out of order or contains out of range string
                                             					 length

LLDP FramesInErrorsTotal

Total number of LLDP frames that received with one or more
                                             					 detectable errors

LLDP FramesInTotal

Total number of LLDP frames received on the phone

LLDP TLVDiscardedTotal

Total number of LLDP Threshold Limit Values (TLV) that are discarded

LLDP TLVUnrecognizedTotal

Total number of LLDP TLVs that are not recognized on the phone

Restart Cause

Reason for the last restart

Port

Speed and duplex information

IPv4

IPv4 Address

## Device Logs Area

The Device Logs area on a phone web page
                           		provides information you can use to monitor and troubleshoot the phone. To
                           		access a Device Log area, access the web page for the phone as described in the Access Web Page for Phone .

Console Logs: Displays hyperlinks to individual log files. The
                                 			 console log files include debug and error messages received on the phone.

Core Dumps: Displays hyperlinks to individual dump files. The core
                                 			 dump files include data from a phone crash.

Status Messages: Displays up to the 80 most recent status messages
                                 			 that the phone has generated since it was last powered up. You can also see
                                 			 this information from the Status Messages screen on the Web page of the phone. Status Messages Area describes the status messages that may be displayed.

The following sections describe the Status Messages Area.

### Status Messages Area

The Status Messages web page displays up to 80 of the most
                                 		  recent status messages that the phone has generated since it was last powered
                                 		  up. You can access the Status Messages web page even if the phone is not
                                 		  running. The following table describes the status messages. This table also
                                 		  includes possible explanations and actions to troubleshoot errors.

Message

Description

Possible Explanation and Action

CFG file not found

The name-based and default configuration file was not found on
                                             					 the TFTP Server.

The Cisco Unified Communications Manager creates the configuration file for the phone when the phone is added to the database.
                                             If the phone has
                                             					 not been added to the Cisco UnifiedCommunications Manager database, the TFTP
                                             					 server generates a CFG File Not Found response.

Phone is not
                                             						registered with Cisco Unified Communications Manager. You must manually add the phone to Cisco
                                             						  UnifiedCommunications Manager if you are not allowing phones to autoregister.
                                             						  For more information, see the Cisco Unified Communications Manager Phone Addition Methods .

If you are using
                                             						DHCP, verify that the DHCP server is pointing to the correct TFTP server.

If you are using
                                             						static IP addresses, check the TFTP server configuration.

CFG TFTP Size Error

The configuration file is too large for the file system on the
                                             					 phone.

Power cycle the phone.

Checksum Error

Downloaded software file is corrupted.

Obtain a new copy of the phone firmware and place it in the
                                             					 TFTPPath directory. You should only copy files into this directory when the
                                             					 TFTP server software is shut down, otherwise the files may be corrupted.

DHCP timeout

DHCP server did not respond.

- Network is busy:
                                                						The errors should resolve themselves when the network load reduces.

- No network
                                                						connectivity between the DHCP server and the phone: Verify the network
                                                						connections.

- DHCP server is
                                                						down: Check the DHCP server configuration.

- Errors persist:
                                                						Consider assigning a static IP address.

DNS timeout

DNS server did not respond.

- Network is busy:
                                                						The errors should resolve themselves when the network load reduces.

- No network
                                                						connectivity between the DNS server and the phone: Verify the network
                                                						connections.

- DNS server is down: Check the DNS server configuration.

DNS unknown host

DNS could not resolve the name of the TFTP server or Cisco
                                             					 Unified Communications Manager.

- Verify that the
                                                						host names of the TFTP server or Cisco UnifiedCommunications Manager are
                                                						configured properly in DNS.

- Consider using IP
                                                						addresses rather than host names.

Duplicate IP

Another device is using the IP address assigned to the phone.

- If the phone has a
                                                						static IP address, verify that you have not assigned a duplicate IP address.

- If you are using
                                                						DHCP, check the DHCP server configuration.

Error update locale

One or more localization files could not be found in the
                                             					 TFTPPath directory or were not valid. The locale was not changed.

From Cisco Unified Operating System Administration, check that
                                             					 the following files are located within subdirectories in the TFTP File
                                             					 Management:

tones.xml

glyphs.xml

dictionary.xml

kate.xml

File not found

The phone cannot locate the phone load file specified
                                             					 in the phone configuration file on the TFTP server.

From Cisco Unified Operating System Administration, make sure
                                             					 that the phone load file is on the TFTP server, and that the entry in the
                                             					 configuration file is correct.

IP address released

The phone has been configured to release the  IP address.

The phone remains idle until it is power cycled or you reset
                                             					 the DHCP address.

Load ID incorrect

Load ID of the software file is of the wrong type.

Check the load ID assigned to the phone (from Cisco
                                             					 UnifiedCommunications Manager, choose Device > Phone ).
                                             					 Verify that the load ID is entered correctly.

Load rejected HC

The application that was downloaded is not compatible with the
                                             					 phone hardware.

Occurs if you were attempting to install a version of software
                                             					 on this phone that did not support hardware changes on this newer phone.

Check the load ID assigned to the phone (from Cisco
                                             					 UnifiedCommunications Manager, choose Device > Phone ).
                                             					 Re-enter the load displayed on the phone.

No default router

The DHCP or static configuration did not specify a default
                                             					 router.

- If the phone has a
                                                						static IP address, verify that the default router has been configured.

- If you are using
                                                						DHCP, the DHCP server may not contain default router. Check the DHCP server
                                                						configuration.

No DNS server IP

A name was specified but the DHCP or static IP configuration
                                             					 did not specify a DNS server address.

- If the phone has a
                                                						static IP address, verify that the DNS server has been configured.

- If you are using
                                                						DHCP, the DHCP server may not contain a DNS server. Check the DHCP server
                                                						configuration.

TFTP access error

TFTP server is pointing to a directory that does not exist.

- If you are using
                                                						DHCP, verify that the DHCP server is pointing to the correct TFTP server.

- If you are using
                                                						static IP addresses, check the TFTP server configuration.

TFTP error

The phone does not recognize an error code provided by the
                                             					 TFTP server.

Contact the Cisco TAC.

TFTP file not found

The requested load file (.bin) was not found in the TFTPPath
                                             					 directory.

Check the load ID assigned to the phone. From Cisco
                                             					 UnifiedCommunications Manager, choose Device > Phone .
                                             					 Verify that the TFTPPath directory contains a .bin file with this load ID as
                                             					 the name.

TFTP server not authorized

The specified TFTP server could not be found in the phone CTL.

- The DHCP server
                                                						has the wrong configuration file for the TFTP server. Update the TFTP server
                                                						configuration to specify the correct TFTP server.

- The CTL file was
                                                						made and then the TFTP server address changed. Regenerate the CTL file.

- If the phone is
                                                						using a static IP address, the phone may be configured with the wrong TFTP
                                                						server address. Enter the correct TFTP server address in the Network
                                                						Configuration menu on the phone.

- If the TFTP server
                                                						address is correct, there may be a problem with the CTL file. Run the CTL
                                                						client and update the CTL file, making sure that the proper TFTP servers are
                                                						included in this file.

TFTP timeout

TFTP server did not respond.

- Network is busy:
                                                						The errors should resolve themselves when the network load reduces.

- No network
                                                						connectivity between the TFTP server and the phone: Verify the network
                                                						connections.

- TFTP server is
                                                						down: Check the TFTP server configuration.

Timed Out

Supplicant attempted 802.1X transaction but timed out to due
                                             					 the absence of an authenticator.

Authentication typically times out if 802.1X is not configured
                                             					 on the switch.

Version error

The name of the phone load file is incorrect.

Make sure that the phone load file has the correct name.

XmlDefault.cnf.xml, or .cnf.xml corresponding to the phone
                                             					 device name

Name of the configuration file.

None. This is an informational message indicating the name of
                                             					 the configuration file for the phone.

## Streaming Statistics Area

A CiscoUnifiedIPPhone can stream information to and from
                              		  up to three devices simultaneously. A phone streams information when it is on
                              		  a call or running a service that sends or receives audio or data.

The Streaming Statistics areas on a phone web page provide
                              		  information about the streams. Cisco Unified IP Phone 6900 Series phones use
                              		  only Stream 1.

To display a Streaming Statistics area, access the web page
                              		  for the phone as described in the Access Web Page for Phone ,
                              		  and then click the Stream 1 hyperlink.

The following table describes the items in the Streaming
                              		  Statistics areas.

Item

Description

Remote Address

IP address and UDP port of the destination of the stream.

Local Address

IP address and UDP port of the phone.

Start Time

Internal time stamp indicating when
                                          					 CiscoUnifiedCommunications Manager requested that the phone start
                                          					 transmitting packets.

Stream Status

Indication of whether streaming is active or not.

Host Name

Unique, fixed name that is automatically assigned to the phone
                                          					 based on the  MAC address.

Sender Packets

Total number of RTP data packets transmitted by the phone
                                          					 since starting this connection. The value is 0 if the connection is in
                                          					 receive-only mode.

Sender Octets

Total number of payload octets transmitted in RTP data packets
                                          					 by the phone since starting this connection. Receive-only connections display 0 in the field.

Sender Codec

Type of audio encoding used for the transmitted stream.

Sender Reports Sent

Number of times the RTCP Sender Report have been sent.

Sender Report Time Sent

Internal time stamp of when the last RTCP Sender
                                          					 Report was sent.

Rcvr Lost Packets

Total number of RTP data packets that have been lost since
                                          					 starting receiving data on this connection. Defined as the number of expected
                                          					 packets less the number of packets actually received, where the number of
                                          					 received packets includes any that are late or duplicate. Send-only connections display 0 in the field.

Avg Jitter

Estimate of mean deviation of the RTP data packet
                                          					 interarrival time, measured in milliseconds. Send-only connections display 0 in the field.

Rcvr Codec

Type of audio encoding used for the received stream.

Rcvr Reports Sent

Number of times the RTCP Receiver Reports have been sent.

Rcvr Report Time Sent

Internal time stamp indication when a RTCP Receiver Report was
                                          					 sent.

Rcvr Packets

Total number of RTP data packets received by the phone since
                                          					 starting receiving data on this connection. Includes packets received from
                                          					 different sources if this is a multicast call. Send-only connections display 0 in the field.

Rcvr Octets

Total number of payload octets received in RTP data packets by
                                          					 the device since starting reception on the connection. Includes packets
                                          					 received from different sources if this is a multicast call. Send-only connections display 0 in the field.

Latency

Estimate of the network latency, expressed in milliseconds.
                                          					 Represents a running average of the round-trip delay, measured when RTCP
                                          					 receiver report blocks are received.

Max Jitter

Maximum value of instantaneous jitter, in milliseconds.

Sender Size

RTP packet size, in milliseconds, for the transmitted stream.

Sender Reports Received

Number of times RTCP Sender Reports have been received.

Sender Report Time Received

Last time at which an RTCP Sender Report was received.

Rcvr Size

RTP packet size, in milliseconds, for the received stream.

Rcvr Discarded

RTP packets received from network but discarded from jitter
                                          					 buffers.

Rcvr Reports Received

Number of times RTCP Receiver Reports have been received.

Rcvr Report Time Received

Last time at which an RTCP Receiver Report was received.

| Note | If you cannot access the web page, it may be disabled. For more information, see the Disable and Enable Web Page Access . |
|---|---|

| Step 1 | Obtain the IP address of the CiscoUnified IP Phone using one of
                                       			 these methods: Search for the
                                          				phone in CiscoUnifiedCommunications Manager by choosing Device > Phone .
                                          				Phones registered with CiscoUnifiedCommunications Manager display the IP
                                          				address on the 
                                          				Find and List Phones window and at the top of
                                          				the 
                                          				Phone Configuration window. On the
                                          				CiscoUnified IP Phone, press the *, #, and 0 buttons simultaneously, enter the password, and
                                          				then follow the voice prompts to review the network setting. |
|---|---|
| Step 2 | Open a web browser and enter the following URL, where IP_address is the IPaddress of the CiscoUnified IP Phone: http://IP_address |

| Step 1 | Choose Device > Phone . |
|---|---|
| Step 2 | Specify the criteria to find the phone and click Find , or click Find to display a list of all phones. |
| Step 3 | Click the device name to open the 
                                       			 Phone Configuration window for the device. |
| Step 4 | Scroll down to the Product Specific Configuration section. |
| Step 5 | To disable access, from the Web Access drop-down list, choose 
                                       			 Disabled. |
| Step 6 | To enable access, from the Web Access drop-down list,
                                       			 choose Enabled. |
| Step 7 | Click Save . |
| Step 8 | Click Apply Config . |

| Item | Description |
|---|---|
| MAC Address | Media Access Control (MAC) address of the phone |
| Host Name | Unique, fixed name that is automatically assigned to the phone
                                          					 based on the MAC address |
| Phone DN | Directory number assigned to the phone |
| App Load ID | Identifier of the firmware running on the phone |
| Boot Load ID | Identifier of the factory-installed load running on the phone |
| Hardware Revision | Revision value of the phone hardware |
| Serial Number | Unique serial number of the phone |
| Model Number | Model number of the phone |
| Message Waiting | Indicates if there is a voice message waiting on the primary
                                          					 line for this phone |
| UDI | Displays the following Cisco Unique Device Identifier (UDI)
                                          					 information about the phone: Device Type:
                                             						Indicates hardware type. For example, phone displays for all phone models Device Description: Displays the name of the phone associated with the indicated model type Product Identifier: Specifies the phone model Version Identifier: Represents the hardware version of the phone Serial Number:
                                             						Displays the unique serial number of the phone |
| Time | Time obtained from the Date/Time Group in CiscoUnified
                                          					 Communications Manager to which the phone belongs |
| Time Zone | Time zone obtained from the Date/Time Group in CiscoUnified
                                          					 Communications Manager to which the phone belongs |
| Date | Date obtained from the Date/Time Group in CiscoUnified
                                          					 Communications Manager to which the phone belongs |

| Item | Description |
|---|---|
| DHCP Server | IP address of the Dynamic Host Configuration Protocol (DHCP)
                                          					 server that assigns the phone IP address. |
| MAC Address | Media Access Control (MAC) address of the phone. |
| Host Name | Host name that the DHCP server assigned to the phone. |
| Domain Name | Name of the Domain Name System (DNS) domain in which the phone
                                          					 resides. |
| IP Address | Internet Protocol (IP) address of the phone. |
| Subnet Mask | Subnet mask used by the phone. |
| TFTP Server 1 | Primary Trivial File Transfer Protocol (TFTP) server used by
                                          					 the phone. |
| TFTP Server 2 | Backup Trivial File Transfer Protocol (TFTP) server used by
                                          					 the phone. |
| Default Router 1 | Default router used by the phone. |
| DNS Server 1 through 5 | Primary DNS server (DNS Server 1) and
                                          					 optional backup DNS servers  (DNS Server 2 - 5) used by the phone. |
| Operational VLAN ID | Auxiliary Virtual Local Area Network (VLAN) configured on a
                                          					 Cisco Catalyst switch in which the phone is a member. |
| Admin. VLAN ID | Auxiliary VLAN in which the phone is a member. |
| CallManager 1–5 | Host names or IP addresses, in prioritized order, of the
                                          					 CiscoUnifiedCommunications Manager servers with which the phone can register. For an available server, an item shows the
                                          					 CiscoUnifiedCommunications Manager server IP address and one of the following
                                          					 states: Active:
                                             						CiscoUnifiedCommunications Manager server from which the phone is currently
                                             						receiving call processing services. Standby:
                                             						CiscoUnifiedCommunications Manager server to which the phone switches if the
                                             						current server becomes unavailable. Blank: No current
                                             						connection to the CiscoUnifiedCommunications Manager server. An item may also include the Survivable Remote Site Telephony
                                          					 (SRST) designation, which identifies an SRST router capable of providing
                                          					 CiscoUnifiedCommunications Manager functionality with a limited feature set.
                                          					 This router assumes control of call processing if all other
                                          					 CiscoUnifiedCommunications Manager servers become unreachable. The SRST
                                          					 CiscoUnifiedCommunications Manager always appears last in the list of
                                          					 servers, even if it is active. You configure the SRST router address in the
                                          					 Device Pool section in CiscoUnifiedCommunications Manager Configuration
                                          					 window. |
| DHCP Enabled | Indicates whether the phone uses DHCP. |
| DHCP Address Released | Indicates the setting of the DHCP Address Released option on
                                          					 the phone Network Configuration menu. |
| Alternate TFTP | Indicates whether the phone uses an alternative TFTP server. |
| Automatic Port Synchronization (Cisco Unified IP Phone 6911 only) | Indicates if the automatic port synchronization is enabled or
                                          					 disabled. When automatic port synchronization is enabled, Cisco recommends
                                          					 that you configure both ports to autonegotiate. If one port is enabled for
                                          					 autonegotiate and the other is at a fixed speed, the phone synchronizes to the
                                          					 fixed port speed. |
| SW Port Remote Configuration | Indicates if the software port configuration of the speed and
                                          					 duplex mode for the SW port is enabled or disabled. |
| PC Port Remote Configuration (Cisco Unified IP Phone 6911 only) | Indicates if the remote port configuration of the speed and
                                          					 duplex mode for the PC port is enabled or disabled. |
| SW Port Setup | Speed and duplex of the switch port, where: A: Auto Negotiate 10H:
                                             						10-BaseT/half duplex 10F:
                                             						10-BaseT/full duplex 100H:
                                             						100-BaseT/half duplex 100F:
                                             						100-BaseT/full duplex No Link: No
                                             						connection to the switch port |
| PC Port Setup (Cisco Unified IP Phone 6911 only) | Speed and duplex of the switch port, where: A: Auto Negotiate 10H:
                                             						10-BaseT/half duplex 10F:
                                             						10-BaseT/full duplex 100H:100-BaseT/half duplex 100F:
                                             						100-BaseT/full duplex No Link: No
                                             						connection to the PC port |
| User Locale | User locale associated with the phone user. Identifies a set
                                          					 of detailed information to support users, including language, font, date and
                                          					 time formatting, and alphanumeric keyboard text information. |
| Network Locale | Network locale associated with the phone user. Identifies a
                                          					 set of detailed information to support the phone in a specific location,
                                          					 including definitions of the tones and cadences used by the phone. |
| User Locale Version | Version of the user locale loaded on the phone. |
| Network Locale Version | Version of the network locale loaded on the phone. |
| PC Port Disabled (Cisco Unified IP Phone 6911 only) | Indicates whether the PC port on the phone is enabled or
                                          					 disabled. |
| Speaker Enabled (Cisco Unified IP Phone 6911 only) | Indicates whether the speakerphone is enabled on the phone. |
| GARP Enabled | Indicates whether the phone learns MAC addresses from
                                          					 Gratuitous ARP (GARP) responses. |
| Video Capability Enabled (Cisco Unified IP Phone 6911 only) | Indicates whether the phone can participate in video calls
                                          					 when connected to an appropriately equipped PC. |
| Voice VLAN Enabled | Indicates whether the phone allows a device attached to the PC
                                          					 port to access the Voice VLAN. |
| DSCP for Call Control | Digital Signal Control Processing (DSCP) classification for call control signaling. |
| DSCP for Configuration | DSCP classification for any phone configuration transfer. |
| DSCP for Services | DSCP classification for phone-based services. |
| Security Mode | Displays the security mode for the phone. |
| Web Access Enabled | Indicates whether web access is enabled or disabled
                                          					 for the phone. |
| Span to PC Port (Cisco Unified IP Phone 6911 only) | Indicates whether the phone will forward packets transmitted
                                          					 and received on the network port to the access port. |
| CDP: PC Port (Cisco Unified IP Phone 6911 only) | Indicates whether CDP is supported on the PC port (default is
                                          					 enabled). Enable CDP on the PC port when Cisco VT Advantage/Unified
                                          					 Video Advantage (CVTA) is connected to the PC port. CVTA does not work without
                                          					 CDP interaction with the phone. When CDP is disabled in Cisco Unified Communications Manager,
                                          					 a warning displays to indicate that disabling CDP on the PC port prevents CVTA
                                          					 from working. The current PC and switch port CDP values display on the
                                          					 Settings menu. |
| CDP: SW Port | Indicates whether CDP is supported on the switch port (default
                                          					 is enabled). Enable CDP on the switch port for VLAN assignment for the
                                          					 phone, power negotiation, QoS management, and 802.1x security. Enable CDP on the switch port when the phone is connected to a
                                          					 Cisco switch. When CDP is disabled in Cisco Unified Communications Manager,
                                          					 a warning displays to, indicate that CDP should be disabled on the switch
                                          					 port only if the phone is connected to a non-Cisco switch. The current PC and switch port CDP values are shown on the
                                          					 Settings menu. |
| SSH Access Enabled | Indicates whether the phone accepts or blocks the SSH
                                          					 connections. |
| EnergyWise Level | Indicates the EnergyWise Level. |
| EnergyWise Domain | The EnergyWise domain that the phone is in. |
| Federal Information Processing Standard (FIPS) Mode Enabled | Indicates whether FIPS mode is enabled. |
| IP Addressing Mode | Displays the IP addressing mode that is available on the
                                          					 phone. |
| IP Preference Mode Control | Indicates the IP address version that the phone uses during
                                          					 signaling with Cisco Unified Communications Manager when both IPv4 and IPv6 are
                                          					 both available on the phone. |
| IPv6 Auto Configuration | Displays whether the autoconfiguration is enabled or disabled
                                          					 on the phone. |
| IPv6 CAPF Server | Common Name (from the Cisco Unified Communications Manager
                                          					 Certificate) of the CAPF used by the phone. |
| DHCPv6 | Dynamic Host Configuration Protocol version 6 (DHCPv6) automatically
                                          					 assigns IPv6 address to devices when you connect them to the network. Cisco
                                          					 Unified IP Phones enable DHCP by default. |
| IPv6 Default Router 1 | Default router used by the phone (Default Router 1). |
| IPv6 Address | The 128 bit IPv6 address of the phone. |
| IPv6 Prefix Length | Subnet prefix length that is used by the phone. The subnet
                                          					 prefix length is a decimal value from 1-128, that specifies the portion of the
                                          					 IPv6 address that comprises the subnet. |
| IPv6 TFTP Server | Indicates whether the phone is using the IPv6 Alternate TFTP
                                          					 server. |

| Item | Description |
|---|---|
| Tx Frames | Total number of packets transmitted by the phone |
| Tx broadcast | Total number of broadcast packets transmitted by the phone |
| Tx multicast | Total number of multicast packets transmitted by the phone |
| Tx unicast | Total number of unicast packets transmitted by the phone |
| Rx Frames | Total number of packets received by the phone |
| Rx broadcast | Total number of broadcast packets received by the phone |
| Rx multicast | Total number of multicast packets received by the phone |
| Rx unicast | Total number of unicast packets received by the phone |
| RxPacketNoDes | Total number of shed packets caused by no Direct Memory Access
                                             					 (DMA) descriptor |

| Item | Description |
|---|---|
| Tx Frames | Total number of packets transmitted by the phone |
| Tx broadcast | Total number of broadcast packets transmitted by the phone |
| Tx unicast | Total number of unicast packets transmitted by the phone |
| Rx Frames | Total number of packets received by the phone |
| Rx broadcast | Total number of broadcast packets received by the phone |
| Rx unicast | Total number of unicast packets received by the phone |
| Neighbor Device ID | Identifier of a device connected to this port discovered by
                                             					 CDP protocol or Link Layer Discovery Protocol (LLDP) |
| Neighbor IP Address | IP address of the neighbor device discovered by CDP protocol |
| Neighbor Port | Neighbor device port to which the phone is connected
                                             					 discovered by CDP protocol |
| LLDP AgeoutsTotal | Total number of LLDP frames that have been time out in cache |
| LLDP FramesDiscardedTotal | Total number of LLDP frames that are discarded when any of the
                                             					 mandatory TLVs is missing or out of order or contains out of range string
                                             					 length |
| LLDP FramesInErrorsTotal | Total number of LLDP frames that received with one or more
                                             					 detectable errors |
| LLDP FramesInTotal | Total number of LLDP frames received on the phone |
| LLDP TLVDiscardedTotal | Total number of LLDP Threshold Limit Values (TLV) that are discarded |
| LLDP TLVUnrecognizedTotal | Total number of LLDP TLVs that are not recognized on the phone |
| Restart Cause | Reason for the last restart |
| Port | Speed and duplex information |
| IPv4 | IPv4 Address |

| Message | Description | Possible Explanation and Action |
|---|---|---|
| CFG file not found | The name-based and default configuration file was not found on
                                             					 the TFTP Server. | The Cisco Unified Communications Manager creates the configuration file for the phone when the phone is added to the database.
                                             If the phone has
                                             					 not been added to the Cisco UnifiedCommunications Manager database, the TFTP
                                             					 server generates a CFG File Not Found response. Phone is not
                                             						registered with Cisco Unified Communications Manager. You must manually add the phone to Cisco
                                             						  UnifiedCommunications Manager if you are not allowing phones to autoregister.
                                             						  For more information, see the Cisco Unified Communications Manager Phone Addition Methods . If you are using
                                             						DHCP, verify that the DHCP server is pointing to the correct TFTP server. If you are using
                                             						static IP addresses, check the TFTP server configuration. |
| CFG TFTP Size Error | The configuration file is too large for the file system on the
                                             					 phone. | Power cycle the phone. |
| Checksum Error | Downloaded software file is corrupted. | Obtain a new copy of the phone firmware and place it in the
                                             					 TFTPPath directory. You should only copy files into this directory when the
                                             					 TFTP server software is shut down, otherwise the files may be corrupted. |
| DHCP timeout | DHCP server did not respond. | Network is busy:
                                                						The errors should resolve themselves when the network load reduces. No network
                                                						connectivity between the DHCP server and the phone: Verify the network
                                                						connections. DHCP server is
                                                						down: Check the DHCP server configuration. Errors persist:
                                                						Consider assigning a static IP address. |
| DNS timeout | DNS server did not respond. | Network is busy:
                                                						The errors should resolve themselves when the network load reduces. No network
                                                						connectivity between the DNS server and the phone: Verify the network
                                                						connections. DNS server is down: Check the DNS server configuration. |
| DNS unknown host | DNS could not resolve the name of the TFTP server or Cisco
                                             					 Unified Communications Manager. | Verify that the
                                                						host names of the TFTP server or Cisco UnifiedCommunications Manager are
                                                						configured properly in DNS. Consider using IP
                                                						addresses rather than host names. |
| Duplicate IP | Another device is using the IP address assigned to the phone. | If the phone has a
                                                						static IP address, verify that you have not assigned a duplicate IP address. If you are using
                                                						DHCP, check the DHCP server configuration. |
| Error update locale | One or more localization files could not be found in the
                                             					 TFTPPath directory or were not valid. The locale was not changed. | From Cisco Unified Operating System Administration, check that
                                             					 the following files are located within subdirectories in the TFTP File
                                             					 Management: Located in
                                                						subdirectory with the same name as network locale: tones.xml Located in
                                                						subdirectory with the same name as user locale: glyphs.xml dictionary.xml kate.xml |
| File not found | The phone cannot locate the phone load file specified
                                             					 in the phone configuration file on the TFTP server. | From Cisco Unified Operating System Administration, make sure
                                             					 that the phone load file is on the TFTP server, and that the entry in the
                                             					 configuration file is correct. |
| IP address released | The phone has been configured to release the  IP address. | The phone remains idle until it is power cycled or you reset
                                             					 the DHCP address. |
| Load ID incorrect | Load ID of the software file is of the wrong type. | Check the load ID assigned to the phone (from Cisco
                                             					 UnifiedCommunications Manager, choose Device > Phone ).
                                             					 Verify that the load ID is entered correctly. |
| Load rejected HC | The application that was downloaded is not compatible with the
                                             					 phone hardware. | Occurs if you were attempting to install a version of software
                                             					 on this phone that did not support hardware changes on this newer phone. Check the load ID assigned to the phone (from Cisco
                                             					 UnifiedCommunications Manager, choose Device > Phone ).
                                             					 Re-enter the load displayed on the phone. |
| No default router | The DHCP or static configuration did not specify a default
                                             					 router. | If the phone has a
                                                						static IP address, verify that the default router has been configured. If you are using
                                                						DHCP, the DHCP server may not contain default router. Check the DHCP server
                                                						configuration. |
| No DNS server IP | A name was specified but the DHCP or static IP configuration
                                             					 did not specify a DNS server address. | If the phone has a
                                                						static IP address, verify that the DNS server has been configured. If you are using
                                                						DHCP, the DHCP server may not contain a DNS server. Check the DHCP server
                                                						configuration. |
| TFTP access error | TFTP server is pointing to a directory that does not exist. | If you are using
                                                						DHCP, verify that the DHCP server is pointing to the correct TFTP server. If you are using
                                                						static IP addresses, check the TFTP server configuration. |
| TFTP error | The phone does not recognize an error code provided by the
                                             					 TFTP server. | Contact the Cisco TAC. |
| TFTP file not found | The requested load file (.bin) was not found in the TFTPPath
                                             					 directory. | Check the load ID assigned to the phone. From Cisco
                                             					 UnifiedCommunications Manager, choose Device > Phone .
                                             					 Verify that the TFTPPath directory contains a .bin file with this load ID as
                                             					 the name. |
| TFTP server not authorized | The specified TFTP server could not be found in the phone CTL. | The DHCP server
                                                						has the wrong configuration file for the TFTP server. Update the TFTP server
                                                						configuration to specify the correct TFTP server. The CTL file was
                                                						made and then the TFTP server address changed. Regenerate the CTL file. If the phone is
                                                						using a static IP address, the phone may be configured with the wrong TFTP
                                                						server address. Enter the correct TFTP server address in the Network
                                                						Configuration menu on the phone. If the TFTP server
                                                						address is correct, there may be a problem with the CTL file. Run the CTL
                                                						client and update the CTL file, making sure that the proper TFTP servers are
                                                						included in this file. |
| TFTP timeout | TFTP server did not respond. | Network is busy:
                                                						The errors should resolve themselves when the network load reduces. No network
                                                						connectivity between the TFTP server and the phone: Verify the network
                                                						connections. TFTP server is
                                                						down: Check the TFTP server configuration. |
| Timed Out | Supplicant attempted 802.1X transaction but timed out to due
                                             					 the absence of an authenticator. | Authentication typically times out if 802.1X is not configured
                                             					 on the switch. |
| Version error | The name of the phone load file is incorrect. | Make sure that the phone load file has the correct name. |
| XmlDefault.cnf.xml, or .cnf.xml corresponding to the phone
                                             					 device name | Name of the configuration file. | None. This is an informational message indicating the name of
                                             					 the configuration file for the phone. |

| Item | Description |
|---|---|
| Remote Address | IP address and UDP port of the destination of the stream. |
| Local Address | IP address and UDP port of the phone. |
| Start Time | Internal time stamp indicating when
                                          					 CiscoUnifiedCommunications Manager requested that the phone start
                                          					 transmitting packets. |
| Stream Status | Indication of whether streaming is active or not. |
| Host Name | Unique, fixed name that is automatically assigned to the phone
                                          					 based on the  MAC address. |
| Sender Packets | Total number of RTP data packets transmitted by the phone
                                          					 since starting this connection. The value is 0 if the connection is in
                                          					 receive-only mode. |
| Sender Octets | Total number of payload octets transmitted in RTP data packets
                                          					 by the phone since starting this connection. Receive-only connections display 0 in the field. |
| Sender Codec | Type of audio encoding used for the transmitted stream. |
| Sender Reports Sent | Number of times the RTCP Sender Report have been sent. |
| Sender Report Time Sent | Internal time stamp of when the last RTCP Sender
                                          					 Report was sent. |
| Rcvr Lost Packets | Total number of RTP data packets that have been lost since
                                          					 starting receiving data on this connection. Defined as the number of expected
                                          					 packets less the number of packets actually received, where the number of
                                          					 received packets includes any that are late or duplicate. Send-only connections display 0 in the field. |
| Avg Jitter | Estimate of mean deviation of the RTP data packet
                                          					 interarrival time, measured in milliseconds. Send-only connections display 0 in the field. |
| Rcvr Codec | Type of audio encoding used for the received stream. |
| Rcvr Reports Sent | Number of times the RTCP Receiver Reports have been sent. |
| Rcvr Report Time Sent | Internal time stamp indication when a RTCP Receiver Report was
                                          					 sent. |
| Rcvr Packets | Total number of RTP data packets received by the phone since
                                          					 starting receiving data on this connection. Includes packets received from
                                          					 different sources if this is a multicast call. Send-only connections display 0 in the field. |
| Rcvr Octets | Total number of payload octets received in RTP data packets by
                                          					 the device since starting reception on the connection. Includes packets
                                          					 received from different sources if this is a multicast call. Send-only connections display 0 in the field. |
| Latency | Estimate of the network latency, expressed in milliseconds.
                                          					 Represents a running average of the round-trip delay, measured when RTCP
                                          					 receiver report blocks are received. |
| Max Jitter | Maximum value of instantaneous jitter, in milliseconds. |
| Sender Size | RTP packet size, in milliseconds, for the transmitted stream. |
| Sender Reports Received | Number of times RTCP Sender Reports have been received. |
| Sender Report Time Received | Last time at which an RTCP Sender Report was received. |
| Rcvr Size | RTP packet size, in milliseconds, for the received stream. |
| Rcvr Discarded | RTP packets received from network but discarded from jitter
                                          					 buffers. |
| Rcvr Reports Received | Number of times RTCP Receiver Reports have been received. |
| Rcvr Report Time Received | Last time at which an RTCP Receiver Report was received. |

| Note | When the RTP Control Protocol is disabled, no data generates for
                                       		  this field and thus displays as 0. |
|---|---|