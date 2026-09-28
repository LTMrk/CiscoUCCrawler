---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-user-playback-message-setting-e79c6463bd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_cupi-user-playback-message-setting.html
retrieved_at: 2026-08-17T03:48:21.378425+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Playback Message Settings

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Playback Message Settings

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- User Playback Message Settings

Links to Other API pages: Cisco_Unity_Connection_APIs

## Playback Message
                        	 Settings API

The following URI can be used to
                              		  view the playback message settings of the specific user:

```
GET https://<connection-server>/vmrest/users/<user-objectid>
```

### Edit Parameters

```
PUT https://<connection-server>/vmrest/users/<user-objectid>
```

```
<User>
  <Volume>50</Volume>
  <Speed>100</Speed>
  <SayTotalNew>true</SayTotalNew>
  <SayTotalNewVoice>true</SayTotalNewVoice>
  <SayTotalNewEmail>false</SayTotalNewEmail>
  <SayTotalNewFax>false</SayTotalNewFax>
  <SayTotalReceipts>false</SayTotalReceipts>
  <SayTotalSaved>true</SayTotalSaved>
  <SayTotalDraftMsg>false</SayTotalDraftMsg>
  <MessageTypeMenu>false</MessageTypeMenu>
  <NewMessageSortOrder>2</NewMessageSortOrder>
  <SaveMessageOnHangup>1</SaveMessageOnHangup>
  <DeletedMessageSortOrder>1</DeletedMessageSortOrder>
  <SaySender>true</SaySender>
  <SaySenderExtension>false</SaySenderExtension> 
  <SayAni>true</SayAni>
  <SayMsgNumber>true</SayMsgNumber>
  <SayTimestampBefore>true</SayTimestampBefore>
  <AutoAdvanceMsgs>false</AutoAdvanceMsgs>
  <ConfirmDeleteMessage>true</ConfirmDeleteMessage>
</User>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

for new message:

```
<NewMessageSortOrder>
 2
</NewMessageSortOrder>
```

for saved message:

```
<SaveMessageSortOrder>
 1 
</SaveMessageSortOrder>
```

for deleted message:

```
<DeletedMessageSortOrder>
 1
</DeletedMessageSortOrder>
```

All the possible values for above three parameters are given in the
                                 		  table.

JSON Example

```
PUT https://<connection-server>/vmrest/users/<user-objectid>
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

