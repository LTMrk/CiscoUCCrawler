---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-v14-vtgs-b-release-notes-collab-14-html-3e16f4e2cf
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/V14/vtgs_b_release-notes-collab-14.html
retrieved_at: 2026-08-16T18:26:48.066247+00:00
---

Release Notes for Cisco Collaboration Systems Release 14

# Release Notes for Cisco Collaboration Systems Release 14

### Download Options

Updated: April 15, 2021

First Published: April 15, 2021

# Introduction to Collaboration Systems Release

As part of our standard methodology for each Cisco Collaboration Systems Release, we:

Perform system-wide testing of Cisco Collaboration products to supplement the product-level testing performed on each collaboration
                        product.

Recommend compatible software releases that were verified by the testing teams. The recommendations are not exclusive and
                        are in addition to interoperability recommendations for each of the individual applications or products.

For software compatibility data, see the Cisco Collaboration Systems Release Compatibility Matrix .

Not all Collaboration System product release versions may be available at the same time. For latest product version availability,
                                 see individual product support pages at, Support and Downloads .

This document focuses on the Collaboration components tested as part of the Cisco Collaboration Systems Release. For information
                  focused on Contact Center components that were tested as part of Cisco Collaboration Systems Release, see: Release Notes for Contact Center: Cisco Collaboration Systems Release at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-system/products-release-notes-list.html

This document provides release notes details based on the system-wide testing which includes the following types of components:

Calling components, such as Cisco Unified Communications Manager, Cisco Webex Calling, Cisco Emergency Responder, Cisco Unifed
                        Attendant Console, Cisco Paging Server, Cisco Business Edition, Cisco Unified Communications Manager Express, and Cisco Unified
                        Survivable Remote Site Telephony.

Messaging components such as Cisco Unified Communications Manager IM and Presence Service and Cisco Webex.

Voicemail components, such as Cisco Unity Connection.

Enterprise Edge components, such as Cisco Expressway Series, Cisco Unified Border Element and Cisco Unified SIP Proxy.

Conferencing components, such as Cisco Meeting Server, Cisco Meeting App, Cisco Meeting Management, Cisco TelePresence Management
                        Suite, Cisco TelePresence Management Suite Provisioning Extension, and Cisco TelePresence Management Suite Extension for Microsoft
                        Exchange, Cisco Webex, Cisco Webex Meetings for Cisco Collaboration Meeting Rooms (CMR) Cloud, Cisco Webex Meetings Server,
                        Cisco Webex Meetings, and Cloud Webex Edge Video Mesh..

Endpoint components, such as Cisco IP Phone Series, Cisco Webex Desk Series, Cisco Webex Room Series, Cisco Webex app, Cisco
                        TelePresence IX5000, Cisco Jabber, Cisco Jabber Softphone for VDI, and Cisco Headset Series.

Service Management components, such as Cisco Prime Collaboration.

Communication Gateway components, such as Cisco Integrated Services Routers (ISR), Cisco 1000 Series Aggregation Servics Routers,
                        and Cisco VG Series Analog Voice Gateways.

## Tested Functionality

System-wide testing was done for features and upgrade paths.

### Feature Testing

The following Release 14 Solution features were tested:

SIP OAuth Mode Support for Cisco IP Phone 7800 and 8800 Series —SIP OAuth Mode support is extended to include secure SIP line registrations for Cisco IP Phone 7800 and 8800 Series enterprise
                              phones. This feature enhances the security for these phones while simplifying the process of securing your system.

UDS Bulk Search by Email for Cisco Jabber —Cisco Jabber clients can now send batch requests using the email attribute. This feture prevents high CPU usage by UDS and
                              Cisco Tomcat services.

Mobile and Remote Access Registration Failover —This feature provides automatic registraton failover for Cisco Jabber clients over Mobile and Remote Access. This feature
                              provide faster failover times with dynamic route updates to handle any server failures.

Wi-Fi to LTE for Webex App —Cisco Webex users can now switch between Wi-Fi and LTE networks seamlessly wihtout dropping the connection. This feature
                              adds flexibility and support for Webex users while roaming between networks.

This feature is supported on both Cisco Webex Mobile and Desktop versions.

