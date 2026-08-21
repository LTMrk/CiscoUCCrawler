---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-14su1-cucm-b-bulk-administration-guide-14su1-cucm-b-bulk-administra-af5c3fa504
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/14SU1/cucm_b_bulk-administration-guide-14SU1/cucm_b_bulk-administration-guide-1251su2_preface_00.html
retrieved_at: 2026-08-21T09:07:42.415095+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: October 27, 2021

Chapter: Preface

## Chapter: Preface

# Preface

This preface describes the purpose, audience, organization, and
                        		conventions of this guide, and provides information on how to obtain related
                        		documentation.

This document may not represent the latest Cisco product information
                                    		  available. You can obtain the most current documentation by accessing Cisco's
                                    		  product documentation page at this URL: http://www.cisco.com/en/US/products/sw/voicesw/ps556/tsd_products_support_series_home.html

## Purpose

The CiscoUnified Communications Manager Bulk Administration Guide provides instructions for using the Bulk Administration menu of Cisco Unified Communications Manager Administration.

## Audience

This document provides information for network administrators and engineers who are responsible for managing the Cisco Unified Communications Manager system. Administering Cisco Unified Communications Manager Bulk Administration (BAT) requires knowledge of telephony and IP networking technology.

## Organization

Table1 provides the organization of this guide.

Layout of BAT Tool User Guide

Chapter

Description

Overview

Unified Communications Manager Bulk Administration Overview

Provides an overview of BAT.

File Upload and Download

Upload/Download Files

Describes how to upload and download files.

Phones

Phones

Describes how to add phones, phones and users, computer telephony integration (CTI) ports, and CTI ports and users in batches
                                       rather than adding each device or combination individually. Also describes how to add or update lines, phone services, and
                                       speed dials and how to update and delete phones.

Users

Users

Describes how to add, update, and delete batches of users.

Phones and Users

Phones and Users

Describes how to add a group of users and their phones on a Unified Communications Manager server in one bulk transaction.

Managers and Assistants

Managers and Assistants

Describes how to add, update, or delete Manager Assistant Associations.

User Device Profiles

User Device Profiles

Describes how to add, update, or delete User Device Profiles.

Gateways

Gateways

Describes how to add, update, or delete Cisco VG200 gateways and ports, and how to add or delete Foreign Exchange Station
                                       (FXS) ports for Cisco Catalyst 6000 analog interface modules. Also describes how to create a gateway directory number template
                                       for use with FXS ports.

Forced Authorization Codes and Client Matter Codes

Forced Authorization Codes and Client Matter Codes

Describes how to add, update, or delete Client Matter Codes and Forced Authorization Codes.

Call Pickup Groups

Pickup Groups

Describes how to add, update, or delete call pickup groups.

Mobility

Mobility

Describes how to insert, delete, and export access lists, remote destinations and remote destination profiles.

Region Matrix

Region Matrix

Describes how to populate and depopulate the region matrix.

Import/Export

Import/Export

Describes how to import or export Unified Communications Manager database to another server, or to the same server with modifications.

Phone Migration

Phone Migration

Describes the Phone Migration menu in BAT and details the procedure to migrate phones in bulk.

Extension Mobility Cross Cluster (EMCC)

Extension Mobility Cross Cluster (EMCC)

Describes the EMCC menu in BAT and details how to insert, delete, and update EMCC.

Intercompany Media Engine (IME)

Intercompany Media Services

Describes the Intercompany Media Services menu in BAT and details how to insert and delete Trusted Element, Trusted Group,
                                       Enrolled Group, Exclusion Group, and Fallback Profile configuration.

CUPS

CUPS

Describes the CUPS menu in BAT and details its use to update and export the CUPS and CUPC users.

Tool for Auto-Registered Phones Support

Tool for Auto-Registered Phones Support (TAPS).

Describes how to install, configure, and use TAPS.

Scheduling Jobs

Scheduling Jobs

Describes how to schedule and activate jobs.

