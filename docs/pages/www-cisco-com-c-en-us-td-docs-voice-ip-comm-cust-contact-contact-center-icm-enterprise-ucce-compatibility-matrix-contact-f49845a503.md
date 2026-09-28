---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-ucce-compatibility-matrix-contact-f49845a503
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/ucce_compatibility/matrix/Contact_Center_Enterprise_Solution_Compatibility_Matrix_Release_12_6.html
retrieved_at: 2026-08-16T14:54:13.045260+00:00
---

Contact Center Enterprise Solution Compatibility Matrix, Release 12.6(x)

# Contact Center Enterprise Solution Compatibility Matrix, Release 12.6(x)

### Download Options

Updated: May 16, 2024

Contact Center Enterprise Solution Compatibility Matrix, Release 12.6(x)

First Published : 2021-05-14

NOTE: Works with document’s Advanced Properties “First Published” property. Click File | Properties | Advanced Properties | Custom .

Last Updated: 2026-03-17

Americas Headquarters

Cisco Systems, Inc.

170 West Tasman Drive

San Jose, CA 95134-1706 USA

http://www.cisco.com Tel: 408 526-4000

800 553-NETS (6387) Fax: 408 527-0883

Contents

Overview .. 4

Central Controller and Component Compatibility . 5

Cisco Gateway Hardware and Software . 10

IOS Versioning Key 16.1(4) M3 and 16.1(4) T1 as Examples . 14

IOS-XE Versioning Key 16.12.1a and 16.12.3 as Examples . 14

Cisco Unified SIP Proxy (Deprecated) 14

Cisco Contact Center SIP Proxy . 15

Third-party SIP Proxy . 15

End Points for Agents and Callers . 15

Endpoints Supported for Callers Only . 18

Single Sign On (SSO) Identity Providers (IdPs) 18

Transport Layer Security . 18

Client Operating System .. 20

Supported Browsers . 22

Server Operating System .. 22

SQL Server and Informix Versions . 24

Microsoft Windows and Microsoft SQL Server Localization Support 25

JDK and JRE . 26

Supported Languages . 27

Microsoft .NET Framework . 29

Other Supported Software . 29

Virtual Desktop Infrastructure Support 30

VMWare ESXI Compatibility . 30

Automatic Speech Recognition and Text to Speech . 31

Load Balancers . 31

Non-Reference Design Compatibility . 32

Unified CCE Parent Child Compatibility . 32

ICM-to-ICM Gateway Compatibility . 32

Third Party ACDs . 33

Avaya . 33

Legal Information (software documentation only) 36

Cisco Trademark (all documentation) 37

Cisco Copyright (all documentation) 37

## Overview

The Contact Center Enterprise (CCE) Solution Compatibility Matrix includes all the Cisco CCE solutions and component compatibility information. This compatibility matrix specifies all supported configurations and versions for Release 12.6(x), which includes the maintenance or ES releases of 12.6(x). The information in this compatibility matrix supersedes compatibility information in any other CCE documentation. If the Compatibility Matrix does not state a configuration or version, then it does not support it.

■ Make sure that your Router, Logger, and AW are in the same version as your PG or in a version that is higher than your PG.

■ The Compatibility Matrix specifies all supported third-party software (such as Nuance and Informix) and its versions. Support for these software versions and their interoperability depends on the release cycles (patches and upgrades) of the third-party software. For example, support for ESXi depends on VMware release cycles.

■ Packaged CCE: In Release 12.6(x), the multistage upgrade support is backward compatible with Release 12.0 only. For all releases prior to 12.0, all components must be on the same release.

Exception: Cisco Unified CM (CUCM) can continue to be on an earlier compatible release for an off-box solution deployment.

■ Support for a CUCM release is inclusive of all updates.

■ For details on the browsers and the languages that are supported by Cisco Webex Experience Management, see Experience Management.

■ Upgrade all the solution components to experience the new features delivered as part of a particular solution release version. Upgrading only the component that delivers the new feature may not be sufficient in all cases. For more information on upgrade paths, see the CCE Upgrade Flowcharts in the respective Contact Center Enterprise Installation and Upgrade Guides.

■ IP IVR 12.5(1), IP IVR 12.5(1) SU1, IP IVR 12.5(1) SU2, and IP IVR 12.5(1) SU3 are compatible with CCE 12.6(x).

■ Live Data 12.6(2) requires CUIC to be on the version 12.6(2) and beyond.

## Central Controller and Component Compatibility

PCCE/UCCE Components, Release 12.6(x)

PCCE/UCCE Components, Release 12.5

Cloud Connect

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

Customer Collaboration Platform

CCMP

Notes

Cloud Connect

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

Identity Server (Standalone)

N

Y

Y

Y

Y

Finesse

N

N

Y

Y

N

Y

Y

Y

Y

When Cisco Finesse and CUIC are on 12.6, and Live Data is on 12.5, for Live Data gadgets to load in Cisco Finesse, install CUIC 12.5(1) ES 09 or later on all Live Data stand-alone servers.

CVP

N

Y

Y

Y

Y

Y

VVB

N

Y

CUIC (Standalone)

N

N

N

Y

Y

CUIC-LiveData-IdS (Coresident)

N

N

N

N

Y

Router

N

N

N

N

Y

Y

N

Logger

N

N

Y

Y

N

AW

N

N

N

Y

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

N

Y

PG

N

N

Y

N

N

N

N

N

N

Y

Upgrade CCP to 12.5(1) SU1 for compatibility with CCE 12.6.

PCCE/UCCE Components, Release 12.6(1)

PCCE/UCCE, Release 12.5

Cloud Connect

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

Customer Collaboration Platform

CCMP

Notes

ECE

N

Y

Y

Y

CCMP

Y

Y

Y

Y

Not Applicable to Packaged CCE.

PCCE/UCCE Components, Release 12.6(x)

PCCE/UCCE, Release 12.0

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

CCMP

Notes

Cloud Connect

N

N

N

N

N

N

N

N

N

N

N

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

