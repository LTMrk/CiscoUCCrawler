---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-managed-services-12-5-1-cucm-b-managed-services-guide-1251-cucm-b-manag-23128b27a9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/managed_services/12_5_1/cucm_b_managed-services-guide-1251/cucm_b_managed-services-guide-1251_preface_00.html
retrieved_at: 2026-08-21T08:59:27.503975+00:00
---

Managed Services Guide for Cisco Unified Communications Manager and IM and Presence Service

# Managed Services Guide for Cisco Unified Communications Manager and IM and Presence Service

Updated: January 22, 2019

Chapter: Preface

## Chapter: Preface

# Preface

This preface describes the purpose, audience, organization, and
                        		conventions of this guide, and provides information on how to obtain related
                        		documentation.

This document may not represent the latest available Cisco product
                                    		  information. You can obtain the most current documentation by accessing the
                                    		  Cisco product documentation page at this URL:

http://www.cisco.com/en/US/products/sw/voicesw/ps556/tsd_products_support_series_home.html

## Purpose

This document gives an overview of Cisco Unified Communications Manager (formerly Cisco Unified CallManager), deployment models,
                              and related Management Information Bases (MIBs). It also explains syslogs, alerts, and alarms for the managed services that
                              Service Providers implement in their networks. This document outlines basic concepts including Simple Network Management Protocol
                              (SNMP) and the features of Cisco Unified Serviceability including Real-Time Monitoring Tool (RTMT).

## Audience

This document provides information for administrators who install, upgrade, and maintain a service provider network. You need
                              to have an understanding of Cisco Unified Communications Manager and Cisco Unified Communications Manager Business Edition 5000. See the Related Documentation for Cisco Unified Communications Manager documents and other related technologies.

## Organization

The following table provides an outline of the chapters in this
                              		  document.

Chapter

Description

Overview

Describes concepts with which you need to be familiar to
                                          						implement SNMP, MIBs, and serviceability features.

Cisco Unified Communications Manager Systems Management and Monitoring

Describes methods for managing and monitoring the Cisco
                                          						Unified Communications Manager servers.

Simple Network Management Protocol

Describes the versions of SNMP and provides some
                                          						troubleshooting tips.

Cisco Unified Real-Time Monitoring Tool Tracing PerfMon Counters and Alerts

Describes the Cisco Unified Real-Time Monitoring Tool,
                                          						default alarms, PerfMon counters, trace collection and other tools for
                                          						troubleshooting.

Cisco Unified Serviceability Alarms and CiscoLog Messages

Describes error messages in Cisco Unified Serviceability and
                                          						CiscoLog message formats.

Cisco Management Information Base

Describes Cisco MIBs and the functionality of each with
                                          						troubleshooting tips.

Industry-Standard Management Information Base

Describes industry-standard MIBs including the functionality
                                          						of each with troubleshooting tips.

## Related
                        	 Documentation

This section lists documents that provide information on Unified Communications Manager , Cisco Unified IP Phones, and Cisco Unified Serviceability. Find the index to the documents at http://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_maintenance_guides_list.html

Unified Communications Manager —A suite of documents that relate to the installation and configuration of Unified Communications Manager . Refer to the Cisco Unified Communications Manager Documentation Guide for a list of documents on installing and configuring Unified Communications Manager including:

Administration Guide for Cisco Unified Communications Manager

System Configuration Guide for Cisco Unified Communications Manager

Feature Configuration Guide for Cisco Unified Communications Manager

Cisco IP Phones and Services —A suite of documents that relate to the installation and configuration of Cisco IP Phones.

Cisco Unified Serviceability —A suite of documents that relate to the maintenance of managed services within Cisco Unified Serviceability. Refer to the Cisco Unified Communications Manager Documentation Guide for a complete list of documents including:

Cisco Unified Serviceability Administration Guide

Cisco Unified Communications Manager Call Detail Records Administration Guide

Cisco Unified Communications Manager CDR Analysis and Reporting Administration Guide

