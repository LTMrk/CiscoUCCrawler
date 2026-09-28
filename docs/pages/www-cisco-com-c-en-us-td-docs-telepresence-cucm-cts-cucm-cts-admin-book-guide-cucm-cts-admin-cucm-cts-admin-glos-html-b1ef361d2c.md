---
doc_id: www-cisco-com-c-en-us-td-docs-telepresence-cucm-cts-cucm-cts-admin-book-guide-cucm-cts-admin-cucm-cts-admin-glos-html-b1ef361d2c
source_url: https://www.cisco.com/c/en/us/td/docs/telepresence/cucm_cts/cucm_cts_admin_book/guide/cucm_cts_admin/cucm_cts_admin_glos.html
retrieved_at: 2026-08-17T00:10:16.374652+00:00
---

Cisco Unified Communications Manager Configuration Guide for the Cisco TelePresence System

# Cisco Unified Communications Manager Configuration Guide for the Cisco TelePresence System

Updated: April 15, 2014

Chapter: Glossary

## Chapter: Glossary

### Glossary

OL-21851-01

ACU

Auxiliary Control Unit. Provides the ability to conserve energy by powering the lights, projector, and optional peripherals for Cisco TelePresence systems on and off. The ACU is controlled by the CTS Administrator.

ad hoc meeting

Non-scheduled, administrator-initiated, dial-out meeting. A meeting scheduler or administrator initiates the meeting through the Cisco TelePresence Multipoint Switch (CTMS) administration interface by listing the telephone number of the rooms which will participate in the multipoint meeting. See static meeting .

AES

Advanced Encryption Standard. An encryption standard comprising three block ciphers, AES-128, AES-192, and AES-256, adopted from a larger collection originally published as Rijndael. Each AES cipher has a 128-bit block size, with key sizes of 128, 192 and 256 bits, respectively.

Auto Answer

A phone set to automatically answer an inbound call. Use the Auto Answer feature in Cisco Unified Communications Manager. Activating this option or button causes the speaker phone to go off hook automatically when an incoming call is received.

Auto Collaborate

Cisco TelePresence simple information sharing using a powerful “Auto Collaborate” feature that allows any object, document, or PC application to be displayed in a plug-and-play fashion. Auto Collaborate enables you to share images instantly in multiple locations by plugging in a laptop computer or high-definition ceiling document camera. The Cisco TelePresence 3000 Series built-in projector automatically displays images from the most recently activated device.

Ceiling cameras are perfect for capturing images of objects that are too valuable to ship, or cannot easily be copied or sent electronically. Cisco recommends and document cameras made by WolfVision, specifically the WolfVision Visualizer. This is a special live-camera system designed for picking up any object on a working surface with perfect illumination and depth of focus. All types of objects (e.g., photos, books, brochures, transparencies, slides, or three-dimensional objects) can be picked up quickly and easily, and meeting participants can use a wireless remote to control light, zoom, or focus.

Cisco TelePresence 3000 and 1000 systems support the Auto Collaborate capability, and meeting organizers can project content in multiple locations, including above or below displays, or on the side of a room.

A/V Expansion Box

Audio/video extension unit. Required if your system uses an Auxiliary Control Unit ( ACU ).

AXL

Administrative XML. SOAP -based protocol that enables remote provisioning of Unified CM. Cisco AXL Web Service allows Unified CM to be updated from Architecture for Voice, Video and Integrated Data (AVVID) client-based applications that use AXL.

bit rate

Speed at which bits are transmitted, usually expressed in bits per second.

black screen codes

System status information messages that appear on the main display screen before your meeting starts and while the screen is still black. For example, “Please wait, you are the first meeting participant.”

For more information, see the Cisco TelePresence System User Guide .

BPDU

Bridge Protocol Data Units. Data frames that exchange information about bridge IDs and root path costs. A bridge sends a BPDU frame using the unique MAC address of the port as a source address, and a destination address of the Spanning Tree Protocol (STP) multicast address 01:80:C2:00:00:00.

CCP

The Conference Control Protocol (CCP) is an interface between the CTS and the CTMS that controls the following elements of a Cisco TelePresence conference:

- Locks a meeting.

- Sets the switching policy.

- Sends end meeting notifications.

- Obtains the roster list.

- Requests to meeting to be extended.

- Sends black screen messages. See black screen codes .

- Allows you to specify default outbound http proxy route.

CIF

Common Intermediate Format. A video standard that provides 352x288 pixels, or picture elements, of video resolution.

Cisco CTI Manager

CTI Manager is required in a cluster for applications that use TAPI or JTAPI Computer Telephony Integration (CTI). The CTI Manager acts as a broker between the CTI application and the Cisco Unified Communications Manager Service. It provides authentication of the application and enables control or monitoring of authorized devices. The CTI application communicates with a primary CTI Manager and, in the event of a failure, will switch to a backup CTI Manager. The CTI Manager should be enabled only on call processing subscribers, thus allowing for a maximum of eight CTI Managers in a cluster. Cisco recommends that you load-balance CTI applications across the various CTI Managers in the cluster to provide maximum resilience, performance, and redundancy.

Cisco TelePresence TX Series

The Cisco TelePresence TX Series high-definition presentation capabilities and simple controls on a touch display help make your meeting as immersive and natural as possible. See Immersive Telepresence Endpoints .

Cisco Unified Communications Manager

Unified CM. Application that extends enterprise telephony features and capabilities to packet telephony network devices such as IP phones and multimedia applications. Open telephony application interfaces make possible services such as multimedia conferencing and interactive multimedia response systems.

codec

The “brain” of the CTS. The primary codec connects with the network and Cisco Unified Communications Manager (Cisco Unified CM) to perform call management functions for the system. The secondary codec performs processing for the system elements that are attached to them. The optional presentation codec the document camera (if present), auxiliary displays, and works with an auxiliary control unit and audio extension unit for additional audio/video applications. The number and type of codecs your system uses depends on which CTS device you are using.

CTMS

Cisco TelePresence Multipoint Switch . Support for voice-activated switching in up to 48 locations in a single meeting across many endpoint s.

CTRS

Cisco TelePresence Recording Server . Providing HD studio recording capabilities in existing Cisco TelePresence rooms. Recordings can be archived automatically on a schedule or transferred to a digital content management system. The CTRS can deliver Cisco TelePresence recordings to any video-enabled device including PCs, smartphones, and digital signs. CTRS runs on the same reliable Media Convergence Server platform as Cisco TelePresence Multipoint Switch and Cisco TelePresence Manager.

CTS device

Cisco TelePresence System (CTS) device: CTS 500, CTS 1000, CTS 1100, CTS 1300, CTS 3000 series, CTS 3200 series.

CTS-Manager

Cisco TelePresence Manager . Software application that schedules and manages Cisco TelePresence calls using common enterprise groupware such as Microsoft Exchange and Lotus Notes.

CTS Manager PreQualification Assistant

The CTS-Man PreQualification Assistant ensures that your pre-configuration set-up is performed correctly. The data that is entered into the Tool Test Configuration forms that are used to verify connections to the servers and to get data from them to be used to configure CTS-Man.

CUCM

Cisco Unified Communications Manager (Unified CM).

default gateway

A router on a computer network that serves as an access point to another network.

DES

