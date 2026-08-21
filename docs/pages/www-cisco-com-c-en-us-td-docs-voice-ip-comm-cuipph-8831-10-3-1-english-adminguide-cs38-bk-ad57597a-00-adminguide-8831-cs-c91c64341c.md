---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8831-10-3-1-english-adminguide-cs38-bk-ad57597a-00-adminguide-8831-cs-c91c64341c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8831/10_3_1/english/AdminGuide/CS38_BK_AD57597A_00_adminguide-8831/CS38_BK_AD57597A_00_adminguide-8831_chapter_01000.html
retrieved_at: 2026-08-21T13:38:18.308007+00:00
---

Cisco Unified IP Conference Phone 8831 and 8831NR Administration Guide

# Cisco Unified IP Conference Phone 8831 and 8831NR Administration Guide

Updated: November 17, 2014

Chapter: Remote
	 Monitoring

## Chapter: Remote
	 Monitoring

# Remote
                     	 Monitoring

## Remote Monitoring
                        	 Overview

Each Cisco Unified IP Conference Phone has a web page from which
                           		you can view a variety of information about the conference phone, including:

Device information

Network configuration information

Ethernet information

Device logs

Streaming statistics

This chapter describes the information that you can obtain from the
                           		conference phone web page. You can use this information to remotely monitor the
                           		operation of a conference phone and to assist with troubleshooting.

You can also obtain much of this information directly from a conference
                           		phone. For more information, see Model Information, Status, and Statistics .

For more information about troubleshooting the conference phone, see Troubleshooting and Maintenance .

## Access Web
                        	 Page

If you cannot
                                          			 access the web page, it may be disabled. See the Control Web Page Access section for more information.

Obtain the IP
                                       			 address of the conference phone using one of these methods:

From Cisco
                                                					 Unified Communications Manager Administration, choose Device > Phone . Enter search criteria to locate
                                                					 the conference phone, and then click the conference phone name. Conference
                                                					 phones registered with Cisco Unified Communications Manager display the IP
                                                					 address at the top of the Phone Configuration web page.

On the
                                                					 conference phone, choose Apps > Settings > Network
                                                      						  Configuration . Then, scroll to the IP Address option.

Open a web
                                       			 browser and enter the following URL, where IP address is the IP address of the
                                       			 conference phone: http:// <IP_address>

### Web Page
                           	 Information

The web page for a
                              		conference phone includes these hyperlinks:

Device Information :
                                    			 Displays device settings and related information for the conference phone.

Network Configuration :
                                    			 Displays network configuration information and information about other
                                    			 conference phone settings.

Ethernet Information :
                                    			 Displays network statistics.

Device Logging :
                                    			 Displays messages that might be useful to Cisco TAC if you require assistance
                                    			 with troubleshooting.

Streaming Statistics :
                                    			 Displays call statistics.

## Control Web Page
                        	 Access

For security purposes,
                              		  you may choose to prevent access to the web pages for a conference phone. If
                              		  you do so, you will prevent access to the web pages that are described in this
                              		  chapter and to the Cisco Unified Communications Manager Self Care Portal.

To enable or
                              		  disable access to the web pages for a conference phone, follow these steps from
                              		  Cisco Unified Communications Manager Administration:

Choose Device >
                                          				Phone .

Specify the
                                       			 criteria to find the phone and click Find , or click Find to
                                       			 display a list of all phones.

Click the
                                       			 device name to open the Phone Configuration web page for the device.

In the Product
                                       			 Specific Configuration Layout area, from the Web Access drop-down list, choose Enabled or
                                          				Disabled .

Click Update .

Some
                                                         					 features, such as Cisco Quality Report Tool, do not function properly without
                                                         					 access to the conference phone web pages. Disabling web access also affects any
                                                         					 serviceability application that relies on web access, such as CiscoWorks.

## Device Information
                        	 Area

The Device
                           		Information area on a conference phone web page displays device settings and
                           		related information for the conference phone. The following table describes
                           		these items.

