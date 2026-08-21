---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-release-notes-srst-releasenotes-12-6-html-856d48b08a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/release/notes/SRST_ReleaseNotes_12_6.html
retrieved_at: 2026-08-21T21:28:52.228377+00:00
---

Release Notes for Cisco Unified Survivable Remote Site Telephony, 12.6

# Release Notes for Cisco Unified Survivable Remote Site Telephony, 12.6

## Table of Contents

Release Notes for Cisco Unified Survivable Remote Site Telephony, Release 12.6

Contents

Introduction

System Requirements

Memory Requirements

Hardware Supported

Platforms

Software Compatibility

Determining the Software Version

Upgrading to a New Software Release

Feature Set Tables

New and Changed Information

Changed Information for Unified SRST, 12.6

Deprecation of CLI Commands under Call-Manager-Fallback Configuration Mode

New Features in Unified SRST, Release 12.6

Support for Toll Fraud Prevention for Line Side SIP on Unified SRST and Unified E-SRST

Support for Unified SRST, Unified E-SRST, and Unified Secure SRST Password Policy

Support for SNMP Version 3 (SNMPv3) on Unified SRST

Support for Specific License Reservation (SLR)

Caveats

Open Caveats—Unified SRST, Release 12.6

Related Documentation

Software Documents

Service and Support

Obtain Documentation and Submit a Service Request

First Published: April 15, 2019

Last Updated: October 30, 2020

## Introduction

This Release Notes document describes the features of Cisco Unified Survivable Remote Site Telephony, Release 12.6 (Cisco IOS XE Gibraltar 16.11.1a, Cisco IOS XE Gibraltar 16.12.1).

To ensure that you have the latest version of this Release Notes, go to https://www.cisco.com/c/en/us/products/unified-communications/unified-survivable-remote-site-telephony/index.html . Choose Release and General Information > Release Notes, and locate the latest release notes pertaining to your release.

## System Requirements

### Memory Requirements

The Cisco 4000 Series Integrated Services Router platforms require 4 GB of DRAM.

Hardware Supported

### Hardware Supported

### Platforms

The following Cisco 4000 Series Integrated Services Router platforms are supported:

- Cisco 4321 Integrated Services Router

- Cisco 4331 Integrated Services Router

- Cisco 4351 Integrated Services Router

- Cisco 4431 Integrated Services Router

- Cisco 4451 Integrated Services Router

- Cisco 4461 Integrated Services Router (Supported from Cisco IOS XE Gibraltar 16.10.1 Release)

### Software Compatibility

For more information on supported images and minimum software version requirement for Unified SRST features, see Cisco Unified SCCP and SIP SRST System Administrator Guide .

To determine the correct Cisco IOS release to support a specific Unified SRST version, see the Cisco Unified CME, Unified SRST, and Cisco IOS Software Version Compatibility Matrix .

Use Cisco Feature Navigator to find information about platform support and Cisco IOS software image support. To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn . You do not need an account on Cisco.com for access.

### Determining the Software Version

To determine the release of Cisco IOS software currently running on your Cisco router, log in to the router and enter the show version command. The following sample output from the show version command indicates the Cisco IOS release on the first output line:

Router-4400# show version

Cisco IOS XE Software, Version Cisco IOS XE 16.11.1a

Cisco IOS Software, ISR Software (X86_64_LINUX_IOSD-UNIVERSALK9-M),

Copyright (c) 1986-2018 by Cisco Systems, Inc.

Compiled Fri 16-Nov-18 01:12.

Router-4400# show version

Cisco IOS XE Software, Version Cisco IOS XE 16.12.1

Cisco IOS Software, ISR Software (X86_64_LINUX_IOSD-UNIVERSALK9-M),

Copyright (c) 1986-2018 by Cisco Systems, Inc.

Compiled Fri 16-Nov-18 01:12.

### Upgrading to a New Software Release

To determine which Cisco IOS software release supports the recommended Unified SRST version, see Unified SRST and Cisco IOS Software Compatibility Matrix . To install the new software release, see the “Install Cisco IOS Software” section of the Cisco Unified Communications Manager Express Administrator Guide .

### Feature Set Tables

Use Cisco Feature Navigator to find information about platform support and software image support. Cisco Feature Navigator enables you to determine which software images support a specific software release, feature set, or platform. To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn .

## New and Changed Information

### Changed Information for Unified SRST, 12.6

From Unified SRST Release 12.6 (Cisco IOS XE Gibraltar 16.11.1a), the following changes are applicable to Unified SRST:

- Deprecation of CLI Commands under Call-Manager-Fallback Configuration Mode

### Deprecation of CLI Commands under Call-Manager-Fallback Configuration Mode

For information on the list of CLI commands that are not supported on Unified SRST Release12.6 and later releases as part of security enhancement, see Cisco Unified SCCP and SIP SRST System Administrator Guide (All Versions) .

### Support for Toll Fraud Prevention for Line Side SIP on Unified SRST and Unified E-SRST

For information on configuring toll fraud prevention for line side SIP on Unified SRST, see Cisco Unified SCCP and SIP SRST System Administrator Guide (All Versions) .

### Support for Unified SRST, Unified E-SRST, and Unified Secure SRST Password Policy

For information on the new Unified SRST, Unified E-SRST, and Unified Secure SRST password policy, see Cisco Unified SCCP and SIP SRST System Administrator Guide (All Versions) .

### Support for SNMP Version 3 (SNMPv3) on Unified SRST

For information on support for Simple Network Management Protocol Version 3 (SNMPv3) on Unified SRST, see Cisco Unified SCCP and SIP SRST System Administrator Guide (All Versions) .

### Support for Specific License Reservation (SLR)

From Cisco IOS XE Gibraltar 16.12.1 (Unified SRST/Unified E-SRST12.6), Specific License Reservation (SLR) is supported on Cisco 4000 Series Integrated Services Routers. For more information, see Cisco Unified SCCP and SIP SRST System Administrator Guide (All Versions) .

## Caveats

- Open Caveats—Unified SRST, Release 12.6

### Open Caveats—Unified SRST, Release 12.6

Unified Secure SRST 12.6 (Cisco IOS XE Gibraltar 16.11.1a Release) is not a recommended release version for:

- Unified Secure SCCP SRST and secure call flows that include stcapp configuration

- Multicast Music On Hold

The following are the open or unresolved caveats for Unified SRST, 12.6 Release in Cisco IOS XE Gibraltar 16.11.1a Release.

Caveat

Description

CSCvo04856

DataPlane (DP) crash observed in MMOH call flow

CSCvo00221

Crash observed on secure SRST with Secure SCCP and STCAPP configurations

The following are the open or unresolved caveats for Unified SRST, 12.6 Release in Cisco IOS XE Gibraltar 16.12.1 Release.

Caveat

Description

CSCvw00301

For Cisco 4000 Series Integrated Services Routers in Specific License Reservation (SLR) mode, license status is displayed as AUTHORIZED though more license than reserved is consumed.

## Service and Support

The Cisco Support and Documentation website provide online resources to download documentation, software, and tools. Use these resources to install and configure the software and to troubleshoot and resolve technical issues with Cisco products and technologies.

Access to most tools on the Cisco Support and Documentation website requires a Cisco.com user ID and password.

To access the website, go to: http://www.cisco.com/cisco/web/support/index.html .

## Obtain Documentation and Submit a Service Request

For information on obtaining documentation, using the Cisco Bug Search Tool (BST), submitting a service request, and gathering additional information, see What’s New in Cisco Product Documentation .

To receive new and revised Cisco technical content directly to your desktop, you can subscribe to the What’s New in Cisco Product Documentation RSS feed . The RSS feeds are a free service.

### Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1721R)

Any Internet Protocol (IP) addresses and phone numbers used in this document are not intended to be actual addresses and phone numbers. Any examples, command display output, network topology diagrams, and other figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses or phone numbers in illustrative content is unintentional and coincidental. © 2019 Cisco Systems, Inc. All rights reserved.

### This Document Applies to These Products

- Unified Survivable Remote Site Telephony

| Caveat | Description |
|---|---|
| CSCvo04856 | DataPlane (DP) crash observed in MMOH call flow |
| CSCvo00221 | Crash observed on secure SRST with Secure SCCP and STCAPP configurations |

| Caveat | Description |
|---|---|
| CSCvw00301 | For Cisco 4000 Series Integrated Services Routers in Specific License Reservation (SLR) mode, license status is displayed as AUTHORIZED though more license than reserved is consumed. |