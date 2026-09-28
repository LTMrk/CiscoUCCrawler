---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-v12-5-1-vtgs-b-csr-collaboration-release-notes-1251-html-a169675001
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/V12-5-1/vtgs_b_csr-collaboration-release-notes-1251.html
retrieved_at: 2026-08-16T18:27:08.958491+00:00
---

Release Notes for Cisco Collaboration Systems Release 12.5(1)

# Release Notes for Cisco Collaboration Systems Release 12.5(1)

### Download Options

Updated: February 27, 2019

First Published: February 27, 2019

# Introduction to Cisco Collaboration Systems Release 12.5(1)

As part of our standard methodology for each Cisco Collaboration Systems Release, we:

Perform system-wide testing of Cisco Collaboration products to supplement the product-level testing performed on each collaboration
                     product.

Recommend compatible software releases that were verified by the testing teams. The recommendations are not exclusive and
                     are in addition to interoperability recommendations for each of the individual applications or products.

For software compatibility data, see the Cisco Collaboration Systems Release Compatibility Matrix .

Software compatibility data for all Cisco Collaboration Systems releases before 10.5(1) is available from the Cisco Collaboration Systems Compatibility Tool .

Not all Collaboration System product release versions may be available at the same time. For latest product version availability,
                              see individual product support pages at, Support and Downloads .

This document focuses on the Collaboration components tested as part of the Cisco Collaboration Systems Release. For information
               focused on Contact Center components that were tested as part of Cisco Collaboration Systems Release, see: https://cisco.com/go/unified-techinfo .

This document provides release notes details based on the system-wide testing which includes the following types of components:

Call Control components, such as Cisco Unified Communications Manager, Cisco Unified Communications Manager IM and Presence
                     Service, Cisco Business Edition, Cisco Unified Communications Manager Express, and Cisco Unified Survivable Remote Site Telephony.

Conferencing components, such as Cisco Meeting Server, Cisco Meeting App, Cisco Meeting Management, Cisco TelePresence Management
                     Suite, Cisco TelePresence Management Suite Provisioning Extension, and Cisco TelePresence Management Suite Extension for Microsoft
                     Exchange.

Enterprise Edge components, such as Cisco TelePresence Video Communication Server, Cisco Expressway Series, and Cisco Unified
                     Border Element.

Server Applications, such as Cisco Emergency Responder, Cisco Paging Server, and Cisco Unified Attendant Consoles.

Cloud and Hybrid Services, such as Cisco Webex Teams, Cisco Webex Meetings for Cisco Collaboration Meeting Rooms (CMR) Cloud,
                     Cisco Webex Meetings Server, Cisco Webex Meetings, and Cloud Webex Edge Video Mesh.

Voicemail and Messaging components, such as Cisco Unity Connection and Cisco Unity Express.

Endpoint components, such as Cisco IP Phone Series, Cisco TelePresence IX5000, Cisco Webex DX80, Cisco TelePresence MX and
                     SX Series, Cisco Jabber, and Cisco Virtualization Experience Media Engine.

Service Management components, such as Cisco Prime Collaboration.

Communication Gateway components, such as Cisco Integrated Services Routers (ISR).

## Tested Functionality

System-wide testing was done for features and upgrade paths.

### Feature Testing

In this release, the following features were system-tested.

#### Mobility

Jabber for iOS Push Notifications

Cisco Web Security Applicance for iOS Push Notifications

For details on iOS Push Notifications, see: Push Notifications Deployment for Cisco Jabber on iPhone and iPad with Cisco Unified Communications Manager .

Mobile and Remote Access (MRA):

Interactive Connectivity Establishment (ICE) with SIP OAuth (for on-premise and MRA)

MRA recording through Built-in Bridge (BiB) for Jabber

Persistent chat for Jabber mobile

Jabber multi-line support over MRA

IM and Presence Service Centralized Deployment—for large-scale deployments (225K users)

#### Cisco Webex Teams Hybrid Services

Cisco Jabber and Webex Teams interoperability via IM and Presence Service Connector

Diversion on Decline

#### Interoperability

RFC 2833 DTMF Support on SCCP Media Resources

VoLTE Interoperability for TelePresence and Jabber

#### Recording

Multi-fork recording from Unified CM—testing recording resilience for FS compliance

#### Security

Transport Layer Security (TLS) 1.2 enhancements:

Cipher management controls

Elliptical curve cryptography for point to point calls

