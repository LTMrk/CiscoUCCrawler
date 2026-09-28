---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-v12-5-1-vtgs-b-csr-contactcenter-release-notes-1251-html-b4baa27e8d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/V12-5-1/vtgs_b_csr-contactcenter-release-notes-1251.html
retrieved_at: 2026-08-16T18:27:04.649853+00:00
---

Release Notes for Contact Center: Cisco Collaboration Systems Release 12.5 and 12.6

# Release Notes for Contact Center: Cisco Collaboration Systems Release 12.5 and 12.6

### Download Options

Updated: June 19, 2019

First Published: February 11, 2019

Last Updated: June 19, 2019

# Introduction to Cisco Collaboration Systems Release for Contact Center

As part of our standard methodology for each Cisco Collaboration Systems Release, we:

Perform system-wide testing of Cisco Collaboration products to supplement the product-level testing performed on each collaboration
                     product.

Recommend compatible software releases that were verified by the testing teams. The recommendations are not exclusive and
                     are in addition to interoperability recommendations for each of the individual applications or products.

For software compatibility data, see the Cisco Collaboration Systems Release Compatibility Matrix .

Software compatibility data for all Cisco Collaboration Systems releases before 10.5(1) is available from the Cisco Collaboration Systems Compatibility Tool .

Not all Collaboration System product release versions may be available at the same time. For latest product version availability,
                              see individual product support pages at, Support and Downloads .

This document focuses on the Contact Center components tested as part of the Cisco Collaboration Systems Release. For information
               focused on Collaboration components that were tested as part of Cisco Collaboration Systems Release, see: https://cisco.com/go/unified-techinfo .

This document provides release notes details based on the system-wide testing which includes the following types of components:

Call control components, such as Cisco Unified Communications Manager (Unified CM), and Cisco Unified Communications Manager
                     IM and Presence Service.

Contact center components, such as Cisco Unified Contact Center Enterprise (Unified CCE), Cisco Packaged Contact Center Enterprise
                     (Packaged CCE), Cisco Unified Contact Center Express (Unified CCX), Cisco Unified Intelligence Center (Unified Intelligence
                     Center), Cisco Finesse, and Cisco Unified Customer Voice Portal (Unified CVP).

Enterprise Edge components such as Cisco TelePresence Video Communication Server, Cisco Unified Border Element (CUBE), and
                     Cisco Expressway Series.

Devices (Endpoints), such as Cisco DX Series (DX Series), Cisco IP Phone 7800/8800 Series (7800/8800 Series), Cisco Jabber
                     for Windows (Jabber for Windows) and Cisco Virtualization Experience Media Edition (VXME) for Windows.

Communications gateway components such as Cisco Integrated Services Routers (ISR).

## Tested Functionality

System-wide testing was done for features and upgrade paths.

### Feature Testing

In this release, the following features were system-tested:

#### Cisco Packed Contact Center Enterprise (Packaged CCE) 12.0(1)

Cisco IP Phones 8845 and 8865 in Packaged CCE environment

Jabber multi-line support for Packaged CCE features

FiNext: the new Finesse Agent Desktop

Single GUI for all the administrative configurations (replacing OAMP)

#### Cisco Unified Contact Center Express (Unified CCX) 12.0(1)

Jabber multi-line support for Unified CCX features

Unified CCX migration from RHEL 6 to CentOS 6.8

FiNext: the new Finesse Agent Desktop

Advanced Supervisor Capabilities

Agent to Agent chat: Agent can chat with another agent using the Finesse desktop without using Social Miner/DMZ

### Upgrade Paths

The system-wide functionality testing included verifying upgrade paths across various product components for a single stage
                        upgrade from Cisco Collaboration Systems Release 12.0 to Cisco Collaboration Systems Release 12.5 and 12.6.

For a list of versions that are compatible with Cisco Collaboration Systems Release 12.5 and 12.6, see the Cisco Collaboration Systems Compatibility Matrix .

## New and Changed Features

For details about what is new for Cisco Collaboration Systems Release 12.5 and 12.6, see the Solution Overview .

For details about new and changed contact center product features, access individual product release notes from Product Documentation .

## System Requirements

This section provides information about system requirements for this Cisco Collaboration Systems Release.

### End-of-Sale Components

The following components have reached end-of-sale (EOS) status but are still supported.

Cisco MediaSense, End-of-Sale and End-of-Life Notices

Cisco Unified E-Mail Interaction Manager, End-of-Sale and End-of-Life Notices

Cisco Unified Web Interaction Manager, End-of-Life and End-of-Sale Notices

Cisco TelePresence MCU 5300 Series, End-of-Sale and End-of-Life Notices

Cisco DX650, End-of-Sale and End-of-Life Notices

