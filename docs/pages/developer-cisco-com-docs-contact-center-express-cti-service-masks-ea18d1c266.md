---
doc_id: developer-cisco-com-docs-contact-center-express-cti-service-masks-ea18d1c266
source_url: https://developer.cisco.com/docs/contact-center-express/cti-service-masks/
retrieved_at: 2026-09-07T14:05:17.485049+00:00
---

# CTI Service Masks

CTI service masks specify the CTI services that the client
		  requests.

Mask name

Description

Bytes

CTI_SERVICE_CLIENT_EVENTS

Client receives call and agent state change events
					 associated with a specific phone.

This bit is used to indicate the client is in agent
					 mode. This bit cannot be set if CTI_SERVICE_ALL_EVENT is
					 set.

0x00000001

CTI_SERVICE_CALL_DATA_UPDATE

Client can modify call context data.

0x00000002

CTI_SERVICE_CLIENT_CONTROL

Client can control calls and agent states
					 associated with a specific phone.

0x00000004

CTI_SERVICE_ALL_EVENTS

Client receives all call and agent-state change
					 events (associated with any phone).

This is the bit to indicate that the client is in
					 bridge mode. This bit cannot be set when CTI_SERVICE_CLIENT_EVENTS is set.

0x00000010

CTI_SERVICE_SUPERVISOR

Client can perform agent supervisory functions.

0x00000080

CTI_AGENT_STATE_CONTROL_ONLY (Version 12)

Client can perform agent state control functions.

0x00002000

CTI_SERVICE_CONFIG_EVENTS

Requests that this client receive configuration
					 events.

0x00040000

| Mask name | Description | Bytes |
|---|---|---|
| CTI_SERVICE_CLIENT_EVENTS | Client receives call and agent state change events
					 associated with a specific phone. This bit is used to indicate the client is in agent
					 mode. This bit cannot be set if CTI_SERVICE_ALL_EVENT is
					 set. | 0x00000001 |
| CTI_SERVICE_CALL_DATA_UPDATE | Client can modify call context data. | 0x00000002 |
| CTI_SERVICE_CLIENT_CONTROL | Client can control calls and agent states
					 associated with a specific phone. | 0x00000004 |
| CTI_SERVICE_ALL_EVENTS | Client receives all call and agent-state change
					 events (associated with any phone). This is the bit to indicate that the client is in
					 bridge mode. This bit cannot be set when CTI_SERVICE_CLIENT_EVENTS is set. | 0x00000010 |
| CTI_SERVICE_SUPERVISOR | Client can perform agent supervisory functions. | 0x00000080 |
| CTI_AGENT_STATE_CONTROL_ONLY (Version 12) | Client can perform agent state control functions. | 0x00002000 |
| CTI_SERVICE_CONFIG_EVENTS | Requests that this client receive configuration
					 events. | 0x00040000 |