When Cisco Finesse and CUIC are on 12.6, and Live Data is on 12.0, for Live Data gadgets to load in Cisco Finesse, install CUIC 12.0(1) ES 15 or later on all Live Data stand-alone servers.

CVP

Y

Y

Y

Y

Y

On Packaged CCE 12.0, install CCE 12.0 ES37 before you upgrade CVP to 12.6(1).

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

N

PCCE/UCCE Components, Release 12.6(1)

PCCE/UCCE, Release 12.0

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

CCMP

Notes

ECE

N

Y

Y

Y

CCMP

Y

Y

Y

Y

Not Applicable to Packaged CCE.

Unified CCE Components, Release 12.6(1)

Unified CCE, Release 11.6

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

CCMP

Notes

Cloud Connect

N

N

N

N

N

N

N

N

N

N

N

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

When Cisco Finesse and CUIC are on 12.6, and Live Data is on 11.6, for Live Data gadgets to load in Cisco Finesse, install CUIC 11.6(1) ES 22 or later on all Live Data stand-alone servers.

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

N

CCMP

Y

Y

Y

Y

CCMP is not applicable to Packaged CCE.

On UCCE 11.6, install UCCE 11.6(1) ES 7 or 11.6(2) before you upgrade CCMP to 12.5(1).

Notes

■ Unified CCE and Packaged CCE compatibility with CUCM:

— CUCM, releases 11.5, 12.0, 12.5 and 14 are supported with Unified CCE and Packaged CCE, Release 12.6.

— CUCM 15 is supported with Unified CCE, Release 12.6(1) and 12.6(2). CUCM 15 is supported with Packaged CCE Release 12.6(2) if CCE 12.6(2) ES 27 is installed.

■ Cisco Unified Contact Center Management Portal (CCMP) compatibility with CUCM:

— CUCM 11.5, 12.0, 12.5 and 14 are supported with CCMP, Release 12.6.

— CUCM 15 is supported with CCMP, Release 12.6 if CCMP 12.6(1) ES 12 is installed.

■ CCE 12.6 supports the latest versions of Cisco Smart Software Manager (CSSM) On-Prem 8.x.

■ PCCE 12.5 (2) is compatible with CVP 12.6 (x). To use CVP 12.6 (x) with PCCE 12.5(1), install the CCE 12.5(1) ES 144 .

■ In Live Data (standalone) 11.6 and 12.0 deployments, when CUIC and Cisco Finesse components are in version 12.6, Live Data gadgets will not load in Cisco Finesse. You must enable Cross-Origin Resource Sharing (CORS) and set Finesse host URLs to load the Live Data gadgets.

■ SSO Deployments upgrading to 12.6(2) should ensure that Reverse Proxy Installer (for VPN-Less deployments) 12.6(2) ES02 or later, followed by IdS 12.6(2) ES02 or later, is installed before upgrading any of the components like Cisco Finesse/CUIC to 12.6.(2).

■ You can use VPNLess Finesse in a 2000 Agent Deployment with LiveData 12.6(2) in one of the following ways:

■ Install LiveData 12.6(2) and operate it on a single port (443). It is important to note that in this scenario, you need to upgrade all Central Controller components to 12.6(2).

■ Use LiveData 12.6(1) template in VPNLess installer to configure and operate LiveData on a dual port. In this scenario, LiveData is compatible with the 12.6(1) Central Controller components.

■ For 2000 Agent Coresident Deployment model, CUIC, LD, and Unified CCE (Router, Logger, and AW) should be upgraded in the same maintenance window.

■ For SSO clients, Cisco IDS needs to be on version 12.6(2) as there is no forward compatibility with Cisco IDS version 12.6(1) and 12.6(2) clients.

■ For more information on CORS CLIs, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

■ For Unified CCE and Packaged CCE, Release 11.6, the last date of support is 30 September, 2023. The Unified CCE and Packaged CCE, Release 12.6(1) compatibility with Release 11.6 will be removed from 30 September, 2023. For more information about end of life milestones, see End-of-Sale and End-of-Life Announcement for the Cisco Unified Contact Center Enterprise, Cisco Packaged Contact Center Enterprise, Cisco Unified Intelligent Contact Management Enterprise, and Cisco HCS for Contact Center 11.6 .

■ To find a comprehensive list of the guides available for a specific release, see the Documentation Guides .

## Cisco Gateway Hardware and Software

Gateway Functionality

Central Controller version 12.6(2) Model

Software Version

VXML Gateway Browser

Call Progress Analysis for Outbound Options for SIP Trunks (CUBE)

Unified CCE and Packaged CCE Support

ASR 1001X

ASR 1002X

ASR 1004 RP2

ASR 1006 RP2

IOS XE 17.2

No

Yes

Yes

IOS XE 17.4

IOS XE 17.6

IOS XE 17.9

IOS XE 17.12

IOS XE 17.15

IOS XE 17.18

Virtual CUBE

IOS XE 17.6

No

No

Yes

IOS XE 17.9

IOS XE 17.12

IOS XE 17.15

IOS XE 17.18

ISR G3 43xx (4321, 4331, 4351)

ISR G3 44xx (4431, 4451, 4461)

IOS XE 17.6

No

Yes

Yes

IOS XE 17.9

IOS XE 17.12

IOS XE 17.15

IOS XE 17.18

Catalyst 8200/8300

IOS XE 17.6

No

Yes

Yes

IOS XE 17.9

IOS XE 17.12

IOS XE 17.15

IOS XE 17.18

Gateway Functionality

Central Controller version 12.6(1) Model

Software Version

VXML Gateway Browser

Call Progress Analysis for Outbound Options for SIP Trunks (CUBE)

Unified CCE and Packaged CCE Support

ASR 1001X

ASR 1002X

ASR 1004 RP2

ASR 1006 RP2

IOS XE 17.2

No

Yes

Yes

IOS XE 17.4

IOS XE 17.6

IOS XE 17.9

Virtual CUBE

IOS XE 17.2

No

No

Yes

IOS XE 17.4

IOS XE 17.6

