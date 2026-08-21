---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-214528-configure-an-2af54f8ddd
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/214528-configure-and-troubleshoot-proxy-tftp-on.html
retrieved_at: 2026-08-21T13:58:50.789514+00:00
---

Configure and Troubleshoot Proxy TFTP on CUCM

# Configure and Troubleshoot Proxy TFTP on CUCM

### Download Options

Updated: October 18, 2022

Document ID: 214528

Contents

## Contents

## Introduction

This document describes the Proxy Trivial File Transfer Protocol (TFTP) feature for Cisco Unified Communications Manager (CUCM).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Phone Registration

- Cisco TFTP service on CUCM

### Components Used

This document is not restricted to specific software and hardware versions as currently supported software and hardware include this feature.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

This document covers the purpose of the feature, configuration of the feature, important diagnostic data, example analysis of the data, and related resources for additional research.

The purpose of this feature is to create a scalable TFTP configuration for large CUCM environments which include multiple CUCM clusters.

### Network Diagram

## Configure

### Manual Proxy TFTP Configuration

Add remote clusters via the Find and List Remote Clusters on the Cisco Unified CM Administration web interface.

Step 1. Add a remote cluster.

- In Cisco Unified CM Administration , choose Advanced Features > Cluster View .

- Click Add New then enter the Cluster Id and Fully Qualified Domain Name .

- Click Save .

Step 2. Enable the Proxy TFTP feature.

- Click the TFTP hyperlink. The Remote Cluster Manually Override Configuration window appears.

- Choose Manually configure remote service addresses.

- Enter the IP addresses for the TFTP servers of the remote cluster.

- Click Save .

Step 3. Add the remote TFTP servers.

- Click the TFTP hyperlink. The Remote Cluster Manually Override Configuration window appears.

- Choose Manually configure remote service addresses.

- Enter the IP addresses for the TFTP servers of the remote cluster.

- Click Save .

Step 4. (Optional) Add the proxy TFTP server to your Dynamic Host Configuration Protocol (DHCP) scope.

For multiple cluster deployments, modify the DHCP scope for individual remote nodes to include the IP address of the primary proxy TFTP server.

### Dynamic Proxy TFTP Configuration

Step 1. Configure Intercluster Lookup Service (ILS) .

Step 2. Check the box for TFTP in the cluster view page.

## Troubleshoot

### Data to Collect

In the case of a proxy TFTP issue, you must collect this information from each CUCM cluster:

- Detailed TFTP logs

- Event Viewer - Application logs

- Event Viewer - System logs

- Packet captures

You must also collect this information from the phone:

- A Problem Report Tool (PRT)

- Packet captures

### Example Analysis

#### Device information from Cisco lab

Phone:

Model: 8861 Firmware version: sip88xx.12-1-1SR1-4 IP address: 192.0.2.11 eth.addr==28:34:a2:82:3b:58

Leaf Cluster where the phone register:

192.0.2.1400-11 192.0.2.12 (only 1 server)

Proxy Cluster:

192.0.2.1500-18 198.51.100.0 (only 1 server)

#### PCAP review for Proxy TFTP cluster

#### TFTP log review for Proxy TFTP cluster

