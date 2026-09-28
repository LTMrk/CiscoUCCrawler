---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-6901-6911-10-0-english-admin-guide-p691-bk-af85a164-00-admin-guide-69-d74316b0a9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/6901_6911/10_0/english/admin_guide/P691_BK_AF85A164_00_admin-guide-6901-6911-10_0/P691_BK_AF85A164_00_admin-guide-6901-6911-10_0_chapter_01.html
retrieved_at: 2026-08-21T14:27:15.993851+00:00
---

Cisco Unified IP Phone 6901 and 6911 Administration Guide for Cisco Unified Communications Manager 10.0 (SCCP and SIP)

# Cisco Unified IP Phone 6901 and 6911 Administration Guide for Cisco Unified Communications Manager 10.0 (SCCP and SIP)

Updated: May 9, 2025

Chapter: Cisco Unified IP Phone

## Chapter: Cisco Unified IP Phone

# Cisco Unified IP Phone

## Phone Overview

The Cisco Unified IP Phone 6901 and 6911 provides voice communication over an Internet Protocol (IP) network. The Cisco Unified
                           IP Phone functions much like a digital business phone, allowing you to place and receive phone calls. The Cisco Unified IP
                           Phones in this guide have the following attributes:

Cisco Unified IP Phone 6901 supports basic features such as hold, redial, transfer, and conference.

Cisco Unified IP Phone 6911 supports advanced features such as mute, hold, transfer, conference, speed dial, call forward,
                                 and more.

A Cisco Unified IP Phone, like other network devices, must be configured and managed. These phones encode G.711a, G.711mu,
                           G.729a,  G.729ab, and iLBC codecs, and decode G.711a, G.711mu, G.729, G.729ab, and iLBC codecs. These phones encode and decode
                           the codecs in similar manner.

Caution

Using a cell, mobile, or GSM phone, or two-way radio in close proximity to a Cisco Unified IP Phone might cause interference.
                                       For more information, refer to the manufacturer’s documentation of the interfering device.

For more information, see the Cisco Unified IP Phone 6901 and 6911 User Guide for Cisco Unified Communications Manager (SCCP and SIP) .

## Cisco Unified IP Phone 6901

The following sections describe the Cisco Unified IP Phone 6901 hardware.

### Phone Connections

For your phone to work, it must be connected to the corporate
                                 		  IP telephony network.

1

Slot for Ethernet cable.

4

Network port (10/100 SW) connection. IEEE 802.3af power enabled.

Handset connection.

5

DC adaptor port (DC48V).

Slot for handset cable.

Slot for DC adaptor cable.

In the EU and UK, your phone is shipped with a power switch cable that is required in order to provide power to your phone
                                             when using an AC-to-DC power supply. Connect the power cord to the power switch cable and then connect the other end of the
                                             power switch cable to the DC adapter port.

### Buttons and Hardware

1

Hookswitch

Activates the features (hookflash) on your phone.

2

Places a connected call on hold.

3

Dials the last dialed number.

4

Allows you to pick up a second incoming call. The Line
                                             						button LED indicates the call status.

Allows you to answer a ringing call and swap between two
                                             						calls on the same line. Also, you can use the line button to create a new call
                                             						when the phone is idle. The LED associated with the line button lights up to
                                             						reflect the line status.

Color LEDs indicate the line state:

- Green,
                                                						  steady—Active call

- Green,
                                                						  flashing—Held call

- Amber,
                                                						  Flashing—Incoming call

- Amber,
                                                						  steady—Call Forward All activated

- Red,
                                                						  steady—Remote line in use (shared line)

- Red,
                                                						  flashing—Remote line on hold

5

Controls the handset (off hook) and the ringer volume (on hook).

6

Keypad

Allows you to dial phone numbers.

7

Handset with light strip

Lights up to indicate a ringing call (flashing red) or a new
                                             						voice message (steadyred).

### Hookswitch Button

The cradle rest of your phone contains the hookswitch button. You can press and quickly release the hookswitch button to activate
                                 		  features (hookflash) on your phone.

## Cisco Unified IP Phone 6911

The following sections describe the Cisco Unified IP Phone 6901 hardware.

### Phone Connections

For your phone to work, it must be connected to the corporate
                                 		  IP telephony network.

1

DC adaptor port (DC48V).

4

Network port (10/100 SW) connection. IEEE 802.3af power enabled.

2

AC-to-DC power supply (optional).

5

Access port (10/100 PC) connection.

3

AC power wall plug (optional).

6

Handset connection.

### Buttons and Hardware

1

Handset with light strip

Lights up to indicate a ringing call (flashing red) or a new
                                             						voice message (steady red).

2

Paper label

A paper strip used to enter name and contact numbers.

3

Transfers a call.

4

Creates a conference call.

5

Places an active call on hold.

6

Allows you to pick up a second incoming call and to resume
                                             						a held call. The LED shows call status.

7

Selects the speakerphone as the default audio path and
                                             						initiates a new call, picks up an incoming call, or ends a call. During a call,
                                             						the button lights green. The speakerphone audio path does not change until 
                                             						you select a new audio path (for example, by picking up the handset).

8

Keypad

Allows you to dial phone numbers.

9

Toggles the microphone on or off. When the microphone is
                                             						muted, the button lights red.

10

Controls the handset and speakerphone volume (off hook) and
                                             						the ringer volume (on hook).

11

Messages button

Auto dials your voice messaging system.

12

Dials the last dialed number.

13

Depending on the
                                             						phone setup, the feature button provides you with access to Speed Dial, Call Forward
                                             						All, Pickup, Group Pickup and Meet Me features. You can configure up to nine
                                             						items on the feature button. To access these features, press the feature button
                                             						followed by the number associated with the feature. You must press the feature
                                             						button and the number within five seconds of each other. The number can only be
                                             						a single digit number from 1–9.

- Call Forward
                                                   						  All—Allows you to forward a call.

- Pickup—Allows
                                                   						  you to pickup a call on the third party phone.

- Group
                                                   						  Pickup—Allows you pick up a call within a group.

- Meet Me—Allows
                                                   						  you setup a conference.

14

Handset

Phone handset.

### Paper Label

Cisco Unified IP Phone 6911 does not include an LCD display.
                                 		  Cisco provides a paper strip, which can be used to enter name and contact numbers.

### Clean your phone screen

If your phone screen gets dirty, wipe it with a soft, dry cloth.

Caution

Don't use any liquids or powders on the phone because they can contaminate the phone components and cause failures.

## General Phone Information

This section contains information that is
                           		common to all the IP Phone models in this guide.

### Footstand

If the phone is placed on a table or desk, the footstand can
                                 		  be connected to the back of your phone for a higher or lower viewing angle,
                                 		  depending on your preference.

1

Insert the connectors into the lower slots.

2

Lift the footstand until the connectors snap into the upper
                                             									slots.

Phone Display Angle

### Raise Phone Angle

Connect the footstand to the lower slots for a higher viewing
                                          			 angle, as shown in the following figure.

### Lower Phone Angle

Connect the footstand to the upper slots for a lower viewing
                                          			 angle, as shown in the following figure.

### Important Headset Safety Information

High Sound Pressure—Avoid listening to high volume levels for long periods to prevent possible hearing damage.

When you plug in your headset, lower the volume of the headset speaker before you put the headset on. If you remember to lower
                              the volume before you take the headset off, the volume will start lower when you plug in your headset again.

Be aware of your surroundings. When you use your headset, it may block out important external sounds, particularly in emergencies
                              or in noisy environments. Don’t use the headset while driving. Don’t leave your headset or headset cables in an area where
                              people or pets can trip over them. Always supervise children who are near your headset or headset cables.

## Network Protocols

CiscoUnifiedIPPhones support several industry-standard and
                              		  Cisco network protocols required for voice communication. The following
                              		  table provides an overview of the network protocols that the Cisco Unified IP Phone 6901 and 6911 support.

Network Protocol

Purpose

Usage notes

Cisco Audio Session Tunneling (CAST)

(Cisco Unified IP Phone 6911 only)

The CAST protocol allows IP Phones and associated applications
                                          					 behind the phone to discover and communicate with the remote endpoints without
                                          					 requiring changes to the traditional signaling components like Cisco Unified
                                          					 Communications Manager and gateways. The CAST protocol allows separate hardware
                                          					 devices to synchronize related media and it allows PC applications to augment
                                          					 nonvideo-capable phones to become video enabled by using the PC as the video
                                          					 resource.

-

Cisco Discovery Protocol (CDP)

CDP is a device-discovery protocol that runs on all
                                          					 Cisco-manufactured equipment.

Using CDP, a device advertises its existence to other devices
                                          					 and receives information about other devices in the network.

The Cisco UnifiedIPPhone uses CDP to communicate information
                                          					 such as auxiliary VLAN ID, per port power management details, and Quality of
                                          					 Service (QoS) configuration information with the Cisco Catalyst switch.

Dynamic Host Configuration Protocol (DHCP)

DHCP dynamically allocates and assigns an IP address to
                                          					 network devices.

DHCP enables you to connect an IP Phone into the network and
                                          					 have the phone become operational without needing to manually assign an IP
                                          					 address or to configure additional network parameters.

