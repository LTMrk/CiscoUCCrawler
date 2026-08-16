---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unity-connection-213808-configure-direct-transfer-to-unity-con-12b9b70684
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-connection/213808-configure-direct-transfer-to-unity-conne.html
retrieved_at: 2026-08-16T18:51:47.392298+00:00
---

Configure Direct Transfer to Unity Connection Mailbox with Extension Wildcard

# Configure Direct Transfer to Unity Connection Mailbox with Extension Wildcard

### Download Options

Updated: October 10, 2018

Document ID: 213808

Contents

## Contents

## Introduction

This document describes how to transfer calls directly into a voicemail box with extension mask in Cisco Unity Connection (CUC). Contributed by Luis Gomez, Cisco TAC Engineer.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Unity Connection

- Cisco Unfied Communication Manager (CUCM)

### Components Used

The information in this document is based on CUC Release 9.X or later integrated via Session Initiation Protocol (SIP) or Skinny Call Control Protocol (SCCP) with CUCM 9.x or later.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configuration

Step 1. Create a new Voice Mail Profile on CUCM:

Navigate to Advance Features > Voice Mail > Voice Mail Profile > Add New

Voice Mail Profile Name

Use a distinguished name for this Profile

Assign the pre-configured pilot number and Calling Search Space (CSS) for current integration, use Route Pattern if SIP or Hunt Pilot if SCCP

Similar as shown in the image:

Step 2. Create a new CTI Route Point on CUCM:

Navigate to Device > CTI Route Point > Add New , configure these settings:

Similar as shown in the image:

Step 3.  Configure the Directory Number for CTI

Add a New Line under the Association section , configure the Directory Number as asterisk+wildcard  to match dial plan of users extensions:

Similar as shown in the image:

Under Call Forward and Call Pickup Settings select Forward All to Voice Mail option:

## Verify

Transfer to any pattern that match *XXXX reach the CTI Route Point, the Voicemail Box mask XXXX allows only 4 digit extension to be routed, Unity Connection receives the call as a forwarded call to that extension and send caller directly to user's mailbox.

## Troubleshoot

For transferred call that reach CUC Default Opening Greeting use Remote Port Status Monitor (rPSM) for Unity Connection to verify the transfer extensions.

### Contributed by Cisco Engineers

Luis Gomez

Cisco TAC Engineer

### This Document Applies to These Products

- Unity Connection

| Voice Mail Profile Name | Use a distinguished name for this Profile |
|---|---|
| Description | Optional |
| Voice Mail Pilot | Assign the pre-configured pilot number and Calling Search Space (CSS) for current integration, use Route Pattern if SIP or Hunt Pilot if SCCP |
| Voice Mail Box Mask | Use a wildcard to match the dialing plan of users extension, for example: use XXXX to match 4 digit extensions dial plan |
| Make this the default Voice Mail Profile for the System | Unchecked |

| Device Name | Use a distinguished name for this Route Point |
|---|---|
| Description | Optional |
| Device Pool | Use pre-configured Device Pool for Voice Mail Integration |
| Calling Search Space | Use pre-configured CSS for Voice Mail Integration |