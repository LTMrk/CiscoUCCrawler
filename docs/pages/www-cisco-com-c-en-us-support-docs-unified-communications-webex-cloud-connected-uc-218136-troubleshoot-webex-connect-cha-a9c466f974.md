---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-cloud-connected-uc-218136-troubleshoot-webex-connect-cha-a9c466f974
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-cloud-connected-uc/218136-troubleshoot-webex-connect-chat-creation.html
retrieved_at: 2026-08-21T12:49:13.468835+00:00
---

Troubleshoot Webex Connect Chat Creation Failure Error at Create Task Node

# Troubleshoot Webex Connect Chat Creation Failure Error at Create Task Node

### Download Options

Updated: September 7, 2022

Document ID: 218136

Contents

## Contents

## Introduction

This document describes one possible reason why the initial chat creation fails to the Create Task node.

Error seen:

Contributed by Bhushan Suresh - Cisco TAC Engineer

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Webex Contact Center (WxCC) 2.0

- Webex connect portal with Email flows configured

### Components Used

The information in this document is based on these software versions:

- WxCC 2.0

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Problem

When you open the flow and enable Decrypted debug logs, the error value is mandatory , name : origin is seen at the Create Task node:

Error Description:

```
status : 4002 , desc : value is mandatory , name : origin [ id : 3f5a23f9-6770-84c5-c9ea-8baa649950ce]
```

## Reason for the Failure

The issue resides in the Origin field. Double-click the Create Task node and check these 3 fields:

Access the variables passed on the Create Task node through Input Variables > Receive and check the Name and Email fields. This must MATCH the variables in the earlier image.

These two fields are set through the Chat template where the Name and the Email fields are mandatory.

## Solution

Ensure the Name and Email parameters have the Name set to Name and Email :

If you would like to have the field Name and Email fields named differently, (Email parameter is named as eMail and not Email )

.

Please ensure the fields are updated the same on the Create Task node or the Create Task for the chat fails.

### Revision History

1.0

07-Sep-2022

Initial Release

### Contributed by Cisco Engineers

Bhushan Suresh

Technical Consulting Engineer

### This Document Applies to These Products

- Webex Cloud-Connected UC

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 07-Sep-2022 | Initial Release |