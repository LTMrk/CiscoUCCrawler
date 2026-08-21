---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-calling-222153-recognize-how-dial-by-name-works-html-a4339b94a7
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-calling/222153-recognize-how-dial-by-name-works.html
retrieved_at: 2026-08-21T07:16:19.171174+00:00
---

Recognize how Dial by Name Works

# Recognize how Dial by Name Works

### Download Options

Updated: July 19, 2024

Document ID: 222153

Contents

## Contents

## Introduction

This document describes how Dial by Name Works for Auto Attendant menu option or Monitored lines when a user name is filtered.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Webex Calling

- Control Hub

- Auto Attendant Configuration

- Monitoring Lines

### Components Used

This document is not restricted to specific hardware or software requirements.

The information in this document was created from the devices in a specific lab environment. All the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

Administrators have the option to assign the Dial by Name function to a keypad number in an Auto Attendant, so originators can look for the user name when they do not know the extension assigned.

Another use of the caller ID is when they have users to be monitored. They can select some users from their organization to be displayed in their Multi Platform Phone (MPP) or Key Expansion Modules (KEM).

## How Dial by Name Works

TAC usually receives cases reporting originators cannot find a specific user name during a Dial by Name search in an Auto Attendant menu or looking for a user in their monitored lines, even when the name is not repeated in the organization. For example, an originator looks for Daniel Mendes, and it is the only Daniel in the organization, but the originator gets a message error that says the party was not found.

However, when the configuration is reviewed, it is common to find the caller ID name and last name do not match with the user details name.

User Details Screen

Calling-Caller ID First Name and Caller ID Last Name Configuration

In the previous example, it can be observed that the account name is Daniel Mendes but the caller ID name is Jane Doe. So, when the user was introduced during the Auto Attendant call, there was no one found for a Daniel even when he is the only one in their organization.

When a name is introduced in the phone keypad, the servers look for the entry name and compare it versus the data contained in the caller ID first name and caller ID last name configured for the users, not the account name.

So, if the originator would look for Jane, the call would have been transferred to Daniel Mendes.

This scenario is common when an account could have changed owner or the caller ID parameter was filled with any other data.

It is recommended that the administrator always confirm the Account name matches with the caller ID name. Once confirmed, any originator would be able to find a user.

### Revision History

1.0

19-Jul-2024

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 19-Jul-2024 | Initial Release |