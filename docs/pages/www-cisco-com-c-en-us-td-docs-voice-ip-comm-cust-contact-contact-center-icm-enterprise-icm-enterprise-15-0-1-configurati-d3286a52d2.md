---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-configurati-d3286a52d2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/configuration/guide/ucce_b_serviceability-guide-for-cisco-unified-icm-contact-center-enterprise-release-15-0/unified_icm_unified_cce_snmp_notifications.html
retrieved_at: 2026-08-20T18:59:51.740926+00:00
---

Serviceability Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

# Serviceability Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

Updated: April 30, 2025

Chapter: Unified CCE SNMP Notifications

## Chapter: Unified CCE SNMP Notifications

# Unified CCE SNMP Notifications

## SNMP
                           		  Notifications

The message ID also contains the severity in the two most significant
                                             							bits of the integer value. The message ID value shown is with these two
                                             							bits masked to zero.

Alarms with an asterisk (*) next to the Message ID are deemed to be
                                             							critical alarms.

The %n variable (where n is a
                                             							numeric value) indicates a substitution field whereby node-specific or
                                             							process-specific information is inserted.

## Administrative
                        	 Data Server SNMP Notifications

Message

Severity

Error

Type

Raise

Description

World Wide Web Publishing Service may be down. ICM is unable to communicate with web server.

Action

If the World Wide Web Publishing Service is not running, restart it or look for the messages in the IIS error log.

Message

Severity

Informational

Type

Clear

Description

World
                                       				  Wide Web Publishing Service is up.

Action

No action
                                       				  is required.

## Node Manager SNMP Notifications

Message

Severity

Warning

Type

Clear

Description

The node management library, common to all ICM processes, is initializing itself. This is a standard practice when a process
                                       (re)starts.

Action

No action is required.

Message

Severity

Informational

Type

Clear

Description

The Node Manager successfully started. The Node Manager shutdown because the operator requested a clean shutdown of the ICM
                                       node.

Action

No action is required.

Message

Severity

Informational

Type

Clear

Description

The Node Manager successfully started. The last reason the Node Manager stopped was because a clean shutdown of the node
                                       was requested by the operator.

Action

No action is required.

Message

Severity

Warning

Type

Raise

Description

The Node Manager on the ICM node has given the command to stop ICM services. This happens when an operator/administrator stop
                                       the ICM services using ICM Service Control, "nmstop", "net stop", Control Panel Services, or shutsdown the node.

Action

Contact the operator/administrator to determine the reason for the shutdown.

Message

Severity

Informational

Type

Clear

Description

The Node Manager process (which supervises the Node Manager) has started.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

A critical process required to run the ICM software on this node has terminated execution. The Node Manager is forced to
                                       reboot the node.

Action

Contact the technical assistance center.

Message

Severity

Warning

Type

Clear

Description

The Node Manager is restarting a process.

Action

No action is required.

Message

Severity

Informational

Type

Clear

Description

The Node Manager requested the shutdown since a critical process for the node failed. The Node Manager started.

Action

No action is required.

Message

Severity

Error

Type

Clear

Description

The Node Manager unable to determine the reason for the system restart.

Possible causes are power failure, a system failure (e.g. a Windows blue screen), a system not responding (in which an operator
                                       is forced to reboot), or a Node Manager exit.

The Node Manager started.

Action

Contact the technical assistance center.

Message

Severity

Warning

Type

Raise

Description

A process exited after running for '%1' seconds. Such processes must run for a minimum amount of time before the Node Manager
                                       will automatically restart them after they terminate.

The Node Manager will restart the process after delaying a number of seconds for other environmental changes to complete.

Action

No action is required.

Message

Severity

Warning

Type

Clear

Description

The Node Manager is restarting a process after the requisite delay.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

The Node Manager reports the termination of a process.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

A process exited (terminated itself) after it detected an internal software error.

Action

If the process continues to terminate itself, call the technical assistance center for help in diagnosing the problem.

Message

Severity

Warning

Type

Raise

Description

The specified process has detected a situation that requires it to ask the Node Manager to restart it. This often indicates
                                       a problem external to the process itself (for example, some other process may have failed).

Action

Node Manager on the ICM node will restart the process. The node should be checked to ensure that it is online. The process
                                       logs may be examined for root cause.

Message

Severity

Error

Type

Raise

Description

The specified process exited (terminated) with the indicated exit code. This termination is unexpected; the process died
                                       for an unknown reason. It will be automatically restarted.

Action

Determine if the process has returned to service or has stayed offline. If the process is offline or "bouncing", determine
                                       root cause from the process logs.

Message

Severity

Warning

Type

Raise

Description

Specified process is down after running for the indicated number of seconds. It will restart after delaying for the specified
                                       number of seconds for related operations to complete.

Action

Determine if the process has returned to service or has stayed offline. If the process is offline or "bouncing", determine
                                       root cause from the process logs.

Message

Severity

Warning

Type

Clear

Description

A process was successfully restarted.

Action

No action is required.

Message

Severity

Informational

Type

Clear

Description

The process was successfully started.

Action

No action is required.

Message

Severity

Warning

Type

Raise

Description

A process terminated itself successfully, and has requested the Node Manager to restart it.

Action

No action is required.

Message

Severity

Warning

Type

Raise

Description

A process exited as a result of a CTRL-C request or a request to close the process's active window.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

A process terminated itself successfully but, due to other conditions, has requested that the Node Manager to reboot the
                                       system.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

The Node Manager has itself exited after having run for "%1" seconds. The system will be rebooted after waiting a few seconds
                                       for related operations to complete.

Action

Contact the technical assistance center.

Message

Severity

Error

Type

Raise

Description

The Node Manager has itself exited after having run for "%1" seconds. The system cannot be rebooted since auto-reboot is
                                       disabled. The Node Manager Manager will attempt to restart the service.

Action

Contact the technical assistance center.

Message

Severity

Error

Type

Raise

Description

The Node Manager has requested the system to be rebooted after having run for "%1" seconds. The system will be rebooted after
                                       waiting a few seconds for related operations to complete.

Action

Contact the technical assistance center.

Message

Severity

Error

Type

Raise

Description

The Node Manager has requested the system to be rebooted after having run for "%1" seconds. The system cannot be rebooted
                                       since auto-reboot is disabled. The Node Manager Manager will attempt to restart the service.

Action

Contact the technical assistance center.

Message

Severity

Error

Type

Raise

Description

A critical process has requested a reboot after the service has been up for "%1" seconds. The system cannot be rebooted since
                                       auto-reboot on process request is disabled. The Node Manager Manager will attempt to restart the service.

Action

Contact the technical assistance center.

Message

Severity

Error

Type

Raise

Description

A critical process has requested the system to be rebooted after having run for "%1" seconds. The system will be rebooted
                                       after waiting "%2" seconds.

Action

Contact the technical assistance center.

## Message Delivery Service SNMP Notifications

Message

Severity

Informational

Type

Clear

Description

The indicated device is using this side of the central controller for its idle communication path (and is therefore using
                                       the other side of the central controller for its active communication path).

Action

No action is required.

Message

Severity

Informational

Type

Clear

Description

The indicated device is using this side of the central controller for its active communication path.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

The indicated device failed to realign its message stream to this side of the central controller.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

The indicated device has been disconnected from this side of the central controller. This may be caused by a network problem
                                       or device failure.

Action

Remedy network problems, if any. Call the Cisco Systems, Inc. technical assistance center in the event of a software failure
                                       on the device.

Message

Severity

Warning

Type

Raise

Description

The communication path between this side of the central controller and the indicated device has been reset to an initial
                                       state.

Action

No action is required.

Message

Severity

Informational

Type

Clear

Description

The indicated device is initializing its message stream with this side of the central controller.

Action

No action is required.

Message

Severity

Warning

Type

Raise

Description

No communication path from the indicated device to this side of the central controller has existed for the indicated time
                                       period. This indicates either an extended network outage or an extended outage at the device.

Action

One or more network links between the named device and the named side of the ICM router has failed. If alarms exist for BOTH
                                       routers, the site is offline. If alarms exist for one side of the router, then the site should be up but network redundancy
                                       is degraded. Communication (network) between the central controller (router) and the PG should be checked using "ping" and
                                       "tracert". Must have visible and visible high priority connection from PG to router. CCAG process on router and PGAG process
                                       on PG should be checked.

Message

Severity

Warning

Type

Raise

Description

The MDS message synchronizer was unable to connect to its duplexed partner within the timeout period. Either the duplexed
                                       partner is down, or there is no connectivity to the duplexed partner on the private network.

Action

Verify reliable network connectivity on the private network. Call the Cisco Systems, Inc. technical assistance center in
                                       the event of a software failure on the duplexed partner.

Message

Severity

Error

Type

Raise

Description

The MDS message synchronizer has lost connectivity to its duplexed partner. This indicates either a failure of the private
                                       network, or a failure of the duplexed partner.

Action

Confirm services are running on peer machine. Check MDS process to determine if it is paired or isolated. Ping test between
                                       peers over the private network. Check PGAG and MDS for TOS (Test Other Side) messages indicating the private network has failed
                                       and MDS is testing the health of the peer over the public network.

Message

Severity

Informational

Type

Clear

Description

The MDS message synchronizer has established communication with its duplexed partner.

Action

No action is required.

Message

Severity

Warning

Type

Single-State Raise

Description

MDS time delivery queue size is increasing over time.

Action

Ensure that the ICM/IPCC configuration (# agents, # skills/agent, # PGs) is within the supported limit.

## Router SNMP
                        	 Notifications

Message

Severity

Error

Type

Raise

Description

An application gateway connection has failed. This means that
                                       				  the application gateway process has attempted to connect to the host the number
                                       				  of times indicated in the Session Retry Limit field and has failed. It will not
                                       				  try to reconnect again until the connection is taken out of service and brought
                                       				  back into service.

Action

Determine why the Application Gateway cannot connect to the
                                       				  host. Verify the connection between the two VMs. After fixing the issue, take
                                       				  the Application Gateway out of service and then bring it back in service.

Message

Severity

Informational

Type

Clear

Description

The application gateway is now connected to the host process.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

An external application used in some scripts has disconnected
                                       				  from the specified Application Gateway. Error recovery mechanisms will attempt
                                       				  to reconnect. Routing may be impacted.

Action

Verify the connection properties in the Application Gateway
                                       				  configuration. If the host application was off-line for a long time, restart
                                       				  the Application Gateway to reconnect.

Message

Severity

Informational

Type

Clear

Description

The Contact Share node connection to Live Data is up.

Message

Severity

Error

Type

Raise

Description

The Contact Share node connection to Live Data is down.

Message

Severity

Error

Type

Raise

Description

The Contact Share node has determined that none of the
                                       				  configured AW hosts are active or have current data.

Message

Severity

Informational

Type

Clear

Description

The Contact Share node is able to connect to the AW and is able
                                       				  to retrieve data.

Message

Severity

Informational

Type

Clear

Description

The specified peripheral is on-line to the ICM. Call and agent
                                       				  state information is being received by the Router for this site.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

The specified ACD/IVR is not visible to the Peripheral Gateway.
                                       				  No call or agent state information is being received by the Router from this
                                       				  site. Routing to this site is impacted.

Action

If Peripheral Gateway is also offline per messaging (message ID
                                       				  10500D1) or "rttest" result, then first proceed with troubleshooting for
                                       				  Peripheral Gateway off-line alarm. Otherwise ACD/IVR Vendor should be contacted
                                       				  for resolution.

Message

Severity

Informational

Type

Clear

Description

The Router is reporting that physical controller "%2" is
                                       				  on-line.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

The specified Peripheral Gateway is not connected to the
                                       				  central controller. It could be down. Possibly it has been taken out of
                                       				  service. Routing to this site is impacted.

Action

Communication (network) between the central controller (Router)
                                       				  and the PG should be checked using "ping" and "tracert". You must have a
                                       				  visible high priority connection from the PG to the Router. The CCAgent process
                                       				  on the Router and the PGAgent process on the PG should be checked. The PG may
                                       				  have been taken out of service for maintenance.

Message

Severity

Informational

Type

Clear

Description

PG has reported that peripheral "%2" (ID "%1") is operational.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

This may indicate that the peripheral is off-line for
                                       				  maintenance or that the physical interface between the peripheral and the PG is
                                       				  not functioning.

Action

Check that the peripheral is not off-line and that the
                                       				  connection from the peripheral to the PG is intact.

10500E9

Message

UpdateCC from: %1 on: %2, rejected because no Loggers are in operation.

Severity

Error

Type

Single-State Raise

Description

The attempt to update the central controller configuration was rejected because none of the Loggers are operational.

This SNMP Notification is supported with UCCE 12.6(2) if CCE 12.6(2)_ES 36 is installed.

Action

Retry the update operation after at least one of the Loggers is operational.

Message

Severity

Informational

Type

Raise

Description

Script table "%2" is only available on the side A Router. If
                                       				  the side A Router goes down, no DBLookup requests can be processed as side B
                                       				  cannot access the script table.

Action

Configure a script table on side B that is identical to that on
                                       				  side A.

Message

Severity

Informational

Type

Raise

Description

Script table "%2" is only available on the side B Router. If
                                       				  the side B Router goes down, no DBLookup requests can be processed as side A
                                       				  cannot access the script table.

Action

Configure a script table on side B that is identical to that on
                                       				  side A.

Message

Severity

Error

Type

Raise

Description

No DBLookup requests can be processed as script table "%2" is
                                       				  unavailable on either side of the central controller.

Action

Configure a script table on either side A or side B, or both.

Message

Severity

Informational

Type

Clear

Description

Script table "%2" is configured on both sides of the central
                                       				  controller.

Action

No action is required.

Message

Severity

Informational

Type

Clear

Description

The Router is reporting that side "%1" process "%2" is OK.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

This alarm only occurs for central controller (Router and
                                       				  Logger) processes. If the process for BOTH sides is down there is a total
                                       				  failure for that process. This could be part of Router shutdown. Critical
                                       				  processes: - "mds" (Router/Logger): coordinates messaging between duplexed
                                       				  Routers AND Loggers. When mds is down the central controller is down and no
                                       				  calls are being routed. - "rtr" (Router): call routing intelligence. -
                                       				  "clgr/hlgr" (Logger) - configuration/historical data processing to
                                       				  configuration database. - "rts" (Router): Real Time Server data feed from the
                                       				  Router to the Admin Workstations for reporting. - "rcv" (Logger Recovery):
                                       				  keeps the redundant historical databases synchronized between duplexed Loggers.

Action

No action is required.

Message

Severity

Informational

Type

Clear

Description

The specified node is on-line to the ICM.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

The specified node is not visible to the ICM. Distribution of
                                       				  real time data may be impacted.

Action

No action is required.

Message

Severity

Informational

Type

Clear

Description

The Router's state size of "%1" MB is now below the alarm limit
                                       				  of "%2" MB.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

The Router's state size of "%1" MB has grown beyond the alarm
                                       				  limit of "%2" MB. This may indicate a memory leak, or it may indicate that the
                                       				  customer's configuration size has grown larger. Large state sizes may cause
                                       				  problems when synchronizing Routers, so the bandwidth of the private link may
                                       				  also need to be investigated.

Action

The alarm limit can be raised with the "rtsetting" tool.

Message

Severity

Informational

Type

Clear

Description

The specified node is on-line to the ICM.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

The specified node is not visible to the ICM. Distribution of real time data may be impacted. This condition can exist briefly
                                       while the system is loading. If it does not clear, it may indicate a problem with the node or the communications paths that
                                       connect the Router and node.

Action

Check the communication paths that connect the Router and the
                                       				  node.

Message

Severity

Informational

Type

Clear

Description

The specified node is on-line to the ICM.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

This condition indicates that the Router has not yet completed the initialization step of loading a configuration from the
                                       Logger. This condition can exist briefly while the system is loading. If it does not clear, it may indicate a problem with
                                       the Logger or the communications paths that connect the Router and the Logger.

Action

Check the communication paths that connect the Router and the
                                       				  Logger.

Message

Severity

Error

Type

Single-State Raise

Description

The Router has detected that it is no longer synchronized with
                                       				  its partner. One result of this is that the Router might be routing some calls
                                       				  incorrectly.

Action

Stop the Router on both sides. After both sides are completely stopped, restart both Routers. Alternate Action: Restart the
                                       Router on one side. After doing this, the Routers might still route some calls incorrectly, but they will be in sync.

Message

Severity

Error

Type

Raise

Description

There is a change in the congestion level of the Router which
                                       				  implies that there is a change in the call rejection percentage also. When
                                       				  congestion control is enabled, the system will reject or treat the calls
                                       				  according to the congestion level and rejection percentage determined. When
                                       				  congestion control is disabled, the system will not reject or treat the calls
                                       				  until the congestion enabled option is turned on in the congestion control
                                       				  settings gadget.

Action

The system has exceeded the designed capacity. Re-evaluate the
                                       				  system design if the congestion occurs frequently. When congestion control is
                                       				  disabled and the system is congested, you can turn on the congestion enabled
                                       				  option in the congestion control settings gadget to reject or treat the
                                       				  congested calls.

Message

Severity

Warning

Type

Clear

Description

The Router is currently not congested.

Action

None

Message

Severity

Error

Type

Single-State Raise

Description

Total number of agent skill group pairs exceeds the defined
                                       				  system default limit.

Action

Log out agents or remove skill groups associated to the agent
                                       				  such that the agent skill group pair count does not exceed the defined system
                                       				  default limit.

Message

Severity

Error

Type

Raise

Description

The Contact Share connection to the application gateway is
                                       				  down.

Message

Severity

Informational

Type

Clear

Description

The Contact Share connection to the application gateway is up.

Message

Severity

Informational

Type

Clear

Description

The Contact Share connection to the application gateway is
                                       				  active.

Message

Severity

Informational

Type

Raise

Description

The Contact Share connection to the application gateway is
                                       				  inactive.

Message

Severity

Warning

Type

Raise

Description

The number of logged-in agents has reached the maximum capacity
                                       				  supported by this deployment type.

Action

No action is required.

Message

Severity

Informational

Type

Clear

Description

The number of logged-in agents is now below the maximum
                                       				  capacity supported by this deployment type.

Action

No action is required.

## Logger SNMP Notifications

Message

Severity

Error

Type

Raise

Description

Indicates that the MDS event feed connection from the ICM router to the CSFS process on the logger has failed.

Action

No action is required.

Message

Severity

Informational

Type

Clear

Description

Indicates MDS event feed connection from ICM router to CSFS process has connected.

Action

If not a planned startup of the system, determine if the event is due to process, network, or system failure.

Message

Severity

Informational

Type

N/A

Description

Periodic message sent to indicate that the ICM Message Delivery Service (MDS) is in service and the system on which event
                                       management system processes reside can send events to the configured listener system. This message is also passed to the SNMP
                                       agent to indicate that the event stream is active.

Action

No action is required.

Message

Severity

Informational

Type

Clear

Description

A system (via a particular process), connected to the SDDSN server has successfully registered as a valid endpoint using
                                       a unique ID. The system can now start sending diagnostic event data using the SDDSN server.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

A system (via a particular process), connected to the SDDSN server has failed to unregistered as a valid endpoint using a
                                       unique ID. This indicates that the system abruptly disconnected from the SDDSN server.

Action

This could indicate that the SDDSN server has failed or the TCP/IP connection to the server was lost. If this is a fault
                                       tolerant SDDSN server, check to see if the secondary SDDSN server has successfully re-registered the system). This would be
                                       indicated by a CLEAR condition to this alarm while the side of SDDSN that is reporting would be the other SDDSN server. If
                                       the primary SDDSN server is still running, check to see if you can ping between the system and the primary SDDSN server. Other
                                       scenarios include a simplex SDDSN server failure or lost TCP/IP connection, or the system that was communicating with the
                                       SDDSN server has somehow failed.

Message

Severity

Informational

Type

Clear

Description

A system (via a particular process), connected to the SDDSN server has successfully unregistered as a valid endpoint using
                                       a unique ID. This indicates that the system gracefully disconnected from the SDDSN server.

Action

No action is required.

Message

Severity

Error

Type

Single-State Raise

Description

An event has been received that the SDDSN server cannot decipher using the resource files (message DLLs) because they are
                                       missing or out of date. The SDDSN server has forwarded the ciphered event, and then disconnected the system that generated
                                       that event. %1 is the product number (in decimal). %2 is the Message ID that was sent. A value of 0 indicates that none of
                                       the messages can be deciphered. %3 is the name of the product.

Action

