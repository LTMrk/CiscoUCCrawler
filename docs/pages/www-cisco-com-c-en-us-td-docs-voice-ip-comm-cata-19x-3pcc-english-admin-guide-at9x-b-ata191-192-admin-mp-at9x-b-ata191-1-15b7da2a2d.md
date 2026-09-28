---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-english-admin-guide-at9x-b-ata191-192-admin-mp-at9x-b-ata191-1-15b7da2a2d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/english/admin-guide/at9x_b_ata191-192-admin-mp/at9x_b_ata191-192-admin-mp_chapter_011.html
retrieved_at: 2026-08-21T12:49:27.355962+00:00
---

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

# Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

Updated: January 30, 2026

Chapter: Voice Settings Configuration

## Chapter: Voice Settings Configuration

# Voice Settings Configuration

## Information

Use the Voice > Information page to view information about the ATA voice application.

### Product Information

Field

Description

Product Name

The product name of ATA.

Serial Number

The serial number of ATA.

Software Version

The software version of ATA.

Hardware Version

The hardware version of ATA.

MAC Address

The mac address of ATA.

Client Certificate

The client certificate of ATA.

Customization

The customization of ATA.

### System Status

Field

Description

Current Time

Current date and time of the system; for example, 10/3/2003 16:43:00.

Set the system time by using the Network Setup > Time Settings page.

Elapsed Time

Total time elapsed since the last reboot of the system; for example, 25 days and 18:12:36.

RTP Packets Sent

Total number of RTP packets sent, including redundant packets.

RTP Bytes Sent

Total number of RTP bytes sent.

RTP Packets Recv

Total number of RTP packets received, including redundant packets.

RTP Bytes Recv

Total number of RTP bytes received.

SIP Messages Sent

Total number of SIP messages sent, including retransmissions.

SIP Bytes Sent

Total number of bytes of SIP messages sent, including retransmissions.

SIP Messages Recv

Total number of SIP messages received, including retransmissions.

SIP Bytes Recv

Total number of bytes of SIP messages received, including retransmissions.

External IP

The External IP address used for NAT mapping.

### Line 1 and Line 2 Settings (PHONE 1 and PHONE 2)

Use the Voice > Line 1 and Voice > Line 2 pages to configure the settings for calls through the PHONE 1 and PHONE 2 ports.

Enter the settings as described. After making changes, click Submit to save your settings, or click Cancel to redisplay the page with the saved settings.

In a configuration profile, the FXS parameters must include an appropriate numeral for identifying the port receiving the
                                          setting.

### Custom CA Status

Field

Description

Custom CA Provisioning Status

The status of the latest custom CA (Certificate Authority) certificate download.

Custom CA Info

The successfully downloaded CA information, or “Not Installed” if no custom CA certificate was installed.

Default setting: Not Installed

### Provision Status

Field

Description

Provisioning Profile

Profile rule setting

Default setting: Empty

Provision Status

Indicate the status of last provisioning

Default setting: Empty

Provisioning Failure Reason

Reason for failure

Default setting: Empty

### MIC Cert Refresh Status

Use the fields under the section MIC Cert Settings from Voice > Provisioning to enable the MIC certificate renewal. Once you submit the changes, you can view the certificate refreshing status under
                                 the section MIC Cert Refresh Status from Voice > Information .

Field

Description

MIC Cert Provisioning Status

The download status of the latest renewed MIC certificate from the SUDI renewal service. If the certificate download is successful,
                                             the status is Download Successful . Otherwise, you might receive one of the following error messages:

Downlaod Failed: Dns query failed

Downlaod Failed: Bad scheme

Downlaod Failed: resource exhausted

Downlaod Failed:Connection error

Downlaod Failed:File not found

Downlaod Failed: Access violation

Downlaod Failed: Disk full

Downlaod Failed: Bad operation

Downlaod Failed: Bad option

Downlaod Failed: internal server error

Downlaod Failed: Not Implemented

Downlaod Failed: Bad Gateway

Downlaod Failed: Service Unavailable

Downlaod Failed: Zero file size

Downlaod Failed: file size exceed

Downlaod Failed: corrupted file

Downlaod Failed: Unknown, error code(**)

If the system detects that the ATA doesn't need to renew the MIC certificate, the status is still empty.

Default: Empty

MIC CA Info

Common name of the Certificate Authority (CA) that issues the MIC certificate. It can be one of the following:

Cisco Manufacturing CA

Cisco Manufacturing CA II

Cisco Manufacturing CA III

For a successful MIC certificate renewal, the common name is Cisco Manufacturing CA III .

For a failed MIC certificate renewal, the common name can be Cisco Manufacturing CA or Cisco Manufacturing CA II .

Default: Empty

## System

Use the Voice > System page to configure general voice system settings and to enable logging by using a syslog server. Logging can also be configured
                           in the Administration > Logging pages.

### System Configuration

Field

Description

Restricted Access Domains

Domain that Cisco IP phones responds to SIP messages only from the identified servers. Applicable to Line 1.

IVR Admin Passwd

Password for the administrator to manage the ATA by using the built-in IVR through a connected phone.

Network Startup Delay

The number of seconds of delay between restarting the voice module and initializing network interface.

Default setting: 3

### Miscellaneous Settings

Field

Description

DNS Query TTL Ignore

In DNS packages, the server suggests a TTL value to the client. If this parameter is set to Yes, the value from the server
                                          is ignored.

Default setting: No

Survivability Test Mode

Determines whether the ATA will always register to the Local Survivability Gateway (LSG) nodes even though the Webex Calling
                                          Session Signaling Engine (SSE) nodes are reachable.

This mode is used to test whether the LSG nodes can work normally.

Default setting: No

### Security Settings

Field

Description

FIPS Mode

Determine whether to enable or disable the Federal Information Processing Standards (FIPS) 140-3 cryptographic module on the
                                          ATA. If enabled, the product is in compliance with the standard.

FIPS standards are designed to ensure the security and interoperability of information systems used by the federal government
                                          and its contractors.

Click Enabled to enable this feature, or click Disabled to disable it.

When you failed to enable the FIPS mode, the LED on the Problem Report Tool (PRT) button lights up in solid amber. Press the PRT button to clear the warning and turn off the PRT LED.

When the FIPS mode is enabled, TR-069 may not function.

When the FIPS mode is enabled, the following features can work seamlessly on the ATA:

Image authentication

Secure Storage

TLS (HTTPs, PRT upload, Firmware upgrade, Profile resync, Onboard service, SIP over TLS)

SIP Digest (RFC 8760)

SRTP

SNMPV3

Default setting: Disabled

TLS Min Version

Select the minimum protocol version required for the TLS connections.

If the TLS version on the remote side is older than the selected TLS version on the ATA, the TLS connection will be rejected.
                                          See the table TLS Minimum Version Results for details.

Available options: TLS 1.0, TLS 1.1, TLS 1.2, and TLS 1.3.

Default setting: TLS 1.1

Client TLS Min Version

Server Highest TLS Version

Results

TLS 1.0

TLS 1.0

TLS 1.0

TLS 1.1

TLS 1.1

TLS 1.2

TLS 1.2

TLS 1.3

TLS 1.3

TLS 1.1

TLS 1.0

Protocol alert

TLS 1.1

TLS 1.1

TLS 1.2

TLS 1.2

TLS 1.3

TLS 1.3

TLS 1.2

TLS 1.0

Protocol alert

TLS 1.1

Protocol alert

TLS 1.2

TLS 1.2

TLS 1.3

TLS 1.3

TLS 1.3

TLS 1.0

Protocol alert

TLS 1.1

Protocol alert

TLS 1.2

Protocol alert

TLS 1.3

TLS 1.3

## SIP

Use the Voice > SIP page to configure SIP parameters and values.

Enter the settings as described below. After making changes, click Submit to save your settings, or click Cancel to redisplay the page with the saved settings.

For a deeper understanding of these fields, refer to Request for Comments (RFC) 3261.

### SIP Parameters

Field

Description

Max Forward:

The maximum times a call can be forwarded. The valid range is from 1 to 255.

Default setting: 70

Max Redirection:

Number of times an invite can be redirected to avoid an infinite loop.

Default setting: 5.

Max Auth:

The maximum number of times (from 0 to 255) a request may be challenged.

Default setting: 2

SIP User Agent Name:

The User-Agent header used in outbound requests. If empty, the header is not included. Macro expansion of $A to $D corresponding
                                             to GPP_A to GPP_D allowed.

Default setting: $VERSION

SIP Server Name:

The server header used in responses to inbound responses.

Default setting: $VERSION

SIP Reg User Agent Name:

The User-Agent name to be used in a REGISTER request. If this value is not specified, the SIP User Agent Name parameter is
                                             also used for the REGISTER request.

Default setting: Blank

SIP Reg Starting Sequence Number:

Defines the SIP Reg message Sequence Number.

Default setting: Blank

SIP Accept Language:

Accept-Language header used. There is no default; this indicates that the ATA does not include this header. If empty, the
                                             header is not included.

Default setting: Blank

DTMF Relay MIME Type:

The MIME Type used in a SIP INFO message to signal a DTMF event.

Default setting: Application/dtmf-relay.

Hook Flash MIME Type:

The MIME Type used in a SIP INFO message to signal a hook flash event.

Default setting: Application/hook-flash.

Remove Last Reg:

Determines whether the ATA removes the last registration before submitting a new one, if the value is different. Select yes
                                             to remove the last registration, or select no to omit this step.

Default setting: No

Use Compact Header:

Determines if the ATA uses compact SIP headers in outbound SIP messages.

Select Yes to use compact SIP headers in outbound SIP messages.

Select No to use normal SIP headers.

If inbound SIP requests contain compact headers, the ATA reuses the same headers when generating the response regardless of
                                             the Use Compact Header parameter. If inbound SIP requests contain normal headers, the ATA substitutes those headers with compact
                                             headers as defined by RFC 261 when Use Compact Header is set to Yes.

Default setting: No

Escape Display Name:

Determines if the Display Name is private. Select Yes if you want the ATA to enclose the string configured in the Display Name in a pair of double quotes for out bound SIP messages.
                                             If the display name includes " or \, these will be escaped to \" and \\ within the double quotes. Otherwise, select No .

Default setting: No

RFC 2543 Call Hold:

Configures the type of call hold: a:sendonly or 0.0.0.0. Do not use the 0.0.0.0 syntax in a HOLD SDP; use the a:sendonly syntax.

Default setting: Yes

Mark All AVT Packets:

Select Yes if you want all AVT tone packets encoded for redundancy to have the marker bit set for each DTMF event.

Select No to have the marker bit set only for the first packet.

Default setting: Yes

AVT Packet Size:

Indicates the AVT Packet size according to value set in ptime or fixed 10ms.

Default setting: ptime

SIP TCP Port Min:

The lowest TCP port number that can be used for SIP sessions.

Default setting: 5060

SIP TCP Port Max:

The highest TCP port number that can be used for SIP sessions.

Default setting: 5080

CTI Enable:

Enables or disables the Computer Telephone Interface feature provided by some servers.

Default setting: no

Keep Referee When REFER Failed:

Set this parameter to Yes to configure the phone to handle NOTIFY sipfrag messages.

You can also configure this parameter in the configuration file:

```
<Keep_Referee_When_REFER_Failed ua="na">Yes
```

```
</Keep_Referee_When_REFER_Failed>
```

Caller ID Header:

Provides the option to take the caller ID from PAID-RPID-FROM,P-ASSERTEDIDENTITY, REMOTE-PARTY-ID, or FROM header.

Default setting: PAID-RPID-FROM

### SIP Timer Values

Field

Description

SIP T1

RFC 3261 T1 value (round-trip time estimate), which can range from 0 to 64 seconds.

Default setting: 0.5

SIP T2

RFC 3261 T2 value (maximum retransmit interval for non-INVITE requests and INVITE responses), which can range from 0 to 64
                                          seconds.

Default setting: 4

SIP T4

RFC 3261 T4 value (maximum duration a message remains in the network), which can range from 0 to 64 seconds.

Default setting: 5

SIP Timer B

INVITE time-out value, which can range from 0 to 64 seconds.

Default setting: 32

SIP Timer F

Non-INVITE time-out value, which can range from 0 to 64 seconds.

Default setting: 16

SIP Timer H

H INVITE final response, time-out value, which can range from 0 to 64 seconds.

Default setting: 32

SIP Timer D

ACK hang-around time, which can range from 0 to 64 seconds.

Default setting: 32

SIP Timer J

Non-INVITE response hang-around time, which can range from 0 to 64 seconds.

Default setting: 32

INVITE Expires

INVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Range: 0–(2 31 –1)

Default setting: 240

ReINVITE Expires

ReINVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Range: 0–(2 31 –1)

Default setting: 30

Reg Min Expires

Minimum registration expiration time allowed from the proxy in the Expires header or as a Contact header parameter. If the
                                          proxy returns a value less than this setting, the minimum value is used.

Default setting: 1

Reg Max Expires

Maximum registration expiration time allowed from the proxy in the Min-Expires header. If the value is larger than this setting,
                                          the maximum value is used.

Default setting: 7200

Reg Retry Intvl

Interval to wait before the ATA retries registration after failing during the last registration.

Default setting: 30

Reg Retry Long Intvl

When registration fails with a SIP response code that does not match Retry Reg RSC, the ATA waits for the specified length
                                          of time before retrying. If this interval is 0, the ATA stops trying. This value must be larger than the Reg Retry Intvl value,
                                          which cannot be 0.

Default setting: 1200

Reg Retry Random Delay

Random delay range (in seconds) to add to Register Retry Intvl when retrying REGISTER after a failure.

Default setting: 0 (disabled)

Reg Retry Long Random Delay

Random delay range (in seconds) to add to Register Retry Long Intvl when retrying REGISTER after a failure.

Default setting: 0 (disabled)

Reg Retry Intvl Cap

The maximum value to cap the exponential back-off retry delay (which starts at Register Retry Intvl and doubles on every REGISTER
                                          retry after a failure). The retry interval is always at Register Retry Intvl seconds after a failure. If this feature is enabled,
                                          Reg Retry Random Delay is added on top of the exponential back-off adjusted delay value.

Default setting: 0, which disables the exponential backoff feature.

### Response Status Code Handling

Field

Description

SIT1 RSC

SIP response status code for the appropriate Special Information Tone (SIT). Reorder or Busy tone is played by default for
                                          all unsuccessful response status code for SIT 1 RSC through SIT 4 RSC.

Default setting: blank

SIP response status code to INVITE on which to play the SIT2 Tone.

Default setting: blank

SIP response status code to INVITE on which to play the SIT3 Tone.

Default setting: blank

SIP response status code to INVITE on which to play the SIT4 Tone.

Default setting: blank

SIP response code that retries a backup server for the current request.

Default setting: blank

Interval to wait before the ATA retries registration after failing during the last registration.

Default setting: blank

### RTP Parameters

Field

Description

RTP Port Min

Minimum port number for RTP transmission and reception.

The RTP Port Min and RTP Port Max parameters should define a range that contains at least 4 even number ports, such as 100
                                          to 106.

Default setting: 16384.

RTP Port Max

Maximum port number for RTP transmission and reception.

Default setting: 16482.

RTP Packet Size

Packet size in seconds, which can range from 0.01 to 0.16. Valid values must be a multiple of 0.01 seconds.

Default setting: 0.030

RTP Tx Packet Size Follows Remote SDP

Enable the Remote pair RTP Packet Size.

Default setting: Yes

Number of successive ICMP errors allowed when transmitting RTP packets to the peer before the ATA terminates the call. If
                                          value is set to 0, the ATA ignores the limit on ICMP errors.

Default setting: 0

Interval for sending out RTCP sender reports on an active connection. It can range from 0 to 255 seconds. During an active
                                          connection, the ATA can be programmed to send out compound RTCP packet on the connection. Each compound RTP packet except
                                          the last one contains a SR (Sender Report) and a SDES (Source Description). The last RTCP packet contains an extra BYE packet.
                                          Each SR except the last one contains exactly 1 RR (Receiver Report); the last SR carries no RR. The SDES contains CNAME, NAME,
                                          and TOOL identifiers. The CNAME is set to <User ID>@<Proxy>, NAME is set to <Display Name> (or Anonymous if user blocks caller
                                          ID), and TOOL is set to the Vendor/Hardware-platform-software-version. The NTP timestamp used in the SR is a snapshot of the
                                          local time for the ATA, not the time reported by an NTP server. If the ATA receives a RR from the peer, it attempts to compute
                                          the round-trip delay and show it as the Call Round Trip Delay value (ms) on the Information page.

Default setting: 0

Select yes if you want the ATA to calculate the UDP header checksum for SIP messages. Otherwise, select no.

Default setting: no

Determines whether the ATA includes the P-RTP-Stat header or response in a BYE message. The header contains the RTP statistics
                                          of the current call. Select yes or no from the drop-down list.

Default setting: yes

The format of the P-RTP-Stat header is:

P-RTP-State: PS=<packets sent>,OS=<octets sent>,PR=<packets received>,OR=<octets received>,PL=<packets lost>,JI=<jitter in
                                          ms>,LA=<delay in ms>,DU=<call duration ins>,EN=<encoder>,DE=<decoder>.

Call Statistics

Specifies whether the phone sends end-of-call statistics within SIP messages when a call terminates or is put on hold.

You can select Yes to enable the phone to send end-of-call statistics in Session Initiation Protocol (SIP) messages (BYE and re-INVITE messages).
                                          The phone sends call statistics to the other party of the call when the call terminates or when the call is on hold. The statistics
                                          include:

Real-time Transport Protocol (RTP) packets sent or received

Total bytes sent or received

Total number of lost packets

Delay jitter

Round-trip delay

Call duration

The call statistics are sent as headers in SIP BYE messages and SIP BYE response messages (200 OK and re-INVITE during hold).
                                          For audio sessions, the headers are RTP-RxStat and RTP-TxStat.

Rtp-Rxstat -> Data received

Rtp-Txstat -> Data transmitted

Example of call statistics in a SIP BYE message:

From: xxxx

User-Agent: xxxx

Call-ID: xxxx

Rtp - Rxstat :Dur=13,Pkt=408,Oct=97680,LatePkt=8,LostPkt=0,AvgJit=0,VQMetrics="CCR=0.0017;ICR=0.0000;ICRmx=0.0077;CS=2;

SCS=0;VoRxCodec=PCMU;CID=4;VoPktSizeMs=30;VoPktLost=0;VoPktDis=1;VoOneWayDelayMs=281;maxJitter=12;MOScq=4.21;MOSlq=3.52;network=ethernet;hwType=CP-8865;rtpBitrate=60110;rtcpBitrate=0“

You can also use the Call_Statistics parameter in the phone configuration file to enable this feature.

Default: Yes

Options: Yes and No

### SDP Payload Types

Field

Description

NSE dynamic payload type. The valid range is 96-127.

Default setting: 100

AVT dynamic payload type. The valid range is 96-127.

Default setting: 101

INFOREQ Dynamic Payload

INFOREQ dynamic payload type.

Default setting: blank

G726r32 Dynamic Payload

G726r32 dynamic payload type.

Default setting: 2

G729b Dynamic Payload

G.729b dynamic payload type. The valid range is 96-127.

Default setting: 99

EncapRTP Dynamic Payload

EncapRTP Dynamic Payload type.

Default setting: 112

RTP-Start-Loopback Dynamic Payload

RTP-Start-Loopback Dynamic Payload type.

Default setting: 113

RTP-Start-Loopback Codec

RTP-Start-Loopback Codec. Select one of the following: G711u, G711a, G726-32, G729a.

Default setting: G711u

NSE Codec Name

NSE codec name used in SDP.

Default setting: NSE

AVT Codec Name

AVT codec name used in SDP.

Default setting: telephone-event

G711u Codec Name

G.711u codec name used in SDP.

Default setting: PCMU

G711a Codec Name

G.711a codec name used in SDP.

Default setting: PCMA

G726r32 Codec Name

G.726-32 codec name used in SDP.

Default setting: G726-32

G729a Codec Name

G.729a codec name used in SDP.

Default setting: G729a

G729b Codec Name

G.729b codec name used in SDP.

Default setting: G729ab

EncapRTP Codec Name

EncapRTP codec name used in SDP.

Default setting: encaprtp

### NAT Support Parameters

Field

Description

If you select Yes , the ATA processes the received parameter in the VIA header. The server inserts this value in a response to any one of its
                                          requests. If you select No , the parameter is ignored.

If you select Yes , the ATA processes the rport parameter in the VIA header. This value is inserted by the server in a response to any one of
                                          its requests. If you select No , the parameter is ignored.

Default setting: No

Inserts the received parameter into the VIA header of SIP responses if the received-from IP and VIA sent-by IP values differ.

Select Yes or No from the drop-down menu.

Default setting: No

Inserts the parameter into the VIA header of SIP responses if the received-from IP and VIA sent-by IP values differ.

Select Yes or No from the drop-down menu.

Default setting: No

Lets you use NAT-mapped IP:port values in the VIA header. Select yes or no from the drop-down menu.

Default setting: No

Sends responses to the request source port instead of the VIA sent-by port.

Select Yes or No from the drop-down menu.

Default setting: No

Enables the use of STUN to discover NAT mapping.

Select Yes or No from the drop-down menu.

Default setting: No

If the STUN Enable feature is enabled and a valid STUN server is available, the ATA can perform a NAT-type discovery operation
                                          when it powers on. It contacts the configured STUN server, and the result of the discovery is reported in a Warning header
                                          in all subsequent REGISTER requests. If the ATA detects symmetric NAT or a symmetric firewall, NAT mapping is disabled.

Default setting: No

IP address or fully-qualified domain name of the STUN server to contact for NAT mapping discovery.

Default setting: blank

External IP address to substitute for the actual IP address of the ATA in all outgoing SIP messages. If 0.0.0.0 is specified,
                                          no IP address substitution is performed.

If this parameter is specified, the ATA assumes this IP address when generating SIP messages and SDP. However, the results
                                          of STUN and VIA received parameter processing supersede this statically configured value.

This option requires that you have (1) a static IP address from your Internet Service Provider and (2) an edge device with
                                          a symmetric NAT mechanism. If the ATA is the edge device, the second requirement is met.

Default setting: blank

External port mapping number of the RTP Port Min. number. If this number is not zero, the RTP port number in all outgoing
                                          SIP messages is substituted for the corresponding port value in the external RTP port range.

Default setting: blank

Interval between NAT-mapping keep alive messages.

Default setting: 15

Enables or disables NAT Redirect keep alive messages.

Default setting: No

## Provisioning

Use the Voice > Provisioning page to configure profiles and parameters to configure the ATA from a remote server.

Enter the settings as described. After making changes, click Submit to save your settings, or click Cancel to redisplay the page with the saved settings.

### Configuration Profile

Field

Description

Provision Enable:

Controls all resync actions independently of firmware upgrade actions. Set to yes to enable remote provisioning.

Default setting: Yes

Resync On Reset:

Triggers a resync after every reboot except for reboots caused by parameter updates and firmware upgrades.

