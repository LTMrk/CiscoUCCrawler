---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-windows-116433-probsol-jabber-00-html-db1f79ed22
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber-windows/116433-probsol-jabber-00.html
retrieved_at: 2026-08-21T06:59:37.679767+00:00
---

Jabber Displays Incorrect Contact for a Number

# Jabber Displays Incorrect Contact for a Number

### Download Options

Updated: April 13, 2022

Document ID: 116433

Contents

## Contents

## Introduction

This document describes a method to resolve a common Jabber softphone name resolution issue.

## Problem

When a call is made to a Jabber softphone, the Jabber softphone attempts to look up the number of the incoming call, and then resolve the number to a user name if it can be found.

Sometimes Jabber for Windows displays an incorrect display name for a specific calling number.

In order to resolve names to numbers, Jabber looks at three things in this order to find a resolution:

- Local Jabber Cache of Jabber Contacts and Recents

- Outlook Contacts

- Lightweight Directory Access Protocol (LDAP) Directory

The search takes place in a top-down fashion. As soon as a number is resolved to a name, it displays that contact information.

Unfortunately, once there is incorrect information in the local cache, the cache must be deleted. It is most often found that Jabber picks up an Outlook Contact that has incorrect information. However, when this information is used once by Jabber, it is cached and then further lookups are never done for this number again.

## Solution

Once the problem is identified, the only solution is to find the Jabber cache of the Jabber client that is displayed incorrectly, and delete the cache.

The cache is stored in a folder called “Jabber” which can be found at this location:

```
C:\Users\<User>\AppData\Local\Cisco\Unified Communications\
```

- Exit Jabber and delete the "Jabber" folder.

- Restart Jabber.

- Before you test, check the Outlook Contact on the PC that showed the incorrect display name for the proper contact information.

- If the contact information is valid, then also check the LDAP directory in order to ensure the proper contact information for the users involved in the call.

### Revision History

2.0

13-Apr-2022

Corrected a typographical error.

1.0

13-Nov-2013

Initial Release

### Contributed by Cisco Engineers

Joshua Hammonds

Cisco TAC Engineer

Scott Hills

Cisco TAC Engineer

### This Document Applies to These Products

- Jabber for Windows

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 13-Apr-2022 | Corrected a typographical error. |
| 1.0 | 13-Nov-2013 | Initial Release |