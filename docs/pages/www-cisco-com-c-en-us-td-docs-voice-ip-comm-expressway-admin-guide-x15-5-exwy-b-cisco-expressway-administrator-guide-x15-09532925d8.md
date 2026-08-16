---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-admin-guide-x15-5-exwy-b-cisco-expressway-administrator-guide-x15-09532925d8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/admin_guide/X15-5/exwy_b_cisco-expressway-administrator-guide-x155/exwy_m_introduction.html
retrieved_at: 2026-08-16T22:24:03.199462+00:00
---

Cisco Expressway Administrator Guide (X15.5)

# Cisco Expressway Administrator Guide (X15.5)

Updated: February 9, 2026

Chapter: Introduction

## Chapter: Introduction

# Introduction

## About the Expressway

Cisco Expressway Series (Expressway) is designed specifically for comprehensive
                           			collaboration services. It features established firewall-traversal technology and helps
                           			to redefine traditional enterprise collaboration boundaries, to support our Cisco vision
                           			of any-to-any collaboration.

Expressway offers the following primary features and benefits:

Provides proven, highly secure, firewall-traversal technology.

Facilitates connections for business-to-business, business-to-consumer, and
                                 					business-to-cloud-service-provider.

Facilitates session-based access to collaboration services for remote workers,
                                 					with no need for a separate VPN client.

Supports a wide range of devices, including Cisco Jabber for smartphones,
                                 					tablets, and desktops.

Complements bring-your-own-device strategies and policies for remote and mobile
                                 					workers.

A typical Expressway system is deployed as a pair: an Expressway-C with a trunk and
                           			line-side connection to Unified CM, and an Expressway-E deployed in the DMZ and
                           			configured with a traversal zone to an Expressway-C.

Expressway is available on a dedicated physical appliance such as a CE1200, or as a virtual machine (VM) on a Cisco UCS server.

### Expressway Types

Each Expressway can be configured as one of two types, which offer different
                                 				capabilities.

#### Expressway-C

Expressway-C delivers any-to-any enterprise wide conference and session management
                                 				and interworking capabilities. It extends the reach of telepresence conferences by
                                 				enabling interworking between Session Initiation Protocol (SIP)- and H.323-compliant
                                 				endpoints, interworking with third-party endpoints; it integrates with Unified CM
                                 				and supports third-party IP private branch exchange (IP PBX) solutions. Expressway-C
                                 				implements the tools required for creative session management, including definition
                                 				of aspects such as routing, dial plans, and bandwidth usage, while allowing
                                 				organizations to define call-management applications, customized to their
                                 				requirements.

#### Expressway-E

The Expressway-E deployed with the Expressway-C enables smooth video communications
                                 				easily and securely outside the enterprise. It enables business-to-business video
                                 				collaboration, improves the productivity of remote and home-based workers, and
                                 				enables service providers to provide video communications to customers. The
                                 				application performs securely through standards-based and secure firewall traversal
                                 				for all SIP and H.323 devices. As a result, organizations benefit from increased
                                 				employee productivity and enhanced communication with partners and customers.

It uses an intelligent framework that allows endpoints behind firewalls to discover
                                 				paths through which they can pass media, verify peer-to-peer connectivity through
                                 				each of these paths, and then select the optimum media connection path, eliminating
                                 				the need to reconfigure enterprise firewalls.

The Expressway-E is built for high reliability and scalability, supporting
                                 				multivendor firewalls, and it can traverse any number of firewalls regardless of SIP
                                 				or H.323 protocol.

### Standard Features

Standard features on Expressway include the following:

Secure firewall traversal and session-based access to Cisco Unified
                                       						Communications Manager for remote workers, without the need for a separate
                                       						VPN client

Endpoint registration support.

SIP Registrar (requires Room or Desktop SIP Proxy. Note that SIP and H.323 protocols are
                                       						disabled by default on new installs, and can be enabled from Configuration > Protocols Registration licenses.)

SIP and H.323 support, including SIP / H.323 interworking

IPv4 and IPv6 support, including IPv4 / IPv6 interworking

TURN relay licenses

Advanced networking

Device provisioning and FindMe services

H.323 gatekeeper

QoS tagging

Bandwidth management on both a per-call and a total usage basis, configurable
                                       						separately for calls within the local subzones and to external systems and
                                       						zones

Automatic downspeeding option for calls that exceed the available
                                       						bandwidth

URI and ENUM dialing via DNS, enabling global connectivity