Troubleshooting BAT and TAPS

Troubleshooting BAT and UnifiedCM Auto-Register Phone Tool

Describes some common scenarios for bulk transaction log files and provides an explanation and resolution for various error
                                       messages that you may encounter while working with BAT or UnifiedCM Auto-Register Phone Tool.

Appendixes

Appendixes

Describes how to create text-based files for the devices and users for bulk transactions. Also provides example of file formats
                                       for different scenarios.

## Related
                        	 Documentation

Refer to
                              		  the following documents for further information about related
                              		  CiscoIPtelephony applications and products:

Cisco Unified Communications
                                          					 Manager Online Help

Cisco Unified Communications Manager System Configuration
                                       				  Guide

Release Notes for Cisco Unified Communications Manager

Installing Cisco Unified Communications Manager

Cisco Unified Serviceability Administration Guide

Cisco Unified Communications Manager Security Guide

Hardware Configuration Guide
                                       				  for the Cisco VG200

Software Configuration Guide
                                       				  for the Cisco VG200

Cisco VG248 Analog Phone
                                       				  Gateway Software Configuration Guide

CiscoUnifiedIPPhone Administration Guide for Cisco Unified Communications Manager

Feature Configuration Guide for Cisco Unified Communications
                                       				  Manager

Troubleshooting Guide for Cisco Unified Communications Manager

Cisco Unified Communications Manager Assistant User Guide

## Conventions

This document uses the following conventions:

Convention

Description

boldface font

Commands and keywords are in boldface.

italic font

Arguments for which you supply values are in italics.

string

A nonquoted set of characters. Do not use quotation marks around the string or the string will include the quotation marks.

screen font

Terminal sessions and information the system displays are in screen font.

boldface screen font

Information you must enter is in boldface screen font.

Notes use the following conventions:

Means reader take note. Notes contain helpful suggestions or references to material not covered in the publication.

Timesavers use the following conventions:

Timesaver

Means the described action saves time. You can save time by performing the action described in the paragraph.

Tips use the following conventions:

Tip

Means the information contains useful tips.

Cautions use the following conventions:

Caution

Means reader be careful. In this situation, you might do something that could result in equipment damage or loss of data.

Warnings use the following conventions:

Warning

This warning symbol means danger. You are in a situation that could cause bodily injury. Before you work on any equipment,
                                          you must be aware of the hazards involved with electrical circuitry and familiar with standard practices for preventing accidents.

## Documentation and Service Requests

For information on obtaining documentation, submitting a
                              		  service request, and gathering additional information, see the monthly What'sNew in CiscoProduct Documentation , which also lists all new and
                              		  revised Ciscotechnical documentation, at:

http://www.cisco.com/en/US/docs/general/whatsnew/whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication(RSS) feed and set content to be delivered
                              		  directly to your desktop using a reader application. The RSS feeds are a free
                              		  service and Cisco currently supports RSSVersion2.0.

## Cisco Product Security Overview

This product contains cryptographic features and is subject to United States and local country laws governing import, export,
                              transfer and use. Delivery of Cisco cryptographic products does not imply third-party authority to import, export, distribute
                              or use encryption. Importers, exporters, distributors and users are responsible for compliance with U.S. and local country
                              laws. By using this product you agree to comply with applicable laws and regulations. If you are unable to comply with U.S.
                              and local laws, return this product immediately.

Further information regarding U.S. export regulations may be found at http://www.access.gpo.gov/bis/ear/ear_data.html

| Note | This document may not represent the latest Cisco product information
                                    		  available. You can obtain the most current documentation by accessing Cisco's
                                    		  product documentation page at this URL: http://www.cisco.com/en/US/products/sw/voicesw/ps556/tsd_products_support_series_home.html |
|---|---|

