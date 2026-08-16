---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-v12-7-1-vtgs-b-csr-contact-center-rns-1271-html-56e1e7326c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/V12_7_1/vtgs_b_csr-contact-center-rns-1271.html
retrieved_at: 2026-08-16T18:26:56.299276+00:00
---

Cisco Collaboration Systems Release 12.7: Release Notes for Contact Center

# Cisco Collaboration Systems Release 12.7: Release Notes for Contact Center

### Download Options

Updated: January 30, 2020

First Published: August 6, 2020

Last Updated: March 19, 2021

# Contact Center Releases

This document covers Cisco Collaboration Systems Release 12.7 systems testing for Contact Center. Although a variety of Contact
                  Center versions are supported with this systems release, the following Contact Center versions are recommended:

Cisco Unified Contact Center Express 12.5(1)SU1

Cisco Unified Contact Center Enterprise 12.6(1)

Cisco Packaged Contact Center Enterprise 12.6(1)

For a detailed listing of Contact Center applications that are supported with this systems release, including Minimum and Recommended versions, see the Compatibility Matrix for Cisco Collaboration Systems Release .

## Introduction to Cisco Collaboration Systems Release for Contact Center

As part of our standard methodology for each Cisco Collaboration Systems Release, we:

Perform system-wide testing of Cisco Collaboration products to supplement the product-level testing performed on each collaboration
                        product.

Recommend compatible software releases that were verified by the testing teams. The recommendations are not exclusive and
                        are in addition to interoperability recommendations for each of the individual applications or products.

For software compatibility data, see the Cisco Collaboration Systems Release Compatibility Matrix .

Not all Collaboration System product release versions may be available at the same time. For latest product version availability,
                                 see individual product support pages at, Support and Downloads .

This document focuses on the Contact Center components tested as part of the Cisco Collaboration Systems Release. For information
                  focused on Collaboration components that were tested as part of Cisco Collaboration Systems Release, see: Release Notes for Cisco Collaboration Systems Release at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-system/products-release-notes-list.html .

This document provides release notes details based on the system-wide testing which includes the following types of components:

Call control components, such as Cisco Unified Communications Manager (Unified CM), and Cisco Unified Communications Manager
                        IM and Presence Service.

Contact center components, such as Cisco Unified Contact Center Enterprise (Unified CCE), Cisco Packaged Contact Center Enterprise
                        (Packaged CCE), Cisco Unified Contact Center Express (Unified CCX), Cisco Unified Intelligence Center (Unified Intelligence
                        Center), Cisco Finesse, and Cisco Unified Customer Voice Portal (Unified CVP).

Enterprise Edge components such as Cisco Unified Border Element (CUBE), and Cisco Expressway Series.

Devices (Endpoints), such as Cisco DX Series (DX Series), Cisco IP Phone 7800 Series, Cisco IP Phone 8800 Series, and Cisco
                        Jabber for Windows (Jabber for Windows).

Communications gateway components such as Cisco Integrated Services Routers (ISR).

## Tested Functionality

System-wide testing was done for features and upgrade paths.

### Feature Testing

The following Contact Center features were tested:

#### Packaged Contact Center Enteprise

Customer Virtual Assistant (CVA) —This feature enables the IVR Platform to integrate with cloud-based speech services (currently validated with Google Dialog
                              flow).  The feature supports human-like interactions that let customers resolve issues quickly and more efficiently within
                              the IVR, thereby reducing the number of calls that are directed towards actual agents. Solution validation included the intent
                              fulfilment done at both the Cloud Provider (Google) and  the On-prem side (CVVB).

Hybrid Features :

Hybrid Analyzer —Hybrid Analyzer lets On-Premise solutions (Enterprise and Express) leverage CJP Business Metrics reporting (Analyzer) capabilities
                                    to provide Business Insights to customers. These Insights provide the information to make better decisions. Today, we provide
                                    operational metrics only to our on-prem customers and we can use the barrage of data that customers have to provide Business
                                    Insights to our customers.

Use Case Validated —Abandon contacts. For basic and supplementary call flows in Packaged CCE 2K deployments for voice-only call flows.

Voicea —Contact Center integration with Voicea reduces the agent workload and saves costs for the contact center. This feature enhances
                                    the agent experience by providing the agent with a live transcript of the call so that the agent can recap on what the customer
                                    said and so that the agent can capture notes in real time.This functionality helps the agent to improve the accuracy of the
                                    call "wrap-up" notes and reduces the time needed for call wrap-up.

Use case validated: —Validated the transcript for a basic call between agent and customer using the transcript gadget in Finesse desktop.

Webex Experience Managment (WXM) aka CloudCherry —This feature lets Packaged CCE customers use WXM (CloudCherry) for presenting surveys to users. This feature also lets customers
                                    access analytics on the survey responses so that they can understand the customer experience trend.

Use Case Validated —Basic call between agent and customer, post hanging up the call, the customer is transferred so that they can provide the
                                    survey inputs. Due to lab limitations, validation is done up when the refer transfer is made successfully to the WMX media
                                    server.

#### Unified Contact Center Express

Hybrid Analyzer —Hybrid Analyzer enables Premise solutions (Enterprise and Express) to leverage CJP Business Metrics reporting (Analyzer)
                              capabilities to provide Business Insights to our customers. These Insights provide necessary wisdom to take to better decisions/course
                              corrections. Today, we provide operational metrics only to our on-prem customers and we can use the barrage of data that customers
                              have to provide Business Insights to our customers.

Use Case Validated —Abandon contacts. For basic and supplementary call flows in Unified CCX deployment for voice and non-voice (chat) call flow:

sRTP: Unified CCX supports End to End secure call flow.

