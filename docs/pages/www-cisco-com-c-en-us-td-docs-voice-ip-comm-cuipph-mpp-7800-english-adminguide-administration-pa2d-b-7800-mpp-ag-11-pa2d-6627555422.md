---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7800-english-adminguide-administration-pa2d-b-7800-mpp-ag-11-pa2d-6627555422
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7800/english/adminguide/administration/pa2d_b_7800-mpp-ag-11/pa2d_b_7800-mpp-ag-11_chapter_0101.html
retrieved_at: 2026-09-01T15:41:00.985414+00:00
---

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

# Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

Updated: April 29, 2019

Chapter: Technical Details

## Chapter: Technical Details

# Technical Details

## Overview of the Cisco IP Phone

The Cisco IP Phone 7800 Series Multiplatform Phones comprises a set of full-featured VoIP (Voice-over-Internet Protocol) phones that provide voice communication over an IP network.
                           The phones provide all the features of traditional business phones, such as call forwarding, redialing, speed dialing, transferring
                           calls, and conference calling. The Cisco IP Phone 7800 Series Multiplatform Phones is targeted for solutions that are centered on Third-Party SIP-based IP PBX.

In this document, the terms Cisco IP Phone or phone mean Cisco IP Phone 7800 Series Multiplatform Phones .

## Physical and Operating Environment Specifications

The following table shows the physical and operating environment specifications for the Cisco IP Phone 7800 Series with Multiplatform
                              Firmware.

Specification

Value or
                                          					 Range

Operating
                                          					 temperature

32° to
                                          					 104°F (0° to 40°C)

Operating
                                          					 relative humidity

10% to 90%
                                          					 (noncondensing)

Storage
                                          					 temperature

14° to
                                          					 140°F (–10° to 60°C)

Height

8.14 in.
                                          					 (207 mm)

Width

Cisco IP Phone 7811— 7.67 in. (195 mm)

Cisco IP Phone 7821 — 8.11 in. (206 mm)

Cisco IP Phone 7841 — 8.11 in. (206 mm)

Cisco IP Phone 7861— 10.42 in. (264.91 mm)

Depth

1.1 in.
                                          					 (28 mm)

Weight

Cisco IP Phone 7811— 0.84 kg

- Cisco IP Phone 7821 — 0.867 kg

- Cisco IP Phone 7841 — 0.868 kg

- Cisco IP Phone 7861— 1.053 kg

Power

- 100-240 VAC, 50-60 Hz, 0.5
                                             						A—When using the AC adapter

- 48 VDC, 0.2 A—When using
                                             						the in-line power over the network cable

Cables

Category 3/5/5e/6 for 10-Mbps cables with 4 pairs

Category 5/5e/6 for 100-Mbps cables with 4 pairs

Cisco IP Phone 7841: Category 5/5e/6 for 1000-Mbps cables with 4
                                          					 pairs

Cables
                                                      						have 4 pairs of wires for a total of 8 conductors.

Distance
                                          					 Requirements

As
                                          					 supported by the Ethernet Specification, it is assumed that the maximum cable
                                          					 length between each Cisco IP Phone and the switch is 100 meters (330 feet).

For more information, see the Cisco IP Phone 7800 Series Data Sheet : https://www.cisco.com/c/en/us/products/collaboration-endpoints/ip-phone-7800-series-multiplatform-firmware/datasheet-listing.html

## Cable Specifications

RJ-9 jack (4-conductor) for handset and headset connection.

The Cisco IP Phone 7811 does not contain a headset jack.

RJ-45 jack for the LAN 10/100BaseT connection (on  Cisco IP Phones 7811, 7821, and 7861) and the LAN 1000BaseT connection
                                    (on the Cisco IP Phone 7841).

RJ-45 jack for a second 10/100BaseT compliant connection (on Cisco IP Phones 7811, 7821, and 7861) and the LAN 1000BaseT connection
                                    (on the Cisco IP Phone 7841).

