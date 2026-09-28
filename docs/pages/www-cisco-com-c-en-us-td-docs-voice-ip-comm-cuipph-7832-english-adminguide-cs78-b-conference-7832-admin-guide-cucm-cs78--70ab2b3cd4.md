---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7832-english-adminguide-cs78-b-conference-7832-admin-guide-cucm-cs78--70ab2b3cd4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7832/english/adminguide/cs78_b_conference-7832-admin-guide-cucm/cs78_b_conference-7832-admin-guide-cucm_chapter_0111.html
retrieved_at: 2026-08-21T13:27:37.177618+00:00
---

Cisco IP Conference Phone 7832 Administration Guide for Cisco Unified Communication Manager

# Cisco IP Conference Phone 7832 Administration Guide for Cisco Unified Communication Manager

Updated: November 6, 2025

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

Press Settings > Phone information .

Step 2

To exit the menu, press Exit .

### Display the Status Menu

Step 1

Press Settings > Status .

Step 2

To exit the menu, press Back .

#### Display the Status Messages Window

Step 1

Press Settings > Status > Status Messages .

Step 2

To exit the menu, press Back .

##### Status Messages Fields

The following table describes the status messages that
                                       		  display on the Status Messages screen of the phone.

Message

Description

Possible Explanation and Action

Could not acquire an IP address from DHCP

The phone has not previously obtained an IP
                                                   address from a DHCP Server. This can occur when you perform an out of box or factory
                                                   reset.

Confirm that the DHCP server is available and that an IP address is available  for the phone.

TFTP Size Error

The configuration file is too large for file system on the
                                                   					 phone.

Power cycle the phone.

ROM Checksum Error

Downloaded software file is corrupted.

Obtain a new copy of the phone firmware and place it in the
                                                   					 TFTPPath directory. You should only copy files into this directory when the
                                                   					 TFTP server software is shut down; otherwise, the files may be corrupted.

Duplicate IP

Another device is using the IP address that is assigned to the phone.

If the phone has a
                                                   						static IP address, verify that you did not assigned a duplicate IP address.

If you are using
                                                   						DHCP, check the DHCP server configuration.

Erasing CTL and ITL files

Erasing CTL or ITL file.

None. This message is informational only.

Error Updating Locale

One or more localization files could not be found in the
                                                   					 TFTP Path directory or were not valid. The locale was not changed.

From Cisco Unified Operating System Administration, check that
                                                   					 the following files are located within subdirectories in the TFTP File
                                                   					 Management:

tones.xml

glyphs.xml

dictionary.xml

kate.xml

File not found <Cfg File>

The name-based and default configuration file was not found on
                                                   					 the TFTP Server.

The configuration file for a phone is created when the phone
                                                   					 is added to the Cisco Unified Communications Manager database. If the phone
                                                   					 does not exist in the Cisco Unified Communications Manager database, the TFTP
                                                   					 server generates a CFG File Not Found response.

Phone is not
                                                         						registered with Cisco Unified Communications Manager.

You must manually add the phone to Cisco Unified
                                                         						  Communications Manager if you are not allowing phones to autoregister.

If you are using
                                                         						DHCP, verify that the DHCP server is pointing to the correct TFTP server.

If you are using
                                                         						static IP addresses, check configuration of the TFTP server.

File Not Found <CTLFile.tlv>

This message displays on the phone when the Cisco Unified
                                                   					 Communications Manager cluster is not in secure mode.

No impact; the phone can still register to Cisco Unified
                                                   					 Communications Manager.

IP Address Released

The phone is configured to release the IP address.

The phone remains idle until it is power cycled or until you reset
                                                   					 the DHCP address.

IPv4 DHCP Timeout

IPv4 DHCP server did not respond.

Network is
                                                   						busy: The errors should resolve themselves when the network load reduces.

No network
                                                   						connectivity between the IPv4 DHCP server and the phone: Verify the network
                                                   						connections.

IPv4 DHCP server is
                                                   						down: Check configuration of IPv4 DHCP server.

Errors
                                                   						persist: Consider assigning a static IPv4 address.

IPv6 DHCP Timeout

IPv6 DHCP server did not respond.

Network is
                                                   						busy - The errors should resolve themselves when the network load reduces.

No network
                                                   						connectivity between the IPv6 DHCP server and the phone: Verify the network
                                                   						connections.

IPv6 DHCP server is
                                                   						down: Check configuration of IPv6 DHCP server.

Errors
                                                   						persist: Consider assigning a static IPv6 address.

IPv4 DNS Timeout

IPv4 DNS server did not respond.

Network is
                                                   						busy: The errors should resolve themselves when the network load reduces.

No network
                                                   						connectivity between the IPv4 DNS server and the phone: Verify the network
                                                   						connections.

IPv4 DNS server is
                                                   						down: Check configuration of the IPv4 DNS server.

IPv6 DNS Timeout

IPv6 DNS server did not respond.

Network is
                                                   						busy: The errors should resolve themselves when the network load reduces.

No network
                                                   						connectivity between the IPv6 DNS server and the phone: Verify the network
                                                   						connections.

IPv6 DNS server is
                                                   						down: Check configuration of the IPv6 DNS server.

DNS unknown IPv4 Host

IPv4 DNS could not resolve the name of the TFTP server or Cisco
                                                   					 Unified Communications Manager.

Verify that the
                                                   						host names of the TFTP server or Cisco Unified Communications Manager are
                                                   						configured properly in IPv4 DNS.

Consider using IPv4
                                                   						addresses rather than host names

DNS unknown IPv6 Host

IPv6 DNS could not resolve the name of the TFTP server or Cisco
                                                   					 Unified Communications Manager.

Verify that the
                                                   						host names of the TFTP server or Cisco Unified Communications Manager are
                                                   						configured properly in IPv6 DNS.

Consider using IPv6
                                                   						addresses rather than host names

Load Rejected HC

The application that was downloaded is not compatible with the
                                                   					 phone hardware.

Occurs if you attempt to install a version of software
                                                   					 on this phone that did not support hardware changes on this  phone.

Check the load ID that is assigned to the phone (from Cisco Unified
                                                   					 Communications Manager, choose Device > Phone ).
                                                   					 Reenter the load that displays on the phone.

No Default Router

DHCP or static configuration did not specify a default router.

If the phone has a
                                                   						static IP address, verify that the default router is configured.

If you are using
                                                   						DHCP, the DHCP server has not provided a default router. Check the DHCP server
                                                   						configuration.

No IPv4 DNS Server

A name was specified but DHCP or static IP configuration did
                                                   					 not specify a IPv4 DNS server address.

If the phone has a
                                                   						static IP address, verify that the IPv4 DNS server is configured.

If you are using
                                                   						DHCP, the DHCP server has not provided a IPv4 DNS server. Check the DHCP server
                                                   						configuration.

No IPv6 DNS Server

A name was specified but DHCP or static IP configuration did
                                                   					 not specify a IPv6 DNS server address.

If the phone has a
                                                   						static IP address, verify that the IPv6 DNS server is configured.

If you are using
                                                   						DHCP, the DHCP server has not provided a IPv6 DNS server. Check the DHCP server
                                                   						configuration.

No Trust List Installed

The CTL file or the ITL file is not installed on the phone.

The trust list is not configured on the Cisco Unified
                                                   					 Communications Manager, which does not support security by default.

The trust list is not configured.

For more information about trust lists, see the documentation for your particular Cisco Unified Communications Manager release.

Phone failed to register. Cert key size is not FIPS compliant.

FIPS requires that the RSA server certificate is 2048 bits or greater.

Update the  certificate.

Restart requested by Cisco Unified Communications Manager

The phone is restarting due to a request from Cisco Unified
                                                   					 Communications Manager.

Configuration changes were likely made to the phone in Cisco
                                                   					 Unified Communications Manager, and Apply Config was pressed so that the changes take
                                                   					 effect.

TFTP Access Error

TFTP server is pointing to a directory that does not exist.

If you are using
                                                   						DHCP, verify that the DHCP server is pointing to the correct TFTP server.

If you are using
                                                   						static IP addresses, check configuration of TFTP server.

TFTP Error

The phone does not recognize an error code that the
                                                   					 TFTP server provided.

Contact Cisco TAC.

TFTP Timeout

TFTP server did not respond.

Network is
                                                   						busy: The errors should resolve themselves when the network load reduces.

No network
                                                   						connectivity between the TFTP server and the phone: Verify the network
                                                   						connections.

TFTP server is
                                                   						down: Check configuration of TFTP server.

Timed Out

Supplicant attempted 802.1X transaction but timed out to due
                                                   					 the absence of an authenticator.

Authentication typically times out if 802.1X is not configured
                                                   					 on the switch.

Trust List Update Failed

Update of the CTL and ITL files failed.

Phone has CTL and ITL files installed and it failed to update
                                                   					 the new CTL and ITL files.

Possible reasons for failure:

- Network failure occurred.

- TFTP server was
                                                      						down.

- The new security
                                                      						token that was used to sign CTL file and the TFTP certificate that was used to sign ITL file are
                                                      						introduced, but are not available in the current CTL and ITL files in the
                                                      						phone.

- Internal phone
                                                      						failure occurred.

Possible solutions:

- Check network
                                                      						connectivity.

- Check whether the TFTP
                                                      						server is active and functioning normally.

- If the
                                                      						Transactional Vsam Services (TVS) server is supported on Cisco Unified
                                                      						Communications Manager, check whether the TVS server is active and functioning
                                                      						normally.

- Verify whether the
                                                      						security token and the TFTP server are valid.

Manually delete the CTL and ITL files if all the preceding
                                                   					 solutions fail; reset the phone.

For more information about trust lists, see the documentation for your particular Cisco Unified Communications Manager release.

Trust List Updated

The CTL file, the ITL file, or both files are updated.

None. This message is informational only.

For more information about trust lists, see the documentation for your particular Cisco Unified Communications Manager release.

Version Error

The name of the phone load file is incorrect.

Make sure that the phone load file has the correct name.

XmlDefault.cnf.xml, or .cnf.xml corresponding to the phone
                                                   					 device name

Name of the configuration file.

None. This message indicates the name of the configuration
                                                   					 file for the phone.

