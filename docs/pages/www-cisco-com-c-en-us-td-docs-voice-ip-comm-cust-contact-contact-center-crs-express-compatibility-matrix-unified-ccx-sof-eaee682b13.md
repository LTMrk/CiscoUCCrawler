---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-compatibility-matrix-unified-ccx-sof-eaee682b13
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_compatibility/matrix/Unified_CCX_Software_Compatibility_Matrix_for_1251_SU2.html
retrieved_at: 2026-08-16T15:02:54.593202+00:00
---

Unified CCX Software Compatibility Matrix for 12.5(1) SU2

# Unified CCX Software Compatibility Matrix for 12.5(1) SU2

- SU2

- SU1

- 12.5(1)

### Download Options

Updated: August 14, 2023

Unified CCX Software Compatibility Matrix for 12.5(1) SU2

First Published: 2023-05-08

Last Updated: 2026-01-13

Americas Headquarters

Cisco Systems, Inc.

170 West Tasman Drive

San Jose, CA 95134-1706 USA

http://www.cisco.com Tel: 408 526-4000

800 553-NETS (6387) Fax: 408 527-0883

Contents

Unified CCX and IP IVR . 4

Solution Products and Components . 4

Webex Workforce Optimization Compatibility . 6

Cisco Workforce Optimization Compatibility . 6

Hardware and Virtualization . 7

Third-party Software . 7

ASR and TTS . 7

Export Unified Intelligence Center Reporting . 8

Wallboard Reporting . 8

Enterprise Database . 8

Enterprise Database for Unified Intelligence Center . 9

Microsoft Exchange Server for Email 9

Cloud Based Email Services . 9

Supported Single Sign-On Identity Providers . 9

Supported Browsers . 10

Transport Layer Security . 11

Client Operating System .. 11

Desktop Virtualization . 11

Application Virtualization . 12

Endpoint Devices . 12

Jabber: 14

Cisco Expressway . 14

Platform .. 14

Supported Languages . 15

Legal Information . 19

Cisco Trademark (all documentation) . 20

Cisco Copyright (all documentation) . 20

## Unified CCX and IP IVR

Unified CCX and Unified IP IVR

Supported Unified UCCX and Unified IP IVR Upgrade Paths (FN1,2)

Standalone Unified Intelligence Center

APIs

■ 12.5(1) SU2

■ UCSInstall_UCCX_12_5_1_UCOS_12.5.1.11002-481.sgn.iso

■ 11.6.2

■ 12.0(1)

■ 12.5(1)

■ 12.5(1) and above

CTI Server -

Versions 13 to 18

For Unified CCX configuration APIs and Finesse APIs, see the Cisco Unified Contact Center Express Developer Guide, located at: https://developer.cisco.com/site/contact-center-express/ .

(FN1) The upgrade is also supported from any of the Engineering Specials and Service Update (SU) versions of all the mentioned Unified CCX versions.

(FN 2) Unified CCX includes the co-resident Unified Intelligence Center and Finesse.

## Solution Products and Components

Cisco Unified

Communications Manager (Unified CM)

and Business Edition

6000 and 7000 (FN 1)

G ateways for Outbound Agent and IVR (FN 2,4)

Customer Collaboration Platform (CCP) (FN6)

Cisco Prime Collaboration

Cisco Instant Messaging and Presence (IM&P) (FN5)

Cisco Smart Software Manager On-Prem(Cisco SSM On-Prem) (FN 10)

11.x (FN 7)

1 2.x (FN 8)

1 4

Prime Deployment

Prime Assurance

11.5(1)

12.0(1)

12.5(1)

14 and latest

Router Series

■ 29XX

■ 39XX

■ 43XX

■ 44XX

Cisco IOS (FN 3)

■ 15.5(3)M

■ 15.5(3)S (FN 4)

■ 15.6(3)M

■ 15.7(3)M

■ 16.6

■ 16.9

■ 16.12

12.5(1) SU2

12.6(1)

11.6(1)

■ 12.5(1)

■ 14

8-202112 (FN 9 )

■ (FN 1) For the Unified CM version that is supported, all the corresponding Service Update (SU) and Engineering Special (ES) releases are also supported.

■ (FN 2) Outbound Agent (Predictive and Progressive) and Outbound IVR are supported only on IOS versions that incorporate Call Progress Analysis. For information on Call Progress Analysis, see http://www.cisco.com/en/US/tech/tk652/tk701/tech_tech_notes_list.html .

