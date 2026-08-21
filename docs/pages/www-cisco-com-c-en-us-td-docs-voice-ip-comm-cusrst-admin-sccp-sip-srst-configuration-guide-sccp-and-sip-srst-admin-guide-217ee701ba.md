---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-admin-sccp-sip-srst-configuration-guide-sccp-and-sip-srst-admin-guide-217ee701ba
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/admin/sccp_sip_srst/configuration/guide/SCCP_and_SIP_SRST_Admin_Guide/srst_setting_up_using_sip.html
retrieved_at: 2026-08-21T02:49:15.170107+00:00
---

Cisco Unified SRST Administration Guide (All Versions)

# Cisco Unified SRST Administration Guide (All Versions)

Updated: April 25, 2026

Chapter: Setting Up Cisco Unified IP Phones using SIP

## Chapter: Setting Up Cisco Unified IP Phones using SIP

# Setting Up Cisco Unified IP Phones using SIP

Session Initiation Protocol (SIP) registrar functionality in Cisco IOS software is an essential part of Cisco Unified SIP
                        Survivable Remote Site Telephony (SRST). According to RFC 3261, a SIP registrar is a server that accepts Register requests
                        and is typically collocated with a proxy or redirect server. A SIP registrar may also offer location services.

## Prerequisites for Configuring the SIP Registrar

Complete the prerequisites documented in the Prerequisites for Configuring Cisco Unified SIP SRST section in Cisco Unified SRST Feature Overview chapter.

## Restrictions for Configuring the SIP Registrar

See the restrictions documented in the Restrictions for Configuring Cisco Unified SIP SRST section in the Cisco Unified SRST Feature Overview chapter.

## Information About Configuring the SIP Registrar

Cisco Unified SIP SRST provides backup to an external SIP call control (IP-PBX) by providing basic registrar and call handling
                           services. These services are used by a SIP IP phone in the event of a WAN connection outage when the SIP phone is unable to
                           communicate with its primary SIP proxy. The Cisco Unified SIP SRST device also provides PSTN gateway access for placing and
                           receiving PSTN calls.

Cisco Unified SIP SRST works for the following types of calls:

Local SIP IP phone to local SIP phone, if the main proxy is unavailable.

Additional services like class of restriction (COR) for local SIP IP phones to the outgoing PSTN. For example, to block outgoing
                                 1-900 numbers.

### How to Configure the SIP Registrar

## Configuring the SIP Registrar

The local SIP gateway that becomes the SIP registrar acts as a backup SIP proxy and accepts SIP Register messages from SIP
                              phones. It becomes a location database of local SIP IP phones.

A registrar accepts SIP Register requests and dynamically builds VoIP dial peers, allowing the Cisco IOS voice gateway software
                              to route calls to SIP phones.

If a SIP Register request has a Contact header that includes a DNS address, the Contact header is resolved before the contact
                              is added to the SIP registrar database. This is done because during a WAN failure (and the resulting Cisco Unified SIP SRST
                              functionality), DNS servers may not be available.

SIP registrar functionality is enabled with the following configuration. By default, Cisco Unified SIP SRST is not enabled
                              and cannot accept SIP Register messages. The following configuration must be set up to accept incoming SIP Register messages.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- allow-connections sip to sip

- sip

- registrar server [ expires [ max sec ]  [ min sec ] ]

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice service voip

### Example:

```
Router(config)# voice service voip
```

Enters voice service configuration mode.

Step 4

allow-connections sip to sip

### Example:

```
Router(config-voi-srv)# allow-connections sip
to sip
```

Allows connections from SIP to SIP endpoints.

Step 5

sip

### Example:

```
Router(config-voi-srv)# sip
```

Enters SIP configuration mode.

Step 6

registrar server [ expires [ max sec ]  [ min sec ] ]

### Example:

```
Router(conf-serv-sip)# registrar server expires
max 600 min 60
```

Enables SIP registrar functionality. The keywords and arguments are defined as follows:

expires: (Optional) Sets the active time for an incoming registration.

max sec: (Optional) Maximum expiration time for a registration, in seconds. The range is from 600 to 86400. The default is
                                                3600.

Ensure that the registration expiration timeout is set to a value smaller than the TCP connection aging timeout to avoid disconnection
                                                            from the TCP.

min sec: (Optional) Minimum expiration time for a registration, in seconds. The range is from 60 to 3600. The default is 60.

Step 7

end

### Example:

```
Router(conf-serv-sip)# end
```

Returns to privileged EXEC mode.

### What to do next

For incoming SIP Register messages to be successfully accepted, users must also set up a voice register pool. See the section Configuring Backup Registrar Service to SIP Phones .

## Configuring Backup Registrar Service to SIP Phones

Backup registrar service to SIP IP phones can be provided by configuring a voice register pool on SIP gateways. The voice
                              register pool configuration provides registration permission control and can also be used to configure some dial-peer attributes
                              that are applied to the dynamically created VoIP dial peers when SIP phone registrations match the pool. The following call
                              types are supported:

SIP IP phone to or from:

Local PSTN

Local analog FXS phones

Local SIP IP phone

The commands in the configuration below provide registration permission control and set up a basic voice register pool. The
                              pool gives users control over which registrations are accepted by a Cisco Unified SIP SRST device and which can be rejected.
                              Registrations that match this pool create VoIP SIP dial peers with the dial-peer attributes set to these configurations. Although
                              only the id command is mandatory, this configuration example shows basic functionality.

For command-level information, see the appropriate command page in Cisco Unified SRST and Cisco Unified SIP SRST Command Reference (All Versions).

### Before you begin

The SIP registrar must be configured before a voice register pool is set up. See the section Configuring the SIP Registrar .

Restrictions

The id command identifies the individual SIP IP phone or sets of SIP IP phones that are to be configured. Thus, the id command configured in Step 5 is required and must be configured before any other voice register pool commands. When the mac address keyword and argument are used, the IP phone must be in the same subnet as that of the router’s LAN interface, such that the
                                    phone’s MAC address is visible in the router’s Address Resolution Protocol (ARP) cache. Once a MAC address is configured for
                                    a specific voice register pool, remove the existing MAC address before changing to a new MAC address.

Proxy dial peers are autogenerated dial peers that route all calls from the PSTN to Cisco Unified SIP SRST. When a SIP phone
                                    registers to Cisco Unified SIP SRST and the proxy command is enabled, two dial peers are automatically created. The first dial peer routes to the proxy, and the second (or
                                    fallback) dial peer routes to the SIP phone. The same functionality can also be achieved with the appropriate creation of
                                    static dial peers (manually creating dial peers that point to the proxy). Proxy dial peers can be monitored to one proxy IP
                                    address, only. That is, only one proxy from a voice registration pool can be monitored at a time. If more than one proxy address
                                    needs to be monitored, you must manually create and configure additional dial peers.