48-volt power connector.

## Network and Computer Port Pinouts

Although both the network and computer (access) ports are used for network connectivity, they serve different purposes and
                              have different port pinouts:

The network port is the 10/100 SW port; the Cisco IP Phone 7841 has a 10/100/1000 SW network port.

The computer (access) port is the 10/100 PC port; the Cisco IP Phone 7841 has a 10/100/1000 PC computer port.

### Network Port Connector

The following table describes the network port connector pinouts.

Pin Number

Function

1

BI_DA+

2

BI_DA-

3

BI_DB+

4

BI_DC+

5

BI_DC-

6

BI_DB-

7

BI_DD+

8

BI_DD-

BI stands for bidirectional, while DA, DB, DC, and DD stand for Data A, Data B, Data C, and Data D respectively.

### Computer Port Connector

The following table describes the computer port connector pinouts.

Pin Number

Function

1

BI_DB+

2

BI_DB-

3

BI_DA+

4

BI_DD+

5

BI_DD-

6

BI_DA-

7

BI_DC+

8

BI_DC-

BI stands for bidirectional, while DA, DB, DC, and DD stand for Data A, Data B, Data C, and Data D respectively.

## Phone Power
                        	 Requirements

The 
                              		Cisco IP Phone can be powered with external power or with Power over
                              		Ethernet (PoE). A separate power supply provides external power. The switch can
                              		provide PoE through the phone Ethernet cable.

When you install a
                                          		  phone that is powered with external power, connect the power supply to the
                                          		  phone and to a power outlet before you connect the Ethernet cable to the phone.
                                          		  When you remove a phone that is powered with external power, disconnect the
                                          		  Ethernet cable from the phone before you disconnect the power supply.

Power Type

Guidelines

External
                                          					 power: Provided through the CP-PWR-CUBE-3= external power supply

The 
                                          					 Cisco IP Phone uses the CP-PWR-CUBE-3 power supply.

External power—Provided through the Cisco IP Phone Power Injector

The Cisco IP Phone Power Injector may be used with most Cisco IP Phones. The phone datasheet identifies if the phone can use
                                          the power injector.

Functioning as a midspan device, the injector delivers inline power to the attached phone. The Cisco IP Phone Power Injector
                                          connects between a switch port and the IP Phone, and supports a maximum cable length of 100m between the unpowered switch
                                          and the IP phone.

PoE
                                          					 power—Provided by a switch through the Ethernet cable attached to the phone.

To ensure
                                          					 uninterruptible operation of the phone, make sure that the switch has a backup
                                          					 power supply.

Make sure
                                          					 that the CatOS or IOS version that runs on your switch supports your intended
                                          					 phone deployment. See the documentation for your switch for operating system
                                          					 version information.

The documents in the following table provide more information on the following topics:

Cisco switches that work with Cisco IP Phones

Cisco IOS releases that support bidirectional power negotiation

Other requirements and restrictions about power

Document topics

URL

PoE Solutions

http://www.cisco.com/c/en/us/solutions/enterprise-networks/power-over-ethernet-solutions/index.html

Cisco Catalyst Switches

http://www.cisco.com/c/en/us/products/switches/index.html

Integrated Service Routers

http://www.cisco.com/c/en/us/products/routers/index.html

Cisco IOS Software

http://www.cisco.com/c/en/us/products/ios-nx-os-software/index.html

### Power Outage

Your access to emergency service through the phone requires that the phone receive power. If a power interruption occurs,
                              service or emergency calling service dialing does not function until power is restored. If a power failure or disruption occurs,
                              you may need to reset or reconfigure the equipment before you can use service or emergency calling service dialing.

### Power Reduction

You can reduce the amount of energy that the Cisco IP Phone consumes by using Power Save mode.

In Power Save mode, the backlight on the screen is not lit when the phone is not in use. The phone remains in Power Save mode
                                       until the user lifts the handset or presses any button. Set up each phone to enable or disable Power Save settings.

