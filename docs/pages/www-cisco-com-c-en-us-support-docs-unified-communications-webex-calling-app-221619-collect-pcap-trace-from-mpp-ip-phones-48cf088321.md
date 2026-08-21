---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-calling-app-221619-collect-pcap-trace-from-mpp-ip-phones-48cf088321
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-calling-app/221619-collect-pcap-trace-from-mpp-ip-phones.html
retrieved_at: 2026-08-21T07:16:44.363057+00:00
---

Collect PCAP Trace from MPP IP Phones

# Collect PCAP Trace from MPP IP Phones

### Download Options

Updated: February 2, 2024

Document ID: 221619

Contents

## Contents

## Introduction

This document describes the process to collect a PCAP trace from MPP Cisco IP phones.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Control Hub Administration.

- How to access to Cisco IP Phone Web Page.

- Admin Password Device.

Note : For Webex Calling (WxC) provisioned devices ask WxC support.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

A Packet Capture ( PCAP ) Trace is a capture taken from a network interface to do a network analysis and troubleshooting. The output file is a .pcap and can be read in any Network Packet Analyzer like Wireshark .

Cisco IP Phones, at times, do not take the config files to be provisioned or they have problems registering Webex Calling sevices.

In that case, is very helpful to get a PCAP trace directly from the IP Phone to know what is happening in the network.

Step 1. Navigate to Admin Page https://IP_ADDRESS_PHONE/Admin

Note : If the IP Address is unknown, it can be obtained from Settings > Status > Network Status > IPv4 Status .

Step 2. Log in as username Admin , enter the password, and select Login button.

Log In Page

Note : For factory reset devices, the log in page doesn`t appear. The config page appears directly

Step 3. Select Info and then Debug Info in the top menu.

Top Menu

Step 4. Select Start Packet Capture located in the right of the page.

Start Packet Capture

Step 5. Packet Capture options appears. Select Filter All and select the button Submit .

Packet Capture Options

Step 6. A ttempt to recreate or reproduce the specific problem or issue that you currently have.

Step 7. After successfully recreating the issue, proceed to select the Stop Packet Capture option.

Stop Packet Capture

Step 8. Once the phone has finished to create the pcap, the new file appears.

New Pcap File

Step 9. Download the PRT Log. Right-click on the link pcap and choose Save link as... in order to download the logs.

Save link

Step 10. Select the directory where you want to save and the button Save .

Save

## Related Information

- Configure and manage Webex Calling devices

- Configure and modify device settings in Webex Calling

- Generate PRT Manually for MPP Phones

### Revision History

1.0

02-Feb-2024

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 02-Feb-2024 | Initial Release |