---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-admin-sccp-sip-srst-configuration-guide-sccp-and-sip-srst-admin-guide-a3e4a790c7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/admin/sccp_sip_srst/configuration/guide/SCCP_and_SIP_SRST_Admin_Guide/srst_sip_trunking.html
retrieved_at: 2026-08-16T23:04:57.180968+00:00
---

Cisco Unified SRST Administration Guide (All Versions)

# Cisco Unified SRST Administration Guide (All Versions)

Updated: April 25, 2026

Chapter: Configuring SIP Trunking on Unified SRST

## Chapter: Configuring SIP Trunking on Unified SRST

# Configuring SIP Trunking on Unified SRST

This chapter describes how to configure SIP trunking on Cisco Unified Survivable Remote Site Telephony (Unified SRST).

This chapter describes the configuration recommendations and details on the various line side and SIP trunking features on
                        Unified SRST. Also, details are provided on the co-location of Unified Border Element and Unified SRST.

## Unified SRST and Unified Border Element Co-location

For Unified SRST Release 12.1 and later releases, you can deploy product instances of Cisco Unified Border Element and Unified
                           SRST (only for SIP) on the same Cisco 4000 Series Integrated Services Router. Co-location of Unified SRST and Unified Border
                           element is supported from the release Cisco IOS XE Fuji 16.7.1. All the Cisco SIP IP Phones are supported for this deployment.
                           The phone support includes, but is not limited to:

Cisco IP Phone 7800 Series

Cisco IP Phone 8800 Series

Cisco Unified IP Phone 9900 Series

When the Wide Area Network (WAN) is available, the router acts as a pure Cisco Unified Border Element, and not as a Unified
                           SRST.

During a WAN outage, the phones registered to the Unified Communications Manager fall back on the Unified SRST. However, phones
                           registered to Unified SRST can place or receive PSTN calls through SIP trunk.

The Unified SRST and the Unified Border Element feature set is limited to the features mentioned. The following features are
                           supported on the phone when registered to Unified SRST:

Incoming or Outgoing Basic Call

Hold/Resume

Call Forward

Call Transfer

Conference (Built-in Bridge)

Hunt Groups

MOH (for SIP lines in SRST mode)

The list of SIP trunk features supported for Unified SRST and Unified Border Element co-location are:

SIP-UA Registration/Authentication, Registrar, Register/Register Refresh

SIP-Server, Outbound Proxy

DNS Service Record

Bind Global / Dial-peer

SRTP / TLS, SRTP – RTP Interworking

Connection Reuse

IP Trust List

Voice class tenant

RTP-NTE DTMF

P-Called-Party ID, Privacy Header (PAI)

SIP Normalization

For more information on configuring tenants on SIP trunks, see Cisco Unified Border Element Configuration Guide . For more information on the recommended configurations for the Unified Border Element co-location, see Configuration Recommendations for Unified SRST and Unified Border Element Co-location .

The Figure shows a co-located deployment of Unified SRST with Cisco Unified Border Element.

### Configuration Recommendations for Unified SRST and Unified Border Element Co-location

The recommended configurations have considered single SIP trunk dial-peer, acting as both inbound and outbound dial-peer to
                                          handle calls to and from the Service Provider. Similarly, a single dial-peer, acting as both inbound and outbound dial-peer
                                          to handle calls to and from the Communication Manager.

The dial-peers created after the phones (registered to Unified Communications Manager) fall back on Unified SRST are dynamic
                              dial-peers. Hence, the configurations under voice service voip and sip-ua are inherited by these dynamic dial-peers. Move voice service voip and sip-ua configurations under voice class tenant configuration mode to avoid configuration conflict. The voice class tenant is included in the SIP trunk dial-peer configuration.

Similarly, the relevant global configurations are grouped under a voice class tenant and can be applied on the dial-peer toward Unified Communications Manager as well. These configurations grouped under the voice class tenant are used whenever the Unified Communications Manager is available (WAN is available). For sample configurations of the co-located
                              deployment of Unified SRST and Unified Border Element, see Examples .

