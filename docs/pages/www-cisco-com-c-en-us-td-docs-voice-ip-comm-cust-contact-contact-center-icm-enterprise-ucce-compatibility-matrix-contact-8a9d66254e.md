---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-ucce-compatibility-matrix-contact-8a9d66254e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/ucce_compatibility/matrix/Contact_Center_Enterprise_Solution_Compatibility_Matrix_Release_15_0.html
retrieved_at: 2026-08-16T14:53:01.242480+00:00
---

Contact Center Enterprise Solution Compatibility Matrix, Release 15.0(1)

# Contact Center Enterprise Solution Compatibility Matrix, Release 15.0(1)

### Download Options

Updated: July 30, 2026

Contact Center Enterprise Solution Compatibility Matrix, Release 15.0(1)

First Published : 2025-04-30

NOTE: Works with document’s Advanced Properties “First Published” property. Click File | Properties | Advanced Properties | Custom .

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

IOS Versioning Key 16.1(4) M3 and 16.1(4) T1 as Examples . 11

IOS-XE Versioning Key 16.12.1a and 16.12.3 as Examples . 12

Cisco Unified SIP Proxy (Deprecated) 12

Cisco Contact Center SIP Proxy . 12

End Points for Agents and Callers . 12

Endpoints Supported for Callers Only . 15

Single Sign On (SSO) Identity Providers (IdPs) 15

Transport Layer Security . 15

Client Operating System .. 17

Supported Browsers . 18

Server Operating System .. 19

SQL Server and Informix Versions . 20

Microsoft Windows and Microsoft SQL Server Localization Support 20

Java, JDK, and Tomcat 22

Supported Languages . 23

Microsoft .NET Framework . 25

Other Supported Software . 26

Virtual Desktop Infrastructure Support 26

Hypervisor compatibility . 27

VMWare ESXI Compatibility . 27

Nutanix Compatibility . 27

Automatic Speech Recognition and Text to Speech . 27

Load Balancers . 28

ICM-to-ICM Gateway Compatibility . 28

Third Party ACDs . 29

Avaya . 29

Legal Information (software documentation only) 30

Cisco Trademark (all documentation) 31

Cisco Copyright (all documentation) 31

## Overview

The Contact Center Enterprise (CCE) Solution Compatibility Matrix includes all the Cisco CCE solutions and component compatibility information. This compatibility matrix specifies all supported configurations and versions for Release 15.0(1), which includes the maintenance, ES or SU releases of 15.0(1). The information in this compatibility matrix supersedes compatibility information in any other CCE documentation. If the Compatibility Matrix does not state a configuration or version, then it does not support it.

Notes

■ Make sure that your Router, Logger, and AW are in the same version as your PG or in a version that is higher than your PG.

■ The Compatibility Matrix specifies all supported third-party software (such as Nuance and Informix) and its versions. Support for these software versions and their interoperability depends on the release cycles (patches and upgrades) of the third-party software. For example, support for ESXi depends on VMware release cycles.

■ As per the CCE's long-term MR strategy, the latest ES (patch) release is the primary supported version in that train.

■ Support for a CUCM release is inclusive of all updates.

■ Upgrade all the solution components to experience the new features delivered as part of a particular solution release version. Upgrading only the component that delivers the new feature may not be sufficient in all cases. For more information on upgrade paths, see the CCE Upgrade Flowcharts in the respective Contact Center Enterprise Installation and Upgrade Guides.

■ If you are upgrading from version 12.6(2) to 15.0 SU1, follow the compatibility tables for 12.6(x) to 15.0(1) in this Compatibility Matrix. However, if you are upgrading from 15.0(1) to 15.0 SU1, there is no need to refer to a specific Compatibility Matrix.

■ Fresh install of IP IVR 15.0(1) is compatible with CCE 15.0(1).

## Central Controller and Component Compatibility

PCCE/UCCE Components, Release 15.0(1)

PCCE/UCCE Components, Release 12.6(x)

Cisco Reverse Proxy

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

Cisco Reverse Proxy

Y

Y

Y

Y

Y

Y

Y

Cloud Connect

N

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

N

Y

Y

Y

Y

Y

Finesse

N

N

N

Y

Y

N

Y

Y

Y

Y

When Cisco Finesse is on 15.0(1) and CUIC is on 12.6(2), install CUIC 12.6(2) ES04 or later on all CUIC nodes for the CUIC gadgets to load. Finesse 15.0(1) and CUIC 12.6(1) are not compatible.

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

N

N

Y

Y

CUIC-LiveData-IdS (Coresident)

N

N

N

Y

Y

Y

12.6(2) AW is compatible with 15.0(1) Coresident, but 12.6(1) AW is not.

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

Y

Y

Y

Y

12.6(2) AW is compatible with 15.0(1) Live Data, but 12.6(1) AW is not.

PG

N

N

N

N

N

N

N

N

Y

PCCE/UCCE Components, Release 15.0(1)

