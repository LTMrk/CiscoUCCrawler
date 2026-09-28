---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-english-adminguide-p881-bk-c136782f-00-cisco-ip-phone-880-477119d474
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/english/adminguide/P881_BK_C136782F_00_cisco-ip-phone-8800_series/P881_BK_C136782F_00_cisco-ip-phone-8811-8841_chapter_01101.html
retrieved_at: 2026-08-21T09:49:28.624759+00:00
---

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

# Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

Updated: November 6, 2025

Chapter: Monitoring Phone Systems

## Chapter: Monitoring Phone Systems

# Monitoring Phone Systems

## Cisco IP Phone
                        	 Status

This section describes how to view model information, status messages, and network statistics on the Cisco IP Phone 8800 series.

Model
                                    				Information: Displays hardware and software information about the phone.

Status menu:
                                    				Provides access to screens that display the status messages, network
                                    				statistics, and statistics for the current call.

You can
                              		  use the information that displays on these screens to monitor the operation of
                              		  a phone and to assist with troubleshooting.

You can
                              		  also obtain much of this information, and obtain other related information,
                              		  remotely through the phone web page.

For more information about
                              		  troubleshooting, see Troubleshooting .

### Display Phone Information Window

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

To exit the Model Information screen, press Exit .

#### Phone Information Fields

The following table describes the phone information settings.

Option

Description

Model number

Model number of the phone.

IPv4 Address

IP address of the phone.

Host name

Host name of the phone.

Active load

Version of firmware currently installed on the phone. The user
                                                					 can press Details for more information.

Inactive load

Inactive load appears only when a download is in progress. A
                                                					 download icon and a status of "Upgrade in Progress" or "Upgrade Failed" also display. If a user presses Details during an upgrade, the download filename and
                                                					 components are listed.

A new firmware image can be set to download in advance of a
                                                					 maintenance window. Thus instead of waiting for all of the phones to download
                                                					 the firmware, the system switches more rapidly between resetting an existing
                                                					 load to Inactive status and installing the new load.

When the download is complete, the icon changes to indicate
                                                					 the completed status; and a check mark displays for a successful download, or
                                                					 an "X" displays for a failed download. If possible, the rest
                                                					 of the loads continue to download.

Last upgrade

Date of the most recent firmware upgrade.

Active server

Domain name of the server to which the phone is registered.

Stand-by server

Domain name of the standby server.

### Display Status
                           	 Menu

The
                                 		  Status menu includes the following options, which provide information about the
                                 		  phone and phone operations:

Status
                                       				Messages: Displays the Status Messages screen, which shows a log of important
                                       				system messages.

Ethernet
                                       				Statistic: Displays the Ethernet Statistics screen, which shows Ethernet
                                       				traffic statistics.

Wireless
                                       				Statistics: Displays the Wireless Statistics screen, if applicable.

Call
                                       				Statistics: Displays counters and statistics for the current call.

Current Access
                                       				Point: Displays the Current Access Point screen, if applicable.

To
                                 		  display the Status menu, perform these steps:

Step 1

To display the Status menu, press Applications .

Step 2

Select Admin
                                                				  settings > Status .

Step 3

To exit the
                                          			 Status menu, press Exit .

#### Display Status
                              	 Messages Window

The Status
                                    		  Messages window displays the 30 most recent status messages that the phone has
                                    		  generated. You can access this screen at any time, even if the phone has not
                                    		  finished starting up.

Step 1

Press Applications .

Step 2

Select Admin
                                                   				  settings > Status > Status
                                                   				  messages .

Step 3

To remove the
                                             			 current status messages, press Clear .

Step 4

To exit the
                                             			 Status Messages screen, press Exit .

##### Status Messages
                                 	 Fields

The following table describes the status messages that display on the Status Messages screen of the phone.

Message

Description

Possible explanation and action

CFG TFTP Size Error

The configuration file is too large for file system on the phone.

Power cycle the phone.

Checksum Error

Downloaded software file is corrupted.

Obtain a new copy of the phone firmware and place it in the TFTPPath directory. You should only copy files into this directory
                                                   when the TFTP server software is shut down; otherwise, the files may be corrupted.

Could not acquire an IP address from DHCP

The phone has not previously obtained an IP address from a DHCP Server. This can occur when you perform an out of box or factory
                                                   reset.

Confirm that the DHCP server is available and that an IP address is available for the phone.

CTL and ITL installed

The CTL and ITL files are installed on the phone.

None. This message is informational only. Neither the CTL file nor the ITL file was installed previously.

CTL Installed

A certificate trust list (CTL) file is installed in the phone.

None. This message is informational only. The CTL file was not installed previously.

CTL update failed

The phone could not update the certificate trust list (CTL) file.

Problem with the CTL file on the TFTP server.

DHCP timeout

DHCP server did not respond.

Network is busy: The errors should resolve themselves when the network load reduces.

No network connectivity between the DHCP server and the phone: Verify the network connections.

DHCP server is down: Check configuration of DHCP server.

Errors persist: Consider assigning a static IP address.

DNS timeout

DNS server did not respond.

Network is busy: The errors should resolve themselves when the network load reduces.

No network connectivity between the DNS server and the phone: Verify the network connections.

DNS server is down: Check configuration of the DNS server.

DNS unknown host

DNS could not resolve the name of the TFTP server or Cisco Unified Communications Manager.

Verify that the host names of the TFTP server or Cisco Unified Communications Manager are configured properly in DNS.

Consider using IP addresses rather than host names

Duplicate IP

Another device is using the IP address that is assigned to the phone.

If the phone has a static IP address, verify that you did not assigned a duplicate IP address.

If you are using DHCP, check the DHCP server configuration.

Erasing CTL and ITL files

Erasing CTL or ITL file.

None. This message is informational only.

Error update locale

One or more localization files could not be found in the TFTPPath directory or were not valid. The locale was not changed.

From Cisco Unified Operating System Administration, check that the following files are located within subdirectories in the
                                                   TFTP File Management:

tones.xml

glyphs.xml

dictionary.xml

kate.xml

File not found <Cfg File>

The name-based and default configuration file was not found on the TFTP Server.

The configuration file for a phone is created when the phone is added to the Cisco Unified Communications Manager database.
                                                   If the phone does not exist in the Cisco Unified Communications Manager database, the TFTP server generates a CFG File Not Found response.

You must manually add the phone to Cisco Unified Communications Manager if you are not allowing phones to autoregister. See Phone Addition Methods for details.

- If you are using DHCP, verify that the DHCP server is pointing to the correct TFTP server.

- If you are using static IP addresses, check configuration of the TFTP server.

File Not Found <CTLFile.tlv>

This message displays on the phone when the Cisco Unified Communications Manager cluster is not in secure mode.

No impact; the phone can still register to Cisco Unified Communications Manager.

IP address released

The phone is configured to release the IP address.

The phone remains idle until it is power cycled or until you reset the DHCP address.

ITL installed

The ITL file is installed in the phone.

None. This message is informational only. The ITL file was not installed previously.

Load rejected HC

The application that was downloaded is not compatible with the phone hardware.

Occurs if you attempted to install a version of software on this phone that did not support hardware changes on this phone.

Check the load ID that is assigned to the phone (from Cisco Unified Communications Manager, choose Device > Phone ). Reenter the load that displays on the phone.

No default router

DHCP or static configuration did not specify a default router.

If the phone has a static IP address, verify that the default router is configured.

If you are using DHCP, the DHCP server has not provided a default router. Check the DHCP server configuration.

No DNS server IP

A name was specified but DHCP or static IP configuration did not specify a DNS server address.

If the phone has a static IP address, verify that the DNS server is configured.

If you are using DHCP, the DHCP server has not provided a DNS server. Check the DHCP server configuration.

No Trust List installed

The CTL file or the ITL file is not installed on the phone.

The trust list is not configured on the Cisco Unified Communications Manager, which does not support security by default.

Phone failed to register. Cert key size is not FIPS compliant.

FIPS requires that the RSA server certificate is 2048 bits or greater.

Update the certificate.

Restart requested by Cisco Unified Communications Manager

The phone is restarting due to on a request from Cisco Unified Communications Manager.

Configuration changes were likely made to the phone in Cisco Unified Communications Manager, and Apply was pressed so that
                                                   the changes take effect.

TFTP access error

TFTP server is pointing to a directory that does not exist.

If you are using DHCP, verify that the DHCP server is pointing to the correct TFTP server.

If you are using static IP addresses, check configuration of TFTP server.

TFTP error

The phone does not recognize an error code that the TFTP server provided.

Contact Cisco TAC.

TFTP timeout

TFTP server did not respond.

Network is bus: The errors should resolve themselves when the network load reduces.

No network connectivity between the TFTP server and the phone: Verify the network connections.

TFTP server is down: Check configuration of TFTP server.

Timed Out

Supplicant attempted 802.1X transaction but timed out to due the absence of an authenticator.

Authentication typically times out if 802.1X is not configured on the switch.

Trust List update failed

Update of the CTL and ITL files failed.

Phone has CTL and ITL files installed and it failed to update the new CTL and ITL files.

Possible reasons for failure:

- Network failure occurred.

- TFTP server was down.

- The new security token that was used to sign CTL file and the TFTP certificate that was used to sign ITL file are introduced,
                                                      but are not available in the current CTL and ITL files in the phone.

- Internal phone failure occurred.

Possible solutions:

- Check network connectivity.

- Check whether the TFTP server is active and functioning normally.

- If the Transactional Vsam Services (TVS) server is supported on Cisco Unified Communications Manager, check whether the TVS
                                                      server is active and functioning normally.

- Verify whether the security token and the TFTP server are valid.

Manually delete the CTL and ITL files if all the preceding solutions fail; reset the phone.

Trust List updated

The CTL file, the ITL file, or both files are updated.

None. This message is informational only.

Version error

The name of the phone load file is incorrect.

Make sure that the phone load file has the correct name.

XmlDefault.cnf.xml, or .cnf.xml corresponding to the phone device name

Name of the configuration file.

None. This message indicates the name of the configuration file for the phone.

#### Display Network Information Screen

Use the information displayed on the Network Info screen to  resolve connection issues on a phone.

A message is displayed on the phone if a user has trouble connecting to a  phone network.

Step 1

To display the Status menu, press Applications .

Step 2

Select Admin
                                                   				  settings > Status > Status messages .

Step 3

Select Network Info .

Step 4

To exit 
                                             			 Network Info, press Exit .

#### Display Network
                              	 Statistics Screen

The
                                    		  Networks Statistics screen displays information about the phone and network
                                    		  performance.

To
                                    		  display the Network Statistics screen, follow these steps:

Step 1

Press Applications .

Step 2

Select Admin
                                                				settings > Status > Network
                                                				statistics .

Step 3

To reset the
                                             			 Rx Frames, Tx Frames, and Rx Broadcasts statistics to 0, press Clear .

Step 4

To exit the
                                             			 Ethernet Statistics screen, press Exit .

##### Ethernet
                                 	 Statistics Information

The following tables describe the information in the Ethernet
                                       		  Statistics screen.

Item

Description

Rx Frames

Number of packets that the phone received.

Tx Frames

Number of packets that the phone sent.

Rx Broadcasts

Number of broadcast packets that the phone received.

Restart Cause

Cause of the last reset of the phone. Specifies one of the
                                                   					 following values:

- Initialized

- TCP-timeout

- CM-closed-TCP

- TCP-Bad-ACK

- CM-reset-TCP

- CM-aborted-TCP

- CM-NAKed

- KeepaliveTO

- Failback

- Phone-Keypad

- Phone-Re-IP

- Reset-Reset

- Reset-Restart

- Phone-Reg-Rej

- Load Rejected HC

- CM-ICMP-Unreach

- Phone-Abort

Elapsed Time

Amount of time that has elapsed since the phone last rebooted.

Port 1

Link state and connection of the Network port. For example, Auto 100 Mb Full-Duplex means that the
                                                   					 Network port is in a link-up state and has autonegotiated a full-duplex,
                                                   					 100-Mbps connection.

Port 2

Link state and connection of the PC port.

DHCP state (IPv4 / IPv6)

In IPv4-only mode, displays only the DHCPv4 state, such as DHCP BOUND.

In IPv6-mode, displays only the DHCPv6 state, such as ROUTER ADVERTISE.

DHCPv6 state information is displayed.

The following tables describe the messages that appear for DHCPv4 and
                                       		  DHCPv6 states.

DHCPv4 state

Description

CDP INIT

CDP is not bound or WLAN is not in service

DHCP BOUND

DHCPv4 is BOUND

DHCP DISABLED

DHCPv4 is disabled

DHCP INIT

DHCPv4 is INIT

DHCP INVALID

DHCPv4 is INVALID; this is initial state

DHCP RENEWING

DHCPv4 is RENEWING

DHCP REBINDING

DHCPv4 is REBINDING

DHCP REBOOT

DHCPv4 is init-reboot

DHCP REQUESTING

DHCPv4 is requesting

DHCP RESYNC

DHCPv4 is RESYNCH

DHCP WAITING COLDBOOT TIMEOUT

DHCPv4 is booting