IOS XE 17.9

IOS XE 17.15

ISR G3 43xx (4321, 4331, 4351)

ISR G3 44xx (4431, 4451, 4461)

IOS XE 17.2

No

Yes

Yes

IOS XE 17.4

IOS XE 17.6

IOS XE 17.9

Catalyst 8200/8300

IOS XE 17.6

No

Yes

Yes

IOS XE 17.9

IOS XE 17.15

Notes

■ Virtual CUBE (vCUBE) can run either on Cisco Cloud Services Router (CSR) 1000V (if you use IOS XE 16.9, 16.12, or 17.2) or Cisco Catalyst 8000V Edge Software (if you use IOS XE 17.4 or 17.6).

■ All gateways in the preceding table support inbound contact center calls. For details on support for Call Progress Analysis (CPA) for Outbound Option with TDM Trunks, see the Cisco ASR 1000 Series documentation at https://www.cisco.com/c/en/us/support/routers/asr-1000-series-aggregation-services-routers/products-documentation-roadmaps-list.html

■ For IPv6-enabled deployments, the supported IOS versions for NAT64 translations are 15.4(2)T3 and later releases.

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

Unified CCE and Packaged CCE 12.6(x) solutions support Cisco Unified SIP Proxy (CUSP) 10.1(x) and 10.2(x) only in non-secure mode.

Notes: CUSP is deprecated. For more information, see End-of-Sale and End-of-Life Announcement for the Cisco Unified SIP Proxy Version 10 at https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-sip-proxy-software/unified-sip-proxy-v10-eol.html .

## Cisco Contact Center SIP Proxy

Unified CCE and Packaged CCE 12.6(x) solutions are compatible with Cisco Contact Center SIP Proxy (CCCSP) 15.0(1).

## Third-party SIP Proxy

Cisco recommends Oracle® Communication Session Router, version SCZ9.1.0 GA (Build 46) or later. However, you can also choose to deploy any third-party SIP proxy that suits your requirements.

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

Webex DX 80/Webex Desk Pro

Y

Y

Voice-only

N

N

N

N

N

Y

Y

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

■ Webex:

— Point-to-Point calls are supported if the lines are registered with CUCM or via SIP URI.

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

The following AD FS versions are supported with this Unified CCE release:

■ AD FS 5.0: Windows Server 2019

■ AD FS 4.0: Windows Server 2016

■ AD FS 3.0: Windows Server 2012 R2

Besides the AD FS versions listed above, Unified CCE supports all SAML 2.0 compliant IdPs.

See the documentation of your IdP for details on configuring the IdP in CCE.

Notes

■ Unified CCMP, Release 12.6 support Microsoft AD FS 2012 R2 and 2016 with WS-Federation via JSON Web Token (JWT).

However, user authentication access for Unified CCMP can be provided by one of the supported IdPs via Federated Trust with Microsoft AD FS. Federated Trust is supported per Microsoft AD FS and third-party IdP documentation and support.

■ Kerberos is supported for single-domain authentication (non-federated environments).

■ For ECE:

— Agent-based users have the same compatibility as Cisco IDS.

— Supervisors outside Cisco Finesse support any SAML 2.0 complaint IDP.

## Transport Layer Security

The Unified CCE database access encrypts SQL user authentication using TLS, but the data connection isn’t encrypted.

12.6 Component

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

CCMP

✔

X

ACD

X

N/A

UC Manager

✔

N/A

## Client Operating System

Components

Clients OS

Cisco Finesse

Microsoft Windows 10 and Windows 11 (64-bit)

Mac OS X 10.15.x or later

Chrome OS 88.0.4324 or later

Cisco Unified Intelligence Center

Microsoft Windows 10 and Windows 11 (64-bit)

Mac OS X 10.15.x or later

Cisco Unified Call Studio

Microsoft Windows 10 (64-bit)

Microsoft Windows 11 (64-bit) with CVP 12.6(2) ES11 or later

Administration Client

Microsoft Windows Server 2016 (Standard and Datacenter editions)

Microsoft Windows Server 2019 (Standard and Datacenter editions) (64-bit)

Microsoft Windows 10 (Enterprise and Professional) (64-bit) Microsoft Windows 11 (Enterprise and Professional) (64-bit)

Internet Script Editor (ISE)

Microsoft Windows 10 (Enterprise and Professional) (64-bit) Microsoft Windows 11 (Enterprise and Professional) (64-bit)

Silent Monitor Service for Unified CCE Toolkit

Microsoft Windows 10 (Enterprise and Professional) (64-bit)

CTI OS Clients

Microsoft Windows 10 (Enterprise and Professional) (64-bit)

Note: For more information on the supported versions of Microsoft Windows 10 with specific versions of .NET Framework, see the Microsoft documentation.

Notes

■ CTI OS is only supported for Unified ICM when used in conjunction with Avaya PG, Aspect PG, AACC (Symposium) PG, or non-reference design deployments like Parent-Child that employ Unified CCE System PG. The supported CTI OS version is aligned with the supported PG version.

■ CTI OS and CAD are not supported from Unified CCE, Release 11.5(x). New and existing deployments upgrading to Unified CCE release 12.0(1) or later must use Finesse desktop instead of CTI OS and CAD.

■ Silent Monitoring Service is not supported on CTI OS deployments starting with Unified CCE release 11.5(1).

## Supported Browsers

Operating System

Browser Version for Release 12.6(1)

Browser Version for Release 12.6(2)

Microsoft Windows Server 2016 (Standard and Datacenter editions)

Microsoft Windows Server 2019 (Standard and Datacenter editions)

Google Chrome 88.0.4324 or later

Google Chrome 106.0.5249 or later

Edge Chromium 88.0.4324 or later

Edge Chromium 106.0.5249 or later

Firefox Extended Supported Release (ESR) 68.4 and later ESRs

Firefox Extended Supported Release (ESR) 78.11 and later ESRs

Microsoft Windows 10 and Windows 11 (64-bit)

Google Chrome 88.0.4324 or later

Google Chrome 106.0.5249 or later

