---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-installatio-de40860b4f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/installation/guide/ucce_b_install_upgrade_guide_1262/ucce_b_12_6_1-install_upgrade_guide_preface_00.html
retrieved_at: 2026-08-16T19:59:21.528936+00:00
---

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2)

Updated: April 28, 2023

Chapter: Preface

## Chapter: Preface

# Preface

## Change History

This table lists changes made to this guide. Most recent changes appear at the top:

See

Date

Initial Release of Document for Release 12.6(2)

Added new topics to generate Indentity Token

CCE Orchestration > Orchestration in CCE Deployment > Deployment Tasks > Generate Artifactory Authentication Credentials >
                                       Generate the Artifactory Identity Token > Configure Identity Token Auto Rotation

March 2026

Replaced API Key with Artifactory Authentication Credentials

CCE Orchestration > Orchestration in CCE Deployment > Deployment Tasks > CLI to Configure Artifactory URL and Artifactory
                                       Authentication Credentials

March 2026

Custom SQL Server Port

Chapter: Common Ground Upgrade

Chapter: Technology Refresh Upgrade

Doc update: Added a note pertaining to Custom SQL server port.

Added the topic Install Microsoft Windows 11 for Administration Client

Preinstallation > Preinstallation Tasks > Set Up Third-Party Software

Simplified upgrade using orchestration

CCE Orchestration

CLI to configure software download schedule

CLI to configure the bandwidth for Orchestration software download

Enforce software download from Cisco hosted software artifactory

CLI to configure proxy for orchestration

Serviceability enhancement for entitlement failure update in CLI to configure artifactory URL and API key

Unified ICM upgrade path

Unified CCE Upgrade Overview

Multistage upgrade

Multistage UpgradeWorkflow for 4000 Agents and above Deployments

Java Requirements

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
| Initial Release of Document for Release 12.6(2) |  |
| Added new topics to generate Indentity Token | CCE Orchestration > Orchestration in CCE Deployment > Deployment Tasks > Generate Artifactory Authentication Credentials >
                                       Generate the Artifactory Identity Token > Configure Identity Token Auto Rotation | March 2026 |
| Replaced API Key with Artifactory Authentication Credentials | CCE Orchestration > Orchestration in CCE Deployment > Deployment Tasks > CLI to Configure Artifactory URL and Artifactory
                                       Authentication Credentials | March 2026 |
| Custom SQL Server Port | Chapter: Common Ground Upgrade Chapter: Technology Refresh Upgrade Doc update: Added a note pertaining to Custom SQL server port. | December 2025 |
| Added the topic Install Microsoft Windows 11 for Administration Client | Preinstallation > Preinstallation Tasks > Set Up Third-Party Software | April 2023 |
| Simplified upgrade using orchestration | CCE Orchestration |
| CLI to configure software download schedule |
| CLI to configure the bandwidth for Orchestration software download |
| Enforce software download from Cisco hosted software artifactory |
| CLI to configure proxy for orchestration |
| Serviceability enhancement for entitlement failure update in CLI to configure artifactory URL and API key |
| Unified ICM upgrade path | Unified CCE Upgrade Overview |
| Multistage upgrade | Multistage UpgradeWorkflow for 4000 Agents and above Deployments |
| Java Upgrade | Java Requirements |

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