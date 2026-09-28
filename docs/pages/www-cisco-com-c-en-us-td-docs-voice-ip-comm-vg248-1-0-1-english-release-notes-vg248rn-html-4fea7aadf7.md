---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-vg248-1-0-1-english-release-notes-vg248rn-html-4fea7aadf7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/vg248/1_0_1/english/release/notes/vg248rn.html
retrieved_at: 2026-08-21T12:51:36.847039+00:00
---

Cisco VG248 Analog Phone Gateway Version 1.0 (1) Release Notes

# Cisco VG248 Analog Phone Gateway Version 1.0 (1) Release Notes

- Notes

- Notes

### Download Options

Updated: September 21, 2001

## Table Of Contents

Cisco VG248 Analog Phone Gateway Version 1.0(1) Release Notes

Documentation Roadmap

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

## Cisco VG248 Analog Phone Gateway Version 1.0(1) Release Notes

October 4, 2001

These release notes are for use with the Cisco VG248 Analog Phone Gateway with software version 1.0(1). The VG248 enables you to integrate analog telephony devices with Cisco CallManager IP telephony systems.

These release notes provide the following information:

• Documentation Roadmap

• Open Caveats

• Obtaining Documentation

• Obtaining Technical Assistance

## Documentation Roadmap

Table 1 provides summaries and locations of available documents for the Cisco VG248 Analog Phone Gateway.

Table 1 Available Documentation for the Cisco VG248

Document Title

Description

Where to Find It

Cisco VG248 Analog Phone Gateway Hardware Installation Guide

Provides the site preparation, safety information, and hardware installation and setup instructions to safely install the VG248.

• In the box—A printed version of this document ships with the product

• Online at Cisco.com—HTML and PDF versions of this document are available from Cisco.com:

http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/hard_ins/index.htm

• By ordering—See the "Ordering Documentation" section for details

Cisco VG248 Analog Phone Gateway Software Configuration Guide

Provides information about understanding, configuring, managing, and troubleshooting the VG248.

Online at Cisco.com—HTML and PDF versions of this document are available from Cisco.com:

http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/soft_con/index.htm

Cisco VG248 Analog Phone Gateway Release Notes

Describes known caveats and any documentation errata for the VG248.

Online at Cisco.com—HTML and PDF versions of this document are available from Cisco.com:

http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/rel_note/index.htm

## Open Caveats

Open caveats are unexpected behaviors or defects in the software releases for a product. Table 2 contains information on known problems for the VG248.

If you have a CCO account, you can search for known problems on the Cisco bug tracking system tool, called Bug Navigator II. To access Bug Navigator II, do one of the following tasks:

• Enter http://www.cisco.com/support/bugtools in your web browser.

• Log in to CCO and choose Service & Support  > Technical Assistance Center  > Tools  >   Software Bug Toolkit >  Bug Navigator II .

Table 2 VG248 Open Caveats

Bug ID

Summary

Explanation

CSCdu44880

Audio volume is reduced on extensions with a Ringer Equivalence Number (REN) of three.

The VG248 supports a maximum REN of three per port. This means that as many as three devices, each with a REN of one, can be connected as extensions to a single VG248 port. The VG248 allows a maximum of two devices to be off hook at any time.

The VG248 will not be damaged if devices with a total REN greater than two are off hook at the same time on a single port, but users on these extensions might experience quieter audio than normal, and possibly no audio at all.

To work around this problem, ensure that no more than two extensions on a single port are off hook at the same time. One way you can do this is by restricting the total REN of all extensions on a port to two.

For more information, refer to the section "Connecting Too Many Phones to the VG248" in the Software Configuration Guide :

http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/soft_con/vg248swt.htm#xtocid240276

CSCdu54384

VG248 loses audio during excess broadcast network traffic.

If the VG248 is attached to a network on which a large amount of broadcast traffic occurs, this traffic might have adverse effects on the operation of the VG248. These effects include reduced audio quality and, in extreme circumstances, loss of Cisco CallManager registration for some ports. If the latter situation arises, a large number of discarded packets are reported (both for receive and transmit) on the VG248 Network Statistics screen. To get to the Network Statistics screen from the Main screen, select Display > Network statistics .

