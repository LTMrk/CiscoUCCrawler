---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-213481-configure-verify-and-troubleshoot-multi-html-19f503c74d
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/213481-configure-verify-and-troubleshoot-multi.html
retrieved_at: 2026-08-21T13:12:20.190812+00:00
---

Configure Multiple CMS WebBridges via Expressway

# Configure Multiple CMS WebBridges via Expressway

### Download Options

Updated: May 28, 2020

Document ID: 213481

Contents

## Contents

## Introduction

This document describes the steps to configure, verify and troubleshoot Cisco Meeting Server (CMS) multiple WebBridges (WB) over Expressway for WebRTC.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Expressway X8.11 and above

- CMS server 2.3 and above

- Network Address Translation (NAT)

- Traversal Using Relays around NAT (TURN)

- Session Traversal Utilities for NAT (STUN)

- Domain Name System (DNS)

Configuration prerequisites:

- In order to refer to a guide for a single WB proxy via Expressway, click here

- Database clustering of all CMS nodes, click here for the configuration guide

- WB, Extensible Messaging and Presence Protocol (XMPP) and CallBridge (CB) configured and enabled on CMS, click here for the configuration guide

- Clustering of the CB nodes, click here for the configuration guide

### Components Used

- Expressway X8.11

- CMS 2.3.4 (3 Nodes)

The information in this document was created from the devices in a specific lab environment. If your setup is live, ensure that you understand the potential impact of any command or configuration changes.

## Background Information

Support of WebRTC proxy with multiple WB via Expressway has been added to Expressway from version X8.11, which enables the redundancy and load balancing across WB.

In versions prior to X8.11 only load balancing is supported and connections fail when the WB chosen by the Expressway is down.

Expressway-C discovers the WB IP addresses by querying DNS with the use of the Guest account client URI , and from X8.11, then uses round-robin to distribute WebRTC connections evenly amongst those WBs.

Expressway-C now maintains a dynamic list of IP addresses that it knows are WB with the use of these processes:

- It queries the DNS (every 60 minutes approximately) with the use of the ( Guest account client URI ) in order to detect any deliberate changes to your deployment; for example, host addresses being added to or removed from the Service (SRV) record

- It then probes the host addresses returned by DNS to check if they are reachable and that they are WB (with the use of an API call)

- If an address is not reachable, or the host is not a WB, then the Expressway-C stops to send WebRTC connections to that address and such addresses are marked with the Failed status on CMS page on the Expressway-C

Note : This document focuses on the multiple WB integration onto the Expressway and not the complete configuration of the WebRTC proxy which is covered in the guide on the first bullet point on the Configuration prerequisites.

## Configure

### Network Diagram

### Configurations

1. Configure these DNS SRV records for each WB nodes to which the Guest account client URI resolves:

In this example, the following applies:

Guest account client URI: joinext.vngtp.cms

WB1 FQDN: cmsvngtp.vngtp.cms

WB2 FQDN: cms2.vngtp.cms

WB3 FQDN: cmsdb.vngtp.cms

Note : The below assumes that cmsdb.vngtp.cms has more capacity than the other callbridges so the priority is lower to allow more connections to go there from the Expressway-C.

These DNS SRV records are configured for each host Fully Qualified Domain Name ( FQDN):

Example from DNS server:

Note : To allow for better load balancing of WebRTC connections via Expressway (assuming that all the servers have the same capacity) ensure that the priority and weight are the same for all the SRV records above, see below example:

2. Integrate WB onto Expressway-C with the use of the external FQDN (to be used by the external party):

- Navigate to Configuration > Unified Communications > Cisco Meeting Server

- Enter the FQDN in the Guest account client URI

- Then select Save

An example is shown on this image:

## Verify

Use this section in order to confirm that your configuration works properly.

Check to ensure that the Expressway-C has been able to connect to all the WB to which the FQDN resolves.

Navigate to Configuration > Unified Communications > Cisco Meeting Server .

Once the Expresssway-C has been able to reach the WB, the Status will be Active , as shown in this image:

Some log review of what happens when the WB is added to the Expressway-C:

a. Expressway-C creates an object UUID for the Webbridge FQDN on its database for the command executions:

```
2018-07-09T14:09:10.773+02:00 vcsc httpd[8724]: web: Event="System Configuration Changed" Detail="commands/ cmsadd /uuid - created with value: ' d86cf754-dc5c-438f-900f-51e5c702b94e '" Src-ip="192.168.1.5" Src-port="51223" User="admin" Level="1" UTCTime="2018-07-09 12:09:10" 
2018-07-09T14:09:10.773+02:00 vcsc httpd[8724]: web: Event="System Configuration Changed" Detail="commands/ cmsadd /time_started - created with value: '0'" Src-ip="192.168.1.5" Src-port="51223" User="admin" Level="1" UTCTime="2018-07-09 12:09:10" 
2018-07-09T14:09:10.773+02:00 vcsc httpd[8724]: web: Event="System Configuration Changed" Detail="commands/ cmsadd /time_finished - created with value: '0'" Src-ip="192.168.1.5" Src-port="51223" User="admin" Level="1" UTCTime="2018-07-09 12:09:10" 
2018-07-09T14:09:10.773+02:00 vcsc httpd[8724]: web: Event="System Configuration Changed" Detail="commands/ cmsadd /command_state - created with value: 'queued'" Src-ip="192.168.1.5" Src-port="51223" User="admin" Level="1" UTCTime="2018-07-09 12:09:10" 
2018-07-09T14:09:10.773+02:00 vcsc httpd[8724]: web: Event="System Configuration Changed" Detail="commands/ cmsadd /command_error - created with value: ''" Src-ip="192.168.1.5" Src-port="51223" User="admin" Level="1" UTCTime="2018-07-09 12:09:10" 
2018-07-09T14:09:10.773+02:00 vcsc httpd[8724]: web: Event="System Configuration Changed" Detail="commands/ cmsadd /name - created with value: ' joinext.vngtp.cms '" Src-ip="192.168.1.5" Src-port="51223" User="admin" Level="1" UTCTime="2018-07-09 12:09:10"
```

b. Queries DNS for the SRV records _cms-web._tls.<WB_FQDN> , in this example _cms web._tls.joinext.vngtp.cms :

```
205	2018-07-09 12:09:11.029	192.168.1.64	192.168.1.61	DNS	91	Standard query 0xfb10 SRV _cms-web._tls.joinext.vngtp.cms 206	2018-07-09 12:09:11.032	192.168.1.61	192.168.1.64	DNS	246	Standard query response 0xfb10 SRV _cms-web._tls.joinext.vngtp.cms SRV 15 1 443 cms2.vngtp.cms SRV 20 1 443 cmsvngtp.vngtp.cms SRV 10 1 443 cmsdb.vngtp.cms A 192.168.1.211 A 192.168.1.66 A 192.168.1.212
```

c. Creates individual entries in its database for each WB in relation to the external join URI used to integrate them:

```
2018-07-09T14:09:11.187+02:00 vcsc UTCTime="2018-07-09 12:09:11,187" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid cb7d5de8-1ab3-4a0d-a52a-8dbc885effeb name: joinext.vngtp.cms name: joinext.vngtp.cms"
2018-07-09T14:09:11.187+02:00 vcsc UTCTime="2018-07-09 12:09:11,187" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid cb7d5de8-1ab3-4a0d-a52a-8dbc885effeb name: joinext.vngtp.cms guid: 81db7b67-2aa9-4f64-8d74-04c4037397a8 "
2018-07-09T14:09:11.187+02:00 vcsc UTCTime="2018-07-09 12:09:11,187" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid cb7d5de8-1ab3-4a0d-a52a-8dbc885effeb name: joinext.vngtp.cms dnsname: cms2.vngtp.cms "
2018-07-09T14:09:11.187+02:00 vcsc UTCTime="2018-07-09 12:09:11,187" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid cb7d5de8-1ab3-4a0d-a52a-8dbc885effeb name: joinext.vngtp.cms address: 192.168.1.211 "
2018-07-09T14:09:11.187+02:00 vcsc UTCTime="2018-07-09 12:09:11,187" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid cb7d5de8-1ab3-4a0d-a52a-8dbc885effeb name: joinext.vngtp.cms priority: 15"
2018-07-09T14:09:11.187+02:00 vcsc UTCTime="2018-07-09 12:09:11,187" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid cb7d5de8-1ab3-4a0d-a52a-8dbc885effeb name: joinext.vngtp.cms weight: 1"
2018-07-09T14:09:11.187+02:00 vcsc UTCTime="2018-07-09 12:09:11,187" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid cb7d5de8-1ab3-4a0d-a52a-8dbc885effeb name: joinext.vngtp.cms port: 443"

2018-07-09T14:09:11.193+02:00 vcsc UTCTime="2018-07-09 12:09:11,193" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 0408bdd0-9ada-45a0-834d-ccda166e8006 name: joinext.vngtp.cms name: joinext.vngtp.cms"
2018-07-09T14:09:11.193+02:00 vcsc UTCTime="2018-07-09 12:09:11,193" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 0408bdd0-9ada-45a0-834d-ccda166e8006 name: joinext.vngtp.cms guid: 97d8fa86-7de4-4410-9767-7bc8b1eeaced "
2018-07-09T14:09:11.193+02:00 vcsc UTCTime="2018-07-09 12:09:11,193" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 0408bdd0-9ada-45a0-834d-ccda166e8006 name: joinext.vngtp.cms dnsname: cmsvngtp.vngtp.cms "
2018-07-09T14:09:11.193+02:00 vcsc UTCTime="2018-07-09 12:09:11,193" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 0408bdd0-9ada-45a0-834d-ccda166e8006 name: joinext.vngtp.cms address: 192.168.1.66 "
2018-07-09T14:09:11.193+02:00 vcsc UTCTime="2018-07-09 12:09:11,193" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 0408bdd0-9ada-45a0-834d-ccda166e8006 name: joinext.vngtp.cms priority: 20"
2018-07-09T14:09:11.193+02:00 vcsc UTCTime="2018-07-09 12:09:11,193" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 0408bdd0-9ada-45a0-834d-ccda166e8006 name: joinext.vngtp.cms weight: 1"
2018-07-09T14:09:11.193+02:00 vcsc UTCTime="2018-07-09 12:09:11,193" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 0408bdd0-9ada-45a0-834d-ccda166e8006 name: joinext.vngtp.cms port: 443"

2018-07-09T14:09:11.206+02:00 vcsc UTCTime="2018-07-09 12:09:11,206" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid b151839e-a0dd-4176-bbed-ad28e05e9283 name: joinext.vngtp.cms name: joinext.vngtp.cms"
2018-07-09T14:09:11.206+02:00 vcsc UTCTime="2018-07-09 12:09:11,206" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid b151839e-a0dd-4176-bbed-ad28e05e9283 name: joinext.vngtp.cms guid: 9c788380-6601-4dba-96e0-739511728369 "
2018-07-09T14:09:11.206+02:00 vcsc UTCTime="2018-07-09 12:09:11,206" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid b151839e-a0dd-4176-bbed-ad28e05e9283 name: joinext.vngtp.cms dnsname: cmsdb.vngtp.cms "
2018-07-09T14:09:11.206+02:00 vcsc UTCTime="2018-07-09 12:09:11,206" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid b151839e-a0dd-4176-bbed-ad28e05e9283 name: joinext.vngtp.cms address: 192.168.1.212 "
2018-07-09T14:09:11.206+02:00 vcsc UTCTime="2018-07-09 12:09:11,206" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid b151839e-a0dd-4176-bbed-ad28e05e9283 name: joinext.vngtp.cms priority: 10"
2018-07-09T14:09:11.206+02:00 vcsc UTCTime="2018-07-09 12:09:11,206" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid b151839e-a0dd-4176-bbed-ad28e05e9283 name: joinext.vngtp.cms weight: 1"
2018-07-09T14:09:11.206+02:00 vcsc UTCTime="2018-07-09 12:09:11,206" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid b151839e-a0dd-4176-bbed-ad28e05e9283 name: joinext.vngtp.cms port: 443"
```

d. The Expressway-C creates general access rules for HTTPS and WebSocket traffic in the HTTP allow list in the Automatic inbound rules for the general path to the WB:

## Troubleshoot

This section provides information you can use in order to troubleshoot your configuration.

Here are some typical issues seen after you integrate WB onto the Expressway:

