---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-12-5-1-su1-english-administration-guide-cer0-b-cisco-emergency-responder-cde114755b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/12_5_1_su1/english/administration/guide/cer0_b_cisco-emergency-responder-administration-guide-1251SU1/cer0_b_cisco-emergency-responder-administration-guide-1251SU1_appendix_010100.html
retrieved_at: 2026-08-21T15:34:12.794448+00:00
---

Cisco Emergency Responder Administration Guide for Release 12.5(1)SU1

# Cisco Emergency Responder Administration Guide for Release 12.5(1)SU1

Updated: February 1, 2024

Chapter: Event Log Messages

## Chapter: Event Log Messages

# Event Log Messages

## CER_DATABASE

Type

Message

INFO

Failed to get the fully qualified host name. DNS might not be
                                          					 enabled. Putting Ipaddress in Cluster database.

ERROR

CER Server Memory Usage is HIGH - above threshold value of 80%

ERROR

Database replication BROKEN.

ERROR

Number of <NUM> limit exceeded. Fetching only a maximum
                                          					 of *** <NUM> *** entries

## CER_SYSADMIN

Type

Message

ERROR

Failed to add this CER group to CER cluster.

WARNING

Cisco ER cluster functionality will not work till this problem
                                          					 is fixed.

Check if "CERCluster password" is same as in Cisco ER
                                                						  ClusterDB.

Check if Cisco Tomcat and Database services are running on
                                                						  Cisco ER ClusterDB.

Check if Cisco ER ClusterDB Hostname is correct and
                                                						  accessible.

For more details see EventViewer on ER Server.<Error
                                          					 reason>.

ERROR

Failed to initialize LDAP. <Error Message>

## CER_TELEPHONY

Type

Message

WARNING

Emergency
                                          					 call from<CALLING ADDRESS>has been routed to default ERL because calling
                                          					 party modification failed.

Please make sure that the check box "Enable Calling Party Number Modification" is checked on the Call Manager user page for
                                          the CER user. PSAP callbacks MAY NOT work correctly. The CER service will need to be restarted once the flag is checked on
                                          the Call Manager User page.

WARNING

Emergency
                                          					 call from<calling address>could not be routed using the following
                                          					 Routepatterns.

<LIST
                                          					 OF RP's>

Call
                                          					 Routed to <RP/NUMBER>

Please check the availability of the above routes.

Also,
                                          					 check for the following error conditions.

If FAC
                                                						  and/or CMC are configured on the route patterns used for CER, please disable
                                                						  them.

If the
                                                						  "Calling Party Number Modification" flag on the CER user page in the call
                                                						  manager is not enabled, please enable it.

ERROR

Failed to
                                          					 load class <CLASS NAME>.

ERROR

CCMString
                                          					 is empty can't load telephony classes.

WARNING

Got
                                          					 OutOfService event from provider: <PROVIDER_NAME>.

INFO

Got
                                          					 InService event from provider: <PROVIDER_NAME>.

WARNING

Logged out
                                          					 of the duplicate provider - <CTI_Manager> from CER. Specify the CTI Ports
                                          					 (if any) of this provider, in a different CCM node.

WARNING

Cannot
                                          					 register media terminal for port: <PORT_NUMBER>.

WARNING

CTI Port:
                                          					 <PORT_NUMBER> is in OUTOFSERVICE, trying after 10 seconds.

ERROR

Media channel creation failed: <ERROR>.

WARNING

Failed to
                                          					 create media channel for: <PORT_NUMBER>.

ERROR

Failed to
                                          					 initiate call to security: <NUMBER> <ERROR>.

<ERROR> corresponds to:

PrivilegeViolationException

InvalidPartyException

MethodNotSupportedException

InvalidArgumentException

InvalidStateException

E911CallRouterException

<Other Exceptions (if any)>

ERROR

Failed to
                                          					 register route point: <ROUTE_PATTERN> with Provider:
                                          					 <PROVIDER_NAME>.

ERROR

