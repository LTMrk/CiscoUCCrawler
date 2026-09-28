---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-ucce-compatibility-matrix-contact-73f060cea9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/ucce_compatibility/matrix/Contact_Center_Enterprise_Solution_Compatibility_Matrix_Release_12_5.html
retrieved_at: 2026-08-16T14:54:17.871764+00:00
---

Contact Center Enterprise Solution Compatibility Matrix, Release 12.5(x)

# Contact Center Enterprise Solution Compatibility Matrix, Release 12.5(x)

### Download Options

Updated: April 14, 2024

Contact Center Enterprise Solution Compatibility Matrix, Release 12.5(x)

First Published : April 6, 2022

NOTE: Works with document’s Advanced Properties “First Published” property. Click File | Properties | Advanced Properties | Custom .

Last Updated: August 21, 2024

EDCS Document #: 23088169

Americas Headquarters

Cisco Systems, Inc.

170 West Tasman Drive

San Jose, CA 95134-1706 USA

http://www.cisco.com Tel: 408 526-4000

800 553-NETS (6387) Fax: 408 527-0883

Contents

Central Controller and Component Compatibility . 1

Cisco Gateway Hardware and Software . 1

IOS Versioning Key 16.1(4) M3 and 16.1(4) T1 as Examples . 1

IOS-XE Versioning Key 16.12.1a and 16.12.3 as Examples . 1

Cisco Unified SIP Proxy (Deprecated) 1

Third-party SIP Proxy . 1

End Points for Agents and Callers . 1

Endpoints Supported for Callers Only . 1

Single Sign On (SSO) Identity Providers (IdPs) 1

Transport Layer Security . 1

Client Operating System .. 1

Supported Browsers . 1

Browser Exceptions . 1

Server Operating System .. 1

SQL Server and Informix Versions . 1

Java JRE and JDK . 1

Supported Languages . 1

Microsoft .NET Framework . 1

Other Supported Software . 1

Virtual Desktop Infrastructure Support 1

VMWare ESXI Compatibility . 1

Automatic Speech Recognition and Text to Speech . 1

Load Balancers . 1

Non-Reference Design Compatibility . 1

Unified CCE Parent Child Compatibility . 1

ICM-to-ICM Gateway Compatibility . 1

Third Party ACDs . 1

Avaya . 1

Avaya Nortel 1

Avaya Aura Contact Center . 1

Nortel SDK . 1

Legal Information (software documentation only) 1

Cisco Trademark (all documentation) 1

Cisco Copyright (all documentation) 1

Overview

The Contact Center Enterprise (CCE) Solution Compatibility Matrix includes all the Cisco CCE solutions and component compatibility information. This compatibility matrix specifies all supported configurations and versions for Release 12.5(x), which includes the maintenance or ES releases of 12.5(x). The information in this compatibility matrix supersedes compatibility information in any other CCE documentation. If the Compatibility Matrix does not state a configuration or version, then it does not support it.

The process of migrating from Unified CCE, Packaged CCE, or Hosted Collaboration Solution for CC to Webex CCE is like performing a premise-based tech refresh, but with a few key differences pointed out within this document. This document provides guidance on the access and tools available and recommendations on how to accomplish a Webex CCE migration. This document focuses on the core Cisco components. It does not provide information about third-party solution components.

Notes

■ Make sure that your Router, Logger, and AW are in the same version as your PG or in a version that is higher than your PG.

■ The Compatibility Matrix specifies all supported third-party software (such as Nuance and Informix) and its versions. Support for these software versions and their interoperability depends on the release cycles (patches and upgrades) of the third-party software. For example, support for ESXi depends on VMware release cycles.

■ Cisco Hosted Collaboration Solution for Contact Center (HCS for CC) shares the same media kit as Cisco Unified CCE, which includes some components not supported in a Cisco HCS for CC deployment.

■ Packaged CCE: In Release 12.5(x), the multistage upgrade support is backward compatible with Release 12.0 only. For all releases prior to 12.0, all components must be on the same release.

Exception: Cisco Unified CM (CUCM) can continue to be on an earlier compatible release for an off-box solution deployment.

■ Support for a CUCM release is inclusive of all updates.

■ For details on the browsers and the languages that are supported by Cisco Webex Experience Management, see Experience Management .

■ Upgrade all the solution components to experience the new features delivered as part of a particular solution release version. Upgrading only the component that delivers the new feature may not be sufficient in all cases. For more information on upgrade paths, see the CCE Upgrade Flowcharts in the respective Contact Center Enterprise Installation and Upgrade Guides .

■ IP IVR 12.5(1), IP IVR 12.5(1) SU1 , IP IVR 12.5(1) SU2, and IP IVR 12.5(1) SU3 are compatible with CCE 12.5(x) .

## Central Controller and Component Compatibility

PCCE/UCCE Components, Release 12.5(x)

PCCE/UCCE/HCS for CC components, Release 12.0

IdS (Standalone)

Finesse

ECE

CVP

VVB

CUIC (Standalone)

CUIC-LiveData-IdS (Coresident)

Router

Logger

AW

Live Data (Standalone)

PG

SocialMiner

CCMP/CCDM

Notes

Router

N

N

N

Y

Y

N

Logger

N

Y

Y

N

AW

N

N

N

N

N

N

N

Y

Y

N

Live Data (Standalone)

N

N

N

N

Y

PG

N

N

N

N

N

N

N

N

PCCE/UCCE/HCS for CC Components, Release 12.5(1)

PCCE/UCCE/HCS for CC Components, Release 12.0

IdS (Standalone)

Finesse

ECE

CVP

VVB

CUIC (Standalone)

CUIC-LiveData-IdS (Coresident)

Router

Logger

AW

Live Data (Standalone)

PG

SocialMiner

CCMP/ CCDM

Notes

Identity Server (Standalone)

Y

Y

Y

Y

Finesse

N

N

Y

N

Y

Y

Y

Y

For Live data gadgets to load in Cisco Finesse, install CUIC 12.0(1) ES 06 or later on Live Data (Standalone) server. See Notes for more information.

ECE

N

Y

Y

Y

CVP

Y

Y

Y

Y

Y

On PCCE 12.0, install CCE 12.0 ES37 before you upgrade CVP to 12.5(1).

VVB

Y

CUIC (Standalone)

N

N

Y

Y

CUIC-LiveData-IdS (Coresident)

N

N

N

Y

Customer Collaboration Platform

N

CCMP

Y

Y

Y

Y

Not Applicable to Packaged CCE.

CCDM

Y

Y

Y

Y

Applicable only to HCS for CC.

Unified CCE/HCS for CC Components, Release 12.5(x)

Unified CCE/HCS for CC Components, Release 11.6

IdS (Standalone)

Finesse

ECE

CVP

VVB

CUIC (Standalone)

CUIC-LiveData-IdS (Coresident)

Router

Logger

AW

Live Data (Standalone)

PG

SocialMiner

CCMP/ CCDM

Notes

Router

N

N

N

Y

Y

N

Logger

N

Y

Y

N

AW

N

N

N

N

N

N

N

Y

Y

N

Live Data (Standalone)

N

N

N

N

Y

24000 Agent Deployment is not supported with PG 11.6.

PG

N

N

N

N

N

N

N

N

Unified CCE/HCS for CC Components, Release 12.5(1)

Unified CCE/HCS for CC Components, Release 11.6

IdS (Standalone)

Finesse

ECE

CVP

VVB

CUIC (Standalone)

CUIC-LiveData-IdS (Coresident)

Router

Logger

AW

Live Data (Standalone)

PG

SocialMiner

CCMP/ CCDM

Notes

Identity Server (Standalone)

Y

Y

Y

Y

Finesse

N

N

Y

N

Y

Y

Y

Y

For Live data gadgets to load in Cisco Finesse, ensure to install CUIC 11.6(1) ES18 or later on Live Data (Standalone) server. See Notes for more information.

ECE

N

Y

Y

Y

ECE 12.5 is not compatible with Packaged CCE 11.6.

CVP

Y

Y

Y

Y