PCCE/UCCE, Release 12.6(x)

Cisco Reverse Proxy

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

N

Y

N

Y

Y

CCMP

Y

Y

Y

Y

Not applicable to Packaged CCE.

PCCE/UCCE Components, Release 15.0(1)

PCCE/UCCE Components, Release 12.5(x)

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

Identity Server (Standalone)

Y

Y

Y

Y

Y

Finesse

N

Y

N

N

Y

Y

Y

Y

When Cisco Finesse is on 15.0(1) and CUIC is on 12.5(2), CUIC gadgets will not load in Finesse. Finesse 15.0(1) and CUIC 12.5(1) are not compatible.

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

Y

PCCE/UCCE Components, Release 15.0(1)

PCCE/UCCE, Release 12.5(x)

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

N

Y

Y

CCMP

Y

Y

Y

Y

Not Applicable to Packaged CCE.

Notes

■ Unified CCE and Packaged CCE compatibility with CUCM:

— CUCM, releases 14 and 15 ( including all its service updates) are supported with Unified CCE and Packaged CCE, Release 15.0(1).

■ Cisco Unified Contact Center Management Portal (CCMP) compatibility with CUCM:

— CUCM 14 ( including all its service updates like 14SU4) and 15 are supported with CCMP, Release 15.0(1).

■ The 12.5(2) OVA versions for Cisco Finesse, Unified Intelligence Center, Live Data, IdS, and Cisco VVB are listed as 12.5(1) SU on the Cisco software downloads page.

■ The IdS and Coresident compatibility mentioned in the preceding Central Controller tables applies only when SSO is enabled.

■ For SSO clients, Cisco IDS needs to be on version 15.0(1) as there is no forward compatibility with Cisco IDS version 12.6(1) and 15.0(1) clients.

■ Before upgrading a CCE deployment with SSO to 15.0(1), install Reverse Proxy Installer 15.0(1) and IdS 15.0(1) first, and then upgrade components like Finesse or Unified Intelligence Center to 15.0(1).

■ For more information on CORS CLIs, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

■ To find a comprehensive list of the guides available for a specific release, see the Documentation Guides .

## Cisco Gateway Hardware and Software

Central Controller version 15.0(1) Model

Software Version

Call Progress Analysis for Outbound Options for SIP Trunks (CUBE)

Unified CCE and Packaged CCE Support

ASR 1001X

ASR 1002X

ASR 1006 RP2

IOS XE 17.6

Yes

Yes

IOS XE 17.9 [Last supported release]

Virtual CUBE

IOS XE 17.6

No

Yes

IOS XE 17.9

IOS XE 17.12

IOS XE 17.15

IOS XE 17.18

ISR G3 43xx (4321, 4331, 4351)

ISR G3 44xx (4431, 4451, 4461)

IOS XE 17.6

Yes

Yes

IOS XE 17.9

IOS XE 17.12 [Last supported release]

Catalyst 8200/ 8300

IOS XE 17.6

Yes

Yes

IOS XE 17.9

IOS XE 17.12

IOS XE 17.15

IOS XE 17.18

Notes

■ As the Catalyst 1000v platform is no longer supported, we recommend deploying Virtual CUBE images on Catalyst 8300 platforms.

■ All gateways in the preceding table support inbound contact center calls. For details on support for Call Progress Analysis (CPA) for Outbound Option with TDM Trunks, see the Cisco ASR 1000 Series documentation at https://www.cisco.com/c/en/us/support/routers/asr-1000-series-aggregation-services-routers/products-documentation-roadmaps-list.html

■ For IPv6-enabled deployments, the supported IOS versions for NAT64 translations are 15.4(2)T3 and later releases.

### IOS Versioning Key 16.1(4) M3 and 16.1(4) T1 as Examples

■ 16.1 is the version number.

■ (4) is the release number.

■ M3 and T1 are the train release numbers. M is the mainline train, and T is the technology train.

■ An increment in the release number after M or T refers to additional bug fixes.

### IOS-XE Versioning Key 16.12.1a and 16.12.3 as Examples

■ 16.12 is the version number.

■ 1 and 3 are the increment release numbers with additional bug fixes.

■ "a" indicates a special release.

■ Every three releases include a maintenance release incremented as 16.3, 16.6, 16.9, 16.12, 17.3, and so on.

## Cisco Unified SIP Proxy (Deprecated)

Unified CCE and Packaged CCE 15.0(1) solutions support Cisco Unified SIP Proxy (CUSP) 10.1(x) and 10.2(x) only in non-secure mode.

Notes: CUSP is deprecated. For more information, see End-of-Sale and End-of-Life Announcement for the Cisco Unified SIP Proxy Version 10 at https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-sip-proxy-software/unified-sip-proxy-v10-eol.html .

## Cisco Contact Center SIP Proxy

Unified CCE and Packaged CCE 15.0(1) solutions are compatible with Cisco Contact Center SIP Proxy (CCCSP) 15.0(1).

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

