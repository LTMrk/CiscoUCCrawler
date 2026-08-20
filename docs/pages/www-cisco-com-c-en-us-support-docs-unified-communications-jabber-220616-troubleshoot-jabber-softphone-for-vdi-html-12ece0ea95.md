---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-220616-troubleshoot-jabber-softphone-for-vdi-html-12ece0ea95
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber/220616-troubleshoot-jabber-softphone-for-vdi.html
retrieved_at: 2026-08-20T22:14:02.873032+00:00
---

Troubleshoot Jabber Softphone for VDI - Common Issues

# Troubleshoot Jabber Softphone for VDI - Common Issues

### Download Options

Updated: July 24, 2023

Document ID: 220616

Contents

## Contents

## Introduction

This document describes the most common Jabber Softphone for VDI issues and how to correct them.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of Cisco Unified Communications Manager (CUCM) and Jabber Softphone for VDI (JVDI).

### Components Used

The information in this document is based on the listed software versions:

- Cisco Unified Communications Manager 14.0.1 SU2

- Cisco Jabber 14.1.3

- JVDI Agent 14.1.3

- JVDI Client 14.1.3

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Common Problems and Solutions

### CTI Errors

If a JVDI softphone failure is due to a failed CTI connection, the Jabber connection status from the VDI displays the virtual channel and SIP as connected but CTI as Not Connected .

CTI Connection Failure

When the SIP connection from the JVDI Client is working and there is a CTI failure occurring, the Jabber CSF device displays as registered from the CUCM Administration > Device > Phone website.

CSF registered during CTI failure

#### CTI Timeout

To verify if a CTI timeout occured collect the listed traces and logs.

- CUCM CTIManager Traces

- Jabber Problem Report from virtual desktop infrastructure (VDI)

CUCM CTIManager SDL Trace show that CTIManager attempts a rebind to LDAP and sets the network timeout to 5 seconds.