The Cisco IP Phone 7811 does not support Power Save because the phone screen does not have a backlight.

### Power Negotiation Over LLDP

The phone and the switch negotiate the power that the phone consumes. Cisco IP Phone operates at multiple power settings,
                              which lowers power consumption when less power is available.

After a phone reboots, the switch locks to one protocol (CDP or LLDP) for power negotiation. The switch locks to the first
                              protocol (containing a power Threshold Limit Value [TLV]) that the phone transmits. If the system administrator disables that
                              protocol on the phone, the phone cannot power up any accessories because the switch does not respond to power requests in
                              the other protocol.

Cisco recommends that Power Negotiation always be enabled (default) when connecting to a switch that supports power negotiation.

If Power Negotiation is disabled, the switch may disconnect power to the phone. If the switch does not support power negotiation,
                              disable the Power Negotiation feature before you power up accessories over PoE. When the Power Negotiation feature is disabled,
                              the phone can power the accessories up to the maximum that the IEEE 802.3af-2003 standard allows.

When CDP and Power Negotiation are disabled, the phone can power the accessories up to 15.4W.

## Network Protocols

Cisco IP Phones support several industry-standard and Cisco network protocols that are required for voice communication. The
                              following table provides an overview of the network protocols that the phones support.

Network
                                          					 Protocol

Purpose

Usage
                                          					 Notes

Bootstrap
                                          					 Protocol (BootP)

BootP
                                          					 enables a network device, such as the Cisco IP Phone, to discover certain startup
                                          					 information, such as its IP address.

—

Cisco
                                          					 Discovery Protocol (CDP)

CDP is a
                                          					 device-discovery protocol that runs on all Cisco-manufactured equipment.

A device can use CDP to advertise its existence to other devices and receive information
                                          					 about other devices in the network.

The Cisco
                                          					 IP Phone uses CDP to communicate information such as auxiliary VLAN ID, per
                                          					 port power management details, and Quality of Service (QoS) configuration
                                          					 information with the Cisco Catalyst switch.

Domain Name Server (DNS)

DNS translates domain names to IP addresses.

Cisco IP Phones have a DNS client to translate domain names into IP addresses.

Dynamic
                                          					 Host Configuration Protocol (DHCP)

DHCP
                                          					 dynamically allocates and assigns an IP address to network devices.

DHCP
                                          					 enables you to connect an IP phone into the network and have the phone become
                                          					 operational without the need to manually assign an IP address or to
                                          					 configure additional network parameters.

DHCP is enabled by default. If disabled, you must manually configure the IP address, subnet mask, and gateway on each phone
                                          locally.

We recommend that you use the DHCP custom option 160, 159.

Hypertext Transfer Protocol (HTTP)

HTTP is
                                          					 the standard protocol for transfer of information and movement of documents across the
                                          					 Internet and the web.

Cisco IP
                                          					 Phones use HTTP for XML services, provisioning, upgrade and for troubleshooting purposes.

Hypertext Transfer Protocol Secure (HTTPS)

Hypertext Transfer Protocol Secure (HTTPS) is a combination of
                                          					 the Hypertext Transfer Protocol with the SSL/TLS protocol to provide encryption
                                          					 and secure identification of servers.

Web
                                          					 applications with both HTTP and HTTPS support have two URLs configured. Cisco
                                          					 IP Phones that support HTTPS choose the HTTPS URL.

A lock
                                          					 icon is displayed to the user if the connection to the service is via HTTPS.

Internet
                                          					 Protocol (IP)

IP is a
                                          					 messaging protocol that addresses and sends packets across the network.

To
                                          					 communicate with IP, network devices must have an assigned IP address, subnet,
                                          					 and gateway.

