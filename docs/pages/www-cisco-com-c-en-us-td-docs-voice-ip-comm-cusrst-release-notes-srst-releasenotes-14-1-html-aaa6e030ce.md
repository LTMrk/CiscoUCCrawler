---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-release-notes-srst-releasenotes-14-1-html-aaa6e030ce
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/release/notes/SRST_ReleaseNotes_14_1.html
retrieved_at: 2026-08-21T21:28:43.805352+00:00
---

Release Notes for Cisco Unified Survivable Remote Site Telephony, 14.1

# Release Notes for Cisco Unified Survivable Remote Site Telephony, 14.1

### Download Options

## Table of Contents

Release Notes for Cisco Unified Survivable Remote Site Telephony, Release 14.1

Contents

Introduction

System Requirements

Hardware Supported

Platforms

Software Compatibility

Determining the Software Version

Upgrading to a New Software Release

Feature Set Tables

New and Changed Information

New Features in Unified SRST, Release 14.1

Support for Unified SRST on Cisco 1100 Series Integrated Services Router Platforms

Support for Unified SRST on Cisco 8200L Catalyst Edge Series Platforms

Support for Unified SRST on Cisco 8200 Catalyst Edge Series Platforms

Support for Unified SRST on Cisco 8300 Catalyst Edge Series Platforms

Support for Cisco Smart Licensing Using Policy for Unified SRST

Support for YANG Model for SRST CLIs

Caveats

Open Caveats—Unified SRST, Release 14.1

Related Documentation

Software Documents

Service and Support

Obtain Documentation and Submit a Service Request

First Published: December 18, 2020

Last Updated: August 16, 2021

## Introduction

This Release Notes document describes the features of Cisco Unified Survivable Remote Site Telephony, Release 14.1. The Cisco Unified Survivable Remote Site Telephony, Release 14.1 is included in Cisco IOS XE Amsterdam 17.3.2 and later releases.

To ensure that you have the latest version of this Release Notes, go to https://www.cisco.com/c/en/us/products/unified-communications/unified-survivable-remote-site-telephony/index.html . Choose Release and General Information > Release Notes, and locate the latest release notes pertaining to your release.

## System Requirements

Hardware Supported

### Hardware Supported

### Platforms

The following Cisco 4000 Series Integrated Services Router platforms support Unified SRST 14.1 from Cisco IOS XE Amsterdam 17.3.2:

- Cisco 4321 Integrated Services Router

- Cisco 4331 Integrated Services Router

- Cisco 4351 Integrated Services Router

- Cisco 4431 Integrated Services Router

- Cisco 4451 Integrated Services Router

- Cisco 4461 Integrated Services Router

The following Cisco 8300 Catalyst Edge Series platforms support Unified SRST 14.1 from Cisco IOS XE Amsterdam 17.3.2:

- C8300-1N1S-6T

- C8300-1N1S-4T2X

- C8300-2N2S-6T

- C8300-2N2S-4T2X

The following Cisco 8200 Catalyst Edge Series platform support Unified SRST 14.1 from Cisco IOS XE Bengaluru 17.4.1a:

- C8200-1N-4T

The following router platforms support Unified SRST 14.1 from Cisco IOS XE Bengaluru 17.5.1a:

- Cisco 1100 Series Integrated Services Router

- C8200L-1N-4T

### Software Compatibility

For more information on supported images and minimum software version requirement for Unified SRST features, see Cisco Unified SCCP and SIP SRST System Administrator Guide .

To determine the correct Cisco IOS release to support a specific Unified SRST version, see the Cisco Unified CME, Unified SRST, and Cisco IOS Software Version Compatibility Matrix .

Use Cisco Feature Navigator to find information about platform support and Cisco IOS software image support. To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn . You do not need an account on Cisco.com for access.

### Determining the Software Version

To determine the release of Cisco IOS software currently running on your Cisco router, log in to the router and enter the show version command. The following sample output from the show version command indicates the Cisco IOS release on the first output line:

Router-4400# show version

Cisco IOS XE Software, Version Cisco IOS XE 17.5.1a

Cisco IOS Software, ISR Software (X86_64_LINUX_IOSD-UNIVERSALK9-M),

Copyright (c) 1986-2021 by Cisco Systems, Inc.

