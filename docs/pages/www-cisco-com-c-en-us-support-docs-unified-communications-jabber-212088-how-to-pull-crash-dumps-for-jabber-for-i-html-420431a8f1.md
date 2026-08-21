---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-212088-how-to-pull-crash-dumps-for-jabber-for-i-html-420431a8f1
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber/212088-How-to-Pull-Crash-Dumps-for-Jabber-for-i.html
retrieved_at: 2026-08-21T07:06:18.773408+00:00
---

How to Pull Crash Dumps for Jabber for iOS

# How to Pull Crash Dumps for Jabber for iOS

### Download Options

Updated: September 14, 2017

Document ID: 212088

Contents

## Contents

## Introduction

This document provides instructions on how to pull crash dumps for Jabber for iOS devices with the XCode or the iPhone Configuration Utility

Contributed by Fareed Warrad, Cisco TAC Engineer. Edited by Harry Doyle and Jasmeet Sandhu.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Jabber clients

### Components Used

The information in this document is based on these software and hardware versions:

- Xcode 9

- iPhone Configuration 3.6.1

- iPhone 6

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

When Jabber crashes on any client it generates a memory dump up to the time before the application crashed. The memory dump is not included in the problem report from the client and must be retrieved via an appliation on a computer.

## How to Collect Memory Dump(s) and Console Log with Xcode

To collect the files with Xcode navigate to this area(s):

- Console log:

Open xCode navigate to Organizer , select device , and select console .

- Crash reports:

Open xCode navigate to Organizer , select your device , and select Device Logs .

- Viewed in Console for MAC:

In Console , navigate to ~/Library/Logs , select the drop down arrow to view CrashReporter, expand this section to view MobileDevice . Find your device and expand to retrieve the logs.

## How to Collect Memory Dump(s) and Console Log with iPhone Configuration Utility

To collect the memory dump and console logs please navigate to the below area(s):

- Console log:

Open iPhone Configuration Utility , navigate to your device , and select the Console tab .

- Crash reports:

Open File Explorer and navigate to the below area:

C:\Users\{YOUR_SPECIFIC_USER}\AppData\Roaming\Apple computer\Logs\CrashReporter\MobileDevice\<your iPhone’s name>Labels parameters

### Contributed by Cisco Engineers

Contributed by Fareed Warrad

Cisco TAC

Edited by Harry Doyle

Cisco TAC

Edited by Jasmeet Sandhu

Cisco TAC

### This Document Applies to These Products

- Jabber