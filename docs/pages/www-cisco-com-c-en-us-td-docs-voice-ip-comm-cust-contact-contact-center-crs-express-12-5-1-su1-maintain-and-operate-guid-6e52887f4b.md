---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su1-maintain-and-operate-guid-6e52887f4b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su1/maintain_and_operate/guide/uccx_b_1251su1admin-and-operations-guide/uccx_b_12_5_2admin-and-operations-guide_preface_00.html
retrieved_at: 2026-08-16T21:38:03.920653+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)SU1

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)SU1

Updated: January 31, 2021

Chapter: Preface

## Chapter: Preface

# Preface

## Change History

This table lists the changes made to this guide. The most recent changes appear at the top.

Change

See

Date

Added information about the availability of case-insensitive login IDs for agents and supervisors

Unified CCX AdministrationWeb Interface >Access Unified CCX Administration Web Interface

Cisco Unified Contact Center Express Supervisor and User Options Plug-Ins > Unified CCX Supervisor Web Interface >Access Unified
                                       CCX Supervisor Web Page

System Menu  >Single Sign-On (SSO)

October 2021

Added information about the availability of team settings to override global settings

System Menu>System Parameters>Agent Settings

July 2021

Added information about the Team Settings section

Subsystems Menu>RmCmMenu>Teams Configuration>Create Teams Subsystems Menu>RmCmMenu>Teams Configuration>Modify Teams

Added information about the availability of the Change Agent State to Not Ready when Agent Busy on Non ACD Line setting in the Supervisor Capability View menu

Tools Menu>User Management Menu>Supervisor Capability View

Tools Menu>User Management Menu>Supervisor Capability View>View Supervisor Details

Initial Release of Document for Release 12.5(1) SU1

January 2021

Removed the utils uccx notification service log command

Command Line Interface>Utils Commands

Removed the set cuic trace and show cuic trace commands

Command Line Interface>Cisco Unified Intelligence Center Commands

Included Syslog Support for Critical Cisco Finesse Log Messages

Real-Time Monitoring > Tools > Syslog Support for Critical Cisco Finesse Log Messages

Removed the Cisco Finesse Trace Logging section

Command Line Interface>Cisco Finesse Commands

Included Finesse Log Configuration

Command Line Interface > Cisco Finesse Commands > Finesse Log Configuration

Included Connected Agents

Cisco Finesse>Cisco Finesse Administration Console>Manage Connected Agents>Connected Agents

Command Line Interface > Cisco Finesse Commands > ConnectedUsersInfo

Included Multi-Tab Gadget

Cisco Finesse>Cisco Finesse Administration Console>Manage Desktop Layout>Gadgets and Components>Multi-Tab Gadgets

Cisco Finesse>Cisco Finesse Administration Console>Manage Desktop Layout>Gadgets and Components>Call Control Gadget in Multi-Tab

Cisco Finesse>Cisco Finesse Administration Console>Manage Desktop Layout>Default Layout XML

Cisco Finesse>Cisco Finesse Administration Console>Manage Desktop Layout>Configure Multi-Tab Gadget Layout

Cisco Finesse>Cisco Finesse Administration Console>Manage Desktop Layout>Drag-and-Drop and Resize Gadget or Component

Command Line Interface>Cisco Finesse Commands>Desktop Properties>Maximum Number of Visible Multi-Tab Gadget Tabs, Non-Page
                                       Level Gadgets Preceding Page-Level Gadgets in a Multi-Tab Gadget, Notifications from Call Control in Multi-Tab Gadgets

The procedure to set up certificates in Chrome is updated with Edge Chromium

Unified CCX System Management>Set Up Certificates>Set Up CA Certificate for Chrome and Edge Browsers

Cisco Finesse>Cisco Finesse Administration Console>Getting Started>Administration Tools>Cisco Finesse Administration Console>Sign
                                       In to Cisco Finesse Administration Console

Added the command set cuic properties report-query-timeout

Command Line Interface>Cisco Unified Intelligence Center Commands

Updated SRTP with the information related to RmCm provider user

System Menu>System Parameters

Added information related to Data Check and Data Resync when SRTP is selected

Telephony and Media Provision>Provision Unified CM Telephony Subsystem>Synchronize Unified CM Telephony Data

