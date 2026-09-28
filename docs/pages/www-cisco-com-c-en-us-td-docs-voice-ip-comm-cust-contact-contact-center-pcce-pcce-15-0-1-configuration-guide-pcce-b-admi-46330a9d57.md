---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-15-0-1-configuration-guide-pcce-b-admi-46330a9d57
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_15_0_1/configuration/guide/pcce_b_admin-and-config-guide-15_0_1/pcce_m_troubleshooting_15_0.html
retrieved_at: 2026-08-21T16:51:15.913155+00:00
---

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Troubleshooting

## Chapter: Troubleshooting

# Troubleshooting

## Packaged CCE
                        	 Logs

You can download
                              		  several types of Packaged CCE log files from the Unified CCE Administration
                              		  interface.

### System Validation Logs

When you configure your deployment, if either the server or any of the VMs do not meet requirements, you see a message indicating
                              connection problems. This message has a link to a log file. Open this file to see whether the servers are valid and whether
                              all VMs match the deployment profiles.

Sample log file showing summary of invalid results:

```
VM Validation Results: Wed Aug 20 08:05:36 EDT 2012
Overall: false
Valid Systems: 0 of 1
Summary:
ESX Server: sideB
ESX Server Properties Valid: true
VM Layout Valid: false.
```

The information at the top of the log is a summary of the results. This log shows that the server is valid but the VM layout
                              is not.

Sample log showing invalid server

This shows that the server does not have the required number of CPU Cores.

```
Server Result:
Required Version: 5.0.0
Required Min CPU Cores: 20
Required Min Memory (MB): 95000
Required HD(s) (GB): [1392, 1949, 273]
Required Bios <Major version>: C260
Required Vendor: Cisco Systems Inc
Found Version: 5.0.0
Found CPU Cores: 10
Found Memory (MB): 98185
Found HD(s) (GB): [1392, 273, 1949]
Found Bios: C260.1.4.2b.0.102620111637
Found Vendor: Cisco Systems Inc
```

There are three log entries for invalid VMS:

Required Profiles without Matching Virtual Machines

This means system does not have VMs present that match our requirements

Optional Profiles without Matching Virtual Machines

This means that the CVP Reporting profile, which is defined as optional, does not exist on the system. This does not block
                                    validation.

Virtual Machines without Matching Profiles

This means the system has VMs that do not match requirements. They might be extra VMs or incorrectly-configured VMs.

Sample log showing valid VM

```
Virtual Machines Matching Defined Profiles:
VM: BB-CCE-AW-A
Profile: Unified CCE Data Server
CPU Cores: 4
Reservation: 5100
RAM (MB): 8192
HD(s) (GB): [80, 750]
VMWare Tools Version: 8384
```

### Bulk Job
                              		  Logs

A log file is generated for each bulk job. The log file is retained until the bulk job is deleted and contains details about
                              each operation that was performed, as well as a summary indicating whether the bulk job completed successfully or failed.

Follow this
                              		  procedure to open the log:

Open the Bulk
                                    				Jobs tool.

From the List of
                                    				Bulk Jobs, click the ID to go to the View Bulk Job page.

Click Log File Download . If the job is still processing, click Download again to review the updates as the job progresses.

You must authenticate to open or save this file.

The Download button is disabled if the bulk job was created using Unified CCE Administration on an AW host that is different from the
                                    host on which the job is being viewed.

Sample log file:

```
2016-06-27T17:20:19-04:00 - Job created
2016-06-27T17:20:19-04:00 - Job started
2016-06-27T17:20:19-04:00 - Processing line 1: Header
2016-06-27T17:20:19-04:00 - Processing line 2: operation=CREATE, agentId=1000, userName=asmith, 
firstName=Agent, lastName=Smith, password=secret, loginEnabled=true, ssoEnabled=false, 
description=Agent Smith, agentStateTrace=false,agentDeskSettingsName=Default_Agent_Desk_Settings, 
agentTeamName=robots, skillGroups=sg1;sg2, defaultSkillGroup=sg1, attributes=, supervisor=false, 
supervisorTeams=, departmentName=
2016-06-27T17:20:20-04:00 - Created /unifiedconfig/config/agentteam/6348
2016-06-27T17:20:20-04:00 - Created /unifiedconfig/config/skillgroup/13515
2016-06-27T17:20:21-04:00 - Created /unifiedconfig/config/skillgroup/13516
2016-06-27T17:20:21-04:00 - Created /unifiedconfig/config/agent/13517
2016-06-27T17:20:21-04:00 - Processing line 3: operation=UPDATE, agentId=, userName=neo@cisco.com, 
firstName=Mister, lastName=Anderson, password=passw0rd, loginEnabled=true, ssoEnabled=false, 
description=Neo, agentStateTrace=true,agentDeskSettingsName=~, agentTeamName=~, skillGroups=, 
defaultSkillGroup=~, attributes=kungFu=9; actuallyKnowsKungFu=false, supervisor=true, 
supervisorTeams=team1;team2, departmentName=department1
2016-06-27T17:20:21-04:00 - Error processing line 3: agentUserName: The specified agent userName 
does not exist neo@cisco.com.
2016-06-27T17:20:21-04:00 - Processing line 4: operation=UPDATE, agentId=1001, userName=, firstName=, 
lastName=, password=, loginEnabled=, ssoEnabled=, description=, agentStateTrace=,agentDeskSettingsName=, 
agentTeamName=, skillGroups=, defaultSkillGroup=, attributes=, supervisor=, supervisorTeams=, 
departmentName=
2016-06-27T17:20:21-04:00 - Error processing line 4: agentId: The specified agent Id does not exist 1001.
2016-06-27T17:20:21-04:00 - Processing line 5: operation=DELETE, agentId=1001, userName=, firstName=, 
lastName=, password=, loginEnabled=, ssoEnabled=, description=, agentStateTrace=,agentDeskSettingsName=, 
agentTeamName=, skillGroups=, defaultSkillGroup=, attributes=, supervisor=, supervisorTeams=, 
departmentName=
2016-06-27T17:20:21-04:00 - Error processing line 5: agentId: The specified agent Id does not exist 1001.
2016-06-27T17:20:21-04:00 - Processing line 6: operation=DELETE, agentId=, userName=jsmith, firstName=, 
lastName=, password=, loginEnabled=, ssoEnabled=, description=, agentStateTrace=,agentDeskSettingsName=, 
agentTeamName=, skillGroups=, defaultSkillGroup=, attributes=, supervisor=, supervisorTeams=, 
departmentName=
2016-06-27T17:20:21-04:00 - Error processing line 6: agentUserName: The specified agent userName does not 
exist jsmith.
2016-06-27T17:20:21-04:00 - Job partially completed due to errors
2016-06-27T17:20:21-04:00 - 5 lines processed, 1 succeeded, 4 failed
2016-06-27T17:20:21-04:00 - 1 agent teams created, 1 agents created, 2 skill groups created
```

## Character Sets

If you installed
                              		  the Language Pack, the Sign-In window includes a Language drop-down menu. The
                              		  drop-down menu includes more than a dozen languages. Select any one of them to
                              		  see the Unified CCE Administration interface and online help in that language.

You must enter
                              		  characters that the database recognizes in the Description field in all tools and in the First
                                 			 Name and Last
                                 			 Name fields in the Agent tool. If you do not, you see an error
                              		  message which states that "The system does
                                 			 not support these characters."

## System Performance
                        	 During Database Updates

### Saving,
                              		  Editing, and Deleting

The addition,
                           		update, or deletion of any object triggers a database update. The system can
                           		process a single update at a time. When an update is already in progress, the
                           		system queues subsequent pending updates.

While updates are
                           		pending or in progress, a spinning wheel, indicating progress, appears on the
                           		window during a save or deletion.

If an update fails, you see an error message appear indicating that your record was
                           		not saved or deleted. You do not need to refresh or navigate away from the
                           		page. You can try the save or delete action again.

### Validation and
                              		  Capacity Checks

The system
                              		  performs the following checks when you initially save or edit and when you
                              		  confirm a deletion. It performs the same two checks when the transaction
                              		  reaches the head of the queue and is about to be written to the database.

Validation
                                    				check. The initial validation checks if a required field is missing or if a
                                    				field contains too many characters or invalid characters. The second validation
                                    				ensures system integrity. For example, are you adding an agent to an agent team
                                    				that was just deleted?

Capacity
                                    				check.

If the transaction
                              		  fails either check, an error message alerts you to the validation error or
                              		  capacity restriction.