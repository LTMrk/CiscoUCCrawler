---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-for-end-user-b-cupi-api-for-end-user-b-cupi-api-2f5eb64c84
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API_for_End_User/b_CUPI_API_for_End_User/b_CUPI_API_for_End_User_chapter_010100.html
retrieved_at: 2026-08-21T08:05:41.630798+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

Updated: January 24, 2019

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- Notification Devices API

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- Notification Devices API

# Cisco Unity Connection Provisioning Interface (CUPI) API -- Notification Devices API

## HTML Devices

Cisco Unity Connection Provisioning Interface (CUPI) API allows users to view list of Html Notification Devices, a specific
                           notification device or modify an existing HTML Notification Device. This API is available in in Cisco Unity Connection 9.0(1)
                           and later releases.

### Listing All HTML Devices

```
GET https://<connection-server>/vmrest/user/notificationdevices/htmldevices
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                 by you:

```
<HtmlDevices>
  <HtmlDevice>
  <URI>/vmrest/user/notificationdevices/htmldevices/8660c5af-b544-47cc-93eb-93f4923bc03b</URI>
  <Active>false</Active>
  <CallbackNumber>1234</CallbackNumber>
  <DeviceName>HTML</DeviceName>
  <DisableMobileNumberFromPCA>false</DisableMobileNumberFromPCA>
  <DisableTemplateSelectionFromPCA>false</DisableTemplateSelectionFromPCA>
  <DisplayName>HTML</DisplayName>
  <NotificationTemplateID> 75825d74-bf4f-4af3-bf84-6226389a8611</NotificationTemplateID>
  <ObjectId> 8660c5af-b544-47cc-93eb-93f4923bc03b</ObjectId>
  <PhoneNumber/>
  <SmtpAddress/>
  <Undeletable>true</Undeletable>
  <SubscriberObjectId> a880bb22-0df1-45aa-893e-895ebf2d3652 </SubscriberObjectId>
  </HtmlDevice>
</HtmlDevices>
<pre>
Response Code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/user/notificationdevices/htmldevices
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                 by you:

```
{
  "URI": "/vmrest/user/notificationdevices/htmldevices/8660c5af-b544-47cc-93eb-93f4923bc03b",
  "Active": "false",
  "CallbackNumber": "1234",
  "DeviceName": "HTML",
  "DisableMobileNumberFromPCA": "false",
  "DisableTemplateSelectionFromPCA": "false",
  "DisplayName": "HTML",
  "NotificationTemplateID": "75825d74-bf4f-4af3-bf84-6226389a8611",
  "ObjectId": "8660c5af-b544-47cc-93eb-93f4923bc03b",
  "PhoneNumber": [],
  "SmtpAddress": [],
  "Undeletable": "true",
  "SubscriberObjectId": "a880bb22-0df1-45aa-893e-895ebf2d3652"
}
```

```
Response Code: 200
```

### Listing Details of a Particular HTML Notification Device

The following is an example of the GET request that lists a particular html notification device for the end user represented
                                 by <deviceid>:

```
GET https://<connection-server>/vmrest/user/notificationdevices/htmldevices/<deviceid> 
The following is the response from the above *GET* request and the actual response will depend upon the information given by you:
<pre>
<HtmlDevice>
  <URI>/vmrest/user/notificationdevices/htmldevices/8660c5af-b544-47cc-93eb-93f4923bc03b</URI>
  <Active>false</Active>
  <CallbackNumber>1234</CallbackNumber>
  <DeviceName>HTML</DeviceName>
  <DisableMobileNumberFromPCA>false</DisableMobileNumberFromPCA>
  <DisableTemplateSelectionFromPCA>false</DisableTemplateSelectionFromPCA>
  <DisplayName>HTML</DisplayName>
  <NotificationTemplateID>75825d74-bf4f-4af3-bf84-6226389a8611</NotificationTemplateID>
  <ObjectId>8660c5af-b544-47cc-93eb-93f4923bc03b</ObjectId>
  <PhoneNumber />
  <SmtpAddress />
  <Undeletable>true</Undeletable>
  <SubscriberObjectId>a880bb22-0df1-45aa-893e-895ebf2d3652</SubscriberObjectId>
  <UserURI>/vmrest/user</UserURI>
  <EventList>NewVoiceMail</EventList>
  <ScheduleSetObjectId>1fb3df1c-6ff6-4876-996d-59052126f1fa    </ScheduleSetObjectId>
  <InitialDelay>0</InitialDelay>
  <RepeatInterval>0</RepeatInterval>
  <RepeatNotify>false</RepeatNotify>
</HtmlDevice>
```

