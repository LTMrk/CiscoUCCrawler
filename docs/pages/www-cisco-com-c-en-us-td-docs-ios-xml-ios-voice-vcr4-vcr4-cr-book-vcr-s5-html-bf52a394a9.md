---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr4-vcr4-cr-book-vcr-s5-html-bf52a394a9
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr4/vcr4-cr-book/vcr-s5.html
retrieved_at: 2026-08-16T23:17:41.673437+00:00
---

Cisco IOS Voice Command Reference - S commands

# Cisco IOS Voice Command Reference - S commands

Updated: December 20, 2025

Chapter: show dial-peer through show gatekeeper zone prefix

## Chapter: show dial-peer through show gatekeeper zone prefix

# show dial-peer through show gatekeeper zone prefix

## show dial-peer

To display the dial plan mapping table for protocol peers, use the show dial-peer command in privileged EXEC mode.

show dial-peer { carrier | cor | trunk-group-label }

### Syntax Description

carrier

Displays carrier ID configuration details of the peer protocol.

cor

Displays restriction settings class details.

trunk-group-label

Displays trunk group label configuration details.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(17)SX

This command was introduced.

12.4(22)T

This command was modified in a release earlier than Cisco IOS Release 12.4(22)T. The carrier and trunk-group-label keywords were added.

### Usage Guidelines

Use this command to display the dial plan mapping table for protocol peers along with the available keywords.

## Examples

The following sample output from the show dial-peer command displays restriction settings class details. The fields are self-explanatory.

```
Router# show dial-peer cor Class of Restriction
name: class1
```

## show dial-peer video

To display configuration information for video dial peers, use the show dial - peer video command in privileged EXEC mode.

show dial-peer video [number] [ summary ]

### Syntax Description

number

(Optional) A specific video dial peer. Output displays information about that dial peer.

summary

(Optional) Output displays a one-line summary of each video dial peer.

### Command Default

If both the name argument and summary keyword are omitted, command output displays detailed information about all video dial peers.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.0(5)XK

This command was introduced on the Cisco MC3810.

12.0(7)T

This command was integrated into Cisco IOS Release 12.0(7)T.

### Usage Guidelines

Use this command to display the configuration for all video dial peers configured for a router. To show configuration information
                              for only one specific dial peer, use the number argument to identify the dial peer.

## Examples

The following sample output displays detailed information about all configured video dial peers:

```
Router# show dial-peer video Video Dial-Peer 1
      type = videocodec, destination-pattern = 111
      port signal = 1/0, port media = Serial1
      nsap = 47.0091810000000050E201B101.00107B09C6F2.C8
Video Dial-Peer 2
      type = videoatm,   destination-pattern = 222
      session-target = ATM0 svc nsap 47.0091810000000050E201B101.00E01E92ADC2.C8
Video Dial-Peer 3
      type = videoatm,   destination-pattern = 333
      session-target = ATM0 pvc 70/70
```

The table below describes the significant fields shown in the output.

Field

Description

NSAP

Network service access point (NSAP) address

## show dial-peer voip keepalive status

To display the status of the destination when options-keepalive is configured under dial-peer, use the show dial-peer voip keepalive status command in privileged EXEC mode.

show dial-peer voip keepalive status [ dp-tag | tenant tenant-tag | <cr> ]

dp-tag

Dial-Peer Tag. Range: 1—1073741823.

tenant-tag

Keepalive status info for tenants. Range: 1—10000.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

This command was introduced.

### Usage Guidelines

Use this command to know the status of the destination when options-keepalive is configured under the dial-peer configuration
                              mode using the command voice-class sip options-keepalive profile . You can use this command to display the options keepalive status for individual session targets and server groups. The keepalive
                              status is displayed for IPv4, IPv6, and DNS format destinations.

CUBE does not display the status for dynamic dial-peers.

If the destination is configured as DNS SRV, the status of each of the records is maintained by CUBE. For example, if the
                              DNS SRV lookup results in four records, the status of each of these four records is displayed. For session server groups which
                              have multiple destinations, the keepalive status of each of these targets is displayed by the command.

The command output can be filtered also on the basis of tenant-tag and dp-tag .

The different STATUS for the dial-peer, as displayed by the
                              command, include:

active —The dial-peer is active and contains destinations that are available to be considered by CUBE for the routing of call handling.

busyout —The dial-peer is inactive and no suitable
                                    destinations are available currently.

partial —A dial-peer is marked as partially active
                                    if at least one of the destinations is active out of a group, and the rest
                                    are inactive (busyout).

NA —The command voice-class sip options-keepalive profile is not configured and hence the status is not available.

The different STATUS for the different destinations, as
                              displayed by the command, include:

active —The destination is available to CUBE.

busyout —The destination is marked inactive after
                                    the keepalive retries are exhausted.

You need to configure the same transport type for the dial-peers with same SRV
                                          destination.

## Examples

The following is sample output of the command that displays the status of the
                              dial-peer destination when options-keepalive is configured under the dial-peer:

```
router#show dial-peer voip keepalive status
 TAG        TENANT   DESTINATION                    OOD-SessID   PRI     WT      STATUS
 6          4        dns:company.com                                             partial
                      company1.com                  437          10      50      active              
                      ipv4:10.105.34.88:8788        
                      company2.com*                 0            10      50      busyout             
 8          -        dns:ex.company.com                                          active
                      example1.com                  438          10      50      active              
                      ipv4:10.105.34.88:8790        
                      example2.com                  439          10      50      active              
                      ipv4:10.64.86.70:8789         
 9          3        ipv4:10.64.86.70:8073          1            -       -       busyout
 10         -        sess-svr-grp:1        
                      ipv4:10.105.34.88:8071        2            -       -       busyout
                      ipv4:10.105.34.88:8072        3            -       -       busyout
                      ipv4:10.105.34.88:8073        4            -       -       busyout
 11         -        dns:demo3.com                                               active
                      ipv4:10.64.86.70:5060         440          -       -       active              
 12         -        dns:demo_failed.com*                                        busyout
 13         -        dns:demo4.com                                               partial
                      example3.com                  441          10      50      active              
                      ipv4:10.105.34.88:8792        
                      example4.com*                 0            10      50      busyout             
Note: For destinations that are marked with (*), DNS resolution has failed.

router#
```

### Related Commands

Command

Description

show voice class sip-options-keepalive

Displays the details of connectivity between CUBE VoIP dial peers and SIP servers.

## show dial-peer voice

To display information for voice dial peers, use the show dial-peer voice command in user EXEC or privileged EXEC mode.

show dial-peer voice [ number | busy-trigger-counter | summary | voip system ]

### Syntax Description

number

(Optional) A specific voice dial peer. The output displays detailed information about that dial peer.

busy-trigger-counter

(Optional) Displays the busy trigger call count on the VoIP dial peer.

summary

(Optional) Displays a short summary of each voice dial peer.

voip system

(Optional) Displays information about the VoIP dial peer.

### Command Default

If both the number argument and summary keyword are omitted, the output displays detailed information about all voice dial peers.

### Command Modes

User EXEC (>)

