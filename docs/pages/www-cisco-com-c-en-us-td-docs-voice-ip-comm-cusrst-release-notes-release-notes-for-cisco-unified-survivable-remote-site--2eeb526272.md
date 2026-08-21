---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-release-notes-release-notes-for-cisco-unified-survivable-remote-site--2eeb526272
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/release/notes/release-notes-for-cisco-unified-survivable-remote-site-telephony.html
retrieved_at: 2026-08-21T21:28:22.811372+00:00
---

Release Notes for Cisco Unified Survivable Remote Site Telephony, 15.0

# Release Notes for Cisco Unified Survivable Remote Site Telephony, 15.0

First Published: December 20, 2025

Last Updated: April 25, 2026

# Release Notes for Cisco Unified Survivable Remote Site Telephony

## Introduction

This Release Notes document describes the features of Cisco Unified Survivable Remote Site Telephony, Release 15.0. The Cisco
                     Unified Survivable Remote Site Telephony, Release 15.0 is included in the following releases:

Cisco IOS XE 17.18.1a

Cisco IOS XE 17.18.2

Cisco IOS XE 26.1.1

To ensure that you have the latest version of this Release Notes, go to https://www.cisco.com/c/en/us/products/unified-communications/unified-survivable-remote-site-telephony/index.html . Choose Release and General Information > Release Notes , and locate the latest release notes pertaining to your release.

## System Requirements

### Hardware Platforms Supported

Unified SRST supports the following Cisco 8300 Series Secure Router platform:

C8375-E-G2 Secure Router with vDSP enabled

Unified SRST supports the following Cisco 4000 Series Integrated Services Router platforms:

Cisco 4321 Integrated Services Router

Cisco 4331 Integrated Services Router

Cisco 4351 Integrated Services Router

Cisco 4431 Integrated Services Router

Cisco 4451 Integrated Services Router

Cisco 4461 Integrated Services Router

Unified SRST supports the following Cisco 8300 Catalyst Edge Series platforms:

C8300-1N1S-6T

C8300-1N1S-4T2X

C8300-2N2S-6T

C8300-2N2S-4T2X

Unified SRST supports the following Cisco 8200 Catalyst Edge Series platform:

C8200-1N-4T

C8200L-1N-4T

Unified SRST also supports the following Router platforms:

Cisco 1100 Series Integrated Services Router (ISR1100 running IOS XE)

Catalyst 8000V

### Software Compatibility

For more information on supported images and minimum software version requirement for Unified SRST features, see Cisco Unified SCCP and SIP SRST System Administrator Guide .

To determine the correct Cisco IOS release to support a specific Unified SRST version, see the Cisco Unified CME, Unified SRST, and Cisco IOS Software Version Compatibility Matrix .

Use Cisco Feature Navigator to find information about platform support and Cisco IOS software image support. To access Cisco
                     Feature Navigator, go to http://www.cisco.com/go/cfn . You do not need an account on Cisco.com for access.

### Determine the Software Version

To determine the release of Cisco IOS software currently running on your Cisco router, log in to the router and enter the show version command. The following sample output from the show version command indicates the Cisco IOS release on the first output line:

```
Device#show version
Cisco IOS XE Software, Version Cisco IOS XE 26.1.1
Cisco IOS Software [IOSXE], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M),
Copyright (c) 1986-2026 by Cisco Systems, Inc.
Compiled Mon 02-Mar-26 20:04
```

### Upgrade to a New Software Release

To determine which Cisco IOS software release supports the recommended Unified SRST version, see Unified SRST and Cisco IOS Software Compatibility Matrix . To install the new software release, see the “Install Cisco IOS Software” section of the Cisco Unified Communications Manager Express Administrator Guide .

### Feature Set Tables

Use Cisco Feature Navigator to find information about platform support and software image support. Cisco Feature Navigator
                     enables you to determine which software images support a specific software release, feature set, or platform. To access Cisco
                     Feature Navigator, go to http://www.cisco.com/go/cfn .

