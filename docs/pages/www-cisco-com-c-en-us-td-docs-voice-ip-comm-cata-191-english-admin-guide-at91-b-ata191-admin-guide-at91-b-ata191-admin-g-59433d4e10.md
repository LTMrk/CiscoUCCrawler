---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-191-english-admin-guide-at91-b-ata191-admin-guide-at91-b-ata191-admin-g-59433d4e10
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/191/english/admin-guide/at91_b_ata191-admin-guide/at91_b_ata191-admin-guide_chapter_00.html
retrieved_at: 2026-08-22T01:05:01.486852+00:00
---

Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager

# Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager

Updated: August 15, 2025

Chapter: Cisco ATA 191 Analog Telephone Adapter Overview

## Chapter: Cisco ATA 191 Analog Telephone Adapter Overview

# Cisco ATA 191 Analog Telephone Adapter Overview

## Your Analog Telephone Adapter

The ATA 191 analog telephone adapter is a telephony-device-to-Ethernet adapter that allows regular analog phones to operate
                              on IP-based telephony networks. The ATA 191 supports two voice ports, each with an independent phone number. The ATA 191 also
                              has an RJ-45 10/100BASE-T data port.

### Session Initiation Protocol

Session Initiation Protocol (SIP) is the Internet Engineering Task Force (IETF) standard for real-time calls and conferencing
                              over Internet Protocol (IP). SIP is an ASCII-based, application-layer control protocol (defined in RFC3261). It is used to
                              establish, maintain, and terminate multimedia sessions or calls between two or more endpoints.

Like other Voice over IP (VoIP) protocols, SIP is designed to address the functions of signaling and session management within
                              a packet telephony network. Signaling allows call information to be carried across network boundaries. Session management
                              is used to control the attributes of an end-to-end call.

SIP for the ATA 191 is compliant with RFC2543.

#### SIP Capabilities

Session Initiation Protocol (SIP) provides these capabilities:

Determines the availability of the target endpoint. If the target endpoint is unavailable, SIP determines whether the called
                                          party is already on the phone or didn't answer in the allotted number of rings. SIP then returns a message indicating why
                                          the target endpoint was unavailable.

Determines the location of the target endpoint. SIP supports address resolution, name mapping, and call redirection.

Determines the media capabilities of the target endpoint. Using the Session Description Protocol (SDP), SIP determines the
                                          lowest level of common services between endpoints. Conferences are established using only the media capabilities that all
                                          endpoints support.

Establishes a session between the originating and target endpoint. If the call can be completed, SIP establishes a session
                                          between the endpoints. SIP also supports midcall changes, such as adding another endpoint to the conference or changing the
                                          media characteristic or codec.

Handles the transfer and termination of calls. SIP supports the transfer of calls from one endpoint to another. During a call
                                          transfer, SIP establishes a session between the transferee and a new endpoint (specified by the transferring party). SIP also
                                          terminates the session between the transferee and the transferring party. At the end of a call, SIP terminates the sessions
                                          between all parties. Conferences can consist of two or more users and can be established using multicast or multiple unicast
                                          sessions.

#### SIP Components

SIP is a peer-to-peer protocol. The peers in a session are called User Agents (UAs). A user agent can function in one of these
                                    roles:

User agent client (UAC)—A client application that initiates the SIP request.

User agent server (UAS)—A server application that contacts the user when a SIP request is received and returns a response
                                          on behalf of the user.

Typically, a SIP endpoint is capable of functioning as both a UAC and a UAS, but functions only as one or the other per transaction.
                                    Whether the endpoint functions as a UAC or a UAS depends on the UA that initiated the request.

From an architectural standpoint, the physical components of a SIP network can also be grouped into two categories—Clients
                                    and servers. The following figure shows the architecture of a SIP network.

SIP servers can interact with other application services, such as Lightweight Directory Access Protocol (LDAP) servers, a
                                                database application, or an extensible markup language (XML) application. These application services provide back-end services
                                                such as directory, authentication, and billable services.

##### SIP Clients

SIP clients include:

Gateways—Provide call control. Gateways provide many services, the most common being a translation function between SIP conferencing
                                             endpoints and other terminal types. This function includes translation between transmission formats and between communications
                                             procedures. In addition, the gateway also translates between audio and video codecs and performs call setup and clearing on
                                             both the LAN side and the switched-circuit network side.

Phones—Can act as either a UAS or UAC. The ATA 191 can initiate SIP requests and respond to requests.

##### SIP Servers

SIP servers include:

Proxy server—The proxy server is an intermediate device that receives SIP requests from a client and then forwards the requests
                                             on the client’s behalf. Proxy servers receive SIP messages and forward them to the next SIP server in the network. Proxy servers
                                             can provide functions such as authentication, authorization, network access control, routing, reliable request retransmission,
                                             and security.