Y

VVB

Y

CUIC (Standalone)

N

N

Y

Y

CUIC-LiveData-IdS (Coresident)

N

N

N

Y

Customer Collaboration Platform

N

CCMP

Y

Y

Y

Y

CCMP is not applicable to Packaged CCE.

On UCCE and HCS for CC 11.6, install UCCE 11.6(1) ES 7 before you upgrade CCMP to 12.5(1).

CCDM

Y

Y

Y

Y

CCDM is applicable only to HCS for CC.

On HCS for CC 11.6, install UCCE 11.6(1) ES 7 before you upgrade CCDM to 12.5(1).

Notes

■ Unified CCE and Packaged CCE compatibility with CUCM:

— CUCM 11.5, 12.0, and 12.5 are supported with Unified CCE, Packaged CCE, and HCS for CC, Release 12.5.

— CUCM 14 is supported with Unified CCE and Packaged CCE, Release 12.5 if UCCE 12.5(1) ES 72 or 12.5(2) MR is installed.

— CUCM 15 is supported with Unified CCE, Release 12.5(2). CUCM 15 is supported with Packaged CCE Release 12.5(2) if CCE 12.5(2) ES 38 is installed.

■ Cisco Unified Contact Center Management Portal (CCMP) compatibility with CUCM:

— CUCM 11.5, 12.0, 12.5 and 14 are supported with CCMP, Release 12.5.

— CUCM 15 is supported with CCMP, Release 12.5 if CCMP 12.5(1) ES 12 is installed.

■ CCE 12.5 supports the latest versions of Cisco Smart Software Manager (CSSM) On-Prem 8.x, that were released in the year 2022.

■ In Live Data (standalone) 11.6 and 12.0 deployments, when CUIC and Cisco Finesse components are in version 12.5, Live Data gadgets will not load in Cisco Finesse. You must enable Cross-Origin Resource Sharing (CORS) and set Finesse host URLs to load the Live Data gadgets.

■ For more information on CORS CLIs, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide .

■ To find a comprehensive list of the guides available for a specific release, see the respective Documentation Guides.

## Cisco Gateway Hardware and Software

Gateway Functionality

Central Controller version 12.5(x) Model

Software Version

Software Feature Set

VXML Gateway Browser

Call Progress Analysis for Outbound Options for SIP Trunks (CUBE)

Unified CCE, Packaged CCE, And Cisco HCS for CC Support

ASR 1001X

ASR 1002X

ASR 1004 RP2

ASR 1006 RP2

IOS XE 16.6

Universal

No

Yes

Yes

IOS XE 16.9

IOS XE 16.12

IOS XE 17.2

IOS XE 17.6

IOS XE 17.9

Virtual CUBE

IOS XE 16.6

Universal

No

No

Yes

IOS XE 16.9

IOS XE 16.12

IOS XE 17.2

IOS XE 17.6

IOS XE 17.9

15.7(3)M1

ISR G3 43xx (4321, 4331, 4351)

ISR G3 44xx (4431, 4451, 4461)

IOS XE 16.6

Universal

No

Yes

Yes

IOS XE 16.9

IOS XE 16.12

IOS XE 17.2

IOS XE 17.6

IOS XE 17.9

Catalyst 8200/8300

IOS XE 17.6

Universal

No

Yes

Yes

IOS XE 17.9

Notes

■ Virtual CUBE (vCUBE) can run either on Cisco Cloud Services Router (CSR) 1000V (if you use IOS XE 16.9, 16.12, or 17.2) or Cisco Catalyst 8000V Edge Software (if you use IOS XE 17.4 or 17.6).

■ All gateways in the preceding table support inbound contact center calls. For details on support for Call Progress Analysis (CPA) for Outbound Option with TDM Trunks, see the Cisco ASR 1000 Series documentation at https://www.cisco.com/c/en/us/support/routers/asr-1000-series-aggregation-services-routers/products-documentation-roadmaps-list.html

■ For IPv6-enabled deployments, the supported IOS versions for NAT64 translations are 15.4(2)T3 and later releases.

■ Multi-VRF requires IOS XE 16.3.4 to support HCS for CC.

■ The Virtual Assistant–Voice (VAV) feature is supported only on Unified CVP and Cisco VVB. It is not supported with the VXML Gateway.

### IOS Versioning Key 16.1(4) M3 and 16.1(4) T1 as Examples

■ 16.1 is the version number.

■ (4) is the release number.

■ M3 and T1 are the train release numbers. M is the mainline train and T is the technology train.

■ An increment in the release number after M or T refers to additional bug fixes.

### IOS-XE Versioning Key 16.12.1a and 16.12.3 as Examples

■ 16.12 is the version number.

■ 1 and 3 are the increment release numbers with additional bug fixes.

■ "a" indicates a special release.

■ Every three releases include a maintenance release incremented as 16.3, 16.6, 16.9, 16.12, 17.3, and so on.

## Cisco Unified SIP Proxy (Deprecated)

Supported Versions: Unified CCE, Packaged CCE and HCS for CC solutions support Cisco Unified SIP Proxy (CUSP) 10.0(x), 10.1(x) and 10.2(x) only in non-secure mode.

Notes: CUSP is deprecated. For more information, see End-of-Sale and End-of-Life Announcement for the Cisco Unified SIP Proxy Version 10 .

## Third-party SIP Proxy

Cisco recommends Oracle® Communication Session Router, version SCZ9.1.0 GA (Build 46) or later. However, you can also choose to deploy any third-party SIP proxy that suits your requirement.

## End Points for Agents and Callers

Endpoint

Voice & Finesse Desktop

Video

Unified CM Silent Monitor

BIB-based recording

Agent Greeting

Whisper Announcements

Finesse IP Agent Phone

IPv6 SCCP (UCCE Only)

IPv6 SIP

MRA

7821, 7841, 7861

Y

N

Y

Y

Y

Y

Y

N

Y

Yes Audio Only

7942G,7945G, 7962G,7965G, 7975G

Y

N

Y

Y

Y

Y

N

Y

N

N

8811, 8821, 8841, 8851, 8851NR, 8861

Y

N

Y

Y

Y

Y

Y

N

Y

Yes Audio Only

8845, 8865

Y

Y

Y

Y

Y

Y

Y

Y

Y

Yes Audio Only

9841, 9851, 9861, 9871

Y

N

Y

Y

Y

Y

N

N

Y

Yes Audio only

EX60

Y

Y

N

N

N

N

N

N

Y

N

Jabber for Mac

Y

Y

Voice only

Y

N

Y

N

N

N

Y

Jabber for VDI

Y

N

N

Y

Y

Y

N

N

N

Y

Jabber for Windows

Y

Y

Voice-only

Y

Y

Y

N

N

N

Y

Webex App for MacOS/Windows

Y

Y

Y

Y

Y

Y

N

N

Y

Y

Webex App for VDI

Y

Y

Y

Y

Y

Y

N

N

N

Y

MX300 G2, MX700, MX800 Telepresence

Y

Y

N

N

N

N

N

N

Y

N

SX10, SX20, SX80 Telepresence

Y

Y

N

N

N

N

N

N

Y

N

Notes

■ The phone models that are end-of-sale and end-of-software-maintenance will continue to work with Contact Center Enterprise solutions. The phone models that are end-of-support are still compatible with Contact Center Enterprise solutions, but they are neither tested nor supported by Cisco.

— For end-of-life and end-of-sale announcements, see https://www.cisco.com/c/en/us/products/eos-eol-listing.html .

— For information on a specific endpoint, see the product page of the endpoint.

■ General: Only the Cisco IP Phones listed in the preceding table are supported as contact center agent phones. As an alternative, you can deploy the Mobile Agent solution to enable the contact center to use any phone as an agent phone.

■ General: The Join Across Line (JAL) and Direct Transfer Across Line (DTAL) phone features aren’t supported, and must be disabled on phones that come packaged with these features and local CTI ports (LCP) for Mobile Agent.

■ General: For any phone that allows Single-Line Mode, you can use Shared Line on a non-ACD line. You must have your PG in Single-Line Mode (set the Agent Phone Line Control setting to Single Line).