Data Encryption Standard. A block cipher (a form of shared secret encryption) that was selected by the National Bureau of Standards as an official Federal Information Processing Standard (FIPS) for the United States in 1976 and which has subsequently enjoyed widespread use internationally. It is based on a symmetric-key algorithm that uses a 56-bit key.

DHCP

Dynamic Host Configuration Protocol. Provides a mechanism for allocating IP addresses dynamically so that addresses can be reused when hosts no longer need them.

Directory

Button or Softkey on the Cisco Unified IP Phone that is configured from the Administration and User interfaces. Gives users access to several directories including the Corporate Directory and the Personal Directory.

display screen animation

System information icons that may be displayed on the Cisco TelePresence System (CTS) main display screen. System information includes call connection status alerts, meeting alerts, and maintenance alerts. These alerts fade from one state to another to show the status of the system.

display screen icon

System information icons that may be displayed on the Cisco TelePresence System (CTS) display screen. System information includes call connection status alerts, meeting alerts, and maintenance alerts.

DMP

Digital Media Player. Cisco Digital Media Players are highly-reliable, IP-based endpoints that can play high-definition live and on-demand video, motion graphics, web pages, and dynamic content on digital displays, usually an LCD Professional Series display or any other directly attached television screen, monitor, or projector (analog or digital, standard-definition or high-definition) that shows media to an audience. There is an extra input connector for the Digital Media Player (DMP) on your Cisco TelePresence device. See the Cisco Digital Media Players home page on Cisco.com.

See also LCD .

DN

Directory number.

DNS

Domain Name System. Domain in which the phone resides. Primary Domain Name System (DNS) server (DNS Server 1) and optional backup DNS servers (DNS Server 2-5) used by the phone. Redundant DNS servers that point to the Cisco Unified CM are configured and listed on the in-room phone by navigating to Settings > Network Configuration > IPv4 Configuration.

DSCP

Differentiated Services Code Point. A field in the header of IP packets for packet classification purposes. DSCP for TelePresence Calls field description: This parameter specifies the DSCP value for Cisco TelePresence calls. This parameter is set to the default value unless a Cisco support engineer instructs otherwise. This is a required field, if present on your system. Default: CS4(precedence 4) DSCP (100000) and is selectable per device.

DVI

DVI cables are used for direct digital connections between source video (namely, video cards) and LCD monitors. Plugs into desktop, PC, or laptop docking station. See also VGA .

enbloc dialing

Allows you to compose and edit the number to dial on your phone's display before it is sent to the phone system to be dialed.

endpoint

Cisco TelePresence System (CTS) endpoint. The combination of hardware and software that comprise a Cisco TelePresence System. The hardware for an endpoint includes a Cisco Unified IP Phone 7900 Series, one or more large-screen meeting displays, plus presentation devices, cameras, microphones, speakers, and in some models, lighting systems.

EWS

Exchange Web Services. Managed API that provides an intuitive interface for developing client applications that use Exchange Web Services. The EWS Managed API provides unified access to Microsoft Exchange Server resources, while using Microsoft Office Outlook–compatible business logic. The EWS Managed API communicates with the Exchange Client Access server by means of EWS SOAP messages.

extranet

An extranet is a private network that uses Internet protocols and network connectivity. An extranet can be viewed as part of a company's intranet that is extended to users outside the company, usually via the Internet. It has also been described as a “state of mind” in which the Internet is perceived as a way to do business with a selected set of other companies (business-to-business, B2B), in isolation from all other Internet users. In contrast, business-to-consumer (B2C) models involve known servers of one or more companies, communicating with previously unknown consumer users.

An extranet can be understood as an intranet mapped onto the public Internet or some other transmission system not accessible to the general public, but managed by more than one company's administrator(s). For example, military networks of different security levels may map onto a common military radio transmission system that never connects to the Internet. Any private network mapped onto a public one is a virtual private network (VPN), often using special security protocols.

Favorites

The Favorites softkey and screen on the CTS Cisco Unified IP Phone.

fluorescent lamp

A lamp that uses electricity to excite mercury vapor in a gas that results in an energy that produces short-wave ultraviolet light. This light then causes a phosphor to fluoresce, producing visible light. Sources of light in most rooms are either incandescent light bulbs that use tungsten filaments or fluorescent lights. Each of these light sources, and the amount of light in terms of lumens or watts, produces a different color temperature. This color temperature is sometimes expressed using terms such cool, warm, or daylight, but can be expressed more precisely in kelvins (K) as a numeric value. When adjusting the images on the display screens for the Cisco TelePresence system, you must take the color temperature of the ambient light in the room into consideration.

full duplex mode

Transmission of data in two directions simultaneously.

guest operating system

An operating system that is installed and run in a virtual machine . In the Cisco TelePresence environment, the CTS Manager, CTMS, and CTRS are guest operating systems. Before you can install the guest operating system, you must obtain the installation media for the operating system and configure the virtual machine to use the CD/DVD drive to access the installation media. See VMware .

gzip

GNU zip. Software application used for file compression.

half duplex mode

Transmission of data in one direction at a time.

HD

High definition display. High-definition video or HD video refers to any video system of higher resolution than standard-definition (SD) video, and most commonly involves display resolutions of 1280×720 pixels (720p) or 1920×1080 pixels (1080i/1080p).

HDMI

Document camera input and cable.

IDR

An IDR frame is a special kind of I frame used in MPEG-4 AVC encoding. IDR frames can be used to create Advanced Video Coding (AVC) streams, which can be easily edited.

Immersive Telepresence Endpoints

CTS 3210, CTS 1300, Cisco TelePresence T3. Provides an immersive, interactive in-person experience. See also personal system .

incandescent lamp

A lamp that allows an electric current to pass through a thin filament, heating it and causing it to emit light. Sources of light in most rooms are either incandescent light bulbs that use tungsten filaments or fluorescent lights. Each of these light sources, and the amount of light in terms of lumens or watts, produces a different color temperature. This color temperature is sometimes expressed using terms such cool, warm, or daylight, but can be expressed more precisely in kelvins (K) as a numeric value. When adjusting the images on the display screens for the Cisco TelePresence system, you must take the color temperature of the ambient light in the room into consideration.

Internet model (free path)

The Internet model is an unsecured “free path” model of packet delivery: Packets are delivered in any way possible and each uncontrolled router on the way to the destination handles how to deliver the packet to the next stop. See VPN model (fixed path) .

IP address

A device identifier on a TCP/IP network.

jitter

jitter call

jitter period

Variation in packet transit delay caused by queuing, contention, and serialization effects on the path through the network. In general, higher levels of jitter are more likely to occur on either slow or heavily congested links.

Jitter call is the average jitter measurement per call. Shown in the Jitter/Call output field as part of Per Call Jitter and Packet Loss Reporting.

Jitter period is the interval between two times of maximum effect (or minimum effect) of a signal characteristic that varies regularly with time. Jitter frequency, the more commonly quoted figure, is its inverse.

The CTS measures jitter every 10 seconds. The Jitter/Period field reports the jitter measurement for the last 10-second period.

The CTS calculates jitter as the sum of the maximum deviation (both late and early) from the expected arrival time as given by the frame period. CMA computes frame jitter based on the arrival time of the last packet of a frame.

LCD

Liquid crystal display. The LCD display is an accessory for the Cisco Digital Media Player (DMP) for use in your digital signage network or your enterprise TV network. It is used for displaying video, images, or computer data during a Cisco TelePresence meeting. See the Cisco LCD Professional Series Displays home page on Cisco.com for more information.

