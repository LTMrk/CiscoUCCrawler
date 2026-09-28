---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-ipv6-vtgs-b-ipv6-deployment-guide-for-cisco-vtgs-b-ipv6-deployment-2595ef4250
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/IPv6/vtgs_b_ipv6-deployment-guide-for-cisco/vtgs_b_ipv6-deployment-guide-for-cisco_chapter_01110.html
retrieved_at: 2026-08-16T18:22:48.068266+00:00
---

IPv6 Deployment Guide

# IPv6 Deployment Guide

Updated: October 18, 2024

Chapter: Collaboration Endpoints

## Chapter: Collaboration Endpoints

# Collaboration Endpoints

## IPv6 Capabilities of Collaboration Endpoints

This chapter describes a subset of the Cisco Collaboration endpoints and their IPv6 capabilities. The following table lists
                           the endpoint types and summarizes their IPv6 capabilities. IPv6 support extends to only a subset of the Cisco analog gateways
                           and IP phones. The following sections discuss these devices in more detail.

Endpoint Type

IPv6 Capability

Analog gateways

Does not support Cisco VG Series Gateways for IPv6-only.

Cisco IP Phones

Cisco Unified IP Phones 78xx and 88xx Series support IPv6-only.

Software-based endpoints

Jabber software-based endpoints support IPv6.

Wireless endpoints

No wireless endpoints support IPv6.

Cisco Unified IP Conference Station

Conference stations support IPv6.

Cisco TelePresence video endpoints (CE software)

-

Third-party SIP IP phones

Third-party IPv6-capable phones are not supported.

## IPv6 Support on Cisco IP Phones

For a list of endpoints that support IPv6-only, see Supported IPv6 Addressing Modes . Any endpoints not listed there should be configured in IPv4-only stack.

When a phone with a single IPv4 address needs to communicate with a phone with a single IPv6 address, an IP addressing version
                              incompatibility exists. To resolve this media addressing incompatibility, Unified CM dynamically inserts a media termination
                              point (MTP) to convert the media stream from IPv4 to IPv6 (and conversely).

### IP Phone Deployment Considerations in an IPv6 Network

The PC Voice LAN Access setting on IP phones is typically used to allow the monitoring of IP phone traffic by monitoring and recording applications
                              and by network monitoring software. This setting also allows multicast traffic to be propagated from the voice VLAN to the
                              IP phone's PC port. By default, the PC Voice VLAN Access setting is enabled on IP phones.

In IPv6-enabled networks, this default PC Voice VLAN Access setting allows Router Advertisement (RA) multicast messages to
                              be sent from the voice VLAN to the IP phone's PC port. Ordinarily, the PC should drop any packets that it receives with a
                              voice VLAN tag because it is not configured for the voice VLAN and does not understand 802.1g tagging. However, if the PC
                              does accept packets with a voice VLAN tag and uses an RA from the voice VLAN, it can cause an IPv6 address from the voice
                              VLAN to be assigned to the PC.

If you encounter the issue of incorrect IPv6 address assignment for PC port devices, use either of the following techniques
                              to resolve this issue:

Set the prefix lifetime of RAs sent by routers in the voice VLAN to a shorter lifetime value than the RAs sent by routers
                                    in the data VLAN, and also ensure that routers in the data VLAN have higher priority than those in the voice VLAN. IPv6 devices
                                    in the data VLAN using the Address Selection Algorithm (RFC 3484) choose the Network Prefix included in RAs with the longest
                                    lifetime, and thus prefer routers in the data VLAN.

For all IP phones with connected devices that are affected by the above issue, set the IP phone's PC Voice VLAN Access setting
                                    to disabled. For large numbers of phones, this configuration change can be bulk-provisioned through the Unified CM Bulk Administration
                                    Tool (BAT).

### Common Device Configuration Profile