RouteAddress: <ADDRESS> is in OUTOFSERVICE.

WARNING

<ADDRESS> Route Point received IN_SERVICE event from
                                          					 Provider <NAME>.

WARNING

<ADDRESS> Route Point received OUT_OF_SERVICE event from
                                          					 Provider <NAME>.

ERROR

<msg>Address = <CALLING ADDRESS> ; Terminal =
                                          					 <CALLING TERMINAL> because, routeEndEvent returned :<CAUSE>

<msg> corresponds to

Call
                                          					 failed to reach PSAP for : /PSAP Callback failed for :

<CAUSE> corresponds to

CAUSE_
                                          					 INVALID_DESTINATION/CAUSE_ROUTING_TIMER_EXPIRED/CAUSE_ PARAMETER_NOT_
                                          					 SUPPORTED/CAUSE_STATE_INCOMPATIBLE/CAUSE_UNSPECIFIED_ ERROR

ERROR

<msg>Address = <CALLING ADDRESS> ; Terminal =
                                          					 <CALLING TERMINAL> because, routeEndEvent returned :
                                          					 CAUSE_CTIERR_FAC_CMC_REASON_CMC_NEEDED. Please Uncheck the Requirement of
                                          					 FAC/CMC codes on the Route points used by the Cisco Emergency Responder.

WARNING

Call from <CALLER ID> could not be routed to the Offpremise ERL : <ERL NAME>.

Possible
                                          					 reasons: The phone-location association has not yet happened or has met with
                                          					 errors.

Device
                                          					 Name: <DEVICE NAME>

Caller ID:
                                          					 <CALLER ID>

WARNING

Failed to
                                          					 get the JTAPI Provider for: <NAME_STRING> trying infinitely.

WARNING

Not
                                          					 registering the provider: <PROVIDER_NAME> as is already registered/in the
                                          					 same CCM Cluster as that of:<element>.

WARNING

JTAPI logs
                                          					 are not enabled as the logs path is empty in E911Bootstrap properties.

ERROR

Failed to
                                          					 get the JTAPI Provider for: <IP Address/Host Name> after <NUMBER>
                                          					 attempts.

WARNING

Currently,
                                          					 no CTI Ports are available to place the call for <CallingAddress>. Phone
                                          					 notification will be retried in the next 60 seconds.

## CER_AGGREGATOR

Type

Message

WARNING

Device <ipaddress> is SNMP unreachable. Please check
                                          					 SNMP settings in CER and also on this CCM. Please confirm proper access
                                          					 privilege ( READ_ONLY ) set on this box for SNMP service. Also, verify n/w
                                          					 connectivity.

WARNING

During discovery some devices are unreachable.

List of
                                          					 Unreachable Switches <List>.

WARNING

WARNING During discovery some devices are unreachable.

List of
                                          					 Unreachable CCMs <List>.

WARNING

CERServer could not communicate with CERPhoneTrackingEngine.

WARNING

CERServer could not communicate with CERPhoneTrackingEngine.

INFO

Device <IP Address> is SNMP unreachable. Please check
                                          					 SNMP settings in CER and also on this CCM. Please confirm proper access
                                          					 privilege ( READ_ONLY ) set on this box for SNMP service. Also, verify n/w
                                          					 connectivity.

INFO

Error in resolving HostName -> IPAddress through DNS,
                                          					 ignoring the seed from DE <IP Address>.

INFO

IP
                                          					 Address mismatch detected,OLD_IP <IP Address> NEW_IP <IP Address>
                                          					 SEED <IP Address> for any changed configuration, deletion and re addition
                                          					 of seed device is recommended.

INFO

Device <IP Address> is not a valid switch.

INFO

Device <IP Address> is SNMP Un-reachable.

INFO

Device <IP Address> is not supported.

INFO

This Device <IP Address> is identified for a different
                                          					 device family than earlier discovered, ignored for this discovery cycle.

INFO

Failed to retrieve SysOid of a device <IP Address> Please
                                          					 check if device is SNMP reachable.