33538217.033 |07:32:28.921 |AppInfo |authenticationDB::login (Authenticating using LDAP) 33538217.038 |07:32:28.921 |AppInfo |LDAP not initialized...connecting... 33538217.042 |07:32:28.921 |AppInfo |Authenticating with SSL not enabled (0)-(ldap://ldap.domain.local:389) 33538217.046 |07:32:28.924 |AppInfo |LDAP set LDAP_OPT_NETWORK_TIMEOUT option set to 5 seconds

CUCM CTIManager SDL Trace indicates that CTIManager verified the timeout period has passed and sends a provider complete event containing a timeout error to Jabber.

33538233.000 |07:32:38.644 |SdlSig |CtiLoginCheckTimeout |authenticating |CTIHandler(1,200,12,212) |SdlTimerService(1,200,3,1) |1,200,21,215.3^*^* |[R:H-H:0,N:0,L:0,V:0,Z:0,D:0] mSequenceNumber=2 33538233.003 |07:32:38.647 |AppInfo |[CTI-APP] [CTIHandler::OutputCtiMessage ] CTI ProviderOpenCompletedEvent (seq#=2) provider id=16777428 CM Version=14.0.1 error code=2362179701 description=Directory login failed - timeout enableIpv6=0 NoOfDaysPwdToExp=4294967295 33538233.004 |07:32:38.651 |AppInfo |CtiProviderOpenFailure - CTI application failed to open provider; application startup failed CTIconnectionId:212 Reason code.:-1932787595 IPAddress: xxx.xxx.xxx.xxx IPv6Address: App ID:Cisco CTIManager Cluster ID:StandAloneCluster Node ID:cucmpub.domain.local

Jabber log shows Jabber received the PROVIDER_OPEN_COMPLETED_EVENT from CTIManager and closes the CTI connection due to the timeout error received.

2023-01-24 07:32:38,598 DEBUG [0x000026e0] [c\deskphoneprovider\DPProvider.cpp(1274)] [csf.ecc] [CDPProvider::DispatchTheMessage] - [id=0] CDPProvider::DispatchTheMessage, nPduNum=126, pduName=PROVIDER_OPEN_COMPLETED_EVENT 2023-01-24 07:32:38,598 WARN [0x000026e0] [rc\deskphoneprovider\DPProvider.cpp(598)] [csf.ecc] [CDPProvider::HandleEvent_ProviderOpenCompleted] - ProviderOpen failed: reason: 0x8ccc0075, Directory login failed - timeout 2023-01-24 07:32:38,598 ERROR [0x000026e0] [deskphoneprovider\CtiConnection.cpp(260)] [csf.ecc] [CtiConnection::SocketWorkItem::run] - CtiConnection: Socket disconnect failed!

CTI Timeout Solutions

- Verify the CUCM LDAP Authentication port in use. Changing the authentication port to a Global Catalog port (3268\3269) can reduce delay for authentication requests.

- Verify if LDAP Authentication servers are configured as fully qualified domain name (FQDN). If so, make sure all server FQDN are resolvable via DNS from CUCM.

Note : Cisco CTIManager does need to be restarted whenever the authentication port is changed.

#### CTI Permissions

To verify if CTI Permissions are the cause of a CTI failure collect the listed traces and logs.

- CUCM CTIManager Traces

- Jabber Problem Report from VDI

CUCM CTIManager SDL Traces show CTIManager verifying the user settings. During the settings verification CTIManager sends a ProviderOpenCompletedEvent notifying Jabber that the user does not have the correct permissions to perform CTI control.

33401907.000 |07:49:58.670 |SdlSig |CtiUserSettingsRes |verifying |CTIHandler(1,200,12,150) |CTIDbAccess(1,200,8,1) |1,200,21,153.3^*^* |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0] SuperProvider = Disabled CallParkRetrievalAllowed = Disabled ModifyCallingNumber = Disabled CTI Enabled = Disabled CallMonitor=Disabled CallRecord=Disabled Userid = jking result=0 33401907.005 |07:49:58.670 |AppInfo |[CTI-APP] [CTIHandler::OutputCtiMessage ] CTI ProviderOpenCompletedEvent (seq#=2) provider id=16777366 CM Version=14.0.1 error code=2362179679 description=Directory login failed - User not present in Standard CTI Users group. enableIpv6=0 NoOfDaysPwdToExp=4294967295 33401907.006 |07:49:58.673 |AppInfo |CtiProviderOpenFailure - CTI application failed to open provider; application startup failed CTIconnectionId:150 Reason code.:-1932787617 IPAddress:xxx.xxx.xxx.xxx IPv6Address: App ID:Cisco CTIManager Cluster ID:StandAloneCluster Node ID:cucmpub.domain.local

Jabber logs indicates that Jabber receives the PROVIDER_OPEN_COMPLETED_EVENT from CTIManager but fails due to incorrect permissions.

2023-01-23 07:49:58,561 DEBUG [0x000026a8] [c\deskphoneprovider\DPProvider.cpp(1274)] [csf.ecc] [CDPProvider::DispatchTheMessage] - [id=0] CDPProvider::DispatchTheMessage, nPduNum=126, pduName=PROVIDER_OPEN_COMPLETED_EVENT 2023-01-23 07:49:58,561 WARN [0x000026a8] [rc\deskphoneprovider\DPProvider.cpp(598)] [csf.ecc] [CDPProvider::HandleEvent_ProviderOpenCompleted] - ProviderOpen failed: reason: 0x8ccc005f, Directory login failed - User not present in Standard CTI Users group. 2023-01-23 07:49:35,561 ERROR [0x000026a8] [deskphoneprovider\CtiConnection.cpp(260)] [csf.ecc] [CtiConnection::SocketWorkItem::run] - CtiConnection: Socket disconnect failed!

CTI Permissions Solution

- This issue can be solved by adding the Standard CTI Enabled role to the CUCM end users configuration ( CUCM Administration > User Management > End User ).

Standard CTI Enable CUCM end user role

#### CTI Line Control Disabled

To verify if CTI line control errors exist collect the listed traces and logs.

- CUCM CTIManager Traces

- Jabber Problem Report from VDI

CUCM CTIManager SDL Trace show CTI Manager received a LineOpenRequest from Jabber. CTIManager is unable to perform the line open and sends a line open failed event to Jabber.

33407677.002 |08:35:28.159 |AppInfo |[CTI-APP] [CTIHandler::processIncomingMessage] CTI LineOpenRequest ( seq#=5 AutoAccept=0 Partition=Internal_PT) 33407688.000 |08:35:28.162 |SdlSig-I |CtiLineOpenLineRes |ready |CTIDeviceLineMgr(1,200,9,1) |CTIRegistrar(3,100,26,1) |1,200,21,167.6^xxx.xxx.xxx.xxx^CSFJKING |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0] AsyncResponse=624 Name=CSFJKING LH=1|145 Result=0x8ccc00d3 Auto Accept Status=0 33407688.001 |08:35:28.162 |AppInfo |[CTI-APP] [Line(145)::openLineResponse] (Signal=CtiLineOpenLineRes State=lineState_opening LineNumber=1151026, LineHandle: CtiID=1:LineID=145, LineRequestTimeout=5) 33407688.002 |08:35:28.162 |AppInfo |CtiLineOpenFailure - Unable to open the line CTI Connection Id:1 Device Name:CSFJKING Directory Number:1151026 Partition:Internal_PT UNKNOWN_PARAMTYPE:Reason:-1932787501 App ID:Cisco CTIManager Cluster ID:StandAloneCluster Node ID:cucmpub.domain.local

33407688.008 |08:35:28.162 |AppError |LineOpen failed. Removing Line. Device=CSFJKING Local LH=1|145 33407689.003 |08:35:28.176 |AppInfo |[CTI-APP] [CTIHandler::OutputCtiMessage ] CTI LineClosedEvent ( LH=1|144 reason=8 )

Jabber.log shows Jabber received the LINE_CLOSED_EVENT from CTI Manager and sets the line to out of service. Once set to out of service Jabber sends a device and provider close event to CTI Manager and the CTI connection is terminated.

2023-01-23 08:35:28,471 DEBUG [0x00001e6c] [c\deskphoneprovider\DPProvider.cpp(1405)] [csf.ecc] [CDPProvider::DispatchTheMessage] - [id=0] Received: , pdunames[nPduNum]=LINE_CLOSED_EVENT 2023-01-23 08:35:28,471 DEBUG [0x00001e6c] [cc\src\deskphoneprovider\DPLine.cpp(711)] [csf.ecc] [CDPLine::HandleEvent_LineClosed] - CDPLine::HandleEvent_LineClosed 2023-01-23 08:35:28,471 DEBUG [0x00001e6c] [c\src\deskphoneprovider\DPLine.cpp(1078)] [csf.ecc] [CDPLine::OutOfService] - CDPLine::OutOfService, bClose=1 2023-01-23 08:35:28,486 DEBUG [0x00002818] [c\deskphoneprovider\DPProvider.cpp(1086)] [csf.ecc] [CDPProvider::SendRequest] - [id=0] SendRequest Succeed., pdunames[msg.msgID]=DEVICE_CLOSE_REQUEST, msg.sequenceNumber=6 2023-01-23 08:35:28,486 DEBUG [0x00002818] [c\deskphoneprovider\DPProvider.cpp(1086)] [csf.ecc] [CDPProvider::SendRequest] - [id=0] SendRequest Succeed., pdunames[msg.msgID]=PROVIDER_CLOSE_REQUEST, msg.sequenceNumber=7 2023-01-23 08:35:28,486 ERROR [0x00001e6c] [deskphoneprovider\CtiConnection.cpp(260)] [csf.ecc] [CtiConnection::SocketWorkItem::run] - CtiConnection: Socket disconnect failed!

Line Close Solution

Verify the Allow Control of Device from CTI setting is enabled on the CSF Line configuration ( CUCM Administration > Device > Phone ).

Directory Number CTI Permissions

Note : If the " Allow Control of Device from CTI " is enabled on the line but the CTI errors are still seen, toggle the setting off and on saving between changes.

#### CTI Device Association

To verify if CTI device association errors exist collect the listed traces and logs.

- CUCM CTIManager Traces

- Jabber Problem Report from VDI

CUCM CTIManager SDL Trace reveal CTI Manager receives the PROVIDER_OPEN_REQUEST and sends a provider response with user authentication successful.

33301558.002 |13:27:34.924 |AppInfo |CTIManager::CtiManager::providerOpenRequest(): PROVIDER_OPEN_REQUEST received -- Connection Id=2 TcpHandle=[1:200:21:139] PeerIPAddr=xxx.xxx.xxx.xxx PeerPort=50155 User name= CtiHandler=[1:200:12:136] 33301560.004 |13:27:34.925 |AppInfo |[CTI-APP] [CTIHandler::OutputCtiMessage ] CTI ProviderOpenResponse (seq#=2) provider id=16777352 FIPSMode = 0 33301565.090 |13:27:35.271 |AppInfo |AuthenticationImpl:: Authentication successful for User ID : jking

Next, CTI Manager does a lookup of the CUCM end users controlled devices and no devices are found. A ProviderOpenCompleteEvent is then sent to Jabber with the TotalControllableDevices set to 0.

33301572.000 |13:27:35.271 |SdlSig |CtiDeviceListWithDPFetchRes |ready |CTIDeviceRegManager(1,200,10,1) |CTIDbAccess(1,200,8,1) |1,200,21,139.3^*^* |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0] EnumHandle=89 NumDevices=0 Total=0 mbMore=0 33301572.001 |13:27:35.271 |AppError |ready_CtiDeviceListWithDPFetchRes EnumHandle=89 numDevices=0 TotalDevices=0 More=0 Result=0 33301577.004 |13:27:35.272 |AppInfo |[CTI-INFO] [CTIHandler::GenerateQBEProviderOpenSuccess] totalControllableDevices = 0 33301577.007 |13:27:35.272 |AppInfo |[CTI-APP] [CTIHandler::OutputCtiMessage ] CTI ProviderOpenCompletedEvent (seq#=2) provider id=16777352 dscpForCTI2Apps =96 EnableIpv6 =0 autoCallPickupEnabled =0 LoginUserID = NoOfDaysPwdToExp =4294967295 TotalControllableDevices =0 ClusterId =StandAloneCluster

Jabber.log shows Jabber received the ProviderOpenCompleteEvent from CTI Manager. The get devices request timed out and the handleOpenFailed with a error 8.

2023-01-22 13:26:13,888 DEBUG [0x000025a4] [c\deskphoneprovider\DPProvider.cpp(1274)] [csf.ecc] [CDPProvider::DispatchTheMessage] - [id=0] CDPProvider::DispatchTheMessage, nPduNum=126, pduName=PROVIDER_OPEN_COMPLETED_EVENT 2023-01-22 13:26:13,888 DEBUG [0x000025a4] [c\deskphoneprovider\DPProvider.cpp(1423)] [csf.ecc] [CDPProvider::DispatchTheMessage] - [id=0] PDUTYPE_ProviderEvent or PDUTYPE_Heartbeat, nPduNum=126, pdunames[nPduNum]=PROVIDER_OPEN_COMPLETED_EVENT 2023-01-22 13:26:13,888 DEBUG [0x000025a4] [rc\deskphoneprovider\DPProvider.cpp(577)] [csf.ecc] [CDPProvider::HandleEvent_ProviderOpenCompleted] - [id=0] CDPProvider::HandleEvent_ProviderOpenCompleted

2023-01-22 13:26:32,868 DEBUG [0x00002404] [per\DeskPhoneConnectionContext.cpp(1068)] [csf.ecc] [csf::ecc::DeskPhoneConnectionContext::GetDevicesTimeoutWorkItem::run] - [id=1] DeskPhoneConnectionContext::GetDevicesTimeoutWorkItem::run() 2023-01-22 13:26:32,868 DEBUG [0x00002404] [per\DeskPhoneConnectionContext.cpp(1071)] [csf.ecc] [csf::ecc::DeskPhoneConnectionContext::GetDevicesTimeoutWorkItem::run] - [id=1] Devices timeout 2023-01-22 13:26:32,868 ERROR [0x00002404] [pper\DeskPhoneConnectionContext.cpp(509)] [csf.ecc] [csf::ecc::DeskPhoneConnectionContext::handleOpenFailed] - [id=1] state:2login state:3error:8

Jabber then closes the CTI connection to CUCM and sets telephony service to disconnected due to no device found.

2023-01-22 13:26:32,868 DEBUG [0x00002040] [c\deskphoneprovider\DPProvider.cpp(1070)] [csf.ecc] [CDPProvider::SendRequest] - [id=1] CDPProvider::SendRequest, msg.sequenceNumber=4, pObject=1758DB6C, pdunames[msg.msgID]=PROVIDER_CLOSE_REQUEST 2023-01-22 13:26:32,868 INFO [0x00002040] [\deskphoneprovider\CtiConnection.cpp(60)] [csf.ecc] [CtiConnection::stop] - CtiConnection::stop 2023-01-22 13:26:32,868 ERROR [0x00001e10] [deskphoneprovider\CtiConnection.cpp(260)] [csf.ecc] [CtiConnection::SocketWorkItem::run] - CtiConnection: Socket disconnect failed!

2023-01-22 13:26:32,868 DEBUG [0x000024fc] [ntrol\TelephonyCallControlImpl.cpp(1022)] [jcf.tel.callcontrol] [CSFUnified::TelephonyCallControlImpl::onServiceStartResult] - Service Start Result: [eDeskPhone], Connection Failure code: [eDeviceRegSelectedDeviceNotFound] 2023-01-22 13:26:32,868 INFO [0x00002434] [ices\impl\TelephonyServiceImpl.cpp(3998)] [jcf.tel.service] [CSFUnified::TelephonyServiceImpl::OnTelephonyServiceConnectionStatusChanged] - Telephony Service Device Connection Status changed from [Connecting] to [Disconnected] 2023-01-22 13:26:32,868 DEBUG [0x00002434] [\impl\TelephonyServerHealthImpl.cpp(477)] [jcf.tel.health] [CSFUnified::TelephonyServerHealthImpl::commitIfNotAlreadyCommitted] - deskphone video server health has not been committed because no deskphone found in device list yet

CTI Device Association Solution

- These errors are seen when the JVDI CSF devices is not present in the CUCM end user Controlled Devices . Adding the CSF device to the controlled devices to correct this issue ( CUCM Administration > User Management > End User ).

CUCM Controlled Devices

#### CTI Device Control Disabled

To verify if CTI device control is disabled.collect the listed traces and logs.

- CUCM CTIManager Traces

- Jabber Problem Report from VDI

Jabber log shows Jabber sent a DEVICE_OPEN_REQUEST to CUCM CTI Manager.

2023-01-23 08:14:26,674 DEBUG [0x00002578] [c\deskphoneprovider\DPProvider.cpp(1086)] [csf.ecc] [CDPProvider::SendRequest] - [id=0] SendRequest Succeed., pdunames[msg.msgID]=DEVICE_OPEN_REQUEST, msg.sequenceNumber=4

CUCM CTIManager SDL Trace reveal that CTI Manager received the device open request and responds back to Jabber with a CtiDeviceOpenFailure.

33404809.002 |08:14:27.899 |AppInfo |[CTI-APP] [CTIHandler::processIncomingMessage] CTI DeviceOpenRequest ( seq#=4 device name=CSFJKING softkeys AppID=1234) 33404811.009 |08:14:27.899 |AppError |DeviceThirdParty::isDeviceOpenValid deviceName=CSFJKING Sending CtiDeviceOpenDeviceRes (Seq#=4 error=0x8ccc00d2) 33404812.003 |08:14:27.899 |AppInfo |[CTI-APP] [CTIHandler::OutputCtiMessage ] CTI FailureResponse ( seq#=4 result=2362179794 description=) 33404812.004 |08:14:27.900 |AppInfo |CtiDeviceOpenFailure - Device Open failed CTI Connection Id:154 Device Name:CSFJKING UNKNOWN_PARAMTYPE:ReasonCode:-1932787502 App ID:Cisco CTIManager Cluster ID:StandAloneCluster Node ID:cucmpub.domain.local Process ID:jking-xxx.xxx.xxx.xxx-51126 Process ID:29347 Process Name:CtiHandler

Jabber.log shows Jabber received the Failure Response from CTI Manager and the CTI session is disconnected.

2023-01-23 08:14:27,674 ERROR [0x00002578] [c\deskphoneprovider\DPProvider.cpp(1287)] [csf.ecc] [CDPProvider::DispatchTheMessage] - FailureResponse , result= 0x8ccc00d2 , ( CTIERR_DEVICE_RESTRICTED ) 2023-01-23 08:14:27,674 DEBUG [0x00002578] [c\deskphoneprovider\DPProvider.cpp(1333)] [csf.ecc] [CDPProvider::DispatchTheMessage] - [id=0] Received , pdunames[nPduNum]= FAILURE_RESPONSE , seqNum=4 2023-01-23 08:14:27,686 ERROR [0x00002578] [deskphoneprovider\CtiConnection.cpp(260)] [csf.ecc] [CtiConnection::SocketWorkItem::run] - CtiConnection: Socket disconnect failed!

CTI Device Control Disabled Solution

- Verify the Allow Control of Device from CTI setting is enabled on the CSF Device configuration (CUCM Administration > Device > Phone) .

CSF Device CTI Allow Control

### SIP Errors

When a JVDI softphone failure is due to a failed SIP connection, the Jabber connection status from the VDI displays the virtual channel as connected but the SIP and CTI status show as Not Connected.

JVDI SIP Error

When the SIP connection from the JVDI Client is failing the Jabber CSF device shows as unregistered from the CUCM Administration > Device > Phone website.

CUCM CSF Unregistered

#### SIP Socket Failure

With JVDI all SIP traffic originates from the JVDI Client on the thin client machine. To troubleshoot collect the listed traces and logs.

- CUCM CallManager Traces

- Jabber Problem Report from VDI

JVDI Client vxc log shows that the primary and secondary CUCM servers that are used for SIP 5060 signaling. The primary server is set to the active server.

2020-01-23 08:58:44,623 DEBUG [0x00000000000036a0] [ore\sipstack\sip_common_transport.c(866)] [csf.sip-call-control] [sipTransportCfgTableInit] - [SIP][TRANS][1] PRIMARY_CCM: IPv4 Addr: cucmsub.domain.local:5060 IPv6 Addr: :5060 transport: 4 2020-01-23 08:58:44,623 DEBUG [0x00000000000036a0] [ore\sipstack\sip_common_transport.c(866)] [csf.sip-call-control] [sipTransportCfgTableInit] - [SIP][TRANS][2] SECONDARY_CCM: IPv4 Addr: cucmpub.domain.local:5060 IPv6 Addr: :5060 transport: 4 2020-01-23 08:58:44,633 ERROR [0x00000000000036a0] [re\sipstack\sip_common_transport.c(1075)] [csf.sip-call-control] [sip_transport_get_ti_addr] - [SIP][TRANS] No active 1: PRIMARY_CCM found using primary CUCM

JVDI Client reports a failed socket connection when attempting to connected to the primary server on port 5060. The session is then purged.

2020-01-23 08:58:44,656 DEBUG [0x00000000000036a0] [\core\sipstack\ccsip_platform_tcp.c(910)] [csf.sip-call-control] [sip_tcp_set_reason_for_active_connfailed] - SIPCC-SIP_TCP_MSG: sip_tcp_set_reason_for_active_connfailed: Disconnected from Active Server (). unRegReason:12 Errno:0, Cause:1, Reason:[SOCKET_REMOTE_CLOSURE / CC_UNREG_REASON_CM_RESET_TCP] 2020-01-23 08:58:44,656 INFO [0x00000000000036a0] [tiveapp\sipcc\core\ccapp\cc_alarm.c(816)] [csf.sip-call-control] [setUnregReason] - SIPCC-PLAT_API: setUnregReason: setting unreg reason to=12 2020-01-23 08:58:44,656 DEBUG [0x00000000000036a0] [sipstack\sip_transport_connection.c(282)] [csf.sip-call-control] [sip_transport_connection_on_socket_error] - [SIP][CONN][] socket(3912) error:-1 2020-01-23 08:58:44,656 DEBUG [0x00000000000036a0] [\core\sipstack\ccsip_platform_tcp.c(634)] [csf.sip-call-control] [sip_tcp_destroy_connection] - SIPCC-SIP_SOCK: sip_tcp_destroy_connection: purge entry, socket is 3912, connid is 0 2020-01-23 08:58:44,656 INFO [0x00000000000036a0] [\core\sipstack\ccsip_platform_tcp.c(384)] [csf.sip-call-control] [sip_tcp_purge_entry] - SIPCC-SIP_TCP_MSG: sip_tcp_purge_entry: Socket fd: 3912 closed for connid 0 with address: xxx.xxx.xxx.xxx, remote port: 5060 2020-01-23 08:58:44,656 DEBUG [0x00000000000036a0] [e\sipstack\sip_transport_session.c(1055)] [csf.sip-call-control] [sip_transport_session_disconnect] - [SIP][SESS][0] destroy connection. 2020-01-23 08:58:44,656 INFO [0x00000000000036a0] [re\sipstack\sip_common_transport.c(1666)] [csf.sip-call-control] [sip_transport_on_session_create_failed] - [SIP][TRANS][1] transpot crate failed!

JVDI Client then sets the SIP connection to failed and the SIP route is marked as destroyed.

2020-01-23 08:58:44,656 DEBUG [0x00000000000036a0] [\core\sipstack\sip_common_regmgr.c(3713)] [csf.sip-call-control] [sip_regmgr_on_transport_cucm_connecting_failed] - SIPCC-SIP_REG: sip_regmgr_on_transport_cucm_connecting_failed: [1] cucm connecting failed! 2020-01-23 08:58:44,656 INFO [0x00000000000036a0] [\core\sipstack\sip_common_regmgr.c(2242)] [csf.sip-call-control] [sip_regmgr_cc_create_failed] - SIPCC-SIP_CC_CONN: sip_regmgr_cc_create_failed: cucm 1 lost 2020-01-23 08:58:44,657 DEBUG [0x00000000000036a0] [ore\sipstack\sip_common_transport.c(306)] [csf.sip-call-control] [sip_transport_destroy_cc_conn] - [SIP][TRANS][1] destroy transport session: jabber <-...-> cucm-1 (PRIMARY_CCM)

Common Solutions for SIP socket failures:

- If a VPN is in use verify the JVDI required ports are allowed on all appropriate security appliances. Reference the Port Requirement section of the Jabber Softphone for VDI Deployment and Installation Guide.

- If you are using Citrix Access Gateway or VMware Access Gateway Cisco JVDI requires MRA to be used. Support for JVDI over MRA begins in JVDI and Jabber version 12.6.

- Routing between the Thin Client VLAN and the CUCM VLAN.

- Verify all required ports for JVDI are reachable. Reference the Port Requirement section of the Jabber Softphone for VDI Deployment and Installation Guide.

- Verify if the TCP Syn is making it to the CUCM

- Verify if the thin client or server is resetting the TCP session.

### Revision History

1.0

24-Jul-2023

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 24-Jul-2023 | Initial Release |