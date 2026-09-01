---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-mib-reference-guide-srst34-srst34mb-srstpref-html-2ed4d8e29b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/mib/reference/guide/srst34/srst34mb/SRSTPref.html
retrieved_at: 2026-09-01T21:28:29.448509+00:00
---

Cisco SRST SNMP MIB Release 3.4 Guide

# Cisco SRST SNMP MIB Release 3.4 Guide

Book Contents

- Book Title Page

- Preface

- Cisco SRST SNMP MIB Support

Find Matches in This Book

## Results

Updated: November 4, 2005

Chapter: Preface

## Chapter: Preface

# Preface

## About this Preface

This preface describes the objectives, audience, organization, and conventions of this document, and explains how to find additional information on related products and services. It contains the following sections :

• Document Objective

• Audience

• Document Organization

• Obtaining Technical Assistance

• Document Conventions

• Syntax Conventions

• Obtaining Documentation

• Cisco Product Security Overview

• Obtaining Technical Assistance

• Obtaining Additional Publications and Information

• Summary History of Document Changes

## Document Objective

This document describes the information regarding the Cisco SRST Simple Network Management Protocol (SNMP) Management Information Base (MIB). The document contains tables for you to use when using the SNMP MIB to monitor your system.

## Audience

The primary audience for this document is network operators and administrators who have experience in the following areas:

• Telecommunications network operations

• Data network operations

• SNMP operstion

• MIB syntax

• Telecommunications hardware

• Data network hardware

In addition, the following audiences may find this document useful:

• Software and hardware installers

• Network designers

## Document Organization

This document contains the chapters listed in Table 1 .

Table 1 Document Organization

Chapter 1

Provisioning Overview

This chapter includes a description of the Cisco SRST MIB.

## Document Conventions

Note Means reader take note . Notes contain helpful suggestions or references to materials not contained in this manual.

Tip Means the following information might help you solve a problem .

Timesaver Means the described action saves time . You can save time by performing the action described in the paragraph.

## Syntax Conventions

Conventions used throughout this guide are shown in Table 2 .

Table 2 Conventions

Boldface

Commands and keywords you enter as shown.

offset-list

Italics

Variables for which you supply values.

command type interface

You replace the variable with the type of interface.

In contexts that do not allow italics, such as online help, arguments are enclosed in angle brackets (< >).

Square brackets ([ ])

Optional elements.

command [abc]

abc is optional (not required), but you can choose it.

Vertical bars ( | )

Separated alternative elements.

command [ abc | def ]

You can choose either abc or def, or neither, but not both.

Braces ({ })

Required choices.

command { abc | def }

You must choose either abc or def, but not both.

Braces and vertical bars within square brackets ([ { | } ])

A required choice within an optional element.

command [ abc { def | ghi } ]

You have three options:

nothing

abc def

abc ghi

Caret character (^)

Control key.

The key combinations ^D and Ctrl-D are equivalent: Both mean "hold down the Control key while you press the D key." Keys are indicated in capital letters, but are not case sensitive.

A nonquoted set of characters

A string.

For example, when setting an SNMP community string to public , do not use quotation marks around the string; otherwise, the string will include the quotation marks.

System prompts

Denotes interactive sessions, indicates that the user enters commands at the prompt.

The system prompt indicates the current command mode. For example, the prompt Router (config) # indicates global configuration mode.

Screen font

Terminal sessions and information the system displays.

Angle brackets (< >)

Nonprinting characters such as passwords.

Exclamation point (!) at the beginning of a line

A comment line.

Comments are sometimes displayed by the Cisco IOS software.

Conventions used in the Cisco SRST system (such as in CLI commands) are shown in Table 3 .

Table 3 Data Types

Integer

A series of decimal digits from the set of 0 through 9 that represents a positive integer. An integer may have one or more leading zero digits (0) added to the left side to align the columns. Leading zeros are always valid as long as the number of digits is less than or equal to ten digits. Values of this type have a range of zero through 4294967295.

```
123
```

```
000123
```

```
4200000000
```

Signed integer

This data type has the same basic format as the integer but can be either positive or negative. When negative, it is preceded by the sign character (-). As with the integer data type, this data type can be as many as ten digits in length, not including the sign character. The value of this type has a range of 0 minus 2147483647 through 2147483647.

