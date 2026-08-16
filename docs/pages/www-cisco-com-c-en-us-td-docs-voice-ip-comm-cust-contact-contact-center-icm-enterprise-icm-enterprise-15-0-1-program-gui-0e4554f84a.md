---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-0e4554f84a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/ucce_b_cisco-unified-contact-center-enterprise-developer-reference-release-15-0/ucce_m_administrator-api_1501.html
retrieved_at: 2026-08-16T20:14:37.102985+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: December 10, 2025

Chapter: Administrator API

## Chapter: Administrator API

- Administrator API

- Administrator                              	 API

# Administrator API

## Administrator
                        	 API

An administrator is
                           		an Active Directory user who has been provided access to the system.

Use the
                           		Administrator API to list the administrators currently defined in the database,
                           		define new administrators, and view, edit, and delete existing administrators.

### URL

### Operations

create : Creates
                                    				one administrator.

delete :
                                    				Permanently deletes one administrator.

get : Returns one
                                    				administrator, using the URL https://<server>/unifiedconfig/config/administrator/<id> .

list : Retrieves a
                                    				list of administrators.

update : Updates
                                    				one administrator.

### Parameters

refURL: The
                                    				refURL of the administrator. See Shared Parameters .

changeStamp:
                                    				See Shared Parameters .

description:
                                    				See Shared Parameters .

userName:
                                    				Required. The unique username of an existing Active Directory account. Maximum
                                    				length of 64 characters.

domainName:
                                    				The domain for this administrator. If blank, system uses the default domain
                                    				name. Maximum length of 64 characters.

- customer: A reference to a customer, including the refURL.

readOnly:
                                    				Required. Specifies whether the administrator has read-only access to the APIs
                                    				and tools. Values are true/false.

### Search and Sort Values

The following table shows the parameters that are searched and the
                              		  parameters that are sortable.

- userName

- domainName

- description

- userName

- domainName

- description

See Search and Sort .

### Example Get
                              		  Response

```
<administrator>
    <changeStamp>0</changeStamp>
    <domainName>domain</domainName>
    <userName>user1</userName>
    <readOnly>false</readOnly>
    <customer>
       <refURL>/unifiedconfig/config/customer/(id)</refURL>
    </customer>
</administrator>
```

| Search parameters | Sort parameters |
|---|---|
| userName domainName description | userName domainName description |