If Jabber for desktop clients must register with Unified SRST, ensure that voice register pools are configured for all desktop computer networks.

To monitor SIP proxies, the call fallback active command must be configured, as described in Step 3

### SUMMARY STEPS

- enable

- configure terminal

- call fallback active

- voice register pool tag

- id { network address mask mask | ip address mask mask | mac address }

- preference preference-order

- proxy ip-address [ preference value [ monitor probe {icmp-ping | rtr } alternate-ip-address ]]

- voice-class codec tag

- (Optional) application application-name

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

call fallback active

### Example:

```
Router(config)# call fallback active
```

Enables a call request to fall back to alternate dial peers in case of network congestion.

This command is used if you want to monitor the proxy dial peer and fallback to the next preferred dial peer. For full information
                                          on the call fallback active command, see PSTN Fallback Feature.

Step 4

voice register pool tag

### Example:

```
Router(config)# voice register pool 12
```

Enters voice register pool configuration mode for SIP phones.

Use this command to control which registrations are accepted or rejected by a Cisco Unified SIP SRST device.

Step 5

id { network address mask mask | ip address mask mask | mac address }

### Example:

```
Router(config-register-pool)# id network
172.16.0.0 mask 255.255.0.0
```

Explicitly identifies a locally available individual or set of SIP IP phones. The keywords and arguments are defined as follows:

network address mask mask : The network address mask mask keyword/argument combination is used to accept SIP Register messages for the indicated phone numbers from any IP phone within
                                                the indicated IP subnet.

ip address mask mask : The ip address mask mask keyword/argument combination is used to identify an individual phone.

mac address : MAC address of a particular Cisco Unified IP Phone.

Step 6

preference preference-order

### Example:

```
Router(config-register-pool)# preference 2
```

Sets the preference order for the VoIP dial peers to be created. Range is from 0 to 10. Default is 0, which is the highest
                                          preference.

The preference must be greater (lower priority) than the preference configured with the preference keyword in the proxy command.

Step 7

proxy ip-address [ preference value [ monitor probe {icmp-ping | rtr } alternate-ip-address ]]

### Example:

```
Router(config-register-pool)# proxy
10.2.161.187 preference 1
```

Autogenerates additional VoIP dial peers to reach the main SIP proxy whenever a Cisco Unified SIP IP Phone registers with
                                          a Cisco Unified SIP SRST gateway. The keywords and arguments are defined as follows:

ip-address : The ip-address of the SIP Proxy.

preference value : Defines the preference of the proxy dial peers that are created. The preference must be less (higher priority) than the
                                                preference configured with the reference command.

Range is from 0 to 10. The highest preference is 0. There is no default.

monitor probe : Enables monitoring of proxy dial peers.

icmp-ping : Enables monitoring of proxy dial peers using ICMP ping.

The dial peer on which the probe is configured will be excluded from call routing only for outbound calls. Inbound calls can
                                                            arrive through this dial peer.

rtr : Enables monitoring of proxy dial peers using RTR probes.

alternate-ip-address : Enables monitoring of alternate IP addresses other than the proxy address. For example, to monitor a gateway front end
                                                to a SIP proxy.

Step 8

voice-class codec tag

### Example:

```
Router(config-register-pool)# voice-class codec
15
```

Sets the voice class codec parameters. The tag argument is a codec group number between 1 and 10000.

Step 9

(Optional) application application-name

### Example:

```
Router(config-register-pool)# application
SIP.App
```

Selects the session-level application on the VoIP dial peer. Use the application-name argument to define a specific interactive voice response (IVR) application.

Step 10

end

### Example:

```
Router(config-register-pool)# end
```

Returns to privileged EXEC mode.

### What to do next

There are several more voice register pool commands that add functionality, but that are not required. See the section Configuring Backup Registrar Service to SIP Phones (Using Optional Commands) for these commands.

## Configuring Backup Registrar Service to SIP Phone (Using Optional Commands)

The prior configurations set up a basic voice register pool. The configuration in this procedure adds optional attributes
                              to increase functionality.

### Before you begin

Prerequisites as described in the Configuring Backup Registrar Service to SIP Phones section.

Configuration of the required commands as described in the Configuring Backup Registrar Service to SIP Phones section .

Before configuring the alias command, translation rules must be set using the translate-outgoing (voice register pool) command.

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool tag

- translation-profile outgoing profile-tag

- alias tag pattern to target [ preference value ]

- cor {incoming | outgoing} cor-list-name {cor-list-number starting-number [- ending-number] | default }

- incoming called-number [ number ]

- number tag number-pattern  { preference value } [ huntstop ]

- dtmf-relay [cisco-rtp] [rtp-nte] [sip-notify]

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice register pool tag

### Example:

```
Router(config)# voice register pool 12
```

Enters voice register pool configuration mode.

Use this command to control which registrations are accepted or rejected by a Cisco Unified SIP SRST device.

Step 4

translation-profile outgoing profile-tag

### Example:

```
Router(config-register-pool)#
voice translation-rule 1
rule 1 /1000/ /1006/
!
!
voice translation-profile 1
translate called 1
!
voice register pool xxx
translation-profile outgoing 1
```

Use this command to apply the translation profile to a specific directory number or to all directory numbers on a SIP phone.

Profile-tag: Translation profile name to handle translation to outgoing calls.

Step 5

alias tag pattern to target [ preference value ]

### Example:

```
Router(config-register-pool)# alias 1 94... to 91011 preference 8
```

Allows Cisco Unified SIP IP Phones to handle inbound PSTN calls to telephone numbers that are unavailable when the main proxy
                                          is not available. The keywords and arguments are defined as follows:

tag : Number from 1 to 5 and the distinguishing factor when there are multiple alias commands.

pattern : The prefix number; matches the incoming telephone number and may include wildcards.

to : Connects the tag number pattern to the alternate number.

target : The target number; an alternate telephone number to route incoming calls to match the number pattern.

preference value : Assigns a dial-peer preference value to the alias. The value argument is the value of the associated dial peer, and the range is from 1 to 10. There is no default.

Step 6

cor {incoming | outgoing} cor-list-name {cor-list-number starting-number [- ending-number] | default }

### Example:

```
Router(config-register-pool)# cor incoming
call91 1 91011
```

Configures a class of restriction (COR) on the VoIP dial peers associated with directory numbers. COR specifies which incoming
                                          dial peers can use which outgoing dial peers to make a call. Each dial peer can be provisioned with an incoming and outgoing
                                          COR list. The keywords and arguments are defined as follows:

incoming : COR list to be used by incoming dial peers.

outgoing : COR list to be used by outgoing dial peers.

cor-list-name : COR list name.

cor-list-number : COR list identifier. The maximum number of COR lists that can be created is four, comprised of incoming or outgoing dial
                                                peers.

starting-number : Start of a directory number range, if an ending number is included. Can also be a standalone number.

Indicator that a full range is configured.

ending-number : End of a directory number range.

default : Instructs the router to use an existing default COR list.

Step 7

incoming called-number [ number ]

### Example:

```
Router(config-register-pool)# incoming
called-number 308
```

Applies incoming called parameters to dynamically created dial peers. The number argument is optional and indicates a sequence
                                          of digits that represent a phone number prefix.

Step 8

number tag number-pattern  { preference value } [ huntstop ]

### Example:

```
Router(config-register-pool)# number 1 50..
preference 2
```

Indicates the E.164 phone numbers that the registrar permits to handle the Register message from the Cisco Unified SIP IP
                                          Phone. The keywords and arguments are defined as follows:

tag : Number from 1 to 10 and the distinguishing factor when there are multiple number commands.

number-pattern : Phone numbers (including wildcards and patterns) that are permitted by the registrar to handle the Register message from
                                                the SIP IP phone.

preference value : Defines the number list preference order.

huntstop : Stops hunting if the dial peer is busy.

Step 9

dtmf-relay [cisco-rtp] [rtp-nte] [sip-notify]

### Example:

```
Router(config-register-pool)# dtmf-relay
rtp-nte
```

Specifies how a SIP gateway relays dual tone multifrequency (DTMF) tones between telephony interfaces and an IP network. The
                                          keywords are defined as follows:

cisco-rtp : Forwards DTMF tones by using Real-Time Transport Protocol (RTP) with a Cisco proprietary payload type.

rtp-nte : Forwards DTMF tones by using RTP with the Named Telephone Event (NTE) payload type.

sip-notify : Forwards DTMF tones using SIP NOTIFY messages.

Step 10

end

### Example:

```
Router(config-register-pool)# end
```

Returns to privileged EXEC mode.

### Example

The following partial output from the show running-config command shows that voice register pool 12 is configured to accept
                              all registrations from SIP IP phones with extension number 50xx from the 172.16.0.0/16 network. Autogenerated dial peers for
                              registrations that match pool 12 have attributes configured in this pool.

```
.
.
.
voice register pool 12
id network 172.16.0.0 mask 255.255.0.0
number 1 50.. preference 2
application SIP.app
preference 2
incoming called-number
cor incoming allowall default
translate-outgoing called 1
voice-class codec 1
.
.
.
```

## Verifying SIP Registrar Configuration

To help you troubleshoot a SIP registrar and voice register pool, perform the following steps.

### SUMMARY STEPS

- debug voice register errors

- debug voice register events

- show sip-ua status registrar

### DETAILED STEPS

Step 1

debug voice register errors

### Example:

```
Router# debug voice register errors
*Apr 22 11:52:54.523 PDT: VOICE_REG_POOL: Contact
doesn't match any pools
*Apr 22 11:52:54.539 PDT: VOICE_REG_POOL: Register
request for (33015) from (10.2.152.39)
*Apr 22 11:52:54.539 PDT: VOICE_REG_POOL: Contact
doesn't match any pools.
*Apr 22 11:52:54.559 PDT: VOICE_REG_POOL: Register
request for (33017) from (10.2.152.39)
*Apr 22 11:53:04.559 PDT: VOICE_REG_POOL: Maximum
registration threshold for pool(3) hit
```

Use this command to debug errors that happen during registration.

If there are no voice register pools configured for a particular registration request, the message Contact doesn’t match any pools is displayed.

Step 2

debug voice register events

### Example:

```
Router# debug voice register events
Apr 22 10:50:21.731 PDT: VOICE_REG_POOL: Contact
matches pool 1
Apr 22 10:50:21.731 PDT: VOICE_REG_POOL: key(91011)
contact(192.168.0.2) add to contact table
Apr 22 10:50:21.731 PDT: VOICE_REG_POOL: key(91011)
exists in contact table
Apr 22 10:50:21.731 PDT: VOICE_REG_POOL:
contact(192.168.0.2) exists in contact table, ref
updated
Apr 22 10:50:21.731 PDT: VOICE_REG_POOL: Created
dial-peer entry of type 1
Apr 22 10:50:21.731 PDT: VOICE_REG_POOL:
Registration successful for 91011, registration id
is 257
```

Using the debug voice register events command should suffice to display registration activity. Registration activity includes matching of pools, registration creation,
                                          and automatic creation of dial peers. For more details and error conditions, you can use the debug voice register errors command.

The phone number 91011 registered successfully, and type 1 is reported, which means there is a pre-existing VoIP dial peer.

Step 3

show sip-ua status registrar

### Example:

```
Router# show sip-ua status registrar
Line    destination expires(sec) contact
======= =========== ============ =======
91021   192.168.0.3 227          192.168.0.3
91011   192.168.0.2 176          192.168.0.2
95021   10.2.161.50 419          10.2.161.50
95012   10.2.161.50 419          10.2.161.50
95011   10.2.161.50 420          10.2.161.50
95500   10.2.161.50 420          10.2.161.50
94011   10.2.161.40 128          10.2.161.40
94500   10.2.161.40 129          10.2.161.40
```

Use this command to display all the SIP endpoints currently registered with the contact address.

## Verifying Proxy Dial-Peer Configuration

To use the icmp-ping keyword with the proxy command to assist in troubleshooting proxy dial peers, perform the following steps.

### SUMMARY STEPS

- configure terminal

- voice register pool

- proxy ip-address [ preference value ] [ monitor probe {icmp-ping|rtr} [ alternate-ip-address ]]

- end

- show voice register dial-peers

- show dial-peer voice

### DETAILED STEPS

Step 1

configure terminal

### Example:

```
Router# configure terminal
```

Use this command to enter global configuration mode.

Step 2

voice register pool

### Example:

```
Router(config)# voice register pool 1
```

Use this command to enter voice register pool configuration mode.

Step 3

proxy ip-address [ preference value ] [ monitor probe {icmp-ping|rtr} [ alternate-ip-address ]]

### Example:

```
Router(config-register-pool)# proxy 10.2.161.187
preference 1 monitor probe icmp-ping
```

Set the proxy command to monitor with icmp-ping .

Step 4

end

### Example:

```
Router(config-register-pool)# end
```

