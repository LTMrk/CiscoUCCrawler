---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-3905-10-0-english-admin-guide-ip05-bk-a6e3f5ab-00-adminguide-3905-10--7179a7e663
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/3905/10_0/english/admin_guide/IP05_BK_A6E3F5AB_00_adminguide-3905-10_0/IP05_BK_A6E3F5AB_00_adminguide-3905-10_0_chapter_01001.html
retrieved_at: 2026-08-21T14:35:25.844524+00:00
---

Cisco Unified SIP Phone 3905 Administration Guide for Cisco Unified Communications Manager 10.0

# Cisco Unified SIP Phone 3905 Administration Guide for Cisco Unified Communications Manager 10.0

Updated: May 9, 2025

Chapter: Monitoring Phone Systems

## Chapter: Monitoring Phone Systems

# Monitoring Phone Systems

## Cisco Unified SIP Phone status

This section describes how to use the following menus on the
                              		Cisco Unified SIP Phone 3905 to view model information, status messages, and
                              		network statistics for the phone:

Model Information screen: Displays hardware and software
                                    			 information about the phone.

Status menu: Provides access to screens that display the status
                                    			 messages, network statistics, and statistics for the current call.

You can use the information on these screens to monitor the
                              		operation of a phone and to assist with troubleshooting.

You can also obtain much of this information, and obtain other
                              		related information, remotely through the phone web page.

For more information about troubleshooting the 
                              		Cisco Unified SIP Phone 3905, see Troubleshooting

### Display Model Information Window

To display the Model Information screen, follow these steps.

Step 1

Press Applications .

Step 2

Select Phone Information .

If the user is connected to a secure or authenticated server, a
                                             				corresponding icon (lock or certificate) displays in the Phone Information
                                             				Screen to the right of the server option. If the user is not connected to a
                                             				secure or authenticated server, no icon appears.

Step 3

To exit the Model Information screen, press Back .

#### Model Information Fields

Option

Description

To Change

Model Number

Model number of the phone.

Display only - cannot configure.

MAC Address

MAC address of the phone.

Display only - cannot configure.

Active Load ID

Version of firmware currently installed on the phone.

Display only - cannot configure.

Boot Load ID

Identifier of the factory-installed load running on the phone.

Display only - cannot configure.

IP Address

IP address of the phone.

Display only - cannot configure.

Active Server

IP address or name of the server to which the phone is
                                             					 registered.

Display only - cannot configure.

Stand-by Server

IP address or name of the standby server.

Display only - cannot configure.

### Display Status Menu

The Status menu includes theses options, which provide information about the phone and its operation:

Network Statistics: Displays the Network Statistics screen, which shows Ethernet traffic statistics

Call Statistics: Displays counters and statistics for the current call.

Step 1

Press Applications .

Step 2

Select Admin
                                                				  Settings > Status .

Step 3

To exit the Status menu, press Back .

### Display Status Messages Window

To display the Status Messages screen,

Step 1

Press Applications .

Step 2

Select Admin Settings > Status Messages .

For information on the messages, see Status Messages .

Step 3

To exit the Status Messages screen, press Back .

#### Status Messages

Message

Description

Possible Explanation and Action

CFG file not found

The name-based and default configuration file was not found on
                                                					 the TFTP Server.

The configuration file for a phone is created when the phone
                                                					 is added to the Cisco UnifiedCommunications Manager database. If the phone has
                                                					 not been added to the Cisco UnifiedCommunications Manager database, the TFTP
                                                					 server generates a CFG File Not Found response.

You must manually add the phone to Cisco
                                                      						  UnifiedCommunications Manager if you are not allowing phones to auto-register.
                                                      						  See Phone Addition Methods for details.

- If you are using
                                                   						DHCP, verify that the DHCP server is pointing to the correct TFTP server.

- If you are using
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

- Network is busy.
                                                   						The errors should resolve themselves when the network load reduces.

- No network
                                                   						connectivity between the DHCP server and the phone. Verify the network
                                                   						connections.

- DHCP server is
                                                   						down. Check the DHCP server configuration.

- Errors persist.
                                                   						Consider assigning a static IP address.

DNS timeout

DNS server did not respond.

- Network is busy.
                                                   						The errors should resolve themselves when the network load reduces.

- No network
                                                   						connectivity between the DNS server and the phone. Verify the network
                                                   						connections.

- DNS server is down. Check the DNS server configuration.

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

File not found

The phone cannot locate, on the TFTP server, the phone load
                                                					 file that is specified in the phone configuration file.

From Cisco Unified Operating System Administration, make sure
                                                					 that the phone load file is on the TFTP server, and that the entry in the
                                                					 configuration file is correct.

IP address released

The phone has been configured to release its IP address.

The phone remains idle until it is power cycled or you reset
                                                					 the DHCP address.

Load ID incorrect

Load ID of the software file is of the wrong type.

Check the load ID assigned to the phone (from Cisco
                                                					 UnifiedCommunications Manager, choose Device > Phone ).
                                                					 Verify that the load ID is entered correctly.

Load rejected HC

The application that was downloaded is not compatible with the
                                                					 phone’s hardware.

Occurs if you were attempting to install a version of software
                                                					 on this phone that did not support hardware changes on this newer phone.

Check the load ID assigned to the phone (from Cisco
                                                					 UnifiedCommunications Manager, choose Device > Phone ). Re-enter the load displayed on the phone.

No default router

DHCP or static configuration did not specify a default router.

- If the phone has a
                                                   						static IP address, verify that the default router has been configured.

- If you are using
                                                   						DHCP, the DHCP server has not provided a default router. Check the DHCP server
                                                   						configuration.

No DNS server IP

A name was specified but DHCP or static IP configuration did
                                                					 not specify a DNS server address.

- If the phone has a
                                                   						static IP address, verify that the DNS server has been configured.

- If you are using
                                                   						DHCP, the DHCP server has not provided a DNS server. Check the DHCP server
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

Check the load ID assigned to the phone (from Cisco
                                                					 UnifiedCommunications Manager, choose Device > Phone ).
                                                					 Verify that the TFTPPath directory contains a .bin file with this load ID as
                                                					 the name.

TFTP timeout

TFTP server did not respond.

- Network is busy.
                                                   						The errors should resolve themselves when the network load reduces.

- No network
                                                   						connectivity between the TFTP server and the phone. Verify the network
                                                   						connections.

- TFTP server is
                                                   						down. Check the TFTP server configuration.

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

### Display Network Statistics Screen

The Network Statistics screen displays information about the
                                 		  phone and network performance.

Step 1

Press Applications .

Step 2

Select Admin Settings .

Step 3

Select Status .

Step 4

Select Network Statistics . Network Statistics Fields describes the information that appears in this screen.

Step 5

To exit the Network Statistics screen, press Back .

#### Network Statistics Fields

The following table lists the Network Statistics Message
                                    		  information.

Item

Description

Rx Frames

Number of packets received by the phone

Tx Frames

Number of packets sent by the phone

Rx Broadcasts

Number of broadcast packets received by the phone

Restart Cause

Cause of the last reset of the phone - One of these values:

- Hardware Reset
                                                   						(Power-on reset)

- Software Reset
                                                   						(memory controller also reset)

- Software Reset
                                                   						(memory controller not reset)

- Watchdog Reset

- Unknown

Port 1

Link state and connection of the PC port (for example, Auto 100 Mb Full-Duplex means that the
                                                					 PC port is in a link-up state and has auto-negotiated a full-duplex, 100-Mbps
                                                					 connection)

Port 2

Link state and connection of the Network port

IPv4

Information on the DHCP status. This includes the following
                                                					 states:

- CDP BOUND

- CDP INIT

- DHCP BOUND

- DHCP DISABLED