Cisco TelePresence System EX60 and EX90, End-of-Sale and End-of-Life Notices

Cisco Unified IP Phone 6911, 6921, 6941, 6945, 6961, End-of-Sale and End-of-Life Notices

Cisco Unified IP Phone 7937G, 7931G, 7942G, 7962G, Cisco Unified IP Phone Expansion Module 7915, Cisco Unified Wireless IP
                              Phone 7925G, 7925G-EX, 7926G, End-of-Sale and End-of-Life Notices :

The following are now End-of-Support: 7936, 7906G, 7911G, 7941G, 7961G, 7985G.

Cisco Unified Communications Manager Release 12.x does not support some deprecated phone models. For more information, see
                                          the related Field Notice .

Cisco Unified IP Phone 8941, 8945, 8961, End-of-Sale and End-of-Life Announcement

Cisco Unified IP Phones 9900 Series, End-of-Sale and End-of-Life Notices

Cisco Unity Express 7.1, 7.2, 8.5, and 8.6, End-of-Sale and End-of-Life Notices

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

Product Information pages, from which you can access product overview and marketing material such as product data sheets.

Product Documentation pages, from which you can access technical documentation such as Release Notes, Design, Installation, Configuration, and
                              Troubleshooting guides.

For details about component versions, see Component Versions .

Component

Links

Call Control

Cisco Unified Communications Manager

Product Information

Documentation

Cisco Unified Communications Manager IM and Presence Service

Product Information

Documentation

Contact Center

Cisco Unified Contact Center Enterprise

Product Information

Documentation

Cisco Packaged Contact Center Enterprise

Product Information

Documentation

Cisco Unified Contact Center Express

Product Information

Documentation

Cisco Unified Intelligence Center

Product Information

Documentation

Cisco MediaSense (End-of-Sale: Oct 4, 2017)

Product Information

Documentation

Cisco Finesse

Product Information

Documentation

Cisco Unified Customer Voice Portal

Product Information

Documentation

Cisco Virtualized Voice Browser

Documentation

Cisco Unified Intelligent Contact Management Enterprise

Product Information

Documentation

Cisco Unified E-Mail Interaction Manager (EOS)

Product Information

Documentation

Cisco Unified Web Interaction Manager (EOS)

Product Information

Documentation

Conferencing

Cisco TelePresence Conductor

Product Information

Documentation

Enterprise Edge

Cisco TelePresence Video Communication Server

Product Information

Documentation

Cisco Expressway Series

Product Information

Documentation

Cisco Unified Border Element

Product Information

Documentation

Endpoints

Cisco DX Series

Product Information

Documentation

Cisco TelePresence System EX Series (EOS)

Product Information

Documentation

Cisco Unified IP Phone 6901

Product Information

Documentation

Cisco Unified IP Phone 6911, 6921, 6941, 6945, 6961 (EOS)

Product Information

Documentation

Cisco IP Phone 7800 Series

Product Information

Documentation

Cisco Unified IP Phone 7900 Series

Product Information

Documentation

Cisco IP Phone 8800 Series

Product Information

Documentation

Cisco Unified IP Phone 8900 Series (EOS)

Product Information

Documentation

Cisco Unified IP Phone 9900 Series (EOS)

Product Information

Documentation

Cisco Jabber for Mac

Product Information

Documentation

Cisco Jabber for Windows

Product Information

Documentation

Cisco Virtualization Experience Media Edition for Windows

Product Information

Documentation

Cisco Virtualization Experience Media Edition for SUSE Linux

Product Information

Documentation

Cisco Jabber Guest

Product Information

Documentation

Communication Gateways

Cisco Unified SIP Proxy

Product Information

Documentation

Cisco 2900 Series Integrated Services Routers

Product Information

Documentation

Cisco 3900 Series Integrated Services Routers

Product Information

Documentation

Cisco 4400 Series Integrated Services Routers

Product Information

Documentation

## Limitations and Restrictions

If you are a Cisco partner or a registered Cisco.com user with a Cisco service contract, you can use the Bug Search tool to
                     find caveats of any severity for any release. Access Bug Search at: https://bst.cloudapps.cisco.com/bugsearch/ .

We offer a Cisco Notification Service that allows you to set up one or more profiles. These profiles enable you to receive
                     email notification of new Field Notices, Product Alerts, or End of Sale information for the products that you have selected.
                     The Product Alert Tool is available at: https://www.cisco.com/cisco/support/notifications.html .

### Important Notes

This section includes important notes related to the testing of this Cisco Collaboration Systems Release.

#### Push Notifications Calls Fail During Unified Communications Manager Failover

