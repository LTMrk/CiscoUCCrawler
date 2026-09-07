---
doc_id: developer-cisco-com-docs-contact-center-express-the-unified-ccx-cti-server-in-a-high-availability-unified-ccx-system-313faff8ac
source_url: https://developer.cisco.com/docs/contact-center-express/the-unified-ccx-cti-server-in-a-high-availability-unified-ccx-system/
retrieved_at: 2026-09-07T14:04:58.513953+00:00
---

# The Unified CCX CTI Server in a High Availability Unified CCX System

High availability is a feature in CRS from release 4.0 onwards,
		except for the CRS 4.5 release.

A Unified CCX cluster consists of identically configured
		servers. Only one server is tagged as the master server. The master server
		makes decisions global to the cluster, like keeping track of calls, agent
		states, and maintaining socket connections to all CTI clients. At run-time only
		one of the servers can be the master server at a given time. The standby
		servers do not process any events on their own, with the possible exception of
		system events applicable to the local server.

Since a standby server does not manage any CTI clients, it does
		not receive any CTI events. If an attempt is made to connect to the slave
		server with an OPEN_REQ message, it responds with a FAILURE_CONF message with a
		status code of E_CTI_SERVER_NOT_MASTER.

If the master server fails, one of the standby servers becomes
		the new master server. Since the servers are configured identically, there is
		no need for a fail back unless the new master server does not have the same
		capacity as the original one. This would be the case if a different type of
		hardware is used to install the Unified CCX software in the cluster. Agents are
		re-connected to the new master server in case of failure of the master server.
		The TCP port number is specified in the System Parameters web page in the UCCX
		Administration. The field is RmCm TCP Port* .