By default, the phone has DHCP enabled. If disabled, you must manually
                                          					 configure the IP address, subnet mask, gateway, and a TFTP server on each phone
                                          					 locally.

Cisco recommends that you use DHCP custom option 150. With
                                          					 this method, you configure the TFTP server IP address as the option value. For
                                          					 additional supported DHCP configurations, go to the "Dynamic Host Configuration Protocol" chapter and
                                          					 the "CiscoTFTP" chapter in the Cisco Unified Communications Manager System Guide .

If you cannot use option 150, you may try using DHCP option
                                                      						66.

Hypertext Transfer Protocol (HTTP)

HTTP is the standard way of transferring information and
                                          					 moving documents across the Internet and the web.

Cisco UnifiedIP Phones use HTTP for troubleshooting purposes.

IEEE 802.1X

The IEEE 802.1X standard defines a client-server-based access
                                          					 control and authentication protocol that restricts unauthorized clients from
                                          					 connecting to a LAN through publicly accessible ports.

Until the client is authenticated, 802.1X access control
                                          					 allows only Extensible Authentication Protocol over LAN (EAPOL) traffic through
                                          					 the port to which the client connects. After successful authentication,
                                          					 normal traffic passes through the port.

The Cisco Unified IP Phone implements the IEEE 802.1X standard
                                          					 by providing support for the following authentication methods: EAP-FAST and
                                          					 EAP-TLS.

When 802.1X authentication is enabled on the phone, you should
                                          					 disable the voice VLAN. Refer to the 802.1X Authentication for additional information.

Internet Protocol (IP)

IP is a messaging protocol that addresses and sends packets
                                          					 across the network.

To communicate using IP, network devices must have an assigned
                                          					 IP address, subnet, and gateway.

IP addresses, subnets, and gateways  are
                                          					 automatically assigned if you are using the Cisco UnifiedIPPhone with Dynamic
                                          					 Host Configuration Protocol (DHCP). If you are not using DHCP, you must
                                          					 manually assign these properties to each phone locally.

The Cisco Unified IP Phones support IPv6 address. For more
                                          					 information, see "Internet Protocol Version 6 (IPv6)" in the Cisco Unified Communications Manager Features and
                                             						Services Guide .

Link Layer Discovery Protocol (LLDP)

( Cisco Unified IP Phone 6911 only)

LLDP is a standardized network discovery protocol (similar to
                                          					 CDP) that is supported on some Cisco and third-party devices.

The Cisco UnifiedIPPhone 6911 supports LLDP on the switch and PC
                                          					 port.

Link Layer Discovery Protocol-Media Endpoint Devices
                                          					 (LLDP-MED)

LLDP-MED is an extension of the LLDP standard developed for
                                          					 voice products.

The Cisco UnifiedIPPhone supports LLDP-MED on the SW port to
                                          					 communicate information such as:

Voice VLAN
                                                						configuration

Device discovery

Power management

Inventory
                                                				  	management

For more information about LLDP-MED support, see the LLDP-MED
                                          					 and Cisco Discovery Protocol white paper:

http://www.cisco.com/en/US/technologies/tk652/tk701/technologies_white_paper0900aecd804cd46d.html

Real-Time Transport Protocol (RTP)

RTP is a standard protocol for transporting real-time data,
                                          					 such as interactive voice and video, over data networks.

Cisco Unified IP Phones use the RTP protocol to send and
                                          					 receive real-time voice traffic from other phones and gateways.

Real-Time Control Protocol (RTCP)

RTCP works in conjunction with RTP to provide QoS data (such
                                          					 as jitter, latency, and round trip delay) on RTP streams.

By default, the phones have RTCP disabled, but you can enable it on each
                                          					 individual phone using CiscoUnified Communications Manager.

Session Initiation Protocol (SIP)

SIP is the Internet Engineering Task Force (IETF) standard for
                                          					 multimedia conferencing over IP. SIP is an ASCII-based application-layer
                                          					 control protocol (defined in RFC 3261) that can be used to establish, maintain,
                                          					 and terminate calls between two or more endpoints.

Like other VoIP protocols, SIP is designed to address the
                                          					 functions of signaling and session management within a packet telephony
                                          					 network. Signaling allows call information to be carried across network
                                          					 boundaries. Session management provides the ability to control the attributes
                                          					 of an end-to-end call.

You can configure the Cisco Unified IP Phone to use either SIP
                                          					 or Skinny Client Control Protocol (SCCP).

Skinny Client Control Protocol (SCCP)

SCCP includes a messaging set that allows communications
                                          					 between call control servers and endpoint clients such as IP Phones. SCCP is
                                          					 proprietary to Cisco Systems.

Cisco Unified IP Phone 6901 and 6911 use SCCP, version 20 for
                                          					 call control.

Transmission Control Protocol (TCP)

TCP is a connection-oriented transport protocol.

Cisco Unified IP Phones use TCP to connect to Cisco Unified
                                          					 Communications Manager.

Transport Layer Security (TLS)

TLS is a standard protocol for securing and authenticating
                                          					 communications.

When security is implemented, Cisco UnifiedIPPhones use the
                                          					 TLS protocol when securely registering with Cisco UnifiedCommunications
                                          					 Manager.

For more information, see the CiscoUnified
                                             					 Communications Manager Security Guide .

Trivial File Transfer Protocol (TFTP)

TFTP allows you to transfer files over the network.

On the Cisco UnifiedIPPhone, TFTP enables you to obtain a
                                          					 configuration file specific to the phone type.

TFTP requires a TFTP server in your network, which can be
                                          					 automatically identified from the DHCP server. If you want a phone to use a
                                          					 TFTP server other than the one specified by the DHCP server, you must manually
                                          					 assign the IP address of the TFTP server by using the Network Configuration
                                          					 menu on the phone.

For more information, go to the "CiscoTFTP" chapter in the Cisco Unified Communications Manager System Guide .

User Datagram Protocol (UDP)

UDP is a connectionless messaging protocol for delivery of
                                          					 data packets.

Cisco Unified IP Phones transmit and receive RTP streams,
                                          					 which use UDP.

## Cisco Unified IP Phone 6901 and 6911 Supported Features

Cisco UnifiedIPPhones function much like a digital business phone, allowing you to place and receive phone calls. In addition
                           to traditional telephony features, the Cisco Unified IP Phone includes features that enable you to administer and monitor the phone as a network device.

### Feature Overview

CiscoUnified IP Phones provide traditional telephony functionality, Call Forward, Transfer, Redial, Conference, and voice
                              message system access. CiscoUnified IP Phones also provide a variety of other features. For more information on the features,
                              see the Cisco Unified IP Phone 6901 and 6911 User Guide for Cisco Unified Communications Manager (SCCP and SIP) .

As with other network devices, you must configure CiscoUnified IP Phones to prepare them to access CiscoUnifiedCommunications
                              Manager and the rest of the IP network. By using DHCP, you have fewer settings to configure on a phone, but if your network
                              requires it, you can manually configure information, such as an IP address, TFTP server, and subnet information.

Finally, because the CiscoUnified IP Phone is a network device, you can obtain detailed status information from the phone
                              directly. This information can assist you with troubleshooting any problems users might encounter when using their IP Phones.

### Telephony Feature Administration

You can modify additional settings for the CiscoUnified IP
                              		Phone from Cisco Unified Communications Manager. Use Cisco Unified
                              		Communications Manager to set up phone registration criteria and calling search
                              		spaces, among other tasks.

For more information about CiscoUnified Communications
                              		Manager, see the  CiscoUnifiedCommunications Manager documentation, including Cisco UnifiedCommunications Manager Administration Guide .
                              		You can also use the context-sensitive help available within the application
                              		for guidance.

### Cisco Unified IP Phone Network Parameters

You configure parameters such as DHCP, TFTP, and IP settings on the phone.

### Information for End Users

If you are a system administrator, you are likely the primary
                              		source of information for CiscoUnified IP Phone users in your network or
                              		company. To ensure that you distribute the most current feature and procedural
                              		information, familiarize yourself with CiscoUnified IP Phone documentation on
                              		the CiscoUnifiedIPPhone web site.

In addition to providing documentation, you should inform users about the features enabled on the phones, including those
                              specific to your company or network. You should also give users instructions on how to access and customize the features,
                              if appropriate. You might want to use an internal support web site to keep your users informed.

## Cisco Unified IP Phones Security Features

Implementing security in the CiscoUnified Communications
                              		  Manager system prevents identity theft of the phone and CiscoUnified
                              		  Communications Manager server, prevents data tampering, and prevents call
                              		  signaling and media stream tampering.

To alleviate these threats, the Cisco IP telephony network
                              		  establishes and maintains authenticated and encrypted communication streams
                              		  between a phone and the server, digitally signs files before they are
                              		  transferred to a phone, and encrypts media streams and call signaling between
                              		  CiscoUnified IP Phones.

The Cisco Unified IP Phone 6901 and 6911 use the Phone security profile, which defines whether the
                              		  device is nonsecure, authenticated, or encrypted. For information on applying
                              		  the security profile to the phone, see the Cisco Unified Communications Manager Security Guide .