Edge Chromium 88.0.4324 or later

Edge Chromium 106.0.5249 or later

Firefox ESR 68.4 and later ESRs

Firefox ESR 78.11 and later ESRs

Mac OS X

Google Chrome 88.0.4324 or later

Google Chrome 106.0.5249 or later

Edge Chromium 88.0.4324 or later

Edge Chromium 106.0.5249 or later

Firefox ESR 68.4 and later ESRs

Firefox ESR 78.11 and later ESRs

Chromebook with Chrome OS 70

Google Chrome 60 or later

Google Chrome 60 or later

Chromium 73 or later

Chromium 73 or later

Note: Unified CCE Administration Client supports only Microsoft Chromium Edge browser.

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

■ Unified ICM/CCE is qualified only on a retail installation of the Microsoft Windows Server (Standard and Datacenter editions). Cisco doesn't support Unified ICM/CCE on a customized Microsoft Windows image (for example, a corporate image). If you use a customized image of the Microsoft Windows operating system, the Unified ICM/CCE application can fail.

■ ECE 12.6 is supported only on Windows Server 2019 (Standard and Datacenter). For Windows Server 2016 support across the deployment, continue to use ECE 12.5 with CCE 12.6.

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

■ ECE 400 agent deployment: Microsoft SQL Server 2019 (Standard and Enterprise editions)

■ ECE 1500 agent deployment: Microsoft SQL Server 2019 (Standard and Enterprise editions)

■ ECE 2500 agent deployment: Microsoft SQL Server 2019 (Standard and Enterprise editions)

■ ECE Geographically Redundant/High Availability installation: Microsoft SQL Server 2019 (Enterprise edition)

Unified CCMP

Microsoft SQL Server 2019 (Standard and Enterprise editions)

Note: For CCE components, the combination of Windows Server 2016 with SQL Server 2019, or Windows Server 2019 with SQL Server 2017 is not supported.

## Microsoft Windows and Microsoft SQL Server Localization Support

The following table lists the supported localized versions of Microsoft Windows Server and SQL Server to use with Cisco Unified ICM and Unified CCE components.

Microsoft Windows Server

Microsoft SQL Server

SQL Collation Setting

Danish

Latin1_General

Dutch

Finnish

French

French

German

German

Italian

Italian

Norwegian

Portuguese (Brazil)

Portuguse (Brazil)

Spanish

Spanish

Swedish

Chinese (simplified)

Chinese (simplified)

Chinese_PRC

Chinese (traditional)

Chinese (traditional)

Chinese_Taiwan_Stroke

Japanese

Japanese

Japanese

Korean

Korean

Korean_Wansung

Polish

Polish

Russian

Cyrillic_General

Turkish

Turkish

Notes

■ In the above table, if a corresponding localized SQL Server in the Microsoft SQL Server column for a particular language in the Microsoft Windows Server column is not shown, use the English SQL Server with the applicable setting in the SQL Collation Setting column.

■ Unified CCE supports multilingual versions of Microsoft Windows Server (English Windows Server with language packs installed). For details about how to set up multilingual versions of Microsoft Windows Server, see the http://www.cisco.com/en/US/products/sw/custcosw/ps1844/prod_installation_guides_list.html.

■ Use English SQL Server on multilingual versions of the Microsoft Windows Server environment. These are examples of supported multilingual environments:

— English Windows Server with Japanese Windows language pack installed, and English SQL Server with Japanese SQL Collation Setting.

— English Windows Server with Russian Windows language pack installed, and English SQL Server with Cyrillic_General SQL Collation Setting.

## JDK and JRE

CCE Component(s)

Release 12.6(1)

Release 12.6(2)

Unified CCE

version 1.8 (32-bit), update 272 or later

version 1.8 (32-bit), update 352 or later

Unified CVP

version 1.8 (64-bit), update 275 or later

version 1.8 (64-bit), update 342 or later

Cisco Enterprise Chat and Email, and Unified CCMP

version 11

These components do not have a 12.6(2) release.

Unified Intelligence Center, Live Data, Cisco IdS, and Cisco Finesse

version 1.8 (64-bit), update 282

version 1.8 (64-bit), update 282

Platform services for the Cisco Voice Operating System (VOS) components

version 1.8 (32-bit), update 262

version 1.8 (32-bit), update 262

Cisco VVB

version 1.8 (32-bit), update 262

version 1.8 (32-bit), update 262

Speech server

version 11.0.16 (64-bit)

version 11.0.16 (64-bit)

Cloud Connect

version 1.8 (32-bit), update 262

version 1.8 (64-bit), update 345

version 1.8 (32-bit), update 262

version 1.8 (64-bit), update 345

Customer Collaboration Platform 12.5(1) SU1

version 1.8, update 262

version 1.8, update 262

For instructions on applying newer Java security updates, see the Security Guide for Cisco Unified ICM/Contact Center Enterprise guide.

Note: OpenLogic is the only supported and certified OpenJDK JRE vendor for ICM Core, Unified CCE, and Unified CVP applications.

## Supported Languages

Unified CCE Administration

Unified CCE Reporting Templates

Unified Intelligence Center

Finesse

Customer Collaboration Platform

Enterprise Chat and Email

CCMP

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

■ Microsoft Windows Server 2016 (Standard and Datacenter editions) comes with pre-installed .NET version 4.6.2.

■ Microsoft Windows Server 2019 (Standard and Datacenter editions) comes with pre-installed .NET version 4.7.2.

■ Unified CCE, Administration Client, and CTI OS Client installs .NET version 4.8.

## Other Supported Software

Function

Software

Microsoft Active Directory

Microsoft Active Directory versions 2012 R2, 2016, 2019, and 2022 are supported with Unified ICM/Unified CCE and Packaged CCE solutions.

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

■ Unified CCE and Packaged CCE solutions support third-party VDI infrastructures for Cisco Finesse and CUIC. Ensure that your third-party VDI infrastructure is supported by Cisco softphone endpoints used on agent and supervisor VDI-based desktops.

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

