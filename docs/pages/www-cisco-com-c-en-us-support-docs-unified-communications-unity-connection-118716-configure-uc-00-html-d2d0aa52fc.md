---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unity-connection-118716-configure-uc-00-html-d2d0aa52fc
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-connection/118716-configure-uc-00.html
retrieved_at: 2026-08-16T18:54:35.614165+00:00
---

Unity Connection PreGreetings Recording Configuration Example

# Unity Connection PreGreetings Recording Configuration Example

### Download Options

Updated: January 21, 2015

Document ID: 118716

Contents

## Contents

## Introduction

This document describes how to configure a Common Greeting such as an introductory Welcome Message before every user's or Call Handler's Greeting.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of Cisco Unity Connection (UC).

### Components Used

The information in this document is based on UC Versions 8.X and later but might work for earlier versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Design

A standard greeting (for example, "Welcome to Cisco...") must be played before every user's Personal Recording or before a Call Handler Greeting.

Here are some examples:

- A call is forwarded to John's mailbox: " Welcome to Cisco. Hello, This is John. I'm not available....... "

- A call is forwarded to Peter's mailbox: " Welcome to Cisco. Hi, This is Peter. Please leave a message....."

- A call is forwarded to a Call Handler: " Welcome to Cisco . Thank you for calling....."

- A call is forwarded to a Directory Handler: " Welcome to Cisco. Spell the Last and First Name....."

This document provides an example to configure a PreGreeting Recording for a call transferred to a user's mailbox or Call Handler with the use of the Forwarded Routing Rule.

Note : In order to configure a similar greeting before a user signs in, complete the same steps and use the Direct Routing rule instead of the Forwarded Routing Rule.

The Call Handler for the Pre-GreetingMessage can also be configured to accept Call Inputs to transfer the call to a user extension, external number, or Directory Handler.

## Configure

Here is an overview of the configuration:

- Create a New Call Handler (for example, PreGreetingsMessage) and record the message.

- Create a New Forwarded Routing Rule (for example, PreGreetingsRule) with no Conditions (without conditions, all calls will match this rule).

- Configure the PreGreetingsRule Forwarded Routing Rule in order to send the call to PreGreetingsMessage Call Handler.

- Configure the PreGreetingsMessage Call Handler in order to choose the After Greeting option as a Call Action and select Route from Next Call Routing Rule from the drop-down menu.

- Configure Caller Input for the PreGreetingsMessage Call Handler if required.

### Create a New Call Handler

- Log into UC Administration with an Administrator account.

### Create a New Forwarded Routing Rule

- Navigate to Call Routing > Forwarded Routing Rule and create a new Routing Rule called PreGreetingsRule.

- In the Send Call to section, select Call Handler and select PreGreetingsMessage from the drop-down menu.

### Configure the New Call Handler

- Navigate to Call Management > System Call Handlers and select PreGreetingsMessage .

- Go to Edit > Greetings and select Standard .

- Under the Callers Hear section, select My Personal Recording .

- Under the After Greeting section, select Call Action and choose Route From Next Call Routing Rule from the drop-down menu.

### Configure Caller Input

If the call is transferred to voicemail, this feature gives the caller the option to transfer the call to a Directoy Handler rather than leave a message. Caller Inputs can also be set to transfer the call to an Operator, Opening Greeting, or Caller System Transfers. This example uses the Directory Handler for the transfer.

Here is an example:

- A call is forwarded to John's mailbox: " Welcome to Cisco. Press 9 to search for a user. Hello, This is John. I'm not available.... "

- A call is forwarded to Peter's mailbox: " Welcome to Cisco. Press 9 to search for a user. Hi, This is Peter. Please leave a message...."

Complete these steps in order to configure caller input.

- Navigate to Call Management > System Call Handlers and select PreGreetingsMessage .

- Go to Edit > Caller Input and select Key 9 .

- Under Action, choose Directory Handler and select the Directory Handler Name from the drop-down menu.

Here are some other options:

- In order to transfer the call to a defined extension, select Transfer to Alternate Contact Number and define the extension under Action.

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

1.0

21-Jan-2015

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 21-Jan-2015 | Initial Release |