Default setting: Yes

Resync Random Delay:

The maximum value for a random time interval that the ATA waits before making its initial contact with the provisioning server.
                                             This delay is effective only on the initial configuration attempt following power-on or reset. The delay is a pseudo-random
                                             number between zero and this value.

This parameter is in units of 20 seconds; the default value of 2 represents 40 seconds. This feature is disabled when this
                                             parameter is set to zero.

This feature can be used to prevent an overload of the provisioning server when many devices power-on simultaneously.

Default setting: 2 (40 seconds)

Resync At (HHmm):

The time of day when the device tries to resync. The resync is performed each day. Used with the Resync At Random Delay.

Default setting: blank

Resync At Random Delay:

Used with the Resync At (HHmm) setting, this parameter sets a range of possible values for the resync delay. The system randomly
                                             chooses a value from this range and waits the specified number of seconds before attempting to resync. This feature is intended
                                             to prevent the network jam that would occur if all resynchronizing devices began the resync at the exact same time of day.

Default setting: 600

Resync Periodic:

The time interval between periodic resyncs with the provisioning server. The associated resync timer is active only after
                                             the first successful synchronization with the server. Setting this parameter to zero disables periodic resynchronization.

Default setting: 3600

Resync Error Retry Delay:

Resync retry interval (in seconds) applied if there is a resync failure. The ATA has an error retry timer that activates if
                                             the previous attempt to sync with the provisioning server fails. The ATA waits to contact the server again until the timer
                                             counts down to zero.

This parameter is the value that is initially loaded into the error retry timer. If this parameter is set to zero, the ATA
                                             immediately retries to sync with the provisioning server following a failed attempt.

Default setting: 3600

Forced Resync Delay:

Maximum delay (in seconds) that the ATA waits before performing a resync. The ATA does not resync while one of its lines is
                                             active. Because a resync can take several seconds, it is desirable to wait until the ATA has been idle for an extended period
                                             before resynchronizing. It allows you to make calls in succession without interruption.

The ATA has a timer that begins counting down when all lines become idle. This parameter is the initial value of the counter.

Resync events are delayed until this counter decrements to zero.

Default setting: 14400

Resync From SIP:

Enables a resync to be triggered with a SIP NOTIFY message.

Default setting: yes

Resync After Upgrade Attempt:

Triggers a resync after every firmware upgrade attempt.

Default setting: yes

Resync Trigger 1:

Resync Trigger 2:

Configurable resync trigger conditions. A resync is triggered when the logic equation in these parameters evaluates to TRUE.

Default setting: blank

Resync Fails On FNF:

Determines whether a file-not-found response from the provisioning server constitutes a successful or a failed resync. A failed
                                             resync activates the error resync timer.

Default setting: yes

Profile Rule:

This parameter is a profile script that evaluates to the provisioning resync command. The command is a TCP/IP operation and
                                             an associated URL. The TCP/IP operation can be TFTP, HTTP, or HTTPS.

If the command is not specified, TFTP is assumed, and the address of the TFTP server is obtained through DHCP option 66. In
                                             the URL, either the IP address or the FQDN of the server can be specified. The filename can have macros, such as $MA, which
                                             expands to the ATA MAC address.

Default setting: /spa$PSN.cfg

Profile Rule B:

Profile Rule C:

Profile Rule D:

Defines second, third, and fourth resync commands and associated profile URLs. These profile scripts are executed sequentially
                                             after the primary Profile Rule resync operation has completed. If a resync is triggered and Profile Rule is blank, Profile
                                             Rules B, C, and D are still evaluated and executed.

Default setting: blank

DHCP Option To Use:

DHCP Options, delimited by commas, retrieves firmware and profiles.

Default setting: 66.160.159.150

Transport Protocol:

Transport Protocol retrieves firmware and profiles. If none is selected, TFTP is assumed and the IP address of the TFTP server
                                             is obtained from the DHCP server.

Default setting: https

Log Resync Request Msg:

This parameter contains the message that is sent to the Syslog server at the start of a resync attempt.

Default setting: $PN $MAC -- Requesting resync $SCHEME://$SERVIP:$PORT$PATH

Log Resync Success Msg:

Syslog message issued upon successful completion of a resync attempt.

Default setting: $PN $MAC -- Successful resync $SCHEME://$SERVIP:$PORT$PATH

Log Resync Failure Msg:

Syslog message issued after a failed resync attempt.

Default setting: $PN $MAC -- Resync failed: $ERR

Report Rule:

The target URL to which configuration reports are sent. This parameter has the same syntax as the Profile_Rule parameter,
                                             and resolves to a TCP/IP command with an associated URL.

A configuration report is generated in response to an authenticated SIP NOTIFY message, with Event: report. The report is
                                             an XML file containing the name and value of all the device parameters.

This parameter may optionally contain an encryption key. For example:

[ --key $K ] tftp://ps.callhome.net/$MA/rep.xml.enc

Default setting: blank

### Firmware Upgrade

Field

Description

Upgrade Enable.

Determines if the firmware upgrade operations occur independently of resync actions.

Default setting: yes

Upgrade Error Retry Delay.

The upgrade retry interval (in seconds) applied if there is an upgrade failure. The ATA has a firmware upgrade error timer
                                          that activates after a failed firmware upgrade attempt. The timer is initialized with the value in this parameter. The next
                                          firmware upgrade attempt occurs when this timer counts down to zero.

Default setting: 3600

Downgrade Rev Limit.

Enforces a lower limit on the acceptable version number during a firmware upgrade or downgrade. The ATA does not complete
                                          a firmware upgrade operation unless the firmware version is greater than or equal to this parameter.

Default setting: blank

Upgrade Rule.

This parameter is a firmware upgrade script with the same syntax as Profile_Rule. Defines upgrade conditions and associated
                                          firmware URLs.

Default setting: blank

Log Upgrade Request Msg.

Syslog message issued at the start of a firmware upgrade attempt.

Default setting: $PN $MAC -- Requesting upgrade $SCHEME://$SERVIP:$PORT$PATH

Log Upgrade Success Msg.

Syslog message issued after a firmware upgrade attempt completes successfully.

Default setting: $PN $MAC -- Successful upgrade $SCHEME://$SERVIP:$PORT$PATH -- $ERR

Log Upgrade Failure Msg.

Syslog message issued after a failed firmware upgrade attempt.

Default setting: $PN $MAC -- Upgrade failed: $ERR

### CA Settings

Field

Description

Custom CA URL

The URL of a file location for a custom Certificate Authority (CA) certificate. Either the IP address or the FQDN of the server
                                          can be specified. The file name can have macros, such as $MA, which expands to the ATA MAC address.

Default setting: blank

### General Purpose Parameters

Field

Description

GPP A to GPP P

General purpose provisioning parameters. These parameters can be used as variables in provisioning and upgrade rules. They
                                          are referenced by prepending the variable name with a ‘$’ character, such as $GPP_A.

Default setting: blank

### MIC Cert Settings

Field

Description

MIC Cert Refresh Enable

Controls whether to enable the Manufacture Installed Certificate (MIC) renewal by the default or a specified Secure Unique
                                             Device Identifier (SUDI) service.

Default setting: no

MIC Cert Refresh Rule

Enters an HTTP URL of the SUDI service that provides the renewed MIC certificate.

You can use the default URL or specify another valid URL of a SUDI renewal service.

Default setting: http://sudirenewal.cisco.com/

## Regional

Use the Voice > Regional page to localize your system with the appropriate regional settings.

Enter the settings as described. After making changes, click Submit to save your settings, or click Cancel to redisplay the page with the saved settings.

### Ring, Cadence, and Tone Scripts

To define ring and tone patterns, the ATA uses the concept of scripts. In the next sections, you will find information about
                                 creating Cadence Scripts (CadScripts), Frequency Scripts (FreqScripts), and Tone Scripts (ToneScripts).

#### CadScript

A mini-script of up to 127 characters that specifies the cadence parameters of a signal.

Syntax: S1[;S2], where:

Si=Di(oni,1/offi,1[,oni,2/offi,2[,oni,3/offi,3[,oni,4/offi,4[,oni,5/offi,5,oni,6/offi,6]]]]]) and is known as a section, oni,j
                                    and offi,j are the on/off duration in seconds of a segment and i = 1 or 2, and j = 1 to 6. Di is the total duration of the
                                    section in seconds. All durations can have up to three decimal places to provide 1-ms resolution. The wildcard character “*”
                                    represents infinite duration. The segments within a section are played in order and repeated until the total duration is played.

##### Example 1: 60(2/4)

Number of Cadence Sections = 1

Cadence Section 1: Section Length = 60 s

Number of Segments = 1

Segment 1: On=2s, Off=4s

Total Ring Length = 60s

##### Example 2—Distinctive Ring (short,short,short,long): 60(.2/.2,.2/.2,.2/.2,1/4)

Number of Cadence Sections = 1

Cadence Section 1: Section Length = 60s

Number of Segments = 4

Segment 1: On=0.2s, Off=0.2s

Segment 2: On=0.2s, Off=0.2s

Segment 3: On=0.2s, Off=0.2s

Segment 4: On=1.0s, Off=4.0s

Total Ring Length = 60s

#### FreqScript

A mini-script of up to 127 characters that specifics the frequency and level parameters of a tone.

Syntax: F1@L1[,F2@L2[,F3@L3[,F4@L4[,F5@L5[,F6@L6]]]]

Where F1–F6 are frequency in Hz (unsigned integers only) and L1–L6 are corresponding levels in dBm (with up to 1 decimal place).
                                    White spaces are allowed before and after the comma, but they are not recommended.

##### Example 1—Call Waiting Tone: 440@-10

Number of Frequencies = 1

Frequency 1 = 440 Hz at –10 dBm

##### Example 2—Dial Tone: 350@-19,440@-19

Number of Frequencies = 2

Frequency 1 = 350 Hz at –19 dBm

Frequency 2 = 440 Hz at –19 dBm

#### ToneScript

A mini-script of up to 127 characters that specifies the frequency, level, and cadence parameters of a call progress tone.
                                    May contain up to 127 characters.

Syntax: ToneScript;Z1[;Z2].

The section Z1 is similar to the S1 section in a CadScript except that each on/off segment is followed by a frequency components
                                    parameter: Z1 = D1(oni,1/offi,1/fi,1[,oni,2/offi,2/fi,2[,oni,3/offi,3/fi,3[,oni,4/offi,4/fi,4[,oni,5/offi,5/fi,5[,oni,6/offi,6/fi,6]]]]]),
                                    where fi,j = n1[+n2]+n3[+n4[+n5[+n6]]]]] and 1 < nk < 6 indicates which of the frequency components given in the FreqScript
                                    are used in that segment; if more than one frequency component is used in a segment, the components are summed together.

##### Example 1—Dial tone: 350@-19,440@-19;10(*/0/1+2)

Number of Frequencies = 2

Frequency 1 = 350 Hz at –19 dBm

Frequency 2 = 440 Hz at –19 dBm

Number of Cadence Sections = 1

Cadence Section 1: Section Length = 10 s

Number of Segments = 1

Segment 1: On=forever, with Frequencies 1 and 2

Total Tone Length = 10s

##### Example 2—Stutter tone: 350@-19,440@-19;2(.1/.1/1+2);10(*/0/1+2)

Number of Frequencies = 2

Frequency 1 = 350 Hz at –19 dBm

Frequency 2 = 440 Hz at –19 dBm

Number of Cadence Sections = 2

Cadence Section 1: Section Length = 2s

Number of Segments = 1

Segment 1: On=0.1s, Off=0.1s with Frequencies 1 and 2

Cadence Section 2: Section Length = 10s

Number of Segments = 1

Segment 1: On=forever, with Frequencies 1 and 2

Total Tone Length = 12s

### Call Progress Tones

Field

Description

Dial Tone

Prompts you to enter a phone number. Reorder Tone is played automatically when Dial Tone or any of its alternatives times
                                             out.

Default setting: 350@-19,440@-19;10(*/0/1+2)

Second Dial Tone

Alternative to the Dial Tone when you dial a three-way call.

Default setting: 420@-19,520@-19;10(*/0/1+2)

Outside Dial Tone

Alternative to the Dial Tone. It prompts you to enter an external phone number, as opposed to an internal extension. A comma
                                             character in the dial plan triggers it.

Default setting: 420@-16;10(*/0/1)

Prompt Tone

Prompts you to enter a call forwarding phone number.

Default setting: 520@-19,620@-19;10(*/0/1+2)

Busy Tone

Played when a 486 RSC is received for an outbound call.

Default setting: 480@-19,620@-19;10(.5/.5/1+2)

Reorder Tone

Played when an outbound call has failed, or after the far end hangs up during an established call. Reorder Tone is played
                                             automatically when Dial Tone or any of its alternatives times out.

Default setting: 480@-19,620@-19;10(.25/.25/1+2)

Off Hook Warning Tone

Played when the caller has not properly placed the handset on the cradle. Off Hook Warning Tone is played when the Reorder
                                             Tone times out.

Default setting: 480@-10,620@0;10(.125/.125/1+2)

Ring Back Tone

Played during an outbound call when the far end is ringing.

Default setting: 440@-19,480@-19;*(2/4/1+2)

Ring Back 2 Tone

Your ATA plays this tone instead of Ring Back Tone if the called party replies with a SIP 182 response without SDP to its
                                             outbound INVITE request.

Default setting: the same as Ring Back Tone, except the cadence is 1s on and 1s off.

Default setting: 440@-19,480@-19;*(1/1/1+2)

Confirm Tone

Brief tone to notify you that the last input value has been accepted.

Default setting: 600@-16;1(.25/.25/1)

SIT1 Tone

Alternative to the Reorder Tone played when an error occurs as a caller makes an outbound call. The RSC to trigger this tone
                                             is configurable on the SIP screen.

Default setting: 985@-16,1428@-16,1777@-16;20(.380/0/1,.380/0/2,.380/0/3,0/4/0)

SIT2 Tone

Alternative to the Reorder Tone played when an error occurs as a caller makes an outbound call. The RSC to trigger this tone
                                             is configurable on the SIP screen.

Default setting: 914@-16,1371@-16,1777@-16;20(.274/0/1,.274/0/2,.380/0/3,0/4/0)

SIT3 Tone

Alternative to the Reorder Tone played when an error occurs as a caller makes an outbound call. The RSC to trigger this tone
                                             is configurable on the SIP screen.

Default setting: 914@-16,1371@-16,1777@-16;20(.380/0/1,.380/0/2,.380/0/3,0/4/0)

SIT4 Tone

Alternative to the Reorder Tone played when an error occurs as a caller makes an outbound call. The RSC to trigger this tone
                                             is configurable on the SIP screen.

Default setting: 985@-16,1371@-16,1777@-16;20(.380/0/1,.274/0/2,.380/0/3,0/4/0)

MWI Dial Tone

Played instead of the Dial Tone when there are unheard messages in the caller’s mailbox.

Default setting: 350@-19,440@-19;2(.1/.1/1+2);10(*/0/1+2)

Cfwd Dial Tone

Played when all calls are forwarded.

Default setting: 350@-19,440@-19;2(.2/.2/1+2);10(*/0/1+2)

Holding Tone

Informs the local caller that the far end has placed the call on hold.

Default setting: 600@-19;*(.1/.1/1,.1/.1/1,.1/9.5/1)

Conference Tone

Played to all parties when a three-way conference call is in progress.

Default setting: 350@-19;20(.1/.1/1,.1/9.7/1)

Secure Call Indication Tone

Played when a call has been successfully switched to secure mode. Play it for a short period - less than 30 seconds - and
                                             at a reduced level - less than 19 dBm - so it doesn't interfere with the call.

Default setting: 397@-19,507@-19;15(0/2/0,.2/.1/1,.1/2.1/2)

Feature Invocation Tone

Played when a feature is implemented.

Default setting: 350@-16;*(.1/.1/1)

Call Remind Tone

The holding tone is played on the Phone ports during the active call to remind you of the held call.

Default setting: blank

### Distinctive Ring Patterns

Field

Description

Ring1 Cadence

Cadence script for distinctive ring 1.

Default setting: 60(2/4)

Ring2 Cadence

Cadence script for distinctive ring 2.

Default setting: 60(.8/.4,.8/4)

Ring3 Cadence

Cadence script for distinctive ring 3.

Default setting: 60(.4/.2,.4/.2,.8/4)

Ring4 Cadence

Cadence script for distinctive ring 4.

Default setting: 60(.3/.2,1/.2,.3/4)

Ring5 Cadence

Cadence script for distinctive ring 5.

Default setting: 1(.5/.5)

Ring6 Cadence

Cadence script for distinctive ring 6.

Default setting: 60(.2/.4,.2/.4,.2/4)

Ring7 Cadence

Cadence script for distinctive ring 7.

Default setting: 60(.4/.2,.4/.2,.4/4)

Ring8 Cadence

Cadence script for distinctive ring 8.

Default setting: 60(0.25/9.75)

### Distinctive Call Waiting Tone Patterns

Field

Description

CWT1 Cadence

Cadence script for distinctive CWT 1.

Default setting: *(.3/9.7)

CWT2 Cadence

Cadence script for distinctive CWT 2.

Default setting: 30(.1/.1, .1/9.7)

CWT3 Cadence

Cadence script for distinctive CWT 3.

Default setting: 30(.1/.1, .1/.1, .1/9.7)

CWT4 Cadence

Cadence script for distinctive CWT 4.

Default setting: 30(.1/.1, .3/.1, .1/9.3)

CWT5 Cadence

Cadence script for distinctive CWT 5.

Default setting: 1(.5/.5)

CWT6 Cadence

Cadence script for distinctive CWT 6.

Default setting: 30(.1/.1,.3/.2,.3/9.1)

CWT7 Cadence

Cadence script for distinctive CWT 7.

Default setting: 30(.3/.1,.3/.1,.1/9.1)

CWT8 Cadence

Cadence script for distinctive CWT 8.

Default setting: 2.3(.3/2)

### Distinctive Ring/CWT Pattern Names

Field

Description

Ring1 Name

Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 1 for the inbound call.

Default setting: Bellcore-r1

Ring2 Name

Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 2 for the inbound call.

Default setting: Bellcore-r2

Ring3 Name

Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 3 for the inbound call.

Default setting: Bellcore-r3

Ring4 Name

Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 4 for the inbound call.

Default setting: Bellcore-r4

Ring5 Name

Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 5 for the inbound call.

Default setting: Bellcore-r5

Ring6 Name

Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 6 for the inbound call.

Default setting: Bellcore-r6

Ring7 Name

Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 7 for the inbound call.

Default setting: Bellcore-r7

Ring8 Name

Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 8 for the inbound call.

Default setting: Bellcore-r8

### Ring and Call Waiting Tone Spec

IMPORTANT: Ring and Call Waiting tones do not work the same way on all phones. When setting ring tones, consider the following recommendations:

Begin with the default Ring Waveform, Ring Frequency, and Ring Voltage.

If your ring cadence doesn’t sound right, or your phone doesn’t ring, change the following settings:

Ring Waveform: Sinusoid

Ring Frequency: 25

Ring Voltage: 80

Field

Description

Ring Waveform

Waveform for the ringing signal. Choices are Sinusoid or Trapezoid.

Default setting: Trapezoid

Ring Frequency

Frequency of the ringing signal. Valid values are 15–50 (Hz)

Default setting: 20

Ring Voltage

Ringing voltage. Choices are 30–90 (V)

Default setting: 85

CWT Frequency

Frequency script of the call waiting tone. All distinctive CWTs are based on this tone.

Default setting: 440@-10

Synchronized Ring

If this is set to yes, when the ATA is called, all lines ring at the same time (similar to a regular PSTN line). After one
                                             line answers, the others stop ringing.

Default setting: no

### Control Timer Values (Sec)

Field

Description

Hook Flash Timer Min.

Minimum on-hook time before off-hook qualifies as hook flash. Less than this value, and the on-hook event is ignored. Range:
                                             0.1–0.4 seconds.

Default setting: 0.1

Hook Flash Timer.

Max Maximum on-hook time before off-hook qualifies as hook flash. More than this value, and the on-hook event is treated as
                                             on hook (no hook-flash event).

Range: 0.4–1.6 seconds.

Default setting: 0.9

Callee On Hook Delay.

Phone must be on-hook for time before the ATA tears down the current inbound call. It does not apply to outbound calls.

Range: 0–255 seconds.

Default setting: 0

Reorder Delay.

Delay after far end hangs up before reorder tone is played. 0 = plays immediately, inf = never plays. Range: 0–255 seconds.

Default setting: 5.

Call Back Expires.

Expiration time in seconds of a call back activation. Range: 0–65535 seconds.

Default setting: 1800

Call Back Retry Intvl.

Call back retry interval in seconds. Range: 0–255 seconds.

Default setting: 30

Call Back Delay.

Delay after receiving the first SIP 18x response before declaring the remote end is ringing. If a busy response is received
                                             during this time, the ATA still considers the call as failed and keeps on retrying. Range: 0–65 seconds.

Default setting: 0.5

VMWI Refresh Intvl.

Interval between VMWI refresh to the device. Range: 0–65535 seconds.

Default setting: 0

Interdigit Long Timer.

Long timeout between entering digits when dialing. The interdigit timer values are used as defaults when dialing. The Interdigit_Long_Timer
                                             is used after any one digit, if all valid matching sequences in the dial plan are incomplete as dialed. Range: 0–64 seconds.

Default setting: 10

Interdigit Short Timer.

Short timeout between entering digits when dialing. The Interdigit_Short_Timer is used after any one digit, if at least one
                                             matching sequence is complete as dialed, but more dialed digits would match other as yet incomplete sequences. Range: 0–64
                                             seconds.

Default setting: 3

CPC Delay.

Delay in seconds after caller hangs up when the ATA starts removing the tip-and-ring voltage to the attached equipment of
                                             the called party. The range is 0–255 seconds. This feature is generally used for answer supervision on the caller side to
                                             signal to the attached equipment when the call has been connected (remote end has answered) or disconnected (remote end has
                                             hung up) This feature should be disabled for the called party (in other words, by using the same polarity for connected and
                                             idle state) and the CPC feature should be used instead.

Without CPC enabled, reorder tone is played after a configurable delay. If CPC is enabled, dial tone will be played when tip-to-ring
                                             voltage is restored. Resolution is 1 second.

Default setting: 2

CPC Duration.

Duration in seconds for which the tip-to-ring voltage is removed after the caller hangs up. After that, tip-to-ring voltage
                                             is restored and the dial tone applies if the attached equipment is still off-hook. CPC is disabled if this value is set to
                                             0. Range: 0 to 1.000 second. Resolution is 0.001 second.

Default setting: 0.5

### Vertical Service Activation Codes

Vertical Service Activation Codes are automatically appended to the dial-plan. There is no need to include them in dial-plan,
                                 although no harm is done if they are included.

Field

Description

Call Return Code.

Call Return Code This code calls the last caller.

Default setting: *69

Call Redial Code.

Redials the last number called.

Default setting: *07

Blind Transfer Code.