INFO

This device is not supported <seed>.

INFO

This Device <IPADDRESS> is earlier discovered with
                                          					 different device family for changed device config (ipAddress, deviceFamily,
                                          					 dnsName ). Delete and re-add the device is must; also you need to re-enter SNMP
                                          					 community string if changed from earlier one.

INFO

The device <IP Address> is not a valid switch...please
                                          					 confirm.

INFO

This device not a valid CCM to discover <IP Address>.

INFO

Error in resolving HostName -> IPAddress, ignoring the seed
                                          					 for discovery <IP Address>.

INFO

IP
                                          					 Address mismatch detected,OLD_IP <IP Address> NEW_IP <IP Address>
                                          					 SEED <IP Address> for any changed configuration, deletion and re addition
                                          					 of seed device is recommended.

During discovery some devices are unreachable List of
                                          					 Unreachable Switches<SWITCH LIST> Cisco CallManager(s)<CCM LIST>.

Device <IPADDRESS> is SNMP unreachable. Please check
                                          					 SNMP settings in CER and also on device. IF this is a CCM box then please
                                          					 confirm proper access privilege ( READ_ONLY ) set on this box for SNMP service.
                                          					 Also, verify n/w connectivity.

INFO

Device <IP Address> is not a valid CCM.

## CER_GROUP

Type

Message

INFO

Active Cisco Emergency Responder set to : <Server
                                          					 Details>.

INFO

Connection established with Cisco Emergency Responder:
                                          					 <PEER>

WARNING

Disconnected from Cisco ER: <PEER>.

ERROR

Cisco ER Couldn't open socket at port <NUMBER>, Exiting.

WARNING

Failed to open connection with Cisco Emergency Responder:
                                          					 <_remoteAddress>/<_remotePort>

## CER_CALLENGINE

Type

Message

INFO

Cisco ER
                                          					 Exiting: Graceful shutdown.

ERROR

Problem in
                                          					 initializing SERVER (Server Group). Cannot continue... <EXCEPTION>.

ERROR

Problem in
                                          					 initializing Database (E911ServerGroupParameters). Retried... <COUNT>
                                          					 times.

ERROR

Problem in
                                          					 initializing SERVER (Server). Cannot continue... <EXCEPTION>.

ERROR

Problem in
                                          					 initializing Database (Server). Cannot continue... <EXCEPTION>.

ERROR

Problem in
                                          					 initializing Database (CERServers). Retried... <COUNT> times.

ERROR

Problem in
                                          					 initializing SERVER (License). Cannot continue... <EXCEPTION>.

ERROR

Problem in
                                          					 initializing SERVER (Zone). Cannot continue... <EXCEPTION>.

ERROR

Problem in
                                          					 initializing SERVER (DiscoveryEngine). Cannot continue... <EXCEPTION>.

ERROR

Problem in
                                          					 initializing SERVER (CERIPSubnetManager). Cannot continue... <EXCEPTION>.

ERROR

Problem in
                                          					 initializing SERVER (CERVHMPhoneManager). Cannot continue... <EXCEPTION>.

ERROR

Problem in
                                          					 initializing SERVER (CCM Cluster - No Call Manager seeds configured). Cannot
                                          					 continue... <EXCEPTION>.

ERROR

Problem in
                                          					 initializing SERVER (Seed Switch). Cannot continue... <EXCEPTION>.

ERROR

Problem in
                                          					 initializing SERVER (Discrepant entry). Cannot continue... <EXCEPTION>.

ERROR

Problem in
                                          					 initializing SERVER (Security Contact). Cannot continue... <EXCEPTION>.

ERROR

Problem in
                                          					 refreshing LDAP (Server Group). Cannot continue... <EXCEPTION>.

ERROR

Problem in
                                          					 refreshing LDAP (Zone). Cannot continue... <EXCEPTION>.

ERROR

Problem in
                                          					 refreshing LDAP (Server). Cannot continue... <EXCEPTION>.

