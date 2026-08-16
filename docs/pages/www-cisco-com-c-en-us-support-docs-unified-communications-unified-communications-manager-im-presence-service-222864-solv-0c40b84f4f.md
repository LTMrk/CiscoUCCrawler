---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-im-presence-service-222864-solv-0c40b84f4f
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-im-presence-service/222864-solve-persistent-chat-rooms-not-showing.html
retrieved_at: 2026-08-16T23:38:13.850577+00:00
---

Solve Persistent Chat Rooms Not Showing Up for Jabber Users Assigned to Specific IM&P Node

# Solve Persistent Chat Rooms Not Showing Up for Jabber Users Assigned to Specific IM&P Node

### Download Options

Updated: March 19, 2025

Document ID: 222864

Contents

## Contents

## Introduction

This document describes how to solve the issue when the persistent chat rooms disappear from the Jabber.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Instant Messaging and Presence Service (IM&P)

- Cisco Jabber

- Command Line Interface (CLI)

- SQL language

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

Scenario and conditions go as follows:

- All users assigned to IM&P node A (which can be Database Publisher or Subscriber node within High Availability (HA) pair can see all Persistent Chat rooms.

- All users assigned to IM&P node B (which can be Database Publisher or Subscriber node within HA pair) cannnot see most or some of the Persistent Chat rooms.

- If you unassign any user from IM&P node B and assign it to node A instead, once they sign out and sign back in to Jabber, they are able to see all Persistent Chat rooms.

- If you issue show perf query class "Cisco XCP TC Room Counters" CLI command on IM&P node A, you are able to see all Persistent Chat rooms being listed.

- If you issue show perf query class "Cisco XCP TC Room Counters" CLI command on IM&P node B, you are not able to see all Persistent Chat rooms being listed.

## Troubleshoot

Reproduce the issue and collect Debug Level traces for these services:

- Cisco XCP Text Conference Manager

- Cisco XCP Router

- Cisco XCP Connection Manager

From the logs, when user is assigned to node B, you are able to see how the Cisco XCP Text Conference Manager service replies with 404 Not Found error back to user:

```
Line 3807: 16:12:44.634 |046f1b70| debug| DiscoGear.cpp:240 Handling disco#info query: <iq from='pchatroom251381924019240@conference-3-standalonecluster64ba2.cisco.com' id='5375193f:9f7a:4146:b7a6:c0100a9fc105' to='jabberuser@cisco.com/jabber_7321' type='error' xml:lang='en'><query node='conference-3-standalonecluster64ba2.cisco.com' xmlns=' http://jabber.org/protocol/disco#info'><feature var='jabber:iq:search'/><feature var=' http://www.jabber.com/protocol/muc#history'/><feature var=' http://www.jabber.com/schemas/muc#persistent'/></query><error code='404' type='cancel'><item-not-found xmlns='urn:ietf:params:xml:ns:xmpp-stanzas'/></error></iq>
```

Also, look for any errors or mismatches in the " tcaliases " table between these nodes. You can list the content of "tcaliases" table by issuing run sql select * from tcaliases CLI command on each IM&P node.

The output looks something like this, and most be the same on both nodes:

```
admin:run sql select * from tcaliases
pkid                                 tcalias                                             isprimary fkprocessnode                        peerclusterid originalfkprocessnode
==================================== =================================================== ========= ==================================== ============= ====================================
043d4cad-2a9d-4295-b371-46641ae034f4 conference-2-StandAloneCluster64ba2.cisco.com t         b7b69c1f-baf5-3ff4-7d26-8f56fd0d4d11 NULL          b7b69c1f-baf5-3ff4-7d26-8f56fd0d4d11
88ac04fc-c619-4541-a526-e6ee6934e4bf conference-3-StandAloneCluster64ba2.cisco.com t         ce4a26a8-8551-8baa-c34d-fb4fbf81ff08 NULL          ce4a26a8-8551-8baa-c34d-fb4fbf81ff08
3c2d12d6-7e98-6d2b-3dc4-70016a4597b9 alias.cisco.com                               f         b7b69c1f-baf5-3ff4-7d26-8f56fd0d4d11 NULL          b7b69c1f-baf5-3ff4-7d26-8f56fd0d4d11
```

## Solution 1

Once you have identified this error signature and behavior, you can try to re-sync the rooms by restarting Cisco XCP Text Conference manager service on both IM&P nodes

Run the CLI command on both nodes: utils service restart Cisco XCP Text Conference Manager

While restarting Cisco XCP Text Conference Manager:

```
admin:utils service restart Cisco XCP Text Conference Manager
Do not press Ctrl+C while the service is restarting. If the service has not restarted properly, execute the same command again.
Service Manager is running
Cisco XCP Text Conference Manager[STARTING]
Cisco XCP Text Conference Manager[STARTING]
Cisco XCP Text Conference Manager[STARTED]
```

Note : The restart of the Cisco XCP Text Conference Manager service, temporarily brings down the ad-hoc group chats and Persistent Chat Rooms for Jabber users.

After that, have the Jabber users assigned to node B to sign out and sign back in. This must allow them to rediscover all of the missing rooms.

## Solution 2

In case the issue persists after the application of the Workaround 1, the issue occurs due to the tc-1.xml file (Text Conference configuration file) in the node B, which is not aligned to the one in node A.

These are the steps to solve the issue:

Step 1. Enable "High Availability" in CM Administration > System > Presence Redundancy Groups .

Step 2. Initiate a manual failover of node B to node A. At this point, tcaliases table and tc-1.xml file must be updated with the current High Availability state.

Step 3. Initiate a fallback so that the Presence Redundancy Group goes back to Normal/Normal state. The tcaliases table and tc-1.xml file now are updated.

Note : The actions applied on the Workaround 2 temporarily cause disconnection from IM and Presence services for Jabber users while they get moved from one node to another.

After that, have the Jabber users assigned to node B to sign out and sign back in. This process now allow them to rediscover all of the missing rooms.

## Verify

There is currently no verification procedure available for this configuration.

### Revision History

1.0

19-Mar-2025

Initial Release

### Contributed by Cisco Engineers

Edgar Rodriguez Aguilar

Cisco TAC

### This Document Applies to These Products

- Unified Communications Manager IM & Presence Service

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 19-Mar-2025 | Initial Release |