Returns to privileged EXEC mode.

Step 5

show voice register dial-peers

### Example:

```
Router# show voice register dial-peers
dial-peer voice 40035 voip
preference 5
destination-pattern 91011
session target ipv4:192.168.0.2
session protocol sipv2
voice-class codec 1
dial-peer voice 40036 voip
preference 1
destination-pattern 91011
session target ipv4:10.2.161.187
session protocol sipv2
voice-class codec 1
monitor probe icmp-ping 10.2.161.187
```

Use this command to verify dial-peer configurations, and notice that icmp-ping monitoring is set.

Step 6

show dial-peer voice

### Example:

```
Router# show dial-peer voice
VoiceOverIpPeer40036
peer type = voice, information type = voice,
description = `',
tag = 40036, destination-pattern = `91011',
answer-address = `', preference=1,
CLID Restriction = None
CLID Network Number = `'
CLID Second Number sent
source carrier-id = `', target carrier-id = `',
source trunk-group-label = `', target
trunk-group-label = `',
numbering Type = `unknown'
group = 40036, Admin state is up, Operation state is
up,
incoming called-number = `', connections/maximum =
0/unlimited,
! Default output for incoming called-number command
DTMF Relay = disabled,
modem transport = system,
huntstop = disabled,
in bound application associated: 'DEFAULT'
out bound application associated: ''
dnis-map =
permission :both
incoming COR list:maximum capability
! Default output for cor command
outgoing COR list:minimum requirement
! Default output for cor command
Translation profile (Incoming):
Translation profile (Outgoing):
incoming call blocking:
translation-profile = `'
disconnect-cause = `no-service'
advertise 0x40 capacity_update_timer 25 addrFamily 4
oldAddrFamily 4
type = voip, session-target = `ipv4:10.2.161.187',
technology prefix:
settle-call = disabled
ip media DSCP = ef, ip signaling DSCP = af31,
ip video rsvp-none DSCP = af41,ip video rsvp-pass
DSCP = af41
ip video rsvp-fail DSCP = af41,
UDP checksum = disabled,
session-protocol = sipv2, session-transport =
system,
req-qos = best-effort, acc-qos = best-effort,
req-qos video = best-effort, acc-qos video =
best-effort,
req-qos audio def bandwidth = 64, req-qos audio max
bandwidth = 0,
req-qos video def bandwidth = 384, req-qos video max
bandwidth = 0,
RTP dynamic payload type values: NTE = 101
Cisco: NSE=100, fax=96, fax-ack=97, dtmf=121,
fax-relay=122
S=123, ClearChan=125, PCM switch over
u-law=0,A-law=8
RTP comfort noise payload type = 19
fax rate = voice, payload size = 20 bytes
fax protocol = system
fax-relay ecm enable
fax NSF = 0xAD0051 (default)
codec = g729r8, payload size = 20 bytes,
Media Setting = flow-through (global)
Expect factor = 0, Icpif = 20,
Playout Mode is set to adaptive,
Initial 60 ms, Max 300 ms
Playout-delay Minimum mode is set to default, value
40 ms
Fax nominal 300 ms
Max Redirects = 1, signaling-type = cas,
VAD = enabled, Poor QOV Trap = disabled,
Source Interface = NONE
voice class sip url = system,
voice class sip rel1xx = system,
monitor probe method: icmp-ping ip address:
10.2.161.187,
Monitored destination reachable
voice class perm tag = `'
Time elapsed since last clearing of voice call
statistics never
Connect Time = 0, Charged Units = 0,
Successful Calls = 0, Failed Calls = 0, Incomplete
Calls = 0
Accepted Calls = 0, Refused Calls = 0,
Last Disconnect Cause is "",
Last Disconnect Text is "",
Last Setup Time = 0.
```

Use the show dial-peer voice command on dial peer 40036, and notice the monitor probe status.

Also highlighted is the output of the cor and incoming called-number commands.

### What to do next

The next step is configuring incoming and outgoing calls for Cisco Unified SRST. For more information, see the Configuring Call Handling section.

## IPv6 Support for Unified SRST SIP IP Phones

Internet Protocol version 6 (IPv6) is the latest version of the Internet Protocol (IP). IPv6 uses packets to exchange data,
                           voice, and video traffic over digital networks. Also, IPv6 increases the number of network address bits from 32 bits in IPv4
                           to 128 bits. From Unified SRST Release 12.0 onwards, Unified SRST supports IPv6 protocols for SIP IP phones.

IPv6 support in Unified SRST allows the network to behave transparently in a dual-stack (IPv4 and IPv6) environment and provides
                           additional IP address space to SIP IP phones that are connected to the network. If you do not have a dual-stack configuration,
                           configure the CLI command call service stop under voice service voip configuration mode before changing to dual-stack mode. For an example of switching to dual-stack mode, see Examples for Configuring IPv6 Pools for SIP IP Phones .

The Cisco IP Phone 7800 Series and 8800 Series are supported on IPv6 for Unified SRST.

For more information on configuring SIP IP phones for IPv6 source address, see Configure IPv6 Pools for SIP IP Phones .

For an example of configuring IPv6 Support on Unified SRST, see Examples for Configuring IPv6 Pools for SIP IP Phones .

For more details about IPv6 deployment, see IPv6 Deployment Guide for Cisco Collaboration Systems Release 12.0 .

### Feature Support for IPv6 in Unified SRST SIP IP Phones

The basic feature supported for a IPv6 WAN down scenario is:

Basic SIP Line (IPv4 or IPv6) to SIP Line calls (IPv4 or IPv6) when Unified SRST is in dual-stack no anat mode.

The following supplementary services are supported as part of IPv6 in Unified SRST IP Phones:

Hold/Resume

Call Forward

Call Transfer

Three-way Conference (with BIB conferencing only)

Line to T1/E1 Trunk and Trunk to Line with Supplementary Service Features

Fax to and from PSTN (IPv4 ATA to ISDN T1/E1) for both T.38 Fax Relay and Fax Passthrough

### Restrictions

The following are the known restrictions for IPv6 support on Unified SRST:

SIP Trunks are not supported on Unified SRST for IPv6 deployment. PSTN calls are supported only through T1/E1 trunks.

SCCP IP Phones are not supported in a deployment of IPv6 for Unified SRST.

SIP Phones can be either in IPv4 only or IPv6 only mode ( no anat ).

Trancoding and Transrating are not supported.

H.323 trunks are not supported.

Secure SIP lines or trunks are not supported.

IPv6 on Unified SRST is not supported on the Cisco IOS platform. The support is restricted to Cisco IOS XE platform with Cisco
                                    IOS Release 16.6.1 or later versions.

For IPv6 Support on Unified SRST, all the legacy IP Phones and Voice Gateways must be converted or reconfigured to IPv4-Only
                                    SIP signaling from SCCP signaling, if applicable.

### Configure IPv6 Pools for SIP IP Phones

#### Before you begin

Unified SRST 12.0 or a later version.

IPv6 option only appears if protocol mode is dual-stack configured under sip-ua configuration mode or IPv6.

Cisco Unified SRST License must be configured for the gateway to function as a Unified SRST gateway to support IPv6 functionality.
                                       For more information on licenses, see Licensing .

Cisco Unified Communications Manager (Unified Communications Manager) is provisioned with the IPv6 address of Unified SRST.
                                       For information on configuration of Unified SRST on Unified Communications Manager, see Survivable Remote Site Telephony Configuration in Cisco Unified Communications Manager Administration Guide.

### SUMMARY STEPS

- enable

- configure terminal

- ipv6 unicast-routing

- voice service voip

- sip

- no anat

- call service stop

- exit

- exit

- sip-ua

- protocol mode { ipv4 | ipv6 | dual-stack [ preference { ipv4 | ipv6 } ] }

- exit

- voice service { voip }

- sip

- no call service stop

- exit

- voice register global

- default mode

- max-dn max-directory-numbers

- max-pool max-voice-register-pools

- exit

- voice register pool pool-tag

- id { network address mask mask | ip address mask mask | mac address }

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router #configure terminal
```

