---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7800-series-english-admin-guide-pa2d-b-7800-series-admin-guide-cucm-p-a79341af26
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7800-series/english/admin-guide/pa2d_b_7800-series-admin-guide-cucm/pa2d_b_7800-series-admin-guide-cucm_chapter_010.html
retrieved_at: 2026-08-21T13:26:00.959677+00:00
---

Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

# Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

Updated: May 29, 2025

Chapter: Technical Details

## Chapter: Technical Details

# Technical Details

## Physical and
                        	 Operating Environment Specifications

The following table shows the physical and operating environment specifications for the Cisco IP Phone 7800 Series.

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
                                          					 length between each Cisco IP Phone and the switch is 100meters (330feet).

## Cable Specifications

RJ-9 jack (4-conductor) for handset and headset connection.

The Cisco IP Phone 7811 does not contain a headset jack.

RJ-45 jack for the LAN 10/100BaseT connection (on Cisco IP Phones 7811, 7821, and 7861)  and the LAN 1000BaseT connection
                                    (on the Cisco IP Phone 7841).

RJ-45 jack for a second 10/100BaseT compliant connection (on Cisco IP Phones 7811, 7821, and 7861) and the LAN 1000BaseT connection
                                    (on the Cisco IP Phone 7841).

48-volt power connector.

## Network and Computer Port Pinouts

Although both the network and computer (access) ports are used for network connectivity, they serve different purposes and
                              have different port pinouts:

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

You can reduce the amount of energy that the Cisco IP Phone consumes by using Power Save or EnergyWise (Power Save Plus) mode.

In Power Save mode, the backlight on the screen is not lit when the phone is not in use. The phone remains in Power Save mode
                                       for the scheduled duration or until the user lifts the handset or presses any button.

The Cisco IP Phone 7811 does not support Power Save because the phone screen does not have a backlight.

The Cisco IP Phone supports Cisco EnergyWise (Power Save Plus) mode. When your network contains an EnergyWise (EW) controller
                                       (for example, a Cisco switch with the EnergyWise feature enabled), you can configure these phones to sleep (power down) and
                                       wake (power up) on a schedule to further reduce power consumption.

The Cisco IP Phone 7811 does not support Power Save Plus.

Set up each phone to enable or disable the EnergyWise settings. If EnergyWise is enabled, configure a sleep and wake time,
                                       as well as other parameters. These parameters are sent to the phone as part of the phone configuration XML file.

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

CiscoIPPhones support several industry-standard and Cisco
                              		  network protocols that are required for voice communication. The following table
                              		  provides an overview of the network protocols that the 
                              		  phones support.

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

We
                                          					 recommend that you use DHCP custom option 150. With this method, you configure
                                          					 the TFTP server IP address as the option value. For additional supported DHCP
                                          					 configurations, see the documentation for your particular Cisco Unified Communications Manager release.

Cisco
                                          					 Audio Session Tunneling (CAST)

The CAST
                                          					 protocol allows IP phones and associated applications behind the phone to
                                          					 discover and communicate with the remote endpoints without requiring changes to
                                          					 the traditional signaling components like Cisco Unified Communications Manager
                                          					 and gateways. The CAST protocol allows separate hardware devices to synchronize
                                          					 related media and it allows PC applications to augment nonvideo-capable phones
                                          					 to become video enabled using the PC as the video resource.

The Cisco IP Phone uses CAST as an interface between CUVA and Cisco Unified Communications Manager using the Cisco IP Phone
                                          as a SIP proxy.

Cisco
                                          					 Discovery Protocol (CDP)

CDP is a
                                          					 device-discovery protocol that runs on all Cisco-manufactured equipment.

A device can use CDP to advertise its existence to other devices and receive information
                                          					 about other devices in the network.

The Cisco
                                          					 IPPhone uses CDP to communicate information such as auxiliary VLAN ID, per
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

DHCP is
                                          					 enabled by default. If disabled, you must manually configure the IP address,
                                          					 subnet mask, gateway, and a TFTP server on each phone locally.

We
                                          					 recommend that you use DHCP custom option 150. With this method, you configure
                                          					 the TFTP server IP address as the option value. For additional supported DHCP
                                          					 configurations, see the documentation for your particular Cisco Unified Communications Manager release.

If you cannot use option 150, use DHCP option 66.

Hypertext Transfer Protocol (HTTP)

HTTP is
                                          					 the standard protocol for transfer of information and movement of documents across the
                                          					 Internet and the web.

Cisco IP Phones use HTTP for XML services, provisioning, upgrade and for troubleshooting purposes.

Hypertext Transfer Protocol Secure (HTTPS)