Begins a blind transfer of the active call to the extension specified after the activation code.

Default setting: *98

Call Back Act Code.

Starts a callback when the last outbound call is not busy.

Default setting: *66

Call Back Deact Code.

Cancels a callback.

Default setting: *86

Call Back Busy Act Code.

Starts a callback when the last outbound call is busy.

Default setting: *05

Cfwd All Act Code.

Forwards all calls to the extension specified after the activation code.

Default setting: *72

Cfwd All Deact Code.

Cancels call forwarding of all calls.

Default setting: *73

Cfwd Busy Act Code.

Forwards busy calls to the extension specified after the activation code.

Default setting: *90

Cfwd Busy Deact Code.

Cancels call forwarding of busy calls.

Default setting: *91

Cfwd No Ans Act Code.

Forwards no-answer calls to the extension specified after the activation code.

Default setting: *92

Cfwd No Ans Deact Code.

Cancels call forwarding of no-answer calls.

Default setting: *93

Cfwd Last Act Code.

Forwards the last inbound or outbound call to the number that you specify after entering the activation code.

Default setting: *63

Cfwd Last Deact Code.

Cancels call forwarding of the last inbound or outbound call.

Default setting: *83

Block Last Act Code.

Blocks the last inbound call.

Default setting: *60

Block Last Deact Code.

Cancels blocking of the last inbound call.

Default setting: *80

Accept Last Act Code.

Accepts the last outbound call. It lets the call ring through when Do Not Disturb or call forwarding of all calls are enabled.

Default setting: *64

Accept Last Deact Code.

Cancels the code to accept the last outbound call.

Default setting: *84

CW Act Code.

Enables call waiting on all calls.

Default setting: *56

CW Deact Code.

Disables call waiting on all calls.

Default setting: *57

CW Per Call Act Code.

Enables call waiting for the next call.

Default setting: *71

CW Per Call Deact Code.

Disables call waiting for the next call.

Default setting: *70

Block CID Act Code.

Blocks caller ID on all outbound calls.

Default setting: *67

Block CID Deact Code.

Removes caller ID blocking on all outbound calls.

Default setting: *68

Block CID Per Call Act Code.

Blocks caller ID on the next outbound call.

Default setting: *81

Block CID Per Call Deact Code.

Removes caller ID blocking on the next inbound call.

Default setting: *82

Block ANC Act Code.

Blocks all anonymous calls.

Default setting: *77

Block ANC Deact Code.

Removes blocking of all anonymous calls.

Default setting: *87

DND Act Code.

Enables the Do Not Disturb feature.

Default setting: *78

DND Deact Code.

Disables the Do Not Disturb feature.

Default setting: *79

CID Act Code.

Enables caller ID generation.

Default setting: *65

CID Deact Code.

Disables caller ID generation.

Default setting: *85

CWCID Act Code.

Enables call waiting, caller ID generation.

Default setting: *25

CWCID Deact Code.

Disables call waiting, caller ID generation.

Default setting: *45

Dist Ring Act Code.

Enables the distinctive ringing feature.

Default setting: *26

Dist Ring Deact Code.

Disables the distinctive ringing feature.

Default setting: *46

Speed Dial Act Code.

Assigns a speed dial number.

Default setting: *74

Paging Code.

Used for paging other clients in the group.

Default setting: *96

Secure All Call Act Code.

Makes all outbound calls secure.

Default setting: *16

Secure No Call Act Code.

Makes all outbound calls not secure.

Default setting: *17

Secure One Call Act Code.

Makes the next outbound call secure. (It is redundant if all outbound calls are secure by default).

Default setting: *18

Secure One Call Deact Code.

Makes the next outbound call not secure. (It is redundant if all outbound calls are not secure by default).

Default setting: *19

Conference Act Code.

If this code is specified, you must enter it before dialing the third party for a conference call. Enter the code for a conference
                                             call.

Default setting: blank

Attn-Xfer Act Code.

If the code is specified, you must enter it before dialing the third party for a call transfer. Enter the code for a call
                                             transfer.

Default setting: blank

Modem Line Toggle Code.

Toggles the line to a modem. Modem passthrough mode can be triggered only by pre-dialing this code.

Default setting: *99

FAX Line Toggle Code.

Toggles the line to a fax machine.

Default setting: #99

Media Loopback Code.

Use for media loopback.

Default setting: *03

Referral Services Codes.

These codes tell the ATA what to do when you place the active call on hold and is listening to the second dial tone. One or
                                             more *codes can be configured into this parameter, such as *98, or *97|*98|*123, and so on. The maximum length is 79 characters.
                                             This parameter applies when you place the active call on hold by pressing the hook flash button. Each *code (and the following
                                             valid target number according to current dial plan) triggers the ATA to perform a blind transfer to a target number that is
                                             prepended by the service *code.

For example, after you dial *98, the ATA plays the Prompt Tone while waiting for you to enter a target number (which is checked
                                             according to dial plan as in normal dialing). When a complete number is entered, the ATA sends a blind REFER to the holding
                                             party with the Refer-To target equal to *98 target_number. This feature allows the ATA to hand off a call to an application
                                             server to perform further processing, such as call park.

The *codes should not conflict with any of the other vertical service codes internally processed by the ATA. You can empty
                                             the corresponding *code that you do not want the ATA to process.

Default setting: blank

Feature Dial Services Codes.

These codes let the ATA know what to do when you are listening to the first or second dial tone.

One or more *codes can be configured into this parameter, such as *72, or *72|*74|*67|*82, and so on. The maximum length is
                                             79 characters. This parameter applies when you have a dial tone (first or second dial tone).

After receiving dial tone, you enters the *code and the target number according to current dial plan. For example, after you
                                             dial *72, the ATA plays a special tone called a Prompt tone while awaiting you to enter a valid target number. When a complete
                                             number is entered, the ATA sends a INVITE to *72 target_number as in a normal call. This feature allows the proxy to process
                                             features like call forward (*72) or Block Caller ID (*67).

The *codes should not conflict with any of the other vertical service codes internally processed by the ATA. You can remove
                                             a corresponding *code that you do not want to the ATA to process.

You can add a parameter to indicate which tone plays after the *code is entered, such as *72‘c‘|*67‘p‘. Below is a list of
                                             allowed tone parameters (note the use of open quotes surrounding the parameter, without spaces).

- 'c' = <Cfwd Dial Tone>

- 'd' = <Dial Tone>

- 'm' = <MWI Dial Tone>

- 'o' = <Outside Dial Tone>

- 'p' = <Prompt Dial Tone>

- 's' = <Second Dial Tone>

- 'x' = No tones are placed, x is any digit not used above.

If no tone parameter is specified, the ATA plays Prompt tone by default.

If the *code is not to be followed by a phone number, such as *73 to cancel call forwarding, do not include this parameter.
                                             Instead, add the *code in the dial plan and the ATA send INVITE *73@..... as usual when you dial *73.

Default setting: blank

### Vertical Service Announcement Codes

Field

Description

Service Annc Base Number

Base number for service announcements.

Default setting: blank

Service Annc Extension Codes

Extension codes for service announcements.

Default setting: blank

### Outbound Call Codec Selection Codes

Field

Description

Prefer G711u Code.

Dial prefix to make G.711u the preferred codec for the call.

Default setting: *017110

Force G711u Code.

Dial prefix to make G.711u the only codec that can be used for the call.

Default setting: *027110

Prefer G711a Code.

Dial prefix to make G.711a the preferred codec for the call.

Default setting: *017111

Force G711a Code.

Dial prefix to make G.711a the only codec that can be used for the call.

Default setting: *027111

Prefer G726r32 Code.

Dial prefix to make G.726r32 the preferred codec for the call.

Default setting: *0172632

Force G726r32 Code.

Dial prefix to make G.726r32 the only codec that can be used for the call.

Default setting: *0272632

Prefer G729a Code.

Dial prefix to make G.729a the preferred codec for the call.

Default setting: *01729

Force G729a Code.

Dial prefix to make G.729a the only codec that can be used for the call.

Default setting: *02729

### Miscellaneous

Field

Description

FXS Port Impedance:

Sets the electrical impedance of the PHONE port.

600

900

600+2.16uF

900+2.16uF

220+850||120nF

220+820||115nF

200+600||100nF

Default setting: 600

FXS Port Input Gain:

Input gain in dB, up to three decimal places. The range is 6.000 to -12.000.

Default setting: -3

FXS Port Output Gain:

Output gain in dB, up to three decimal places. The range is 6.000 to -12.000. The Call Progress Tones and DTMF playback level
                                             are not affected by the FXS Port Output Gain parameter.

Default setting: -3

DTMF Playback Level:

Local DTMF playback level in dBm, up to one decimal place. Range: -30–0.

Default setting: -16.0

DTMF Twist:

To gain difference between the two tone frequency. Range: 0–5.

Default setting: 2

DTMF Playback Length:

Local DTMF playback duration in milliseconds. Range: 0–65 seconds.

Default setting: 0.1

Detect ABCD:

To enable local detection of DTMF ABCD, select Yes . Otherwise, select No . Default setting: Yes

This setting has no effect if DTMF Tx Method is INFO; ABCD is always sent OOB regardless in this setting.

Playback ABCD:

To enable local playback of OOB DTMF ABCD, select Yes . Otherwise, select No . Default setting: Yes

Caller ID Method:

Bellcore (N.Amer,China): CID, CIDCW, and VMWI. FSK sent after first ring (same as ETSI FSK sent after first ring) (no polarity
                                                      reversal or DTAS).

DTMF (Finland, Sweden): CID only. DTMF sent after polarity reversal (and no DTAS) and before first ring.

DTMF (Denmark): CID only. DTMF sent before first ring with no polarity reversal and no DTAS.

ETSI DTMF: CID only. DTMF sent after DTAS (and no polarity reversal) and before first ring.

ETSI DTMF With PR: CID only. DTMF sent after polarity reversal and DTAS and before first ring.

ETSI DTMF After Ring: CID only. DTMF sent after first ring (no polarity reversal or DTAS).

ETSI FSK: CID, CIDCW, and VMWI. FSK sent after DTAS (but no polarity reversal) and before first ring. Waits for ACK from a
                                                      device after DTAS for CIDCW.

ETSI FSK With PR (UK): CID, CIDCW, and VMWI. FSK is sent after polarity reversal and DTAS and before first ring. Waits for
                                                      ACK from a device after DTAS for CIDCW. Polarity reversal is applied only if equipment is on hook.

DTMF (Denmark) with PR: CID only. DTMF sent after polarity reversal (and no DTAS) and before first ring.

Default setting: Bellcore(N.Amer, China)

FXS Port Power Limit:

The choices are from 1 to 8. Default setting: 3

Caller ID FSK Standard:

The ATA supports bell 202 and v.23 standards for caller ID generation. Default setting: bell 202

Feature Invocation Method:

Select the method you want to use, Default, or Sweden default. Default setting: Default.

## Line 1 and Line 2 Settings (PHONE 1 and PHONE 2)

Use the Voice > Line 1 and Voice > Line 2 pages to configure the settings for calls through the PHONE 1 and PHONE 2 ports.

Enter the settings as described. After making changes, click Submit to save your settings, or click Cancel to redisplay the page with the saved settings.

In a configuration profile, the FXS parameters must include an appropriate numeral for identifying the port receiving the
                                       setting.

### General

Field

Description

Line Enable

To enable this line for service, select yes . Otherwise, select no .

Default setting: yes

### Streaming Audio Server (SAS)

Field

Description

SAS Enable

To enable the use of the line as a streaming audio source, select yes. Otherwise, select no. If enabled, the line cannot be
                                             used for outgoing calls. Instead, it auto-answers incoming calls and streams audio RTP packets to the caller.

Default setting: no

SAS DLG Refresh Intvl

A non-zero value is the interval in which the streaming audio server sends out session refresh (SIP re-INVITE) messages to
                                             determine if the connection is active. If the caller does not respond to the refresh message, the ATA ends this call with
                                             a SIP BYE message. The range is 0 to 255 seconds (0 means that the session refresh is disabled).

Default setting: 30

SAS Inbound RTP Sink

This parameter works around devices that do not play inbound RTP if the SAS line declares itself as a send-only device and
                                             tells the client not to stream out audio. This parameter is an FQDN or IP address of an RTP sink to be used by the SAS line
                                             in the SDP of its 200 response to inbound INVITE from a client. It appears in the c = line and the port number appears in
                                             the m = line of the SDP.

If this value is not specified or is equal to 0, then c = 0.0.0.0 and a=sendonly are used in the SDP to tell the SAS client
                                             not to send any RTP to this SAS line. If a non-zero value is specified, then a=sendrecv and the SAS client streams audio to
                                             the given address.

Special case: If the value is $IP, then the SAS line’s own IP address is used in the c = line and a=sendrecv. In that case,
                                             the SAS client streams RTP packets to the SAS line.

Default setting: blank

### NAT Settings

Field

Description

NAT Mapping Enable

To use externally mapped IP addresses and SIP/RTP ports in SIP messages, select yes . Otherwise, select no .

Default setting: no

NAT Keep Alive Enable

To send the configured NAT keep alive message periodically, select yes . Otherwise, select no .

Default setting: no

NAT Keep Alive Msg

Enter the keep alive message sent periodically to maintain the current NAT mapping.

Valid values are: $NOTIFY , $REGISTER , and $OPTIONS .

$NOTIFY: A NOTIFY message is sent to keep NAT alive.

$REGISTER: A REGISTER message without contact is sent.

$OPTIONS: An OPTIONS message is sent.

Default setting: $NOTIFY

NAT Keep Alive Dest

Destination receiving the NAT keep alive messages. If the value is $PROXY, the messages are sent to the current proxy server
                                             or outbound proxy server.

Default setting: $PROXY

### Network Settings

Field

Description

SIP ToS/DiffServ Value

TOS/DiffServ field value in UDP IP packets carrying a SIP message.

Default setting: 0x68

SIP CoS Value [0-7]

CoS value for SIP messages. Valid values are 0 through 7.

Default setting: 3

RTP ToS/DiffServ Value

ToS/DiffServ field value in UDP IP packets carrying RTP data.

Default setting: 0xb8

RTP CoS Value [0- 7]

CoS value for RTP data. Valid values are 0 through 7.

Default setting: 6

Network Jitter Level

Determines how jitter buffer size is adjusted by the ATA. Jitter buffer size is adjusted dynamically. The minimum jitter buffer
                                             size is 30 milliseconds or (10 milliseconds + current RTP frame size), whichever is larger, for all jitter level settings.
                                             However, the starting jitter buffer size value is larger for higher jitter levels. This setting controls the rate at which
                                             the jitter buffer size is adjusted to reach the minimum. Select the appropriate setting: low, medium, high, very high, or
                                             extremely high.

Default setting: high

Jitter Buffer Adjustment

Choose yes to enable or no to disable this feature.

Default setting: yes

### SIP Settings

Field

Description

SIP Transport

Select the protocol for SIP messages:

UDP

TCP

TLS

AUTO

The TCP choice provides “guaranteed delivery”, which assures that lost packets are retransmitted. TCP also guarantees that
                                             the SIP packages are received in the same order that they were sent. As a result, TCP overcomes the main disadvantages of
                                             UDP. In addition, for security reasons, most corporate firewalls block UDP ports. With TCP, new ports don't need to be opened
                                             or packets dropped for activities such as Internet browsing or e-commerce.

AUTO allows the ATA to select the appropriate protocol automatically, based on the NAPTR records on the DNS server.

SIP Port

Port number of the SIP message listening and transmission port.

Default setting: 5060 for PHONE1 and 5061 for PHONE2

SIP 100REL Enable

To enable the support of 100REL SIP extension for reliable transmission of provisional responses (18x) and use of PRACK requests,
                                             select yes . Otherwise, select No .

Default setting: No

EXT SIP Port

The external SIP port number.

Default setting: blank

Auth Resync-Reboot

If this feature is enabled, the ATA authenticates the sender when it receives the NOTIFY resync reboot (RFC 2617) message.
                                             To use this feature, select Yes . Otherwise, select No .

When the ATA works as a User Agent Server (UAS) and receives NOTIFY request from a User Agent Client (UAC), you can enable
                                             the 401 challenge for the NOTIFY request by doing the following:

Set the field to Yes .

Configure the fields User ID and Password (under the section Subscriber Information from Voice > Line (n) ).

You can replace User ID with Auth ID for the authentication. To achieve this, see Subscriber information for details.

Default setting: Yes

SIP Proxy-Require

The SIP proxy can support a specific extension or behavior when it sees this header from the user agent. If this field is
                                             configured and the proxy does not support it, it responds with the message, unsupported. Enter the appropriate header in the
                                             field provided.

Default setting: blank

SIP Remote-Party-ID

To use the Remote-Party-ID header instead of the From header, select Yes . Otherwise, select No .

Default setting: Yes

SIP GUID

This feature limits the registration of SIP accounts. The Global Unique ID is generated for each line for each ATA. When it
                                             is enabled, the ATA adds a GUID header in the SIP request. The GUID is generated the first time the unit boots up and stays
                                             with the unit through rebooting and even factory reset.

Default setting: No

RTP Log Intvl

The interval for the RTP log.

Default setting: 0

Restrict Source IP

If configured, the ATA drops all packets sent to its SIP Ports from an untrusted IP address. A source IP address is untrusted
                                             if it doesn't match the IP addresses resolved from the configured Proxy (or Outbound Proxy if Use Outbound Proxy is Yes).

Default setting: No

Referor Bye Delay

The number of seconds to wait before sending a BYE to the referrer to terminate a stale call leg after a call transfer).

Default setting: 4

Refer Target Bye Delay

The number of seconds to wait before sending a BYE to the refer target to terminate a stale call leg after a call transfer.

Default setting: 0

Referee Bye Delay

The number of seconds to wait before sending a BYE to the referee to terminate a stale call leg after a call transfer.

Default setting: 0

Refer-To Target Contact

To contact the refer-to target, select yes . Otherwise, select No .

Default setting: no

Sticky 183

If this feature is enabled, the ATA ignores further 180 SIP responses after receiving the first 183 SIP response for an outbound
                                             INVITE. To enable this feature, select Yes . Otherwise, select No .

Default setting: No

Auth INVITE

When enabled, authorization is required for initial incoming INVITE requests from the SIP proxy.

When the ATA works as a User Agent Server (UAS) and receives INVITE request from a User Agent Client (UAC), you can enable
                                             the 401 challenge for the INVITE request by doing the following:

Set the field to Yes .

Configure the fields User ID and Password (under the section Subscriber Information from Voice > Line (n) ).

You can replace User ID with Auth ID for the authentication. To achieve this, see Subscriber information for details.

Default setting: No

Reply 182 On Call Waiting

When enabled, the ATA replies with a SIP182 response to the caller if it is already in a call and the line is off-hook. To
                                             use this feature, select Yes .

Default setting: No

Use Anonymous With RPID

Determine whether the ATA uses “Anonymous” when Remote Party ID is requested in the SIP message.

Default setting: Yes

Use Local Addr In From

Use the local ATA IP address in the SIP FROM message.

Default setting: No

Broadsoft ALTC

Set whether the SIP is the Broadsoft ALTC.

Default setting: No

Auth Support RFC8760

Determine whether the ATA authorization supports RFC-8760.

If set to Yes , ATA authorization supports the digest algorithms SHA256, SHA-512/256, and MD5.

When ATA works as a User Agent Client (UAC), it sends SIP REGISTER or INVITE or SUBSCRIBE requests without authorization header
                                                   field. SIP server responses 401/407 status code with www-authenticate or proxy-authenticate header field. A SIP server responds
                                                   with multiple www-authenticate headers. If multiple headers are sent, each must have a different algorithm, with the most
                                                   preferred one first.

When the field, Auth Resync-Reboot , and Auth INVITE are set to Yes , ATA will send 401 status code with multiple www-authenticate header fields. The algorithm SHA-256 is top prioritized.

If set to No , ATA authorization only supports the digest algorithm MD5.

When ATA works as a User Agent Client (UAC), it sends SIP requests without authorization header field. SIP server responses
                                                   401 status code. ATA retries to send request and add an authorization header with MD5 algorithm for server to validate.

Default setting: No

MediaSec Request

Determine whether the ATA initiates media plane security negotiations with the server.

If set to Yes , ATA supports the client-initiated mode. The ATA phone can initiate media plane security negotiations.

If set to No , ATA only supports the server-initiated mode. In this case, the server initiates media plane security negotiations. The ATA
                                                   doesn't initiate negotiations, but can handle negotiation requests from the server to establish secure calls.

To use this parameter, make sure that the following conditions are satisfied:

Set Secure Call Serv (under the section Supplementary Service Subscription )  to Yes .

Set Secure Call Option (under the section Call Feature Settings ) set to Optional .

Default setting: No

MediaSec Over TLS Only

Determine how the ATA initiates or handles the media plane security negotiations. This parameter works with MediaSec Request .

If set to Yes , ATA initiates or handles media plane security negotiations only when SIP over TLS.

If set to No , ATA initiates or handles media plane security negotiations regardless of the protocol (UDP/TCP/TLS) for SIP messages.

To use this parameter, make sure the following conditions are satisfied:

Set Secure Call Serv (under the section Supplementary Service Subscription )  to Yes .

Set Secure Call Option (under the section Call Feature Settings ) set to Optional .

Default setting: No

### Set up a Secure Line

You can configure a line to only accept secure calls. If the line is configured to only accept secure calls, then any calls
                                 the line makes will be secure.

#### Before you begin

Access the phone adapter administration web page. See Access the Phone Web Interface .

Enable Secure Call Serv under Supplementary Service Subscription section from Voice > Line(n) .

SIP transport with TLS can be set statically on the phone adapter administration web page or automatically with information
                                       in the DNS NAPTR records. If the SIP transport parameter is set for the ATA line as TLS, it only allows SRTP. If the SIP transport
                                       parameter is set to AUTO, the phone adapter performs a DNS query to get the transport method.

Step 1

Select Voice > Line(n) , where n is the line number that represents PHONE 1 or PHONE 2.

Step 2

In the section Call Feature Settings , set the paramter Secure Call Option as described in Call Feature Settings .

Step 3

Click Submit .

### Call Feature Settings

Field

Description

Blind Attn-Xfer Enable

Enables the ATA to perform an attended transfer operation by ending the active call leg and performing a blind transfer of
                                             the other call leg. If this feature is disabled, the ATA performs an attended transfer operation by referring the other call
                                             leg to the active call leg, while maintaining both call legs. To use this feature, select yes . Otherwise, select no .

Default setting: no

MOH Server

User ID or URL of the auto-answering streaming audio server. When only a user ID is specified, the current or outbound proxy
                                             is contacted. Music-on-hold is disabled if the MOH Server is not specified.

Default setting: blank

Xfer When Hangup Conf

Makes the ATA perform a transfer when a conference call has ended. Select yes or no from the drop-down menu.

Default setting: yes

Conference Bridge URL

