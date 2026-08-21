---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-telepresence-management-suite-tms-217657-how-to-apply-workaround-of-tms--d1fd361d61
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/telepresence-management-suite-tms/217657-how-to-apply-workaround-of-tms-enhanceme.html
retrieved_at: 2026-08-21T06:28:31.641975+00:00
---

How to Apply workaround of TMS Enhancement CSCvf19937

# How to Apply workaround of TMS Enhancement CSCvf19937

### Download Options

Updated: January 26, 2022

Document ID: 217657

Contents

## Contents

## Introduction

This document describes how to configure participant templates within Telepresence Management Suite (TMS), in order to connect external participants which require Dual Tone Multi-Frequency (DTMF) to join.

## Prerequisites

Cisco recommends that you have knowledge of these topics:

- TMS web admin page management.

- Cisco Meeting Server (CMS).

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Problem

Enter the string of DTMF digits to be sent after a call has connected, if needed. A DTMF sequence is used to dial systems with keypad/tone navigation menus, such as an audio bridge.

There are some other scenarios where DTMF are required to be sent :

- WebEx requires DTMF digits to be sent out of band to external dial-out participants.

- Telepresence Server (TS) does not support Request For Comment (RFC) 2833 for outbound as per Cisco bug ID CSCur49008

- CMS does support RFC 2833, but it can't be scheduled via TMS as under the Connection Settings tab on the conference, it does not show settings for the DTMF tones to be entered in.

## Solution

### Create Participant Template

In order to adress this situation, participant templates with DTMF tones configured can be used to connect external (non-TMS managed systems) into the conference.

Step 1. Open TMS web admin page with the https://<FQDN>/tms on a web browser tab.

Step 2. Navigate to Booking > Participant Templates.

Note : Participant templates are only available when booking directly in Cisco TMS, they cannot be used with Smart Scheduler, Cisco TMSXE, or any other application that uses Cisco TelePresence Management Suite Extension Booking Application Programing Interface (API).

Step 3. Under Participant Templates section select New.

Step 4. Add a name for the template and select the Dial Out option under Direction drop-down menu.

Step 5. Configure the number of alias to be dialed by this participant under the Number field, and the DTMF tones to be sent within the DTMF Tones configuration field and select Ok in order to save the changes.

Note : The DTMF sequence can contain the digits 0-9, the star/asterisk character (*), the hash/pound character (#), and the comma character (,).

### Apply Participant Template

In order to apply the previously created participant template and apply it to a conference follow the next stpes:

Step 1. Create a new meeting, navigate to Booking > New Conference.

Step 2. When general details about the meeting are added along with the required participants, select the option Add Participants. A pop-up window with Add Participants sub-menú now shows the options.

Step 3. Navigate to Templates tab. Select the Participant Template box, and select the > button, in order to complete the process and select Ok in order to save the changes.

Step 4. Review the meeting takes place and verify the participant can join to the meeting as expected.

### Revision History

1.0

25-Jan-2022

Initial Release

### Contributed by Cisco Engineers

Amadeus Ubaldo

### This Document Applies to These Products

- TelePresence Management Suite (TMS)

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 25-Jan-2022 | Initial Release |