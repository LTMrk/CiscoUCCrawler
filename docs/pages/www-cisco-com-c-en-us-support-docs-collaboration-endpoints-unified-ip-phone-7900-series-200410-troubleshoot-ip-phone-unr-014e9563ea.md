---
doc_id: www-cisco-com-c-en-us-support-docs-collaboration-endpoints-unified-ip-phone-7900-series-200410-troubleshoot-ip-phone-unr-014e9563ea
source_url: https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/unified-ip-phone-7900-series/200410-Troubleshoot-IP-Phone-Unregistration-A.html
retrieved_at: 2026-08-20T20:40:38.919879+00:00
---

Troubleshoot IP Phone Unregistration - A Case Study

# Troubleshoot IP Phone Unregistration - A Case Study

### Download Options

Updated: February 10, 2016

Document ID: 200410

Contents

## Contents

## Introduction

This document describes information that can used in order to troubleshoot your configuration.

Cisco IP Phone uses application level keep-alive mechanism in addition to the the Network level TCP keep alive mechanism. Keep-Alive mechanism for Skinny Call Control Protocol (SCCP) and Session Initiation Protocol (SIP) devices ensures that the device stays registered with call control. They are also meant to re-establish connection of devices with call control.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

This document is not restricted to specific software and hardware versions.

## SCCP Keep-alives and Failover Mechanism

SCCP uses TCP protocol for Transport and it uses the port 2000 and 2443 (for secured) to make connection to the Call Manager. The SCCP phones should make a TCP connection with the Cisco Unified Communications Manager (CUCM) before registering to it. Following which, a TCP 3 way handshake will happen on port 2000 to establish a communication channel. The phone initiates this connection by sending a SYN (synchronize) to CUCM and CUCM responds with SYN, ACK (acknowledgement). The phone in turn responds with an ACK and the TCP connection gets established.

### Keep-alives

There are two keep-alive methods: Application level (SKINNY keep-alive) and Network level (TCP keep-alive)

### Failover

In an ideal scenario, a SCCP phone keeps a TCP connection established to the primary CUCM and the first backup CUCM. SCCP phone sends keep-alive to all the CUCM to which it has the established a TCP connection. Primary server then responds to the SCCP keep-alive. The time interval is 30 seconds to primary server and 60 seconds to the backup server.

The primary CUCM responds back with SCCP keepalive ACK which acknowledges both SCCP and TCP connection. The backup CUCM just sends a TCP ACK to the keep-alive sent by the phone. When the phone fails to backup CUCM because the Call Manager service is not available or the TCP connection itself is unavailable with the primary CUCM, it uses two kinds of mechanisms to detect the primary CM failure and they are normal and delayed.

### Normal failover

This method uses an algorithm to calculate the average of the time taken by the CUCM to acknowledge the previous keep-alives.

For example, if the average time taken by CUCM is X seconds to respond for the past 10000 keep-alives, the phone will wait for X seconds before it detects the failure of CUCM. Following which, it will try to register to the backup CUCM.

### Delayed failover

In this mechanism, the phone waits for the 3 keep-alive intervals to detect the failure of the primary CUCM.

### Drawback

Networks where transit time of packets fluctuate, delayed failover helps avoid unnecessary unregistration.

Example of Transit Time Fluctuation (Note the time delay for ping response):

```
64 bytes from 10.106.97.150: icmp_seq=1 ttl=63 time=0.100 ms
64 bytes from 10.106.97.150: icmp_seq=2 ttl=63 time=200 ms
64 bytes from 10.106.97.150: icmp_seq=3 ttl=63 time=0.180 ms
64 bytes from 10.106.97.150: icmp_seq=4 ttl=63 time=0.678 ms
64 bytes from 10.106.97.150: icmp_seq=5 ttl=63 time=590 ms
64 bytes from 10.106.97.150: icmp_seq=6 ttl=63 time=0.100 ms
64 bytes from 10.106.97.150: icmp_seq=7 ttl=63 time=345 ms
64 bytes from 10.106.97.150: icmp_seq=8 ttl=63 time=456 ms
64 bytes from 10.106.97.150: icmp_seq=9 ttl=63 time=0.345 ms
```

### Advantage

This mechanism can be used in the delay sensitive networks.

## SIP Keep-alive

The SIP phone registers to the CUCM and sends keep-alive every 120 seconds as per the settings in CUCM. When the phone sends the initial register to primary CUCM, it sets the Expires timer to 3600 seconds (default set in SIP profile applied on the phone). CUCM sends an ACK by modifying the timer to 120 seconds as per the value set in Service parameter.