See also DMP .

LED

Light-emitting diode. Indicators on the CTS that determine whether the user is sitting within camera range.

light temperature

A theoretical means of describing visible light that is determined by comparing its hue with a heated black-body radiator. The lamp’s color temperature is the temperature in kelvins at which the heated black-body radiator matches the hue of the lamp.

Live Desk

The Live Desk is a person who has been assigned to a Cisco TelePresence endpoint to assist you with problems that may occur during a meeting. To connect to Live Desk, touch the Live Desk softkey. If a Live Desk has not been assigned to your Cisco TelePresence endpoint , the following message is displayed on your phone screen: “There is no Live Desk number configured”

If your system is running CTS software release 1.9.1 or later, you can configure Live Desk using the Live Desk field in Unified CM. For more information, refer to the Live Desk in Cisco Unified CM section of the Release Notes for Cisco TelePresence System Software Release 1.9 .

If your system is running CTS software release prior to 1.9.1, you can configure Live Desk in the Configure > Live Desks Window of the CTS-Manager Administration interface. Refer to the Cisco TelePresence Manager Installation and Configuration Guide on Cisco.com.

LTRP

Long Term Reference Picture.

MAC address

Media Access Control address. A hardware address that uniquely identifies each node of a network.

MD5

Message-Digest algorithm 5. Widely used cryptographic hash function with a 128-bit hash value. As an Internet standard (RFC 1321), MD5 has been employed in a wide variety of security applications, and is also commonly used to check the integrity of files. MD5 is not suitable for applications like SSL certificates or digital signatures that rely on this property. An MD5 hash is typically expressed as a 32 digit hexadecimal number.

Meeting Extension

Meeting Extension feature that can be used from the CTS Cisco Unified IP phone when MIDlets are configured. This feature provides an option on the CTS Cisco Unified IP phone to extend Cisco TelePresence meetings past their scheduled end time. Meeting participants may request to extend the scheduled meeting using the phone softkey options. CTS Manager Administrators can configure Meeting Extension settings using the Meeting Options tab on the CTS Manager System Configuration > Application Settings page.

MIDlets

Mobile Information Device Profile (MIDP). A Java application designed to run on resource-constrained devices such as phones, PDAs, intelligent appliances, and the like. A MIDlet (in J2ME) is similar to a Java Applet (in J2SE), but more specialized, efficient, and optimized for limited devices. MIDlets graphics and animation, multimedia, touchscreen, networking, persistent data storage, and provides excellent Look And Feel (LAF) integration with the host platform.

The Cisco Unified IP Phone uses MIDlets as part of the Cisco TelePresence System Enhanced Phone User Interface: MIDlets support CTS Cisco Unified IP phone features. Configure MIDlets in the Cisco Unified CM Administration interface for Cisco TelePresence.

See Configuring and Managing the Cisco Unified IP Phone for more information.

mixed mode

Cluster Security Mode field is set to 1 in the Configuration Settings for CTL Client in Cisco Unified CM Administration > System > Enterprise Parameters . To configure and verify cluster security mode, see the Verifying the Cisco Unified Communications Manager Security Mode section of the Cisco TelePresence Security Solutions Guide .

multipoint meeting

Multipoint is where you are able to connect more than two sites in one video conference. This normally requires a bridge, although some video conference units are also able to connect multiple sites.

MXE

Media eXperience Engine. The Cisco Media Experience Engine is a modular media processing system that provides interoperability between Cisco TelePresence and video conferencing devices, extending the reach of collaboration and communication within organizations. MXE provides 720p interoperability with video conferencing.

Configure MXE in CTS-Manager . See also Cisco TelePresence Firewall and Access List Considerations for support information for Cisco TelePresence.

nonce

A nonce value (a random number that digest authentication) is used to calculate the MD5 hash of the digest authentication password.

Non-permitted User

Cisco WebEx user role configured in the CTS Manager Administration interface. These users are not permitted to request Cisco WebEx; no Cisco WebEx meeting options are available to these users. See Permitted User .

One-Button-to-Push

Launches a call with Cisco TelePresence Manager. Cisco TelePresence Manager works with enterprise groupware software such as Microsoft Exchange and Lotus Notes to allow you to schedule Cisco TelePresence meetings just as you would a regular meeting. Enterprise groupware sends Cisco TelePresence Manager the meeting schedule, and the software pushes that information to the in-room phone for call launch. The “One-Button-to-Push” feature allows you to simply touch the meeting that is listed on the in-room IP phone to start a Cisco TelePresence meeting.

Participant List

A list of Cisco WebEx meeting participants displayed on the phone that are visible when you touch the Participant List softkey or the phone screen touch button on the fully configured CTS Cisco Unified Phone. This list is configured in Cisco Unified CM Display (Internal Caller ID) fields.

P-frame

An easily compressible video frame type. A video frame is compressed using different algorithms that allow varied amounts of data compression. These different algorithms for video frames are called picture types or frame types. The three major picture types used in the different video algorithms are I, P, and B.

Permitted User

Cisco WebEx user role configured in the CTS Manager Administration interface. These users are permitted to request Cisco WebEx for specific meetings using CTS Manager. See Non-permitted User .

personal system

Personal Cisco TelePresence System. The virtual, in-person experience of Cisco TelePresence directly into the private office. The CTS 500 and CTS 1000 are considered to be personal systems. See also Immersive Telepresence Endpoints .

PiP

Presentation-in-Picture. Data or graphics content sharing through an external monitor known as presentation-in-picture (PiP) format for space-constrained offices. Using the PiPCtrl softkey and options in the PiP control screen on your CTS Cisco Unified IP phone, you can toggle the position of the PiP between center, left, or right locations on the screen or change its size in relation to the meeting participant video input during a meeting.

PoE

Power over Ethernet.

point-to-point meeting

The direct connection of two sites in a video conference. This only works if both sites use the same type of connection (either IP or ISDN).

Premium User

Cisco WebEx user role configured in the CTS Manager Administration interface: Cisco WebEx is always on. Controlled on the CTS Manager LDAP configuration page.

presentation codec

The presentation codec provides 30 frames per second to support full-motion video presentations between Cisco TelePresence endpoints.

Presenter

Cisco WebEx user role configured in the CTS Manager Administration interface: A Presenter shares presentations, specific applications, or the entire desktop. The Presenter controls the annotation tools and can grant and revoke remote control over the shared applications and desktop to individual Attendees.

primary codec

The primary codec is the primary unit; it communicates with secondary units, sends and receives packets on the uplink network. It contains an onboard Gigabit Ethernet switch. For example, in a CTS 3000 or CTS 3200 system, the primary codec controls two secondary codecs as well as many system components and the graphical user interfaces (GUI). In a Cisco TelePresence 1000, it controls all system functions.

PCB

Printed circuit board.

RFC

Request for Comments. Document series used as the primary means for communicating information about the Internet. Some RFCs are designated by the IAB as Internet standards.

scheduled meeting

Multipoint TelePresence meetings are scheduled by end users using Microsoft Exchange or IBM Domino clients in the same manner that a point-to-point meeting is scheduled. Scheduled meetings require no CTMS administrator interaction. CTS Manager is a required component for scheduled meetings. It provides the interface between Microsoft Exchange or Lotus Domino and the CTMS, allowing the appropriate resources on the CTMS to be reserved for the multipoint meeting .

Scheduling API

