---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-1000-217204-how-to-configure-in-meeting-chat-for-cms-html-a0428efa2f
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server-1000/217204-how-to-configure-in-meeting-chat-for-cms.html
retrieved_at: 2026-08-21T13:12:03.339689+00:00
---

How to Configure in Meeting Chat for CMS with Skype for Business

# How to Configure in Meeting Chat for CMS with Skype for Business

### Download Options

Updated: June 18, 2021

Document ID: 217204

Contents

## Contents

## Introduction

This document describes the steps required to configure in Meeting Chat for Cisco Meeting Server (CMS) interoperability with Skype for Business.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CMS general configuration

- CMS Application Programing Interface (API)

### Components Used

The information in this document is based on CMS version 3.2.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configuration

Step 1. Create a new CallProfile via API.

- Access CMS via Webadmin and navigate to Configuration/API/v1/CallProfile .

- Create a new CallProfile and modify the next parameter as shown in the image:

chatAllowed: true

Note : The chatAllowed parameter has the next options available to be configured: true , false and unset .

Step 2. Assign the CallProfile to the space.

- Open the Webadmin and  navigate to Configuration/api/v1/coSpaces .

- Select the space required to assign the CallProfile created in Step 1.

CallProfile: 27340a55-78cc-4179-a47d-b346cf7f7340

Note : If parameter chatAllowed is configured to unset then chat must not be displayed or must be grayed out.

## Verify

Verify if the configuration is applied successfully.

- Start a call to the space where the CallProfile is assigned and send messages to users in the conference.

- If all configuration is correct, messages must be displayed in the Skype for Bussiness side as shown in the image:

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Contributed by Cisco Engineers

Moises Martinez