---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-81ea9e0030
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_single-sign-on-global-state-api_1501.html
retrieved_at: 2026-08-21T16:48:20.236126+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

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