AV1 Codec Support for Webex Video Endpoints —The AV1 video codec is now supported for various Cisco Webex video endpoints, including the Cisco Webex Desk Pro, Cisco Webex
                              Codec Pro, and Cisco Webex Room Panorama systems. AV1 provides improved compression rates compared to H.264 while matching
                              the user experience.

Jabber Zero Downtime —Enhancements for IM and Presence Service upgrades reduce the amount of downtime for Cisco Jabber clients to nearly zero.
                              During upgrades, clients maintain a soft connection to a primary and backup node providing high availability even during upgrades.

Deskphone Presence to Webex App —The user presence that the Webex app advertises now includes deskphone presence from any deskphones the user owns that are
                              registered to Csico Unified Communications Manager.

Cisco Jabber Push Notifications —The latest Push Notifications features and support were tested for iOS and Android devices.

### Upgrade Paths

The system-wide functionality testing included verifying upgrade paths across various product components for a single stage
                        upgrade from Cisco Collaboration Systems Release 12.8 to Cisco Collaboration Systems Release 14.

For a list of versions that are compatible with this release of Cisco Collaboration Systems, see the Cisco Collaboration Systems Compatibility Matrix .

## New and Changed Features

For details about what features are included with Cisco Collaboration Systems Release 14, see the Cisco Collaboration Systems Release 14 .

For details about new and changed collaboration product features, access individual product release notes from Product Components

## System Requirements

This section provides information about system requirements for this Cisco Collaboration Systems Release.

### End-of-Sale Components

#### Product Components that are End of Sale

As of March 31, 2021, the following product components are End-of-Sale (EOS), but are still supported. Refer to the corresponding
                        link for up to date information.

Cisco TelePresence Video Communication Server, End of Sale and End of Life Notices

Cisco TelePresence Service on Multiparty Media 820, End of Sale and End of Life Notices

Cisco TelePresence MCU 5300 Series, End-of-Sale and End-of-Life Notices

Cisco TelePresence MCU MSE 8510, End of Sale and End-of-Life Notices

Cisco Webex Meetings Server, End of Life and End of Sale Notices

Cisco TelePresence Management Suite Provisioning Extension, End of Life and End of Sale Notices ,

Cisco TelePresence IX5000 Series, End of Life and End of Sale Notices

Cisco TelePresence MX700D, MX800S, 800D, End of Life and End of Sale Notices

Cisco TelePresence MX300G2, End of Life and End of Sale Noticices

Cisco TelePresence MX200G2, End of Life and End of Sale Notices

Cisco TelePresence SX10, SX20, SX80, End of Life and End of Sale Notices

Cisco TelePresence Touch 10, End of Life and End of Sale Notices

Cisco Webex Touch 10, End of Life and End of Sale Notices

Cisco TelePresence  EX90, End-of-Sale and End-of-Life Notices

Cisco DX70, End of Sale and End of Life Notices

Cisco Webex DX80, End of Life and End of Sale Notices

Cisco DX650, End-of-Sale and End-of-Life Notices

Cisco Unified IP Phone 7945G, 7965G, 7975G Cisco Unified IP Phone Expansion Module 7916, , End-of-Sale and End-of-Life Notices

Cisco Unifed IP Conference Phone 8831, End of Sale and End of Life Notices

Cisco IP Phone 9951 and 9971. End of Life and End of Sale Notices

The following phone models are End-of-Support as of March 31 2021: 3911, 3951, 6911, 6921, 6941, 6945, 6961, 7902G, 7905G,
                                          7906G, 7911G, 7912G, 7915 7925G, 7925G-EX, 7926G, 7931G, 7936, 7937G, 7940G, 7941G, 7941G-GE, 7942G, 7960G, 7961G, 7961G-GE,
                                          7962G, 7970G, 7971G-GE, 7985G, 8941, 8945, 8961

Many phone models are deprecated in Cisco Unified Communications Manager Releases 11.5(x) and up. Deprecated phone models
                                          will not work in the Unified Communications Manager for which they are deprecated. For information on which phone models are
                                          deprecated, and as of which release, see the Deprecated Phone Models notice.

Cisco IP Communicator, End of Life and End of Sale Notices

Cisco Unity Express End-of-Sale and End-of-Life Notices

Cisco ATA 190 Analog Telephone Adapter, End of Sale and End of Life Notices

