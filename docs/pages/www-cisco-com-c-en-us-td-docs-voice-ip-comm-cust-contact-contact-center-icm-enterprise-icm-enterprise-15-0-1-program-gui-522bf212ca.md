---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-522bf212ca
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_agent_security_api_1501.html
retrieved_at: 2026-08-21T16:44:59.883743+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Agent Security API

## Chapter: Agent Security API

- Agent Security API

- Agent Security API

# Agent Security API

## Agent Security API

Use the Agent Security API to get and update the status of global switch for generating
                           advanced agent password hashing, and also to clear older agent password hashes from the
                           system.

This API is available for administrators only, applicable for all the deployments, and is
                           not supported in SSO modes.

### URL

https://unifiedconfig/config/agentsecurity

### Operations

get : Returns the secure global
                                    switch value.

https://unifiedconfig/config/agentsecurity?details=true

update : Updates the secure global
                                    switch status and clears the older agent password from the system.

### Parameters

enforceAdvancedHashing: true means, global switch will be enabled and removes older
                              Agent passwords, false means global switch will be disabled.

### Example Get Response

```
<agentSecurity>
     <enforceAdvancedHashing>true</enforceAdvancedHashing>
    <agentsWithoutAdvancedHashing>10</agentsWithoutAdvancedHashing>
    <unsupportedPeripheralGateways>2</unsupportedPeripheralGateways>
</agentSecurity>
```

### Example Update Request

```
<agentSecurity>
    <changeStamp>277</changeStamp>
    <enforceAdvancedHashing>true</enforceAdvancedHashing>
</agentSecurity>
```