---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-vg248-1-1-2-english-release-notes-vg248rn4-html-9c36624b70
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/vg248/1_1_2/english/release/notes/vg248rn4.html
retrieved_at: 2026-08-21T12:51:24.836402+00:00
---

VG248 Analog Phone Gateway Version 1.1(2) Release Notes

# VG248 Analog Phone Gateway Version 1.1(2) Release Notes

- Notes

- Notes

### Download Options

Updated: April 1, 2002

## Table Of Contents

Cisco VG248 Analog Phone Gateway Version 1.1(2) Release Notes

New and Changed Information

Enabling Fax Relay Per Port

Setting Echo Cancelling Policy

Modifying Serial Settings for Async Ports

Setting and Clearing MWI Messages

Previous Updates

SMDI Support for Voice Mail Integration

Support for Italian Phones

Call Forward Dial-Tone

Documentation Roadmap

Updates to Cisco CallManager Compatibility

Using Cisco CallManager Version 3.1

Using Cisco CallManager Version 3.2

Changes to the Cisco CallManager Interface

Important Caveats

Adding the VG248 Gateway to Cisco CallManager

Configuring VG248 Analog Ports

Fax Over IP Support

Resolved Caveats

Open Caveats

Obtaining Documentation

World Wide Web

Documentation CD-ROM

Ordering Documentation

Documentation Feedback

Obtaining Technical Assistance

Cisco.com

Technical Assistance Center

Cisco TAC Web Site

Cisco TAC Escalation Center

## Cisco VG248 Analog Phone Gateway Version 1.1(2) Release Notes

April 17, 2002

These release notes are for use with the Cisco VG248 Analog Phone Gateway with software version 1.1(2). The VG248 enables you to integrate analog telephony devices and existing voice mail systems (using Simplified Message Desk Interface) with Cisco CallManager IP telephony systems.

These release notes provide the following information:

• New and Changed Information

• Previous Updates

• Documentation Roadmap

• Updates to Cisco CallManager Compatibility

• Fax Over IP Support

• Resolved Caveats

• Open Caveats

• Obtaining Documentation

• Obtaining Technical Assistance

## New and Changed Information

The following topics describe features now available in version 1.1(2) of the VG248 software:

• Enabling Fax Relay Per Port

• Setting Echo Cancelling Policy

• Modifying Serial Settings for Async Ports

### Enabling Fax Relay Per Port

When making fax calls through a VG248, the VG248 uses either fax pass through or Cisco fax relay to transport the document information. Fax pass through sends the signals in an audio form similar to that used for a normal voice call, and Cisco fax relay encodes the information in a different format which is converted back to analog fax signals by the other party in the call.

Fax relay is more robust and should normally be enabled. However, some types of modems sometimes appear to the VG248 to be sending fax signals. In these cases, Cisco fax relay should not be initiated. If you experience these modem problems, disable fax relay on the affected ports on the VG248.

In previous versions of the VG248 software, you could enable fax relay for the entire device. All ports would then be configured to initiate Cisco fax relay or to use fax pass through only.

With version 1.1(2), you can now enable fax relay on a per port basis instead. This enables you to configure individual ports for Cisco fax relay or fax pass through to ensure best performance depending on the types of fax machines attached.

After upgrading to version 1.1(2), Cisco fax relay is enabled by default on all ports. To disable Cisco fax relay and use fax pass through instead, follow these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose Telephony .

Step 3 Choose Port specific parameters .

Step 4 Use the arrow keys to select the port to configure and press Enter.

Step 5 Choose Fax relay .

Step 6 Choose Disabled .

### Setting Echo Cancelling Policy

You can now select an alternative method for cancelling echo that might be present in the system. For an explanation of the echo issues in IP telephony networks, refer to the document, Echo Analysis for Voice over IP, available at the following location on Cisco.com:

http://www.cisco.com/univercd/cc/td/doc/cisintwk/intsolns/voipsol/ea_isd.htm

The default echo cancelling technique in version 1.1(2) is identical to previous software versions. You should only change this setting if you experience certain specific echo issues in your network and you are instructed to do so by a Cisco technical representative.

Step 1 From the main menu, choose Configure .

Step 2 Choose Telephony .

Step 3 Choose Advanced settings

Step 4 Choose Echo cancelling policy .

Step 5 Choose one of the following:

• default: use SLIC

• alternate: use DSP

### Modifying Serial Settings for Async Ports

The VG248 software release 1.1(1) introduced the use of the Async 1 and Async 2 serial ports for the transportation of SMDI information to accomplish integration with analog voice mail systems. However, the Async 1 and Async 2 ports were only able to run with a certain fixed serial configuration: 9600 baud, 8 data bits, no parity and 1 stop bit.

Version 1.1(2) extends this capability by enabling you to modify these parameters. Versions 1.1(1) and 1.1(2) of the VG248 software requires that you disable flow control on the Async serial links.

Note The console port, used to access the VG248 menu interface through a serial connection, remains fixed at: 9600 baud, 8 data bits, no parity and 1 stop bit.

Async port speed

This parameter defines the baud rate used for the Async 1 and Async 2 serial connections used to connect VG248 devices to an analog voice mail system or to a legacy PBX. The speed of the Async 1 and Async 2 must be the same, and this speed must match the baud rate of the analog voice mail system's SMDI port. If you have chained multiple VG248 devices together, ensure that each device is set to the same port speed.

Async 1 or 2 Data Bits

You can set the number of data bits being used for the serial connection of the Async 1 or Async 2 port to be 8 (the default value) or 7.

Set this value to match the corresponding setting of the device to which the Async port is connected.

• Async 1—setting should match the setting on the SMDI port of the analog voice mail system or the Async 2 port of the next VG248 device in the chain.

• Async 2—setting should match the legacy PBX or the Async 1 of another VG248 device.

Async 1 or 2 Parity

You can set the parity on the Async ports to: none (the default setting), even or odd.

• Async 1—setting should match the setting on the SMDI port of the analog voice mail system or the Async 2 port of the next VG248 device in the chain.

• Async 2—setting should match the legacy PBX or the Async 1 of another VG248 device.

Async 1 or 2 Stop Bits

You can set the number of stop bits being used for the serial connection of the Async 1 or 2 port to be set to either 1 (the default value) or 2.

• Async 1—setting should match the setting on the SMDI port of the analog voice mail system or the Async 2 port of the next VG248 device in the chain.

• Async 2—setting should match the legacy PBX or the Async 1 of another VG248 device.

Step 1 From the main menu, choose Configure .

Step 2 Choose SMDI .

Step 3 Choose Async port serial settings

Step 4 Choose one of the following:

• Async port speed

– 1200 bps

– 2400 bps

– 4800 bps

– 9600 bps

• Async 1 data bits

– 8

– 7

• Async 1 parity

– none

– even

– odd

• Async 1 stop bits

– 1

– 2

• Async 2 data bits

– 8

– 7

• Async 2 parity

– none

– even

– odd

• Async 2 stop bits

– 1

– 2

### Setting and Clearing MWI Messages

If the VG248 is not properly setting or clearing message waiting indicators (MWIs), you should verify that you have properly configured this option.

To enable the VG248 to set or clear message waiting indicators (MWIs), ensure that the MWI port (commonly referred to as VG248 port 0) is configured within Cisco CallManager to have a unique directory number. If this port does not have a directory number, the VG248 is unable to set or clear message waiting indicators.

See Chapter 5, "Integrating Cisco CallManager with Voice Mail Systems Using SMDI" in the Cisco VG248 Analog Phone Gateway Software Configuration Guide for details:

http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_1/sw_confg/vg248smd.htm#xtocid9

## Previous Updates

The following topics describe features previously available in version 1.1(1) of the VG248 software:

• SMDI Support for Voice Mail Integration

• Support for Italian Phones

• Call Forward Dial-Tone

### SMDI Support for Voice Mail Integration

You can use the VG248 with v1.1(1) software to integrate your existing voice mail systems (such as Lyrix, Octel 200, Octel 250, Octel 300 and Octel 350) and legacy PBX systems with Cisco CallManager. See Chapter 5, "Integrating Cisco CallManager with Voice Mail Systems Using SMDI" in the Cisco VG248 Analog Phone Gateway Software Configuration Guide for details:

http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_1/sw_confg/vg248smd.htm

### Support for Italian Phones

The VG248 now supports the tones, cadences and telephone impedances used by standard Italian phones. Countries previously supported include: North America (USA and Canada), United Kingdom, Germany, France, Austria, and Switzerland.

### Call Forward Dial-Tone

When forward all is activated, users now hear a distinctive dial tone to indicate that all calls are currently being forwarded to a different directory number.

## Documentation Roadmap

Table 1 provides summaries and locations of available documents for the Cisco VG248 Analog Phone Gateway.

Table 1 Available Documentation for the Cisco VG248

Document Title

Description

Where to Find It

Cisco VG248 Analog Phone Gateway Hardware Installation Guide

Provides the site preparation, safety information, and hardware installation and setup instructions to safely install the VG248.

• In the box—A printed version of this document ships with the product

• Online at Cisco.com—HTML and PDF versions of this document are available from Cisco.com:

http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/hard_ins/index.htm

• By ordering—See the "Obtaining Documentation" section for details

Cisco VG248 Analog Phone Gateway Software Configuration Guide

Provides information about understanding, configuring, managing, and troubleshooting the VG248.

Online at Cisco.com—HTML and PDF versions of this document are available from Cisco.com:

http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_1/sw_confg/index.htm

Cisco VG248 Analog Phone Gateway Version 1.1(2) Release Notes

Describes known caveats and any documentation errata for the VG248.

Online at Cisco.com—HTML and PDF versions of this document are available from Cisco.com:

http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_1/rel_note/vg248rn3.htm

## Updates to Cisco CallManager Compatibility

You configure the VG248 differently depending on the version of Cisco CallManager you are using in your network. Refer to these sections for tips on using the VG248 with your version of Cisco CallManager:

• Using Cisco CallManager Version 3.1

• Using Cisco CallManager Version 3.2

### Using Cisco CallManager Version 3.1

The Cisco VG248 Analog Phone Gateway Software Configuration Guide provides the information needed to use the VG248 with Cisco CallManager 3.1. Refer to the "Documentation Roadmap" section for information on obtaining this document.

To use auto-registration with the VG248 and Cisco CallManager 3.1, you must use Cisco CallManager 3.1(3a), which is available at the following location on Cisco.com: http://www.cisco.com/cgi-bin/tablebuild.pl/callmgr-31.

### Using Cisco CallManager Version 3.2

Cisco CallManager 3.2 includes some interface changes that require you to manage the VG248 slightly differently than with Cisco CallManager 3.1. The following sections provide details about these changes:

• Changes to the Cisco CallManager Interface

• Important Caveats

• Adding the VG248 Gateway to Cisco CallManager

• Configuring VG248 Analog Ports

### Changes to the Cisco CallManager Interface

When using the VG248 with Cisco CallManager 3.2, you have access to new features, including:

• The addition of a VG248 gateway type

This allows you to add the device as a VGC gateway to Cisco CallManager and then configure each of the ports as VGC phone models. This consolidates each of the 48 analog or SMDI ports onto a single device. However, once you add the gateway and ports to Cisco CallManager, you still must configure these ports in the VG248 interface. See the "Adding the VG248 Gateway to Cisco CallManager" section for details.

• An additional port, port 00[VMI] appears on the VG248 Gateway Configuration window

This port appears if you are using the VG248 to integrate analog or SMDI devices. However, the VG248 uses this port only when setting or clearing MWIs on phones using SMDI. See the "Configuring VG248 Analog Ports" section for details on configuring ports.

### Important Caveats

When using the VG248 with Cisco CallManager 3.2, these important caveats apply:

• You cannot use auto-registration to add a VG248 to Cisco CallManager 3.2.

You must add the VG248 to Cisco CallManager manually. See the "Adding the VG248 Gateway to Cisco CallManager" section for details.

• If you are upgrading to Cisco CallManager 3.2 from Cisco CallManager 3.1, and you already have a VG248 configured in the database, the information is retained.

During the upgrade process, Cisco CallManager automatically creates a new VG248 gateway device based on the port information you entered in Cisco CallManager 3.1

• On the VG248 gateway configuration page in Cisco CallManager, the Reset Device button does not work.

• When configuring the VG248 ports as VGC phone models, additional fields that are not used by the VG248 appear, including:

– Auto Answer

– Line text label

– MW lamp policy

You can ignore these fields; they are not used by the VG248.

• If you perform a search for the VG248 gateway type (from Device > Gateway in Cisco CallManager Administration) the results indicate "Device Not Found".

Although you cannot locate the device using the gateway search, you can locate the device by searching for the VGC phone model.

• After configuring one port (VGC phone) on the VG248, Cisco CallManager provides the option to "Configure all ports like Port 1".

If you use this option, Cisco CallManager automatically configures 49 ports, rather than 48. You can delete port 49; it is not functional.

### Adding the VG248 Gateway to Cisco CallManager

With Cisco CallManager 3.2, you must manually add the VG248 as a gateway following this procedure:

Step 1 In Cisco CallManager, choose Devices > Add a New Device > Cisco VG248 Gateway .

Step 2 Enter this information for the gateway:

• MAC Address—Enter the last 10 digits of the Media Access Control (MAC) address for the VG248.

Only one MAC address exists for the Cisco VG248 Analog Phone Gateway, but Cisco CallManager requires unique MAC addresses for all devices. By entering only 10 digits of the MAC address, Cisco CallManager is able to use the MAC address for the gateway and append additional information to it to create the MAC addresses for the VGC phones. See the "Configuring VG248 Analog Ports" section for details.

• Description—Enter the purpose of the device, such as VG248 gateway.

Step 3 Click Insert .

Step 4 Choose 48_PORTS from the Installed Ports section.

Step 5 Click on a port to configure.

Step 6 Configure each port as described in the "Configuring VG248 Analog Ports" section .

### Configuring VG248 Analog Ports

Each port on the VG248 corresponds to an analog or SMDI device in your IP telephony network. To manage these devices using Cisco CallManager you must add each port to the Cisco CallManager database. To Cisco CallManager, each port is recognized and handled as a phone. For example, if you have 48 devices connected to the VG248, you must add and configure 48 ports to Cisco CallManager. Cisco CallManager recognizes 48 separate phones connected to it.

Note Ports 1-48 are available for use with analog devices or for SMDI connections. If you are using the VG248 with SMDI, port 00 is used to transmit and receive voice mail messages to Cisco CallManager. If you are using the VG248 for analog devices only, this port appears, but it is not functional.

Before You Begin

This procedure is identical in Cisco CallManager 3.1 and 3.2 and is also described in the Cisco VG248 Analog Phone Gateway Software Configuration Guide . It is included here for your convenience.