```
123
```

```
-000123
```

```
-2100000000l
```

Hexadecimal

A series of 16-based digits from the set of 0 through 9, a through f, or A through F. The hexadecimal number may have one or more leading zeros (0) added to the left side. For all hexadecimal values, the maximum size is 0xffffffff (eight hexadecimal digits).

```
1f3
```

```
01f3000
```

Text

A series of alphanumeric characters from the ASCII character set, where defined. Tab, space, and double quote ( " " ) characters cannot be used. Text can be as many as 255 characters; however, it is recommended that you limit the text to no more than 32 characters for readability.

```
EntityID
```

```
LineSES_Threshold999
```

String

A series of alphanumeric characters and white-space characters. A string is surrounded by double quotes ( " " ). Strings can be as many as 255 characters; however, it is recommended that you limit the strings to no more than 80 characters for readability.

```
"This is a descriptive 
string."
```

Note Hexadecimal and integer fields in files may have different widths (number of characters) for column alignment.

## Obtaining Documentation

Cisco documentation and additional literature are available on Cisco.com. Cisco also provides several ways to obtain technical assistance and other technical resources. These sections explain how to obtain technical information from Cisco Systems.

### Cisco.com

You can access the most current Cisco documentation at this URL:

http://www.cisco.com/cisco/web/psa/default.html?mode=prod

You can access the Cisco website at this URL:

http://www.cisco.com

You can access international Cisco websites at this URL:

http://www.cisco.com/public/countries_languages.shtml

### Documentation DVD

Cisco documentation and additional literature are available in a Documentation DVD package, which may have shipped with your product. The Documentation DVD is updated regularly and may be more current than printed documentation. The Documentation DVD package is available as a single unit.

Registered Cisco.com users (Cisco direct customers) can order a Cisco Documentation DVD (product number DOC-DOCDVD=) from the Ordering tool or Cisco Marketplace.

Cisco Ordering tool:

http://www.cisco.com/en/US/partner/ordering/

Cisco Marketplace:

http://www.cisco.com/go/marketplace/

### Ordering Documentation

You can find instructions for ordering documentation at this URL:

http://www.cisco.com/univercd/cc/td/doc/es_inpck/pdi.htm

You can order Cisco documentation in these ways:

• Registered Cisco.com users (Cisco direct customers) can order Cisco product documentation from the Ordering tool:

http://www.cisco.com/en/US/partner/ordering/

• Nonregistered Cisco.com users can order documentation through a local account representative by calling Cisco Systems Corporate Headquarters (California, USA) at 408 526-7208 or, elsewhere in North America, by calling 1 800 553-NETS (6387).

## Documentation Feedback

You can send comments about technical documentation to bug-doc@cisco.com.

You can submit comments by using the response card (if present) behind the front cover of your document or by writing to the following address:

Cisco Systems Attn: Customer Document Ordering 170 West Tasman Drive San Jose, CA 95134-9883

We appreciate your comments.

## Cisco Product Security Overview

Cisco provides a free online Security Vulnerability Policy portal at this URL:

http://www.cisco.com/en/US/products/products_security_vulnerability_policy.html

From this site, you can perform these tasks:

• Report security vulnerabilities in Cisco products.

• Obtain assistance with security incidents that involve Cisco products.

• Register to receive security information from Cisco.

A current list of security advisories and notices for Cisco products is available at this URL:

http://www.cisco.com/go/psirt

If you prefer to see advisories and notices as they are updated in real time, you can access a Product Security Incident Response Team Really Simple Syndication (PSIRT RSS) feed from this URL:

http://www.cisco.com/en/US/products/products_psirt_rss_feed.html

### Reporting Security Problems in Cisco Products

Cisco is committed to delivering secure products. We test our products internally before we release them, and we strive to correct all vulnerabilities quickly. If you think that you might have identified a vulnerability in a Cisco product, contact PSIRT:

• Emergencies — security-alert@cisco.com

• Nonemergencies — psirt@cisco.com

Tip We encourage you to use Pretty Good Privacy (PGP) or a compatible product to encrypt any sensitive information that you send to Cisco. PSIRT can work from encrypted information that is compatible with PGP versions 2. x through 8. x .

