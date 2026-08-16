---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-program-gui-28dbcfb1ea
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/program/guide/ucce_b_cisco-ucce_developer_guide-12-6-2-/ucce_m_contact_share_rule_api-12_6_1.html
retrieved_at: 2026-08-16T20:20:10.314825+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

Updated: August 21, 2023

Chapter: Contact Share Rule API

## Chapter: Contact Share Rule API

- Contact Share Rule API

- Contact Share Rule                              	 API

# Contact Share Rule API

## Contact Share Rule
                        	 API

A Contact Share
                           		rule is required when configuring a Contact Share group. A group is sent in
                           		every routing request to the Contact Share process. Each group has a rule that
                           		defines the logic for selecting a skill group or precision queue in that group
                           		for a routing request. Use the Contact Share Rules API to create, update, list,
                           		and delete rules. This API is only available on the Contact Director
                           		deployment.

To learn more
                                       		  about the other APIs available in the Contact Director deployment, see Access .

### URL

### Parameters

refURL: The refURL of the Contact Share rule. See Shared Parameters .

name:
                                    				Required. The name of the Contact Share rule.

ruleExpression: Required. The logical expression with which the
                                    				rule operates.

description:
                                    				Optional. The description of the rule.

changeStamp: See Shared Parameters .

### Operations

create :
                                    				Creates one Contact Share rule.

delete :
                                    				Permanently deletes one Contact Share rule.

get :
                                    				Returns one Contact Share rule, using the URL
                                    				https://<server>:/unifiedconfig/config/contactsharerule<id>.

list :
                                    				Retrieves a list of Contact Share rules.

update :
                                    				Updates one Contact Share rule.

### Search and
                              		  Sort Values

The following
                              		  table shows the parameters that are searched and the parameters that are
                              		  sortable.

- name

- description

- ruleExpression

- name(default)

- description

- ruleExpression

See Search and Sort .

### Example Get
                              		  Response

```
<contactShareRule>
  <refURL>/unified/config/contactsharerule/(id)</refURL>
  <name>test</name>
  <ruleExpression>Call.PeripheralVariable==1</ruleExpression>
  <description>test something</description>
  <changeStamp>0</changeStamp>
</contactShareRule>
```

| Note | To learn more
                                       		  about the other APIs available in the Contact Director deployment, see Access . |
|---|---|

| Search parameters | Sort parameters |
|---|---|
| name description ruleExpression | name(default) description ruleExpression |