If you configure security-related settings in CiscoUnified
                              		  Communications Manager, the phone configuration file  contains sensitive
                              		  information. To ensure the privacy of a configuration file, you must configure
                              		  it for encryption. For detailed information, see the "Configuring Encrypted Phone Configuration Files" chapter in Cisco Unified Communications Manager Security Guide .

The following table shows where you can find additional
                              		  information about security in this and other documents.

Topic

Reference

Detailed explanation of security, including set up,
                                          					 configuration, and troubleshooting information for Cisco UnifiedCommunications
                                          					 Manager and Cisco UnifiedIP Phones

Troubleshooting Guide for Cisco Unified Communications
                                             						Manager and Cisco Unified Communications Manager Security Guide

Security features supported on the Cisco Unified IP Phone

Supported Security Features

Viewing a security profile name

See Supported Security Features for an overview of the security features supported by the Cisco Unified IP Phone 6901 and 6911 . For more information about these features and
                                          					 about Cisco Unified Communications Manager and Cisco Unified IP Phone security,
                                          					 refer to the Cisco Unified Communications Manager Security
                                             						Guide .

Identifying phone calls for which security is implemented

Authenticated, Encrypted, and Protected Phone Calls

TLS connection

- Network Protocols

- Cisco Unified Communications Manager Phone Addition Methods

Security and the phone startup process

Phone Startup Process

Security and phone configuration files

Cisco Unified Communications Manager Phone Addition Methods

Disabling access to phone web pages

Disable and Enable Web Page Access

Troubleshooting

- Troubleshooting and Maintenance

- Troubleshooting Guide for Cisco Unified Communications Manager

Deleting the CTL file from the phone

Cisco Unified IP Phone Reset or Restore

Resetting or restoring the phone

Cisco Unified IP Phone Reset or Restore

802.1X Authentication for Cisco Unified IP Phones

- 802.1X Authentication

- Troubleshooting and Maintenance

### Supported Security Features

The following table provides an overview of the security
                                 		  features that the Cisco Unified IP Phone 6901 and 6911 support. For more information about these features and about
                                 		  CiscoUnifiedCommunications Manager and CiscoUnifiedIPPhone security, see the Cisco UnifiedCommunications Manager Security Guide .

Most security features are available only if the phone contains a certificate trust list (CTL). For more information about
                                             the CTL, see the "Configuring the Cisco CTL Client" chapter in Cisco Unified Communications Manager Security Guide .

Feature

Description

Image authentication

Signed binary files (with the extension .zz.sgn) prevent
                                             					 tampering with the firmware image before it is loaded on a phone. Tampering
                                             					 with the image causes a phone to fail the authentication process and reject the
                                             					 new image.

Customer-site certificate installation

Each Cisco Unified IP Phone requires a unique certificate for
                                             					 device authentication. Phones include a manufacturing installed certificate
                                             					 (MIC), but for additional security, you can specify in Cisco
                                             					 UnifiedCommunications Manager Administration that a certificate be installed
                                             					 by using the Certificate Authority Proxy Function (CAPF).

Device authentication

Occurs between the Cisco Unified Communications Manager server
                                             					 and the phone when each entity accepts the certificate of the other entity.
                                             					 Determines whether a secure connection between the phone and a Cisco Unified
                                             					 Communications Manager should occur and, if necessary, creates a secure
                                             					 signaling path between the entities by using TLS protocol. Cisco Unified
                                             					 Communications Manager will not register phones unless they can be
                                             					 authenticated by the Cisco UnifiedCommunications Manager.

File authentication

Validates digitally signed files that the phone downloads. The
                                             					 phone validates the signature to make sure that file tampering did not occur
                                             					 after the file creation. Files that fail authentication are not written to
                                             					 flash memory on the phone. The phone rejects unauthenticated files without further
                                             					 processing.

Signaling Authentication

Uses the TLS protocol to validate that no tampering has
                                             					 occurred to signaling packets during transmission.

Manufacturing installed certificate

Each Cisco Unified IP Phone contains a unique manufacturing
                                             					 installed certificate (MIC), which is used for device authentication. The MIC
                                             					 is a permanent unique proof of identity for the phone, and allows Cisco Unified
                                             					 Communications Manager to authenticate the phone.

Secure SRST reference

After you configure a Cisco Unified Survivable Remote Site
                                             					 Telephony (SRST) reference for security and reset the dependent devices in
                                             					 Cisco Unified Communications Manager, the TFTP server adds the SRST certificate
                                             					 to the phone configuration file and sends the file to the phone. A secure phone
                                             					 uses a TLS connection to interact with the SRST-enabled router.

The configuration file uses one of the following
                                             					 extensions:

.cnf.xml

.cnf.xml.sgn

.cnf.xml.enc.sgn

Media encryption

Uses SRTP to ensure that the media streams between supported phones proves secure and that
                                             									only the intended phone receives and reads the data. Includes
                                             									creating a media primary key pair for the phones, delivering the
                                             									keys to the phones, and securing the delivery of the keys while
                                             									the keys are in transport.

Signaling encryption

Ensures that all SCCP and SIP signaling messages sent between
                                             					 the phone and the Cisco Unified Communications Manager server are encrypted.

Certificate Authority Proxy Function (CAPF)

Implements parts of the certificate generation procedure that
                                             					 are too processing-intensive for the phone, and interacts with the phone for
                                             					 key generation and certificate installation. The CAPF can be configured to
                                             					 request certificates from customer-specified certificate authorities on behalf
                                             					 of the phone, or it can be configured to generate certificates locally.

Security profiles

Defines whether the phone is nonsecure, authenticated,
                                             					 encrypted, or protected.

Encrypted configuration files

Ensures the privacy of phone configuration files.

Optional disabling of the web server functionality for a phone

Prevents access to a phone web page that displays a variety of
                                             					 operational statistics for the phone.

Phone hardening

The following is an additional security option that you control from Cisco
                                             					 Unified Communications Manager:

Disabling access
                                                   						to web pages for a phone

802.1X Authentication

Defines the use of 802.1X authentication to request and gain
                                             					 access to the network.

Voice Quality Metrics

MOS LQK

Objective estimate of the Mean Opinion Score (MOS) for
                                             					 Listening Quality (LQK) that ranks audio quality from 5 (excellent) to 1 (bad).
                                             					 This score is based on audible-concealment events due to a frame loss in the
                                             					 preceding 8 seconds of the voice stream.

The MOS LQK score can vary based on the type of codec that
                                                         						the CiscoUnifiedIPPhone uses.

Avg MOS LQK

Average MOS LQK score for the entire voice stream.

Min MOS LQK

Lowest MOS LQK score from the start of the voice stream.

Max MOS LQK

Baseline or highest MOS LQK score from the start of the voice
                                             					 stream.

The following codecs provide the corresponding maximum MOS LQK
                                             					 scores under normal conditions with no frame loss:

G.711: 4.5

G.728/iLBC: 3.9

G729A/AB: 3.7

MOS LQK Version

Version of the Cisco-proprietary algorithm used to calculate
                                             					 the MOS LQK scores.

### Security Profiles

All Cisco Unified IP Phones that support CiscoUnified
                              		Communications Manager use a security profile, which defines whether the phone
                              		is nonsecure, authenticated, or encrypted. For information about configuring
                              		the security profile and applying the profile to the phone, see the Cisco Unified Communications Manager Security Guide .

To view the phone security mode, you can
                              		view the security profile in Cisco Unified Communications Manager.

### Authenticated, Encrypted, and Protected Phone Calls

In an authenticated call, all devices participating in the
                              		establishment of the call are trusted devices, and authenticated by
                              		CiscoUnified Communications Manager.

In an encrypted call, all devices participating in the
                              		establishment of the call are trusted devices, and authenticated by
                              		CiscoUnified Communications Manager. In addition, call signaling and media
                              		streams are encrypted. An encrypted call offers a high level of security,
                              		providing integrity and privacy to the call.

If the call is routed through non-IP call legs, for example,
                              		PSTN, the call may be nonsecure even though it is encrypted within the IP
                              		network.

In a protected call, a security tone plays at the beginning of
                              		a call to indicate that the other connected phone is also receiving and
                              		transmitting encrypted audio and video (if video is involved). If your call is
                              		connected to a non-protected phone, the security tone does not play.

Connections between two phones support protected calling. Some features, such as conference calling and shared lines, are
                                          not
                                          		  available when protected calling is configured. Protected calls are not
                                          		  authenticated.

#### Identify Protected Calls

A protected call establishes when your phone and the phone on the other end are set up for protected calling. The other phone
                                    can be in the same Cisco IP network, or on a network outside the IP network. Protected calls can only be made between two
                                    phones. Conference calls and other multiple-line calls do not support protected calls.

A protected call establishes using this process:

A user initiates the call from a protected phone (protected security mode).

A security tone plays if the call connects to another protected phone, indicating that both ends of the conversation are encrypted
                                          and protected. If the call connects to a non protected phone, then the secure tone does not play.

Connections between two phones support protected calling. Some features, such as conference calling and shared lines are not
                                                available when protected calling is configured.

#### Call Security Interactions and Restrictions

Cisco Unified Communications Manager checks the phone
                                    		  security status when conferences  establish and changes the security
                                    		  indication for the conference or blocks the completion of the call to maintain
                                    		  integrity and security in the system.

