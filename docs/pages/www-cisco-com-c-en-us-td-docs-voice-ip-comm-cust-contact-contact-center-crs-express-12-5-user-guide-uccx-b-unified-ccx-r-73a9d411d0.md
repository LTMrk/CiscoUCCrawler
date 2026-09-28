---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-user-guide-uccx-b-unified-ccx-r-73a9d411d0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/user/guide/uccx_b_unified-ccx-reporting-user-guide-125/uccx_b_unified-ccx-reporting-user-guide-125_appendix_01100.html
retrieved_at: 2026-08-16T21:27:01.180638+00:00
---

Cisco Unified Contact Center Express Reporting User Guide, Release 12.5(1)

# Cisco Unified Contact Center Express Reporting User Guide, Release 12.5(1)

Updated: January 31, 2020

Chapter: Data Reconciliation between Reports

## Chapter: Data Reconciliation between Reports

- Data Reconciliation between Reports

# Data Reconciliation between Reports

This appendix
                           		  explains the differences between reports in Unified CCX. These differences are
                           		  not limitations of the product but are inherent in the way these reports are
                           		  designed and are intended to work.

## Calls
                           		  Reported

Each report type
                           		  includes different types of calls in its calculations. The following table
                           		  lists the report types and the calls that they include:

Report Type

Report Name

Reported Call Types

ACD Calls

ACD + Non-ACD Calls

Inbound

Outbound 1

Historical reports

Contact Service Queue Activity Report

Y

N

Y

N

CSQ Agent Summary Report

Y

N

Y

N

Agent Detail Report

N

Y

Y

Y

Agent Call Summary Report

N

Y

Y

Y

Agent Summary Report

Y

N

Y

N

Detailed Call by Call CCDR Report

N

Y

Y

Y

Detailed Call CSQ Agent Report

N

Y

Y

Y

## Consult
                           		  Transfer

Consult transfer
                           		  is reported in different ways in different reports. Consider the following call
                           		  flow.

Call Flow Example

A caller calls
                           		  into a Call Center Route Point, which queues the call in CSQ and routes it to
                           		  agent1. Agent1 talks to the caller, initiates a consult transfer to agent2,
                           		  talks to agent2, and completes the transfer. Agent2 talks to the caller and
                           		  then drops the call.

This scenario will be reported as follows:

Report

Data Presented

Detailed Call by Call CCDR Report (System perspective)

One call record with type = 1 (incoming) for the call between the caller and agent1.

One call record with type = 3 (internal) for the consult call between the two agents.

One call record with type = 5 (transferred-in) for the call between the caller and agent2.

Agent Detail Report (Agent perspective)

For agent1:

One call record for call with the caller (Inbound + transfer-out) to indicate that this call was transferred out to another
                                                   agent.

One call record for the consult call with agent2 (outbound).

For agent2:

One call record for the consult call with agent1 (Inbound Non-ACD). Consult calls are always Non-ACD in Historical reports.

One call record for the call with the caller (Inbound + transfer-in) to indicate that a transferred call was received.

| Report Type | Report Name | Reported Call Types |
|---|---|---|
| ACD Calls | ACD + Non-ACD Calls | Inbound | Outbound 1 |
| Historical reports | Contact Service Queue Activity Report | Y | N | Y | N |
| CSQ Agent Summary Report | Y | N | Y | N |
| Agent Detail Report | N | Y | Y | Y |
| Agent Call Summary Report | N | Y | Y | Y |
| Agent Summary Report | Y | N | Y | N |
| Detailed Call by Call CCDR Report | N | Y | Y | Y |
| Detailed Call CSQ Agent Report | N | Y | Y | Y |

| Report | Data Presented |
|---|---|
| Detailed Call by Call CCDR Report (System perspective) | One call record with type = 1 (incoming) for the call between the caller and agent1. One call record with type = 3 (internal) for the consult call between the two agents. One call record with type = 5 (transferred-in) for the call between the caller and agent2. |
| Agent Detail Report (Agent perspective) | For agent1: One call record for call with the caller (Inbound + transfer-out) to indicate that this call was transferred out to another
                                                   agent. One call record for the consult call with agent2 (outbound). For agent2: One call record for the consult call with agent1 (Inbound Non-ACD). Consult calls are always Non-ACD in Historical reports. One call record for the call with the caller (Inbound + transfer-in) to indicate that a transferred call was received. |