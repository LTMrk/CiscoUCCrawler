---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-android-201013-configure-jabber-for-android-to-register-812610ccb8
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber-android/201013-Configure-Jabber-for-Android-to-register.html
retrieved_at: 2026-08-21T12:36:16.178471+00:00
---

Configure Jabber for Android to Register as BOT or TAB Device

# Configure Jabber for Android to Register as BOT or TAB Device

### Download Options

Updated: July 15, 2021

Document ID: 201013

Contents

## Contents

## Introduction

This document describes the different registration user agents available on Jabber for Android client and how to configure them manually.

This document provides additional details to some of the topics covered in the document titled Jabber for Android Configuration Example .

It is recommended that you also read the other document for a more detailed configuration example of Cisco Jabber for Android.

Contributed by Neo Jiang, Cisco TAC Engineer.

## Problem

Steps to reproduce:

- Call Manager configured with Cisco Dual Mode for Android (BOT) and Cisco Jabber for Tablet (TAB) devices.

- Both devices assigned to the same End User.

- User launches Jabber for Android on the tablet and it registers as the BOT device instead of the TAB device.

## Solution

The Advanced Settings option, Register without mobile phone integration , is turned off by default so the Jabber SIP User-Agent is Cisco-SOUNDWAVE:

```
REGISTER sip:cucmpub.ciscodomain.local SIP/2.0 Via: SIP/2.0/TCP 192.168.1.170:35936;branch=z9hG4bK18952482 From: <sip: 1111@cucmpub.ciscodomain.local >;tag=f4f1e1ff3028000741b43293-2f1aaac6 To: <sip: 1111@cucmpub.ciscodomain.local > Call-ID: f4f1e1ff-30280002-7ed309e2-10521e5b@192.168.1.170 Max-Forwards: 70 Date: Mon, 16 Jan 2017 00:43:24 GMT CSeq: 105 REGISTER User-Agent: Cisco-SOUNDWAVE
```

By toggling that option in Advanced Settings , Jabber then registers with User-Agent as Cisco-TAB:

```
REGISTER sip:cucmpub.ciscodomain.local SIP/2.0 Via: SIP/2.0/TCP 192.168.1.170:37988;branch=z9hG4bK0a3241dd From: <sip: 7626@cucmpub.ciscodomain.local >;tag=f4f1e1ff3028000b5ee8db3b-69ffdedd To: <sip: 7626@cucmpub.ciscodomain.local > Call-ID: f4f1e1ff-30280003-29831859-0284bdcf@192.168.1.170 Max-Forwards: 70 Date: Mon, 16 Jan 2017 00:44:32 GMT CSeq: 107 REGISTER User-Agent: Cisco-TAB
```

The Register without mobile phone integration option can be seen on Advanced Settings page here:

### Revision History

1.0

07-Mar-2017

Initial Release

### Contributed by Cisco Engineers

Neo Jiang

Cisco TAC Engineer

### This Document Applies to These Products

- Jabber for Android

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 07-Mar-2017 | Initial Release |