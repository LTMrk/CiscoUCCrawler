---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb-12-5-installation-guide-ccvp-b-125-9d91f2b913
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/VVB_12_5/installation/guide/ccvp_b_1251-migration-guide-for-cisco-virtualized-voice-browser-release-1251/ccvp_b_1251-migration-guide-for-cisco-virtualized-voice-browser-release-1251_chapter_0110.html
retrieved_at: 2026-08-21T16:28:21.500517+00:00
---

Migration Guide for Cisco Virtualized Voice Browser, Release 12.5(1)

# Migration Guide for Cisco Virtualized Voice Browser, Release 12.5(1)

Updated: January 31, 2020

Chapter: High Availability Consideration

## Chapter: High Availability Consideration

# High Availability Consideration

## High availability
                        	 Consideration

In Cisco VVB there are two types of high availability models:

Comprehensive

Standalone

### Comprehensive
                           	 Model

Cisco Virtualized Voice Browser is a single node and there is no high availability inbuilt for active redundancy. In order
                              to improve level of availability and to eliminate single point of failure, deploy additional Cisco VVB(s) to build passive
                              redundancy by including the additional Cisco VVB(s) in the CVP SIP Server group.

When CVP detects failure of one of the Cisco VVB's in the SIP Server
                              		group, CVP will continue to route calls to remaining active Cisco VVBs,
                              		thereby, allowing new calls to be accepted.

All active calls on the failed Cisco VVB will disconnect and all the
                                          		  call data is lost.

When the failed Cisco VVB recovers and is detected by CVP heartbeat
                              		mechanism, CVP will start routing calls to the recovered Cisco VVB. So by
                              		deploying redundant Cisco VVBs, you can manage unscheduled and scheduled
                              		downtime of one of the Cisco VVBs.

### Standalone
                           	 Model

For standalone call
                              		model, user can configure primary and secondary VXML servers for an
                              		application. On arrival of a new call, if the primary server fails to respond
                              		to new session request, Cisco VVB will attempt to establish new session with
                              		the secondary server. If VXML server goes down when a session is already
                              		established, Cisco VVB will play a critical error message as part of error
                              		handling.

In order to improve level of availability and to eliminate single point of failure, deploy additional Cisco VVB(s) to build
                              passive redundancy. One of the methods by which this can be done is by including the additional Cisco VVB(s) in the Ingress
                              GWs dial-peer configuration. For this create ‘voice class uri’ for ‘VVB’ and then add dial-peers for various VVBs which define
                              destination session target for the uri ‘VVB’ (refer to IOS-GW documentation for more details). This way the Ingress GW will
                              load balance between the various deployed VVBs and if any of the VVB serving standalone call model fails, then Ingress-GW
                              will continue to route new calls to remaining active VVBs.

Survivability is currently unavailable for Standalone Model
                                          		  deployment.

| Note | All active calls on the failed Cisco VVB will disconnect and all the
                                          		  call data is lost. |
|---|---|

| Note | Survivability is currently unavailable for Standalone Model
                                          		  deployment. |
|---|---|