However, this procedure describes the process for adding analog ports to Cisco CallManager. If you are using the VG248 to integrate SMDI devices with Cisco CallManager, you must refer to the detailed procedures included in the software guide. See Chapter 5, "Integrating Cisco CallManager with Voice Mail Systems Using SMDI" in the Cisco VG248 Analog Phone Gateway Software Configuration Guide for details:

http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_1/sw_confg/vg248smd.htm

Step 1 Enter the appropriate fields, following these recommendations:

• The MAC address automatically appears based on the MAC address of the VG248, according to these guidelines:

– The first two digits of the MAC address are dropped.

– The number is shifted two places to the left.

– The two-digit port number is added to the right.

• Use the host name or other name for the Description for each port. For ease of administration, use a similar name for ports configured on the same VG248.

• Consider adding a descriptive line to the Display field, such as "Analog phone."

Step 2 Click Insert .

Step 3 To add a directory number to this phone, click OK and enter the appropriate settings.

If you need assistance entering the directory number information, refer to the documentation and online help included with Cisco CallManager for details.

## Fax Over IP Support

The VG248 supports fax pass through and Cisco fax relay using the Skinny Client Control Protocol (SCCP). For detailed information about fax support on this and other Cisco voice gateways, refer to the Implementing Fax Over IP on Cisco Voice Gateways document available from Cisco.com at the following location: http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/fxmdmnt.htm

## Resolved Caveats

Table 2 includes the list of caveats from the VG248 1.0(2) or 1.1(1) that have been resolved with this software update 1.1(2).

Table 2 VG248 1.1(1) Resolved Caveats

Bug ID

Summary

Explanation

CSCdw08369

Incorrect value returned for ciscoMemoryPoolLargestFree object in Cisco Memory Pool MIB

A software fault in the VG248 causes the incorrect value to be returned for this object.

A code change to the VG248 software corrects this behavior

CSCdw08376

Out-of-range values returned for some Cisco Process MIB objects

The allowable range for several of these objects is 1-100. However, 0 might be returned for a process that is inactive or if the VG248 as a whole is very lightly loaded.

A code change to the VG248 software corrects this behavior.

CSCdw18092

The Ethernet interface MIB object, ifOperStatus, always appears to be "down."

The per-interface object ifOperStatus defined in the RFC 1213 MIB and the Interfaces MIB derived from RFC 1573 should return "up" for the Ethernet interface. However, a software fault means that the resulting status is always "down."

A code change to the VG248 software corrects this behavior.

CSCdx07118

The VG248 uses odd number UDP ports for RTP media streams

The IETF specification RFC 1889 which defines RTP (the Real Time Protocol used for sending media streams over IP) requires that media is sent to and from even UDP port numbers. However, a defect in the VG248 software in versions prior to 1.1(2) meant that it could use either odd or even UDP port numbers for this purpose, in violation of the IETF specification.

A code change to the VG248 version 1.1(2) software corrects this behavior.

CSCuk28977

Inability to resume a held call from a shared line in some circumstances.

You cannot perform some functions using phones with a shared directory number.

For example, if a call is answered on one telephone and subsequently put on hold by that handset, it is not always possible to resume that call from a phone (connected to another VG248 port) that shares the directory number.

A code change to the VG248 version 1.1(2) software corrects this behavior.

CSCuk31381

Some calls have one-way audio only

A defect in the VG248 software can cause the VG248 to lose the ability to allocate new UDP port numbers for receiving incoming media streams. If this occurs, users with analog phones connected to a VG248 cannot hear the remote party, but the remote party can hear them.

A code change to the VG248 software corrects this behavior.

CSCuk31594

Use of shared directory number causes loss of connection to Cisco CallManager.

Under certain circumstances, the use of another telephone which is sharing a directory number with an analog handset connected to a VG248 can cause the VG248 port to drop its connection to Cisco CallManager and re-register. This is particularly apparent when the Barge feature of Cisco CallManager version 3.2(1) and above is enabled, though there may be other situations which provoke this action.

A code change to the VG248 version 1.1(2) software corrects this behavior.

CSCuk31630

SCCP "invalid length messages received" event log warnings reported

With Cisco CallManager versions 3.2(1) and above, the VG248 might report SCCP warnings in the event log with the description "invalid length message received." This is due to a small change in SCCP, which is the control protocol used by the VG248 to communicate with Cisco CallManager.

This message does not cause any problems beyond the event log warning itself. However, a small amount of verification leniency introduced in version 1.1(2) solves this problem, and the event log warning should no longer occur after upgrading to this software image.

CSCuk32122

Unexpected restart when handling SNMP GetBulk requests.

Due to a bug in the handling of SNMP v2 GetBulk request packets, the VG248 might unexpectedly restart if particular packets of this type are sent to it. The packets that produce this effect are those in which the non-repeaters count is greater than the number of VarBind objects present in the VarBindList; see the IETF specification document RFC 1905 for more details of these terms. Technically, these are invalid SNMP request packets so this defect is only likely to manifest itself when running test tools specifically designed to discover software defects; management tools intended to retrieve useful data are likely to run without issue.

A code change to the VG248 version 1.1(2) software corrects this behavior.

CSCuk32219

No INV responses generated with Keep alive SMDI number set to 0

The Keep alive SMDI numbe r is used to determine whether or not the SMDI connection is active. The attached analog voice mail system sends MWI commands and expects to receive failure indications indicating that it is connected to a device that implements the SMDI protocol. However, a defect in the VG248 1.1(1) software image prevented the VG248 from sending the required SMDI INV responses if this value was set to 0.

A code change to the VG248 version 1.1(2) software corrects this behavior.

CSCuk32400

Unexpected restart due to DSP fault under certain circumstances

In rare cases a particular sequence of packets and timings can cause a Digital Signal Processor (DSP) component to cease operations. Due to the architecture of the VG248, this causes either four analog ports to stop working or, in the worst case, the VG248 unit to restart. In the event of a restart, all calls active when the DSP fault occurred are dropped.

Version 1.1(2) of the VG248 software contains a change which limits the effect of any such fault to a brief pause in audio on the four affected ports.

CSCuk32665

Unexpected restart when handling SNMP packets containing invalid ASN1 constructs

Due to a bug in the parsing and validation of the ASN1 encoding used by SNMP, the VG248 might unexpectedly restart if a particular type of error is present in an SNMP packet sent to the VG248. If a packet is received that uses the long form of the Basic Encoding Rules contents length with a very large invalid value, the validation software might fail to detect the error. Later processing of the packet is likely to result in an invalid memory access. See the ITU specification X.209 for a full explanation of the Basic Encoding Rules.

A code change to the VG248 version 1.1(2) software corrects this behavior.

CSCuk33322

No data sent on Async 1 link to a voice mail system not supporting serial DSR

The VG248 uses the serial DSR signals on the Async 1 and Async 2 connections to determine whether those links are active. The current status of the links displays on the Display > System status screen. Also, when an Async link is active, the appropriate LED on the front panel is lit. No data transmission is attempted on an Async link that is inactive. So, analog voice mail integration does not operate correctly if the voice mail system does not assert the RS232 DSR signal on its SMDI link.

A code change in VG248 software version 1.1(2) means that transmission now takes place on Async 1 regardless whether the attached device asserts the DSR signal. Async 2 transmission, however (used in the chained and multiplexed configurations), remains controlled by the presence of DSR. The VG248 halts transmission of Message Waiting Indicator commands and queues them internally until the link is reactivated. This makes it robust against temporary cabling faults such as the link being briefly disconnected.

## Open Caveats