Cisco VG350 Analog Voice Gateways End-of-Sale and End-of-Life Notices

Cisco 2900 Series Integrated Services Routers, End of Sale and End of Life Notices

Cisco 3900 Series Integrated Services Routers, End of Life and End of Sale Notices

The following gateway models are End-of-Support as of March 31, 2021: Cisco VG202 Analog Voice Gateway, Cisco VG204 Analog
                                          Voice Gateway, Cisco VG224 Analog Voice Gateway, Cisco VG248 48-PortAnalog Voice Gateway, Cisco 2800 Series Integrated Services
                                          Routers, Cisco 3800 Series Integrated Services Routers, Cisco ATA 187 Analog Telephony Adapter.

The EOS date is the last date to order the product through Cisco point-of-sale mechanisms. The product is no longer for sale.
                        Another process, the end-of-life (EOL) cycle, guides the final business operations associated with the product.

The EOL process consists of a series of technical and business milestones and activities that, when completed, make a product
                        obsolete. After a product becomes obsolete, it is not sold, manufactured, improved, repaired, maintained, or supported.

For information about recommended replacements and a comprehensive list of announcements, see Products & Services End-of-Sale and End-of-Life Products .

Go to End-of-Life Policy for more information about the EOL policy.

#### Software Versions

Refer to the below links for information on which software versions are End of Sale for that product component:

Cisco Unified Communications Manager, End of Life and End of Sale Notices

Cisco Unified Communications Manager IM and Presence Service, End of Life and End of Sale Notices

Cisco Business Edition 6000, End of Life and End of Sale Notices

Cisco Business Edition 7000, End of Life and End of Sale Notices

Cisco Emergency Responder, End of Life and End of Sale Notices

Cisco Unified Attendant Console (Standard/Advanced), End of Life and End of Sale Notices

Cisco Unified Communications Manager Express, End of Life and End of Sale Notices

Cisco Unified Survivable Remote Site Telephony, End of Life and End of Sale Notices

Cisco Expressway, End of Life and End of Sale Notices

Cisco Unified Border Element, End of Life and End of Sale Notices

Cisco Unity Connection, End of Life and End of Sale Notices

Cisco Unity Express, End of Life and End of Sale Notices

Cisco Meeting Server, End of Life and End of Sale Notices

Cisco TelePresence Management Suite, End of Life and End of Sale Notices

Cisco TelePresence Video Communications Server, End of Life and End of Sale Notices

Cisco Webex Meetings, End of Life and End of Sale Notices

Cisco Webex Meetings Server, End of Life and End of Sale Notices

Cisco Jabber for Windows, End of Life and End of Sale Notices

Cisco Jabber for Mac, End of Life and End of Sale Notices

Cisco Jabber for iOS, End of Life and End of Sale Notices

Cisco Jabber for Android, End of Life and End of Sale Notices

Cisco Jabber Softphone for VDI, End of Life and End of Sale Notices

Cisco Prime Collaboration, End of Life and End of Sale Notices

Cisco Unified SIP Proxy, End of Life and End of Sale Notices

Cisco VG Series Gateways, End of Life and End of Sale Notices

Cisco ATA 190 Series Analog Telephone Adapters, End of Life and End of Sale Notices

Cisco ASR 1000 Series Aggregation Services Routers, End of Life and End of Sale Notices

Cisco 2900 Series Integrated Services Routers, End of Life and End of Sale Notices

Cisco 3900 Series Integrated Services Routers, End of Life and End of Sale Notices

Cisco 4000 Series Integrated Services Routers, End of Life and End of Sale Notices

Cisco IOS XE Software for Cisco 4000 Series Integrated Services Routers, End of Life and End of Sale Notices

### Deployment Considerations

This section lists deployment considerations for Cisco Collaboration Systems Release. Cisco Collaboration Systems validation
                        does not test every rebuild. Therefore, more regression testing in a customer or Cisco-specific certification lab is recommended
                        before deployment.

For your reference, see the Cisco Collaboration Systems Release Design Guides .

When deploying Cisco Collaboration Systems, consider the following.

At the minimum, deploy the software release that is recommended in:

Cisco Collaboration Systems Compatibility Matrix

For other software components, use the most current rebuild of a maintenance release. For IOS, information about the latest
                              releases, including deferral advisories, is available at:

http://tools.cisco.com/ITDIT/CFN/jsp/index.jsp

If the recommended release has been deferred to a subsequent release, use the subsequent release.

Before deploying a release, examine the open caveats in the chosen release to determine if any affect your implementation.
                              View open caveats through the Bug Search tool, which is located at:

https://tools.cisco.com/bugsearch/

Deploy the chosen release in a lab environment that uses the same product components as your product components before moving
                              to a production environment.

If you want to deploy Cisco TelePresence Conductor, the product is now End of Software Maintenance:

https://www.cisco.com/c/en/us/products/collateral/conferencing/telepresence-conductor/eos-eol-notice-c51-739456.html

### Latest Software Upgrades

The following are links to the latest software upgrades for Cisco Collaboration Systems Release components.

To launch the Product Upgrade Tool, go to:

https://upgrad.cloudapps.cisco.com/upgrad/jsp/index.jsp

To download the latest software for all other components, go to:

https://software.cisco.com/download/home

## Component Versions

For current Cisco Collaboration Systems Release compatible component versions, refer to the Cisco Collaboration Systems Compatibility Matrix .

Product-specific compatibility documents provide complete compatibility information between components.

Not all Collaboration System product release versions may be available at the same time. For latest product version availability,
                              see individual product support pages at, Support and Downloads .

You can set up a virtualized environment by running collaboration applications on a virtual machine on a Unified Computing
                                 System (UCS). For more details, including UCS hardware information and third-party requirements, see:

https://www.cisco.com/go/virtualized-collaboration

Cisco Hosted Collaboration Solution (Cisco HCS) is a hosted solution that includes various Cisco Collaboration Systems release
                              components. For more information about Cisco HCS, see: Cisco Hosted Collaboration Solution and Cisco HCS Product Support .

## Related Documentation

### Product Components

For documentation that covers the product components that make up a Cisco Collaboration Systems Release, refer to the below
                        table. For each product component, the table provides links to:

Product Overview pages, from which you can access general product information such as product data sheets and additional marketing material.

Documentation pages, from which you can access technical documentation such as release notes, design, installation, configuration, and
                              troubleshooting guides.

For details about which product versions are recommended for this Collaboration Systems Release, see Cisco Collaboration Systems
                                    Release Compatibility Matrix at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/unified/communications/system/Compatibility/CSR-Compatibility-Matrix.html .

Component

Links

Calling

Cisco Unified Communications Manager

Product Overview

Documentation

Cisco Webex Calling

Product Overview

Documentation

Hybrid Call Service

Cisco Business Edition 6000

Product Overview

Documentation

Cisco Business Edition 7000

Product Overview

Documentation

Cisco Emergency Responder

Product Overview

Documentation

Cisco Paging Server

Product Overview

Documentation

Cisco Paging Server 14 is not available as of Cisco Collaboration Systems Release 14 General Availability. Paging Server 14
                                             is expected to release in June 2021.

Cisco Unified Attendant Console Standard

Product Overview

Documentation

Cisco Unified Attendant Console Advanced

Product Overview

Documentation

Cisco Unified Communications Manager Express

Product Overview

Documentation

Cisco Unified Survivable Remote Site Telephony

Product Overview

Documentation

Voicemail

Cisco Unity Connection

Product Overview

Documentation

Cisco Unity Express

Product Overview

Documentation

Messaging

Cisco Unified Communications Manager IM & Presence Service

Product Overview

Documentation

Cisco Webex

Product Overview

Hybrid Message Service, Hybrid Calendar Service

Enterprise Edge

Cisco Expressway Series

Product Overview

Documentation

Cisco Unified Border Element

Product Overview

Documentation

Cisco Unified SIP Proxy

Product Overview

Documentation

Meetings

Cisco Meeting Server

Product Overview

Documentation

Cisco Meeting App

Documentation

Cisco Meeting Management

Documentation

Cisco Webex Meetings

Product Overview

Documentation

Cisco Webex Meetings Server

Product Overview

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

Cisco TelePresence Video Communication Server

Product Overview

Documentation

As of the publishing date, this product is still available, but the End of Sale date is announced.

Endpoints

Cisco Headset 500 Series

Product Overview

Documentation

Cisco Headset 700 Series