For more details on TLS 1.2 compatibility, see: TLS 1.2 Compatibility Matrix for Cisco Collaboration Products .

#### Simplified Administration

Simplified upgrade with cluster-wide configuration

Cisco Prime Collaboration Deployment enhancement – batch/bulk task chaining

Jabber configuration file management

Device onboarding via activation codes (on-premise phones)

#### Conferencing

Cisco Meeting Server (CMS) enhancements that support Cisco Telepresence MCU migrations to CMS

Media Adaptation and Resilience (MARI) enhancement that allows unknown SDP passthrough for on-premise endpoint that connects
                              to a cloud-hosted conference

@CMS Scheduling

Interoperability enhancement with Skype for Business

Conferencing enhancements for on-premise endpoints that connect to cloud-hosted conferences (including when a Hybrid Media
                              Node is deployed):

Roster List

Dual Screen UX

Active Control for on-premise Jabber

### Upgrade Paths

The system-wide functionality testing included verifying upgrade paths across various product components for a single stage
                        upgrade from Cisco Collaboration Systems Release 12.0(1) to Cisco Collaboration Systems Release 12.5(1).

For a list of versions that are compatible with Cisco Collaboration Systems Release 12.5, see the Cisco Collaboration Systems Compatibility Matrix .

## New and Changed Features

For details about what is new for Cisco Collaboration Systems Release 12.5(1), see the Solution Overview .

For details about new and changed collaboration product features, access individual product release notes from Product Documentation .

## System Requirements

This section provides information about system requirements for this Cisco Collaboration Systems Release.

### End-of-Sale Components

The following components have reached end-of-sale (EOS) status but are still supported.

Cisco TelePresence Conductor, End-of-Life and End-of-Sale Notices

Cisco TelePresence Server, End-of-Life and End-of-Sale Notices

Cisco MediaSense, End-of-Sale and End-of-Life Notices

Cisco Multiparty Media 400v, End-of-Sale and End-of-Life Notices

Cisco TelePresence MCU 4200 Series, End-of-Sale and End-of-Life Notices

Cisco TelePresence MCU 4500 Series, End-of-Sale and End-of-Life Notices

Cisco TelePresence MCU 5300 Series, End-of-Sale and End-of-Life Notices

Cisco TelePresence MCU MSE 8420 Blade, End-of-Sale and End-of-Life Notices

Cisco DX650, End-of-Sale and End-of-Life Notices

Cisco TelePresence System EX60 and EX90, End-of-Sale and End-of-Life Notices

Cisco TelePresence System 500, End-of-Sale and End-of-Life Notices

Cisco TelePresence Profile Series, End-of-Sale and End-of-Life Notices

Cisco TelePresence System 1100, End-of-Sale and End-of-Life Notices

Cisco TelePresence Integrator C Series, End-of-Sale and End-of-Life Notices

Cisco Unified IP Phone 6911, 6921, 6941, 6945, 6961, End-of-Sale and End-of-Life Notices

Cisco Unified IP Phone 7937G, 7931G, 7942G, 7962G, Cisco Unified IP Phone Expansion Module 7915, Cisco Unified Wireless IP
                              Phone 7925G, 7925G-EX, 7926G, End-of-Sale and End-of-Life Notices :

The following are now End-of-Support: 7936, 7906G, 7911G, 7941G, 7961G, 7985G.

Cisco Unified Communications Manager Release 12.x does not support some deprecated phone models. For more information, see
                                          the related Field Notice .

Cisco Unified IP Phone 8941, 8945, 8961, End-of-Sale and End-of-Life Announcement

Cisco Unified IP Phones 9900 Series, End-of-Sale and End-of-Life Notices

Cisco Unity Express 7.1, 7.2, 8.5, and 8.6, End-of-Sale and End-of-Life Notices

Cisco VG202, VG204, and VG224 Analog Voice Gateways, End-of-Sale and End-of-Life Notices

The following are End-of-Support: Cisco 2800 Series Integrated Services Routers , Cisco 3800 Series Integrated Services Routers , VG248 48-Port Analog Voice Gateway.

Cisco VG350 Analog Voice Gateways End-of-Sale and End-of-Life Notices

The EOS date is the last date to order the product through Cisco point-of-sale mechanisms. The product is no longer for sale.
                        Another process, the end-of-life (EOL) cycle, guides the final business operations associated with the product.

