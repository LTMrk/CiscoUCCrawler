---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-expressway-217244-mobile-and-remote-access-phone-services-html-c97e0fe2e7
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html
retrieved_at: 2026-08-16T15:44:13.743961+00:00
---

How Phone Services Failover works for Jabber Version 14 over MRA

# How Phone Services Failover works for Jabber Version 14 over MRA

### Download Options

Updated: July 8, 2021

Document ID: 217244

Contents

## Contents

## Introduction

This document describes how failover works for phone services on Jabber when registered via Mobile and Remote Access (MRA) with the addition of Session Traversal Utilities for NAT (STUN) keep alives on version 14 and later.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Communications Manager (CUCM).

- Cisco Expressway Core.

- Cisco Expressway Edge.

- Cisco Jabber for Windows.

- Cisco Jabber for MAC.

- Cisco Jabber for Android.

- Cisco Jabber for iOS.

### Components Used

The information in this document is based on these software and hardware versions:

- Expressway Version X14.0.

- CUCM 14.0.

- Cisco Jabber Version 14.0.

The information in this document was created from the devices in a specific lab environment. All of the devices   used in this document started with a cleared (default) configuration. If your network is live, ensure that you   understand the potential impact of any command.

## Background Information

For versions previous to x14.0, the MRA solution does not support automatic failover for phone services on soft clients like Jabber. With the introduction of STUN keep alives, this is now supported as long as the involved components meet the required criteria, this allows jabber to register to a secondary server if the main route or server itself become compromised or unreachable.

## Configuration

The only configuration required is to enable STUN Keep Alives on the expressway servers. This feature is enabled by default and only requires to be configured if it has been previously disabled.

Step 1. Open the Expressway-C web interface.

Step 2. Navigate to Configuration > Unified Communications > Configuration > Advanced .

Step 3. Open the Expressway-C Command Line Interface (CLI).

Step 4. Run the next command: xconfiguration SIP Advanced StunKeepAliveForRegisteredPathEnabled: on .

Note : The setting must match between core and edge servers in order to avoid decode issues.

## Troubleshooting

To ensure the feature is effective, the registration signaling needs to be analyzed.

### Collect diagnostic logs

Step 1. On the expressway servers web interface, navigate to Maintenance > Diagnostics > Diagnostic Logging.

Step 2. Check the Take tcpdump while logging checkbox.

Step 3. Select Start new log on both Core and Edge servers.

Step 4. Log in to your account on the jabber client with your standard username and password and wait for the phone services to register.

Step 5. Select Stop logging on both Core and Edge servers

Step 6. On all expressway servers, select Collect Log and Download log after it loads.

Note : In case of a cluster, Step 6 must be repeated on secondary peers.

### Registration

A jabber client on version 14 and later includes the tag x-cisco-mra-ha=AR_SK on the register message as seen below on the Contact header or Supported header , this indicates that STUN keep alives are supported.

```
SIPMSG:
 |REGISTER sip:cmpub01.rvalverd.local SIP/2.0
 Via: SIP/2.0/TLS 172.16.84.136:58980;branch=z9hG4bK00003665
 Call-ID: 00505696-779a0005-00001bba-00007938@172.16.84.136
 CSeq: 104 REGISTER
 Contact: <sip:7514c56a-1034-a684-3299-9b956979ee5c@172.16.84.136:58980;transport=tls>;+sip.instance="<urn:uuid:00000000-0000-0000-0000-00505696779a>";+u.sip!devicename.ccm.cisco.com="CSFMRA01";+u.sip!model.ccm.cisco.com="503";video;x-cisco-mra-ha=AR_SK;x-cisco-reg-id=1
 From: <sip:10001@cmpub01.rvalverd.local>;tag=00505696779a000700006827-00006484
```

The 200 OK message must contain this as well on the Supported header to indicate the server supports it.

```
SIPMSG:
 |SIP/2.0 200 OK
 Via: SIP/2.0/TLS 172.16.84.136:58980;branch=z9hG4bK00007e98;received=10.88.246.8;rport=58980;ingress-zone=CollaborationEdgeZone
 Call-ID: 00505696-779a0005-00001bba-00007938@172.16.84.136
 CSeq: 105 REGISTER
 Contact: <sip:7514c56a-1034-a684-3299-9b956979ee5c@10.15.20.10:5060;transport=tcp;orig-hostport=172.16.84.136:58980>;+sip.instance="<urn:uuid:00000000-0000-0000-0000-00505696779a>";+u.sip!devicename.ccm.cisco.com="CSFMRA01";+u.sip!model.ccm.cisco.com="503";video;x-cisco-mra-ha=AR_SK;x-cisco-reg-id=1;+u.sip!userid.ccm.cisco.com="mra01";x-cisco-newreg
 From: <sip:10001@cmpub01.rvalverd.local>;tag=00505696779a000700006827-00006484
 To: <sip:10001@cmpub01.rvalverd.local>;tag=385623253
 Server: Cisco-CUCM12.5
 Expires: 120
 Date: Thu, 24 Jun 2021 19:09:09 GMT
 Supported: X-cisco-srtp-fallback,X-cisco-sis-9.2.0,X-cisco-supports-AR_SK
 Session-ID: 9b8c276600255000a0000e5dc13f0000;remote=c31f584200255000a00000ddda3c0000
```

After this, jabber then sends a STUN keep alive packet every 30 seconds to the expressway servers in order to check the path availability. The timeout for the STUN keep alive is 3 seconds and if no response is received, the jabber considers the edge node to be down and performs a registration failover via a different edge server.

Note : The MRA client does not attempt a registration failover while it is on an active call. Instead, the failover is queued until the call finishes. If this happens, the failover occurs even if the downed server recovers.

### Revision History

1.0

08-Jul-2021

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 08-Jul-2021 | Initial Release |