ERROR

Problem in
                                          					 refreshing LDAP (Seed Switch). Cannot continue...<EXCEPTION>.

ERROR

Problem in
                                          					 refreshing LDAP (CCM Cluster). Cannot continue... <EXCEPTION>.

ERROR

Problem in
                                          					 refreshing LDAP (Discrepant entry). Cannot continue... <EXCEPTION>.

ERROR

Problem in
                                          					 refreshing LDAP (Security Contact). Cannot continue... <EXCEPTION>.

ERROR

Problem in
                                          					 refreshing LDAP (Security Contact). Cannot continue...<EXCEPTION>.

ERROR

Problem in
                                          					 refreshing zone port tree (Switchport to zone map). Cannot continue...
                                          					 <EXCEPTION>.

ERROR

LicenseManager: End Of 60 Day Evaluation Period. CER Will not
                                          					 work. Please upload a valid License file.

WARNING

Warning!!!
                                          					 You have insufficient number of user licenses. Total phones tracked by the
                                          					 group of CER instances added to the Smart Software Manager exceed the user
                                          					 licenses available.

## CER_CLUSTER

Type

Message

WARNING

IntraCluster Communication failed to ServerGroup with servers Primary:<SERVER DETAILS> StandBy: <SERVER DETAILS>.

## CER_ONSITEALERT

Type

Message

WARNING

Backup Cisco ER <hostname> has taken control as Active
                                          					 Cisco ER.

Transition time: <timestamp>.

WARNING

Primary Cisco ER <hostname> has taken control as Active Cisco ER.

Transition Time: <timestamp>.

WARNING

Emergency call DetailsCaller Extension:<Extn>Call Time
                                          					 :<TimeStamp>

WARNING

Emergency call DetailsCaller Extension:<Extn>Zone/ERL
                                          					 :<zone>LOCATION :<Location>Call Time :<Timestamp>

## CER_PHONETRACKINGENGINE

Type

Message

WARNING

Unified Communication Manager : <IP address> configured for tracking in Cisco Emergency Responder doesn't have Phones registered
                                          to it or unable to send Phone details to CER. Please check on Unified Communication Manager.

| Type | Message |
|---|---|
| INFO | Failed to get the fully qualified host name. DNS might not be
                                          					 enabled. Putting Ipaddress in Cluster database. |
| ERROR | CER Server Memory Usage is HIGH - above threshold value of 80% |
| ERROR | Database replication BROKEN. |
| ERROR | Number of <NUM> limit exceeded. Fetching only a maximum
                                          					 of *** <NUM> *** entries |

| Type | Message |
|---|---|
| ERROR | Failed to add this CER group to CER cluster. |
| WARNING | Cisco ER cluster functionality will not work till this problem
                                          					 is fixed. Check if "CERCluster password" is same as in Cisco ER
                                                						  ClusterDB. Check if Cisco Tomcat and Database services are running on
                                                						  Cisco ER ClusterDB. Check if Cisco ER ClusterDB Hostname is correct and
                                                						  accessible. For more details see EventViewer on ER Server.<Error
                                          					 reason>. |
| ERROR | Failed to initialize LDAP. <Error Message> |

| Type | Message |
|---|---|
| WARNING | Emergency
                                          					 call from<CALLING ADDRESS>has been routed to default ERL because calling
                                          					 party modification failed. Please make sure that the check box "Enable Calling Party Number Modification" is checked on the Call Manager user page for
                                          the CER user. PSAP callbacks MAY NOT work correctly. The CER service will need to be restarted once the flag is checked on
                                          the Call Manager User page. |
| WARNING | Emergency
                                          					 call from<calling address>could not be routed using the following
                                          					 Routepatterns. <LIST
                                          					 OF RP's> Call
                                          					 Routed to <RP/NUMBER> Please check the availability of the above routes. Also,
                                          					 check for the following error conditions. If FAC
                                                						  and/or CMC are configured on the route patterns used for CER, please disable
                                                						  them. If the
                                                						  "Calling Party Number Modification" flag on the CER user page in the call
                                                						  manager is not enabled, please enable it. |