The EOL process consists of a series of technical and business milestones and activities that, when completed, make a product
                        obsolete. After a product becomes obsolete, it is not sold, manufactured, improved, repaired, maintained, or supported.

For information about recommended replacements and a comprehensive list of announcements, see Products & Services End-of-Sale and End-of-Life Products .

For information about specific products, go to Product/Technology Support . Then click End-of-Sale and End-of-Life and select products or technologies from the lists to the right.

Go to End-of-Life Policy for more information about the EOL policy.

### Deployment Considerations

This section lists deployment considerations for Cisco Collaboration Systems Release. Cisco Collaboration Systems validation
                        does not test every rebuild. Therefore, more regression testing in a customer or Cisco-specific certification lab is recommended
                        before deployment.

For your reference, see the Cisco Collaboration Systems Release Design Guides .

When deploying Cisco Collaboration Systems, consider the following.

At the minimum, deploy the software release that is recommended in:

Cisco Collaboration Systems Compatibility Matrix

For compatibility information before Collaboration Systems Release 10.5, refer to the Compatibility Tool .

For other software components, use the most current rebuild of a maintenance release. For IOS, information about the latest
                              releases, including deferral advisories, is available at:

http://tools.cisco.com/ITDIT/CFN/jsp/index.jsp

If the recommended release has been deferred to a subsequent release, use the subsequent release.

Before deploying a release, examine the open caveats in the chosen release to determine if any affect your implementation.
                              View open caveats through the Bug Search tool, which is located at:

https://tools.cisco.com/bugsearch/

Deploy the chosen release in a lab environment that uses the same product components as your product components before moving
                              to a production environment.

### Latest Software Upgrades

The following are links to the latest software upgrades for Cisco Collaboration Systems Release components.

To launch the Product Upgrade Tool, go to:

http://tools.cisco.com/gct/Upgrade/jsp/index.jsp

To download the latest software for all other components, go to:

https://software.cisco.com/download/home

## Component Versions

For current Cisco Collaboration Systems Release compatible component versions, refer to the Cisco Collaboration Systems Compatibility Matrix .

For compatibility information before Collaboration Systems Release 10.5, refer to the Compatibility Tool .

Product-specific compatibility documents provide complete compatibility information between components.

Not all Collaboration System product release versions may be available at the same time. For latest product version availability,
                              see individual product support pages at, Support and Downloads .

You can set up a virtualized environment by running collaboration applications on a virtual machine on a Unified Computing
                                 System (UCS). For more details, including UCS hardware information and third-party requirements, see:

https://www.cisco.com/go/virtualized-collaboration

Cisco Hosted Collaboration Solution (Cisco HCS) is a hosted solution that includes various Cisco Collaboration Systems release
                              components. For more information about Cisco HCS, see: Cisco Hosted Collaboration Solution and Cisco HCS Product Support .

## Related Documentation

### System Documentation

For high-level information about Cisco Collaboration Systems, see Cisco Collaboration Systems Solution and Component Support Documentation and Downloads .

### Product Documentation

The following table provides links to product documentation for the major Collaboration Systems Release components. The table
                        provides links to:

Product Overview pages, from which you can access marketing material, such as product data sheets.

Product Documentation pages, from which you can access technical documents such as release notes, design, installation, configuration, and troubleshooting
                              guides.

Component

Links

Call Control

Cisco Unified Communications Manager

Product Overview

Documentation

Cisco Unified Communications Manager IM & Presence Service

Product Overview

Documentation

Cisco Business Edition 6000

Product Overview

Documentation

Cisco Business Edition 7000

Product Overview

Documentation

Cisco Unified Communications Manager Express

Product Overview

Documentation

Cisco Unified Survivable Remote Site Telephony

Product Overview

Documentation

Contact Center

Cisco MediaSense (EOS)

Product Overview

Documentation

Conferencing

Cisco Meeting Server

Product Overview

Documentation

Cisco Meeting App

Documentation

Cisco Meeting Management

Documentation

Cisco TelePresence Management Suite

Product Overview

Documentation

Cisco TelePresence Management Suite Provisioning Extension

Product Overview

Documentation

Cisco TelePresence Management Suite Extension for Microsoft Exchange

Product Overview

Documentation

Cisco TelePresence Server on Virtual Machine (EOS)

Product Overview

Documentation

Cisco TelePresence Server on Multiparty Media 820 (EOS)

Product Overview

Documentation

Cisco TelePresence Conductor (EOS)

Product Overview

