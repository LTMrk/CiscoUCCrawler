---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-configurati-5a0aeb8373
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/configuration/guide/ucce_b_serviceability-guide-for-cisco-unified-icm-contact-center-enterprise-release-15-0/ucce_m_preface_15_0.html
retrieved_at: 2026-08-25T00:03:16.867762+00:00
---

Serviceability Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

# Serviceability Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

Updated: April 30, 2025

Chapter: Preface

## Chapter: Preface

# Preface

## Change history

This table lists the changes made to this guide. The most recent changes appear at the top.

Date

Initial Release of Document for Release 15(0)

Added AppDynamics - Loose Coupling details

Chapter: CCE Serviceability and Monitoring using AppDynamics

Topic: Prerequistes

Topic: Install, Upgrade, or Downgrade AppDynamics Agents

Topic: Performance Monitoring

Topic: Dashboards

Topic: Check Logs

December

Added serviceability details for cache service

Chapter: Cloud Connect Serviceability

Topic: Serviceability for Cache Service

December 2025

Added trace for Unified Config

Chapter: Contact Center Trace Levels

Topic: Trace - Unified Config (CCE API Server)

December 2025

Added MRD configuration counter details

Access JMX Counters using API

Access Counters using JConsole

## About This Guide

This document contains system diagrams, staging steps and sample test cases for supported models of Unified CCE.

The Serviceability Guide for Cisco Unified CCE provides tools and procedures to monitor, troubleshoot, and maintain system
                           health across UCCE components. It covers diagnostics, logs, service control, SNMP/syslog integration, and high availability
                           features to ensure optimal system performance and reliability.

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
| Initial Release of Document for Release 15(0) |  |
| Added AppDynamics - Loose Coupling details | Chapter: CCE Serviceability and Monitoring using AppDynamics Topic: Prerequistes Topic: Install, Upgrade, or Downgrade AppDynamics Agents Topic: Performance Monitoring Topic: Dashboards Topic: Check Logs | December 2025 |
| Added serviceability details for cache service | Chapter: Cloud Connect Serviceability Topic: Serviceability for Cache Service | December 2025 |
| Added trace for Unified Config | Chapter: Contact Center Trace Levels Topic: Trace - Unified Config (CCE API Server) | December 2025 |
| Added MRD configuration counter details | Access JMX Counters using API Access Counters using JConsole | Oct 2024 |
| Added 'Download Certificate for System CLI' topic | Diagnostic Tools > Download Certificate for System CLI | Oct 2024 |

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