| ERROR | Failed to
                                          					 load class <CLASS NAME>. |
| ERROR | CCMString
                                          					 is empty can't load telephony classes. |
| WARNING | Got
                                          					 OutOfService event from provider: <PROVIDER_NAME>. |
| INFO | Got
                                          					 InService event from provider: <PROVIDER_NAME>. |
| WARNING | Logged out
                                          					 of the duplicate provider - <CTI_Manager> from CER. Specify the CTI Ports
                                          					 (if any) of this provider, in a different CCM node. |
| WARNING | Cannot
                                          					 register media terminal for port: <PORT_NUMBER>. |
| WARNING | CTI Port:
                                          					 <PORT_NUMBER> is in OUTOFSERVICE, trying after 10 seconds. |
| ERROR | Media channel creation failed: <ERROR>. |
| WARNING | Failed to
                                          					 create media channel for: <PORT_NUMBER>. |
| ERROR | Failed to
                                          					 initiate call to security: <NUMBER> <ERROR>. <ERROR> corresponds to: PrivilegeViolationException InvalidPartyException MethodNotSupportedException InvalidArgumentException InvalidStateException E911CallRouterException <Other Exceptions (if any)> |
| ERROR | Failed to
                                          					 register route point: <ROUTE_PATTERN> with Provider:
                                          					 <PROVIDER_NAME>. |
| ERROR | RouteAddress: <ADDRESS> is in OUTOFSERVICE. |
| WARNING | <ADDRESS> Route Point received IN_SERVICE event from
                                          					 Provider <NAME>. |
| WARNING | <ADDRESS> Route Point received OUT_OF_SERVICE event from
                                          					 Provider <NAME>. |
| ERROR | <msg>Address = <CALLING ADDRESS> ; Terminal =
                                          					 <CALLING TERMINAL> because, routeEndEvent returned :<CAUSE> <msg> corresponds to Call
                                          					 failed to reach PSAP for : /PSAP Callback failed for : <CAUSE> corresponds to CAUSE_
                                          					 INVALID_DESTINATION/CAUSE_ROUTING_TIMER_EXPIRED/CAUSE_ PARAMETER_NOT_
                                          					 SUPPORTED/CAUSE_STATE_INCOMPATIBLE/CAUSE_UNSPECIFIED_ ERROR |
| ERROR | <msg>Address = <CALLING ADDRESS> ; Terminal =
                                          					 <CALLING TERMINAL> because, routeEndEvent returned :
                                          					 CAUSE_CTIERR_FAC_CMC_REASON_CMC_NEEDED. Please Uncheck the Requirement of
                                          					 FAC/CMC codes on the Route points used by the Cisco Emergency Responder. |
| WARNING | Call from <CALLER ID> could not be routed to the Offpremise ERL : <ERL NAME>. Possible
                                          					 reasons: The phone-location association has not yet happened or has met with
                                          					 errors. Device
                                          					 Name: <DEVICE NAME> Caller ID:
                                          					 <CALLER ID> |
| WARNING | Failed to
                                          					 get the JTAPI Provider for: <NAME_STRING> trying infinitely. |
| WARNING | Not
                                          					 registering the provider: <PROVIDER_NAME> as is already registered/in the
                                          					 same CCM Cluster as that of:<element>. |
| WARNING | JTAPI logs
                                          					 are not enabled as the logs path is empty in E911Bootstrap properties. |
| ERROR | Failed to
                                          					 get the JTAPI Provider for: <IP Address/Host Name> after <NUMBER>
                                          					 attempts. |
| WARNING | Currently,
                                          					 no CTI Ports are available to place the call for <CallingAddress>. Phone
                                          					 notification will be retried in the next 60 seconds. |

