---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-20ab04605d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce-m-1501-agent-config-summary-api.html
retrieved_at: 2026-08-21T16:42:49.572462+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Agent Config Summary API

## Chapter: Agent Config Summary API

- Agent Config Summary API

- Agent Config Summary API

# Agent Config Summary API

## Agent Config Summary API

Agent Config Summary API provides a report of number of Agents that are configured with AI features.

### URL

https://<server>/unifiedconfig/config/contactcenterai/configsummary/agent

### Operations

GET : Returns Agent AI configuration summary

### Example Get Response

```
<agentConfigSummary>
    <totalAgents>982</totalAgents>
    <agentsWithFeatures>70</agentsWithFeatures>
    <featureList>
        <agentCountByFeature>
            <agentCount>68</agentCount>
            <featureId>1</featureId>
        </agentCountByFeature>
        <agentCountByFeature>
            <agentCount>4</agentCount>
            <featureId>2</featureId>
        </agentCountByFeature>
        <agentCountByFeature>
            <agentCount>4</agentCount>
            <featureId>3</featureId>
        </agentCountByFeature>
        <agentCountByFeature>
            <agentCount>1</agentCount>
            <featureId>4</featureId>
        </agentCountByFeature>
    </featureList>
</agentConfigSummary>
```