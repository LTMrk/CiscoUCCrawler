---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-maintain-and-operate-guide-uccx-ef2a348827
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/maintain_and_operate/guide/uccx_b_uccx-125admin-and-operations-guide/uccx_b_uccx-125admin-and-operations-guide_preface_011110.html
retrieved_at: 2026-08-16T21:42:14.458606+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)

Updated: January 31, 2020

Chapter: Preface

## Chapter: Preface

# Preface

## Change History

This table lists changes made to this guide. Most recent changes appear at the top.

Change

See

Date

Added note for saving agent competence level in the Contact Service Queues

Added details about using License Control

System Menu>License Management>Smart License Management

System Menu>License Management>Register with Cisco Smart Software Manager

July 2020

Introduced FIPS and added commands to use FIPS

Command Line Interface>Utils Commands>utils fips

Introduced Specific License Reservation Commands

Command Line Interface>Specific License Reservation Commands

Added Finesse failover mechanisms.

Cisco Finesse>>Cisco Finesse Administration Console >> Cisco Finesse Failover Mechanisms

June 2020

Added Content Security Policy details.

Command Line Interface>>Cisco Finesse Commands>>Supported Content Security Policy Directives

Updated Document for Release 12.5(1) SU1 EFT1

May 2020

Updated the option Enable Cisco Webex Experience Management post-call survey to enable Experience Management SMS/Email post-call survey.

Cisco Applications Configuration >> About Unified CCX Applications > > Add New Cisco Script Application

Added new DTMF desktop behaviour CLI.

Command Line Interface>>Cisco Finesse Commands>>Desktop Properties

Added new service property configuration CLI for port 5223.

Command Line Interface>>Cisco Finesse Commands>>Service Properties

Added Smart License Reservation Commands

Command Line Interface>>Smart License Reservation Commands

Command Line Interface>>Smart License Reservation Commands>>license smart reservation enable

Command Line Interface>>Smart License Reservation Commands>>license smart reservation request

Command Line Interface>>Smart License Reservation Commands>>license smart reservation install

Command Line Interface>>Smart License Reservation Commands>>license smart reservation return

Command Line Interface>>Smart License Reservation Commands>>license smart reservation return-authorization

Command Line Interface>>Smart License Reservation Commands>>license smart reservation cancel

Command Line Interface>>Smart License Reservation Commands>>license smart reservation disable

Initial Release of Document for Release 12.5(1)

January 2020

Cisco SocialMiner (SM) has been renamed as Customer Collaboration Platform (CCP).

Subsystems Menu>>Customer Collaboration Platform Configuration.

Subsystems Menu>>Delete Customer Collaboration Platform Configuration.

From this release, Context Service is not supported.

-

Added Cloud Connect server settings.

Added keyboard shortcuts.

Cisco Finesse>>Cisco Finesse Administration Console>>Manage System Settings>>Keyboard Shortcuts

Added edit call variables.

Added text and XML editors for Desktop Layout.

Added desktop property customization.

Cisco Finesse>>Cisco Finesse Administration Console>>Manage Desktop Layout>>Customize Desktop Properties

Changed the phone book limits.

Added text and XML editors for Team Resources.

Added desktop properties customization at team level.

Cisco Finesse>>Cisco Finesse Administration Console>>Manage Team Resources>>Assign Custom Desktop Layout to Team>>Customize
                                       Desktop Properties at Team Level

Added security enhancements.

Added Finesse IP Phone agent certificate management.

Cisco Finesse>>Cisco Finesse Administration Console>>Manage Finesse IP Phone Agent>>Finesse IP Phone Agent Certificate Management

Added new desktop property configuration CLIs.

Command Line Interface>>Cisco Finesse Commands>>Desktop Properties

Added new service property configuration CLIs.

Command Line Interface>>Cisco Finesse Commands>>Service Properties

Added a new section about recording a prompt.

Management of Prompts, Grammars, Documents, and Custom Files>>Upload of Prompt Files>>Record a Prompt

Added a new section for CORS.

Cisco Finesse>>Manage Security>>Cross-Origin Resource Sharing (CORS)

Added new commands for showing ASR and TTS sessions.

Command Line Interface>>Show commands>>show uccx asr sessions

Command Line Interface>>Show commands>>show uccx tts sessions

Added new sections about licensing, which details about Classic Licensing and Smart Licensing.

System Menu>>License Information

Introduced SRTP and added information about enabling SRTP.

