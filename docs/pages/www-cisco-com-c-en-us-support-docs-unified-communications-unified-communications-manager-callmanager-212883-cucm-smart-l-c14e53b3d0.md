---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-212883-cucm-smart-l-c14e53b3d0
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/212883-cucm-smart-licensing-mediated-model.html
retrieved_at: 2026-08-16T17:57:07.613629+00:00
---

Configure Mediated Model to Synchronize CUCM with Smart Accounts

# Configure Mediated Model to Synchronize CUCM with Smart Accounts

### Download Options

Updated: June 4, 2026

Document ID: 212883

Contents

## Contents

## Introduction

This document describes mediated model configuration to synchronize your Cisco Unified Communications Manager (CUCM) with your Smart accounts.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Communications Manager (CUCM) version 12.0

- Cisco License Central Satellite

### Components Used

The information in this document is based on these software and hardware versions:

- Cisco Call Manager version 12.0

- Cisco License Central Satellite

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

Cisco Smart Software Licensing simplifies the licensing experience across the enterprise making it easier to purchase, deploy, track and renew Cisco Software. It provides visibility into license ownership and consumption through a single, simple user interface.

- You place an order on Cisco Commerce and associate the order with smart account. This information is populated on Cisco License Central, which resides on Cisco.com. Now, you have complete view of your orders and purchases.

- Direct Model- Customer Licensing information is where security is not a major concern. You can use HTTPS proxy or Transport Gateway to allow devices to talk to the through private network. This becomes the centralized access point for Cisco License Central. All of this is HTTPS so it is secured.

- Mediated Deployment Model- This is for those who have security concerns. You do not want your devices to talk directly to Cisco.com from your private network. You can install Cisco License Central Satellite on a VM, which resides on your premises, and acts as Cisco License Central. It can be synchronized with Cisco License Central on Cisco.com monthly, weekly, or totally disconnected. If you do not have an internet connection from your network, you can do file upload and download. All it needs to have is the synchronization to know the entitlement, as recommendation is to do the sync in 30 days.

### Where do I Create Smart Accounts

- To create a Customer Smart Account, log into CSC with your CCO ID and initiate a request for a Customer Smart Account.

- To create a Partner Holding Smart Account, log in to CSC with your CCO ID and initiate a request for a Partner Holding Account.

- You can also initiate a request for either type of Smart Account when ordering in CCW. Although, the recommended best practice is to proactively set up your Smart Accounts.

Note : There is no upper limit; you can create as many Virtual Accounts as your company needs.

### Cisco Smart License Manager Service

Cisco Smart License Manager Service is a network service running only on CUCM publisher. Since this is a network service, it runs all the time and cannot be started or stopped from UI or CLI. Since no service runs on subscriber, none of the smart licensing operations can be done from the sub. The CLI commands also do not provide any output on sub,

### Smart Licensing States in UCM

There are two main statuses in Smart Licensing :

Registration Status:There are 3 registration status types:

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

In addition to the previous smart licensing statuses, UCM provides an overage period of 90 days (This is a concept already present in pre 12.0 with classic licensing. UCM can continue providing the overage period with smart licensing as well).

## Configure (Mediated Deployment)

### Prerequisites

These ports must be enabled for communication with Cisco License Central:

- User Interface: HTTPS (port 8443)

- Product Registration: HTTPS (port 443), HTTP (port 80)

- Communication to Cisco License Central: HTTPS (tools.cisco.com, api.cisco.com, cloudsso.cisco.com), port 443

There are 2 deployment options under mediated deployment model,

Connected using Proxy Server: Here you can use the proxy server to facilitate connectivity between CUCM and Smart Account.

Disconnected: Used when there is NO direct connectivity from CUCM / Satellite to Cisco.com. Smart Account Synchronization must be done using file upload and download manually.

### Configuration (Satellite)

- Log in to satellite. Configure as new satellite. Verify Network settings. Configure valid NTP server.

Note : For the first time log in, the default credential for satellite log in is Admin/Admin!23.

- Choose Manual Setup and download the Registration File.

Log into your Smart Account in Cisco License Central .

Navigate to Satellites under the section of Cisco License Central and click New Satellite... button  Add a new satellite. Associate the newly created virtual account to the satellite. Once this is done, generate the authorization file.

In order to complete registration process, navigate to the satellite log in and upload the authorization file. Satellite restarts. Now the satellite is synced to the virtual account.

Log in to satellite and generate a token.

Navigate to CUCM admin page > System > Licensing > License Management > View/Edit the Licensing Smart Call Home settings and then set the Cisco License Central satellite URL to Device Request Handler (10.106.81.131 is the IP address of the satellite configured) and save , as shown in the image.

- Click Register and paste the token generated in step 6.

### Configuration (Proxy Server)

- Instead of using satellite server, you can also use proxy server. If CUCM is already registered via Direct Method or satellite, first deregister and navigate to System > Licensing > License management . Here you have Actions Tab, selectderegister .

- If CUCM is not registered, directly choose View/Edit , the licensing Smart Callhome settings. Here add proxy server details, and be sure that proxy server has connectivity to tools.cisco.com so that CUCM can be synced to the virtual account via proxy server.

- Generate Token request from virtual account.

- Navigate to CUCM . Here, click register and paste the token copied in Step 3.

## Verify

Show license summary.

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

Show license UDI.

```
UDI: PID:UCM,SN:37624,UUID:6fe83addc80240bc92dc071ac7a37624
```

Show license all.

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

Collect the logs for troubleshooting issues related to registration:

- Packet capture from CUCM CLI

- License Manager logs

- Diagnostic logs from satellite

### Known Bugs

- Cisco bug ID CSCvh16069 : Cisco Smart licensing satellite cannot borrow license from higher level to make it compliant.

- Cisco bug ID CSCvf86710 : Cisco Smart License Manager platform service does not run.

- Cisco bug ID CSCvc94366 : CUCM smart license registration to Cisco License Central does not accept the proxy port 443.

- Cisco bug ID CSCvh72897: Unable to use proxy server when authorization is enabled on proxy server.

## Related Information

### Revision History

3.0

04-Jun-2026

Replace references to "Cisco Smart Software Manager (SSM)" with "Cisco License Central."

2.0

14-Jun-2023

Added Alt Text.
Updated Title, Machine Translation, Style Requirements and Formatting.

1.0

12-Mar-2018

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 3.0 | 04-Jun-2026 | Replace references to "Cisco Smart Software Manager (SSM)" with "Cisco License Central." |
| 2.0 | 14-Jun-2023 | Added Alt Text.
Updated Title, Machine Translation, Style Requirements and Formatting. |
| 1.0 | 12-Mar-2018 | Initial Release |