Product Overview

Documentation

Cisco Webex Board Series

Product Overview

Documentation

Cisco Webex Desk Series

Product Overview

Documentation

Cisco Webex Room Phone

Product Overview

Documentation

Cisco Webex Room Series

Product Information

Documentation

Cisco Webex Share

Product Information

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

Cisco Webex app

Product Overview

Documentation

Service Management

Cisco Prime Collaboration (Provisioning, Assurance)

Product Overview

Documentation

Cisco Prime Collaboration (Deployment)

Product Overview

Documentation

Cisco Webex Cloud-Connected UC

Product Overview

Documentation

Cisco Directory Connector

Hybrid Services Directory

Communication Gateways

Cisco IOS 15 M&T

Documentation

Cisco IOS XE 17

Documentation

Cisco ATA 180 Series Analog Telephone Adapters

Product Overview

Documentation

Cisco ATA 190 Series Analog Telephone Adapters

Product Overview

Documentation

Cisco VG Series Gateways

Product Overview

Documentation

Cisco ASR 1000 Routers

Product Overview

Documentation

Cisco 2900 Series Integrated Services Routers (EOS)

Product Overview

Documentation

Cisco 3900 Series Integrated Services Routers

Product Overview

Documentation

Cisco 4000 Series Integrated Services Routers

Product Overview

Documentation

Cisco Catalyst 8300 Edge Series Platform

Product Overview

Documentation

### Managed Services Documentation

For information about managed services of certain products, refer to the product support documentation. For example, see the Managed Services Guide for Cisco Unified Communications Manager, Release 14 at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

## Limitations and Restrictions

If you are a Cisco partner or a registered Cisco.com user with a Cisco service contract, you can use the Bug Search tool to
                     find caveats of any severity for any release. Access Bug Search at: https://bst.cloudapps.cisco.com/bugsearch/ .

We offer a Cisco Notification Service that allows you to set up one or more profiles. These profiles enable you to receive
                     email notification of new Field Notices, Product Alerts, or End of Sale information for the products that you have selected.
                     The Product Alert Tool is available at: https://www.cisco.com/cisco/support/notifications.html .

### Important Notes

This section includes important notes related to the testing of this Cisco Collaboration Systems Release.

#### MRA Phones Require Activation Code Onboarding

As of Release 14, if you are onboarding supported Cisco IP Phone 78xx Series and 88xx Series phones for Mobile and Remote
                           Access, the phones switch to MRA mode only if the Allow Activation Code via MRA check box is checked within the Phone Configuration window of Cisco Unified Communications Manager. Using this approach, you must configure Activation Code onboarding for MRA
                           phones. In addition, the MRA phone user must enter the correct activation code in order to activate and use the phone.

For details on configuring Activation Code Onboarding, see the "Device Onboarding via Activation Codes" chapter of the Feature Configuration Guide for Cisco Unified Communications Manager.

### Open Caveats

The following table contains a list of open caveats with Cisco Collaboration Systems Release 14.

Caveat

Description

CSCvm84478

TLS SIP Trunk Out of Service due to race condition caused by multiple Reset/Restarts

CSCvs58554

Phone stops trying registration, see two 'downd' process alive

CSCvw17487

Conference participants except the host are not listed in conflist

CSCvw68373

Subscriber Upgrade is stuck in databaseInstall when performing a standard Install/Upgr

CSCvx22242

Exception in AXL APIs - 'The cursor has been previously released and is unavailable'

CSCvx22651

CCM process cores due to memory exhaustion caused by sip device Alarm UC_CALLMANAGER-6-StationAlarm

CSCvx25564

Use download credentials and software location from Publisher (yes/no), does not give Error message

CSCvx56062

Failed to generate Multi-Server (SAN) CSR with different OSAdmin password for nodes in the cluster

CSCvx63367

IP Phone 7800 display is stuck in activation code screen when onboarded on-prem with mramode

CSCvx64219

DB-Replication failed to complete after L2 upgrade, tables out-of-sync/DB Active-Dropp

CSCvx70719

Restore on CUSP 10.2.1 is failing

CSCvx74452

ISR4461 Cored under load during SRTP packet processing in DP

CSCvx85953

Failed to enable remote_account on UCM subscriber node after L2 upgrade