DHCP UNRECOGNIZED

Unrecognized DHCPv4 state

DISABLED DUPLICATE IP

Duplicated IPv4 Address

DHCP TIMEOUT

DHCPv4 Timeout

IPV4 STACK TURNED OFF

Phone is in IPv6-only mode with IPv4 Stack turned off

ILLEGAL IPV4 STATE

Illegal IPv4 state and should not happen

DHCPv6 State

Description

CDP INIT

CDP is initializing

DHCP6 BOUND

DHCPv6 is BOUND

DHCP6 DISABLED

DHCPv6 is DISABLED

DHCP6 RENEW

DHCPv6 is renewing

DHCP6 REBIND

DHCPv6 is rebinding

DHCP6 INIT

DHCPv6 is initializing

DHCP6 SOLICIT

DHCPv6 is soliciting

DHCP6 REQUEST

DHCPv6 is requesting

DHCP6 RELEASING

DHCPv6 is releasing

DHCP6 RELEASED

DHCPv6 is released

DHCP6 DISABLING

DHCPv6 is disabling

DHCP6 DECLINING

DHCPv6 is declining

DHCP6 DECLINED

DHCPv6 is declined

DHCP6 INFOREQ

DHCPv6 is INFOREQ

DHCP6 INFOREQ DONE

DHCPv6 is INFOREQ DONE

DHCP6 INVALID

DHCPv6 is INVALID; this is initial state

DISABLED DUPLICATE IPV6

DHCP6 is DISABLED, but DUPLICATE IPV6 DETECTED

DHCP6 DECLINED DUPLICATE IP

DHCP6 is DECLINED -- DUPLICATE IPV6 DETECTED

ROUTER ADVERTISE., (DUPLICATE IP)

Duplicated autoconfigured IPv6 address

DHCP6 WAITING COLDBOOT TIMEOUT

DHCPv6 is booting

DHCP6 TIMEOUT USING RESTORED VAL

DHCPv6 timeout, using the value saved in flash memory

DHCP6 TIMEOUT CANNOT RESTORE

DHCP6 timeout and there is no backup from flash memory

IPV6 STACK TURNED OFF

Phone is in IPv4-only mode with IPv6 Stack turned off

ROUTER ADVERTISE., (GOOD IP)

ROUTER ADVERTISE., (BAD IP)

UNRECOGNIZED MANAGED BY

IPv6 Address is not from router or DHCPv6 server

ILLEGAL IPV6 STATE

Illegal IPv6 state and should not happen

#### Display Wireless
                              	 Statistics Screen

This procedure
                                    		  only applies to the wireless Cisco IP Phone 8861.

To
                                    		  display the Wireless Statistics screen, follow these steps:

Step 1

Press Applications .

Step 2

Select Admin
                                                				settings > Status > Wireless Statistics .

Step 3

To reset the
                                             			 Wireless statistics to 0, press Clear .

Step 4

To exit the
                                             			 Wireless Statistics screen, press Exit .

##### WLAN
                                 	 Statistics

The
                                       		  following table describes the WLAN statistics on the phone.

Item

Description

tx bytes

Number of bytes that the phone transmitted.

rx bytes

Number of bytes that the phone received.

tx packets

Number of packets that the phone transmitted.

rx packets

Number of packets that the phone received.

tx packets dropped

The number of packets dropped during transmission.

rx packets dropped

The number of packets dropped during reception.

tx packets errors

The number of erroneous packets that phone transmitted.

rx packets errors

The number of erroneous packets that phone received.

Tx frames

The number of successfully transmitted MSDU.

tx multicast frames

The nunber of successfully transmitted multicast MSDU.

tx retry

The number of MSDU that is successfully transmitted after one
                                                   					 or more retransmissions.

tx multi retry

The number of multicast MSDU that is successfully transmitted
                                                   					 after one or more retransmissions.

tx failure

This number of MSDU that is not transmitted successfully due
                                                   					 to the number of transmit attempts exceeding the retry limit.

rts succeess

This counter shall increment when a CTS is received in
                                                   					 response to an RTS.

rts failure

This counter shall increment when a CTS is not received in
                                                   					 response to an RTS.

ack failure

This counter shall increment when an ACK is not received when
                                                   					 expected.

rx duplicate frames

The number of received frame that the Sequence Control field
                                                   					 indicates is a duplicate.

rx fraagmented packets

The number of successfully received MPDU of type Data or
                                                   					 Management.

Roaming count

The number of succesful roaming.

#### Display Call
                              	 Statistics Window

You can
                                    		  access the Call Statistics screen on the phone to display counters, statistics,
                                    		  and voice-quality metrics of the most recent call.

You can also
                                                			 remotely view the call statistics information by using a web browser to access
                                                			 the Streaming Statistics web page. This web page contains additional RTCP
                                                			 statistics that are not available on the phone.

A single
                                    		  call can use multiple voice streams, but data is captured for only the last
                                    		  voice stream. A voice stream is a packet stream between two endpoints. If one
                                    		  endpoint is put on hold, the voice stream stops even though the call is still
                                    		  connected. When the call resumes, a new voice packet stream begins, and the new
                                    		  call data overwrites the former call data.

Step 1

Press Applications .

Step 2

Select Admin
                                                   				  settings > Status > Call
                                                   				  statistics .

Step 3

To exit the
                                             			 Call Statistics screen, press Exit .

##### Call Statistics
                                 	 Fields

The
                                       		  following table describes the items on the Call Statistics screen.

Item

Description

Receiver
                                                   					 codec

G.729

G.722

G722.2 AMR-WB

G.711 mu-law

G.711 A-law

iLBC

Opus

iSAC

Sender
                                                   					 codec

G.729

G.722

G722.2 AMR-WB

G.711 mu-law

G.711 A-law

iLBC.

Opus

iSAC

Receiver
                                                   					 size

Size of
                                                   					 voice packets, in milliseconds, in the receiving voice stream (RTP streaming
                                                   					 audio).

Sender
                                                   					 size

Size of
                                                   					 voice packets, in milliseconds, in the transmitting voice stream.

Receiver
                                                   					 packets

Number of
                                                   					 RTP voice packets that were received since voice stream opened.

This
                                                               						number is not necessarily identical to the number of RTP voice packets that
                                                               						were received since the call began because the call might have been placed on
                                                               						hold.

Sender
                                                   					 packets

Number of
                                                   					 RTP voice packets that were transmitted since voice stream opened.

This
                                                               						number is not necessarily identical to the number of RTP voice packets that
                                                               						were transmitted since the call began because the call might have been placed
                                                               						on hold.

Avg jitter

Estimated
                                                   					 average RTP packet jitter (dynamic delay that a packet encounters when going
                                                   					 through the network), in milliseconds, that was observed since the receiving
                                                   					 voice stream opened.

Max jitter

Maximum
                                                   					 jitter, in milliseconds, that was observed since the receiving voice stream
                                                   					 opened.

Receiver
                                                   					 discarded

Number of
                                                   					 RTP packets in the receiving voice stream that were discarded (bad packets, too
                                                   					 late, and so on).

The
                                                               						phone discards payload type 19 comfort noise packets that Cisco Gateways
                                                               						generate, because they increment this counter.

Receiver
                                                   					 lost packets

Missing
                                                   					 RTP packets (lost in transit).

Voice-Quality
                                                      						Metrics

Cumulative
                                                   					 conceal ratio

Total
                                                   					 number of concealment frames divided by total number of speech frames that were
                                                   					 received from start of the voice stream.

Interval
                                                   					 conceal ratio

Ratio of
                                                   					 concealment frames to speech frames in preceding 3-second interval of active
                                                   					 speech. If using voice activity detection (VAD), a longer interval might be
                                                   					 required to accumulate 3 seconds of active speech.

Max
                                                   					 conceal ratio

Highest
                                                   					 interval concealment ratio from start of the voice stream.

Conceal
                                                   					 seconds

Number of
                                                   					 seconds that have concealment events (lost frames) from the start of the voice
                                                   					 stream (includes severely concealed seconds).

Severely
                                                   					 conceal seconds

Number
                                                   					 of seconds that have more than 5 percent concealment events (lost frames) from
                                                   					 the start of the voice stream.

Latency

Estimate
                                                   					 of the network latency, expressed in milliseconds. Represents a running average
                                                   					 of the round-trip delay, measured when RTCP receiver report blocks are
                                                   					 received.

#### Display Current
                              	 Access Point Window

The
                                    		  Current Access Point screen displays statistics about the access point that the
                                    		  Cisco IP Phone 8861 uses for wireless communications.

Step 1

Press Applications .

Step 2

Select Admin
                                                   				  settings > Status > Current Access
                                                   				  Point .

Step 3

To exit the
                                             			 Current Access Point screen, press Exit .

##### Current Access
                                 	 Points Fields

The
                                       		  following table describes the fields in the Current Access Point screen.

Item

Description

AP name

Name of
                                                   					 the AP, if it is CCX-compliant; otherwise, the MAC address displays here.

MAC
                                                   					 address

MAC
                                                   					 address of the AP.

Frequency

The latest
                                                   					 frequency where this AP was observed.

Current
                                                   					 channel

The
                                                   					 latest channel where this AP was observed.

Last RSSI

The latest
                                                   					 RSSI in which this AP was observed.

Beacon
                                                   					 interval

Number of
                                                   					 time units between beacons. A time unit is 1.024 ms.

Capability

This field
                                                   					 contains a number of subfields that are used to indicate requested or
                                                   					 advertised optional capabilities.

Basic
                                                   					 rates

Data rates
                                                   					 that the AP requires and the AP at which the station must be capable of
                                                   					 operating.

Optional
                                                   					 rates

Data rates
                                                   					 that the AP supports and the AP that are optional for the station to operate
                                                   					 at.

Supported VHT(rx) rates

VHT Supported RX MCS Set received from AP.

Supported VHT(tx) rates

VHT Supported TX MCS Set received from AP.

Supported HT MCS

HT Supported MCS Set received from AP.

DTIM
                                                   					 period

Every nth
                                                   					 beacon is a dtime period. After each DTIM beacon, the AP sends any broadcast or
                                                   					 multicast packets that are queued for power-save devices.

Country
                                                   					 code

A
                                                   					 two-digit country code. Country information might not be display if the country
                                                   					 information element (IE) is not present in the beacon.

Channels

A list of
                                                   					 supported channels (from the country IE).

Power
                                                   					 constraint

The amount
                                                   					 of power by which the maximum transmit power should be reduced from the
                                                   					 regulatory domain limit.

Power
                                                   					 limit

Maximum
                                                   					 transmit power in dBm that is permitted for that channel.

Channel
                                                   					 utilization

The
                                                   					 percentage of time, normalized to 255, in which the AP sensed the medium was
                                                   					 busy, as indicated by the physical or virtual carrier sense (CS) mechanism.

Station
                                                   					 count

The total
                                                   					 number of STAs currently associated with this AP.

Admission
                                                   					 capacity

An
                                                   					 unsigned integer that specifies the remaining amount of medium time that is
                                                   					 available through explicit admission control, in units of 32 microseconds per
                                                   					 second.

If the
                                                   					 value is 0, the AP does not support this information element and the capacity
                                                   					 is unknown.

WMM
                                                   					 supported

Support
                                                   					 for Wi-Fi multimedia extensions.

UAPSD
                                                   					 Supported

The AP
                                                   					 supports Unscheduled Automatic Power Save Delivery. May only be available if
                                                   					 WMM is supported. This feature is critical for talk time and for achieving
                                                   					 maximum call density on the wireless IP Phone.

Proxy
                                                   					 ARP

CCX-compliant AP supports responding to IP ARP requests on
                                                   					 behalf of the associated station. This feature is critical to standby time on
                                                   					 the wireless IP Phone.

CCX
                                                   					 version

If the
                                                   					 AP is CCX compliant, this field shows the CCX version.

Best
                                                   					 Effort

Contains information related to the Best Effort queue.

Background

Contains information related to the Background queue.

Video

Contains information related to the Video queue.

Voice

Contains information related to the Voice queue.

## Cisco IP Phone Web
                        	 Page

Each Cisco IP Phone has a web page from which you can view a
                              		  variety of information about the phone, including:

Device information: Displays device settings and related
                                    				information for the phone.

Network setup: Displays network setup information and information
                                    				about other phone settings.

Network statistics: Displays hyperlinks that provide information
                                    				about network traffic.

Device logs: Displays hyperlinks that provide information that you
                                    				can use for troubleshooting.

Streaming statistic: Displays hyperlinks that display a variety of
                                    				streaming statistics.

System: Displays a hyperlink to restart the phone.

This section describes the information that you can obtain
                              		  from the phone web page. You can use this information to remotely monitor the
                              		  operation of a phone and to assist with troubleshooting.

You can also obtain much of this information directly from a
                              		  phone.

### Access Web Page
                           	 for Phone

To access
                                 		  the web page for a phone, follow these steps:

If you cannot
                                             			 access the web page, it may be disabled by default.

Step 1

Obtain the IP
                                          			 address of the Cisco IP Phone by using one of these methods:

Search for
                                                				  the phone in Cisco Unified Communications Manager Administration by choosing Device > Phone . Phones that register with Cisco
                                                				  Unified Communications Manager display the IP address on the Find and List
                                                   				  Phones window and at the top of the Phone Configuration window.

On the
                                                				  Cisco IP Phone, press Applications ,
                                                					 choose Admin
                                                      						  settings > Network setup > Ethernet
                                                      						  setup > IPv4 setup , and then scroll to the IP
                                                					 Address field.

Step 2

Open a web
                                          			 browser and enter the following URL, where IP_address is the IP
                                          			 address of the Cisco IP Phone:

http:// IP_address

#### Device
                              	 Information

The Device
                                 		information area on a phone web page displays device settings and related
                                 		information for the phone. The following table describes these items.

Some of the items
                                             		  in the following table do not apply to all phone models.

To display
                                 		the Device information area, access the web page for the phone as described in Access Web Page for Phone ,
                                 		and then click the Device information hyperlink.

Item

Description

Service mode

The service mode for the phone.

Service name

The domain for the service.

Service state

The current state of the service.

MAC Address

Media Access
                                             				Control (MAC) address of the phone.

Host name

Unique, fixed
                                             				name that is automatically assigned to the phone based on the MAC address.

Phone DN

Directory
                                             				number that is assigned to the phone.

App load ID

Application firmware version  that is running on the phone.

Boot load ID

Boot firmware version.

Version

Identifier of
                                             				the firmware that is running on the phone.

Key expansion
                                             				module 1

Identifier for
                                             				the first key expansion module, if applicable.

Applicable to Cisco IP Phone 8851, 8851NR, 8861, 8865, and 8865NR.

Key expansion
                                             				module 2

Identifier for
                                             				the second key expansion module, if applicable.

Applicable to Cisco IP Phone 8851, 8851NR, 8861, 8865, and 8865NR.

Key expansion
                                             				module 3

Identifier for
                                             				the third key expansion module, if applicable.

Applicable to Cisco IP Phone 8851, 8851NR, 8861, 8865, and 8865NR.

Hardware
                                             				revision

Minor revision value of the phone hardware.

Serial number

Unique serial
                                             				number of the phone.

Model number

Model number
                                             				of the phone.

Message
                                             				waiting

Indicates
                                             				whether is a voice message is waiting on the primary line for this phone.

UDI

Displays the
                                             				following Cisco Unique Device Identifier (UDI) information about the phone:

Device type—Indicates hardware type. For example, phone displays for all phone models.

Device description—Displays the name of the phone associated with the indicated model type.

Product identifier—Specifies the phone model.

Version ID (VID)—Specifies the major hardware version number.

Serial number—Displays the unique serial number of the phone.

Key expansion
                                             				module UDI

Cisco Unique
                                             				Device Identifier (UDI) of the key expansion module.

Applicable to Cisco IP Phone 8851, 8851NR, 8861, 8865, and 8865NR.

Name of the Headset

Displays the name of the attached Cisco headset in the left column. The right column contains this information:

Port—Displays how the headset connects to the phone.

USB

AUX

Version—Displays the headset firmware version.

Radio range—Displays the strength configured for the DECT radio. Applicable to the Cisco Headset 560 Series only.

Bandwidth—Displays if the headset uses Wide band or Narrow band. Applicable to the Cisco Headset 560 Series only.

Bluetooth—Displays if Bluetooth is enabled or disabled. Applicable to the Cisco Headset 560 Series only.

Conference—Displays if the conference feature is enabled or disabled. Applicable to the Cisco Headset 560 Series only.

Firmware source—Displays the permitted firmware upgrade method:

Restrict to UCM only

Allow from UCM or Cisco Cloud

Applicable to the Cisco Headset 560 Series only.

Time

Time for the
                                             				Date/Time Group to which the phone belongs. This information comes from Cisco
                                             				Unified Communications Manager.

Time zone

Time zone for
                                             				the Date/Time Group to which the phone belongs. This information comes from
                                             				Cisco Unified Communications Manager.

Date

Date for the
                                             				Date/Time Group to which the phone belongs. This information comes from Cisco
                                             				Unified Communications Manager.

System free memory

Amount of unused memory on the phone

Java heap free memory

Amount of free internal Java heap memory

Java pool free memory

Amount of free internal Java pool memory

FIPS mode
                                             				enabled

Indicates if
                                             				the Federal Information Processing Standard (FIPS) Mode is enabled.

#### Network
                              	 Setup

The
                                 		Network setup area on a phone web page displays network setup information and
                                 		information about other phone settings. The following table describes these
                                 		items.

You can
                                 		view and set many of these items from the Network Setup menu on the Cisco IP
                                 		Phone.

Some of the items in the following table do not apply to all phone models.

To display
                                 		the Network Setup area, access the web page for the phone as described in Access Web Page for Phone ,
                                 		and then click the Network setup hyperlink.

Item

Description

MAC address

Media Access
                                             				Control (MAC) address of the phone.

Host name

Host name that
                                             				the DHCP server assigned to the phone.

Domain name

Name of the
                                             				Domain Name System (DNS) domain in which the phone resides.

DHCP server

IP address of
                                             				the Dynamic Host Configuration Protocol (DHCP) server from which the phone
                                             				obtains the IP address.

BOOTP server

Indicates
                                             				whether the phone obtains the configuration from a Bootstrap Protocol (BootP)
                                             				server.

DHCP

Indicates
                                             				whether the phone uses DHCP.

IP address

Internet
                                             				Protocol (IPv4) address of the phone.

Subnet mask

Subnet mask
                                             				that the phone uses.

Default router

Default router
                                             				used that the phone uses.

DNS server 1–3

Primary Domain
                                             				Name System (DNS) server (DNS Server 1) and optional backup DNS servers (DNS
                                             				Server 2 and 3) that the phone uses.

Alternate TFTP

Indicates
                                             				whether the phone is using an alternative TFTP server.

TFTP server 1

Primary
                                             				Trivial File Transfer Protocol (TFTP) server used that the phone uses.

TFTP server 2

Backup Trivial
                                             				File Transfer Protocol (TFTP) server used that the phone uses.

DHCP address released

Indicates
                                             				the setting of the DHCP address rReleased option on the phone Network
                                             				Configuration menu.

Operational VLAN ID

Operational
                                             				Virtual Local Area Network (VLAN) that is configured on a Cisco Catalyst switch
                                             				in which the phone is a member.

Admin VLAN ID

Auxiliary VLAN
                                             				in which the phone is a member.

CUCM server1–5

Host names or
                                             				IP addresses, in prioritized order, of the Cisco Unified Communications Manager
                                             				servers with which the phone can register. An item can also show the IP address
                                             				of an SRST router that is capable of providing limited Cisco Unified
                                             				Communications Manager functionality, if such a router is available.

For an
                                             				available server, an item shows the Cisco Unified Communications Manager server
                                             				IP address and one of the following states:

- Active—Cisco Unified
                                                				  Communications Manager server from which the phone is currently receiving
                                                				  call-processing services

- Standby—Cisco Unified
                                                				  Communications Manager server to which the phone switches if the current server
                                                				  becomes unavailable

- Blank—No current
                                                				  connection to this Cisco Unified Communications Manager server

An item may
                                             				also include the Survivable Remote Site Telephony (SRST) designation, which
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

Messages URL

URL of the
                                             				server from which the phone obtains message services.

Services URL

URL of the
                                             				server from which the phone obtains Cisco Unified IP Phone services.

Idle URL

URL that the
                                             				phone displays when the phone is idle for the time that the Idle URL Time field
                                             				specifies and no menu is open.

Idle URL time

Number of
                                             				seconds that the phone is idle and no menu is open before the XML service that
                                             				the Idle URL specifies activates.

Proxy server URL

URL of proxy
                                             				server, which makes HTTP requests to nonlocal host addresses on behalf of the
                                             				phone HTTP client and provides responses from the nonlocal host to the phone
                                             				HTTP client.

Authentication URL

URL that the
                                             				phone uses to validate requests that are made to the phone web server.

SW port setup

Speed and
                                             				duplex of the switch port, where:

- A = Auto Negotiate

- 10H = 10-BaseT/half
                                                				  duplex

- 10F = 10-BaseT/full
                                                				  duplex

- 100H = 100-BaseT/half
                                                				  duplex

- 100F = 100-BaseT/full
                                                				  duplex

- 1000F = 1000-BaseT/full
                                                				  duplex

- No Link= No connection to
                                                				  the switch port

PC port setup

Speed and
                                             				duplex of the PC port, where:

- A = Auto Negotiate

- 10H = 10-BaseT/half
                                                				  duplex

- 10F = 10-BaseT/full
                                                				  duplex

- 100H = 100-BaseT/half
                                                				  duplex

- 100F = 100-BaseT/full
                                                				  duplex

- 1000F = 1000-BaseT/full
                                                				  duplex

- No Link = No connection
                                                				  to the PC port

PC port disabled

Indicates
                                             				whether the PC port on the phone is enabled or disabled.

User locale

User locale
                                             				that associates with the phone user. Identifies a set of detailed information
                                             				to support users, including language, font, date and time formatting, and
                                             				alphanumeric keyboard text information.

Network locale

Network
                                             				locale that associates with the phone user. Identifies a set of detailed
                                             				information to support the phone in a specific location, including definitions
                                             				of the tones and cadences that the phone uses.

User locale version

Version of
                                             				the user locale that is loaded on the phone.

Network locale version

Version of
                                             				the network locale that is loaded on the phone.

Speaker enabled

Indicates
                                             				whether the speakerphone is enabled on the phone.

GARP enabled

Indicates
                                             				whether the phone learns MAC addresses from Gratuitous ARP responses.

Span to PC port

Indicates
                                             				whether the phone forwards packets that are transmitted and received on the
                                             				network port to the access port.

Video capability enabled

Indicates
                                             				whether the phone can participate in video calls when it connects to an
                                             				appropriately equipped camera.

Voice VLAN enabled

Indicates
                                             				whether the phone allows a device that is attached to the PC port to access the
                                             				Voice VLAN.

PC VLAN enabled

VLAN that
                                             				identifies and removes 802.1P/Q tags from packets that are sent to the PC.

Auto line select enabled

Identifies if the phone automatically selects a line when the phone goes off hook.

DSCP protocol control

DSCP IP
                                             				classification for call control signaling.

DSCP for configuration

DSCP IP
                                             				classification for any phone configuration transfer.

DSCP for services

DSCP IP
                                             				classification for phone-based services.

Security mode (nonsecure)

Security
                                             				mode that is set for the phone.

Web access enabled

Indicates
                                             				whether web access is enabled (Yes) or disabled (No) for the phone.

SSH access enabled

Indicates if the SSH port has been enabled or disabled.

CDP: SW Port

Indicates
                                             				whether CDP support exists on the switch port (default is enabled).

Enable CDP
                                             				on the switch port for VLAN assignment for the phone, power negotiation, QoS
                                             				management, and 802.1x security.

Enable CDP
                                             				on the switch port when the phone connects to a Cisco switch.

When CDP is
                                             				disabled in Cisco Unified Communications Manager, a warning is presented,
                                             				indicating that CDP should be disabled on the switch port only if the phone
                                             				connects to a non-Cisco switch.

The current
                                             				PC and switch port CDP values are shown on the Settings menu.

CDP: PC Port

Indicates
                                             				whether CDP is supported on the PC port (default is enabled).

When CDP is
                                             				disabled in Cisco Unified Communications Manager, a warning is displays to
                                             				indicate that disabling CDP on the PC port prevents CVTA from working.

The current
                                             				PC and switch port CDP values are shown in the Settings menu.

LLDP-MED:SW Port

Indicates
                                             				whether Link Layer Discovery Protocol Media Endpoint Discovery (LLDP-MED) is
                                             				enabled on the switch port.

LLDP-MED:PC Port

Indicates
                                             				whether LLDP-MED is enabled on the PC port.

LLDP Power Priority

Phone power priority to the switch, thus enabling the switch to
                                             				appropriately provide power to the phones. Settings include:

- Unknown: This is the
                                                				  default value.

- Low

- High

- Critical

LLDP Asset ID

Asset ID that is assigned to the phone for inventory management.

CTL file

MD5 hash of the CTL file.

ITL file

The ITL file contains the initial trust list.

ITL signature

MD5 hash of the ITL file

CAPF server

CPF server in use

TVS

The main component of Security by Default. Trust Verification Services (TVS) enables Cisco Unified IP Phones to authenticate
                                             application servers, such as EM services, directory, and MIDlet, during HTTPS establishment.

TFTP server

The name of the TFTP Server used by the phone.

TFTP server

The name of the TFTP Server used by the phone.

Automatic port synchronization

Indicates if the  phone automatically synchronizes port speed to eliminate packet loss.

Switch port remote configuration

Indicates if the SW port is remotely controlled.

PC port remote configuration

Indicates if the PC port is remotely controlled.

IP addressing mode

Identifies the addressing mode:

IPv4 Only

IPv4 and IPv6

IPv6 Only

IP preference mode control

Indicates the IP address version that the phone uses during signaling with Cisco Unified Communications Manager when both
                                             IPv4 and IPv6 are both available on the phone.