To display the
                           		Device Information area, access the web page for the conference phone as
                           		described in the Access Web Page section, and then click the Device
                              		  Information hyperlink.

Item

MAC Address

Media Access
                                       				Control (MAC) address of the conference phone.

Host Name

Unique, fixed
                                       				name that is automatically assigned to the conference phone based on its MAC
                                       				address.

DN

Directory
                                       				number assigned to the conference phone.

Version

Version of the
                                       				firmware running on the conference phone.

Hardware
                                       				Revision

Revision value
                                       				of the conference phone hardware.

Serial Number

Serial number
                                       				of the conference phone.

Model Number

Model number
                                       				of the conference phone.

Message
                                       				Waiting

Indicates if
                                       				there is a voice message waiting for this conference phone.

UDI

Device
                                                					 Type: Indicates hardware type. For example, phone displays for all phone models

Device
                                                					 Description: Displays the name of the conference phone associated with the
                                                					 indicated model type

Product
                                                					 Identifier: Specifies the conference phone model

Serial
                                                					 Number: Displays the conference phone unique serial number

Time

Time obtained
                                       				from the Date/Time Group in Cisco Unified Communications Manager to which the
                                       				conference phone belongs.

Time Zone

Time zone
                                       				obtained from the Date/Time Group in Cisco Unified Communications Manager to
                                       				which the conference phone belongs.

Date

Date obtained
                                       				from the Date/Time Group in Cisco Unified Communications Manager to which the
                                       				conference phone belongs.

## Network
                        	 Configuration Area

The Network
                           		Configuration area on a conference phone web page displays network
                           		configuration information and information about other conference phone
                           		settings. The following table describes this information.

You can view and set
                           		many of these items from the Network Configuration Menu and the Device
                           		Configuration Menu on the conference phone.

To display the
                           		Network Configuration area, access the web page for the conference phone as
                           		described in the Access Web Page section, and then click the Network
                              		  Configuration hyperlink.

Item

Description

DHCP
                                       					 Enabled

Indicates
                                       					 whether DHCP is being used by the conference phone.

MAC
                                       					 Address

MAC
                                       					 address of the conference phone.

Host Name

Host name
                                       					 that the DHCP server assigned to the conference phone.

IP Address

IP address
                                       					 of the conference phone.

Subnet
                                       					 Mask

IP address
                                       					 of the subnet mask used by the conference phone.

Default
                                       					 Router 1

Default
                                       					 router used by the conference phone (Default Router 1).

Domain
                                       					 Name

Name of
                                       					 the Domain Name System (DNS) domain in which the conference phone resides.

DNS Server
                                       					 1–5

Primary
                                       					 Domain Name System (DNS) server (DNS Server 1) and optional backup DNS servers
                                       					 (DNS Server 2–5) used by the conference phone.

Operational VLAN ID

Auxiliary
                                       					 Virtual Local Area Network (VLAN) configured on a Cisco Catalyst switch in
                                       					 which the conference phone is a member.

Admin.
                                       					 VLAN ID

Auxiliary
                                       					 VLAN in which the conference phone is a member.

TFTP
                                       					 Server 1

Primary
                                       					 Trivial File Transfer Protocol (TFTP) server used by the conference phone.

TFTP
                                       					 Server 2

Optional
                                       					 backup TFTP server that the conference phone uses if the primary TFTP server is
                                       					 unavailable.

Alternate
                                       					 TFTP

Indicates
                                       					 whether the conference phone is using an alternate TFTP server.

Ethernet
                                       					 Configuration

Speed and
                                       					 duplex of the Ethernet port (labeled LAN on the conference phone).

CallManager 1–5

Host names
                                       					 or IP addresses, in prioritized order, of the Cisco Unified Communications
                                       					 Manager servers with which the conference phone can register. An item can also
                                       					 show the IP address of a Survivable Remote Site Telephony (SRST) router that is
                                       					 capable of providing limited Cisco Unified Communications Manager
                                       					 functionality, if such a router is available.