Open caveats are unexpected behaviors or defects in the software releases for a product. Table 3 contains information about known problems for the VG248.

If you have a Cisco.com account, you can search for known problems on the Cisco bug tracking system tool, called Bug Toolkit. To access Bug Toolkit do one of the following tasks using a web browser:

• Enter http://www.cisco.com/cgi-bin/Support/Bugtool/launch_bugtool.pl .

• Log in to Cisco.com and choose Service & Support > Technical Support Help-Cisco TAC > Tool Index > Software Bug Toolkit .

Table 3 VG248 Open Caveats

Bug ID

Summary

Explanation

CSCdu44880

Audio volume is reduced on extensions with a Ringer Equivalence Number (REN) of three.

The VG248 supports a maximum REN of three per port. This means that as many as three devices, each with a REN of one, can be connected as extensions to a single VG248 port. The VG248 allows a maximum of two devices to be off hook at any time.

The VG248 will not be damaged if devices with a total REN greater than two are off hook at the same time on a single port, but users on these extensions might experience quieter audio than normal, and possibly no audio at all.

To work around this problem, ensure that no more than two extensions on a single port are off hook at the same time. To, do this, restrict the total REN of all extensions on a port to two.

For more information, refer to the section "Connecting Too Many Phones to the VG248" in the Cisco VG248 Analog Phone Gateway Software Configuration Guide :

http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/soft_con/vg248swt.htm#xtocid154706

CSCdu54384

VG248 loses audio during excess broadcast network traffic.

If the VG248 is attached to a network on which a large amount of broadcast traffic occurs, this traffic might have adverse effects on the operation of the VG248. These effects include reduced audio quality and, in extreme circumstances, loss of Cisco CallManager registration for some ports. If the latter situation arises, a large number of discarded packets are reported (both for receive and transmit) on the VG248 Network Statistics screen. To get to the Network Statistics screen from the Main screen, select Display > Network statistics .

These situations would occur only if the broadcast traffic were to exceed several Megabits per second. This is far higher than the normal rate and likely would cause other network problems.

The workaround is to identify the source of the broadcast data and prevent it from generating excessive amounts of network traffic. The VG248 will recover and recommence normal operation once the excessive broadcast condition ceases.

CSCdu57118

FTP sessions to the VG248 will be disconnected after 10 minutes of inactivity.

When an FTP connection has been established to the VG248 (typically for the purposes of performing a software upgrade), and has been left idle for 10 minutes, the VG248 automatically disconnects that session.

CSCdu59990

Successive VG248 ports are not guaranteed to obtain sequential directory numbers when registering with Cisco CallManager in auto-registration mode.

On start up, the VG248 attempts to register all its enabled ports with Cisco CallManager in numerical order. However, this numerical registration of directories is not guaranteed. One reason numerical registration might not be successful is that there might not be large enough contiguous blocks of directory numbers available.

To work around this problem, manually create the ports in Cisco CallManager before enabling them on the VG248. You must know the device name that the VG248 will give to each port; this name is normally derived from the VG248 MAC address. You can then explicitly assign directory numbers to ports, thus following any desired pattern.

For more information, refer to the chapter "Configuring Analog Phones Using Cisco CallManager" in the Cisco VG248 Analog Phone Gateway Software Configuration Guide :

http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/soft_con/vg248swp.htm

CSCdu60375

VG248 port status shows up as "Not Found" in Cisco CallManager.

The VG248 requires Cisco CallManager version 3.1(1) or greater. However, version 3.1(1) and certain other Cisco CallManager versions do not contain support for the VG248 within the Real-time Information Service, which is used to collect information for display through the Cisco CallManager web interface. Therefore, the current status of VG248 port registrations is not available for these versions of Cisco CallManager.

This is solely a display problem; VG248 ports are able to register successfully with all versions of Cisco CallManager from 3.1(1) onwards. The ability of the ports to perform all required telephony operations is not affected by the lack of support by the Real-time Information Service.

CSCdu62479

Loss of functionality due to insufficient network bandwidth.

Cisco recommends that you connect the VG248 to a switch or router port capable of full duplex operation. In addition, Cisco recommends that this port be capable of running at 100 Mbps. If there is insufficient network bandwidth available, reduced audio quality is likely to occur. Also, some ports might lose their Cisco CallManager registrations.

The bandwidth requirement does not apply only to the connection between the VG248 and the Ethernet port to which the VG248 is attached. The same capacity is potentially required at each intermediate connection in the path to remote endpoints or gateways. For example, if the route to the rest of the VoIP network involves a 1.5-Mbps T1 link, this is likely to result in losses of functionality on all but the most lightly loaded VG248.

CSCdu79519

Voltage might be too low for Message Waiting Indication (MWI) lamps on some phones.

Some older phones that use MWI lamps might not light up, even if the VG248 port is configured to indicate Message Waiting with the Lamp setting. To check this setting, choose Telephony > Port specific parameters > MWI type from the Main screen:

This problem arises because these MWI lamps require a line voltage greater than the maximum voltage that the VG248 can supply.

If you suspect that your MWI lamp should be lit, check the configuration of the port and the status of the messages in your mailbox. If the configuration is correct and you have a waiting message, you should try replacing the phone with one of a similar type to confirm that your phone is not faulty. If the lamp still does not light, you probably have a phone that cannot have its MWI lamp lit by the VG248. Other phone functionality is not impaired by the lamp deficiency.

The only workaround to this problem is to consider replacing your phone. Test the new phone before committing to a large purchase.

CSCdu84588

Interrupted FTP put operation might leave a partial file present on the VG248 filing system.

If you are using an FTP put operation to write a file to the VG248 internal filing system, and the operation is interrupted, a portion of the file might remain on the VG248 system. In such a scenario, if the partial file is a software build-image file, the VG248 will probably fail when restarted.

To work around this problem, always check the size of the file after the transfer to make sure it is the same size as the original file. If it is not the same size, re-attempt the file transfer.

For more information, refer to the "Resolving an Incomplete Upgrade" section in the Cisco VG248 Analog Phone Gateway Software Configuration Guide :

http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/soft_con/vg248swt.htm#xtocid1547015

CSCdv36727

Silence suppression is always reported as off .

When a call is in progress, the VG248 per-port status screen displays the codec in use and indicates whether silence suppression is active.

Silence suppression, which is configurable in Cisco CallManager, means that no media packets will be transmitted if they contain silence. Transmission will resume once the user commences speaking.

The VG248 does not support the silence-suppression feature; therefore this setting will always be off . However, the VG248 can communicate with parties performing silence suppression, so you can allow this feature to remain enabled in Cisco CallManager.

CSCdv37478

Unable to achieve modem connection speeds greater than 33.6 kbps per second.

Running a modem connection through a VG248 port involves complex conversions between the VG248 and the far end-modem. Therefore, normal modem speeds might range from 28.8 to 33.6 kbps.

Some modems might run at speeds slower than 28.8 kbps per second.

For best performance, Cisco recommends that ports intended for use with modems are configured with Cisco CallManager to use only G.711 media.

CSCdv87437

Failure to connect with Cisco CallManager in auto-registration mode

The VG248 should be able to connect to Cisco CallManager using auto-registration or manual registration. However, auto-registration might not work with some versions of Cisco CallManager 3.1 and 3.2.

To avoid this problem, configure the VG248 ports in Cisco CallManager before enabling them on the VG248 itself.

For more information, refer to the "Configuring Analog Phones Using Cisco CallManager" section in the Cisco VG248 Analog Phone Gateway Software Configuration Guide :

