---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-configadminguide-12-5-1-cup0-b-config-and-admin-guide-1251--93dbcaa8a2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/configAdminGuide/12_5_1/cup0_b_config-and-admin-guide-1251/cup0_b_config-and-admin-guide-1251_chapter_010010.html
retrieved_at: 2026-08-16T16:43:18.410654+00:00
---

Configuration and Administration of the IM and Presence Service, Release 12.5(1)

# Configuration and Administration of the IM and Presence Service, Release 12.5(1)

Updated: November 27, 2024

Chapter: Configure Multiple Device Messaging

## Chapter: Configure Multiple Device Messaging

# Configure Multiple Device Messaging

## Multiple Device Messaging Overview

With Multiple Device Messaging (MDM), you can have one-to-one instant message (IM) conversations tracked across all devices
                           on which you are currently signed in. If you are using a desktop client and a mobile device, both of which are MDM-enabled,
                           messages are sent, or carbon copied, to both devices. Read notifications are also synchronized on both devices as you participate
                           in a conversation.

MDM lets you maintain an IM conversation while moving between any of your devices. For example, if you start an IM conversation
                           on your desktop computer, but you have to leave your desk for a meeting, you can you can continue the IM  conversation on
                           your mobile device.  Clients must be signed-in to be MDM-enabled. Signed-out clients do not display sent or received IMs or
                           notifications.

MDM supports quiet mode, which helps to conserve battery power on your mobile devices. The Jabber client turns quiet mode
                           on automatically when the mobile client is not being used. Quiet mode is turned off when the client becomes active again.

## Multiple Device Messaging Prerequisites

Instant messaging must be enabled. For details, see

## Configure Multiple Device Messaging

Multiple Device Messaging is enabled by default. You can use this procedure to disable the feature, or to turn it back on
                              after it has been disabled.

Step 1

In Cisco Unified CM IM and Presence Administration , choose System > Service Parameters .

Step 2

From the Server drop-down list, choose the IM and Presence Service Publisher node.

Step 3

From the Service drop-down list, choose Cisco XCP Router (Active) .

Step 4

From the Enable Multi-Device Messaging drop-down list,  select either Enabled (the default value) or Disabled .

Step 5

Click Save .

Step 6

Restart the Cisco XCP Router service:

Log in to Cisco Unified IM and Presence Serviceability and choose Tools > Control Center - Network Services .

From the Server drop-down list box, select the IM and Presence publisher node.

Under IM and Presence Services , select Cisco XCP Router and click Restart .

## Multiple Device Messaging Flow Use Case

This flow describes how messages and notifications are handled when a user, Alice, has MDM enabled on her laptop and mobile
                              device.

Alice has a Jabber client open on her laptop, and is also using Jabber on her mobile device.

Alice receives an instant message (IM) from Bob.

Her laptop receives a notification and displays a new message indicator. Her mobile device receives a new message with no
                                    notification.

IMs are always sent to all MDM-enabled clients. Notifications are displayed either on the active Jabber client only or, if
                                                no Jabber client is active, notifications are sent to all Jabber clients.

Alice chats with Bob for 20 minutes.

Alice uses her laptop as normal to do this, while on her mobile device new messages are received and are marked as read. No
                                    notifications are sent to her mobile device.

When Alice receives three chat messages from a third user, Colin, Alice's devices behave as they did in step 2.

Alice does not respond, and closes the lid on her laptop. While on the bus home Alice receives another message from Bob.

In this case, both her laptop and mobile device receive a new message with notifications.

Alice opens her mobile device, where she finds the new messages sent from Bob and Colin. These messages have also been sent
                                    to her laptop.

Alice reads through her messages on her mobile device, and as she does so, messages are marked as read on both her laptop
                                    and on her mobile device.

## Multiple Device Messaging Quiet Mode Use Case

This flow describes the steps Multiple Device Messaging uses to enable quiet mode on a mobile device.

Alice is using Jabber on her laptop and also on her mobile device. She reads a message from Bob and sends a response message
                                    using Jabber on her laptop.

Alice starts using another application on her mobile device. Jabber on her mobile device continues working in the background.

Because Jabber on her mobile device is now running in the background, quiet mode is automatically enabled.

Bob sends another message to Alice. Because Alice's Jabber on her mobile device in quiet mode, messages are not delivered.
                                    Bob’s response message to Alice is buffered.

Message buffering continues until one of these triggering events occur:

An <iq> stanza is received.

A <message> stanza is received when Alice has no other active clients currently operating on any other device.

An active client is the last client that sent either an Available presence status or an instant message in the previous five
                                                      minutes.

The buffering limit is reached.

When Alice returns to Jabber on her mobile device, it becomes active again. Bob's message, which had been buffered is delivered,
                                    and Alice is able to view it.