■ (FN 3) CUBE is supported with the SIP Outbound Dialer and CPA; supported versions of CUBE are ISR Pi27 15.5(2), Pi28 15.5(3), Pi29 15.6(3), and Pi32 15.7(3).

■ (FN 4) Unified CCX Agent and IVR Outbound supports E1 R2 signaling on ISR Gateway 4451 with IOS version 15.5(3)S and later.

■ (FN 5) Desktop chat requires IM&P 12.5(1) and Unified CM 12.5(1) or higher.

■ (FN 6) SocialMiner has been renamed as Customer Collaboration Platform (CCP).

■ (FN 7) Minimum requirement is 11.5(SU4).

■ (FN 8) In Unified CCX, to enable SRTP in FIPS 140-2 mode, minimum requirement is Unified CM 12.5(1).

■ (FN 9) For more information about CSSM version 8, see the Cisco Smart Software Manager On-Prem Release .

■ (FN 10) Transport Gateway is not supported in Unified CCX.

## Webex Workforce Optimization Compatibility

Unified CCX

Cisco Unified Communications Manager

Cisco IP Communicator

Cisco Jabber

IP Phones

Webex WFO

■ 11.6(2)

■ 12.0(1)

■ 12.5(1)

■ 11.6(1)

■ 12.0(1)

■ 12.5(1)

Y es

Y es

Yes

## Cisco Workforce Optimization Compatibility

Note: Cisco Workforce Optimization is End-of-Life as on August 1, 2020. For more information, refer to Cisco Unified Contact Center Express - End-of-Sale and End-of-Life Announcement for Cisco Unified Workforce Optimization - Cisco .

Note: Cisco Workforce Optimization licenses are not supported with Smart Licensing. Consequently, customers who upgrade to 12.5 must continue with Classic Licensing if they want to continue using Cisco WFO.

Alternatively, customers who want to move to Smart Licensing for Unified CCX must consider migrating to Webex WFO or SolutionsPlus version of Workforce Optimization if they want to stay with On-prem.

Unified CCX

Cisco Unified Communications Manager

Compliance Recording/Advanced Quality Management (FN1,2)

Workforce Management (WFM) (FN 3)

■ 12.0(1)

■ 12.5(1)

■ 11.5(1)

■ 12.0(1)

■ 12.5(1)

■ 11.5(1)

■ 11.5(1)

■ (FN 1) Compliance Recording/Advanced Quality Management (CR/AQM) are 32-bit applications.

— Support for the application client operation on Windows 7 64-bit machines is through WoW64 emulator mode.

— Desktop-based monitoring and recording is not supported in WoW64 mode.

■ (FN 2) Cisco AQM has direct dependencies upon Cisco Unified Communications Manager for CTI and SIP events. Therefore, AQM compatibility with Unified CM is limited to the current Unified CM version at the time of release and at least one prior version. Previous versions of AQM are not generally updated for compatibility with new versions of Unified CM. Therefore, when you plan an upgrade, consult the appropriate AQM Installation Guide for Unified CM compatibility. See footnote on individual AQM versions to identify the Unified Communications Manager versions that are supported by that AQM.

■ (FN 3) All associated Service Updates are supported with compatible versions of WFM.

## Hardware and Virtualization

■ For information about UC Virtualization Supported Hardware, see http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-hardware.html .

■ For information about Unified Communications in a Virtualized Environment, see http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html .

■ For information about Virtualization for Cisco Unified Contact Center Express, see http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-contact-center-express.html .

■ For information about Virtualization for Customer Collaboration Platform, see http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-contact-center-express.html .

■ For information about Virtualization for Cisco Unified Intelligence Center, see http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-intelligence-center.html .

## Third-party Software

### ASR and TTS

MRCP

VXML

Speech Servers

Nuance

1.0

2.0 (FN 1)

2.0

Nuance Speech Server 7.x

Recognizer 11.x

Vocalizer 20.x (FN 2)

Krypton 4.x (Dragon Voice engine)

Nuance License Manager 11.x

Nuance Management Station 6.x

■ Latest version of the ASR-TTS packages recommended by Nuance can be used. See http://network.nuance.com/portal/server.pt . Using the latest Nuance packages will not impact the integration functionality between Unified CCX and Nuance until there is any major change by Nuance in the underlying design. However, customers must maintain the compatibility among different ASR-TTS packages as suggested by Nuance.