The SDDSN server needs to have an updated installation of the resource files that are shipped with the product (%3). If %3
                                       indicates 'Unknown', contact the technical assistance center to get a correlation between %1 and the actual product name.
                                       Install the updated support files for that product on the SDDSN server and restart it. This update will contain files named
                                       MSGSn.DLL and CATn.DLL where the 'n' should be replaced with the number %1 from this error message (e.g. MSGS2.DLL, CAT2.DLL,
                                       etc.).

Message

Severity

Error

Type

Single-State Raise

Description

An event has been received by a client system using an incompatible version of the SDDSN protocol.

Action

The client system needs to be configured to send the correct version of the SDDSN protocol, or the SDDSN server needs to
                                       be upgraded to support the desired version.

Message

Severity

Informational

Type

Single-State Raise

Description

%1%% of the available free space is used in %2 database. This is an indication of how full the database is. When this value
                                       gets too high, the Logger will begin deleting the oldest historical records from the database.

Action

Change the purge interval to save data for a shorter period of time. If this is not practical, add more disk space to the
                                       system and add disk devices to the database by using SQL Server Management Studio.

Message

Severity

Informational

Type

Single-State Raise

Description

%1%% of the available log space is used in the %2 database.

Action

No action is required.

Message

Severity

Warning

Type

Raise

Description

The automatic purge is being run in order to keep the database from running out of space. The parameters for the daily purge
                                       need to be adjusted to match the database storage capacity.

Action

Contact the technical assistance center.

Message

Severity

Warning

Type

Clear

Description

The automatic purge has been run in order to keep the database from running out of space. The parameters for the daily purge
                                       need to be adjusted to match the database storage capacity.

Action

No action is required.

Message

Severity

Informational

Type

Clear

Description

The Logger successfully connected to a client system.

Action

No action is required.

Message

Severity

Informational

Type

Raise

Description

Logger or HDS on the specified TCP/IP connection and port number either went out of service or communication has been broken.

Action

The Historical Data Server (HDS) or the peer Logger (on the other side of the duplexed central controller) is no longer getting
                                       its historical feed from this Logger. This can occur due to networking outages, SQL issues on the Logger or HDS, or the Logger
                                       or the HDS may have been shut down or otherwise disabled.

Message

Severity

Warning

Type

Single-State Raise

Description

CICR replication must find a routing client in the database with a matching network routing client. Otherwise, it cannot
                                       translate the routing client ID foreign key in the dialed number or label properly. CICR replication is unable to complete
                                       the replication in this case.

Action

No action is required.

Message

Severity

Warning

Type

Single-State Raise

Description

CICR replication must find a customer and instance in the database with matching names. Otherwise, it cannot translate the
                                       customer definition ID foreign key in the dialed number or label properly. CICR replication is unable to complete the replication
                                       in this case.

Action

No action is required.

Message

Severity

Warning

Type

Single-State Raise

Description

CICR replication has found that inserting the dialed number or label would cause a duplicate key error. Therefore, the dialed
                                       number or label cannot be inserted. CICR replication is unable to complete the replication in this case.

Action

No action is required.

Message

Severity

Warning

Type

Single-State Raise

Description

CICR replication has found that a dialed number already exists with this enterprise name. Therefore, it cannot insert the
                                       new dialed number. CICR replication is unable to complete the replication in this case.

Action

No action is required.

Message

Severity

Warning

Type

Single-State Raise

Description

CICR replication has found that a dialed number already exists with this routing client ID and dialed number string. Therefore,
                                       it cannot insert the new dialed number. CICR replication is unable to complete the replication in this case.

Action

No action is required.

Message

Severity

Warning

Type

Single-State Raise

Description

CICR replication has found that a label already exists with this routing client ID and label string. Therefore, it cannot
                                       insert the new label. CICR replication is unable to complete the replication in this case.

Action

No action is required.

Message

Severity

Informational

Type

Clear

Description

The CICR replication process is active.

Action

No action is required.

Message

Severity

Informational

Type

Raise

Description

The CICR replication process is inactive.

Action

No action is required.

Message

Severity

Error

Type

Single-State Raise

Description

Invalid host name has been configured for the customer.

Action

Use the ConfigICR-@gt;ICR_NODE to change the host name or system name and re-start the CICR replication process.

Message

Severity

Warning

Type

Single-State Raise

Description

CICR replication failed to update the configuration change due to the error caused by the "commit update CC transaction"
                                       failure.

Action

No action is required.

Message

Severity

Warning

Type

Single-State Raise

Description

Found historical records with date/time greater than current central controller time. Delete the records which have date
                                       time greater than the current central controller time.

Action

No action is required.

Message

Severity

Informational

Type

Raise

Description

The NICR replication process is inactive.

Action

No action is required.

Message

Severity

Informational

Type

Clear

Description

The NICR replication process is active.

Action

No action is required.

Message

Severity

Error

Type

Single-State Raise

Description

Invalid primary distributor has been configured for the customer, or the system is unable to resolve the hostname for the
                                       named primary distributor for some reason.

Action

Use the ConfigICR-@gt;ICR_NODE to change the host name or system name and re-start the CICR replication process. Alternatively,
                                       check name resolution for the specified host name.

## Peripheral Gateway SNMP Notifications

Message

Severity

Informational

Type

Clear

Description

The Enterprise CTI server associated with this Peripheral Gateway is on-line. Enterprise CTI Client applications are able
                                       to connect to the server and exchange call and agent data.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

The Enterprise CTI server associated with this Peripheral Gateway is off-line. Enterprise CTI client applications are not
                                       able to connect to the server and exchange call and agent data.

Action

Review the CTI server events and logs.

Message

Severity

Error

Type

Single-State Raise

Description

OPC has detected that it is no longer synchronized with its partner.

Action

No action is required.

Message

Severity

Error

Type

Single-State Raise

Description

PG has failed activation and will be restarted.

This SNMP Notification is supported with UCCE 12.6(2) if CCE 12.5(2) ES 23 is installed.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

Message Integration Service (MIS) was unable to connect to the indicated component and address.

Action

Confirm component is available, configuration of IP address(es) and port(s) are correct, and network connectivity would allow
                                       for connection.

Message

Severity

Informational

Type

Clear

Description

Message Integration Service (MIS) was able to connect to the indicated component and address.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

Message Integration Service (MIS) was unable to open a session to the indicated component.

Action

No action is required.

Message

Severity

Informational

Type

Clear

Description

Message Integration Service (MIS) was able to open a session to the indicated component and address.

Action

No action is required.

Message

Severity

Error

Type

Single-State Raise

Description

A message pertaining to the indicated trunk group and trunk has not been configured with MIS.

Action

Configure extension, trunk group, and trunk in MIS.

Message

Severity

Error

Type

Single-State Raise

Description

A call within MIS could not be tracked successfully.

Action

Determine where tracking problem occurred and correct (for MIS problem, it could be MIS, VRU, or PG).

Message

Severity

Error

Type

Raise

Description

An error occurred on the connection between the ACMI ACD server (CTI) and the ACMI peripheral gateway. ACMI peripheral gateway
                                       is offline.

Action

If ACMI peripheral gateway does not re-attach, contact the technical assistance center.

Message

Severity

Informational

Type

Clear

Description

Peripheral status was DOWN, going NORMAL. ACMI peripheral gateway is online.

Action

No action is required.

Message

Severity

Informational

Type

Clear

Description

The DN is operational.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

The Permit Application Routing box on the child system is not checked for DN.

Action

Check Permit Application Routing box.

Message

Severity

Error

Type

Raise

Description

You have configured a DN or DN for a translation route on the parent that doesn't exist on the child system. Don't forget
                                       to check 'Permit Application Routing' when adding it.

Action

Add the DN on the child system and ensure that 'Permit Application Routing' is enabled.

Message

Severity

Error

Type

Raise

Description

You have configured a DN or DN for a translation route on the parent that doesn't exist on the child system. Don't forget
                                       to check 'Permit Application Routing' when adding it.

Action

Add the DN on the child system and ensure that 'Permit Application Routing' is enabled.

Message

Severity

Error

Type

Single-State Raise

Description

You have specified an incorrect server peripheral ID in the PG Setup of the Gateway PG.

Action

Correct the server peripheral ID in the PG Setup of the Gateway PG and restart the PG.

Message

Severity

Error

Type

Single-State Raise

Description

Another Gateway PG has requested control of this DN. This is most like likely due to an incorrect server hostname being configured.

Action

Correct the server host name in the PG Setup of the Gateway PG and restart the PG.

Message

Severity

Error

Type

Single-State Raise

Description

You have specified an incorrect server peripheral ID in the PG Setup of the Gateway PG.

Action

Correct the server peripheral ID in the PG Setup of the Gateway PG and restart the PG.

Message

Severity

Error

Type

Raise

Description

Central controller connection on child down - ACMI peripheral gateway status DOWN.

Action

No action is required.

## CTI SNMP Notifications

Message

Severity

Informational

Type

Clear

Description

An Enterprise CTI session has been opened by client ID %1 (signature %2) from IP address %3.

Action

No action is required.

Message

Severity

Warning

Type

Raise

Description

The Enterprise CTI session with client ID %1 (signature %2) at IP address %3 has been closed by the client.

Action

This indicates that an Enterprise CTI client application that is generally always connected to the Enterprise CTI Server
                                       has closed its connection. The CTI client application software may need to be checked for proper operation.

Message

Severity

Error

Type

Raise

Description

The Enterprise CTI session with client ID %1 (signature %2) at IP address %3 has been terminated by the Enterprise CTI Server.

Action

This indicates that an Enterprise CTI Client application that is generally always connected to the Enterprise CTI Server
                                       has been disconnected due to errors. If the problem persists, the CTI client application software may need to be checked for
                                       proper operation.

Message

Severity

Informational

Type

Clear

Description

The Enterprise CTI client %1 application software has reported the following normal event for object %2: %3.

Action

No action is required.

Message

Severity

Warning

Type

Raise

Description

The Enterprise CTI client %1 application software has reported the following warning for object %2: %3.

Action

This indicates that the CTI client application software has detected a possible error or other abnormal condition and may
                                       need to be checked for proper operation.

Message

Severity

Error

Type

Raise

Description

The Enterprise CTI client %1 application software has reported the following error for object %2: %3.

Action

This indicates that the CTI client application software has detected an error condition and may need to be checked for proper
                                       operation.

Message

Severity

Warning

Type

Raise

Description

A CTI client: %1 (signature: %2) from IP address: %3 with a version prior to 14 has connected to CTI Server that supports
                                       multi-line phones. Problems may be encountered with that application depending upon what messages/devices, etc. it processes
                                       events for.

Action

Check with the vendor of the software and see if they have ensured compatibility.

Message

Severity

Warning

Type

Clear

Description

A CTI client %1 (signature %2) from IP address %3 with a version prior to 14 has connected to CTI Server that supports multi-line
                                       phones. Problems may be encountered with that application depending upon what messages/devices, etc. it processes events for.

Action

Check with the vendor of the software and see if they have ensured compatibility.

Message

Severity

Warning

Type

Single-State Raise

Description

CTI Server found too much data in ECC variables while processing messages. ECC Variables will not be forwarded for there
                                       messages.

Action

This indicates that too many / too large ECC variables are configured in the system. Eliminate some ECC variables or reduce
                                       the size of existing ECC variables to alleviate this condition.

Message

Severity

Informational

Type

Clear

Description

Message indicating the version of CTI OS Server as well as the protocol version CTI OS Server uses to connect to CTI Server.

Message

Severity

Warning

Type

Raise

Description

CTI OS Server has cycled itself because its connection to CTI Server closed. When CTI OS Server restarts, it will re-establish
                                       its connection to CTI Server.

Message

Severity

Error

Type

Raise

Description

CTI OS Server has cycled itself because its connection to CTI Server failed. When CTI OS Server restarts, it will re-establish
                                       its connection to CTI Server.

Message

Severity

Informational

Type

Clear

Description

The CTI OS Server incoming message is now below 10,000 messages.

Message

Severity

Warning

Type

Raise

Description

The CTI OS Server incoming message queue exceeded 10,000 messages. This might result in unwanted behavior.

Message

Severity

Error

Type

Single-State Raise

Description

CTI OS Server generated an exception while processing a request or an event specified in this method.

Message

Severity

Error

Type

Single-State Raise

Description

CTI OS Server generated an exception while processing the request or event specified in this method.

Message

Severity

Informational

Type

Clear

Description

CTI OS Server is current running with an acceptable number of agents connected to it.

Message

Severity

Warning

Type

Raise

Description

CTI OS Server is currently running with an excessive number of agents connected to it.

Message

Severity

Informational

Type

Clear

Description

CTI OS Server is current running with an acceptable number of monitor-mode applications connected to it.

Message

Severity

Warning

Type

Raise

Description

CTI OS Server is currently running with an excessive number of monitor-mode applications connected to it.

Message

Severity

Informational

Type

Clear

Description

CTI OS Server has re-enabled monitor mode functionality.

Message

Severity

Warning

Type

Raise

Description

CTI OS Server has disabled access to monitor mode functionality because an excessive number of consecutive failed attempts
                                       to access monitor mode functionality have occurred. An attempt to access monitor mode functionality fails when the CTI OS
                                       monitor mode password is incorrectly specified.

Message

Severity

Warning

Type

Raise

Description

Upon re-establishment of the CTI Server Link, CTI OS Server detected a configuration change. CTI OS Server will restart to
                                       insure proper configuration.

Message

Severity

Warning

Type

Raise

Description

CTI OS Server's connection to the CTI Server has closed. CTI OS Server will attempt to re-establish the connection to the
                                       CTI Server. If Unsuccessful, CTI OS Server will restart.

Message

Severity

Informational

Type

Clear

Description

CTI OS Server is within the supported operational limit for this configuration/action.

Message

Severity

Warning

Type

Raise

Description

The CTI OS Server is within the supported operational limit has been exceeded

## Live Data Events

Message

Severity

Informational

Type

Raise

Description

Informs JMS publisher connection to ActiveMQ service is down.  JMS publisher terminated/stopped.

Action

Ordinarily, no action required.

However, if connection to JMS (ActiverMQ service) is down for extended periods of time, then, verify if ActiveMQ service status
                                       and evaluate overall system health, i.e., verify services are up, disk partitions have free space, system is not CPU starved,
                                       not swapping, not I/O bound, etc.

Message

Severity

Informational

Type

Clear

Description

Informs JMS publisher connection to ActiveMQ service is up. JMS publisher started, or, if connection lost, connection established.

Action

No action required.

Note, however, that if JMS connection is bouncing often, then, this could be an indication of a system-wide issue, so evaluate
                                       overall system health, i.e., verify services are up, disk partitions have free space, system is not CPU starved, not swapping,
                                       not I/O bound, etc.

Message

Severity

Error

Type

Raise

Description

Failure during creation of JMX bean for TIP statistical reporting, which can be linked to JMX services failure to initialize,
                                       lack of system resources, or incorrect configuration of JMX host/port.

Action

Verify overall system health, i.e., services are up, disk partitions have free space, system is not CPU starved, not swapping,
                                       not I/O bound, etc. Attempt system restart, if problem persists, contact tech. support.

Message

Severity

Error

Type

Raise

Description

Failure during establishment of JMX bean for event spout (PG, Router, etc) operations. This means no operations to/from spouts
                                       will be possible via JMX.

Action

Attempt system restart, if problem persists, contact tech. support.

Message

Severity

Error

Type

Clear

Description

Success in establishing JMX bean for event spout (PG, Router, etc) operations.

Action

No action required.

Message

Severity

Warning

Type

Raise

Description

Destination host/port not accepting connections.

Too many messages (from server) pending processing by Live Data.

Write to closed (by far-end) connection.

Action

Verify CCE server host/port configuration is correct, and port is open on host fire-wall.

Verify CPU availability to Live Data. If problem persists contact tech. support.

No action required for attempt to write to closed (by far-end) connection.

Message

Severity

Warning

Type

Clear

Description

Missed one heartbeat to CCE server is not uncommon, and it is typically linked to a busy system. Live Data uses heartbeat
                                       to track the health of a CCE connection, and if too many (configurable) heartbeats are lost it will close and (attempt) to
                                       re-open the connection.

Action

No action required.

Message

Severity

Critical

Type

Raise

Description

Failover to standby cluster node.

JMX reset connection request.

System shutdown.

Action

On failover: determine failover root cause and correct it. Start with overall system health, i.e., services are up, disk partitions
                                       have free space, system is not CPU starved, not swapping, not I/O bound, etc. If no reason is found, or reason cannot be corrected,
                                       contact tech. support. For all the other reasons: no action required.

Message

Severity

Critical

Type

Clear

Description

Indicates spout communication controller, responsible for CCE message processing, has started.

Action

No action required.

Message

Severity

Error

Type

Raise

Description

Request/response timeout

Unrecognized message format

Failure in message decoding

Failure in message processing

Action

Protocol request/response timeouts are not uncommon and are typically linked to communication failure due to far-end port
                                       disconnect (i.e., attempt to write to a closed socket). For all other failures, contact tech. support.

Message

Severity

Error

Type

Raise

Description

Configuration to CCE server is incomplete, or invalid. Port is not numeric in range 1-65565, host name contains invalid characters,
                                       etc.

Action

Verify Live Data configuration and restart system.

Message

Severity

Error

Type

Raise

Description

Indicates data loss during last CCE connection switch-over. PG/Router unavailable simultaneous to a communication loss to
                                       PG/Router corresponding side (A or B).

Action

No action required.

The system will issue a new sequence group, and request a snapshot to re-synch its internal state with that of the failed
                                       component.

Message

Severity

Error

Type

Raise

Description

Indicates data loss during last CCE communication. PG/Router crash simultaneous to a communication loss to PG/Router corresponding
                                       side (A or B).

Action

No action required.

The system will request a snapshot to re-synch its internal state with that of the failed component.

Message

Severity

Warning

Type

Raise

Description

Indicates spout communication controller has detected an active connection (to CCE server) is down, and that the standby connection
                                       to configured PG/Router will become active (switch-over). The PG/Router communication was severed, or the CCE server is no
                                       longer running.

Action

Verify CCE server (PG, Router, etc) health.

Message

Severity

Error

Type

Clear

Description

Indicates that during a switch-over (from active connection to standby) the sequence number received by standby is in ascending
                                       order, and that it can be released from CCE server side. PG/Router unavailable, but Live Data state is not affected by it.

Action

No action required.

Message

Severity

Warning

Type

Raise

Description

Request to CCE server has failed, or timed out.

Action

No action required.

Message

Severity

Error

Type

Raise

Description

Protocol error during response processing (of a request to CCE server) due to response to an invalid, or inexistent, pending
                                       request id. This can be linked to an expired request, as well as, an inexistent request.

Action

No action required.

Message

Severity

Error

Type

Raise

Description

Reached allowed number of heartbeat losses to CCE server. This will disconnect all CCE servers (PG, Router, etc) associated
                                       with a given CCE side (A or B). A switch over to other CCE server side (A or B) will be automatically initiated.

Action

Determine network integrity between Live Data and CCE servers on failed side (A or B). Determine if CCE server (PG, Router,
                                       etc) is up and running.

Message

Severity

Error

Type

Raise

Description

Indicates TOS (related to Live Data Cluster node state) protocol error.

Failure to start TOS communication

Failure during write to TOS far-end server

Action

Verify Live Data configuration, restart system.

Message

Severity

Warning

Type

Raise

Description

Unable to send message to assess Live Data Cluster state on far end. Triggered by failure to receive cluster node state via
                                       JMS (ActiveMQ/Netbridge in this case), which can be caused by cluster node crash, network failure, ActiveMQ crash, or Netbridge
                                       crash.

Action

Verify network integrity between Live Data cluster nodes. Verify ActiveMQ service is up, and cluster nodes configured for
                                       fail-over.

Message

Severity

Warning

Type

Raise

Description

Request/response round trip time to cluster nodes is greater than configured seconds. This can be linked to network latency,
                                       or sluggish response from cluster node far end.

Action

Verify network integrity between Live Data clusters nodes. Verify overall system health on all Live Data cluster nodes.

Message

Severity

Warning

Type

Raise

Description

Missed one heartbeat to CCE server is not uncommon, and it is typically linked to a busy system. Live Data uses heartbeat
                                       to track the health of a CCE connection, and if too many (configurable) heartbeats are lost it will close and (attempt) to
                                       re-open the connection.

Action

Verify network integrity between CCE server and Live Data.

Message

Severity

Error

Type

Raise

Description