Note : SSO access to the Unified Contact Center Enterprise web applications through the load balancer is not qualified.

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

Note: For specific interfaces where you can use load balancers in your deployment, see the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html.

## Non-Reference Design Compatibility

### Unified CCE Parent Child Compatibility

Parent PG 11.6(x)

Parent PG 12.0(x)

Parent PG 12.5(x)

Parent PG 12.6(x)

Child PG 11.6(x)

Yes

Yes

Yes

Yes

Child PG 12.0(x)

Yes

Yes

Yes

Yes

Child PG 12.5(x)

Yes

Yes

Yes

Yes

Child PG 12.6(x)

Yes

Yes

Yes

Yes

### ICM-to-ICM Gateway Compatibility

ICM Client

ICM Server

12.6

12.6

12.6

12.5

12.6

12.0

12.6

11.6

12.5

12.6

12.0

12.6

11.6

12.6

Packaged CCE 12.6 supports ICM-to-ICM Gateway in 4000 and 12000 Agent deployments only.

### Third Party ACDs

#### Avaya

##### Avaya Considerations

■ Avaya changed names from DEFINITY to MultiVantage to Avaya Communications Manager (ACM) to Avaya Aura Communications Manager (AACM).

■ Packaged CCE 12.6 versions support Avaya Peripheral Gateways for AACM in the 4000 and 12000 Agent deployments only.

■ Real-Time Agent (RTA) 5.0.5 and 6.0 enhanced functionality (60 skills per agent and 2000 skill groups per system) are not supported by ICM.

■ ICM does not support more than 12000 active associations on a single system.

■ Using the CMS interface with Avaya 10.x requires a minimum CMS version of 20.

■ Cisco supports the Avaya S8300, S8400, S85XX, S87XX, and S88XX Servers in support of ACM.

■ Cisco supports the general use of Avaya IP Phones.

■ Although Avaya stopped supporting the CVLAN interface in 2012, Unified CCE still uses this interface to communicate with Avaya products. Note that 12.6(1) is the last supported release in the 12.6 release train for the CVLAN interface.

■ Avaya Multi-Application Platform for DEFINITY (MAPD) is not supported.

■ Support for third-party ACD clients, SDKs, and interfaces integrated with ICM stops when the third-party ACD manufacturer ends mainstream support.

■ Ten-digit Agent extensions and Agent IDs are supported from ICM 9.0(3) and later that have ACM 6.2 and later, AES 6.2 and later, and CMS R16 with RTA 6.0 pl: 13g.

##### Avaya CMS RTA Support

RTA Version

ICM/Packaged CCE 12.6

6.0(x)

Yes

6.0 Extended

No

7.0

Note : Supported only with Avaya 10.x, which requires a minimum CMS version of 20.

Yes

##### Avaya Communications Manager (ACM) Support

ACM Version

ICM/Packaged CCE 12.6

ACM 8.1 (x)

Yes

ACM 10.1(x)

Note : When configuring the Avaya PG using the Peripheral Gateway Setup tool for integration with the 10.1(x) version of the AES or ACM server, use the CVLAN interface. The TSAPI interface is currently not supported with AES or ACM 10.x servers.

Yes

##### Notes on Avaya Communications Manager Support

Avaya Product Support Notice patch PSN020249u is required for ACM 7.0 (x) and above. For details, see the Product Support Notice at https://downloads.avaya.com/css/P8/documents/101020687 .

##### AES Server and CVLAN/TSAPI Client Support

AES Server

CVLAN Client Supported

TSAPI Client Supported

ICM/Packaged CCE 12.6

AES 8.1(x)

Yes

Yes

Yes

AES 10.1 (x)

Yes

No

Yes

##### Notes on AES Server and CVLAN/TSAPI Client Support

· ICM/Packaged CCE 12.6 supports all CVLAN Client and TSAPI Client versions currently supported by Avaya.

· Support for an ACM or AES version depends on the Avaya release cycles (patches and upgrades). For more details on supported versions, see the Avaya documentation.

· Starting ICM Release 12.6(2), Cisco recommends that you install TSAPI client library version 10.1 on the Avaya Peripheral Gateway machine as we have refreshed the TAESPIM using the TSAPI 10.1 SDK. If you are on the ICM Release 12.6(1) or earlier, you must install the TSAPI client library version that is the same as the AES server.

· If you plan to integrate the Avaya AES server with the TSAPI interface instead of CVLAN, contact your Cisco Account Manager for support advice. CVLAN is the recommended interface for Unified ICM/CCE in the 12.6(2) release.

##### CTI Support for ACD Types

ACD Vendor

ACD Model

CTI Server Protocol Support

CTI OS Support

Avaya

Avaya Communication Manager v6.3 to v8.1 (over CVLAN and TSAPI in CCE release 12.6(1))

Yes

Yes

Cisco

Unified CCE

Yes

Yes (only when integrated via Unified CCE System PG)

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

© 2023 Cisco Systems, Inc. All rights reserved.

[1] For more information, check the Release Notes at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html .

| PCCE/UCCE Components, Release 12.6(x) | PCCE/UCCE Components, Release 12.5 |
|---|---|
| Cloud Connect | IdS (Standalone) | Finesse | ECE | CVP | VVB | CUIC (Standalone) | CUIC-LiveData-IdS (Coresident) | Router | Logger | AW | Live Data (Standalone) | PG | Customer Collaboration Platform | CCMP | Notes |
| Cloud Connect |  | Y | Y |  | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |  |  |
| Identity Server (Standalone) | N |  | Y | Y |  |  | Y |  |  |  | Y |  |  |  |  |  |
| Finesse | N | N |  | Y |  |  | Y | N |  |  | Y | Y | Y | Y |  | When Cisco Finesse and CUIC are on 12.6, and Live Data is on 12.5, for Live Data gadgets to load in Cisco Finesse, install CUIC 12.5(1) ES 09 or later on all Live Data stand-alone servers. |
| CVP | N |  |  |  |  | Y |  |  | Y | Y | Y |  | Y |  |  |  |
| VVB | N |  |  |  | Y |  |  |  |  |  |  |  |  |  |  |  |
| CUIC (Standalone) | N | N | N |  |  |  |  |  |  |  | Y | Y |  |  |  |  |
| CUIC-LiveData-IdS (Coresident) | N |  | N |  |  |  |  |  | N |  | N |  | Y |  |  |  |
| Router | N |  |  |  | N |  |  | N |  |  |  | N | Y | Y | N |  |
| Logger | N |  |  |  | N |  |  |  |  |  |  |  | Y | Y | N |  |
| AW | N | N | N | Y | N |  | N | N |  |  |  | N | Y | Y | N |  |
| Live Data (Standalone) | N |  | N |  |  |  | N |  | N |  | N |  | Y |  |  |  |
| PG | N |  | N | Y | N |  |  | N | N | N | N | N |  | Y |  | Upgrade CCP to 12.5(1) SU1 for compatibility with CCE 12.6. |