This feature supports external conference bridging for n-way conference calls (n>2), instead of mixing audio locally. To use
                                             this feature, set this parameter to that of the server's name. For example: conf@mysefver.com:12345 or conf (which uses the
                                             Proxy value as the domain).

Default setting: blank

Conference Bridge Ports

Select the maximum number of conference call participants. The range is 3 to 10.

Default setting: 3

Enable IP Dialing.

Enable or disable IP dialing. If IP dialing is enabled, you can dial [userid@] a.b.c.d[:port], where ‘@’, ‘.’, and ‘:’ are
                                             dialed by entering *, user-id must be numeric and a, b, c, d must be between 0 and 255; the port must be larger than 255.
                                             If port is not given, 5060 is used. Port and User-Id are optional. If the user-id portion matches a pattern in the dial plan,
                                             then it is interpreted as a regular phone number according to the dial plan. The INVITE message, however, is still sent to
                                             the outbound proxy if it is enabled.

Default setting: no

Emergency Number

Comma separated list of emergency number patterns. If outbound call matches one of the patterns, the ATA disables hook flash
                                             event handling. The condition is restored to normal after the call ends. Blank signifies that there is no emergency number.
                                             Maximum number length is 63 characters.

Default setting: blank

Mailbox ID

Enter the ID number of the mailbox for this line.

Default setting: blank

Feature Key Sync

Allows the phone to synchronize with the call server. If Do Not Disturb or Call Forwarding settings are changed on the phone,
                                             the changes are also made on the server. If changes are made on the server, they are propagated to the phone.

Default setting: no

Secure Call Option

Configures a line to only accept secure calls. Select any of the options:

Optional: Retains the current secure call option for the phone adapter.

Strict: Allows SRTP only when SIP transport is set to TLS and if the ATA receives an unsecure call, the call fails. Allows
                                             RTP only when SIP transport is UDP/TCP and if the ATA receives an unsecure call, the call fails.

Default setting: Optional

### E911 Geolocation Configuration

Field

Description

Company UUID

The Universally Unique Identifier (UUID) assigned to the customer by the emergency call services provider.

For example:

19c8168c-a366-44b5-853c-960fcaa19592

Allowed values: Maximum identifier length is 128 characters.

Default setting: Blank

Primary Request URL

URL of the primary location server that provides the emergency call services.

The location server returns an HELD response to the phone with the requested location URI that is tied to the user phone IP
                                             address.

This parameter must be in the form of a valid HTTP or HTTPS URL.

Allowed values: A valid URL not exceeding 255 characters.

Default setting: Blank

Secondary Request URL

URL of the backup server to obtain the user's phone location.

If the primary request URL fails, ATA tries to send the secondary request URL to the emergency call services provider.

This parameter must be in the form of a valid HTTP or HTTPS URL.

Allowed values: A valid URL not exceeding 255 characters.

Default setting: Blank

### Proxy and Registration

Field

Description

Proxy

SIP proxy server for all outbound requests.

Default setting: blank

Outbound Proxy

SIP Outbound Proxy Server where all outbound requests are sent as the first hop.

Default setting: blank

Survivability Proxy

Specifies a DNS A record of the Local Survivability Gateway (LSG) nodes. This allows the ATA to perform a failover to a survivability
                                             gateway.

String syntax:

```
hostname[:port][:p=priority][:w=weight][:A=ip-list]
[| hostname2[:port][:p=priority][:w=weight][:A=ip-list]]
```

```
ip-list: ip-addr[,ip-addr[,ip-addr…]]
```

Default: port=0

```
webex-sgw.example.com:8933:A=10.10.10.10
```

Where,

webex-sgw.example.com=Provisioned LSG hostname. It is used for TLS certificate validation when connecting to LSG nodes.

8933=LSG port

10.10.10.10=Provisioned LSG address

Compared to LSG nodes that have the lowest priority, SSE nodes always have high priority. If there are multiple LSG nodes,
                                             try one after the other.

Default setting: blank

Use Outbound Proxy

Enables the use of an Outbound Proxy. If set to no, the Outbound Proxy and Use OB Proxy in Dialog parameters are ignored.

Default setting: no

Use OB Proxy In Dialog

Whether to force SIP requests to be sent to the outbound proxy within a dialog. Ignored if the parameter Use Outbound Proxy
                                             is no, or the Outbound Proxy parameter is empty.

Default setting: yes

Register

Enable periodic registration with the Proxy parameter. This parameter is ignored if Proxy is not specified.

Default setting: yes

Make Call Without Reg

Allow making outbound calls without successful (dynamic) registration by the unit. If No, dial tone will not play unless registration
                                             is successful.

Default setting: no

Register Expires

Expires value in sec in a REGISTER request. The ATA will periodically renew registration shortly before the current registration
                                             expired. This parameter is ignored if the Register parameter is no. Range: 0 – (231 – 1) sec.

Default setting: 3600

Ans Call Without Reg

Allow answering inbound calls without successful (dynamic) registration by the unit.

Default setting: no

Use DNS SRV

Whether to use DNS SRV lookup for Proxy and Outbound Proxy.

Default setting: no

DNS SRV Auto Prefix

If enabled, the ATA will automatically prepend the Proxy or Outbound Proxy name with _sip._udp when performing a DNS SRV lookup
                                             on that name.

Default setting: no

Proxy Fallback Intvl

After failing over to a lower priority server, the ATA waits for the specified Proxy Fallback Interval, in seconds, before
                                             retrying the highest priority proxy (or outbound proxy) servers. This parameter is useful only if the primary and backup proxy
                                             server list is provided to the ATA via DNS SRV record lookup on the server name.

Using multiple DNS A records per server name does not allow the notion of priority, so all hosts will be considered at the
                                             same priority and the ATA will not attempt to fall back after a failover.

If the value is 0, the SIP proxy fallback feature is disabled.

Range: 0 –65535 sec

Default setting: 3600

Survivability Proxy Fallback Intvl

After ATA is registered to an LSG node, it waits for the specified interval before it attempts to fallback to a Webex Calling
                                             SSE node when any SSE node is reachable.

If there's an active call on the ATA, the call still remains during the fallback process.

Default setting: 30

Proxy Redundancy Method

The method that the ATA uses to create a list of proxies returned in the DNS SRV records. If you select Normal , the list will contain proxiesranked by weight and priority. If you select Based on SRV port, the ATA also inspects the port number based on 1st proxy’s port.

Default setting: Normal

Mailbox Subscribe URL

The URL or IP address of the voicemail server.

Default setting: blank

Mailbox Subscribe Expires

Sets subscription interval for voicemail message waiting indication. When this time period expires, the ATA sends another
                                             subscribe message to the voice mail server.

Default setting: 2147483647

Auto Register When Failover

Controls the fallback duration.

no : the fallback happens immediately and automatically. If the Proxy Fallback Intvl is exceeded, all the new SIP messages go
                                                   to the primary proxy.

yes : the fallback happens only when current registration expires, which means only a REGISTER message can trigger fallback.

For example, when the value for Register Expires is 3600 seconds and Proxy Fallback Intvl is 600 seconds, the fallback is
                                             triggered 3600 seconds later and not 600 seconds later. When the value for Register Expires is 600 seconds and Proxy Fallback
                                             Intvl is 1000 seconds, the fallback is triggered at 1200 seconds. After successfully registering back to primary server, all
                                             the SIP messages go to primary server.

Default setting: yes

### Subscriber Information

Field

Description

Display Name

Display name for caller ID.

Default setting: blank

User ID

User ID for this line.

Default setting: blank

Password

Password for this line.

Default setting: blank

Use Auth ID

To use the authentication ID and password for SIP authentication, select yes . Otherwise, select no to use the user ID and password.

Default setting: no

Auth ID

Authentication ID for SIP authentication.

Default setting: blank

Reserved Auth Realm

The value of an authentication realm, which is used in the www-authenticate/proxy-authenticate header field for the INVITE
                                             and NOTIFY requests.

Default setting: Blank. The proxy IP address is used as the authentication realm.

Resident Online Number

This setting allows you to associate a "local" telephone number with this line using a valid Skype Online Number from Skype.
                                             Calls made to that number will ring your phone. Enter the number without spaces or special characters.

Default setting: blank

SIP URI

The parameter by which the user agent will identify itself for this line. If this field is blank, the actual URI used in the
                                             SIP signaling should be automatically formed as: sip:UserName@Domain

Where UserName is the username given for this line in the User ID, and Domain is the domain given for this profile in the
                                             User Agent Domain.

If the User Agent Domain is an empty string, then the IP address of the phone should be used for the domain.

If the URI field is not empty, but if a SIP or SIPS URI that contains no @ character, then the actual URI used in the SIP
                                             signaling should be automatically formed by appending this parameter with an @ character followed by the IP address of the
                                             device.

### Supplementary Service Subscription

The ATA provides native support of a large set of enhanced or supplementary services. All of these services are optional.
                                 The parameters listed in the following table are used to enable or disable a specific supplementary service. A supplementary
                                 service should be disabled if a) the user has not subscribed for it, or b) the Service Provider intends to support similar
                                 service using other means than relying on the ATA.

Field

Description

Call Waiting Serv

Enable Call Waiting Service.

Default setting: yes

Block CID Serv

Enable Block Caller ID Service.

Default setting: yes

Block ANC Serv

Enable Block Anonymous Calls Service

Default setting: yes

Dist Ring Serv

Enable Distinctive Ringing Service

Default setting: yes

Cfwd All Serv

Enable Call Forward All Service

Default setting: yes

Cfwd Busy Serv

Enable Call Forward Busy Service

Default setting: yes

Cfwd No Ans Serv

Enable Call Forward No Answer Service

Default setting: yes

Cfwd Sel Serv

Enable Call Forward Selective Service. Configure this service in the Selective Call Forward Settings section.

Default setting: yes

Cfwd Last Serv

Enable Forward Last Call Service

Default setting: yes

Block Last Serv

Enable Block Last Call Service

Default setting: yes

Accept Last Serv

Enable Accept Last Call Service

Default setting: yes

DND Serv

Enable Do Not Disturb Service

Default setting: yes

CID–Serv

Enable Caller ID Service

Default setting: yes

CWCID Serv

Enable Call Waiting Caller ID Service

Default setting: yes

Call Return Serv

Enable Call Return Service

Default setting: yes

Call Redial Serv

Enable Call Redial Service.

Default setting: yes

Call Back Serv

Enable Call Back Service.

Default setting: yes

Three Way Call Serv

Enable Three Way Calling Service. Three Way Calling is required for Three Way Conference and Attended Transfer.

Default setting: yes

Three Way Conf Serv

Enable Three Way Conference Service. Three Way Conference is required for Attended Transfer.

Default setting: yes

Attn Transfer Serv

Enable Attended Call Transfer Service. Three Way Conference is required for Attended Transfer.

Default setting: yes

Unattn Transfer Serv

Enable Unattended (Blind) Call Transfer Service.

Default setting: yes

MWI Serv

Enable MWI Service. MWI is available only if a Voice Mail Service is set-up in the deployment.

Default setting: yes

VMWI Serv

Enable VMWI Service (FSK)

Default setting: yes

Speed Dial Serv

Enable Speed Dial Service.

Default setting: yes

Secure Call Serv

Secure Call Service. If this feature is enabled, a user can make a secure call by entering an activation code (*18 by default)
                                             before dialing the target number. Then audio traffic in both directions is encrypted for the duration of the call.

Default setting: yes

Star codes are set in Vertical Service Activation Codes. To enable secure calling by default, without requiring a star code,
                                             set the user’s Secure Call Setting to yes. See User 1 and User 2 .

Referral Serv

Enable Referral Service. See the Referral Services Codes parameter in Vertical Service Activation Codes for more information.

Default setting: yes

Feature Dial Serv

Enable Feature Dial Service. See the Feature Dial Services Codes parameter in Vertical Service Activation Codes for more information.

Default setting: yes

Service Announcement Serv

Enable Service Announcement Service.

Default setting: no

Reuse CID Number As Name

Use the Caller ID number as the caller name.

Default settings: yes

CONFCID Serv

Enable Caller ID during conference call.

Default settings: yes

#### Audio Configuration

Field

Description

Preferred Codec

Preferred codec for all calls. (The actual codec used in a call still depends on the outcome of the codec negotiation protocol.)
                                                Select one of the following:

G711u

G711a

G726-32

G729a

Default setting: G711u.

Second Preferred Codec

If the first codec fails, then second preferred codec is tried.

Default setting: blank

Third Preferred Codec

If the second codec fails, then third preferred codec is tried.

Default setting: blank

Use Pref Codec Only

To use only the preferred codec for all calls, select yes . (The call fails if the far end does not support this codec.) Otherwise, select no .

Default setting: no

Codec Negotiation

When set to Default , the Cisco IP phone responds to an Invite with a 200 OK response advertising the preferred codec only. When set to List All , the Cisco IP phone responds listing all the codecs that the phone supports.

Default setting: Default

G729a Enable

To enable the use of the G.729a codec at 8 kbps, select yes . Otherwise, select no .

Default setting: yes

Silence Supp Enable

To enable silence suppression so that silent audio frames are not transmitted, select yes . Otherwise, select no .

Default setting: no

G726-32 Enable

To enable the use of the G.726 codec at 32 kbps, select yes . Otherwise, select no .

Default setting: yes

Silence Threshold

Select the appropriate setting for the threshold: high , medium , or low .

Default setting: medium

FAX V21 Detect Enable

To enable detection of V21 fax tones, select yes . Otherwise, select no .

Default setting: yes

Echo Canc Enable

To enable the use of the echo canceller, select yes . Otherwise, select no.

Default setting: yes

FAX CNG Detect Enable

To enable detection of the fax Calling Tone (CNG), select yes . Otherwise, select no .

Default setting: yes

FAX Passthru Codec

Select the codec for fax passthrough, G711u or G711a .

Default setting: G711u

FAX Codec Symmetric

To force the ATA to use a symmetric codec during fax passthrough, select yes . Otherwise, select no .

Default setting: yes

DTMF Process INFO

To use the DTMF process info feature, select yes . Otherwise, select no .

Default setting: yes

FAX Passthru Method

Select the fax passthrough method: None , NSE , or ReINVITE .

Default setting: NSE

DTMF Process AVT

To use the DTMF process AVT feature, select yes . Otherwise, select no .

Default setting: yes

FAX Process NSE

To use the fax process NSE feature, select yes . Otherwise, select no .

Default setting: yes

DTMF Tx Method

Select the method to transmit DTMF signals to the far end: InBand , AVT , INFO , or Auto . InBand sends DTMF by using the audio path. AVT sends DTMF as AVT events. INFO uses the SIP INFO method. Auto uses InBand
                                                or AVT based on the outcome of codec negotiation.

Default setting: Auto

FAX Disable ECAN

If enabled, this feature automatically disables the echo canceller when a fax tone is detected. To use this feature, select yes . Otherwise, select no .

Default setting: no

DTMF Tx Mode

DTMF Detection Tx Mode is available for SIP information and AVT.

Options are: Strict or Normal .

Default setting: Strict for which the following are true:

A DTMF digit requires an extra hold time after detection.

The DTMF level threshold is raised to -20 dBm.

The minimum and maximum duration thresholds are:

strict mode for AVT and SIP: the value set in DTMF Tx Strict Hold Off Time

normal mode for AVT: 40 ms

normal mode for SIP: 50 ms

DTMF Tx Strict Hold Off Time

This parameter is in effect only when DTMF Tx Mode is set to strict, and when DTMF Tx Method is not set to inband; that is,
                                                either AVT or INFO. The value can be set as low as 40 ms. There is no maximum limit. A larger value will reduce the chance
                                                of talk-off (beeping) during conversation, at the expense of reduced performance of DTMF detection, which is needed for interactive
                                                voice response systems (IVR).

Default setting: 70 ms

FAX Enable T38

To enable the use of ITU-T T.38 standard for FAX Relay, select yes . Otherwise select no .

no : The ATA can parse only one "m=" line of the SDP packet.

If the ATA receives multiple "m=" lines contained in the SDP packet from a provider, an outbound FAX failure might occur.
                                                      This issue typically occurs when the first "m=" line specifies an invalid port number "0" while the second "m=" line specifies
                                                      a valid port.

To avoid this issue, set FAX Enable T38 to yes and FAX Passthru Method to ReINVITE .

In the aforementioned situation, the ATA can parse the second "m=" line successfully.

yes : The ATA can parse the first two "m=" lines of the SDP packet. It ignores the other "m=" lines.

Default setting: no

Hook Flash Tx Method

Select the method for signaling hook flash events: None , AVT , or INFO . None does not signal hook flash events. AVT uses RFC2833 AVT (event = 16) INFO uses SIP INFO with the single line signal=hf
                                                in the message body. The MIME type for this message body is taken from the Hook Flash MIME Type setting.

Default setting: None

FAX T38 Redundancy

Select the appropriate number to indicate the number of previous packet payloads to repeat with each packet. Choose 0 for no payload redundancy. The higher the number, the larger the packet size and the more bandwidth consumed.

Default setting: 1

FAX T38 ECM Enable

Select yes to enable T.38 Error Correction Mode. Otherwise select no .

Default setting: yes

FAX Tone Detect Mode

This parameter has three possible values:

caller or callee : The ATA will detect FAX tone whether it is callee or caller

caller only : The ATA will detect FAX tone only if it is the caller

callee only : The ATA will detect FAX tone only if it is the callee

Default setting: caller or callee.

Symmetric RTP

Enable symmetric RTP operation. If enabled, the ATA sends RTP packets to the source address and port of the last received
                                                valid inbound RTP packet. If disabled (or before the first RTP packet arrives) the ATA sends RTP to the destination as indicated
                                                in the inbound SDP.

Default setting: no

Fax T38 Return to Voice

When this feature is enabled, upon completion of the fax image transfer, the connection remains established and reverts to
                                                a voice call using the previously designated codec. Select yes to enable this feature, or select no to disable it.

Default setting: no

Modem Line

Enable an alternate method to make the modem call without Modem Line Toggle Code pre-dialing.

Default setting: no

RTP to Proxy in Remote Hold

Enable to send RTP to proxy when line is held by remote side.

Default setting: no

Encryption Method

Encryption algorithm used for the SRTP sessions (for example,  secure calls). Select one of the following:

AES 128

AES 256 GCM

Make sure that the Secure Call Service is enabled, see the parameter Secure Call Serv from the chapter Supplementary Service Subscription .

Default setting: AES 128

### Dial Plan

The default dial plan script for the line is as follows:

(*xx|[3469]11|0|00|[2-9]xxxxxx|1xxx[2-9]xxxxxx|xxxxxxxxxxxx.)

Each parameter is separated by a semi-colon (;)

Example 1:

*1xxxxxxxxxx<:@fwdnat.pulver.com:5082;uid=jsmith;pwd=xy z

Example 2:

*1xxxxxxxxxx<:@fwd.pulver.com;nat;uid=jsmith;pwd=xyz

The syntax for a dial plan expression is described in the table below.

Dial Plan Entry

Functionality

*xx

Allow arbitrary 2 digit star code

[3469]11

Allow x11 sequences

0

Operator

00

Int’l Operator

[2-9]xxxxxx

US local number

1xxx[2-9]xxxxxx

US 1 + 10-digit long distance number

xxxxxxxxxxxx.

Everything else

### FXS Port Polarity Configuration

Field

Description

Idle Polarity

Polarity before a call is connected: Forward or Reverse.

Default setting: Forward

Caller Conn Polarity

Polarity after an outbound call is connected: Forward or Reverse.

Default setting: Forward.

Callee Conn Polarity

Polarity after an inbound call is connected: Forward or Reverse.

Default setting: Forward

## User 1 and User 2

Use the Voice > User 1 and Voice > User2 pages to set the user preferences for the calls through the PHONE 1 and PHONE 2 ports.

Enter the settings as described below. After making changes, click Submit to save your settings, or click Cancel to redisplay the page with the saved settings.

### Call Forward Settings

Field

Description

Cfwd All Dest

Forward number for Call Forward All Service.

Default setting: blank

Cfwd Busy Dest

Forward number for Call Forward Busy Service. Same as Cfwd All Dest.

Default setting: blank

Cfwd No Ans Dest

Forward number for Call Forward No Answer Service. Same as Cfwd All Dest.

Default setting: blank

Cfwd No Ans Delay

Delay in sec before Call Forward No Answer triggers.

Default setting: 20

### Selective Call Forward Settings

Field

Description

Cfwd Sel1-8 Caller

Caller number pattern to trigger Call Forward Selective service. When the caller’s phone number matches the entry, the call
                                             is forwarded to the corresponding Cfwd Selective Destination (Cfwd Sel1-8 Dest).

• Use ? to match any single digit.

• Use * to match any number of digits.

Example: 1408*, 1512???1234

In the above example, a call is forwarded to the corresponding destination if the caller ID either starts with 1408 or is
                                             an 11-digit numbering starting with 1512 and ending with 1234.

Default setting: blank

Cfwd Sel1-8 Dest

The destination for the corresponding Call Forward Selective caller pattern (Cfwd Sel1-8 Caller).

Default setting: blank

Cfwd Last Caller

The number of the last caller; this caller is actively forwarded to the Cfwd Last Dest via the Call Forward Last service.
                                             For more information, see Vertical Service Activation Codes .

Default setting: blank

Cfwd Last Dest

The destination for the Cfwd Last Caller.

Block Last Caller

The number of the last caller; this caller is blocked via the Block Last Caller Service. For more information, see Vertical Service Activation Codes .

Default setting: blank

Accept Last Caller

The number of the last caller; this caller is accepted via the Accept Last Caller Service. For more information, see Vertical Service Activation Codes .

Default setting: blank

### Speed Dial Settings

Field

Description

Speed Dial 2-9

Target phone number (or URL) assigned to speed dial 2, 3, 4, 5, 6, 7, 8, or 9.

Default setting: blank

### Supplementary Service Settings

Field

Description

CW Setting

Call Waiting on/off for all calls.

Default setting: yes

Block CID

Setting Block Caller ID on/off for all calls.

Default setting: no

Block ANC

Setting Block Anonymous Calls on or off.

Default setting: no

DND

Setting DND on or off.

Default setting: no

CID Setting

Caller ID Generation on or off.

Default setting: yes

CWCID Setting

Call Waiting Caller ID Generation on or off.

Default setting: yes

Dist Ring

Setting Distinctive Ring on or off.

Default setting: yes

Secure Call Setting

If yes, all outbound calls are secure calls by default, without requiring the user to dial a star code first.

Default setting: no

If Secure Call Setting is set to yes , all outbound calls are secure. However, a user can disable security for a call by dialing *19 before dialing the target
                                                   number.

If Secure Call Setting is set to No , the user can make a secure outbound call by dialing *18 before dialing the target number.

A user cannot force inbound calls to be secure or not secure; that depends on whether the caller has security enabled or not.

This setting is applicable only if Secure Call Serv is set to yes on the line interface. See Line 1 and Line 2 Settings (PHONE 1 and PHONE 2) .

Message Waiting

