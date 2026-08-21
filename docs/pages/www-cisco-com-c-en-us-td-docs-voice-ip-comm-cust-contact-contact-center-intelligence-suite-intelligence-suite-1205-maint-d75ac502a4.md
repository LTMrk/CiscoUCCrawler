---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-1205-maint-d75ac502a4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_1205/maintain_and_operate/guide/cuic_b_admin-console-user-guide-1205/cuic_b_admin-console-user-guide-1205_appendix_01100.html
retrieved_at: 2026-08-21T04:37:45.718963+00:00
---

Administration Console User Guide for Cisco Unified Intelligence Center, Release 12.5(1)

# Administration Console User Guide for Cisco Unified Intelligence Center, Release 12.5(1)

Updated: January 31, 2020

Chapter: Load Balance

## Chapter: Load Balance

- Load Balance

- Load Balance

# Load Balance

## Load Balance

In cases where a
                              		  Unified Intelligence Center multi-node deployment experiences a heavy reporting
                              		  workload, system administrators have the option to deploy server load balancing
                              		  (SLB).

SLB is a technique
                              		  to distribute client requests among the nodes in a cluster or to select the
                              		  server that can successfully fulfill a client request in the shortest time
                              		  without overloading that server or the cluster as a whole.

In a Unified
                                          			 Intelligence Center deployment with SLB, if one of Unified Intelligence Center
                                          			 is down, the report viewer pointing to that server displays this error Report
                                             				execution Failed. Please check browser console logs for more info .
                                          			 When you perform a browser refresh a new Unified Intelligence Center log in
                                          			 page will display.

Load balancing
                                          			 for Live Data reports in Unified Intelligence Center is not supported in any
                                          			 deployments.

| Note | In a Unified
                                          			 Intelligence Center deployment with SLB, if one of Unified Intelligence Center
                                          			 is down, the report viewer pointing to that server displays this error Report
                                             				execution Failed. Please check browser console logs for more info .
                                          			 When you perform a browser refresh a new Unified Intelligence Center log in
                                          			 page will display. |
|---|---|

| Note | Load balancing
                                          			 for Live Data reports in Unified Intelligence Center is not supported in any
                                          			 deployments. |
|---|---|