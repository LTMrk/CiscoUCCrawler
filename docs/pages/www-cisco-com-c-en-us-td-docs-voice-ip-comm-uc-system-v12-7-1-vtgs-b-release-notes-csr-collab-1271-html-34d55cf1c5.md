---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-v12-7-1-vtgs-b-release-notes-csr-collab-1271-html-34d55cf1c5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/V12_7_1/vtgs_b_release-notes-csr-collab-1271.html
retrieved_at: 2026-08-16T18:26:52.662321+00:00
---

Release Notes for Cisco Collaboration Systems Release 12.7 and 12.8

# Release Notes for Cisco Collaboration Systems Release 12.7 and 12.8

### Download Options

Updated: February 10, 2020

First Published: February 5, 2020

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

### Release 12.7

Cisco Collaboration Systems Release 12.7 aligns with the following core Cisco Collaboration application releases:

Cisco Unified Communications Manager 12.5(1)SU2

IM and Presence Service 12.5(1)SU2

Cisco Unity Connection 12.5(1)SU2

Cisco Emergency Responder 12.5(1)SU2

Cisco Expressway X12.5.6

Supported Cisco IP Phone 78xx and 88xx Series 12.7(1)

Cisco Jabber (on Android, iPhone, iPad, Mac or Windows) 12.7

For a detailed breakdown of product components and up to date Recommended releases that make up the Cisco Collaboration Systems
                     Release, see Cisco Collaboration Systems Release Compatibility Matrix .

### Release 12.8

Cisco Collaboration Systems Release 12.8 aligns with the following core Cisco Collaboration application releases:

Cisco Unified Communications Manager 12.5(1)SU3 and SU4

IM and Presence Service 12.5(1)SU3 and SU4

Cisco Unity Connection 12.5(1)SU3 and SU4

Cisco Emergency Responder 12.5(1)SU3 and SU4

Cisco Expressway X12.6 and X12.7

Supported Cisco IP Phone 78xx and 88xx Series 12.8(1)SR2

Cisco Jabber (on Android, iPhone, iPad, Mac or Windows) 12.9.x

For a detailed breakdown of product components and up date Recommended releases that make up the Cisco Collaboration Systems
                     Release, see Cisco Collaboration Systems Release Compatibility Matrix .

## Tested Functionality

System-wide testing was done for features and upgrade paths.

### Feature Testing

#### Release 12.7

The following features were tested for CSR 12.7 release:

Cisco Headsets 2.0 release include the following updates:

Easy integration with Webex Teams and Webex Meetings

Cisco Headset support for Contact Center

Launch of Cisco Headset 700 series

Simple Phone Replacement with Self-Provisioning and Native Migration— The Self-Provisioning feature is now enhanced with re-provisioning
                              support. This helps provisioning by allowing the following use case: an engineer provisions the phone on day 1 to a generic
                              identity. An end user re-provisions the phone on day 2 to himself.

OCSP Revocation for Common Criteria Certification—Online Certificate Status Protocol enhancements help your deployment comply
                              with Common Criteria requirements by ensuring that your system doesn’t make TLS connections to entities whose certificates
                              are revoked.

Active Directory 2019 Support

Activation Code Onboarding for MPP and Broadcloud—You can now use device activation codes to onboard Cisco TelePresence endpoints
                              for MPP and Broadcloud deployments. This includes both on-premise and MRA deployments.

Jabber LDAP Security Credentials—You can now configure Cisco Jabber with secure LDAP credentials via a Service Profile in
                              Unified Communications Manager.

HCS CLR Support—Improved control at a granular level for the External Line Presentation number.

Cisco Emergency Responder Customized Email—Administrators can now customize Email Alert Notifications for 911 Emergency Calls.

Cisco Emergency Responder Switch Support—Support is enhanced to include selected Meraki MS355 switches and Cisco Catalyst
                              1000 switches.

IM and Presence Service Hardening—The IM and Presence Service has been hardened to secure the system as a part of Common Criteria
                              requirements.

Smart Licensing Reservation Hierarchy—The Smart Licensing Export Compliance requirements are updated making it easier to deploy
                              encryption features for satellite deployments.

