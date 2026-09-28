---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-program-gui-b1f50d1bd5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/program/guide/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5_chapter_011011.html
retrieved_at: 2026-08-16T20:29:18.561769+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

Updated: February 6, 2020

Chapter: Skill Group API

## Chapter: Skill Group API

- Skill Group API

- Skill Group                              	 API

# Skill Group API

## Skill Group
                        	 API

A skill group is a
                           		collection of agents who share a common set of competencies that equip them to
                           		handle the same types of requests. Some examples of skill groups are a
                           		collection of agents who speak a specific language or who can assist callers
                           		with billing questions.

Use the Skill Group API to list, view, or edit
                           		existing skill groups.

Access to this API
                                       		  is different for supervisors and administrators. For more information, see Access .

### URL

unifiedconfig api does not support skill groups in System PGs

### Operations

get :
                                    				Returns one skill group, using the URL https://<server>/unifiedconfig/config/skillgroup/<id> .

list :
                                    				Retrieves a list of skill groups.

Query
                                             						Parameters:

selectedAgentCount: Use this query parameter to augment skill
                                                						  group information about multiple agents. The selectedAgentCount parameter shows
                                                						  the number of specified agents belonging to that skill group. For example, to
                                                						  find out how many of agents 5000, 5001, 5002, and 5003 belong to each of the
                                                						  skill groups in the list, add selectedAgentCount=5000,5001,5002,5003 .

Using selectedAgentCount automatically sets the summary list query parameter to true .

Summary list: See list .

update :
                                    				Updates one skill group.

### Parameters

refURL: The
                                    				refURL of the skill group. See Shared Parameters .

name: The name
                                    				of the skill group. See Shared Parameters .

changeStamp:
                                    				See Shared Parameters .

description:
                                    				See Shared Parameters .

peripheral:
                                    				Contains the name and id of the peripheral.

mediaRoutingDomain: A reference to the media routing domain ( Media Routing Domain API ) including the name and refURL. See References .

Defaults
                                          					 to Cisco_Voice MRD if this parameter is not provided.

This
                                          					 reference cannot be updated.

agents: A collection of agents assigned to the skill
                                    						group (See Agent Call API). References also include firstName, lastName,
                                    						agentId, and agentTeam (which includes the team name and refURL). See References .

canRemove:
                                          					 This parameter only appears for supervisors. It indicates whether or not the
                                          					 supervisor has permission to remove the agent from this skill group. The
                                          					 supervisor can remove the agent from the skill group if the agent belongs to a
                                          					 team of this supervisor.

agentsAdded: A
                                    				collection of agent references to be added to the skill group, including the
                                    				refURL of each agent to be added. This parameter is update only, and cannot be
                                    				used in conjunction with the agents parameter. This parameter can be used with
                                    				the agentsRemoved parameter. See References .

agentsRemoved: A collection of agent references to be removed
                                    				from the skill group, including the refURL of each agent to be removed. This
                                    				parameter is update only, and cannot be used in conjunction with the agents
                                    				parameter. This parameter can be used with the agentsAdded parameter. See References .

agentCount:
                                    				Read-only parameter containing the number of agents having the skill.

selectedAgentCount: Read-only field. Indicates the number of
                                    				specified agents belonging to the skill group. Returned only when using the
                                    				selectedAgentCount query parameter.

bucketInterval: A reference to the bucket interval ( Bucket Interval API ).
                                    				Includes the name and refURL. See References .

serviceLevelThreshold: Maximum time in seconds that a caller
                                    				should wait before being connected with an agent. Positive integers only, or
                                    				blank.

serviceLevelType: This value indicates how the system calculates
                                    				the service level.

1:
                                          					 Ignore Abandoned Calls (default).

2:
                                          					 Abandoned Calls have Negative Impact.

3:
                                          					 Abandoned Calls have Positive Impact.

### Search and
                              		  Sort Values

The following
                              		  table shows the parameters that are searched and the parameters that are
                              		  sortable.

name

description

name (default)

description

serviceLevelThreshold

serviceLevelType

peripheralNumber

peripheral.name

See Search and Sort .

For more
                              		  information on search restrictions, see Search .

Advanced Search Parameters

peripherals:
                                       				  (peri1|peri2|peri3, ...) which returns all SkillGroups that have any of the
                                    				specified peripherals. Up to ten peripherals can be specified. The peripheral
                                    				names are fully matched (case-insensitive, no partial matches).

### Example Get
                              		  Response

```
<skillGroup>
    <refURL>/unifiedconfig/config/skillgroup/(id)</refURL>
    <name>test</name>
    <description>test skill group</description>
    <changeStamp>0</changeStamp> <peripheral>
        <id>5001</id>
        <name>CUCM_PG1</name>
    </peripheral> <mediaRoutingDomain>
        <name>Cisco_Voice</name>
        <refURL>/unifiedconfig/config/mediaroutingdomain/1</refURL>
    </mediaRoutingDomain>
    <bucketInterval>
        <name>bucketIntervalName</name>
        <refURL>/unifiedconfig/config/bucketinterval/1</refURL>
    </bucketInterval>
    <serviceLevelThreshold>20</serviceLevelThreshold>
    <serviceLevelType>1</serviceLevelType>
    <agents>
        <agent>
            <refURL>/unifiedconfig/config/agent/5000</refURL>
            <firstName>Jane</firstName>
            <lastName>Doe</lastName>
            <userName>username</userName>
            <agentId>8007</agentId>
            <canRemove>true</canRemove>
        </agent>
        <agent>
            <refURL>/unifiedconfig/config/agent/5001</refURL>
            <firstName>John</firstName>
            <lastName>Smith</lastName>
            <userName>username2</userName>
            <agentId>8008</agentId>
            <agentTeam>
                <refURL>/unifiedconfig/config/agentteam/5000</refURL>
                <name>someTeam</name>
            </agentTeam>
            <canRemove>false</canRemove>
        </agent>
        <agent>...</agent>
        <agent>...</agent>
    </agents>
    <agentCount>4</agentCount>
 </skillGroup>
```

| Note | Access to this API
                                       		  is different for supervisors and administrators. For more information, see Access . |
|---|---|

| Note | unifiedconfig api does not support skill groups in System PGs |
|---|---|

| Note | Using selectedAgentCount automatically sets the summary list query parameter to true . |
|---|---|

| Search parameters | Sort parameters |
|---|---|
| name description | name (default) description serviceLevelThreshold serviceLevelType peripheralNumber peripheral.name |