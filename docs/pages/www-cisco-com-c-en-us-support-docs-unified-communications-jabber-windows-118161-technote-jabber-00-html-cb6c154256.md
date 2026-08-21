---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-windows-118161-technote-jabber-00-html-cb6c154256
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber-windows/118161-technote-jabber-00.html
retrieved_at: 2026-08-21T06:59:45.974151+00:00
---

Jabber for Windows Persistent Registry Keys Prevent Install

# Jabber for Windows Persistent Registry Keys Prevent Install

### Download Options

Updated: August 23, 2021

Document ID: 118161

Contents

## Contents

## Introduction

This document describes how to resolve a problem that is caused by persistent registry keys when you install or upgrade Cisco Jabber for Windows.

## Prerequisites

### Requirements

Cisco recommends you have knowledge of these topics:

- Cisco Jabber for Windows

- Microsoft Windows Version 7 Operating System (32 and 64 bit)

- Microsoft Windows Version 10 Operating System (32 and 64 bit)

### Components Used

This document is not restricted to specific hardware or software versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Problem

When you attempt to install or upgrade Cisco Jabber for Windows Version 9.x or later, the attempt fails and you receive this error message:

```
Error 1714. The older version of Cisco Jabber cannot be removed. Contact your technical Support team
```

### Cause

The programs that are installed via the Microsoft Installer (MSI) file contain an entry in the uninstall key with a Windows Installer value of one ( 1 ). When the Add/Remove Programs function encounters this entry, it reviews the key name and alters it. It then searches for a key that is named with the reordered GUID in this location:

HKLM > Software > Classes > Installer > Products

Since the registry key is corrupt, it must be deleted.

## Solution

Click OK in order to collect the Windows Installer logs; then find the registry that points to ARPPRoduction and see which registry is affected.

Here is an example of the Jabber install logs:

```
MSI (s) (00:68) [13:39:25:865]: Doing action: RemoveExistingProducts
Action 13:39:25: RemoveExistingProducts. Removing applications
Action start 13:39:25: RemoveExistingProducts.
RemoveExistingProducts: Application: {B63FA739-46CF-4270-B903-90F5698EDF39}, Command line: UPGRADINGPRODUCTCODE={F5C0DBF4-2D93-4A73-9AF3-E931AFF8BAF9} CLIENTPROCESSID=13016 CLIENTUILEVEL=0 REMOVE=ALL

MSI (s) (00:24) [13:39:25:880]: Unexpected or missing value (name: 'PackageName', value: '') in key ' HKLM\Software\Classes\Installer\Products\937AF36BFC6407249B30095F96E8FD93\SourceList '
CustomAction  returned actual error code 1610 (note this may not be 100% accurate if translation happened inside sandbox)
MSI (s) (00:68) [13:39:25:880]: Note: 1: 1714 2: Cisco Jabber 3: 1610 
MSI (c) (D8:B8) [13:39:28:589]: Doing action: setErrorUnknownError
Action 13:39:28: setErrorUnknownError. 
Action start 13:39:28: setErrorUnknownError.
MSI (c) (D8:B8) [13:39:28:589]: PROPERTY CHANGE: Modifying ERROR_INSTALL property. Its current value is '0'. Its new value: '4'.
Action ended 13:39:28: setErrorUnknownError. Return value 1.
Error 1714. The older version of Cisco Jabber cannot be removed.  Contact your technical support group.  System Error 1610.
MSI (s) (00:68) [13:39:28:605]: Product: Cisco Jabber -- Error 1714. The older version of Cisco Jabber cannot be removed.  Contact your technical support group.  System Error 1610.
```

From the client machine, click Run > Regedit and navigate to these locations:

HKLM > Software > Classes > Installer > Products >937AF36BFC6407249B30095F96E8FD93 > SourceList

Delete the keys, reboot the computer, and restart the install or upgrade process.

Note : Administrative access might be required in order to access the registry keys on the computer.

### Revision History

1.0

23-Aug-2021

Initial Release

### Contributed by Cisco Engineers

Manjunath D S

Cisco TAC Engineer

Miguel Castillo Torres

Cisco TAC Engineer

### This Document Applies to These Products

- Jabber for Windows

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 23-Aug-2021 | Initial Release |