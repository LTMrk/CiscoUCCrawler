---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-cd5b14e6d8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/ucce_b_cisco-unified-contact-center-enterprise-developer-reference-release-15-0/ucce-m-1501-config-summary-api.html
retrieved_at: 2026-08-16T20:17:24.946529+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: December 10, 2025

Chapter: Config Summary API

## Chapter: Config Summary API

- Config Summary API

- Config Summary API

# Config Summary API

## Config Summary API

Config Summary API provides a report of number of Agents and Call types that use AI features and configurations.

If default CCAI configuration is already set, Call types that are not configured with any AI features are counted against
                           the default configuration.

### URL

https://<server>/unifiedconfig/config/contactcenterai/configsummary

### Operation

GET : Returns both Agent and Call type AI configuration summaries.

### Example Get Response

```
<aiConfigSummary>
    <agentConfigSummary>
        <totalAgents>982</totalAgents>
        <agentsWithFeatures>69</agentsWithFeatures>
        <featureList>
            <agentCountByFeature>
                <agentCount>67</agentCount>
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
    <callTypeConfigSummary>
        <totalCallTypes>4269</totalCallTypes>
        <aiConfigList>
            <callTypeCountByAiConfig>
                <aiConfig>Webex CCAI Config</aiConfig>
                <callTypeCount>4266</callTypeCount>
            </callTypeCountByAiConfig>
            <callTypeCountByAiConfig>
                <aiConfig>GoogleConf2</aiConfig>
                <callTypeCount>1</callTypeCount>
            </callTypeCountByAiConfig>
            <callTypeCountByAiConfig>
                <aiConfig>GoogleConf1</aiConfig>
                <callTypeCount>1</callTypeCount>
            </callTypeCountByAiConfig>
        </aiConfigList>
        <aiConnectorList>
            <callTypeCountByAiConnector>
                <aiConnector>Google</aiConnector>
                <callTypeCount>2</callTypeCount>
            </callTypeCountByAiConnector>
            <callTypeCountByAiConnector>
                <aiConnector>Cisco</aiConnector>
                <callTypeCount>4266</callTypeCount>
            </callTypeCountByAiConnector>
        </aiConnectorList>
    </callTypeConfigSummary>
</aiConfigSummary>
```