1. Priority and Weight are not seen on the CMS page on the Expressway-C, as shown on the image:

Logs required:

- Navigate to Maintenance  > Diagnostics > Diagnostic Logging

- Ensure that Take tcpdump while logging is checked, then select Start New Log

What to look for in the logs:

a. In the diagnostic logs:

- Open the diagnostic logs with the use of a text editor (for example Notepad++), then search for the join URL with the use of the Find All in Current Document option

- You will see in logs that the Expressway-C doesn't create the individual WB UUID with the use of their actual FQDN, instead do so with the use of the general join URL, as shown in this log snippet:

```
2018-07-13T14:44:21.688+02:00 vcsc UTCTime="2018-07-13 12:44:21,688" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 0ab708c9-4ce1-47b3-9bb6-2964baf39bb3 name: joinext.vngtp.cms guid: 97d8fa86-7de4-4410-9767-7bc8b1eeaced "
2018-07-13T14:44:21.688+02:00 vcsc UTCTime="2018-07-13 12:44:21,688" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 0ab708c9-4ce1-47b3-9bb6-2964baf39bb3 name: joinext.vngtp.cms dnsname: joinext.vngtp.cms "
2018-07-13T14:44:21.688+02:00 vcsc UTCTime="2018-07-13 12:44:21,688" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 0ab708c9-4ce1-47b3-9bb6-2964baf39bb3 name: joinext.vngtp.cms address: 192.168.1.66 "
2018-07-13T14:44:21.688+02:00 vcsc UTCTime="2018-07-13 12:44:21,688" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 0ab708c9-4ce1-47b3-9bb6-2964baf39bb3 name: joinext.vngtp.cms priority: 65536"
2018-07-13T14:44:21.688+02:00 vcsc UTCTime="2018-07-13 12:44:21,688" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 0ab708c9-4ce1-47b3-9bb6-2964baf39bb3 name: joinext.vngtp.cms weight: 0"
2018-07-13T14:44:21.688+02:00 vcsc UTCTime="2018-07-13 12:44:21,688" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 0ab708c9-4ce1-47b3-9bb6-2964baf39bb3 name: joinext.vngtp.cms port: 443" 2018-07-13T14:44:21.702+02:00 vcsc UTCTime="2018-07-13 12:44:21,702" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 4b1b99fb-1b8f-400e-b066-d8906ffcd6fc name: joinext.vngtp.cms name: joinext.vngtp.cms"
2018-07-13T14:44:21.702+02:00 vcsc UTCTime="2018-07-13 12:44:21,702" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 4b1b99fb-1b8f-400e-b066-d8906ffcd6fc name: joinext.vngtp.cms guid: 81db7b67-2aa9-4f64-8d74-04c4037397a8 "
2018-07-13T14:44:21.702+02:00 vcsc UTCTime="2018-07-13 12:44:21,702" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 4b1b99fb-1b8f-400e-b066-d8906ffcd6fc name: joinext.vngtp.cms dnsname: joinext.vngtp.cms "
2018-07-13T14:44:21.702+02:00 vcsc UTCTime="2018-07-13 12:44:21,702" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 4b1b99fb-1b8f-400e-b066-d8906ffcd6fc name: joinext.vngtp.cms address: 192.168.1.211 "
2018-07-13T14:44:21.702+02:00 vcsc UTCTime="2018-07-13 12:44:21,702" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 4b1b99fb-1b8f-400e-b066-d8906ffcd6fc name: joinext.vngtp.cms priority: 65536"
2018-07-13T14:44:21.702+02:00 vcsc UTCTime="2018-07-13 12:44:21,702" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 4b1b99fb-1b8f-400e-b066-d8906ffcd6fc name: joinext.vngtp.cms weight: 0"
2018-07-13T14:44:21.702+02:00 vcsc UTCTime="2018-07-13 12:44:21,702" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 4b1b99fb-1b8f-400e-b066-d8906ffcd6fc name: joinext.vngtp.cms port: 443" 2018-07-13T14:44:21.706+02:00 vcsc UTCTime="2018-07-13 12:44:21,706" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 6cc95c70-0636-4190-85f2-333b86b29c91 name: joinext.vngtp.cms name: joinext.vngtp.cms"
2018-07-13T14:44:21.706+02:00 vcsc UTCTime="2018-07-13 12:44:21,706" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 6cc95c70-0636-4190-85f2-333b86b29c91 name: joinext.vngtp.cms guid: 9c788380-6601-4dba-96e0-739511728369 "
2018-07-13T14:44:21.706+02:00 vcsc UTCTime="2018-07-13 12:44:21,706" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 6cc95c70-0636-4190-85f2-333b86b29c91 name: joinext.vngtp.cms dnsname: joinext.vngtp.cms "
2018-07-13T14:44:21.706+02:00 vcsc UTCTime="2018-07-13 12:44:21,706" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 6cc95c70-0636-4190-85f2-333b86b29c91 name: joinext.vngtp.cms address: 192.168.1.212 "
2018-07-13T14:44:21.706+02:00 vcsc UTCTime="2018-07-13 12:44:21,706" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 6cc95c70-0636-4190-85f2-333b86b29c91 name: joinext.vngtp.cms priority: 65536"
2018-07-13T14:44:21.706+02:00 vcsc UTCTime="2018-07-13 12:44:21,706" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 6cc95c70-0636-4190-85f2-333b86b29c91 name: joinext.vngtp.cms weight: 0"
2018-07-13T14:44:21.706+02:00 vcsc UTCTime="2018-07-13 12:44:21,706" Event="System Configuration Changed" Node="clusterdb@127.0.0.1" PID="<0.488.0>" Detail="xconfiguration edgeCmsServerAddresses uuid 6cc95c70-0636-4190-85f2-333b86b29c91 name: joinext.vngtp.cms port: 443"
```

