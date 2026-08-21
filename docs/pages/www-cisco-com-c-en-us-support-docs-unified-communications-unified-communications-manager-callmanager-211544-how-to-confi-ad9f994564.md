---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-211544-how-to-confi-ad9f994564
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/211544-How-to-Configure-Conference-Now-Feature.html
retrieved_at: 2026-08-21T13:56:24.319124+00:00
---

How to Configure Conference Now Feature in CUCM 11.X

# How to Configure Conference Now Feature in CUCM 11.X

### Download Options

Updated: August 7, 2017

Document ID: 211544

Contents

## Contents

## Introduction

This document describes a new feature Conference Now , in Cisco Unified Communications Manager (CUCM).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of Media resources on Call Manager.

### Components Used

The information in this document is based on CUCM version 11.5.0.99838-4.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

The Conference Now feature allows both external and internal callers to join a conference by dialing a Conference Now IVR Directory Number, which is a centralized conference assistant number. An IVR application guides the caller to join the conference by playing announcements. After the host enters both Meeting Number and PIN correctly, a conference bridge is allocated based on the Media Resource Group List (MRGL) of the host. Participants, who join before the meeting starts, are redirected to the same conference bridge. The host can set the Attendees Access Code for a secure conference call.

## Configure

This is a procedure to configure the Conference Now feature.

### Configurations

Step 1. Configure the Conference Now.

Navigate to Call Routing > Conference Now , as shown in the image:

Here keep the Conference Now DN in Partition which is accessible with respective Calling Search Space (CSS).

Step 2. Now under Device and assign the Owner User.

Navigate to Device > Phone and search for the device.

Select the correct Device .

Here select Owner as User and assign the Owner User ID . Here cisco is used as O wner User ID.

Step 3. As shown in the image, navigate to User Management > End User .

Search for the user and select the user assigned on Phone in Step 2.

Keep the user PIN. This pin is used if you are the Host of the meeting.

Step 4. Select the checkbox for Enable End User to Host Conference Now , as shown in the image:

## Verify

To verify your configuration, Call to Conference Now Directory Number(DN)  i.e 3030 . Enter the meeting number 3002 followed by # key.

As a Host please keep the pin configured in step 3. Now for other participant please share the meeting number 3002 and Participant Code 1234 .

## Troubleshoot

Troubleshooting steps for this configuration are covered in a separate document .

### Contributed by Cisco Engineers

Sachin Kalekar

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager (CallManager)