IP
                                          					 addresses, subnets, and gateways identifications are automatically assigned if
                                          					 you are using the Cisco IP Phone with Dynamic Host Configuration Protocol
                                          					 (DHCP). If you are not using DHCP, you must manually assign these properties to
                                          					 each phone locally.

Link
                                          					 Layer Discovery Protocol (LLDP)

LLDP is
                                          					 a standardized network discovery protocol (similar to CDP) that is supported on
                                          					 some Cisco and third-party devices.

The
                                          					 Cisco IP Phone supports LLDP on the PC port.

Link
                                          					 Layer Discovery Protocol-Media Endpoint Devices (LLDP-MED)

LLDP-MED
                                          					 is an extension of the LLDP standard developed for voice products.

The
                                          					 Cisco IP Phone supports LLDP-MED on the SW port to communicate information such
                                          					 as:

Voice VLAN configuration

Device discovery

Power management

Inventory management

For more
                                          					 information about LLDP-MED support, see the LLDP-MED and Cisco Discovery Protocol white paper at this URL: http://www.cisco.com/en/US/tech/tk652/tk701/technologies_white_paper0900aecd804cd46d.shtml

Network Transport Protocol (NTP)

NTP is a networking protocol for clock synchronization between computer systems over packet-switched, variable-latency data
                                          networks.

Cisco IP Phones have an NTP client integrated into the software.

Real-Time Transport Protocol (RTP)

RTP is a
                                          					 standard protocol for transporting real-time data, such as interactive voice
                                          					 and video, over data networks.

Cisco IP
                                          					 Phones use the RTP protocol to send and receive real-time voice traffic from
                                          					 other phones and gateways.

Real-Time Control Protocol (RTCP)

RTCP
                                          					 works in conjunction with RTP to provide QoS data (such as jitter, latency, and
                                          					 round trip delay) on RTP streams.

RTCP is
                                          					 disabled by default.

Session Description Protocol (SDP)

SDP is the portion of the SIP protocol that determines which parameters are available during a connection between two endpoints.
                                          Conferences are established by using only the SDP capabilities that all endpoints in the conference support.

SDP capabilities, such as codec types, DTMF detection, and comfort noise, are normally configured on a global basis by a Third-Party
                                          Call Control System or a Media Gateway in operation. Some SIP endpoints may allow configuration of these parameters on the
                                          endpoint itself.

Session
                                          					 Initiation Protocol (SIP)

SIP is
                                          					 the Internet Engineering Task Force (IETF) standard for multimedia conferencing
                                          					 over IP. SIP is an ASCII-based application-layer control protocol (defined in
                                          					 RFC 3261) that can be used to establish, maintain, and terminate calls between
                                          					 two or more endpoints.

Like
                                          					 other VoIP protocols, SIP is designed to address the functions of signaling and
                                          					 session management within a packet telephony network. Signaling allows call
                                          					 information to be carried across network boundaries. Session management
                                          					 provides the ability to control the attributes of an end-to-end call.

Secure
                                          					 Real-Time Transfer protocol (SRTP)

SRTP is
                                          					 an extension of the Real-Time Protocol (RTP) Audio/Video Profile and ensures
                                          					 the integrity of RTP and Real-Time Control Protocol (RTCP) packets providing
                                          					 authentication, integrity, and encryption of media packets between two
                                          					 endpoints.

Cisco IP
                                          					 Phones use SRTP for media encryption.

Transmission Control Protocol (TCP)

TCP is a
                                          					 connection-oriented transport protocol.

—

Transport Layer Security (TLS)

TLS is a
                                          					 standard protocol for securing and authenticating communications.

When security is implemented, Cisco IP Phones use the TLS protocol when securely registering with the third-party call control
                                          system.

Trivial
                                          					 File Transfer Protocol (TFTP)

TFTP
                                          					 allows you to transfer files over the network.

On the
                                          					 Cisco IP Phone, TFTP enables you to obtain a configuration file specific to the
                                          					 phone type.