- DHCP INIT

- DHCP INVALID

- DHCP REBINDING

- DHCP REBOOT

- DHCP RENEWING

- DHCP REQUESTING

- DHCP RESYNC

- DHCP UNRECOGNIZED

- DHCP WAITING
                                                   						COLDBOOT TIMEOUT

- SET DHCP COLDBOOT

- SET DHCP DISABLED

- DISABLED DUPLICATE
                                                   						IP

- SET DHCP FAST

### Display Call Statistics Window

You can access the Call Statistics screen on the phone to display counters, statistics, and voice-quality metrics of the most
                                 recent call.

You can also remotely view the call statistics information by using a web browser to access the Streaming Statistics web page.
                                             This web page contains additional RTCP statistics not available on the phone. For more information about remote monitoring,
                                             see Cisco IP Phone Web Page .

A single call can have multiple voice streams, but data is captured for only the last voice stream. A voice stream is a packet
                                 stream between two endpoints. If one endpoint is put on hold, the voice stream stops even though the call is still connected.
                                 When the call resumes, a new voice packet stream begins, and the new call data overwrites the former call data.

To display the Call Statistics screen for information about the latest voice stream, perform these steps:

Step 1

Press Applications .

Step 2

Select Admin Settings .

Step 3

Select Status .

Step 4

Select Call Statistics .

Call Statistics Fields describes the information that appears in this window.

Step 5

To exit the Call Statistics window, press Back .

#### Call Statistics Fields

The following table contains the fields in the Call
                                    		  Statistics screen.

Item

Description

Rcvr Codec

Type of voice stream received (RTP streaming audio from
                                                					 codec): G.729, G.711 u-law, G.711 A-law.

Sender Codec

Type of voice stream transmitted (RTP streaming audio from
                                                					 codec): G.729, G.711 u-law, G.711 A-law.

Avg Jitter

Estimated average RTP packet jitter (dynamic delay that a
                                                					 packet encounters when going through the network) observed since the receiving
                                                					 voice stream was opened.

Max Jitter

Maximum jitter observed since the receiving voice stream was
                                                					 opened.

Voice Quality Metrics

MOS LQK

Objective estimate of the Mean Opinion Score (MOS) for
                                                					 Listening Quality (LQK) that ranks audio quality from 5 (excellent) to 1 (bad).
                                                					 This score is based on audible-concealment events due to a frame loss in the
                                                					 preceding 8 seconds of the voice stream.

The MOS LQK score can vary based on the type of codec that
                                                            						the CiscoUnifiedIPPhone uses.

Avg MOS LQK

Average MOS LQK score for the entire voice stream.

Min MOS LQK

Lowest MOS LQK score from the start of the voice stream.

Max MOS LQK

Baseline or highest MOS LQK score from the start of the voice
                                                					 stream.

The following codecs provide the corresponding maximum MOS LQK
                                                					 scores under normal conditions with no frame loss:

- G.711: 4.5

- G729A/AB: 3.7

MOS LQK Version

Version of the Cisco-proprietary algorithm used to calculate
                                                					 the MOS LQK scores.

Latency

Estimate of the network latency, expressed in milliseconds.
                                                					 Represents a running average of the round-trip delay, measured when RTCP
                                                					 receiver report blocks are received.

## Cisco IP Phone Web
                        	 Page

Each Cisco
                              		  IP Phone has a web page from which you can view a variety of information about
                              		  the phone, including:

Device
                                    				information: Displays device settings and related information for the phone.

Network setup
                                    				information: Displays network setup information and information about other
                                    				phone settings.

Network
                                    				statistics: Displays hyperlinks that provide information about network traffic.

Device logs:
                                    				Displays hyperlinks that provide information that you can use for
                                    				troubleshooting.

Streaming
                                    				statistic: Includes the Audio and Video statistics, Stream 1, Stream 2, Stream
                                    				3, Stream 4, Stream 5 and Stream 6 hyperlinks, which display a variety of
                                    				streaming statistics.

This
                              		  section describes the information that you can obtain from the phone web page.
                              		  You can use this information to remotely monitor the operation of a phone and
                              		  to assist with troubleshooting.

You can
                              		  also obtain much of this information directly from a phone.

### Access Web Page for Phone

To access the web page for a Cisco Unified IP Phone, perform
                                 		  these steps.

If you cannot access the web page, it may be disabled. See Control Phone Web Page Access for more information.

Step 1

Obtain the IP address of the Cisco Unified IP Phone using one of
                                          			 these methods:

- Search for the
                                             				phone in Cisco Unified Communications Manager by choosing Device > Phone .
                                             				Phones registered with Cisco Unified Communications Manager display the IP
                                             				address on the Find and List Phones window and at the top
                                             				of the Phone Configuration window.

- On the Cisco
                                             				Unified IP Phone, press Applications , choose Network > IPv4 ,
                                             				and then scroll to the IP Address option.

Step 2

Open a web browser and enter the following URL, where IP_address is the IP address of the Cisco Unified IP Phone:

http:/ /IP_address

### Device Information

The Device Information area on a phone web page displays
                              		  device settings and related information for the phone. The following table
                              		  describes these items.

To display the Device Information area, access the web page
                              		  for the phone as described in Access Web Page for Phone ,
                              		  and click the Device Information hyperlink.

Item

Description

MAC Address

Media Access Control (MAC) address of the phone

Host Name

Unique, fixed name that is automatically assigned to the phone
                                          					 based on its MAC address

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

### Network Setup Page

The Network Setup page on a phone web page displays network
                              		  setup information and information about other phone settings. The following
                              		  table describes these items.

You can view and set many of these items from the Network
                              		  Setup Menu and the Phone Information Menu on the CiscoUnified IP Phone. For
                              		  more information, see Cisco Unified SIP Phone Installation

To display the Network Setup area, access the web page for
                              		  the phone as described in the Access Web Page for Phone ,
                              		  and click the Network Configuration hyperlink.

Item

Description

DHCP Server

IP address of the Dynamic Host Configuration Protocol (DHCP)
                                          					 server from which the phone obtains its IP address.

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

DNS Server 1–5

Primary Domain Name System (DNS) server (DNS Server 1) and
                                          					 optional backup DNS server (DNS Server 2 - 5) used by the phone.

Operational VLAN ID

Auxiliary Virtual Local Area Network (VLAN) configured on a
                                          					 Cisco Catalyst switch in which the phone is a member.

Admin VLAN ID

Auxiliary VLAN in which the phone is a member.

CallManager 1–5

Host names or IP addresses, in prioritized order, of the
                                          					 CiscoUnifiedCommunications Manager servers with which the phone can register.
                                          					 An item can also show the IP address of an SRST router that is capable of
                                          					 providing limited CiscoUnifiedCommunications Manager functionality, if such a
                                          					 router is available.

For an available server, an item will show the
                                          					 CiscoUnifiedCommunications Manager server IP address and one of the following
                                          					 states:

- Active:
                                             						CiscoUnifiedCommunications Manager server from which the phone is currently
                                             						receiving call-processing services.

- Standby:
                                             						CiscoUnifiedCommunications Manager server to which the phone switches if the
                                             						current server becomes unavailable.

- Blank: No current
                                             						connection to this CiscoUnifiedCommunications Manager server.

An item may also include the Survivable Remote Site Telephony
                                          					 (SRST) designation, which identifies an SRST router capable of providing
                                          					 CiscoUnifiedCommunications Manager functionality with a limited feature set.
                                          					 This router assumes control of call processing if all other
                                          					 CiscoUnifiedCommunications Manager servers become unreachable. The SRST
                                          					 CiscoUnifiedCommunications Manager always appears last in the list of
                                          					 servers, even if it is active. You configure the SRST router address in the
                                          					 Device Pool section in CiscoUnifiedCommunications Manager
                                          						Configuration window.