■ (FN 1) MRCP V2.0 is supported from Unified CCX Release 12.5(1).

■ (FN 2) This is a new versioning scheme. Nuance Enterprise Version 20.x is the continuation of Nuance Enterprise version 7.x.

### Export Unified Intelligence Center Reporting

For exporting reports

■ Microsoft Excel 2007

■ Microsoft Excel 2010

■ Microsoft Excel 2013

■ Microsoft Excel 2016

■ Microsoft 365

Note: Office 365 does not support authenticated Excel report permalink.

### Wallboard Reporting

Unified CCX supports wallboard reporting. Obtain the wallboard from a Cisco-approved vendor from Cisco Marketplace: https://marketplace.cisco.com/ .

### Enterprise Database

■ Oracle 11g R2

■ Oracle 12c R1

■ Oracle 19c (FN 1)

■ Oracle 21c

■ Sybase Adaptive Server 12

■ IBM DB2 8.2, 10.5

■ MS SQL Server 2012

■ MS SQL Server 2014

■ MS SQL Server 2016

Note:

— (FN 1) Unified CCX does not support any views created on Oracle 19c.

— Unified CCX connection to external databases has been qualified only for non-encrypted connections and hence is not supported with encryption.

### Enterprise Database for Unified Intelligence Center

■ MS SQL Server 2012

■ MS SQL Server 2014

■ Informix Database Server 12.10.UC5W1X7(UC7X3)

### Microsoft Exchange Server for Email

■ Microsoft Exchange Server 2013 (FN 1) - Enterprise and Standard Edition

■ Microsoft Exchange Server 2016 - Enterprise and Standard Edition

■ Microsoft Exchange Server 2019 - Enterprise and Standard Edition

Not e: (FN 1) Download and install the latest cumulative update (Cumulative Update 15 for Microsoft Exchange Server 2013 (KB3197044) or higher) to support TLS version 1.2.

### Cloud Based Email Services

■ Office 365

■ Gmail

### Supported Single Sign-On Identity Providers

Cisco Identity Service supports the Identity Providers (IdPs) listed below and any other IdPs that comply to generic SAML 2.0 authentication as per the considerations described in the Unified CCX Solution Design Guide located at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-implementation-design-guides-list.html .

Microsoft ADFS (Active Directory Federation Services)

2.0, 2.1, 3.0, and 4.0

PingFederate

8.2.2.0

OpenAM

10.0.1

Shibboleth

3.3.0

F5

13.0

## Supported Browsers

Firefox 91

Extended Support Release (ESR) and higher ESR

Chrome 83 and higher

Microsoft Edge (Edge Chromium)

88.0.4324 and higher

Unified CCX Administration

Y

Y

Y

Cisco Finesse (FN 1)

Y

Y

Y

Cisco Unified Intelligence Center

Y

Y

Y

Cisco Unified Intelligence Center (Live Data Gadgets)

Y

Y

Y

CCP Administration

Y

Y

Y

Cisco Identity Service Administration

Y

Y

Y

Cisco Webex Experience Management

Refer to Experience Management to know the browsers that are supported.

Note: (FN 1) The supported resolution for the Finesse desktop is 1366 x 768 or higher.

## Transport Layer Security

Transport Layer Security (TLS) 1.2 is supported for both incoming and outgoing connections.

## Client Operating System

Windows 10

Chromebook

Linux

MacOS

Android

Apple iOS with Safari browser

Finesse

Y

Y

N

Y

10.12, 10.13, 10.14, 10.15.x

N

N

Cisco Unified CCX Editor Installer for Windows (FN 1)

Y

N

N

N

N

N

Cisco Unified CCX Editor Web Launcher

Y

Y

Y

Y

N

N

(FN 1) The Windows User launching the Cisco Unified CCX Editor must be a part of the Windows Administrator Group.

Note:

1. For information on Jabber Client Operating System, refer to the specific versions of Jabber Release Notes .

2. Real Time Monitoring Tool is not supported on Windows 2012 server. The supported operating systems are listed below:

a. Windows 10

b. Linux with KDE or GNOME client

## Desktop Virtualization

Unified CCX allows Cisco Finesse to run on third-party Virtual Desktop Infrastructure (VDI). Customers need to ensure that their third-party VDI infrastructure is supported by the Cisco soft phones that are used on the agent and supervisor VDI-based desktops.

