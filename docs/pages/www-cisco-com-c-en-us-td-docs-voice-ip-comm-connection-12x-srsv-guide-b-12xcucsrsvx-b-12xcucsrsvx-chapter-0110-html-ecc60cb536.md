---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-srsv-guide-b-12xcucsrsvx-b-12xcucsrsvx-chapter-0110-html-ecc60cb536
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/srsv/guide/b_12xcucsrsvx/b_12xcucsrsvx_chapter_0110.html
retrieved_at: 2026-08-21T07:56:09.381276+00:00
---

Complete Reference Guide for Cisco Unity Connection Survivable Remote Site Voicemail (SRSV)

# Complete Reference Guide for Cisco Unity Connection Survivable Remote Site Voicemail (SRSV)

Updated: August 17, 2017

Chapter: Alarm and Events

## Chapter: Alarm and Events

- Alarm and Events

- Unity Connection                              	 SRSV Alarms and Events

# Alarm and Events

## Unity Connection
                        	 SRSV Alarms and Events

The Table
                                 			 7-1 lists the types of alarms and events reported by Unity Connection
                              		  SRSV. The table also provides the explanation for the alarms and the
                              		  recommended actions to prevent the occurence of similar events.

Cisco Unity Connection SRSV Alarms and Events

Alarm Name

Severity

Description

Route To

Explanation

EvtBranchNotReachable

ERROR_ALARM

Branch[name=%1, address=%2] is not reachable

Event Log, Alert Log

There is an issue with the connectivity between the central
                                          						Unity Connection server and the specified branch.

If there is no connectivity between the central Unity Connection
                                          						server and the branch office, see the “Error Message Appears When Testing the
                                          						Connectivity of Unity Connection with Branch" section of the “Troubleshooting
                                          						Unity Connection SRSV” chapter in the Troubleshooting Guide for Cisco Unity
                                          						Connection, Release 11.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/troubleshooting/guide/b_11xcuctsg.html .

If the problem is not resolved then please contact Cisco TAC.

EvtBranchProvisioned

INFORMATIONAL_ALARM

The branch[name=%1, address=%2] has been successfully
                                          						provisioned

Event Log, Alert Log

The branch has been successfully associated with the central
                                          						Unity Connection server.

NONE

EvtBranchProvisioningFailed

WARNING_ALARM

Provisioning for branch[name= %1, address= %2] has failed

Event Log, Alert Log

The provisioning of branch has been failed.

If there is no connectivity between the central Unity Connection
                                          						server and the branch office, see the “Error Message Appears When Testing the
                                          						Connectivity of Unity Connection with Branch” section of the “Troubleshooting
                                          						Unity Connection SRSV” chapter in the Troubleshooting Guide for Cisco Unity
                                          						Connection, Release 11.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/troubleshooting/guide/b_11xcuctsg.html .

If the problem is not resolved then please contact Cisco TAC.

EvtBranchProvisioningFailedMaxRetries

ERROR_ALARM

Provisioning for branch[name= %1, address= %2] has failed after
                                          						maximum %3 retries

Event Log, Alert Log

Provisioning for a branch has failed in all the retries.

If there is no connectivity between the central Unity Connection
                                          						server and the branch office, see the “Error Message Appears When Testing the
                                          						Connectivity of Unity Connection with Branch” section of the “Troubleshooting
                                          						Unity Connection SRSV” chapter in the Troubleshooting Guide for Cisco Unity
                                          						Connection, Release 11.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/troubleshooting/guide/b_11xcuctsg.html .

If the problem is not resolved then please contact Cisco TAC.

EvtBranchProvisioningFailedMaxWait

ERROR_ALARM

A provisioning completion notification was not received for
                                          						branch[name= %1, address= %2] within the maximum wait time of %3 minutes

Event Log, Alert Log

Provisioning for a branch has failed because the branch did not
                                          						return the provisioning completion status within the defined timeframe.