Setting this value to yes can activate stutter tone and VMWI signal. This parameter is stored in long term memory and will
                                             survive after reboot or power cycle.

Default setting: no

Accept Media Loopback Request

Controls how to handle incoming requests for loopback operation.

never —Never accepts loopback calls; replies 486 to the caller.

automatic —Automatically accepts the call without ringing.

manual —Rings the phone first, and the call must be picked up manually before loopback starts.

Default setting: Automatic

Media Loopback Mode

The loopback mode to assume locally when making call to request media loopback. Choices are: Source and Mirror .

Default setting: source

If the ATA answers the call, the mode is determined by the caller.

Media Loopback Type

The loopback type to use when making call to request media loopback operation. Choices are Media and Packet .

Default setting: media

Note that if the ATA answers the call, then the loopback type is determined by the caller (the ATA always picks the first
                                             loopback type in the offer if it contains multiple type)

CONFCID Setting

Enables or disables the CONFCID.

Default setting: yes

### Distinctive Ring Settings

Field

Description

Ring1 - 8 Caller

Caller number pattern to play Distinctive Ring/CWT 1, 2, 3, 4, 5, 6, 7, or 8. Caller number patterns are matched from Ring
                                             1 to Ring 8. The first match (not the closest match) will be used for alerting the subscriber. The distinctive rings are set
                                             on the Regional page. See Regional .

Default setting: blank

### Ring Settings

Field

Description

Default Ring

Default ringing pattern, 1–8, for all callers.

Default setting: 1

Default CWT

Default CWT pattern, 1–8, for all callers.

Default setting: 1

Hold Reminder Ring

Ring pattern for reminder of a holding call when the phone is on-hook.

Default setting: 8

Call Back Ring

Ring pattern for call back notification.

Default setting: 7

Cfwd Ring Splash Len

Duration of ring splash when a call is forwarded (0 – 10.0s)

Default setting: 0

Cblk Ring Splash Len

Duration of ring splash when a call is blocked (0 – 10.0s)

Default setting: 0

VMWI Ring Policy

The parameter controls when a ring splash is played when a the VM server sends a SIP NOTIFY message to the ATA indicating
                                             the status of the subscriber’s mail box. Three settings are available.

Default setting: New VM Available

New VM Available —Ring as long as there new voicemail messages.

New VM Becomes Available —Ring at the point when the first new voicemail message is received.

New VM Arrives —Ring when the number of new voicemail messages increases.

VMWI Ring Splash Len

Duration of ring splash when new messages arrive before the VMWI signal is applied (0 – 10.0s)

Default setting: 0

Ring On No New VM

If enabled, the ATA plays a ring splash when the voicemail server sends SIP NOTIFY message to the ATA indicating that there
                                             are no more unread voice mails. Some equipment requires a short ring to precede the FSK signal to turn off VMWI lamp.

Default setting: no

| Field | Description |
|---|---|
| Product Name | The product name of ATA. |
| Serial Number | The serial number of ATA. |
| Software Version | The software version of ATA. |
| Hardware Version | The hardware version of ATA. |
| MAC Address | The mac address of ATA. |
| Client Certificate | The client certificate of ATA. |
| Customization | The customization of ATA. |

| Field | Description |
|---|---|
| Current Time | Current date and time of the system; for example, 10/3/2003 16:43:00. Set the system time by using the Network Setup > Time Settings page. |
| Elapsed Time | Total time elapsed since the last reboot of the system; for example, 25 days and 18:12:36. |
| RTP Packets Sent | Total number of RTP packets sent, including redundant packets. |
| RTP Bytes Sent | Total number of RTP bytes sent. |
| RTP Packets Recv | Total number of RTP packets received, including redundant packets. |
| RTP Bytes Recv | Total number of RTP bytes received. |
| SIP Messages Sent | Total number of SIP messages sent, including retransmissions. |
| SIP Bytes Sent | Total number of bytes of SIP messages sent, including retransmissions. |
| SIP Messages Recv | Total number of SIP messages received, including retransmissions. |
| SIP Bytes Recv | Total number of bytes of SIP messages received, including retransmissions. |
| External IP | The External IP address used for NAT mapping. |

| Note | In a configuration profile, the FXS parameters must include an appropriate numeral for identifying the port receiving the
                                          setting. |
|---|---|

| Field | Description |
|---|---|
| Custom CA Provisioning Status | The status of the latest custom CA (Certificate Authority) certificate download. |
| Custom CA Info | The successfully downloaded CA information, or “Not Installed” if no custom CA certificate was installed. Default setting: Not Installed |

| Field | Description |
|---|---|
| Provisioning Profile | Profile rule setting Default setting: Empty |
| Provision Status | Indicate the status of last provisioning Default setting: Empty |
| Provisioning Failure Reason | Reason for failure Default setting: Empty |

| Field | Description |
|---|---|
| MIC Cert Provisioning Status | The download status of the latest renewed MIC certificate from the SUDI renewal service. If the certificate download is successful,
                                             the status is Download Successful . Otherwise, you might receive one of the following error messages: Downlaod Failed: Dns query failed Downlaod Failed: Bad scheme Downlaod Failed: resource exhausted Downlaod Failed:Connection error Downlaod Failed:File not found Downlaod Failed: Access violation Downlaod Failed: Disk full Downlaod Failed: Bad operation Downlaod Failed: Bad option Downlaod Failed: internal server error Downlaod Failed: Not Implemented Downlaod Failed: Bad Gateway Downlaod Failed: Service Unavailable Downlaod Failed: Zero file size Downlaod Failed: file size exceed Downlaod Failed: corrupted file Downlaod Failed: Unknown, error code(**) If the system detects that the ATA doesn't need to renew the MIC certificate, the status is still empty. Default: Empty |
| MIC CA Info | Common name of the Certificate Authority (CA) that issues the MIC certificate. It can be one of the following: Cisco Manufacturing CA Cisco Manufacturing CA II Cisco Manufacturing CA III For a successful MIC certificate renewal, the common name is Cisco Manufacturing CA III . For a failed MIC certificate renewal, the common name can be Cisco Manufacturing CA or Cisco Manufacturing CA II . Default: Empty |

| Field | Description |
|---|---|
| Restricted Access Domains | Domain that Cisco IP phones responds to SIP messages only from the identified servers. Applicable to Line 1. |
| IVR Admin Passwd | Password for the administrator to manage the ATA by using the built-in IVR through a connected phone. |
| Network Startup Delay | The number of seconds of delay between restarting the voice module and initializing network interface. Default setting: 3 |

| Field | Description |
|---|---|
| DNS Query TTL Ignore | In DNS packages, the server suggests a TTL value to the client. If this parameter is set to Yes, the value from the server
                                          is ignored. Default setting: No |
| Survivability Test Mode | Determines whether the ATA will always register to the Local Survivability Gateway (LSG) nodes even though the Webex Calling
                                          Session Signaling Engine (SSE) nodes are reachable. This mode is used to test whether the LSG nodes can work normally. Default setting: No |

| Field | Description |
|---|---|
| FIPS Mode | Determine whether to enable or disable the Federal Information Processing Standards (FIPS) 140-3 cryptographic module on the
                                          ATA. If enabled, the product is in compliance with the standard. FIPS standards are designed to ensure the security and interoperability of information systems used by the federal government
                                          and its contractors. Click Enabled to enable this feature, or click Disabled to disable it. When you failed to enable the FIPS mode, the LED on the Problem Report Tool (PRT) button lights up in solid amber. Press the PRT button to clear the warning and turn off the PRT LED. Note When the FIPS mode is enabled, TR-069 may not function. When the FIPS mode is enabled, the following features can work seamlessly on the ATA: Image authentication Secure Storage TLS (HTTPs, PRT upload, Firmware upgrade, Profile resync, Onboard service, SIP over TLS) SIP Digest (RFC 8760) SRTP SNMPV3 Default setting: Disabled | Note | When the FIPS mode is enabled, TR-069 may not function. |
| Note | When the FIPS mode is enabled, TR-069 may not function. |
| TLS Min Version | Select the minimum protocol version required for the TLS connections. If the TLS version on the remote side is older than the selected TLS version on the ATA, the TLS connection will be rejected.
                                          See the table TLS Minimum Version Results for details. Available options: TLS 1.0, TLS 1.1, TLS 1.2, and TLS 1.3. Default setting: TLS 1.1 |

| Note | When the FIPS mode is enabled, TR-069 may not function. |
|---|---|

| Client TLS Min Version | Server Highest TLS Version | Results |
|---|---|---|
| TLS 1.0 | TLS 1.0 | TLS 1.0 |
| TLS 1.1 | TLS 1.1 |
| TLS 1.2 | TLS 1.2 |
| TLS 1.3 | TLS 1.3 |
| TLS 1.1 | TLS 1.0 | Protocol alert |
| TLS 1.1 | TLS 1.1 |
| TLS 1.2 | TLS 1.2 |
| TLS 1.3 | TLS 1.3 |
| TLS 1.2 | TLS 1.0 | Protocol alert |
| TLS 1.1 | Protocol alert |
| TLS 1.2 | TLS 1.2 |
| TLS 1.3 | TLS 1.3 |
| TLS 1.3 | TLS 1.0 | Protocol alert |
| TLS 1.1 | Protocol alert |
| TLS 1.2 | Protocol alert |
| TLS 1.3 | TLS 1.3 |

| Note | For a deeper understanding of these fields, refer to Request for Comments (RFC) 3261. |
|---|---|

| Field | Description |
|---|---|
| Max Forward: | The maximum times a call can be forwarded. The valid range is from 1 to 255. Default setting: 70 |
| Max Redirection: | Number of times an invite can be redirected to avoid an infinite loop. Default setting: 5. |
| Max Auth: | The maximum number of times (from 0 to 255) a request may be challenged. Default setting: 2 |
| SIP User Agent Name: | The User-Agent header used in outbound requests. If empty, the header is not included. Macro expansion of $A to $D corresponding
                                             to GPP_A to GPP_D allowed. Default setting: $VERSION |
| SIP Server Name: | The server header used in responses to inbound responses. Default setting: $VERSION |
| SIP Reg User Agent Name: | The User-Agent name to be used in a REGISTER request. If this value is not specified, the SIP User Agent Name parameter is
                                             also used for the REGISTER request. Default setting: Blank |
| SIP Reg Starting Sequence Number: | Defines the SIP Reg message Sequence Number. Default setting: Blank |
| SIP Accept Language: | Accept-Language header used. There is no default; this indicates that the ATA does not include this header. If empty, the
                                             header is not included. Default setting: Blank |
| DTMF Relay MIME Type: | The MIME Type used in a SIP INFO message to signal a DTMF event. Default setting: Application/dtmf-relay. |
| Hook Flash MIME Type: | The MIME Type used in a SIP INFO message to signal a hook flash event. Default setting: Application/hook-flash. |
| Remove Last Reg: | Determines whether the ATA removes the last registration before submitting a new one, if the value is different. Select yes
                                             to remove the last registration, or select no to omit this step. Default setting: No |
| Use Compact Header: | Determines if the ATA uses compact SIP headers in outbound SIP messages. Select Yes to use compact SIP headers in outbound SIP messages. Select No to use normal SIP headers. If inbound SIP requests contain compact headers, the ATA reuses the same headers when generating the response regardless of
                                             the Use Compact Header parameter. If inbound SIP requests contain normal headers, the ATA substitutes those headers with compact
                                             headers as defined by RFC 261 when Use Compact Header is set to Yes. Default setting: No |
| Escape Display Name: | Determines if the Display Name is private. Select Yes if you want the ATA to enclose the string configured in the Display Name in a pair of double quotes for out bound SIP messages.
                                             If the display name includes " or \, these will be escaped to \" and \\ within the double quotes. Otherwise, select No . Default setting: No |
| RFC 2543 Call Hold: | Configures the type of call hold: a:sendonly or 0.0.0.0. Do not use the 0.0.0.0 syntax in a HOLD SDP; use the a:sendonly syntax. Default setting: Yes |
| Mark All AVT Packets: | Select Yes if you want all AVT tone packets encoded for redundancy to have the marker bit set for each DTMF event. Select No to have the marker bit set only for the first packet. Default setting: Yes |
| AVT Packet Size: | Indicates the AVT Packet size according to value set in ptime or fixed 10ms. Default setting: ptime |
| SIP TCP Port Min: | The lowest TCP port number that can be used for SIP sessions. Default setting: 5060 |
| SIP TCP Port Max: | The highest TCP port number that can be used for SIP sessions. Default setting: 5080 |
| CTI Enable: | Enables or disables the Computer Telephone Interface feature provided by some servers. Default setting: no |
| Keep Referee When REFER Failed: | Set this parameter to Yes to configure the phone to handle NOTIFY sipfrag messages. You can also configure this parameter in the configuration file: <Keep_Referee_When_REFER_Failed ua="na">Yes </Keep_Referee_When_REFER_Failed> |
| Caller ID Header: | Provides the option to take the caller ID from PAID-RPID-FROM,P-ASSERTEDIDENTITY, REMOTE-PARTY-ID, or FROM header. Default setting: PAID-RPID-FROM |

| Field | Description |
|---|---|
| SIP T1 | RFC 3261 T1 value (round-trip time estimate), which can range from 0 to 64 seconds. Default setting: 0.5 |
| SIP T2 | RFC 3261 T2 value (maximum retransmit interval for non-INVITE requests and INVITE responses), which can range from 0 to 64
                                          seconds. Default setting: 4 |
| SIP T4 | RFC 3261 T4 value (maximum duration a message remains in the network), which can range from 0 to 64 seconds. Default setting: 5 |
| SIP Timer B | INVITE time-out value, which can range from 0 to 64 seconds. Default setting: 32 |
| SIP Timer F | Non-INVITE time-out value, which can range from 0 to 64 seconds. Default setting: 16 |
| SIP Timer H | H INVITE final response, time-out value, which can range from 0 to 64 seconds. Default setting: 32 |
| SIP Timer D | ACK hang-around time, which can range from 0 to 64 seconds. Default setting: 32 |
| SIP Timer J | Non-INVITE response hang-around time, which can range from 0 to 64 seconds. Default setting: 32 |
| INVITE Expires | INVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Range: 0–(2 31 –1) Default setting: 240 |
| ReINVITE Expires | ReINVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Range: 0–(2 31 –1) Default setting: 30 |
| Reg Min Expires | Minimum registration expiration time allowed from the proxy in the Expires header or as a Contact header parameter. If the
                                          proxy returns a value less than this setting, the minimum value is used. Default setting: 1 |
| Reg Max Expires | Maximum registration expiration time allowed from the proxy in the Min-Expires header. If the value is larger than this setting,
                                          the maximum value is used. Default setting: 7200 |
| Reg Retry Intvl | Interval to wait before the ATA retries registration after failing during the last registration. Default setting: 30 |
| Reg Retry Long Intvl | When registration fails with a SIP response code that does not match Retry Reg RSC, the ATA waits for the specified length
                                          of time before retrying. If this interval is 0, the ATA stops trying. This value must be larger than the Reg Retry Intvl value,
                                          which cannot be 0. Default setting: 1200 |
| Reg Retry Random Delay | Random delay range (in seconds) to add to Register Retry Intvl when retrying REGISTER after a failure. Default setting: 0 (disabled) |
| Reg Retry Long Random Delay | Random delay range (in seconds) to add to Register Retry Long Intvl when retrying REGISTER after a failure. Default setting: 0 (disabled) |
| Reg Retry Intvl Cap | The maximum value to cap the exponential back-off retry delay (which starts at Register Retry Intvl and doubles on every REGISTER
                                          retry after a failure). The retry interval is always at Register Retry Intvl seconds after a failure. If this feature is enabled,
                                          Reg Retry Random Delay is added on top of the exponential back-off adjusted delay value. Default setting: 0, which disables the exponential backoff feature. |

| Field | Description |
|---|---|
| SIT1 RSC | SIP response status code for the appropriate Special Information Tone (SIT). Reorder or Busy tone is played by default for
                                          all unsuccessful response status code for SIT 1 RSC through SIT 4 RSC. Default setting: blank |
| SIT2 RSC | SIP response status code to INVITE on which to play the SIT2 Tone. Default setting: blank |
| SIT3 RSC | SIP response status code to INVITE on which to play the SIT3 Tone. Default setting: blank |
| SIT4 RSC | SIP response status code to INVITE on which to play the SIT4 Tone. Default setting: blank |
| Try Backup RSC | SIP response code that retries a backup server for the current request. Default setting: blank |
| Retry Reg RSC | Interval to wait before the ATA retries registration after failing during the last registration. Default setting: blank |

| Field | Description |
|---|---|
| RTP Port Min | Minimum port number for RTP transmission and reception. The RTP Port Min and RTP Port Max parameters should define a range that contains at least 4 even number ports, such as 100
                                          to 106. Default setting: 16384. |
| RTP Port Max | Maximum port number for RTP transmission and reception. Default setting: 16482. |
| RTP Packet Size | Packet size in seconds, which can range from 0.01 to 0.16. Valid values must be a multiple of 0.01 seconds. Default setting: 0.030 |
| RTP Tx Packet Size Follows Remote SDP | Enable the Remote pair RTP Packet Size. Default setting: Yes |
| Max RTP ICMP Err | Number of successive ICMP errors allowed when transmitting RTP packets to the peer before the ATA terminates the call. If
                                          value is set to 0, the ATA ignores the limit on ICMP errors. Default setting: 0 |
| RTCP Tx Interval | Interval for sending out RTCP sender reports on an active connection. It can range from 0 to 255 seconds. During an active
                                          connection, the ATA can be programmed to send out compound RTCP packet on the connection. Each compound RTP packet except
                                          the last one contains a SR (Sender Report) and a SDES (Source Description). The last RTCP packet contains an extra BYE packet.
                                          Each SR except the last one contains exactly 1 RR (Receiver Report); the last SR carries no RR. The SDES contains CNAME, NAME,
                                          and TOOL identifiers. The CNAME is set to <User ID>@<Proxy>, NAME is set to <Display Name> (or Anonymous if user blocks caller
                                          ID), and TOOL is set to the Vendor/Hardware-platform-software-version. The NTP timestamp used in the SR is a snapshot of the
                                          local time for the ATA, not the time reported by an NTP server. If the ATA receives a RR from the peer, it attempts to compute
                                          the round-trip delay and show it as the Call Round Trip Delay value (ms) on the Information page. Default setting: 0 |
| No UDP Checksum | Select yes if you want the ATA to calculate the UDP header checksum for SIP messages. Otherwise, select no. Default setting: no |
| Stats In BYE | Determines whether the ATA includes the P-RTP-Stat header or response in a BYE message. The header contains the RTP statistics
                                          of the current call. Select yes or no from the drop-down list. Default setting: yes The format of the P-RTP-Stat header is: P-RTP-State: PS=<packets sent>,OS=<octets sent>,PR=<packets received>,OR=<octets received>,PL=<packets lost>,JI=<jitter in
                                          ms>,LA=<delay in ms>,DU=<call duration ins>,EN=<encoder>,DE=<decoder>. |
| Call Statistics | Specifies whether the phone sends end-of-call statistics within SIP messages when a call terminates or is put on hold. You can select Yes to enable the phone to send end-of-call statistics in Session Initiation Protocol (SIP) messages (BYE and re-INVITE messages).
                                          The phone sends call statistics to the other party of the call when the call terminates or when the call is on hold. The statistics
                                          include: Real-time Transport Protocol (RTP) packets sent or received Total bytes sent or received Total number of lost packets Delay jitter Round-trip delay Call duration The call statistics are sent as headers in SIP BYE messages and SIP BYE response messages (200 OK and re-INVITE during hold).
                                          For audio sessions, the headers are RTP-RxStat and RTP-TxStat. Rtp-Rxstat -> Data received Rtp-Txstat -> Data transmitted Example of call statistics in a SIP BYE message: From: xxxx User-Agent: xxxx Call-ID: xxxx Rtp - Rxstat :Dur=13,Pkt=408,Oct=97680,LatePkt=8,LostPkt=0,AvgJit=0,VQMetrics="CCR=0.0017;ICR=0.0000;ICRmx=0.0077;CS=2; SCS=0;VoRxCodec=PCMU;CID=4;VoPktSizeMs=30;VoPktLost=0;VoPktDis=1;VoOneWayDelayMs=281;maxJitter=12;MOScq=4.21;MOSlq=3.52;network=ethernet;hwType=CP-8865;rtpBitrate=60110;rtcpBitrate=0“ Rtp-Txstat : Dur=13,Pkt=417,Oct=100080,tvqMetrics="TxCodec=PCMU;rtpbitrate=61587;rtcpbitrate=0" You can also use the Call_Statistics parameter in the phone configuration file to enable this feature. <Call_Statistics ua="na">Yes</Call_Statistics> Default: Yes Options: Yes and No |

| Field | Description |
|---|---|
| NSE Dynamic Payload | NSE dynamic payload type. The valid range is 96-127. Default setting: 100 |
| AVT Dynamic Payload | AVT dynamic payload type. The valid range is 96-127. Default setting: 101 |
| INFOREQ Dynamic Payload | INFOREQ dynamic payload type. Default setting: blank |
| G726r32 Dynamic Payload | G726r32 dynamic payload type. Default setting: 2 |
| G729b Dynamic Payload | G.729b dynamic payload type. The valid range is 96-127. Default setting: 99 |
| EncapRTP Dynamic Payload | EncapRTP Dynamic Payload type. Default setting: 112 |
| RTP-Start-Loopback Dynamic Payload | RTP-Start-Loopback Dynamic Payload type. Default setting: 113 |
| RTP-Start-Loopback Codec | RTP-Start-Loopback Codec. Select one of the following: G711u, G711a, G726-32, G729a. Default setting: G711u |
| NSE Codec Name | NSE codec name used in SDP. Default setting: NSE |
| AVT Codec Name | AVT codec name used in SDP. Default setting: telephone-event |
| G711u Codec Name | G.711u codec name used in SDP. Default setting: PCMU |
| G711a Codec Name | G.711a codec name used in SDP. Default setting: PCMA |
| G726r32 Codec Name | G.726-32 codec name used in SDP. Default setting: G726-32 |
| G729a Codec Name | G.729a codec name used in SDP. Default setting: G729a |
| G729b Codec Name | G.729b codec name used in SDP. Default setting: G729ab |
| EncapRTP Codec Name | EncapRTP codec name used in SDP. Default setting: encaprtp |

| Field | Description |
|---|---|
| Handle VIA received. | If you select Yes , the ATA processes the received parameter in the VIA header. The server inserts this value in a response to any one of its
                                          requests. If you select No , the parameter is ignored. Default setting: No |
| Handle VIA rport. | If you select Yes , the ATA processes the rport parameter in the VIA header. This value is inserted by the server in a response to any one of
                                          its requests. If you select No , the parameter is ignored. Default setting: No |
