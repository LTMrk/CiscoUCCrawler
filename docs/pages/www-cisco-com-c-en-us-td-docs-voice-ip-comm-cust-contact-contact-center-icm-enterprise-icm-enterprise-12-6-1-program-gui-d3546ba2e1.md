---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-program-gui-d3546ba2e1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/program/guide/ucce_b_cisco-ucce_developer_guide-12_6_1/rcct_m_wccai-global-config-api.html
retrieved_at: 2026-08-16T20:22:24.621756+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(1)

Updated: August 21, 2023

Chapter: Contact Center AI API

## Chapter: Contact Center AI API

- Contact Center AI API

- Global Config API

- Config API

# Contact Center AI API

## Global Config API

Use the Contact Center AI (CCAI) Global Config API to retrieve the global configuration for AI services. This API is available
                           for administrators only when Cloud Connect is added in the inventory and is registered.

### URL

### Operations

get : returns the
                                    global CCAI configuration.

https://<server>/unifiedconfig/config/contactcenterai/globalconfig

post: syncs the default global configurations with the latest available from
                                    the control
                                    hub.

### Parameters

name : Configuration Name.

value : Configuration Value.

status : Indicates if the values are in sync with Control Hub.

lastSyncTime :Time when config data was last synced with
                                    Control Hub

### Example Get Response

```
<globalConfigDetail>
    <globalConfigs>
        <globalConfig>
            <name>CCAI.GlobalConfigId</name>
            <value>AXgB4em4bwWpdn7vJcLC</value>
        </globalConfig>
        <globalConfig>
            <name>CCAI.GlobalConfigName</name>
            <value>SS5T1</value>
        </globalConfig>
    </globalConfigs>
    <lastSyncTime>2021-03-05T16:07:43.497+05:30</lastSyncTime>
    <status>IN_SYNC</status>
</globalConfigDetail>
```

## Config API

Control Hub API is a proxy to Control Hub CMS service to fetch Contact Center AI
                           configuration.

### URL

### Operations

get : Returns Contact Center AI
                                    config corresponding to <id> using the URL

https://<server>/unifiedconfig/config/contactcenterai/config/<id> .

list : Retrieves list of Contact
                                    Center AI configs.

### Example Get Response

```
<ccaiconfig>
<conversationProfileId>sdfsd78bmplj89</conversationProfileId>
<defaultVirtualAgent>false</defaultVirtualAgent>
<connectorId>XK123UIU6887787JLK</connectorId>
<defaultAnswers>true</defaultAnswers>
<name>CCAIConfig2</name>
<description>Sample CCAI Config2</description>
<id>AXQlSeOzECsy_j49EVRz</id>
<type>Cisco</type>
<orgId>6d9069aa-76ce-45d6-a799-d38e60e92788</orgId>
</ccaiconfig>
```

### Example List Response

```
<ccaiconfigs>
<ccaiconfig>
<conversationProfileId>sdfsd78bmplj89</conversationProfileId>
<defaultVirtualAgent>false</defaultVirtualAgent>
<connectorId>XK123UIU6887787JLK</connectorId>
<defaultAnswers>true</defaultAnswers>
<name>CCAIConfig2</name>
<description>Sample CCAI Config2</description>
<id>AXQlSeOzECsy_j49EVRz</id>
<type>Cisco</type>
<orgId>6d9069aa-76ce-45d6-a799-d38e60e92788</orgId>
</ccaiconfig>
<ccaiconfig>
<conversationProfileId>asdf8768mnnb89</conversationProfileId>
<defaultVirtualAgent>true</defaultVirtualAgent>
<connectorId>XK123UIU6123567JLK</connectorId>
<defaultAnswers>false</defaultAnswers>
<name>CCAIConfig3</name>
<description>Sample CCAI Config3</description>
<id>AXQlSjp5ECsy_j49EVSp3</id>
<type>Google</type>
<orgId>6d9069aa-76ce-45d6-a799-d38e60e92788</orgId>
</ccaiconfig>
<ccaiconfig>
<conversationProfileId>qwewq556sad8asd</conversationProfileId>
<defaultVirtualAgent>false</defaultVirtualAgent>
<connectorId>XK123UIU6778787JLK</connectorId>
<defaultAnswers>false</defaultAnswers>
<name>CCAIConfig</name>
<description>Sample CCAI Config</description>
<id>AXQlSmksECsy_j49EVSs</id>
<type>Google</type>
<orgId>6d9069aa-76ce-45d6-a799-d38e60e92788</orgId>
</ccaiconfig>
</ccaiconfigs>
```