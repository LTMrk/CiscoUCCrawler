---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-program-gui-8184b50d2c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/program/guide/ucce_b_cisco-ucce_developer_guide-12-6-2-/ucce_m_contact_share_group_api-12_6_1.html
retrieved_at: 2026-08-16T20:20:06.496361+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

Updated: August 21, 2023

Chapter: Contact Share Group API

## Chapter: Contact Share Group API

- Contact Share Group API

- Contact Share                              	 Group API

# Contact Share Group API

## Contact Share
                        	 Group API

The Contact Share
                           		group is a routing entity that operates on a single Contact Share rule with a
                           		set of Contact Share queues. It is used to determine to which target Unifed CCE
                           		to send the call, given the definition of the rule and the realtime data on
                           		each of the queues. This API is only available on the Contact Director
                           		Deployment.

To learn more
                                       		  about the other Contact Share APIs available in the Contact Director
                                       		  Deployment, see Access .

### URL

### Parameters

changeStamp:
                                    				See Shared Parameters .

refURL: The
                                    				refURL of the Contact Share group. See Shared Parameters .

contactShareRule: Required. The refURL of a Contact Share rule
                                    				to apply to this group.

name:
                                    				Required. The name of the Contact Share group.

acceptQueueIf
                                    				: Optional. A logical expression that qualifies individual queues to be used in
                                    				the group.

description:
                                    				Optional. The description of the group.

contactShareQueues: Optional. Information for any Queues in the
                                    				Contact Share group.

### Operations

create :
                                    				Creates one Contact Share group.

delete :
                                    				Deletes one Contact Share group.

get :
                                    				Returns one Contact Share group, using the URL
                                    				https://<server>/unifiedconfig/config/contactsharegroup<id>.

list :
                                    				Retrieves a list of Contact Share group.

update :
                                    				Updates one Contact Share group.

### Search and
                              		  Sort Values

The following
                              		  table shows the parameters that are searched and the parameters that are
                              		  sortable.

- name

- description

- groupExpression

- name(default)

- description

- groupExpression

See Search and Sort .

### Example Get
                              		  Response

```
<contactShareGroup>
   <changeStamp>0</changeStamp>
   <refURL>/unifiedconfig/config/contactsharegroup/5000</refURL>
   <contactShareRule>
      <name>Cisco_MED</name>
      <refURL>/unifiedconfig/config/contactsharerule/5000</refURL>
   </contactShareRule>
   <name>test</name>
   <acceptQueueIf>Call.PeripheralVariable1==1</acceptQueueIf>
   <description>test something</description>
	  <contactShareQueues>
      <contactShareQueue>
         <refURL>/unifiedconfig/config/contactsharequeue/5000</refURL>
         <name>CSQ-1</name>
         <queueType>skillGroup</queueType>
			      <targetInstance>
            <id>5000</id>
            <name>cs01</name>
         </targetInstance>
      </contactShareQueue>
   </contactShareQueues>
</contactShareGroup>
```

| Note | To learn more
                                       		  about the other Contact Share APIs available in the Contact Director
                                       		  Deployment, see Access . |
|---|---|

| Search parameters | Sort parameters |
|---|---|
| name description groupExpression | name(default) description groupExpression |