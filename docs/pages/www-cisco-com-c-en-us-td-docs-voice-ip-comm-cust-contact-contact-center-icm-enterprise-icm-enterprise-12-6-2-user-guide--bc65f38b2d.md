---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-user-guide--bc65f38b2d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/user/guide/ucce_b_scripting-and-media-routing-guide_1262/ucce_b_scripting-and-media-routing-guide_preface_00.html
retrieved_at: 2026-08-16T20:31:26.079295+00:00
---

Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(2)

# Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(2)

Updated: November 21, 2022

Chapter: Preface

## Chapter: Preface

# Preface

## Change History

This table lists changes made to this guide. Most recent changes appear at the top.

See

Date

Initial Release of Document for Release 12.6(2)

Custom SQL Server Port

Chapter: Contact Categorization

Topic: Database Lookup Authentication

Doc update: CallRouter Registry of custom SQL server port.

Added new sections for the digital channel integration using Webex Connect

Determination of Call Type for a Digital Routing Task

Digital Routing using Webex Connect

Example Digital Channel Interactions Using Webex Connect

April 2023

## About This
                        	 Guide

This manual describes how to use the Script Editor tool for Cisco
                              		  Unified Intelligent Contact Management (Unified ICM) and Cisco Unified Contact
                              		  Center Enterprise (Unified CCE) to create and maintain routing and
                              		  administrative scripts.

## Audience

This document is intended for system managers. A system manager must
                              		  have a general understanding of contact center operations and management, and
                              		  specific information about the contact centers and carrier networks connected
                              		  to a Unified ICM/Unified CCE system.

## Related Documents

Documentation for Cisco Unified Intelligent Contact Management/Cisco Unified Contact Center Enterprise, as well as related
                           documentation, is accessible from Cisco.com at: https://www.cisco.com/cisco/web/psa/default.html .

Related documentation includes the documentation sets for Cisco Unified Contact Center
                           Management Portal, Cisco Unified Customer Voice Portal (Unified CVP), Cisco
                           Unified IP IVR, and Cisco Unified Intelligence Center. The following list provides for information:

For documentation for these Cisco Unified Contact Center Products, go to https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/tsd-products-support-series-home.html

For troubleshooting tips for the Cisco Unified Contact Center
                                 products, go to https://techzone.cisco.com/t5/Unified-Contact-Center/ct-p/ucc_ucce .

You can access documentation for Cisco Unified Communications Manager from: https://www.cisco.com/c/en_in/products/unified-communications/unified-communications-manager-callmanager/index.html

You can access technical Support documentation and tools from: https://www.cisco.com/en/US/support/index.html .

You can access the Product Alert tool from (login required): https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html .

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

| Change | See | Date |
|---|---|---|
| Initial Release of Document for Release 12.6(2) |  |
| Custom SQL Server Port | Chapter: Contact Categorization Topic: Database Lookup Authentication Doc update: CallRouter Registry of custom SQL server port. | December 2025 |
| Added new sections for the digital channel integration using Webex Connect | Determination of Call Type for a Digital Routing Task Digital Routing using Webex Connect Example Digital Channel Interactions Using Webex Connect | April 2023 |

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