Rich media session (RMS) support

1000 external zones with up to 2000 matches

1000 subzones and supporting up to 3000 membership rules

Flexible zone configuration with prefix, suffix and regex support

Can function as a standalone Expressway, or be neighbored with other systems
                                       						such as other Expressways, gatekeepers and SIP proxies

Can be clustered with up to 6 Expressways to provide n+1 redundancy, and up to 4 x individual capacity.

Can be clustered with up to 6 Expressways to provide n+2 redundancy, and up to 4 x individual capacity.

Intelligent Route Director for single number dialing and network failover
                                       						facilities

Optional endpoint authentication

Control over which endpoints are allowed to register

Call Policy (also known as Administrator Policy) including support for
                                       						CPL

Support for external policy servers

Can be managed with Cisco TelePresence Management Suite 13.2 or later

Active Directory authentication

Pre-configured neighbor zone defaults for Cisco Unified Communications
                                       						Manager and for Nortel Communication Server

Embedded setup wizard using a serial port for initial configuration

System administration using a web interface or SSH, or via the CIMC port for a CE nnnn physical appliance

Intrusion protection

### Do Not Install Other Cisco or Third-Party Software onto Expressway

Cisco does not support the installation of any additional Cisco or third-party
                                 				software, applications, or agents on Expressway (VMs or physical appliances), unless
                                 				we state explicitly otherwise. Non-Expressway products may corrupt the Expressway
                                 				code and must not be installed.

### Hardware Appliance and Virtual Machine Options

Expressway supports on-premises and cloud applications and is available as a
                                 				dedicated appliance or as a virtualized application on VMware, with additional
                                 				support for Cisco Unified Computing System (Cisco UCS) platforms.

#### Virtual Machine Options

Expressway has these virtualized application deployment types:

Small (for Cisco Business Edition 6000 or supported VMware ESXi platforms,
                                       						subject to the required minimum hardware specification)

Medium (standard installation)

Large (extra performance and scalability capabilities)

See Cisco Expressway Virtual Machine Installation Guide on the Expressway Installation Guides page.

#### Hardware CE Series Appliances

The Expressway is also available as a dedicated CE Series appliance based on UCS
                                 				hardware. For example, the CE1200 appliance based on a UCS C220 M5L, operates as a
                                 				medium capacity or large capacity Expressway.

The Cisco VCS series is not supported on CE1200 appliances.

Changing the default system size

For appliances deployed as Expressway-E you can manually change the default system
                                 				size of appliances from Large to Medium, or the other way round. This capability was
                                 				introduced to mitigate an issue with demultiplexing ports for media traversal on
                                 				appliances with a 1 Gbps NIC (SFP module) that are configured as Medium systems.

To change the size of the appliance, go to System > Administration settings page and select the required size from the Deployment Configuration list.

#### Installation information

See Cisco Expressway CE1200 Appliance Installation Guide on the Expressway Installation Guides page.

#### Limitation

##### Medium Appliances with 1 Gbps NIC - Demultiplexing Ports

If you upgrade a Medium appliance with a 1 Gbps NIC to X8.10 or later, Expressway / Cisco VCS automatically converts the system to a Large system. This means that Expressway-E / Cisco VCS Expressway listens for multiplexed RTP/RTCP traffic on the default demultiplexing ports for Large systems (36000 to 36011) and not on
                                    the demultiplexing ports configured for Medium systems. In this case, the Expressway-E / Cisco VCS Expressway drops the calls because ports 36000 to 36011 are not open on the firewall.

##### Workaround

From X8.11.4 you can manually change the system size back to Medium, through the System > Administration settings page (select Medium from the Deployment Configuration list).

Before X8.11.4, the workaround is to open the default demultiplexing ports for Large systems on the firewall.

## About This Guide

This guide describes the various features, services, and capabilities of Expressway. It
                           			assumes a fully equipped version of Expressway, so your deployment may not support all
                           			of the items described.

The guide only applies to the Cisco Expressway Series product. For information about Cisco VCS, please refer to the X12.5.x Cisco VCS Administrator Guide on the Cisco TelePresence Video Communication Server Maintain and Operate Guides page.

Most configuration tasks on Expressway can be done through the web user interface or the
                           			command line interface (CLI). The guide mainly describes how to use the web user
                           			interface. Some features are only available through the CLI, and these are described
                           			where relevant.

Web user interface directions are shown in the format Menu > Submenu followed by the Name of the page that you will be
                           			taken to.