■ General: Other than call initiation, all other call control on the non-ACD extensions is supported from multiline capable desktops. Calls initiated from the hard phone can be controlled after initial call setup.

■ 78xx: If Cisco Finesse IPPA agents use 78xx series phone, you must either disable the Cisco Finesse IPPA Inactivity Timeout feature or increase the timeout in the range of 120 seconds to one day (86400 seconds), so that the agent doesn’t get logged out of Cisco Finesse IPPA even if the agent is on any other screen.

■ 88xx phones are supported only with desktop controls in the Standard Line mode. If both desktop and device controls are required, use the Enhanced Line mode.

■ 89xx and 99xx: 89xx and 99xx series phones don’t support video prompt and queue.

■ 89xx, 99xx: These phones don’t support directly disabling the Join Across Line (JAL) and Direct Transfer Across Line (DTAL) phone features. Instead, you must configure the Unified CM PG to use Multi-Line only. This setting applies to all phones controlled by that specific Unified PG. You cannot configure it on a phone-by-phone basis. Also, configure all phones with Set Maximum number of calls to 2 and Set Busy trigger to 1.

■ Webex:

— For minimum supported versions of CUCM and Expressway (for MRA deployments) to support Webex, see the Supported Unified CM Releases and the Supported Expressway Releases tables at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/wbxt/ucmcalling/unified-cm-wbx-teams-deployment-guide/unified-cm-wbx-teams-deployment-guide_chapter_011.html .

■ Jabber:

— Agent Greeting support for Jabber requires minimum Cisco Jabber version 12.9.

— MRA support for Jabber requires minimum Cisco Jabber version 12.5 and Expressway 12.5. If you have VPN split-tunneling configured, you can use Jabber with MRA and the Finesse desktop on the same client machine. See https://www.cisco.com/c/en/us/support/security/anyconnect-secure-mobility-client/products-installation-and-configuration-guides-list.html for Cisco AnyConnect Mobility Client split-tunneling configuration.

— If VPN split-tunneling isn’t available, use one of the following options for the remote agents:

o A remote agent who runs Jabber with MRA on one client machine and the Finesse desktop with a VPN connection on a second client machine.

o A remote agent who runs a Jabber softphone on a laptop that is connected over MRA and runs the Finesse desktop as a Xenapp thin client on the same laptop.

— Jabber for VDI isn’t supported in Video Contact Center deployments.

— Jabber Multiline feature is supported from CCE 11.6.

— For Cisco Jabber software compatibility details, see the Planning guide for Cisco Jabber at https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

■ The phone models that are on end-of-life plan and have reached the end of maintenance for CUCM Release 14 will no longer register. For more information on the end-of-life phones, see the Field Notices at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-field-notices-list.html .

## Endpoints Supported for Callers Only

Callers outside of the enterprise's network can use the following endpoints:

■ Jabber for iOS

■ Jabber for Android

## Single Sign On (SSO) Identity Providers (IdPs)

This Unified CCE release supports the following IdPs:

Identity Providers

Versions

Microsoft AD FS (Active Directory Federation Services)

AD FS 5.0: Windows Server 2019

AD FS 4.0: Windows Server 2016

AD FS 3.0: Windows Server 2012 R2

PingFederate

8.2.2.0

OpenAM

10.0.1

Shibboleth

3.3.0

F5

13

Besides the IdPs listed above, Unified CCE supports all SAML 2.0 compliant IdPs. See the documentation of your IdP for details on configuring the IdP in CCE.

Notes

■ CCMP and Cisco Unified Contact Center Domain Manager (CCDM), Release 12.5 support Microsoft AD FS 2012 R2 and 2016 with WS-Federation via JSON Web Token (JWT). However, user authentication access for CCMP and CCDM can be provided by one of the supported IdPs via Federated Trust with Microsoft AD FS. Federated Trust is supported per Microsoft AD FS and third-party IdP documentation and support.

■ Kerberos is supported for single-domain authentication (non-federated environments). Kerberos isn’t supported on HCS for CC.

■ For ECE:

— Agent-based users have the same compatibility as Cisco IDS.

— Supervisors outside Cisco Finesse support any SAML 2.0 complaint IDP.

## Transport Layer Security

The Unified CCE database access encrypts SQL user authentication using TLS, but the data connection isn’t encrypted.

12.5 Component

TLS 1.2

Web Interfaces

Database Access

PCCE

✔

✔

UCCE/ICM

✔

✔

AW Distributor/HDS/Logger

N/A

✔

Internet Script Editor

✔

N/A

CCE Admin

✔

✔

Web Setup

✔

✔

Diagnostic Portal

✔

N/A

Live Data

✔

✔

CTIOS C++ CIL

✔

N/A

SQL Gateway - DB Lookup

N/A

✔

Protocol - CTI Server and Media Routing

N/A

✔

CVP [1]

✔

N/A

VVB

✔

N/A

IdS

✔

N/A

Finesse

✔

✔

CUIC

✔

✔

ECE

✔

✔

Live Data

✔

N/A

Customer Collaboration Platform

✔

N/A

CCMP/CCDM

✔

X

ACD

X

N/A

UC Manager

✔

N/A

1 For more information, check the Release Notes at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html .

## Client Operating System

Components

Clients OS

Cisco Finesse

Microsoft Windows 11 (64 bit)

Microsoft Windows 10

Note: CCE Release 12.5(1) supports Microsoft Windows 10 only. CCE Release 12.5(2) supports Microsoft Windows 10 and Windows 11 (64 bit).

Mac OS X 10.12, 10.13 and10.14

ChromeOS 70 (64-bit) and higher

Cisco Unified Call Studio

Microsoft Windows 10 (64-bit)

Administration Client

Microsoft Windows Server 2016 and 2019 (Standard and Datacenter editions)

Note: CCE Release 12.5(1) supports Microsoft Windows Server 2016 only. CCE Release 12.5(2) supports Microsoft Windows Server 2016 and 2019.

Microsoft Windows 10 (Enterprise and Professional) Microsoft Windows 11 (Enterprise and Professional) (64-bit)

Internet Script Editor (ISE)

Microsoft Windows 10 (Enterprise and Professional) Microsoft Windows 11 (Enterprise and Professional) (64-bit)

Silent Monitor Service for Unified CCE Toolkit

Microsoft Windows 10 (Enterprise and Professional)

CTI OS Clients

Microsoft Windows 10 (Enterprise and Professional)

Note: For more information on the supported versions of Microsoft Windows 10 with specific versions of .NET Framework, see the Microsoft documentation.

Notes

■ CTI OS is only supported for Unified ICM when used in conjunction with Avaya PG, Aspect PG, AACC (Symposium) PG, or non-reference design deployments like Parent-Child that employ Unified CCE System PG. The supported CTI OS version is aligned with the supported PG version.

■ CTI OS and CAD are not supported from Unified CCE, Release 11.5(x). New and existing deployments upgrading to Unified CCE release 12.0(1) or later must use Finesse desktop instead of CTI OS and CAD.

■ Silent Monitoring Service is not supported on CTI OS deployments starting with Unified CCE release 11.5(1).

## Supported Browsers

Operating System

Browser Version

Microsoft Windows Server 2016 (Standard and Datacenter editions)

Microsoft Windows Server 2019 (Standard and Datacenter editions)

Internet Explorer v11.3085.14393.0 or later in Native Mode

Chrome v76.0.3809 or later

Firefox Extended Supported Release (ESR) 68 and later ESRs

Edge Chromium (Microsoft Edge v79 and later)

Microsoft Windows 10 and Windows 11 (64 bit)

Note: CCE Release 12.5(1) supports Microsoft Windows 10 only. CCE Release 12.5(2) supports Microsoft Windows 10 and Windows 11 (64 bit).

Internet Explorer v11.345.17134 or later in Native Mode

Google Chrome v76.0.3809 or later

Firefox ESR 68 and later ESRs

Edge Chromium (Microsoft Edge v79 and later)

Mac OS X