The following are the configuration recommendations for the Unified SRST and Unified Border Element co-location:

Move SIP trunk specific voice service voip and sip-ua configurations under voice class tenant . This is to avoid configuration conflict between SIP trunk and line side dial-peer configurations. When tenant is configured
                                    under dial-peer, the configurations are applied in the following order of preference:

Dial-peer configuration

Tenant configuration

Global configuration

Certain CLI commands which need to be moved under tenant , are moved under dial-peer configuration mode. This is because these CLIs are not available under voice class tenant . For example, the CLI command srtp fallback needs to be configured under dial-peer , not voice class tenant configuration mode.

Use dial-peer groups feature to group multiple outbound dial-peers into a dial-peer group and configure this dial-peer group
                                    as the destination of an inbound dial-peer (Unified CM trunk). For more information on dial-peer groups, see Dial Peer Configuration Guide .

Configure SIP Options Request Keepalives to monitor reachability towards Unified Communications Manager. For example:

```
voice class sip-options-keepalive 101
 up-interval 30
 retry 3 transport tcp

Options keepalive under dialpeer

dial-peer voice 101 voip
 description **CUCM/PBX**
 voice-class sip options-keepalive profile 101
```

The relevant CLI commands for configuring dial-peer groups are:

voice class dpg dial-peer-group-id (Creates a dial-peer group).

destination dpg dial-peer-group-id (Specifies the dial-peer group from which the outbound dial-peer(s) is chosen).

Avoid configuring dial-peer groups on the Service Provider SIP trunk dial-peer.

Configure the destination pattern (.T) on the Unified Communications Manager dial-peer.

It is mandatory to configure voice class tenant on the Service Provider SIP trunk dial-peer router. A configuration with voice class tenant on the Unified Communications
                                    Manager dial-peer is also validated, though it is not mandatory.

Configure the CLI command destination dpg dial-peer-group-id (destination dpg 101) on the Unified Communications Manager dial-peer. This dpg configuration has Service Provider SIP trunk
                                    dial-peer information. You can configure preferences for the dial-peers within the dial-peer group:

```
voice class dpg 1
dial-peer 2900 preference 2
dial-peer 3900 preference 1
```

Do not configure incoming called-number (.T), on the Service Provider SIP trunk dial-peer. Match the incoming call from SIP trunk using the address information From
                                    URI.

```
voice class uri 201 sip
host dns:sip-trunk.sample

Under dial-peer:
incoming uri from 201
```

Configure the CLI command transport tcp tls v1.2 under sip-ua configuration mode, not voice class tenant .

Avoid modification of contact header in a Secure SIP to SIP (and vice versa) call flow, as it leads to call establishment
                                    issues. If sip-profiles are used to modify header information from sips: to sip: in SIP REQUESTS and RESPONSES, there must
                                    be rules to include ‘transport=tls’ in the contact header.

If dial-peers are using voice class codec , configure the same voice class codec under voice register pool too.

Ensure that an srtp voice-class is created using the voice class srtp-crypto crypto-tag command. A sample configuration is as follows:

```
voice class srtp-crypto 1
crypto 1 AES_CM_128_HMAC_SHA1_32
crypto 2 AES_CM_128_HMAC_SHA1_80
```

Configure the SIP Registrar under voice service voip sip configuration mode with maximum and minimum expiry time for an incoming registration using the CLI command registrar server [ expires [ max sec ] [ min sec ] ] .

registrar server expires max 120 min 60

Move all the CLI commands related to SIP Bind feature under voice class tenant configuration mode. For example, it is recommended to have the CLI commands voice-class sip bind control , and voice-class sip bind media , under voice class tenant configuration mode.

Exclude SIP ports from NAT services, if NAT is configured on the router. The recommended CLIs for excluding SIP ports from
                                    NAT services are:

no ip nat service sip udp port 5060

no ip nat service sip tcp port 5060

Configure the CLI commands no supplementary-service sip refer , no supplementary-service sip moved-temporarily , supplementary-service media-renegotiate under voice service voip configuration mode.