The following table provides information about changes to
                                    		  call security levels when using Barge for 
                                    		  Cisco Unified IP Phone 6911.

Initiator’s phone security level

Feature used

Call security level

Results of action

Nonsecure

cBarge

Encrypted call

Call barged and identified as nonsecure call

Secure (encrypted)

cBarge

Authenticated call

Call barged and identified as authenticated call

Secure (authenticated)

cBarge

Encrypted call

Call barged and identified as authenticated call

Nonsecure

cBarge

Authenticated call

Call barged and identified as nonsecure call

The following table provides information about changes to
                                    		  conference security levels depending on the initiator phone security level, the
                                    		  security levels of participants, and the availability of secure conference
                                    		  bridges.

Initiator’s phone security level

Feature used

Security level of participants

Results of action

Nonsecure

Conference

Encrypted or authenticated

Nonsecure conference bridge

Nonsecure conference

Secure (encrypted or authenticated)

Conference

At least one member is nonsecure

Nonsecure conference

Secure (encrypted)

Conference

All participants are encrypted

Secure encrypted level conference

Secure (authenticated)

Conference

All participants are encrypted or authenticated

Secure authenticated level conference

Nonsecure

cBarge

All participants are encrypted

Conference changes to nonsecure

Nonsecure

Meet Me

Minimum security level is encrypted

Initiator receives the message Does not meet Security Level , and the call rejected.

Secure (encrypted)

Meet Me

Minimum security level is authenticated

Conference accepts encrypted and authenticated calls

Secure (encrypted)

Meet Me

Minimum security level is nonsecure

Only secure conference bridge available and used

Conference accepts all calls

### 802.1X Authentication

The following sections describe the 802.1X support on the
                              		Cisco Unified IP Phones.

#### Overview

Cisco Unified IP Phones and Cisco Catalyst switches traditionally use Cisco Discovery Protocol (CDP) to identify each other
                                 and determine parameters such as VLAN allocation and inline power requirements. CDP does not identify locally attached workstations.
                                 Cisco Unified IP Phones provide an EAPOL pass-through mechanism.  This mechanism allows a workstation attached to the Cisco
                                 Unified IP Phone to pass EAPOL messages to the 802.1X authenticator at the LAN switch. The pass-through mechanism ensures
                                 that the IP phone does not act as the LAN switch to authenticate a data endpoint before accessing the network.

Cisco Unified IP Phones also provide a proxy EAPOL Logoff mechanism. In the event that the locally attached PC disconnects
                                 from the IP phone, the LAN switch does not see the physical link fail, because the link between the LAN switch and the IP
                                 phone is maintained. To avoid compromising network integrity, the IP phone sends an EAPOL-Logoff message to the switch on
                                 behalf of the downstream PC, which triggers the LAN switch to clear the authentication entry for the downstream PC.

Cisco Unified IP Phones also contain an 802.1X supplicant. This supplicant allows network administrators to control the connectivity
                                 of IP phones to the LAN switch ports. The current release of the phone 802.1X supplicant uses the EAP-FAST, EAP-TLS, and EAP-MD5
                                 options for network authentication.

#### Required Network Components

Support for 802.1X authentication on Cisco Unified IP Phones
                                 		requires several components, including:

Cisco Unified IP Phone: The phone acts as the 802.1X supplicant , which initiates the request to access the network.

Cisco Secure Access Control Server (ACS) (or other third-party
                                       			 authentication server): The authentication server and the phone must both be
                                       			 configured with a shared secret that authenticates the phone.

Cisco Catalyst Switch (or other third-party switch): The switch
                                       			 must support 802.1X, so it can act as the authenticator and pass the messages between the phone and the
                                       			 authentication server. After the exchange completes, the switch grants or
                                       			 denies the phone access to the network.

#### Best Practices-Requirements and Recommendations

Enable 802.1X Authentication: If you want to use the 802.1X
                                       			 standard to authenticate Cisco Unified IP Phones, be sure that you have
                                       			 properly configured the other components before enabling the standard on the phone.

Configure PC Port: The 802.1X standard does not take into account
                                       			 the use of VLANs and thus Cisco recommends that only a single device should be
                                       			 authenticated to a specific switch port. However, some switches (including
                                       			 Cisco Catalyst switches) support multi-domain authentication. The switch
                                       			 configuration determines whether you can connect a PC to the PC port of the phone.

Only Cisco Unified IP Phone 6911 has a PC port.

Enabled: If you are using a switch that supports multi-domain
                                             					 authentication, you can enable the PC port and connect a PC to it. In this
                                             					 case, Cisco Unified IP Phones support proxy EAPOL-Logoff to monitor the
                                             					 authentication exchanges between the switch and the attached PC. For more
                                             					 information about IEEE 802.1X support on the Cisco Catalyst switches, refer to
                                             					 the Cisco Catalyst switch configuration guides at:

http://www.cisco.com/en/US/products/hw/switches/ps708/tsd_products_support_series_home.html

Disabled: If the switch does not support multiple
                                             					 802.1X-compliant devices on the same port, you should disable the PC Port when
                                             					 802.1X authentication is enabled. If you do not disable this port and
                                             					 subsequently attempt to attach a PC to it, the switch will deny network access
                                             					 to both the phone and the PC.

Configure Voice VLAN: Because the 802.1X standard does
                                       						  not account for VLANs, you should configure this setting based on the switch
                                       						  support.

Enabled: If you are using a switch that supports multi-domain
                                             					 authentication, you can continue to use the Voice VLAN.

Disabled: If the switch does not support multi-domain
                                             					 authentication, disable the Voice VLAN and consider assigning the port to the
                                             					 native VLAN.

## Cisco Unified IP Phone Deployment

When deploying a new IP telephony system, system
                           		administrators and network administrators must complete several initial
                           		configuration tasks to prepare the network for IPtelephony service. For
                           		information and a checklist for setting up and configuring a Cisco IP telephony
                           		network, see the "System Configuration Overview " chapter in Cisco Unified Communications Manager System Guide .

After you set up the IP telephony system and configure
                           		system-wide features in CiscoUnified Communications Manager, you can add IP
                           		Phones to the system.

### Cisco Unified IP Phones Setup in Cisco Unified Communications Manager

To add phones to the CiscoUnified Communications Manager
                              		database, you can use:

Autoregistration: Not supported if Cisco Unified Communications
                                    			 Manager operates in mixed mode.

CiscoUnified Communications Manager

BulkAdministration Tool (BAT)

BAT and the Tool for Auto-Registered Phones Support (TAPS)

For general information about
                              		configuring phones in CiscoUnified Communications Manager, refer to the
                              		following documentation:

"CiscoUnified IP Phones" , Cisco Unified Communications Manager System Guide

"Cisco Unified IP Phone Configuration" , CiscoUnified Communications Manager Administration Guide

"Autoregistration Configuration" , CiscoUnified Communications Manager Administration
                                       				Guide

The following section provides additional information.

#### Set Up Cisco Unified IP Phone 6901 and 6911 in Cisco Unified Communications Manager

The following procedure provides an overview of
                                    		  configuration tasks for the Cisco Unified IP Phone 6901 and 6911 in CiscoUnifiedCommunications Manager Administration. The
                                    		  procedure presents a suggested order to guide you through the phone configuration
                                    		  process. Some tasks are optional, depending on your system and user needs. For
                                    		  detailed procedures and information, see the sources in the procedure.

Step 1

Gather the following information about the phone:

Phone Model

MAC address

Physical location of the phone

Name or user ID of phone user

Device pool

Partition, calling search space, and location information

Associated directory number (DN) to assign to the phone

Cisco UnifiedCommunications Manager user to associate with
                                                      					 the phone

Provides list of configuration requirements for setting up phones.

For more information, see the "CiscoUnified IP Phones" chapter in the Cisco Unified Communications Manager System Guide and
                                                				see Telephony Features Available for Cisco Unified IP Phone .

Step 2

Verify that you have sufficient unit licenses for your phone. For
                                             			 more information, see the "License Unit Report" chapter in the Cisco Communications Manager Administration Guide .

Step 3

Add and configure the phone by completing the required fields in
                                             			 the Phone Configuration window. An asterisk (*) next to the field name indicates a required field for example, MAC address
                                             			 and device pool.

The phone with the  default settings gets added to the Cisco
                                                				Unified Communications Manager database. For more information, see the "Cisco Unified IP Phone Configuration" chapter in
                                                				the Cisco Communications Manager Administration Guide .

For information about Product Specific Configuration fields, see ? Button Help in the 
                                                				Phone Configuration window.

If you want to add both the phone and user to the Cisco Unified
                                                            				  Communications Manager database at the same time, see the "User/Phone Add Configuration" chapter in the Cisco Communications Manager Administration Guide .

Step 4

Add and configure directory numbers (lines) on the phone by
                                             			 completing the required fields in the Directory Number Configuration window.
                                             			 An asterisk (*) next to the field name indicates a required field  for
                                             			 example, directory number and presence group.

For more information, see the "Directory Number Configuration" chapter in the Cisco Unified Communications Manager Administration
                                                   				  Guide and see Telephony Features Available for Cisco Unified IP Phone .

