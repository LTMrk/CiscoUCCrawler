---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-for-end-user-b-cupi-api-for-end-user-b-cupi-api-846a52fb42
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API_for_End_User/b_CUPI_API_for_End_User/b_CUPI_API_for_End_User_chapter_01011.html
retrieved_at: 2026-08-21T08:05:03.783988+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

Updated: January 18, 2019

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- HTML Notification Devices

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- HTML Notification Devices

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- HTML Notification Devices

## About HTML Notification Devices (in Cisco Unity Connection 9.0(1) and Later)

Cisco Unity Connection Provisioning Interface (CUPI) API allows users to view list of Html Notification Devices, a specific
                           notification device or modify an existing HTML Notification Device.

## Listing HTML Notification Devices

The following is an example of the GET request that lists the HTML notification devices for a user:

```
GET https://<connection-server>/vmrest/user/notificationdevices/htmldevices
```

The following is an example of the response from the above GET request and the actual response will depend upon the information
                              given by you:

```
<HtmlDevices>
    <HtmlDevice>
      <URI>/vmrest/user/notificationdevices/htmldevices/f00be19d-656c-411b-aa6e-1d4fe0390a5a</URI>
      <Active>true</Active>
      <DeviceName>HTML</DeviceName>
      <DisableMobileNumberFromPCA>false</DisableMobileNumberFromPCA>
      <DisplayName>HTML_Missed_Call</DisplayName>
      <NotificationTemplateID>74bcb8a5-7506-4e13-bb4f-ebbdf74f3ff5</NotificationTemplateID>
      <ObjectId>f00be19d-656c-411b-aa6e-1d4fe0390a5a</ObjectId>
      <SmtpAddress>xyz@cisco.com</SmtpAddress>
      <Undeletable>true</Undeletable>
      <SubscriberObjectId>f70379df-f952-4868-9981-cff387b52abf</SubscriberObjectId>
      <DisableTemplateSelectionFromPCA>false</DisableTemplateSelectionFromPCA>
      <AllowVoiceMailAsAttachment>false</AllowVoiceMailAsAttachment>
      <MessageCountInSummary>10</MessageCountInSummary>
    </HtmlDevice>
      ----
   </HtmlDevices>
```

## Listing an HTML Notification Device for a User

The following is an example of the GET request that lists a particular html notification device for the end user represented
                              by <device-object-id>:

```
GET https://<connection-server>/vmrest/user/notificationdevices/htmldevices/<device-object-id>
```

The following is the response from the above GET request and the actual result will depend upon the information provided by
                              you:

```
<HtmlDevice>
    <URI>/vmrest/user/notificationdevices/htmldevices/a3b60dec-6a2d-433d-9fa4-9e2b784c8dc8</URI>
    <Active>true</Active>
    <DeviceName>HTML</DeviceName>
    <DisableMobileNumberFromPCA>false</DisableMobileNumberFromPCA>
    <DisplayName>HTML_Scheduled_Summary</DisplayName>
    <NotificationTemplateID>f2904a86-8619-434c-88d2-42627f2c6e5f</NotificationTemplateID>
    <ObjectId>a3b60dec-6a2d-433d-9fa4-9e2b784c8dc8</ObjectId>
    <SmtpAddress>xyz@cisco.com</SmtpAddress>
    <Undeletable>true</Undeletable>
    <SubscriberObjectId>f70379df-f952-4868-9981-cff387b52abf</SubscriberObjectId>
    <UserURI>/vmrest/user</UserURI>
    <DisableTemplateSelectionFromPCA>false</DisableTemplateSelectionFromPCA>
    <AllowVoiceMailAsAttachment>false</AllowVoiceMailAsAttachment>
    <MessageCountInSummary>10</MessageCountInSummary>
    <EventList/>
    <ScheduleSetObjectId>b924bde7-1bfa-4b1e-b224-af4a8eb7089e</ScheduleSetObjectId>
    <SendScheduledNotificationAt/>
  </HtmlDevice>
```

## Modifying an HTML Notification Device for User

This PUT request allows user to apply an HTML-based notification template with an HTML notification device. The user can perform
                              this action if the template selection rights are given by administrator. The following is an example of PUT request:

```
PUT https://<connection-server>/vmrest/user/notificationdevices/htmldevices/<device-object-id>
```

