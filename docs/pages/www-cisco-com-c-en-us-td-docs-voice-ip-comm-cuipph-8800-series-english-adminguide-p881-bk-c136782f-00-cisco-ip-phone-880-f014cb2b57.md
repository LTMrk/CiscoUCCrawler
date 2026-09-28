---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-english-adminguide-p881-bk-c136782f-00-cisco-ip-phone-880-f014cb2b57
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/english/adminguide/P881_BK_C136782F_00_cisco-ip-phone-8800_series/P881_BK_C136782F_00_cisco-ip-phone-8811-8841_chapter_01.html
retrieved_at: 2026-08-21T09:48:47.573735+00:00
---

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

# Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

Updated: November 6, 2025

Chapter: Technical Details

## Chapter: Technical Details

# Technical Details

## Physical and
                        	 Operating Environment Specifications

The following
                              		  table shows the physical and operating environment specifications for the Cisco
                              		  IP Phone 8800 Series.

Specification

Value or
                                          					 range

Operating
                                          					 temperature

32° to
                                          					 104°F (0° to 40°C)

Operating
                                          					 relative humidity

Operating:
                                          					 10% to 90% (non-condensing)

Non-operating: 10% to 95% (non-condensing)

Storage
                                          					 temperature

14° to
                                          					 140°F (–10° to 60°C)

Height

9.02 in.
                                          					 (229.1 mm)

Width

10.13 in.
                                          					 (257.34 mm)

Depth

1.57 in.
                                          					 (40 mm)

Weight

2.62 lb
                                          					 (1.19 kg)

Power

100-240
                                          					 VAC, 50-60 Hz, 0.5 A when using the AC adapter

48 VDC,
                                          					 0.2 A when using the in-line power over the network cable

Cables

Category
                                          					 3/5/5e/6 for 10-Mbps cables with 4 pairs

Category
                                          					 5/5e/6 for 100-Mbps cables with 4 pairs

Category
                                          					 5e/6 for 1000-Mbps cables with 4 pairs

Cables
                                                      						have 4 pairs of wires for a total of 8 conductors.

Distance
                                          					 requirements

As
                                          					 supported by the Ethernet Specification, the maximum cable length between each
                                          					 Cisco IP Phone and the switch is assumed to be 330 feet (100 meters).

## Cable Specifications

The following information lists the cable specifications:

RJ-9 jack (4-conductor) for handset and headset connection

RJ-45 jack for the LAN 10/100/1000BaseT connection (10/100/1000 Network port on the phone)

RJ-45 jack for a second 10/100/1000BaseT compliant connection (10/100/1000 Computer port on the phone)

3.5 mm jack for speaker connection (only Cisco IP Phone 8861)

48-volt power connector

USB ports/connector: one USB port for Cisco IP Phone 8851 and two USB ports for Cisco IP Phone 8861

3 key expansion modules connectors which is considered as USB connector for Cisco IP Phone 8851 and 8861

### Network and Computer Port Pinouts

Although both
                              		the network and computer (access) ports are used for network connectivity, they
                              		serve different purposes and have different port pinouts.

The network port
                                    			 is the 10/100/1000 SW port on the Cisco IP Phone.

The computer
                                    			 (access) port is the 10/100/1000 PC port on the Cisco IP Phone.

#### Network Port Connector

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

#### Computer Port Connector

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

The Cisco
                           		IP Phone can be powered with external power or with Power over Ethernet (PoE).
                           		A separate power supply provides external power. The switch can provide PoE
                           		through the phone Ethernet cable.

Cisco IP Phones 8861 and 8865 are PoE Class 4 devices and require a switch or line card with Class 4 capabilities to support
                           extra features.

For more information on your phone's power requirements, consult your phone's data sheet.

When you install a phone that is powered with external power, connect the power supply before you connect the Ethernet cable
                           to the phone. When you remove a phone that is powered with external power, disconnect the Ethernet cable from the phone before
                           you disconnect the power supply.

Power type

Guidelines

External power: Provided through the CP-PWR-CUBE-4= external power supply

The Cisco IP Phone uses the CP-PWR-CUBE-4 power supply.

PoE power—Provided by a switch through the Ethernet cable attached to the phone.

Cisco IP Phones 8851, 8851NR, 8861, 8865, and 8865NR support 802.3at PoE for accessory use. For more information, consult
                                       your phone's data sheet.

The switch requires a backup power supply for uninterruptible operation of the phone

Make sure that the CatOS or IOS version that runs on your switch supports your intended phone deployment. See the documentation
                                       for your switch for operating system version information.

Universal Power over Ethernet (UPoE)

Cisco IP Phones 8865 and 8865NR supports UPoE.

The
                           	 documents in the following table provide more information on the following
                           	 topics:

Cisco switches
                                 		  that work with Cisco IP Phones

Cisco IOS releases
                                 		  that support bidirectional power negotiation

Other requirements
                                 		  and restrictions about power

Document
                                       				  topics

URL

PoE
                                       				  Solutions

http://www.cisco.com/c/en/us/solutions/enterprise-networks/power-over-ethernet-solutions/index.html

UPoE

http://www.cisco.com/c/en/us/solutions/enterprise-networks/upoe/index.html

Cisco
                                       				  Catalyst Switches

http://www.cisco.com/c/en/us/products/switches/index.html

Integrated
                                       				  Service Routers

http://www.cisco.com/c/en/us/products/routers/index.html

Cisco IOS
                                       				  Software

http://www.cisco.com/c/en/us/products/ios-nx-os-software/index.html

### Power Outage

Your access to emergency service through the phone requires that the phone receive power. If a power interruption occurs,
                              service or emergency calling service dialing does not function until power is restored. If a power failure or disruption occurs,
                              you may need to reset or reconfigure the equipment before you can use service or emergency calling service dialing.

### Power Reduction

You can reduce the amount of energy that the Cisco IP Phone consumes by using Power Save or EnergyWise (Power Save Plus) mode.

In Power Save mode, the backlight on the screen is not lit when the phone is not in use. The phone remains in Power Save mode
                                       for the scheduled duration or until the user lifts the handset or presses any button.

The Cisco IP Phone supports Cisco EnergyWise (Power Save Plus) mode. When your network contains an EnergyWise (EW) controller
                                       (for example, a Cisco switch with the EnergyWise feature enabled), you can configure these phones to sleep (power down) and
                                       wake (power up) on a schedule to further reduce power consumption.

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

## Network
                        	 Protocols

Cisco IP Phone 8800 Series support
                              		  several industry-standard and Cisco network protocols required for voice
                              		  communication. The following table provides an overview of the network
                              		  protocols that the phones support.

Network
                                          					 protocol

Purpose

Usage
                                          					 notes

Bluetooth

Bluetooth
                                          					 is a wireless personal area network (WPAN) protocol that specifies how devices
                                          					 communicate over short distances.

Cisco IP Phones 8845, 8865, and 8851 support Bluetooth 4.1.

Cisco IP Phone 8861 support Bluetooth 4.0.

Cisco IP Phone 8811, 8841, 8851NR, and 8865NR do not support Bluetooth.

Bootstrap
                                          					 Protocol (BootP)

BootP
                                          					 enables a network device, such as the Cisco IP Phone, to discover certain
                                          					 startup information, such as the IP address.

—

Cisco Audio Session Tunnel (CAST)

The CAST protocol allows your phones and associated applications to communicate with the remote IP Phones without requiring
                                          changes to the signaling components.

The Cisco IP Phone uses CAST as an interface between CUVA and Cisco Unified Communications Manager using the Cisco IP Phone
                                          as a SIP proxy.

Cisco
                                          					 Discovery Protocol (CDP)

CDP is a
                                          					 device-discovery protocol that runs on all Cisco-manufactured equipment.

Using CDP,
                                          					 a device can advertise its existence to other devices and receive information
                                          					 about other devices in the network.

The Cisco
                                          					 IP Phones use CDP to communicate information such as auxiliary VLAN ID, per
                                          					 port power management details, and Quality of Service (QoS) configuration
                                          					 information with the Cisco Catalyst switch.

Cisco Peer-to-Peer Distribution Protocol (CPPDP)

CPPDP is a Cisco proprietary protocol used to form a peer-to-peer hierarchy of devices. This hierarchy is used to distribute
                                          firmware files from peer devices to their neighboring devices.

CPPDP is used by the Peer Firmware Sharing feature.

Dynamic
                                          					 Host Configuration Protocol (DHCP)

DHCP
                                          					 dynamically allocates and assigns an IP address to network devices.

DHCP
                                          					 enables you to connect an IP phone into the network and the phone to become
                                          					 operational without the need to manually assign an IP address or to configure
                                          					 additional network parameters.

DHCP is enabled by default. If disabled, you must manually configure the IP address, subnet mask, gateway, and a TFTP server
                                          on each phone locally.

We recommend that you use DHCP custom option 150. With this method, you configure the TFTP server IP address as the option
                                          value. For more information, see the documentation for your particular Cisco Unified Communications Manager release.

If you cannot use option 150, you may try using DHCP option 66.

Hypertext
                                          					 Transfer Protocol (HTTP)

HTTP is
                                          					 the standard way of transferring information and moving documents across the
                                          					 Internet and the web.

Cisco IP Phones use HTTP for XML services and for troubleshooting purposes.

Hypertext
                                          					 Transfer Protocol Secure (HTTPS)