## Troubleshooting

For troubleshooting information, tips, and recommendations related to Cisco Collaboration Systems Releases, see individual
                     product Troubleshooting Guides located in Component Documentation .

### This Document Applies to These Products

- Collaboration Systems Release 14

| Note | Not all Collaboration System product release versions may be available at the same time. For latest product version availability,
                                 see individual product support pages at, Support and Downloads . |
|---|---|

| Note | The following phone models are End-of-Support as of March 31 2021: 3911, 3951, 6911, 6921, 6941, 6945, 6961, 7902G, 7905G,
                                          7906G, 7911G, 7912G, 7915 7925G, 7925G-EX, 7926G, 7931G, 7936, 7937G, 7940G, 7941G, 7941G-GE, 7942G, 7960G, 7961G, 7961G-GE,
                                          7962G, 7970G, 7971G-GE, 7985G, 8941, 8945, 8961 |
|---|---|

| Note | Many phone models are deprecated in Cisco Unified Communications Manager Releases 11.5(x) and up. Deprecated phone models
                                          will not work in the Unified Communications Manager for which they are deprecated. For information on which phone models are
                                          deprecated, and as of which release, see the Deprecated Phone Models notice. |
|---|---|

| Note | The following gateway models are End-of-Support as of March 31, 2021: Cisco VG202 Analog Voice Gateway, Cisco VG204 Analog
                                          Voice Gateway, Cisco VG224 Analog Voice Gateway, Cisco VG248 48-PortAnalog Voice Gateway, Cisco 2800 Series Integrated Services
                                          Routers, Cisco 3800 Series Integrated Services Routers, Cisco ATA 187 Analog Telephony Adapter. |
|---|---|

| Note | For your reference, see the Cisco Collaboration Systems Release Design Guides . |
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

| Note | For details about which product versions are recommended for this Collaboration Systems Release, see Cisco Collaboration Systems
                                    Release Compatibility Matrix at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/unified/communications/system/Compatibility/CSR-Compatibility-Matrix.html . |
|---|---|

| Component | Links |
|---|---|
| Calling |
| Cisco Unified Communications Manager | Product Overview Documentation |
| Cisco Webex Calling | Product Overview Documentation Hybrid Call Service |
| Cisco Business Edition 6000 | Product Overview Documentation |
| Cisco Business Edition 7000 | Product Overview Documentation |
| Cisco Emergency Responder | Product Overview Documentation |
| Cisco Paging Server | Product Overview Documentation Note Cisco Paging Server 14 is not available as of Cisco Collaboration Systems Release 14 General Availability. Paging Server 14
                                             is expected to release in June 2021. | Note | Cisco Paging Server 14 is not available as of Cisco Collaboration Systems Release 14 General Availability. Paging Server 14
                                             is expected to release in June 2021. |
| Note | Cisco Paging Server 14 is not available as of Cisco Collaboration Systems Release 14 General Availability. Paging Server 14
                                             is expected to release in June 2021. |
