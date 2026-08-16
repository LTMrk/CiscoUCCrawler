---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-user-ucce-b-2689eb0c43
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/user/ucce_b_1262_outbound_options_guide/ucce_m_1262_preface.html
retrieved_at: 2026-08-16T20:32:26.970982+00:00
---

Outbound Option Guide for Unified Contact Center Enterprise, Release 12.6(2)

# Outbound Option Guide for Unified Contact Center Enterprise, Release 12.6(2)

Updated: August 19, 2025

Chapter: Preface

## Chapter: Preface

# Preface

## Change History

This table lists changes made to this guide. The most recent changes appear at the top.

Date

Release of Document for 12.6(1) ES65

Enable or disable outbound Dialer from redialing or retrying failed personal callbacks.

Dialer registry settings table in Registry Settings chapter

July 2023

Initial Release of Document for Release 12.6(1)

May 2021

Graceful Shutdown feature is introduced

Graceful Shutdown

## About This
                        	 Guide

This manual provides
                           		conceptual, installation, and configuration information about the Cisco Unified
                           		Contact Center Enterprise (Unified CCE) Outbound Option application (formerly
                           		called "Blended
                              		  Agent" ). It also provides verification checklists and troubleshooting
                           		information to ensure that the Outbound Option installation and configuration
                           		setup is successful.

For detailed
                           		Outbound Option Components field descriptions, see the online help.

## Audience

This document is intended for contact center supervisors and contact
                           		center technology experts who perform the following functions using
                           		Outbound Option:

System Administrators – The installer/partner who sets up the Unified CCE system to support Outbound Option and  installs and integrates the Outbound
                                 Option components.

Administrator – The administrator responsible for
                                 			 configuration tasks, such as adding agents, skill groups, campaigns, and
                                 			 scripts necessary for ongoing activity.

Supervisors/Business users – These users might perform such tasks as modifying a query rule, adjusting the lines per agent, or
                                 			 enabling or disabling a campaign. This group of users also read
                                 			 and interpret reports to help them run their business.

Sales – A secondary audience, interested primarily in
                                 			 conceptual information.

## Related Documents

For documentation for these Cisco Unified Contact Center Products, go to https://www.cisco.com/cisco/web/psa/default.html , select Voice and Unified Communications > CustomCisco Unified Contact Center Productser Collaboration > Cisco Unified Contact Center Products or Cisco Unified Voice Self-Service Products , and select the product/option in which you are interested.

Related documentation includes the documentation sets for:

Cisco CTI Object Server (CTI OS)

Cisco
                                 Unified Contact Center Management Portal

Cisco Unified Customer Voice Portal (CVP)

Cisco
                                 Unified IP IVR

Cisco Unified Intelligence Center

Cisco Finesse

Cisco Agent Desktop (CAD)

Documentation for Unified CM is also accessible through https://www.cisco.com/cisco/web/psa/default.html .

Technical Support documentation and tools are accessible from: https://www.cisco.com/en/US/support/index.html .

The Product Alert tool is accessible from (sign in required): https://www.cisco.com/cgi-bin/Support/FieldNoticeTool/field-notice .

## Communications, Services, and Additional Information

To receive timely, relevant information from Cisco, sign up at Cisco Profile Manager .

To get the business results you’re looking for with the technologies that matter, visit Cisco Services .

To submit a service request, visit Cisco Support .

To discover and browse secure, validated enterprise-class apps, products, solutions and services, visit Cisco DevNet .

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
| Release of Document for 12.6(1) ES65 Enable or disable outbound Dialer from redialing or retrying failed personal callbacks. | Dialer registry settings table in Registry Settings chapter | July 2023 |
| Initial Release of Document for Release 12.6(1) | May 2021 |
| Graceful Shutdown feature is introduced | Graceful Shutdown |

| Note | Successfully completing the Outbound Option installation also requires use of the Staging Guide for Cisco Unified ICM/Contact Center Enterprise . See https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/tsd-products-support-series-home.html for the complete set of Cisco Unified ICM/ Contact Center Enterprise and Hosted software manuals. |
|---|---|

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