The input for the PUT request will be XML or JSON as per HtmlDevice schema. The output for this request returns the successful
                              response code.

```
<HtmlDevice>
   <NotificationTemplateID>103c4514-db6e-489b-bc08-e9e131b60099</NotificationTemplateID>
 </HtmlDevice>
```

## Configuring Schedule Notification

Cisco Unity Connection allows the user to receive schedule notification in 24 hours format (hh:mm). The time at which a user
                              wants to receive scheduled notifications can be listed/configured using <SendScheduledNotificationAt> tag. User can configure
                              multiple time-slots using comma in the separated values. The schedules mentioned in this tag would overwrite all the existing
                              schedules. In order to delete all existing schedules, provide an empty <SendScheduledNotificationAt> tag.

The following is an example of the PUT request that modifies the Schedule notification for the user as represented by <SendScheduledNotificationAt>:

```
PUT https://<connection-server>vmrest/user/<user-object-id>/notificationdevices/htmldevices/<device-object-id>
```

The following is the response of above PUT request.

```
Response Code: 204 OK
```

```
<HtmlDevice>
  <URI>/vmrest/user/a3ab2df0-f16c-405f-afdf-394495acf000/notificationdevices/htmldevices/856c8ce9-d7dd-4623-888b-8d14874061af</URI>
  <Active>True</Active>
  <DeviceName>HTML</DeviceName>
  <DisplayName>HTMLDevice1</DisplayName>
  <NotificationTemplateID>3be2bd9e-114b-4103-a724-4e6c908d7c86</NotificationTemplateID>
  <ObjectId>856c8ce9-d7dd-4623-888b-8d14874061af</ObjectId>
  <SubscriberObjectId>a3ab2df0-f16c-405f-afdf-394495acf000</SubscriberObjectId>
  <SendScheduledNotificationAt>10:15,23:00 </SendScheduledNotificationAt>
  <EventList>NewVoiceMail</EventList>
</HtmlDevice>
```

JSON Example

```
PUT vmrest/user/<user-object-id>/notificationdevices/htmldevices/<device-object-id>?jsonp=1
```

```
{
   "Active":"false",
   "DisplayName":"HTML",
   "NotificationTemplateID":"3be2bd9e-114b-4103-a724-4e6c908d7c86",
   "EventList":"NewMissedCall",
   "SendScheduledNotificationAt":"9:00"
}
```

```
Response Code: 204 OK
```

The following is an example of the PUT request that deletes all the existing schedules by representing the empty <SendScheduledNotificationAt>
                              tag:

```
<HtmlDevice>
  <Active>True</Active>
  <DisplayName>HTMLDevice1</DisplayName>
  <NotificationTemplateID>3be2bd9e-114b-4103-a724-4e6c908d7c86</NotificationTemplateID>
  <ObjectId>856c8ce9-d7dd-4623-888b-8d14874061af</ObjectId>
  <EventList>None</EventList>
  <SendScheduledNotificationAt></SendScheduledNotificationAt>
</HtmlDevice>
```

```
Response Code : 204 Ok
```

JSON Example

```
{
   "Active":"false",
   "DisplayName":"HTML",
   "NotificationTemplateID":"3be2bd9e-114b-4103-a724-4e6c908d7c86",
   "EventList":"NewMissedCall",
   "SendScheduledNotificationAt":""
}
```

```
Response Code : 204 Ok
```

## Explanation of Data Fields

The following chart lists all of the data fields available on HTML Notification Devices.

Field Name

Device Type

Writable?

Explanation

ObjectId

All

Read-only

ObjectId of the Device

Type

Base

Read-only

Active

All

Read/Write

Factory default=false. For newly-created, default=true

DeviceName

All

Read/Write

Friendly name for the Device type (not shown in CUCA or CPCA). Default="Other"

DisplayName

All

Friendly name for the Device like "Mobile Phone"

EventList

All

Read/Write

Comma-delimited list of Events that trigger Notification, Default=NewVoiceMail

InitialDelay

All

Read/Write

Time in minutes to wait after a Message is received before Notification is triggered. Default=0

RepeatInterval

All

Read/Write

Time in minutes to wait before re-notifying of messages. Default=0

RepeatNotify

All

Read/Write

Flags if Notification process should begin for each newly arrived message. Default=false

ScheduleSetObjectId

All