Incoming Push Notifications calls to Cisco Jabber on iPhone or iPad will fail if Cisco Unified Communications Manager is in
                           failover state and the Jabber client has been in standby mode for more than 3 minutes, or if Jabber is in a killed or swiped-away
                           state. In this case, to receive incoming Push Notifications calls, the mobile device, or the Jabber client, must be relauched.

For details, see CSCvj93746 .

### Open Caveats for 12.5

The following table lists known caveats, grouped by severity, related to Cisco Collaboration Systems Release testing. It also
                        includes caveats from previous releases, which were not resolved at the time this document was written. For more information
                        about each defect, click the linked caveat number in the Identifier column.

For information about a defect not listed in the table, go to Bug Search Tool .

Identifier

Headline

Severity 2-3 Caveats

CSCvo04890

Multiple observations on PCCE when VM tools are out of date for CUIC post upgrade

### Open Caveats for 12.6

The following table lists known caveats, grouped by severity, related to Cisco Collaboration Systems Release testing. It also
                        includes caveats from previous releases, which were not resolved at the time this document was written. For more information
                        about each defect, click the linked caveat number in the Identifier column.

For information about a defect not listed in the table, go to Bug Search Tool .

Identifier

Headline

Severity 2-3 Caveats

CSCvo12799

Call is not getting connected in Forking Re-INVITE scenario

CSCvj72294

Memory leak @ CCSIP_SPI_CONTR

CSCvp72978

VXML gateway crashed on 4th day Load run - ISR G2 Platform

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

| Note | For details about component versions, see Component Versions . |
|---|---|

| Component | Links |
|---|---|
| Call Control |
| Cisco Unified Communications Manager | Product Information Documentation |
| Cisco Unified Communications Manager IM and Presence Service | Product Information Documentation |
| Contact Center |
| Cisco Unified Contact Center Enterprise | Product Information Documentation |
| Cisco Packaged Contact Center Enterprise | Product Information Documentation |
| Cisco Unified Contact Center Express | Product Information Documentation |
| Cisco Unified Intelligence Center | Product Information Documentation |
| Cisco MediaSense (End-of-Sale: Oct 4, 2017) | Product Information Documentation |
| Cisco Finesse | Product Information Documentation |
| Cisco Unified Customer Voice Portal | Product Information Documentation |
| Cisco Virtualized Voice Browser | Documentation |
| Cisco Unified Intelligent Contact Management Enterprise | Product Information Documentation |
| Cisco Unified E-Mail Interaction Manager (EOS) | Product Information Documentation |
| Cisco Unified Web Interaction Manager (EOS) | Product Information Documentation |
| Conferencing |
| Cisco TelePresence Conductor | Product Information Documentation |
| Enterprise Edge |
| Cisco TelePresence Video Communication Server | Product Information Documentation |
| Cisco Expressway Series | Product Information Documentation |
| Cisco Unified Border Element | Product Information Documentation |
| Endpoints |
| Cisco DX Series | Product Information Documentation |
| Cisco TelePresence System EX Series (EOS) | Product Information Documentation |
| Cisco Unified IP Phone 6901 | Product Information Documentation |
| Cisco Unified IP Phone 6911, 6921, 6941, 6945, 6961 (EOS) | Product Information Documentation |
| Cisco IP Phone 7800 Series | Product Information Documentation |
| Cisco Unified IP Phone 7900 Series | Product Information Documentation |
| Cisco IP Phone 8800 Series | Product Information Documentation |
| Cisco Unified IP Phone 8900 Series (EOS) | Product Information Documentation |
| Cisco Unified IP Phone 9900 Series (EOS) | Product Information Documentation |
| Cisco Jabber for Mac | Product Information Documentation |
| Cisco Jabber for Windows | Product Information Documentation |
| Cisco Virtualization Experience Media Edition for Windows | Product Information Documentation |
| Cisco Virtualization Experience Media Edition for SUSE Linux | Product Information Documentation |
| Cisco Jabber Guest | Product Information Documentation |
| Communication Gateways |
| Cisco Unified SIP Proxy | Product Information Documentation |
| Cisco 2900 Series Integrated Services Routers | Product Information Documentation |
| Cisco 3900 Series Integrated Services Routers | Product Information Documentation |
| Cisco 4400 Series Integrated Services Routers | Product Information Documentation |

| Identifier | Headline |
|---|---|
| Severity 2-3 Caveats |
| CSCvo04890 | Multiple observations on PCCE when VM tools are out of date for CUIC post upgrade |

| Identifier | Headline |
|---|---|
| Severity 2-3 Caveats |
| CSCvo12799 | Call is not getting connected in Forking Re-INVITE scenario |
| CSCvj72294 | Memory leak @ CCSIP_SPI_CONTR |
| CSCvp72978 | VXML gateway crashed on 4th day Load run - ISR G2 Platform |