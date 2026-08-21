---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-calling-222146-identify-procedure-to-modify-caller-id-n--58cff83ae5
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-calling/222146-identify-procedure-to-modify-caller-id-n.html
retrieved_at: 2026-08-21T07:15:32.253560+00:00
---

Identify Procedure to Modify Caller ID Name when a User Extension Is Reassigned

# Identify Procedure to Modify Caller ID Name when a User Extension Is Reassigned

### Download Options

Updated: July 18, 2024

Document ID: 222146

Contents

## Contents

## Introduction

This document describes the procedure for customers to modify the caller ID name of a user extension that is reassigned to another owner/user.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Webex Calling

- Control Hub

- New users creation

## Component Used

The information in this document was created from the devices in a specific lab environment. All the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

Tip : Cisco always recommends not to re-use Webex Calling users/accounts to avoid any conflict and, as best practice, delete the user that is no longer in use and create a new one.

Is common for administrators to reassign users in their organization that are no longer in use when a previous owner leaves the company or there are not enough licenses.

Administrators normally modify the Identity information of the user to be reassigned.

User Identity Configuration. Configuration of Previous Owner.

User Identity configuration. Configuration of new owner.

However, when new owner executes a call, the caller ID name still shows the previous owner name in the screen of the user that receives the call (NY Testing, in this case).

Its important to remember that the Identity information configured in Control Hub correspond only to the user configuration, but not for the calling configuration.

Caller ID name is a SIP configuration delivered in the From header of a SIP invite to be used for the destination party to identify the originator name.

Therefore, to ensure that destination numbers display the current owner caller ID name, the Caller ID first name and Caller ID last name fields must be updated with the next steps:

Step 1. Navigate to User > Calling > Numbers > Caller ID and modify Caller ID first name and caller ID last name accordingly.

Step 2. Click Save .

Calling ID configuration section.

Now the destination is able to see the correct caller ID name of the originator user in their Multi Platform Phone or Webex App.

Note : This procedure applies for most of the received cases. If the issue persist, do not hesitate to reach TAC opening a case for further analysis.

### Revision History

1.0

19-Jul-2024

Initial Release

### Contributed by Cisco Engineers

Mitzi Fuentes

Technical Consulting Engineer

### This Document Applies to These Products

- Webex Calling

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 19-Jul-2024 | Initial Release |