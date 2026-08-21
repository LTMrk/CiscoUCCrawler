---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-dx-series-admin-1022-dx00-bk-c9fcbae4-00-cisco-dx-series-ag1022-dx00-bk-c9fc-cae8d3847e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/dx/series/admin/1022/DX00_BK_C9FCBAE4_00_cisco-dx-series-ag1022/DX00_BK_C9FCBAE4_00_cisco-dx-series-ag1022_chapter_01101.html
retrieved_at: 2026-08-21T21:02:23.718682+00:00
---

Cisco DX Series Administration Guide, Release 10.2(2)

# Cisco DX Series Administration Guide, Release 10.2(2)

Updated: September 18, 2014

Chapter: Remote Monitoring

## Chapter: Remote Monitoring

Contents

# Remote Monitoring

## Enable and Disable Web Page Access

For security purposes, access to the web pages for the device
		  is disabled by default. This prevents access to the web pages that are described in this
		  chapter and to the 
		  Self Care Portal.

## Access Device Web Page

- Search for the
				device in Cisco Unified Communications Manager by choosing Device > Phone .
				Devices that are registered with Cisco Unified Communications Manager display
				the IP address on the Find and List Phones window and at the top of the Phone
				Configuration window.

- On the device,
				choose Settings > About
					 device > Status > DHCP
					 Information and get the IP address for either Wi-Fi
				or Ethernet.

http://<IP_address>

The web page for the device includes these topics:

Device Information - Provides device settings and related
					 information.

Network Setup - Provides network setup information.

Security Information - Provides security information.

Ethernet Statistics - Includes the following hyperlinks, which
					 provide information about network traffic:

Ethernet Information - Provides information about Ethernet
						  traffic.

Access - Provides information about network traffic to and
						  from 
						  the device.

Network - Provides information about network traffic to
						  and from 
						  the device.

WLAN Setup

Current AP - Provides information about the current access point

WLAN Statistics - Provides information about WLAN traffic

Console Logs - Includes hyperlinks to individual log
						  files.

Core Dumps - Includes hyperlinks to individual dump files.

Status Messages - Provides up to the ten most recent status
						  messages that 
						  the device has
						  generated since it was last powered up.

Debug Display - Provides debug messages that might be
						  useful to Cisco Technical Assistance Center (TAC) if you require assistance
						  with troubleshooting.

Streaming Statistics - Includes the Audio and Video
					 statistics, Stream 1, Stream 2, Stream 3, Stream 4, Stream 5 and Stream 6
					 hyperlinks, which display a variety of streaming statistics.

## Device Information

The Device Information area on 
		  the device web page includes
		  device settings and related information.

Item

Description

Ethernet Network State

Ethernet Network State

Wifi Network State

Wifi Network State

MAC Address

Ethernet MAC Address

WLAN MAC Address

IP address for Wi-Fi connection

Host Name

Unique, fixed name that is automatically assigned to 
					 the device based on
					 its MAC address

Phone DN

Directory number that is assigned to 
					 the device

Version

Identifier of the firmware running on 
					 the device

Hardware Revision

Revision value of 
					 the device hardware

Serial Number

Unique serial number of 
					 the device

Model Number

Model number of 
					 the device

Message Waiting

Indicates whether a voice message is waiting on the primary
					 line for 
					 the device.

UDI

Provides the following Cisco Unique Device Identifier (UDI)
					 information about 
					 the device:

- Device Type: Indicates hardware type.

- Device Description: Provides the name of 
						the device
						that is associated with the indicated model type.

- Serial Number: Specifies the unique serial number of 
						the device.

Time

Time obtained from the Date/Time Group in Cisco Unified Communications Manager to which 
					 the device belongs

Time Zone

Time zone obtained from the Date/Time Group in Cisco Unified Communications Manager to which 
					 the device belongs

Date

Date obtained from the Date/Time Group in Cisco Unified Communications Manager to which 
					 the device belongs

## Network Setup

The Network Setup area on 
		  the device web page provides
		  network setup information and information about other 
		  settings. The
		  following table describes these items.

You can view and set many of these items from the Settings application on the 
		  device.

Item

Description

Wifi Information

Wifi DHCP Server

IP address of the Dynamic Host Configuration Protocol (DHCP)
					 server from which the device obtains its Wifi IP address.

Wifi MAC Address

Wifi Media Access Control (MAC) address of the device.

Wifi Host Name

Hostname that the DHCP server assigned to the device.

Wifi Domain Name

Name of the Domain Name System (DNS) domain in which the device resides.

Wifi IP Address

Internet Protocol (IP) address of the device.

Wifi SubNet Mask

Subnet Mask used by the device.

Wifi Default Router

Default router used by the device.

Wifi DNS Server 1

Primary Domain Name System (DNS) server used by the device.

Wifi DNS Server 2

Optional backup DNS server used by the device.

Wifi EAP Authentication

Indicates EAP authentication setting

Wifi SSID

Indicates the current wifi SSID

Wifi Security Mode

Indicates the current wifi security mode

Wifi 80211 Mode

Indicates the current wifi 80211 mode

Ethernet Information

Ethernet DHCP Server

IP address of the Dynamic Host Configuration Protocol (DHCP)
					 server from which the device obtains its IP address.

Ethernet MAC Address

Media Access Control (MAC) address of the device.

Ethernet Host Name

Hostname that the DHCP server assigned to the device.

Ethernet Domain Name

Name of the Domain Name System (DNS) domain in which the device resides.

Ethernet IP Address

Internet Protocol (IP) address of the device.

Ethernet SubNet Mask

Subnet Mask used by the device.

Ethernet DNS Server 1

Primary Domain Name System (DNS) server used by the device.

Ethernet DNS Server 2

Optional backup DNS server used by the device.

Operational VLAN ID

Auxiliary Virtual Local Area Network (VLAN) configured on a
					 Cisco Catalyst switch in which the device is a member.

Admin. VLAN ID

Auxiliary VLAN in which the device is a member.

PC VLAN

VLAN that is used to identify and remove 802.1P/Q tags from packets
					 sent to the PC.

SW Port Speed

Speed and duplex of the switch port, where:

- A - Auto Negotiate

- 10H -
						10BaseT/half duplex

- 10F -
						10BaseT/full duplex

- 100H -
						100BaseT/half duplex

- 100F -
						100BaseT/full duplex

- 1000F -
						1000BaseT/full duplex

- No Link - No
						connection to the switch port

PC Port Speed

Speed and duplex of the switch port, where:

- A - Auto Negotiate

- 10H -
						10-BaseT/half duplex

- 10F -
						10-BaseT/full duplex

- 100H -
						100-BaseT/half duplex

- 100F -
						100-BaseT/full duplex

- 1000F -
						1000-BaseT/full duplex

- No Link - No
						connection to the switch port

IPv6 Information

IP Addressing Mode

Indicates IP addressing mode.

IP Preference Mode Control

Indicates IP preference mode.

IPv6 Auto Configuration

Indicates if IPv6 auto configuration is enabled or disabled.

Duplicate Address Detection

Indicates if duplicate address detection is enabled or disabled.

Accept Redirect Messages

Indicates if accepting redirect messages is enabled or disabled.

Reply Multicast Echo Request

Indicates if replying to multicast echo requests is enabled or disabled.

IPv6 Address

IPv6 Prefix Length

Indicates IPv6 prefix length.

IPv6 Default Router

Indicates default router.

IPv6 DNS Server 1

Primary DNS server used by the device.

IPv6 DNS Server 2

optional backup DNS server used by the device

IPv6 Alternate TFTP

Indicates whether the device is using an alternative TFTP
					 server.

IPv6 TFTP Server 1

Primary Trivial File Transfer Protocol (TFTP) server used by
					 the device.

IPv6 TFTP Server 2

Backup Trivial File Transfer Protocol (TFTP) server used by
					 the device.

CUCM Configuration

CUCM Server 1-5

Hostnames or IP addresses, in prioritized order, of the Cisco Unified Communications Manager servers with which the device can register. An
					 item can also show the IP address of an SRST router that is capable of
					 providing limited Cisco Unified Communications Manager functionality, if such a
					 router is available.

- Active - Cisco Unified Communications Manager server from which the device is currently
						receiving call-processing services

- Standby - Cisco Unified Communications Manager server to which the device switches if the
						current server becomes unavailable

- Blank - No current
						connection to this Cisco Unified Communications Manager server

An item may also include the Survivable Remote Site Telephony
					 (SRST) designation, which identifies an SRST router that is capable of providing Cisco Unified Communications Manager functionality with a limited feature set. This
					 router assumes control of call processing if all other Cisco Unified Communications Manager servers become unreachable. The SRST Cisco Unified Communications Manager always appears last in the list of servers, even if it
					 is active. You configure the SRST router address in the Device Pool window in Cisco Unified Communications Manager Administration.

Information URL

This feature is not supported on Cisco DX Series devices.

Directories URL

This feature is not supported on Cisco DX Series devices.

Messages URL

This feature is not supported on Cisco DX Series devices.

Services URL

This feature is not supported on Cisco DX Series devices.

Forwarding Delay

The time that is spent in the listening and learning state.

Idle URL

This feature is not supported on Cisco DX Series devices.

Idle URL time

This feature is not supported on Cisco DX Series devices.

Proxy Server URL

This feature is not supported on Cisco DX Series devices.

Authentication URL

This feature is not supported on Cisco DX Series devices.

TFTP Server 1

Primary Trivial File Transfer Protocol (TFTP) server used by
					 the device.

TFTP Server 2

Backup Trivial File Transfer Protocol (TFTP) server used by
					 the device.

Alternate TFTP

Indicates whether the device is using an alternative TFTP
					 server.

User Locale

User locale that is associated with the device user. Identifies a set
					 of detailed information to support users, including language, font, date, and
					 time formatting, and alphanumeric keyboard text information.

Network Locale

Network locale that is associated with the device user. Identifies a
					 set of detailed information to support the device in a specific location,
					 including definitions of the tones and cadences that the device uses.

User Locale Version

Version of the user locale that is loaded on the device.

Network Locale Version

Version of the network locale that is loaded on the device.

PC Port Disabled

Indicates whether the PC port on the device is
					 enabled or disabled.

GARP Enabled

Indicates whether the device learns MAC addresses from
					 Gratuitous ARP responses.

Video Capability Enabled

Indicates whether the device can participate in video calls.

Voice Vlan Access Enabled

Indicates whether the device allows a device attached to the
					 PC port to access the Voice VLAN.

Auto Select Line

Indicates whether auto select line is enabled for the device.

Dscp For Call Control

DSCP IP classification for call control signaling.

Dscp For Setup.

DSCP IP classification for the device configuration transfer.

Dscp For Services

DSCP IP classification for the device-based services.

Security Mode

The security mode that is set for the device.

Web Access

Indicates whether web access is enabled (Yes) or disabled (No)
					 for the device.

Span PC Port

Indicates whether the device will forward packets that are transmitted
					 and received on the network port to the access port.

CDP on PC Port

Indicates whether CDP is supported on the PC port (default is
					 enabled).

When CDP is disabled in Cisco Unified Communications Manager ,
					 a warning is displayed, indicating that disabling CDP on the PC port prevents
					 CVTA from working.

The current PC and switch port CDP values are shown in the
					 Settings application.

CDP on SW Port

Indicates whether CDP is supported on the switch port (default
					 is enabled).

Enable CDP on the switch port for VLAN assignment for the device, power negotiation, QoS management, and 802.1x security.

Enable CDP on the switch port when the device is connected to
					 a Cisco switch.

When CDP is disabled in Cisco Unified Communications Manager ,
					 a warning is presented, indicating that CDP is disabled on the switch port only if
					 the device is connected to a non-Cisco switch.

The current PC and switch port CDP values are shown in the
					 Settings application.

LLDP-MED SW Port

Indicates whether Link Layer Discovery Protocol Media Endpoint
					 Discovery (LLDP-MED) is enabled on the switch port.

LLDP PC Port

Indicates whether Link Layer Discovery Protocol (LLDP) is
					 enabled on the PC port.

LLDP Power Priority

- Unknown - Default

- Low

- High

- Critical

LLDP Asset ID

Identifies the asset ID that is assigned to the device for inventory
					 management.

Switch Port Remote Configuration

Allows the administrator to configure the speed and function
					 of the device table port remotely by using Cisco Unified Communications Manager Administration.

PC Port Remote Configuration

Allows the administrator to configure the speed and function
					 of the device table port remotely by using Cisco Unified Communications Manager Administration.

## Security Information

The Security Information area on the device web page includes information about the CTL and ITL files, and 802.1X authentication.

## Ethernet Statistics

The following Ethernet statistics hyperlinks on 
		  the device web page provide
		  information about network traffic. To display a
		  network statistics area, access the device web page.