#### Display the Network Statistics Window

Step 1

Press Settings > Status > Network Statistics .

Step 2

To exit the menu, press Back .

##### Network Statistics Fields

The following table describes the information in the Network Statistics screen.

Item

Description

Tx Frames

Number of
                                                   					 packets sent by the phone

Tx
                                                   					 broadcast

Number of
                                                   					 broadcast packets sent by the phone

Tx unicast

Total
                                                   					 number of unicast packets transmitted by the phone

Rx Frames

Number of
                                                   					 packets received by the phone

Rx
                                                   					 broadcast

Number of
                                                   					 broadcast packets received by the phone

Rx unicast

Total
                                                   					 number of unicast packets received by the phone

CDP Neighbor
                                                   					 Device ID

Identifier
                                                   					 of a device connected to this port discovered by CDP protocol.

CDP Neighbor IP Address

Identifier
                                                   					 of a device connected to this port discovered by CDP protocol using IP.

CDP Neighbor Port

Identifier
                                                   					 of a device connected to this port discovered by CDP protocol.

Restart
                                                   					 Cause: One of these values:

Hardware Reset (Power-on
                                                         						reset)

Software Reset (memory
                                                         						controller also reset)

Software Reset (memory
                                                         						controller not reset)

Watchdog Reset

Initialized

Unknown

Cause of
                                                   					 the last reset of the phone

Port 1

Link state
                                                   					 and connection of the network port (for example, 100 Full means that the PC port is in
                                                   					 a link-up state and has auto-negotiated a full-duplex, 100-Mbps connection)

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

- DHCP WAITING COLDBOOT
                                                      						TIMEOUT

- DISABLED DUPLICATE IP

- SET DHCP COLDBOOT

- SET DHCP DISABLED

- SET DHCP FAST

IPv6

CDP INIT

DHCP6 BOUND

DHCP6 DISABLED

DHCP6 RENEW

DHCP6 REBIND

DHCP6 INIT

DHCP6 SOLICIT

DHCP6 REQUEST

DHCP6 RELEASING

DHCP6 RELEASED

DHCP6 DISABLING

DHCP6 DECLINING

DHCP6 DECLINED

DHCP6 INFOREQ

DHCP6 INFOREQ DONE

DHCP6 INVALID

DISABLED DUPLICATE IPV6

DHCP6 DECLINED DUPLICATE IP

ROUTER ADVERTISE

DHCP6 WAITING COLDBOOT TIMEOUT

DHCP6 TIMEOUT USING RESTORED VAL

DHCP6 TIMEOUT CANNOT RESTORE

IPV6 STACK TURNED OFF

ROUTER ADVERTISE

ROUTER ADVERTISE

UNRECOGNIZED MANAGED BY

ILLEGAL IPV6 STATE

#### Display the Call Statistics Window

Step 1

Press Settings > Status > Call Statistics .

Step 2

To exit the menu, press Back .

##### Call Statistics Fields

The following table describes the items on the Call Statistics screen.

Item

Description

Receiver Codec

Type of received voice stream (RTP streaming audio from codec):

G.729

G.722

G.722 AMR WB

G.711 mu-law

G.711 A-law

iLBC

OPUS

iSAC

Sender Codec

Type of transmitted voice stream (RTP streaming audio from codec):

G.729

G.722

G.722 AMR WB

G.711 mu-law

G.711 A-law

iLBC

OPUS

iSAC

Receiver Size

Size of voice packets, in milliseconds, in the receiving voice
                                                   					 stream (RTP streaming audio).

Sender Size

Size of voice packets, in milliseconds, in the transmitting
                                                   					 voice stream.

Rcvr Packets

Number of RTP voice packets that were received since voice stream
                                                   					 opened.

This number is not necessarily identical to the number of
                                                               						RTP voice packets that were received since the call began because the call might have
                                                               						been placed on hold.

Sender Packets

Number of RTP voice packets that were transmitted since voice stream
                                                   					 opened.

This number is not necessarily identical to the number of
                                                               						RTP voice packets that were transmitted since the call began because the call might have
                                                               						been placed on hold.

Avg Jitter

Estimated average RTP packet jitter (dynamic delay that a
                                                   					 packet encounters when going through the network), in milliseconds, that was observed
                                                   					 since the receiving voice stream opened.

Max Jitter

Maximum jitter, in milliseconds, that was observed since the receiving
                                                   					 voice stream opened.

Receiver Discarded

Number of RTP packets in the receiving voice stream that were
                                                   					 discarded (bad packets, too late, and so on).

The phone discards payload type 19 comfort noise packets
                                                               						that  Cisco Gateways generate, because they increment this counter.

Rcvr Lost Packets

Missing RTP packets (lost in transit).

Voice-Quality Metrics

Cumulative Conceal Ratio

Total number of concealment frames divided by total number of
                                                   					 speech frames that were received from start of the voice stream.

Interval Conceal Ratio

Ratio of concealment frames to speech frames in preceding
                                                   					 3-second interval of active speech. If using voice activity detection (VAD), a
                                                   					 longer interval might be required to accumulate 3 seconds of active speech.

Max Conceal Ratio

Highest interval concealment ratio from start of the voice
                                                   					 stream.

Conceal Seconds

Number of seconds that have concealment events (lost frames)
                                                   					 from the start of the voice stream (includes severely concealed seconds).

Severely Conceal Seconds

Number of seconds that have more than 5 percent concealment
                                                   					 events (lost frames) from the start of the voice stream.

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
                                    				Information: Displays device settings and related information for the phone.

Network Setup:
                                    				Displays network setup information and information about other phone settings.

Network
                                    				Statistics: Displays hyperlinks that provide information about network traffic.

Device Logs:
                                    				Displays hyperlinks that provide information that you can use for
                                    				troubleshooting.

Streaming
                                    				Statistic: Displays hyperlinks to a variety of streaming statistics.

This
                              		  section describes the information that you can obtain from the phone web page.
                              		  You can use this information to remotely monitor the operation of a phone and
                              		  to assist with troubleshooting.

You can
                              		  also obtain much of this information directly from a phone.

### Access the Phone Web Page

If you cannot access the web page, it may be disabled by default.

Step 1

Obtain the IP address of the Cisco IP Phone by using one of
                                          			 these methods:

Search for the phone in Cisco Unified Communications Manager
                                                				  Administration by choosing Device > Phone .
                                                				  Phones that register with Cisco Unified Communications Manager display the IP
                                                				  address on the Find and List Phones window and at the top of the Phone
                                                				  Configuration window.

On the phone, press Settings > Admin
                                                      						Settings > Network Setup > IPv4 Setup , and then
                                                				  scroll to the IP Address field.

Step 2

Open a web browser and enter the following URL, where IP_address is the IP address of the Cisco IP Phone:

http:// <IP_address>

### Device Information Web Page

The Device Information area on a phone web page displays device settings and related information for the phone. The following
                                 table describes these items.

To display the Device Information area, access the web page for the phone, and then click the Device Information hyperlink.

Field

Description

Service mode

The service mode for the phone.

Service domain

The domain for the service.

Service state

The current state of the service.

MAC Address

Media Access Control (MAC) address of the phone.

Host Name

Unique, fixed name that is automatically assigned to the phone based on the MAC address.

Phone DN

Directory number that is assigned to the phone.

App Load ID

Identifies the application load version.

Boot Load ID

Indicates the boot load version.

Version

Identifier of the firmware that is running on the phone.

Hardware Revision

Minor revision value of the phone hardware.

Serial Number

Unique serial number of the phone.

Model Number

Model number of the phone.

Message waiting

Indicates whether is a voice message is waiting on the primary line for this phone.

UDI

Displays the following Cisco Unique Device Identifier (UDI) information about the phone:

Hardware type

Phone model name

Product identifier

Version ID (VID)—Specifies the major hardware version number.

Serial number

Time

Time for the Date/Time Group to which the phone belongs. This information comes from Cisco Unified Communications Manager.

Time Zone

Time zone for the Date/Time Group to which the phone belongs. This information comes from Cisco Unified Communications Manager.

Date

Date for the Date/Time Group to which the phone belongs. This information comes from Cisco Unified Communications Manager.

System Free Memory

Amount of available system memory.

Java Heap Free Memory

Amount of free memory for the Java heap.

Java Pool Free Memory

Amount of free memory for the Java pool.

FIPS Mode Enabled

Indicates if the Federal Information processing Standard (FIPS) Mode is enabled.

### Network Setup Web Page

The
                                 		  Network Setup area on a phone web page displays network setup information and
                                 		  information about other phone settings. The following table describes these
                                 		  items.

You can
                                 		  view and set many of these items from the Network Setup menu on the Cisco IP
                                 		  Phone.

To
                                 		  display the Network Setup area, access the web page for the phone, and then
                                 		  click the Network
                                    			 Setup hyperlink.

Item

Description

MAC
                                             					 Address

Media
                                             					 Access Control (MAC) address of the phone.

Host Name

Host name
                                             					 that the DHCP server assigned to the phone.

Domain
                                             					 Name

Name of
                                             					 the Domain Name System (DNS) domain in which the phone resides.

DHCP
                                             					 Server

IP address
                                             					 of the Dynamic Host Configuration Protocol (DHCP) server from which the phone
                                             					 obtains the IP address.

BOOTP
                                             					 Server

Indicates
                                             					 whether the phone obtains the configuration from a Bootstrap Protocol (BootP)
                                             					 server.

DHCP

Indicates whether the phone uses DHCP.

IP Address

Internet
                                             					 Protocol (IP) address of the phone.

Subnet
                                             					 Mask

Subnet
                                             					 mask that the phone uses.

Default
                                             					 Router 1

Default
                                             					 router used that the phone uses.

DNS Server
                                             					 1–3

Primary
                                             					 Domain Name System (DNS) server (DNS Server 1) and optional backup DNS servers
                                             					 (DNS Server 2 and 3) that the phone uses.

Alternate TFTP

Indicates whether the phone is using an alternative TFTP server.

TFTP
                                             					 Server 1

Primary
                                             					 Trivial File Transfer Protocol (TFTP) server used that the phone uses.

TFTP
                                             					 Server 2

