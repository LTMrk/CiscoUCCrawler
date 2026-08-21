---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-b168b30e44
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_agent--state-trace-api_1501.html
retrieved_at: 2026-08-21T16:45:04.043746+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Agent  State Trace API

## Chapter: Agent  State Trace API

- Agent  State Trace API

- Agent State Trace                              	 API

# Agent  State Trace API

## Agent State Trace
                        	 API

Enabling agent trace
                           		allows you to track and report on every state an agent passes through. Use this
                           		feature for short-term tracking of specific agents.

The maximum number
                                       		  of agents with AgentStateTrace on is 100.

### URL

### Operations

list :
                                    				Returns a list of agents whose agent state trace is turned on.

update :
                                    				Updates the agent state trace in the database.

### Parameters

refURL: The
                                    				refURL for agent state trace. See Shared Parameters .

agents: A collection of agent references. Each reference contains person (including firstName, lastName, userName, and loginEnabled
                                    parameters), agent refURL, agentId, supervisor, and agentStateTrace. Agents who are not specified in this collection have
                                    agentStateTrace turned off. To turn off all the agent state trace, pass in an empty list. See References .

### Example Get
                              		  Response

```
<agentstatetrace>
   <refURL>/unifiedconfig/config/agentstatetrace</refURL>
      <agents>
           <agent xsi:type="agentSummary">
                 <refURL>/unifiedconfig/config/agent/10884</refURL>
                 <agentId>4294305</agentId>
                 <agentStateTrace>true</agentStateTrace>
                 <description>Here is a descr</description>
                 <person>
                   <firstName>John</firstName>
                   <lastName>Doe</lastName>
                   <loginEnabled>true</loginEnabled>
                   <userName>jdoe</userName>
                 </person>
               <supervisor>false</supervisor>
           </agent>
      </agents>
 </agentstatetrace>
```

| Note | The maximum number
                                       		  of agents with AgentStateTrace on is 100. |
|---|---|