Reached allowed number of heartbeat losses to CCE server (PG, Router, etc). This will cause a disconnection followed by reconnection
                                       to CCE servers (PG, Router, etc).

Action

Verify network integrity from CCE server (PG, Router, etc) to Live Data. Verify CCE server (PG, Router, etc) is up and running.

Message

Severity

Error

Type

Raise

Description

Failed to open connection to JMS (ActiveMQ) or to publish to indicated topic.   Configuration to JMS (ActiveMQ) is incorrect,
                                       or service is down.

Action

Verify Live Data configuration. Assess overall system health, i.e., services are up, disk partitions have free space, system
                                       is not CPU starved, not swapping, not I/O bound, etc.

Note that, in case of ActiveMQ service down, the Live Data cluster will fail-over to standby node.

Message

Severity

Error

Type

Raise

Description

Error during load of Live Data configuration from AWDB. Dataset name pointing to AWDB, incorrectly configured in CUIC. location.

Action

Using CUIC interface assure data set name for CUIC is correctly configured with address to AWDB. Ensure AWDB system is up
                                       and running. If problem persists, contact tech. support.

Message

Severity

Informational

Type

Clear

Description

Live Data configuration, from AWDB, loaded to local memory.

Action

No action required.

Message

Severity

Error

Type

Raise

Description

JMS command spout failed to initialize. Scenario JMS (ActiveMQ) communication was not possible via Camel, and an exception
                                       was thrown.

Action

Verify Live Data configuration, and restart system. If problem persists, contact tech. support.

Message

Severity

Error

Type

Raise

Description

JMS command spout failed to close JMS connection.

Action

No action required.

Message

Severity

Error

Type

Raise

Description

During communication with CCE server, message sequence number was not in increasing order, and/or presented a gap. Possible
                                       data loss.

Action

Gather logs and contact tech. support.

Message

Severity

Error

Type

Raise

Description

Zookeeper connection object could not instantiate or connect.

Establishment of JMS command queue listener failed.

JMX configuration could not be written to Zookeeper.

Action

Verify Zookeeper service is up and running, and restart system. If problem persists, contact tech. support.

Message

Severity

Error

Type

Raise

Description

Connection to Zookeeper was severed, which might be linked to a Zookeeper down/terminated. Note that a Zookeeper disconnection
                                       will cause a Live Data cluster failover.

Action

Zookeeper is central to Storm and, as such, to Live Data; verify service is up and running. If disconnections are frequent,
                                       contact tech. support.

Message

Severity

Informational

Type

Clear

Description

Connection to Zookeeper established.

Action

No action required.

Message

Severity

Critical

Type

Raise

Description

Event spout is deactivated due to a Live Data Cluster failover. One of the central components to Live Data is down. Central
                                       components are: Zookeeper, ActiveMQ, and (pairs of) CCE servers (PG/Router).

Action

Verify overall system health, i.e., services are up, disk partitions have free space, system is not CPU starved, not swapping,
                                       not I/O bound, etc. Verify network to PGs and Routers are healthy. Verify PGs and Routers are up and running. If problem persists,
                                       contact tech. support.

Message

Severity

Critical

Type

Clear

Description

Event spout transitioned to active state due to startup, or Live Data Cluster failover.

Action

No action required.

Message

Severity

Informational

Type

Clear

Description

Deployment type change from UCCE to PCCE, or vice-versa. This WILL impact the feature set available in Live Data, and require
                                       environment reconfiguration. The expectation is, in fact, that environment adjustments (to/from UCCE to PCCE), took place
                                       before changing deployment type.

Action

No action required.

Message

Severity

Error

Type

Raise

Description

Indicates Live Data EndPoint configuration is present, but data is inconsistent (values missing from tables, incomplete data,
                                       etc.).

Action

Correct Live Data EndPoint Configuration.

Message

Severity

Error

Type

Raise

Description

Live Data configuration is incomplete/incorrect and TOS protocol host/port is in error.

Action

Correct Live Data EndPoint Configuration.

Message

Severity

Error

Type

Raise

Description

Zookeeper connection failure. Possibly Zookeeper service is down, or hung. This will cause Live Data to fail during startup,
                                       or to failover if already up.

Action

Verify overall system health, i.e., services are up, disk partitions have free space, system is not CPU starved, not swapping,
                                       not I/O bound, etc. If problem persists, contact tech. support.

Message

Severity

Error

Type

Raise

Description

Attempt to write to, or read from, Zookeeper failed, but the error does not characterize Zookeeper to be down. The operation
                                       is attempted a few times before the error is reported, so it is very likely Zookeeper connection will be restarted in short
                                       order (which will trigger a Live Data Cluster failover).

Action

Verify overall system health, i.e., services are up, disk partitions have free space, system is not CPU starved, not swapping,
                                       not I/O bound, etc. If problem persists, contact tech. support.

Message

Severity

Error

Type

Raise

Description

Reports error/exception during attempt to connect or operate against Zookeeper instance. Depending on error, a failed connection
                                       to Zookeeeper is going to be declared, and Live Data Cluster failover will be triggered.

Action

Verify Zookeeper is up and running. Verify overall system health. If problem persists, contact tech. support.

Message

Severity

Informational

Type

Clear

Description

Indicates Live Data Cluster state.

Action

No action required.

Message

Severity

Error

Type

Raise

Description

Indicates failure during Cluster Peer spout initialization. Also informs failures during TOS request/response and cluster
                                       spout stop.

Action

Verify overall system health. Verify network integrity between Live Data and CCE servers (PG, Router, etc). Verify CCE servers
                                       (PG, Router, etc) are up and running. If problem persists, contact tech. support.

Message

Severity

Warning

Type

Raise

Description

Cluster Peer Spout failed to initialize JMS (ActiveMQ) subscriber for exchanging of cluster node state, which means cluster
                                       failover will not be functional. This can only happen during system startup.  JMS (ActiveMQ) configuration is incorrect, or
                                       service is down.

Action

Verify Live Data configuration, verify ActiveMQ service is up and running, and check overall system health. If problem persists,
                                       contact tech. support.

Message

Severity

Informational

Type

Clear

Description

Cluster Peer Spout successfully connected and subscribed to JMS (ActiveMQ) in order to exchange cluster node state.

Action

No action required.

Message

Severity

Warning

Type

Raise

Description

Cluster Peer Spout failed to initialize JMS (ActiveMQ) publisher for exchanging of cluster node state, which means cluster
                                       failover will not be functional. This can only happen during system startup.  JMS (ActiveMQ) configuration is incorrect, or
                                       service is down.

Action

Verify Live Data configuration, verify ActiveMQ service is up and running, and check overall system health. If problem persists,
                                       contact tech. support.

Message

Severity

Informational

Type

Clear

Description

Cluster Peer Spout successfully connected and can publish to JMS (ActiveMQ) in order to exchange cluster node state.

Action

No action required.

Message

Severity

Error

Type

Raise

Description

Cluster State Machine is in a state from which received event is invalid!

Action

Gather logs and contact tech. support.

Message

Severity

Informational

Type

Clear

Description

Indicates Cluster State Machine has satisfied all conditions to allow for event spouts to connect to CCE servers (PG, Router,
                                       etc).

Action

No action required.

Message

Severity

Critical

Type

Raise

Description

Indicates Cluster State Machine has detected a condition under which event spouts are not allowed to be connected to (or should
                                       disconnect from) CCE servers (PG, Router, etc).

Action

No action required.

Message

Severity

Critical

Type

Raise

Description

Indicates ActiveMQ transitioned to down/disconnected state. This will trigger a cluster failover.

Action

Verify ActiveMQ service is up. Verify network integrity between cluster nodes. Verify overall system health.

Message

Severity

Critical

Type

Clear

Description

Indicates ActiveMQ transitioned to up/connected state.

Action

No action required.

Message

Severity

Critical

Type

Raise

Description

Indicates ActiveMQ Netbridge transitioned to down/disconnected state. This might trigger a cluster failover depending on TOS
                                       request/response to far-end cluster node.

Action

Verify ActiveMQ service is up. Verify network integrity between cluster nodes. Verify overall system health.

Message

Severity

Critical

Type

Clear

Description

Indicates ActiveMQ Netbridge transitioned to up/connected state.

Action

No action required.

Message

Severity

Error

Type

Raise

Description

Reports database (typically AWDB) runtime error, informing object attempting DB access, and description of failure cause,
                                       including SQL query (where appropriate). Failure during connection to AWDB tables to memory, failure to access Hibernate element,
                                       failure creating DBSession.

Action

Determine if AWDB is available, and verify Live Data configuration and CUIC, specifically where it pertains to AWDB connection
                                       information on datasource tab in CUIC.

Message

Severity

Error

Type

Raise

Description

Reports database (typically AWDB) access error during retrieve/update elements, via Hiberate. Execute SQL query, retrieve
                                       column value.

Action

Determine if AWDB is available, and verify Live Data configuration and CUIC, specifically where it pertains to AWDB connection
                                       information on datasource tab in CUIC.

Message

Severity

Error

Type

Raise

Description

Reports failure during retrieval of configuration element which would allow Live Data a connection to Cassandra DB.

Action

Verify Live Data configuration.

Message

Severity

Error

Type

Raise

Description

Informs current version found in AWDB is not what Live Data expects to see. This indicates a schema mismatch. Live Data cannot
                                       proceed since no data from AWDB can be retrieved. This condition is detected during Live Data startup only.

Action

Gather logs, and contact tech. support.

Message

Severity

Informational

Type

Raise

Description

Reports failure, and cause, during connection attempt to Cassandra DB. Reports Cassandra configuration values used for Cassandra
                                       connection.

Action

Verify Live Data configuration, and assure Cassandra DB is up and running. No action required.

Message

Severity

Error

Type

Raise

Description

Reports failure during attempt to obtain connection, from Cassandra connection pool. Most likely connection pool is depleted
                                       and new connections to Cassandra DB are not possible.

Action

Ensure Cassandra DB is up. Verify in Live Data configuration points to Cassandra correctly, and that connection pool is large
                                       enough.

Message

Severity

Error

Type

Raise

Description

Reports failure during attempt to read/write to Cassandra DB, and, if available, a description of the problem.

Action

Ensure Cassandra DB is up, verify Live Data configuration points to Cassandra correctly.

Message

Severity

Error

Type

Raise

Description

Reports failure, and cause, while reading AWDB Config from Cassandra.

Action

Verify Live Data configuration, and ensure Cassandra DB is up and running, and AWDBConfig is present using cli "show live-data
                                       aw-access"

Message

Severity

Error

Type

Raise

Description

Live Data trapped an exception to which it has no recourse other than report and proceed.

Action

Gather logs and contact tech. support.

Message

Severity

Error

Type

Raise

Description

Live Data exception while performing operation on CCM Database connection pool

Action

Gather logs and contact tech. support.

Message

Severity

Error

Type

Clear

Description

The tick handler threw a runtime exception. Scenario Unknown.

Action

Contact tech. support.

Message

Severity

Error

Type

Clear

Description

The interval processor threw an exception. Scenario Unknown.

Action

Contact tech. support.

## Live Data TIP Server SNMP Notifications

Message

Severity

Error

Type

Raise

Description

The TIP Server failed to start. If TIP services are not required, disable TIP in the registry.

Action

If TIP services are required, configure the proper TIP address/port and restart the node. If TIP services are not required,
                                       disable TIP in the registry.

Message

Severity

Error

Type

Raise

Description

The TIP Server has been disabled.

Action

No action is required.

Message

Severity

Warning

Type

Raise

Description

The TIP Server is waiting for client connections.

Action

If condition persists, ensure that the Live Data client is running, has connectivity, and the correct configuration information
                                       to contact this TIP Server.

Message

Severity

Warning

Type

Raise

Description

The TIP Server is waiting for client connections.

Action

No action is required.

Message

Severity

Warning

Type

Raise

Description

The TIP Server client connection has failed.

Action

No action is required.

Message

Severity

Warning

Type

Raise

Description

The TIP Server has exceeded configured warning memory limits. The oldest TIP events are being deleted before acknowledgement
                                       is received, making event loss possible.

Action

If this condition persists, ensure that the Live Data client is running, has connectivity and correct configuration information
                                       to contact this TIP server.

Message

Severity

Error

Type

Raise

Description

The TIP Server has exceeded configured critical memory limits. The oldest TIP events are being deleted before acknowledgement
                                       is received, making event loss possible.

Action

If this condition persists, ensure that the Live Data client is running, has connectivity and correct configuration information
                                       to contact this TIP Server.

Message

Severity

Warning

Type

Raise

Description

The TIP Server is within configured memory limits.

Action

None

Message

Severity

Warning

Type

Raise

Description

The TIP Server has exceeded configured maximum queue size. The oldest TIP events are being deleted before acknowledgement
                                       is received, making event loss possible.

Action

If condition persists, ensure that the Live Data client is running, has connectivity and correct configuration information
                                       to contact this TIP Server.

Message

Severity

Warning

Type

Raise

Description

The TIP Server has exceeded configured warning memory limits, but has not met the TIP minimum queue size. No action will
                                       be taken, but the process may be unstable.

Action

Monitor process memory usage and take appropriate action if memory overflow is imminent.

Message

Severity

Error

Type

Raise

Description

The TIP Server has exceeded configured critical memory limits, but has not met the TIP minimum queue size. No action will
                                       be taken, but the process may be unstable.

Action

Monitor process memory usage and take appropriate action if memory overflow is imminent.

Message

Severity

Error

Type

Raise

Description

The TIP Server has exceeded configured critical memory limits. The oldest TIP events are being deleted before acknowledgement
                                       is received, making event loss possible.

Action

Monitor process memory usage and take appropriate action if memory overflow is imminent.

Message

Severity

Error

Type

Raise

Description

The TIP Server has exceeded configured critical memory limits, and has not met the TIP minimum queue size. TIP events will
                                       be deleted and events may be lost. The process may be unstable.

Action

Monitor process memory usage and take appropriate action if memory overflow is imminent.

## Outbound Option SNMP Notifications

Message

Severity

Error

Type

Raise

Description

The Outbound Option Campaign Manager is not running. Dialer(s) will only run for a short period of time without a Campaign
                                       Manager. In addition, configuration messages will not be forwarded to Dialer(s) or the Import process.

Action

Make sure the Campaign Manager process is enabled in the registry. Also, check that the Outbound Option database server is
                                       running. The Outbound Option private database should have been created with the ICMDBA tool.

Message

Severity

Informational

Type

Clear

Description

Outbound Option Campaign Manager is ready to distribute customer records and configuration data.

Action

No action is required.

Message

Severity

Error

Type

Single-State Raise

Description

The schema for a specified table has been changed but the overwrite option has not been enabled. This means that an existing
                                       database table does not match the configured import.

Action

Change the import to an overwrite import. This will drop the existing customer table and create a new table that will match
                                       the import. Please note that all existing customer data for that import will be lost.

Message

Severity

Error

Type

Single-State Raise

Description

Could not create the specified table due to invalid import schema definition.

Action

Check that all table columns for the failed import are correct. Making a character column too long could cause this failure.

Message

Severity

Error

Type

Single-State Raise

Description

This error could occur if the import file did not match the table definition.

Action

Check that the import table definition matches the import file.

Message

Severity

Error

Type

Single-State Raise

Description

A dialing list could not be populated from the specified table.

Action

Check if another process has the dialing list table locked. For example, if a report was running on the table while the dialing
                                       list was being generated.

Message

Severity

Error

Type

Single-State Raise

Description

The Outbound Option private database has not been initialized or SQL Server is not running.

Action

Make sure that SQL Server is running. Check the ODBC configuration settings for the Outbound Option private database. Was
                                       the ICMDBA tool run to create the Outbound Option private database?

Message

Severity

Error

Type

Single-State Raise

Description

An import started running but part of its configuration was deleted before it was able to do anything.

Action

Reschedule the import.

Message

Severity

Error

Type

Raise

Description

The Outbound Option CTI Server connection has been terminated.

Action

Make sure CTI Server is active. Also make sure the PIM has connectivity to the switch.

Message

Severity

Informational

Type

Clear

Description

Outbound Option CTI Server connection is active.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

A telephony error has occurred on a specific Dialer port. This may indicate a fault on the Dialogic telephony card, or the
                                       interface card on the switch. However, a more likely scenario is that a T1 line may have been disconnected or cut.

Action

Check that all wires going to the Dialer and the switch are intact. If port 0 failed, it means the first port on the first
                                       telephony card has received a failure message from the telephony driver. The first telephony card is the one that is assigned
                                       the lowest ID. The card's ID is assigned by a hardware switch on the top of the card. Ports are numbered consecutively across
                                       all ports.

Message

Severity

Informational

Type

Clear

Description

A previously malfunctioning telephony port has received a message from the telephony driver indicating the port is back in
                                       service.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

BAImport is not running on the specified host.

Action

Please check that the import process has not been shut down. Check that the Outbound Option private database has been created.
                                       Also, ensure that SQL Server is running.

Message

Severity

Informational

Type

Clear

Description

BAImport is running on the specified host.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

Dialer is down on the specified host.

Action

Please check that the Dialogic drivers are configured and running. Also, verify that the Dialer has been started by Node
                                       Manager.

Message

Severity

Informational

Type

Clear

Description

Dialer is up on the specified host.

Action

No action is required.

Message

Severity

Error

Type

Single-State Raise

Description

Failed to rename or delete the import file for import rule Id: @lt;id; filename@gt;. This import rule has been temporarily
                                       disabled. To correct this condition, manually remove the import file and disable and re-enable the import rule using Import
                                       Configuration Component.

Action

File polling is enabled for this import rule. After the import, the BAImport process was unable to rename or delete the file.
                                       This import rule is temporarily disabled. Rename or delete the import file, disable and re-enable this import rule from the
                                       BAImport Configuration Component.

Message

Severity

Error

Type

Single-State Raise

Description

Campaign [campaign name] tried to run a query [query name] and the database timed out.

Action

No action is required.

Message

Severity

Error

Type

Single-State Raise

Description

Database is running out of space.

Action

Please create some space in the database.

Message

Severity

Error

Type

Single-State Raise

Description

The agent skill group received is not configured for this campaign.

Action

Make sure the skill group configured in the script is the same as the skill group configured in the campaign.

Message

Severity

Warning

Type

Single-State Raise

Description

Timeout happening for the call on port.

Action

Timeout happening for a call on port. Check the registry key TimeToWaitForMRIResponse.

Message

Severity

Error

Type

Raise

Description

Media Routing PIM disconnected with the specified Dialer.

Action

Check if the MR PIM is active.

Message

Severity

Error

Type

Clear

Description

MR PIM connected to Dialer [dialer name].

Action

No action is required.

Message

Severity

Error

Type

Single-State Raise

Description

Import process has more than 10,000 errors.

Action

Restart the import process.

Message

Severity

Error

Type

Single-State Raise

Description

A Dialer with an incorrect protocol version is trying to connect to the Campaign Manager.

Action

Please check the Dialer version.

Message

Severity

Error

Type

Single-State Raise

Description

The DO Not Call (DNC) list to be imported has exceeded the number of DNC records set by ConfigLimit. Please check the CampaignManager
                                       log files for more details.

Action

Please check the DNC record limit set by the ConfigLimit tool.

Message

Severity

Error

Type

Single-State Raise

Description

Memory overflow. Not able to instantiate or assign enough memory.

Action

This is a memory outage, and the configuration of the system may not be sufficient.

Message

Severity

Error

Type

Single-State Raise

Description

Dialer: Unknown port owner.

Action

Please check the administrator scripts.

Message

Severity

Error

Type

Single-State Raise

Description

Cannot find the specified key in the Windows registry.

Action

Please ensure that the installation process went smooth.

Message

Severity

Error

Type

Single-State Raise

Description

Unable to open registry key.

Action

Please ensure that the installation process was successful.

Message

Severity

Error

Type

Single-State Raise

Description

Campaign Manager could not connect to the Outbound Option private database.

Action

Make sure that SQL Server is running and the Outbound Option private database is initialized.

Message

Severity

Error

Type

Single-State Raise

Description

Dialer attempted to connect to incorrect Campaign Manager version.

Action

Please ensure that the Campaign Manager is compatible with the Dialer version.

Message

Severity

Error

Type

Single-State Raise

Description

Your configured dialer type doesn't match this dialer type.

Action

Please check the dialer type configured. IP or SIP.

Message

Severity

Error

Type

Single-State Raise

Description

Dialer has too many ports configured.

Action

Please decrease the number of ports configured.

Message

Severity

Error

Type

Single-State Raise

Description