Documentation

Cisco TelePresence MCU 5300 Series (EOS)

Product Overview

Documentation

Cisco Collaboration Meeting Rooms (CMR) Cloud

Product Overview

Documentation

Cisco Collaboration Meeting Rooms (CMR) Hybrid

Release Notes, Documentation, and Product Overview

Enterprise Edge

Cisco Expressway Series

Product Overview

Documentation

Cisco Unified Border Element

Product Overview

Documentation

Server Applications

Cisco Emergency Responder

Product Overview

Documentation

Cisco Unified Attendant Console Standard

Product Overview

Documentation

Cisco Unified Attendant Console Advanced

Product Overview

Documentation

Cloud and Hybrid Services Applications

Cisco Webex Teams

Message, Meet, Call

Cisco Webex Devices

Documentation, Devices and Applications

Cisco Webex Board

Documentation, Devices and Applications

Cisco Webex Hybrid Services

Hybrid Services Calendar

Hybrid Services Call

Cisco Directory Connector

Hybrid Services Directory

Cisco Expressway Series

Product Overview

Documentation

Cisco Webex Meetings Server

Product Overview

Documentation

Cisco Webex Meetings

Product Overview

Documentation

Voicemail and Messaging

Cisco Unity Connection

Product Overview

Documentation

Cisco Unity Express

Product Overview

Documentation

Endpoints

Cisco DX70

Cisco TelePresence DX70

Product Overview

Documentation

Cisco Webex DX80

Product Overview

Documentation

Cisco Webex Room Kit

Product Overview

Documentation

Cisco Webex Room Kit Plus

Product Overview

Documentation

Cisco DX650 (EOS)

Product Overview

Documentation

Cisco TelePresence System EX Series (EOS)

Product Overview

Documentation

Cisco TelePresence System 500-32 (EOS)

Product Overview

Documentation

Cisco TelePresence System 500-37 (EOS)

Product Overview

Documentation

Cisco TelePresence IX5000

Product Overview

Documentation

Cisco TelePresence MX Series

Product Overview

Documentation

Cisco TelePresence SX Series

Product Overview

Documentation

Cisco TelePresence System 1100 (EOS)

Product Overview

Documentation

Cisco TelePresence Integrator C Series (EOS)

Product Overview

Documentation

Cisco TelePresence Precision 60 Camera

Product Overview

Documentation

Cisco IP Phone 7800 Series

Product Overview

Documentation

Cisco IP Phone 8800 Series

Product Overview

Documentation

Cisco Jabber for Android

Product Overview

Documentation

Cisco Jabber iPhone and iPad

Product Overview

Documentation

Cisco Jabber for Mac

Product Overview

Documentation

Cisco Jabber for Windows

Product Overview

Documentation

Service Management

Cisco Prime Collaboration (Provisioning, Assurance)

Product Overview

Documentation

Cisco Prime Collaboration (Deployment)

Product Overview

Documentation

Communication Gateways

Cisco IOS 15 M&T

Documentation

Cisco IOS XE 16

Documentation

Cisco 2900 Series Integrated Services Routers (EOS)

Product Overview

Documentation

Cisco 3900 Series Integrated Services Routers

Product Overview

Documentation

Cisco 4400 Series Integrated Services Routers

Product Overview

Documentation

### Managed Services Documentation

For information about managed services of certain products, refer to the product support documentation. For example, see the Managed Services Guide for Cisco Unified Communications Manager and IM and Presence Service, Release 12.5(1) .

## Limitations and Restrictions

If you are a Cisco partner or a registered Cisco.com user with a Cisco service contract, you can use the Bug Search tool to
                     find caveats of any severity for any release. Access Bug Search at: https://bst.cloudapps.cisco.com/bugsearch/ .

We offer a Cisco Notification Service that allows you to set up one or more profiles. These profiles enable you to receive
                     email notification of new Field Notices, Product Alerts, or End of Sale information for the products that you have selected.
                     The Product Alert Tool is available at: https://www.cisco.com/cisco/support/notifications.html .

### Important Notes

This section includes important notes related to the testing of this Cisco Collaboration Systems Release.

#### Duplicate Certificates Leads to CPU Spike during Certificate Sync

In a customer environment where multiple certificate operations have taken place, it is possible to end up in a situation
                           where multiple certificates for the same Common Name exist in the database. When this occurs, the CPU spikes every 30 minutes
                           during standard certificate maintenance by the Certificate Sync service. The following types of lines may appear in Change
                           Notification logs:

2018-10-26 08:48:02,731 INFO [Timer-0] - IN -- CertDBUtil.java - deleteTrustCertInFileSystem.. unit : tomcat-trust :: FileName
                                    :: /usr/local/platform/.security/tomcat/trust-certs/<CN2>.pem

2018-10-26 08:49:01,943 INFO [Timer-0] - IN -- CertDBUtil.java - deleteTrustCertInFileSystem.. unit : CallManager-trust ::
                                    FileName :: /usr/local/cm/.security/CallManager/trust-certs/<CN1>.pem

To verify whether there are duplicate certificates in the DB, run the below queries from CLI:

For CallManager-trust:

run sql select serialnumber, subjectname from certificate A, certificateservicecertificatemap B where B.fkcertificate=A.pkid
                                    and B.tkcertificateservice=4 and subjectname like '%<CN1>%'

For Tomcat-trust:

run sql select serialnumber, subjectname from certificate A, certificateservicecertificatemap B where B.fkcertificate=A.pkid
                                    and B.tkcertificateservice=6 and subjectname like '%<CN2>%'

For additional details, see CSCvn65359.

#### Memory Corruption Issue Causes System Crash

Under extended heavy load conditions, Cisco Unified Communications Manager has been observed to crash due to a memory allocation
                           issue. This issue results in a ccm process coredump. The issue is currently being investigated.

For additional details, see CSCvn32181.

#### System Crashes when Allocating Memory for Multiple Threads Simultaneously

Cisco Unified Communications Manager has been observed to crash in situations with very heavy call loads. This may occur due
                           to multiple threads allocating memory simultaneously. In normal conditions, this situation does not occur as simultaneous
                           memory allocation would not occur.

For additional details, see CSCvn77809.

#### DHCPv6 as Default for Dual-stack DX

If you configure a DX with CE build as dual-stack endpoint on Unified CM, you won’t see an IPv6 address on the endpoint. To
                           allow the endpoint to use an IPv6 address, turn on the DHCP IPv6 setting under the endpoint’s network configuration. For more
                           details, see CSCvi49092 .

#### show dspfarm profile Information Not Displayed

In calls from endpoints that don’t support Keypad Markup Language (KPML), the show dspfarm profile command doesn’t show the
                           actual resources being used. The profile shows only the SCCP connections. For more details, see CSCvd91119 .

#### Caller-ID Not Changed After Transfer

On Cisco Webex Call phones, the caller-ID is not updated properly after a transfer from enterprise phones. For more details,
                           see CSCve56223 .

#### Support for Hostname When Configuring InformaCast Wizard

If you enter the FQDN of the InformaCast server on the Connecting to InformaCast page of the wizard, the install wizard for
                           Emergency Notifications Paging may fail to connect to InformaCast. To work around this potential issue, enter the IP Address
                           instead of the FQDN of the InformaCast.

For more details, see CSCvf58052 .

#### Show Connection Status Not Updated After Unified Communications Manager Failover for Jabber in Mobile and Remote Access Deployment

When Jabber is registered using Mobile and Remote Access, the "Connection status" window shows connected address as the primary Unified Communications Manager, even after a Unified Communications Manager
                        failover has happened, and the client is registered to the secondary Unified Communications Manager. For more information,
                        see CSCuo89949 .

### Open Caveats

The following table lists known caveats, grouped by severity, related to Cisco Collaboration Systems Release testing. It also
                        includes caveats from previous releases, which were not resolved at the time this document was written. For more information
                        about each defect, click the linked caveat number in the Identifier column.

For information about a defect not listed in the table, go to Bug Search Tool .

For information about known issues with Cisco Webex Hybrid Services, go to Help Central: Cisco Cloud Collaboration Management - Known Issues .

Identifier

Headline

Severity 2-3 Caveats

CSCve56223

Caller-ID not changed after transfer since Expressway-c doesnt update P-Asserted-Identity

CSCvj93746

Expressway changes for APNS calls failing with jabber app killed/device standby and UCM failover

CSCvm60911

TCP conn. failed between source (28405) & destination (5071) on same Expressway-C server

CSCvn32181

Under extended traffic load, Memory corruption caused ccm process core dump

CSCvn35907

Utils os kerneldump status shows enabled when kerneldump is not enabled

CSCvn50468

APNS cluster onboarded but IMP xcpconfigmgr failing to fetch token due to missing certs

