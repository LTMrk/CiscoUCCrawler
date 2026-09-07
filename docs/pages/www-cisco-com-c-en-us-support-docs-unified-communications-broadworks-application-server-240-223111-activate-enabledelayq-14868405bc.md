---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-broadworks-application-server-240-223111-activate-enabledelayq-14868405bc
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/broadworks-application-server-240/223111-activate-enabledelayquickreinvite-on.html
retrieved_at: 2026-09-07T13:02:32.919068+00:00
---

Activate enableDelayQuickReinvite on the Broadworks AS

# Activate enableDelayQuickReinvite on the Broadworks AS

### Download Options

Updated: June 20, 2025

Document ID: 223111

Contents

## Contents

## Introduction

This document describes how to configure enableDelayQuickReinvite to prevent the Application Server (AS) to send re-INVITE too quickly after an ACK.

## Prerequisites

- Basic Session Initiation Protocol (SIP) knowledge

- Basic AS knowledge

- Basic BroadWorks bwcli knowledge

### Requirements

- Be able to use the AS bwcli and an admin user

- Be able to review the AS XSLogs

### Components Used

- Cisco BW AS

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

In some call scenarios, the AS needs to start a reconnection, and in order to do this, it sends a re-INVITE to both ends. It happens when the AS needs to trigger a reconnection after a session has been established, for example for calls to Call Centers, Hunt Groups, or those that involve the Click to Dial or Call Recording feature.

When the AS needs to send re-INVITE  after the ACK was sent in the same dialog, the AS normally sends the re-INVITE at the same moment as the ACK, and this can cause the ACK and re-INVITE to be received out of order by the remote device.

When this happens, the device that receives the re-INVITE before the pending ACK can reject the re-INVITE, normally with a 500 error code (but this can vary, based on the remote device implementation).

## Configure

There are two parameters used to configure this feature, and they are both located in the bwcli at AS_CLI/Interface/SIP> .

- enableDelayQuickReInvite is the main switch to turn on or off the feature. The accepted values are true and false.

- delayQuickReInviteMilliseconds is the value in milliseconds (ms) of the delay added after the ACK. The value range is 100ms to 10000ms.

In order to configure this feature, open the AS bwcli, log in as an Admin user, then navigate to AS_CLI/Interface/SIP> :

```
AS_CLI> cd /Interface/SIP AS_CLI/Interface/SIP>
```

First run a get command to check the current values of both parameters. By default enableDelayQuickReInvite is disabled (false) and the default value of delayQuickReInviteMilliseconds is 1000 (1000ms, or 1 second).

Part of the get command output is omitted for enhanced readability.

```
AS_CLI/Interface/SIP> get ... enableDelayQuickReInvite = false delayQuickReInviteMilliseconds = 1000 ...
```

Then configure the delayQuickReInviteMilliseconds parameter. You can accept the default value, or use the one most suitable to your environment. The recommendation is to use the lowest possible value, so it is advisable to start with the value of 100ms, and increase it just in case it is not enough to allow the problem to be solved.

```
AS_CLI/Interface/SIP> set delayQuickReInviteMilliseconds 100 ...Done
```

Once the value for delayQuickReInviteMilliseconds has been configured, you can enable enableDelayQuickReInvite .

```
AS_CLI/Interface/SIP> set enableDelayQuickReInvite true ...Done
```

## Verify

Once the configuration is finished, run the call scenario again, to ascertain that the AS adds the delay between the ACK and the re-INVITE. For example, if the AS has been configured to add 100ms, you can expect the delay to be at least 100ms, but it could be a few ms higher.

100ms are normally enough to prevent the ACK and re-INVITE to be received out of order, but the value could be higher, based on the network environment and the involved SIP entities in the signalling path.

## Troubleshoot

If the device still responds with a 500 error code, and the ACK and re-INVITE have been delivered in the correct order, further investigation is needed on the device.

Use the XSLogs on the AS to verify that the AS added the delay as configured, and use a packet capture or the device logs to make sure that the delay was enough for the messages to be delivered in the correct order.

Note that this only works when the AS sends a re-INVITE just after it sent an ACK, but it does not work in case the AS receives an ACK and that causes the AS to send a re-INVITE.

### Revision History

1.0

20-Jun-2025

Initial Release

### Contributed by Cisco Engineers

Diego Cimarosti

Technical Consulting Engineer

### This Document Applies to These Products

- BroadWorks

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 20-Jun-2025 | Initial Release |