Enters global configuration mode.

Step 3

ipv6 unicast-routing

#### Example:

```
Router(config)# ipv6 unicast-routing
```

Enables the forwarding of IPv6 unicast datagrams.

Step 4

voice service voip

#### Example:

```
Router (config)# voice service voip
```

Enters voice-service configuration mode to specify a voice encapsulation type.

voip — Specifies Voice over IP (VoIP) parameters.

Step 5

sip

#### Example:

```
Router(config-voi-serv)# sip
```

Enters SIP configuration mode.

Step 6

no anat

#### Example:

```
Router(config-serv-sip)# no anat
```

Disables Alternative Network Address Types (ANAT) on a SIP trunk.

Step 7

call service stop

#### Example:

```
Router(config-serv-sip)# call service stop
```

Shuts down SIP call service.

Step 8

exit

#### Example:

```
Router(config-serv-sip)# exit
```

Exits SIP configuration mode.

Step 9

exit

#### Example:

```
Router(config-voi-sip)# exit
```

Exits voice service voip configuration mode.

Step 10

sip-ua

#### Example:

```
Router(config)# sip-ua
```

Enters SIP user-agent configuration mode.

Step 11

protocol mode { ipv4 | ipv6 | dual-stack [ preference { ipv4 | ipv6 } ] }

#### Example:

```
Router(config-sip-ua)# protocol mode dual-stack
preference ipv6
```

Allows phones to interact with phones on IPv6 voice gateways. You can configure phones for IPv4 addresses, IPv6 address es,
                                             or for a dual-stack mode.

ipv4—Allows you to set the protocol mode as an IPv4 address.

ipv6—Allows you to set the protocol mode as an IPv6 address.

dual-stack—Allows you to set the protocol mode for both IPv4 and IPv6 addresses.

preference—Allows you to choose a preferred IP address family if protocol mode is dual-stack.

Step 12

exit

#### Example:

```
Router(config-sip-ua)# exit
```

Exits SIP configuration mode.

Step 13

voice service { voip }

#### Example:

```
Router (config)# voice service voip
```

Enters voice-service configuration mode to specify a voice encapsulation type.

voip — Specifies Voice over IP (VoIP) parameters.

Step 14

sip

#### Example:

```
Router(config-voi-serv)# sip
```

Enters SIP configuration mode.

Step 15

no call service stop

#### Example:

```
Router(config-serv-sip)# call service stop
```

Activates SIP call service.

Step 16

exit

#### Example:

```
Router(config-serv-sip)# exit
```

Exits SIP configuration mode.

Step 17

voice register global

#### Example:

```
Router(config)# voice register global
```

Enters voice register global configuration mode to set parameters for all supported SIP phones in Cisco Unified CME.

Step 18

default mode

#### Example:

```
Router(config-register-global)# default mode
```

Enables mode for provisioning SIP phones in Unified SRST. The default mode is Unified SRST itself.

Step 19

max-dn max-directory-numbers

#### Example:

```
Router(config-register-global)# max-dn 50
```

Limits number of directory numbers to be supported by this router.

Maximum number is platform and version-specific. Type ? for value.

Step 20

max-pool max-voice-register-pools

#### Example:

```
Router(config-register-global)# max-pool 40
```

Sets maximum number of SIP phones to be supported by the Unified SRST router.

Step 21

exit

#### Example:

```
Router(config-register-global)# exit
```

Exits voice register global configuration mode.

Step 22

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 1
```

Enters voice register pool configuration mode to set phone-specific parameters for a SIP phone.

Step 23

id { network address mask mask | ip address mask mask | mac address }

#### Example:

```
Router(config-register-pool)# id network
2001:420:54FF:13::901:0/117
```

```
Router(config-register-pool)# id network
10.64.88.0 mask 255.255.255.0
```

Explicitly identifies a locally available individual SIP phone to support a degree of authentication.

Step 24

end

#### Example:

```
Router(config)# end
```

Exits to privileged EXEC mode.

### Examples for Configuring IPv6 Pools for SIP IP Phones

The following example provides configuration of IPv6 pools for SIP IP Phones:

```
ipv6 unicast-routing
voice service voip
sip
no anat
call service stop
exit
exit
sip-ua
protocol mode dual-stack
exit
voice service voip
sip
no call service stop
exit
voice register global
default mode
max-dn 50
max-pool 40
exit
voice register pool 1
id network 2001:420:54FF:13::901:0/117
end
```

The following example provides interface configuration for IPv6 supported on Unified SRST:

```
configure terminal
interface GigabitEthernet0/0/1
 ip address 10.64.86.229 255.255.255.0
 negotiation auto
 ipv6 address 2001:420:54FF:13::312:82/119
 ipv6 enable
