---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-program-gui-dfe8deac58
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/program/guide/ucce_b_cisco-ucce_developer_guide-12-6-2-/ucce_m_sso_global_state_api-12_6_1.html
retrieved_at: 2026-08-16T20:21:08.904607+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

Updated: August 21, 2023

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