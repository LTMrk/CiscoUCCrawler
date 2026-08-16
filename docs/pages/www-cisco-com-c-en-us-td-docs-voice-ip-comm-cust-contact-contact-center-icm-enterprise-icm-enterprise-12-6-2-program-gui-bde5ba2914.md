---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-program-gui-bde5ba2914
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/program/guide/ucce_b_cisco-ucce_developer_guide-12-6-2-/ucce_m_call-type_12_6_1.html
retrieved_at: 2026-08-16T20:19:53.234397+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

Updated: August 21, 2023

Chapter: Call Type

## Chapter: Call Type

- Call Type

- Call Type

# Call Type

## Call Type

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

survey: Is used to map call type with survey type.

The two Survey types are

Questionnaire Name: Is used to identify the Inline Survey which is Digital Channel (Email and Chat) and Post Call Voice Survey.

Dispatch Id: Is used to identify Deferred Survey which is Post Call Email and SMS Survey.

You can associate only one survey to a call type.

The above parameters will be available only if you have added Cloud Connect in the Inventory page, and configured Webex Experience Management in the system.

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

| Note | You can associate only one survey to a call type. The above parameters will be available only if you have added Cloud Connect in the Inventory page, and configured Webex Experience Management in the system. |
|---|---|

| Search parameters | Sort parameters |
|---|---|
| name description id | name (default) description id serviceLevelThreshold serviceLevelType |