Never use a revoked or an expired encryption key. The correct public key to use in your correspondence with PSIRT is the one that has the most recent creation date in this public key server list:

http://pgp.mit.edu:11371/pks/lookup?search=psirt%40cisco.com&op=index&exact=on

In an emergency, you can also reach PSIRT by telephone:

• 1 877 228-7302

• 1 408 525-6532

## Obtaining Technical Assistance

For all customers, partners, resellers, and distributors who hold valid Cisco service contracts, Cisco Technical Support provides 24-hour-a-day, award-winning technical assistance. The Cisco Technical Support Website on Cisco.com features extensive online support resources. In addition, Cisco Technical Assistance Center (TAC) engineers provide telephone support. If you do not hold a valid Cisco service contract, contact your reseller.

### Cisco Technical Support Website

The Cisco Technical Support Website provides online documents and tools for troubleshooting and resolving technical issues with Cisco products and technologies. The website is available 24 hours a day, 365 days a year, at this URL:

http://www.cisco.com/techsupport

Access to all tools on the Cisco Technical Support Website requires a Cisco.com user ID and password. If you have a valid service contract but do not have a user ID or password, you can register at this URL:

http://tools.cisco.com/RPF/register/register.do

Note Use the Cisco Product Identification (CPI) tool to locate your product serial number before submitting a web or phone request for service. You can access the CPI tool from the Cisco Technical Support Website by clicking the Tools & Resources link under Documentation & Tools. Choose Cisco Product Identification Tool from the Alphabetical Index drop-down list, or click the Cisco Product Identification Tool link under Alerts & RMAs. The CPI tool offers three search options: by product ID or model name; by tree view; or for certain products, by copying and pasting show command output. Search results show an illustration of your product with the serial number label location highlighted. Locate the serial number label on your product and record the information before placing a service call.

### Submitting a Service Request

Using the online TAC Service Request Tool is the fastest way to open S3 and S4 service requests. (S3 and S4 service requests are those in which your network is minimally impaired or for which you require product information.) After you describe your situation, the TAC Service Request Tool provides recommended solutions. If your issue is not resolved using the recommended resources, your service request is assigned to a Cisco TAC engineer. The TAC Service Request Tool is located at this URL:

http://www.cisco.com/techsupport/servicerequest

For S1 or S2 service requests or if you do not have Internet access, contact the Cisco TAC by telephone. (S1 or S2 service requests are those in which your production network is down or severely degraded.) Cisco TAC engineers are assigned immediately to S1 and S2 service requests to help keep your business operations running smoothly.

To open a service request by telephone, use one of the following numbers:

Asia-Pacific: +61 2 8446 7411 (Australia: 1 800 805 227) EMEA: +32 2 704 55 55 USA: 1 800 553-2447

For a complete list of Cisco TAC contacts, go to this URL:

http://www.cisco.com/techsupport/contacts

### Definitions of Service Request Severity

To ensure that all service requests are reported in a standard format, Cisco has established severity definitions.

Severity 1 (S1)—Your network is "down," or there is a critical impact to your business operations. You and Cisco will commit all necessary resources around the clock to resolve the situation.

Severity 2 (S2)—Operation of an existing network is severely degraded, or significant aspects of your business operation are negatively affected by inadequate performance of Cisco products. You and Cisco will commit full-time resources during normal business hours to resolve the situation.

Severity 3 (S3)—Operational performance of your network is impaired, but most business operations remain functional. You and Cisco will commit resources during normal business hours to restore service to satisfactory levels.

Severity 4 (S4)—You require information or assistance with Cisco product capabilities, installation, or configuration. There is little or no effect on your business operations.

## Obtaining Additional Publications and Information

Information about Cisco products, technologies, and network solutions is available from various online and printed sources.

• Cisco Marketplace provides a variety of Cisco books, reference guides, and logo merchandise. Visit Cisco Marketplace, the company store, at this URL:

http://www.cisco.com/go/marketplace/

• Cisco Press publishes a wide range of general networking, training and certification titles. Both new and experienced users will benefit from these publications. For current Cisco Press titles and other information, go to Cisco Press at this URL:

http://www.ciscopress.com