Active: Cisco Unified Communications Manager server from which
                                                						  the conference phone is currently receiving call-processing services.

Standby: Cisco Unified Communications Manager server to which
                                                						  the conference phone switches if the current server becomes unavailable.

Blank:
                                                						  No current connection to this Cisco Unified Communications Manager.

An option
                                       					 may also include the SRST designation, which indicates an SRST router capable
                                       					 of providing Cisco Unified Communications Manager functionality with a limited
                                       					 feature set. This router assumes control of call processing if all other Cisco
                                       					 Unified Communications Manager servers become unreachable. The SRST Cisco
                                       					 Unified Communications Manager always appears last in the list of servers, even
                                       					 if it is active. You configure the SRST router address in the Device Pool
                                       					 section in Cisco Unified Communications Manager.

Information URL

URL of the
                                       					 help text that appears on the conference phone.

Services
                                       					 URL

URL of the
                                       					 server from which the conference phone obtains conference phone services.

Directories URL

URL of the
                                       					 server from which the conference phone obtains directory information.

Messages
                                       					 URL

URL of the
                                       					 server from which the conference phone obtains message services.

Authentication URL

URL that
                                       					 the conference phone uses to validate requests made to the conference phone web
                                       					 server.

Proxy
                                       					 Server URL

URL of
                                       					 proxy server, which makes HTTP requests to non-local host addresses on behalf
                                       					 of the conference phone HTTP client and provides responses from the non-local
                                       					 host to the conference phone HTTP client.

Idle URL

URL that
                                       					 the conference phone displays when the conference phone has not been used for
                                       					 the time specified by Idle URL Time and no menu is open.

Idle URL
                                       					 Time

Number of
                                       					 seconds that the conference phone has not been used and no menu is open before
                                       					 the XML service specified by Idle URL is activated.

User
                                       					 Locale

User
                                       					 locale associated with the conference phone user. Identifies a set of detailed
                                       					 information to support users, including language, font, date and time
                                       					 formatting, and alphanumeric keyboard text information.

User
                                       					 Locale Version

Version
                                       					 of the user locale loaded on the conference phone.

User
                                       					 Locale Char Set

Version
                                       					 of the character set that the conference phone uses for the user locale.

Network
                                       					 Locale

Network
                                       					 locale associated with the conference phone user. Identifies a set of detailed
                                       					 information to support the conference phone in a specific location, including
                                       					 definitions of the tones and cadences used by the conference phone.

Network
                                       					 Locale Version

Version
                                       					 of the network locale loaded on the conference phone.

DSCP For
                                       					 Call Control

DSCP IP
                                       					 classification for call control signaling.

DSCP For
                                       					 Configuration

DSCP IP
                                       					 classification for any conference phone configuration transfer.

DSCP For
                                       					 Services

DSCP IP
                                       					 classification for conference phone-based services.

Web
                                       					 Access Enabled

Indicates whether web access is enabled (Yes) or disabled (No)
                                       					 for the conference phone.

## Ethernet
                        	 Information Area

Ethernet traffic

Network traffic
                                    			 to and from the PC port on the conference phone

Network traffic
                                    			 to and from the network port on the conference phone

To display the
                           		Ethernet Information area, access the web page for the conference phone as
                           		described in the Access Web Page section, and then click the Ethernet
                              		  Information hyperlink.

The following table
                           		describes the information in the Ethernet Information area.

Item

Description

Rx error

Total number
                                       				of FCS error packets or Align error packets received.

Rx PacketNoDes

Total number
                                       				of shed packets caused by no DMA descriptor.

Rx Overruns

Total number
                                       				of received packets dropped because of buffer overruns.

Rx alignErr

Total number
                                       				of packets received between 64 and 1522 bytes in length that have bad FCS
                                       				errors.

Rx length
                                       				error

Number of
                                       				packets discarded due to improper length.

Rx symbol
                                       				error

