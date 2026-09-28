---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-ff68604a4f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_administrator-api_1501.html
retrieved_at: 2026-08-21T16:42:41.108696+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Administrator API

## Chapter: Administrator API

- Administrator API

- Administrator API

# Administrator API

## Administrator API

An administrator is an Active Directory user who has been provided access to the system.

That access can be controlled by assigning the administrator to roles and departments (see Role API and Department API ) .

Use the Administrator API to list the administrators currently defined in the database, define new administrators, and view,
                           edit, and delete existing administrators.

### URL

### Operations

create : Creates one administrator.

delete : Permanently deletes one administrator.

get : Returns one administrator, using the URL https://<server>/unifiedconfig/config/administrator/<id> .

list : Retrieves a list of administrators.

update : Updates one administrator.

### Parameters

refURL: The refURL of the administrator. See Shared Parameters .

changeStamp: See Shared Parameters .

description: See Shared Parameters .

userName: Required. The unique username of an existing Active Directory account. Maximum length of 64 characters.

domainName: The domain for this administrator. If blank, system uses the default domain name. Maximum length of 64 characters.

departments: A collection of department ( Department API ) references associated with this administrator, including the refURL and name. Leave this collection empty to allow the administrator
                                    to have access to all departments. See References .

role: A reference to a role ( Role API ), including refURL and name. This parameter sets access to specific features. Automatically creates membership to Active
                                    Directory Setup group or Config group. If no role is assigned, the administrator is not placed in either group and does not
                                    have access to any of the web configuration tools, the Configuration Manager, or the Script Editor. See References .

readOnly: Required. Specifies whether the administrator has read-only access to the APIs and tools. Values are true/false.

### Search and Sort Values

The following table shows the parameters that are searched and the parameters that are sortable.

- userName

- domainName

- description

- userName

- domainName

- description

See Search and Sort .

### Example Get Response

```
<administrator>
      <changeStamp>3</changeStamp>
      <refURL>/unifiedconfig/config/administrator/5000</refURL>
      <domainName>domain</domainName>
      <userName>user1</userName>
      <departments>
        <department>
          <refURL>/unifiedconfig/config/department/5000</refURL>
          <name>dept1</name>
        </department>
        <department>
          <refURL>/unifiedconfig/config/department/5001</refURL>
          <name>dept2</name>
        </department>
      </departments>
      <description>desc</description>
      <readOnly>true</readOnly>
      <role>
        <refURL>/unifiedconfig/config/role/5005</refURL>
        <name>ConfigAdmin</name>
      </role>
</administrator>
```

| Search parameters | Sort parameters |
|---|---|
| userName domainName description | userName domainName description |