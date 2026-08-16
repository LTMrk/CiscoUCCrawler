---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-ipv6-vtgs-b-ipv6-deployment-guide-for-cisco-vtgs-b-ipv6-deployment-7146cf069a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/IPv6/vtgs_b_ipv6-deployment-guide-for-cisco/vtgs_b_ipv6-deployment-guide-for-cisco_chapter_010.html
retrieved_at: 2026-08-16T18:21:58.489310+00:00
---

IPv6 Deployment Guide

# IPv6 Deployment Guide

Updated: October 18, 2024

Chapter: IP Addressing Modes for Cisco Collaboration Products

## Chapter: IP Addressing Modes for Cisco Collaboration Products

# IP Addressing Modes for Cisco Collaboration Products

## IP Addressing Modes

IP addressing modes specify the types of addresses that a device can communicate with and understand. The following IP addressing
                           modes are used as part of the Cisco Collaboration Systems Release.

IP Addressing Mode

Description

Notes

IPv4-only stack

Used for some endpoints and gateways.

IPv6-only stack

Used for some endpoints and gateways.

Dual-stacks: IPv4-only and IPv6-only

Used for applications servers, such as Cisco Unified Communications Manager, Cisco Unity Connection, Cisco Emergency Responder,
                                       and Cisco Unified Survivable Remote Site Telephony (Unified SRST).

The session initiation protocol (SIP) session description protocol (SDP) attribute should not be configured to transition
                                       to IPv6-only.

IPv6 Aware

Used for applications servers that use IPv4 to transport IPv6 application information, such as the Cisco Prime Collaboration
                                       Provisioning module, Cisco Emergency Responder, and Unified CM.

IPv6 aware devices communicate with IPv4 addresses, but can receive and understand IPv6 addresses embedded in application
                                       protocol data units (PDUs).

Dual-stack

Used for applications servers, such as Cisco Unified Communications Manager, Cisco Unity Connection, Cisco Emergency Responder,
                                       and Cisco Unified Survivable Remote Site Telephony (Unified SRST).

-

## Supported IPv6 Addressing Modes

For Collaboration IPv6 implementations, we recommend that you configure:

IPv6-only stack for endpoints and gateways where supported.

IPv4-only and IPv6-only stack for application servers and interfaces where supported. Unified CM and other applications ensure
                                    interoperability with existing IPv4-only devices and applications.

The following tables illustrate the SIP IP addressing modes for Cisco Collaboration Systems Release (CSR)  products. Any products
                              not listed here should be configured in IPv4-only stack.

For a list of product configuration resources for IPv6, see Product Configuration Resources for IPv6 .

Endpoint (SIP)

IPv4-only

IPv6-only

Dual- Stacks: IPv4 and IPv6

Comments

Cisco IP Phone 7811, 7821, 7841, 7861

Yes

Yes

Yes

Cisco IP Phone 8811, 8841, 8845, 8851, 8861, 8865, 8875

Yes

Yes

Yes

Cisco IP Conference Phone 7832

Yes

Yes

Yes

Cisco IP Conference Phone 8832

Yes

Yes

Yes

Catalyst 8000 Series Edge Platforms

Yes

No

Yes

Cisco Jabber

Yes

Yes

Yes

IPv6-only is for on-premise Jabber desktop deployment. No ANAT.

Cisco Webex Room Series, Board Series, Desk Series

Yes

Yes

Yes

Gateway

Applications

IPv4-only

IPv6-only

Dual- Stacks: IPv4 and IPv6

Comments

The "Yes" and "No" means whether the IP Addressing mode is supported or not.

Cisco 4000 Series Integrated Services Routers (ISR)

IOS Gateways

Yes

No

Yes

For more information, see Cisco IOS Unified Communications Gateways with SIP

Unified SRST

Yes

No

Yes

CUBE

Yes

No

Yes

Only ISR G2.

MTP

Yes

No

Yes

Cisco 2900 and 3900 Series Integrated Services Routers (ISR)

IOS Gateways

Yes

No

No

EOS Notices for ISR 28xx / 38xx / 29xx / 39xx

Unified SRST

Yes

No

No

CUBE