```
Response Code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/user/notificationdevices/htmldevices/<device-id>
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                 by you:

```
{
  "URI": "/vmrest/user/notificationdevices/htmldevices/8660c5af-b544-47cc-93eb-93f4923bc03b",
  "Active": "false",
  "CallbackNumber": "1234",
  "DeviceName": "HTML",
  "DisableMobileNumberFromPCA": "false",
  "DisableTemplateSelectionFromPCA": "false",
  "DisplayName": "HTML",
  "NotificationTemplateID": "75825d74-bf4f-4af3-bf84-6226389a8611",
  "ObjectId": "8660c5af-b544-47cc-93eb-93f4923bc03b",
  "PhoneNumber": [],
  "SmtpAddress": [],
  "Undeletable": "true",
  "SubscriberObjectId": "a880bb22-0df1-45aa-893e-895ebf2d3652",
  "UserURI": "/vmrest/user",
  "EventList": "NewVoiceMail",
  "ScheduleSetObjectId": "1fb3df1c-6ff6-4876-996d-59052126f1fa",
  "InitialDelay": "0",
  "RepeatInterval": "0",
  "RepeatNotify": "false"
}
```

```
Response Code: 200
```

### SMTP Devices

Cisco Unity Connection Provisioning Interface (CUPI) API allows users to view list of SMTP Notification Devices, a specific
                              notification device or modify an existing SMTP Notification Device. This API is available in in Cisco Unity Connection 9.0(1)
                              and Later releases.

#### Listing All SMTP Device of User

```
GET:https://<connection-server>/vmrest/user/notificationdevices/smtpdevices
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                    by you:

```
<SmtpDevices>
  <SmtpDevice>
  <URI>/vmrest/user/notificationdevices/smtpdevices/eb4dbeae-ec87-417c-8cc0-d4ac3ab04942</URI>
  <SendCount>true</SendCount>
  <SmtpAddress>John@cisco.com</SmtpAddress>
  <StaticText/>
  <ObjectId>eb4dbeae-ec87-417c-8cc0-d4ac3ab04942</ObjectId>
  <Active>false</Active>
  <DeviceName>SMTP</DeviceName>
  <DisplayName>SMTP</DisplayName>
  <MaxBody>512</MaxBody>
  <MaxSubject>64</MaxSubject>
  <SubscriberObjectId>104b8800-554e-47cd-9fe7-ee16c79ce4d2</SubscriberObjectId>
  <SendCallerId>true</SendCallerId>
  <SendPcaLink>false</SendPcaLink>
  <Undeletable>true</Undeletable>
  <HeaderText>Texoma_Header</HeaderText>
  <FooterText>Texoma_Footer</FooterText>
  </SmtpDevice>
  <SmtpDevice>
  <URI>/vmrest/user/notificationdevices/smtpdevices/fdb94b56-5da8-4d67-99b3-1eeb44c9601b</URI>
  <PhoneNumber/>
  <SendCount>true</SendCount>
  <SmtpAddress/>
  <StaticText/>
  <ObjectId>fdb94b56-5da8-4d67-99b3-1eeb44c9601b</ObjectId>
  <Active>false</Active>
  <DeviceName>Other</DeviceName>
  <DisplayName>Test Smtp</DisplayName>
  <MaxBody>512</MaxBody>
  <MaxSubject>64</MaxSubject>
  <SubscriberObjectId>104b8800-554e-47cd-9fe7-ee16c79ce4d2</SubscriberObjectId>
  <SendCallerId>true</SendCallerId>
  <SendPcaLink>false</SendPcaLink>
  <Undeletable>false</Undeletable>
  <HeaderText>Test Header2</HeaderText>
  <FooterText>Test Footer2</FooterText>
  </SmtpDevice>
</SmtpDevices>
```

