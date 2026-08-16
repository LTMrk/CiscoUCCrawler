---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-dfa375aab9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/ucce_b_cisco-unified-contact-center-enterprise-developer-reference-release-15-0/ucce-m-1501-agent-config-summary-api.html
retrieved_at: 2026-08-16T20:14:45.158388+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: December 10, 2025

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