Yes

No

Yes

MTP

Yes

No

Yes

H.323 Gateways

Yes

No

No

EOS Notice for the H.323  Call Control features in Cisco IOS-XE Software

EOS Notices for ISR 28xx / 38xx / 29xx / 39xx

Media Gateway Control Protocol (MGCP) Gateways

Yes

No

No

EOS Notices for ISR 28xx / 38xx / 29xx / 39xx

Application or Interface

IPv4-only

IPv6-only

Dual- Stacks: IPv4 and IPv6

Comments

Cisco Unified Communications Manager (Unified CM)

Yes

No

Yes

Product required for IPv6 deployment.

Cisco Unified Communications Manager IM and Presence Service (IM and Presence Service)

Yes

No

Yes

Product required for IPv6 deployment.

Cisco Unified Communications Manager Express (Unified CME)

Yes

No

No

Cisco Unified Survivable Remote Site Telephony (Unified SRST)

Yes

No

Yes

Product required for IPv6 deployment for ISR G3.

Yes

No

Yes

For Agent IPv6-only stack, NAT64.

Cisco Unified Contact Center Express (Unified CCX)

Yes

No

Yes

For Agent IPv6-only stack, NAT64.

Cisco Emergency Responder (Emergency Responder)

Yes

No

Yes

Cisco Unity Connection

Yes

No

Yes

Cisco Meeting Server

Yes

No

No

Cisco TelePresence Management Suite

Yes

No

No

Cisco Unity Express

Yes

No

No

End-of-Sale: Cisco Unified MeetingPlace

Yes

No

No

EOS Notice

Cisco Prime Collaboration

Yes

No

Yes

Applicable to IOS Gateways, Unified SRST, CUBE.

Cisco Smart Software Licensing

Yes

No

Yes

Applicable to Unified CM, IM and Presence Service, Cisco Unity Connection.

LAN/WAN

Yes

Yes

Yes

Dynamic Host Configuration Protocol (DHCP)

Yes

Yes

Yes

Domain Name System (DNS)

Yes

Yes

Yes

Directory LDAP

Yes

Yes

Yes

NAT64

Yes

No

No

Except for Unified CCE and Unified CCX, which have internal NAT64.

## IPv6 Addressing in Cisco Collaboration Products

As you design your network, you'll need information about the number of IPv6 addresses that the various products can support.

### Cisco Unified Communications Manager and IPv6 Addresses

Each Cisco Media Convergence Server (MCS) can support the following addresses simultaneously:

One IPv6 link local address (for example, FE80::987:65FF:FE01:2345)

Either of the following:

One IPv6 unique local address (ULA), for example:

```
FD00:AAAA:BBBB:CCCC:0987:65FF:FE01:2345
```

One IPv6 global address (GA), for example:

```
2001:0DB8:BBBB:CCCC:0987:65FF:FE01:2345
```

One IPv4 address

All IPv6 devices must have a link local address that is automatically created.

A unique local address is equivalent to a private address in IPv4 (for example, 10.10.10.1).

A global address is a globally unique public address.

### Cisco IP Phones and IPv6 Addresses

A Cisco IP Phone can support a combination of the following addresses:

One IPv6 link local address (for example, FE80::987:65FF:FE01:2345)

Multiple IPv6 unique local addresses (for example, FD00:AAAA:BBBB:CCCC:0987:65FF:FE01:2345)

Multiple IPv6 global addresses (for example, 2001:0DB8:BBBB:CCCC:0987:65FF:FE01:2345)

One IPv4 address

IPv6 NAT-based solution is not supported.

Cisco IP Phones must support one link local address and can support a combination of up to 20 global or unique local addresses.
                                 The IP phone can use only IPv6 highest address scopes that can be received (RFC 4193) (global address or unique local IPv6
                                 addresses) to register to Unified CM. After registration, this IPv6 address is used for signaling and media.

The following characteristics also apply to IPv6 addresses on IP phones:

A link local address is never sent to Cisco Unified Communications Manager as a signaling and media address.

If the IP phone has both unique local and global addresses, the highest scoped global addresses take precedence over unique
                                       local addresses.