The Cisco Unified Intelligence Center and Cisco Unified Contact Center Express Administration are not supported on virtual desktops.

## Application Virtualization

■ Cisco Finesse

■ Citrix XenApp 7.x

## Endpoint Devices

Cisco Unified IP Phones for Cisco Finesse IP Phone Agent (FN 3,6)

End Points for Cisco Finesse (FN 1,2)

Cisco IP Phone 7811 (FN5)

Cisco IP Phone 7811

Cisco IP Phone 7821 (FN5)

Cisco IP Phone 7821

Cisco IP Phone 7841 (FN5)

Cisco IP Phone 7841

Cisco IP Phone 7861 (FN5)

Cisco IP Phone 7861

Cisco IP Phone 8811

Cisco IP Phone 7945G

Cisco IP Phone 8821

Cisco IP Phone 7975G

Cisco IP Phone 8841

Cisco IP Phone 8811

Cisco IP Phone 8845

Cisco IP Phone 8821

Cisco IP Phone 8851

Cisco IP Phone 8841

Cisco IP Phone 8861

Cisco IP Phone 8845

Cisco IP Phone 8865

Cisco IP Phone 8851

Cisco IP Phone 8861

Cisco IP Phone 8865

Cisco IP Phone 8961

Cisco IP Phone 9951

Cisco IP Phone 9971

Cisco IP Communicator (FN 9)

Jabber for Windows, Mac, and VDI (FN7)

Webex (FN8)

Cisco Webex DX80 (FN4)

■ (FN 1) All Cisco Finesse phones support BiB.

■ (FN 2) Cisco Finesse supports with caveats mentioned in Cisco Finesse section of the Release Notes for Unified Contact Center Express Solution, located at: http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-release-notes-list.html .

Note: The Cisco Mobile Supervisor application is withdrawn from the Cisco App Store. Cisco does not provide support for Cisco Mobile Supervisor deployments.

■ (FN 3) All the Cisco IP Phones for Cisco Finesse IP Phone Agent currently do not support the Simplified New Call UI.

■ (FN 4) Telepresence CE software does not support Transfer or Conference operations from Finesse.

■ (FN 5) If Cisco Finesse IPPA agents use 78xx series phone, you must either disable the Cisco Finesse IPPA Inactivity Timeout feature or increase the timeout to be within the range of 120 seconds to one day (86400seconds), so that the agent does not get logged out of Cisco Finesse IPPA even if the agent is on any other screen.

■ (FN 6) Cisco Finesse IP Phone Agent is not supported over Mobile and Remote Access (MRA).

■ (FN 7) Unified CCX is compatible with those Jabber versions that are compatible with the CUCM version being used with Unified CCX. The minimum supported Cisco Jabber version is 12.5.

■ (FN 8) For minimum supported versions of CUCM and Expressway (for MRA deployments) to support Webex, see the Supported Unified CM Releases and the Supported Expressway Releases tables at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/wbxt/ucmcalling/unified-cm-wbx-teams-deployment-guide/unified-cm-wbx-teams-deployment-guide_chapter_011.html .

■ (FN 9) For supported Cisco IP Communicator (SCCP) versions, see Cisco Unified Communications Manager Software Compatibility Matrix, available at: http://www.cisco.com/en/US/products/sw/voicesw/ps556/products_device_support_tables_list.html .

### Jabber:

■ MRA support for Jabber requires minimum Cisco Jabber version 12.5 and Expressway 12.5. If you have VPN split-tunneling configured, you can use Jabber with MRA and the Finesse desktop on the same client machine. See https://www.cisco.com/c/en/us/support/security/anyconnect-secure-mobility-client/products-installation-and-configuration-guides-list.html for Cisco AnyConnect Mobility Client split-tunneling configuration.

■ If VPN split-tunneling is not available, you can run Jabber with MRA and the Finesse desktop after splitting them onto two clients.

— A remote agent who runs Jabber with MRA on one client machine and the Finesse desktop with a VPN connection on a second client machine.

— A remote agent who runs a Jabber softphone on a laptop that is connected over MRA and runs the Finesse desktop as a Xenapp thin client.

■ Jabber for VDI is not supported in Video Contact Center deployments.

■ For Cisco Jabber software compatibility details, see the Planning guide for Cisco Jabber at https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

■ For Home Agent with Extend and Connect, set Jabber to Extend Mode so that the agents can select or edit the remote destination number.