These situations would occur only if the broadcast traffic were to exceed several Megabits per second. This is far higher than the normal rate and likely would cause other network problems.

The workaround is to identify the source of the broadcast data and prevent it from generating excessive amounts of network traffic. The VG248 will recover and recommence normal operation once the excessive broadcast condition ceases.

CSCdu57118

FTP sessions to the VG248 will be disconnected after 10 minutes of inactivity.

When an FTP connection has been established to the VG248 (typically for the purposes of performing a software upgrade), and has been left idle for 10 minutes, the VG248 automatically disconnects that session.

CSCdu59990

Successive VG248 ports are not guaranteed to obtain sequential directory numbers when registering with Cisco CallManager in auto-registration mode.

On start up, the VG248 attempts to register all its enabled ports with Cisco CallManager in numerical order. However, this numerical registration of directories is not guaranteed. One reason numerical registration might not be successful is that there might not be large enough contiguous blocks of directory numbers available.

To work around this problem, manually create the ports in Cisco CallManager before enabling them on the VG248. You must know the device name that the VG248 will give to each port; this name is normally derived from the VG248 MAC address. You can then explicitly assign directory numbers to ports, thus following any desired pattern.

For more information, refer to the chapter "Configuring Analog Phones Using Cisco CallManager" in the Software Configuration Guide :

http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/soft_con/vg248swp.htm

CSCdu60375

VG248 port status shows up as "Not Found" in Cisco CallManager.

The VG248 requires Cisco CallManager versions 3.1(1) or greater. However, Cisco CallManager versions prior to 3.1(2) do not contain support for the VG248 within the Real-time Information Service, which is used to collect information for display through the Cisco CallManager web interface.

Therefore, the current status of VG248 port registrations is not available for Cisco CallManager versions prior to 3.1(2).

This is solely a display problem; VG248 ports are able to register successfully with version 3.1(1). Their ability to perform all required telephony operations is not affected by the lack of support by the Real-time Information Service.

To work around this issue, upgrade to Cisco CallManager 3.1(2) or greater.

CSCdu62479

Loss of functionality due to insufficient network bandwidth.

Cisco recommends that you connect the VG248 to a switch or router port capable of full duplex operation. In addition, Cisco recommends that this port be capable of running at 100 Mbps. If there is insufficient network bandwidth available, reduced audio quality is likely to occur. Also, some ports might lose their Cisco CallManager registrations.

The bandwidth requirement does not apply only to the connection between the VG248 and the Ethernet port to which the VG248 is attached. The same capacity is potentially required at each intermediate connection in the path to remote endpoints or gateways. For example, if the route to the rest of the VoIP network involves a 1.5-Mbps T1 link, this is likely to result in losses of functionality on all but the most lightly loaded VG248.

CSCdu79519

Voltage might be too low for Message Waiting Indication (MWI) lamps on some phones.

Some older phones that use MWI lamps might not light up, even if the VG248 port is configured to indicate Message Waiting with the Lamp setting. To check this setting, go to the following path from the Main screen:

Telephony > Port specific parameters > MWI type

This problem arises because MWI lamps require a line voltage greater than the maximum voltage that the VG248 can supply.

If you suspect that your lamp MWI should be lit, check the configuration of the port and the status of the messages in your mailbox. If the configuration is correct and you have a waiting message, you should try replacing the phone with one of a similar type to confirm that your phone is not faulty. If the lamp still does not light, you probably have a phone that cannot have its MWI lamp lit by the VG248. Other phone functionality is not impaired by the lamp deficiency.

The only workaround to this problem is to consider replacing your phone. Test the new phone before committing to a large purchase.

CSCdu84588

Interrupted FTP put operation might leave a partial file present on the VG248 filing system.

If you are using an FTP put operation to write a file to the VG248 internal filing system, and the operation is interrupted, a portion of the file might remain on the VG248 system. In such a scenario, if the partial file is a software build-image file, the VG248 will probably fail when restarted.

