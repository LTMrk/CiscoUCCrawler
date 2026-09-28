---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-installatio-2d874cd9e2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/installation/guide/ucce_b_12_5_Install_upgrade_guide_ucce/ucce_b_cisco-unified-contact-center-enterprise12_5_preface_00.html
retrieved_at: 2026-08-16T19:52:34.372593+00:00
---

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.5(1) and 12.5(2)

# Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.5(1) and 12.5(2)

Updated: February 3, 2020

Chapter: Preface

## Chapter: Preface

# Preface

## Change History

This table lists changes made to this guide. Most recent changes appear at the top:

See

Date

Added the topic Install Microsoft Windows 11 for Administration Client

Preinstallation > Preinstallation Tasks > Set Up Third-Party Software

October, 2023

Removed a Note.

Initial Configuration > Initial Configuration Tasks > Configure Permissions in the Local Machine > Configure Registry Permissions

Added a Note.

Technology Refresh Upgrade > Technology Refresh Upgrade Tasks > Upgrade Unified CCE Administration Client

Document updated for MR Release 12.5(2)

July, 2022

12.5.2

Added the release number-12.5(2) to title

Dual Platform

Dual platform support updates in applicable sections

Initial Release of Document for Release 12.5(1)

CCE Orchestration

OpenJDK updates

Java Upgrades

Upgrade Tomcat Utility

Certificates for Unified Contact Center Enterprise Web Administration

Change Java Truststore Password

Added a new section

March, 2021

Edge Chromium (Microsoft Edge) updates

Install Microsoft Windows Server

Set Up CA Certificate for Chrome and Edge Chromium (Microsoft Edge) Browsers

Accept Security Certificates

Verification of the Downloaded ISO

CCEDataProtectTool updates

Bring Upgraded Side A into Service

Updated the Common Groung Upgrade Workflow for 2000 Agents Deployment

Multistage Upgrade Workflow for 2000 Agents Deployment

Updated Tomcat version

Upgrade Tomcat Utility

Upgrade Tomcat

Added a new topic for certificates

Certificates for CCE Web Administration

Added certificate information

Configure Folder Permissions

Common Ground Upgrade Task Flow

Common Upgrade Tasks

Added a new section for Cloud Connect Installation

Install Cloud Connect

## About This Guide

This guide describes how to install the components and software for a
                              		new Unified CCE system, or to upgrade an existing Unified CCE system.

## Audience

This guide is intended for users who install and upgrade Unified CCE
                              		contact centers.

The procedures assume that the system has been
                              		thoroughly designed and staged in preparation for the installation or upgrade.

## Related Documents

Design
                                          					 considerations and guidelines for deploying a Unified CCE solution, including
                                          					 its various components and subsystems.

Design Guide

System
                                          					 diagrams, staging steps and sample test cases for supported models of Unified
                                          					 CCE.

Staging Guide

Pre-installation requirements and issues to address when you
                                          					 prepare for a Unified CCE installation.

Preinstallation and Planning

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
| Added the topic Install Microsoft Windows 11 for Administration Client | Preinstallation > Preinstallation Tasks > Set Up Third-Party Software | October, 2023 |
| Removed a Note. | Initial Configuration > Initial Configuration Tasks > Configure Permissions in the Local Machine > Configure Registry Permissions |
| Added a Note. | Technology Refresh Upgrade > Technology Refresh Upgrade Tasks > Upgrade Unified CCE Administration Client |
| Document updated for MR Release 12.5(2) | July, 2022 |
| 12.5.2 | Added the release number-12.5(2) to title |
| Dual Platform | Dual platform support updates in applicable sections |
| Initial Release of Document for Release 12.5(1) |
| CCE Orchestration | CCE Orchestration | May, 2021 |
| OpenJDK updates | Java Upgrades | Mar, 2021 |
| Upgrade Tomcat Utility |
| Certificates for Unified Contact Center Enterprise Web Administration |
| Change Java Truststore Password |
| Added a new section | Java Requirements | March, 2021 |
| Edge Chromium (Microsoft Edge) updates | Install Microsoft Windows Server | December, 2020 |
| Set Up CA Certificate for Chrome and Edge Chromium (Microsoft Edge) Browsers |
| Accept Security Certificates |
| Added new procedure | Verification of the Downloaded ISO | February, 2020 |
| CCEDataProtectTool updates | Bring Upgraded Side A into Service |
| Updated the Common Groung Upgrade Workflow for 2000 Agents Deployment | Multistage Upgrade Workflow for 2000 Agents Deployment |
| Updated Tomcat version | Upgrade Tomcat Utility Upgrade Tomcat |
| Added a new topic for certificates | Certificates for CCE Web Administration |
| Added certificate information | Configure Folder Permissions |
| Common Ground Upgrade Task Flow |
| Common Upgrade Tasks |
| Added a new section for Cloud Connect Installation | Install Cloud Connect |

| Subject | Link |
|---|---|
| Design
                                          					 considerations and guidelines for deploying a Unified CCE solution, including
                                          					 its various components and subsystems. | Design Guide |
| System
                                          					 diagrams, staging steps and sample test cases for supported models of Unified
                                          					 CCE. | Staging Guide |
| Pre-installation requirements and issues to address when you
                                          					 prepare for a Unified CCE installation. | Preinstallation and Planning |

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