CSCvn55141

Time elapsed details while doing upgrades

CSCvn65359

CertSync causes CPU spikes due to duplicate certs in DB/file system, even with fix for CSCvg47019

CSCvn75705

Jabberd process core dump just after L2 system upgrade.

CSCvn77809

Threads allocating memory at the same time leading to deadlock condition that cause CM process core

CSCvn82784

RTMT shows AMC service down in publisher

CSCvn91735

Install of cleanup gets stuck in some conditions

CSCvn94361

CUCM Upgrade command asks to re-use credentials, but also uses directory path of SFTP from Pub

## Troubleshooting

For troubleshooting information, tips, and recommendations related to Cisco Collaboration Systems Releases, see individual
                     product Troubleshooting Guides located in Component Documentation .

### This Document Applies to These Products

- Collaboration Systems Release 12.5

| Note | Software compatibility data for all Cisco Collaboration Systems releases before 10.5(1) is available from the Cisco Collaboration Systems Compatibility Tool . |
|---|---|

| Note | Not all Collaboration System product release versions may be available at the same time. For latest product version availability,
                              see individual product support pages at, Support and Downloads . |
|---|---|

| Note | The following are now End-of-Support: 7936, 7906G, 7911G, 7941G, 7961G, 7985G. |
|---|---|

| Note | Cisco Unified Communications Manager Release 12.x does not support some deprecated phone models. For more information, see
                                          the related Field Notice . |
|---|---|

| Note | The following are End-of-Support: Cisco 2800 Series Integrated Services Routers , Cisco 3800 Series Integrated Services Routers , VG248 48-Port Analog Voice Gateway. |
|---|---|

| Note | For your reference, see the Cisco Collaboration Systems Release Design Guides . |
|---|---|

| Note | For compatibility information before Collaboration Systems Release 10.5, refer to the Compatibility Tool . |
|---|---|

| Note | For compatibility information before Collaboration Systems Release 10.5, refer to the Compatibility Tool . |
|---|---|

| Note | Product-specific compatibility documents provide complete compatibility information between components. |
|---|---|

| Note | Not all Collaboration System product release versions may be available at the same time. For latest product version availability,
                              see individual product support pages at, Support and Downloads . |
|---|---|

| Note | You can set up a virtualized environment by running collaboration applications on a virtual machine on a Unified Computing
                                 System (UCS). For more details, including UCS hardware information and third-party requirements, see: https://www.cisco.com/go/virtualized-collaboration |
|---|---|

| Note | Cisco Hosted Collaboration Solution (Cisco HCS) is a hosted solution that includes various Cisco Collaboration Systems release
                              components. For more information about Cisco HCS, see: Cisco Hosted Collaboration Solution and Cisco HCS Product Support . |
|---|---|

