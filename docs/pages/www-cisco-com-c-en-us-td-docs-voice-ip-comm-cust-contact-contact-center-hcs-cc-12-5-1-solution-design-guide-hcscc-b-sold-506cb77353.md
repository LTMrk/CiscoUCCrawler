---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-hcs-cc-12-5-1-solution-design-guide-hcscc-b-sold-506cb77353
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/hcs-cc/12_5_1/Solution_Design_Guide/hcscc_b_soldg-for-hcs-cc-12_5/hcscc_b_soldg-for-hcs-cc-12_5_preface_00.html
retrieved_at: 2026-08-21T23:54:05.210811+00:00
---

Solution Design Guide for Cisco Hosted Collaboration Solution for Contact Center, Release 12.5

# Solution Design Guide for Cisco Hosted Collaboration Solution for Contact Center, Release 12.5

Updated: February 16, 2020

Chapter: Preface

## Chapter: Preface

# Preface

## Change History

This table lists the major changes made to this guide. The most recent changes appear at the top.

Changes

Section

Date

Added support for vMotion

Solution-Wide Support for vMotion

May, 2021

Increased configuration limit for active mobile agents with call-by-call connections per agent PG

Agent Limits

PG Agent Capacity with Mobile Agents

March, 2021

Added support to scale to 36000 Agents from 24000 Agents Reference Design

Scale Up to 36000 Agents

February, 2021

Initial Release of Document for 12.5(1)

February, 2020

Added Reference Design layouts and VM specifications on Cisco UCS C240 M5SX and Cisco Hyperflex HX220c M5SX TRC servers for
                                       the following deployment types:

2000 Agent Deployment

4000 Agent Deployment

12000 Agent Deployment

24000 Agent Deployment

Contact Center Enterprise Reference Designs

Contact Center Enterprise Solutions Overview

Design Considerations for Integrated Features

Design Considerations for Integrated Features

Added shared ACD Line support for both home and work phone on two shared ACD lines

Design Considerations for Integrated Features

Increased configuration limits for the following:

Outbound dialer maximum calls per second per dialer

Outbound dialer maximum ports per SIP dialer

Number of preview campaigns per system

Number of predictive Campaigns per system (Agent or VRU based)

Predictive Campaign Skill Groups per Peripheral

Outbound Campaign Limits

Removed information on Cisco MediaSense, Cisco Remote Expert, and Context Service which reached its end of maintenance support.

Added desktop chat search

Desktop Chat Server Settings

## About This Guide

This guide provides design considerations and guidelines for deploying Cisco Unified Contact Center Enterprise (Unified CCE)
                           solutions. The guide combines information for all the components that might be present in your solution. This guide assumes
                           that you are familiar with basic contact center terms and concepts. Successful deployment of Unified CCE solutions also requires
                           familiarity with the information presented in the Cisco Collaboration System
                                    				  Solution Reference Network Designs .

This guide focuses on the design process. Its goal is to present the necessary information to take your design from starting
                           concept to final submission. Details of installation, configuration, and administration of your contact center enterprise
                           solution are covered in other guides.

The first four chapters of the book give a broad perspective of the contact center enterprise solutions:

Packaged Contact Center Enterprise

Cisco Hosted
                                       						Collaboration Solution for Contact Center

Unified Contact Center Enterprise

For information about design considerations and guidelines specific to HCS for CC , see the remaining chapters.

## Audience

The first three chapters in this guide are for anyone who wants a broad overview of the contact center enterprise solutions.

The primary audience for the guide is people who design contact centers. The guide is also helpful for system administrators
                           who want a deeper understanding of how the components in a contact center enterprise solution work together.

## Related Documents

Consult these documents for details of these subjects that are not covered in this guide.

Compatibility Matrix for information on which versions of which products are supported for a contact center enterprise solution.

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html

https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-device-support-tables-list.html

https://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-contact-center/products-device-support-tables-list.html

Cisco Unified Contact Center Enterprise Features Guide for detailed information on the configuration and administration of integrated features in your solution.

http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html

Cisco Hosted Collaboration Solution for detailed information on Hosted Unified Communications and Data Center infrastructure
                                       on which the HCS for CC solution is built.

http://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-hcs/tsd-products-support-series-home.html

You can find the full documentation of each of the components in the contact center enterprise solutions at these sites:

Component

Link

Cisco Hosted
                                             						Collaboration Solution for Contact Center

https://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-contact-center/tsd-products-support-series-home.html

Cisco Finesse

http://www.cisco.com/c/en/us/support/customer-collaboration/finesse/tsd-products-support-series-home.html

Cisco Customer Collaboration Platform

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/tsd-products-support-series-home.html

Cisco Unified Customer Voice Portal

http://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html

Cisco Unified Intelligence Center

http://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/tsd-products-support-series-home.html

Cisco Virtualized Voice Browser

http://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/tsd-products-support-series-home.html

## Communications, Services, and Additional Information

To receive timely, relevant information from Cisco, sign up at Cisco Profile Manager .

To get the business impact you’re looking for with the technologies that matter, visit Cisco Services .

To submit a service request, visit Cisco Support .

To discover and browse secure, validated enterprise-class apps, products, solutions and services, visit Cisco Marketplace .

To obtain general networking, training, and certification titles, visit Cisco Press .

To find warranty information for a specific product or product family, access Cisco Warranty Finder .

### Cisco Bug Search Tool

Cisco Bug Search Tool (BST) is a web-based tool that acts as a gateway to the Cisco bug tracking system that maintains a comprehensive list of
                              defects and vulnerabilities in Cisco products and software. BST provides you with detailed defect information about your products
                              and software.

## Field Notice