Number of
                                       				valid length packets received that have at least one invalid data symbol.

Rx CRC Errors

Total number
                                       				of packets received with CRC failed.

Rx Broadcasts

Number of
                                       				broadcast packets received by the conference phone.

Rx Multicasts

Total number
                                       				of multicast packets received by the conference phone.

Rx fail filter

Total number
                                       				of packets received by the conference phone that failed.

Rx VLAN

Total number
                                       				of packets received on the Virtual Local Area Network.

Rx control
                                       				frames

Total number
                                       				of control frames received.

Rx unicast

Total number
                                       				of unicast packets received by the conference phone.

Tx error

Total number
                                       				of FCS error packets or Align error packets transmitted by the conference
                                       				phone.

Tx no
                                       				descriptor

Total number
                                       				of transmit packets dropped because no descriptor was specified.

Tx
                                       				fifoUnderrun

Total number
                                       				of transmit packets dropped because of fifo underrun.

Tx
                                       				lateCollision

Number of
                                       				times that collisions occurred later than 512 bit times after the start of
                                       				packet transmission.

Tx Excessive
                                       				Collisions

Total number
                                       				of packets that could not be sent because of network congestion.

Tx excessDefer

Total number
                                       				of packets delayed from transmitting due to medium being busy.

Tx Deferred
                                       				Abort

Total number
                                       				of transmit packets aborted.

Tx Collisions

Total number
                                       				of collisions that occurred while a packet was being transmitted.

Event send
                                       				failed

Total number
                                       				of packets that failed to transmit.

Event Rx
                                       				packet send failed

Total number
                                       				of packets that were not received.

Tx
                                       				excessLength

Total number
                                       				of packets not transmitted because the packet experienced 16 transmission
                                       				attempts.

Rx totalPkt

Total number
                                       				of packets received by the conference phone.

Packet
                                       				Transmitted

Total number
                                       				of packets transmitted by the conference phone.

Rcvr Octets

Total number
                                       				of octets received by the conference phone.

Sender Octets

Total number
                                       				of octets sent by the conference phone.

## Device Logs
                        	 Area

The Device Logs area
                           		on a conference phone web page provides information you can use to help monitor
                           		and troubleshoot the conference phone. It includes debug and error messages
                           		received on the conference phone that might be useful to Cisco TAC if you
                           		require assistance with troubleshooting.

To display device
                           		logs, access the web page for the conference phone as described in the Access Web Page section, and then click the Device
                              		  Logging hyperlink. In the File Download dialog box, click Open to view the device logs, or click Save to save the logs to a specific location.

## Streaming
                        	 Statistics Area

A conference phone
                           		can stream information to and from up to three devices simultaneously. A
                           		conference phone streams information when it is on a call or running a service
                           		that sends or receives audio or data.

The Streaming
                           		Statistics area on a conference phone web page provides information about the
                           		streams. Most calls use only one stream (Stream 1), but some calls use two or
                           		three streams. For example, a barged call uses Stream 1 and Stream 2.

To display the
                           		Streaming Statistics area, access the web page for the conference phone as
                           		described in the Access Web Page section, and then click the Streaming
                              		  Statistics hyperlink.

The following table
                           		describes the items in the Streaming Statistics areas.

Item

Description

Remote Address

IP address and
                                       				UDP port of the stream.

Local Address

IP address and
                                       				UDP port of the conference phone.

Start Time

Internal time
                                       				stamp indicating when Cisco Unified Communications Manager requested that the
                                       				conference phone start transmitting packets.

Codec Type

Type of voice
                                       				stream received or transmitted (RTP streaming audio): G.729, G.711 u-law, G.711
                                       				A-law, G.722, or Lin16k.

Payload Size

Size of voice
                                       				packets, in milliseconds, in the receiving or transmitting voice stream (RTP
                                       				streaming audio).

Rcvr Packets

Number of RTP
                                       				voice packets received since voice stream was opened.