```

The following example provides IP route configuration for IPv6 supported on Unified SRST:

```
ipv6 route 2001:420:54FF:13::312:0/119 2001:420:54FF:13::312:1
ipv6 route 2001:420:54FF:13::901:0/119 2001:420:54FF:13::312:1
```

The following example displays output when SIP call service is shut down with the call service stop CLI command:

```
Router# show sip service
SIP service is shut
under voice service voip, sip submode
```

The following example displays output when SIP call service is active with the no call service stop CLI command:

```
Router# show sip-ua service
SIP Service is up
under voice service voip, sip submode
```

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice service configuration mode. |
| Step 4 | allow-connections sip to sip Example: Router(config-voi-srv)# allow-connections sip
to sip | Allows connections from SIP to SIP endpoints. |
| Step 5 | sip Example: Router(config-voi-srv)# sip | Enters SIP configuration mode. |
| Step 6 | registrar server [ expires [ max sec ]  [ min sec ] ] Example: Router(conf-serv-sip)# registrar server expires
max 600 min 60 | Enables SIP registrar functionality. The keywords and arguments are defined as follows: expires: (Optional) Sets the active time for an incoming registration. max sec: (Optional) Maximum expiration time for a registration, in seconds. The range is from 600 to 86400. The default is
                                                3600. Note Ensure that the registration expiration timeout is set to a value smaller than the TCP connection aging timeout to avoid disconnection
                                                            from the TCP. min sec: (Optional) Minimum expiration time for a registration, in seconds. The range is from 60 to 3600. The default is 60. | Note | Ensure that the registration expiration timeout is set to a value smaller than the TCP connection aging timeout to avoid disconnection
                                                            from the TCP. |
| Note | Ensure that the registration expiration timeout is set to a value smaller than the TCP connection aging timeout to avoid disconnection
                                                            from the TCP. |
| Step 7 | end Example: Router(conf-serv-sip)# end | Returns to privileged EXEC mode. |

| Note | Ensure that the registration expiration timeout is set to a value smaller than the TCP connection aging timeout to avoid disconnection
                                                            from the TCP. |
|---|---|

| Note | To monitor SIP proxies, the call fallback active command must be configured, as described in Step 3 |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | call fallback active Example: Router(config)# call fallback active | Enables a call request to fall back to alternate dial peers in case of network congestion. This command is used if you want to monitor the proxy dial peer and fallback to the next preferred dial peer. For full information
                                          on the call fallback active command, see PSTN Fallback Feature. |
| Step 4 | voice register pool tag Example: Router(config)# voice register pool 12 | Enters voice register pool configuration mode for SIP phones. Use this command to control which registrations are accepted or rejected by a Cisco Unified SIP SRST device. |
| Step 5 | id { network address mask mask \| ip address mask mask \| mac address } Example: Router(config-register-pool)# id network
172.16.0.0 mask 255.255.0.0 | Explicitly identifies a locally available individual or set of SIP IP phones. The keywords and arguments are defined as follows: network address mask mask : The network address mask mask keyword/argument combination is used to accept SIP Register messages for the indicated phone numbers from any IP phone within
                                                the indicated IP subnet. ip address mask mask : The ip address mask mask keyword/argument combination is used to identify an individual phone. mac address : MAC address of a particular Cisco Unified IP Phone. |
| Step 6 | preference preference-order Example: Router(config-register-pool)# preference 2 | Sets the preference order for the VoIP dial peers to be created. Range is from 0 to 10. Default is 0, which is the highest
                                          preference. The preference must be greater (lower priority) than the preference configured with the preference keyword in the proxy command. |
| Step 7 | proxy ip-address [ preference value [ monitor probe {icmp-ping \| rtr } alternate-ip-address ]] Example: Router(config-register-pool)# proxy
10.2.161.187 preference 1 | Autogenerates additional VoIP dial peers to reach the main SIP proxy whenever a Cisco Unified SIP IP Phone registers with
                                          a Cisco Unified SIP SRST gateway. The keywords and arguments are defined as follows: ip-address : The ip-address of the SIP Proxy. preference value : Defines the preference of the proxy dial peers that are created. The preference must be less (higher priority) than the
                                                preference configured with the reference command. Range is from 0 to 10. The highest preference is 0. There is no default. monitor probe : Enables monitoring of proxy dial peers. icmp-ping : Enables monitoring of proxy dial peers using ICMP ping. Note The dial peer on which the probe is configured will be excluded from call routing only for outbound calls. Inbound calls can
                                                            arrive through this dial peer. rtr : Enables monitoring of proxy dial peers using RTR probes. alternate-ip-address : Enables monitoring of alternate IP addresses other than the proxy address. For example, to monitor a gateway front end
                                                to a SIP proxy. | Note | The dial peer on which the probe is configured will be excluded from call routing only for outbound calls. Inbound calls can
                                                            arrive through this dial peer. |
| Note | The dial peer on which the probe is configured will be excluded from call routing only for outbound calls. Inbound calls can
                                                            arrive through this dial peer. |
| Step 8 | voice-class codec tag Example: Router(config-register-pool)# voice-class codec
15 | Sets the voice class codec parameters. The tag argument is a codec group number between 1 and 10000. |
| Step 9 | (Optional) application application-name Example: Router(config-register-pool)# application
SIP.App | (Optional) Selects the session-level application on the VoIP dial peer. Use the application-name argument to define a specific interactive voice response (IVR) application. |
| Step 10 | end Example: Router(config-register-pool)# end | Returns to privileged EXEC mode. |

| Note | The dial peer on which the probe is configured will be excluded from call routing only for outbound calls. Inbound calls can
                                                            arrive through this dial peer. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice register pool tag Example: Router(config)# voice register pool 12 | Enters voice register pool configuration mode. Use this command to control which registrations are accepted or rejected by a Cisco Unified SIP SRST device. |
| Step 4 | translation-profile outgoing profile-tag Example: Router(config-register-pool)#
voice translation-rule 1
rule 1 /1000/ /1006/
!
!
voice translation-profile 1
translate called 1
!
voice register pool xxx
translation-profile outgoing 1 | Use this command to apply the translation profile to a specific directory number or to all directory numbers on a SIP phone. Profile-tag: Translation profile name to handle translation to outgoing calls. |
| Step 5 | alias tag pattern to target [ preference value ] Example: Router(config-register-pool)# alias 1 94... to 91011 preference 8 | Allows Cisco Unified SIP IP Phones to handle inbound PSTN calls to telephone numbers that are unavailable when the main proxy
                                          is not available. The keywords and arguments are defined as follows: tag : Number from 1 to 5 and the distinguishing factor when there are multiple alias commands. pattern : The prefix number; matches the incoming telephone number and may include wildcards. to : Connects the tag number pattern to the alternate number. target : The target number; an alternate telephone number to route incoming calls to match the number pattern. preference value : Assigns a dial-peer preference value to the alias. The value argument is the value of the associated dial peer, and the range is from 1 to 10. There is no default. |
| Step 6 | cor {incoming \| outgoing} cor-list-name {cor-list-number starting-number [- ending-number] \| default } Example: Router(config-register-pool)# cor incoming
call91 1 91011 | Configures a class of restriction (COR) on the VoIP dial peers associated with directory numbers. COR specifies which incoming
                                          dial peers can use which outgoing dial peers to make a call. Each dial peer can be provisioned with an incoming and outgoing
                                          COR list. The keywords and arguments are defined as follows: incoming : COR list to be used by incoming dial peers. outgoing : COR list to be used by outgoing dial peers. cor-list-name : COR list name. cor-list-number : COR list identifier. The maximum number of COR lists that can be created is four, comprised of incoming or outgoing dial
                                                peers. starting-number : Start of a directory number range, if an ending number is included. Can also be a standalone number. Indicator that a full range is configured. ending-number : End of a directory number range. default : Instructs the router to use an existing default COR list. |
| Step 7 | incoming called-number [ number ] Example: Router(config-register-pool)# incoming
called-number 308 | Applies incoming called parameters to dynamically created dial peers. The number argument is optional and indicates a sequence
                                          of digits that represent a phone number prefix. |
| Step 8 | number tag number-pattern  { preference value } [ huntstop ] Example: Router(config-register-pool)# number 1 50..
preference 2 | Indicates the E.164 phone numbers that the registrar permits to handle the Register message from the Cisco Unified SIP IP
                                          Phone. The keywords and arguments are defined as follows: tag : Number from 1 to 10 and the distinguishing factor when there are multiple number commands. number-pattern : Phone numbers (including wildcards and patterns) that are permitted by the registrar to handle the Register message from
                                                the SIP IP phone. preference value : Defines the number list preference order. huntstop : Stops hunting if the dial peer is busy. |
| Step 9 | dtmf-relay [cisco-rtp] [rtp-nte] [sip-notify] Example: Router(config-register-pool)# dtmf-relay
rtp-nte | Specifies how a SIP gateway relays dual tone multifrequency (DTMF) tones between telephony interfaces and an IP network. The
                                          keywords are defined as follows: cisco-rtp : Forwards DTMF tones by using Real-Time Transport Protocol (RTP) with a Cisco proprietary payload type. rtp-nte : Forwards DTMF tones by using RTP with the Named Telephone Event (NTE) payload type. sip-notify : Forwards DTMF tones using SIP NOTIFY messages. |
| Step 10 | end Example: Router(config-register-pool)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | debug voice register errors Example: Router# debug voice register errors
*Apr 22 11:52:54.523 PDT: VOICE_REG_POOL: Contact
doesn't match any pools
*Apr 22 11:52:54.539 PDT: VOICE_REG_POOL: Register
request for (33015) from (10.2.152.39)
*Apr 22 11:52:54.539 PDT: VOICE_REG_POOL: Contact
doesn't match any pools.
*Apr 22 11:52:54.559 PDT: VOICE_REG_POOL: Register
request for (33017) from (10.2.152.39)
*Apr 22 11:53:04.559 PDT: VOICE_REG_POOL: Maximum
registration threshold for pool(3) hit | Use this command to debug errors that happen during registration. If there are no voice register pools configured for a particular registration request, the message Contact doesn’t match any pools is displayed. |
| Step 2 | debug voice register events Example: Router# debug voice register events
Apr 22 10:50:21.731 PDT: VOICE_REG_POOL: Contact
matches pool 1
Apr 22 10:50:21.731 PDT: VOICE_REG_POOL: key(91011)
contact(192.168.0.2) add to contact table
Apr 22 10:50:21.731 PDT: VOICE_REG_POOL: key(91011)
exists in contact table
Apr 22 10:50:21.731 PDT: VOICE_REG_POOL:
contact(192.168.0.2) exists in contact table, ref
updated
Apr 22 10:50:21.731 PDT: VOICE_REG_POOL: Created
dial-peer entry of type 1
Apr 22 10:50:21.731 PDT: VOICE_REG_POOL:
Registration successful for 91011, registration id
is 257 | Using the debug voice register events command should suffice to display registration activity. Registration activity includes matching of pools, registration creation,
                                          and automatic creation of dial peers. For more details and error conditions, you can use the debug voice register errors command. The phone number 91011 registered successfully, and type 1 is reported, which means there is a pre-existing VoIP dial peer. |
| Step 3 | show sip-ua status registrar Example: Router# show sip-ua status registrar
Line    destination expires(sec) contact
======= =========== ============ =======
91021   192.168.0.3 227          192.168.0.3
91011   192.168.0.2 176          192.168.0.2
95021   10.2.161.50 419          10.2.161.50
95012   10.2.161.50 419          10.2.161.50
95011   10.2.161.50 420          10.2.161.50
95500   10.2.161.50 420          10.2.161.50
94011   10.2.161.40 128          10.2.161.40
94500   10.2.161.40 129          10.2.161.40 | Use this command to display all the SIP endpoints currently registered with the contact address. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | configure terminal Example: Router# configure terminal | Use this command to enter global configuration mode. |
| Step 2 | voice register pool Example: Router(config)# voice register pool 1 | Use this command to enter voice register pool configuration mode. |
| Step 3 | proxy ip-address [ preference value ] [ monitor probe {icmp-ping\|rtr} [ alternate-ip-address ]] Example: Router(config-register-pool)# proxy 10.2.161.187
preference 1 monitor probe icmp-ping | Set the proxy command to monitor with icmp-ping . |
| Step 4 | end Example: Router(config-register-pool)# end | Returns to privileged EXEC mode. |
| Step 5 | show voice register dial-peers Example: Router# show voice register dial-peers
dial-peer voice 40035 voip
preference 5
destination-pattern 91011
session target ipv4:192.168.0.2
session protocol sipv2
voice-class codec 1
dial-peer voice 40036 voip
preference 1
destination-pattern 91011
session target ipv4:10.2.161.187
session protocol sipv2
voice-class codec 1
monitor probe icmp-ping 10.2.161.187 | Use this command to verify dial-peer configurations, and notice that icmp-ping monitoring is set. |
| Step 6 | show dial-peer voice Example: Router# show dial-peer voice
VoiceOverIpPeer40036
peer type = voice, information type = voice,
description = `',
tag = 40036, destination-pattern = `91011',
answer-address = `', preference=1,
CLID Restriction = None
CLID Network Number = `'
CLID Second Number sent
source carrier-id = `', target carrier-id = `',
source trunk-group-label = `', target
trunk-group-label = `',
numbering Type = `unknown'
group = 40036, Admin state is up, Operation state is
up,
incoming called-number = `', connections/maximum =
0/unlimited,
! Default output for incoming called-number command
DTMF Relay = disabled,
modem transport = system,
huntstop = disabled,
in bound application associated: 'DEFAULT'
out bound application associated: ''
dnis-map =
permission :both
incoming COR list:maximum capability
! Default output for cor command
outgoing COR list:minimum requirement
! Default output for cor command
Translation profile (Incoming):
Translation profile (Outgoing):
incoming call blocking:
translation-profile = `'
disconnect-cause = `no-service'
advertise 0x40 capacity_update_timer 25 addrFamily 4
oldAddrFamily 4
type = voip, session-target = `ipv4:10.2.161.187',
technology prefix:
settle-call = disabled
ip media DSCP = ef, ip signaling DSCP = af31,
ip video rsvp-none DSCP = af41,ip video rsvp-pass
DSCP = af41
ip video rsvp-fail DSCP = af41,
UDP checksum = disabled,
session-protocol = sipv2, session-transport =
system,
req-qos = best-effort, acc-qos = best-effort,
req-qos video = best-effort, acc-qos video =
best-effort,
req-qos audio def bandwidth = 64, req-qos audio max
bandwidth = 0,
req-qos video def bandwidth = 384, req-qos video max
bandwidth = 0,
RTP dynamic payload type values: NTE = 101
Cisco: NSE=100, fax=96, fax-ack=97, dtmf=121,
fax-relay=122
S=123, ClearChan=125, PCM switch over
u-law=0,A-law=8
RTP comfort noise payload type = 19
fax rate = voice, payload size = 20 bytes
fax protocol = system
fax-relay ecm enable
fax NSF = 0xAD0051 (default)
codec = g729r8, payload size = 20 bytes,
Media Setting = flow-through (global)
Expect factor = 0, Icpif = 20,
Playout Mode is set to adaptive,
Initial 60 ms, Max 300 ms
Playout-delay Minimum mode is set to default, value
40 ms
Fax nominal 300 ms
Max Redirects = 1, signaling-type = cas,
VAD = enabled, Poor QOV Trap = disabled,
Source Interface = NONE
voice class sip url = system,
voice class sip rel1xx = system,
monitor probe method: icmp-ping ip address:
10.2.161.187,
Monitored destination reachable
voice class perm tag = `'
Time elapsed since last clearing of voice call
statistics never
Connect Time = 0, Charged Units = 0,
Successful Calls = 0, Failed Calls = 0, Incomplete
Calls = 0
Accepted Calls = 0, Refused Calls = 0,
Last Disconnect Cause is "",
Last Disconnect Text is "",
Last Setup Time = 0. | Use the show dial-peer voice command on dial peer 40036, and notice the monitor probe status. Note Also highlighted is the output of the cor and incoming called-number commands. | Note | Also highlighted is the output of the cor and incoming called-number commands. |
| Note | Also highlighted is the output of the cor and incoming called-number commands. |

