---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-finesse-finesse-1261-admin-guide-cfin-b-1261-cis-dcc4a3a126
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/finesse/finesse_1261/admin/guide/cfin_b_1261-cisco-finesse-administration-guide/cfin_m_1261-preface.html
retrieved_at: 2026-08-21T15:56:37.531576+00:00
---

Cisco Finesse Administration Guide, Release 12.6(1)

# Cisco Finesse Administration Guide, Release 12.6(1)

Updated: May 14, 2021

Chapter: Preface

## Chapter: Preface

# Preface

## Change History

This table lists the changes that are made to this guide. Most recent changes appear at the top.

Change

See

Date

Updated Release 12.6(1) ES02

November 2021

Provided reference to Desktop Interface API

Manage Desktop Layout>Gadgets and Components

Introduced utils finesse locked_out_users list CLI command

Cisco Finesse CLI>Finesse System Commands

Updated utils finesse node_statistics list CLI command

Cisco Finesse CLI>Finesse System Commands

Updated Release 12.6(1) ES01

August 2021

Added CLIs for Maintenance Mode

Cisco Finesse CLI>Desktop Properties

Added CLIs for AI Services Configuration

Cisco Finesse CLI>AI Services Configuration

Added the following CLIs:

utils finesse show_property desktop

retryLoginAfterLogoutPhoneFailure and utils finesse set_property desktop

retryLoginAfterLogoutPhoneFailure true.

Cisco Finesse CLI>Desktop Properties

May 2021

Added a new topic for Transcript gadgets.

Add Transcript Gadget

Added a new service Orchestration Manager in log collection.

Log Collection

Added Multi-Tab Gadget details.

Gadgets and Components

Added attributes related to Multi-Tab Gadgets.

Default Layout

Added configuration details for Multi-Tab gadgets.

Configure Multi-Tab Gadgets

Added CLIs for Multi-Tab Gadgets.

Desktop Properties

Added CLIs for Enable Automatic Device Selection for Single
                                          Active Device.

Desktop Properties

Added Finesse maintenance mode.

Cisco Finesse Failover Mechanisms

Added CLIs for Finesse maintenance mode services.

Finesse Maintenance Mode Services

Added CLIs for Connected User Info.

ConnectedUserInfo

Added prevent Finesse IP Phone Agent login during maintenance mode.

Finesse IP Phone Agent Login During Maintenance Mode

Added syslog messages for Finesse maintenance mode.

Syslog Support for Critical Log Messages

Added configure custom logon messages

Configure Custom Logon Messages

Added agent device selection details.

Device Selection for Shared ACD Line

Added hostname, IP address and domain name change details.

Manage IP Address and Hostname

Added drop participants from conference call details.

Drop Participants from Conference

Added desktop properties for drop participants.

Customize Desktop Properties

Added desktop properties for drop participants at the team level.

Customize Desktop Properties at Team Level

Updated task activity notification details for gadgets.

Cisco Webex Experience Management

Updated syslog messages with AWDB, CTI details, and Finesse
                                          Maintenancemode details.

Syslog Support for Critical Log Messages

Added Agent PG maintenance mode details.

Cisco Finesse Failover Mechanisms

Added log configuration details.

Finesse Log Configuration

All references to whitelist in the CLIs are changed to allowed_list.

Gadget Source Allowed List

Added Content Security Policy directives.

Supported Content Security Policy Directives

Added new desktop property configuration CLIs.

Desktop Properties

Added new service property configuration CLIs.

Service Properties

Added CLIs to update CUIC gadget URL.

Upgrade

Removed Cisco Finesse Trace Logging.

Added Contact Center AI topic.

Added CLI for Finesse Maintenance Mode Services.

Finesse Maintenance Mode Services

Prevent Finesse IP Phone Agent Login during maintenance

Finesse IP Phone Agent Login during Maintenance Mode

Added Connected Agents gadget in Cisco Administration
                                          Console.

Manage Connected Agents

Removed Cisco Finesse Notification Service Logging.

—

Enable or Disable Plain XMPP Socket—Port 5223

Enable or Disable Plain XMPP Socket—Port 5223

DTMF Updates

Customize Desktop Properties

Restricting Access - External XMPP Notification Port 5223

Restricting Access - External XMPP Notification Port 5223

Changed Finesse Host to Hostname in one of the entities in the table

Connected Agents

## About This
                        	 Guide

The Cisco Finesse Administration Guide describes how to
                           		administer and maintain Cisco Finesse.

## Audience

This guide is
                              		  prepared for Unified Contact Center Enterprise system administrators who
                              		  configure, administer, and monitor Cisco Finesse.

For information about administering Finesse within a Unified Contact Center Express environment, see Cisco Unified Contact Center Express Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html .

## Related
                        	 Documents

Document
                                       					 or resource

Link

Cisco Finesse Documentation
                                          						Guide

https://www.cisco.com/en/US/partner/products/ps11324/products_documentation_roadmaps_list.html

