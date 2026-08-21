---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-cdrdef-cucm-b-cdr-admin-guide-1251-cucm-b-cdr-admin-guid-2a3614df03
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/cdrdef/cucm_b_cdr-admin-guide-1251/cucm_b_cdr-admin-guide-1251_preface_00.html
retrieved_at: 2026-08-21T01:38:02.125378+00:00
---

Call Detail Records Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Call Detail Records Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: January 22, 2019

Chapter: Preface

## Chapter: Preface

# Preface

## Change History

Change

Date

Information on CDR OnDemand Service AXIS 1.4 Compatibility With Cisco Unified Communications Manager Release 12.0

March 22, 2018

## Purpose

The Cisco Unified Communications Manager Call Detail Records
                                    				Administration Guide describes how to configure call detail
                              		  records (CDRs) and call management records (CMRs) and provides examples of
                              		  these records. Use this guide in conjunction with the following documents:

CDR Analysis and Reporting Administration
                                          					 Guide —This document describes how to configure and use Cisco Unified Communications
                                       				  Manager CDR Analysis and Reporting (CAR), a tool that is used to
                                    				create user, system, device, and billing reports.

Cisco Unified Serviceability Administration
                                          					 Guide —This document provides descriptions and procedures for
                                    				configuring alarms, traces, SNMP, and so on, through Cisco Unified
                                       				  Serviceability .

Real-Time Monitoring Tool Administration Guide —This document describes how to use Real-Time Monitoring Tool (RTMT), a tool
                                    				that allows you to monitor many aspects of the system (critical services,
                                    				alerts, performance counters, and so on).

Cisco Unity Connection Serviceability Administration
                                          					 Guide —This document provides descriptions and procedures for
                                    				using alarms, traces, reports, and so on, through Cisco Unity Connection
                                       				  Serviceability .

## Audience

The Cisco Unified Communications Manager Call Detail Records
                                    				Administration Guide provides information for administrators
                              		  who are responsible for managing and supporting CDRs. Network engineers, system
                              		  administrators, or telecom engineers use this guide to learn the content and
                              		  structure of CDR and CMR records to import them into billing programs and other
                              		  third-party programs. CAR administrators, managers, and end users use this
                              		  guide to analyze the information that is generated in certain CAR reports.

## Related
                        	 Documentation

See the Cisco Unified Communications Manager Documentation Guide for more Unified Communications Manager documentation. The following URL shows an example of the path to the documentation guide:

http://www.cisco.com/en/US/docs/voice_ip_comm/cucm/docguide/8_0_1/dg801.html

For more Cisco Unity Connection documentation, see the Cisco Unity Connection Documentation Guide at http://www.cisco.com/en/US/products/ps6509/products_documentation_roadmaps_list.html.

## Organization

The
                              		  following table shows how this guide is organized:

Chapter

Description

Overview

Cisco Call Detail Records

Provides an overview of call detail records and an understanding
                                          						of CDR management.

CDR Processing

Describes the procedures for how CDRs are processed.

Call Information Record Types

Provides information on call information records.

Call Detail Records

CDR Examples

Provides examples of call detail records.

Cisco Call Detail Records Field Descriptions

Describes all call detail record fields.

Cisco Call Detail Records Codes

Provides information on all CDR codes, including call
                                          						termination cause codes, codec type codes, redirect reason codes, and
                                          						onbehalfof codes.

Call Management Records

Call Management Records

Provides an overview of call management records (CMRs).

Cisco Call Management Record Field Descriptions

Describes CMR fields.

Cisco Call Management Records K-Factor Data

Describes K-Factor data information in the CMR record.

Example Cisco Call Management Records

Provides examples of CMRs.

## Conventions

This
                              		  document uses the following conventions:

Convention

Description

boldface font

Commands and keywords are in boldface .

italic font

Arguments for which you supply values are in italics .

[]

Elements in square brackets are optional.

{
                                          						x | y | z }

Alternative keywords are grouped in braces and separated by
                                          						vertical bars.

[
                                          						x | y | z ]

Optional alternative keywords are grouped in brackets and
                                          						separated by vertical bars.

string

A
                                          						nonquoted set of characters. Do not use quotation marks around the string or
                                          						the string will include the quotation marks.

screen font

Terminal sessions and information the system displays are in screen font.

boldface screen font

Information you must enter is in boldface screen font.

italic
                                             						  screen font

Arguments for which you supply values are in italic
                                             						  screen font.

^

