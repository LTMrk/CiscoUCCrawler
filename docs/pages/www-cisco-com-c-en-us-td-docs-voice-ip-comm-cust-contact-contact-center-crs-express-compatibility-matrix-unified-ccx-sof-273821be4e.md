---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-compatibility-matrix-unified-ccx-sof-273821be4e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_compatibility/matrix/Unified_CCX_Software_Compatibility_Matrix_for_1251_SU3.html
retrieved_at: 2026-08-16T15:02:46.381633+00:00
---

Unified CCX Software Compatibility Matrix for 1251 SU3

# Unified CCX Software Compatibility Matrix for 1251 SU3

### Download Options

Updated: July 17, 2024

Unified CCX Software Compatibility Matrix for 12.5(1) SU3

First Published: 2023-05-08

Last Updated: 2024-09-20

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

Hardware and Virtualization . 6

Third-party Software . 7

ASR and TTS . 7

Export Unified Intelligence Center Reporting . 7

Wallboard Reporting . 7

Enterprise Database (FN 2) 8

Enterprise Database for Unified Intelligence Center . 8

Microsoft Exchange Server for Email 8

Cloud Based Email Services . 8

Supported Single Sign-On Identity Providers . 9

Supported Browsers . 9

Transport Layer Security . 9

Client Operating System (FN 2,3) 10

Desktop Virtualization . 10

Application Virtualization . 10

Endpoint Devices . 11

Jabber . 12

Cisco Expressway . 13

Platform .. 13

Supported Languages . 14

Legal Information . 18

Cisco Trademark (all documentation) 19

Cisco Copyright (all documentation) 19

## Unified CCX and IP IVR

Unified CCX and Unified IP IVR

Supported Unified UCCX and Unified IP IVR Upgrade Paths (FN1,2)

Standalone Unified Intelligence Center

APIs

■ 12.5(1) SU3

■ UCSInstall_UCCX_12_5_1_UCOS_12.5.1.11003-511.sgn.iso

■ 11.6.2

■ 12.0(1)

■ 12.5(1)

■ 12.5(1) and above

CTI Server -

Versions 13 to 18

For Unified CCX configuration APIs and Finesse APIs, see the Cisco Unified Contact Center Express Developer Guide, located at: https://developer.cisco.com/site/contact-center-express/ .

(FN1) You can upgrade from any of the Engineering Specials and Service Update (SU) versions for all the mentioned Unified CCX versions.

(FN 2) Unified CCX includes the co-resident Unified Intelligence Center and Finesse.

## Solution Products and Components

Cisco Unified

Communications Manager (Unified CM)

and Business Edition

6000 and 7000 (FN 1)

G ateways for Outbound Agent and IVR ( FN 2,4)

Customer Collaboration Platform (CCP) (FN6)

Cisco Prime Collaboration

Cisco Instant Messaging and Presence (IM&P) (FN5)

Cisco Smart Software Manager On-Prem (Cisco SSM On- Prem) ( FN 9)

11.x (FN 7, 11 )

1 2.x

1 4 (FN 10)

15 (FN 12)

Prime Deployment

Prime Assurance (FN 13)

11.5(1)

12.5(1)

14.0

15

Router Series

■ 29XX

■ 43XX

■ 44XX

■ Catalyst 8200, 8300, and 8500

Cisco IOS (FN 3)

■ 15.7(3)M

■ 16.9

■ 16.12

■ 17.4

■ 17.5

■ 17.6

■ 17.9

12.5(1) SU3

12.6(1)

12.1

■ 12.5(1)

■ 14.X

8-202308 (FN 8 )

■ (FN 1) For the Unified CM version that is supported, all the corresponding Service Update (SU) and Engineering Special (ES) releases are also supported.

■ (FN 2) Outbound Agent (Predictive and Progressive) and Outbound IVR are supported only on IOS versions that incorporate Call Progress Analysis. For information on Call Progress Analysis, see https://www.cisco.com/c/en/us/tech/voice/ip-telephony-voice-over-ip-voip/index.html .

■ (FN 3) CUBE is supported with the SIP Outbound Dialer and CPA; supported versions of CUBE are ISR Pi28 15.5(3), Pi29 15.6(3), and Pi32 15.7(3) and later.

