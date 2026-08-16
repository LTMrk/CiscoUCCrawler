---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-im-presence-service-217581-trou-515fb634bf
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-im-presence-service/217581-troubleshoot-im-p-inter-clustering-issue.html
retrieved_at: 2026-08-16T23:38:22.233939+00:00
---

Troubleshoot IM&P Inter-Clustering Issues Caused by DNS Misconfiguration

# Troubleshoot IM&P Inter-Clustering Issues Caused by DNS Misconfiguration

### Download Options

Updated: December 3, 2021

Document ID: 217581

Contents

## Contents

## Introduction

This document describes a scenario where "Not reachable (Check peer address is valid, AXL is running on peer and AXL username/password credentials are valid)" error is received for the Peer Connectivity Test within Cisco Instant Messaging and Presence (IM&P) Server in an intercluster peer scenario.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco IM and Presence Service

- Intercluster peering feature

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

The next image shows the error found within Cisco Unified CM IM and Presence Administration > Presence > Inter-Clustering :

- Both Administrative XML Web Service (AXL) Username and AXL Password are valid.

- Cisco AXL Web Service is running on the peer.

- This Inter-Clustering error is caused by issues with the Domain Name System (DNS) configuration; however, the IM&P traces can mislead the initial triage, as they seem to indicate a possible delay introduced by the network. Simultaneous packet capture collection from both peers would then show that there is no delay in the network whatsoever.

Note : Usually, this is a one-way issue, which means that the IM&P Cluster A is able to successfully communicate with the IM&P Cluster B, but the IM&P Cluster B throws the Not reachable error when it tries to communicate with IM&P Cluster A.

## Troubleshoot

Step 1. Verify that the AXL Usernames, AXL Passwords, and Peer Addresses are all correct. In this scenario, connectivity is not a problem and peers must be able to communicate in both ways (they must not only be pingable but also reachable through the corresponding AXL ports: 8443).

Step 2. Collect at least these set of logs from both IM&P Cluster A and B:

- Cisco AXL Web Service

- Cisco Intercluster Sync Agent

Caution : Some service traces require to be set to debug level before the test is performed. Set the trace level to its default state after the tests are performed to avoid any further impact on the performance of the servers.

Note : It is important to gather the logs from both clusters involved.

The path to enable Debug level for each service is:

- Cisco Unified IM and Presence Serviceability > Trace > Configuration > Select IM&P Server and click Go > Select Database and Admin Services and click Go > Select Cisco AXL Web Service and click Go

- Cisco Unified IM and Presence Serviceability > Trace > Configuration > Select IM&P Server and click Go > Select IM and Presence Services and click Go > Select Cisco Intercluster Sync Agent and click Go

Step 3. The log analysis shows this message flow:

From the Intercluster Sync Agent logs in Cluster B (the cluster which shows the Not reachable error), you need to identify the AXL request and the exact time at which such request was sent. It looks something like this:

```
2019-07-14 06:00:07,842 DEBUG [Peer: node name in Cluster A] axl.AXLClientLogger - runSoapReq: The axl request is : <?xml version="1.0" encoding="UTF-8" standalone="no"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.cisco.com/AXL/API/8.0"><SOAP-ENV:Header/><SOAP-ENV:Body><ns:executeSQLQuery sequence="{color:red}1563080407841{color}"><sql>SELECT count(*) from processnode WHERE systemnode='f' and tknodeusage= 0</sql></ns:executeSQLQuery></SOAP-ENV:Body></SOAP-ENV:Envelope>
```

The same Intercluster Sync Agent logs in the Cluster B show that the response is received until two minutes later, which causes a timeout for the transaction:

```
019-07-14 06:02:36,176 DEBUG [AXL Runner for parent thread ID:4741 (Peer: node name in Cluster A] axl.AXLClientLogger - AXLClientBase - sendSOAPRequest received : <?xml version="1.0" encoding="UTF-8"?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><soapenv:Body><ns:executeSQLQueryResponse xmlns:ns="http://www.cisco.com/AXL/API/8.0" sequence="{color:red}1563080407841{color}"><return><row><count>2</count></row></return></ns:executeSQLQueryResponse></soapenv:Body></soapenv:Envelope>
"node name in Cluster A" received AXL request at "2019-07-14 01:02:36"
```