Step 5

Add user information by configuring required fields. An asterisk (*) next to the field name indicates a required field for
                                             example, User ID and last name.

Assign a password (for User Options web pages) and PIN (for
                                                               					 accessing the Network Menu from  the Interactive Voice Response [IVR]).

Adds user information to the global directory for Cisco
                                                				UnifiedCommunications Manager (Unified CM).

For more information, see the "End User Configuration" chapter in the Cisco Unified Communications Manager Administration
                                                   				  Guide and see Add Users to Cisco Unified Communications Manager .

If you want to add both the phone and user to the Cisco
                                                               					 Unified Communications Manager database at the same time, see the "User/Phone Add Configurations" chapter in the Cisco Unified Communications Manager Administration
                                                                  						Guide .

Step 6

Associate a user to a user group. Assigns users a common list of
                                             			 roles and permissions that apply to all users in a user group. Administrators
                                             			 can manage user groups, roles, and permissions to control the level of access
                                             			 (and, therefore, the level of security) for system users.

For end users to access Cisco Unified CM User Options, you must
                                                            				  add users to the standard Cisco CCM End Users group.

For more information, see the following sections in the Cisco Unified Communications Manager Administration
                                                   				  Guide :

End User Configuration Settings section in
                                                      					 the "End User Configuration" chapter.

Adding Users to a User Group section in the "User Group Configuration" chapter.

Step 7

Associate a user with a phone. Provides
                                             			 users with control over their phone for actions such as forwarding calls or adding
                                             			 speed-dial numbers or services.

Some phones, such as those in conference rooms, do not have an
                                                            				  associated user.

For more information, see  the Associating Devices to an
                                                				  End User section in the "End User Configuration" chapter in the Cisco Unified Communications Manager Administration
                                                   				  Guide .

### Cisco Unified IP Phones Installation

After you have added the phones to the CiscoUnified
                              		Communications Manager database, you can complete the phone installation. You
                              		(or the phone user) can install the phone at the location of the user.

Upgrade the phone with the current firmware image before you install
                                          		  the phone. For information about upgrading, see the Readme file for your
                                          		  phone, located at:

http://tools.cisco.com/support/downloads/go/Redirect.x?mdfid=278875240

For instructions on upgrading the firmware, see the Release Notes,
                                          		  located at:

http://www.cisco.com/en/US/products/ps10326/prod_release_notes_list.html

After the phone connects to the network, the phone startup
                              		process begins, and the phone registers with CiscoUnified Communications
                              		Manager. To finish installing the phone, configure the network settings on the
                              		phone depending on whether you enable or disable DHCP service.

If you used autoregistration, you need to update the specific
                              		configuration information for the phone such as associating the phone with a
                              		user, changing the button table, or directory number.

#### Install Cisco Unified IP Phone 6901 and 6911

The following procedure provides an overview of
                                    		  installation tasks for the Cisco Unified IP Phone 6901 and 6911 . The procedure presents a suggested order to guide you through
                                    		  the phone installation. Some tasks are optional, depending on your system and
                                    		  user needs. For detailed procedures and information, see the sources in
                                    		  the procedure.

Step 1

Choose the power source for the phone:

Power over Ethernet (PoE)

External power supply

Determines how the phone receives power. For more information, see Cisco Unified IP Phone Power .

Step 2

Assemble the phone, adjust phone placement, and connect the
                                             			 network cable.

Locates and installs the phone in the network. See Install Cisco Unified IP Phone .

See Footstand .

Step 3

Monitor the phone startup process. Associates directory numbers to
                                             			 the phone and verifies that phone is configured properly.

See Phone Startup Verification .

Step 4

If you are configuring the network settings on the phone, you can
                                             			 set up an IP address for the phone by either using DHCP or manually entering an
                                             			 IP address.

Verify that the phone has DHCP enabled using  the IVR. You can
                                                            					 set an alternate TFTP server by entering the IP address for the TFTP when prompted by
                                                            					 the IVR.

Consult with the network administrator to determine whether
                                                                        						you need to assign an alternative TFTP server instead of using the TFTP server
                                                                        						assigned by DHCP.

Verify that the phone has DHCP disabled using  the IVR. You
                                                            					 must then configure the IP address, subnet mask, TFTP server, and default
                                                            					 router locally by using the IVR on the phone.

For more information, see Network Settings and Cisco Unified IP Phone Network Settings Setup .

Step 5

Set up security on the phone.

Provides protection against data tampering threats and identity
                                                				theft of phones.

For more information, see Cisco Unified IP Phone Security .

Step 6

Make calls with the Cisco Unified IP Phone. Verifies that the
                                             			 phone and features work correctly. For more information, see Cisco Unified IP Phone 6901 and 6911 User Guide for Cisco Unified Communications Manager (SCCP and SIP) .

Step 7

Provide information to end users about how to use their phones and
                                             			 how to configure their phone options.

Ensures that users have adequate information to successfully use
                                                				their Cisco UnifiedIPPhones.

See Internal Support Web Site

## Phone Power Reduction

The Cisco Unified IP Phone 6901 and 6911 supports Cisco EnergyWise (EW) (also known as Power Save Plus). When your network
                           contains an EnergyWise controller, you can configure these phones to sleep (power down) and wake (power up) on a schedule
                           to reduce your power consumption.

You set up each phone to enable or disable the EnergyWise settings. If EnergyWise is enabled, you configure a sleep and wake
                           time, as well as other parameters. These parameters are sent to the phone as part of the phone configuration file.

## Terminology Differences

The following table highlights some of the important
                              		  differences in terminology used in these documents:

Cisco Unified IP Phone 6901 and 6911 User Guide for Cisco Unified Communications
                                       				  Manager (SCCP and SIP)

Cisco Unified IP Phone 6901 and 6911 Administration Guide
                                       				  for Cisco Unified Communications Manager (SCCP and SIP)

Cisco Unified Communications Manager Administration
                                       				  Guide

Cisco Unified Communications Manager System Guide

User Guide

Administration and System Guides

Auto Barge

cBarge

Message Indicators

Message Waiting Indicator (MWI) or Message Waiting Lamp

Voice mail system

Voice messaging system

| Caution | Using a cell, mobile, or GSM phone, or two-way radio in close proximity to a Cisco Unified IP Phone might cause interference.
                                       For more information, refer to the manufacturer’s documentation of the interfering device. |
|---|---|

| 1 | Slot for Ethernet cable. | 4 | Network port (10/100 SW) connection. IEEE 802.3af power enabled. |
|---|---|---|---|
| 2 | Handset connection. | 5 | DC adaptor port (DC48V). |
| 3 | Slot for handset cable. | 6 | Slot for DC adaptor cable. |

| Note | In the EU and UK, your phone is shipped with a power switch cable that is required in order to provide power to your phone
                                             when using an AC-to-DC power supply. Connect the power cord to the power switch cable and then connect the other end of the
                                             power switch cable to the DC adapter port. |
|---|---|

| 1 | Hookswitch | Activates the features (hookflash) on your phone. |
|---|---|---|
| 2 | Hold button | Places a connected call on hold. |
| 3 | Redial button | Dials the last dialed number. |
| 4 | Line button | Allows you to pick up a second incoming call. The Line
                                             						button LED indicates the call status. Allows you to answer a ringing call and swap between two
                                             						calls on the same line. Also, you can use the line button to create a new call
                                             						when the phone is idle. The LED associated with the line button lights up to
                                             						reflect the line status. Color LEDs indicate the line state: Green,
                                                						  steady—Active call Green,
                                                						  flashing—Held call Amber,
                                                						  Flashing—Incoming call Amber,
                                                						  steady—Call Forward All activated Red,
                                                						  steady—Remote line in use (shared line) Red,
                                                						  flashing—Remote line on hold |
| 5 | Volume button | Controls the handset (off hook) and the ringer volume (on hook). |
| 6 | Keypad | Allows you to dial phone numbers. |
| 7 | Handset with light strip | Lights up to indicate a ringing call (flashing red) or a new
                                             						voice message (steadyred). |

| 1 | DC adaptor port (DC48V). | 4 | Network port (10/100 SW) connection. IEEE 802.3af power enabled. |
|---|---|---|---|
| 2 | AC-to-DC power supply (optional). | 5 | Access port (10/100 PC) connection. |
| 3 | AC power wall plug (optional). | 6 | Handset connection. |

| 1 | Handset with light strip | Lights up to indicate a ringing call (flashing red) or a new
                                             						voice message (steady red). |
|---|---|---|
| 2 | Paper label | A paper strip used to enter name and contact numbers. |
| 3 | Transfer button | Transfers a call. |
| 4 | Conference button | Creates a conference call. |
| 5 | Hold button | Places an active call on hold. |
| 6 | Line button | Allows you to pick up a second incoming call and to resume
                                             						a held call. The LED shows call status. |
| 7 | Speakerphone button | Selects the speakerphone as the default audio path and
                                             						initiates a new call, picks up an incoming call, or ends a call. During a call,
                                             						the button lights green. The speakerphone audio path does not change until 
                                             						you select a new audio path (for example, by picking up the handset). |