Backup
                                             					 Trivial File Transfer Protocol (TFTP) server used that the phone uses.

DHCP
                                             					 Address Released

Indicates the setting of the DHCP Address Released option.

Operational VLAN ID

Operational Virtual Local Area Network (VLAN) that is configured
                                             					 on a Cisco Catalyst switch in which the phone is a member.

Admin
                                             					 VLAN ID

Auxiliary
                                             					 VLAN in which the phone is a member.

Unified CM 1-5

Host names
                                             					 or IP addresses, in prioritized order, of the Cisco Unified Communications
                                             					 Manager servers with which the phone can register. An item can also show the IP
                                             					 address of an SRST router that is capable of providing limited Cisco Unified
                                             					 Communications Manager functionality, if such a router is available.

For an
                                             					 available server, an item shows the Cisco Unified Communications Manager server
                                             					 IP address and one of the following states:

Active: Cisco Unified Communications Manager server from which the phone is currently receiving call-processing services

Standby: Cisco Unified Communications Manager server to which the phone switches if the current server becomes unavailable

Blank: No current connection to this Cisco Unified Communications Manager server

An item
                                             					 may also include the Survivable Remote Site Telephony (SRST) designation, which
                                             					 identifies an SRST router capable of providing Cisco Unified Communications
                                             					 Manager functionality with a limited feature set. This router assumes control
                                             					 of call processing if all other Cisco Unified Communications Manager servers
                                             					 become unreachable. The SRST Cisco Unified Communications Manager always
                                             					 appears last in the list of servers, even if it is active. You configure the
                                             					 SRST router address in the Device Pool section in Cisco Unified Communications
                                             					 Manager Configuration window.

Information URL

URL of the
                                             					 help text that appears on the phone.

Directories URL

URL of the
                                             					 server from which the phone obtains directory information.

Messages
                                             					 URL

URL of
                                             					 the server from which the phone obtains message services.

Services
                                             					 URL

URL of
                                             					 the server from which the phone obtains Cisco IP Phone services.

Idle URL

URL that
                                             					 the phone displays when the phone is idle for the time that the Idle URL Time
                                             					 field specifies and no menu is open.

Idle URL
                                             					 Time

Number
                                             					 of seconds that the phone is idle and no menu is open before the XML service
                                             					 that the Idle URL specifies activates.

Proxy
                                             					 Server URL

URL of
                                             					 proxy server, which makes HTTP requests to nonlocal host addresses on behalf of
                                             					 the phone HTTP client and provides responses from the nonlocal host to the
                                             					 phone HTTP client.

Authentication URL

URL that
                                             					 the phone uses to validate requests that are made to the phone web server.

SW Port
                                             					 Setup

Speed
                                             					 and duplex of the switch port, where:

A = Auto Negotiate

10H = 10-BaseT/half duplex

10F = 10-BaseT/full duplex

100H = 100-BaseT/half duplex

100F = 100-BaseT/full duplex

1000F = 1000-BaseT/full duplex

No Link= No connection to the switch port

User
                                             					 Locale

User
                                             					 locale that associates with the phone user. Identifies a set of detailed
                                             					 information to support users, including language, font, date and time
                                             					 formatting, and alphanumeric keyboard text information.

Network
                                             					 Locale

Network
                                             					 locale that associates with the phone user. Identifies a set of detailed
                                             					 information to support the phone in a specific location, including definitions
                                             					 of the tones and cadences that the phone uses.

User
                                             					 Locale Version

Version
                                             					 of the user locale that is loaded on the phone.

Network
                                             					 Locale Version

Version
                                             					 of the network locale that is loaded on the phone.

Speaker
                                             					 Enabled

Indicates whether the speakerphone is enabled on the phone.

Group Listen

Indicates whether the group listen feature is enabled on the phone.  Group listen enables you to talk using the handset and
                                             listen on the speaker at the same time.

GARP
                                             					 Enabled

Indicates whether the phone learns MAC addresses from Gratuitous
                                             					 ARP responses.

Auto Line Select Enabled

Indicates whether the phone shifts the call focus to incoming
                                             					 calls on all lines.

DSCP for
                                             					 Call Control

DSCP IP
                                             					 classification for call control signaling.

DSCP for
                                             					 Configuration

DSCP IP
                                             					 classification for any phone configuration transfer.

DSCP for
                                             					 Services

DSCP IP
                                             					 classification for phone-based services.

Security
                                             					 Mode

Security
                                             					 mode that is set for the phone.

Web
                                             					 Access Enabled

Indicates whether web access is enabled (Yes) or disabled (No)
                                             					 for the phone.

SSH
                                             					 Access Enabled

Indicates whether the phone accepts or blocks the SSH connections.

CDP:
                                             					 SW Port

Indicates whether CDP support exists on the switch port (default
                                             					 is enabled).

Enable
                                             					 CDP on the switch port for VLAN assignment for the phone, power negotiation,
                                             					 QoS management, and 802.1x security.

Enable
                                             					 CDP on the switch port when the phone connects to a Cisco switch.

When CDP
                                             					 is disabled in Cisco Unified Communications Manager, a warning is presented,
                                             					 indicating that CDP should be disabled on the switch port only if the phone
                                             					 connects to a non-Cisco switch.

The
                                             					 current PC and switch port CDP values are shown on the Settings menu.

LLDP-MED: SW Port

Indicates whether Link Layer Discovery Protocol Media Endpoint
                                             					 Discovery (LLDP-MED) is enabled on the switch port.

LLDP
                                             					 Power Priority

Advertises the phone power priority to the switch, thus enabling
                                             					 the switch to appropriately provide power to the phones. Settings include:

Unknown: This is the default value.

Low

High

Critical

LLDP
                                             					 Asset ID

Identifies the asset ID that is assigned to the phone for
                                             					 inventory management.

CTL File

Identifies the CTL file.

ITL File

The ITL file contains the initial trust list.

ITL Signature

Enhances security by using the secure hash algorithm (SHA-1) in the CTL and ITL files.

CAPF Server

The name of the CAPF server used by the phone.

TVS

The main component of Security by Default. Trust Verification Services (TVS) enables Cisco Unified IP Phones to authenticate
                                             application servers, such as EM services, directory, and MIDlet, during HTTPS establishment.

TFTP Server

The name of the TFTP Server used by the phone.

Automatic Port Synchronization

Synchronizes the ports to the lower speed which eliminates
                                             					 packet loss.

Switch
                                             					 Port Remote Configuration

Allows
                                             					 the administrator to configure the speed and function of the Cisco Desktop
                                             					 Collaboration Experience table port remotely by using Cisco Unified
                                             					 Communications Manager Administration.

IP
                                             					 Addressing Mode

Displays the IP addressing mode that is available on the phone.

IP
                                             					 Preference Mode Control

Indicates the IP address version that the phone uses during signaling with
                                             					 Cisco Unified Communications Manager when both IPv4 and IPv6 are both available
                                             					 on the phone.

IP
                                             					 Preference Mode For Media

Indicates that for media  the device uses an IPv4 address to connect to the Cisco Unified Communications Manager.

IPv6
                                             					 Auto Configuration

Displays whether the auto configuration is enabled or disabled on the phone.

IPv6 DAD

Verifies the uniqueness of new unicast IPv6 addresses before the addresses are assigned to interfaces.

IPv6 Accept Redirect Message

Indicates if  the phone accepts the redirect messages from the same router that is used for the destination number.

IPv6 Reply Multicast Echo Request

Indicates that the phone sends an Echo Reply message in response to an Echo Request message sent to an IPv6 address.

IPv6
                                             					 Load Server

Used to
                                             					 optimize installation time for phone firmware upgrades and off load the WAN by
                                             					 storing images locally, negating the need to traverse the WAN link for each
                                             					 phone's upgrade.

IPv6 Log
                                             					 Server

Indicates the IP address and port of the remote logging machine
                                             					 to which the phone sends log messages.

IPv6
                                             					 CAPF Server

Common
                                             					 Name (from the Cisco Unified Communications Manager Certificate) of the CAPF
                                             					 used by the phone.

DHCPv6

Dynamic
                                             					 Host Configuration Protocol (DHCP) automatically assigns IPv6 address to
                                             					 devices when you connect them to the network. Cisco Unified IP Phones enable
                                             					 DHCP by default.

IPv6
                                             					 Address

Displays
                                             					 the current IPv6 address of the phone or allows the user to enter a new IPv6
                                             					 address.

IPv6
                                             					 Prefix Length

Displays
                                             					 the current prefix length for the subnet or allows the user to enter a new
                                             					 prefix length.

IPv6
                                             					 Default Router 1

Displays
                                             					 the default router used by the phone or allows the user to enter a new IPv6
                                             					 default router.

IPv6 DNS
                                             					 Server 1

Displays
                                             					 the primary DNSv6 server used by the phone or allows the user to enter a new
                                             					 server.

IPv6 DNS
                                             					 Server 2

Displays
                                             					 the secondary DNSv6 server used by the phone or allows the user to set a new
                                             					 secondary DNSv6 server.

IPv6
                                             					 Alternate TFTP

Allows
                                             					 the user to enable the use of an alternate (secondary) IPv6 TFTP server.

IPv6
                                             					 TFTP Server 1

Displays
                                             					 the primary IPv6 TFTP server used by the phone or allows the user to set a new
                                             					 primary TFTP server.

IPv6
                                             					 TFTP Server 2

Displays
                                             					 the secondary IPv6 TFTP server used if the primary IPv6 TFTP server is
                                             					 unavailable or allows the user to set a new secondary TFTP server.

IPv6
                                             					 Address Released

Allows
                                             					 the user to release IPv6-related information.

Energywise Power Level

A
                                             					 measure of the energy consumed by devices in an EnergyWise network.

Energywise Domain

An
                                             					 administrative grouping of devices for the purpose of power monitoring and
                                             					 control.

### Ethernet Information Web Page

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

### Network Web Pages

The
                                 		  following table describes the information in the Network Area
                                 		  web pages.

When you click the Network link under Network statistics, the page is titled "Port Information" .

Item

Description

Rx
                                             					 totalPkt

Total
                                             					 number of packets that the phone received.

Rx
                                             					 multicast