If the IP phone has multiple unique local addresses or multiple global addresses, the first address configured is the one
                                       used for signaling and media.

The following priority order applies to IPv6 addresses configured on an IP phone:

Use the IPv6 address configured manually through the phone's user interface (UI).

If a manually configured address is not available, but stateless auto-configuration (SLAAC) is enabled for the phone, then
                                             the phone uses SLAAC to create an IPv6 address.

In Cisco Unified Communications Manager, SLAAC is On by default. With SLAAC, the phone uses the IPv6 network prefix advertised
                                                         in the link local router's Router Advertisements (RAs). The phone creates the IPv6 host ID by using the phone's MAC address
                                                         and the EUI-64 format for host IDs. If SLAAC is used, Stateless DHCP IPv6 provides IPv6 address for TFTP and DNS server.

### Cisco IOS Devices and IPv6 Addresses

Each interface of a Cisco IOS device can support a combination of the following addresses:

One IPv6 link local address, for example:

```
FE80::987:65FF:FE01:2345
```

Multiple IPv6 unique local addresses, for example:

```
FD00:AAAA:BBBB:CCCC:0987:65FF:FE01:2345
```

Multiple IPv6 global addresses, for example:

```
2001:0DB8:BBBB:CCCC:0987:65FF:FE01:2345
```

Multiple IPv4 addresses

Cisco IOS media termination points (MTPs) are associated with the router's interface through the sccp local <interface> command. The MTP inherits the IPv4 and IPv6 addresses of the interface.

## Configuration Parameters and Features for IPv6 in Unified CM

These configuration parameters and features support IPv6 in Cisco Unified Communications Manager (Unified CM):

Common device configuration for phones and trunks

IP addressing mode

IP addressing mode preference for signaling

Allow Stateless auto-configuration for phones

Role of the media termination point (MTP) in IPv6-enabled Unified CM clusters

New enterprise parameters

MTP selection

You can enable and configure IPv6 for an entire cluster and you can configure your IPv6 devices (as shown in Supported IPv6 Addressing Modes ) to use IPv6 for signaling and media.

### Common Device Configuration

Rather than add IPv6 configuration parameters to specific IP phones and SIP trunks and phones, you can use Unified CM's common
                                 device configuration template. This template contains the IPv6-specific configuration parameters for IP phones and SIP trunks.
                                 You can create and associate multiple common device configuration profiles to IP phones and SIP trunks.

To find the template, choose Device > Device Settings > Common Device Configuration .

The profile contains this configuration information for IPv6:

IP Addressing Mode

IP Addressing Mode Preference for Signaling

Allow (Stateless) Auto-Configuration for Phones

#### Default Common Device Configuration

There is no default common device configuration profile. Devices are initially set to <None>. If you enable IPv6 in the Unified
                                 CM cluster in this <None> configuration, then your IPv6 devices adopt the following settings:

IP Addressing Mode = IPv4 and IPv6

IP Addressing Mode Preference for Signaling = Use System Default

Allow (Stateless) Auto-Configuration for Phones = Default

For enterprise deployment models, you must configure IP Addressing Mode to IPv6.

#### IP Addressing Mode for IPv6 Phones

After you configure the common device configuration profile and assign it to your phones, the specified IP addressing modes
                                    will be applied. The IP addressing modes are:

IPv4 Only —The phone acquires and uses only one IPv4 address for all signaling and media. If the phone acquired an IPv6 address previously,
                                          it releases the IPv6 address.

IPv6 Only —The phone acquires and uses only one IPv6 address for all signaling and media. If the phone acquired an IPv4 address previously,
                                          it releases the IPv4 address.

IPv4 and IPv6 —The phone acquires and uses one IPv4 address and one IPv6 address. It can use the appropriate address as required for media.
                                          It uses either the IPv4 address or the IPv6 address for call control signaling.

If IPv6 is enabled in the Unified CM cluster, the default phone setting for IP addressing mode is IPv6. IP phones should not
                                    be configured for IPv4 and IPv6 , it should be configured for IPv6-only phones.

#### IP Addressing Modes for Media Streams Between Devices