Ethernet Information: Provides information about Ethernet
				traffic. The first table describes the items in this area.

Access area: Provides information about network traffic to and
				from 
				the device. The second
				table describes the items in this area.

Network area: Provides information about network traffic to and
				from 
				the device. The second
				table describes the items in this area.

Item

Description

Tx Frames

Total number of packets transmitted by 
					 the device

Tx broadcast

Total number of broadcast packets transmitted by 
					 the device

Tx multicast

Total number of multicast packets transmitted by 
					 the device

Tx unicast

Total number of unicast packets transmitted by 
					 the device

Rx Frames

Total number of packets received by 
					 the device

Rx broadcast

Total number of broadcast packets received by 
					 the device

Rx multicast

Total number of multicast packets received by 
					 the device

Rx unicast

Total number of unicast packets received by 
					 the device

Rx PacketNoDes

Total number of shed packets caused by no Direct Memory Access
					 (DMA) descriptor

Item

Description

Rx totalPkt

Total number of packets received by 
					 the device

Rx crcErr

Total number of packets received with CRC failed

Rx alignErr

Total number of packets received between 64 and 1522 bytes in
					 length with a bad Frame Check Sequence (FCS)

Rx multicast

Total number of multicast packets received by 
					 the device

Rx broadcast

Total number of broadcast packets received by 
					 the device

Rx unicast

Total number of unicast packets received by 
					 the device

Rx shortErr

Total number of FCS error packets or Align error packets
					 received that are less than 64 bytes in size

Rx shortGood

Total number of good packets received that are less than 64
					 bytes size

Rx longGood

Total number of good packets received that are greater than
					 1522 bytes in size

Rx longErr

Total number of FCS error packets or Align error packets
					 received that are greater than 1522 bytes in size

Rx size64

Total number of packets received, including bad packets, that
					 are between 0 and 64 bytes in size

Rx size65to127

Total number of packets received, including bad packets, that
					 are between 65 and 127 bytes in size

Rx size128to255

Total number of packets received, including bad packets, that
					 are between 128 and 255 bytes in size

Rx size256to511

Total number of packets received, including bad packets, that
					 are between 256 and 511 bytes in size

Rx size512to1023

Total number of packets received, including bad packets, that
					 are between 512 and 1023 bytes in size

Rx size1024to1518

Total number of packets received, including bad packets, that
					 are between 1024 and 1518 bytes in size

Rx tokenDrop

Total number of packets dropped due to lack of resources (for
					 example, FIFO overflow)

Tx excessDefer

Total number of packets delayed from transmitting due to
					 medium being busy

Tx lateCollision

Number of times that collisions occurred later than 512 bit
					 times after the start of packet transmission

Tx totalGoodPkt

Total number of good packets (multicast, broadcast, and
					 unicast) received by 
					 the device

Tx Collisions

Total number of collisions that occurred while a packet was
					 being transmitted

Tx excessLength

Total number of packets not transmitted because the packet
					 experienced 16 transmission attempts

Tx broadcast

Total number of broadcast packets transmitted by 
					 the device

Tx multicast

Total number of multicast packets transmitted by 
					 the device

LLDP FramesOutTotal

Total number of LLDP frames sent out from 
					 the device

LLDP AgeoutsTotal

Total number of LLDP frames that have been timed out in cache

LLDP FramesDiscardedTotal

Total number of LLDP frames that are discarded when any of the
					 mandatory TLVs is missing or out of order or contains out-of-range string
					 length

LLDP FramesInErrorsTotal

Total number of LLDP frames received with one or more
					 detectable errors

LLDP FramesInTotal

Total number of LLDP frames received on 
					 the device

LLDP TLVDiscardedTotal

Total number of LLDP TLVs that are discarded

LLDP TLVUnrecognizedTotal

Total number of LLDP TLVs that are not recognized on 
					 the device

CDP Neighbor Device ID

Identifier of a device connected to this port discovered by
					 CDP

CDP Neighbor IP Address

IP address of the neighbor device discovered by CDP

CDP Neighbor Port

Neighbor device port to which 
					 the device is
					 connected discovered by CDP

LLDP Neighbor Device ID

Identifier of a device connected to this port discovered by
					 LLDP

LLDP Neighbor IP Address

IP address of the neighbor device discovered by LLDP

LLDP Neighbor Port

Neighbor device port to which 
					 the device is
					 connected discovered by LLDP

Port Information

Speed and duplex information

## WLAN Setup

Current AP

WLAN Statistics

## Device Logs

The following device log hyperlinks on 
		the device web page provide
		information you can use to help monitor and troubleshoot 
		the device. To access a device
		log area, access the device web page.

Console Logs: Includes hyperlinks to individual log files. The
			 console log files include the current syslog, archived logs from the inactive
			 load, logs from the last reboot, archived logs for the current load, and
			 compressed collections of logs that the Problem Report Tool generates.

Core Dumps: Includes hyperlinks to individual dump files. The core
			 dumps (tombstone_xx) include data from application crashes. The ANR file
			 (traces.txt) includes data for applications that the device determines are not
			 responding and the user chooses to terminate the application.

Status Messages: Includes up to the 50 most recent status messages
			 that 
			 the device has generated
			 since it was last powered up. You can also see this information from the Status
			 Messages screen on the device.

Debug Display: Includes debug messages that might be useful to
			 Cisco TAC if you require assistance with troubleshooting.

## Streaming Statistics

The device streams
		  information when it is on a call or is running a service that sends or receives
		  audio or data.

The streaming statistics areas on 
		  the device web page provide
		  information about the streams.

To display a Streaming Statistics area, access the device web page,
		  and then click a Stream hyperlink.

The following table describes the items in the Streaming
		  Statistics areas.

Item

Description

Remote Address

IP address and UDP port of the destination of the stream.

Local Address

IP address and UDP port of 
					 the device.

Start Time

Internal time stamp that indicates when Cisco Unified Communications Manager requested that 
					 the device start
					 transmitting packets.

Stream Status

Indication of whether streaming is active or not.

Host Name

Unique, fixed name that is automatically assigned to 
					 the device based on
					 its MAC address.

Sender Packets

Total number of RTP data packets that are transmitted by 
					 the device since
					 starting this connection. The value is 0 if the connection is set to Receive
					 Only.

Sender Octets

Total number of payload octets that are transmitted in RTP data packets
					 by 
					 the device since
					 starting this connection. The value is 0 if the connection is set to Receive
					 Only.

Sender Codec

Type of audio encoding that is used for the transmitted stream.

Sender Reports Sent (see note)

Number of times that  the RTCP Sender Report has been sent.

Sender Report Time Sent 
					 (see note)

Internal time stamp indication when the last RTCP Sender
					 Report was sent.

Receiver Lost Packets

Total number of RTP data packets that have been lost since
					 starting receiving data on this connection. Defined as the number of expected
					 packets less the number of packets received, where the number of received
					 packets includes any that are late or duplicate. The value displays as 0 if the
					 connection was set to Send Only.

Avg Jitter

Estimate of mean deviation of the RTP data packet
					 inter-arrival time, measured in milliseconds. The value displays as 0 if the
					 connection was set to Send Only.

Receiver Codec

Type of audio encoding that is used for the received stream.

Receiver Reports Sent 
					 (see note)

Number of times the RTCP Receiver Reports have been sent.

Receiver Report Time Sent 
					 (see note)

Internal time stamp indication when a RTCP Receiver Report was
					 sent.

Receiver Packets

Total number of RTP data packets received by 
					 the device since
					 starting receiving data on this connection. Includes packets received from
					 different sources if this is a multicast call. The value displays as 0 if the
					 connection was set to Send Only.

Receiver Octets

Total number of payload octets received in RTP data packets by
					 the device since starting reception on the connection. Includes packets
					 received from different sources if this is a multicast call. The value displays
					 as 0 if the connection was set to Send Only.

Cumulative Conceal Ratio

Total number of concealment frames divided by total number of
					 speech frames received from start of the voice stream.

Interval Conceal Ratio

Ratio of concealment frames to speech frames in preceding
					 3-second interval of active speech. If  voice activity detection (VAD) is in use, a
					 longer interval might be required to accumulate 3 seconds of active speech.

Max Conceal Ratio

Highest interval concealment ratio from start of the voice
					 stream.

Conceal Secs

Number of seconds that have concealment events (lost frames)
					 from the start of the voice stream (includes severely concealed seconds).

Severely Conceal Secs

Number of seconds that have more than five percent concealment
					 events (lost frames) from the start of the voice stream.

Latency 
					 (see note)

Estimate of the network latency, expressed in milliseconds.
					 Represents a running average of the round-trip delay, measured when RTCP
					 receiver report blocks are received.

Max Jitter

Maximum value of instantaneous jitter, in milliseconds.

Sender Size

RTP packet size, in milliseconds, for the transmitted stream.

Sender Reports Received 
					 (see note)

Number of times RTCP Sender Reports have been received.

Sender Report Time Received 
					 (see note)

Last time at which an RTCP Sender Report was received.

Receiver Size

RTP packet size, in milliseconds, for the received stream.

Receiver Discarded

RTP packets received from network but discarded from jitter
					 buffers.

Receiver Reports Received 
					 (see note)

Number of times RTCP Receiver Reports have been received.

Receiver Report Time Received 
					 (see note)

Last time at which an RTCP Receiver Report was received.

Receiver Encrypted

Indicates if the receiver stream is encrypted.

Sender Encrypted

Indicates if the sender stream is encrypted.

Sender Frames

Number of video frames that by the device transmitted since the video stream opened.

Sender Partial Frames

Number of P-frames that the device sent since the video stream opened.

Sender IFrames

Number of I-frames that the device sent since the video stream opened.

Sender Frame Rate

Rate at which video frames are transmitted (in frames per second).

Sender Bandwidth

Bandwidth of the transmitted video steam in kbps (kilo bits per second).

Sender Resolution

Resolution of the video stream that the device transmits.

Receiver Frames

Number of video frames that the device received since the video stream opened.

Receiver Partial Frames

Number of P-frames that the device received since the video stream opened.

Receiver IFrames

Number of I-frames that the device received since the video stream opened.

Receiver IFrames Req

Number of IDR requests that the device sent to the remote endpoint since the video stream opened.

Receiver Frame Rate

Rate at which video frames are received (in frames per second).

Receiver Frames Lost

Number of frames lost that the video decoder reported since the video stream opened.

Receiver Frames Errors

Number of errors that the video decoder reported since the video stream opened.

Receiver Bandwidth

Bandwidth of the received video steam in kbps (kilo bits per second).

Receiver Resolution

Resolution of the video stream that the phone received from the remote endpoint.

Domain Name

Indicates the domain name.

Sender Joins

Number of times the device has started transmitting a stream

Receiver Joins

Number of times the device has started receiving a stream

Byes

Number of times the device has stopped transmitting a stream

Sender Start Time

Time stamp that indicates when the first RTP packet is sent to the network.

Receiver Start Time

Time stamp that indicates when the first RTP packet is received from the network.

Sender DSCP

DSCP value for sender SIP signaling packets

Receiver DSCP

DSCP value for receiver SIP signaling packets

Sender RTCP DSCP

DSCP value for sender RTP packets

Receiver RTCP DSCP

DSCP value for sender RTP packets

Is Video

Indicates a video call.

Is Presentation

Indicates a presentation call.

Sender Active

Indicates the sender is active.

Receiver Active

Indicates the receiver is active.

When the RTP Control
						Protocol is disabled, no data is generated for this field and therefore it
						displays as 0.

# Remote Monitoring

## Enable and Disable Web Page Access

For security purposes, access to the web pages for the device
		  is disabled by default. This prevents access to the web pages that are described in this
		  chapter and to the 
		  Self Care Portal.

## Access Device Web Page

- Search for the
				device in Cisco Unified Communications Manager by choosing Device > Phone .
				Devices that are registered with Cisco Unified Communications Manager display
				the IP address on the Find and List Phones window and at the top of the Phone
				Configuration window.

- On the device,
				choose Settings > About
					 device > Status > DHCP
					 Information and get the IP address for either Wi-Fi
				or Ethernet.

http://<IP_address>

The web page for the device includes these topics:

Device Information - Provides device settings and related
					 information.

Network Setup - Provides network setup information.

Security Information - Provides security information.

Ethernet Statistics - Includes the following hyperlinks, which
					 provide information about network traffic:

Ethernet Information - Provides information about Ethernet
						  traffic.

Access - Provides information about network traffic to and
						  from 
						  the device.

Network - Provides information about network traffic to
						  and from 
						  the device.

WLAN Setup

Current AP - Provides information about the current access point

WLAN Statistics - Provides information about WLAN traffic

Console Logs - Includes hyperlinks to individual log
						  files.

Core Dumps - Includes hyperlinks to individual dump files.