CLI commands where provided, are shown in the format:

```
xConfiguration <Element> <SubElement>
xCommand <Command>
```

### Change History

Date

Change

Reason

April  2026

First published for X15.5.

Included a new topic "Managing the Expressway Client Certificate".

X15.5  release

February 2026

First published for X15.4.

Addressed a few defects:

On the Maintenance > Email notifications page, the SMTP Server field and the SMTP Port field can now handle proxy or relay
                                             strings.

X15.4  release

August  2025

First published for X15.3.

Addressed a few defects:

Removed the section "Jabber Guest" and occurrances of "Jabber Guest" from the guide.

Removed references to "Hybrid Services & Connector Management".

Rephrased a portion of the content on Call History.

Updated the Capacity guidelines for small deployment.

X15.3  release

February 2025

Republishing X15.2.

Addressed a defect. Replaced the existing content "CSRF Protection is Disabled by default." with "The CSRF Protection is Enabled
                                             by default," The change is made in the "Expressway Interfaces" chapter, "About the API" section, "Cross-Site Request Forgery
                                             Protection Header" section.

X15.2 release

October  2024

First published for X15.2.

Introduced a few xConfiguration commands:

xConfiguration MRACookieConfig Httponly

xConfiguration MRACookieConfig Expiry

Updated the following:

Replaced the default port value of the "xConfiguration SIP Advanced SipTlsDhKeySize: <1024/2048/3072>" from 1024 to 2048.

Implementation of default access for API use for admin needs to be disabled on GUI and CLI.

Expressway shall check for poll validation fields in ntpd servers from ntp-4.2.8p18.

Addressed a few Customer Defects.

Corrected the "Verify System key command" from /sbin/verify-skey to /sbin/verify-syskey

Expressway to send RSA algorithm as default algorithm during TLSv1.3 negotiation.

Default Ciphers list for fresh install and upgrades.

X15.2  release

December 2023

First published for X15.0.

Enabling/Disabling the Cross-Site Request Forgery (CSRF) Protection Header

Enable PreRoutedRouteHeader (PRRH) on the Expressway Select image

LDAP TLS supports different ports other than 636 and 3269

Banned ciphers are removed that are offered by default: TLS_DHE_RSA_WITH_AES_128_CCM, TLS_RSA_WITH_AES_256_CCM, TLS_RSA_WITH_AES_128_CCM

WebRTC session counter on Web User Interface for Expressway-E.

Addressed Customer Defects

Log rotation stops in the Expressway

X15.0  release

June 2023

First published for X14.3.

Updated the following tables "Capacity Guidelines for Standalone Systems, Capacity Guidelines for Clustered Systems, and Fast
                                                   Path Registration for MRA (Caching Optimization for Registrations)" in chapter "Expressway Capacity and Sizing".

Removed the tables, Standalone Systems, Capacity Guidelines for Clustered Systems, and Fast Path Registration for MRA (Caching
                                                   Optimization for Registrations) from the chapter "Clustering and Peers." Provided a link to the chapter "Expressway Capacity
                                                   and Sizing" for details.

Support for Elliptic Curve Digital Signature Algorithm (ECDSA) Certificate, Update to the Command Line Interface

Route calls to US Suicide Prevention Hotline (988) without RMS licenses

Set the Default Value of SIP TLS DH key size to 2048 for Fresh Install and Upgrade

X14.3 release

August 2022

Republished X14.2.

Replaced Bug ID

X14.2 release

August 2022

First published for X14.2.

Smart Licensing Export Compliance - Capped at 2500 encrypted signaling sessions to endpoints

New REST API - CDB Rest API Access - Enable/Disable CDB REST API Access

TLS Verification Mode - Enabled server certificate verification by default

TLS 1.3 Support

ECDSA Cipher Preference Over RSA

Alternate Method of Using xCommand FIPS

Reducing Email Notifications

XCP Routing Table

Support for 4+1 and 5+1 Redundancy Models

X14.2 release

July 2021

Updates for X14.0.2.

Updated the section "Certificate Requirements". Traffic Server Enforces Certificate Verification

New REST API - Status - fail2banbannedaddress

Auto Created CE Zone Status

X14.0.2 release

June 2021

Updates for X14.0.1.

Updated a few security related enhancements, MRA Registration issues using a wrong Traversal Zone are fixed

New REST API - Alarms - view and acknowledge, SNMP Configuration

X14.0.1 release

May 2021

