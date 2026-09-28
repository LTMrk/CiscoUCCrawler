---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-6c1ab2c28d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_stats-api_1501.html
retrieved_at: 2026-08-21T16:48:45.619418+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Stats API

## Chapter: Stats API

- Stats API

- Stats API

# Stats API

## Stats API

Use the Stats API to get statistical information about your deployment, such as the number of logged in agents.

This API is read-only.

### URL

### Operations

get :
                                    				Returns statistical information about your deployment.

### Response Parameters

numberOfAgentsLoggedIn: The number of agents logged in.

### Example Get Response

```
<stats>
    <numberOfAgentsLoggedIn>10</numberOfAgentsLoggedIn>
</stats>
```