Hypertext
                                          					 Transfer Protocol Secure (HTTPS) is a combination of the Hypertext Transfer
                                          					 Protocol with the SSL/TLS protocol to provide encryption and secure
                                          					 identification of servers.

Web
                                          					 applications with both HTTP and HTTPS support have two URLs configured. Cisco
                                          					 IP Phones that support HTTPS choose the HTTPS URL.

IEEE 802.1X

The IEEE 802.1X standard defines a client-server-based access control and authentication protocol that restricts unauthorized
                                          clients from connecting to a LAN through publicly accessible ports.

Until the client is authenticated, 802.1X access control allows only Extensible Authentication Protocol over LAN (EAPOL) traffic
                                          through the port to which the client is connected. After authentication is successful, normal traffic can pass through the
                                          port.

The Cisco IP Phone implements the IEEE 802.1X standard by providing support for the following authentication methods: EAP-FAST,
                                          and EAP-TLS.

When 802.1X authentication is enabled on the phone, you should disable the PC port and voice VLAN.

IEEE
                                          					 802.11n/802.11ac

The IEEE
                                          					 802.11 standard specifies how devices communication over a wireless local area
                                          					 network (WLAN).

802.11n
                                          					 operates at the 2.4 GHz and 5 GHz band and 802.11ac operates at the 5 GHz band.

The
                                          					 802.11 interface is a deployment option for cases when Ethernet cabling is
                                          					 unavailable or undesirable.

Only Cisco IP Phone 8861 and 8865 support WLAN.

Internet
                                          					 Protocol (IP)

IP is a
                                          					 messaging protocol that addresses and sends packets across the network.

To
                                          					 communicate using IP, network devices must have an assigned IP address, subnet,
                                          					 and gateway.

IP
                                          					 addresses, subnets, and gateway identifications are automatically assigned if
                                          					 you are using the Cisco IPPhone with Dynamic Host Configuration Protocol
                                          					 (DHCP). If you are not using DHCP, you must manually assign these properties to
                                          					 each phone locally.

The Cisco IP Phones support IPv6 addresses. For more information, see the documentation for your particular Cisco Unified
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
                                          					 is an extension of the LLDP standard for voice products.

The
                                          					 Cisco IPPhone supports LLDP-MED on the SW port to communicate information such
                                          					 as:

- Voice VLAN configuration

- Device discovery

- Power management

- Inventory management

Real-Time Transport Protocol (RTP)

RTP is a
                                          					 standard protocol for transporting real-time data, such as interactive voice,
                                          					 over data networks.

Cisco IP
                                          					 Phones use the RTP protocol to send and receive real-time voice traffic from
                                          					 other phones and gateways.

Real-Time Control Protocol (RTCP)

RTCP
                                          					 works in conjunction with RTP to provide QoS data (such as jitter, latency, and
                                          					 round-trip delay) on RTP streams.

RTCP is enabled by default.

Session Description Protocol (SDP)

SDP is the portion of the SIP protocol that determines which parameters are available during a connection between two endpoints.
                                          Conferences are established by using only the SDP capabilities that all endpoints in the conference support.

SDP capabilities, such as codec types, DTMF detection, and comfort noise, are normally configured on a global basis by Cisco
                                          Unified Communications Manager or Media Gateway in operation. Some SIP endpoints may allow configuration of these parameters
                                          on the endpoint itself.

Session
                                          					 Initiation Protocol (SIP)

SIP is
                                          					 the Internet Engineering Task Force (IETF) standard for multimedia conferencing
                                          					 over IP. SIP is an ASCII-based application-layer control protocol (defined in
                                          					 RFC 3261) that can be used to establish, maintain, and terminate calls between
                                          					 two or more endpoints.

Like other VoIP protocols, SIP addresses the functions of signaling and session management within a packet telephony network.
                                          Signaling allows transportation of call information across network boundaries. Session management provides the ability to
                                          control the attributes of an end-to-end call.

Cisco IP Phones support the SIP protocol when the phones are operating in IPv6-only, IPv4-only, or in both IPv4 and IPv6.

Transmission Control Protocol (TCP)

TCP is a
                                          					 connection-oriented transport protocol.

Cisco IP Phones use TCP to connect to Cisco Unified Communications Manager and to access XML services.

Transport Layer Security (TLS)

TLS is a
                                          					 standard protocol for securing and authenticating communications.

Upon security implementation, Cisco IP Phones use the TLS protocol when securely registering with Cisco Unified Communications
                                          Manager.

Trivial
                                          					 File Transfer Protocol (TFTP)

TFTP
                                          					 allows you to transfer files over the network.

On the
                                          					 Cisco IPPhone, TFTP enables you to obtain a configuration file specific to the
                                          					 phone type.