DHCP Enabled

Indicates if DHCP is being used by the phone.

DHCP Address Released

Indicates the setting of the DHCP Address Released option on
                                          					 the phone’s Network Configuration menu.

Alternate TFTP

Indicates if the phone is using an alternative TFTP
                                          					 server.

SW Port Setup Auto Negotiate

Indicates if switch port is set to auto negotiate.

PC Port Setup Auto Negotiate

Indicates if PC port is set to auto negotiate.

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

Indicates if the PC port on the phone is enabled or
                                          					 disabled.

Speaker Enabled

Indicates if the speakerphone is enabled on the phone.

GARP Enabled

Indicates if the phone learns MAC addresses from
                                          					 Gratuitous ARP responses.

Voice VLAN Enabled

Indicates if the phone allows a device attached to the PC
                                          					 port to access the Voice VLAN.

DSCP for Call Control

DSCP IP classification for call control signaling.

DSCP for Configuration

DSCP IP classification for any phone configuration transfer.

DSCP for Services

DSCP IP classification for phone-based services.

Web Access Enabled

Indicates if web access is enabled (Yes) or disabled (No)
                                          					 for the phone.

Span to PC Port

Indicates if the phone forwards packets transmitted
                                          					 and received on the network port to the access port.

PC VLAN

VLAN used to identify and remove 802.1P/Q tags from packets
                                          					 sent to the PC.

CDP: PC Port

Indicates if CDP is supported on the PC port (default is
                                          					 enabled).

Enable CDP on the PC port when Cisco VT Advantage/Unified
                                          					 Video Advantage (CVTA) is connected to the PC port. CVTA does not work without
                                          					 CDP interaction with the phone.

When CDP is disabled in Cisco Unified Communications Manager,
                                          					 a warning is displayed, indicating that disabling CDP on the PC port prevents
                                          					 CVTA from working.

The current PC and switch port CDP values are shown on the
                                          					 Settings menu.

CDP: SW Port

Indicates if CDP is supported on the switch port (default
                                          					 is enabled).

Enable CDP on the switch port for VLAN assignment for the
                                          					 phone, power negotiation, QoS management, and 802.1x security.

Enable CDP on the switch port when the phone is connected to a
                                          					 Cisco switch.

When CDP is disabled in Cisco Unified Communications Manager,
                                          					 a warning is presented, indicating that CDP should be disabled on the switch
                                          					 port only if the phone is connected to a non-Cisco switch.

The current PC and switch port CDP values are shown on the
                                          					 Settings menu.

### Network Statistics

The following table lists the Network Statistics information.

Item

Description

Rx Frames

Number of packets received by the phone

Tx Frames

Number of packets sent by the phone

Rx Broadcasts

Number of broadcast packets received by the phone

Restart Cause

Cause of the last reset of the phone - One of these values:

- Hardware Reset
                                                						(Power-on reset)

- Software Reset
                                                						(memory controller also reset)

- Software Reset
                                                						(memory controller not reset)

- Watchdog Reset

- Unknown

Port 1

Link state and connection of the Network port

Port 2

Link state and connection of the PC port (for example, Auto 100 Mb Full-Duplex means that the
                                             					 PC port is in a link-up state and has auto-negotiated a full-duplex, 100-Mbps
                                             					 connection)

IPv4

Information on the DHCP status. This includes the following
                                             					 states:

- CDP BOUND

- CDP INIT

- DHCP BOUND

- DHCP DISABLED

- DHCP INIT

- DHCP INVALID

- DHCP REBINDING

- DHCP REBOOT

- DHCP RENEWING

- DHCP REQUESTING

- DHCP RESYNC

- DHCP UNRECOGNIZED

- DHCP WAITING
                                                						COLDBOOT TIMEOUT

- SET DHCP COLDBOOT

- SET DHCP DISABLED

- DISABLED DUPLICATE
                                                						IP

- SET DHCP FAST

#### Ethernet Information Web Page

The following table describes the contents of the Ethernet Information web page.

Item

Description

Tx Frames

Total number of packets that the phone transmits.

Tx broadcast

Total number of broadcast packets that the phone transmits.

Tx multicast

Total number of multicast packets that the phone transmits.

Tx unicast

Total number of unicast packets that the phone transmits.

Rx Frames

Total number of packets received by the phone.

Rx broadcast

Total number of broadcast packets that the phone receives..

Rx multicast

Total number of multicast packets that the phone receives.

Rx unicast

Total number of unicast packets that the phone receives.

Rx PacketNoDes

Total number of shed packets that the no Direct Memory Access (DMA) descriptor causes.

#### Network Information Fields

The following table describes the information in the Network Area web page.

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

Identifier of a device connected to this port discovered by CDP protocol or LLDP

Neighbor IP Address

IP address of the neighbor device discovered by CDP protocol

Neighbor Port

Neighbor device port to which the phone is connected discovered by CDP protocol

LLDP AgeoutsTotal

Total number of LLDP frames that have been time out in cache

LLDP FramesDiscardedTotal

Total number of LLDP frames that are discarded when any of the mandatory TLVs is missing or out of order or contains out of
                                                range string length

LLDP FramesInErrorsTotal

Total number of LLDP frames that received with one or more detectable errors

LLDP FramesInTotal

Total number of LLDP frames received on the phone

LLDP TLVDiscardedTotal

Total number of LLDP TLVs that are discarded

LLDP TLVUnrecognizedTotal

Total number of LLDP TLVs that are not recognized on the phone

Restart Cause

Reason for the last restart

Port 1-2

Speed and duplex information

IPv4

IPv4 Address

IPv6

IPv6 Address

### Device Logs

The following device logs hyperlinks on a phone web page
                                 		provide information you can use to help monitor and troubleshoot the phone.

Console Logs: Includes hyperlinks to individual log files. The
                                       			 console log files include debug and error messages received on the phone.

Core Dumps: Includes hyperlinks to individual dump files. The core
                                       			 dump files include data from a phone crash.

Status Messages: Displays up to the 30 most recent status messages
                                       			 that the phone has generated since it was last powered up. You can also see
                                       			 this information from the Status Messages screen on the Web page of the phone. 
                                       			 The following table describes the status
                                       			 messages that may be displayed.

Debug Display: Displays debug messages that might be useful to the
                                       			 Cisco Technical Assistance Center (TAC) if you require assistance with
                                       			 troubleshooting.

The Status Messages web page displays up to 30 of the most
                                 		  recent status messages that the phone has generated since it was last powered
                                 		  up. You can access the Status Messages web page even if the phone is not
                                 		  running. The following table describes the status messages. This table also
                                 		  includes possible explanations and actions to troubleshoot errors.

Message

Description

Possible explanation and action

CFG file not found

The name-based and default configuration file was not found on
                                             					 the TFTP Server.

The configuration file for a phone is created when the phone
                                             					 is added to the Cisco UnifiedCommunications Manager database. If the phone has
                                             					 not been added to the Cisco UnifiedCommunications Manager database, the TFTP
                                             					 server generates a CFG File Not Found response.

You must manually add the phone to Cisco
                                                   						  UnifiedCommunications Manager if you are not allowing phones to autoregister.
                                                   						  See Phone Addition Methods for details.

- If you are using
                                                						DHCP, verify that the DHCP server is pointing to the correct TFTP server.

- If you are using
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

- Network is busy.
                                                						The errors should resolve themselves when the network load reduces.

- No network
                                                						connectivity between the DHCP server and the phone. Verify the network
                                                						connections.

- DHCP server is
                                                						down. Check the DHCP server configuration.

- Errors persist.
                                                						Consider assigning a static IP address.

DNS timeout

DNS server did not respond.