### Upgrade Paths

System-wide testing included verifying upgrade paths, including a single-stage upgrade to Cisco Collaboration Systems Release
                        12.7 from releases such as 12.0, 12.5 or 12.6.

For a list of versions that are compatible with this Cisco Collaboration Systems Release, see the Cisco Collaboration Systems Release Compatibility Matrix .

## New and Changed Features

For details about what is new for Cisco Collaboration Systems Release 12.5, 12.6, and 12.7 see the Solution Overview .

For details about new and changed contact center product features, access individual product release notes from Product Documentation .

## System Requirements

This section provides information about system requirements for this Cisco Collaboration Systems Release.

### End-of-Sale Components

#### Product Components

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

Cisco Unified Workforce Optimization, End of Life and End of Sale Notices

The EOS date is the last date to order the product through Cisco point-of-sale mechanisms. The product is no longer for sale.
                        Another process, the end-of-life (EOL) cycle, guides the final business operations associated with the product.

The EOL process consists of a series of technical and business milestones and activities that, when completed, make a product
                        obsolete. After a product becomes obsolete, it is not sold, manufactured, improved, repaired, maintained, or supported.

For information about recommended replacements and a comprehensive list of announcements, see Products & Services End-of-Sale and End-of-Life Products .

Go to End-of-Life Policy for more information about the EOL policy.

#### Software Versions

For support information for specific product components, and which software versions are End of Sale for those components,
                        refer to the below links:

Cisco Unified Communications Manager, End of Life and End of Sale Notices

Cisco Unified Communications Manager IM and Presence Service, End of Life and End of Sale Notices

Cisco Expressway, End of Life and End of Sale Notices

Cisco Unified Border Element, End of Life and End of Sale Notices

Cisco Unified Contact Center Enterprise or Packaged Contact Center Enterprise, End of Life and End of Sale Notices

Cisco Finesse, End of Life and End of Sale Notices

Cisco Social Miner, End of Life and End of Sale Notices

Cisco Unified IP Interactive Voice Response, End of Life and End of Sale Notices

Cisco Unified Customer Voice Portal, End of Life and End of Sale Notices

Cisco Unified Intelligent Contact Management Enterprise, End of Life and End of Sale Notices

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

### Collaboration Systems Documentation

For systems documentation that covers Cisco Collaboration Systems Releases 12.5 through 12.7, go to https://www.cisco.com/c/en/us/support/unified-communications/collaboration-systems-release-12-5/model.html

### Product Documentation

For documentation that covers the product components that make up the Contact Center portion of a Cisco Collaboration Systems
                        Release, refer to the below table. For each product component, the table provides links to:

Product Overview pages, from which you can access general product information such as product data sheets and additional marketing material.

Documentation pages, from which you can access technical documentation such as release notes, design, installation, configuration, and
                              troubleshooting guides.

For details about which product versions are recommended for this Collaboration Systems Release, see Cisco Collaboration Systems
                                    Release Compatibility Matrix at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/unified/communications/system/Compatibility/CSR-Compatibility-Matrix.html .

Component

Links

Call Control

Cisco Unified Communications Manager

Product Overview

Documentation

Cisco Unified Communications Manager IM & Presence Service

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

Enterprise Edge

Cisco Expressway Series

Product Overview

Documentation

Cisco Unified Border Element

Product Overview

Documentation

Endpoints

Cisco Headset 500 Series

Product Overview

Documentation

Cisco Headset 700 Series

Product Overview

Documentation

Cisco Webex Board

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

Communication Gateways

Cisco IOS 15 M&T

Documentation

Cisco IOS XE 16

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

### Open Caveats

#### Open Caveats for Cisco Collaboration Systems Release for Contact Center 12.7

The following table contains severity level 1-3 open caveats for Cisco Collaboration Systems for Contact Center, Release 12.7.

Caveat

Headline

CSCvs94916

Kernel Panic seen on UCCX Box after graceful reboot

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
| Call Control |
| Cisco Unified Communications Manager | Product Overview Documentation |
| Cisco Unified Communications Manager IM & Presence Service | Product Overview Documentation |
| Contact Center |
| Cisco Packaged Contact Center Enterprise | Product Information Documentation |
| Cisco Unified Contact Center Express | Product Information Documentation |
| Cisco Unified Contact Center Enterprise | Product Information Documentation |
| Cisco Finesse | Product Information Documentation |
| Cisco Unified Intelligence Center | Product Information Documentation |
| Cisco Virtualized Voice Browser | Documentation |
| Cisco Unified Intelligent Contact Management Enterprise | Product Information Documentation |
| Cisco Unified Customer Voice Portal | Product Information Documentation |
| Enterprise Edge |
| Cisco Expressway Series | Product Overview Documentation |
| Cisco Unified Border Element | Product Overview Documentation |
| Endpoints |
| Cisco Headset 500 Series | Product Overview Documentation |
| Cisco Headset 700 Series | Product Overview Documentation |
| Cisco Webex Board | Product Overview Documentation |
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
| Communication Gateways |
| Cisco IOS 15 M&T | Documentation |
| Cisco IOS XE 16 | Documentation |
| Cisco VG Series Gateways | Product Overview Documentation |
| Cisco ASR 1000 Routers | Product Overview Documentation |
| Cisco 2900 Series Integrated Services Routers (EOS) | Product Overview Documentation |
| Cisco 3900 Series Integrated Services Routers | Product Overview Documentation |
| Cisco 4000 Series Integrated Services Routers | Product Overview Documentation |

| Caveat | Headline |
|---|---|
| CSCvs94916 | Kernel Panic seen on UCCX Box after graceful reboot |