TFTP requires a TFTP server in your network that the DHCP server can automatically identify. If you want a phone to use a
                                          TFTP server other than the one that the DHCP server specifies, you must manually assign the IP address of the TFTP server
                                          by using the Network Configuration menu on the phone.

For more information, see the documentation for your particular Cisco Unified Communications Manager release.

User
                                          					 Datagram Protocol (UDP)

UDP is a
                                          					 connectionless messaging protocol for delivery of data packets.

UDP is
                                          					 used only for RTP streams. SIP signaling on the phones do not support UDP.

For more information about LLDP-MED support, see the LLDP-MED and Cisco Discovery
                              				Protocol white paper:

http://www.cisco.com/en/US/tech/tk652/tk701/technologies_white_paper0900aecd804cd46d.shtml

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

When your phone works with the Cisco Unified Communications Manager Express (Unified CME), it must go into CME mode.

When a user invokes the conference feature, the tag allows the phone to
                           		use either a local or network hardware conference bridge.

The phones do not support the following actions:

Transfer—Only supported in the connected call transfer scenario.

Conference—Only supported in the connected call transfer scenario.

Join—Supported using the Conference button or hookflash access.

Hold—Supported using the Hold button.

Barge and Merge—Not supported.

Direct Transfer—Not supported.

Select—Not supported.

The users cannot create conference and transfer calls across different
                           		lines.

Unified CME supports intercom calls, also known as whisper paging. But the page is rejected by the phone during calls.

Both Session line mode and Enhanced line mode are supported in CME mode.

## Voice Messaging System Interaction

Cisco Unified Communications Manager lets you integrate with different voice messaging systems, including the Cisco Unity
                           Connection voice messaging system. Because you can integrate with various systems, you must provide users with information
                           about how to use your specific system.

To enable the ability for a user to transfer to voicemail, set up a *xxxxx dialing pattern and configure it as Call Forward
                           All to Voicemail. For more information, see the Cisco Unified Communications Manager documentation.

Provide the following information to each user:

How to access
                                 			 the voice messaging system account.

Make sure that
                                 			 you have used the Cisco Unified Communications Manager to configure the Messages
                                 			 button on the Cisco IP Phone.

Initial password
                                 			 for accessing the voice messaging system.

Configure a default voice messaging system password for all users.

How the phone
                                 			 indicates that voice messages are waiting.

Use Cisco Unified Communications Manager to set up a message waiting indicator (MWI) method.

## Phone Startup
                        	 Overview

When
                              		  connecting to the VoIP network, the Cisco IP Phones goes through a standard
                              		  startup process. Depending on your specific network configuration, only some of
                              		  these steps may occur on your Cisco IP Phone.

Obtain power
                                    				from the switch. If a phone is not using external power, the switch provides
                                    				inline power through the Ethernet cable that is attached to the phone.

(For the Cisco IP Phone 8861 and 8865 in a wireless LAN only) Scan for an access point. The Cisco IP Phone 8861 and 8865 scans
                                    the RF coverage area with the radio. The phone searches the network profiles and scans for access points that contain a matching
                                    SSID and authentication type. The phone associates with the access point with the highest RSSI that matches with the network
                                    profile.

(For the Cisco IP Phone 8861 and 8865 in a wireless LAN only) Authenticate with the access point. The Cisco IP Phone begins
                                    the authentication process. The following table describes the authentication process:

Authentication type

Key
                                                							 management options

Description

Open

None

Any
                                                							 device can authenticate to the access point. For added security, static WEP
                                                							 encryption might optionally be used.

Shared Key

None

The
                                                							 phone encrypts the challenge text by using the WEP key and the access point
                                                							 must verify the WEP key that was used to encrypt the challenge text before
                                                							 network access is available.

PEAP
                                                							 or EAP-FAST

None

The
                                                							 RADIUS server authenticates the username and password before network access is
                                                							 available.

Load the
                                    				stored phone image. At startup, the phone runs a bootstrap loader that loads a
                                    				phone firmware image that is stored in flash memory. Using this image, the
                                    				phone initializes the software and hardware.

Configure the
                                    				VLAN. If the Cisco IP Phone is connected to a Cisco Catalyst switch, the switch
                                    				next informs the phone of the voice VLAN that is defined on the switch. The
                                    				phone needs to know the VLAN membership before it can proceed with the Dynamic
                                    				Host Configuration Protocol (DHCP) request for an IP address.

Obtain an IP
                                    				address. If the Cisco IP Phone is using DHCP to obtain an IP address, the phone
                                    				queries the DHCP server to obtain one. If you are not using DHCP in your
                                    				network, you must assign static IP addresses to each phone locally.

Request the
                                    				CTL file. The TFTP server stores the CTL file. This file contains the
                                    				certificates that are necessary for establishing a secure connection between
                                    				the phone and Cisco Unified Communications Manager.

