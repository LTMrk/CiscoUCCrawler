---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-installatio-d7fa4bca80
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/installation/guide/ucce_b_150_install_upgrade_guide/preface.html
retrieved_at: 2026-08-16T19:56:08.082353+00:00
---

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Preface

## Chapter: Preface

# Preface

## Change History

This table lists changes made to this guide. Most recent changes appear at the top:

See

Date

This chapter describes the prerequisites, procedures, and post-configuration required to migrate the CCE and its components
                                          from VMware to Nutanix.

Migration from VMware to Nutanix chapter

July 2026

Added the below new topics,

To enable Orchestration Parallel Patch/Rollback options

To initiate deployment cache update

To check status of Orchestration Deployment Cache

To configure Orchestration Scheduled Jobs

CCE Orchestration > Orchestration in CCE Deployment > Deployment Tasks > CLI To Configure Orchestration Maximum Parallel Tasks
                                          > CLI to Enforce Deployment Cache Update > CLI to Check Status of Orchestration Deployment Cache > CLI to Configure Orchestration
                                          Scheduled Jobs

April 2026

Added new topics to generate Indentity Token

CCE Orchestration > Orchestration in CCE Deployment > Deployment Tasks > Generate Artifactory Authentication Credentials >
                                          Generate the Artifactory Identity Token > Configure Identity Token Auto Rotation

March 2026

Replaced API Key with Artifactory Authentication Credentials

CCE Orchestration > Orchestration in CCE Deployment > Deployment Tasks > CLI to Configure Artifactory URL and Artifactory
                                          Authentication Credentials

March 2026

Added CLI Commands

CLI Commands > Cloud Connect CLI Commands > CLI Commands for Cache Service

Replaced CUSP with CCCSP.

Throughout the document

Maintenance Mode supports Router and Rogger through Orchestration.

CCE Orchestration > Orchestration in CCE Deployment > Administration Tasks > Install Patch to Specific Node or Group of Nodes

CCE Orchestration > Orchestration in CCE Deployment > Administration Tasks > Roll Back Patch from Specific Node or Group of
                                          Nodes

CCE Orchestration > Orchestration in CCE Deployment > Administration Tasks > Install Windows Updates to Specific Node or Group
                                          of Nodes

CCE Orchestration > Orchestration in CCE Deployment > Administration Tasks > Roll Back Windows Update from Specific Node or
                                          Group of Nodes

CCE Orchestration > Orchestration in CCE Deployment > Administration Tasks > Initiate maintenance mode for a specific nodes

August 2025

Initial Release of Document for Release 15.0(1)

April 30, 2025

Upgrade to Visual Studio 2022

Throughout the document

Updated Microsoft Windows Server to 2022

Throughout the document

Updated Microsoft SQL Server to 2022

Throughout the document

Updated the OpenLogic-OpenJDK JRE details and included a note in the Java Requirements topic

Preparation > Java Requirements

Added a note about VRU PG that uses existing maintenance mode from Unified CVP

Common Ground Upgrade > Upgrade Peripheral Gateways

Bring down all Unified CCE services on the servers you are upgrading by invoking maintenance mode

Chapter: Common Ground Upgrade

Throughout this chapter

Chapter: Common Upgrade Task

Throughout this chapter

Added Cisco Reverse Proxy upgrade as Stage 1 in the upgrade flow

Throughout this chapter

Updated the common ground task flow

Common Ground Upgrade > Common Ground Upgrade Task Flow

Section in this table that impacts: Unified CCE Central Controller and Administration & Data server Components

Replaced VXML gateway instances with Cisco VVB

Initial configuration Tasks> Configure Unified CVP Operations Console> Configure SIP Server Group

Initial configuration Tasks> Configure Unified CVP Operations Console> Configure Dialed Number Patterns

Features removed and unsupported in the CCE 15.0(1) release have been removed from this guide

See the Release notes for Cisco Contact Center Enterprise Solutions, Release 15.0(1) for the list of removed/unsupported features at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html

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
| This chapter describes the prerequisites, procedures, and post-configuration required to migrate the CCE and its components
                                          from VMware to Nutanix. | Migration from VMware to Nutanix chapter | July 2026 |
| Added the below new topics, To enable Orchestration Parallel Patch/Rollback options To initiate deployment cache update To check status of Orchestration Deployment Cache To configure Orchestration Scheduled Jobs | CCE Orchestration > Orchestration in CCE Deployment > Deployment Tasks > CLI To Configure Orchestration Maximum Parallel Tasks
                                          > CLI to Enforce Deployment Cache Update > CLI to Check Status of Orchestration Deployment Cache > CLI to Configure Orchestration
                                          Scheduled Jobs | April 2026 |
| Added new topics to generate Indentity Token | CCE Orchestration > Orchestration in CCE Deployment > Deployment Tasks > Generate Artifactory Authentication Credentials >
                                          Generate the Artifactory Identity Token > Configure Identity Token Auto Rotation | March 2026 |
| Replaced API Key with Artifactory Authentication Credentials | CCE Orchestration > Orchestration in CCE Deployment > Deployment Tasks > CLI to Configure Artifactory URL and Artifactory
                                          Authentication Credentials | March 2026 |
| Added CLI Commands | CLI Commands > Cloud Connect CLI Commands > CLI Commands for Cache Service | November 2025 |
| Replaced CUSP with CCCSP. | Throughout the document | November 2025 |
| Maintenance Mode supports Router and Rogger through Orchestration. | CCE Orchestration > Orchestration in CCE Deployment > Administration Tasks > Install Patch to Specific Node or Group of Nodes CCE Orchestration > Orchestration in CCE Deployment > Administration Tasks > Roll Back Patch from Specific Node or Group of
                                          Nodes CCE Orchestration > Orchestration in CCE Deployment > Administration Tasks > Install Windows Updates to Specific Node or Group
                                          of Nodes CCE Orchestration > Orchestration in CCE Deployment > Administration Tasks > Roll Back Windows Update from Specific Node or
                                          Group of Nodes CCE Orchestration > Orchestration in CCE Deployment > Administration Tasks > Initiate maintenance mode for a specific nodes | August 2025 |
| Initial Release of Document for Release 15.0(1) | April 30, 2025 |
| Upgrade to Visual Studio 2022 | Throughout the document |
| Updated Microsoft Windows Server to 2022 | Throughout the document |
| Updated Microsoft SQL Server to 2022 | Throughout the document |
| Updated the OpenLogic-OpenJDK JRE details and included a note in the Java Requirements topic | Preparation > Java Requirements |
| Added a note about VRU PG that uses existing maintenance mode from Unified CVP | Common Ground Upgrade > Upgrade Peripheral Gateways |
| Bring down all Unified CCE services on the servers you are upgrading by invoking maintenance mode | Chapter: Common Ground Upgrade Throughout this chapter Chapter: Common Upgrade Task Throughout this chapter |
| Added Cisco Reverse Proxy upgrade as Stage 1 in the upgrade flow | Throughout this chapter |
| Updated the common ground task flow | Common Ground Upgrade > Common Ground Upgrade Task Flow Section in this table that impacts: Unified CCE Central Controller and Administration & Data server Components |
| Replaced VXML gateway instances with Cisco VVB | Initial configuration Tasks> Configure Unified CVP Operations Console> Configure SIP Server Group Initial configuration Tasks> Configure Unified CVP Operations Console> Configure Dialed Number Patterns |
| Features removed and unsupported in the CCE 15.0(1) release have been removed from this guide | See the Release notes for Cisco Contact Center Enterprise Solutions, Release 15.0(1) for the list of removed/unsupported features at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html |

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