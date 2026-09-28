---
doc_id: www-cisco-com-c-en-us-support-docs-collaboration-endpoints-wireless-ip-phone-8821-201021-troubleshoot-8821-ip-phone-disp-e675f06b6c
source_url: https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/wireless-ip-phone-8821/201021-troubleshoot-8821-ip-phone-display-mic.html
retrieved_at: 2026-08-17T01:16:17.591499+00:00
---

Troubleshoot 8821 IP Phone Display "MIC Not Installed" Error - Solved

# Troubleshoot 8821 IP Phone Display "MIC Not Installed" Error - Solved

Updated: April 24, 2018

Document ID: 201021

Contents

## Contents

## Introduction

This document describes the guideline to troubleshoot the Cisco Wireless 8821 IP Phone when it displays the error message "MIC not installed " on screen caused by defect CSCvc65418 which was resolved through fix of CSCve44412 .

Note : Manufacturing Installed Certificate (MIC), where MIC does not refer to a microphone.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Wireless IP Phone 8821 and 8821-EX User Guide

- Cisco Wireless IP Phone 8821 and 8821-EX Wireless LAN Deployment Guide

### Components Used

The information in this document is based on the hardware and software version:

- Model = CP-8821

- Version = 11.0(3)SR3 ()

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is in live production, ensure that you understand the potential impact of any command.

## Background Information

The MIC certificate can be used for the wireless authentication (for instance Extensible Authentication Protocol (EAP) - Transport Layer Security (TLS) as well as other security features/interfaces:

- Cisco Unified Communications Manager (CUCM) Encrypted/Authenticated device security mode

- HTTPS

- Secure Shell (SSH)

- Simple Certificate Enrollment Protocol ( SCEP) Proof of Identity (POI)

In order to troubleshoot the 8821 IP Phone when it displays "MIC not installed", there are several steps that must be followed:

### Step 1. Confirm the Error Message

Verify that the phone displays the "MIC not installed" error message on the screen as shown in the image:

If the error has disappeared, verify it is present as a status message:

- Navigate to Settings > Admin settings > Status > Status messages .

### Step 2. Restore Functionality

If not required for the wireless authentication or SCEP, the MIC can be replaced with Locally Significant Certificate (LSC) with the use of CUCM Certificate Authority Proxy Function (CAPF) so the phone operates normally. Install an LSC on the phone once the error message is confirmed and test once more. Ensure By Null String or By Authentication String is selected for the Authentication Mode in order for the LSC to be installed successfully despite the fact that MIC is not present.

In 11.0(3)SR3.2, the "MIC Not Installed" message in the status bar is supressed when the LSC is installed on the phone. The message is displayed for the first 10 seconds after power on. For earlier loads, a LSC can be installed on the phone and function but the “MIC Not Installed” message continues to be displayed on the phone’s status bar.

### Step 3. Prevent New Occurrences

Upgrade all Cisco 8821 phones to 11.0(3)SR3.2 or higher as soon as possible, as the issue has been fixed from this version onwards. For devices that have already displayed this error message, an upgrade will not recover the MIC. The code that contains the fix for CSCvc65418 (resolved through fix of CSCve44412 ) prevents disappearance of the MIC in the first place.

For further assistance or if the MIC is required for wireless authentication on an affected phone, contact Cisco TAC for a Return Material Authorization (RMA).

## Related Information

### Contributed by Cisco Engineers

Larry Lam

Cisco TAC Engineer

Ricardo Garcia Duarte

Cisco TAC Engineer

David Spindola

Cisco TAC Engineer