| PCCE/UCCE Components, Release 12.6(1) | PCCE/UCCE, Release 12.5 |
|---|---|
| Cloud Connect | IdS (Standalone) | Finesse | ECE | CVP | VVB | CUIC (Standalone) | CUIC-LiveData-IdS (Coresident) | Router | Logger | AW | Live Data (Standalone) | PG | Customer Collaboration Platform | CCMP | Notes |
| ECE |  | N | Y |  |  |  |  |  |  |  | Y |  | Y |  |  |  |
| CCMP |  |  |  |  | Y |  |  |  | Y | Y | Y |  |  |  |  | Not Applicable to Packaged CCE. |

| PCCE/UCCE Components, Release 12.6(x) | PCCE/UCCE, Release 12.0 |
|---|---|
| IdS (Standalone) | Finesse | ECE | CVP | VVB | CUIC (Standalone) | CUIC-LiveData-IdS (Coresident) | Router | Logger | AW | Live Data (Standalone) | PG | SocialMiner | CCMP | Notes |
| Cloud Connect |  | N |  | N | N | N | N | N | N | N | N | N | N |  |  |
| Identity Server (Standalone) |  | Y | Y |  |  | Y |  |  |  | Y |  |  |  |  |  |
| Finesse | N |  | N |  |  | Y | N |  |  | Y | Y | Y | Y |  | When Cisco Finesse and CUIC are on 12.6, and Live Data is on 12.0, for Live Data gadgets to load in Cisco Finesse, install CUIC 12.0(1) ES 15 or later on all Live Data stand-alone servers. |
| CVP |  |  |  |  | Y |  |  | Y | Y | Y |  | Y |  |  | On Packaged CCE 12.0, install CCE 12.0 ES37 before you upgrade CVP to 12.6(1). |
| VVB |  |  |  | Y |  |  |  |  |  |  |  |  |  |  |  |
| CUIC (Standalone) | N | N |  |  |  |  |  |  |  | Y | Y |  |  |  |  |
| CUIC-LiveData-IdS (Coresident) |  | N |  |  |  |  |  | N |  | N |  | Y |  |  |  |
| Router |  |  |  | N |  |  | N |  |  |  | N | Y | Y | N |  |
| Logger |  |  |  | N |  |  |  |  |  |  |  | Y | Y | N |  |
| AW | N | N | N | N |  | N | N |  |  |  | N | Y | Y | N |  |
| Live Data (Standalone) |  | N |  |  |  | N |  | N |  | N |  | Y |  |  |  |
| PG |  | N | N | N |  |  | N | N | N | N | N |  | N |  |  |

| PCCE/UCCE Components, Release 12.6(1) | PCCE/UCCE, Release 12.0 |
|---|---|
| IdS (Standalone) | Finesse | ECE | CVP | VVB | CUIC (Standalone) | CUIC-LiveData-IdS (Coresident) | Router | Logger | AW | Live Data (Standalone) | PG | SocialMiner | CCMP | Notes |
| ECE | N | Y |  |  |  |  |  |  |  | Y |  | Y |  |  |  |
| CCMP |  |  |  | Y |  |  |  | Y | Y | Y |  |  |  |  | Not Applicable to Packaged CCE. |

| Unified CCE Components, Release 12.6(1) | Unified CCE, Release 11.6 |
|---|---|
| IdS (Standalone) | Finesse | ECE | CVP | VVB | CUIC (Standalone) | CUIC-LiveData-IdS (Coresident) | Router | Logger | AW | Live Data (Standalone) | PG | SocialMiner | CCMP | Notes |
| Cloud Connect |  | N |  | N | N | N | N | N | N | N | N | N | N |  |  |
| Identity Server (Standalone) |  | Y | Y |  |  | Y |  |  |  | Y |  |  |  |  |  |
| Finesse | N |  | N |  |  | Y | N |  |  | Y | Y | Y | Y |  | When Cisco Finesse and CUIC are on 12.6, and Live Data is on 11.6, for Live Data gadgets to load in Cisco Finesse, install CUIC 11.6(1) ES 22 or later on all Live Data stand-alone servers. |
| ECE | N | Y |  |  |  |  |  |  |  | Y |  | Y |  |  |  |
| CVP |  |  |  |  | Y |  |  | Y | Y | Y |  | Y |  |  |  |
| VVB |  |  |  | Y |  |  |  |  |  |  |  |  |  |  |  |
| CUIC (Standalone) | N | N |  |  |  |  |  |  |  | Y | Y |  |  |  |  |
| CUIC-LiveData-IdS (Coresident) |  | N |  |  |  |  |  | N |  | N |  | Y |  |  |  |
| Router |  |  |  | N |  |  | N |  |  |  | N | Y | Y | N |  |
| Logger |  |  |  | N |  |  |  |  |  |  |  | Y | Y | N |  |
| AW | N | N | N | N |  | N | N |  |  |  | N | Y | Y | N |  |
| Live Data (Standalone) |  | N |  |  |  | N |  | N |  | N |  | Y |  |  |  |
| PG |  | N | N | N |  |  | N | N | N | N | N |  | N |  |  |
| CCMP |  |  |  | Y |  |  |  | Y | Y | Y |  |  |  |  | CCMP is not applicable to Packaged CCE. On UCCE 11.6, install UCCE 11.6(1) ES 7 or 11.6(2) before you upgrade CCMP to 12.5(1). |

