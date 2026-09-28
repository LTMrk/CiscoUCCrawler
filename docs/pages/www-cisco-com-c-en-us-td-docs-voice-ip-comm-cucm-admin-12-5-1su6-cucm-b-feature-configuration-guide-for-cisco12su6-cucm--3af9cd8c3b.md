---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su6-cucm-b-feature-configuration-guide-for-cisco12su6-cucm--3af9cd8c3b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU6/cucm_b_feature-configuration-guide-for-cisco12su6/cucm_b_feature-configuration-guide-for-cisco1251su3_chapter_01100.html
retrieved_at: 2026-08-16T16:35:52.985463+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: October 8, 2025

Chapter: Agent Greeting

## Chapter: Agent Greeting

# Agent Greeting

## Agent Greeting
                        	 Overview

Agent Greeting enables Unified Communications Manager to automatically play a prerecorded announcement following a successful media connection to the agent device. Agent Greeting
                              is audible for the agent and the customer.

The process of recording a greeting is similar to recording a message
                              		  for voicemail. Depending on how your contact center is set up, you can record
                              		  different greetings that play for different types of callers (for example, an
                              		  English greeting for English speakers or an Italian greeting for Italian
                              		  speakers).

By default, agent greeting is enabled when you log in to your agent
                              		  desktop but you can turn it off and on as necessary.

## Agent Greeting
                        	 Prerequisites

Install Cisco Unified Contact Center Enterprise. See Cisco Unified Contact Center Enterprise Installation and Upgrade Guide .

Install Cisco Unified Customer Voice Portal. See Installation and Upgrade Guide for Cisco Unified Customer Voice Portal .

Ensure that you enable Built In Bridge. To view the details, see Configure Built In Bridge .

## Agent Greeting
                        	 Configuration Task Flow

Agent Greeting configuration tasks are completed in Cisco Unified Contact Center Enterprise (Unified CCE) and Cisco Unified
                              Customer Voice Portal (Unified CVP). To view detailed steps for the following tasks, see the Agent Greeting section in the Cisco Unified Contact Center Enterprise Features Guide .

### Before you begin

Review Agent Greeting Prerequisites

Step 1

Configure a
                                       			 media server for Agent Greeting.

- Configure a server to act
                                          				as a media server.

- Add the media server in
                                          				Unified CVP.

- Configure the media server
                                          				to write files.

Step 2

Republish .tcl
                                       			 scripts to Voice Extensible Markup Language (VXML) Gateway.

The .tcl
                                          				script files that ship with Unified CVP Release 9.0(1) include updates to
                                          				support Agent Greeting. You must republish these updated files to your VXML
                                          				Gateway.

Republishing
                                          				scripts to the VXML Gateways is a standard task in Unified CVP upgrades. If you
                                          				did not upgrade Unified CVP and republish the scripts, you must republish the
                                          				scripts before you can use Agent Greeting.

Step 3

Set the cache
                                       			 size on the VXML Gateway.

Step 4

Create voice
                                       			 prompts to record greetings.

Step 5

Configure call
                                       			 types.

Complete to
                                          				record and play agent greetings.

Step 6

Configure a
                                       			 dialed number.

Complete to
                                          				record and play agent greetings.

Step 7

Schedule the
                                       			 script.

Step 8

Define network
                                       			 VRU scripts.

Step 9

(Optional)
                                       			 Import sample Agent Greeting scripts.

Step 10

Modify the
                                       			 Unified CCE call routing scripts.

### Configure Built In
                           	 Bridge

The Built in Bridge field setting in the Phone Configuration window for an individual phone overrides the setting for the Builtin Bridge Enable clusterwide service parameter.

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find to select the agent phone.

Step 3

From the Built in Bridge drop-down list, choose one of the following options:

- On —The Built in Bridge is enabled.

- Off —The Built in Bridge is disabled.

- Default —The setting of the clusterwide Builtin Bridge Enable service parameter is used.

Step 4

Click Save .

## Agent Greeting Troubleshooting

For information about how to troubleshoot Agent Greeting issues, see "Troubleshooting Agent Greeting" chapter in the Agent Greeting and Whisper Announcement Feature Guide for Cisco Unified Contact Center Enterprise guide.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure a
                                       			 media server for Agent Greeting. Configure a server to act
                                          				as a media server. Add the media server in
                                          				Unified CVP. Configure the media server
                                          				to write files. | Agent
                                       			 Greeting uses the Unified CVP media server to store and serve prompt and
                                       			 greeting files. |
| Step 2 | Republish .tcl
                                       			 scripts to Voice Extensible Markup Language (VXML) Gateway. | The .tcl
                                          				script files that ship with Unified CVP Release 9.0(1) include updates to
                                          				support Agent Greeting. You must republish these updated files to your VXML
                                          				Gateway. Republishing
                                          				scripts to the VXML Gateways is a standard task in Unified CVP upgrades. If you
                                          				did not upgrade Unified CVP and republish the scripts, you must republish the
                                          				scripts before you can use Agent Greeting. |
| Step 3 | Set the cache
                                       			 size on the VXML Gateway. | To ensure
                                       			 adequate performance, set the size of the cache on the VXML Gateway to the
                                       			 maximum allowed. The maximum size is 100 megabytes; the default is 15
                                       			 kilobytes. Failure to set the VXML Gateway cache to its maximum can result in
                                       			 slowed performance to increased traffic to the media server. |
| Step 4 | Create voice
                                       			 prompts to record greetings. | Create audio
                                       			 files for each of the voice prompts that agents hear as they record a greeting. |
| Step 5 | Configure call
                                       			 types. | Complete to
                                          				record and play agent greetings. |
| Step 6 | Configure a
                                       			 dialed number. | Complete to
                                          				record and play agent greetings. |
| Step 7 | Schedule the
                                       			 script. |  |
| Step 8 | Define network
                                       			 VRU scripts. | For Agent
                                       			 Greeting record and play scripts to interact with Unified CVP, Network VRU
                                       			 scripts are required. |
| Step 9 | (Optional)
                                       			 Import sample Agent Greeting scripts. |  |
| Step 10 | Modify the
                                       			 Unified CCE call routing scripts. | Modify the
                                       			 Unified CCE call routing scripts to use the Play Agent Greeting script. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find to select the agent phone. |
| Step 3 | From the Built in Bridge drop-down list, choose one of the following options: On —The Built in Bridge is enabled. Off —The Built in Bridge is disabled. Default —The setting of the clusterwide Builtin Bridge Enable service parameter is used. |
| Step 4 | Click Save . |