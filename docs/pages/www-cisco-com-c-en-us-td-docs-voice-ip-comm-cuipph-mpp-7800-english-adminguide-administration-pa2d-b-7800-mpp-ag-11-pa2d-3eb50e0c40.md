---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7800-english-adminguide-administration-pa2d-b-7800-mpp-ag-11-pa2d-3eb50e0c40
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7800/english/adminguide/administration/pa2d_b_7800-mpp-ag-11/pa2d_b_7800-mpp-ag-11_chapter_01111.html
retrieved_at: 2026-09-01T15:41:45.720785+00:00
---

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

# Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

Updated: April 29, 2019

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

## Include a Device Identifier in Uploaded Syslog Messages

You can choose to include a device identifier in syslog messages that are uploaded to the syslog server. While the IP address
                              of a phone may change over time, the device identifier does not change. This can ease the process of identifying the source
                              of each message in a stream of incoming messages from multiple phones. The device identifier appears after the timestamp in
                              each message.

### Before you begin

On the phone administration web page, go to Voice > System > Optional Network Configuration .

Configure the Syslog Identifier parameter as described in Optional Network Configuration .

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

Press Applications .

Select Status > Product Information .

When a user password is set, a corresponding icon (lock or certificate) displays at the top-right corner of the phone screen.

To exit the Model Information screen, press Back .

### View the Phone Status

Press Applications .

Select Status > Phone Status > Phone Status .

You can view the following information:

Elapsed time —Total time elapsed since the last reboot of the system

Tx (Packets) —Transmitted packets from the phone.

Rx (Packets) —Received packets from the phone.

### View the Status Messages on the Phone

Press Applications .

Select Status > Status messages .

You can view a log of the various phone statuses since provisioning was last done.

Status messages reflect UTC time and are not affected by the timezone settings on the phone.

Press Back .

### View the Network Status

Press Applications .

Select Status > Network Status .

You can view the following information:

Network type —Indicates the type of Local Area Netwrok (LAN) connection that the phone uses.

Network status —Indicates if the phone is connected to a network.

IPv4 status —IP address of the phone. You can see information on IP address, Addressing type, IP status, Subnet mask, Default router,
                                                   Domain Name Server (DNS) 1, DNS 2 of the phone.

IPv6 status —IP address of the phone. You can see information on IP address, Addressing type, IP status, Subnet mask, Default router,
                                                   Domain Name Server (DNS) 1, DNS 2 of the phone.

VLAN ID —VLAN ID of the phone.

MAC address —Unique Media Access Control (MAC) address of the phone.

Host name —Displays the current host name assigned to the phone.

Domain —Displays the network domain name of the phone. Default: cisco.com

Switch port link —Status of the switch port.

Switch port config —Indicates speed and duplex of the network port.

PC port config —Indicates speed and duplex of the PC port.

PC port link —Indicates speed and duplex of the PC port.

### Display Call Statistics Window

You can access the Call Statistics screen on the phone to display counters, statistics, and voice-quality metrics of the most
                                 recent call.

You can also remotely view the call statistics information by using a web browser to access the Streaming Statistics web page.
                                             This web page contains additional RTCP statistics that are not available on the phone.

A single call can use multiple voice streams, but data is captured for only the last voice stream. A voice stream is a packet
                                 stream between two endpoints. If one endpoint is put on hold, the voice stream stops even though the call is still connected.
                                 When the call resumes, a new voice packet stream begins, and the new call data overwrites the former call data.

To display the Call Statistics screen for information about the latest voice stream, follow these steps:

Press Applications .

Select Status > Phone Status > Call Statistics .

Press Back .

#### Call Statistics Fields

The following table describes the items on the Call Statistics screen.

Item

Description

Receiver Codec

G.729

G.722

G.711 mu-law

G.711 A-law

OPUS

iLBC

Sender Codec

G.729

G.722

G.711 mu-law

G.711 A-law

OPUS

iLBC

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

### View the Customization State in the Configuration Utility

After the RC download from the EDOS server completes, you can view the customization state of a phone using the web interface.

Here are the descriptions of the remote customization states:

Open—The phone has booted for the first time and is not configured.

Aborted—Remote customization is aborted due to other Provisioning like DHCP options.

Pending—The profile has been downloaded from the EDOS server.

Custom-Pending—The phone has downloaded a redirect URL from the EDOS server.

Acquired—In the profile downloaded from the EDOS server, there is a redirect URL for provision configuration. If the redirect
                                       URL download from the provisioning server is successful, this state is displayed.

Unavailable—Remote customization has stopped because the EDOS server responded with an empty provisioning file and the HTTP
                                       response was 200 OK .

On the Phone Web page, select Admin Login > Info > Status .

In the Product Information section, you can view the customization state of the phone in the Customization field.

If any provisioning is failing, you can view the details in the Provisioning Status section on the same page.

## Cisco IP Phone Web Page

This section describes the information that you can obtain from the phone web page. You can use this information to remotely
                              monitor the operation of a phone and to assist with troubleshooting.

### Info

The fields on this tab are read-only and cannot be edited.

Status

#### System Information

Parameter

Description

Host Name

Displays the current host name assigned to the phone.

Domain

Displays the network domain name of the phone.

Default: cisco.com

Primary NTP Server

Displays the primary NTP server assigned to the phone.

Secondary NTP Server

Displays the secondary NTP server assigned to the phone.

#### IPv4 Information

Parameter

Description

IP Status

Indicates that the connection is established.

Connection Type

Indicates the type of internet connection for the phone:

DHCP

Static IP

Current IP

Displays the current IP address assigned to the IP phone.

Current Netmask

Displays the network mask assigned to the phone.

Current Gateway

Displays the default router assigned to the phone.

Primary DNS

Displays the primary DNS server assigned to the phone.

Secondary DNS

Displays the secondary DNS server assigned to the phone.

#### IPv6 Information

Parameter

Description

IP Status

Indicates that the connection is established.

Connection Type

Indicates the type of internet connection for the phone:

Static IP

DHCP

Current IP

Displays the current IPv6 address assigned to the IP phone.

Prefix Length

Identifies number of bits of a global unicast IPv6 address that are part of`the network. For example, if the IPv6 address
                                                is 2001:0DB8:0000:000b::/64, the number 64 identifies that the first 64 bits are part of the network.

Current Gateway

Displays the default router assigned to the phone.

Primary DNS

Displays the primary DNS server assigned to the phone.

Secondary DNS

Displays the secondary DNS server assigned to the phone.

#### Reboot History

For information about reboot history, see Reboot Reasons .

#### Product Information

Parameter

Description

Product Name

Model number of the phone.

Software Version

Version number of the phone firmware.

MAC Address

Hardware address of the phone.

Customization

For an RC unit, this field indicates whether the unit has been customized or not. Pending indicates a new RC unit that is
                                                ready for provisioning. If the unit has already retrieved its customized profile, this field displays the name of the company
                                                that provisioned the unit.

Serial Number

Serial number of the phone.

Hardware Version

Version number of the phone hardware.

Client Certificate

Status of the client certificate, which authenticates the phone for use in the ITSP network. This field indicates if the client
                                                certificate is properly installed in the phone.

#### Downloaded Locale Package

Parameter

Description

Locale download status

Displays the downloaded locale package status.

Locale download URL

Displays the location from where the local package is downloaded.

Font download status

Displays the downloaded font file status.

Font download URL

Displays the location from where the font file is downloaded.

#### Phone Status

Parameter

Description

Current Time

Current date and time of the system; for example, 08/06/14 1:42:56 a.m.

Elapsed Time

Total time elapsed since the last reboot of the system; for example, 7 days, 02:13:02.

SIP Messages Sent

Total number of SIP messages sent (including retransmissions).

SIP Bytes Sent

Total number of SIP messages received (including retransmissions).

SIP Messages Recv

Total number of bytes of SIP messages sent which includes retransmissions.

SIP Bytes Recv

Total number of bytes of SIP messages received (including retransmissions).

Network Packets Sent

Total number of network packets sent.

Network Packets Recv

Total number of network packets received.

External IP

External IP of the phone.

Operational VLAN ID

ID of the VLAN currently in use if applicable.

SW Port

Displays the type of Ethernet connection from the IP phone to the switch.

PC Port

Displays the type of Ethernet connection from PC Port.

Upgrade Status

Displays status of the last phone upgrade.

SW Port Config

Displays the type of SW port configuration.

PC Port Config

Displays the type of PC port configuration.

Last Successful Login

Displays the time when the phone has last successful log in.

Last Failed Login

Displays the time when the phone has last failed log in.

#### Dot1x Authentication

Parameter

Description

Transaction status

Indicates if the phone is authenticated.

Protocol

Displays the protocol of the registered phone.

#### Ext Status

Parameter

Description

Registration State

Shows “Registered” if the phone is registered, or “Not Registered” if the phone is not registered to the ITSP.

Last Registration At

Last date and time the line was registered.

Next Registration In Seconds

Number of seconds before the next registration renewal.

Message Waiting

Indicates whether message waiting is enabled or disabled.

Mapped SIP Port

Port number of the SIP port mapped by NAT.

Hoteling State

Indicates whether Hoteling is enabled or disabled.

Extended Function Status

Indicates whether extended function is enabled.

#### Line Call Status

Parameter

Description

Call State

Status of the call.

Tone

Type of tone that the call uses.

Encoder

Codec used for encoding.

Decoder

Codec used for decoding.

Type

Direction of the call.

Remote Hold

Indicates whether the far end placed the call on hold.

Callback

Indicates whether the call was triggered by a call back request.

Mapped RTP Port

The port mapped for Real Time Protocol traffic for the call.

Peer Name

Name of the internal phone.

Peer Phone

Phone number of the internal phone.

Duration

Duration of the call.

Packets Sent

Number of packets sent.

Packets Recv

Number of packets received.

Bytes Sent

Number of bytes sent.

Bytes Recv

Number of bytes received.

Decode Latency

Number of milliseconds for decoder latency.

Jitter

Number of milliseconds for receiver jitter.

Round Trip Delay

Number of milliseconds for delay in the RTP-to-RTP interface round trip.

Packets Lost

Number of packets lost.

Loss Rate

The fraction of RTP data packets from the source lost since the beginning of reception. Defined in RFC-3611—RTP Control Protocol
                                                Extended Reports (RTCP XR).

Packet Discarded

The fraction of RTP data packets from the source lost since the beginning of reception. Defined in RFC-3611—RTP Control Protocol
                                                Extended Reports (RTCP XR).

Discard Rate

The fraction of RTP data packets from the source that have been discarded since the beginning of reception, due to late or
                                                early arrival, under-run or overflow at the receiving jitter buffer. Defined in RFC-3611—RTP Control Protocol Extended Reports
                                                (RTCP XR).

Burst Duration

The mean duration, expressed in milliseconds, of the burst periods that have occurred since the beginning of reception. Defined
                                                in RFC-3611—RTP Control Protocol Extended Reports (RTCP XR).

Gap Duration

The mean duration, expressed in milliseconds, of the gap periods that have occurred since the beginning of reception. Defined
                                                in RFC-3611—RTP Control Protocol Extended Reports (RTCP XR).

R-Factor

Voice quality metric that describes the segment of the call that is carried over this RTP session. Defined in RFC-3611—RTP
                                                Control Protocol Extended Reports (RTCP XR).

MOS-LQ

The estimated mean opinion score for listening quality (MOS-LQ) is a voice quality metric on a scale from 1 to 5, in which
                                                5 represents excellent and 1 represents unacceptable. Defined in RFC-3611—RTP Control Protocol Extended Reports (RTCP XR).

MOS-CQ

The estimated mean opinion score for conversational quality (MOS-CQ) is defined as including the effects of delay and other
                                                effects that affect conversational quality. Defined in RFC-3611—RTP Control Protocol Extended Reports (RTCP XR).

#### Paging Status

Parameter

Description

Multicast Rx Pkts

Indicates Rx packets during a multicast paging.

Multicast Tx Pkts

Indicates Tx packets during a multicast paging.

#### TR-069 Status

Parameter

Description

TR-069 Feature

Indicates if TR-069 function is enabled or disabled.

Periodic Inform Time

Displays the inform time interval from CPE to ACS.

Last Inform Time

Indicates the last inform time.

Last Transaction Status

Displays the success or the failure status.

Last Session

Indicates the start and end time of the session.

ParameterKey

Displays the key for reference checkpoint for parameter set configured.

#### PRT Status

Parameter

Description

PRT Generation Status

The location of initiation and status of generation of the most recently initiated problem report.

Problem reports may be initiated from the phone LCD user interface, from the phone administration web page, or remotely. See Report All Phone Issues from the Phone Web Page and Report a Phone Problem Remotely for details.

XML tag in status.xml : PRT_Generation_Status

PRT Upload Status

The status of upload of the most recently initiated problem report.

See Configure PRT Upload for information on configuring an upload rule for problem reports.

XML tag in status.xml : PRT_Upload_Status

#### Custom CA Status

These fields display the status of provisioning using a custom Certificate Authority (CA).

Parameter

Description

Custom CA Provisioning Status

Indicates whether provisioning using a custom CA succeeded or failed:

Last provisioning succeeded on mm/dd/yyyy HH:MM:SS;

Last provisioning failed on mm/dd/yyyy HH:MM:SS

Custom CA Info

Displays information about the custom CA:

Installed—Displays the "CN Value" , where "CN Value" is the value of the CN parameter for the Subject field in the first certificate.

Not Installed—Displays if no custom CA certificate is installed.

Custom CA certificates are configured in the Provisioning tab. For more information about custom CA certificates, see the Cisco IP Phone 7800 Series Multiplatform Phones Provisioning Guide .

#### Provisioning Status

Parameter

Description

Provisioning Profile

Displays the profile file name of the phone.

Provisioning Status 1

Displays the provisioning status (resync) of the phone.

Provisioning Status 2

Provisioning Status 3

Provisioning Failure Reason

Displays the reason for the failure of provisioning of the phone.

The Upgrade and Provisioning Status are displayed in reverse chronological order (like reboot history). Each entry gives the
                                                status, time, and reason.

Debug Info

#### Console Logs

Displays the syslog output of the phone in the reverse order, where messages is the latest one. The display includes hyperlinks
                                    to individual log files. The console log files include debug and error messages received on the phone and the time stamp reflects
                                    UTC time, regardless of the time zone settings.

Parameter

Description

Debug Message

Displays debug messages when you click messages link.

#### Problem Reports

Parameter

Description

Report Problem

Displays the tab Generate PRT.

Prt file

Displays the file name of the PRT logs.

Packet Capture

Displays the tab Start Packet Capture . Click this tab to initiate capture packets. Click All to capture all packets that the phone receives or click Host IP Address to capture packets only when src/dest is the IP address of the phone.

You can also stop the capture process after initiating it.

Capture File

Displays the file that contains the captured packets. Download the file to see the packet details.

#### Factory Reset

Parameter

Description

Factory Reset

Resets the phone when you click Factory Reset tab when the phone is idle.

Download Status

#### Firmware Upgrade Status

Parameter

Description

Firmware Upgrade Status 1

Displays the upgrade status (failed or succeeded) with reason for the same.

Firmware Upgrade Status 2

Firmware Upgrade Status 3

#### Provisioning Status

Parameter

Description

Provisioning Status 1

Displays the provisioning status (resync) of the phone.

Provisioning Status 2

Provisioning Status 3

#### Custom CA Status

Parameter

Description

Custom CA Provisioning Status

Indicates whether provisioning using a custom CA succeeded or failed:

Last provisioning succeeded on mm/dd/yyyy HH:MM:SS;

Last provisioning failed on mm/dd/yyyy HH:MM:SS

Custom CA Info

Displays information about the custom CA:

Installed—Displays the "CN Value" , where "CN Value" is the value of the CN parameter for the Subject field in the first certificate.

Not Installed—Displays if no custom CA certificate is installed.

Network Statistics

#### Ethernet Information

Parameter

Description

TxFrames

Total number of packets that the phone transmitted.

TxBroadcasts

Total number of broadcast packets that the phone transmitted.

TxMulticasts

Total number of multicast packets that the phone transmitted.

TxUnicasts

Total number of unicast packets that the phone transmitted.

RxFrames

Total number of packets received by the phone.

RxBroadcasts

Total number of broadcast packets that the phone received.

RxMulticasts

Total number of multicast packets that the phone received.

RxUnicasts

Total number of unicast packets that the phone received.

#### Network Port Information

Parameter

Description

RxtotalPkt

Total number of packets that the phone received.

Rxunicast

Total number of unicast packets that the phone received.

Rxbroadcast

Total number of broadcast packets that the phone received.

Rxmulticast

Total number of multicast packets that the phone received.

RxDropPkts

Total number of packets dropped.

RxUndersizePkts

The total number of packets received that are less than 64 octets long, which excludes framing bits, but includes FCS octets,
                                             and are otherwise well formed.

RxOversizePkts

The total number of packets received that are longer than 1518 octets, which excludes framing bits, but includes FCS octets,
                                             and are otherwise well formed.

RxJabbers

The total number of packets received that are longer than 1518 octets, which excludes framing bits, but incudes FCS octets,
                                             and do not end with an even number of octets (alignment error), or had an FCS error.

RxAlignErr

Total number of packets between 64 and 1522 bytes in length that were received and that had a bad Frame Check Sequence (FCS).

Rxsize64

Total number of received packets, including bad packets, that were between 0 and 64 bytes in size.

Rxsize65to127

Total number of received packets, including bad packets, that were between 65 and 127 bytes in size.

Rxsize128to255

Total number of received packets, including bad packets, that were between 128 and 255 bytes in size.

Rxsize256to511

Total number of received packets, including bad packets, that were between 256 and 511 bytes in size.

Rxsize512to1023

Total number of received packets, including bad packets, that were between 512 and 1023 bytes in size.

Rxsize1024to1518

Total number of received packets, including bad packets, that were between 1024 and 1518 bytes in size.

TxtotalGoodPkt

Total number of good packets (multicast, broadcast, and unicast) that the phone received.

lldpFramesOutTotal

Total number of LLDP frames that the phone sent out.

lldpAgeoutsTotal

Total number of LLDP frames that timed out in the cache.

lldpFramesDiscardedTotal

Total number of LLDP frames that were discarded when any of the mandatory TLVs is missing, out of order, or contains out of
                                             range string length.

lldpFramesInErrorsTotal

Total number of LLDP frames that were received with one or more detectable errors.

lldpFramesInTotal

Total number of LLDP frames that the phone received.

lldpTLVDiscardedTotal

Total number of LLDP TLVs that were discarded.

lldpTLVUnrecognizedTotal

Total number of LLDP TLVs that were not recognized on the phone.

CDPNeighborDeviceId

Identifier of a device connected to this port that CDP discovered.

CDPNeighborIP

IP address of the neighbor device discovered that CDP discovered.

CDPNeighborPort

Neighbor device port to which the phone is connected discovered by CDP.

LLDPNeighborDeviceId

Identifier of a device connected to this port discovered by LLDP discovered.

LLDPNeighborIP

IP address of the neighbor device that LLDP discovered.

LLDPNeighborPort

Neighbor device port to which the phone connects that LLDP discovered.

PortSpeed

Speed and duplex information.

#### Access Port Information

Parameter

Description

RxtotalPkt

Total number of packets that the phone received.

Rxunicast

Total number of unicast packets that the phone received.

Rxbroadcast

Total number of broadcast packets that the phone received.

Rxmulticast

Total number of multicast packets that the phone received.

RxDropPkts

Total number of packets dropped.

RxUndersizePkts

The total number of packets received that are less than 64 octets long, which excludes framing bits, but includes FCS octets,
                                             and are otherwise well formed.

RxOversizePkts

The total number of packets received that are longer than 1518 octets, which excludes framing bits, but includes FCS octets,
                                             and are otherwise well formed.

RxJabbers

The total number of packets received that are longer than 1518 octets, which excludes framing bits, but incudes FCS octets,
                                             and do not end with an even number of octets (alignment error), or had an FCS error.

RxAlignErr

Total number of packets between 64 and 1522 bytes in length that were received and that had a bad Frame Check Sequence (FCS).

Rxsize64

Total number of received packets, including bad packets, that were between 0 and 64 bytes in size.

Rxsize65to127

Total number of received packets, including bad packets, that were between 65 and 127 bytes in size.

Rxsize128to255

Total number of received packets, including bad packets, that were between 128 and 255 bytes in size.

Rxsize256to511

Total number of received packets, including bad packets, that were between 256 and 511 bytes in size.

Rxsize512to1023

Total number of received packets, including bad packets, that were between 512 and 1023 bytes in size.

Rxsize1024to1518

Total number of received packets, including bad packets, that were between 1024 and 1518 bytes in size.

TxtotalGoodPkt

Total number of good packets (multicast, broadcast, and unicast) that the phone received.

lldpFramesOutTotal

Total number of LLDP frames that the phone sent out.

lldpAgeoutsTotal

Total number of LLDP frames that timed out in the cache.

lldpFramesDiscardedTotal

Total number of LLDP frames that were discarded when any of the mandatory TLVs is missing, out of order, or contains out of
                                             range string length.

lldpFramesInErrorsTotal

Total number of LLDP frames that were received with one or more detectable errors.

lldpFramesInTotal

Total number of LLDP frames that the phone received.

lldpTLVDiscardedTotal

Total number of LLDP TLVs that were discarded.

lldpTLVUnrecognizedTotal

Total number of LLDP TLVs that were not recognized on the phone.

CDPNeighborDeviceId

Identifier of a device connected to this port that CDP discovered.

CDPNeighborIP

IP address of the neighbor device discovered that CDP discovered.

CDPNeighborPort

Neighbor device port to which the phone is connected discovered by CDP.

LLDPNeighborDeviceId

Identifier of a device connected to this port discovered by LLDP discovered.

LLDPNeighborIP

IP address of the neighbor device that LLDP discovered.

LLDPNeighborPort

Neighbor device port to which the phone connects that LLDP discovered.

PortSpeed

Speed and duplex information.

### Voice

System

#### System Configuration

Parameter

Description

Restricted Access Domains

This feature is used when implementing software customization.

Enable Web Server

Enable/disable web server of the IP phone.

Default: Yes

Enable Protocol

Choose the type of protocol:

Http

Https

If you specify the HTTPS protocol, you must include https: in the URL.

Default: Http

Enable Direct Action Url

Enables the direct action of the URL.

Default: Yes

Session Max Timeout

Allows you to enter maximum timeout of the session.

Default: 3600

Session Idle Timeout

Allows you to enter idle timeout of the session.

Default: 3600

Web Server Port

Allows you to enter port number of the phone web user interface.

Default: 80

80 for protocol HTTP.

443 for protocol HTTPS.

If you specify a port number other than the default value for that protocol, you must include the nondefault port number in
                                                the server URL.

Example: https://192.0.2.1:999/admin/advanced

Enable Web Admin Access

Allows you to enable or disable local access to the phone web user interface. Select Yes or No from the drop-down menu.

Default: Yes

Admin Password

Allows you to enter password for the administrator.

Default: Blank

User Password

Allows you to enter password for the user.

Default: Blank

Phone-UI-readonly

Allows you to make the phone menus and options that the phone users see as read-only fields.

Default: No

Phone-UI-User-Mode

Allows you to restrict the menus and options that phone users see when they use the phone interface. Choose yes to enable
                                                this parameter and restrict access.

Default: No

Specific parameters are then designated as "na" , "ro" , or "rw" using provisioning files. Parameters designated as "na" don't appear on the phone screen. Parameters designated as "ro" aren't editable by the user. Parameters designated as "rw" are editable by the user.

Block Nonproxy SIP

Enables or disables the phone receiving SIP messages from non-proxy server. If you choose Yes , the phone blocks any incoming non-proxy SIP messages except IN-dialog message. If you choose No , the phone does not block any incoming non-proxy SIP messages.

Set Block Nonproxy SIP to No for phones that use TCP or TLS to transport SIP messages. Nonproxy SIP messages transported over TCP or TLS are blocked
                                                by default.

Default: No

#### Network Settings

Parameter

Description

IP Mode

Allows you to select the internet protocol mode in which the phone operates. Options are: IPv4 Only, IPv6 Only, and Dual Mode.
                                                In dual mode, the phone can have both IPv4 and IPv6 addresses.

Default: Dual Mode

#### IPv4 Settings

Parameter

Description

Connection Type

Internet connection type that is configured for the phone. Options are DHCP and Static IP.

Default: DHCP

NetMask

Subnet mask of the phone.

Static IP

IP address of the phone.

Gateway

IP address of the gateway.

Primary DNS

Primary Domain Name Server (DNS) assigned to the phone.

Secondary DNS

Secondary Domain Name Server (DNS) if assigned to the phone.

#### IPv6 Settings

Parameter

Description

Connection Type

Internet connection type that is configured for the phone. Options are DHCP and Static IP.

Default: DHCP

Static IP

IPv6 address of the phone.

Prefix Length

Identifies number of bits of a global unicast IPv6 address that are part of`the network. For example, if the IPv6 address
                                                is 2001:0DB8:0000:000b::/64, the number 64 identifies that the first 64 bits are part of the network.

Gateway

IP address of the gateway.

Primary DNS

Primary Domain Name Server (DNS) assigned to the phone.

Secondary DNS

Secondary Domain Name Server (DNS) if assigned to the phone.

Broadcast Echo

Options are Disabled and Enabled.

Default: Disabled

Auto Config

When enabled, phone generates an IPv6 address by default with the prefix length sent from the router. Options are Disabled
                                                and Enabled.

Default: Enabled

#### 802.1X Authentication

Parameter

Description

Enable 802.1X Authentication

Enables/disables 802.1X

Default: No

#### Optional Network Configuration

Parameter

Description

Host Name

The hostname of the Cisco IP Phone.

Domain

The network domain of the Cisco IP Phone.

If you are using LDAP, see LDAP Configuration .

DNS Server Order

Specifies the method for selecting the DNS server:

Manual, DHCP

Manual

DHCP,Manual

DNS Query Mode

Specified mode of DNS query.

Parallel

Sequential

DNS Caching Enable

When set to Yes, the DNS query results are not cached.

Default: Yes

Switch Port Config

Allows you to select speed and duplex of the network port. Values are:

Auto

10MB half

10MB full

100 MB half

100MB full

100 half

1000 full

PC Port Config

Allows you to select Speed and duplex of the Computer (access) port.

Auto

10MB half

10MB full

100 MB half

100MB full

100 half

1000 full

PC PORT Enable

Specifies if PC port is enabled. Options are Yes or No.

Enable PC Port Mirror

Adds the ability to port mirror on the PC port. When enabled, you can see the packets on the phone. Select Yes to enable PC port mirroring and select No to disable it.

Syslog Server

Specify the syslog server name and port. This feature specifies the server for logging IP phone system information and critical
                                                events. If both Debug Server and Syslog Server are specified, Syslog messages are also logged to the Debug Server.

Syslog Identifier

Select the device identifier to include in syslog messages that are uploaded to the syslog server. The device identifier appears
                                                after the timestamp in each message.

None: No device identifier.

$MA: The MAC address of the phone, expressed as continuous lower case letters and digits. Example: c4b9cd811e29

$MAU: The MAC address of the phone, expressed as continuous upper case letters and digits. Example: C4B9CD811E29

$MAC: The MAC address of the phone in the standard colon-separated format. Example: c4:b9:cd:81:1e:29

$SN: The product serial number of the phone.

Default: None

Example XML configuration:

```
<Syslog_Identifier ua="na">$MAC</Syslog_Identifier>
```

Debug Level

The debug level from 0 to 2. The higher the level, the more debug information is generated. Zero (0) means that no debug information
                                                is generated. To log SIP messages, you must set the Debug Level to at least 2.

Default: 0

Primary NTP Server

IP address or name of the primary NTP server used to synchronize its time.

Default: Blank

Secondary NTP Server

IP address or name of the secondary NTP server used to synchronize its time.

Default: Blank

Enable SSLv3

Choose Yes to enable SSLv3. Choose No to disable.

Default: No

#### VLAN Settings

Parameter

Description

Enable VLAN

Choose Yes to enable VLAN. Choose No to disable.

Enable CDP

Enable CDP only if you are using a switch that has Cisco Discovery Protocol. CDP is negotiation based and determines which
                                                VLAN the IP phone resides in.

Enable LLDP-MED

Choose Yes to enable LLDP-MED for the phone to advertise itself to devices that use that discovery protocol.

When the LLDP-MED feature is enabled, after the phone has initialized and Layer 2 connectivity is established, the phone sends
                                                out LLDP-MED PDU frames. If the phone receives no acknowledgment, the manually configured VLAN or default VLAN will be used
                                                if applicable. If the CDP is used concurrently, the waiting period of 6 seconds is used. The waiting period will increase
                                                the overall startup time for the phone.

Network Startup Delay

Setting this value causes a delay for the switch to get to the forwarding state before the phone will send out the first LLDP-MED
                                                packet. The default delay is 3 seconds. For configuration of some switches, you might need to increase this value to a higher
                                                value for LLDP-MED to work. Configuring a delay can be important for networks that use Spanning Tree Protocol.

VLAN ID

If you use a VLAN without CDP (VLAN enabled and CDP disabled), enter a VLAN ID for the IP phone. Note that only voice packets
                                                are tagged with the VLAN ID. Do not use 1 for the VLAN ID.

PC Port VLAN ID

VLAN ID for the PC port.

DHCP VLAN Option

A predefined DHCP VLAN option to learn the voice VLAN ID. You can use the feature only when no voice VLAN information is available
                                                by CDP/LLDP and manual VLAN methods. CDP/LLDP and manual VLAN are all disabled.

Valid values are:

Null

128 to 149

151 to 158

161 to 254

Set the value to Null to disable DHCP VLAN option.

Cisco recommends that you use DHCP Option 132.

#### Inventory Settings

Parameter

Description

Asset ID

