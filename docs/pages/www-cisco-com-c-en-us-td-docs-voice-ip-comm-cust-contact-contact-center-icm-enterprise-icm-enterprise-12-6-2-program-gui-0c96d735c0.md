---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-program-gui-0c96d735c0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/program/guide/ucce_b_cisco-ucce_developer_guide-12-6-2-/pcce_m_general_setting_api_15_0.html
retrieved_at: 2026-08-16T20:20:35.187015+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

Updated: August 21, 2023

Chapter: General Setting API

## Chapter: General Setting API

- General Setting API

- General Setting API

# General Setting API

## General Setting API

GeneralSetting API is introduced to include the session inactivity timeout field. Both GET and PUT are available in all supported
                           deployments.

### URL

### Operations

get : Returns the general settings configured in the system.

put : To update any general setting applicable in the system.

### Parameters

sessioninactivitytimeout: Timeout after which user is logged out if the user is inactive

### Example Get Request

```
<generalSettings>
    <loginSession>
        <sessionInactivityTimeout>
            30
        </sessionInactivityTimeout>
    </loginSession>
</generalSettings>
```

### Example Put Request

```
<generalSettings>
    <loginSession>
        <sessionInactivityTimeout>
            60
        </sessionInactivityTimeout>
    </loginSession>
</generalSettings>
```