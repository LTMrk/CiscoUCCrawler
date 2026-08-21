---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-212059-how-to-gather-microsoft-outlook-logs-for-html-d67d13f6b9
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber/212059-How-to-Gather-Microsoft-Outlook-Logs-for.html
retrieved_at: 2026-08-21T07:06:27.152859+00:00
---

How to Gather Microsoft Outlook Logs for Jabber Presence issues

# How to Gather Microsoft Outlook Logs for Jabber Presence issues

### Download Options

Updated: September 13, 2017

Document ID: 212059

Contents

## Contents

## Introduction

This document describes the procedure used to gather logs from Microsoft Outlook for Jabber Presence issues.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Jabber for Windows

- Microsoft Outlook

- Post Office Protocol 3 (POP3)

- Simple Mail Transfer Protocol (SMTP)

- Messaging Application Programming Interface (MAPI)

- Internet Message Access Protocol (IMAP)

### Components Used

The information in this document is based on these software and hardware versions:

- Microsoft Outlook 2007

- Microsoft Outlook 2010

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## How to enable MS Outlook log file generation

Microsoft Outlook 2010

Step 1. Go to File > Options

Step 2. Select Advanced in the left frame

Step 3. In the right frame, select the Enable troubleshooting logging option in the Other section

Step 4. Select OK

Step 5. Close and restart Microsoft Outlook

Microsoft Outlook 2007 and older

Step 1. Expand Tools select Options

Step 2. Open the Other tab

Step 3. Select Advanced Options

Step 4. Activate the Enable logging (troubleshooting) option

Step 5. Select OK twice

Step 6. Close and restart Microsoft Outlook

Once you have this option enabled, the application log begins registering all data regarding the interaction between Microsoft Outlook and a mail server each time a message is sent or received.

Warning : Once the issue is reproduced and logs gathered, disable the Log Collection. The Outlook log file will continue to grow which can potentially consume all hard drive resources.

Log file location

- For POP3, SMTP, MAPI protocols

```
%temp%\Outlook Logging\Opmlog.log
```

- For IMAP protocol

```
%temp%\Outlook Logging\IMAP-usernamedomainname-date-time.log
```

Note : If the log file cannot be seen or does not contain current data, exit Microsoft Outlook as the data can be registered in the log when it is not currently active.

## Related Information

- Microsoft Guide to Enable Advanced Logging

- Technical Support & Documentation - Cisco Systems

### Contributed by Cisco Engineers

Md Hasan

Cisco TAC Engineer

Edited by Billy Turnbow

Cisco TAC Engineer

### This Document Applies to These Products

- Jabber