| Type | Message |
|---|---|
| WARNING | Device <ipaddress> is SNMP unreachable. Please check
                                          					 SNMP settings in CER and also on this CCM. Please confirm proper access
                                          					 privilege ( READ_ONLY ) set on this box for SNMP service. Also, verify n/w
                                          					 connectivity. |
| WARNING | During discovery some devices are unreachable. List of
                                          					 Unreachable Switches <List>. |
| WARNING | WARNING During discovery some devices are unreachable. List of
                                          					 Unreachable CCMs <List>. |
| WARNING | CERServer could not communicate with CERPhoneTrackingEngine. |
| WARNING | CERServer could not communicate with CERPhoneTrackingEngine. |
| INFO | Device <IP Address> is SNMP unreachable. Please check
                                          					 SNMP settings in CER and also on this CCM. Please confirm proper access
                                          					 privilege ( READ_ONLY ) set on this box for SNMP service. Also, verify n/w
                                          					 connectivity. |
| INFO | Error in resolving HostName -> IPAddress through DNS,
                                          					 ignoring the seed from DE <IP Address>. |
| INFO | IP
                                          					 Address mismatch detected,OLD_IP <IP Address> NEW_IP <IP Address>
                                          					 SEED <IP Address> for any changed configuration, deletion and re addition
                                          					 of seed device is recommended. |
| INFO | Device <IP Address> is not a valid switch. |
| INFO | Device <IP Address> is SNMP Un-reachable. |
| INFO | Device <IP Address> is not supported. |
| INFO | This Device <IP Address> is identified for a different
                                          					 device family than earlier discovered, ignored for this discovery cycle. |
| INFO | Failed to retrieve SysOid of a device <IP Address> Please
                                          					 check if device is SNMP reachable. |
| INFO | This device is not supported <seed>. |
| INFO | This Device <IPADDRESS> is earlier discovered with
                                          					 different device family for changed device config (ipAddress, deviceFamily,
                                          					 dnsName ). Delete and re-add the device is must; also you need to re-enter SNMP
                                          					 community string if changed from earlier one. |
| INFO | The device <IP Address> is not a valid switch...please
                                          					 confirm. |
| INFO | This device not a valid CCM to discover <IP Address>. |
| INFO | Error in resolving HostName -> IPAddress, ignoring the seed
                                          					 for discovery <IP Address>. |
| INFO | IP
                                          					 Address mismatch detected,OLD_IP <IP Address> NEW_IP <IP Address>
                                          					 SEED <IP Address> for any changed configuration, deletion and re addition
                                          					 of seed device is recommended. |
|  | During discovery some devices are unreachable List of
                                          					 Unreachable Switches<SWITCH LIST> Cisco CallManager(s)<CCM LIST>. |
|  | Device <IPADDRESS> is SNMP unreachable. Please check
                                          					 SNMP settings in CER and also on device. IF this is a CCM box then please
                                          					 confirm proper access privilege ( READ_ONLY ) set on this box for SNMP service.
                                          					 Also, verify n/w connectivity. |
| INFO | Device <IP Address> is not a valid CCM. |

| Type | Message |
|---|---|
| INFO | Active Cisco Emergency Responder set to : <Server
                                          					 Details>. |
| INFO | Connection established with Cisco Emergency Responder:
                                          					 <PEER> |
| WARNING | Disconnected from Cisco ER: <PEER>. |
| ERROR | Cisco ER Couldn't open socket at port <NUMBER>, Exiting. |
| WARNING | Failed to open connection with Cisco Emergency Responder:
                                          					 <_remoteAddress>/<_remotePort> |

| Type | Message |
|---|---|
| INFO | Cisco ER
                                          					 Exiting: Graceful shutdown. |
| ERROR | Problem in
                                          					 initializing SERVER (Server Group). Cannot continue... <EXCEPTION>. |
| ERROR | Problem in
                                          					 initializing Database (E911ServerGroupParameters). Retried... <COUNT>
                                          					 times. |
| ERROR | Problem in
                                          					 initializing SERVER (Server). Cannot continue... <EXCEPTION>. |