For the co-located deployment of Unified SRST and Unified Border Element, do not configure the CLI command no transport udp under sip-ua configuration mode. This is because, phones register to the Unified SRST device using UDP for signaling transport with the
                                    non-secure SIP SRST configuration.

Playback of MOH from the flash memory of the router is supported for SIP lines in SRST mode in a co-located deployment of
                                    Unified SRST and Cisco Unified Border Element. Cisco IOS XE Fuji 16.7.1 and later releases support this feature.

Redundancy is not supported for the co-located deployment of Unified SRST and Unified Border Element.

Virtual interfaces are not supported for the co-located deployment of Unified SRST and Unified Border Element.

Configure Media Inactivity Timer to enable router to monitor and disconnect calls if no Real-Time Protocol (RTP) packets are
                                    received within a configurable time period. A sample configuration is as follows:

```
ip rtcp report interval 9000
gateway
media-inactivity-criteria all
timer receive-rtp 1200
timer receive-rtcp 5
```

#### Restrictions

The following restrictions are observed for a co-located deployment of Unified SRST and Unified Border Element:

You need to disable the NAT firewall support for SIP trunk side, using the CLI commands no ip nat service sip udp port 5060 and no ip nat service sip tcp port 5060 .

All the SIP trunk features are not supported in a Unified SRST and Unified Border Element co-location deployment. For the
                                       list of supported features, see Unified SRST and Unified Border Element Co-location .

#### Examples

The following is a sample configuration for a voice class tenant:

```
voice class tenant 1
registrar ipv4:10.64.86.64:5061:5061 scheme sips expires 240 tcp tls auth-realm
sip-trunk.sample
credentials number +492281844672 username xxxx password xxxx realm sip-trunk.sample
authentication username xxxx password xxxx realm sip-trunk.sample
no remote-party-id
timers expires 900000
timers register 100
sip-server dns:sip-trunk.sample:5061
connection-reuse
asserted-id pai
bind control source-interface GigabitEthernet0/0/1
bind media source-interface GigabitEthernet0/0/1
conn-reuse
sip-profiles 3000
outbound-proxy dns:reg.sip-trunk.sample
privacy-policy passthru
call-route p-called-party-id
midcall-signaling preserve-codec
```

In the following configuration, the voice class tenant configured in the previous example is part of the dial-peer on the
                                    SIP trunk.

```
dial-peer voice 201 voip
description **SIP-TRUNK.SAMPLE**
session protocol sipv2
session target sip-server
session transport tcp tls
destination e164-pattern-map 201
incoming uri from 201
voice-class codec 1
voice-class sip url sips
voice-class sip asserted-id pai
voice-class sip outbound-proxy dns:reg.sip-trunk.sample
voice-class sip tenant 1
voice-class sip srtp-crypto 1
voice-class sip bind control source-interface GigabitEthernet0/0/1
voice-class sip bind media source-interface GigabitEthernet0/0/1
dtmf-relay rtp-nte
srtp
fax-relay ecm disable
fax rate 14400
ip qos dscp cs6 signaling
clid strip name
no vad
```

The following example provides the show running-config command output for the co-located deployment of Unified SRST and Unified
                                    Border Element:

```
Building configuration...
Current configuration : 15564 bytes
!
! Last configuration change at 17:52:50 IST Tue Jul 4 2017
! NVRAM config last updated at 17:52:54 IST Tue Jul 4 2017
!
version 16.7
service timestamps debug datetime msec
service timestamps log datetime msec
service sequence-numbers
platform qfp utilization monitor load 80
no platform punt-keepalive disable-kernel-core
platform shell
platform trace runtime slot F0 bay 0 process forwarding-manager module aom level debug
platform trace runtime slot F0 bay 0 process forwarding-manager module dsp level verbose
platform trace runtime slot F0 bay 0 process forwarding-manager module sbc level debug
platform trace runtime slot R0 bay 0 process forwarding-manager module dsp level verbose
platform trace runtime slot R0 bay 0 process forwarding-manager module om level debug
platform trace runtime slot R0 bay 0 process forwarding-manager module sbc level debug
!
hostname be4k-technium
!
boot-start-marker
boot-end-marker
!
!
vrf definition Mgmt-intf
!
address-family ipv4
exit-address-family
!
address-family ipv6
exit-address-family
!
! card type command needed for slot/bay 0/1
no logging queue-limit
logging buffered 100000000
no logging rate-limit
no logging console
!
no aaa new-model
process cpu statistics limit entry-percentage 10 size 7200
clock timezone IST 5 30
!
!
!
ip host gauss-lnx.cisco.com 10.64.86.64
ip name-server 8.41.20.1
ip dhcp excluded-address 8.39.23.13 8.39.23.50
!
ip dhcp pool phones
network 8.39.0.0 255.255.0.0
default-router 8.39.23.13
domain-name cisco.com
dns-server 8.39.23.13
!
!
!
!
!
!
!
!
!
!
subscriber templating
!
!
!
!
!
!
!
multilink bundle-name authenticated
!
!
!
!
!
!
trunk group 1
xsvc
!
!
crypto pki trustpoint sipgw1
enrollment url http://8.41.20.1:80
serial-number
ip-address 8.39.23.13
subject-name CN=sipgw1
revocation-check crl
rsakeypair cisco123
!
!
crypto pki certificate chain sipgw1
certificate 02
30820234 3082019D A0030201 02020102 300D0609 2A864886 F70D0101 05050030
13311130 0F060355 04031308 63617365 72766572 301E170D 31373036 32383134
32393330 5A170D31 38303632 38313432 3933305A 305C310F 300D0603 55040313
06736970 67773131 49301206 03550405 130B4644 4F323031 31413132 33301706
092A8648 86F70D01 0908130A 382E3339 2E32332E 3133301A 06092A86 4886F70D
01090216 0D626534 6B2D7465 63686E69 756D3081 9F300D06 092A8648 86F70D01
01010500 03818D00 30818902 818100B5 3CE45902 52517DBE E735F0B5 9D6A412F
FBF398A8 F306F28F A4C79A41 198A19D7 06025696 F5EC6237 EFCB1BBD C7430263
1D0D3C7E AF06B4B2 0D30547C F049A3CD CC4FCFA1 335DA8C5 602A2D18 F91ECC32
E0A7E279 60945941 DF5B53F9 102B9067 8782C1E0 874D6CBC DB0CDA82 C64B7423
E56C5C33 2E13C729 9AB7FEEA 068E7102 03010001 A34F304D 300B0603 551D0F04
04030205 A0301F06 03551D23 04183016 8014265B 6595680C E517CC42 F54AE9EC
1F328FBE BF33301D 0603551D 0E041604 14BA096E DE4E2289 12E8F4D8 95E06E4A
F93876E7 96300D06 092A8648 86F70D01 01050500 03818100 9B172FF6 291C193A
E505ABE9 45AC3202 621BBE2B 6BA45F19 AE0DA7A0 EF5FBC19 5197094E 7A50BCF3
CC49656E A0D991AC FED14749 EAB50892 0239E39C 345ED555 7CD74760 66B0DF49
7E26B654 B8F9E1B1 72FD4039 8A13C9AC EBE75F21 B457D8E3 24BA70E3 F1B3A0C9
5C3153FA B3C744B7 D81F706F B836617F 9E95AD51 813F20AD
quit
certificate ca 01
308201FF 30820168 A0030201 02020101 300D0609 2A864886 F70D0101 04050030
13311130 0F060355 04031308 63617365 72766572 301E170D 31373036 32383134
32383131 5A170D32 30303632 37313432 3831315A 30133111 300F0603 55040313
08636173 65727665 7230819F 300D0609 2A864886 F70D0101 01050003 818D0030
81890281 8100A3AC A4003239 62667AB4 6E8ACE2B 90672DD8 1E2A2952 AFC8A1F6
D56173C9 269F9176 747E93D1 6F699B6F 0C2E600D 8C864F27 4379ED8A E88187F7
17A77C63 B87B7EF6 1556D949 43C743F6 01D9941D 946FCEC8 880B342C 97CC9CEA
9F015EAC A667F30B 505281AA 29EB10A3 F1C75A99 2A224653 F3B985DD F17BC8DD
40C8C609 62C90203 010001A3 63306130 0F060355 1D130101 FF040530 030101FF
300E0603 551D0F01 01FF0404 03020186 301F0603 551D2304 18301680 14265B65
95680CE5 17CC42F5 4AE9EC1F 328FBEBF 33301D06 03551D0E 04160414 265B6595
680CE517 CC42F54A E9EC1F32 8FBEBF33 300D0609 2A864886 F70D0101 04050003
81810077 C36A6C9A B7C18856 EBDA4504 C38565F0 CF6385EE 29AFC38B 8B90C741
B20C8C36 E979FD72 7B849B34 0BBE3EFA 191E1776 C28FDCF8 5D5F7CFF 170CF615
B4105ABD CD6E0318 4B576FFD 44D115FF 2817E279 78B2794E 577F694F DD129820
B500BB08 E57BFAA9 87835645 4EA53352 B80B51AD 2CC0633A AB9974EB E523A944 0EC230
quit
!
!
!
!
voice service voip
ip address trusted list
ipv4 8.55.0.0 255.255.0.0
ipv4 10.64.0.0 255.255.0.0
address-hiding
mode border-element license capacity 50
media statistics
media bulk-stats
media disable-detailed-stats
allow-connections sip to sip
no supplementary-service sip moved-temporarily
no supplementary-service sip refer
supplementary-service media-renegotiate
fax protocol t38 version 0 ls-redundancy 0 hs-redundancy 0 fallback none
sip
registrar server expires max 240 min 60
!
!
voice class uri 101 sip
host ipv4:10.64.86.136
!
voice class uri 201 sip
host dns:sip-trunk.sample
!
voice class uri 301 sip
host ipv4:10.64.86.138
voice class codec 1
codec preference 1 g711alaw
codec preference 2 g722-64
codec preference 3 g711ulaw
!
!
voice class sip-profiles 3000
rule 1 request REGISTER sip-header SIP-Req-URI modify "sips:(.*)" "sip:\1"
rule 2 request REGISTER sip-header To modify "<sips:(.*)" "<sip:\1"
rule 3 request REGISTER sip-header From modify "<sips:(.*)" "<sip:\1"
rule 4 request REGISTER sip-header Contact modify "<.*:.*@(.*)>"
"<sip:\1;transport=tls;bnc>"
rule 6 request REGISTER sip-header Proxy-Require add "Proxy-Require: gin"
rule 7 request REGISTER sip-header Require add "Require: gin"
!
voice class sip-profiles 201
rule 1 request ANY sip-header P-Asserted-Identity modify "<sips:(.*)>"
"<sip:+4922842293220@sip-trunk.sample>"
rule 2 request ANY sip-header SIP-Req-URI modify "sips:(.*)" "sip:\1"
rule 3 request ANY sip-header To modify "<sips:(.*)" "<sip:\1"
rule 4 request ANY sip-header From modify "<sips:(.*)" "<sip:\1"
rule 5 request ANY sip-header Contact modify "<sips:(.*)>" "<sip:\1;transport=tls>"
rule 6 response ANY sip-header To modify "<sips:(.*)" "<sip:\1"
rule 7 response ANY sip-header From modify "<sips:(.*)" "<sip:\1"
rule 8 response ANY sip-header Contact modify "<sips:(.*)>" "<sip:\1;transport=tls>"
rule 9 request ANY sip-header Min-SE remove
rule 10 request ANY sip-header Diversion remove
rule 11 request ANY sdp-header Connection-Info remove
rule 12 response ANY sdp-header Connection-Info remove
rule 13 request INVITE sip-header Allow-Header modify "INFO," ""
!
voice class sip-profiles 101
rule 1 request INVITE sip-header Supported modify "100rel," ""
!
voice class sip-profiles 102
rule 1 request INVITE sip-header Privacy add "Privacy:id"
rule 2 request INVITE sip-header P-Called-Party-ID add "P-Called-Party-ID:
sip:2001@10.64.86.64"
!
!
voice class sip-copylist 201
sip-header FROM
!
voice class e164-pattern-map 101
e164 +492284229322T
!
!
voice class e164-pattern-map 201
e164 11[02]
e164 11[68]T
e164 11[025]
e164 +T
e164 0T
e164 2...
!
!
voice class e164-pattern-map 301
e164 3...
!
!
voice class dpg 201
!
voice class dpg 101
dial-peer 201
!
voice class dpg 301
dial-peer 301
!
voice class server-group 1
ipv4 10.64.86.136
description **CUCM Server Group**
!
voice class sip-options-keepalive 101
up-interval 30
retry 3
transport tcp
sip-profiles 3000
!
voice class tenant 1
registrar dns:sip-trunk.sample:5061 scheme sips expires 240 tcp tls auth-realm
sip-trunk.sample
credentials number +492281844672 username xxxx password 7 060506324F41 realm
sip-trunk.sample
authentication username xxxx password 7 121A0C041104 realm sip-trunk.sample
no remote-party-id
timers expires 60000
timers register 100
timers buffer-invite 1000
timers dns registrar-cache ttl
sip-server dns:sip-trunk.sample:5061
connection-reuse
asserted-id pai
bind control source-interface GigabitEthernet0/0/1
bind media source-interface GigabitEthernet0/0/1
no pass-thru content custom-sdp
conn-reuse
sip-profiles 3000
outbound-proxy dns:reg.sip-trunk.sample
privacy-policy passthru
call-route p-called-party-id
midcall-signaling preserve-codec
!
voice class tenant 2
registrar dns:sip-trunk.sample:5060 expires 240 tcp auth-realm sip-trunk.sample
credentials number +492281844673 username xxxx password 7 030752180500 realm
sip-trunk.sample
authentication username xxxx password 7 121A0C041104 realm sip-trunk.sample
no remote-party-id
timers expires 900000
timers register 100
timers buffer-invite 10000
timers dns registrar-cache ttl
sip-server dns:sip-trunk.sample:5060
connection-reuse
asserted-id pai
bind control source-interface GigabitEthernet0/0/1
bind media source-interface GigabitEthernet0/0/1
no pass-thru content custom-sdp
conn-reuse
sip-profiles 3000
outbound-proxy dns:reg.sip-trunk.sample
privacy-policy passthru
call-route p-called-party-id
midcall-signaling preserve-codec
!
voice class tenant 3
registrar dns:sipp.sample:6600 expires 240 auth-realm sip-trunk.sample
credentials number +492281844672 username xxxx password 7 121A0C041104 realm
sip-trunk.sample
authentication username xxxx password 7 05080F1C2243 realm sip-trunk.sample
no remote-party-id
timers expires 900000
timers register 500
timers buffer-invite 1000
timers dns registrar-cache ttl
sip-server dns:sipp.sample
connection-reuse
asserted-id pai
bind control source-interface GigabitEthernet0/0/1
bind media source-interface GigabitEthernet0/0/1
no pass-thru content custom-sdp
conn-reuse
sip-profiles 3000
outbound-proxy dns:sipp.sample:6600
privacy-policy passthru
call-route p-called-party-id
midcall-signaling preserve-codec
!
voice class tenant 4
timers expires 60000
timers buffer-invite 10000
connection-reuse
asserted-id pai
bind control source-interface GigabitEthernet0/0/0
bind media source-interface GigabitEthernet0/0/0
no pass-thru content custom-sdp
privacy-policy passthru
call-route p-called-party-id
midcall-signaling preserve-codec
!
voice class srtp-crypto 1
crypto 1 AES_CM_128_HMAC_SHA1_32
crypto 2 AES_CM_128_HMAC_SHA1_80
!
!
!
voice register global
default mode
no allow-hash-in-dn
max-dn 40
max-pool 40
!
voice register pool 1
id network 8.55.0.0 mask 255.255.0.0
dtmf-relay rtp-nte
voice-class codec 1
!
voice hunt-group 1 parallel
list 1001,1002,1003
timeout 15
statistics collect
pilot 1234
!
!
voice hunt-group 2 sequential
list 1002,1003,1004
timeout 5
statistics collect
pilot 2345
!
!
!
!
!
!
voice-card 0/1
dsp services dspfarm
no watchdog
!
license udi pid ISR4321/K9 sn FDO201115PV
license boot level uck9
license boot level securityk9
no license smart enable
diagnostic bootup level minimal
!
spanning-tree extend system-id
!
!
!
username xxxx privilege 15 password 0 cisco
username xxxx password 0 cisco
!
redundancy
mode none
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
template 1
!
!
!
!
!
interface GigabitEthernet0/0/0
ip address 8.39.23.13 255.255.0.0
ip nat inside
media-type rj45
negotiation auto
!
interface GigabitEthernet0/0/1
ip address 10.64.86.64 255.255.0.0
ip nat outside
negotiation auto
!
interface Service-Engine0/1/0
!
interface GigabitEthernet0
vrf forwarding Mgmt-intf
no ip address
negotiation auto
!
no ip nat service sip tcp port 5060
no ip nat service sip udp port 5060
ip nat pool pool1 8.39.0.0 8.39.255.255 netmask 255.255.0.0
ip nat inside source list 100 interface GigabitEthernet0/0/1 overload
ip forward-protocol nd
ip http server
no ip http secure-server
ip tftp source-interface GigabitEthernet0/0/0
ip tftp blocksize 1520
ip rtcp report interval 9000
ip route 0.0.0.0 0.0.0.0 8.39.0.1
ip route 10.0.0.0 255.0.0.0 10.64.86.1
!
ip ssh server algorithm encryption aes128-ctr aes192-ctr aes256-ctr
ip ssh client algorithm encryption aes128-ctr aes192-ctr aes256-ctr
!
!
ip access-list extended nat-list
access-list 100 permit ip 8.39.23.0 0.0.0.255 any
!
!
tftp-server flash:fbi88xx.BE-01-010.sbn
tftp-server flash:kern88xx.12-0-1MN-113.sbn
tftp-server flash:rootfs88xx.12-0-1MN-113.sbn
tftp-server flash:sb288xx.BE-01-020.sbn
tftp-server flash:sip88xx.12-0-1MN-113.loads
tftp-server flash:vc488xx.12-0-1MN-113.sbn
!
!
ipv6 access-list preauth_v6
permit udp any any eq domain
permit tcp any any eq domain
permit icmp any any nd-ns
permit icmp any any nd-na
permit icmp any any router-solicitation
permit icmp any any router-advertisement
permit icmp any any redirect
permit udp any eq 547 any eq 546
permit udp any eq 546 any eq 547
deny ipv6 any any
!
control-plane
!
!
voip trunk group 1
xsvc
!
uc wsapi
message-exchange max-failures 99
response-timeout 2
source-address 8.39.23.13
probing interval keepalive 60
probing max-failures 2
provider xcc
remote-url http://8.39.23.13:8090/xcc
!
!
provider xsvc
!
!
!
mgcp behavior rsip-range tgcp-only
mgcp behavior comedia-role none
mgcp behavior comedia-check-media-src disable
mgcp behavior comedia-sdp-force disable
!
mgcp profile default
!
!
!
!
dial-peer voice 201 voip
description **SIP-TRUNK.SAMPLE**
session protocol sipv2
session target sip-server
session transport tcp tls
destination e164-pattern-map 201
incoming uri from 201
voice-class codec 1
voice-class sip url sips
voice-class sip profiles 201
voice-class sip tenant 1
voice-class sip srtp-crypto 1
dtmf-relay rtp-nte
srtp
fax-relay ecm disable
fax rate 14400
clid strip name
no vad
!
dial-peer voice 301 voip
description **SIP-TRUNK.SAMPLE**
session protocol sipv2
session target sip-server
session transport tcp
destination e164-pattern-map 301
incoming uri from 201
voice-class codec 1
voice-class sip url sip
voice-class sip profiles 201
voice-class sip tenant 2
dtmf-relay rtp-nte
srtp fallback
fax-relay ecm disable
fax rate 14400
clid strip name
no vad
!
dial-peer voice 401 voip
description **SIP-TRUNK.SAMPLE**
destination-pattern 4...
session protocol sipv2
session target sip-server
session transport udp
incoming uri from 301
voice-class codec 1
voice-class sip url sip
voice-class sip profiles 201
voice-class sip tenant 3
dtmf-relay rtp-nte
fax-relay ecm disable
fax rate 14400
clid strip name
no vad
!
dial-peer voice 101 voip
description **CUCM/PBX**
destination-pattern .T
session protocol sipv2
session transport tcp
session server-group 1
destination dpg 101
incoming uri via 101
voice-class codec 1
no voice-class sip outbound-proxy
voice-class sip srtp negotiate cisco
voice-class sip profiles 102 inbound
voice-class sip tenant 4
voice-class sip srtp-crypto 1
voice-class sip options-keepalive profile 101
dtmf-relay rtp-nte
srtp fallback
fax-relay ecm disable
fax rate 14400
fax protocol t38 version 0 ls-redundancy 0 hs-redundancy 0 fallback pass-through g711alaw
no vad
!
!
presence
!
gateway
media-inactivity-criteria all
timer receive-rtcp 5
timer receive-rtp 180
!
sip-ua
transport tcp tls v1.2
crypto signaling default trustpoint sipgw1
!
alias exec cl clear logg
alias exec rtp show voip rtp connections
alias exec pool show voice register pool all brief
!
line con 0
exec-timeout 0 0
password cisco
width 0
transport input none
stopbits 1
line aux 0
stopbits 1
line vty 0 4
exec-timeout 0 0
password cisco
login local
length 0
transport input all
!
!
!
!
!
!
end
```

