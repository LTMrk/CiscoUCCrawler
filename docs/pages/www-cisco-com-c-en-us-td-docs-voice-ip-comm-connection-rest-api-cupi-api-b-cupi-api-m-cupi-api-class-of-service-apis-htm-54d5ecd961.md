---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-api-class-of-service-apis-htm-54d5ecd961
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_cupi-api-class-of-service-apis.html
retrieved_at: 2026-08-17T03:49:08.192348+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- Class of Service (COS) APIs

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- Class of Service (COS) APIs

# Cisco Unity Connection Provisioning Interface (CUPI) API -- Class of Service (COS) APIs

## Classes of
                        	 Service

A class of service (COS) defines limits and permissions for accounts
                              		  with voice mailboxes. For example, a COS.

- Controls user access to licensed features such as the Cisco Unity Connection Web Inbox (Connection 8.5 and later) or Messaging
                                 Inbox (Connection 8.0). (When a COS includes access to a feature that requires individual licenses, you can assign groups
                                 of users to the COS only if enough licenses are available.)

- Controls user access to non-licensed features such as personal call transfer rules.

- Controls how users interact with Connection. For example, a COS dictates the maximum length of user messages and greetings,
                                 and whether users can choose to be listed in the corporate directory.

- Controls call transfer options.

- Specifies the number of private distribution lists allowed to users, and the number of members allowed on each list.

- Specifies the restriction tables used to control the phone numbers that users can use for transfers and when placing calls.

A COS is not specified for the individual accounts or templates that
                              		  are associated with users without voice mailboxes (typically, these are
                              		  administrator accounts). Permissions associated with administrator accounts are
                              		  instead controlled by roles in Connection Administration.

Default Classes of Service in Cisco Unity Connection

Administrator can use this API to create/update/delete/fetch the Class
                              		  of Service. Various attributes of Class of Service can also be updated using
                              		  this API.

### Listing the Class
                           	 of Services

The following is an example of
                                 		  the GET request that lists all the class of services:

```
GET https://<connection-server>/vmrest/coses
```

The following is an example of the response from the above *GET*
                                 		  request:

```
<Coses total="3">
  <Cos>
    <URI>/vmrest/coses/6e2c52a8-6bb6-40b0-b31e-27627293520c</URI>
    <ObjectId>6e2c52a8-6bb6-40b0-b31e-27627293520c</ObjectId>
    <DisplayName>Voice Mail User COS</DisplayName>
  </Cos>
  <Cos>
    <URI>/vmrest/coses/4af565ec-47d5-43be-9c3b-49d5ea995f63</URI>
    <ObjectId>4af565ec-47d5-43be-9c3b-49d5ea995f63</ObjectId>
    <DisplayName>System</DisplayName>
  </Cos>
  <Cos>
    <URI>/vmrest/coses/870f9a46-cc28-4d55-8fbd-e89cd02b9ff8</URI>
    <ObjectId>870f9a46-cc28-4d55-8fbd-e89cd02b9ff8</ObjectId>
    <DisplayName>Taxoma_COS_1</DisplayName>
  </Cos>
  </Coses>
```

```
Response Code: 200
```

JSON Example

To list all class of services, do the following: < pre> Request URI: GET https://<connection-server>/vmrest/coses Accept:
                                 application /json Connection: keep-alive < /pre> The following is the response from the above *GET* request and the actual
                                 response will depend upon the information given by you:

```
{
  "@total": "3",
  "Cos": [
{
    "URI": "/vmrest/coses/6e2c52a8-6bb6-40b0-b31e-27627293520c",
    "ObjectId": "6e2c52a8-6bb6-40b0-b31e-27627293520c",
    "DisplayName": "Voice Mail User COS"
},
{
    "URI": "/vmrest/coses/4af565ec-47d5-43be-9c3b-49d5ea995f63",
    "ObjectId": "4af565ec-47d5-43be-9c3b-49d5ea995f63",
    "DisplayName": "System"
},
{
"URI": "/vmrest/coses/870f9a46-cc28-4d55-8fbd-e89cd02b9ff8",
"ObjectId": "870f9a46-cc28-4d55-8fbd-e89cd02b9ff8",
"DisplayName": "Taxoma_COS_1"
}
]
}
```

```
Response Code: 200
```

### Viewing the
                           	 Specific Class of Services

The following is an example of
                                 		  the GET request that lists the details of specific class of services
                                 		  represented by the provided value of class of services object ID:

```
GET https://<connection-server>/vmrest/coses/<cosobjectid>
```

The following is the response from the above *GET* request:

```
<Cos>
    <URI>/vmrest/coses/77862e8e-42f3-4dac-811d-0be5291a9504</URI>
    <ObjectId>77862e8e-42f3-4dac-811d-0be5291a9504</ObjectId>
    <AccessFaxMail>false</AccessFaxMail>
    <AccessTts>false</AccessTts>
    <CallHoldAvailable>false</CallHoldAvailable>
    <CallScreenAvailable>false</CallScreenAvailable>
    <CanRecordName>true</CanRecordName>
    <FaxRestrictionObjectId>8045d752-6723-4062-9fc3-22090b85b5d7</FaxRestrictionObjectId>
    <ListInDirectoryStatus>true</ListInDirectoryStatus>
    <LocationObjectId>359e627b-c481-4428-8674-bc28f40e8d43</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/359e627b-c481-4428-8674-bc28f40e8d43</LocationURI>
    <MaxGreetingLength>90</MaxGreetingLength>
    <MaxMsgLength>300</MaxMsgLength>
    <MaxNameLength>30</MaxNameLength>
    <MaxPrivateDlists>25</MaxPrivateDlists>
    <MovetoDeleteFolder>true</MovetoDeleteFolder>
    <OutcallRestrictionObjectId>9c07accb-2187-4ca4-baf4-6ae0613f605a</OutcallRestrictionObjectId>
    <PersonalAdministrator>true</PersonalAdministrator>
    <DisplayName>HELLO_COS_1</DisplayName>
    <XferRestrictionObjectId>9c040521-fb05-4ba7-ba8f-d4f06f140b4c</XferRestrictionObjectId>
    <Undeletable>false</Undeletable>
    <WarnIntervalMsgEnd>0</WarnIntervalMsgEnd>
    <CanSendToPublicDl>true</CanSendToPublicDl>
    <EnableEnhancedSecurity>false</EnableEnhancedSecurity>
    <AccessVmi>false</AccessVmi>
    <AccessLiveReply>false</AccessLiveReply>
    <UaAlternateExtensionAccess>0</UaAlternateExtensionAccess>
    <AccessCallRoutingRules>false</AccessCallRoutingRules>
    <WarnMinMsgLength>0</WarnMinMsgLength>
    <SendBroadcastMessage>false</SendBroadcastMessage>
    <UpdateBroadcastMessage>false</UpdateBroadcastMessage>
    <AccessVui>false</AccessVui>
    <ImapCanFetchMessageBody>true</ImapCanFetchMessageBody>
    <ImapCanFetchPrivateMessageBody>false</ImapCanFetchPrivateMessageBody>
    <MaxMembersPVL>99</MaxMembersPVL>
    <AccessIMAP>false</AccessIMAP>
    <ReadOnly>false</ReadOnly>
    <AccessAdvancedUserFeatures>false</AccessAdvancedUserFeatures>
    <AccessAdvancedUser>false</AccessAdvancedUser>
    <AccessUnifiedClient>false</AccessUnifiedClient>
    <RequireSecureMessages>4</RequireSecureMessages>
    <AccessOutsideLiveReply>false</AccessOutsideLiveReply>
    <AccessSTT>false</AccessSTT>
    <EnableSTTSecureMessage>0</EnableSTTSecureMessage>
    <MessagePlaybackRestriction>0</MessagePlaybackRestriction>
    <SttType>1</SttType>
</Cos>
```

```
Response Code: 200
```

JSON Example

To view individual class of services, do the following

```
Request URI:
GET https://<connection-server>/vmrest/coses/<cosobjectid>
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
{
    "URI": "/vmrest/coses/77862e8e-42f3-4dac-811d-0be5291a9504",
    "ObjectId": "77862e8e-42f3-4dac-811d-0be5291a9504",
    "AccessFaxMail": "false",
    "AccessTts": "false",
    "CallHoldAvailable": "false",
    "CallScreenAvailable": "false",
    "CanRecordName": "true",
    "FaxRestrictionObjectId": "8045d752-6723-4062-9fc3-22090b85b5d7",
    "ListInDirectoryStatus": "true",
    "LocationObjectId": "359e627b-c481-4428-8674-bc28f40e8d43",
    "LocationURI": "/vmrest/locations/connectionlocations/359e627b-c481-4428-8674-bc28f40e8d43",
    "MaxGreetingLength": "90",
    "MaxMsgLength": "300",
    "MaxNameLength": "30",
    "MaxPrivateDlists": "25",
    "MovetoDeleteFolder": "true",
    "OutcallRestrictionObjectId": "9c07accb-2187-4ca4-baf4-6ae0613f605a",
    "PersonalAdministrator": "true",
    "DisplayName": "HELLO_COS_1",
    "XferRestrictionObjectId": "9c040521-fb05-4ba7-ba8f-d4f06f140b4c",
    "Undeletable": "false",
    "WarnIntervalMsgEnd": "0",
    "CanSendToPublicDl": "true",
    "EnableEnhancedSecurity": "false",
    "AccessVmi": "false",
    "AccessLiveReply": "false",
    "UaAlternateExtensionAccess": "0",
    "AccessCallRoutingRules": "false",
    "WarnMinMsgLength": "0",
    "SendBroadcastMessage": "false",
    "UpdateBroadcastMessage": "false",
    "AccessVui": "false",
    "ImapCanFetchMessageBody": "true",
    "ImapCanFetchPrivateMessageBody": "false",
    "MaxMembersPVL": "99",
    "AccessIMAP": "false",
    "ReadOnly": "false",
    "AccessAdvancedUserFeatures": "false",
    "AccessAdvancedUser": "false",
    "AccessUnifiedClient": "false",
    "RequireSecureMessages": "4",
    "AccessOutsideLiveReply": "false",
    "AccessSTT": "false",
    "EnableSTTSecureMessage": "0",
    "MessagePlaybackRestriction": "0",
    "SttType": "1"
}
```

```
Response Code: 200
```

### Creating a Class
                           	 of Services

You can create a new class of services in a generic way or by giving
                                 		  restriction tables as input.

Example 1: In a generic way

```
POST https://<connection-server>/vmrest/coses
Request Body:
<Cos>
<DisplayName>Texoma_cos_1</DisplayName>
</Cos>
```

The following is an example of the *POST* request that creates a new
                                 		  class of service in a generic way:

```
Response Code: 201
```

JSON Example

To create new COS, do the following:

```
Request URI:
POST https://<connection-server>/vmrest/coses
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "DisplayName":"Texoma_cos_1"
}
```

The following is the response from the above *POST* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 201
```

Example 2: Giving restriction tables as input

The following is an example of the *POST* request that creates a new
                                 		  class of services by giving restriction tables as input:

```
POST https://<connection-server>/vmrest/coses
Request Body:
<cos>
    <DisplayName>Texoma_cos</DisplayName>
    <FaxRestrictionObjectId>3da15ac5-e56f-4fac-b631-9f08826e1472</FaxRestrictionObjectId>
    <OutcallRestrictionObjectId>3da15ac5-e56f-4fac-b631-9f08826e1472</OutcallRestrictionObjectId>
    <XferRestrictionObjectId>3da15ac5-e56f-4fac-b631-9f08826e1472</XferRestrictionObjectId>
</cos>
```

The following is the response from the above *POST* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 201
```

JSON Example:

```
Request URI:
POST https://<connection-server>/vmrest/coses
Accept: application/json
Content-Type: application/json
Connection: keep-alive 
Request Body:
{
    "FaxRestrictionObjectId":"3da15ac5-e56f-4fac-b631-9f08826e1472",
    "OutcallRestrictionObjectId":"3da15ac5-e56f-4fac-b631-9f08826e1472",
    "XferRestrictionObjectId":"3da15ac5-e56f-4fac-b631-9f08826e1472"
}
The following is the response from the above *POST* request and the actual response will depend upon the information given by you:
<pre>
Response Code: 201
```

