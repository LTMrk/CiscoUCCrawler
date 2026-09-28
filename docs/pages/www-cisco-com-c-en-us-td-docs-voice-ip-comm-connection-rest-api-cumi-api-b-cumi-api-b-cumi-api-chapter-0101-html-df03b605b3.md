---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cumi-api-b-cumi-api-b-cumi-api-chapter-0101-html-df03b605b3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUMI_API/b_CUMI-API/b_CUMI-API_chapter_0101.html
retrieved_at: 2026-08-21T08:06:27.432483+00:00
---

Cisco Unity Connection Messaging Interface (CUMI) API

# Cisco Unity Connection Messaging Interface (CUMI) API

Updated: December 23, 2018

Chapter: Cisco Unity Connection Messaging
	 Interface (CUMI) API -- Using the CUMI API for Sending Notifications

## Chapter: Cisco Unity Connection Messaging
	 Interface (CUMI) API -- Using the CUMI API for Sending Notifications

# Cisco Unity Connection Messaging
                     	 Interface (CUMI) API -- Using the CUMI API for Sending Notifications

## About
                        	 Notifications

CUMI supports Comet notifications
                           		for message operations on the Inbox and Deleted folders.

## Getting
                        	 Started

These are the basic steps to get
                              		  up and running with Comet:

Start Jetty: Activate the Connection Jetty service by
                                    				browsing to the Cisco Unity Connection Serviceability page and selecting
                                    				Services. Find Connection Jetty in the list and select the Activate button.

Request Notifications: Clients need to request notifications
                                    				so that the Connection server knows it should start publishing Comet events for
                                    				the current authenticated user:

```
$.ajax({ 
 type: "POST", 
 contentType: "application/xml; charset=utf-8", 
 url: "/vmrest/mailbox?method=requestnotification", 
 data: "{}", 
 dataType: "text", 
 success: function(subscriptionId) { 
 gSubscriptionId = subscriptionId; 
 alert("Requested events for mailbox, subscriptionId=" + subscriptionId); 
 } 
 });
```

This returns a subscriptionId that must be used to get Comet
                                    				notifications for this user (rather than the userID, for security reasons).

Subscribe for events: This is just standard Comet now, but
                                    				there are a few details to know such as the port and URL to use. Jetty runs on
                                    				port 7080 for non SSL and port 7443 over SSL, and cometd is running at
                                    				/vmevents/cometd. Here's sample code to initialize and subscribe (in JQuery):

```
$.comet.init("http://connection-server:7080/vmevents/cometd"); 
 $.comet.subscribe("/vmrest/mailbox/" + gSubscriptionId, function(e) 
 { 
 alert("Event: " + e.data.EventType ); 
 });
```

## Comet Event
                        	 Structure

### Example Comet Notifications

Each Comet event has the
                              		  following attributes:

DisplayName

Display Name of Mailbox

SubscriptionId

Subscription ID

USN

Message USN

EventTime

Time of event

EventType

Type of event

MailboxId

Mailbox ID

MessageInfo

Array of message info objects(see below)

MessageInfo is an array of one or more objects with the
                              		  following attributes:

MessageId

CallerAni

MsgType

Priority

ReceiveTime

Sender

EventType will be one of the following:

EventType

Description

NEW_MESSAGE

This event is sent when a new message arrives in the inbox
                                             						folder.

SAVED_MESSAGE

This message is sent when a message is marked as read in the
                                             						inbox folder.

UNREAD_MESSAGE

This event is sent when a message is marked as unread in the
                                             						inbox folder.

DELETED_MESSAGE

This event is sent when a message is deleted from the inbox
                                             						folder.

DELETED_MESSAGE_CREATE

This event is sent when a new message arrives in the deleted
                                             						folder.

DELETED_MESSAGE_READ

This event is sent when a message is marked as read in the
                                             						deleted folder.

DELETED_MESSAGE_UNREAD

The event is sent when a message is marked as unread in the
                                             						deleted folder.

DELETED_MESSAGE_DELETE

The event is sent when a message is hard deleted from the
                                             						deleted folder or from the Inbox folder

DELETED_MESSAGE_UNDELETE

This event is sent when a message is marked as undeleted
                                             						from the Deleted folder.

Example 1: When a message is deleted from inbox folder or when a
                              		  new message arrives in the deleted folder, the following events take place:

DELETED_MESSAGE

DELETED_MESSAGE_CREATE

