---
doc_id: developer-cisco-com-docs-contact-center-express-how-a-clientserver-connection-is-managed-3125fbad71
source_url: https://developer.cisco.com/docs/contact-center-express/how-a-clientserver-connection-is-managed/
retrieved_at: 2026-09-01T17:33:24.667332+00:00
---

# How a Client/Server Connection is Managed

The client uses TCP/IP protocols for network connectivity to
		the Unified CCX server.

TCP/IP transport services are used in a client/server
		arrangement. The clients are connected to specific addresses and ports on the
		server with a hostname/port number pair that is the IP address and the TCP port
		number of the server. See The Unified CCX CTI Server in a High Availability Unified CCX System for how to select an IP address and port number.

Clients attempt to connect to the server until a connection is
		established. Once a connection between the client and the server has been
		established, the connection remains in place until a failure occurs or the
		client closes the connection. If a failure occurs, the client may again attempt
		to establish a connection to the server until a new connection is established.

Connection failures may be detected by the TCP layer (see Reasons for a Connection to Fail ) or
		by the heartbeat mechanism (see How a Session is Maintained ).