Firefox ESR 68 and later ESRs

Google Chrome v76.0.3809 or later

Chromebook with Chrome OS v70

Chromium v73 or later

Google Chrome v60 or later

Notes

■ For information about supported browsers for Cisco Webex Experience Management, refer to https://cloudcherry.com/docs/user/getting-help/ .

■ CCE Release 12.5(1) supports Microsoft Windows Server 2016 only. CCE Release 12.5(2) supports Microsoft Windows Server 2016 and 2019.

■ Unified CCE Administration requires full screen view of the browser with the minimum resolution of 1366 x 768.

■ All browsers must support SHA-256 certificates.

## Browser Exceptions

■ Windows 10 has Microsoft Edge as default browser. Enable Internet Explorer v11.345.17134 or later in native mode as default browser, if required.

■ CCE Administration Client (AW) Setup tool does not support Firefox and Chrome. Use Internet Explorer v11.345.17134 or later versions, or Microsoft Edge v41.16299.15.0 or later.

■ CVP Operations Console (OAMP) and VVB App admin are supported on Internet Explorer, only in compatibility mode. To ensure that all the functionalities of CVP OAMP work in Internet Explorer, set the emulation level to at least 10 by following the steps documented in the Test your sites for document mode compatibility section at Fix web compatibility issues using document modes and the Enterprise Mode site list .

■ In Enterprise Chat and Email, Edge Chromium is supported only for Agent Desktops. For more information, see System Requirements for Enterprise Chat and Email, Release 12.5(1) .

## Server Operating System

Components

Server OS

Unified CCE, Packaged CCE, ICM, and System PG

Microsoft Windows Server 2016 and 2019 (Standard and Datacenter editions)

Unified CVP

Microsoft Windows Server 2016 and 2019 (Standard and Datacenter editions)

Enterprise Chat and Email

Microsoft Windows Server 2019 (Standard and Datacenter editions)

Unified CCMP

Microsoft Windows Server 2019 (Standard and Datacenter editions)

Silent Monitor Server

Microsoft Windows Server 2016 and 2019 (Standard and Datacenter editions)

CTI OS Server

Microsoft Windows Server 2016 and 2019 (Standard and Datacenter editions)

Notes

■ CCE Release 12.5(1) supports Microsoft Windows Server 2016 only. CCE Release 12.5(2) supports Microsoft Windows Server 2016 and 2019.

■ Unified ICM/CCE is qualified only on a retail installation of the Microsoft Windows Server (Standard and Datacenter editions). Cisco doesn't support Unified ICM/CCE on a customized Microsoft Windows image (for example, a corporate image). If you use a customized image of the Microsoft Windows operating system, the Unified ICM/CCE application can fail.

## SQL Server and Informix Versions

Components

SQL Server Version

Unified CCE, Packaged CCE, and ICM

Microsoft SQL Server 2017 (Standard and Enterprise editions) with cumulative updates

Microsoft SQL Server 2019 (Standard and Enterprise editions) with cumulative updates

Note: Microsoft SQL Server 2019 with native compatibility level 150 and backward compatibility level 140 of Microsoft SQL Server 2017 is supported.

Note: Contact Center Enterprise solution supports only the 64-bit version of Microsoft SQL Server. Contact Center Enterprise solution does not support the following:

■ Encrypted connections to SQL Server.

■ Linked Server feature of SQL Server.

Unified CVP

IBM Informix Dynamic Server Version 14.10.FC8

Enterprise Chat and Email

■ ECE 400 agent deployment: Microsoft SQL Server 2016 SP2 (Standard and Enterprise editions)

■ ECE 1500 agent deployment: Microsoft SQL Server 2016 SP2 (Standard and Enterprise editions)

■ ECE Geographically Redundant/High Availability installation: Microsoft SQL Server 2016 (Enterprise edition)

Unified CCMP

Microsoft SQL Server 2016 SP2 (Standard edition)

Unified CCDM

Microsoft SQL Server 2016 SP2 (Standard edition)

Notes

■ CCE Release 12.5(1) supports Microsoft SQL Server 2017 only. CCE Release 12.5(2) supports Microsoft SQL Server 2017 and 2019.

■ For CCE components, the combination of Windows Server 2016 with SQL Server 2019, or Windows Server 2019 with SQL Server 2017 is not supported.

## Java JRE and JDK

The following are the Java Runtime Environment (JRE) versions that are supported:

■ Unified CCE uses OpenLogic’s OpenJDK JRE version 1.8 (32-bit), update 272 or later with the 12.5(1a) base installer and 12.5(1) ES55 (and all subsequent updates). 12.5(1) installations prior to ES55 support Oracle JRE versions.

■ Unified CVP uses OpenLogic's OpenJDK JRE version 1.8 (64-bit), update 275 or later with the 12.5(1a) base installer and 12.5(1) ES18 (and all subsequent updates). 12.5(1) installations prior to ES18 support Oracle JRE versions.

■ Cisco Enterprise Chat and Email, Cisco CCMP, and CCDM use Oracle JRE version 1.8 (32-bit), update 121 or later.

■ Cisco Voice Operating System (VOS) components:

— Cisco Unified Intelligence Center, Live Data, and Cisco Finesse, release 12.5(1) use OpenJDK JRE version 1.7 (32-bit), update 231 and OpenJDK JRE version 1.8 (64-bit), update 222. 12.5(2) installations support OpenJDK JRE version 1.8 (64-bit), update 262 and OpenJDK JRE version 1.8 (32-bit), update 282.

— Cisco VVB release 12.5(1) uses OpenJDK JRE version 1.7 (32-bit), update 231 and OpenJDK JRE version 11.0.2.7-0.el7_6 (64-bit). 12.5(2) installations support OpenJDK JRE version 1.8 (32-bit), update 262 and OpenJDK JRE version 11.0.16.0.8-1.el7_9 (64-bit).

■ For instructions on applying newer Java security updates, see Security Guide for Cisco Unified ICM/Contact Center Enterprise guide at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

## Supported Languages

Unified CCE Administration

Unified CCE Reporting Templates

Unified Intelligence Center

Finesse

Social Miner

Enterprise Chat and Email

CCMP/CCDM

Bulgarian

No

Yes

Yes

Yes

Yes

No

No

Catalan

No

Yes

Yes

Yes

Yes

No

No

Chinese (China)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Chinese (Taiwan)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Croatian

No

Yes

Yes

Yes

Yes

No

No

Czech

No

Yes

Yes

Yes

Yes

Yes

No

Danish

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Dutch

Yes

Yes

Yes

Yes

Yes

Yes

Yes

English (United States)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Finnish

No

Yes

Yes

Yes

Yes

No

No

French (France)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

French (Canada)

No

No

No

No

No

Yes

Yes

German

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Hungarian

No

Yes

Yes

Yes

Yes

No

No

Italian

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Japanese

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Korean

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Norwegian

No

Yes

Yes

Yes

Yes

No

No

Polish

No

Yes

Yes

Yes

Yes

Yes

No

Portuguese (Brazil)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Romanian

No

Yes

Yes

Yes

Yes

No

No

Russian

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Serbian

No

Yes

Yes

Yes

Yes

No

No

Slovenian

No

Yes

Yes

Yes

Yes

No

No

Slovakian

No

Yes

Yes

Yes

Yes

No

No

Spanish

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Swedish

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Turkish

No

Yes

Yes

Yes

Yes

No

Yes

## Microsoft .NET Framework

For release 12.5(1):

■ Microsoft Windows Server 2016 (Standard and Datacenter editions) comes with pre-installed .NET version 4.6.2.

■ Unified CCE and Administration client install .NET version 4.7.2, and CTI OS Client installs .NET version 4.7.1.

For release 12.5(2)

■ Microsoft Windows Server 2016 (Standard and Datacenter editions) comes with pre-installed .NET version 4.6.2.

■ Microsoft Windows Server 2019 (Standard and Datacenter editions) comes with pre-installed .NET version 4.7.2.

■ Unified CCE, Administration client, and CTI OS client install .NET version 4.8.