## Feature Information for Configuring SIP Trunking on Cisco Unified SRST

Not all commands may be available in your Cisco IOS Software release. For release information about specific command, see
                           the command reference documentation.

Use Cisco Feature Navigator to find information about the platform support and software image support. Cisco Feature Navigator
                           enables you to determine which Cisco IOS and Cisco Catalyst operating system software images support a specific software release,
                           feature set, or platform. To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn . You do not need an account on Cisco.com.

The table lists only the Cisco IOS Software release that introduced support for a given feature in a given Cisco IOS Software
                                       release train. Unless noted otherwise, subsequent releases of that Cisco IOS Software release train also support that feature.

The following table lists the release history for this feature.

Feature Name

Releases

Feature Information

Cisco Unified SRST and Cisco Unified Border Element Co-location

Cisco IOS XE Fuji 16.7.1

Added Support for co-location of Cisco Unified SRST and Cisco Unified Border Element on Cisco 4000 Series Integrated Services
                                       Router.

| Note | The recommended configurations have considered single SIP trunk dial-peer, acting as both inbound and outbound dial-peer to
                                          handle calls to and from the Service Provider. Similarly, a single dial-peer, acting as both inbound and outbound dial-peer
                                          to handle calls to and from the Communication Manager. |
|---|---|

| Note | Certain CLI commands which need to be moved under tenant , are moved under dial-peer configuration mode. This is because these CLIs are not available under voice class tenant . For example, the CLI command srtp fallback needs to be configured under dial-peer , not voice class tenant configuration mode. |
|---|---|

| Note | The table lists only the Cisco IOS Software release that introduced support for a given feature in a given Cisco IOS Software
                                       release train. Unless noted otherwise, subsequent releases of that Cisco IOS Software release train also support that feature. |
|---|---|

| Feature Name | Releases | Feature Information |
|---|---|---|
| Cisco Unified SRST and Cisco Unified Border Element Co-location | Cisco IOS XE Fuji 16.7.1 | Added Support for co-location of Cisco Unified SRST and Cisco Unified Border Element on Cisco 4000 Series Integrated Services
                                       Router. |