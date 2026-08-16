---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-trouble-15-fieldnotices-cucm-b-deprecated-ccd-cucm-html-7c8c067b25
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/trouble/15/fieldNotices/cucm_b_deprecated-ccd-cucm.html
retrieved_at: 2026-08-16T17:50:49.440507+00:00
---

Deprecation of Call Control Discovery via Service Advertisement Framework in Cisco Unified Communications Manager

# Deprecation of Call Control Discovery via Service Advertisement Framework in Cisco Unified Communications Manager

### Download Options

Updated: July 29, 2025

# Deprecation of Call Control Discovery via Service Advertisement Framework in Cisco Unified Communications Manager

## Overview

Cisco Unified Communications Manager does not support Call Control Discovery via Service Advertisement Framework.

THIS ADVISORY IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY
                  OF MERCHANTABILITY. YOUR USE OF THE INFORMATION OR MATERIALS LINKED FROM THE ADVISORY IS AT YOUR OWN RISK. CISCO RESERVES
                  THE RIGHT TO CHANGE OR UPDATE THIS ADVISORY AT ANY TIME.

## Products Affected

Products Affected

Version

Cisco Unified Communications Manager

12.5.x

Cisco Unified Communications Manager

14 and SUs

Cisco Unified Communications Manager

15 and SUs

## Problem Description

The following feature is deprecated and is no longer supported by Cisco Unified Communications Manager (Unified Communications
                  Manager) for the versions mentioned earlier.

Call Control Discovery via Service Advertisement Framework

## Background

The Service Advertisement Framework (SAF) acts as the communication backbone in Cisco's Intelligent WAN (IWAN) solution and
                  is used by Performance Routing (PfR) to distribute policies and configurations from a central hub to all participating routers.
                  SAF ensures that all routers within the IWAN domain—including both hub and branch routers—have a consistent understanding
                  of routing policies, monitoring configurations, and other relevant settings.

Cisco IWAN is End of Life (EOL): EOL Announcement . Cisco’s SD-WAN solution is the recommended migration option for customers.

Call Control Discovery (CCD) with SAF as the communication backbone is used to advertise Unified Communications Manager information
                  along with other key attributes, such as directory number patterns. Other call control entities that utilize the SAF network
                  can use the advertised information to dynamically configure and adapt their routing operations.

## Problem / Symptom

Cisco Unified Communications Manager configured as an SAF Client and Cisco IOS routers configured as SAF Forwarders will no
                  longer work and are not supported.

## Product Migration Options / Recommendations

Customers are encouraged to migrate to Global Dial Plan Replication via the Intercluster Lookup Service (ILS), which is the
                  recommended feature.

For more information, see the System Configuration Guide for Cisco Unified Communications Manager .

## Opening a Case with TAC

If you require further assistance, or if you have any further questions regarding this field notice, contact Cisco Systems Technical Assistance Center (TAC) by one of the following methods:

Open a Service Request on cisco.com

By Email

By Telephone

| Products Affected | Version |
|---|---|
| Cisco Unified Communications Manager | 12.5.x |
| Cisco Unified Communications Manager | 14 and SUs |
| Cisco Unified Communications Manager | 15 and SUs |