The symbol ^ represents the key labeled Control—for example, the
                                          						key combination ^D in a screen display means hold down the Control key while
                                          						you press the Dkey.

<>

Nonprinting characters, such as passwords, are in angle
                                          						brackets.

Notes use
                              		  the following conventions:

Timesavers
                              		  use the following conventions:

Tips use
                              		  the following conventions:

Cautions
                              		  use the following conventions:

Warnings
                              		  use the following conventions:

## Obtain Documentation
                        	 and Submit Service Requests

For
                              		  information on obtaining documentation, submitting a service request, and
                              		  gathering additional information, see the monthly What'sNew in CiscoProduct
                                 			 Documentation , which also lists all new and revised Ciscotechnical
                              		  documentation, at:

http://www.cisco.com/en/US/docs/general/whatsnew/whatsnew.html

Subscribe
                              		  to the What's New in
                                 			 Cisco Product Documentation as a Really Simple Syndication (RSS) feed
                              		  and set content to be delivered directly to your desktop using a reader
                              		  application. The RSS feeds are a free service and Cisco currently supports RSS
                              		  version 2.0.

## Cisco Product
                        	 Security Overview

This
                              		  product contains cryptographic features and is subject to United States and
                              		  local country laws governing import, export, transfer and use. Delivery of
                              		  Cisco cryptographic products does not imply third-party authority to import,
                              		  export, distribute or use encryption. Importers, exporters, distributors and
                              		  users are responsible for compliance with U.S. and local country laws. By using
                              		  this product you agree to comply with applicable laws and regulations. If you
                              		  are unable to comply with U.S. and local laws, return this product immediately.

Further
                              		  information regarding U.S. export regulations may be found at http://www.access.gpo.gov/bis/ear/ear_data.html.

| Change | Date |
|---|---|
| Information on CDR OnDemand Service AXIS 1.4 Compatibility With Cisco Unified Communications Manager Release 12.0 | March 22, 2018 |

| Chapter | Description |
|---|---|
| Overview |
| Cisco Call Detail Records | Provides an overview of call detail records and an understanding
                                          						of CDR management. |
| CDR Processing | Describes the procedures for how CDRs are processed. |
| Call Information Record Types | Provides information on call information records. |
| Call Detail Records |
| CDR Examples | Provides examples of call detail records. |
| Cisco Call Detail Records Field Descriptions | Describes all call detail record fields. |
| Cisco Call Detail Records Codes | Provides information on all CDR codes, including call
                                          						termination cause codes, codec type codes, redirect reason codes, and
                                          						onbehalfof codes. |
| Call Management Records |
| Call Management Records | Provides an overview of call management records (CMRs). |
| Cisco Call Management Record Field Descriptions | Describes CMR fields. |
| Cisco Call Management Records K-Factor Data | Describes K-Factor data information in the CMR record. |
| Example Cisco Call Management Records | Provides examples of CMRs. |

| Convention | Description |
|---|---|
| boldface font | Commands and keywords are in boldface . |
| italic font | Arguments for which you supply values are in italics . |
| [] | Elements in square brackets are optional. |
| {
                                          						x \| y \| z } | Alternative keywords are grouped in braces and separated by
                                          						vertical bars. |
| [
                                          						x \| y \| z ] | Optional alternative keywords are grouped in brackets and
                                          						separated by vertical bars. |
| string | A
                                          						nonquoted set of characters. Do not use quotation marks around the string or
                                          						the string will include the quotation marks. |
| screen font | Terminal sessions and information the system displays are in screen font. |
| boldface screen font | Information you must enter is in boldface screen font. |
| italic
                                             						  screen font | Arguments for which you supply values are in italic
                                             						  screen font. |
| ^ | The symbol ^ represents the key labeled Control—for example, the
                                          						key combination ^D in a screen display means hold down the Control key while
                                          						you press the Dkey. |
| <> | Nonprinting characters, such as passwords, are in angle
                                          						brackets. |

| Note | Means reader take note . Notes contain helpful suggestions or references to material not covered in the publication. |
|---|---|

| Timesaver | Means the described action saves time . You can save time by performing the action described in the paragraph. |
|---|---|

| Tip | Means the information contains useful tips. |
|---|---|

| Caution | Means reader be careful . In this situation, you might do something that could result in equipment damage or loss of data. |
|---|---|

| Warning | This warning symbol means danger. You are in a situation that could cause bodily injury. Before you work on any equipment,
                                       you must be aware of the hazards involved with electrical circuitry and familiar with standard practices for preventing accidents. |
|---|---|