Cisco TelePresence Scheduling API provides programmatic access to your organization's CTS-Manager using a simple, powerful, and secure application-programming interface for customers who are not using Microsoft Exchange or IBM Domino Notes. For developers this API allows groupware applications to utilize Cisco TelePresence Manager for scheduling Cisco TelePresence calls with resource reservations and One-Button-to-Push .

screen resolution

The fineness of detail that can be presented in the image on the CTS main display screen. Recommended screen resolution for Cisco TelePresence is 1024 x 768.

SD

Standard definition display. See HD .

secondary codec

Codecs that assist the primary codec in the large Cisco TelePresence 3000/3200 systems. Secondary codecs process audio and video signals and send them to the primary codec, which multiplexes the signals into separate, single RTP streams.

Show and Share

If your Cisco TelePresence network administrator has configured Cisco Show and Share as your enterprise video portal, you can immediately publish your recording or save a draft to Cisco Show and Share from the Cisco TelePresence Touch 12 or Cisco Unified IP phone. For more information on creating and viewing recordings, see the Cisco TelePresence System User Guide on Cisco.com that corresponds with your system’s software release.

single system

A Cisco TelePresence System featuring a single main display screen.

SHA

Secure Hash Algorithm. A set of cryptographic hash functions designed by the National Security Agency (NSA) and published by the NIST as a U.S. Federal Information Processing Standard. The three SHA algorithms are structured differently and are distinguished as SHA-0, SHA-1, and SHA-2.

SIP

Session Initiation Protocol. Protocol designed to signal the setup of voice and multimedia calls over IP networks.

SNMP

Simple Network Management Protocol. Network management protocol used almost exclusively in TCP/IP networks as a means to monitor and control network devices, and to manage configurations, statistics collection, performance, and security. See the Cisco TelePresence System Message Guide .

SOAP

Simple Object Access Protocol. XML-based protocol to let applications exchange information over HTTP.

SSCD

System Status Collection Daemon. The daemon gathers statistics about the system it is running on and stores this information. Those statistics can then be used to find current performance bottlenecks (performance analysis, for example) and predict future system load (capacity planning, for example).

static meeting

Non-scheduled meetings configured on the Cisco TelePresence Multipoint Switch (CTMS) through the administration interface. A meeting scheduler or administrator, who sets up the static meeting, manually assigns a meeting access number that is used to access the meeting. See ad hoc meeting .

switching mode

CTS Manager configuration. CTS 3000 and CTS 3200 endpoints only.

Auto-Assign—Switching mode is determined by the default CTMS policy, which is configured in System Configuration > Policy Management page of your CTMS setup.

Room—All the participant displays of the endpoint are switched each time the meeting participant who is speaking changes to a meeting participant at a different endpoint.

Speaker—Only the corresponding participant display (left, center, or right) is switched; the remaining participant displays are not switched. Using the speaker switching mode provides the ability to view up to three different remote endpoints at the same time.

Sysop

System Operation (sysop) Logs. Sysop messages describe system activity. Some messages can help you identify and resolve system operation problems. These messages are available to the user from the CTS Administration interface. See the Cisco TelePresence System Administration Guide on Cisco.com.

Syslog

System Logs (syslog). Debugging logs that are collected from your system and used by Cisco technical response to diagnose and resolve issues. These messages are not ordinarily seen by the user.

.tar

untar

tar (derived from tape archive) is both file format (in the form of a type of archive bitstream) and the name of the program used to handle such files. Used to collate collections of files into one larger file, for distribution or archiving, while preserving file system information such as user and group permissions, dates, and directory structures. Downloadable Linux or Unix files found on the internet are compressed using a tar or tar.gz compression format.

Open a tar file, or “untar” it.

trap

An SNMP trap is a message which is initiated by a network element and sent to the network management system. See the Cisco TelePresence System Message Guide .

triple system

A Cisco TelePresence System featuring three main screen display screens.

TFTP

Trivial File Transfer Protocol. Simplified version of FTP that allows files to be transferred from one computer to another over a network, usually without the use of client authentication (for example, username and password).

TIP

Telepresence Interoperability Protocol. The TIP Specification provides a protocol for interoperability between videoconferencing products, including streaming of audio, video, and data to and from videoconferencing products.

This feature adds TIP 7 support to the CTS and CTMS 1.7 release. The main purpose of the feature is for CTS and CTMS to operate in a strict TIP V7 mode when communicating with devices advertising TIP V7 support. This feature adds the ability to differentiate between MUX and TIP modes of operation to help with the strict adherence to the TIP V7 specifications as well as improving debugging and other operational processes. This feature adds the ability for the CTS to be configured for operation in a TIP-only mode and configured with a set of media features typically not used in Cisco-only deployments. This helps the CTS and CTMS inter-operate with third-party TIP devices.

TIP allows only endpoints with Restricted media settings to join Cisco TelePresence meetings. TIP endpoints are expected to be able to send restricted media and to drop endpoints that can only transmit un-restricted media. See the Telepresence Interoperability Protocol for Developers home page on Cisco.com.

UDI

Unique device identification.

VGA

Video Graphics Array port and cable for Cisco TelePresence. A CTS endpoint initiates a presentation at any point by plugging the VGA Auxiliary cable into the CTS endpoint presenter's laptop, which automatically shares from the presenter’s laptop. The last participant in the meeting to plug in their laptop with the VGA cable shares their presentation using PiP . See the Cisco TelePresence System User Guide for more information about sharing presentations.

virtual machine

A virtual machine (VM) is a software implementation of a machine (a computer, for example) that executes programs like a physical machine does. A system virtual machine provides a complete system platform which the execution of a complete operating system (OS). See the Cisco TelePresence System Commercial Express Installation Guide on Cisco.com for more information.

VLAN ID

The identification of the virtual LAN, which is used by the standard IEEE 802.1Q. Being on 12 bits, it allows the identification of 4096 VLANs.

VMware

VMware software provides a completely virtualized set of hardware to the guest operating system. VMware software virtualizes the hardware for a video adapter, a network adapter, and hard disk adapters. The host provides pass-through drivers for guest USB, serial, and parallel devices. In this way, VMware virtual machines become highly portable between computers, because every host looks nearly identical to the guest. In practice, a system administrator can pause operations on a virtual machine guest, move or copy that guest to another physical computer, and there resume execution exactly at the point of suspension. Alternately, for enterprise servers, a feature called VMotion allows the migration of operational guest virtual machines between similar but separate hardware hosts sharing the same storage. Each of these transitions is completely transparent to any users on the virtual machine at the time it is being migrated. See the Cisco TelePresence System Commercial Express Installation Guide on Cisco.com for more information.

VPN model (fixed path)

The VPN model uses a fixed, more secure path for packet delivery. VPNs only allow authorized personnel to gain access to their network.

WebDAV

Web-based Distributed Authoring and Versioning (WebDAV) is a set of methods based on the Hypertext Transfer Protocol (HTTP) that facilitates collaboration between users in editing and managing documents and files stored on World Wide Web servers. WebDAV was defined in RFC 4918 by a working group of the Internet Engineering Task Force (IETF).

WebEx

Cisco WebEx collaboration tools combine real-time desktop sharing with phone conferencing. See the Cisco TelePresence WebEx OneTouch Configuration Guide for the Cisco TelePresence System for first-time setup information. See also the Cisco TelePresence System User Guide that corresponds with your system.

