---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-212915-configure-cu-1866ec0a92
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/212915-configure-cucm-smart-licensing-direct.html
retrieved_at: 2026-08-16T17:57:12.068446+00:00
---

Configure CUCM Smart Licensing - Direct Model

# Configure CUCM Smart Licensing - Direct Model

### Download Options

Updated: June 4, 2026

Document ID: 212915

Contents

## Contents

## Introduction

This document describes the direct model configuration to synchronize your CUCM directly with your Smart accounts.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Communications Manager (CUCM) version 12.0

### Components Used

The information in this document is based on Cisco Call Manager version 12.0

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

Cisco Smart Software Licensing is a new way to think about licensing. It simplifies the licensing experience across the enterprise and makes it easier to purchase, deploy, track, and renew Cisco Software. It provides visibility into license ownership and consumption through a single, simple user interface.

You place an order on Cisco Commerce and the order is associated with the smart account. This information is populated on Cisco License Central . Now, you have a complete view on what you have ordered and purchased.

The product that has smart licensing enabled (via CLI or GUI), is registered to Cisco License Central, and report license consumption to Cisco License Central. Two models exist to report the usage.

### Direct Model

Use this model in environments where devices can communicate directly to the Internet or can connect to the Internet via an HTTPS proxy. Communication to Cisco.com is via HTTPS, therefore all traffic is encrypted in transport. If traffic is sent through an HTTPS proxy or transport gateway, all communications between devices and Cisco.com is channeled through a centralized location if additional inspection or security policies need to be applied.

### Mediated Deployment Model

Use this model in networks where devices do not have any form to connect to the Internet, and therefore cannot reach Cisco.com. This deployment model requires that you install a Cisco License Central satellite virtual machine on-premises which is then reachable by all internal hosts. The on-premise satellite can be deployed in a connected mode that synchronizes with Cisco License Central monthly, weekly, or can be deployed in a totally disconnected configuration which requires manual file uploads and downloads to keep the satellite in sync. The recommendation is to do a sync at least every 30 days.

### Where Do I Create Smart Accounts

- To create a Smart Account, log in to CSC with your CCO ID and initiate a request for a Customer Smart Account .

- To create a Partner Holding Smart Account, log in to CSC with your CCO ID and initiate a request for a Partner Holding Account.

- You can also initiate a request for either type of Smart Account when you order in CCW. Although, the recommended best practice is to proactively set up your Smart Accounts.

Note : There is no upper limit; you can create as many Virtual Accounts as your company needs.

### Cisco Smart License Manager Service

Cisco Smart License Manager Service is a network service, which runs only on CUCM publisher. Since this is a network service, it runs all the time and cannot be started or stopped from UI or CLI. Since there is no service that runs on the subscriber, none of the smart licensing operations can be done from the sub. The CLI commands also do not provide any output on the sub,

### Smart Licensing States in UCM

There are two main states in Smart Licensing:

Registration Status: There are three registration Statuses:

- Unidentified / Unregistered

- Registered

- Unregistered-registered Expired

Authorization Status:

- No License in use

- Evaluation Mode

- Evaluation Expired

- Authorized

- Out of compliance

- Authorization Expired

In addition to these smart licensing states, UCM provides an overage period of 90 days (This is a concept already present in pre 12.0 with classic licensing. UCM continues to provide the average period with smart licensing as well)

## Configure (Direct Deployment)

Note : For direct deployment to work, your CUCM must have connectivity to the Internet.

### Configuration

- Log in to Cisco Software Central with your username and password.

- Select Inventory under Smart Software Licensing .

- Generate a new Token.

- Under the CUCM admin page, navigate to System > Licensing > License Management > View/Edit the Licensing Smart Call Home settings and then Verify Direct is selected and Production Cisco License Central URL is updated.

- Click Register and paste the token created in step 3, and click Register . This can be done from cli as well: license smart register idtoken <token> [force]

## Verify

- Show license summary

Smart Licensing is ENABLED.

```
Registration:
  Status: REGISTERED
  Smart Account: BU Production Test
  Virtual Account: TAC-CollabTesting
  Last Renewal Attempt: None
  Next Renewal Attempt: Jul 25 15:11:23 2018 IST
 
License Authorization:
  Status: AUTHORIZED
  Last Communication Attempt: SUCCEEDED
  Next Communication Attempt: Feb 25 15:12:59 2018 IST
 
License Usage:
  License                     Entitlement Tag                                                                        Count        Status
  --------------------------------------------------------------------------------------------------------------------------------------
                              regid.2017-02.com.cisco.UCM_CUWL,12.0_cc59375a-1cd8-4b36-8366-6f4d2abba965             0            Init
                              regid.2016-07.com.cisco.UCM_EnhancedPlus,12.0_d8372792-588c-4caa-b279-8587e5ce2f82     0            Init
  66d0d1cf-4863-4761-91d0-d01d3eb1949aregid.2016-07.com.cisco.UCM_Enhanced,12.0_66d0d1cf-4863-4761-91d0-d01d3eb1949a         5            InCompliance
  ef827a2f-f4ae-4ebb-887f-052737063d3aregid.2016-07.com.cisco.UCM_Basic,12.0_ef827a2f-f4ae-4ebb-887f-052737063d3a            2            InCompliance
                              regid.2016-07.com.cisco.UCM_Essential,12.0_25f9c396-c67c-4519-aa98-d4b3ad18f805        0            Init
                              regid.2016-07.com.cisco.UCM_TelePresenceRoom,12.0_d9a71418-29e9-4c9a-9d3a-1366ebe38e7c 0            Init
```