To work around this problem, always check the size of the file after the transfer to make sure it is the same size as the original file. If it is not the same size, re-attempt the file transfer.

For more information, refer to the "Resolving an Incomplete Upgrade" section in the Software Configuration Guide :

http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/soft_con/vg248swt.htm#xtocid2402715

CSCdv36727

Silence suppression is always reported as off .

When a call is in progress, the VG248 per-port status screen displays the codec in use and indicates whether silence suppression is active.

Silence suppression, which is configurable in Cisco CallManager, means that no media packets will be transmitted if these packets would contain silence. Transmission would resume once the user commences speaking.

The VG248 does not support the silence-suppression feature; therefore this setting will always be off . However, the VG248 can communicate with parties performing silence suppression, so you can allow this feature to remain enabled in Cisco CallManager.

CSCdv37478

Unable to achieve modem connection speeds greater than 33.6 kbps per second.

Running a modem connection through a VG248 port involves complex conversions between the VG248 and the far end-modem. Therefore, normal modem speeds might range from 28.8 to 33.6 kbps.

Some modems might run at speeds slower than 28.8 kbps per second.

For best performance, Cisco recommends that ports intended for use with modems are configured with Cisco CallManager to use only G.711 media.

CSCuk25852

FTP directory listing on VG248 does not show correct date information.

When you issue a directory listing command in an FTP session, the date stamp for each file is shown as "Jan 1, 1900." This is because the VG248 filing system does not store a date or time for its files. However, because some FTP client programs normally show such information in directory listings, the VG248 displays a fixed date value for those clients for compatibility reasons.

CSCuk27560

Message Waiting Indication might cause some modems connected to VG248 to erroneously detect ringing.

If a VG248 port is configured to indicate Message Waiting with the Lamp setting configured, and there is a message waiting, then a modem connected to this port might falsely detect a ringing condition. If the modem is configured to auto-answer, it might also attempt to answer the call. In some cases, this situation can prevent the modem from making an outgoing call (even if auto-answer is not configured). Navigate the following path from the Main screen to see this setting:

Telephony > Port specific parameters > MWI type

Not all modems detect the lamp Message Waiting Indication (MWI) as ringing, and those that do are typically not prevented from making outgoing calls altogether, although some attempts might fail.

The workaround for this problem is to disable the Lamp MWI for this port (ideally disable MWI altogether). If this is not possible or is impractical, then the problem might be cleared by retrieving the waiting message, then cancelling the MWI. Furthermore, you should disable auto-answer on modems connected to VG248 ports that have the Lamp MWI setting configured.

CSCuk27613

Fax machines connected to the VG248 might return to the on-hook condition immediately after answering an incoming call.

When the VG248 receives an incoming call, Caller Identification (CID) is sent along with the signal in order for the called device to ring. In some countries, CID information is sent between the first and second rings, while in other countries it is sent just before the first ring.

In cases where the CID information arrives before the first ring, some fax machines answer the call but immediately hang up.

To work around this problem, disable Caller Identification for VG248 ports to which a fax machine is connected. This is done in Cisco CallManager.

CSCuk27761

Message Waiting Indication (MWI) behavior might not be as expected after a configuration change.

The VG248 supports three methods of Message Waiting Indication (MWI):

• Lamp

• Caller ID

• stutter

For more information, refer to the "Choosing Message Waiting Indicator Type" section in the Software Configuration Guid e:

http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/soft_con/vg248swv.htm#xtocid2380613

Configuration options allow you to select any of these three methods as well as pairings of the methods or no MWI at all.

The display on the phone will not necessarily be updated to reflect configuration changes you make.

The MWI Caller ID (CID) option is also affected by whether incoming call Caller Identification is configured enabled or disabled for a port.

To work around these issues, clear all Caller Identification information before changing the MWI configuration for a given port. Then, manually check for waiting messages once the configuration is finalized.

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