TFTP
                                          					 requires a TFTP server in your network, which can be automatically identified
                                          					 from the DHCP server.

User
                                          					 Datagram Protocol (UDP)

UDP is a
                                          					 connectionless messaging protocol for delivery of data packets.

UDP is used only for RTP streams. SIP uses UDP, TCP, and TLS.

## VLAN Interaction

The Cisco IP Phone contains an internal Ethernet switch, enabling forwarding of packets to the phone, and to the computer
                              (access) port and the network port on the back of the phone.

If a computer is connected to the computer (access) port, the computer and the phone share the same physical link to the switch
                              and share the same port on the switch. This shared physical link has the following implications for the VLAN configuration
                              on the network:

The current VLANs might be configured on an IP subnet basis. However, additional IP addresses might not be available to assign
                                    the phone to the same subnet as other devices that connect to the same port.

Data traffic present on the VLAN supporting phones might reduce the quality of VoIP traffic.

Network security may indicate a need to isolate the VLAN voice traffic from the VLAN data traffic.

You can resolve these issues by isolating the voice traffic onto a separate VLAN. The switch port to which the phone connects
                              would be configured for separate VLANs for carrying:

Voice traffic to and from the IP phone (auxiliary VLAN on the Cisco Catalyst 6000 series, for example)

Data traffic to and from the PC that connects to the switch through the computer (access) port of the IP phone (native VLAN)

Isolating the phones on a separate, auxiliary VLAN increases the quality of the voice traffic and allows a large number of
                              phones to be added to an existing network that does not have enough IP addresses for each phone.

For more information, see the documentation that is included with a Cisco switch. You can also access switch information at
                              this URL:

http://cisco.com/en/US/products/hw/switches/index.html

## External Devices

We recommend that you use good-quality external devices that are shielded against unwanted radio frequency (RF) and audio
                           frequency (AF) signals. External devices include headsets, cables, and connectors.

Depending on the quality of these devices and their proximity to other devices, such as mobile phones or two-way radios, some
                           audio noise may still occur. In these cases, we recommend that you take one or more of these actions:

Move the external device away from the source of the RF or AF signals.

Route the external device cables away from the source of the RF or AF signals.

Use shielded cables for the external device, or use cables with a better shield and connector.

Shorten the length of the external device cable.

Apply ferrites or other such devices on the cables for the external device.

Cisco cannot guarantee the performance of external devices, cables, and connectors.

In European Union countries, use only external speakers, microphones, and headsets that are fully compliant with the EMC Directive
                                       [89/336/EC].

| Note | In this document, the terms Cisco IP Phone or phone mean Cisco IP Phone 7800 Series Multiplatform Phones . |
|---|---|

| Specification | Value or
                                          					 Range |
|---|---|
| Operating
                                          					 temperature | 32° to
                                          					 104°F (0° to 40°C) |
| Operating
                                          					 relative humidity | 10% to 90%
                                          					 (noncondensing) |
| Storage
                                          					 temperature | 14° to
                                          					 140°F (–10° to 60°C) |
| Height | 8.14 in.
                                          					 (207 mm) |
| Width | Cisco IP Phone 7811— 7.67 in. (195 mm) Cisco IP Phone 7821 — 8.11 in. (206 mm) Cisco IP Phone 7841 — 8.11 in. (206 mm) Cisco IP Phone 7861— 10.42 in. (264.91 mm) |
| Depth | 1.1 in.
                                          					 (28 mm) |
| Weight | Cisco IP Phone 7811— 0.84 kg Cisco IP Phone 7821 — 0.867 kg Cisco IP Phone 7841 — 0.868 kg Cisco IP Phone 7861— 1.053 kg |
| Power | 100-240 VAC, 50-60 Hz, 0.5
                                             						A—When using the AC adapter 48 VDC, 0.2 A—When using
                                             						the in-line power over the network cable |