| Insert VIA received. | Inserts the received parameter into the VIA header of SIP responses if the received-from IP and VIA sent-by IP values differ. Select Yes or No from the drop-down menu. Default setting: No |
| Insert VIA rport. | Inserts the parameter into the VIA header of SIP responses if the received-from IP and VIA sent-by IP values differ. Select Yes or No from the drop-down menu. Default setting: No |
| Substitute VIA Addr | Lets you use NAT-mapped IP:port values in the VIA header. Select yes or no from the drop-down menu. Default setting: No |
| Send Resp To Src Port | Sends responses to the request source port instead of the VIA sent-by port. Select Yes or No from the drop-down menu. Default setting: No |
| STUN Enable | Enables the use of STUN to discover NAT mapping. Select Yes or No from the drop-down menu. Default setting: No |
| STUN Test Enable | If the STUN Enable feature is enabled and a valid STUN server is available, the ATA can perform a NAT-type discovery operation
                                          when it powers on. It contacts the configured STUN server, and the result of the discovery is reported in a Warning header
                                          in all subsequent REGISTER requests. If the ATA detects symmetric NAT or a symmetric firewall, NAT mapping is disabled. Default setting: No |
| STUN Server | IP address or fully-qualified domain name of the STUN server to contact for NAT mapping discovery. Default setting: blank |
| EXT IP | External IP address to substitute for the actual IP address of the ATA in all outgoing SIP messages. If 0.0.0.0 is specified,
                                          no IP address substitution is performed. If this parameter is specified, the ATA assumes this IP address when generating SIP messages and SDP. However, the results
                                          of STUN and VIA received parameter processing supersede this statically configured value. This option requires that you have (1) a static IP address from your Internet Service Provider and (2) an edge device with
                                          a symmetric NAT mechanism. If the ATA is the edge device, the second requirement is met. Default setting: blank |
| EXT RTP Port Min | External port mapping number of the RTP Port Min. number. If this number is not zero, the RTP port number in all outgoing
                                          SIP messages is substituted for the corresponding port value in the external RTP port range. Default setting: blank |
| NAT Keep Alive Intvl | Interval between NAT-mapping keep alive messages. Default setting: 15 |
| Redirect Keep Alive | Enables or disables NAT Redirect keep alive messages. Default setting: No |

| Field | Description |
|---|---|
| Provision Enable: | Controls all resync actions independently of firmware upgrade actions. Set to yes to enable remote provisioning. Default setting: Yes |
| Resync On Reset: | Triggers a resync after every reboot except for reboots caused by parameter updates and firmware upgrades. Default setting: Yes |
| Resync Random Delay: | The maximum value for a random time interval that the ATA waits before making its initial contact with the provisioning server.
                                             This delay is effective only on the initial configuration attempt following power-on or reset. The delay is a pseudo-random
                                             number between zero and this value. This parameter is in units of 20 seconds; the default value of 2 represents 40 seconds. This feature is disabled when this
                                             parameter is set to zero. This feature can be used to prevent an overload of the provisioning server when many devices power-on simultaneously. Default setting: 2 (40 seconds) |
| Resync At (HHmm): | The time of day when the device tries to resync. The resync is performed each day. Used with the Resync At Random Delay. Default setting: blank |
| Resync At Random Delay: | Used with the Resync At (HHmm) setting, this parameter sets a range of possible values for the resync delay. The system randomly
                                             chooses a value from this range and waits the specified number of seconds before attempting to resync. This feature is intended
                                             to prevent the network jam that would occur if all resynchronizing devices began the resync at the exact same time of day. Default setting: 600 |
| Resync Periodic: | The time interval between periodic resyncs with the provisioning server. The associated resync timer is active only after
                                             the first successful synchronization with the server. Setting this parameter to zero disables periodic resynchronization. Default setting: 3600 |
| Resync Error Retry Delay: | Resync retry interval (in seconds) applied if there is a resync failure. The ATA has an error retry timer that activates if
                                             the previous attempt to sync with the provisioning server fails. The ATA waits to contact the server again until the timer
                                             counts down to zero. This parameter is the value that is initially loaded into the error retry timer. If this parameter is set to zero, the ATA
                                             immediately retries to sync with the provisioning server following a failed attempt. Default setting: 3600 |
| Forced Resync Delay: | Maximum delay (in seconds) that the ATA waits before performing a resync. The ATA does not resync while one of its lines is
                                             active. Because a resync can take several seconds, it is desirable to wait until the ATA has been idle for an extended period
                                             before resynchronizing. It allows you to make calls in succession without interruption. The ATA has a timer that begins counting down when all lines become idle. This parameter is the initial value of the counter. Resync events are delayed until this counter decrements to zero. Default setting: 14400 |
| Resync From SIP: | Enables a resync to be triggered with a SIP NOTIFY message. Default setting: yes |
| Resync After Upgrade Attempt: | Triggers a resync after every firmware upgrade attempt. Default setting: yes |
| Resync Trigger 1: Resync Trigger 2: | Configurable resync trigger conditions. A resync is triggered when the logic equation in these parameters evaluates to TRUE. Default setting: blank |
| Resync Fails On FNF: | Determines whether a file-not-found response from the provisioning server constitutes a successful or a failed resync. A failed
                                             resync activates the error resync timer. Default setting: yes |
| Profile Rule: | This parameter is a profile script that evaluates to the provisioning resync command. The command is a TCP/IP operation and
                                             an associated URL. The TCP/IP operation can be TFTP, HTTP, or HTTPS. If the command is not specified, TFTP is assumed, and the address of the TFTP server is obtained through DHCP option 66. In
                                             the URL, either the IP address or the FQDN of the server can be specified. The filename can have macros, such as $MA, which
                                             expands to the ATA MAC address. Default setting: /spa$PSN.cfg |
| Profile Rule B: Profile Rule C: Profile Rule D: | Defines second, third, and fourth resync commands and associated profile URLs. These profile scripts are executed sequentially
                                             after the primary Profile Rule resync operation has completed. If a resync is triggered and Profile Rule is blank, Profile
                                             Rules B, C, and D are still evaluated and executed. Default setting: blank |
| DHCP Option To Use: | DHCP Options, delimited by commas, retrieves firmware and profiles. Default setting: 66.160.159.150 |
| Transport Protocol: | Transport Protocol retrieves firmware and profiles. If none is selected, TFTP is assumed and the IP address of the TFTP server
                                             is obtained from the DHCP server. Default setting: https |
| Log Resync Request Msg: | This parameter contains the message that is sent to the Syslog server at the start of a resync attempt. Default setting: $PN $MAC -- Requesting resync $SCHEME://$SERVIP:$PORT$PATH |
| Log Resync Success Msg: | Syslog message issued upon successful completion of a resync attempt. Default setting: $PN $MAC -- Successful resync $SCHEME://$SERVIP:$PORT$PATH |
| Log Resync Failure Msg: | Syslog message issued after a failed resync attempt. Default setting: $PN $MAC -- Resync failed: $ERR |
| Report Rule: | The target URL to which configuration reports are sent. This parameter has the same syntax as the Profile_Rule parameter,
                                             and resolves to a TCP/IP command with an associated URL. A configuration report is generated in response to an authenticated SIP NOTIFY message, with Event: report. The report is
                                             an XML file containing the name and value of all the device parameters. This parameter may optionally contain an encryption key. For example: [ --key $K ] tftp://ps.callhome.net/$MA/rep.xml.enc Default setting: blank |

| Field | Description |
|---|---|
| Upgrade Enable. | Determines if the firmware upgrade operations occur independently of resync actions. Default setting: yes |
| Upgrade Error Retry Delay. | The upgrade retry interval (in seconds) applied if there is an upgrade failure. The ATA has a firmware upgrade error timer
                                          that activates after a failed firmware upgrade attempt. The timer is initialized with the value in this parameter. The next
                                          firmware upgrade attempt occurs when this timer counts down to zero. Default setting: 3600 |
| Downgrade Rev Limit. | Enforces a lower limit on the acceptable version number during a firmware upgrade or downgrade. The ATA does not complete
                                          a firmware upgrade operation unless the firmware version is greater than or equal to this parameter. Default setting: blank |
| Upgrade Rule. | This parameter is a firmware upgrade script with the same syntax as Profile_Rule. Defines upgrade conditions and associated
                                          firmware URLs. Default setting: blank |
| Log Upgrade Request Msg. | Syslog message issued at the start of a firmware upgrade attempt. Default setting: $PN $MAC -- Requesting upgrade $SCHEME://$SERVIP:$PORT$PATH |
| Log Upgrade Success Msg. | Syslog message issued after a firmware upgrade attempt completes successfully. Default setting: $PN $MAC -- Successful upgrade $SCHEME://$SERVIP:$PORT$PATH -- $ERR |
| Log Upgrade Failure Msg. | Syslog message issued after a failed firmware upgrade attempt. Default setting: $PN $MAC -- Upgrade failed: $ERR |

| Field | Description |
|---|---|
| Custom CA URL | The URL of a file location for a custom Certificate Authority (CA) certificate. Either the IP address or the FQDN of the server
                                          can be specified. The file name can have macros, such as $MA, which expands to the ATA MAC address. Default setting: blank |

| Field | Description |
|---|---|
| GPP A to GPP P | General purpose provisioning parameters. These parameters can be used as variables in provisioning and upgrade rules. They
                                          are referenced by prepending the variable name with a ‘$’ character, such as $GPP_A. Default setting: blank |

| Field | Description |
|---|---|
| MIC Cert Refresh Enable | Controls whether to enable the Manufacture Installed Certificate (MIC) renewal by the default or a specified Secure Unique
                                             Device Identifier (SUDI) service. Default setting: no |
| MIC Cert Refresh Rule | Enters an HTTP URL of the SUDI service that provides the renewed MIC certificate. You can use the default URL or specify another valid URL of a SUDI renewal service. Default setting: http://sudirenewal.cisco.com/ |

| Field | Description |
|---|---|
| Dial Tone | Prompts you to enter a phone number. Reorder Tone is played automatically when Dial Tone or any of its alternatives times
                                             out. Default setting: 350@-19,440@-19;10(*/0/1+2) |
| Second Dial Tone | Alternative to the Dial Tone when you dial a three-way call. Default setting: 420@-19,520@-19;10(*/0/1+2) |
| Outside Dial Tone | Alternative to the Dial Tone. It prompts you to enter an external phone number, as opposed to an internal extension. A comma
                                             character in the dial plan triggers it. Default setting: 420@-16;10(*/0/1) |
| Prompt Tone | Prompts you to enter a call forwarding phone number. Default setting: 520@-19,620@-19;10(*/0/1+2) |
| Busy Tone | Played when a 486 RSC is received for an outbound call. Default setting: 480@-19,620@-19;10(.5/.5/1+2) |
| Reorder Tone | Played when an outbound call has failed, or after the far end hangs up during an established call. Reorder Tone is played
                                             automatically when Dial Tone or any of its alternatives times out. Default setting: 480@-19,620@-19;10(.25/.25/1+2) |
| Off Hook Warning Tone | Played when the caller has not properly placed the handset on the cradle. Off Hook Warning Tone is played when the Reorder
                                             Tone times out. Default setting: 480@-10,620@0;10(.125/.125/1+2) |
| Ring Back Tone | Played during an outbound call when the far end is ringing. Default setting: 440@-19,480@-19;*(2/4/1+2) |
| Ring Back 2 Tone | Your ATA plays this tone instead of Ring Back Tone if the called party replies with a SIP 182 response without SDP to its
                                             outbound INVITE request. Default setting: the same as Ring Back Tone, except the cadence is 1s on and 1s off. Default setting: 440@-19,480@-19;*(1/1/1+2) |
| Confirm Tone | Brief tone to notify you that the last input value has been accepted. Default setting: 600@-16;1(.25/.25/1) |
| SIT1 Tone | Alternative to the Reorder Tone played when an error occurs as a caller makes an outbound call. The RSC to trigger this tone
                                             is configurable on the SIP screen. Default setting: 985@-16,1428@-16,1777@-16;20(.380/0/1,.380/0/2,.380/0/3,0/4/0) |
| SIT2 Tone | Alternative to the Reorder Tone played when an error occurs as a caller makes an outbound call. The RSC to trigger this tone
                                             is configurable on the SIP screen. Default setting: 914@-16,1371@-16,1777@-16;20(.274/0/1,.274/0/2,.380/0/3,0/4/0) |
| SIT3 Tone | Alternative to the Reorder Tone played when an error occurs as a caller makes an outbound call. The RSC to trigger this tone
                                             is configurable on the SIP screen. Default setting: 914@-16,1371@-16,1777@-16;20(.380/0/1,.380/0/2,.380/0/3,0/4/0) |
| SIT4 Tone | Alternative to the Reorder Tone played when an error occurs as a caller makes an outbound call. The RSC to trigger this tone
                                             is configurable on the SIP screen. Default setting: 985@-16,1371@-16,1777@-16;20(.380/0/1,.274/0/2,.380/0/3,0/4/0) |
| MWI Dial Tone | Played instead of the Dial Tone when there are unheard messages in the caller’s mailbox. Default setting: 350@-19,440@-19;2(.1/.1/1+2);10(*/0/1+2) |
| Cfwd Dial Tone | Played when all calls are forwarded. Default setting: 350@-19,440@-19;2(.2/.2/1+2);10(*/0/1+2) |
| Holding Tone | Informs the local caller that the far end has placed the call on hold. Default setting: 600@-19;*(.1/.1/1,.1/.1/1,.1/9.5/1) |
| Conference Tone | Played to all parties when a three-way conference call is in progress. Default setting: 350@-19;20(.1/.1/1,.1/9.7/1) |
| Secure Call Indication Tone | Played when a call has been successfully switched to secure mode. Play it for a short period - less than 30 seconds - and
                                             at a reduced level - less than 19 dBm - so it doesn't interfere with the call. Default setting: 397@-19,507@-19;15(0/2/0,.2/.1/1,.1/2.1/2) |
| Feature Invocation Tone | Played when a feature is implemented. Default setting: 350@-16;*(.1/.1/1) |
| Call Remind Tone | The holding tone is played on the Phone ports during the active call to remind you of the held call. Default setting: blank |

| Field | Description |
|---|---|
| Ring1 Cadence | Cadence script for distinctive ring 1. Default setting: 60(2/4) |
| Ring2 Cadence | Cadence script for distinctive ring 2. Default setting: 60(.8/.4,.8/4) |
| Ring3 Cadence | Cadence script for distinctive ring 3. Default setting: 60(.4/.2,.4/.2,.8/4) |
| Ring4 Cadence | Cadence script for distinctive ring 4. Default setting: 60(.3/.2,1/.2,.3/4) |
| Ring5 Cadence | Cadence script for distinctive ring 5. Default setting: 1(.5/.5) |
| Ring6 Cadence | Cadence script for distinctive ring 6. Default setting: 60(.2/.4,.2/.4,.2/4) |
| Ring7 Cadence | Cadence script for distinctive ring 7. Default setting: 60(.4/.2,.4/.2,.4/4) |
| Ring8 Cadence | Cadence script for distinctive ring 8. Default setting: 60(0.25/9.75) |

| Field | Description |
|---|---|
| CWT1 Cadence | Cadence script for distinctive CWT 1. Default setting: *(.3/9.7) |
| CWT2 Cadence | Cadence script for distinctive CWT 2. Default setting: 30(.1/.1, .1/9.7) |
| CWT3 Cadence | Cadence script for distinctive CWT 3. Default setting: 30(.1/.1, .1/.1, .1/9.7) |
| CWT4 Cadence | Cadence script for distinctive CWT 4. Default setting: 30(.1/.1, .3/.1, .1/9.3) |
| CWT5 Cadence | Cadence script for distinctive CWT 5. Default setting: 1(.5/.5) |
| CWT6 Cadence | Cadence script for distinctive CWT 6. Default setting: 30(.1/.1,.3/.2,.3/9.1) |
| CWT7 Cadence | Cadence script for distinctive CWT 7. Default setting: 30(.3/.1,.3/.1,.1/9.1) |
| CWT8 Cadence | Cadence script for distinctive CWT 8. Default setting: 2.3(.3/2) |

| Field | Description |
|---|---|
| Ring1 Name | Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 1 for the inbound call. Default setting: Bellcore-r1 |
| Ring2 Name | Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 2 for the inbound call. Default setting: Bellcore-r2 |
| Ring3 Name | Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 3 for the inbound call. Default setting: Bellcore-r3 |
| Ring4 Name | Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 4 for the inbound call. Default setting: Bellcore-r4 |
| Ring5 Name | Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 5 for the inbound call. Default setting: Bellcore-r5 |
| Ring6 Name | Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 6 for the inbound call. Default setting: Bellcore-r6 |
| Ring7 Name | Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 7 for the inbound call. Default setting: Bellcore-r7 |
| Ring8 Name | Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 8 for the inbound call. Default setting: Bellcore-r8 |

| Field | Description |
|---|---|
| Ring Waveform | Waveform for the ringing signal. Choices are Sinusoid or Trapezoid. Default setting: Trapezoid |
| Ring Frequency | Frequency of the ringing signal. Valid values are 15–50 (Hz) Default setting: 20 |
| Ring Voltage | Ringing voltage. Choices are 30–90 (V) Default setting: 85 |
| CWT Frequency | Frequency script of the call waiting tone. All distinctive CWTs are based on this tone. Default setting: 440@-10 |
| Synchronized Ring | If this is set to yes, when the ATA is called, all lines ring at the same time (similar to a regular PSTN line). After one
                                             line answers, the others stop ringing. Default setting: no |

| Field | Description |
|---|---|
| Hook Flash Timer Min. | Minimum on-hook time before off-hook qualifies as hook flash. Less than this value, and the on-hook event is ignored. Range:
                                             0.1–0.4 seconds. Default setting: 0.1 |
| Hook Flash Timer. | Max Maximum on-hook time before off-hook qualifies as hook flash. More than this value, and the on-hook event is treated as
                                             on hook (no hook-flash event). Range: 0.4–1.6 seconds. Default setting: 0.9 |
| Callee On Hook Delay. | Phone must be on-hook for time before the ATA tears down the current inbound call. It does not apply to outbound calls. Range: 0–255 seconds. Default setting: 0 |
| Reorder Delay. | Delay after far end hangs up before reorder tone is played. 0 = plays immediately, inf = never plays. Range: 0–255 seconds. Default setting: 5. |
| Call Back Expires. | Expiration time in seconds of a call back activation. Range: 0–65535 seconds. Default setting: 1800 |
| Call Back Retry Intvl. | Call back retry interval in seconds. Range: 0–255 seconds. Default setting: 30 |
| Call Back Delay. | Delay after receiving the first SIP 18x response before declaring the remote end is ringing. If a busy response is received
                                             during this time, the ATA still considers the call as failed and keeps on retrying. Range: 0–65 seconds. Default setting: 0.5 |
| VMWI Refresh Intvl. | Interval between VMWI refresh to the device. Range: 0–65535 seconds. Default setting: 0 |
| Interdigit Long Timer. | Long timeout between entering digits when dialing. The interdigit timer values are used as defaults when dialing. The Interdigit_Long_Timer
                                             is used after any one digit, if all valid matching sequences in the dial plan are incomplete as dialed. Range: 0–64 seconds. Default setting: 10 |
| Interdigit Short Timer. | Short timeout between entering digits when dialing. The Interdigit_Short_Timer is used after any one digit, if at least one
                                             matching sequence is complete as dialed, but more dialed digits would match other as yet incomplete sequences. Range: 0–64
                                             seconds. Default setting: 3 |
| CPC Delay. | Delay in seconds after caller hangs up when the ATA starts removing the tip-and-ring voltage to the attached equipment of
                                             the called party. The range is 0–255 seconds. This feature is generally used for answer supervision on the caller side to
                                             signal to the attached equipment when the call has been connected (remote end has answered) or disconnected (remote end has
                                             hung up) This feature should be disabled for the called party (in other words, by using the same polarity for connected and
                                             idle state) and the CPC feature should be used instead. Without CPC enabled, reorder tone is played after a configurable delay. If CPC is enabled, dial tone will be played when tip-to-ring
                                             voltage is restored. Resolution is 1 second. Default setting: 2 |
| CPC Duration. | Duration in seconds for which the tip-to-ring voltage is removed after the caller hangs up. After that, tip-to-ring voltage
                                             is restored and the dial tone applies if the attached equipment is still off-hook. CPC is disabled if this value is set to
                                             0. Range: 0 to 1.000 second. Resolution is 0.001 second. Default setting: 0.5 |

| Field | Description |
|---|---|
| Call Return Code. | Call Return Code This code calls the last caller. Default setting: *69 |
| Call Redial Code. | Redials the last number called. Default setting: *07 |
| Blind Transfer Code. | Begins a blind transfer of the active call to the extension specified after the activation code. Default setting: *98 |
| Call Back Act Code. | Starts a callback when the last outbound call is not busy. Default setting: *66 |
| Call Back Deact Code. | Cancels a callback. Default setting: *86 |
| Call Back Busy Act Code. | Starts a callback when the last outbound call is busy. Default setting: *05 |
| Cfwd All Act Code. | Forwards all calls to the extension specified after the activation code. Default setting: *72 |
| Cfwd All Deact Code. | Cancels call forwarding of all calls. Default setting: *73 |
| Cfwd Busy Act Code. | Forwards busy calls to the extension specified after the activation code. Default setting: *90 |
| Cfwd Busy Deact Code. | Cancels call forwarding of busy calls. Default setting: *91 |
| Cfwd No Ans Act Code. | Forwards no-answer calls to the extension specified after the activation code. Default setting: *92 |
| Cfwd No Ans Deact Code. | Cancels call forwarding of no-answer calls. Default setting: *93 |
| Cfwd Last Act Code. | Forwards the last inbound or outbound call to the number that you specify after entering the activation code. Default setting: *63 |
| Cfwd Last Deact Code. | Cancels call forwarding of the last inbound or outbound call. Default setting: *83 |
| Block Last Act Code. | Blocks the last inbound call. Default setting: *60 |
| Block Last Deact Code. | Cancels blocking of the last inbound call. Default setting: *80 |
| Accept Last Act Code. | Accepts the last outbound call. It lets the call ring through when Do Not Disturb or call forwarding of all calls are enabled. Default setting: *64 |
| Accept Last Deact Code. | Cancels the code to accept the last outbound call. Default setting: *84 |
| CW Act Code. | Enables call waiting on all calls. Default setting: *56 |
| CW Deact Code. | Disables call waiting on all calls. Default setting: *57 |
| CW Per Call Act Code. | Enables call waiting for the next call. Default setting: *71 |
| CW Per Call Deact Code. | Disables call waiting for the next call. Default setting: *70 |
| Block CID Act Code. | Blocks caller ID on all outbound calls. Default setting: *67 |
| Block CID Deact Code. | Removes caller ID blocking on all outbound calls. Default setting: *68 |
| Block CID Per Call Act Code. | Blocks caller ID on the next outbound call. Default setting: *81 |
| Block CID Per Call Deact Code. | Removes caller ID blocking on the next inbound call. Default setting: *82 |
| Block ANC Act Code. | Blocks all anonymous calls. Default setting: *77 |
| Block ANC Deact Code. | Removes blocking of all anonymous calls. Default setting: *87 |
| DND Act Code. | Enables the Do Not Disturb feature. Default setting: *78 |
| DND Deact Code. | Disables the Do Not Disturb feature. Default setting: *79 |
| CID Act Code. | Enables caller ID generation. Default setting: *65 |
| CID Deact Code. | Disables caller ID generation. Default setting: *85 |
| CWCID Act Code. | Enables call waiting, caller ID generation. Default setting: *25 |
| CWCID Deact Code. | Disables call waiting, caller ID generation. Default setting: *45 |
| Dist Ring Act Code. | Enables the distinctive ringing feature. Default setting: *26 |
| Dist Ring Deact Code. | Disables the distinctive ringing feature. Default setting: *46 |
| Speed Dial Act Code. | Assigns a speed dial number. Default setting: *74 |
| Paging Code. | Used for paging other clients in the group. Default setting: *96 |
| Secure All Call Act Code. | Makes all outbound calls secure. Default setting: *16 |
| Secure No Call Act Code. | Makes all outbound calls not secure. Default setting: *17 |
| Secure One Call Act Code. | Makes the next outbound call secure. (It is redundant if all outbound calls are secure by default). Default setting: *18 |
| Secure One Call Deact Code. | Makes the next outbound call not secure. (It is redundant if all outbound calls are not secure by default). Default setting: *19 |
| Conference Act Code. | If this code is specified, you must enter it before dialing the third party for a conference call. Enter the code for a conference
                                             call. Default setting: blank |