#### Release 12.8

The following features were tested for Release 12.8:

Push Notifications updates:

iOS13 SDK updates—Apple Push Notifications support includes enhancements with iOS13, including Push Notification Caller ID,
                                    External Presentation Name and Number support and active registration node for call failover.

iOS13 SDK updates for China—Apple Push Notifications support includes iOS13 udpates that are targeted specifically to China.

Android Push Notifications support—Push Notifications support is now offered for Jabber and Webex Teams clients that run on
                                    Android.

Native Phone Refresh—The native Phone Migration service makes it easy to replace old and obsolete phones. Feature testing
                              included proxy TFTP deployment tests.

Headset-based Extension Mobility Login—Headset Services allow you to connect Cisco Headset into a supported Device to provide
                              simple and integrated user-focused experiences such as Headset-based Extension Mobility login.

E911 Compliance - Kari's Law—Unified Communications Manager supports emergency call routing regulations that let your system
                              comply with regulations such as Kari's Law

Lower Your Voice Banner and SPAM Update—For open office envirnoCisco IP Phones include a ba feature updates targeted to open
                              offices that . In addition, you can tag incoming calls as SPAM so that future calls from that number go straight to voicemail.

Headset Dongle for Jabber

Cisco Webex Room Phone—Cisco Webex Room Phone provides a collaborate work experience for huddle spaces and meeting rooms.
                              You can use the phone to make calls, to share information, and to collaborate during meetings. Connect a screen display, and
                              you can collaborate with everyone in the room.

Webex Cloud Connected UC

Security Readiness—Cisco Collaboration applications were tested for security readiness.

#### Feature Testing for Cisco Unified Communications Manager, Release 12.5(1)SU4

The Cisco Collaboration Systems Release Team also completed testing in support of Cisco Unified Communications Manager, Release
                        12.5(1)SU4. Testing includes support for the Cisco Catalyst 8300 Series Edge Platform , which is supported with 12.5(1)SU4.

For a complete breakdown of the features that are a part of this release, see Release Notes for Cisco Unified Communications Manager, Release 12.5(1)SU4 at https://www.cisco.com/content/en/us/td/docs/voice_ip_comm/cucm/rel_notes/12_5_1/SU4/cucm_b_release-notes-for-cucm-imp-1251su4.html .

### Upgrade Paths

The system-wide functionality testing included verifying upgrade paths across various product components for a single stage
                        upgrade from Cisco Collaboration Systems Release 12.0 to Cisco Collaboration Systems Release 12.5, 12.6, 12.7 and 12.8.

For a list of versions that are compatible with  this release of Cisco Collaboration Systems, see the Cisco Collaboration Systems Compatibility Matrix .

## New and Changed Features

For details about what is new for Cisco Collaboration Systems Release 12.5, 12.6, and 12.7 see the Solution Overview .

For details about new and changed collaboration product features, access individual product release notes from Product Documentation .

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

### Collaboration Systems Documentation

For systems documentation that covers Cisco Collaboration Systems Releases 12.5 through 12.8, go to https://www.cisco.com/c/en/us/support/unified-communications/collaboration-systems-release-12-5/model.html

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

### Solution Feature Documentation

Refer to the below links for information on how to configure and use the following solution features, which were added for
                        this release:

Certificate Monitoring and Revocation with OCSP —Refer to this document for information on how to set up certicate monitoring and certificate revocation via the Online Certificate
                              Status Protocol (OCSP).

Simple Phone Replacement with Self-Provisioning —For information on how to use Unified Communications Manager's Self-Provisioning feature to migrate and replace existing
                              phones, refer to Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2 .

Cisco Headset Management —For details on how to use Cisco Headset Serviceability to manage Cisco Headset 500 series and 700 series headset deployments
                              from Unified Communications Manager, refer to Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2 .

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

#### show dspfarm profile Information Not Displayed

In calls from endpoints that don’t support Keypad Markup Language (KPML), the show dspfarm profile command doesn’t show the
                           actual resources being used. The profile shows only the SCCP connections. For more details, see CSCvd91119 .

#### Caller-ID Not Changed After Transfer

