---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-215438-how-to-expor-07deb5a5b7
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/215438-how-to-export-tls-certifcate-from-cucm-p.html
retrieved_at: 2026-08-17T00:13:58.537170+00:00
---

How to Export TLS Certifcate from CUCM Packet Capture (PCAP)

# How to Export TLS Certifcate from CUCM Packet Capture (PCAP)

### Download Options

Updated: April 23, 2020

Document ID: 215438

Contents

## Contents

## Introduction

This document describes the procedure to export a certificate from a Cisco Unified Communications Manager (CUCM) PCAP.

Contributed by Adrian Esquillo, Cisco TAC Engineer.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics: • Transport Layer Security (TLS) Handshake • CUCM Certificate Management • Secure File Transport Protocol (SFTP) server • Realtime Monitoring Tool (RTMT)

• Wireshark Application

### Components Used

• CUCM release 9.X and higher

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

A server certificate/certificate chain can be exported in order to confirm that the server certificate/certificate chain provided by the server matches the certificate(s) to upload or that are uploaded to CUCM Certificate Management.

As part of the TLS handshake, the server provides its server certificate/certificate chain to CUCM.

## Export TLS Certificate from CUCM PCAP

Step 1. Start the packet capture command on CUCM

Establish a Secure Shell (SSH) connection to the CUCM node and run the command utils network capture (or capture-rotate) file <filename> count 1000000 size ALL , as shown in the image:

Step 2. Start a TLS connection between Server and CUCM

In this example, you start a TLS connection between a Secure Lightweight Directory Access Protocol (LDAPS) server and CUCM by establishes a connection on TLS port 636, as shown in the image:

Step 3. Stop CUCM PCAP after TLS handshake Is completed

Press Control-C to stop the packet capture, as shown in the image

Step 4. Download the packer capture file by any of the two methods listed

1. Launch RTMT for CUCM node and Navigate to System > Tools > Trace > Trace & Log Central > Collect Files and check the Packet Capture Logs box (continue through the RTMT process in order to download the pcap), as shown in the image:

2. Start a Secure File Transport Protocol (SFTP) server and in the CUCM SSH session run the command file get activelog /patform/cli/<pcap filename>.cap (continue through the prompts in order to download the PCAP on SFTP server), as shown in the image:

Step 5. Determine the Number of Certificates Presented to CUCM by the Server

Utilize Wireshark application in order to open the pcap and filter on tls to determine the packet with Server Hello that contains the server certificate/certificate chain presented to CUCM. This is frame 122, as shown in the image:

• Expand the Transport Layer Security > Certificate information from the Server Hello packet with certificate in order to determine the number of certificates presented to CUCM. The top certificate is the server certificate. In this case only 1 certificate, the server certificate, is presented as shown in the image:

Step 6. Export the server certificate/certificate chain from the CUCM PCAP

In this example, only the server certificate is presented, so you need to examine the server certificate. Right click on the server certificate and select Export Packet Bytes in order to save as a .cer certificate, as shown in the image:

• In the subsequent window, provide a .cer file name and then click save. The file that was saved (in this case, to the desktop) was named servercert.cer, as shown in the image:

Step 7. Open saved .CER file in order to examine contents

Double click on the .cer file in order to examine the information in the General , Details and Certificate Path tabs, as shown in the image:

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.