This number
                                                   				  is not necessarily identical to the number of RTP voice packets received since
                                                   				  the call began because the call might have been placed on hold.

Rcvr Lost
                                       				Packets

Missing RTP
                                       				packets (lost in transit).

Rcvr Octets

Number of
                                       				bytes of voice packets received since voice stream was opened.

Rx Expected
                                       				Pkts

The expected
                                       				number of packets received for the local conference phone.

Last Rx Seq No

The sequence
                                       				number of the last RTP packet received.

Most recent Rx
                                       				SSRC

The
                                       				Synchronization Source field of the last RTP packet received.

Avg Jitter

Estimated
                                       				average RTP packet jitter (dynamic delay that a packet encounters when going
                                       				through the network) observed since the receiving voice stream was opened.

Max Jitter

Maximum jitter
                                       				observed since the receiving voice stream was opened.

Sender Packets

Number of RTP
                                       				voice packets transmitted since voice stream was opened.

This number
                                                   				  is not necessarily identical to the number of RTP voice packets transmitted
                                                   				  since the call began because the call might have been placed on hold.

Sender Octets

Number of
                                       				bytes of voice packets transmitted since voice stream was opened.

| Note | If you cannot
                                          			 access the web page, it may be disabled. See the Control Web Page Access section for more information. |
|---|---|

| Step 1 | Obtain the IP
                                       			 address of the conference phone using one of these methods: From Cisco
                                                					 Unified Communications Manager Administration, choose Device > Phone . Enter search criteria to locate
                                                					 the conference phone, and then click the conference phone name. Conference
                                                					 phones registered with Cisco Unified Communications Manager display the IP
                                                					 address at the top of the Phone Configuration web page. On the
                                                					 conference phone, choose Apps > Settings > Network
                                                      						  Configuration . Then, scroll to the IP Address option. |
|---|---|
| Step 2 | Open a web
                                       			 browser and enter the following URL, where IP address is the IP address of the
                                       			 conference phone: http:// <IP_address> |

| Step 1 | Choose Device >
                                          				Phone . |
|---|---|
| Step 2 | Specify the
                                       			 criteria to find the phone and click Find , or click Find to
                                       			 display a list of all phones. |
| Step 3 | Click the
                                       			 device name to open the Phone Configuration web page for the device. |
| Step 4 | In the Product
                                       			 Specific Configuration Layout area, from the Web Access drop-down list, choose Enabled or
                                          				Disabled . |
| Step 5 | Click Update . Note Some
                                                         					 features, such as Cisco Quality Report Tool, do not function properly without
                                                         					 access to the conference phone web pages. Disabling web access also affects any
                                                         					 serviceability application that relies on web access, such as CiscoWorks. | Note | Some
                                                         					 features, such as Cisco Quality Report Tool, do not function properly without
                                                         					 access to the conference phone web pages. Disabling web access also affects any
                                                         					 serviceability application that relies on web access, such as CiscoWorks. |
| Note | Some
                                                         					 features, such as Cisco Quality Report Tool, do not function properly without
                                                         					 access to the conference phone web pages. Disabling web access also affects any
                                                         					 serviceability application that relies on web access, such as CiscoWorks. |

| Note | Some
                                                         					 features, such as Cisco Quality Report Tool, do not function properly without
                                                         					 access to the conference phone web pages. Disabling web access also affects any
                                                         					 serviceability application that relies on web access, such as CiscoWorks. |
|---|---|

| Item |  |
|---|---|
| MAC Address | Media Access
                                       				Control (MAC) address of the conference phone. |
| Host Name | Unique, fixed
                                       				name that is automatically assigned to the conference phone based on its MAC
                                       				address. |
| DN | Directory
                                       				number assigned to the conference phone. |
| Version | Version of the
                                       				firmware running on the conference phone. |
| Hardware
                                       				Revision | Revision value
                                       				of the conference phone hardware. |
| Serial Number | Serial number
                                       				of the conference phone. |
| Model Number | Model number
                                       				of the conference phone. |