Added information related to data synchronization

System Menu>System Parameters

Added info about restoring from a backup when SRTP is enabled and disabled

Backup and Restore>Restore Scenarios

Introduced setting of webapp session timeout

Unified CCX AdministrationWeb Interface>Access Unified CCX Administration Web Interface

Added the commands show webapp session timeout , show cli session timeout , set webapp session maxlimit , and set webapp session timeout

Command Line Interface>Show commands

Command Line Interface>Set Commands

Updated Agent ID details to support 64 characters

Provision Unified CM for Unified CCX>Unified Communications Manager for Unified CCX Configuration>Unified Communications Manager
                                       Users as Unified CCX Agents

Added a note about secure JTAPI connection for the SRTP field

System Menu>System Parameters

Added information about custom logon message

Unified CCX AdministrationWeb Interface>Access Unified CCX Administration Web Interface

Command Line Interface>Cisco Finesse Commands>Desktop Properties>Security Banner Message for Desktop Users

Command Line Interface>Cisco Finesse Commands>Service Properties>Security Banner Message for Administrators

Removed Cisco Unified Intelligence Center Services and added a note about CUIC CLI

Cisco Unified CCX Serviceability>Traces>Component Trace Files

Added the commands utils cuic logging list , utils cuic logging config set , utils cuic logging update , utils cuic logging config show , utils cuic logging reset, utils cuic logging config clear, utils cuic session list, and utils cuic session delete

Command Line Interface>Cisco Unified Intelligence Center Commands

Updated the description of Authorization Status and Status fields with Added Authorized - Reserved and Not Authorized - Reserved

System Menu>License Information>Smart License Management

Added the fields Reserved Count , License Control , Current License Type , Overage Allowance , and I have purchased High Availability License

System Menu>License Information>Smart License Management

Added information about the points to be considered before enabling FIPS

Command Line Interface>Utils Commands>utils fips

Added the new alerts EmailOAuthConnectionFailed and EmailAuthenticationFailed

Real-Time Monitoring>Tools>Alerts>Unified CCX Alerts

Added the new fields Authentication Type and Private Key

Added a note for Email password field

Subsystems Menu>Chat and Email Menu Options>Contact Service Queues

Added information about accessibility support for visually challenged

Subsystems Menu>Chat and Email Menu Options>Chat Widgets

Updated Localize Accessibility Messages

Subsystems Menu>Chat and Email Menu Options>Chat Widgets>Chat Widget Configuration>Integration of Chat Code into CustomerWebsite>Localize
                                       Accessibility Messages

Added a new topic to list Specific License Reservation commands

Command Line Interface>Specific License Reservation Commands

Added the new field HTTP

Subsystems Menu>Chat and Email Menu Options>Mail Server Configuration

Included Agent Device Selection

System Menu>System Parameters

Included Auto Answer

Provision of Unified CCX>Teams Configuration

Subsystems Menu>RmCm Menu>Teams Configuration

## About This Guide

Cisco Unified Contact Center Express (Unified CCX), a member of
                           		the Cisco Unified Communications family of products, manages customer voice
                           		contact centers for departments, branches, or small to medium-size companies
                           		planning to deploy an entry-level or mid-market contact center solution.

The Cisco Unified CCX Administration Guide provides instructions
                           		for using the Administration web interface to provision the subsystems of the
                           		Unified CCX package and to configure Unified CCX applications.

This guide shows you how to implement the following two systems
                           		that integrate with the Unified CCX:

Cisco Unified Contact Center Express (Unified CCX)

Cisco Unified IP IVR

This guide also includes a reference section that describes all
                           		the menus and menu options of the Unified CCXAdministration web interface.

This guide will help you to:

Perform initial configuration tasks

Administer applications such as the Unified CCXEngine and other
                                 			 components of the CiscoUnified Communications family of products

Familiarize yourself with the menus and menu options of the Unified
                                 			 CCXAdministration web interface

## Audience

The Cisco Unified CCX Administration Guide is written for business analysts and application designers who have the domain-specific knowledge required to create multimedia
                           and telephony customer response applications. Experience or training with Java is not required but is useful for making best
                           use of the capabilities of the Cisco Unified Communications family of products.