IP preference mode for media

IPv6 auto configuration

Indicates that for media the device uses an IPv4 address to connect to the Cisco Unified Communications Manager.

IPv6 duplicate address protection

IPv6 accept redirect message

Indicates if phone accepts the redirect messages from the same router that is used for the destination number.

IPv6 reply multicast echo request

Indicates that the phone sends an Echo Reply message in response to an Echo Request message sent to an IPv6-only address.

IPv6 load server

Used to optimize installation time for phone firmware upgrades and off load the WAN by storing images locally, negating the
                                             need to traverse the WAN link for each phone's upgrade.

IPv6 log server

IPv6 CAPF server

Indicates the IP address and port of the remote logging machine to which the phone sends log messages.

DHCPv6

Indicates the method that the phone uses to get the IPv6-only address.

When DHCPv6 is enabled, the phone gets the IPv6 address either
                                             from DHCPv6 server or from SLAAC by RA sent by the IPv6-enabled
                                             router. And if DHCPv6 is disabled, the phone will not have any
                                             stateful (from DHCPv6 server) or stateless (from SLAAC) IPv6
                                             address.

Unlike DHCPv4, even DHCPv6 is disabled the phone can still
                                                         generate a SLAAC address if autoconfigure is enabled.

IPv6 address

Displays the current IPv6-only address of the phone.

Two address formats are supported:

Eight sets of hexadecimal digits separated by colons X:X:X:X:X:X:X:X

Compressed format to collapse a single run of consecutive zero groups into a single group represented by a double colon.

IPv6 prefix length

Displays the current IPv6-only prefix length for the subnet.

IPv6 default router

Displays the default IPv6 router used by the phone.

IPv6 DNS server 1–2

Displays the primary and secondary DNSv6 server used by the phone

IPv6 Alternate TFTP

Displays if an alternate IPv6 TFTP server is used.

IPv6 TFTP server 1–2

Displays the primary and secondary IPv6 TFTP server used by the phone.

IPv6 address released

Displays if the user has released the IPv6-related information.

EnergyWise power level

The power level that is used when the phone is sleeping.

EnergyWise domain

The EnergyWise domain that the phone is in.

DF_BIT

Indicates the DF bit setting for packets.

#### Network
                              	 Statistics

The following Network statistics hyperlinks on a phone web
                                    		  page provide information about network traffic on the phone:

Ethernet information: Displays information about Ethernet traffic.

Access: Displays information about network traffic to and from the
                                          				PC port on the phone.

Network: Displays information about network traffic to and from
                                          				the network port on the phone.

To display a Network statistics area, access the web page
                                    		  for the phone, and then click the Ethernet Information , the Access , or the Network hyperlink.

##### Ethernet
                                 	 Information Web Page

The following table describes the contents of the Ethernet
                                       		  information web page.

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

Total number of shed packets that the no Direct Memory Access
                                                   					 (DMA) descriptor causes.

##### Access and Network
                                 	 Web Pages

The following table describes the information in the Access
                                       		  and Network web pages.

Item

Description

Rx totalPkt

Total number of packets that the phone received.

Rx crcErr

Total number of packets that were received with CRC failed.

Rx alignErr

Total number of packets between 64 and 1522 bytes in length
                                                   					 that were received and that have a bad Frame Check Sequence (FCS).

Rx multicast

Total number of multicast packets that the phone received.

Rx broadcast

Total number of broadcast packets that the phone received.

Rx unicast

Total number of unicast packets that the phone received.

Rx shortErr

Total number of received FCS error packets or Align error
                                                   					 packets that are less than 64 bytes in size.

Rx shortGood

Total number of received good packets that are less than 64
                                                   					 bytes size.

Rx longGood

Total number of received good packets that are greater than
                                                   					 1522 bytes in size.

Rx longErr

Total number of received FCS error packets or Align error
                                                   					 packets that are greater than 1522 bytes in size.

Rx size64

Total number of received packets, including bad packets, that
                                                   					 are between 0 and 64 bytes in size.

Rx size65to127

Total number of received packets, including bad packets, that
                                                   					 are between 65 and 127 bytes in size.

Rx size128to255

Total number of received packets, including bad packets, that
                                                   					 are between 128 and 255 bytes in size.

Rx size256to511

Total number of received packets, including bad packets, that
                                                   					 are between 256 and 511 bytes in size.

Rx size512to1023

Total number of received packets, including bad packets, that
                                                   					 are between 512 and 1023 bytes in size.

Rx size1024to1518

Total number of received packets, including bad packets, that
                                                   					 are between 1024 and 1518 bytes in size.

Rx tokenDrop

Total number of packets that were dropped due to lack of
                                                   					 resources (for example, FIFO overflow).

Tx excessDefer

Total number of packets that were delayed from transmitting
                                                   					 due to busy medium.

Tx lateCollision

Number of times that collisions occurred later than 512 bit
                                                   					 times after the start of packet transmission.

Tx totalGoodPkt

Total number of good packets (multicast, broadcast, and
                                                   					 unicast) that the phone received.

Tx Collisions

Total number of collisions that occurred while a packet was
                                                   					 transmitted.

Tx excessLength

Total number of packets that were not transmitted because the
                                                   					 packet experienced 16 transmission attempts.

Tx broadcast

Total number of broadcast packets that the phone transmitted.

Tx multicast

Total number of multicast packets that the phone transmitted.

LLDP FramesOutTotal

Total number of LLDP frames that the phone sent out.

LLDP AgeoutsTotal

Total number of LLDP frames that timed out in the cache.

LLDP FramesDiscardedTotal

Total number of LLDP frames that were discarded when any of
                                                   					 the mandatory TLVs is missing, out of order, or contains out of range string
                                                   					 length.

LLDP FramesInErrorsTotal

Total number of LLDP frames that were received with one or
                                                   					 more detectable errors.

LLDP FramesInTotal

Total number of LLDP frames that the phone receives.

LLDP TLVDiscardedTotal

Total number of LLDP TLVs that are discarded.

LLDP TLVUnrecognizedTotal

Total number of LLDP TLVs that are not recognized on the
                                                   					 phone.

CDP Neighbor Device ID

Identifier of a device connected to this port that CDP
                                                   					 discovered.

CDP Neighbor IPv6 address

IP address of the neighbor device discovered that CDP protocol
                                                   					 discovered.

CDP Neighbor Port

Neighbor device port to which the phone is connected
                                                   					 discovered by CDP protocol.

LLDP Neighbor Device ID

Identifier of a device connected to this port discovered by
                                                   					 LLDP discovered.

LLDP Neighbor IPv6 address

IP address of the neighbor device that LLDP protocol
                                                   					 discovered.

LLDP Neighbor Port

Neighbor device port to which the phone connects that LLDP
                                                   					 protocol discovered.

Port Information

Speed and duplex information.

#### Device
                              	 Logs

The following Device log hyperlinks on a phone web page provide
                                    		  information that helps to monitor and troubleshoot the phone.

Console logs: Includes hyperlinks to individual log files. The
                                          				console log files include debug and error messages that the phone received.

Core dumps: Includes hyperlinks to individual dump files. The core
                                          				dump files include data from a phone crash.

Status messages: Displays the 10 most recent status messages that
                                          				the phone has generated since it last powered up. The Status Messages screen on
                                          				the phone also displays this information.

Debug display: Displays debug messages that might be useful to
                                          				Cisco TAC if you require assistance with troubleshooting.

#### Streaming
                              	 Statistics

A Cisco Unified IP Phone can stream information to and from
                                    		  up to three devices simultaneously. A phone streams information when it is on a
                                    		  call or is running a service that sends or receives audio or data.

The Streaming statistics areas on a phone web page provide
                                    		  information about the streams.

The following table describes the items in the Streaming
                                    		  Statistics areas.

Item

Description

Remote address

IP address and UDP port of the destination of the stream.

Local address

IP address and UPD port of the phone.

Start time

Internal time stamp indicates when Cisco Unified
                                                					 Communications Manager requested that the phone start transmitting packets.

Stream status

Indication of whether streaming is active or not.

Host name

Unique, fixed name that is automatically assigned to the phone
                                                					 based on the MAC address.

Sender packets

Total number of RTP data packets that the phone transmitted
                                                					 since it started this connection. The value is 0 if the connection is set to
                                                					 receive-only mode.

Sender octets

Total number of payload octets that the phone transmitted in
                                                					 RTP data packets since it started this connection. The value is 0 if the
                                                					 connection is set to receive-only mode.

Sender codec

Type of audio encoding that is for the transmitted stream.

Sender reports sent

(see note)

Number of times the RTCP Sender Report has been sent.

Sender report time sent

(see note)

Internal time-stamp indication as to when the last RTCP Sender
                                                					 Report was sent.

Rcvr lost packets

Total number of RTP data packets that have been lost since
                                                					 data reception started on this connection. Defined as the number of expected
                                                					 packets less the number of packets actually received, where the number of
                                                					 received packets includes any that are late or are duplicates. The value
                                                					 displays as 0 if the connection was set to send-only mode.

Avg jitter

Estimate of mean deviation of the RTP data packet interarrival
                                                					 time, measured in milliseconds. The value displays as 0 if the connection was
                                                					 set to send-only mode.

Receiver codec

Type of audio encoding that is used for the received stream.

Receiver reports sent

(see note)

Number of times the RTCP Receiver Reports have been sent.

Receiver report time sent

(see note)

Internal time-stamp indication as to when a RTCP Receiver
                                                					 Report was sent.

Rcvr packets

Total number of RTP data packets that the phone has received
                                                					 since data reception started on this connection. Includes packets that were
                                                					 received from different sources if this call is a multicast call. The value
                                                					 displays as 0 if the connection was set to send-only mode.

Rcvr octets

Total number of payload octets that the device received in RTP
                                                					 data packets since reception started on the connection. Includes packets that
                                                					 were received from different sources if this call is a multicast call. The
                                                					 value displays as 0 if the connection was set to send-only mode.

MOS LQK

Score that is an objective estimate of the mean opinion score
                                                					 (MOS) for listening quality (LQK) that rates from 5 (excellent) to 1(bad).
                                                					 This score is based on audible concealment events that are to frame loss in the
                                                					 preceding eight-second interval of the voice stream. For more information, see Voice Quality Monitoring .

The MOS LQK score can vary due to the codec type that the
                                                            						Cisco Unified IP Phone uses.

Avg MOS LQK

Average MOS LQK score that was observed for the entire voice
                                                					 stream.

Min MOS LQK

Lowest MOS LQK score that was observed from the start of the
                                                					 voice stream.

Max MOS LQK

Baseline or highest MOS LQK score that was observed from start
                                                					 of the voice stream.

These codecs provide the following maximum MOS LQK score under
                                                					 normal conditions with no frame loss:

- G.711 yields 4.5.

- G.729 A /AB yields
                                                   						3.7.

MOS LQK version

Version of the Cisco proprietary algorithm that is used to
                                                					 calculate MOS LQK scores.

Cumulative conceal ratio

Total number of concealment frames divided by total number of
                                                					 speech frames that were received from the start of the voice stream.

Interval conceal ratio

Ratio of concealment frames to speech frames in the preceding
                                                					 3-second interval of active speech. If voice activity detection (VAD) is in
                                                					 use, a longer interval might be required to accumulate three seconds of active
                                                					 speech.

Max conceal ratio

Highest interval concealment ratio from the start of the voice
                                                					 stream.

Conceal secs

Number of seconds that have concealment events (lost frames)
                                                					 from the start of the voice stream (includes severely concealed seconds).

Severely conceal secs

Number of seconds that have more than five percent concealment
                                                					 events (lost frames) from the start of the voice stream.

Latency

(see note)

Estimate of the network latency, expressed in milliseconds.
                                                					 Represents a running average of the round-trip delay, measured when RTCP
                                                					 receiver report blocks are received.

Max jitter

Maximum value of instantaneous jitter, in milliseconds.

Sender size

RTP packet size, in milliseconds, for the transmitted stream.

Sender reports received

(see note)

Number of times RTCP Sender Reports have been received.

Sender report time received

(see note)

Most recent time when an RTCP Sender Report was received.

Receiver size

RTP packet size, in milliseconds, for the received stream.

Receiver discarded

RTP packets that were received from the network but were
                                                					 discarded from the jitter buffers.

Receiver reports received

(see note)

Number of times RTCP Receiver Reports have been received.

Receiver report time received

(see note)

Most recent time when an RTCP Receiver Report was received.

Rcvr encrypted

Indicates if the receiver  is using encryption.

Sender encrypted

Indicates if the sender is using encryption.

Sender frames

Number of frames sent.

Sender partial frames

Number of partial frames sent.

Sender i frames

Number of I frames sent. I frames are used in video transmission.

Sender IDR frames

Number of instantaneous decoder refresh (IDR) frames sent. IDR frames are used in video transmission.

Sender frame rate

Rate at which the sender is sending frames.

Sender bandwidth

Bandwidth for the sender.

Sender resolution

Video resolution of the sender.

Rcvr frames

Number of frames received

Rcvr partial frames

Number of partial frames received