| A |  |
|---|---|
| ACU | Auxiliary Control Unit. Provides the ability to conserve energy by powering the lights, projector, and optional peripherals for Cisco TelePresence systems on and off. The ACU is controlled by the CTS Administrator. |
| ad hoc meeting | Non-scheduled, administrator-initiated, dial-out meeting. A meeting scheduler or administrator initiates the meeting through the Cisco TelePresence Multipoint Switch (CTMS) administration interface by listing the telephone number of the rooms which will participate in the multipoint meeting. See static meeting . |
| AES | Advanced Encryption Standard. An encryption standard comprising three block ciphers, AES-128, AES-192, and AES-256, adopted from a larger collection originally published as Rijndael. Each AES cipher has a 128-bit block size, with key sizes of 128, 192 and 256 bits, respectively. |
| Auto Answer | A phone set to automatically answer an inbound call. Use the Auto Answer feature in Cisco Unified Communications Manager. Activating this option or button causes the speaker phone to go off hook automatically when an incoming call is received. |
| Auto Collaborate | Cisco TelePresence simple information sharing using a powerful “Auto Collaborate” feature that allows any object, document, or PC application to be displayed in a plug-and-play fashion. Auto Collaborate enables you to share images instantly in multiple locations by plugging in a laptop computer or high-definition ceiling document camera. The Cisco TelePresence 3000 Series built-in projector automatically displays images from the most recently activated device. Ceiling cameras are perfect for capturing images of objects that are too valuable to ship, or cannot easily be copied or sent electronically. Cisco recommends and document cameras made by WolfVision, specifically the WolfVision Visualizer. This is a special live-camera system designed for picking up any object on a working surface with perfect illumination and depth of focus. All types of objects (e.g., photos, books, brochures, transparencies, slides, or three-dimensional objects) can be picked up quickly and easily, and meeting participants can use a wireless remote to control light, zoom, or focus. Cisco TelePresence 3000 and 1000 systems support the Auto Collaborate capability, and meeting organizers can project content in multiple locations, including above or below displays, or on the side of a room. |
| A/V Expansion Box | Audio/video extension unit. Required if your system uses an Auxiliary Control Unit ( ACU ). |
| AXL | Administrative XML. SOAP -based protocol that enables remote provisioning of Unified CM. Cisco AXL Web Service allows Unified CM to be updated from Architecture for Voice, Video and Integrated Data (AVVID) client-based applications that use AXL. |

| B |  |
|---|---|
| bit rate | Speed at which bits are transmitted, usually expressed in bits per second. |
| black screen codes | System status information messages that appear on the main display screen before your meeting starts and while the screen is still black. For example, “Please wait, you are the first meeting participant.” For more information, see the Cisco TelePresence System User Guide . |
| BPDU | Bridge Protocol Data Units. Data frames that exchange information about bridge IDs and root path costs. A bridge sends a BPDU frame using the unique MAC address of the port as a source address, and a destination address of the Spanning Tree Protocol (STP) multicast address 01:80:C2:00:00:00. |

| C |  |
|---|---|
| CCP | The Conference Control Protocol (CCP) is an interface between the CTS and the CTMS that controls the following elements of a Cisco TelePresence conference: Locks a meeting. Sets the switching policy. Sends end meeting notifications. Obtains the roster list. Requests to meeting to be extended. Sends black screen messages. See black screen codes . Allows you to specify default outbound http proxy route. |
| CIF | Common Intermediate Format. A video standard that provides 352x288 pixels, or picture elements, of video resolution. |
| Cisco CTI Manager | CTI Manager is required in a cluster for applications that use TAPI or JTAPI Computer Telephony Integration (CTI). The CTI Manager acts as a broker between the CTI application and the Cisco Unified Communications Manager Service. It provides authentication of the application and enables control or monitoring of authorized devices. The CTI application communicates with a primary CTI Manager and, in the event of a failure, will switch to a backup CTI Manager. The CTI Manager should be enabled only on call processing subscribers, thus allowing for a maximum of eight CTI Managers in a cluster. Cisco recommends that you load-balance CTI applications across the various CTI Managers in the cluster to provide maximum resilience, performance, and redundancy. |
| Cisco TelePresence TX Series | The Cisco TelePresence TX Series high-definition presentation capabilities and simple controls on a touch display help make your meeting as immersive and natural as possible. See Immersive Telepresence Endpoints . |
| Cisco Unified Communications Manager | Unified CM. Application that extends enterprise telephony features and capabilities to packet telephony network devices such as IP phones and multimedia applications. Open telephony application interfaces make possible services such as multimedia conferencing and interactive multimedia response systems. |
| codec | The “brain” of the CTS. The primary codec connects with the network and Cisco Unified Communications Manager (Cisco Unified CM) to perform call management functions for the system. The secondary codec performs processing for the system elements that are attached to them. The optional presentation codec the document camera (if present), auxiliary displays, and works with an auxiliary control unit and audio extension unit for additional audio/video applications. The number and type of codecs your system uses depends on which CTS device you are using. |
| CTMS | Cisco TelePresence Multipoint Switch . Support for voice-activated switching in up to 48 locations in a single meeting across many endpoint s. |
| CTRS | Cisco TelePresence Recording Server . Providing HD studio recording capabilities in existing Cisco TelePresence rooms. Recordings can be archived automatically on a schedule or transferred to a digital content management system. The CTRS can deliver Cisco TelePresence recordings to any video-enabled device including PCs, smartphones, and digital signs. CTRS runs on the same reliable Media Convergence Server platform as Cisco TelePresence Multipoint Switch and Cisco TelePresence Manager. |
| CTS device | Cisco TelePresence System (CTS) device: CTS 500, CTS 1000, CTS 1100, CTS 1300, CTS 3000 series, CTS 3200 series. |
| CTS-Manager | Cisco TelePresence Manager . Software application that schedules and manages Cisco TelePresence calls using common enterprise groupware such as Microsoft Exchange and Lotus Notes. |
| CTS Manager PreQualification Assistant | The CTS-Man PreQualification Assistant ensures that your pre-configuration set-up is performed correctly. The data that is entered into the Tool Test Configuration forms that are used to verify connections to the servers and to get data from them to be used to configure CTS-Man. |
| CUCM | Cisco Unified Communications Manager (Unified CM). |