Read/Write

ObjectId of the ScheduleSet during which Notification may trigger. Default=AllHours

SendPcaLink

Base, SMTP

Read/Write

Flag to include a link to CPCA in the Notification message. Default=false

SmtpAddess

Base, SMTP

Read/Write

SMTP address to send the Notification message to

SubscriberObjectId

All

Read-only

ObjectId of the User

Undeletable

All

Read-only

Factory default=true. For newly-created, default=false

SendScheduledNotificationAt

HTML

Read/Write

Timeslot(s) at which user wants to receive scheduled notification

MessageCountInSummary

HTML

Read/Write

Specify maximum number of messages to be listed in summary notification mail

The EventList field is a comma-delimited list of Message types which could trigger Notification. It can contain any of the
                              following values.

Event Name

Description

None

No messages of any type or urgency

NewVoiceMail

All voicemail messages

NewUrgentVoiceMail

All urgent voicemail messages

NewMissedCall

Missed Call

You can not add any other event with None and NewMissedCal event.

| GET https://<connection-server>/vmrest/user/notificationdevices/htmldevices |
|---|

| <HtmlDevices>
    <HtmlDevice>
      <URI>/vmrest/user/notificationdevices/htmldevices/f00be19d-656c-411b-aa6e-1d4fe0390a5a</URI>
      <Active>true</Active>
      <DeviceName>HTML</DeviceName>
      <DisableMobileNumberFromPCA>false</DisableMobileNumberFromPCA>
      <DisplayName>HTML_Missed_Call</DisplayName>
      <NotificationTemplateID>74bcb8a5-7506-4e13-bb4f-ebbdf74f3ff5</NotificationTemplateID>
      <ObjectId>f00be19d-656c-411b-aa6e-1d4fe0390a5a</ObjectId>
      <SmtpAddress>xyz@cisco.com</SmtpAddress>
      <Undeletable>true</Undeletable>
      <SubscriberObjectId>f70379df-f952-4868-9981-cff387b52abf</SubscriberObjectId>
      <DisableTemplateSelectionFromPCA>false</DisableTemplateSelectionFromPCA>
      <AllowVoiceMailAsAttachment>false</AllowVoiceMailAsAttachment>
      <MessageCountInSummary>10</MessageCountInSummary>
    </HtmlDevice>
      ----
   </HtmlDevices> |
|---|

| GET https://<connection-server>/vmrest/user/notificationdevices/htmldevices/<device-object-id> |
|---|

| <HtmlDevice>
    <URI>/vmrest/user/notificationdevices/htmldevices/a3b60dec-6a2d-433d-9fa4-9e2b784c8dc8</URI>
    <Active>true</Active>
    <DeviceName>HTML</DeviceName>
    <DisableMobileNumberFromPCA>false</DisableMobileNumberFromPCA>
    <DisplayName>HTML_Scheduled_Summary</DisplayName>
    <NotificationTemplateID>f2904a86-8619-434c-88d2-42627f2c6e5f</NotificationTemplateID>
    <ObjectId>a3b60dec-6a2d-433d-9fa4-9e2b784c8dc8</ObjectId>
    <SmtpAddress>xyz@cisco.com</SmtpAddress>
    <Undeletable>true</Undeletable>
    <SubscriberObjectId>f70379df-f952-4868-9981-cff387b52abf</SubscriberObjectId>
    <UserURI>/vmrest/user</UserURI>
    <DisableTemplateSelectionFromPCA>false</DisableTemplateSelectionFromPCA>
    <AllowVoiceMailAsAttachment>false</AllowVoiceMailAsAttachment>
    <MessageCountInSummary>10</MessageCountInSummary>
    <EventList/>
    <ScheduleSetObjectId>b924bde7-1bfa-4b1e-b224-af4a8eb7089e</ScheduleSetObjectId>
    <SendScheduledNotificationAt/>
  </HtmlDevice> |
|---|

| PUT https://<connection-server>/vmrest/user/notificationdevices/htmldevices/<device-object-id> |
|---|

| <HtmlDevice>
   <NotificationTemplateID>103c4514-db6e-489b-bc08-e9e131b60099</NotificationTemplateID>
 </HtmlDevice> |
|---|

| PUT https://<connection-server>vmrest/user/<user-object-id>/notificationdevices/htmldevices/<device-object-id> |
|---|

