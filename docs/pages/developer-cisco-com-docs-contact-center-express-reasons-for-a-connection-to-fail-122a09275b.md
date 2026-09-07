---
doc_id: developer-cisco-com-docs-contact-center-express-reasons-for-a-connection-to-fail-122a09275b
source_url: https://developer.cisco.com/docs/contact-center-express/reasons-for-a-connection-to-fail/
retrieved_at: 2026-09-07T14:05:03.260099+00:00
---

# Reasons for a Connection to Fail

If for any reason the server determines that a new session must
		not be opened, it responds to the OPEN_REQ message with a FAILURE_CONF message.

The following are some of the reasons a new session might not
		be opened:

If required floating data has not been provided, a FAILURE_CONF
			 message, defined in FAILURE_CONF ,
			 is returned with the status code set to E_CTI_REQUIRED_DATA_MISSING.

If a client attempts to open a session for CLIENT EVENTS service
			 (that is when the client is in Agent Mode — see Two Client Modes for Connecting with Unified CCX )
			 and the provided IP phone information items are not consistent with each other,
			 a FAILURE_CONF message is returned with the status code set to
			 E_CTI_INCONSISTENT_AGENT_DATA.

If the indicated IP phone is already associated with a different
			 client, the server refuses to open the new session and returns a FAILURE_CONF
			 message with the status code set to E_CTI_DEVICE_IN_USE.

If a connection is made to the non-master server, the server will
			 reply with a FAILURE_CONF indicating error E_CTI_SERVER_NOT_MASTER.

That a session does not fail does not mean the client was granted
		  everything requested. The server grants the client only what is available.

| Note | That a session does not fail does not mean the client was granted
		  everything requested. The server grants the client only what is available. |
|---|---|