### Updating the Class
                           	 of Services

Example 1: The following is an example of the PUT request that
                                    			 allows you to update the display name of the class of services:

```
PUT https://<connection-server>/vmrest/coses/<cosobjectid>
Request Body:
<Cos>
    <DisplayName>Texoma_123</DisplayName>
</Cos>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To update display name of COS, do the following:

```
Request URI:
PUT https://<connection-server>/vmrest/coses/<cosobjectid>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "DisplayName": "Texoma_123"
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

Example 2: The following is an example of the PUT request that
                                    			 allows you to update the other fields of the class of services:

```
PUT https://<connection-server>/vmrest/coses/<cosobjectid>
Request Body:
<Cos>
    <MaxGreetingLength>45</MaxGreetingLength>
    <MaxMsgLength>500</MaxMsgLength>
    <MaxNameLength>50</MaxNameLength>
    <MaxPrivateDlists>30</MaxPrivateDlists>
</Cos>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

```
Request URI:
PUT https://<connection-server>/vmrest/coses/<cosobjectid>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{ 
    "MaxGreetingLength": "45", 
    "MaxMsgLength":"500", 
    "MaxNameLength":"50", 
    "MaxPrivateDlists":"30"
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Deleting the Class
                           	 of Services

The following is an example of
                                 		  the DELETE request that deletes a specific class of services where you need to
                                 		  mention the class of service object ID:

```
DELETE https://<connection-server>/vmrest/coses/<cosobjectid>
```

The following is the response from the above *DELETE* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To delete class of services, do the following:

```
Request URI:
DELETE https://<connection-server>/vmrest/coses/<cosobjectid>
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *DELETE* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Explanation of
                           	 Data Fields

The following chart lists all of the data fields:

Future feature, 3rd-party fax is not supported in Cisco
                                                						Unity Connection. Possible values are:

- false: Do not
                                                      						  allow access to fax mail

- true: Allow
                                                      						  access to fax mail

To allow subscribers to have their e-mail messages delivered
                                                						to a fax machine, both this column and "AccessTts" must be set to "true".
                                                						Default Value: false.

Possible values are:

- false: Cannot
                                                      						  have e-mail messages read over the phone

- true: Can have
                                                      						  e-mail messages read over the phone

To allow subscribers to have their e-mail messages delivered
                                                						to a fax machine, both this column and "AccessFaxMail" must be set to '"true".
                                                						Default Value: false.

Possible values are:

- false: Cannot
                                                      						  change call holding settings via Cisco Unity Assistant

- true: Can change
                                                      						  call holding settings via Cisco Unity Assistant

Default Value: false.

Possible values are:

- false: Cannot
                                                      						  change call screening settings via Cisco Unity Assistant

- true: Can change
                                                      						  call screening settings via Cisco Unity Assistant

Default Value: false.

Possible values are:

- false: Cannot
                                                      						  record their name

- true: Can record
                                                      						  their name

Default Value: true.

Possible values are:

- false: Cannot
                                                      						  choose whether or not to be listed in phone directory

- true: Can choose
                                                      						  whether or not to be listed in phone directory

Default value is: true.

The range can vary from 1 to 1200. Default Value: 90.

The range can vary from 1 to 3600. Default Value: 300

The range can vary from 1 to 100. Default Value: 30

The range can vary from 1 to 99.

true='deletion' moves messages to the DeletedItems folder,
                                                						where it ages until it evaporates. false='deletion' physically deletes the
                                                						message. When this column is set to "1," a subscriber can:

- Use the phone
                                                      						  and the Cisco Unity Connection Inbox (as applicable) to permanently delete
                                                      						  messages stored in their Deleted Items folder.

- Use the phone
                                                      						  and the Cisco Unity Connection Inbox to listen to, reply to, or forward
                                                      						  messages in their Deleted Items folder, or to restore them to the Inbox.

Possible values are:

- false: Deleted
                                                      						  messages are not moved to a Deleted Items folder, rather they are permanently
                                                      						  deleted.

- true: Deleted
                                                      						  messages are moved to a Deleted Items folder.

Default Value: true.

Possible values are:

- false: Cannot
                                                      						  use Cisco Unity Assistant

- true: Can use
                                                      						  Cisco Unity Assistant

Default Value: true.

Possible values are:

- false: COS can
                                                      						  be deleted

- true: COS cannot
                                                      						  be deleted

Default Value: false.

Call termination warning only works with the Unified
                                                						Communications Manager integration. Possible values are:

- 0: Record
                                                      						  termination warning disabled

- 1-30000: The
                                                      						  number of milliseconds from the end of the maximum recording time when the
                                                      						  record termination warning tone is played.

Default Value: 0.

Possible values are:

- false: Cannot
                                                      						  send messages to system distribution lists

- true: Can send
                                                      						  messages to system distribution lists

Default Value: true.

Possible values are:

- false: Regular
                                                      						  security

- true: Enhanced
                                                      						  phone security (RSA two-factor security)

Default Value: false.

Possible values are:

- false: Cannot
                                                      						  use Cisco Unity Connection Inbox

- true: Can use
                                                      						  Cisco Unity Connection Inbox

Default Value: false.

Possible values are:

- false: Cannot
                                                      						  "live reply" to another subscriber

- true: Can "live
                                                      						  reply" to another subscriber after listening to message from another subscriber

Default Value: false.

Possible values are:

- 3: CRUD access -
                                                      						  subscriber can view administrator-defined alternate extensions and manage
                                                      						  (create, modify, and delete) their own subscriber-defined alternate extensions

- 2: CUD access -
                                                      						  subscriber can manage (create, modify, and delete) their own subscriber-defined
                                                      						  alternate extensions.

- 1: Read access -
                                                      						  subscriber can view administrator-defined alternate extensions.

- 0: No access -
                                                      						  subscriber cannot view or manage alternate extensions.

Default Value: 0.

Possible values are:

- false: Cannot
                                                      						  access to Personal Call Routing rules

- true: Can access
                                                      						  to Personal Call Routing rules

Default Value: false.

The range of this field can vary from 0 to 99999. Default
                                                						Value: 0.

Possible values are:

- false: Cannot
                                                      						  send broadcast messages.

- true: Can send
                                                      						  broadcast messages.

Default Value: false.

Possible values are:

- false: Cannot
                                                      						  update broadcast messages.

- true: Can update
                                                      						  broadcast messages.

Default Value: false.

Possible values are:

- false: Cannot
                                                      						  use the voice driven inbox conversation

- true: Can use
                                                      						  the voice driven inbox conversation

Default Value: false.

Possible values are:

- false: Cannot
                                                      						  fetch message body of non-private messages.

- true: Using
                                                      						  IMAP, subscriber can fetch message body of non-private messages.

Default Value: true.

Possible values are:

- false: Cannot
                                                      						  fetch message body of private messages.

- true: Using
                                                      						  IMAP, subscriber can fetch message body of private messages.

Default Value: false.

Possible values are:

- false: Cannot
                                                      						  access voice mail via IMAP

- true: Can access
                                                      						  voice mail via IMAP

Default Value: false.

Possible values are:

- false: Cannot
                                                      						  access voice mail using unified client

- true: Can access
                                                      						  voice mail using unified client

Default Value: true.

Possible values are:

- false: Can
                                                      						  modify this COS.

- true: Cannot
                                                      						  modify this COS.

Default Value: false.

Possible values are:

- false: The
                                                      						  Subscriber cannot access advanced user features.

- true: The
                                                      						  Subscriber can access advanced user features.

Default Value: false.

Possible values are: 1: Always mark secure 2: Never mark
                                                						secure 3: Ask 4: Set private messages secure Default Value: 4.

Possible values are:

- false: User
                                                      						  cannot "Use Live Reply to Unidentified Callers"

- true: User can
                                                      						  "Use Live Reply to Unidentified Callers"after listening to message."

Default Value: false.

Possible values are:

- false: Do not
                                                      						  use transcription service (speech view).

- true: Use speech
                                                      						  view transcription service.

Default Value: false.

Possible values are:

- false: Cannot
                                                      						  have automatic alternate extension.

- true: Can have
                                                      						  automatic alternate extension.

Default Value: false.

Possible values are:

- 0: Do not
                                                      						  transcribe secure messages

- 1: Allow
                                                      						  transcriptions of secure messages

- 2: Allow
                                                      						  transcriptions and notifications of secure messages

Default Value: 0.

Possible values are:

- 0: No
                                                      						  restrictions on message playback

- 1: Allow
                                                      						  playback on computer speakers only

- 2: Allow
                                                      						  playback on phone only

Default Value: 0.

Possible values are:

- 1: Use speech
                                                      						  view standard transcription service.

- 2: Use speech
                                                      						  view pro transcription service.

Default Value: 1.

Possible Values:

- true : allow
                                                      						  Video messaging

- false: Do not
                                                      						  allow video messaging

Default value: false.

Possible Values:

- false: The
                                                      						  Subscriber cannot access advanced user features.

- true: The
                                                      						  Subscriber can access advanced user features.

Default: false

| Voicemail User COS | Contains settings that are applicable to end users. By default, this COS is associated with the default Voicemail User template |
|---|---|
| System | A COS that special default user accounts are members of. This COS is read-only and cannot be modified or deleted |

| GET https://<connection-server>/vmrest/coses |
|---|

| <Coses total="3">
  <Cos>
    <URI>/vmrest/coses/6e2c52a8-6bb6-40b0-b31e-27627293520c</URI>
    <ObjectId>6e2c52a8-6bb6-40b0-b31e-27627293520c</ObjectId>
    <DisplayName>Voice Mail User COS</DisplayName>
  </Cos>
  <Cos>
    <URI>/vmrest/coses/4af565ec-47d5-43be-9c3b-49d5ea995f63</URI>
    <ObjectId>4af565ec-47d5-43be-9c3b-49d5ea995f63</ObjectId>
    <DisplayName>System</DisplayName>
  </Cos>
  <Cos>
    <URI>/vmrest/coses/870f9a46-cc28-4d55-8fbd-e89cd02b9ff8</URI>
    <ObjectId>870f9a46-cc28-4d55-8fbd-e89cd02b9ff8</ObjectId>
    <DisplayName>Taxoma_COS_1</DisplayName>
  </Cos>
  </Coses> |
|---|

| Response Code: 200 |
|---|

| {
  "@total": "3",
  "Cos": [
{
    "URI": "/vmrest/coses/6e2c52a8-6bb6-40b0-b31e-27627293520c",
    "ObjectId": "6e2c52a8-6bb6-40b0-b31e-27627293520c",
    "DisplayName": "Voice Mail User COS"
},
{
    "URI": "/vmrest/coses/4af565ec-47d5-43be-9c3b-49d5ea995f63",
    "ObjectId": "4af565ec-47d5-43be-9c3b-49d5ea995f63",
    "DisplayName": "System"
},
{
"URI": "/vmrest/coses/870f9a46-cc28-4d55-8fbd-e89cd02b9ff8",
"ObjectId": "870f9a46-cc28-4d55-8fbd-e89cd02b9ff8",
"DisplayName": "Taxoma_COS_1"
}
]
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/coses/<cosobjectid> |
|---|

| <Cos>
    <URI>/vmrest/coses/77862e8e-42f3-4dac-811d-0be5291a9504</URI>
    <ObjectId>77862e8e-42f3-4dac-811d-0be5291a9504</ObjectId>
    <AccessFaxMail>false</AccessFaxMail>
    <AccessTts>false</AccessTts>
    <CallHoldAvailable>false</CallHoldAvailable>
    <CallScreenAvailable>false</CallScreenAvailable>
    <CanRecordName>true</CanRecordName>
    <FaxRestrictionObjectId>8045d752-6723-4062-9fc3-22090b85b5d7</FaxRestrictionObjectId>
    <ListInDirectoryStatus>true</ListInDirectoryStatus>
    <LocationObjectId>359e627b-c481-4428-8674-bc28f40e8d43</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/359e627b-c481-4428-8674-bc28f40e8d43</LocationURI>
    <MaxGreetingLength>90</MaxGreetingLength>
    <MaxMsgLength>300</MaxMsgLength>
    <MaxNameLength>30</MaxNameLength>
    <MaxPrivateDlists>25</MaxPrivateDlists>
    <MovetoDeleteFolder>true</MovetoDeleteFolder>
    <OutcallRestrictionObjectId>9c07accb-2187-4ca4-baf4-6ae0613f605a</OutcallRestrictionObjectId>
    <PersonalAdministrator>true</PersonalAdministrator>
    <DisplayName>HELLO_COS_1</DisplayName>
    <XferRestrictionObjectId>9c040521-fb05-4ba7-ba8f-d4f06f140b4c</XferRestrictionObjectId>
    <Undeletable>false</Undeletable>
    <WarnIntervalMsgEnd>0</WarnIntervalMsgEnd>
    <CanSendToPublicDl>true</CanSendToPublicDl>
    <EnableEnhancedSecurity>false</EnableEnhancedSecurity>
    <AccessVmi>false</AccessVmi>
    <AccessLiveReply>false</AccessLiveReply>
    <UaAlternateExtensionAccess>0</UaAlternateExtensionAccess>
    <AccessCallRoutingRules>false</AccessCallRoutingRules>
    <WarnMinMsgLength>0</WarnMinMsgLength>
    <SendBroadcastMessage>false</SendBroadcastMessage>
    <UpdateBroadcastMessage>false</UpdateBroadcastMessage>
    <AccessVui>false</AccessVui>
    <ImapCanFetchMessageBody>true</ImapCanFetchMessageBody>
    <ImapCanFetchPrivateMessageBody>false</ImapCanFetchPrivateMessageBody>
    <MaxMembersPVL>99</MaxMembersPVL>
    <AccessIMAP>false</AccessIMAP>
    <ReadOnly>false</ReadOnly>
    <AccessAdvancedUserFeatures>false</AccessAdvancedUserFeatures>
    <AccessAdvancedUser>false</AccessAdvancedUser>
    <AccessUnifiedClient>false</AccessUnifiedClient>
    <RequireSecureMessages>4</RequireSecureMessages>
    <AccessOutsideLiveReply>false</AccessOutsideLiveReply>
    <AccessSTT>false</AccessSTT>
    <EnableSTTSecureMessage>0</EnableSTTSecureMessage>
    <MessagePlaybackRestriction>0</MessagePlaybackRestriction>
    <SttType>1</SttType>
</Cos> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/coses/<cosobjectid>
Accept: application/json
Connection: keep-alive |
|---|

| {
    "URI": "/vmrest/coses/77862e8e-42f3-4dac-811d-0be5291a9504",
    "ObjectId": "77862e8e-42f3-4dac-811d-0be5291a9504",
    "AccessFaxMail": "false",
    "AccessTts": "false",
    "CallHoldAvailable": "false",
    "CallScreenAvailable": "false",
    "CanRecordName": "true",
    "FaxRestrictionObjectId": "8045d752-6723-4062-9fc3-22090b85b5d7",
    "ListInDirectoryStatus": "true",
    "LocationObjectId": "359e627b-c481-4428-8674-bc28f40e8d43",
    "LocationURI": "/vmrest/locations/connectionlocations/359e627b-c481-4428-8674-bc28f40e8d43",
    "MaxGreetingLength": "90",
    "MaxMsgLength": "300",
    "MaxNameLength": "30",
    "MaxPrivateDlists": "25",
    "MovetoDeleteFolder": "true",
    "OutcallRestrictionObjectId": "9c07accb-2187-4ca4-baf4-6ae0613f605a",
    "PersonalAdministrator": "true",
    "DisplayName": "HELLO_COS_1",
    "XferRestrictionObjectId": "9c040521-fb05-4ba7-ba8f-d4f06f140b4c",
    "Undeletable": "false",
    "WarnIntervalMsgEnd": "0",
    "CanSendToPublicDl": "true",
    "EnableEnhancedSecurity": "false",
    "AccessVmi": "false",
    "AccessLiveReply": "false",
    "UaAlternateExtensionAccess": "0",
    "AccessCallRoutingRules": "false",
    "WarnMinMsgLength": "0",
    "SendBroadcastMessage": "false",
    "UpdateBroadcastMessage": "false",
    "AccessVui": "false",
    "ImapCanFetchMessageBody": "true",
    "ImapCanFetchPrivateMessageBody": "false",
    "MaxMembersPVL": "99",
    "AccessIMAP": "false",
    "ReadOnly": "false",
    "AccessAdvancedUserFeatures": "false",
    "AccessAdvancedUser": "false",
    "AccessUnifiedClient": "false",
    "RequireSecureMessages": "4",
    "AccessOutsideLiveReply": "false",
    "AccessSTT": "false",
    "EnableSTTSecureMessage": "0",
    "MessagePlaybackRestriction": "0",
    "SttType": "1"
} |
|---|

| Response Code: 200 |
|---|

| POST https://<connection-server>/vmrest/coses
Request Body:
<Cos>
<DisplayName>Texoma_cos_1</DisplayName>
</Cos> |
|---|

| Response Code: 201 |
|---|

| Request URI:
POST https://<connection-server>/vmrest/coses
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "DisplayName":"Texoma_cos_1"
} |
|---|

| Response Code: 201 |
|---|

| POST https://<connection-server>/vmrest/coses
Request Body:
<cos>
    <DisplayName>Texoma_cos</DisplayName>
    <FaxRestrictionObjectId>3da15ac5-e56f-4fac-b631-9f08826e1472</FaxRestrictionObjectId>
    <OutcallRestrictionObjectId>3da15ac5-e56f-4fac-b631-9f08826e1472</OutcallRestrictionObjectId>
    <XferRestrictionObjectId>3da15ac5-e56f-4fac-b631-9f08826e1472</XferRestrictionObjectId>
</cos> |
|---|

| Response Code: 201 |
|---|

| Request URI:
POST https://<connection-server>/vmrest/coses
Accept: application/json
Content-Type: application/json
Connection: keep-alive 
Request Body:
{
    "FaxRestrictionObjectId":"3da15ac5-e56f-4fac-b631-9f08826e1472",
    "OutcallRestrictionObjectId":"3da15ac5-e56f-4fac-b631-9f08826e1472",
    "XferRestrictionObjectId":"3da15ac5-e56f-4fac-b631-9f08826e1472"
}
The following is the response from the above *POST* request and the actual response will depend upon the information given by you:
<pre>
Response Code: 201 |
|---|

| PUT https://<connection-server>/vmrest/coses/<cosobjectid>
Request Body:
<Cos>
    <DisplayName>Texoma_123</DisplayName>
</Cos> |
|---|

| Response Code: 204 |
|---|

| Request URI:
PUT https://<connection-server>/vmrest/coses/<cosobjectid>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "DisplayName": "Texoma_123"
} |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/coses/<cosobjectid>
Request Body:
<Cos>
    <MaxGreetingLength>45</MaxGreetingLength>
    <MaxMsgLength>500</MaxMsgLength>
    <MaxNameLength>50</MaxNameLength>
    <MaxPrivateDlists>30</MaxPrivateDlists>
</Cos> |
|---|

| Response Code: 204 |
|---|

| Request URI:
PUT https://<connection-server>/vmrest/coses/<cosobjectid>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{ 
    "MaxGreetingLength": "45", 
    "MaxMsgLength":"500", 
    "MaxNameLength":"50", 
    "MaxPrivateDlists":"30"
} |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/coses/<cosobjectid> |
|---|

| Response Code: 204 |
|---|

| Request URI:
DELETE https://<connection-server>/vmrest/coses/<cosobjectid>
Accept: application/json
Connection: keep-alive |
|---|

| Response Code: 204 |
|---|

| Parameters | Operations | Data Type | Comments |
|---|---|---|---|
| URI | Read Only | String | Specifies URI for class of service |
| ObjectId | Read Only | String(36) | Specifies object id of class of service |
| accessfaxmail | Read/Write | Boolean | A flag indicating whether a subscriber
                                             					 assigned this COS is allowed to manage their fax messages over the phone or
                                             					 from the Cisco Unity Connection Inbox. Future feature, 3rd-party fax is not supported in Cisco
                                                						Unity Connection. Possible values are: false: Do not
                                                      						  allow access to fax mail true: Allow
                                                      						  access to fax mail To allow subscribers to have their e-mail messages delivered
                                                						to a fax machine, both this column and "AccessTts" must be set to "true".
                                                						Default Value: false. |
| accesstts | Read/Write | Boolean | A flag indicating whether a subscriber
                                             					 assigned this COS can have to their e-mail messages read to them by an e-mail
                                             					 reader over the phone. Possible values are: false: Cannot
                                                      						  have e-mail messages read over the phone true: Can have
                                                      						  e-mail messages read over the phone To allow subscribers to have their e-mail messages delivered
                                                						to a fax machine, both this column and "AccessFaxMail" must be set to '"true".
                                                						Default Value: false. |
| callholdavailable | Read/Write | Boolean | A flag indicating whether the subscriber
                                             					 has the ability to change their own call holding options by using the Cisco
                                             					 Unity Connection Assistant. Call holding settings apply when calls are
                                             					 transferred from the automated attendant or a directory handler to subscriber
                                             					 phones. They do not apply when an outsider caller or another subscriber dials a
                                             					 subscriber extension directly. Possible values are: false: Cannot
                                                      						  change call holding settings via Cisco Unity Assistant true: Can change
                                                      						  call holding settings via Cisco Unity Assistant Default Value: false. |
| callscreenavailable | Read/Write | Boolean | A flag indicating whether the subscriber
                                             					 has the ability to change their own call screening options by using the Cisco
                                             					 Unity Assistant. Call screening settings apply when calls are transferred from
                                             					 the automated attendant or a directory handler to subscriber phones. They do
                                             					 not apply when an outsider caller or another subscriber dials a subscriber
                                             					 extension directly. Possible values are: false: Cannot
                                                      						  change call screening settings via Cisco Unity Assistant true: Can change
                                                      						  call screening settings via Cisco Unity Assistant Default Value: false. |
| canrecordname | Read/Write | Boolean | Used to prevent subscribers from recording
                                             					 their own names (for example, if an organization has all names and greetings
                                             					 recorded in one voice). Possible values are: false: Cannot
                                                      						  record their name true: Can record
                                                      						  their name Default Value: true. |
| faxrestrictionobjectid | Read/Write(36) | String | The unique identifier for the
                                             					 RestrictionTable objects that Cisco Unity Connection uses to limit phone
                                             					 numbers that the subscriber can enter in fax dialing settings. |
| listindirectorystatus | Read/Write | Boolean | A flag indicating whether subscribers can
                                             					 choose to be listed or not in the phone directory. The phone directory
                                             					 (directory assistance) is the audio listing that subscribers and unidentified
                                             					 callers use to reach subscribers and to leave messages. Possible values are: false: Cannot
                                                      						  choose whether or not to be listed in phone directory true: Can choose
                                                      						  whether or not to be listed in phone directory Default value is: true. |
| locationobjectid | Read Only | String | The unique identifier of the LocationVMS to
                                             					 which this COS belongs. |
| locationURI | Read Only | String | URI of the LocationVMS. |
| maxgreetinglength | Read/Write | Integer | The maximum recording length (in seconds)
                                             					 allowed to the subscriber for recording their greeting. The range can vary from 1 to 1200. Default Value: 90. |
| maxmsglength | Read/Write | Integer | The maximum recording length (in seconds)
                                             					 allowed to the subscriber for recording messages and conversations. The range can vary from 1 to 3600. Default Value: 300 |
| maxnamelength | Read/Write | Integer | The maximum recording length (in seconds)
                                             					 allowed to the subscriber for recording their voice name. The range can vary from 1 to 100. Default Value: 30 |
| maxprivatedlists | Read/Write | Integer | The maximum number of personal voice mail
                                             					 lists the subscriber is allowed to create. The range can vary from 1 to 99. Default Value: 25 |
| movetodeletefolder | Read/Write | Boolean | A flag indicating whether Cisco Unity
                                             					 Connection moves deleted messages for the subscriber to a Deleted Items folder
                                             					 or physically deletes the message. true='deletion' moves messages to the DeletedItems folder,
                                                						where it ages until it evaporates. false='deletion' physically deletes the
                                                						message. When this column is set to "1," a subscriber can: Use the phone
                                                      						  and the Cisco Unity Connection Inbox (as applicable) to permanently delete
                                                      						  messages stored in their Deleted Items folder. Use the phone
                                                      						  and the Cisco Unity Connection Inbox to listen to, reply to, or forward
                                                      						  messages in their Deleted Items folder, or to restore them to the Inbox. Possible values are: false: Deleted
                                                      						  messages are not moved to a Deleted Items folder, rather they are permanently
                                                      						  deleted. true: Deleted
                                                      						  messages are moved to a Deleted Items folder. Default Value: true. |
| outcallrestrictionobjectid | Read/Write(36) | String | The unique identifier of the Restriction
                                             					 Table object that Cisco Unity Connection uses to limit phone numbers that the
                                             					 subscriber can enter in message delivery settings. The restriction table also
                                             					 restricts the subscriber extensions that Cisco Unity Connection dials when the
                                             					 phone is selected as the recording and playback device for the Media Master. |
| personaladministrator | Read/Write | Boolean | A flag indicating whether Cisco Unity
                                             					 Connection allows a subscriber to use the Cisco Unity Assistant to personalize
                                             					 their Cisco Unity Connection setting -- including their recorded greetings and
                                             					 message delivery options -- or to set up message notification devices and
                                             					 create private lists. Possible values are: false: Cannot
                                                      						  use Cisco Unity Assistant true: Can use
                                                      						  Cisco Unity Assistant Default Value: true. |
| displayname | Read/Write(64) | String | The unique text name of this COS, e.g.
                                             					 "Default COS," "Basic Voice Mail." Used when displaying entries in the
                                             					 administrative console, e.g. Cisco Unity Connection Administration. DisplayName
                                             					 is a required when creating a new COS. DisplayName Length allowed is 64. |
| xferrestrictionobjectid | Read/Write(36) | String | The unique identifier of the
                                             					 RestrictionTable objects that Cisco Unity Connection uses to limit phone
                                             					 numbers that the subscriber can enter in call transfer settings. |
| undeletable | Read/Write | Boolean | A flag indicating whether this COS can be
                                             					 deleted via an administrative application such as Cisco Unity Connection
                                             					 Administration. It is used to prevent deletion of factory defaults. Possible values are: false: COS can
                                                      						  be deleted true: COS cannot
                                                      						  be deleted Default Value: false. |
| warnintervalmsgend | Read/Write | Integer | This column works together with
                                             					 "WarnMinMsgLength" enabling the record termination warning feature. If the
                                             					 feature is enabled by the settings of these two columns, callers will hear a
                                             					 warning tone sound before the maximum message length is reached. Call termination warning only works with the Unified
                                                						Communications Manager integration. Possible values are: 0: Record
                                                      						  termination warning disabled 1-30000: The
                                                      						  number of milliseconds from the end of the maximum recording time when the
                                                      						  record termination warning tone is played. Default Value: 0. |
| cansendtopublicdl | Read/Write | Boolean | A flag indicating whether the subscriber
                                             					 can send messages to system (formerly called "public") distribution lists. Possible values are: false: Cannot
                                                      						  send messages to system distribution lists true: Can send
                                                      						  messages to system distribution lists Default Value: true. |
| enableenhancedsecurity | Read/Write | Boolean | A flag indicating whether the subscriber
                                             					 uses regular or enhanced phone security. Enhanced phone security adds RSA
                                             					 two-factor authentication to regular security. Possible values are: false: Regular
                                                      						  security true: Enhanced
                                                      						  phone security (RSA two-factor security) Default Value: false. |
| accessvmi | Read/Write | Boolean | A flag indicating whether a subscriber
                                             					 assigned this COS can use the Cisco Unity Connection Inbox to listen to,
                                             					 compose, reply to, forward, and delete voice messages. If the subscriber has
                                             					 "AccessFaxMail" set, they can also use it to manage their faxes. This is a
                                             					 licensed feature. Possible values are: false: Cannot
                                                      						  use Cisco Unity Connection Inbox true: Can use
                                                      						  Cisco Unity Connection Inbox Default Value: false. |
| accesslivereply | Read/Write | Boolean | A flag indicating whether a subscriber
                                             					 assigned this COS can after listening to a message from another subscriber
                                             					 press 4-4, and Cisco Unity Connection will call the subscriber who left the
                                             					 message. Generally referred to as "Live Reply." Possible values are: false: Cannot
                                                      						  "live reply" to another subscriber true: Can "live
                                                      						  reply" to another subscriber after listening to message from another subscriber Default Value: false. |
| uaalternateextensionaccess | Read/Write | Integer | The abilities a subscriber has to manage
                                             					 administer-defined alternate extensions assigned to the subscriber. Determines
                                             					 whether subscribers can view the administrator-defined alternate extensions,
                                             					 and whether subscribers can manage (add, modify, and delete) their own set of
                                             					 alternate extensions in the Cisco Unity Assistant. If enabled, subscribers can
                                             					 define up to 5 alternate extensions in addition to the 9 alternate extensions
                                             					 that an administrator can define for them. Possible values are: 3: CRUD access -
                                                      						  subscriber can view administrator-defined alternate extensions and manage
                                                      						  (create, modify, and delete) their own subscriber-defined alternate extensions 2: CUD access -
                                                      						  subscriber can manage (create, modify, and delete) their own subscriber-defined
                                                      						  alternate extensions. 1: Read access -
                                                      						  subscriber can view administrator-defined alternate extensions. 0: No access -
                                                      						  subscriber cannot view or manage alternate extensions. Default Value: 0. |
| accesscallroutingrules | Read/Write | Boolean | A flag indicating whether a subscriber
                                             					 assigned this COS can access personal call routing rules. Possible values are: false: Cannot
                                                      						  access to Personal Call Routing rules true: Can access
                                                      						  to Personal Call Routing rules Default Value: false. |
| warnminmsglength | Read/Write | Integer | The minimum length (in milliseconds) that
                                             					 the maximum recording time has to be before the record termination warning
                                             					 feature is active. When the record termination feature is active, Cisco Unity
                                             					 Connection plays a warning tone indicating to the caller that they are almost
                                             					 out of recording time. The range of this field can vary from 0 to 99999. Default
                                                						Value: 0. |
| sendbroadcastmessage | Read/Write | Boolean | A flag indicating whether the subscriber
                                             					 has the ability to send broadcast messages to all subscribers on the VMS. Possible values are: false: Cannot
                                                      						  send broadcast messages. true: Can send
                                                      						  broadcast messages. Default Value: false. |
| updatebroadcastmessage | Read/Write | Boolean | A flag indicating whether the subscriber
                                             					 has the ability to update broadcast messages that are active or will be active
                                             					 in the future. Possible values are: false: Cannot
                                                      						  update broadcast messages. true: Can update
                                                      						  broadcast messages. Default Value: false. |
| accessvui | Read/Write | Boolean | A flag indicating whether a subscriber
                                             					 assigned this COS can use the voice driven inbox conversation. Possible values are: false: Cannot
                                                      						  use the voice driven inbox conversation true: Can use
                                                      						  the voice driven inbox conversation Default Value: false. |
| imapcanfetchmessagebody | Read/Write | Boolean | A flag indicating whether the subscriber
                                             					 can fetch the body of a non-private message using IMAP. Possible values are: false: Cannot
                                                      						  fetch message body of non-private messages. true: Using
                                                      						  IMAP, subscriber can fetch message body of non-private messages. Default Value: true. |
| imapcanfetchprivatemessagebody | Read/Write | Boolean | A flag indicating whether the subscriber
                                             					 can fetch the body of a private message using IMAP. Possible values are: false: Cannot
                                                      						  fetch message body of private messages. true: Using
                                                      						  IMAP, subscriber can fetch message body of private messages. Default Value: false. |
| maxmemberspvl | Read/Write | Integer | The maximum number of members allowed in a
                                             					 personal voice mail list. Range 1-999. default value is 99 |
| accessimap | Read/Write | Boolean | A flag indicating whether a subscriber
                                             					 assigned this COS can access VM via an IMAP client. Possible values are: false: Cannot
                                                      						  access voice mail via IMAP true: Can access
                                                      						  voice mail via IMAP Default Value: false. |
| accessunifiedclient | Read/Write | Boolean | A flag indicating whether a subscriber can
                                             					 use the unified client. Possible values are: false: Cannot
                                                      						  access voice mail using unified client true: Can access
                                                      						  voice mail using unified client Default Value: true. |
| readonly | Read/Write | Boolean | A flag indicating that this COS is read
                                             					 only. It cannot be modified from the Connection Administration. Possible values are: false: Can
                                                      						  modify this COS. true: Cannot
                                                      						  modify this COS. Default Value: false. |
| accessadvanceduserfeatures | Read/Write | Boolean | A flag indicating whether or not the
                                             					 subscriber has access to advanced user features. Currently, there are two
                                             					 advanced user features: TTS and VUI. Possible values are: false: The
                                                      						  Subscriber cannot access advanced user features. true: The
                                                      						  Subscriber can access advanced user features. Default Value: false. |
| requiresecuremessages | Read/Write | Integer | Specifies when to mark message secure. Possible values are: 1: Always mark secure 2: Never mark
                                                						secure 3: Ask 4: Set private messages secure Default Value: 4. |
| accessoutsidelivereply | Read/Write | Boolean | A flag indicating whether a subscriber,
                                             					 assigned this COS, can after listening to a message from outside caller issue a
                                             					 command to call the outside caller. When a VUI or TUI command is issued, Cisco
                                             					 Unity Connection will call the outside caller who left the message. Generally
                                             					 referred to as "Return Call to Outside Caller." Possible values are: false: User
                                                      						  cannot "Use Live Reply to Unidentified Callers" true: User can
                                                      						  "Use Live Reply to Unidentified Callers"after listening to message." Default Value: false. |
| accessstt | Read/Write | Boolean | An integer value indicating whether a
                                             					 subscriber assigned this COS can have to their voice messages transcribed to
                                             					 text. Possible values are: false: Do not
                                                      						  use transcription service (speech view). true: Use speech
                                                      						  view transcription service. Default Value: false. |
| autoalternateextension | Read/Write | Boolean | A flag indicating whether a subscriber
                                             					 assigned this COS can have automatic alternate extension. Possible values are: false: Cannot
                                                      						  have automatic alternate extension. true: Can have
                                                      						  automatic alternate extension. Default Value: false. |
| enablesttsecuremessage | Read/Write | Integer | Controls transcriptions and notification of
                                             					 secure messages for Speech To Text transcription feature. Possible values are: 0: Do not
                                                      						  transcribe secure messages 1: Allow
                                                      						  transcriptions of secure messages 2: Allow
                                                      						  transcriptions and notifications of secure messages Default Value: 0. |
| messageplaybackrestriction | Read/Write | Integer | Playback restrictions for GUI clients.
                                             					 Allows restricting playback to phone only or computer only. Possible values are: 0: No
                                                      						  restrictions on message playback 1: Allow
                                                      						  playback on computer speakers only 2: Allow
                                                      						  playback on phone only Default Value: 0. |
| stttype | Read/Write | Integer | An integer value indicating whether a
                                             					 subscriber assigned standard or PRO COS for STT. Possible values are: 1: Use speech
                                                      						  view standard transcription service. 2: Use speech
                                                      						  view pro transcription service. Default Value: 1. |
| enablevideomessaging | Read/Write | Boolean | Allows video messaging for the users in
                                             					 this class of service. Possible Values: true : allow
                                                      						  Video messaging false: Do not
                                                      						  allow video messaging Default value: false. |
| accessadvanceduser | Read/Write | Boolean | Duplicate of AdvnacedUserFeatures for
                                             					 licensing code purposes. Possible Values: false: The
                                                      						  Subscriber cannot access advanced user features. true: The
                                                      						  Subscriber can access advanced user features. Default: false |