Internal error: Unable to convert SystemTime to FileTime.

Action

No action is required.

Message

Severity

Error

Type

Raise

Description

Outbound Option SIP server heart beat failure, the connection is down.

Action

Please make sure SIP server is alive and reachable from Outbound Option SIP dialer.

Message

Severity

Informational

Type

Clear

Description

Outbound Option SIP server heartbeat ACK received, the connection is up.

Action

No action is required.

Message

Severity

Error

Type

Single-State Raise

Description

Outbound Option private database version is not correct. It needs to be upgraded using EDMT.

Action

Please upgrade private database to the correct version using EDMT for this release.

Message

Severity

Error

Type

Single-State Raise

Description

Static route file, ..\Dialer\DNPHost, is missing or has no valid static route entry when configuring the SIP Dialer to connect
                                       to voice gateway.

Action

Re-run the Dialer setup to install sample DNPHost file, and/or enter valid static route entry.

Message

Severity

Error

Type

Single-State Raise

Description

CPA is disabled or not supported on voice gateway.

Action

Please enable CPA on voice gateway.

Message

Severity

Error

Type

Single-State Raise

Description

Outbound Option database space utilization has reached the threshold limit.

Action

Please increase the database space utilization or remove unnecessary records from the Outbound Option database.

Message

Severity

Informational

Type

Single-State Raise

Description

Campaign skill group has insufficient customer records.

Action

Please increase the "records to cache" from the campaign configuration.

Message

Severity

Warning

Type

Single-State Raise

Description

The capacity of voice gateway or carrier has been exceeded.

Action

Please check the capacity of voice gateway or carrier, and adjust the value of "Port Throttle" from the Dialer configuration
                                       accordingly.

Message

Severity

Warning

Type

Single-State Raise

Description

SIP Dialer decreases the port throttle since the capacity of voice gateway or carrier is exceeded.

Action

Please adjust the value of "Port Throttle" from the Dialer configuration or check the Design Guide for the proper sizing
                                       calculation for the Outbound Dialer.

Message

Severity

Error

Type

Raise

Description

There is a change in the congestion level of the Outbound Option Campaign Manager and thus a change in the dialer port throttle
                                       percentage. The Campaign Manager will throttle the dialers according to the congestion level, throttling each dialer back
                                       to a predetermined percentage of full capacity in order to preserve Campaign Manager throughput and prevent a possible brief
                                       outage.

Action

The Campaign Manager has exceeded its maximum throughput capacity. Re-evaluate the system design if the congestion occurs
                                       frequently since the system is not able to maintain the high dialing rate. If congestion is occurring at a dialing rate that
                                       was once sustained without congestion, please examine the BA database for fragmentation and/or for a large number of unnecessary
                                       rows of data (i.e. please purge unneeded data from the database).

Message

Severity

Warning

Type

Clear

Description

The Campaign Manager is currently not congested and the dialers have resumed dialing at full capacity.

Action

None

Message

Severity

Warning

Type

Single-State Raise

Description

There is a change in the current state of the Outbound Option Campaign Manager. This typically occurs when one Campaign Manager
                                       side has failed-over to the peer side. A failover may be due to a failure of the Campaign Manager on one side or due to connectivity
                                       issues with the Router, the dialers or the Import process. Only one Campaign Manager will be in an 'active' state at a given
                                       time, the other being in a 'standby' state.

Action

If the state change is not due to an administrator intentionally shutting down the Logger service on the node where the active
                                       Campaign Manager is coresident, determine whether the state change is due to a failure of the active Campaign Manager (check
                                       the event logs for errors). Lastly, ensure that there are no connectivity issues between the active Campaign Manager and the
                                       Router, the Import process or the dialers.

Message

Severity

Error

Type

Single-State Raise

Description

The number of records in the contact table has exceeded the threshold limit, that may in turn be triggered owing to the import
                                       being performed without the overwrite option, or the number of records in the import file being large. A large Contact table
                                       can result in slow creation of dialing lists as well as excessive space utilization in the BA database

Action

Run import corresponding to table with overwrite flag enabled or increase the threshold limit.

## ICM Network Interface Controller SNMP Notifications

| Note | The message ID also contains the severity in the two most significant
                                             							bits of the integer value. The message ID value shown is with these two
                                             							bits masked to zero. Alarms with an asterisk (*) next to the Message ID are deemed to be
                                             							critical alarms. The %n variable (where n is a
                                             							numeric value) indicates a substitution field whereby node-specific or
                                             							process-specific information is inserted. |
|---|---|

| Message ID (hex) | Property | Value |
|---|---|---|
| 106003A | Message | World Wide Web Publishing Service may be down. ICM is unable to communicate with web server. |
| Severity | Error |
| Type | Raise |
| Description | World Wide Web Publishing Service may be down. ICM is unable to communicate with web server. |
| Action | If the World Wide Web Publishing Service is not running, restart it or look for the messages in the IIS error log. |
| 106003B | Message | World Wide Web Publishing
                                       				  Service is up. |
| Severity | Informational |
| Type | Clear |
| Description | World
                                       				  Wide Web Publishing Service is up. |
| Action | No action
                                       				  is required. |

| Message ID (hex) | Property | Value |
|---|---|---|
| 1028101 | Message | %1 Node Manager initializing. |
| Severity | Warning |
| Type | Clear |
| Description | The node management library, common to all ICM processes, is initializing itself. This is a standard practice when a process
                                       (re)starts. |
| Action | No action is required. |
| 1028103 | Message | The operator requested for the shutdown, %1 Node Manager is now functional. |
| Severity | Informational |
| Type | Clear |
| Description | The Node Manager successfully started. The Node Manager shutdown because the operator requested a clean shutdown of the ICM
                                       node. |
| Action | No action is required. |
| 1028104 | Message | %1 Node Manager started. Last shutdown was due to system shutdown. |
| Severity | Informational |
| Type | Clear |
| Description | The Node Manager successfully started. The last reason the Node Manager stopped was because a clean shutdown of the node
                                       was requested by the operator. |
| Action | No action is required. |
| 1028105 | Message | The operator/administrator has shutdown the ICM software on: %1. |
| Severity | Warning |
| Type | Raise |
| Description | The Node Manager on the ICM node has given the command to stop ICM services. This happens when an operator/administrator stop
                                       the ICM services using ICM Service Control, "nmstop", "net stop", Control Panel Services, or shutsdown the node. |
| Action | Contact the operator/administrator to determine the reason for the shutdown. |
| 1029101 | Message | %1 Node Manager Manager started. |
| Severity | Informational |
| Type | Clear |
| Description | The Node Manager process (which supervises the Node Manager) has started. |
| Action | No action is required. |
| 102C101 | Message | Node: %1, critical process: %2, has terminated. Rebooting node. |
| Severity | Error |
| Type | Raise |
| Description | A critical process required to run the ICM software on this node has terminated execution. The Node Manager is forced to
                                       reboot the node. |
| Action | Contact the technical assistance center. |
| 102C103 | Message | Node: %1, restarting process: %2. |
| Severity | Warning |
| Type | Clear |
| Description | The Node Manager is restarting a process. |
| Action | No action is required. |
| 102C107 | Message | The last shutdown was to reboot the Node Manager after the failure of critical process. %1 Node Manager started. |
| Severity | Informational |
| Type | Clear |
| Description | The Node Manager requested the shutdown since a critical process for the node failed. The Node Manager started. |
| Action | No action is required. |
| 102C108 | Message | The reason for the last shutdown is unknown. Possible causes includes a power failure, a system failure or a Node Manager
                                       exit. %1 Node Manager started. |
| Severity | Error |
| Type | Clear |
| Description | The Node Manager unable to determine the reason for the system restart. Possible causes are power failure, a system failure (e.g. a Windows blue screen), a system not responding (in which an operator
                                       is forced to reboot), or a Node Manager exit. The Node Manager started. |
| Action | Contact the technical assistance center. |
| 102C109 | Message | Node: %4, process: %5, exited after %1 seconds. Minimum required uptime for process: %5 is %2 seconds. Delaying process restart
                                       for %3 seconds. |
| Severity | Warning |
| Type | Raise |
| Description | A process exited after running for '%1' seconds. Such processes must run for a minimum amount of time before the Node Manager
                                       will automatically restart them after they terminate. The Node Manager will restart the process after delaying a number of seconds for other environmental changes to complete. |
| Action | No action is required. |
| 102C10A | Message | Node: %2, restarting process: %3, after having delayed restart for %1 seconds. |
| Severity | Warning |
| Type | Clear |
| Description | The Node Manager is restarting a process after the requisite delay. |
| Action | No action is required. |
| 102C10B | Message | Terminating process: %2. |
| Severity | Error |
| Type | Raise |
| Description | The Node Manager reports the termination of a process. |
| Action | No action is required. |
| 102C10C | Message | Node: %1, process: %2, exited after having detected a software failure. |
| Severity | Error |
| Type | Raise |
| Description | A process exited (terminated itself) after it detected an internal software error. |
| Action | If the process continues to terminate itself, call the technical assistance center for help in diagnosing the problem. |
| 102C10D | Message | Node: %1, process: %2, has detected a failure. Node Manager is restarting the process. |
| Severity | Warning |
| Type | Raise |
| Description | The specified process has detected a situation that requires it to ask the Node Manager to restart it. This often indicates
                                       a problem external to the process itself (for example, some other process may have failed). |
| Action | Node Manager on the ICM node will restart the process. The node should be checked to ensure that it is online. The process
                                       logs may be examined for root cause. |
| 102C10E | Message | Node: %1, process: %2, went down for an unknown reason. Exit code: %3. It will be automatically restarted. |
| Severity | Error |
| Type | Raise |
| Description | The specified process exited (terminated) with the indicated exit code. This termination is unexpected; the process died
                                       for an unknown reason. It will be automatically restarted. |
| Action | Determine if the process has returned to service or has stayed offline. If the process is offline or "bouncing", determine
                                       root cause from the process logs. |
| 102C10F | Message | Node: %3, process: %4, is down after running for %1 seconds. It will restart after delaying %2 seconds for related operations
                                       to complete. |
| Severity | Warning |
| Type | Raise |
| Description | Specified process is down after running for the indicated number of seconds. It will restart after delaying for the specified
                                       number of seconds for related operations to complete. |
| Action | Determine if the process has returned to service or has stayed offline. If the process is offline or "bouncing", determine
                                       root cause from the process logs. |
| 102C110 | Message | Node: %1, process: %2, successfully reinitialized after restart. |
| Severity | Warning |
| Type | Clear |
| Description | A process was successfully restarted. |
| Action | No action is required. |
| 102C111 | Message | Node: %1, process: %2, successfully started. |
| Severity | Informational |
| Type | Clear |
| Description | The process was successfully started. |
| Action | No action is required. |
| 102C112 | Message | Node: %1, process: %2, exited cleanly and requested that it be restarted by the Node Manager. |
| Severity | Warning |
| Type | Raise |
| Description | A process terminated itself successfully, and has requested the Node Manager to restart it. |
| Action | No action is required. |
| 102C113 | Message | Node: %1, process: %2, exited from Ctrl-C or window close. |
| Severity | Warning |
| Type | Raise |
| Description | A process exited as a result of a CTRL-C request or a request to close the process's active window. |
| Action | No action is required. |
| 102C114 | Message | Node: %1, process: %2, exited and requested that the Node Manager reboot the system. |
| Severity | Error |
| Type | Raise |
| Description | A process terminated itself successfully but, due to other conditions, has requested that the Node Manager to reboot the
                                       system. |
| Action | No action is required. |
| 102D101 | Message | %3 Node Manager exited after having been up for %1 seconds. Scheduling system reboot in %2 seconds. |
| Severity | Error |
| Type | Raise |
| Description | The Node Manager has itself exited after having run for "%1" seconds. The system will be rebooted after waiting a few seconds
                                       for related operations to complete. |
| Action | Contact the technical assistance center. |
| 102D102 | Message | %2 Node Manager exited after having been up for %1 seconds. Auto-reboot is disabled. Will attempt service restart. |
| Severity | Error |
| Type | Raise |
| Description | The Node Manager has itself exited after having run for "%1" seconds. The system cannot be rebooted since auto-reboot is
                                       disabled. The Node Manager Manager will attempt to restart the service. |
| Action | Contact the technical assistance center. |
| 102D103 | Message | %3 Node Manager requested reboot after having been up for %1 seconds. Scheduling system reboot in %2 seconds. |
| Severity | Error |
| Type | Raise |
| Description | The Node Manager has requested the system to be rebooted after having run for "%1" seconds. The system will be rebooted after
                                       waiting a few seconds for related operations to complete. |
| Action | Contact the technical assistance center. |
| 102D104 | Message | %2 Node Manager requested reboot after having been up for %1 seconds. Auto-reboot is disabled. Will attempt service restart. |
| Severity | Error |
| Type | Raise |
| Description | The Node Manager has requested the system to be rebooted after having run for "%1" seconds. The system cannot be rebooted
                                       since auto-reboot is disabled. The Node Manager Manager will attempt to restart the service. |
| Action | Contact the technical assistance center. |
| 102D105 | Message | %2: A critical process has requested a reboot after the service has been up for %1 seconds. Auto-reboot on process request
                                       is disabled. Will attempt service restart. |
| Severity | Error |
| Type | Raise |
| Description | A critical process has requested a reboot after the service has been up for "%1" seconds. The system cannot be rebooted since
                                       auto-reboot on process request is disabled. The Node Manager Manager will attempt to restart the service. |
| Action | Contact the technical assistance center. |
| 102D106 | Message | %3: A critical process has requested a reboot after having been up for %1 seconds. Scheduling system reboot in %2 seconds. |
| Severity | Error |
| Type | Raise |
| Description | A critical process has requested the system to be rebooted after having run for "%1" seconds. The system will be rebooted
                                       after waiting "%2" seconds. |
| Action | Contact the technical assistance center. |

| Message ID (hex) | Property | Value |
|---|---|---|
| 10F8004 | Message | Device: %1, path changing to idle state. |
| Severity | Informational |
| Type | Clear |
| Description | The indicated device is using this side of the central controller for its idle communication path (and is therefore using
                                       the other side of the central controller for its active communication path). |
| Action | No action is required. |
| 10F8005 | Message | Device: %1, path changing to active state. |
| Severity | Informational |
| Type | Clear |
| Description | The indicated device is using this side of the central controller for its active communication path. |
| Action | No action is required. |
| 10F8007 | Message | Device: %1, path realignment failed. |
| Severity | Error |
| Type | Raise |
| Description | The indicated device failed to realign its message stream to this side of the central controller. |
| Action | No action is required. |
| 10F8008 | Message | Device: %1, disconnected. |
| Severity | Error |
| Type | Raise |
| Description | The indicated device has been disconnected from this side of the central controller. This may be caused by a network problem
                                       or device failure. |
| Action | Remedy network problems, if any. Call the Cisco Systems, Inc. technical assistance center in the event of a software failure
                                       on the device. |
| 10F800E | Message | Device: %1, path reset. |
| Severity | Warning |
| Type | Raise |
| Description | The communication path between this side of the central controller and the indicated device has been reset to an initial
                                       state. |
| Action | No action is required. |
| 10F800F | Message | Device: %1, initializing message stream. |
| Severity | Informational |
| Type | Clear |
| Description | The indicated device is initializing its message stream with this side of the central controller. |
| Action | No action is required. |
| 10F801D | Message | The network communications between ICM router and Peripheral Gateway or NIC: %2 has been down for: %1 minutes. |
| Severity | Warning |
| Type | Raise |
| Description | No communication path from the indicated device to this side of the central controller has existed for the indicated time
                                       period. This indicates either an extended network outage or an extended outage at the device. |
| Action | One or more network links between the named device and the named side of the ICM router has failed. If alarms exist for BOTH
                                       routers, the site is offline. If alarms exist for one side of the router, then the site should be up but network redundancy
                                       is degraded. Communication (network) between the central controller (router) and the PG should be checked using "ping" and
                                       "tracert". Must have visible and visible high priority connection from PG to router. CCAG process on router and PGAG process
                                       on PG should be checked. |
| 1040010 | Message | Synchronizer timed out trying to establish connection to peer. |
| Severity | Warning |
| Type | Raise |
| Description | The MDS message synchronizer was unable to connect to its duplexed partner within the timeout period. Either the duplexed
                                       partner is down, or there is no connectivity to the duplexed partner on the private network. |
| Action | Verify reliable network connectivity on the private network. Call the Cisco Systems, Inc. technical assistance center in
                                       the event of a software failure on the duplexed partner. |
| 1040022 | Message | Connectivity with duplexed partner has been lost due to a failure of the private network, or duplexed partner is out of service. |
| Severity | Error |
| Type | Raise |
| Description | The MDS message synchronizer has lost connectivity to its duplexed partner. This indicates either a failure of the private
                                       network, or a failure of the duplexed partner. |
| Action | Confirm services are running on peer machine. Check MDS process to determine if it is paired or isolated. Ping test between
                                       peers over the private network. Check PGAG and MDS for TOS (Test Other Side) messages indicating the private network has failed
                                       and MDS is testing the health of the peer over the public network. |