This could lead you to suspect that there is some sort of packet delay within the network. However, the response's body itself indicates that the peer in Cluster A received an AXL request two minutes later (you need to effectuate the time zone conversion if the clusters are located in different time zones).

If you look into AXL Web Service logs in Cluster A, you can find that the request is processed in a matter of milliseconds:

```
2019-07-14 01:02:36,110 INFO  [http-bio-443-exec-742] servletRouters.AXLFilter - AXL REQUEST : 
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.cisco.com/AXL/API/8.0"><SOAP-ENV:Header/><SOAP-ENV:Body><ns:executeSQLQuery sequence="{color:red}1563080407841{color}"><sql>SELECT count(*) from processnode WHERE systemnode='f' and tknodeusage= 0</sql></ns:executeSQLQuery></SOAP-ENV:Body></SOAP-ENV:Envelope>
"node name in Cluster A" sent response at "2019-07-14 01:02:36"
```

```
2019-07-14 01:02:36,131 DEBUG [http-bio-443-exec-742] servletRouters.AXLFilter - Final response String  : <?xml version='1.0' encoding='utf-8'?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><soapenv:Body><ns:executeSQLQueryResponse sequence="{color:red}1563080407841{color}" xmlns:ns="http://www.cisco.com/AXL/API/8.0"><return><row><count>2</count></row></return></ns:executeSQLQueryResponse></soapenv:Body></soapenv:Envelope>
```

Simultaneous packet captures from both peers demonstrate the same: the actual delay is not within the network itself, but the issue is that Cluster B delays the packet before it is sent out to Cluster A. Cluster A processes the request and replies to it in a few milliseconds, as expected.

The investigation as to why Cluster B delays the AXL request or what is the exact cause for this issue could be very time-consuming. However, there are a couple of validations that have been identified as basic diagnosis steps for this scenario.

## Workaround

There have been multiple cases where this delay within IM&P Cluster B is caused by an issue with the DNS. You could face either of these two scenarios:

Scenario 1:

In Cluster B, the Primary DNS server is not reachable. Although the Secondary DNS server is reachable, the node has taken a significant delay when it attempted to resolve all required FQDNs via the Primary DNS server. By the time it changes to the Secondary DNS server, there is already a 2-minute delay and, therefore, the request times out.

The way you can validate this is via these Command Line Interface (CLI) commands :

Issue the show network eth0 command to list the DNS servers IM&P node is configured to use:

```
admin:show network eth0
Ethernet 0
DHCP         : disabled           Status     : up
IP Address   : 10.0.10.10         IP Mask    : 255.255.255.000
Link Detected: yes                Mode       : Auto disabled, Full, 10000 Mbits/s
Duplicate IP : no

DNS
Primary      : 10.0.10.31         Secondary  : 10.0.10.32
```

Then, try to ping the Primary DNS server via the utils network ping <Primary DNS server's IP Address> command:

```
admin:utils network ping 10.0.10.31
PING 10.0.10.31 (10.0.10.31) 56(84) bytes of data.
From 10.0.10.10 icmp_seq=2 Destination Host Unreachable
From 10.0.10.10 icmp_seq=3 Destination Host Unreachable
From 10.0.10.10 icmp_seq=4 Destination Host Unreachable
```

If the Primary DNS server is not reachable, ensure that the IP Address that was configured for it is correct. Then, fix all connectivity issues. Once you are able to ping both Primary and Secondary DNS servers without issues, the Inter-Clustering error must also be fixed. In case the issue persists after these actions, go through the steps from Scenario 2.

Scenario 2:

In Cluster B, both Primary and Secondary DNS servers are reachable/pingable, but the IM&P server still shows a DNS unreachable warning in the CLI and web page:

```
Command Line Interface is starting up, please wait ...

   Welcome to the Platform Command Line Interface

VMware Installation:
        128 vCPU: Intel(R) Xeon(R) CPU E5-2699A v4 @ 2.40GHz
        Disk 1: 80GB, Partitions aligned
        4096 Mbytes RAM
        WARNING: DNS unreachable
```