Total
                                             					 number of multicast packets that the phone received.

Rx
                                             					 broadcast

Total
                                             					 number of broadcast packets that the phone received.

Rx unicast

Total
                                             					 number of unicast packets that the phone received.

Rx
                                             					 tokenDrop

Total
                                             					 number of packets that were dropped due to lack of resources (for example, FIFO
                                             					 overflow).

Tx
                                             					 totalGoodPkt

Total
                                             					 number of good packets (multicast, broadcast, and unicast) that the phone
                                             					 received.

Tx
                                             					 broadcast

Total
                                             					 number of broadcast packets that the phone transmitted.

Tx
                                             					 multicast

Total
                                             					 number of multicast packets that the phone transmitted.

LLDP
                                             					 FramesOutTotal

Total
                                             					 number of LLDP frames that the phone sent out.

LLDP
                                             					 AgeoutsTotal

Total
                                             					 number of LLDP frames that timed out in the cache.

LLDP
                                             					 FramesDiscardedTotal

Total
                                             					 number of LLDP frames that were discarded when any of the mandatory TLVs is
                                             					 missing, out of order, or contains out of range string length.

LLDP
                                             					 FramesInErrorsTotal

Total
                                             					 number of LLDP frames that were received with one or more detectable errors.

LLDP
                                             					 FramesInTotal

Total
                                             					 number of LLDP frames that the phone receives.

LLDP
                                             					 TLVDiscardedTotal

Total
                                             					 number of LLDP TLVs that are discarded.

LLDP
                                             					 TLVUnrecognizedTotal

Total
                                             					 number of LLDP TLVs that are not recognized on the phone.

CDP
                                             					 Neighbor Device ID

Identifier of a device connected to this port that CDP
                                             					 discovered.

CDP
                                             					 Neighbor IP Address

IP
                                             					 address of the neighbor device discovered that CDP discovered.

CDP Neighbor IPv6 Address

IPv6 address of the neighbor device discovered that CDP
                                             					 discovered.

CDP
                                             					 Neighbor Port

Neighbor
                                             					 device port to which the phone is connected that CDP discovered.

LLDP
                                             					 Neighbor Device ID

Identifier of a device connected to this port that LLDP discovered.

LLDP
                                             					 Neighbor IP Address

IP
                                             					 address of the neighbor device that LLDP discovered.

LLDP Neighbor IPv6 Address

IPv6 address of the neighbor device that CDP
                                             					 discovered.

LLDP
                                             					 Neighbor Port

Neighbor
                                             					 device port to which the phone connects that LLDP discovered.

Port
                                             					 Information

Speed
                                             					 and duplex information.

### Console Logs, Core Dumps, Status Messages, and Debug Display Web Pages

Under the Device Logs heading, the Console Logs, Core Dumps, Status Messages, and Debug Display hyperlinks provide
                                 information that helps to monitor and troubleshoot the phone.

Console Logs—Includes hyperlinks to individual log files. The
                                       console log files include debug and error messages that the phone
                                       received.

Core Dumps—Includes hyperlinks to individual dump files. The
                                       core dump files include data from a phone crash.

Status Messages—Displays the 10 most recent status messages
                                       that the phone has generated since it last powered up. You can also get this information from the Status
                                       Messages screen on the phone.

Debug Display—Displays debug messages that might be useful to
                                       Cisco TAC if you require assistance with troubleshooting.

### Streaming Statistics Web Page

A Cisco IP Phone can stream information to and from up to five devices  simultaneously. A phone streams information when it
                                 is on a call or is running a service that sends or receives audio or data.

The Streaming statistics areas on a phone web page provide information about the streams.

To display a Streaming Statistics area, access the web page for the phone, and then click a Stream hyperlink.

The following table describes the items in the Streaming Statistics areas.

Item

Description

Remote Address

IP address and UDP port of the destination of the stream.

Local Address

IP address and UPD port of the phone.

Start Time

Internal time stamp indicates when Cisco Unified Communications Manager requested that the phone start transmitting packets.

Stream Status

Indication of whether streaming is active or not.

Host Name

Unique, fixed name that is automatically assigned to the phone based on the MAC address.

Sender Packets

Total number of RTP data packets that the phone transmitted since it started this connection. The value is 0 if the connection
                                             is set to receive-only mode.

Sender Octets

Total number of payload octets that the phone transmitted in RTP data packets since it started this connection. The value
                                             is 0 if the connection is set to receive-only mode.

Sender Codec

Type of audio encoding that is for the transmitted stream.

Sender Reports Sent

(see note)

Number of times the RTCP Sender Report has been sent.

Sender Report Time Sent

(see note)

Internal time-stamp indication as to when the last RTCP Sender Report was sent.

Rcvr Lost Packets

Total number of RTP data packets that have been lost since data reception started on this connection. Defined as the number
                                             of expected packets less the number of packets actually received, where the number of received packets includes any that are
                                             late or are duplicates. The value displays as 0 if the connection was set to send-only mode.

Avg Jitter

Estimate of mean deviation of the RTP data packet interarrival time, measured in milliseconds. The value displays as 0 if
                                             the connection was set to send-only mode.

Receiver Codec

Type of audio encoding that is used for the received stream.

Receiver Reports Sent

(see note)

Number of times the RTCP Receiver Reports have been sent.

Receiver Report Time Sent

(see note)

Internal time-stamp indication as to when a RTCP Receiver Report was sent.

Rcvr Packets

Total number of RTP data packets that the phone has received since data reception started on this connection. Includes packets
                                             that were received from different sources if this call is a multicast call. The value displays as 0 if the connection was
                                             set to send-only mode.

Rcvr Octets

Total number of payload octets that the device received in RTP data packets since reception started on the connection. Includes
                                             packets that were received from different sources if this call is a multicast call. The value displays as 0 if the connection
                                             was set to send-only mode.

Cumulative Conceal Ratio

Total number of concealment frames divided by total number of speech frames that were received from the start of the voice
                                             stream.

Interval Conceal Ratio

Ratio of concealment frames to speech frames in the preceding 3-second interval of active speech. If  voice activity detection
                                             (VAD) is in use, a longer interval might be required to accumulate three seconds of active speech.

Max Conceal Ratio

Highest interval concealment ratio from the start of the voice stream.

Conceal Seconds

Number of seconds that have concealment events (lost frames) from the start of the voice stream (includes severely concealed
                                             seconds).

Severely Conceal Seconds

Number of seconds that have more than five percent concealment events (lost frames) from the start of the voice stream.

Latency

(see note)

Estimate of the network latency, expressed in milliseconds. Represents a running average of the round-trip delay, measured
                                             when RTCP receiver report blocks are received.

Max Jitter

Maximum value of instantaneous jitter, in milliseconds.

Sender Size

RTP packet size, in milliseconds, for the transmitted stream.

Sender Reports Received

(see note)

Number of times RTCP Sender Reports have been received.

Sender Report Time Received

(see note)

Most recent time when an RTCP Sender Report was received.

Receiver Size

RTP packet size, in milliseconds, for the received stream.

Receiver Discarded

RTP packets that were received from the network but were discarded from the jitter buffers.

Receiver Reports Received

(see note)

Number of times RTCP Receiver Reports have been received.

Receiver Report Time Received

(see note)

Most recent time when an RTCP Receiver Report was received.

When the RTP Control Protocol is disabled, no data generates for this field and thus displays as 0.

## Request
                        	 Information from the Phone in XML

For
                              		  troubleshooting purposes, you can request information from the phone. The
                              		  resulting information is in XML format. The following information is available:

CallInfo is
                                    				call session information for a specific line.

LineInfo is
                                    				line configuration information for the phone.

ModeInfo is
                                    				phone mode information.

### Before you begin

Web access needs
                              		  to be enabled to get the information.

The phone must be
                              		  associated with a user.

Step 1

For Call Info,
                                       			 enter the following URL in a browser: http://<phone ip
                                          				address>/CGI/Java/CallInfo<x>

where

<phone
                                                   						ip address> is the IP address of the phone

<x> is the line number to obtain information about.

The command
                                          				returns an XML document.

Step 2

For Line Info,
                                       			 enter the following URL in a browser: http://<phone ip address>/CGI/Java/LineInfo

where

<phone
                                                   						ip address> is the IP address of the phone

The command
                                          				returns an XML document.

Step 3

For Model
                                       			 Info, enter the following URL in a browser: http://<phone ip address>/CGI/Java/ModeInfo

where

<phone
                                                   						ip address> is the IP address of the phone

The command
                                          				returns an XML document.

### Sample CallInfo
                           	 Output

The following XML
                                 		  code is an example of the output from the CallInfo command.

```
<?xml version="1.0" encoding="UTF-8"?>
<CiscoIPPhoneCallLineInfo>
  <Prompt/>
	 <Notify/>
	 <Status/>
	 <LineDirNum>1030</LineDirNum>
	 <LineState>CONNECTED</LineState>
	 <CiscoIPPhoneCallInfo>
		   <CallState>CONNECTED</CallState>
		   <CallType>INBOUND</CallType>
		   <CallingPartyName/>
		   <CallingPartyDirNum>9700</CallingPartyDirNum>
	   	<CalledPartyName/>
		   <CalledPartyDirNum>1030</CalledPartyDirNum>
		   <HuntPilotName/>
		   <CallReference>30303060</CallReference>
		   <CallDuration>12835</CallDuration>
	   	<CallStatus>null</CallStatus>
	   	<CallSecurity>UNAUTHENTICATED</CallSecurity>
		   <CallPrecedence>ROUTINE</CallPrecedence>
		   <FeatureList/>
  	</CiscoIPPhoneCallInfo>
  	<VisibleFeatureList>
	   	<Feature Position="1" Enabled="true" Label="End Call"/>
	   	<Feature Position="2" Enabled="true" Label="Show Detail"/>
  	</VisibleFeatureList>
</CiscoIPPhoneCallLineInfo>
```

### Sample LineInfo
                           	 Output

The following XML
                                 		  code is an example of the output from the LineInfo command.