For more
                                    				information, the documentation for your particular Cisco Unified Communications Manager release.

Request the
                                    				ITL file. The phone requests the ITL file after it requests the CTL file. The
                                    				ITL file contains the certificates of the entities that the phone can trust.
                                    				The certificates are used to authenticate a secure connection with the servers
                                    				or to authenticate a digital signature signed by the servers. Cisco Unified
                                    				Communications Manager 8.5 and later supports the ITL file.

Access a TFTP
                                    				server. In addition to assigning an IP address, the DHCP server directs the
                                    				Cisco IP Phone to a TFTP Server. If the phone has a statically defined IP
                                    				address, you must configure the TFTP server locally on the phone; the phone
                                    				then contacts the TFTP server directly.

You can also
                                                				  assign an alternate TFTP server to use instead of the one that DHCP assigns.

Request the
                                    				configuration file. The TFTP server has configuration files, which define
                                    				parameters for connecting to Cisco Unified Communications Manager and other
                                    				information for the phone.

Contact Cisco
                                    				Unified Communications Manager. The configuration file defines how the Cisco IP
                                    				Phone communicates with Cisco Unified Communications Manager and provides a
                                    				phone with the load ID. After it obtains the file from the TFTP server, the
                                    				phone attempts to make a connection to the highest priority Cisco Unified
                                    				Communications Manager on the list.

If the
                                    				security profile of the phone is configured for secure signaling (encrypted or
                                    				authenticated) and the Cisco Unified Communications Manager is set to secure
                                    				mode, the phone makes a TLS connection. Otherwise, the phone makes a nonsecure
                                    				TCP connection.

If the phone
                                    				was manually added to the database, Cisco Unified Communications Manager
                                    				identifies the phone. If the phone was not manually added to the database and
                                    				autoregistration is enabled in Cisco Unified Communications Manager, the phone
                                    				attempts to autoregister itself in the Cisco Unified Communications Manager
                                    				database.

Autoregistration is disabled when you configure the CTL client.
                                                				  In this case, you must add the phone to the Cisco Unified Communications
                                                				  Manager database manually.

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

## USB Port
                        	 Information

The Cisco IP Phones 8851, 8851NR, 8861, 8865, and 8865NR support a maximum of five devices that connect to each USB port.
                              Each device that connects to the phone is included in the maximum device count. For example, your phone can support five USB
                              devices on the side port and five more standard USB devices on the back port. Many third-party USB products count as multiple
                              USB devices; for example, a device containing a USB hub and headset can count as two USB devices. For more information, see
                              the USB device documentation.

Unpowered hubs are not supported, and powered hubs with more
                                                				  than four ports are not supported.

USB headsets that connect to the phone through a USB hub are not
                                                				  supported.

Each key expansion module connects to the phone counts as a USB device. If three key expansion modules are connected to the
                              phone, these count as three USB devices.

## Phone
                        	 Configuration Files

Configuration files for a phone are stored on the TFTP server
                           		and define parameters for connecting to Cisco Unified
                              				Communications Manager . In general, any time you make a
                           		change in Cisco Unified
                              				Communications Manager that requires the phone to be reset,
                           		a change is automatically made to the phone configuration file.

Configuration files also contain information about which image
                           		load the phone should be running. If this image load differs from the one
                           		currently loaded on a phone, the phone contacts the TFTP server to request the
                           		required load files.

If you
                           		configure security-related settings in Cisco Unified
                              				Communications Manager Administration , the phone configuration file will
                           		contain sensitive information. To ensure the privacy of a configuration file,
                           		you must configure it for encryption. For more information, see the documentation for your particular Cisco Unified Communications
                           Manager release. A phone
                           		requests a configuration file whenever it resets and registers with Cisco Unified
                              				Communications Manager .

A phone
                           		accesses a default configuration file named XmlDefault.cnf.xml from the TFTP
                           		server when the following conditions exist:

You have enabled
                                 			 autoregistration in Cisco Unified
                                    				Communications Manager

The phone has
                                 			 not been added to the Cisco Unified
                                    				Communications Manager database

The phone is
                                 			 registering for the first time

## Phone Behavior
                        	 During Times of Network Congestion

Anything that degrades network performance can affect phone audio and video quality, and in some cases, can cause a call to
                              drop. Sources of network degradation can include, but are not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan.

Attacks that occur on your network, such as a Denial of Service attack.

## Phone Behavior on a Network with Two Network Routers

The Cisco IP Phone 8800 Series uses a firewall to provide protection against cyber intrusions, such as a man-in-the-middle
                              attack. This firewall cannot be disabled. But it could stop traffic on a phone, if you configure your network with two network
                              routers in the same subnet and with IP redirect.

