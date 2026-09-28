---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-expressway-217220-how-to-troubleshoot-partial-registration-htm-037b67cbbb
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217220-how-to-troubleshoot-partial-registration.html
retrieved_at: 2026-08-16T15:44:22.034582+00:00
---

How to Troubleshoot Partial Registration for MRA

# How to Troubleshoot Partial Registration for MRA

### Download Options

Updated: June 29, 2021

Document ID: 217220

Contents

## Contents

## Introduction

This document describes, how to troubleshoot Partial Registered Session Initiation Protocol (SIP) Phone over Mobile and Remote Access (MRA), why this happen, and how to identify it.

## Background Information

### What is Partial Registered for a Device?

Partially registered means that not all lines on a SIP phone have registered. This issue can be cause for different reasons, like Line Button templates, Identity Trust list/Certificate Trust List (ITL/CTL) mismatch, SIP message size, Keep alive, etc.

### SIP Phone with Multiple Lines Registration

The first register from an endpoint with multiple lines contains all SIP lines configured to register all lines.

Then it's expected to see REGISTER (Keep-alive) messages every 120 seconds (actually 115 seconds which is 120 minus the delta value configured in SIP profile, which is 5 seconds by default). In this case, the phone sends keep-alive every 115 seconds, as shown in the image:

In the first REGISTER the SIP phone sends more details inside the Content-Type section of the Session Description Protocol (SDP), as shown in the next image:

The next REGISTER messages does not contain any additional Content-Type information.

In summary, when an endpoint connected over MRA has multiple lines configured and a SIP keep Alive arrives at Cisco Unified Comunnications Manager (CUCM) too late, that CUCM has already cleared the registration (unregistered the device), when the keep Alive arrives, CUCM re-registers the device but only the primary line since that is all that is in the register message.

There are also other scenarios when the phone connects over MRA where this problem can occur If the Transmission Control Protocol (TCP) connection drops between Expressway-C and CUCM, the SIP phone is unregistered from the CUCM perspective, but the phone does not know this and sends a Keep Alive register instead of a Full register, that causes the Partial Registration behavior.

## Troubleshooting

Collect the next log files:

- Expressway C and E Diagnostics logs. Downloading Expressway Diagnostic Logs and Packet Captures | Cisco Virtual Events

- CUCM traces. Unified Communications Manager - RTMT Trace Collection | Cisco Virtual Events

- Call Manager

- Event Viewer System and Application logs.

- IP Phone PRT. How to Collect a Collaboration Endpoint PRT File with Cisco 78XX and 88XX Phones - Cisco

Expressway logs, are taken in real time, it's not possible to know when would be a good time to start/stop Diagnostics logs, so in case you want to review the information mentioned above, you can follow the next procedure:

### Optional Troubleshooting Procedure

There is a way to set alerts with Real-Time Monitoring Tool (RTMT). The idea is to take logs from Expressways with Windows Secure Copy (WinSCP) right after the email alert from RTMT tool is received.

Note : E-mail server must be already configured. https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-connection/117890-technote-cucm-00.html

### Configure RTMT Alarm

It's possible to create an alarm with RTMT tool, that sends an email, once a SIP Phone is on Partial Registered state, in order to implement the alarm follow the next steps:

- Open RTMT tool, and navigate to Performance > Performance . Then Select Cisco CallManager and look for PartialRegisteredPhone .

- Then right click and select Set Alert/Properties.

- Check Enable Alert , and Set Severity as Critical .

- Under Threshold configuration, check Value , then you can set Over as 1.

- Check Enable Email option.

- Under Trigger Alert Action , select Configure , select Add and set a new name for the Action List, in this example the name is emai .

- Add the email address for the alerts to be received.

- Select Save .

Once you get an alert from RTMT tool, you can go to your Expressways servers and follow the next steps:

- Open WinSCP, access Expressway C and E, with IP address or Fully Qualified Domain Name (FQDN) and root credentials.

- Navigate to /mnt/harddisk/log/ .

- network_log

- messages

- developer_log

Expressways usage can overwrite the information on log files very fast, make sure you get the files with the correct time stamp.

With information included on network_log file, is possible to determine if REGISTER messages reach CUCM servers on time, and if after any issue, IP Phone sends REGISTER message with one or all the lines to register back.

### Enhancement Request

Currently the CUCM is unable to notify the SIP phones that are Partialy Registered, an enhacement to allow CUCM the notification is already opened: CSCvw49110 .

As stated on enhancement request the workaround is:

- Reset the endpoint to force all lines to re-register.

- Additionally increase the Timer Register Delta value in the SIP Profile on CUCM to 20 (default is 5) to tolerate more delay and decrease the likelihood this occurs.

### Revision History

1.0

29-Jun-2021

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 29-Jun-2021 | Initial Release |