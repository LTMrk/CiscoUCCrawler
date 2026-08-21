---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-installation-guide-pcce-b-cisco-4ae8fca8ea
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/installation/guide/pcce_b_cisco-pcce-installationandupgrade-guide-12_5/pcce_b_cisco-pcce-installationandupgrade-guide-12_5_preface_00.html
retrieved_at: 2026-08-21T16:38:39.546340+00:00
---

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.5(1) and 12.5(2)

# Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.5(1) and 12.5(2)

Updated: February 4, 2020

Chapter: Preface

## Chapter: Preface

# Preface

## Change History

Change

See

Date

MR Release 12.5(2)

12.5(2) MR related updates in applicable sections

July 2022

Dual Platform

Dual Platform support updates in applicable sections

12.5.2

Added the release number-12.5(2) to title

July 2022

Initial Release of Document for Release 12.5(1)

OpenJDK updates

Java Upgrades

Upgrade Tomcat Utility

Added a new section

March 2021

Edge Chromium (Microsoft Edge) updates

Install Microsoft Windows Server

Added Technology Refresh upgrade details

Upgrade Overview

July, 2020

Technology Refresh Upgrade Process

Added Multistage Upgrade Process for Common Ground Upgrade

Version Upgrade

February, 2020

Updated Tomcat version

Upgrade Tomcat Utility

Upgrade Tomcat

Updated the topics to include certificate information

Upgrade Side A

Upgrade Side B

Postupgrade Tasks

Update the Java Runtime Environment (Optional)

Added a new section

Java Requirements

## About This Guide

This guide
                           		explains how to install, configure, and upgrade Cisco Packaged Contact Center
                           		Enterprise (Packaged CCE).

Packaged CCE is a solution deployment for delivering Cisco Unified Contact Center Enterprise in a virtualized environment.
                           Packaged CCE requires strict adherence to capacity limits that are detailed in the Solution Design Guide for Cisco Packaged Contact Center Enterprise , available at https://www.cisco.com/en/US/products/ps12586/prod_technical_reference_list.html . It is mandatory to follow all rules and requirements stated in the Design Guide.

This document does not discuss the Packaged CCE Lab Only deployment. For information about that deployment, see the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

## Audience

This guide
                           		is prepared for partners and service providers who will be implementing
                           		Packaged CCE, who are familiar with Cisco contact center applications, and who
                           		are experienced regarding the deployment and management of virtual machines
                           		using VMware technology.

## Related
                        	 Documents

Cisco
                                       					 Packaged Contact Center Enterprise

Cisco
                                       					 Unified Contact Center Enterprise

Cisco
                                       					 Unified Communications Manager

Cisco
                                       					 Unified Intelligence Center

Cisco
                                       					 Finesse

Cisco Unified Customer Voice Portal

Cisco Enterprise Chat and Email

https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/tsd-products-support-series-home.html

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

## Field Alerts and Field Notices

Note that Cisco products may be modified or key processes may be determined important. These are announced through use of
                           the Cisco Field Alert and Cisco Field Notice mechanisms. You can register to receive Field Alerts and Field Notices through
                           the Product Alert Tool on Cisco.com. This tool enables you to create a profile to receive announcements by selecting all products
                           of interest. Log into www.cisco.com; then access the tool at:

https://www.cisco.com/cisco/support/notifications.html

## Documentation
                        	 Feedback

To provide comments
                           		about this document, send an email message to the following address:

contactcenterproducts_docfeedback@cisco.com

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

| Change | See | Date |
|---|---|---|
| MR Release 12.5(2) | 12.5(2) MR related updates in applicable sections | July 2022 |
| Dual Platform | Dual Platform support updates in applicable sections | July 2022 |
| 12.5.2 | Added the release number-12.5(2) to title | July 2022 |
| Initial Release of Document for Release 12.5(1) |
| OpenJDK updates | Java Upgrades | Mar, 2021 |
| Upgrade Tomcat Utility |
| Added a new section | Java Requirements | March 2021 |
| Edge Chromium (Microsoft Edge) updates | Install Microsoft Windows Server | Dec, 2020 |
| Added Technology Refresh upgrade details | Upgrade Overview | July, 2020 |
| Technology Refresh Upgrade Process |
| Added Multistage Upgrade Process for Common Ground Upgrade | Version Upgrade | February, 2020 |
| Updated Tomcat version | Upgrade Tomcat Utility Upgrade Tomcat |
| Updated the topics to include certificate information | Upgrade Side A Upgrade Side B Postupgrade Tasks Update the Java Runtime Environment (Optional) |
| Added a new section | Java Requirements |

| Subject | Link |
|---|---|
| Cisco
                                       					 Packaged Contact Center Enterprise | https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/tsd-products-support-series-home.html |
| Cisco
                                       					 Unified Contact Center Enterprise | https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/tsd-products-support-series-home.html |
| Cisco
                                       					 Unified Communications Manager | https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html |
| Cisco
                                       					 Unified Intelligence Center | https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/tsd-products-support-series-home.html |
| Cisco
                                       					 Finesse | https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/tsd-products-support-series-home.html |
| Cisco Unified Customer Voice Portal | https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html |
| Cisco Enterprise Chat and Email | https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/tsd-products-support-series-home.html |

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