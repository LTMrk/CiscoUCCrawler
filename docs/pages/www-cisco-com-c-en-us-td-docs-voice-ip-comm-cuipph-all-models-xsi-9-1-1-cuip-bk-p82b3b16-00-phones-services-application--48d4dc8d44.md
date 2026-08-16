---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-all-models-xsi-9-1-1-cuip-bk-p82b3b16-00-phones-services-application--48d4dc8d44
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/all_models/xsi/9-1-1/CUIP_BK_P82B3B16_00_phones-services-application-development-notes/CUIP_BK_P82B3B16_00_phones-services-application-development-notes_preface_00.html
retrieved_at: 2026-08-16T18:01:25.397520+00:00
---

Cisco Unified IP Phone Services Application Development Notes for Cisco Unified Communications Manager and Multiplatform Phones

# Cisco Unified IP Phone Services Application Development Notes for Cisco Unified Communications Manager and Multiplatform Phones

Updated: August 6, 2026

Chapter: Preface

## Chapter: Preface

# Preface

## Overview

You can use this document to develop and deploy customized client services for the phone that support Cisco Unified Phone
                           services.

Because of the complexity of a communications network, this guide does not provide complete and detailed information for procedures
                           that you need to perform in Cisco Unified Communications Manager, other third-party call control systems, or other network
                           devices.

In this document, the term call control system means Cisco Unified Communications Manager or third-party call control systems. The term phone means the Cisco IP Phones, Cisco Wireless Phones, Cisco IP Conference Phones, Cisco IP Phones with Multiplatform, Cisco Video
                           Phones, Cisco Desk Phones.

For information about how to use or administer the phones, see the appropriate phone user guide, phone administration guide,
                           and call control system documentation.

## Audience

This document provides the information needed for eXtensible Markup Language (XML) and X/Open System Interface (XSI) programmers
                           and system administrators to develop and deploy new services.

## Organization

This document contains the following sections:

Chapter

Description

Custom Client Services Overview

Provides an overview of the phone services for developers.

New and Changed Information

Provides details on the new and changed information in the XML service interface for the call control system.

CiscoIPPhone XML Objects

Describes the general behavior and usage of each XML object.

Component APIs

Describes additional application programming interfaces (API) available to the phones.

Internal URI Features

Describes how to implement embedded features on phones.

HTTP Requests and Header Settings

Provides a procedure on handling HTTP client requests, definitions for HTTP header elements, identifies the capabilities of
                                          the requesting IP phone client, and defines the Accept header.

Troubleshooting Cisco Unified IP Phone Service Applications

Provides troubleshooting tips, XML parsing errors, and error messages.

Cisco IP Phone Services Software Development Kit (SDK)

Provides a list of the components used in the Cisco Unified IP Services Software Development Kit (SDK) and the sample services
                                          requirements.

IP Phone Service Administration and Subscription

Describes how to add and administer Cisco Unified IP Phone Services through Cisco Unified Communications Manager Administration.

CiscoIPPhone XML Object Quick Reference

Provides a quick reference of the CiscoIPPhone XML objects and the definitions that are associated with each object.

Device Capability Query via CTI Feature

Provides information on the Device Capability Query via CTI feature.

## Related
                        	 Documentation

### Cisco Desk Phone 9800 Series Documentation

Find documentation specific to your language, phone model, and call control system on the product support page for the Cisco
                                 Desk Phone 9800 Series.

Get started with Cisco Desk Phone 9800 Series

Help articles for administrators and end-users

Cisco Desk Phone 9800 Series Support Page

### Cisco IP Phone 6800 Series Documentation

See the publications that are specific to your language, phone model, and multiplatform firmware release. Navigate from the
                                 following Uniform Resource Locator (URL):

https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-6800-series-multiplatform-firmware/tsd-products-support-series-home.html

### Cisco IP Phone 7800 Series Documentation

Find documentation specific to your language, phone model, and call control system on the product support page for the Cisco IP Phone 7800 Series.

### Cisco IP Conference Phone 7832 Documentation