Privileged EXEC (#)

## Command History

Release

Modification

11.3(1)T

This command was introduced.

11.3(1)MA

This command was modified. The summary keyword was added for the Cisco MC3810.

12.0(3)XG

This command was implemented for Voice over Frame Relay (VoFR) on the Cisco 2600 series and Cisco 3600 series.

12.0(4)T

This command was implemented for VoFR on the Cisco 7200 series.

12.1(3)T

This command was implemented for modem pass-through over VoIP on the Cisco AS5300.

12.2(2)XB

This command was modified to support VoiceXML applications.

12.2(4)T

This command was implemented on the Cisco 1750.

12.2(8)T

This command was implemented on the Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745.

12.2(2)XN

This command was modified. Support for enhanced Media Gateway Control Protocol (MGCP) voice gateway interoperability was
                                          added to Cisco CallManager 3.1 for the Cisco 2600 series, Cisco 3600 series, and Cisco VG200.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T and Cisco CallManager 3.2 and implemented on the Cisco IAD2420.
                                          The command was enhanced to display configuration information for bandwidth, video codec, and rtp payload-type for H.263+
                                          and H.264 video codec.

12.4(22)T

This command was modified. This command was enhanced to display the current configuration state of the history-info header.
                                          Command output was updated to show IPv6 information.

15.0(1)XA

This command was modified. The output was enhanced to show the logical partitioning class of restriction (LPCOR) policy for
                                          outgoing calls.

15.1(1)T

This command was integrated into Cisco IOS Release 15.1(1)T.

15.1(3)T

This command was modified. The output was enhanced to display information about the bind at the dial-peer level and to display
                                          the connection status of Foreign Exchange Office (FXO) ports.

Cisco IOS XE Cupertino
                                                17.9.1a

This command was modified. The output was enhanced to display the OPTIONS ping keepalive status for a dial-peer.

### Usage Guidelines

Use the show dial-peer voice command to display the configuration for all VoIP and POTS dial peers configured for a gateway. To display configuration
                              information for only one specific dial peer, use the number argument. To display summary information for all dial peers, use the summary keyword.

The recommended command to verify the QoS settings that the signaling and media packets will be marked with when RSVP is not
                                          configured for call signaling on the Cisco UBE is the show dial-peer voice command.

## Examples

The following is sample output from the show dial-peer voice command for a POTS dial peer:

```
Device# show dial-peer voice 100 VoiceEncapPeer3201
peer type = voice, information type = video,
description = `',
tag = 3201, destination-pattern = `86001',
answer-address = `', preference=0,
CLID Restriction = None
CLID Network Number = `'
CLID Second Number sent 
CLID Override RDNIS = disabled,
source carrier-id = `',	target carrier-id = `',
source trunk-group-label = `',	target trunk-group-label = `',
numbering Type = `unknown'
group = 3201, Admin state is up, Operation state is up,
Outbound state is up,
incoming called-number = `', connections/maximum = 0/unlimited,
DTMF Relay = disabled,
URI classes:
	    Destination = 
huntstop = disabled,
in bound application associated: 'DEFAULT'
out bound application associated: ''
dnis-map = 
permission :both
        incoming COR list:maximum capability
outgoing COR list:minimum requirement
Translation profile (Incoming):
Translation profile (Outgoing):
incoming call blocking:
translation-profile = `'
disconnect-cause = `no-service'
advertise 0x40 capacity_update_timer 25 addrFamily 4 oldAddrFamily 4
type = pots, prefix = `',
forward-digits 4
session-target = `', voice-port = `2/0:23',
direct-inward-dial = enabled,
digit_strip = enabled,
register E.164 number with H323 GK and/or SIP Registrar = TRUE
fax rate = system,   payload size =  20 bytes
supported-language = ''
preemption level = `routine'
bandwidth:
	    maximum = 384 KBits/sec, minimum = 64 KBits/sec
voice class called-number:
	    inbound = `', outbound = `1'
Time elapsed since last clearing of voice call statistics never
        Connect Time = 0, Charged Units = 0,
Successful Calls = 0, Failed Calls = 0, Incomplete Calls = 0
Accepted Calls = 0, Refused Calls = 0,
Last Disconnect Cause is "",
Last Disconnect Text is "",
Last Setup Time = 0.
```

## Examples

The following is a sample output from this command for a VoIP dial peer:

```
Device# show dial-peer voice 101 VoiceOverIpPeer101
peer type = voice, system default peer = FALSE, information type = voice,
description = `',
tag = 1234, destination-pattern = `',
voice reg type = 0, corresponding tag = 0,
allow watch = FALSE
answer-address = `', preference=0,
CLID Restriction = None
CLID Network Number = `'
CLID Second Number sent 
CLID Override RDNIS = disabled,
rtp-ssrc mux = system
source carrier-id = `', target carrier-id = `',
source trunk-group-label = `',  target trunk-group-label = `',
numbering Type = `unknown'
group = 1234, Admin state is up, Operation state is down,
incoming called-number = `', connections/maximum = 0/unlimited,
DTMF Relay = disabled,
modem transport = system,
URI classes:
Incoming (Request) = 
Incoming (Via) = 
Incoming (To) = 
Incoming (From) = 
Destination = 
huntstop = disabled,
in bound application associated: 'DEFAULT'
out bound application associated: ''
dnis-map = 
permission :both
incoming COR list:maximum capability
outgoing COR list:minimum requirement
outgoing LPCOR: 
Translation profile (Incoming):
Translation profile (Outgoing):
incoming call blocking:
translation-profile = `'
disconnect-cause = `no-service'
advertise 0x40 capacity_update_timer 25 addrFamily 4 oldAddrFamily 4
mailbox selection policy: none
type = voip, session-target = `',
technology prefix: 
settle-call = disabled
ip media DSCP = ef, ip media rsvp-pass DSCP = ef
ip media rsvp-fail DSCP = ef, ip signaling DSCP = af31,
ip video rsvp-none DSCP = af41,ip video rsvp-pass DSCP = af41
ip video rsvp-fail DSCP = af41,
ip defending Priority = 0, ip preemption priority = 0
ip policy locator voice: 
ip policy locator video: 
UDP checksum = disabled,
session-protocol = sipv2, session-transport = system,
req-qos = best-effort, acc-qos = best-effort,
req-qos video = best-effort, acc-qos video = best-effort,
req-qos audio def bandwidth = 64, req-qos audio max bandwidth = 0,
req-qos video def bandwidth = 384, req-qos video max bandwidth = 0, 
RTP dynamic payload type values: NTE = 101
Cisco: NSE=100, fax=96, fax-ack=97, dtmf=121, fax-relay=122
CAS=123, TTY=119, ClearChan=125, PCM switch over u-law=0,
A-law=8, GSMAMR-NB=117 iLBC=116, AAC-ld=114, iSAC=124
lmr_tone=0, nte_tone=0
h263+=118, h264=119
G726r16 using static payload
G726r24 using static payload
RTP comfort noise payload type = 19
fax rate = voice,   payload size =  20 bytes
fax protocol = system
fax-relay ecm enable
Fax Relay ans enabled
Fax Relay SG3-to-G3 Enabled (by system configuration)
fax NSF = 0xAD0051 (default)
codec = g729r8,   payload size =  20 bytes,
video codec = None
voice class codec = `'
voice class sip session refresh system
voice class sip rsvp-fail-policy voice post-alert mandatory keep-alive interval 30
voice class sip rsvp-fail-policy voice post-alert optional keep-alive interval 30
voice class sip rsvp-fail-policy video post-alert mandatory keep-alive interval 30
voice class sip rsvp-fail-policy video post-alert optional keep-alive interval 30
text relay = disabled
Media Setting = forking (disabled) flow-through (global)
Expect factor = 10, Icpif = 20,
Playout Mode is set to adaptive,
Initial 60 ms, Max 1000 ms
Playout-delay Minimum mode is set to default, value 40 ms 
Fax nominal 300 ms
Max Redirects = 1, signaling-type = cas,
VAD = enabled, Poor QOV Trap = disabled, 
Source Interface = NONE
voice class sip url = system,
voice class sip tel-config url = system,
voice class sip rel1xx = system,
voice class sip anat = system,
voice class sip outbound-proxy = "system",
voice class sip associate registered-number = system,
voice class sip asserted-id system,
voice class sip privacy system
voice class sip e911 = system,
voice class sip history-info = system,
voice class sip reset timer expires 183 = system,
voice class sip pass-thru headers = system,
voice class sip pass-thru content unsupp = system,
voice class sip pass-thru content sdp = system,
voice class sip copy-list = system,
voice class sip g729 annexb-all = system,
voice class sip early-offer forced = system,
voice class sip negotiate cisco = system,
voice class sip block 180 = system,
voice class sip block 183 = system,
voice class sip block 181 = system,
voice class sip preloaded-route = system,
voice class sip random-contact = system,
voice class sip random-request-uri validate = system,
voice class sip call-route p-called-party-id = system,
voice class sip call-route history-info = system,
voice class sip privacy-policy send-always = system,
voice class sip privacy-policy passthru = system,
voice class sip privacy-policy strip history-info = system,
voice class sip privacy-policy strip diversion = system,
voice class sip map resp-code 181 = system,
voice class sip bind control = enabled, 9.42.28.29,
voice class sip bind media = enabled, 9.42.28.29,
voice class sip bandwidth audio = system,
voice class sip bandwidth video = system,
voice class sip encap clear-channel = system,
voice class sip error-code-override options-keepalive failure = system,
voice class sip calltype-video = false
voice class sip registration passthrough = System
voice class sip authenticate redirecting-number  = system,
redirect ip2ip = disabled
local peer = false
probe disabled,
Secure RTP: system (use the global setting)
voice class perm tag = `'
Time elapsed since last clearing of voice call statistics never
Connect Time = 0, Charged Units = 0,
Successful Calls = 0, Failed Calls = 0, Incomplete Calls = 0
Accepted Calls = 0, Refused Calls = 0,
Last Disconnect Cause is "",
Last Disconnect Text is "",
Last Setup Time = 0.
Last Disconnect Time = 0.
When there is no Dial-peer level bind -
voice class sip bind control = system,
voice class sip bind media = system,
```

## Examples

The following is sample output from the show dial-peer voice summary command that shows connected FXO port 0/2/0 (the last entry) has OUT STAT set to "up," which indicates that the POTS dial
                              peer can be used for an outgoing call. If this port is disconnected, the status changes in the output so that the OUT STAT
                              field reports "down," and the POTS dial peer cannot be used for an outgoing call.

Beginning in Cisco IOS Release 15.1(3)T, there is improved status monitoring of FXO ports--any time an FXO port is connected
                                          or disconnected, a message is displayed to indicate the status change. For example, the following message is displayed to
                                          report that a cable has been connected, and the status is changed to "up" for FXO port 0/2/0: 000118: Jul 14 18:06:05.122
                                          EST: %LINK-3-UPDOWN: Interface Foreign Exchange Office 0/2/0, changed state to operational status up due to cable reconnection

```
Router# show dial-peer voice summary dial-peer hunt 0
             AD                                    PRE PASS                OUT 
TAG    TYPE  MIN  OPER PREFIX    DEST-PATTERN      FER THRU SESS-TARGET    STAT PORT    KEEPALIVE
39275- voip  up   up             .T                 0  syst ipv4:172.18.108.26  
82                                                                             
8880   pots  up   up             8880               0                      up   2/0/0
8881   pots  up   up             8881               0                      up   2/0/1
8882   pots  up   up             8882               0                      up   2/0/2
8883   pots  up   up             8883               0                      up   2/0/3
8884   pots  up   up             8884               0                      up   2/0/4
8885   pots  up   up             8885               0                      up   2/0/5
8886   pots  up   up             8886               0                      up   2/0/6
8887   pots  up   up             8887               0                      up   2/0/7
88888- pots  up   up                                0 	                 down  0/3/0:23
888                                                                            
65033- pots  up   up             6503352            0                      up   0/2/0
52
```

The table below describes the significant fields shown in the displays, in alphabetical order.

Field

Description

Accepted Calls

Number of calls accepted from this peer since system startup.

acc-qos

Lowest acceptable quality of service configured for calls for this peer.

Admin state

Administrative state of this peer.

answer-address

Answer address configured for this dial peer.

bandwidth maximum/minimum

The maximum and minimum bandwidth, in Kb/s.

Charged Units

Total number of charging units that have applied to this peer since system startup, in hundredths of a second.

CLID Restriction

Indicates if Calling Line ID (CLID) restriction is enabled.

CLID Network Number

Displays the network number sent as CLID, if configured.

CLID Second Number sent

Displays whether a second calling number is stripped from the call setup.

CLID Override RDNIS

Indicates whether the CLID is overridden by the redirecting number.

codec

Default voice codec rate of speech.

Connect Time

Accumulated connect time to the peer since system startup for both incoming and outgoing calls, in hundredths of a second.

connections/maximum

Indicates the maximum number of call connections per peer.

Destination

Indicates the voice class that is used to match the destination URL.

destination-pattern

Destination pattern (telephone number) for this peer.

digit_strip

Indicates if digit stripping is enabled.

direct-inward-dial

Indicates if direct inward dial is enabled.

disconnect-cause

Indicates the disconnect cause code to be used when an incoming call is blocked.

dnis-map

Name of the dialed-number identification service (DNIS) map.

DTMF Relay

Indicates if dual-tone multifrequency (DTMF) relay is enabled.

Expect factor

User-requested expectation factor of voice quality for calls through this peer.

Failed Calls

Number of failed call attempts to this peer since system startup.

fax rate

Fax transmission rate configured for this peer.

forward-digits

Indicates the destination digits to be forwarded of this peer.

group

Group number associated with this peer.

huntstop

Indicates whether dial-peer hunting is turned on, by the huntstop command, for this dial peer.

Icpif

Configured Impairment/Calculated Planning Impairment Factor (ICPIF) value for calls sent by a dial peer.

in bound application associated

Interactive voice response (IVR) application that is configured to handle inbound calls to this dial peer.

incall-number

Full E.164 telephone number to be used to identify the dial peer.

incoming call blocking

Indicates the incoming call blocking setup of this peer.

incoming called-number

Indicates the incoming called number if it has been set.

incoming COR list

Indicates the level of Class of Restrictions for incoming calls of this peer.

Incomplete Calls

Indicates the number of outgoing disconnected calls with the user busy (17), no user response (18), or no answer (19) cause
                                          code.

information type

Information type for this call (voice, fax, video).

Last Disconnect Cause

Encoded network cause associated with the last call. This value is updated whenever a call is started or cleared and depends
                                          on the interface type and session protocol being used on this interface.

Last Disconnect Text

ASCII text describing the reason for the last call termination.

Last Setup Time

Value of the system uptime when the last call to this peer was started.

Modem passthrough

Modem pass-through signaling method is named signaling event (NSE).

numbering Type

Indicates the numbering type for a peer call leg.

Operation state

Operational state of this peer.

outgoing COR list

Indicates the level of Class of Restrictions for outgoing calls of this peer.

outgoing LPCOR

Setting of the lpcor outgoing command.

out bound application associated

The voice application that is configured to handle outbound calls from this dial peer. Outbound calls are handed off to the
                                          named application.

Outbound state

Indicates the current outbound status of a POTS peer.

payload size

Indicates the size (in bytes) of the payload of the fax rate or codec setup.

payload type

NSE payload type.

peer type

Dial peer type (voice, data).

permission

Configured permission level for this peer.

Poor QOV Trap

Indicates if poor quality of voice trap messages is enabled.

preemption level

Indicates the call preemption level of this peer.

prefix

Indicates dialed digits prefix of this peer.

Redundancy

Packet redundancy (RFC 2198) for modem traffic.

Refused Calls

Number of calls from this peer refused since system startup.

register E.164 number with H.323 GK and/or SIP Registrar

Indicates the "register e.164" option of this peer.

req-qos

Configured requested quality of service for calls for this dial peer.

session-target

Session target of this peer.

session-protocol

Session protocol to be used for Internet calls between local and remote routers through the IP backbone.

source carrier-id

Indicates the source carrier ID of this peer that will be used to match the source carrier ID of an incoming call.

source trunk-group label

Indicates the source trunk group label of this peer that can be used to match the source trunk group label of an incoming
                                          call.

Successful Calls

Number of completed calls to this peer.

supported-language

Indicates the list of supported languages of this peer.

tag

Unique dial peer ID number.

target carrier-id

Indicates the target carrier ID of this peer that will be used to match the target carrier ID for an outgoing call.

target-trunkgroup-label

Indicates the target trunk group label of this peer that can be used to match the target trunk group label of an outgoing
                                          call.

Time elapsed since last clearing of voice call statistics

Elapsed time between the current time and the time when the clear dial-peer voice command was executed.

Translation profile (Incoming)

Indicates the translation profile for incoming calls.

Translation profile (Outgoing)

Indicates the translation profile for outgoing calls.

translation-profile

Indicates the number translation profile of this peer.

type

Indicates the peer encapsulation type (pots, voip, vofr, voatm or mmoip).

VAD

Whether voice activation detection (VAD) is enabled for this dial peer.

voice class called-number inbound/outbound

Indicates the voice-class called number inbound or outbound setup of this peer.

voice class sip history-info

Indicates the configuration state of the history-info header. If the history-info header is not configured for the dial peer,
                                          this field is set to system. If the history-info header is enabled on this dial peer, this field is set to enable. If the
                                          history-info header is disabled on this dial peer, this field is set to disable.

voice class sip bind

Indicates the configuration state of the bind address. If the bind is configured for the global, this field is sent to system.
                                          If the bind address is enabled on this dial peer, this field is set to enabled.

voice-port

Indicates the voice interface setting of this POTS peer.

The following is sample output from this command with the summary keyword:

```
Router# show dial-peer voice summary dial-peer hunt 0
                                                      PASS
  TAG TYPE   ADMIN OPER PREFIX   DEST-PATTERN     PREF THRU SESS-TARGET    PORT
  100 pots   up    up                              0
  101 voip   up    up            5550112           0   syst ipv4:10.10.1.1
  102 voip   up    up            5550134           0   syst ipv4:10.10.1.1
   99 voip   up    down                            0   syst
   33 pots   up    down                            0
```

The table below describes the significant fields shown in the display.

Field

Description

dial-peer hunt

Hunt group selection order that is defined for the dial peer by the dial-peer hunt command.

TAG

Unique identifier assigned to the dial peer when it was created.

TYPE

Type of dial peer (mmoip, pots, voatm, vofr, or voip).

ADMIN

Whether the administrative state is up or down.

OPER

Whether the operational state is up or down.

PREFIX

Prefix that is configured in the dial peer by the prefix command.

DEST-PATTERN

Destination pattern that is configured in the dial peer by the destination-pattern command.

PREF

Hunt group preference that is configured in the dial peer by the preference command.

PASS THRU

Modem pass-through method that is configured in the dial peer by the modem passthrough command.

SESS-TARGET

Destination that is configured in the dial peer by the session target command.

PORT

Router voice port that is configured for the dial peer. Valid only for POTS dial peers.

## Examples

The following is sample output of the show dial-peer voice summary command that is enhanced from Cisco IOS XE Cupertino
                                    17.9.1a to display the overall keepalive status for the DNS SRV at the dial-peer level:

```
Router# show dial-peer voice summary dial-peer hunt 0
             AD                                    PRE PASS SESS-SER-GRP\  OUT 
TAG    TYPE  MIN  OPER PREFIX    DEST-PATTERN      FER THRU SESS-TARGET    STAT PORT    KEEPALIVE    VRF
4      voip  up   up             1234               0  syst dns:example1.com             active      NA            
5      voip  up   up             123456             0  syst dns:example2.com             partial     NA             
44     voip  up   up             1234               0  syst dns:example3.com             busyout     NA 
For server-grp details please execute command:show voice class server-group <tag_id>
To see complete session target for ipv6 use 'sh running-config | section dial-peer <tag>
Some nodes of this target may be down. Please execute the command 'show dial-peer voip keepalive status' to know the exact status of each node.
```

A dial-peer is marked as partially active ( partial ) if at least one of the destinations is active out of a group, and the rest are inactive.

### Related Commands

Command

Description

show call active voice

Displays the VoIP active call table.

show call history voice

Displays the VoIP call history table.

show dialplan incall number

Displays which POTS dial peer is matched for a specific calling number or voice port.

show dialplan number

Displays which dial peer is reached when a specific telephone number is dialed.

show num-exp

Displays how the number expansions are configured in VoIP.

show voice port

Displays configuration information about a specific voice port.

## show dialplan dialpeer

To display the outbound dial peers that are matched to an incoming dial peer based on the class of restriction (COR) criteria
                              and the dialed number, use the show dialplan dialpeer command in privileged EXEC mode.

show dialplan dialpeer incoming-dialpeer-tag number number [ timeout ]

### Syntax Description

incoming-dialpeer-tag

The dial peer COR identifier used to determine the matching outbound dial peer.

number

The dialed number used in conjunction with the COR identifier to determine the matching outbound dial peer.

timeout

(Optional) Allows matching for variable-length destination patterns.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.1(3)T

This command was introduced on the Cisco 2600 series and Cisco 3600 series routers and on Cisco AS5800 access servers.

12.2(11)T

This command was implemented on the Cisco 1751 and Cisco 3700 series routers and on Cisco AS5300 access servers.

### Usage Guidelines

Use this command as a troubleshooting tool to determine which outbound dial peer is matched for an incoming call, based on
                              the COR criteria and dialed number specified in the command line. Use the timeout keyword to enable matching variable-length
                              destination patters associated with dial peers. This can increase your chances of finding a match for the dial peer number
                              you specify.

For actual voice calls coming into the router, the incoming corlist of a specified inbound dial peer and the outgoing called
                                          number will be used to match the outbound dial peer.

## Examples

The following sample output shows an incoming call with a dialed number of 19001111 and meeting the COR criteria as part
                              of dial peer 300 with incoming COR-list has been matched to an outbound dial peer with IP address 1.8.50.7:

```
Router# show dialplan dialpeer 300 number 1900111 VoiceOverIpPeer900
        information type = voice,
        description = `',
        tag = 900, destination-pattern = `1900',
        answer-address = `', preference=0,
        numbering Type = `unknown'
        group = 900, Admin state is up, Operation state is up,
        incoming called-number = `', connections/maximum = 0/unlimited,
        DTMF Relay = disabled,
        modem passthrough = system,
        huntstop = disabled,
        in bound application associated: 'DEFAULT'
        out bound application associated: ''
        dnis-map = 
        permission :both
        incoming COR list:maximum capability
        outgoing COR list:to900
        type = voip, session-target = `ipv4:1.8.50.7',
        technology prefix: 
        settle-call = disabled
        ...
        Time elapsed since last clearing of voice call statistics never
        Connect Time = 0, Charged Units = 0,
        Successful Calls = 0, Failed Calls = 0, Incomplete Calls = 0
        Accepted Calls = 0, Refused Calls = 0,
        Last Disconnect Cause is "",
        Last Disconnect Text is "",
        Last Setup Time = 0.
Matched: 19001111   Digits: 4
Target: ipv4:1.8.50.7
```

The table below describes the significant fields shown in the display.

Field

Description

Macro Exp.

Expected destination pattern for this dial peer.

VoiceEncapPeer

Dial peer associated with the calling number entered.

VoiceOverIpPeer

Dial peer associated with the calling number entered.

peer type

Type of this dial peer (voice or data).

information type

Information type for this dial peer (voice or data).

description

Any additional information for this dial peer entered using the description dial peer command.

tag

Unique number identifying the dial peer.

destination-pattern

Destination pattern (telephone number) configured for this dial peer.

answer-address

Answer address (calling number) configured for this dial peer.

preference

Hunt group preference order set for this dial peer.

CLID restriction

Indicates the Caller ID restriction (if any) configured for this dial peer.

CLID Network Number

Indicates the originating network of the Caller ID source.

CLID Second Number sent

Indicates the digits in the second number (if any) forwarded for this dial peer.

source carrier-id

VoIP or POTS source carrier identifier.

source trunk-group-label

VoIP or POTS source trunk group identifier.

numbering Type

Identifies the numbering scheme employed for this dial peer.

group

Dial peer group in which this dial peer is a member.

Admin state

Administrative state of this dial peer.

Operation state

Operational state of this dial peer.

incoming called-number

Called number (DNIS) configured for this dial peer.

connections/maximum

Number of actual and maximum allowable connections associated with this dial peer.

DTMF Relay

Whether the dtmf - relay command is enabled or disabled for this dial peer.

URI classes: Incoming (Request)

URI voice class used for matching dial peer to Request-URI in an incoming SIP Invite message.

URI classes: Incoming (To)

URI voice class used for matching dial peer to the To header in an incoming SIP Invite message.

URI classes: Incoming (From)

URI voice class used for matching dial peer to the From header in an incoming SIP Invite message.

URI classes: Destination

URI voice class used to match the dial peer to the destination URI for an outgoing call.

modem transport

Transport method configured for modem calls. The default is system, which means that the value configured globally is used.

huntstop

Whether the huntstop command is enabled or disabled for this dial peer.

in bound application associated

IVR application that is associated with this dial peer when this dial peer is used for an inbound call leg.

out bound application associated

IVR application that is associated with this dial peer when this dial peer is used for an outbound call leg.

dnis-map

Name of the dialed-number identification service (DNIS) map that is configured in the dial peer with the dnis - map command.

permission

Configured permission level for this dial peer.

incoming COR list

Class of restriction (COR) criteria associated when matching an incoming dial peer.

outgoing COR list

COR criteria used to determine the appropriate outbound dial peer.

Translation profile (Incoming)

Incoming translation criteria applied to this dial peer.

Translation profile (Outgoing)

Translation criteria applied to this dial peer when matching an outbound dial peer.

incoming call blocking

Indicates whether or not incoming call blocking has been applied for this dial peer.

translation-profile

The predefined translation profile associated with this dial peer.

disconnect-cause

Encoded network cause associated with the last call.

voice-port

Voice port through which calls come into this dial peer.

type

Type of dial peer (POTS or VoIP).

prefix

Prefix number that is added to the front of the dial string before it is forwarded to the telephony device.

forward-digits

Which digits are forwarded to the telephony interface as configured using the forward - digits command.

session-target

Configured session target (IP address or host name) for this dial peer.

direct-inward-dial

Whether the direct - inward - dial command is enabled or disabled for this dial peer.

digit_strip

Whether digit stripping is enabled or disabled in the dial peer. Enabled is the default.

register E.164 number with GK

Indicates whether or not the dial peer has been configured to register its full E.164-format number with the local gatekeeper.

fax rate

The transmission speed configured for fax calls. The default is system, which means that the value configured globally is
                                          used.

payload size

The size (in bytes) for a fax transmission payload.

session-protocol

Session protocol to be used for Internet calls between local and remote router via the IP backbone.

req-qos

Configured requested quality of service for calls for this dial peer.

acc-qos

Lowest acceptable quality of service configured for calls for this dial peer.

codec

Voice codec configured for this dial peer. Default is G.729 (8 kbps).

Expect factor

User-requested expectation factor of voice quality for calls through this dial peer.

Icpif

Configured calculated planning impairment factor (ICPIF) value for calls sent by this dial peer.

VAD

Indicates whether or not voice activation detection (VAD) is enabled for this dial peer.

voice class sip url

URL format (SIP or TEL) used for SIP calls to this dial peer, as configured with the voice - class sip url command. The default is system, which means that the value configured globally with the url command in voice service VoIP SIP mode is used.

voice class sip rel1xx

Indicates whether or not reliable provisional responses are supported, as configured with the voice - class sip rel1xx command. The default is system, which means that the value configured globally with the rel1xx command in voice service VoIP SIP mode is used.

voice class perm tag

Voice class for a trunk that is assigned to this dial peer with the voice - class permanent command.

Connect Time

Unit of measure indicating the call connection time associated with this dial peer.

Charged Units

Number of call units charged to this dial peer.

Successful Calls

Number of completed calls to this dial peer since system startup.

Failed Calls

Number of uncompleted (failed) calls to this dial peer since system startup.

Incomplete Calls

Number of incomplete calls to this dial peer since system startup.

Accepted Calls

Number of calls from this dial peer accepted since system startup.

Refused Calls

Number of calls from this dial peer refused since system startup.

Last Disconnect Cause

Encoded network cause associated with the last call. This value is updated whenever a call is started or cleared and depends
                                          on the interface type and session protocol being used on this interface.

Last Disconnect Text

ASCII text describing the reason for the last call termination.

Last Setup Time

Value of the System Up Time when the last call to this peer was started.

Matched

Destination pattern matched for this dial peer.

Digits

Number of digits in this destination pattern matched for this dial peer.

Target

Matched session target (IP address or host name) for this dial peer.

### Related Commands

Command

Description

show dialplan in-carrier

Displays which VoIP or POTS dial peer is matched for a specific source carrier.

show dialplan in-trunk-group-label

Displays which VoIP or POTS dial peer is matched for a specific source trunk group.

show dialplan incall

Displays which POTS dial peer is matched for a specific calling number or voice port.

show dialplan number

Displays which dial peer is matched for a particular telephone number.

## show dialplan incall

To display which incoming POTS dial peer is matched for a specific calling number or voice port, use the show dialplan incall number command in privileged EXEC mode.

show dialplan incall voice-port number calling-number [ timeout ]

### Syntax Description

voice - port

Voice port location. The syntax of this argument is platform-specific. For information on the syntax for a particular platform,
                                          see the voice - port command.

calling - number

E.164 Calling number or ANI of the incoming voice call.

timeout

(Optional) Allows matching for variable-length destination patterns.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

11.3(1)T

This command was introduced on the Cisco 3600 series.

12.2(8)T

This command was implemented on the Cisco 1751, Cisco 2600 series, Cisco 3725, and Cisco 3745 and the timeout keyword was
                                          added.

### Usage Guidelines

Use this command as a troubleshooting tool to determine which POTS dial peer is matched for an incoming call, for the selected
                              calling number and voice port. The router attempts to match these items in the order listed:

Calling number with answer-address configured in dial peer

Calling number with destination-pattern configured in dial peer

Voice port with voice port configured in dial peer

The router first attempts to match a dial peer based on the calling number (ANI). If the router is unable to match a dial
                              peer based on the calling number, it matches the call to a POTS dial peer based on the selected voice interface. If more than
                              one dial peer uses the same voice port, the router selects the first matching dial peer. Use the timeout keyword to enable
                              matching variable-length destination patters associated with dial peers. This can increase you r chances of finding a match
                              for the dial peer number you specify.

For actual voice calls coming into the router, the router attempts to match the called number (the dialed number identification
                                          service [DNIS] number) with the incoming called-number configured in a dial peer. The router, however, does not consider the
                                          called number when using the show dialplan incall number command.

## Examples

The following sample output shows that an incoming call from interface 1/0/0:D with a calling number of 12345 is matched to
                              POTS dial peer 10:

```
Router# show dialplan incall 1/0/0:D number 12345 Macro Exp.: 12345
VoiceEncapPeer10
        information type = voice,
        tag = 10, destination-pattern = `123..',
        answer-address = `', preference=0,
        numbering Type = `unknown'
        group = 10, Admin state is up, Operation state is up,
        incoming called-number = `', connections/maximum = 0/unlimited,
        DTMF Relay = disabled,
        huntstop = disabled,
        in bound application associated: DEFAULT
        out bound application associated:
        permission :both
        incoming COR list:maximum capability
        outgoing COR list:minimum requirement
        type = pots, prefix = `',
        forward-digits default
        session-target = `', voice-port = `1/0/0:D',
        direct-inward-dial = disabled,
        digit_strip = enabled,
        register E.164 number with GK = TRUE
        Connect Time = 0, Charged Units = 0,
        register E.164 number with GK = TRUE
        Connect Time = 0, Charged Units = 0,
        Successful Calls = 0, Failed Calls = 0,
        Accepted Calls = 0, Refused Calls = 0,
        Last Disconnect Cause is "",
        Last Disconnect Text is "",
        Last Setup Time = 0.
Matched: 12345   Digits: 3
Target:
```

The following sample output shows that, if no dial peer has a destination pattern or answer address that matches the calling
                              number of 888, the incoming call is matched to POTS dial peer 99, because the call comes in on voice port 1/0/1:D, which is
                              the voice port configured for this dial peer:

```
Router# show dialplan incall 1/0/1:D number 888 Macro Exp.: 888
VoiceEncapPeer99
        information type = voice,
        tag = 99, destination-pattern = `99...',
        answer-address = `', preference=1,
        numbering Type = `national'
        group = 99, Admin state is up, Operation state is up,
        incoming called-number = `', connections/maximum = 0/unlimited,
        DTMF Relay = disabled,
        huntstop = disabled,
        in bound application associated: DEFAULT
        out bound application associated:
        permission :both
        incoming COR list:maximum capability
        outgoing COR list:minimum requirement
        type = pots, prefix = `5',
        forward-digits 4
        session-target = `', voice-port = `1/0/1:D',
        direct-inward-dial = enabled,
        digit_strip = enabled,
register E.164 number with GK = TRUE
        Connect Time = 0, Charged Units = 0,
        Successful Calls = 0, Failed Calls = 0,
        Accepted Calls = 0, Refused Calls = 0,
        Last Disconnect Cause is "",
        Last Disconnect Text is "",
        Last Setup Time = 0.
Matched:    Digits: 0
Target:
```

### Related Commands

Command

Description

show dialplan dialpeer

Displays which outbound dial peer is matched based upon the incoming dialed number and the COR criteria specified in the command
                                          line.

show dialplan in-carrier

Displays which VoIP or POTS dial peer is matched for a specific source carrier.

show dialplan in-trunk-group-label

Displays which VoIP or POTS dial peer is matched for a specific source trunk group.

show dialplan number

Displays which dial peer is matched for a particular telephone number.

## show dialplan incall uri

To display which dial peer is matched for a specific uniform resource identifier (URI) in an incoming voice call, use the show dialplan incall uri command in privileged EXEC mode.

### H.323 Session Protocol

show dialplan incall uri h323 { called | calling } uri

### SIP Session Protocol

show dialplan incall uri sip { from | request | to } uri

### Syntax Description

called

Voice class that is configured in dial peers with the incoming uri called command.

calling

Voice class that is configured in dial peers with the incoming uri calling command.

from

Voice class that is configured in dial peers with the incoming uri from command.

request

Voice class that is configured in dial peers with the incoming uri request command.

to

Voice class that is configured in dial peers with the incoming uri to command.

uri

URI of the incoming call.

### Command Default

No default behavior or values

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

Use this command for troubleshooting to determine which dial peer is matched for an incoming call, based on the selected
                                    URI and the specified field in the call message.

To set the URI format for matching calls, use the voice class uri command. To set the URI voice class in the inbound dial peer, use the incoming uri command.

## Examples

The following is sample output from this command for a SIP URI:

```
Router# show dialplan incall uri sip from sip:5551234 Inbound VoIP dialpeer matching based on SIP URI's
VoiceOverIpPeer10
        peer type = voice, information type = voice,
        description = `',
        tag = 10, destination-pattern = `',
        answer-address = `', preference=0,
        CLID Restriction = None
        CLID Network Number = `'
        CLID Second Number sent 
        source carrier-id = `', target carrier-id = `',
        source trunk-group-label = `',  target trunk-group-label = `',
        numbering Type = `unknown'
        group = 10, Admin state is up, Operation state is up,
        incoming called-number = `', connections/maximum = 0/unlimited,
        DTMF Relay = disabled,
        modem transport = system,
        URI classes:
            Incoming (Request) = 
            Incoming (To) = 
            Incoming (From) = 101
            Destination = 
        huntstop = disabled,
        in bound application associated: 'get_headers_tcl'
        out bound application associated: ''
        dnis-map = 
        permission :both
        incoming COR list:maximum capability
        outgoing COR list:minimum requirement
        Translation profile (Incoming):
        Translation profile (Outgoing):
        incoming call blocking:
        translation-profile = `'
        disconnect-cause = `no-service'
        type = voip, session-target = `',
        technology prefix: 
        settle-call = disabled
        ip media DSCP = ef, ip signaling DSCP = af31, UDP checksum = disabled,
        session-protocol = sipv2, session-transport = system, req-qos = best-ef 
        acc-qos = best-effort, 
        RTP dynamic payload type values: NTE = 101
        Cisco: NSE=100, fax=96, fax-ack=97, dtmf=121, fax-relay=122
               CAS=123, ClearChan=125, PCM switch over u-law=0,A-law=8
        RTP comfort noise payload type = 19
        fax rate = voice,   payload size =  20 bytes
        fax protocol = system
        fax-relay ecm enable
        fax NSF = 0xAD0051 (default)
        codec = g729r8,   payload size =  20 bytes,
        Expect factor = 0, Icpif = 20,
        Playout Mode is set to default,
        Initial 60 ms, Max 300 ms
        Playout-delay Minimum mode is set to default, value 40 ms 
        Fax nominal 300 ms
        Max Redirects = 1, signaling-type = ext-signal,
        VAD = enabled, Poor QOV Trap = disabled, 
        Source Interface = NONE
        voice class sip url = system,
        voice class sip rel1xx = system,
        voice class perm tag = `'
        Time elapsed since last clearing of voice call statistics never
        Connect Time = 0, Charged Units = 0,
        Successful Calls = 0, Failed Calls = 0, Incomplete Calls = 0
        Accepted Calls = 0, Refused Calls = 0,
        Last Disconnect Cause is "",
        Last Disconnect Text is "",
        Last Setup Time = 0.
Matched:    Digits: 0
Target:
```

The following is sample output from this command for a TEL URI:

```
Router# show dialplan incall uri h323 called tel:1234567 Inbound VoIP dialpeer matching based on H323 URI's
VoiceOverIpPeer25
        peer type = voice, information type = voice,
        description = `',
        tag = 25, destination-pattern = `',
        answer-address = `', preference=0,
        CLID Restriction = None
        CLID Network Number = `'
        CLID Second Number sent 
        source carrier-id = `', target carrier-id = `',
        source trunk-group-label = `',  target trunk-group-label = `',
        numbering Type = `unknown'
        group = 25, Admin state is up, Operation state is up,
        incoming called-number = `', connections/maximum = 0/unlimited,
        DTMF Relay = disabled,
        modem transport = system,
        URI classes:
            Incoming (Called) = 103
            Incoming (Calling) = 
            Destination = 
        huntstop = disabled,
        in bound application associated: 'callme'
        out bound application associated: ''
        dnis-map = 
        permission :both
        incoming COR list:maximum capability
        outgoing COR list:minimum requirement
        Translation profile (Incoming):
        Translation profile (Outgoing):
        incoming call blocking:
        translation-profile = `'
        disconnect-cause = `no-service'
        type = voip, session-target = `ipv4:10.10.1.1',
        technology prefix: 
        settle-call = disabled
        ip media DSCP = ef, ip signaling DSCP = af31, UDP checksum = disabled,
        session-protocol = cisco, session-transport = system, req-qos = best-ef 
        acc-qos = best-effort, 
        RTP dynamic payload type values: NTE = 101
        Cisco: NSE=100, fax=96, fax-ack=97, dtmf=121, fax-relay=122
               CAS=123, ClearChan=125, PCM switch over u-law=0,A-law=8
        RTP comfort noise payload type = 19
        fax rate = voice,   payload size =  20 bytes
        fax protocol = system
        fax-relay ecm enable
        fax NSF = 0xAD0051 (default)
        codec = g729r8,   payload size =  20 bytes,
        Expect factor = 0, Icpif = 20,
        Playout Mode is set to default,
        Initial 60 ms, Max 300 ms
        Playout-delay Minimum mode is set to default, value 40 ms 
        Fax nominal 300 ms
        Max Redirects = 1, signaling-type = ext-signal,
        VAD = enabled, Poor QOV Trap = disabled, 
        Source Interface = NONE
        voice class sip url = system,
        voice class sip rel1xx = system,
        voice class perm tag = `'
        Time elapsed since last clearing of voice call statistics never
        Connect Time = 0, Charged Units = 0,
        Successful Calls = 0, Failed Calls = 0, Incomplete Calls = 0
        Accepted Calls = 0, Refused Calls = 0,
        Last Disconnect Cause is "",
        Last Disconnect Text is "",
        Last Setup Time = 0.
Matched:    Digits: 0
Target:
```

The table below describes significant fields in the displays.

Field

Description

VoiceOverIpPeer

Dial peer associated with the calling number entered.

information type

Information type for this call; for example, voice or fax.

tag

Unique number that identifies the dial peer.

destination-pattern

Destination pattern (called number) configured for this dial peer.

answer-address

Answer address (calling number) configured for this dial peer.

preference

Hunt group preference order set for this dial peer.

Admin state

Administrative state of this dial peer.

Operation state

Operational state of this dial peer.

incoming called-number

Called number (DNIS) configured for this dial peer.

DTMF Relay

Whether the dtmf-relay command is enabled or disabled for this dial peer.

URI classes: Incoming (Request)

URI voice class used for matching dial peer to Request-URI in an incoming SIP Invite message.

URI classes: Incoming (To)

URI voice class used for matching dial peer to the To header in an incoming SIP Invite message.

URI classes: Incoming (From)

URI voice class used for matching dial peer to the From header in an incoming SIP Invite message.

URI classes: Destination

URI voice class used to match the dial peer to the destination URI for an outgoing call.

huntstop

Whether the huntstop command is enabled or disabled for this dial peer.

in bound application associated

IVR application that is associated with this dial peer when this dial peer is used for an inbound call leg.

out bound application associated

IVR application that is associated with this dial peer when this dial peer is used for an outbound call leg.

dnis-map

Name of the dialed-number identification service (DNIS) map that is configured in the dial peer with the dnis-map command.

permission

Configured permission level for this peer.

type

Type of dial peer (POTS or VoIP).

session-target

Configured session target (IP address or host name) for this dial peer.

session-protocol

Session protocol to be used for Internet calls between local and remote router via the IP backbone.

req-qos

Configured requested quality of service for calls for this dial peer.

acc-qos

Lowest acceptable quality of service configured for calls for this peer.

codec

Voice codec configured for this dial peer. Default is G.729 (8 kbps).

Expect factor

User-requested expectation factor of voice quality for calls through this peer.

Icpif

Configured calculated planning impairment factor (ICPIF) value for calls sent by a dial peer.

VAD

Whether voice activation detection (VAD) is enabled for this dial peer.

voice class sip url

URL format (SIP or TEL) used for SIP calls to this dial peer, as configured with the voice-class sip url command. The default is system, which means that the value configured globally with the url command in voice service VoIP SIP mode is used.

voice class sip rel1xx

Whether reliable provisional responses are supported, as configured with the voice-class sip rel1xx command. The default is system, which means that the value configured globally with the rel1xx command in voice service VoIP SIP mode is used.

voice class perm tag

Voice class for a trunk that is assigned to this dial peer with the voice-class permanent command.

Connect Time

Unit of measure indicating the call connection time associated with this dial peer.

Charged Units

Number of call units charged to this dial peer.

Successful Calls

Number of completed calls to this peer since system startup.

Failed Calls

Number of uncompleted (failed) calls to this peer since system startup.

Accepted Calls

Number of calls from this peer accepted since system startup.

Refused Calls

Number of calls from this peer refused since system startup.

Last Disconnect Cause

Encoded network cause associated with the last call. This value is updated whenever a call is started or cleared and depends
                                          on the interface type and session protocol being used on this interface.

Last Disconnect Text

ASCII text describing the reason for the last call termination.

Last Setup Time

Value of the System Up Time when the last call to this peer was started.

Matched

Destination pattern matched for this dial peer.

Target

Matched session target (IP address or host name) for this dial peer.

### Related Commands

Command

Description

debug voice uri

Displays debugging messages related to URI voice classes.

incoming uri

Specifies the voice class used to match a VoIP dial peer to the URI of an incoming call.

session protocol

Specifies the session protocol in the dial peer for calls between the local and remote router.

show dial-peer voice

Displays detailed and summary information about voice dial peers.

show dialplan uri

Displays which outbound dial peer is matched for a specific destination URI.

voice class uri

Creates or modifies a voice class for matching dial peers to calls containing a SIP or TEL URI.

voice class uri sip preference

Sets a preference for selecting voice classes for a SIP URI.

## show dialplan in-carrier

To display which incoming VoIP or POTS dial peer is matched for a specific source carrier or voice port, use the show dialplan in - carrier command in privileged EXEC mode.

show dialplan in-carrier carrier-id [ voip | pots ]

### Syntax Description

carrier - id

VoIP or POTS source carrier identifier.

voip

(Optional) Allows you to limit the search criteria to only VoIP dial peers.

pots

(Optional) Allows you to limit the search criteria to only POTS dial peers.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(13)T

This command was introduced on the Cisco 2600 series and Cisco 3600 series routers and on Cisco AS5300, Cisco AS5400, and
                                          Cisco AS5800 access servers.

### Usage Guidelines

Use this command as a troubleshooting tool to determine which VoIP or POTS dial peer is matched for an incoming call, based
                              on the carrier identifier specified in the command line. Use the voip or pots keywords to further limit the scope of possible
                              matches for the dial peer specified in the show dialplan command line.

## Examples

The following sample output shows a VoIP or POTS dial peer being matched to another POTS dial peer based on its carrier identifier,
                              "aaa":

```
Router# show dialplan in-carrier aaa pots
 Inbound pots dialpeer Matching based on source carrier-id
VoiceEncapPeer7777
        information type = voice,
        description = `',
        tag = 7777, destination-pattern = `',
        answer-address = `', preference=0,
        CLID Restriction = None
        CLID Network Number = `'
        CLID Second Number sent 
        source carrier-id = `aaa',      target carrier-id = `',
        source trunk-group-label = `',  target trunk-group-label = `',
        numbering Type = `unknown'
        group = 7777, Admin state is up, Operation state is up,
        incoming called-number = `', connections/maximum = 0/unlimited,
        DTMF Relay = disabled,
        huntstop = disabled,
        in bound application associated:'DEFAULT'
        out bound application associated:''
        dnis-map = 
        permission :both
        incoming COR list:maximum capability
        outgoing COR list:minimum requirement
        Translation profile (Incoming):
        Translation profile (Outgoing):
        incoming call blocking:
        translation-profile = `'
        disconnect-cause = `no-service'
voice-port = `'
        type = pots, prefix = `',
        forward-digits default
        session-target = `', up,
        direct-inward-dial = disabled,
        digit_strip = enabled,
        register E.164 number with GK = TRUE
        fax rate = system,   payload size =  20 bytes
        Time elapsed since last clearing of voice call statistics never
        Connect Time = 0, Charged Units = 0,
        Successful Calls = 0, Failed Calls = 0, Incomplete Calls = 0
        Accepted Calls = 0, Refused Calls = 0,
        Last Disconnect Cause is "",
        Last Disconnect Text is "",
        Last Setup Time = 0.
Matched:   Digits:0
Target:
```

### Related Commands

Command

Description

show dialplan dialpeer

Displays which outbound dial peer is matched based upon the incoming dialed number and the COR criteria specified in the command
                                          line.

show dialplan incall

Displays which POTS dial peer is matched for a specific calling number or voice port.

show dialplan in-trunk-group-label

Displays which VoIP or POTS dial peer is matched for a specific source trunk group.

show dialplan number

Displays which dial peer is matched for a particular telephone number.

## show dialplan in-trunk-group-label

To display which incoming VoIP or POTS dial peer is matched for a
                              		  specific trunk group label, use the show dialplan in - trunk - group - label command in privileged EXEC mode.

show dialplan in-trunk-group-label trunk-group-label { pots | voip }

### Syntax Description

trunk - group - label

VoIP or POTS source trunk group identifier.

voip

(Optional) Allows you to limit the search criteria to only
                                          						VoIP dial peers.

pots

(Optional) Allows you to limit the search criteria to only
                                          						POTS dial peers.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(13)T

This command was introduced on the Cisco 2600 series and
                                          						Cisco 3600 series routers and on Cisco AS5300, Cisco AS5400, and Cisco AS5800
                                          						access servers.

### Usage Guidelines

Use this command to determine which VoIP or POTS dial peer is matched
                              		  for an incoming call, based on the identifier of the source trunk group. The
                              		  router attempts to match these items in the order listed. Use the voip or pots
                              		  keywords to further limit the scope of possible matches for the dial peer
                              		  specified in the show dialplan command line.

## Examples

The following sample output shows an inbound VoIP or POTS dial peer
                              		  being matched to an outbound POTS dial peer based on the trunk group label
                              		  "NYtrunk":

```
Router# show dialplan in-trunk-group-label NYtrunk pots
 Inbound pots dialpeer Matching based on source trunk-group-label
VoiceEncapPeer2003
        information type = voice,
        description = `',
        tag = 2003, destination-pattern = `',
        answer-address = `', preference=0,
        CLID Restriction = None
        CLID Network Number = `'
        CLID Second Number sent 
        source carrier-id = `', target carrier-id = `',
        source trunk-group-label = `NYtrunk',   target trunk-group-label = `',
        numbering Type = `unknown'
        group = 2003, Admin state is up, Operation state is up,
        incoming called-number = `', connections/maximum = 0/unlimited,
        DTMF Relay = disabled,
        huntstop = disabled,
        in bound application associated:'debit-card'
        out bound application associated:''
        dnis-map = 
        permission :both
        incoming COR list:maximum capability
        outgoing COR list:minimum requirement
        Translation profile (Incoming):
        Translation profile (Outgoing):
        incoming call blocking:
        translation-profile = `'
        disconnect-cause = `no-service'
voice-port = `'
        type = pots, prefix = `',
        forward-digits default
        session-target = `', up,
        direct-inward-dial = disabled,
        digit_strip = enabled,
        register E.164 number with GK = TRUE
        fax rate = system,   payload size =  20 bytes
        Time elapsed since last clearing of voice call statistics never
        Connect Time = 0, Charged Units = 0,
        Successful Calls = 0, Failed Calls = 0, Incomplete Calls = 0
        Accepted Calls = 0, Refused Calls = 0,
        Last Disconnect Cause is "",
        Last Disconnect Text is "",
        Last Setup Time = 0.
Matched:   Digits:0
Target:
```

### Related Commands

Command

Description

show dialplan dialpeer

Displays which outbound dial peer is matched based upon the
                                          						incoming dialed number and the COR criteria specified in the command line.

show dialplan in-carrier

Displays which VoIP or POTS dial peer is matched for a
                                          						specific source carrier.

show dialplan incall

Displays which POTS dial peer is matched for a specific
                                          						calling number or voice port.

show dialplan number

Displays which dial peer is matched for a particular
                                          						telephone number.

## show dialplan number

To display which outgoing dial peer is reached when a particular telephone number is dialed, use the show dialplan number command in privileged EXEC mode.

show dialplan number dial-string [ carrier identifier ] [ fax | huntstop | voice ] [ timeout ]

### Syntax Description

dial - string

Particular destination pattern (E.164 telephone number).

carrier

(Optional) Indicates that you wish to base your search for applicable dial peers on the source carrier identifier.

identifier

(Optional) Source carrier identifier to accompany the carrier keyword.

fax

(Optional) Fax information type.

huntstop

(Optional) Terminates further dial-peer hunting upon encountering the first dial-string match.

timeout

(Optional) Allows matching for variable-length destination patterns.

voice

(Optional) Voice information type.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

11.3(1)T

This command was introduced on the Cisco 3600 series.

12.2(1)

The huntstop keyword was added.

12.2(8)T

This command was implemented on the Cisco 1751, Cisco 2600 series, Cisco 3725, and Cisco 3745 and the timeout keyword was
                                          added.

12.2(11)T

The carrier , fax , and voice keywords were added.

### Usage Guidelines

Use this command to test whether the dial plan configuration is valid and working as expected. Use the timeout keyword to
                              enable matching variable-length destination patters associated with dial peers. This can increase you r chances of finding
                              a match for the dial peer number you specify.

## Examples

The following is sample output from this command using a destination pattern of 1001:

```
Router# show dialplan number 1001 Macro Exp.: 1001
VoiceEncapPeer1003
         information type = voice,
         tag = 1003, destination-pattern = `1001',
         answer-address = `', preference=0,
         numbering Type = `unknown'
         group = 1003, Admin state is up, Operation state is up,
         incoming called-number = `', connections/maximum = 0/unlimited,
         DTMF Relay = disabled,
         huntstop = enabled,
         type = pots, prefix = `',
         forward-digits default
         session-target = `', voice-port = `1/1',
         direct-inward-dial = disabled,
         Connect Time = 0, Charged Units = 0,
         Successful Calls = 0, Failed Calls = 0, Incomplete Calls = 0
         Accepted Calls = 0, Refused Calls = 0,
         Last Disconnect Cause is "",
         Last Disconnect Text is "",
         Last Setup Time = 0.
Matched: 1001   Digits: 4
Target:
VoiceEncapPeer1004
         information type = voice,
         tag = 1004, destination-pattern = `1001',
         answer-address = `', preference=0,
         numbering Type = `unknown'
         group = 1004, Admin state is up, Operation state is up,
...
Matched: 1001   Digits: 4
Target:
VoiceEncapPeer1002
         information type = voice,
         tag = 1002, destination-pattern = `1001',
         answer-address = `', preference=0,
         numbering Type = `unknown'
         group = 1002, Admin state is up, Operation state is up,
...
Matched: 1001   Digits: 4
Target:
VoiceEncapPeer1001
         information type = voice,
         tag = 1001, destination-pattern = `1001',
         answer-address = `', preference=0,
         numbering Type = `unknown'
         group = 1001, Admin state is up, Operation state is up,
...
Matched: 1001   Digits: 4
Target:
```

The following is sample output from this command using a destination pattern of 1001 and the huntstop keyword:

```
Router# show dialplan number 1001 huntstop Macro Exp.: 1001
 VoiceEncapPeer1003
         information type = voice,
         tag = 1003, destination-pattern = `1001',
         answer-address = `', preference=0,
         numbering Type = `unknown'
         group = 1003, Admin state is up, Operation state is up,
         incoming called-number = `', connections/maximum = 0/unlimited,
         DTMF Relay = disabled,
         huntstop = enabled,
         type = pots, prefix = `',
         forward-digits default
         session-target = `', voice-port = `1/1',
         direct-inward-dial = disabled,
         Connect Time = 0, Charged Units = 0,
         Successful Calls = 0, Failed Calls = 0, Incomplete Calls = 0
         Accepted Calls = 0, Refused Calls = 0,
         Last Disconnect Cause is "",
         Last Disconnect Text is "",
         Last Setup Time = 0.
 Matched: 1001   Digits: 4
 Target:
```

### Related Commands

Command

Description

show dialplan dialpeer

Displays which outbound dial peer is matched based upon the incoming dialed number and the COR criteria specified in the command
                                          line.

show dialplan incall

Displays which POTS dial peer is matched for a specific calling number or voice port.

show dialplan in-carrier

Displays which VoIP or POTS dial peer is matched for a specific source carrier.

show dialplan in-trunk-group-label

Displays which VoIP or POTS dial peer is matched for a specific source trunk group.

## show dialplan uri

To display which outbound dial peer is matched for a specific destination uniform resource identifier (URI), use the show dialplan uri command in privileged EXEC mode.

show dialplan uri uri

### Syntax Description

uri

Destination Session Initiation Protocol (SIP) or telephone (TEL) URI for the outgoing call.

### Command Default

No default behavior or values

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

Use this command for troubleshooting to determine which dial peer is matched for an outgoing call, based on the selected URI.

To set the URI format used to match calls, use the voice class uri command. To set the URI voice class in the outbound dial peer, use the destination uri command.

## Examples

The following is sample output from this command:

```
Router# show dialplan uri sip:123456 Outbound dialpeer matching based on destination URI
VoiceOverIpPeer99
        peer type = voice, information type = voice,
        description = `',
        tag = 99, destination-pattern = `',
        answer-address = `', preference=0,
        CLID Restriction = None
        CLID Network Number = `'
        CLID Second Number sent 
        source carrier-id = `', target carrier-id = `',
        source trunk-group-label = `',  target trunk-group-label = `',
        numbering Type = `unknown'
        group = 99, Admin state is up, Operation state is up,
        incoming called-number = `', connections/maximum = 0/unlimited,
        DTMF Relay = disabled,
        modem transport = system,
        URI classes:
            Incoming (Request) = 
            Incoming (To) = 
            Incoming (From) = 
            Destination = 100
        huntstop = disabled,
        in bound application associated: 'DEFAULT'
        out bound application associated: ''
        dnis-map = 
        permission :both
        incoming COR list:maximum capability
        outgoing COR list:minimum requirement
        Translation profile (Incoming):
        Translation profile (Outgoing):
        incoming call blocking:
        translation-profile = `'
        disconnect-cause = `no-service'
        type = voip, session-target = `',
        technology prefix: 
        settle-call = disabled
        ip media DSCP = ef, ip signaling DSCP = af31, UDP checksum = disabled,
        session-protocol = sipv2, session-transport = system, req-qos = best-ef 
        acc-qos = best-effort, 
        RTP dynamic payload type values: NTE = 101
        Cisco: NSE=100, fax=96, fax-ack=97, dtmf=121, fax-relay=122
               CAS=123, ClearChan=125, PCM switch over u-law=0,A-law=8
        RTP comfort noise payload type = 19
        fax rate = voice,   payload size =  20 bytes
        fax protocol = system
        fax-relay ecm enable
        fax NSF = 0xAD0051 (default)
        codec = g729r8,   payload size =  20 bytes,
        Expect factor = 0, Icpif = 20,
        Playout Mode is set to default,
        Initial 60 ms, Max 300 ms
        Playout-delay Minimum mode is set to default, value 40 ms 
        Fax nominal 300 ms
        Max Redirects = 1, signaling-type = ext-signal,
        VAD = enabled, Poor QOV Trap = disabled, 
        Source Interface = NONE
        voice class sip url = system,
        voice class sip rel1xx = system,
        voice class perm tag = `'
        Time elapsed since last clearing of voice call statistics never
        Connect Time = 0, Charged Units = 0,
        Successful Calls = 0, Failed Calls = 0, Incomplete Calls = 0
        Accepted Calls = 0, Refused Calls = 0,
        Last Disconnect Cause is "",
        Last Disconnect Text is "",
        Last Setup Time = 0.
Matched:    Digits: 0
Target:
```

### Related Commands

Command

Description

debug voice uri

Displays debugging messages related to URI voice classes.

destination uri

Specifies the voice class used to match the dial peer to the destination URI for an outgoing call.

show dialplan incall uri

Displays which dial peer is matched for a specific URI in an incoming call.

voice class uri

Creates or modifies a voice class for matching dial peers to a SIP or TEL URI.

voice class uri sip preference

Sets a preference for selecting voice classes for a SIP URI.

## show dn-numbers

To display directory number information of Call Manager Express (CME), use the show dn-numbers command in user EXEC or privileged EXEC mode.

show dn-numbers

### Syntax Description

This command has no arguments or keywords.

### Command Modes

User EXEC (>) Privileged EXEC (#))

## Command History

Release

Modification

12.4(15)T

This command was introduced.

Cisco IOS XE Release 2.4

This command was integrated into Cisco IOS XE Release 2.4.

## Examples

The following is sample output from the show dn-numbers command:

```
Router# show dn-numbers Directory numbers                                                
 Entry          name                         number
 1             user1                         0 
 10            user2                         7890
 3             user3                         1234
 4             user4                         890 
 12            user5                         5676
 11            user6                         987 
 
 ephone directory numbers                                         
 DN             name                          number
 2              user7                         1000 
 4              user10                        34567 
 6              user11                        1234567891 
 10             user12                        1234567 
sip phone numbers                                                
 DN             name                           number
 1              user13                         10000 
 8              user14                         87953893 
 9              user15                         Not Configured
```

The table below describes the significant fields shown in the display.

Field

Description

DN

Directory number.

name

Name of the connection.

number

Telephone number.

## show dspfarm

To display digital signal processor (DSP) farm service information such as operational status and DSP resource allocation
                              for transcoding and conferencing, use the show dspfarm command in user EXEC or privileged EXEC mode.

show dspfarm [ all | dsp { active | all | idle | stats bridge-id [ sample seconds ]
                              
                              }
                              
                               | profile [profile-id] | sessions [session-id] | video { conference | statistics | transcode }
                              
                              ]

### Cisco ASR 1000 Series Router

show dspfarm { all | dsp { active | all | idle | stats bridge-id [ sample seconds ]
                              
                              }
                              
                               | profile [profile-identifier] }

### Syntax Description

all

(Optional) Displays all global information about the DSP farm service.

dsp

(Optional) Displays DSP information about the DSP farm service.

active

Displays active DSP information about the DSP farm service.

all

Displays all DSP information about the DSP farm service.

idle

Displays idle DSP information about the DSP farm service.

stats

Displays DSP statistics about the DSP farm service.

bridge-id

Displays the DSP statistics for a call bridge the specified bridge ID.

sample

(Optional) Displays statistics of the specified sample interval.

seconds

(Optional) The DSP sample interval time, in seconds.

profile

(Optional) Displays profiles about the DSP farm service.

profile-id

(Optional) The profile ID about the DSP farm service.

sessions

(Optional) Displays sessions and connections about the DSP farm service.

session-id

(Optional) The session identifier to be displayed for the DSP farm service.

video

(Optional) Displays information on video resources.

conference

(Optional) Displays the DSP information, such as the codecs, video bridge channel, and transmit (tx) and receive (rx) packets
                                          that are used for each participant in a conference and is grouped by conference sessions.

statistics

(Optional) Displays the DSP statistics of the call bridge.

transcode

(Optional) Displays the DSP status and statistics for the transcoding call.

### Command Modes

User EXEC (>)

Privileged EXEC (#)

## Command History

Release

Modification

Cisco IOS XE 17.18.2

This command was implemented on C8375-E-G2 router platform.

15.1(4)M

This command was modified. The video , conference , statistics , and transcode keywords were added.

Cisco IOS XE Release 3.2S

This command was implemented on the Cisco ASR 1000 Series Router.

12.4(15)T

The stats , sample , sessions , and profile keywords were added. The bridge-id , profile-id , seconds , and session-id arguments were added.

12.2(13)T

This command was implemented on the Cisco 2600 series, Cisco 3620, Cisco 3640, Cisco 3660, and Cisco 3700 series.

12.1(5)YH

This command was introduced on the Cisco VG200.

### Usage Guidelines

The router on which this command is used must be equipped with one or more digital T1/E1 packet voice trunk network modules
                              (NM-HDVs) or high-density voice (HDV) transcoding/conferencing DSP farms (NM-HDV-FARMs) to provide DSP resources.

Cisco ASR 1000 Series Router

The show dspfarm command is used to view the DSP farm service information such as operational status and DSP resource allocation
                              for transcoding.

The session keyword and session-id argument is not supported on Cisco ASR 1000 Series Router.

## Examples

The following is sample output from several forms of the show dspfarm command. The fields are self explanatory.

```
Router# show dspfarm DSPFARM Configuration Information:
Admin State: UP, Oper Status: ACTIVE - Cause code: NONE
Transcoding Sessions: 4, Conferencing Sessions: 0
RTP Timeout: 600
Router# show dspfarm all DSPFARM Configuration Information:
Admin State: UP, Oper Status: ACTIVE - Cause code: NONE
Transcoding Sessions: 4, Conferencing Sessions: 2
RTP Timeout: 1200
Connection average duration: 3600, Connection check interval 600
Codec G729 VAD: ENABLED
Total number of active session(s) 0, and connection(s) 0
SLOT  DSP   CHNL  STATUS USE   TYPE   SESS-ID   CONN-ID   PKTS-RXED PKTS-TXED
1     3     1     UP     FREE  conf   -         -         -         -
1     3     2     UP     FREE  conf   -         -         -         -
1     3     3     UP     FREE  conf   -         -         -         -
1     3     4     UP     FREE  conf   -         -         -         -
1     3     5     UP     FREE  conf   -         -         -         -
1     3     6     UP     FREE  conf   -         -         -         -
1     4     1     UP     FREE  conf   -         -         -         -
1     4     2     UP     FREE  conf   -         -         -         -
1     4     3     UP     FREE  conf   -         -         -         -
1     4     4     UP     FREE  conf   -         -         -         -
1     4     5     UP     FREE  conf   -         -         -         -
1     4     6     UP     FREE  conf   -         -         -         -
1     5     1     UP     FREE  xcode  -         -         -         -
1     5     2     UP     FREE  xcode  -         -         -         -
1     5     3     UP     FREE  xcode  -         -         -         -
1     5     4     UP     FREE  xcode  -         -         -         -
1     5     5     UP     FREE  xcode  -         -         -         -
1     5     6     UP     FREE  xcode  -         -         -         -
1     5     7     UP     FREE  xcode  -         -         -         -
1     5     8     UP     FREE  xcode  -         -         -         -
Total number of DSPFARM DSP channel(s) 20
Router# show dspfarm dsp all DSPFARM Configuration Information:
Admin State: UP, Oper Status: ACTIVE - Cause code: NONE
Transcoding Sessions: 4, Conferencing Sessions: 2
RTP Timeout: 1200
Connection average duration: 3600, Connection check interval 600
Codec G729 VAD: ENABLED
Total number of active session(s) 0, and connection(s) 0
SLOT  DSP  CHNL  STATUS  USE   TYPE   SESS-ID  CONN-ID  PKTS-RXED  PKTS-TXED
1     3    1     UP      FREE  conf   -        -        -          -
1     3    2     UP      FREE  conf   -        -        -          -
1     3    3     UP      FREE  conf   -        -        -          -
1     3    4     UP      FREE  conf   -        -        -          -
1     3    5     UP      FREE  conf   -        -        -          -
1     3    6     UP      FREE  conf   -        -        -          -
1     4    1     UP      FREE  conf   -        -        -          -
1     4    2     UP      FREE  conf   -        -        -          -
1     4    3     UP      FREE  conf   -        -        -          -
1     4    4     UP      FREE  conf   -        -        -          -
1     4    5     UP      FREE  conf   -        -        -          -
1     4    6     UP      FREE  conf   -        -        -          -
1     5    1     UP      FREE  xcode  -        -        -          -
1     5    2     UP      FREE  xcode  -        -        -          -
1     5    3     UP      FREE  xcode  -        -        -          -
1     5    4     UP      FREE  xcode  -        -        -          -
1     5    5     UP      FREE  xcode  -        -        -          -
1     5    6     UP      FREE  xcode  -        -        -          -
1     5    7     UP      FREE  xcode  -        -        -          -
1     5    8     UP      FREE  xcode  -        -        -          -
Total number of DSPFARM DSP channel(s) 20
```

## Examples

```
Router# show dspfarm sessions sess_id  conn_id  stype  mode      codec  pkt  ripaddr      rport  sport
4        145      xcode  sendrecv  g711a  20   10.10.10.19  19460  21284
4        161      xcode  sendrecv  g729   10   10.10.10.28  19414  20382
5        177      xcode  sendrecv  g711u  20   10.10.10.17  18290  21170
5        193      xcode  sendrecv  g729b  10   10.10.10.18  19150  18968
```

## Examples

The following output shows the active channels on the slots of C8375-E-G2 router platform:

```
Router# show dspfarm dsp active VDSP   DSP VERSION  STATUS CHNL USE   TYPE    RSC_ID BRIDGE_ID PKTS_TXED PKTS_RXED
 
     vDSP   1   1.0.827  UP     4    USED  xcode   1      24        0         0        
     vDSP   1   1.0.827  UP     4    USED  xcode   1      23        0         0        
        Total number of DSPFARM DSP channel(s) 1
```

## Examples

The following sample output displays dspfarm profiles for video conferencing and video transcoding:

```
Router# show dspfarm profile Profile ID = 1, Service = VIDEO CONFERENCING, Resource ID = 2  
 Video Conference Type : HOMOGENEOUS, Layout : disabled
 Profile Description :  
 Profile Service Mode : Non Secure 
 Profile Admin State : DOWN 
 Profile Operation State : DOWN 
 Application : SCCP   Status : NOT ASSOCIATED 
 Resource Provider : FLEX_DSPRM   Status : NONE 
 Number of Resource Configured : 1 
 Number of Resource Available : 0
 Maximum conference participants : 16
 Codec Configuration: num_of_codecs:6 
 Codec : g711ulaw, Maximum Packetization Period : 30 
 Codec : g711alaw, Maximum Packetization Period : 30 
 Codec : g729ar8, Maximum Packetization Period : 60 
 Codec : g729abr8, Maximum Packetization Period : 60 
 Codec : g729r8, Maximum Packetization Period : 60 
 Codec : g729br8, Maximum Packetization Period : 60 
 Video Codec Configuration:
 Codec : h263
   Resolution : cif
     Frame rate:30, Min bitrate:320kbps, Max bitrate:320kbps 
     Payload protocol : rfc-2190, Extension : annex-none
 Profile ID = 2, Service = VIDEO CONFERENCING, Resource ID = 3  
 Video Conference Type : HETEROGENEOUS, Layout : disabled
 Profile Description :  
 Profile Service Mode : Non Secure 
 Profile Admin State : UP 
 Profile Operation State : ACTIVE IN PROGRESS 
 Application : SCCP   Status : ASSOCIATION IN PROGRESS 
 Resource Provider : FLEX_DSPRM   Status : UP 
 Number of Resource Configured : 1 
 Number of Resource Available : 1
 Maximum conference participants : 4
 Maximum video ports : 4
 Codec Configuration: num_of_codecs:6 
 Codec : g729br8, Maximum Packetization Period : 60 
 Codec : g729r8, Maximum Packetization Period : 60 
 Codec : g729abr8, Maximum Packetization Period : 60 
 Codec : g729ar8, Maximum Packetization Period : 60 
 Codec : g711alaw, Maximum Packetization Period : 30 
 Codec : g711ulaw, Maximum Packetization Period : 30 
 Video Codec Configuration:
 Codec : h264
   Resolution : qcif
     Frame rate:15, Min bitrate:64kbps, Max bitrate:704kbps
     Frame rate:30, Min bitrate:64kbps, Max bitrate:704kbps
   Resolution : cif
     Frame rate:15, Min bitrate:64kbps, Max bitrate:704kbps
     Frame rate:30, Min bitrate:64kbps, Max bitrate:704kbps
 Codec : h263
   Resolution : qcif
     Frame rate:15, Min bitrate:64kbps, Max bitrate:704kbps
     Frame rate:30, Min bitrate:64kbps, Max bitrate:704kbps
   Resolution : cif
     Frame rate:15, Min bitrate:64kbps, Max bitrate:704kbps
     Frame rate:30, Min bitrate:64kbps, Max bitrate:704kbps
Dspfarm Profile Configuration
Profile ID = 3, Service =Universal TRANSCODING, Resource ID = 1                
 Profile Description :                                                          
 Profile Service Mode : Non Secure                                              
 Profile Admin State : DOWN                                                     
 Profile Operation State : DOWN                                                 
 Application : SCCP   Status : NOT ASSOCIATED                                   
 Resource Provider : FLEX_DSPRM   Status : NONE                                 
 Number of Resource Configured : 0                                              
 Number of Resource Available : 0                                               
 Codec Configuration: num_of_codecs:4                                           
 Codec : g711ulaw, Maximum Packetization Period : 30                            
 Codec : g711alaw, Maximum Packetization Period : 30                            
 Codec : g729ar8, Maximum Packetization Period : 60                             
 Codec : g729abr8, Maximum Packetization Period : 60
```

## Examples

The following sample output displays DSP information for video conferences:

```
Router# show dspfarm video conference VIDEO CONFERENCE SESSION: slot 0 dsp 3 channel_id 1 rsc_id 8 profile_id 101
 conferee_id 1  name_num:  62783363                                         
         audio_codec g711u     pkt_size 160  bridge_id 1        
         dsp_txed_pkts 25993     dsp_rxed_pkts 25888    
 conferee_id 1  name_num:  62783363                                         
         video_codec H264_VGA  rfc_number RFC3984 payload rx: 97   tx:97  
         framerate 30 bitrate(k) 960  annex 0x40   
         cluster_id 0  bridge_id 2         layout_id 0 
         dsp_txed_pkts 59230     dsp_rxed_pkts 63019    
 conferee_id 2  name_num:  62783365                                         
         audio_codec g711u     pkt_size 160  bridge_id 3        
         dsp_txed_pkts 21682     dsp_rxed_pkts 21598    
 conferee_id 2  name_num:  62783365                                         
         video_codec H264_4CIF rfc_number RFC3984 payload rx: 97   tx:97  
         framerate 30 bitrate(k) 960  annex 0x40   
         cluster_id 1  bridge_id 4         layout_id 0 
         dsp_txed_pkts 49488     dsp_rxed_pkts 78510    
 conferee_id 3  name_num:  3004                                             
         audio_codec g711u     pkt_size 160  bridge_id 5        
         dsp_txed_pkts 12130     dsp_rxed_pkts 12067    
 conferee_id 3  name_num:  3004                                             
         video_codec H264_CIF  rfc_number RFC3984 payload rx: 97   tx:97  
         framerate 30 bitrate(k) 704  annex 0x40   
         cluster_id 2  bridge_id 6         layout_id 0 
         dsp_txed_pkts 20354     dsp_rxed_pkts 25702    
 conferee_id 4  name_num: LifeSize LifeSize                                 
         audio_codec g711u     pkt_size 160  bridge_id 7        
         dsp_txed_pkts 1751      dsp_rxed_pkts 1672     
 conferee_id 4  name_num: LifeSize LifeSize                                 
         video_codec H264_4CIF rfc_number RFC3984 payload rx: 96   tx:96  
         framerate 30 bitrate(k) 1100 annex 0x40   
         cluster_id 1  bridge_id 8         layout_id 0 
         dsp_txed_pkts 3558      dsp_rxed_pkts 3569     
 cluster_id 0  video_codec H264_VGA  rfc_number RFC3984 rfc_payload 100 
         framerate 30 bitrate(k) 1000, annex 0x40  
 decoder_id 1  slot 0  dsp 13 codec h264 vga           cluster_id 0 
 encoder_id 1  slot 0  dsp 10 codec h264 vga           cluster_id 0 
 cluster_id 1  video_codec H264_4CIF rfc_number RFC3984 rfc_payload 100 
         framerate 30 bitrate(k) 1000, annex 0x40  
 decoder_id 1  slot 0  dsp 2  codec h264 4cif          cluster_id 1 
 encoder_id 1  slot 0  dsp 7  codec h264 4cif          cluster_id 1 
 cluster_id 2  video_codec H264_CIF  rfc_number RFC3984 rfc_payload 100 
         framerate 30 bitrate(k) 704 , annex 0x40  
 decoder_id 1  slot 0  dsp 15 codec h264 cif           cluster_id 2 
 encoder_id 1  slot 0  dsp 14 codec h264 cif           cluster_id 2 
Total number of DSPFARM DSP channel(s) 1
```

## Examples

The following sample output displays the statistics for a call that uses video transcoding:

```
Router# show dspfarm dsp stats Gathering total stats...
Video Statistics for bridge_id=3 call_id=2
 Video Decoder Statistics:
  Slot=0  DSP_Id=8  Decoder_Id=1
  CallDuration=268  Codec=1  ProfileId=0x0  LevelId=0
  PicWidth=352  PicHeight=288  FrameRate=30  Bitrate=360000
  NumMacroBlocksConcealed=0  NumFramesConcealed=0
  NumPackets=13269  NumBytesConsumed=12096254
  NumBadHeaderPackets=0  NumOutOfSyncPackets=24
  NumBufferOverflow=0
 Video Encoder Statistics:
  Slot=0  DSP_Id=2  Encoder_Id=1
  Duration=268  Codec=1  ProfileId=0x0  LevelId=0
  PicWidth=176  PicHeight=144  FrameRate=30  Bitrate=704000
  InstantBitrate=440000  NumPackets=17571  NumBytesGenerated=14830996
```

## Examples

The following sample output displays the statistics for a video conference:

```
Router# show dspfarm dsp stats Gathering total stats...
Video Statistics for bridge_id=3 call_id=4
 Video Conferee Status - ConfereeID=1
  ContributionState=0x1  IngressMute=0  EgressMute=0
  DtmfRtpPlt=0  ClusterId=1  StreamDir=3
  PayloadType=0x6161  TxSSRC=0x1F3C  RtpProtocol=2
  CodecType=2  Annex=0x0  PicWidth=352  PicHeight=288
  FrameRate=30  Bitrate(x100)=3760
 Video Conferee Statistics - ConfereeID=1
  TotalRxPackets=5076  TotalRxBytes=3957126
  TotalTxPackets=3829  TotalTxBytes=3429797
  TotalDroppedPackets=3  CurDroppedPackets=0
  TotalOutOfOrderPackets=0  CurOutOfOrderPackets=0
  MaxObservedJitter=0  CurObservedJitter=0
  MaxObservedDelay=0  CurObservedDelay=0
  MaxOutOfSyncDelay=0  CurOutOfSyncDelay=0
  ActualFrameRate=0  ActualBitrate(x100)=2017
  FastVideoUpdateRate=0  TotalDuration=135
 Video Conference Status:
  ServiceType=0  MuteAllStatus=0
  CurSpeakerConfereeId=1  LastSpeakerConfereeId=3  NewSpeakerConfereeId=0
  ConfereeIdBitMap=0x07
 Video Conference Statistics:
  NumActiveChans=3  NumMaxChans=1
  TotalRxPackets=42589  TotalRxBytes=29979147
  TotalTxPackets=12361  TotalTxBytes=10003701
  TotalDroppedPackets=3  CurDroppedPackets=0
  TotalOutOfOrderPackets=0  CurOutOfOrderPackets=0
  MaxObservedJitter=0  CurObservedJitter=0
  MaxObservedDelay=0  CurObservedDelay=0
MaxOutOfSyncDelay=0  CurOutOfSyncDelay=0
```

## Examples

The following is a sample output of the show dspfarm all command on Cisco ASR 1000 Series Router:

```
Router# show dspfarm all Dspfarm Profile Configuration
 Profile ID = 1, Service = TRANSCODING, Resource ID = 1
 Profile Description :
 Profile Service Mode : Non Secure
 Profile Admin State : UP
 Profile Operation State : ACTIVE
 Application : SBC   Status : ASSOCIATED
 Resource Provider : FLEX_DSPRM   Status : UP
 Number of Resources Configured : 588
 Number of Resources Out of Service : 0
 Codec Configuration
 Codec : g711ulaw, Maximum Packetization Period : 30
 Codec : g711alaw, Maximum Packetization Period : 30
 Codec : g729ar8, Maximum Packetization Period : 60
 Codec : g729abr8, Maximum Packetization Period : 60
SLOT DSP VERSION  STATUS CHNL USE   TYPE    RSC_ID BRIDGE_ID
5    1   26.7.0   UP     N/A  FREE  xcode  1      -         -         -
5    1   26.7.0   UP     N/A  FREE  xcode  1      -         -         -
5    1   26.7.0   UP     N/A  FREE  xcode  1      -         -         -
5    1   26.7.0   UP     N/A  FREE  xcode  1      -         -         -
5    1   26.7.0   UP     N/A  FREE  xcode  1      -         -         -
```

## Examples

The following is a sample output of the show dspfarm dsp idle command providing idle DSP information on Cisco ASR 1000 Series Router:

```
Router# show dspfarm dsp idle SLOT DSP VERSION  STATUS CHNL USE   TYPE    RSC_ID BRIDGE_ID
5    1   26.7.0   UP     N/A  FREE  xcode  1      -         -         -
5    1   26.7.0   UP     N/A  FREE  xcode  1      -         -         -
5    1   26.7.0   UP     N/A  FREE  xcode  1      -         -         -
5    1   26.7.0   UP     N/A  FREE  xcode  1      -         -         -
5    1   26.7.0   UP     N/A  FREE  xcode  1      -         -         -
5    1   26.7.0   UP     N/A  FREE  xcode  1      -         -         -
5    1   26.7.0   UP     N/A  FREE  xcode  1      -         -         -
5    1   26.7.0   UP     N/A  FREE  xcode  1      -         -         -
5    1   26.7.0   UP     N/A  FREE  xcode  1      -         -         -
5    1   26.7.0   UP     N/A  FREE  xcode  1      -         -         -
```

## Examples

The following is sample output of the show dspfarm profile 1 command providing DSP Farm profile configuration details such as application association, number of resources configured,
                              Codecs added, and maximum number of sessions for profile 1 on Cisco ASR 1000 Series Router.

```
Router# show dspfarm profile 1 Dspfarm Profile Configuration
 Profile ID = 1, Service = TRANSCODING, Resource ID = 1
 Profile Description :
 Profile Service Mode : Non Secure
 Profile Admin State : UP
 Profile Operation State : ACTIVE
 Application : SBC   Status : ASSOCIATED
 Resource Provider : FLEX_DSPRM   Status : UP
 Number of Resources Configured : 588
 Number of Resources Out of Service : 0
 Codec Configuration
 Codec : g711ulaw, Maximum Packetization Period : 30
 Codec : g711alaw, Maximum Packetization Period : 30
 Codec : g729ar8, Maximum Packetization Period : 60
 Codec : g729abr8, Maximum Packetization Period : 60
Router#show dspfarm profile ?
  <1-65535>  Profile ID
  |          Output modifiers
  <cr>
```

### Related Commands

Command

Description

dspfarm (DSP farm)

Enables DSP-farm service.

## show dspfarm profile

To display configured digital signal processor (DSP) farm profile information for a selected Cisco CallManager group, use
                              the show dspfarm profile command in privileged EXEC mode.

show dspfarm profile [profile-identifier]

### Syntax Description

profile ide ntifier

(Optional) Number that uniquely identifies a profile. Range is from 1 to 65535. There is no default.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

### Usage Guidelines

Use the show dspfarm profile command to verify that the association between Skinny Client Control Protocol (SCCP) Cisco Unified CallManager and the DSP
                              farm profiles match your organizational plan.

The output of the show dspfarm profile command differs depending on the services configured in the profile.

## Examples

```
The following is sample output from the show dspfarm profile command:
Router# show dspfarm profile Dspfarm Profile Configuration
 Profile ID = 6, Service = TRANSCODING, Resource ID = 1   
 Profile Description :  
 Profile Service Mode : Non Secure 
 Profile Admin State : UP 
 Profile Operation State : ACTIVE 
 Application : SCCP   Status : ASSOCIATED 
 Resource Provider : FLEX_DSPRM   Status : UP 
 Number of Resource Configured : 4 
 Number of Resource Available : 4
 Codec Configuration 
 Codec : g711ulaw, Maximum Packetization Period : 30 
 Codec : g711alaw, Maximum Packetization Period : 30 
 Codec : g729ar8, Maximum Packetization Period : 60 
 Codec : g729abr8, Maximum Packetization Period : 60 
 Codec : g729br8, Maximum Packetization Period : 60 
 RSVP : ENABLED 
 TRP : FW-TRAVERSAL ENABLED 
Dspfarm Profile Configuration
 Profile ID = 27, Service = CONFERENCING, Resource ID = 2  
 Profile Description :  
 Profile Service Mode : Non Secure 
 Profile Admin State : UP 
 Profile Operation State : ACTIVE 
 Application : SCCP   Status : ASSOCIATED 
 Resource Provider : FLEX_DSPRM   Status : UP 
 Number of Resource Configured : 6
 Number of Resource Available : 6
 Codec Configuration
 Codec : g711alaw, Maximum Packetization Period : 30 
 Codec : g729ar8, Maximum Packetization Period : 60
Dspfarm Profile Configuration
 Profile ID = 34, Service = MTP, Resource ID = 1  
 Profile Description :  
 Profile Service Mode : secure 
 Profile Admin State : UP 
 Profile Operation State : ACTIVE 
 Application : SCCP   Status : ASSOCIATED 
 Resource Provider : NONE   Status : UP 
 Number of Resource Configured : 2 
 Number of Resource Available : 2
 Hardware Configured Resources : 1
 Hardware Available Resources : 1
 Software Resources : 1
 Codec Configuration 
 Codec : g711ulaw, Maximum Packetization Period : 30
 TRP : FW-TRAVERSAL ENABLED
```

The table below describes the significant fields shown in the display.

Field

Description

Profile ID

Displays the profile ID number.

Service

Displays the service that is associated with the profile.

Resource ID

Displays the ID number that the profile is associated with in the Cisco CallManager register.

Profile Description

Displays the description of the profile.

Profile Service Mode

The status of the profile service. It can be either Secure or Non Secure.

Profile Admin State

Displays the status of the profile. If the Profile Admin State is DOWN, use the no shutdown command in DSP farm profile configuration mode.

Profile Operation State

Displays the status of the DSP farm profiles registration process with the Cisco CallManager. Status options are as follows:

ACTIVE--The profile is registered with the Cisco Unified CallManager.

ACTIVE IN PROGRESS--The profile is still registering with the Cisco Unified CallManager. Wait for the profile to finish registering.

DOWN--The profile is not registering with the Cisco Unified CallManager. Check the connectivity between the DSP farm gateway
                                                and the Cisco Unified CallManager.

DOWN IN PROGRESS--The profile is deregistering from the Cisco Unified CallManager and deallocating the DSP resources.

RESOURCE ALLOCATED--The DSP resources for this profile are allocated or reserved.

Application

Displays the routing protocol used.

Number of Resource Configured

Maximum number of sessions that are supported by a profile.

Number of Resource Available

Total number of resources that are configurable.

Hardware Configured Resources

Number of sessions configured in the profile.

Hardware Available Resources

Number of sessions available for this profile.

Software Resources

Number of software sessions configured for this profile (applicable only to MTP profiles).

Codec Configuration

Lists the codecs that are configured.

Media Termination Point (MTP) profile supports only one codec per profile.

RSVP

Resource Reservation Protocol (RSVP) support for this profile.

TRP

Displays whether firewall traversal is enabled for Trusted Relay Point.

### Related Commands

Command

Description

dsp services dspfarm

Configures DSP farm services for a specified voice card.

dspfarm profile

Enters DSP farm profile configuration mode and defines a profile for DSP farm services.

show media resource status

Displays the current media resource status.

## show dsp-group

To display digital signal processor (DSP) group information including both voice and video information, use the show dsp-group command in user EXEC or privileged EXEC mode.

show dsp-group { all | slot slot-number | video [ all | slot slot-number ] | voice [ all | slot slot-number ]}

### Syntax Description

all

Displays DSP information for all DSP group.

slot

Displays DSP information for the specified slot.

slot-number

Slot used in the DSP group.

video

Displays information on video resources.

voice

Displays information on voice resources.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release

Modification

15.1(4)M

This command was introduced.

### Usage Guidelines

The router on which this command is used must be equipped with one or more digital T1/E1 packet voice trunk network modules
                              (NM-HDVs), high-density voice (HDV) transcoding/conferencing DSP farms (NM-HDV-FARMs), or packet voice data module (PVDM)
                              slots to provide DSP resources.

## Examples

The following shows sample output from several forms of the show dsp-group command. The fields are self explanatory.

```
Router# show dsp-group all DSP groups on slot 0:
dsp 1:
  State: UP, firmware: 28.0.103
  Max signal/voice channel: 32/32
  Max credits: 480, Voice credits: 0, Video credits: 480
  num_of_sig_chnls_allocated: 32
  Transcoding channels allocated: 0
  Group: FLEX_GROUP_VIDEO_POOL, complexity: FLEX
    Video Credits Max: 480, Share: 0, Reserved (rounded-up): 480
    Video Group: VIDEO_CONF, rsc id: 2, mode: VCONF_HETE
      Session: 0, maximum participants: 4
        Video Transcoding channels reserved credits: 480
        Video Transcoding channels allocated: 1
          Encoder: inactive, credit reserved: 480
  Slot: 0
  Device idx: 0
  PVDM Slot: 0
  Dsp Type: SP2600
dsp 2:
  State: UP, firmware: 28.0.103
  Max signal/voice channel: 32/32
  Max credits: 480, Voice credits: 0, Video credits: 480
  num_of_sig_chnls_allocated: 32
  Transcoding channels allocated: 0
  Group: FLEX_GROUP_VIDEO_POOL, complexity: FLEX
    Video Credits Max: 480, Share: 0, Reserved (rounded-up): 480
    Video Group: VIDEO_CONF, rsc id: 2, mode: VCONF_HETE
      Session: 0, maximum participants: 4
        Video Transcoding channels reserved credits: 480
        Video Transcoding channels allocated: 3
          Decoder: inactive, credits reserved: 160
          Decoder: inactive, credits reserved: 160
          Decoder: inactive, credits reserved: 160
  Slot: 0
  Device idx: 0
  PVDM Slot: 0
  Dsp Type: SP2600
DSP groups on slot 1:
 This command is not applicable to slot 1
DSP groups on slot 2:
 This command is not applicable to slot 2
DSP groups on slot 3:
 This command is not applicable to slot 3
```

### Related Commands

Command

Description

dsp service dspfarm

Configures DSP farm services for a specified voice card.

dspfarm (DSP farm)

Enables DSP-farm service.

voice service dsp-reservation

Configures the percentage of DSP resources are reserved for voice services and enables video services to use the remaining
                                          DSP resources.

This command is required to enable video services.

voice-card

Enters voice-card configuration mode.

## show echo-cancel

To display the echo-cancellation information of T1/E1 multiflex voice/WAN interface cards, use the show echo-cancel command in privileged EXEC mode.

show echo-cancel hardware status slot-number

### Syntax Description

hardware

Displays information about the hardware accelerated EC device.

status

Displays the allocation status.

slot-number

The slot number of the interface cards.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.4(24)T

This command was introduced in a release earlier than Cisco IOS Release 12.4(24)T.

### Usage Guidelines

Hardware echo cancellation is restricted to the same baseboard voice/WAN interface card (VWIC) on which the daughter card
                              (EC-MFT-32 and EC-MFT-64) is installed and cannot be shared by other T1/E1 controllers.

## Examples

The following is sample output from the show echo-cancel hardware status command:

```
Router# show echo-cancel hardware status ECAN CH   Assigned   DSP ID   VOICEPORT   EC   NLP   COV  LAW
===============================================================
   0          yes       8       1/0/0      on   off   on   u-Law
   1          no        -          -       off  on    on   u-Law
   2          no        -          -       off  on    on   u-Law
   3          no        -          -       off  on    on   u-Law
   4          no        -          -       off  on    on   u-Law
   5          no        -          -       off  on    on   u-Law
```

The table below describes the significant fields shown in the display.

Field

Description

ECAN CH

Total channels in the slot.

Assigned

Status of the assigned channels.

DSP ID

Digital Signaling Processor (DSP) identification number for the assigned channels.

VOICEPORT

Voice port of the channels.

EC

Echo Cancellation status of the assigned channels.

NLP

Status of the Non-Linear Processor (NLP).

COV

Echo cancellation Coverage status of the assigned channels.

## show event-manager consumers

To display event-manager statistics for debugging purposes, use the show event-manager consumers command in privileged EXEC mode.

show event-manager consumers

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Release

Modification

12.3(4)T

This command was introduced.

## Examples

The following example shows one call (two call legs) going through the gateway:

```
Router# show event-manager consumers Hash table indexed by AAA_UNIQUE_ID
Uid        Consumer_id  Consumer_hdl  evt_type
00000015   0002         65B35570      START
00000015   0002         65B35570      STOP
00000016   0002         65B34ECC      START
00000016   0002         65B34ECC      STOP
```

The table below lists and describes the significant output fields.

Field

Description

Uid

User ID.

Consumer_id

ID of the consumer client process.

Consumer_hdl

Handler of the consumer client process.

evt_type

Event type.

### Related Commands

Command

Description

show voice statistics csr interval accounting

Displays all accounting CSRs specified by interval number.

show voice statistics csr interval aggregation

Displays signaling CSRs specified by interval number.

show voice statistics csr since-reset accounting

Displays all accounting CSRs since the last reset.

show voice statistics csr since-reset aggregation-level

Displays all signaling CSRs since the last reset.

show voice statistics csr since-reset all

Displays all CSRs since the last reset.

show voice statistics interval-tag

Displays the configured interval numbers.

show voice statistics memory-usage

Displays current memory usage.

## show frame-relay vofr

To display information about the FRF.11 subchannels being used on Voice over Frame Relay (VoFR) data link connection identifiers
                              (DLCIs), use the show frame - relay vofr command in privileged EXEC mode.

show frame-relay vofr [ interface [ dlci [cid] ]]

### Syntax Description

interface

(Optional) Specific interface type and number for which you want to display FRF.11 subchannel information.

dlci

(Optional) Specific data link connection identifier for which you want to display FRF.11 subchannel information.

cid

(Optional) Specific subchannel for which you want to display information.

### Command Default

If this command is entered without a specified interface, FRF.11 subchannel information is displayed for all VoFR interfaces
                              and DLCIs configured on the router.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.0(4)T

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810 series.

## Examples

The following is sample output from this command when an interface is not specified:

```
Router# show frame-relay vofr
interface         vofr-type   dlci   cid   cid-type
Serial0/0.1       VoFR        16     4     data
Serial0/0.1       VoFR        16     5     call-control
Serial0/0.1       VoFR        16     10    voice
Serial0/1.1       VoFR cisco  17     4     data
```

The following is sample output from this command when an interface is specified:

```
Router# show frame-relay vofr serial0
interface         vofr-type   dlci   cid   cid-type
Serial0           VoFR        16     4     data
Serial0           VoFR        16     5     call-control
Serial0           VoFR        16     10    voice
```

The following is sample output from this command when an interface and a DLCI are specified:

```
Router# show frame-relay vofr serial0 16
VoFR Configuration for interface Serial0
dlci vofr-type  cid cid-type          input-pkts    output-pkts   dropped-pkts
16   VoFR       4   data              0             0             0
16   VoFR       5   call-control      85982         86099         0
16   VoFR       10  voice             2172293       6370815       0
```

The following is sample output from this command when an interface, a DLCI, and a CID are specified:

```
Router# show frame-relay vofr serial0 16 10
VoFR Configuration for interface Serial0 dlci 16
  vofr-type  VoFR     cid 10      cid-type voice
  input-pkts 2172293   output-pkts 6370815   dropped-pkts 0
```

The table below describes significant fields shown in this output.

Field

Description

interface

Number of the interface that has been selected for observation of FRF.11 subchannels.

vofr-type

Type of VoFR DLCI being observed.

cid

Portion of the specified DLCI that is carrying the designated traffic type. A DLCI can be subdivided into 255 subchannels.

cid-type

Type of traffic carried on this subchannel.

input-pkts

Number of packets received by this subchannel.

output-pkts

Number of packets sent on this subchannel.

dropped-pkts

Total number of packets discarded by this subchannel.

### Related Commands

Command

Description

show call active voice

Displays the contents of the active call table.

show call history voice

Displays the contents of the call history table.

show dial-peer voice

Displays configuration information and call statistics for dial peers.

show frame-relay fragment

Displays Frame Relay fragmentation details.

show frame-relay pvc

Displays statistics about PVCs for Frame Relay interfaces.

show voice-port

Displays configuration information about a specific voice port.

## show gatekeeper calls

To display the status of each ongoing call of which a gatekeeper is aware, use the show gatekeeper calls command in privileged EXEC mode.

show gatekeeper calls [ history ]

### Syntax Description

history

(Optional) Displays call history information along with internal error codes at the gatekeeper. The number of disconnected
                                          calls displayed in response to this command is the number specified in the call-history max-size number command. Use of this max-size number helps to reduce CPU usage in the storage and reporting of this information.

### Command Default

The default expression of this command displays information for all active calls detected on the gatekeeper.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

11.3(2)NA

This command was introduced.

12.0(3)T

This command was integrated into Cisco IOS Release 12.0(3)T.

12.0(5)T

The output for this command was changed.

12.1(5)XM2

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(4)T

Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400 is not included in this release.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T. This command is supported on the Cisco AS5300, Cisco AS5350,
                                          Cisco AS5400, and Cisco AS5850 in this release.

12.4(4)T

The history keyword was added to display historical information on disconnected calls.

### Usage Guidelines

Use this command to show all active calls currently being handled by a particular Multimedia Conference Manager (MCM) gatekeeper.
                              If you force a disconnect for either a particular call or all calls associated with a particular MCM gatekeeper by using the clear h323 gatekeeper call command, the system does not display information about those calls.

Using the history keyword displays the number of disconnected calls specified in the call-history max-size number command. Use of this max-size number helps to reduce CPU usage in the storage and reporting of this information.

## Examples

The following is sample output showing active calls:

```
Router# show gatekeeper calls
Total number of active calls = 1.
                         GATEKEEPER CALL INFO
                         ====================
LocalCallID                        Age(secs)   BW
12-3339                            94          768(Kbps)
 Endpt(s):Alias        E.164Addr     CallSignalAddr  Port  RASSignalAddr   Port
   src EP:epA                        10.0.0.0        1720  10.0.0.0        1700
   dst EP:epB@zoneB.com
   src PX:pxA                        10.0.0.0        1720  10.0.0.00       24999
   dst PX:pxB                        255.255.255.0   1720  255.255.255.0   24999
```

The table below describes the significant fields shown in the display.

Field

Description

LocalCallID

Identification number of the call.

Age(secs)

Age of the call, in seconds.

BW(Kbps)

Bandwidth in use, in kilobytes per second.

Endpt

Role of each endpoint (terminal, gateway, or proxy) in the call (originator, target, or proxy) and the call signaling and
                                          Registration, Admission, and Status (RAS) protocol address.

Alias

H.323-Identification (ID) or Email-ID of the endpoint.

E.164Addr

E.164 address of the endpoint.

CallSignalAddr

Call-signaling IP address of the endpoint.

Port

Call-signaling port number of the endpoint.

RASSignalAddr

RAS IP address of the endpoint.

Port

RAS port number of the endpoint.

### Related Commands

Command

Description

clear h323 gatekeeper call

Forces the disconnection of a specific call or of all calls active on a particular gatekeeper.

call history max

Specifies the number of records to be kept in the history table.

## show gatekeeper circuits

To display the circuit information on a gatekeeper, use the show gatekeeper circuits command in privileged EXEC mode.

show gatekeeper circuits [ { begin | exclude | include } expression ]

### Syntax Description

begin

(Optional) Displays all circuits, beginning with the line containing the expression.

exclude

(Optional) Displays all circuits, excluding those containing the expression.

include

(Optional) Displays all circuits, including those containing the expression.

expression

(Optional) Word or phrase used to determine what lines are displayed.

### Command Default

Shows all circuit information.

### Command Modes

Privileged EXEC

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

Use this command to display current configuration information about the circuits that are registered with the gatekeeper.

## Examples

The following command displays the circuit information for the gatekeeper:

```
Router# show gatekeeper circuits Circuit       Endpoint   Max Calls Avail Calls Resources     Zone
-------       --------   --------- ----------- ---------     ----
CarrierA      Total Endpoints: 2
              3640-gw1   25        25          Available
              5400-gw1   23        19          Unavailable
CarrierB      Total Zones: 1
                                                             MsPacmanGK
```

The table below describes the fields shown in this output.

Field

Description

Circuit

Name of the each circuit connected to the gatekeeper.

Endpoint

Name of each H.323 endpoint.

Max Calls

Maximum number of calls that circuit can handle.

Avail Calls

Number of new calls that the circuit can handle at the current time.

Resources

Whether the circuit’s resources have exceeded the defined threshold limits. The endpoint resource - threshold command defines these thresholds.

Zone

Zone that supports the endpoint. The zone circuit - id command assigns a zone to an endpoint.

Total Endpoints

Total number of endpoints supported by the circuit.

Total Zones

Total number of zones supported by the circuit.

### Related Commands

Command

Description

endpoint resource-threshold

Sets a gateway’s capacity thresholds in the gatekeeper.

zone circuit-id

Assigns a remote zone to a carrier.

## show gatekeeper cluster

To display all the configured gatekeeper clusters information, use the show gatekeeper cluster command in user EXEC or privileged EXEC mode.

show gatekeeper cluster

### Syntax Description

This command has no arguments or keywords.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release1.25

Modification

12.1(5)XM

This command was introduced.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T.

12.2(2)XB1

This command was integrated into Cisco IOS Release 12.2(2)XB1 and implemented on the Cisco AS5850 router.

## Examples

The following is sample output from the show gatekeeper cluster command. Field descriptions are self-explanatory.

```
Router# show gatekeeper cluster CONFIGURED CLUSTERS
                    ===================
Cluster Name    Type     Local Zone   Elements  IP
------------    ----     ----------   --------  --
Cluster A       Local    AGK1         AGK2      192.168.200.254 1719
                                      AGK3      192.168.200.223 1719
Cluster B       Remote                BGK1      192.168.200.257 1719
                                      BGK2      192.168.200.258 1719
                                      BGK3      192.168.200.259 1719
```

### Related Commands

Command

Description

show gatekeeper endpoints

Displays the status of all registered endpoints for a gatekeeper.

show gatekeeper performance stats

Displays the performance statistics on the the gatekeeper level message.

show gatekeeper zone cluster

Displays the dynamic status of all local clusters.

## show gatekeeper endpoint circuits

To display information on all registered endpoints and carriers or trunk groups for a gatekeeper, use the show gatekeeper endpoint circuits command in privileged EXEC mode.

show gatekeeper endpoint circuits [ { begin | exclude | include } expression ]

### Syntax Description

| begin

(Optional) Displays all circuits, beginning with the line that contains expression.

| exclude

(Optional) Displays all circuits, excluding those that contain expression.

| include

(Optional) Displays all circuits, including those that contain expression.

expression

(Optional) Word or phrase used to determine what lines are displayed.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

11.3(2)NA

This command was introduced.

12.0(5)T

The display format was modified for H.323 Version 2.

12.2(11)T

The display format was modified to show the E.164 ID, carrier and trunk group data, and total number of active calls.

### Usage Guidelines

Use this command to display current configuration information about the endpoints and carriers registered with the gatekeeper.
                              Note that you must type the pipe (|) before any of the optional keywords.

## Examples

The following command displays the circuit information for the gatekeeper:

```
Router# show gatekeeper endpoint circuits GATEKEEPER ENDPOINT REGISTRATION
                    ================================
CallSignalAddr  Port  RASSignalAddr   Port  Zone Name         Type    Flags
--------------- ----- --------------- ----- ---------         ----    -----
172.18.195.120  1720  172.18.195.120  51059 LavenderGK        VOIP-GW
    E164-ID: 4081234
    H323-ID: 3640-gw1
    Carrier: CarrierA, Max Calls: 25, Available: 25
172.18.197.143  1720  172.18.197.143  57071 LavenderGK        VOIP-GW
    H323-ID: 5400-gw1
    Carrier: CarrierB, Max Calls: 23, Available: 19
    Carrier: CarrierA, Max Calls: 25, Available: 25
Total number of active registrations = 2
```

The table below describes the fields shown in this output.

Field

Description

CallsignalAddr

Call signaling IP address of the endpoint. If the endpoint is also registered with an alias, a list of all aliases registered
                                          for that endpoint should be listed on the line below.

Port

Call signaling port number of the endpoint.

RASSignalAddr

RAS IP address of the endpoint.

Port

RAS port number of the endpoint.

Zone Name

Zone name (gatekeeper ID) that this endpoint registered in.

Type

Endpoint type (for example, terminal, gateway, or MCU).

Flags

S--Endpoint is statically entered from the alias command rather than being dynamically registered through RAS messages.

O--Endpoint, which is a gateway, has sent notification that it is nearly out of resources.

E164-ID

E.164 ID of the endpoint.

H323-ID

H.323 ID of the endpoint.

Carrier

Carrier associated with the endpoint.

Max Calls

Maximum number of calls the circuit can handle.

Available

Number of new calls the circuit can handle currently.

### Related Commands

Command

Description

endpoint circuit-id h323id

Assigns a circuit to a non-Cisco endpoint.

endpoint resource-threshold

Sets a gateway’s capacity thresholds in the gatekeeper.

zone circuit-id

Assigns a circuit to a remote zone.

## show gatekeeper endpoints

To display the status of all registered endpoints for a gatekeeper, use the show gatekeeper endpoints command in privileged EXEC mode.

show gatekeeper endpoints [ alternates ]

### Syntax Description

alternates

(Optional) Displays information about alternate endpoints. All information normally included with this command is also displayed.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

11.3(2)NA

This command was introduced.

12.0(5)T

The display format was modified for H.323 Version 2.

12.1(5)XM

The alternates keyword was added.

12.1(5)XM2

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T.

12.2(4)T

This command was not supported on the Cisco AS5300, Cisco AS5350, and Cisco AS5400 in this release.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T. The registration and call capacity values were added to the
                                          output display.

12.3(1)

This command was modified to reflect concurrent calls for the endpoints.

## Examples

The following is sample output from this command:

```
Router# show gatekeeper endpoints
CallsignalAddr   Port  RASSignalAddr   Port   Zone Name    Type     F
---------------  ----  -------------   -----  ----------   -----    --
172.21.127.8     1720  172.21.127.8    24999  sj-gk        MCU            H323-ID:joe@cisco.com
           Voice Capacity Max.=23  Avail.=23
           Total number of active registrations = 1
172.21.13.88     1720  172.21.13.88    1719   sj-gk        VOIP-GW   O    H323-ID:la-gw
```

The table below describes significant fields shown in this output.

Field

Description

CallsignalAddr

Call signaling IP address of the endpoint. If the endpoint is also registered with an alias (or aliases), a list of all aliases
                                          registered for that endpoint should be listed on the line below.

Port

Call signaling port number of the endpoint.

RASSignalAddr

Registration, Admission, and Status (RAS) protocol IP address of the endpoint.

Port

RAS port number of the endpoint.

Zone Name

Zone name (gatekeeper identification [ID]) to which this endpoint is registered.

Type

Endpoint type (for example, terminal, gateway, or multipoint control unit [MCU]).

F

S--Endpoint is statically entered from the alias command rather than being dynamically registered through RAS messages. O--Endpoint, which is a gateway, has sent notification
                                          that it is nearly out of resources.

Voice Capacity Max.

Maximum number of channels available on the endpoint.

Avail.

Current number of channels available on the endpoint.

Total number of active registrations

Total number of endpoints registered with the gatekeeper.

In the following example, the show gatekeeper endpoints output has been modified to reflect concurrent calls for the endpoint. If an endpoint is not reporting capacity and the endpoint max - calls h323id command is not configured, "Voice Capacity Max." and "Avail." will not be shown. "Current.= 2" indicates that the current
                              active calls for the endpoint are 2.

```
Router# show gatekeeper endpoints
!
                    GATEKEEPER ENDPOINT REGISTRATION
                    ================================
CallSignalAddr  Port  RASSignalAddr   Port  Zone Name         Type    Flags 
--------------- ----  -------------   ----  ---------         ----    ----- 
172.18.200.27   1720  172.18.200.27   49918 GK-1              VOIP-GW 
    H323-ID:GW1
    Voice Capacity Max.=  Avail.=  Current.= 2
```

If an endpoint is reporting capacity but the endpoint max - calls h323id command is not configured, "Voice Capacity Max." and "Avail." will show reported call capacity of the endpoint as follows:

```
Router# show gatekeeper endpoints
!
                    GATEKEEPER ENDPOINT REGISTRATION
                    ================================
CallSignalAddr  Port  RASSignalAddr  Port  Zone Name          Type  Flags
--------------  ----  -------------  ----  ---------          ----  ----- 
172.18.200.29   1720  172.18.200.29  53152 GK-2               VOIP-GW 
    H323-ID:GW2
    Voice Capacity Max.= 23 Avail.= 22 Current.= 1
```

If an endpoint is reporting capacity but the endpoint max - calls h323id command is not configured, "Voice Capacity Max." will show the maximum calls configured and "Avail." will show the available
                              calls of the endpoint. In this example, "Voice Capacity Max.= 10" is showing that the maximum calls configured for the endpoint
                              are 10. "Avail.= 2" shows that currently available calls for the endpoint are 2. "Current.= 8" shows that current active calls
                              for the endpoint are 8.

```
Router# show gatekeeper endpoints
!
                    GATEKEEPER ENDPOINT REGISTRATION
                    ================================
CallSignalAddr  Port  RASSignalAddr   Port  Zone Name         Type     Flags 
--------------  ----  -------------   ----  ---------         ----     ----- 
172.18.200.27   1720  172.18.200.27   49918 GK-1              VOIP-GW
    H323-ID:GW1
    Voice Capacity Max.= 10  Avail.= 2  Current.= 8
```

The table below describes significant fields in the output examples.

Field

Description

CallsignalAddr

Call signaling IP address of the endpoint. If the endpoint is also registered with an alias (or aliases), a list of all aliases
                                          registered for that endpoint should be listed on the line below.

Port

Call signaling port number of the endpoint.

RASSignalAddr

Registration, Admission, and Status (RAS) protocol IP address of the endpoint.

Port

RAS port number of the endpoint.

Zone Name

Zone name (gatekeeper ID) to which this endpoint is registered.

Type

The endpoint type (for example, terminal, gateway, or multipoint control unit [MCU]).

Flags

S--Endpoint is statically entered from the alias command rather than being dynamically registered through RAS messages. O--Endpoint, which is a gateway, has sent notification
                                          that it is nearly out of resources.

### Related Commands

Command

Description

endpoint resource-threshold

Sets a gateway’s capacity thresholds in the gatekeeper.

show gatekeeper endpoint circuits

Displays endpoint and carrier or trunk group call capacities.

show gatekeeper gw-type-prefix

Displays the gateway technology prefix table.

show gatekeeper zone status

Displays the status of zones related to a gatekeeper.

show gateway

Displays the current gateway status.

## show gatekeeper gw-type-prefix

To display the gateway technology prefix table, use the show gatekeeper gw - type - prefix command in privileged EXEC mode.

show gatekeeper gw-type-prefix

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

11.3(2)NA

This command was introduced.

12.0(5)T

The display format was modified for H.323 Version 2.

12.1(5)XM2

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(4)T

This command was not supported on the Cisco AS5300, Cisco AS5350, and Cisco AS5400 in this release.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

## Examples

The following is sample output from this command for a gatekeeper that controls two local zones, sj-gk and la-gk:

```
Router# show gatekeeper gw-type-prefix
GATEWAY TYPE PREFIX TABLE
===========================
Prefix:12#*     (Default gateway-technology)
  Zone sj-gk master gateway list:
    10.0.0.0:1720 sj-gw1
    10.0.0.0:1720 sj-gw2 (out-of-resources)
    10.0.0.0:1720 sj-gw3
  Zone sj-gk prefix 408....... priority gateway list(s):
   Priority 10:
    10.0.0.0:1720 sj-gw1
   Priority 5:
    10.0.0.0:1720 sj-gw2 (out-of-resources)
    10.0.0.0:1720 sj-gw3
Prefix:7#*     (Hopoff zone la-gk)
  Statically-configured gateways (not necessarily currently registered):
    10.0.0.0:1720
    10.0.0.0:1720
  Zone la-gk master gateway list:
    10.0.0.0:1720 la-gw1
    10.0.0.0:1720 la-gw2
```

The table below describes significant fields shown in this output.

Field

Description

Prefix

Technology prefix defined with the gw - type - prefix command.

Zone sj-gk master gateway list

List of all the gateways registered to zone sj-gk with the technology prefix under which they are listed. (This display shows
                                          that gateways sj-gw1, sj-gw2, and sj-gw3 have registered in zone sj-gk with the technology prefix 12#.)

Zone sj-gk prefix 408....... priority gateway list(s)

List of prioritized gateways to handle calls to area code 408.

Priority 10

Highest priority level. Gateways listed following "Priority 10" are given the highest priority when selecting a gateway to
                                          service calls to the specified area code. (In this display, gateway sj-gw1 is given the highest priority to handle calls to
                                          the 408 area code.)

Priority 5

Any gateway that does not have a priority level assigned to it defaults to priority 5.

(out-of-resources)

Indication that the displayed gateway has sent a "low-in-resources" notification.

(Hopoff zone la-gk)

Any call that specifies this technology prefix should be directed to hop off in the la-gk zone, no matter what the area code
                                          of the called number is. (In this display, calls that specify technology prefix 7# are always routed to zone la-gk, regardless
                                          of the actual zone prefix in the destination address.)

Zone la-gk master gateway list

List of all the gateways registered to la-gk with the technology prefix under which they are listed. (This display shows
                                          that gateways la-gw1 and la-gw2 have registered in zone la-gk with the technology prefix 7#. No priority lists are displayed
                                          here because none were defined for zone la-gk.)

(Default gateway-technology)

If no gateway-type prefix is specified in a called number, then gateways that register with 12# are the default type to be
                                          used for the call.

Statically-configured gateways

List of all IP addresses and port numbers of gateways that are incapable of supplying technology-prefix information when
                                          they register. This display shows that, when gateways 1.1.1.1:1720 and 2.2.2.2:1720 register, they are considered to be of
                                          type 7#.

### Related Commands

Command

Description

show gatekeeper calls

Displays the status of each ongoing call of which a gatekeeper is aware.

show gatekeeper endpoints

Displays the status of all registered endpoints for a gatekeeper.

show gateway

Displays the current gateway status.

## show gatekeeper performance statistics

To display performance statistics on the gatekeeper level message, use the show gatekeeper performance stats command in user EXEC or privileged EXEC mode.

show gatekeeper performance statistics [ zone [ name zone-name ]] [ cumulative ]

### Syntax Description

zone

(Optional) Displays zone statistics of the gatekeeper.

name zone - name

(Optional) Specifies the zone name or gatekeeper name.

cumulative

(Optional) Displays the total statistics collected by the gatekeeper since the last reload.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release

Modification

12.1(5)XM

This command was introduced.

12.2(2)T1

This command was integrated into Cisco IOS Release 12.2(2)T.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(15)T

This command was modified. The zone , name , and cumulative keywords were added and the zone - name argument was added.

12.4(5)

This command was modified. Command output was enhanced to include counters for:

Automatic rejections (ARJs) sent due to an ARQ access-list denial.

Location rejections (LRJs) sent due to an LRQ access-list denial.

### Usage Guidelines

Use this command to display the statistics on calls, registration, calls routed to other gatekeepers, and calls used via
                              zone processing.

When the cumulative keyword is used along with zone name keywords displays the total statistics for the specified zone, from the starting time of the gatekeeper. These values are
                              not reset when the clear h323 gatekeeper stats command is used.

This command displays statistical data related to the router. You can identify the number of call initiation events using
                              the following messages:

Automatic repeat request (ARQ)

Admission confirmation (ACF)

Admission rejection (ARJ)

You can identify endpoint contact events that have been requested and either confirmed or rejected on the router using the
                              following:

Location request (LRQ)

Location confirm (LCF)

Location reject (LRJ)

The counts associated with overload and the number of endpoints sent to alternate gatekeepers that are associated with overload
                              conditions are also displayed. Only when the router experiences an overload condition do these counters reveal a value other
                              than zero. The real endpoint count simply displays the number of endpoints registered on this router platform. The time stamp
                              displays the start time when the counters started capturing the data. When you want to request a new start period, enter the clear h323 gatekeeper stats command. The counters are reset and the time stamp is updated with the new time.

You can identify remote gatekeeper contacts that have been requested and either confirmed or rejected on the router using
                              the following messages:

Location confirm (LCF)

Location rejection (LRJ)

Location request (LRQ)

You can identify zone-level or gatekeeper-level registration statistics using the following messages:

Registration confirmation (RCF)

Registration rejection (RRJ)

Registration request (RRQ)

You can identify zone-level or gatekeeper-level unregistration statistics using the following messages:

Unregistration confirmation (UCF)

Unregistration rejection (URJ)

Unregistration request (URQ)

## Examples

The following is the example of basic output from the show gatekeeper performance stats command. The basic output specifies that the counters are reset using the clear h323 gatekeeper stats command and the output displays the statistcs from the last reset.

```
Router# show gatekeeper performance stats -----Gatekeeper Performance Statistics-----
Performance statistics captured since: 20:09:00 UTC Thu Sep 15 2005
Gatekeeper level Admission Statistics:
        ARQs received: 1
        ARQs received from originating endpoints: 0
        ACFs sent: 1
        ACFs sent to the originating endpoint: 0
        ARJs sent: 0
        ARJs sent to the originating endpoint: 0
        ARJs sent due to overload: 0
        ARJs sent due to ARQ access-list denial: 0
        Number of concurrent calls: 0
        Number of concurrent originating calls: 0
Gatekeeper level Location Statistics:
        LRQs received: 3
        LRQs sent: 0
        LCFs received: 0
        LCFs sent: 1
        LRJs received: 0
        LRJs sent: 2
        LRJs sent due to overload: 0
        LRJs sent due to LRQ access-list denial: 2
Gatekeeper level Registration Statistics:
        RRJ due to overload: 0
        Total Registered  Endpoints: 2
Gatekeeper level Disengage Statistics:
        DRQs received: 1
        DRQs sent: 0
        DCFs received: 0
        DCFs sent: 1
        DRJs received: 0
        DRJs sent: 0
Gatekeeper viazone message counters:
        inARQ: 0
        infwdARQ: 0
        inerrARQ: 0
        inLRQ: 0
        infwdLRQ: 0
        inerrLRQ: 0
        outLRQ: 0
        outfwdLRQ: 0
        outerrLRQ: 0
        outARQ: 0
        outfwdARQ: 0
        outerrARQ: 0
Load balancing events: 0
```

The following is the example of cumulative output from the show gatekeeper performance stats command. The cumulative output specifies that the counters are not reset and the output displays the total statistcs from
                              the starting time of the gatekeeper.

```
Router# show gatekeeper performance stats zone name voip3-2600-2 Performance statistics for zone voip3-2600-2
-----Zone Level Performance Statistics-----
Performance statistics captured since: 00:17:00 UTC Mon Mar 1 1993 
Zone level Admission Statistics:
        ARQs received: 1 
        ARQs received from originating endpoints: 0 
        ACFs sent: 1 
        ACFs sent to the originating endpoint: 0 
        ARJs sent: 0 
        ARJs sent to the originating endpoint: 0 
        Number of concurrent total calls: 0 
        Number of concurrent originating calls: 0
Zone level Location Statistics:
        LRQs received: 1 
        LRQs sent: 0 
        LCFs received: 0 
        LCFs sent: 1 
        LRJs received: 0 
        LRJs sent: 0
Zone level Registration Statistics:
        Full RRQs received: 1 
        Light RRQs received: 574 
        RCFs sent: 576 
        RRJs sent: 0 
        Total Registered Endpoints: 1
Zone level UnRegistration Statistics:
        URQs received: 0 
        URQs sent: 0 
        UCFs received: 0 
        UCFs sent: 0 
        URJs received: 0 
        URJs sent: 0 
        URQs sent due to timeout: 0
Zone level Disengage Statistics:
        DRQs received: 1 
        DRQs sent: 0 
        DCFs received: 0 
        DCFs sent: 1 
        DRJs received: 0 
        DRJs sent: 0
```

The table below shows significant fields shown in the displays. Most of the fields are self-explanatory and are not listed
                              the table.

Field

Description

Full RRQs received

A full registration request (RRQ) contains all registration information that is used for successful registration.

Light RRQs received

A light RRQ contains abbreviated registration information that is used to maintain an existing registration.

### Related Commands

Command

Description

clear h323 gatekeeper stats

Clears statistics about gatekeeper performance.

## show gatekeeper servers

To display a list of currently registered and statically configured triggers on a gatekeeper router, use the show gatekeeper servers command in EXEC mode.

show gatekeeper servers [gkid]

### Syntax Description

gkid

(Optional) Local gatekeeper name to which this trigger applies.

### Command Modes

EXEC (#)

## Command History

Release

Modification

12.1(1)T

This command was introduced on the Cisco 2500 series, Cisco 2600 series, Cisco 3600 series, Cisco 7200, and Cisco MC3810.

12.2(2)XB

The output of this command was modified to show additional server statistics, including the following: gatekeeper server
                                          timeout value; Gatekeeper Transaction Message Protocol (GKTMP) version installed; number of Registration Request (RRQ), Registration
                                          Response (RRQ), Response Confirmation (RCF), and Response Reject (RRJ) messages received; timeouts encountered; average response
                                          time; and if the server is usable.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T.

12.2(11)T

This command was implemented on the Cisco 3700 series.

12.2(15)T12

The command was modified to show additional server statistics.

12.3(8)T

The command was modified to show additional server statistics.

12.3(9)

The command was modified to show additional server statistics.

### Usage Guidelines

Use this command to show all server triggers (whether dynamically registered from the external servers or statically configured
                              from the command-line interface) on this gatekeeper. If the gatekeeper ID is specified, only triggers applied to the specified
                              gatekeeper zone appear. If the gatekeeper ID is not specified, server triggers for all local zones on this gatekeeper appear.

## Examples

The following is sample output from this command:

```
Router# show gatekeeper servers GATEKEEPER SERVERS STATUS
            =========================
Gatekeeper Server listening port: 8250
Gatekeeper Server timeout value: 30 (100ms)
GateKeeper GKTMP version: 4.1
Gatekeeper-ID: Gatekeeper1
------------------------
RRQ Priority: 5
Server-ID: Server43
Server IP address: 209.165.200.254:40118
Server type: dynamically registered
Connection Status: active
Trigger Information:
Trigger unconditionally
Server Statistics:
REQUEST RRQ Sent=0
RESPONSE RRQ Received = 0
RESPONSE RCF Received = 0
RESPONSE RRJ Received = 0
Average response time(ms)=0
Server Usable=TRUE
Timeout Statistics:
Server-ID: Server43
Server IP address: 209.165.200.254:40118
Server type: dynamically registered
Connection Status: active
Timeout Encountered=0
```

The table below describes significant fields shown in this output.

Field

Description

GateKeeper GKTMP version

Version of Gatekeeper Transaction Message Protocol installed.

RRQ Priority

Registration priority.

Server-ID

Server ID name.

Server IP address

Server IP address.

Server type

Type of server.

Connection Status

Whether the connection is active or inactive.

Trigger Information

Which Registration, Admission, and Status (RAS) messages the Cisco IOS gatekeeper forwards to the external application.

REQUEST RRQ

Registration requests received.

RESPONSE RRQ

Registration responses received.

RESPONSE RCF

Response confirmations received.

RESPONSE RRJ

Response reject messages received.

### Related Commands

Command

Description

debug gatekeeper server

Traces all the message exchanges between the Cisco IOS gatekeeper and the external applications.

endpoint circuit-id h323id

Tracks call capacity information on the gatekeeper.

server registration-port

Configures a listening port on the gatekeeper for server registration.

server trigger arq

Configures static triggers on the gatekeeper.

## show gatekeeper status

To display overall gatekeeper status, including authorization and authentication status and zone status, use the show gatekeeper status command in privileged EXEC mode.

show gatekeeper status

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

11.3(2)NA

This command was introduced.

12.0(3)T

This command was integrated into Cisco IOS Release 12.0(3)T.

12.1(5)XM

This command was modified to show information about load balancing and vendor-specific attributes.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T.

12.2(2)XB

This command was modified to show information about server flow control.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T.

## Examples

The following is sample output from this command:

```
Router# show gatekeeper status Gatekeeper State: UP
    Load Balancing:   DISABLED
    Flow Control:     ENABLED
    Zone Name:        snet-3660-3
    Accounting:       DISABLED
    Endpoint Throttling:        DISABLED
    Security:         DISABLED
    Maximum Remote Bandwidth:              unlimited
    Current Remote Bandwidth:              0 kbps
    Current Remote Bandwidth (w/ Alt GKs): 0 kbps
```

The table below describes significant fields shown in this output.

Field

Description

Gatekeeper State

Gatekeeper state has the following values:

UP is operational.

DOWN is administratively shut down.

INACTIVE is administratively enabled; that is, the no shutdown command has been issued, but no local zones have been configured.

HSRP STANDBY indicates that the gatekeeper is on hot standby and will take over when the currently active gatekeeper fails.

Load Balancing

Whether load balancing is enabled.

Flow Control

Whether server flow control is enabled.

Zone Name

Zone name to which the gatekeeper belongs.

Accounting

Whether authorization and accounting features are enabled.

Endpoint Throttling

Whether endpoint throttling is enabled.

Security

Whether security features are enabled.

Bandwidth

Maximum remote bandwidth, current remote bandwidth, and current remote bandwidth with alternate gatekeepers.

### Related Commands

Command

Description

show gatekeeper servers

Displays statistics about the gatekeeper.

## show gatekeeper status cluster

To display information about each element of a local cluster, such as the amount of memory used, the number of active calls,
                              and the number of endpoints registered on the element, use the show gatekeeper status cluster command in privileged EXEC mode.

show gatekeeper status cluster

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.1(5)XM1

This command was introduced.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

## Examples

The following command displays information about elements of a local cluster, two of whose components are RoseGK and LavenderGK:

```
Router# show gatekeeper status cluster CLUSTER INFORMATION
                   ===================
                           Active     Endpoint       Last
Hostname     %Mem   %CPU    Calls        Count   Announce
--------     ----   ----   ------     --------   --------
RoseGK         72      0        1   Local Host
LavenderGK     30      1        0            4        14s
```

### Related Commands

Command

Description

show gatekeeper endpoints

Displays the status of all registered endpoints for a gatekeeper.

show gatekeeper performance statistics

Displays information about the number of calls accepted and rejected, and finds the number of endpoints sent to other gatekeepers.

show gatekeeper zone cluster

Displays the dynamic status of all local clusters.

## show gatekeeper zone cluster

To display the dynamic status of all local clusters, use the show gatekeeper zone cluster command in privileged EXEC mode.

show gatekeeper zone cluster

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.1(5)XM1

This command was introduced.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

## Examples

The following command displays information about the current bandwidth values and about when the last announcement message
                              from the alternate gatekeeper was received. In the following example, PRI represents the priority value assigned to an alternate
                              gatekeeper. This field ranges from 0 to 127, with 127 representing the lowest priority.

```
Router# show gatekeeper zone cluster LOCAL CLUSTER INFORMATION¸6t
                  ============================
                                   TOT BW   INT BW   REM BW   LAST       ALT GK
LOCAL GK NAME   ALT GK NAME   PRI  (kbps)   (kbps)   (kbps)   ANNOUNCE   STATUS
-------------   -----------   ---  ------   ------   ------   --------   ------
ParisGK         GenevaGK      120  0        0        0        7s         CONNECTED
NiceGK          ZurichGK      100  0        0        0        7s         CONNECTED
```

### Related Commands

Command

Description

timer cluster - element announce

Defines the time interval between successive announcement messages exchanged between elements of a local cluster.

zone cluster local

Defines a local grouping of gatekeepers.

zone remote

Statically specifies a remote zone if DNS is unavailable or undesirable.

## show gatekeeper zone prefix

To display the zone prefix table, use the show gatekeeper zone prefix command in privileged EXEC mode.

show gatekeeper zone prefix [ all ]

### Syntax Description

all

(Optional) Displays the dynamic zone prefixes registered by each gateway.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

11.3(2)NA

This command was introduced.

12.2(15)T

The all keyword was added.

### Usage Guidelines

If the all keyword is not specified, this command displays the static zone prefixes only. Use the include filter with the all keyword to display the prefixes associated with a particular gateway. For example, the show gatekeeper zone prefix all | include GW1 command displays the dynamic prefixes associated with gateway GW1.

## Examples

The following command displays the zone prefix table for the gatekeeper:

```
Router# show gatekeeper zone prefix
      ZONE PREFIX TABLE
      =================
GK-NAME               E164-PREFIX
-------               -----------
gk2                   408*       
gk2                   5551001*   
gk2                   5551002*   
gk2                   5553020*   
gk2                   5553020*   
gk1                   555....    
gk2                   719*       
gk2                   919*
```

The following command displays the zone prefix table, including the dynamic zone prefixes, for the gatekeeper:

```
Router# show gatekeeper zone prefix all
                    ZONE PREFIX TABLE
      ===============================================
GK-NAME               E164-PREFIX       Dynamic GW-priority
-------               -----------       -------------------
gk2                  408*
gk2                  5551001*             GW1 /5
gk2                  5551002*             GW1 /5 GW2 /10
gk2                  5553020*             GW1 /8 
gk2                  5553020*
gk1                  555....
gk2                  719*
gk2                  919*                 GW2 /5
```

The table below describes significant fields shown in this output.

Field

Description

GK-NAME

Gatekeeper name.

E164-PREFIX

E.164 prefix and a dot that acts as a wildcard for matching each remaining number in the telephone number.

Dynamic GW-priority

Gateway that serves this E164 prefix.

Gateway priority. A 0 value prevents the gatekeeper from using the gateway for that prefix. Value 10 places the highest priority
                                          on the gateway. The default priority value for a dynamic gateway is 5.

### Related Commands

Command

Description

show gatekeeper zone cluster

Displays the dynamic status of all local clusters.

## show gatekeeper zone status

To display the status of zones related to a gatekeeper, use the show gatekeeper zone status command in privileged EXEC mode.

show gatekeeper zone status

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

11.3(2)NA

This command was introduced.

12.0(5)T

The display format was modified for H.323 Version 2.

12.1(5)XM2

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(4)T

This command was not supported on the Cisco AS5300, Cisco AS5350, and Cisco AS5400 in this release.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

## Examples

The following is sample output from this command:

```
Router# show gatekeeper zone status GATEKEEPER ZONES
                      ================
GK name      Domain Name   RAS Address     PORT  FLAGS MAX-BW   CUR-BW
                                                       (kbps)   (kbps)
-------      -----------   -----------     ----  ----- ------   ------
sj.xyz.com   xyz.com       10.0.0.0        1719  LS             0
  SUBNET ATTRIBUTES :
    All Other Subnets :(Enabled)
  PROXY USAGE CONFIGURATION :
    inbound Calls from germany.xyz.com :
      to terminals in local zone sj.xyz.com :use proxy
      to gateways in local zone sj.xyz.com  :do not use proxy
    Outbound Calls to germany.xyz.com
      from terminals in local zone germany.xyz.com :use proxy
      from gateways in local zone germany.xyz.com  :do not use proxy
    Inbound Calls from all other zones :
      to terminals in local zone sj.xyz.com :use proxy
      to gateways in local zone sj.xyz.com  :do not use proxy
    Outbound Calls to all other zones :
      from terminals in local zone sj.xyz.com :do not use proxy
      from gateways in local zone sj.xyz.com  :do not use proxy
tokyo.xyz.co xyz.com         10.0.0.0        1719  RS             0
milan.xyz.co xyz.com         10.0.0.0        1719  RS             0
```

The table below describes significant fields shown in this output.

Field

Description

GK name

Gatekeeper name (also known as the zone name), which is truncated after 12 characters in the display.

Domain Name

Domain with which the gatekeeper is associated.

RAS Address

Registration, Admission, and Status (RAS) protocol address of the gatekeeper.

FLAGS

Displays the following information:

S = static (CLI-configured, not DNS-discovered)

L = local

R = remote

MAX-BW

Maximum bandwidth for the zone, in kbps.

CUR-BW

Current bandwidth in use, in kbps.

SUBNET ATTRIBUTES

List of subnets controlled by the local gatekeeper.

PROXY USAGE CONFIGURATION

Inbound and outbound proxy policies as configured for the local gatekeeper (or zone).

### Related Commands

Command

Description

show gatekeeper calls

Displays the status of each ongoing call of which a gatekeeper is aware.

show gatekeeper endpoints

Displays the status of registered endpoints for a gatekeeper.

show gateway

Displays the current gateway status.

| carrier | Displays carrier ID configuration details of the peer protocol. |
|---|---|
| cor | Displays restriction settings class details. |
| trunk-group-label | Displays trunk group label configuration details. |

| Release | Modification |
|---|---|
| 12.2(17)SX | This command was introduced. |
| 12.4(22)T | This command was modified in a release earlier than Cisco IOS Release 12.4(22)T. The carrier and trunk-group-label keywords were added. |

| number | (Optional) A specific video dial peer. Output displays information about that dial peer. |
|---|---|
| summary | (Optional) Output displays a one-line summary of each video dial peer. |

| Release | Modification |
|---|---|
| 12.0(5)XK | This command was introduced on the Cisco MC3810. |
| 12.0(7)T | This command was integrated into Cisco IOS Release 12.0(7)T. |

| Field | Description |
|---|---|
| NSAP | Network service access point (NSAP) address |

| dp-tag | Dial-Peer Tag. Range: 1—1073741823. |
|---|---|
| tenant-tag | Keepalive status info for tenants. Range: 1—10000. |

| Release | Modification |
|---|---|
| Cisco IOS XE Cupertino
                                             17.9.1a | This command was introduced. |

| Note | CUBE does not display the status for dynamic dial-peers. |
|---|---|

| Note | You need to configure the same transport type for the dial-peers with same SRV
                                          destination. |
|---|---|

| Command | Description |
|---|---|
| show voice class sip-options-keepalive | Displays the details of connectivity between CUBE VoIP dial peers and SIP servers. |

| number | (Optional) A specific voice dial peer. The output displays detailed information about that dial peer. |
|---|---|
| busy-trigger-counter | (Optional) Displays the busy trigger call count on the VoIP dial peer. |
| summary | (Optional) Displays a short summary of each voice dial peer. |
| voip system | (Optional) Displays information about the VoIP dial peer. |

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced. |
| 11.3(1)MA | This command was modified. The summary keyword was added for the Cisco MC3810. |
| 12.0(3)XG | This command was implemented for Voice over Frame Relay (VoFR) on the Cisco 2600 series and Cisco 3600 series. |
| 12.0(4)T | This command was implemented for VoFR on the Cisco 7200 series. |
| 12.1(3)T | This command was implemented for modem pass-through over VoIP on the Cisco AS5300. |
| 12.2(2)XB | This command was modified to support VoiceXML applications. |
| 12.2(4)T | This command was implemented on the Cisco 1750. |
| 12.2(8)T | This command was implemented on the Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745. |
| 12.2(2)XN | This command was modified. Support for enhanced Media Gateway Control Protocol (MGCP) voice gateway interoperability was
                                          added to Cisco CallManager 3.1 for the Cisco 2600 series, Cisco 3600 series, and Cisco VG200. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T and Cisco CallManager 3.2 and implemented on the Cisco IAD2420.
                                          The command was enhanced to display configuration information for bandwidth, video codec, and rtp payload-type for H.263+
                                          and H.264 video codec. |
| 12.4(22)T | This command was modified. This command was enhanced to display the current configuration state of the history-info header.
                                          Command output was updated to show IPv6 information. |
| 15.0(1)XA | This command was modified. The output was enhanced to show the logical partitioning class of restriction (LPCOR) policy for
                                          outgoing calls. |
| 15.1(1)T | This command was integrated into Cisco IOS Release 15.1(1)T. |
| 15.1(3)T | This command was modified. The output was enhanced to display information about the bind at the dial-peer level and to display
                                          the connection status of Foreign Exchange Office (FXO) ports. |
| Cisco IOS XE Cupertino
                                                17.9.1a | This command was modified. The output was enhanced to display the OPTIONS ping keepalive status for a dial-peer. |

| Note | The recommended command to verify the QoS settings that the signaling and media packets will be marked with when RSVP is not
                                          configured for call signaling on the Cisco UBE is the show dial-peer voice command. |
|---|---|

| Note | Beginning in Cisco IOS Release 15.1(3)T, there is improved status monitoring of FXO ports--any time an FXO port is connected
                                          or disconnected, a message is displayed to indicate the status change. For example, the following message is displayed to
                                          report that a cable has been connected, and the status is changed to "up" for FXO port 0/2/0: 000118: Jul 14 18:06:05.122
                                          EST: %LINK-3-UPDOWN: Interface Foreign Exchange Office 0/2/0, changed state to operational status up due to cable reconnection |
|---|---|

| Field | Description |
|---|---|
| Accepted Calls | Number of calls accepted from this peer since system startup. |
| acc-qos | Lowest acceptable quality of service configured for calls for this peer. |
| Admin state | Administrative state of this peer. |
| answer-address | Answer address configured for this dial peer. |
| bandwidth maximum/minimum | The maximum and minimum bandwidth, in Kb/s. |
| Charged Units | Total number of charging units that have applied to this peer since system startup, in hundredths of a second. |
| CLID Restriction | Indicates if Calling Line ID (CLID) restriction is enabled. |
| CLID Network Number | Displays the network number sent as CLID, if configured. |
| CLID Second Number sent | Displays whether a second calling number is stripped from the call setup. |
| CLID Override RDNIS | Indicates whether the CLID is overridden by the redirecting number. |
| codec | Default voice codec rate of speech. |
| Connect Time | Accumulated connect time to the peer since system startup for both incoming and outgoing calls, in hundredths of a second. |
| connections/maximum | Indicates the maximum number of call connections per peer. |
| Destination | Indicates the voice class that is used to match the destination URL. |
| destination-pattern | Destination pattern (telephone number) for this peer. |
| digit_strip | Indicates if digit stripping is enabled. |
| direct-inward-dial | Indicates if direct inward dial is enabled. |
| disconnect-cause | Indicates the disconnect cause code to be used when an incoming call is blocked. |
| dnis-map | Name of the dialed-number identification service (DNIS) map. |
| DTMF Relay | Indicates if dual-tone multifrequency (DTMF) relay is enabled. |
| Expect factor | User-requested expectation factor of voice quality for calls through this peer. |
| Failed Calls | Number of failed call attempts to this peer since system startup. |
| fax rate | Fax transmission rate configured for this peer. |
| forward-digits | Indicates the destination digits to be forwarded of this peer. |
| group | Group number associated with this peer. |
| huntstop | Indicates whether dial-peer hunting is turned on, by the huntstop command, for this dial peer. |
| Icpif | Configured Impairment/Calculated Planning Impairment Factor (ICPIF) value for calls sent by a dial peer. |
| in bound application associated | Interactive voice response (IVR) application that is configured to handle inbound calls to this dial peer. |
| incall-number | Full E.164 telephone number to be used to identify the dial peer. |
| incoming call blocking | Indicates the incoming call blocking setup of this peer. |
| incoming called-number | Indicates the incoming called number if it has been set. |
| incoming COR list | Indicates the level of Class of Restrictions for incoming calls of this peer. |
| Incomplete Calls | Indicates the number of outgoing disconnected calls with the user busy (17), no user response (18), or no answer (19) cause
                                          code. |
| information type | Information type for this call (voice, fax, video). |
| Last Disconnect Cause | Encoded network cause associated with the last call. This value is updated whenever a call is started or cleared and depends
                                          on the interface type and session protocol being used on this interface. |
| Last Disconnect Text | ASCII text describing the reason for the last call termination. |
| Last Setup Time | Value of the system uptime when the last call to this peer was started. |
| Modem passthrough | Modem pass-through signaling method is named signaling event (NSE). |
| numbering Type | Indicates the numbering type for a peer call leg. |
| Operation state | Operational state of this peer. |
| outgoing COR list | Indicates the level of Class of Restrictions for outgoing calls of this peer. |
| outgoing LPCOR | Setting of the lpcor outgoing command. |
| out bound application associated | The voice application that is configured to handle outbound calls from this dial peer. Outbound calls are handed off to the
                                          named application. |
| Outbound state | Indicates the current outbound status of a POTS peer. |
| payload size | Indicates the size (in bytes) of the payload of the fax rate or codec setup. |
| payload type | NSE payload type. |
| peer type | Dial peer type (voice, data). |
| permission | Configured permission level for this peer. |
| Poor QOV Trap | Indicates if poor quality of voice trap messages is enabled. |
| preemption level | Indicates the call preemption level of this peer. |
| prefix | Indicates dialed digits prefix of this peer. |
| Redundancy | Packet redundancy (RFC 2198) for modem traffic. |
| Refused Calls | Number of calls from this peer refused since system startup. |
| register E.164 number with H.323 GK and/or SIP Registrar | Indicates the "register e.164" option of this peer. |
| req-qos | Configured requested quality of service for calls for this dial peer. |
| session-target | Session target of this peer. |
| session-protocol | Session protocol to be used for Internet calls between local and remote routers through the IP backbone. |
| source carrier-id | Indicates the source carrier ID of this peer that will be used to match the source carrier ID of an incoming call. |
| source trunk-group label | Indicates the source trunk group label of this peer that can be used to match the source trunk group label of an incoming
                                          call. |
| Successful Calls | Number of completed calls to this peer. |
| supported-language | Indicates the list of supported languages of this peer. |
| tag | Unique dial peer ID number. |
| target carrier-id | Indicates the target carrier ID of this peer that will be used to match the target carrier ID for an outgoing call. |
| target-trunkgroup-label | Indicates the target trunk group label of this peer that can be used to match the target trunk group label of an outgoing
                                          call. |
| Time elapsed since last clearing of voice call statistics | Elapsed time between the current time and the time when the clear dial-peer voice command was executed. |
| Translation profile (Incoming) | Indicates the translation profile for incoming calls. |
| Translation profile (Outgoing) | Indicates the translation profile for outgoing calls. |
| translation-profile | Indicates the number translation profile of this peer. |
| type | Indicates the peer encapsulation type (pots, voip, vofr, voatm or mmoip). |
| VAD | Whether voice activation detection (VAD) is enabled for this dial peer. |
| voice class called-number inbound/outbound | Indicates the voice-class called number inbound or outbound setup of this peer. |
| voice class sip history-info | Indicates the configuration state of the history-info header. If the history-info header is not configured for the dial peer,
                                          this field is set to system. If the history-info header is enabled on this dial peer, this field is set to enable. If the
                                          history-info header is disabled on this dial peer, this field is set to disable. |
| voice class sip bind | Indicates the configuration state of the bind address. If the bind is configured for the global, this field is sent to system.
                                          If the bind address is enabled on this dial peer, this field is set to enabled. |
| voice-port | Indicates the voice interface setting of this POTS peer. |

| Field | Description |
|---|---|
| dial-peer hunt | Hunt group selection order that is defined for the dial peer by the dial-peer hunt command. |
| TAG | Unique identifier assigned to the dial peer when it was created. |
| TYPE | Type of dial peer (mmoip, pots, voatm, vofr, or voip). |
| ADMIN | Whether the administrative state is up or down. |
| OPER | Whether the operational state is up or down. |
| PREFIX | Prefix that is configured in the dial peer by the prefix command. |
| DEST-PATTERN | Destination pattern that is configured in the dial peer by the destination-pattern command. |
| PREF | Hunt group preference that is configured in the dial peer by the preference command. |
| PASS THRU | Modem pass-through method that is configured in the dial peer by the modem passthrough command. |
| SESS-TARGET | Destination that is configured in the dial peer by the session target command. |
| PORT | Router voice port that is configured for the dial peer. Valid only for POTS dial peers. |

| Note | A dial-peer is marked as partially active ( partial ) if at least one of the destinations is active out of a group, and the rest are inactive. |
|---|---|

| Command | Description |
|---|---|
| show call active voice | Displays the VoIP active call table. |
| show call history voice | Displays the VoIP call history table. |
| show dialplan incall number | Displays which POTS dial peer is matched for a specific calling number or voice port. |
| show dialplan number | Displays which dial peer is reached when a specific telephone number is dialed. |
| show num-exp | Displays how the number expansions are configured in VoIP. |
| show voice port | Displays configuration information about a specific voice port. |

| incoming-dialpeer-tag | The dial peer COR identifier used to determine the matching outbound dial peer. |
|---|---|
| number | The dialed number used in conjunction with the COR identifier to determine the matching outbound dial peer. |
| timeout | (Optional) Allows matching for variable-length destination patterns. |

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced on the Cisco 2600 series and Cisco 3600 series routers and on Cisco AS5800 access servers. |
| 12.2(11)T | This command was implemented on the Cisco 1751 and Cisco 3700 series routers and on Cisco AS5300 access servers. |

| Note | For actual voice calls coming into the router, the incoming corlist of a specified inbound dial peer and the outgoing called
                                          number will be used to match the outbound dial peer. |
|---|---|

| Field | Description |
|---|---|
| Macro Exp. | Expected destination pattern for this dial peer. |
| VoiceEncapPeer | Dial peer associated with the calling number entered. |
| VoiceOverIpPeer | Dial peer associated with the calling number entered. |
| peer type | Type of this dial peer (voice or data). |
| information type | Information type for this dial peer (voice or data). |
| description | Any additional information for this dial peer entered using the description dial peer command. |
| tag | Unique number identifying the dial peer. |
| destination-pattern | Destination pattern (telephone number) configured for this dial peer. |
| answer-address | Answer address (calling number) configured for this dial peer. |
| preference | Hunt group preference order set for this dial peer. |
| CLID restriction | Indicates the Caller ID restriction (if any) configured for this dial peer. |
| CLID Network Number | Indicates the originating network of the Caller ID source. |
| CLID Second Number sent | Indicates the digits in the second number (if any) forwarded for this dial peer. |
| source carrier-id | VoIP or POTS source carrier identifier. |
| source trunk-group-label | VoIP or POTS source trunk group identifier. |
| numbering Type | Identifies the numbering scheme employed for this dial peer. |
| group | Dial peer group in which this dial peer is a member. |
| Admin state | Administrative state of this dial peer. |
| Operation state | Operational state of this dial peer. |
| incoming called-number | Called number (DNIS) configured for this dial peer. |
| connections/maximum | Number of actual and maximum allowable connections associated with this dial peer. |
| DTMF Relay | Whether the dtmf - relay command is enabled or disabled for this dial peer. |
| URI classes: Incoming (Request) | URI voice class used for matching dial peer to Request-URI in an incoming SIP Invite message. |
| URI classes: Incoming (To) | URI voice class used for matching dial peer to the To header in an incoming SIP Invite message. |
| URI classes: Incoming (From) | URI voice class used for matching dial peer to the From header in an incoming SIP Invite message. |
| URI classes: Destination | URI voice class used to match the dial peer to the destination URI for an outgoing call. |
| modem transport | Transport method configured for modem calls. The default is system, which means that the value configured globally is used. |
| huntstop | Whether the huntstop command is enabled or disabled for this dial peer. |
| in bound application associated | IVR application that is associated with this dial peer when this dial peer is used for an inbound call leg. |
| out bound application associated | IVR application that is associated with this dial peer when this dial peer is used for an outbound call leg. |
| dnis-map | Name of the dialed-number identification service (DNIS) map that is configured in the dial peer with the dnis - map command. |
| permission | Configured permission level for this dial peer. |
| incoming COR list | Class of restriction (COR) criteria associated when matching an incoming dial peer. |
| outgoing COR list | COR criteria used to determine the appropriate outbound dial peer. |
| Translation profile (Incoming) | Incoming translation criteria applied to this dial peer. |
| Translation profile (Outgoing) | Translation criteria applied to this dial peer when matching an outbound dial peer. |
| incoming call blocking | Indicates whether or not incoming call blocking has been applied for this dial peer. |
| translation-profile | The predefined translation profile associated with this dial peer. |
| disconnect-cause | Encoded network cause associated with the last call. |
| voice-port | Voice port through which calls come into this dial peer. |
| type | Type of dial peer (POTS or VoIP). |
| prefix | Prefix number that is added to the front of the dial string before it is forwarded to the telephony device. |
| forward-digits | Which digits are forwarded to the telephony interface as configured using the forward - digits command. |
| session-target | Configured session target (IP address or host name) for this dial peer. |
| direct-inward-dial | Whether the direct - inward - dial command is enabled or disabled for this dial peer. |
| digit_strip | Whether digit stripping is enabled or disabled in the dial peer. Enabled is the default. |
| register E.164 number with GK | Indicates whether or not the dial peer has been configured to register its full E.164-format number with the local gatekeeper. |
| fax rate | The transmission speed configured for fax calls. The default is system, which means that the value configured globally is
                                          used. |
| payload size | The size (in bytes) for a fax transmission payload. |
| session-protocol | Session protocol to be used for Internet calls between local and remote router via the IP backbone. |
| req-qos | Configured requested quality of service for calls for this dial peer. |
| acc-qos | Lowest acceptable quality of service configured for calls for this dial peer. |
| codec | Voice codec configured for this dial peer. Default is G.729 (8 kbps). |
| Expect factor | User-requested expectation factor of voice quality for calls through this dial peer. |
| Icpif | Configured calculated planning impairment factor (ICPIF) value for calls sent by this dial peer. |
| VAD | Indicates whether or not voice activation detection (VAD) is enabled for this dial peer. |
| voice class sip url | URL format (SIP or TEL) used for SIP calls to this dial peer, as configured with the voice - class sip url command. The default is system, which means that the value configured globally with the url command in voice service VoIP SIP mode is used. |
| voice class sip rel1xx | Indicates whether or not reliable provisional responses are supported, as configured with the voice - class sip rel1xx command. The default is system, which means that the value configured globally with the rel1xx command in voice service VoIP SIP mode is used. |
| voice class perm tag | Voice class for a trunk that is assigned to this dial peer with the voice - class permanent command. |
| Connect Time | Unit of measure indicating the call connection time associated with this dial peer. |
| Charged Units | Number of call units charged to this dial peer. |
| Successful Calls | Number of completed calls to this dial peer since system startup. |
| Failed Calls | Number of uncompleted (failed) calls to this dial peer since system startup. |
| Incomplete Calls | Number of incomplete calls to this dial peer since system startup. |
| Accepted Calls | Number of calls from this dial peer accepted since system startup. |
| Refused Calls | Number of calls from this dial peer refused since system startup. |
| Last Disconnect Cause | Encoded network cause associated with the last call. This value is updated whenever a call is started or cleared and depends
                                          on the interface type and session protocol being used on this interface. |
| Last Disconnect Text | ASCII text describing the reason for the last call termination. |
| Last Setup Time | Value of the System Up Time when the last call to this peer was started. |
| Matched | Destination pattern matched for this dial peer. |
| Digits | Number of digits in this destination pattern matched for this dial peer. |
| Target | Matched session target (IP address or host name) for this dial peer. |

| Command | Description |
|---|---|
| show dialplan in-carrier | Displays which VoIP or POTS dial peer is matched for a specific source carrier. |
| show dialplan in-trunk-group-label | Displays which VoIP or POTS dial peer is matched for a specific source trunk group. |
| show dialplan incall | Displays which POTS dial peer is matched for a specific calling number or voice port. |
| show dialplan number | Displays which dial peer is matched for a particular telephone number. |

| voice - port | Voice port location. The syntax of this argument is platform-specific. For information on the syntax for a particular platform,
                                          see the voice - port command. |
|---|---|
| calling - number | E.164 Calling number or ANI of the incoming voice call. |
| timeout | (Optional) Allows matching for variable-length destination patterns. |

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on the Cisco 3600 series. |
| 12.2(8)T | This command was implemented on the Cisco 1751, Cisco 2600 series, Cisco 3725, and Cisco 3745 and the timeout keyword was
                                          added. |

| Note | For actual voice calls coming into the router, the router attempts to match the called number (the dialed number identification
                                          service [DNIS] number) with the incoming called-number configured in a dial peer. The router, however, does not consider the
                                          called number when using the show dialplan incall number command. |
|---|---|

| Command | Description |
|---|---|
| show dialplan dialpeer | Displays which outbound dial peer is matched based upon the incoming dialed number and the COR criteria specified in the command
                                          line. |
| show dialplan in-carrier | Displays which VoIP or POTS dial peer is matched for a specific source carrier. |
| show dialplan in-trunk-group-label | Displays which VoIP or POTS dial peer is matched for a specific source trunk group. |
| show dialplan number | Displays which dial peer is matched for a particular telephone number. |

| called | Voice class that is configured in dial peers with the incoming uri called command. |
|---|---|
| calling | Voice class that is configured in dial peers with the incoming uri calling command. |
| from | Voice class that is configured in dial peers with the incoming uri from command. |
| request | Voice class that is configured in dial peers with the incoming uri request command. |
| to | Voice class that is configured in dial peers with the incoming uri to command. |
| uri | URI of the incoming call. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Field | Description |
|---|---|
| VoiceOverIpPeer | Dial peer associated with the calling number entered. |
| information type | Information type for this call; for example, voice or fax. |
| tag | Unique number that identifies the dial peer. |
| destination-pattern | Destination pattern (called number) configured for this dial peer. |
| answer-address | Answer address (calling number) configured for this dial peer. |
| preference | Hunt group preference order set for this dial peer. |
| Admin state | Administrative state of this dial peer. |
| Operation state | Operational state of this dial peer. |
| incoming called-number | Called number (DNIS) configured for this dial peer. |
| DTMF Relay | Whether the dtmf-relay command is enabled or disabled for this dial peer. |
| URI classes: Incoming (Request) | URI voice class used for matching dial peer to Request-URI in an incoming SIP Invite message. |
| URI classes: Incoming (To) | URI voice class used for matching dial peer to the To header in an incoming SIP Invite message. |
| URI classes: Incoming (From) | URI voice class used for matching dial peer to the From header in an incoming SIP Invite message. |
| URI classes: Destination | URI voice class used to match the dial peer to the destination URI for an outgoing call. |
| huntstop | Whether the huntstop command is enabled or disabled for this dial peer. |
| in bound application associated | IVR application that is associated with this dial peer when this dial peer is used for an inbound call leg. |
| out bound application associated | IVR application that is associated with this dial peer when this dial peer is used for an outbound call leg. |
| dnis-map | Name of the dialed-number identification service (DNIS) map that is configured in the dial peer with the dnis-map command. |
| permission | Configured permission level for this peer. |
| type | Type of dial peer (POTS or VoIP). |
| session-target | Configured session target (IP address or host name) for this dial peer. |
| session-protocol | Session protocol to be used for Internet calls between local and remote router via the IP backbone. |
| req-qos | Configured requested quality of service for calls for this dial peer. |
| acc-qos | Lowest acceptable quality of service configured for calls for this peer. |
| codec | Voice codec configured for this dial peer. Default is G.729 (8 kbps). |
| Expect factor | User-requested expectation factor of voice quality for calls through this peer. |
| Icpif | Configured calculated planning impairment factor (ICPIF) value for calls sent by a dial peer. |
| VAD | Whether voice activation detection (VAD) is enabled for this dial peer. |
| voice class sip url | URL format (SIP or TEL) used for SIP calls to this dial peer, as configured with the voice-class sip url command. The default is system, which means that the value configured globally with the url command in voice service VoIP SIP mode is used. |
| voice class sip rel1xx | Whether reliable provisional responses are supported, as configured with the voice-class sip rel1xx command. The default is system, which means that the value configured globally with the rel1xx command in voice service VoIP SIP mode is used. |
| voice class perm tag | Voice class for a trunk that is assigned to this dial peer with the voice-class permanent command. |
| Connect Time | Unit of measure indicating the call connection time associated with this dial peer. |
| Charged Units | Number of call units charged to this dial peer. |
| Successful Calls | Number of completed calls to this peer since system startup. |
| Failed Calls | Number of uncompleted (failed) calls to this peer since system startup. |
| Accepted Calls | Number of calls from this peer accepted since system startup. |
| Refused Calls | Number of calls from this peer refused since system startup. |
| Last Disconnect Cause | Encoded network cause associated with the last call. This value is updated whenever a call is started or cleared and depends
                                          on the interface type and session protocol being used on this interface. |
| Last Disconnect Text | ASCII text describing the reason for the last call termination. |
| Last Setup Time | Value of the System Up Time when the last call to this peer was started. |
| Matched | Destination pattern matched for this dial peer. |
| Target | Matched session target (IP address or host name) for this dial peer. |

| Command | Description |
|---|---|
| debug voice uri | Displays debugging messages related to URI voice classes. |
| incoming uri | Specifies the voice class used to match a VoIP dial peer to the URI of an incoming call. |
| session protocol | Specifies the session protocol in the dial peer for calls between the local and remote router. |
| show dial-peer voice | Displays detailed and summary information about voice dial peers. |
| show dialplan uri | Displays which outbound dial peer is matched for a specific destination URI. |
| voice class uri | Creates or modifies a voice class for matching dial peers to calls containing a SIP or TEL URI. |
| voice class uri sip preference | Sets a preference for selecting voice classes for a SIP URI. |

| carrier - id | VoIP or POTS source carrier identifier. |
|---|---|
| voip | (Optional) Allows you to limit the search criteria to only VoIP dial peers. |
| pots | (Optional) Allows you to limit the search criteria to only POTS dial peers. |

| Release | Modification |
|---|---|
| 12.2(13)T | This command was introduced on the Cisco 2600 series and Cisco 3600 series routers and on Cisco AS5300, Cisco AS5400, and
                                          Cisco AS5800 access servers. |

| Command | Description |
|---|---|
| show dialplan dialpeer | Displays which outbound dial peer is matched based upon the incoming dialed number and the COR criteria specified in the command
                                          line. |
| show dialplan incall | Displays which POTS dial peer is matched for a specific calling number or voice port. |
| show dialplan in-trunk-group-label | Displays which VoIP or POTS dial peer is matched for a specific source trunk group. |
| show dialplan number | Displays which dial peer is matched for a particular telephone number. |

| trunk - group - label | VoIP or POTS source trunk group identifier. |
|---|---|
| voip | (Optional) Allows you to limit the search criteria to only
                                          						VoIP dial peers. |
| pots | (Optional) Allows you to limit the search criteria to only
                                          						POTS dial peers. |

| Release | Modification |
|---|---|
| 12.2(13)T | This command was introduced on the Cisco 2600 series and
                                          						Cisco 3600 series routers and on Cisco AS5300, Cisco AS5400, and Cisco AS5800
                                          						access servers. |

| Command | Description |
|---|---|
| show dialplan dialpeer | Displays which outbound dial peer is matched based upon the
                                          						incoming dialed number and the COR criteria specified in the command line. |
| show dialplan in-carrier | Displays which VoIP or POTS dial peer is matched for a
                                          						specific source carrier. |
| show dialplan incall | Displays which POTS dial peer is matched for a specific
                                          						calling number or voice port. |
| show dialplan number | Displays which dial peer is matched for a particular
                                          						telephone number. |

| dial - string | Particular destination pattern (E.164 telephone number). |
|---|---|
| carrier | (Optional) Indicates that you wish to base your search for applicable dial peers on the source carrier identifier. |
| identifier | (Optional) Source carrier identifier to accompany the carrier keyword. |
| fax | (Optional) Fax information type. |
| huntstop | (Optional) Terminates further dial-peer hunting upon encountering the first dial-string match. |
| timeout | (Optional) Allows matching for variable-length destination patterns. |
| voice | (Optional) Voice information type. |

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on the Cisco 3600 series. |
| 12.2(1) | The huntstop keyword was added. |
| 12.2(8)T | This command was implemented on the Cisco 1751, Cisco 2600 series, Cisco 3725, and Cisco 3745 and the timeout keyword was
                                          added. |
| 12.2(11)T | The carrier , fax , and voice keywords were added. |

| Command | Description |
|---|---|
| show dialplan dialpeer | Displays which outbound dial peer is matched based upon the incoming dialed number and the COR criteria specified in the command
                                          line. |
| show dialplan incall | Displays which POTS dial peer is matched for a specific calling number or voice port. |
| show dialplan in-carrier | Displays which VoIP or POTS dial peer is matched for a specific source carrier. |
| show dialplan in-trunk-group-label | Displays which VoIP or POTS dial peer is matched for a specific source trunk group. |

| uri | Destination Session Initiation Protocol (SIP) or telephone (TEL) URI for the outgoing call. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| debug voice uri | Displays debugging messages related to URI voice classes. |
| destination uri | Specifies the voice class used to match the dial peer to the destination URI for an outgoing call. |
| show dialplan incall uri | Displays which dial peer is matched for a specific URI in an incoming call. |
| voice class uri | Creates or modifies a voice class for matching dial peers to a SIP or TEL URI. |
| voice class uri sip preference | Sets a preference for selecting voice classes for a SIP URI. |

| Release | Modification |
|---|---|
| 12.4(15)T | This command was introduced. |
| Cisco IOS XE Release 2.4 | This command was integrated into Cisco IOS XE Release 2.4. |

| Field | Description |
|---|---|
| DN | Directory number. |
| name | Name of the connection. |
| number | Telephone number. |

| all | (Optional) Displays all global information about the DSP farm service. |
|---|---|
| dsp | (Optional) Displays DSP information about the DSP farm service. |
| active | Displays active DSP information about the DSP farm service. |
| all | Displays all DSP information about the DSP farm service. |
| idle | Displays idle DSP information about the DSP farm service. |
| stats | Displays DSP statistics about the DSP farm service. |
| bridge-id | Displays the DSP statistics for a call bridge the specified bridge ID. |
| sample | (Optional) Displays statistics of the specified sample interval. |
| seconds | (Optional) The DSP sample interval time, in seconds. |
| profile | (Optional) Displays profiles about the DSP farm service. |
| profile-id | (Optional) The profile ID about the DSP farm service. |
| sessions | (Optional) Displays sessions and connections about the DSP farm service. |
| session-id | (Optional) The session identifier to be displayed for the DSP farm service. |
| video | (Optional) Displays information on video resources. |
| conference | (Optional) Displays the DSP information, such as the codecs, video bridge channel, and transmit (tx) and receive (rx) packets
                                          that are used for each participant in a conference and is grouped by conference sessions. |
| statistics | (Optional) Displays the DSP statistics of the call bridge. |
| transcode | (Optional) Displays the DSP status and statistics for the transcoding call. |

| Release | Modification |
|---|---|
| Cisco IOS XE 17.18.2 | This command was implemented on C8375-E-G2 router platform. |
| 15.1(4)M | This command was modified. The video , conference , statistics , and transcode keywords were added. |
| Cisco IOS XE Release 3.2S | This command was implemented on the Cisco ASR 1000 Series Router. |
| 12.4(15)T | The stats , sample , sessions , and profile keywords were added. The bridge-id , profile-id , seconds , and session-id arguments were added. |
| 12.2(13)T | This command was implemented on the Cisco 2600 series, Cisco 3620, Cisco 3640, Cisco 3660, and Cisco 3700 series. |
| 12.1(5)YH | This command was introduced on the Cisco VG200. |

| Note | The session keyword and session-id argument is not supported on Cisco ASR 1000 Series Router. |
|---|---|

| Command | Description |
|---|---|
| dspfarm (DSP farm) | Enables DSP-farm service. |

| profile ide ntifier | (Optional) Number that uniquely identifies a profile. Range is from 1 to 65535. There is no default. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |

| Field | Description |
|---|---|
| Profile ID | Displays the profile ID number. |
| Service | Displays the service that is associated with the profile. |
| Resource ID | Displays the ID number that the profile is associated with in the Cisco CallManager register. |
| Profile Description | Displays the description of the profile. |
| Profile Service Mode | The status of the profile service. It can be either Secure or Non Secure. |
| Profile Admin State | Displays the status of the profile. If the Profile Admin State is DOWN, use the no shutdown command in DSP farm profile configuration mode. |
| Profile Operation State | Displays the status of the DSP farm profiles registration process with the Cisco CallManager. Status options are as follows: ACTIVE--The profile is registered with the Cisco Unified CallManager. ACTIVE IN PROGRESS--The profile is still registering with the Cisco Unified CallManager. Wait for the profile to finish registering. DOWN--The profile is not registering with the Cisco Unified CallManager. Check the connectivity between the DSP farm gateway
                                                and the Cisco Unified CallManager. DOWN IN PROGRESS--The profile is deregistering from the Cisco Unified CallManager and deallocating the DSP resources. RESOURCE ALLOCATED--The DSP resources for this profile are allocated or reserved. |
| Application | Displays the routing protocol used. |
| Number of Resource Configured | Maximum number of sessions that are supported by a profile. |
| Number of Resource Available | Total number of resources that are configurable. |
| Hardware Configured Resources | Number of sessions configured in the profile. |
| Hardware Available Resources | Number of sessions available for this profile. |
| Software Resources | Number of software sessions configured for this profile (applicable only to MTP profiles). |
| Codec Configuration | Lists the codecs that are configured. Note Media Termination Point (MTP) profile supports only one codec per profile. | Note | Media Termination Point (MTP) profile supports only one codec per profile. |
| Note | Media Termination Point (MTP) profile supports only one codec per profile. |
| RSVP | Resource Reservation Protocol (RSVP) support for this profile. |
| TRP | Displays whether firewall traversal is enabled for Trusted Relay Point. |

| Note | Media Termination Point (MTP) profile supports only one codec per profile. |
|---|---|

| Command | Description |
|---|---|
| dsp services dspfarm | Configures DSP farm services for a specified voice card. |
| dspfarm profile | Enters DSP farm profile configuration mode and defines a profile for DSP farm services. |
| show media resource status | Displays the current media resource status. |

| all | Displays DSP information for all DSP group. |
|---|---|
| slot | Displays DSP information for the specified slot. |
| slot-number | Slot used in the DSP group. |
| video | Displays information on video resources. |
| voice | Displays information on voice resources. |

| Release | Modification |
|---|---|
| 15.1(4)M | This command was introduced. |

| Command | Description |
|---|---|
| dsp service dspfarm | Configures DSP farm services for a specified voice card. |
| dspfarm (DSP farm) | Enables DSP-farm service. |
| voice service dsp-reservation | Configures the percentage of DSP resources are reserved for voice services and enables video services to use the remaining
                                          DSP resources. This command is required to enable video services. |
| voice-card | Enters voice-card configuration mode. |

| hardware | Displays information about the hardware accelerated EC device. |
|---|---|
| status | Displays the allocation status. |
| slot-number | The slot number of the interface cards. |

| Release | Modification |
|---|---|
| 12.4(24)T | This command was introduced in a release earlier than Cisco IOS Release 12.4(24)T. |

| Field | Description |
|---|---|
| ECAN CH | Total channels in the slot. |
| Assigned | Status of the assigned channels. |
| DSP ID | Digital Signaling Processor (DSP) identification number for the assigned channels. |
| VOICEPORT | Voice port of the channels. |
| EC | Echo Cancellation status of the assigned channels. |
| NLP | Status of the Non-Linear Processor (NLP). |
| COV | Echo cancellation Coverage status of the assigned channels. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Field | Description |
|---|---|
| Uid | User ID. |
| Consumer_id | ID of the consumer client process. |
| Consumer_hdl | Handler of the consumer client process. |
| evt_type | Event type. |

| Command | Description |
|---|---|
| show voice statistics csr interval accounting | Displays all accounting CSRs specified by interval number. |
| show voice statistics csr interval aggregation | Displays signaling CSRs specified by interval number. |
| show voice statistics csr since-reset accounting | Displays all accounting CSRs since the last reset. |
| show voice statistics csr since-reset aggregation-level | Displays all signaling CSRs since the last reset. |
| show voice statistics csr since-reset all | Displays all CSRs since the last reset. |
| show voice statistics interval-tag | Displays the configured interval numbers. |
| show voice statistics memory-usage | Displays current memory usage. |

| interface | (Optional) Specific interface type and number for which you want to display FRF.11 subchannel information. |
|---|---|
| dlci | (Optional) Specific data link connection identifier for which you want to display FRF.11 subchannel information. |
| cid | (Optional) Specific subchannel for which you want to display information. |

| Release | Modification |
|---|---|
| 12.0(4)T | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810 series. |

| Field | Description |
|---|---|
| interface | Number of the interface that has been selected for observation of FRF.11 subchannels. |
| vofr-type | Type of VoFR DLCI being observed. |
| cid | Portion of the specified DLCI that is carrying the designated traffic type. A DLCI can be subdivided into 255 subchannels. |
| cid-type | Type of traffic carried on this subchannel. |
| input-pkts | Number of packets received by this subchannel. |
| output-pkts | Number of packets sent on this subchannel. |
| dropped-pkts | Total number of packets discarded by this subchannel. |

| Command | Description |
|---|---|
| show call active voice | Displays the contents of the active call table. |
| show call history voice | Displays the contents of the call history table. |
| show dial-peer voice | Displays configuration information and call statistics for dial peers. |
| show frame-relay fragment | Displays Frame Relay fragmentation details. |
| show frame-relay pvc | Displays statistics about PVCs for Frame Relay interfaces. |
| show voice-port | Displays configuration information about a specific voice port. |

| history | (Optional) Displays call history information along with internal error codes at the gatekeeper. The number of disconnected
                                          calls displayed in response to this command is the number specified in the call-history max-size number command. Use of this max-size number helps to reduce CPU usage in the storage and reporting of this information. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(2)NA | This command was introduced. |
| 12.0(3)T | This command was integrated into Cisco IOS Release 12.0(3)T. |
| 12.0(5)T | The output for this command was changed. |
| 12.1(5)XM2 | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(4)T | Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400 is not included in this release. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. This command is supported on the Cisco AS5300, Cisco AS5350,
                                          Cisco AS5400, and Cisco AS5850 in this release. |
| 12.4(4)T | The history keyword was added to display historical information on disconnected calls. |

| Field | Description |
|---|---|
| LocalCallID | Identification number of the call. |
| Age(secs) | Age of the call, in seconds. |
| BW(Kbps) | Bandwidth in use, in kilobytes per second. |
| Endpt | Role of each endpoint (terminal, gateway, or proxy) in the call (originator, target, or proxy) and the call signaling and
                                          Registration, Admission, and Status (RAS) protocol address. |
| Alias | H.323-Identification (ID) or Email-ID of the endpoint. |
| E.164Addr | E.164 address of the endpoint. |
| CallSignalAddr | Call-signaling IP address of the endpoint. |
| Port | Call-signaling port number of the endpoint. |
| RASSignalAddr | RAS IP address of the endpoint. |
| Port | RAS port number of the endpoint. |

| Command | Description |
|---|---|
| clear h323 gatekeeper call | Forces the disconnection of a specific call or of all calls active on a particular gatekeeper. |
| call history max | Specifies the number of records to be kept in the history table. |

| begin | (Optional) Displays all circuits, beginning with the line containing the expression. |
|---|---|
| exclude | (Optional) Displays all circuits, excluding those containing the expression. |
| include | (Optional) Displays all circuits, including those containing the expression. |
| expression | (Optional) Word or phrase used to determine what lines are displayed. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Field | Description |
|---|---|
| Circuit | Name of the each circuit connected to the gatekeeper. |
| Endpoint | Name of each H.323 endpoint. |
| Max Calls | Maximum number of calls that circuit can handle. |
| Avail Calls | Number of new calls that the circuit can handle at the current time. |
| Resources | Whether the circuit’s resources have exceeded the defined threshold limits. The endpoint resource - threshold command defines these thresholds. |
| Zone | Zone that supports the endpoint. The zone circuit - id command assigns a zone to an endpoint. |
| Total Endpoints | Total number of endpoints supported by the circuit. |
| Total Zones | Total number of zones supported by the circuit. |

| Command | Description |
|---|---|
| endpoint resource-threshold | Sets a gateway’s capacity thresholds in the gatekeeper. |
| zone circuit-id | Assigns a remote zone to a carrier. |

| Release1.25 | Modification |
|---|---|
| 12.1(5)XM | This command was introduced. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T. |
| 12.2(2)XB1 | This command was integrated into Cisco IOS Release 12.2(2)XB1 and implemented on the Cisco AS5850 router. |

| Command | Description |
|---|---|
| show gatekeeper endpoints | Displays the status of all registered endpoints for a gatekeeper. |
| show gatekeeper performance stats | Displays the performance statistics on the the gatekeeper level message. |
| show gatekeeper zone cluster | Displays the dynamic status of all local clusters. |

| \| begin | (Optional) Displays all circuits, beginning with the line that contains expression. |
|---|---|---|
| \| exclude | (Optional) Displays all circuits, excluding those that contain expression. |
| \| include | (Optional) Displays all circuits, including those that contain expression. |
| expression | (Optional) Word or phrase used to determine what lines are displayed. |

| Release | Modification |
|---|---|
| 11.3(2)NA | This command was introduced. |
| 12.0(5)T | The display format was modified for H.323 Version 2. |
| 12.2(11)T | The display format was modified to show the E.164 ID, carrier and trunk group data, and total number of active calls. |

| Field | Description |
|---|---|
| CallsignalAddr | Call signaling IP address of the endpoint. If the endpoint is also registered with an alias, a list of all aliases registered
                                          for that endpoint should be listed on the line below. |
| Port | Call signaling port number of the endpoint. |
| RASSignalAddr | RAS IP address of the endpoint. |
| Port | RAS port number of the endpoint. |
| Zone Name | Zone name (gatekeeper ID) that this endpoint registered in. |
| Type | Endpoint type (for example, terminal, gateway, or MCU). |
| Flags | S--Endpoint is statically entered from the alias command rather than being dynamically registered through RAS messages. O--Endpoint, which is a gateway, has sent notification that it is nearly out of resources. |
| E164-ID | E.164 ID of the endpoint. |
| H323-ID | H.323 ID of the endpoint. |
| Carrier | Carrier associated with the endpoint. |
| Max Calls | Maximum number of calls the circuit can handle. |
| Available | Number of new calls the circuit can handle currently. |

| Command | Description |
|---|---|
| endpoint circuit-id h323id | Assigns a circuit to a non-Cisco endpoint. |
| endpoint resource-threshold | Sets a gateway’s capacity thresholds in the gatekeeper. |
| zone circuit-id | Assigns a circuit to a remote zone. |

| alternates | (Optional) Displays information about alternate endpoints. All information normally included with this command is also displayed. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(2)NA | This command was introduced. |
| 12.0(5)T | The display format was modified for H.323 Version 2. |
| 12.1(5)XM | The alternates keyword was added. |
| 12.1(5)XM2 | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T. |
| 12.2(4)T | This command was not supported on the Cisco AS5300, Cisco AS5350, and Cisco AS5400 in this release. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. The registration and call capacity values were added to the
                                          output display. |
| 12.3(1) | This command was modified to reflect concurrent calls for the endpoints. |

| Field | Description |
|---|---|
| CallsignalAddr | Call signaling IP address of the endpoint. If the endpoint is also registered with an alias (or aliases), a list of all aliases
                                          registered for that endpoint should be listed on the line below. |
| Port | Call signaling port number of the endpoint. |
| RASSignalAddr | Registration, Admission, and Status (RAS) protocol IP address of the endpoint. |
| Port | RAS port number of the endpoint. |
| Zone Name | Zone name (gatekeeper identification [ID]) to which this endpoint is registered. |
| Type | Endpoint type (for example, terminal, gateway, or multipoint control unit [MCU]). |
| F | S--Endpoint is statically entered from the alias command rather than being dynamically registered through RAS messages. O--Endpoint, which is a gateway, has sent notification
                                          that it is nearly out of resources. |
| Voice Capacity Max. | Maximum number of channels available on the endpoint. |
| Avail. | Current number of channels available on the endpoint. |
| Total number of active registrations | Total number of endpoints registered with the gatekeeper. |

| Field | Description |
|---|---|
| CallsignalAddr | Call signaling IP address of the endpoint. If the endpoint is also registered with an alias (or aliases), a list of all aliases
                                          registered for that endpoint should be listed on the line below. |
| Port | Call signaling port number of the endpoint. |
| RASSignalAddr | Registration, Admission, and Status (RAS) protocol IP address of the endpoint. |
| Port | RAS port number of the endpoint. |
| Zone Name | Zone name (gatekeeper ID) to which this endpoint is registered. |
| Type | The endpoint type (for example, terminal, gateway, or multipoint control unit [MCU]). |
| Flags | S--Endpoint is statically entered from the alias command rather than being dynamically registered through RAS messages. O--Endpoint, which is a gateway, has sent notification
                                          that it is nearly out of resources. |

| Command | Description |
|---|---|
| endpoint resource-threshold | Sets a gateway’s capacity thresholds in the gatekeeper. |
| show gatekeeper endpoint circuits | Displays endpoint and carrier or trunk group call capacities. |
| show gatekeeper gw-type-prefix | Displays the gateway technology prefix table. |
| show gatekeeper zone status | Displays the status of zones related to a gatekeeper. |
| show gateway | Displays the current gateway status. |

| Release | Modification |
|---|---|
| 11.3(2)NA | This command was introduced. |
| 12.0(5)T | The display format was modified for H.323 Version 2. |
| 12.1(5)XM2 | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(4)T | This command was not supported on the Cisco AS5300, Cisco AS5350, and Cisco AS5400 in this release. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |

| Field | Description |
|---|---|
| Prefix | Technology prefix defined with the gw - type - prefix command. |
| Zone sj-gk master gateway list | List of all the gateways registered to zone sj-gk with the technology prefix under which they are listed. (This display shows
                                          that gateways sj-gw1, sj-gw2, and sj-gw3 have registered in zone sj-gk with the technology prefix 12#.) |
| Zone sj-gk prefix 408....... priority gateway list(s) | List of prioritized gateways to handle calls to area code 408. |
| Priority 10 | Highest priority level. Gateways listed following "Priority 10" are given the highest priority when selecting a gateway to
                                          service calls to the specified area code. (In this display, gateway sj-gw1 is given the highest priority to handle calls to
                                          the 408 area code.) |
| Priority 5 | Any gateway that does not have a priority level assigned to it defaults to priority 5. |
| (out-of-resources) | Indication that the displayed gateway has sent a "low-in-resources" notification. |
| (Hopoff zone la-gk) | Any call that specifies this technology prefix should be directed to hop off in the la-gk zone, no matter what the area code
                                          of the called number is. (In this display, calls that specify technology prefix 7# are always routed to zone la-gk, regardless
                                          of the actual zone prefix in the destination address.) |
| Zone la-gk master gateway list | List of all the gateways registered to la-gk with the technology prefix under which they are listed. (This display shows
                                          that gateways la-gw1 and la-gw2 have registered in zone la-gk with the technology prefix 7#. No priority lists are displayed
                                          here because none were defined for zone la-gk.) |
| (Default gateway-technology) | If no gateway-type prefix is specified in a called number, then gateways that register with 12# are the default type to be
                                          used for the call. |
| Statically-configured gateways | List of all IP addresses and port numbers of gateways that are incapable of supplying technology-prefix information when
                                          they register. This display shows that, when gateways 1.1.1.1:1720 and 2.2.2.2:1720 register, they are considered to be of
                                          type 7#. |

| Command | Description |
|---|---|
| show gatekeeper calls | Displays the status of each ongoing call of which a gatekeeper is aware. |
| show gatekeeper endpoints | Displays the status of all registered endpoints for a gatekeeper. |
| show gateway | Displays the current gateway status. |

| zone | (Optional) Displays zone statistics of the gatekeeper. |
|---|---|
| name zone - name | (Optional) Specifies the zone name or gatekeeper name. |
| cumulative | (Optional) Displays the total statistics collected by the gatekeeper since the last reload. |

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was introduced. |
| 12.2(2)T1 | This command was integrated into Cisco IOS Release 12.2(2)T. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(15)T | This command was modified. The zone , name , and cumulative keywords were added and the zone - name argument was added. |
| 12.4(5) | This command was modified. Command output was enhanced to include counters for: Automatic rejections (ARJs) sent due to an ARQ access-list denial. Location rejections (LRJs) sent due to an LRQ access-list denial. |

| Field | Description |
|---|---|
| Full RRQs received | A full registration request (RRQ) contains all registration information that is used for successful registration. |
| Light RRQs received | A light RRQ contains abbreviated registration information that is used to maintain an existing registration. |

| Command | Description |
|---|---|
| clear h323 gatekeeper stats | Clears statistics about gatekeeper performance. |

| gkid | (Optional) Local gatekeeper name to which this trigger applies. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced on the Cisco 2500 series, Cisco 2600 series, Cisco 3600 series, Cisco 7200, and Cisco MC3810. |
| 12.2(2)XB | The output of this command was modified to show additional server statistics, including the following: gatekeeper server
                                          timeout value; Gatekeeper Transaction Message Protocol (GKTMP) version installed; number of Registration Request (RRQ), Registration
                                          Response (RRQ), Response Confirmation (RCF), and Response Reject (RRJ) messages received; timeouts encountered; average response
                                          time; and if the server is usable. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T. |
| 12.2(11)T | This command was implemented on the Cisco 3700 series. |
| 12.2(15)T12 | The command was modified to show additional server statistics. |
| 12.3(8)T | The command was modified to show additional server statistics. |
| 12.3(9) | The command was modified to show additional server statistics. |

| Field | Description |
|---|---|
| GateKeeper GKTMP version | Version of Gatekeeper Transaction Message Protocol installed. |
| RRQ Priority | Registration priority. |
| Server-ID | Server ID name. |
| Server IP address | Server IP address. |
| Server type | Type of server. |
| Connection Status | Whether the connection is active or inactive. |
| Trigger Information | Which Registration, Admission, and Status (RAS) messages the Cisco IOS gatekeeper forwards to the external application. |
| REQUEST RRQ | Registration requests received. |
| RESPONSE RRQ | Registration responses received. |
| RESPONSE RCF | Response confirmations received. |
| RESPONSE RRJ | Response reject messages received. |

| Command | Description |
|---|---|
| debug gatekeeper server | Traces all the message exchanges between the Cisco IOS gatekeeper and the external applications. |
| endpoint circuit-id h323id | Tracks call capacity information on the gatekeeper. |
| server registration-port | Configures a listening port on the gatekeeper for server registration. |
| server trigger arq | Configures static triggers on the gatekeeper. |

| Release | Modification |
|---|---|
| 11.3(2)NA | This command was introduced. |
| 12.0(3)T | This command was integrated into Cisco IOS Release 12.0(3)T. |
| 12.1(5)XM | This command was modified to show information about load balancing and vendor-specific attributes. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T. |
| 12.2(2)XB | This command was modified to show information about server flow control. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T. |

| Field | Description |
|---|---|
| Gatekeeper State | Gatekeeper state has the following values: UP is operational. DOWN is administratively shut down. INACTIVE is administratively enabled; that is, the no shutdown command has been issued, but no local zones have been configured. HSRP STANDBY indicates that the gatekeeper is on hot standby and will take over when the currently active gatekeeper fails. |
| Load Balancing | Whether load balancing is enabled. |
| Flow Control | Whether server flow control is enabled. |
| Zone Name | Zone name to which the gatekeeper belongs. |
| Accounting | Whether authorization and accounting features are enabled. |
| Endpoint Throttling | Whether endpoint throttling is enabled. |
| Security | Whether security features are enabled. |
| Bandwidth | Maximum remote bandwidth, current remote bandwidth, and current remote bandwidth with alternate gatekeepers. |

| Command | Description |
|---|---|
| show gatekeeper servers | Displays statistics about the gatekeeper. |

| Release | Modification |
|---|---|
| 12.1(5)XM1 | This command was introduced. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |

| Command | Description |
|---|---|
| show gatekeeper endpoints | Displays the status of all registered endpoints for a gatekeeper. |
| show gatekeeper performance statistics | Displays information about the number of calls accepted and rejected, and finds the number of endpoints sent to other gatekeepers. |
| show gatekeeper zone cluster | Displays the dynamic status of all local clusters. |

| Release | Modification |
|---|---|
| 12.1(5)XM1 | This command was introduced. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |

| Command | Description |
|---|---|
| timer cluster - element announce | Defines the time interval between successive announcement messages exchanged between elements of a local cluster. |
| zone cluster local | Defines a local grouping of gatekeepers. |
| zone remote | Statically specifies a remote zone if DNS is unavailable or undesirable. |

| all | (Optional) Displays the dynamic zone prefixes registered by each gateway. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(2)NA | This command was introduced. |
| 12.2(15)T | The all keyword was added. |

| Field | Description |
|---|---|
| GK-NAME | Gatekeeper name. |
| E164-PREFIX | E.164 prefix and a dot that acts as a wildcard for matching each remaining number in the telephone number. |
| Dynamic GW-priority | Gateway that serves this E164 prefix. Gateway priority. A 0 value prevents the gatekeeper from using the gateway for that prefix. Value 10 places the highest priority
                                          on the gateway. The default priority value for a dynamic gateway is 5. |

| Command | Description |
|---|---|
| show gatekeeper zone cluster | Displays the dynamic status of all local clusters. |

| Release | Modification |
|---|---|
| 11.3(2)NA | This command was introduced. |
| 12.0(5)T | The display format was modified for H.323 Version 2. |
| 12.1(5)XM2 | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(4)T | This command was not supported on the Cisco AS5300, Cisco AS5350, and Cisco AS5400 in this release. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |

| Field | Description |
|---|---|
| GK name | Gatekeeper name (also known as the zone name), which is truncated after 12 characters in the display. |
| Domain Name | Domain with which the gatekeeper is associated. |
| RAS Address | Registration, Admission, and Status (RAS) protocol address of the gatekeeper. |
| FLAGS | Displays the following information: S = static (CLI-configured, not DNS-discovered) L = local R = remote |
| MAX-BW | Maximum bandwidth for the zone, in kbps. |
| CUR-BW | Current bandwidth in use, in kbps. |
| SUBNET ATTRIBUTES | List of subnets controlled by the local gatekeeper. |
| PROXY USAGE CONFIGURATION | Inbound and outbound proxy policies as configured for the local gatekeeper (or zone). |

| Command | Description |
|---|---|
| show gatekeeper calls | Displays the status of each ongoing call of which a gatekeeper is aware. |
| show gatekeeper endpoints | Displays the status of registered endpoints for a gatekeeper. |
| show gateway | Displays the current gateway status. |