| 8 | Keypad | Allows you to dial phone numbers. |
| 9 | Mute button | Toggles the microphone on or off. When the microphone is
                                             						muted, the button lights red. |
| 10 | Volume button | Controls the handset and speakerphone volume (off hook) and
                                             						the ringer volume (on hook). |
| 11 | Messages button | Auto dials your voice messaging system. |
| 12 | Redial button | Dials the last dialed number. |
| 13 | Feature button | Depending on the
                                             						phone setup, the feature button provides you with access to Speed Dial, Call Forward
                                             						All, Pickup, Group Pickup and Meet Me features. You can configure up to nine
                                             						items on the feature button. To access these features, press the feature button
                                             						followed by the number associated with the feature. You must press the feature
                                             						button and the number within five seconds of each other. The number can only be
                                             						a single digit number from 1–9. You can access the following features either off hook or on hook: Call Forward
                                                   						  All—Allows you to forward a call. Pickup—Allows
                                                   						  you to pickup a call on the third party phone. Group
                                                   						  Pickup—Allows you pick up a call within a group. Meet Me—Allows
                                                   						  you setup a conference. |
| 14 | Handset | Phone handset. |

| If your phone screen gets dirty, wipe it with a soft, dry cloth. Caution Don't use any liquids or powders on the phone because they can contaminate the phone components and cause failures. | Caution | Don't use any liquids or powders on the phone because they can contaminate the phone components and cause failures. |
|---|---|---|
| Caution | Don't use any liquids or powders on the phone because they can contaminate the phone components and cause failures. |

| Caution | Don't use any liquids or powders on the phone because they can contaminate the phone components and cause failures. |
|---|---|

| 1 | Insert the connectors into the lower slots. | 2 | Lift the footstand until the connectors snap into the upper
                                             									slots. |
|---|---|---|---|

| Connect the footstand to the lower slots for a higher viewing
                                          			 angle, as shown in the following figure. |
|---|

| Connect the footstand to the upper slots for a lower viewing
                                          			 angle, as shown in the following figure. |
|---|

|  | High Sound Pressure—Avoid listening to high volume levels for long periods to prevent possible hearing damage. |
|---|---|

| Network Protocol | Purpose | Usage notes |
|---|---|---|
| Cisco Audio Session Tunneling (CAST) (Cisco Unified IP Phone 6911 only) | The CAST protocol allows IP Phones and associated applications
                                          					 behind the phone to discover and communicate with the remote endpoints without
                                          					 requiring changes to the traditional signaling components like Cisco Unified
                                          					 Communications Manager and gateways. The CAST protocol allows separate hardware
                                          					 devices to synchronize related media and it allows PC applications to augment
                                          					 nonvideo-capable phones to become video enabled by using the PC as the video
                                          					 resource. | - |
| Cisco Discovery Protocol (CDP) | CDP is a device-discovery protocol that runs on all
                                          					 Cisco-manufactured equipment. Using CDP, a device advertises its existence to other devices
                                          					 and receives information about other devices in the network. | The Cisco UnifiedIPPhone uses CDP to communicate information
                                          					 such as auxiliary VLAN ID, per port power management details, and Quality of
                                          					 Service (QoS) configuration information with the Cisco Catalyst switch. |
| Dynamic Host Configuration Protocol (DHCP) | DHCP dynamically allocates and assigns an IP address to
                                          					 network devices. DHCP enables you to connect an IP Phone into the network and
                                          					 have the phone become operational without needing to manually assign an IP
                                          					 address or to configure additional network parameters. | By default, the phone has DHCP enabled. If disabled, you must manually
                                          					 configure the IP address, subnet mask, gateway, and a TFTP server on each phone
                                          					 locally. Cisco recommends that you use DHCP custom option 150. With
                                          					 this method, you configure the TFTP server IP address as the option value. For
                                          					 additional supported DHCP configurations, go to the "Dynamic Host Configuration Protocol" chapter and
                                          					 the "CiscoTFTP" chapter in the Cisco Unified Communications Manager System Guide . Note If you cannot use option 150, you may try using DHCP option
                                                      						66. | Note | If you cannot use option 150, you may try using DHCP option
                                                      						66. |
| Note | If you cannot use option 150, you may try using DHCP option
                                                      						66. |
| Hypertext Transfer Protocol (HTTP) | HTTP is the standard way of transferring information and
                                          					 moving documents across the Internet and the web. | Cisco UnifiedIP Phones use HTTP for troubleshooting purposes. |
| IEEE 802.1X | The IEEE 802.1X standard defines a client-server-based access
                                          					 control and authentication protocol that restricts unauthorized clients from
                                          					 connecting to a LAN through publicly accessible ports. Until the client is authenticated, 802.1X access control
                                          					 allows only Extensible Authentication Protocol over LAN (EAPOL) traffic through
                                          					 the port to which the client connects. After successful authentication,
                                          					 normal traffic passes through the port. | The Cisco Unified IP Phone implements the IEEE 802.1X standard
                                          					 by providing support for the following authentication methods: EAP-FAST and
                                          					 EAP-TLS. When 802.1X authentication is enabled on the phone, you should
                                          					 disable the voice VLAN. Refer to the 802.1X Authentication for additional information. |
| Internet Protocol (IP) | IP is a messaging protocol that addresses and sends packets
                                          					 across the network. | To communicate using IP, network devices must have an assigned
                                          					 IP address, subnet, and gateway. IP addresses, subnets, and gateways  are
                                          					 automatically assigned if you are using the Cisco UnifiedIPPhone with Dynamic
                                          					 Host Configuration Protocol (DHCP). If you are not using DHCP, you must
                                          					 manually assign these properties to each phone locally. The Cisco Unified IP Phones support IPv6 address. For more
                                          					 information, see "Internet Protocol Version 6 (IPv6)" in the Cisco Unified Communications Manager Features and
                                             						Services Guide . |
| Link Layer Discovery Protocol (LLDP) ( Cisco Unified IP Phone 6911 only) | LLDP is a standardized network discovery protocol (similar to
                                          					 CDP) that is supported on some Cisco and third-party devices. | The Cisco UnifiedIPPhone 6911 supports LLDP on the switch and PC
                                          					 port. |
| Link Layer Discovery Protocol-Media Endpoint Devices
                                          					 (LLDP-MED) | LLDP-MED is an extension of the LLDP standard developed for
                                          					 voice products. | The Cisco UnifiedIPPhone supports LLDP-MED on the SW port to
                                          					 communicate information such as: Voice VLAN
                                                						configuration Device discovery Power management Inventory
                                                				  	management For more information about LLDP-MED support, see the LLDP-MED
                                          					 and Cisco Discovery Protocol white paper: http://www.cisco.com/en/US/technologies/tk652/tk701/technologies_white_paper0900aecd804cd46d.html |
| Real-Time Transport Protocol (RTP) | RTP is a standard protocol for transporting real-time data,
                                          					 such as interactive voice and video, over data networks. | Cisco Unified IP Phones use the RTP protocol to send and
                                          					 receive real-time voice traffic from other phones and gateways. |
| Real-Time Control Protocol (RTCP) | RTCP works in conjunction with RTP to provide QoS data (such
                                          					 as jitter, latency, and round trip delay) on RTP streams. | By default, the phones have RTCP disabled, but you can enable it on each
                                          					 individual phone using CiscoUnified Communications Manager. |
| Session Initiation Protocol (SIP) | SIP is the Internet Engineering Task Force (IETF) standard for
                                          					 multimedia conferencing over IP. SIP is an ASCII-based application-layer
                                          					 control protocol (defined in RFC 3261) that can be used to establish, maintain,
                                          					 and terminate calls between two or more endpoints. | Like other VoIP protocols, SIP is designed to address the
                                          					 functions of signaling and session management within a packet telephony
                                          					 network. Signaling allows call information to be carried across network
                                          					 boundaries. Session management provides the ability to control the attributes
                                          					 of an end-to-end call. You can configure the Cisco Unified IP Phone to use either SIP
                                          					 or Skinny Client Control Protocol (SCCP). |
| Skinny Client Control Protocol (SCCP) | SCCP includes a messaging set that allows communications
                                          					 between call control servers and endpoint clients such as IP Phones. SCCP is
                                          					 proprietary to Cisco Systems. | Cisco Unified IP Phone 6901 and 6911 use SCCP, version 20 for
                                          					 call control. |
| Transmission Control Protocol (TCP) | TCP is a connection-oriented transport protocol. | Cisco Unified IP Phones use TCP to connect to Cisco Unified
                                          					 Communications Manager. |
| Transport Layer Security (TLS) | TLS is a standard protocol for securing and authenticating
                                          					 communications. | When security is implemented, Cisco UnifiedIPPhones use the
                                          					 TLS protocol when securely registering with Cisco UnifiedCommunications
                                          					 Manager. For more information, see the CiscoUnified
                                             					 Communications Manager Security Guide . |
| Trivial File Transfer Protocol (TFTP) | TFTP allows you to transfer files over the network. On the Cisco UnifiedIPPhone, TFTP enables you to obtain a
                                          					 configuration file specific to the phone type. | TFTP requires a TFTP server in your network, which can be
                                          					 automatically identified from the DHCP server. If you want a phone to use a
                                          					 TFTP server other than the one specified by the DHCP server, you must manually
                                          					 assign the IP address of the TFTP server by using the Network Configuration
                                          					 menu on the phone. For more information, go to the "CiscoTFTP" chapter in the Cisco Unified Communications Manager System Guide . |
