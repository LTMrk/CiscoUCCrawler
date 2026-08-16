---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-trouble-15-fieldnotices-cucm-b-deprecated-rcc-15-html-2c9f468afe
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/trouble/15/fieldNotices/cucm_b_deprecated-rcc-15.html
retrieved_at: 2026-08-16T17:50:53.319660+00:00
---

Deprecation of Remote Call Control with Microsoft Lync Server for IM and Presence Service on Cisco Unified Communications Manager, Release 15

# Deprecation of Remote Call Control with Microsoft Lync Server for IM and Presence Service on Cisco Unified Communications Manager, Release 15

### Download Options

Updated: May 11, 2026

# Deprecation of Remote Call Control with Microsoft Lync Server for IM and Presence Service on Cisco Unified Communications
            Manager, Release 15

## Overview

Cisco Unified Communications Manager Release 15 does not support Remote Call Control with Microsoft Lync Server for IM and
                  Presence Service.

THIS ADVISORY IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY
                  OF MERCHANTABILITY. YOUR USE OF THE INFORMATION OR MATERIALS LINKED FROM THE ADVISORY IS AT YOUR OWN RISK. CISCO RESERVES
                  THE RIGHT TO CHANGE OR UPDATE THIS ADVISORY AT ANY TIME.

## Products Affected

Products Affected

Version

Cisco Unified Communications Manager

15

Cisco Unified Communications Manager IM and Presence Service

15

Cisco Business Edition 6000

15

Cisco Business Edition 7000

15

## Problem Description

The Remote Call Control feature is deprecated and isn't supported by the products mentioned above in Release 15. If you are
                  using this feature currently in your deployment and you are trying to upgrade to Release 15, you won't be able to use this
                  feature after the upgrade.

For more information on Remote Call Control, see Remote Call Control with Microsoft Lync Server for IM and Presence Service .

## Background

The Remote Call Control with Microsoft Lync Server feature is deprecated as Microsoft Lync Server 2013 is past Microsoft’s
                  Mainstream End of Support (EOS) dated April 10, 2018 and also extended EOS dated April 11, 2023.

For more information, see https://learn.microsoft.com/en-us/lifecycle/products/microsoft-lync-server-2013 .

## Problem / Symptom

The IM and Presence Service Release 15, deprecated its CTI gateway functionality and can no longer listen for CSTA session
                  requests or maintain active telephony connections. After upgrading to Release 15, Lync 2013 and Skype for Business (SfB) clients
                  cannot control Cisco Unified IP Phones.

## Recommendation

For organizations that prefer to maintain their existing on-premises infrastructure, Cisco Jabber offers a robust solution
                  for controlling Cisco Unified IP Phones. Customers can optimize their current environment by transitioning from Microsoft
                  Lync 2013 / Skype for Business (SfB) to Cisco Jabber. To achieve this, organizations are required to perform the following
                  steps:

Client Migration —Replace the existing Microsoft Lync 2013 / Skype for Business (SfB) application with the Cisco Jabber application to enable
                        integrated call control.

Server Reconfiguration —Reconfigure the existing IM and Presence servers to operate in the standard IM and Presence mode, with Directory URI addressing
                        scheme.

## Product Migration Options

Alternatively, organizations are encouraged to migrate to the Cisco Webex App, the cloud-based unified collaboration platform.

## Opening a Case with TAC

If you require further assistance, or if you have any further questions regarding this field notice, contact Cisco Systems Technical Assistance Center (TAC) by one of the following methods:

Open a Service Request on cisco.com

By Email

By Telephone

## Receive Email Notification for New Field Notices

Cisco Notification Service —Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco
                  products you specify.

### This Document Applies to These Products

- Unified Communications Manager Version 15

| Products Affected | Version |
|---|---|
| Cisco Unified Communications Manager | 15 |
| Cisco Unified Communications Manager IM and Presence Service | 15 |
| Cisco Business Edition 6000 | 15 |
| Cisco Business Edition 7000 | 15 |