---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-4b1e35e091
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/ucce_b_cisco-unified-contact-center-enterprise-developer-reference-release-15-0/ucce_m_agent-event-detail-extended.html
retrieved_at: 2026-08-16T20:18:03.106610+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: December 10, 2025

Chapter: GeneralSetting API with Agent Event Detail Extended support

## Chapter: GeneralSetting API with Agent Event Detail Extended support

- GeneralSetting API with Agent Event Detail Extended support

- General Setting API with Agent Event Detail Extended Support

# GeneralSetting API with Agent Event Detail Extended support

## General Setting API with Agent Event Detail Extended Support

You can enable the agent event details from the user instance, thus the value of the AED.AgentEventDetailExtended flag is
                           set to yes on the t_Global_Configuration table. The agent event details can be obtained using the Agent Event Detail Extended
                           API.

### URL

https://<server>/unifiedconfig/config/generalsetting

### Operations

GET : Returns the value of AED.AgentEventDetailExtended set in the t_Global_Configuration table. The returned value is “true”,
                                    if AED.AgentEventDetailExtended is set to “yes". Or else, it returns "false" if its value is set to “no” or if no record is
                                    found.

PUT : Creates the AED.AgentEventDetailsExtended entry in the t_Global_Configuration table if no entry is found. If an entry is
                                    found, it would update the AED.AgentEventDetailsExtended flag value to “yes” or  "no" based on whether the value for “agentEventDetailExtended”
                                    in the request body is “true" or "false”.

### Parameters

agentEventDetailExtended : Indicates whether agent event details are enabled or not.

sessionInactivityTimeout : Indicates the time interval for which a session can be inactive. You can change the session inactivity timer.

generalSettings : You can now change both the session inactivity timer and also change the agentEventDetailExtended flag value.

### Example Get Response

```
<generalSettings>
    <agentEventDetailExtended>true</agentEventDetailExtended>
    <loginSession>
        <sessionInactivityTimeout>30</sessionInactivityTimeout>
    </loginSession>
</generalSettings>
```

### Example Put Response

```
{
    "agentEventDetailExtended": false
}
```