## Conventions

This manual uses the following conventions.

Convention

Description

boldface font

Boldface font is used to indicate commands, such as user
                                       					 entries, keys, buttons, and folder and submenu names. For example:

Choose Edit > Find

Click Finish .

italic font

Italic font is used to indicate the following:

To introduce a new term. Example: A skill group is a collection of agents who share
                                             						  similar skills.

For emphasis. Example: Do not use the numerical naming convention.

An argument for which you must supply values.

Example:

IF ( condition, true-value, false-value )

A book title. Example:

See the Cisco Unified Contact Center Express Installation
                                                							 Guide .

window font

Window font, such as Courier, is used for the following:

Text as it appears in code or information that the system
                                             						  displays. Example:

<html><title> Cisco Systems,Inc.
                                                							 </title></html>

File names. Example: tserver.properties .

Directory paths. Example:

C:\Program Files\Adobe

string

Nonquoted sets of characters (strings) appear in regular font.
                                       					 Do not use quotation marks around a string or the string will include the
                                       					 quotation marks.

[ ]

Optional elements appear in square brackets.

{ x | y | z }

Alternative keywords are grouped in braces and separated by
                                       					 vertical bars.

[ x | y | z ]

Optional alternative keywords are grouped in brackets and
                                       					 separated by vertical bars.

< >

Angle brackets are used to indicate the following:

For arguments where the context does not allow italic,
                                             						  such as ASCII output.

A character string that the user enters but that does not
                                             						  appear on the window such as a password.

^

The key labeled Control is represented in screen displays by
                                       					 the symbol ^. For example, the screen instruction to hold down the Control key
                                       					 while you press the D key appears as ^D.

## Related
                        	 Documents

Document or Resource

Link

Cisco Unified Contact Center Express Documentation Guide

https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_documentation_roadmaps_list.html

Cisco Unified CCX documentation

https://www.cisco.com/en/US/products/sw/custcosw/ps1846/tsd_products_support_series_home.html

Cisco Unified Intelligence Center documentation

https://www.cisco.com/en/US/products/ps9755/tsd_products_support_series_home.html

Cisco Finesse documentation

https://www.cisco.com/en/US/products/ps11324/tsd_products_support_series_home.html

Cisco Customer Collaboration Platform documentation

From Unified CCX Release 12.5(1), CCP documents are available in the Cisco Unified CCX documentation folder.

https://www.cisco.com/en/US/products/sw/custcosw/ps1846/tsd_products_support_series_home.html

Cisco Unified CCX Virtualization Information

https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-contact-center-express.html

Cisco Unified CCX Compatibility Information

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html

## Documentation and
                        	 Support

To download documentation, submit a service request, and find additional information, see What's New in Cisco Product Documentation at https://www.cisco.com/en/US/docs/general/whatsnew/whatsnew.html .

## Documentation Feedback

To provide your
                           		feedback for this document, send an email to:

contactcenterproducts_docfeedback@cisco.com

| Change | See | Date |
|---|---|---|
| Added information about the availability of case-insensitive login IDs for agents and supervisors | Unified CCX AdministrationWeb Interface >Access Unified CCX Administration Web Interface Cisco Unified Contact Center Express Supervisor and User Options Plug-Ins > Unified CCX Supervisor Web Interface >Access Unified
                                       CCX Supervisor Web Page System Menu  >Single Sign-On (SSO) | October 2021 |
