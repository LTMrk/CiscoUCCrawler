---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-trouble-15-fieldnotices-cucm-b-deprecated-h323-15-html-4c08c6c459
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/trouble/15/fieldNotices/cucm_b_deprecated-h323-15.html
retrieved_at: 2026-08-16T17:51:01.692714+00:00
---

Deprecation of H.323 Gatekeeper Control Options in Cisco Unified Communications Manager Release 15

# Deprecation of H.323 Gatekeeper Control Options in Cisco Unified Communications Manager Release 15

### Download Options

Updated: December 19, 2023

# Deprecation of H.323 Gatekeeper Control Options in Cisco Unified Communications Manager, Release 15

## Overview

Cisco Unified Communications Manager Release 15 does not support the H.323 Gatekeeper Control options.

THIS ADVISORY IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY
                  OF MERCHANTABILITY. YOUR USE OF THE INFORMATION OR MATERIALS LINKED FROM THE ADVISORY IS AT YOUR OWN RISK. CISCO RESERVES
                  THE RIGHT TO CHANGE OR UPDATE THIS ADVISORY AT ANY TIME.

## Products Affected

Products Affected

Version

Cisco Unified Communications Manager

15

## Problem Description

The following feature is deprecated and is not supported by Cisco Unified Communications Manager (Unified Communications Manager),
                  Release 15. If you are using this feature currently in your deployment and you are trying to upgrade to Release 15, you will
                  not be able to use this feature after the upgrade.

H.323 Gatekeeper Control options

## Background

Unified Communications Manager has provided support for H.323 call control signaling since the introduction of voice features
                  about 20 years ago. Currently, customers use the Session Initiation Protocol (SIP) for multimedia session control and hence
                  minimal demand for the H.323 functionality.

In acknowledgement of this reduced demand, Unified Communications Manager will not provide support for the H.323 Gatekeeper
                  Control options from Release 15 onwards.

Also the H.323 call control features in Cisco IOS XE Software are past the End of SW Maintenance Release dated May 30, 2022.
                  For more information, see https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/bulletin-c25-2479306.html .

## Problem / Symptom

If you are using this feature currently in your deployment and you are trying to upgrade to Release 15, you will not be able
                  to use this feature after the upgrade.

H.323 gateways and H.323 protocol continue to be supported.

## Product Migration Options

Customers are encouraged to migrate to SIP trunk with Location Bandwidth Manager (LBM).

For more information, see the System Configuration Guide for Cisco Unified Communications Manager, Release 15 .

## Opening a Case with TAC

If you require further assistance, or if you have any further questions regarding this field notice, contact Cisco Systems Technical Assistance Center (TAC) by one of the following methods:

Open a Service Request on cisco.com

By Email

By Telephone

### This Document Applies to These Products

- Unified Communications Manager Version 15

| Products Affected | Version |
|---|---|
| Cisco Unified Communications Manager | 15 |

| Note | H.323 gateways and H.323 protocol continue to be supported. |
|---|---|