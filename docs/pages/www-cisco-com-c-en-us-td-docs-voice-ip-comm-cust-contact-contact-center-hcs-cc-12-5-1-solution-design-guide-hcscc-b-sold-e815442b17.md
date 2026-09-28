---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-hcs-cc-12-5-1-solution-design-guide-hcscc-b-sold-e815442b17
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/hcs-cc/12_5_1/Solution_Design_Guide/hcscc_b_soldg-for-hcs-cc-12_5/hcscc_b_soldg-for-hcs-cc-12_5_chapter_01101.html
retrieved_at: 2026-08-21T23:55:04.656320+00:00
---

Solution Design Guide for Cisco Hosted Collaboration Solution for Contact Center, Release 12.5

# Solution Design Guide for Cisco Hosted Collaboration Solution for Contact Center, Release 12.5

Updated: February 16, 2020

Chapter: Avaya PG

## Chapter: Avaya PG

# Avaya PG

## Avaya PG

Cisco Unified
                           		Intelligent Contact Management (Unified ICM) Peripheral Gateway (PG) supports
                           		Avaya Automatic Call Distributor (ACD). Avaya PG is the component that
                           		communicates to the Avaya ACD device that has agents on it. Avaya PG supports
                           		ACD using CVLAN (Call Visor LAN) Service, running on Avaya Application
                           		Enablement Services (AES). CVLAN is an Avaya software option that allows the
                           		Unified ICM PG to communicate with the Avaya ACD. CVLAN also allows the PG to
                           		perform Post-Routing, station monitoring, and third-party call control. For
                           		more information about Avaya PG, see Avaya PG Considerations .

Avaya PG is an
                                       		  optional cisco component supported for 4000 and 12000 agent deployments only.
                                       		  Each Avaya PG is counted towards the total number of supported PGs.

### Avaya PG
                           	 Considerations

Avaya PG Design Considerations

Avaya PG High Availability

#### Avaya PG Design
                              	 Considerations

The following table
                                 		includes the deployment consideration for Avaya PG. The Avaya PG is supported
                                 		only in 4000 and 12000 agent deployment models.

#### Avaya PG High
                              	 Availability

When PG(PIM) side
                                    		  A fails, PG(PIM) side B becomes active. Agents who are on call continues, with
                                    		  no third-party call control (conference, transfer, and so on) available from
                                    		  their agent desktop. During the failover to the B-Side PIM. Agents who are not
                                    		  on a call, CTI desktop disable their agent state or third-party call control
                                    		  buttons on the desktop. After the failover completes, the agent desktop buttons
                                    		  are restored. When PG side A recovers, the PIM does not fall-back, PG side B
                                    		  remains active and call processing continues.

| Note | Avaya PG is an
                                       		  optional cisco component supported for 4000 and 12000 agent deployments only.
                                       		  Each Avaya PG is counted towards the total number of supported PGs. |
|---|---|

| Feature/Call Flow | Design
                                          				  Considerations |
|---|---|
| Agent
                                          				  Reporting | Supported |
| Duplexed PG Implementation | Supported |
| Unified
                                          				  ICM web Option | Supported |
| Straight Calls | Supported |
| Transfer Calls | Supported |
| Conference Calls | Supported |
| Translation Route | Supported |
| Remote
                                          				  Silent Monitoring (RSM) | Not
                                          				  Supported |
| Multimedia support (ECE) | Not
                                          				  Supported |
| Precision Queues | Not
                                          				  Supported |
| Finesse
                                          				  Desktop support | Not
                                          				  Supported |
| Outbound | Not
                                          				  Supported |
| Split PG
                                          				  over WAN | Not
                                          				  Supported |
| Avaya
                                          				  ACD remote from PG | Not
                                          				  Supported |
| Extension Digits Supported | 10 |
| Agents
                                          				  per PG | 2000 |
| Maximum
                                          				  Skills per agent | 20 |
| Maximum
                                          				  UII size | 40 bytes |