```
<CiscoIPPhoneLineInfo>
	  <Prompt/>
  	<Notify/>
  	<Status>null</Status>
	  <CiscoIPPhoneLines>
	   	<LineType>9</LineType>
		   <lineDirNum>1028</lineDirNum>
	   	<MessageWaiting>NO</MessageWaiting>
	   	<RingerName>Chirp1</RingerName>
	   	<LineLabel/>
	   	<LineIconState>ONHOOK</LineIconState>
  	</CiscoIPPhoneLines>
  	<CiscoIPPhoneLines>
	   	<LineType>9</LineType>
	   	<lineDirNum>1029</lineDirNum>
   		<MessageWaiting>NO</MessageWaiting>		<RingerName>Chirp1</RingerName>
	   	<LineLabel/>
   		<LineIconState>ONHOOK</LineIconState>
  	</CiscoIPPhoneLines>
	  <CiscoIPPhoneLines>
	   	<LineType>9</LineType>
	   	<lineDirNum>1030</lineDirNum>
	   	<MessageWaiting>NO</MessageWaiting>
	   	<RingerName>Chirp1</RingerName>
	   	<LineLabel/>
	   	<LineIconState>CONNECTED</LineIconState>
	  </CiscoIPPhoneLines>
  	<CiscoIPPhoneLines>
   		<LineType>2</LineType>
   		<lineDirNum>9700</lineDirNum>
   		<MessageWaiting>NO</MessageWaiting>
   		<LineLabel>SD9700</LineLabel>
   		<LineIconState>ON</LineIconState>
 	</CiscoIPPhoneLines>
</CiscoIPPhoneLineInfo>
```

### Sample ModeInfo
                           	 Output

The following XML
                                 		  code is an example of the output from the ModeInfo command.

```
<?xml version="1.0" encoding="utf-8"?>
<CiscoIPPhoneModeInfo>
   <PlaneTitle>Applications</PlaneTitle>
   <PlaneFieldCount>12</PlaneFieldCount>
   <PlaneSoftKeyIndex>0</PlaneSoftKeyIndex>
   <PlaneSoftKeyMask>0</PlaneSoftKeyMask>
   <Prompt></Prompt>
   <Notify></Notify>
   <Status></Status>
   <CiscoIPPhoneFields>
      <FieldType>0</FieldType>
      <FieldAttr></FieldAttr>
      <fieldHelpIndex>0</fieldHelpIndex>
      <FieldName>Call History</FieldName>
      <FieldValue></FieldValue>
   </CiscoIPPhoneFields>
   <CiscoIPPhoneFields>
      <FieldType>0</FieldType>
      <FieldAttr></FieldAttr>
      <fieldHelpIndex>0</fieldHelpIndex>
      <FieldName>Preferences</FieldName>
      <FieldValue></FieldValue>
   </CiscoIPPhoneFields>
   ...
</CiscoIPPhoneModeInfo>
```

| Step 1 | Press Settings > Phone information . |
|---|---|
| Step 2 | To exit the menu, press Exit . |

| Step 1 | Press Settings > Status . |
|---|---|
| Step 2 | To exit the menu, press Back . |

| Step 1 | Press Settings > Status > Status Messages . |
|---|---|
| Step 2 | To exit the menu, press Back . |

| Message | Description | Possible Explanation and Action |
|---|---|---|
| Could not acquire an IP address from DHCP | The phone has not previously obtained an IP
                                                   address from a DHCP Server. This can occur when you perform an out of box or factory
                                                   reset. | Confirm that the DHCP server is available and that an IP address is available  for the phone. |
| TFTP Size Error | The configuration file is too large for file system on the
                                                   					 phone. | Power cycle the phone. |
| ROM Checksum Error | Downloaded software file is corrupted. | Obtain a new copy of the phone firmware and place it in the
                                                   					 TFTPPath directory. You should only copy files into this directory when the
                                                   					 TFTP server software is shut down; otherwise, the files may be corrupted. |
| Duplicate IP | Another device is using the IP address that is assigned to the phone. | If the phone has a
                                                   						static IP address, verify that you did not assigned a duplicate IP address. If you are using
                                                   						DHCP, check the DHCP server configuration. |
| Erasing CTL and ITL files | Erasing CTL or ITL file. | None. This message is informational only. |
| Error Updating Locale | One or more localization files could not be found in the
                                                   					 TFTP Path directory or were not valid. The locale was not changed. | From Cisco Unified Operating System Administration, check that
                                                   					 the following files are located within subdirectories in the TFTP File
                                                   					 Management: Located in
                                                      						subdirectory with same name as network locale: tones.xml Located in
                                                      						subdirectory with same name as user locale: glyphs.xml dictionary.xml kate.xml |
| File not found <Cfg File> | The name-based and default configuration file was not found on
                                                   					 the TFTP Server. | The configuration file for a phone is created when the phone
                                                   					 is added to the Cisco Unified Communications Manager database. If the phone
                                                   					 does not exist in the Cisco Unified Communications Manager database, the TFTP
                                                   					 server generates a CFG File Not Found response. Phone is not
                                                         						registered with Cisco Unified Communications Manager. You must manually add the phone to Cisco Unified
                                                         						  Communications Manager if you are not allowing phones to autoregister. If you are using
                                                         						DHCP, verify that the DHCP server is pointing to the correct TFTP server. If you are using
                                                         						static IP addresses, check configuration of the TFTP server. |
| File Not Found <CTLFile.tlv> | This message displays on the phone when the Cisco Unified
                                                   					 Communications Manager cluster is not in secure mode. | No impact; the phone can still register to Cisco Unified
                                                   					 Communications Manager. |
| IP Address Released | The phone is configured to release the IP address. | The phone remains idle until it is power cycled or until you reset
                                                   					 the DHCP address. |
| IPv4 DHCP Timeout | IPv4 DHCP server did not respond. | Network is
                                                   						busy: The errors should resolve themselves when the network load reduces. No network
                                                   						connectivity between the IPv4 DHCP server and the phone: Verify the network
                                                   						connections. IPv4 DHCP server is
                                                   						down: Check configuration of IPv4 DHCP server. Errors
                                                   						persist: Consider assigning a static IPv4 address. |
| IPv6 DHCP Timeout | IPv6 DHCP server did not respond. | Network is
                                                   						busy - The errors should resolve themselves when the network load reduces. No network
                                                   						connectivity between the IPv6 DHCP server and the phone: Verify the network
                                                   						connections. IPv6 DHCP server is
                                                   						down: Check configuration of IPv6 DHCP server. Errors
                                                   						persist: Consider assigning a static IPv6 address. |
| IPv4 DNS Timeout | IPv4 DNS server did not respond. | Network is
                                                   						busy: The errors should resolve themselves when the network load reduces. No network
                                                   						connectivity between the IPv4 DNS server and the phone: Verify the network
                                                   						connections. IPv4 DNS server is
                                                   						down: Check configuration of the IPv4 DNS server. |
| IPv6 DNS Timeout | IPv6 DNS server did not respond. | Network is
                                                   						busy: The errors should resolve themselves when the network load reduces. No network
                                                   						connectivity between the IPv6 DNS server and the phone: Verify the network
                                                   						connections. IPv6 DNS server is
                                                   						down: Check configuration of the IPv6 DNS server. |
| DNS unknown IPv4 Host | IPv4 DNS could not resolve the name of the TFTP server or Cisco
                                                   					 Unified Communications Manager. | Verify that the
                                                   						host names of the TFTP server or Cisco Unified Communications Manager are
                                                   						configured properly in IPv4 DNS. Consider using IPv4
                                                   						addresses rather than host names |
| DNS unknown IPv6 Host | IPv6 DNS could not resolve the name of the TFTP server or Cisco
                                                   					 Unified Communications Manager. | Verify that the
                                                   						host names of the TFTP server or Cisco Unified Communications Manager are
                                                   						configured properly in IPv6 DNS. Consider using IPv6
                                                   						addresses rather than host names |
| Load Rejected HC | The application that was downloaded is not compatible with the
                                                   					 phone hardware. | Occurs if you attempt to install a version of software
                                                   					 on this phone that did not support hardware changes on this  phone. Check the load ID that is assigned to the phone (from Cisco Unified
                                                   					 Communications Manager, choose Device > Phone ).
                                                   					 Reenter the load that displays on the phone. |
| No Default Router | DHCP or static configuration did not specify a default router. | If the phone has a
                                                   						static IP address, verify that the default router is configured. If you are using
                                                   						DHCP, the DHCP server has not provided a default router. Check the DHCP server
                                                   						configuration. |
| No IPv4 DNS Server | A name was specified but DHCP or static IP configuration did
                                                   					 not specify a IPv4 DNS server address. | If the phone has a
                                                   						static IP address, verify that the IPv4 DNS server is configured. If you are using
                                                   						DHCP, the DHCP server has not provided a IPv4 DNS server. Check the DHCP server
                                                   						configuration. |
| No IPv6 DNS Server | A name was specified but DHCP or static IP configuration did
                                                   					 not specify a IPv6 DNS server address. | If the phone has a
                                                   						static IP address, verify that the IPv6 DNS server is configured. If you are using
                                                   						DHCP, the DHCP server has not provided a IPv6 DNS server. Check the DHCP server
                                                   						configuration. |
| No Trust List Installed | The CTL file or the ITL file is not installed on the phone. | The trust list is not configured on the Cisco Unified
                                                   					 Communications Manager, which does not support security by default. The trust list is not configured. For more information about trust lists, see the documentation for your particular Cisco Unified Communications Manager release. |
| Phone failed to register. Cert key size is not FIPS compliant. | FIPS requires that the RSA server certificate is 2048 bits or greater. | Update the  certificate. |
| Restart requested by Cisco Unified Communications Manager | The phone is restarting due to a request from Cisco Unified
                                                   					 Communications Manager. | Configuration changes were likely made to the phone in Cisco
                                                   					 Unified Communications Manager, and Apply Config was pressed so that the changes take
                                                   					 effect. |
| TFTP Access Error | TFTP server is pointing to a directory that does not exist. | If you are using
                                                   						DHCP, verify that the DHCP server is pointing to the correct TFTP server. If you are using
                                                   						static IP addresses, check configuration of TFTP server. |
| TFTP Error | The phone does not recognize an error code that the
                                                   					 TFTP server provided. | Contact Cisco TAC. |