Depending on the devices that you have chosen and the configuration profiles that you have set up, you can potentially have
                                    an assortment of devices using IPv4 addresses or IPv6 addresses. For two devices (such as phones) that support mismatched
                                    addressing modes, an IP addressing version incompatibility exists when a device with an IPv4 address wants to establish a
                                    RTP voice stream with a device with an IPv6 address. To resolve this IP addressing incompatibility for media, Unified CM dynamically
                                    inserts a media termination point (MTP) to convert the media stream from IPv4 to IPv6 or conversely. For more information
                                    on how and when MTPs are used for IPv6 calls, see Media Resources and Music on Hold Overview .

##### IP Addressing Mode Preference for Signaling for Phones

The phone IP Addressing Mode Preference for Signaling has three settings:

IPv4 —The phone uses its IPv4 address for call control signaling to Unified CM.

IPv6 —The phone uses its IPv6 address for call control signaling to Unified CM.

Use System Default —The phone uses the cluster-wide setting for IP Addressing Mode for Signaling if it has an address of that type. At first
                                          glance, you might worry that a cluster-wide setting could lead to incompatibility issues: What if a phone is using an IPv4
                                          address and it tries to set up a voice stream with a phone that is using an IPv6 address? Unified CM handles this situation
                                          dynamically. It inserts an MTP that converts the media stream from IPv4 to IPv6 and back again.

##### Allow (Stateless) Auto-Configuration for Phones

You can allow phones to receive an IP address and other information automatically. Your options are partly dependent on how
                                    you configure the link local router.

You have these options:

On —The phone can use Stateless Address Auto-Configuration (SLAAC), if supported by the link local router's configuration. It
                                          depends on the O and M bits in the Router Advertisements (RAs).

If the O-bit is set—The router allows the phone to use SLAAC to acquire its IP address and to use the DHCP server to acquire
                                                other information (such as the TFTP server address and DNS server address). This is known as stateless DHCP IPv6.

If the M-bit is set—The router does not allow the phone to use SLAAC but allows it to use the DHCP server to acquire its IP
                                                address and other information.

If neither bit is set—The router allows the phone to use SLAAC to acquire an IP address but does not allow it to use DHCP
                                                for other information. You need to configure a TFTP server address through the phone’s user interface (UI). The phone uses
                                                this TFTP server to download its configuration file and register to Unified CM. We do not recommend this for a production
                                                environment.

Off —The phone does not use SLAAC to acquire an IPv6 address.

Default —The phone uses the cluster-wide enterprise parameter configuration value for Allow (Stateless) Auto-Configuration for Phones.
                                          If IPv6 is enabled in the Unified CM cluster, the phone's default setting for Allow (Stateless) Auto-Configuration for Phones
                                          setting is Default . If the IP phone supports IPv6-only, it adopts the cluster-wide setting for Allow (Stateless) Auto-Configuration for Phones,
                                          but all IPv4 phones ignore this setting.

#### Common Device Profile Configuration for SIP Trunks

You can apply SIP trunk configuration settings through the Common Device Configuration profile that you create and assign
                                    to the IPv6-Only SIP trunk with ANAT disabled.

With IPv6 enabled and with IPv4 addresses defined on the Unified CM server, you can configure the SIP trunk to use either
                                    of these addresses as its source IP address for SIP signaling. The SIP trunk also listens for incoming SIP signaling on the
                                    configured incoming port number of the server's IPv4 or IPv6 address.

##### IP Addressing Mode for SIP Trunks

The SIP trunk IP addressing mode has three settings:

IPv4 Only —The SIP trunk uses the Unified CM IPv4 address for signaling and either an MTP or phone IPv4 address for media.

IPv6 Only —The SIP trunk uses the IPv6 address for signaling and either an MTP or phone IPv6 address for media.

IPv4 and IPv6 —For signaling, the SIP trunk will use either the Unified CM IPv4 address or the Unified CM IPv6 address. For media, the SIP
                                          trunk will use either an MTP IPv4 and/or IPv6 address or the phone IPv4 and/or IPv6 address.

If IPv6 is enabled in the Unified CM cluster, the default SIP trunk setting for the IP Addressing mode is IPv4 and IPv6. All
                                    IPv4 trunks (H.323 and MGCP) will ignore this setting.