### Cisco Expressway

Cisco Expressway

X12.5.6 and later (FN 1)

(FN 1) For any caveats related to recording with Jabber, refer to the Mobile and Remote Access Through Cisco Expressway Deployment Guide. See https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-installation-and-configuration-guides-list.html .

## Platform

UCOS Platform Version

Internal Unified CCX Database (IDS)

Transport Layer Security (TLS)

Tomcat

Open SSL

Cent OS

Java versions

Servers

CCM_FREEZE_12_5_1_14900_63_BT5089_GIT

Informix IDS12.10.UC9W1X3

1.2

Tomcat 9.0.37

1.0.2u.6.2.374

7.4.1708

OpenJDK 1.8.0_26

■ Custom Classes/SDK

■ Real-Time Reporting

## Supported Languages

ASR Grammar for Workflow Steps

IP Phone Agent Supported Languages

Unified Intelligence Center (FN 3)

Unified CCX Administration

Finesse

IVR Prompts

CCP

TTS

VXML Grammar

Workforce Management

Quality Management

Arabic

No

No

No

No

No

Yes

No

Dependent on software provided by the TTS vendor

Dependent on software provided by the MRCP vendor

No

No

Canadian French

Yes

No

No

No

No

Yes

Yes

No

No

Cantonese

No

No

No

No

No

No

No

No

No

Cantonese Hong Kong

No

No

No

No

No

Yes

No

No

No

Chinese

No

No

No

No

No

No

No

No

No

Czech

No

No

Yes

No

Yes

Yes

No

No

No

Danish

No

Yes

Yes

No

Yes

Yes

Yes

Yes

Yes

Dutch

No

Yes

Yes

No

Yes

Yes

Yes

Yes

Yes

English

Yes

(GB, US)

Yes

Yes

(US)

Yes

Yes

Yes

(AU, CA, GB, US)

Yes

Yes

Yes

Finnish

No

Yes

Yes

No

Yes

Yes

No

No

No

French

Yes

Yes

Yes

No

Yes

Yes

Yes

Yes

Yes

German

Yes

Yes

Yes

No

Yes

Yes

Yes

Yes

Yes

Hebrew

No

No

No

No

No

Yes (IL)

No

No

No

Hungarian

No

No

Yes

No

Yes

Yes

No

No

No

Italian

Yes

Yes

Yes

No

Yes

Yes

Yes

Yes

Yes

Japanese

Yes

Yes

Yes

No

Yes

Yes

Yes (FN 1)

No

Yes

Korean

No

Yes

Yes

No

Yes

Yes

Yes (FN 1)

No

Yes

Malay

No

No

No

No

No

Yes

No

No

No

Chinese Mandarin

No

No

No

No

No

Yes, and also Mandarin (Taiwan)

Yes (FN 1) and in Taiwan (FN 1)

No

No

Norwegian

No

Yes

Yes

No

Yes

Yes

Yes

No

No

Polish

No

Yes

Yes

No

Yes

Yes

Yes

No

No

Portuguese

No

Yes

Yes, and Portuguese (Brazil)

No

Yes

Yes (Brazilian)

Yes (Brazilian)

Yes (Brazilian)

Yes (Brazilian)

Russian

No

Yes

Yes

No

Yes

Yes

Yes

No

Yes

Simplified Chinese

No

Yes

Yes

No

Yes

No

No

No

Yes

Spanish

Yes (CO, EX, MX)

Yes

Yes

No

Yes

Yes (CO, ES, MX, US)

Yes

Yes

Yes

Swedish

No

Yes

Yes

No

Yes

Yes

Yes

Yes

Yes

Thai

No

No

No

No

No

Yes

No

No

No

Traditional Chinese

No

Yes

Yes

No

Yes

No

No

No

Yes

Turkish

No

Yes

Yes

No

Yes

Yes

Yes

No

No

Serbian

No

No

Yes

No

Yes

No

No

No

No

Croatian

No

No

Yes

No

Yes

No

No

No

No

Bulgarian

No

No

Yes

No

Yes

No

No

No

No

Romanian

No

No

Yes

No

Yes

No

No

No

No

Slovenian

No

No

Yes

No

Yes

No

No

No

No

Slovakian

No

No

Yes

No

Yes

No

No

No

No

Catalan

No

No

Yes

No

Yes

No

No

No

No

(FN 1) Finesse IPPA supports all languages currently supported by Finesse if the phones support UTF.

