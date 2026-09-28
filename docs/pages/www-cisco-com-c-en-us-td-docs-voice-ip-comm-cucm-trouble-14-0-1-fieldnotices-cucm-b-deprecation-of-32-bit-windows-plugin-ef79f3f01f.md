---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-trouble-14-0-1-fieldnotices-cucm-b-deprecation-of-32-bit-windows-plugin-ef79f3f01f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/trouble/14_0_1/fieldNotices/cucm_b_deprecation-of-32-bit-windows-plugin-support-tapi-cucm.html
retrieved_at: 2026-08-16T17:50:36.791414+00:00
---

Deprecation of 32-Bit Windows Plugin Support for Cisco TAPI Service Provider in Cisco Unified Communications Manager

# Deprecation of 32-Bit Windows Plugin Support for Cisco TAPI Service Provider in Cisco Unified Communications Manager

### Download Options

Updated: February 5, 2026

# Deprecation of 32-Bit Windows Plugin Support for Cisco TAPI Service Provider in Cisco Unified Communications Manager

## Overview

Cisco Unified Communications Manager does not support Cisco TAPI Service Provider (TSP) 32-bit Windows plugin.

THIS ADVISORY IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY
                  OF MERCHANTABILITY. YOUR USE OF THE INFORMATION OR MATERIALS LINKED FROM THE ADVISORY IS AT YOUR OWN RISK. CISCO RESERVES
                  THE RIGHT TO CHANGE OR UPDATE THIS ADVISORY AT ANY TIME.

## Products Affected

Products Affected

Version

Cisco Unified Communications Manager

14SU5

Cisco Unified Communications Manager

15SU4

## Problem Description

The following feature is deprecated and is not supported by Cisco Unified Communications Manager (Unified Communications Manager)
                  for the version mentioned above:

32-bit Windows plugin support for Cisco TAPI Service Provider

## Background

Microsoft has announced the end of support for the following Windows platforms that supported 32-bit versions:

Windows 10 will reach end of support on October 14, 2025. As of January 10, 2023, computers running Windows 8.1 no longer
                        receive security updates from Microsoft.

Support for Windows 7 has been discontinued. Microsoft customer service no longer provides technical assistance, and PCs running
                        Windows 7 will not receive security updates.

There is no 32-bit version of Windows 11 or later; Windows 11 is only available in a 64-bit version.

## Problem / Symptom

The 32-bit plugin for Cisco TAPI Service Provider (TSP) does not work on Windows 10, Windows 8.1, or Windows 7.

## Product Migration Options

Customers are encouraged to migrate to the 64-bit plugin version of Cisco TAPI Service Provider (TSP) on supported Windows
                  platforms.

https://developer.cisco.com/site/tapi/supported-windows-os

## Opening a Case with TAC

If you require further assistance, or if you have any further questions regarding this field notice, contact Cisco Systems Technical Assistance Center (TAC) by one of the following methods:

Open a Service Request on cisco.com

By Email

By Telephone

| Products Affected | Version |
|---|---|
| Cisco Unified Communications Manager | 14SU5 |
| Cisco Unified Communications Manager | 15SU4 |