| Message
                                       				Waiting | Indicates if
                                       				there is a voice message waiting for this conference phone. |
| UDI | Displays the
                                       				following Cisco Unique Device Identifier (UDI) information about the conference
                                       				phone: Device
                                                					 Type: Indicates hardware type. For example, phone displays for all phone models Device
                                                					 Description: Displays the name of the conference phone associated with the
                                                					 indicated model type Product
                                                					 Identifier: Specifies the conference phone model Serial
                                                					 Number: Displays the conference phone unique serial number |
| Time | Time obtained
                                       				from the Date/Time Group in Cisco Unified Communications Manager to which the
                                       				conference phone belongs. |
| Time Zone | Time zone
                                       				obtained from the Date/Time Group in Cisco Unified Communications Manager to
                                       				which the conference phone belongs. |
| Date | Date obtained
                                       				from the Date/Time Group in Cisco Unified Communications Manager to which the
                                       				conference phone belongs. |

| Item | Description |
|---|---|
| DHCP
                                       					 Enabled | Indicates
                                       					 whether DHCP is being used by the conference phone. |
| MAC
                                       					 Address | MAC
                                       					 address of the conference phone. |
| Host Name | Host name
                                       					 that the DHCP server assigned to the conference phone. |
| IP Address | IP address
                                       					 of the conference phone. |
| Subnet
                                       					 Mask | IP address
                                       					 of the subnet mask used by the conference phone. |
| Default
                                       					 Router 1 | Default
                                       					 router used by the conference phone (Default Router 1). |
| Domain
                                       					 Name | Name of
                                       					 the Domain Name System (DNS) domain in which the conference phone resides. |
| DNS Server
                                       					 1–5 | Primary
                                       					 Domain Name System (DNS) server (DNS Server 1) and optional backup DNS servers
                                       					 (DNS Server 2–5) used by the conference phone. |
| Operational VLAN ID | Auxiliary
                                       					 Virtual Local Area Network (VLAN) configured on a Cisco Catalyst switch in
                                       					 which the conference phone is a member. |
| Admin.
                                       					 VLAN ID | Auxiliary
                                       					 VLAN in which the conference phone is a member. |
| TFTP
                                       					 Server 1 | Primary
                                       					 Trivial File Transfer Protocol (TFTP) server used by the conference phone. |
| TFTP
                                       					 Server 2 | Optional
                                       					 backup TFTP server that the conference phone uses if the primary TFTP server is
                                       					 unavailable. |
| Alternate
                                       					 TFTP | Indicates
                                       					 whether the conference phone is using an alternate TFTP server. |
| Ethernet
                                       					 Configuration | Speed and
                                       					 duplex of the Ethernet port (labeled LAN on the conference phone). |
| CallManager 1–5 | Host names
                                       					 or IP addresses, in prioritized order, of the Cisco Unified Communications
                                       					 Manager servers with which the conference phone can register. An item can also
                                       					 show the IP address of a Survivable Remote Site Telephony (SRST) router that is
                                       					 capable of providing limited Cisco Unified Communications Manager
                                       					 functionality, if such a router is available. For an
                                       					 available server, an item will show the Cisco Unified Communications Manager
                                       					 server IP address and one of the following states: Active: Cisco Unified Communications Manager server from which
                                                						  the conference phone is currently receiving call-processing services. Standby: Cisco Unified Communications Manager server to which
                                                						  the conference phone switches if the current server becomes unavailable. Blank:
                                                						  No current connection to this Cisco Unified Communications Manager. An option
                                       					 may also include the SRST designation, which indicates an SRST router capable
                                       					 of providing Cisco Unified Communications Manager functionality with a limited
                                       					 feature set. This router assumes control of call processing if all other Cisco
                                       					 Unified Communications Manager servers become unreachable. The SRST Cisco
                                       					 Unified Communications Manager always appears last in the list of servers, even
                                       					 if it is active. You configure the SRST router address in the Device Pool
                                       					 section in Cisco Unified Communications Manager. |
