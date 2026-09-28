---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-0c9c68911a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_expanded-call-variable-api_1501.html
retrieved_at: 2026-08-21T16:46:35.653989+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Expanded Call Variable API

## Chapter: Expanded Call Variable API

- Expanded Call Variable API

- Expanded Call Variable API

# Expanded Call Variable API

## Expanded Call Variable API

Calls carry data with them as they move through the system. This data, called expanded call variable data, is embedded with
                           the call and is visible on the agent desktop.

Use the Expanded Call Variable API to list the expanded call variables currently defined in the database, define new expanded
                           call variables, and view, edit, and delete existing expanded call variables.

### URL

### Operations

create : Creates one expanded call variable.

delete : Marks one expanded call variable for deletion, but does not permanently delete it.

get : Returns one expanded call variable, using the URL https://<server>/unifiedconfig/config/expandedcallvariable/<id> .

list : Retrieves a list of expanded call variables.

update : Updates one expanded call variable.

update : Updates one expanded call variable.

### Parameters

refURL: The refURL of the expanded call variable. See Shared Parameters .

name: The name of the expanded call variable. See Shared Parameters .

changeStamp: See Shared Parameters .

description: See Shared Parameters .

maximumLength: The maximum length of the expanded call variable. The  value is 1 to 210.

Cisco Provided POD.ID variable, Maximum length can be modified.

eccArray: Indicates whether the expanded call variable is an array. Values are true/false.

maximumArraySize: The maximum number of elements in the array is 1 to 255. Required if eccArray is true; must be blank or
                                    not specified if eccArray is false.

enabled: Indicates whether the expanded call variable is enabled. Values are true/false.

persistent:  Specifies whether the expanded call variable is written to the historical database with each Termination Call
                                    Detail and Route Call Detail record. Values are true/false.

No persistent,
                                          					 enabled arrays are allowed.

The maximum number
                                          					 of persistent, scalar, enabled variables is 20.

ciscoProvided: Indicates whether the expanded call variable is provided by Cisco. Values are true/false. Read-only.

bytesRequired: The number of bytes required to store the expanded call variable in the system. Read-only.

The size is calculated using the following formula:

If eccArray is
                                          						  false, the size is 5+Maximum Length.

If eccArray is
                                          						  true, the size is 5+(1+Maximum length)*Maximum Array size.

bytesRequiredInCtiServer:  The number of bytes required to send this variable to CTI Server. Read-only.

The size is calculated using the following formula:

If eccArray is
                                          						  false, the size is Length of name+Maximum length+4.

If eccArray is
                                          						  true, the size is (Length of name+Maximum length+5)*Maximum array size.

The total bytesRequired of all enabled expanded call variables cannot exceed 2000 bytes.

The total bytesRequiredInCtiServer of all enabled expanded call variables cannot exceed 2500 bytes.

### Search and Sort Values

The following table shows the parameters that are searched and the parameters that are sortable.

name

description

name (default)

description

maximumLength

maximumArraySize

eccArray

enabled

persistent

ciscoProvided

See Search and Sort .

### Example Get Response

```
<expandedCallVariable>
    <refURL>/unifiedconfig/config/expandedcallvariable/(id)</refURL>
    <name>test</name>
    <maximumLength>9</maximumLength>
    <maximumArraySize>10</maximumArraySize>
    <eccArray>true</eccArray>
    <enabled>true</enabled>
    <ciscoProvided>false</ciscoProvided>
    <description>test expanded call variable</description>
    <persistent>false</persistent>
    <changeStamp>0</changeStamp>
    <bytesRequired>105</bytesRequired>
    <bytesRequiredInCtiServer>180</bytesRequiredInCtiServer>
</expandedCallVariable>
```

| Note | Cisco Provided POD.ID variable, Maximum length can be modified. |
|---|---|

| Search parameters | Sort parameters |
|---|---|
| name description | name (default) description maximumLength maximumArraySize eccArray enabled persistent ciscoProvided |