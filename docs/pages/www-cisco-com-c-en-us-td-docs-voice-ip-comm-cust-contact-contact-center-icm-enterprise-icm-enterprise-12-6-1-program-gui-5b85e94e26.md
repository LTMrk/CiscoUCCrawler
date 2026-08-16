---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-program-gui-5b85e94e26
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/program/guide/ucce_b_cisco-ucce_developer_guide-12_6_1/ucce_b_cisco-ucce_developer_guide-12_6_1_chapter_011101.html
retrieved_at: 2026-08-16T20:23:32.349894+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(1)

Updated: August 21, 2023

Chapter: Single Sign-On Registration API

## Chapter: Single Sign-On Registration API

- Single Sign-On Registration API

- Single Sign-On Registration API

# Single Sign-On Registration API

## Single Sign-On Registration API

Use the Single Sign-On (SSO) Registration API to register SSO-compatible components with the Cisco Identity Service.  These
                           components include AW, Finesse, and Unified Intelligence Center machines.

To retrieve the overall registration status or the status for a single component, see the Single Sign-On Status API .

### URL

https://<server>/unifiedconfig/config/sso/register

### Operations

update : Registers all SSO-compatible components in the Machine Inventory with the Cisco Identity Service, using the URL https://<server>/unifiedconfig/config/sso/register . 
                                    (See Machine Inventory API

### Parameters

None