Status Messages - Provides up to the ten most recent status
						  messages that 
						  the device has
						  generated since it was last powered up.

Debug Display - Provides debug messages that might be
						  useful to Cisco Technical Assistance Center (TAC) if you require assistance
						  with troubleshooting.

Streaming Statistics - Includes the Audio and Video
					 statistics, Stream 1, Stream 2, Stream 3, Stream 4, Stream 5 and Stream 6
					 hyperlinks, which display a variety of streaming statistics.

## Device Information

The Device Information area on 
		  the device web page includes
		  device settings and related information.

Item

Description

Ethernet Network State

Ethernet Network State

Wifi Network State

Wifi Network State

MAC Address

Ethernet MAC Address

WLAN MAC Address

IP address for Wi-Fi connection

Host Name

Unique, fixed name that is automatically assigned to 
					 the device based on
					 its MAC address

Phone DN

Directory number that is assigned to 
					 the device

Version

Identifier of the firmware running on 
					 the device

Hardware Revision

Revision value of 
					 the device hardware

Serial Number

Unique serial number of 
					 the device

Model Number

Model number of 
					 the device

Message Waiting

Indicates whether a voice message is waiting on the primary
					 line for 
					 the device.

UDI

Provides the following Cisco Unique Device Identifier (UDI)
					 information about 
					 the device:

- Device Type: Indicates hardware type.

- Device Description: Provides the name of 
						the device
						that is associated with the indicated model type.

- Serial Number: Specifies the unique serial number of 
						the device.

Time

Time obtained from the Date/Time Group in Cisco Unified Communications Manager to which 
					 the device belongs

Time Zone

Time zone obtained from the Date/Time Group in Cisco Unified Communications Manager to which 
					 the device belongs

Date

Date obtained from the Date/Time Group in Cisco Unified Communications Manager to which 
					 the device belongs

## Network Setup

The Network Setup area on 
		  the device web page provides
		  network setup information and information about other 
		  settings. The
		  following table describes these items.

You can view and set many of these items from the Settings application on the 
		  device.

Item

Description

Wifi Information

Wifi DHCP Server

IP address of the Dynamic Host Configuration Protocol (DHCP)
					 server from which the device obtains its Wifi IP address.

Wifi MAC Address

Wifi Media Access Control (MAC) address of the device.

Wifi Host Name

Hostname that the DHCP server assigned to the device.

Wifi Domain Name

Name of the Domain Name System (DNS) domain in which the device resides.

Wifi IP Address

Internet Protocol (IP) address of the device.

Wifi SubNet Mask

Subnet Mask used by the device.

Wifi Default Router

Default router used by the device.

Wifi DNS Server 1

Primary Domain Name System (DNS) server used by the device.

Wifi DNS Server 2

Optional backup DNS server used by the device.

Wifi EAP Authentication

Indicates EAP authentication setting

Wifi SSID

Indicates the current wifi SSID

Wifi Security Mode

Indicates the current wifi security mode

Wifi 80211 Mode

Indicates the current wifi 80211 mode

Ethernet Information

Ethernet DHCP Server

IP address of the Dynamic Host Configuration Protocol (DHCP)
					 server from which the device obtains its IP address.

Ethernet MAC Address

Media Access Control (MAC) address of the device.

Ethernet Host Name

Hostname that the DHCP server assigned to the device.

Ethernet Domain Name

Name of the Domain Name System (DNS) domain in which the device resides.

Ethernet IP Address

Internet Protocol (IP) address of the device.

Ethernet SubNet Mask

Subnet Mask used by the device.

Ethernet DNS Server 1

Primary Domain Name System (DNS) server used by the device.

Ethernet DNS Server 2

Optional backup DNS server used by the device.

Operational VLAN ID

Auxiliary Virtual Local Area Network (VLAN) configured on a
					 Cisco Catalyst switch in which the device is a member.

Admin. VLAN ID

Auxiliary VLAN in which the device is a member.

PC VLAN

VLAN that is used to identify and remove 802.1P/Q tags from packets
					 sent to the PC.

SW Port Speed

Speed and duplex of the switch port, where:

- A - Auto Negotiate

- 10H -
						10BaseT/half duplex

- 10F -
						10BaseT/full duplex

- 100H -
						100BaseT/half duplex

- 100F -
						100BaseT/full duplex

- 1000F -
						1000BaseT/full duplex

- No Link - No
						connection to the switch port

PC Port Speed

Speed and duplex of the switch port, where:

- A - Auto Negotiate

- 10H -
						10-BaseT/half duplex

- 10F -
						10-BaseT/full duplex

- 100H -
						100-BaseT/half duplex

- 100F -
						100-BaseT/full duplex

- 1000F -
						1000-BaseT/full duplex

- No Link - No
						connection to the switch port

IPv6 Information

IP Addressing Mode

Indicates IP addressing mode.

IP Preference Mode Control

Indicates IP preference mode.

IPv6 Auto Configuration

Indicates if IPv6 auto configuration is enabled or disabled.

Duplicate Address Detection

Indicates if duplicate address detection is enabled or disabled.

Accept Redirect Messages

Indicates if accepting redirect messages is enabled or disabled.

Reply Multicast Echo Request

Indicates if replying to multicast echo requests is enabled or disabled.

IPv6 Address

IPv6 Prefix Length

Indicates IPv6 prefix length.

IPv6 Default Router

Indicates default router.

IPv6 DNS Server 1

Primary DNS server used by the device.

IPv6 DNS Server 2

optional backup DNS server used by the device

IPv6 Alternate TFTP

Indicates whether the device is using an alternative TFTP
					 server.

IPv6 TFTP Server 1

Primary Trivial File Transfer Protocol (TFTP) server used by
					 the device.

IPv6 TFTP Server 2

Backup Trivial File Transfer Protocol (TFTP) server used by
					 the device.

CUCM Configuration

CUCM Server 1-5

Hostnames or IP addresses, in prioritized order, of the Cisco Unified Communications Manager servers with which the device can register. An
					 item can also show the IP address of an SRST router that is capable of
					 providing limited Cisco Unified Communications Manager functionality, if such a
					 router is available.

- Active - Cisco Unified Communications Manager server from which the device is currently
						receiving call-processing services

- Standby - Cisco Unified Communications Manager server to which the device switches if the
						current server becomes unavailable

- Blank - No current
						connection to this Cisco Unified Communications Manager server

An item may also include the Survivable Remote Site Telephony
					 (SRST) designation, which identifies an SRST router that is capable of providing Cisco Unified Communications Manager functionality with a limited feature set. This
					 router assumes control of call processing if all other Cisco Unified Communications Manager servers become unreachable. The SRST Cisco Unified Communications Manager always appears last in the list of servers, even if it
					 is active. You configure the SRST router address in the Device Pool window in Cisco Unified Communications Manager Administration.

Information URL

This feature is not supported on Cisco DX Series devices.

Directories URL

This feature is not supported on Cisco DX Series devices.

Messages URL

This feature is not supported on Cisco DX Series devices.

Services URL

This feature is not supported on Cisco DX Series devices.

Forwarding Delay

The time that is spent in the listening and learning state.

Idle URL

This feature is not supported on Cisco DX Series devices.

Idle URL time

This feature is not supported on Cisco DX Series devices.

Proxy Server URL

This feature is not supported on Cisco DX Series devices.

Authentication URL

This feature is not supported on Cisco DX Series devices.

TFTP Server 1

Primary Trivial File Transfer Protocol (TFTP) server used by
					 the device.

TFTP Server 2

Backup Trivial File Transfer Protocol (TFTP) server used by
					 the device.

Alternate TFTP

Indicates whether the device is using an alternative TFTP
					 server.

User Locale

User locale that is associated with the device user. Identifies a set
					 of detailed information to support users, including language, font, date, and
					 time formatting, and alphanumeric keyboard text information.

Network Locale

Network locale that is associated with the device user. Identifies a
					 set of detailed information to support the device in a specific location,
					 including definitions of the tones and cadences that the device uses.

User Locale Version

Version of the user locale that is loaded on the device.

Network Locale Version

Version of the network locale that is loaded on the device.

PC Port Disabled

Indicates whether the PC port on the device is
					 enabled or disabled.

GARP Enabled

Indicates whether the device learns MAC addresses from
					 Gratuitous ARP responses.

Video Capability Enabled

Indicates whether the device can participate in video calls.

Voice Vlan Access Enabled

Indicates whether the device allows a device attached to the
					 PC port to access the Voice VLAN.

Auto Select Line

Indicates whether auto select line is enabled for the device.

Dscp For Call Control

DSCP IP classification for call control signaling.

Dscp For Setup.

DSCP IP classification for the device configuration transfer.

Dscp For Services

DSCP IP classification for the device-based services.

Security Mode

The security mode that is set for the device.

Web Access

Indicates whether web access is enabled (Yes) or disabled (No)
					 for the device.

Span PC Port

Indicates whether the device will forward packets that are transmitted
					 and received on the network port to the access port.

CDP on PC Port

Indicates whether CDP is supported on the PC port (default is
					 enabled).

When CDP is disabled in Cisco Unified Communications Manager ,
					 a warning is displayed, indicating that disabling CDP on the PC port prevents
					 CVTA from working.

The current PC and switch port CDP values are shown in the
					 Settings application.

CDP on SW Port

Indicates whether CDP is supported on the switch port (default
					 is enabled).

Enable CDP on the switch port for VLAN assignment for the device, power negotiation, QoS management, and 802.1x security.

Enable CDP on the switch port when the device is connected to
					 a Cisco switch.

When CDP is disabled in Cisco Unified Communications Manager ,
					 a warning is presented, indicating that CDP is disabled on the switch port only if
					 the device is connected to a non-Cisco switch.

The current PC and switch port CDP values are shown in the
					 Settings application.

LLDP-MED SW Port

Indicates whether Link Layer Discovery Protocol Media Endpoint
					 Discovery (LLDP-MED) is enabled on the switch port.

LLDP PC Port

Indicates whether Link Layer Discovery Protocol (LLDP) is
					 enabled on the PC port.

LLDP Power Priority

- Unknown - Default

- Low

- High

- Critical

LLDP Asset ID

Identifies the asset ID that is assigned to the device for inventory
					 management.

Switch Port Remote Configuration

Allows the administrator to configure the speed and function
					 of the device table port remotely by using Cisco Unified Communications Manager Administration.

PC Port Remote Configuration

Allows the administrator to configure the speed and function
					 of the device table port remotely by using Cisco Unified Communications Manager Administration.

## Security Information

The Security Information area on the device web page includes information about the CTL and ITL files, and 802.1X authentication.

## Ethernet Statistics

The following Ethernet statistics hyperlinks on 
		  the device web page provide
		  information about network traffic. To display a
		  network statistics area, access the device web page.

Ethernet Information: Provides information about Ethernet
				traffic. The first table describes the items in this area.

Access area: Provides information about network traffic to and
				from 
				the device. The second
				table describes the items in this area.

Network area: Provides information about network traffic to and
				from 
				the device. The second
				table describes the items in this area.

Item

Description

Tx Frames

Total number of packets transmitted by 
					 the device

Tx broadcast

Total number of broadcast packets transmitted by 
					 the device

Tx multicast

Total number of multicast packets transmitted by 
					 the device

Tx unicast

Total number of unicast packets transmitted by 
					 the device

Rx Frames

Total number of packets received by 
					 the device

Rx broadcast

Total number of broadcast packets received by 
					 the device

Rx multicast

Total number of multicast packets received by 
					 the device

Rx unicast

Total number of unicast packets received by 
					 the device

Rx PacketNoDes

Total number of shed packets caused by no Direct Memory Access
					 (DMA) descriptor

Item

Description

Rx totalPkt

Total number of packets received by 
					 the device

Rx crcErr

Total number of packets received with CRC failed

Rx alignErr

Total number of packets received between 64 and 1522 bytes in
					 length with a bad Frame Check Sequence (FCS)

Rx multicast

Total number of multicast packets received by 
					 the device

Rx broadcast

Total number of broadcast packets received by 
					 the device

Rx unicast

Total number of unicast packets received by 
					 the device

Rx shortErr

Total number of FCS error packets or Align error packets
					 received that are less than 64 bytes in size

Rx shortGood

Total number of good packets received that are less than 64
					 bytes size

Rx longGood

Total number of good packets received that are greater than
					 1522 bytes in size

Rx longErr

Total number of FCS error packets or Align error packets
					 received that are greater than 1522 bytes in size

Rx size64

Total number of packets received, including bad packets, that
					 are between 0 and 64 bytes in size

Rx size65to127

Total number of packets received, including bad packets, that
					 are between 65 and 127 bytes in size

Rx size128to255

Total number of packets received, including bad packets, that
					 are between 128 and 255 bytes in size

