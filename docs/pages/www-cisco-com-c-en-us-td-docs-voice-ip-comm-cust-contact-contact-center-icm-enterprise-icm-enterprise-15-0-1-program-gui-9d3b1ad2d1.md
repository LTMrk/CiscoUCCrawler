---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-9d3b1ad2d1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_agent-desk-settings-api_1501.html
retrieved_at: 2026-08-21T16:42:53.957656+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Agent Desk Settings API

## Chapter: Agent Desk Settings API

- Agent Desk Settings API

- Agent Desk Settings API

# Agent Desk Settings API

## Agent Desk Settings API

A desk settings is a collection of permissions or characteristics for the agent, such as how and when calls to the agent are
                           redirected, how and when the agent enters various work states, and how requests to the supervisor are handled.

Use the Agent Desk Settings API to list the agent desk settings currently defined in the database, define new agent desk settings,
                           and view, edit, and delete existing agent desk settings.

### URL

### Operations

create : Creates one agent desk settings.

delete : Permanently deletes one agent desk settings.

get : Returns one agent desk settings, using the URL https://<server>/unifiedconfig/config/agentdesksetting/<id> .

list : Retrieves a list of agent desk settings.

update : Updates one agent desk settings.

### Parameters

refURL: The refURL of the agent desk settings. See Shared Parameters .

name: The name of the agent desk settings. See Shared Parameters .

changeStamp: See Shared Parameters .

description: See Shared Parameters .

department: A reference to the department ( Department API ), including refURL and name. See References .

wrapupDataIncomingMode: Indicates whether the agent is allowed or required to enter wrap-up data after an inbound call.

0: Required

1: Optional (Default)

2: Not Allowed

wrapupDataOutgoingMode: Indicates whether the agent is allowed or required to enter wrap-up data after an outbound call.

0: Required

1: Optional (Default)

2: Not Allowed

remoteAgentType: Indicates if agents are allowed to login as remote agents.

0: Not Allowed

1: Call by Call

2: Nailed Up

3: Agent Chooses

logoutNonActivityTime: Number of seconds of non-activity at the desktop after which the software automatically logs out the
                                    agent. Value must be between 10 and 7200 seconds (default is NULL).

workModeTimer: Specifies the auto wrap-up time out. Value must be between 1 and 7200 seconds (default is 7200).

supervisorAssistCallMethod: Indicates how the supervisor assist request call is made.

0: Consultative Call (Default)

1: Blind Conference

emergencyCallMethod: Indicates how the emergency call request is made.

0: Consultative Call (Default)

1: Blind Conference

idleReasonRequired: Indicates whether the agent must enter a reason before entering the Idle state. Values are true/false.

logoutReasonRequired: Indicates whether or not the agent must enter a reason before logging out. Values are true/false.

autoAnswerEnabled: Indicates whether or not calls sent to this agent will be answered automatically. Values are true/false.

agentStateAfterRONA: Indicates the agent state after RONA. Values are notReady or ready.

playZipTone: Indicates to determine whether to play a ziptone when auto answering an inbound call. In order to set this field,
                                    auto answer must be enabled for the desk setting or an APIError will be returned.

ACDSharedLineUsage: Indicates to determine whether the agent will be allowed to log into devices which have a shared ACD line.

### Search and Sort Values

The following table shows the parameters that are searched and the parameters that are sortable.

- name

- description

- name (default)

- description

- wrapupDataIncomingMode

- wrapupDataOutgoingMode

- remoteAgentType

- logoutNonActivityTime

- workModeTimer

- supervisorAssistCallMethod

- emergencyCallMethod

- idleReasonRequired

- logoutReasonRequired

- autoAnswerEnabled

See Search and Sort .

### Example Get Response

```
<agentDeskSetting> <department>
         <refURL>/unifiedconfig/config/department/5000</refURL>
         <name>debit_card</name>
         </department> <refURL>/unifiedconfig/config/agentdesksetting/5001</refURL>
      <changeStamp>3</changeStamp>
      <refURL>/unifiedconfig/config/agentdesksetting/5000</refURL> <agentStateAfterRONA>notReady</agentStateAfterRONA> <autoAnswerEnabled>false</autoAnswerEnabled>
      <emergencyCallMethod>0</emergencyCallMethod>
      <idleReasonRequired>false</idleReasonRequired>
      <logoutReasonRequired>false</logoutReasonRequired>
      <name>Default_Agent_Desk_Settings</name>
      <remoteAgentType>0</remoteAgentType>
      <supervisorAssistCallMethod>0</supervisorAssistCallMethod>
      <workModeTimer>7200</workModeTimer>
      <wrapupDataIncomingMode>1</wrapupDataIncomingMode>
      <wrapupDataOutgoingMode>1</wrapupDataOutgoingMode>
</agentDeskSetting>
```

| Search parameters | Sort parameters |
|---|---|
| name description | name (default) description wrapupDataIncomingMode wrapupDataOutgoingMode remoteAgentType logoutNonActivityTime workModeTimer supervisorAssistCallMethod emergencyCallMethod idleReasonRequired logoutReasonRequired autoAnswerEnabled |