■ (FN 4) Unified CCX Agent and IVR Outbound supports E1 R2 signaling on ISR Gateway 4451 with IOS version 15.5(3)S and later.

■ (FN 5) Desktop chat requires IM&P 12.5(1) and Unified CM 12.5(1) or higher.

■ (FN 6) SocialMiner has been renamed as Customer Collaboration Platform (CCP).

■ (FN 7) Minimum requirement is 11.5 (SU4).

■ (FN 8) For more information about CSSM version 8, see the Cisco Smart Software Manager On-Prem Release .

■ (FN 9) Transport Gateway is not supported in Unified CCX.

■ (FN 10) For FIPS to be enabled on 12.5(1) SU3, the Unified CM version should be 14.0 SU3 or later. This is because of the change in the security providers in the product.

■ (FN 11) Unified CM 11.5 is compatible with all the versions up to Unified CCX 12.5 (1) SU3 ES03, to use it with Unified CCX 12.5 (1) SU3 ES04 and later, you must install the ES04-Special COP. For more information about the ES04 special COP, see the Readme .

■ (FN 12) Unified CM 15 is compatible with Unified CCX 12.5 (1) SU3 ES04 and higher. You must install Unified CCX 12.5 (1) SU3 ES04 before upgrading to Unified CM 15.

■ (FN 13) Cisco Prime Collaboration Assurance will be End of Life on October 31 st , 2024. For more information, refer to the EOL notice .

## Webex Workforce Optimization Compatibility

Unified CCX

Cisco Unified Communications Manager

Cisco Jabber

IP Phones

Webex

Webex WFO

■ 12.5(1)

■ 11.5(1)

■ 12.5(1)

■ 14

■ 15

Y es

Yes

Yes

## Hardware and Virtualization

■ For information about UC Virtualization Supported Hardware, see https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-infrastructure.html .

■ For information about Unified Communications in a Virtualized Environment, see http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html .

■ For information about Virtualization for Cisco Unified Contact Center Express, see https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-contact-center-express.html .

■ For information about Virtualization for Customer Collaboration Platform, see https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-contact-center-express.html .

■ For information about Virtualization for Cisco Unified Intelligence Center, see https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-intelligence-center.html .

## Third-party Software

### ASR and TTS

MRCP

VXML

Speech Servers

Nuance

1.0

2.0(FN 1)

2.0

Nuance Software

Cisco Virtualized Voice Browser (VVB) supports the following Nuance components

Nuance Speech Suite 11.0.12

Speech Server 7.9.0

Recognizer 11.8.0

Vocalizer Server 21.12.7 (FN 2)

Management Station 6.7.0

Krypton-4.17.0 (Dragon Voice engine)

License Manager 11.19.1

■ Latest version of the ASR-TTS packages recommended by Nuance can be used. See http://network.nuance.com/portal/server.pt . Using the latest Nuance packages will not impact the integration functionality between Unified CCX and Nuance until there is any major change by Nuance in the underlying design. However, customers must maintain the compatibility among different ASR-TTS packages as suggested by Nuance.

■ (FN 1) MRCP V2.0 is supported from Unified CCX Release 12.5(1).

■ (FN 2) This is a new versioning scheme. Nuance Enterprise Version 20.x is the continuation of Nuance Enterprise version 7.x.

### Export Unified Intelligence Center Reporting

For exporting reports

■ Microsoft Excel 2016

■ Microsoft 365 (FN 1)

■ (FN 1) Office 365 does not support authenticated Excel report permalink.

### Wallboard Reporting

Unified CCX supports wallboard reporting. Obtain the wallboard from a Cisco-approved vendor from Cisco Marketplace: https://www.cisco.com/pcgi-bin/marketplace/welcome.pl .

### Enterprise Database (FN 2)

■ Oracle 19c (FN 1)

■ Oracle 21c

■ IBM DB2 8.2, 10.5

■ MS SQL Server 2014

■ MS SQL Server 2016

■ MS SQL Server 2019

■ MS SQL Server 2022

(FN 1) Unified CCX does not support any views created on Oracle 19c.

