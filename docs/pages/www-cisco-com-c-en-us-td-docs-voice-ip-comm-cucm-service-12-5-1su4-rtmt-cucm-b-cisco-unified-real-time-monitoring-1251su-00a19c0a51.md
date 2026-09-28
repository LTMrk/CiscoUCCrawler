---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1su4-rtmt-cucm-b-cisco-unified-real-time-monitoring-1251su-00a19c0a51
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1SU4/rtmt/cucm_b_cisco-unified-real-time-monitoring-1251su4/cucm_b_cisco-unified-rtmt-administration-1251su2_preface_00.html
retrieved_at: 2026-08-21T01:41:08.726937+00:00
---

Cisco Unified Real-Time Monitoring Tool Administration Guide, Release 12.5(1)SU4

# Cisco Unified Real-Time Monitoring Tool Administration Guide, Release 12.5(1)SU4

Updated: January 9, 2023

Chapter: Preface

## Chapter: Preface

# Preface

This document may not represent the latest Cisco product information available. You can obtain the most current documentation
                                       by accessing the Cisco product documentation page at:

http://www.cisco.com/en/US/products/sw/voicesw/ps556/tsd_products_support_series_home.html

## About This
                        	 Guide

The Cisco Unified Real-Time Monitoring Tool Administration Guide provides information about the Cisco Unified Real-Time Monitoring
                              Tool.

Use this
                              		  guide with the following documentation for your configuration:

, , Cisco Unified Serviceability Administration Guide, and

Cisco Unity Connection System Administration Guide and Cisco Unity Connection Serviceability Administration Guide

These
                              		  documents provide the following information:

Instructions for administering , , and .

Descriptions
                                    				of procedural tasks that you can perform by using the administration interface.

## Audience

The Cisco Unified Real-Time Monitoring Tool Administration Guide provides information for network administrators who are responsible for
                              		  managing and supporting Cisco Unified Communications Manager , Cisco Unified Communications Manager IM and Presence Service , and Cisco Unity Connection . Network engineers, system administrators, or telecom
                              		  engineers can use this guide to learn about, and administer, remote serviceability
                              		  features. This guide requires knowledge of telephony and IP networking
                              		  technology.

## Related
                        	 Documentation

For additional documentation
                              		  about Cisco Unified Communications
                                 			 Manager and Cisco Unified Communications
                                 			 Manager IM and Presence Service , see the Cisco Unified Communications Manager Documentation
                                    				Guide .

For
                              		  additional documentation about Cisco Unity
                                 			 Connection , see the Cisco Unity Connection Documentation Guide .

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

Alternative keywords are grouped in braces and
                                          						separated by vertical bars.

[ x | y | z ]

Optional alternative keywords are grouped in
                                          						brackets and separated by vertical bars.

string

A nonquoted set of characters. Do not use
                                          						quotation marks around the string or the string will include the quotation
                                          						marks.

screen font

Terminal sessions and information the system
                                          						displays are in screen font.

boldface screen font

Information you must enter is in boldface screen font.

italic screen font

Arguments for which you supply values are in italic screen font.

^

The symbol ^ represents the key labeled
                                          						Control—for example, the key combination ^D in a screen display means hold down
                                          						the Control key while you press the Dkey.

<>

Nonprinting characters, such as passwords, are in
                                          						angle brackets.

Notes use the following conventions:

Means reader take note . Notes contain helpful suggestions or
                                          			 references to material not covered in the publication.

Timesavers use the following conventions:

Timesaver

Means the described action saves time . You can save time by
                                          			 performing the action described in the paragraph.

Tips use the following conventions:

Tip

Means the information contains useful tips .

Cautions use the following conventions:

Caution

Means reader be careful . In this situation, you might do something
                                          			 that could result in equipment damage or loss of data.

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

### Cisco Product Security

This product contains cryptographic features and is subject to United States and local country laws governing import, export,
                              transfer and use. Delivery of Cisco cryptographic products does not imply third-party authority to import, export, distribute
                              or use encryption. Importers, exporters, distributors and users are responsible for compliance with U.S. and local country
                              laws. By using this product you agree to comply with applicable laws and regulations. If you are unable to comply with U.S.
                              and local laws, return this product immediately.

Further information regarding U.S. export regulations may be found at http://www.access.gpo.gov/bis/ear/ear_data.html .

## Organization

Overview of 
                                       					 Unified RTMT, including browser support.

Description of how to install, access, and use the Unified RTMT client.

Overview of system performance monitoring in RTMT, including how to manage predefined objects for your system, Cisco Unified Communications Manager , Cisco Intercompany Media Engine, Cisco Unified Communications Manager IM and Presence Service , and Cisco Unity Connection.

Provides information about Cisco Unified Analysis
                                       						Manager, including procedures to install and configure the Unified Analysis Manager; procedures to add nodes that the
                                       Unified Analysis Manager can diagnose; procedures for device management; and information about troubleshooting.

Provides information about how to manage profiles and categories.

Provides procedures for working with performance
                                       						monitors, including viewing performance counters and counter descriptions, and
                                       						perfmon logs.

Provides procedures for working with alerts.

Provides information about configuring on-demand trace
                                       						collection and crash dump files for system services and methods to view the
                                       						trace files in the appropriate viewer.

Provides a complete list of performance objects
                                       						and their associated counters for components of your system.

| Note | This document may not represent the latest Cisco product information available. You can obtain the most current documentation
                                       by accessing the Cisco product documentation page at: http://www.cisco.com/en/US/products/sw/voicesw/ps556/tsd_products_support_series_home.html |
|---|---|

|  | , , Cisco Unified Serviceability Administration Guide, and |
|---|---|
|  |  |
|  | Cisco Unity Connection System Administration Guide and Cisco Unity Connection Serviceability Administration Guide |

| Convention | Description |
|---|---|
| boldface font | Commands and keywords are in boldface . |
| italic font | Arguments for which you supply values are in italics . |
| [] | Elements in square brackets are optional. |
| { x \| y \| z } | Alternative keywords are grouped in braces and
                                          						separated by vertical bars. |
| [ x \| y \| z ] | Optional alternative keywords are grouped in
                                          						brackets and separated by vertical bars. |
| string | A nonquoted set of characters. Do not use
                                          						quotation marks around the string or the string will include the quotation
                                          						marks. |
| screen font | Terminal sessions and information the system
                                          						displays are in screen font. |
| boldface screen font | Information you must enter is in boldface screen font. |
| italic screen font | Arguments for which you supply values are in italic screen font. |
| ^ | The symbol ^ represents the key labeled
                                          						Control—for example, the key combination ^D in a screen display means hold down
                                          						the Control key while you press the Dkey. |
| <> | Nonprinting characters, such as passwords, are in
                                          						angle brackets. |

| Note | Means reader take note . Notes contain helpful suggestions or
                                          			 references to material not covered in the publication. |
|---|---|

| Timesaver | Means the described action saves time . You can save time by
                                          			 performing the action described in the paragraph. |
|---|---|

| Tip | Means the information contains useful tips . |
|---|---|

| Caution | Means reader be careful . In this situation, you might do something
                                          			 that could result in equipment damage or loss of data. |
|---|---|