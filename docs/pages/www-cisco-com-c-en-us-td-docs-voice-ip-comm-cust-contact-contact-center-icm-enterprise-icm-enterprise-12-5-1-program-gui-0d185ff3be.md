---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-program-gui-0d185ff3be
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/program/guide/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5_chapter_0100.html
retrieved_at: 2026-08-16T20:25:40.417625+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

Updated: February 6, 2020

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

### Search and Sort Values

The following table shows the parameters that are searched and the parameters that are sortable.

name

description

name (default)

description

See Search and Sort .

### Example Get Response

```
<agentTeam>
 
    <refURL>/unifiedconfig/config/agentteam/(id)</refURL>
    <name>team1</name>
    <dialedNumber>
       <refURL>/unifiedconfig/config/dialednumber/(id)</refURL>
       <dialedNumberString>8885551212</dialedNumberString>
    </dialedNumber>
    <description>test agent team1</description>
    <agents>
       <agent>
          <refURL>/unifiedconfig/config/agent/(id_1)</refURL>
          <firstName>John</firstName>
          <lastName>Smith</lastName>
          <userName>username</userName>
          <agentId>8006</agentId>
       </agent>
       <agent>
          <refURL>/unifiedconfig/config/agent/(id_2)</refURL>
          <firstName>Jane</firstName>
          <lastName>Doe</lastName>
          <userName>username</userName>
          <agentId>8007</agentId>
       </agent>
    </agents>
    <supervisor>
       <supervisor>
          <refURL>/unifiedconfig/config/agent/(id_3)</refURL>
          <firstName>Mary</firstName>
          <lastName>Hart</lastName>
          <userName>username</userName>
          <agentId>8008</agentId>
       </supervisor>
       <supervisor>
          <refURL>/unifiedconfig/config/agent/(id_4)</refURL>
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
| name description | name (default) description |