Changed the MRA Registrations (proxied) value for CE1200 in the Table - Standalone Capacity Guidelines - Single Expressway.

Document correction

April 2021

First published for X14.0.

X14.0 release

December 2020

Updates for X12.7.

X12.7 release

October 2020

Update missing and out of date settings in pre-configured zones.

Remove duplicated content about HSM.

Clarify external/third party gatekeeper meaning in RMS license usage.

Document corrections

October 2020

Update missing and out of date settings in pre-configured zones.

Document correction

October 2020

Updates for X12.6.4 maintenance release (fix for software bug ID CSCvv92477 - configurable DH key length for H.323-SIP interworking).

Changes to Configuring Password Security topic to reflect that Enforce strict passwords applies to all locally-managed accounts since X12.6, not just to local admin accounts.

X12.6.4 maintenance release / document correction

August 2020

Updates for X12.6.2 maintenance release.

X12.6.2 maintenance release

July 2020

Restructure content related to logging and serviceability and integrate content that was formerly in the Expressway Serviceability
                                             Guide and is now merged into this guide. Also restructure troubleshooting and diagnostics information into its own chapter.

Document reorganization

July 2020

Updates for X12.6.1 maintenance release including MRA registrations count; and Expressway-E TURN server no longer functions
                                             as a generic STUN server.

X12.6.1 maintenance release

June 2020

Update Firewall Traversal section to explain cases of IP address mismatch in STUN packets.

Document clarification

June 2020

Updates for X12.6, add process to restore "Applications" menu if not visible in web UI.

X12.6 release

February 2020

Updates for X12.5.7 maintenance release including "Kari's Law" .

X12.5.7 now withdrawn and replaced with X12.5.9.

Clarify option keys for CE1200 appliances.

X12.5.7 maintenance release

January 2020

Update Cluster License Usage and Capacity Guidelines section to clarify no capacity gain from clustering Small VMs.

Document correction

December 2019

Clarify not to install other software onto the product.

Correct location of VM Size field.

Document clarification

Document correction

November 2019

Updates for X12.5.6 maintenance release.

X12.5.6 maintenance release

July 2019

Updated for X12.5.4. Removed references to release key as it is not required to upgrade a system on X8.6.x or later software
                                             to 12.5.4 or later.

Fix incorrect default value for "Redirect HTTP requests to HTTPS" in the Network Services section. CSCvq39362 refers.

X12.5.4 release

June 2019

RMS license consumption table updated, now includes only those scenarios which consume RMS licenses.

Document correction

May 2019

Fix incorrect reference to 488 response code in the description of Meeting Server load balancing setting.

Document correction

April 2019

Updates for X12.5.2 maintenance release (includes support for virtualized Small VMs on VMware ESXi platform).

X12.5.2 maintenance release

March 2019

Updates for X12.5.1 maintenance release.

X12.5.1 maintenance release

February 2019

Reinstate "Services That Can be Hosted Together" table in the Introduction.

Documentation correction

January 2019

Updates for X12.5.

X12.5 release

December 2018

Retitle for X8.11.4 (no substantive updates). Adjust B2BUA calls status section for CSCvn73111.

X8.11.4 maintenance release

October 2018

Updates for X8.11.3 maintenance release.

X8.11.3 maintenance release (withdrawn)

September 2018

Updated for Webex and Spark platform rebranding, CE1200 appliance, and X8.11.1 release.

X8.11.1 release (withdrawn)

July 2018

Updates for X8.11.

X8.11 release (withdrawn)

July 2017

Updates for X8.10.

X8.10 release

January 2017

General corrections and updates. New feature added.

X8.9.1 maintenance release

December 2016

New features and general corrections.

X8.9 release

September 2016

Help and admin guide updates including new call policy rule configuration.

X8.8.2 maintenance release

July 2016

Correction in MRA overview and Xconfig SIP Advanced CLI commands added.

X8.8 document corrections

June 2016

Updates for X8.8.

X8.8 release

April 2016

General corrections and updates. New features added.

X8.7.2 Maintenance release

February 2016

General corrections and updates. Document change history (this table) added. DNS zone parameters and alarm reference updated.

X8.7.1 Maintenance release

### Training

Training is available online and at our training locations. For more information on all the training we provide and where
                                 our training offices are located, visit www.cisco.com/go/telepresencetraining .

### Glossary

A glossary of TelePresence terms is available at: https://tp-tools-web01.cisco.com/start/glossary/ .

### Accessibility Notice

