---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-configurati-1c0bace626
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/configuration/guide/ucce_b_serviceability-guide-for-cisco-unified12_5/ucce_b_serviceability-guide-for-cisco-unified12_5_preface_00.html
retrieved_at: 2026-08-16T14:49:25.073863+00:00
---

Serviceability Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1) and 12.5(2)

# Serviceability Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1) and 12.5(2)

Updated: July 26, 2022

Chapter: Preface

## Chapter: Preface

# Preface

## Change History

This table lists the changes made to this guide. The most recent changes appear at the top.

Date

Document updated for MR Release 12.5(2)

MR related changes in applicable sections.

July, 2022

Added Release -12.5(2) to the title

12.5(2) MR  (SSH for existing commands in System CLI to Gateway)

Import File Syntax

Device, Protocol and Command Mapping Table

Dual Platform (references to any version of windows were removed and made generic)

Dual platform support updates in applicable sections

Initial Release of Document for Release 12.5(1)

Initial Release

February, 2020

## About This Guide

This document contains system diagrams, staging steps and sample test cases for supported models
                              				of Unified
                                 					ICM/CCE .

Dedicated Forest/Domain Model

Chilc Domain Model

Hosted Network Applications Manager (NAM) / Customer ICM (CICM) Model

## Audience

Individuals
                              		utilizing this document must have knowledge and experience with the following
                              		tools/software/hardware to stage the system software as described in this
                              		document:

Cisco Unified
                                    			 ICM Scripting and Configuration Tools

Third-party
                                    			 software (if installed)

Microsoft
                                    			 Windows Server
                                    			 and Windows Active Directory administration

Microsoft SQL
                                    			 Server administration

## Related
                        	 Documents

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
| Document updated for MR Release 12.5(2) | MR related changes in applicable sections. | July, 2022 |
| Added Release -12.5(2) to the title | Title |
| 12.5(2) MR  (SSH for existing commands in System CLI to Gateway) | Import File Syntax Device, Protocol and Command Mapping Table |
| Dual Platform (references to any version of windows were removed and made generic) | Dual platform support updates in applicable sections |
| Initial Release of Document for Release 12.5(1) |
| Initial Release |  | February, 2020 |

| Note | This document is for individuals responsible
                                       				for staging deployments of Cisco contact centers. Individuals must be trained on the
                                       				use and functions of Unified ICM/CCE & Hosted as well as Microsoft Windows
                                       				Server, Active Directory (AD), and DNS. This document does not provide detailed
                                       				Cisco Unified Intelligent Contact Management Enterprise (Unified ICM), Hosted
                                       				NAM/CICM, or Microsoft Windows Server specific information. You can find this
                                       				information elsewhere in specific documentation from Cisco or Microsoft. |
|---|---|

| Document or Resource | Link |
|---|---|
| Cisco Unified Communications Manager | https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-express/tsd-products-support-series-home.html |

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