Hypertext Transfer Protocol Secure (HTTPS) is a combination of the Hypertext Transfer Protocol with the SSL/TLS protocol to
                                          provide encryption and secure identification of servers.

IP phones can be HTTPS clients; they cannot be HTTPS servers.

Web applications with both HTTP and HTTPS support have two URLs configured. Cisco IP Phones that support HTTPS choose the
                                          HTTPS URL.

A lock icon is displayed to the user if the connection to the service is via HTTPS.

IEEE
                                          					 802.1X

The IEEE
                                          					 802.1X standard defines a client-server-based access control and authentication
                                          					 protocol that restricts unauthorized clients from connection to a LAN through
                                          					 publicly accessible ports.

Until
                                          					 the client is authenticated, 802.1X access control allows only Extensible
                                          					 Authentication Protocol over LAN (EAPOL) traffic through the port to which the
                                          					 client is connected. After authentication is successful, normal traffic can
                                          					 pass through the port.

The
                                          					 Cisco IP Phone implements the IEEE 802.1X standard through support for the
                                          					 following authentication methods: EAP-FAST and EAP-TLS.

When
                                          					 802.1X authentication is enabled on the phone, you should disable the PC port
                                          					 and voice VLAN.

Internet
                                          					 Protocol (IP)

IP is a
                                          					 messaging protocol that addresses and sends packets across the network.

To
                                          					 communicate with IP, network devices must have an assigned IP address, subnet,
                                          					 and gateway.

IP
                                          					 addresses, subnets, and gateways identifications are automatically assigned if
                                          					 you are using the Cisco IPPhone with Dynamic Host Configuration Protocol
                                          					 (DHCP). If you are not using DHCP, you must manually assign these properties to
                                          					 each phone locally.

The
                                          					 Cisco IP Phones support IPv6 address.  For more information, see the documentation for your particular Cisco Unified
                                          Communications Manager release.

Link
                                          					 Layer Discovery Protocol (LLDP)

LLDP is
                                          					 a standardized network discovery protocol (similar to CDP) that is supported on
                                          					 some Cisco and third-party devices.

The
                                          					 Cisco IPPhone supports LLDP on the PC port.

Link
                                          					 Layer Discovery Protocol-Media Endpoint Devices (LLDP-MED)

LLDP-MED
                                          					 is an extension of the LLDP standard developed for voice products.

The
                                          					 Cisco IPPhone supports LLDP-MED on the SW port to communicate information such
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
                                          					 enabled by default.

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

Cisco IP
                                          					 Phones use TCP to connect to Cisco Unified Communications Manager and to access
                                          					 XML services.

Transport Layer Security (TLS)

TLS is a
                                          					 standard protocol for securing and authenticating communications.

When security is implemented, Cisco IP Phones use the TLS protocol when securely registering with the Cisco Unified Communications
                                          Manager. For more information, see the documentation for your particular Cisco Unified Communications Manager release.

Trivial
                                          					 File Transfer Protocol (TFTP)

TFTP
                                          					 allows you to transfer files over the network.

On the
                                          					 Cisco IPPhone, TFTP enables you to obtain a configuration file specific to the
                                          					 phone type.

TFTP
                                          					 requires a TFTP server in your network, which can be automatically identified
                                          					 from the DHCP server. If you want a phone to use a TFTP server other than the
                                          					 one specified by the DHCP server, you must manually assign the IP address of
                                          					 the TFTP server by using the Network Setup menu on the phone.

For more
                                          					 information,  see the documentation for your particular Cisco Unified Communications Manager release.

User
                                          					 Datagram Protocol (UDP)

UDP is a
                                          					 connectionless messaging protocol for delivery of data packets.

UDP is used only for RTP streams. SIP uses UDP, TCP and TLS.

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

## Cisco Unified
                        	 Communications Manager Interaction

Cisco Unified Communications Manager is an open, industry-standard call processing system. Cisco Unified Communications Manager
                           software sets up and tears down calls between phones, integrating traditional PBX functionality with the corporate IP network.
                           Cisco Unified Communications Manager manages the components of the telephony system, such as the phones, the access gateways,
                           and the resources necessary for features such as call conferencing and route planning. Cisco Unified Communications Manager
                           also provides:

Firmware for
                                 			 phones

Certificate Trust List (CTL) and Identity Trust List (ITL) files using the TFTP and HTTP services

Phone
                                 			 registration

Call
                                 			 preservation, so that a media session continues if signaling is lost between
                                 			 the primary Communications Manager and a phone

For information about configuring Cisco Unified Communications Manager to work with the phones described in this chapter,
                           see the documentation for your particular Cisco Unified Communications Manager release.