Provision Unified CM for Unified CCX>>Unified Communications Manager for Unified CCX Configuration>>Guidelines for Agent Phone
                                       Configuration

System Menu>>System Parameters

MRCPv2 is now available for selection and the default port numbers for MRCP are updated.

System Menu>>System Parameters

Telephony and Media Provision>>ASR and TTS in Unified CCX>>Provision of MRCP ASR Subsystem>>Provision MRCP ASR Servers

Telephony and Media Provision>>ASR and TTS in Unified CCX>>MRCP TTS Subsystem>>Provision MRCP TTS Servers

Bubble chat can be launched on any device and the display adapts to the screen size of the device used.

Appendix C>>Bubble Chat Experience

Administrators can use the Unified CCX Health Check Utility to check the overall health of the Unified CCX system.

Appendix A>>Command Line Interface

Customer Collaboration Platform configuration can now be deleted using the Unified CCX Administration interface.

Subsystems Menu>>Delete Customer Collaboration Platform

Mange classic Licensing and Smart Licensing.

System Menu>>License Management

Cisco Smart Licensing helps to procure, deploy, and manage licenses easily, and report license consumption.

System Menu>>Smart Licensing

When secure RTP is enabled, the signaling channel (JTAPI) between Unified CCX and Unified CM is also secured and encrypted.

Provision Unified CM for Unified CCX>>Modify AXL Information

Only TLS 1.2 is supported.

Tools Menu>>Real-Time Reporting Tool

Command Line Interface>>show tls server min-version

Command Line Interface>>show tls client min-version

Command Line Interface>>set tls server min-version

Command Line Interface>>set tls client min-version

Introduced Webex Experience Management (WXM) Post-Call Survey.

Cisco Applications Configuration>>Add New Cisco Script Application

You can assign prompts to applications.

Tools Menu>>Assign Prompts

Introduced Docker Engine and Cisco Cloud Connect Container Manager.

Command Line Interface>>utils service

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
| Added note for saving agent competence level in the Contact Service Queues | Digital Channels > Task Flow to Enable Digital Channels > Contact Service Queues | 22 December 2022 |
| Added details about using License Control | System Menu>License Management>Smart License Management System Menu>License Management>Register with Cisco Smart Software Manager | July 2020 |
| Introduced FIPS and added commands to use FIPS | Command Line Interface>Utils Commands>utils fips |
| Introduced Specific License Reservation Commands | Command Line Interface>Specific License Reservation Commands |
| Added Finesse failover mechanisms. | Cisco Finesse>>Cisco Finesse Administration Console >> Cisco Finesse Failover Mechanisms | June 2020 |
| Added Content Security Policy details. | Command Line Interface>>Cisco Finesse Commands>>Supported Content Security Policy Directives |  |
| Updated Document for Release 12.5(1) SU1 EFT1 | May 2020 |
| Updated the option Enable Cisco Webex Experience Management post-call survey to enable Experience Management SMS/Email post-call survey. | Cisco Applications Configuration >> About Unified CCX Applications > > Add New Cisco Script Application |
| Added new DTMF desktop behaviour CLI. | Command Line Interface>>Cisco Finesse Commands>>Desktop Properties |
| Added new service property configuration CLI for port 5223. | Command Line Interface>>Cisco Finesse Commands>>Service Properties |
| Added Smart License Reservation Commands | Command Line Interface>>Smart License Reservation Commands Command Line Interface>>Smart License Reservation Commands>>license smart reservation enable Command Line Interface>>Smart License Reservation Commands>>license smart reservation request Command Line Interface>>Smart License Reservation Commands>>license smart reservation install Command Line Interface>>Smart License Reservation Commands>>license smart reservation return Command Line Interface>>Smart License Reservation Commands>>license smart reservation return-authorization Command Line Interface>>Smart License Reservation Commands>>license smart reservation cancel Command Line Interface>>Smart License Reservation Commands>>license smart reservation disable |
| Initial Release of Document for Release 12.5(1) | January 2020 |
| Cisco SocialMiner (SM) has been renamed as Customer Collaboration Platform (CCP). | Subsystems Menu>>Customer Collaboration Platform Configuration. Subsystems Menu>>Delete Customer Collaboration Platform Configuration. |
| From this release, Context Service is not supported. | - |
| Added Cloud Connect server settings. | Cisco Finesse>>Cisco Finesse Administration Console >> Manage System Settings>>Cloud Connect Server Settings |
| Added keyboard shortcuts. | Cisco Finesse>>Cisco Finesse Administration Console>>Manage System Settings>>Keyboard Shortcuts |
| Added edit call variables. | Cisco Finesse>>Cisco Finesse Administration Console>>Manage Call Variables Layouts>>Call Variables>>Edit Call Variables |
| Added text and XML editors for Desktop Layout. | Cisco Finesse>>Cisco Finesse Administration Console>>Manage Desktop Layout>>Finesse Desktop Layout XML |
| Added desktop property customization. | Cisco Finesse>>Cisco Finesse Administration Console>>Manage Desktop Layout>>Customize Desktop Properties |
| Changed the phone book limits. | Cisco Finesse>>Cisco Finesse Administration Console>>Manage Phone Books>>Phone Books and Contacts |
| Added text and XML editors for Team Resources. | Cisco Finesse>>Cisco Finesse Administration Console>>Manage Team Resources>>Assign Custom Desktop Layout to Team |
| Added desktop properties customization at team level. | Cisco Finesse>>Cisco Finesse Administration Console>>Manage Team Resources>>Assign Custom Desktop Layout to Team>>Customize
                                       Desktop Properties at Team Level |
