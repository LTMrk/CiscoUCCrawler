---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-200694-configure-an-91bdace4ad
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/200694-Configure-and-Troubleshoot-Joining-Clust.html
retrieved_at: 2026-08-21T13:55:42.838336+00:00
---

Configure and Troubleshoot Joining Clusters for ILS

# Configure and Troubleshoot Joining Clusters for ILS

### Download Options

Updated: September 28, 2016

Document ID: 200694

Contents

## Contents

## Introduction

This document describes the possible configuration methods to join Clusters for Intercluster Lookup Service (ILS) also log analysis to troublshoot each the methods.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

The information in this document is based on these software and hardware versions:

- Cisco Unified Communications Manager (CUCM) Version 11.5

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

### Network Diagram

﻿

### Configurations

#### Method 1. Using Password Authentication between Clusters

Log in to CUCM Administration Page, navigate to Advanced Features > ILS Configuration . In the ILS Configuration window, check the Use Password check box. Manage the passwords then hit Save . The password must be same across all clusters in the ILS network.

﻿

#### Method 2. Using TLS Authentication between Clusters

To use this method, ensure that all clusters that to be a part of ILS Network have imported the remote clusters Tomcat Certificates in its tomcat-trust. In CUCM Administration, navigate to Advanced Features > ILS Configuration . In the ILS Configuration window, check the Use TLS Certificates check box under ILS Authentication.

﻿

#### Method 3. Use TLS with Password Authentication between Clusters .

The advantage of this method is that no need to cross import the Tomcat Certificates between the clusters to establish the TLS connection if it’s signed by External Certificate Authority(CA). This method is available from CUCM 11.5 and later. To use this method, ensure that all clusters that to be a part of ILS Network have the tomcat certificates signed by an External CA and the root certificate of this CA is present in tomcat-trust. Also, the password must be same across all clusters in the ILS network.

In CUCM Administration, navigate to Advanced Features > ILS Configuration Under ILS Authentication, check the Use TLS Certificates and Use Password check box.

﻿ ﻿

#### Method 4. Switching to TLS Authentication after cluster is joined with Password authentication.

This is another way to use TLS without cross importing the Tomcat Certificates between the clusters if it’s signed by External CA. This is useful for CUCM versions prior 11.5 where method 3 is not supported.

To use this method, ensure that all clusters that to be a part of ILS Network have the tomcat certificates signed by an External CA and the root certificate of this CA is present in tomcat-trust.

Join the cluster first using the Password Authentication. In Cisco Unified CM Administration, navigate to Advanced Features > ILS Configuration . Under ILS Authentication, check Use Password check box. Manage the Passwords. Click Save .

The password must be same in client and server side at the time of joining the cluster.

﻿

Once the Connection is established, change the authentication method to TLS.  In CUCM Administration, navigate to Advanced Features > ILS Configuration . In the ILS Configuration window, check the Use TLS Certificates check box under ILS Authentication.

﻿

## Verify

Successful registration can be seen under ILS Clusters and Global DialPlan Imported Catalogs in

Advanced Features > ILS Configuration

﻿

Remote cluster details are listed using command run sql select * from remotecluster

﻿

## Troubleshoot

Set the debug trace level for Cisco Intercluster Lookup Service to detailed .

Location for the Trace :  activelog /cm/trace/ils/sdl/

The log analysis for Success and Failure scenarios for each ILS registration methods with example ar explained.

### Log Analysis for ILS Registration for Method 1

#### Spoke Registers Succesfully to the Hub using Password Authentication between Clusters

Log Snippet from Hub:

```
00154617.001 |16:58:42.888 |AppInfo  |IlsD IlsHandler: Ils::wait_SdlConnectionInd(): New connection accepted. DeviceName=, TCPPid = [1.600.13.5], IPAddr=10.106.104.201, Port=37816, Controller=[1,20,1]
 
00154617.002 |16:58:42.888 |AppInfo  |IlsD Ils::ConnectInd TCPPid([1, 600, 13, 5]), PeerIP/Port(10.106.104.201:37816), LocalIP/Port(10.106.104.220:7502) (10.106.104.201:37816)
 
00154618.012 |16:58:42.889 |AppInfo  |IlsD ::ConnectIndInner Server Connection to PeerId(f7f885dcaca845f18f3b7e583ff6c457), TCPPid([1, 600, 13, 5]), PeerIP/Port(10.106.104.201:37816), LocalIP/Port(10.106.104.220:7502) TLSReq(f) established
```

