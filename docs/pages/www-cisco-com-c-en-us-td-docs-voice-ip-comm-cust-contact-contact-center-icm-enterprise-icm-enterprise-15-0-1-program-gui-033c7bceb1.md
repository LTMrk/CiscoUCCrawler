---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-033c7bceb1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/ucce_b_cisco-unified-contact-center-enterprise-developer-reference-release-15-0/ucce_m_call-type_1501.html
retrieved_at: 2026-08-16T20:17:16.485303+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: December 10, 2025

Chapter: Call Type API

## Chapter: Call Type API

- Call Type API

- Call Type API

# Call Type API

## Call Type API

Call types categorize calls. Based on call type, the system maps a dialed number to a routing script that ultimately sends
                           the call to the appropriate destination.

Use the Call Type API to list the call types currently defined in the database, define new call types, and view, edit, or
                           delete records of existing call types.

### URL

### Operations

get : Returns one call type, using the URL https://<server>/unifiedconfig/config/calltype/<id> .

list : Retrieves a list of call types.

update : Updates one call type.

### Parameters

refURL: The refURL of the call type. See Shared Parameters .

name: The name of the call type. See Shared Parameters .

changeStamp: See Shared Parameters .

description: See Shared Parameters .

ccaiConfigID: Identifier for the Contact Center AI (CCAI) configuration saved in the Control Hub. Used to map the call type
                                    with the CCAI configuration. This parameter is available for administrators only when Cloud Connect is added in the inventory.

id: The database id of the call type. Read-only field. Used in scripting.

serviceLevelThreshold: Maximum time in seconds that a caller should wait before being connected with an agent. Leave blank
                                    to use the system default.

serviceLevelType: This value indicates how the system calculates the service level.

blank: Use the system default.

1: Ignore Abandoned Calls.

2: Abandoned Calls have Negative Impact.

3: Abandoned Calls have Positive Impact.

bucketInterval: A reference to the bucket interval ( Bucket Interval API ), including the refURL and name.

### Search and Sort Values

The following table shows the parameters that are searched and the parameters that are sortable.

name

description

id

name (default)

description

id

serviceLevelThreshold

serviceLevelType

See Search and Sort .

### Example Get Response

```
<callType>
<department>
<refURL>/unifiedconfig/config/department/5001</refURL>
<name>Sales</name>
</department>
<refURL>/unifiedconfig/config/calltype/(id)</refURL>
<name>test</name>
<description>test call type</description>
<id>5002</id> <ccaiConfigID>Serviceconfig</ccaiConfigID> <serviceLevelThreshold>10</serviceLevelThreshold>
<serviceLevelType>1</serviceLevelType>
<changeStamp>0</changeStamp>
<bucketInterval>
<refURL>/unifiedconfig/config/bucketinterval/(id)</refURL>
<name>bucket1</name>
</bucketInterval>
<survey>
<questionnaireName>1d222cb3</questionnaireName>
 OR <dispatchId>115097d3-ea65-432b-b90a-08aa7e5de361</dispatchId>
</survey>
</callType>
```

| Search parameters | Sort parameters |
|---|---|
| name description id | name (default) description id serviceLevelThreshold serviceLevelType |