| TFTP Timeout | TFTP server did not respond. | Network is
                                                   						busy: The errors should resolve themselves when the network load reduces. No network
                                                   						connectivity between the TFTP server and the phone: Verify the network
                                                   						connections. TFTP server is
                                                   						down: Check configuration of TFTP server. |
| Timed Out | Supplicant attempted 802.1X transaction but timed out to due
                                                   					 the absence of an authenticator. | Authentication typically times out if 802.1X is not configured
                                                   					 on the switch. |
| Trust List Update Failed | Update of the CTL and ITL files failed. | Phone has CTL and ITL files installed and it failed to update
                                                   					 the new CTL and ITL files. Possible reasons for failure: Network failure occurred. TFTP server was
                                                      						down. The new security
                                                      						token that was used to sign CTL file and the TFTP certificate that was used to sign ITL file are
                                                      						introduced, but are not available in the current CTL and ITL files in the
                                                      						phone. Internal phone
                                                      						failure occurred. Possible solutions: Check network
                                                      						connectivity. Check whether the TFTP
                                                      						server is active and functioning normally. If the
                                                      						Transactional Vsam Services (TVS) server is supported on Cisco Unified
                                                      						Communications Manager, check whether the TVS server is active and functioning
                                                      						normally. Verify whether the
                                                      						security token and the TFTP server are valid. Manually delete the CTL and ITL files if all the preceding
                                                   					 solutions fail; reset the phone. For more information about trust lists, see the documentation for your particular Cisco Unified Communications Manager release. |
| Trust List Updated | The CTL file, the ITL file, or both files are updated. | None. This message is informational only. For more information about trust lists, see the documentation for your particular Cisco Unified Communications Manager release. |
| Version Error | The name of the phone load file is incorrect. | Make sure that the phone load file has the correct name. |
| XmlDefault.cnf.xml, or .cnf.xml corresponding to the phone
                                                   					 device name | Name of the configuration file. | None. This message indicates the name of the configuration
                                                   					 file for the phone. |

| Step 1 | Press Settings > Status > Network Statistics . |
|---|---|
| Step 2 | To exit the menu, press Back . |

| Item | Description |
|---|---|
| Tx Frames | Number of
                                                   					 packets sent by the phone |
| Tx
                                                   					 broadcast | Number of
                                                   					 broadcast packets sent by the phone |
| Tx unicast | Total
                                                   					 number of unicast packets transmitted by the phone |
| Rx Frames | Number of
                                                   					 packets received by the phone |
| Rx
                                                   					 broadcast | Number of
                                                   					 broadcast packets received by the phone |
| Rx unicast | Total
                                                   					 number of unicast packets received by the phone |
| CDP Neighbor
                                                   					 Device ID | Identifier
                                                   					 of a device connected to this port discovered by CDP protocol. |
| CDP Neighbor IP Address | Identifier
                                                   					 of a device connected to this port discovered by CDP protocol using IP. |
| CDP Neighbor Port | Identifier
                                                   					 of a device connected to this port discovered by CDP protocol. |
| Restart
                                                   					 Cause: One of these values: Hardware Reset (Power-on
                                                         						reset) Software Reset (memory
                                                         						controller also reset) Software Reset (memory
                                                         						controller not reset) Watchdog Reset Initialized Unknown | Cause of
                                                   					 the last reset of the phone |
| Port 1 | Link state
                                                   					 and connection of the network port (for example, 100 Full means that the PC port is in
                                                   					 a link-up state and has auto-negotiated a full-duplex, 100-Mbps connection) |
| IPv4 | Information on the DHCP status. This includes the following
                                                   					 states: CDP BOUND CDP INIT DHCP BOUND DHCP DISABLED DHCP INIT DHCP INVALID DHCP REBINDING DHCP REBOOT DHCP RENEWING DHCP REQUESTING DHCP RESYNC DHCP UNRECOGNIZED DHCP WAITING COLDBOOT
                                                      						TIMEOUT DISABLED DUPLICATE IP SET DHCP COLDBOOT SET DHCP DISABLED SET DHCP FAST |
| IPv6 | Information on the DHCP status. This includes the following
                                                   					 states: CDP INIT DHCP6 BOUND DHCP6 DISABLED DHCP6 RENEW DHCP6 REBIND DHCP6 INIT DHCP6 SOLICIT DHCP6 REQUEST DHCP6 RELEASING DHCP6 RELEASED DHCP6 DISABLING DHCP6 DECLINING DHCP6 DECLINED DHCP6 INFOREQ DHCP6 INFOREQ DONE DHCP6 INVALID DISABLED DUPLICATE IPV6 DHCP6 DECLINED DUPLICATE IP ROUTER ADVERTISE DHCP6 WAITING COLDBOOT TIMEOUT DHCP6 TIMEOUT USING RESTORED VAL DHCP6 TIMEOUT CANNOT RESTORE IPV6 STACK TURNED OFF ROUTER ADVERTISE ROUTER ADVERTISE UNRECOGNIZED MANAGED BY ILLEGAL IPV6 STATE |

| Step 1 | Press Settings > Status > Call Statistics . |
|---|---|
| Step 2 | To exit the menu, press Back . |

| Item | Description |
|---|---|
| Receiver Codec | Type of received voice stream (RTP streaming audio from codec): G.729 G.722 G.722 AMR WB G.711 mu-law G.711 A-law iLBC OPUS iSAC |
| Sender Codec | Type of transmitted voice stream (RTP streaming audio from codec): G.729 G.722 G.722 AMR WB G.711 mu-law G.711 A-law iLBC OPUS iSAC |
| Receiver Size | Size of voice packets, in milliseconds, in the receiving voice
                                                   					 stream (RTP streaming audio). |
| Sender Size | Size of voice packets, in milliseconds, in the transmitting
                                                   					 voice stream. |
| Rcvr Packets | Number of RTP voice packets that were received since voice stream
                                                   					 opened. Note This number is not necessarily identical to the number of
                                                               						RTP voice packets that were received since the call began because the call might have
                                                               						been placed on hold. | Note | This number is not necessarily identical to the number of
                                                               						RTP voice packets that were received since the call began because the call might have
                                                               						been placed on hold. |
| Note | This number is not necessarily identical to the number of
                                                               						RTP voice packets that were received since the call began because the call might have
                                                               						been placed on hold. |
| Sender Packets | Number of RTP voice packets that were transmitted since voice stream
                                                   					 opened. Note This number is not necessarily identical to the number of
                                                               						RTP voice packets that were transmitted since the call began because the call might have
                                                               						been placed on hold. | Note | This number is not necessarily identical to the number of
                                                               						RTP voice packets that were transmitted since the call began because the call might have
                                                               						been placed on hold. |
| Note | This number is not necessarily identical to the number of
                                                               						RTP voice packets that were transmitted since the call began because the call might have
                                                               						been placed on hold. |
| Avg Jitter | Estimated average RTP packet jitter (dynamic delay that a
                                                   					 packet encounters when going through the network), in milliseconds, that was observed
                                                   					 since the receiving voice stream opened. |
| Max Jitter | Maximum jitter, in milliseconds, that was observed since the receiving
                                                   					 voice stream opened. |
| Receiver Discarded | Number of RTP packets in the receiving voice stream that were
                                                   					 discarded (bad packets, too late, and so on). Note The phone discards payload type 19 comfort noise packets
                                                               						that  Cisco Gateways generate, because they increment this counter. | Note | The phone discards payload type 19 comfort noise packets
                                                               						that  Cisco Gateways generate, because they increment this counter. |
| Note | The phone discards payload type 19 comfort noise packets
                                                               						that  Cisco Gateways generate, because they increment this counter. |
| Rcvr Lost Packets | Missing RTP packets (lost in transit). |
| Voice-Quality Metrics |
| Cumulative Conceal Ratio | Total number of concealment frames divided by total number of
                                                   					 speech frames that were received from start of the voice stream. |
| Interval Conceal Ratio | Ratio of concealment frames to speech frames in preceding
                                                   					 3-second interval of active speech. If using voice activity detection (VAD), a
                                                   					 longer interval might be required to accumulate 3 seconds of active speech. |
| Max Conceal Ratio | Highest interval concealment ratio from start of the voice
                                                   					 stream. |
| Conceal Seconds | Number of seconds that have concealment events (lost frames)
                                                   					 from the start of the voice stream (includes severely concealed seconds). |
| Severely Conceal Seconds | Number of seconds that have more than 5 percent concealment
                                                   					 events (lost frames) from the start of the voice stream. |
| Latency | Estimate of the network latency, expressed in milliseconds.
                                                   					 Represents a running average of the round-trip delay, measured when RTCP
                                                   					 receiver report blocks are received. |

| Note | This number is not necessarily identical to the number of
                                                               						RTP voice packets that were received since the call began because the call might have
                                                               						been placed on hold. |
|---|---|

| Note | This number is not necessarily identical to the number of
                                                               						RTP voice packets that were transmitted since the call began because the call might have
                                                               						been placed on hold. |
|---|---|

| Note | The phone discards payload type 19 comfort noise packets
                                                               						that  Cisco Gateways generate, because they increment this counter. |
|---|---|

| Note | If you cannot access the web page, it may be disabled by default. |
|---|---|

| Step 1 | Obtain the IP address of the Cisco IP Phone by using one of
                                          			 these methods: Search for the phone in Cisco Unified Communications Manager
                                                				  Administration by choosing Device > Phone .
                                                				  Phones that register with Cisco Unified Communications Manager display the IP
                                                				  address on the Find and List Phones window and at the top of the Phone
                                                				  Configuration window. On the phone, press Settings > Admin
                                                      						Settings > Network Setup > IPv4 Setup , and then
                                                				  scroll to the IP Address field. |
|---|---|
| Step 2 | Open a web browser and enter the following URL, where IP_address is the IP address of the Cisco IP Phone: http:// <IP_address> |

