---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-broadworks-application-server-220-221699-troubleshoot-webex-fo-9ba66c1573
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/broadworks-application-server-220/221699-troubleshoot-webex-for-bworks-failed-to.html
retrieved_at: 2026-09-07T13:03:14.971978+00:00
---

Troubleshoot Webex for Bworks "Failed to Parse the Configuration" Error

# Troubleshoot Webex for Bworks "Failed to Parse the Configuration" Error

### Download Options

Updated: February 15, 2024

Document ID: 221699

Contents

## Contents

## Introduction

This document describes the steps to use when "failed to parse the configuration" error is seen in Webex for Broadworks client logs.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

When analyzing Webex for Broadworks client logs for errors such as “Phone Services not connected”, one potential cause for these connection failures could be the presence of characters which cannot be parsed within the configuration file.

### Associated Logs

This is an example log snippet showing log sequences containing “failed to parse the configuration” error. This is for reference.

```
2024-01-30T07:01:25.213Z <Info> [0x390] parser.rl:232 TP::Xml::Parser::parse:BWC:INTERNAL: Incomplete
2024-01-30T07:01:25.213Z <Info> [0x390] BroadWorksCallControl.cpp:493 BroadWorksCallControl::createConfig:BWC:SCF: failed to parse the configuration ... ...
2024-01-30T07:19:10.077Z <Error> [0x45c] BroadWorksManager.cpp:781 BroadWorksManager::registerClient::<lambda_367b7b02ffeb826e6e6a25aafb052a78>::()::<lambda_f7b7c2330cd9b6c4719bd5256940e122>::operator ():BWC:SCF: BroadWorks Calling - failed to register client. errorCode=1507 2024-01-30T07:19:10.078Z <Error> [0x45c] BroadWorksLoginAdapter.cpp:452 BroadWorksLoginAdapter::handleLoginError:BWC:SCF: Login error occurred: errorCode=1507
```

## How to Check

To verify the current default device encoding, use this command:

```
AS_CLI/System/DeviceType/SIP> detail "Business Communicator - PC"
```

This displays various details about the device. Look for the defaultDeviceEncoding field. For example:

```
AS_CLI/System/DeviceType/SIP> detail "Business Communicator - PC" ... ... deviceAccessContextName = dms deviceAccessURI = bc/pc/ defaultDeviceLanguage = defaultDeviceEncoding = ISO-8859-1 <--------- Here ... ...
```

Note : If the defaultDeviceEncoding is set to ISO-8859-1, you can experience issues with accented characters. If the defaultDeviceEncoding parameter is not set, it defaults to ISO-8859-1.

## How to Change the Default Encoding

Default device encoding can be changed using this command:

```
AS_CLI/System/DeviceType/SIP> set "Business Communicator - PC" defaultDeviceEncoding UTF-8
```

This sets defaultDeviceEncoding for the Business Communicator - PC device type to UTF-8.

## Verification

After changing the default encoding, you can rebuild the profile and ask the user to log out and in. This forces the client to download the latest config-wxt.xml from Broadworks. Test again to verify issue is resolved.

## Related Information

- Cisco Technical Support & Downloads

### Revision History

1.0

16-Feb-2024

Initial Release

### Contributed by Cisco Engineers

Mark Gardner

Technical Consulting Engineer

### This Document Applies to These Products

- Webex for  Cisco BroadWorks

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 16-Feb-2024 | Initial Release |