- Network is busy.
                                                						The errors should resolve themselves when the network load reduces.

- No network
                                                						connectivity between the DNS server and the phone. Verify the network
                                                						connections.

- DNS server is down. Check the DNS server configuration.

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

File not found

The phone cannot locate, on the TFTP server, the phone load
                                             					 file that is specified in the phone configuration file.

From Cisco Unified Operating System Administration, make sure
                                             					 that the phone load file is on the TFTP server, and that the entry in the
                                             					 configuration file is correct.

IP address released

The phone has been configured to release its IP address.

The phone remains idle until it is power cycled or you reset
                                             					 the DHCP address.

Load ID incorrect

Load ID of the software file is of the wrong type.

Check the load ID assigned to the phone (from Cisco
                                             					 UnifiedCommunications Manager, choose Device > Phone ).
                                             					 Verify that the load ID is entered correctly.

Load rejected HC

The application that was downloaded is not compatible with the
                                             					 phone’s hardware.

Occurs if you were attempting to install a version of software
                                             					 on this phone that did not support hardware changes on this newer phone.

Check the load ID assigned to the phone (from Cisco
                                             					 UnifiedCommunications Manager, choose Device > Phone ). Re-enter the load displayed on the phone.

No default router

DHCP or static configuration did not specify a default router.

- If the phone has a
                                                						static IP address, verify that the default router has been configured.

- If you are using
                                                						DHCP, the DHCP server has not provided a default router. Check the DHCP server
                                                						configuration.

No DNS server IP

A name was specified but DHCP or static IP configuration did
                                             					 not specify a DNS server address.

- If the phone has a
                                                						static IP address, verify that the DNS server has been configured.

- If you are using
                                                						DHCP, the DHCP server has not provided a DNS server. Check the DHCP server
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

Check the load ID assigned to the phone (from Cisco
                                             					 UnifiedCommunications Manager, choose Device > Phone ).
                                             					 Verify that the TFTPPath directory contains a .bin file with this load ID as
                                             					 the name.

TFTP timeout

TFTP server did not respond.

- Network is busy.
                                                						The errors should resolve themselves when the network load reduces.

- No network
                                                						connectivity between the TFTP server and the phone. Verify the network
                                                						connections.

- TFTP server is
                                                						down. Check the TFTP server configuration.

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

### Streaming Statistics

A Cisco Unified IP Phone can stream information to and from
                                 		  up to three devices simultaneously. A phone streams information when it is on a
                                 		  a call or running a service that sends or receives audio or data.

The streaming statistics areas on a phone web page provide
                                 		  information about the streams. Cisco Unified SIP Phone 3905 use only Stream 1.

To display a Streaming Statistics area, access the web page
                                 		  for the phone as described in Access Web Page for Phone and click the 
                                 		  Stream 1 hyperlink.

Item

Description

Remote Address

IP address and UDP port of the destination of the stream.

Local Address

IP address and UDP port of the phone.

Start Time

Internal time stamp indicating when
                                             					 Cisco Unified Communications Manager requested that the phone start
                                             					 transmitting packets.

Stream Status

Indication of whether streaming is active or not.

Host Name

Unique, fixed name that is automatically assigned to the phone
                                             					 based on its MAC address.

Sender Packets

Total number of RTP data packets transmitted by the phone
                                             					 since starting this connection. The value is 0 if the connection is set to
                                             					 receive only mode.

Sender Octets

Total number of payload octets transmitted in RTP data packets
                                             					 by the phone since starting this connection. The value is 0 if the connection
                                             					 is set to receive only mode.

Sender Codec

Type of audio encoding used for the transmitted stream.

Sender Reports Sent

Number of times the RTCP Sender Report have been sent.

When the RTCP Control Protocol is disabled, no data generates for this field and thus displays as 0.

Sender Report Time Sent

Internal time stamp indication when the last RTCP Sender
                                             					 Report was sent.

When the RTCP Control Protocol is disabled, no data generates for this field and thus displays as 0.

Rcvr Lost Packets

Total number of RTP data packets that have been lost since
                                             					 starting receiving data on this connection. Defined as the number of expected
                                             					 packets less the number of packets actually received, where the number of
                                             					 received packets includes any that are late or duplicate. The value displays as
                                             					 0 if the connection was set to send-only mode.

Avg Jitter

Estimate of mean deviation of the RTP data packet
                                             					 inter-arrival time, measured in milliseconds. The value displays as 0 if the
                                             					 connection was set to send-only mode.

Rcvr Codec

Type of audio encoding used for the received stream.

Rcvr Reports Sent

Number of times the RTCP Receiver Reports have been sent.

When the RTCP Control Protocol is disabled, no data generates for this field and thus displays as 0.

Rcvr Report Time Sent

Internal time stamp indication when a RTCP Receiver Report was
                                             					 sent.

When the RTCP Control Protocol is disabled, no data generates for this field and thus displays as 0.

Rcvr Packets

Total number of RTP data packets received by the phone since
                                             					 starting receiving data on this connection. Includes packets received from
                                             					 different sources if this is a multicast call. The value displays as 0 if the
                                             					 connection was set to send-only mode.

Rcvr Octets

Total number of payload octets received in RTP data packets by
                                             					 the device since starting reception on the connection. Includes packets
                                             					 received from different sources if this is a multicast call. The value displays
                                             					 as 0 if the connection was set to send-only mode.

MOS LQK

Objective estimate of the Mean Opinion Score (MOS) for
                                             					 Listening Quality (LQK) that ranks audio quality from 5 (excellent) to 1 (bad).
                                             					 This score is based on audible-concealment events due to a frame loss in the
                                             					 preceding 8 seconds of the voice stream.

The MOS LQK score can vary based on the type of codec that
                                                         						the Cisco Unified IP Phone uses.

Avg MOS LQK

Average MOS LQK score for the entire voice stream.

Min MOS LQK

Lowest MOS LQK score from the start of the voice stream.

Max MOS LQK

Baseline or highest MOS LQK score from the start of the voice
                                             					 stream.

The following codecs provide the corresponding maximum MOS LQK
                                             					 scores under normal conditions with no frame loss:

- G.711: 4.5

- G729A/AB: 3.7

MOS LQK Version

Version of the Cisco-proprietary algorithm used to calculate
                                             					 the MOS LQK scores.

Cumulative Conceal Ratio

Total number of concealment frames divided by total number of
                                             					 speech frames received from start of the voice stream.

Interval Conceal Ratio

Ratio of concealment frames to speech frames in preceding
                                             					 3-second interval of active speech. If using voice activity detection (VAD), a
                                             					 longer interval might be required to accumulate 3 seconds of active speech.

Max Conceal Ratio

Highest interval concealment ratio from start of the voice
                                             					 stream.

Conceal Secs

Number of seconds that have concealment events (lost frames)
                                             					 from the start of the voice stream (includes severely concealed seconds).

Severely Conceal Secs

Number of seconds that have more than 5 percent concealment
                                             					 events (lost frames) from the start of the voice stream.

Latency

Estimate of the network latency, expressed in milliseconds.
                                             					 Represents a running average of the round-trip delay, measured when RTCP
                                             					 receiver report blocks are received.

When the RTCP Control Protocol is disabled, no data generates for this field and thus displays as 0.

Max Jitter

Maximum value of instantaneous jitter, in milliseconds.

Sender Size

RTP packet size, in milliseconds, for the transmitted stream.

Sender Reports Received

Number of times RTCP Sender Reports have been received.

When the RTCP Control Protocol is disabled, no data generates for this field and thus displays as 0.

Sender Report Time Received

Last time at which an RTCP Sender Report was received.

When the RTCP Control Protocol is disabled, no data generates for this field and thus displays as 0.

Rcvr Size