| User Datagram Protocol (UDP) | UDP is a connectionless messaging protocol for delivery of
                                          					 data packets. | Cisco Unified IP Phones transmit and receive RTP streams,
                                          					 which use UDP. |

| Note | If you cannot use option 150, you may try using DHCP option
                                                      						66. |
|---|---|

| Topic | Reference |
|---|---|
| Detailed explanation of security, including set up,
                                          					 configuration, and troubleshooting information for Cisco UnifiedCommunications
                                          					 Manager and Cisco UnifiedIP Phones | Troubleshooting Guide for Cisco Unified Communications
                                             						Manager and Cisco Unified Communications Manager Security Guide |
| Security features supported on the Cisco Unified IP Phone | Supported Security Features |
| Viewing a security profile name | See Supported Security Features for an overview of the security features supported by the Cisco Unified IP Phone 6901 and 6911 . For more information about these features and
                                          					 about Cisco Unified Communications Manager and Cisco Unified IP Phone security,
                                          					 refer to the Cisco Unified Communications Manager Security
                                             						Guide . |
| Identifying phone calls for which security is implemented | Authenticated, Encrypted, and Protected Phone Calls |
| TLS connection | Network Protocols Cisco Unified Communications Manager Phone Addition Methods |
| Security and the phone startup process | Phone Startup Process |
| Security and phone configuration files | Cisco Unified Communications Manager Phone Addition Methods |
| Disabling access to phone web pages | Disable and Enable Web Page Access |
| Troubleshooting | Troubleshooting and Maintenance Troubleshooting Guide for Cisco Unified Communications Manager |
| Deleting the CTL file from the phone | Cisco Unified IP Phone Reset or Restore |
| Resetting or restoring the phone | Cisco Unified IP Phone Reset or Restore |
| 802.1X Authentication for Cisco Unified IP Phones | 802.1X Authentication Troubleshooting and Maintenance |

| Note | Most security features are available only if the phone contains a certificate trust list (CTL). For more information about
                                             the CTL, see the "Configuring the Cisco CTL Client" chapter in Cisco Unified Communications Manager Security Guide . |
|---|---|

| Feature | Description |
|---|---|
| Image authentication | Signed binary files (with the extension .zz.sgn) prevent
                                             					 tampering with the firmware image before it is loaded on a phone. Tampering
                                             					 with the image causes a phone to fail the authentication process and reject the
                                             					 new image. |
| Customer-site certificate installation | Each Cisco Unified IP Phone requires a unique certificate for
                                             					 device authentication. Phones include a manufacturing installed certificate
                                             					 (MIC), but for additional security, you can specify in Cisco
                                             					 UnifiedCommunications Manager Administration that a certificate be installed
                                             					 by using the Certificate Authority Proxy Function (CAPF). |
| Device authentication | Occurs between the Cisco Unified Communications Manager server
                                             					 and the phone when each entity accepts the certificate of the other entity.
                                             					 Determines whether a secure connection between the phone and a Cisco Unified
                                             					 Communications Manager should occur and, if necessary, creates a secure
                                             					 signaling path between the entities by using TLS protocol. Cisco Unified
                                             					 Communications Manager will not register phones unless they can be
                                             					 authenticated by the Cisco UnifiedCommunications Manager. |
| File authentication | Validates digitally signed files that the phone downloads. The
                                             					 phone validates the signature to make sure that file tampering did not occur
                                             					 after the file creation. Files that fail authentication are not written to
                                             					 flash memory on the phone. The phone rejects unauthenticated files without further
                                             					 processing. |
| Signaling Authentication | Uses the TLS protocol to validate that no tampering has
                                             					 occurred to signaling packets during transmission. |
| Manufacturing installed certificate | Each Cisco Unified IP Phone contains a unique manufacturing
                                             					 installed certificate (MIC), which is used for device authentication. The MIC
                                             					 is a permanent unique proof of identity for the phone, and allows Cisco Unified
                                             					 Communications Manager to authenticate the phone. |
| Secure SRST reference | After you configure a Cisco Unified Survivable Remote Site
                                             					 Telephony (SRST) reference for security and reset the dependent devices in
                                             					 Cisco Unified Communications Manager, the TFTP server adds the SRST certificate
                                             					 to the phone configuration file and sends the file to the phone. A secure phone
                                             					 uses a TLS connection to interact with the SRST-enabled router. The configuration file uses one of the following
                                             					 extensions: .cnf.xml .cnf.xml.sgn .cnf.xml.enc.sgn |
| Media encryption | Uses SRTP to ensure that the media streams between supported phones proves secure and that
                                             									only the intended phone receives and reads the data. Includes
                                             									creating a media primary key pair for the phones, delivering the
                                             									keys to the phones, and securing the delivery of the keys while
                                             									the keys are in transport. |
| Signaling encryption | Ensures that all SCCP and SIP signaling messages sent between
                                             					 the phone and the Cisco Unified Communications Manager server are encrypted. |
| Certificate Authority Proxy Function (CAPF) | Implements parts of the certificate generation procedure that
                                             					 are too processing-intensive for the phone, and interacts with the phone for
                                             					 key generation and certificate installation. The CAPF can be configured to
                                             					 request certificates from customer-specified certificate authorities on behalf
                                             					 of the phone, or it can be configured to generate certificates locally. |
| Security profiles | Defines whether the phone is nonsecure, authenticated,
                                             					 encrypted, or protected. |
| Encrypted configuration files | Ensures the privacy of phone configuration files. |
| Optional disabling of the web server functionality for a phone | Prevents access to a phone web page that displays a variety of
                                             					 operational statistics for the phone. |
| Phone hardening | The following is an additional security option that you control from Cisco
                                             					 Unified Communications Manager: Disabling access
                                                   						to web pages for a phone |
| 802.1X Authentication | Defines the use of 802.1X authentication to request and gain
                                             					 access to the network. |
| Voice Quality Metrics |
| MOS LQK | Objective estimate of the Mean Opinion Score (MOS) for
                                             					 Listening Quality (LQK) that ranks audio quality from 5 (excellent) to 1 (bad).
                                             					 This score is based on audible-concealment events due to a frame loss in the
                                             					 preceding 8 seconds of the voice stream. Note The MOS LQK score can vary based on the type of codec that
                                                         						the CiscoUnifiedIPPhone uses. | Note | The MOS LQK score can vary based on the type of codec that
                                                         						the CiscoUnifiedIPPhone uses. |
| Note | The MOS LQK score can vary based on the type of codec that
                                                         						the CiscoUnifiedIPPhone uses. |
| Avg MOS LQK | Average MOS LQK score for the entire voice stream. |
| Min MOS LQK | Lowest MOS LQK score from the start of the voice stream. |
| Max MOS LQK | Baseline or highest MOS LQK score from the start of the voice
                                             					 stream. The following codecs provide the corresponding maximum MOS LQK
                                             					 scores under normal conditions with no frame loss: G.711: 4.5 G.728/iLBC: 3.9 G729A/AB: 3.7 |
| MOS LQK Version | Version of the Cisco-proprietary algorithm used to calculate
                                             					 the MOS LQK scores. |

| Note | The MOS LQK score can vary based on the type of codec that
                                                         						the CiscoUnifiedIPPhone uses. |
|---|---|

| Note | Connections between two phones support protected calling. Some features, such as conference calling and shared lines, are
                                          not
                                          		  available when protected calling is configured. Protected calls are not
                                          		  authenticated. |
|---|---|

| Note | Connections between two phones support protected calling. Some features, such as conference calling and shared lines are not
                                                available when protected calling is configured. |
|---|---|

| Initiator’s phone security level | Feature used | Call security level | Results of action |
|---|---|---|---|
| Nonsecure | cBarge | Encrypted call | Call barged and identified as nonsecure call |
| Secure (encrypted) | cBarge | Authenticated call | Call barged and identified as authenticated call |
| Secure (authenticated) | cBarge | Encrypted call | Call barged and identified as authenticated call |
| Nonsecure | cBarge | Authenticated call | Call barged and identified as nonsecure call |

| Initiator’s phone security level | Feature used | Security level of participants | Results of action |
|---|---|---|---|
| Nonsecure | Conference | Encrypted or authenticated | Nonsecure conference bridge Nonsecure conference |
| Secure (encrypted or authenticated) | Conference | At least one member is nonsecure | Nonsecure conference |
| Secure (encrypted) | Conference | All participants are encrypted | Secure encrypted level conference |
| Secure (authenticated) | Conference | All participants are encrypted or authenticated | Secure authenticated level conference |
| Nonsecure | cBarge | All participants are encrypted | Conference changes to nonsecure |
| Nonsecure | Meet Me | Minimum security level is encrypted | Initiator receives the message Does not meet Security Level , and the call rejected. |
| Secure (encrypted) | Meet Me | Minimum security level is authenticated | Conference accepts encrypted and authenticated calls |
| Secure (encrypted) | Meet Me | Minimum security level is nonsecure | Only secure conference bridge available and used Conference accepts all calls |

