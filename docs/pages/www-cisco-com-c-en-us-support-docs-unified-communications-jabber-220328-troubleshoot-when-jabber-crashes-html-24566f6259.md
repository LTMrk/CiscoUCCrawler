---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-220328-troubleshoot-when-jabber-crashes-html-24566f6259
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber/220328-troubleshoot-when-jabber-crashes.html
retrieved_at: 2026-08-20T22:13:49.450486+00:00
---

Troubleshoot when Jabber Crashes

# Troubleshoot when Jabber Crashes

### Download Options

Updated: April 3, 2023

Document ID: 220328

Contents

## Contents

## Introduction

This document describes how to troubleshoot a Jabber application crash.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics.

- Cisco Jabber

### Components Used

The information in this document is based on these software and hardware versions.

- Jabber version 12.9.X.

- Jabber version 14.X.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

The Jabber application presents an unrecoverable failure that causes a crash. It can be detected, because when Jabber crashes, the application closes abruptly and its services cannot be used any longer. Then, a new Jabber window is prompted to allow user to obtain a Jabber Problem Report (Jabber PRT) necessary for troubleshoot purposes.

The Jabber application has the possibility to create a Jabber PRT whenever the user needs it. In the case of a crash scenario, the Jabber PRT window shows off so the user can report this misbehavior. It is necessary to fill the blank spaces and to gather as much information as possible, like the kind of issue, and general details of the scenario before the crash is produced. Moreover, there is a checkbox automatically checked at the end of the options. That checkbox allows the user to get the Jabber PRT with the dump file needed by TAC in order to perform the root cause analysis.

## Problem

If the Jabber client crashes, Jabber is now unable to provide services such as Instant Messaging or Presence. It is also unable to provide any kind of serviceability as the application closes. That can be caused due to several conditions related to the environment where Jabber works, for example,

- Compatibility with Windows security updates.

- Headsets.

- Cameras or any hardware not listed in the list of compatible devices for Cisco Jabber.

- Unsupported environment conditions like unsupported Bluetooth devices.

- Unsupported Audio and Video codecs.

- Any condition that is not met from the official documentation like Planning Guide for Cisco Jabber 14.0.

## Solution

If the Cisco Jabber crashes, the solution is to take the Jabber PRT from the window that is prompted immediately after the application closes. Make sure to leave the checkbox to collect the dump file marked, when that remains checked the Jabber PRT includes the dump file needed by TAC to debug the file and to get an Exception Analysis that guides TAC to isolate the issue and identify further steps. Also, it is crucial to make sure to have Jabber updated to the latest version available, since latest releases include the fixes of previously identified issues from previous versions. That In order to make sure that Jabber performs without known issues.

In some cases, that stack trace found in the dump file analysis form the Jabber PRT previously obtained, shows that the component that causes the crash is in the Windows side. When it is on the Windows side, it is a win32u.dll component. That can be due to a corrupted .dll or another program that uses the same .dll component at the same time that Jabber does. In some cases, TAC recommends to reinstall Jabber in "Safe Mode with Networking" in order to get rid of Windows .dll corrupted components, in some other cases there are automatic software upgrade processes enabled in the Windows side, like the System Center Configuration Manager (SCCM). In those cases, it is needed to temporarily disable SCCM in order to test if Jabber client is pushed by third party software to be upgraded. In cases were the issue is related to bluetooth cameras or headsets with compatibility issues it is necessary to change the unsupported device to a listed device in the Supported Bluetooh Devices list section in the Planning Guide for Cisco Jabber 14.0 or the version required and to verify the Bluetooth Limitations section as well.

## Verify

That can be verified in the Jabber log file.

```
Log File snippet. INFO  [0x00001270] [ts\csf-logger\src\LogController.cpp(141)] [LogController] [CSF::csflogger::LogController::Impl::init] - ***** Jabber launched, start logging ***** INFO  [0x00001270] [tils\src\exceptionhandlinghelper.cpp(22)] [exception-handling-helper] [jabberutils::ExceptionHandlingHelper::setCOMExceptionHandlingPolicy] - set COM exception handling policy to: EnableExceptions DEBUG [0x00001270] [tils\src\exceptionhandlinghelper.cpp(47)] [exception-handling-helper] [jabberutils::ExceptionHandlingHelper::setCOMExceptionHandlingPolicy] - Successfully set COM exception handling policy to: COMGLB_EXCEPTION_DONOT_HANDLE.
```

## Troubleshoot

Open a case with Cisco TAC and share the Jabber PRT with the dump file that is generated after the crash activity happens.

## Related Information

- Cisco Technical Support & Downloads

### Revision History

2.0

03-Apr-2023

Initial Release

1.0

31-Mar-2023

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 03-Apr-2023 | Initial Release |
| 1.0 | 31-Mar-2023 | Initial Release |