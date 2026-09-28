---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cumi-api-b-cumi-api-b-cumi-api-chapter-0111-html-f0ddcf7b15
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUMI_API/b_CUMI-API/b_CUMI-API_chapter_0111.html
retrieved_at: 2026-08-21T08:06:36.107401+00:00
---

Cisco Unity Connection Messaging Interface (CUMI) API

# Cisco Unity Connection Messaging Interface (CUMI) API

Updated: December 23, 2018

Chapter: Cisco Unity Connection Messaging
	 Interface (CUMI) API -- Dispatch Message Operations

## Chapter: Cisco Unity Connection Messaging
	 Interface (CUMI) API -- Dispatch Message Operations

# Cisco Unity Connection Messaging
                     	 Interface (CUMI) API -- Dispatch Message Operations

## About Dispatch
                        	 Messages

A

Dispatch message

is a message that needs to go to one and only one member of a group.
                           		When the message is accepted by any one user, it is no longer available to
                           		other users. When the message is rejected by a user in the group, it is removed
                           		from the user's voicemail list.

## Sending a
                        	 Dispatch Message

Sending a
                              		  Dispatch Message is very similar to sending any other CUMI Message. To sending
                              		  a Dispatch message, a Boolean field (<Dispatch>) is set on the POST API
                              		  call.

```
<Dispatch>true</Dispatch>
```

For more details
                              		  on using the CUMI to send messages, refer here

## Accepting or
                        	 Rejecting a Dispatch Message

A POST API call on the Message
                              		  can be used to accept or reject a Dispatch message.

```
POST /vmrest/messages/{messageObjectId}?method=accept
POST /vmrest/messages/{messageObjectId}?method=reject
```

| <Dispatch>true</Dispatch> |
|---|

| POST /vmrest/messages/{messageObjectId}?method=accept
POST /vmrest/messages/{messageObjectId}?method=reject |
|---|