## Other Supported Software

Function

Software

Microsoft Active Directory

Microsoft Active Directory versions 2012 R2, 2016, 2019, and 2022 are supported with Unified ICM/Unified CCE, Packaged CCE and HCS for CC solutions.

Remote Administration

For Remote Desktop usage information, see the Remote Administration section in the Security Guide for Cisco Unified ICM/Contact Center Enterprise .

Antivirus Software

Cisco Contact Center Enterprise solution supports all the third-party antivirus software and scanners.

For more information, see the following documents:

■ General Antivirus Guidelines section in the Security Guide for Cisco Unified ICM/Contact Center Enterprise .

■ Cisco Customer Contact Software Policy for Use of Third-Party Software Bulletin

Virtualization

For more information about virtualization for all Unified CCE components, see the Unified Communications in a Virtualization page https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html .

Unified Intelligence Center reporting

Microsoft Excel Versions 2013, 2016, Office 365.

Note: Office 365 doesn’t support Authenticated excel report permalink.

## Virtual Desktop Infrastructure Support

■ Unified CCE, Packaged CCE and HCS for CC solutions support third-party VDI infrastructures for Cisco Finesse and CUIC. Ensure that your third-party VDI infrastructure is supported by Cisco softphone endpoints used on agent and supervisor VDI-based desktops.

■ Unified Communications Manager Silent Monitoring is the only silent monitoring type supported with VDI.

■ Desktop solutions are only supported on PC-like devices that utilize a keyboard and mouse. Tablets and mobile devices aren’t currently supported.

■ Verify that the bandwidth and deployment considerations of the solution meet the performance and timing requirements.

■ Cisco Unified Contact Center Enterprise Administration isn’t supported on virtual desktops.

## VMWare ESXI Compatibility

For information on the VMware ESXi versions compatible with Unified CCE solution components see Cisco Collaboration Virtualization at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html .

## Automatic Speech Recognition and Text to Speech

Note : Cisco does not test consecutive Nuance Service Packs and relies on Nuance to follow standard release practices and avoid making significant changes or updates in Service Pack releases. As Service Packs typically contain defect fixes, enhancements, and improvements, Nuance highly recommends keeping up to date with Service Packs and staying within a supported release according to their "On Premise Service Pack Deprecation and Support Policy." Nuance Support should be contacted should any issues arise with a Service Pack application, and a rollback plan be in place for any updates, as per industry best practices.

Category

Requirements

Nuance Speech Suite 11.0.x

Note: Cisco Virtualized Voice Browser (VVB) supports the Nuance components compatible with MRCP Protocol v1 and v2. For further details on the compatibility, see the Nuance Compatibility Matrix.

MRCP Protocol Version

v1 and v2

VoiceXML Protocol Version

2.0

## Load Balancers

These Cisco components support third-party load balancers in redirect mode.

■ Unified CCE

■ Unified CVP

■ Unified Intelligence Center

■ Finesse

■ Enterprise Chat and Email

Third-party load balancers must meet these requirements:

■ Both SSL offloading and SSL pass through must be supported

■ Load Balancer High Availability

■ Persistence - cookie-insert

■ Distribution algorithm - Round-robin

See these documents for the interoperability notes and any known caveats of F5 Big-IP and Citrix NetScalar 1000v:

■ https://www.cisco.com/c/dam/en/us/solutions/collateral/enterprise/interoperability-portal/bigip.pdf

■ https://www.cisco.com/c/dam/en/us/solutions/collateral/enterprise/interoperability-portal/interop-note-customer-voice-portal.pdf

Note: For specific interfaces where you can use load balancers in your deployment, see the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html .

## Non-Reference Design Compatibility

### Unified CCE Parent Child Compatibility

Parent PG 11.6(x)

Parent PG 12.0(x)

Parent PG 12.5(x)

Child PG 11.6(x)

Yes

Yes

Yes

Child PG 12.0(x)

Yes

Yes

Yes

Child PG 12.5(x)

Yes

Yes

Yes

### ICM-to-ICM Gateway Compatibility

ICM Client

ICM Server

12.5

12.5

12.5

12.0

12.5

11.6

12.0

12.5

11.6

12.5

### Third Party ACDs

#### Avaya

##### Avaya Considerations

■ Avaya changed names from DEFINITY to MultiVantage to Avaya Communications Manager (ACM) to Avaya Aura Communications Manager (AACM).

■ Cisco HCS for CC supports Avaya Peripheral Gateways.

■ Packaged CCE 12.5 and 12.0(1) ES26 (and above) versions support Avaya Peripheral Gateways for AACM in the 4000 and 12000 Agent deployments only.

■ Real-Time Agent (RTA) 5.0.5 and 6.0 enhanced functionality (60 skills per agent and 2000 skill groups per system) are not supported by ICM.

■ ICM does not support more than 12000 active associations on a single system.

■ All Call Management System (CMS) versions are supported as long as a supported RTA is used.

■ Cisco supports the Avaya S8300, S8400, S85XX, S87XX, and S88XX Servers in support of ACM.

■ Cisco supports the general use of Avaya IP Phones.

■ Although Avaya stopped supporting the CVLAN interface in 2012, Unified CCE still uses this interface to communicate with Avaya products. Note that 12.5(1) is the last supported release in the 12.5 release train for the CVLAN interface.

■ Avaya Multi-Application Platform for DEFINITY (MAPD) is not supported.

■ Support for third-party ACD clients, SDKs, and interfaces integrated with ICM stops when the third-party ACD manufacturer ends mainstream support.

■ Ten-digit Agent extensions and Agent IDs are supported from ICM 9.0(3) and later that have ACM 6.2 and later, AES 6.2 and later, and CMS R16 with RTA 6.0 pl: 13g.

##### Avaya CMS RTA Support

RTA Version

ICM/Packaged CCE 12.5

6.0(x)

Yes

6.0 Extended

No

##### Avaya Communications Manager (ACM) Support

ACM Version

ICM/Packaged CCE 12.5

ACM 6.3 (x) to 8.1 (x)

Yes

##### Notes on Avaya Communications Manager Support

Avaya Product Support Notice patch PSN020249u is required for ACM 7.0 (x) and above. For details, see the Product Support Notice at https://downloads.avaya.com/css/P8/documents/101020687 .

##### AES Server and CVLAN/TSAPI Client Support

AES Server

CVLAN Client Supported

TSAPI Client Supported

ICM/Packaged CCE 12.5

6.3 (x) to 8.1(x)

Yes

Yes [2]

Yes

2 Starting ICM Release 12.5(2), Cisco recommends that you install TSAPI client library version 10.1 on

the Avaya Peripheral Gateway machine as we have refreshed the TAESPIM using the TSAPI 10.1 SDK.

If you are on the ICM Release 12.5(1) or lower, you must install the TSAPI client library version that is the same as the AES server.

##### Notes on AES Server and CVLAN/TSAPI Client Support

ICM/Packaged CCE 12.5 supports all CVLAN Client and TSAPI Client versions currently supported by Avaya.

Note: Support for an ACM or AES version depends on the Avaya release cycles (patches and upgrades). For more details on supported versions, refer Avaya documentation. 12.5(1) is the last supported release in the 12.5 release train for the Unified ICM PG integration with Avaya Communications Manager using the ECS PIM / CVLAN interface PG. For more information, refer to the CVLAN to TSAPI Migration chapter in the Cisco Unified ICM ACD Supplement for Avaya Communication Manager , Release 12.5(1).

### Avaya Nortel

##### Note Starting CCE release 12.5(2), the Avaya Nortel is not supported.

These notes apply to the support of Avaya/Nortel's ACD switch types:

■ Cisco only supports certain Succession platforms with Symposium. See the following chart for details.

■ Cisco does not support more than one PG pair connected to a single Symposium server.

■ You must request the SCCS Toolkit from Cisco. To do so, send an email with the following information to icm-nortelpg-sdk@cisco.com :

— Customer name

— Maintenance contract number

— ICM version

— PG version

— Number of PGs

### Avaya Aura Contact Center

AACC Version