(FN 2) Cisco Unified Intelligence Center uses the browser locale to display the Date & Time format in the filter page. If Unified Intelligence Center does not support the browser locale language, then the locale selected in the Unified Intelligence Center application is used.

Note: For the languages that are supported by Cisco Webex Experience Management, click Experience Management .

## Legal Information

THE SPECIFICATIONS AND INFORMATION REGARDING THE PRODUCTS IN THIS MANUAL ARE SUBJECT TO CHANGE WITHOUT NOTICE. ALL STATEMENTS, INFORMATION, AND RECOMMENDATIONS IN THIS MANUAL ARE BELIEVED TO BE ACCURATE BUT ARE PRESENTED WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. USERS MUST TAKE FULL RESPONSIBILITY FOR THEIR APPLICATION OF ANY PRODUCTS.

THE SOFTWARE LICENSE AND LIMITED WARRANTY FOR THE ACCOMPANYING PRODUCT ARE SET FORTH IN THE INFORMATION PACKET THAT SHIPPED WITH THE PRODUCT AND ARE INCORPORATED HEREIN BY THIS REFERENCE. IF YOU ARE UNABLE TO LOCATE THE SOFTWARE LICENSE OR LIMITED WARRANTY, CONTACT YOUR CISCO REPRESENTATIVE FOR A COPY.

The Cisco implementation of TCP header compression is an adaptation of a program developed by the University of California, Berkeley (UCB) as part of UCB’s public domain version of the UNIX operating system. All rights reserved. Copyright © 1981, Regents of the University of California.

NOTWITHSTANDING ANY OTHER WARRANTY HEREIN, ALL DOCUMENT FILES AND SOFTWARE OF THESE SUPPLIERS ARE PROVIDED “AS IS” WITH ALL FAULTS. CISCO AND THE ABOVE-NAMED SUPPLIERS DISCLAIM ALL WARRANTIES, EXPRESSED OR IMPLIED, INCLUDING, WITHOUT LIMITATION, THOSE OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OR ARISING FROM A COURSE OF DEALING, USAGE, OR TRADE PRACTICE.

IN NO EVENT SHALL CISCO OR ITS SUPPLIERS BE LIABLE FOR ANY INDIRECT, SPECIAL, CONSEQUENTIAL, OR INCIDENTAL DAMAGES, INCLUDING, WITHOUT LIMITATION, LOST PROFITS OR LOSS OR DAMAGE TO DATA ARISING OUT OF THE USE OR INABILITY TO USE THIS MANUAL, EVEN IF CISCO OR ITS SUPPLIERS HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

Any Internet Protocol (IP) addresses and phone numbers used in this document are not intended to be actual addresses and phone numbers. Any examples, command display output, network topology diagrams, and other figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses or phone numbers in illustrative content is unintentional and coincidental.

All printed copies and duplicate soft copies are considered un-Controlled copies and the original on-line version should be referred to for latest version.

Cisco has more than 200 offices worldwide. Addresses, phone numbers, and fax numbers are listed on the Cisco website at www.cisco.com/go/offices .

## Cisco Trademark (all documentation)

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company.

## Cisco Copyright (all documentation)

© 2023 Cisco Systems, Inc. All rights reserved.

| Unified CCX and Unified IP IVR | Supported Unified UCCX and Unified IP IVR Upgrade Paths (FN1,2) | Standalone Unified Intelligence Center | APIs |
|---|---|---|---|
| ■ 12.5(1) SU2 ■ UCSInstall_UCCX_12_5_1_UCOS_12.5.1.11002-481.sgn.iso | ■ 11.6.2 ■ 12.0(1) ■ 12.5(1) | ■ 12.5(1) and above | CTI Server - Versions 13 to 18 For Unified CCX configuration APIs and Finesse APIs, see the Cisco Unified Contact Center Express Developer Guide, located at: https://developer.cisco.com/site/contact-center-express/ . |