| D |  |
|---|---|
| default gateway | A router on a computer network that serves as an access point to another network. |
| DES | Data Encryption Standard. A block cipher (a form of shared secret encryption) that was selected by the National Bureau of Standards as an official Federal Information Processing Standard (FIPS) for the United States in 1976 and which has subsequently enjoyed widespread use internationally. It is based on a symmetric-key algorithm that uses a 56-bit key. |
| DHCP | Dynamic Host Configuration Protocol. Provides a mechanism for allocating IP addresses dynamically so that addresses can be reused when hosts no longer need them. |
| Directory | Button or Softkey on the Cisco Unified IP Phone that is configured from the Administration and User interfaces. Gives users access to several directories including the Corporate Directory and the Personal Directory. |
| display screen animation | System information icons that may be displayed on the Cisco TelePresence System (CTS) main display screen. System information includes call connection status alerts, meeting alerts, and maintenance alerts. These alerts fade from one state to another to show the status of the system. |
| display screen icon | System information icons that may be displayed on the Cisco TelePresence System (CTS) display screen. System information includes call connection status alerts, meeting alerts, and maintenance alerts. |
| DMP | Digital Media Player. Cisco Digital Media Players are highly-reliable, IP-based endpoints that can play high-definition live and on-demand video, motion graphics, web pages, and dynamic content on digital displays, usually an LCD Professional Series display or any other directly attached television screen, monitor, or projector (analog or digital, standard-definition or high-definition) that shows media to an audience. There is an extra input connector for the Digital Media Player (DMP) on your Cisco TelePresence device. See the Cisco Digital Media Players home page on Cisco.com. See also LCD . |
| DN | Directory number. |
| DNS | Domain Name System. Domain in which the phone resides. Primary Domain Name System (DNS) server (DNS Server 1) and optional backup DNS servers (DNS Server 2-5) used by the phone. Redundant DNS servers that point to the Cisco Unified CM are configured and listed on the in-room phone by navigating to Settings > Network Configuration > IPv4 Configuration. |
| DSCP | Differentiated Services Code Point. A field in the header of IP packets for packet classification purposes. DSCP for TelePresence Calls field description: This parameter specifies the DSCP value for Cisco TelePresence calls. This parameter is set to the default value unless a Cisco support engineer instructs otherwise. This is a required field, if present on your system. Default: CS4(precedence 4) DSCP (100000) and is selectable per device. |
| DVI | DVI cables are used for direct digital connections between source video (namely, video cards) and LCD monitors. Plugs into desktop, PC, or laptop docking station. See also VGA . |

| E |  |
|---|---|
| enbloc dialing | Allows you to compose and edit the number to dial on your phone's display before it is sent to the phone system to be dialed. |
| endpoint | Cisco TelePresence System (CTS) endpoint. The combination of hardware and software that comprise a Cisco TelePresence System. The hardware for an endpoint includes a Cisco Unified IP Phone 7900 Series, one or more large-screen meeting displays, plus presentation devices, cameras, microphones, speakers, and in some models, lighting systems. |
| EWS | Exchange Web Services. Managed API that provides an intuitive interface for developing client applications that use Exchange Web Services. The EWS Managed API provides unified access to Microsoft Exchange Server resources, while using Microsoft Office Outlook–compatible business logic. The EWS Managed API communicates with the Exchange Client Access server by means of EWS SOAP messages. |
| extranet | An extranet is a private network that uses Internet protocols and network connectivity. An extranet can be viewed as part of a company's intranet that is extended to users outside the company, usually via the Internet. It has also been described as a “state of mind” in which the Internet is perceived as a way to do business with a selected set of other companies (business-to-business, B2B), in isolation from all other Internet users. In contrast, business-to-consumer (B2C) models involve known servers of one or more companies, communicating with previously unknown consumer users. An extranet can be understood as an intranet mapped onto the public Internet or some other transmission system not accessible to the general public, but managed by more than one company's administrator(s). For example, military networks of different security levels may map onto a common military radio transmission system that never connects to the Internet. Any private network mapped onto a public one is a virtual private network (VPN), often using special security protocols. |

| F |  |
|---|---|
| Favorites | The Favorites softkey and screen on the CTS Cisco Unified IP Phone. |
| fluorescent lamp | A lamp that uses electricity to excite mercury vapor in a gas that results in an energy that produces short-wave ultraviolet light. This light then causes a phosphor to fluoresce, producing visible light. Sources of light in most rooms are either incandescent light bulbs that use tungsten filaments or fluorescent lights. Each of these light sources, and the amount of light in terms of lumens or watts, produces a different color temperature. This color temperature is sometimes expressed using terms such cool, warm, or daylight, but can be expressed more precisely in kelvins (K) as a numeric value. When adjusting the images on the display screens for the Cisco TelePresence system, you must take the color temperature of the ambient light in the room into consideration. |
| full duplex mode | Transmission of data in two directions simultaneously. |

| G |  |
|---|---|
| guest operating system | An operating system that is installed and run in a virtual machine . In the Cisco TelePresence environment, the CTS Manager, CTMS, and CTRS are guest operating systems. Before you can install the guest operating system, you must obtain the installation media for the operating system and configure the virtual machine to use the CD/DVD drive to access the installation media. See VMware . |
| gzip | GNU zip. Software application used for file compression. |

| H |  |
|---|---|
| half duplex mode | Transmission of data in one direction at a time. |
| HD | High definition display. High-definition video or HD video refers to any video system of higher resolution than standard-definition (SD) video, and most commonly involves display resolutions of 1280×720 pixels (720p) or 1920×1080 pixels (1080i/1080p). |
| HDMI | Document camera input and cable. |

| I |  |
|---|---|
| IDR | An IDR frame is a special kind of I frame used in MPEG-4 AVC encoding. IDR frames can be used to create Advanced Video Coding (AVC) streams, which can be easily edited. |
| Immersive Telepresence Endpoints | CTS 3210, CTS 1300, Cisco TelePresence T3. Provides an immersive, interactive in-person experience. See also personal system . |
| incandescent lamp | A lamp that allows an electric current to pass through a thin filament, heating it and causing it to emit light. Sources of light in most rooms are either incandescent light bulbs that use tungsten filaments or fluorescent lights. Each of these light sources, and the amount of light in terms of lumens or watts, produces a different color temperature. This color temperature is sometimes expressed using terms such cool, warm, or daylight, but can be expressed more precisely in kelvins (K) as a numeric value. When adjusting the images on the display screens for the Cisco TelePresence system, you must take the color temperature of the ambient light in the room into consideration. |
| Internet model (free path) | The Internet model is an unsecured “free path” model of packet delivery: Packets are delivered in any way possible and each uncontrolled router on the way to the destination handles how to deliver the packet to the next stop. See VPN model (fixed path) . |
| IP address | A device identifier on a TCP/IP network. |

| J |  |
|---|---|
| jitter jitter call jitter period | Variation in packet transit delay caused by queuing, contention, and serialization effects on the path through the network. In general, higher levels of jitter are more likely to occur on either slow or heavily congested links. Jitter call is the average jitter measurement per call. Shown in the Jitter/Call output field as part of Per Call Jitter and Packet Loss Reporting. Jitter period is the interval between two times of maximum effect (or minimum effect) of a signal characteristic that varies regularly with time. Jitter frequency, the more commonly quoted figure, is its inverse. The CTS measures jitter every 10 seconds. The Jitter/Period field reports the jitter measurement for the last 10-second period. The CTS calculates jitter as the sum of the maximum deviation (both late and early) from the expected arrival time as given by the frame period. CMA computes frame jitter based on the arrival time of the last packet of a frame. |

| L |  |
|---|---|
| LCD | Liquid crystal display. The LCD display is an accessory for the Cisco Digital Media Player (DMP) for use in your digital signage network or your enterprise TV network. It is used for displaying video, images, or computer data during a Cisco TelePresence meeting. See the Cisco LCD Professional Series Displays home page on Cisco.com for more information. See also DMP . |
| LED | Light-emitting diode. Indicators on the CTS that determine whether the user is sitting within camera range. |
| light temperature | A theoretical means of describing visible light that is determined by comparing its hue with a heated black-body radiator. The lamp’s color temperature is the temperature in kelvins at which the heated black-body radiator matches the hue of the lamp. |
| Live Desk | The Live Desk is a person who has been assigned to a Cisco TelePresence endpoint to assist you with problems that may occur during a meeting. To connect to Live Desk, touch the Live Desk softkey. If a Live Desk has not been assigned to your Cisco TelePresence endpoint , the following message is displayed on your phone screen: “There is no Live Desk number configured” If your system is running CTS software release 1.9.1 or later, you can configure Live Desk using the Live Desk field in Unified CM. For more information, refer to the Live Desk in Cisco Unified CM section of the Release Notes for Cisco TelePresence System Software Release 1.9 . If your system is running CTS software release prior to 1.9.1, you can configure Live Desk in the Configure > Live Desks Window of the CTS-Manager Administration interface. Refer to the Cisco TelePresence Manager Installation and Configuration Guide on Cisco.com. |
| LTRP | Long Term Reference Picture. |