| Response Code: 204 OK |
|---|

| <HtmlDevice>
  <URI>/vmrest/user/a3ab2df0-f16c-405f-afdf-394495acf000/notificationdevices/htmldevices/856c8ce9-d7dd-4623-888b-8d14874061af</URI>
  <Active>True</Active>
  <DeviceName>HTML</DeviceName>
  <DisplayName>HTMLDevice1</DisplayName>
  <NotificationTemplateID>3be2bd9e-114b-4103-a724-4e6c908d7c86</NotificationTemplateID>
  <ObjectId>856c8ce9-d7dd-4623-888b-8d14874061af</ObjectId>
  <SubscriberObjectId>a3ab2df0-f16c-405f-afdf-394495acf000</SubscriberObjectId>
  <SendScheduledNotificationAt>10:15,23:00 </SendScheduledNotificationAt>
  <EventList>NewVoiceMail</EventList>
</HtmlDevice> |
|---|

| PUT vmrest/user/<user-object-id>/notificationdevices/htmldevices/<device-object-id>?jsonp=1 |
|---|

| {
   "Active":"false",
   "DisplayName":"HTML",
   "NotificationTemplateID":"3be2bd9e-114b-4103-a724-4e6c908d7c86",
   "EventList":"NewMissedCall",
   "SendScheduledNotificationAt":"9:00"
} |
|---|

| Response Code: 204 OK |
|---|

| <HtmlDevice>
  <Active>True</Active>
  <DisplayName>HTMLDevice1</DisplayName>
  <NotificationTemplateID>3be2bd9e-114b-4103-a724-4e6c908d7c86</NotificationTemplateID>
  <ObjectId>856c8ce9-d7dd-4623-888b-8d14874061af</ObjectId>
  <EventList>None</EventList>
  <SendScheduledNotificationAt></SendScheduledNotificationAt>
</HtmlDevice> |
|---|

| Response Code : 204 Ok |
|---|

| {
   "Active":"false",
   "DisplayName":"HTML",
   "NotificationTemplateID":"3be2bd9e-114b-4103-a724-4e6c908d7c86",
   "EventList":"NewMissedCall",
   "SendScheduledNotificationAt":""
} |
|---|

| Response Code : 204 Ok |
|---|

| Field Name | Device Type | Writable? | Explanation |
|---|---|---|---|
| ObjectId | All | Read-only | ObjectId of the Device |
| Type | Base | Read-only | Auto-set during Create. 1=Phone, 2=Pager, 4=SMTP, 8=HTML |
| Active | All | Read/Write | Factory default=false. For newly-created, default=true |
| DeviceName | All | Read/Write | Friendly name for the Device type (not shown in CUCA or CPCA). Default="Other" |
| DisplayName | All | Read/Write | Friendly name for the Device like "Mobile Phone" |
| EventList | All | Read/Write | Comma-delimited list of Events that trigger Notification, Default=NewVoiceMail |
| InitialDelay | All | Read/Write | Time in minutes to wait after a Message is received before Notification is triggered. Default=0 |
| RepeatInterval | All | Read/Write | Time in minutes to wait before re-notifying of messages. Default=0 |
| RepeatNotify | All | Read/Write | Flags if Notification process should begin for each newly arrived message. Default=false |
| ScheduleSetObjectId | All | Read/Write | ObjectId of the ScheduleSet during which Notification may trigger. Default=AllHours |
| SendPcaLink | Base, SMTP | Read/Write | Flag to include a link to CPCA in the Notification message. Default=false |
| SmtpAddess | Base, SMTP | Read/Write | SMTP address to send the Notification message to |
| SubscriberObjectId | All | Read-only | ObjectId of the User |
| Undeletable | All | Read-only | Factory default=true. For newly-created, default=false |
| SendScheduledNotificationAt | HTML | Read/Write | Timeslot(s) at which user wants to receive scheduled notification |
| MessageCountInSummary | HTML | Read/Write | Specify maximum number of messages to be listed in summary notification mail |

| Event Name | Description |
|---|---|
| None | No messages of any type or urgency |
| NewVoiceMail | All voicemail messages |
| NewUrgentVoiceMail | All urgent voicemail messages |
| NewMissedCall | Missed Call |

| Note | You can not add any other event with None and NewMissedCal event. |
|---|---|