Rcvr i frames

Number of I frames received.

Rcvr IDR frames

Number of IDR frames received.

Rcvr IFrames req

Number of requested IDR frames received

Rcvr frame rate

Rate at which the receiver is receiving frames.

Rcvr frames lost

Number of frames that were not received.

Rcvr frame errors

Number of frames that were not received.

Rcvr bandwidth

Bandwidth of the receiver.

Rcvr resolution

Video resolution of the receiver.

Domain

Domain that the phone resides in.

Sender joins

Number of times the sender joined.

Rcvr joins

Number of times the receiver joined

Byes

Number of "Bye" frames

Sender start time

Time that the sender started.

Rcvr start time

Time that the receiver started.

Row status

Whether the phone is streaming

Sender tool

Type of audio encoding used for the stream

Sender reports

RTCP Sender Reports

Sender report time

Last time at which an RTCP Sender Report was sent.

Rcvr Jitter

Maximum jitter of stream

Receiver tool

Type of audio encoding used for the stream

Rcvr reports

Number of times this streaming statistics report has been accessed from the web page.

Rcvr report time

Internal time stamp indicating when this streaming statistics report was generated

Is video

Indicates if the call was a video call or audio only.

Call ID

Identification of the call

Group ID

Identification of the group that the phone is in.

When the RTP Control Protocol is disabled, no data generates for
                                                			 this field and thus displays as 0.

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

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Phone Information . If the user is connected to a secure or authenticated server, a
                                             				corresponding icon (lock or certificate) displays in the Phone Information
                                             				Screen to the right of the server option. If the user is not connected to a
                                             				secure or authenticated server, no icon appears. |
| Step 3 | To exit the Model Information screen, press Exit . |

| Option | Description |
|---|---|
| Model number | Model number of the phone. |
| IPv4 Address | IP address of the phone. |
| Host name | Host name of the phone. |
| Active load | Version of firmware currently installed on the phone. The user
                                                					 can press Details for more information. |
| Inactive load | Inactive load appears only when a download is in progress. A
                                                					 download icon and a status of "Upgrade in Progress" or "Upgrade Failed" also display. If a user presses Details during an upgrade, the download filename and
                                                					 components are listed. A new firmware image can be set to download in advance of a
                                                					 maintenance window. Thus instead of waiting for all of the phones to download
                                                					 the firmware, the system switches more rapidly between resetting an existing
                                                					 load to Inactive status and installing the new load. When the download is complete, the icon changes to indicate
                                                					 the completed status; and a check mark displays for a successful download, or
                                                					 an "X" displays for a failed download. If possible, the rest
                                                					 of the loads continue to download. |
| Last upgrade | Date of the most recent firmware upgrade. |
| Active server | Domain name of the server to which the phone is registered. |
| Stand-by server | Domain name of the standby server. |

| Step 1 | To display the Status menu, press Applications . |
|---|---|
| Step 2 | Select Admin
                                                				  settings > Status . |
| Step 3 | To exit the
                                          			 Status menu, press Exit . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Admin
                                                   				  settings > Status > Status
                                                   				  messages . |
| Step 3 | To remove the
                                             			 current status messages, press Clear . |
| Step 4 | To exit the
                                             			 Status Messages screen, press Exit . |

| Message | Description | Possible explanation and action |
|---|---|---|
| CFG TFTP Size Error | The configuration file is too large for file system on the phone. | Power cycle the phone. |
| Checksum Error | Downloaded software file is corrupted. | Obtain a new copy of the phone firmware and place it in the TFTPPath directory. You should only copy files into this directory
                                                   when the TFTP server software is shut down; otherwise, the files may be corrupted. |
| Could not acquire an IP address from DHCP | The phone has not previously obtained an IP address from a DHCP Server. This can occur when you perform an out of box or factory
                                                   reset. | Confirm that the DHCP server is available and that an IP address is available for the phone. |
| CTL and ITL installed | The CTL and ITL files are installed on the phone. | None. This message is informational only. Neither the CTL file nor the ITL file was installed previously. |
| CTL Installed | A certificate trust list (CTL) file is installed in the phone. | None. This message is informational only. The CTL file was not installed previously. |
| CTL update failed | The phone could not update the certificate trust list (CTL) file. | Problem with the CTL file on the TFTP server. |
| DHCP timeout | DHCP server did not respond. | Network is busy: The errors should resolve themselves when the network load reduces. No network connectivity between the DHCP server and the phone: Verify the network connections. DHCP server is down: Check configuration of DHCP server. Errors persist: Consider assigning a static IP address. |
| DNS timeout | DNS server did not respond. | Network is busy: The errors should resolve themselves when the network load reduces. No network connectivity between the DNS server and the phone: Verify the network connections. DNS server is down: Check configuration of the DNS server. |
| DNS unknown host | DNS could not resolve the name of the TFTP server or Cisco Unified Communications Manager. | Verify that the host names of the TFTP server or Cisco Unified Communications Manager are configured properly in DNS. Consider using IP addresses rather than host names |
| Duplicate IP | Another device is using the IP address that is assigned to the phone. | If the phone has a static IP address, verify that you did not assigned a duplicate IP address. If you are using DHCP, check the DHCP server configuration. |
| Erasing CTL and ITL files | Erasing CTL or ITL file. | None. This message is informational only. |
| Error update locale | One or more localization files could not be found in the TFTPPath directory or were not valid. The locale was not changed. | From Cisco Unified Operating System Administration, check that the following files are located within subdirectories in the
                                                   TFTP File Management: Located in subdirectory with same name as network locale: tones.xml Located in subdirectory with same name as user locale: glyphs.xml dictionary.xml kate.xml |
| File not found <Cfg File> | The name-based and default configuration file was not found on the TFTP Server. | The configuration file for a phone is created when the phone is added to the Cisco Unified Communications Manager database.
                                                   If the phone does not exist in the Cisco Unified Communications Manager database, the TFTP server generates a CFG File Not Found response. Phone is not registered with Cisco Unified Communications Manager. You must manually add the phone to Cisco Unified Communications Manager if you are not allowing phones to autoregister. See Phone Addition Methods for details. If you are using DHCP, verify that the DHCP server is pointing to the correct TFTP server. If you are using static IP addresses, check configuration of the TFTP server. |
| File Not Found <CTLFile.tlv> | This message displays on the phone when the Cisco Unified Communications Manager cluster is not in secure mode. | No impact; the phone can still register to Cisco Unified Communications Manager. |
| IP address released | The phone is configured to release the IP address. | The phone remains idle until it is power cycled or until you reset the DHCP address. |
| ITL installed | The ITL file is installed in the phone. | None. This message is informational only. The ITL file was not installed previously. |
| Load rejected HC | The application that was downloaded is not compatible with the phone hardware. | Occurs if you attempted to install a version of software on this phone that did not support hardware changes on this phone. Check the load ID that is assigned to the phone (from Cisco Unified Communications Manager, choose Device > Phone ). Reenter the load that displays on the phone. |
| No default router | DHCP or static configuration did not specify a default router. | If the phone has a static IP address, verify that the default router is configured. If you are using DHCP, the DHCP server has not provided a default router. Check the DHCP server configuration. |
| No DNS server IP | A name was specified but DHCP or static IP configuration did not specify a DNS server address. | If the phone has a static IP address, verify that the DNS server is configured. If you are using DHCP, the DHCP server has not provided a DNS server. Check the DHCP server configuration. |
| No Trust List installed | The CTL file or the ITL file is not installed on the phone. | The trust list is not configured on the Cisco Unified Communications Manager, which does not support security by default. |
| Phone failed to register. Cert key size is not FIPS compliant. | FIPS requires that the RSA server certificate is 2048 bits or greater. | Update the certificate. |
| Restart requested by Cisco Unified Communications Manager | The phone is restarting due to on a request from Cisco Unified Communications Manager. | Configuration changes were likely made to the phone in Cisco Unified Communications Manager, and Apply was pressed so that
                                                   the changes take effect. |
| TFTP access error | TFTP server is pointing to a directory that does not exist. | If you are using DHCP, verify that the DHCP server is pointing to the correct TFTP server. If you are using static IP addresses, check configuration of TFTP server. |
| TFTP error | The phone does not recognize an error code that the TFTP server provided. | Contact Cisco TAC. |
| TFTP timeout | TFTP server did not respond. | Network is bus: The errors should resolve themselves when the network load reduces. No network connectivity between the TFTP server and the phone: Verify the network connections. TFTP server is down: Check configuration of TFTP server. |
| Timed Out | Supplicant attempted 802.1X transaction but timed out to due the absence of an authenticator. | Authentication typically times out if 802.1X is not configured on the switch. |
| Trust List update failed | Update of the CTL and ITL files failed. | Phone has CTL and ITL files installed and it failed to update the new CTL and ITL files. Possible reasons for failure: Network failure occurred. TFTP server was down. The new security token that was used to sign CTL file and the TFTP certificate that was used to sign ITL file are introduced,
                                                      but are not available in the current CTL and ITL files in the phone. Internal phone failure occurred. Possible solutions: Check network connectivity. Check whether the TFTP server is active and functioning normally. If the Transactional Vsam Services (TVS) server is supported on Cisco Unified Communications Manager, check whether the TVS
                                                      server is active and functioning normally. Verify whether the security token and the TFTP server are valid. Manually delete the CTL and ITL files if all the preceding solutions fail; reset the phone. |
| Trust List updated | The CTL file, the ITL file, or both files are updated. | None. This message is informational only. |
| Version error | The name of the phone load file is incorrect. | Make sure that the phone load file has the correct name. |
| XmlDefault.cnf.xml, or .cnf.xml corresponding to the phone device name | Name of the configuration file. | None. This message indicates the name of the configuration file for the phone. |

| Step 1 | To display the Status menu, press Applications . |
|---|---|
| Step 2 | Select Admin
                                                   				  settings > Status > Status messages . |
| Step 3 | Select Network Info . |
| Step 4 | To exit 
                                             			 Network Info, press Exit . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Admin
                                                				settings > Status > Network
                                                				statistics . |
| Step 3 | To reset the
                                             			 Rx Frames, Tx Frames, and Rx Broadcasts statistics to 0, press Clear . |
| Step 4 | To exit the
                                             			 Ethernet Statistics screen, press Exit . |

| Item | Description |
|---|---|
| Rx Frames | Number of packets that the phone received. |
| Tx Frames | Number of packets that the phone sent. |
| Rx Broadcasts | Number of broadcast packets that the phone received. |
| Restart Cause | Cause of the last reset of the phone. Specifies one of the
                                                   					 following values: Initialized TCP-timeout CM-closed-TCP TCP-Bad-ACK CM-reset-TCP CM-aborted-TCP CM-NAKed KeepaliveTO Failback Phone-Keypad Phone-Re-IP Reset-Reset Reset-Restart Phone-Reg-Rej Load Rejected HC CM-ICMP-Unreach Phone-Abort |
| Elapsed Time | Amount of time that has elapsed since the phone last rebooted. |
| Port 1 | Link state and connection of the Network port. For example, Auto 100 Mb Full-Duplex means that the
                                                   					 Network port is in a link-up state and has autonegotiated a full-duplex,
                                                   					 100-Mbps connection. |
| Port 2 | Link state and connection of the PC port. |
| DHCP state (IPv4 / IPv6) | In IPv4-only mode, displays only the DHCPv4 state, such as DHCP BOUND. In IPv6-mode, displays only the DHCPv6 state, such as ROUTER ADVERTISE. DHCPv6 state information is displayed. |

| DHCPv4 state | Description |
|---|---|
| CDP INIT | CDP is not bound or WLAN is not in service |
| DHCP BOUND | DHCPv4 is BOUND |
| DHCP DISABLED | DHCPv4 is disabled |
| DHCP INIT | DHCPv4 is INIT |
| DHCP INVALID | DHCPv4 is INVALID; this is initial state |
| DHCP RENEWING | DHCPv4 is RENEWING |
| DHCP REBINDING | DHCPv4 is REBINDING |
| DHCP REBOOT | DHCPv4 is init-reboot |
| DHCP REQUESTING | DHCPv4 is requesting |
| DHCP RESYNC | DHCPv4 is RESYNCH |
| DHCP WAITING COLDBOOT TIMEOUT | DHCPv4 is booting |
| DHCP UNRECOGNIZED | Unrecognized DHCPv4 state |
| DISABLED DUPLICATE IP | Duplicated IPv4 Address |
| DHCP TIMEOUT | DHCPv4 Timeout |
| IPV4 STACK TURNED OFF | Phone is in IPv6-only mode with IPv4 Stack turned off |
| ILLEGAL IPV4 STATE | Illegal IPv4 state and should not happen |