| Added information about the availability of team settings to override global settings | System Menu>System Parameters>Agent Settings | July 2021 |
| Added information about the Team Settings section | Subsystems Menu>RmCmMenu>Teams Configuration>Create Teams Subsystems Menu>RmCmMenu>Teams Configuration>Modify Teams |
| Added information about the availability of the Change Agent State to Not Ready when Agent Busy on Non ACD Line setting in the Supervisor Capability View menu | Tools Menu>User Management Menu>Supervisor Capability View Tools Menu>User Management Menu>Supervisor Capability View>View Supervisor Details |
| Initial Release of Document for Release 12.5(1) SU1 | January 2021 |
| Removed the utils uccx notification service log command | Command Line Interface>Utils Commands |
| Removed the set cuic trace and show cuic trace commands | Command Line Interface>Cisco Unified Intelligence Center Commands |
| Included Syslog Support for Critical Cisco Finesse Log Messages | Real-Time Monitoring > Tools > Syslog Support for Critical Cisco Finesse Log Messages |
| Removed the Cisco Finesse Trace Logging section | Command Line Interface>Cisco Finesse Commands |
| Included Finesse Log Configuration | Command Line Interface > Cisco Finesse Commands > Finesse Log Configuration |
| Included Connected Agents | Cisco Finesse>Cisco Finesse Administration Console>Manage Connected Agents>Connected Agents Command Line Interface > Cisco Finesse Commands > ConnectedUsersInfo |
| Included Multi-Tab Gadget | Cisco Finesse>Cisco Finesse Administration Console>Manage Desktop Layout>Gadgets and Components>Multi-Tab Gadgets Cisco Finesse>Cisco Finesse Administration Console>Manage Desktop Layout>Gadgets and Components>Call Control Gadget in Multi-Tab Cisco Finesse>Cisco Finesse Administration Console>Manage Desktop Layout>Default Layout XML Cisco Finesse>Cisco Finesse Administration Console>Manage Desktop Layout>Configure Multi-Tab Gadget Layout Cisco Finesse>Cisco Finesse Administration Console>Manage Desktop Layout>Drag-and-Drop and Resize Gadget or Component Command Line Interface>Cisco Finesse Commands>Desktop Properties>Maximum Number of Visible Multi-Tab Gadget Tabs, Non-Page
                                       Level Gadgets Preceding Page-Level Gadgets in a Multi-Tab Gadget, Notifications from Call Control in Multi-Tab Gadgets |
| The procedure to set up certificates in Chrome is updated with Edge Chromium | Unified CCX System Management>Set Up Certificates>Set Up CA Certificate for Chrome and Edge Browsers Cisco Finesse>Cisco Finesse Administration Console>Getting Started>Administration Tools>Cisco Finesse Administration Console>Sign
                                       In to Cisco Finesse Administration Console |
| Added the command set cuic properties report-query-timeout | Command Line Interface>Cisco Unified Intelligence Center Commands |
| Updated SRTP with the information related to RmCm provider user | System Menu>System Parameters |
| Added information related to Data Check and Data Resync when SRTP is selected | Telephony and Media Provision>Provision Unified CM Telephony Subsystem>Synchronize Unified CM Telephony Data |
| Added information related to data synchronization | System Menu>System Parameters |
| Added info about restoring from a backup when SRTP is enabled and disabled | Backup and Restore>Restore Scenarios |
| Introduced setting of webapp session timeout | Unified CCX AdministrationWeb Interface>Access Unified CCX Administration Web Interface |
| Added the commands show webapp session timeout , show cli session timeout , set webapp session maxlimit , and set webapp session timeout | Command Line Interface>Show commands Command Line Interface>Set Commands |
| Updated Agent ID details to support 64 characters | Provision Unified CM for Unified CCX>Unified Communications Manager for Unified CCX Configuration>Unified Communications Manager
                                       Users as Unified CCX Agents |
| Added a note about secure JTAPI connection for the SRTP field | System Menu>System Parameters |
| Added information about custom logon message | Unified CCX AdministrationWeb Interface>Access Unified CCX Administration Web Interface Command Line Interface>Cisco Finesse Commands>Desktop Properties>Security Banner Message for Desktop Users Command Line Interface>Cisco Finesse Commands>Service Properties>Security Banner Message for Administrators |
| Removed Cisco Unified Intelligence Center Services and added a note about CUIC CLI | Cisco Unified CCX Serviceability>Traces>Component Trace Files |
| Added the commands utils cuic logging list , utils cuic logging config set , utils cuic logging update , utils cuic logging config show , utils cuic logging reset, utils cuic logging config clear, utils cuic session list, and utils cuic session delete | Command Line Interface>Cisco Unified Intelligence Center Commands |
| Updated the description of Authorization Status and Status fields with Added Authorized - Reserved and Not Authorized - Reserved | System Menu>License Information>Smart License Management |
| Added the fields Reserved Count , License Control , Current License Type , Overage Allowance , and I have purchased High Availability License | System Menu>License Information>Smart License Management |
| Added information about the points to be considered before enabling FIPS | Command Line Interface>Utils Commands>utils fips |
| Added the new alerts EmailOAuthConnectionFailed and EmailAuthenticationFailed | Real-Time Monitoring>Tools>Alerts>Unified CCX Alerts |
| Added the new fields Authentication Type and Private Key Added a note for Email password field | Subsystems Menu>Chat and Email Menu Options>Contact Service Queues |
| Added information about accessibility support for visually challenged | Subsystems Menu>Chat and Email Menu Options>Chat Widgets |
| Updated Localize Accessibility Messages | Subsystems Menu>Chat and Email Menu Options>Chat Widgets>Chat Widget Configuration>Integration of Chat Code into CustomerWebsite>Localize
                                       Accessibility Messages |