Cisco is committed to designing and delivering accessible products and
                                 				technologies.

The Voluntary Product Accessibility Template (VPAT) for Cisco Expressway is available
                                 				here:

http://www.cisco.com/web/about/responsibility/accessibility/legal_regulatory/vpats.html#telepresence

You can find more information about accessibility here:

http://www.cisco.com/web/about/responsibility/accessibility/index.html

### Related Documentation

Support videos

Videos provided by Cisco TAC engineers about certain common Expressway configuration procedures are available on the Expressway/VCS Screencast Video List page (search for "Expressway videos" )

Installation - virtual machines

Cisco Expressway Virtual Machine Installation Guide on the Expressway Installation Guides page

Installation - physical appliances

Cisco Expressway CE1200 Appliance Installation Guide on the Expressway Installation Guides page.

Basic configuration for single-box systems

Cisco Expressway Registrar Deployment Guide on the Expressway Configuration Guides page

Basic configuration for paired-box systems (firewall
                                             									traversal)

Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide on the Expressway Configuration Guides page

Administration and maintenance

Cisco Expressway Administrator Guide on the Expressway Maintain and Operate Guides page (includes Serviceability information)

Clustering

Cisco Expressway Cluster Creation and Maintenance Deployment Guide on the Expressway Configuration Guides page

Certificates

Cisco Expressway Certificate Creation and Use Deployment Guide on the Expressway Configuration Guides page

Ports

Cisco Expressway IP Port Usage Configuration Guide on the Expressway Configuration Guides page

Unified Communications

Mobile and Remote Access Through Cisco Expressway on the Expressway Configuration Guides page

Cisco Meeting Server

Cisco Meeting Server with Cisco Expressway Deployment Guide on the Expressway Configuration Guides page

Cisco Meeting Server API Reference Guide on the Cisco Meeting Server Programming Guides page

Other Cisco Meeting Server guides are available on the Cisco Meeting Server Configuration Guides page

Cisco Webex Hybrid Services

Hybrid Services Knowledge Base

Cisco Hosted Collaboration Solution (HCS)

HCS Customer Documentation

Microsoft infrastructure

Cisco Expressway with Microsoft Infrastructure Deployment Guide on the Expressway Configuration Guides page

Cisco Jabber and Microsoft Skype for Business Infrastructure Configuration Cheatsheet on the Expressway Configuration Guides page

Rest API

Cisco Expressway REST API Summary Guide on the Expressway Configuration Guides page (high-level information only as the API is self-documented)

Multiway Conferencing

Cisco TelePresence Multiway Deployment Guide on the Expressway Configuration Guides page

## About the Service Setup Wizard (Service Selection Page)

The Service Setup Wizard makes it easier to configure Expressway for its chosen purpose in your environment, and simplifies
                           the web user interface. As well as running the wizard for initial configuration you can subsequently access its service selection
                           page at any time ( Status > Overview ). For more details about using the wizard, see the Cisco Expressway-E and Expressway-C - Basic Configuration guide on the Expressway Configuration Guides page.

