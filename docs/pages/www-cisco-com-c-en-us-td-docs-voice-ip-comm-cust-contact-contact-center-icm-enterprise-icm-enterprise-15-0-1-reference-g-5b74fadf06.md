---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-reference-g-5b74fadf06
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/reference/guide/ucce-b-database-schema-handbook-for-cisco-unified-icm-contact-center-enterprise-release-1501/ucce-m-preface-1501.html
retrieved_at: 2026-08-16T19:43:48.684337+00:00
---

Database Schema Handbook for Cisco Unified Contact Center Enterprise, Release 15.0(1)

# Database Schema Handbook for Cisco Unified Contact Center Enterprise, Release 15.0(1)

Updated: November 28, 2025

Chapter: Preface

## Chapter: Preface

# Preface

## Change History

This table lists changes made to this guide. Most recent changes appear at the top.

Date

Replaced CUSP with CCCSP

Initial Release of Document for Release 15.0(1)

April 2025

Renamed SlrEnabled to ReservationType

Chapter: All Tables

Topic: Smart_License_Server

Added New Field DigitalChannelEnabled

Chapter: All Tables

Topic: Person

Added new RouterErrorCodes=704, new sub-error codes are also added.

Chapter: Field Value

Topic: Router Error Codes

Extended Agent Event Details

Chapter: All Tables

Topic: Agent_Event_Detail

Global Configuration

Chapter: All Tables

Topic: Global_Configuration

## About This
                        	 Guide

The Database Schema Handbook for Cisco Unified Contact Center Enterprise describes the database schema used by Unified Contact Center Enterprise
                              		  (Unified CCE), including the types of data stored in the database and the
                              		  relationships among those data. This guide documents each table, major
                              		  categories of tables, coded values used, and the dependencies and constraints.

## Audience

This manual is intended for Unified ICM and Unified CCE software
                              		  system managers and supervisors. Understanding the database schema helps you to
                              		  create your own monitoring screens and reports. It also helps you to understand
                              		  how the Unified ICM and Unified CCE software works.

You can navigate the PDF file using the Contents, the Index, and the
                              		  links.

## Related
                        	 Documents

Documentation for contact center enterprise solutions is accessible from Cisco.com at: https://www.cisco.com/c/en/us/support/contact-center/category.html . Click Voice and Unified Communications , then click Cisco Unified Contact Center Products or Cisco Unified Voice Self-Service Products , then click the product or option you want.

For the
                                    				Unified CCE Documentation guide, go to http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-documentation-roadmaps-list.html .

Related
                                    				documentation includes the documentation sets for Cisco Unified Contact Center
                                    				Management Portal (Unified CCMP), Cisco Unified Customer Voice Portal (Unified
                                    				CVP), and Cisco Unified IP IVR.

Documentation for Cisco Unified Communications Manager (Unified CM) is accessible from https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-documentation-roadmaps-list.html .

Technical
                                    				Support documentation and tools are accessible from http://www.cisco.com/en/US/support/index.html .

For information on the Cisco software support methodology, see Software Release and Support Methodology: Unified CCE available at (sign-in required) http://www.cisco.com/c/en/us/products/customer-collaboration/unified-contact-center-enterprise/bulletin-listing.html .

For a detailed list of language localizations, see the Cisco Unified Contact Center Product and System Localization Matrix available at the bottom of http://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligent-contact-management-enterprise/products-technical-reference-list.html .

## Communications, Services, and Additional Information

To receive timely, relevant information from Cisco, sign up at Cisco Profile Manager .

To get the business results you’re looking for with the technologies that matter, visit Cisco Services .

To submit a service request, visit Cisco Support .

To discover and browse secure, validated enterprise-class apps, products, solutions and services, visit Cisco Marketplace .

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

| Change | See | Date |
|---|---|---|
| Replaced CUSP with CCCSP | Throughout the document | November 2025 |
| Initial Release of Document for Release 15.0(1) | April 2025 |
| Renamed SlrEnabled to ReservationType | Chapter: All Tables Topic: Smart_License_Server |
| Added New Field DigitalChannelEnabled | Chapter: All Tables Topic: Person |
| Added new RouterErrorCodes=704, new sub-error codes are also added. | Chapter: Field Value Topic: Router Error Codes |
| Extended Agent Event Details | Chapter: All Tables Topic: Agent_Event_Detail |
| Global Configuration | Chapter: All Tables Topic: Global_Configuration |

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