(FN 2) Unified CCX (ES03 and higher) is qualified for encrypted external database connections to Oracle 19c, Oracle 21c, MS SQL Server 2014 (SP2 and SP3 with latest cumulative update), MS SQL Server 2016, MS SQL Server 2019, and MS SQL Server 2022.

### Enterprise Database for Unified Intelligence Center

■ MS SQL Server 2017 and above

■ Informix Database Server 12. 10.UC 9W1X3

### Microsoft Exchange Server for Email

■ Microsoft Exchange Server 2016 - Enterprise and Standard Edition

■ Microsoft Exchange Server 2019 - Enterprise and Standard Edition

### Cloud Based Email Services

■ Office 365

■ Gmail

### Supported Single Sign-On Identity Providers

Cisco Identity Service supports the Identity Providers (IdPs) that comply to generic SAML 2.0 authentication as per the considerations described in the Unified CCX Solution Design Guide located at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-implementation-design-guides-list.html .

## Supported Browsers

Firefox 123.0

Extended Support Release (ESR) and higher ESR

Google Chrome

122.0.6261.70 and higher

Microsoft Edge (Edge Chromium)

121.0.2277.128 and higher

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

Cisco Unified Intelligence Center (LiveData Gadgets)

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

■ (FN 1) The supported resolution for the Finesse desktop is 1366 x 768 or higher.

## Transport Layer Security

Transport Layer Security (TLS) 1.2 is supported for both incoming and outgoing connections.

## Client Operating System (FN 2,3)

Windows 10

Windows 11

Chromebook

Linux

MacOS

Android

Apple iOS with Safari browser

Finesse

Y

Y

Y

106.0.5249 and higher

N

Y

10.15.x and above

N

N

Cisco Unified CCX Editor Installer for Windows (FN 1)

Y

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

106.0.5249 and higher

Y

Y

10.15.x and above

N

N

■ (FN 1) The Windows User launching the Cisco Unified CCX Editor must be a part of the Windows Administrator Group.

■ (FN 2) For information on Jabber Client Operating System, refer to the specific versions of Jabber Release Notes .

■ (FN 3) The supported operating systems for Real Time Monitoring Tool are as follows:

■ Windows 10

■ Windows 11

■ Linux with KDE or GNOME client

## Desktop Virtualization

Unified CCX allows Cisco Finesse to run on third-party Virtual Desktop Infrastructure (VDI). Customers must ensure that their third-party VDI infrastructure is supported by the Cisco soft phones that are used on the agent and supervisor VDI-based desktops.

The Cisco Unified Intelligence Center and Cisco Unified Contact Center Express Administration are not supported on virtual desktops.

## Application Virtualization

■ Cisco Finesse

■ Citrix XenApp 7.x (FN 1)

■ Citrix Virtual Apps and Desktops 7 1808 and later

(FN 1) After 7.18, Citrix continued with the versioning but consolidated the product under the Citrix Virtual Apps and Desktops branding.

## Endpoint Devices

Cisco Unified IP Phones for Cisco Finesse IP Phone Agent(FN 3,6)

End Points for Cisco Finesse(FN 1,2)

Cisco IP Phone 7811(FN5)

Cisco IP Phone 7811

Cisco IP Phone 7821(FN5)

Cisco IP Phone 7821

Cisco IP Phone 7841(FN5)

Cisco IP Phone 7841

Cisco IP Phone 7861(FN5)

Cisco IP Phone 7861

Cisco IP Phone 8811

Cisco IP Phone 8811

Cisco IP Phone 8821

Cisco IP Phone 8821

Cisco IP Phone 8841

Cisco IP Phone 8841

Cisco IP Phone 8845

Cisco IP Phone 8845

Cisco IP Phone 8851

Cisco IP Phone 8851

Cisco IP Phone 8861

Cisco IP Phone 8861

Cisco IP Phone 8865

Cisco IP Phone 8865

Cisco IP Phone 8961

Cisco IP Phone 9951

Cisco IP Phone 9971

Cisco IP Phone 9841

Cisco IP Phone 9851

Cisco IP Phone 9861

Cisco IP Phone 9871