Log snippet from Spoke:

```
00145095.017 |16:58:42.878 |AppInfo  |IlsD Ils::ConnectReq(): Requesting Connection to IpAddr(10.106.104.220), IpPort(7502), TLSReq(f)

00145095.018 |16:58:42.878 |AppInfo  |IlsD Ils::ConnectReq() Pub IP/Port(10.106.104.220:7502) Pri IP/Port(:7502) TLSReq(false)
 
00145095.024 |16:58:42.879 |AppInfo  |IlsD Ils::processConnectReq Initiating non-TLS Connection
 
00145096.001 |16:58:42.881 |AppInfo  |IlsD Ils::ConnectRes() appCorr(1029) TCPPid([1, 600, 13, 5]), PeerIP/Port(10.106.104.220:7502), LocalIP/Port(10.106.104.201:37816) TLSReq(f) found
 
00145096.002 |16:58:42.881 |AppInfo  |IlsD DEBUG(0000FA0E): Client Connection to peerId(00000000000000000000000000000000) ipAddr(10.106.104.220) ipPort(7502) TLSReq(f) succeeded
 
00145097.010 |16:58:42.896 |AppInfo  |IlsD ::ConnectIndInner starting  to PeerId(77c59d0960cc4fdc959168a3d686a6de), TCPPid([1, 600, 13, 5]), PeerIP/Port(10.106.104.220:7502), LocalIP/Port(10.106.104.201:37816) TLSReq(f) established
```

#### Spoke to Tries to Register to Hub but it fails due to the password mismatch

DecryptData failed and ILSPwdAuthenticationFailed alarm in the Hub logs indicates the mismatch of the password.

Log snippet from Hub:

```
00155891.005 |17:25:26.197 |AppInfo  |IlsD IlsHandler: wait_SdlDataInd EncrUtil:: decryptData failed . DeviceName=, TCPPid = [1.600.13.7], IPAddr=10.106.104.201, Port=40592, Controller=[1,20,1]
 
 00155891.006 |17:25:26.197 |AppInfo  |IlsD wait_SdlDataInd sending ILSPwdAuthenticationFailed alarm with IPAddress= 10.106.104.201; mAlarmedConnections count= 1
```

Note : The error is same in rest of the methods too whenever connection fails due to password mismatch.

### Log Analysis for ILS Registration for Method 2

#### Spoke Registers Succesfully to the Hub using TLS Authentication

Log snippet from Hub:

```
00000901.001 |15:46:27.238 |AppInfo  |IlsD Ils::VerifyCertificateInfo(): peer certificates are in certificate store
 
00000902.008 |15:46:27.240 |AppInfo  |IlsD ::ConnectIndInner Server Connection to PeerId(f7f885dcaca845f18f3b7e583ff6c457), TCPPid([1, 600, 17, 4]), PeerIP/Port(10.106.104.201:60938), LocalIP/Port(10.106.104.220:7501) TLSReq(t) established
```

Log Snippet from Spoke:

```
00000646.001 |15:46:27.189 |AppInfo  |IlsD Ils::VerifyCertificateInfo(): peer certificates are in certificate store
 
00000647.006 |15:46:27.199 |AppInfo  |IlsD ::ConnectIndInner starting  to PeerId(77c59d0960cc4fdc959168a3d686a6de), TCPPid([1, 600, 17, 3]), PeerIP/Port(10.106.104.220:7501), LocalIP/Port(10.106.104.201:36115) TLSReq(t) established
```

#### Connection Fails as Tomcat Certificate of the Hub is not imported in Spoke

Log from Spoke indicates that the Certificate Verification for the Hub is failed.

Log snippet from Spoke:

```
00001821.000 |16:34:01.765 |AppInfo  |[1, 600, 17, 5]: HandleSSLError - Certificate verification failed:(Verification error:18)- self signed certificate for 10.106.104.220:7501
 
00001822.000 |16:34:01.765 |AppInfo  |[1, 600, 17, 5]: HandleSSLError - Certificate verification failed for 10.106.104.220:7501
 
00001827.002 |16:34:01.766 |AppInfo  |IlsD Ils::wait_SdlConnectErrRsp sending ILSTLSAuthenticationFailed alarm with Cluster1 = 10.106.104.220; mAlarmedConnections count= 1
 
00001827.004 |16:34:01.770 |AppInfo  |IlsD ERROR(000005C9): Connection to peerId(00000000000000000000000000000000) ipAddr(10.106.104.220) ipPort(7501) TLSReq(t) failed, ConnReason(1)
```