8845, 8865. 8875

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

Y

N

Y

Yes Audio only

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

Voice only

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

N

Voice only

Y

Y

Y

N

N

N

Y

Webex App for VDI

Y

N

Voice only

Y

Y

Y

N

N

N

Y

Notes

■ The phone models that are end-of-sale and end-of-software-maintenance will continue to work with Contact Center Enterprise solutions. The phone models that are end-of-support are still compatible with Contact Center Enterprise solutions, but they are neither tested nor supported by Cisco.

— For end-of-life and end-of-sale announcements, see https://www.cisco.com/c/en/us/products/eos-eol-listing.html .

— For information on a specific endpoint, see the product page of the endpoint.

■ General: Only the Cisco IP Phones listed in the preceding table are supported as contact center agent phones. As an alternative, you can deploy the Mobile Agent solution to enable the contact center to use any phone as an agent phone.

■ General: The Join Across Line (JAL) and Direct Transfer Across Line (DTAL) phone features aren’t supported and must be disabled on phones that come packaged with these features and local CTI ports (LCP) for Mobile Agent.

■ General: For any phone that allows Single-Line Mode, you can use Shared Line on a non-ACD line. You must have your PG in Single-Line Mode (set the Agent Phone Line Control setting to Single Line).

■ General: Other than call initiation, all other call control on the non-ACD extensions is supported from multiline capable desktops. Calls initiated from the hard phone can be controlled after the initial call setup.

■ 78xx: If Cisco Finesse IPPA agents use 78xx series phone, you must either disable the Cisco Finesse IPPA Inactivity Timeout feature or increase the timeout in the range of 120 seconds to one day (86400 seconds), so that the agent doesn’t get logged out of Cisco Finesse IPPA even if the agent is on any other screen.

■ 88xx phones are supported only with desktop controls in the Standard Line mode. If both desktop and device controls are required, use the Enhanced Line mode.

■ Webex:

— Point-to-Point calls are supported if the lines are registered with CUCM or via SIP URI.

— For minimum supported versions of CUCM and Expressway (for MRA deployments) to support Webex, see the Supported Unified CM Releases and the Supported Expressway Releases tables at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/wbxt/ucmcalling/unified-cm-wbx-teams-deployment-guide/unified-cm-wbx-teams-deployment-guide_chapter_011.html .

■ Jabber:

— If you are currently using Cisco Jabber for Windows, Mac, or VDI versions 12.6.x or 12.7.x, it's recommended to upgrade to the Cisco Jabber version 12.8.x or later, 14.x, or 15.x.

— Agent Greeting support for Jabber requires a minimum Cisco Jabber version 12.9.

— MRA support for Jabber requires minimum Cisco Jabber version 12.5 and Expressway 12.5. If you have VPN split-tunneling configured, you can use Jabber with MRA and the Finesse desktop on the same client machine. See https://www.cisco.com/c/en/us/support/security/anyconnect-secure-mobility-client/products-installation-and-configuration-guides-list.html for Cisco AnyConnect Mobility Client split-tunneling configuration.

— If VPN split-tunneling isn’t available, use one of the following options for the remote agents:

o A remote agent who runs Jabber with MRA on one client machine and the Finesse desktop with a VPN connection on a second client machine.

o A remote agent who runs a Jabber softphone on a laptop that is connected over MRA and runs the Finesse desktop as a Xenapp thin client on the same laptop.

— Jabber for VDI isn’t supported in Video Contact Center deployments.

— For Cisco Jabber software compatibility details, see the Planning guide for Cisco Jabber at https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

■ The phone models that are on end-of-life plan and have reached the end of maintenance for CUCM Release 14 will no longer register. For more information on the end-of-life phones, see the Field Notices at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-field-notices-list.html .

## Endpoints Supported for Callers Only

Callers outside of the enterprise's network can use the following endpoints:

■ Jabber for iOS

■ Jabber for Android

## Single Sign On (SSO) Identity Providers (IdPs)

The following AD FS versions are supported with this Unified CCE release:

■ AD FS 5.0: Windows Server 2022

■ AD FS 5.0: Windows Server 2019

■ AD FS 4.0: Windows Server 2016

■ AD FS 3.0: Windows Server 2012 R2

Besides the AD FS versions listed above, Unified CCE supports all SAML 2.0 compliant IdPs. See the documentation of your IdP for details on configuring the IdP in CCE.

Notes

- Unified CCMP, Release 15.0(1) supports Microsoft AD FS 2012 R2 and 2016 with WS-Federation via JSON Web Token (JWT).

However, user authentication access for Unified CCMP can be provided by one of the supported IdPs via Federated Trust with Microsoft AD FS. Federated Trust is supported per Microsoft AD FS and third-party IdP documentation and support.

- Kerberos is supported for single-domain authentication (non-federated environments).

- For ECE:

§ Agent-based users have the same compatibility as Cisco IDS.

§ Supervisors outside Cisco Finesse support any SAML 2.0 complaint IDP.

