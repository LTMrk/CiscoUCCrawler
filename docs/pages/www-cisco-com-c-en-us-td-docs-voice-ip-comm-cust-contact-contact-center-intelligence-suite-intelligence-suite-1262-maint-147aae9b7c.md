---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-1262-maint-147aae9b7c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_1262/maintain_and_operate/guide/cuic_b_1262-admin-console-user-guide/cuic_m_1261_load-balance.html
retrieved_at: 2026-08-21T04:40:38.635094+00:00
---

Administration Console User Guide for Cisco Unified Intelligence Center, Release 12.6(2)

# Administration Console User Guide for Cisco Unified Intelligence Center, Release 12.6(2)

Updated: April 28, 2023

Chapter: Load Balance

## Chapter: Load Balance

- Load Balance

- Load Balance

# Load Balance

## Load Balance

In cases where a Unified Intelligence Center multi-node deployment experiences a heavy reporting workload, system administrators
                              have the option to deploy server load balancing (SLB).

SSO access to the Unified Contact Center Enterprise web applications through the load balancer is not qualified.

SLB is a technique to distribute client requests among the nodes in a cluster or to select the server that can successfully
                              fulfill a client request in the shortest time without overloading that server or the cluster as a whole.

In a Unified Intelligence Center deployment with SLB, if one of Unified Intelligence Center is down, the report viewer pointing
                                          to that server displays this error Report execution Failed. Please check browser console logs for more info . When you refresh your browser, a new Unified Intelligence Center log in page will display.

Load balancing for Live Data reports in Unified Intelligence Center is not supported in any deployments.

| Note | SSO access to the Unified Contact Center Enterprise web applications through the load balancer is not qualified. |
|---|---|

| Note | In a Unified Intelligence Center deployment with SLB, if one of Unified Intelligence Center is down, the report viewer pointing
                                          to that server displays this error Report execution Failed. Please check browser console logs for more info . When you refresh your browser, a new Unified Intelligence Center log in page will display. |
|---|---|

| Note | Load balancing for Live Data reports in Unified Intelligence Center is not supported in any deployments. |
|---|---|