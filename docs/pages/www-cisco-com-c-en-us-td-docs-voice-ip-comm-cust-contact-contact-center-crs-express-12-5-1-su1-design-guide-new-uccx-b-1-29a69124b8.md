---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su1-design-guide-new-uccx-b-1-29a69124b8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su1/design/guide_new/uccx_b_1251su1solution-design-gude/uccx_b_1252solution-design-gude_preface_00.html
retrieved_at: 2026-08-16T21:07:42.987843+00:00
---

Solution Design Guide for Cisco Unified Contact Center Express, Release 12.5(1) SU1

# Solution Design Guide for Cisco Unified Contact Center Express, Release 12.5(1) SU1

Updated: January 31, 2021

Chapter: Preface

## Chapter: Preface

# Preface

## Change History

Change

See

Date

Initial Release of Document for Release 12.5(1) SU1

January 2021

Changed Cisco WFO to Webex WFO and Advanced Quality Management to Quality Management

Contact Center Express Solutions Overview>Unified CCX Licensing

Contact Center Express Solutions Overview>Features>Webex Quality Management and Compliance Recording

Contact Center Express Solutions Overview>Features>Agent Interfaces>Cisco Finesse Agent Desktop Features

Contact Center Express Solutions Overview>Features>Inbound Voice

Contact Center Express Solutions Overview>Features>Unified CCX Outbound Dialer>Direct Preview Outbound

Contact Center Express Solutions Overview>Features>Recording

Contact Center Express Solutions Overview>Features>Webex Quality Management and Compliance Recording

CiscoWebex Experience Management

Added info about secure JTAPI connection between CUCM and Unified CM
                                       Telephony and RmCm

Solution Security>Secure Real-Time Protocol (Secure RTP or SRTP)

Added Agent Device Selection

Contact Center Express Solutions Overview > Features > Agent Device
                                       Selection

## About This
                        	 Guide

This guide provides design considerations and guidelines for deploying
                           		Cisco Unified Contact Center Express (Unified CCX). This guide assumes that you
                           		are familiar with basic contact center terms and concepts.

## Audience

This guide is primarily for contact center designers and system
                           		administrators.

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
| Initial Release of Document for Release 12.5(1) SU1 | January 2021 |
| Changed Cisco WFO to Webex WFO and Advanced Quality Management to Quality Management | Contact Center Express Solutions Overview>Unified CCX Licensing Contact Center Express Solutions Overview>Features>Webex Quality Management and Compliance Recording Contact Center Express Solutions Overview>Features>Agent Interfaces>Cisco Finesse Agent Desktop Features Contact Center Express Solutions Overview>Features>Inbound Voice Contact Center Express Solutions Overview>Features>Unified CCX Outbound Dialer>Direct Preview Outbound Contact Center Express Solutions Overview>Features>Recording Contact Center Express Solutions Overview>Features>Webex Quality Management and Compliance Recording CiscoWebex Experience Management |
| Added info about secure JTAPI connection between CUCM and Unified CM
                                       Telephony and RmCm | Solution Security>Secure Real-Time Protocol (Secure RTP or SRTP) |
| Added Agent Device Selection | Contact Center Express Solutions Overview > Features > Agent Device
                                       Selection |

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