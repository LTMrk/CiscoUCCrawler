---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-trouble-12-5-1-cucm-b-troubleshooting-guide-1251-cucm-b-troubleshooting-1a48835de4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/trouble/12_5_1/cucm_b_troubleshooting-guide-1251/cucm_b_troubleshooting-guide-1251_preface_00.html
retrieved_at: 2026-08-16T18:15:15.400586+00:00
---

Troubleshooting Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Troubleshooting Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: November 24, 2023

Chapter: Preface

## Chapter: Preface

# Preface

This preface describes the purpose, audience, organization, and conventions of this guide and provides information on how
                        to obtain related documentation.

## Purpose

The Troubleshooting Guide for Cisco Unified Communications Manager provides troubleshooting procedures for this release of Unified Communications Manager .

The information in this version of the Troubleshooting Guide for Unified Communications Manager may not apply to earlier releases of the Unified Communications Manager software.

This document does not cover every possible trouble event that might occur on a Unified Communications Manager system but instead focuses on those events that are frequently seen by the Cisco Technical Assistance Center (TAC) or frequently
                           asked questions from newsgroups.

## Audience

The Troubleshooting Guide for Unified Communications Manager provides guidance for network administrators who are responsible for managing the Unified Communications Manager system, for enterprise managers, and for employees. This guide requires knowledge of telephony and IP networking technology.

## Organization

The following table shows how this guide is organized.

Chapter and Title

Description

Troubleshooting Overview

Provides an overview of the tools and resources that are available for troubleshooting the Unified Communications Manager .

Troubleshooting Tools

Addresses the tools and utilities that you can use to configure, monitor, and troubleshoot Unified Communications Manager and provides general guidelines for collecting information to avoid repetitive testing and re-collection of identical data.

Cisco Unified Communications Manager System Issues

Describes solutions for the most common issues that relate to a Unified Communications Manager system.

Device Issues

Describes solutions for the most common issues that relate to IP phones and gateways.

Dial Plans and Routing Issues

Describes solutions for the most common issues that relate to dial plans, route partitions, and calling search spaces.

Cisco Unified Communications Manager Services Issues

Describes solutions for the most common issues related to services, such as conference bridges and media termination points.

Voice Messaging Issues

Describes solutions for the most common voice-messaging issues.

Troubleshooting Features and Services

Provides information to help you resolve common issues with Unified Communications Manager features and services.

SNMP Troubleshooting

Provides information on how to troubleshoot with SNMP

Opening a Case With TAC

Describes what information is needed to open a case for TAC.

Case Study: Troubleshooting Cisco Unified IP Phone Calls

Describes in detail the call flow between two Cisco Unified IP Phone s within a cluster.

Case Study: Troubleshooting Cisco Unified IP Phone-to-Cisco IOS Gateway Calls

Describes a Cisco Unified IP Phone calling through a Cisco IOS Gateway to a phone that is connected through a local PBX or on the Public Switched Telephone
                                       Network (PSTN).

## Related Documentation

Refer to the Cisco Unified Communications Manager Documentation Guide for further information about related Cisco IP telephony applications and products. The following URL shows an example of
                           the path to the documentation guide:

http://www.cisco.com/en/US/products/sw/voicesw/ps556/products_documentation_roadmaps_list.html

For documentation that relates to Cisco Unity, refer to the following URL:

https://www.cisco.com/c/en/us/support/unified-communications/index.html

## Conventions

This document uses the following conventions:

Convention

Description

boldface font

Commands and keywords are in boldface .

italic font

Arguments for which you supply values are in italics .

[]

Elements in square brackets are optional.

{ x | y | z }

Alternative keywords are grouped in braces and separated by vertical bars.

[ x | y | z ]

Optional alternative keywords are grouped in brackets and separated by vertical bars.

string

A nonquoted set of characters. Do not use quotation marks around the string or the string will include the quotation marks.

screen font

Terminal sessions and information the system displays are in screen font.

boldface screen font

Information you must enter is in boldface screen font.

italic screen font

Arguments for which you supply values are in italic screen font.

<>

Nonprinting characters, such as passwords, are in angle brackets.

Notes use the following conventions:

Means reader take note . Notes contain helpful suggestions or references to material not covered in the publication.

Timesavers use the following conventions:

Timesaver

Means the described action saves time . You can save time by performing the action described in the paragraph.

Tips use the following conventions:

Tip

Means the information contains useful tips .