Rx size256to511

Total number of packets received, including bad packets, that
					 are between 256 and 511 bytes in size

Rx size512to1023

Total number of packets received, including bad packets, that
					 are between 512 and 1023 bytes in size

Rx size1024to1518

Total number of packets received, including bad packets, that
					 are between 1024 and 1518 bytes in size

Rx tokenDrop

Total number of packets dropped due to lack of resources (for
					 example, FIFO overflow)

Tx excessDefer

Total number of packets delayed from transmitting due to
					 medium being busy

Tx lateCollision

Number of times that collisions occurred later than 512 bit
					 times after the start of packet transmission

Tx totalGoodPkt

Total number of good packets (multicast, broadcast, and
					 unicast) received by 
					 the device

Tx Collisions

Total number of collisions that occurred while a packet was
					 being transmitted

Tx excessLength

Total number of packets not transmitted because the packet
					 experienced 16 transmission attempts

Tx broadcast

Total number of broadcast packets transmitted by 
					 the device

Tx multicast

Total number of multicast packets transmitted by 
					 the device

LLDP FramesOutTotal

Total number of LLDP frames sent out from 
					 the device

LLDP AgeoutsTotal

Total number of LLDP frames that have been timed out in cache

LLDP FramesDiscardedTotal

Total number of LLDP frames that are discarded when any of the
					 mandatory TLVs is missing or out of order or contains out-of-range string
					 length

LLDP FramesInErrorsTotal

Total number of LLDP frames received with one or more
					 detectable errors

LLDP FramesInTotal

Total number of LLDP frames received on 
					 the device

LLDP TLVDiscardedTotal

Total number of LLDP TLVs that are discarded

LLDP TLVUnrecognizedTotal

Total number of LLDP TLVs that are not recognized on 
					 the device

CDP Neighbor Device ID

Identifier of a device connected to this port discovered by
					 CDP

CDP Neighbor IP Address

IP address of the neighbor device discovered by CDP

CDP Neighbor Port

Neighbor device port to which 
					 the device is
					 connected discovered by CDP

LLDP Neighbor Device ID

Identifier of a device connected to this port discovered by
					 LLDP

LLDP Neighbor IP Address

IP address of the neighbor device discovered by LLDP

LLDP Neighbor Port

Neighbor device port to which 
					 the device is
					 connected discovered by LLDP

Port Information

Speed and duplex information

## WLAN Setup

Current AP

WLAN Statistics

## Device Logs

The following device log hyperlinks on 
		the device web page provide
		information you can use to help monitor and troubleshoot 
		the device. To access a device
		log area, access the device web page.

Console Logs: Includes hyperlinks to individual log files. The
			 console log files include the current syslog, archived logs from the inactive
			 load, logs from the last reboot, archived logs for the current load, and
			 compressed collections of logs that the Problem Report Tool generates.

Core Dumps: Includes hyperlinks to individual dump files. The core
			 dumps (tombstone_xx) include data from application crashes. The ANR file
			 (traces.txt) includes data for applications that the device determines are not
			 responding and the user chooses to terminate the application.

Status Messages: Includes up to the 50 most recent status messages
			 that 
			 the device has generated
			 since it was last powered up. You can also see this information from the Status
			 Messages screen on the device.

Debug Display: Includes debug messages that might be useful to
			 Cisco TAC if you require assistance with troubleshooting.

## Streaming Statistics

The device streams
		  information when it is on a call or is running a service that sends or receives
		  audio or data.

The streaming statistics areas on 
		  the device web page provide
		  information about the streams.

To display a Streaming Statistics area, access the device web page,
		  and then click a Stream hyperlink.

The following table describes the items in the Streaming
		  Statistics areas.

Item

Description

Remote Address

IP address and UDP port of the destination of the stream.

Local Address

IP address and UDP port of 
					 the device.

Start Time

Internal time stamp that indicates when Cisco Unified Communications Manager requested that 
					 the device start
					 transmitting packets.

Stream Status

Indication of whether streaming is active or not.

Host Name

Unique, fixed name that is automatically assigned to 
					 the device based on
					 its MAC address.

Sender Packets

Total number of RTP data packets that are transmitted by 
					 the device since
					 starting this connection. The value is 0 if the connection is set to Receive
					 Only.

Sender Octets

Total number of payload octets that are transmitted in RTP data packets
					 by 
					 the device since
					 starting this connection. The value is 0 if the connection is set to Receive
					 Only.

Sender Codec

Type of audio encoding that is used for the transmitted stream.

Sender Reports Sent (see note)

Number of times that  the RTCP Sender Report has been sent.

Sender Report Time Sent 
					 (see note)

Internal time stamp indication when the last RTCP Sender
					 Report was sent.

Receiver Lost Packets

Total number of RTP data packets that have been lost since
					 starting receiving data on this connection. Defined as the number of expected
					 packets less the number of packets received, where the number of received
					 packets includes any that are late or duplicate. The value displays as 0 if the
					 connection was set to Send Only.

Avg Jitter

Estimate of mean deviation of the RTP data packet
					 inter-arrival time, measured in milliseconds. The value displays as 0 if the
					 connection was set to Send Only.

Receiver Codec

Type of audio encoding that is used for the received stream.

Receiver Reports Sent 
					 (see note)

Number of times the RTCP Receiver Reports have been sent.

Receiver Report Time Sent 
					 (see note)

Internal time stamp indication when a RTCP Receiver Report was
					 sent.

Receiver Packets

Total number of RTP data packets received by 
					 the device since
					 starting receiving data on this connection. Includes packets received from
					 different sources if this is a multicast call. The value displays as 0 if the
					 connection was set to Send Only.

Receiver Octets

Total number of payload octets received in RTP data packets by
					 the device since starting reception on the connection. Includes packets
					 received from different sources if this is a multicast call. The value displays
					 as 0 if the connection was set to Send Only.

Cumulative Conceal Ratio

Total number of concealment frames divided by total number of
					 speech frames received from start of the voice stream.

Interval Conceal Ratio

Ratio of concealment frames to speech frames in preceding
					 3-second interval of active speech. If  voice activity detection (VAD) is in use, a
					 longer interval might be required to accumulate 3 seconds of active speech.

Max Conceal Ratio

Highest interval concealment ratio from start of the voice
					 stream.

Conceal Secs

Number of seconds that have concealment events (lost frames)
					 from the start of the voice stream (includes severely concealed seconds).

Severely Conceal Secs

Number of seconds that have more than five percent concealment
					 events (lost frames) from the start of the voice stream.

Latency 
					 (see note)

Estimate of the network latency, expressed in milliseconds.
					 Represents a running average of the round-trip delay, measured when RTCP
					 receiver report blocks are received.

Max Jitter

Maximum value of instantaneous jitter, in milliseconds.

Sender Size

RTP packet size, in milliseconds, for the transmitted stream.

Sender Reports Received 
					 (see note)

Number of times RTCP Sender Reports have been received.

Sender Report Time Received 
					 (see note)

Last time at which an RTCP Sender Report was received.

Receiver Size

RTP packet size, in milliseconds, for the received stream.

Receiver Discarded

RTP packets received from network but discarded from jitter
					 buffers.

Receiver Reports Received 
					 (see note)

Number of times RTCP Receiver Reports have been received.

Receiver Report Time Received 
					 (see note)

Last time at which an RTCP Receiver Report was received.

Receiver Encrypted

Indicates if the receiver stream is encrypted.

Sender Encrypted

Indicates if the sender stream is encrypted.

Sender Frames

Number of video frames that by the device transmitted since the video stream opened.

Sender Partial Frames

Number of P-frames that the device sent since the video stream opened.

Sender IFrames

Number of I-frames that the device sent since the video stream opened.

Sender Frame Rate

Rate at which video frames are transmitted (in frames per second).

Sender Bandwidth

Bandwidth of the transmitted video steam in kbps (kilo bits per second).

Sender Resolution

Resolution of the video stream that the device transmits.

Receiver Frames

Number of video frames that the device received since the video stream opened.

Receiver Partial Frames

Number of P-frames that the device received since the video stream opened.

Receiver IFrames

Number of I-frames that the device received since the video stream opened.

Receiver IFrames Req

Number of IDR requests that the device sent to the remote endpoint since the video stream opened.

Receiver Frame Rate

Rate at which video frames are received (in frames per second).

Receiver Frames Lost

Number of frames lost that the video decoder reported since the video stream opened.

Receiver Frames Errors

Number of errors that the video decoder reported since the video stream opened.

Receiver Bandwidth

Bandwidth of the received video steam in kbps (kilo bits per second).

Receiver Resolution

Resolution of the video stream that the phone received from the remote endpoint.

Domain Name

Indicates the domain name.

Sender Joins

Number of times the device has started transmitting a stream

Receiver Joins

Number of times the device has started receiving a stream

Byes

Number of times the device has stopped transmitting a stream

Sender Start Time

Time stamp that indicates when the first RTP packet is sent to the network.

Receiver Start Time

Time stamp that indicates when the first RTP packet is received from the network.

Sender DSCP

DSCP value for sender SIP signaling packets

Receiver DSCP

DSCP value for receiver SIP signaling packets

Sender RTCP DSCP

DSCP value for sender RTP packets

Receiver RTCP DSCP

DSCP value for sender RTP packets

Is Video

Indicates a video call.

Is Presentation

Indicates a presentation call.

Sender Active

Indicates the sender is active.

Receiver Active

Indicates the receiver is active.

When the RTP Control
						Protocol is disabled, no data is generated for this field and therefore it
						displays as 0.

| Step 1 | From Cisco Unified Communications Manager , choose Device > Phone . |
|---|---|
| Step 2 | Specify the criteria to find the device and click Find , or click Find to display a list of all phones. |
| Step 3 | Click the device name to open the Phone
				Configuration window for the device. |
| Step 4 | Scroll down to the Product Specific Configuration section. From
			 the Web Access drop-down list, choose Enabled to enable web page access or choose Disabled to disable web page access. |
| Step 5 | Click Save . Note Some features, such as the Cisco Quality Report Tool, do not
				  function properly without access to the device web pages. Disabling web access
				  also affects any serviceability application that relies on web access. | Note | Some features, such as the Cisco Quality Report Tool, do not
				  function properly without access to the device web pages. Disabling web access
				  also affects any serviceability application that relies on web access. |
| Note | Some features, such as the Cisco Quality Report Tool, do not
				  function properly without access to the device web pages. Disabling web access
				  also affects any serviceability application that relies on web access. |

| Note | Some features, such as the Cisco Quality Report Tool, do not
				  function properly without access to the device web pages. Disabling web access
				  also affects any serviceability application that relies on web access. |
|---|---|

| Step 1 | Use one of
			 these methods to obtain the IP address of 
			 the device: Search for the
				device in Cisco Unified Communications Manager by choosing Device > Phone .
				Devices that are registered with Cisco Unified Communications Manager display
				the IP address on the Find and List Phones window and at the top of the Phone
				Configuration window. On the device,
				choose Settings > About
					 device > Status > DHCP
					 Information and get the IP address for either Wi-Fi
				or Ethernet. |
|---|---|
| Step 2 | Open a web browser and enter the following URL, where <IP_address>
			 is the IP address of the device: http://<IP_address> The web page for the device includes these topics: Device Information - Provides device settings and related
					 information. Network Setup - Provides network setup information. Security Information - Provides security information. Ethernet Statistics - Includes the following hyperlinks, which
					 provide information about network traffic: Ethernet Information - Provides information about Ethernet
						  traffic. Access - Provides information about network traffic to and
						  from 
						  the device. Network - Provides information about network traffic to
						  and from 
						  the device. WLAN Setup Current AP - Provides information about the current access point WLAN Statistics - Provides information about WLAN traffic Device Logs - Includes
				  the following hyperlinks, which provide information that you can use for
				  troubleshooting: Console Logs - Includes hyperlinks to individual log
						  files. Core Dumps - Includes hyperlinks to individual dump files. Status Messages - Provides up to the ten most recent status
						  messages that 
						  the device has
						  generated since it was last powered up. Debug Display - Provides debug messages that might be
						  useful to Cisco Technical Assistance Center (TAC) if you require assistance
						  with troubleshooting. Streaming Statistics - Includes the Audio and Video
					 statistics, Stream 1, Stream 2, Stream 3, Stream 4, Stream 5 and Stream 6
					 hyperlinks, which display a variety of streaming statistics. |

| Item | Description |
|---|---|
| Ethernet Network State | Ethernet Network State |
| Wifi Network State | Wifi Network State |
| MAC Address | Ethernet MAC Address |
| WLAN MAC Address | IP address for Wi-Fi connection |
| Host Name | Unique, fixed name that is automatically assigned to 
					 the device based on
					 its MAC address |