| Cisco Unified Communications Manager (Unified CM) and Business Edition 6000 and 7000 (FN 1) | G ateways for Outbound Agent and IVR (FN 2,4) | Customer Collaboration Platform (CCP) (FN6) | Cisco Prime Collaboration | Cisco Instant Messaging and Presence (IM&P) (FN5) | Cisco Smart Software Manager On-Prem(Cisco SSM On-Prem) (FN 10) |
|---|---|---|---|---|---|
| 11.x (FN 7) | 1 2.x (FN 8) | 1 4 | Prime Deployment | Prime Assurance |
| 11.5(1) | 12.0(1) 12.5(1) | 14 and latest | Router Series ■ 29XX ■ 39XX ■ 43XX ■ 44XX Cisco IOS (FN 3) ■ 15.5(3)M ■ 15.5(3)S (FN 4) ■ 15.6(3)M ■ 15.7(3)M ■ 16.6 ■ 16.9 ■ 16.12 | 12.5(1) SU2 | 12.6(1) | 11.6(1) | ■ 12.5(1) ■ 14 | 8-202112 (FN 9 ) |

|  | Unified CCX | Cisco Unified Communications Manager | Cisco IP Communicator | Cisco Jabber | IP Phones |
|---|---|---|---|---|---|
| Webex WFO | ■ 11.6(2) ■ 12.0(1) ■ 12.5(1) | ■ 11.6(1) ■ 12.0(1) ■ 12.5(1) | Y es | Y es | Yes |

| Unified CCX | Cisco Unified Communications Manager | Compliance Recording/Advanced Quality Management (FN1,2) | Workforce Management (WFM) (FN 3) |
|---|---|---|---|
| ■ 12.0(1) ■ 12.5(1) | ■ 11.5(1) ■ 12.0(1) ■ 12.5(1) | ■ 11.5(1) | ■ 11.5(1) |

| MRCP | VXML | Speech Servers |
|---|---|---|
| Nuance |
| 1.0 2.0 (FN 1) | 2.0 | Nuance Speech Server 7.x Recognizer 11.x Vocalizer 20.x (FN 2) Krypton 4.x (Dragon Voice engine) Nuance License Manager 11.x Nuance Management Station 6.x |

| For exporting reports | ■ Microsoft Excel 2007 ■ Microsoft Excel 2010 ■ Microsoft Excel 2013 ■ Microsoft Excel 2016 ■ Microsoft 365 |
|---|---|

| Microsoft ADFS (Active Directory Federation Services) | 2.0, 2.1, 3.0, and 4.0 |
|---|---|
| PingFederate | 8.2.2.0 |
| OpenAM | 10.0.1 |
| Shibboleth | 3.3.0 |
| F5 | 13.0 |

|  | Firefox 91 Extended Support Release (ESR) and higher ESR | Chrome 83 and higher | Microsoft Edge (Edge Chromium) 88.0.4324 and higher |
|---|---|---|---|
| Unified CCX Administration | Y | Y | Y |
| Cisco Finesse (FN 1) | Y | Y | Y |
| Cisco Unified Intelligence Center | Y | Y | Y |
| Cisco Unified Intelligence Center (Live Data Gadgets) | Y | Y | Y |
| CCP Administration | Y | Y | Y |
| Cisco Identity Service Administration | Y | Y | Y |
| Cisco Webex Experience Management | Refer to Experience Management to know the browsers that are supported. |

|  | Windows 10 | Chromebook | Linux | MacOS | Android | Apple iOS with Safari browser |
|---|---|---|---|---|---|---|
| Finesse | Y | Y | N | Y 10.12, 10.13, 10.14, 10.15.x | N | N |
| Cisco Unified CCX Editor Installer for Windows (FN 1) | Y | N | N | N | N | N |
| Cisco Unified CCX Editor Web Launcher | Y | Y | Y | Y | N | N |

| Cisco Unified IP Phones for Cisco Finesse IP Phone Agent (FN 3,6) | End Points for Cisco Finesse (FN 1,2) |
|---|---|
| Cisco IP Phone 7811 (FN5) | Cisco IP Phone 7811 |
| Cisco IP Phone 7821 (FN5) | Cisco IP Phone 7821 |
| Cisco IP Phone 7841 (FN5) | Cisco IP Phone 7841 |
| Cisco IP Phone 7861 (FN5) | Cisco IP Phone 7861 |
| Cisco IP Phone 8811 | Cisco IP Phone 7945G |
| Cisco IP Phone 8821 | Cisco IP Phone 7975G |
| Cisco IP Phone 8841 | Cisco IP Phone 8811 |
| Cisco IP Phone 8845 | Cisco IP Phone 8821 |
| Cisco IP Phone 8851 | Cisco IP Phone 8841 |
| Cisco IP Phone 8861 | Cisco IP Phone 8845 |
| Cisco IP Phone 8865 | Cisco IP Phone 8851 |
|  | Cisco IP Phone 8861 |
|  | Cisco IP Phone 8865 |
|  | Cisco IP Phone 8961 |
|  | Cisco IP Phone 9951 |
|  | Cisco IP Phone 9971 |
|  | Cisco IP Communicator (FN 9) |
|  | Jabber for Windows, Mac, and VDI (FN7) |
|  | Webex (FN8) |
|  | Cisco Webex DX80 (FN4) |