The phone firewall stops traffic because this network setup is similar to a man-in-the-middle attack. The phone receives redirect
                              packets for different destination IPs in a different subnet from the phone. The phone is on a network with more than one router,
                              and the default router sends traffic to a second router.

```
sip_tcp_create_connection: socket connect failed cpr_errno: 1.
```

A network with  two network routers in the same subnet and with  IP redirect is not a common configuration. If you are using
                              this network setup, consider using only one router  on a subnet. But if you require  two network routers on the same subnet,
                              disable IP Redirect on the router  and reboot the phone.

## Application Programming Interface

Cisco supports phone API utilization by 3rd party applications that have been tested and certified through Cisco by the 3rd
                              party application developer. Any phone issues related to uncertified application interaction must be addressed by the 3rd
                              party and will not be addressed by Cisco.

For support model of Cisco certified 3rd party applications/solutions, please refer to Cisco Solution Partner Program website for details.

| Specification | Value or
                                          					 range |
|---|---|
| Operating
                                          					 temperature | 32° to
                                          					 104°F (0° to 40°C) |
| Operating
                                          					 relative humidity | Operating:
                                          					 10% to 90% (non-condensing) Non-operating: 10% to 95% (non-condensing) |
| Storage
                                          					 temperature | 14° to
                                          					 140°F (–10° to 60°C) |
| Height | 9.02 in.
                                          					 (229.1 mm) |
| Width | 10.13 in.
                                          					 (257.34 mm) |
| Depth | 1.57 in.
                                          					 (40 mm) |
| Weight | 2.62 lb
                                          					 (1.19 kg) |
| Power | 100-240
                                          					 VAC, 50-60 Hz, 0.5 A when using the AC adapter 48 VDC,
                                          					 0.2 A when using the in-line power over the network cable |
| Cables | Category
                                          					 3/5/5e/6 for 10-Mbps cables with 4 pairs Category
                                          					 5/5e/6 for 100-Mbps cables with 4 pairs Category
                                          					 5e/6 for 1000-Mbps cables with 4 pairs Note Cables
                                                      						have 4 pairs of wires for a total of 8 conductors. | Note | Cables
                                                      						have 4 pairs of wires for a total of 8 conductors. |
| Note | Cables
                                                      						have 4 pairs of wires for a total of 8 conductors. |
| Distance
                                          					 requirements | As
                                          					 supported by the Ethernet Specification, the maximum cable length between each
                                          					 Cisco IP Phone and the switch is assumed to be 330 feet (100 meters). |

| Note | Cables
                                                      						have 4 pairs of wires for a total of 8 conductors. |
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

| Power type | Guidelines |
|---|---|
| External power: Provided through the CP-PWR-CUBE-4= external power supply | The Cisco IP Phone uses the CP-PWR-CUBE-4 power supply. |
| PoE power—Provided by a switch through the Ethernet cable attached to the phone. | Cisco IP Phones 8851, 8851NR, 8861, 8865, and 8865NR support 802.3at PoE for accessory use. For more information, consult
                                       your phone's data sheet. The switch requires a backup power supply for uninterruptible operation of the phone Make sure that the CatOS or IOS version that runs on your switch supports your intended phone deployment. See the documentation
                                       for your switch for operating system version information. |
| Universal Power over Ethernet (UPoE) | Cisco IP Phones 8865 and 8865NR supports UPoE. |

| Document
                                       				  topics | URL |
|---|---|
| PoE
                                       				  Solutions | http://www.cisco.com/c/en/us/solutions/enterprise-networks/power-over-ethernet-solutions/index.html |
| UPoE | http://www.cisco.com/c/en/us/solutions/enterprise-networks/upoe/index.html |
| Cisco
                                       				  Catalyst Switches | http://www.cisco.com/c/en/us/products/switches/index.html |
| Integrated
                                       				  Service Routers | http://www.cisco.com/c/en/us/products/routers/index.html |
| Cisco IOS
                                       				  Software | http://www.cisco.com/c/en/us/products/ios-nx-os-software/index.html |

| Note | When CDP and Power Negotiation are disabled, the phone can power the accessories up to 15.4W. |
|---|---|

| Network
                                          					 protocol | Purpose | Usage
                                          					 notes |
|---|---|---|
| Bluetooth | Bluetooth
                                          					 is a wireless personal area network (WPAN) protocol that specifies how devices
                                          					 communicate over short distances. | Cisco IP Phones 8845, 8865, and 8851 support Bluetooth 4.1. Cisco IP Phone 8861 support Bluetooth 4.0. Cisco IP Phone 8811, 8841, 8851NR, and 8865NR do not support Bluetooth. |
| Bootstrap
                                          					 Protocol (BootP) | BootP
                                          					 enables a network device, such as the Cisco IP Phone, to discover certain
                                          					 startup information, such as the IP address. | — |