| Note | Only Cisco Unified IP Phone 6911 has a PC port. |
|---|---|

| Step 1 | Gather the following information about the phone: Phone Model MAC address Physical location of the phone Name or user ID of phone user Device pool Partition, calling search space, and location information Associated directory number (DN) to assign to the phone Cisco UnifiedCommunications Manager user to associate with
                                                      					 the phone Provides list of configuration requirements for setting up phones. For more information, see the "CiscoUnified IP Phones" chapter in the Cisco Unified Communications Manager System Guide and
                                                				see Telephony Features Available for Cisco Unified IP Phone . |
|---|---|
| Step 2 | Verify that you have sufficient unit licenses for your phone. For
                                             			 more information, see the "License Unit Report" chapter in the Cisco Communications Manager Administration Guide . |
| Step 3 | Add and configure the phone by completing the required fields in
                                             			 the Phone Configuration window. An asterisk (*) next to the field name indicates a required field for example, MAC address
                                             			 and device pool. The phone with the  default settings gets added to the Cisco
                                                				Unified Communications Manager database. For more information, see the "Cisco Unified IP Phone Configuration" chapter in
                                                				the Cisco Communications Manager Administration Guide . For information about Product Specific Configuration fields, see ? Button Help in the 
                                                				Phone Configuration window. Note If you want to add both the phone and user to the Cisco Unified
                                                            				  Communications Manager database at the same time, see the "User/Phone Add Configuration" chapter in the Cisco Communications Manager Administration Guide . | Note | If you want to add both the phone and user to the Cisco Unified
                                                            				  Communications Manager database at the same time, see the "User/Phone Add Configuration" chapter in the Cisco Communications Manager Administration Guide . |
| Note | If you want to add both the phone and user to the Cisco Unified
                                                            				  Communications Manager database at the same time, see the "User/Phone Add Configuration" chapter in the Cisco Communications Manager Administration Guide . |
| Step 4 | Add and configure directory numbers (lines) on the phone by
                                             			 completing the required fields in the Directory Number Configuration window.
                                             			 An asterisk (*) next to the field name indicates a required field  for
                                             			 example, directory number and presence group. For more information, see the "Directory Number Configuration" chapter in the Cisco Unified Communications Manager Administration
                                                   				  Guide and see Telephony Features Available for Cisco Unified IP Phone . |
| Step 5 | Add user information by configuring required fields. An asterisk (*) next to the field name indicates a required field for
                                             example, User ID and last name. Note Assign a password (for User Options web pages) and PIN (for
                                                               					 accessing the Network Menu from  the Interactive Voice Response [IVR]). Adds user information to the global directory for Cisco
                                                				UnifiedCommunications Manager (Unified CM). For more information, see the "End User Configuration" chapter in the Cisco Unified Communications Manager Administration
                                                   				  Guide and see Add Users to Cisco Unified Communications Manager . Note If you want to add both the phone and user to the Cisco
                                                               					 Unified Communications Manager database at the same time, see the "User/Phone Add Configurations" chapter in the Cisco Unified Communications Manager Administration
                                                                  						Guide . | Note | Assign a password (for User Options web pages) and PIN (for
                                                               					 accessing the Network Menu from  the Interactive Voice Response [IVR]). | Note | If you want to add both the phone and user to the Cisco
                                                               					 Unified Communications Manager database at the same time, see the "User/Phone Add Configurations" chapter in the Cisco Unified Communications Manager Administration
                                                                  						Guide . |
| Note | Assign a password (for User Options web pages) and PIN (for
                                                               					 accessing the Network Menu from  the Interactive Voice Response [IVR]). |
| Note | If you want to add both the phone and user to the Cisco
                                                               					 Unified Communications Manager database at the same time, see the "User/Phone Add Configurations" chapter in the Cisco Unified Communications Manager Administration
                                                                  						Guide . |
| Step 6 | Associate a user to a user group. Assigns users a common list of
                                             			 roles and permissions that apply to all users in a user group. Administrators
                                             			 can manage user groups, roles, and permissions to control the level of access
                                             			 (and, therefore, the level of security) for system users. Note For end users to access Cisco Unified CM User Options, you must
                                                            				  add users to the standard Cisco CCM End Users group. For more information, see the following sections in the Cisco Unified Communications Manager Administration
                                                   				  Guide : End User Configuration Settings section in
                                                      					 the "End User Configuration" chapter. Adding Users to a User Group section in the "User Group Configuration" chapter. | Note | For end users to access Cisco Unified CM User Options, you must
                                                            				  add users to the standard Cisco CCM End Users group. |
| Note | For end users to access Cisco Unified CM User Options, you must
                                                            				  add users to the standard Cisco CCM End Users group. |
| Step 7 | Associate a user with a phone. Provides
                                             			 users with control over their phone for actions such as forwarding calls or adding
                                             			 speed-dial numbers or services. Note Some phones, such as those in conference rooms, do not have an
                                                            				  associated user. For more information, see  the Associating Devices to an
                                                				  End User section in the "End User Configuration" chapter in the Cisco Unified Communications Manager Administration
                                                   				  Guide . | Note | Some phones, such as those in conference rooms, do not have an
                                                            				  associated user. |
| Note | Some phones, such as those in conference rooms, do not have an
                                                            				  associated user. |

| Note | If you want to add both the phone and user to the Cisco Unified
                                                            				  Communications Manager database at the same time, see the "User/Phone Add Configuration" chapter in the Cisco Communications Manager Administration Guide . |
|---|---|

| Note | Assign a password (for User Options web pages) and PIN (for
                                                               					 accessing the Network Menu from  the Interactive Voice Response [IVR]). |
|---|---|

| Note | If you want to add both the phone and user to the Cisco
                                                               					 Unified Communications Manager database at the same time, see the "User/Phone Add Configurations" chapter in the Cisco Unified Communications Manager Administration
                                                                  						Guide . |
|---|---|

| Note | For end users to access Cisco Unified CM User Options, you must
                                                            				  add users to the standard Cisco CCM End Users group. |
|---|---|

| Note | Some phones, such as those in conference rooms, do not have an
                                                            				  associated user. |
|---|---|

| Note | Upgrade the phone with the current firmware image before you install
                                          		  the phone. For information about upgrading, see the Readme file for your
                                          		  phone, located at: http://tools.cisco.com/support/downloads/go/Redirect.x?mdfid=278875240 For instructions on upgrading the firmware, see the Release Notes,
                                          		  located at: http://www.cisco.com/en/US/products/ps10326/prod_release_notes_list.html |
|---|---|

| Step 1 | Choose the power source for the phone: Power over Ethernet (PoE) External power supply Determines how the phone receives power. For more information, see Cisco Unified IP Phone Power . |
|---|---|
| Step 2 | Assemble the phone, adjust phone placement, and connect the
                                             			 network cable. Locates and installs the phone in the network. See Install Cisco Unified IP Phone . See Footstand . |
| Step 3 | Monitor the phone startup process. Associates directory numbers to
                                             			 the phone and verifies that phone is configured properly. See Phone Startup Verification . |
| Step 4 | If you are configuring the network settings on the phone, you can
                                             			 set up an IP address for the phone by either using DHCP or manually entering an
                                             			 IP address. Using DHCP Verify that the phone has DHCP enabled using  the IVR. You can
                                                            					 set an alternate TFTP server by entering the IP address for the TFTP when prompted by
                                                            					 the IVR. Note Consult with the network administrator to determine whether
                                                                        						you need to assign an alternative TFTP server instead of using the TFTP server
                                                                        						assigned by DHCP. Without DHCP Verify that the phone has DHCP disabled using  the IVR. You
                                                            					 must then configure the IP address, subnet mask, TFTP server, and default
                                                            					 router locally by using the IVR on the phone. For more information, see Network Settings and Cisco Unified IP Phone Network Settings Setup . | Note | Consult with the network administrator to determine whether
                                                                        						you need to assign an alternative TFTP server instead of using the TFTP server
                                                                        						assigned by DHCP. |
| Note | Consult with the network administrator to determine whether
                                                                        						you need to assign an alternative TFTP server instead of using the TFTP server
                                                                        						assigned by DHCP. |
| Step 5 | Set up security on the phone. Provides protection against data tampering threats and identity
                                                				theft of phones. For more information, see Cisco Unified IP Phone Security . |
| Step 6 | Make calls with the Cisco Unified IP Phone. Verifies that the
                                             			 phone and features work correctly. For more information, see Cisco Unified IP Phone 6901 and 6911 User Guide for Cisco Unified Communications Manager (SCCP and SIP) . |
| Step 7 | Provide information to end users about how to use their phones and
                                             			 how to configure their phone options. Ensures that users have adequate information to successfully use
                                                				their Cisco UnifiedIPPhones. See Internal Support Web Site |

| Note | Consult with the network administrator to determine whether
                                                                        						you need to assign an alternative TFTP server instead of using the TFTP server
                                                                        						assigned by DHCP. |
|---|---|

| User Guide | Administration and System Guides |
|---|---|
| Auto Barge | cBarge |
| Message Indicators | Message Waiting Indicator (MWI) or Message Waiting Lamp |
| Voice mail system | Voice messaging system |