```
##### 07:28:32.110 || SdlConnectionInd for the phone connecting to request the CTL file 00004372.000 |07:28:32.110 |SdlSig   |SdlConnectionInd                       |listening                      |HTTPServer(1,600,25,1)           |SdlTCPConnection(1,600,14,63)    |1,600,12,1.43^*^*                        |*TraceFlagOverrode
00004373.000 |07:28:32.110 |SdlStat  |Period: 17s #Lines: 1 #Bytes: 240 Total Number of Buffers: 2000 Free LWM: 1997 Free LWM(total): 1918
00004372.001 |07:28:32.110 |AppInfo  |-->HTTPSERVER::listening_SdlConnectionInd 
00004372.002 |07:28:32.110 |AppInfo  |HTTPServer::listening_SdlConnection - Printing the sender PID = [1, 600, 14, 63]
00004372.003 |07:28:32.110 |AppInfo  |HTTPServer::handleConnection - Sending a Reassociate Request to Reassociate the newly created HTTPConnectionInfo object to the network/client
00004372.004 |07:28:32.110 |AppInfo  |HTTPServer::listening_SdlConnectionInd - Maximum serving count for HTTP connection is  = 2500
00004372.005 |07:28:32.110 |AppInfo  |HTTPServer::listening_SdlConnectionInd - HTTPConnectionCount = 1
00004372.006 |07:28:32.110 |AppInfo  |<--HTTPSERVER::listening_SdlConnectionInd 
00004374.000 |07:28:32.110 |SdlSig   |SdlReassociateRsp                      |listening                      |HTTPServer(1,600,25,1)           |SdlTCPConnection(1,600,14,63)    |1,600,12,1.43^*^*                        |*TraceFlagOverrode
00004374.001 |07:28:32.110 |AppInfo  |HTTPServer::listening_SdlReassociateRsp - Reassociation Successfull
00004374.002 |07:28:32.110 |AppInfo  |HTTPServer::listening_SdlReassociateRsp - Printing the PID of sender = [1, 600, 14, 63]
00004375.000 |07:28:32.110 |SdlSig   |SdlReassociateInd                      |wait                           |HTTPConnection(1,600,26,3)       |SdlTCPConnection(1,600,14,63)    |1,600,12,1.43^*^*                        |*TraceFlagOverrode
00004375.001 |07:28:32.110 |AppInfo  |-->HTTPConnection::wait_SdlReassociateInd 
00004375.002 |07:28:32.110 |AppInfo  |   HTTPConnection::wait_SdlReassociateInd Received ReassociateIndication from 192.0.2.11
00004375.003 |07:28:32.110 |AppInfo  |<--HTTPConnection::wait_SdlReassociateInd 
00004376.000 |07:28:32.110 |SdlSig   |SdlDataInd                             |wait                           |HTTPConnection(1,600,26,3)       |SdlTCPConnection(1,600,14,63)    |1,600,14,63.2^*^*                        |*TraceFlagOverrode
00004376.001 |07:28:32.110 |AppInfo  |-->HTTPConnection::wait_SdlDataInd 
00004376.002 |07:28:32.110 |AppInfo  |   HTTPConnection::wait_SdlDataInd SdlDataInd recived from TcpPID-[1, 600, 14, 63] ##### 07:28:32.110 || Phone requests the CTL file 00004376.003 |07:28:32.110 |AppInfo  |   HTTPConnection::wait_SdlDataInd Printing the HTTPRequest : msgBuffer size [64] --: GET /CTLSEP2834A2823B58.tlv HTTP/1.1
Host:198.51.100.0:6970

X
00004376.004 |07:28:32.110 |AppInfo  |   HTTPConnection::wait_SdlDataInd Proxy Request- 0 , CTLSEP2834A2823B58.tlv
00004376.005 |07:28:32.110 |AppInfo  |   HTTPConnection::wait_SdlDataInd Decode successful - Filename is : CTLSEP2834A2823B58.tlv
00004376.006 |07:28:32.110 |AppInfo  |   HTTPConnection::wait_SdlDataInd File request signal sent to ServeFile process
00004376.007 |07:28:32.110 |AppInfo  |<--HTTPConnection::wait_SdlDataInd 
00004377.000 |07:28:32.110 |SdlSig   |FileRequest                            |wait                           |ServeFile(1,600,22,1)            |HTTPConnection(1,600,26,3)       |1,600,14,63.2^*^*                        |*TraceFlagOverrode
00004377.001 |07:28:32.110 |AppInfo  |-->ServeFile::wait_FileRequest 
00004377.002 |07:28:32.110 |AppInfo  |   ServeFile::wait_FileRequest Received File request for CTLSEP2834A2823B58.tlv with Request ID 43
00004377.003 |07:28:32.110 |AppInfo  |-->ServeFile::validateFileName 
00004377.004 |07:28:32.110 |AppInfo  |   ServeFile::validateFileName File Requested CTLSEP2834A2823B58.tlv
00004377.005 |07:28:32.110 |AppInfo  |<--ServeFile::validateFileName 
00004377.006 |07:28:32.110 |AppInfo  |   ServeFile::wait_FileRequest File Validation Success and the File to be Searched is CTLSEP2834A2823B58.tlv
00004377.007 |07:28:32.110 |AppInfo  |-->ServeFile::CheckFileIsStatic 
00004377.008 |07:28:32.110 |AppInfo  |   ServeFile::CheckFileIsStatic ctlsep2834a2823b58.tlv is (Not a Static) File
00004377.009 |07:28:32.110 |AppInfo  |<--ServeFile::CheckFileIsStatic 
00004377.010 |07:28:32.110 |AppInfo  |   ServeFile::wait_FileRequest Sending the FileRequest signal to ProcessServeDynamicFile process
00004377.011 |07:28:32.110 |AppInfo  |<--ServeFile::wait_FileRequest 
00004378.000 |07:28:32.110 |SdlSig   |FileRequest                            |wait                           |ServeDynamicFile(1,600,23,5)     |ServeFile(1,600,22,1)            |1,600,14,63.2^*^*                        |*TraceFlagOverrode
00004378.001 |07:28:32.110 |AppInfo  |-->ServeDynamicFile::wait_FileRequest 
00004378.002 |07:28:32.110 |AppInfo  |   ServeDynamicFile::wait_FileRequest Received File request for the dynamic file CTLSEP2834A2823B58.tlv
00004378.003 |07:28:32.110 |AppInfo  |-->ServeDynamicFile::isCTLCAPFRequest 
00004378.004 |07:28:32.110 |AppInfo  |   ServeDynamicFile::isCTLCAPFRequest [CTLSEP2834A2823B58.tlv] is Not a CTLCAPF File
00004378.005 |07:28:32.110 |AppInfo  |<--ServeDynamicFile::isCTLCAPFRequest 
00004378.006 |07:28:32.110 |AppInfo  |   ServeDynamicFile::wait_FileRequest HandleCTL: [CTLSEP2834A2823B58.tlv] is CTLSEPMac.tlv file, Searching[2834A2823B58]
00004378.007 |07:28:32.110 |AppInfo  |TFTPCache::FindMatching(SEP2834A2823B58), Not Found ##### 07:28:32.110 || The file isn't found locally 00004378.008 |07:28:32.110 |AppInfo  |   ServeDynamicFile::wait_FileRequest HandleCTL: Match[CTLSEP2834A2823B58.tlv] Not found locally
00004378.009 |07:28:32.110 |AppInfo  |-->ServeDynamicFile::FindAndServe 
00004378.010 |07:28:32.110 |AppInfo  |[CTLSEP2834A2823B58.tlv] file not found. Checking [CTLSEP2834A2823B58.tlv.sgn] to strip from
00004378.011 |07:28:32.110 |AppInfo  |   ServeDynamicFile::FindAndServe File Not Found - 404 - Failure
00004378.012 |07:28:32.110 |AppInfo  |<--ServeDynamicFile::FindAndServe 
00004378.013 |07:28:32.110 |AppInfo  |   ServeDynamicFile::wait_FileRequest ID not found for the request... Sending File Not Found
00004378.014 |07:28:32.110 |AppInfo  |<--ServeDynamicFile::wait_FileRequest 
00004379.000 |07:28:32.110 |SdlSig   |FileResponse                           |wait                           |ServeFile(1,600,22,1)            |ServeDynamicFile(1,600,23,5)     |1,600,14,63.2^*^*                        |*TraceFlagOverrode
00004379.001 |07:28:32.110 |AppInfo  |-->ServeFile::wait_FileResponse 
00004379.002 |07:28:32.110 |AppInfo  |   ServeFile::wait_FileResponse File Response signal received by ServeFile process ##### 07:28:32.110 || The TFTP service checks for remote TFTP servers 00004379.003 |07:28:32.110 |AppInfo  |   ServeFile::wait_FileResponse FileStatus : 0 -- OffClusters Configured : 1
00004379.004 |07:28:32.110 |AppInfo  |   ServeFile::wait_FileResponse OffClusters are configured. Have to search in off-cluster
00004379.005 |07:28:32.110 |AppInfo  |-->ServeFile::searchFileInOffCluster  
00004379.006 |07:28:32.110 |AppInfo  |   ServeFile::searchFileInOffCluster  FileName = CTLSEP2834A2823B58.tlv
00004379.007 |07:28:32.110 |AppInfo  |   ServeFile::searchFileInOffCluster  RequestID = 43
00004379.008 |07:28:32.110 |AppInfo  |   ServeFile::searchFileInOffCluster  IsStatic = 0
00004379.009 |07:28:32.110 |AppInfo  |-->ServeFile::StartSearchReq  
00004379.010 |07:28:32.110 |AppInfo  |   ServeFile::StartSearchReq  Inserting to CRMDB - [CTLSEP2834A2823B58.tlv] [0] ##### 07:28:32.110 || The request is sent to the ClusterGWAPi 00004379.011 |07:28:32.110 |AppInfo  |   ServeFile::StartSearchReq  Sending New SearchReq signal with TransID [43] to ClusterGWAPi
00004379.012 |07:28:32.110 |AppInfo  |-->ClusterGWApi::searchReq 
00004379.013 |07:28:32.110 |AppInfo  |   ClusterGWApi::searchReq Sending the SearchReq signal with trans ID [43] to ClusterGW.
00004379.014 |07:28:32.110 |AppInfo  |<--ClusterGWApi::searchReq 
00004379.015 |07:28:32.110 |AppInfo  |<--ServeFile::StartSearchReq  
00004379.016 |07:28:32.110 |AppInfo  |   ServeFile::searchFileInOffCluster  CRM DB Lookup failed, hence sending 503 ##### 07:28:32.110 || The search for the file in other clusters is started 00004379.017 |07:28:32.110 |AppInfo  |   ServeFile::searchFileInOffCluster  Started the Search Request in the Off Cluster
00004379.018 |07:28:32.110 |AppInfo  |<--ServeFile::searchFileInOffCluster  
00004379.019 |07:28:32.110 |AppInfo  |<--ServeFile::wait_FileResponse 
00004380.000 |07:28:32.110 |SdlSig   |SearchReq                              |wait                           |ClusterMgr(1,600,28,1)           |ClusterGW(1,600,29,1)            |1,600,14,63.2^*^*                        |*TraceFlagOverrode
00004380.001 |07:28:32.110 |AppInfo  |-->ClusterMgr::wait_SearchReq ##### 07:28:32.110 || The pkid for the remote cluster is listed as the cluster where the search is delivered to 00004380.002 |07:28:32.110 |AppInfo  |   ClusterMgr::wait_SearchReq Sending Search signal with TransID [43] to Cluster [99a15a05-1cb3-4d8f-9d55-0ec097da47cc]
00004380.003 |07:28:32.110 |AppInfo  |<--ClusterMgr::wait_SearchReq 
00004381.000 |07:28:32.110 |SdlSig   |SearchReq                              |wait                           |Cluster(1,600,31,2)              |ClusterMgr(1,600,28,1)           |1,600,14,63.2^*^*                        |*TraceFlagOverrode
00004381.001 |07:28:32.110 |AppInfo  |-->Cluster::wait_SearchReq 
00004381.002 |07:28:32.110 |AppInfo  |<--Cluster::wait_SearchReq 
00004382.000 |07:28:32.110 |SdlSig   |SearchRsp                              |wait                           |ClusterMgr(1,600,28,1)           |Cluster(1,600,31,2)              |1,600,14,63.2^*^*                        |*TraceFlagOverrode
00004382.001 |07:28:32.110 |AppInfo  |-->ClusterMgr::wait_SearchRsp 
00004382.002 |07:28:32.110 |AppInfo  |<--ClusterMgr::wait_SearchRsp 
00004383.000 |07:28:32.110 |SdlSig   |FileResponse                           |wait                           |HTTPConnection(1,600,26,3)       |ServeFile(1,600,22,1)            |1,600,14,63.2^*^*                        |*TraceFlagOverrode
00004383.001 |07:28:32.110 |AppInfo  |-->HTTPConnection::wait_FileResponse 
00004383.002 |07:28:32.110 |AppInfo  |   HTTPConnection::wait_FileResponse HTTPConnection::wait_FileResponse - Requested file is Busy... Sending 503 response
00004383.003 |07:28:32.110 |AppInfo  |<--HTTPConnection::wait_FileResponse 
00004384.000 |07:28:32.110 |SdlSig   |SearchRsp                              |wait                           |ClusterGW(1,600,29,1)            |ClusterMgr(1,600,28,1)           |1,600,14,63.2^*^*                        |*TraceFlagOverrode
00004384.001 |07:28:32.110 |AppInfo  |-->SearchRspCb ##### 07:28:32.110 || The response from teh remote cluster is received and we can see it states FileNotFound. This is expected as the leaf cluster is not in mixed mode. 00004384.002 |07:28:32.110 |AppInfo  |   SearchRspCb Received Search Query response from search engine
00004384.003 |07:28:32.110 |AppInfo  |-->UpdateSearchRsp: Signal TransID[43] 
00004384.004 |07:28:32.110 |AppInfo  |   UpdateSearchRsp: Signal TransID[43] SearchRsp received filename[CTLSEP2834A2823B58.tlv] result [1] transId [43] clusterId [99a15a05-1cb3-4d8f-9d55-0ec097da47cc]isStatic [0] DynamicFile []
00004384.005 |07:28:32.110 |AppInfo  |   UpdateSearchRsp: Signal TransID[43] Search req updated to CRMDB [CTLSEP2834A2823B58.tlv] [FileNotFound] [0] time taken [0] secs
00004384.006 |07:28:32.110 |AppInfo  |<--UpdateSearchRsp: Signal TransID[43] 
00004384.007 |07:28:32.110 |AppInfo  |<--SearchRspCb ##### 07:28:32.110 || SdlCloseRsp for the CTL SdlTCPConnection(1,600,14,63); however, this isn't closed at this time 00004385.000 |07:28:32.110 |SdlSig   |SdlCloseRsp                            |wait                           |HTTPConnection(1,600,26,3)       |SdlTCPConnection(1,600,14,63)    |1,600,14,63.2^*^*                        |*TraceFlagOverrode
00004385.001 |07:28:32.110 |AppInfo  |-->HTTPConnection::wait_SdlCloseRsp 
00004385.002 |07:28:32.110 |AppInfo  |   HTTPConnection::wait_SdlCloseRsp Recieved CloseRsp from TcpConnectionPID-[1, 600, 14, 63]
00004385.003 |07:28:32.110 |AppInfo  |<--HTTPConnection::wait_SdlCloseRsp 
00004386.000 |07:28:32.110 |SdlSig   |UpdateReqCount                         |listening                      |HTTPServer(1,600,25,1)           |HTTPConnection(1,600,26,3)       |1,600,14,63.2^*^*                        |*TraceFlagOverrode
00004386.001 |07:28:32.110 |AppInfo  |HTTPServer::listening_UpdateReqCount - Printing the PID of sender = [1, 600, 26, 3]
00004386.002 |07:28:32.110 |AppInfo  |HTTPServer::listening_throttle_UpdateReqCount - HTTPConnectionCount = 0, PersistentConnectionCount = 0
00004387.000 |07:28:32.738 |AppInfo  |RequestPoller::pollForRequest(30), fd(24) Read Ready
00004388.000 |07:28:32.738 |AppInfo  |-->TID[e71f5b70] TFTPEngine::getRequest[0xf4d26318](), server socket(24) ##### 07:28:32.738 || The TFTP service seems to do another search for the file 00004389.000 |07:28:32.738 |AppInfo  |   TID[e71f5b70] TFTPEngine::getRequest[0xf4d26318](), server socket(24) INFO:: File Requested CTLSEP2834A2823B58.tlv
00004390.000 |07:28:32.738 |AppInfo  |<--TID[e71f5b70] TFTPEngine::getRequest[0xf4d26318](), server socket(24) 
00004391.000 |07:28:32.738 |AppInfo  |   TID[e71f5b70] TFTPServer::recvMessage[0x892bfd8]() sockets:24 CReqContext[0xf4d26318] Requested File[CTLSEP2834A2823B58.tlv]
00004392.000 |07:28:32.738 |AppInfo  |TFTPEngine::isReadRequest[0xf4d26318~5~192.0.2.11~51909], [CTLSEP2834A2823B58.tlv] opcode(1), Mode(octet), Serving Count(0)
00004393.000 |07:28:32.738 |AppInfo  |   TID[e71f5b70] TFTPServer::recvMessage[0x892bfd8]() sockets:24 count(00000), connect(0xf4d26318), nbytes(31)
00004394.000 |07:28:32.738 |AppInfo  |TID[e71f5b70] CReqProcessThreads::processTftpReq(push CReqContext[0xf4d26318])
00004395.000 |07:28:32.738 |AppInfo  |-->TID[e71f5b70] MemPool::getFromMemPool() 
00004396.000 |07:28:32.738 |AppInfo  |   TID[e71f5b70] MemPool::getFromMemPool() Element[6], Buff[0xf4d26d18], used[1]
00004397.000 |07:28:32.738 |AppInfo  |<--TID[e71f5b70] MemPool::getFromMemPool() 
00004398.000 |07:28:32.738 |AppInfo  |-->TID[f116fb70] CReqContext::TFTPProxyRun(), [0xf4d26318~5~192.0.2.11~51909] 
00004399.000 |07:28:32.738 |AppInfo  |-->TFTPEngine::setupTransport[0xf4d26318~5~192.0.2.11~51909] 
00004400.000 |07:28:32.739 |AppInfo  |   TFTPEngine::setupTransport[0xf4d26318~5~192.0.2.11~51909] TFTP IP_TOS conn sock dscp=96
00004401.000 |07:28:32.739 |AppInfo  |<--TFTPEngine::setupTransport[0xf4d26318~5~192.0.2.11~51909] 
00004402.000 |07:28:32.739 |AppInfo  |-->CReqContext::tftp[0xf4d26318~5~192.0.2.11~51909] 
00004403.000 |07:28:32.739 |AppInfo  |CReqContext::CheckAndSetIsStatic(ctlsep2834a2823b58.tlv) is (Not a Static) File
00004404.000 |07:28:32.739 |AppInfo  |CReqContext::isCTLCAPFRequest[CTLSEP2834A2823B58.tlv] Not a CTLCAPF File
00004405.000 |07:28:32.739 |AppInfo  |   CReqContext::tftp[0xf4d26318~5~192.0.2.11~51909] HandleCTL: [CTLSEP2834A2823B58.tlv] is CTLSEPMac.tlv file, Searching[2834A2823B58] ##### 07:28:32.739 || Once again we see Not found locally 00004406.000 |07:28:32.739 |AppInfo  |TFTPCache::FindMatching(SEP2834A2823B58), Not Found
00004407.000 |07:28:32.739 |AppInfo  |   CReqContext::tftp[0xf4d26318~5~192.0.2.11~51909] HandleCTL: Match[2834A2823B58] Not found locally
00004408.000 |07:28:32.739 |AppInfo  |CReqContext::checkAndHandleDiagReq[0xf4d26318~5~192.0.2.11~51909], File[CTLSEP2834A2823B58.tlv]
00004409.000 |07:28:32.739 |AppInfo  |   CReqContext::tftp[0xf4d26318~5~192.0.2.11~51909] Found entry [CTLSEP2834A2823B58.tlv] in state[1] in CRMDB with count [0]
00004410.000 |07:28:32.739 |AppInfo  |INFO: TFTPEngine::sendNAK[0xf4d26318~5~192.0.2.11~51909], File[CTLSEP2834A2823B58.tlv], Error(1)
00004411.000 |07:28:32.739 |AppInfo  |<--CReqContext::tftp[0xf4d26318~5~192.0.2.11~51909] 
00004412.000 |07:28:32.739 |AppInfo  |<--TID[f116fb70] CReqContext::TFTPProxyRun(), [0xf4d26318~5~192.0.2.11~51909] 
00004413.000 |07:28:32.739 |AppInfo  |TID[f116fb70] CReqContext::~CReqContext[0xf4d26318~5~192.0.2.11~51909]destructor
00004414.000 |07:28:32.739 |AppInfo  |TID[f116fb70] MemPool::putToMemPool(0xf4d26318) m_element[5].Buff = [0xf4d26318] ##### 07:28:32.946 || SdlConnectionInd for the phone connecting to request the ITL file 00004415.000 |07:28:32.946 |SdlSig   |SdlConnectionInd                       |listening                      |HTTPServer(1,600,25,1)           |SdlTCPConnection(1,600,14,64)    |1,600,12,1.44^*^*                        |*TraceFlagOverrode
00004415.001 |07:28:32.946 |AppInfo  |-->HTTPSERVER::listening_SdlConnectionInd 
00004415.002 |07:28:32.946 |AppInfo  |HTTPServer::listening_SdlConnection - Printing the sender PID = [1, 600, 14, 64]
00004415.003 |07:28:32.946 |AppInfo  |HTTPServer::handleConnection - Sending a Reassociate Request to Reassociate the newly created HTTPConnectionInfo object to the network/client
00004415.004 |07:28:32.946 |AppInfo  |HTTPServer::listening_SdlConnectionInd - Maximum serving count for HTTP connection is  = 2500
00004415.005 |07:28:32.946 |AppInfo  |HTTPServer::listening_SdlConnectionInd - HTTPConnectionCount = 1
00004415.006 |07:28:32.946 |AppInfo  |<--HTTPSERVER::listening_SdlConnectionInd 
00004416.000 |07:28:32.946 |SdlSig   |SdlReassociateRsp                      |listening                      |HTTPServer(1,600,25,1)           |SdlTCPConnection(1,600,14,64)    |1,600,12,1.44^*^*                        |*TraceFlagOverrode
00004416.001 |07:28:32.946 |AppInfo  |HTTPServer::listening_SdlReassociateRsp - Reassociation Successfull
00004416.002 |07:28:32.946 |AppInfo  |HTTPServer::listening_SdlReassociateRsp - Printing the PID of sender = [1, 600, 14, 64]
00004417.000 |07:28:32.946 |SdlSig   |SdlReassociateInd                      |wait                           |HTTPConnection(1,600,26,4)       |SdlTCPConnection(1,600,14,64)    |1,600,12,1.44^*^*                        |*TraceFlagOverrode
00004417.001 |07:28:32.946 |AppInfo  |-->HTTPConnection::wait_SdlReassociateInd 
00004417.002 |07:28:32.946 |AppInfo  |   HTTPConnection::wait_SdlReassociateInd Received ReassociateIndication from 192.0.2.11
00004417.003 |07:28:32.946 |AppInfo  |<--HTTPConnection::wait_SdlReassociateInd 
00004418.000 |07:28:32.946 |SdlSig   |SdlDataInd                             |wait                           |HTTPConnection(1,600,26,4)       |SdlTCPConnection(1,600,14,64)    |1,600,14,64.2^*^*                        |*TraceFlagOverrode
00004418.001 |07:28:32.946 |AppInfo  |-->HTTPConnection::wait_SdlDataInd 
00004418.002 |07:28:32.946 |AppInfo  |   HTTPConnection::wait_SdlDataInd SdlDataInd recived from TcpPID-[1, 600, 14, 64] ##### 07:28:32.946 || The phone requests it's ITL 00004418.003 |07:28:32.946 |AppInfo  |   HTTPConnection::wait_SdlDataInd Printing the HTTPRequest : msgBuffer size [64] --: GET /ITLSEP2834A2823B58.tlv HTTP/1.1
Host:198.51.100.0:6970


00004418.004 |07:28:32.946 |AppInfo  |   HTTPConnection::wait_SdlDataInd Proxy Request- 0 , ITLSEP2834A2823B58.tlv
00004418.005 |07:28:32.946 |AppInfo  |   HTTPConnection::wait_SdlDataInd Decode successful - Filename is : ITLSEP2834A2823B58.tlv
00004418.006 |07:28:32.946 |AppInfo  |   HTTPConnection::wait_SdlDataInd File request signal sent to ServeFile process
00004418.007 |07:28:32.946 |AppInfo  |<--HTTPConnection::wait_SdlDataInd 
00004419.000 |07:28:32.946 |SdlSig   |FileRequest                            |wait                           |ServeFile(1,600,22,1)            |HTTPConnection(1,600,26,4)       |1,600,14,64.2^*^*                        |*TraceFlagOverrode
00004419.001 |07:28:32.946 |AppInfo  |-->ServeFile::wait_FileRequest 
00004419.002 |07:28:32.946 |AppInfo  |   ServeFile::wait_FileRequest Received File request for ITLSEP2834A2823B58.tlv with Request ID 44
00004419.003 |07:28:32.946 |AppInfo  |-->ServeFile::validateFileName 
00004419.004 |07:28:32.946 |AppInfo  |   ServeFile::validateFileName File Requested ITLSEP2834A2823B58.tlv
00004419.005 |07:28:32.946 |AppInfo  |<--ServeFile::validateFileName 
00004419.006 |07:28:32.946 |AppInfo  |   ServeFile::wait_FileRequest File Validation Success and the File to be Searched is ITLSEP2834A2823B58.tlv
00004419.007 |07:28:32.946 |AppInfo  |-->ServeFile::CheckFileIsStatic 
00004419.008 |07:28:32.946 |AppInfo  |   ServeFile::CheckFileIsStatic itlsep2834a2823b58.tlv is (Not a Static) File
00004419.009 |07:28:32.946 |AppInfo  |<--ServeFile::CheckFileIsStatic 
00004419.010 |07:28:32.946 |AppInfo  |   ServeFile::wait_FileRequest Sending the FileRequest signal to ProcessServeDynamicFile process
00004419.011 |07:28:32.946 |AppInfo  |<--ServeFile::wait_FileRequest 
00004420.000 |07:28:32.946 |SdlSig   |FileRequest                            |wait                           |ServeDynamicFile(1,600,23,1)     |ServeFile(1,600,22,1)            |1,600,14,64.2^*^*                        |*TraceFlagOverrode
00004420.001 |07:28:32.946 |AppInfo  |-->ServeDynamicFile::wait_FileRequest 
00004420.002 |07:28:32.946 |AppInfo  |   ServeDynamicFile::wait_FileRequest Received File request for the dynamic file ITLSEP2834A2823B58.tlv
00004420.003 |07:28:32.946 |AppInfo  |-->ServeDynamicFile::isCTLCAPFRequest 
00004420.004 |07:28:32.946 |AppInfo  |   ServeDynamicFile::isCTLCAPFRequest [ITLSEP2834A2823B58.tlv] is Not a CTLCAPF File
00004420.005 |07:28:32.946 |AppInfo  |<--ServeDynamicFile::isCTLCAPFRequest ##### 07:28:32.946 || We see "Not found locally" for the ITL as well 00004420.006 |07:28:32.946 |AppInfo  |   ServeDynamicFile::wait_FileRequest HandleITL: [ITLSEP2834A2823B58.tlv] is ITLSEPMac.tlv file, Searching[2834A2823B58]
00004420.007 |07:28:32.946 |AppInfo  |TFTPCache::FindMatching(SEP2834A2823B58), Not Found
00004420.008 |07:28:32.946 |AppInfo  |   ServeDynamicFile::wait_FileRequest HandleITL: Match[ITLSEP2834A2823B58.tlv] Not found locally
00004420.009 |07:28:32.946 |AppInfo  |-->ServeDynamicFile::FindAndServe 
00004420.010 |07:28:32.946 |AppInfo  |[ITLSEP2834A2823B58.tlv] file not found. Checking [ITLSEP2834A2823B58.tlv.sgn] to strip from
00004420.011 |07:28:32.946 |AppInfo  |   ServeDynamicFile::FindAndServe File Not Found - 404 - Failure
00004420.012 |07:28:32.946 |AppInfo  |<--ServeDynamicFile::FindAndServe 
00004420.013 |07:28:32.946 |AppInfo  |   ServeDynamicFile::wait_FileRequest ID not found for the request... Sending File Not Found
00004420.014 |07:28:32.946 |AppInfo  |<--ServeDynamicFile::wait_FileRequest 
00004421.000 |07:28:32.946 |SdlSig   |FileResponse                           |wait                           |ServeFile(1,600,22,1)            |ServeDynamicFile(1,600,23,1)     |1,600,14,64.2^*^*                        |*TraceFlagOverrode
00004421.001 |07:28:32.946 |AppInfo  |-->ServeFile::wait_FileResponse 
00004421.002 |07:28:32.946 |AppInfo  |   ServeFile::wait_FileResponse File Response signal received by ServeFile process ##### 07:28:32.946 || Again TFTP checks for remote TFTP clusters 00004421.003 |07:28:32.946 |AppInfo  |   ServeFile::wait_FileResponse FileStatus : 0 -- OffClusters Configured : 1
00004421.004 |07:28:32.946 |AppInfo  |   ServeFile::wait_FileResponse OffClusters are configured. Have to search in off-cluster
00004421.005 |07:28:32.946 |AppInfo  |-->ServeFile::searchFileInOffCluster  
00004421.006 |07:28:32.946 |AppInfo  |   ServeFile::searchFileInOffCluster  FileName = ITLSEP2834A2823B58.tlv
00004421.007 |07:28:32.946 |AppInfo  |   ServeFile::searchFileInOffCluster  RequestID = 44
00004421.008 |07:28:32.946 |AppInfo  |   ServeFile::searchFileInOffCluster  IsStatic = 0
00004421.009 |07:28:32.946 |AppInfo  |   ServeFile::searchFileInOffCluster  Found entry [ITLSEP2834A2823B58.tlv] in state[15] in CRMDB with count [0] ##### 07:28:32.946 || The request is sent to ClusterGWApi 00004421.010 |07:28:32.946 |AppInfo  |   ServeFile::searchFileInOffCluster  File [ITLSEP2834A2823B58.tlv] Found in CRMDB. Sending ServeReq Signal to ClusterGWApi.
00004421.011 |07:28:32.946 |AppInfo  |   ServeFile::searchFileInOffCluster  Saved ConReq [0xed605458]. Sending New ServeReq signal with TransID [44] to ClusterGWAPi
00004421.012 |07:28:32.946 |AppInfo  |-->ClusterGWApi::serveReq 
00004421.013 |07:28:32.946 |AppInfo  |   ClusterGWApi::serveReq Sending the ServeReq signal with trans ID [44] to ClusterGW.
00004421.014 |07:28:32.946 |AppInfo  |<--ClusterGWApi::serveReq 
00004421.015 |07:28:32.946 |AppInfo  |<--ServeFile::searchFileInOffCluster  
00004421.016 |07:28:32.946 |AppInfo  |<--ServeFile::wait_FileResponse 
00004422.000 |07:28:32.946 |SdlSig   |ServeReq                               |wait                           |ClusterMgr(1,600,28,1)           |ClusterGW(1,600,29,1)            |1,600,14,64.2^*^*                        |*TraceFlagOverrode
00004422.001 |07:28:32.946 |AppInfo  |-->ClusterMgr::wait_ServeReq ##### 07:28:32.946 || The pkid for the remote cluster is listed as the cluster where the search is delivered to 00004422.002 |07:28:32.946 |AppInfo  |   ClusterMgr::wait_ServeReq Sending ServeReq signal with TransID [44] to Cluster [99a15a05-1cb3-4d8f-9d55-0ec097da47cc]
00004422.003 |07:28:32.946 |AppInfo  |<--ClusterMgr::wait_ServeReq 
00004423.000 |07:28:32.946 |SdlSig   |ServeReq                               |wait                           |Cluster(1,600,31,2)              |ClusterMgr(1,600,28,1)           |1,600,14,64.2^*^*                        |*TraceFlagOverrode
00004423.001 |07:28:32.946 |AppInfo  |-->Cluster::wait_ServeReq 
00004423.002 |07:28:32.946 |AppInfo  |<--Cluster::wait_ServeReq 
00004424.000 |07:28:32.947 |SdlSig   |SdlReadRsp                             |searching                      |ClusterClient(1,600,30,11)       |SdlTCPConnection(1,600,14,14)    |1,600,14,14.33^*^*                       |*TraceFlagOverrode
00004424.001 |07:28:32.947 |AppInfo  |-->ClusterClient::searching_SdlReadRsp ##### 07:28:32.947 || We see a 200 OK 00004424.002 |07:28:32.947 |AppInfo  |   ClusterClient::searching_SdlReadRsp ClusterClient_searching_SdlReadRsp: Contents of msgBuffer is HTTP/1.1 200 OK
Content-length: 8003
Cache-Control: no-store
Content-type: */*
00004424.003 |07:28:32.947 |AppInfo  |-->ClusterClient::decodeHttpHdr ##### 07:28:32.947 || The file is written to /usr/local/cm/tftp/tftpcache/ 00004424.004 |07:28:32.947 |AppInfo  |   ClusterClient::decodeHttpHdr SERVE_QUERY: Writing Dynamic file to location [/usr/local/cm/tftp/tftpcache/ITLSEP2834A2823B58.tlv.44]
00004424.005 |07:28:32.947 |AppInfo  |<--ClusterClient::decodeHttpHdr 
00004424.006 |07:28:32.947 |AppInfo  |<--ClusterClient::searching_SdlReadRsp 
00004425.000 |07:28:32.947 |SdlSig   |WriteReq                               |wait                           |Writer(1,600,20,1)               |WriterMgr(1,600,19,1)            |1,600,14,14.33^*^*                       |*TraceFlagOverrode
00004425.001 |07:28:32.947 |AppInfo  |-->WriteReq::wait_WriteReq 
00004426.000 |07:28:32.947 |SdlSig   |SdlReadRsp                             |searching                      |ClusterClient(1,600,30,11)       |SdlTCPConnection(1,600,14,14)    |1,600,14,14.34^*^*                       |*TraceFlagOverrode
00004426.001 |07:28:32.947 |AppInfo  |-->ClusterClient::searching_SdlReadRsp ##### 07:28:32.947 || the content is decoded 00004426.002 |07:28:32.947 |AppInfo  |-->ClusterClient::decodeHttpContent 
00004426.003 |07:28:32.947 |AppInfo  |sendServeRsp to [1.600.31.2], result[15], transId[44], filename[ITLSEP2834A2823B58.tlv], clusterId[192.0.2.12(99a15a05-1cb3-4d8f-9d55-0ec097da47cc)],prevResult[0],Protocoltype [1] 
00004426.004 |07:28:32.947 |AppInfo  |<--ClusterClient::decodeHttpContent 
00004426.005 |07:28:32.947 |AppInfo  |<--ClusterClient::searching_SdlReadRsp 
00004427.000 |07:28:32.947 |SdlSig   |ServeRsp                               |wait                           |Cluster(1,600,31,2)              |ClusterClient(1,600,30,11)       |1,600,14,14.34^*^*                       |*TraceFlagOverrode
00004427.001 |07:28:32.947 |AppInfo  |-->Cluster::recvServeRsp 
00004427.002 |07:28:32.947 |AppInfo  |<--Cluster::recvServeRsp 
00004428.000 |07:28:32.947 |SdlSig   |ServeRsp                               |wait                           |ClusterMgr(1,600,28,1)           |Cluster(1,600,31,2)              |1,600,14,14.34^*^*                       |*TraceFlagOverrode
00004428.001 |07:28:32.947 |AppInfo  |-->ClusterMgr::wait_ServeRsp 
00004428.002 |07:28:32.947 |AppInfo  |   ClusterMgr::wait_ServeRsp File found for the ServeReq with TransID [44] in Cluster [99a15a05-1cb3-4d8f-9d55-0ec097da47cc]
00004428.003 |07:28:32.947 |AppInfo  |<--ClusterMgr::wait_ServeRsp 
00004425.002 |07:28:32.947 |AppInfo  |<--WriteReq::wait_WriteReq 
00004429.000 |07:28:32.947 |SdlSig   |WriteReq                               |wait                           |Writer(1,600,20,1)               |WriterMgr(1,600,19,1)            |1,600,14,14.34^*^*                       |*TraceFlagOverrode
00004429.001 |07:28:32.947 |AppInfo  |-->WriteReq::wait_WriteReq 
00004429.002 |07:28:32.947 |AppInfo  |<--WriteReq::wait_WriteReq 
00004430.000 |07:28:32.947 |SdlSig   |WriteReq                               |wait                           |Writer(1,600,20,1)               |WriterMgr(1,600,19,1)            |1,600,14,14.34^*^*                       |*TraceFlagOverrode
00004430.001 |07:28:32.947 |AppInfo  |-->WriteReq::wait_WriteReq 
00004430.002 |07:28:32.947 |AppInfo  |sendServeRsp from writerThread to clusterGw, result[15], transId[44], filename[ITLSEP2834A2823B58.tlv], clusterId[99a15a05-1cb3-4d8f-9d55-0ec097da47cc], ProtocolType[1]
00004430.003 |07:28:32.947 |AppInfo  |<--WriteReq::wait_WriteReq 
00004431.000 |07:28:32.947 |SdlSig   |ServeRsp                               |wait                           |ClusterGW(1,600,29,1)            |Writer(1,600,20,1)               |1,600,14,14.34^*^*                       |*TraceFlagOverrode
00004431.001 |07:28:32.947 |AppInfo  |-->SearchRspCb 
00004431.002 |07:28:32.947 |AppInfo  |   SearchRspCb Received Serve Query response from search engine
00004431.003 |07:28:32.947 |AppInfo  |   SearchRspCb ProtocolValue = 1
00004431.004 |07:28:32.947 |AppInfo  |-->ReceivedServeRsp: Signal TransID[44] 
00004431.005 |07:28:32.947 |AppInfo  |   ReceivedServeRsp: Signal TransID[44] Dynamic Filename [/usr/local/cm/tftp/tftpcache/ITLSEP2834A2823B58.tlv.44]
00004431.006 |07:28:32.947 |AppInfo  |   ReceivedServeRsp: Signal TransID[44] File Found - 200 - Success
00004431.007 |07:28:32.947 |AppInfo  |   ReceivedServeRsp: Signal TransID[44] FileResponse Signal sent to connection object
00004431.008 |07:28:32.947 |AppInfo  |<--ReceivedServeRsp: Signal TransID[44] 
00004431.009 |07:28:32.947 |AppInfo  |<--SearchRspCb 
00004432.000 |07:28:32.947 |SdlSig   |FileResponse                           |wait                           |HTTPConnection(1,600,26,4)       |ServeFile(1,600,22,1)            |1,600,14,14.34^*^*                       |*TraceFlagOverrode
00004432.001 |07:28:32.947 |AppInfo  |-->HTTPConnection::wait_FileResponse ##### 07:28:32.947 || The Proxy TFTP sends the ITL file to the phone. 00004432.002 |07:28:32.947 |AppInfo  |   HTTPConnection::wait_FileResponse Requested file FOUND... Sending file Response
00004432.003 |07:28:32.947 |AppInfo  |   HTTPConnection::wait_FileResponse Skip envelope is false or this is not a static file request, serving file [/usr/local/cm/tftp/tftpcache/ITLSEP2834A2823B58.tlv.44]
00004432.004 |07:28:32.947 |AppInfo  |<--HTTPConnection::wait_FileResponse 
00004433.000 |07:28:32.947 |SdlSig   |SdlSendfileRsp                         |wait                           |HTTPConnection(1,600,26,4)       |SdlTCPConnection(1,600,14,64)    |1,600,14,64.3^*^*                        |*TraceFlagOverrode
00004433.001 |07:28:32.947 |AppInfo  |-->HTTPConnection::wait_SdlSendfileRsp 
00004433.002 |07:28:32.947 |AppInfo  |<--HTTPConnection::wait_SdlSendfileRsp ##### 07:28:33.560 || SdlCloseInd closing the connection for the ITL requestSdlTCPConnection(1,600,14,64) 00004434.000 |07:28:33.560 |SdlSig   |SdlCloseInd                            |wait                           |HTTPConnection(1,600,26,4)       |SdlTCPConnection(1,600,14,64)    |1,600,14,64.4^*^*                        |*TraceFlagOverrode
00004434.001 |07:28:33.560 |AppInfo  |-->HTTPConnection::wait_SdlCloseInd 
00004434.002 |07:28:33.560 |AppInfo  |   HTTPConnection::wait_SdlCloseInd Recieved CloseInd from TcpConnectionPID-[1, 600, 14, 64]
00004434.003 |07:28:33.560 |AppInfo  |<--HTTPConnection::wait_SdlCloseInd 
00004435.000 |07:28:33.560 |SdlSig   |UpdateReqCount                         |listening                      |HTTPServer(1,600,25,1)           |HTTPConnection(1,600,26,4)       |1,600,14,64.4^*^*                        |*TraceFlagOverrode
00004435.001 |07:28:33.560 |AppInfo  |HTTPServer::listening_UpdateReqCount - Printing the PID of sender = [1, 600, 26, 4]
00004435.002 |07:28:33.560 |AppInfo  |HTTPServer::listening_throttle_UpdateReqCount - HTTPConnectionCount = 0, PersistentConnectionCount = 0 ##### 07:28:34.615 || SdlConnectionInd for the phone connecting to request the config file SdlTCPConnection(1,600,14,65) 00004436.000 |07:28:34.615 |SdlSig   |SdlConnectionInd                       |listening                      |HTTPServer(1,600,25,1)           |SdlTCPConnection(1,600,14,65)    |1,600,12,1.45^*^*                        |*TraceFlagOverrode
00004436.001 |07:28:34.615 |AppInfo  |-->HTTPSERVER::listening_SdlConnectionInd 
00004436.002 |07:28:34.615 |AppInfo  |HTTPServer::listening_SdlConnection - Printing the sender PID = [1, 600, 14, 65]
00004436.003 |07:28:34.615 |AppInfo  |HTTPServer::handleConnection - Sending a Reassociate Request to Reassociate the newly created HTTPConnectionInfo object to the network/client
00004436.004 |07:28:34.615 |AppInfo  |HTTPServer::listening_SdlConnectionInd - Maximum serving count for HTTP connection is  = 2500
00004436.005 |07:28:34.615 |AppInfo  |HTTPServer::listening_SdlConnectionInd - HTTPConnectionCount = 1
00004436.006 |07:28:34.615 |AppInfo  |<--HTTPSERVER::listening_SdlConnectionInd 
00004437.000 |07:28:34.615 |SdlSig   |SdlReassociateRsp                      |listening                      |HTTPServer(1,600,25,1)           |SdlTCPConnection(1,600,14,65)    |1,600,12,1.45^*^*                        |*TraceFlagOverrode
00004437.001 |07:28:34.615 |AppInfo  |HTTPServer::listening_SdlReassociateRsp - Reassociation Successfull
00004437.002 |07:28:34.615 |AppInfo  |HTTPServer::listening_SdlReassociateRsp - Printing the PID of sender = [1, 600, 14, 65]
00004438.000 |07:28:34.615 |SdlSig   |SdlReassociateInd                      |wait                           |HTTPConnection(1,600,26,5)       |SdlTCPConnection(1,600,14,65)    |1,600,12,1.45^*^*                        |*TraceFlagOverrode
00004438.001 |07:28:34.615 |AppInfo  |-->HTTPConnection::wait_SdlReassociateInd 
00004438.002 |07:28:34.615 |AppInfo  |   HTTPConnection::wait_SdlReassociateInd Received ReassociateIndication from 192.0.2.11
00004438.003 |07:28:34.615 |AppInfo  |<--HTTPConnection::wait_SdlReassociateInd 
00004439.000 |07:28:34.615 |SdlSig   |SdlDataInd                             |wait                           |HTTPConnection(1,600,26,5)       |SdlTCPConnection(1,600,14,65)    |1,600,14,65.2^*^*                        |*TraceFlagOverrode
00004439.001 |07:28:34.615 |AppInfo  |-->HTTPConnection::wait_SdlDataInd 
00004439.002 |07:28:34.615 |AppInfo  |   HTTPConnection::wait_SdlDataInd SdlDataInd recived from TcpPID-[1, 600, 14, 65] ##### 07:28:34.615 || The phone requests it's config file 00004439.003 |07:28:34.615 |AppInfo  |   HTTPConnection::wait_SdlDataInd Printing the HTTPRequest : msgBuffer size [69] --: GET /SEP2834A2823B58.cnf.xml.sgn HTTP/1.1
Host:198.51.100.0:6970


00004439.004 |07:28:34.615 |AppInfo  |   HTTPConnection::wait_SdlDataInd Proxy Request- 0 , SEP2834A2823B58.cnf.xml.sgn
00004439.005 |07:28:34.615 |AppInfo  |   HTTPConnection::wait_SdlDataInd Decode successful - Filename is : SEP2834A2823B58.cnf.xml.sgn
00004439.006 |07:28:34.615 |AppInfo  |   HTTPConnection::wait_SdlDataInd File request signal sent to ServeFile process
00004439.007 |07:28:34.615 |AppInfo  |<--HTTPConnection::wait_SdlDataInd 
00004440.000 |07:28:34.615 |SdlSig   |FileRequest                            |wait                           |ServeFile(1,600,22,1)            |HTTPConnection(1,600,26,5)       |1,600,14,65.2^*^*                        |*TraceFlagOverrode
00004440.001 |07:28:34.615 |AppInfo  |-->ServeFile::wait_FileRequest 
00004440.002 |07:28:34.616 |AppInfo  |   ServeFile::wait_FileRequest Received File request for SEP2834A2823B58.cnf.xml.sgn with Request ID 45
00004440.003 |07:28:34.616 |AppInfo  |-->ServeFile::validateFileName 
00004440.004 |07:28:34.616 |AppInfo  |   ServeFile::validateFileName File Requested SEP2834A2823B58.cnf.xml.sgn
00004440.005 |07:28:34.616 |AppInfo  |<--ServeFile::validateFileName 
00004440.006 |07:28:34.616 |AppInfo  |   ServeFile::wait_FileRequest File Validation Success and the File to be Searched is SEP2834A2823B58.cnf.xml.sgn
00004440.007 |07:28:34.616 |AppInfo  |-->ServeFile::CheckFileIsStatic 
00004440.008 |07:28:34.616 |AppInfo  |   ServeFile::CheckFileIsStatic sep2834a2823b58.cnf.xml.sgn is (Not a Static) File
00004440.009 |07:28:34.616 |AppInfo  |<--ServeFile::CheckFileIsStatic 
00004440.010 |07:28:34.616 |AppInfo  |   ServeFile::wait_FileRequest Sending the FileRequest signal to ProcessServeDynamicFile process
00004440.011 |07:28:34.616 |AppInfo  |<--ServeFile::wait_FileRequest 
00004441.000 |07:28:34.616 |SdlSig   |FileRequest                            |wait                           |ServeDynamicFile(1,600,23,2)     |ServeFile(1,600,22,1)            |1,600,14,65.2^*^*                        |*TraceFlagOverrode
00004441.001 |07:28:34.616 |AppInfo  |-->ServeDynamicFile::wait_FileRequest 
00004441.002 |07:28:34.616 |AppInfo  |   ServeDynamicFile::wait_FileRequest Received File request for the dynamic file SEP2834A2823B58.cnf.xml.sgn
00004441.003 |07:28:34.616 |AppInfo  |-->ServeDynamicFile::isCTLCAPFRequest 
00004441.004 |07:28:34.616 |AppInfo  |   ServeDynamicFile::isCTLCAPFRequest [SEP2834A2823B58.cnf.xml.sgn] is Not a CTLCAPF File
00004441.005 |07:28:34.616 |AppInfo  |<--ServeDynamicFile::isCTLCAPFRequest 
00004441.006 |07:28:34.616 |AppInfo  |   ServeDynamicFile::wait_FileRequest Requested File is : [sep2834a2823b58.cnf.xml.sgn]
00004441.007 |07:28:34.616 |AppInfo  |-->ServeDynamicFile::retrieveTypeOfRequest 
00004441.008 |07:28:34.616 |AppInfo  |   ServeDynamicFile::retrieveTypeOfRequest Request is for XML signed Config File
00004441.009 |07:28:34.616 |AppInfo  |   ServeDynamicFile::retrieveTypeOfRequest File Requested is : [sep2834a2823b58.cnf.xml.sgn]
00004441.010 |07:28:34.616 |AppInfo  |<--ServeDynamicFile::retrieveTypeOfRequest 
00004441.011 |07:28:34.616 |AppInfo  |   ServeDynamicFile::wait_FileRequest Type of Request is : [2]
00004441.012 |07:28:34.616 |AppInfo  |-->CServiceModule::getDeviceNameFromRequest 
00004441.013 |07:28:34.616 |AppInfo  |   CServiceModule::getDeviceNameFromRequest File name after stripping off the extensions = sep2834a2823b58
00004441.014 |07:28:34.616 |AppInfo  |<--CServiceModule::getDeviceNameFromRequest 
00004441.015 |07:28:34.616 |AppInfo  |-->CServiceModule::getIDForRequest 
00004441.016 |07:28:34.616 |AppInfo  |   CServiceModule::getIDForRequest Unable to find device in DB = sep2834a2823b58
00004441.017 |07:28:34.616 |AppInfo  |<--CServiceModule::getIDForRequest 
00004441.018 |07:28:34.616 |AppInfo  |-->ServeDynamicFile::FindAndServe ##### 07:28:34.616 || The proxy TFTP service lets us know the phone's config file isn't found; however, this time it doesn't state Not found locally 00004441.019 |07:28:34.616 |AppInfo  |   ServeDynamicFile::FindAndServe File Not Found - 404 - Failure
00004441.020 |07:28:34.616 |AppInfo  |<--ServeDynamicFile::FindAndServe 
00004441.021 |07:28:34.616 |AppInfo  |   ServeDynamicFile::wait_FileRequest ID not found for the request... Sending File Not Found
00004441.022 |07:28:34.616 |AppInfo  |<--ServeDynamicFile::wait_FileRequest 
00004442.000 |07:28:34.616 |SdlSig   |FileResponse                           |wait                           |ServeFile(1,600,22,1)            |ServeDynamicFile(1,600,23,2)     |1,600,14,65.2^*^*                        |*TraceFlagOverrode
00004442.001 |07:28:34.616 |AppInfo  |-->ServeFile::wait_FileResponse 
00004442.002 |07:28:34.616 |AppInfo  |   ServeFile::wait_FileResponse File Response signal received by ServeFile process ##### 07:28:34.616 || The TFTP service checks for remote TFTP servers 00004442.003 |07:28:34.616 |AppInfo  |   ServeFile::wait_FileResponse FileStatus : 0 -- OffClusters Configured : 1
00004442.004 |07:28:34.616 |AppInfo  |   ServeFile::wait_FileResponse OffClusters are configured. Have to search in off-cluster
00004442.005 |07:28:34.616 |AppInfo  |-->ServeFile::searchFileInOffCluster  
00004442.006 |07:28:34.616 |AppInfo  |   ServeFile::searchFileInOffCluster  FileName = SEP2834A2823B58.cnf.xml.sgn
00004442.007 |07:28:34.616 |AppInfo  |   ServeFile::searchFileInOffCluster  RequestID = 45
00004442.008 |07:28:34.616 |AppInfo  |   ServeFile::searchFileInOffCluster  IsStatic = 0
00004442.009 |07:28:34.616 |AppInfo  |   ServeFile::searchFileInOffCluster  Found entry [SEP2834A2823B58.cnf.xml.sgn] in state[15] in CRMDB with count [0] ##### 07:28:34.616 || The request is sent to the ClusterGWAPi 00004442.010 |07:28:34.616 |AppInfo  |   ServeFile::searchFileInOffCluster  File [SEP2834A2823B58.cnf.xml.sgn] Found in CRMDB. Sending ServeReq Signal to ClusterGWApi.
00004442.011 |07:28:34.616 |AppInfo  |   ServeFile::searchFileInOffCluster  Saved ConReq [0xed605458]. Sending New ServeReq signal with TransID [45] to ClusterGWAPi
00004442.012 |07:28:34.616 |AppInfo  |-->ClusterGWApi::serveReq 
00004442.013 |07:28:34.616 |AppInfo  |   ClusterGWApi::serveReq Sending the ServeReq signal with trans ID [45] to ClusterGW.
00004442.014 |07:28:34.616 |AppInfo  |<--ClusterGWApi::serveReq 
00004442.015 |07:28:34.616 |AppInfo  |<--ServeFile::searchFileInOffCluster  
00004442.016 |07:28:34.616 |AppInfo  |<--ServeFile::wait_FileResponse 
00004443.000 |07:28:34.616 |SdlSig   |ServeReq                               |wait                           |ClusterMgr(1,600,28,1)           |ClusterGW(1,600,29,1)            |1,600,14,65.2^*^*                        |*TraceFlagOverrode
00004443.001 |07:28:34.616 |AppInfo  |-->ClusterMgr::wait_ServeReq ##### 07:28:34.616 || The pkid for the remote cluster is listed as the cluster where the search is delivered to 00004443.002 |07:28:34.616 |AppInfo  |   ClusterMgr::wait_ServeReq Sending ServeReq signal with TransID [45] to Cluster [99a15a05-1cb3-4d8f-9d55-0ec097da47cc]
00004443.003 |07:28:34.616 |AppInfo  |<--ClusterMgr::wait_ServeReq 
00004444.000 |07:28:34.616 |SdlSig   |ServeReq                               |wait                           |Cluster(1,600,31,2)              |ClusterMgr(1,600,28,1)           |1,600,14,65.2^*^*                        |*TraceFlagOverrode
00004444.001 |07:28:34.616 |AppInfo  |-->Cluster::wait_ServeReq 
00004444.002 |07:28:34.616 |AppInfo  |<--Cluster::wait_ServeReq 
00004445.000 |07:28:34.624 |SdlSig   |SdlReadRsp                             |searching                      |ClusterClient(1,600,30,11)       |SdlTCPConnection(1,600,14,14)    |1,600,14,14.35^*^*                       |*TraceFlagOverrode
00004445.001 |07:28:34.624 |AppInfo  |-->ClusterClient::searching_SdlReadRsp ##### 07:28:34.624 || We see a 200 OK 00004445.002 |07:28:34.624 |AppInfo  |   ClusterClient::searching_SdlReadRsp ClusterClient_searching_SdlReadRsp: Contents of msgBuffer is HTTP/1.1 200 OK
Content-length: 12952
Cache-Control: no-store
Content-type: */*

킹׋ɱ
00004445.003 |07:28:34.624 |AppInfo  |-->ClusterClient::decodeHttpHdr ##### 07:28:34.624 || The file is written to /usr/local/cm/tftp/tftpcache/ 00004445.004 |07:28:34.624 |AppInfo  |   ClusterClient::decodeHttpHdr SERVE_QUERY: Writing Dynamic file to location [/usr/local/cm/tftp/tftpcache/SEP2834A2823B58.cnf.xml.sgn.45]
00004445.005 |07:28:34.624 |AppInfo  |<--ClusterClient::decodeHttpHdr 
00004445.006 |07:28:34.624 |AppInfo  |<--ClusterClient::searching_SdlReadRsp 
00004446.000 |07:28:34.624 |SdlSig   |WriteReq                               |wait                           |Writer(1,600,20,1)               |WriterMgr(1,600,19,1)            |1,600,14,14.35^*^*                       |*TraceFlagOverrode
00004446.001 |07:28:34.624 |AppInfo  |-->WriteReq::wait_WriteReq 
00004446.002 |07:28:34.624 |AppInfo  |<--WriteReq::wait_WriteReq 
00004447.000 |07:28:34.624 |SdlSig   |SdlReadRsp                             |searching                      |ClusterClient(1,600,30,11)       |SdlTCPConnection(1,600,14,14)    |1,600,14,14.36^*^*                       |*TraceFlagOverrode
00004447.001 |07:28:34.624 |AppInfo  |-->ClusterClient::searching_SdlReadRsp ##### 07:28:34.624 || the content is decoded 00004447.002 |07:28:34.624 |AppInfo  |-->ClusterClient::decodeHttpContent 
00004447.003 |07:28:34.624 |AppInfo  |sendServeRsp to [1.600.31.2], result[15], transId[45], filename[SEP2834A2823B58.cnf.xml.sgn], clusterId[192.0.2.12(99a15a05-1cb3-4d8f-9d55-0ec097da47cc)],prevResult[0],Protocoltype [1] 
00004447.004 |07:28:34.624 |AppInfo  |<--ClusterClient::decodeHttpContent 
00004447.005 |07:28:34.624 |AppInfo  |<--ClusterClient::searching_SdlReadRsp 
00004448.000 |07:28:34.624 |SdlSig   |ServeRsp                               |wait                           |Cluster(1,600,31,2)              |ClusterClient(1,600,30,11)       |1,600,14,14.36^*^*                       |*TraceFlagOverrode
00004448.001 |07:28:34.624 |AppInfo  |-->Cluster::recvServeRsp 
00004448.002 |07:28:34.624 |AppInfo  |<--Cluster::recvServeRsp 
00004449.000 |07:28:34.624 |SdlSig   |ServeRsp                               |wait                           |ClusterMgr(1,600,28,1)           |Cluster(1,600,31,2)              |1,600,14,14.36^*^*                       |*TraceFlagOverrode
00004449.001 |07:28:34.624 |AppInfo  |-->ClusterMgr::wait_ServeRsp 
00004449.002 |07:28:34.624 |AppInfo  |   ClusterMgr::wait_ServeRsp File found for the ServeReq with TransID [45] in Cluster [99a15a05-1cb3-4d8f-9d55-0ec097da47cc]
00004449.003 |07:28:34.624 |AppInfo  |<--ClusterMgr::wait_ServeRsp 
00004450.000 |07:28:34.624 |SdlSig   |WriteReq                               |wait                           |Writer(1,600,20,1)               |WriterMgr(1,600,19,1)            |1,600,14,14.36^*^*                       |*TraceFlagOverrode
00004450.001 |07:28:34.624 |AppInfo  |-->WriteReq::wait_WriteReq 
00004450.002 |07:28:34.624 |AppInfo  |<--WriteReq::wait_WriteReq 
00004451.000 |07:28:34.624 |SdlSig   |WriteReq                               |wait                           |Writer(1,600,20,1)               |WriterMgr(1,600,19,1)            |1,600,14,14.36^*^*                       |*TraceFlagOverrode
00004451.001 |07:28:34.624 |AppInfo  |-->WriteReq::wait_WriteReq 
00004451.002 |07:28:34.624 |AppInfo  |sendServeRsp from writerThread to clusterGw, result[15], transId[45], filename[SEP2834A2823B58.cnf.xml.sgn], clusterId[99a15a05-1cb3-4d8f-9d55-0ec097da47cc], ProtocolType[1]
00004451.003 |07:28:34.624 |AppInfo  |<--WriteReq::wait_WriteReq 
00004452.000 |07:28:34.624 |SdlSig   |ServeRsp                               |wait                           |ClusterGW(1,600,29,1)            |Writer(1,600,20,1)               |1,600,14,14.36^*^*                       |*TraceFlagOverrode
00004452.001 |07:28:34.624 |AppInfo  |-->SearchRspCb 
00004452.002 |07:28:34.624 |AppInfo  |   SearchRspCb Received Serve Query response from search engine
00004452.003 |07:28:34.624 |AppInfo  |   SearchRspCb ProtocolValue = 1
00004452.004 |07:28:34.624 |AppInfo  |-->ReceivedServeRsp: Signal TransID[45] 
00004452.005 |07:28:34.624 |AppInfo  |   ReceivedServeRsp: Signal TransID[45] Dynamic Filename [/usr/local/cm/tftp/tftpcache/SEP2834A2823B58.cnf.xml.sgn.45]
00004452.006 |07:28:34.624 |AppInfo  |   ReceivedServeRsp: Signal TransID[45] File Found - 200 - Success
00004452.007 |07:28:34.624 |AppInfo  |   ReceivedServeRsp: Signal TransID[45] FileResponse Signal sent to connection object
00004452.008 |07:28:34.624 |AppInfo  |<--ReceivedServeRsp: Signal TransID[45] 
00004452.009 |07:28:34.624 |AppInfo  |<--SearchRspCb ##### 07:28:34.625 || The Proxy TFTP sends the file to the phone 00004453.000 |07:28:34.625 |SdlSig   |FileResponse                           |wait                           |HTTPConnection(1,600,26,5)       |ServeFile(1,600,22,1)            |1,600,14,14.36^*^*                       |*TraceFlagOverrode
00004453.001 |07:28:34.625 |AppInfo  |-->HTTPConnection::wait_FileResponse 
00004453.002 |07:28:34.625 |AppInfo  |   HTTPConnection::wait_FileResponse Requested file FOUND... Sending file Response
00004453.003 |07:28:34.625 |AppInfo  |   HTTPConnection::wait_FileResponse Skip envelope is false or this is not a static file request, serving file [/usr/local/cm/tftp/tftpcache/SEP2834A2823B58.cnf.xml.sgn.45]
00004453.004 |07:28:34.625 |AppInfo  |<--HTTPConnection::wait_FileResponse 
00004454.000 |07:28:34.625 |SdlSig   |SdlSendfileRsp                         |wait                           |HTTPConnection(1,600,26,5)       |SdlTCPConnection(1,600,14,65)    |1,600,14,65.3^*^*                        |*TraceFlagOverrode
00004454.001 |07:28:34.625 |AppInfo  |-->HTTPConnection::wait_SdlSendfileRsp 
00004454.002 |07:28:34.625 |AppInfo  |<--HTTPConnection::wait_SdlSendfileRsp ##### 07:28:35.110 || SdlCloseInd closing the connection for the CNF request SdlTCPConnection(1,600,14,65) 00004455.000 |07:28:35.110 |SdlSig   |SdlCloseInd                            |wait                           |HTTPConnection(1,600,26,5)       |SdlTCPConnection(1,600,14,65)    |1,600,14,65.4^*^*                        |*TraceFlagOverrode
00004455.001 |07:28:35.110 |AppInfo  |-->HTTPConnection::wait_SdlCloseInd 
00004455.002 |07:28:35.110 |AppInfo  |   HTTPConnection::wait_SdlCloseInd Recieved CloseInd from TcpConnectionPID-[1, 600, 14, 65]
00004455.003 |07:28:35.110 |AppInfo  |<--HTTPConnection::wait_SdlCloseInd 
00004456.000 |07:28:35.110 |SdlSig   |UpdateReqCount                         |listening                      |HTTPServer(1,600,25,1)           |HTTPConnection(1,600,26,5)       |1,600,14,65.4^*^*                        |*TraceFlagOverrode
00004456.001 |07:28:35.110 |AppInfo  |HTTPServer::listening_UpdateReqCount - Printing the PID of sender = [1, 600, 26, 5]
00004456.002 |07:28:35.110 |AppInfo  |HTTPServer::listening_throttle_UpdateReqCount - HTTPConnectionCount = 0, PersistentConnectionCount = 0 ##### 07:28:37.124 || At this point the timer for the connection to request the CTL is hit 00004457.000 |07:28:37.124 |SdlSig   |HTTPReadTimer                          |wait                           |HTTPConnection(1,600,26,3)       |SdlTimerService(1,600,3,1)       |1,600,14,63.2^*^*                        |*TraceFlagOverrode
00004457.001 |07:28:37.124 |AppInfo  |-->HTTPConnection::wait_HTTPReadTimer ##### 07:28:37.124 || The connection for the CTL request is closed due to timeout 00004457.002 |07:28:37.124 |AppInfo  |   HTTPConnection::wait_HTTPReadTimer Received a HTTPReadRequest Timeout signal... Closing connection : [1:600:14:63]
00004457.003 |07:28:37.124 |AppInfo  |   HTTPConnection::wait_HTTPReadTimer TCPConnectionPID : [1:600:14:63] not found in active connections
00004457.004 |07:28:37.124 |AppInfo  |<--HTTPConnection::wait_HTTPReadTimer ##### 07:28:38.208 || SdlConnectionInd for the phone connecting to request the AppDialRules.xml file SdlTCPConnection(1,600,14,66) 00004458.000 |07:28:38.208 |SdlSig   |SdlConnectionInd                       |listening                      |HTTPServer(1,600,25,1)           |SdlTCPConnection(1,600,14,66)    |1,600,12,1.46^*^*                        |*TraceFlagOverrode
00004459.000 |07:28:38.208 |SdlStat  |Period: 6s #Lines: 395 #Bytes: 49155 Total Number of Buffers: 2000 Free LWM: 1928 Free LWM(total): 1918
00004458.001 |07:28:38.208 |AppInfo  |-->HTTPSERVER::listening_SdlConnectionInd 
00004458.002 |07:28:38.208 |AppInfo  |HTTPServer::listening_SdlConnection - Printing the sender PID = [1, 600, 14, 66]
00004458.003 |07:28:38.208 |AppInfo  |HTTPServer::handleConnection - Sending a Reassociate Request to Reassociate the newly created HTTPConnectionInfo object to the network/client
00004458.004 |07:28:38.208 |AppInfo  |HTTPServer::listening_SdlConnectionInd - Maximum serving count for HTTP connection is  = 2500
00004458.005 |07:28:38.208 |AppInfo  |HTTPServer::listening_SdlConnectionInd - HTTPConnectionCount = 1
00004458.006 |07:28:38.208 |AppInfo  |<--HTTPSERVER::listening_SdlConnectionInd 
00004460.000 |07:28:38.208 |SdlSig   |SdlReassociateRsp                      |listening                      |HTTPServer(1,600,25,1)           |SdlTCPConnection(1,600,14,66)    |1,600,12,1.46^*^*                        |*TraceFlagOverrode
00004460.001 |07:28:38.208 |AppInfo  |HTTPServer::listening_SdlReassociateRsp - Reassociation Successfull
00004460.002 |07:28:38.208 |AppInfo  |HTTPServer::listening_SdlReassociateRsp - Printing the PID of sender = [1, 600, 14, 66]
00004461.000 |07:28:38.208 |SdlSig   |SdlReassociateInd                      |wait                           |HTTPConnection(1,600,26,1)       |SdlTCPConnection(1,600,14,66)    |1,600,12,1.46^*^*                        |*TraceFlagOverrode
00004461.001 |07:28:38.208 |AppInfo  |-->HTTPConnection::wait_SdlReassociateInd 
00004461.002 |07:28:38.208 |AppInfo  |   HTTPConnection::wait_SdlReassociateInd Received ReassociateIndication from 192.0.2.11
00004461.003 |07:28:38.208 |AppInfo  |<--HTTPConnection::wait_SdlReassociateInd 
00004462.000 |07:28:38.208 |SdlSig   |SdlDataInd                             |wait                           |HTTPConnection(1,600,26,1)       |SdlTCPConnection(1,600,14,66)    |1,600,14,66.2^*^*                        |*TraceFlagOverrode
00004462.001 |07:28:38.208 |AppInfo  |-->HTTPConnection::wait_SdlDataInd 
00004462.002 |07:28:38.208 |AppInfo  |   HTTPConnection::wait_SdlDataInd SdlDataInd recived from TcpPID-[1, 600, 14, 66] ##### 07:28:38.208 || The phone requests the AppDialRules.xml 00004462.003 |07:28:38.208 |AppInfo  |   HTTPConnection::wait_SdlDataInd Printing the HTTPRequest : msgBuffer size [58] --: GET /AppDialRules.xml HTTP/1.1
Host:198.51.100.0:6970

0004462.004 |07:28:38.208 |AppInfo  |   HTTPConnection::wait_SdlDataInd Proxy Request- 0 , AppDialRules.xml
00004462.005 |07:28:38.208 |AppInfo  |   HTTPConnection::wait_SdlDataInd Decode successful - Filename is : AppDialRules.xml
00004462.006 |07:28:38.208 |AppInfo  |   HTTPConnection::wait_SdlDataInd File request signal sent to ServeFile process
00004462.007 |07:28:38.208 |AppInfo  |<--HTTPConnection::wait_SdlDataInd 
00004463.000 |07:28:38.208 |SdlSig   |FileRequest                            |wait                           |ServeFile(1,600,22,1)            |HTTPConnection(1,600,26,1)       |1,600,14,66.2^*^*                        |*TraceFlagOverrode
00004463.001 |07:28:38.208 |AppInfo  |-->ServeFile::wait_FileRequest 
00004463.002 |07:28:38.208 |AppInfo  |   ServeFile::wait_FileRequest Received File request for AppDialRules.xml with Request ID 46
00004463.003 |07:28:38.208 |AppInfo  |-->ServeFile::validateFileName 
00004463.004 |07:28:38.208 |AppInfo  |   ServeFile::validateFileName File Requested AppDialRules.xml
00004463.005 |07:28:38.208 |AppInfo  |<--ServeFile::validateFileName 
00004463.006 |07:28:38.208 |AppInfo  |   ServeFile::wait_FileRequest File Validation Success and the File to be Searched is AppDialRules.xml
00004463.007 |07:28:38.208 |AppInfo  |-->ServeFile::CheckFileIsStatic 
00004463.008 |07:28:38.208 |AppInfo  |   ServeFile::CheckFileIsStatic appdialrules.xml is (Not a Static) File
00004463.009 |07:28:38.208 |AppInfo  |<--ServeFile::CheckFileIsStatic 
00004463.010 |07:28:38.208 |AppInfo  |   ServeFile::wait_FileRequest Sending the FileRequest signal to ProcessServeDynamicFile process
00004463.011 |07:28:38.208 |AppInfo  |<--ServeFile::wait_FileRequest 
00004464.000 |07:28:38.208 |SdlSig   |FileRequest                            |wait                           |ServeDynamicFile(1,600,23,3)     |ServeFile(1,600,22,1)            |1,600,14,66.2^*^*                        |*TraceFlagOverrode
00004464.001 |07:28:38.208 |AppInfo  |-->ServeDynamicFile::wait_FileRequest 
00004464.002 |07:28:38.208 |AppInfo  |   ServeDynamicFile::wait_FileRequest Received File request for the dynamic file AppDialRules.xml
00004464.003 |07:28:38.208 |AppInfo  |-->ServeDynamicFile::isCTLCAPFRequest 
00004464.004 |07:28:38.208 |AppInfo  |   ServeDynamicFile::isCTLCAPFRequest [AppDialRules.xml] is Not a CTLCAPF File
00004464.005 |07:28:38.208 |AppInfo  |<--ServeDynamicFile::isCTLCAPFRequest 
00004464.006 |07:28:38.208 |AppInfo  |   ServeDynamicFile::wait_FileRequest Requested File is : [appdialrules.xml]
00004464.007 |07:28:38.208 |AppInfo  |-->ServeDynamicFile::retrieveTypeOfRequest 
00004464.008 |07:28:38.208 |AppInfo  |   ServeDynamicFile::retrieveTypeOfRequest Request is for XML Config File
00004464.009 |07:28:38.208 |AppInfo  |   ServeDynamicFile::retrieveTypeOfRequest File Requested is : [appdialrules.xml]
00004464.010 |07:28:38.208 |AppInfo  |<--ServeDynamicFile::retrieveTypeOfRequest 
00004464.011 |07:28:38.208 |AppInfo  |   ServeDynamicFile::wait_FileRequest Type of Request is : [1]
00004464.012 |07:28:38.208 |AppInfo  |-->CServiceModule::getDeviceNameFromRequest 
00004464.013 |07:28:38.208 |AppInfo  |   CServiceModule::getDeviceNameFromRequest File Request without extensions
00004464.014 |07:28:38.208 |AppInfo  |<--CServiceModule::getDeviceNameFromRequest 
00004464.015 |07:28:38.208 |AppInfo  |-->CServiceModule::getIDForRequest 
00004464.016 |07:28:38.208 |AppInfo  |   CServiceModule::getIDForRequest Unable to find device in DB = appdialrules.xml
00004464.017 |07:28:38.208 |AppInfo  |<--CServiceModule::getIDForRequest 
00004464.018 |07:28:38.208 |AppInfo  |-->ServeDynamicFile::FindAndServe ##### 07:28:38.208 || appdialrules.xml is found 00004464.019 |07:28:38.208 |AppInfo  |   ServeDynamicFile::FindAndServe File Found - 200 - Success
00004464.020 |07:28:38.208 |AppInfo  |   ServeDynamicFile::FindAndServe ServeDynamicFile::wait_dynamicFileRequest [FileName:(AppDialRules.xml),Content Length:(25)]
00004464.021 |07:28:38.208 |AppInfo  |   ServeDynamicFile::FindAndServe Request ID : 46
00004464.022 |07:28:38.208 |AppInfo  |<--ServeDynamicFile::FindAndServe 
00004464.023 |07:28:38.208 |AppInfo  |<--ServeDynamicFile::wait_FileRequest 
00004465.000 |07:28:38.208 |SdlSig   |FileResponse                           |wait                           |ServeFile(1,600,22,1)            |ServeDynamicFile(1,600,23,3)     |1,600,14,66.2^*^*                        |*TraceFlagOverrode
00004465.001 |07:28:38.208 |AppInfo  |-->ServeFile::wait_FileResponse 
00004465.002 |07:28:38.208 |AppInfo  |   ServeFile::wait_FileResponse File Response signal received by ServeFile process
00004465.003 |07:28:38.208 |AppInfo  |   ServeFile::wait_FileResponse FileStatus : 1 -- OffClusters Configured : 1 ##### 07:28:38.208 || The TFTP service makes it clear the file was found locally 00004465.004 |07:28:38.208 |AppInfo  |   ServeFile::wait_FileResponse File found in proxy tftp itself. Sending the file response to corresponding connection object
00004465.005 |07:28:38.208 |AppInfo  |<--ServeFile::wait_FileResponse 
00004466.000 |07:28:38.208 |SdlSig   |FileResponse                           |wait                           |HTTPConnection(1,600,26,1)       |ServeFile(1,600,22,1)            |1,600,14,66.2^*^*                        |*TraceFlagOverrode
00004466.001 |07:28:38.208 |AppInfo  |-->HTTPConnection::wait_FileResponse ##### 07:28:38.208 || The file response is sent 00004466.002 |07:28:38.208 |AppInfo  |   HTTPConnection::wait_FileResponse Requested file FOUND... Sending file Response
00004466.003 |07:28:38.208 |AppInfo  |<--HTTPConnection::wait_FileResponse ##### 07:28:38.275 || SdlCloseInd closing the connection for the phone requesting the appdialrules SdlTCPConnection(1,600,14,66) 00004467.000 |07:28:38.275 |SdlSig   |SdlCloseInd                            |wait                           |HTTPConnection(1,600,26,1)       |SdlTCPConnection(1,600,14,66)    |1,600,14,66.3^*^*                        |*TraceFlagOverrode
00004467.001 |07:28:38.275 |AppInfo  |-->HTTPConnection::wait_SdlCloseInd 
00004467.002 |07:28:38.275 |AppInfo  |   HTTPConnection::wait_SdlCloseInd Recieved CloseInd from TcpConnectionPID-[1, 600, 14, 66]
00004467.003 |07:28:38.275 |AppInfo  |<--HTTPConnection::wait_SdlCloseInd 
00004468.000 |07:28:38.275 |SdlSig   |UpdateReqCount                         |listening                      |HTTPServer(1,600,25,1)           |HTTPConnection(1,600,26,1)       |1,600,14,66.3^*^*                        |*TraceFlagOverrode
00004468.001 |07:28:38.275 |AppInfo  |HTTPServer::listening_UpdateReqCount - Printing the PID of sender = [1, 600, 26, 1]
00004468.002 |07:28:38.275 |AppInfo  |HTTPServer::listening_throttle_UpdateReqCount - HTTPConnectionCount = 0, PersistentConnectionCount = 0 ##### 07:28:38.337 || SdlConnectionInd for the phone connecting to request the SK72f64050-7ad5-4b47-9bfa-5e9ad9cd4aa9.xml.sgn SdlTCPConnection(1,600,14,67) 00004469.000 |07:28:38.337 |SdlSig   |SdlConnectionInd                       |listening                      |HTTPServer(1,600,25,1)           |SdlTCPConnection(1,600,14,67)    |1,600,12,1.47^*^*                        |*TraceFlagOverrode
00004469.001 |07:28:38.337 |AppInfo  |-->HTTPSERVER::listening_SdlConnectionInd 
00004469.002 |07:28:38.337 |AppInfo  |HTTPServer::listening_SdlConnection - Printing the sender PID = [1, 600, 14, 67]
00004469.003 |07:28:38.337 |AppInfo  |HTTPServer::handleConnection - Sending a Reassociate Request to Reassociate the newly created HTTPConnectionInfo object to the network/client
00004469.004 |07:28:38.337 |AppInfo  |HTTPServer::listening_SdlConnectionInd - Maximum serving count for HTTP connection is  = 2500
00004469.005 |07:28:38.337 |AppInfo  |HTTPServer::listening_SdlConnectionInd - HTTPConnectionCount = 1
00004469.006 |07:28:38.337 |AppInfo  |<--HTTPSERVER::listening_SdlConnectionInd 
00004470.000 |07:28:38.337 |SdlSig   |SdlReassociateRsp                      |listening                      |HTTPServer(1,600,25,1)           |SdlTCPConnection(1,600,14,67)    |1,600,12,1.47^*^*                        |*TraceFlagOverrode
00004470.001 |07:28:38.337 |AppInfo  |HTTPServer::listening_SdlReassociateRsp - Reassociation Successfull
00004470.002 |07:28:38.337 |AppInfo  |HTTPServer::listening_SdlReassociateRsp - Printing the PID of sender = [1, 600, 14, 67]
00004471.000 |07:28:38.337 |SdlSig   |SdlReassociateInd                      |wait                           |HTTPConnection(1,600,26,2)       |SdlTCPConnection(1,600,14,67)    |1,600,12,1.47^*^*                        |*TraceFlagOverrode
00004471.001 |07:28:38.337 |AppInfo  |-->HTTPConnection::wait_SdlReassociateInd 
00004471.002 |07:28:38.337 |AppInfo  |   HTTPConnection::wait_SdlReassociateInd Received ReassociateIndication from 192.0.2.11
00004471.003 |07:28:38.337 |AppInfo  |<--HTTPConnection::wait_SdlReassociateInd 
00004472.000 |07:28:38.337 |SdlSig   |SdlDataInd                             |wait                           |HTTPConnection(1,600,26,2)       |SdlTCPConnection(1,600,14,67)    |1,600,14,67.2^*^*                        |*TraceFlagOverrode
00004472.001 |07:28:38.337 |AppInfo  |-->HTTPConnection::wait_SdlDataInd 
00004472.002 |07:28:38.337 |AppInfo  |   HTTPConnection::wait_SdlDataInd SdlDataInd recived from TcpPID-[1, 600, 14, 67] ##### 07:28:38.337 || The phone requests SK72f64050-7ad5-4b47-9bfa-5e9ad9cd4aa9.xml.sgn 00004472.003 |07:28:38.337 |AppInfo  |   HTTPConnection::wait_SdlDataInd Printing the HTTPRequest : msgBuffer size [88] --: GET /SK72f64050-7ad5-4b47-9bfa-5e9ad9cd4aa9.xml.sgn HTTP/1.1
Host:198.51.100.0:6970


00004472.004 |07:28:38.337 |AppInfo  |   HTTPConnection::wait_SdlDataInd Proxy Request- 0 , SK72f64050-7ad5-4b47-9bfa-5e9ad9cd4aa9.xml.sgn
00004472.005 |07:28:38.337 |AppInfo  |   HTTPConnection::wait_SdlDataInd Decode successful - Filename is : SK72f64050-7ad5-4b47-9bfa-5e9ad9cd4aa9.xml.sgn
00004472.006 |07:28:38.337 |AppInfo  |   HTTPConnection::wait_SdlDataInd File request signal sent to ServeFile process
00004472.007 |07:28:38.337 |AppInfo  |<--HTTPConnection::wait_SdlDataInd 
00004473.000 |07:28:38.337 |SdlSig   |FileRequest                            |wait                           |ServeFile(1,600,22,1)            |HTTPConnection(1,600,26,2)       |1,600,14,67.2^*^*                        |*TraceFlagOverrode
00004473.001 |07:28:38.337 |AppInfo  |-->ServeFile::wait_FileRequest 
00004473.002 |07:28:38.337 |AppInfo  |   ServeFile::wait_FileRequest Received File request for SK72f64050-7ad5-4b47-9bfa-5e9ad9cd4aa9.xml.sgn with Request ID 47
00004473.003 |07:28:38.337 |AppInfo  |-->ServeFile::validateFileName 
00004473.004 |07:28:38.337 |AppInfo  |   ServeFile::validateFileName File Requested SK72f64050-7ad5-4b47-9bfa-5e9ad9cd4aa9.xml.sgn
00004473.005 |07:28:38.337 |AppInfo  |<--ServeFile::validateFileName 
00004473.006 |07:28:38.337 |AppInfo  |   ServeFile::wait_FileRequest File Validation Success and the File to be Searched is SK72f64050-7ad5-4b47-9bfa-5e9ad9cd4aa9.xml.sgn
00004473.007 |07:28:38.337 |AppInfo  |-->ServeFile::CheckFileIsStatic 
00004473.008 |07:28:38.337 |AppInfo  |   ServeFile::CheckFileIsStatic sk72f64050-7ad5-4b47-9bfa-5e9ad9cd4aa9.xml.sgn is (Not a Static) File
00004473.009 |07:28:38.337 |AppInfo  |<--ServeFile::CheckFileIsStatic 
00004473.010 |07:28:38.337 |AppInfo  |   ServeFile::wait_FileRequest Sending the FileRequest signal to ProcessServeDynamicFile process
00004473.011 |07:28:38.337 |AppInfo  |<--ServeFile::wait_FileRequest 
00004474.000 |07:28:38.337 |SdlSig   |FileRequest                            |wait                           |ServeDynamicFile(1,600,23,4)     |ServeFile(1,600,22,1)            |1,600,14,67.2^*^*                        |*TraceFlagOverrode
00004474.001 |07:28:38.337 |AppInfo  |-->ServeDynamicFile::wait_FileRequest 
00004474.002 |07:28:38.337 |AppInfo  |   ServeDynamicFile::wait_FileRequest Received File request for the dynamic file SK72f64050-7ad5-4b47-9bfa-5e9ad9cd4aa9.xml.sgn
00004474.003 |07:28:38.337 |AppInfo  |-->ServeDynamicFile::isCTLCAPFRequest 
00004474.004 |07:28:38.337 |AppInfo  |   ServeDynamicFile::isCTLCAPFRequest [SK72f64050-7ad5-4b47-9bfa-5e9ad9cd4aa9.xml.sgn] is Not a CTLCAPF File
00004474.005 |07:28:38.337 |AppInfo  |<--ServeDynamicFile::isCTLCAPFRequest 
00004474.006 |07:28:38.337 |AppInfo  |   ServeDynamicFile::wait_FileRequest Requested File is : [sk72f64050-7ad5-4b47-9bfa-5e9ad9cd4aa9.xml.sgn]
00004474.007 |07:28:38.337 |AppInfo  |-->ServeDynamicFile::retrieveTypeOfRequest 
00004474.008 |07:28:38.337 |AppInfo  |   ServeDynamicFile::retrieveTypeOfRequest Request is for XML signed Config File
00004474.009 |07:28:38.337 |AppInfo  |   ServeDynamicFile::retrieveTypeOfRequest File Requested is : [sk72f64050-7ad5-4b47-9bfa-5e9ad9cd4aa9.xml.sgn]
00004474.010 |07:28:38.337 |AppInfo  |<--ServeDynamicFile::retrieveTypeOfRequest 
00004474.011 |07:28:38.337 |AppInfo  |   ServeDynamicFile::wait_FileRequest Type of Request is : [2]
00004474.012 |07:28:38.337 |AppInfo  |-->CServiceModule::getDeviceNameFromRequest 
00004474.013 |07:28:38.337 |AppInfo  |   CServiceModule::getDeviceNameFromRequest File Request without extensions
00004474.014 |07:28:38.337 |AppInfo  |<--CServiceModule::getDeviceNameFromRequest 
00004474.015 |07:28:38.337 |AppInfo  |-->CServiceModule::getIDForRequest 
00004474.016 |07:28:38.337 |AppInfo  |   CServiceModule::getIDForRequest Unable to find device in DB = sk72f64050-7ad5-4b47-9bfa-5e9ad9cd4aa9.xml.sgn
00004474.017 |07:28:38.337 |AppInfo  |<--CServiceModule::getIDForRequest 
00004474.018 |07:28:38.337 |AppInfo  |-->ServeDynamicFile::FindAndServe ##### 07:28:38.337 || SK72f64050-7ad5-4b47-9bfa-5e9ad9cd4aa9.xml.sgn is found 00004474.019 |07:28:38.337 |AppInfo  |   ServeDynamicFile::FindAndServe File Found - 200 - Success
00004474.020 |07:28:38.337 |AppInfo  |   ServeDynamicFile::FindAndServe ServeDynamicFile::wait_dynamicFileRequest [FileName:(SK72f64050-7ad5-4b47-9bfa-5e9ad9cd4aa9.xml.sgn),Content Length:(4963)]
00004474.021 |07:28:38.337 |AppInfo  |   ServeDynamicFile::FindAndServe Request ID : 47
00004474.022 |07:28:38.337 |AppInfo  |<--ServeDynamicFile::FindAndServe 
00004474.023 |07:28:38.337 |AppInfo  |<--ServeDynamicFile::wait_FileRequest 
00004475.000 |07:28:38.337 |SdlSig   |FileResponse                           |wait                           |ServeFile(1,600,22,1)            |ServeDynamicFile(1,600,23,4)     |1,600,14,67.2^*^*                        |*TraceFlagOverrode
00004475.001 |07:28:38.337 |AppInfo  |-->ServeFile::wait_FileResponse 
00004475.002 |07:28:38.337 |AppInfo  |   ServeFile::wait_FileResponse File Response signal received by ServeFile process
00004475.003 |07:28:38.337 |AppInfo  |   ServeFile::wait_FileResponse FileStatus : 1 -- OffClusters Configured : 1 ##### 07:28:38.337 || The TFTP service makes it clear the file was found locally 00004475.004 |07:28:38.337 |AppInfo  |   ServeFile::wait_FileResponse File found in proxy tftp itself. Sending the file response to corresponding connection object
00004475.005 |07:28:38.337 |AppInfo  |<--ServeFile::wait_FileResponse 
00004476.000 |07:28:38.337 |SdlSig   |FileResponse                           |wait                           |HTTPConnection(1,600,26,2)       |ServeFile(1,600,22,1)            |1,600,14,67.2^*^*                        |*TraceFlagOverrode
00004476.001 |07:28:38.337 |AppInfo  |-->HTTPConnection::wait_FileResponse ##### 07:28:38.337 || The file response is sent 00004476.002 |07:28:38.337 |AppInfo  |   HTTPConnection::wait_FileResponse Requested file FOUND... Sending file Response
00004476.003 |07:28:38.337 |AppInfo  |<--HTTPConnection::wait_FileResponse ##### 07:28:38.940 || SdlCloseInd closing the connection for the phone requesting SK72f64050-7ad5-4b47-9bfa-5e9ad9cd4aa9.xml.sgn SdlTCPConnection(1,600,14,67) 00004477.000 |07:28:38.940 |SdlSig   |SdlCloseInd                            |wait                           |HTTPConnection(1,600,26,2)       |SdlTCPConnection(1,600,14,67)    |1,600,14,67.3^*^*                        |*TraceFlagOverrode
00004477.001 |07:28:38.940 |AppInfo  |-->HTTPConnection::wait_SdlCloseInd 
00004477.002 |07:28:38.940 |AppInfo  |   HTTPConnection::wait_SdlCloseInd Recieved CloseInd from TcpConnectionPID-[1, 600, 14, 67]
00004477.003 |07:28:38.940 |AppInfo  |<--HTTPConnection::wait_SdlCloseInd
```

## Related Information

### Revision History

2.0

18-Oct-2022

Aligned document with documentation addressing and domain standards.

1.0

19-Jun-2019

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 18-Oct-2022 | Aligned document with documentation addressing and domain standards. |
| 1.0 | 19-Jun-2019 | Initial Release |