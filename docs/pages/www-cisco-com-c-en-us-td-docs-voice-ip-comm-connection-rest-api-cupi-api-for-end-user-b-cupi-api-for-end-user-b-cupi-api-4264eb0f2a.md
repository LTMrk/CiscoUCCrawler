---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-for-end-user-b-cupi-api-for-end-user-b-cupi-api-4264eb0f2a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API_for_End_User/b_CUPI_API_for_End_User/b_CUPI_API_for_End_User_chapter_01111.html
retrieved_at: 2026-08-21T08:05:20.367263+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

Updated: January 24, 2019

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- Class Of Service

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- Class Of Service

- Cisco Unity Connection Provisioning Interface (CUPI) API -- Class Of Service

- Listing the Class of Service

- Explanation of Data Field

# Cisco Unity Connection Provisioning Interface (CUPI) API -- Class Of Service

## Listing the Class of Service

The user's class of service (COS) can be retrieved from the following URL:

```
GET https://<connection-server>/vmrest/user/cos
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                              by you:

```
<Cos>
  <URI>/vmrest/coses/803f97c3-a2fd-4edc-9277-10838f9765ec</URI>
  <ObjectId>803f97c3-a2fd-4edc-9277-10838f9765ec</ObjectId>
  <AccessFaxMail>false</AccessFaxMail>
  <AccessTts>false</AccessTts>
  <CallHoldAvailable>false</CallHoldAvailable>
  <CallScreenAvailable>false</CallScreenAvailable>
  <CanRecordName>true</CanRecordName>
  <FaxRestrictionObjectId>e29bada0-f4e2-47e3-863f-923f9d30bcbf</FaxRestrictionObjectId>
  <ListInDirectoryStatus>true</ListInDirectoryStatus>
  <LocationObjectId>94c234f0-62a0-492f-b918-2ba125f213f6</LocationObjectId>
  <LocationURI>/vmrest/locations/connectionlocations/94c234f0-62a0-492f-b918-2ba125f213f6</LocationURI>
  <MaxGreetingLength>90</MaxGreetingLength>
  <MaxMsgLength>300</MaxMsgLength>
  <MaxNameLength>30</MaxNameLength>
  <MaxPrivateDlists>25</MaxPrivateDlists>
  <MovetoDeleteFolder>true</MovetoDeleteFolder>
  <OutcallRestrictionObjectId>d4732d6a-2ab9-428b-a985-e63e4c026a47</OutcallRestrictionObjectId>
  <PersonalAdministrator>true</PersonalAdministrator>
  <DisplayName>Voice Mail User COS</DisplayName>
  <XferRestrictionObjectId>c6afc86a-13f4-4985-8d40-75a982d406e2</XferRestrictionObjectId>
  <Undeletable>true</Undeletable>
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

```
GET https://<connection-server>/vmrest/user/cos
Accept: application/json
Connection: keep-alive
```