If you use Smart Licensing, you cannot change the Series setting from the Service Selection page/wizard (to convert an Expressway to a VCS
                                       				product). Instead this process must start with a factory reset (to disable Smart
                                       				Licensing because it's not supported on VCS). Some of the other settings shown in
                                       				this example are unnecessary with Smart Licensing and do not appear in the wizard on
                                       				Expressways that use Smart Licensing.

### Services That Can Be Hosted Together

Some services are incompatible and cannot be selected together. The following table
                                 				provides a matrix of compatible services. The matrix specifies which services you
                                 				can use together on the same system or cluster.

Cisco Webex Hybrid Services (Connectors

Mobile and Remote Access

Jabber

Microsoft gateway server

Registration

CMR Cloud

Business to Business calling (includes Hybrid Call Service)

Cisco Webex Hybrid Services (Connectors)

Y

N

N

N

N

Y

Y

Mobile and Remote Access and/or (from X8.9) Meeting Server Web Proxy

N

Y

N

N

Y

Y

Y*

Microsoft gateway service

N

N

N

Y

N

N

N

Registrar

N

Y

Y

N

Y

Y

Y

CMR Cloud

Y

Y

Y

N

Y

Y

Y

Business to Business calling (includes Hybrid Call Service)

Y

Y*

Y

N

Y

Y

Y

Key to Table

Y: Yes, these services can be hosted on the same system or cluster

N: No, these services may not be hosted on the same system or cluster

Rules

Hybrid Services connectors may co-reside with the Expressway-C of a traversal
                                       						pair used for Call Service, subject to user number limitations.

* If your Hybrid Call Service (or B2B) traversal pair is also used for MRA,
                                       						then the Hybrid Services connectors must be on a separate Expressway-C. This
                                       						is because we do not support the connectors being hosted on the Expressway-C
                                       						that is used for MRA.

Microsoft gateway service requires a dedicated VCS Control or Expressway-C (called "Gateway VCS" or "Gateway Expressway" in the help and documentation)

MRA is currently not supported in IPv6 only mode. If you want IPv6 B2B
                                       						calling to co-reside with IPv4 MRA on the same Expressway traversal pair,
                                       						the Expressway-E and Expressway-C must both be in dual stack mode.

| Note | The Cisco VCS series is not supported on CE1200 appliances. |
|---|---|

| Date | Change | Reason |
|---|---|---|
| April  2026 | First published for X15.5. Included a new topic "Managing the Expressway Client Certificate". | X15.5  release |
| February 2026 | First published for X15.4. Addressed a few defects: On the Maintenance > Email notifications page, the SMTP Server field and the SMTP Port field can now handle proxy or relay
                                             strings. | X15.4  release |
| August  2025 | First published for X15.3. Addressed a few defects: Removed the section "Jabber Guest" and occurrances of "Jabber Guest" from the guide. Removed references to "Hybrid Services & Connector Management". Rephrased a portion of the content on Call History. Updated the Capacity guidelines for small deployment. | X15.3  release |
| February 2025 | Republishing X15.2. Addressed a defect. Replaced the existing content "CSRF Protection is Disabled by default." with "The CSRF Protection is Enabled
                                             by default," The change is made in the "Expressway Interfaces" chapter, "About the API" section, "Cross-Site Request Forgery
                                             Protection Header" section. | X15.2 release |
| October  2024 | First published for X15.2. Introduced a few xConfiguration commands: xConfiguration MRACookieConfig Httponly xConfiguration MRACookieConfig Expiry Updated the following: Replaced the default port value of the "xConfiguration SIP Advanced SipTlsDhKeySize: <1024/2048/3072>" from 1024 to 2048. Implementation of default access for API use for admin needs to be disabled on GUI and CLI. Expressway shall check for poll validation fields in ntpd servers from ntp-4.2.8p18. Addressed a few Customer Defects. Corrected the "Verify System key command" from /sbin/verify-skey to /sbin/verify-syskey Expressway to send RSA algorithm as default algorithm during TLSv1.3 negotiation. Default Ciphers list for fresh install and upgrades. | X15.2  release |
| December 2023 | First published for X15.0. Enabling/Disabling the Cross-Site Request Forgery (CSRF) Protection Header Enable PreRoutedRouteHeader (PRRH) on the Expressway Select image LDAP TLS supports different ports other than 636 and 3269 Banned ciphers are removed that are offered by default: TLS_DHE_RSA_WITH_AES_128_CCM, TLS_RSA_WITH_AES_256_CCM, TLS_RSA_WITH_AES_128_CCM WebRTC session counter on Web User Interface for Expressway-E. Addressed Customer Defects Log rotation stops in the Expressway | X15.0  release |
| June 2023 | First published for X14.3. Updated the following tables "Capacity Guidelines for Standalone Systems, Capacity Guidelines for Clustered Systems, and Fast
                                                   Path Registration for MRA (Caching Optimization for Registrations)" in chapter "Expressway Capacity and Sizing". Removed the tables, Standalone Systems, Capacity Guidelines for Clustered Systems, and Fast Path Registration for MRA (Caching
                                                   Optimization for Registrations) from the chapter "Clustering and Peers." Provided a link to the chapter "Expressway Capacity
                                                   and Sizing" for details. Support for Elliptic Curve Digital Signature Algorithm (ECDSA) Certificate, Update to the Command Line Interface Route calls to US Suicide Prevention Hotline (988) without RMS licenses Set the Default Value of SIP TLS DH key size to 2048 for Fresh Install and Upgrade | X14.3 release |
| August 2022 | Republished X14.2. Replaced Bug ID | X14.2 release |
| August 2022 | First published for X14.2. Smart Licensing Export Compliance - Capped at 2500 encrypted signaling sessions to endpoints New REST API - CDB Rest API Access - Enable/Disable CDB REST API Access TLS Verification Mode - Enabled server certificate verification by default TLS 1.3 Support ECDSA Cipher Preference Over RSA Alternate Method of Using xCommand FIPS Reducing Email Notifications XCP Routing Table Support for 4+1 and 5+1 Redundancy Models | X14.2 release |
| July 2021 | Updates for X14.0.2. Updated the section "Certificate Requirements". Traffic Server Enforces Certificate Verification New REST API - Status - fail2banbannedaddress Auto Created CE Zone Status | X14.0.2 release |
| June 2021 | Updates for X14.0.1. Updated a few security related enhancements, MRA Registration issues using a wrong Traversal Zone are fixed New REST API - Alarms - view and acknowledge, SNMP Configuration | X14.0.1 release |
| May 2021 | Changed the MRA Registrations (proxied) value for CE1200 in the Table - Standalone Capacity Guidelines - Single Expressway. | Document correction |
| April 2021 | First published for X14.0. | X14.0 release |
| December 2020 | Updates for X12.7. | X12.7 release |
| October 2020 | Update missing and out of date settings in pre-configured zones. Remove duplicated content about HSM. Clarify external/third party gatekeeper meaning in RMS license usage. | Document corrections |
| October 2020 | Update missing and out of date settings in pre-configured zones. | Document correction |
| October 2020 | Updates for X12.6.4 maintenance release (fix for software bug ID CSCvv92477 - configurable DH key length for H.323-SIP interworking). Changes to Configuring Password Security topic to reflect that Enforce strict passwords applies to all locally-managed accounts since X12.6, not just to local admin accounts. | X12.6.4 maintenance release / document correction |
| August 2020 | Updates for X12.6.2 maintenance release. | X12.6.2 maintenance release |
| July 2020 | Restructure content related to logging and serviceability and integrate content that was formerly in the Expressway Serviceability
                                             Guide and is now merged into this guide. Also restructure troubleshooting and diagnostics information into its own chapter. | Document reorganization |
| July 2020 | Updates for X12.6.1 maintenance release including MRA registrations count; and Expressway-E TURN server no longer functions
                                             as a generic STUN server. | X12.6.1 maintenance release |
| June 2020 | Update Firewall Traversal section to explain cases of IP address mismatch in STUN packets. | Document clarification |
| June 2020 | Updates for X12.6, add process to restore "Applications" menu if not visible in web UI. | X12.6 release |
| February 2020 | Updates for X12.5.7 maintenance release including "Kari's Law" . Note X12.5.7 now withdrawn and replaced with X12.5.9. Clarify option keys for CE1200 appliances. | Note | X12.5.7 now withdrawn and replaced with X12.5.9. | X12.5.7 maintenance release |
| Note | X12.5.7 now withdrawn and replaced with X12.5.9. |
| January 2020 | Update Cluster License Usage and Capacity Guidelines section to clarify no capacity gain from clustering Small VMs. | Document correction |
| December 2019 | Clarify not to install other software onto the product. Correct location of VM Size field. | Document clarification Document correction |
| November 2019 | Updates for X12.5.6 maintenance release. | X12.5.6 maintenance release |
| July 2019 | Updated for X12.5.4. Removed references to release key as it is not required to upgrade a system on X8.6.x or later software
                                             to 12.5.4 or later. Fix incorrect default value for "Redirect HTTP requests to HTTPS" in the Network Services section. CSCvq39362 refers. | X12.5.4 release |
| June 2019 | RMS license consumption table updated, now includes only those scenarios which consume RMS licenses. | Document correction |
| May 2019 | Fix incorrect reference to 488 response code in the description of Meeting Server load balancing setting. | Document correction |
| April 2019 | Updates for X12.5.2 maintenance release (includes support for virtualized Small VMs on VMware ESXi platform). | X12.5.2 maintenance release |
| March 2019 | Updates for X12.5.1 maintenance release. | X12.5.1 maintenance release |
| February 2019 | Reinstate "Services That Can be Hosted Together" table in the Introduction. | Documentation correction |
| January 2019 | Updates for X12.5. | X12.5 release |
| December 2018 | Retitle for X8.11.4 (no substantive updates). Adjust B2BUA calls status section for CSCvn73111. | X8.11.4 maintenance release |
| October 2018 | Updates for X8.11.3 maintenance release. | X8.11.3 maintenance release (withdrawn) |
| September 2018 | Updated for Webex and Spark platform rebranding, CE1200 appliance, and X8.11.1 release. | X8.11.1 release (withdrawn) |
| July 2018 | Updates for X8.11. | X8.11 release (withdrawn) |
| July 2017 | Updates for X8.10. | X8.10 release |
| January 2017 | General corrections and updates. New feature added. | X8.9.1 maintenance release |
| December 2016 | New features and general corrections. | X8.9 release |
| September 2016 | Help and admin guide updates including new call policy rule configuration. | X8.8.2 maintenance release |
| July 2016 | Correction in MRA overview and Xconfig SIP Advanced CLI commands added. | X8.8 document corrections |
| June 2016 | Updates for X8.8. | X8.8 release |
| April 2016 | General corrections and updates. New features added. | X8.7.2 Maintenance release |
| February 2016 | General corrections and updates. Document change history (this table) added. DNS zone parameters and alarm reference updated. | X8.7.1 Maintenance release |

| Note | X12.5.7 now withdrawn and replaced with X12.5.9. |
|---|---|

| Support videos | Videos provided by Cisco TAC engineers about certain common Expressway configuration procedures are available on the Expressway/VCS Screencast Video List page (search for "Expressway videos" ) |
|---|---|
| Installation - virtual machines | Cisco Expressway Virtual Machine Installation Guide on the Expressway Installation Guides page |
| Installation - physical appliances | Cisco Expressway CE1200 Appliance Installation Guide on the Expressway Installation Guides page. |
| Basic configuration for single-box systems | Cisco Expressway Registrar Deployment Guide on the Expressway Configuration Guides page |
| Basic configuration for paired-box systems (firewall
                                             									traversal) | Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide on the Expressway Configuration Guides page |
| Administration and maintenance | Cisco Expressway Administrator Guide on the Expressway Maintain and Operate Guides page (includes Serviceability information) |
| Clustering | Cisco Expressway Cluster Creation and Maintenance Deployment Guide on the Expressway Configuration Guides page |
| Certificates | Cisco Expressway Certificate Creation and Use Deployment Guide on the Expressway Configuration Guides page |
| Ports | Cisco Expressway IP Port Usage Configuration Guide on the Expressway Configuration Guides page |
| Unified Communications | Mobile and Remote Access Through Cisco Expressway on the Expressway Configuration Guides page |
| Cisco Meeting Server | Cisco Meeting Server with Cisco Expressway Deployment Guide on the Expressway Configuration Guides page Cisco Meeting Server API Reference Guide on the Cisco Meeting Server Programming Guides page Other Cisco Meeting Server guides are available on the Cisco Meeting Server Configuration Guides page |
| Cisco Webex Hybrid Services | Hybrid Services Knowledge Base |
| Cisco Hosted Collaboration Solution (HCS) | HCS Customer Documentation |
| Microsoft infrastructure | Cisco Expressway with Microsoft Infrastructure Deployment Guide on the Expressway Configuration Guides page Cisco Jabber and Microsoft Skype for Business Infrastructure Configuration Cheatsheet on the Expressway Configuration Guides page |
| Rest API | Cisco Expressway REST API Summary Guide on the Expressway Configuration Guides page (high-level information only as the API is self-documented) |
| Multiway Conferencing | Cisco TelePresence Multiway Deployment Guide on the Expressway Configuration Guides page |

| Note | If you use Smart Licensing, you cannot change the Series setting from the Service Selection page/wizard (to convert an Expressway to a VCS
                                       				product). Instead this process must start with a factory reset (to disable Smart
                                       				Licensing because it's not supported on VCS). Some of the other settings shown in
                                       				this example are unnecessary with Smart Licensing and do not appear in the wizard on
                                       				Expressways that use Smart Licensing. |
|---|---|

|  | Cisco Webex Hybrid Services (Connectors | Mobile and Remote Access | Jabber | Microsoft gateway server | Registration | CMR Cloud | Business to Business calling (includes Hybrid Call Service) |
|---|---|---|---|---|---|---|---|
| Cisco Webex Hybrid Services (Connectors) | Y | N | N | N | N | Y | Y |
| Mobile and Remote Access and/or (from X8.9) Meeting Server Web Proxy | N | Y | N | N | Y | Y | Y* |
| Microsoft gateway service | N | N | N | Y | N | N | N |
| Registrar | N | Y | Y | N | Y | Y | Y |
| CMR Cloud | Y | Y | Y | N | Y | Y | Y |
| Business to Business calling (includes Hybrid Call Service) | Y | Y* | Y | N | Y | Y | Y |