## Transport Layer Security

The Unified CCE database access encrypts SQL user authentication using TLS, but the data connection isn’t encrypted.

15.0(1) Component

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

SQL Gateway - DB Lookup

N/A

✔

Protocol - CTI Server and Media Routing

N/A

✔

CVP 0F [1]

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

✔

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

Mac OS X 13.7.1 or later

Chrome OS 106.0.5249 or later

Cisco Unified Intelligence Center

Microsoft Windows 10 and Windows 11 (64-bit)

Mac OS X 13.7.1 or later

Cisco Unified Call Studio

Microsoft Windows 10 (64-bit)

Microsoft Windows 11 (64-bit)

Administration Client

Microsoft Windows Server 2019 (Standard and Datacenter editions) (64-bit)

Microsoft Windows Server 2022 (Standard and Datacenter editions) (64-bit)

Microsoft Windows 10 (Enterprise and Professional) (64-bit) Microsoft Windows 11 (Enterprise and Professional) (64-bit)

Internet Script Editor (ISE)

Microsoft Windows 10 (Enterprise and Professional) (64-bit) Microsoft Windows 11 (Enterprise and Professional) (64-bit)

## Supported Browsers

Operating System

Browser Version for Release 15.0(1)

Microsoft Windows Server 2019 (Standard and Datacenter editions)

Microsoft Windows Server 2022 (Standard and Datacenter editions)

Google Chrome 126 or later

Edge Chromium 131 or later

Firefox Extended Support Release (ESR) 137 or later, including other non-ESR updates.

Microsoft Windows 10 and Windows 11 (64-bit)

Google Chrome 126 or later

Edge Chromium 131 or later

Firefox Extended Support Release (ESR) 137 or later, including other non-ESR updates.

Mac OS X

Google Chrome 126 or later

Edge Chromium 131 or later

Firefox Extended Support Release (ESR) 137 or later, including other non-ESR updates.

Note: Unified CCE Administration Client supports only Microsoft Chromium Edge browser.

## Server Operating System

Components

Server OS

Unified CCE, Packaged CCE, ICM, and System PG

Microsoft Windows Server 2019 and 2022 (Standard and Datacenter editions)

Unified CVP

Microsoft Windows Server 2019 and 2022 (Standard and Datacenter editions)

Enterprise Chat and Email

Microsoft Windows Server 2022 (Standard and Datacenter editions)

Unified CCMP

Microsoft Windows Server 2022 (Standard and Datacenter editions)

Notes

■ Unified ICM/CCE is qualified only on the retail installation of the Microsoft Windows Server (Standard and Datacenter editions). Cisco doesn't support Unified ICM/CCE on a customized Microsoft Windows image (for example, a corporate image). If you use a customized image of the Microsoft Windows operating system, the Unified ICM/CCE application can fail.

## SQL Server and Informix Versions

Components

SQL Server Version

Unified CCE, Packaged CCE, and ICM

Microsoft SQL Server 2022 (Standard and Enterprise editions) with cumulative updates

Microsoft SQL Server 2019 (Standard and Enterprise editions) with cumulative updates

Note: Contact Center Enterprise solution supports only the 64-bit version of Microsoft SQL Server. Contact Center Enterprise solution does not support the following:

■ Encrypted connections to SQL Server.

■ Linked Server feature of SQL Server.

Unified CVP Reporting Server

IBM Informix Dynamic Server Version 14.10.FC10W2 with 15.0(1)

IBM Informix Dynamic Server Version 14.10.FC12W5 with 15.0(1) ES202603

Enterprise Chat and Email

■ ECE 400 agent deployment: Microsoft SQL Server 2022(Standard and Enterprise editions)

■ ECE 2500 agent deployment: Microsoft SQL Server 2022 (Standard and Enterprise editions)

■ ECE Geographically Redundant/High Availability installation: Microsoft SQL Server 2022 (Enterprise edition)

Unified CCMP

Microsoft SQL Server 2022 (Standard and Enterprise editions)

Note: For CCE components, the combination of Windows Server 2019 with SQL Server 2022, or Windows Server 2022 with SQL Server 2019 is not supported.

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

Portuguese (Brazil)

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

■ Unified CCE supports multilingual versions of Microsoft Windows Server (English Windows Server with language packs installed). For details about how to set up multilingual versions of Microsoft Windows Server, see the http://www.cisco.com/en/US/products/sw/custcosw/ps1844/prod_installation_guides_list.html .

■ Use English SQL Server on multilingual versions of the Microsoft Windows Server environment. These are examples of supported multilingual environments:

— English Windows Server with Japanese Windows language pack installed, and English SQL Server with Japanese SQL Collation Setting.

— English Windows Server with Russian Windows language pack installed, and English SQL Server with Cyrillic_General SQL Collation Setting.

## Java, JDK, and Tomcat

CCE Solutions & Applications

Tomcat

Java Versions

Application

Platform

Unified CCE/Packaged CCE