```
Request Body:
{
  "Volume":"50"
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Explanation of
                           	 Data Fields

Possible values:

- 25: Low

- 50: Medium

- 100: High

Default value: 50

- 50: Slow

- 100: Normal

- 150: Fast

- 200: Fastest

Default value: 100

Possible values:

- false: Do not
                                                      						  announce total number of new messages.

- true: Announce
                                                      						  the total number of new messages in the subscriber mailbox.

Default Value: false

Possible values:

- false: Do not
                                                      						  announce total number of new e-mail messages.

- true: Announce
                                                      						  the total number of new e-mail messages in the subscriber mailbox.

Default Value: false

- false: Do not
                                                      						  announce total number of new fax messages.

- true: Announce
                                                      						  the total number of new fax messages in the subscriber mailbox.

Default Value: false

- false: Do not
                                                      						  announce total number of new voice messages.

- true: Announce
                                                      						  the total number of new voice messages in the subscriber mailbox.

Default Value: true

Possible values:

- false: Do not
                                                      						  announce total number of new receipts.

- true: Announce
                                                      						  the total number of new receipts in the subscriber mailbox.

Default Value: false

Possible values:

- false: Do not
                                                      						  announce total number of saved messages.

- true: Announce
                                                      						  the total number of saved messages in the subscriber mailbox.

Default Value: false

Possible values

- false: Do not
                                                      						  announce total number of draft messages.

- true: Announce
                                                      						  the total number of draft messages in the subscriber mailbox.

Default Value: false

Possible values:

- false: Do not
                                                      						  play message type menu

- true: Play
                                                      						  message type menu

Default Value: false

Possible values:

- Urgent voice
                                                      						  messages

- Non-urgent voice
                                                      						  messages

- Urgent fax
                                                      						  messages

- Non-urgent fax
                                                      						  messages

- Urgent e-mail
                                                      						  messages

- Non-urgent
                                                      						  e-mail messages

- Receipts and
                                                      						  notices

Possible Values:

- false: Message
                                                      						  is marked new again

- true: Message is
                                                      						  marked read

Default Value: false

- Urgent voice
                                                      						  messages

- Non-urgent voice
                                                      						  messages

- Urgent fax
                                                      						  messages

- Non-urgent fax
                                                      						  messages

- Urgent e-mail
                                                      						  messages

- Non-urgent
                                                      						  e-mail messages

- Receipts and
                                                      						  notices

Possible values:

- 1: Newest First

- 2: Oldest First

Default Value: 1

Possible values:

- 1: Newest First

- 2: Oldest First

Default Value: 2

Possible values:

- 1: Newest First

- 2: Oldest First

Default Value: 2

Possible values:

- false: Do not
                                                      						  announce the sender.

- true: Announce
                                                      						  the sender.

Default Value: true

Possible values:

- false: Do not
                                                      						  play the extension information of the subscriber who sent the message.

- true: After
                                                      						  playing the sender's voice name, play the primary extension information of the
                                                      						  subscriber who sent the message.

Possible Values:

- true

- false

Default value: false

Possible values:

- false: Do not
                                                      						  play the message number.

- true: Play the
                                                      						  message number.

Default value: true

- false: Do not
                                                      						  announce the timestamp before each message is played.

- true: Announce
                                                      						  the timestamp before each message is played.

Default value: false

possible values:

- true

- false

Default value: false

Default Value: 5000 The range can vary from 1000 to 60000.

Default Value: 5000 The range can vary from 1000 to 60000.

Possible values:

- false: Message
                                                      						  Bookmark feature is disabled for subscriber

- true: Message
                                                      						  Bookmark feature is enabled for subscriber

Default value: false

- false: Message
                                                      						  is marked new again

- true: Message is
                                                      						  marked read

Default Value: false

Possible Values:

- false: Do not
                                                      						  announce the sender.

- True: Announce
                                                      						  the sender.

Possible Values:

- false: Do not
                                                      						  play the extension information of the subscriber who sent the message.

- true- After
                                                      						  playing the sender's voice name, play the primary extension information of the
                                                      						  subscriber who sent the message.

Possible Values:

- false: Do not
                                                      						  play the message number.

- true: Play the
                                                      						  message number.

Possible Values:

- true

- false

Default value: false

Possible Values:

- true

- false

Default value: false

Possible Values:

- false: Do not
                                                      						  automatically skip to the next message after playing the After Message Menu
                                                      						  once.

- true:
                                                      						  Automatically skip to the next message after playing the After Message Menu
                                                      						  once.

Default Value: false

- false: system
                                                      						  will not request confirmation from a subscriber before proceeding with a
                                                      						  deletion of a single new or saved message.

- true: system
                                                      						  will request confirmation from a subscriber before proceeding with a deletion
                                                      						  of a single new or saved message.

Default Value: false

| GET https://<connection-server>/vmrest/users/<user-objectid> |
|---|

| PUT https://<connection-server>/vmrest/users/<user-objectid> |
|---|

| <User>
  <Volume>50</Volume>
  <Speed>100</Speed>
  <SayTotalNew>true</SayTotalNew>
  <SayTotalNewVoice>true</SayTotalNewVoice>
  <SayTotalNewEmail>false</SayTotalNewEmail>
  <SayTotalNewFax>false</SayTotalNewFax>
  <SayTotalReceipts>false</SayTotalReceipts>
  <SayTotalSaved>true</SayTotalSaved>
  <SayTotalDraftMsg>false</SayTotalDraftMsg>
  <MessageTypeMenu>false</MessageTypeMenu>
  <NewMessageSortOrder>2</NewMessageSortOrder>
  <SaveMessageOnHangup>1</SaveMessageOnHangup>
  <DeletedMessageSortOrder>1</DeletedMessageSortOrder>
  <SaySender>true</SaySender>
  <SaySenderExtension>false</SaySenderExtension> 
  <SayAni>true</SayAni>
  <SayMsgNumber>true</SayMsgNumber>
  <SayTimestampBefore>true</SayTimestampBefore>
  <AutoAdvanceMsgs>false</AutoAdvanceMsgs>
  <ConfirmDeleteMessage>true</ConfirmDeleteMessage>
</User> |
|---|

| Response Code: 204 |
|---|

| Note | To sort the message type: |
|---|---|

| <NewMessageSortOrder>
 2
</NewMessageSortOrder> |
|---|

| <SaveMessageSortOrder>
 1 
</SaveMessageSortOrder> |
|---|

| <DeletedMessageSortOrder>
 1
</DeletedMessageSortOrder> |
|---|

| PUT https://<connection-server>/vmrest/users/<user-objectid>
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| Request Body:
{
  "Volume":"50"
} |
|---|

| Response Code: 204 |
|---|

| Parameters | Data Type | Operation | Description |
|---|---|---|---|
| Volume | Integer | Read/Write | The audio volume expressed as a percentage
                                             					 that Cisco Unity Connection uses to play back message. The range can vary from
                                             					 0 to 100. Possible values: 25: Low 50: Medium 100: High Default value: 50 |
| Speed | Integer | Read/Write | The audio speed system uses to play back
                                             					 messages to the subscriber. The range can vary from 0 to 200. 50: Slow 100: Normal 150: Fast 200: Fastest Default value: 100 |
| SayTotalNew | Boolean | Read/Write | A flag indicating whether system announces
                                             					 the total number of new messages in the subscriber mailbox. Possible values: false: Do not
                                                      						  announce total number of new messages. true: Announce
                                                      						  the total number of new messages in the subscriber mailbox. Default Value: false |
| SayTotalNewEmail | Boolean | Read/Write | A flag indicating whether system announces
                                             					 the total number of new e-mail messages in the subscriber mailbox Possible values: false: Do not
                                                      						  announce total number of new e-mail messages. true: Announce
                                                      						  the total number of new e-mail messages in the subscriber mailbox. Default Value: false |
| SayTotalNewFax | Boolean | Read/Write | A flag indicating whether system announces
                                             					 the total number of new fax messages in the subscriber mailbox. false: Do not
                                                      						  announce total number of new fax messages. true: Announce
                                                      						  the total number of new fax messages in the subscriber mailbox. Default Value: false |
| SayTotalNewVoice | Boolean | Read/Write | A flag indicating whether system announces
                                             					 the total number of new voice messages in the subscriber mailbox. false: Do not
                                                      						  announce total number of new voice messages. true: Announce
                                                      						  the total number of new voice messages in the subscriber mailbox. Default Value: true |
| SayTotalReceipts | Boolean | Read/Write | A flag indicating whether system announces
                                             					 the total number of new receipts in the subscriber mailbox. Possible values: false: Do not
                                                      						  announce total number of new receipts. true: Announce
                                                      						  the total number of new receipts in the subscriber mailbox. Default Value: false |
| SayTotalSaved | Boolean | Read/Write | A flag indicating whether system announces
                                             					 the total number of saved messages in the subscriber mailbox. Possible values: false: Do not
                                                      						  announce total number of saved messages. true: Announce
                                                      						  the total number of saved messages in the subscriber mailbox. Default Value: false |
| SayTotalDraftMsg | Boolean | Read/Write | A flag indicating whether Cisco Unity
                                             					 Connection announces the total number of draft messages in the subscriber
                                             					 mailbox. Possible values false: Do not
                                                      						  announce total number of draft messages. true: Announce
                                                      						  the total number of draft messages in the subscriber mailbox. Default Value: false |
| MessageTypeMenu | Boolean | Read/Write | A flag indicating whether system plays the
                                             					 message type menu when the subscriber logs on to system over the phone. Possible values: false: Do not
                                                      						  play message type menu true: Play
                                                      						  message type menu Default Value: false |
| NewMessageStackOrder | String | Read/Write | The order in which system plays the
                                             					 following types new messages: Possible values: Urgent voice
                                                      						  messages Non-urgent voice
                                                      						  messages Urgent fax
                                                      						  messages Non-urgent fax
                                                      						  messages Urgent e-mail
                                                      						  messages Non-urgent
                                                      						  e-mail messages Receipts and
                                                      						  notices |
| SaveMessageOnHangup | Boolean | Read/Write | A flag indicating when hanging up while
                                             					 listening to a new message, whether the message is marked new again or is
                                             					 marked read. Possible Values: false: Message
                                                      						  is marked new again true: Message is
                                                      						  marked read Default Value: false |
| SavedMessageStackOrder | String(36) | Read/Write | The order in which system plays the
                                             					 following types of saved messages: Urgent voice
                                                      						  messages Non-urgent voice
                                                      						  messages Urgent fax
                                                      						  messages Non-urgent fax
                                                      						  messages Urgent e-mail
                                                      						  messages Non-urgent
                                                      						  e-mail messages Receipts and
                                                      						  notices |
| NewMessageSortOrder | Integer | Read/Write | The order in which Cisco Unity Connection
                                             					 will sort new messages. Possible values: 1: Newest First 2: Oldest First Default Value: 1 |
| SavedMessageSortOrder | Integer | Read/Write | The order in which Cisco Unity Connection
                                             					 will sort saved messages.. Possible values: 1: Newest First 2: Oldest First Default Value: 2 |
| DeleteMessageSortOrder | Integer | Read/Write | The order in which Cisco Unity Connection
                                             					 presents deleted messages to the subscriber. Possible values: 1: Newest First 2: Oldest First Default Value: 2 |
| SaySender | Boolean | Read/Write | A flag indicating whether system announces
                                             					 the sender of a message during message playback for the subscriber. Possible values: false: Do not
                                                      						  announce the sender. true: Announce
                                                      						  the sender. Default Value: true |
| SaySenderExtension | Boolean | Read/Write | A flag indicating whether Cisco Unity
                                             					 Connection during message playback, plays the primary extension information of
                                             					 the subscriber who sent the message after playing the sender's voice name. Possible values: false: Do not
                                                      						  play the extension information of the subscriber who sent the message. true: After
                                                      						  playing the sender's voice name, play the primary extension information of the
                                                      						  subscriber who sent the message. |
| SayAni | Boolean | Read/Write | A flag indicating whether Cisco Unity
                                             					 Connection plays the Automatic Number Identification (ANI) information during
                                             					 message playback for voice messages from unidentified callers. Possible Values: true false Default value: false |
| SayMsgNumber | Boolean | Read/Write | A flag indicating whether system announces
                                             					 the position of each message in the stack (i.e., 'Message 1', 'Message 2'
                                             					 ,etc.) during message playback for the subscriber. Possible values: false: Do not
                                                      						  play the message number. true: Play the
                                                      						  message number. Default value: true |
| SayTimestampBefore | Boolean | Read/Write | A flag indicating whether system announces
                                             					 the timestamp before it plays back each for the subscriber. false: Do not
                                                      						  announce the timestamp before each message is played. true: Announce
                                                      						  the timestamp before each message is played. Default value: false |
| SayMessageLength | Boolean | Read/Write | A flag indicating whether Cisco Unity
                                             					 Connection announces the length of each message during message playback. possible values: true false Default value: false |
| SkipForwardTime | Integer | Read/Write | Indicates the amount of time (in
                                             					 milliseconds) to jump forward when skipping ahead in a voice or TTS message
                                             					 using either DTMF or voice commands while reviewing messages. Default Value: 5000 The range can vary from 1000 to 60000. |
| SkipReverseTime | Integer | Read/Write | Indicates the amount of time (in
                                             					 milliseconds) to jump backward when skipping in reverse in a voice or TTS
                                             					 message using either DTMF or voice commands while reviewing messages. Default Value: 5000 The range can vary from 1000 to 60000. |
| EnableMessageBookmark | Boolean | Read/Write | A flag indicating whether Message Bookmark
                                             					 is enabled for the subscriber Possible values: false: Message
                                                      						  Bookmark feature is disabled for subscriber true: Message
                                                      						  Bookmark feature is enabled for subscriber Default value: false |
| SaveMessageOnHangup | Boolean | Read/Write | A flag indicating when hanging up while
                                             					 listening to a new message, whether the message is marked new again or is
                                             					 marked read. false: Message
                                                      						  is marked new again true: Message is
                                                      						  marked read Default Value: false |
| SaySenderAfter | Boolean | Read/Write | This flag works exactly the same as the
                                             					 SaySender flag on a user, except the conversation plays the sender in the
                                             					 message footer. Possible Values: false: Do not
                                                      						  announce the sender. True: Announce
                                                      						  the sender. |
| SaySenderExtensionAfter | Boolean | Read/Write | This flag works exactly the same as the
                                             					 SaySenderExtension flag on a user, except the conversation plays the sender's
                                             					 extension in the message footer. Possible Values: false: Do not
                                                      						  play the extension information of the subscriber who sent the message. true- After
                                                      						  playing the sender's voice name, play the primary extension information of the
                                                      						  subscriber who sent the message. |
| SayMsgNumberAfter | Boolean | Read/Write | This flag works exactly the same as the
                                             					 SayMsgNumber flag on a user, except the conversation plays the message number
                                             					 in the message footer. Possible Values: false: Do not
                                                      						  play the message number. true: Play the
                                                      						  message number. |
| SayAniAfter | Boolean | Read/Write | This flag works exactly the same as the
                                             					 SayAni flag on a user, except the conversation plays the ani in the message
                                             					 footer. Possible Values: true false Default value: false |
| SayMessageLengthAfter | Boolean | Read/Write | This flag works exactly the same as the
                                             					 SayMessageLength flag on a user, except the conversation plays the message
                                             					 length in the message footer. Possible Values: true false Default value: false |
| AutoAdvanceMsgs | Boolean | Read/Write | A flag indicating whether the conversation
                                             					 moves to the next message in the playback stack automatically during playback
                                             					 after playing the After Message Menu. Possible Values: false: Do not
                                                      						  automatically skip to the next message after playing the After Message Menu
                                                      						  once. true:
                                                      						  Automatically skip to the next message after playing the After Message Menu
                                                      						  once. Default Value: false |
| ConfirmDeleteMessage | Boolean | Read/Write | A flag indicating whether system will
                                             					 request confirmation from a subscriber before proceeding with a deletion of a
                                             					 single new or saved message. false: system
                                                      						  will not request confirmation from a subscriber before proceeding with a
                                                      						  deletion of a single new or saved message. true: system
                                                      						  will request confirmation from a subscriber before proceeding with a deletion
                                                      						  of a single new or saved message. Default Value: false |