Cautions use the following conventions:

Caution

Means reader be careful . In this situation, you might do something that could result in equipment damage or loss of data.

Warnings use the following conventions:

Warning

This warning symbol means danger. You are in a situation that could cause bodily injury. Before you work on any equipment,
                                       you must be aware of the hazards involved with electrical circuitry and familiar with standard practices for preventing accidents.

## Obtaining Documentation, Obtaining Support, and Security Guidelines

For information on obtaining documentation, obtaining support, providing documentation feedback, security guidelines, and
                           also recommended aliases and general Cisco documents, see the monthly What''s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http://www.cisco.com/en/US/docs/general/whatsnew/whatsnew.html

## Cisco Product Security Overview

This product contains cryptographic features and is subject to United States and local country laws governing import, export,
                           transfer and use. Delivery of Cisco cryptographic products does not imply third-party authority to import, export, distribute
                           or use encryption. Importers, exporters, distributors and users are responsible for compliance with U.S. and local country
                           laws. By using this product you agree to comply with applicable laws and regulations. If you are unable to comply with U.S.
                           and local laws, return this product immediately.

Further information regarding U.S. export regulations may be found at http://www.access.gpo.gov/bis/ear/ear_data.html.

| Note | The information in this version of the Troubleshooting Guide for Unified Communications Manager may not apply to earlier releases of the Unified Communications Manager software. |
|---|---|

| Chapter and Title | Description |
|---|---|
| Troubleshooting Overview | Provides an overview of the tools and resources that are available for troubleshooting the Unified Communications Manager . |
| Troubleshooting Tools | Addresses the tools and utilities that you can use to configure, monitor, and troubleshoot Unified Communications Manager and provides general guidelines for collecting information to avoid repetitive testing and re-collection of identical data. |
| Cisco Unified Communications Manager System Issues | Describes solutions for the most common issues that relate to a Unified Communications Manager system. |
| Device Issues | Describes solutions for the most common issues that relate to IP phones and gateways. |
| Dial Plans and Routing Issues | Describes solutions for the most common issues that relate to dial plans, route partitions, and calling search spaces. |
| Cisco Unified Communications Manager Services Issues | Describes solutions for the most common issues related to services, such as conference bridges and media termination points. |
| Voice Messaging Issues | Describes solutions for the most common voice-messaging issues. |
| Troubleshooting Features and Services | Provides information to help you resolve common issues with Unified Communications Manager features and services. |
| SNMP Troubleshooting | Provides information on how to troubleshoot with SNMP |
| Opening a Case With TAC | Describes what information is needed to open a case for TAC. |
| Case Study: Troubleshooting Cisco Unified IP Phone Calls | Describes in detail the call flow between two Cisco Unified IP Phone s within a cluster. |
| Case Study: Troubleshooting Cisco Unified IP Phone-to-Cisco IOS Gateway Calls | Describes a Cisco Unified IP Phone calling through a Cisco IOS Gateway to a phone that is connected through a local PBX or on the Public Switched Telephone
                                       Network (PSTN). |

| Convention | Description |
|---|---|
| boldface font | Commands and keywords are in boldface . |
| italic font | Arguments for which you supply values are in italics . |
| [] | Elements in square brackets are optional. |
| { x \| y \| z } | Alternative keywords are grouped in braces and separated by vertical bars. |
| [ x \| y \| z ] | Optional alternative keywords are grouped in brackets and separated by vertical bars. |
| string | A nonquoted set of characters. Do not use quotation marks around the string or the string will include the quotation marks. |
| screen font | Terminal sessions and information the system displays are in screen font. |
| boldface screen font | Information you must enter is in boldface screen font. |
| italic screen font | Arguments for which you supply values are in italic screen font. |
| <> | Nonprinting characters, such as passwords, are in angle brackets. |

| Note | Means reader take note . Notes contain helpful suggestions or references to material not covered in the publication. |
|---|---|

| Timesaver | Means the described action saves time . You can save time by performing the action described in the paragraph. |
|---|---|

| Tip | Means the information contains useful tips . |
|---|---|

| Caution | Means reader be careful . In this situation, you might do something that could result in equipment damage or loss of data. |
|---|---|

| Warning | This warning symbol means danger. You are in a situation that could cause bodily injury. Before you work on any equipment,
                                       you must be aware of the hazards involved with electrical circuitry and familiar with standard practices for preventing accidents. |
|---|---|