| 1040023 | Message | Communication with peer Synchronizer established. |
| Severity | Informational |
| Type | Clear |
| Description | The MDS message synchronizer has established communication with its duplexed partner. |
| Action | No action is required. |
| 104802A | Message | MDS time delivery queue size is increasing, current size is: %1, but will continue to send messages. |
| Severity | Warning |
| Type | Single-State Raise |
| Description | MDS time delivery queue size is increasing over time. |
| Action | Ensure that the ICM/IPCC configuration (# agents, # skills/agent, # PGs) is within the supported limit. |

| Message ID (hex) | Property | Value |
|---|---|---|
| 12B0013 | Message | Application Gateway has
                                       				  failed. Application Gateway ID: %1. |
| Severity | Error |
| Type | Raise |
| Description | An application gateway connection has failed. This means that
                                       				  the application gateway process has attempted to connect to the host the number
                                       				  of times indicated in the Session Retry Limit field and has failed. It will not
                                       				  try to reconnect again until the connection is taken out of service and brought
                                       				  back into service. |
| Action | Determine why the Application Gateway cannot connect to the
                                       				  host. Verify the connection between the two VMs. After fixing the issue, take
                                       				  the Application Gateway out of service and then bring it back in service. |
| 12B001F | Message | Application Gateway has
                                       				  connected with the host. Application Gateway ID: %1. |
| Severity | Informational |
| Type | Clear |
| Description | The application gateway is now connected to the host process. |
| Action | No action is required. |
| 12B0020 | Message | Application Gateway is not
                                       				  connected to the host. Application Gateway ID: %1; routing may be
                                       				  impacted. |
| Severity | Error |
| Type | Raise |
| Description | An external application used in some scripts has disconnected
                                       				  from the specified Application Gateway. Error recovery mechanisms will attempt
                                       				  to reconnect. Routing may be impacted. |
| Action | Verify the connection properties in the Application Gateway
                                       				  configuration. If the host application was off-line for a long time, restart
                                       				  the Application Gateway to reconnect. |
| 12B0030 | Message | Contact share node
                                       				  connection to Live Data %1 is Up. |
| Severity | Informational |
| Type | Clear |
| Description | The Contact Share node connection to Live Data is up. |
| 12B0031 | Message | Contact share node
                                       				  connection to Live Data %1 is Down. |
| Severity | Error |
| Type | Raise |
| Description | The Contact Share node connection to Live Data is down. |
| 12B0034 | Message | Contact share node has
                                       				  determined that none of the configured AW hosts are active or have current
                                       				  data. |
| Severity | Error |
| Type | Raise |
| Description | The Contact Share node has determined that none of the
                                       				  configured AW hosts are active or have current data. |
| 12B0035 | Message | Contact share node is able
                                       				  to connect to AW and is able to retrieve data. |
| Severity | Informational |
| Type | Clear |
| Description | The Contact Share node is able to connect to the AW and is able
                                       				  to retrieve data. |
| 105007D | Message | Peripheral: %2 (ID: %1) is
                                       				  on-line. |
| Severity | Informational |
| Type | Clear |
| Description | The specified peripheral is on-line to the ICM. Call and agent
                                       				  state information is being received by the Router for this site. |
| Action | No action is required. |
| 105007E | Message | ACD/IVR: %2 (ID: %1) is
                                       				  off-line and not visible to the Peripheral Gateway. Routing to this site is
                                       				  impacted. |
| Severity | Error |
| Type | Raise |
| Description | The specified ACD/IVR is not visible to the Peripheral Gateway.
                                       				  No call or agent state information is being received by the Router from this
                                       				  site. Routing to this site is impacted. |
| Action | If Peripheral Gateway is also offline per messaging (message ID
                                       				  10500D1) or "rttest" result, then first proceed with troubleshooting for
                                       				  Peripheral Gateway off-line alarm. Otherwise ACD/IVR Vendor should be contacted
                                       				  for resolution. |
| 10500D0 | Message | Physical controller: %2
                                       				  (ID: %1) is on-line. |
| Severity | Informational |
| Type | Clear |
| Description | The Router is reporting that physical controller "%2" is
                                       				  on-line. |
| Action | No action is required. |
| 10500D1 | Message | Peripheral Gateway: %2 (ID:
                                       				  %1) is not connected to the central controller or is out of service. Routing to
                                       				  this site is impacted. |
| Severity | Error |
| Type | Raise |
| Description | The specified Peripheral Gateway is not connected to the
                                       				  central controller. It could be down. Possibly it has been taken out of
                                       				  service. Routing to this site is impacted. |
| Action | Communication (network) between the central controller (Router)
                                       				  and the PG should be checked using "ping" and "tracert". You must have a
                                       				  visible high priority connection from the PG to the Router. The CCAgent process
                                       				  on the Router and the PGAgent process on the PG should be checked. The PG may
                                       				  have been taken out of service for maintenance. |
| 10500D2 | Message | PG has reported that
                                       				  peripheral: %2 (ID: %1) is operational. |
| Severity | Informational |
| Type | Clear |
| Description | PG has reported that peripheral "%2" (ID "%1") is operational. |
| Action | No action is required. |
| 10500D3 | Message | PG has reported that
                                       				  peripheral: %2 (ID: %1) is not operational. |
| Severity | Error |
| Type | Raise |
| Description | This may indicate that the peripheral is off-line for
                                       				  maintenance or that the physical interface between the peripheral and the PG is
                                       				  not functioning. |
| Action | Check that the peripheral is not off-line and that the
                                       				  connection from the peripheral to the PG is intact. |
| 10500E9 | Message | UpdateCC from: %1 on: %2, rejected because no Loggers are in operation. |
| Severity | Error |
| Type | Single-State Raise |
| Description | The attempt to update the central controller configuration was rejected because none of the Loggers are operational. Note This SNMP Notification is supported with UCCE 12.6(2) if CCE 12.6(2)_ES 36 is installed. | Note | This SNMP Notification is supported with UCCE 12.6(2) if CCE 12.6(2)_ES 36 is installed. |
| Note | This SNMP Notification is supported with UCCE 12.6(2) if CCE 12.6(2)_ES 36 is installed. |
| Action | Retry the update operation after at least one of the Loggers is operational. |
| 10500F6 | Message | Script table: %2 (ID: %1)
                                       				  is available only on side A. |
| Severity | Informational |
| Type | Raise |
| Description | Script table "%2" is only available on the side A Router. If
                                       				  the side A Router goes down, no DBLookup requests can be processed as side B
                                       				  cannot access the script table. |
| Action | Configure a script table on side B that is identical to that on
                                       				  side A. |
| 10500F7 | Message | Script table: %2 (ID: %1)
                                       				  is available only on side B. |
| Severity | Informational |
| Type | Raise |
| Description | Script table "%2" is only available on the side B Router. If
                                       				  the side B Router goes down, no DBLookup requests can be processed as side A
                                       				  cannot access the script table. |
| Action | Configure a script table on side B that is identical to that on
                                       				  side A. |
| 10500F8 | Message | Script table: %2 (ID: %1)
                                       				  is not available on either side. |
| Severity | Error |
| Type | Raise |
| Description | No DBLookup requests can be processed as script table "%2" is
                                       				  unavailable on either side of the central controller. |
| Action | Configure a script table on either side A or side B, or both. |
| 10500F9 | Message | Script table: %2 (ID: %1)
                                       				  is available on both sides A & B. |
| Severity | Informational |
| Type | Clear |
| Description | Script table "%2" is configured on both sides of the central
                                       				  controller. |
| Action | No action is required. |
| 10500FF | Message | Side: %1: %2 process is
                                       				  OK. |
| Severity | Informational |
| Type | Clear |
| Description | The Router is reporting that side "%1" process "%2" is OK. |
| Action | No action is required. |
| 1050100 | Message | Process: %2 at the central
                                       				  site side: %1 is down. |
| Severity | Error |
| Type | Raise |
| Description | This alarm only occurs for central controller (Router and
                                       				  Logger) processes. If the process for BOTH sides is down there is a total
                                       				  failure for that process. This could be part of Router shutdown. Critical
                                       				  processes: - "mds" (Router/Logger): coordinates messaging between duplexed
                                       				  Routers AND Loggers. When mds is down the central controller is down and no
                                       				  calls are being routed. - "rtr" (Router): call routing intelligence. -
                                       				  "clgr/hlgr" (Logger) - configuration/historical data processing to
                                       				  configuration database. - "rts" (Router): Real Time Server data feed from the
                                       				  Router to the Admin Workstations for reporting. - "rcv" (Logger Recovery):
                                       				  keeps the redundant historical databases synchronized between duplexed Loggers. |
| Action | No action is required. |
| 10501F1 | Message | ICM node: %2 (ID: %1) is
                                       				  on-line. |
| Severity | Informational |
| Type | Clear |
| Description | The specified node is on-line to the ICM. |
| Action | No action is required. |
| 10501F2 | Message | ICM node: %2 (ID: %1) is
                                       				  off-line. |
| Severity | Error |
| Type | Raise |
| Description | The specified node is not visible to the ICM. Distribution of
                                       				  real time data may be impacted. |
| Action | No action is required. |
| 10501F6 | Message | The Router's state size of:
                                       				  %1 MB is now below the alarm limit of: %2 MB. |
| Severity | Informational |
| Type | Clear |
| Description | The Router's state size of "%1" MB is now below the alarm limit
                                       				  of "%2" MB. |
| Action | No action is required. |
| 10501F7 | Message | The Router's state size of:
                                       				  %1 MB has grown beyond the alarm limit of: %2 MB. |
| Severity | Error |
| Type | Raise |
| Description | The Router's state size of "%1" MB has grown beyond the alarm
                                       				  limit of "%2" MB. This may indicate a memory leak, or it may indicate that the
                                       				  customer's configuration size has grown larger. Large state sizes may cause
                                       				  problems when synchronizing Routers, so the bandwidth of the private link may
                                       				  also need to be investigated. |
| Action | The alarm limit can be raised with the "rtsetting" tool. |
| 10501F8 | Message | ICM node: %2 (ID: %1), on
                                       				  system: %3, is on-line. |
| Severity | Informational |
| Type | Clear |
| Description | The specified node is on-line to the ICM. |
| Action | No action is required. |
| 10501F9 | Message | ICM node: %2 (ID: %1), on
                                       				  system: %3, is off-line. |
| Severity | Error |
| Type | Raise |
| Description | The specified node is not visible to the ICM. Distribution of real time data may be impacted. This condition can exist briefly
                                       while the system is loading. If it does not clear, it may indicate a problem with the node or the communications paths that
                                       connect the Router and node. |
| Action | Check the communication paths that connect the Router and the
                                       				  node. |
| 10501FD | Message | The Router has completed
                                       				  loading the initial configuration from the Logger. |
| Severity | Informational |
| Type | Clear |
| Description | The specified node is on-line to the ICM. |
| Action | No action is required. |
| 10501FE | Message | The Router has not loaded a
                                       				  configuration from the Logger. |
| Severity | Error |
| Type | Raise |
| Description | This condition indicates that the Router has not yet completed the initialization step of loading a configuration from the
                                       Logger. This condition can exist briefly while the system is loading. If it does not clear, it may indicate a problem with
                                       the Logger or the communications paths that connect the Router and the Logger. |
| Action | Check the communication paths that connect the Router and the
                                       				  Logger. |
| 105023C | Message | The Router has detected
                                       				  that it is no longer synchronized with its partner. |
| Severity | Error |
| Type | Single-State Raise |
| Description | The Router has detected that it is no longer synchronized with
                                       				  its partner. One result of this is that the Router might be routing some calls
                                       				  incorrectly. |
| Action | Stop the Router on both sides. After both sides are completely stopped, restart both Routers. Alternate Action: Restart the
                                       Router on one side. After doing this, the Routers might still route some calls incorrectly, but they will be in sync. |
| 105029A | Message | Congestion level changed
                                       				  from: %1, with rejection percentage: %2, to congestion level: %3, with
                                       				  rejection percentage: %4, on: %5. |
| Severity | Error |
| Type | Raise |
| Description | There is a change in the congestion level of the Router which
                                       				  implies that there is a change in the call rejection percentage also. When
                                       				  congestion control is enabled, the system will reject or treat the calls
                                       				  according to the congestion level and rejection percentage determined. When
                                       				  congestion control is disabled, the system will not reject or treat the calls
                                       				  until the congestion enabled option is turned on in the congestion control
                                       				  settings gadget. |
| Action | The system has exceeded the designed capacity. Re-evaluate the
                                       				  system design if the congestion occurs frequently. When congestion control is
                                       				  disabled and the system is congested, you can turn on the congestion enabled
                                       				  option in the congestion control settings gadget to reject or treat the
                                       				  congested calls. |
| 105029B | Message | The system congestion
                                       				  control level has moved to the normal operating level for the deployment:
                                       				  %1. |
| Severity | Warning |
| Type | Clear |
| Description | The Router is currently not congested. |
| Action | None |
| 105029D | Message | Total number of agent skill
                                       				  group pairs: %1, exceeds the defined system default limit: %2. |
| Severity | Error |
| Type | Single-State Raise |
| Description | Total number of agent skill group pairs exceeds the defined
                                       				  system default limit. |
| Action | Log out agents or remove skill groups associated to the agent
                                       				  such that the agent skill group pair count does not exceed the defined system
                                       				  default limit. |
| 10502B0 | Message | Error: %1 |
| Severity | Error |
| Type | Raise |
| Description | The Contact Share connection to the application gateway is
                                       				  down. |
| 10502B9 | Message | Informational: %1 |
| Severity | Informational |
| Type | Clear |
| Description | The Contact Share connection to the application gateway is up. |
| 10502BA | Message | Informational: %1 |
| Severity | Informational |
| Type | Clear |
| Description | The Contact Share connection to the application gateway is
                                       				  active. |
| 10502BB | Message | Informational: %1 |
| Severity | Informational |
| Type | Raise |
| Description | The Contact Share connection to the application gateway is
                                       				  inactive. |
| 10502BE | Message | The deployment has reached
                                       				  the maximum agent capacity of: %1. |
| Severity | Warning |
| Type | Raise |
| Description | The number of logged-in agents has reached the maximum capacity
                                       				  supported by this deployment type. |
| Action | No action is required. |
| 10502BF | Message | The deployment is below the
                                       				  maximum agent capacity of: %1. |
| Severity | Informational |
| Type | Clear |
| Description | The number of logged-in agents is now below the maximum
                                       				  capacity supported by this deployment type. |
| Action | No action is required. |

| Note | This SNMP Notification is supported with UCCE 12.6(2) if CCE 12.6(2)_ES 36 is installed. |
|---|---|

| Message ID (hex) | Property | Value |
|---|---|---|
| 12A0001 | Message | Message Delivery Service (MDS) feed from the router to the logger has failed. |
| Severity | Error |
| Type | Raise |
| Description | Indicates that the MDS event feed connection from the ICM router to the CSFS process on the logger has failed. |
| Action | No action is required. |
| 12A0002 | Message | MDS is in service. |
| Severity | Informational |
| Type | Clear |
| Description | Indicates MDS event feed connection from ICM router to CSFS process has connected. |
| Action | If not a planned startup of the system, determine if the event is due to process, network, or system failure. |
| 12A0003 | Message | Heartbeat event for: %1. |
| Severity | Informational |
| Type | N/A |
| Description | Periodic message sent to indicate that the ICM Message Delivery Service (MDS) is in service and the system on which event
                                       management system processes reside can send events to the configured listener system. This message is also passed to the SNMP
                                       agent to indicate that the event stream is active. |
| Action | No action is required. |
| 12A4001 | Message | SDDSN registration has been completed with system: %1, process: %2, using unique ID: %3. The registered system can now send
                                       diagnostic data via the SDDSN server. |
| Severity | Informational |
| Type | Clear |
| Description | A system (via a particular process), connected to the SDDSN server has successfully registered as a valid endpoint using
                                       a unique ID. The system can now start sending diagnostic event data using the SDDSN server. |
| Action | No action is required. |
| 12A4002 | Message | SDDSN unregistration was never received from system: %1, process: %2, using unique ID: %3. The registered system abruptly
                                       disconnected from the SDDSN server. |
| Severity | Error |
| Type | Raise |
| Description | A system (via a particular process), connected to the SDDSN server has failed to unregistered as a valid endpoint using a
                                       unique ID. This indicates that the system abruptly disconnected from the SDDSN server. |
| Action | This could indicate that the SDDSN server has failed or the TCP/IP connection to the server was lost. If this is a fault
                                       tolerant SDDSN server, check to see if the secondary SDDSN server has successfully re-registered the system). This would be
                                       indicated by a CLEAR condition to this alarm while the side of SDDSN that is reporting would be the other SDDSN server. If
                                       the primary SDDSN server is still running, check to see if you can ping between the system and the primary SDDSN server. Other
                                       scenarios include a simplex SDDSN server failure or lost TCP/IP connection, or the system that was communicating with the
                                       SDDSN server has somehow failed. |
| 12A4003 | Message | SDDSN unregistration has been received from system: %1, process: %2, using unique ID: %3. The registered system has indicated
                                       that it will stop sending diagnostic data via the SDDSN server. |
| Severity | Informational |
| Type | Clear |
| Description | A system (via a particular process), connected to the SDDSN server has successfully unregistered as a valid endpoint using
                                       a unique ID. This indicates that the system gracefully disconnected from the SDDSN server. |
| Action | No action is required. |
| 12A400A | Message | The SDDSN server is missing, or has outdated, resource files and cannot decipher messages for product: %1, (%3). Message ID
                                       = %2 |
| Severity | Error |
| Type | Single-State Raise |
| Description | An event has been received that the SDDSN server cannot decipher using the resource files (message DLLs) because they are
                                       missing or out of date. The SDDSN server has forwarded the ciphered event, and then disconnected the system that generated
                                       that event. %1 is the product number (in decimal). %2 is the Message ID that was sent. A value of 0 indicates that none of
                                       the messages can be deciphered. %3 is the name of the product. |
| Action | The SDDSN server needs to have an updated installation of the resource files that are shipped with the product (%3). If %3
                                       indicates 'Unknown', contact the technical assistance center to get a correlation between %1 and the actual product name.
                                       Install the updated support files for that product on the SDDSN server and restart it. This update will contain files named
                                       MSGSn.DLL and CATn.DLL where the 'n' should be replaced with the number %1 from this error message (e.g. MSGS2.DLL, CAT2.DLL,
                                       etc.). |
| 12A4010 | Message | The client system: %3, attempted to send an incompatible version: %1, SDDSN event. The current version supported is: %2. |
| Severity | Error |
| Type | Single-State Raise |
| Description | An event has been received by a client system using an incompatible version of the SDDSN protocol. |
| Action | The client system needs to be configured to send the correct version of the SDDSN protocol, or the SDDSN server needs to
                                       be upgraded to support the desired version. |
| 118C002 | Message | %1%% of the available free space is used in database :%2. |
| Severity | Informational |
| Type | Single-State Raise |
| Description | %1%% of the available free space is used in %2 database. This is an indication of how full the database is. When this value
                                       gets too high, the Logger will begin deleting the oldest historical records from the database. |
| Action | Change the purge interval to save data for a shorter period of time. If this is not practical, add more disk space to the
                                       system and add disk devices to the database by using SQL Server Management Studio. |
| 118C00C | Message | %1%% of the available log space is used in database: %2. |
| Severity | Informational |
| Type | Single-State Raise |
| Description | %1%% of the available log space is used in the %2 database. |
| Action | No action is required. |
| 118C00F | Message | Begin automatic purge: %1%% of the available data space is used in database: %2. |
| Severity | Warning |
| Type | Raise |
| Description | The automatic purge is being run in order to keep the database from running out of space. The parameters for the daily purge
                                       need to be adjusted to match the database storage capacity. |
| Action | Contact the technical assistance center. |
| 118C010 | Message | Automatic purge complete: %1%% of the available data space is used in database: %2. |
| Severity | Warning |
| Type | Clear |
| Description | The automatic purge has been run in order to keep the database from running out of space. The parameters for the daily purge
                                       need to be adjusted to match the database storage capacity. |
| Action | No action is required. |
| 118C015 | Message | Connected to client: %1, on port: %2. |
| Severity | Informational |
| Type | Clear |
| Description | The Logger successfully connected to a client system. |
| Action | No action is required. |
| 118C017 | Message | Logger or HDS connection to client: %1, on port: %2, either went out of service or has been broken. |
| Severity | Informational |
| Type | Raise |
| Description | Logger or HDS on the specified TCP/IP connection and port number either went out of service or communication has been broken. |
| Action | The Historical Data Server (HDS) or the peer Logger (on the other side of the duplexed central controller) is no longer getting
                                       its historical feed from this Logger. This can occur due to networking outages, SQL issues on the Logger or HDS, or the Logger
                                       or the HDS may have been shut down or otherwise disabled. |
| 118C033 | Message | Cannot find routing client with network routing client: %1, on server: %2, in database: %3; unable to replicate data to customer:
                                       %4, on CICR instance: %5. |
| Severity | Warning |
| Type | Single-State Raise |
| Description | CICR replication must find a routing client in the database with a matching network routing client. Otherwise, it cannot
                                       translate the routing client ID foreign key in the dialed number or label properly. CICR replication is unable to complete
                                       the replication in this case. |
| Action | No action is required. |
| 118C034 | Message | Cannot find customer: %1, or instance: %2, on server: %3, in database: %4. Unable to replicate to customer: %1, on CICR instance:
                                       %2. |
| Severity | Warning |
| Type | Single-State Raise |
| Description | CICR replication must find a customer and instance in the database with matching names. Otherwise, it cannot translate the
                                       customer definition ID foreign key in the dialed number or label properly. CICR replication is unable to complete the replication
                                       in this case. |
| Action | No action is required. |
| 118C035 | Message | Dialed number or label exists with duplicate key on server: %1, in database %2; unable to replicate to customer: %3. on CICR
                                       Instance %4 |
| Severity | Warning |
| Type | Single-State Raise |
| Description | CICR replication has found that inserting the dialed number or label would cause a duplicate key error. Therefore, the dialed
                                       number or label cannot be inserted. CICR replication is unable to complete the replication in this case. |
| Action | No action is required. |
| 118C036 | Message | Duplicate key exists for dialed number with enterprise name: %1. |
| Severity | Warning |
| Type | Single-State Raise |
| Description | CICR replication has found that a dialed number already exists with this enterprise name. Therefore, it cannot insert the
                                       new dialed number. CICR replication is unable to complete the replication in this case. |
| Action | No action is required. |
| 118C037 | Message | Duplicate key exists for dialed number with routing client ID: %1, and dialed number string: %2. |
| Severity | Warning |
| Type | Single-State Raise |
| Description | CICR replication has found that a dialed number already exists with this routing client ID and dialed number string. Therefore,
                                       it cannot insert the new dialed number. CICR replication is unable to complete the replication in this case. |
| Action | No action is required. |
| 118C038 | Message | Duplicate key exists for label with routing client ID: %1, and label string: %2. |
| Severity | Warning |
| Type | Single-State Raise |
| Description | CICR replication has found that a label already exists with this routing client ID and label string. Therefore, it cannot
                                       insert the new label. CICR replication is unable to complete the replication in this case. |
| Action | No action is required. |
| 118C039 | Message | CICR replication on side%1 is now active. |
| Severity | Informational |
| Type | Clear |
| Description | The CICR replication process is active. |
| Action | No action is required. |
| 118C03A | Message | CICR replication on side%1 is now inactive. |
| Severity | Informational |
| Type | Raise |
| Description | The CICR replication process is inactive. |
| Action | No action is required. |
| 118C03D | Message | Invalid host name is configured for customer: %1. Use the Configure ICM tool to re-configure the host name for customer: %1. |
| Severity | Error |
| Type | Single-State Raise |
| Description | Invalid host name has been configured for the customer. |
| Action | Use the ConfigICR-@gt;ICR_NODE to change the host name or system name and re-start the CICR replication process. |
| 118C03E | Message | CICR replication failed to update CICR instance: %1, due to commit update CC transaction failure. Unable to rReplicate to
                                       customer: %1. Check and correct the errors. |