| Attn-Xfer Act Code. | If the code is specified, you must enter it before dialing the third party for a call transfer. Enter the code for a call
                                             transfer. Default setting: blank |
| Modem Line Toggle Code. | Toggles the line to a modem. Modem passthrough mode can be triggered only by pre-dialing this code. Default setting: *99 |
| FAX Line Toggle Code. | Toggles the line to a fax machine. Default setting: #99 |
| Media Loopback Code. | Use for media loopback. Default setting: *03 |
| Referral Services Codes. | These codes tell the ATA what to do when you place the active call on hold and is listening to the second dial tone. One or
                                             more *codes can be configured into this parameter, such as *98, or *97\|*98\|*123, and so on. The maximum length is 79 characters.
                                             This parameter applies when you place the active call on hold by pressing the hook flash button. Each *code (and the following
                                             valid target number according to current dial plan) triggers the ATA to perform a blind transfer to a target number that is
                                             prepended by the service *code. For example, after you dial *98, the ATA plays the Prompt Tone while waiting for you to enter a target number (which is checked
                                             according to dial plan as in normal dialing). When a complete number is entered, the ATA sends a blind REFER to the holding
                                             party with the Refer-To target equal to *98 target_number. This feature allows the ATA to hand off a call to an application
                                             server to perform further processing, such as call park. The *codes should not conflict with any of the other vertical service codes internally processed by the ATA. You can empty
                                             the corresponding *code that you do not want the ATA to process. Default setting: blank |
| Feature Dial Services Codes. | These codes let the ATA know what to do when you are listening to the first or second dial tone. One or more *codes can be configured into this parameter, such as *72, or *72\|*74\|*67\|*82, and so on. The maximum length is
                                             79 characters. This parameter applies when you have a dial tone (first or second dial tone). After receiving dial tone, you enters the *code and the target number according to current dial plan. For example, after you
                                             dial *72, the ATA plays a special tone called a Prompt tone while awaiting you to enter a valid target number. When a complete
                                             number is entered, the ATA sends a INVITE to *72 target_number as in a normal call. This feature allows the proxy to process
                                             features like call forward (*72) or Block Caller ID (*67). The *codes should not conflict with any of the other vertical service codes internally processed by the ATA. You can remove
                                             a corresponding *code that you do not want to the ATA to process. You can add a parameter to indicate which tone plays after the *code is entered, such as *72‘c‘\|*67‘p‘. Below is a list of
                                             allowed tone parameters (note the use of open quotes surrounding the parameter, without spaces). 'c' = <Cfwd Dial Tone> 'd' = <Dial Tone> 'm' = <MWI Dial Tone> 'o' = <Outside Dial Tone> 'p' = <Prompt Dial Tone> 's' = <Second Dial Tone> 'x' = No tones are placed, x is any digit not used above. If no tone parameter is specified, the ATA plays Prompt tone by default. If the *code is not to be followed by a phone number, such as *73 to cancel call forwarding, do not include this parameter.
                                             Instead, add the *code in the dial plan and the ATA send INVITE *73@..... as usual when you dial *73. Default setting: blank |

| Field | Description |
|---|---|
| Service Annc Base Number | Base number for service announcements. Default setting: blank |
| Service Annc Extension Codes | Extension codes for service announcements. Default setting: blank |

| Field | Description |
|---|---|
| Prefer G711u Code. | Dial prefix to make G.711u the preferred codec for the call. Default setting: *017110 |
| Force G711u Code. | Dial prefix to make G.711u the only codec that can be used for the call. Default setting: *027110 |
| Prefer G711a Code. | Dial prefix to make G.711a the preferred codec for the call. Default setting: *017111 |
| Force G711a Code. | Dial prefix to make G.711a the only codec that can be used for the call. Default setting: *027111 |
| Prefer G726r32 Code. | Dial prefix to make G.726r32 the preferred codec for the call. Default setting: *0172632 |
| Force G726r32 Code. | Dial prefix to make G.726r32 the only codec that can be used for the call. Default setting: *0272632 |
| Prefer G729a Code. | Dial prefix to make G.729a the preferred codec for the call. Default setting: *01729 |
| Force G729a Code. | Dial prefix to make G.729a the only codec that can be used for the call. Default setting: *02729 |

| Field | Description |
|---|---|
| FXS Port Impedance: | Sets the electrical impedance of the PHONE port. Choices are: 600 900 600+2.16uF 900+2.16uF 220+850\|\|120nF 220+820\|\|115nF 200+600\|\|100nF Default setting: 600 |
| FXS Port Input Gain: | Input gain in dB, up to three decimal places. The range is 6.000 to -12.000. Default setting: -3 |
| FXS Port Output Gain: | Output gain in dB, up to three decimal places. The range is 6.000 to -12.000. The Call Progress Tones and DTMF playback level
                                             are not affected by the FXS Port Output Gain parameter. Default setting: -3 |
| DTMF Playback Level: | Local DTMF playback level in dBm, up to one decimal place. Range: -30–0. Default setting: -16.0 |
| DTMF Twist: | To gain difference between the two tone frequency. Range: 0–5. Default setting: 2 |
| DTMF Playback Length: | Local DTMF playback duration in milliseconds. Range: 0–65 seconds. Default setting: 0.1 |
| Detect ABCD: | To enable local detection of DTMF ABCD, select Yes . Otherwise, select No . Default setting: Yes This setting has no effect if DTMF Tx Method is INFO; ABCD is always sent OOB regardless in this setting. |
| Playback ABCD: | To enable local playback of OOB DTMF ABCD, select Yes . Otherwise, select No . Default setting: Yes |
| Caller ID Method: | Your choices are: Bellcore (N.Amer,China): CID, CIDCW, and VMWI. FSK sent after first ring (same as ETSI FSK sent after first ring) (no polarity
                                                      reversal or DTAS). DTMF (Finland, Sweden): CID only. DTMF sent after polarity reversal (and no DTAS) and before first ring. DTMF (Denmark): CID only. DTMF sent before first ring with no polarity reversal and no DTAS. ETSI DTMF: CID only. DTMF sent after DTAS (and no polarity reversal) and before first ring. ETSI DTMF With PR: CID only. DTMF sent after polarity reversal and DTAS and before first ring. ETSI DTMF After Ring: CID only. DTMF sent after first ring (no polarity reversal or DTAS). ETSI FSK: CID, CIDCW, and VMWI. FSK sent after DTAS (but no polarity reversal) and before first ring. Waits for ACK from a
                                                      device after DTAS for CIDCW. ETSI FSK With PR (UK): CID, CIDCW, and VMWI. FSK is sent after polarity reversal and DTAS and before first ring. Waits for
                                                      ACK from a device after DTAS for CIDCW. Polarity reversal is applied only if equipment is on hook. DTMF (Denmark) with PR: CID only. DTMF sent after polarity reversal (and no DTAS) and before first ring. Default setting: Bellcore(N.Amer, China) |
| FXS Port Power Limit: | The choices are from 1 to 8. Default setting: 3 |
| Caller ID FSK Standard: | The ATA supports bell 202 and v.23 standards for caller ID generation. Default setting: bell 202 |
| Feature Invocation Method: | Select the method you want to use, Default, or Sweden default. Default setting: Default. |

| Note | In a configuration profile, the FXS parameters must include an appropriate numeral for identifying the port receiving the
                                       setting. |
|---|---|

| Field | Description |
|---|---|
| Line Enable | To enable this line for service, select yes . Otherwise, select no . Default setting: yes |

| Field | Description |
|---|---|
| SAS Enable | To enable the use of the line as a streaming audio source, select yes. Otherwise, select no. If enabled, the line cannot be
                                             used for outgoing calls. Instead, it auto-answers incoming calls and streams audio RTP packets to the caller. Default setting: no |
| SAS DLG Refresh Intvl | A non-zero value is the interval in which the streaming audio server sends out session refresh (SIP re-INVITE) messages to
                                             determine if the connection is active. If the caller does not respond to the refresh message, the ATA ends this call with
                                             a SIP BYE message. The range is 0 to 255 seconds (0 means that the session refresh is disabled). Default setting: 30 |
| SAS Inbound RTP Sink | This parameter works around devices that do not play inbound RTP if the SAS line declares itself as a send-only device and
                                             tells the client not to stream out audio. This parameter is an FQDN or IP address of an RTP sink to be used by the SAS line
                                             in the SDP of its 200 response to inbound INVITE from a client. It appears in the c = line and the port number appears in
                                             the m = line of the SDP. If this value is not specified or is equal to 0, then c = 0.0.0.0 and a=sendonly are used in the SDP to tell the SAS client
                                             not to send any RTP to this SAS line. If a non-zero value is specified, then a=sendrecv and the SAS client streams audio to
                                             the given address. Special case: If the value is $IP, then the SAS line’s own IP address is used in the c = line and a=sendrecv. In that case,
                                             the SAS client streams RTP packets to the SAS line. Default setting: blank |

| Field | Description |
|---|---|
| NAT Mapping Enable | To use externally mapped IP addresses and SIP/RTP ports in SIP messages, select yes . Otherwise, select no . Default setting: no |
| NAT Keep Alive Enable | To send the configured NAT keep alive message periodically, select yes . Otherwise, select no . Default setting: no |
| NAT Keep Alive Msg | Enter the keep alive message sent periodically to maintain the current NAT mapping. Valid values are: $NOTIFY , $REGISTER , and $OPTIONS . $NOTIFY: A NOTIFY message is sent to keep NAT alive. $REGISTER: A REGISTER message without contact is sent. $OPTIONS: An OPTIONS message is sent. Default setting: $NOTIFY |
| NAT Keep Alive Dest | Destination receiving the NAT keep alive messages. If the value is $PROXY, the messages are sent to the current proxy server
                                             or outbound proxy server. Default setting: $PROXY |

| Field | Description |
|---|---|
| SIP ToS/DiffServ Value | TOS/DiffServ field value in UDP IP packets carrying a SIP message. Default setting: 0x68 |
| SIP CoS Value [0-7] | CoS value for SIP messages. Valid values are 0 through 7. Default setting: 3 |
| RTP ToS/DiffServ Value | ToS/DiffServ field value in UDP IP packets carrying RTP data. Default setting: 0xb8 |
| RTP CoS Value [0- 7] | CoS value for RTP data. Valid values are 0 through 7. Default setting: 6 |
| Network Jitter Level | Determines how jitter buffer size is adjusted by the ATA. Jitter buffer size is adjusted dynamically. The minimum jitter buffer
                                             size is 30 milliseconds or (10 milliseconds + current RTP frame size), whichever is larger, for all jitter level settings.
                                             However, the starting jitter buffer size value is larger for higher jitter levels. This setting controls the rate at which
                                             the jitter buffer size is adjusted to reach the minimum. Select the appropriate setting: low, medium, high, very high, or
                                             extremely high. Default setting: high |
| Jitter Buffer Adjustment | Choose yes to enable or no to disable this feature. Default setting: yes |

| Field | Description |
|---|---|
| SIP Transport | Select the protocol for SIP messages: UDP TCP TLS AUTO The TCP choice provides “guaranteed delivery”, which assures that lost packets are retransmitted. TCP also guarantees that
                                             the SIP packages are received in the same order that they were sent. As a result, TCP overcomes the main disadvantages of
                                             UDP. In addition, for security reasons, most corporate firewalls block UDP ports. With TCP, new ports don't need to be opened
                                             or packets dropped for activities such as Internet browsing or e-commerce. AUTO allows the ATA to select the appropriate protocol automatically, based on the NAPTR records on the DNS server. |
| SIP Port | Port number of the SIP message listening and transmission port. Default setting: 5060 for PHONE1 and 5061 for PHONE2 |
| SIP 100REL Enable | To enable the support of 100REL SIP extension for reliable transmission of provisional responses (18x) and use of PRACK requests,
                                             select yes . Otherwise, select No . Default setting: No |
| EXT SIP Port | The external SIP port number. Default setting: blank |
| Auth Resync-Reboot | If this feature is enabled, the ATA authenticates the sender when it receives the NOTIFY resync reboot (RFC 2617) message.
                                             To use this feature, select Yes . Otherwise, select No . When the ATA works as a User Agent Server (UAS) and receives NOTIFY request from a User Agent Client (UAC), you can enable
                                             the 401 challenge for the NOTIFY request by doing the following: Set the field to Yes . Configure the fields User ID and Password (under the section Subscriber Information from Voice > Line (n) ). Note You can replace User ID with Auth ID for the authentication. To achieve this, see Subscriber information for details. Default setting: Yes | Note | You can replace User ID with Auth ID for the authentication. To achieve this, see Subscriber information for details. |
| Note | You can replace User ID with Auth ID for the authentication. To achieve this, see Subscriber information for details. |
| SIP Proxy-Require | The SIP proxy can support a specific extension or behavior when it sees this header from the user agent. If this field is
                                             configured and the proxy does not support it, it responds with the message, unsupported. Enter the appropriate header in the
                                             field provided. Default setting: blank |
| SIP Remote-Party-ID | To use the Remote-Party-ID header instead of the From header, select Yes . Otherwise, select No . Default setting: Yes |
| SIP GUID | This feature limits the registration of SIP accounts. The Global Unique ID is generated for each line for each ATA. When it
                                             is enabled, the ATA adds a GUID header in the SIP request. The GUID is generated the first time the unit boots up and stays
                                             with the unit through rebooting and even factory reset. Default setting: No |
| RTP Log Intvl | The interval for the RTP log. Default setting: 0 |
| Restrict Source IP | If configured, the ATA drops all packets sent to its SIP Ports from an untrusted IP address. A source IP address is untrusted
                                             if it doesn't match the IP addresses resolved from the configured Proxy (or Outbound Proxy if Use Outbound Proxy is Yes). Default setting: No |
| Referor Bye Delay | The number of seconds to wait before sending a BYE to the referrer to terminate a stale call leg after a call transfer). Default setting: 4 |
| Refer Target Bye Delay | The number of seconds to wait before sending a BYE to the refer target to terminate a stale call leg after a call transfer. Default setting: 0 |
| Referee Bye Delay | The number of seconds to wait before sending a BYE to the referee to terminate a stale call leg after a call transfer. Default setting: 0 |
| Refer-To Target Contact | To contact the refer-to target, select yes . Otherwise, select No . Default setting: no |
| Sticky 183 | If this feature is enabled, the ATA ignores further 180 SIP responses after receiving the first 183 SIP response for an outbound
                                             INVITE. To enable this feature, select Yes . Otherwise, select No . Default setting: No |
| Auth INVITE | When enabled, authorization is required for initial incoming INVITE requests from the SIP proxy. When the ATA works as a User Agent Server (UAS) and receives INVITE request from a User Agent Client (UAC), you can enable
                                             the 401 challenge for the INVITE request by doing the following: Set the field to Yes . Configure the fields User ID and Password (under the section Subscriber Information from Voice > Line (n) ). Note You can replace User ID with Auth ID for the authentication. To achieve this, see Subscriber information for details. Default setting: No | Note | You can replace User ID with Auth ID for the authentication. To achieve this, see Subscriber information for details. |
| Note | You can replace User ID with Auth ID for the authentication. To achieve this, see Subscriber information for details. |
| Reply 182 On Call Waiting | When enabled, the ATA replies with a SIP182 response to the caller if it is already in a call and the line is off-hook. To
                                             use this feature, select Yes . Default setting: No |
| Use Anonymous With RPID | Determine whether the ATA uses “Anonymous” when Remote Party ID is requested in the SIP message. Default setting: Yes |
| Use Local Addr In From | Use the local ATA IP address in the SIP FROM message. Default setting: No |
| Broadsoft ALTC | Set whether the SIP is the Broadsoft ALTC. Default setting: No |
| Auth Support RFC8760 | Determine whether the ATA authorization supports RFC-8760. If set to Yes , ATA authorization supports the digest algorithms SHA256, SHA-512/256, and MD5. When ATA works as a User Agent Client (UAC), it sends SIP REGISTER or INVITE or SUBSCRIBE requests without authorization header
                                                   field. SIP server responses 401/407 status code with www-authenticate or proxy-authenticate header field. A SIP server responds
                                                   with multiple www-authenticate headers. If multiple headers are sent, each must have a different algorithm, with the most
                                                   preferred one first. When the field, Auth Resync-Reboot , and Auth INVITE are set to Yes , ATA will send 401 status code with multiple www-authenticate header fields. The algorithm SHA-256 is top prioritized. If set to No , ATA authorization only supports the digest algorithm MD5. When ATA works as a User Agent Client (UAC), it sends SIP requests without authorization header field. SIP server responses
                                                   401 status code. ATA retries to send request and add an authorization header with MD5 algorithm for server to validate. Default setting: No |
| MediaSec Request | Determine whether the ATA initiates media plane security negotiations with the server. If set to Yes , ATA supports the client-initiated mode. The ATA phone can initiate media plane security negotiations. If set to No , ATA only supports the server-initiated mode. In this case, the server initiates media plane security negotiations. The ATA
                                                   doesn't initiate negotiations, but can handle negotiation requests from the server to establish secure calls. To use this parameter, make sure that the following conditions are satisfied: Set Secure Call Serv (under the section Supplementary Service Subscription )  to Yes . Set Secure Call Option (under the section Call Feature Settings ) set to Optional . Default setting: No |
| MediaSec Over TLS Only | Determine how the ATA initiates or handles the media plane security negotiations. This parameter works with MediaSec Request . If set to Yes , ATA initiates or handles media plane security negotiations only when SIP over TLS. If set to No , ATA initiates or handles media plane security negotiations regardless of the protocol (UDP/TCP/TLS) for SIP messages. To use this parameter, make sure the following conditions are satisfied: Set Secure Call Serv (under the section Supplementary Service Subscription )  to Yes . Set Secure Call Option (under the section Call Feature Settings ) set to Optional . Default setting: No |

| Note | You can replace User ID with Auth ID for the authentication. To achieve this, see Subscriber information for details. |
|---|---|

| Note | You can replace User ID with Auth ID for the authentication. To achieve this, see Subscriber information for details. |
|---|---|

| Step 1 | Select Voice > Line(n) , where n is the line number that represents PHONE 1 or PHONE 2. |
|---|---|
| Step 2 | In the section Call Feature Settings , set the paramter Secure Call Option as described in Call Feature Settings . |
| Step 3 | Click Submit . |

| Field | Description |
|---|---|
| Blind Attn-Xfer Enable | Enables the ATA to perform an attended transfer operation by ending the active call leg and performing a blind transfer of
                                             the other call leg. If this feature is disabled, the ATA performs an attended transfer operation by referring the other call
                                             leg to the active call leg, while maintaining both call legs. To use this feature, select yes . Otherwise, select no . Default setting: no |
| MOH Server | User ID or URL of the auto-answering streaming audio server. When only a user ID is specified, the current or outbound proxy
                                             is contacted. Music-on-hold is disabled if the MOH Server is not specified. Default setting: blank |
| Xfer When Hangup Conf | Makes the ATA perform a transfer when a conference call has ended. Select yes or no from the drop-down menu. Default setting: yes |
| Conference Bridge URL | This feature supports external conference bridging for n-way conference calls (n>2), instead of mixing audio locally. To use
                                             this feature, set this parameter to that of the server's name. For example: conf@mysefver.com:12345 or conf (which uses the
                                             Proxy value as the domain). Default setting: blank |
| Conference Bridge Ports | Select the maximum number of conference call participants. The range is 3 to 10. Default setting: 3 |
| Enable IP Dialing. | Enable or disable IP dialing. If IP dialing is enabled, you can dial [userid@] a.b.c.d[:port], where ‘@’, ‘.’, and ‘:’ are
                                             dialed by entering *, user-id must be numeric and a, b, c, d must be between 0 and 255; the port must be larger than 255.
                                             If port is not given, 5060 is used. Port and User-Id are optional. If the user-id portion matches a pattern in the dial plan,
                                             then it is interpreted as a regular phone number according to the dial plan. The INVITE message, however, is still sent to
                                             the outbound proxy if it is enabled. Default setting: no |
| Emergency Number | Comma separated list of emergency number patterns. If outbound call matches one of the patterns, the ATA disables hook flash
                                             event handling. The condition is restored to normal after the call ends. Blank signifies that there is no emergency number.
                                             Maximum number length is 63 characters. Default setting: blank |
| Mailbox ID | Enter the ID number of the mailbox for this line. Default setting: blank |
| Feature Key Sync | Allows the phone to synchronize with the call server. If Do Not Disturb or Call Forwarding settings are changed on the phone,
                                             the changes are also made on the server. If changes are made on the server, they are propagated to the phone. Default setting: no |
| Secure Call Option | Configures a line to only accept secure calls. Select any of the options: Optional: Retains the current secure call option for the phone adapter. Strict: Allows SRTP only when SIP transport is set to TLS and if the ATA receives an unsecure call, the call fails. Allows
                                             RTP only when SIP transport is UDP/TCP and if the ATA receives an unsecure call, the call fails. Default setting: Optional |

| Field | Description |
|---|---|
| Company UUID | The Universally Unique Identifier (UUID) assigned to the customer by the emergency call services provider. For example: 19c8168c-a366-44b5-853c-960fcaa19592 Allowed values: Maximum identifier length is 128 characters. Default setting: Blank |
| Primary Request URL | URL of the primary location server that provides the emergency call services. The location server returns an HELD response to the phone with the requested location URI that is tied to the user phone IP
                                             address. This parameter must be in the form of a valid HTTP or HTTPS URL. Allowed values: A valid URL not exceeding 255 characters. Default setting: Blank |