| DHCPv6 State | Description |
|---|---|
| CDP INIT | CDP is initializing |
| DHCP6 BOUND | DHCPv6 is BOUND |
| DHCP6 DISABLED | DHCPv6 is DISABLED |
| DHCP6 RENEW | DHCPv6 is renewing |
| DHCP6 REBIND | DHCPv6 is rebinding |
| DHCP6 INIT | DHCPv6 is initializing |
| DHCP6 SOLICIT | DHCPv6 is soliciting |
| DHCP6 REQUEST | DHCPv6 is requesting |
| DHCP6 RELEASING | DHCPv6 is releasing |
| DHCP6 RELEASED | DHCPv6 is released |
| DHCP6 DISABLING | DHCPv6 is disabling |
| DHCP6 DECLINING | DHCPv6 is declining |
| DHCP6 DECLINED | DHCPv6 is declined |
| DHCP6 INFOREQ | DHCPv6 is INFOREQ |
| DHCP6 INFOREQ DONE | DHCPv6 is INFOREQ DONE |
| DHCP6 INVALID | DHCPv6 is INVALID; this is initial state |
| DISABLED DUPLICATE IPV6 | DHCP6 is DISABLED, but DUPLICATE IPV6 DETECTED |
| DHCP6 DECLINED DUPLICATE IP | DHCP6 is DECLINED -- DUPLICATE IPV6 DETECTED |
| ROUTER ADVERTISE., (DUPLICATE IP) | Duplicated autoconfigured IPv6 address |
| DHCP6 WAITING COLDBOOT TIMEOUT | DHCPv6 is booting |
| DHCP6 TIMEOUT USING RESTORED VAL | DHCPv6 timeout, using the value saved in flash memory |
| DHCP6 TIMEOUT CANNOT RESTORE | DHCP6 timeout and there is no backup from flash memory |
| IPV6 STACK TURNED OFF | Phone is in IPv4-only mode with IPv6 Stack turned off |
| ROUTER ADVERTISE., (GOOD IP) |  |
| ROUTER ADVERTISE., (BAD IP) |  |
| UNRECOGNIZED MANAGED BY | IPv6 Address is not from router or DHCPv6 server |
| ILLEGAL IPV6 STATE | Illegal IPv6 state and should not happen |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Admin
                                                				settings > Status > Wireless Statistics . |
| Step 3 | To reset the
                                             			 Wireless statistics to 0, press Clear . |
| Step 4 | To exit the
                                             			 Wireless Statistics screen, press Exit . |

| Item | Description |
|---|---|
| tx bytes | Number of bytes that the phone transmitted. |
| rx bytes | Number of bytes that the phone received. |
| tx packets | Number of packets that the phone transmitted. |
| rx packets | Number of packets that the phone received. |
| tx packets dropped | The number of packets dropped during transmission. |
| rx packets dropped | The number of packets dropped during reception. |
| tx packets errors | The number of erroneous packets that phone transmitted. |
| rx packets errors | The number of erroneous packets that phone received. |
| Tx frames | The number of successfully transmitted MSDU. |
| tx multicast frames | The nunber of successfully transmitted multicast MSDU. |
| tx retry | The number of MSDU that is successfully transmitted after one
                                                   					 or more retransmissions. |
| tx multi retry | The number of multicast MSDU that is successfully transmitted
                                                   					 after one or more retransmissions. |
| tx failure | This number of MSDU that is not transmitted successfully due
                                                   					 to the number of transmit attempts exceeding the retry limit. |
| rts succeess | This counter shall increment when a CTS is received in
                                                   					 response to an RTS. |
| rts failure | This counter shall increment when a CTS is not received in
                                                   					 response to an RTS. |
| ack failure | This counter shall increment when an ACK is not received when
                                                   					 expected. |
| rx duplicate frames | The number of received frame that the Sequence Control field
                                                   					 indicates is a duplicate. |
| rx fraagmented packets | The number of successfully received MPDU of type Data or
                                                   					 Management. |
| Roaming count | The number of succesful roaming. |

| Note | You can also
                                                			 remotely view the call statistics information by using a web browser to access
                                                			 the Streaming Statistics web page. This web page contains additional RTCP
                                                			 statistics that are not available on the phone. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Admin
                                                   				  settings > Status > Call
                                                   				  statistics . |
| Step 3 | To exit the
                                             			 Call Statistics screen, press Exit . |

| Item | Description |
|---|---|
| Receiver
                                                   					 codec | Type of received voice stream (RTP streaming audio from codec): G.729 G.722 G722.2 AMR-WB G.711 mu-law G.711 A-law iLBC Opus iSAC |
| Sender
                                                   					 codec | Type of transmitted voice stream (RTP streaming audio from codec): G.729 G.722 G722.2 AMR-WB G.711 mu-law G.711 A-law iLBC. Opus iSAC |
| Receiver
                                                   					 size | Size of
                                                   					 voice packets, in milliseconds, in the receiving voice stream (RTP streaming
                                                   					 audio). |
| Sender
                                                   					 size | Size of
                                                   					 voice packets, in milliseconds, in the transmitting voice stream. |
| Receiver
                                                   					 packets | Number of
                                                   					 RTP voice packets that were received since voice stream opened. Note This
                                                               						number is not necessarily identical to the number of RTP voice packets that
                                                               						were received since the call began because the call might have been placed on
                                                               						hold. | Note | This
                                                               						number is not necessarily identical to the number of RTP voice packets that
                                                               						were received since the call began because the call might have been placed on
                                                               						hold. |
| Note | This
                                                               						number is not necessarily identical to the number of RTP voice packets that
                                                               						were received since the call began because the call might have been placed on
                                                               						hold. |
| Sender
                                                   					 packets | Number of
                                                   					 RTP voice packets that were transmitted since voice stream opened. Note This
                                                               						number is not necessarily identical to the number of RTP voice packets that
                                                               						were transmitted since the call began because the call might have been placed
                                                               						on hold. | Note | This
                                                               						number is not necessarily identical to the number of RTP voice packets that
                                                               						were transmitted since the call began because the call might have been placed
                                                               						on hold. |
| Note | This
                                                               						number is not necessarily identical to the number of RTP voice packets that
                                                               						were transmitted since the call began because the call might have been placed
                                                               						on hold. |
| Avg jitter | Estimated
                                                   					 average RTP packet jitter (dynamic delay that a packet encounters when going
                                                   					 through the network), in milliseconds, that was observed since the receiving
                                                   					 voice stream opened. |
| Max jitter | Maximum
                                                   					 jitter, in milliseconds, that was observed since the receiving voice stream
                                                   					 opened. |
| Receiver
                                                   					 discarded | Number of
                                                   					 RTP packets in the receiving voice stream that were discarded (bad packets, too
                                                   					 late, and so on). Note The
                                                               						phone discards payload type 19 comfort noise packets that Cisco Gateways
                                                               						generate, because they increment this counter. | Note | The
                                                               						phone discards payload type 19 comfort noise packets that Cisco Gateways
                                                               						generate, because they increment this counter. |
| Note | The
                                                               						phone discards payload type 19 comfort noise packets that Cisco Gateways
                                                               						generate, because they increment this counter. |
| Receiver
                                                   					 lost packets | Missing
                                                   					 RTP packets (lost in transit). |
| Voice-Quality
                                                      						Metrics |
| Cumulative
                                                   					 conceal ratio | Total
                                                   					 number of concealment frames divided by total number of speech frames that were
                                                   					 received from start of the voice stream. |
| Interval
                                                   					 conceal ratio | Ratio of
                                                   					 concealment frames to speech frames in preceding 3-second interval of active
                                                   					 speech. If using voice activity detection (VAD), a longer interval might be
                                                   					 required to accumulate 3 seconds of active speech. |
| Max
                                                   					 conceal ratio | Highest
                                                   					 interval concealment ratio from start of the voice stream. |
| Conceal
                                                   					 seconds | Number of
                                                   					 seconds that have concealment events (lost frames) from the start of the voice
                                                   					 stream (includes severely concealed seconds). |
| Severely
                                                   					 conceal seconds | Number
                                                   					 of seconds that have more than 5 percent concealment events (lost frames) from
                                                   					 the start of the voice stream. |
| Latency | Estimate
                                                   					 of the network latency, expressed in milliseconds. Represents a running average
                                                   					 of the round-trip delay, measured when RTCP receiver report blocks are
                                                   					 received. |

| Note | This
                                                               						number is not necessarily identical to the number of RTP voice packets that
                                                               						were received since the call began because the call might have been placed on
                                                               						hold. |
|---|---|

| Note | This
                                                               						number is not necessarily identical to the number of RTP voice packets that
                                                               						were transmitted since the call began because the call might have been placed
                                                               						on hold. |
|---|---|

| Note | The
                                                               						phone discards payload type 19 comfort noise packets that Cisco Gateways
                                                               						generate, because they increment this counter. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Admin
                                                   				  settings > Status > Current Access
                                                   				  Point . |
| Step 3 | To exit the
                                             			 Current Access Point screen, press Exit . |

| Item | Description |
|---|---|
| AP name | Name of
                                                   					 the AP, if it is CCX-compliant; otherwise, the MAC address displays here. |
| MAC
                                                   					 address | MAC
                                                   					 address of the AP. |
| Frequency | The latest
                                                   					 frequency where this AP was observed. |
| Current
                                                   					 channel | The
                                                   					 latest channel where this AP was observed. |
| Last RSSI | The latest
                                                   					 RSSI in which this AP was observed. |
| Beacon
                                                   					 interval | Number of
                                                   					 time units between beacons. A time unit is 1.024 ms. |
| Capability | This field
                                                   					 contains a number of subfields that are used to indicate requested or
                                                   					 advertised optional capabilities. |
| Basic
                                                   					 rates | Data rates
                                                   					 that the AP requires and the AP at which the station must be capable of
                                                   					 operating. |
| Optional
                                                   					 rates | Data rates
                                                   					 that the AP supports and the AP that are optional for the station to operate
                                                   					 at. |
| Supported VHT(rx) rates | VHT Supported RX MCS Set received from AP. |
| Supported VHT(tx) rates | VHT Supported TX MCS Set received from AP. |
| Supported HT MCS | HT Supported MCS Set received from AP. |
| DTIM
                                                   					 period | Every nth
                                                   					 beacon is a dtime period. After each DTIM beacon, the AP sends any broadcast or
                                                   					 multicast packets that are queued for power-save devices. |
| Country
                                                   					 code | A
                                                   					 two-digit country code. Country information might not be display if the country
                                                   					 information element (IE) is not present in the beacon. |
| Channels | A list of
                                                   					 supported channels (from the country IE). |
| Power
                                                   					 constraint | The amount
                                                   					 of power by which the maximum transmit power should be reduced from the
                                                   					 regulatory domain limit. |
| Power
                                                   					 limit | Maximum
                                                   					 transmit power in dBm that is permitted for that channel. |
| Channel
                                                   					 utilization | The
                                                   					 percentage of time, normalized to 255, in which the AP sensed the medium was
                                                   					 busy, as indicated by the physical or virtual carrier sense (CS) mechanism. |
| Station
                                                   					 count | The total
                                                   					 number of STAs currently associated with this AP. |
| Admission
                                                   					 capacity | An
                                                   					 unsigned integer that specifies the remaining amount of medium time that is
                                                   					 available through explicit admission control, in units of 32 microseconds per
                                                   					 second. If the
                                                   					 value is 0, the AP does not support this information element and the capacity
                                                   					 is unknown. |
| WMM
                                                   					 supported | Support
                                                   					 for Wi-Fi multimedia extensions. |
| UAPSD
                                                   					 Supported | The AP
                                                   					 supports Unscheduled Automatic Power Save Delivery. May only be available if
                                                   					 WMM is supported. This feature is critical for talk time and for achieving
                                                   					 maximum call density on the wireless IP Phone. |
| Proxy
                                                   					 ARP | CCX-compliant AP supports responding to IP ARP requests on
                                                   					 behalf of the associated station. This feature is critical to standby time on
                                                   					 the wireless IP Phone. |
| CCX
                                                   					 version | If the
                                                   					 AP is CCX compliant, this field shows the CCX version. |
| Best
                                                   					 Effort | Contains information related to the Best Effort queue. |
| Background | Contains information related to the Background queue. |
| Video | Contains information related to the Video queue. |
| Voice | Contains information related to the Voice queue. |

| Note | If you cannot
                                             			 access the web page, it may be disabled by default. |
|---|---|

| Step 1 | Obtain the IP
                                          			 address of the Cisco IP Phone by using one of these methods: Search for
                                                				  the phone in Cisco Unified Communications Manager Administration by choosing Device > Phone . Phones that register with Cisco
                                                				  Unified Communications Manager display the IP address on the Find and List
                                                   				  Phones window and at the top of the Phone Configuration window. On the
                                                				  Cisco IP Phone, press Applications ,
                                                					 choose Admin
                                                      						  settings > Network setup > Ethernet
                                                      						  setup > IPv4 setup , and then scroll to the IP
                                                					 Address field. |
|---|---|
| Step 2 | Open a web
                                          			 browser and enter the following URL, where IP_address is the IP
                                          			 address of the Cisco IP Phone: http:// IP_address |

| Note | Some of the items
                                             		  in the following table do not apply to all phone models. |
|---|---|

| Item | Description |
|---|---|
| Service mode | The service mode for the phone. |
| Service name | The domain for the service. |
| Service state | The current state of the service. |
| MAC Address | Media Access
                                             				Control (MAC) address of the phone. |
