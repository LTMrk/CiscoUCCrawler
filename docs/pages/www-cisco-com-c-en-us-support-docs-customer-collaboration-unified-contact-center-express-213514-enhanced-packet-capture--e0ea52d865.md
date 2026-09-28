---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-contact-center-express-213514-enhanced-packet-capture--e0ea52d865
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-express/213514-enhanced-packet-capture-on-all-vos-appli.html
retrieved_at: 2026-08-16T15:05:20.403384+00:00
---

Enhanced Packet Capture on All VOS Appliance Models

# Enhanced Packet Capture on All VOS Appliance Models

Updated: July 25, 2018

Document ID: 213514

Contents

## Contents

## Introduction

This document describes the process in order to see the trace between Voice Operarting System (VOS) node and Phone/Gateway/3rd Party Server.

When you troubleshoot in Cisco Unified Communications Manager (CUCM), Cisco Unified Contact Center Express (UCCX), Cisco Unity Connection (CUC) or Instant Message and Presence (IM&P), it is sometimes necessary to collect packets for intermittent issues which are being sent to and from the network interface on a VOS server. The commands and screenshots are shown for CUCM version 11.X, the same can be applied for CUC, UCCX and IM&P (from 11.X and above).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CUCM

- UCCX

- CUC

- IM&P Version 11.X and above

### Components Used

The information in this document is based on Call Manager 11.X.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

### Normal Interface Packet Captures

Step 1. Connect to the CUCM Host.

With the use of an Secure Shell (SSH) client like Putty/SecureCRT connect to the CUCM node as shown in the image.

Step 2. Prepare a Capture Trace File.

Now, after admin prompt, you can start to prepare a capture network utility in order to capture packets as shown in the image.

```
utils network capture             [Currently available option]
utils network capture-rotate  [New feature available from CUCM, UCCX, CUC, IMP version 11.X]
```

Step 3. For a usual capture, one might want to collect ALL packets of ALL sizes from and to ALL address into a capture file called PC.cap . In order to do this, simply run utils network capture eth0 file packets count 100000 size all on the admin CLI and as shown in the image.

Step 4. Press Ctrl + C in order to stop captures.

- Limited number of packets (100000) when you capture to file (Limitation with above option)

- Difficult to capture intermittent issues

Now, what if you want to capture packets more than 100000 or for intermittent issues, so this Enhancement method is used to collect captures on CUCM interface.

### Enhanced Packet Capture

#### Features

- Capture more than 100000 packets

- Capture continuously based on set parameters

- Capture intermittent issues

- Leverage larger common partitions

- Restriction/Limitation: Do not consume entire common partition or trigger LowWaterMark condition

#### Configuration

You can use this method in order to add the rotating file parameters:

```
admin:utils network capture-rotate file PC maxfiles 40 sizeperfile 20

Syntax:

 

utils network capture-rotate [options]

 

file fname - output the information to a file          //Note: The file will be saved in platform/cli/fname. fname should not contain the "." character
         
size bytes              - the number of bytes of the packet to capture.   //Note: Valid values include any number up to 65535 or ALL. The default will be ALL.
   
sizePerFile megabytes   - the sizePerFile sets the value for the size of the log files.   //Note: The default value of sizePerFile is 25 MB.
    
maxFiles num            - the maxFiles indicates the maximum number of log files to be created. // Note: The default value of maxFiles is 10.
   
src addr                 - the source address of the packet as a host name or IPV4 address
dest addr               - the destination address of the packet as a host name or IPV4 address
port num                - the port number of the packet (either src or dest)
host protocol addr      - the protocol should be one of the following: ip/arp/rarp/all. The host address of the packet as a host name or IPV4 address. This option will display all packets to and fro that address.
```

Note : If host is provided, do not provide src or dest.

The image shows a successful Packet Capture rotate command:

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

This section provides information you can use in order to troubleshoot your configuration.

Low Watermark (LWM) indicates that the available disk space is low on the log (Common) partition. If Common Partition exceeds (LWM - 5), capture is prevented.

When LWM is hit, capture fails as shown in the image.

If Database is down and query fails for LWM, the error published is as shown in the image.

If query for LWM fails, enhanced capture commands fails with Database error. These command queries LWM configuration from the database and subtracts 5, so if database is down, it assumes LWM is 90% and print warning.

File format for enhanced captures:

```
<filename>.cap0, <filename>.cap1
<filename>.cap00, <filename>.cap01
```

CLI command in order to collect packet Captures:

```
file get activelog platform/cli/*.cap*
```

Collect Packet Captures from Real-Time Monitoring Tool ( RTMT). Navigate to System > Trace & Log central > Collect files  > Packet Capture Logs and as shown in the image.

Note : In order to recover common partition space, it might be necessary to delete capture files.

Note : If CLI session is closed, while rotate command is active, Packet captures stop (and saved) at the moment when window is closed.

Packet captures remains on disk until deleted. It is recommended to delete these captures periodically.

- In order to list all captures, run file list activelog platform/cli/*.cap*

- In order to download captures, run file get activelog platform/cli/*.cap*

- In order to delete captures, run file delete activelog platform/cli/*.cap*

How to download the Captures via SSH FTP (SFTP) Server is as shown in the image.

### Revision History

1.0

25-Jul-2018

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 25-Jul-2018 | Initial Release |