The process for configuring IPv6 on the phones is similar to that for SIP trunks. In Cisco Unified CM Administration, select Device > Device Settings > Common Device Configuration > to create and configure a Common Device Configuration Profile and associated it with one or more IP phones. The Common Device
                                 Configuration Profile contains the following IPv6 configuration information:

IP Addressing Mode

IP Addressing Mode Preference for Signaling

Allow Auto-Configuration for Phones

#### IP Addressing Mode

The phone IP Addressing Mode has three settings:

IPv4 Only

In this mode, the phone acquires and uses only one IPv4 address for all signaling and media. If the phone has previously acquired
                                       an IPv6 address, it releases that address.

IPv6 Only

In this mode, the phone acquires and uses only one IPv6 address for all signaling and media. If the phone has previously acquired
                                       an IPv4 address, it releases that address.

IPv4 and IPv6

In this mode, the phone acquires and uses one IPv4 address and one IPv6 address. It can use the IPv4 and the IPv6 address
                                       as required for media. It uses either the IPv4 address or the IPv6 address for call control signaling to Unified CM.

If IPv6 is enabled in the Unified CM cluster, the default phone setting for IP Addressing Mode is IPv4 and IPv6. If the IP
                                 phone supports both IPv4 and IPv6 , it will adopt this setting, but all IPv4-only phones will ignore this setting.

We recommend setting the phone IP Addressing Mode to IPv4 and IPv6 .

#### IP Addressing Mode Preference for Signaling

The phone IP Addressing Mode Preference for Signaling has three settings:

IPv4

If the phone has an IPv4 address, it uses that IPv4 address for call control signaling to Unified CM.

IPv6

If the phone has an IPv6 address, it uses that IPv6 address for call control signaling to Unified CM.

Use System Default

In this case, the phone uses the cluster-wide Enterprise Parameter configuration value for its IP Addressing Mode for Signaling.

If IPv6 is enabled in the Unified CM cluster, the default phone setting for IP Addressing Mode for Signaling is Use System Default . If the IP phone supports either IPv6 or both IPv4 and IPv6, it will adopt the cluster-wide setting for IP Addressing Mode
                                 for Signaling, but all IPv4-only phones will ignore this setting.

#### Allow Auto-Configuration for Phones

Allow Auto-Configuration for Phones has three settings:

On

With this setting, the phone is allowed to use Stateless Auto Address Configuration (SLAAC) to acquire an IPv6 address. Whether
                                       or not the phone uses SLAAC depends on the link-local router's O and M bit configuration for router advertisements (RAs),
                                       as follows:

If the O bit is set in the router's RAs, the phone uses SLAAC to acquire an IPv6 address and uses the DHCP server to acquire
                                             other information such as the TFTP server address.

If the M bit is set in the router's RAs, the phone does not use SLAAC. Instead, it uses the DHCP server to acquire its IP
                                             address and other information.

If neither the M bit nor the O bit is set, the phone uses SLAAC to acquire an IP address and does not use DHCP for other information.
                                             The phone also requires a TFTP server address to download its configuration file and register to Unified CM. This TFTP server
                                             address can be configured manually through the phone’s user interface (UI).

Off

With this setting, the phone does not use Stateless Auto Address Configuration (SLAAC) to acquire an IPv6 address. In this
                                       case, the phone can be configured manually to acquire an IPv6 address and TFTP server address.

Default

With this setting, the phone uses the cluster-wide Enterprise Parameter configuration value for Allow Auto-Configuration for
                                       Phones.

### Default Common Device Configuration Profile

By default, there are no Common Device Configuration profiles configured, and each device is associated with a <None> Common
                                 Device Configuration. If IPv6 is enabled in the Unified CM cluster with this default configuration, IPv6-capable devices adopt
                                 the following settings:

IP Addressing Mode = IPv4 or IPv6

IP Addressing Mode Preference for Signaling = Use System Default

Allow Auto-Configuration for Phones = Default

### Other IP Phone Functions

The following functions also affect the use of IPv6 on Cisco IP Phones.

#### TFTP