| Severity | Warning |
| Type | Single-State Raise |
| Description | CICR replication failed to update the configuration change due to the error caused by the "commit update CC transaction"
                                       failure. |
| Action | No action is required. |
| 118C040 | Message | Found %1 records with date/time greater than current central controller time: %2 in table: %3. Check and correct the errors. |
| Severity | Warning |
| Type | Single-State Raise |
| Description | Found historical records with date/time greater than current central controller time. Delete the records which have date
                                       time greater than the current central controller time. |
| Action | No action is required. |
| 118C048 | Message | NICR replication on side%1 is now inactive. |
| Severity | Informational |
| Type | Raise |
| Description | The NICR replication process is inactive. |
| Action | No action is required. |
| 118C049 | Message | NICR replication on side%1 is now active. |
| Severity | Informational |
| Type | Clear |
| Description | The NICR replication process is active. |
| Action | No action is required. |
| 118C051 | Message | Invalid host name: %1, is configured for primary distributor for customer: %2. Use the Configure ICM tool to re-configure
                                       the primary distributor for customer: %2. |
| Severity | Error |
| Type | Single-State Raise |
| Description | Invalid primary distributor has been configured for the customer, or the system is unable to resolve the hostname for the
                                       named primary distributor for some reason. |
| Action | Use the ConfigICR-@gt;ICR_NODE to change the host name or system name and re-start the CICR replication process. Alternatively,
                                       check name resolution for the specified host name. |

| Message ID (hex) | Property | Value |
|---|---|---|
| 108C020 | Message | The Enterprise CTI Server associated with this Peripheral Gateway is on-line on: %1. |
| Severity | Informational |
| Type | Clear |
| Description | The Enterprise CTI server associated with this Peripheral Gateway is on-line. Enterprise CTI Client applications are able
                                       to connect to the server and exchange call and agent data. |
| Action | No action is required. |
| 108C021 | Message | The Enterprise CTI server associated with this Peripheral Gateway is down. |
| Severity | Error |
| Type | Raise |
| Description | The Enterprise CTI server associated with this Peripheral Gateway is off-line. Enterprise CTI client applications are not
                                       able to connect to the server and exchange call and agent data. |
| Action | Review the CTI server events and logs. |
| 108C02B | Message | OPC has detected that it is no longer synchronized with its partner. |
| Severity | Error |
| Type | Single-State Raise |
| Description | OPC has detected that it is no longer synchronized with its partner. |
| Action | No action is required. |
| 1088085 | Message | PG has failed activation request for %1 consecutive times. |
| Severity | Error |
| Type | Single-State Raise |
| Description | PG has failed activation and will be restarted. Note This SNMP Notification is supported with UCCE 12.6(2) if CCE 12.5(2) ES 23 is installed. | Note | This SNMP Notification is supported with UCCE 12.6(2) if CCE 12.5(2) ES 23 is installed. |
| Note | This SNMP Notification is supported with UCCE 12.6(2) if CCE 12.5(2) ES 23 is installed. |
| Action | No action is required. |
| 13E0002 | Message | Message Integration Service was unable to connect to: %1%2, on: %3, TCP/IP port: %4. |
| Severity | Error |
| Type | Raise |
| Description | Message Integration Service (MIS) was unable to connect to the indicated component and address. |
| Action | Confirm component is available, configuration of IP address(es) and port(s) are correct, and network connectivity would allow
                                       for connection. |
| 13E0003 | Message | Connection to: %1%2, address: %3:%4, succeeded. |
| Severity | Informational |
| Type | Clear |
| Description | Message Integration Service (MIS) was able to connect to the indicated component and address. |
| Action | No action is required. |
| 13E0004 | Message | Message Integration Service was unable to open a session to: %1%2. |
| Severity | Error |
| Type | Raise |
| Description | Message Integration Service (MIS) was unable to open a session to the indicated component. |
| Action | No action is required. |
| 13E0005 | Message | Session to: %1%2, opened. |
| Severity | Informational |
| Type | Clear |
| Description | Message Integration Service (MIS) was able to open a session to the indicated component and address. |
| Action | No action is required. |
| 13E0006 | Message | Trunk group: %1, trunk: %2; received in message from VRU-%3; not configured. |
| Severity | Error |
| Type | Single-State Raise |
| Description | A message pertaining to the indicated trunk group and trunk has not been configured with MIS. |
| Action | Configure extension, trunk group, and trunk in MIS. |
| 13E0007 | Message | Call tracking error: %1. |
| Severity | Error |
| Type | Single-State Raise |
| Description | A call within MIS could not be tracked successfully. |
| Action | Determine where tracking problem occurred and correct (for MIS problem, it could be MIS, VRU, or PG). |
| 1540002 | Message | An error occurred on the TCP/IP connection between the ACMI ACD server (CTI) and the ACMI peripheral gateway. ACMI peripheral
                                       gateway is offline. |
| Severity | Error |
| Type | Raise |
| Description | An error occurred on the connection between the ACMI ACD server (CTI) and the ACMI peripheral gateway. ACMI peripheral gateway
                                       is offline. |
| Action | If ACMI peripheral gateway does not re-attach, contact the technical assistance center. |
| 1540003 | Message | Peripheral status was DOWN, going NORMAL. ACMI peripheral gateway is online. |
| Severity | Informational |
| Type | Clear |
| Description | Peripheral status was DOWN, going NORMAL. ACMI peripheral gateway is online. |
| Action | No action is required. |
| 1540007 | Message | The route register on the DN: %1, is operational. |
| Severity | Informational |
| Type | Clear |
| Description | The DN is operational. |
| Action | No action is required. |
| 1540008 | Message | The route register failed for DN: %1. |
| Severity | Error |
| Type | Raise |
| Description | The Permit Application Routing box on the child system is not checked for DN. |
| Action | Check Permit Application Routing box. |
| 1540009 | Message | The route register failed for DN: %1. |
| Severity | Error |
| Type | Raise |
| Description | You have configured a DN or DN for a translation route on the parent that doesn't exist on the child system. Don't forget
                                       to check 'Permit Application Routing' when adding it. |
| Action | Add the DN on the child system and ensure that 'Permit Application Routing' is enabled. |
| 154000A | Message | The route register failed for DN: %1. |
| Severity | Error |
| Type | Raise |
| Description | You have configured a DN or DN for a translation route on the parent that doesn't exist on the child system. Don't forget
                                       to check 'Permit Application Routing' when adding it. |
| Action | Add the DN on the child system and ensure that 'Permit Application Routing' is enabled. |
| 154000B | Message | The route register failed for DN: %1. |
| Severity | Error |
| Type | Single-State Raise |
| Description | You have specified an incorrect server peripheral ID in the PG Setup of the Gateway PG. |
| Action | Correct the server peripheral ID in the PG Setup of the Gateway PG and restart the PG. |
| 154000C | Message | The route register failed for DN: %1. |
| Severity | Error |
| Type | Single-State Raise |
| Description | Another Gateway PG has requested control of this DN. This is most like likely due to an incorrect server hostname being configured. |
| Action | Correct the server host name in the PG Setup of the Gateway PG and restart the PG. |
| 154000D | Message | The peripheral ID: %1 given, is not valid. |
| Severity | Error |
| Type | Single-State Raise |
| Description | You have specified an incorrect server peripheral ID in the PG Setup of the Gateway PG. |
| Action | Correct the server peripheral ID in the PG Setup of the Gateway PG and restart the PG. |
| 154000E | Message | Central controller connection on child down - ACMI peripheral gateway status DOWN. |
| Severity | Error |
| Type | Raise |
| Description | Central controller connection on child down - ACMI peripheral gateway status DOWN. |
| Action | No action is required. |

| Note | This SNMP Notification is supported with UCCE 12.6(2) if CCE 12.5(2) ES 23 is installed. |
|---|---|

| Message ID (hex) | Property | Value |
|---|---|---|
| 12E8006 | Message | CONNECTION MONITOR SERVICE: Enterprise CTI session established by client: %1 (%2) at: %3. |
| Severity | Informational |
| Type | Clear |
| Description | An Enterprise CTI session has been opened by client ID %1 (signature %2) from IP address %3. |
| Action | No action is required. |
| 12E8007 | Message | CONNECTION MONITOR SERVICE: Enterprise CTI session closed by client: %1 (%2) at: %3. |
| Severity | Warning |
| Type | Raise |
| Description | The Enterprise CTI session with client ID %1 (signature %2) at IP address %3 has been closed by the client. |
| Action | This indicates that an Enterprise CTI client application that is generally always connected to the Enterprise CTI Server
                                       has closed its connection. The CTI client application software may need to be checked for proper operation. |
| 12E8008 | Message | CONNECTION MONITOR SERVICE: Enterprise CTI session terminated with client: %1 (%2) at: %3. |
| Severity | Error |
| Type | Raise |
| Description | The Enterprise CTI session with client ID %1 (signature %2) at IP address %3 has been terminated by the Enterprise CTI Server. |
| Action | This indicates that an Enterprise CTI Client application that is generally always connected to the Enterprise CTI Server
                                       has been disconnected due to errors. If the problem persists, the CTI client application software may need to be checked for
                                       proper operation. |
| 12E800C | Message | Client: %1, object: %2, normal event report: %3. |
| Severity | Informational |
| Type | Clear |
| Description | The Enterprise CTI client %1 application software has reported the following normal event for object %2: %3. |
| Action | No action is required. |
| 12E800D | Message | Client: %1, object: %2, warning event report: %3. |
| Severity | Warning |
| Type | Raise |
| Description | The Enterprise CTI client %1 application software has reported the following warning for object %2: %3. |
| Action | This indicates that the CTI client application software has detected a possible error or other abnormal condition and may
                                       need to be checked for proper operation. |
| 12E800E | Message | Client: %1, object: %2, error event report: %3. |
| Severity | Error |
| Type | Raise |
| Description | The Enterprise CTI client %1 application software has reported the following error for object %2: %3. |
| Action | This indicates that the CTI client application software has detected an error condition and may need to be checked for proper
                                       operation. |
| 12E800F | Message | A version 13 or prior CTI client ID: %1 (%2) at: %3, connected with agent multi line enabled. |
| Severity | Warning |
| Type | Raise |
| Description | A CTI client: %1 (signature: %2) from IP address: %3 with a version prior to 14 has connected to CTI Server that supports
                                       multi-line phones. Problems may be encountered with that application depending upon what messages/devices, etc. it processes
                                       events for. |
| Action | Check with the vendor of the software and see if they have ensured compatibility. |
| 12E8010 | Message | A version 13 or prior CTI client ID: %1 (%2) at: %3, disconnected with agent multi line enabled. |
| Severity | Warning |
| Type | Clear |
| Description | A CTI client %1 (signature %2) from IP address %3 with a version prior to 14 has connected to CTI Server that supports multi-line
                                       phones. Problems may be encountered with that application depending upon what messages/devices, etc. it processes events for. |
| Action | Check with the vendor of the software and see if they have ensured compatibility. |
| 12EC00E | Message | CTI Server was unable to forward ECC variables due to an overflow condition. |
| Severity | Warning |
| Type | Single-State Raise |
| Description | CTI Server found too much data in ECC variables while processing messages. ECC Variables will not be forwarded for there
                                       messages. |
| Action | This indicates that too many / too large ECC variables are configured in the system. Eliminate some ECC variables or reduce
                                       the size of existing ECC variables to alleviate this condition. |
| 1560004 | Message | CTI OS Server version: %2, is online. Connected to CTI Server at: %3. CTI Server protocol is: %1. |
| Severity | Informational |
| Type | Clear |
| Description | Message indicating the version of CTI OS Server as well as the protocol version CTI OS Server uses to connect to CTI Server. |
| 1560005 | Message | CTI OS Server version: %2, cycled because the connection to CTI Server at: %3, closed. CTI Server protocol is: %1. |
| Severity | Warning |
| Type | Raise |
| Description | CTI OS Server has cycled itself because its connection to CTI Server closed. When CTI OS Server restarts, it will re-establish
                                       its connection to CTI Server. |
| 1560006 | Message | CTI OS Server version: %2, cycled because the connection to CTI Server at: %3, failed. CTI Server protocol is: %1. |
| Severity | Error |
| Type | Raise |
| Description | CTI OS Server has cycled itself because its connection to CTI Server failed. When CTI OS Server restarts, it will re-establish
                                       its connection to CTI Server. |
| 1560007 | Message | CTI OS Server has %1 messages in queue. |
| Severity | Informational |
| Type | Clear |
| Description | The CTI OS Server incoming message is now below 10,000 messages. |
| 1560008 | Message | CTI OS Server has %1 messages in queue. |
| Severity | Warning |
| Type | Raise |
| Description | The CTI OS Server incoming message queue exceeded 10,000 messages. This might result in unwanted behavior. |
| 1560009 | Message | CTI OS Server has generated an exception in: %2, processing %3. Details: %4: %1 %5. |
| Severity | Error |
| Type | Single-State Raise |
| Description | CTI OS Server generated an exception while processing a request or an event specified in this method. |
| 156000A | Message | CTI OS Server has generated an exception in: %2, processing %3. Details: %4: %1 %5. |
| Severity | Error |
| Type | Single-State Raise |
| Description | CTI OS Server generated an exception while processing the request or event specified in this method. |
| 156000B | Message | CTI OS Server's total amount of agent mode connections is: %1. This is within CTI OS Server's limit of: %2. |
| Severity | Informational |
| Type | Clear |
| Description | CTI OS Server is current running with an acceptable number of agents connected to it. |
| 156000C | Message | CTI OS Server's total amount of agent mode connections is: %1. This exceeds CTI OS Server's limit of: %2. |
| Severity | Warning |
| Type | Raise |
| Description | CTI OS Server is currently running with an excessive number of agents connected to it. |
| 156000D | Message | CTI OS Server's total amount of monitor mode connections is: %1. This is within CTI OS Server's limit of: %2. |
| Severity | Informational |
| Type | Clear |
| Description | CTI OS Server is current running with an acceptable number of monitor-mode applications connected to it. |
| 156000E | Message | CTI OS Server's total amount of monitor mode connections is: %1. This exceeds CTI OS Server's limit of: %2. |
| Severity | Warning |
| Type | Raise |
| Description | CTI OS Server is currently running with an excessive number of monitor-mode applications connected to it. |
| 156000F | Message | CTI OS Server's monitor mode functionality has been re-enabled. Monitor mode functionality was previously disabled after %1
                                       failed attempts to access monitor mode functionality. |
| Severity | Informational |
| Type | Clear |
| Description | CTI OS Server has re-enabled monitor mode functionality. |
| 1560010 | Message | CTI OS Server's monitor mode functionality has been disabled after %1 failed attempts to access monitor mode functionality. |
| Severity | Warning |
| Type | Raise |
| Description | CTI OS Server has disabled access to monitor mode functionality because an excessive number of consecutive failed attempts
                                       to access monitor mode functionality have occurred. An attempt to access monitor mode functionality fails when the CTI OS
                                       monitor mode password is incorrectly specified. |
| 1560011 | Message | After the CTI OS Server version %2 re-established the connection to CTI Server at: %3, configuration change was detected.
                                       The CTI OS Server will restart. CTI Server protocol is: %1. |
| Severity | Warning |
| Type | Raise |
| Description | Upon re-establishment of the CTI Server Link, CTI OS Server detected a configuration change. CTI OS Server will restart to
                                       insure proper configuration. |
| 1560012 | Message | The CTI OS Server version %2 connection to CTI Server at: %3 has closed. The CTI OS Server will attempt to re-establish the
                                       connection. CTI Server protocol is: %1. |
| Severity | Warning |
| Type | Raise |
| Description | CTI OS Server's connection to the CTI Server has closed. CTI OS Server will attempt to re-establish the connection to the
                                       CTI Server. If Unsuccessful, CTI OS Server will restart. |
| 1560013 | Message | CTI OS Server is within the supported limit for: %1 %2. %3. |
| Severity | Informational |
| Type | Clear |
| Description | CTI OS Server is within the supported operational limit for this configuration/action. |
| 1560014 | Message | CTI OS Server is within the supported limit for %1 %2 has been exceeded. %3. |
| Severity | Warning |
| Type | Raise |
| Description | The CTI OS Server is within the supported operational limit has been exceeded |

| Message ID (decimal) | Property | Value |
|---|---|---|
| 107 | Message | [server_address=%s]: Connection Terminated to ActiveMQ |
| Severity | Informational |
| Type | Raise |
| Description | Informs JMS publisher connection to ActiveMQ service is down.  JMS publisher terminated/stopped. |
| Action | Ordinarily, no action required. However, if connection to JMS (ActiverMQ service) is down for extended periods of time, then, verify if ActiveMQ service status
                                       and evaluate overall system health, i.e., verify services are up, disk partitions have free space, system is not CPU starved,
                                       not swapping, not I/O bound, etc. |
| 108 | Message | [server_address=%s]: Connection Established to ActiveMQ |
| Severity | Informational |
| Type | Clear |
| Description | Informs JMS publisher connection to ActiveMQ service is up. JMS publisher started, or, if connection lost, connection established. |
| Action | No action required. Note, however, that if JMS connection is bouncing often, then, this could be an indication of a system-wide issue, so evaluate
                                       overall system health, i.e., verify services are up, disk partitions have free space, system is not CPU starved, not swapping,
                                       not I/O bound, etc. |
| 301 | Message | [message_error=%s]: Error initializing JMX MBean |
| Severity | Error |
| Type | Raise |
| Description | Failure during creation of JMX bean for TIP statistical reporting, which can be linked to JMX services failure to initialize,
                                       lack of system resources, or incorrect configuration of JMX host/port. |
| Action | Verify overall system health, i.e., services are up, disk partitions have free space, system is not CPU starved, not swapping,
                                       not I/O bound, etc. Attempt system restart, if problem persists, contact tech. support. |
| 303 | Message | [jmx_bean_name=%s]: JMX MBean registration failed |
| Severity | Error |
| Type | Raise |
| Description | Failure during establishment of JMX bean for event spout (PG, Router, etc) operations. This means no operations to/from spouts
                                       will be possible via JMX. |
| Action | Attempt system restart, if problem persists, contact tech. support. |
| 304 | Message | [jmx_bean_name=%s]: JMX MBean registration succeeded |
| Severity | Error |
| Type | Clear |
| Description | Success in establishing JMX bean for event spout (PG, Router, etc) operations. |
| Action | No action required. |
| 405 | Message | [connection_usage=%s][server_address=%s][state=%s][message_error=%s]: Connection error |
| Severity | Warning |
| Type | Raise |
| Description | Error during attempt to communicate (or establish connection) to CCE server (PG, Router, etc).  This can be caused by: Destination host/port not accepting connections. Too many messages (from server) pending processing by Live Data. Write to closed (by far-end) connection. |
| Action | As follows: Verify CCE server host/port configuration is correct, and port is open on host fire-wall. Verify CPU availability to Live Data. If problem persists contact tech. support. No action required for attempt to write to closed (by far-end) connection. |
| 407 | Message | [server_address=%s][tip_missed_heartbeats=%d]:	Heatbeat Missed on TIP connection |
| Severity | Warning |
| Type | Clear |
| Description | Missed one heartbeat to CCE server is not uncommon, and it is typically linked to a busy system. Live Data uses heartbeat
                                       to track the health of a CCE connection, and if too many (configurable) heartbeats are lost it will close and (attempt) to
                                       re-open the connection. |
| Action | No action required. |
| 501 | Message | [properties=%s]: TIP Controller Stopped |
| Severity | Critical |
| Type | Raise |
| Description | Indicates spout communication controller, responsible for CCE message processing, has terminated/stopped. This can happen
                                       on following scenarios: Failover to standby cluster node. JMX reset connection request. System shutdown. |
| Action | On failover: determine failover root cause and correct it. Start with overall system health, i.e., services are up, disk partitions
                                       have free space, system is not CPU starved, not swapping, not I/O bound, etc. If no reason is found, or reason cannot be corrected,
                                       contact tech. support. For all the other reasons: no action required. |
