---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-v12-6-1-vtgs-b-csr-collaboration-release-notes-1261-html-237ca89db2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/V12_6_1/vtgs_b_csr-collaboration-release-notes-1261.html
retrieved_at: 2026-08-16T18:27:00.659885+00:00
---

Release Notes for Cisco Collaboration Systems Release 12.6

# Release Notes for Cisco Collaboration Systems Release 12.6

### Download Options

Updated: June 24, 2019

First Published: June 19, 2019

Last Updated: May 17, 2021

# Introduction to Cisco Collaboration Systems

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

Call Control components, such as Cisco Unified Communications Manager, Cisco Unified Communications Manager IM and Presence
                     Service, Cisco Business Edition, Cisco Unified Communications Manager Express, and Cisco Unified Survivable Remote Site Telephony.

Conferencing components, such as Cisco Meeting Server, Cisco Meeting App, Cisco Meeting Management, Cisco TelePresence Management
                     Suite, Cisco TelePresence Management Suite Provisioning Extension, and Cisco TelePresence Management Suite Extension for Microsoft
                     Exchange.

Enterprise Edge components, such as Cisco Expressway Series and Cisco Unified Border Element.

Server Applications, such as Cisco Emergency Responder, Cisco Paging Server, and Cisco Unified Attendant Consoles.

Cloud and Hybrid Services, such as Cisco Webex Teams, Cisco Webex Meetings for Cisco Collaboration Meeting Rooms (CMR) Cloud,
                     Cisco Webex Meetings Server, Cisco Webex Meetings, and Cloud Webex Edge Video Mesh.

Voicemail and Messaging components, such as Cisco Unity Connection and Cisco Unity Express.

Endpoint components, such as Cisco IP Phone Series, Cisco Webex Desk Series, Cisco Webex Room Series, Cisco TelePresence IX5000,
                     Cisco Jabber, and Cisco Jabber Softphone for VDI.

Service Management components, such as Cisco Prime Collaboration.

Communication Gateway components, such as Cisco Integrated Services Routers (ISR).

## Collaboration Release Alignment

Cisco Collaboration Systems Release 12.6 aligns with the following core Collaboration applications:

Cisco Unified Communications Manager 12.5(1)SU1

IM and Presence Service 12.5(1)SU1

Cisco Unity Connection 12.5(1)SU1

Cisco Emergency Responder 12.5(1)SU1

Cisco Expressway X12.5

Supported Cisco IP Phone 78xx and 88xx Series 12.5(1)SR3

Cisco Jabber (on Android, iPhone, iPad, Mac or Windows) 12.6

For a detailed breakdown of product components and up to date Recommended releases for the Cisco Collaboration Systems Release,
                     see Cisco Collaboration Systems Release Compatibility Matrix .

## Tested Functionality

System-wide testing was done for features and upgrade paths.

### Feature Testing for 12.6

In Release 12.6, the following solution features were tested:

#### Simplicity Features (Ordering, Deploying, Managing and Upgrading)

Headset Provisioning and Management via Cisco Unified Communications Manager —You can now configure customized headset templates for Cisco headsets. In addition, Headset Serviceability updates let you
                              manage your headset inventory and call diagnostics for headsets right from the Cisco Unified Communications Manager user interface.

Video Endpoint Provisioning via Cisco Unified Communications Manager —This feature makes it simpler to provision and manage Cisco TelePresence video endpoints. In addition to provisioning, administrators
                              can also configure the Product-Specific Configuration fields that previously could be assigned only from the endpoint itself.

Enhanced Location Tracking for Cisco Jabber —The Location Awareness feature now includes location tracking for Cisco Jabber clients.

#### Mobile and Remote Access

Activation Code Onboarding over MRA —Device activation code support is enhanced to include the onboarding of supported 7800 and 8800 series phones over Mobile
                              and Remote Access (MRA).

Active Control for Cisco Jabber over MRA —The Encrypted iX channel lets Cisco Jabber clients assume active control of conferences while connecting via MRA

SIP OAuth Mode for Cisco Jabber over MRA —SIP OAuth Mode privodes encrypted signalling and media without impacting the Certificate Authority Proxy Function (CAPF).
                              This release updates SIP OAuth Mode support to include Cisco Jabber clients whom are connecting via MRA.

#### Security & Compliance Features

Encryption of Data at Rest —Self-encrypting hardware drives further enhance your deployment's security in the event that a hardware drive is lost or
                              replaced.

#### Recording

CTI Monitoring for Mobile Recording —This feature provides CTI monitoring for the recording of calls over mobile devices. This feature provides partners in the
                              financial industry with additional support that lets their system comply with MiFID requirements. (MiFID Phase I)

#### Licensing

Smart Licensing for CUBE —The Smart Licensing feature is updated to include licensing for the trunk side of a Cisco Unified Border Element.

#### Webex Calling Interop

Webex Calling Interop Updates —Webex interoperability updates include local gateway support.

#### Product-Specific Features

Session ID in Logs —New Session ID CDR and CMR records are added to Cisco Unified Communications Manager to provide additional call session analytics.