|  | Gateway Functionality |  |
|---|---|---|
| Central Controller version 12.6(2) Model | Software Version | VXML Gateway Browser | Call Progress Analysis for Outbound Options for SIP Trunks (CUBE) | Unified CCE and Packaged CCE Support |
| ASR 1001X ASR 1002X ASR 1004 RP2 ASR 1006 RP2 | IOS XE 17.2 | No | Yes | Yes |
| IOS XE 17.4 |
| IOS XE 17.6 |
| IOS XE 17.9 |
| IOS XE 17.12 |
| IOS XE 17.15 |
| IOS XE 17.18 |
| Virtual CUBE | IOS XE 17.6 | No | No | Yes |
| IOS XE 17.9 |
| IOS XE 17.12 |
| IOS XE 17.15 |
| IOS XE 17.18 |
| ISR G3 43xx (4321, 4331, 4351) ISR G3 44xx (4431, 4451, 4461) | IOS XE 17.6 | No | Yes | Yes |
| IOS XE 17.9 |
| IOS XE 17.12 |
| IOS XE 17.15 |
| IOS XE 17.18 |
| Catalyst 8200/8300 | IOS XE 17.6 | No | Yes | Yes |
| IOS XE 17.9 |
| IOS XE 17.12 |
| IOS XE 17.15 |
| IOS XE 17.18 |

|  | Gateway Functionality |  |
|---|---|---|
| Central Controller version 12.6(1) Model | Software Version | VXML Gateway Browser | Call Progress Analysis for Outbound Options for SIP Trunks (CUBE) | Unified CCE and Packaged CCE Support |
| ASR 1001X ASR 1002X ASR 1004 RP2 ASR 1006 RP2 | IOS XE 17.2 | No | Yes | Yes |
| IOS XE 17.4 |
| IOS XE 17.6 |
| IOS XE 17.9 |
| Virtual CUBE | IOS XE 17.2 | No | No | Yes |
| IOS XE 17.4 |
| IOS XE 17.6 |
| IOS XE 17.9 |
| IOS XE 17.15 |
| ISR G3 43xx (4321, 4331, 4351) ISR G3 44xx (4431, 4451, 4461) | IOS XE 17.2 | No | Yes | Yes |
| IOS XE 17.4 |
| IOS XE 17.6 |
| IOS XE 17.9 |
| Catalyst 8200/8300 | IOS XE 17.6 | No | Yes | Yes |
| IOS XE 17.9 |
| IOS XE 17.15 |

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
| Webex DX 80/Webex Desk Pro | Y | Y | Voice-only | N | N | N | N | N | Y | Y |

| 12.6 Component | TLS 1.2 |
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
| CCMP | ✔ | X |
| ACD | X | N/A |
| UC Manager | ✔ | N/A |

| Components | Clients OS |
|---|---|
| Cisco Finesse | Microsoft Windows 10 and Windows 11 (64-bit) |
| Mac OS X 10.15.x or later |
| Chrome OS 88.0.4324 or later |
| Cisco Unified Intelligence Center | Microsoft Windows 10 and Windows 11 (64-bit) |
| Mac OS X 10.15.x or later |
| Cisco Unified Call Studio | Microsoft Windows 10 (64-bit) Microsoft Windows 11 (64-bit) with CVP 12.6(2) ES11 or later |
| Administration Client | Microsoft Windows Server 2016 (Standard and Datacenter editions) Microsoft Windows Server 2019 (Standard and Datacenter editions) (64-bit) |
| Microsoft Windows 10 (Enterprise and Professional) (64-bit) Microsoft Windows 11 (Enterprise and Professional) (64-bit) |
| Internet Script Editor (ISE) | Microsoft Windows 10 (Enterprise and Professional) (64-bit) Microsoft Windows 11 (Enterprise and Professional) (64-bit) |
| Silent Monitor Service for Unified CCE Toolkit | Microsoft Windows 10 (Enterprise and Professional) (64-bit) |
| CTI OS Clients | Microsoft Windows 10 (Enterprise and Professional) (64-bit) Note: For more information on the supported versions of Microsoft Windows 10 with specific versions of .NET Framework, see the Microsoft documentation. |

| Operating System | Browser Version for Release 12.6(1) | Browser Version for Release 12.6(2) |
|---|---|---|
| Microsoft Windows Server 2016 (Standard and Datacenter editions) Microsoft Windows Server 2019 (Standard and Datacenter editions) | Google Chrome 88.0.4324 or later | Google Chrome 106.0.5249 or later |
| Edge Chromium 88.0.4324 or later | Edge Chromium 106.0.5249 or later |
| Firefox Extended Supported Release (ESR) 68.4 and later ESRs | Firefox Extended Supported Release (ESR) 78.11 and later ESRs |
| Microsoft Windows 10 and Windows 11 (64-bit) | Google Chrome 88.0.4324 or later | Google Chrome 106.0.5249 or later |
| Edge Chromium 88.0.4324 or later | Edge Chromium 106.0.5249 or later |
| Firefox ESR 68.4 and later ESRs | Firefox ESR 78.11 and later ESRs |
| Mac OS X | Google Chrome 88.0.4324 or later | Google Chrome 106.0.5249 or later |
| Edge Chromium 88.0.4324 or later | Edge Chromium 106.0.5249 or later |
| Firefox ESR 68.4 and later ESRs | Firefox ESR 78.11 and later ESRs |
| Chromebook with Chrome OS 70 | Google Chrome 60 or later | Google Chrome 60 or later |
| Chromium 73 or later | Chromium 73 or later |

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
| Enterprise Chat and Email | ■ ECE 400 agent deployment: Microsoft SQL Server 2019 (Standard and Enterprise editions) ■ ECE 1500 agent deployment: Microsoft SQL Server 2019 (Standard and Enterprise editions) ■ ECE 2500 agent deployment: Microsoft SQL Server 2019 (Standard and Enterprise editions) ■ ECE Geographically Redundant/High Availability installation: Microsoft SQL Server 2019 (Enterprise edition) |
| Unified CCMP | Microsoft SQL Server 2019 (Standard and Enterprise editions) |