- Show license UDI

UDI: PID:UCM,SN:37624,UUID:6fe83addc80240bc92dc071ac7a37624

- Show license all

```
Smart Licensing Status
=======================
Smart Licensing is ENABLED
 
Registration:
  Status: REGISTERED
  Smart Account: BU Production Test
  Virtual Account: TAC-CollabTesting
  Export-Controlled Functionality: Allowed
  Initial Registration: SUCCEEDED on Jan 26 15:11:23 2018 IST
  Last Renewal Attempt: SUCCEEDED on Jan 26 15:11:23 2018 IST
  Next Renewal Attempt: Jul 25 15:11:23 2018 IST
  Registration Expires: Jan 26 15:06:21 2019 IST
 
License Authorization:
  Status: AUTHORIZED on Jan 26 15:12:59 2018 IST
  Last Communication Attempt: SUCCEEDED on Jan 26 15:12:59 2018 IST
  Next Communication Attempt: Feb 25 15:12:59 2018 IST
  Communication Deadline: Apr 26 15:06:59 2018 IST
 
Evaluation Period:
  Evaluation Mode: Not In Use
  EVALUATION PERIOD EXPIRED on Nov 9 23:46:35 2017 IST
 
License Usage
=============
License Authorization Status: AUTHORIZED as of Jan 26 15:12:59 2018 IST
 
 (regid.2017-02.com.cisco.UCM_CUWL,12.0_cc59375a-1cd8-4b36-8366-6f4d2abba965)
  Description: null
  Count: 0
  Version: 12.0
  Status: Init
 
 (regid.2016-07.com.cisco.UCM_EnhancedPlus,12.0_d8372792-588c-4caa-b279-8587e5ce2f82)
  Description: null
  Count: 0
  Version: 12.0
  Status: Init
 
UC Manager Enhanced License (12.x) (regid.2016-07.com.cisco.UCM_Enhanced,12.0_66d0d1cf-4863-4761-91d0-d01d3eb1949a)
  Description: UC Manager Enhanced License
  Count: 5
  Version: 12.0
  Status: InCompliance
 
UC Manager Basic License  (12.x) (regid.2016-07.com.cisco.UCM_Basic,12.0_ef827a2f-f4ae-4ebb-887f-052737063d3a)
  Description: UC Manager Basic License
  Count: 2
  Version: 12.0
  Status: InCompliance
 
 (regid.2016-07.com.cisco.UCM_Essential,12.0_25f9c396-c67c-4519-aa98-d4b3ad18f805)
  Description: null
  Count: 0
  Version: 12.0
  Status: Init
 
 (regid.2016-07.com.cisco.UCM_TelePresenceRoom,12.0_d9a71418-29e9-4c9a-9d3a-1366ebe38e7c)
  Description: null
  Count: 0
  Version: 12.0
  Status: Init
 
Product Information
===================
UDI: PID:UCM,SN:37624,UUID:6fe83addc80240bc92dc071ac7a37624
 
Agent Version
=============
Smart Agent for Licensing: 1.3.4
```

## Troubleshoot

Please collect these logs to troubleshoot issues related to registration:

- Packet capture from CUCM CLI

- License Manager logs

### Known Bugs

- Cisco bug ID CSCvh16069 : Cisco Smart licensing satellite cannot borrow a license from a higher level to make it in compliance.

- Cisco bug ID CSCvf86710 :  Cisco Smart License Manager platform service does not run.

- Cisco bug ID CSCvc94366

: CUCM smart license registration to Cisco License Central does not accept the proxy port 443.

## Related Information

- Technical Support & Documentation - Cisco Systems

### Revision History

4.0

04-Jun-2026

Replace references to "Cisco Smart Software Manager (SSM)" with "Cisco License Central."

3.0

20-Aug-2024

Added Alt Text.
Updated Style Requirements and Formatting.

2.0

14-Jul-2022

Updates made for style requirements, machine translation, gerunds, etc. to comply  with Cisco guidelines.

1.0

22-Mar-2018

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 4.0 | 04-Jun-2026 | Replace references to "Cisco Smart Software Manager (SSM)" with "Cisco License Central." |
| 3.0 | 20-Aug-2024 | Added Alt Text.
Updated Style Requirements and Formatting. |
| 2.0 | 14-Jul-2022 | Updates made for style requirements, machine translation, gerunds, etc. to comply  with Cisco guidelines. |
| 1.0 | 22-Mar-2018 | Initial Release |