| Host name | Unique, fixed
                                             				name that is automatically assigned to the phone based on the MAC address. |
| Phone DN | Directory
                                             				number that is assigned to the phone. |
| App load ID | Application firmware version  that is running on the phone. |
| Boot load ID | Boot firmware version. |
| Version | Identifier of
                                             				the firmware that is running on the phone. |
| Key expansion
                                             				module 1 | Identifier for
                                             				the first key expansion module, if applicable. Applicable to Cisco IP Phone 8851, 8851NR, 8861, 8865, and 8865NR. |
| Key expansion
                                             				module 2 | Identifier for
                                             				the second key expansion module, if applicable. Applicable to Cisco IP Phone 8851, 8851NR, 8861, 8865, and 8865NR. |
| Key expansion
                                             				module 3 | Identifier for
                                             				the third key expansion module, if applicable. Applicable to Cisco IP Phone 8851, 8851NR, 8861, 8865, and 8865NR. |
| Hardware
                                             				revision | Minor revision value of the phone hardware. |
| Serial number | Unique serial
                                             				number of the phone. |
| Model number | Model number
                                             				of the phone. |
| Message
                                             				waiting | Indicates
                                             				whether is a voice message is waiting on the primary line for this phone. |
| UDI | Displays the
                                             				following Cisco Unique Device Identifier (UDI) information about the phone: Device type—Indicates hardware type. For example, phone displays for all phone models. Device description—Displays the name of the phone associated with the indicated model type. Product identifier—Specifies the phone model. Version ID (VID)—Specifies the major hardware version number. Serial number—Displays the unique serial number of the phone. |
| Key expansion
                                             				module UDI | Cisco Unique
                                             				Device Identifier (UDI) of the key expansion module. Applicable to Cisco IP Phone 8851, 8851NR, 8861, 8865, and 8865NR. |
| Name of the Headset | Displays the name of the attached Cisco headset in the left column. The right column contains this information: Port—Displays how the headset connects to the phone. USB AUX Version—Displays the headset firmware version. Radio range—Displays the strength configured for the DECT radio. Applicable to the Cisco Headset 560 Series only. Bandwidth—Displays if the headset uses Wide band or Narrow band. Applicable to the Cisco Headset 560 Series only. Bluetooth—Displays if Bluetooth is enabled or disabled. Applicable to the Cisco Headset 560 Series only. Conference—Displays if the conference feature is enabled or disabled. Applicable to the Cisco Headset 560 Series only. Firmware source—Displays the permitted firmware upgrade method: Restrict to UCM only Allow from UCM or Cisco Cloud Applicable to the Cisco Headset 560 Series only. |
| Time | Time for the
                                             				Date/Time Group to which the phone belongs. This information comes from Cisco
                                             				Unified Communications Manager. |
| Time zone | Time zone for
                                             				the Date/Time Group to which the phone belongs. This information comes from
                                             				Cisco Unified Communications Manager. |
| Date | Date for the
                                             				Date/Time Group to which the phone belongs. This information comes from Cisco
                                             				Unified Communications Manager. |
| System free memory | Amount of unused memory on the phone |
| Java heap free memory | Amount of free internal Java heap memory |
| Java pool free memory | Amount of free internal Java pool memory |
| FIPS mode
                                             				enabled | Indicates if
                                             				the Federal Information Processing Standard (FIPS) Mode is enabled. |

| Note | Some of the items in the following table do not apply to all phone models. |
|---|---|

| Item | Description |
|---|---|
| MAC address | Media Access
                                             				Control (MAC) address of the phone. |
| Host name | Host name that
                                             				the DHCP server assigned to the phone. |
| Domain name | Name of the
                                             				Domain Name System (DNS) domain in which the phone resides. |
| DHCP server | IP address of
                                             				the Dynamic Host Configuration Protocol (DHCP) server from which the phone
                                             				obtains the IP address. |
| BOOTP server | Indicates
                                             				whether the phone obtains the configuration from a Bootstrap Protocol (BootP)
                                             				server. |
| DHCP | Indicates
                                             				whether the phone uses DHCP. |
| IP address | Internet
                                             				Protocol (IPv4) address of the phone. |
| Subnet mask | Subnet mask
                                             				that the phone uses. |
| Default router | Default router
                                             				used that the phone uses. |
| DNS server 1–3 | Primary Domain
                                             				Name System (DNS) server (DNS Server 1) and optional backup DNS servers (DNS
                                             				Server 2 and 3) that the phone uses. |
| Alternate TFTP | Indicates
                                             				whether the phone is using an alternative TFTP server. |
| TFTP server 1 | Primary
                                             				Trivial File Transfer Protocol (TFTP) server used that the phone uses. |
| TFTP server 2 | Backup Trivial
                                             				File Transfer Protocol (TFTP) server used that the phone uses. |
| DHCP address released | Indicates
                                             				the setting of the DHCP address rReleased option on the phone Network
                                             				Configuration menu. |
| Operational VLAN ID | Operational
                                             				Virtual Local Area Network (VLAN) that is configured on a Cisco Catalyst switch
                                             				in which the phone is a member. |
| Admin VLAN ID | Auxiliary VLAN
                                             				in which the phone is a member. |
| CUCM server1–5 | Host names or
                                             				IP addresses, in prioritized order, of the Cisco Unified Communications Manager
                                             				servers with which the phone can register. An item can also show the IP address
                                             				of an SRST router that is capable of providing limited Cisco Unified
                                             				Communications Manager functionality, if such a router is available. For an
                                             				available server, an item shows the Cisco Unified Communications Manager server
                                             				IP address and one of the following states: Active—Cisco Unified
                                                				  Communications Manager server from which the phone is currently receiving
                                                				  call-processing services Standby—Cisco Unified
                                                				  Communications Manager server to which the phone switches if the current server
                                                				  becomes unavailable Blank—No current
                                                				  connection to this Cisco Unified Communications Manager server An item may
                                             				also include the Survivable Remote Site Telephony (SRST) designation, which
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
| Messages URL | URL of the
                                             				server from which the phone obtains message services. |
| Services URL | URL of the
                                             				server from which the phone obtains Cisco Unified IP Phone services. |
| Idle URL | URL that the
                                             				phone displays when the phone is idle for the time that the Idle URL Time field
                                             				specifies and no menu is open. |
| Idle URL time | Number of
                                             				seconds that the phone is idle and no menu is open before the XML service that
                                             				the Idle URL specifies activates. |
| Proxy server URL | URL of proxy
                                             				server, which makes HTTP requests to nonlocal host addresses on behalf of the
                                             				phone HTTP client and provides responses from the nonlocal host to the phone
                                             				HTTP client. |
| Authentication URL | URL that the
                                             				phone uses to validate requests that are made to the phone web server. |
| SW port setup | Speed and
                                             				duplex of the switch port, where: A = Auto Negotiate 10H = 10-BaseT/half
                                                				  duplex 10F = 10-BaseT/full
                                                				  duplex 100H = 100-BaseT/half
                                                				  duplex 100F = 100-BaseT/full
                                                				  duplex 1000F = 1000-BaseT/full
                                                				  duplex No Link= No connection to
                                                				  the switch port |
| PC port setup | Speed and
                                             				duplex of the PC port, where: A = Auto Negotiate 10H = 10-BaseT/half
                                                				  duplex 10F = 10-BaseT/full
                                                				  duplex 100H = 100-BaseT/half
                                                				  duplex 100F = 100-BaseT/full
                                                				  duplex 1000F = 1000-BaseT/full
                                                				  duplex No Link = No connection
                                                				  to the PC port |
| PC port disabled | Indicates
                                             				whether the PC port on the phone is enabled or disabled. |
| User locale | User locale
                                             				that associates with the phone user. Identifies a set of detailed information
                                             				to support users, including language, font, date and time formatting, and
                                             				alphanumeric keyboard text information. |
| Network locale | Network
                                             				locale that associates with the phone user. Identifies a set of detailed
                                             				information to support the phone in a specific location, including definitions
                                             				of the tones and cadences that the phone uses. |
| User locale version | Version of
                                             				the user locale that is loaded on the phone. |
| Network locale version | Version of
                                             				the network locale that is loaded on the phone. |
| Speaker enabled | Indicates
                                             				whether the speakerphone is enabled on the phone. |
| GARP enabled | Indicates
                                             				whether the phone learns MAC addresses from Gratuitous ARP responses. |
| Span to PC port | Indicates
                                             				whether the phone forwards packets that are transmitted and received on the
                                             				network port to the access port. |
| Video capability enabled | Indicates
                                             				whether the phone can participate in video calls when it connects to an
                                             				appropriately equipped camera. |
| Voice VLAN enabled | Indicates
                                             				whether the phone allows a device that is attached to the PC port to access the
                                             				Voice VLAN. |
| PC VLAN enabled | VLAN that
                                             				identifies and removes 802.1P/Q tags from packets that are sent to the PC. |
| Auto line select enabled | Identifies if the phone automatically selects a line when the phone goes off hook. |
| DSCP protocol control | DSCP IP
                                             				classification for call control signaling. |
| DSCP for configuration | DSCP IP
                                             				classification for any phone configuration transfer. |
| DSCP for services | DSCP IP
                                             				classification for phone-based services. |
| Security mode (nonsecure) | Security
                                             				mode that is set for the phone. |
| Web access enabled | Indicates
                                             				whether web access is enabled (Yes) or disabled (No) for the phone. |
| SSH access enabled | Indicates if the SSH port has been enabled or disabled. |
| CDP: SW Port | Indicates
                                             				whether CDP support exists on the switch port (default is enabled). Enable CDP
                                             				on the switch port for VLAN assignment for the phone, power negotiation, QoS
                                             				management, and 802.1x security. Enable CDP
                                             				on the switch port when the phone connects to a Cisco switch. When CDP is
                                             				disabled in Cisco Unified Communications Manager, a warning is presented,
                                             				indicating that CDP should be disabled on the switch port only if the phone
                                             				connects to a non-Cisco switch. The current
                                             				PC and switch port CDP values are shown on the Settings menu. |
| CDP: PC Port | Indicates
                                             				whether CDP is supported on the PC port (default is enabled). When CDP is
                                             				disabled in Cisco Unified Communications Manager, a warning is displays to
                                             				indicate that disabling CDP on the PC port prevents CVTA from working. The current
                                             				PC and switch port CDP values are shown in the Settings menu. |
| LLDP-MED:SW Port | Indicates
                                             				whether Link Layer Discovery Protocol Media Endpoint Discovery (LLDP-MED) is
                                             				enabled on the switch port. |
| LLDP-MED:PC Port | Indicates
                                             				whether LLDP-MED is enabled on the PC port. |
| LLDP Power Priority | Phone power priority to the switch, thus enabling the switch to
                                             				appropriately provide power to the phones. Settings include: Unknown: This is the
                                                				  default value. Low High Critical |
| LLDP Asset ID | Asset ID that is assigned to the phone for inventory management. |
| CTL file | MD5 hash of the CTL file. |
| ITL file | The ITL file contains the initial trust list. |
| ITL signature | MD5 hash of the ITL file |
| CAPF server | CPF server in use |
| TVS | The main component of Security by Default. Trust Verification Services (TVS) enables Cisco Unified IP Phones to authenticate
                                             application servers, such as EM services, directory, and MIDlet, during HTTPS establishment. |
| TFTP server | The name of the TFTP Server used by the phone. |
| TFTP server | The name of the TFTP Server used by the phone. |
| Automatic port synchronization | Indicates if the  phone automatically synchronizes port speed to eliminate packet loss. |
| Switch port remote configuration | Indicates if the SW port is remotely controlled. |
| PC port remote configuration | Indicates if the PC port is remotely controlled. |
| IP addressing mode | Identifies the addressing mode: IPv4 Only IPv4 and IPv6 IPv6 Only |
| IP preference mode control | Indicates the IP address version that the phone uses during signaling with Cisco Unified Communications Manager when both
                                             IPv4 and IPv6 are both available on the phone. |
| IP preference mode for media |  |
| IPv6 auto configuration | Indicates that for media the device uses an IPv4 address to connect to the Cisco Unified Communications Manager. |
| IPv6 duplicate address protection |  |
| IPv6 accept redirect message | Indicates if phone accepts the redirect messages from the same router that is used for the destination number. |
| IPv6 reply multicast echo request | Indicates that the phone sends an Echo Reply message in response to an Echo Request message sent to an IPv6-only address. |
| IPv6 load server | Used to optimize installation time for phone firmware upgrades and off load the WAN by storing images locally, negating the
                                             need to traverse the WAN link for each phone's upgrade. |
| IPv6 log server |  |
| IPv6 CAPF server | Indicates the IP address and port of the remote logging machine to which the phone sends log messages. |
| DHCPv6 | Indicates the method that the phone uses to get the IPv6-only address. When DHCPv6 is enabled, the phone gets the IPv6 address either
                                             from DHCPv6 server or from SLAAC by RA sent by the IPv6-enabled
                                             router. And if DHCPv6 is disabled, the phone will not have any
                                             stateful (from DHCPv6 server) or stateless (from SLAAC) IPv6
                                             address. Note Unlike DHCPv4, even DHCPv6 is disabled the phone can still
                                                         generate a SLAAC address if autoconfigure is enabled. | Note | Unlike DHCPv4, even DHCPv6 is disabled the phone can still
                                                         generate a SLAAC address if autoconfigure is enabled. |