## Multiple Device Messaging Interactions and Restrictions

The following table summarizes feature interactions and restrictions with the Multiple Device Messaging (MDM) feature.

Feature

Interaction or Restriction

Cisco Jabber Clients

MDM is supported by all Jabber clients from version 11.7 and higher.

Group Chat

Group chat is available for all MDM users, who have signed in from any device.

Message Archiver

MDM is compatible with the Message Archiver feature.

Managed File Transfer

File transfer is available for all MDM users, who have signed in from any device.

Mobile and Remote Access via Expressway

For Mobile and Remote Access clients that connect to IM and Presence Service via Cisco Expressway, you must be running at
                                          least Expressway X8.8 minimum to use MDM.

Server Recovery Manager

The Multiple Device Messaging feature causes a delay with server recovery on the IM and Presence Service if failover occurs.
                                          If server failover occurs on a system where Multiple Device Messaging is configured, the failover times generally are twice
                                          as long as the times specified with the Cisco Server Recovery Manager service parameters.

Third-Party Clients

MDM is compatible with third-party clients that do not support the feature.

## Counters for Multiple Device Messaging

Multiple Device Messaging (MDM) uses the following counters from the Cisco XCP MDM Counters Group:

Counter Name

Description

MDMSessions

The current number of MDM enabled sessions.

MDMSilentModeSessions

The current number of sessions in silent mode.

MDMQuietModeSessions

The current number of sessions in quiet mode.

MDMBufferFlushes

The total number of MDM buffer flushes.

MDMBufferFlushesLimitReached

The total number of MDM buffer flushes due to reaching the overall buffer size limit.

MDMBufferFlushPacketCount

The number of packets flushed in the last timeslice.

MDMBufferAvgQueuedTime

The average time in seconds before the MDM buffer is flushed.

| Note | If you plan to enable Multiple Device Messaging, measure deployments by the number of clients instead of the number of users
                                       as each user may have multiple Jabber clients. For example, if you have 25,000 users, and each user has two Jabber clients,
                                       your deployment requires the capacity of 50,000 users. |
|---|---|

| Step 1 | In Cisco Unified CM IM and Presence Administration , choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose the IM and Presence Service Publisher node. |
| Step 3 | From the Service drop-down list, choose Cisco XCP Router (Active) . |
| Step 4 | From the Enable Multi-Device Messaging drop-down list,  select either Enabled (the default value) or Disabled . |
| Step 5 | Click Save . |
| Step 6 | Restart the Cisco XCP Router service: Log in to Cisco Unified IM and Presence Serviceability and choose Tools > Control Center - Network Services . From the Server drop-down list box, select the IM and Presence publisher node. Under IM and Presence Services , select Cisco XCP Router and click Restart . |

| Note | IMs are always sent to all MDM-enabled clients. Notifications are displayed either on the active Jabber client only or, if
                                                no Jabber client is active, notifications are sent to all Jabber clients. |
|---|---|

| Note | An active client is the last client that sent either an Available presence status or an instant message in the previous five
                                                      minutes. |
|---|---|

| Feature | Interaction or Restriction |
|---|---|
| Cisco Jabber Clients | MDM is supported by all Jabber clients from version 11.7 and higher. |
| Group Chat | Group chat is available for all MDM users, who have signed in from any device. |
| Message Archiver | MDM is compatible with the Message Archiver feature. |
| Managed File Transfer | File transfer is available for all MDM users, who have signed in from any device. |
| Mobile and Remote Access via Expressway | For Mobile and Remote Access clients that connect to IM and Presence Service via Cisco Expressway, you must be running at
                                          least Expressway X8.8 minimum to use MDM. |
| Server Recovery Manager | The Multiple Device Messaging feature causes a delay with server recovery on the IM and Presence Service if failover occurs.
                                          If server failover occurs on a system where Multiple Device Messaging is configured, the failover times generally are twice
                                          as long as the times specified with the Cisco Server Recovery Manager service parameters. |
| Third-Party Clients | MDM is compatible with third-party clients that do not support the feature. |

| Counter Name | Description |
|---|---|
| MDMSessions | The current number of MDM enabled sessions. |
| MDMSilentModeSessions | The current number of sessions in silent mode. |
| MDMQuietModeSessions | The current number of sessions in quiet mode. |
| MDMBufferFlushes | The total number of MDM buffer flushes. |
| MDMBufferFlushesLimitReached | The total number of MDM buffer flushes due to reaching the overall buffer size limit. |
| MDMBufferFlushPacketCount | The number of packets flushed in the last timeslice. |
| MDMBufferAvgQueuedTime | The average time in seconds before the MDM buffer is flushed. |