| Chapter | Description |
|---|---|
| Overview | Unified Communications Manager Bulk Administration Overview Provides an overview of BAT. |
| File Upload and Download | Upload/Download Files Describes how to upload and download files. |
| Phones | Phones Describes how to add phones, phones and users, computer telephony integration (CTI) ports, and CTI ports and users in batches
                                       rather than adding each device or combination individually. Also describes how to add or update lines, phone services, and
                                       speed dials and how to update and delete phones. |
| Users | Users Describes how to add, update, and delete batches of users. |
| Phones and Users | Phones and Users Describes how to add a group of users and their phones on a Unified Communications Manager server in one bulk transaction. |
| Managers and Assistants | Managers and Assistants Describes how to add, update, or delete Manager Assistant Associations. |
| User Device Profiles | User Device Profiles Describes how to add, update, or delete User Device Profiles. |
| Gateways | Gateways Describes how to add, update, or delete Cisco VG200 gateways and ports, and how to add or delete Foreign Exchange Station
                                       (FXS) ports for Cisco Catalyst 6000 analog interface modules. Also describes how to create a gateway directory number template
                                       for use with FXS ports. |
| Forced Authorization Codes and Client Matter Codes | Forced Authorization Codes and Client Matter Codes Describes how to add, update, or delete Client Matter Codes and Forced Authorization Codes. |
| Call Pickup Groups | Pickup Groups Describes how to add, update, or delete call pickup groups. |
| Mobility | Mobility Describes how to insert, delete, and export access lists, remote destinations and remote destination profiles. |
| Region Matrix | Region Matrix Describes how to populate and depopulate the region matrix. |
| Import/Export | Import/Export Describes how to import or export Unified Communications Manager database to another server, or to the same server with modifications. |
| Phone Migration | Phone Migration Describes the Phone Migration menu in BAT and details the procedure to migrate phones in bulk. |
| Extension Mobility Cross Cluster (EMCC) | Extension Mobility Cross Cluster (EMCC) Describes the EMCC menu in BAT and details how to insert, delete, and update EMCC. |
| Intercompany Media Engine (IME) | Intercompany Media Services Describes the Intercompany Media Services menu in BAT and details how to insert and delete Trusted Element, Trusted Group,
                                       Enrolled Group, Exclusion Group, and Fallback Profile configuration. |
| CUPS | CUPS Describes the CUPS menu in BAT and details its use to update and export the CUPS and CUPC users. |
| Tool for Auto-Registered Phones Support | Tool for Auto-Registered Phones Support (TAPS). Describes how to install, configure, and use TAPS. |
| Scheduling Jobs | Scheduling Jobs Describes how to schedule and activate jobs. |
| Troubleshooting BAT and TAPS | Troubleshooting BAT and UnifiedCM Auto-Register Phone Tool Describes some common scenarios for bulk transaction log files and provides an explanation and resolution for various error
                                       messages that you may encounter while working with BAT or UnifiedCM Auto-Register Phone Tool. |
| Appendixes | Appendixes Describes how to create text-based files for the devices and users for bulk transactions. Also provides example of file formats
                                       for different scenarios. |

| Convention | Description |
|---|---|
| boldface font | Commands and keywords are in boldface. |
| italic font | Arguments for which you supply values are in italics. |
| string | A nonquoted set of characters. Do not use quotation marks around the string or the string will include the quotation marks. |
| screen font | Terminal sessions and information the system displays are in screen font. |
| boldface screen font | Information you must enter is in boldface screen font. |

| Note | Means reader take note. Notes contain helpful suggestions or references to material not covered in the publication. |
|---|---|

| Timesaver | Means the described action saves time. You can save time by performing the action described in the paragraph. |
|---|---|

| Tip | Means the information contains useful tips. |
|---|---|

| Caution | Means reader be careful. In this situation, you might do something that could result in equipment damage or loss of data. |
|---|---|

| Warning | This warning symbol means danger. You are in a situation that could cause bodily injury. Before you work on any equipment,
                                          you must be aware of the hazards involved with electrical circuitry and familiar with standard practices for preventing accidents. |
|---|---|