| Cables | Cisco IP Phone 7811, 7821, 7841, and 7861: Category 3/5/5e/6 for 10-Mbps cables with 4 pairs Category 5/5e/6 for 100-Mbps cables with 4 pairs Cisco IP Phone 7841: Category 5/5e/6 for 1000-Mbps cables with 4
                                          					 pairs Note Cables
                                                      						have 4 pairs of wires for a total of 8 conductors. | Note | Cables
                                                      						have 4 pairs of wires for a total of 8 conductors. |
| Note | Cables
                                                      						have 4 pairs of wires for a total of 8 conductors. |
| Distance
                                          					 Requirements | As
                                          					 supported by the Ethernet Specification, it is assumed that the maximum cable
                                          					 length between each Cisco IP Phone and the switch is 100 meters (330 feet). |

| Note | Cables
                                                      						have 4 pairs of wires for a total of 8 conductors. |
|---|---|

| Note | The Cisco IP Phone 7811 does not contain a headset jack. |
|---|---|

| Pin Number | Function |
|---|---|
| 1 | BI_DA+ |
| 2 | BI_DA- |
| 3 | BI_DB+ |
| 4 | BI_DC+ |
| 5 | BI_DC- |
| 6 | BI_DB- |
| 7 | BI_DD+ |
| 8 | BI_DD- |
| Note BI stands for bidirectional, while DA, DB, DC, and DD stand for Data A, Data B, Data C, and Data D respectively. | Note | BI stands for bidirectional, while DA, DB, DC, and DD stand for Data A, Data B, Data C, and Data D respectively. |
| Note | BI stands for bidirectional, while DA, DB, DC, and DD stand for Data A, Data B, Data C, and Data D respectively. |

| Note | BI stands for bidirectional, while DA, DB, DC, and DD stand for Data A, Data B, Data C, and Data D respectively. |
|---|---|

| Pin Number | Function |
|---|---|
| 1 | BI_DB+ |
| 2 | BI_DB- |
| 3 | BI_DA+ |
| 4 | BI_DD+ |
| 5 | BI_DD- |
| 6 | BI_DA- |
| 7 | BI_DC+ |
| 8 | BI_DC- |
| Note BI stands for bidirectional, while DA, DB, DC, and DD stand for Data A, Data B, Data C, and Data D respectively. | Note | BI stands for bidirectional, while DA, DB, DC, and DD stand for Data A, Data B, Data C, and Data D respectively. |
| Note | BI stands for bidirectional, while DA, DB, DC, and DD stand for Data A, Data B, Data C, and Data D respectively. |

| Note | BI stands for bidirectional, while DA, DB, DC, and DD stand for Data A, Data B, Data C, and Data D respectively. |
|---|---|

| Note | When you install a
                                          		  phone that is powered with external power, connect the power supply to the
                                          		  phone and to a power outlet before you connect the Ethernet cable to the phone.
                                          		  When you remove a phone that is powered with external power, disconnect the
                                          		  Ethernet cable from the phone before you disconnect the power supply. |
|---|---|

| Power Type | Guidelines |
|---|---|
| External
                                          					 power: Provided through the CP-PWR-CUBE-3= external power supply | The 
                                          					 Cisco IP Phone uses the CP-PWR-CUBE-3 power supply. |
| External power—Provided through the Cisco IP Phone Power Injector | The Cisco IP Phone Power Injector may be used with most Cisco IP Phones. The phone datasheet identifies if the phone can use
                                          the power injector. Functioning as a midspan device, the injector delivers inline power to the attached phone. The Cisco IP Phone Power Injector
                                          connects between a switch port and the IP Phone, and supports a maximum cable length of 100m between the unpowered switch
                                          and the IP phone. |
| PoE
                                          					 power—Provided by a switch through the Ethernet cable attached to the phone. | To ensure
                                          					 uninterruptible operation of the phone, make sure that the switch has a backup
                                          					 power supply. Make sure
                                          					 that the CatOS or IOS version that runs on your switch supports your intended
                                          					 phone deployment. See the documentation for your switch for operating system
                                          					 version information. |