| Component | Links |
|---|---|
| Call Control |
| Cisco Unified Communications Manager | Product Overview Documentation |
| Cisco Unified Communications Manager IM & Presence Service | Product Overview Documentation |
| Cisco Business Edition 6000 | Product Overview Documentation |
| Cisco Business Edition 7000 | Product Overview Documentation |
| Cisco Unified Communications Manager Express | Product Overview Documentation |
| Cisco Unified Survivable Remote Site Telephony | Product Overview Documentation |
| Contact Center |
| Cisco MediaSense (EOS) | Product Overview Documentation |
| Conferencing |
| Cisco Meeting Server | Product Overview Documentation |
| Cisco Meeting App | Documentation |
| Cisco Meeting Management | Documentation |
| Cisco TelePresence Management Suite | Product Overview Documentation |
| Cisco TelePresence Management Suite Provisioning Extension | Product Overview Documentation |
| Cisco TelePresence Management Suite Extension for Microsoft Exchange | Product Overview Documentation |
| Cisco TelePresence Server on Virtual Machine (EOS) | Product Overview Documentation |
| Cisco TelePresence Server on Multiparty Media 820 (EOS) | Product Overview Documentation |
| Cisco TelePresence Conductor (EOS) | Product Overview Documentation |
| Cisco TelePresence MCU 5300 Series (EOS) | Product Overview Documentation |
| Cisco Collaboration Meeting Rooms (CMR) Cloud | Product Overview Documentation |
| Cisco Collaboration Meeting Rooms (CMR) Hybrid | Release Notes, Documentation, and Product Overview |
| Enterprise Edge |
| Cisco Expressway Series | Product Overview Documentation |
| Cisco Unified Border Element | Product Overview Documentation |
| Server Applications |
| Cisco Emergency Responder | Product Overview Documentation |
| Cisco Unified Attendant Console Standard | Product Overview Documentation |
| Cisco Unified Attendant Console Advanced | Product Overview Documentation |
| Cloud and Hybrid Services Applications |
| Cisco Webex Teams | Message, Meet, Call |
| Cisco Webex Devices | Documentation, Devices and Applications |
| Cisco Webex Board | Documentation, Devices and Applications |
| Cisco Webex Hybrid Services | Hybrid Services Calendar Hybrid Services Call |
| Cisco Directory Connector | Hybrid Services Directory |
| Cisco Expressway Series | Product Overview Documentation |
| Cisco Webex Meetings Server | Product Overview Documentation |
| Cisco Webex Meetings | Product Overview Documentation |
| Voicemail and Messaging |
| Cisco Unity Connection | Product Overview Documentation |
| Cisco Unity Express | Product Overview Documentation |
| Endpoints |
| Cisco DX70 Cisco TelePresence DX70 | Product Overview Documentation |
| Cisco Webex DX80 | Product Overview Documentation |
| Cisco Webex Room Kit | Product Overview Documentation |
| Cisco Webex Room Kit Plus | Product Overview Documentation |
| Cisco DX650 (EOS) | Product Overview Documentation |
| Cisco TelePresence System EX Series (EOS) | Product Overview Documentation |
| Cisco TelePresence System 500-32 (EOS) | Product Overview Documentation |
| Cisco TelePresence System 500-37 (EOS) | Product Overview Documentation |
| Cisco TelePresence IX5000 | Product Overview Documentation |
| Cisco TelePresence MX Series | Product Overview Documentation |
| Cisco TelePresence SX Series | Product Overview Documentation |
| Cisco TelePresence System 1100 (EOS) | Product Overview Documentation |
| Cisco TelePresence Integrator C Series (EOS) | Product Overview Documentation |
| Cisco TelePresence Precision 60 Camera | Product Overview Documentation |
| Cisco IP Phone 7800 Series | Product Overview Documentation |
| Cisco IP Phone 8800 Series | Product Overview Documentation |
| Cisco Jabber for Android | Product Overview Documentation |
| Cisco Jabber iPhone and iPad | Product Overview Documentation |
| Cisco Jabber for Mac | Product Overview Documentation |
| Cisco Jabber for Windows | Product Overview Documentation |
| Service Management |
| Cisco Prime Collaboration (Provisioning, Assurance) | Product Overview Documentation |
| Cisco Prime Collaboration (Deployment) | Product Overview Documentation |
| Communication Gateways |
| Cisco IOS 15 M&T | Documentation |
| Cisco IOS XE 16 | Documentation |
| Cisco 2900 Series Integrated Services Routers (EOS) | Product Overview Documentation |
| Cisco 3900 Series Integrated Services Routers | Product Overview Documentation |
| Cisco 4400 Series Integrated Services Routers | Product Overview Documentation |

| Identifier | Headline |
|---|---|
| Severity 2-3 Caveats |
| CSCve56223 | Caller-ID not changed after transfer since Expressway-c doesnt update P-Asserted-Identity |
| CSCvj93746 | Expressway changes for APNS calls failing with jabber app killed/device standby and UCM failover |
| CSCvm60911 | TCP conn. failed between source (28405) & destination (5071) on same Expressway-C server |
| CSCvn32181 | Under extended traffic load, Memory corruption caused ccm process core dump |
| CSCvn35907 | Utils os kerneldump status shows enabled when kerneldump is not enabled |
| CSCvn50468 | APNS cluster onboarded but IMP xcpconfigmgr failing to fetch token due to missing certs |
| CSCvn55141 | Time elapsed details while doing upgrades |
| CSCvn65359 | CertSync causes CPU spikes due to duplicate certs in DB/file system, even with fix for CSCvg47019 |
| CSCvn75705 | Jabberd process core dump just after L2 system upgrade. |
| CSCvn77809 | Threads allocating memory at the same time leading to deadlock condition that cause CM process core |
| CSCvn82784 | RTMT shows AMC service down in publisher |
| CSCvn91735 | Install of cleanup gets stuck in some conditions |
| CSCvn94361 | CUCM Upgrade command asks to re-use credentials, but also uses directory path of SFTP from Pub |