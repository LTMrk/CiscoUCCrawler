---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-reference-g-58fe448957
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/reference/guide/ucce_b_acd-supplement-guide-for-avaya-12_6_2/ucce_m_preface1262.html
retrieved_at: 2026-08-16T19:45:41.013703+00:00
---

Cisco Unified ICM ACD Supplement for Avaya Communication Manager, Release 12.6(2)

# Cisco Unified ICM ACD Supplement for Avaya Communication Manager, Release 12.6(2)

Updated: April 28, 2023

Chapter: Preface

## Chapter: Preface

# Preface

## Change History

This table lists and links to changes made to this guide and gives the dates those changes were made. Earliest changes appear
                           in the bottom rows.

Initial Release of Document for Release 12.6(2)

April 2023

Added a new section for Network Take-Back and Transfer Support

Network Take-Back and Transfer Support

Added a new chapter that has details about migrating your existing Avaya PGs from the CVLAN interface to the TSAPI interface.

CVLAN to TSAPI Migration

Removed a reference to "Product Reference Guide for Cisco Unified ICM Hosted"

Related Documents

Removed "Table 3: Unified ICM Compatibility for Maximum Agent and BHCA"

Maximum Agent and BHCA

## About this
                        	 Guide

This document
                           		contains the specific information you need to maintain an Avaya Peripheral
                           		Gateway (PG) in a Unified Intelligent Contact Management (Unified ICM)
                           		environment. It is intended to be used as the Avaya‑specific companion to the
                           		Unified ICM software documentation set.

While the other
                           		Unified ICM documents cover general topics such as configuring an overall
                           		Unified ICM system and writing scripts to route contact center requests, this
                           		document provides specific information on configuring an Avaya PG and making
                           		any necessary adjustments to the Avaya ACD configuration.

## Audience

This document is
                           		intended for Unified ICM system managers. The reader understands the Unified 
                           		ICM functions as described in the following
                           		documents:

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide

Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise

The reader should
                           		also have specific knowledge about the Avaya and CMS systems.

## Related
                        	 Documents

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

## Communications, Services, and Additional Information

To receive timely, relevant information from Cisco, sign up at Cisco Profile Manager .

To get the business results you’re looking for with the technologies that matter, visit Cisco Services .

To submit a service request, visit Cisco Support .

To discover and browse secure, validated enterprise-class apps, products, solutions and services, visit Cisco DevNet .

To obtain general networking, training, and certification titles, visit Cisco Press .

To find warranty information for a specific product or product family, access Cisco Warranty Finder .

### Cisco Bug Search Tool

Cisco Bug Search Tool (BST) is a web-based tool that acts as a gateway to the Cisco bug tracking system that maintains a comprehensive list of
                              defects and vulnerabilities in Cisco products and software. BST provides you with detailed defect information about your products
                              and software.

## Conventions

This document uses
                           		the following conventions:

font

Boldface
                                       					 font is used to indicate commands, such as user entries, keys, buttons, and
                                       					 folder and submenu names.

For
                                       					 example:

Choose Edit > Find

Click Finish

font

To
                                                						  introduce a new term. Example: A skill group is a collection of agents who
                                                						  share similar skills.

A
                                                						  syntax value that the user must replace. Example: IF (condition,true-value,
                                                						  false-value)

A
                                                						  book title. Example: See the Cisco Unified Contact Center Enterprise Installation
                                                   							 and Upgrade Guide .

window
                                       					 font

Text as it appears in code or that the window displays.
                                                						  Example:

<html><title>Cisco Systems, Inc.
                                          						</title></html>

< >

Angle
                                       					 brackets are used to indicate the following:

For arguments where the context does not allow italic,
                                             						  such as ASCII output.

A character string that the user enters but that does not
                                             						  appear on the window such as a password.

| Change | See | Date |
|---|---|---|
| Initial Release of Document for Release 12.6(2) | April 2023 |
| Added a new section for Network Take-Back and Transfer Support | Network Take-Back and Transfer Support |
| Added a new chapter that has details about migrating your existing Avaya PGs from the CVLAN interface to the TSAPI interface. | CVLAN to TSAPI Migration |
| Removed a reference to "Product Reference Guide for Cisco Unified ICM Hosted" | Related Documents |
| Removed "Table 3: Unified ICM Compatibility for Maximum Agent and BHCA" | Maximum Agent and BHCA |

| Convention | Description |
|---|---|
| boldface font | Boldface
                                       					 font is used to indicate commands, such as user entries, keys, buttons, and
                                       					 folder and submenu names. For
                                       					 example: Choose Edit > Find Click Finish |
| italic font | Italic
                                       					 font is used to indicate the following: To
                                                						  introduce a new term. Example: A skill group is a collection of agents who
                                                						  share similar skills. A
                                                						  syntax value that the user must replace. Example: IF (condition,true-value,
                                                						  false-value) A
                                                						  book title. Example: See the Cisco Unified Contact Center Enterprise Installation
                                                   							 and Upgrade Guide . |
| window
                                       					 font | Window
                                       					 font, such as Courier, is used for the following: Text as it appears in code or that the window displays.
                                                						  Example: <html><title>Cisco Systems, Inc.
                                          						</title></html> |
| < > | Angle
                                       					 brackets are used to indicate the following: For arguments where the context does not allow italic,
                                             						  such as ASCII output. A character string that the user enters but that does not
                                             						  appear on the window such as a password. |