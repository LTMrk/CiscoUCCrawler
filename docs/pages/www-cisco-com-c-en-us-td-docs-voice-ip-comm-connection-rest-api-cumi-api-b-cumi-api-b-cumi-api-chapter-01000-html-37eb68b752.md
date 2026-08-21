---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cumi-api-b-cumi-api-b-cumi-api-chapter-01000-html-37eb68b752
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUMI_API/b_CUMI-API/b_CUMI-API_chapter_01000.html
retrieved_at: 2026-08-21T08:06:40.373675+00:00
---

Cisco Unity Connection Messaging Interface (CUMI) API

# Cisco Unity Connection Messaging Interface (CUMI) API

Updated: December 23, 2018

Chapter: Cisco Unity Connection Messaging
	 Interface (CUMI) API -- Using the CUMI API for Broadcast Messages

## Chapter: Cisco Unity Connection Messaging
	 Interface (CUMI) API -- Using the CUMI API for Broadcast Messages

- Cisco Unity Connection Messaging                              	 Interface (CUMI) API -- Using the CUMI API for Broadcast Messages

- About Broadcast                              	 Messages

- Sending Broadcast                              	 Messages Reference

# Cisco Unity Connection Messaging
                     	 Interface (CUMI) API -- Using the CUMI API for Broadcast Messages

## About Broadcast
                        	 Messages

Broadcast messages are
                              		  system-owned messages that are meant to be heard by all users. The target user
                              		  is either the signed-in user or the user specified by an administrator by using
                              		  the optional "userobjectid=<user object id>" parameter.

URI

Method

Description

```
mailbox/broadcastmessages
```

GET

Returns a list of broadcast messages that are active and
                                             						have not yet been heard by the user.

```
mailbox/broadcastmessages/<message id>/voicefile
```

GET

Returns the broadcast message voice file.

```
mailbox/broadcastmessages/<message id>?read
```

POST

Marks the broadcast message as heard by the target user.

```
mailbox/broadcastmessages
```

POST

Sends a broadcast message (see below).

## Sending Broadcast
                        	 Messages Reference

### Schema

A broadcast message can be sent
                              		  by a POST request to the URI noted in the table above. The content of the
                              		  request is "mutipart/form-data". There must be two pieces of data in the
                              		  request in the following order:

A broadcast message in either "application/xml" or
                                    				"application/json" format.

Audio data as "audio/wav."

The only user-modifiable fields for a broadcast message are the start
                              		  date, end date, and the audio content. The rest of the fields are managed
                              		  internally.

```
<xs:complexType name="BroadcastMessage">
 <xs:all minOccurs="0">
 <xs:element name="URI" type="xs:anyURI" minOccurs="0" />
 <xs:element name="ObjectId" type="xs:string" minOccurs="0">
 <xs:annotation>
 <xs:documentation> The primary key for this table. A globally unique, system-generated identifier for a BroadcastMessage object.</xs:documentation>
 </xs:annotation>
 </xs:element>
 <xs:element name="StreamFileObjectId" type="xs:string" minOccurs="0">
 <xs:annotation>
 <xs:documentation>StreamFileObjectId - use StreamFile instead of this column. The unique identifier of the StreamFile object 
 containing the name of the WAV file that is the broadcast message.</xs:documentation>
 </xs:annotation>
 </xs:element>
 <xs:element name="VoiceFileURI" type="xs:anyURI" minOccurs="0" />
 <xs:element name="SubscriberObjectId" type="xs:string" minOccurs="0">
 <xs:annotation>
 <xs:documentation> The unique identifier of the Subscriber object that sent this broadcast message.</xs:documentation>
 </xs:annotation>
 </xs:element>
 <xs:element name="UserURI" type="xs:anyURI" minOccurs="0" />
 <xs:element name="CreationDate" type="xs:string" minOccurs="0">
 <xs:annotation>
 <xs:documentation> The date and time when the message was created.</xs:documentation>
 </xs:annotation>
 </xs:element>
 <xs:element name="StartDate" type="xs:string" minOccurs="0">
 <xs:annotation>
 <xs:documentation> The date and time when the message becomes active.</xs:documentation>
 </xs:annotation>
 </xs:element>
 <xs:element name="EndDate" type="xs:string" minOccurs="0">
 <xs:annotation>
 <xs:documentation> The date and time when the message expires.</xs:documentation>
 </xs:annotation>
 </xs:element>
 <xs:element name="LastModificationSubscriberObjectId" type="xs:string" minOccurs="0">
 <xs:annotation>
 <xs:documentation> The unique identifier of the subscriber that last modified the message.</xs:documentation>
 </xs:annotation>
 </xs:element>
 <xs:element name="LastModificationUserURI" type="xs:anyURI" minOccurs="0" />
 <xs:element name="LastModificationDate" type="xs:string" minOccurs="0">
 <xs:annotation>
 <xs:documentation> The date and time the message was last modified.</xs:documentation>
 </xs:annotation>
 </xs:element>
 <xs:element name="StreamFile" type="xs:string" minOccurs="0">
 <xs:annotation>
 <xs:documentation>Name of audio file for this broadcast message. The name of the WAV file containing 
 the recorded audio (voice name, greeting, etc.) for the parent object.</xs:documentation>
 </xs:annotation>
 </xs:element>
 </xs:all>
 </xs:complexType>
```