| M |  |
|---|---|
| MAC address | Media Access Control address. A hardware address that uniquely identifies each node of a network. |
| MD5 | Message-Digest algorithm 5. Widely used cryptographic hash function with a 128-bit hash value. As an Internet standard (RFC 1321), MD5 has been employed in a wide variety of security applications, and is also commonly used to check the integrity of files. MD5 is not suitable for applications like SSL certificates or digital signatures that rely on this property. An MD5 hash is typically expressed as a 32 digit hexadecimal number. |
| Meeting Extension | Meeting Extension feature that can be used from the CTS Cisco Unified IP phone when MIDlets are configured. This feature provides an option on the CTS Cisco Unified IP phone to extend Cisco TelePresence meetings past their scheduled end time. Meeting participants may request to extend the scheduled meeting using the phone softkey options. CTS Manager Administrators can configure Meeting Extension settings using the Meeting Options tab on the CTS Manager System Configuration > Application Settings page. |
| MIDlets | Mobile Information Device Profile (MIDP). A Java application designed to run on resource-constrained devices such as phones, PDAs, intelligent appliances, and the like. A MIDlet (in J2ME) is similar to a Java Applet (in J2SE), but more specialized, efficient, and optimized for limited devices. MIDlets graphics and animation, multimedia, touchscreen, networking, persistent data storage, and provides excellent Look And Feel (LAF) integration with the host platform. The Cisco Unified IP Phone uses MIDlets as part of the Cisco TelePresence System Enhanced Phone User Interface: MIDlets support CTS Cisco Unified IP phone features. Configure MIDlets in the Cisco Unified CM Administration interface for Cisco TelePresence. See Configuring and Managing the Cisco Unified IP Phone for more information. |
| mixed mode | Cluster Security Mode field is set to 1 in the Configuration Settings for CTL Client in Cisco Unified CM Administration > System > Enterprise Parameters . To configure and verify cluster security mode, see the Verifying the Cisco Unified Communications Manager Security Mode section of the Cisco TelePresence Security Solutions Guide . |
| multipoint meeting | Multipoint is where you are able to connect more than two sites in one video conference. This normally requires a bridge, although some video conference units are also able to connect multiple sites. |
| MXE | Media eXperience Engine. The Cisco Media Experience Engine is a modular media processing system that provides interoperability between Cisco TelePresence and video conferencing devices, extending the reach of collaboration and communication within organizations. MXE provides 720p interoperability with video conferencing. Configure MXE in CTS-Manager . See also Cisco TelePresence Firewall and Access List Considerations for support information for Cisco TelePresence. |

| N |  |
|---|---|
| nonce | A nonce value (a random number that digest authentication) is used to calculate the MD5 hash of the digest authentication password. |
| Non-permitted User | Cisco WebEx user role configured in the CTS Manager Administration interface. These users are not permitted to request Cisco WebEx; no Cisco WebEx meeting options are available to these users. See Permitted User . |

| O |  |
|---|---|
| One-Button-to-Push | Launches a call with Cisco TelePresence Manager. Cisco TelePresence Manager works with enterprise groupware software such as Microsoft Exchange and Lotus Notes to allow you to schedule Cisco TelePresence meetings just as you would a regular meeting. Enterprise groupware sends Cisco TelePresence Manager the meeting schedule, and the software pushes that information to the in-room phone for call launch. The “One-Button-to-Push” feature allows you to simply touch the meeting that is listed on the in-room IP phone to start a Cisco TelePresence meeting. |

| P |  |
|---|---|
| Participant List | A list of Cisco WebEx meeting participants displayed on the phone that are visible when you touch the Participant List softkey or the phone screen touch button on the fully configured CTS Cisco Unified Phone. This list is configured in Cisco Unified CM Display (Internal Caller ID) fields. |
| P-frame | An easily compressible video frame type. A video frame is compressed using different algorithms that allow varied amounts of data compression. These different algorithms for video frames are called picture types or frame types. The three major picture types used in the different video algorithms are I, P, and B. |
| Permitted User | Cisco WebEx user role configured in the CTS Manager Administration interface. These users are permitted to request Cisco WebEx for specific meetings using CTS Manager. See Non-permitted User . |
| personal system | Personal Cisco TelePresence System. The virtual, in-person experience of Cisco TelePresence directly into the private office. The CTS 500 and CTS 1000 are considered to be personal systems. See also Immersive Telepresence Endpoints . |
| PiP | Presentation-in-Picture. Data or graphics content sharing through an external monitor known as presentation-in-picture (PiP) format for space-constrained offices. Using the PiPCtrl softkey and options in the PiP control screen on your CTS Cisco Unified IP phone, you can toggle the position of the PiP between center, left, or right locations on the screen or change its size in relation to the meeting participant video input during a meeting. |
| PoE | Power over Ethernet. |
| point-to-point meeting | The direct connection of two sites in a video conference. This only works if both sites use the same type of connection (either IP or ISDN). |
| Premium User | Cisco WebEx user role configured in the CTS Manager Administration interface: Cisco WebEx is always on. Controlled on the CTS Manager LDAP configuration page. |
| presentation codec | The presentation codec provides 30 frames per second to support full-motion video presentations between Cisco TelePresence endpoints. |
| Presenter | Cisco WebEx user role configured in the CTS Manager Administration interface: A Presenter shares presentations, specific applications, or the entire desktop. The Presenter controls the annotation tools and can grant and revoke remote control over the shared applications and desktop to individual Attendees. |
| primary codec | The primary codec is the primary unit; it communicates with secondary units, sends and receives packets on the uplink network. It contains an onboard Gigabit Ethernet switch. For example, in a CTS 3000 or CTS 3200 system, the primary codec controls two secondary codecs as well as many system components and the graphical user interfaces (GUI). In a Cisco TelePresence 1000, it controls all system functions. |
| PCB | Printed circuit board. |

| R |  |
|---|---|
| RFC | Request for Comments. Document series used as the primary means for communicating information about the Internet. Some RFCs are designated by the IAB as Internet standards. |