| Note | Also highlighted is the output of the cor and incoming called-number commands. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router #configure terminal | Enters global configuration mode. |
| Step 3 | ipv6 unicast-routing Example: Router(config)# ipv6 unicast-routing | Enables the forwarding of IPv6 unicast datagrams. |
| Step 4 | voice service voip Example: Router (config)# voice service voip | Enters voice-service configuration mode to specify a voice encapsulation type. voip — Specifies Voice over IP (VoIP) parameters. |
| Step 5 | sip Example: Router(config-voi-serv)# sip | Enters SIP configuration mode. |
| Step 6 | no anat Example: Router(config-serv-sip)# no anat | Disables Alternative Network Address Types (ANAT) on a SIP trunk. |
| Step 7 | call service stop Example: Router(config-serv-sip)# call service stop | Shuts down SIP call service. |
| Step 8 | exit Example: Router(config-serv-sip)# exit | Exits SIP configuration mode. |
| Step 9 | exit Example: Router(config-voi-sip)# exit | Exits voice service voip configuration mode. |
| Step 10 | sip-ua Example: Router(config)# sip-ua | Enters SIP user-agent configuration mode. |
| Step 11 | protocol mode { ipv4 \| ipv6 \| dual-stack [ preference { ipv4 \| ipv6 } ] } Example: Router(config-sip-ua)# protocol mode dual-stack
preference ipv6 | Allows phones to interact with phones on IPv6 voice gateways. You can configure phones for IPv4 addresses, IPv6 address es,
                                             or for a dual-stack mode. ipv4—Allows you to set the protocol mode as an IPv4 address. ipv6—Allows you to set the protocol mode as an IPv6 address. dual-stack—Allows you to set the protocol mode for both IPv4 and IPv6 addresses. preference—Allows you to choose a preferred IP address family if protocol mode is dual-stack. |