9.0.98

21.0.11

21.0.11

9.0.111 (updated for ES202511)

21.0.11

21.0.11

Unified CVP

9.0.98

17.0.18

17.0.18

9.0.106 (updated for ES202508)

Cisco Enterprise Chat and Email

N/A

21.0

21.0

Unified CCMP

N/A

21.0

21.0

Customer Collaboration Platform

9.0.88

1.8.0 Update 362, 64-bit build

1.8.0 Update 362, 64-bit build

Cloud Connect

9.0.88

17.0.16-25

17.0.16-25

Unified Intelligence Center, Live Data, and Cisco IdS

9.0.88

17.0.10.0.7-1

1.8.0 Update 362-b09, 64-bit build

Cisco VVB

9.0.88

17.0.10.0.7-1

1.8.0 Update 362-b09, 64-bit build

Cisco Finesse

9.0.88

17.0.10.0.7-1

1.8.0 Update 362-b09, 64-bit build

For instructions on applying newer Java security updates, see the Security Guide for Cisco Unified ICM/Contact Center Enterprise guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

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

■ Microsoft Windows Server 2019 (Standard and Datacenter editions) comes with pre-installed .NET version 4.7.2.

■ Microsoft Windows Server 2022 (Standard and Datacenter editions) comes with pre-installed .NET version 4.8.

■ Unified CCE and Administration Client, installs .NET version 4.8.

■ Unified CVP automatically installs .NET version 3.5 by default on Microsoft Windows Server 2019, as this version comes pre-installed.

■ Unified CVP automatically installs .NET version 4.8 by default on Microsoft Windows Server 2022.

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

■ Desktop solutions are only supported on PC-like devices that utilize a keyboard and mouse. Tablets and mobile devices aren’t currently supported.

■ Verify that the bandwidth and deployment considerations of the solution meet the performance and timing requirements.

■ Cisco Unified Contact Center Enterprise Administration isn’t supported on virtual desktops.

## Hypervisor compatibility

### VMWare ESXI Compatibility

For information on the VMware ESXi versions compatible with Unified CCE solution components see Cisco Collaboration Virtualization at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html .

### Nutanix Compatibility

Cisco validated the CCE deployment on the following Nutanix software versions:

Software

Version

Nutanix Cloud Infrastructure (NCI)

7.5

Prism Central

7.5.1.4

Nutanix AOS (Acropolis Operating System)

7.5.0.6

Nutanix AHV (Acropolis Hypervisor)

11.0.0.2

## Automatic Speech Recognition and Text to Speech

Note: Cisco does not test consecutive Nuance Service Packs and relies on Nuance to follow standard release practices and avoid making significant changes or updates in Service Pack releases. As Service Packs typically contain defect fixes, enhancements, and improvements, Nuance highly recommends keeping up to date with Service Packs and staying within a supported release according to their "On Premise Service Pack Deprecation and Support Policy." Nuance Support should be contacted should any issues arise with a Service Pack application, and a rollback plan be in place for any updates, as per industry’s best practices.

Category

Requirements

Nuance Speech Suite 11.0.x

Note: Cisco Virtualized Voice Browser (VVB) supports the Nuance components compatible with MRCP Protocol v1 and v2. For further details on compatibility, see the Nuance Compatibility Matrix.

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

Note: For specific interfaces where you can use load balancers in your deployment, see the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html .

### ICM-to-ICM Gateway Compatibility

ICM Client

ICM Server

15.0

15.0

15.0

12.6

15.0

12.5

12.6

15.0

12.5

15.0

### Third Party ACDs

#### Avaya

Avaya PG is no longer supported in version 15.0(1). If you plan to migrate Avaya PG Agents to a Unified CCE PG, you can use the Avaya PG installer on CCE version 12.5(x) or 12.6(x) with the 15.0(1) CCE Central Controller.

For more information, see the Avaya section in the following Compatibility Matrices:

· Contact Center Enterprise Solution Compatibility Matrix, Release 12.6(x) and at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/ucce_compatibility/matrix/Contact_Center_Enterprise_Solution_Compatibility_Matrix_Release_12_6.html#_Toc217399622

· Contact Center Enterprise Solution Compatibility Matrix, Release 12.5(x) and at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/ucce_compatibility/matrix/Contact_Center_Enterprise_Solution_Compatibility_Matrix_Release_12_5.html#_Toc161643388

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

© 2025 Cisco Systems, Inc. All rights reserved.

[1] For more information, check the Release Notes at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html .

