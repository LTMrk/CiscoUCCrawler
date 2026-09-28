---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-mac-116682-technote-jabber-00-html-58b68684e9
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber-mac/116682-technote-jabber-00.html
retrieved_at: 2026-09-28T06:14:42.982116+00:00
---

Jabber for Mac 9.2 Locate the Log File and Cache Location

# Jabber for Mac 9.2 Locate the Log File and Cache Location

### Download Options

Updated: November 1, 2013

Document ID: 116682

Contents

## Contents

## Introduction

In some cases users need to access the log file, plist file, jabber-config.xml file, or cache file location in order to troubleshoot issues. The locations of these files are provided in this document.

## Problem

The user needs to locate  the log file, plist file, jabber-config.xml or cache location.

## Solution

```
/Users/<userid>/Library/Logs/Jabber/Jabber- <date_with_numeric_number>-Console.log/Users/<userid> /Library/Logs/Jabber/Jabber-<date_with_numeric_number>.log
```

```
/User/<userid>/Library/Preferences/.com.cisco.jabber.plist/User/ <userid>/Library/Preferences/.com.cisco.jabber.plist.lockfile
```

```
/Users/<userid>/Library/Caches/com.cisco.Jabber/<user_email>/
```

The Jabber-config.xml file location and filename are shown here:

Jabber-config.xml file:

```
/Users/<userid>/Library/Application Support/Cisco/ Unified Communications/Jabber
```

### Revision History

1.0

01-Nov-2013

Initial Release

### Contributed by Cisco Engineers

Md Hasan

Cisco TAC Engineer.

### This Document Applies to These Products

- Jabber for Mac

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 01-Nov-2013 | Initial Release |

## Figuras

![TAC Authored](https://www.cisco.com/etc/designs/cdc/fw/i/TAC_lg-icon.png)

![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)