If there is no connectivity between the central Unity Connection
                                          						server and the branch office, see the “Error Message Appears When Testing the
                                          						Connectivity of Unity Connection with Branch” section of the “Troubleshooting
                                          						Unity Connection SRSV” chapter in the Troubleshooting Guide for Cisco Unity
                                          						Connection, Release 11.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/troubleshooting/guide/b_11xcuctsg.html .

If the problem is not resolved then please contact Cisco TAC.

EvtBranchVoiceMailUpload

INFORMATIONAL_ALARM

Voice mail upload for branch[name= %1, address= %2] completed
                                          						successfully. %3 messages were uploaded

Event Log

Voicemails from branch are uploaded on the central Unity
                                          						Connection server.

NONE

EvtBranchVoiceMailUploadFailed

ERROR_ALARM

Voice mail upload for branch[name= %1, address= %2] has failed

Event Log

No voicemail could be uploaded from the branch to the central
                                          						Unity Connection server.

If there is no connectivity between the central Unity Connection
                                          						server and the branch office, see the “Error Message Appears When Testing the
                                          						Connectivity of Unity Connection with Branch” section of the “Troubleshooting
                                          						Unity Connection SRSV” chapter in the Troubleshooting Guide for Cisco Unity
                                          						Connection, Release 11.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/troubleshooting/guide/b_11xcuctsg.html .

If the problem is not resolved then please contact Cisco TAC.

EvtBranchVoiceMailUploadPartial

WARNING_ALARM

Voice mail upload for branch[name= %1, address= %2] partially
                                          						completed. %3 messages out of %4 were uploaded

Event Log

All the voicemails could not be uploaded from branch to the
                                          						central Unity Connection server.

If there is no connectivity between the central Unity Connection
                                          						server and the branch office, see the “Error Message Appears When Testing the
                                          						Connectivity of Unity Connection with Branch” section of the “Troubleshooting
                                          						Unity Connection SRSV” chapter in the Troubleshooting Guide for Cisco Unity
                                          						Connection, Release 11.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/troubleshooting/guide/b_11xcuctsg.html .

If the problem is not resolved then please contact Cisco TAC.

EvtCentralNotReachable

ERROR_ALARM

Central Unity Connection[address= %1] is not reachable

Event Log, Alert Log

There is an issue with the connectivity between the central
                                          						Unity Connection server and the specified branch.

If there is no connectivity between the central Unity Connection
                                          						server and the branch office, see the “Error Message Appears When Testing the
                                          						Connectivity of Unity Connection with Branch” section of the “Troubleshooting
                                          						Unity Connection SRSV” chapter in the Troubleshooting Guide for Cisco Unity
                                          						Connection, Release 11.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/troubleshooting/guide/b_11xcuctsg.html .

If the problem is not resolved then please contact Cisco TAC.

| Alarm Name | Severity | Description | Route To | Explanation |  |
|---|---|---|---|---|---|
| EvtBranchNotReachable | ERROR_ALARM | Branch[name=%1, address=%2] is not reachable | Event Log, Alert Log | There is an issue with the connectivity between the central
                                          						Unity Connection server and the specified branch. | If there is no connectivity between the central Unity Connection
                                          						server and the branch office, see the “Error Message Appears When Testing the
                                          						Connectivity of Unity Connection with Branch" section of the “Troubleshooting
                                          						Unity Connection SRSV” chapter in the Troubleshooting Guide for Cisco Unity
                                          						Connection, Release 11.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/troubleshooting/guide/b_11xcuctsg.html . If the problem is not resolved then please contact Cisco TAC. |
| EvtBranchProvisioned | INFORMATIONAL_ALARM | The branch[name=%1, address=%2] has been successfully
                                          						provisioned | Event Log, Alert Log | The branch has been successfully associated with the central
                                          						Unity Connection server. | NONE |
| EvtBranchProvisioningFailed | WARNING_ALARM | Provisioning for branch[name= %1, address= %2] has failed | Event Log, Alert Log | The provisioning of branch has been failed. | If there is no connectivity between the central Unity Connection
                                          						server and the branch office, see the “Error Message Appears When Testing the
                                          						Connectivity of Unity Connection with Branch” section of the “Troubleshooting
                                          						Unity Connection SRSV” chapter in the Troubleshooting Guide for Cisco Unity
                                          						Connection, Release 11.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/troubleshooting/guide/b_11xcuctsg.html . If the problem is not resolved then please contact Cisco TAC. |