| Document topics | URL |
|---|---|
| PoE Solutions | http://www.cisco.com/c/en/us/solutions/enterprise-networks/power-over-ethernet-solutions/index.html |
| Cisco Catalyst Switches | http://www.cisco.com/c/en/us/products/switches/index.html |
| Integrated Service Routers | http://www.cisco.com/c/en/us/products/routers/index.html |
| Cisco IOS Software | http://www.cisco.com/c/en/us/products/ios-nx-os-software/index.html |

| Note | The Cisco IP Phone 7811 does not support Power Save because the phone screen does not have a backlight. |
|---|---|

| Note | When CDP and Power Negotiation are disabled, the phone can power the accessories up to 15.4W. |
|---|---|

| Network
                                          					 Protocol | Purpose | Usage
                                          					 Notes |
|---|---|---|
| Bootstrap
                                          					 Protocol (BootP) | BootP
                                          					 enables a network device, such as the Cisco IP Phone, to discover certain startup
                                          					 information, such as its IP address. | — |
| Cisco
                                          					 Discovery Protocol (CDP) | CDP is a
                                          					 device-discovery protocol that runs on all Cisco-manufactured equipment. A device can use CDP to advertise its existence to other devices and receive information
                                          					 about other devices in the network. | The Cisco
                                          					 IP Phone uses CDP to communicate information such as auxiliary VLAN ID, per
                                          					 port power management details, and Quality of Service (QoS) configuration
                                          					 information with the Cisco Catalyst switch. |
| Domain Name Server (DNS) | DNS translates domain names to IP addresses. | Cisco IP Phones have a DNS client to translate domain names into IP addresses. |
| Dynamic
                                          					 Host Configuration Protocol (DHCP) | DHCP
                                          					 dynamically allocates and assigns an IP address to network devices. DHCP
                                          					 enables you to connect an IP phone into the network and have the phone become
                                          					 operational without the need to manually assign an IP address or to
                                          					 configure additional network parameters. | DHCP is enabled by default. If disabled, you must manually configure the IP address, subnet mask, and gateway on each phone
                                          locally. We recommend that you use the DHCP custom option 160, 159. |
| Hypertext Transfer Protocol (HTTP) | HTTP is
                                          					 the standard protocol for transfer of information and movement of documents across the
                                          					 Internet and the web. | Cisco IP
                                          					 Phones use HTTP for XML services, provisioning, upgrade and for troubleshooting purposes. |
| Hypertext Transfer Protocol Secure (HTTPS) | Hypertext Transfer Protocol Secure (HTTPS) is a combination of
                                          					 the Hypertext Transfer Protocol with the SSL/TLS protocol to provide encryption
                                          					 and secure identification of servers. | Web
                                          					 applications with both HTTP and HTTPS support have two URLs configured. Cisco
                                          					 IP Phones that support HTTPS choose the HTTPS URL. A lock
                                          					 icon is displayed to the user if the connection to the service is via HTTPS. |
| Internet
                                          					 Protocol (IP) | IP is a
                                          					 messaging protocol that addresses and sends packets across the network. | To
                                          					 communicate with IP, network devices must have an assigned IP address, subnet,
                                          					 and gateway. IP
                                          					 addresses, subnets, and gateways identifications are automatically assigned if
                                          					 you are using the Cisco IP Phone with Dynamic Host Configuration Protocol
                                          					 (DHCP). If you are not using DHCP, you must manually assign these properties to
                                          					 each phone locally. |
| Link
                                          					 Layer Discovery Protocol (LLDP) | LLDP is
                                          					 a standardized network discovery protocol (similar to CDP) that is supported on
                                          					 some Cisco and third-party devices. | The
                                          					 Cisco IP Phone supports LLDP on the PC port. |
