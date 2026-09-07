---
doc_id: developer-cisco-com-docs-contact-center-express-error-e-status-codes-b3b2793b86
source_url: https://developer.cisco.com/docs/contact-center-express/error-e-status-codes/
retrieved_at: 2026-09-07T14:05:41.515700+00:00
---

# Error (E) Status Codes

Table 1 lists the status
		  codes with their numeric code values that may be included in the FAILURE_CONF
		  and FAILURE_EVENT Unified CCX CTI messages.

Status code

Description

Value

E_CTI_NO_ERROR

No error occurred.

0

E_CTI_INVALID_VERSION

The server does not support the protocol version
					 number requested by the client.

1

E_CTI_INVALID_MESSAGE_TYPE

A message with an invalid message type field was
					 received.

2

E_CTI_INVALID_FIELD

A message with an invalid floating field tag was
					 received.

3

E_CTI_SESSION_NOT_OPEN

No session is currently open on the connection.

4

E_CTI_SESSION_ALREADY_OPEN

A session is already open on the connection.

5

E_CTI_REQUIRED_DATA_MISSING

The request did not include one or more floating
					 items that are required.

6

E_CTI_INVALID_PERIPHERAL_ID

One of the reserved fields in the fixed part of the
					 message is incorrect.

7

E_CTI_INVALID_AGENT_DATA

The provided agent data item(s) are not valid.

8

E_CTI_AGENT_NOT_LOGGED_ON

The indicated agent is not currently logged on.

9

E_CTI_DEVICE_IN_USE

The indicated agent IP phone is already associated
					 with a different client.

10

E_CTI_NEW_SESSION_OPENED

This session is being terminated due to a new
					 session open request from the client.

11

reserved

12

E_CTI_INVALID_CALLID

A request message was received with an invalid
					 CallID value.

13

reserved

14-16

E_CTI_UNSPECIFIED_FAILURE

An unspecified error occurred.

17

E_CTI_INVALID_TIMEOUT

The IdleTimeout field contains a value that less
					 than 20 seconds (4 times the minimum heartbeat interval of 5 seconds).

18

reserved

19-22

E_CTI_INVALID_FIELD_LENGTH

A floating field exceeds the allowable length for
					 that field type.

23

reserved

24-91

E_CTI_SERVER_NOT_MASTER

The server is a standby server.

92

E_CTI_INVALID_CSQ

The specified CSQ is invalid.

93

E_CTI_JTAPI_CCM_PROBLEM

Indicates a JTAPI or Cisco Unified Communications Manager problem.

94

reserved

95

E_CTI_AUTO_CONFIG_RESET

The client needs to resend the
					 CONFIG_REQUEST_KEY_EVENT and the CONFIG_REQUEST_EVENT message.

96

| Status code | Description | Value |
|---|---|---|
| E_CTI_NO_ERROR | No error occurred. | 0 |
| E_CTI_INVALID_VERSION | The server does not support the protocol version
					 number requested by the client. | 1 |
| E_CTI_INVALID_MESSAGE_TYPE | A message with an invalid message type field was
					 received. | 2 |
| E_CTI_INVALID_FIELD | A message with an invalid floating field tag was
					 received. | 3 |
| E_CTI_SESSION_NOT_OPEN | No session is currently open on the connection. | 4 |
| E_CTI_SESSION_ALREADY_OPEN | A session is already open on the connection. | 5 |
| E_CTI_REQUIRED_DATA_MISSING | The request did not include one or more floating
					 items that are required. | 6 |
| E_CTI_INVALID_PERIPHERAL_ID | One of the reserved fields in the fixed part of the
					 message is incorrect. | 7 |
| E_CTI_INVALID_AGENT_DATA | The provided agent data item(s) are not valid. | 8 |
| E_CTI_AGENT_NOT_LOGGED_ON | The indicated agent is not currently logged on. | 9 |
| E_CTI_DEVICE_IN_USE | The indicated agent IP phone is already associated
					 with a different client. | 10 |
| E_CTI_NEW_SESSION_OPENED | This session is being terminated due to a new
					 session open request from the client. | 11 |
| reserved |  | 12 |
| E_CTI_INVALID_CALLID | A request message was received with an invalid
					 CallID value. | 13 |
| reserved |  | 14-16 |
| E_CTI_UNSPECIFIED_FAILURE | An unspecified error occurred. | 17 |
| E_CTI_INVALID_TIMEOUT | The IdleTimeout field contains a value that less
					 than 20 seconds (4 times the minimum heartbeat interval of 5 seconds). | 18 |
| reserved |  | 19-22 |
| E_CTI_INVALID_FIELD_LENGTH | A floating field exceeds the allowable length for
					 that field type. | 23 |
| reserved |  | 24-91 |
| E_CTI_SERVER_NOT_MASTER | The server is a standby server. | 92 |
| E_CTI_INVALID_CSQ | The specified CSQ is invalid. | 93 |
| E_CTI_JTAPI_CCM_PROBLEM | Indicates a JTAPI or Cisco Unified Communications Manager problem. | 94 |
| reserved |  | 95 |
| E_CTI_AUTO_CONFIG_RESET | The client needs to resend the
					 CONFIG_REQUEST_KEY_EVENT and the CONFIG_REQUEST_EVENT message. | 96 |