| 502 | Message | [tip_client_seggrp=%s][tip_client_app_seqnum=%s][properties=%s]: TIP Controller Started |
| Severity | Critical |
| Type | Clear |
| Description | Indicates spout communication controller, responsible for CCE message processing, has started. |
| Action | No action required. |
| 503 | Message | [server_address=%s][message_error=%s]: Error in TIP Controller Processes |
| Severity | Error |
| Type | Raise |
| Description | Indicates protocol error due to: Request/response timeout Unrecognized message format Failure in message decoding Failure in message processing |
| Action | Protocol request/response timeouts are not uncommon and are typically linked to communication failure due to far-end port
                                       disconnect (i.e., attempt to write to a closed socket). For all other failures, contact tech. support. |
| 505 | Message | [message_error=Connection-%s]: Invalid TIP Configuration for |
| Severity | Error |
| Type | Raise |
| Description | Configuration to CCE server is incomplete, or invalid. Port is not numeric in range 1-65565, host name contains invalid characters,
                                       etc. |
| Action | Verify Live Data configuration and restart system. |
| 507 | Message | [server_address=%s][tip_client_seqgrp=%s][tip_server_seqgrp=%s]: TIP Sequence Group Mismatch |
| Severity | Error |
| Type | Raise |
| Description | Indicates data loss during last CCE connection switch-over. PG/Router unavailable simultaneous to a communication loss to
                                       PG/Router corresponding side (A or B). |
| Action | No action required. The system will issue a new sequence group, and request a snapshot to re-synch its internal state with that of the failed
                                       component. |
| 509 | Message | [server_address=%s][tip_client_seqgrp=%s][tip_server_seqgrp=%s]: TIP Message Gap between client and server |
| Severity | Error |
| Type | Raise |
| Description | Indicates data loss during last CCE communication. PG/Router crash simultaneous to a communication loss to PG/Router corresponding
                                       side (A or B). |
| Action | No action required. The system will request a snapshot to re-synch its internal state with that of the failed component. |
| 511 | Message | [server_address=%s]: TIP Controller switching Active Side |
| Severity | Warning |
| Type | Raise |
| Description | Indicates spout communication controller has detected an active connection (to CCE server) is down, and that the standby connection
                                       to configured PG/Router will become active (switch-over). The PG/Router communication was severed, or the CCE server is no
                                       longer running. |
| Action | Verify CCE server (PG, Router, etc) health. |
| 512 | Message | [server_address=%s][tip_client_seqgrp=%s][tip_server_seqgrp=%s]: TIP Message Synchronization Successful with TIP Server |
| Severity | Error |
| Type | Clear |
| Description | Indicates that during a switch-over (from active connection to standby) the sequence number received by standby is in ascending
                                       order, and that it can be released from CCE server side. PG/Router unavailable, but Live Data state is not affected by it. |
| Action | No action required. |
| 515 | Message | [server_address=%s][operation_type=%s]: TIP Protocol Request Failure |
| Severity | Warning |
| Type | Raise |
| Description | Request to CCE server has failed, or timed out. |
| Action | No action required. |
| 517 | Message | [server_address=%s][message_error=%s][operation_type=%s]: TIP Protocol Errors |
| Severity | Error |
| Type | Raise |
| Description | Protocol error during response processing (of a request to CCE server) due to response to an invalid, or inexistent, pending
                                       request id. This can be linked to an expired request, as well as, an inexistent request. |
| Action | No action required. |
| 521 | Message | [server_address=%s][message_error=%s]: TIP Heartbeat Failure |
| Severity | Error |
| Type | Raise |
| Description | Reached allowed number of heartbeat losses to CCE server. This will disconnect all CCE servers (PG, Router, etc) associated
                                       with a given CCE side (A or B). A switch over to other CCE server side (A or B) will be automatically initiated. |
| Action | Determine network integrity between Live Data and CCE servers on failed side (A or B). Determine if CCE server (PG, Router,
                                       etc) is up and running. |
| 523 | Message | [server_address=%s][message_error=%s]: Error in TOS Client |
| Severity | Error |
| Type | Raise |
| Description | Indicates TOS (related to Live Data Cluster node state) protocol error. Possible error causes are: Failure to start TOS communication Failure during write to TOS far-end server |
| Action | Verify Live Data configuration, restart system. |
| 601 | Message | [server_address=%s][message_error=%s]: Warning in TOS Client" |
| Severity | Warning |
| Type | Raise |
| Description | Unable to send message to assess Live Data Cluster state on far end. Triggered by failure to receive cluster node state via
                                       JMS (ActiveMQ/Netbridge in this case), which can be caused by cluster node crash, network failure, ActiveMQ crash, or Netbridge
                                       crash. |
| Action | Verify network integrity between Live Data cluster nodes. Verify ActiveMQ service is up, and cluster nodes configured for
                                       fail-over. |
| 603 | Message | [server_address=%s][message_error=%s]: TOS REQUEST RESPONSE latency alert. |
| Severity | Warning |
| Type | Raise |
| Description | Request/response round trip time to cluster nodes is greater than configured seconds. This can be linked to network latency,
                                       or sluggish response from cluster node far end. |
| Action | Verify network integrity between Live Data clusters nodes. Verify overall system health on all Live Data cluster nodes. |
| 607 | Message | [server_address=%s][missed_heartbeats]: Heatbeat Missed on TOS connection |
| Severity | Warning |
| Type | Raise |
| Description | Missed one heartbeat to CCE server is not uncommon, and it is typically linked to a busy system. Live Data uses heartbeat
                                       to track the health of a CCE connection, and if too many (configurable) heartbeats are lost it will close and (attempt) to
                                       re-open the connection. |
| Action | Verify network integrity between CCE server and Live Data. |
| 609 | Message | [server_address=%s][message_error=%s]: TOS Heartbeat Failure |
| Severity | Error |
| Type | Raise |
| Description | Reached allowed number of heartbeat losses to CCE server (PG, Router, etc). This will cause a disconnection followed by reconnection
                                       to CCE servers (PG, Router, etc). |
| Action | Verify network integrity from CCE server (PG, Router, etc) to Live Data. Verify CCE server (PG, Router, etc) is up and running. |
| 703 | Message | [operation_error_desc=%s]: Camel Service Error |
| Severity | Error |
| Type | Raise |
| Description | Failed to open connection to JMS (ActiveMQ) or to publish to indicated topic.   Configuration to JMS (ActiveMQ) is incorrect,
                                       or service is down. |
| Action | Verify Live Data configuration. Assess overall system health, i.e., services are up, disk partitions have free space, system
                                       is not CPU starved, not swapping, not I/O bound, etc. Note that, in case of ActiveMQ service down, the Live Data cluster will fail-over to standby node. |
| 801 | Message | [server_id=%s]: Spout failed to load UCCE Configuration |
| Severity | Error |
| Type | Raise |
| Description | Error during load of Live Data configuration from AWDB. Dataset name pointing to AWDB, incorrectly configured in CUIC. location. |
| Action | Using CUIC interface assure data set name for CUIC is correctly configured with address to AWDB. Ensure AWDB system is up
                                       and running. If problem persists, contact tech. support. |
| 802 | Message | [server_id=%s]: Spout loaded UCCE Configuration |
| Severity | Informational |
| Type | Clear |
| Description | Live Data configuration, from AWDB, loaded to local memory. |
| Action | No action required. |
| 805 | Message | [message_error=%s]: JMS Command Spout failed to Initialize |
| Severity | Error |
| Type | Raise |
| Description | JMS command spout failed to initialize. Scenario JMS (ActiveMQ) communication was not possible via Camel, and an exception
                                       was thrown. |
| Action | Verify Live Data configuration, and restart system. If problem persists, contact tech. support. |
| 807 | Message | [message_error=%s]: JMS Command Spout failed to Close |
| Severity | Error |
| Type | Raise |
| Description | JMS command spout failed to close JMS connection. |
| Action | No action required. |
| 809 | Message | [server_id=%s][tip_client_app_seqnum=%d][tip_server_app_seqnum=%d]: Invalid Application Sequence Number Received |
| Severity | Error |
| Type | Raise |
| Description | During communication with CCE server, message sequence number was not in increasing order, and/or presented a gap. Possible
                                       data loss. |
| Action | Gather logs and contact tech. support. |
| 813 | Message | [server_id=%s][message_error=%s]: Spout runtime error |
| Severity | Error |
| Type | Raise |
| Description | Indicates event spout runtime error: Zookeeper connection object could not instantiate or connect. Establishment of JMS command queue listener failed. JMX configuration could not be written to Zookeeper. |
| Action | Verify Zookeeper service is up and running, and restart system. If problem persists, contact tech. support. |
| 815 | Message | [server_id=%s]: Spout lost connection to Zookeeper |
| Severity | Error |
| Type | Raise |
| Description | Connection to Zookeeper was severed, which might be linked to a Zookeeper down/terminated. Note that a Zookeeper disconnection
                                       will cause a Live Data cluster failover. |
| Action | Zookeeper is central to Storm and, as such, to Live Data; verify service is up and running. If disconnections are frequent,
                                       contact tech. support. |
| 816 | Message | [server_id=%s]: Spout Connected Successfully to Zookeeper |
| Severity | Informational |
| Type | Clear |
| Description | Connection to Zookeeper established. |
| Action | No action required. |
| 819 | Message | [server_id=%s]: Spout deactivated |
| Severity | Critical |
| Type | Raise |
| Description | Event spout is deactivated due to a Live Data Cluster failover. One of the central components to Live Data is down. Central
                                       components are: Zookeeper, ActiveMQ, and (pairs of) CCE servers (PG/Router). |
| Action | Verify overall system health, i.e., services are up, disk partitions have free space, system is not CPU starved, not swapping,
                                       not I/O bound, etc. Verify network to PGs and Routers are healthy. Verify PGs and Routers are up and running. If problem persists,
                                       contact tech. support. |
| 820 | Message | [server_id=%s]: Spout activated |
| Severity | Critical |
| Type | Clear |
| Description | Event spout transitioned to active state due to startup, or Live Data Cluster failover. |
| Action | No action required. |
| 902 | Message | [server_id=%s][value=%s]: Spout UCCE Configuration - Deployment Type Modified |
| Severity | Informational |
| Type | Clear |
| Description | Deployment type change from UCCE to PCCE, or vice-versa. This WILL impact the feature set available in Live Data, and require
                                       environment reconfiguration. The expectation is, in fact, that environment adjustments (to/from UCCE to PCCE), took place
                                       before changing deployment type. |
| Action | No action required. |
| 905 | Message | [server_id=%s][value=%s]: Spout UCCE Configuration - Spout end point configuration error |
| Severity | Error |
| Type | Raise |
| Description | Indicates Live Data EndPoint configuration is present, but data is inconsistent (values missing from tables, incomplete data,
                                       etc.). |
| Action | Correct Live Data EndPoint Configuration. |
| 907 | Message | [server_id=%s][value=%s]: Spout UCCE Configuration - Spout TOS end point configuration error |
| Severity | Error |
| Type | Raise |
| Description | Live Data configuration is incomplete/incorrect and TOS protocol host/port is in error. |
| Action | Correct Live Data EndPoint Configuration. |
| 1401 | Message | [message_error=%s]: Error connecting to Zookeeper |
| Severity | Error |
| Type | Raise |
| Description | Zookeeper connection failure. Possibly Zookeeper service is down, or hung. This will cause Live Data to fail during startup,
                                       or to failover if already up. |
| Action | Verify overall system health, i.e., services are up, disk partitions have free space, system is not CPU starved, not swapping,
                                       not I/O bound, etc. If problem persists, contact tech. support. |
| 1403 | Message | [message_error=%s]: Error communicating with Zookeeper |
| Severity | Error |
| Type | Raise |
| Description | Attempt to write to, or read from, Zookeeper failed, but the error does not characterize Zookeeper to be down. The operation
                                       is attempted a few times before the error is reported, so it is very likely Zookeeper connection will be restarted in short
                                       order (which will trigger a Live Data Cluster failover). |
| Action | Verify overall system health, i.e., services are up, disk partitions have free space, system is not CPU starved, not swapping,
                                       not I/O bound, etc. If problem persists, contact tech. support. |
| 1011 | Message | [operation_error_desc=%s]: Zookeeper Connection Error |
| Severity | Error |
| Type | Raise |
| Description | Reports error/exception during attempt to connect or operate against Zookeeper instance. Depending on error, a failed connection
                                       to Zookeeeper is going to be declared, and Live Data Cluster failover will be triggered. |
| Action | Verify Zookeeper is up and running. Verify overall system health. If problem persists, contact tech. support. |
| 1014 | Message | [value=%s]: Cluster state update |
| Severity | Informational |
| Type | Clear |
| Description | Indicates Live Data Cluster state. |
| Action | No action required. |
| 1017 | Message | [message_error=%s]: Error in cluster operations |
| Severity | Error |
| Type | Raise |
| Description | Indicates failure during Cluster Peer spout initialization. Also informs failures during TOS request/response and cluster
                                       spout stop. |
| Action | Verify overall system health. Verify network integrity between Live Data and CCE servers (PG, Router, etc). Verify CCE servers
                                       (PG, Router, etc) are up and running. If problem persists, contact tech. support. |
| 1023 | Message | [operation_error_desc=%s]: Cluster Heartbeat subscriber start failed with cause |
| Severity | Warning |
| Type | Raise |
| Description | Cluster Peer Spout failed to initialize JMS (ActiveMQ) subscriber for exchanging of cluster node state, which means cluster
                                       failover will not be functional. This can only happen during system startup.  JMS (ActiveMQ) configuration is incorrect, or
                                       service is down. |
| Action | Verify Live Data configuration, verify ActiveMQ service is up and running, and check overall system health. If problem persists,
                                       contact tech. support. |
| 1024 | Message | Cluster Heartbeat Subscriber started successfully |
| Severity | Informational |
| Type | Clear |
| Description | Cluster Peer Spout successfully connected and subscribed to JMS (ActiveMQ) in order to exchange cluster node state. |
| Action | No action required. |
| 1025 | Message | [operation_error_desc=%s]: Cluster Publisher start failed with cause |
| Severity | Warning |
| Type | Raise |
| Description | Cluster Peer Spout failed to initialize JMS (ActiveMQ) publisher for exchanging of cluster node state, which means cluster
                                       failover will not be functional. This can only happen during system startup.  JMS (ActiveMQ) configuration is incorrect, or
                                       service is down. |
| Action | Verify Live Data configuration, verify ActiveMQ service is up and running, and check overall system health. If problem persists,
                                       contact tech. support. |
| 1026 | Message | Cluster Publisher started successfully |
| Severity | Informational |
| Type | Clear |
| Description | Cluster Peer Spout successfully connected and can publish to JMS (ActiveMQ) in order to exchange cluster node state. |
| Action | No action required. |
| 1101 | Message | [operation_error_desc=%s]: Cluster state machine encounters an error |
| Severity | Error |
| Type | Raise |
| Description | Cluster State Machine is in a state from which received event is invalid! |
| Action | Gather logs and contact tech. support. |
| 1107 | Message | Cluster state machine activates RTR/PG spouts |
| Severity | Informational |
| Type | Clear |
| Description | Indicates Cluster State Machine has satisfied all conditions to allow for event spouts to connect to CCE servers (PG, Router,
                                       etc). |
| Action | No action required. |
| 1109 | Message | Cluster state machine deactivates RTR/PG spouts |
| Severity | Critical |
| Type | Raise |
| Description | Indicates Cluster State Machine has detected a condition under which event spouts are not allowed to be connected to (or should
                                       disconnect from) CCE servers (PG, Router, etc). |
| Action | No action required. |
| 1201 | Message | [descr=%s]: ActiveMQ connection state down |
| Severity | Critical |
| Type | Raise |
| Description | Indicates ActiveMQ transitioned to down/disconnected state. This will trigger a cluster failover. |
| Action | Verify ActiveMQ service is up. Verify network integrity between cluster nodes. Verify overall system health. |
| 1202 | Message | [descr=%s]: ActiveMQ connection state up |
| Severity | Critical |
| Type | Clear |
| Description | Indicates ActiveMQ transitioned to up/connected state. |
| Action | No action required. |
| 1301 | Message | [descr=Side-%s]: NetBridge connection state down |
| Severity | Critical |
| Type | Raise |
| Description | Indicates ActiveMQ Netbridge transitioned to down/disconnected state. This might trigger a cluster failover depending on TOS
                                       request/response to far-end cluster node. |
| Action | Verify ActiveMQ service is up. Verify network integrity between cluster nodes. Verify overall system health. |
| 1302 | Message | [descr=Side-%s]: NetBridge connection state up |
| Severity | Critical |
| Type | Clear |
| Description | Indicates ActiveMQ Netbridge transitioned to up/connected state. |
| Action | No action required. |
| 20101 | Message | [db_object_type=%s][mesage_error=%s]: Error attempting operation with CCE Database |
| Severity | Error |
| Type | Raise |
| Description | Reports database (typically AWDB) runtime error, informing object attempting DB access, and description of failure cause,
                                       including SQL query (where appropriate). Failure during connection to AWDB tables to memory, failure to access Hibernate element,
                                       failure creating DBSession. |
| Action | Determine if AWDB is available, and verify Live Data configuration and CUIC, specifically where it pertains to AWDB connection
                                       information on datasource tab in CUIC. |
| 20103 | Message | [message_error=%s]: Error attempting to connect to CCE Database |
| Severity | Error |
| Type | Raise |
| Description | Reports database (typically AWDB) access error during retrieve/update elements, via Hiberate. Execute SQL query, retrieve
                                       column value. |
| Action | Determine if AWDB is available, and verify Live Data configuration and CUIC, specifically where it pertains to AWDB connection
                                       information on datasource tab in CUIC. |
| 20107 | Message | [message_error=%s]: Error attempting to read local address from CCE database for Cassandra connection |
| Severity | Error |
| Type | Raise |
| Description | Reports failure during retrieval of configuration element which would allow Live Data a connection to Cassandra DB. |
| Action | Verify Live Data configuration. |
| 20201 | Message | [db_ver_expected=%s][db_ver_read=%s]: CCE configuration database version mismatch |
| Severity | Error |
| Type | Raise |
| Description | Informs current version found in AWDB is not what Live Data expects to see. This indicates a schema mismatch. Live Data cannot
                                       proceed since no data from AWDB can be retrieved. This condition is detected during Live Data startup only. |
| Action | Gather logs, and contact tech. support. |
| 20304 | Message | Error creating Cassandra Database connection |
| Severity | Informational |
| Type | Raise |
| Description | Reports failure, and cause, during connection attempt to Cassandra DB. Reports Cassandra configuration values used for Cassandra
                                       connection. |
| Action | Verify Live Data configuration, and assure Cassandra DB is up and running. No action required. |
| 20305 | Message | [message_error=%s]: Error interacting with the Cassandra Connection Pool |
| Severity | Error |
| Type | Raise |
| Description | Reports failure during attempt to obtain connection, from Cassandra connection pool. Most likely connection pool is depleted
                                       and new connections to Cassandra DB are not possible. |
| Action | Ensure Cassandra DB is up. Verify in Live Data configuration points to Cassandra correctly, and that connection pool is large
                                       enough. |
| 20307 | Message | [message_error=%s]: Error interacting Cassandra database |
| Severity | Error |
| Type | Raise |
| Description | Reports failure during attempt to read/write to Cassandra DB, and, if available, a description of the problem. |
| Action | Ensure Cassandra DB is up, verify Live Data configuration points to Cassandra correctly. |
| 20309 | Message | Error reading AWDB Configuration from Cassandra |
| Severity | Error |
| Type | Raise |
| Description | Reports failure, and cause, while reading AWDB Config from Cassandra. |
| Action | Verify Live Data configuration, and ensure Cassandra DB is up and running, and AWDBConfig is present using cli "show live-data
                                       aw-access" |
| 20401 | Message | [message_error=%s]: Error trapped on expected exception |
| Severity | Error |
| Type | Raise |
| Description | Live Data trapped an exception to which it has no recourse other than report and proceed. |
| Action | Gather logs and contact tech. support. |
| 20402 | Message | [message_error=%s]: Exception on CCMDB Connection Pool |
| Severity | Error |
| Type | Raise |
| Description | Live Data exception while performing operation on CCM Database connection pool |
| Action | Gather logs and contact tech. support. |
| 10703 | Message | Tick handler caught a runtime exception |
| Severity | Error |
| Type | Clear |
| Description | The tick handler threw a runtime exception. Scenario Unknown. |
| Action | Contact tech. support. |
| 10705 | Message | interval processing threw an exception |
| Severity | Error |
| Type | Clear |
| Description | The interval processor threw an exception. Scenario Unknown. |
| Action | Contact tech. support. |