Therefore, the phone sends keep-alive every 120 seconds (actually 115 seconds which is 120 minus the delta value configured in SIP profile, which is 5 seconds by default). In this case, the phone sends keep-alive every 115 seconds.

SIP phone exchanges the Register message to Backup CUCM with Expires field set to 0.

### To Primary

```
REGISTER sip:10.106.114.161 SIP/2.0

Via: SIP/2.0/TCP 10.106.114.185:53006;branch=z9hG4bKd451a4fa

From: <sip:5678@10.106.114.161>;tag=0024142ddf242c6644b6e5d2-f01c795a

To: <sip:5678@10.106.114.161>

Call-ID: 0024142d-df24000a-44da4e09-0de51424@10.106.114.185

Max-Forwards: 70

Date: Wed, 15 Jul 2015 12:42:56 GMT

CSeq: 11435 REGISTER

User-Agent: Cisco-CP7975G/9.3.1

Contact: <sip:9e9e1ffb-0206-4ea1-6d77-ba04a72017f7@10.106.114.185:53006;transport=tcp>;+sip.instance="<urn:uuid:00000000-0000-0000-0000-0024142ddf24>";+u.sip!devicename.ccm.cisco.com="SEP0024142DDF24";+u.sip!model.ccm.cisco.com="437"

Supported: replaces,join,sdp-anat,norefersub,resource-priority,extended-refer,X-cisco-callinfo,X-cisco-serviceuri,X-cisco-escapecodes,X-cisco-service-control,X-cisco-srtp-fallback,X-cisco-monrec,X-cisco-config,X-cisco-sis-6.0.0,X-cisco-xsi-8.5.1

Content-Length: 0

Expires: 3600

SIP/2.0 100 Trying

Via: SIP/2.0/TCP 10.106.114.185:53006;branch=z9hG4bKd451a4fa

From: <sip:5678@10.106.114.161>;tag=0024142ddf242c6644b6e5d2-f01c795a

To: <sip:5678@10.106.114.161>

Date: Wed, 15 Jul 2015 12:42:59 GMT

Call-ID: 0024142d-df24000a-44da4e09-0de51424@10.106.114.185

CSeq: 11435 REGISTER

Content-Length: 0

SIP/2.0 200 OK

Via: SIP/2.0/TCP 10.106.114.185:53006;branch=z9hG4bKd451a4fa

From: <sip:5678@10.106.114.161>;tag=0024142ddf242c6644b6e5d2-f01c795a

To: <sip:5678@10.106.114.161>;tag=1708299782

Date: Wed, 15 Jul 2015 12:42:59 GMT

Call-ID: 0024142d-df24000a-44da4e09-0de51424@10.106.114.185

CSeq: 11435 REGISTER

Expires: 120

Contact: <sip:9e9e1ffb-0206-4ea1-6d77-ba04a72017f7@10.106.114.185:53006;transport=tcp>;+sip.instance="<urn:uuid:00000000-0000-0000-0000-0024142ddf24>";+u.sip!devicename.ccm.cisco.com="SEP0024142DDF24";+u.sip!model.ccm.cisco.com="437"

Supported: X-cisco-srtp-fallback,X-cisco-sis-6.0.0

Content-Length: 0
```

### To Secondary

```
REGISTER sip:10.60.1.12:5060;transport=tcp SIP/2.0

Via: SIP/2.0/TCP 10.60.63.21:3784;rport;branch=z9hG4bKPjdcJ819aZtTCtmvr0VBheV6p0uL8aC.pG

Max-Forwards: 70

From: <sip:6836@10.60.1.12>;tag=5oI-ew53.DGjTDu5LB9orkdDpZlccNbv

To: <sip:6836@10.60.1.12>

Call-ID: HxTK.m6BH9qxjstVwexTbhVnUxNeuxle

CSeq: 18800 REGISTER

Expires: 0

Contact: <sip:e2b0f175-feae-d664-befa-b7cd0837fcc6@10.60.63.21:5060;transport=TCP>;+sip.instance="<urn:uuid:00000000-0000-0000-0000-e0d1730ac1b1>";+u.sip!devicename.ccm.cisco.com="SEPE0D1730AC1B1";+u.sip!model.ccm.cisco.com="592";expires=0;cisco-keep-alive

Content-Length:  0
```

## Logs Required

In order to identify why the phone unregistration occurred, collect information outlined:

- Event Viewer Application and System Logs - Provides alarm/error codes for the phone unregistration and using that we can proceed with troubleshooting.

- Packet capture from phone and the CUCM (both primary and backup) at the same time - Helps in isolating the issue network perspective.