| S |  |
|---|---|
| scheduled meeting | Multipoint TelePresence meetings are scheduled by end users using Microsoft Exchange or IBM Domino clients in the same manner that a point-to-point meeting is scheduled. Scheduled meetings require no CTMS administrator interaction. CTS Manager is a required component for scheduled meetings. It provides the interface between Microsoft Exchange or Lotus Domino and the CTMS, allowing the appropriate resources on the CTMS to be reserved for the multipoint meeting . |
| Scheduling API | Cisco TelePresence Scheduling API provides programmatic access to your organization's CTS-Manager using a simple, powerful, and secure application-programming interface for customers who are not using Microsoft Exchange or IBM Domino Notes. For developers this API allows groupware applications to utilize Cisco TelePresence Manager for scheduling Cisco TelePresence calls with resource reservations and One-Button-to-Push . |
| screen resolution | The fineness of detail that can be presented in the image on the CTS main display screen. Recommended screen resolution for Cisco TelePresence is 1024 x 768. |
| SD | Standard definition display. See HD . |
| secondary codec | Codecs that assist the primary codec in the large Cisco TelePresence 3000/3200 systems. Secondary codecs process audio and video signals and send them to the primary codec, which multiplexes the signals into separate, single RTP streams. |
| Show and Share | If your Cisco TelePresence network administrator has configured Cisco Show and Share as your enterprise video portal, you can immediately publish your recording or save a draft to Cisco Show and Share from the Cisco TelePresence Touch 12 or Cisco Unified IP phone. For more information on creating and viewing recordings, see the Cisco TelePresence System User Guide on Cisco.com that corresponds with your system’s software release. |
| single system | A Cisco TelePresence System featuring a single main display screen. |
| SHA | Secure Hash Algorithm. A set of cryptographic hash functions designed by the National Security Agency (NSA) and published by the NIST as a U.S. Federal Information Processing Standard. The three SHA algorithms are structured differently and are distinguished as SHA-0, SHA-1, and SHA-2. |
| SIP | Session Initiation Protocol. Protocol designed to signal the setup of voice and multimedia calls over IP networks. |
| SNMP | Simple Network Management Protocol. Network management protocol used almost exclusively in TCP/IP networks as a means to monitor and control network devices, and to manage configurations, statistics collection, performance, and security. See the Cisco TelePresence System Message Guide . |
| SOAP | Simple Object Access Protocol. XML-based protocol to let applications exchange information over HTTP. |
| SSCD | System Status Collection Daemon. The daemon gathers statistics about the system it is running on and stores this information. Those statistics can then be used to find current performance bottlenecks (performance analysis, for example) and predict future system load (capacity planning, for example). |
| static meeting | Non-scheduled meetings configured on the Cisco TelePresence Multipoint Switch (CTMS) through the administration interface. A meeting scheduler or administrator, who sets up the static meeting, manually assigns a meeting access number that is used to access the meeting. See ad hoc meeting . |
| switching mode | CTS Manager configuration. CTS 3000 and CTS 3200 endpoints only. Auto-Assign—Switching mode is determined by the default CTMS policy, which is configured in System Configuration > Policy Management page of your CTMS setup. Room—All the participant displays of the endpoint are switched each time the meeting participant who is speaking changes to a meeting participant at a different endpoint. Speaker—Only the corresponding participant display (left, center, or right) is switched; the remaining participant displays are not switched. Using the speaker switching mode provides the ability to view up to three different remote endpoints at the same time. |
| Sysop | System Operation (sysop) Logs. Sysop messages describe system activity. Some messages can help you identify and resolve system operation problems. These messages are available to the user from the CTS Administration interface. See the Cisco TelePresence System Administration Guide on Cisco.com. |
| Syslog | System Logs (syslog). Debugging logs that are collected from your system and used by Cisco technical response to diagnose and resolve issues. These messages are not ordinarily seen by the user. |

| T |  |
|---|---|
| .tar untar | tar (derived from tape archive) is both file format (in the form of a type of archive bitstream) and the name of the program used to handle such files. Used to collate collections of files into one larger file, for distribution or archiving, while preserving file system information such as user and group permissions, dates, and directory structures. Downloadable Linux or Unix files found on the internet are compressed using a tar or tar.gz compression format. Open a tar file, or “untar” it. |
| trap | An SNMP trap is a message which is initiated by a network element and sent to the network management system. See the Cisco TelePresence System Message Guide . |
| triple system | A Cisco TelePresence System featuring three main screen display screens. |
| TFTP | Trivial File Transfer Protocol. Simplified version of FTP that allows files to be transferred from one computer to another over a network, usually without the use of client authentication (for example, username and password). |
| TIP | Telepresence Interoperability Protocol. The TIP Specification provides a protocol for interoperability between videoconferencing products, including streaming of audio, video, and data to and from videoconferencing products. This feature adds TIP 7 support to the CTS and CTMS 1.7 release. The main purpose of the feature is for CTS and CTMS to operate in a strict TIP V7 mode when communicating with devices advertising TIP V7 support. This feature adds the ability to differentiate between MUX and TIP modes of operation to help with the strict adherence to the TIP V7 specifications as well as improving debugging and other operational processes. This feature adds the ability for the CTS to be configured for operation in a TIP-only mode and configured with a set of media features typically not used in Cisco-only deployments. This helps the CTS and CTMS inter-operate with third-party TIP devices. TIP allows only endpoints with Restricted media settings to join Cisco TelePresence meetings. TIP endpoints are expected to be able to send restricted media and to drop endpoints that can only transmit un-restricted media. See the Telepresence Interoperability Protocol for Developers home page on Cisco.com. |

| U |  |
|---|---|
| UDI | Unique device identification. |

| V |  |
|---|---|
| VGA | Video Graphics Array port and cable for Cisco TelePresence. A CTS endpoint initiates a presentation at any point by plugging the VGA Auxiliary cable into the CTS endpoint presenter's laptop, which automatically shares from the presenter’s laptop. The last participant in the meeting to plug in their laptop with the VGA cable shares their presentation using PiP . See the Cisco TelePresence System User Guide for more information about sharing presentations. |
| virtual machine | A virtual machine (VM) is a software implementation of a machine (a computer, for example) that executes programs like a physical machine does. A system virtual machine provides a complete system platform which the execution of a complete operating system (OS). See the Cisco TelePresence System Commercial Express Installation Guide on Cisco.com for more information. |
| VLAN ID | The identification of the virtual LAN, which is used by the standard IEEE 802.1Q. Being on 12 bits, it allows the identification of 4096 VLANs. |
| VMware | VMware software provides a completely virtualized set of hardware to the guest operating system. VMware software virtualizes the hardware for a video adapter, a network adapter, and hard disk adapters. The host provides pass-through drivers for guest USB, serial, and parallel devices. In this way, VMware virtual machines become highly portable between computers, because every host looks nearly identical to the guest. In practice, a system administrator can pause operations on a virtual machine guest, move or copy that guest to another physical computer, and there resume execution exactly at the point of suspension. Alternately, for enterprise servers, a feature called VMotion allows the migration of operational guest virtual machines between similar but separate hardware hosts sharing the same storage. Each of these transitions is completely transparent to any users on the virtual machine at the time it is being migrated. See the Cisco TelePresence System Commercial Express Installation Guide on Cisco.com for more information. |
| VPN model (fixed path) | The VPN model uses a fixed, more secure path for packet delivery. VPNs only allow authorized personnel to gain access to their network. |

| W |  |
|---|---|
| WebDAV | Web-based Distributed Authoring and Versioning (WebDAV) is a set of methods based on the Hypertext Transfer Protocol (HTTP) that facilitates collaboration between users in editing and managing documents and files stored on World Wide Web servers. WebDAV was defined in RFC 4918 by a working group of the Internet Engineering Task Force (IETF). |
| WebEx | Cisco WebEx collaboration tools combine real-time desktop sharing with phone conferencing. See the Cisco TelePresence WebEx OneTouch Configuration Guide for the Cisco TelePresence System for first-time setup information. See also the Cisco TelePresence System User Guide that corresponds with your system. |