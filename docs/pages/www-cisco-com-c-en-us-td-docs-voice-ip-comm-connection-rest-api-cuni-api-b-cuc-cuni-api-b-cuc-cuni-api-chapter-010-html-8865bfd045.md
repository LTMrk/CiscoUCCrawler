---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cuni-api-b-cuc-cuni-api-b-cuc-cuni-api-chapter-010-html-8865bfd045
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUNI_API/b_CUC_CUNI_API/b_CUC_CUNI_API_chapter_010.html
retrieved_at: 2026-08-17T03:06:56.499469+00:00
---

Cisco Unity Connection Notification Interface (CUNI) API

# Cisco Unity Connection Notification Interface (CUNI) API

Updated: December 27, 2018

Chapter: Cisco Unity
	 Connection Notification Interface (CUNI) API -- Subscribing to and Processing
	 Notification Events

## Chapter: Cisco Unity
	 Connection Notification Interface (CUNI) API -- Subscribing to and Processing
	 Notification Events

- Cisco Unity                              	 Connection Notification Interface (CUNI) API -- Subscribing to and Processing                              	 Notification Events

- Subscribing to                              	 Notification Events

- Processing                              	 Notification Events

# Cisco Unity
                     	 Connection Notification Interface (CUNI) API -- Subscribing to and Processing
                     	 Notification Events

## Subscribing to
                        	 Notification Events

Subscribing to notification events is done through the web service
                              		  interface, and can be as simple as a single web service call to "subscribe".

At a minimum you should pass in:

- The callback URL where XML notifications will be posted by the Notifier.

- The date/time when the
                                    			 subscription will expire

It is also possible to pass in a list of the resources (userid) that
                              		  you are interested in receiving events for, although that can also be done via
                              		  a subsequent call to "addResourceIdToSubscription". We recommend that you leave
                              		  the eventTypeList empty, indicating that you would like to receive all types of
                              		  message events.

This example shows making a call to subscribe in Java, using Axis2
                              		  stubs generated from the WSDL:

```
Calendar expiration = java.util.Calendar.getInstance();
com.cisco.unity.messageeventservice.MessageEventServiceStub.Subscribe s = 
    new com.cisco.unity.messageeventservice.MessageEventServiceStub.Subscribe(); 

// Set subscription expiry to two months from now.
expiration.add(Calendar.MONTH, 2); 
s.setExpiration(expiration);

// Specify the users we're interested in, which is just the operator for this example.
ArrayOfString resourceList = new ArrayOfString(); 
resourceList.addString("operator");

s.setResourceIdList(resourceList); 
s.setExpiration(expiration);

// Set the callback information - a username and password can be specified, but they are optional.
MessageEventServiceStub.CallbackServiceInfo c = new MessageEventServiceStub.CallbackServiceInfo(); 
c.setCallbackServiceUrl(callbackUrl); 
c.setPassword(callbackPassword); 
c.setUsername(callbackUserId); 
s.setCallbackServiceInfo(c);

// Subscribe! 
SubscribeResponse r = stub.subscribe(s);
```

CUNI Subscriptions will be removed from Cisco Unity Connection server database, if you perform a refresh upgrade. Make sure
                                          to perform re-subscription after successful upgrade of the cluster.

## Processing
                        	 Notification Events

Events will be delivered via HTTP POST to the callback URL that was
                              		  provided in the call to subscribe.

Cisco Unity Connection Release 12.5(1) SU3 and later, CUNI supports HTTPS for callback URL.

For SSL communication user has the option to choose between Self-signed Certificates and Third Party CA signed Certificates
                                          from Cisco Unified Mobility Advantage server. Make sure to follow below mentioned steps for Third Party CA signed certificates:

Upload Third Party CA signed certificates in tomcat trust of Unity Connection server.

Restart Tomcat and Notifier services after adding certificates.

DELETED_MESSAGE_READ

This event is sent when a message is marked as read in the Deleted folder.

DELETED_MESSAGE_UNREAD

This event is sent when a message is marked as unread in the Deleted folder.

DELETED_MESSAGE_UNDELETE

This event is sent when a message is marked as undeleted from  the Deleted folder

TRANSCRIPTION_NEW_MESSAGE

This event is sent when transcribed message arrives on web clients.

Example

This is an example of an event xml. Please note that it is valid to have more than one messageInfo per messageEvent:

```
<?xml version="1.0" ?>
<messageEvent subscriptionId="00bdcfd3-159a-48d3-ac7b-2f3b4f83db6c"
              eventType="SAVED_MESSAGE"
              eventTime="11:15:40 PM 10/30/2008" 
              mailboxId="abell"
              displayName="Alexander Bell" 
              USN="2265">
    <messageInfo messageId="72204bd7-e5c3-446e-adb6-ae5f80db26fb"
                 receiveTime="04:15:40 PM 10/30/2008" 
                 uid="543"
                 msgType="Voice"
                 priority="Normal-Priority"
                 sender="null"
                 callerAni="null" />
</messageEvent>
```

After receiving notifications from CUNI API, if user want to perform messaging operations, then refer " Inbox Folder Operations " section of  "Cisco Unity Connection Messaging Interface (CUMI) API -- Using the CUMI API" chapter of Cisco Unity Connection Messaging Interface (CUMI) API Guide available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUMI_API/b_CUMI-API.html

| Calendar expiration = java.util.Calendar.getInstance();
com.cisco.unity.messageeventservice.MessageEventServiceStub.Subscribe s = 
    new com.cisco.unity.messageeventservice.MessageEventServiceStub.Subscribe(); 

// Set subscription expiry to two months from now.
expiration.add(Calendar.MONTH, 2); 
s.setExpiration(expiration);

// Specify the users we're interested in, which is just the operator for this example.
ArrayOfString resourceList = new ArrayOfString(); 
resourceList.addString("operator");

s.setResourceIdList(resourceList); 
s.setExpiration(expiration);

// Set the callback information - a username and password can be specified, but they are optional.
MessageEventServiceStub.CallbackServiceInfo c = new MessageEventServiceStub.CallbackServiceInfo(); 
c.setCallbackServiceUrl(callbackUrl); 
c.setPassword(callbackPassword); 
c.setUsername(callbackUserId); 
s.setCallbackServiceInfo(c);

// Subscribe! 
SubscribeResponse r = stub.subscribe(s); |
|---|

| Note | CUNI Subscriptions will be removed from Cisco Unity Connection server database, if you perform a refresh upgrade. Make sure
                                          to perform re-subscription after successful upgrade of the cluster. |
|---|---|

| Note | Cisco Unity Connection Release 12.5(1) SU3 and later, CUNI supports HTTPS for callback URL. For SSL communication user has the option to choose between Self-signed Certificates and Third Party CA signed Certificates
                                          from Cisco Unified Mobility Advantage server. Make sure to follow below mentioned steps for Third Party CA signed certificates: Upload Third Party CA signed certificates in tomcat trust of Unity Connection server. Restart Tomcat and Notifier services after adding certificates. |
|---|---|

| Event Type | Description |
|---|---|
| NEW_MESSAGE | This event is sent when a new message arrives in the Inbox folder. |
| SAVED_MESSAGE | This event is sent when a message is marked as read in the Inbox folder. |
| UNREAD_MESSAGE | This event is sent when a message is marked as unread in the Inbox folder. |
| DELETED_MESSAGE | This event is sent when a message is deleted from the Inbox folder. |
| DELETED_MESSAGE_DELETE | This event is sent when a message is hard deleted from the Deleted folder or from the Inbox folder. |
| DELETED_MESSAGE_CREATE | This event is sent when a new message arrives in the Deleted folder. |
| DELETED_MESSAGE_READ | This event is sent when a message is marked as read in the Deleted folder. |
| DELETED_MESSAGE_UNREAD | This event is sent when a message is marked as unread in the Deleted folder. |
| DELETED_MESSAGE_UNDELETE | This event is sent when a message is marked as undeleted from  the Deleted folder |
| TRANSCRIPTION_NEW_MESSAGE | This event is sent when transcribed message arrives on web clients. |

| <?xml version="1.0" ?>
<messageEvent subscriptionId="00bdcfd3-159a-48d3-ac7b-2f3b4f83db6c"
              eventType="SAVED_MESSAGE"
              eventTime="11:15:40 PM 10/30/2008" 
              mailboxId="abell"
              displayName="Alexander Bell" 
              USN="2265">
    <messageInfo messageId="72204bd7-e5c3-446e-adb6-ae5f80db26fb"
                 receiveTime="04:15:40 PM 10/30/2008" 
                 uid="543"
                 msgType="Voice"
                 priority="Normal-Priority"
                 sender="null"
                 callerAni="null" />
</messageEvent> |
|---|