http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/soft_con/vg248swp.htm

CSCdw25272

Async LEDs light even if serial settings are incorrect

An analog voice mail system or PBX attached to one of the Async ports on the VG248 via a serial connection must have its own serial interface running with settings matching those on the VG248. Specifically, these settings are: 9600 baud, 8 data bits, no parity, 1 stop bit and no flow control.

When the Async 1 or Async 2 port has a serial connection to a voice mail system or PBX, the corresponding LED on the VG248 front panel should light, indicating the link is established at the hardware level. However, a lit LED does not necessarily indicate that the speed and parity settings are correctly matched.

If you experience problems using SMDI, check that the necessary Async 1 or Async 2 LEDs are lit, and then check the serial interface settings of the voice mail system or PBX.

CSCuk25852

FTP directory listing on VG248 does not show correct date information.

When you issue a directory listing command in an FTP session, the date stamp for each file is shown as "Jan 1, 1900." This is because the VG248 filing system does not store a date or time for its files. However, because some FTP client programs normally show such information in directory listings, the VG248 displays a fixed date value for those clients for compatibility reasons.

CSCuk27560

Message Waiting Indicator might cause some modems connected to VG248 to erroneously detect ringing.

If a VG248 port is configured to indicate Message Waiting with the Lamp setting configured, and there is a message waiting, then a modem connected to this port might falsely detect a ringing condition. If the modem is configured to auto-answer, it might also attempt to answer the call. In some cases, this situation can prevent the modem from making an outgoing call (even if auto-answer is not configured). From the main screen on the VG248 choose Configure > Telephony > Port specific parameters > MWI type to change the MWI type.

Not all modems detect the lamp Message Waiting Indication (MWI) as ringing, and those that do are typically not prevented from making outgoing calls altogether, although some attempts might fail.

The workaround for this problem is to disable the Lamp MWI for this port (ideally disable MWI altogether). If this is not possible or is impractical, then the problem might be cleared by retrieving the waiting message, then cancelling the MWI. Furthermore, you should disable auto-answer on modems connected to VG248 ports that have the Lamp MWI setting configured.

CSCuk27613

Fax machines connected to the VG248 might return to the on-hook condition immediately after answering an incoming call.

When the VG248 receives an incoming call, Caller Identification (CID) is sent along with the signal in order for the called device to ring. In some countries, CID information is sent between the first and second rings, while in other countries it is sent just before the first ring.

In cases where the CID information arrives before the first ring, some fax machines answer the call but immediately hang up.

To work around this problem, disable Caller Identification for VG248 ports to which a fax machine is connected. To do this, choose Configure > Telephony > Port specific parameters from the main menu on the VG248.

CSCuk27761

Message Waiting Indicator (MWI) might not behave as expected after a configuration change.

The VG248 supports three methods of Message Waiting Indication (MWI):

• Lamp

• Caller ID

• stutter

You can select any of these three methods, pairings of the methods, or no MWI at all (from the main screen select Telephony > Port specific parameters > MWI type ). The display on the phone will not necessarily be updated to reflect configuration changes you make.

The MWI Caller ID (CID) option is affected by whether incoming call Caller Identification is enabled or disabled for a port.

To work around these issues, clear all Caller Identification information before changing the MWI configuration for a given port. Then, manually check for waiting messages once the configuration is finalized.

CSCdv90121

Certain modem calls may fail if fax relay is enabled

Certain modems, when connected to the VG248, send signals during operation that the VG248 detects as fax tones. If the VG248 is configured with Cisco fax relay enabled and the Cisco fax relay negotiation between the VG248 and the remote party is successful, a Cisco fax relay connection initiates between the two endpoints. However, this Cisco fax relay connection is not suitable for general modem traffic, and the modem call fails soon after it has been established.

The only workaround for this problem is to disable the use of Cisco fax relay and to rely on fax pass through instead. In VG248 software images prior to 1.1(2), you must disable Cisco fax relay for the entire device. With version 1.1(2), you can disable fax relay on a per-port basis. See "Enabling Fax Relay Per Port" section for details. Ensure that Cisco fax relay is enabled on only those ports to which fax machines are connected.

CSCdw54749

Large amounts of input gain may cause dialing problems

The Input gain setting determines how much to increase or decrease the volume of audio from the attached analog handset before sending it across the IP Telephony network. The default value is 0dB, which leaves the audio unchanged, but can range from -6dB to +14dB. With certain telephone handsets, if this parameter is set to too high a value (for example, 12dB or higher), problems might occur when dialing digits. These problems result because dialing digits involves sending certain frequencies of tone from the telephone to the VG248. If the volume of these tones is increased to such an extent that they become distorted, the VG248 cannot recognize them properly.

## Obtaining Documentation

The following sections explain how to obtain documentation from Cisco Systems.

### World Wide Web

You can access the most current Cisco documentation on the World Wide Web at the following URL:

http://www.cisco.com

Translated documentation is available at the following URL:

http://www.cisco.com/public/countries_languages.shtml

### Documentation CD-ROM

Cisco documentation and additional literature are available in a Cisco Documentation CD-ROM package, which is shipped with your product. The Documentation CD-ROM is updated monthly and may be more current than printed documentation. The CD-ROM package is available as a single unit or through an annual subscription.

### Ordering Documentation

Cisco documentation is available in the following ways:

• Registered Cisco Direct Customers can order Cisco product documentation from the Networking Products MarketPlace:

http://www.cisco.com/web/ordering/root/index.html

• Registered Cisco.com users can order the Documentation CD-ROM through the online Subscription Store:

http://www.cisco.com/go/subscription

• Nonregistered Cisco.com users can order documentation through a local account representative by calling Cisco corporate headquarters (California, USA) at 408 526-7208 or, elsewhere in North America, by calling 800 553-NETS (6387).

### Documentation Feedback

If you are reading Cisco product documentation on Cisco.com, you can submit technical comments electronically. Click Leave Feedback at the bottom of the Cisco Documentation home page. After you complete the form, print it out and fax it to Cisco at 408 527-0730.

You can e-mail your comments to bug-doc@cisco.com.

To submit your comments by mail, use the response card behind the front cover of your document, or write to the following address:

Cisco Systems Attn: Document Resource Connection 170 West Tasman Drive San Jose, CA 95134-9883

We appreciate your comments.

## Obtaining Technical Assistance

Cisco provides Cisco.com as a starting point for all technical assistance. Customers and partners can obtain documentation, troubleshooting tips, and sample configurations from online tools by using the Cisco Technical Assistance Center (TAC) Web Site. Cisco.com registered users have complete access to the technical support resources on the Cisco TAC Web Site.

### Cisco.com

Cisco.com is the foundation of a suite of interactive, networked services that provides immediate, open access to Cisco information, networking solutions, services, programs, and resources at any time, from anywhere in the world.

Cisco.com is a highly integrated Internet application and a powerful, easy-to-use tool that provides a broad range of features and services to help you to

• Streamline business processes and improve productivity

• Resolve technical issues with online support

• Download and test software packages

• Order Cisco learning materials and merchandise

• Register for online skill assessment, training, and certification programs

You can self-register on Cisco.com to obtain customized information and service. To access Cisco.com, go to the following URL:

http://www.cisco.com

### Technical Assistance Center

The Cisco TAC is available to all customers who need technical assistance with a Cisco product, technology, or solution. Two types of support are available through the Cisco TAC: the Cisco TAC Web Site and the Cisco TAC Escalation Center.

Inquiries to Cisco TAC are categorized according to the urgency of the issue:

• Priority level 4 (P4)—You need information or assistance concerning Cisco product capabilities, product installation, or basic product configuration.

• Priority level 3 (P3)—Your network performance is degraded. Network functionality is noticeably impaired, but most business operations continue.

• Priority level 2 (P2)—Your production network is severely degraded, affecting significant aspects of business operations. No workaround is available.

• Priority level 1 (P1)—Your production network is down, and a critical impact to business operations will occur if service is not restored quickly. No workaround is available.

Which Cisco TAC resource you choose is based on the priority of the problem and the conditions of service contracts, when applicable.

### Cisco TAC Web Site

The Cisco TAC Web Site allows you to resolve P3 and P4 issues yourself , saving both cost and time. The site provides around-the-clock access to online tools, knowledge bases, and software. To access the Cisco TAC Web Site, go to the following URL:

http://www.cisco.com/tac

All customers, partners, and resellers who have a valid Cisco services contract have complete access to the technical support resources on the Cisco TAC Web Site. The Cisco TAC Web Site requires a Cisco.com login ID and password. If you have a valid service contract but do not have a login ID or password, go to the following URL to register:

http://www.cisco.com/register/

If you cannot resolve your technical issues by using the Cisco TAC Web Site, and you are a Cisco.com registered user, you can open a case online by using the TAC Case Open tool at the following URL:

http://www.cisco.com/tac/caseopen

If you have Internet access, it is recommended that you open P3 and P4 cases through the Cisco TAC Web Site.

### Cisco TAC Escalation Center

The Cisco TAC Escalation Center addresses issues that are classified as priority level 1 or priority level 2; these classifications are assigned when severe network degradation significantly impacts business operations. When you contact the TAC Escalation Center with a P1 or P2 problem, a Cisco TAC engineer will automatically open a case.

To obtain a directory of toll-free Cisco TAC telephone numbers for your country, go to the following URL:

http://www.cisco.com/warp/public/687/Directory/DirTAC.shtml

Before calling, please check with your network operations center to determine the level of Cisco support services to which your company is entitled; for example, SMARTnet, SMARTnet Onsite, or Network Supported Accounts (NSA). In addition, please have available your service agreement number and your product serial number.

### CCIP, the Cisco Powered Network mark, the Cisco Systems Verified logo, Cisco Unity, Follow Me Browsing, FormShare, Internet Quotient, iQ Breakthrough, iQ Expertise, iQ FastTrack, the iQ Logo, iQ Net Readiness Scorecard, Networking Academy, ScriptShare, SMARTnet, TransPath, and Voice LAN are trademarks of Cisco Systems, Inc.; Changing the Way We Work, Live, Play, and Learn, Discover All That's Possible, The Fastest Way to Increase Your Internet Quotient, and iQuick Study are service marks of Cisco Systems, Inc.; and Aironet, ASIST, BPX, Catalyst, CCDA, CCDP, CCIE, CCNA, CCNP, Cisco, the Cisco Certified Internetwork Expert logo, Cisco IOS, the Cisco IOS logo, Cisco Press, Cisco Systems, Cisco Systems Capital, the Cisco Systems logo, Empowering the Internet Generation, Enterprise/Solver, EtherChannel, EtherSwitch, Fast Step, GigaStack, IOS, IP/TV, LightStream, MGX, MICA, the Networkers logo, Network Registrar, Packet , PIX, Post-Routing, Pre-Routing, RateMUX, Registrar, SlideCast, StrataView Plus, Stratm, SwitchProbe, TeleRouter, and VCO are registered trademarks of Cisco Systems, Inc. and/or its affiliates in the U.S. and certain other countries.

### All other trademarks mentioned in this document or Web site are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (0203R)

### Copyright © 2001-2002, Cisco Systems, Inc. All rights reserved.

### This Document Applies to These Products

- VG Series Gateways

| Document Title | Description | Where to Find It |
|---|---|---|
| Cisco VG248 Analog Phone Gateway Hardware Installation Guide | Provides the site preparation, safety information, and hardware installation and setup instructions to safely install the VG248. | • In the box—A printed version of this document ships with the product • Online at Cisco.com—HTML and PDF versions of this document are available from Cisco.com: http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/hard_ins/index.htm • By ordering—See the "Obtaining Documentation" section for details |
| Cisco VG248 Analog Phone Gateway Software Configuration Guide | Provides information about understanding, configuring, managing, and troubleshooting the VG248. | Online at Cisco.com—HTML and PDF versions of this document are available from Cisco.com: http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_1/sw_confg/index.htm |
| Cisco VG248 Analog Phone Gateway Version 1.1(2) Release Notes | Describes known caveats and any documentation errata for the VG248. | Online at Cisco.com—HTML and PDF versions of this document are available from Cisco.com: http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_1/rel_note/vg248rn3.htm |