Jabber for Windows, Mac, and VDI(FN7)

Webex(FN8)

Cisco Webex DX80(FN4)

■ (FN 1) All Cisco Finesse phones support BiB.

■ (FN 2) Cisco Finesse supports with caveats mentioned in Cisco Finesse section of the Release Notes for Unified Contact Center Express Solution, located at: http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-release-notes-list.html .

Note: The Cisco Mobile Supervisor application is withdrawn from the Cisco App Store. Cisco does not provide support for Cisco Mobile Supervisor deployments.

■ (FN 3) All the Cisco IP Phones for Cisco Finesse IP Phone Agent currently do not support the Simplified New Call UI.

■ (FN 4) Telepresence CE software does not support Transfer or Conference operations from Finesse.

■ (FN 5) If Cisco Finesse IPPA agents use 78xx series phone, you must either disable the Cisco Finesse IPPA Inactivity Timeout feature or increase the timeout to be within the range of 120 seconds to one day (86400seconds), so that the agent does not get logged out of Cisco Finesse IPPA even if the agent is on any other screen.

■ (FN 6) Cisco Finesse IP Phone Agent is not supported over Mobile and Remote Access (MRA).

■ (FN 7) Unified CCX is compatible with those Jabber versions that are compatible with the Unified CM version being used with Unified CCX. The minimum supported Cisco Jabber version is 12.5.

■ (FN 8) For minimum supported versions of Unified CM and Expressway (for MRA deployments) to support Webex, see the Supported Unified CM Releases and the Supported Expressway Releases tables at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/wbxt/ucmcalling/unified-cm-wbx-teams-deployment-guide/unified-cm-wbx-teams-deployment-guide_chapter_011.html .

### Jabber

■ MRA support for Jabber requires minimum Cisco Jabber version 12.5 and Expressway 12.5. If you have VPN split-tunneling configured, you can use Jabber with MRA and the Finesse desktop on the same client machine. See https://www.cisco.com/c/en/us/support/security/anyconnect-secure-mobility-client/products-installation-and-configuration-guides-list.html for Cisco AnyConnect Mobility Client split-tunneling configuration.

■ If VPN split-tunneling is not available, you can run Jabber with MRA and the Finesse desktop after splitting them onto two clients.

■ A remote agent who runs Jabber with MRA on one client machine and the Finesse desktop with a VPN connection on a second client machine.

■ A remote agent who runs a Jabber softphone on a laptop that is connected over MRA and runs the Finesse desktop as a XenApp thin client.

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

CCM_FREEZE_14_0_1_12900_161_BT5281_GIT

Informix IDS12. 10.UC 9W1X3

1.2

Tomcat 9.0.56

2.0.0.1-1

CiscoSSL 1.1.1n.7.2.390

7.8.2003

OpenJDK 1.8.0_262

■ Custom Classes/SDK

■ Real-Time Reporting

## Supported Languages

ASR Grammar for Workflow Steps

IP Phone Agent Supported Languages

Unified Intelligence Center (FN 2)

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

## Legal Information

THE SPECIFICATIONS AND INFORMATION REGARDING THE PRODUCTS IN THIS MANUAL ARE SUBJECT TO CHANGE WITHOUT NOTICE. ALL STATEMENTS, INFORMATION, AND RECOMMENDATIONS IN THIS MANUAL ARE BELIEVED TO BE ACCURATE BUT ARE PRESENTED WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. USERS MUST TAKE FULL RESPONSIBILITY FOR THEIR APPLICATION OF ANY PRODUCTS.

THE SOFTWARE LICENSE AND LIMITED WARRANTY FOR THE ACCOMPANYING PRODUCT ARE SET FORTH IN THE INFORMATION PACKET THAT SHIPPED WITH THE PRODUCT AND ARE INCORPORATED HEREIN BY THIS REFERENCE. IF YOU ARE UNABLE TO LOCATE THE SOFTWARE LICENSE OR LIMITED WARRANTY, CONTACT YOUR CISCO REPRESENTATIVE FOR A COPY.

The Cisco implementation of TCP header compression is an adaptation of a program developed by the University of California, Berkeley (UCB) as part of UCB's public domain version of the UNIX operating system. All rights reserved. Copyright © 1981, Regents of the University of California.