For more information on these SIP trunk IP addressing modes, see SIP Trunks Using Delayed Offer .

##### IP Addressing Mode Preference for Signaling for SIP Trunks

The SIP trunk IP Addressing Mode Preference for Signaling is used only for outbound calls. Unified CM listens for incoming
                                    SIP signaling on the configured incoming port number of the server's address.

The SIP trunk IP Addressing Mode Preference for Signaling has three settings:

IPv4 —The SIP trunk uses the Unified CM IPv4 address as its source address for SIP signaling.

IPv6 —The SIP trunk uses the Unified CM IPv6 address as its source address for SIP signaling.

If IPv6 is enabled in the Unified CM cluster, this is the default SIP trunk setting for IP Addressing Mode Preference for
                                                      Signaling. All IPv4 trunks ignore this setting.

Use System Default— The SIP trunk uses the cluster-wide enterprise parameter configuration value for its IP addressing mode for signaling.

If IPv6 is enabled in the Unified CM cluster, the default SIP trunk setting for IP Addressing Mode Preference for Signaling
                                    is Use System Default . With this setting the SIP trunk will adopt the cluster-wide setting for IP Addressing Mode Preference for Signaling. All
                                    IPv4 trunks will ignore this setting.

The SIP trunk IP Addressing Mode Preference for Signaling is used only for outbound calls. Unified CM will listen for incoming
                                    SIP signaling on the configured incoming port number of the server's IPv4 and IPv6 address.

##### Allow Auto-Configuration for Phones

The parameter to Allow Auto-Configuration for Phones is not used by SIP trunks.

### Cluster-Wide Configuration (Enterprise Parameters)

Before configuring the cluster-wide parameters in Unified CM, configure each server with an IPv6 address. For details on Unified
                                 CM IPv6 address configuration, see Configuring IPv6 in Cisco Unified CM, page A-1. In the Unified CM Administration interface,
                                 select Enterprise Parameters > IPv6 Configuration Modes to configure the following cluster-wide IPv6 settings for each Unified CM server.

Enable IPv6

IP Addressing Mode Preference for Media

IP Addressing Mode Preference for Signaling

Allow Auto-Configuration for Phones

#### Enable IPv6

Set this parameter to True to enable IPv6. False is the default setting.

#### IP Addressing Mode Preference for Media

IP Addressing Mode Preference for Media has two setting options:

IPv4 (Default setting)

IPv6 setting

The cluster-wide IP Addressing Mode Preference for Media is different than the device-level IP addressing mode. The cluster-wide
                                 IP Addressing Mode Preference for Media:

Selects which IP addressing version will be used for media when a call is made between two dual-stack devices.

Is used when there is a mismatch in supported IP addressing versions between two devices. For example, if an IPv6-only device
                                       calls an IPv4-only device, an MTP must be inserted into the media path to convert from IPv4 to IPv6, and conversely.

From Release 15SU2 onwards, when calls are made over an SME cluster to a dial-stack-supported device, the configuration of
                                             the IP Addressing Mode Preference for Media enterprise parameter should be consistent for all clusters in the call flow. If
                                             there is any inconsistency in the parameter configuration between clusters, then the parameter configuration of the destination
                                             cluster is considered. For more information, see the Configure IP Addressing Preference for Cluster section of the System Configuration Guide for Cisco Unified Communications Manager .

Typically, both devices have MTP media resources available to them in their media resource group (MRG). The IP Addressing
                                 Mode Preference for Media is used to select which device's MTP is used to convert from IPv4 to IPv6 (and conversely) for the
                                 call, as follows:

If the IP Addressing Mode Preference for Media is set to IPv4, the MTP associated with the IPv6-only device is selected, so
                                       that the longest call leg between the device and the MTP uses IPv4.

If the IP Addressing Mode Preference for Media is set to IPv6, the MTP associated with the IPv4-only device is selected, so
                                       that the longest call leg between the device and the MTP uses IPv6.

If the preferred device’s MTP is not available, the other device's MTP is used.

If no MTPs are available, the call fails.