| Bug ID | Summary | Explanation |
|---|---|---|
| CSCdw08369 | Incorrect value returned for ciscoMemoryPoolLargestFree object in Cisco Memory Pool MIB | A software fault in the VG248 causes the incorrect value to be returned for this object. A code change to the VG248 software corrects this behavior |
| CSCdw08376 | Out-of-range values returned for some Cisco Process MIB objects | The allowable range for several of these objects is 1-100. However, 0 might be returned for a process that is inactive or if the VG248 as a whole is very lightly loaded. A code change to the VG248 software corrects this behavior. |
| CSCdw18092 | The Ethernet interface MIB object, ifOperStatus, always appears to be "down." | The per-interface object ifOperStatus defined in the RFC 1213 MIB and the Interfaces MIB derived from RFC 1573 should return "up" for the Ethernet interface. However, a software fault means that the resulting status is always "down." A code change to the VG248 software corrects this behavior. |
| CSCdx07118 | The VG248 uses odd number UDP ports for RTP media streams | The IETF specification RFC 1889 which defines RTP (the Real Time Protocol used for sending media streams over IP) requires that media is sent to and from even UDP port numbers. However, a defect in the VG248 software in versions prior to 1.1(2) meant that it could use either odd or even UDP port numbers for this purpose, in violation of the IETF specification. A code change to the VG248 version 1.1(2) software corrects this behavior. |
| CSCuk28977 | Inability to resume a held call from a shared line in some circumstances. | You cannot perform some functions using phones with a shared directory number. For example, if a call is answered on one telephone and subsequently put on hold by that handset, it is not always possible to resume that call from a phone (connected to another VG248 port) that shares the directory number. A code change to the VG248 version 1.1(2) software corrects this behavior. |
| CSCuk31381 | Some calls have one-way audio only | A defect in the VG248 software can cause the VG248 to lose the ability to allocate new UDP port numbers for receiving incoming media streams. If this occurs, users with analog phones connected to a VG248 cannot hear the remote party, but the remote party can hear them. A code change to the VG248 software corrects this behavior. |
| CSCuk31594 | Use of shared directory number causes loss of connection to Cisco CallManager. | Under certain circumstances, the use of another telephone which is sharing a directory number with an analog handset connected to a VG248 can cause the VG248 port to drop its connection to Cisco CallManager and re-register. This is particularly apparent when the Barge feature of Cisco CallManager version 3.2(1) and above is enabled, though there may be other situations which provoke this action. A code change to the VG248 version 1.1(2) software corrects this behavior. |
| CSCuk31630 | SCCP "invalid length messages received" event log warnings reported | With Cisco CallManager versions 3.2(1) and above, the VG248 might report SCCP warnings in the event log with the description "invalid length message received." This is due to a small change in SCCP, which is the control protocol used by the VG248 to communicate with Cisco CallManager. This message does not cause any problems beyond the event log warning itself. However, a small amount of verification leniency introduced in version 1.1(2) solves this problem, and the event log warning should no longer occur after upgrading to this software image. |
| CSCuk32122 | Unexpected restart when handling SNMP GetBulk requests. | Due to a bug in the handling of SNMP v2 GetBulk request packets, the VG248 might unexpectedly restart if particular packets of this type are sent to it. The packets that produce this effect are those in which the non-repeaters count is greater than the number of VarBind objects present in the VarBindList; see the IETF specification document RFC 1905 for more details of these terms. Technically, these are invalid SNMP request packets so this defect is only likely to manifest itself when running test tools specifically designed to discover software defects; management tools intended to retrieve useful data are likely to run without issue. A code change to the VG248 version 1.1(2) software corrects this behavior. |
| CSCuk32219 | No INV responses generated with Keep alive SMDI number set to 0 | The Keep alive SMDI numbe r is used to determine whether or not the SMDI connection is active. The attached analog voice mail system sends MWI commands and expects to receive failure indications indicating that it is connected to a device that implements the SMDI protocol. However, a defect in the VG248 1.1(1) software image prevented the VG248 from sending the required SMDI INV responses if this value was set to 0. A code change to the VG248 version 1.1(2) software corrects this behavior. |
| CSCuk32400 | Unexpected restart due to DSP fault under certain circumstances | In rare cases a particular sequence of packets and timings can cause a Digital Signal Processor (DSP) component to cease operations. Due to the architecture of the VG248, this causes either four analog ports to stop working or, in the worst case, the VG248 unit to restart. In the event of a restart, all calls active when the DSP fault occurred are dropped. Version 1.1(2) of the VG248 software contains a change which limits the effect of any such fault to a brief pause in audio on the four affected ports. |
| CSCuk32665 | Unexpected restart when handling SNMP packets containing invalid ASN1 constructs | Due to a bug in the parsing and validation of the ASN1 encoding used by SNMP, the VG248 might unexpectedly restart if a particular type of error is present in an SNMP packet sent to the VG248. If a packet is received that uses the long form of the Basic Encoding Rules contents length with a very large invalid value, the validation software might fail to detect the error. Later processing of the packet is likely to result in an invalid memory access. See the ITU specification X.209 for a full explanation of the Basic Encoding Rules. A code change to the VG248 version 1.1(2) software corrects this behavior. |
| CSCuk33322 | No data sent on Async 1 link to a voice mail system not supporting serial DSR | The VG248 uses the serial DSR signals on the Async 1 and Async 2 connections to determine whether those links are active. The current status of the links displays on the Display > System status screen. Also, when an Async link is active, the appropriate LED on the front panel is lit. No data transmission is attempted on an Async link that is inactive. So, analog voice mail integration does not operate correctly if the voice mail system does not assert the RS232 DSR signal on its SMDI link. A code change in VG248 software version 1.1(2) means that transmission now takes place on Async 1 regardless whether the attached device asserts the DSR signal. Async 2 transmission, however (used in the chained and multiplexed configurations), remains controlled by the presence of DSR. The VG248 halts transmission of Message Waiting Indicator commands and queues them internally until the link is reactivated. This makes it robust against temporary cabling faults such as the link being briefly disconnected. |