Configure SNMP Trap in Cisco Finesse

https://www.cisco.com/c/en/us/support/docs/contact-center/finesse/214387-configure-snmp-trap-in-cisco-finesse.html

Cisco.com
                                       					 site for Finesse documentation

https://www.cisco.com/en/US/partner/products/ps11324/tsd_products_support_series_home.html

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
|  |  |  |
| Updated Release 12.6(1) ES02 | November 2021 |
| Provided reference to Desktop Interface API | Manage Desktop Layout>Gadgets and Components |
| Introduced utils finesse locked_out_users list CLI command | Cisco Finesse CLI>Finesse System Commands |
| Updated utils finesse node_statistics list CLI command | Cisco Finesse CLI>Finesse System Commands |
| Updated Release 12.6(1) ES01 | August 2021 |
| Added CLIs for Maintenance Mode | Cisco Finesse CLI>Desktop Properties |
| Added CLIs for AI Services Configuration | Cisco Finesse CLI>AI Services Configuration |
| Added the following CLIs: utils finesse show_property desktop retryLoginAfterLogoutPhoneFailure and utils finesse set_property desktop retryLoginAfterLogoutPhoneFailure true. | Cisco Finesse CLI>Desktop Properties |
| Initial Release of Document for Release 12.6(1) | May 2021 |
| Added a new topic for Transcript gadgets. | Add Transcript Gadget |
| Added a new service Orchestration Manager in log collection. | Log Collection |
| Added Multi-Tab Gadget details. | Gadgets and Components |
| Added attributes related to Multi-Tab Gadgets. | Default Layout XML |
| Added configuration details for Multi-Tab gadgets. | Configure Multi-Tab Gadgets |
| Added CLIs for Multi-Tab Gadgets. | Desktop Properties |
| Added CLIs for Enable Automatic Device Selection for Single
                                          Active Device. | Desktop Properties |
| Added Finesse maintenance mode. | Cisco Finesse Failover Mechanisms |
| Added CLIs for Finesse maintenance mode services. | Finesse Maintenance Mode Services |
| Added CLIs for Connected User Info. | ConnectedUserInfo |
| Added prevent Finesse IP Phone Agent login during maintenance mode. | Finesse IP Phone Agent Login During Maintenance Mode |
| Added syslog messages for Finesse maintenance mode. | Syslog Support for Critical Log Messages |
| Added configure custom logon messages | Configure Custom Logon Messages |
| Added agent device selection details. | Device Selection for Shared ACD Line |
| Added hostname, IP address and domain name change details. | Manage IP Address and Hostname |
| Added drop participants from conference call details. | Drop Participants from Conference |
| Added desktop properties for drop participants. | Customize Desktop Properties |
| Added desktop properties for drop participants at the team level. | Customize Desktop Properties at Team Level |
| Updated task activity notification details for gadgets. | Cisco Webex Experience Management |
| Updated syslog messages with AWDB, CTI details, and Finesse
                                          Maintenancemode details. | Syslog Support for Critical Log Messages |
| Added Agent PG maintenance mode details. | Cisco Finesse Failover Mechanisms |
| Added log configuration details. | Finesse Log Configuration |
| All references to whitelist in the CLIs are changed to allowed_list. | Gadget Source Allowed List |
| Added Content Security Policy directives. | Supported Content Security Policy Directives |
| Added new desktop property configuration CLIs. | Desktop Properties |
| Added new service property configuration CLIs. | Service Properties |
| Added CLIs to update CUIC gadget URL. | Upgrade |
| Removed Cisco Finesse Trace Logging. |  |
| Added Contact Center AI topic. |  |
| Added CLI for Finesse Maintenance Mode Services. | Finesse Maintenance Mode Services |
| Prevent Finesse IP Phone Agent Login during maintenance . | Finesse IP Phone Agent Login during Maintenance Mode |
| Added Connected Agents gadget in Cisco Administration
                                          Console. | Manage Connected Agents |
| Removed Cisco Finesse Notification Service Logging. | — |
| Enable or Disable Plain XMPP Socket—Port 5223 | Enable or Disable Plain XMPP Socket—Port 5223 |
| DTMF Updates | Customize Desktop Properties |
| Restricting Access - External XMPP Notification Port 5223 | Restricting Access - External XMPP Notification Port 5223 |
| Changed Finesse Host to Hostname in one of the entities in the table | Connected Agents |

| Document
                                       					 or resource | Link |
|---|---|
| Cisco Finesse Documentation
                                          						Guide | https://www.cisco.com/en/US/partner/products/ps11324/products_documentation_roadmaps_list.html |
| Configure SNMP Trap in Cisco Finesse | https://www.cisco.com/c/en/us/support/docs/contact-center/finesse/214387-configure-snmp-trap-in-cisco-finesse.html |
| Cisco.com
                                       					 site for Finesse documentation | https://www.cisco.com/en/US/partner/products/ps11324/tsd_products_support_series_home.html |

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