| Information URL | URL of the
                                       					 help text that appears on the conference phone. |
| Services
                                       					 URL | URL of the
                                       					 server from which the conference phone obtains conference phone services. |
| Directories URL | URL of the
                                       					 server from which the conference phone obtains directory information. |
| Messages
                                       					 URL | URL of the
                                       					 server from which the conference phone obtains message services. |
| Authentication URL | URL that
                                       					 the conference phone uses to validate requests made to the conference phone web
                                       					 server. |
| Proxy
                                       					 Server URL | URL of
                                       					 proxy server, which makes HTTP requests to non-local host addresses on behalf
                                       					 of the conference phone HTTP client and provides responses from the non-local
                                       					 host to the conference phone HTTP client. |
| Idle URL | URL that
                                       					 the conference phone displays when the conference phone has not been used for
                                       					 the time specified by Idle URL Time and no menu is open. |
| Idle URL
                                       					 Time | Number of
                                       					 seconds that the conference phone has not been used and no menu is open before
                                       					 the XML service specified by Idle URL is activated. |
| User
                                       					 Locale | User
                                       					 locale associated with the conference phone user. Identifies a set of detailed
                                       					 information to support users, including language, font, date and time
                                       					 formatting, and alphanumeric keyboard text information. |
| User
                                       					 Locale Version | Version
                                       					 of the user locale loaded on the conference phone. |
| User
                                       					 Locale Char Set | Version
                                       					 of the character set that the conference phone uses for the user locale. |
| Network
                                       					 Locale | Network
                                       					 locale associated with the conference phone user. Identifies a set of detailed
                                       					 information to support the conference phone in a specific location, including
                                       					 definitions of the tones and cadences used by the conference phone. |
| Network
                                       					 Locale Version | Version
                                       					 of the network locale loaded on the conference phone. |
| DSCP For
                                       					 Call Control | DSCP IP
                                       					 classification for call control signaling. |
| DSCP For
                                       					 Configuration | DSCP IP
                                       					 classification for any conference phone configuration transfer. |
| DSCP For
                                       					 Services | DSCP IP
                                       					 classification for conference phone-based services. |
| Web
                                       					 Access Enabled | Indicates whether web access is enabled (Yes) or disabled (No)
                                       					 for the conference phone. |

| Item | Description |
|---|---|
| Rx error | Total number
                                       				of FCS error packets or Align error packets received. |
| Rx PacketNoDes | Total number
                                       				of shed packets caused by no DMA descriptor. |
| Rx Overruns | Total number
                                       				of received packets dropped because of buffer overruns. |
| Rx alignErr | Total number
                                       				of packets received between 64 and 1522 bytes in length that have bad FCS
                                       				errors. |
| Rx length
                                       				error | Number of
                                       				packets discarded due to improper length. |
| Rx symbol
                                       				error | Number of
                                       				valid length packets received that have at least one invalid data symbol. |
| Rx CRC Errors | Total number
                                       				of packets received with CRC failed. |
| Rx Broadcasts | Number of
                                       				broadcast packets received by the conference phone. |
| Rx Multicasts | Total number
                                       				of multicast packets received by the conference phone. |
| Rx fail filter | Total number
                                       				of packets received by the conference phone that failed. |
| Rx VLAN | Total number
                                       				of packets received on the Virtual Local Area Network. |
| Rx control
                                       				frames | Total number
                                       				of control frames received. |
| Rx unicast | Total number
                                       				of unicast packets received by the conference phone. |
| Tx error | Total number
                                       				of FCS error packets or Align error packets transmitted by the conference
                                       				phone. |
| Tx no
                                       				descriptor | Total number
                                       				of transmit packets dropped because no descriptor was specified. |
| Tx
                                       				fifoUnderrun | Total number
                                       				of transmit packets dropped because of fifo underrun. |
| Tx
                                       				lateCollision | Number of
                                       				times that collisions occurred later than 512 bit times after the start of
                                       				packet transmission. |