| EvtBranchProvisioningFailedMaxRetries | ERROR_ALARM | Provisioning for branch[name= %1, address= %2] has failed after
                                          						maximum %3 retries | Event Log, Alert Log | Provisioning for a branch has failed in all the retries. | If there is no connectivity between the central Unity Connection
                                          						server and the branch office, see the “Error Message Appears When Testing the
                                          						Connectivity of Unity Connection with Branch” section of the “Troubleshooting
                                          						Unity Connection SRSV” chapter in the Troubleshooting Guide for Cisco Unity
                                          						Connection, Release 11.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/troubleshooting/guide/b_11xcuctsg.html . If the problem is not resolved then please contact Cisco TAC. |
| EvtBranchProvisioningFailedMaxWait | ERROR_ALARM | A provisioning completion notification was not received for
                                          						branch[name= %1, address= %2] within the maximum wait time of %3 minutes | Event Log, Alert Log | Provisioning for a branch has failed because the branch did not
                                          						return the provisioning completion status within the defined timeframe. | If there is no connectivity between the central Unity Connection
                                          						server and the branch office, see the “Error Message Appears When Testing the
                                          						Connectivity of Unity Connection with Branch” section of the “Troubleshooting
                                          						Unity Connection SRSV” chapter in the Troubleshooting Guide for Cisco Unity
                                          						Connection, Release 11.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/troubleshooting/guide/b_11xcuctsg.html . If the problem is not resolved then please contact Cisco TAC. |
| EvtBranchVoiceMailUpload | INFORMATIONAL_ALARM | Voice mail upload for branch[name= %1, address= %2] completed
                                          						successfully. %3 messages were uploaded | Event Log | Voicemails from branch are uploaded on the central Unity
                                          						Connection server. | NONE |
| EvtBranchVoiceMailUploadFailed | ERROR_ALARM | Voice mail upload for branch[name= %1, address= %2] has failed | Event Log | No voicemail could be uploaded from the branch to the central
                                          						Unity Connection server. | If there is no connectivity between the central Unity Connection
                                          						server and the branch office, see the “Error Message Appears When Testing the
                                          						Connectivity of Unity Connection with Branch” section of the “Troubleshooting
                                          						Unity Connection SRSV” chapter in the Troubleshooting Guide for Cisco Unity
                                          						Connection, Release 11.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/troubleshooting/guide/b_11xcuctsg.html . If the problem is not resolved then please contact Cisco TAC. |
| EvtBranchVoiceMailUploadPartial | WARNING_ALARM | Voice mail upload for branch[name= %1, address= %2] partially
                                          						completed. %3 messages out of %4 were uploaded | Event Log | All the voicemails could not be uploaded from branch to the
                                          						central Unity Connection server. | If there is no connectivity between the central Unity Connection
                                          						server and the branch office, see the “Error Message Appears When Testing the
                                          						Connectivity of Unity Connection with Branch” section of the “Troubleshooting
                                          						Unity Connection SRSV” chapter in the Troubleshooting Guide for Cisco Unity
                                          						Connection, Release 11.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/troubleshooting/guide/b_11xcuctsg.html . If the problem is not resolved then please contact Cisco TAC. |
| EvtCentralNotReachable | ERROR_ALARM | Central Unity Connection[address= %1] is not reachable | Event Log, Alert Log | There is an issue with the connectivity between the central
                                          						Unity Connection server and the specified branch. | If there is no connectivity between the central Unity Connection
                                          						server and the branch office, see the “Error Message Appears When Testing the
                                          						Connectivity of Unity Connection with Branch” section of the “Troubleshooting
                                          						Unity Connection SRSV” chapter in the Troubleshooting Guide for Cisco Unity
                                          						Connection, Release 11.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/troubleshooting/guide/b_11xcuctsg.html . If the problem is not resolved then please contact Cisco TAC. |