RTP packet size, in milliseconds, for the received stream.

Rcvr Discarded

RTP packets received from network but discarded from jitter
                                             					 buffers.

Rcvr Reports Received

Number of times RTCP Receiver Reports have been received.

When the RTCP Control Protocol is disabled, no data generates for this field and thus displays as 0.

Rcvr Report Time Received

Last time at which an RTCP Receiver Report was received.

When the RTCP Control Protocol is disabled, no data generates for this field and thus displays as 0.

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Phone Information . If the user is connected to a secure or authenticated server, a
                                             				corresponding icon (lock or certificate) displays in the Phone Information
                                             				Screen to the right of the server option. If the user is not connected to a
                                             				secure or authenticated server, no icon appears. |
| Step 3 | To exit the Model Information screen, press Back . |

| Option | Description | To Change |
|---|---|---|
| Model Number | Model number of the phone. | Display only - cannot configure. |
| MAC Address | MAC address of the phone. | Display only - cannot configure. |
| Active Load ID | Version of firmware currently installed on the phone. | Display only - cannot configure. |
| Boot Load ID | Identifier of the factory-installed load running on the phone. | Display only - cannot configure. |
| IP Address | IP address of the phone. | Display only - cannot configure. |
| Active Server | IP address or name of the server to which the phone is
                                             					 registered. | Display only - cannot configure. |
| Stand-by Server | IP address or name of the standby server. | Display only - cannot configure. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Admin
                                                				  Settings > Status . |
| Step 3 | To exit the Status menu, press Back . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Admin Settings > Status Messages . For information on the messages, see Status Messages . |
| Step 3 | To exit the Status Messages screen, press Back . |

| Message | Description | Possible Explanation and Action |
|---|---|---|
| CFG file not found | The name-based and default configuration file was not found on
                                                					 the TFTP Server. | The configuration file for a phone is created when the phone
                                                					 is added to the Cisco UnifiedCommunications Manager database. If the phone has
                                                					 not been added to the Cisco UnifiedCommunications Manager database, the TFTP
                                                					 server generates a CFG File Not Found response. Phone is not
                                                   						registered with Cisco Unified Communications Manager. You must manually add the phone to Cisco
                                                      						  UnifiedCommunications Manager if you are not allowing phones to auto-register.
                                                      						  See Phone Addition Methods for details. If you are using
                                                   						DHCP, verify that the DHCP server is pointing to the correct TFTP server. If you are using
                                                   						static IP addresses, check the TFTP server configuration. |
| CFG TFTP Size Error | The configuration file is too large for the file system on the
                                                					 phone. | Power cycle the phone. |
| Checksum Error | Downloaded software file is corrupted. | Obtain a new copy of the phone firmware and place it in the
                                                					 TFTPPath directory. You should only copy files into this directory when the
                                                					 TFTP server software is shut down, otherwise the files may be corrupted. |
| DHCP timeout | DHCP server did not respond. | Network is busy.
                                                   						The errors should resolve themselves when the network load reduces. No network
                                                   						connectivity between the DHCP server and the phone. Verify the network
                                                   						connections. DHCP server is
                                                   						down. Check the DHCP server configuration. Errors persist.
                                                   						Consider assigning a static IP address. |
| DNS timeout | DNS server did not respond. | Network is busy.
                                                   						The errors should resolve themselves when the network load reduces. No network
                                                   						connectivity between the DNS server and the phone. Verify the network
                                                   						connections. DNS server is down. Check the DNS server configuration. |
| DNS unknown host | DNS could not resolve the name of the TFTP server or Cisco
                                                					 Unified Communications Manager. | Verify that the
                                                   						host names of the TFTP server or Cisco UnifiedCommunications Manager are
                                                   						configured properly in DNS. Consider using IP
                                                   						addresses rather than host names. |
| Duplicate IP | Another device is using the IP address assigned to the phone. | If the phone has a
                                                   						static IP address, verify that you have not assigned a duplicate IP address. If you are using
                                                   						DHCP, check the DHCP server configuration. |
| File not found | The phone cannot locate, on the TFTP server, the phone load
                                                					 file that is specified in the phone configuration file. | From Cisco Unified Operating System Administration, make sure
                                                					 that the phone load file is on the TFTP server, and that the entry in the
                                                					 configuration file is correct. |
| IP address released | The phone has been configured to release its IP address. | The phone remains idle until it is power cycled or you reset
                                                					 the DHCP address. |
| Load ID incorrect | Load ID of the software file is of the wrong type. | Check the load ID assigned to the phone (from Cisco
                                                					 UnifiedCommunications Manager, choose Device > Phone ).
                                                					 Verify that the load ID is entered correctly. |
| Load rejected HC | The application that was downloaded is not compatible with the
                                                					 phone’s hardware. | Occurs if you were attempting to install a version of software
                                                					 on this phone that did not support hardware changes on this newer phone. Check the load ID assigned to the phone (from Cisco
                                                					 UnifiedCommunications Manager, choose Device > Phone ). Re-enter the load displayed on the phone. |
| No default router | DHCP or static configuration did not specify a default router. | If the phone has a
                                                   						static IP address, verify that the default router has been configured. If you are using
                                                   						DHCP, the DHCP server has not provided a default router. Check the DHCP server
                                                   						configuration. |
| No DNS server IP | A name was specified but DHCP or static IP configuration did
                                                					 not specify a DNS server address. | If the phone has a
                                                   						static IP address, verify that the DNS server has been configured. If you are using
                                                   						DHCP, the DHCP server has not provided a DNS server. Check the DHCP server
                                                   						configuration. |
| TFTP access error | TFTP server is pointing to a directory that does not exist. | If you are using
                                                   						DHCP, verify that the DHCP server is pointing to the correct TFTP server. If you are using
                                                   						static IP addresses, check the TFTP server configuration. |
| TFTP error | The phone does not recognize an error code provided by the
                                                					 TFTP server. | Contact the Cisco TAC. |
| TFTP file not found | The requested load file (.bin) was not found in the TFTPPath
                                                					 directory. | Check the load ID assigned to the phone (from Cisco
                                                					 UnifiedCommunications Manager, choose Device > Phone ).
                                                					 Verify that the TFTPPath directory contains a .bin file with this load ID as
                                                					 the name. |
| TFTP timeout | TFTP server did not respond. | Network is busy.
                                                   						The errors should resolve themselves when the network load reduces. No network
                                                   						connectivity between the TFTP server and the phone. Verify the network
                                                   						connections. TFTP server is
                                                   						down. Check the TFTP server configuration. |
| Timed Out | Supplicant attempted 802.1X transaction but timed out to due
                                                					 the absence of an authenticator. | Authentication typically times out if 802.1X is not configured
                                                					 on the switch. |
| Version error | The name of the phone load file is incorrect. | Make sure that the phone load file has the correct name. |
| XmlDefault.cnf.xml, or .cnf.xml corresponding to the phone
                                                					 device name | Name of the configuration file. | None. This is an informational message indicating the name of
                                                					 the configuration file for the phone. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Admin Settings . |
| Step 3 | Select Status . |
| Step 4 | Select Network Statistics . Network Statistics Fields describes the information that appears in this screen. |
| Step 5 | To exit the Network Statistics screen, press Back . |

| Item | Description |
|---|---|
| Rx Frames | Number of packets received by the phone |
| Tx Frames | Number of packets sent by the phone |
| Rx Broadcasts | Number of broadcast packets received by the phone |
| Restart Cause | Cause of the last reset of the phone - One of these values: Hardware Reset
                                                   						(Power-on reset) Software Reset
                                                   						(memory controller also reset) Software Reset
                                                   						(memory controller not reset) Watchdog Reset Unknown |