| Added a new topic to list Specific License Reservation commands | Command Line Interface>Specific License Reservation Commands |
| Added the new field HTTP | Subsystems Menu>Chat and Email Menu Options>Mail Server Configuration |
| Included Agent Device Selection | System Menu>System Parameters |
| Included Auto Answer | Provision of Unified CCX>Teams Configuration Subsystems Menu>RmCm Menu>Teams Configuration |

| Convention | Description |
|---|---|
| boldface font | Boldface font is used to indicate commands, such as user
                                       					 entries, keys, buttons, and folder and submenu names. For example: Choose Edit > Find Click Finish . |
| italic font | Italic font is used to indicate the following: To introduce a new term. Example: A skill group is a collection of agents who share
                                             						  similar skills. For emphasis. Example: Do not use the numerical naming convention. An argument for which you must supply values. Example: IF ( condition, true-value, false-value ) A book title. Example: See the Cisco Unified Contact Center Express Installation
                                                							 Guide . |
| window font | Window font, such as Courier, is used for the following: Text as it appears in code or information that the system
                                             						  displays. Example: <html><title> Cisco Systems,Inc.
                                                							 </title></html> File names. Example: tserver.properties . Directory paths. Example: C:\Program Files\Adobe |
| string | Nonquoted sets of characters (strings) appear in regular font.
                                       					 Do not use quotation marks around a string or the string will include the
                                       					 quotation marks. |
| [ ] | Optional elements appear in square brackets. |
| { x \| y \| z } | Alternative keywords are grouped in braces and separated by
                                       					 vertical bars. |
| [ x \| y \| z ] | Optional alternative keywords are grouped in brackets and
                                       					 separated by vertical bars. |
| < > | Angle brackets are used to indicate the following: For arguments where the context does not allow italic,
                                             						  such as ASCII output. A character string that the user enters but that does not
                                             						  appear on the window such as a password. |
| ^ | The key labeled Control is represented in screen displays by
                                       					 the symbol ^. For example, the screen instruction to hold down the Control key
                                       					 while you press the D key appears as ^D. |

| Document or Resource | Link |
|---|---|
| Cisco Unified Contact Center Express Documentation Guide | https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_documentation_roadmaps_list.html |
| Cisco Unified CCX documentation | https://www.cisco.com/en/US/products/sw/custcosw/ps1846/tsd_products_support_series_home.html |
| Cisco Unified Intelligence Center documentation | https://www.cisco.com/en/US/products/ps9755/tsd_products_support_series_home.html |
| Cisco Finesse documentation | https://www.cisco.com/en/US/products/ps11324/tsd_products_support_series_home.html |
| Cisco Customer Collaboration Platform documentation Note From Unified CCX Release 12.5(1), CCP documents are available in the Cisco Unified CCX documentation folder. | Note | From Unified CCX Release 12.5(1), CCP documents are available in the Cisco Unified CCX documentation folder. | https://www.cisco.com/en/US/products/sw/custcosw/ps1846/tsd_products_support_series_home.html |
| Note | From Unified CCX Release 12.5(1), CCP documents are available in the Cisco Unified CCX documentation folder. |
| Cisco Unified CCX Virtualization Information | https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-contact-center-express.html |
| Cisco Unified CCX Compatibility Information | https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html |

| Note | From Unified CCX Release 12.5(1), CCP documents are available in the Cisco Unified CCX documentation folder. |
|---|---|