## New and Changed Information

### New Features in Unified SRST, Release 15.0 ( Cisco IOS XE 26.1.1 )

Insecure TLS versions (v1.0, v 1.1) and ciphers are not supported in default configurations. However, these insecure configurations
                           are supported in "system mode insecure" mode.  Support for the following non-compliant ciphers has been discontinued:

DHE_RSA_WITH_AES_256_CBC_SHA

CHACHA20_POLY1305_SHA256

See Configure Secure SRST for SCCP and SIP .

### New Features in Unified SRST, Release 15.0 ( Cisco IOS XE 17.18.2 )

From Unified SRST Release 15.0, support for Unified SRST on Cisco 8300 Series Secure Routers platform. For more information,
                           see Compatibility Information for Unified SRST/E-SRST 15.0 Supported Firmware, Platforms, Memory, and Voice Products .

Security warnings for usage of legacy TLS and associated weaker ciphers. For more information, see Signaling Security on Unified SRST - TLS .

### New Features in Unified SRST, Release 15.0 ( Cisco IOS XE 17.18.1a )

From Unified SRST Release 15.0, smart licensing reports flex subscription entitlement tag. To maintain the continued support
                           and entitlements to the future application versions, purchase a Collaboration Flex subscription. For more information, see Cisco Unified SCCP and SIP SRST System Administrator Guide (All Versions) .

From Unified SRST Release 15.0, support is added for Cisco Desk Phone 9861 (DP-9861) and Cisco Desk Phone 9871 (DP-9871) devices.
                           For more information, see Compatibility Information for Unified SRST/E-SRST 15.0 Supported Firmware, Platforms, Memory, and Voice Products .

## Caveats

### Bug Search Tool

The Bug Search Tool contains information about open and resolved issues for the release, including descriptions of the problems
                     and available workarounds. The identifiers listed in this release notes takes you directly to a description of each issue.

To look for information about a specific issue:

Using a web browser, go to the Bug Search Tool .

Sign in with a cisco.com username and password.

Enter the bug identifier in the Search field and click Search .

To look for information when you do not know the identifier:

Type the product name in the Search field and click Search .

From the list of bugs that appear, use the Filter drop-down list to filter on Keyword, Modified Date, Severity, Status, or Bug Type.

Use Advanced Search on the Bug Search Tool home page for a specific software version. The help pages have further information on using the Bug Search Tool .

### Open and Resolved Issues

Follow the links to read the most recent information about open and resolved issues in SRST release.

Open issues

Resolved issues

## Related Documentation

## Service and Support

The Cisco Support and Documentation website provide online resources to download documentation, software, and tools. Use these
                     resources to install and configure the software and to troubleshoot and resolve technical issues with Cisco products and technologies.

Access to most tools on the Cisco Support and Documentation website requires a Cisco.com user ID and password.

To access the website, go to: http://www.cisco.com/cisco/web/support/index.html .

## Obtain Documentation and Submit a Service Request

For information on obtaining documentation, using the Cisco Bug Search Tool (BST), submitting a service request, and gathering
                     additional information, see What’s New in Cisco Product Documentation .

To receive new and revised Cisco technical content directly to your desktop, you can subscribe to the What’s New in Cisco Product Documentation RSS feed . The RSS feeds are a free service.

This document is to be used in conjunction with the documents listed in the “Related Documentation” section.

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries.
                     To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks. Third-party trademarks mentioned are the
                     property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and
                     any other company. (1721R)

Any Internet Protocol (IP) addresses and phone numbers used in this document are not intended to be actual addresses and phone
                     numbers. Any examples, command display output, network topology diagrams, and other figures included in the document are shown
                     for illustrative purposes only. Any use of actual IP addresses or phone numbers in illustrative content is unintentional and
                     coincidental.

### This Document Applies to These Products

- Unified Survivable Remote Site Telephony