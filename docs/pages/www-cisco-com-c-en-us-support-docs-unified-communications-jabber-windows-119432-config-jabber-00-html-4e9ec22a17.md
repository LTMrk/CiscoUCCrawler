---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-windows-119432-config-jabber-00-html-4e9ec22a17
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber-windows/119432-config-jabber-00.html
retrieved_at: 2026-09-01T21:16:06.358716+00:00
---

Configure Jabber for Windows 10.5 Call Pickup and Hunt Group Call Answer

# Configure Jabber for Windows 10.5 Call Pickup and Hunt Group Call Answer

### Download Options

Updated: January 14, 2016

Document ID: 119432

Contents

## Contents

## Introduction

This document provides a basic configuration example for Jabber for Windows 10.5 call pickup and Hunt Group call answer.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

The information in this document is based on these software and hardware versions:

- Jabber for Windows 10.5

- Cisco Presence 8.6.4.12900-2

- Cisco Call Manager Version 8.6.4.23900-10

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

### Create a Call Pickup Group

- Go to the Call Manager admin page and choose Call Routing > Call Pickup Group .

In this case Jabber CSF has an extension of 1004 and the need is to add the pickup group in its DN page. See this screenshot for details.

- Once done, make sure that this pickup group is also added to other DNs. In this test case it will be DN 1002, so add the same call pickup group to this DN "1002".

```
<Policies> <EnableCallPickup>true</EnableCallPickup> <EnableGroupCallPickup>true</EnableGroupCallPickup> <EnableOtherGroupPickup>true</EnableOtherGroupPickup> <EnableHuntGroup>true</EnableHuntGroup> </Policies>
```

Note : "EnableHuntGroup" is added in order to get the "Log into Hunt Groups" option. It is not mandatory in the case that Jabber for Windows will only be used for call pickup and not to answer calls as a member of a Hunt Group.

Once Jabber accepts these settings, this is what you will see activated in Jabber for Windows.

### Configure Hunt Group Call Answer via Jabber for Windows

Click the "Log into Hunt Groups" radio button in order to ensure Jabber for Windows is enabled to answer calls as a member of the Hunt Group. As soon as this is configured, the Hunt Group & Pickup icon in Jabber displays a green button that confirms Jabber is enabled for Hunt Group and call pickup answer mode.

In this test example, this is what is set up:

- Line Group ( members are 1004 and 1002) (test1- Line Group Name)

- Hunt List  ( Name : test123) includes this Line Group (test1)

- Hunt group Pilot ( 7000)

In summary, a call was placed to the Hunt pilot (7000) and it was verified that the "Log into Hunt groups" option was enabled, otherwise the call would not make it to the Jabber for Windows .csf extension.

## Verify

Use this section in order to confirm that your configuration works properly.

### Verify Call Pickup Operation

Since 1002 (a desk phone at extension 7975 in the lab) and 1004 (test Jabber for Windows CSF extension) are made to point to the same call pickup group, if 1002 is called then Jabber is prompted for a call pickup as both extensions point to the same call pickup group. Here is how Jabber receives the notification:

Calling Party number : 1000

Called Party number : 1002

Call pickup group number and name: 4000 (test); both 1000 and 1002 are part of this call pickup group, hence Jabber receives the call pickup group call as seen in this screen capture.

### Verify Hunt Group Call Answer Operation

Here is a notification received when Jabber for Windows receives the call as per the "distribution algorithm" in Line group. Details of the call that was placed to lead to the mentioned notification are shown here:

Calling Party : 1000

Called Party : 7000 ( hunt pilot pattern)

Jabber CSF ( ext :1004) is member of the line group point via Hunt list to this Hunt Group

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

1.0

14-Jan-2016

Initial Release

Contributed by Cisco Engineers

### Contributed by Cisco Engineers

### This Document Applies to These Products

- Jabber for Windows

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 14-Jan-2016 | Initial Release |