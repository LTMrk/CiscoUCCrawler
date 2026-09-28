---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-15-0-1-design-guide-pcce-b-pcce-soluti-e2ced910e1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_15_0_1/design/guide/pcce_b_pcce-solution-design-guide-15-0/rcct_b_ucce_soldg-for-unified-cce-1261_preface_00.html
retrieved_at: 2026-08-21T12:11:39.384184+00:00
---

Solution Design Guide for Cisco Packaged Contact Center Enterprise, Release 15.0(1)

# Solution Design Guide for Cisco Packaged Contact Center Enterprise, Release 15.0(1)

Updated: July 4, 2026

Chapter: Preface

## Chapter: Preface

# Preface

## Change History

This table lists the major changes made to this guide. The most recent changes appear at the top.

Changes

Section

Date

Initial Release of Document for 15.0(1)

TLS secure connection between CCE components such as Router, Logger, Peripheral Gateway, Administration and Data Server, Administration
                                       Client, and Dialer.

Initial Release of Document for 15.0(1)

VM specifications values have been updated in all Reference Designs

Chapter: Unified CCE Reference Designs

April 2025

Extended Agent Events

Chapter:  Unified CCE Reference Designs

Topic: Scale up to 36000 Agents topic

Features removed and unsupported in the CCE 15.0(1) release have been removed from this guide.

See the Release notes for Cisco Contact Center Enterprise Solutions, Release 15.0(1) for the list of removed/unsupported features at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html

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

Unified Contact Center Enterprise

For information about design considerations and guidelines specific to Packaged CCE , see the remaining chapters.

## Audience

The first three chapters in this guide are for anyone who wants a broad overview of the contact center enterprise solutions.

The primary audience for the guide is people who design contact centers. The guide is also helpful for system administrators
                           who want a deeper understanding of how the components in a contact center enterprise solution work together.

## Related Documents

Consult these documents for details of these subjects that are not covered in this guide.

Compatibility Matrix for information on which versions of which products are supported for a contact center enterprise solution.

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html

https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-device-support-tables-list.html

Cisco Unified Contact Center Enterprise Features Guide for detailed information on the configuration and administration of integrated features in your solution.

http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html

Cisco Collaboration Systems Solution Reference Network Designs for detailed information on the Unified Communications infrastructure on which your solution is built.

http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-implementation-design-guides-list.html

Cisco Packaged Contact Center Enterprise Features Guide

https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide for details on  ICM-to-ICM configurations.

You can find the full documentation of each of the components in the contact center enterprise solutions at these sites:

Component

Link

Cisco Packaged Contact Center Enterprise

https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/tsd-products-support-series-home.html

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

To get the business results you’re looking for with the technologies that matter, visit Cisco Services .

To submit a service request, visit Cisco Support .

To discover and browse secure, validated enterprise-class apps, products, solutions and services, visit Cisco DevNet .

To obtain general networking, training, and certification titles, visit Cisco Press .

To find warranty information for a specific product or product family, access Cisco Warranty Finder .

### Cisco Bug Search Tool

Cisco Bug Search Tool (BST) is a web-based tool that acts as a gateway to the Cisco bug tracking system that maintains a comprehensive list of defects
                              and vulnerabilities in Cisco products and software. BST provides you with detailed defect information about your products
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
| Initial Release of Document for 15.0(1) |
| TLS secure connection between CCE components such as Router, Logger, Peripheral Gateway, Administration and Data Server, Administration
                                       Client, and Dialer. | Solution Security > Secure PII in Transit | March 2026 |
| Initial Release of Document for 15.0(1) |
| VM specifications values have been updated in all Reference Designs | Chapter: Unified CCE Reference Designs | April 2025 |
| Extended Agent Events | Chapter:  Unified CCE Reference Designs Topic: Scale up to 36000 Agents topic |
| Features removed and unsupported in the CCE 15.0(1) release have been removed from this guide. | See the Release notes for Cisco Contact Center Enterprise Solutions, Release 15.0(1) for the list of removed/unsupported features at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html |

| Subject | Link |
|---|---|
| Compatibility Matrix for information on which versions of which products are supported for a contact center enterprise solution. | https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-device-support-tables-list.html |
| Cisco Unified Contact Center Enterprise Features Guide for detailed information on the configuration and administration of integrated features in your solution. | http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html |
| Cisco Collaboration Systems Solution Reference Network Designs for detailed information on the Unified Communications infrastructure on which your solution is built. | http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-implementation-design-guides-list.html |
| Cisco Packaged Contact Center Enterprise Features Guide | https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html |
| Cisco Packaged Contact Center Enterprise Administration and Configuration Guide for details on  ICM-to-ICM configurations. |

| Component | Link |
|---|---|
| Cisco Packaged Contact Center Enterprise | https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/tsd-products-support-series-home.html |
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