On Cisco Webex Call phones, the caller-ID is not updated properly after a transfer from enterprise phones. For more details,
                           see CSCve56223 .

### Open Caveats

#### Open Caveats for Cisco Collaboration Systems Release 12.7

The following table contains open caveats for Cisco Collaboration Systems Release 12.7.

Caveat

Description

CSCvp11701

Improve Recovery for Issues at CCM Startup or Fail Completely

CSCvr96670

Insufficient PAWS logging for PCD initiated upgrade being stuck

After L2 upgrade UCM Subscriber node loose NTP configuration if NTP process does not start properly.

CSCvr96670

Insufficient PAWS logging for PCD initiated upgrade being stuck

CSCvs80927

HEADSET_MGMT:MRA 886X connected Sunkist unable to upgrade firmware when upgrade source as CUCM only

CSCvs88408

HEADSET_MGMT:MRA 886X connected 56x HS unable to upgrade firmware ...

CSCvs38748

After L2 upgrade UCM Subscriber node loose NTP configuration if NTP process does not start properly.

#### Open Caveats for Cisco Collaboration Systems Release 12.8

The following table contains open caveats for Cisco Collaboration Systems Release 12.8.

Caveat

Description

CSCvu81967

IM&P cluster L2 upgrade, Auto switch-version fails for a subscriber node in 6 nodes cluster

CSCvv03282

Getting bad request while clearing 100 calls from the failed call search list

CSCvv11252

Off-premise device not displaying Legal disclaimer after upgrade

CSCvv13694

Jabber 12.9 release note needs to be updated with the information on Silent Monitor support

CSCvv18139

E911Proxy stops working

CSCvv18464

Push notifications are not enabled on Jabber after CUCM upgrade

CSCvv20152

Inactive core seen on IMnP node core.7446.11.EspConfigAgent.1594806539

CSCvv23410

CUSP online help should be updated with the correct steps for configuring the backup parameters

CSCvv23379

Guest OS and ESXi compatibility are showing older version for CUSP 10.2

CSCvv29379

Call Manager subscriber nodes DB not coming up after restart

CSCvv33657

Kernel panic seen on CUCM subscriber node after while powering it on after a glitch

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

| Caveat | Description |
|---|---|
| CSCvp11701 | Improve Recovery for Issues at CCM Startup or Fail Completely |
| CSCvr96670 | Insufficient PAWS logging for PCD initiated upgrade being stuck |
| CSCvs38748 | After L2 upgrade UCM Subscriber node loose NTP configuration if NTP process does not start properly. |
| CSCvr96670 | Insufficient PAWS logging for PCD initiated upgrade being stuck |
| CSCvs80927 | HEADSET_MGMT:MRA 886X connected Sunkist unable to upgrade firmware when upgrade source as CUCM only |
| CSCvs88408 | HEADSET_MGMT:MRA 886X connected 56x HS unable to upgrade firmware ... |
| CSCvs38748 | After L2 upgrade UCM Subscriber node loose NTP configuration if NTP process does not start properly. |

| Caveat | Description |
|---|---|
| CSCvu81967 | IM&P cluster L2 upgrade, Auto switch-version fails for a subscriber node in 6 nodes cluster |
| CSCvv03282 | Getting bad request while clearing 100 calls from the failed call search list |
| CSCvv11252 | Off-premise device not displaying Legal disclaimer after upgrade |
| CSCvv13694 | Jabber 12.9 release note needs to be updated with the information on Silent Monitor support |
| CSCvv18139 | E911Proxy stops working |
| CSCvv18464 | Push notifications are not enabled on Jabber after CUCM upgrade |
| CSCvv20152 | Inactive core seen on IMnP node core.7446.11.EspConfigAgent.1594806539 |
| CSCvv23410 | CUSP online help should be updated with the correct steps for configuring the backup parameters |
| CSCvv23379 | Guest OS and ESXi compatibility are showing older version for CUSP 10.2 |
| CSCvv29379 | Call Manager subscriber nodes DB not coming up after restart |
| CSCvv33657 | Kernel panic seen on CUCM subscriber node after while powering it on after a glitch |