| Port 1 | Link state and connection of the PC port (for example, Auto 100 Mb Full-Duplex means that the
                                                					 PC port is in a link-up state and has auto-negotiated a full-duplex, 100-Mbps
                                                					 connection) |
| Port 2 | Link state and connection of the Network port |
| IPv4 | Information on the DHCP status. This includes the following
                                                					 states: CDP BOUND CDP INIT DHCP BOUND DHCP DISABLED DHCP INIT DHCP INVALID DHCP REBINDING DHCP REBOOT DHCP RENEWING DHCP REQUESTING DHCP RESYNC DHCP UNRECOGNIZED DHCP WAITING
                                                   						COLDBOOT TIMEOUT SET DHCP COLDBOOT SET DHCP DISABLED DISABLED DUPLICATE
                                                   						IP SET DHCP FAST |

| Note | You can also remotely view the call statistics information by using a web browser to access the Streaming Statistics web page.
                                             This web page contains additional RTCP statistics not available on the phone. For more information about remote monitoring,
                                             see Cisco IP Phone Web Page . |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Admin Settings . |
| Step 3 | Select Status . |
| Step 4 | Select Call Statistics . Call Statistics Fields describes the information that appears in this window. |
| Step 5 | To exit the Call Statistics window, press Back . |

| Item | Description |
|---|---|
| Rcvr Codec | Type of voice stream received (RTP streaming audio from
                                                					 codec): G.729, G.711 u-law, G.711 A-law. |
| Sender Codec | Type of voice stream transmitted (RTP streaming audio from
                                                					 codec): G.729, G.711 u-law, G.711 A-law. |
| Avg Jitter | Estimated average RTP packet jitter (dynamic delay that a
                                                					 packet encounters when going through the network) observed since the receiving
                                                					 voice stream was opened. |
| Max Jitter | Maximum jitter observed since the receiving voice stream was
                                                					 opened. |
| Voice Quality Metrics |
| MOS LQK | Objective estimate of the Mean Opinion Score (MOS) for
                                                					 Listening Quality (LQK) that ranks audio quality from 5 (excellent) to 1 (bad).
                                                					 This score is based on audible-concealment events due to a frame loss in the
                                                					 preceding 8 seconds of the voice stream. Note The MOS LQK score can vary based on the type of codec that
                                                            						the CiscoUnifiedIPPhone uses. | Note | The MOS LQK score can vary based on the type of codec that
                                                            						the CiscoUnifiedIPPhone uses. |
| Note | The MOS LQK score can vary based on the type of codec that
                                                            						the CiscoUnifiedIPPhone uses. |
| Avg MOS LQK | Average MOS LQK score for the entire voice stream. |
| Min MOS LQK | Lowest MOS LQK score from the start of the voice stream. |
| Max MOS LQK | Baseline or highest MOS LQK score from the start of the voice
                                                					 stream. The following codecs provide the corresponding maximum MOS LQK
                                                					 scores under normal conditions with no frame loss: G.711: 4.5 G729A/AB: 3.7 |
| MOS LQK Version | Version of the Cisco-proprietary algorithm used to calculate
                                                					 the MOS LQK scores. |
| Latency | Estimate of the network latency, expressed in milliseconds.
                                                					 Represents a running average of the round-trip delay, measured when RTCP
                                                					 receiver report blocks are received. |

| Note | The MOS LQK score can vary based on the type of codec that
                                                            						the CiscoUnifiedIPPhone uses. |
|---|---|

| Note | If you cannot access the web page, it may be disabled. See Control Phone Web Page Access for more information. |
|---|---|

| Step 1 | Obtain the IP address of the Cisco Unified IP Phone using one of
                                          			 these methods: Search for the
                                             				phone in Cisco Unified Communications Manager by choosing Device > Phone .
                                             				Phones registered with Cisco Unified Communications Manager display the IP
                                             				address on the Find and List Phones window and at the top
                                             				of the Phone Configuration window. On the Cisco
                                             				Unified IP Phone, press Applications , choose Network > IPv4 ,
                                             				and then scroll to the IP Address option. |
|---|---|
| Step 2 | Open a web browser and enter the following URL, where IP_address is the IP address of the Cisco Unified IP Phone: http:/ /IP_address |

| Item | Description |
|---|---|
| MAC Address | Media Access Control (MAC) address of the phone |
| Host Name | Unique, fixed name that is automatically assigned to the phone
                                          					 based on its MAC address |
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
                                          					 server from which the phone obtains its IP address. |
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
| DNS Server 1–5 | Primary Domain Name System (DNS) server (DNS Server 1) and
                                          					 optional backup DNS server (DNS Server 2 - 5) used by the phone. |
| Operational VLAN ID | Auxiliary Virtual Local Area Network (VLAN) configured on a
                                          					 Cisco Catalyst switch in which the phone is a member. |
| Admin VLAN ID | Auxiliary VLAN in which the phone is a member. |
| CallManager 1–5 | Host names or IP addresses, in prioritized order, of the
                                          					 CiscoUnifiedCommunications Manager servers with which the phone can register.
                                          					 An item can also show the IP address of an SRST router that is capable of
                                          					 providing limited CiscoUnifiedCommunications Manager functionality, if such a
                                          					 router is available. For an available server, an item will show the
                                          					 CiscoUnifiedCommunications Manager server IP address and one of the following
                                          					 states: Active:
                                             						CiscoUnifiedCommunications Manager server from which the phone is currently
                                             						receiving call-processing services. Standby:
                                             						CiscoUnifiedCommunications Manager server to which the phone switches if the
                                             						current server becomes unavailable. Blank: No current
                                             						connection to this CiscoUnifiedCommunications Manager server. An item may also include the Survivable Remote Site Telephony
                                          					 (SRST) designation, which identifies an SRST router capable of providing
                                          					 CiscoUnifiedCommunications Manager functionality with a limited feature set.
                                          					 This router assumes control of call processing if all other
                                          					 CiscoUnifiedCommunications Manager servers become unreachable. The SRST
                                          					 CiscoUnifiedCommunications Manager always appears last in the list of
                                          					 servers, even if it is active. You configure the SRST router address in the
                                          					 Device Pool section in CiscoUnifiedCommunications Manager
                                          						Configuration window. |
| DHCP Enabled | Indicates if DHCP is being used by the phone. |
| DHCP Address Released | Indicates the setting of the DHCP Address Released option on
                                          					 the phone’s Network Configuration menu. |
| Alternate TFTP | Indicates if the phone is using an alternative TFTP
                                          					 server. |
| SW Port Setup Auto Negotiate | Indicates if switch port is set to auto negotiate. |
| PC Port Setup Auto Negotiate | Indicates if PC port is set to auto negotiate. |
| User Locale | User locale associated with the phone user. Identifies a set
                                          					 of detailed information to support users, including language, font, date and
                                          					 time formatting, and alphanumeric keyboard text information. |
| Network Locale | Network locale associated with the phone user. Identifies a
                                          					 set of detailed information to support the phone in a specific location,
                                          					 including definitions of the tones and cadences used by the phone. |
| User Locale Version | Version of the user locale loaded on the phone. |
| Network Locale Version | Version of the network locale loaded on the phone. |
| PC Port Disabled | Indicates if the PC port on the phone is enabled or
                                          					 disabled. |
| Speaker Enabled | Indicates if the speakerphone is enabled on the phone. |
| GARP Enabled | Indicates if the phone learns MAC addresses from
                                          					 Gratuitous ARP responses. |
| Voice VLAN Enabled | Indicates if the phone allows a device attached to the PC
                                          					 port to access the Voice VLAN. |
| DSCP for Call Control | DSCP IP classification for call control signaling. |
| DSCP for Configuration | DSCP IP classification for any phone configuration transfer. |
| DSCP for Services | DSCP IP classification for phone-based services. |
| Web Access Enabled | Indicates if web access is enabled (Yes) or disabled (No)
                                          					 for the phone. |