| Phone DN | Directory number that is assigned to 
					 the device |
| Version | Identifier of the firmware running on 
					 the device |
| Hardware Revision | Revision value of 
					 the device hardware |
| Serial Number | Unique serial number of 
					 the device |
| Model Number | Model number of 
					 the device |
| Message Waiting | Indicates whether a voice message is waiting on the primary
					 line for 
					 the device. |
| UDI | Provides the following Cisco Unique Device Identifier (UDI)
					 information about 
					 the device: Device Type: Indicates hardware type. Device Description: Provides the name of 
						the device
						that is associated with the indicated model type. Serial Number: Specifies the unique serial number of 
						the device. |
| Time | Time obtained from the Date/Time Group in Cisco Unified Communications Manager to which 
					 the device belongs |
| Time Zone | Time zone obtained from the Date/Time Group in Cisco Unified Communications Manager to which 
					 the device belongs |
| Date | Date obtained from the Date/Time Group in Cisco Unified Communications Manager to which 
					 the device belongs |

| Item | Description |
|---|---|
| Wifi Information |
| Wifi DHCP Server | IP address of the Dynamic Host Configuration Protocol (DHCP)
					 server from which the device obtains its Wifi IP address. |
| Wifi MAC Address | Wifi Media Access Control (MAC) address of the device. |
| Wifi Host Name | Hostname that the DHCP server assigned to the device. |
| Wifi Domain Name | Name of the Domain Name System (DNS) domain in which the device resides. |
| Wifi IP Address | Internet Protocol (IP) address of the device. |
| Wifi SubNet Mask | Subnet Mask used by the device. |
| Wifi Default Router | Default router used by the device. |
| Wifi DNS Server 1 | Primary Domain Name System (DNS) server used by the device. |
| Wifi DNS Server 2 | Optional backup DNS server used by the device. |
| Wifi EAP Authentication | Indicates EAP authentication setting |
| Wifi SSID | Indicates the current wifi SSID |
| Wifi Security Mode | Indicates the current wifi security mode |
| Wifi 80211 Mode | Indicates the current wifi 80211 mode |
| Ethernet Information |
| Ethernet DHCP Server | IP address of the Dynamic Host Configuration Protocol (DHCP)
					 server from which the device obtains its IP address. |
| Ethernet MAC Address | Media Access Control (MAC) address of the device. |
| Ethernet Host Name | Hostname that the DHCP server assigned to the device. |
| Ethernet Domain Name | Name of the Domain Name System (DNS) domain in which the device resides. |
| Ethernet IP Address | Internet Protocol (IP) address of the device. |
| Ethernet SubNet Mask | Subnet Mask used by the device. |
| Ethernet DNS Server 1 | Primary Domain Name System (DNS) server used by the device. |
| Ethernet DNS Server 2 | Optional backup DNS server used by the device. |
| Operational VLAN ID | Auxiliary Virtual Local Area Network (VLAN) configured on a
					 Cisco Catalyst switch in which the device is a member. |
| Admin. VLAN ID | Auxiliary VLAN in which the device is a member. |
| PC VLAN | VLAN that is used to identify and remove 802.1P/Q tags from packets
					 sent to the PC. |
| SW Port Speed | Speed and duplex of the switch port, where: A - Auto Negotiate 10H -
						10BaseT/half duplex 10F -
						10BaseT/full duplex 100H -
						100BaseT/half duplex 100F -
						100BaseT/full duplex 1000F -
						1000BaseT/full duplex No Link - No
						connection to the switch port |
| PC Port Speed | Speed and duplex of the switch port, where: A - Auto Negotiate 10H -
						10-BaseT/half duplex 10F -
						10-BaseT/full duplex 100H -
						100-BaseT/half duplex 100F -
						100-BaseT/full duplex 1000F -
						1000-BaseT/full duplex No Link - No
						connection to the switch port |
| IPv6 Information |
| IP Addressing Mode | Indicates IP addressing mode. |
| IP Preference Mode Control | Indicates IP preference mode. |
| IPv6 Auto Configuration | Indicates if IPv6 auto configuration is enabled or disabled. |
| Duplicate Address Detection | Indicates if duplicate address detection is enabled or disabled. |
| Accept Redirect Messages | Indicates if accepting redirect messages is enabled or disabled. |
| Reply Multicast Echo Request | Indicates if replying to multicast echo requests is enabled or disabled. |
| IPv6 Address | Internet Protocol version 6 (IPv6) address of the phone. |
| IPv6 Prefix Length | Indicates IPv6 prefix length. |
| IPv6 Default Router | Indicates default router. |
| IPv6 DNS Server 1 | Primary DNS server used by the device. |
| IPv6 DNS Server 2 | optional backup DNS server used by the device |
| IPv6 Alternate TFTP | Indicates whether the device is using an alternative TFTP
					 server. |
| IPv6 TFTP Server 1 | Primary Trivial File Transfer Protocol (TFTP) server used by
					 the device. |
| IPv6 TFTP Server 2 | Backup Trivial File Transfer Protocol (TFTP) server used by
					 the device. |
| CUCM Configuration |
| CUCM Server 1-5 | Hostnames or IP addresses, in prioritized order, of the Cisco Unified Communications Manager servers with which the device can register. An
					 item can also show the IP address of an SRST router that is capable of
					 providing limited Cisco Unified Communications Manager functionality, if such a
					 router is available. For an available server, an item shows the Cisco Unified Communications Manager server IP address and one of the following states: Active - Cisco Unified Communications Manager server from which the device is currently
						receiving call-processing services Standby - Cisco Unified Communications Manager server to which the device switches if the
						current server becomes unavailable Blank - No current
						connection to this Cisco Unified Communications Manager server An item may also include the Survivable Remote Site Telephony
					 (SRST) designation, which identifies an SRST router that is capable of providing Cisco Unified Communications Manager functionality with a limited feature set. This
					 router assumes control of call processing if all other Cisco Unified Communications Manager servers become unreachable. The SRST Cisco Unified Communications Manager always appears last in the list of servers, even if it
					 is active. You configure the SRST router address in the Device Pool window in Cisco Unified Communications Manager Administration. |
| Information URL | This feature is not supported on Cisco DX Series devices. |
| Directories URL | This feature is not supported on Cisco DX Series devices. |
| Messages URL | This feature is not supported on Cisco DX Series devices. |
| Services URL | This feature is not supported on Cisco DX Series devices. |
| Forwarding Delay | The time that is spent in the listening and learning state. |
| Idle URL | This feature is not supported on Cisco DX Series devices. |
| Idle URL time | This feature is not supported on Cisco DX Series devices. |
| Proxy Server URL | This feature is not supported on Cisco DX Series devices. |
| Authentication URL | This feature is not supported on Cisco DX Series devices. |
| TFTP Server 1 | Primary Trivial File Transfer Protocol (TFTP) server used by
					 the device. |
| TFTP Server 2 | Backup Trivial File Transfer Protocol (TFTP) server used by
					 the device. |
| Alternate TFTP | Indicates whether the device is using an alternative TFTP
					 server. |
| User Locale | User locale that is associated with the device user. Identifies a set
					 of detailed information to support users, including language, font, date, and
					 time formatting, and alphanumeric keyboard text information. |
| Network Locale | Network locale that is associated with the device user. Identifies a
					 set of detailed information to support the device in a specific location,
					 including definitions of the tones and cadences that the device uses. |
| User Locale Version | Version of the user locale that is loaded on the device. |
| Network Locale Version | Version of the network locale that is loaded on the device. |
| PC Port Disabled | Indicates whether the PC port on the device is
					 enabled or disabled. |
| GARP Enabled | Indicates whether the device learns MAC addresses from
					 Gratuitous ARP responses. |
| Video Capability Enabled | Indicates whether the device can participate in video calls. |
| Voice Vlan Access Enabled | Indicates whether the device allows a device attached to the
					 PC port to access the Voice VLAN. |
| Auto Select Line | Indicates whether auto select line is enabled for the device. |
| Dscp For Call Control | DSCP IP classification for call control signaling. |
| Dscp For Setup. | DSCP IP classification for the device configuration transfer. |
| Dscp For Services | DSCP IP classification for the device-based services. |
| Security Mode | The security mode that is set for the device. |
| Web Access | Indicates whether web access is enabled (Yes) or disabled (No)
					 for the device. |
| Span PC Port | Indicates whether the device will forward packets that are transmitted
					 and received on the network port to the access port. |
| CDP on PC Port | Indicates whether CDP is supported on the PC port (default is
					 enabled). When CDP is disabled in Cisco Unified Communications Manager ,
					 a warning is displayed, indicating that disabling CDP on the PC port prevents
					 CVTA from working. The current PC and switch port CDP values are shown in the
					 Settings application. |
| CDP on SW Port | Indicates whether CDP is supported on the switch port (default
					 is enabled). Enable CDP on the switch port for VLAN assignment for the device, power negotiation, QoS management, and 802.1x security. Enable CDP on the switch port when the device is connected to
					 a Cisco switch. When CDP is disabled in Cisco Unified Communications Manager ,
					 a warning is presented, indicating that CDP is disabled on the switch port only if
					 the device is connected to a non-Cisco switch. The current PC and switch port CDP values are shown in the
					 Settings application. |
| LLDP-MED SW Port | Indicates whether Link Layer Discovery Protocol Media Endpoint
					 Discovery (LLDP-MED) is enabled on the switch port. |
| LLDP PC Port | Indicates whether Link Layer Discovery Protocol (LLDP) is
					 enabled on the PC port. |
| LLDP Power Priority | Advertises the device power priority to the switch, enabling
					 the switch to appropriately provide power to the device. Settings include: Unknown - Default Low High Critical |
| LLDP Asset ID | Identifies the asset ID that is assigned to the device for inventory
					 management. |
| Switch Port Remote Configuration | Allows the administrator to configure the speed and function
					 of the device table port remotely by using Cisco Unified Communications Manager Administration. |
| PC Port Remote Configuration | Allows the administrator to configure the speed and function
					 of the device table port remotely by using Cisco Unified Communications Manager Administration. |

| Item | Description |
|---|---|
| Signaling Security Mode | Indicates signaling security mode. |
| LSC | Indicates whether LSC is installed on the device. |
| CAPF Server (IPv4) | Indicates CAPF server address for IPv4 |
| CAPF Server (IPv6) | Indicates CAPF server address for IPv6 |
| CAPF Port | Indicates CAPF port |
| CTL File |
| CTL Signature | Displays CTL signature |
| CUCM Server/TFTP Server | Indicates CUCM/TFTP server addresses |
| Application Server | Indicates application server |
| CAPF Server | Indicates CAPF server |
| ITL File |
| ITL Signature | Displays ITL signature |
| CAPF Server | Indicates CAPF server |
| TVS | Indicates TVS addresses |
| CUCM Server/TFTP Server | Indicates CUCM/TFTP server addresses |
| Configuration File | Indicates whether ITL configuration file is installed on the device |
| 802.1X Authentication |
| Device Authentication | Indicates whether 802.1X device authentication is enabled. |
| Transaction Status | Indicates whether 802.1X transaction status is enabled. |
| Protocol | Indicates 802.1X protocol. |
| Device ID | Displays device ID. |

| Item | Description |
|---|---|
| Tx Frames | Total number of packets transmitted by 
					 the device |
| Tx broadcast | Total number of broadcast packets transmitted by 
					 the device |
| Tx multicast | Total number of multicast packets transmitted by 
					 the device |
| Tx unicast | Total number of unicast packets transmitted by 
					 the device |
| Rx Frames | Total number of packets received by 
					 the device |
| Rx broadcast | Total number of broadcast packets received by 
					 the device |
| Rx multicast | Total number of multicast packets received by 
					 the device |
| Rx unicast | Total number of unicast packets received by 
					 the device |
| Rx PacketNoDes | Total number of shed packets caused by no Direct Memory Access
					 (DMA) descriptor |

| Item | Description |
|---|---|
| Rx totalPkt | Total number of packets received by 
					 the device |
| Rx crcErr | Total number of packets received with CRC failed |
| Rx alignErr | Total number of packets received between 64 and 1522 bytes in
					 length with a bad Frame Check Sequence (FCS) |
| Rx multicast | Total number of multicast packets received by 
					 the device |
| Rx broadcast | Total number of broadcast packets received by 
					 the device |
| Rx unicast | Total number of unicast packets received by 
					 the device |
| Rx shortErr | Total number of FCS error packets or Align error packets
					 received that are less than 64 bytes in size |
| Rx shortGood | Total number of good packets received that are less than 64
					 bytes size |
| Rx longGood | Total number of good packets received that are greater than
					 1522 bytes in size |
| Rx longErr | Total number of FCS error packets or Align error packets
					 received that are greater than 1522 bytes in size |