| Field | Description |
|---|---|
| Service mode | The service mode for the phone. |
| Service domain | The domain for the service. |
| Service state | The current state of the service. |
| MAC Address | Media Access Control (MAC) address of the phone. |
| Host Name | Unique, fixed name that is automatically assigned to the phone based on the MAC address. |
| Phone DN | Directory number that is assigned to the phone. |
| App Load ID | Identifies the application load version. |
| Boot Load ID | Indicates the boot load version. |
| Version | Identifier of the firmware that is running on the phone. |
| Hardware Revision | Minor revision value of the phone hardware. |
| Serial Number | Unique serial number of the phone. |
| Model Number | Model number of the phone. |
| Message waiting | Indicates whether is a voice message is waiting on the primary line for this phone. |
| UDI | Displays the following Cisco Unique Device Identifier (UDI) information about the phone: Hardware type Phone model name Product identifier Version ID (VID)—Specifies the major hardware version number. Serial number |
| Time | Time for the Date/Time Group to which the phone belongs. This information comes from Cisco Unified Communications Manager. |
| Time Zone | Time zone for the Date/Time Group to which the phone belongs. This information comes from Cisco Unified Communications Manager. |
| Date | Date for the Date/Time Group to which the phone belongs. This information comes from Cisco Unified Communications Manager. |
| System Free Memory | Amount of available system memory. |
| Java Heap Free Memory | Amount of free memory for the Java heap. |
| Java Pool Free Memory | Amount of free memory for the Java pool. |
| FIPS Mode Enabled | Indicates if the Federal Information processing Standard (FIPS) Mode is enabled. |

| Item | Description |
|---|---|
| MAC
                                             					 Address | Media
                                             					 Access Control (MAC) address of the phone. |
| Host Name | Host name
                                             					 that the DHCP server assigned to the phone. |
| Domain
                                             					 Name | Name of
                                             					 the Domain Name System (DNS) domain in which the phone resides. |
| DHCP
                                             					 Server | IP address
                                             					 of the Dynamic Host Configuration Protocol (DHCP) server from which the phone
                                             					 obtains the IP address. |
| BOOTP
                                             					 Server | Indicates
                                             					 whether the phone obtains the configuration from a Bootstrap Protocol (BootP)
                                             					 server. |
| DHCP | Indicates whether the phone uses DHCP. |
| IP Address | Internet
                                             					 Protocol (IP) address of the phone. |
| Subnet
                                             					 Mask | Subnet
                                             					 mask that the phone uses. |
| Default
                                             					 Router 1 | Default
                                             					 router used that the phone uses. |
| DNS Server
                                             					 1–3 | Primary
                                             					 Domain Name System (DNS) server (DNS Server 1) and optional backup DNS servers
                                             					 (DNS Server 2 and 3) that the phone uses. |
| Alternate TFTP | Indicates whether the phone is using an alternative TFTP server. |
| TFTP
                                             					 Server 1 | Primary
                                             					 Trivial File Transfer Protocol (TFTP) server used that the phone uses. |
| TFTP
                                             					 Server 2 | Backup
                                             					 Trivial File Transfer Protocol (TFTP) server used that the phone uses. |
| DHCP
                                             					 Address Released | Indicates the setting of the DHCP Address Released option. |
| Operational VLAN ID | Operational Virtual Local Area Network (VLAN) that is configured
                                             					 on a Cisco Catalyst switch in which the phone is a member. |
| Admin
                                             					 VLAN ID | Auxiliary
                                             					 VLAN in which the phone is a member. |
| Unified CM 1-5 | Host names
                                             					 or IP addresses, in prioritized order, of the Cisco Unified Communications
                                             					 Manager servers with which the phone can register. An item can also show the IP
                                             					 address of an SRST router that is capable of providing limited Cisco Unified
                                             					 Communications Manager functionality, if such a router is available. For an
                                             					 available server, an item shows the Cisco Unified Communications Manager server
                                             					 IP address and one of the following states: Active: Cisco Unified Communications Manager server from which the phone is currently receiving call-processing services Standby: Cisco Unified Communications Manager server to which the phone switches if the current server becomes unavailable Blank: No current connection to this Cisco Unified Communications Manager server An item
                                             					 may also include the Survivable Remote Site Telephony (SRST) designation, which
                                             					 identifies an SRST router capable of providing Cisco Unified Communications
                                             					 Manager functionality with a limited feature set. This router assumes control
                                             					 of call processing if all other Cisco Unified Communications Manager servers
                                             					 become unreachable. The SRST Cisco Unified Communications Manager always
                                             					 appears last in the list of servers, even if it is active. You configure the
                                             					 SRST router address in the Device Pool section in Cisco Unified Communications
                                             					 Manager Configuration window. |
| Information URL | URL of the
                                             					 help text that appears on the phone. |
| Directories URL | URL of the
                                             					 server from which the phone obtains directory information. |
| Messages
                                             					 URL | URL of
                                             					 the server from which the phone obtains message services. |
| Services
                                             					 URL | URL of
                                             					 the server from which the phone obtains Cisco IP Phone services. |
| Idle URL | URL that
                                             					 the phone displays when the phone is idle for the time that the Idle URL Time
                                             					 field specifies and no menu is open. |
| Idle URL
                                             					 Time | Number
                                             					 of seconds that the phone is idle and no menu is open before the XML service
                                             					 that the Idle URL specifies activates. |
| Proxy
                                             					 Server URL | URL of
                                             					 proxy server, which makes HTTP requests to nonlocal host addresses on behalf of
                                             					 the phone HTTP client and provides responses from the nonlocal host to the
                                             					 phone HTTP client. |
| Authentication URL | URL that
                                             					 the phone uses to validate requests that are made to the phone web server. |
| SW Port
                                             					 Setup | Speed
                                             					 and duplex of the switch port, where: A = Auto Negotiate 10H = 10-BaseT/half duplex 10F = 10-BaseT/full duplex 100H = 100-BaseT/half duplex 100F = 100-BaseT/full duplex 1000F = 1000-BaseT/full duplex No Link= No connection to the switch port |
| User
                                             					 Locale | User
                                             					 locale that associates with the phone user. Identifies a set of detailed
                                             					 information to support users, including language, font, date and time
                                             					 formatting, and alphanumeric keyboard text information. |
| Network
                                             					 Locale | Network
                                             					 locale that associates with the phone user. Identifies a set of detailed
                                             					 information to support the phone in a specific location, including definitions
                                             					 of the tones and cadences that the phone uses. |
| User
                                             					 Locale Version | Version
                                             					 of the user locale that is loaded on the phone. |
| Network
                                             					 Locale Version | Version
                                             					 of the network locale that is loaded on the phone. |
| Speaker
                                             					 Enabled | Indicates whether the speakerphone is enabled on the phone. |
| Group Listen | Indicates whether the group listen feature is enabled on the phone.  Group listen enables you to talk using the handset and
                                             listen on the speaker at the same time. |
| GARP
                                             					 Enabled | Indicates whether the phone learns MAC addresses from Gratuitous
                                             					 ARP responses. |
| Auto Line Select Enabled | Indicates whether the phone shifts the call focus to incoming
                                             					 calls on all lines. |
| DSCP for
                                             					 Call Control | DSCP IP
                                             					 classification for call control signaling. |
| DSCP for
                                             					 Configuration | DSCP IP
                                             					 classification for any phone configuration transfer. |
| DSCP for
                                             					 Services | DSCP IP
                                             					 classification for phone-based services. |
| Security
                                             					 Mode | Security
                                             					 mode that is set for the phone. |
| Web
                                             					 Access Enabled | Indicates whether web access is enabled (Yes) or disabled (No)
                                             					 for the phone. |
| SSH
                                             					 Access Enabled | Indicates whether the phone accepts or blocks the SSH connections. |
| CDP:
                                             					 SW Port | Indicates whether CDP support exists on the switch port (default
                                             					 is enabled). Enable
                                             					 CDP on the switch port for VLAN assignment for the phone, power negotiation,
                                             					 QoS management, and 802.1x security. Enable
                                             					 CDP on the switch port when the phone connects to a Cisco switch. When CDP
                                             					 is disabled in Cisco Unified Communications Manager, a warning is presented,
                                             					 indicating that CDP should be disabled on the switch port only if the phone
                                             					 connects to a non-Cisco switch. The
                                             					 current PC and switch port CDP values are shown on the Settings menu. |
| LLDP-MED: SW Port | Indicates whether Link Layer Discovery Protocol Media Endpoint
                                             					 Discovery (LLDP-MED) is enabled on the switch port. |
| LLDP
                                             					 Power Priority | Advertises the phone power priority to the switch, thus enabling
                                             					 the switch to appropriately provide power to the phones. Settings include: Unknown: This is the default value. Low High Critical |
| LLDP
                                             					 Asset ID | Identifies the asset ID that is assigned to the phone for
                                             					 inventory management. |
| CTL File | Identifies the CTL file. |
| ITL File | The ITL file contains the initial trust list. |
| ITL Signature | Enhances security by using the secure hash algorithm (SHA-1) in the CTL and ITL files. |
| CAPF Server | The name of the CAPF server used by the phone. |
| TVS | The main component of Security by Default. Trust Verification Services (TVS) enables Cisco Unified IP Phones to authenticate
                                             application servers, such as EM services, directory, and MIDlet, during HTTPS establishment. |
| TFTP Server | The name of the TFTP Server used by the phone. |
| Automatic Port Synchronization | Synchronizes the ports to the lower speed which eliminates
                                             					 packet loss. |
| Switch
                                             					 Port Remote Configuration | Allows
                                             					 the administrator to configure the speed and function of the Cisco Desktop
                                             					 Collaboration Experience table port remotely by using Cisco Unified
                                             					 Communications Manager Administration. |
| IP
                                             					 Addressing Mode | Displays the IP addressing mode that is available on the phone. |
| IP
                                             					 Preference Mode Control | Indicates the IP address version that the phone uses during signaling with
                                             					 Cisco Unified Communications Manager when both IPv4 and IPv6 are both available
                                             					 on the phone. |
| IP
                                             					 Preference Mode For Media | Indicates that for media  the device uses an IPv4 address to connect to the Cisco Unified Communications Manager. |
| IPv6
                                             					 Auto Configuration | Displays whether the auto configuration is enabled or disabled on the phone. |