| Secondary Request URL | URL of the backup server to obtain the user's phone location. If the primary request URL fails, ATA tries to send the secondary request URL to the emergency call services provider. This parameter must be in the form of a valid HTTP or HTTPS URL. Allowed values: A valid URL not exceeding 255 characters. Default setting: Blank |

| Field | Description |
|---|---|
| Proxy | SIP proxy server for all outbound requests. Default setting: blank |
| Outbound Proxy | SIP Outbound Proxy Server where all outbound requests are sent as the first hop. Default setting: blank |
| Survivability Proxy | Specifies a DNS A record of the Local Survivability Gateway (LSG) nodes. This allows the ATA to perform a failover to a survivability
                                             gateway. String syntax: hostname[:port][:p=priority][:w=weight][:A=ip-list]
[\| hostname2[:port][:p=priority][:w=weight][:A=ip-list]] Where: ip-list: ip-addr[,ip-addr[,ip-addr…]] Default: port=0 Example: webex-sgw.example.com:8933:A=10.10.10.10 Where, webex-sgw.example.com=Provisioned LSG hostname. It is used for TLS certificate validation when connecting to LSG nodes. 8933=LSG port 10.10.10.10=Provisioned LSG address Compared to LSG nodes that have the lowest priority, SSE nodes always have high priority. If there are multiple LSG nodes,
                                             try one after the other. Default setting: blank |
| Use Outbound Proxy | Enables the use of an Outbound Proxy. If set to no, the Outbound Proxy and Use OB Proxy in Dialog parameters are ignored. Default setting: no |
| Use OB Proxy In Dialog | Whether to force SIP requests to be sent to the outbound proxy within a dialog. Ignored if the parameter Use Outbound Proxy
                                             is no, or the Outbound Proxy parameter is empty. Default setting: yes |
| Register | Enable periodic registration with the Proxy parameter. This parameter is ignored if Proxy is not specified. Default setting: yes |
| Make Call Without Reg | Allow making outbound calls without successful (dynamic) registration by the unit. If No, dial tone will not play unless registration
                                             is successful. Default setting: no |
| Register Expires | Expires value in sec in a REGISTER request. The ATA will periodically renew registration shortly before the current registration
                                             expired. This parameter is ignored if the Register parameter is no. Range: 0 – (231 – 1) sec. Default setting: 3600 |
| Ans Call Without Reg | Allow answering inbound calls without successful (dynamic) registration by the unit. Default setting: no |
| Use DNS SRV | Whether to use DNS SRV lookup for Proxy and Outbound Proxy. Default setting: no |
| DNS SRV Auto Prefix | If enabled, the ATA will automatically prepend the Proxy or Outbound Proxy name with _sip._udp when performing a DNS SRV lookup
                                             on that name. Default setting: no |
| Proxy Fallback Intvl | After failing over to a lower priority server, the ATA waits for the specified Proxy Fallback Interval, in seconds, before
                                             retrying the highest priority proxy (or outbound proxy) servers. This parameter is useful only if the primary and backup proxy
                                             server list is provided to the ATA via DNS SRV record lookup on the server name. Using multiple DNS A records per server name does not allow the notion of priority, so all hosts will be considered at the
                                             same priority and the ATA will not attempt to fall back after a failover. If the value is 0, the SIP proxy fallback feature is disabled. Range: 0 –65535 sec Default setting: 3600 |
| Survivability Proxy Fallback Intvl | After ATA is registered to an LSG node, it waits for the specified interval before it attempts to fallback to a Webex Calling
                                             SSE node when any SSE node is reachable. If there's an active call on the ATA, the call still remains during the fallback process. Default setting: 30 |
| Proxy Redundancy Method | The method that the ATA uses to create a list of proxies returned in the DNS SRV records. If you select Normal , the list will contain proxiesranked by weight and priority. If you select Based on SRV port, the ATA also inspects the port number based on 1st proxy’s port. Default setting: Normal |
| Mailbox Subscribe URL | The URL or IP address of the voicemail server. Default setting: blank |
| Mailbox Subscribe Expires | Sets subscription interval for voicemail message waiting indication. When this time period expires, the ATA sends another
                                             subscribe message to the voice mail server. Default setting: 2147483647 |
| Auto Register When Failover | Controls the fallback duration. no : the fallback happens immediately and automatically. If the Proxy Fallback Intvl is exceeded, all the new SIP messages go
                                                   to the primary proxy. yes : the fallback happens only when current registration expires, which means only a REGISTER message can trigger fallback. For example, when the value for Register Expires is 3600 seconds and Proxy Fallback Intvl is 600 seconds, the fallback is
                                             triggered 3600 seconds later and not 600 seconds later. When the value for Register Expires is 600 seconds and Proxy Fallback
                                             Intvl is 1000 seconds, the fallback is triggered at 1200 seconds. After successfully registering back to primary server, all
                                             the SIP messages go to primary server. Default setting: yes |

| Field | Description |
|---|---|
| Display Name | Display name for caller ID. Default setting: blank |
| User ID | User ID for this line. Default setting: blank |
| Password | Password for this line. Default setting: blank |
| Use Auth ID | To use the authentication ID and password for SIP authentication, select yes . Otherwise, select no to use the user ID and password. Default setting: no |
| Auth ID | Authentication ID for SIP authentication. Default setting: blank |
| Reserved Auth Realm | The value of an authentication realm, which is used in the www-authenticate/proxy-authenticate header field for the INVITE
                                             and NOTIFY requests. Default setting: Blank. The proxy IP address is used as the authentication realm. |
| Resident Online Number | This setting allows you to associate a "local" telephone number with this line using a valid Skype Online Number from Skype.
                                             Calls made to that number will ring your phone. Enter the number without spaces or special characters. Default setting: blank |
| SIP URI | The parameter by which the user agent will identify itself for this line. If this field is blank, the actual URI used in the
                                             SIP signaling should be automatically formed as: sip:UserName@Domain Where UserName is the username given for this line in the User ID, and Domain is the domain given for this profile in the
                                             User Agent Domain. If the User Agent Domain is an empty string, then the IP address of the phone should be used for the domain. If the URI field is not empty, but if a SIP or SIPS URI that contains no @ character, then the actual URI used in the SIP
                                             signaling should be automatically formed by appending this parameter with an @ character followed by the IP address of the
                                             device. |

| Field | Description |
|---|---|
| Call Waiting Serv | Enable Call Waiting Service. Default setting: yes |
| Block CID Serv | Enable Block Caller ID Service. Default setting: yes |
| Block ANC Serv | Enable Block Anonymous Calls Service Default setting: yes |
| Dist Ring Serv | Enable Distinctive Ringing Service Default setting: yes |
| Cfwd All Serv | Enable Call Forward All Service Default setting: yes |
| Cfwd Busy Serv | Enable Call Forward Busy Service Default setting: yes |
| Cfwd No Ans Serv | Enable Call Forward No Answer Service Default setting: yes |
| Cfwd Sel Serv | Enable Call Forward Selective Service. Configure this service in the Selective Call Forward Settings section. Default setting: yes |
| Cfwd Last Serv | Enable Forward Last Call Service Default setting: yes |
| Block Last Serv | Enable Block Last Call Service Default setting: yes |
| Accept Last Serv | Enable Accept Last Call Service Default setting: yes |
| DND Serv | Enable Do Not Disturb Service Default setting: yes |
| CID–Serv | Enable Caller ID Service Default setting: yes |
| CWCID Serv | Enable Call Waiting Caller ID Service Default setting: yes |
| Call Return Serv | Enable Call Return Service Default setting: yes |
| Call Redial Serv | Enable Call Redial Service. Default setting: yes |
| Call Back Serv | Enable Call Back Service. Default setting: yes |
| Three Way Call Serv | Enable Three Way Calling Service. Three Way Calling is required for Three Way Conference and Attended Transfer. Default setting: yes |
| Three Way Conf Serv | Enable Three Way Conference Service. Three Way Conference is required for Attended Transfer. Default setting: yes |
| Attn Transfer Serv | Enable Attended Call Transfer Service. Three Way Conference is required for Attended Transfer. Default setting: yes |
| Unattn Transfer Serv | Enable Unattended (Blind) Call Transfer Service. Default setting: yes |
| MWI Serv | Enable MWI Service. MWI is available only if a Voice Mail Service is set-up in the deployment. Default setting: yes |
| VMWI Serv | Enable VMWI Service (FSK) Default setting: yes |
| Speed Dial Serv | Enable Speed Dial Service. Default setting: yes |
| Secure Call Serv | Secure Call Service. If this feature is enabled, a user can make a secure call by entering an activation code (*18 by default)
                                             before dialing the target number. Then audio traffic in both directions is encrypted for the duration of the call. Default setting: yes Star codes are set in Vertical Service Activation Codes. To enable secure calling by default, without requiring a star code,
                                             set the user’s Secure Call Setting to yes. See User 1 and User 2 . |
| Referral Serv | Enable Referral Service. See the Referral Services Codes parameter in Vertical Service Activation Codes for more information. Default setting: yes |
| Feature Dial Serv | Enable Feature Dial Service. See the Feature Dial Services Codes parameter in Vertical Service Activation Codes for more information. Default setting: yes |
| Service Announcement Serv | Enable Service Announcement Service. Default setting: no |
| Reuse CID Number As Name | Use the Caller ID number as the caller name. Default settings: yes |
| CONFCID Serv | Enable Caller ID during conference call. Default settings: yes |

| Field | Description |
|---|---|
| Preferred Codec | Preferred codec for all calls. (The actual codec used in a call still depends on the outcome of the codec negotiation protocol.)
                                                Select one of the following: G711u G711a G726-32 G729a Default setting: G711u. |
| Second Preferred Codec | If the first codec fails, then second preferred codec is tried. Default setting: blank |
| Third Preferred Codec | If the second codec fails, then third preferred codec is tried. Default setting: blank |
| Use Pref Codec Only | To use only the preferred codec for all calls, select yes . (The call fails if the far end does not support this codec.) Otherwise, select no . Default setting: no |
| Codec Negotiation | When set to Default , the Cisco IP phone responds to an Invite with a 200 OK response advertising the preferred codec only. When set to List All , the Cisco IP phone responds listing all the codecs that the phone supports. Default setting: Default |
| G729a Enable | To enable the use of the G.729a codec at 8 kbps, select yes . Otherwise, select no . Default setting: yes |
| Silence Supp Enable | To enable silence suppression so that silent audio frames are not transmitted, select yes . Otherwise, select no . Default setting: no |
| G726-32 Enable | To enable the use of the G.726 codec at 32 kbps, select yes . Otherwise, select no . Default setting: yes |
| Silence Threshold | Select the appropriate setting for the threshold: high , medium , or low . Default setting: medium |
| FAX V21 Detect Enable | To enable detection of V21 fax tones, select yes . Otherwise, select no . Default setting: yes |
| Echo Canc Enable | To enable the use of the echo canceller, select yes . Otherwise, select no. Default setting: yes |
| FAX CNG Detect Enable | To enable detection of the fax Calling Tone (CNG), select yes . Otherwise, select no . Default setting: yes |
| FAX Passthru Codec | Select the codec for fax passthrough, G711u or G711a . Default setting: G711u |
| FAX Codec Symmetric | To force the ATA to use a symmetric codec during fax passthrough, select yes . Otherwise, select no . Default setting: yes |
| DTMF Process INFO | To use the DTMF process info feature, select yes . Otherwise, select no . Default setting: yes |
| FAX Passthru Method | Select the fax passthrough method: None , NSE , or ReINVITE . Default setting: NSE |
| DTMF Process AVT | To use the DTMF process AVT feature, select yes . Otherwise, select no . Default setting: yes |
| FAX Process NSE | To use the fax process NSE feature, select yes . Otherwise, select no . Default setting: yes |
| DTMF Tx Method | Select the method to transmit DTMF signals to the far end: InBand , AVT , INFO , or Auto . InBand sends DTMF by using the audio path. AVT sends DTMF as AVT events. INFO uses the SIP INFO method. Auto uses InBand
                                                or AVT based on the outcome of codec negotiation. Default setting: Auto |
| FAX Disable ECAN | If enabled, this feature automatically disables the echo canceller when a fax tone is detected. To use this feature, select yes . Otherwise, select no . Default setting: no |
| DTMF Tx Mode | DTMF Detection Tx Mode is available for SIP information and AVT. Options are: Strict or Normal . Default setting: Strict for which the following are true: A DTMF digit requires an extra hold time after detection. The DTMF level threshold is raised to -20 dBm. The minimum and maximum duration thresholds are: strict mode for AVT and SIP: the value set in DTMF Tx Strict Hold Off Time normal mode for AVT: 40 ms normal mode for SIP: 50 ms |
| DTMF Tx Strict Hold Off Time | This parameter is in effect only when DTMF Tx Mode is set to strict, and when DTMF Tx Method is not set to inband; that is,
                                                either AVT or INFO. The value can be set as low as 40 ms. There is no maximum limit. A larger value will reduce the chance
                                                of talk-off (beeping) during conversation, at the expense of reduced performance of DTMF detection, which is needed for interactive
                                                voice response systems (IVR). Default setting: 70 ms |
| FAX Enable T38 | To enable the use of ITU-T T.38 standard for FAX Relay, select yes . Otherwise select no . no : The ATA can parse only one "m=" line of the SDP packet. If the ATA receives multiple "m=" lines contained in the SDP packet from a provider, an outbound FAX failure might occur.
                                                      This issue typically occurs when the first "m=" line specifies an invalid port number "0" while the second "m=" line specifies
                                                      a valid port. To avoid this issue, set FAX Enable T38 to yes and FAX Passthru Method to ReINVITE . In the aforementioned situation, the ATA can parse the second "m=" line successfully. yes : The ATA can parse the first two "m=" lines of the SDP packet. It ignores the other "m=" lines. Default setting: no |
| Hook Flash Tx Method | Select the method for signaling hook flash events: None , AVT , or INFO . None does not signal hook flash events. AVT uses RFC2833 AVT (event = 16) INFO uses SIP INFO with the single line signal=hf
                                                in the message body. The MIME type for this message body is taken from the Hook Flash MIME Type setting. Default setting: None |
| FAX T38 Redundancy | Select the appropriate number to indicate the number of previous packet payloads to repeat with each packet. Choose 0 for no payload redundancy. The higher the number, the larger the packet size and the more bandwidth consumed. Default setting: 1 |
| FAX T38 ECM Enable | Select yes to enable T.38 Error Correction Mode. Otherwise select no . Default setting: yes |
| FAX Tone Detect Mode | This parameter has three possible values: caller or callee : The ATA will detect FAX tone whether it is callee or caller caller only : The ATA will detect FAX tone only if it is the caller callee only : The ATA will detect FAX tone only if it is the callee Default setting: caller or callee. |
| Symmetric RTP | Enable symmetric RTP operation. If enabled, the ATA sends RTP packets to the source address and port of the last received
                                                valid inbound RTP packet. If disabled (or before the first RTP packet arrives) the ATA sends RTP to the destination as indicated
                                                in the inbound SDP. Default setting: no |
| Fax T38 Return to Voice | When this feature is enabled, upon completion of the fax image transfer, the connection remains established and reverts to
                                                a voice call using the previously designated codec. Select yes to enable this feature, or select no to disable it. Default setting: no |
| Modem Line | Enable an alternate method to make the modem call without Modem Line Toggle Code pre-dialing. Default setting: no |
| RTP to Proxy in Remote Hold | Enable to send RTP to proxy when line is held by remote side. Default setting: no |
| Encryption Method | Encryption algorithm used for the SRTP sessions (for example,  secure calls). Select one of the following: AES 128 AES 256 GCM Make sure that the Secure Call Service is enabled, see the parameter Secure Call Serv from the chapter Supplementary Service Subscription . Default setting: AES 128 |

| Dial Plan Entry | Functionality |
|---|---|
| *xx | Allow arbitrary 2 digit star code |
| [3469]11 | Allow x11 sequences |
| 0 | Operator |
| 00 | Int’l Operator |
| [2-9]xxxxxx | US local number |
| 1xxx[2-9]xxxxxx | US 1 + 10-digit long distance number |
| xxxxxxxxxxxx. | Everything else |

| Field | Description |
|---|---|
| Idle Polarity | Polarity before a call is connected: Forward or Reverse. Default setting: Forward |
| Caller Conn Polarity | Polarity after an outbound call is connected: Forward or Reverse. Default setting: Forward. |
| Callee Conn Polarity | Polarity after an inbound call is connected: Forward or Reverse. Default setting: Forward |

| Field | Description |
|---|---|
| Cfwd All Dest | Forward number for Call Forward All Service. Default setting: blank |
| Cfwd Busy Dest | Forward number for Call Forward Busy Service. Same as Cfwd All Dest. Default setting: blank |
| Cfwd No Ans Dest | Forward number for Call Forward No Answer Service. Same as Cfwd All Dest. Default setting: blank |
| Cfwd No Ans Delay | Delay in sec before Call Forward No Answer triggers. Default setting: 20 |

| Field | Description |
|---|---|
| Cfwd Sel1-8 Caller | Caller number pattern to trigger Call Forward Selective service. When the caller’s phone number matches the entry, the call
                                             is forwarded to the corresponding Cfwd Selective Destination (Cfwd Sel1-8 Dest). • Use ? to match any single digit. • Use * to match any number of digits. Example: 1408*, 1512???1234 In the above example, a call is forwarded to the corresponding destination if the caller ID either starts with 1408 or is
                                             an 11-digit numbering starting with 1512 and ending with 1234. Default setting: blank |
| Cfwd Sel1-8 Dest | The destination for the corresponding Call Forward Selective caller pattern (Cfwd Sel1-8 Caller). Default setting: blank |
| Cfwd Last Caller | The number of the last caller; this caller is actively forwarded to the Cfwd Last Dest via the Call Forward Last service.
                                             For more information, see Vertical Service Activation Codes . Default setting: blank |
| Cfwd Last Dest | The destination for the Cfwd Last Caller. |
| Block Last Caller | The number of the last caller; this caller is blocked via the Block Last Caller Service. For more information, see Vertical Service Activation Codes . Default setting: blank |
| Accept Last Caller | The number of the last caller; this caller is accepted via the Accept Last Caller Service. For more information, see Vertical Service Activation Codes . Default setting: blank |

| Field | Description |
|---|---|
| Speed Dial 2-9 | Target phone number (or URL) assigned to speed dial 2, 3, 4, 5, 6, 7, 8, or 9. Default setting: blank |

| Field | Description |
|---|---|
| CW Setting | Call Waiting on/off for all calls. Default setting: yes |
| Block CID | Setting Block Caller ID on/off for all calls. Default setting: no |
| Block ANC | Setting Block Anonymous Calls on or off. Default setting: no |
| DND | Setting DND on or off. Default setting: no |
| CID Setting | Caller ID Generation on or off. Default setting: yes |
| CWCID Setting | Call Waiting Caller ID Generation on or off. Default setting: yes |
| Dist Ring | Setting Distinctive Ring on or off. Default setting: yes |
| Secure Call Setting | If yes, all outbound calls are secure calls by default, without requiring the user to dial a star code first. Default setting: no If Secure Call Setting is set to yes , all outbound calls are secure. However, a user can disable security for a call by dialing *19 before dialing the target
                                                   number. If Secure Call Setting is set to No , the user can make a secure outbound call by dialing *18 before dialing the target number. A user cannot force inbound calls to be secure or not secure; that depends on whether the caller has security enabled or not. Note This setting is applicable only if Secure Call Serv is set to yes on the line interface. See Line 1 and Line 2 Settings (PHONE 1 and PHONE 2) . | Note | This setting is applicable only if Secure Call Serv is set to yes on the line interface. See Line 1 and Line 2 Settings (PHONE 1 and PHONE 2) . |
| Note | This setting is applicable only if Secure Call Serv is set to yes on the line interface. See Line 1 and Line 2 Settings (PHONE 1 and PHONE 2) . |
| Message Waiting | Setting this value to yes can activate stutter tone and VMWI signal. This parameter is stored in long term memory and will
                                             survive after reboot or power cycle. Default setting: no |
| Accept Media Loopback Request | Controls how to handle incoming requests for loopback operation. never —Never accepts loopback calls; replies 486 to the caller. automatic —Automatically accepts the call without ringing. manual —Rings the phone first, and the call must be picked up manually before loopback starts. Default setting: Automatic |
| Media Loopback Mode | The loopback mode to assume locally when making call to request media loopback. Choices are: Source and Mirror . Default setting: source Note If the ATA answers the call, the mode is determined by the caller. | Note | If the ATA answers the call, the mode is determined by the caller. |
| Note | If the ATA answers the call, the mode is determined by the caller. |
| Media Loopback Type | The loopback type to use when making call to request media loopback operation. Choices are Media and Packet . Default setting: media Note that if the ATA answers the call, then the loopback type is determined by the caller (the ATA always picks the first
                                             loopback type in the offer if it contains multiple type) |
| CONFCID Setting | Enables or disables the CONFCID. Default setting: yes |

| Note | This setting is applicable only if Secure Call Serv is set to yes on the line interface. See Line 1 and Line 2 Settings (PHONE 1 and PHONE 2) . |
|---|---|

| Note | If the ATA answers the call, the mode is determined by the caller. |
|---|---|

| Field | Description |
|---|---|
| Ring1 - 8 Caller | Caller number pattern to play Distinctive Ring/CWT 1, 2, 3, 4, 5, 6, 7, or 8. Caller number patterns are matched from Ring
                                             1 to Ring 8. The first match (not the closest match) will be used for alerting the subscriber. The distinctive rings are set
                                             on the Regional page. See Regional . Default setting: blank |

| Field | Description |
|---|---|
| Default Ring | Default ringing pattern, 1–8, for all callers. Default setting: 1 |
| Default CWT | Default CWT pattern, 1–8, for all callers. Default setting: 1 |
| Hold Reminder Ring | Ring pattern for reminder of a holding call when the phone is on-hook. Default setting: 8 |
| Call Back Ring | Ring pattern for call back notification. Default setting: 7 |
| Cfwd Ring Splash Len | Duration of ring splash when a call is forwarded (0 – 10.0s) Default setting: 0 |
| Cblk Ring Splash Len | Duration of ring splash when a call is blocked (0 – 10.0s) Default setting: 0 |
| VMWI Ring Policy | The parameter controls when a ring splash is played when a the VM server sends a SIP NOTIFY message to the ATA indicating
                                             the status of the subscriber’s mail box. Three settings are available. Default setting: New VM Available New VM Available —Ring as long as there new voicemail messages. New VM Becomes Available —Ring at the point when the first new voicemail message is received. New VM Arrives —Ring when the number of new voicemail messages increases. |
| VMWI Ring Splash Len | Duration of ring splash when new messages arrive before the VMWI signal is applied (0 – 10.0s) Default setting: 0 |
| Ring On No New VM | If enabled, the ATA plays a ring splash when the voicemail server sends SIP NOTIFY message to the ATA indicating that there
                                             are no more unread voice mails. Some equipment requires a short ring to precede the FSK signal to turn off VMWI lamp. Default setting: no |