| Tx Excessive
                                       				Collisions | Total number
                                       				of packets that could not be sent because of network congestion. |
| Tx excessDefer | Total number
                                       				of packets delayed from transmitting due to medium being busy. |
| Tx Deferred
                                       				Abort | Total number
                                       				of transmit packets aborted. |
| Tx Collisions | Total number
                                       				of collisions that occurred while a packet was being transmitted. |
| Event send
                                       				failed | Total number
                                       				of packets that failed to transmit. |
| Event Rx
                                       				packet send failed | Total number
                                       				of packets that were not received. |
| Tx
                                       				excessLength | Total number
                                       				of packets not transmitted because the packet experienced 16 transmission
                                       				attempts. |
| Rx totalPkt | Total number
                                       				of packets received by the conference phone. |
| Packet
                                       				Transmitted | Total number
                                       				of packets transmitted by the conference phone. |
| Rcvr Octets | Total number
                                       				of octets received by the conference phone. |
| Sender Octets | Total number
                                       				of octets sent by the conference phone. |

| Item | Description |
|---|---|
| Remote Address | IP address and
                                       				UDP port of the stream. |
| Local Address | IP address and
                                       				UDP port of the conference phone. |
| Start Time | Internal time
                                       				stamp indicating when Cisco Unified Communications Manager requested that the
                                       				conference phone start transmitting packets. |
| Codec Type | Type of voice
                                       				stream received or transmitted (RTP streaming audio): G.729, G.711 u-law, G.711
                                       				A-law, G.722, or Lin16k. |
| Payload Size | Size of voice
                                       				packets, in milliseconds, in the receiving or transmitting voice stream (RTP
                                       				streaming audio). |
| Rcvr Packets | Number of RTP
                                       				voice packets received since voice stream was opened. Note This number
                                                   				  is not necessarily identical to the number of RTP voice packets received since
                                                   				  the call began because the call might have been placed on hold. | Note | This number
                                                   				  is not necessarily identical to the number of RTP voice packets received since
                                                   				  the call began because the call might have been placed on hold. |
| Note | This number
                                                   				  is not necessarily identical to the number of RTP voice packets received since
                                                   				  the call began because the call might have been placed on hold. |
| Rcvr Lost
                                       				Packets | Missing RTP
                                       				packets (lost in transit). |
| Rcvr Octets | Number of
                                       				bytes of voice packets received since voice stream was opened. |
| Rx Expected
                                       				Pkts | The expected
                                       				number of packets received for the local conference phone. |
| Last Rx Seq No | The sequence
                                       				number of the last RTP packet received. |
| Most recent Rx
                                       				SSRC | The
                                       				Synchronization Source field of the last RTP packet received. |
| Avg Jitter | Estimated
                                       				average RTP packet jitter (dynamic delay that a packet encounters when going
                                       				through the network) observed since the receiving voice stream was opened. |
| Max Jitter | Maximum jitter
                                       				observed since the receiving voice stream was opened. |
| Sender Packets | Number of RTP
                                       				voice packets transmitted since voice stream was opened. Note This number
                                                   				  is not necessarily identical to the number of RTP voice packets transmitted
                                                   				  since the call began because the call might have been placed on hold. | Note | This number
                                                   				  is not necessarily identical to the number of RTP voice packets transmitted
                                                   				  since the call began because the call might have been placed on hold. |
| Note | This number
                                                   				  is not necessarily identical to the number of RTP voice packets transmitted
                                                   				  since the call began because the call might have been placed on hold. |
| Sender Octets | Number of
                                       				bytes of voice packets transmitted since voice stream was opened. |

| Note | This number
                                                   				  is not necessarily identical to the number of RTP voice packets received since
                                                   				  the call began because the call might have been placed on hold. |
|---|---|

| Note | This number
                                                   				  is not necessarily identical to the number of RTP voice packets transmitted
                                                   				  since the call began because the call might have been placed on hold. |
|---|---|