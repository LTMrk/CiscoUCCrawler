---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su1-reference-guide-uccx-b-12-bd9de25913
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su1/reference/guide/uccx_b_1251su1db-schema-guide/uccx_b_1252schema-guide_preface_00.html
retrieved_at: 2026-08-16T21:03:42.813874+00:00
---

Cisco Unified Contact Center Express Database Schema Guide, Release 12.5(1) SU1

# Cisco Unified Contact Center Express Database Schema Guide, Release 12.5(1) SU1

Find Matches in This Book

## Results

Updated: January 31, 2021

Chapter: Preface

## Chapter: Preface

# Preface

## Change History

This table lists changes made to this guide. Most recent changes appear at the top.

Change

See

Date

A new field acdbusyonnonacdbusy is included in the Team table.

Database Schema>Database Table Details>Team

July 2021

A new field nonacdbusyoverride is included in the Team table.

Database Schema>Database Table Details>Team

A new field autoanswer is included in the Team table

Database Schema>Database Table Details>Team

January 2021

The storage size of the resourceLoginID and reskiller fields are updated to 128

Database Schema>Database Table Details>AuditReskill

Database Schema>Database Table Details>AuditResidualSkills

Database Schema>Database Table Details>Resource

Database Schema>Database Table Details>RmonResConfig

Database Schema>Database Table Details>RmonUser

Database Schema>Database Table Details>Schedule Reskill

Database Schema>Database Table Details>Supervisor

Database Schema>Database Table Details>SupervisorCampaignMap

Database Schema>Database Table Details>SupervisorApplicationMap

Added two new fields emailAuthType and emailOAuthDetails

Database Schema>Database Table Details>ContactServiceQueue

Added a point about SMS/Email survey

Database Schema>Database Table Details>ContactCallDetail

Added new fields surveyname and dispatchid

Database Schema>Database Table Details>CrsApplication

Added the new field usehttpproxy

Database Schema>Database Table Details>ChannelProvider

Removed the fields wdcode and wdcontextservicefieldsets

Database Schema>Database Table Details>ChatWidget

## About This
                        	 Guide

The Cisco Unified CCX Database Schema Guide for Cisco Unified
                           		Contact Center Express (Unified CCX) describes how data is organized in the
                           		Unified CCX Databases. This document provides detailed description of the
                           		records and fields in each database table and enables you to create your own
                           		reports.

## Audience

This manual is intended for system managers, administrators, and
                           		developers who want to create custom reports using the generally available
                           		third-party programs that create reports from databases.

## Organization

The Database Table Details describes
                           		each table in the Cisco Unified CCX database. The descriptions are arranged in
                           		the alphabetical order by table name. Each description includes a detailed
                           		explanation of each record in the table. The Index helps you find information
                           		in this book.

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

Cisco Mediasense documentation

https://www.cisco.com/c/en/us/support/customer-collaboration/mediasense/tsd-products-support-series-home.html

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
| A new field acdbusyonnonacdbusy is included in the Team table. | Database Schema>Database Table Details>Team | July 2021 |
| A new field nonacdbusyoverride is included in the Team table. | Database Schema>Database Table Details>Team |
| Initial Release of Document for Release 12.5(1) SU1 |
| A new field autoanswer is included in the Team table | Database Schema>Database Table Details>Team | January 2021 |
| The storage size of the resourceLoginID and reskiller fields are updated to 128 | Database Schema>Database Table Details>AuditReskill Database Schema>Database Table Details>AuditResidualSkills Database Schema>Database Table Details>Resource Database Schema>Database Table Details>RmonResConfig Database Schema>Database Table Details>RmonUser Database Schema>Database Table Details>Schedule Reskill Database Schema>Database Table Details>Supervisor Database Schema>Database Table Details>SupervisorCampaignMap Database Schema>Database Table Details>SupervisorApplicationMap |
| Added two new fields emailAuthType and emailOAuthDetails | Database Schema>Database Table Details>ContactServiceQueue |
| Added a point about SMS/Email survey | Database Schema>Database Table Details>ContactCallDetail |
| Added new fields surveyname and dispatchid | Database Schema>Database Table Details>CrsApplication |
| Added the new field usehttpproxy | Database Schema>Database Table Details>ChannelProvider |
| Removed the fields wdcode and wdcontextservicefieldsets | Database Schema>Database Table Details>ChatWidget |

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
| Cisco Mediasense documentation | https://www.cisco.com/c/en/us/support/customer-collaboration/mediasense/tsd-products-support-series-home.html |
| Cisco Unified CCX Virtualization Information | https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-contact-center-express.html |
| Cisco Unified CCX Compatibility Information | https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html |

| Note | From Unified CCX Release 12.5(1), CCP documents are available in the Cisco Unified CCX documentation folder. |
|---|---|