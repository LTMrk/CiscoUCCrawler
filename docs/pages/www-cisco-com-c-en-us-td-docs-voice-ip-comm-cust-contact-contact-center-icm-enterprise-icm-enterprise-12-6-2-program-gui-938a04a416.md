---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-program-gui-938a04a416
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/program/guide/ucce_b_cisco-ucce_developer_guide-12-6-2-/ucce_m_attribte_api-12_6_1.html
retrieved_at: 2026-08-16T20:19:36.478507+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

Updated: August 21, 2023

Chapter: Attribute API

## Chapter: Attribute API

- Attribute API

- Attribute                              	 API

# Attribute API

## Attribute
                        	 API

Attributes identify
                           		a call routing requirement, such as language, location, or agent expertise. You
                           		can create two types of attributes: boolean or proficiency. For example, you
                           		can create a Boston attribute that specifies that the agent assigned to this
                           		attribute must be located in Boston. Then, if a precision queue requires an
                           		agent who lives in Boston, then an agent with the attributes Boston = True is a
                           		good match. When you create a proficiency attribute, you assign a proficiency
                           		level to the agent.

Use the Attribute
                           		API to list the attributes currently defined in the database, define new
                           		attributes, and view, edit, and delete existing attributes.

### URL

### Operations

create :
                                    				Creates an attribute.

delete :
                                    				Marks one attribute and associated Agent attribute values for deletion, but
                                    				does not permanently delete them.

get :
                                    				Returns one attribute, using the URL https://<server>/unifiedconfig/config/attribute/<id> .

list :
                                    				Retrieves a list of attributes.

Query
                                             						parameters:

selectedAgentCount: Use this query parameter to augment
                                                						  attribute information about multiple agents. The selectedAgentCount parameter
                                                						  shows the number of specified agents associated with this attribute. For
                                                						  example, to find out how many of agents 5000, 5001, 5002, and 5003 in the list
                                                						  have this associated attribute, add selectedAgentCount=5000,5001,5002,5003 .

Using selectedAgentCount automatically sets the summary list query parameter to true .

Summary list: See list .

update :
                                    				Updates one attribute.

Query Parameters:

- removeNonMatchingDepartmentalRefs: Use this query parameter to
                                             						remove all agent attributes from an attribute when they no longer belong to the
                                             						department id specified in the query parameter or the global department. For
                                             						example, to remove all agent attributes that do not belong to department 5000
                                             						or the global department, add removeNonMatchingDepartmentalRefs=5000. If this
                                             						parameter is not specified, the agent attributes must belong to the attribute's
                                             						department or the global department.

### Parameters

refURL: The
                                    				refURL of the attribute. See Shared Parameters .

name: The name
                                    				of the attribute. See Shared Parameters .

changeStamp:
                                    				See Shared Parameters .

description:
                                    				See Shared Parameters .

dataType: The
                                    				data type of the attribute. Values are:

3:
                                          					 Boolean.

4:
                                          					 Proficiency.

defaultValue:
                                    				Used to specify the default value for the attribute when assigned to an agent,
                                    				if no explicit value is provided. Values are:

Boolean:
                                          					 true\false.

Proficiency: 1-10.

agentAttributes: A collection of agent attribute references for
                                    				this attribute, including the description, refURL, and read-only parameters
                                    				agentId, userName, firstName, and lastName. Also includes the attributeValue
                                    				parameter which indicates the value (true/false or 1-10) of the attribute for
                                    				this agent. See References .

agentAttributesAdded: A collection of agent attribute references ( Attribute API ) to be added to the attribute, including the agent refURL and the attributeValue of each agent. If the attributeValue is
                                    not specified, it is assigned the default value. Agents that already have this attribute are updated with the specified attributeValue.
                                    This parameter is update only, and cannot be used in conjunction with the agentAttributes parameter. This parameter can be
                                    used with the agentAttributesRemoved parameter. See References .

agentAttributesRemoved: A collection of agent attribute references ( Attribute API ) to be removed from the attribute, including the refURL of each agent. This parameter is update only, and cannot be used
                                    in conjunction with the agentAttributes parameter. This parameter can be used with the agentAttributesAdded parameter. See References .

agentCount:
                                    				Read-only field. Number of agents associated with the attribute.

selectedAgentCount: Read-only field. Indicates the number of
                                    				specified agents associated with this attribute. Returned only when using the
                                    				selectedAgentCount query parameter.

### Search and
                              		  Sort Values

The following
                              		  table shows the parameters that are searched and the parameters that are
                              		  sortable.

- name

- description

- name (default)

- dataType

- defaultValue

- description

See Search and Sort .

### Example Get
                              		  Response

```
<attribute>
      
	  <refURL>/unifiedconfig/config/attribute/5002</refURL>
         <changeStamp>0</changeStamp>
         <dataType>4</dataType>
         <defaultValue>1</defaultValue>
         <description>test</description>
         <name>AttributeA</name>
</attribute>
```

| Note | Using selectedAgentCount automatically sets the summary list query parameter to true . |
|---|---|

| Search parameters | Sort parameters |
|---|---|
| name description | name (default) dataType defaultValue description |