As previously described, TFTP servers support both IPv4 and IPv6 addresses. IPv4-only phones use their received IPv4 TFTP
                                 address to reach the TFTP server, and IPv6-only phones use their received IPv6 TFTP address to reach the TFTP server. Dual-stack
                                 phones can use either their IPv4 or IPv6 TFTP address to reach the TFTP server.

The following IPv6 information is sent to the phone in its configuration file from the TFTP server:

Unified CM IPv4 and IPv6 addresses

The setting for IP Addressing Mode

The setting for IP Addressing Mode Preference for Signaling

The setting for Allow Stateless Auto-Configuration for Phones

#### Unified CM Registration for Dual-Stack IP Phones

Dual-stack phones attempt to connect to Unified CM by using the preferred (IPv4 or IPv6) address specified in the IP Addressing
                                 Mode Preference for Signaling parameter found in the TFTP configuration file. If the first attempt at connection fails due
                                 to a TCP timeout, the phone then attempts to connect to Unified CM using its other address.

#### IP Phone HTTP Server Functionality

The HTTP server function of all IP phones uses IPv4-only or IPv6-only. The HTTP server provides several functions, including:

Phone User Interface access to:

Directory search functions

Call history

All IP Phone Services

Extension Mobility

IPv4-only supported Quality Report Tool (QRT)

Web access to the phone through the Unified CM phone administration graphical user interface

#### CDP and LLDP

IP phones support the sending and receiving of IPv4 and IPv6 addresses in data link layer Cisco Discovery Protocol (CDP) and
                                 Link Layer Discovery Protocol (LLDP) messages. Currently, Cisco applications do not use any of the IPv6 addresses sent in
                                 LLDP messages. CDP is applicable to Emergency Responder and discovery of a desk phone device.

### IPv6-Only Supported and Not Supported Features

#### IPv6-Only Supported Features

The following are the  IPv6-Only supported features:

Mobility - MVA/IVR

CAPFv3

TVS and TFTP

Extension Mobility

SRST

SIP GW

SIP Route Pattern

Barge

Intercom

Phone NTP Reference

Device Mobility

Self Care Portal

Self Provisioning using with and without IVR

Phone services - Corporate Directory

Missed Calls

Placed Calls

Intercom Calls

Personal Directory

Voicemail

Received Calls

Web Dialer

Quality Report Tool (QRT)

SNMPv6 MIB

Phone Config download

CTI

IPVMS (Unicast MoH, Software MTP, ANN, Conference Bridge, IVR)

CDR

#### IPv6-Only Not Supported Features

The following are the  IPv6-Only not supported features:

IPv6-Only device profile login for EMCC

Best Effort Early Offer over SIP Trunk

External MoH, Multicast MoH , Video On Hold, Voicemail, Recording (BIB Recording, GW Recording), Enhanced E911

SSH, Cluster Manager, LDAP, Syslog Server/Alarm Library, Serviceability Applications - IPMA, RTMT

DRS, IPSec

Media Resources (IOS Xcoder/ hardware MTP/TRP)/Conference Bridge), Video conference resource (MCU/Conductor), FAX/ATA

MRA (Jabber in IPv6 and Exp-E external interface in v6 and enterprise network in v4 is supported)

Silent Monitoring, Whisper Coaching, Agent Greeting, VG as analog line interface using SCCP (pending test)

| Endpoint Type | IPv6 Capability |
|---|---|
| Analog gateways | Does not support Cisco VG Series Gateways for IPv6-only. |
| Cisco IP Phones | Cisco Unified IP Phones 78xx and 88xx Series support IPv6-only. |
| Software-based endpoints | Jabber software-based endpoints support IPv6. |
| Wireless endpoints | No wireless endpoints support IPv6. |
| Cisco Unified IP Conference Station | Conference stations support IPv6. |
| Cisco TelePresence video endpoints (CE software) | - |
| Third-party SIP IP phones | Third-party IPv6-capable phones are not supported. |