Redirect server—Receives SIP requests, strips out the address in the request, checks its address tables for any other addresses
                                             that may be mapped to the address in the request, and then returns the results of the address mapping to the client. Redirect
                                             servers provide the client with information about the next hop or hops that a message should take, then the client contacts
                                             the next hop server or UAS directly.

Registrar server—Processes requests from UACs for registration of their current location. Registrar servers are often colocated
                                             with a redirect or proxy server.

### Cisco ATA 191  Hardware

The ATA 191 and ATA 192 are compact, easy to install devices.

The unit provides these connectors:

5V DC power connector.

Two RJ-11 FXS (Foreign Exchange Station) ports—Your ATA has two RJ-11 ports that work with any standard analog phone device.
                                       Each port supports either voice calls or fax sessions, and both ports can be used simultaneously.

One WAN network port—An RJ-45 10/100BASE-T data port to connect an Ethernet-capable device to the network.

The ATA network port performs autonegotiation for duplex and speed. It supports speeds of 10/100Mbps and full-duplex.

#### ATA 191 Top Panel

The top panel of your ATA has several LEDs that are used to show the device's status.

The following table describes the LEDs located on your ATA.

Item

Description

Power LED

Steady green: System booted up successfully and is ready for use.

Slow flashing green: System is booting up.

Fast flashing green three times, then repeats: System failed to boot up.

Fast flashing green: The LED behaviour occurs in the following situations:

System detects a factory reset.

A factory reset is performed successfully.

Off: Power is off.

Network LED

Flashing green: Data transmission or reception is in progress through the WAN port.

Off: No link.

Phone 1 LED

Phone 2 LED

Steady green: On hook.

Slow flashing green: Off hook.

Fast flashing green three times, then repeats: The analog device failed to register.

Fast flashing green: A factory reset is performed successfully.

Off: The port is not configured.

Problem Report Tool (PRT) Button

Press this button to create a problem report using the Problem Report Tool.

This is not a power button. When you press this button, a problem report is generated and uploaded to a server for the system
                                                            administrator.

Problem Report Tool (PRT) LED

Flashing amber: The PRT is preparing the data for the problem report.

Fast Flashing amber: The PRT is sending the problem report log to the PRT server.

Solid green for five seconds, then off: The PRT report was sent successfully.

Fast flashing green: A factory reset is performed successfully.

Flashing red: The PRT report failed. Press the PRT button to turn the LED off. Once it is off, another press triggers a new PRT report.

##### Problem Report Tool Button

The Problem Report Tool (PRT) button is on the ATA top panel. Press the PRT button, and a log file is prepared and uploaded
                                    to the server for troubleshooting your network.

You can instruct your analog phone users to press the PRT button on the ATA device to start the PRT log file process.

Set up the HTTP server to upload the PRT log file from the ATA.

Configure the customer support upload URL to best suit your needs, and apply it to the ATA.

#### ATA 191 Back Panel

The back panel of your ATA has several ports used to connect your device and to power it. The back panel also has the reset
                                    button for resetting the device to the factory settings.

The following table describes the ports that are located on the back panel of your ATA.

Port or Button

Description

RESET

To restart the ATA, use a paper clip or similar object to press this button briefly.

To restore the factory default settings, press and hold for 10 seconds.

The LED behaviour for the factory reset:

After you press and hold the button for about 10 seconds, the Power LED is fast flashing green.

After the factory reset is performed successfully, all LEDs are fast flashing green for about 5 seconds.

PHONE 1

Use an RJ-11 phone cable to connect an analog phone or fax machine.

PHONE 2

Use an RJ-11 phone cable to connect a second analog phone or fax machine.

NETWORK

Use an Ethernet cable to connect to the network.

DC 5V POWER

Use the provided power adapter to connect to a power source.

### Software Features

#### Secure Real-Time Transport Protocol

Secure Real-Time Transport Protocol secures voice conversations on the network and provides protection against replay attacks.

#### Fax Passthrough

Name Signaling Event (NSE) -based and re-INVITE-based passthrough provide transport of fax communications using the G.711a/u
                                    codec.

#### Transport Layer Security Protocol

Transport Layer Security (TLS) is a cryptographic protocol that secures data communications such as email on the Internet.
                                    TLS is functionally equivalent to Secure Sockets Layer (SSL).

#### T.38 Fax Relay

The T.38 fax relay feature enables devices to use fax machines to send files over the IP network. In general, when a fax is
                                    received, it is converted to an image, then sent to the T.38 fax device. When the target T.38 fax device receives this image,
                                    the device converts the image back to an analog fax signal.