| Bug ID | Summary | Explanation |
|---|---|---|
| CSCdu44880 | Audio volume is reduced on extensions with a Ringer Equivalence Number (REN) of three. | The VG248 supports a maximum REN of three per port. This means that as many as three devices, each with a REN of one, can be connected as extensions to a single VG248 port. The VG248 allows a maximum of two devices to be off hook at any time. The VG248 will not be damaged if devices with a total REN greater than two are off hook at the same time on a single port, but users on these extensions might experience quieter audio than normal, and possibly no audio at all. To work around this problem, ensure that no more than two extensions on a single port are off hook at the same time. To, do this, restrict the total REN of all extensions on a port to two. For more information, refer to the section "Connecting Too Many Phones to the VG248" in the Cisco VG248 Analog Phone Gateway Software Configuration Guide : http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/soft_con/vg248swt.htm#xtocid154706 |
| CSCdu54384 | VG248 loses audio during excess broadcast network traffic. | If the VG248 is attached to a network on which a large amount of broadcast traffic occurs, this traffic might have adverse effects on the operation of the VG248. These effects include reduced audio quality and, in extreme circumstances, loss of Cisco CallManager registration for some ports. If the latter situation arises, a large number of discarded packets are reported (both for receive and transmit) on the VG248 Network Statistics screen. To get to the Network Statistics screen from the Main screen, select Display > Network statistics . These situations would occur only if the broadcast traffic were to exceed several Megabits per second. This is far higher than the normal rate and likely would cause other network problems. The workaround is to identify the source of the broadcast data and prevent it from generating excessive amounts of network traffic. The VG248 will recover and recommence normal operation once the excessive broadcast condition ceases. |
| CSCdu57118 | FTP sessions to the VG248 will be disconnected after 10 minutes of inactivity. | When an FTP connection has been established to the VG248 (typically for the purposes of performing a software upgrade), and has been left idle for 10 minutes, the VG248 automatically disconnects that session. |
| CSCdu59990 | Successive VG248 ports are not guaranteed to obtain sequential directory numbers when registering with Cisco CallManager in auto-registration mode. | On start up, the VG248 attempts to register all its enabled ports with Cisco CallManager in numerical order. However, this numerical registration of directories is not guaranteed. One reason numerical registration might not be successful is that there might not be large enough contiguous blocks of directory numbers available. To work around this problem, manually create the ports in Cisco CallManager before enabling them on the VG248. You must know the device name that the VG248 will give to each port; this name is normally derived from the VG248 MAC address. You can then explicitly assign directory numbers to ports, thus following any desired pattern. For more information, refer to the chapter "Configuring Analog Phones Using Cisco CallManager" in the Cisco VG248 Analog Phone Gateway Software Configuration Guide : http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/soft_con/vg248swp.htm |
| CSCdu60375 | VG248 port status shows up as "Not Found" in Cisco CallManager. | The VG248 requires Cisco CallManager version 3.1(1) or greater. However, version 3.1(1) and certain other Cisco CallManager versions do not contain support for the VG248 within the Real-time Information Service, which is used to collect information for display through the Cisco CallManager web interface. Therefore, the current status of VG248 port registrations is not available for these versions of Cisco CallManager. This is solely a display problem; VG248 ports are able to register successfully with all versions of Cisco CallManager from 3.1(1) onwards. The ability of the ports to perform all required telephony operations is not affected by the lack of support by the Real-time Information Service. |
| CSCdu62479 | Loss of functionality due to insufficient network bandwidth. | Cisco recommends that you connect the VG248 to a switch or router port capable of full duplex operation. In addition, Cisco recommends that this port be capable of running at 100 Mbps. If there is insufficient network bandwidth available, reduced audio quality is likely to occur. Also, some ports might lose their Cisco CallManager registrations. The bandwidth requirement does not apply only to the connection between the VG248 and the Ethernet port to which the VG248 is attached. The same capacity is potentially required at each intermediate connection in the path to remote endpoints or gateways. For example, if the route to the rest of the VoIP network involves a 1.5-Mbps T1 link, this is likely to result in losses of functionality on all but the most lightly loaded VG248. |
| CSCdu79519 | Voltage might be too low for Message Waiting Indication (MWI) lamps on some phones. | Some older phones that use MWI lamps might not light up, even if the VG248 port is configured to indicate Message Waiting with the Lamp setting. To check this setting, choose Telephony > Port specific parameters > MWI type from the Main screen: This problem arises because these MWI lamps require a line voltage greater than the maximum voltage that the VG248 can supply. If you suspect that your MWI lamp should be lit, check the configuration of the port and the status of the messages in your mailbox. If the configuration is correct and you have a waiting message, you should try replacing the phone with one of a similar type to confirm that your phone is not faulty. If the lamp still does not light, you probably have a phone that cannot have its MWI lamp lit by the VG248. Other phone functionality is not impaired by the lamp deficiency. The only workaround to this problem is to consider replacing your phone. Test the new phone before committing to a large purchase. |
| CSCdu84588 | Interrupted FTP put operation might leave a partial file present on the VG248 filing system. | If you are using an FTP put operation to write a file to the VG248 internal filing system, and the operation is interrupted, a portion of the file might remain on the VG248 system. In such a scenario, if the partial file is a software build-image file, the VG248 will probably fail when restarted. To work around this problem, always check the size of the file after the transfer to make sure it is the same size as the original file. If it is not the same size, re-attempt the file transfer. For more information, refer to the "Resolving an Incomplete Upgrade" section in the Cisco VG248 Analog Phone Gateway Software Configuration Guide : http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/soft_con/vg248swt.htm#xtocid1547015 |
| CSCdv36727 | Silence suppression is always reported as off . | When a call is in progress, the VG248 per-port status screen displays the codec in use and indicates whether silence suppression is active. Silence suppression, which is configurable in Cisco CallManager, means that no media packets will be transmitted if they contain silence. Transmission will resume once the user commences speaking. The VG248 does not support the silence-suppression feature; therefore this setting will always be off . However, the VG248 can communicate with parties performing silence suppression, so you can allow this feature to remain enabled in Cisco CallManager. |
| CSCdv37478 | Unable to achieve modem connection speeds greater than 33.6 kbps per second. | Running a modem connection through a VG248 port involves complex conversions between the VG248 and the far end-modem. Therefore, normal modem speeds might range from 28.8 to 33.6 kbps. Some modems might run at speeds slower than 28.8 kbps per second. For best performance, Cisco recommends that ports intended for use with modems are configured with Cisco CallManager to use only G.711 media. |
| CSCdv87437 | Failure to connect with Cisco CallManager in auto-registration mode | The VG248 should be able to connect to Cisco CallManager using auto-registration or manual registration. However, auto-registration might not work with some versions of Cisco CallManager 3.1 and 3.2. To avoid this problem, configure the VG248 ports in Cisco CallManager before enabling them on the VG248 itself. For more information, refer to the "Configuring Analog Phones Using Cisco CallManager" section in the Cisco VG248 Analog Phone Gateway Software Configuration Guide : http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/soft_con/vg248swp.htm |
| CSCdw25272 | Async LEDs light even if serial settings are incorrect | An analog voice mail system or PBX attached to one of the Async ports on the VG248 via a serial connection must have its own serial interface running with settings matching those on the VG248. Specifically, these settings are: 9600 baud, 8 data bits, no parity, 1 stop bit and no flow control. When the Async 1 or Async 2 port has a serial connection to a voice mail system or PBX, the corresponding LED on the VG248 front panel should light, indicating the link is established at the hardware level. However, a lit LED does not necessarily indicate that the speed and parity settings are correctly matched. If you experience problems using SMDI, check that the necessary Async 1 or Async 2 LEDs are lit, and then check the serial interface settings of the voice mail system or PBX. |
| CSCuk25852 | FTP directory listing on VG248 does not show correct date information. | When you issue a directory listing command in an FTP session, the date stamp for each file is shown as "Jan 1, 1900." This is because the VG248 filing system does not store a date or time for its files. However, because some FTP client programs normally show such information in directory listings, the VG248 displays a fixed date value for those clients for compatibility reasons. |
| CSCuk27560 | Message Waiting Indicator might cause some modems connected to VG248 to erroneously detect ringing. | If a VG248 port is configured to indicate Message Waiting with the Lamp setting configured, and there is a message waiting, then a modem connected to this port might falsely detect a ringing condition. If the modem is configured to auto-answer, it might also attempt to answer the call. In some cases, this situation can prevent the modem from making an outgoing call (even if auto-answer is not configured). From the main screen on the VG248 choose Configure > Telephony > Port specific parameters > MWI type to change the MWI type. Not all modems detect the lamp Message Waiting Indication (MWI) as ringing, and those that do are typically not prevented from making outgoing calls altogether, although some attempts might fail. The workaround for this problem is to disable the Lamp MWI for this port (ideally disable MWI altogether). If this is not possible or is impractical, then the problem might be cleared by retrieving the waiting message, then cancelling the MWI. Furthermore, you should disable auto-answer on modems connected to VG248 ports that have the Lamp MWI setting configured. |
| CSCuk27613 | Fax machines connected to the VG248 might return to the on-hook condition immediately after answering an incoming call. | When the VG248 receives an incoming call, Caller Identification (CID) is sent along with the signal in order for the called device to ring. In some countries, CID information is sent between the first and second rings, while in other countries it is sent just before the first ring. In cases where the CID information arrives before the first ring, some fax machines answer the call but immediately hang up. To work around this problem, disable Caller Identification for VG248 ports to which a fax machine is connected. To do this, choose Configure > Telephony > Port specific parameters from the main menu on the VG248. |
| CSCuk27761 | Message Waiting Indicator (MWI) might not behave as expected after a configuration change. | The VG248 supports three methods of Message Waiting Indication (MWI): • Lamp • Caller ID • stutter You can select any of these three methods, pairings of the methods, or no MWI at all (from the main screen select Telephony > Port specific parameters > MWI type ). The display on the phone will not necessarily be updated to reflect configuration changes you make. The MWI Caller ID (CID) option is affected by whether incoming call Caller Identification is enabled or disabled for a port. To work around these issues, clear all Caller Identification information before changing the MWI configuration for a given port. Then, manually check for waiting messages once the configuration is finalized. |
| CSCdv90121 | Certain modem calls may fail if fax relay is enabled | Certain modems, when connected to the VG248, send signals during operation that the VG248 detects as fax tones. If the VG248 is configured with Cisco fax relay enabled and the Cisco fax relay negotiation between the VG248 and the remote party is successful, a Cisco fax relay connection initiates between the two endpoints. However, this Cisco fax relay connection is not suitable for general modem traffic, and the modem call fails soon after it has been established. The only workaround for this problem is to disable the use of Cisco fax relay and to rely on fax pass through instead. In VG248 software images prior to 1.1(2), you must disable Cisco fax relay for the entire device. With version 1.1(2), you can disable fax relay on a per-port basis. See "Enabling Fax Relay Per Port" section for details. Ensure that Cisco fax relay is enabled on only those ports to which fax machines are connected. |
| CSCdw54749 | Large amounts of input gain may cause dialing problems | The Input gain setting determines how much to increase or decrease the volume of audio from the attached analog handset before sending it across the IP Telephony network. The default value is 0dB, which leaves the audio unchanged, but can range from -6dB to +14dB. With certain telephone handsets, if this parameter is set to too high a value (for example, 12dB or higher), problems might occur when dialing digits. These problems result because dialing digits involves sending certain frequencies of tone from the telephone to the VG248. If the volume of these tones is increased to such an extent that they become distorted, the VG248 cannot recognize them properly. |