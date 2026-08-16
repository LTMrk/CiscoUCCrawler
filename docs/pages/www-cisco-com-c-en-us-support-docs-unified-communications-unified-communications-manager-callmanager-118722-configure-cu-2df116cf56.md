---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-118722-configure-cu-2df116cf56
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/118722-configure-cucm-00.html
retrieved_at: 2026-08-16T18:54:27.271177+00:00
---

CUCM and CUC Meet Me Conference with User Authentication Configuration Example

# CUCM and CUC Meet Me Conference with User Authentication Configuration Example

### Download Options

Updated: January 23, 2015

Document ID: 118722

Contents

## Contents

## Introduction

This document provides an example of how to configure the Meet Me feature with User Authentication. The Meet Me feature is available in Cisco Unified Communications Manager (CUCM), and the Authentication is achieved with the help of Cisco Unity Connection (CUC).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of CUCM and CUC.

### Components Used

The information in this document is based on CUCM / CUC Release 8.x and later, but might also apply to earlier releases of CUCM / CUC.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Design

Meet Me conferences allow users to dial-in to a conference. This requires that a directory number be allocated for exclusive use of the conference. The users call the directory number in order to join the conference. Here Authentication is not required and the users are connected to the conference call. More information can be found in the System Guide .

In order to enable User Authentication, the call is transferred via CUC. The User System Transfer Conversation is used in order to authenticate the caller. For this purpose, a user is created on CUC. This conversation prompts callers to sign in to CUC. After callers enter the CUC ID and PIN, CUC prompts them to enter the number to which they want to be transferred.

### Call Flow

Caller dials 5000 > Computer Telephony Integration (CTI) Route Point with Extension 5000 set to Call Forward All to Voice Mail > Call Handler with extension 5000 > Caller provides ID and PIN > Caller dials the Meet Me Number (5002) > Call transferred to Meet Me Number on CUCM.

## Configure

For details on Voice Mail Profile Configuration and appropriate selection of Calling Search Space (CSS), refer to the SCCP Integration Guide or SIP Integration Guide .

For external callers, a translation pattern is required in order to translate the called number. This document does not provide information about number translations. In order to configure translations on CUCM, refer to the Translation Pattern Configuration document. In order to configure translations on Gateway, refer to the Number Translation using Voice Translation Profiles document.

Here are the steps to configure the Meet Me feature with User Authentication:

- Assign appropriate CSS and Voicemail Profile to the Extension 5000 and set Forward All to VM.

- [Optional] In order to call from an external number, configure the appropriate translation patterns on the Gateway or CUCM to convert the called number to 5000.

- Select My Personal Recording under Callers Hear Section.

- Select the User System Transfer Conversation under the After Greeting section.

- Click Play/Record in order to record a Greeting. The Greeting could be "Welcome to Cisco...". If you do not need a Greeting, select Nothing under the Callers Hear section.

- Modiy the CSS of the Voicemail Ports or the Rerouting CSS of the Session Initiation Protocol (SIP) trunk. This CSS should have the partition of the Meet Me Number.

- Configure the Meet Me Number. Refer to Meet-Me Number/Pattern Configuration for more information.

- Create a SoftKey Template to include the Meet-Me Softkey. Associate this template to the phones that will initiate the conference.

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

1.0

23-Jan-2015

Initial Release

### Contributed by Cisco Engineers

Aravind Krishna Murthy and Anirudh Mavilakandy

Cisco TAC Engineers.

### This Document Applies to These Products

- Unified Communications Manager (CallManager)

- Unity Connection

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 23-Jan-2015 | Initial Release |