| Rx size64 | Total number of packets received, including bad packets, that
					 are between 0 and 64 bytes in size |
| Rx size65to127 | Total number of packets received, including bad packets, that
					 are between 65 and 127 bytes in size |
| Rx size128to255 | Total number of packets received, including bad packets, that
					 are between 128 and 255 bytes in size |
| Rx size256to511 | Total number of packets received, including bad packets, that
					 are between 256 and 511 bytes in size |
| Rx size512to1023 | Total number of packets received, including bad packets, that
					 are between 512 and 1023 bytes in size |
| Rx size1024to1518 | Total number of packets received, including bad packets, that
					 are between 1024 and 1518 bytes in size |
| Rx tokenDrop | Total number of packets dropped due to lack of resources (for
					 example, FIFO overflow) |
| Tx excessDefer | Total number of packets delayed from transmitting due to
					 medium being busy |
| Tx lateCollision | Number of times that collisions occurred later than 512 bit
					 times after the start of packet transmission |
| Tx totalGoodPkt | Total number of good packets (multicast, broadcast, and
					 unicast) received by 
					 the device |
| Tx Collisions | Total number of collisions that occurred while a packet was
					 being transmitted |
| Tx excessLength | Total number of packets not transmitted because the packet
					 experienced 16 transmission attempts |
| Tx broadcast | Total number of broadcast packets transmitted by 
					 the device |
| Tx multicast | Total number of multicast packets transmitted by 
					 the device |
| LLDP FramesOutTotal | Total number of LLDP frames sent out from 
					 the device |
| LLDP AgeoutsTotal | Total number of LLDP frames that have been timed out in cache |
| LLDP FramesDiscardedTotal | Total number of LLDP frames that are discarded when any of the
					 mandatory TLVs is missing or out of order or contains out-of-range string
					 length |
| LLDP FramesInErrorsTotal | Total number of LLDP frames received with one or more
					 detectable errors |
| LLDP FramesInTotal | Total number of LLDP frames received on 
					 the device |
| LLDP TLVDiscardedTotal | Total number of LLDP TLVs that are discarded |
| LLDP TLVUnrecognizedTotal | Total number of LLDP TLVs that are not recognized on 
					 the device |
| CDP Neighbor Device ID | Identifier of a device connected to this port discovered by
					 CDP |
| CDP Neighbor IP Address | IP address of the neighbor device discovered by CDP |
| CDP Neighbor Port | Neighbor device port to which 
					 the device is
					 connected discovered by CDP |
| LLDP Neighbor Device ID | Identifier of a device connected to this port discovered by
					 LLDP |
| LLDP Neighbor IP Address | IP address of the neighbor device discovered by LLDP |
| LLDP Neighbor Port | Neighbor device port to which 
					 the device is
					 connected discovered by LLDP |
| Port Information | Speed and duplex information |

| Item | Description |
|---|---|
| AP Name | Provides the current access point name. |
| MAC Address | Provides the MAC address of the access point. |
| Current Channel | The latest channel where this AP was observed. |
| Last RSSI | The latest RSSI in which this AP was observed. |
| Beacon Interval | Number of time units between beacons. A time unit is 1.024 ms. |
| Min Rate | Minimum data rate that the AP requires. |
| Max Rate | Maximum data rate that the AP requires. |
| WMM Supported | Support for Wi-Fi multimedia extensions. |
| UAPSD Supported | The AP supports Unscheduled Automatic Power Save Delivery. May only be available if WMM is supported. This feature is critical for talk time and for achieving maximum call density. |
| Noise | Indicates the current noise level. |
| Load | Indicates the current load. |
| Quality | Indicates voice quality. |

| Item | Description |
|---|---|
| NetDevice Stats |
| Tx bytes | Total number of bytes that the device transmits. |
| Rx Bytes | Total number of bytes that the device receives. |
| Tx Packets | Total number of packets that the device transmits. |
| Rx Packets | Total number of packets that the device receives. |
| Tx Packets Dropped | Total number of transmitted packets that the device dropped. |
| Rx Packets Dropped | Total number of received packets that the device dropped. |
| Tx Packets Error | Total number of transmitted error packets. |
| Rx Packets Error | Total number of received error packets. |
| Firmware Stats |
| Multicast Tx Frames | Total number of multicast packets that the device transmitted. |
| Failed | Transmission of packet failed. |
| Retry | Counter of total retries. |
| Multiple Retry | Transmission of packet required two or more retries before success. |
| Frame Dup | Number of duplicate packets received by the device. |
| Rts Success | A corresponding CTS was received. |
| Rts Failure | A corresponding CTS was not received. |
| Ack Failure | AP did not acknowledge a transmission. |
| Rx Frag | Number of fragmented packets that the device received. |
| Multicast Rx Frame | Number of multicast packets that the device received. |
| FCS Error | Increments when a Frame Checksum (FCS) error is detected in a received MPDU. |
| Tx Frames | Number of packets that the device sent. |
| Roaming Stats |
| current/total | Current roaming time/total roaming time in ms. |

| Item | Description |
|---|---|
| Remote Address | IP address and UDP port of the destination of the stream. |
| Local Address | IP address and UDP port of 
					 the device. |
| Start Time | Internal time stamp that indicates when Cisco Unified Communications Manager requested that 
					 the device start
					 transmitting packets. |
| Stream Status | Indication of whether streaming is active or not. |
| Host Name | Unique, fixed name that is automatically assigned to 
					 the device based on
					 its MAC address. |
| Sender Packets | Total number of RTP data packets that are transmitted by 
					 the device since
					 starting this connection. The value is 0 if the connection is set to Receive
					 Only. |
| Sender Octets | Total number of payload octets that are transmitted in RTP data packets
					 by 
					 the device since
					 starting this connection. The value is 0 if the connection is set to Receive
					 Only. |
| Sender Codec | Type of audio encoding that is used for the transmitted stream. |
| Sender Reports Sent (see note) | Number of times that  the RTCP Sender Report has been sent. |
| Sender Report Time Sent 
					 (see note) | Internal time stamp indication when the last RTCP Sender
					 Report was sent. |
| Receiver Lost Packets | Total number of RTP data packets that have been lost since
					 starting receiving data on this connection. Defined as the number of expected
					 packets less the number of packets received, where the number of received
					 packets includes any that are late or duplicate. The value displays as 0 if the
					 connection was set to Send Only. |
| Avg Jitter | Estimate of mean deviation of the RTP data packet
					 inter-arrival time, measured in milliseconds. The value displays as 0 if the
					 connection was set to Send Only. |
| Receiver Codec | Type of audio encoding that is used for the received stream. |
| Receiver Reports Sent 
					 (see note) | Number of times the RTCP Receiver Reports have been sent. |
| Receiver Report Time Sent 
					 (see note) | Internal time stamp indication when a RTCP Receiver Report was
					 sent. |
| Receiver Packets | Total number of RTP data packets received by 
					 the device since
					 starting receiving data on this connection. Includes packets received from
					 different sources if this is a multicast call. The value displays as 0 if the
					 connection was set to Send Only. |
| Receiver Octets | Total number of payload octets received in RTP data packets by
					 the device since starting reception on the connection. Includes packets
					 received from different sources if this is a multicast call. The value displays
					 as 0 if the connection was set to Send Only. |
| Cumulative Conceal Ratio | Total number of concealment frames divided by total number of
					 speech frames received from start of the voice stream. |
| Interval Conceal Ratio | Ratio of concealment frames to speech frames in preceding
					 3-second interval of active speech. If  voice activity detection (VAD) is in use, a
					 longer interval might be required to accumulate 3 seconds of active speech. |
| Max Conceal Ratio | Highest interval concealment ratio from start of the voice
					 stream. |
| Conceal Secs | Number of seconds that have concealment events (lost frames)
					 from the start of the voice stream (includes severely concealed seconds). |
| Severely Conceal Secs | Number of seconds that have more than five percent concealment
					 events (lost frames) from the start of the voice stream. |
| Latency 
					 (see note) | Estimate of the network latency, expressed in milliseconds.
					 Represents a running average of the round-trip delay, measured when RTCP
					 receiver report blocks are received. |
| Max Jitter | Maximum value of instantaneous jitter, in milliseconds. |
| Sender Size | RTP packet size, in milliseconds, for the transmitted stream. |
| Sender Reports Received 
					 (see note) | Number of times RTCP Sender Reports have been received. |
| Sender Report Time Received 
					 (see note) | Last time at which an RTCP Sender Report was received. |
| Receiver Size | RTP packet size, in milliseconds, for the received stream. |
| Receiver Discarded | RTP packets received from network but discarded from jitter
					 buffers. |
| Receiver Reports Received 
					 (see note) | Number of times RTCP Receiver Reports have been received. |
| Receiver Report Time Received 
					 (see note) | Last time at which an RTCP Receiver Report was received. |
| Receiver Encrypted | Indicates if the receiver stream is encrypted. |
| Sender Encrypted | Indicates if the sender stream is encrypted. |
| Sender Frames | Number of video frames that by the device transmitted since the video stream opened. |
| Sender Partial Frames | Number of P-frames that the device sent since the video stream opened. |
| Sender IFrames | Number of I-frames that the device sent since the video stream opened. |
| Sender Frame Rate | Rate at which video frames are transmitted (in frames per second). |
| Sender Bandwidth | Bandwidth of the transmitted video steam in kbps (kilo bits per second). |
| Sender Resolution | Resolution of the video stream that the device transmits. |
| Receiver Frames | Number of video frames that the device received since the video stream opened. |
| Receiver Partial Frames | Number of P-frames that the device received since the video stream opened. |
| Receiver IFrames | Number of I-frames that the device received since the video stream opened. |
| Receiver IFrames Req | Number of IDR requests that the device sent to the remote endpoint since the video stream opened. |
| Receiver Frame Rate | Rate at which video frames are received (in frames per second). |
| Receiver Frames Lost | Number of frames lost that the video decoder reported since the video stream opened. |
| Receiver Frames Errors | Number of errors that the video decoder reported since the video stream opened. |
| Receiver Bandwidth | Bandwidth of the received video steam in kbps (kilo bits per second). |
| Receiver Resolution | Resolution of the video stream that the phone received from the remote endpoint. |
| Domain Name | Indicates the domain name. |
| Sender Joins | Number of times the device has started transmitting a stream |
| Receiver Joins | Number of times the device has started receiving a stream |
| Byes | Number of times the device has stopped transmitting a stream |
| Sender Start Time | Time stamp that indicates when the first RTP packet is sent to the network. |
| Receiver Start Time | Time stamp that indicates when the first RTP packet is received from the network. |
| Sender DSCP | DSCP value for sender SIP signaling packets |
| Receiver DSCP | DSCP value for receiver SIP signaling packets |
| Sender RTCP DSCP | DSCP value for sender RTP packets |
| Receiver RTCP DSCP | DSCP value for sender RTP packets |
| Is Video | Indicates a video call. |
| Is Presentation | Indicates a presentation call. |
| Sender Active | Indicates the sender is active. |
| Receiver Active | Indicates the receiver is active. |

| Note | When the RTP Control
						Protocol is disabled, no data is generated for this field and therefore it
						displays as 0. |
|---|---|

| Step 1 | From Cisco Unified Communications Manager , choose Device > Phone . |
|---|---|
| Step 2 | Specify the criteria to find the device and click Find , or click Find to display a list of all phones. |
| Step 3 | Click the device name to open the Phone
				Configuration window for the device. |
| Step 4 | Scroll down to the Product Specific Configuration section. From
			 the Web Access drop-down list, choose Enabled to enable web page access or choose Disabled to disable web page access. |
| Step 5 | Click Save . Note Some features, such as the Cisco Quality Report Tool, do not
				  function properly without access to the device web pages. Disabling web access
				  also affects any serviceability application that relies on web access. | Note | Some features, such as the Cisco Quality Report Tool, do not
				  function properly without access to the device web pages. Disabling web access
				  also affects any serviceability application that relies on web access. |
| Note | Some features, such as the Cisco Quality Report Tool, do not
				  function properly without access to the device web pages. Disabling web access
				  also affects any serviceability application that relies on web access. |

| Note | Some features, such as the Cisco Quality Report Tool, do not
				  function properly without access to the device web pages. Disabling web access
				  also affects any serviceability application that relies on web access. |
|---|---|

| Step 1 | Use one of
			 these methods to obtain the IP address of 
			 the device: Search for the
				device in Cisco Unified Communications Manager by choosing Device > Phone .
				Devices that are registered with Cisco Unified Communications Manager display
				the IP address on the Find and List Phones window and at the top of the Phone
				Configuration window. On the device,
				choose Settings > About
					 device > Status > DHCP
					 Information and get the IP address for either Wi-Fi
				or Ethernet. |
