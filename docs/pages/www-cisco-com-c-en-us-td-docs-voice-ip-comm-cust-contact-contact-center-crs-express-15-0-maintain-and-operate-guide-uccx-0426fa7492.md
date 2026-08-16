---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-15-0-maintain-and-operate-guide-uccx-0426fa7492
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_15_0/maintain_and_operate/guide/uccx_b_1501_admin-and-operations-guide/uccx_m_1501_preface.html
retrieved_at: 2026-08-16T21:27:05.443475+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 15.0

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 15.0

Updated: April 30, 2025

Chapter: Preface

## Chapter: Preface

# Preface

## Change History

This table lists the changes made to this guide. The most recent changes appear at the top.

Change

See

Date

Removed Cloud Connect

System Menu

April, 2025

Cisco Finesse

Unified CCX System Management > Unified CCX IP Address/hostname Management > IP Address Modification > Change IP Address for
                                          Server in Single-Node Deployment

Command Line Interface > Utils Commands > utils service

Removed Cisco Webex Experience Management

Cisco Applications Configuration > About Unified CCX Applications > Add New Cisco Script Application

VPN-less Access to Finesse Desktop > Reverse-Proxy selection and configurations > Determine Gadget Compatibility

Added Trigger OVA migration command topic. This topic has the following CLIs:

utils uccx ova info

utils uccx ova migrate

Backup and Restore

Added a new CLI utils uccx database reindex tablename .

Command Line Interface > Utils Commands

Removed the Change Licensing Packages topic.

Unified CCX Provision Checklist

Removed Upload Licensing topic.

Unified CCX Introduction > Set Up Unified CCX > View License Information

Updated the examples for 15.0.

Command Line Interface > Specific License Reservation Commands > license smart reservation install

Removed the content related to Perpetual License.

Unified CCX Provision Checklist > Provision Unified CCX

Provision of Unified CCX > Contact Service Queue Configuration > Create a Contact Service Queue > Contact Service Queue Configuration
                                          Web Page

Provision of Unified CCX > Configure Agent-Based Routing

Unified CCX Outbound Dialer Configuration > Outbound Feature for Unified CCX > Unified CCX Requirements

Command Line Interface > Cisco Finesse Commands > utils uccx finesse

Unified CCX Introduction > Set Up Unified CCX > View License Information

Command Line Interface > Specific License Reservation Commands > license smart reservation request

Unified CCX Introduction > Unified CCX Product Family > Unified Contact Center Express

Subsystems Menu > RmCm Menu

Unified CCX License Packages

Backup and Restore > Restore Scenarios > Restore SA Setup (with Rebuild)

Backup and Restore > Restore Scenarios > Restore Only First Node in HA Setup (with Rebuild)

Backup and Restore > Restore Scenarios > Restore Both Nodes in HA Setup (with Rebuild)

Unified CCX License Packages > Application Availability by License Package

Unified CCX License Packages > Trigger Availability by License Package

Unified CCX License Packages > Subsystem Availability by License Package

Unified CCX License Packages > Unified CCX Services Availability by License Package

Unified CCX License Packages > Unified CCX Component Availability by License Package

Removed content relatated to License Management and Classic License Management.

System Menu > License Information > License Management

Removed NFR, Perpetual Enhanced, and Perpetual Premium.

System Menu > License Information > License Management > Smart Licensing

Removed the topic Classic License Management .

System Menu > License Information > License Management

Removed content related Perpetual License.

Introduction > Set Up Unified CCX > View License Information > Enable Smart Licensing

Removed the utils uccx delete license licenseName topic.

Command Line Interface > Utils Commands

Removed the utils uccx list license topic.

Command Line Interface > Utils Commands

Removed the show uccx license topic.

Command Line Interface > Show Commands

Added information about switch back from Unifed CCX 15.0 to previous releases.

Backup and Restore > Important Considerations

Added the topic Cipher Management .

Backup and Restore > SFTP Requirements

Added the following CLIs

utils system tls_ciphers config list

utils system tls_ciphers config export

utils system tls_ciphers config import

utils system tls_ciphers config reset

Utils Commands

Updated the connection method to Cisco SSM.

Introduction > Setup Unified CCX > View License Information > Configure transport settings for smart licensing

Added a new field Secure Connection .

Updated the second bullet in description of JDBC URL to mention that the encryption is supported.

Provision of Additional Subsystems > Provision of Database Subsystem > Add New Datasource > Datasource Configuration Web Page

Updated the Note to mention that the encrytion is supported.

Tools Menu > Real-Time Snapshot Config Menu > Create System DSN for Wallboard

Added the topic utils uccx informix_ssl status .

Command Line Interface > Utils Commands

Added the topic utils uccx informix_ssl cert generate .

Command Line Interface > Utils Commands

