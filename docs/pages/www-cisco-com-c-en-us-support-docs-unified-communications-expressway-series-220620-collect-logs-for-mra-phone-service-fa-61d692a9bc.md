---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-expressway-series-220620-collect-logs-for-mra-phone-service-fa-61d692a9bc
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway-series/220620-collect-logs-for-mra-phone-service-failu.html
retrieved_at: 2026-08-16T15:43:40.077453+00:00
---

Collect Logs for MRA Phone Service Failures

# Collect Logs for MRA Phone Service Failures

### Download Options

Updated: July 24, 2023

Document ID: 220620

Contents

## Contents

## Introduction

This document describes how to collect the logs required for troubleshooting phone service problems experienced when using Mobile Remote Access (MRA).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of Cisco Unified Communications Manager (CUCM) and Cisco Expressway.

### Components Used

The information in this document is based on the listed software versions:

- Cisco Unified Communications Manager 14.0.1 SU3

- Cisco Expressway X14.2.5

- Cisco Jabber 14.1.5

- Webex App 43.6.0

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Process to Collect Logs

### Setup Logging

It is important to setup logging correctly before re-creating the reported MRA phone service failure.

#### Cisco Expressway

- Select the checkbox near the option for Take tcpdump while logging .

- Next, select Start new log .

Note : Select the Start new log option from Primary Expressway C and Expressway E to initiate logging on all cluster peers.

#### Jabber

- Set Cisco Jabber for iPhone and Android to detailed logging. Reference the steps detailed in the Collect Logs for UC Applications guide.

Note : Cisco Jabber for Windows and MAC does not need to have detailed logging set as it is set to detailed by default.

### Collect Logs and Traces

After recreating the phone service issue over MRA, collect the logs and traces.

#### Cisco Expressway

Collect the Expressway C and Expressway E diagnostic log.

- Select Stop Logging .

- Next, select Collect Log .

- Once the download log button appears, select Download Log to save the file.

#### Cisco Unified Communications Manager Traces

CUCM logs can be collected easily using the Real Time Monitoring Tool (RTMT) desktop application or Cloud Connected Unified Communication (CCUC) Web RTMT.

Collect the CUCM logs using Cisco Real Time Monitoring Tool (RTMT)

For information on how to use RTMT to collect logs from CUCM, refer to the Collect Trace Data for CUCM 9.X or Later guide.

Collect the listed traces:

- Cisco CallManager

- Cisco CTIManager

- Cisco Tomcat

- Cisco Tomcat Security

- Cisco User Data Services

- Event Viewer - Application Log

- Event Viewer - System Log

Collect CUCM logs using Web RTMT

- Log in to WebEx Control Hub

- Select the CUCM Cluster from clusters section.

- Once redirected, log into the tool with an Admin account.

CUCM Web RTMT Log in

- Once logged in, select the Trace/Log from the navigation menu.

Web RTMT Trace/Log

- Cisco CallManager

- Cisco CTIManager

- Cisco Tomcat

- Cisco Tomcat Security

- Cisco User Data Services

- Event Viewer - Application Log

- Event Viewer - System Log

- Once the services have been chosen, select the radio button to Download Logs and define the time range you would like to collect. Then, select Download .

Web RTMT Download Log

#### Cisco Jabber

When collecting the Jabber logs, take note of the operating system that Jabber is being used on, and refer to the Collect Logs for UC Applications guide.

#### Cisco WebEx App

Webex App Desktop

- For information on how to collect the WebEx App Diagnostic logs on a Windows or MAC machine, refer to the Webex App | Troubleshoot connection issues guide.

WebEx App for iPhone

- Select the Profile Picture located in the top left corner.

- Choose the option to Report an Issue .

- Select the Profile Picture located in the top left corner.

- Choose Settings .

- Select your email app, and enter the email where you want to send the logs.

WebEx App for Android

- Select the Profile Picture located in the top left corner.

- Choose the option to Send Logs .

- Select the Profile Picture located in the top left corner.

- Choose the Gear Icon .

- Select your email app, and enter the email where you want to send the logs.

### Revision History

1.0

24-Jul-2023

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 24-Jul-2023 | Initial Release |