---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-213403-configure-jabber-version-12-0-in-phone-m-html-4c9ee468dd
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber/213403-configure-jabber-version-12-0-in-phone-m.html
retrieved_at: 2026-08-16T23:36:58.117820+00:00
---

Configure Jabber in Phone Mode for Contacts

# Configure Jabber in Phone Mode for Contacts

### Download Options

Updated: January 5, 2022

Document ID: 213403

Contents

## Contents

## Introduction

This document describes how to implement contacts for Cisco Jabber that are used in Phone Mode.

## Prerequisites

### Requirements

Cisco recommends you have a knowledge of:

- Cisco Unified Communications Manager (CUCM)

- Instant Messaging and Presence (IM&P)

- Cisco Jabber for Windows

### Components Used

The information in this document is based on these software versions:

- Cisco Jabber for Windows 12.0(0) or later.

- Cisco Unified Communications Manager (CUCM) version 11.5(1)SU4 (11.5.1.14900-11)

- Instant Messaging & Presence (IM&P) version 11.5(1)SU4 (11.5.1.14900-32)

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

Cisco Jabber for Windows version 12.0 introduces support for contacts, and even phone presence, when you use it in Phone Mode (formerly known as Phone Only Mode). The use of PRODUCT_MODE=Phone_Mode during the .msi installation is no longer required (as stated in the On-Premises Deployment guide for Cisco Jabber). In order to allow contacts to be stored, when Cisco Jabber version 12.0 uses a Unified Communication (UC) Service Profile with no IM&P servers configured (that is, Phone Mode), a GLOBAL IM&P setting must be changed.

Note : Jabber in Phone Mode with contacts uses the IM&P server as its contact list server (changes to the settings on the IM&P server affect all the users of Instant Messaging Server).

In order for contacts to be used in Phone Only Mode, Enable instant messaging must be unchecked on your IM&P servers (so no one would be able to use instant messaging) as shown in the image; however, that disables the Instant Messaging icon from all the Cisco Jabber clients.

Enable availability sharing can also be Unchecked (if presence is not desired) as shown in the image:

After you uncheck the boxes for both Enable instant messaging and Enable availability sharing , then restart the Cisco XCP Router service on all nodes, you can then use a UC Service Profile with no IM&P server and contacts are displayed by Cisco Jabber for Windows 12.0 clients.

Note : If you want the Jabber users to show their Presence status, the IM and Presence server is required.

In order for the contacts to be displayed, the check box for Enable User for Unified CM IM and Presence (Configure IM and Presence in the associated UC Service Profile) does still need to be checked (even though the UC Service Profile actually does not have any IM&P servers listed on it):

...even though PhoneOnlyServiceProfile has:

## Verify

The difference between a 12.0(1) Cisco Jabber client, and an old 11.7(1) client (both in Phone Mode) can be seen here:

If presence is still required then:

- Enable availability sharing can still be checked (under the Presence → Settings → Standard Configuration )

- the Cisco XCP Router service restarted (on every node)

- the Jabber client reset (sign out, then choose settings → File Reset Cisco Jabber )

This is what the comparison looks like:

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

2.0

05-Jan-2022

Updated the Configure Section.

1.0

13-Jun-2018

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 05-Jan-2022 | Updated the Configure Section. |
| 1.0 | 13-Jun-2018 | Initial Release |