Added the topic utils uccx informix_ssl cert info .

Command Line Interface > Utils Commands

Added the topic utils uccx informix_ssl enable .

Command Line Interface > Utils Commands

Added the topic utils uccx informix_ssl disable .

Command Line Interface > Utils Commands

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
| Removed Cloud Connect | System Menu | April, 2025 |
| Cisco Finesse |
| Unified CCX System Management > Unified CCX IP Address/hostname Management > IP Address Modification > Change IP Address for
                                          Server in Single-Node Deployment |
| Command Line Interface > Utils Commands > utils service |
| Removed Cisco Webex Experience Management | Cisco Applications Configuration > About Unified CCX Applications > Add New Cisco Script Application |
| VPN-less Access to Finesse Desktop > Reverse-Proxy selection and configurations > Determine Gadget Compatibility |
| Added Trigger OVA migration command topic. This topic has the following CLIs: utils uccx ova info utils uccx ova migrate | Backup and Restore |
| Added a new CLI utils uccx database reindex tablename . | Command Line Interface > Utils Commands |
| Removed the Change Licensing Packages topic. | Unified CCX Provision Checklist |
| Removed Upload Licensing topic. | Unified CCX Introduction > Set Up Unified CCX > View License Information |
| Updated the examples for 15.0. | Command Line Interface > Specific License Reservation Commands > license smart reservation install |
| Removed the content related to Perpetual License. | Unified CCX Provision Checklist > Provision Unified CCX |
| Provision of Unified CCX > Contact Service Queue Configuration > Create a Contact Service Queue > Contact Service Queue Configuration
                                          Web Page |
| Provision of Unified CCX > Configure Agent-Based Routing |
| Unified CCX Outbound Dialer Configuration > Outbound Feature for Unified CCX > Unified CCX Requirements |
| Command Line Interface > Cisco Finesse Commands > utils uccx finesse |
| Unified CCX Introduction > Set Up Unified CCX > View License Information |
| Command Line Interface > Specific License Reservation Commands > license smart reservation request |
| Unified CCX Introduction > Unified CCX Product Family > Unified Contact Center Express |
| Subsystems Menu > RmCm Menu |
| Unified CCX License Packages |
| Backup and Restore > Restore Scenarios > Restore SA Setup (with Rebuild) |
| Backup and Restore > Restore Scenarios > Restore Only First Node in HA Setup (with Rebuild) |
| Backup and Restore > Restore Scenarios > Restore Both Nodes in HA Setup (with Rebuild) |
| Unified CCX License Packages > Application Availability by License Package |
| Unified CCX License Packages > Trigger Availability by License Package |
| Unified CCX License Packages > Subsystem Availability by License Package |
| Unified CCX License Packages > Unified CCX Services Availability by License Package |
| Unified CCX License Packages > Unified CCX Component Availability by License Package |
| Removed content relatated to License Management and Classic License Management. | System Menu > License Information > License Management |
| Removed NFR, Perpetual Enhanced, and Perpetual Premium. | System Menu > License Information > License Management > Smart Licensing |
| Removed the topic Classic License Management . | System Menu > License Information > License Management |
| Removed content related Perpetual License. | Introduction > Set Up Unified CCX > View License Information > Enable Smart Licensing |
| Removed the utils uccx delete license licenseName topic. | Command Line Interface > Utils Commands |
| Removed the utils uccx list license topic. | Command Line Interface > Utils Commands |
| Removed the show uccx license topic. | Command Line Interface > Show Commands |
| Added information about switch back from Unifed CCX 15.0 to previous releases. | Backup and Restore > Important Considerations |
| Added the topic Cipher Management . | Backup and Restore > SFTP Requirements |
| Added the following CLIs utils system tls_ciphers config list utils system tls_ciphers config export utils system tls_ciphers config import utils system tls_ciphers config reset | Utils Commands |
| Updated the connection method to Cisco SSM. | Introduction > Setup Unified CCX > View License Information > Configure transport settings for smart licensing |
| Added a new field Secure Connection . Updated the second bullet in description of JDBC URL to mention that the encryption is supported. | Provision of Additional Subsystems > Provision of Database Subsystem > Add New Datasource > Datasource Configuration Web Page |
| Updated the Note to mention that the encrytion is supported. | Tools Menu > Real-Time Snapshot Config Menu > Create System DSN for Wallboard |
| Added the topic utils uccx informix_ssl status . | Command Line Interface > Utils Commands |
| Added the topic utils uccx informix_ssl cert generate . | Command Line Interface > Utils Commands |
| Added the topic utils uccx informix_ssl cert info . | Command Line Interface > Utils Commands |
| Added the topic utils uccx informix_ssl enable . | Command Line Interface > Utils Commands |
| Added the topic utils uccx informix_ssl disable . | Command Line Interface > Utils Commands |

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