| Cisco Expressway | X12.5.6 and later (FN 1) |
|---|---|

| UCOS Platform Version | Internal Unified CCX Database (IDS) | Transport Layer Security (TLS) | Tomcat | Open SSL | Cent OS | Java versions |
|---|---|---|---|---|---|---|
| Servers |
| CCM_FREEZE_12_5_1_14900_63_BT5089_GIT | Informix IDS12.10.UC9W1X3 | 1.2 | Tomcat 9.0.37 | 1.0.2u.6.2.374 | 7.4.1708 | OpenJDK 1.8.0_26 ■ Custom Classes/SDK ■ Real-Time Reporting |

|  | ASR Grammar for Workflow Steps | IP Phone Agent Supported Languages | Unified Intelligence Center (FN 3) | Unified CCX Administration | Finesse | IVR Prompts | CCP | TTS | VXML Grammar | Workforce Management | Quality Management |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Arabic | No | No | No | No | No | Yes | No | Dependent on software provided by the TTS vendor | Dependent on software provided by the MRCP vendor | No | No |
| Canadian French | Yes | No | No | No | No | Yes | Yes | No | No |
| Cantonese | No | No | No | No | No | No | No | No | No |
| Cantonese Hong Kong | No | No | No | No | No | Yes | No | No | No |
| Chinese | No | No | No | No | No | No | No | No | No |
| Czech | No | No | Yes | No | Yes | Yes | No |  | No | No |
| Danish | No | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes |
| Dutch | No | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes |
| English | Yes (GB, US) | Yes | Yes (US) | Yes | Yes | Yes (AU, CA, GB, US) | Yes | Yes | Yes |
| Finnish | No | Yes | Yes | No | Yes | Yes | No | No | No |
| French | Yes | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes |
| German | Yes | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes |
| Hebrew | No | No | No | No | No | Yes (IL) | No | No | No |
| Hungarian | No | No | Yes | No | Yes | Yes | No | No | No |
| Italian | Yes | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes |
| Japanese | Yes | Yes | Yes | No | Yes | Yes | Yes (FN 1) | No | Yes |
| Korean | No | Yes | Yes | No | Yes | Yes | Yes (FN 1) | No | Yes |
| Malay | No | No | No | No | No | Yes | No | No | No |
| Chinese Mandarin | No | No | No | No | No | Yes, and also Mandarin (Taiwan) | Yes (FN 1) and in Taiwan (FN 1) | No | No |
| Norwegian | No | Yes | Yes | No | Yes | Yes | Yes | No | No |
| Polish | No | Yes | Yes | No | Yes | Yes | Yes | No | No |
| Portuguese | No | Yes | Yes, and Portuguese (Brazil) | No | Yes | Yes (Brazilian) | Yes (Brazilian) | Yes (Brazilian) | Yes (Brazilian) |
| Russian | No | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Simplified Chinese | No | Yes | Yes | No | Yes | No | No | No | Yes |
| Spanish | Yes (CO, EX, MX) | Yes | Yes | No | Yes | Yes (CO, ES, MX, US) | Yes | Yes | Yes |
| Swedish | No | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes |
| Thai | No | No | No | No | No | Yes | No | No | No |
| Traditional Chinese | No | Yes | Yes | No | Yes | No | No | No | Yes |
| Turkish | No | Yes | Yes | No | Yes | Yes | Yes | No | No |
| Serbian | No | No | Yes | No | Yes | No | No | No | No |
| Croatian | No | No | Yes | No | Yes | No | No | No | No |
| Bulgarian | No | No | Yes | No | Yes | No | No | No | No |
| Romanian | No | No | Yes | No | Yes | No | No | No | No |
| Slovenian | No | No | Yes | No | Yes | No | No | No | No |
| Slovakian | No | No | Yes | No | Yes | No | No | No | No |
| Catalan | No | No | Yes | No | Yes | No | No | No | No |