| ERROR | Problem in
                                          					 initializing Database (Server). Cannot continue... <EXCEPTION>. |
| ERROR | Problem in
                                          					 initializing Database (CERServers). Retried... <COUNT> times. |
| ERROR | Problem in
                                          					 initializing SERVER (License). Cannot continue... <EXCEPTION>. |
| ERROR | Problem in
                                          					 initializing SERVER (Zone). Cannot continue... <EXCEPTION>. |
| ERROR | Problem in
                                          					 initializing SERVER (DiscoveryEngine). Cannot continue... <EXCEPTION>. |
| ERROR | Problem in
                                          					 initializing SERVER (CERIPSubnetManager). Cannot continue... <EXCEPTION>. |
| ERROR | Problem in
                                          					 initializing SERVER (CERVHMPhoneManager). Cannot continue... <EXCEPTION>. |
| ERROR | Problem in
                                          					 initializing SERVER (CCM Cluster - No Call Manager seeds configured). Cannot
                                          					 continue... <EXCEPTION>. |
| ERROR | Problem in
                                          					 initializing SERVER (Seed Switch). Cannot continue... <EXCEPTION>. |
| ERROR | Problem in
                                          					 initializing SERVER (Discrepant entry). Cannot continue... <EXCEPTION>. |
| ERROR | Problem in
                                          					 initializing SERVER (Security Contact). Cannot continue... <EXCEPTION>. |
| ERROR | Problem in
                                          					 refreshing LDAP (Server Group). Cannot continue... <EXCEPTION>. |
| ERROR | Problem in
                                          					 refreshing LDAP (Zone). Cannot continue... <EXCEPTION>. |
| ERROR | Problem in
                                          					 refreshing LDAP (Server). Cannot continue... <EXCEPTION>. |
| ERROR | Problem in
                                          					 refreshing LDAP (Seed Switch). Cannot continue...<EXCEPTION>. |
| ERROR | Problem in
                                          					 refreshing LDAP (CCM Cluster). Cannot continue... <EXCEPTION>. |
| ERROR | Problem in
                                          					 refreshing LDAP (Discrepant entry). Cannot continue... <EXCEPTION>. |
| ERROR | Problem in
                                          					 refreshing LDAP (Security Contact). Cannot continue... <EXCEPTION>. |
| ERROR | Problem in
                                          					 refreshing LDAP (Security Contact). Cannot continue...<EXCEPTION>. |
| ERROR | Problem in
                                          					 refreshing zone port tree (Switchport to zone map). Cannot continue...
                                          					 <EXCEPTION>. |
| ERROR | LicenseManager: End Of 60 Day Evaluation Period. CER Will not
                                          					 work. Please upload a valid License file. |
| WARNING | Warning!!!
                                          					 You have insufficient number of user licenses. Total phones tracked by the
                                          					 group of CER instances added to the Smart Software Manager exceed the user
                                          					 licenses available. |

| Type | Message |
|---|---|
| WARNING | IntraCluster Communication failed to ServerGroup with servers Primary:<SERVER DETAILS> StandBy: <SERVER DETAILS>. |

| Type | Message |
|---|---|
| WARNING | Backup Cisco ER <hostname> has taken control as Active
                                          					 Cisco ER. Transition time: <timestamp>. |
| WARNING | Primary Cisco ER <hostname> has taken control as Active Cisco ER. Transition Time: <timestamp>. |
| WARNING | Emergency call DetailsCaller Extension:<Extn>Call Time
                                          					 :<TimeStamp> |
| WARNING | Emergency call DetailsCaller Extension:<Extn>Zone/ERL
                                          					 :<zone>LOCATION :<Location>Call Time :<Timestamp> |

| Type | Message |
|---|---|
| WARNING | Unified Communication Manager : <IP address> configured for tracking in Cisco Emergency Responder doesn't have Phones registered
                                          to it or unable to send Phone details to CER. Please check on Unified Communication Manager. |