If the phone model that you want to configure does not appear in the Phone Type drop-down list in Cisco Unified Communications
                                       Manager Administration, install the latest device package for your version of Cisco Unified Communications Manager from Cisco.com.

## Cisco Unified
                        	 Communications Manager Express Interaction

When the Cisco IP
                           		Phone works with the Cisco Unified Communications Manager Express, the phones
                           		must go into CME mode.

When a user invokes
                           		the conference feature, the tag allows the phone to use either a local or
                           		network hardware conference bridge.

The Cisco IP Phones
                           		do not support the following actions:

Only
                                 				supported in the connected call transfer scenario.

Only
                                 				supported in the connected call transfer scenario.

Supported
                                 				using the Conference button or Hookflash access.

Supported
                                 				using the Hold button or Hold softkey.

Not supported.

Not supported.

Not supported.

Users cannot create
                           		conference and transfer calls across different lines.

Unified CME supports intercom calls, also known as whisper paging. But the page is rejected by the phone during calls.

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

Caution

In European Union countries, use only external speakers, microphones, and headsets that are fully compliant with the EMC Directive
                                       [89/336/EC].

## Phone Behavior
                        	 During Times of Network Congestion

Anything that degrades network performance can affect phone audio and, in some cases, can cause a call to drop. Sources of
                              network degradation can include, but are not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan.

Attacks that occur on your network, such as a Denial of Service attack.

## Application Programming Interface

Cisco supports phone API utilization by 3rd party applications that have been tested and certified through Cisco by the 3rd
                              party application developer. Any phone issues related to uncertified application interaction must be addressed by the 3rd
                              party and will not be addressed by Cisco.

For support model of Cisco certified 3rd party applications/solutions, please refer to Cisco Solution Partner Program website for details.

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
                                          					 length between each Cisco IP Phone and the switch is 100meters (330feet). |

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

| Note | The Cisco IP Phone 7811 does not support Power Save Plus. |
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
                                          					 information, such as its IP address. | We
                                          					 recommend that you use DHCP custom option 150. With this method, you configure
                                          					 the TFTP server IP address as the option value. For additional supported DHCP
                                          					 configurations, see the documentation for your particular Cisco Unified Communications Manager release. |
| Cisco
                                          					 Audio Session Tunneling (CAST) | The CAST
                                          					 protocol allows IP phones and associated applications behind the phone to
                                          					 discover and communicate with the remote endpoints without requiring changes to
                                          					 the traditional signaling components like Cisco Unified Communications Manager
                                          					 and gateways. The CAST protocol allows separate hardware devices to synchronize
                                          					 related media and it allows PC applications to augment nonvideo-capable phones
                                          					 to become video enabled using the PC as the video resource. | The Cisco IP Phone uses CAST as an interface between CUVA and Cisco Unified Communications Manager using the Cisco IP Phone
                                          as a SIP proxy. |
| Cisco
                                          					 Discovery Protocol (CDP) | CDP is a
                                          					 device-discovery protocol that runs on all Cisco-manufactured equipment. A device can use CDP to advertise its existence to other devices and receive information
                                          					 about other devices in the network. | The Cisco
                                          					 IPPhone uses CDP to communicate information such as auxiliary VLAN ID, per
                                          					 port power management details, and Quality of Service (QoS) configuration
                                          					 information with the Cisco Catalyst switch. |
| Domain Name Server (DNS) | DNS translates domain names to IP addresses. | Cisco IP Phones have a DNS client to translate domain names into IP addresses. |
| Dynamic
                                          					 Host Configuration Protocol (DHCP) | DHCP
                                          					 dynamically allocates and assigns an IP address to network devices. DHCP
                                          					 enables you to connect an IP phone into the network and have the phone become
                                          					 operational without the need to manually assign an IP address or to
                                          					 configure additional network parameters. | DHCP is
                                          					 enabled by default. If disabled, you must manually configure the IP address,
                                          					 subnet mask, gateway, and a TFTP server on each phone locally. We
                                          					 recommend that you use DHCP custom option 150. With this method, you configure
                                          					 the TFTP server IP address as the option value. For additional supported DHCP
                                          					 configurations, see the documentation for your particular Cisco Unified Communications Manager release. Note If you cannot use option 150, use DHCP option 66. | Note | If you cannot use option 150, use DHCP option 66. |
| Note | If you cannot use option 150, use DHCP option 66. |
| Hypertext Transfer Protocol (HTTP) | HTTP is
                                          					 the standard protocol for transfer of information and movement of documents across the
                                          					 Internet and the web. | Cisco IP Phones use HTTP for XML services, provisioning, upgrade and for troubleshooting purposes. |