| Added security enhancements. | Cisco Finesse>>Cisco Finesse Administration Console>>Manage Security>>Security Enhancements |
| Added Finesse IP Phone agent certificate management. | Cisco Finesse>>Cisco Finesse Administration Console>>Manage Finesse IP Phone Agent>>Finesse IP Phone Agent Certificate Management |
| Added new desktop property configuration CLIs. | Command Line Interface>>Cisco Finesse Commands>>Desktop Properties |  |
| Added new service property configuration CLIs. | Command Line Interface>>Cisco Finesse Commands>>Service Properties |  |
| Added a new section about recording a prompt. | Management of Prompts, Grammars, Documents, and Custom Files>>Upload of Prompt Files>>Record a Prompt |  |
| Added a new section for CORS. | Cisco Finesse>>Manage Security>>Cross-Origin Resource Sharing (CORS) |  |
| Added new commands for showing ASR and TTS sessions. | Command Line Interface>>Show commands>>show uccx asr sessions Command Line Interface>>Show commands>>show uccx tts sessions |  |
| Added new sections about licensing, which details about Classic Licensing and Smart Licensing. | System Menu>>License Information |  |
| Introduced SRTP and added information about enabling SRTP. | Provision Unified CM for Unified CCX>>Unified Communications Manager for Unified CCX Configuration>>Guidelines for Agent Phone
                                       Configuration System Menu>>System Parameters |  |
| MRCPv2 is now available for selection and the default port numbers for MRCP are updated. | System Menu>>System Parameters Telephony and Media Provision>>ASR and TTS in Unified CCX>>Provision of MRCP ASR Subsystem>>Provision MRCP ASR Servers Telephony and Media Provision>>ASR and TTS in Unified CCX>>MRCP TTS Subsystem>>Provision MRCP TTS Servers |  |
| Bubble chat can be launched on any device and the display adapts to the screen size of the device used. | Appendix C>>Bubble Chat Experience |  |
| Administrators can use the Unified CCX Health Check Utility to check the overall health of the Unified CCX system. | Appendix A>>Command Line Interface |  |
| Customer Collaboration Platform configuration can now be deleted using the Unified CCX Administration interface. | Subsystems Menu>>Delete Customer Collaboration Platform |  |
| Mange classic Licensing and Smart Licensing. | System Menu>>License Management |  |
| Cisco Smart Licensing helps to procure, deploy, and manage licenses easily, and report license consumption. | System Menu>>Smart Licensing |  |
| When secure RTP is enabled, the signaling channel (JTAPI) between Unified CCX and Unified CM is also secured and encrypted. | Provision Unified CM for Unified CCX>>Modify AXL Information |  |
| Only TLS 1.2 is supported. | Tools Menu>>Real-Time Reporting Tool Command Line Interface>>show tls server min-version Command Line Interface>>show tls client min-version Command Line Interface>>set tls server min-version Command Line Interface>>set tls client min-version |  |
| Introduced Webex Experience Management (WXM) Post-Call Survey. | Cisco Applications Configuration>>Add New Cisco Script Application |  |
| You can assign prompts to applications. | Tools Menu>>Assign Prompts |  |
| Introduced Docker Engine and Cisco Cloud Connect Container Manager. | Command Line Interface>>utils service |  |

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