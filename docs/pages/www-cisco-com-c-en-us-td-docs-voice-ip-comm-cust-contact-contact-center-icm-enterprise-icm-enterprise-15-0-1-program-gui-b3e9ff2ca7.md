---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-b3e9ff2ca7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/ucce_b_cisco-unified-contact-center-enterprise-developer-reference-release-15-0/ucce_m_agent_team_api_1501.html
retrieved_at: 2026-08-16T20:14:53.516633+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: December 10, 2025

Chapter: Agent Team API

## Chapter: Agent Team API

- Agent Team API

- Agent Team API

# Agent Team API

## Agent Team API

You can associate a set of agents to a team with a specific supervisor. The supervisor can run reports on that team and receive
                           Supervisor Assist requests from its members.

You can use the Agent Team API to list and view the agent teams currently defined in the database.

### URL

### Operations

get : Returns one agent team, using the URL https://<server>/unifiedconfig/config/agentteam/<id> .

list : Retrieves a list of agent teams.

Query parameters:

Summary list: See list .

create : Creates a agentTeam using the url: https://<ip_address>/unifiedconfig/config/agentteam

update : Updates a agentTeam using the url: https://<ip_address>/unifiedconfig/config/agentteam/<agentTeamID>

delete : Deletes a agentTeam using the url: https://<ip_address>/unifiedconfig/config/agentteam/<agentTeamID>

### Parameters

peripheral: Required for Create API only. Fully ignored for Update API. Includes the following parameters:

id: a mandatory field for Create API only. This value is not allowed to be changed/updated.

primarySupervisor: Added, which will be mapped to supervisorId.

refURL: The refURL of the agent team.

name: The name of the agent team. Maximum length of 32 characters allowed.

description: Description for agent team. See Shared Parameters . Maximum length of 255 characters.

dialedNumber: A reference to an internal dialed number  (Dialed Number API) for the agent team, including the refURL and dialed
                                       number string.

agents: A collection of agent (Agent Call API) references, including the refURL, first name, last name, username, and agent
                                    ID for each agent on the team.

agentCount: Read-only field. Number of agents on the team.

supervisors: A collection of supervisor (Agent Call API) references, including the refURL, first name, last name, username,
                                    and agent ID for each supervisor who supervises this team.

supervisorCount: Read-only field. Number of supervisors who supervise this team.

### Search and Sort Values

Sorting fields can be set to ascending (asc) or descending (desc) order.

The following table shows the parameters that are searchable and the parameters that are sortable.

name

description

name (default)

description

See Search and Sort .

### Example Get Response

```
<agentTeam> 
     <refURL>/unifiedconfig/config/agentteam/5000</refURL> 
     <changeStamp>1</changeStamp>
     <agentCount>10</agentCount>
     <name>1000.AT</name>                   
     <peripheral>               
          <id>5000</id>              
          <name>PG1_CCM1</name>  
     </peripheral>      
     <peripheralId>5000</peripheralId> 
     <supervisorCount>1</supervisorCount>     
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
     <primarySupervisor>                
          <refURL>/unifiedconfig/config/agent/27001</refURL>                
          <agentId>8010572</agentId>               
          <firstName>8010572</firstName>               
          <lastName>8010572</lastName>                
          <userName>8010572@stooges.icm</userName>            
     </primarySupervisor>            
     <supervisors>                
          <supervisor>                    
               <refURL>/unifiedconfig/config/agent/27001</refURL>                    
               <agentId>8010572</agentId>                    
               <firstName>8010572</firstName>                    
               <lastName>8010572</lastName>                     
               <userName>8010572@stooges.icm</userName>                
          </supervisor>            
     </supervisors>
 </agentTeam>
```

| Note | Access to this API is different for supervisors and administrators. For more information, see Access . |
|---|---|

| Search parameters | Sort parameters |
|---|---|
| name description | name (default) description |