---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-installandupgrade-816a1b2b6d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/installandupgrade/guide/ccvp_b_1261-installation-and-upgrade-guide-for-cisco-unified-customer-voice-portal/ccvp_b_1252-installation-and-upgrade-guide-for-cisco-unified-customer-voice-portal_chapter_0111.html
retrieved_at: 2026-08-21T17:04:10.476601+00:00
---

Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

# Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

Updated: May 14, 2021

Chapter: Unified CVP Migration

## Chapter: Unified CVP Migration

- Unified CVP Migration

- Migrate Unified CVP to Windows Server 2019

# Unified CVP Migration

## Migrate Unified CVP to Windows Server 2019

The following table lists the migration paths to replace the existing Unified CVP version with the MR on Windows Server 2019.

Unified CVP

12.5(1) to 12.6(1)

Yes

First install Unified CVP 12.5(1) on Windows Server 2019. Then upgrade to Unified CVP 12.6(1) through MR.

.NET framework must be installed before installing Unified CVP 12.5(1).

Platform change is required.

Unified CVP

12.5(1b) to 12.6(1)

Yes

First install Unified CVP 12.5(1b) on Windows Server 2019. Then upgrade to Unified CVP 12.6(1) through MR.

.NET framework must be installed before installing Unified CVP 12.5(1b).

Platform change is required.

The steps to be followed for installing Windows Server 2019 are the same as the steps for installing Windows Server 2016.

For migration to Windows Server 2019, refer to the Unified CVP Migration chapter in the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.5(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html .

Inline upgrade to 12.6(1) on Windows Server 2019 is not supported.

If the installer gives a Windows Server warning regarding the configured guest OS on the virtual machine, ignore it.

It is recommended to use the OVA file CVP_12.6_Windows_vmv13_v8.0.ova . available at https://software.cisco.com/download/home/270563413/type/280840592/release/12.6(1) .

For installing Unified CVP 12.5 on Windows Server 2019, refer to the Unified CVP Installation section in the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.5(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html .

| Migration Path from Older Release to New Release | Platform Change | Conversion Process | Description |
|---|---|---|---|
| Unified CVP 12.5(1) to 12.6(1) | Yes | First install Unified CVP 12.5(1) on Windows Server 2019. Then upgrade to Unified CVP 12.6(1) through MR. Note .NET framework must be installed before installing Unified CVP 12.5(1). | Note | .NET framework must be installed before installing Unified CVP 12.5(1). | Platform change is required. |
| Note | .NET framework must be installed before installing Unified CVP 12.5(1). |
| Unified CVP 12.5(1b) to 12.6(1) | Yes | First install Unified CVP 12.5(1b) on Windows Server 2019. Then upgrade to Unified CVP 12.6(1) through MR. Note .NET framework must be installed before installing Unified CVP 12.5(1b). | Note | .NET framework must be installed before installing Unified CVP 12.5(1b). | Platform change is required. |
| Note | .NET framework must be installed before installing Unified CVP 12.5(1b). |

| Note | .NET framework must be installed before installing Unified CVP 12.5(1). |
|---|---|

| Note | .NET framework must be installed before installing Unified CVP 12.5(1b). |
|---|---|

| Note | The steps to be followed for installing Windows Server 2019 are the same as the steps for installing Windows Server 2016. |
|---|---|

| Note | Inline upgrade to 12.6(1) on Windows Server 2019 is not supported. If the installer gives a Windows Server warning regarding the configured guest OS on the virtual machine, ignore it. It is recommended to use the OVA file CVP_12.6_Windows_vmv13_v8.0.ova . available at https://software.cisco.com/download/home/270563413/type/280840592/release/12.6(1) . . |
|---|---|