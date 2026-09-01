---
doc_id: developer-cisco-com-docs-contact-center-express-open-conf-78f0d5ded4
source_url: https://developer.cisco.com/docs/contact-center-express/open_conf/
retrieved_at: 2026-09-01T17:33:42.682109+00:00
---

# OPEN_CONF

The OPEN_CONF message, defined in the following tables,
		  confirms the completion of the processing requested by the OPEN_REQ message.

Fixed part

Field name

Value

Data type

Maximum size

InvokeID

The InvokeID from the corresponding OPEN_REQ
					 message.

UINT

4

ServicesGranted

A bitwise combination of the CTI Services listed in CTI Service Masks that the client has
					 been granted. Services granted can be less than those requested.

UINT

4

reserved

Zero.

UINT

4

reserved

Zero.

UINT

4

reserved

Zero.

TIME

4

Unified CCX Online

The current Unified CCX on-line status when client
					 EVENTS service has been granted.

1: online 0: offline

BOOL

2

reserved

Zero.

USHORT

2

AgentState

The value representing the current state of the associated agent (see Table 1 ).

USHORT

2

Floating part

Field name

Value

Data type

Maximum size

AgentExtension [4]

The agent’s IP phone extension, when client EVENTS
					 service has been granted and the agent is currently logged into Unified CCX.

This field is required for Agent mode.

STRING

16

reserved [5]

Ignore this value.

STRING

12

AgentInstrument [6]

The agent’s IP phone number, when client EVENTS
					 service has been granted and the agent is currently logged into Unified CCX.

This field is required for Agent mode.

STRING

64

AgentID [194]

The agent’s Unified CCX login.

This field is required for Agent mode.

STRING

129

NumPeripherals [228]

(Version 14 and later)

The number of FltPeripheralID and
					 MultilineAgentControl pairs specified in the floating portion of the message.
					 For Unified CCX, this is always 1.

USHORT

2

FltPeripheralID [208]

(Version 14 and later)

The Peripheral ID for the MultilineAgentControl
					 field. For Unified CCX, this is the peripheral ID given by the OPEN_REQ.

UINT

4

MultilineAgentControl [224]

(Version 14 and later)

Specifies if multi-line agent control is available
					 on the above peripheral. For Unified CCX, this is always 1.

USHORT

2

ConfigMsgMaskGranted [248]

(Version 18 and later)

Indicates the types of configuration events that the CTI server sends to the CTI clients. For Unified CCX, the configuration event masks are listed in Table 1 .

USHORT

2

| Fixed part Field name | Value | Data type | Maximum size |
|---|---|---|---|
| InvokeID | The InvokeID from the corresponding OPEN_REQ
					 message. | UINT | 4 |
| ServicesGranted | A bitwise combination of the CTI Services listed in CTI Service Masks that the client has
					 been granted. Services granted can be less than those requested. | UINT | 4 |
| reserved | Zero. | UINT | 4 |
| reserved | Zero. | UINT | 4 |
| reserved | Zero. | TIME | 4 |
| Unified CCX Online | The current Unified CCX on-line status when client
					 EVENTS service has been granted. 1: online 0: offline | BOOL | 2 |
| reserved | Zero. | USHORT | 2 |
| AgentState | The value representing the current state of the associated agent (see Table 1 ). | USHORT | 2 |

| Floating part Field name | Value | Data type | Maximum size |
|---|---|---|---|
| AgentExtension [4] | The agent’s IP phone extension, when client EVENTS
					 service has been granted and the agent is currently logged into Unified CCX. This field is required for Agent mode. | STRING | 16 |
| reserved [5] | Ignore this value. | STRING | 12 |
| AgentInstrument [6] | The agent’s IP phone number, when client EVENTS
					 service has been granted and the agent is currently logged into Unified CCX. This field is required for Agent mode. | STRING | 64 |
| AgentID [194] | The agent’s Unified CCX login. This field is required for Agent mode. | STRING | 129 |
| NumPeripherals [228] (Version 14 and later) | The number of FltPeripheralID and
					 MultilineAgentControl pairs specified in the floating portion of the message.
					 For Unified CCX, this is always 1. | USHORT | 2 |
| FltPeripheralID [208] (Version 14 and later) | The Peripheral ID for the MultilineAgentControl
					 field. For Unified CCX, this is the peripheral ID given by the OPEN_REQ. | UINT | 4 |
| MultilineAgentControl [224] (Version 14 and later) | Specifies if multi-line agent control is available
					 on the above peripheral. For Unified CCX, this is always 1. | USHORT | 2 |
| ConfigMsgMaskGranted [248] (Version 18 and later) | Indicates the types of configuration events that the CTI server sends to the CTI clients. For Unified CCX, the configuration event masks are listed in Table 1 . | USHORT | 2 |