```
{
  "URI": "/vmrest/coses/803f97c3-a2fd-4edc-9277-10838f9765ec",
  "ObjectId": "803f97c3-a2fd-4edc-9277-10838f9765ec", 
  "AccessFaxMail": "false",
  "AccessTts": "false",
  "CallHoldAvailable": "false",
  "CallScreenAvailable": "false",
  "CanRecordName": "true",
  "FaxRestrictionObjectId": "e29bada0-f4e2-47e3-863f-923f9d30bcbf",
  "ListInDirectoryStatus": "true",
  "LocationObjectId": "94c234f0-62a0-492f-b918-2ba125f213f6",
  "LocationURI": "/vmrest/locations/connectionlocations/94c234f0-62a0-492f-b918-2ba125f213f6",
  "MaxGreetingLength": "90",
  "MaxMsgLength": "300",
  "MaxNameLength": "30",
  "MaxPrivateDlists": "25",
  "MovetoDeleteFolder": "true",
  "OutcallRestrictionObjectId": "d4732d6a-2ab9-428b-a985-e63e4c026a47",
  "PersonalAdministrator": "true",
  "DisplayName": "Voice Mail User COS", 
  "XferRestrictionObjectId": "c6afc86a-13f4-4985-8d40-75a982d406e2",
  "Undeletable": "true",
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

## Explanation of Data Field

Parameter

Operation

Data Type

Comments

URI

Read Only

String

URI for Class of Service

OpjectId

Read Only

String

Object id of Class of service

accessfaxmail

Read/Write

Boolean

A flag indicating whether a subscriber assigned this COS is allowed to manage their fax messages over the phone or from the
                                          Cisco Unity Connection Inbox. Future feature, 3rd-party fax is not supported in Cisco Unity Connection. To allow subscribers
                                          to have their e-mail messages delivered to a fax machine, both this column and "AccessTts" must be set to "true."

Possible Values:

false : Do not allow access to fax mail

true : Allow access to fax mail

Default value is false

accesstts

Read/Write

Boolean

A flag indicating whether a subscriber assigned this COS can have to their e-mail messages read to them by an e-mail reader
                                          over the phone. To allow subscribers to have their e-mail messages delivered to a fax machine, both this column and "AccessFaxMail"
                                          must be set to '"true"

Possible Values:

false : Cannot have e-mail messages read over the phone

true : Can have e-mail messages read over the phone

Default value is false

callholdavailable

Read/Write

Boolean

A flag indicating whether the subscriber has the ability to change their own call holding options by using the Cisco Unity
                                          Connection Assistant. Call holding settings apply when calls are transferred from the automated attendant or a directory handler
                                          to subscriber phones. They do not apply when an outsider caller or another subscriber dials a subscriber extension directly.

Possible Values:

false : Cannot change call holding settings via Cisco Unity Assistant

true : Can change call holding settings via Cisco Unity Assistant

Default value is false

callscreenavailable

Read/Write

Boolean

A flag indicating whether the subscriber has the ability to change their own call screening options by using the Cisco Unity
                                          Assistant. Call screening settings apply when calls are transferred from the automated attendant or a directory handler to
                                          subscriber phones. They do not apply when an outsider caller or another subscriber dials a subscriber extension directly.

Possible Values:

false: Cannot change call screening settings via Cisco Unity Assistant

true: Can change call screening settings via Cisco Unity Assistant

Default value is false.

canrecordname

Read/Write

Boolean

Used to prevent subscribers from recording their own names (for example, if an organization has all names and greetings recorded
                                          in one voice).

Possible Values: false: Cannot record their name, true : Can record their name Default value: true

faxrestrictionobjectid

Read/Write

String

The unique identifier for the RestrictionTable object that Cisco Unity Connection uses to limit phone numbers that the subscriber
                                          can enter in fax dialing settings.

listindirectorystatus

Read/Write

Boolean

A flag indicating whether subscribers can choose to be listed or not in the phone directory. The phone directory (directory
                                          assistance) is the audio listing that subscribers and unidentified callers use to reach subscribers and to leave messages.

Possible Values:

false : Cannot choose whether or not to be listed in phone directory,

true : Can choose whether or not to be listed in phone directory

Default value is: true

locationobjectid

Read Only

String

The unique identifier of the LocationVMS to which this COS belongs.

locationURI

Read Only

String

maxgreetinglength

Read/Write

Integer

The maximum recording length (in seconds) allowed to the subscriber for recording their greeting.

Possible Values: Range:-1-1200 Default value is 90.

maxmsglength

Read/Write

Integer

The maximum recording length (in seconds) allowed to the subscriber for recording messages and conversations.

Possible Values: Range 1-3600 Default value is 300.

maxnamelength

Read/Write

Integer

The maximum recording length (in seconds) allowed to the subscriber for recording their voice name.

Possible Values: Range :- 1-100 Default value is 30.

MaxPrivateDlists

Read/Write

Integer

The maximum number of personal voice mail lists the subscriber is allowed to create.

Possible Values: Range :- 1-99 Default value is 25.

MovetoDeleteFolder

Read/Write

Boolean

A flag indicating whether Cisco Unity Connection moves deleted messages for the subscriber to a Deleted Items folder or physically
                                          deletes the message.

True='deletion' moves messages to the DeletedItems folder, where it ages until it evaporates. False='deletion' physically
                                          deletes the message When this column is set to "true," a subscriber can:

- Use the phone and the Cisco Unity Connection Inbox (as applicable) to permanently delete messages stored in their Deleted
                                             Items folder.

Use the phone and the Cisco Unity Connection Inbox to listen to, reply to, or forward messages in their Deleted Items folder,
                                                or to restore them to the Inbox.

OutcallRestrictionObjectId

Read/Write

String

PersonalAdministrator

Read/Write

Boolean

A flag indicating whether Cisco Unity Connection allows a subscriber to use the Cisco Unity Assistant to personalize their
                                          Cisco Unity Connection setting -- including their recorded greetings and message delivery options -- or to set up message
                                          notification devices and create private lists.

Possible Values: false : Cannot use Cisco Unity Assistant , true : Can use Cisco Unity Assistant Default value is true

DisplayName

Read/Write

String

The unique text name of this COS , e.g. "Default COS," "Basic Voice Mail." Used when displaying entries in the administrative
                                          console, e.g. Cisco Unity Connection Administration. DisplayName is a required when creating a new COS.

XferRestrictionObjectId

Read/Write

String

The unique identifier of the RestrictionTable object that Cisco Unity Connection uses to limit phone numbers that the subscriber
                                          can enter in call transfer settings.

Undeletable

Read/Write

Boolean

A flag indicating whether this COS can be deleted via an administrative application such as Cisco Unity Connection Administration.
                                          It is used to prevent deletion of factory defaults.It is true for default COS.

Possible Values: false : COS can be deleted , true : COS cannot be deleted Default value:false

WarnIntervalMsgEnd

Read/Write

Integer

This column works together with "WarnMinMsgLength" enabling the record termination warning feature. If the feature is enabled
                                          by the settings of these two columns, callers will hear a warning tone sound before the maximum message length is reached.
                                          Call termination warning only works with the Unified Communications Manager integration.

Possible Values:

0: Record termination warning disabled,

1-30000: The number of milliseconds from the end of the maximum recording time when the record termination warning tone is
                                                played

Default value is 0.

CanSendToPublicDl

Read/Write

Boolean

A flag indicating whether the subscriber can send messages to system (formerly called "public") distribution lists.

Possible Values: false: Cannot send messages to system distribution lists , true: Can send messages to system distribution
                                          lists Default value is true

EnableEnhancedSecurity

Read/Write

Boolean

A flag indicating whether the subscriber uses regular or enhanced phone security. Enhanced phone security adds RSA two-factor
                                          authentication to regular security.

Possible Values:

false : Regular security

- true : Enhanced phone security (RSA two-factor security)

default value is false

AccessVmi

Read/Write

Boolean

A flag indicating whether a subscriber assigned this COS can use the Cisco Unity Connection Inbox to listen to, compose, reply
                                          to, forward, and delete voice messages. If the subscriber has "AccessFaxMail" set, they can also use it to manage their faxes.
                                          This is a licensed feature.

Possible Values:

false : Cannot use Cisco Unity Connection Inbox

true : Can use Cisco Unity Connection Inbox

Default value is false

AccessLiveReply

Read/Write

Boolean

A flag indicating whether a subscriber assigned this COS can after listening to a message from another subscriber press 4-4,
                                          and Cisco Unity Connection will call the subscriber who left the message. Generally referred to as "Live Reply."

Possible Values:

false : Cannot "live reply" to another subscriber,

true : Can "live reply" to another subscriber after listening to message from another subscriber

Default value is false

UaAlternateExtensionAccess

Read/Write

Integer

The abilities a subscriber has to manage administer-defined alternate extensions assigned to the subscriber. Determines whether
                                          subscribers can view the administrator-defined alternate extensions, and whether subscribers can manage (add, modify, and
                                          delete) their own set of alternate extensions in the Cisco Unity Assistant. If enabled, subscribers can define up to 5 alternate
                                          extensions in addition to the 9 alternate extensions that an administrator can define for them.

Possible Values:

3 -CRUD access - subscriber can view administrator-defined alternate extensions and manage (create, modify, and delete) their
                                                own subscriber-defined alternate extensions.

2 - CUD access - subscriber can manage (create, modify, and delete) their own subscriber-defined alternate extensions.

0 - No access - subscriber cannot view or manage alternate extensions.

1 - Read access - subscriber can view administrator-defined alternate extensions.

Default Value is 0

AccessCallRoutingRules

Read/Write

Boolean

A flag indicating whether a subscriber assigned this COS can access personal call routing rules.

Default value is false Possible Values:

false : Cannot access to Personal Call Routing rules

true : Can access to Personal Call Routing rules

WarnMinMsgLength

Read/Write

Integer

The minimum length (in milliseconds) that the maximum recording time has to be before the record termination warning feature
                                          is active. When the record termination feature is active, Cisco Unity Connection plays a warning tone indicating to the caller
                                          that they are almost out of recording time.

Possible Values: Range 0-99999 Default value is 0.

SendBroadcastMessage

Read/Write

Boolean

A flag indicating whether the subscriber has the ability to send broadcast messages to all subscribers on the VMS.

Possible Values:

false : Cannot send broadcast messages.

true: Can send broadcast messages.

default value is false

UpdateBroadcastMessage

Read/Write

Boolean

A flag indicating whether the subscriber has the ability to update broadcast messages that are active or will be active in
                                          the future.

Possible Values:

false: Cannot update broadcast message

true: Can update broadcast message

Default value is false.

AccessVui

Read/Write

Boolean

A flag indicating whether a subscriber assigned this COS can use the voice driven inbox conversation.

Possible Values:

false: Cannot use the voice driven inbox conversation

true: Can use the voice driven inbox conversation

Default value is false.

ImapCanFetchMessageBody

Read/Write

Boolean

A flag indicating whether the subscriber can fetch the body of a non-private message using IMAP.

Possible Values:

false : Cannot fetch message body of non-private messages.

true : Using IMAP, subscriber can fetch message body of non-private messages

Default value is true

ImapCanFetchPrivateMessageBody

Read/Write

Boolean

A flag indicating whether the subscriber can fetch the body of a private message using IMAP.

Possible Values:

false : Cannot fetch message body of private messages.

true : Using IMAP, subscriber can fetch message body of private messages.

Default value is false

MaxMembersPVL

Read/Write

Integer

The maximum number of members allowed in a personal voice mail list.

Possible Values: Range 1-999 default value is 99

AccessIMAP

Read/Write

Boolean

A flag indicating whether a subscriber assigned this COS can access VM via an IMAP client.

Possible Values:

false : Cannot access voice mail via IMAP

true : Can access voice mail via IMAP

Default value is false

accessunifiedclient

Read/Write

Boolean

A flag indicating whether a subscriber can use the unified client.

Possible Values:

false : Cannot access voice mail using unified client

true : Can access voice mail using unified client

Default value is true.

ReadOnly

Read/Write

Boolean

A flag indicating that this COS is read only. It cannot be modified from the SA.

Possible Values: Default value is false

AccessAdvancedUserFeatures

Read/Write

Boolean

A flag indicating whether or not the subscriber has access to advanced user features. Currently, there are two advanced user
                                          features: TTS and VUI.

Possible Values:

false : The Subscriber can not access advanced user features.

true : The Subscriber can access advanced user features.

Default Value is false

RequireSecureMessages

Read/Write

Integer

Specifies when to mark message secure.

Possible Values:

1 Always mark secure

2 Never mark secure

3 Ask

4 Set private messages secure

Default value is 4

AccessOutsideLiveReply

Read/Write

Boolean

A flag indicating whether a subscriber, assigned this COS, can after listening to a message from outside caller issue a command
                                          to call the outside caller . When a VUI or TUI command is issued, Cisco Unity Connection will call the outside caller who
                                          left the message. Generally referred to as "Return Call to Outside Caller."

Possible Values:

false: User cannot "Use Live Reply to Unidentified Callers"

true- User can "Use Live Reply to Unidentified Callers"after listening to message."

Default value is false

AccessSTT

Read/Write

Boolean

An integer value indicating whether a subscriber assigned this COS can have to their voice messages transcribed to text.

Possible Values:

false : Do not use transcription service (speech view).

true : Use speech view transcription service.

Default value is false

autoalternateextension

Read/Write

Boolean

A flag indicating whether a subscriber assigned this COS can have automatic alternate extension.

Possible Values:

false : Cannot have automatic alternate extension.

true : Can have automatic alternate extension.

Default value is false

EnableSTTSecureMessage

Read/Write

Integer

Controls transcriptions and notification of secure messages for Speech To Text transcription feature.

Possible Values:

0 Do not transcribe secure messages

1 Allow transcriptions of secure messages

2 Allow transcriptions and notifications of secure messages

Default value is 0

MessagePlaybackRestriction

Read/Write

Integer

Playback restrictions for GUI clients. Allows restricting playback to phone only or computer only.

Possible Values:

0 No restrictions on message playback

1 Allow playback on computer speakers only

2 Allow playback on phone only

Default value is 0

SttType

Read/Write

Integer

An integer value indicating whether a subscriber assigned standard or PRO COS for STT.

Possible Values:

1: Use speech view standard transcription service.

2: Use speech view pro transcription service.

Default value is 1

enablevideomessaging

Read/Write

Boolean

Allows video messaging for the users in this class of service

Possible Values:

true: allow Video messaging

false: Do not allow video messaging

Default value is false

accessadvanceduser

Read/Write

Boolean

Duplicate of AdvancedUserFeatures for licensing code purposes.

Possible Values:

false: The Subscriber can not access advanced user features.

true: The Subscriber can access advanced user features.

Default:false

| GET https://<connection-server>/vmrest/user/cos |
|---|

| <Cos>
  <URI>/vmrest/coses/803f97c3-a2fd-4edc-9277-10838f9765ec</URI>
  <ObjectId>803f97c3-a2fd-4edc-9277-10838f9765ec</ObjectId>
  <AccessFaxMail>false</AccessFaxMail>
  <AccessTts>false</AccessTts>
  <CallHoldAvailable>false</CallHoldAvailable>
  <CallScreenAvailable>false</CallScreenAvailable>
  <CanRecordName>true</CanRecordName>
  <FaxRestrictionObjectId>e29bada0-f4e2-47e3-863f-923f9d30bcbf</FaxRestrictionObjectId>
  <ListInDirectoryStatus>true</ListInDirectoryStatus>
  <LocationObjectId>94c234f0-62a0-492f-b918-2ba125f213f6</LocationObjectId>
  <LocationURI>/vmrest/locations/connectionlocations/94c234f0-62a0-492f-b918-2ba125f213f6</LocationURI>
  <MaxGreetingLength>90</MaxGreetingLength>
  <MaxMsgLength>300</MaxMsgLength>
  <MaxNameLength>30</MaxNameLength>
  <MaxPrivateDlists>25</MaxPrivateDlists>
  <MovetoDeleteFolder>true</MovetoDeleteFolder>
  <OutcallRestrictionObjectId>d4732d6a-2ab9-428b-a985-e63e4c026a47</OutcallRestrictionObjectId>
  <PersonalAdministrator>true</PersonalAdministrator>
  <DisplayName>Voice Mail User COS</DisplayName>
  <XferRestrictionObjectId>c6afc86a-13f4-4985-8d40-75a982d406e2</XferRestrictionObjectId>
  <Undeletable>true</Undeletable>
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

| GET https://<connection-server>/vmrest/user/cos
Accept: application/json
Connection: keep-alive |
|---|

| {
  "URI": "/vmrest/coses/803f97c3-a2fd-4edc-9277-10838f9765ec",
  "ObjectId": "803f97c3-a2fd-4edc-9277-10838f9765ec", 
  "AccessFaxMail": "false",
  "AccessTts": "false",
  "CallHoldAvailable": "false",
  "CallScreenAvailable": "false",
  "CanRecordName": "true",
  "FaxRestrictionObjectId": "e29bada0-f4e2-47e3-863f-923f9d30bcbf",
  "ListInDirectoryStatus": "true",
  "LocationObjectId": "94c234f0-62a0-492f-b918-2ba125f213f6",
  "LocationURI": "/vmrest/locations/connectionlocations/94c234f0-62a0-492f-b918-2ba125f213f6",
  "MaxGreetingLength": "90",
  "MaxMsgLength": "300",
  "MaxNameLength": "30",
  "MaxPrivateDlists": "25",
  "MovetoDeleteFolder": "true",
  "OutcallRestrictionObjectId": "d4732d6a-2ab9-428b-a985-e63e4c026a47",
  "PersonalAdministrator": "true",
  "DisplayName": "Voice Mail User COS", 
  "XferRestrictionObjectId": "c6afc86a-13f4-4985-8d40-75a982d406e2",
  "Undeletable": "true",
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

| Parameter | Operation | Data Type | Comments |
|---|---|---|---|
| URI | Read Only | String | URI for Class of Service |
| OpjectId | Read Only | String | Object id of Class of service |
| accessfaxmail | Read/Write | Boolean | A flag indicating whether a subscriber assigned this COS is allowed to manage their fax messages over the phone or from the
                                          Cisco Unity Connection Inbox. Future feature, 3rd-party fax is not supported in Cisco Unity Connection. To allow subscribers
                                          to have their e-mail messages delivered to a fax machine, both this column and "AccessTts" must be set to "true." Possible Values: false : Do not allow access to fax mail true : Allow access to fax mail Default value is false |
| accesstts | Read/Write | Boolean | A flag indicating whether a subscriber assigned this COS can have to their e-mail messages read to them by an e-mail reader
                                          over the phone. To allow subscribers to have their e-mail messages delivered to a fax machine, both this column and "AccessFaxMail"
                                          must be set to '"true" Possible Values: false : Cannot have e-mail messages read over the phone true : Can have e-mail messages read over the phone Default value is false |
| callholdavailable | Read/Write | Boolean | A flag indicating whether the subscriber has the ability to change their own call holding options by using the Cisco Unity
                                          Connection Assistant. Call holding settings apply when calls are transferred from the automated attendant or a directory handler
                                          to subscriber phones. They do not apply when an outsider caller or another subscriber dials a subscriber extension directly. Possible Values: false : Cannot change call holding settings via Cisco Unity Assistant true : Can change call holding settings via Cisco Unity Assistant Default value is false |
| callscreenavailable | Read/Write | Boolean | A flag indicating whether the subscriber has the ability to change their own call screening options by using the Cisco Unity
                                          Assistant. Call screening settings apply when calls are transferred from the automated attendant or a directory handler to
                                          subscriber phones. They do not apply when an outsider caller or another subscriber dials a subscriber extension directly. Possible Values: false: Cannot change call screening settings via Cisco Unity Assistant true: Can change call screening settings via Cisco Unity Assistant Default value is false. |
| canrecordname | Read/Write | Boolean | Used to prevent subscribers from recording their own names (for example, if an organization has all names and greetings recorded
                                          in one voice). Possible Values: false: Cannot record their name, true : Can record their name Default value: true |
| faxrestrictionobjectid | Read/Write | String | The unique identifier for the RestrictionTable object that Cisco Unity Connection uses to limit phone numbers that the subscriber
                                          can enter in fax dialing settings. |
| listindirectorystatus | Read/Write | Boolean | A flag indicating whether subscribers can choose to be listed or not in the phone directory. The phone directory (directory
                                          assistance) is the audio listing that subscribers and unidentified callers use to reach subscribers and to leave messages. Possible Values: false : Cannot choose whether or not to be listed in phone directory, true : Can choose whether or not to be listed in phone directory Default value is: true |
| locationobjectid | Read Only | String | The unique identifier of the LocationVMS to which this COS belongs. |
| locationURI | Read Only | String | URI of the LocationVMS |
| maxgreetinglength | Read/Write | Integer | The maximum recording length (in seconds) allowed to the subscriber for recording their greeting. Possible Values: Range:-1-1200 Default value is 90. |
| maxmsglength | Read/Write | Integer | The maximum recording length (in seconds) allowed to the subscriber for recording messages and conversations. Possible Values: Range 1-3600 Default value is 300. |
| maxnamelength | Read/Write | Integer | The maximum recording length (in seconds) allowed to the subscriber for recording their voice name. Possible Values: Range :- 1-100 Default value is 30. |
| MaxPrivateDlists | Read/Write | Integer | The maximum number of personal voice mail lists the subscriber is allowed to create. Possible Values: Range :- 1-99 Default value is 25. |
| MovetoDeleteFolder | Read/Write | Boolean | A flag indicating whether Cisco Unity Connection moves deleted messages for the subscriber to a Deleted Items folder or physically
                                          deletes the message. True='deletion' moves messages to the DeletedItems folder, where it ages until it evaporates. False='deletion' physically
                                          deletes the message When this column is set to "true," a subscriber can: Use the phone and the Cisco Unity Connection Inbox (as applicable) to permanently delete messages stored in their Deleted
                                             Items folder. Use the phone and the Cisco Unity Connection Inbox to listen to, reply to, or forward messages in their Deleted Items folder,
                                                or to restore them to the Inbox. Default value is true |
| OutcallRestrictionObjectId | Read/Write | String | The unique identifier of the RestrictionTable object that Cisco Unity Connection uses to limit phone numbers that the subscriber
                                       can enter in message delivery settings. The restriction table also restricts the subscriber extensions that Cisco Unity Connection
                                       dials when the phone is selected as the recording and playback device for the Media Master. |
| PersonalAdministrator | Read/Write | Boolean | A flag indicating whether Cisco Unity Connection allows a subscriber to use the Cisco Unity Assistant to personalize their
                                          Cisco Unity Connection setting -- including their recorded greetings and message delivery options -- or to set up message
                                          notification devices and create private lists. Possible Values: false : Cannot use Cisco Unity Assistant , true : Can use Cisco Unity Assistant Default value is true |
| DisplayName | Read/Write | String | The unique text name of this COS , e.g. "Default COS," "Basic Voice Mail." Used when displaying entries in the administrative
                                          console, e.g. Cisco Unity Connection Administration. DisplayName is a required when creating a new COS. |
| XferRestrictionObjectId | Read/Write | String | The unique identifier of the RestrictionTable object that Cisco Unity Connection uses to limit phone numbers that the subscriber
                                          can enter in call transfer settings. |
| Undeletable | Read/Write | Boolean | A flag indicating whether this COS can be deleted via an administrative application such as Cisco Unity Connection Administration.
                                          It is used to prevent deletion of factory defaults.It is true for default COS. Possible Values: false : COS can be deleted , true : COS cannot be deleted Default value:false |
| WarnIntervalMsgEnd | Read/Write | Integer | This column works together with "WarnMinMsgLength" enabling the record termination warning feature. If the feature is enabled
                                          by the settings of these two columns, callers will hear a warning tone sound before the maximum message length is reached.
                                          Call termination warning only works with the Unified Communications Manager integration. Possible Values: 0: Record termination warning disabled, 1-30000: The number of milliseconds from the end of the maximum recording time when the record termination warning tone is
                                                played Default value is 0. |
| CanSendToPublicDl | Read/Write | Boolean | A flag indicating whether the subscriber can send messages to system (formerly called "public") distribution lists. Possible Values: false: Cannot send messages to system distribution lists , true: Can send messages to system distribution
                                          lists Default value is true |
| EnableEnhancedSecurity | Read/Write | Boolean | A flag indicating whether the subscriber uses regular or enhanced phone security. Enhanced phone security adds RSA two-factor
                                          authentication to regular security. Possible Values: false : Regular security true : Enhanced phone security (RSA two-factor security) default value is false |
| AccessVmi | Read/Write | Boolean | A flag indicating whether a subscriber assigned this COS can use the Cisco Unity Connection Inbox to listen to, compose, reply
                                          to, forward, and delete voice messages. If the subscriber has "AccessFaxMail" set, they can also use it to manage their faxes.
                                          This is a licensed feature. Possible Values: false : Cannot use Cisco Unity Connection Inbox true : Can use Cisco Unity Connection Inbox Default value is false |
| AccessLiveReply | Read/Write | Boolean | A flag indicating whether a subscriber assigned this COS can after listening to a message from another subscriber press 4-4,
                                          and Cisco Unity Connection will call the subscriber who left the message. Generally referred to as "Live Reply." Possible Values: false : Cannot "live reply" to another subscriber, true : Can "live reply" to another subscriber after listening to message from another subscriber Default value is false |
| UaAlternateExtensionAccess | Read/Write | Integer | The abilities a subscriber has to manage administer-defined alternate extensions assigned to the subscriber. Determines whether
                                          subscribers can view the administrator-defined alternate extensions, and whether subscribers can manage (add, modify, and
                                          delete) their own set of alternate extensions in the Cisco Unity Assistant. If enabled, subscribers can define up to 5 alternate
                                          extensions in addition to the 9 alternate extensions that an administrator can define for them. Possible Values: 3 -CRUD access - subscriber can view administrator-defined alternate extensions and manage (create, modify, and delete) their
                                                own subscriber-defined alternate extensions. 2 - CUD access - subscriber can manage (create, modify, and delete) their own subscriber-defined alternate extensions. 0 - No access - subscriber cannot view or manage alternate extensions. 1 - Read access - subscriber can view administrator-defined alternate extensions. Default Value is 0 |
| AccessCallRoutingRules | Read/Write | Boolean | A flag indicating whether a subscriber assigned this COS can access personal call routing rules. Default value is false Possible Values: false : Cannot access to Personal Call Routing rules true : Can access to Personal Call Routing rules |
| WarnMinMsgLength | Read/Write | Integer | The minimum length (in milliseconds) that the maximum recording time has to be before the record termination warning feature
                                          is active. When the record termination feature is active, Cisco Unity Connection plays a warning tone indicating to the caller
                                          that they are almost out of recording time. Possible Values: Range 0-99999 Default value is 0. |
| SendBroadcastMessage | Read/Write | Boolean | A flag indicating whether the subscriber has the ability to send broadcast messages to all subscribers on the VMS. Possible Values: false : Cannot send broadcast messages. true: Can send broadcast messages. default value is false |
| UpdateBroadcastMessage | Read/Write | Boolean | A flag indicating whether the subscriber has the ability to update broadcast messages that are active or will be active in
                                          the future. Possible Values: false: Cannot update broadcast message true: Can update broadcast message Default value is false. |
| AccessVui | Read/Write | Boolean | A flag indicating whether a subscriber assigned this COS can use the voice driven inbox conversation. Possible Values: false: Cannot use the voice driven inbox conversation true: Can use the voice driven inbox conversation Default value is false. |
| ImapCanFetchMessageBody | Read/Write | Boolean | A flag indicating whether the subscriber can fetch the body of a non-private message using IMAP. Possible Values: false : Cannot fetch message body of non-private messages. true : Using IMAP, subscriber can fetch message body of non-private messages Default value is true |
| ImapCanFetchPrivateMessageBody | Read/Write | Boolean | A flag indicating whether the subscriber can fetch the body of a private message using IMAP. Possible Values: false : Cannot fetch message body of private messages. true : Using IMAP, subscriber can fetch message body of private messages. Default value is false |
| MaxMembersPVL | Read/Write | Integer | The maximum number of members allowed in a personal voice mail list. Possible Values: Range 1-999 default value is 99 |
| AccessIMAP | Read/Write | Boolean | A flag indicating whether a subscriber assigned this COS can access VM via an IMAP client. Possible Values: false : Cannot access voice mail via IMAP true : Can access voice mail via IMAP Default value is false |
| accessunifiedclient | Read/Write | Boolean | A flag indicating whether a subscriber can use the unified client. Possible Values: false : Cannot access voice mail using unified client true : Can access voice mail using unified client Default value is true. |
| ReadOnly | Read/Write | Boolean | A flag indicating that this COS is read only. It cannot be modified from the SA. Possible Values: Default value is false |
| AccessAdvancedUserFeatures | Read/Write | Boolean | A flag indicating whether or not the subscriber has access to advanced user features. Currently, there are two advanced user
                                          features: TTS and VUI. Possible Values: false : The Subscriber can not access advanced user features. true : The Subscriber can access advanced user features. Default Value is false |
| RequireSecureMessages | Read/Write | Integer | Specifies when to mark message secure. Possible Values: 1 Always mark secure 2 Never mark secure 3 Ask 4 Set private messages secure Default value is 4 |
| AccessOutsideLiveReply | Read/Write | Boolean | A flag indicating whether a subscriber, assigned this COS, can after listening to a message from outside caller issue a command
                                          to call the outside caller . When a VUI or TUI command is issued, Cisco Unity Connection will call the outside caller who
                                          left the message. Generally referred to as "Return Call to Outside Caller." Possible Values: false: User cannot "Use Live Reply to Unidentified Callers" true- User can "Use Live Reply to Unidentified Callers"after listening to message." Default value is false |
| AccessSTT | Read/Write | Boolean | An integer value indicating whether a subscriber assigned this COS can have to their voice messages transcribed to text. Possible Values: false : Do not use transcription service (speech view). true : Use speech view transcription service. Default value is false |
| autoalternateextension | Read/Write | Boolean | A flag indicating whether a subscriber assigned this COS can have automatic alternate extension. Possible Values: false : Cannot have automatic alternate extension. true : Can have automatic alternate extension. Default value is false |
| EnableSTTSecureMessage | Read/Write | Integer | Controls transcriptions and notification of secure messages for Speech To Text transcription feature. Possible Values: 0 Do not transcribe secure messages 1 Allow transcriptions of secure messages 2 Allow transcriptions and notifications of secure messages Default value is 0 |
| MessagePlaybackRestriction | Read/Write | Integer | Playback restrictions for GUI clients. Allows restricting playback to phone only or computer only. Possible Values: 0 No restrictions on message playback 1 Allow playback on computer speakers only 2 Allow playback on phone only Default value is 0 |
| SttType | Read/Write | Integer | An integer value indicating whether a subscriber assigned standard or PRO COS for STT. Possible Values: 1: Use speech view standard transcription service. 2: Use speech view pro transcription service. Default value is 1 |
| enablevideomessaging | Read/Write | Boolean | Allows video messaging for the users in this class of service Possible Values: true: allow Video messaging false: Do not allow video messaging Default value is false |
| accessadvanceduser | Read/Write | Boolean | Duplicate of AdvancedUserFeatures for licensing code purposes. Possible Values: false: The Subscriber can not access advanced user features. true: The Subscriber can access advanced user features. Default:false |