| Microsoft Windows Server | Microsoft SQL Server | SQL Collation Setting |
|---|---|---|
| Danish |  | Latin1_General |
| Dutch |  |
| Finnish |  |
| French | French |
| German | German |
| Italian | Italian |
| Norwegian |  |
| Portuguese (Brazil) | Portuguse (Brazil) |
| Spanish | Spanish |
| Swedish |  |
| Chinese (simplified) | Chinese (simplified) | Chinese_PRC |
| Chinese (traditional) | Chinese (traditional) | Chinese_Taiwan_Stroke |
| Japanese | Japanese | Japanese |
| Korean | Korean | Korean_Wansung |
| Polish |  | Polish |
| Russian |  | Cyrillic_General |
| Turkish |  | Turkish |

| CCE Component(s) | Release 12.6(1) | Release 12.6(2) |
|---|---|---|
| Unified CCE | version 1.8 (32-bit), update 272 or later | version 1.8 (32-bit), update 352 or later |
| Unified CVP | version 1.8 (64-bit), update 275 or later | version 1.8 (64-bit), update 342 or later |
| Cisco Enterprise Chat and Email, and Unified CCMP | version 11 | These components do not have a 12.6(2) release. |
| Unified Intelligence Center, Live Data, Cisco IdS, and Cisco Finesse | version 1.8 (64-bit), update 282 | version 1.8 (64-bit), update 282 |
| Platform services for the Cisco Voice Operating System (VOS) components | version 1.8 (32-bit), update 262 | version 1.8 (32-bit), update 262 |
| Cisco VVB | version 1.8 (32-bit), update 262 | version 1.8 (32-bit), update 262 |
| Speech server | version 11.0.16 (64-bit) | version 11.0.16 (64-bit) |
| Cloud Connect | version 1.8 (32-bit), update 262 version 1.8 (64-bit), update 345 | version 1.8 (32-bit), update 262 version 1.8 (64-bit), update 345 |
| Customer Collaboration Platform 12.5(1) SU1 | version 1.8, update 262 | version 1.8, update 262 |

|  | Unified CCE Administration | Unified CCE Reporting Templates | Unified Intelligence Center | Finesse | Customer Collaboration Platform | Enterprise Chat and Email | CCMP |
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
| Microsoft Active Directory | Microsoft Active Directory versions 2012 R2, 2016, 2019, and 2022 are supported with Unified ICM/Unified CCE and Packaged CCE solutions. |
| Remote Administration | For Remote Desktop usage information, see the Remote Administration section in the Security Guide for Cisco Unified ICM/Contact Center Enterprise . |
| Antivirus Software | Cisco Contact Center Enterprise solution supports all the third-party antivirus software and scanners. For more information, see the following documents: ■ General Antivirus Guidelines section in the Security Guide for Cisco Unified ICM/Contact Center Enterprise . ■ Cisco Customer Contact Software Policy for Use of Third-Party Software Bulletin |
| Virtualization | For more information about virtualization for all Unified CCE components, see the Unified Communications in a Virtualization page https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html . |
| Unified Intelligence Center reporting | Microsoft Excel Versions 2013, 2016, Office 365. Note: Office 365 doesn’t support Authenticated excel report permalink. |

| Category | Requirements |
|---|---|
| Nuance Speech Suite 11.0.x | Note: Cisco Virtualized Voice Browser (VVB) supports the Nuance components compatible with MRCP Protocol v1 and v2. For further details on the compatibility, see the Nuance Compatibility Matrix. |
| MRCP Protocol Version | v1 and v2 |
| VoiceXML Protocol Version | 2.0 |

|  | Parent PG 11.6(x) | Parent PG 12.0(x) | Parent PG 12.5(x) | Parent PG 12.6(x) |
|---|---|---|---|---|
| Child PG 11.6(x) | Yes | Yes | Yes | Yes |
| Child PG 12.0(x) | Yes | Yes | Yes | Yes |
| Child PG 12.5(x) | Yes | Yes | Yes | Yes |
| Child PG 12.6(x) | Yes | Yes | Yes | Yes |

| ICM Client | ICM Server |
|---|---|
| 12.6 | 12.6 |
| 12.6 | 12.5 |
| 12.6 | 12.0 |
| 12.6 | 11.6 |
| 12.5 | 12.6 |
| 12.0 | 12.6 |
| 11.6 | 12.6 |

| RTA Version | ICM/Packaged CCE 12.6 |
|---|---|
| 6.0(x) | Yes |
| 6.0 Extended | No |
| 7.0 Note : Supported only with Avaya 10.x, which requires a minimum CMS version of 20. | Yes |

| ACM Version | ICM/Packaged CCE 12.6 |
|---|---|
| ACM 8.1 (x) | Yes |
| ACM 10.1(x) Note : When configuring the Avaya PG using the Peripheral Gateway Setup tool for integration with the 10.1(x) version of the AES or ACM server, use the CVLAN interface. The TSAPI interface is currently not supported with AES or ACM 10.x servers. | Yes |

| AES Server | CVLAN Client Supported | TSAPI Client Supported | ICM/Packaged CCE 12.6 |
|---|---|---|---|
| AES 8.1(x) | Yes | Yes | Yes |
| AES 10.1 (x) | Yes | No | Yes |

| ACD Vendor | ACD Model | CTI Server Protocol Support | CTI OS Support |
|---|---|---|---|
| Avaya | Avaya Communication Manager v6.3 to v8.1 (over CVLAN and TSAPI in CCE release 12.6(1)) | Yes | Yes |
| Cisco | Unified CCE | Yes | Yes (only when integrated via Unified CCE System PG) |