- Cisco Call Manager Traces.

### Relevant Links

Collecting packet captures from CUCM

Collecting capture from IP Phone

Collecting CUCM Traces

Analyzing the Logs and Packet Captures

- Event Viewer Application log prints EndPointUnregistered message and also a related Reason Codes .

```
Example: 31 uc-ucm-01 local7 3 : 41679: uc-ucm-01.pcce.local Jul 02 2015 06:22:31 UTC :   %UC_CALLMANAGER-3-EndPointUnregistered: %[DeviceName=SEPE0D1730A8137][IPAddress=10.60.98.210][Protocol=SIP][DeviceType=592][Description=Phone][Reason=13][IPAddrAttributes=0][LastSignalReceived=SIPStationDPrimaryLineTimeout][AppID=Cisco CallManager][ClusterID=StandAloneCluster][NodeID=uc-ucm-01]: An endpoint has unregistered
```

The Reason Codes for EndPointUnregistration can be found in System Error Messages Documentation.

Reading Wireshark Logs

When Captures from both end are collected, to verify that the keepalive sent by phone is actually reaching the CUCM or not.

Sequence Number of TCP packet will help easily track the TCP traffic between phone and CUCM in sniffer capture.

### Capture from Phone

Phone sends a packet with sequence number 2991996107, verify that this packet reaches the CUCM.

### Capture from CUCM

Sequence number that is seen in phone sniffer capture should be seen in the CUCM capture.

## Case Study 1.2

### Problem Description

SCCP phones keep restarting at regular intervals.

### Troubleshoot

Event Viewer Application log indicates that the phones kept restarting due to missing keep alives with error code of 13.

```
Event Viewer Message.
```

Collect packet capture from IP Phone and CUCM.  In this scenario, the last keep-alive sent from IP Phone did not reach CUCM.

```
Image.
```

Keep-alive is getting dropped because of this reason:

When the phone sent an ARP to get the MAC adress of CUCM, the response came in from ARP Proxy with ASA mac-address. Clearly, the first response was not from CUCM. However, since the phone recieves it first, it sends the frame to the switch with the MAC address of the other device.

This happens mostly when ARP-proxy is enabled on ASA.

### Resolution

Disable ARP Proxy on ASA to address the problem.

## Case Study 2.

### Problem Description

Cisco IP Phone model 8961 phones reset every 16 minutes and registers to secondary CUCM. After 2 minutes the phone falls back to Primary CUCM and this cycle continues.

### Troubleshoot

Collect Packet captures from the phone and CUCM traces. The unregistration was due to SIP keep-alive missed by the IP Phone.

### Analysis

The SIP phone registers to the CUCM and it sends Keep-alive every 120 seconds as per the settings in CUCM.

When the phone sends the initial register it sets the expires timer to 3600 seconds (default set in SIP profile applied on the phone). CUCM acknowledges it by modifying the timer to 120 seconds as per the value set in Service parameter.

The phone sends Keepalive every 120 seconds ( keep-alive interval is 115 seconds which is 120 minus the delta value configured in SIP profile, which is 5 seconds by default). In this case the phone sends keepalive every 115 seconds.

In this problem scenario the phone sends the first keepalive at 115 second and it gets dropped in the network. This results in  phone retransmitting the keepalive in .01 seconds(100 ms). It gets an response from CUCM for the REGISTER request.

Now the phone sends the second keepalive at 115 seconds and it gets dropped in the network. Now the phone increases it's REGISTER retry interval to .02 seconds (200 millisecond).

Every time the phone sends the keepalive after 115, it gets dropped in the network and this makes the phone to retransmit the packet. Also the phone exponentially increases it's retry interval. After few such keep-alives the phones retry increases to 14 seconds.

The phone retransmits after 14 seconds and it gets an ACK from the CUCM.

The next time when the phone sends keep-alive, it is lost and then the phone retransmits REGISTER request after 28 seconds. The CUCM cannot wait for 28 seconds, it waits for only 15 seconds (after the 115s) then it sends the unregister signal.

The keep-alive time and the RTO sums up to 16 minutes and a few seconds.

After 16 minutes due to the unregister signal from CUCM, the phones register to secondary CUCM and after 2 minutes they register back to Primary and this continues.

### Cause for the keep-alive drops

When the Switch port was configured with port security, the port aging was configured with inactive timer. The timer was set to one minute which is lesser than the SIP keep-alive timer. This resulted in switch port flushing the phone MAC every one minute. The packets keep being dropped as the SIP keep-alive interval is every 2 minutes.