T.38 fax relays configured with voice gateways decode or demodulate the fax signals before they are transported over IP. With
                                    the SIP call control protocol, the Session Description Protocol (SDP) entries in the initial SIP INVITE message indicate that
                                    T.38 fax relay is present. After the initial SIP INVITE message, the call is established to switch from voice mode to T.38
                                    mode. Cisco Unified Communications Administration allows you to configure a SIP profile that supports T.38 fax communication.

The ATA 191 only supports T38 Fax Relay Version 0 (G3).

#### Supported Voice Codecs

The ATA 191 supports these voice codecs:

G.711 mu-law

G.711 A-law

G.729a

G.729ab

Check your other network devices for the codecs they support.

#### Other Supported Protocols

The ATA supports these additional protocols:

802.1Q VLAN tagging

Cisco Discovery Protocol (CDP)

Domain Name System (DNS)

Dynamic Host Configuration Protocol (DHCP)

Internet Control Message Protocol (ICMP)

Internet Protocol (IP) v4 and IPv6

Link Layer Discovery Protocol (LLDP)

Secure Real-Time Transport Protocol (SRTP)

Transmission Control Protocol (TCP)

Trivial File Transfer Protocol (TFTP)

User Datagram Protocol (UDP)

Transport Layer Security (TLS)

Secure Socket Shell (SSH)

Network Time Protocol (NTP)

HyperText Transfer Protocol (HTTP)

#### Supported SIP Services

The following SIP services are supported on the ATA:

IP address assignment—DHCP-provided or statically configured

ATA 191 configuration by Cisco Unified Communications Manager configuration interface

VLAN configuration

Cisco Discovery Protocol (CDP)

Low-bit-rate codec selection

User authentication

Configurable tones (ringback tone, reorder tone, dialing tone, outside dialing tone, busy tone, call waiting tone)

Dial plan and PLAR

SIP Proxy Server redundancy

Privacy features

User-configurable, call waiting, permanent default setting

Comfort noise during silent period when using G.711u/a and G.729ab

Caller ID format

Ring frequency/voltage adjustment

Hookflash detection timing configuration

Type of Service (ToS) configuration for audio and signaling Ethernet packets

Debugging and diagnostic tools

#### Supported Call Services

The following call services are supported on the ATA:

IP address assignment—DHCP-provided or statically configured

ATA191 configuration by Cisco Unified Communications Manager configuration interface

VLAN configuration

Cisco Discovery Protocol (CDP)

Low-bit-rate codec selection

User authentication

Configurable tones (ringback tone, reorder tone, dialing tone, outside dialing tone, busy tone, call waiting tone)

Dial plan and PLAR

SIP Proxy Server redundancy

Privacy features

User-configurable, call waiting, permanent default setting

Comfort noise during silent period when using G.711u/a and G.729ab

Caller ID format

Ring frequency/voltage adjustment

Hookflash detection timing configuration

Type of Service (ToS) configuration for audio and signaling Ethernet packets

Debugging and diagnostic tools

#### 802.1X Authentication

Support for 802.1X authentication requires several components:

The ATA 191: The ATA initiates the request to access the network. The ATA contains an 802.1X supplicant. This supplicant allows
                                          network administrators to control the connectivity of ATAs to the LAN switch ports. The current release of the ATA 802.1X
                                          supplicant uses the EAP-FAST and EAP-TLS options for network authentication.

Cisco Secure Access Control Server (ACS) (or other third-party authentication server): The authentication server and the ATA
                                          must both be configured with a shared secret that authenticates the ATA.

A LAN switch supporting 802.1X: The switch acts as the authenticator and pass the messages between the ATA and the authentication
                                          server. After the exchange completes, the switch grants or denies the ATA access to the network.

You must perform the following actions to configure 802.1X.

Configure the other components before you enable 802.1X authentication on the ATA.

Configure Voice VLAN: Because the 802.1X standard does not account for VLANs, you should configure this setting based on the
                                          switch support.

Enabled: If you are using a switch that supports multidomain authentication, you can continue to use the voice VLAN.

Disabled: If the switch does not support multidomain authentication, disable the Voice VLAN and consider assigning the port
                                                to the native VLAN.

Currently, the ATA doesn't support the IPv6 network access through 802.1X authentication.

To check the status of the 802.1X authentication, use one of the following methods:

On the ATA web page, go to Status > Network Status > 802.1x authentication information .

On the phone connected to the ATA, use IVR number 803 .

#### Modem Standards

The ATA supports these modem standards:

V.90

V.92

V.44

K56Flex

ITU-T V.34 Annex 12

ITU-T V.34

V.32bis

V.32

V.21

V.22

V.23

#### Fax Services

The ATA 191 supports two modes of fax services:

Fax pass-through mode: Receiver-side Called Station Identification (CED) tone detection with automatic G.711A-law or G.711µ-law
                                          switching.