ICM 12.5

6

Yes

6.4

Yes

7.1

Yes

##### Notes to Avaya Aura Contact Center

The Automated Administrator for Symposium (AAS) feature is not supported with AACC 6.4.

### Nortel SDK

ACD Version

ICM 12.5

Notes

Nortel SDK 5.0 (with SCCS 5.0 and NCCM 6.0)

No

As of September 2008, Nortel does not provide support for SCCS 5.0.

Nortel SDK 6.0 (with NCCM 6.0, NCCM 7.0 and AACC 6.0)

Yes

For HDX 6, you must install RTD 6 on the PG.

Note: SDKs are not integrated with ICM.

##### Notes to Nortel SDK

■ Cisco does not support any major ACD version not shown in this matrix.

■ Nortel Contact Center Manager (NCCM), earlier known as Symposium (SCCS), was renamed to Avaya Aura Contact Center (AACC).

##### CTI Support for ACD Types

ACD Vendor

ACD Model

CTI Server Protocol Support

CTI OS Support

Avaya

Avaya Communication Manager v6.3 to v8.1

Yes

Yes

Cisco

Unified CCE (only when integrated via Unified CCE System PG)

Yes

Yes

## Legal Information (software documentation only)

THE SPECIFICATIONS AND INFORMATION REGARDING THE PRODUCTS IN THIS MANUAL ARE SUBJECT TO CHANGE WITHOUT NOTICE. ALL STATEMENTS, INFORMATION, AND RECOMMENDATIONS IN THIS MANUAL ARE BELIEVED TO BE ACCURATE BUT ARE PRESENTED WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. USERS MUST TAKE FULL RESPONSIBILITY FOR THEIR APPLICATION OF ANY PRODUCTS.

THE SOFTWARE LICENSE AND LIMITED WARRANTY FOR THE ACCOMPANYING PRODUCT ARE SET FORTH IN THE INFORMATION PACKET THAT SHIPPED WITH THE PRODUCT AND ARE INCORPORATED HEREIN BY THIS REFERENCE. IF YOU ARE UNABLE TO LOCATE THE SOFTWARE LICENSE OR LIMITED WARRANTY, CONTACT YOUR CISCO REPRESENTATIVE FOR A COPY.

The Cisco implementation of TCP header compression is an adaptation of a program developed by the University of California, Berkeley (UCB) as part of UCB’s public domain version of the UNIX operating system. All rights reserved. Copyright © 1981, Regents of the University of California.

NOTWITHSTANDING ANY OTHER WARRANTY HEREIN, ALL DOCUMENT FILES AND SOFTWARE OF THESE SUPPLIERS ARE PROVIDED “AS IS” WITH ALL FAULTS. CISCO AND THE ABOVE-NAMED SUPPLIERS DISCLAIM ALL WARRANTIES, EXPRESSED OR IMPLIED, INCLUDING, WITHOUT LIMITATION, THOSE OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OR ARISING FROM A COURSE OF DEALING, USAGE, OR TRADE PRACTICE.

IN NO EVENT SHALL CISCO OR ITS SUPPLIERS BE LIABLE FOR ANY INDIRECT, SPECIAL, CONSEQUENTIAL, OR INCIDENTAL DAMAGES, INCLUDING, WITHOUT LIMITATION, LOST PROFITS OR LOSS OR DAMAGE TO DATA ARISING OUT OF THE USE OR INABILITY TO USE THIS MANUAL, EVEN IF CISCO OR ITS SUPPLIERS HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

Any Internet Protocol (IP) addresses and phone numbers used in this document are not intended to be actual addresses and phone numbers. Any examples, command display output, network topology diagrams, and other figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses or phone numbers in illustrative content is unintentional and coincidental.

All printed copies and duplicate soft copies are considered un-Controlled copies and the original on-line version should be referred to for latest version.

Cisco has more than 200 offices worldwide. Addresses, phone numbers, and fax numbers are listed on the Cisco website at www.cisco.com/go/offices .

## Cisco Trademark (all documentation)

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1110R)

## Cisco Copyright (all documentation)

© 2024 Cisco Systems, Inc. All rights reserved.

[1] For more information, check the Release Notes at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html .

[2] Starting ICM Release 12.5(2), Cisco recommends that you install TSAPI client library version 10.1 on the Avaya Peripheral Gateway machine as we have refreshed the TAESPIM using the TSAPI 10.1 SDK. If you are on the ICM Release 12.5(1) or lower, you must install the TSAPI client library version that is the same as the AES server.

| PCCE/UCCE Components, Release 12.5(x) | PCCE/UCCE/HCS for CC components, Release 12.0 |
|---|---|
| IdS (Standalone) | Finesse | ECE | CVP | VVB | CUIC (Standalone) | CUIC-LiveData-IdS (Coresident) | Router | Logger | AW | Live Data (Standalone) | PG | SocialMiner | CCMP/CCDM | Notes |
| Router |  |  |  | N |  |  | N |  |  |  | N | Y | Y | N |  |
| Logger |  |  |  | N |  |  |  |  |  |  |  | Y | Y | N |  |
| AW | N | N | N | N |  | N | N |  |  |  | N | Y | Y | N |  |
| Live Data (Standalone) |  | N |  |  |  | N |  | N |  | N |  | Y |  |  |  |
| PG |  | N | N | N |  |  | N | N | N | N | N |  |  |  |  |

| PCCE/UCCE/HCS for CC Components, Release 12.5(1) | PCCE/UCCE/HCS for CC Components, Release 12.0 |
|---|---|
| IdS (Standalone) | Finesse | ECE | CVP | VVB | CUIC (Standalone) | CUIC-LiveData-IdS (Coresident) | Router | Logger | AW | Live Data (Standalone) | PG | SocialMiner | CCMP/ CCDM | Notes |
| Identity Server (Standalone) |  | Y | Y |  |  | Y |  |  |  | Y |  |  |  |  |  |
| Finesse | N |  | N |  |  | Y | N |  |  | Y | Y | Y | Y |  | For Live data gadgets to load in Cisco Finesse, install CUIC 12.0(1) ES 06 or later on Live Data (Standalone) server. See Notes for more information. |
| ECE | N | Y |  |  |  |  |  |  |  | Y |  | Y |  |  |  |
| CVP |  |  |  |  | Y |  |  | Y | Y | Y |  | Y |  |  | On PCCE 12.0, install CCE 12.0 ES37 before you upgrade CVP to 12.5(1). |
| VVB |  |  |  | Y |  |  |  |  |  |  |  |  |  |  |  |
| CUIC (Standalone) | N | N |  |  |  |  |  |  |  | Y | Y |  |  |  |  |
| CUIC-LiveData-IdS (Coresident) |  | N |  |  |  |  |  | N |  | N |  | Y |  |  |  |
| Customer Collaboration Platform |  | N |  |  |  |  |  |  |  |  |  |  |  |  |  |
| CCMP |  |  |  | Y |  |  |  | Y | Y | Y |  |  |  |  | Not Applicable to Packaged CCE. |
| CCDM |  |  |  | Y |  |  |  | Y | Y | Y |  |  |  |  | Applicable only to HCS for CC. |

| Unified CCE/HCS for CC Components, Release 12.5(x) | Unified CCE/HCS for CC Components, Release 11.6 |
|---|---|
| IdS (Standalone) | Finesse | ECE | CVP | VVB | CUIC (Standalone) | CUIC-LiveData-IdS (Coresident) | Router | Logger | AW | Live Data (Standalone) | PG | SocialMiner | CCMP/ CCDM | Notes |
| Router |  |  |  | N |  |  | N |  |  |  | N | Y | Y | N |  |
| Logger |  |  |  | N |  |  |  |  |  |  |  | Y | Y | N |  |
| AW | N | N | N | N |  | N | N |  |  |  | N | Y | Y | N |  |
| Live Data (Standalone) |  | N |  |  |  | N |  | N |  | N |  | Y |  |  | 24000 Agent Deployment is not supported with PG 11.6. |
| PG |  | N | N | N |  |  | N | N | N | N | N |  |  |  |  |