| IPv6 DAD | Verifies the uniqueness of new unicast IPv6 addresses before the addresses are assigned to interfaces. |
| IPv6 Accept Redirect Message | Indicates if  the phone accepts the redirect messages from the same router that is used for the destination number. |
| IPv6 Reply Multicast Echo Request | Indicates that the phone sends an Echo Reply message in response to an Echo Request message sent to an IPv6 address. |
| IPv6
                                             					 Load Server | Used to
                                             					 optimize installation time for phone firmware upgrades and off load the WAN by
                                             					 storing images locally, negating the need to traverse the WAN link for each
                                             					 phone's upgrade. |
| IPv6 Log
                                             					 Server | Indicates the IP address and port of the remote logging machine
                                             					 to which the phone sends log messages. |
| IPv6
                                             					 CAPF Server | Common
                                             					 Name (from the Cisco Unified Communications Manager Certificate) of the CAPF
                                             					 used by the phone. |
| DHCPv6 | Dynamic
                                             					 Host Configuration Protocol (DHCP) automatically assigns IPv6 address to
                                             					 devices when you connect them to the network. Cisco Unified IP Phones enable
                                             					 DHCP by default. |
| IPv6
                                             					 Address | Displays
                                             					 the current IPv6 address of the phone or allows the user to enter a new IPv6
                                             					 address. |
| IPv6
                                             					 Prefix Length | Displays
                                             					 the current prefix length for the subnet or allows the user to enter a new
                                             					 prefix length. |
| IPv6
                                             					 Default Router 1 | Displays
                                             					 the default router used by the phone or allows the user to enter a new IPv6
                                             					 default router. |
| IPv6 DNS
                                             					 Server 1 | Displays
                                             					 the primary DNSv6 server used by the phone or allows the user to enter a new
                                             					 server. |
| IPv6 DNS
                                             					 Server 2 | Displays
                                             					 the secondary DNSv6 server used by the phone or allows the user to set a new
                                             					 secondary DNSv6 server. |
| IPv6
                                             					 Alternate TFTP | Allows
                                             					 the user to enable the use of an alternate (secondary) IPv6 TFTP server. |
| IPv6
                                             					 TFTP Server 1 | Displays
                                             					 the primary IPv6 TFTP server used by the phone or allows the user to set a new
                                             					 primary TFTP server. |
| IPv6
                                             					 TFTP Server 2 | Displays
                                             					 the secondary IPv6 TFTP server used if the primary IPv6 TFTP server is
                                             					 unavailable or allows the user to set a new secondary TFTP server. |
| IPv6
                                             					 Address Released | Allows
                                             					 the user to release IPv6-related information. |
| Energywise Power Level | A
                                             					 measure of the energy consumed by devices in an EnergyWise network. |
| Energywise Domain | An
                                             					 administrative grouping of devices for the purpose of power monitoring and
                                             					 control. |

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

| Note | When you click the Network link under Network statistics, the page is titled "Port Information" . |
|---|---|

| Item | Description |
|---|---|
| Rx
                                             					 totalPkt | Total
                                             					 number of packets that the phone received. |
| Rx
                                             					 multicast | Total
                                             					 number of multicast packets that the phone received. |
| Rx
                                             					 broadcast | Total
                                             					 number of broadcast packets that the phone received. |
| Rx unicast | Total
                                             					 number of unicast packets that the phone received. |
| Rx
                                             					 tokenDrop | Total
                                             					 number of packets that were dropped due to lack of resources (for example, FIFO
                                             					 overflow). |
| Tx
                                             					 totalGoodPkt | Total
                                             					 number of good packets (multicast, broadcast, and unicast) that the phone
                                             					 received. |
| Tx
                                             					 broadcast | Total
                                             					 number of broadcast packets that the phone transmitted. |
| Tx
                                             					 multicast | Total
                                             					 number of multicast packets that the phone transmitted. |
| LLDP
                                             					 FramesOutTotal | Total
                                             					 number of LLDP frames that the phone sent out. |
| LLDP
                                             					 AgeoutsTotal | Total
                                             					 number of LLDP frames that timed out in the cache. |
| LLDP
                                             					 FramesDiscardedTotal | Total
                                             					 number of LLDP frames that were discarded when any of the mandatory TLVs is
                                             					 missing, out of order, or contains out of range string length. |
| LLDP
                                             					 FramesInErrorsTotal | Total
                                             					 number of LLDP frames that were received with one or more detectable errors. |
| LLDP
                                             					 FramesInTotal | Total
                                             					 number of LLDP frames that the phone receives. |
| LLDP
                                             					 TLVDiscardedTotal | Total
                                             					 number of LLDP TLVs that are discarded. |
| LLDP
                                             					 TLVUnrecognizedTotal | Total
                                             					 number of LLDP TLVs that are not recognized on the phone. |
| CDP
                                             					 Neighbor Device ID | Identifier of a device connected to this port that CDP
                                             					 discovered. |
| CDP
                                             					 Neighbor IP Address | IP
                                             					 address of the neighbor device discovered that CDP discovered. |
| CDP Neighbor IPv6 Address | IPv6 address of the neighbor device discovered that CDP
                                             					 discovered. |
| CDP
                                             					 Neighbor Port | Neighbor
                                             					 device port to which the phone is connected that CDP discovered. |
| LLDP
                                             					 Neighbor Device ID | Identifier of a device connected to this port that LLDP discovered. |
| LLDP
                                             					 Neighbor IP Address | IP
                                             					 address of the neighbor device that LLDP discovered. |
| LLDP Neighbor IPv6 Address | IPv6 address of the neighbor device that CDP
                                             					 discovered. |
| LLDP
                                             					 Neighbor Port | Neighbor
                                             					 device port to which the phone connects that LLDP discovered. |
| Port
                                             					 Information | Speed
                                             					 and duplex information. |

| Item | Description |
|---|---|
| Remote Address | IP address and UDP port of the destination of the stream. |
| Local Address | IP address and UPD port of the phone. |
| Start Time | Internal time stamp indicates when Cisco Unified Communications Manager requested that the phone start transmitting packets. |
| Stream Status | Indication of whether streaming is active or not. |
| Host Name | Unique, fixed name that is automatically assigned to the phone based on the MAC address. |
| Sender Packets | Total number of RTP data packets that the phone transmitted since it started this connection. The value is 0 if the connection
                                             is set to receive-only mode. |
| Sender Octets | Total number of payload octets that the phone transmitted in RTP data packets since it started this connection. The value
                                             is 0 if the connection is set to receive-only mode. |
| Sender Codec | Type of audio encoding that is for the transmitted stream. |
| Sender Reports Sent (see note) | Number of times the RTCP Sender Report has been sent. |
| Sender Report Time Sent (see note) | Internal time-stamp indication as to when the last RTCP Sender Report was sent. |
| Rcvr Lost Packets | Total number of RTP data packets that have been lost since data reception started on this connection. Defined as the number
                                             of expected packets less the number of packets actually received, where the number of received packets includes any that are
                                             late or are duplicates. The value displays as 0 if the connection was set to send-only mode. |
| Avg Jitter | Estimate of mean deviation of the RTP data packet interarrival time, measured in milliseconds. The value displays as 0 if
                                             the connection was set to send-only mode. |
| Receiver Codec | Type of audio encoding that is used for the received stream. |
| Receiver Reports Sent (see note) | Number of times the RTCP Receiver Reports have been sent. |
| Receiver Report Time Sent (see note) | Internal time-stamp indication as to when a RTCP Receiver Report was sent. |
| Rcvr Packets | Total number of RTP data packets that the phone has received since data reception started on this connection. Includes packets
                                             that were received from different sources if this call is a multicast call. The value displays as 0 if the connection was
                                             set to send-only mode. |
| Rcvr Octets | Total number of payload octets that the device received in RTP data packets since reception started on the connection. Includes
                                             packets that were received from different sources if this call is a multicast call. The value displays as 0 if the connection
                                             was set to send-only mode. |
| Cumulative Conceal Ratio | Total number of concealment frames divided by total number of speech frames that were received from the start of the voice
                                             stream. |
| Interval Conceal Ratio | Ratio of concealment frames to speech frames in the preceding 3-second interval of active speech. If  voice activity detection
                                             (VAD) is in use, a longer interval might be required to accumulate three seconds of active speech. |
| Max Conceal Ratio | Highest interval concealment ratio from the start of the voice stream. |
| Conceal Seconds | Number of seconds that have concealment events (lost frames) from the start of the voice stream (includes severely concealed
                                             seconds). |
| Severely Conceal Seconds | Number of seconds that have more than five percent concealment events (lost frames) from the start of the voice stream. |
| Latency (see note) | Estimate of the network latency, expressed in milliseconds. Represents a running average of the round-trip delay, measured
                                             when RTCP receiver report blocks are received. |
| Max Jitter | Maximum value of instantaneous jitter, in milliseconds. |
| Sender Size | RTP packet size, in milliseconds, for the transmitted stream. |
| Sender Reports Received (see note) | Number of times RTCP Sender Reports have been received. |
| Sender Report Time Received (see note) | Most recent time when an RTCP Sender Report was received. |
| Receiver Size | RTP packet size, in milliseconds, for the received stream. |
| Receiver Discarded | RTP packets that were received from the network but were discarded from the jitter buffers. |
| Receiver Reports Received (see note) | Number of times RTCP Receiver Reports have been received. |
| Receiver Report Time Received (see note) | Most recent time when an RTCP Receiver Report was received. |

| Note | When the RTP Control Protocol is disabled, no data generates for this field and thus displays as 0. |
|---|---|

| Step 1 | For Call Info,
                                       			 enter the following URL in a browser: http://<phone ip
                                          				address>/CGI/Java/CallInfo<x> where <phone
                                                   						ip address> is the IP address of the phone <x> is the line number to obtain information about. The command
                                          				returns an XML document. |
|---|---|
| Step 2 | For Line Info,
                                       			 enter the following URL in a browser: http://<phone ip address>/CGI/Java/LineInfo where <phone
                                                   						ip address> is the IP address of the phone The command
                                          				returns an XML document. |
| Step 3 | For Model
                                       			 Info, enter the following URL in a browser: http://<phone ip address>/CGI/Java/ModeInfo where <phone
                                                   						ip address> is the IP address of the phone The command
                                          				returns an XML document. |