Compiled Fri 2-Feb-21 01:12.

### Upgrading to a New Software Release

To determine which Cisco IOS software release supports the recommended Unified SRST version, see Unified SRST and Cisco IOS Software Compatibility Matrix . To install the new software release, see the “Install Cisco IOS Software” section of the Cisco Unified Communications Manager Express Administrator Guide .

### Feature Set Tables

Use Cisco Feature Navigator to find information about platform support and software image support. Cisco Feature Navigator enables you to determine which software images support a specific software release, feature set, or platform. To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn .

## New and Changed Information

- New Features in Unified SRST, Release 14.1

### Support for Unified SRST on Cisco 1100 Series Integrated Services Router Platforms

From Cisco IOS XE Bengaluru 17.5.1a Support for Unified SRST on Cisco 1100 Series Integrated Services Router platforms, Release 14.1. For more information, see Cisco Unified SCCP and SIP SRST System Administrator Guide

### Support for Unified SRST on Cisco 8200L Catalyst Edge Series Platforms

From Cisco IOS XE Bengaluru 17.5.1a Support for Unified SRST on Cisco 8200L Catalyst Edge Series Platform is being introduced from Unified SRST, Release 14.1. For more information, see Unified SRST/E-SRST 14.1 Supported Firmware, Platforms, Memory, and Voice Products .

### Support for Unified SRST on Cisco 8200 Catalyst Edge Series Platforms

From Cisco IOS XE Amsterdam 17.4.1a Support for Unified SRST on Cisco 8200 Catalyst Edge Series Platform is being introduced from Unified SRST, Release 14.1. For more information, see Cisco Unified SCCP and SIP SRST System Administrator Guide (All Versions) .

### Support for Unified SRST on Cisco 8300 Catalyst Edge Series Platforms

From Cisco IOS XE Amsterdam 17.3.2 Support for Unified SRST on Cisco 8300 Catalyst Edge Series Platforms is being introduced from Unified SRST, Release 14.1. For more information, see Cisco Unified SCCP and SIP SRST System Administrator Guide (All Versions) .

### Support for Cisco Smart Licensing Using Policy for Unified SRST

Support for Cisco Smart Licensing Using Policy for Unified SRST is being introduced from Unified SRST, Release 14.1. For more information, see Cisco Unified SCCP and SIP SRST System Administrator Guide (All Versions) .

### Support for YANG Model for SRST CLIs

From Cisco IOS XE Bengaluru 17.6.1a onwards, YANG models for Class of Restriction configuration are supported:

- dial-peer voice <tag> pots/voip corlist

- dial-peer voice vad

- dial-peer cor custom name <string>

- dial-peer cor list <string> member <string>

- voice num-exp <string1> <string2>

- voice register pool <string>  [no] cor {incoming | outgoing} cor-list-name {cor-list-number starting-number [- ending-number] | default}

For more information, see Programmability Guide for Cisco IOS XE Unified Communications VoIP Products .

## Caveats

- Open Caveats—Unified SRST, Release 14.1

### Open Caveats—Unified SRST, Release 14.1

There are no open or unresolved caveats for Unified SRST, 14.1 Release.

## Service and Support

The Cisco Support and Documentation website provide online resources to download documentation, software, and tools. Use these resources to install and configure the software and to troubleshoot and resolve technical issues with Cisco products and technologies.

Access to most tools on the Cisco Support and Documentation website requires a Cisco.com user ID and password.

To access the website, go to: http://www.cisco.com/cisco/web/support/index.html .

## Obtain Documentation and Submit a Service Request

For information on obtaining documentation, using the Cisco Bug Search Tool (BST), submitting a service request, and gathering additional information, see What’s New in Cisco Product Documentation .

To receive new and revised Cisco technical content directly to your desktop, you can subscribe to the What’s New in Cisco Product Documentation RSS feed . The RSS feeds are a free service.

### Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1721R)

Any Internet Protocol (IP) addresses and phone numbers used in this document are not intended to be actual addresses and phone numbers. Any examples, command display output, network topology diagrams, and other figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses or phone numbers in illustrative content is unintentional and coincidental. © 2021 Cisco Systems, Inc. All rights reserved.

### Let Us Help