SIP Line Support for Gateway —VG450 and ISR 4461 gateways are enhanced to support FXS ports that register to Unfiied Communications Manager. This update
                              lets you register analog phones as SIP endpoints.

### Upgrade Paths

The system-wide functionality testing included verifying upgrade paths across various product components for a single stage
                        upgrade from Cisco Collaboration Systems Release 12.0 to Cisco Collaboration Systems Release 12.5, 12.6, 12.7 and 12.8.

For a list of versions that are compatible with  this release of Cisco Collaboration Systems, see the Cisco Collaboration Systems Compatibility Matrix .

## New and Changed Features

For details about what is new for Cisco Collaboration Systems Release 12.5, 12.6, and 12.7 see the Solution Overview .

## System Requirements

This section provides information about system requirements for this Cisco Collaboration Systems Release.

### End-of-Sale Components

#### Product Components that are End of Sale

As of March 31, 2021, the following product components are End-of-Sale (EOS), but are still supported. Refer to the corresponding
                        link for up to date information.

Cisco TelePresence MX700D, MX800S, 800D, End of Life and End of Sale Notices

Cisco TelePresence MX300G2, End of Life and End of Sale Noticices

Cisco TelePresence MX200G2, End of Life and End of Sale Notices

Cisco TelePresence SX10, SX20, SX80, End of Life and End of Sale Notices

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

Cisco Expressway, End of Life and End of Sale Notices

Cisco Unified Border Element, End of Life and End of Sale Notices

Cisco Jabber for Windows, End of Life and End of Sale Notices

Cisco Jabber for Mac, End of Life and End of Sale Notices

Cisco Jabber for iOS, End of Life and End of Sale Notices

Cisco Jabber for Android, End of Life and End of Sale Notices

Cisco Jabber Softphone for VDI, End of Life and End of Sale Notices

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

### System Documentation

For high-level information about Cisco Collaboration Systems, see Cisco Collaboration Systems Solution and Component Support Documentation and Downloads .

### Product Documentation

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

Contact Center

Cisco Packaged Contact Center Enterprise

Product Information

Documentation

Cisco Unified Contact Center Express

Product Information

Documentation

Cisco Unified Contact Center Enterprise

Product Information

Documentation

Cisco Finesse

Product Information

Documentation

Cisco Unified Intelligence Center

Product Information

Documentation

Cisco Virtualized Voice Browser

Documentation

Cisco Unified Intelligent Contact Management Enterprise

Product Information

Documentation

Cisco Unified Customer Voice Portal

Product Information

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

Cisco IOS XE 16

Documentation

Cisco Unified SIP Proxy

Product Overview

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

#### System Crashes when Allocating Memory for Multiple Threads Simultaneously

Cisco Unified Communications Manager has been observed to crash in situations with very heavy call loads. This may occur due
                           to multiple threads allocating memory simultaneously. In normal conditions, this situation does not occur as simultaneous
                           memory allocation would not occur.

For additional details, see CSCvn77809 .

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

## Troubleshooting

For troubleshooting information, tips, and recommendations related to Cisco Collaboration Systems Releases, see individual
                     product Troubleshooting Guides located in Component Documentation .

### This Document Applies to These Products

- Collaboration Systems Release 12.5

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
| Cisco Paging Server | Product Overview Documentation |
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
| Contact Center |
| Cisco Packaged Contact Center Enterprise | Product Information Documentation |
| Cisco Unified Contact Center Express | Product Information Documentation |
| Cisco Unified Contact Center Enterprise | Product Information Documentation |
| Cisco Finesse | Product Information Documentation |
| Cisco Unified Intelligence Center | Product Information Documentation |
| Cisco Virtualized Voice Browser | Documentation |
| Cisco Unified Intelligent Contact Management Enterprise | Product Information Documentation |
| Cisco Unified Customer Voice Portal | Product Information Documentation |
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
| Service Management |
| Cisco Prime Collaboration (Provisioning, Assurance) | Product Overview Documentation |
| Cisco Prime Collaboration (Deployment) | Product Overview Documentation |
| Cisco Webex Cloud-Connected UC | Product Overview Documentation |
| Cisco Directory Connector | Hybrid Services Directory |
| Communication Gateways |
| Cisco IOS 15 M&T | Documentation |
| Cisco IOS XE 16 | Documentation |
| Cisco Unified SIP Proxy | Product Overview Documentation |
| Cisco ATA 180 Series Analog Telephone Adapters | Product Overview Documentation |
| Cisco ATA 190 Series Analog Telephone Adapters | Product Overview Documentation |
| Cisco VG Series Gateways | Product Overview Documentation |
| Cisco ASR 1000 Routers | Product Overview Documentation |
| Cisco 2900 Series Integrated Services Routers (EOS) | Product Overview Documentation |
| Cisco 3900 Series Integrated Services Routers | Product Overview Documentation |
| Cisco 4000 Series Integrated Services Routers | Product Overview Documentation |

| Note | As of the publishing date, this product is still available, but the End of Sale date is announced. |
|---|---|