http://www.cisco.com/cgi-bin/order/order_root.pl

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

### AccessPath, AtmDirector, Browse with Me, CCIP, CCSI, CD-PAC, CiscoLink , the Cisco Powered Network logo, Cisco Systems Networking Academy, the Cisco Systems Networking Academy logo, Fast Step, Follow Me Browsing, FormShare, FrameShare, GigaStack, IGX, Internet Quotient, IP/VC, iQ Breakthrough, iQ Expertise, iQ FastTrack, the iQ Logo, iQ Net Readiness Scorecard, MGX, the Networkers logo, Packet , RateMUX, ScriptBuilder, ScriptShare, SlideCast, SMARTnet, TransPath, Unity, Voice LAN, Wavelength Router, and WebViewer are trademarks of Cisco Systems, Inc.; Changing the Way We Work, Live, Play, and Learn, Discover All That's Possible, and Empowering the Internet Generation, are service marks of Cisco Systems, Inc.; and Aironet, ASIST, BPX, Catalyst, CCDA, CCDP, CCIE, CCNA, CCNP, Cisco, the Cisco Certified Internetwork Expert logo, Cisco IOS, the Cisco IOS logo, Cisco Press, Cisco Systems, Cisco Systems Capital, the Cisco Systems logo, Enterprise/Solver, EtherChannel, EtherSwitch, FastHub, FastSwitch, IOS, IP/TV, LightStream, MICA, Network Registrar, PIX, Post-Routing, Pre-Routing, Registrar, StrataView Plus, Stratm, SwitchProbe, TeleRouter, and VCO are registered trademarks of Cisco Systems, Inc. and/or its affiliates in the U.S. and certain other countries.

### All other trademarks mentioned in this document or Web site are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (0108R)

### Copyright © 2001, Cisco Systems, Inc. All rights reserved.

### This Document Applies to These Products

- VG Series Gateways

| Document Title | Description | Where to Find It |
|---|---|---|
| Cisco VG248 Analog Phone Gateway Hardware Installation Guide | Provides the site preparation, safety information, and hardware installation and setup instructions to safely install the VG248. | • In the box—A printed version of this document ships with the product • Online at Cisco.com—HTML and PDF versions of this document are available from Cisco.com: http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/hard_ins/index.htm • By ordering—See the "Ordering Documentation" section for details |
| Cisco VG248 Analog Phone Gateway Software Configuration Guide | Provides information about understanding, configuring, managing, and troubleshooting the VG248. | Online at Cisco.com—HTML and PDF versions of this document are available from Cisco.com: http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/soft_con/index.htm |
| Cisco VG248 Analog Phone Gateway Release Notes | Describes known caveats and any documentation errata for the VG248. | Online at Cisco.com—HTML and PDF versions of this document are available from Cisco.com: http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/rel_note/index.htm |