T.38 Fax Relay mode: The T.38 fax relay feature enables devices to use fax machines to send files over the IP network. In
                                          general, when a fax is received, it is converted to an image, then sent to the T.38 fax device. When the target T.38 fax device
                                          receives this image, the device converts the image back to an analog fax signal. T.38 fax relays configured with voice gateways
                                          decode or demodulate the fax signals before they are transported over IP.

Success of fax transmission depends on network conditions and fax modem response to these conditions. The network must have
                                                reasonably low network jitter, network delay, and packet loss rate.

#### Supported Methods

The ATA 191 supports these methods:

REGISTER

REFER

INVITE

BYE

CANCEL

NOTIFY

OPTIONS

ACK

SUBSCRIBE

For more information, see RFC3261, SIP: Session Initiation Protocol.

#### Supported ATA Call Features

SIP supplementary services are services that you can use to enhance your phone service.

The ATA supports these SIP supplementary services:

Caller ID

Call-waiting caller ID

Voice mail indication

Making a conference call

Call waiting

Call forwarding

Calling-line identification

Unattended transfer

Attended transfer

Shared Line

SpeedDial

Meet-Me Conference

Call Pickup/Group Call Pickup

Redial

Secure Call

C-Barge

#### Installation and Configuration Overview

The following basic steps are required to install and configure the ATA. The steps also make the ATA operational in a typical
                                 SIP environment where many ATAs are deployed.

Plan the network and the ATA configuration.

Install the Ethernet connection.

Install and configure the other network devices.

Install the ATA but do not power it up yet.

Power up the ATA.

| Note | SIP for the ATA 191 is compliant with RFC2543. |
|---|---|

| Note | SIP servers can interact with other application services, such as Lightweight Directory Access Protocol (LDAP) servers, a
                                                database application, or an extensible markup language (XML) application. These application services provide back-end services
                                                such as directory, authentication, and billable services. |
|---|---|

| Note | The ATA network port performs autonegotiation for duplex and speed. It supports speeds of 10/100Mbps and full-duplex. |
|---|---|

| Item | Description |
|---|---|
| Power LED | Steady green: System booted up successfully and is ready for use. Slow flashing green: System is booting up. Fast flashing green three times, then repeats: System failed to boot up. Fast flashing green: The LED behaviour occurs in the following situations: System detects a factory reset. To perform a factory reset, press and hold the RESET button for about 10 seconds. A factory reset is performed successfully. Off: Power is off. |
| Network LED | Flashing green: Data transmission or reception is in progress through the WAN port. Off: No link. |
| Phone 1 LED Phone 2 LED | Steady green: On hook. Slow flashing green: Off hook. Fast flashing green three times, then repeats: The analog device failed to register. Fast flashing green: A factory reset is performed successfully. Off: The port is not configured. |
| Problem Report Tool (PRT) Button | Press this button to create a problem report using the Problem Report Tool. Note This is not a power button. When you press this button, a problem report is generated and uploaded to a server for the system
                                                            administrator. | Note | This is not a power button. When you press this button, a problem report is generated and uploaded to a server for the system
                                                            administrator. |
| Note | This is not a power button. When you press this button, a problem report is generated and uploaded to a server for the system
                                                            administrator. |
| Problem Report Tool (PRT) LED | Flashing amber: The PRT is preparing the data for the problem report. Fast Flashing amber: The PRT is sending the problem report log to the PRT server. Solid green for five seconds, then off: The PRT report was sent successfully. Fast flashing green: A factory reset is performed successfully. Flashing red: The PRT report failed. Press the PRT button to turn the LED off. Once it is off, another press triggers a new PRT report. |

| Note | This is not a power button. When you press this button, a problem report is generated and uploaded to a server for the system
                                                            administrator. |
|---|---|

| Port or Button | Description |
|---|---|
| RESET | To restart the ATA, use a paper clip or similar object to press this button briefly. To restore the factory default settings, press and hold for 10 seconds. The LED behaviour for the factory reset: After you press and hold the button for about 10 seconds, the Power LED is fast flashing green. After the factory reset is performed successfully, all LEDs are fast flashing green for about 5 seconds. |
| PHONE 1 | Use an RJ-11 phone cable to connect an analog phone or fax machine. |
| PHONE 2 | Use an RJ-11 phone cable to connect a second analog phone or fax machine. |
| NETWORK | Use an Ethernet cable to connect to the network. |
| DC 5V POWER | Use the provided power adapter to connect to a power source. |

| Note | Currently, the ATA doesn't support the IPv6 network access through 802.1X authentication. |
|---|---|

| Note | Success of fax transmission depends on network conditions and fax modem response to these conditions. The network must have
                                                reasonably low network jitter, network delay, and packet loss rate. |
|---|---|