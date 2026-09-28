---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-program-gui-c2c7e43a03
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/program/guide/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5_chapter_010000.html
retrieved_at: 2026-08-16T20:28:28.013611+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

Updated: February 6, 2020

Chapter: ECC Payload API

## Chapter: ECC Payload API

- ECC Payload API

- ECC Payload API

# ECC Payload API

## ECC Payload API

You use expanded call variables to store values that are associated with a call. These variables are commonly called Expanded
                              Call Context (ECC) variables. While you can define many more ECC variables in the system, you can pass a maximum of 2000 bytes
                              of these variables at any time over any interface. To enable you to pass different ECC variables at different times, the solution
                              has ECC payloads.

An ECC payload is a defined set of ECC variables. You can create ECC payloads to suit the necessary information for a given
                              operation. You can include an ECC variable in multiple ECC payloads. The particular ECC variables in a given ECC payload are
                              called its members.

ECC payload ID 1 is the default ECC payload. The API prevents the deletion of this ECC payload.

In solutions that only use the default ECC payload,
                                                the Logger does not create an ECC variable that
                                                exceeds the 2000-byte limit for an ECC payload or
                                                the 2500-byte CTI Message Size limit. The Logger
                                                does this because it automatically adds all ECC
                                                variables to the default ECC payload if that is the
                                                only ECC payload.

If you create another ECC payload, the Logger no longer checks the 2000-byte limit when creating ECC variables. The Logger
                                                creates the ECC variables without assigning them to an ECC payload. Assign the new ECC variable to an appropriate ECC payload
                                                yourself, either through the ECC Payload API or through the ECC Payload Tool.

For create and update operations, the ECC Payload API verifies that the members of the ECC payload do not exceed the 2000-byte
                                                limit.

During
                                          upgrades, when the system first migrates your existing ECC
                                          variables to the Default payload, it does not check the CTI
                                          message size limit. The member names might exceed the extra
                                          500 bytes that is allocated for ECC payloads to a CTI
                                          client. Manually
                                             check the CTI Message Size counter in the Expanded Call Variable Payload
                                                List tool to ensure that the Default
                                             payload does not exceed the limit. If the Default
                                          payload exceeds the limit, modify it to meet the limit.

### URL

### Operations

create : Creates one ECC payload and stores it in the database.

Query Parameters

name: The name of the ECC payload (Required)

description: A description of the ECC payload (Optional)

variables: 0 or more ECC variables (Optional)

Specify each variable with the ecc.refURL of a valid, non-deleted ECC variable.

This API supports synchronous and asynchronous create operations.

delete : Permanently deletes one ECC payload and all its members from the database.

get : Returns one ECC payload from the database, using the URL https://<server>/unifiedconfig/config/eccpayload/<id> .

list : Retrieves a list of ECC payloads.

update : Updates one ECC payload in the database.

Query Parameters

changeStamp: The change stamp for the ECC payload record which the GET returns (Required)

refURL: The refURL of the ECC payload to update (Required)

name: The name of the ECC payload (Optional)

description: A description of the ECC payload (Optional)

variables: 0 or more ECC variables (Optional)

Specify each variable with the ecc.refURL of a valid, non-deleted ECC variable.

### Parameters

refURL: The refURL of the ECC payload. See Shared Parameters .

name: The name of the ECC payload. See Shared Parameters .

changeStamp: See Shared Parameters .

description: See Shared Parameters .

variables: The members of the ECC payload.

### Search and Sort Values

The following table shows the parameters that are searched and the parameters that are sortable.

name

description

name (default)

description

See Search and Sort .

This API does not support advanced search parameters.

### Example Get Response

```
<eccpayload>
  <refURL>/unifiedconfig/config/eccpayload/1</refURL>
  <changeStamp>18</changeStamp>
  <description>Initial default data.</description>
  <name>Default</name>
  <variables>
    <variable>
      <refURL>/unifiedconfig/config/expandedcallvariable/8</refURL>
      <name>POD.ID</name>
    </variable>
    <variable>
      <refURL>/unifiedconfig/config/expandedcallvariable/5009</refURL>
      <name>user.A1</name>
    </variable>
    <variable>
      <refURL>/unifiedconfig/config/expandedcallvariable/5010</refURL>
      <name>user.A2</name>
    </variable>
  </variables>
</eccpayload>
```

| Note | ECC payload ID 1 is the default ECC payload. The API prevents the deletion of this ECC payload. In solutions that only use the default ECC payload,
                                                the Logger does not create an ECC variable that
                                                exceeds the 2000-byte limit for an ECC payload or
                                                the 2500-byte CTI Message Size limit. The Logger
                                                does this because it automatically adds all ECC
                                                variables to the default ECC payload if that is the
                                                only ECC payload. If you create another ECC payload, the Logger no longer checks the 2000-byte limit when creating ECC variables. The Logger
                                                creates the ECC variables without assigning them to an ECC payload. Assign the new ECC variable to an appropriate ECC payload
                                                yourself, either through the ECC Payload API or through the ECC Payload Tool. For create and update operations, the ECC Payload API verifies that the members of the ECC payload do not exceed the 2000-byte
                                                limit. |
|---|---|

| Important | During
                                          upgrades, when the system first migrates your existing ECC
                                          variables to the Default payload, it does not check the CTI
                                          message size limit. The member names might exceed the extra
                                          500 bytes that is allocated for ECC payloads to a CTI
                                          client. Manually
                                             check the CTI Message Size counter in the Expanded Call Variable Payload
                                                List tool to ensure that the Default
                                             payload does not exceed the limit. If the Default
                                          payload exceeds the limit, modify it to meet the limit. |
|---|---|

| Note | Specify each variable with the ecc.refURL of a valid, non-deleted ECC variable. |
|---|---|

| Note | This API supports synchronous and asynchronous create operations. |
|---|---|

| Note | Specify each variable with the ecc.refURL of a valid, non-deleted ECC variable. |
|---|---|

| Search parameters | Sort parameters |
|---|---|
| name description | name (default) description |

| Note | This API does not support advanced search parameters. |
|---|---|