Find documentation specific to your language, phone model, and call control system on the product support page for the Cisco IP Conference Phone 7832.

### Cisco IP Phone 8800 Series Documentation

Find documentation specific to your language, phone model, and call control system on the product support page for the Cisco IP Phone 8800 Series.

For help information about Cisco Video Phone 8875, see Cisco Video Phone 8875 .

### Cisco Wireless Phone 9821 Documentation

Find documentation that is specific to your call control system and language in the following links:

Product support page

Help documentation for users and administrators

Cisco Wireless Phone 9821 data sheet

### Cisco Wireless Phone 800 Series Documentation

Find documentation that is specific to your phone model, call control system, and language on the product support page for
                                 the Cisco Wireless Phone 840 and 860 . From these pages, you can also find the Cisco Wireless Phone 840 and 860 Deployment Guide .

### Cisco Wireless IP Phone 882x Series Documentation

Find documentation that is specific to your phone model, call control system, and language on the product support page for
                                 the Cisco Wireless IP Phone 8821 and Cisco Wireless IP Phone 8821-EX . From these pages, you can also find the Cisco Wireless IP Phone 8821 and 8821-EX Wireless LAN Deployment Guide and Cisco Wireless IP Phone 8821 and 8821-EX Solution Compatibility Matrix .

### Cisco Unified IP Conference Phone 8831 Documentation

Refer to
                                 		  publications that are specific to your language, phone model, and call control
                                 		  system. Navigate from the following documentation URL:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/tsd-products-support-series-home.html

### Cisco IP Conference Phone 8832 Documentation

Find documentation specific to your language, phone model, and call control system on the product support page for the Cisco IP Conference Phone 8832.

## Guide Conventions

This document uses the following conventions:

Convention

Description

boldface font

Commands and keywords are in boldface .

italic font

Arguments for which you supply values are in italics .

[   ]

Elements in square brackets are optional.

{x | y | z}

Alternative keywords are grouped in braces and separated by
                                          						vertical bars.

[x | y | z]

Optional alternative keywords are grouped in brackets and
                                          						separated by vertical bars.

string

A nonquoted set of characters. Do not use quotation marks
                                          						around the string or the string will include the quotation marks.

screen font

Terminal sessions and information the system displays are in screen font.

input font

Information you must enter is in input font.

italic screen font

Arguments for which you supply values are in italic screen font.

^

The symbol ^ represents the key labeled Control - for
                                          						example, the key combination ^D in a screen display means hold down the Control
                                          						key while you press the D key.

<  >

Nonprinting characters such as passwords are in angle
                                          						brackets.

Means reader take note . Notes contain helpful suggestions or
                                          			 references to material not covered in the publication.

Caution

Means reader be careful . In this situation, you might do something
                                          			 that could result in equipment damage or loss of data.

Warnings use the following convention:

Attention

IMPORTANT SAFETY INSTRUCTIONS

This warning symbol means
                                          				  danger. You are in a situation that could cause bodily injury. Before you work
                                          				  on any equipment, be aware of the hazards involved with electrical circuitry
                                          				  and be familiar with standard practices for preventing accidents. Use the
                                          				  statement number provided at the end of each warning to locate its translation
                                          				  in the translated safety warnings that accompanied this device. Statement 1071

SAVE THESE INSTRUCTIONS

## Cisco DevNet, Cisco TAC, and Cisco Solutions Partner Program

The Cisco DevNet portal provides access to API documentation, learning, tools, and communities across multiple Cisco product
                           technology areas, enabling developers, customers, and partners to accelerate development of applications and integrated solutions.
                           Free help options include knowledge bases, Webex chat, and community forums.

Cisco DevNet: https://developer.cisco.com

For break or fix service-level agreement production support of Cisco APIs, contact the Cisco Technical Assistance Center (TAC).

Cisco TAC: https://www.cisco.com/c/en/us/support/index.html

