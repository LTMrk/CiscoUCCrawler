---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-15-0-1-configuration-guide-pcce-b-admi-ff04feaa8d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_15_0_1/configuration/guide/pcce_b_admin-and-config-guide-15_0_1/preface_m_150.html
retrieved_at: 2026-08-21T16:49:19.440440+00:00
---

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Preface

## Chapter: Preface

# Preface

## Change History

This table lists changes made to this guide. Most recent changes appear at the top.

Change

See

Date

Added 'Configuring Custom SQL Server Port During Packaged CCE 2000 Agents Fresh Install'

Chapter: Custom SQL Server Port

Topic: Configuring Custom SQL Server Port During Packaged CCE 2000 Agents Fresh Install

July 2026

Added 'Custom SQL Server'

Chapter: Custom SQL Server Port

November 2025

Added new topic "Modify Logger"

Post Installation Configuration > Modify Logger

April 2025

Added new subsection pertaining to deployment switching

Post Installation Configuration > Switching to Unified CCE Deployment Type

April 2025

Supported TLS Ciphers are added for FIPS mode and non-FIPS mode

Packaged CCE Administration > Set Up SIP Service

March 2025

Custom Reason Codes

Packaged CCE Administration > Manage Reason Code Conflicts During Upgrade

Feburary 2025

Features removed and unsupported in the CCE 15.0(1) release have been removed from this guide.

See the Release notes for Cisco Contact Center Enterprise Solutions, Release 15.0(1) for the list of removed/unsupported features at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html

January 2025

Product Version Reporting to Cisco SSM

Packaged CCE Administration > Smart Licensing > Product Version Reporting to Cisco SSM

Added a Note about VOS CLIs to manage ciphers.

Packaged CCE Administration > Feature Setup > Manage Features > Cloud Connect Administration

Session Inactivity Timer

Packaged CCE Administration > Miscellaneous

Support for Third Party Gateway

Optional configurations > Update Optional Machines

Smart Transport: Transport mode for Smart Licensing

Smart Licensing > Configure Transport Settings for Smart Licensing

July 2024

## About This Guide

Unified CCE
                           		Administration is a set of web-based tools for creating, configuring, and
                           		maintaining objects, such as agents, teams, skill groups, and call types, that
                           		are used to operate contact centers. This guide
                           		explains the complete set of Unified CCE Administration tools that are
                           		available in a Packaged CCE deployment for an Administrator who has the System
                           		Administrator role. Administrators with other roles, Supervisors, and those who
                           		sign in with other deployment types may not have access to all of tools
                           		documented in this guide.

## Audience

Contact center
                                    			 administrators who configure and run the contact center, manage agents and
                                    			 supervisors, and address operational issues.

Contact center
                                    			 supervisors, who lead agent teams and are responsible for team performance.

This guide
                           		is written with the understanding that your system has been deployed by a
                           		partner or service provider who has validated the deployment type, virtual
                           		machines, and database and has verified that your contact center can receive
                           		and send calls.

## Related
                        	 Documents

Reporting Concepts for Cisco Unified ICM/Contact Center Enterprise

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html

Cisco Packaged Contact Center Enterprise Documentation Guide

https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-documentation-roadmaps-list.html

Cisco.com
                                       					 site for Packaged CCE documentation

https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/tsd-products-support-series-home.html

Solution Design Guide for Cisco Packaged Contact Center Enterprise

https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-technical-reference-list.html

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide

https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html

Cisco Packaged Contact Center Enterprise Features Guide

https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

Cisco Unified Contact Center Enterprise

Cisco Unified Communications Manager

Cisco Unified Intelligence Center

Cisco Finesse

Cisco Unified Customer Voice Portal

Cisco Enterprise Chat and Email

https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/tsd-products-support-series-home.html

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
| Added 'Configuring Custom SQL Server Port During Packaged CCE 2000 Agents Fresh Install' | Chapter: Custom SQL Server Port Topic: Configuring Custom SQL Server Port During Packaged CCE 2000 Agents Fresh Install | July 2026 |
| Added 'Custom SQL Server' | Chapter: Custom SQL Server Port | November 2025 |
| Added new topic "Modify Logger" | Post Installation Configuration > Modify Logger | April 2025 |
| Added new subsection pertaining to deployment switching | Post Installation Configuration > Switching to Unified CCE Deployment Type | April 2025 |
| Supported TLS Ciphers are added for FIPS mode and non-FIPS mode | Packaged CCE Administration > Set Up SIP Service | March 2025 |
| Custom Reason Codes | Packaged CCE Administration > Manage Reason Code Conflicts During Upgrade | Feburary 2025 |
| Features removed and unsupported in the CCE 15.0(1) release have been removed from this guide. | See the Release notes for Cisco Contact Center Enterprise Solutions, Release 15.0(1) for the list of removed/unsupported features at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html | January 2025 |
| Product Version Reporting to Cisco SSM | Packaged CCE Administration > Smart Licensing > Product Version Reporting to Cisco SSM | December 2024 |
| Added a Note about VOS CLIs to manage ciphers. | Packaged CCE Administration > Feature Setup > Manage Features > Cloud Connect Administration | September 2024 |
| Session Inactivity Timer | Packaged CCE Administration > Miscellaneous |
| Support for Third Party Gateway | Optional configurations > Update Optional Machines |
| Smart Transport: Transport mode for Smart Licensing | Smart Licensing > Configure Transport Settings for Smart Licensing | July 2024 |

| Document or resource | Link |
|---|---|
| Reporting Concepts for Cisco Unified ICM/Contact Center Enterprise | https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html |
| Cisco Packaged Contact Center Enterprise Documentation Guide | https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-documentation-roadmaps-list.html |
| Cisco.com
                                       					 site for Packaged CCE documentation | https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/tsd-products-support-series-home.html |
| Solution Design Guide for Cisco Packaged Contact Center Enterprise | https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-technical-reference-list.html |
| Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide | https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html |
| Cisco Packaged Contact Center Enterprise Features Guide | https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html |
| Cisco Unified Contact Center Enterprise | https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/tsd-products-support-series-home.html |
| Cisco Unified Communications Manager | https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html |
| Cisco Unified Intelligence Center | https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/tsd-products-support-series-home.html |
| Cisco Finesse | https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/tsd-products-support-series-home.html |
| Cisco Unified Customer Voice Portal | https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html |
| Cisco Enterprise Chat and Email | https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/tsd-products-support-series-home.html |

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