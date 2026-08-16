---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-89ffe517aa
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_01011.html
retrieved_at: 2026-08-16T17:30:12.552003+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure SIP Profiles

## Chapter: Configure SIP Profiles

- Configure SIP Profiles

- SIP Profile Overview

- Configure SIP Profiles

# Configure SIP Profiles

## SIP Profile Overview

A SIP Profile is a template that comprises common SIP settings. If you are deploying SIP devices or SIP trunks in your network,
                           you can apply common SIP settings to groups of devices through the SIP Profile. You can configure multiple profiles for groups
                           of SIP endpoints. You can choose from a variety of default SIP Profiles or create your own.

Without the SIP Profile, you would have to configure SIP settings individually for every SIP trunk and SIP device in your
                           network. However, you can use the SIP profile to assign many SIP settings, such as the following:

MTP Telephony Payload Types

SIP header details

Timers and counters for SIP messages

SDP transparency profiles for SDP interoperability

SIP Normalization and Transparency scripts for SIP lines

SIP OPTIONS settings

SIP Early Offer support

Call Pickup URIs

## Configure SIP Profiles

Use this procedure to configure a SIP profile with common SIP settings that you can assign to SIP devices and trunks that
                              use this profile.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > SIP Profile .

Step 2

Perform one of the following steps:

- Click Find and select the SIP profile to edit an existing profile, .

- Click Add New to create a new profile.

Step 3

If you want your SIP phones and trunks to support IPv4 and IPv6 stacks, check the Enable ANAT check box.

Step 4

If you want to assign an SDP transparency profile to resolve SDP interoperability, from the SDP Transparency Profile drop-down list.

Step 5

If you want to assign a normalization or transparency script to resolve SIP interoperability issues, from the Normalization Script drop-down list, select the script.

Step 6

(Optional) Check the Send ILS Learned Destination Route String check box for Global Dial Plan Replication deployments where you may need to route calls across a Cisco Unified Border Element.

Step 7

Complete the remaining fields in the SIP Profile Configuration window. For more information on the fields and their configuration options, see Online Help.

Step 8

Click Save .

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > SIP Profile . |
|---|---|
| Step 2 | Perform one of the following steps: Click Find and select the SIP profile to edit an existing profile, . Click Add New to create a new profile. |
| Step 3 | If you want your SIP phones and trunks to support IPv4 and IPv6 stacks, check the Enable ANAT check box. |
| Step 4 | If you want to assign an SDP transparency profile to resolve SDP interoperability, from the SDP Transparency Profile drop-down list. |
| Step 5 | If you want to assign a normalization or transparency script to resolve SIP interoperability issues, from the Normalization Script drop-down list, select the script. |
| Step 6 | (Optional) Check the Send ILS Learned Destination Route String check box for Global Dial Plan Replication deployments where you may need to route calls across a Cisco Unified Border Element. |
| Step 7 | Complete the remaining fields in the SIP Profile Configuration window. For more information on the fields and their configuration options, see Online Help. |
| Step 8 | Click Save . |