| Message ID (hex) | Property | Value |
|---|---|---|
| 1588001 | Message | TIP Server at: %2:%1, failed to start: %3. |
| Severity | Error |
| Type | Raise |
| Description | The TIP Server failed to start. If TIP services are not required, disable TIP in the registry. |
| Action | If TIP services are required, configure the proper TIP address/port and restart the node. If TIP services are not required,
                                       disable TIP in the registry. |
| 1588002 | Message | TIP Server is disabled. |
| Severity | Error |
| Type | Raise |
| Description | The TIP Server has been disabled. |
| Action | No action is required. |
| 1588003 | Message | TIP Server at: %2:%1, is waiting for client connection. |
| Severity | Warning |
| Type | Raise |
| Description | The TIP Server is waiting for client connections. |
| Action | If condition persists, ensure that the Live Data client is running, has connectivity, and the correct configuration information
                                       to contact this TIP Server. |
| 1588004 | Message | TIP Server at: %3:%1, accepted a connection from:%4:%2. |
| Severity | Warning |
| Type | Raise |
| Description | The TIP Server is waiting for client connections. |
| Action | No action is required. |
| 1588006 | Message | TIP Server at: %3:%1, client connection: %4:%2, failed: %5. |
| Severity | Warning |
| Type | Raise |
| Description | The TIP Server client connection has failed. |
| Action | No action is required. |
| 1588008 | Message | TIP Server at: %5:%1, is above warning memory threshold of: %2 MB. Queue will be maintained at: %4; events will be deleted
                                       until memory drops below: %3 MB. TIP event loss is possible. |
| Severity | Warning |
| Type | Raise |
| Description | The TIP Server has exceeded configured warning memory limits. The oldest TIP events are being deleted before acknowledgement
                                       is received, making event loss possible. |
| Action | If this condition persists, ensure that the Live Data client is running, has connectivity and correct configuration information
                                       to contact this TIP server. |
| 1588009 | Message | TIP Server at: %5:%1, is above critical memory threshold: %2 MB. The queue will be reduced from: %4; events will be deleted
                                       until memory drops below: %3 MB. TIP event loss is possible. |
| Severity | Error |
| Type | Raise |
| Description | The TIP Server has exceeded configured critical memory limits. The oldest TIP events are being deleted before acknowledgement
                                       is received, making event loss possible. |
| Action | If this condition persists, ensure that the Live Data client is running, has connectivity and correct configuration information
                                       to contact this TIP Server. |
| 158800A | Message | TIP Server at: %5:%1, is within memory and queue, size limits. Current: %4; events will be kept in queue. |
| Severity | Warning |
| Type | Raise |
| Description | The TIP Server is within configured memory limits. |
| Action | None |
| 158800B | Message | TIP Server at: %5:%1, has exceeded maximum: %4; events will be deleted until queue size is reduced. TIP event loss is possible. |
| Severity | Warning |
| Type | Raise |
| Description | The TIP Server has exceeded configured maximum queue size. The oldest TIP events are being deleted before acknowledgement
                                       is received, making event loss possible. |
| Action | If condition persists, ensure that the Live Data client is running, has connectivity and correct configuration information
                                       to contact this TIP Server. |
| 158800C | Message | TIP Server at: %5:%1, has exceeded warning memory threshold: %2 MB, but the queue is below minimum size: %3. The queue may
                                       grow at: %4; events will be kept in queue. |
| Severity | Warning |
| Type | Raise |
| Description | The TIP Server has exceeded configured warning memory limits, but has not met the TIP minimum queue size. No action will
                                       be taken, but the process may be unstable. |
| Action | Monitor process memory usage and take appropriate action if memory overflow is imminent. |
| 158800D | Message | TIP Server at: %5:%1, has exceeded critical memory threshold: %2 MB, but the queue is below minimum size: %3. The queue may
                                       grow at: %4; events will be kept in queue. |
| Severity | Error |
| Type | Raise |
| Description | The TIP Server has exceeded configured critical memory limits, but has not met the TIP minimum queue size. No action will
                                       be taken, but the process may be unstable. |
| Action | Monitor process memory usage and take appropriate action if memory overflow is imminent. |
| 158800E | Message | TIP Server at: %5:%1 has exceeded critical memory threshold: %2 MB; maintaining queue at minimum: %4; events will be deleted
                                       until memory drops below: %3 MB. TIP event loss is possible. |
| Severity | Error |
| Type | Raise |
| Description | The TIP Server has exceeded configured critical memory limits. The oldest TIP events are being deleted before acknowledgement
                                       is received, making event loss possible. |
| Action | Monitor process memory usage and take appropriate action if memory overflow is imminent. |
| 158800F | Message | TIP Server at: %5:%1, has exceeded critical memory threshold: %2 MB, and the queue is below minimum size: %3. The queue will
                                       be reduced from: %4. TIP event loss is possible. |
| Severity | Error |
| Type | Raise |
| Description | The TIP Server has exceeded configured critical memory limits, and has not met the TIP minimum queue size. TIP events will
                                       be deleted and events may be lost. The process may be unstable. |
| Action | Monitor process memory usage and take appropriate action if memory overflow is imminent. |

| Message ID (hex) | Property | Value |
|---|---|---|
| 1438000 | Message | Outbound Option Campaign Manager on: %1, is down. |
| Severity | Error |
| Type | Raise |
| Description | The Outbound Option Campaign Manager is not running. Dialer(s) will only run for a short period of time without a Campaign
                                       Manager. In addition, configuration messages will not be forwarded to Dialer(s) or the Import process. |
| Action | Make sure the Campaign Manager process is enabled in the registry. Also, check that the Outbound Option database server is
                                       running. The Outbound Option private database should have been created with the ICMDBA tool. |
| 1438001 | Message | Outbound Option Campaign Manager on: %1, is up. |
| Severity | Informational |
| Type | Clear |
| Description | Outbound Option Campaign Manager is ready to distribute customer records and configuration data. |
| Action | No action is required. |
| 1438002 | Message | Failed to execute import into table: %1, due to a change in the table's schema. |
| Severity | Error |
| Type | Single-State Raise |
| Description | The schema for a specified table has been changed but the overwrite option has not been enabled. This means that an existing
                                       database table does not match the configured import. |
| Action | Change the import to an overwrite import. This will drop the existing customer table and create a new table that will match
                                       the import. Please note that all existing customer data for that import will be lost. |
| 1438003 | Message | Import failed due to an invalid table: %1, definition. |
| Severity | Error |
| Type | Single-State Raise |
| Description | Could not create the specified table due to invalid import schema definition. |
| Action | Check that all table columns for the failed import are correct. Making a character column too long could cause this failure. |
| 1438004 | Message | Failed to import data into table: %1. |
| Severity | Error |
| Type | Single-State Raise |
| Description | This error could occur if the import file did not match the table definition. |
| Action | Check that the import table definition matches the import file. |
| 1438005 | Message | Failed to build dialing list from table: %1. |
| Severity | Error |
| Type | Single-State Raise |
| Description | A dialing list could not be populated from the specified table. |
| Action | Check if another process has the dialing list table locked. For example, if a report was running on the table while the dialing
                                       list was being generated. |
| 1438006 | Message | Could not open: %1 database. |
| Severity | Error |
| Type | Single-State Raise |
| Description | The Outbound Option private database has not been initialized or SQL Server is not running. |
| Action | Make sure that SQL Server is running. Check the ODBC configuration settings for the Outbound Option private database. Was
                                       the ICMDBA tool run to create the Outbound Option private database? |
| 1438007 | Message | An import was started but its configuration was deleted while it was running. |
| Severity | Error |
| Type | Single-State Raise |
| Description | An import started running but part of its configuration was deleted before it was able to do anything. |
| Action | Reschedule the import. |
| 1438008 | Message | Outbound Option CTI Server connection on host: %1 is down. |
| Severity | Error |
| Type | Raise |
| Description | The Outbound Option CTI Server connection has been terminated. |
| Action | Make sure CTI Server is active. Also make sure the PIM has connectivity to the switch. |
| 1438009 | Message | Outbound Option CTI Server connection on host: %1, is active. |
| Severity | Informational |
| Type | Clear |
| Description | Outbound Option CTI Server connection is active. |
| Action | No action is required. |
| 1438010 | Message | Dialer telephony port: %1, is not functioning correctly. |
| Severity | Error |
| Type | Raise |
| Description | A telephony error has occurred on a specific Dialer port. This may indicate a fault on the Dialogic telephony card, or the
                                       interface card on the switch. However, a more likely scenario is that a T1 line may have been disconnected or cut. |
| Action | Check that all wires going to the Dialer and the switch are intact. If port 0 failed, it means the first port on the first
                                       telephony card has received a failure message from the telephony driver. The first telephony card is the one that is assigned
                                       the lowest ID. The card's ID is assigned by a hardware switch on the top of the card. Ports are numbered consecutively across
                                       all ports. |
| 1438011 | Message | Outbound Option telephony port: %1, has recovered. |
| Severity | Informational |
| Type | Clear |
| Description | A previously malfunctioning telephony port has received a message from the telephony driver indicating the port is back in
                                       service. |
| Action | No action is required. |
| 1438012 | Message | BAImport is down on host: %1. |
| Severity | Error |
| Type | Raise |
| Description | BAImport is not running on the specified host. |
| Action | Please check that the import process has not been shut down. Check that the Outbound Option private database has been created.
                                       Also, ensure that SQL Server is running. |
| 1438013 | Message | BAImport is up on host: %1. |
| Severity | Informational |
| Type | Clear |
| Description | BAImport is running on the specified host. |
| Action | No action is required. |
| 1438014 | Message | Dialer is down on host: %1. |
| Severity | Error |
| Type | Raise |
| Description | Dialer is down on the specified host. |
| Action | Please check that the Dialogic drivers are configured and running. Also, verify that the Dialer has been started by Node
                                       Manager. |
| 1438015 | Message | Dialer is up on host: %1. |
| Severity | Informational |
| Type | Clear |
| Description | Dialer is up on the specified host. |
| Action | No action is required. |
| 1438018 | Message | Failed to rename or delete the import file for import rule ID: %1. This import rule has been temporarily disabled. |
| Severity | Error |
| Type | Single-State Raise |
| Description | Failed to rename or delete the import file for import rule Id: @lt;id; filename@gt;. This import rule has been temporarily
                                       disabled. To correct this condition, manually remove the import file and disable and re-enable the import rule using Import
                                       Configuration Component. |
| Action | File polling is enabled for this import rule. After the import, the BAImport process was unable to rename or delete the file.
                                       This import rule is temporarily disabled. Rename or delete the import file, disable and re-enable this import rule from the
                                       BAImport Configuration Component. |
| 1438019 | Message | Campaign: %1, trying to: %2; database timed out. |
| Severity | Error |
| Type | Single-State Raise |
| Description | Campaign [campaign name] tried to run a query [query name] and the database timed out. |
| Action | No action is required. |
| 1438020 | Message | Database is running out of space. |
| Severity | Error |
| Type | Single-State Raise |
| Description | Database is running out of space. |
| Action | Please create some space in the database. |
| 1438021 | Message | The agent skill group: %1, received is not the configured skill group: %2, for the campaign: %3. |
| Severity | Error |
| Type | Single-State Raise |
| Description | The agent skill group received is not configured for this campaign. |
| Action | Make sure the skill group configured in the script is the same as the skill group configured in the campaign. |
| 1438022 | Message | Timeout happening for the call on port: %1. Time to get the MR response: %2 seconds. |
| Severity | Warning |
| Type | Single-State Raise |
| Description | Timeout happening for the call on port. |
| Action | Timeout happening for a call on port. Check the registry key TimeToWaitForMRIResponse. |
| 1438023 | Message | Media Routing PIM disconnected with Dialer: %1. |
| Severity | Error |
| Type | Raise |
| Description | Media Routing PIM disconnected with the specified Dialer. |
| Action | Check if the MR PIM is active. |
| 1438024 | Message | MR PIM connected to Dialer: %1. |
| Severity | Error |
| Type | Clear |
| Description | MR PIM connected to Dialer [dialer name]. |
| Action | No action is required. |
| 1438025 | Message | Import ID: %1, has more than 10,000 errors. |
| Severity | Error |
| Type | Single-State Raise |
| Description | Import process has more than 10,000 errors. |
| Action | Restart the import process. |
| 1438026 | Message | Dialer: %1, is trying to connect with an incorrect protocol version. |
| Severity | Error |
| Type | Single-State Raise |
| Description | A Dialer with an incorrect protocol version is trying to connect to the Campaign Manager. |
| Action | Please check the Dialer version. |
| 1438027 | Message | Campaign: %1, DNC list to be imported exceeds the number of DNC records allowed. |
| Severity | Error |
| Type | Single-State Raise |
| Description | The DO Not Call (DNC) list to be imported has exceeded the number of DNC records set by ConfigLimit. Please check the CampaignManager
                                       log files for more details. |
| Action | Please check the DNC record limit set by the ConfigLimit tool. |
| 1438028 | Message | Process: %1; system out of memory. |
| Severity | Error |
| Type | Single-State Raise |
| Description | Memory overflow. Not able to instantiate or assign enough memory. |
| Action | This is a memory outage, and the configuration of the system may not be sufficient. |
| 1438029 | Message | Dialer: Unknown port owner: %1. |
| Severity | Error |
| Type | Single-State Raise |
| Description | Dialer: Unknown port owner. |
| Action | Please check the administrator scripts. |
| 1438030 | Message | Cannot find key: %1, in the registry. |
| Severity | Error |
| Type | Single-State Raise |
| Description | Cannot find the specified key in the Windows registry. |
| Action | Please ensure that the installation process went smooth. |
| 1438031 | Message | Unable to open registry key: %1. |
| Severity | Error |
| Type | Single-State Raise |
| Description | Unable to open registry key. |
| Action | Please ensure that the installation process was successful. |
| 1438032 | Message | Campaign Manager could not connect to the Outbound Option private database. |
| Severity | Error |
| Type | Single-State Raise |
| Description | Campaign Manager could not connect to the Outbound Option private database. |
| Action | Make sure that SQL Server is running and the Outbound Option private database is initialized. |
| 1438033 | Message | Dialer attempted to connect to incorrect Campaign Manager version: %1, required version: %2. |
| Severity | Error |
| Type | Single-State Raise |
| Description | Dialer attempted to connect to incorrect Campaign Manager version. |
| Action | Please ensure that the Campaign Manager is compatible with the Dialer version. |
| 1438034 | Message | Your configured dialer type: %1, doesn't match this dialer type: %2. |
| Severity | Error |
| Type | Single-State Raise |
| Description | Your configured dialer type doesn't match this dialer type. |
| Action | Please check the dialer type configured. IP or SIP. |
| 1438035 | Message | Dialer has too many ports configured: %1, maximum allowed: %2. |
| Severity | Error |
| Type | Single-State Raise |
| Description | Dialer has too many ports configured. |
| Action | Please decrease the number of ports configured. |
| 1438036 | Message | Campaign Manager: Unable to convert SystemTime to FileTime. |
| Severity | Error |
| Type | Single-State Raise |
| Description | Internal error: Unable to convert SystemTime to FileTime. |
| Action | No action is required. |
| 1438037 | Message | Outbound Option connection to SIP server: %1, on host: %2, is down; heartbeat failure detected. |
| Severity | Error |
| Type | Raise |
| Description | Outbound Option SIP server heart beat failure, the connection is down. |
| Action | Please make sure SIP server is alive and reachable from Outbound Option SIP dialer. |
| 1438038 | Message | Outbound Option connection to SIP server: %1, on host: %2, is up; heartbeat ACK detected. |
| Severity | Informational |
| Type | Clear |
| Description | Outbound Option SIP server heartbeat ACK received, the connection is up. |
| Action | No action is required. |
| 1438039 | Message | Current private database version is: %1. Required version is: %2. |
| Severity | Error |
| Type | Single-State Raise |
| Description | Outbound Option private database version is not correct. It needs to be upgraded using EDMT. |
| Action | Please upgrade private database to the correct version using EDMT for this release. |
| 1438040 | Message | Missing/incorrect local static route file is detected on: %1, in the directory: ..\icm\%2\Dialer. |
| Severity | Error |
| Type | Single-State Raise |
| Description | Static route file, ..\Dialer\DNPHost, is missing or has no valid static route entry when configuring the SIP Dialer to connect
                                       to voice gateway. |
| Action | Re-run the Dialer setup to install sample DNPHost file, and/or enter valid static route entry. |
| 1438041 | Message | CPA is disabled on voice gateway: %1; number of calls without CPA: %2. |
| Severity | Error |
| Type | Single-State Raise |
| Description | CPA is disabled or not supported on voice gateway. |
| Action | Please enable CPA on voice gateway. |
| 1438042 | Message | Action required: Outbound Option database free space is very low: %1%% used. |
| Severity | Error |
| Type | Single-State Raise |
| Description | Outbound Option database space utilization has reached the threshold limit. |
| Action | Please increase the database space utilization or remove unnecessary records from the Outbound Option database. |
| 1438043 | Message | Skill group: %1, has insufficient records: %2, in the last minute on Dialer: %3. |
| Severity | Informational |
| Type | Single-State Raise |
| Description | Campaign skill group has insufficient customer records. |
| Action | Please increase the "records to cache" from the campaign configuration. |
| 1438044 | Message | Voice gateway has been overdialed in the the last %1 second(s); resource not available rate is: %2%%; configured-current port
                                       throttle: %3. |
| Severity | Warning |
| Type | Single-State Raise |
| Description | The capacity of voice gateway or carrier has been exceeded. |
| Action | Please check the capacity of voice gateway or carrier, and adjust the value of "Port Throttle" from the Dialer configuration
                                       accordingly. |
| 1438045 | Message | SIP Dialer has decreased the port throttle by: %1, since VGW overdialing has been detected in the last %2 seconds; adjusted-configured
                                       port throttle: %3. |
| Severity | Warning |
| Type | Single-State Raise |
| Description | SIP Dialer decreases the port throttle since the capacity of voice gateway or carrier is exceeded. |
| Action | Please adjust the value of "Port Throttle" from the Dialer configuration or check the Design Guide for the proper sizing
                                       calculation for the Outbound Dialer. |
| 1438046 | Message | Campaign Manager congestion level changed from: %1 to: %2. |
| Severity | Error |
| Type | Raise |
| Description | There is a change in the congestion level of the Outbound Option Campaign Manager and thus a change in the dialer port throttle
                                       percentage. The Campaign Manager will throttle the dialers according to the congestion level, throttling each dialer back
                                       to a predetermined percentage of full capacity in order to preserve Campaign Manager throughput and prevent a possible brief
                                       outage. |
| Action | The Campaign Manager has exceeded its maximum throughput capacity. Re-evaluate the system design if the congestion occurs
                                       frequently since the system is not able to maintain the high dialing rate. If congestion is occurring at a dialing rate that
                                       was once sustained without congestion, please examine the BA database for fragmentation and/or for a large number of unnecessary
                                       rows of data (i.e. please purge unneeded data from the database). |
| 1438047 | Message | Campaign Manager congestion level is back to normal. |
| Severity | Warning |
| Type | Clear |
| Description | The Campaign Manager is currently not congested and the dialers have resumed dialing at full capacity. |
| Action | None |
| 1438048 | Message | Campaign Manager state changed from: %1 to: %2. |
| Severity | Warning |
| Type | Single-State Raise |
| Description | There is a change in the current state of the Outbound Option Campaign Manager. This typically occurs when one Campaign Manager
                                       side has failed-over to the peer side. A failover may be due to a failure of the Campaign Manager on one side or due to connectivity
                                       issues with the Router, the dialers or the Import process. Only one Campaign Manager will be in an 'active' state at a given
                                       time, the other being in a 'standby' state. |
| Action | If the state change is not due to an administrator intentionally shutting down the Logger service on the node where the active
                                       Campaign Manager is coresident, determine whether the state change is due to a failure of the active Campaign Manager (check
                                       the event logs for errors). Lastly, ensure that there are no connectivity issues between the active Campaign Manager and the
                                       Router, the Import process or the dialers. |
| 1438059 | Message | Imported records count %1 in contact table %2 has reached the threshold of %3 |
| Severity | Error |
| Type | Single-State Raise |
| Description | The number of records in the contact table has exceeded the threshold limit, that may in turn be triggered owing to the import
                                       being performed without the overwrite option, or the number of records in the import file being large. A large Contact table
                                       can result in slow creation of dialing lists as well as excessive space utilization in the BA database |
| Action | Run import corresponding to table with overwrite flag enabled or increase the threshold limit. |

| Message ID (hex) | Property | Value |
|---|---|---|