| URI | Method | Description |
|---|---|---|
| mailbox/broadcastmessages | GET | Returns a list of broadcast messages that are active and
                                             						have not yet been heard by the user. |
| mailbox/broadcastmessages/<message id>/voicefile | GET | Returns the broadcast message voice file. |
| mailbox/broadcastmessages/<message id>?read | POST | Marks the broadcast message as heard by the target user. |
| mailbox/broadcastmessages | POST | Sends a broadcast message (see below). |

| <xs:complexType name="BroadcastMessage">
 <xs:all minOccurs="0">
 <xs:element name="URI" type="xs:anyURI" minOccurs="0" />
 <xs:element name="ObjectId" type="xs:string" minOccurs="0">
 <xs:annotation>
 <xs:documentation> The primary key for this table. A globally unique, system-generated identifier for a BroadcastMessage object.</xs:documentation>
 </xs:annotation>
 </xs:element>
 <xs:element name="StreamFileObjectId" type="xs:string" minOccurs="0">
 <xs:annotation>
 <xs:documentation>StreamFileObjectId - use StreamFile instead of this column. The unique identifier of the StreamFile object 
 containing the name of the WAV file that is the broadcast message.</xs:documentation>
 </xs:annotation>
 </xs:element>
 <xs:element name="VoiceFileURI" type="xs:anyURI" minOccurs="0" />
 <xs:element name="SubscriberObjectId" type="xs:string" minOccurs="0">
 <xs:annotation>
 <xs:documentation> The unique identifier of the Subscriber object that sent this broadcast message.</xs:documentation>
 </xs:annotation>
 </xs:element>
 <xs:element name="UserURI" type="xs:anyURI" minOccurs="0" />
 <xs:element name="CreationDate" type="xs:string" minOccurs="0">
 <xs:annotation>
 <xs:documentation> The date and time when the message was created.</xs:documentation>
 </xs:annotation>
 </xs:element>
 <xs:element name="StartDate" type="xs:string" minOccurs="0">
 <xs:annotation>
 <xs:documentation> The date and time when the message becomes active.</xs:documentation>
 </xs:annotation>
 </xs:element>
 <xs:element name="EndDate" type="xs:string" minOccurs="0">
 <xs:annotation>
 <xs:documentation> The date and time when the message expires.</xs:documentation>
 </xs:annotation>
 </xs:element>
 <xs:element name="LastModificationSubscriberObjectId" type="xs:string" minOccurs="0">
 <xs:annotation>
 <xs:documentation> The unique identifier of the subscriber that last modified the message.</xs:documentation>
 </xs:annotation>
 </xs:element>
 <xs:element name="LastModificationUserURI" type="xs:anyURI" minOccurs="0" />
 <xs:element name="LastModificationDate" type="xs:string" minOccurs="0">
 <xs:annotation>
 <xs:documentation> The date and time the message was last modified.</xs:documentation>
 </xs:annotation>
 </xs:element>
 <xs:element name="StreamFile" type="xs:string" minOccurs="0">
 <xs:annotation>
 <xs:documentation>Name of audio file for this broadcast message. The name of the WAV file containing 
 the recorded audio (voice name, greeting, etc.) for the parent object.</xs:documentation>
 </xs:annotation>
 </xs:element>
 </xs:all>
 </xs:complexType> |
|---|