Provides the ability to enter an asset ID for inventory management when using LLDP-MED. The default value for Asset ID is
                                                empty. Enter a string of less than 32 characters if you are using this field.

The Asset ID can be provisioned only by using the web management interface or remote provisioning. The Asset ID is not displayed
                                                on the phone screen.

Changing the Asset ID field causes the phone to reboot.

SIP

#### SIP Parameters

Parameter

Description

Max Forward

SIP Max Forward value, which can range from 1 to 255.

Default: 70

Max Redirection

Number of times an invite can be redirected to avoid an infinite loop.

Default: 5

Max Auth

Maximum number of times (from 0 to 255) a request can be challenged.

Default: 2

SIP User Agent Name

Used in outbound REGISTER requests.

Default: $VERSION

If empty, the header is not included. Macro expansion of $A to $D corresponding to GPP_A to GPP_D allowed

SIP Server Name

Server header used in responses to inbound responses.

Default: $VERSION

SIP Reg User Agent Name

User-Agent name to be used in a REGISTER request. If this is not specified, the SIP User Agent Name is also used for the REGISTER
                                                request.

Default: Blank

SIP Accept Language

Accept-Language header used. To access, click the SIP tab, and fill in the SIP Accept Language field.

There is no default. If empty, the header is not included.

DTMF Relay MIME Type

MIME Type used in a SIP INFO message to signal a DTMF event. This field must match that of the Service Provider.

Default: application/dtmf-relay

Hook Flash MIME Type

MIME Type used in a SIPINFO message to signal a hook flash event.

Remove Last Reg

Enables you to remove the last registration before registering a new one if the value is different. Select yes or no from
                                                the drop-down menu.

Use Compact Header

If set to yes, the phone uses compact SIP headers in outbound SIP messages. If inbound SIP requests contain normal headers,
                                                the phone substitutes incoming headers with compact headers. If set to no, the phones use normal SIP headers. If inbound SIP
                                                requests contain compact headers, the phones reuse the same compact headers when generating the response, regardless of this
                                                setting.

Default: No

Escape Display Name

Enables you to keep the Display Name private.

Select Yes if you want the IP phone to enclose the string (configured in the Display Name) in a pair of double quotes for
                                                outbound SIP messages.

Default: Yes.

Talk Package

Enables support for the BroadSoft Talk Package that lets users answer or resume a call by clicking a button in an external
                                                application.

Default: No

Hold Package

Enables support for the BroadSoft Hold Package, which lets users place a call on hold by clicking a button in an external
                                                application.

Default: No

Conference Package

Enables support for the BroadSoft Conference Package that enables users to start a conference call by clicking a button in
                                                an external application.

Default: No

RFC 2543 Call Hold

If set to yes, unit includes c=0.0.0.0 syntax in SDP when sending a SIP re-INVITE to the peer to hold the call. If set to
                                                no, unit will not include the c=0.0.0.0 syntax in the SDP. The unit will always include a=sendonly syntax in the SDP in either
                                                case.

Default: Yes

Random REG CID on Reboot

If set to yes, the phone uses a different random call-ID for registration after the next software reboot. If set to no, the
                                                Cisco IP phone tries to use the same call-ID for registration after the next software reboot. The Cisco IP phone always uses
                                                a new random Call-ID for registration after a power-cycle, regardless of this setting.

Default: No.

SIP TCP Port Min

Specifies the lowest TCP port number that can be used for SIP sessions.

Default: 5060

SIP TCP Port Max

Specifies the highest TCP port number that can be used for SIP sessions.

Default: 5080

Caller ID Header

Provides the option to take the caller ID from PAID-RPID-FROM, PAID-FROM, RPID-PAID-FROM, RPID-FROM, or FROM header.

Default: PAID-RPID-FROM

Hold Target Before Refer

Controls whether to hold call leg with transfer target before sending REFER to the transferee when initiating a fully-attended
                                                call transfer (where the transfer target has answered).

Default: No

Dialog SDP Enable

When enabled and the Notify message body is too big causing fragmentation, the Notify message xml dialog is simplified; Session
                                                Description Protocol (SDP) is not included in the dialog xml content.

Keep Referee When Refer Failed

If set to yes, it configures the phone to immediately handle NOTIFY sipfrag messages.

Display Diversion Info

Display the Diversion info included in SIP message on LCD or not.

Display Anonymous From Header

Show the caller ID from the SIP INVITE message “From” header when set to Yes, even if the call is an anonymous call. When
                                                the parameter is set to no, the phone displays "Anonymous Caller" as the caller ID.

Sip Accept Encoding

Supports the content-encoding gzip feature. The options are none and gzip.

If gzip is selected, the SIP message header contains the string “Accept-Encoding: gzip”, and the phone is able to process
                                                the SIP message body, which is encoded with the gzip format.

Disable Local Name To Header

The options are No and Yes. If No is selected, no changes are made. The default value is No.

If Yes is selected, it disables the display name in “Directory”, “Call History”, and in the “To” header during an outgoing
                                                call.

SIP IP Preference

Sets if the phone uses IPv4 or IPv6.

Default: IPv4.

#### SIP Timer Values (sec)

Parameter

Description

SIP T1

RFC 3261 T1 value (RTT estimate) that can range from 0 to 64 seconds.

Default: 0.5 seconds

SIP T2

RFC 3261 T2 value (maximum retransmit interval for non-INVITE requests and INVITE responses) that can range from 0 to 64 seconds.

Default: 4 seconds

SIP T4

RFC 3261 T4 value (maximum duration a message remains in the network), which can range from 0 to 64 seconds.

Default: 5 seconds.

SIP Timer B

INVITE time-out value, which can range from 0 to 64 seconds.

Default: 16 seconds.

SIP Timer F

Non-INVITE time-out value, which can range from 0 to 64 seconds.

Default: 16 seconds.

SIP Timer H

INVITE final response, time-out value, which can from 0 to 64 seconds.

Default: 16 seconds.

SIP Timer D

ACK hang-around time, which can range from 0 to 64 seconds.

Default: 16 seconds.

SIP Timer J

Non-INVITE response hang-around time, which can range from 0 to 64 seconds.

Default: 16 seconds.

INVITE Expires

INVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Ranges from 0 to 2000000.

Default: 240 seconds

ReINVITE Expires

ReINVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Ranges from 0 to
                                                2000000.

Default: 30

Reg Min Expires

Minimum registration expiration time allowed from the proxy in the Expires header or as a Contact header parameter. If the
                                                proxy returns a value less than this setting, the minimum value is used.

Reg Max Expires

Maximum registration expiration time allowed from the proxy in the Min-Expires header. If the value is larger than this setting,
                                                the maximum value is used.

Reg Retry Intv

Interval to wait before the Cisco IP Phone retries registration after failing during the last registration.The range is from
                                                1 to 2147483647

Default: 30

See the note below for additional details.

Reg Retry Long Intvl

When registration fails with a SIP response code that does not match<Retry Reg RSC>, the Cisco IP Phone waits for the specified
                                                length of time before retrying. If this interval is 0, the phone stops trying. This value should be much larger than the Reg
                                                Retry Intvl value, which should not be 0.

Default: 1200

See the note below for additional details.

Reg Retry Random Delay

Random delay range (in seconds) to add to <Register Retry Intvl> when retrying REGISTER after a failure. Minimum and maximum
                                                random delay to be added to the short timer. The range is from 0 to 2147483647.

Default: 0

Reg Retry Long Random Delay

Random delay range (in seconds) to add to <Register Retry Long Intvl> when retrying REGISTER after a failure.

Default: 0

Reg Retry Intvl Cap

Maximum value of the exponential delay. The maximum value to cap the exponential backoff retry delay (which starts at the
                                                Register Retry Intvl and doubles every retry). Defaults to 0, which disables the exponential backoff (that is, the error retry
                                                interval is always at the Register Retry Intvl). When this feature is enabled, the Reg Retry Random Delay is added to the
                                                exponential backoff delay value. The range is from 0 to 2147483647.

Default: 0

Sub Min Expires

Sets the lower limit of the REGISTER expires value returned from the Proxy server.

Sub Max Expires

Sets the upper limit of the REGISTER minexpires value returned from the Proxy server in the Min-Expires header.

Default: 7200.

Sub Retry Intvl

This value (in seconds) determines the retry interval when the last Subscribe request fails.

Default: 10.

The phone can use a RETRY-AFTER value when it is received from a SIP proxy server that is too busy to process a request (503
                                                Service Unavailable message). If the response message includes a RETRY-AFTER header, the phone waits for the specified length
                                                of time before to REGISTER again. If a RETRY-AFTER header is not present, the phone waits for the value specified in the Reg
                                                Retry Interval or the Reg Retry Long Interval.

#### Response Status Code Handling

Parameter

Description

Try Backup RSC

This parameter may be set to invoke failover upon receiving specified response codes.

Default: Blank

For example, you can enter numeric values 500 or a combination of numeric values plus wild cards if multiple values are possible.
                                                For the later, you can use 5?? to represent all SIP Response messages within the 500 range. If you want to use multiple ranges,
                                                you can add a comma "," to delimit values of 5?? and 6??

Retry Reg RSC

Interval to wait before the phone retries registration after failing during the last registration.

Default: Blank

For example, you can enter numeric values 500 or a combination of numeric values plus wild cards if multiple values are possible.
                                                For the later, you can use 5?? to represent all SIP Response messages within the 500 range. If you want to use multiple ranges,
                                                you can add a comma "," to delimit values of 5?? and 6??

#### RTP Parameters

Parameter

Description

RTP Port Min

Minimum port number for RTP transmission and reception. Minimum port number for RTP transmission and reception. Should define
                                                a range that contains at least 10 even number ports (twice the number of lines); for example, configure RTP port min to 16384
                                                and RTP port max to 16538.

Default: 16384

RTP Port Max

Maximum port number for RTP transmission and reception. Should define a range that contains at least 10 even number ports
                                                (twice the number of lines); for example, configure RTP port min to 16384 and RTP port max to 16538.

The maximum value for the RTP port must be lesser than 49152.

Default: 16538

RTP Packet Size

Packet size in seconds, which can range from 0.01 to 0.13. Valid values must be a multiple of 0.01 seconds.

Default: 0.02

Max RTP ICMP Err

Number of successive ICMP errors allowed when transmitting RTP packets to the peer before the phone terminates the call. If
                                                value is set to 0, the phone ignores the limit on ICMP errors.

RTCP Tx Interval

Interval for sending out RTCP sender reports on an active connection. It can range from 0 to 255 seconds.

Default: 0

SDP IP Preferences

Select IPv4 or IPv6.

Default: IPv4

If the phone is in dual-mode and has both ipv4 and ipv6 addresses, it will always include both addresses in SDP by attributes
                                                "a=altc …

If  IPv4 address is selected, then ipv4 address has higher priority than ipv6 address in SDP and indicates that phone prefers
                                                using ipv4 RTP address.

If the phone has only ipv4 address or ipv6 address,  SDP does not have ALTC attributes and RTP address is specified in “c=”
                                                line.

#### SDP Payload Types

Parameter

Description

G722.2 Dynamic Payload

G722 Dynamic Payload type.

Default: 96

iLBC Dynamic Payload

iLBC Dynamic Payload type.

Default: 97

iSAC Dynamic Payload

iSAC Dynamic Payload type.

Default: 98

OPUS Dynamic Payload

OPUS Dynamic Payload type.

Default: 99

AVT Dynamic Payload

AVT dynamic payload type. Ranges from 96-127.

Default: 101

INFOREQ Dynamic Payload

INFOREQ Dynamic Payload type.

H264 BP0 Dynamic Payload

H264 BPO Dynamic Payload type.

Default: 110

H264 HP Dynamic Payload

H264 HP Dynamic Payload type.

Default: 110

G711u Codec Name

G711u codec name used in SDP.

Default: PCMU

G711a Codec Name

G711a codec name used in SDP.

Default: PCMA

G729a Codec Name

G729a codec name used in SDP.

Default: G729a

G729b Codec Name

G729b codec name used in SDP.

Default: G729b

G722 Codec Name

G722 codec name used in SDP.

Default: G722

G722.2 Codec Name

G722.2 codec name used in SDP.

Default: G722.2

iLBC Codec Name

iLBC codec name used in SDP.

Default: iLBC

iSAC Codec Name

iSAC codec name used in SDP.

Default: iSAC

OPUS Codec Name

OPUS codec name used in SDP.

Default: OPUS

AVT Codec Name

AVT codec name used in SDP.

Default: telephone-event

#### NAT Support Parameters

Parameter

Description

Handle VIA received

Enables the phone to process the received parameter in the VIA header.

Default: No

Handle VIA rport

Enables the phone to process the rport parameter in the VIA header.

Default: No

Insert VIA received

Enables to insert the received parameter into the VIA header of SIP responses if the received-from IP and VIA sent-by IP values
                                                differ.

Default: No

Insert VIA rport

Enables to insert the rport parameter into the VIA header of SIP responses if the received-from IP and VIA sent-by IP values
                                                differ.

Default: No

Substitute VIA Addr

Enables the user to use NAT-mapped IP:port values in the VIA header.

Default: No

Send Resp To Src Port

Enables to send responses to the request source port instead of the VIA sent-by port.

Default: No

STUN Enable

Enables the use of STUN to discover NAT mapping.

Default: No

STUN Test Enable

If the STUN Enable feature is enabled and a valid STUN server is available, the phone can perform a NAT-type discovery operation
                                                when it powers on. It contacts the configured STUN server, and the result of the discovery is reported in a Warning header
                                                in all subsequent REGISTER requests. If the phone detects symmetric NAT or a symmetric firewall, NAT mapping is disabled.

Default: No

STUN Server

IP address or fully-qualified domain name of the STUN server to contact for NAT mapping discovery. You can use a public STUN
                                                server or set up your own STUN server.

Default: Blank

EXT IP

External IP address to substitute for the actual IP address of phone in all outgoing SIP messages. If 0.0.0.0 is specified,
                                                no IP address substitution is performed.

If this parameter is specified, phone assumes this IP address when generating SIP messages and SDP (if NAT Mapping is enabled
                                                for that line).

Default: Blank

EXT RTP Port Min

External port mapping number of the RTP Port Minimum number. If this value is not zero, the RTP port number in all outgoing
                                                SIP messages is substituted for the corresponding port value in the external RTP port range.

Default: 0

NAT Keep Alive Intvl

Interval between NAT-mapping keep alive messages.

Default: 15

Redirect Keep Alive

If enabled, the IP phone redirects the keepalive message when SIP_301_MOVED_PERMANENTLY is received as the registration response.

Provisioning

#### Configuration Profile

Parameter

Description

Provision Enable

Allows or denies resync actions.

Default: 160,159,66,150

Resync On Reset

The device performs a resync operation after power-up and after each upgrade attempt when set to Yes .

Default: Yes

Resync Random Delay

A random delay following the boot-up sequence before performing the reset, specified in seconds. In a pool of IP Telephony
                                                devices that are scheduled to simultaneously power up, this introduces a spread in the times at which each unit sends a resync
                                                request to the provisioning server. This feature can be useful in a large residential deployment, in the case of a regional
                                                power failure.

The value for this field must be an integer ranging between 0 and 65535.

The default value is 2.

Resync At (HHmm)

The time (HHmm) that the device resynchronizes with the provisioning server.

The value for this field must be a four-digit number ranging from 0000 to 2400 to indicate the time in HHmm format. For example,
                                                0959 indicates 09:59.

The default value is empty. If the value is invalid, the parameter is ignored. If this parameter is set with a valid value,
                                                the Resync Periodic parameter is ignored.

Resync At Random Delay

Prevents an overload of the provisioning server when a large number of devices power-on simultaneously.

To avoid flooding resync requests to the server from multiple phones, the phone resynchronizes in the range between the hours
                                                and minutes, and the hours and minutes plus the random delay (hhmm, hhmm+random_delay). For example, if the random delay =
                                                (Resync At Random Delay + 30)/60 minutes, the input value in seconds is converted to minutes, rounding up to the next minute
                                                to calculate the final random_delay interval.

The valid value ranges between 0 and 65535.

This feature is disabled when this parameter is set to zero. The default value is 600 seconds (10 minutes).

Resync Periodic

The time interval between periodic resynchronizes with the provisioning server. The associated resync timer is active only
                                                after the first successful sync with the server.

The valid formats are as follows:

An integer

Example: An input of 3000 indicates that the next resync occurs in 3000 seconds.

Multiple integers

Example: An input of 600,1200,300 indicates that the first resync occurs in 600 seconds, the second resync occurs in 1200 seconds after the first one, and
                                                      the third resync occurs in 300 seconds after the second one.

A time range

Example, an input of 2400+30 indicates that the next resync occurs in between 2400 and 2430 seconds after a successful resync.

Set this parameter to zero to disable periodic resynchronization.

The default value is 3600 seconds.

Resync Error Retry Delay

If a resync operation fails because the IP Telephony device was unable to retrieve a profile from the server, or the downloaded
                                                file is corrupt, or an internal error occurs, the device tries to resync again after a time specified in seconds.

The valid formats are as follows:

An integer

Example: An input of 300 indicates that the next retry for resync occurs in 300 seconds.

Multiple integers

Example: An input of 600,1200,300 indicates that the first retry occurs in 600 seconds after the failure, the second retry occurs in 1200 seconds after the
                                                      failure of the first retry, and the third retry occurs in 300 seconds after the failure of the second retry.

A time range

Example, an input of 2400+30 indicates that the next retry occurs in between 2400 and 2430 seconds after a resync failure.

If the delay is set to 0, the device does not try to resync again following a failed resync attempt.

Forced Resync Delay

Maximum delay (in seconds) the phone waits before performing a resynchronization.

The device does not resync while one of its phone lines is active. Because a resync can take several seconds, it is desirable
                                                to wait until the device has been idle for an extended period before resynchronizing. This allows a user to make calls in
                                                succession without interruption.

The device has a timer that begins counting down when all of its lines become idle. This parameter is the initial value of
                                                the counter. Resync events are delayed until this counter decrements to zero.

The valid value ranges between 0 and 65535.

The default value is 14,400 seconds.

Resync From SIP

Controls requests for resync operations via a SIP NOTIFY event sent from the service provider proxy server to the IP Telephony
                                                device. If enabled, the proxy can request a resync by sending a SIP NOTIFY message containing the Event: resync header to
                                                the device.

Default: Yes

Resync After Upgrade Attempt

Enables or disables the resync operation after any upgrade occurs. If Yes is selected, sync is triggered.

Default: Yes

Resync Trigger 1

Resync Trigger 2

If the logical equation in these parameters evaluates to FALSE, Resync is not triggered even when Resync On Reset is set to
                                                TRUE. Only Resync via direct action URL and SIP notify ignores these Resync Trigger.

Default: Blank

Resync Fails On FNF

A resync is considered unsuccessful if a requested profile is not received from the server. This can be overridden by this
                                                parameter. When it is set to No , the device accepts a file-not-found response from the server as a successful resync.

Default: Yes

Profile Authentication Type

Specifies the credentials to use for profile account authentication. The available options are:

Disabled : Disables the profile account feature. When this feature is disabled, the Profile account setup menu doesn't display on the phone screen.

Basic HTTP Authentication : The HTTP login credentials are used to authenticate the profile account.

XSI Authentication : XSI login credentials or XSI SIP credentials are used to authenticate the profile account. The authentication credentials
                                                      depend on the XSI Authentication Type for the phone:

When the XSI Authentication Type for the phone is set to Login Credentials , the XSI login credentials are used.

When the XSI Authentication Type for the phone is set to SIP Credentials , the XSI SIP credentials are used.

Default: Basic HTTP Authentication

Profile Rule

Profile Rule B

Profile Rule C

Profile Rule D

Each profile rule informs the phone of a source from which to obtain a profile (configuration file). During every resync operation,
                                                the phone applies all the profiles in sequence.

Default: /$PSN.xml

If you are applying AES-256-CBC encryption to the configuration files, specify the encryption key with the --key keyword as follows:

[--key <encryption key>]