| Step 12 | exit Example: Router(config-sip-ua)# exit | Exits SIP configuration mode. |
| Step 13 | voice service { voip } Example: Router (config)# voice service voip | Enters voice-service configuration mode to specify a voice encapsulation type. voip — Specifies Voice over IP (VoIP) parameters. |
| Step 14 | sip Example: Router(config-voi-serv)# sip | Enters SIP configuration mode. |
| Step 15 | no call service stop Example: Router(config-serv-sip)# call service stop | Activates SIP call service. |
| Step 16 | exit Example: Router(config-serv-sip)# exit | Exits SIP configuration mode. |
| Step 17 | voice register global Example: Router(config)# voice register global | Enters voice register global configuration mode to set parameters for all supported SIP phones in Cisco Unified CME. |
| Step 18 | default mode Example: Router(config-register-global)# default mode | Enables mode for provisioning SIP phones in Unified SRST. The default mode is Unified SRST itself. |
| Step 19 | max-dn max-directory-numbers Example: Router(config-register-global)# max-dn 50 | Limits number of directory numbers to be supported by this router. Maximum number is platform and version-specific. Type ? for value. |
| Step 20 | max-pool max-voice-register-pools Example: Router(config-register-global)# max-pool 40 | Sets maximum number of SIP phones to be supported by the Unified SRST router. |
| Step 21 | exit Example: Router(config-register-global)# exit | Exits voice register global configuration mode. |
| Step 22 | voice register pool pool-tag Example: Router(config)# voice register pool 1 | Enters voice register pool configuration mode to set phone-specific parameters for a SIP phone. |
| Step 23 | id { network address mask mask \| ip address mask mask \| mac address } Example: Router(config-register-pool)# id network
2001:420:54FF:13::901:0/117 Router(config-register-pool)# id network
10.64.88.0 mask 255.255.255.0 | Explicitly identifies a locally available individual SIP phone to support a degree of authentication. |
| Step 24 | end Example: Router(config)# end | Exits to privileged EXEC mode. |