| Hypertext Transfer Protocol Secure (HTTPS) | Hypertext Transfer Protocol Secure (HTTPS) is a combination of the Hypertext Transfer Protocol with the SSL/TLS protocol to
                                          provide encryption and secure identification of servers. Note IP phones can be HTTPS clients; they cannot be HTTPS servers. | Note | IP phones can be HTTPS clients; they cannot be HTTPS servers. | Web applications with both HTTP and HTTPS support have two URLs configured. Cisco IP Phones that support HTTPS choose the
                                          HTTPS URL. A lock icon is displayed to the user if the connection to the service is via HTTPS. |
| Note | IP phones can be HTTPS clients; they cannot be HTTPS servers. |
| IEEE
                                          					 802.1X | The IEEE
                                          					 802.1X standard defines a client-server-based access control and authentication
                                          					 protocol that restricts unauthorized clients from connection to a LAN through
                                          					 publicly accessible ports. Until
                                          					 the client is authenticated, 802.1X access control allows only Extensible
                                          					 Authentication Protocol over LAN (EAPOL) traffic through the port to which the
                                          					 client is connected. After authentication is successful, normal traffic can
                                          					 pass through the port. | The
                                          					 Cisco IP Phone implements the IEEE 802.1X standard through support for the
                                          					 following authentication methods: EAP-FAST and EAP-TLS. When
                                          					 802.1X authentication is enabled on the phone, you should disable the PC port
                                          					 and voice VLAN. |
| Internet
                                          					 Protocol (IP) | IP is a
                                          					 messaging protocol that addresses and sends packets across the network. | To
                                          					 communicate with IP, network devices must have an assigned IP address, subnet,
                                          					 and gateway. IP
                                          					 addresses, subnets, and gateways identifications are automatically assigned if
                                          					 you are using the Cisco IPPhone with Dynamic Host Configuration Protocol
                                          					 (DHCP). If you are not using DHCP, you must manually assign these properties to
                                          					 each phone locally. The
                                          					 Cisco IP Phones support IPv6 address.  For more information, see the documentation for your particular Cisco Unified
                                          Communications Manager release. |
| Link
                                          					 Layer Discovery Protocol (LLDP) | LLDP is
                                          					 a standardized network discovery protocol (similar to CDP) that is supported on
                                          					 some Cisco and third-party devices. | The
                                          					 Cisco IPPhone supports LLDP on the PC port. |
| Link
                                          					 Layer Discovery Protocol-Media Endpoint Devices (LLDP-MED) | LLDP-MED
                                          					 is an extension of the LLDP standard developed for voice products. | The
                                          					 Cisco IPPhone supports LLDP-MED on the SW port to communicate information such
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
                                          					 enabled by default. |
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
                                          					 connection-oriented transport protocol. | Cisco IP
                                          					 Phones use TCP to connect to Cisco Unified Communications Manager and to access
                                          					 XML services. |
| Transport Layer Security (TLS) | TLS is a
                                          					 standard protocol for securing and authenticating communications. | When security is implemented, Cisco IP Phones use the TLS protocol when securely registering with the Cisco Unified Communications
                                          Manager. For more information, see the documentation for your particular Cisco Unified Communications Manager release. |
| Trivial
                                          					 File Transfer Protocol (TFTP) | TFTP
                                          					 allows you to transfer files over the network. On the
                                          					 Cisco IPPhone, TFTP enables you to obtain a configuration file specific to the
                                          					 phone type. | TFTP
                                          					 requires a TFTP server in your network, which can be automatically identified
                                          					 from the DHCP server. If you want a phone to use a TFTP server other than the
                                          					 one specified by the DHCP server, you must manually assign the IP address of
                                          					 the TFTP server by using the Network Setup menu on the phone. For more
                                          					 information,  see the documentation for your particular Cisco Unified Communications Manager release. |
| User
                                          					 Datagram Protocol (UDP) | UDP is a
                                          					 connectionless messaging protocol for delivery of data packets. | UDP is used only for RTP streams. SIP uses UDP, TCP and TLS. |

| Note | If you cannot use option 150, use DHCP option 66. |
|---|---|

| Note | IP phones can be HTTPS clients; they cannot be HTTPS servers. |
|---|---|

| Note | If the phone model that you want to configure does not appear in the Phone Type drop-down list in Cisco Unified Communications
                                       Manager Administration, install the latest device package for your version of Cisco Unified Communications Manager from Cisco.com. |
|---|---|

| Caution | In European Union countries, use only external speakers, microphones, and headsets that are fully compliant with the EMC Directive
                                       [89/336/EC]. |
|---|---|