The Cisco Solutions Partner Program (SPP) is designed for businesses (IHVs and ISVs) interested in going to market with Cisco.
                           The SPP enables members to develop compelling solutions that unify data, voice, video, and more on Cisco's powerful network
                           platforms. The program also allows members to take advantage of Cisco's brand, market leadership position, and installed base
                           to help drive positive business results for themselves and their customers.

Cisco Solutions Partner Program: https://www.cisco.com/c/en/us/partners/partner-with-cisco/solution-partner-program-spp.html

## Cisco Product Security Overview

This product contains cryptographic features and is subject to
                           		United States and local country laws governing import, export, transfer, and
                           		use. Delivery of Cisco cryptographic products does not imply third-party
                           		authority to import, export, distribute, or use encryption. Importers,
                           		exporters, distributors, and users are responsible for compliance with U.S. and
                           		local country laws. By using this product you agree to comply with applicable
                           		laws and regulations. If you are unable to comply with U.S. and local laws,
                           		return this product immediately.

Further information regarding U.S. export regulations may be
                           		found at http://www.bis.doc.gov/index.php/regulations/export-administration-regulations-ear .

| Chapter | Description |
|---|---|
| Custom Client Services Overview | Provides an overview of the phone services for developers. |
| New and Changed Information | Provides details on the new and changed information in the XML service interface for the call control system. |
| CiscoIPPhone XML Objects | Describes the general behavior and usage of each XML object. |
| Component APIs | Describes additional application programming interfaces (API) available to the phones. |
| Internal URI Features | Describes how to implement embedded features on phones. |
| HTTP Requests and Header Settings | Provides a procedure on handling HTTP client requests, definitions for HTTP header elements, identifies the capabilities of
                                          the requesting IP phone client, and defines the Accept header. |
| Troubleshooting Cisco Unified IP Phone Service Applications | Provides troubleshooting tips, XML parsing errors, and error messages. |
| Cisco IP Phone Services Software Development Kit (SDK) | Provides a list of the components used in the Cisco Unified IP Services Software Development Kit (SDK) and the sample services
                                          requirements. |
| IP Phone Service Administration and Subscription | Describes how to add and administer Cisco Unified IP Phone Services through Cisco Unified Communications Manager Administration. |
| CiscoIPPhone XML Object Quick Reference | Provides a quick reference of the CiscoIPPhone XML objects and the definitions that are associated with each object. |
| Device Capability Query via CTI Feature | Provides information on the Device Capability Query via CTI feature. |

| Convention | Description |
|---|---|
| boldface font | Commands and keywords are in boldface . |
| italic font | Arguments for which you supply values are in italics . |
| [   ] | Elements in square brackets are optional. |
| {x \| y \| z} | Alternative keywords are grouped in braces and separated by
                                          						vertical bars. |
| [x \| y \| z] | Optional alternative keywords are grouped in brackets and
                                          						separated by vertical bars. |
| string | A nonquoted set of characters. Do not use quotation marks
                                          						around the string or the string will include the quotation marks. |
| screen font | Terminal sessions and information the system displays are in screen font. |
| input font | Information you must enter is in input font. |
| italic screen font | Arguments for which you supply values are in italic screen font. |
| ^ | The symbol ^ represents the key labeled Control - for
                                          						example, the key combination ^D in a screen display means hold down the Control
                                          						key while you press the D key. |
| <  > | Nonprinting characters such as passwords are in angle
                                          						brackets. |

| Note | Means reader take note . Notes contain helpful suggestions or
                                          			 references to material not covered in the publication. |
|---|---|

| Caution | Means reader be careful . In this situation, you might do something
                                          			 that could result in equipment damage or loss of data. |
|---|---|

| Attention | IMPORTANT SAFETY INSTRUCTIONS This warning symbol means
                                          				  danger. You are in a situation that could cause bodily injury. Before you work
                                          				  on any equipment, be aware of the hazards involved with electrical circuitry
                                          				  and be familiar with standard practices for preventing accidents. Use the
                                          				  statement number provided at the end of each warning to locate its translation
                                          				  in the translated safety warnings that accompanied this device. Statement 1071 SAVE THESE INSTRUCTIONS |
|---|---|