You can enclose the encryption key in double-quotes (") optionally.

DHCP Option To Use

DHCP options, delimited by commas, used to retrieve firmware and profiles.

Default: 66,160,159,150,60,43,125

DHCPv6 Option To Use

DHCP options, delimited by commas, used to retrieve firmware and profiles.

Default: 17,160,159

Log Request Msg

The message sent to the syslog server at the start of a resync attempt.

```
$PN $MAC – Requesting % $SCHEME://$SERVIP:$PORT$PATH
```

Log Success Msg

The syslog message issued upon successful completion of a resync attempt.

```
$PN $MAC -Successful Resync  %
```

```
$SCHEME://$SERVIP:$PORT$PATH
```

Log Failure Msg

The syslog message that is issued after a failed download attempt.

```
$PN $MAC -- Resync failed: $ERR
```

User Configurable Resync

Allows a user to resync the phone from the phone screen.

Default: Yes

#### Upload Configuration Options

Specifies how the phone reports its current internal configuration to the provisioning server. The URLs in this field specify
                                                the destination for a report and can include an encryption key.

You can use the following keywords, encryption key, and file locations and names to control how you store the phone configuration
                                                information:

No keywords and only an XML file reports the entire configuration data to server.

[--status] keyword reports the status data to server.

[--delta] keyword reports the changed configuration to server.

[--key <encryption key>] keyword tells the phone to apply AES-256-CBC encryption with the specified encryption key to the configuration report, before
                                                      sending it to the server.

You can enclose the encryption key in double-quotes (") optionally.

Two rules used together as:

```
[--delta]http://my_http_server/config-mpp-delta.xml [--status]http://my_http_server/config-mpp-status.xml
```

HTTP Report method:

Specifies whether the HTTP Request that the phone sends should be an HTTP PUT or an HTTP POST .

PUT Method –To create a new report or overwrite an existing report at a known location on the server. For example, you may want to keep
                                                      overwriting each report that you send and only store the most current configuration on the server.

POST Method –To send the report data to the server for processing, such as, by a PHP script. This approach provides more flexibility for
                                                      storing the configuration information. For example, you may want to send a series of phone status reports and store all the reports on the server.

Defines when the phone reports its configuration to the provisioning servers.

On Request : The phone reports its configuration only when an administrator sends a sip notify event, or the phone restarts.

On Local Change : The phone reports its configuration when any configuration parameter changes by an action on the phone or on the phone administration
                                                      web page. The phone waits for a few seconds after a change is made, and then reports the configuration. This delay ensures
                                                      that changes are reported to the web server in batches, rather than reporting a single change at a time.

Periodically : The phone reports its configuration at regular intervals. The interval is expressed in seconds.

Example XML configuration:

Periodically

Defines the interval (in seconds) that the phone reports its configuration to the provisioning servers.

This field is used only when Report to Server is set to Periodically .

Default: 3600

Minimum: 600

Maximum: 2592000 (30 days)

Example XML configuration:

Periodically

<!available options: On Request | On Local Change| Periodically-->

3600

Yes

Upload Delay On Local Change:

Defines the delay (in seconds) that the phone waits after a change is made, and then reports the configuration.

This field is used only when Report to Server is set to On Local Change .

Default: 60

Minimum: 10

Maximum: 900

Example XML configuration:

60

#### Firmware Upgrade

Parameter

Description

Upgrade Enable

Allows firmware update operations independent of resync actions.

Default: Yes

Upgrade Rule

A firmware upgrade script that defines upgrade conditions and associated firmware URLs. It uses the same syntax as Profile
                                             Rule.

Use the following format to enter the upgrade rule:

protocol://server[:port]/profile_pathname

For example:

tftp://192.168.1.5/image/sip88xx.11-1-1MPP-221.loads

If no protocol is specified, TFTP is assumed. If no server-name is specified, the host that requests the URL is used as the
                                             server name. If no port is specified, the default port is used (69 for TFTP, 80 for HTTP, or 443 for HTTPS).

You can also include the credentials that are used to access the server. Then, the upgrade rule is:

[--uid $userID --pwd $password]protocol://server[:port]/profile_pathname

For example,

[--uid TEST --pwd TestAbC123]tftp://192.168.1.5/image/sip88xx.11-1-1MPP-221.loads

If the user ID or the password contains special characters (/ [ & } (*) # , etc.), you need to quote them in the upgrade rule.
                                             There are two options for quoting special characters:

Put the user ID or the password that contains special characters into double quotation marks (" "). This option doesn't work
                                                   for some of the special characters, such as " " [ ].

For example,

[--uid TEST --pwd "Test#\AbC123"]tftp://192.168.1.5/image/sip88xx.11-1-1MPP-221.loads

Use the octal encoding of the special characters.

For example, escape the pond (#) with "\043" and the backslash with "\057" for the password "Test#\AbC123" in the following rule:

[--uid TEST --pwd Test\043\057AbC123]tftp://192.168.1.5/image/sip88xx.11-1-1MPP-221.loads

Default: Blank

Log Upgrade Request Msg

Syslog message issued at the start of a firmware upgrade attempt.

Default: $PN $MAC -- Requesting upgrade $SCHEME://$SERVIP:$PORT$PATH

Log Upgrade Success Msg

Syslog message issued after a firmware upgrade attempt completes successfully.

Default: $PN $MAC -- Successful upgrade $SCHEME://$SERVIP:$PORT$PATH -- $ERR

Log Upgrade Failure Msg

Syslog message issued after a failed firmware upgrade attempt.

Default: $PN $MAC -- Upgrade failed: $ERR

Peer Firmware Sharing

Enables or disables the Peer Firmware Sharing feature. Select Yes or No to enable or to disable the feature.

Default: Yes

Peer Firmware Sharing Log Server

Indicates the IP address and the port to which the UDP message is sent.

For example: 10.98.76.123:514 where, 10.98.76.123 is the IP address and 514 is the port number.

For more information about the Provisioning page, see the Cisco IP Phone 7800 Series Multiplatform Phones Provisioning Guide .

#### CA Settings

Parameter

Description

Custom CA Rule

The URL to download Custom CA.

Default: Blank

#### HTTP Settings

Parameter

Description

HTTP User Agent Name

Allows you to enter a name for HTTP user.

Default: Blank

#### Problem Report Tool

Parameter

Description

PRT Upload Rule

Specifies the path to the PRT upload script. You can enter the path in the format:

or

If PRT Max Timer and PRT Upload Rule fields are empty, problem reports are not generated.

PRT Upload Method

Determines the method used to upload PRT logs to the remote server. Options are: HTTP POST and PUT.

Default: POST

PRT Max Timer

Determines at what interval (minutes) the phone starts generating problem report automatically. The interval range that you
                                                can set is 15 minutes to 1440 minutes.

Default: Empty

If PRT Max Timer and PRT Upload Rule fields are empty, problem reports are not generated.

PRT Name

Defines a name for the generated PRT file. Enter the name in the format:

#### General Purpose Parameters

Parameter

Description

GPP A - GPP P

The general purpose parameters GPP_* are used as free string, registers when configuring the Cisco IP phones to interact with
                                                a particular provisioning server solution. They can be configured to contain diverse values, including the following:

Encryption keys

URLs

Multistage provisioning status information

Post request templates

Parameter name alias maps

Partial string values, eventually combined into complete parameter values

Default: Blank

Regional

#### Call Progress Tones

Parameter

Description

Dial Tone

Prompts the user to enter a phone number.

Outside Dial Tone

Alternative to the Dial Tone. It prompts the user to enter an external phone number, as opposed to an internal extension.
                                             It is triggered by a, (comma) character encountered in the dial plan.

Prompt Tone

Prompts the user to enter a call forwarding phone number.

Busy Tone

Played when a 486 RSC is received for an outbound call.

Reorder Tone

Played when an outbound call has failed or after the far end hangs up during an established call. Reorder Tone is played automatically
                                             when <Dial Tone> or any of its alternatives times out.

Off Hook Warning Tone

Played when the phone receiver has been off hook after a period of time.

Ring Back Tone

Played during an outbound call when the far end is ringing.

Call Waiting Tone

Played when a call is waiting.

Confirm Tone

Brief tone to notify the user that the last input value has been accepted.

MWI Dial Tone

Played instead of the Dial Tone when there are unheard messages in the caller’s mailbox.

Cfwd Dial Tone

Played when all calls are forwarded.

Holding Tone

Informs the local caller that the far end has placed the call on hold.

Conference Tone

Played to all parties when a three-way conference call is in progress.

Secure Call Indication Tone

Played when a call has been successfully switched tosecure mode. It should be played only for a short while (less than 30
                                             seconds) and at a reduced level (less than -19 dBm) so it does not interfere with the conversation.

Page Tone

Specifies the tone transmitted when the paging feature is enabled.

Alert Tone

Played when an alert occurs.

Mute Tone

Played when the Mute button is pressed to mute the phone.

Unmute Tone

Played when the Mute button is pressed to unmute the phone.

System Beep

Audible notification tone played when a system error occurs.

Call Pickup Tone

Provides the ability to configure an audio indication for call pickup.

#### Distinctive Ring Patterns

Parameter

Description

Cadence 1

Cadence script for distinctive ring 1.

Defaults to 60(2/4).

Cadence 2

Cadence script for distinctive ring 2.

Defaults to 60(.3/.2, 1/.2,.3/4).

Cadence 3

Cadence script for distinctive ring 3.

Defaults to 60(.8/.4,.8/4).

Cadence 4

Cadence script for distinctive ring 4.

Defaults to 60(.4/.2,.3/.2,.8/4).

Cadence 5

Cadence script for distinctive ring 5.

Defaults to 60(.2/.2,.2/.2,.2/.2,1/4).

Cadence 6

Cadence script for distinctive ring 6.

Defaults to 60(.2/.4,.2/.4,.2/4).

Cadence 7

Cadence script for distinctive ring 7.

Defaults to 60(4.5/4).

Cadence 8

Cadence script for distinctive ring 8.

Defaults to 60(0.25/9.75)

Cadence 9

Cadence script for distinctive ring 9.

Defaults to 60(.4/.2,.4/2).

#### Control Timer Values (sec)

Parameter

Description

Reorder Delay

Delay after far end hangs up before reorder (busy) tone is played. 0 = plays immediately, inf = never plays. Range: 0–255
                                                seconds. Set to 255 to return the phone immediately to on-hook status and to not play the tone.

Interdigit Long Timer

Long timeout between entering digits when dialing. The interdigit timer values are used as defaults when dialing. The Interdigit_Long_Timer
                                                is used after any one digit, if all valid matching sequences in the dial plan are incomplete as dialed. Range: 0–64 seconds.

Default: 10

Interdigit Short Timer

Short timeout between entering digits when dialing. The Interdigit_Short_Timer is used after any one digit, if at least one
                                                matching sequence is complete as dialed, but more dialed digits would match other as yet incomplete sequences. Range: 0–64
                                                seconds.

Default: 3

#### Vertical Service Activation Codes

Parameter

Description

Call Return Code

This code calls the last caller.

Defaults to *69.

Blind Transfer Code

Begins a blind transfer of the current call to the extension specified after the activation code.

Defaults to *88.

Cfwd All Act Code

Forwards all calls to the extension specified after the activation code.

Defaults to *72.

Cfwd All Deact Code

Cancels call forwarding of all calls.

Defaults to *73.

Cfwd Busy Act Code

Forwards busy calls to the extension specified after the activation code.

Defaults to *90.

Cfwd Busy Deact Code

Cancels call forwarding of busy calls.

Defaults to *91.

Cfwd No Ans Act Code

Forwards no-answer calls to the extension specified after the activation code.

Defaults to *92.

Cfwd No Ans Deact Code

Cancels call forwarding of no-answer calls.

Defaults to *93.

CW Act Code

Enables call waiting on all calls.

Defaults to *56.

CW Deact Code

Disables call waiting on all calls.

Defaults to *57.

CW Per Call Act Code

Enables call waiting for the next call.

Defaults to *71.

CW Per Call Deact Code

Disables call waiting for the next call.

Defaults to *70.

Block CID Act Code

Blocks caller ID on all outbound calls.

Defaults to *67.

Block CID Deact Code

Removes caller ID blocking on all outbound calls.

Defaults to *68.

Block CID Per Call Act Code

Removes caller ID blocking on the next inbound call.

Defaults to *81.

Block CID Per Call Deact Code

Removes caller ID blocking on the next inbound call.

Defaults to *82.

Block ANC Act Code

Blocks all anonymous calls.

Defaults to *77.

Block ANC Deact Code

Removes blocking of all anonymous calls.

Defaults to *87.

DND Act Code

Enables the do not disturb feature.

Defaults to *78.

DND Deact Code

Disables the do not disturb feature.

Defaults to *79.

Secure All Call Act Code

Makes all outbound calls secure.

Defaults to *16.

Secure No Call Act Code

Makes all outbound calls not secure.

Defaults to *17.

Secure One Call Act Code

Makes a secure call.

Default: *18.

Secure One Call Deact Code

Disables secure call feature.

Default: *19.

Paging Code

The star code used for paging the other clients in the group.

Defaults to *96.

Call Park Code

The star code used for parking the current call.

Defaults to *38.

Call Pickup Code

The star code used for picking up a ringing call.

Defaults to *36.

Call Unpark Code

The star code used for picking up a call from the call park.

Defaults to *39.

Group Call Pickup Code

The star code used for picking up a group call.

Defaults to *37.

Referral Services Codes

These codes tell the IP phone what to do when the user places the current call on hold and is listening to the second dial
                                                tone.

One or more *code can be configured into this parameter, such as *98, or *97|*98|*123, and so on. Max total length is 79 chars.
                                                This parameter applies when the user places the current call on hold (by Hook Flash) and is listening to second dial tone.
                                                Each *code (and the following valid target number according to current dial plan) entered on the second dial-tone triggers
                                                the phone to perform a blind transfer to a target number that is prepended by the service *code.

For example, after the user dials *98, the IP phone plays a special dial tone called the Prompt Tone while waiting for the
                                                user the enter a target number (which is checked according to dial plan as in normal dialing). When a complete number is entered,
                                                the phone sends a blind REFER to the holding party with the Refer-To target equals to *98<target_number>. This feature allows
                                                the phone to hand off a call to an application server to perform further processing, such as call park.

The *codes should not conflict with any of the other vertical service codes internally processed by the IP phone. You can
                                                empty the corresponding *code that you do not want to the phone to process.

Feature Dial Services Codes

These codes tell the phone what to do when the user is listening to the first or second dial tone.

One or more *code can be configured into this parameter, such as *72, or *72|*74|*67|*82, and so forth. The maximum total
                                                length is 79 characters. This parameter applies when the user has a dial tone (first or second dial tone). Enter *code (and
                                                the following target number according to current dial plan) entered at the dial tone triggers the phone to call the target
                                                number prepended by the *code. For example, after user dials *72, the phone plays a prompt tone awaiting the user to enter
                                                a valid target number. When a complete number is entered, the phone sends a INVITE to *72<target_number> as in a normal call.
                                                This feature allows the proxy to process features like call forward (*72) or BLock Caller ID (*67).

The *codes should not conflict with any of the other vertical service codes internally processed by the phone. You can empty
                                                the corresponding *code that you do not want to the phone to process.

You can add a parameter to each *code in Features Dial Services Codes to indicate what tone to play after the *code is entered,
                                                such as *72‘c‘|*67‘p‘. Below are a list of allowed tone parameters (note the use of back quotes surrounding the parameter
                                                without spaces)

• c = Cfwd Dial Tone

• d = Dial Tone

• m = MWI Dial Tone

• o = Outside Dial Tone

• p = Prompt Dial Tone

• s = Second Dial Tone

• x = No tones are place, x is any digit not used above

If no tone parameter is specified, the phone plays Prompt tone by default.

If the *code is not to be followed by a phone number, such as *73 to cancel call forwarding, do not include it in this parameter.
                                                In that case, simple add that *code in the dial plan and the phone sends INVITE *73@..... as usual when user dials *73.

#### Vertical Service Announcement Codes

Parameter

Description

Service Annc Base Number

Defaults to blank.

Service Annc Extension Codes

Defaults to blank.

#### Outbound Call Codec Selection Codes

Parameter

Description

Prefer G711u Code

Makes this codec the preferred codec for the associated call.

Defaults to *017110.

Force G711u Code

Makes this codec the only codec that can be used for the associated call.

Defaults to *027110.

Prefer G711a Code

Makes this codec the preferred codec for the associated call.

Defaults to *017111

Force G711a Code

Makes this codec the only codec that can be used for the associated call.

Defaults to *027111.

Prefer G722 Code

Makes this codec the preferred codec for the associated call.

Defaults to *01722.

Only one G.722 call at a time is allowed. If a conference call is placed, a SIP re-invite message is sent to switch the calls
                                                to narrowband audio.

Force G722 Code

Makes this codec the only codec that can be used for the associated call.

Defaults to *02722.

Only one G.722 call at a time is allowed. If a conference call is placed, a SIP re-invite message is sent to switch the calls
                                                to narrowband audio.

Prefer G722.2 Code

Makes this codec the preferred codec for the associated call.

Force G722.2 Code

Makes this codec the only codec that can be used for the associated call.

Prefer G729a Code

Makes this codec the preferred codec for the associated call.

Defaults to *01729.

Force G729a Code

Makes this codec the only codec that can be used for the associated call.

Defaults to *02729.

Prefer iLBC Code

Makes this codec the preferred codec for the associated call.

Force iLBC Code

Makes this codec the only codec that can be used for the associated call.

Prefer ISAC Code

Makes this codec the preferred codec for the associated call.

Force ISAC Code

Makes this codec the only codec that can be used for the associated call.

Prefer OPUS Code

Makes this codec the preferred codec for the associated call.

Force OPUS Code

Makes this codec the only codec that can be used for the associated call.

#### Time

Parameter

Description

Set Local Date (mm/dd/yyyy)

Sets the local date (mm represents the month and dd represents the day). The year is optional and uses two or four digits.

Default: Blank

Set Local Time (HH/mm)

Sets the local time (hh represents hours and mm represents minutes). Seconds are optional.

Default: Blank

Time Zone

Selects the number of hours to add to GMT to generate the local time for caller ID generation. Choices are GMT-12:00, GMT-11:00,…,
                                                GMT, GMT+01:00, GMT+02:00, …, GMT+13:00.

Default: GMT-08:00

Time Offset (HH/mm)

This specifies the offset from GMT to use for the local system time.

Default: 00/00

Ignore DHCP Time Offset

When used with some routers that have DHCP with time offset values configured, the IP phone uses the router settings and ignores
                                                the IP phone time zone and offset settings. To ignore the router DHCP time offset value, and use the local time zone and offset
                                                settings, choose yes for this option. Choosing no causes the IP phone to use the router's DHCP time offset value.

Default: Yes.

Daylight Saving Time Rule

Enter the rule for calculating daylight saving time; it should include the start, end, and save values. This rule is comprised
                                                of three fields. Each field is separated by ; (a semicolon) as shown below. Optional values inside [ ] (the brackets) are
                                                assumed to be 0 if they are not specified. Midnight is represented by 0:0:0 of the given date.

This is the format of the rule: Start = <start-time>; end=<end-time>; save = <save-time>.

The <start-time> and <end-time> values specify the start and end dates and times of daylight saving time. Each value is in
                                                this format: <month> /<day> / <weekday>[/HH:[mm[:ss]]]

The <save-time> value is the number of hours, minutes, and/or seconds to add to the current time during daylight saving time.
                                                The <save-time> value can be preceded by a negative (-) sign if subtraction is desired instead of addition. The <save-time>
                                                value is in this format: [/[+|-]HH:[mm[:ss]]]

The <month> value equals any value in the range 1-12 (January-December).

The <day> value equals [+|-] any value in the range 1-31.

If <day> is 1, it means the <weekday> on or before the end of the month (in other words the last occurrence of < weekday>
                                                in that month).

Daylight Saving Time Rule (continued)

The <weekday> value equals any value in the range 1-7 (Monday-Sunday). It can also equal 0. If the <weekday> value is 0, this
                                                means that the date to start or end daylight saving is exactly the date given. In that case, the <day> value must not be negative.
                                                If the <weekday> value is not 0 and the <day> value is positive, then daylight saving starts or ends on the <weekday> value
                                                on or after the date given. If the <weekday> value is not 0 and the <day> value is negative, then daylight saving starts or
                                                ends on the <weekday> value on or before the date given. Where:

HH stands for hours (0-23).

mm stands for minutes (0-59).

ss stands for seconds (0-59).

Default: 3/-1/7/2;end=10/-1/7/2;save=1.

Daylight Saving Time Enable

Enables Daylight Saving Time.

Default: Yes

#### Language

Parameter

Description

Dictionary Server Script

Use this field to specify the language options for the phone display, and the dictionary and font files required for each
                                                language. See Set Up Dictionaries and Fonts .

Default: Blank

Language Selection

Use this field to specify the default language. The value must match one of the languages supported by the dictionary server.
                                                See Specify a Language for the Phone Display .

You can configure the language through the XML Configuration file. For example:

```
<Language_Selection ua="na"> Spanish
</Language_Selection>
```

The language name can have up to 512 characters.

Locale

Use this drop-down list box to see the supported languages. See Supported Languages for the Phone Display .

Phone

#### General

Parameter

Description

Station Name

Name of the phone.

Station Display Name

Name to identify the phone; appears on the phone screen. You can use spaces in this field and the name does not have to be
                                                unique.

Voice Mail Number

A phone number or URL to check voice mail.

Default: None

#### Handsfree

Parameter

Description

Bluetooth Mode

Shows the method of Bluetooth connection.

Phone—Pairs with a Bluetooth headset only.

Handsfree—Operates as a handsfree device with a Bluetooth-enabled mobile phone.

Both—Uses a Bluetooth headset, or operates with a Bluetooth-enabled mobile phone.

Line

Specifies the line number for which the Bluetooth is enabled.

#### Line Key

Each line key has a set of settings.

Parameter

Description

Extension

Specifies the n extension to be assigned to Line Key n.

Default: n

XML configuration examples:

To set the line key 1 to extension 1:

To disable the extension function for line key 2:

Short Name

Specifies the user name for Line Key.

Default: $USER

Share Call Appearance

Specifies whether the incoming call appearance is shared with other phones or it is private.

Extended Function

Use to assign any of the following features or functions to unused line keys on the phone:

Busy Lamp Field

Call Pickup

Speed Dial

#### Miscellaneous Line Key Settings

Parameter

Description

Line ID Mapping

Specifies the shared call appearance line ID mapping. If Vertical First is set, the second call makes the next available line
                                                ID LED flash. If Horizontal first is set, the second call will make the same LED flash on which the first call is received.
                                                Also, the behavior is same for both outgoing and incoming calls.

7811 Cisco IP Phone does not support Line ID Mapping.

Default: Horizontal First

SCA Barge-In Enable

Enables the SCA Barge-In.

Default: No

SCA Sticky Auto Line Seize

If enabled, restricts to automatically pick up an incoming call on a shared line when you take the phone off-hook.

Call Appearances Per Line

This parameter allows you to choose the number of calls per line button. You can choose a value from 2 to 10.

Default: 2

#### Supplementary Services

Parameter

Description

Conference Serv

Enable or disable three-way conference service.

Default: Yes

Attn Transfer Serv

Enable or disable attended-call-transfer service.

Default: Yes

Blind Transfer Serv

Enable or disable blind-call-transfer service.

Default: Yes

DND Serv

Enable or disable do not disturb service.

Default: Yes

Block ANC Serv

Enable or disable block-anonymous-call service.

Default: Yes

Block CID Serv

Enable or disable blocking outbound Caller-ID service.

Default: Yes

Secure Call Serv

Enable or disable secured call services.

Default: Yes

Cfwd All Serv

Enable or disable call-forward-all service.

Default: Yes

Cfwd Busy Serv

Enable or disable call-forward-on-busy service.

Default: Yes

Cfwd No Ans Serv

Enable or disable call-forward-no-answer service.

Default: Yes

Paging Serv

Enable or disable paging service on the phone.

Default: Yes

Call Park Serv

Enable or disable call park services on the phone.

Default: Yes

Call Pick Up Serv

Enable or disable call pick up services on the phone.

Default: Yes

ACD Login Serv

Enable or disable ACD login services on the phone.

Default: Yes

Group Call Pick Up Serv

Enable or disable group call pick up services on the phone.

Default: Yes

Service Annc Serv

Enable or disable the vertical service announcement services on the phone.

Default: No

Call Recording Serv

Enable or disable the call recording services on the phone.

Default: No

Reverse Phone Lookup Serv

Enable or disable reverse name lookup for the phone.

When enabled, the phone can searches the personal address book and call history, server directory, and either the configured
                                                LDAP or XML directory.

Default: Yes

#### Ringtone

Parameter

Description

Ring1 to Ring12

Ring tone scripts for different rings.

Silent Ring Duration

Controls the duration of the silent ring.

For example, if the parameter is set to 20 seconds, the phone plays the silent ring for 20 seconds then sends 480 response
                                                to INVITE message.

#### Extension Mobility

Parameter

Description

EM Enable

Options to enable or to disable the extension mobility support for the phone.

Default: No

EM User Domain

Name of the domain for the phone or the authentication server.

Default: Blank

Session Timer(m)

Specifies the duration of the phone session.

Countdown Timer(s)

Specifies the duration for which it waits before it logs out.

Default: 10

Preferred Password Input Mode

Options to specify the password input method of extension mobility PIN. Options are: Alpha-numeric and Numeric.

Default: Alphanumeric

#### XSI Phone Service

Parameter

Description

XSI Host Server

Enter the name of the server; for example, xsi.iop1.broadworks.net.

XSI Host Server uses http protocol by default. To enable XSI over HTTPS, you can specify https:// in the server.

Default: Blank

XSI Authentication Type

Determines the XSI authentication type. Select Login Credentials to authenticate access with XSI id and password. Select SIP Credentials to authenticate access with the register user ID and password of the SIP account registered on the phone.

Default: Login Credentials

Login User ID

BroadSoft User ID of the phone user; for example, johndoe@xdp.broadsoft.com.

Enter SIP Auth ID when you select Login Credentials or SIP Credentials for XSI authentication type.

When you choose SIP Auth ID as SIP Credentials , you must enter Login User ID. Without Login User ID, the BroadSoft directory will not appear under the phone Directory list.

Default: Blank

Login Password

Alphanumeric password associated with the User ID.

Enter login password, when you select Login Credentials for XSI authentication type.

Default: Blank

SIP Auth ID

The registered user ID of the SIP account registered on the phone.

Enter SIP Auth ID when you select SIP Credentials for XSI authentication type.

SIP Password

The password of the SIP account registered on the phone.

Enter SIP password when you select SIP Credentials for XSI authentication type.

Directory Enable

Enables BroadSoft directory for the phone user. Select Yes to enable the directory and select No to disable it.

Default: No

Directory Name

Name of the directory. Displays on the phone as a directory choice.

Default: Blank

Directory Type

Select the type of BroadSoft directory:

Enterprise: Allows users to search on last name, first name, user or group ID, phone number, extension, department, or email
                                                address.

Group: Allows users to search on last name, first name, user ID, phone number, extension, department, or email address.

Personal: Allows users to search on last name, first name, or telephone number.

Default: Enterprise

CallLog Enable

Enables to log XSI calls. Select Yes to log XSI calls and select No to disable it.

Default: No

CallLog Associated Line

Allows you to select a phone line for which you want to display the recent call logs.

You can select line numbers ranges from 1 to 10.

Display Recents From

Allows you to set which type of recent call logs the phone will display. Choose Server to display BroadSoft XSI recent call logs and select Phone to display local recent call logs.

The Display recents from is added to the Recents screen of the phone only when you set CallLog Enable to Yes and Display Recents From type to Server .

#### Broadsoft XMPP

Parameter

Description

XMPP Enable

Set to Yes to enable the BroadSoft XMPP directory for the phone user.

Default: No

Server

Enter the name of the XMPP server; for example, xsi.iop1.broadworks.net.

Default: Blank

Port

Server port for the directory.

Default: Blank

User ID

BroadSoft User ID of the phone user; for example, johndoe@xdp.broadsoft.com.

Default: Blank

Password

Alphanumeric password associated with the User ID.

Default: Blank

Login Invisible

When enabled, the user's presence information is not published when the user signs in.

Default: No

Retry Intvl

Interval, in seconds, to allow a reconnect without a log in after the client disconnects from the server. After this interval,
                                                the client needs to reauthenticate.

Default: 30

#### XML Service

Parameter

Description

XML Directory Service Name

Name of the XML Directory. Displays on the user’s phone as a directory choice

Default: Blank

XML Directory Service URL

URL where the XML Directory is located.

Default: Blank

XML Application Service Name

Name of the XML application. Displays on the user’s phone as a web application choice.

XML Application Service URL

URL where the XML application is located.

XML User Name

XML service username for authentication purposes

Default: Blank

XML Password

XML service password for authentication purposes

Default: Blank

CISCO XML EXE Enable

Enables or disables Cisco XML EXE authentication.

Default: No

CISCO XML EXE Auth Mode

Specifies the authentication mode for Cisco XML EXE. The available options are:

Trusted—No authentication is performed (local user password is set or not).

Local Credential—Authentication is based on digest authentication using the local user password, if the local user password
                                                      is set. If not set, then no authentication is performed.

Remote Credential—Authentication is based on digest authentication using the remote username/password as set in the XML application
                                                      on the web page (to access an XML application server).

Default: Trusted

#### Multiple Paging Group Parameters

Feature

Description

Group Paging Script

Enter a string to configure group paging and priority paging (out of band paging) that doesn’t require the phone registration.

#### LDAP

Parameter

Description

LDAP Dir Enable

Choose Yes to enable LDAP.

Default: No

Corp Dir Name

Enter a free-form text name, such as “Corporate Directory.”

Default: Blank

Server

Enter a fully qualified domain name or IP address of an LDAP server in the following format:

nnn.nnn.nnn.nnn

Enter the host name of the LDAP server if the MD5 authentication method is used.

Default: Blank

Search Base

Specify a starting point in the directory tree from which to search. Separate domain components [dc] with a comma. For example:

dc=cv2bu,dc=com

Default: Blank

Client DN

Enter the distinguished name domain components [dc]; for example:

dc=cv2bu,dc=com

If you are using the default Active Directory schema (Name(cn)->Users->Domain), an example of the client DN follows:

cn=”David Lee”,dc=users,dc=cv2bu,dc=com

cn=”David Lee”,dc=cv2bu,dc=com

username@domain is the client DN format for a Windows server

For example, DavidLee@cv2bu.com

Default: Blank

User Name

Enter the username for a credentialed user on the LDAP server.

Default: Blank

Password

Enter the password for the LDAP username.

Default: Blank

Auth Method

Select the authentication method that the LDAP server requires. Choices are:

None—No authentication is used between the client and the server.

Simple—The client sends its fully-qualified domain name and password to the LDAP server. Might present security issues.

Digest-MD5—The LDAP server sends authentication options and a token to the client. The client returns an encrypted response
                                                that is decrypted and verified by the server.

Default: None

Last Name Filter

Use this field to specify how the phone must perform searches based on the last name or surname (sn), when users search for
                                                contacts.

Examples:

sn:(sn=$VALUE*) instructs the phone to find all last names that begin with the entered search string.

sn:(sn=*$VALUE*) instructs the phone to find all last names in which the entered search string appears anywhere in the last name. This method
                                                is more inclusive and retrieves more search results. This method is consistent with the search method in other directories
                                                such as the Broadsoft directories and the user's personal address book on the phone.

Default: Blank

First Name Filter

Use this field to specify how the phone must perform searches based on the first name or common name (cn), when users search
                                                for contacts.

Examples:

cn:(cn=$VALUE*) instructs the phone to find all first names that begin with the entered search string.

cn:(cn=*$VALUE*) instructs the phone to find all first names in which the entered search string appears anywhere in the first name. This method
                                                is more inclusive and retrieves more search results. This method is consistent with the search method in other directories
                                                such as the Broadsoft directories and the user's personal address book on the phone.

Default: Blank

Search Item 3

Additional customized search item. Can be blank if not needed.

Default: Blank

Search Item 3 Filter

Customized filter for the searched item. Can be blank if not needed.

Default: Blank

Search Item 4

Additional customized search item. Can be blank if not needed.

Default: Blank

Search Item 4 Filter

Customized filter for the searched item. Can be blank if not needed.

Default: Blank

Display Attrs

Format of LDAP results displayed on phone, where:

a—Attribute name

cn—Common name

sn—Surname (last name)

telephoneNumber—Phone number

n—Display name

For example, n=Phone causes “Phone:” to be displayed in front of the phone number of an LDAP query result when the detail
                                                soft button is pressed.

t—type

When t=p, that is, t is of type phone number, the retrieved number can be dialed. Only one number can be made dialable. If
                                                two numbers are defined as dialable, only the first number is used. For example, a=ipPhone, t=p; a=mobile, t=p;

This example results in only the IP Phone number being dialable and the mobile number is ignored.

p—phone number

When p is assigned to a type attribute, example t=p, the retrieved number is dialable by the phone.

For example, a=givenName,n=firstname;a=sn,n=lastname;a=cn,n=cn;a=telephoneNumber,n=tele,t=p

Default: Blank

Number Mapping

Can be blank if not needed.

With the LDAP number mapping, you can manipulate the number that was retrieved from the LDAP server. For example, you can
                                                            append 9 to the number if your dial plan requires a user to enter 9 before dialing. Add the 9 prefix by adding (<:9xx.>) to
                                                            the LDAP Number Mapping field. For example, 555 1212 would become 9555 1212.

If you do not manipulate the number in this fashion, a user can use the Edit Dial feature to edit the number before dialing
                                                out.

Default: Blank

#### Programmable Softkeys

Parameter

Description

Programmable Softkey Enable

Enables programmable softkeys.

Idle Key List

Softkeys that display when the phone is idle.

Missed Call Key List

Softkeys that display when there is a missed call.

Off Hook Key List

Softkeys that display when the phone is off-hook.

Dialing Input Key List

Softkeys that display when the user must enter dialing data.

Progressing Key List

Softkeys that display when a call is attempting to connect.

Connected Key List

Softkeys that display when a call is connected.

Start-Xfer Key List

Softkeys that display when a call transfer has been initiated.

Start-Conf Key List

Softkeys that display when a conference call has been initiated.

Conferencing Key List

Softkeys that display when a conference call is in progress.

Releasing Key List

Softkeys that display when a call is released.

Hold Key List

Softkeys that display when one or more calls are on hold.

Ringing Key List

Softkeys that display when a call is incoming.

To silence an incoming call, you can add Ignore softkey.

Shared Active Key List

Softkeys that display when a call is active on a shared line.

Shared Held Key List

Softkeys that display when a call is on hold on a shared line.

PSK 1 through PSK 16

Programmable softkey fields. Enter a string in these fields to configure softkeys that display on the phone screen. You can
                                                create softkeys for speed dials to numbers or extensions, vertical service activation codes (* codes), or XML scripts.

Extension

#### General

Parameter

Description

Line Enable

To enable this line for service, select yes. Otherwise, select No.

Default: Yes

Example XML configuration:

To disable service on the line associated with extension 2:

#### Video Configuration

Parameter

Description

H264 BP0 Enable

Enables the H264 Base Profile 0 codec when you select Yes and disables it when you select No .

Default: Yes

H264 HP Enable

Enables the H264 High Profile codec when you select Yes and disables it when you select No .

Default: Yes

Encryption Method

Selects the encryption method to be used during a secured call. Options are AES 128 and AES 256 GCM .

Default: AES 128

#### Share Line Appearance

Parameter

Description

Share Ext

Indicates whether
                                             this extension is to be shared with other Cisco IP phones or
                                             private.

Default: Yes

Shared User ID

The user identified
                                             assigned to the shared line appearance.

Default: Blank

Subscription Expires

Number of seconds
                                             before the SIP subscription expires. Before the subscription
                                             expiration, the phone gets NOTIFY messages from the SIP server on
                                             the status of the shared phone extension.

Default: 3600

Restrict MWI

When enabled, the
                                             message waiting indicator lights only for messages on private
                                             lines.

Default: No

#### NAT Settings

Parameter

Description

NAT Mapping Enable

To use externally mapped IP addresses and SIP/ RTP ports in SIP messages, select yes. Otherwise, select no.

Default: No

NAT Keep Alive Enable

To send the configured NAT keep alive message periodically, select yes. Otherwise, select no.

Default: No

NAT Keep Alive Msg

Enter the keep alive message that should be sent periodically to maintain the current NAT mapping. If the value is $NOTIFY,
                                             a NOTIFY message is sent. If the value is $REGISTER, a REGISTER message without contact is sent.

Default: $NOTIFY

NAT Keep Alive Dest

Destination that should receive NAT keep alive messages. If the value is $PROXY, the messages are sent to the current or outbound
                                             proxy.

#### Network Settings

Parameter

Description

SIP TOS/DiffServ Value

Time of service (ToS)/differentiated services (DiffServ) field value in UDP IP packets carrying a SIP message. Default: 0x68.

RTP ToS/DiffServ Value

Value for the ToS field of voice data packets.

Sets the priority for voice packets in data traffic.

Default: 0xb8.

#### SIP Settings

Parameter

Description

SIP Transport

Select the transport protocol for SIP messages:

UDP

TCP

TLS

AUTO

AUTO allows the phone to select the appropriate protocol automatically, based on the NAPTR records on the DNS server. See Configure the SIP Transport for more details.

Default: UDP

SIP Port

The phone's port number for SIP message listening and transmission.

Specify the port number here only when you are using UDP as the SIP transport protocol.

If you are using TCP, the system uses a random port within the range specified in SIP TCP Port Min and SIP TCP Port Max on the Voice > SIP tab.

If you need to specify a port of SIP proxy server, you can specify it using the Proxy field ( Proxy and Registration ) or the XSI Host Server field ( XSI Line Service ).

Default: 5060

SIP 100REL Enable

Support of 100REL SIP extension for reliable transmission of provisional responses (18x) and use of PRACK requests. Select Yes to enable.

Default: No

EXT SIP Port

The external SIP port number.

Auth Resync-Reboot

The Cisco IP Phone authenticates the sender when it receives a NOTIFY message with the following requests:

resync

reboot

report

restart

XML-service

Select Yes to enable.

Default: Yes

SIP Proxy-Require

The SIP proxy can support a specific extension or behavior when it sees this header from the user agent. If this field is
                                             configured and the proxy does not support it, it responds with the message, unsupported. Enter the appropriate header in the
                                             field provided.

SIP Remote-Party-ID

The Remote-Party-ID header to use instead of the From header. Select Yes to enable.

Default: Yes

Referor Bye Delay

Controls when the phone sends BYE to terminate stale call legs upon completion of call transfers. Multiple delay settings
                                             (Referor, Refer Target, Referee, and Refer-To Target) are configured on this screen. For the Referror Bye Delay, enter the
                                             appropriate period of time in seconds.

Default: 4

Refer-To Target Contact

Indicates the refer-to target. Select Yes to send the SIP Refer to the contact.

Default: No

Referee Bye Delay

For the Referee Bye Delay, enter the appropriate period of time in seconds.

Default: 0

Refer Target Bye Delay

For the Refer Target Bye Delay, enter the appropriate period of time in seconds.

Default: 0

Sticky 183

When enabled, the IP telephony ignores further 180 SIP responses after receiving the first 183 SIP response for an outbound
                                             INVITE. To enable this feature, select Yes . Otherwise, select No .

Default: No

Auth INVITE

When enabled, authorization is required for initial incoming INVITE requests from the SIP proxy. To enable this feature, select Yes .

Default: No

Ntfy Refer On 1xx-To-Inv

If set to Yes , as a transferee, the phone will send a NOTIFY with Event:Refer to the transferor for any 1xx response returned by the transfer
                                             target, on the transfer call leg.

If set to No , the phone will only send a NOTIFY for final responses (200 and higher).

Set G729 annexb

Configure G.729 Annex B settings.

User Equal Phone

When a tel URL is converted to a SIP URL and the phone number is represented by the user portion of the URL, the SIP URL includes
                                             the optional : user=phone parameter (RFC3261). For example:

To: sip:+12325551234@example.com; user=phone

To enable this optional parameter, select Yes .

Default: No

Call Recording Protocol

Determines the type of recording protocol that the phone uses. Options are:

SIPINFO

SIPREC

Default: SIPREC

Privacy Header

Sets user privacy in the SIP message in the trusted network.

The privacy header options are:

Disabled (default)

none—The user requests that a privacy service applies no privacy functions to this SIP message.

header—The user needs a privacy service to obscure headers which cannot be purged of identifying information.

session—The user requests that a privacy service provide anonymity for the sessions.

user—The user requests a privacy level only by intermediaries.

id—The user requests that the system substitute an id that doesn't reveal the IP address or host name.

Default: Disabled

P-Early-Media Support

Controls whether the P-Early-Media header is included in the SIP message for an outgoing call.

To include the P-Early-Media header, select Yes . Otherwise, select No .

Default: No

#### Call Feature Settings

Parameter

Description

Blind Attn-Xfer Enable

Enables the phone to perform an attended transfer operation by ending the current call leg and performing a blind transfer
                                             of the other call leg. If this feature is disabled, the phone performs an attended transfer operation by referring the other
                                             call leg to the current call leg while maintaining both call legs. To use this feature, select Yes. Otherwise, select No.

Default: No

Message Waiting

Indicates whether the Message Waiting Indicator on the phone is lit. This parameter toggles a message from the SIP proxy to
                                             indicate if a message is waiting.

Auth Page

Specifies whether to authenticate the invite before auto answering a page.

Default: No

Default Ring

Type of ring heard. Choose from No Ring or 1 through 10.

Ring options are Sunlight, Chirp 1, Chirp 2, Delight, Evolve, Mellow, Mischief, Reflections, Ringer, Ascent, Are you there,
                                             and Chime.

Auth Page Realm

Identifies the Realm part of the Auth that is accepted when the Auth Page parameter is set to Yes. This parameter accepts
                                             alphanumeric characters.

Conference Bridge URL

URL used to join a conference call, generally in the form of the word conference or user@IPaddress:port.

Auth Page Password

Identifies the password used when the Auth Page parameter is set to Yes. This parameter accepts alphanumeric characters.

Mailbox ID

Identifies the voice mailbox number/ID for the phone.

Voice Mail Server

Identifies the SpecVM server for the phone, generally the IP address, and port number of the VM server.

Voice Mail Subscribe Interval

The expiration time, in seconds, of a subscription to a voice mail server.

Auto Ans Page On Active Call

Determines the behavior of the phone when a page call arrives.

Feature Key Sync

Enable the synchronization of settings between the line and the server if necessary.

Feature Key Sync must be enabled for lines that are configured for the following functions or users:

Call forward all

DND

Call Park Monitor Enable

BroadSoft server-only feature. If call park is enabled on the server or on any of the programmable line keys, you need to
                                             enable this field for call park notification to work.

Default: No

Enable Broadsoft Hoteling

When this parameter is set to yes, the phone sends out subscription messages (without body) to the server.

Default: No

Hoteling Subscription Expires

An expiration value that is added in the subscription message. Default value is 3600.

Secure Call Option

The secure call feature works only when the SIP Transport on the Ext (n) tab is set to TLS .

Enables secured calls on an extension. Options are:

Optional: The phone maintains the current behavior for secure calls.

Required: The phone rejects nonsecure calls from other phones.

Default: Optional

#### ACD Settings

Parameter

Description

Broadsoft ACD

Enables the phone for Automatic Call Distribuion (ACD). Select Yes to enable or No to disable.

Default: No

Call Information Enable

Enables the phone to display details of a call center call. Select Yes to enable or No to disable.

Default: No

Disposition Code Enable

Enables the user to add a disposition code. Select Yes to enable or No to disable.

Default: No

Trace Enable

Enables the user to trace the last incoming call. Select Yes to enable or No to disable.

Default: No

Emergency Escalation Enable

Enables the user to escalate a call to a supervisor in case of emergency. Select Yes to enable or No to disable.

Default: No

Queue Status Notification Enable

Displays the call center status and the agent status. Select Yes to enable or No to disable.

Default: No

#### Proxy and Registration

Parameter

Description

Proxy

SIP proxy server and port number set by the service provider for all outbound requests. For example: 192.168.2.100:6060.

The port number is optional. If you don't specify a port, the default port 5060 is used for UDP, and the default port 5061
                                             is used for TLS.

When you need to refer to this proxy in another setting, for example, the speed dial line key configuration, use the $PROXY macro variable.

Outbound Proxy

All outbound requests are sent as the first hop. Enter an IP address or domain name.

Alternate Proxy

Alternate Outbound Proxy

This feature provides fast fall back when there is network partition at the Internet or when the primary proxy (or primary
                                             outbound proxy) is not responsive or available. The feature works well in a Verizon deployment environment as the alternate
                                             proxy is the Integrated Service Router (ISR) with analog outbound phone connection.

Enter the proxy server addresses and port numbers in these fields. After the phone is registered to the primary proxy and
                                             the alternate proxy (or primary outbound proxy and alternate outbound proxy), the phone always sends out INVITE and Non-INVITE
                                             SIP messages (except registration) via the primary proxy. The phone always registers to both the primary and alternate proxies.
                                             If there is no response from the primary proxy after timeout (per the SIP RFC spec) for a new INVITE, the phone attempts to
                                             connect with the alternate proxy. The phone always tries the primary proxy first, and immediately tries the alternate proxy
                                             if the primary is unreachable.

Active transactions (calls) never fall back between the primary and alternate proxies. If there is fall back for a new INVITE,
                                             the subscribe/notify transaction will fall back accordingly so that the phone's state can be maintained properly. You must
                                             also set Dual Registration in the Proxy and Registration section to Yes.

Use OB Proxy In Dialog

Determines whether to force SIP requests to be sent to the outbound proxy within a dialog. Ignored if the Use Outbound Proxy field is set to No or if the Outbound Proxy field is empty.

Default: Yes

Register

Enables periodic registration with the proxy. This parameter is ignored if a proxy is not specified. To enable this feature,
                                             select Yes .

Default: Yes

Make Call Without Reg

Enables making outbound calls without successful (dynamic) registration by the phone. If set to No, the dial tone plays only
                                             when registration is successful. To enable this feature, select Yes .

Default: No

Register Expires

Defines how often the phone renews registration with the proxy. If the proxy responds to a REGISTER with a lower expires value,
                                             the phone renews registration based on that lower value instead of the configured value.

If registration fails with an “Expires too brief” error response, the phone retries with the value specified in the Min-Expires
                                             header of the error.

The range is from 32 to 2000000.

Default: 3600 seconds

Ans Call Without Reg

If enabled, the user does not have to be registered with the proxy to answer calls.

Default: No

Use DNS SRV

Enables DNS SRV lookup for the proxy and outbound proxy. To enable this feature, select Yes . Otherwise, select No .

Default: No

DNS SRV Auto Prefix

Enables the phone to automatically prepend the proxy or outbound proxy name with _sip._udp when performing a DNS SRV lookup
                                             on that name.

Default: No

Proxy Fallback Intvl

Sets the delay after which the phone retries from the highest priority proxy (or outbound proxy) after it has failed over
                                             to a lower priority server.

The phone should have the primary and backup proxy server list from a DNS SRV record lookup on the server name. It needs to
                                             know the proxy priority; otherwise, it does not retry.

The range is from 0 to 65535.

Default: 3600 seconds

Proxy Redundancy Method

Select Normal or Based on SRV Port . The phone creates an internal list of proxies returned in the DNS SRV records.

If you select Normal, the list contains proxies ranked by weight and priority.

If you select Based on SRV Port, the phone uses normal, then inspects the port number based on the first-listed proxy port.

Default: Normal

Dual Registration

Set to Yes to enable the Dual registration/Fast Fall back feature. To enable the feature you must also configure the alternate proxy/alternate
                                             outbound proxy fields in the Proxy and Registration section.

Auto Register When Failover

If set to No, the fallback happens immediately and automatically. If the Proxy Fallback Intvl is exceeded, all the new SIP
                                             messages go to the primary proxy.

If set to Yes, the fallback happens only when current registration expires, which means only a REGISTER message can trigger
                                             fallback.

For example, when the value for Register Expires is 3600 seconds and Proxy Fallback Intvl is 600 seconds, the fallback is
                                             triggered 3600 seconds later and not 600 seconds later. When the value for Register Expires is 600 seconds and Proxy Fallback
                                             Intvl is 1000 seconds, the fallback is triggered at 1200 seconds. After successfully registering back to primary server, all
                                             the SIP messages go to primary server.

#### Subscriber Information

Parameter

Description

Display Name

Name displayed as the caller ID.

User ID

Extension number for this line.

When you need to refer to this user ID in another setting, for example, the short name for a line key, use the $USER macro variable.

Password

Password for this line.

Default: Blank (no password required)

Auth ID

Authentication ID for SIP authentication.

Default: Blank

SIP URI

The parameter by which the user agent will identify itself for
                                             this line. If this field is blank, the actual URI used in the SIP
                                             signaling should be automatically formed as:

sip:UserName@Domain

where UserName is the username given for this line in the User ID, and Domain is the domain given for this profile in the
                                             User Agent Domain. If the User Agent Domain is an empty string, then the IP address of the phone should be used for the domain.

If the URI field is not empty, but if a SIP or SIPS URI contains no @ character, the actual URI used in the SIP signaling
                                             should be automatically formed by appending this parameter with an @ character followed by the IP address of the device.

#### XSI Line Service

Parameter

Description

XSI Host Server

Enter the name of the server; for example, .

xsi.iop1.broadworks.net

XSI Host Server uses http protocol by default. To enable XSI over HTTPS, you can specify https:// in the server.

For example:

https://xsi.iop1.broadworks.net

You can also specify a port for the server.

For example:

https://xsi.iop1.broadworks.net:5061

If you don't specify a port. The default port for the specified protocol is used.

Default: Blank

XSI Authentication Type

Determines the XSI authentication type. Select Login Credentials to authenticate access with Login User ID and Login Password. Select SIP Credentials to authenticate access with the register Auth ID and Password of the SIP account registered on the phone.

Default: Login Credentials

Login User ID

BroadSoft User ID of the phone user; for example, johndoe@xdp.broadsoft.com.

For any XSI Authentication Type, you must enter Login User ID . Without Login User ID , the BroadWorks Anywhere feature does not work.

Default: Blank

Login Password

Alphanumeric password associated with the Login User ID.

Enter Login Password, when you select Login Credentials for XSI authentication type.

Default: Blank

Anywhere Enable

Enables BroadWorks Anywhere feature on an extension.

If you choose Yes , Anywhere is enabled on this line, and the user can use the phone menu to add multiple locations to this specific line.

Default: Yes

Block CID Enable

Enables XSI Caller ID blocking on a line.

Choose Yes to enable the synchronization of blocking caller id status with the server using XSI interface. Choose No to use the phone's local blocking caller id settings.

CFWD Enable

Enables or disables call forwarding status sync on a line via XSI service.

Choose Yes to enable the phone to synchronize the call forwarding status with the server using the XSI service. Choose No to disable this feature.

When Feature Key Sync is set to Yes , FKS takes precedent over XSI synchronization.

If XSI host server and credentials are not entered and the CFWD Enable field is set to Yes , the phone user can't forward calls on the phone.

DND Enable

Enables or disables DND status sync on a line via XSI service.

Choose Yes to enable the phone to synchronize DND status with the server using the XSI service. Choose No to disable this feature.

When Feature Key Sync is set to Yes , FKS takes precedent over XSI synchronization.

If XSI host server and credentials are not entered and the DND Enable field is set to Yes , the phone user can't turn on DND mode on the phone.

#### Audio
                              	 Configuration

Parameter

Description

Preferred Codec

Preferred codec for all calls. The actual codec used in a call still depends on the outcome of the codec negotiation protocol.

Select one of the following:

G711u

G711a

G729a

G729ab

G722

G722.2

iLBC

OPUS

iSAC

Default: G711u

Use Pref Codec Only

Select No to use any code. Select Yes to use only the preferred codes. When you select Yes, calls fail if the far end does not support the preferred codecs.

Default: No

Second Preferred Codec

Codec to use if the first codec fails.

Default: Unspecified

Third Preferred Codec

Codec to use if the second codec fails.

Default: Unspecified

G711u Enable

Enables use of the G.711u codec.

Default: Yes

G711a Enable

Enables use of the G.711a codec.

Default: Yes

G729a Enable

To enable use of the G.729a codec at 8 kbps, select Yes . Otherwise, select No .

Default: Yes

G722 Enable

Enables use of the G.722 codec.

Default: Yes

G722.2 Enable

Enables use of the G.722.2 codec.

Default: No

iLBC Enable

Enables use of the iLBC codec.

Default: Yes

OPUS Enable

Enables the use of OPUS codec.

Default: Yes

Silence Supp Enable

To enable silence suppression so that silent audio frames are
                                             					 not transmitted, select Yes . Otherwise, select No .

Default: No

DTMF Tx Method

The method for transmitting DTMF signals to the far end. The
                                             					 options are:

AVT—Audio video transport. Sends DTMF as AVT events.

InBand—Sends DTMF by using the audio path.

Auto—Uses InBand or AVT based on the outcome of codec
                                                   						  negotiation.

INFO—Uses the SIP INFO method.

Codec Negotiation

When set to Default, the Cisco IP phone responds to an Invite with a 200 OK response advertising the preferred codec only.
                                             When set to List All, the Cisco IP phone responds listing all the codecs that the phone supports. The default value is Default,
                                             or to respond with the preferred codec only.

Encryption Method

Encryption method to be used during secured call. Options are AES 128 and AES 256 GCM

Default: 128.

#### Dial Plan

Parameter

Description

Dial Plan

Dial plan script for the selected extension.

uid – The authentication user-id

pwd – The authentication password

nat – If this parameter is present, use NAT mapping.

Separate each parameter with a semi-colon (;).

Caller ID Map

Inbound caller ID numbers can be mapped to a different string. For example, a number that begins with +44xxxxxx can be mapped
                                                to 0xxxxxx. This feature has the same syntax as the Dial Plan parameter. With this parameter, you can specify how to map a
                                                caller ID number for display on screen and recorded into call logs.

Enable URI Dialing

Enables or disables URI dialing.

Emergency Number

Enter a comma-separated list of emergency numbers. When one of these numbers is dialed, the unit disables processing of CONF,
                                                HOLD, and other similar softkeys or buttons to avoid accidentally putting the current call on hold. The phone also disables
                                                hook flash event handling.

Only the far end can terminate an emergency call. The phone is restored to normalcy after the call is terminated and the receiver
                                                is back on-hook.

Maximum number length is 63 characters. Defaults to blank (no emergency number).

#### E911 Geolocation Configuration

##### E911 Geolocation Configuration

Parameter

Description

Company UUID

The Universally Unique Identifier (UUID) assigned to the customer by the emergency call services provider.

Maximum identifier length is 128 characters. Defaults to blank.

Primary Request URL

Encrypted HTTPS phone location request. The request uses the phone IP addresses, MAC address, Network Access Identifier (NAI),
                                                and chassis ID and port ID assigned by the network switch manufacturer. The request also includes the location server name
                                                and the customer identifier.

The server used by the emergency call services provider responds with an Emergency Response Location (ERL) that has a location
                                                Uniform Resource Identifier (URI) tied to the user phone IP address.

Defaults to blank.

Secondary Request URL

Encrypted HTTPS request sent to the emergency call services provider's backup server to obtain the user's phone location.

Defaults to blank.

See Emergency Call Support Terminology for terms that describe emergency call support for phones.

User

#### Hold Reminder

Parameter

Description

Hold Reminder Timer

Specifies the time delay (in seconds), that a ring splash is heard on an active call when another call was placed on hold.

Default: 0

Hold Reminder Ringtone

Specifies the volume of the timer ringtone.

#### Call Forward

Parameter

Description

Cfwd Setting

Select Yes to enable call forwarding.

Cfwd All Dest

Enter the extensions to which the call is forwarded.

Cfwd Busy Dest

Enter the extensions to forward calls to when the line is busy.

Default: voicemail

Cfwd No Ans Dest

Enter the extension to forward calls to when the call is not answered.

Default: voicemail

Cfwd No Ans Delay

Enter the delay in time (in seconds) to wait before forwarding a call that is unanswered.

Default: 20 seconds

#### Speed Dial

Parameter

Description

Speed Dial Name (2 to 9)

Name assigned to a specific speed dial number.

Default: Blank

Speed Dial Number 2 to 9)

Target phone number (or URL) assigned to speed dial 2, 3, 4, 5, 6, 7, 8, or 9. Press the digit key (2-9) to dial out the assigned
                                                number.

Default: Blank

#### Supplementary Services

Parameter

Description

CW Setting

Enables or disables the Call Waiting service.

Default: Yes

Block CID Setting

Enables or disables the Block CID service.

Default: No

Block ANC Setting

Enables or disables the Block ANC service.

Default: No

DND Setting

Enables or disables the DND settings options for a user.

Handset LED Alert

Enables or disables LED alert on the handset. Options are: Voicemail and Voicemail, Missed Call.

Default: Voicemail

Secure Call Setting

Enables or disables Secure Call.

Default: No

Auto Answer Page

Enables or disables automatic answering of paged calls.

Default: Yes

Preferred Audio Device

Choose the type of audio that the phone will use. Options are: Speaker and Headset.

Choose the type of audio that the phone will use. Options are: Speaker and Headset.

Default: None

Time Format

Choose the time format for the phone (12 or 24 hour).

Default: 12hr

Date Format

Choose the date format for the phone (month/day or day/month).

Default: month/day

Miss Call Shortcut

Enables or disables the option for creating a missed call shortcut.

Alert Tone Off

Enables or disables the alert tone.

Log Missed Calls for EXT (n)

Enables or disables the missed calls logs for a specific extension.

Shared Line DND Cfwd Enable

Enable/disable the Shared Line DND Call Forward.

#### Audio Volume

Parameter

Description

Ringer Volume

Sets the default volume for the ringer.

Default: 9

Speaker Volume

Sets the default volume for the speakerphone.

Default: 8

Handset Volume

Sets the default volume for the handset.

Default: 10

Headset Volume

Sets the default volume for the headset.

Default: 10

Electronic Hookswitch Control

Enables or disables the Electronic HookSwitch (EHS) feature.

After EHS is enabled, the AUX port does not output phone logs.

#### Audio Compliance

Parameter

Description

Compliant Standard

Specifies the compliance standard for the phone audio. The available options are:

ETSI : A set of standards for speech and multimedia transmission for the narrowband and wideband terminals from European Telecommunications
                                                      Standards Institute (ETSI).

TIA : A set of standards from US Telecommunications Industry Association (TIA). The standards are for narrowband and wideband
                                                      audio transmission via wired telephones.

Default: TIA

#### Screen

Parameter

Description

Screen Saver Enable

Enables a screen saver on the phone. When the phone is idle for
                                             					 a specified time, it enters screen saver mode.

Default: No

Screen Saver Type

Clock : Displays a digital clock on a plain background.

Download Picture : Displays a picture pushed from the phone webpage.

Lock : Enables locking of the screensaver.

Screen Saver Wait

Amount of idle time before screen saver displays.

enter the number of seconds of idle time to elapse before the screen saver starts.

Default: 300

Screen Saver Refresh Period

Number of seconds before the screen saver should refresh (if, for example, you chose a rotation of pictures).

Back Light Timer

Number of seconds for which the back light timer will be on.

LCD Contrast

Value for desired contrast.

Logo Type

Type of logo displayed on the phone screen. Options you can choose:

Default

Download Picutre

Text Logo

Text Logo

Text logo to display when the phone boots up. A service
                                             					 provider, for example, can enter logo text as follows:

Up to 2 lines of text

Each line must be fewer than 32 characters

Insert a new line character (\n) between lines

Insert escape code %0a

```
Super\n%0aTelecom
```

```
Super
```

```
Telecom
```

Use the + character to add spaces for formatting. For example,
                                             					 you can add multiple + characters before and after the text to center it.

Picture Download URL

URL locating the (.png) file to display on the phone screen background.

For more information, see the Phone Information and Display Settings .

Att Console

#### General

The attendant console tab, labeled Att Console , is only available in Admin Login > advanced mode.

Parameter

Description

Subscribe Expires

Specifies how long the subscription remains valid. After the specified period of time elapses, the Cisco Attendant Console
                                                initiates a new subscription.

Default: 1800

Subscribe Retry Interval

Specifies the length of time to wait to try again if the subscription fails.

Default: 30

Subscribe Delay

Length of delay before attempting to subscribe.

Default: 1

Server Type

Specifies the server type with which the phone is connected.

Options available:

BroadSoft

SPA9000

Asterisk

RFC3265_4235

Sylantro

The Uniform Resource Identifier (URI) of the Busy Lamp Field (BLF) list that you have set up for a user of the phone, on the
                                                BroadSoft server.

This field is only applicable if the phone is registered to a BroadSoft server. The BLF list is the list of users whose lines
                                                the phone is allowed to monitor. See Phone Configuration for Monitoring Other Phones for details.

The BLF List URI must be specified in the format <URI name>@<server> . The BLF List URI specified must be the same as the value configured for the List URI: sip parameter on the BroadSoft server.

Default: Blank

Example XML configuration:

```
<BLF_List_URI ua="na">MonitoredUsersList@sipurash22.com</BLF_List_URI>
```

Controls whether the phone uses its line keys to monitor the BLF list, when monitoring of the BLF list is active.

This setting only has significance when BLF List is set to Show .

Default: No

Example XML configuration:

```
<Use_Line_Keys_For_BLF_List ua="na">Yes</Use_Line_Keys_For_BLF_List>
```

Features that users are allowed to configure on line keys.

To allow a feature, add the corresponding option as shown below. Separate options with the semi-colon (;).

Speed dial: sd

Busy Lamp Field (BLF) key to monitor a user: blf

Call pickup from a monitored line: cp

Default: sd;

Adding the sd option automatically allows users to configure speed dial to a monitored line (speed dial with BLF) when the blf option is added.

Example, to allow all features:

```
sd;blf;cp
```

Example XML configuration:

```
<Customizable_PLK_options ua="na">sd;</Customizable_PLK_options>
```

Activates or deactivates monitoring of the BLF list.

When set to Show , the phone assigns available line keys in sequence, to monitor the BLF list entries. The labels of the BLF list keys show
                                                the names of the monitored users and the status of the monitored lines.

This setting only has significance when BLF List URI is configured.

Example XML configuration:

```
<BLF_List ua="rw">Show</BLF_List>
```

BXfer to Starcode Enable

When set to Yes , the phone performs a blind transfer when the *code is defined in a speed dial extended function,. If set to No , the current call is held and a new call is started to the speed dial destination.

Default: No

BXfer On Speed Dial Enable

When set to Yes , the phone performs a blind transfer when the speed dial function key is selected. When set to no, the current connected
                                                call is held and a new call to the speed dial destination is started.

For example, when a user parks a call using the speed dial function, if the parameter is enabled, a blind transfer is performed
                                                to the parking lot. If the parameter is not enabled, an attended transfer is performed to the parking lot.

Default: No

BXfer To Remote Party Number Enable

When set to Yes , the phone performs a blind transfer to a remote number. When set to no, blind transfer to remote number is disabled.

BLF Label Display Mode

Options to select a mode which displays on the phone screen for BLF.

Default: Blank

#### Unit

Enter the programming information for each line key for the Attendant Console unit.

Parameter

Description

Unit Enable

Indicates whether the key expansion module that is added to the phone is enabled.

Unit Online

Indicates whether the key expansion module that is added to the phone is active.

HW Version

Displays the hardware version of the key expansion module that is added to the phone..

SW Version

Displays the software version of the key expansion module that is added to the phone.

TR-069

#### TR-069

Parameter

Description

Enable TR-069

Settings that enables or disables the TR-069 function.

Default: Disabled

ACS URL

URL of the ACS that uses the CPE WAN Management Protocol. This parameter must be in the form of a valid HTTP or HTTPS URL.
                                             The host portion of this URL is used by the CPE to validate the ACS certificate when it uses SSL or TLS.

ACS Username

Username that authenticates the CPE to the ACS when ACS uses the CPE WAN Management Protocol. This username is used only for
                                             HTTP-based authentication of the CPE.

If the user name is not configured, admin is used as default.

ACS Password

Password to access to the ACS for a specific user. This password is used only for HTTP-based authentication of the CPE.

If the password is not configured, admin is used as default.

ACS URL In Use

URL of the ACS that is currently in use. This is a read-only field.

Connection Request URL

URL of the ACS that makes the connection request to the CPE.

Connection Request Username

Username that authenticates the ACS that makes the connection request to the CPE.

Connection Request Password

Password used to authenticate the ACS that makes a connection request to the CPE.

Periodic Inform Interval

Default value is 20 seconds.

Periodic Inform Enable

Settings that enables or disables the CPE connection requests. Default value is Yes.

TR-069 Traceability

Settings that enables or disables TR-069 transaction logs.

The default value is No.

CWMP V1.2 Support

Settings that enables or disables CPE WAN Management Protocol (CWMP) support. If set to disable, the phone does not send any
                                             Inform messages to the ACS nor accept any connection requests from the ACS.

Default value is Yes.

TR-069 VoiceObject Init

Settings to modify voice objects. Select Yes to initialize all voice objects to factory default values or select No to retain
                                             the current values.

TR-069 DHCPOption Init

Settings to modify DHCP settings. Select Yes to initialize the DHCP settings from the ACS or select No to retain the current
                                             DHCP settings.

TR-069 Fallback Support

Settings that enables or disables the TR-069 fallback support.

If the phone attempts to discover the ACS with DHCP and is unsuccessful, the phone next uses DNS to resolve the ACS IP address.

BACKUP ACS URL

Backup URL of the ACS that uses the CPE WAN Management Protocol. This parameter must be in the form of a valid HTTP or HTTPS
                                             URL. The host portion of this URL is used by the CPE to validate the ACS certificate when it uses SSL or TLS.

BACKUP ACS User

Backup username that authenticates the CPE to the ACS when ACS uses the CPE WAN Management Protocol. This username is used
                                             only for HTTP-based authentication of the CPE.

BACKUP ACS Password

Backup password to access to the ACS for a specific user. This password is used only for HTTP-based authentication of the
                                             CPE.

If you do not configure the above parameters, you can also fetch them through DHCP options 60,43, and 125.

### Call History

Displays the call history for the phone.  To change the information displayed, select the type of call history from the following
                                 tabs:

All Calls

Missed

Received

Placed

Select Add to Directory to add the call information to your Personal Directory.

### Personal Directory

The Personal Directory allows a user to store a set of personal numbers.  Directory entries can include the following contact
                                 information:

No. (the directory number)

Name

Work

Mobile

Home

Speed Dials

To edit contact information, click Edit Contacts .

| Step 1 | On the phone administration web page, go to Voice > System > Optional Network Configuration . |
|---|---|
| Step 2 | Configure the Syslog Identifier parameter as described in Optional Network Configuration . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Status > Product Information . When a user password is set, a corresponding icon (lock or certificate) displays at the top-right corner of the phone screen. |
| Step 3 | To exit the Model Information screen, press Back . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Status > Phone Status > Phone Status . You can view the following information: Elapsed time —Total time elapsed since the last reboot of the system Tx (Packets) —Transmitted packets from the phone. Rx (Packets) —Received packets from the phone. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Status > Status messages . You can view a log of the various phone statuses since provisioning was last done. Note Status messages reflect UTC time and are not affected by the timezone settings on the phone. | Note | Status messages reflect UTC time and are not affected by the timezone settings on the phone. |
| Note | Status messages reflect UTC time and are not affected by the timezone settings on the phone. |
| Step 3 | Press Back . |

| Note | Status messages reflect UTC time and are not affected by the timezone settings on the phone. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Status > Network Status . You can view the following information: Network type —Indicates the type of Local Area Netwrok (LAN) connection that the phone uses. Network status —Indicates if the phone is connected to a network. IPv4 status —IP address of the phone. You can see information on IP address, Addressing type, IP status, Subnet mask, Default router,
                                                   Domain Name Server (DNS) 1, DNS 2 of the phone. IPv6 status —IP address of the phone. You can see information on IP address, Addressing type, IP status, Subnet mask, Default router,
                                                   Domain Name Server (DNS) 1, DNS 2 of the phone. VLAN ID —VLAN ID of the phone. MAC address —Unique Media Access Control (MAC) address of the phone. Host name —Displays the current host name assigned to the phone. Domain —Displays the network domain name of the phone. Default: cisco.com Switch port link —Status of the switch port. Switch port config —Indicates speed and duplex of the network port. PC port config —Indicates speed and duplex of the PC port. PC port link —Indicates speed and duplex of the PC port. |

| Note | You can also remotely view the call statistics information by using a web browser to access the Streaming Statistics web page.
                                             This web page contains additional RTCP statistics that are not available on the phone. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Status > Phone Status > Call Statistics . |
| Step 3 | Press Back . |

| Item | Description |
|---|---|
| Receiver Codec | Type of received voice stream (RTP streaming audio from codec): G.729 G.722 G.711 mu-law G.711 A-law OPUS iLBC |
| Sender Codec | Type of transmitted voice stream (RTP streaming audio from codec): G.729 G.722 G.711 mu-law G.711 A-law OPUS iLBC |
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

| Step 1 | On the Phone Web page, select Admin Login > Info > Status . |
|---|---|
| Step 2 | In the Product Information section, you can view the customization state of the phone in the Customization field. If any provisioning is failing, you can view the details in the Provisioning Status section on the same page. |

| Parameter | Description |
|---|---|
| Host Name | Displays the current host name assigned to the phone. |
| Domain | Displays the network domain name of the phone. Default: cisco.com |
| Primary NTP Server | Displays the primary NTP server assigned to the phone. |
| Secondary NTP Server | Displays the secondary NTP server assigned to the phone. |

| Parameter | Description |
|---|---|
| IP Status | Indicates that the connection is established. |
| Connection Type | Indicates the type of internet connection for the phone: DHCP Static IP |
| Current IP | Displays the current IP address assigned to the IP phone. |
| Current Netmask | Displays the network mask assigned to the phone. |
| Current Gateway | Displays the default router assigned to the phone. |
| Primary DNS | Displays the primary DNS server assigned to the phone. |
| Secondary DNS | Displays the secondary DNS server assigned to the phone. |

| Parameter | Description |
|---|---|
| IP Status | Indicates that the connection is established. |
| Connection Type | Indicates the type of internet connection for the phone: Static IP DHCP |
| Current IP | Displays the current IPv6 address assigned to the IP phone. |
| Prefix Length | Identifies number of bits of a global unicast IPv6 address that are part of`the network. For example, if the IPv6 address
                                                is 2001:0DB8:0000:000b::/64, the number 64 identifies that the first 64 bits are part of the network. |
| Current Gateway | Displays the default router assigned to the phone. |
| Primary DNS | Displays the primary DNS server assigned to the phone. |
| Secondary DNS | Displays the secondary DNS server assigned to the phone. |

| Parameter | Description |
|---|---|
| Product Name | Model number of the phone. |
| Software Version | Version number of the phone firmware. |
| MAC Address | Hardware address of the phone. |
| Customization | For an RC unit, this field indicates whether the unit has been customized or not. Pending indicates a new RC unit that is
                                                ready for provisioning. If the unit has already retrieved its customized profile, this field displays the name of the company
                                                that provisioned the unit. |
| Serial Number | Serial number of the phone. |
| Hardware Version | Version number of the phone hardware. |
| Client Certificate | Status of the client certificate, which authenticates the phone for use in the ITSP network. This field indicates if the client
                                                certificate is properly installed in the phone. |

| Parameter | Description |
|---|---|
| Locale download status | Displays the downloaded locale package status. |
| Locale download URL | Displays the location from where the local package is downloaded. |
| Font download status | Displays the downloaded font file status. |
| Font download URL | Displays the location from where the font file is downloaded. |

| Parameter | Description |
|---|---|
| Current Time | Current date and time of the system; for example, 08/06/14 1:42:56 a.m. |
| Elapsed Time | Total time elapsed since the last reboot of the system; for example, 7 days, 02:13:02. |
| SIP Messages Sent | Total number of SIP messages sent (including retransmissions). |
| SIP Bytes Sent | Total number of SIP messages received (including retransmissions). |
| SIP Messages Recv | Total number of bytes of SIP messages sent which includes retransmissions. |
| SIP Bytes Recv | Total number of bytes of SIP messages received (including retransmissions). |
| Network Packets Sent | Total number of network packets sent. |
| Network Packets Recv | Total number of network packets received. |
| External IP | External IP of the phone. |
| Operational VLAN ID | ID of the VLAN currently in use if applicable. |
| SW Port | Displays the type of Ethernet connection from the IP phone to the switch. |
| PC Port | Displays the type of Ethernet connection from PC Port. |
| Upgrade Status | Displays status of the last phone upgrade. |
| SW Port Config | Displays the type of SW port configuration. |
| PC Port Config | Displays the type of PC port configuration. |
| Last Successful Login | Displays the time when the phone has last successful log in. |
| Last Failed Login | Displays the time when the phone has last failed log in. |

| Parameter | Description |
|---|---|
| Transaction status | Indicates if the phone is authenticated. |
| Protocol | Displays the protocol of the registered phone. |

| Parameter | Description |
|---|---|
| Registration State | Shows “Registered” if the phone is registered, or “Not Registered” if the phone is not registered to the ITSP. |
| Last Registration At | Last date and time the line was registered. |
| Next Registration In Seconds | Number of seconds before the next registration renewal. |
| Message Waiting | Indicates whether message waiting is enabled or disabled. |
| Mapped SIP Port | Port number of the SIP port mapped by NAT. |
| Hoteling State | Indicates whether Hoteling is enabled or disabled. |
| Extended Function Status | Indicates whether extended function is enabled. |

| Parameter | Description |
|---|---|
| Call State | Status of the call. |
| Tone | Type of tone that the call uses. |
| Encoder | Codec used for encoding. |
| Decoder | Codec used for decoding. |
| Type | Direction of the call. |
| Remote Hold | Indicates whether the far end placed the call on hold. |
| Callback | Indicates whether the call was triggered by a call back request. |
| Mapped RTP Port | The port mapped for Real Time Protocol traffic for the call. |
| Peer Name | Name of the internal phone. |
| Peer Phone | Phone number of the internal phone. |
| Duration | Duration of the call. |
| Packets Sent | Number of packets sent. |
| Packets Recv | Number of packets received. |
| Bytes Sent | Number of bytes sent. |
| Bytes Recv | Number of bytes received. |
| Decode Latency | Number of milliseconds for decoder latency. |
| Jitter | Number of milliseconds for receiver jitter. |
| Round Trip Delay | Number of milliseconds for delay in the RTP-to-RTP interface round trip. |
| Packets Lost | Number of packets lost. |
| Loss Rate | The fraction of RTP data packets from the source lost since the beginning of reception. Defined in RFC-3611—RTP Control Protocol
                                                Extended Reports (RTCP XR). |
| Packet Discarded | The fraction of RTP data packets from the source lost since the beginning of reception. Defined in RFC-3611—RTP Control Protocol
                                                Extended Reports (RTCP XR). |
| Discard Rate | The fraction of RTP data packets from the source that have been discarded since the beginning of reception, due to late or
                                                early arrival, under-run or overflow at the receiving jitter buffer. Defined in RFC-3611—RTP Control Protocol Extended Reports
                                                (RTCP XR). |
| Burst Duration | The mean duration, expressed in milliseconds, of the burst periods that have occurred since the beginning of reception. Defined
                                                in RFC-3611—RTP Control Protocol Extended Reports (RTCP XR). |
| Gap Duration | The mean duration, expressed in milliseconds, of the gap periods that have occurred since the beginning of reception. Defined
                                                in RFC-3611—RTP Control Protocol Extended Reports (RTCP XR). |
| R-Factor | Voice quality metric that describes the segment of the call that is carried over this RTP session. Defined in RFC-3611—RTP
                                                Control Protocol Extended Reports (RTCP XR). |
| MOS-LQ | The estimated mean opinion score for listening quality (MOS-LQ) is a voice quality metric on a scale from 1 to 5, in which
                                                5 represents excellent and 1 represents unacceptable. Defined in RFC-3611—RTP Control Protocol Extended Reports (RTCP XR). |
| MOS-CQ | The estimated mean opinion score for conversational quality (MOS-CQ) is defined as including the effects of delay and other
                                                effects that affect conversational quality. Defined in RFC-3611—RTP Control Protocol Extended Reports (RTCP XR). |

| Parameter | Description |
|---|---|
| Multicast Rx Pkts | Indicates Rx packets during a multicast paging. |
| Multicast Tx Pkts | Indicates Tx packets during a multicast paging. |

| Parameter | Description |
|---|---|
| TR-069 Feature | Indicates if TR-069 function is enabled or disabled. |
| Periodic Inform Time | Displays the inform time interval from CPE to ACS. |
| Last Inform Time | Indicates the last inform time. |
| Last Transaction Status | Displays the success or the failure status. |
| Last Session | Indicates the start and end time of the session. |
| ParameterKey | Displays the key for reference checkpoint for parameter set configured. |

| Parameter | Description |
|---|---|
| PRT Generation Status | The location of initiation and status of generation of the most recently initiated problem report. Problem reports may be initiated from the phone LCD user interface, from the phone administration web page, or remotely. See Report All Phone Issues from the Phone Web Page and Report a Phone Problem Remotely for details. XML tag in status.xml : PRT_Generation_Status |
| PRT Upload Status | The status of upload of the most recently initiated problem report. See Configure PRT Upload for information on configuring an upload rule for problem reports. XML tag in status.xml : PRT_Upload_Status |

| Parameter | Description |
|---|---|
| Custom CA Provisioning Status | Indicates whether provisioning using a custom CA succeeded or failed: Last provisioning succeeded on mm/dd/yyyy HH:MM:SS; Last provisioning failed on mm/dd/yyyy HH:MM:SS |
| Custom CA Info | Displays information about the custom CA: Installed—Displays the "CN Value" , where "CN Value" is the value of the CN parameter for the Subject field in the first certificate. Not Installed—Displays if no custom CA certificate is installed. |

| Parameter | Description |
|---|---|
| Provisioning Profile | Displays the profile file name of the phone. |
| Provisioning Status 1 | Displays the provisioning status (resync) of the phone. |
| Provisioning Status 2 |
| Provisioning Status 3 |
| Provisioning Failure Reason | Displays the reason for the failure of provisioning of the phone. |

| Note | The Upgrade and Provisioning Status are displayed in reverse chronological order (like reboot history). Each entry gives the
                                                status, time, and reason. |
|---|---|

| Parameter | Description |
|---|---|
| Debug Message | Displays debug messages when you click messages link. |

| Parameter | Description |
|---|---|
| Report Problem | Displays the tab Generate PRT. |
| Prt file | Displays the file name of the PRT logs. |
| Packet Capture | Displays the tab Start Packet Capture . Click this tab to initiate capture packets. Click All to capture all packets that the phone receives or click Host IP Address to capture packets only when src/dest is the IP address of the phone. You can also stop the capture process after initiating it. |
| Capture File | Displays the file that contains the captured packets. Download the file to see the packet details. |

| Parameter | Description |
|---|---|
| Factory Reset | Resets the phone when you click Factory Reset tab when the phone is idle. |

| Parameter | Description |
|---|---|
| Firmware Upgrade Status 1 | Displays the upgrade status (failed or succeeded) with reason for the same. |
| Firmware Upgrade Status 2 |
| Firmware Upgrade Status 3 |

| Parameter | Description |
|---|---|
| Provisioning Status 1 | Displays the provisioning status (resync) of the phone. |
| Provisioning Status 2 |
| Provisioning Status 3 |

| Parameter | Description |
|---|---|
| Custom CA Provisioning Status | Indicates whether provisioning using a custom CA succeeded or failed: Last provisioning succeeded on mm/dd/yyyy HH:MM:SS; Last provisioning failed on mm/dd/yyyy HH:MM:SS |
| Custom CA Info | Displays information about the custom CA: Installed—Displays the "CN Value" , where "CN Value" is the value of the CN parameter for the Subject field in the first certificate. Not Installed—Displays if no custom CA certificate is installed. |

| Parameter | Description |
|---|---|
| TxFrames | Total number of packets that the phone transmitted. |
| TxBroadcasts | Total number of broadcast packets that the phone transmitted. |
| TxMulticasts | Total number of multicast packets that the phone transmitted. |
| TxUnicasts | Total number of unicast packets that the phone transmitted. |
| RxFrames | Total number of packets received by the phone. |
| RxBroadcasts | Total number of broadcast packets that the phone received. |
| RxMulticasts | Total number of multicast packets that the phone received. |
| RxUnicasts | Total number of unicast packets that the phone received. |

| Parameter | Description |
|---|---|
| RxtotalPkt | Total number of packets that the phone received. |
| Rxunicast | Total number of unicast packets that the phone received. |
| Rxbroadcast | Total number of broadcast packets that the phone received. |
| Rxmulticast | Total number of multicast packets that the phone received. |
| RxDropPkts | Total number of packets dropped. |
| RxUndersizePkts | The total number of packets received that are less than 64 octets long, which excludes framing bits, but includes FCS octets,
                                             and are otherwise well formed. |
| RxOversizePkts | The total number of packets received that are longer than 1518 octets, which excludes framing bits, but includes FCS octets,
                                             and are otherwise well formed. |
| RxJabbers | The total number of packets received that are longer than 1518 octets, which excludes framing bits, but incudes FCS octets,
                                             and do not end with an even number of octets (alignment error), or had an FCS error. |
| RxAlignErr | Total number of packets between 64 and 1522 bytes in length that were received and that had a bad Frame Check Sequence (FCS). |
| Rxsize64 | Total number of received packets, including bad packets, that were between 0 and 64 bytes in size. |
| Rxsize65to127 | Total number of received packets, including bad packets, that were between 65 and 127 bytes in size. |
| Rxsize128to255 | Total number of received packets, including bad packets, that were between 128 and 255 bytes in size. |
| Rxsize256to511 | Total number of received packets, including bad packets, that were between 256 and 511 bytes in size. |
| Rxsize512to1023 | Total number of received packets, including bad packets, that were between 512 and 1023 bytes in size. |
| Rxsize1024to1518 | Total number of received packets, including bad packets, that were between 1024 and 1518 bytes in size. |
| TxtotalGoodPkt | Total number of good packets (multicast, broadcast, and unicast) that the phone received. |
| lldpFramesOutTotal | Total number of LLDP frames that the phone sent out. |
| lldpAgeoutsTotal | Total number of LLDP frames that timed out in the cache. |
| lldpFramesDiscardedTotal | Total number of LLDP frames that were discarded when any of the mandatory TLVs is missing, out of order, or contains out of
                                             range string length. |
| lldpFramesInErrorsTotal | Total number of LLDP frames that were received with one or more detectable errors. |
| lldpFramesInTotal | Total number of LLDP frames that the phone received. |
| lldpTLVDiscardedTotal | Total number of LLDP TLVs that were discarded. |
| lldpTLVUnrecognizedTotal | Total number of LLDP TLVs that were not recognized on the phone. |
| CDPNeighborDeviceId | Identifier of a device connected to this port that CDP discovered. |
| CDPNeighborIP | IP address of the neighbor device discovered that CDP discovered. |
| CDPNeighborPort | Neighbor device port to which the phone is connected discovered by CDP. |
| LLDPNeighborDeviceId | Identifier of a device connected to this port discovered by LLDP discovered. |
| LLDPNeighborIP | IP address of the neighbor device that LLDP discovered. |
| LLDPNeighborPort | Neighbor device port to which the phone connects that LLDP discovered. |
| PortSpeed | Speed and duplex information. |

| Parameter | Description |
|---|---|
| RxtotalPkt | Total number of packets that the phone received. |
| Rxunicast | Total number of unicast packets that the phone received. |
| Rxbroadcast | Total number of broadcast packets that the phone received. |
| Rxmulticast | Total number of multicast packets that the phone received. |
| RxDropPkts | Total number of packets dropped. |
| RxUndersizePkts | The total number of packets received that are less than 64 octets long, which excludes framing bits, but includes FCS octets,
                                             and are otherwise well formed. |
| RxOversizePkts | The total number of packets received that are longer than 1518 octets, which excludes framing bits, but includes FCS octets,
                                             and are otherwise well formed. |
| RxJabbers | The total number of packets received that are longer than 1518 octets, which excludes framing bits, but incudes FCS octets,
                                             and do not end with an even number of octets (alignment error), or had an FCS error. |
| RxAlignErr | Total number of packets between 64 and 1522 bytes in length that were received and that had a bad Frame Check Sequence (FCS). |
| Rxsize64 | Total number of received packets, including bad packets, that were between 0 and 64 bytes in size. |
| Rxsize65to127 | Total number of received packets, including bad packets, that were between 65 and 127 bytes in size. |
| Rxsize128to255 | Total number of received packets, including bad packets, that were between 128 and 255 bytes in size. |
| Rxsize256to511 | Total number of received packets, including bad packets, that were between 256 and 511 bytes in size. |
| Rxsize512to1023 | Total number of received packets, including bad packets, that were between 512 and 1023 bytes in size. |
| Rxsize1024to1518 | Total number of received packets, including bad packets, that were between 1024 and 1518 bytes in size. |
| TxtotalGoodPkt | Total number of good packets (multicast, broadcast, and unicast) that the phone received. |
| lldpFramesOutTotal | Total number of LLDP frames that the phone sent out. |
| lldpAgeoutsTotal | Total number of LLDP frames that timed out in the cache. |
| lldpFramesDiscardedTotal | Total number of LLDP frames that were discarded when any of the mandatory TLVs is missing, out of order, or contains out of
                                             range string length. |
| lldpFramesInErrorsTotal | Total number of LLDP frames that were received with one or more detectable errors. |
| lldpFramesInTotal | Total number of LLDP frames that the phone received. |
| lldpTLVDiscardedTotal | Total number of LLDP TLVs that were discarded. |
| lldpTLVUnrecognizedTotal | Total number of LLDP TLVs that were not recognized on the phone. |
| CDPNeighborDeviceId | Identifier of a device connected to this port that CDP discovered. |
| CDPNeighborIP | IP address of the neighbor device discovered that CDP discovered. |
| CDPNeighborPort | Neighbor device port to which the phone is connected discovered by CDP. |
| LLDPNeighborDeviceId | Identifier of a device connected to this port discovered by LLDP discovered. |
| LLDPNeighborIP | IP address of the neighbor device that LLDP discovered. |
| LLDPNeighborPort | Neighbor device port to which the phone connects that LLDP discovered. |
| PortSpeed | Speed and duplex information. |

| Parameter | Description |
|---|---|
| Restricted Access Domains | This feature is used when implementing software customization. |
| Enable Web Server | Enable/disable web server of the IP phone. Default: Yes |
| Enable Protocol | Choose the type of protocol: Http Https If you specify the HTTPS protocol, you must include https: in the URL. Default: Http |
| Enable Direct Action Url | Enables the direct action of the URL. Default: Yes |
| Session Max Timeout | Allows you to enter maximum timeout of the session. Default: 3600 |
| Session Idle Timeout | Allows you to enter idle timeout of the session. Default: 3600 |
| Web Server Port | Allows you to enter port number of the phone web user interface. Default: 80 80 for protocol HTTP. 443 for protocol HTTPS. If you specify a port number other than the default value for that protocol, you must include the nondefault port number in
                                                the server URL. Example: https://192.0.2.1:999/admin/advanced |
| Enable Web Admin Access | Allows you to enable or disable local access to the phone web user interface. Select Yes or No from the drop-down menu. Default: Yes |
| Admin Password | Allows you to enter password for the administrator. Default: Blank |
| User Password | Allows you to enter password for the user. Default: Blank |
| Phone-UI-readonly | Allows you to make the phone menus and options that the phone users see as read-only fields. Default: No |
| Phone-UI-User-Mode | Allows you to restrict the menus and options that phone users see when they use the phone interface. Choose yes to enable
                                                this parameter and restrict access. Default: No Specific parameters are then designated as "na" , "ro" , or "rw" using provisioning files. Parameters designated as "na" don't appear on the phone screen. Parameters designated as "ro" aren't editable by the user. Parameters designated as "rw" are editable by the user. |
| Block Nonproxy SIP | Enables or disables the phone receiving SIP messages from non-proxy server. If you choose Yes , the phone blocks any incoming non-proxy SIP messages except IN-dialog message. If you choose No , the phone does not block any incoming non-proxy SIP messages. Set Block Nonproxy SIP to No for phones that use TCP or TLS to transport SIP messages. Nonproxy SIP messages transported over TCP or TLS are blocked
                                                by default. Default: No |

| Parameter | Description |
|---|---|
| IP Mode | Allows you to select the internet protocol mode in which the phone operates. Options are: IPv4 Only, IPv6 Only, and Dual Mode.
                                                In dual mode, the phone can have both IPv4 and IPv6 addresses. Default: Dual Mode |

| Parameter | Description |
|---|---|
| Connection Type | Internet connection type that is configured for the phone. Options are DHCP and Static IP. Default: DHCP |
| NetMask | Subnet mask of the phone. |
| Static IP | IP address of the phone. |
| Gateway | IP address of the gateway. |
| Primary DNS | Primary Domain Name Server (DNS) assigned to the phone. |
| Secondary DNS | Secondary Domain Name Server (DNS) if assigned to the phone. |

| Parameter | Description |
|---|---|
| Connection Type | Internet connection type that is configured for the phone. Options are DHCP and Static IP. Default: DHCP |
| Static IP | IPv6 address of the phone. |
| Prefix Length | Identifies number of bits of a global unicast IPv6 address that are part of`the network. For example, if the IPv6 address
                                                is 2001:0DB8:0000:000b::/64, the number 64 identifies that the first 64 bits are part of the network. |
| Gateway | IP address of the gateway. |
| Primary DNS | Primary Domain Name Server (DNS) assigned to the phone. |
| Secondary DNS | Secondary Domain Name Server (DNS) if assigned to the phone. |
| Broadcast Echo | Options are Disabled and Enabled. Default: Disabled |
| Auto Config | When enabled, phone generates an IPv6 address by default with the prefix length sent from the router. Options are Disabled
                                                and Enabled. Default: Enabled |

| Parameter | Description |
|---|---|
| Enable 802.1X Authentication | Enables/disables 802.1X Default: No |

| Parameter | Description |
|---|---|
| Host Name | The hostname of the Cisco IP Phone. |
| Domain | The network domain of the Cisco IP Phone. If you are using LDAP, see LDAP Configuration . |
| DNS Server Order | Specifies the method for selecting the DNS server: Manual, DHCP Manual DHCP,Manual |
| DNS Query Mode | Specified mode of DNS query. Parallel Sequential |
| DNS Caching Enable | When set to Yes, the DNS query results are not cached. Default: Yes |
| Switch Port Config | Allows you to select speed and duplex of the network port. Values are: Auto 10MB half 10MB full 100 MB half 100MB full 100 half 1000 full |
| PC Port Config | Allows you to select Speed and duplex of the Computer (access) port. Auto 10MB half 10MB full 100 MB half 100MB full 100 half 1000 full |
| PC PORT Enable | Specifies if PC port is enabled. Options are Yes or No. |
| Enable PC Port Mirror | Adds the ability to port mirror on the PC port. When enabled, you can see the packets on the phone. Select Yes to enable PC port mirroring and select No to disable it. |
| Syslog Server | Specify the syslog server name and port. This feature specifies the server for logging IP phone system information and critical
                                                events. If both Debug Server and Syslog Server are specified, Syslog messages are also logged to the Debug Server. |
| Syslog Identifier | Select the device identifier to include in syslog messages that are uploaded to the syslog server. The device identifier appears
                                                after the timestamp in each message. None: No device identifier. $MA: The MAC address of the phone, expressed as continuous lower case letters and digits. Example: c4b9cd811e29 $MAU: The MAC address of the phone, expressed as continuous upper case letters and digits. Example: C4B9CD811E29 $MAC: The MAC address of the phone in the standard colon-separated format. Example: c4:b9:cd:81:1e:29 $SN: The product serial number of the phone. Default: None Example XML configuration: <Syslog_Identifier ua="na">$MAC</Syslog_Identifier> |
| Debug Level | The debug level from 0 to 2. The higher the level, the more debug information is generated. Zero (0) means that no debug information
                                                is generated. To log SIP messages, you must set the Debug Level to at least 2. Default: 0 |
| Primary NTP Server | IP address or name of the primary NTP server used to synchronize its time. Default: Blank |
| Secondary NTP Server | IP address or name of the secondary NTP server used to synchronize its time. Default: Blank |
| Enable SSLv3 | Choose Yes to enable SSLv3. Choose No to disable. Default: No |

| Parameter | Description |
|---|---|
| Enable VLAN | Choose Yes to enable VLAN. Choose No to disable. |
| Enable CDP | Enable CDP only if you are using a switch that has Cisco Discovery Protocol. CDP is negotiation based and determines which
                                                VLAN the IP phone resides in. |
| Enable LLDP-MED | Choose Yes to enable LLDP-MED for the phone to advertise itself to devices that use that discovery protocol. When the LLDP-MED feature is enabled, after the phone has initialized and Layer 2 connectivity is established, the phone sends
                                                out LLDP-MED PDU frames. If the phone receives no acknowledgment, the manually configured VLAN or default VLAN will be used
                                                if applicable. If the CDP is used concurrently, the waiting period of 6 seconds is used. The waiting period will increase
                                                the overall startup time for the phone. |
| Network Startup Delay | Setting this value causes a delay for the switch to get to the forwarding state before the phone will send out the first LLDP-MED
                                                packet. The default delay is 3 seconds. For configuration of some switches, you might need to increase this value to a higher
                                                value for LLDP-MED to work. Configuring a delay can be important for networks that use Spanning Tree Protocol. |
| VLAN ID | If you use a VLAN without CDP (VLAN enabled and CDP disabled), enter a VLAN ID for the IP phone. Note that only voice packets
                                                are tagged with the VLAN ID. Do not use 1 for the VLAN ID. |
| PC Port VLAN ID | VLAN ID for the PC port. |
| DHCP VLAN Option | A predefined DHCP VLAN option to learn the voice VLAN ID. You can use the feature only when no voice VLAN information is available
                                                by CDP/LLDP and manual VLAN methods. CDP/LLDP and manual VLAN are all disabled. Valid values are: Null 128 to 149 151 to 158 161 to 254 Set the value to Null to disable DHCP VLAN option. Cisco recommends that you use DHCP Option 132. |

| Parameter | Description |
|---|---|
| Asset ID | Provides the ability to enter an asset ID for inventory management when using LLDP-MED. The default value for Asset ID is
                                                empty. Enter a string of less than 32 characters if you are using this field. The Asset ID can be provisioned only by using the web management interface or remote provisioning. The Asset ID is not displayed
                                                on the phone screen. Changing the Asset ID field causes the phone to reboot. |

| Parameter | Description |
|---|---|
| Max Forward | SIP Max Forward value, which can range from 1 to 255. Default: 70 |
| Max Redirection | Number of times an invite can be redirected to avoid an infinite loop. Default: 5 |
| Max Auth | Maximum number of times (from 0 to 255) a request can be challenged. Default: 2 |
| SIP User Agent Name | Used in outbound REGISTER requests. Default: $VERSION If empty, the header is not included. Macro expansion of $A to $D corresponding to GPP_A to GPP_D allowed |
| SIP Server Name | Server header used in responses to inbound responses. Default: $VERSION |
| SIP Reg User Agent Name | User-Agent name to be used in a REGISTER request. If this is not specified, the SIP User Agent Name is also used for the REGISTER
                                                request. Default: Blank |
| SIP Accept Language | Accept-Language header used. To access, click the SIP tab, and fill in the SIP Accept Language field. There is no default. If empty, the header is not included. |
| DTMF Relay MIME Type | MIME Type used in a SIP INFO message to signal a DTMF event. This field must match that of the Service Provider. Default: application/dtmf-relay |
| Hook Flash MIME Type | MIME Type used in a SIPINFO message to signal a hook flash event. |
| Remove Last Reg | Enables you to remove the last registration before registering a new one if the value is different. Select yes or no from
                                                the drop-down menu. |
| Use Compact Header | If set to yes, the phone uses compact SIP headers in outbound SIP messages. If inbound SIP requests contain normal headers,
                                                the phone substitutes incoming headers with compact headers. If set to no, the phones use normal SIP headers. If inbound SIP
                                                requests contain compact headers, the phones reuse the same compact headers when generating the response, regardless of this
                                                setting. Default: No |
| Escape Display Name | Enables you to keep the Display Name private. Select Yes if you want the IP phone to enclose the string (configured in the Display Name) in a pair of double quotes for
                                                outbound SIP messages. Default: Yes. |
| Talk Package | Enables support for the BroadSoft Talk Package that lets users answer or resume a call by clicking a button in an external
                                                application. Default: No |
| Hold Package | Enables support for the BroadSoft Hold Package, which lets users place a call on hold by clicking a button in an external
                                                application. Default: No |
| Conference Package | Enables support for the BroadSoft Conference Package that enables users to start a conference call by clicking a button in
                                                an external application. Default: No |
| RFC 2543 Call Hold | If set to yes, unit includes c=0.0.0.0 syntax in SDP when sending a SIP re-INVITE to the peer to hold the call. If set to
                                                no, unit will not include the c=0.0.0.0 syntax in the SDP. The unit will always include a=sendonly syntax in the SDP in either
                                                case. Default: Yes |
| Random REG CID on Reboot | If set to yes, the phone uses a different random call-ID for registration after the next software reboot. If set to no, the
                                                Cisco IP phone tries to use the same call-ID for registration after the next software reboot. The Cisco IP phone always uses
                                                a new random Call-ID for registration after a power-cycle, regardless of this setting. Default: No. |
| SIP TCP Port Min | Specifies the lowest TCP port number that can be used for SIP sessions. Default: 5060 |
| SIP TCP Port Max | Specifies the highest TCP port number that can be used for SIP sessions. Default: 5080 |
| Caller ID Header | Provides the option to take the caller ID from PAID-RPID-FROM, PAID-FROM, RPID-PAID-FROM, RPID-FROM, or FROM header. Default: PAID-RPID-FROM |
| Hold Target Before Refer | Controls whether to hold call leg with transfer target before sending REFER to the transferee when initiating a fully-attended
                                                call transfer (where the transfer target has answered). Default: No |
| Dialog SDP Enable | When enabled and the Notify message body is too big causing fragmentation, the Notify message xml dialog is simplified; Session
                                                Description Protocol (SDP) is not included in the dialog xml content. |
| Keep Referee When Refer Failed | If set to yes, it configures the phone to immediately handle NOTIFY sipfrag messages. |
| Display Diversion Info | Display the Diversion info included in SIP message on LCD or not. |
| Display Anonymous From Header | Show the caller ID from the SIP INVITE message “From” header when set to Yes, even if the call is an anonymous call. When
                                                the parameter is set to no, the phone displays "Anonymous Caller" as the caller ID. |
| Sip Accept Encoding | Supports the content-encoding gzip feature. The options are none and gzip. If gzip is selected, the SIP message header contains the string “Accept-Encoding: gzip”, and the phone is able to process
                                                the SIP message body, which is encoded with the gzip format. |
| Disable Local Name To Header | The options are No and Yes. If No is selected, no changes are made. The default value is No. If Yes is selected, it disables the display name in “Directory”, “Call History”, and in the “To” header during an outgoing
                                                call. |
| SIP IP Preference | Sets if the phone uses IPv4 or IPv6. Default: IPv4. |

| Parameter | Description |
|---|---|
| SIP T1 | RFC 3261 T1 value (RTT estimate) that can range from 0 to 64 seconds. Default: 0.5 seconds |
| SIP T2 | RFC 3261 T2 value (maximum retransmit interval for non-INVITE requests and INVITE responses) that can range from 0 to 64 seconds. Default: 4 seconds |
| SIP T4 | RFC 3261 T4 value (maximum duration a message remains in the network), which can range from 0 to 64 seconds. Default: 5 seconds. |
| SIP Timer B | INVITE time-out value, which can range from 0 to 64 seconds. Default: 16 seconds. |
| SIP Timer F | Non-INVITE time-out value, which can range from 0 to 64 seconds. Default: 16 seconds. |
| SIP Timer H | INVITE final response, time-out value, which can from 0 to 64 seconds. Default: 16 seconds. |
| SIP Timer D | ACK hang-around time, which can range from 0 to 64 seconds. Default: 16 seconds. |
| SIP Timer J | Non-INVITE response hang-around time, which can range from 0 to 64 seconds. Default: 16 seconds. |
| INVITE Expires | INVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Ranges from 0 to 2000000. Default: 240 seconds |
| ReINVITE Expires | ReINVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Ranges from 0 to
                                                2000000. Default: 30 |
| Reg Min Expires | Minimum registration expiration time allowed from the proxy in the Expires header or as a Contact header parameter. If the
                                                proxy returns a value less than this setting, the minimum value is used. |
| Reg Max Expires | Maximum registration expiration time allowed from the proxy in the Min-Expires header. If the value is larger than this setting,
                                                the maximum value is used. |
| Reg Retry Intv | Interval to wait before the Cisco IP Phone retries registration after failing during the last registration.The range is from
                                                1 to 2147483647 Default: 30 See the note below for additional details. |
| Reg Retry Long Intvl | When registration fails with a SIP response code that does not match<Retry Reg RSC>, the Cisco IP Phone waits for the specified
                                                length of time before retrying. If this interval is 0, the phone stops trying. This value should be much larger than the Reg
                                                Retry Intvl value, which should not be 0. Default: 1200 See the note below for additional details. |
| Reg Retry Random Delay | Random delay range (in seconds) to add to <Register Retry Intvl> when retrying REGISTER after a failure. Minimum and maximum
                                                random delay to be added to the short timer. The range is from 0 to 2147483647. Default: 0 |
| Reg Retry Long Random Delay | Random delay range (in seconds) to add to <Register Retry Long Intvl> when retrying REGISTER after a failure. Default: 0 |
| Reg Retry Intvl Cap | Maximum value of the exponential delay. The maximum value to cap the exponential backoff retry delay (which starts at the
                                                Register Retry Intvl and doubles every retry). Defaults to 0, which disables the exponential backoff (that is, the error retry
                                                interval is always at the Register Retry Intvl). When this feature is enabled, the Reg Retry Random Delay is added to the
                                                exponential backoff delay value. The range is from 0 to 2147483647. Default: 0 |
| Sub Min Expires | Sets the lower limit of the REGISTER expires value returned from the Proxy server. |
| Sub Max Expires | Sets the upper limit of the REGISTER minexpires value returned from the Proxy server in the Min-Expires header. Default: 7200. |
| Sub Retry Intvl | This value (in seconds) determines the retry interval when the last Subscribe request fails. Default: 10. |

| Note | The phone can use a RETRY-AFTER value when it is received from a SIP proxy server that is too busy to process a request (503
                                                Service Unavailable message). If the response message includes a RETRY-AFTER header, the phone waits for the specified length
                                                of time before to REGISTER again. If a RETRY-AFTER header is not present, the phone waits for the value specified in the Reg
                                                Retry Interval or the Reg Retry Long Interval. |
|---|---|

| Parameter | Description |
|---|---|
| Try Backup RSC | This parameter may be set to invoke failover upon receiving specified response codes. Default: Blank For example, you can enter numeric values 500 or a combination of numeric values plus wild cards if multiple values are possible.
                                                For the later, you can use 5?? to represent all SIP Response messages within the 500 range. If you want to use multiple ranges,
                                                you can add a comma "," to delimit values of 5?? and 6?? |
| Retry Reg RSC | Interval to wait before the phone retries registration after failing during the last registration. Default: Blank For example, you can enter numeric values 500 or a combination of numeric values plus wild cards if multiple values are possible.
                                                For the later, you can use 5?? to represent all SIP Response messages within the 500 range. If you want to use multiple ranges,
                                                you can add a comma "," to delimit values of 5?? and 6?? |

| Parameter | Description |
|---|---|
| RTP Port Min | Minimum port number for RTP transmission and reception. Minimum port number for RTP transmission and reception. Should define
                                                a range that contains at least 10 even number ports (twice the number of lines); for example, configure RTP port min to 16384
                                                and RTP port max to 16538. Default: 16384 |
| RTP Port Max | Maximum port number for RTP transmission and reception. Should define a range that contains at least 10 even number ports
                                                (twice the number of lines); for example, configure RTP port min to 16384 and RTP port max to 16538. The maximum value for the RTP port must be lesser than 49152. Default: 16538 |
| RTP Packet Size | Packet size in seconds, which can range from 0.01 to 0.13. Valid values must be a multiple of 0.01 seconds. Default: 0.02 |
| Max RTP ICMP Err | Number of successive ICMP errors allowed when transmitting RTP packets to the peer before the phone terminates the call. If
                                                value is set to 0, the phone ignores the limit on ICMP errors. |
| RTCP Tx Interval | Interval for sending out RTCP sender reports on an active connection. It can range from 0 to 255 seconds. Default: 0 |
| SDP IP Preferences | Select IPv4 or IPv6. Default: IPv4 If the phone is in dual-mode and has both ipv4 and ipv6 addresses, it will always include both addresses in SDP by attributes
                                                "a=altc … If  IPv4 address is selected, then ipv4 address has higher priority than ipv6 address in SDP and indicates that phone prefers
                                                using ipv4 RTP address. If the phone has only ipv4 address or ipv6 address,  SDP does not have ALTC attributes and RTP address is specified in “c=”
                                                line. |

| Parameter | Description |
|---|---|
| G722.2 Dynamic Payload | G722 Dynamic Payload type. Default: 96 |
| iLBC Dynamic Payload | iLBC Dynamic Payload type. Default: 97 |
| iSAC Dynamic Payload | iSAC Dynamic Payload type. Default: 98 |
| OPUS Dynamic Payload | OPUS Dynamic Payload type. Default: 99 |
| AVT Dynamic Payload | AVT dynamic payload type. Ranges from 96-127. Default: 101 |
| INFOREQ Dynamic Payload | INFOREQ Dynamic Payload type. |
| H264 BP0 Dynamic Payload | H264 BPO Dynamic Payload type. Default: 110 |
| H264 HP Dynamic Payload | H264 HP Dynamic Payload type. Default: 110 |
| G711u Codec Name | G711u codec name used in SDP. Default: PCMU |
| G711a Codec Name | G711a codec name used in SDP. Default: PCMA |
| G729a Codec Name | G729a codec name used in SDP. Default: G729a |
| G729b Codec Name | G729b codec name used in SDP. Default: G729b |
| G722 Codec Name | G722 codec name used in SDP. Default: G722 |
| G722.2 Codec Name | G722.2 codec name used in SDP. Default: G722.2 |
| iLBC Codec Name | iLBC codec name used in SDP. Default: iLBC |
| iSAC Codec Name | iSAC codec name used in SDP. Default: iSAC |
| OPUS Codec Name | OPUS codec name used in SDP. Default: OPUS |
| AVT Codec Name | AVT codec name used in SDP. Default: telephone-event |

| Parameter | Description |
|---|---|
| Handle VIA received | Enables the phone to process the received parameter in the VIA header. Default: No |
| Handle VIA rport | Enables the phone to process the rport parameter in the VIA header. Default: No |
| Insert VIA received | Enables to insert the received parameter into the VIA header of SIP responses if the received-from IP and VIA sent-by IP values
                                                differ. Default: No |
| Insert VIA rport | Enables to insert the rport parameter into the VIA header of SIP responses if the received-from IP and VIA sent-by IP values
                                                differ. Default: No |
| Substitute VIA Addr | Enables the user to use NAT-mapped IP:port values in the VIA header. Default: No |
| Send Resp To Src Port | Enables to send responses to the request source port instead of the VIA sent-by port. Default: No |
| STUN Enable | Enables the use of STUN to discover NAT mapping. Default: No |
| STUN Test Enable | If the STUN Enable feature is enabled and a valid STUN server is available, the phone can perform a NAT-type discovery operation
                                                when it powers on. It contacts the configured STUN server, and the result of the discovery is reported in a Warning header
                                                in all subsequent REGISTER requests. If the phone detects symmetric NAT or a symmetric firewall, NAT mapping is disabled. Default: No |
| STUN Server | IP address or fully-qualified domain name of the STUN server to contact for NAT mapping discovery. You can use a public STUN
                                                server or set up your own STUN server. Default: Blank |
| EXT IP | External IP address to substitute for the actual IP address of phone in all outgoing SIP messages. If 0.0.0.0 is specified,
                                                no IP address substitution is performed. If this parameter is specified, phone assumes this IP address when generating SIP messages and SDP (if NAT Mapping is enabled
                                                for that line). Default: Blank |
| EXT RTP Port Min | External port mapping number of the RTP Port Minimum number. If this value is not zero, the RTP port number in all outgoing
                                                SIP messages is substituted for the corresponding port value in the external RTP port range. Default: 0 |
| NAT Keep Alive Intvl | Interval between NAT-mapping keep alive messages. Default: 15 |
| Redirect Keep Alive | If enabled, the IP phone redirects the keepalive message when SIP_301_MOVED_PERMANENTLY is received as the registration response. |

| Parameter | Description |
|---|---|
| Provision Enable | Allows or denies resync actions. Default: 160,159,66,150 |
| Resync On Reset | The device performs a resync operation after power-up and after each upgrade attempt when set to Yes . Default: Yes |
| Resync Random Delay | A random delay following the boot-up sequence before performing the reset, specified in seconds. In a pool of IP Telephony
                                                devices that are scheduled to simultaneously power up, this introduces a spread in the times at which each unit sends a resync
                                                request to the provisioning server. This feature can be useful in a large residential deployment, in the case of a regional
                                                power failure. The value for this field must be an integer ranging between 0 and 65535. The default value is 2. |
| Resync At (HHmm) | The time (HHmm) that the device resynchronizes with the provisioning server. The value for this field must be a four-digit number ranging from 0000 to 2400 to indicate the time in HHmm format. For example,
                                                0959 indicates 09:59. The default value is empty. If the value is invalid, the parameter is ignored. If this parameter is set with a valid value,
                                                the Resync Periodic parameter is ignored. |
| Resync At Random Delay | Prevents an overload of the provisioning server when a large number of devices power-on simultaneously. To avoid flooding resync requests to the server from multiple phones, the phone resynchronizes in the range between the hours
                                                and minutes, and the hours and minutes plus the random delay (hhmm, hhmm+random_delay). For example, if the random delay =
                                                (Resync At Random Delay + 30)/60 minutes, the input value in seconds is converted to minutes, rounding up to the next minute
                                                to calculate the final random_delay interval. The valid value ranges between 0 and 65535. This feature is disabled when this parameter is set to zero. The default value is 600 seconds (10 minutes). |
| Resync Periodic | The time interval between periodic resynchronizes with the provisioning server. The associated resync timer is active only
                                                after the first successful sync with the server. The valid formats are as follows: An integer Example: An input of 3000 indicates that the next resync occurs in 3000 seconds. Multiple integers Example: An input of 600,1200,300 indicates that the first resync occurs in 600 seconds, the second resync occurs in 1200 seconds after the first one, and
                                                      the third resync occurs in 300 seconds after the second one. A time range Example, an input of 2400+30 indicates that the next resync occurs in between 2400 and 2430 seconds after a successful resync. Set this parameter to zero to disable periodic resynchronization. The default value is 3600 seconds. |
| Resync Error Retry Delay | If a resync operation fails because the IP Telephony device was unable to retrieve a profile from the server, or the downloaded
                                                file is corrupt, or an internal error occurs, the device tries to resync again after a time specified in seconds. The valid formats are as follows: An integer Example: An input of 300 indicates that the next retry for resync occurs in 300 seconds. Multiple integers Example: An input of 600,1200,300 indicates that the first retry occurs in 600 seconds after the failure, the second retry occurs in 1200 seconds after the
                                                      failure of the first retry, and the third retry occurs in 300 seconds after the failure of the second retry. A time range Example, an input of 2400+30 indicates that the next retry occurs in between 2400 and 2430 seconds after a resync failure. If the delay is set to 0, the device does not try to resync again following a failed resync attempt. |
| Forced Resync Delay | Maximum delay (in seconds) the phone waits before performing a resynchronization. The device does not resync while one of its phone lines is active. Because a resync can take several seconds, it is desirable
                                                to wait until the device has been idle for an extended period before resynchronizing. This allows a user to make calls in
                                                succession without interruption. The device has a timer that begins counting down when all of its lines become idle. This parameter is the initial value of
                                                the counter. Resync events are delayed until this counter decrements to zero. The valid value ranges between 0 and 65535. The default value is 14,400 seconds. |
| Resync From SIP | Controls requests for resync operations via a SIP NOTIFY event sent from the service provider proxy server to the IP Telephony
                                                device. If enabled, the proxy can request a resync by sending a SIP NOTIFY message containing the Event: resync header to
                                                the device. Default: Yes |
| Resync After Upgrade Attempt | Enables or disables the resync operation after any upgrade occurs. If Yes is selected, sync is triggered. Default: Yes |
| Resync Trigger 1 Resync Trigger 2 | If the logical equation in these parameters evaluates to FALSE, Resync is not triggered even when Resync On Reset is set to
                                                TRUE. Only Resync via direct action URL and SIP notify ignores these Resync Trigger. Default: Blank |
| Resync Fails On FNF | A resync is considered unsuccessful if a requested profile is not received from the server. This can be overridden by this
                                                parameter. When it is set to No , the device accepts a file-not-found response from the server as a successful resync. Default: Yes |
| Profile Authentication Type | Specifies the credentials to use for profile account authentication. The available options are: Disabled : Disables the profile account feature. When this feature is disabled, the Profile account setup menu doesn't display on the phone screen. Basic HTTP Authentication : The HTTP login credentials are used to authenticate the profile account. XSI Authentication : XSI login credentials or XSI SIP credentials are used to authenticate the profile account. The authentication credentials
                                                      depend on the XSI Authentication Type for the phone: When the XSI Authentication Type for the phone is set to Login Credentials , the XSI login credentials are used. When the XSI Authentication Type for the phone is set to SIP Credentials , the XSI SIP credentials are used. Default: Basic HTTP Authentication |
| Profile Rule Profile Rule B Profile Rule C Profile Rule D | Each profile rule informs the phone of a source from which to obtain a profile (configuration file). During every resync operation,
                                                the phone applies all the profiles in sequence. Default: /$PSN.xml If you are applying AES-256-CBC encryption to the configuration files, specify the encryption key with the --key keyword as follows: [--key <encryption key>] You can enclose the encryption key in double-quotes (") optionally. |
| DHCP Option To Use | DHCP options, delimited by commas, used to retrieve firmware and profiles. Default: 66,160,159,150,60,43,125 |
| DHCPv6 Option To Use | DHCP options, delimited by commas, used to retrieve firmware and profiles. Default: 17,160,159 |
| Log Request Msg | The message sent to the syslog server at the start of a resync attempt. Default: $PN $MAC – Requesting % $SCHEME://$SERVIP:$PORT$PATH |
| Log Success Msg | The syslog message issued upon successful completion of a resync attempt. Default: $PN $MAC -Successful Resync  % $SCHEME://$SERVIP:$PORT$PATH |
| Log Failure Msg | The syslog message that is issued after a failed download attempt. Default: $PN $MAC -- Resync failed: $ERR |
| User Configurable Resync | Allows a user to resync the phone from the phone screen. Default: Yes |

| Field | Description |
|---|---|
| Report Rule | Specifies how the phone reports its current internal configuration to the provisioning server. The URLs in this field specify
                                                the destination for a report and can include an encryption key. You can use the following keywords, encryption key, and file locations and names to control how you store the phone configuration
                                                information: No keywords and only an XML file reports the entire configuration data to server. [--status] keyword reports the status data to server. [--delta] keyword reports the changed configuration to server. [--key <encryption key>] keyword tells the phone to apply AES-256-CBC encryption with the specified encryption key to the configuration report, before
                                                      sending it to the server. You can enclose the encryption key in double-quotes (") optionally. Note If you have provisioned the phone with Input Keying Material (IKM) and want the phone to apply RFC 8188-based encryption to
                                                               the file, do not specify a AES-256-CBC encryption key. Two rules used together as: [--delta]http://my_http_server/config-mpp-delta.xml [--status]http://my_http_server/config-mpp-status.xml Caution If you need to use the [--delta]xml-delta file rule and the [--status]xml-status file rule together, you must separate the
                                                         two rules with a space . | Note | If you have provisioned the phone with Input Keying Material (IKM) and want the phone to apply RFC 8188-based encryption to
                                                               the file, do not specify a AES-256-CBC encryption key. | Caution | If you need to use the [--delta]xml-delta file rule and the [--status]xml-status file rule together, you must separate the
                                                         two rules with a space . |
| Note | If you have provisioned the phone with Input Keying Material (IKM) and want the phone to apply RFC 8188-based encryption to
                                                               the file, do not specify a AES-256-CBC encryption key. |
| Caution | If you need to use the [--delta]xml-delta file rule and the [--status]xml-status file rule together, you must separate the
                                                         two rules with a space . |
| HTTP Report method: | Specifies whether the HTTP Request that the phone sends should be an HTTP PUT or an HTTP POST . PUT Method –To create a new report or overwrite an existing report at a known location on the server. For example, you may want to keep
                                                      overwriting each report that you send and only store the most current configuration on the server. POST Method –To send the report data to the server for processing, such as, by a PHP script. This approach provides more flexibility for
                                                      storing the configuration information. For example, you may want to send a series of phone status reports and store all the reports on the server. |
| Report to Server: | Defines when the phone reports its configuration to the provisioning servers. On Request : The phone reports its configuration only when an administrator sends a sip notify event, or the phone restarts. On Local Change : The phone reports its configuration when any configuration parameter changes by an action on the phone or on the phone administration
                                                      web page. The phone waits for a few seconds after a change is made, and then reports the configuration. This delay ensures
                                                      that changes are reported to the web server in batches, rather than reporting a single change at a time. Periodically : The phone reports its configuration at regular intervals. The interval is expressed in seconds. Example XML configuration: <Report_to_Server ua="na"> Periodically </Report_to_Server> |
| Periodic Upload to Server: | Defines the interval (in seconds) that the phone reports its configuration to the provisioning servers. This field is used only when Report to Server is set to Periodically . Default: 3600 Minimum: 600 Maximum: 2592000 (30 days) Example XML configuration: <Report_to_Server ua="na"> Periodically </Report_to_Server> <!available options: On Request \| On Local Change\| Periodically--> <periodic_upload_to_server ua="na"> 3600 </periodic_upload_to_server> <User_Configurable_Resync ua="na"> Yes </User_Configurable_Resync _ |
| Upload Delay On Local Change: | Defines the delay (in seconds) that the phone waits after a change is made, and then reports the configuration. This field is used only when Report to Server is set to On Local Change . Default: 60 Minimum: 10 Maximum: 900 Example XML configuration: <Upload_Delay_On_Local_Change ua="na"> 60 </Upload_Delay_On_Local_Change> |

| Note | If you have provisioned the phone with Input Keying Material (IKM) and want the phone to apply RFC 8188-based encryption to
                                                               the file, do not specify a AES-256-CBC encryption key. |
|---|---|

| Caution | If you need to use the [--delta]xml-delta file rule and the [--status]xml-status file rule together, you must separate the
                                                         two rules with a space . |
|---|---|

| Parameter | Description |
|---|---|
| Upgrade Enable | Allows firmware update operations independent of resync actions. Default: Yes |
| Upgrade Rule | A firmware upgrade script that defines upgrade conditions and associated firmware URLs. It uses the same syntax as Profile
                                             Rule. Use the following format to enter the upgrade rule: protocol://server[:port]/profile_pathname For example: tftp://192.168.1.5/image/sip88xx.11-1-1MPP-221.loads If no protocol is specified, TFTP is assumed. If no server-name is specified, the host that requests the URL is used as the
                                             server name. If no port is specified, the default port is used (69 for TFTP, 80 for HTTP, or 443 for HTTPS). You can also include the credentials that are used to access the server. Then, the upgrade rule is: [--uid $userID --pwd $password]protocol://server[:port]/profile_pathname For example, [--uid TEST --pwd TestAbC123]tftp://192.168.1.5/image/sip88xx.11-1-1MPP-221.loads If the user ID or the password contains special characters (/ [ & } (*) # , etc.), you need to quote them in the upgrade rule.
                                             There are two options for quoting special characters: Put the user ID or the password that contains special characters into double quotation marks (" "). This option doesn't work
                                                   for some of the special characters, such as " " [ ]. For example, [--uid TEST --pwd "Test#\AbC123"]tftp://192.168.1.5/image/sip88xx.11-1-1MPP-221.loads Use the octal encoding of the special characters. For example, escape the pond (#) with "\043" and the backslash with "\057" for the password "Test#\AbC123" in the following rule: [--uid TEST --pwd Test\043\057AbC123]tftp://192.168.1.5/image/sip88xx.11-1-1MPP-221.loads Default: Blank |
| Log Upgrade Request Msg | Syslog message issued at the start of a firmware upgrade attempt. Default: $PN $MAC -- Requesting upgrade $SCHEME://$SERVIP:$PORT$PATH |
| Log Upgrade Success Msg | Syslog message issued after a firmware upgrade attempt completes successfully. Default: $PN $MAC -- Successful upgrade $SCHEME://$SERVIP:$PORT$PATH -- $ERR |
| Log Upgrade Failure Msg | Syslog message issued after a failed firmware upgrade attempt. Default: $PN $MAC -- Upgrade failed: $ERR |
| Peer Firmware Sharing | Enables or disables the Peer Firmware Sharing feature. Select Yes or No to enable or to disable the feature. Default: Yes |
| Peer Firmware Sharing Log Server | Indicates the IP address and the port to which the UDP message is sent. For example: 10.98.76.123:514 where, 10.98.76.123 is the IP address and 514 is the port number. |

| Parameter | Description |
|---|---|
| Custom CA Rule | The URL to download Custom CA. Default: Blank |

| Parameter | Description |
|---|---|
| HTTP User Agent Name | Allows you to enter a name for HTTP user. Default: Blank |

| Parameter | Description |
|---|---|
| PRT Upload Rule | Specifies the path to the PRT upload script. You can enter the path in the format: https://proxy.example.com/prt_upload.php or http://proxy.example.com/prt_upload.php If PRT Max Timer and PRT Upload Rule fields are empty, problem reports are not generated. |
| PRT Upload Method | Determines the method used to upload PRT logs to the remote server. Options are: HTTP POST and PUT. Default: POST |
| PRT Max Timer | Determines at what interval (minutes) the phone starts generating problem report automatically. The interval range that you
                                                can set is 15 minutes to 1440 minutes. Default: Empty If PRT Max Timer and PRT Upload Rule fields are empty, problem reports are not generated. a |
| PRT Name | Defines a name for the generated PRT file. Enter the name in the format: prt-string1-$MACRO |

| Parameter | Description |
|---|---|
| GPP A - GPP P | The general purpose parameters GPP_* are used as free string, registers when configuring the Cisco IP phones to interact with
                                                a particular provisioning server solution. They can be configured to contain diverse values, including the following: Encryption keys URLs Multistage provisioning status information Post request templates Parameter name alias maps Partial string values, eventually combined into complete parameter values Default: Blank |

| Parameter | Description |
|---|---|
| Dial Tone | Prompts the user to enter a phone number. |
| Outside Dial Tone | Alternative to the Dial Tone. It prompts the user to enter an external phone number, as opposed to an internal extension.
                                             It is triggered by a, (comma) character encountered in the dial plan. |
| Prompt Tone | Prompts the user to enter a call forwarding phone number. |
| Busy Tone | Played when a 486 RSC is received for an outbound call. |
| Reorder Tone | Played when an outbound call has failed or after the far end hangs up during an established call. Reorder Tone is played automatically
                                             when <Dial Tone> or any of its alternatives times out. |
| Off Hook Warning Tone | Played when the phone receiver has been off hook after a period of time. |
| Ring Back Tone | Played during an outbound call when the far end is ringing. |
| Call Waiting Tone | Played when a call is waiting. |
| Confirm Tone | Brief tone to notify the user that the last input value has been accepted. |
| MWI Dial Tone | Played instead of the Dial Tone when there are unheard messages in the caller’s mailbox. |
| Cfwd Dial Tone | Played when all calls are forwarded. |
| Holding Tone | Informs the local caller that the far end has placed the call on hold. |
| Conference Tone | Played to all parties when a three-way conference call is in progress. |
| Secure Call Indication Tone | Played when a call has been successfully switched tosecure mode. It should be played only for a short while (less than 30
                                             seconds) and at a reduced level (less than -19 dBm) so it does not interfere with the conversation. |
| Page Tone | Specifies the tone transmitted when the paging feature is enabled. |
| Alert Tone | Played when an alert occurs. |
| Mute Tone | Played when the Mute button is pressed to mute the phone. |
| Unmute Tone | Played when the Mute button is pressed to unmute the phone. |
| System Beep | Audible notification tone played when a system error occurs. |
| Call Pickup Tone | Provides the ability to configure an audio indication for call pickup. |

| Parameter | Description |
|---|---|
| Cadence 1 | Cadence script for distinctive ring 1. Defaults to 60(2/4). |
| Cadence 2 | Cadence script for distinctive ring 2. Defaults to 60(.3/.2, 1/.2,.3/4). |
| Cadence 3 | Cadence script for distinctive ring 3. Defaults to 60(.8/.4,.8/4). |
| Cadence 4 | Cadence script for distinctive ring 4. Defaults to 60(.4/.2,.3/.2,.8/4). |
| Cadence 5 | Cadence script for distinctive ring 5. Defaults to 60(.2/.2,.2/.2,.2/.2,1/4). |
| Cadence 6 | Cadence script for distinctive ring 6. Defaults to 60(.2/.4,.2/.4,.2/4). |
| Cadence 7 | Cadence script for distinctive ring 7. Defaults to 60(4.5/4). |
| Cadence 8 | Cadence script for distinctive ring 8. Defaults to 60(0.25/9.75) |
| Cadence 9 | Cadence script for distinctive ring 9. Defaults to 60(.4/.2,.4/2). |

| Parameter | Description |
|---|---|
| Reorder Delay | Delay after far end hangs up before reorder (busy) tone is played. 0 = plays immediately, inf = never plays. Range: 0–255
                                                seconds. Set to 255 to return the phone immediately to on-hook status and to not play the tone. |
| Interdigit Long Timer | Long timeout between entering digits when dialing. The interdigit timer values are used as defaults when dialing. The Interdigit_Long_Timer
                                                is used after any one digit, if all valid matching sequences in the dial plan are incomplete as dialed. Range: 0–64 seconds. Default: 10 |
| Interdigit Short Timer | Short timeout between entering digits when dialing. The Interdigit_Short_Timer is used after any one digit, if at least one
                                                matching sequence is complete as dialed, but more dialed digits would match other as yet incomplete sequences. Range: 0–64
                                                seconds. Default: 3 |

| Parameter | Description |
|---|---|
| Call Return Code | This code calls the last caller. Defaults to *69. |
| Blind Transfer Code | Begins a blind transfer of the current call to the extension specified after the activation code. Defaults to *88. |
| Cfwd All Act Code | Forwards all calls to the extension specified after the activation code. Defaults to *72. |
| Cfwd All Deact Code | Cancels call forwarding of all calls. Defaults to *73. |
| Cfwd Busy Act Code | Forwards busy calls to the extension specified after the activation code. Defaults to *90. |
| Cfwd Busy Deact Code | Cancels call forwarding of busy calls. Defaults to *91. |
| Cfwd No Ans Act Code | Forwards no-answer calls to the extension specified after the activation code. Defaults to *92. |
| Cfwd No Ans Deact Code | Cancels call forwarding of no-answer calls. Defaults to *93. |
| CW Act Code | Enables call waiting on all calls. Defaults to *56. |
| CW Deact Code | Disables call waiting on all calls. Defaults to *57. |
| CW Per Call Act Code | Enables call waiting for the next call. Defaults to *71. |
| CW Per Call Deact Code | Disables call waiting for the next call. Defaults to *70. |
| Block CID Act Code | Blocks caller ID on all outbound calls. Defaults to *67. |
| Block CID Deact Code | Removes caller ID blocking on all outbound calls. Defaults to *68. |
| Block CID Per Call Act Code | Removes caller ID blocking on the next inbound call. Defaults to *81. |
| Block CID Per Call Deact Code | Removes caller ID blocking on the next inbound call. Defaults to *82. |
| Block ANC Act Code | Blocks all anonymous calls. Defaults to *77. |
| Block ANC Deact Code | Removes blocking of all anonymous calls. Defaults to *87. |
| DND Act Code | Enables the do not disturb feature. Defaults to *78. |
| DND Deact Code | Disables the do not disturb feature. Defaults to *79. |
| Secure All Call Act Code | Makes all outbound calls secure. Defaults to *16. |
| Secure No Call Act Code | Makes all outbound calls not secure. Defaults to *17. |
| Secure One Call Act Code | Makes a secure call. Default: *18. |
| Secure One Call Deact Code | Disables secure call feature. Default: *19. |
| Paging Code | The star code used for paging the other clients in the group. Defaults to *96. |
| Call Park Code | The star code used for parking the current call. Defaults to *38. |
| Call Pickup Code | The star code used for picking up a ringing call. Defaults to *36. |
| Call Unpark Code | The star code used for picking up a call from the call park. Defaults to *39. |
| Group Call Pickup Code | The star code used for picking up a group call. Defaults to *37. |
|  |
| Referral Services Codes | These codes tell the IP phone what to do when the user places the current call on hold and is listening to the second dial
                                                tone. One or more *code can be configured into this parameter, such as *98, or *97\|*98\|*123, and so on. Max total length is 79 chars.
                                                This parameter applies when the user places the current call on hold (by Hook Flash) and is listening to second dial tone.
                                                Each *code (and the following valid target number according to current dial plan) entered on the second dial-tone triggers
                                                the phone to perform a blind transfer to a target number that is prepended by the service *code. For example, after the user dials *98, the IP phone plays a special dial tone called the Prompt Tone while waiting for the
                                                user the enter a target number (which is checked according to dial plan as in normal dialing). When a complete number is entered,
                                                the phone sends a blind REFER to the holding party with the Refer-To target equals to *98<target_number>. This feature allows
                                                the phone to hand off a call to an application server to perform further processing, such as call park. The *codes should not conflict with any of the other vertical service codes internally processed by the IP phone. You can
                                                empty the corresponding *code that you do not want to the phone to process. |
| Feature Dial Services Codes | These codes tell the phone what to do when the user is listening to the first or second dial tone. One or more *code can be configured into this parameter, such as *72, or *72\|*74\|*67\|*82, and so forth. The maximum total
                                                length is 79 characters. This parameter applies when the user has a dial tone (first or second dial tone). Enter *code (and
                                                the following target number according to current dial plan) entered at the dial tone triggers the phone to call the target
                                                number prepended by the *code. For example, after user dials *72, the phone plays a prompt tone awaiting the user to enter
                                                a valid target number. When a complete number is entered, the phone sends a INVITE to *72<target_number> as in a normal call.
                                                This feature allows the proxy to process features like call forward (*72) or BLock Caller ID (*67). The *codes should not conflict with any of the other vertical service codes internally processed by the phone. You can empty
                                                the corresponding *code that you do not want to the phone to process. You can add a parameter to each *code in Features Dial Services Codes to indicate what tone to play after the *code is entered,
                                                such as *72‘c‘\|*67‘p‘. Below are a list of allowed tone parameters (note the use of back quotes surrounding the parameter
                                                without spaces) • c = Cfwd Dial Tone • d = Dial Tone • m = MWI Dial Tone • o = Outside Dial Tone • p = Prompt Dial Tone • s = Second Dial Tone • x = No tones are place, x is any digit not used above If no tone parameter is specified, the phone plays Prompt tone by default. If the *code is not to be followed by a phone number, such as *73 to cancel call forwarding, do not include it in this parameter.
                                                In that case, simple add that *code in the dial plan and the phone sends INVITE *73@..... as usual when user dials *73. |

| Parameter | Description |
|---|---|
| Service Annc Base Number | Defaults to blank. |
| Service Annc Extension Codes | Defaults to blank. |

| Parameter | Description |
|---|---|
| Prefer G711u Code | Makes this codec the preferred codec for the associated call. Defaults to *017110. |
| Force G711u Code | Makes this codec the only codec that can be used for the associated call. Defaults to *027110. |
| Prefer G711a Code | Makes this codec the preferred codec for the associated call. Defaults to *017111 |
| Force G711a Code | Makes this codec the only codec that can be used for the associated call. Defaults to *027111. |
| Prefer G722 Code | Makes this codec the preferred codec for the associated call. Defaults to *01722. Only one G.722 call at a time is allowed. If a conference call is placed, a SIP re-invite message is sent to switch the calls
                                                to narrowband audio. |
| Force G722 Code | Makes this codec the only codec that can be used for the associated call. Defaults to *02722. Only one G.722 call at a time is allowed. If a conference call is placed, a SIP re-invite message is sent to switch the calls
                                                to narrowband audio. |
| Prefer G722.2 Code | Makes this codec the preferred codec for the associated call. |
| Force G722.2 Code | Makes this codec the only codec that can be used for the associated call. |
| Prefer G729a Code | Makes this codec the preferred codec for the associated call. Defaults to *01729. |
| Force G729a Code | Makes this codec the only codec that can be used for the associated call. Defaults to *02729. |
| Prefer iLBC Code | Makes this codec the preferred codec for the associated call. |
| Force iLBC Code | Makes this codec the only codec that can be used for the associated call. |
| Prefer ISAC Code | Makes this codec the preferred codec for the associated call. |
| Force ISAC Code | Makes this codec the only codec that can be used for the associated call. |
| Prefer OPUS Code | Makes this codec the preferred codec for the associated call. |
| Force OPUS Code | Makes this codec the only codec that can be used for the associated call. |

| Parameter | Description |
|---|---|
| Set Local Date (mm/dd/yyyy) | Sets the local date (mm represents the month and dd represents the day). The year is optional and uses two or four digits. Default: Blank |
| Set Local Time (HH/mm) | Sets the local time (hh represents hours and mm represents minutes). Seconds are optional. Default: Blank |
| Time Zone | Selects the number of hours to add to GMT to generate the local time for caller ID generation. Choices are GMT-12:00, GMT-11:00,…,
                                                GMT, GMT+01:00, GMT+02:00, …, GMT+13:00. Default: GMT-08:00 |
| Time Offset (HH/mm) | This specifies the offset from GMT to use for the local system time. Default: 00/00 |
| Ignore DHCP Time Offset | When used with some routers that have DHCP with time offset values configured, the IP phone uses the router settings and ignores
                                                the IP phone time zone and offset settings. To ignore the router DHCP time offset value, and use the local time zone and offset
                                                settings, choose yes for this option. Choosing no causes the IP phone to use the router's DHCP time offset value. Default: Yes. |
| Daylight Saving Time Rule | Enter the rule for calculating daylight saving time; it should include the start, end, and save values. This rule is comprised
                                                of three fields. Each field is separated by ; (a semicolon) as shown below. Optional values inside [ ] (the brackets) are
                                                assumed to be 0 if they are not specified. Midnight is represented by 0:0:0 of the given date. This is the format of the rule: Start = <start-time>; end=<end-time>; save = <save-time>. The <start-time> and <end-time> values specify the start and end dates and times of daylight saving time. Each value is in
                                                this format: <month> /<day> / <weekday>[/HH:[mm[:ss]]] The <save-time> value is the number of hours, minutes, and/or seconds to add to the current time during daylight saving time.
                                                The <save-time> value can be preceded by a negative (-) sign if subtraction is desired instead of addition. The <save-time>
                                                value is in this format: [/[+\|-]HH:[mm[:ss]]] The <month> value equals any value in the range 1-12 (January-December). The <day> value equals [+\|-] any value in the range 1-31. If <day> is 1, it means the <weekday> on or before the end of the month (in other words the last occurrence of < weekday>
                                                in that month). |
| Daylight Saving Time Rule (continued) | The <weekday> value equals any value in the range 1-7 (Monday-Sunday). It can also equal 0. If the <weekday> value is 0, this
                                                means that the date to start or end daylight saving is exactly the date given. In that case, the <day> value must not be negative.
                                                If the <weekday> value is not 0 and the <day> value is positive, then daylight saving starts or ends on the <weekday> value
                                                on or after the date given. If the <weekday> value is not 0 and the <day> value is negative, then daylight saving starts or
                                                ends on the <weekday> value on or before the date given. Where: HH stands for hours (0-23). mm stands for minutes (0-59). ss stands for seconds (0-59). Default: 3/-1/7/2;end=10/-1/7/2;save=1. |
| Daylight Saving Time Enable | Enables Daylight Saving Time. Default: Yes |

| Parameter | Description |
|---|---|
| Dictionary Server Script | Use this field to specify the language options for the phone display, and the dictionary and font files required for each
                                                language. See Set Up Dictionaries and Fonts . Default: Blank |
| Language Selection | Use this field to specify the default language. The value must match one of the languages supported by the dictionary server.
                                                See Specify a Language for the Phone Display . You can configure the language through the XML Configuration file. For example: <Language_Selection ua="na"> Spanish
</Language_Selection> The language name can have up to 512 characters. |
| Locale | Use this drop-down list box to see the supported languages. See Supported Languages for the Phone Display . |

| Parameter | Description |
|---|---|
| Station Name | Name of the phone. |
| Station Display Name | Name to identify the phone; appears on the phone screen. You can use spaces in this field and the name does not have to be
                                                unique. |
| Voice Mail Number | A phone number or URL to check voice mail. Default: None |

| Parameter | Description |
|---|---|
| Bluetooth Mode | Shows the method of Bluetooth connection. Phone—Pairs with a Bluetooth headset only. Handsfree—Operates as a handsfree device with a Bluetooth-enabled mobile phone. Both—Uses a Bluetooth headset, or operates with a Bluetooth-enabled mobile phone. |
| Line | Specifies the line number for which the Bluetooth is enabled. |

| Parameter | Description |
|---|---|
| Extension | Specifies the n extension to be assigned to Line Key n. Default: n XML configuration examples: To set the line key 1 to extension 1: <Extension_1_ ua="na">1</Extension_1_> To disable the extension function for line key 2: <Extension_2_ ua="na">Disabled</Extension_2_> |
| Short Name | Specifies the user name for Line Key. Default: $USER |
| Share Call Appearance | Specifies whether the incoming call appearance is shared with other phones or it is private. |
| Extended Function | Use to assign any of the following features or functions to unused line keys on the phone: Busy Lamp Field Call Pickup Speed Dial |

| Parameter | Description |
|---|---|
| Line ID Mapping | Specifies the shared call appearance line ID mapping. If Vertical First is set, the second call makes the next available line
                                                ID LED flash. If Horizontal first is set, the second call will make the same LED flash on which the first call is received.
                                                Also, the behavior is same for both outgoing and incoming calls. Note 7811 Cisco IP Phone does not support Line ID Mapping. Default: Horizontal First | Note | 7811 Cisco IP Phone does not support Line ID Mapping. |
| Note | 7811 Cisco IP Phone does not support Line ID Mapping. |
| SCA Barge-In Enable | Enables the SCA Barge-In. Default: No |
| SCA Sticky Auto Line Seize | If enabled, restricts to automatically pick up an incoming call on a shared line when you take the phone off-hook. |
| Call Appearances Per Line | This parameter allows you to choose the number of calls per line button. You can choose a value from 2 to 10. Default: 2 |

| Note | 7811 Cisco IP Phone does not support Line ID Mapping. |
|---|---|

| Parameter | Description |
|---|---|
| Conference Serv | Enable or disable three-way conference service. Default: Yes |
| Attn Transfer Serv | Enable or disable attended-call-transfer service. Default: Yes |
| Blind Transfer Serv | Enable or disable blind-call-transfer service. Default: Yes |
| DND Serv | Enable or disable do not disturb service. Default: Yes |
| Block ANC Serv | Enable or disable block-anonymous-call service. Default: Yes |
| Block CID Serv | Enable or disable blocking outbound Caller-ID service. Default: Yes |
| Secure Call Serv | Enable or disable secured call services. Default: Yes |
| Cfwd All Serv | Enable or disable call-forward-all service. Default: Yes |
| Cfwd Busy Serv | Enable or disable call-forward-on-busy service. Default: Yes |
| Cfwd No Ans Serv | Enable or disable call-forward-no-answer service. Default: Yes |
| Paging Serv | Enable or disable paging service on the phone. Default: Yes |
| Call Park Serv | Enable or disable call park services on the phone. Default: Yes |
| Call Pick Up Serv | Enable or disable call pick up services on the phone. Default: Yes |
| ACD Login Serv | Enable or disable ACD login services on the phone. Default: Yes |
| Group Call Pick Up Serv | Enable or disable group call pick up services on the phone. Default: Yes |
| Service Annc Serv | Enable or disable the vertical service announcement services on the phone. Default: No |
| Call Recording Serv | Enable or disable the call recording services on the phone. Default: No |
| Reverse Phone Lookup Serv | Enable or disable reverse name lookup for the phone. When enabled, the phone can searches the personal address book and call history, server directory, and either the configured
                                                LDAP or XML directory. Default: Yes |

| Parameter | Description |
|---|---|
| Ring1 to Ring12 | Ring tone scripts for different rings. |
| Silent Ring Duration | Controls the duration of the silent ring. For example, if the parameter is set to 20 seconds, the phone plays the silent ring for 20 seconds then sends 480 response
                                                to INVITE message. |

| Parameter | Description |
|---|---|
| EM Enable | Options to enable or to disable the extension mobility support for the phone. Default: No |
| EM User Domain | Name of the domain for the phone or the authentication server. Default: Blank |
| Session Timer(m) | Specifies the duration of the phone session. |
| Countdown Timer(s) | Specifies the duration for which it waits before it logs out. Default: 10 |
| Preferred Password Input Mode | Options to specify the password input method of extension mobility PIN. Options are: Alpha-numeric and Numeric. Default: Alphanumeric |

| Parameter | Description |
|---|---|
| XSI Host Server | Enter the name of the server; for example, xsi.iop1.broadworks.net. Note XSI Host Server uses http protocol by default. To enable XSI over HTTPS, you can specify https:// in the server. Default: Blank | Note | XSI Host Server uses http protocol by default. To enable XSI over HTTPS, you can specify https:// in the server. |
| Note | XSI Host Server uses http protocol by default. To enable XSI over HTTPS, you can specify https:// in the server. |
| XSI Authentication Type | Determines the XSI authentication type. Select Login Credentials to authenticate access with XSI id and password. Select SIP Credentials to authenticate access with the register user ID and password of the SIP account registered on the phone. Default: Login Credentials |
| Login User ID | BroadSoft User ID of the phone user; for example, johndoe@xdp.broadsoft.com. Enter SIP Auth ID when you select Login Credentials or SIP Credentials for XSI authentication type. When you choose SIP Auth ID as SIP Credentials , you must enter Login User ID. Without Login User ID, the BroadSoft directory will not appear under the phone Directory list. Default: Blank |
| Login Password | Alphanumeric password associated with the User ID. Enter login password, when you select Login Credentials for XSI authentication type. Default: Blank |
| SIP Auth ID | The registered user ID of the SIP account registered on the phone. Enter SIP Auth ID when you select SIP Credentials for XSI authentication type. |
| SIP Password | The password of the SIP account registered on the phone. Enter SIP password when you select SIP Credentials for XSI authentication type. |
| Directory Enable | Enables BroadSoft directory for the phone user. Select Yes to enable the directory and select No to disable it. Default: No |
| Directory Name | Name of the directory. Displays on the phone as a directory choice. Default: Blank |
| Directory Type | Select the type of BroadSoft directory: Enterprise: Allows users to search on last name, first name, user or group ID, phone number, extension, department, or email
                                                address. Group: Allows users to search on last name, first name, user ID, phone number, extension, department, or email address. Personal: Allows users to search on last name, first name, or telephone number. Default: Enterprise |
| CallLog Enable | Enables to log XSI calls. Select Yes to log XSI calls and select No to disable it. Default: No |
| CallLog Associated Line | Allows you to select a phone line for which you want to display the recent call logs. You can select line numbers ranges from 1 to 10. |
| Display Recents From | Allows you to set which type of recent call logs the phone will display. Choose Server to display BroadSoft XSI recent call logs and select Phone to display local recent call logs. Note The Display recents from is added to the Recents screen of the phone only when you set CallLog Enable to Yes and Display Recents From type to Server . | Note | The Display recents from is added to the Recents screen of the phone only when you set CallLog Enable to Yes and Display Recents From type to Server . |
| Note | The Display recents from is added to the Recents screen of the phone only when you set CallLog Enable to Yes and Display Recents From type to Server . |

| Note | XSI Host Server uses http protocol by default. To enable XSI over HTTPS, you can specify https:// in the server. |
|---|---|

| Note | The Display recents from is added to the Recents screen of the phone only when you set CallLog Enable to Yes and Display Recents From type to Server . |
|---|---|

| Parameter | Description |
|---|---|
| XMPP Enable | Set to Yes to enable the BroadSoft XMPP directory for the phone user. Default: No |
| Server | Enter the name of the XMPP server; for example, xsi.iop1.broadworks.net. Default: Blank |
| Port | Server port for the directory. Default: Blank |
| User ID | BroadSoft User ID of the phone user; for example, johndoe@xdp.broadsoft.com. Default: Blank |
| Password | Alphanumeric password associated with the User ID. Default: Blank |
| Login Invisible | When enabled, the user's presence information is not published when the user signs in. Default: No |
| Retry Intvl | Interval, in seconds, to allow a reconnect without a log in after the client disconnects from the server. After this interval,
                                                the client needs to reauthenticate. Default: 30 |

| Parameter | Description |
|---|---|
| XML Directory Service Name | Name of the XML Directory. Displays on the user’s phone as a directory choice Default: Blank |
| XML Directory Service URL | URL where the XML Directory is located. Default: Blank |
| XML Application Service Name | Name of the XML application. Displays on the user’s phone as a web application choice. |
| XML Application Service URL | URL where the XML application is located. |
| XML User Name | XML service username for authentication purposes Default: Blank |
| XML Password | XML service password for authentication purposes Default: Blank |
| CISCO XML EXE Enable | Enables or disables Cisco XML EXE authentication. Default: No |
| CISCO XML EXE Auth Mode | Specifies the authentication mode for Cisco XML EXE. The available options are: Trusted—No authentication is performed (local user password is set or not). Local Credential—Authentication is based on digest authentication using the local user password, if the local user password
                                                      is set. If not set, then no authentication is performed. Remote Credential—Authentication is based on digest authentication using the remote username/password as set in the XML application
                                                      on the web page (to access an XML application server). Default: Trusted |

| Feature | Description |
|---|---|
| Group Paging Script | Enter a string to configure group paging and priority paging (out of band paging) that doesn’t require the phone registration. |

| Parameter | Description |
|---|---|
| LDAP Dir Enable | Choose Yes to enable LDAP. Default: No |
| Corp Dir Name | Enter a free-form text name, such as “Corporate Directory.” Default: Blank |
| Server | Enter a fully qualified domain name or IP address of an LDAP server in the following format: nnn.nnn.nnn.nnn Enter the host name of the LDAP server if the MD5 authentication method is used. Default: Blank |
| Search Base | Specify a starting point in the directory tree from which to search. Separate domain components [dc] with a comma. For example: dc=cv2bu,dc=com Default: Blank |
| Client DN | Enter the distinguished name domain components [dc]; for example: dc=cv2bu,dc=com If you are using the default Active Directory schema (Name(cn)->Users->Domain), an example of the client DN follows: cn=”David Lee”,dc=users,dc=cv2bu,dc=com cn=”David Lee”,dc=cv2bu,dc=com username@domain is the client DN format for a Windows server For example, DavidLee@cv2bu.com Default: Blank |
| User Name | Enter the username for a credentialed user on the LDAP server. Default: Blank |
| Password | Enter the password for the LDAP username. Default: Blank |
| Auth Method | Select the authentication method that the LDAP server requires. Choices are: None—No authentication is used between the client and the server. Simple—The client sends its fully-qualified domain name and password to the LDAP server. Might present security issues. Digest-MD5—The LDAP server sends authentication options and a token to the client. The client returns an encrypted response
                                                that is decrypted and verified by the server. Default: None |
| Last Name Filter | Use this field to specify how the phone must perform searches based on the last name or surname (sn), when users search for
                                                contacts. Examples: sn:(sn=$VALUE*) instructs the phone to find all last names that begin with the entered search string. sn:(sn=*$VALUE*) instructs the phone to find all last names in which the entered search string appears anywhere in the last name. This method
                                                is more inclusive and retrieves more search results. This method is consistent with the search method in other directories
                                                such as the Broadsoft directories and the user's personal address book on the phone. Default: Blank |
| First Name Filter | Use this field to specify how the phone must perform searches based on the first name or common name (cn), when users search
                                                for contacts. Examples: cn:(cn=$VALUE*) instructs the phone to find all first names that begin with the entered search string. cn:(cn=*$VALUE*) instructs the phone to find all first names in which the entered search string appears anywhere in the first name. This method
                                                is more inclusive and retrieves more search results. This method is consistent with the search method in other directories
                                                such as the Broadsoft directories and the user's personal address book on the phone. Default: Blank |
| Search Item 3 | Additional customized search item. Can be blank if not needed. Default: Blank |
| Search Item 3 Filter | Customized filter for the searched item. Can be blank if not needed. Default: Blank |
| Search Item 4 | Additional customized search item. Can be blank if not needed. Default: Blank |
| Search Item 4 Filter | Customized filter for the searched item. Can be blank if not needed. Default: Blank |
| Display Attrs | Format of LDAP results displayed on phone, where: a—Attribute name cn—Common name sn—Surname (last name) telephoneNumber—Phone number n—Display name For example, n=Phone causes “Phone:” to be displayed in front of the phone number of an LDAP query result when the detail
                                                soft button is pressed. t—type When t=p, that is, t is of type phone number, the retrieved number can be dialed. Only one number can be made dialable. If
                                                two numbers are defined as dialable, only the first number is used. For example, a=ipPhone, t=p; a=mobile, t=p; This example results in only the IP Phone number being dialable and the mobile number is ignored. p—phone number When p is assigned to a type attribute, example t=p, the retrieved number is dialable by the phone. For example, a=givenName,n=firstname;a=sn,n=lastname;a=cn,n=cn;a=telephoneNumber,n=tele,t=p Default: Blank |
| Number Mapping | Can be blank if not needed. Note With the LDAP number mapping, you can manipulate the number that was retrieved from the LDAP server. For example, you can
                                                            append 9 to the number if your dial plan requires a user to enter 9 before dialing. Add the 9 prefix by adding (<:9xx.>) to
                                                            the LDAP Number Mapping field. For example, 555 1212 would become 9555 1212. If you do not manipulate the number in this fashion, a user can use the Edit Dial feature to edit the number before dialing
                                                out. Default: Blank | Note | With the LDAP number mapping, you can manipulate the number that was retrieved from the LDAP server. For example, you can
                                                            append 9 to the number if your dial plan requires a user to enter 9 before dialing. Add the 9 prefix by adding (<:9xx.>) to
                                                            the LDAP Number Mapping field. For example, 555 1212 would become 9555 1212. |
| Note | With the LDAP number mapping, you can manipulate the number that was retrieved from the LDAP server. For example, you can
                                                            append 9 to the number if your dial plan requires a user to enter 9 before dialing. Add the 9 prefix by adding (<:9xx.>) to
                                                            the LDAP Number Mapping field. For example, 555 1212 would become 9555 1212. |

| Note | With the LDAP number mapping, you can manipulate the number that was retrieved from the LDAP server. For example, you can
                                                            append 9 to the number if your dial plan requires a user to enter 9 before dialing. Add the 9 prefix by adding (<:9xx.>) to
                                                            the LDAP Number Mapping field. For example, 555 1212 would become 9555 1212. |
|---|---|

| Parameter | Description |
|---|---|
| Programmable Softkey Enable | Enables programmable softkeys. |
| Idle Key List | Softkeys that display when the phone is idle. |
| Missed Call Key List | Softkeys that display when there is a missed call. |
| Off Hook Key List | Softkeys that display when the phone is off-hook. |
| Dialing Input Key List | Softkeys that display when the user must enter dialing data. |
| Progressing Key List | Softkeys that display when a call is attempting to connect. |
| Connected Key List | Softkeys that display when a call is connected. |
| Start-Xfer Key List | Softkeys that display when a call transfer has been initiated. |
| Start-Conf Key List | Softkeys that display when a conference call has been initiated. |
| Conferencing Key List | Softkeys that display when a conference call is in progress. |
| Releasing Key List | Softkeys that display when a call is released. |
| Hold Key List | Softkeys that display when one or more calls are on hold. |
| Ringing Key List | Softkeys that display when a call is incoming. To silence an incoming call, you can add Ignore softkey. |
| Shared Active Key List | Softkeys that display when a call is active on a shared line. |
| Shared Held Key List | Softkeys that display when a call is on hold on a shared line. |
| PSK 1 through PSK 16 | Programmable softkey fields. Enter a string in these fields to configure softkeys that display on the phone screen. You can
                                                create softkeys for speed dials to numbers or extensions, vertical service activation codes (* codes), or XML scripts. |

| Parameter | Description |
|---|---|
| Line Enable | To enable this line for service, select yes. Otherwise, select No. Default: Yes Example XML configuration: To disable service on the line associated with extension 2: <Line_Enable_2_ ua="na">No</Line_Enable_2_> |

| Parameter | Description |
|---|---|
| H264 BP0 Enable | Enables the H264 Base Profile 0 codec when you select Yes and disables it when you select No . Default: Yes |
| H264 HP Enable | Enables the H264 High Profile codec when you select Yes and disables it when you select No . Default: Yes |
| Encryption Method | Selects the encryption method to be used during a secured call. Options are AES 128 and AES 256 GCM . Default: AES 128 |

| Parameter | Description |
|---|---|
| Share Ext | Indicates whether
                                             this extension is to be shared with other Cisco IP phones or
                                             private. Default: Yes |
| Shared User ID | The user identified
                                             assigned to the shared line appearance. Default: Blank |
| Subscription Expires | Number of seconds
                                             before the SIP subscription expires. Before the subscription
                                             expiration, the phone gets NOTIFY messages from the SIP server on
                                             the status of the shared phone extension. Default: 3600 |
| Restrict MWI | When enabled, the
                                             message waiting indicator lights only for messages on private
                                             lines. Default: No |

| Parameter | Description |
|---|---|
| NAT Mapping Enable | To use externally mapped IP addresses and SIP/ RTP ports in SIP messages, select yes. Otherwise, select no. Default: No |
| NAT Keep Alive Enable | To send the configured NAT keep alive message periodically, select yes. Otherwise, select no. Default: No |
| NAT Keep Alive Msg | Enter the keep alive message that should be sent periodically to maintain the current NAT mapping. If the value is $NOTIFY,
                                             a NOTIFY message is sent. If the value is $REGISTER, a REGISTER message without contact is sent. Default: $NOTIFY |
| NAT Keep Alive Dest | Destination that should receive NAT keep alive messages. If the value is $PROXY, the messages are sent to the current or outbound
                                             proxy. |

| Parameter | Description |
|---|---|
| SIP TOS/DiffServ Value | Time of service (ToS)/differentiated services (DiffServ) field value in UDP IP packets carrying a SIP message. Default: 0x68. |
| RTP ToS/DiffServ Value | Value for the ToS field of voice data packets. Sets the priority for voice packets in data traffic. Default: 0xb8. |

| Parameter | Description |
|---|---|
| SIP Transport | Select the transport protocol for SIP messages: UDP TCP TLS AUTO AUTO allows the phone to select the appropriate protocol automatically, based on the NAPTR records on the DNS server. See Configure the SIP Transport for more details. Default: UDP |
| SIP Port | The phone's port number for SIP message listening and transmission. Specify the port number here only when you are using UDP as the SIP transport protocol. If you are using TCP, the system uses a random port within the range specified in SIP TCP Port Min and SIP TCP Port Max on the Voice > SIP tab. If you need to specify a port of SIP proxy server, you can specify it using the Proxy field ( Proxy and Registration ) or the XSI Host Server field ( XSI Line Service ). Default: 5060 |
| SIP 100REL Enable | Support of 100REL SIP extension for reliable transmission of provisional responses (18x) and use of PRACK requests. Select Yes to enable. Default: No |
| EXT SIP Port | The external SIP port number. |
| Auth Resync-Reboot | The Cisco IP Phone authenticates the sender when it receives a NOTIFY message with the following requests: resync reboot report restart XML-service Select Yes to enable. Default: Yes |
| SIP Proxy-Require | The SIP proxy can support a specific extension or behavior when it sees this header from the user agent. If this field is
                                             configured and the proxy does not support it, it responds with the message, unsupported. Enter the appropriate header in the
                                             field provided. |
| SIP Remote-Party-ID | The Remote-Party-ID header to use instead of the From header. Select Yes to enable. Default: Yes |
| Referor Bye Delay | Controls when the phone sends BYE to terminate stale call legs upon completion of call transfers. Multiple delay settings
                                             (Referor, Refer Target, Referee, and Refer-To Target) are configured on this screen. For the Referror Bye Delay, enter the
                                             appropriate period of time in seconds. Default: 4 |
| Refer-To Target Contact | Indicates the refer-to target. Select Yes to send the SIP Refer to the contact. Default: No |
| Referee Bye Delay | For the Referee Bye Delay, enter the appropriate period of time in seconds. Default: 0 |
| Refer Target Bye Delay | For the Refer Target Bye Delay, enter the appropriate period of time in seconds. Default: 0 |
| Sticky 183 | When enabled, the IP telephony ignores further 180 SIP responses after receiving the first 183 SIP response for an outbound
                                             INVITE. To enable this feature, select Yes . Otherwise, select No . Default: No |
| Auth INVITE | When enabled, authorization is required for initial incoming INVITE requests from the SIP proxy. To enable this feature, select Yes . Default: No |
| Ntfy Refer On 1xx-To-Inv | If set to Yes , as a transferee, the phone will send a NOTIFY with Event:Refer to the transferor for any 1xx response returned by the transfer
                                             target, on the transfer call leg. If set to No , the phone will only send a NOTIFY for final responses (200 and higher). |
| Set G729 annexb | Configure G.729 Annex B settings. |
| User Equal Phone | When a tel URL is converted to a SIP URL and the phone number is represented by the user portion of the URL, the SIP URL includes
                                             the optional : user=phone parameter (RFC3261). For example: To: sip:+12325551234@example.com; user=phone To enable this optional parameter, select Yes . Default: No |
| Call Recording Protocol | Determines the type of recording protocol that the phone uses. Options are: SIPINFO SIPREC Default: SIPREC |
| Privacy Header | Sets user privacy in the SIP message in the trusted network. The privacy header options are: Disabled (default) none—The user requests that a privacy service applies no privacy functions to this SIP message. header—The user needs a privacy service to obscure headers which cannot be purged of identifying information. session—The user requests that a privacy service provide anonymity for the sessions. user—The user requests a privacy level only by intermediaries. id—The user requests that the system substitute an id that doesn't reveal the IP address or host name. Default: Disabled |
| P-Early-Media Support | Controls whether the P-Early-Media header is included in the SIP message for an outgoing call. To include the P-Early-Media header, select Yes . Otherwise, select No . Default: No |

| Parameter | Description |
|---|---|
| Blind Attn-Xfer Enable | Enables the phone to perform an attended transfer operation by ending the current call leg and performing a blind transfer
                                             of the other call leg. If this feature is disabled, the phone performs an attended transfer operation by referring the other
                                             call leg to the current call leg while maintaining both call legs. To use this feature, select Yes. Otherwise, select No. Default: No |
| Message Waiting | Indicates whether the Message Waiting Indicator on the phone is lit. This parameter toggles a message from the SIP proxy to
                                             indicate if a message is waiting. |
| Auth Page | Specifies whether to authenticate the invite before auto answering a page. Default: No |
| Default Ring | Type of ring heard. Choose from No Ring or 1 through 10. Ring options are Sunlight, Chirp 1, Chirp 2, Delight, Evolve, Mellow, Mischief, Reflections, Ringer, Ascent, Are you there,
                                             and Chime. |
| Auth Page Realm | Identifies the Realm part of the Auth that is accepted when the Auth Page parameter is set to Yes. This parameter accepts
                                             alphanumeric characters. |
| Conference Bridge URL | URL used to join a conference call, generally in the form of the word conference or user@IPaddress:port. |
| Auth Page Password | Identifies the password used when the Auth Page parameter is set to Yes. This parameter accepts alphanumeric characters. |
| Mailbox ID | Identifies the voice mailbox number/ID for the phone. |
| Voice Mail Server | Identifies the SpecVM server for the phone, generally the IP address, and port number of the VM server. |
| Voice Mail Subscribe Interval | The expiration time, in seconds, of a subscription to a voice mail server. |
| Auto Ans Page On Active Call | Determines the behavior of the phone when a page call arrives. |
| Feature Key Sync | Enable the synchronization of settings between the line and the server if necessary. Feature Key Sync must be enabled for lines that are configured for the following functions or users: Call forward all DND |
| Call Park Monitor Enable | BroadSoft server-only feature. If call park is enabled on the server or on any of the programmable line keys, you need to
                                             enable this field for call park notification to work. Default: No |
| Enable Broadsoft Hoteling | When this parameter is set to yes, the phone sends out subscription messages (without body) to the server. Default: No |
| Hoteling Subscription Expires | An expiration value that is added in the subscription message. Default value is 3600. |
| Secure Call Option | The secure call feature works only when the SIP Transport on the Ext (n) tab is set to TLS . Enables secured calls on an extension. Options are: Optional: The phone maintains the current behavior for secure calls. Required: The phone rejects nonsecure calls from other phones. Default: Optional |

| Parameter | Description |
|---|---|
| Broadsoft ACD | Enables the phone for Automatic Call Distribuion (ACD). Select Yes to enable or No to disable. Default: No |
| Call Information Enable | Enables the phone to display details of a call center call. Select Yes to enable or No to disable. Default: No |
| Disposition Code Enable | Enables the user to add a disposition code. Select Yes to enable or No to disable. Default: No |
| Trace Enable | Enables the user to trace the last incoming call. Select Yes to enable or No to disable. Default: No |
| Emergency Escalation Enable | Enables the user to escalate a call to a supervisor in case of emergency. Select Yes to enable or No to disable. Default: No |
| Queue Status Notification Enable | Displays the call center status and the agent status. Select Yes to enable or No to disable. Default: No |

| Parameter | Description |
|---|---|
| Proxy | SIP proxy server and port number set by the service provider for all outbound requests. For example: 192.168.2.100:6060. The port number is optional. If you don't specify a port, the default port 5060 is used for UDP, and the default port 5061
                                             is used for TLS. When you need to refer to this proxy in another setting, for example, the speed dial line key configuration, use the $PROXY macro variable. |
| Outbound Proxy | All outbound requests are sent as the first hop. Enter an IP address or domain name. |
| Alternate Proxy Alternate Outbound Proxy | This feature provides fast fall back when there is network partition at the Internet or when the primary proxy (or primary
                                             outbound proxy) is not responsive or available. The feature works well in a Verizon deployment environment as the alternate
                                             proxy is the Integrated Service Router (ISR) with analog outbound phone connection. Enter the proxy server addresses and port numbers in these fields. After the phone is registered to the primary proxy and
                                             the alternate proxy (or primary outbound proxy and alternate outbound proxy), the phone always sends out INVITE and Non-INVITE
                                             SIP messages (except registration) via the primary proxy. The phone always registers to both the primary and alternate proxies.
                                             If there is no response from the primary proxy after timeout (per the SIP RFC spec) for a new INVITE, the phone attempts to
                                             connect with the alternate proxy. The phone always tries the primary proxy first, and immediately tries the alternate proxy
                                             if the primary is unreachable. Active transactions (calls) never fall back between the primary and alternate proxies. If there is fall back for a new INVITE,
                                             the subscribe/notify transaction will fall back accordingly so that the phone's state can be maintained properly. You must
                                             also set Dual Registration in the Proxy and Registration section to Yes. |
| Use OB Proxy In Dialog | Determines whether to force SIP requests to be sent to the outbound proxy within a dialog. Ignored if the Use Outbound Proxy field is set to No or if the Outbound Proxy field is empty. Default: Yes |
| Register | Enables periodic registration with the proxy. This parameter is ignored if a proxy is not specified. To enable this feature,
                                             select Yes . Default: Yes |
| Make Call Without Reg | Enables making outbound calls without successful (dynamic) registration by the phone. If set to No, the dial tone plays only
                                             when registration is successful. To enable this feature, select Yes . Default: No |
| Register Expires | Defines how often the phone renews registration with the proxy. If the proxy responds to a REGISTER with a lower expires value,
                                             the phone renews registration based on that lower value instead of the configured value. If registration fails with an “Expires too brief” error response, the phone retries with the value specified in the Min-Expires
                                             header of the error. The range is from 32 to 2000000. Default: 3600 seconds |
| Ans Call Without Reg | If enabled, the user does not have to be registered with the proxy to answer calls. Default: No |
| Use DNS SRV | Enables DNS SRV lookup for the proxy and outbound proxy. To enable this feature, select Yes . Otherwise, select No . Default: No |
| DNS SRV Auto Prefix | Enables the phone to automatically prepend the proxy or outbound proxy name with _sip._udp when performing a DNS SRV lookup
                                             on that name. Default: No |
| Proxy Fallback Intvl | Sets the delay after which the phone retries from the highest priority proxy (or outbound proxy) after it has failed over
                                             to a lower priority server. The phone should have the primary and backup proxy server list from a DNS SRV record lookup on the server name. It needs to
                                             know the proxy priority; otherwise, it does not retry. The range is from 0 to 65535. Default: 3600 seconds |
| Proxy Redundancy Method | Select Normal or Based on SRV Port . The phone creates an internal list of proxies returned in the DNS SRV records. If you select Normal, the list contains proxies ranked by weight and priority. If you select Based on SRV Port, the phone uses normal, then inspects the port number based on the first-listed proxy port. Default: Normal |
| Dual Registration | Set to Yes to enable the Dual registration/Fast Fall back feature. To enable the feature you must also configure the alternate proxy/alternate
                                             outbound proxy fields in the Proxy and Registration section. |
| Auto Register When Failover | If set to No, the fallback happens immediately and automatically. If the Proxy Fallback Intvl is exceeded, all the new SIP
                                             messages go to the primary proxy. If set to Yes, the fallback happens only when current registration expires, which means only a REGISTER message can trigger
                                             fallback. For example, when the value for Register Expires is 3600 seconds and Proxy Fallback Intvl is 600 seconds, the fallback is
                                             triggered 3600 seconds later and not 600 seconds later. When the value for Register Expires is 600 seconds and Proxy Fallback
                                             Intvl is 1000 seconds, the fallback is triggered at 1200 seconds. After successfully registering back to primary server, all
                                             the SIP messages go to primary server. |

| Parameter | Description |
|---|---|
| Display Name | Name displayed as the caller ID. |
| User ID | Extension number for this line. When you need to refer to this user ID in another setting, for example, the short name for a line key, use the $USER macro variable. |
| Password | Password for this line. Default: Blank (no password required) |
| Auth ID | Authentication ID for SIP authentication. Default: Blank |
| SIP URI | The parameter by which the user agent will identify itself for
                                             this line. If this field is blank, the actual URI used in the SIP
                                             signaling should be automatically formed as: sip:UserName@Domain where UserName is the username given for this line in the User ID, and Domain is the domain given for this profile in the
                                             User Agent Domain. If the User Agent Domain is an empty string, then the IP address of the phone should be used for the domain. If the URI field is not empty, but if a SIP or SIPS URI contains no @ character, the actual URI used in the SIP signaling
                                             should be automatically formed by appending this parameter with an @ character followed by the IP address of the device. |

| Parameter | Description |
|---|---|
| XSI Host Server | Enter the name of the server; for example, . xsi.iop1.broadworks.net Note XSI Host Server uses http protocol by default. To enable XSI over HTTPS, you can specify https:// in the server. For example: https://xsi.iop1.broadworks.net You can also specify a port for the server. For example: https://xsi.iop1.broadworks.net:5061 If you don't specify a port. The default port for the specified protocol is used. Default: Blank | Note | XSI Host Server uses http protocol by default. To enable XSI over HTTPS, you can specify https:// in the server. |
| Note | XSI Host Server uses http protocol by default. To enable XSI over HTTPS, you can specify https:// in the server. |
| XSI Authentication Type | Determines the XSI authentication type. Select Login Credentials to authenticate access with Login User ID and Login Password. Select SIP Credentials to authenticate access with the register Auth ID and Password of the SIP account registered on the phone. Default: Login Credentials |
| Login User ID | BroadSoft User ID of the phone user; for example, johndoe@xdp.broadsoft.com. For any XSI Authentication Type, you must enter Login User ID . Without Login User ID , the BroadWorks Anywhere feature does not work. Default: Blank |
| Login Password | Alphanumeric password associated with the Login User ID. Enter Login Password, when you select Login Credentials for XSI authentication type. Default: Blank |
| Anywhere Enable | Enables BroadWorks Anywhere feature on an extension. If you choose Yes , Anywhere is enabled on this line, and the user can use the phone menu to add multiple locations to this specific line. Default: Yes |
| Block CID Enable | Enables XSI Caller ID blocking on a line. Choose Yes to enable the synchronization of blocking caller id status with the server using XSI interface. Choose No to use the phone's local blocking caller id settings. |
| CFWD Enable | Enables or disables call forwarding status sync on a line via XSI service. Choose Yes to enable the phone to synchronize the call forwarding status with the server using the XSI service. Choose No to disable this feature. Note When Feature Key Sync is set to Yes , FKS takes precedent over XSI synchronization. If XSI host server and credentials are not entered and the CFWD Enable field is set to Yes , the phone user can't forward calls on the phone. | Note | When Feature Key Sync is set to Yes , FKS takes precedent over XSI synchronization. If XSI host server and credentials are not entered and the CFWD Enable field is set to Yes , the phone user can't forward calls on the phone. |
| Note | When Feature Key Sync is set to Yes , FKS takes precedent over XSI synchronization. If XSI host server and credentials are not entered and the CFWD Enable field is set to Yes , the phone user can't forward calls on the phone. |
| DND Enable | Enables or disables DND status sync on a line via XSI service. Choose Yes to enable the phone to synchronize DND status with the server using the XSI service. Choose No to disable this feature. Note When Feature Key Sync is set to Yes , FKS takes precedent over XSI synchronization. If XSI host server and credentials are not entered and the DND Enable field is set to Yes , the phone user can't turn on DND mode on the phone. | Note | When Feature Key Sync is set to Yes , FKS takes precedent over XSI synchronization. If XSI host server and credentials are not entered and the DND Enable field is set to Yes , the phone user can't turn on DND mode on the phone. |
| Note | When Feature Key Sync is set to Yes , FKS takes precedent over XSI synchronization. If XSI host server and credentials are not entered and the DND Enable field is set to Yes , the phone user can't turn on DND mode on the phone. |

| Note | XSI Host Server uses http protocol by default. To enable XSI over HTTPS, you can specify https:// in the server. |
|---|---|

| Note | When Feature Key Sync is set to Yes , FKS takes precedent over XSI synchronization. If XSI host server and credentials are not entered and the CFWD Enable field is set to Yes , the phone user can't forward calls on the phone. |
|---|---|

| Note | When Feature Key Sync is set to Yes , FKS takes precedent over XSI synchronization. If XSI host server and credentials are not entered and the DND Enable field is set to Yes , the phone user can't turn on DND mode on the phone. |
|---|---|

| Parameter | Description |
|---|---|
| Preferred Codec | Preferred codec for all calls. The actual codec used in a call still depends on the outcome of the codec negotiation protocol. Select one of the following: G711u G711a G729a G729ab G722 G722.2 iLBC OPUS iSAC Default: G711u |
| Use Pref Codec Only | Select No to use any code. Select Yes to use only the preferred codes. When you select Yes, calls fail if the far end does not support the preferred codecs. Default: No |
| Second Preferred Codec | Codec to use if the first codec fails. Default: Unspecified |
| Third Preferred Codec | Codec to use if the second codec fails. Default: Unspecified |
| G711u Enable | Enables use of the G.711u codec. Default: Yes |
| G711a Enable | Enables use of the G.711a codec. Default: Yes |
| G729a Enable | To enable use of the G.729a codec at 8 kbps, select Yes . Otherwise, select No . Default: Yes |
| G722 Enable | Enables use of the G.722 codec. Default: Yes |
| G722.2 Enable | Enables use of the G.722.2 codec. Default: No |
| iLBC Enable | Enables use of the iLBC codec. Default: Yes |
| OPUS Enable | Enables the use of OPUS codec. Default: Yes |
| Silence Supp Enable | To enable silence suppression so that silent audio frames are
                                             					 not transmitted, select Yes . Otherwise, select No . Default: No |
| DTMF Tx Method | The method for transmitting DTMF signals to the far end. The
                                             					 options are: AVT—Audio video transport. Sends DTMF as AVT events. InBand—Sends DTMF by using the audio path. Auto—Uses InBand or AVT based on the outcome of codec
                                                   						  negotiation. INFO—Uses the SIP INFO method. |
| Codec Negotiation | When set to Default, the Cisco IP phone responds to an Invite with a 200 OK response advertising the preferred codec only.
                                             When set to List All, the Cisco IP phone responds listing all the codecs that the phone supports. The default value is Default,
                                             or to respond with the preferred codec only. |
| Encryption Method | Encryption method to be used during secured call. Options are AES 128 and AES 256 GCM Default: 128. |

| Parameter | Description |
|---|---|
| Dial Plan | Dial plan script for the selected extension. The dial plan syntax allows the designation of three parameters for use with a specific gateway: uid – The authentication user-id pwd – The authentication password nat – If this parameter is present, use NAT mapping. Separate each parameter with a semi-colon (;). |
| Caller ID Map | Inbound caller ID numbers can be mapped to a different string. For example, a number that begins with +44xxxxxx can be mapped
                                                to 0xxxxxx. This feature has the same syntax as the Dial Plan parameter. With this parameter, you can specify how to map a
                                                caller ID number for display on screen and recorded into call logs. |
| Enable URI Dialing | Enables or disables URI dialing. |
| Emergency Number | Enter a comma-separated list of emergency numbers. When one of these numbers is dialed, the unit disables processing of CONF,
                                                HOLD, and other similar softkeys or buttons to avoid accidentally putting the current call on hold. The phone also disables
                                                hook flash event handling. Only the far end can terminate an emergency call. The phone is restored to normalcy after the call is terminated and the receiver
                                                is back on-hook. Maximum number length is 63 characters. Defaults to blank (no emergency number). |

| Parameter | Description |
|---|---|
| Company UUID | The Universally Unique Identifier (UUID) assigned to the customer by the emergency call services provider. Maximum identifier length is 128 characters. Defaults to blank. |
| Primary Request URL | Encrypted HTTPS phone location request. The request uses the phone IP addresses, MAC address, Network Access Identifier (NAI),
                                                and chassis ID and port ID assigned by the network switch manufacturer. The request also includes the location server name
                                                and the customer identifier. The server used by the emergency call services provider responds with an Emergency Response Location (ERL) that has a location
                                                Uniform Resource Identifier (URI) tied to the user phone IP address. Defaults to blank. |
| Secondary Request URL | Encrypted HTTPS request sent to the emergency call services provider's backup server to obtain the user's phone location. Defaults to blank. |

| Parameter | Description |
|---|---|
| Hold Reminder Timer | Specifies the time delay (in seconds), that a ring splash is heard on an active call when another call was placed on hold. Default: 0 |
| Hold Reminder Ringtone | Specifies the volume of the timer ringtone. |

| Parameter | Description |
|---|---|
| Cfwd Setting | Select Yes to enable call forwarding. |
| Cfwd All Dest | Enter the extensions to which the call is forwarded. |
| Cfwd Busy Dest | Enter the extensions to forward calls to when the line is busy. Default: voicemail |
| Cfwd No Ans Dest | Enter the extension to forward calls to when the call is not answered. Default: voicemail |
| Cfwd No Ans Delay | Enter the delay in time (in seconds) to wait before forwarding a call that is unanswered. Default: 20 seconds |

| Parameter | Description |
|---|---|
| Speed Dial Name (2 to 9) | Name assigned to a specific speed dial number. Default: Blank |
| Speed Dial Number 2 to 9) | Target phone number (or URL) assigned to speed dial 2, 3, 4, 5, 6, 7, 8, or 9. Press the digit key (2-9) to dial out the assigned
                                                number. Default: Blank |

| Parameter | Description |
|---|---|
| CW Setting | Enables or disables the Call Waiting service. Default: Yes |
| Block CID Setting | Enables or disables the Block CID service. Default: No |
| Block ANC Setting | Enables or disables the Block ANC service. Default: No |
| DND Setting | Enables or disables the DND settings options for a user. |
| Handset LED Alert | Enables or disables LED alert on the handset. Options are: Voicemail and Voicemail, Missed Call. Default: Voicemail |
| Secure Call Setting | Enables or disables Secure Call. Default: No |
| Auto Answer Page | Enables or disables automatic answering of paged calls. Default: Yes |
| Preferred Audio Device | Choose the type of audio that the phone will use. Options are: Speaker and Headset. Choose the type of audio that the phone will use. Options are: Speaker and Headset. Default: None |
| Time Format | Choose the time format for the phone (12 or 24 hour). Default: 12hr |
| Date Format | Choose the date format for the phone (month/day or day/month). Default: month/day |
| Miss Call Shortcut | Enables or disables the option for creating a missed call shortcut. |
| Alert Tone Off | Enables or disables the alert tone. |
| Log Missed Calls for EXT (n) | Enables or disables the missed calls logs for a specific extension. |
| Shared Line DND Cfwd Enable | Enable/disable the Shared Line DND Call Forward. |

| Parameter | Description |
|---|---|
| Ringer Volume | Sets the default volume for the ringer. Default: 9 |
| Speaker Volume | Sets the default volume for the speakerphone. Default: 8 |
| Handset Volume | Sets the default volume for the handset. Default: 10 |
| Headset Volume | Sets the default volume for the headset. Default: 10 |
| Electronic Hookswitch Control | Enables or disables the Electronic HookSwitch (EHS) feature. After EHS is enabled, the AUX port does not output phone logs. |

| Parameter | Description |
|---|---|
| Compliant Standard | Specifies the compliance standard for the phone audio. The available options are: ETSI : A set of standards for speech and multimedia transmission for the narrowband and wideband terminals from European Telecommunications
                                                      Standards Institute (ETSI). TIA : A set of standards from US Telecommunications Industry Association (TIA). The standards are for narrowband and wideband
                                                      audio transmission via wired telephones. Default: TIA |

| Parameter | Description |
|---|---|
| Screen Saver Enable | Enables a screen saver on the phone. When the phone is idle for
                                             					 a specified time, it enters screen saver mode. Default: No |
| Screen Saver Type | Types of screen saver. Options you can choose: Clock : Displays a digital clock on a plain background. Download Picture : Displays a picture pushed from the phone webpage. Lock : Enables locking of the screensaver. |
| Screen Saver Wait | Amount of idle time before screen saver displays. enter the number of seconds of idle time to elapse before the screen saver starts. Default: 300 |
| Screen Saver Refresh Period | Number of seconds before the screen saver should refresh (if, for example, you chose a rotation of pictures). |
| Back Light Timer | Number of seconds for which the back light timer will be on. |
| LCD Contrast | Value for desired contrast. |
| Logo Type | Type of logo displayed on the phone screen. Options you can choose: Default Download Picutre Text Logo |
| Text Logo | Text logo to display when the phone boots up. A service
                                             					 provider, for example, can enter logo text as follows: Up to 2 lines of text Each line must be fewer than 32 characters Insert a new line character (\n) between lines Insert escape code %0a For example, Super\n%0aTelecom displays: Super Telecom Use the + character to add spaces for formatting. For example,
                                             					 you can add multiple + characters before and after the text to center it. |
| Picture Download URL | URL locating the (.png) file to display on the phone screen background. For more information, see the Phone Information and Display Settings . |

| Note | The attendant console tab, labeled Att Console , is only available in Admin Login > advanced mode. |
|---|---|

| Parameter | Description |
|---|---|
| Subscribe Expires | Specifies how long the subscription remains valid. After the specified period of time elapses, the Cisco Attendant Console
                                                initiates a new subscription. Default: 1800 |
| Subscribe Retry Interval | Specifies the length of time to wait to try again if the subscription fails. Default: 30 |
| Subscribe Delay | Length of delay before attempting to subscribe. Default: 1 |
| Server Type | Specifies the server type with which the phone is connected. Options available: BroadSoft SPA9000 Asterisk RFC3265_4235 Sylantro |
| BLF List URI | The Uniform Resource Identifier (URI) of the Busy Lamp Field (BLF) list that you have set up for a user of the phone, on the
                                                BroadSoft server. This field is only applicable if the phone is registered to a BroadSoft server. The BLF list is the list of users whose lines
                                                the phone is allowed to monitor. See Phone Configuration for Monitoring Other Phones for details. The BLF List URI must be specified in the format <URI name>@<server> . The BLF List URI specified must be the same as the value configured for the List URI: sip parameter on the BroadSoft server. Default: Blank Example XML configuration: <BLF_List_URI ua="na">MonitoredUsersList@sipurash22.com</BLF_List_URI> |
| Use Line Keys For BLF List | Controls whether the phone uses its line keys to monitor the BLF list, when monitoring of the BLF list is active. This setting only has significance when BLF List is set to Show . Default: No Example XML configuration: <Use_Line_Keys_For_BLF_List ua="na">Yes</Use_Line_Keys_For_BLF_List> |
| Customizable PLK Options | Features that users are allowed to configure on line keys. To allow a feature, add the corresponding option as shown below. Separate options with the semi-colon (;). Speed dial: sd Busy Lamp Field (BLF) key to monitor a user: blf Call pickup from a monitored line: cp Note This option is only effective when the blf option is added. Default: sd; Note Adding the sd option automatically allows users to configure speed dial to a monitored line (speed dial with BLF) when the blf option is added. Example, to allow all features: sd;blf;cp Example XML configuration: <Customizable_PLK_options ua="na">sd;</Customizable_PLK_options> | Note | This option is only effective when the blf option is added. | Note | Adding the sd option automatically allows users to configure speed dial to a monitored line (speed dial with BLF) when the blf option is added. |
| Note | This option is only effective when the blf option is added. |
| Note | Adding the sd option automatically allows users to configure speed dial to a monitored line (speed dial with BLF) when the blf option is added. |
| BLF List | Activates or deactivates monitoring of the BLF list. When set to Show , the phone assigns available line keys in sequence, to monitor the BLF list entries. The labels of the BLF list keys show
                                                the names of the monitored users and the status of the monitored lines. This setting only has significance when BLF List URI is configured. Example XML configuration: <BLF_List ua="rw">Show</BLF_List> |
| BXfer to Starcode Enable | When set to Yes , the phone performs a blind transfer when the *code is defined in a speed dial extended function,. If set to No , the current call is held and a new call is started to the speed dial destination. Default: No |
| BXfer On Speed Dial Enable | When set to Yes , the phone performs a blind transfer when the speed dial function key is selected. When set to no, the current connected
                                                call is held and a new call to the speed dial destination is started. For example, when a user parks a call using the speed dial function, if the parameter is enabled, a blind transfer is performed
                                                to the parking lot. If the parameter is not enabled, an attended transfer is performed to the parking lot. Default: No |
| BXfer To Remote Party Number Enable | When set to Yes , the phone performs a blind transfer to a remote number. When set to no, blind transfer to remote number is disabled. |
| BLF Label Display Mode | Options to select a mode which displays on the phone screen for BLF. Default: Blank |

| Note | This option is only effective when the blf option is added. |
|---|---|

| Note | Adding the sd option automatically allows users to configure speed dial to a monitored line (speed dial with BLF) when the blf option is added. |
|---|---|

| Parameter | Description |
|---|---|
| Unit Enable | Indicates whether the key expansion module that is added to the phone is enabled. |
| Unit Online | Indicates whether the key expansion module that is added to the phone is active. |
| HW Version | Displays the hardware version of the key expansion module that is added to the phone.. |
| SW Version | Displays the software version of the key expansion module that is added to the phone. |

| Parameter | Description |
|---|---|
| Enable TR-069 | Settings that enables or disables the TR-069 function. Default: Disabled |
| ACS URL | URL of the ACS that uses the CPE WAN Management Protocol. This parameter must be in the form of a valid HTTP or HTTPS URL.
                                             The host portion of this URL is used by the CPE to validate the ACS certificate when it uses SSL or TLS. |
| ACS Username | Username that authenticates the CPE to the ACS when ACS uses the CPE WAN Management Protocol. This username is used only for
                                             HTTP-based authentication of the CPE. If the user name is not configured, admin is used as default. |
| ACS Password | Password to access to the ACS for a specific user. This password is used only for HTTP-based authentication of the CPE. If the password is not configured, admin is used as default. |
| ACS URL In Use | URL of the ACS that is currently in use. This is a read-only field. |
| Connection Request URL | URL of the ACS that makes the connection request to the CPE. |
| Connection Request Username | Username that authenticates the ACS that makes the connection request to the CPE. |
| Connection Request Password | Password used to authenticate the ACS that makes a connection request to the CPE. |
| Periodic Inform Interval | Duration in seconds of the interval between CPE attempts to connect to the ACS when Periodic Inform Enable is set to yes. Default value is 20 seconds. |
| Periodic Inform Enable | Settings that enables or disables the CPE connection requests. Default value is Yes. |
| TR-069 Traceability | Settings that enables or disables TR-069 transaction logs. The default value is No. |
| CWMP V1.2 Support | Settings that enables or disables CPE WAN Management Protocol (CWMP) support. If set to disable, the phone does not send any
                                             Inform messages to the ACS nor accept any connection requests from the ACS. Default value is Yes. |
| TR-069 VoiceObject Init | Settings to modify voice objects. Select Yes to initialize all voice objects to factory default values or select No to retain
                                             the current values. |
| TR-069 DHCPOption Init | Settings to modify DHCP settings. Select Yes to initialize the DHCP settings from the ACS or select No to retain the current
                                             DHCP settings. |
| TR-069 Fallback Support | Settings that enables or disables the TR-069 fallback support. If the phone attempts to discover the ACS with DHCP and is unsuccessful, the phone next uses DNS to resolve the ACS IP address. |
| BACKUP ACS URL | Backup URL of the ACS that uses the CPE WAN Management Protocol. This parameter must be in the form of a valid HTTP or HTTPS
                                             URL. The host portion of this URL is used by the CPE to validate the ACS certificate when it uses SSL or TLS. |
| BACKUP ACS User | Backup username that authenticates the CPE to the ACS when ACS uses the CPE WAN Management Protocol. This username is used
                                             only for HTTP-based authentication of the CPE. |
| BACKUP ACS Password | Backup password to access to the ACS for a specific user. This password is used only for HTTP-based authentication of the
                                             CPE. |
| Note If you do not configure the above parameters, you can also fetch them through DHCP options 60,43, and 125. | Note | If you do not configure the above parameters, you can also fetch them through DHCP options 60,43, and 125. |
| Note | If you do not configure the above parameters, you can also fetch them through DHCP options 60,43, and 125. |

| Note | If you do not configure the above parameters, you can also fetch them through DHCP options 60,43, and 125. |
|---|---|