MTP resource allocation is discussed in detail in Media Resources and Music on Hold .

#### IP Addressing Mode Preference for Signaling

The cluster-wide setting for the IP Addressing Mode Preference for Signaling is used by devices whose IP Addressing Mode Preference
                                 for Signaling is set to Use System Default . The IP Addressing Mode Preference for Signaling has two setting options:

IPv4 (Default setting)

IPv6 setting

#### Allow (Stateless) Auto-Configuration for Phones

The cluster-wide setting to Allow (Stateless) Auto-Configuration for Phones is used by phones whose Allow (Stateless) Auto-Configuration
                                 for Phones parameter is set to Default. The parameter to Allow (Stateless) Auto-Configuration for Phones has two setting options:

On (Default setting)

Off

### IPv6 Address Configuration for Unified CM

After you configure an IPv6 address for the Unified CM server, you must also configure this address in the Unified CM Administration
                                 graphical user interface. This IPv6 address is used in the device configuration files stored on the cluster's TFTP servers.
                                 IPv6 devices can use this address to register with Unified CM. A server name can also be used, but an IPv6 DNS server is required
                                 to resolve this name to an IPv6 address.

|  | IP Addressing Mode | Description | Notes |
|---|---|---|---|
|  | IPv4-only stack | Used for some endpoints and gateways. |  |
|  | IPv6-only stack | Used for some endpoints and gateways. |  |
|  | Dual-stacks: IPv4-only and IPv6-only | Used for applications servers, such as Cisco Unified Communications Manager, Cisco Unity Connection, Cisco Emergency Responder,
                                       and Cisco Unified Survivable Remote Site Telephony (Unified SRST). | The session initiation protocol (SIP) session description protocol (SDP) attribute should not be configured to transition
                                       to IPv6-only. |
|  | IPv6 Aware | Used for applications servers that use IPv4 to transport IPv6 application information, such as the Cisco Prime Collaboration
                                       Provisioning module, Cisco Emergency Responder, and Unified CM. | IPv6 aware devices communicate with IPv4 addresses, but can receive and understand IPv6 addresses embedded in application
                                       protocol data units (PDUs). |
|  | Dual-stack | Used for applications servers, such as Cisco Unified Communications Manager, Cisco Unity Connection, Cisco Emergency Responder,
                                       and Cisco Unified Survivable Remote Site Telephony (Unified SRST). | - |

| Note | For a list of product configuration resources for IPv6, see Product Configuration Resources for IPv6 . |
|---|---|

| Endpoint (SIP) | IPv4-only | IPv6-only | Dual- Stacks: IPv4 and IPv6 | Comments |
|---|---|---|---|---|
| Cisco IP Phone 7811, 7821, 7841, 7861 | Yes | Yes | Yes |  |
| Cisco IP Phone 8811, 8841, 8845, 8851, 8861, 8865, 8875 | Yes | Yes | Yes |  |
| Cisco IP Conference Phone 7832 | Yes | Yes | Yes |  |
| Cisco IP Conference Phone 8832 | Yes | Yes | Yes |  |
| Catalyst 8000 Series Edge Platforms | Yes | No | Yes |  |
| Cisco Jabber | Yes | Yes | Yes | IPv6-only is for on-premise Jabber desktop deployment. No ANAT. |
| Cisco Webex Room Series, Board Series, Desk Series | Yes | Yes | Yes |  |

| Gateway | Applications | IPv4-only | IPv6-only | Dual- Stacks: IPv4 and IPv6 | Comments |
|---|---|---|---|---|---|
|  | Note The "Yes" and "No" means whether the IP Addressing mode is supported or not. | Note | The "Yes" and "No" means whether the IP Addressing mode is supported or not. |
| Note | The "Yes" and "No" means whether the IP Addressing mode is supported or not. |
| Cisco 4000 Series Integrated Services Routers (ISR) | IOS Gateways | Yes | No | Yes | For more information, see Cisco IOS Unified Communications Gateways with SIP |
| Unified SRST | Yes | No | Yes |  |
| CUBE | Yes | No | Yes | Only ISR G2. |
| MTP | Yes | No | Yes |  |
| Cisco 2900 and 3900 Series Integrated Services Routers (ISR) | IOS Gateways | Yes | No | No | EOS Notices for ISR 28xx / 38xx / 29xx / 39xx |
| Unified SRST | Yes | No | No |  |
| CUBE | Yes | No | Yes |  |
| MTP | Yes | No | Yes |  |
| H.323 Gateways |  | Yes | No | No | EOS Notice for the H.323  Call Control features in Cisco IOS-XE Software EOS Notices for ISR 28xx / 38xx / 29xx / 39xx |
| Media Gateway Control Protocol (MGCP) Gateways |  | Yes | No | No | EOS Notices for ISR 28xx / 38xx / 29xx / 39xx |