```
Response Code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/user/notificationdevices/smtpdevices
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                    by you:

```
{
  "URI": "/vmrest/user/notificationdevices/smtpdevices/eb4dbeae-ec87-417c-8cc0-d4ac3ab04942",
  "SendCount": "true",
  "SmtpAddress": "John@cisco.com",
  "StaticText": [],
  "ObjectId": "eb4dbeae-ec87-417c-8cc0-d4ac3ab04942",
  "Active": "false",
  "DeviceName": "SMTP",
  "DisplayName": "SMTP",
  "MaxBody": "512",
  "MaxSubject": "64",
  "SubscriberObjectId": "104b8800-554e-47cd-9fe7-ee16c79ce4d2",
  "SendCallerId": "true",
  "SendPcaLink": "false"
  "Undeletable": "true",
  "HeaderText": "Texoma_Header",
  "FooterText": "Texoma_Footer"
}
```

```
Response Code: 200
```

#### Listing Specific SMTP Device

```
GET:https://<connection-server>/vmrest/user/notificationdevices/smtpdevices/<smtpDeviceObjectId>
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                    by you:

```
<SmtpDevice>
  <URI>/vmrest/users/db6320e1-4931-4920-a9ce-8baacc87e3c4/notificationdevices/smtpdevices/84e72420-615e-4d94-b1df-f1317906cce3</URI>
  <PhoneNumber/>
  <SendCount>true</SendCount>
  <SmtpAddress>a</SmtpAddress>
  <StaticText/>
  <ObjectId>84e72420-615e-4d94-b1df-f1317906cce3</ObjectId>
  <Active>false</Active>
  <DeviceName>SMTP</DeviceName>
  <DisplayName>SMTP</DisplayName>
  <MaxBody>512</MaxBody>
  <MaxSubject>64</MaxSubject>
  <SubscriberObjectId>db6320e1-4931-4920-a9ce-8baacc87e3c4</SubscriberObjectId>
  <UserURI>/vmrest/users/db6320e1-4931-4920-a9ce-8baacc87e3c4</UserURI>
  <SendCallerId>true</SendCallerId>
  <SendPcaLink>false</SendPcaLink>
  <Undeletable>true</Undeletable>
  <HeaderText/>
  <FooterText/>
  <EventList>NewVoiceMail</EventList>
  <ScheduleSetObjectId>92421e6b-dffb-402b-bbd5-a126551627cf</ScheduleSetObjectId>
  <InitialDelay>0</InitialDelay>
  <VoiceMessage>false</VoiceMessage>
  <UrgentOnly>false</UrgentOnly>
  <RepeatInterval>0</RepeatInterval>
  <RepeatNotify>false</RepeatNotify>
  </SmtpDevice>
<pre>
<pre>
Response Code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/user/notificationdevices/smtpdevices/<smtpDeviceObjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                    by you:

```
{
  "URI":"/vmrest/users/db6320e1-4931-4920-a9ce-8baacc87e3c4/notificationdevices/smtpdevices/84e72420-615e-4d94-b1df-f1317906cce3",
  "SendCount":"true",
  "SmtpAddress":"abcd@cisco.com",
  "ObjectId:"84e72420-615e-4d94-b1df-f1317906cce3",
  "Active":"false",
  "DeviceName":"SMTP",
  "DisplayName:"SMTP",
  "MaxBody":"512",
  "MaxSubject":"64",
  "SubscriberObjectId":"db6320e1-4931-4920-a9ce-8baacc87e3c4",
  "UserURI":"/vmrest/users/db6320e1-4931-4920-a9ce-8baacc87e3c4",
  "SendCallerId":"true",
  "SendPcaLink":"false",
  "Undeletable":"true",
  "EventList":"NewVoiceMail",
  "ScheduleSetObjectId":"92421e6b-dffb-402b-bbd5-a126551627c",
  "InitialDelay":"0",
  "VoiceMessage":"false",
  "UrgentOnly":"false",
  "RepeatInterval":"12",
  "RepeatNotify":"false" 
}
<pre>
<pre> 
Response Code: 200
```

#### Update SMTP Device

```
PUT:https://<connection-server>/vmrest/user/notificationdevices/smtpdevices/<smtpDeviceObjectId>
```

```
<SmtpDevice>
  <SmtpAddress>John@cisco.com</SmtpAddress> 
  <HeaderText>Texoma_Header</HeaderText>
  <FooterText>Texoma_Footer</FooterText>