|---|---|
| Step 2 | Open a web browser and enter the following URL, where <IP_address>
			 is the IP address of the device: http://<IP_address> The web page for the device includes these topics: Device Information - Provides device settings and related
					 information. Network Setup - Provides network setup information. Security Information - Provides security information. Ethernet Statistics - Includes the following hyperlinks, which
					 provide information about network traffic: Ethernet Information - Provides information about Ethernet
						  traffic. Access - Provides information about network traffic to and
						  from 
						  the device. Network - Provides information about network traffic to
						  and from 
						  the device. WLAN Setup Current AP - Provides information about the current access point WLAN Statistics - Provides information about WLAN traffic Device Logs - Includes
				  the following hyperlinks, which provide information that you can use for
				  troubleshooting: Console Logs - Includes hyperlinks to individual log
						  files. Core Dumps - Includes hyperlinks to individual dump files. Status Messages - Provides up to the ten most recent status
						  messages that 
						  the device has
						  generated since it was last powered up. Debug Display - Provides debug messages that might be
						  useful to Cisco Technical Assistance Center (TAC) if you require assistance
						  with troubleshooting. Streaming Statistics - Includes the Audio and Video
					 statistics, Stream 1, Stream 2, Stream 3, Stream 4, Stream 5 and Stream 6
					 hyperlinks, which display a variety of streaming statistics. |

| Item | Description |
|---|---|
| Ethernet Network State | Ethernet Network State |
| Wifi Network State | Wifi Network State |
| MAC Address | Ethernet MAC Address |
| WLAN MAC Address | IP address for Wi-Fi connection |
| Host Name | Unique, fixed name that is automatically assigned to 
					 the device based on
					 its MAC address |
| Phone DN | Directory number that is assigned to 
					 the device |
| Version | Identifier of the firmware running on 
					 the device |
| Hardware Revision | Revision value of 
					 the device hardware |
| Serial Number | Unique serial number of 
					 the device |
| Model Number | Model number of 
					 the device |
| Message Waiting | Indicates whether a voice message is waiting on the primary
					 line for 
					 the device. |
| UDI | Provides the following Cisco Unique Device Identifier (UDI)
					 information about 
					 the device: Device Type: Indicates hardware type. Device Description: Provides the name of 
						the device
						that is associated with the indicated model type. Serial Number: Specifies the unique serial number of 
						the device. |
| Time | Time obtained from the Date/Time Group in Cisco Unified Communications Manager to which 
					 the device belongs |
| Time Zone | Time zone obtained from the Date/Time Group in Cisco Unified Communications Manager to which 
					 the device belongs |
| Date | Date obtained from the Date/Time Group in Cisco Unified Communications Manager to which 
					 the device belongs |

| Item | Description |
|---|---|
| Wifi Information |
| Wifi DHCP Server | IP address of the Dynamic Host Configuration Protocol (DHCP)
					 server from which the device obtains its Wifi IP address. |
| Wifi MAC Address | Wifi Media Access Control (MAC) address of the device. |
| Wifi Host Name | Hostname that the DHCP server assigned to the device. |
| Wifi Domain Name | Name of the Domain Name System (DNS) domain in which the device resides. |
| Wifi IP Address | Internet Protocol (IP) address of the device. |
| Wifi SubNet Mask | Subnet Mask used by the device. |
| Wifi Default Router | Default router used by the device. |
| Wifi DNS Server 1 | Primary Domain Name System (DNS) server used by the device. |
| Wifi DNS Server 2 | Optional backup DNS server used by the device. |
| Wifi EAP Authentication | Indicates EAP authentication setting |
| Wifi SSID | Indicates the current wifi SSID |
| Wifi Security Mode | Indicates the current wifi security mode |
| Wifi 80211 Mode | Indicates the current wifi 80211 mode |
| Ethernet Information |
| Ethernet DHCP Server | IP address of the Dynamic Host Configuration Protocol (DHCP)
					 server from which the device obtains its IP address. |
| Ethernet MAC Address | Media Access Control (MAC) address of the device. |
| Ethernet Host Name | Hostname that the DHCP server assigned to the device. |
| Ethernet Domain Name | Name of the Domain Name System (DNS) domain in which the device resides. |
| Ethernet IP Address | Internet Protocol (IP) address of the device. |
| Ethernet SubNet Mask | Subnet Mask used by the device. |
| Ethernet DNS Server 1 | Primary Domain Name System (DNS) server used by the device. |
| Ethernet DNS Server 2 | Optional backup DNS server used by the device. |
| Operational VLAN ID | Auxiliary Virtual Local Area Network (VLAN) configured on a
					 Cisco Catalyst switch in which the device is a member. |
| Admin. VLAN ID | Auxiliary VLAN in which the device is a member. |
| PC VLAN | VLAN that is used to identify and remove 802.1P/Q tags from packets
					 sent to the PC. |
| SW Port Speed | Speed and duplex of the switch port, where: A - Auto Negotiate 10H -
						10BaseT/half duplex 10F -
						10BaseT/full duplex 100H -
						100BaseT/half duplex 100F -
						100BaseT/full duplex 1000F -
						1000BaseT/full duplex No Link - No
						connection to the switch port |
| PC Port Speed | Speed and duplex of the switch port, where: A - Auto Negotiate 10H -
						10-BaseT/half duplex 10F -
						10-BaseT/full duplex 100H -
						100-BaseT/half duplex 100F -
						100-BaseT/full duplex 1000F -
						1000-BaseT/full duplex No Link - No
						connection to the switch port |
| IPv6 Information |
| IP Addressing Mode | Indicates IP addressing mode. |
| IP Preference Mode Control | Indicates IP preference mode. |
| IPv6 Auto Configuration | Indicates if IPv6 auto configuration is enabled or disabled. |
| Duplicate Address Detection | Indicates if duplicate address detection is enabled or disabled. |
| Accept Redirect Messages | Indicates if accepting redirect messages is enabled or disabled. |
| Reply Multicast Echo Request | Indicates if replying to multicast echo requests is enabled or disabled. |
| IPv6 Address | Internet Protocol version 6 (IPv6) address of the phone. |
| IPv6 Prefix Length | Indicates IPv6 prefix length. |
| IPv6 Default Router | Indicates default router. |
| IPv6 DNS Server 1 | Primary DNS server used by the device. |
| IPv6 DNS Server 2 | optional backup DNS server used by the device |
| IPv6 Alternate TFTP | Indicates whether the device is using an alternative TFTP
					 server. |
| IPv6 TFTP Server 1 | Primary Trivial File Transfer Protocol (TFTP) server used by
					 the device. |
| IPv6 TFTP Server 2 | Backup Trivial File Transfer Protocol (TFTP) server used by
					 the device. |
| CUCM Configuration |
| CUCM Server 1-5 | Hostnames or IP addresses, in prioritized order, of the Cisco Unified Communications Manager servers with which the device can register. An
					 item can also show the IP address of an SRST router that is capable of
					 providing limited Cisco Unified Communications Manager functionality, if such a
					 router is available. For an available server, an item shows the Cisco Unified Communications Manager server IP address and one of the following states: Active - Cisco Unified Communications Manager server from which the device is currently
						receiving call-processing services Standby - Cisco Unified Communications Manager server to which the device switches if the
						current server becomes unavailable Blank - No current
						connection to this Cisco Unified Communications Manager server An item may also include the Survivable Remote Site Telephony
					 (SRST) designation, which identifies an SRST router that is capable of providing Cisco Unified Communications Manager functionality with a limited feature set. This
					 router assumes control of call processing if all other Cisco Unified Communications Manager servers become unreachable. The SRST Cisco Unified Communications Manager always appears last in the list of servers, even if it
					 is active. You configure the SRST router address in the Device Pool window in Cisco Unified Communications Manager Administration. |
| Information URL | This feature is not supported on Cisco DX Series devices. |
| Directories URL | This feature is not supported on Cisco DX Series devices. |
| Messages URL | This feature is not supported on Cisco DX Series devices. |
| Services URL | This feature is not supported on Cisco DX Series devices. |
| Forwarding Delay | The time that is spent in the listening and learning state. |
| Idle URL | This feature is not supported on Cisco DX Series devices. |
| Idle URL time | This feature is not supported on Cisco DX Series devices. |
| Proxy Server URL | This feature is not supported on Cisco DX Series devices. |
| Authentication URL | This feature is not supported on Cisco DX Series devices. |
| TFTP Server 1 | Primary Trivial File Transfer Protocol (TFTP) server used by
					 the device. |
| TFTP Server 2 | Backup Trivial File Transfer Protocol (TFTP) server used by
					 the device. |
| Alternate TFTP | Indicates whether the device is using an alternative TFTP
					 server. |
| User Locale | User locale that is associated with the device user. Identifies a set
					 of detailed information to support users, including language, font, date, and
					 time formatting, and alphanumeric keyboard text information. |
| Network Locale | Network locale that is associated with the device user. Identifies a
					 set of detailed information to support the device in a specific location,
					 including definitions of the tones and cadences that the device uses. |
| User Locale Version | Version of the user locale that is loaded on the device. |
| Network Locale Version | Version of the network locale that is loaded on the device. |
| PC Port Disabled | Indicates whether the PC port on the device is
					 enabled or disabled. |
| GARP Enabled | Indicates whether the device learns MAC addresses from
					 Gratuitous ARP responses. |
| Video Capability Enabled | Indicates whether the device can participate in video calls. |
| Voice Vlan Access Enabled | Indicates whether the device allows a device attached to the
					 PC port to access the Voice VLAN. |
| Auto Select Line | Indicates whether auto select line is enabled for the device. |
| Dscp For Call Control | DSCP IP classification for call control signaling. |
| Dscp For Setup. | DSCP IP classification for the device configuration transfer. |
| Dscp For Services | DSCP IP classification for the device-based services. |
| Security Mode | The security mode that is set for the device. |
| Web Access | Indicates whether web access is enabled (Yes) or disabled (No)
					 for the device. |
| Span PC Port | Indicates whether the device will forward packets that are transmitted
					 and received on the network port to the access port. |
| CDP on PC Port | Indicates whether CDP is supported on the PC port (default is
					 enabled). When CDP is disabled in Cisco Unified Communications Manager ,
					 a warning is displayed, indicating that disabling CDP on the PC port prevents
					 CVTA from working. The current PC and switch port CDP values are shown in the
					 Settings application. |
| CDP on SW Port | Indicates whether CDP is supported on the switch port (default
					 is enabled). Enable CDP on the switch port for VLAN assignment for the device, power negotiation, QoS management, and 802.1x security. Enable CDP on the switch port when the device is connected to
					 a Cisco switch. When CDP is disabled in Cisco Unified Communications Manager ,
					 a warning is presented, indicating that CDP is disabled on the switch port only if
					 the device is connected to a non-Cisco switch. The current PC and switch port CDP values are shown in the
					 Settings application. |
| LLDP-MED SW Port | Indicates whether Link Layer Discovery Protocol Media Endpoint
					 Discovery (LLDP-MED) is enabled on the switch port. |
| LLDP PC Port | Indicates whether Link Layer Discovery Protocol (LLDP) is
					 enabled on the PC port. |
| LLDP Power Priority | Advertises the device power priority to the switch, enabling
					 the switch to appropriately provide power to the device. Settings include: Unknown - Default Low High Critical |
| LLDP Asset ID | Identifies the asset ID that is assigned to the device for inventory
					 management. |
| Switch Port Remote Configuration | Allows the administrator to configure the speed and function
					 of the device table port remotely by using Cisco Unified Communications Manager Administration. |
| PC Port Remote Configuration | Allows the administrator to configure the speed and function
					 of the device table port remotely by using Cisco Unified Communications Manager Administration. |

| Item | Description |
|---|---|
| Signaling Security Mode | Indicates signaling security mode. |
| LSC | Indicates whether LSC is installed on the device. |
| CAPF Server (IPv4) | Indicates CAPF server address for IPv4 |
| CAPF Server (IPv6) | Indicates CAPF server address for IPv6 |
| CAPF Port | Indicates CAPF port |
| CTL File |
| CTL Signature | Displays CTL signature |
| CUCM Server/TFTP Server | Indicates CUCM/TFTP server addresses |
| Application Server | Indicates application server |
| CAPF Server | Indicates CAPF server |
| ITL File |
| ITL Signature | Displays ITL signature |
| CAPF Server | Indicates CAPF server |
| TVS | Indicates TVS addresses |
| CUCM Server/TFTP Server | Indicates CUCM/TFTP server addresses |
| Configuration File | Indicates whether ITL configuration file is installed on the device |
| 802.1X Authentication |
| Device Authentication | Indicates whether 802.1X device authentication is enabled. |
| Transaction Status | Indicates whether 802.1X transaction status is enabled. |
| Protocol | Indicates 802.1X protocol. |
| Device ID | Displays device ID. |