| Bug ID | Summary | Explanation |
|---|---|---|
| CSCdu44880 | Audio volume is reduced on extensions with a Ringer Equivalence Number (REN) of three. | The VG248 supports a maximum REN of three per port. This means that as many as three devices, each with a REN of one, can be connected as extensions to a single VG248 port. The VG248 allows a maximum of two devices to be off hook at any time. The VG248 will not be damaged if devices with a total REN greater than two are off hook at the same time on a single port, but users on these extensions might experience quieter audio than normal, and possibly no audio at all. To work around this problem, ensure that no more than two extensions on a single port are off hook at the same time. One way you can do this is by restricting the total REN of all extensions on a port to two. For more information, refer to the section "Connecting Too Many Phones to the VG248" in the Software Configuration Guide : http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/soft_con/vg248swt.htm#xtocid240276 |
| CSCdu54384 | VG248 loses audio during excess broadcast network traffic. | If the VG248 is attached to a network on which a large amount of broadcast traffic occurs, this traffic might have adverse effects on the operation of the VG248. These effects include reduced audio quality and, in extreme circumstances, loss of Cisco CallManager registration for some ports. If the latter situation arises, a large number of discarded packets are reported (both for receive and transmit) on the VG248 Network Statistics screen. To get to the Network Statistics screen from the Main screen, select Display > Network statistics . These situations would occur only if the broadcast traffic were to exceed several Megabits per second. This is far higher than the normal rate and likely would cause other network problems. The workaround is to identify the source of the broadcast data and prevent it from generating excessive amounts of network traffic. The VG248 will recover and recommence normal operation once the excessive broadcast condition ceases. |
| CSCdu57118 | FTP sessions to the VG248 will be disconnected after 10 minutes of inactivity. | When an FTP connection has been established to the VG248 (typically for the purposes of performing a software upgrade), and has been left idle for 10 minutes, the VG248 automatically disconnects that session. |
| CSCdu59990 | Successive VG248 ports are not guaranteed to obtain sequential directory numbers when registering with Cisco CallManager in auto-registration mode. | On start up, the VG248 attempts to register all its enabled ports with Cisco CallManager in numerical order. However, this numerical registration of directories is not guaranteed. One reason numerical registration might not be successful is that there might not be large enough contiguous blocks of directory numbers available. To work around this problem, manually create the ports in Cisco CallManager before enabling them on the VG248. You must know the device name that the VG248 will give to each port; this name is normally derived from the VG248 MAC address. You can then explicitly assign directory numbers to ports, thus following any desired pattern. For more information, refer to the chapter "Configuring Analog Phones Using Cisco CallManager" in the Software Configuration Guide : http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/soft_con/vg248swp.htm |
| CSCdu60375 | VG248 port status shows up as "Not Found" in Cisco CallManager. | The VG248 requires Cisco CallManager versions 3.1(1) or greater. However, Cisco CallManager versions prior to 3.1(2) do not contain support for the VG248 within the Real-time Information Service, which is used to collect information for display through the Cisco CallManager web interface. Therefore, the current status of VG248 port registrations is not available for Cisco CallManager versions prior to 3.1(2). This is solely a display problem; VG248 ports are able to register successfully with version 3.1(1). Their ability to perform all required telephony operations is not affected by the lack of support by the Real-time Information Service. To work around this issue, upgrade to Cisco CallManager 3.1(2) or greater. |
| CSCdu62479 | Loss of functionality due to insufficient network bandwidth. | Cisco recommends that you connect the VG248 to a switch or router port capable of full duplex operation. In addition, Cisco recommends that this port be capable of running at 100 Mbps. If there is insufficient network bandwidth available, reduced audio quality is likely to occur. Also, some ports might lose their Cisco CallManager registrations. The bandwidth requirement does not apply only to the connection between the VG248 and the Ethernet port to which the VG248 is attached. The same capacity is potentially required at each intermediate connection in the path to remote endpoints or gateways. For example, if the route to the rest of the VoIP network involves a 1.5-Mbps T1 link, this is likely to result in losses of functionality on all but the most lightly loaded VG248. |
| CSCdu79519 | Voltage might be too low for Message Waiting Indication (MWI) lamps on some phones. | Some older phones that use MWI lamps might not light up, even if the VG248 port is configured to indicate Message Waiting with the Lamp setting. To check this setting, go to the following path from the Main screen: Telephony > Port specific parameters > MWI type This problem arises because MWI lamps require a line voltage greater than the maximum voltage that the VG248 can supply. If you suspect that your lamp MWI should be lit, check the configuration of the port and the status of the messages in your mailbox. If the configuration is correct and you have a waiting message, you should try replacing the phone with one of a similar type to confirm that your phone is not faulty. If the lamp still does not light, you probably have a phone that cannot have its MWI lamp lit by the VG248. Other phone functionality is not impaired by the lamp deficiency. The only workaround to this problem is to consider replacing your phone. Test the new phone before committing to a large purchase. |
| CSCdu84588 | Interrupted FTP put operation might leave a partial file present on the VG248 filing system. | If you are using an FTP put operation to write a file to the VG248 internal filing system, and the operation is interrupted, a portion of the file might remain on the VG248 system. In such a scenario, if the partial file is a software build-image file, the VG248 will probably fail when restarted. To work around this problem, always check the size of the file after the transfer to make sure it is the same size as the original file. If it is not the same size, re-attempt the file transfer. For more information, refer to the "Resolving an Incomplete Upgrade" section in the Software Configuration Guide : http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/soft_con/vg248swt.htm#xtocid2402715 |
| CSCdv36727 | Silence suppression is always reported as off . | When a call is in progress, the VG248 per-port status screen displays the codec in use and indicates whether silence suppression is active. Silence suppression, which is configurable in Cisco CallManager, means that no media packets will be transmitted if these packets would contain silence. Transmission would resume once the user commences speaking. The VG248 does not support the silence-suppression feature; therefore this setting will always be off . However, the VG248 can communicate with parties performing silence suppression, so you can allow this feature to remain enabled in Cisco CallManager. |
| CSCdv37478 | Unable to achieve modem connection speeds greater than 33.6 kbps per second. | Running a modem connection through a VG248 port involves complex conversions between the VG248 and the far end-modem. Therefore, normal modem speeds might range from 28.8 to 33.6 kbps. Some modems might run at speeds slower than 28.8 kbps per second. For best performance, Cisco recommends that ports intended for use with modems are configured with Cisco CallManager to use only G.711 media. |
| CSCuk25852 | FTP directory listing on VG248 does not show correct date information. | When you issue a directory listing command in an FTP session, the date stamp for each file is shown as "Jan 1, 1900." This is because the VG248 filing system does not store a date or time for its files. However, because some FTP client programs normally show such information in directory listings, the VG248 displays a fixed date value for those clients for compatibility reasons. |
| CSCuk27560 | Message Waiting Indication might cause some modems connected to VG248 to erroneously detect ringing. | If a VG248 port is configured to indicate Message Waiting with the Lamp setting configured, and there is a message waiting, then a modem connected to this port might falsely detect a ringing condition. If the modem is configured to auto-answer, it might also attempt to answer the call. In some cases, this situation can prevent the modem from making an outgoing call (even if auto-answer is not configured). Navigate the following path from the Main screen to see this setting: Telephony > Port specific parameters > MWI type Not all modems detect the lamp Message Waiting Indication (MWI) as ringing, and those that do are typically not prevented from making outgoing calls altogether, although some attempts might fail. The workaround for this problem is to disable the Lamp MWI for this port (ideally disable MWI altogether). If this is not possible or is impractical, then the problem might be cleared by retrieving the waiting message, then cancelling the MWI. Furthermore, you should disable auto-answer on modems connected to VG248 ports that have the Lamp MWI setting configured. |
| CSCuk27613 | Fax machines connected to the VG248 might return to the on-hook condition immediately after answering an incoming call. | When the VG248 receives an incoming call, Caller Identification (CID) is sent along with the signal in order for the called device to ring. In some countries, CID information is sent between the first and second rings, while in other countries it is sent just before the first ring. In cases where the CID information arrives before the first ring, some fax machines answer the call but immediately hang up. To work around this problem, disable Caller Identification for VG248 ports to which a fax machine is connected. This is done in Cisco CallManager. |
| CSCuk27761 | Message Waiting Indication (MWI) behavior might not be as expected after a configuration change. | The VG248 supports three methods of Message Waiting Indication (MWI): • Lamp • Caller ID • stutter For more information, refer to the "Choosing Message Waiting Indicator Type" section in the Software Configuration Guid e: http://www.cisco.com/univercd/cc/td/doc/product/voice/c_access/apg/vg248/v1_0/soft_con/vg248swv.htm#xtocid2380613 Configuration options allow you to select any of these three methods as well as pairings of the methods or no MWI at all. The display on the phone will not necessarily be updated to reflect configuration changes you make. The MWI Caller ID (CID) option is also affected by whether incoming call Caller Identification is configured enabled or disabled for a port. To work around these issues, clear all Caller Identification information before changing the MWI configuration for a given port. Then, manually check for waiting messages once the configuration is finalized. |