| PCCE/UCCE Components, Release 15.0(1) | PCCE/UCCE Components, Release 12.6(x) |
|---|---|
| Cisco Reverse Proxy | Cloud Connect | IdS (Standalone) | Finesse | ECE | CVP | VVB | CUIC (Standalone) | CUIC-LiveData-IdS (Coresident) | Router | Logger | AW | Live Data (Standalone) | PG | Customer Collaboration Platform | CCMP | Notes |
| Cisco Reverse Proxy |  | Y | Y | Y | Y |  |  | Y | Y |  |  |  | Y |  |  |  |  |
| Cloud Connect | N |  | Y | Y |  | Y | Y | Y | Y | Y | Y | Y | Y | Y |  |  |  |
| Identity Server (Standalone) | N | N |  | Y | Y |  |  | Y |  |  |  | Y | Y |  |  |  |  |
| Finesse | N | N | N |  | Y |  |  | Y | N |  |  | Y | Y | Y | Y |  | When Cisco Finesse is on 15.0(1) and CUIC is on 12.6(2), install CUIC 12.6(2) ES04 or later on all CUIC nodes for the CUIC gadgets to load. Finesse 15.0(1) and CUIC 12.6(1) are not compatible. |
| CVP |  |  |  |  |  |  | Y |  |  | Y | Y | Y |  | Y |  |  |  |
| VVB |  |  |  |  |  | Y |  |  |  |  |  |  |  |  |  |  |  |
| CUIC (Standalone) | N | N | N | N |  |  |  |  |  |  |  | Y | Y |  |  |  |  |
| CUIC-LiveData-IdS (Coresident) | N | N |  | N |  |  |  |  |  | Y |  | Y |  | Y |  |  | 12.6(2) AW is compatible with 15.0(1) Coresident, but 12.6(1) AW is not. |
| Router |  |  |  |  |  | N |  |  | N |  |  |  | N | Y | Y | N |  |
| Logger |  |  |  |  |  | N |  |  |  |  |  |  |  | Y | Y | N |  |
| AW |  |  | N | N | N | N |  | N | N |  |  |  | N | Y | Y | N |  |
| Live Data (Standalone) | N |  |  | N |  |  |  | N |  | Y | Y | Y |  | Y |  |  | 12.6(2) AW is compatible with 15.0(1) Live Data, but 12.6(1) AW is not. |
| PG |  |  |  | N | N | N |  |  | N | N | N | N | N |  | Y |  |  |

| PCCE/UCCE Components, Release 15.0(1) | PCCE/UCCE, Release 12.6(x) |
|---|---|
| Cisco Reverse Proxy | Cloud Connect | IdS (Standalone) | Finesse | ECE | CVP | VVB | CUIC (Standalone) | CUIC-LiveData-IdS (Coresident) | Router | Logger | AW | Live Data (Standalone) | PG | Customer Collaboration Platform | CCMP | Notes |
| ECE | N |  | N | Y |  |  |  |  | N |  |  | Y |  | Y |  |  |  |
| CCMP |  |  |  |  |  | Y |  |  |  | Y | Y | Y |  |  |  |  | Not applicable to Packaged CCE. |

| PCCE/UCCE Components, Release 15.0(1) | PCCE/UCCE Components, Release 12.5(x) |
|---|---|
| IdS (Standalone) | Finesse | ECE | CVP | VVB | CUIC (Standalone) | CUIC-LiveData-IdS (Coresident) | Router | Logger | AW | Live Data (Standalone) | PG | Customer Collaboration Platform | CCMP | Notes |
| Cloud Connect | Y | Y |  | Y | Y | Y | Y | Y | Y | Y | Y | Y |  |  |  |
| Identity Server (Standalone) |  | Y | Y |  |  | Y |  |  |  | Y | Y |  |  |  |  |
| Finesse | N |  | Y |  |  | N | N |  |  | Y | Y | Y | Y |  | When Cisco Finesse is on 15.0(1) and CUIC is on 12.5(2), CUIC gadgets will not load in Finesse. Finesse 15.0(1) and CUIC 12.5(1) are not compatible. |
| CVP |  |  |  |  | Y |  |  | Y | Y | Y |  | Y |  |  |  |
| VVB |  |  |  | Y |  |  |  |  |  |  |  |  |  |  |  |
| CUIC (Standalone) | N | N |  |  |  |  |  |  |  | Y | Y |  |  |  |  |
| CUIC-LiveData-IdS (Coresident) |  | N |  |  |  |  |  | N |  | N |  | Y |  |  |  |
| Router |  |  |  | N |  |  | N |  |  |  | N | Y | Y | N |  |
| Logger |  |  |  | N |  |  |  |  |  |  |  | Y | Y | N |  |
| AW | N | N | N | N |  | N | N |  |  |  | N | Y | Y | N |  |
| Live Data (Standalone) |  | N |  |  |  | N |  | N | N | N |  | Y |  |  |  |
| PG |  | N | N | N |  |  | N | N | N | N | N |  | Y |  |  |

| PCCE/UCCE Components, Release 15.0(1) | PCCE/UCCE, Release 12.5(x) |
|---|---|
| IdS (Standalone) | Finesse | ECE | CVP | VVB | CUIC (Standalone) | CUIC-LiveData-IdS (Coresident) | Router | Logger | AW | Live Data (Standalone) | PG | Customer Collaboration Platform | CCMP | Notes |
| ECE | N | Y |  |  |  |  | N |  |  | Y |  | Y |  |  |  |
| CCMP |  |  |  | Y |  |  |  | Y | Y | Y |  |  |  |  | Not Applicable to Packaged CCE. |