| Unified CCE/HCS for CC Components, Release 12.5(1) | Unified CCE/HCS for CC Components, Release 11.6 |
|---|---|
| IdS (Standalone) | Finesse | ECE | CVP | VVB | CUIC (Standalone) | CUIC-LiveData-IdS (Coresident) | Router | Logger | AW | Live Data (Standalone) | PG | SocialMiner | CCMP/ CCDM | Notes |
| Identity Server (Standalone) |  | Y | Y |  |  | Y |  |  |  | Y |  |  |  |  |  |
| Finesse | N |  | N |  |  | Y | N |  |  | Y | Y | Y | Y |  | For Live data gadgets to load in Cisco Finesse, ensure to install CUIC 11.6(1) ES18 or later on Live Data (Standalone) server. See Notes for more information. |
| ECE | N | Y |  |  |  |  |  |  |  | Y |  | Y |  |  | ECE 12.5 is not compatible with Packaged CCE 11.6. |
| CVP |  |  |  |  | Y |  |  | Y | Y | Y |  | Y |  |  |  |
| VVB |  |  |  | Y |  |  |  |  |  |  |  |  |  |  |  |
| CUIC (Standalone) | N | N |  |  |  |  |  |  |  | Y | Y |  |  |  |  |
| CUIC-LiveData-IdS (Coresident) |  | N |  |  |  |  |  | N |  | N |  | Y |  |  |  |
| Customer Collaboration Platform |  | N |  |  |  |  |  |  |  |  |  |  |  |  |  |
| CCMP |  |  |  | Y |  |  |  | Y | Y | Y |  |  |  |  | CCMP is not applicable to Packaged CCE. On UCCE and HCS for CC 11.6, install UCCE 11.6(1) ES 7 before you upgrade CCMP to 12.5(1). |
| CCDM |  |  |  | Y |  |  |  | Y | Y | Y |  |  |  |  | CCDM is applicable only to HCS for CC. On HCS for CC 11.6, install UCCE 11.6(1) ES 7 before you upgrade CCDM to 12.5(1). |

|  | Gateway Functionality |  |
|---|---|---|
| Central Controller version 12.5(x) Model | Software Version | Software Feature Set | VXML Gateway Browser | Call Progress Analysis for Outbound Options for SIP Trunks (CUBE) | Unified CCE, Packaged CCE, And Cisco HCS for CC Support |
| ASR 1001X ASR 1002X ASR 1004 RP2 ASR 1006 RP2 | IOS XE 16.6 | Universal | No | Yes | Yes |
| IOS XE 16.9 |
| IOS XE 16.12 |
| IOS XE 17.2 |
| IOS XE 17.6 |
| IOS XE 17.9 |
| Virtual CUBE | IOS XE 16.6 | Universal | No | No | Yes |
| IOS XE 16.9 |
| IOS XE 16.12 |
| IOS XE 17.2 |
| IOS XE 17.6 |
| IOS XE 17.9 |
| 15.7(3)M1 |
| ISR G3 43xx (4321, 4331, 4351) ISR G3 44xx (4431, 4451, 4461) | IOS XE 16.6 | Universal | No | Yes | Yes |
| IOS XE 16.9 |
| IOS XE 16.12 |
| IOS XE 17.2 |
| IOS XE 17.6 |
| IOS XE 17.9 |
| Catalyst 8200/8300 | IOS XE 17.6 | Universal | No | Yes | Yes |
| IOS XE 17.9 |

| Endpoint | Voice & Finesse Desktop | Video | Unified CM Silent Monitor | BIB-based recording | Agent Greeting | Whisper Announcements | Finesse IP Agent Phone | IPv6 SCCP (UCCE Only) | IPv6 SIP | MRA |
|---|---|---|---|---|---|---|---|---|---|---|
| 7821, 7841, 7861 | Y | N | Y | Y | Y | Y | Y | N | Y | Yes Audio Only |
| 7942G,7945G, 7962G,7965G, 7975G | Y | N | Y | Y | Y | Y | N | Y | N | N |
| 8811, 8821, 8841, 8851, 8851NR, 8861 | Y | N | Y | Y | Y | Y | Y | N | Y | Yes Audio Only |
| 8845, 8865 | Y | Y | Y | Y | Y | Y | Y | Y | Y | Yes Audio Only |
| 9841, 9851, 9861, 9871 | Y | N | Y | Y | Y | Y | N | N | Y | Yes Audio only |
| EX60 | Y | Y | N | N | N | N | N | N | Y | N |
| Jabber for Mac | Y | Y | Voice only | Y | N | Y | N | N | N | Y |
| Jabber for VDI | Y | N | N | Y | Y | Y | N | N | N | Y |
| Jabber for Windows | Y | Y | Voice-only | Y | Y | Y | N | N | N | Y |
| Webex App for MacOS/Windows | Y | Y | Y | Y | Y | Y | N | N | Y | Y |
| Webex App for VDI | Y | Y | Y | Y | Y | Y | N | N | N | Y |
| MX300 G2, MX700, MX800 Telepresence | Y | Y | N | N | N | N | N | N | Y | N |
| SX10, SX20, SX80 Telepresence | Y | Y | N | N | N | N | N | N | Y | N |

| Identity Providers | Versions |
|---|---|
| Microsoft AD FS (Active Directory Federation Services) | AD FS 5.0: Windows Server 2019 AD FS 4.0: Windows Server 2016 AD FS 3.0: Windows Server 2012 R2 |
| PingFederate | 8.2.2.0 |
| OpenAM | 10.0.1 |
| Shibboleth | 3.3.0 |
| F5 | 13 |

| 12.5 Component | TLS 1.2 |
|---|---|
| Web Interfaces | Database Access |
| PCCE | ✔ | ✔ |
| UCCE/ICM | ✔ | ✔ |
| AW Distributor/HDS/Logger | N/A | ✔ |
| Internet Script Editor | ✔ | N/A |
| CCE Admin | ✔ | ✔ |
| Web Setup | ✔ | ✔ |
| Diagnostic Portal | ✔ | N/A |
| Live Data | ✔ | ✔ |
| CTIOS C++ CIL | ✔ | N/A |
| SQL Gateway - DB Lookup | N/A | ✔ |
| Protocol - CTI Server and Media Routing | N/A | ✔ |
| CVP [1] | ✔ | N/A |
| VVB | ✔ | N/A |
| IdS | ✔ | N/A |
| Finesse | ✔ | ✔ |
| CUIC | ✔ | ✔ |
| ECE | ✔ | ✔ |
| Live Data | ✔ | N/A |
| Customer Collaboration Platform | ✔ | N/A |
| CCMP/CCDM | ✔ | X |
| ACD | X | N/A |
| UC Manager | ✔ | N/A |

| Components | Clients OS |
|---|---|
| Cisco Finesse | Microsoft Windows 11 (64 bit) Microsoft Windows 10 Note: CCE Release 12.5(1) supports Microsoft Windows 10 only. CCE Release 12.5(2) supports Microsoft Windows 10 and Windows 11 (64 bit). |
| Mac OS X 10.12, 10.13 and10.14 |
| ChromeOS 70 (64-bit) and higher |
| Cisco Unified Call Studio | Microsoft Windows 10 (64-bit) |
| Administration Client | Microsoft Windows Server 2016 and 2019 (Standard and Datacenter editions) Note: CCE Release 12.5(1) supports Microsoft Windows Server 2016 only. CCE Release 12.5(2) supports Microsoft Windows Server 2016 and 2019. |
| Microsoft Windows 10 (Enterprise and Professional) Microsoft Windows 11 (Enterprise and Professional) (64-bit) |
| Internet Script Editor (ISE) | Microsoft Windows 10 (Enterprise and Professional) Microsoft Windows 11 (Enterprise and Professional) (64-bit) |
| Silent Monitor Service for Unified CCE Toolkit | Microsoft Windows 10 (Enterprise and Professional) |
| CTI OS Clients | Microsoft Windows 10 (Enterprise and Professional) Note: For more information on the supported versions of Microsoft Windows 10 with specific versions of .NET Framework, see the Microsoft documentation. |

