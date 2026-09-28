---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-014149a4f1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_skill-group-api_1501.html
retrieved_at: 2026-08-21T16:48:41.339319+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

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

Use the Skill Group API to list the skill groups
                           		currently defined in the database, define new skill groups, and view, edit, or
                           		delete existing skill groups.

Access to this
                                       		  API is different for supervisors and administrators. For more information, see Access .

### URL

### Operations

create :
                                    				Creates one skill group.

A skill
                                                				  group can only be associated with agents that are on the same data center as
                                                				  that skill group.

delete :
                                    				Marks one skill group for deletion, but does not permanently delete it.

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

After
                                                      						a skill group has been created, the data center cannot be modified.

A
                                                      						skill group can only be associated with agents that are on the same data center
                                                      						as that skill group.

### Parameters

refURL: The
                                    				refURL of the skill group. See Shared Parameters .

name: The name
                                    				of the skill group. See Shared Parameters .

department: A
                                    				reference to the department ( Department API ),
                                    				including the name and refURL. See References .

changeStamp:
                                    				See Shared Parameters .

description:
                                    				See Shared Parameters .

mediaRoutingDomain: A reference to the media routing domain ( Media Routing Domain API ) including the name and refURL. See References .

Defaults
                                          					 to Cisco_Voice MRD if this parameter is not provided.

This
                                          					 reference cannot be updated.

agents: A collection of agents assigned to the skill group
                                    						(See Agent Call API). References also include firstName, lastName, agentId,
                                    						and agentTeam (which includes the team name and refURL). See References .

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

Blank means use the value
                                    				from the specified mediaRoutingDomain.

serviceLevelType: This value indicates how the system calculates
                                    				the service level.

1:
                                          					 Ignore Abandoned Calls (default).

2:
                                          					 Abandoned Calls have Negative Impact.

3:
                                          					 Abandoned Calls have Positive Impact.

peripheralSet: This parameter is mandatory for Packaged CCE 4000 Agents or 12000 Agents deployment type. You must provide
                                    the reference to a peripheral set for which Agent PG is configured.

The peripheralSet parameter is not available for Packaged CCE 2000 Agents deployment type.

peripheralNumber: Read-only parameter. Automatically generated
                                    				when using the create operation.

datacenter:
                                    				A reference to the data center, including the refURL and name.

You must provide the reference to a data center that contains above peripheral set. For more information on data center for
                                    4000 Agents or 12000 Agents deployment, see Inventory Import API .

A route record
                                          			 is maintained seamlessly by the Skill Group API; that is, a single route record
                                          			 is generated for each skill group created and the process is hidden from the
                                          			 user. The route records are updated and deleted via the Skill Group API.

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

datacenter.name

peripheralSet.name (Available for Packaged CCE 4000 Agents and 12000 Agents deployment types)

See Search and Sort .

For more
                              		  information on search restrictions, see Search .

Advanced Search
                                 			 Parameters

datacenters: (dc1|dc2|dc3...) which returns all the Skill Groups that belong to any of the specified data centers. Up to three data centers can be specified.
                                    The data center names are fully matched (case-insensitive, no partial matches). Searching for "core" returns all machines
                                    in the core data center.

campaign:(none) which returns all the Skill Groups that are not associated to any campaign.

peripheralSets: (ps1|ps2|ps3...) returns the skill groups specific to the peripheral sets in 4000 Agents/12000 Agents deployment. The peripheral set names
                                    are fully matched (case-insensitive, no partial matches).

### Example Get
                              		  Response

```
<skillGroup> <department>
     <refURL>/unifiedconfig/config/department/5001</refURL>
     <name>Sales</name>
   </department> <refURL>/unifiedconfig/config/skillgroup/(id)</refURL>
    <name>test</name>
    <description>test skill group</description>
    <changeStamp>0</changeStamp <datacenter>
        <name>Berlin</name>
        <refURL>unifiedconfig/config/datacenter/5000</refURL>
    </datacenter> <mediaRoutingDomain>
        <name>Cisco_Voice</name>
        <refURL>/unifiedconfig/config/mediaroutingdomain/1</refURL>
    </mediaRoutingDomain>
    <bucketInterval>
        <name>bucketIntervalName</name>
        <refURL>/unifiedconfig/config/bucketinterval/1</refURL>
    </bucketInterval>
    <serviceLevelThreshold>20</serviceLevelThreshold>
    <serviceLevelType>1</serviceLevelType>
    <peripheralNumber>1234567</peripheralNumber>
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

### Example Get Response for Packaged CCE 4000 Agents or 12000 Agents Deployment Type

```
<skillGroups>
<skillGroup xsi:type="skillGroup"> <department>
     <refURL>/unifiedconfig/config/department/5002</refURL>
     <name>Sales</name>
   </department> <refURL>/unifiedconfig/config/skillgroup/8485</refURL>
<changeStamp>0</changeStamp>
<agentCount>1</agentCount>
<name>SKG1</name>
<peripheralNumber>9194364</peripheralNumber>
<agents>
    <agent>...</agent>
</agents>
<PeripheralSet>
           <refURL>/unifiedconfig/config/inventory/datacenter/bangalore/peripheralset/5001</refURL>
            <name>ps1</name>
 <PeripheralSet/>
 <datacenter>
        <refURL>/unifiedconfig/config/inventory/datacenter/10788</refURL>
        <name>bangalore</name>
 </datacenter>
<mediaRoutingDomain>...</mediaRoutingDomain>
</skillGroup>
</skillGroups>
```

| Note | Access to this
                                       		  API is different for supervisors and administrators. For more information, see Access . |
|---|---|

| Note | A skill
                                                				  group can only be associated with agents that are on the same data center as
                                                				  that skill group. |
|---|---|

| Note | Using selectedAgentCount automatically sets the summary list query parameter to true . |
|---|---|

| Note | After
                                                      						a skill group has been created, the data center cannot be modified. A
                                                      						skill group can only be associated with agents that are on the same data center
                                                      						as that skill group. |
|---|---|

| Note | A route record
                                          			 is maintained seamlessly by the Skill Group API; that is, a single route record
                                          			 is generated for each skill group created and the process is hidden from the
                                          			 user. The route records are updated and deleted via the Skill Group API. |
|---|---|

| Search parameters | Sort parameters |
|---|---|
| name description | name (default) description serviceLevelThreshold serviceLevelType peripheralNumber datacenter.name peripheralSet.name (Available for Packaged CCE 4000 Agents and 12000 Agents deployment types) |