| Central Controller version 15.0(1) Model | Software Version | Call Progress Analysis for Outbound Options for SIP Trunks (CUBE) | Unified CCE and Packaged CCE Support |
|---|---|---|---|
| ASR 1001X ASR 1002X ASR 1006 RP2 | IOS XE 17.6 | Yes | Yes |
| IOS XE 17.9 [Last supported release] |
| Virtual CUBE | IOS XE 17.6 | No | Yes |
| IOS XE 17.9 |
| IOS XE 17.12 |
| IOS XE 17.15 |
| IOS XE 17.18 |
| ISR G3 43xx (4321, 4331, 4351) ISR G3 44xx (4431, 4451, 4461) | IOS XE 17.6 | Yes | Yes |
| IOS XE 17.9 |
| IOS XE 17.12 [Last supported release] |
| Catalyst 8200/ 8300 | IOS XE 17.6 | Yes | Yes |
| IOS XE 17.9 |
| IOS XE 17.12 |
| IOS XE 17.15 |
| IOS XE 17.18 |

| Endpoint | Voice & Finesse Desktop | Video | Unified CM Silent Monitor | BIB-based recording | Agent Greeting | Whisper Announcements | Finesse IP Agent Phone | IPv6 SCCP (UCCE Only) | IPv6 SIP | MRA |
|---|---|---|---|---|---|---|---|---|---|---|
| 7821, 7841, 7861 | Y | N | Y | Y | Y | Y | Y | N | Y | Yes Audio Only |
| 7942G,7945G, 7962G,7965G, 7975G | Y | N | Y | Y | Y | Y | N | Y | N | N |
| 8811, 8821, 8841, 8851, 8851NR, 8861 | Y | N | Y | Y | Y | Y | Y | N | Y | Yes Audio Only |
| 8845, 8865. 8875 | Y | Y | Y | Y | Y | Y | Y | Y | Y | Yes Audio Only |
| 9841, 9851, 9861, 9871 | Y | N | Y | Y | Y | Y | Y | N | Y | Yes Audio only |
| Jabber for Mac | Y | Y | Voice only | Y | N | Y | N | N | N | Y |
| Jabber for VDI | Y | N | Voice only | Y | Y | Y | N | N | N | Y |
| Jabber for Windows | Y | Y | Voice-only | Y | Y | Y | N | N | N | Y |
| Webex App for MacOS/Windows | Y | N | Voice only | Y | Y | Y | N | N | N | Y |
| Webex App for VDI | Y | N | Voice only | Y | Y | Y | N | N | N | Y |

| 15.0(1) Component | TLS 1.2 |
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
| SQL Gateway - DB Lookup | N/A | ✔ |
| Protocol - CTI Server and Media Routing | N/A | ✔ |
| CVP 0F [1] | ✔ | N/A |
| VVB | ✔ | N/A |
| IdS | ✔ | N/A |
| Finesse | ✔ | ✔ |
| CUIC | ✔ | ✔ |
| ECE | ✔ | ✔ |
| Live Data | ✔ | N/A |
| Customer Collaboration Platform | ✔ | N/A |
| CCMP | ✔ | ✔ |
| ACD | X | N/A |
| UC Manager | ✔ | N/A |

| Components | Clients OS |
|---|---|
| Cisco Finesse | Microsoft Windows 10 and Windows 11 (64-bit) |
| Mac OS X 13.7.1 or later |
| Chrome OS 106.0.5249 or later |
| Cisco Unified Intelligence Center | Microsoft Windows 10 and Windows 11 (64-bit) |
| Mac OS X 13.7.1 or later |
| Cisco Unified Call Studio | Microsoft Windows 10 (64-bit) Microsoft Windows 11 (64-bit) |
| Administration Client | Microsoft Windows Server 2019 (Standard and Datacenter editions) (64-bit) Microsoft Windows Server 2022 (Standard and Datacenter editions) (64-bit) |
| Microsoft Windows 10 (Enterprise and Professional) (64-bit) Microsoft Windows 11 (Enterprise and Professional) (64-bit) |
| Internet Script Editor (ISE) | Microsoft Windows 10 (Enterprise and Professional) (64-bit) Microsoft Windows 11 (Enterprise and Professional) (64-bit) |

| Operating System | Browser Version for Release 15.0(1) |
|---|---|
| Microsoft Windows Server 2019 (Standard and Datacenter editions) Microsoft Windows Server 2022 (Standard and Datacenter editions) | Google Chrome 126 or later |
| Edge Chromium 131 or later |
| Firefox Extended Support Release (ESR) 137 or later, including other non-ESR updates. |
| Microsoft Windows 10 and Windows 11 (64-bit) | Google Chrome 126 or later |
| Edge Chromium 131 or later |
| Firefox Extended Support Release (ESR) 137 or later, including other non-ESR updates. |
| Mac OS X | Google Chrome 126 or later |
| Edge Chromium 131 or later |
| Firefox Extended Support Release (ESR) 137 or later, including other non-ESR updates. |