| Span to PC Port | Indicates if the phone forwards packets transmitted
                                          					 and received on the network port to the access port. |
| PC VLAN | VLAN used to identify and remove 802.1P/Q tags from packets
                                          					 sent to the PC. |
| CDP: PC Port | Indicates if CDP is supported on the PC port (default is
                                          					 enabled). Enable CDP on the PC port when Cisco VT Advantage/Unified
                                          					 Video Advantage (CVTA) is connected to the PC port. CVTA does not work without
                                          					 CDP interaction with the phone. When CDP is disabled in Cisco Unified Communications Manager,
                                          					 a warning is displayed, indicating that disabling CDP on the PC port prevents
                                          					 CVTA from working. The current PC and switch port CDP values are shown on the
                                          					 Settings menu. |
| CDP: SW Port | Indicates if CDP is supported on the switch port (default
                                          					 is enabled). Enable CDP on the switch port for VLAN assignment for the
                                          					 phone, power negotiation, QoS management, and 802.1x security. Enable CDP on the switch port when the phone is connected to a
                                          					 Cisco switch. When CDP is disabled in Cisco Unified Communications Manager,
                                          					 a warning is presented, indicating that CDP should be disabled on the switch
                                          					 port only if the phone is connected to a non-Cisco switch. The current PC and switch port CDP values are shown on the
                                          					 Settings menu. |

| Item | Description |
|---|---|
| Rx Frames | Number of packets received by the phone |
| Tx Frames | Number of packets sent by the phone |
| Rx Broadcasts | Number of broadcast packets received by the phone |
| Restart Cause | Cause of the last reset of the phone - One of these values: Hardware Reset
                                                						(Power-on reset) Software Reset
                                                						(memory controller also reset) Software Reset
                                                						(memory controller not reset) Watchdog Reset Unknown |
| Port 1 | Link state and connection of the Network port |
| Port 2 | Link state and connection of the PC port (for example, Auto 100 Mb Full-Duplex means that the
                                             					 PC port is in a link-up state and has auto-negotiated a full-duplex, 100-Mbps
                                             					 connection) |
| IPv4 | Information on the DHCP status. This includes the following
                                             					 states: CDP BOUND CDP INIT DHCP BOUND DHCP DISABLED DHCP INIT DHCP INVALID DHCP REBINDING DHCP REBOOT DHCP RENEWING DHCP REQUESTING DHCP RESYNC DHCP UNRECOGNIZED DHCP WAITING
                                                						COLDBOOT TIMEOUT SET DHCP COLDBOOT SET DHCP DISABLED DISABLED DUPLICATE
                                                						IP SET DHCP FAST |

| Item | Description |
|---|---|
| Tx Frames | Total number of packets that the phone transmits. |
| Tx broadcast | Total number of broadcast packets that the phone transmits. |
| Tx multicast | Total number of multicast packets that the phone transmits. |
| Tx unicast | Total number of unicast packets that the phone transmits. |
| Rx Frames | Total number of packets received by the phone. |
| Rx broadcast | Total number of broadcast packets that the phone receives.. |
| Rx multicast | Total number of multicast packets that the phone receives. |
| Rx unicast | Total number of unicast packets that the phone receives. |
| Rx PacketNoDes | Total number of shed packets that the no Direct Memory Access (DMA) descriptor causes. |

| Item | Description |
|---|---|
| Tx Frames | Total number of packets transmitted by the phone |
| Tx broadcast | Total number of broadcast packets transmitted by the phone |
| Tx unicast | Total number of unicast packets transmitted by the phone |
| Rx Frames | Total number of packets received by the phone |
| Rx broadcast | Total number of broadcast packets received by the phone |
| Rx unicast | Total number of unicast packets received by the phone |
| Neighbor Device ID | Identifier of a device connected to this port discovered by CDP protocol or LLDP |
| Neighbor IP Address | IP address of the neighbor device discovered by CDP protocol |
| Neighbor Port | Neighbor device port to which the phone is connected discovered by CDP protocol |
| LLDP AgeoutsTotal | Total number of LLDP frames that have been time out in cache |
| LLDP FramesDiscardedTotal | Total number of LLDP frames that are discarded when any of the mandatory TLVs is missing or out of order or contains out of
                                                range string length |
| LLDP FramesInErrorsTotal | Total number of LLDP frames that received with one or more detectable errors |
| LLDP FramesInTotal | Total number of LLDP frames received on the phone |
| LLDP TLVDiscardedTotal | Total number of LLDP TLVs that are discarded |
| LLDP TLVUnrecognizedTotal | Total number of LLDP TLVs that are not recognized on the phone |
| Restart Cause | Reason for the last restart |
| Port 1-2 | Speed and duplex information |
| IPv4 | IPv4 Address |
| IPv6 | IPv6 Address |

| Message | Description | Possible explanation and action |
|---|---|---|
| CFG file not found | The name-based and default configuration file was not found on
                                             					 the TFTP Server. | The configuration file for a phone is created when the phone
                                             					 is added to the Cisco UnifiedCommunications Manager database. If the phone has
                                             					 not been added to the Cisco UnifiedCommunications Manager database, the TFTP
                                             					 server generates a CFG File Not Found response. Phone is not
                                                						registered with Cisco Unified Communications Manager. You must manually add the phone to Cisco
                                                   						  UnifiedCommunications Manager if you are not allowing phones to autoregister.
                                                   						  See Phone Addition Methods for details. If you are using
                                                						DHCP, verify that the DHCP server is pointing to the correct TFTP server. If you are using
                                                						static IP addresses, check the TFTP server configuration. |
| CFG TFTP Size Error | The configuration file is too large for the file system on the
                                             					 phone. | Power cycle the phone. |
| Checksum Error | Downloaded software file is corrupted. | Obtain a new copy of the phone firmware and place it in the
                                             					 TFTPPath directory. You should only copy files into this directory when the
                                             					 TFTP server software is shut down, otherwise the files may be corrupted. |
| DHCP timeout | DHCP server did not respond. | Network is busy.
                                                						The errors should resolve themselves when the network load reduces. No network
                                                						connectivity between the DHCP server and the phone. Verify the network
                                                						connections. DHCP server is
                                                						down. Check the DHCP server configuration. Errors persist.
                                                						Consider assigning a static IP address. |
| DNS timeout | DNS server did not respond. | Network is busy.
                                                						The errors should resolve themselves when the network load reduces. No network
                                                						connectivity between the DNS server and the phone. Verify the network
                                                						connections. DNS server is down. Check the DNS server configuration. |
| DNS unknown host | DNS could not resolve the name of the TFTP server or Cisco
                                             					 Unified Communications Manager. | Verify that the
                                                						host names of the TFTP server or Cisco UnifiedCommunications Manager are
                                                						configured properly in DNS. Consider using IP
                                                						addresses rather than host names. |
| Duplicate IP | Another device is using the IP address assigned to the phone. | If the phone has a
                                                						static IP address, verify that you have not assigned a duplicate IP address. If you are using
                                                						DHCP, check the DHCP server configuration. |
| File not found | The phone cannot locate, on the TFTP server, the phone load
                                             					 file that is specified in the phone configuration file. | From Cisco Unified Operating System Administration, make sure
                                             					 that the phone load file is on the TFTP server, and that the entry in the
                                             					 configuration file is correct. |
| IP address released | The phone has been configured to release its IP address. | The phone remains idle until it is power cycled or you reset
                                             					 the DHCP address. |
| Load ID incorrect | Load ID of the software file is of the wrong type. | Check the load ID assigned to the phone (from Cisco
                                             					 UnifiedCommunications Manager, choose Device > Phone ).
                                             					 Verify that the load ID is entered correctly. |