| Item | Description |
|---|---|
| Tx Frames | Total number of packets transmitted by 
					 the device |
| Tx broadcast | Total number of broadcast packets transmitted by 
					 the device |
| Tx multicast | Total number of multicast packets transmitted by 
					 the device |
| Tx unicast | Total number of unicast packets transmitted by 
					 the device |
| Rx Frames | Total number of packets received by 
					 the device |
| Rx broadcast | Total number of broadcast packets received by 
					 the device |
| Rx multicast | Total number of multicast packets received by 
					 the device |
| Rx unicast | Total number of unicast packets received by 
					 the device |
| Rx PacketNoDes | Total number of shed packets caused by no Direct Memory Access
					 (DMA) descriptor |

| Item | Description |
|---|---|
| Rx totalPkt | Total number of packets received by 
					 the device |
| Rx crcErr | Total number of packets received with CRC failed |
| Rx alignErr | Total number of packets received between 64 and 1522 bytes in
					 length with a bad Frame Check Sequence (FCS) |
| Rx multicast | Total number of multicast packets received by 
					 the device |
| Rx broadcast | Total number of broadcast packets received by 
					 the device |
| Rx unicast | Total number of unicast packets received by 
					 the device |
| Rx shortErr | Total number of FCS error packets or Align error packets
					 received that are less than 64 bytes in size |
| Rx shortGood | Total number of good packets received that are less than 64
					 bytes size |
| Rx longGood | Total number of good packets received that are greater than
					 1522 bytes in size |
| Rx longErr | Total number of FCS error packets or Align error packets
					 received that are greater than 1522 bytes in size |
| Rx size64 | Total number of packets received, including bad packets, that
					 are between 0 and 64 bytes in size |
| Rx size65to127 | Total number of packets received, including bad packets, that
					 are between 65 and 127 bytes in size |
| Rx size128to255 | Total number of packets received, including bad packets, that
					 are between 128 and 255 bytes in size |
| Rx size256to511 | Total number of packets received, including bad packets, that
					 are between 256 and 511 bytes in size |
| Rx size512to1023 | Total number of packets received, including bad packets, that
					 are between 512 and 1023 bytes in size |
| Rx size1024to1518 | Total number of packets received, including bad packets, that
					 are between 1024 and 1518 bytes in size |
| Rx tokenDrop | Total number of packets dropped due to lack of resources (for
					 example, FIFO overflow) |
| Tx excessDefer | Total number of packets delayed from transmitting due to
					 medium being busy |
| Tx lateCollision | Number of times that collisions occurred later than 512 bit
					 times after the start of packet transmission |
| Tx totalGoodPkt | Total number of good packets (multicast, broadcast, and
					 unicast) received by 
					 the device |
| Tx Collisions | Total number of collisions that occurred while a packet was
					 being transmitted |
| Tx excessLength | Total number of packets not transmitted because the packet
					 experienced 16 transmission attempts |
| Tx broadcast | Total number of broadcast packets transmitted by 
					 the device |
| Tx multicast | Total number of multicast packets transmitted by 
					 the device |
| LLDP FramesOutTotal | Total number of LLDP frames sent out from 
					 the device |
| LLDP AgeoutsTotal | Total number of LLDP frames that have been timed out in cache |
| LLDP FramesDiscardedTotal | Total number of LLDP frames that are discarded when any of the
					 mandatory TLVs is missing or out of order or contains out-of-range string
					 length |
| LLDP FramesInErrorsTotal | Total number of LLDP frames received with one or more
					 detectable errors |
| LLDP FramesInTotal | Total number of LLDP frames received on 
					 the device |
| LLDP TLVDiscardedTotal | Total number of LLDP TLVs that are discarded |
| LLDP TLVUnrecognizedTotal | Total number of LLDP TLVs that are not recognized on 
					 the device |
| CDP Neighbor Device ID | Identifier of a device connected to this port discovered by
					 CDP |
| CDP Neighbor IP Address | IP address of the neighbor device discovered by CDP |
| CDP Neighbor Port | Neighbor device port to which 
					 the device is
					 connected discovered by CDP |
| LLDP Neighbor Device ID | Identifier of a device connected to this port discovered by
					 LLDP |
| LLDP Neighbor IP Address | IP address of the neighbor device discovered by LLDP |
| LLDP Neighbor Port | Neighbor device port to which 
					 the device is
					 connected discovered by LLDP |
| Port Information | Speed and duplex information |

| Item | Description |
|---|---|
| AP Name | Provides the current access point name. |
| MAC Address | Provides the MAC address of the access point. |
| Current Channel | The latest channel where this AP was observed. |
| Last RSSI | The latest RSSI in which this AP was observed. |
| Beacon Interval | Number of time units between beacons. A time unit is 1.024 ms. |
| Min Rate | Minimum data rate that the AP requires. |
| Max Rate | Maximum data rate that the AP requires. |
| WMM Supported | Support for Wi-Fi multimedia extensions. |
| UAPSD Supported | The AP supports Unscheduled Automatic Power Save Delivery. May only be available if WMM is supported. This feature is critical for talk time and for achieving maximum call density. |
| Noise | Indicates the current noise level. |
| Load | Indicates the current load. |
| Quality | Indicates voice quality. |

| Item | Description |
|---|---|
| NetDevice Stats |
| Tx bytes | Total number of bytes that the device transmits. |
| Rx Bytes | Total number of bytes that the device receives. |
| Tx Packets | Total number of packets that the device transmits. |
| Rx Packets | Total number of packets that the device receives. |
| Tx Packets Dropped | Total number of transmitted packets that the device dropped. |
| Rx Packets Dropped | Total number of received packets that the device dropped. |
| Tx Packets Error | Total number of transmitted error packets. |
| Rx Packets Error | Total number of received error packets. |
| Firmware Stats |
| Multicast Tx Frames | Total number of multicast packets that the device transmitted. |
| Failed | Transmission of packet failed. |
| Retry | Counter of total retries. |
| Multiple Retry | Transmission of packet required two or more retries before success. |
| Frame Dup | Number of duplicate packets received by the device. |
| Rts Success | A corresponding CTS was received. |
| Rts Failure | A corresponding CTS was not received. |
| Ack Failure | AP did not acknowledge a transmission. |
| Rx Frag | Number of fragmented packets that the device received. |
| Multicast Rx Frame | Number of multicast packets that the device received. |
| FCS Error | Increments when a Frame Checksum (FCS) error is detected in a received MPDU. |
| Tx Frames | Number of packets that the device sent. |
| Roaming Stats |
| current/total | Current roaming time/total roaming time in ms. |

| Item | Description |
|---|---|
| Remote Address | IP address and UDP port of the destination of the stream. |
| Local Address | IP address and UDP port of 
					 the device. |
| Start Time | Internal time stamp that indicates when Cisco Unified Communications Manager requested that 
					 the device start
					 transmitting packets. |
| Stream Status | Indication of whether streaming is active or not. |
| Host Name | Unique, fixed name that is automatically assigned to 
					 the device based on
					 its MAC address. |
| Sender Packets | Total number of RTP data packets that are transmitted by 
					 the device since
					 starting this connection. The value is 0 if the connection is set to Receive
					 Only. |
| Sender Octets | Total number of payload octets that are transmitted in RTP data packets
					 by 
					 the device since
					 starting this connection. The value is 0 if the connection is set to Receive
					 Only. |
| Sender Codec | Type of audio encoding that is used for the transmitted stream. |
| Sender Reports Sent (see note) | Number of times that  the RTCP Sender Report has been sent. |
| Sender Report Time Sent 
					 (see note) | Internal time stamp indication when the last RTCP Sender
					 Report was sent. |
| Receiver Lost Packets | Total number of RTP data packets that have been lost since
					 starting receiving data on this connection. Defined as the number of expected
					 packets less the number of packets received, where the number of received
					 packets includes any that are late or duplicate. The value displays as 0 if the
					 connection was set to Send Only. |
| Avg Jitter | Estimate of mean deviation of the RTP data packet
					 inter-arrival time, measured in milliseconds. The value displays as 0 if the
					 connection was set to Send Only. |
| Receiver Codec | Type of audio encoding that is used for the received stream. |
| Receiver Reports Sent 
					 (see note) | Number of times the RTCP Receiver Reports have been sent. |
| Receiver Report Time Sent 
					 (see note) | Internal time stamp indication when a RTCP Receiver Report was
					 sent. |
| Receiver Packets | Total number of RTP data packets received by 
					 the device since
					 starting receiving data on this connection. Includes packets received from
					 different sources if this is a multicast call. The value displays as 0 if the
					 connection was set to Send Only. |
| Receiver Octets | Total number of payload octets received in RTP data packets by
					 the device since starting reception on the connection. Includes packets
					 received from different sources if this is a multicast call. The value displays
					 as 0 if the connection was set to Send Only. |
| Cumulative Conceal Ratio | Total number of concealment frames divided by total number of
					 speech frames received from start of the voice stream. |
| Interval Conceal Ratio | Ratio of concealment frames to speech frames in preceding
					 3-second interval of active speech. If  voice activity detection (VAD) is in use, a
					 longer interval might be required to accumulate 3 seconds of active speech. |
| Max Conceal Ratio | Highest interval concealment ratio from start of the voice
					 stream. |
| Conceal Secs | Number of seconds that have concealment events (lost frames)
					 from the start of the voice stream (includes severely concealed seconds). |
| Severely Conceal Secs | Number of seconds that have more than five percent concealment
					 events (lost frames) from the start of the voice stream. |
| Latency 
					 (see note) | Estimate of the network latency, expressed in milliseconds.
					 Represents a running average of the round-trip delay, measured when RTCP
					 receiver report blocks are received. |
| Max Jitter | Maximum value of instantaneous jitter, in milliseconds. |
| Sender Size | RTP packet size, in milliseconds, for the transmitted stream. |
| Sender Reports Received 
					 (see note) | Number of times RTCP Sender Reports have been received. |
| Sender Report Time Received 
					 (see note) | Last time at which an RTCP Sender Report was received. |
| Receiver Size | RTP packet size, in milliseconds, for the received stream. |
| Receiver Discarded | RTP packets received from network but discarded from jitter
					 buffers. |
| Receiver Reports Received 
					 (see note) | Number of times RTCP Receiver Reports have been received. |
| Receiver Report Time Received 
					 (see note) | Last time at which an RTCP Receiver Report was received. |
| Receiver Encrypted | Indicates if the receiver stream is encrypted. |
| Sender Encrypted | Indicates if the sender stream is encrypted. |
| Sender Frames | Number of video frames that by the device transmitted since the video stream opened. |
| Sender Partial Frames | Number of P-frames that the device sent since the video stream opened. |
| Sender IFrames | Number of I-frames that the device sent since the video stream opened. |
| Sender Frame Rate | Rate at which video frames are transmitted (in frames per second). |
| Sender Bandwidth | Bandwidth of the transmitted video steam in kbps (kilo bits per second). |
| Sender Resolution | Resolution of the video stream that the device transmits. |
| Receiver Frames | Number of video frames that the device received since the video stream opened. |
| Receiver Partial Frames | Number of P-frames that the device received since the video stream opened. |
| Receiver IFrames | Number of I-frames that the device received since the video stream opened. |
| Receiver IFrames Req | Number of IDR requests that the device sent to the remote endpoint since the video stream opened. |
| Receiver Frame Rate | Rate at which video frames are received (in frames per second). |
| Receiver Frames Lost | Number of frames lost that the video decoder reported since the video stream opened. |
| Receiver Frames Errors | Number of errors that the video decoder reported since the video stream opened. |
| Receiver Bandwidth | Bandwidth of the received video steam in kbps (kilo bits per second). |
| Receiver Resolution | Resolution of the video stream that the phone received from the remote endpoint. |
| Domain Name | Indicates the domain name. |
| Sender Joins | Number of times the device has started transmitting a stream |
| Receiver Joins | Number of times the device has started receiving a stream |
| Byes | Number of times the device has stopped transmitting a stream |
| Sender Start Time | Time stamp that indicates when the first RTP packet is sent to the network. |
| Receiver Start Time | Time stamp that indicates when the first RTP packet is received from the network. |
| Sender DSCP | DSCP value for sender SIP signaling packets |
| Receiver DSCP | DSCP value for receiver SIP signaling packets |
| Sender RTCP DSCP | DSCP value for sender RTP packets |
| Receiver RTCP DSCP | DSCP value for sender RTP packets |
| Is Video | Indicates a video call. |
| Is Presentation | Indicates a presentation call. |
| Sender Active | Indicates the sender is active. |
| Receiver Active | Indicates the receiver is active. |

| Note | When the RTP Control
						Protocol is disabled, no data is generated for this field and therefore it
						displays as 0. |
|---|---|