Cisco publishes Field Notices to notify customers and partners about significant issues in Cisco products that typically require
                              an upgrade, workaround, or other user action. For more information, see Product Field Notice Summary at https://www.cisco.com/c/en/us/support/web/tsd-products-field-notice-summary.html .

You can create custom subscriptions for Cisco products, series, or software to receive email alerts or consume RSS feeds when
                              new announcements are released for the following notices:

Cisco Security Advisories

Field Notices

End-of-Sale or Support Announcements

Software Updates

Updates to Known Bugs

For more information on creating custom subscriptions, see My Notifications at https://cway.cisco.com/mynotifications .

## Documentation
                        	 Feedback

To provide comments about this document, send an email message to the following address: contactcenterproducts_docfeedback@cisco.com

We appreciate your
                           		comments.

## Conventions

This document uses
                           		the following conventions:

Convention

Description

boldface font

Boldface font is used to indicate commands, such as user entries, keys, buttons, folder names, and submenu names.

For example:

Choose Edit > Find .

Click Finish .

italic font

Italic
                                       					 font is used to indicate the following:

To
                                             						  introduce a new term. Example: A skill group is a collection of agents who share similar
                                             						  skills.

A
                                             						  syntax value that the user must replace. Example: IF ( condition, true-value,
                                                							 false-value )

A book title. Example: See the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide .

window font

Window
                                       					 font, such as Courier, is used for the following:

Text
                                             						  as it appears in code or that the window displays. Example: <html><title>Cisco Systems, Inc.
                                                							 </title></html>

< >

Angle
                                       					 brackets are used to indicate the following:

For
                                             						  arguments where the context does not allow italic, such as ASCII output.

A
                                             						  character string that the user enters but that does not appear on the window
                                             						  such as a password.

| Changes | Section | Date |
|---|---|---|
| Added a note for OVA when VVB fresh install is performed on a medium or small Open Virtual Appliance (OVA). | Cisco Virtualized Voice Browser Sizing | April, 2023 |
| Added support for vMotion | Solution-Wide Support for vMotion | May, 2021 |
| Increased configuration limit for active mobile agents with call-by-call connections per agent PG | Agent Limits PG Agent Capacity with Mobile Agents | March, 2021 |
| Added support to scale to 36000 Agents from 24000 Agents Reference Design | Scale Up to 36000 Agents | February, 2021 |
| Initial Release of Document for 12.5(1) | February, 2020 |
| Added Reference Design layouts and VM specifications on Cisco UCS C240 M5SX and Cisco Hyperflex HX220c M5SX TRC servers for
                                       the following deployment types: 2000 Agent Deployment 4000 Agent Deployment 12000 Agent Deployment 24000 Agent Deployment | Contact Center Enterprise Reference Designs |
| Added information on the new Cisco Webex Experience Management Feature feature. | Contact Center Enterprise Solutions Overview Design Considerations for Integrated Features |
| Added information on the new Customer Virtual Assistance Feature feature. | Design Considerations for Integrated Features |
| Added shared ACD Line support for both home and work phone on two shared ACD lines | Design Considerations for Integrated Features |
| Increased configuration limits for the following: Outbound dialer maximum calls per second per dialer Outbound dialer maximum ports per SIP dialer Number of preview campaigns per system Number of predictive Campaigns per system (Agent or VRU based) Predictive Campaign Skill Groups per Peripheral | Outbound Campaign Limits |
| Removed information on Cisco MediaSense, Cisco Remote Expert, and Context Service which reached its end of maintenance support. |  |
| Added desktop chat search | Desktop Chat Server Settings |

| Subject | Link |
|---|---|
| Compatibility Matrix for information on which versions of which products are supported for a contact center enterprise solution. | https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-device-support-tables-list.html https://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-contact-center/products-device-support-tables-list.html |
| Cisco Unified Contact Center Enterprise Features Guide for detailed information on the configuration and administration of integrated features in your solution. | http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html |
| Cisco Hosted Collaboration Solution for detailed information on Hosted Unified Communications and Data Center infrastructure
                                       on which the HCS for CC solution is built. | http://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-hcs/tsd-products-support-series-home.html |

| Component | Link |
|---|---|
| Cisco Hosted
                                             						Collaboration Solution for Contact Center | https://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-contact-center/tsd-products-support-series-home.html |
| Cisco Finesse | http://www.cisco.com/c/en/us/support/customer-collaboration/finesse/tsd-products-support-series-home.html |
| Cisco Customer Collaboration Platform | https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/tsd-products-support-series-home.html |
| Cisco Unified Customer Voice Portal | http://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html |
| Cisco Unified Intelligence Center | http://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/tsd-products-support-series-home.html |
| Cisco Virtualized Voice Browser | http://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/tsd-products-support-series-home.html |

| Convention | Description |
|---|---|
| boldface font | Boldface font is used to indicate commands, such as user entries, keys, buttons, folder names, and submenu names. For example: Choose Edit > Find . Click Finish . |
| italic font | Italic
                                       					 font is used to indicate the following: To
                                             						  introduce a new term. Example: A skill group is a collection of agents who share similar
                                             						  skills. A
                                             						  syntax value that the user must replace. Example: IF ( condition, true-value,
                                                							 false-value ) A book title. Example: See the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide . |
| window font | Window
                                       					 font, such as Courier, is used for the following: Text
                                             						  as it appears in code or that the window displays. Example: <html><title>Cisco Systems, Inc.
                                                							 </title></html> |
| < > | Angle
                                       					 brackets are used to indicate the following: For
                                             						  arguments where the context does not allow italic, such as ASCII output. A
                                             						  character string that the user enters but that does not appear on the window
                                             						  such as a password. |