| Note | Unlike DHCPv4, even DHCPv6 is disabled the phone can still
                                                         generate a SLAAC address if autoconfigure is enabled. |
| IPv6 address | Displays the current IPv6-only address of the phone. Two address formats are supported: Eight sets of hexadecimal digits separated by colons X:X:X:X:X:X:X:X Compressed format to collapse a single run of consecutive zero groups into a single group represented by a double colon. |
| IPv6 prefix length | Displays the current IPv6-only prefix length for the subnet. |
| IPv6 default router | Displays the default IPv6 router used by the phone. |
| IPv6 DNS server 1–2 | Displays the primary and secondary DNSv6 server used by the phone |
| IPv6 Alternate TFTP | Displays if an alternate IPv6 TFTP server is used. |
| IPv6 TFTP server 1–2 | Displays the primary and secondary IPv6 TFTP server used by the phone. |
| IPv6 address released | Displays if the user has released the IPv6-related information. |
| EnergyWise power level | The power level that is used when the phone is sleeping. |
| EnergyWise domain | The EnergyWise domain that the phone is in. |
| DF_BIT | Indicates the DF bit setting for packets. |

| Note | Unlike DHCPv4, even DHCPv6 is disabled the phone can still
                                                         generate a SLAAC address if autoconfigure is enabled. |
|---|---|

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
| Rx PacketNoDes | Total number of shed packets that the no Direct Memory Access
                                                   					 (DMA) descriptor causes. |

| Item | Description |
|---|---|
| Rx totalPkt | Total number of packets that the phone received. |
| Rx crcErr | Total number of packets that were received with CRC failed. |
| Rx alignErr | Total number of packets between 64 and 1522 bytes in length
                                                   					 that were received and that have a bad Frame Check Sequence (FCS). |
| Rx multicast | Total number of multicast packets that the phone received. |
| Rx broadcast | Total number of broadcast packets that the phone received. |
| Rx unicast | Total number of unicast packets that the phone received. |
| Rx shortErr | Total number of received FCS error packets or Align error
                                                   					 packets that are less than 64 bytes in size. |
| Rx shortGood | Total number of received good packets that are less than 64
                                                   					 bytes size. |
| Rx longGood | Total number of received good packets that are greater than
                                                   					 1522 bytes in size. |
| Rx longErr | Total number of received FCS error packets or Align error
                                                   					 packets that are greater than 1522 bytes in size. |
| Rx size64 | Total number of received packets, including bad packets, that
                                                   					 are between 0 and 64 bytes in size. |
| Rx size65to127 | Total number of received packets, including bad packets, that
                                                   					 are between 65 and 127 bytes in size. |
| Rx size128to255 | Total number of received packets, including bad packets, that
                                                   					 are between 128 and 255 bytes in size. |
| Rx size256to511 | Total number of received packets, including bad packets, that
                                                   					 are between 256 and 511 bytes in size. |
| Rx size512to1023 | Total number of received packets, including bad packets, that
                                                   					 are between 512 and 1023 bytes in size. |
| Rx size1024to1518 | Total number of received packets, including bad packets, that
                                                   					 are between 1024 and 1518 bytes in size. |
| Rx tokenDrop | Total number of packets that were dropped due to lack of
                                                   					 resources (for example, FIFO overflow). |
| Tx excessDefer | Total number of packets that were delayed from transmitting
                                                   					 due to busy medium. |
| Tx lateCollision | Number of times that collisions occurred later than 512 bit
                                                   					 times after the start of packet transmission. |
| Tx totalGoodPkt | Total number of good packets (multicast, broadcast, and
                                                   					 unicast) that the phone received. |
| Tx Collisions | Total number of collisions that occurred while a packet was
                                                   					 transmitted. |
| Tx excessLength | Total number of packets that were not transmitted because the
                                                   					 packet experienced 16 transmission attempts. |
| Tx broadcast | Total number of broadcast packets that the phone transmitted. |
| Tx multicast | Total number of multicast packets that the phone transmitted. |
| LLDP FramesOutTotal | Total number of LLDP frames that the phone sent out. |
| LLDP AgeoutsTotal | Total number of LLDP frames that timed out in the cache. |
| LLDP FramesDiscardedTotal | Total number of LLDP frames that were discarded when any of
                                                   					 the mandatory TLVs is missing, out of order, or contains out of range string
                                                   					 length. |
| LLDP FramesInErrorsTotal | Total number of LLDP frames that were received with one or
                                                   					 more detectable errors. |
| LLDP FramesInTotal | Total number of LLDP frames that the phone receives. |
| LLDP TLVDiscardedTotal | Total number of LLDP TLVs that are discarded. |
| LLDP TLVUnrecognizedTotal | Total number of LLDP TLVs that are not recognized on the
                                                   					 phone. |
| CDP Neighbor Device ID | Identifier of a device connected to this port that CDP
                                                   					 discovered. |
| CDP Neighbor IPv6 address | IP address of the neighbor device discovered that CDP protocol
                                                   					 discovered. |
| CDP Neighbor Port | Neighbor device port to which the phone is connected
                                                   					 discovered by CDP protocol. |
| LLDP Neighbor Device ID | Identifier of a device connected to this port discovered by
                                                   					 LLDP discovered. |
| LLDP Neighbor IPv6 address | IP address of the neighbor device that LLDP protocol
                                                   					 discovered. |
| LLDP Neighbor Port | Neighbor device port to which the phone connects that LLDP
                                                   					 protocol discovered. |
| Port Information | Speed and duplex information. |

| Item | Description |
|---|---|
| Remote address | IP address and UDP port of the destination of the stream. |
| Local address | IP address and UPD port of the phone. |
| Start time | Internal time stamp indicates when Cisco Unified
                                                					 Communications Manager requested that the phone start transmitting packets. |
| Stream status | Indication of whether streaming is active or not. |
| Host name | Unique, fixed name that is automatically assigned to the phone
                                                					 based on the MAC address. |
| Sender packets | Total number of RTP data packets that the phone transmitted
                                                					 since it started this connection. The value is 0 if the connection is set to
                                                					 receive-only mode. |
| Sender octets | Total number of payload octets that the phone transmitted in
                                                					 RTP data packets since it started this connection. The value is 0 if the
                                                					 connection is set to receive-only mode. |
| Sender codec | Type of audio encoding that is for the transmitted stream. |
| Sender reports sent (see note) | Number of times the RTCP Sender Report has been sent. |
| Sender report time sent (see note) | Internal time-stamp indication as to when the last RTCP Sender
                                                					 Report was sent. |
| Rcvr lost packets | Total number of RTP data packets that have been lost since
                                                					 data reception started on this connection. Defined as the number of expected
                                                					 packets less the number of packets actually received, where the number of
                                                					 received packets includes any that are late or are duplicates. The value
                                                					 displays as 0 if the connection was set to send-only mode. |
| Avg jitter | Estimate of mean deviation of the RTP data packet interarrival
                                                					 time, measured in milliseconds. The value displays as 0 if the connection was
                                                					 set to send-only mode. |
| Receiver codec | Type of audio encoding that is used for the received stream. |
| Receiver reports sent (see note) | Number of times the RTCP Receiver Reports have been sent. |
| Receiver report time sent (see note) | Internal time-stamp indication as to when a RTCP Receiver
                                                					 Report was sent. |
| Rcvr packets | Total number of RTP data packets that the phone has received
                                                					 since data reception started on this connection. Includes packets that were
                                                					 received from different sources if this call is a multicast call. The value
                                                					 displays as 0 if the connection was set to send-only mode. |
| Rcvr octets | Total number of payload octets that the device received in RTP
                                                					 data packets since reception started on the connection. Includes packets that
                                                					 were received from different sources if this call is a multicast call. The
                                                					 value displays as 0 if the connection was set to send-only mode. |
| MOS LQK | Score that is an objective estimate of the mean opinion score
                                                					 (MOS) for listening quality (LQK) that rates from 5 (excellent) to 1(bad).
                                                					 This score is based on audible concealment events that are to frame loss in the
                                                					 preceding eight-second interval of the voice stream. For more information, see Voice Quality Monitoring . Note The MOS LQK score can vary due to the codec type that the
                                                            						Cisco Unified IP Phone uses. | Note | The MOS LQK score can vary due to the codec type that the
                                                            						Cisco Unified IP Phone uses. |
| Note | The MOS LQK score can vary due to the codec type that the
                                                            						Cisco Unified IP Phone uses. |
| Avg MOS LQK | Average MOS LQK score that was observed for the entire voice
                                                					 stream. |
| Min MOS LQK | Lowest MOS LQK score that was observed from the start of the
                                                					 voice stream. |
| Max MOS LQK | Baseline or highest MOS LQK score that was observed from start
                                                					 of the voice stream. These codecs provide the following maximum MOS LQK score under
                                                					 normal conditions with no frame loss: G.711 yields 4.5. G.729 A /AB yields
                                                   						3.7. |
| MOS LQK version | Version of the Cisco proprietary algorithm that is used to
                                                					 calculate MOS LQK scores. |
| Cumulative conceal ratio | Total number of concealment frames divided by total number of
                                                					 speech frames that were received from the start of the voice stream. |
| Interval conceal ratio | Ratio of concealment frames to speech frames in the preceding
                                                					 3-second interval of active speech. If voice activity detection (VAD) is in
                                                					 use, a longer interval might be required to accumulate three seconds of active
                                                					 speech. |
| Max conceal ratio | Highest interval concealment ratio from the start of the voice
                                                					 stream. |
| Conceal secs | Number of seconds that have concealment events (lost frames)
                                                					 from the start of the voice stream (includes severely concealed seconds). |
| Severely conceal secs | Number of seconds that have more than five percent concealment
                                                					 events (lost frames) from the start of the voice stream. |
| Latency (see note) | Estimate of the network latency, expressed in milliseconds.
                                                					 Represents a running average of the round-trip delay, measured when RTCP
                                                					 receiver report blocks are received. |
| Max jitter | Maximum value of instantaneous jitter, in milliseconds. |
| Sender size | RTP packet size, in milliseconds, for the transmitted stream. |
| Sender reports received (see note) | Number of times RTCP Sender Reports have been received. |
| Sender report time received (see note) | Most recent time when an RTCP Sender Report was received. |
| Receiver size | RTP packet size, in milliseconds, for the received stream. |
| Receiver discarded | RTP packets that were received from the network but were
                                                					 discarded from the jitter buffers. |
| Receiver reports received (see note) | Number of times RTCP Receiver Reports have been received. |
| Receiver report time received (see note) | Most recent time when an RTCP Receiver Report was received. |
| Rcvr encrypted | Indicates if the receiver  is using encryption. |
| Sender encrypted | Indicates if the sender is using encryption. |
| Sender frames | Number of frames sent. |
| Sender partial frames | Number of partial frames sent. |
| Sender i frames | Number of I frames sent. I frames are used in video transmission. |
| Sender IDR frames | Number of instantaneous decoder refresh (IDR) frames sent. IDR frames are used in video transmission. |
| Sender frame rate | Rate at which the sender is sending frames. |
| Sender bandwidth | Bandwidth for the sender. |
| Sender resolution | Video resolution of the sender. |
| Rcvr frames | Number of frames received |
| Rcvr partial frames | Number of partial frames received |
| Rcvr i frames | Number of I frames received. |
| Rcvr IDR frames | Number of IDR frames received. |
| Rcvr IFrames req | Number of requested IDR frames received |
| Rcvr frame rate | Rate at which the receiver is receiving frames. |
| Rcvr frames lost | Number of frames that were not received. |
| Rcvr frame errors | Number of frames that were not received. |
| Rcvr bandwidth | Bandwidth of the receiver. |
| Rcvr resolution | Video resolution of the receiver. |
| Domain | Domain that the phone resides in. |
| Sender joins | Number of times the sender joined. |
| Rcvr joins | Number of times the receiver joined |
| Byes | Number of "Bye" frames |
| Sender start time | Time that the sender started. |
| Rcvr start time | Time that the receiver started. |
| Row status | Whether the phone is streaming |
| Sender tool | Type of audio encoding used for the stream |
| Sender reports | RTCP Sender Reports |
| Sender report time | Last time at which an RTCP Sender Report was sent. |
| Rcvr Jitter | Maximum jitter of stream |
| Receiver tool | Type of audio encoding used for the stream |
| Rcvr reports | Number of times this streaming statistics report has been accessed from the web page. |
| Rcvr report time | Internal time stamp indicating when this streaming statistics report was generated |
| Is video | Indicates if the call was a video call or audio only. |
| Call ID | Identification of the call |
| Group ID | Identification of the group that the phone is in. |

| Note | The MOS LQK score can vary due to the codec type that the
                                                            						Cisco Unified IP Phone uses. |
|---|---|

| Note | When the RTP Control Protocol is disabled, no data generates for
                                                			 this field and thus displays as 0. |
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