</SmtpDevice>
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 204
```

JSON Example

```
PUT https://<connection-server>/vmrest/user/notificationdevices/smtpdevices/<smtpDeviceObjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive 
{
  "SmtpAddress": "John@cisco.com",
  "HeaderText": "Texoma_Header",
  "FooterText": "Texoma_Footer"
}
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 204
```

#### Explanation of fields: SMTP Devices

Device Name

Data Type

Operation

Comment

Active

Boolean

Enable SMTP notification device. SMTP address is mandatory to enable it.

SmtpAddress

String

Read/Write

SMTP address to be notified.

DisplayName

String

Read/Write

Display name of the end user.

InitialDelay

Integer

Read/Write

Delay before the First Notification Attempt,

Possible values: 0-120 Default value: 0

RepeatNotify

Boolean

Read/Write

Repeat Notification if there are Still New Messages

Possible value:

false- Do Repeat Notification

true- Repeat Notification

Default: false

RepeatInteval

Integer

Read/Write

Notification Repeat Interval.

Possible values: 0-60 Default value: 0

EventList

String

Read/Write

To have multiple values selected we can have combination of below values separated by comma.

Values:

All messages: AllMessage

All message urgent only: AllUrgentMessage

All Voice messages: NewVoiceMail

All voice message urgent only: NewUrgentVoiceMail

Dispatch messages: DispatchMessage

Dispatch message urgent only: UrgentDispatchMessage

Fax messages: NewFax

Fax messages urgent only: NewUrgentFax

All voice messages and fax message urgent only: NewUrgentFax,NewVoiceMail

All voice message urgent only and fax message: NewUrgentFax,NewUrgentVoiceMail

Fax message and all voice message: NewFax,NewVoiceMail

Calendar Appointment: CalendarAppointment

Calendar meeting: CalendarMeeting

PhoneNumber

Integer

Read/Write

From which number SMTP notification is sent.

HeaderText

String

Read/Write

Message Header

StaticText

String

Read/Write

FooterText

String

Read/Write

Message footer

SubscriberObjectId

String

Read Only

The unique identifier of the Subscriber object to which this notification device belongs.

ScheduleSetObjectId

String

Read Only

The unique identifier of the Schedule. URI to get ObjectId:

https://<Connection-server>/vmrest/schedulesets

SendCallerId

Boolean

Read/Write

Include Message Information in Message Text.

Possible values:

false: Do not send callerId

true: send callerId

SendCount

Boolean

Read/Write

Include Message Count in Message Text

Possible Values:

false: Do not send subscriber message counts.

true: Send subscriber message counts.

SendPcaLink

Boolean

Read/Write

Include a Link to the Cisco Unity Connection Web Inbox in Message Text

DisplayName

String

Read Only

Name of notification device

DeviceName

String

Read Only

Device name of notification device which can’t be changed.

MaxBody

Integer

Read Only

MaxSubject

Integer

Read Only

The maximum number of characters allowed in the 'subject' of a notification message.

Possible value: 0-4096

| GET https://<connection-server>/vmrest/user/notificationdevices/htmldevices |
|---|

| <HtmlDevices>
  <HtmlDevice>
  <URI>/vmrest/user/notificationdevices/htmldevices/8660c5af-b544-47cc-93eb-93f4923bc03b</URI>
  <Active>false</Active>
  <CallbackNumber>1234</CallbackNumber>
  <DeviceName>HTML</DeviceName>
  <DisableMobileNumberFromPCA>false</DisableMobileNumberFromPCA>
  <DisableTemplateSelectionFromPCA>false</DisableTemplateSelectionFromPCA>
  <DisplayName>HTML</DisplayName>
  <NotificationTemplateID> 75825d74-bf4f-4af3-bf84-6226389a8611</NotificationTemplateID>
  <ObjectId> 8660c5af-b544-47cc-93eb-93f4923bc03b</ObjectId>
  <PhoneNumber/>
  <SmtpAddress/>
  <Undeletable>true</Undeletable>
  <SubscriberObjectId> a880bb22-0df1-45aa-893e-895ebf2d3652 </SubscriberObjectId>
  </HtmlDevice>
</HtmlDevices>
<pre>
Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/user/notificationdevices/htmldevices
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| {
  "URI": "/vmrest/user/notificationdevices/htmldevices/8660c5af-b544-47cc-93eb-93f4923bc03b",
  "Active": "false",
  "CallbackNumber": "1234",
  "DeviceName": "HTML",
  "DisableMobileNumberFromPCA": "false",
  "DisableTemplateSelectionFromPCA": "false",
  "DisplayName": "HTML",
  "NotificationTemplateID": "75825d74-bf4f-4af3-bf84-6226389a8611",
  "ObjectId": "8660c5af-b544-47cc-93eb-93f4923bc03b",
  "PhoneNumber": [],
  "SmtpAddress": [],
  "Undeletable": "true",
  "SubscriberObjectId": "a880bb22-0df1-45aa-893e-895ebf2d3652"
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/user/notificationdevices/htmldevices/<deviceid> 
The following is the response from the above *GET* request and the actual response will depend upon the information given by you:
<pre>
<HtmlDevice>
  <URI>/vmrest/user/notificationdevices/htmldevices/8660c5af-b544-47cc-93eb-93f4923bc03b</URI>
  <Active>false</Active>
  <CallbackNumber>1234</CallbackNumber>
  <DeviceName>HTML</DeviceName>
  <DisableMobileNumberFromPCA>false</DisableMobileNumberFromPCA>
  <DisableTemplateSelectionFromPCA>false</DisableTemplateSelectionFromPCA>
  <DisplayName>HTML</DisplayName>
  <NotificationTemplateID>75825d74-bf4f-4af3-bf84-6226389a8611</NotificationTemplateID>
  <ObjectId>8660c5af-b544-47cc-93eb-93f4923bc03b</ObjectId>
  <PhoneNumber />
  <SmtpAddress />
  <Undeletable>true</Undeletable>
  <SubscriberObjectId>a880bb22-0df1-45aa-893e-895ebf2d3652</SubscriberObjectId>
  <UserURI>/vmrest/user</UserURI>
  <EventList>NewVoiceMail</EventList>
  <ScheduleSetObjectId>1fb3df1c-6ff6-4876-996d-59052126f1fa    </ScheduleSetObjectId>
  <InitialDelay>0</InitialDelay>
  <RepeatInterval>0</RepeatInterval>
  <RepeatNotify>false</RepeatNotify>
</HtmlDevice> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/user/notificationdevices/htmldevices/<device-id>
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| {
  "URI": "/vmrest/user/notificationdevices/htmldevices/8660c5af-b544-47cc-93eb-93f4923bc03b",
  "Active": "false",
  "CallbackNumber": "1234",
  "DeviceName": "HTML",
  "DisableMobileNumberFromPCA": "false",
  "DisableTemplateSelectionFromPCA": "false",
  "DisplayName": "HTML",
  "NotificationTemplateID": "75825d74-bf4f-4af3-bf84-6226389a8611",
  "ObjectId": "8660c5af-b544-47cc-93eb-93f4923bc03b",
  "PhoneNumber": [],
  "SmtpAddress": [],
  "Undeletable": "true",
  "SubscriberObjectId": "a880bb22-0df1-45aa-893e-895ebf2d3652",
  "UserURI": "/vmrest/user",
  "EventList": "NewVoiceMail",
  "ScheduleSetObjectId": "1fb3df1c-6ff6-4876-996d-59052126f1fa",
  "InitialDelay": "0",
  "RepeatInterval": "0",
  "RepeatNotify": "false"
} |
|---|

| Response Code: 200 |
|---|

| GET:https://<connection-server>/vmrest/user/notificationdevices/smtpdevices |
|---|

| <SmtpDevices>
  <SmtpDevice>
  <URI>/vmrest/user/notificationdevices/smtpdevices/eb4dbeae-ec87-417c-8cc0-d4ac3ab04942</URI>
  <SendCount>true</SendCount>
  <SmtpAddress>John@cisco.com</SmtpAddress>
  <StaticText/>
  <ObjectId>eb4dbeae-ec87-417c-8cc0-d4ac3ab04942</ObjectId>
  <Active>false</Active>
  <DeviceName>SMTP</DeviceName>
  <DisplayName>SMTP</DisplayName>
  <MaxBody>512</MaxBody>
  <MaxSubject>64</MaxSubject>
  <SubscriberObjectId>104b8800-554e-47cd-9fe7-ee16c79ce4d2</SubscriberObjectId>
  <SendCallerId>true</SendCallerId>
  <SendPcaLink>false</SendPcaLink>
  <Undeletable>true</Undeletable>
  <HeaderText>Texoma_Header</HeaderText>
  <FooterText>Texoma_Footer</FooterText>
  </SmtpDevice>
  <SmtpDevice>
  <URI>/vmrest/user/notificationdevices/smtpdevices/fdb94b56-5da8-4d67-99b3-1eeb44c9601b</URI>
  <PhoneNumber/>
  <SendCount>true</SendCount>
  <SmtpAddress/>
  <StaticText/>
  <ObjectId>fdb94b56-5da8-4d67-99b3-1eeb44c9601b</ObjectId>
  <Active>false</Active>
  <DeviceName>Other</DeviceName>
  <DisplayName>Test Smtp</DisplayName>
  <MaxBody>512</MaxBody>
  <MaxSubject>64</MaxSubject>
  <SubscriberObjectId>104b8800-554e-47cd-9fe7-ee16c79ce4d2</SubscriberObjectId>
  <SendCallerId>true</SendCallerId>
  <SendPcaLink>false</SendPcaLink>
  <Undeletable>false</Undeletable>
  <HeaderText>Test Header2</HeaderText>
  <FooterText>Test Footer2</FooterText>
  </SmtpDevice>
</SmtpDevices> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/user/notificationdevices/smtpdevices
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| {
  "URI": "/vmrest/user/notificationdevices/smtpdevices/eb4dbeae-ec87-417c-8cc0-d4ac3ab04942",
  "SendCount": "true",
  "SmtpAddress": "John@cisco.com",
  "StaticText": [],
  "ObjectId": "eb4dbeae-ec87-417c-8cc0-d4ac3ab04942",
  "Active": "false",
  "DeviceName": "SMTP",
  "DisplayName": "SMTP",
  "MaxBody": "512",
  "MaxSubject": "64",
  "SubscriberObjectId": "104b8800-554e-47cd-9fe7-ee16c79ce4d2",
  "SendCallerId": "true",
  "SendPcaLink": "false"
  "Undeletable": "true",
  "HeaderText": "Texoma_Header",
  "FooterText": "Texoma_Footer"
} |
|---|

| Response Code: 200 |
|---|

| GET:https://<connection-server>/vmrest/user/notificationdevices/smtpdevices/<smtpDeviceObjectId> |
|---|

| <SmtpDevice>
  <URI>/vmrest/users/db6320e1-4931-4920-a9ce-8baacc87e3c4/notificationdevices/smtpdevices/84e72420-615e-4d94-b1df-f1317906cce3</URI>
  <PhoneNumber/>
  <SendCount>true</SendCount>
  <SmtpAddress>a</SmtpAddress>
  <StaticText/>
  <ObjectId>84e72420-615e-4d94-b1df-f1317906cce3</ObjectId>
  <Active>false</Active>
  <DeviceName>SMTP</DeviceName>
  <DisplayName>SMTP</DisplayName>
  <MaxBody>512</MaxBody>
  <MaxSubject>64</MaxSubject>
  <SubscriberObjectId>db6320e1-4931-4920-a9ce-8baacc87e3c4</SubscriberObjectId>
  <UserURI>/vmrest/users/db6320e1-4931-4920-a9ce-8baacc87e3c4</UserURI>
  <SendCallerId>true</SendCallerId>
  <SendPcaLink>false</SendPcaLink>
  <Undeletable>true</Undeletable>
  <HeaderText/>
  <FooterText/>
  <EventList>NewVoiceMail</EventList>
  <ScheduleSetObjectId>92421e6b-dffb-402b-bbd5-a126551627cf</ScheduleSetObjectId>
  <InitialDelay>0</InitialDelay>
  <VoiceMessage>false</VoiceMessage>
  <UrgentOnly>false</UrgentOnly>
  <RepeatInterval>0</RepeatInterval>
  <RepeatNotify>false</RepeatNotify>
  </SmtpDevice>
<pre>
<pre>
Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/user/notificationdevices/smtpdevices/<smtpDeviceObjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| {
  "URI":"/vmrest/users/db6320e1-4931-4920-a9ce-8baacc87e3c4/notificationdevices/smtpdevices/84e72420-615e-4d94-b1df-f1317906cce3",
  "SendCount":"true",
  "SmtpAddress":"abcd@cisco.com",
  "ObjectId:"84e72420-615e-4d94-b1df-f1317906cce3",
  "Active":"false",
  "DeviceName":"SMTP",
  "DisplayName:"SMTP",
  "MaxBody":"512",
  "MaxSubject":"64",
  "SubscriberObjectId":"db6320e1-4931-4920-a9ce-8baacc87e3c4",
  "UserURI":"/vmrest/users/db6320e1-4931-4920-a9ce-8baacc87e3c4",
  "SendCallerId":"true",
  "SendPcaLink":"false",
  "Undeletable":"true",
  "EventList":"NewVoiceMail",
  "ScheduleSetObjectId":"92421e6b-dffb-402b-bbd5-a126551627c",
  "InitialDelay":"0",
  "VoiceMessage":"false",
  "UrgentOnly":"false",
  "RepeatInterval":"12",
  "RepeatNotify":"false" 
}
<pre>
<pre> 
Response Code: 200 |
|---|

| PUT:https://<connection-server>/vmrest/user/notificationdevices/smtpdevices/<smtpDeviceObjectId> |
|---|

| <SmtpDevice>
  <SmtpAddress>John@cisco.com</SmtpAddress> 
  <HeaderText>Texoma_Header</HeaderText>
  <FooterText>Texoma_Footer</FooterText>
</SmtpDevice> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/user/notificationdevices/smtpdevices/<smtpDeviceObjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive 
{
  "SmtpAddress": "John@cisco.com",
  "HeaderText": "Texoma_Header",
  "FooterText": "Texoma_Footer"
} |
|---|

| Response Code: 204 |
|---|

| Device Name | Data Type | Operation | Comment |
|---|---|---|---|
| Active | Boolean | Read/Write | Enable SMTP notification device. SMTP address is mandatory to enable it. |
| SmtpAddress | String | Read/Write | SMTP address to be notified. |
| DisplayName | String | Read/Write | Display name of the end user. |
| InitialDelay | Integer | Read/Write | Delay before the First Notification Attempt, Possible values: 0-120 Default value: 0 |
| RepeatNotify | Boolean | Read/Write | Repeat Notification if there are Still New Messages Possible value: false- Do Repeat Notification true- Repeat Notification Default: false |
| RepeatInteval | Integer | Read/Write | Notification Repeat Interval. Possible values: 0-60 Default value: 0 |
| EventList | String | Read/Write | To have multiple values selected we can have combination of below values separated by comma. Values: All messages: AllMessage All message urgent only: AllUrgentMessage All Voice messages: NewVoiceMail All voice message urgent only: NewUrgentVoiceMail Dispatch messages: DispatchMessage Dispatch message urgent only: UrgentDispatchMessage Fax messages: NewFax Fax messages urgent only: NewUrgentFax All voice messages and fax message urgent only: NewUrgentFax,NewVoiceMail All voice message urgent only and fax message: NewUrgentFax,NewUrgentVoiceMail Fax message and all voice message: NewFax,NewVoiceMail Calendar Appointment: CalendarAppointment Calendar meeting: CalendarMeeting |
| PhoneNumber | Integer | Read/Write | From which number SMTP notification is sent. |
| HeaderText | String | Read/Write | Message Header |
| StaticText | String | Read/Write | Message text |
| FooterText | String | Read/Write | Message footer |
| SubscriberObjectId | String | Read Only | The unique identifier of the Subscriber object to which this notification device belongs. |
| ScheduleSetObjectId | String | Read Only | The unique identifier of the Schedule. URI to get ObjectId: https://<Connection-server>/vmrest/schedulesets |
| SendCallerId | Boolean | Read/Write | Include Message Information in Message Text. Possible values: false: Do not send callerId true: send callerId |
| SendCount | Boolean | Read/Write | Include Message Count in Message Text Possible Values: false: Do not send subscriber message counts. true: Send subscriber message counts. |
| SendPcaLink | Boolean | Read/Write | Include a Link to the Cisco Unity Connection Web Inbox in Message Text |
| DisplayName | String | Read Only | Name of notification device |
| DeviceName | String | Read Only | Device name of notification device which can’t be changed. |
| MaxBody | Integer | Read Only | The maximum number of characters allowed in the 'body' of a notification message. |
| MaxSubject | Integer | Read Only | The maximum number of characters allowed in the 'subject' of a notification message. Possible value: 0-4096 |