#### Connection Fails as Tomcat Certificate of the Spoke is not imported in Hub

Logs from the hub indicates that connection is closed as neither Certificate of the Spoke in local store nor FQDN in the peer info vector.

Log Snippet from Hub:

```
00003366.001 |17:06:30.877 |AppInfo  |CertUtil Ils::isCertInLocalStore X509_STORE_get_by_subject failed.
 
00003366.002 |17:06:30.877 |AppInfo  |IlsD Ils::VerifyCertificateInfo(): certificate is not in the local store and the FQDN (cucm11.adfs.ucce.com) is not in the peer info vector, closing the connection
 
00003366.003 |17:06:30.877 |AppInfo  |IlsD Ils::VerifyCertificateInfo(): sending ILSTLSAuthenticationFailed alarm for Cluster1= cucm11.adfs.ucce.com; mAlarmedConnections count= 1
 
00003366.004 |17:06:30.882 |AppInfo  |IlsD IlsHandler: Close Req. DeviceName=, TCPPid = [1.600.17.16], IPAddr=10.106.104.201, Port=39267, Controller=[1,20,1
```

### Log Analysis for ILS Registration for Method 3

#### Spoke Registers Succesfully to the Hub using TLS with Password Authentication

Log snippet from Hub:

```
00000211.001 |08:06:58.798 |AppInfo  |CertUtil Ils::isCertInLocalStore X509_STORE_get_by_subject failed.
 
00000211.002 |08:06:58.798 |AppInfo  |IlsD Ils::VerifyCertificateInfo(): peer certificates are not in certificate store but Root CA signed certs are uploaded locally
 
00000212.001 |08:06:58.803 |AppInfo  |EncrUtil Function: decryptData at line 163 succedded
 
00000212.002 |08:06:58.803 |AppInfo  |EncrUtil Function: decryptData at line 165 succedded
 
00000212.003 |08:06:58.803 |AppInfo  |EncrUtil Function: decryptData at line 168 succedded
 
00000212.004 |08:06:58.803 |AppInfo  |EncrUtil decryptData: inlen 1956, outlen 1949 succeed
 
00000212.012 |08:06:58.804 |AppInfo  |IlsD ::ConnectIndInner Server Connection to PeerId(f7f885dcaca845f18f3b7e583ff6c457), TCPPid([1, 600, 17, 1]), PeerIP/Port(10.106.104.201:56181), LocalIP/Port(10.106.104.220:7501) TLSReq(t) established
```

Log snippet from Spoke:

```
00000064.000 |08:06:58.802 |SdlSig   |SdlConnectRsp                          |wait                           |Ils(1,600,20,1)                 
|SdlSSLTCPConnection(1,600,17,1)  |1,600,16,1.1^*^*                         |*TraceFlagOverrode
 
00000064.001 |08:06:58.802 |AppInfo  |CertUtil Ils::isCertInLocalStore X509_STORE_get_by_subject failed.
 
00000064.002 |08:06:58.802 |AppInfo  |IlsD Ils::VerifyCertificateInfo(): peer certificates are not in certificate store but Root CA signed certs are uploaded locally.
 
00000064.004 |08:06:58.802 |AppInfo  |IlsD DEBUG(00000407): Client Connection to peerId(00000000000000000000000000000000) ipAddr(10.106.104.220) ipPort(7501) TLSReq(t) succeeded
 
00000065.010 |08:06:58.812 |AppInfo  |IlsD ::ConnectIndInner starting  to PeerId(77c59d0960cc4fdc959168a3d686a6de), TCPPid([1, 600, 17, 1]), PeerIP/Port(10.106.104.220:7501), LocalIP/Port(10.106.104.201:56181) TLSReq(t) established
```

#### Connection Fails as Tomcat Certificate of the Spoke is Self Signed

Logs from Hub Indicates Certificate Verification failure for Self-Signed Certificate of the Spoke.

Log Snippet from Hub:

```
00000103.000 |09:44:16.896 |AppInfo  |[1, 600, 17, 1]: HandleSSLError - Certificate verification failed:(Verification error:18)-
self signed certificate for 10.106.104.201:52124
 
00000104.000 |09:44:16.896 |AppInfo  |[1, 600, 17, 1]: HandleSSLError - Certificate verification failed for 10.106.104.201:52124
 
00000106.000 |09:44:16.896 |AppInfo  |[1, 600, 17, 1]: HandleSSLError - TLS protocol error(ssl reason code=internal error [68]),lib=SSL routines [20],fun=SSL_clear [164], errno=0 for 10.106.104.201:52124
```

#### Connection Fails as Tomcat Certificate of the Hub  is Self Signed

Logs from Spoke indicates Certificate Verification faulure for Self-Signed Certificate of the Hub.

Log Snippet from Spoke:

```
00000064.000 |12:44:19.641 |AppInfo  |[1, 600, 17, 1]: HandleSSLError - Certificate verification failed:(Verification error:18)- self signed certificate for 10.106.104.220:7501
 
00000065.000 |12:44:19.641 |AppInfo  |[1, 600, 17, 1]: HandleSSLError - Certificate verification failed for 10.106.104.220:7501
 
00000067.000 |12:44:19.641 |AppInfo  |[1, 600, 17, 1]: HandleSSLError - TLS protocol error(ssl reason code=bad message type [114]),lib=SSL routines [20],fun=ssl3_get_server_hello [146], errno=0 for 10.106.104.220:7501
```

Note : The error seen in this case is also same when both hub and spoke have self signed.

### Log Analysis for ILS Registration for Method 4

#### Spoke Registers Succesfully to the Hub when switching to TLS Authenitication from the established connection using Password Authentication.

FQDN of the remote cluster presented in the PeerInfoVector as the connection is already established with password authentication method.  When switching to TLS from password authentication method, “ X509_STORE_get_by_subject failed” error is printed in the logs since tomcat certificate is not cross imported. But, the connection still accepted using TLS since “FQDN is in PeerInfoVector”.

Log snippet from Hub:

```
00000169.001 |19:41:50.255 |AppInfo  |CertUtil Ils::isCertInLocalStore X509_STORE_get_by_subject failed.
 
00000169.002 |19:41:50.255 |AppInfo  |IlsD Ils::VerifyCertificateInfo(): FQDN is in PeerInfoVector
 
00000169.003 |19:41:50.255 |AppInfo  |IlsD IlsHandler: Ils::wait_SdlConnectionInd(): New connection accepted. DeviceName=, TCPPid = [1.600.17.1], IPAddr=10.106.104.201, Port=51887, Controller=[1,20,1]
```

Log snippet from Spoke:

```
00000072.001 |19:41:50.257 |AppInfo  |CertUtil Ils::isCertInLocalStore X509_STORE_get_by_subject failed.
 
00000072.002 |19:41:50.257 |AppInfo  |IlsD Ils::VerifyCertificateInfo(): FQDN is in PeerInfoVector
```

#### Connection Fails as Hub has Self Signed Certificate when switching to TLS Authenitication from the established connection using Password Authentication.

Logs from Spoke indicates Certificate Verification failure for Self-Signed Certificate of the Hub.

Log snippet from Spoke:

```
00000151.000 |12:29:18.600 |AppInfo  |[1, 600, 17, 2]: HandleSSLError - Certificate verification failed:(Verification error:18)- self signed certificate for 10.106.104.220:7501
 
00000152.000 |12:29:18.600 |AppInfo  |[1, 600, 17, 2]: HandleSSLError - Certificate verification failed for 10.106.104.220:7501
```

#### Connection Fails as Spoke has Self Signed Certificate when switching to TLS Authenitication from the established connection using Password Authentication.

Logs from Hub indicates Certificate Verification failure for Self-Signed Certificate of the Spoke

Log snippet from Hub:

```
00000089.000 |09:32:27.365 |AppInfo  |[1, 600, 17, 1]: HandleSSLError - Certificate verification failed:(Verification error:18)- self signed certificate for 10.106.104.201:41295
 
00000090.000 |09:32:27.365 |AppInfo  |[1, 600, 17, 1]: HandleSSLError - Certificate verification failed for 10.106.104.201:41295
```