| Note | The "Yes" and "No" means whether the IP Addressing mode is supported or not. |
|---|---|

| Application or Interface | IPv4-only | IPv6-only | Dual- Stacks: IPv4 and IPv6 | Comments |
|---|---|---|---|---|
| Cisco Unified Communications Manager (Unified CM) | Yes | No | Yes | Product required for IPv6 deployment. |
| Cisco Unified Communications Manager IM and Presence Service (IM and Presence Service) | Yes | No | Yes | Product required for IPv6 deployment. |
| Cisco Unified Communications Manager Express (Unified CME) | Yes | No | No |  |
| Cisco Unified Survivable Remote Site Telephony (Unified SRST) | Yes | No | Yes | Product required for IPv6 deployment for ISR G3. |
| Cisco Unified Contact Center Enterprise (Unified CCE) | Yes | No | Yes | For Agent IPv6-only stack, NAT64. |
| Cisco Unified Contact Center Express (Unified CCX) | Yes | No | Yes | For Agent IPv6-only stack, NAT64. |
| Cisco Emergency Responder (Emergency Responder) | Yes | No | Yes |  |
| Cisco Unity Connection | Yes | No | Yes |  |
| Cisco Meeting Server | Yes | No | No |  |
| Cisco TelePresence Management Suite | Yes | No | No |  |
| Cisco Unity Express | Yes | No | No |  |
| End-of-Sale: Cisco Unified MeetingPlace | Yes | No | No | EOS Notice |
| Cisco Prime Collaboration | Yes | No | Yes | Applicable to IOS Gateways, Unified SRST, CUBE. |
| Cisco Smart Software Licensing | Yes | No | Yes | Applicable to Unified CM, IM and Presence Service, Cisco Unity Connection. |
| LAN/WAN | Yes | Yes | Yes |  |
| Dynamic Host Configuration Protocol (DHCP) | Yes | Yes | Yes |  |
| Domain Name System (DNS) | Yes | Yes | Yes |  |
| Directory LDAP | Yes | Yes | Yes |  |
| NAT64 | Yes | No | No | Except for Unified CCE and Unified CCX, which have internal NAT64. |

| Note | IPv6 NAT-based solution is not supported. |
|---|---|

| Note | In Cisco Unified Communications Manager, SLAAC is On by default. With SLAAC, the phone uses the IPv6 network prefix advertised
                                                         in the link local router's Router Advertisements (RAs). The phone creates the IPv6 host ID by using the phone's MAC address
                                                         and the EUI-64 format for host IDs. If SLAAC is used, Stateless DHCP IPv6 provides IPv6 address for TFTP and DNS server. |
|---|---|

| Note | For enterprise deployment models, you must configure IP Addressing Mode to IPv6. |
|---|---|

| Note | If IPv6 is enabled in the Unified CM cluster, this is the default SIP trunk setting for IP Addressing Mode Preference for
                                                      Signaling. All IPv4 trunks ignore this setting. |
|---|---|

| Note | From Release 15SU2 onwards, when calls are made over an SME cluster to a dial-stack-supported device, the configuration of
                                             the IP Addressing Mode Preference for Media enterprise parameter should be consistent for all clusters in the call flow. If
                                             there is any inconsistency in the parameter configuration between clusters, then the parameter configuration of the destination
                                             cluster is considered. For more information, see the Configure IP Addressing Preference for Cluster section of the System Configuration Guide for Cisco Unified Communications Manager . |
|---|---|