Also, the CLI command utils diagnose test shows an issue with DNS resolution, specifically within the validate_network module, which could indicate an error such as Reverse DNS lookup failed :

```
admin:utils diagnose test
Log file: platform/log/diag4.log

Starting diagnostic test(s)
===========================
test - disk_space          : Passed (available: 6938 MB, used: 11852 MB)
skip - disk_files          : This module must be run directly and off hours
test - service_manager     : Passed
test - tomcat              : Passed
test - tomcat_deadlocks    : Passed
test - tomcat_keystore     : Passed
test - tomcat_connectors   : Passed
test - tomcat_threads      : Passed
test - tomcat_memory       : Passed
test - tomcat_sessions     : Passed
skip - tomcat_heapdump     : This module must be run directly and off hours
test - validate_network    : Reverse DNS lookup failed
test - raid                : Passed
```

This particular error indicates an issue with the DNS server, which is unable to resolve some IP addresses to Fully Qualified Domain Names (FQDNs). You can further isolate this issue via the CLI command show network cluster . This command displays the list of entries (All CUCM and IM&P servers) that are part of that cluster:

```
admin:show network cluster
10.3.74.13 IMPPUB.edgrodrilab.com IMPPUB Subscriber cups DBPub authenticated
10.3.74.14 IMPSUB.edgrodrilab.com IMPSUB Subscriber cups DBSub authenticated using TCP since Fri Oct 15 10:22:20 2021
10.3.74.12 CUCMSUB.edgrodrilab.com CUCMSUB Subscriber callmanager DBSub authenticated using TCP since Thu Oct 28 11:24:16 2021
10.3.74.11 CUCMPUB.edgrodrilab.com CUCMPUB Publisher callmanager DBPub authenticated using TCP since Thu Oct 28 11:27:36 2021
```

You must be able to do forward and reverse DNS lookup on all of those entries.

Example of a working DNS resolution:

```
admin:utils network host IMPPUB
Local Resolution:
IMPPUB.edgrodrilab.com resolves locally to 10.0.10.10

External Resolution:
IMPPUB.edgrodrilab.com has address 10.0.10.10

admin:utils network host 10.0.10.10
Local Resolution:
10.0.10.10 resolves locally to IMPPUB.edgrodrilab.com

External Resolution:
10.10.0.10.in-addr.arpa domain name pointer imppub.edgrodrilab.com.
```

Example of a non-working DNS resolution:

```
admin:utils network host IMPSUB
Local Resolution:
IMPSUB.edgrodrilab.com resolves locally to 10.0.10.10

External Resolution:
IMPSUB.edgrodrilab.com has address 10.0.10.10

admin:utils network host 10.0.10.10
Local Resolution:
10.0.10.10 resolves locally to IMPSUB.edgrodrilab.com

External Resolution:
No external servers found
```

In this specific case, the DNS server does not contain the PTR record to resolve from 10.0.10.10 IP address to IMPSUB.edgrodrilab.com FQDN.

To fix the DNS unreachable warning and the Reverse DNS lookup failed error, you need to create the required A Host and PTR records in the DNS server to be able to resolve all the CUCM and IM&P nodes for both forward and reverse DNS lookup.

## Verify

When exact same Inter-Clustering issue is experienced and the error signature matches the logs, one of the basic settings to check is the DNS server status and configuration.

Both Primary and Secondary DNS servers need to be reachable/pingable and able to resolve all of the CUCM and IM&P nodes within the cluster for forward and reverse DNS lookup.

You need to clear all the DNS warnings, errors, or alerts before troubleshoot the Inter-Clustering errors. You can use the utils diagnose test command to validate DNS configuration.

### Revision History

1.0

03-Dec-2021

Initial Release

### Contributed by Cisco Engineers

Edgar Rodriguez

Cisco TAC

### This Document Applies to These Products

- Unified Communications Manager IM & Presence Service

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 03-Dec-2021 | Initial Release |