| Link
                                          					 Layer Discovery Protocol-Media Endpoint Devices (LLDP-MED) | LLDP-MED
                                          					 is an extension of the LLDP standard developed for voice products. | The
                                          					 Cisco IP Phone supports LLDP-MED on the SW port to communicate information such
                                          					 as: Voice VLAN configuration Device discovery Power management Inventory management For more
                                          					 information about LLDP-MED support, see the LLDP-MED and Cisco Discovery Protocol white paper at this URL: http://www.cisco.com/en/US/tech/tk652/tk701/technologies_white_paper0900aecd804cd46d.shtml |
| Network Transport Protocol (NTP) | NTP is a networking protocol for clock synchronization between computer systems over packet-switched, variable-latency data
                                          networks. | Cisco IP Phones have an NTP client integrated into the software. |
| Real-Time Transport Protocol (RTP) | RTP is a
                                          					 standard protocol for transporting real-time data, such as interactive voice
                                          					 and video, over data networks. | Cisco IP
                                          					 Phones use the RTP protocol to send and receive real-time voice traffic from
                                          					 other phones and gateways. |
| Real-Time Control Protocol (RTCP) | RTCP
                                          					 works in conjunction with RTP to provide QoS data (such as jitter, latency, and
                                          					 round trip delay) on RTP streams. | RTCP is
                                          					 disabled by default. |
| Session Description Protocol (SDP) | SDP is the portion of the SIP protocol that determines which parameters are available during a connection between two endpoints.
                                          Conferences are established by using only the SDP capabilities that all endpoints in the conference support. | SDP capabilities, such as codec types, DTMF detection, and comfort noise, are normally configured on a global basis by a Third-Party
                                          Call Control System or a Media Gateway in operation. Some SIP endpoints may allow configuration of these parameters on the
                                          endpoint itself. |
| Session
                                          					 Initiation Protocol (SIP) | SIP is
                                          					 the Internet Engineering Task Force (IETF) standard for multimedia conferencing
                                          					 over IP. SIP is an ASCII-based application-layer control protocol (defined in
                                          					 RFC 3261) that can be used to establish, maintain, and terminate calls between
                                          					 two or more endpoints. | Like
                                          					 other VoIP protocols, SIP is designed to address the functions of signaling and
                                          					 session management within a packet telephony network. Signaling allows call
                                          					 information to be carried across network boundaries. Session management
                                          					 provides the ability to control the attributes of an end-to-end call. |
| Secure
                                          					 Real-Time Transfer protocol (SRTP) | SRTP is
                                          					 an extension of the Real-Time Protocol (RTP) Audio/Video Profile and ensures
                                          					 the integrity of RTP and Real-Time Control Protocol (RTCP) packets providing
                                          					 authentication, integrity, and encryption of media packets between two
                                          					 endpoints. | Cisco IP
                                          					 Phones use SRTP for media encryption. |
| Transmission Control Protocol (TCP) | TCP is a
                                          					 connection-oriented transport protocol. | — |
| Transport Layer Security (TLS) | TLS is a
                                          					 standard protocol for securing and authenticating communications. | When security is implemented, Cisco IP Phones use the TLS protocol when securely registering with the third-party call control
                                          system. |
| Trivial
                                          					 File Transfer Protocol (TFTP) | TFTP
                                          					 allows you to transfer files over the network. On the
                                          					 Cisco IP Phone, TFTP enables you to obtain a configuration file specific to the
                                          					 phone type. | TFTP
                                          					 requires a TFTP server in your network, which can be automatically identified
                                          					 from the DHCP server. |
| User
                                          					 Datagram Protocol (UDP) | UDP is a
                                          					 connectionless messaging protocol for delivery of data packets. | UDP is used only for RTP streams. SIP uses UDP, TCP, and TLS. |

| Caution | In European Union countries, use only external speakers, microphones, and headsets that are fully compliant with the EMC Directive
                                       [89/336/EC]. |
|---|---|