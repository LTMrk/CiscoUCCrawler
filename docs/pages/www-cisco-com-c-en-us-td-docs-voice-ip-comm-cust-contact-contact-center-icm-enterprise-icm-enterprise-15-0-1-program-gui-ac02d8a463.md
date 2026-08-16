---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-ac02d8a463
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/ucce_b_cisco-unified-contact-center-enterprise-developer-reference-release-15-0/ucce-m-1501-call-type-config-summary-api.html
retrieved_at: 2026-08-16T20:17:20.431736+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: December 10, 2025

Chapter: Call Type Config Summary API

## Chapter: Call Type Config Summary API

- Call Type Config Summary API

- Call Type Config Summary API

# Call Type Config Summary API

## Call Type Config Summary API

Call Type Config Summary API provides a report of number of Call Types that are configured with AI features.

If default CCAI configuration is already set, Call types that are not configured with any AI features are counted against
                           the default configuration.

### URL

https://<server>/unifiedconfig/config/contactcenterai/configsummary/calltype

### Operations

GET : Returns Call Type AI configuration summary

### Example Get Response

```
<callTypeConfigSummary>
    <totalCallTypes>4269</totalCallTypes>
    <aiConfigList>
        <callTypeCountByAiConfig>
            <aiConfig>Webex CCAI Config</aiConfig>
            <callTypeCount>4266</callTypeCount>
        </callTypeCountByAiConfig>
        <callTypeCountByAiConfig>
            <aiConfig>GoogleConf2</aiConfig>
            <callTypeCount>2</callTypeCount>
        </callTypeCountByAiConfig>
        <callTypeCountByAiConfig>
            <aiConfig>GoogleConf1</aiConfig>
            <callTypeCount>1</callTypeCount>
        </callTypeCountByAiConfig>
    </aiConfigList>
    <aiConnectorList>
        <callTypeCountByAiConnector>
            <aiConnector>Google</aiConnector>
            <callTypeCount>3</callTypeCount>
        </callTypeCountByAiConnector>
        <callTypeCountByAiConnector>
            <aiConnector>Cisco</aiConnector>
            <callTypeCount>4266</callTypeCount>
        </callTypeCountByAiConnector>
    </aiConnectorList>
</callTypeConfigSummary>
```