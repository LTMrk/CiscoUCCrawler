---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-87d1b01bdd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/ucce_b_cisco-unified-contact-center-enterprise-developer-reference-release-15-0/ucce_m_1501_peripheral_api.html
retrieved_at: 2026-08-16T20:18:33.116308+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: December 10, 2025

Chapter: Peripheral API

## Chapter: Peripheral API

- Peripheral API

- Peripheral API

# Peripheral API

## Peripheral API

### URL

https://<server>/unifiedconfig/config/peripheral

### Operations

get : Returns a single peripheral.

Search Parameter:

q : excludeClientType or includeClientType (e.g. excludeClientType:(13&30)):

Returns peripherals using the search for a specific client type (e.g. clientType=47) - https://<IP adress>/unifiedconfig/config/peripheral?q=includeClientType:(47)

Returns peripherals using search except a specific client type (e.g. clientType=!13) - https://<IP adress>/unifiedconfig/config/peripheral?q=excludeClientType:(13)

Returns peripherals using search except a specific set of client types (e.g. clientType=!13,!30) - https://<IP adress>/unifiedconfig/config/peripheral?q=excludeClientType:(13%2630)

Returns peripherals using search for a specific set of client types (e.g. clientType=13,47) - https://<IP adress>/unifiedconfig/config/peripheral?q=includeClientType:(13%2647)

### Search parameter

### Query parameters

q : query parameter for search

sort :  <fieldName>%20<asc/desc>

startIndex : Default 0

resultsPerPage : Default 25

Access is provided to users who have the ConfigGroup API user role.

### Parameters

Values

Are case-insensitive.

Can be contained anywhere in the parameter value.

Can match any of the default parameters.

Cannot include SQL wildcards. They are not supported.

Must be URL encoded. For example, & must be converted to %26 so that it is not treated as a separator for additional query parameters.

### Search and Sort Values

Sorting fields can be set to ascending (asc) or descending (desc) order.

The following table shows the parameters that are searchable and the parameters that are sortable.

Search Parameter

Sort Parameter

name

values

description

clientType (excludeClientType or includeClientType)

See Search and Sort .

### Example Get Response

```
<peripherals>
            <peripheral>
                <refURL>/unifiedconfig/config/peripheral/5000</refURL>
                <changeStamp>125</changeStamp>
                <clientType>30</clientType>
                <defaultDeskSetting>
                     <refURL>/unifiedconfig/config/agentdesksetting/5000</refURL>
                     <name>Default</name>
                </defaultDeskSetting>
                <name>PG1_CCM1</name>
                <peripheralGateway>
                     <refURL>/unifiedconfig/config/peripheralgateway/5000</refURL>
                     <name>PG1</name>
                </peripheralGateway>
                <peripheralName>PG1_CCM1</peripheralName>
                <peripheralId>5000</peripheralId>
                <routingClient>
                    <refURL>/unifiedconfig/config/routingclient/5000</refURL>
                    <changeStamp>0</changeStamp>
                    <clientType>30</clientType>
                    <lateThreshold>500</lateThreshold>
                    <logicalController>
                         <refURL>/unifiedconfig/config/peripheralgateway/5000</refURL>
                         <name>PG1</name>
                    </logicalController>
                    <name>PG1_CCM1.RC</name>
                    <peripheral>
                         <id>5000</id>
                         <name>PG1_CCM1</name>
                    </peripheral>
                    <timeoutLimit>10</timeoutLimit>
                    <timeoutThreshold>1500</timeoutThreshold>
              </routingClient>
              <routingClientId>5000</routingClientId>
         </peripheral>
      </peripherals>
```

| Note | Access is provided to users who have the ConfigGroup API user role. |
|---|---|

| Search Parameter | Sort Parameter |
|---|---|
| name | values |
| description |  |
| clientType (excludeClientType or includeClientType) |  |