NOTWITHSTANDING ANY OTHER WARRANTY HEREIN, ALL DOCUMENT FILES AND SOFTWARE OF THESE SUPPLIERS ARE PROVIDED "AS IS" WITH ALL FAULTS. CISCO AND THE ABOVE-NAMED SUPPLIERS DISCLAIM ALL WARRANTIES, EXPRESSED OR IMPLIED, INCLUDING, WITHOUT LIMITATION, THOSE OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OR ARISING FROM A COURSE OF DEALING, USAGE, OR TRADE PRACTICE.

IN NO EVENT SHALL CISCO OR ITS SUPPLIERS BE LIABLE FOR ANY INDIRECT, SPECIAL, CONSEQUENTIAL, OR INCIDENTAL DAMAGES, INCLUDING, WITHOUT LIMITATION, LOST PROFITS OR LOSS OR DAMAGE TO DATA ARISING OUT OF THE USE OR INABILITY TO USE THIS MANUAL, EVEN IF CISCO OR ITS SUPPLIERS HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

Any Internet Protocol (IP) addresses and phone numbers used in this document are not intended to be actual addresses and phone numbers. Any examples, command display output, network topology diagrams, and other figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses or phone numbers in illustrative content is unintentional and coincidental.

All printed copies and duplicate soft copies are considered un-Controlled copies and the original on-line version should be referred to for latest version.

Cisco has more than 200 offices worldwide. Addresses, phone numbers, and fax numbers are listed on the Cisco website at https://www.cisco.com/site/us/en/about/contact-cisco/index.html .

## Cisco Trademark (all documentation)

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: https://www.cisco.com/c/en/us/about/legal/trademarks.html . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company.

## Cisco Copyright (all documentation)

© 2024 Cisco Systems, Inc. All rights reserved.

| Unified CCX and Unified IP IVR | Supported Unified UCCX and Unified IP IVR Upgrade Paths (FN1,2) | Standalone Unified Intelligence Center | APIs |
|---|---|---|---|
| ■ 12.5(1) SU3 ■ UCSInstall_UCCX_12_5_1_UCOS_12.5.1.11003-511.sgn.iso | ■ 11.6.2 ■ 12.0(1) ■ 12.5(1) | ■ 12.5(1) and above | CTI Server - Versions 13 to 18 For Unified CCX configuration APIs and Finesse APIs, see the Cisco Unified Contact Center Express Developer Guide, located at: https://developer.cisco.com/site/contact-center-express/ . |

| Cisco Unified Communications Manager (Unified CM) and Business Edition 6000 and 7000 (FN 1) | G ateways for Outbound Agent and IVR ( FN 2,4) | Customer Collaboration Platform (CCP) (FN6) | Cisco Prime Collaboration | Cisco Instant Messaging and Presence (IM&P) (FN5) | Cisco Smart Software Manager On-Prem (Cisco SSM On- Prem) ( FN 9) |
|---|---|---|---|---|---|
| 11.x (FN 7, 11 ) | 1 2.x | 1 4 (FN 10) | 15 (FN 12) | Prime Deployment | Prime Assurance (FN 13) |
| 11.5(1) | 12.5(1) | 14.0 | 15 | Router Series ■ 29XX ■ 43XX ■ 44XX ■ Catalyst 8200, 8300, and 8500 Cisco IOS (FN 3) ■ 15.7(3)M ■ 16.9 ■ 16.12 ■ 17.4 ■ 17.5 ■ 17.6 ■ 17.9 | 12.5(1) SU3 | 12.6(1) | 12.1 | ■ 12.5(1) ■ 14.X | 8-202308 (FN 8 ) |

|  | Unified CCX | Cisco Unified Communications Manager | Cisco Jabber | IP Phones | Webex |
|---|---|---|---|---|---|
| Webex WFO | ■ 12.5(1) | ■ 11.5(1) ■ 12.5(1) ■ 14 ■ 15 | Y es | Yes | Yes |