| Cisco Audio Session Tunnel (CAST) | The CAST protocol allows your phones and associated applications to communicate with the remote IP Phones without requiring
                                          changes to the signaling components. | The Cisco IP Phone uses CAST as an interface between CUVA and Cisco Unified Communications Manager using the Cisco IP Phone
                                          as a SIP proxy. |
| Cisco
                                          					 Discovery Protocol (CDP) | CDP is a
                                          					 device-discovery protocol that runs on all Cisco-manufactured equipment. Using CDP,
                                          					 a device can advertise its existence to other devices and receive information
                                          					 about other devices in the network. | The Cisco
                                          					 IP Phones use CDP to communicate information such as auxiliary VLAN ID, per
                                          					 port power management details, and Quality of Service (QoS) configuration
                                          					 information with the Cisco Catalyst switch. |
| Cisco Peer-to-Peer Distribution Protocol (CPPDP) | CPPDP is a Cisco proprietary protocol used to form a peer-to-peer hierarchy of devices. This hierarchy is used to distribute
                                          firmware files from peer devices to their neighboring devices. | CPPDP is used by the Peer Firmware Sharing feature. |
| Dynamic
                                          					 Host Configuration Protocol (DHCP) | DHCP
                                          					 dynamically allocates and assigns an IP address to network devices. DHCP
                                          					 enables you to connect an IP phone into the network and the phone to become
                                          					 operational without the need to manually assign an IP address or to configure
                                          					 additional network parameters. | DHCP is enabled by default. If disabled, you must manually configure the IP address, subnet mask, gateway, and a TFTP server
                                          on each phone locally. We recommend that you use DHCP custom option 150. With this method, you configure the TFTP server IP address as the option
                                          value. For more information, see the documentation for your particular Cisco Unified Communications Manager release. Note If you cannot use option 150, you may try using DHCP option 66. | Note | If you cannot use option 150, you may try using DHCP option 66. |
| Note | If you cannot use option 150, you may try using DHCP option 66. |
| Hypertext
                                          					 Transfer Protocol (HTTP) | HTTP is
                                          					 the standard way of transferring information and moving documents across the
                                          					 Internet and the web. | Cisco IP Phones use HTTP for XML services and for troubleshooting purposes. |
| Hypertext
                                          					 Transfer Protocol Secure (HTTPS) | Hypertext
                                          					 Transfer Protocol Secure (HTTPS) is a combination of the Hypertext Transfer
                                          					 Protocol with the SSL/TLS protocol to provide encryption and secure
                                          					 identification of servers. | Web
                                          					 applications with both HTTP and HTTPS support have two URLs configured. Cisco
                                          					 IP Phones that support HTTPS choose the HTTPS URL. |
| IEEE 802.1X | The IEEE 802.1X standard defines a client-server-based access control and authentication protocol that restricts unauthorized
                                          clients from connecting to a LAN through publicly accessible ports. Until the client is authenticated, 802.1X access control allows only Extensible Authentication Protocol over LAN (EAPOL) traffic
                                          through the port to which the client is connected. After authentication is successful, normal traffic can pass through the
                                          port. | The Cisco IP Phone implements the IEEE 802.1X standard by providing support for the following authentication methods: EAP-FAST,
                                          and EAP-TLS. When 802.1X authentication is enabled on the phone, you should disable the PC port and voice VLAN. |
| IEEE
                                          					 802.11n/802.11ac | The IEEE
                                          					 802.11 standard specifies how devices communication over a wireless local area
                                          					 network (WLAN). 802.11n
                                          					 operates at the 2.4 GHz and 5 GHz band and 802.11ac operates at the 5 GHz band. | The
                                          					 802.11 interface is a deployment option for cases when Ethernet cabling is
                                          					 unavailable or undesirable. Only Cisco IP Phone 8861 and 8865 support WLAN. |
| Internet
                                          					 Protocol (IP) | IP is a
                                          					 messaging protocol that addresses and sends packets across the network. | To
                                          					 communicate using IP, network devices must have an assigned IP address, subnet,
                                          					 and gateway. IP
                                          					 addresses, subnets, and gateway identifications are automatically assigned if
                                          					 you are using the Cisco IPPhone with Dynamic Host Configuration Protocol
                                          					 (DHCP). If you are not using DHCP, you must manually assign these properties to
                                          					 each phone locally. The Cisco IP Phones support IPv6 addresses. For more information, see the documentation for your particular Cisco Unified
                                          Communications Manager release. |
| Link
                                          					 Layer Discovery Protocol (LLDP) | LLDP is
                                          					 a standardized network discovery protocol (similar to CDP) that is supported on
                                          					 some Cisco and third-party devices. | The
                                          					 Cisco IPPhone supports LLDP on the PC port. |