b. In the packet capture:

- Filter with the use of the string DNS

- In the result, you'll see that the DNS query for SRV records fail, as shown in this image:

Solution:

Check and ensure that you have these in the DNS server used by the Expressway-C:

- Forward Lookup Zone (FLZ) with the Guest account client URI and not just for the domain in the URI

- Ensure that you have the SRV records ( _cms-web._tls.<WB_FQDN> ) configured in this FLZ and that it contains the relevant Priority and Weight

2. One or more WB are in the Active status after you add the cluster with the use of the external join URL, as shown in this image:

Logs required:

- Diagnostic logs that include tcpdump from the Expressway-C

- Packet capture from the server shows the Failed state with the use of the command pcap <interface> on the command line interface (CLI), where the interface is the listening interface of the WB

What to look for in the logs:

a. Diagnostic logs:

- Find All in Current Document with the use ofthe IP address of the failed WB

- The error here is seen in the logs:

```
Detail=" CMS check failed " Address="192.168.1.212", Error="[Errno 111] Connection refused "
```

b. In the packet capture:

- Filter on the packet capture with the use of the string ip.addr==<IP address of the failed WB>

- You will see TCP SYN messages sent from the Expressway-C to the WB and in this case no SYN-ACK nor ACK is received, as shown in this image:

- WB pcap will show that these TCP SYN messages arrive but no response ( SYN-ACK nor ACK ) is sent.

Solution:

Ensure that WB is enabled on that CMS node with the use of the command webbridge enable on the CLI.

### Contributed by Cisco Engineers

Joshua Alero

Cisco TAC Engineer

### This Document Applies to These Products

- Meeting Server

| SRV Record | Port | Priority | Weight | Resolves to |
|---|---|---|---|---|
| _cms-web._tls.joinext.vngtp.cms | 443 | 20 | 1 | cmsvngtp.vngtp.cms |
| _cms-web._tls.joinext.vngtp.cms | 443 | 15 | 1 | cms2.vngtp.cms |
| _cms-web._tls.joinext.vngtp.cms | 443 | 10 | 1 | cmsdb.vngtp.cms |

| SRV Record | Port | Priority | Weight | Resolves to |
|---|---|---|---|---|
| _cms-web._tls.joinext.vngtp.cms | 443 | 0 | 0 | cmsvngtp.vngtp.cms |
| _cms-web._tls.joinext.vngtp.cms | 443 | 0 | 0 | cms2.vngtp.cms |
| _cms-web._tls.joinext.vngtp.cms | 443 | 0 | 0 | cmsdb.vngtp.cms |