| MRCP | VXML | Speech Servers |
|---|---|---|
| Nuance |
| 1.0 2.0(FN 1) | 2.0 | Nuance Software | Cisco Virtualized Voice Browser (VVB) supports the following Nuance components |
| Nuance Speech Suite 11.0.12 | Speech Server 7.9.0 Recognizer 11.8.0 Vocalizer Server 21.12.7 (FN 2) Management Station 6.7.0 Krypton-4.17.0 (Dragon Voice engine) License Manager 11.19.1 |

| For exporting reports | ■ Microsoft Excel 2016 ■ Microsoft 365 (FN 1) |
|---|---|

|  | Firefox 123.0 Extended Support Release (ESR) and higher ESR | Google Chrome 122.0.6261.70 and higher | Microsoft Edge (Edge Chromium) 121.0.2277.128 and higher |
|---|---|---|---|
| Unified CCX Administration | Y | Y | Y |
| Cisco Finesse (FN 1) | Y | Y | Y |
| Cisco Unified Intelligence Center | Y | Y | Y |
| Cisco Unified Intelligence Center (LiveData Gadgets) | Y | Y | Y |
| CCP Administration | Y | Y | Y |
| Cisco Identity Service Administration | Y | Y | Y |

|  | Windows 10 | Windows 11 | Chromebook | Linux | MacOS | Android | Apple iOS with Safari browser |
|---|---|---|---|---|---|---|---|
| Finesse | Y | Y | Y 106.0.5249 and higher | N | Y 10.15.x and above | N | N |
| Cisco Unified CCX Editor Installer for Windows (FN 1) | Y | Y | N | N | N | N | N |
| Cisco Unified CCX Editor Web Launcher | Y | Y | Y 106.0.5249 and higher | Y | Y 10.15.x and above | N | N |

| Cisco Unified IP Phones for Cisco Finesse IP Phone Agent(FN 3,6) | End Points for Cisco Finesse(FN 1,2) |
|---|---|
| Cisco IP Phone 7811(FN5) | Cisco IP Phone 7811 |
| Cisco IP Phone 7821(FN5) | Cisco IP Phone 7821 |
| Cisco IP Phone 7841(FN5) | Cisco IP Phone 7841 |
| Cisco IP Phone 7861(FN5) | Cisco IP Phone 7861 |
| Cisco IP Phone 8811 | Cisco IP Phone 8811 |
| Cisco IP Phone 8821 | Cisco IP Phone 8821 |
| Cisco IP Phone 8841 | Cisco IP Phone 8841 |
| Cisco IP Phone 8845 | Cisco IP Phone 8845 |
| Cisco IP Phone 8851 | Cisco IP Phone 8851 |
| Cisco IP Phone 8861 | Cisco IP Phone 8861 |
| Cisco IP Phone 8865 | Cisco IP Phone 8865 |
|  | Cisco IP Phone 8961 |
|  | Cisco IP Phone 9951 |
|  | Cisco IP Phone 9971 |
|  | Cisco IP Phone 9841 |
|  | Cisco IP Phone 9851 |
|  | Cisco IP Phone 9861 |
|  | Cisco IP Phone 9871 |
|  | Jabber for Windows, Mac, and VDI(FN7) |
|  | Webex(FN8) |
|  | Cisco Webex DX80(FN4) |

| Cisco Expressway | X12.5.6 and later (FN 1) |
|---|---|

| UCOS Platform Version | Internal Unified CCX Database (IDS) | Transport Layer Security (TLS) | Tomcat | Open SSL | Cent OS | Java versions |
|---|---|---|---|---|---|---|
| Servers |
| CCM_FREEZE_14_0_1_12900_161_BT5281_GIT | Informix IDS12. 10.UC 9W1X3 | 1.2 | Tomcat 9.0.56 | 2.0.0.1-1 CiscoSSL 1.1.1n.7.2.390 | 7.8.2003 | OpenJDK 1.8.0_262 ■ Custom Classes/SDK ■ Real-Time Reporting |

|  | ASR Grammar for Workflow Steps | IP Phone Agent Supported Languages | Unified Intelligence Center (FN 2) | Unified CCX Administration | Finesse | IVR Prompts | CCP | TTS | VXML Grammar | Workforce Management | Quality Management |
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