| Components | Server OS |
|---|---|
| Unified CCE, Packaged CCE, ICM, and System PG | Microsoft Windows Server 2019 and 2022 (Standard and Datacenter editions) |
| Unified CVP | Microsoft Windows Server 2019 and 2022 (Standard and Datacenter editions) |
| Enterprise Chat and Email | Microsoft Windows Server 2022 (Standard and Datacenter editions) |
| Unified CCMP | Microsoft Windows Server 2022 (Standard and Datacenter editions) |

| Components | SQL Server Version |
|---|---|
| Unified CCE, Packaged CCE, and ICM | Microsoft SQL Server 2022 (Standard and Enterprise editions) with cumulative updates Microsoft SQL Server 2019 (Standard and Enterprise editions) with cumulative updates Note: Contact Center Enterprise solution supports only the 64-bit version of Microsoft SQL Server. Contact Center Enterprise solution does not support the following: ■ Encrypted connections to SQL Server. ■ Linked Server feature of SQL Server. |
| Unified CVP Reporting Server | IBM Informix Dynamic Server Version 14.10.FC10W2 with 15.0(1) |
| IBM Informix Dynamic Server Version 14.10.FC12W5 with 15.0(1) ES202603 |
| Enterprise Chat and Email | ■ ECE 400 agent deployment: Microsoft SQL Server 2022(Standard and Enterprise editions) ■ ECE 2500 agent deployment: Microsoft SQL Server 2022 (Standard and Enterprise editions) ■ ECE Geographically Redundant/High Availability installation: Microsoft SQL Server 2022 (Enterprise edition) |
| Unified CCMP | Microsoft SQL Server 2022 (Standard and Enterprise editions) |

| Microsoft Windows Server | Microsoft SQL Server | SQL Collation Setting |
|---|---|---|
| Danish |  | Latin1_General |
| Dutch |  |
| Finnish |  |
| French | French |
| German | German |
| Italian | Italian |
| Norwegian |  |
| Portuguese (Brazil) | Portuguese (Brazil) |
| Spanish | Spanish |
| Swedish |  |
| Chinese (simplified) | Chinese (simplified) | Chinese_PRC |
| Chinese (traditional) | Chinese (traditional) | Chinese_Taiwan_Stroke |
| Japanese | Japanese | Japanese |
| Korean | Korean | Korean_Wansung |
| Polish |  | Polish |
| Russian |  | Cyrillic_General |
| Turkish |  | Turkish |

| CCE Solutions & Applications | Tomcat | Java Versions |
|---|---|---|
| Application | Platform |
| Unified CCE/Packaged CCE | 9.0.98 | 21.0.11 | 21.0.11 |
| 9.0.111 (updated for ES202511) | 21.0.11 | 21.0.11 |
| Unified CVP | 9.0.98 | 17.0.18 | 17.0.18 |
| 9.0.106 (updated for ES202508) |
| Cisco Enterprise Chat and Email | N/A | 21.0 | 21.0 |
| Unified CCMP | N/A | 21.0 | 21.0 |
| Customer Collaboration Platform | 9.0.88 | 1.8.0 Update 362, 64-bit build | 1.8.0 Update 362, 64-bit build |
| Cloud Connect | 9.0.88 | 17.0.16-25 | 17.0.16-25 |
| Unified Intelligence Center, Live Data, and Cisco IdS | 9.0.88 | 17.0.10.0.7-1 | 1.8.0 Update 362-b09, 64-bit build |
| Cisco VVB | 9.0.88 | 17.0.10.0.7-1 | 1.8.0 Update 362-b09, 64-bit build |
| Cisco Finesse | 9.0.88 | 17.0.10.0.7-1 | 1.8.0 Update 362-b09, 64-bit build |

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

| Software | Version |
|---|---|
| Nutanix Cloud Infrastructure (NCI) | 7.5 |
| Prism Central | 7.5.1.4 |
| Nutanix AOS (Acropolis Operating System) | 7.5.0.6 |
| Nutanix AHV (Acropolis Hypervisor) | 11.0.0.2 |

| Category | Requirements |
|---|---|
| Nuance Speech Suite 11.0.x | Note: Cisco Virtualized Voice Browser (VVB) supports the Nuance components compatible with MRCP Protocol v1 and v2. For further details on compatibility, see the Nuance Compatibility Matrix. |
| MRCP Protocol Version | v1 and v2 |
| VoiceXML Protocol Version | 2.0 |

| ICM Client | ICM Server |
|---|---|
| 15.0 | 15.0 |
| 15.0 | 12.6 |
| 15.0 | 12.5 |
| 12.6 | 15.0 |
| 12.5 | 15.0 |