| Cisco Unified Attendant Console Standard | Product Overview Documentation |
| Cisco Unified Attendant Console Advanced | Product Overview Documentation |
| Cisco Unified Communications Manager Express | Product Overview Documentation |
| Cisco Unified Survivable Remote Site Telephony | Product Overview Documentation |
| Voicemail |
| Cisco Unity Connection | Product Overview Documentation |
| Cisco Unity Express | Product Overview Documentation |
| Messaging |
| Cisco Unified Communications Manager IM & Presence Service | Product Overview Documentation |
| Cisco Webex | Product Overview Hybrid Message Service, Hybrid Calendar Service |
| Enterprise Edge |
| Cisco Expressway Series | Product Overview Documentation |
| Cisco Unified Border Element | Product Overview Documentation |
| Cisco Unified SIP Proxy | Product Overview Documentation |
| Meetings |
| Cisco Meeting Server | Product Overview Documentation |
| Cisco Meeting App | Documentation |
| Cisco Meeting Management | Documentation |
| Cisco Webex Meetings | Product Overview Documentation |
| Cisco Webex Meetings Server | Product Overview Documentation |
| Cisco TelePresence Management Suite | Product Overview Documentation |
| Cisco TelePresence Management Suite Provisioning Extension | Product Overview Documentation |
| Cisco TelePresence Management Suite Extension for Microsoft Exchange | Product Overview Documentation |
| Cisco TelePresence Server on Virtual Machine (EOS) | Product Overview Documentation |
| Cisco TelePresence Server on Multiparty Media 820 (EOS) | Product Overview Documentation |
| Cisco TelePresence Conductor (EOS) | Product Overview Documentation |
| Cisco TelePresence MCU 5300 Series (EOS) | Product Overview Documentation |
| Cisco Collaboration Meeting Rooms (CMR) Cloud | Product Overview Documentation |
| Cisco Collaboration Meeting Rooms (CMR) Hybrid | Release Notes, Documentation, and Product Overview |
| Cisco TelePresence Video Communication Server | Product Overview Documentation Note As of the publishing date, this product is still available, but the End of Sale date is announced. | Note | As of the publishing date, this product is still available, but the End of Sale date is announced. |
| Note | As of the publishing date, this product is still available, but the End of Sale date is announced. |
| Endpoints |
| Cisco Headset 500 Series | Product Overview Documentation |
| Cisco Headset 700 Series | Product Overview Documentation |
| Cisco Webex Board Series | Product Overview Documentation |
| Cisco Webex Desk Series | Product Overview Documentation |
| Cisco Webex Room Phone | Product Overview Documentation |
| Cisco Webex Room Series | Product Information Documentation |
| Cisco Webex Share | Product Information Documentation |
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
| Cisco Webex app | Product Overview Documentation |
| Service Management |
| Cisco Prime Collaboration (Provisioning, Assurance) | Product Overview Documentation |
| Cisco Prime Collaboration (Deployment) | Product Overview Documentation |
| Cisco Webex Cloud-Connected UC | Product Overview Documentation |
| Cisco Directory Connector | Hybrid Services Directory |
| Communication Gateways |
| Cisco IOS 15 M&T | Documentation |
| Cisco IOS XE 17 | Documentation |
| Cisco ATA 180 Series Analog Telephone Adapters | Product Overview Documentation |
| Cisco ATA 190 Series Analog Telephone Adapters | Product Overview Documentation |
| Cisco VG Series Gateways | Product Overview Documentation |
| Cisco ASR 1000 Routers | Product Overview Documentation |
| Cisco 2900 Series Integrated Services Routers (EOS) | Product Overview Documentation |
| Cisco 3900 Series Integrated Services Routers | Product Overview Documentation |
| Cisco 4000 Series Integrated Services Routers | Product Overview Documentation |
| Cisco Catalyst 8300 Edge Series Platform | Product Overview Documentation |

| Note | Cisco Paging Server 14 is not available as of Cisco Collaboration Systems Release 14 General Availability. Paging Server 14
                                             is expected to release in June 2021. |
|---|---|

| Note | As of the publishing date, this product is still available, but the End of Sale date is announced. |
|---|---|

| Caveat | Description |
|---|---|
| CSCvm84478 | TLS SIP Trunk Out of Service due to race condition caused by multiple Reset/Restarts |
| CSCvs58554 | Phone stops trying registration, see two 'downd' process alive |
| CSCvw17487 | Conference participants except the host are not listed in conflist |
| CSCvw68373 | Subscriber Upgrade is stuck in databaseInstall when performing a standard Install/Upgr |
| CSCvx22242 | Exception in AXL APIs - 'The cursor has been previously released and is unavailable' |
| CSCvx22651 | CCM process cores due to memory exhaustion caused by sip device Alarm UC_CALLMANAGER-6-StationAlarm |
| CSCvx25564 | Use download credentials and software location from Publisher (yes/no), does not give Error message |
| CSCvx56062 | Failed to generate Multi-Server (SAN) CSR with different OSAdmin password for nodes in the cluster |
| CSCvx63367 | IP Phone 7800 display is stuck in activation code screen when onboarded on-prem with mramode |
| CSCvx64219 | DB-Replication failed to complete after L2 upgrade, tables out-of-sync/DB Active-Dropp |
| CSCvx70719 | Restore on CUSP 10.2.1 is failing |
| CSCvx74452 | ISR4461 Cored under load during SRTP packet processing in DP |
| CSCvx85953 | Failed to enable remote_account on UCM subscriber node after L2 upgrade |