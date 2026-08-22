---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-hcs-cc-12-5-1-install-upgrade-guide-hcs-cc-b-ins-926a2532dc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/hcs-cc/12_5_1/Install_Upgrade_Guide/hcs-cc_b_installing-and-upgrading-guide_12_5/hcs-cc_b_installing-and-upgrading-guide-for_preface_00.html
retrieved_at: 2026-08-22T00:12:05.849430+00:00
---

Installing and Upgrading Guide for Cisco Hosted Collaboration Solution for Contact Center, Release 12.5(1) and 12.5(2)

# Installing and Upgrading Guide for Cisco Hosted Collaboration Solution for Contact Center, Release 12.5(1) and 12.5(2)

Updated: July 26, 2022

Chapter: Preface

## Chapter: Preface

# Preface

## Change History

Change

See

Date

12.5(2) MR changes

MR related changes in applicable sections

July 2022

12.5.2

Added the release number- 12.5(2) to title

July 2022

Dual Platform

Dual Platform support updates in applicable sections

July 2022

CCE Orchestration

August 2020

Initial Release of the Document for Release 12.5(1)

Added a new section

March 2021

Removed prerequisite and modified note in the Section, Before you begin

Modified features list

Install Microsoft SQL Server

February 2020

Added new procedure

Verification of the Downloaded ISO

Updated the procedure

Disable Port Blocking

Added certificate details

Upgrading the Unified Component

## About this Guide

This document describes how to install the core and shared components, and software for a new Cisco HCS for Contact Center
                           solution, or to upgrade an existing Cisco HCS for Contact Center solution.

## Audience

This guide is
                           		intended for users who install and upgrade Cisco HCS for Contact Center
                           		solution.

This guide assumes
                           		that you are already familiar with Cisco Contact Center products. You must
                           		acquire the necessary knowledge and experience regarding deployment and
                           		management of virtual machines before you deploy components on VMware virtual
                           		machines. Therefore, you must have a sound knowledge of the VMware
                           		infrastructure.

Cisco HCS for
                           		Contact Center is a subset of Core HCS, this document assumes that the HCS
                           		infrastructure is ready to set up the contact center. Therefore, components
                           		such as UCDM, CUBE Enterprise, and PCA must be installed as part of HCS setup.

## Related Docs

Design Considerations and guidelines for deploying a Cisco HCS for Contact Center solution including various components and
                           subsystems. See, https://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-contact-center/products-implementation-design-guides-list.html

Post-installation procedure for Cisco HCS for Contact Center, See https://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-contact-center/products-installation-guides-list.html

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
| 12.5(2) MR changes | MR related changes in applicable sections | July 2022 |
| 12.5.2 | Added the release number- 12.5(2) to title | July 2022 |
| Dual Platform | Dual Platform support updates in applicable sections | July 2022 |
| CCE Orchestration | CCE Orchestration | August 2020 |
| Initial Release of the Document for Release 12.5(1) |
| Added a new section | Java Requirements | March 2021 |
| Removed prerequisite and modified note in the Section, Before you begin Modified features list | Install Microsoft SQL Server | February 2020 |
| Added new procedure | Verification of the Downloaded ISO |
| Updated the procedure | Disable Port Blocking |
| Added certificate details | Upgrading the Unified Component |

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