| Operating System | Browser Version |
|---|---|
| Microsoft Windows Server 2016 (Standard and Datacenter editions) Microsoft Windows Server 2019 (Standard and Datacenter editions) | Internet Explorer v11.3085.14393.0 or later in Native Mode |
| Chrome v76.0.3809 or later |
| Firefox Extended Supported Release (ESR) 68 and later ESRs |
| Edge Chromium (Microsoft Edge v79 and later) |
| Microsoft Windows 10 and Windows 11 (64 bit) Note: CCE Release 12.5(1) supports Microsoft Windows 10 only. CCE Release 12.5(2) supports Microsoft Windows 10 and Windows 11 (64 bit). | Internet Explorer v11.345.17134 or later in Native Mode |
| Google Chrome v76.0.3809 or later |
| Firefox ESR 68 and later ESRs |
| Edge Chromium (Microsoft Edge v79 and later) |
| Mac OS X | Firefox ESR 68 and later ESRs |
| Google Chrome v76.0.3809 or later |
| Chromebook with Chrome OS v70 | Chromium v73 or later |
| Google Chrome v60 or later |

| Components | Server OS |
|---|---|
| Unified CCE, Packaged CCE, ICM, and System PG | Microsoft Windows Server 2016 and 2019 (Standard and Datacenter editions) |
| Unified CVP | Microsoft Windows Server 2016 and 2019 (Standard and Datacenter editions) |
| Enterprise Chat and Email | Microsoft Windows Server 2019 (Standard and Datacenter editions) |
| Unified CCMP | Microsoft Windows Server 2019 (Standard and Datacenter editions) |
| Silent Monitor Server | Microsoft Windows Server 2016 and 2019 (Standard and Datacenter editions) |
| CTI OS Server | Microsoft Windows Server 2016 and 2019 (Standard and Datacenter editions) |

| Components | SQL Server Version |
|---|---|
| Unified CCE, Packaged CCE, and ICM | Microsoft SQL Server 2017 (Standard and Enterprise editions) with cumulative updates Microsoft SQL Server 2019 (Standard and Enterprise editions) with cumulative updates Note: Microsoft SQL Server 2019 with native compatibility level 150 and backward compatibility level 140 of Microsoft SQL Server 2017 is supported. Note: Contact Center Enterprise solution supports only the 64-bit version of Microsoft SQL Server. Contact Center Enterprise solution does not support the following: ■ Encrypted connections to SQL Server. ■ Linked Server feature of SQL Server. |
| Unified CVP | IBM Informix Dynamic Server Version 14.10.FC8 |
| Enterprise Chat and Email | ■ ECE 400 agent deployment: Microsoft SQL Server 2016 SP2 (Standard and Enterprise editions) ■ ECE 1500 agent deployment: Microsoft SQL Server 2016 SP2 (Standard and Enterprise editions) ■ ECE Geographically Redundant/High Availability installation: Microsoft SQL Server 2016 (Enterprise edition) |
| Unified CCMP | Microsoft SQL Server 2016 SP2 (Standard edition) |
| Unified CCDM | Microsoft SQL Server 2016 SP2 (Standard edition) |

|  | Unified CCE Administration | Unified CCE Reporting Templates | Unified Intelligence Center | Finesse | Social Miner | Enterprise Chat and Email | CCMP/CCDM |
|---|---|---|---|---|---|---|---|
| Bulgarian | No | Yes | Yes | Yes | Yes | No | No |
| Catalan | No | Yes | Yes | Yes | Yes | No | No |
| Chinese (China) | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Chinese (Taiwan) | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Croatian | No | Yes | Yes | Yes | Yes | No | No |
| Czech | No | Yes | Yes | Yes | Yes | Yes | No |
| Danish | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Dutch | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| English (United States) | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Finnish | No | Yes | Yes | Yes | Yes | No | No |
| French (France) | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| French (Canada) | No | No | No | No | No | Yes | Yes |
| German | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Hungarian | No | Yes | Yes | Yes | Yes | No | No |
| Italian | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Japanese | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Korean | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Norwegian | No | Yes | Yes | Yes | Yes | No | No |
| Polish | No | Yes | Yes | Yes | Yes | Yes | No |
| Portuguese (Brazil) | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Romanian | No | Yes | Yes | Yes | Yes | No | No |
| Russian | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Serbian | No | Yes | Yes | Yes | Yes | No | No |
| Slovenian | No | Yes | Yes | Yes | Yes | No | No |
| Slovakian | No | Yes | Yes | Yes | Yes | No | No |
| Spanish | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Swedish | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Turkish | No | Yes | Yes | Yes | Yes | No | Yes |

| Function | Software |
|---|---|
| Microsoft Active Directory | Microsoft Active Directory versions 2012 R2, 2016, 2019, and 2022 are supported with Unified ICM/Unified CCE, Packaged CCE and HCS for CC solutions. |
| Remote Administration | For Remote Desktop usage information, see the Remote Administration section in the Security Guide for Cisco Unified ICM/Contact Center Enterprise . |
| Antivirus Software | Cisco Contact Center Enterprise solution supports all the third-party antivirus software and scanners. For more information, see the following documents: ■ General Antivirus Guidelines section in the Security Guide for Cisco Unified ICM/Contact Center Enterprise . ■ Cisco Customer Contact Software Policy for Use of Third-Party Software Bulletin |
| Virtualization | For more information about virtualization for all Unified CCE components, see the Unified Communications in a Virtualization page https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html . |
| Unified Intelligence Center reporting | Microsoft Excel Versions 2013, 2016, Office 365. Note: Office 365 doesn’t support Authenticated excel report permalink. |

| Category | Requirements |
|---|---|
| Nuance Speech Suite 11.0.x | Note: Cisco Virtualized Voice Browser (VVB) supports the Nuance components compatible with MRCP Protocol v1 and v2. For further details on the compatibility, see the Nuance Compatibility Matrix. |
| MRCP Protocol Version | v1 and v2 |
| VoiceXML Protocol Version | 2.0 |

|  | Parent PG 11.6(x) | Parent PG 12.0(x) | Parent PG 12.5(x) |
|---|---|---|---|
| Child PG 11.6(x) | Yes | Yes | Yes |
| Child PG 12.0(x) | Yes | Yes | Yes |
| Child PG 12.5(x) | Yes | Yes | Yes |

| ICM Client | ICM Server |
|---|---|
| 12.5 | 12.5 |
| 12.5 | 12.0 |
| 12.5 | 11.6 |
| 12.0 | 12.5 |
| 11.6 | 12.5 |

| RTA Version | ICM/Packaged CCE 12.5 |
|---|---|
| 6.0(x) | Yes |
| 6.0 Extended | No |

| ACM Version | ICM/Packaged CCE 12.5 |
|---|---|
| ACM 6.3 (x) to 8.1 (x) | Yes |

| AES Server | CVLAN Client Supported | TSAPI Client Supported | ICM/Packaged CCE 12.5 |
|---|---|---|---|
| 6.3 (x) to 8.1(x) | Yes | Yes [2] | Yes |

| AACC Version | ICM 12.5 |
|---|---|
| 6 | Yes |
| 6.4 | Yes |
| 7.1 | Yes |

| ACD Version | ICM 12.5 | Notes |
|---|---|---|
| Nortel SDK 5.0 (with SCCS 5.0 and NCCM 6.0) | No | As of September 2008, Nortel does not provide support for SCCS 5.0. |
| Nortel SDK 6.0 (with NCCM 6.0, NCCM 7.0 and AACC 6.0) | Yes | For HDX 6, you must install RTD 6 on the PG. |
| Note: SDKs are not integrated with ICM. |

| ACD Vendor | ACD Model | CTI Server Protocol Support | CTI OS Support |
|---|---|---|---|
| Avaya | Avaya Communication Manager v6.3 to v8.1 | Yes | Yes |
| Cisco | Unified CCE (only when integrated via Unified CCE System PG) | Yes | Yes |