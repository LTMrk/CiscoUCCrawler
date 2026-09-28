---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-program-gui-b74dc5bb31
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/program/guide/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5_chapter_011000.html
retrieved_at: 2026-08-16T20:29:05.743869+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

Updated: February 6, 2020

Chapter: Single Sign-On Global State API

## Chapter: Single Sign-On Global State API

- Single Sign-On Global State API

- Single Sign-On Global State API

# Single Sign-On Global State API

## Single Sign-On Global State API

Use the Single Sign-On (SSO) Global State API to view or update the global status of SSO.

To retrieve the overall status of setting the SSO state or the status for a single component, see the Single Sign-On Status API .

### URL

https://<server>/unifiedconfig/config/sso/globalstate

### Operations

get : Returns the current global state of SSO in the database.

update : Updates the global state of SSO in the database.

### Parameters

refURL: The RefURL. See Shared Parameters .

changeStamp: See Shared Parameters .

permissionInfo: Information about permissions.

canUpdate: Whether ssoState can be updated. True or false.

role: The role of the user.

state: Required for update.  Valid values are NON_SSO (SSO is disabled for all users), SSO (SSO is enabled for all users),
                                    and HYBRID (mix of enabled and disabled).

### Example Get Response

```
<ssoState>
    <refURL>/ssostate</refURL>
    <changeStamp>227</changeStamp>
    <permissionInfo>
        <canUpdate>true</canUpdate>
        <role>Administrator</role>
    </permissionInfo>
    <state>SSO</state>
</ssoState>
```