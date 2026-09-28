---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-program-gui-1818b60ed6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/program/guide/ucce_b_cisco-ucce_developer_guide-12_6_1/ucce_b_cisco-ucce_developer_guide-12_6_1_chapter_0101.html
retrieved_at: 2026-08-16T20:21:55.143970+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(1)

Updated: August 21, 2023

Chapter: Agent Team API

## Chapter: Agent Team API

- Agent Team API

- Agent Team                              	 API

# Agent Team API

## Agent Team
                        	 API

You can associate a set of agents to a team with a specific supervisor. The supervisor can run reports on that team and receive
                           Supervisor Assist requests from its members.

You can use the Agent Team API to list and view the agent teams currently defined in the database.

### URL

### Operations

get : Returns one agent team, using the URL https://<server>/unifiedconfig/config/agentteam/<id> .

list : Retrieves a list of agent teams.

Query parameters:

Summary list: See list .

### Parameters

refURL: The refURL of the agent team. See Shared Parameters .

name: The name of the agent team. See Shared Parameters .

description: See Shared Parameters .

dialedNumber: A reference to an internal dialed number () for the agent team, including the refURL and dialed number string.
                                    See References .

agents: A collection of agent (Agent Call API) references, including the refURL,
                                    first name, last name, username, and agent ID for each agent on the team. See References .

agentCount: Read-only field. Number of agents on the team.

supervisors: A collection of supervisor (Agent Call API) references, including the
                                    refURL, first name, last name, username, and agent ID for each supervisor who
                                    supervises this team. See References .

supervisorCount: Read-only field. Number of supervisors who supervise this team.

datacenter: The data center to which the agents on this team belong, including the refURL and name.

### Search and Sort Values

The following table shows the parameters that are searched and the parameters that are sortable.

name

description

name (default)

description

datacenter.name

See Search and Sort .

Advanced Search Parameters

datacenters: (dc1|dc2|dc3...) which returns all teams who belong to any of the specified data centers. You can specify up to three data centers. The data
                              center names are fully matched (case-insensitive, no partial matches). Searching for "core" returns all machines in the core
                              data center.

### Example Get Response

```
<agentTeam>
    
<refURL>https://***.***.***.***/unifiedconfig/config/agentteam/(id)</refURL>
    <name>team1</name>
    <datacenter>
        <refURL>/unifiedconfig/config/datacenter/9887</refURL>
        <name>Boston</name>
    </datacenter>
    <dialedNumber>
     <refURL>[https://***.***.***.***/unifiedconfig/config/dialednumber/(id)]</refURL>
       <dialedNumberString>8885551212</dialedNumberString>
    </dialedNumber>
    <description>test agent team1</description>
    <agentCount>1</agentCount>
    <agents>
       <agent>
          <refURL>[https://***.***.***.***/unifiedconfig/config/agent/(id_1)]</refURL>
          <firstName>John</firstName>
          <lastName>Smith</lastName>
          <userName>username</userName>
          <agentId>8006</agentId>
       </agent>
       <agent>
          <refURL>[https://***.***.***.***/unifiedconfig/config/agent/(id_2)]</refURL>
          <firstName>Jane</firstName>
          <lastName>Doe</lastName>
          <userName>username</userName>
          <agentId>8007</agentId>
       </agent>
    </agents>
    <supervisorCount>2</supervisorCount> <supervisor>
    <supervisors> 
       <supervisor>
          <refURL>[https://***.***.***.***/unifiedconfig/config/agent/(id_3)]</refURL>
          <firstName>Mary</firstName>
          <lastName>Hart</lastName>
          <userName>username</userName>
          <agentId>8008</agentId>
       </supervisor>
       <supervisor>
          <refURL>[https://***.***.***.***/unifiedconfig/config/agent/(id_4)]</refURL>
          <firstName>Jack</firstName>
          <lastName>Jones</lastName>
          <userName>username</userName>
          <agentId>8009</agentId>
       </supervisor>
    </supervisors>
    <changeStamp>0</changeStamp>
 </agentTeam>
```

| Note | Access to this API is different for supervisors and administrators. For more information, see Access . |
|---|---|

| Search parameters | Sort parameters |
|---|---|
| name description | name (default) description datacenter.name |