| Load rejected HC | The application that was downloaded is not compatible with the
                                             					 phone’s hardware. | Occurs if you were attempting to install a version of software
                                             					 on this phone that did not support hardware changes on this newer phone. Check the load ID assigned to the phone (from Cisco
                                             					 UnifiedCommunications Manager, choose Device > Phone ). Re-enter the load displayed on the phone. |
| No default router | DHCP or static configuration did not specify a default router. | If the phone has a
                                                						static IP address, verify that the default router has been configured. If you are using
                                                						DHCP, the DHCP server has not provided a default router. Check the DHCP server
                                                						configuration. |
| No DNS server IP | A name was specified but DHCP or static IP configuration did
                                             					 not specify a DNS server address. | If the phone has a
                                                						static IP address, verify that the DNS server has been configured. If you are using
                                                						DHCP, the DHCP server has not provided a DNS server. Check the DHCP server
                                                						configuration. |
| TFTP access error | TFTP server is pointing to a directory that does not exist. | If you are using
                                                						DHCP, verify that the DHCP server is pointing to the correct TFTP server. If you are using
                                                						static IP addresses, check the TFTP server configuration. |
| TFTP error | The phone does not recognize an error code provided by the
                                             					 TFTP server. | Contact the Cisco TAC. |
| TFTP file not found | The requested load file (.bin) was not found in the TFTPPath
                                             					 directory. | Check the load ID assigned to the phone (from Cisco
                                             					 UnifiedCommunications Manager, choose Device > Phone ).
                                             					 Verify that the TFTPPath directory contains a .bin file with this load ID as
                                             					 the name. |
| TFTP timeout | TFTP server did not respond. | Network is busy.
                                                						The errors should resolve themselves when the network load reduces. No network
                                                						connectivity between the TFTP server and the phone. Verify the network
                                                						connections. TFTP server is
                                                						down. Check the TFTP server configuration. |
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
                                             					 Cisco Unified Communications Manager requested that the phone start
                                             					 transmitting packets. |
| Stream Status | Indication of whether streaming is active or not. |
| Host Name | Unique, fixed name that is automatically assigned to the phone
                                             					 based on its MAC address. |
| Sender Packets | Total number of RTP data packets transmitted by the phone
                                             					 since starting this connection. The value is 0 if the connection is set to
                                             					 receive only mode. |
| Sender Octets | Total number of payload octets transmitted in RTP data packets
                                             					 by the phone since starting this connection. The value is 0 if the connection
                                             					 is set to receive only mode. |
| Sender Codec | Type of audio encoding used for the transmitted stream. |
| Sender Reports Sent | Number of times the RTCP Sender Report have been sent. When the RTCP Control Protocol is disabled, no data generates for this field and thus displays as 0. |
| Sender Report Time Sent | Internal time stamp indication when the last RTCP Sender
                                             					 Report was sent. When the RTCP Control Protocol is disabled, no data generates for this field and thus displays as 0. |
| Rcvr Lost Packets | Total number of RTP data packets that have been lost since
                                             					 starting receiving data on this connection. Defined as the number of expected
                                             					 packets less the number of packets actually received, where the number of
                                             					 received packets includes any that are late or duplicate. The value displays as
                                             					 0 if the connection was set to send-only mode. |
| Avg Jitter | Estimate of mean deviation of the RTP data packet
                                             					 inter-arrival time, measured in milliseconds. The value displays as 0 if the
                                             					 connection was set to send-only mode. |
| Rcvr Codec | Type of audio encoding used for the received stream. |
| Rcvr Reports Sent | Number of times the RTCP Receiver Reports have been sent. When the RTCP Control Protocol is disabled, no data generates for this field and thus displays as 0. |
| Rcvr Report Time Sent | Internal time stamp indication when a RTCP Receiver Report was
                                             					 sent. When the RTCP Control Protocol is disabled, no data generates for this field and thus displays as 0. |
| Rcvr Packets | Total number of RTP data packets received by the phone since
                                             					 starting receiving data on this connection. Includes packets received from
                                             					 different sources if this is a multicast call. The value displays as 0 if the
                                             					 connection was set to send-only mode. |
| Rcvr Octets | Total number of payload octets received in RTP data packets by
                                             					 the device since starting reception on the connection. Includes packets
                                             					 received from different sources if this is a multicast call. The value displays
                                             					 as 0 if the connection was set to send-only mode. |
| MOS LQK | Objective estimate of the Mean Opinion Score (MOS) for
                                             					 Listening Quality (LQK) that ranks audio quality from 5 (excellent) to 1 (bad).
                                             					 This score is based on audible-concealment events due to a frame loss in the
                                             					 preceding 8 seconds of the voice stream. Note The MOS LQK score can vary based on the type of codec that
                                                         						the Cisco Unified IP Phone uses. | Note | The MOS LQK score can vary based on the type of codec that
                                                         						the Cisco Unified IP Phone uses. |
| Note | The MOS LQK score can vary based on the type of codec that
                                                         						the Cisco Unified IP Phone uses. |
| Avg MOS LQK | Average MOS LQK score for the entire voice stream. |
| Min MOS LQK | Lowest MOS LQK score from the start of the voice stream. |
| Max MOS LQK | Baseline or highest MOS LQK score from the start of the voice
                                             					 stream. The following codecs provide the corresponding maximum MOS LQK
                                             					 scores under normal conditions with no frame loss: G.711: 4.5 G729A/AB: 3.7 |
| MOS LQK Version | Version of the Cisco-proprietary algorithm used to calculate
                                             					 the MOS LQK scores. |
| Cumulative Conceal Ratio | Total number of concealment frames divided by total number of
                                             					 speech frames received from start of the voice stream. |
| Interval Conceal Ratio | Ratio of concealment frames to speech frames in preceding
                                             					 3-second interval of active speech. If using voice activity detection (VAD), a
                                             					 longer interval might be required to accumulate 3 seconds of active speech. |
| Max Conceal Ratio | Highest interval concealment ratio from start of the voice
                                             					 stream. |
| Conceal Secs | Number of seconds that have concealment events (lost frames)
                                             					 from the start of the voice stream (includes severely concealed seconds). |
| Severely Conceal Secs | Number of seconds that have more than 5 percent concealment
                                             					 events (lost frames) from the start of the voice stream. |
| Latency | Estimate of the network latency, expressed in milliseconds.
                                             					 Represents a running average of the round-trip delay, measured when RTCP
                                             					 receiver report blocks are received. When the RTCP Control Protocol is disabled, no data generates for this field and thus displays as 0. |
| Max Jitter | Maximum value of instantaneous jitter, in milliseconds. |
| Sender Size | RTP packet size, in milliseconds, for the transmitted stream. |
| Sender Reports Received | Number of times RTCP Sender Reports have been received. When the RTCP Control Protocol is disabled, no data generates for this field and thus displays as 0. |
| Sender Report Time Received | Last time at which an RTCP Sender Report was received. When the RTCP Control Protocol is disabled, no data generates for this field and thus displays as 0. |
| Rcvr Size | RTP packet size, in milliseconds, for the received stream. |
| Rcvr Discarded | RTP packets received from network but discarded from jitter
                                             					 buffers. |
| Rcvr Reports Received | Number of times RTCP Receiver Reports have been received. When the RTCP Control Protocol is disabled, no data generates for this field and thus displays as 0. |
| Rcvr Report Time Received | Last time at which an RTCP Receiver Report was received. When the RTCP Control Protocol is disabled, no data generates for this field and thus displays as 0. |

| Note | The MOS LQK score can vary based on the type of codec that
                                                         						the Cisco Unified IP Phone uses. |
|---|---|