| Link
                                          					 Layer Discovery Protocol-Media Endpoint Devices (LLDP-MED) | LLDP-MED
                                          					 is an extension of the LLDP standard for voice products. | The
                                          					 Cisco IPPhone supports LLDP-MED on the SW port to communicate information such
                                          					 as: Voice VLAN configuration Device discovery Power management Inventory management |
| Real-Time Transport Protocol (RTP) | RTP is a
                                          					 standard protocol for transporting real-time data, such as interactive voice,
                                          					 over data networks. | Cisco IP
                                          					 Phones use the RTP protocol to send and receive real-time voice traffic from
                                          					 other phones and gateways. |
| Real-Time Control Protocol (RTCP) | RTCP
                                          					 works in conjunction with RTP to provide QoS data (such as jitter, latency, and
                                          					 round-trip delay) on RTP streams. | RTCP is enabled by default. |
| Session Description Protocol (SDP) | SDP is the portion of the SIP protocol that determines which parameters are available during a connection between two endpoints.
                                          Conferences are established by using only the SDP capabilities that all endpoints in the conference support. | SDP capabilities, such as codec types, DTMF detection, and comfort noise, are normally configured on a global basis by Cisco
                                          Unified Communications Manager or Media Gateway in operation. Some SIP endpoints may allow configuration of these parameters
                                          on the endpoint itself. |
| Session
                                          					 Initiation Protocol (SIP) | SIP is
                                          					 the Internet Engineering Task Force (IETF) standard for multimedia conferencing
                                          					 over IP. SIP is an ASCII-based application-layer control protocol (defined in
                                          					 RFC 3261) that can be used to establish, maintain, and terminate calls between
                                          					 two or more endpoints. | Like other VoIP protocols, SIP addresses the functions of signaling and session management within a packet telephony network.
                                          Signaling allows transportation of call information across network boundaries. Session management provides the ability to
                                          control the attributes of an end-to-end call. Cisco IP Phones support the SIP protocol when the phones are operating in IPv6-only, IPv4-only, or in both IPv4 and IPv6. |
| Transmission Control Protocol (TCP) | TCP is a
                                          					 connection-oriented transport protocol. | Cisco IP Phones use TCP to connect to Cisco Unified Communications Manager and to access XML services. |
| Transport Layer Security (TLS) | TLS is a
                                          					 standard protocol for securing and authenticating communications. | Upon security implementation, Cisco IP Phones use the TLS protocol when securely registering with Cisco Unified Communications
                                          Manager. |
| Trivial
                                          					 File Transfer Protocol (TFTP) | TFTP
                                          					 allows you to transfer files over the network. On the
                                          					 Cisco IPPhone, TFTP enables you to obtain a configuration file specific to the
                                          					 phone type. | TFTP requires a TFTP server in your network that the DHCP server can automatically identify. If you want a phone to use a
                                          TFTP server other than the one that the DHCP server specifies, you must manually assign the IP address of the TFTP server
                                          by using the Network Configuration menu on the phone. For more information, see the documentation for your particular Cisco Unified Communications Manager release. |
| User
                                          					 Datagram Protocol (UDP) | UDP is a
                                          					 connectionless messaging protocol for delivery of data packets. | UDP is
                                          					 used only for RTP streams. SIP signaling on the phones do not support UDP. |

| Note | If you cannot use option 150, you may try using DHCP option 66. |
|---|---|

| Note | If the phone model that you want to configure does not appear in the Phone Type drop-down list in Cisco Unified Communications
                                       Manager Administration, install the latest device package for your version of Cisco Unified Communications Manager from Cisco.com. |
|---|---|

| Authentication type | Key
                                                							 management options | Description |
|---|---|---|
| Open | None | Any
                                                							 device can authenticate to the access point. For added security, static WEP
                                                							 encryption might optionally be used. |
| Shared Key | None | The
                                                							 phone encrypts the challenge text by using the WEP key and the access point
                                                							 must verify the WEP key that was used to encrypt the challenge text before
                                                							 network access is available. |
| PEAP
                                                							 or EAP-FAST | None | The
                                                							 RADIUS server authenticates the username and password before network access is
                                                							 available. |

| Note | You can also
                                                				  assign an alternate TFTP server to use instead of the one that DHCP assigns. |
|---|---|

| Note | Autoregistration is disabled when you configure the CTL client.
                                                				  In this case, you must add the phone to the Cisco Unified Communications
                                                				  Manager database manually. |
|---|---|

| Caution | In European Union countries, use only external speakers, microphones, and headsets that are fully compliant with the EMC Directive
                                       [89/336/EC]. |
|---|---|

| Note | Unpowered hubs are not supported, and powered hubs with more
                                                				  than four ports are not supported. USB headsets that connect to the phone through a USB hub are not
                                                				  supported. |
|---|---|