Cisco Unified Real-Time Monitoring Tool Administration Guide

Cisco Unified Reporting Administration Guide

Command Line Interface Reference Guide for Cisco Unified Communications Solutions

Administration Guide for Cisco Unified Communications Manager

## Conventions

This document uses the following conventions:

Convention

Description

boldface font

Commands and keywords are in boldface.

italic font

Arguments for which you supply values are in italics.

[   ]

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

^

The symbol ^ represents the key labeled Control—for example, the key combination ^D in a screen display means hold down the
                                          Control key while you press the D key.

<   >

Nonprinting characters, such as passwords are in angle brackets.

Notes use the following conventions:

Means reader take note. Notes contain helpful suggestions or references to material not covered in the publication.

Timesavers use the following conventions:

Means the described action saves time. You can save time by performing the action described in the paragraph.

Tips use the following conventions:

Means the following are useful tips.

## Cisco Product Security Overview

This product contains cryptographic features and is subject to United States and local country laws governing import, export,
                              transfer and use. Delivery of Cisco cryptographic products does not imply third-party authority to import, export, distribute
                              or use encryption. Importers, exporters, distributors and users are responsible for compliance with U.S. and local country
                              laws. By using this product you agree to comply with applicable laws and regulations. If you are unable to comply with U.S.
                              and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at— http://www.cisco.com/wwl/export/crypto/tool/stqrg.html.

If you require further assistance please contact us by sending e-mail to export@cisco.com.

| Note | This document may not represent the latest available Cisco product
                                    		  information. You can obtain the most current documentation by accessing the
                                    		  Cisco product documentation page at this URL: http://www.cisco.com/en/US/products/sw/voicesw/ps556/tsd_products_support_series_home.html |
|---|---|

| Chapter | Description |
|---|---|
| Overview | Describes concepts with which you need to be familiar to
                                          						implement SNMP, MIBs, and serviceability features. |
| Cisco Unified Communications Manager Systems Management and Monitoring | Describes methods for managing and monitoring the Cisco
                                          						Unified Communications Manager servers. |
| Simple Network Management Protocol | Describes the versions of SNMP and provides some
                                          						troubleshooting tips. |
| Cisco Unified Real-Time Monitoring Tool Tracing PerfMon Counters and Alerts | Describes the Cisco Unified Real-Time Monitoring Tool,
                                          						default alarms, PerfMon counters, trace collection and other tools for
                                          						troubleshooting. |
| Cisco Unified Serviceability Alarms and CiscoLog Messages | Describes error messages in Cisco Unified Serviceability and
                                          						CiscoLog message formats. |
| Cisco Management Information Base | Describes Cisco MIBs and the functionality of each with
                                          						troubleshooting tips. |
| Industry-Standard Management Information Base | Describes industry-standard MIBs including the functionality
                                          						of each with troubleshooting tips. |

| Convention | Description |
|---|---|
| boldface font | Commands and keywords are in boldface. |
| italic font | Arguments for which you supply values are in italics. |
| [   ] | Elements in square brackets are optional. |
| { x \| y \| z } | Alternative keywords are grouped in braces and separated by vertical bars. |
| [ x \| y \| z ] | Optional alternative keywords are grouped in brackets and separated by vertical bars. |
| string | A nonquoted set of characters. Do not use quotation marks around the string or the string will include the quotation marks. |
| screen font | Terminal sessions and information the system displays are in screen font. |
| boldface screen font | Information you must enter is in boldface screen font. |
| italic screen font | Arguments for which you supply values are in italic screen font. |
| ^ | The symbol ^ represents the key labeled Control—for example, the key combination ^D in a screen display means hold down the
                                          Control key while you press the D key. |
| <   > | Nonprinting characters, such as passwords are in angle brackets. |

| Note | Means reader take note. Notes contain helpful suggestions or references to material not covered in the publication. |
|---|---|

| Warning | Means the described action saves time. You can save time by performing the action described in the paragraph. |
|---|---|

| Tip | Means the following are useful tips. |
|---|---|