Example 2: When a message is marked as undeleted from deleted
                              		  folder, the following events take place:

SAVED_MESSAGE or UNREAD_MESSAGE

DELETED_MESSAGE_UNDELETE

Example 3:

When a message is marked as hard deleted from the inbox folder, the
                              		  following events take place:

DELETED_MESSAGE

DELETED_MESSAGE_CREATE

DELETED_MESSAGE_DELETE

Apart from the above examples, the USN is not the same for any of the
                              		  other notification scenarios.

Note: During the time Notifier service is down or inactive, if
                              		  there is any action taken on a message that is either in the Inbox or Deleted
                              		  folder, the notification for the latest status of that message is sent when the
                              		  service is back to its active state.

Example Comet Event

```
{ 
 "MessageInfo": [ { 
 "CallerAni": "null", 
 "Sender": "null", 
 "MessageId": "72204bd7-e5c3-446e-adb6-ae5f80db26fb", 
 "ReceiveTime": "04:15:40 PM 10/30/2008", 
 "Priority": "Normal-Priority", 
 "MsgType": "Voice" 
 }], 
 "USN": 2265, 
 "EventTime": "11:15:40 PM 10/30/2008", 
 "SubscriptionId": "00bdcfd3-159a-48d3-ac7b-2f3b4f83db6c", 
 "MailboxId": "abell", 
 "EventType": "SAVED_MESSAGE", 
 "DisplayName": "Alexander Bell"
 }
```

| $.ajax({ 
 type: "POST", 
 contentType: "application/xml; charset=utf-8", 
 url: "/vmrest/mailbox?method=requestnotification", 
 data: "{}", 
 dataType: "text", 
 success: function(subscriptionId) { 
 gSubscriptionId = subscriptionId; 
 alert("Requested events for mailbox, subscriptionId=" + subscriptionId); 
 } 
 }); |
|---|

| $.comet.init("http://connection-server:7080/vmevents/cometd"); 
 $.comet.subscribe("/vmrest/mailbox/" + gSubscriptionId, function(e) 
 { 
 alert("Event: " + e.data.EventType ); 
 }); |
|---|

| DisplayName | Display Name of Mailbox |
|---|---|
| SubscriptionId | Subscription ID |
| USN | Message USN |
| EventTime | Time of event |
| EventType | Type of event |
| MailboxId | Mailbox ID |
| MessageInfo | Array of message info objects(see below) |

| EventType | Description |
|---|---|
| NEW_MESSAGE | This event is sent when a new message arrives in the inbox
                                             						folder. |
| SAVED_MESSAGE | This message is sent when a message is marked as read in the
                                             						inbox folder. |
| UNREAD_MESSAGE | This event is sent when a message is marked as unread in the
                                             						inbox folder. |
| DELETED_MESSAGE | This event is sent when a message is deleted from the inbox
                                             						folder. |
| DELETED_MESSAGE_CREATE | This event is sent when a new message arrives in the deleted
                                             						folder. |
| DELETED_MESSAGE_READ | This event is sent when a message is marked as read in the
                                             						deleted folder. |
| DELETED_MESSAGE_UNREAD | The event is sent when a message is marked as unread in the
                                             						deleted folder. |
| DELETED_MESSAGE_DELETE | The event is sent when a message is hard deleted from the
                                             						deleted folder or from the Inbox folder |
| DELETED_MESSAGE_UNDELETE | This event is sent when a message is marked as undeleted
                                             						from the Deleted folder. |

| Note | The USN remains the same for both the notification events. |
|---|---|

| Note | The USN remains the same for both the notification events. |
|---|---|

| Note | The USN remains the same for the first two notification events. |
|---|---|

| { 
 "MessageInfo": [ { 
 "CallerAni": "null", 
 "Sender": "null", 
 "MessageId": "72204bd7-e5c3-446e-adb6-ae5f80db26fb", 
 "ReceiveTime": "04:15:40 PM 10/30/2008", 
 "Priority": "Normal-Priority", 
 "MsgType": "Voice" 
 }], 
 "USN": 2265, 
 "EventTime": "11:15:40 PM 10/30/2008", 
 "SubscriptionId": "00bdcfd3-159a-48d3-ac7b-2f3b4f83db6c", 
 "MailboxId": "abell", 
 "EventType": "SAVED_MESSAGE", 
 "DisplayName": "Alexander Bell"
 } |
|---|