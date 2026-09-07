---
doc_id: developer-cisco-com-docs-contact-center-express-agent-state-masks-8fb85ec9b4
source_url: https://developer.cisco.com/docs/contact-center-express/agent-state-masks/
retrieved_at: 2026-09-07T14:05:27.102661+00:00
---

# Agent State Masks

The Agent state masks specify the agent state messages that
		  the client requests.

Mask name

Description

Value

AGENT_LOGIN_MASK

Set when client wishes to receive "login" AGENT_STATE_EVENT messages.

0x00000001

AGENT_LOGOUT_MASK

Set when client wishes to receive "logout" AGENT_STATE_EVENT messages.

0x00000002

AGENT_NOT_READY_MASK

Set when client wishes to receive "not ready" AGENT_STATE_EVENT messages.

0x00000004

AGENT_AVAILABLE_MASK

Set when client wishes to receive "available" AGENT_STATE_EVENT messages.

0x00000008

AGENT_TALKING_MASK

Set when client wishes to receive "talking" AGENT_STATE_EVENT messages.

0x00000010

AGENT_WORK_MASK

Set when client wishes to receive "work" AGENT_STATE_EVENT messages.

0x00000020

AGENT_TALKING_PENDING_WORK_MASK

Set when client wishes to receive "talking pending
					 work" AGENT_STATE_EVENT messages.

0x00000040

AGENT_TALKING_PENDING_NOT_READY_MASK

Set when client wishes to receive "talking pending not ready" AGENT_STATE_EVENT messages.

0x00000080

AGENT_RESERVED_MASK

Set when client wishes to receive "reserved" AGENT_STATE_EVENT messages.

0x00000100

| Mask name | Description | Value |
|---|---|---|
| AGENT_LOGIN_MASK | Set when client wishes to receive "login" AGENT_STATE_EVENT messages. | 0x00000001 |
| AGENT_LOGOUT_MASK | Set when client wishes to receive "logout" AGENT_STATE_EVENT messages. | 0x00000002 |
| AGENT_NOT_READY_MASK | Set when client wishes to receive "not ready" AGENT_STATE_EVENT messages. | 0x00000004 |
| AGENT_AVAILABLE_MASK | Set when client wishes to receive "available" AGENT_STATE_EVENT messages. | 0x00000008 |
| AGENT_TALKING_MASK | Set when client wishes to receive "talking" AGENT_STATE_EVENT messages. | 0x00000010 |
| AGENT_WORK_MASK | Set when client wishes to receive "work" AGENT_STATE_EVENT messages. | 0x00000020 |
| AGENT_TALKING_PENDING_WORK_MASK | Set when client wishes to receive "talking pending
					 work" AGENT_STATE_EVENT messages. | 0x00000040 |
| AGENT_TALKING_PENDING_NOT_READY_MASK | Set when client wishes to receive "talking pending not ready" AGENT_STATE_EVENT messages. | 0x00000080 |
| AGENT_RESERVED_MASK | Set when client wishes to receive "reserved" AGENT_STATE_EVENT messages. | 0x00000100 |