• Packet magazine is the Cisco Systems technical user magazine for maximizing Internet and networking investments. Each quarter, Packet delivers coverage of the latest industry trends, technology breakthroughs, and Cisco products and solutions, as well as network deployment and troubleshooting tips, configuration examples, customer case studies, certification and training information, and links to scores of in-depth online resources. You can access Packet magazine at this URL:

http://www.cisco.com/packet

• Internet Protocol Journal is a quarterly journal published by Cisco Systems for engineering professionals involved in designing, developing, and operating public and private internets and intranets. You can access the Internet Protocol Journal at this URL:

http://www.cisco.com/ipj

• World-class networking training is available from Cisco. You can view current offerings at this URL:

http://www.cisco.com/en/US/learning/index.html

## Summary History of Document Changes

Table 4 describes the document changes made after the initial release of the Cisco SRST SNMP MIB Release 3.4 Guide .

Table 4 Summary History of Document Changes

—

OL-7959-01, October 26, 2005

Initial release

| Chapter | Title | Description |
|---|---|---|
| Chapter 1 | Provisioning Overview | This chapter includes a description of the Cisco SRST MIB. |

| Convention | Meaning | Description / Comments |
|---|---|---|
| Boldface | Commands and keywords you enter as shown. | offset-list |
| Italics | Variables for which you supply values. | command type interface You replace the variable with the type of interface. In contexts that do not allow italics, such as online help, arguments are enclosed in angle brackets (< >). |
| Square brackets ([ ]) | Optional elements. | command [abc] abc is optional (not required), but you can choose it. |
| Vertical bars ( \| ) | Separated alternative elements. | command [ abc \| def ] You can choose either abc or def, or neither, but not both. |
| Braces ({ }) | Required choices. | command { abc \| def } You must choose either abc or def, but not both. |
| Braces and vertical bars within square brackets ([ { \| } ]) | A required choice within an optional element. | command [ abc { def \| ghi } ] You have three options: nothing abc def abc ghi |
| Caret character (^) | Control key. | The key combinations ^D and Ctrl-D are equivalent: Both mean "hold down the Control key while you press the D key." Keys are indicated in capital letters, but are not case sensitive. |
| A nonquoted set of characters | A string. | For example, when setting an SNMP community string to public , do not use quotation marks around the string; otherwise, the string will include the quotation marks. |
| System prompts | Denotes interactive sessions, indicates that the user enters commands at the prompt. | The system prompt indicates the current command mode. For example, the prompt Router (config) # indicates global configuration mode. |
| Screen font | Terminal sessions and information the system displays. |  |
| Angle brackets (< >) | Nonprinting characters such as passwords. |  |
| Exclamation point (!) at the beginning of a line | A comment line. | Comments are sometimes displayed by the Cisco IOS software. |

| Data Type | Definition | Example |
|---|---|---|
| Integer | A series of decimal digits from the set of 0 through 9 that represents a positive integer. An integer may have one or more leading zero digits (0) added to the left side to align the columns. Leading zeros are always valid as long as the number of digits is less than or equal to ten digits. Values of this type have a range of zero through 4294967295. | 123 000123 4200000000 |
| Signed integer | This data type has the same basic format as the integer but can be either positive or negative. When negative, it is preceded by the sign character (-). As with the integer data type, this data type can be as many as ten digits in length, not including the sign character. The value of this type has a range of 0 minus 2147483647 through 2147483647. | 123 -000123 -2100000000l |
| Hexadecimal | A series of 16-based digits from the set of 0 through 9, a through f, or A through F. The hexadecimal number may have one or more leading zeros (0) added to the left side. For all hexadecimal values, the maximum size is 0xffffffff (eight hexadecimal digits). | 1f3 01f3000 |
| Text | A series of alphanumeric characters from the ASCII character set, where defined. Tab, space, and double quote ( " " ) characters cannot be used. Text can be as many as 255 characters; however, it is recommended that you limit the text to no more than 32 characters for readability. | EntityID LineSES_Threshold999 |
| String | A series of alphanumeric characters and white-space characters. A string is surrounded by double quotes ( " " ). Strings can be as many as 255 characters; however, it is recommended that you limit the strings to no more than 80 characters for readability. | "This is a descriptive 
string." |

| Subject | Document Number and Change Date | Change Summary |
|---|---|---|
| — | OL-7959-01, October 26, 2005 | Initial release |