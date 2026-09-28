---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-user-notification-devices-api-html-17ae28d440
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_user-notification-devices-api.html
retrieved_at: 2026-08-17T03:48:13.617266+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Notification Devices
	 API

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Notification Devices
	 API

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- User Notification Devices
                     	 API

Links to Other API pages: Cisco_Unity_Connection_APIs

## User Notification
                        	 Devices API

The following URI can be used to
                              		  view the user template object ID:

```
GET https://<connection-server>/vmrest/users/<user-object>
```

From the above URI, get the notification devices object ID:

```
GET https://<connection-server>/vmrest/users/<user-objectid>/usernotificationdevices
```

### Pager

```
PUT:https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/pagerdevices/<pagerobjectid>
```

```
<PagerDevice>
  <RetriesOnBusy>4</RetriesOnBusy>
  <RetriesOnRna>4</RetriesOnRna>
  <RetriesToWait>10</RetriesToWait>
  <BusyRetryInterval>5</BusyRetryInterval>
  <RnaRetryInterval>15</RnaRetryInterval>
</PagerDevice>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

```
PUT https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/pagerdevices/<pagerobjectid>
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

```
{
  "FailDeviceObjectId":"c5ce04c1-e76e-4075-97f9-471ac49b7e85"
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

#### Listing Pager
                              	 Device

JSON Example

To view pager devices, do the following:

```
GET https://<connection-server>/vmrest/users/<users>/<user-objectid>/notificationdevices/pagerdevices/<pagerobjectId>
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
 URI":"/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/notificationdevices/pagerdevices/6215dce7-cf4a-469a-8722-035b6228ba3d"
 "TransmitForcedAuthorizationCode":"false"
 "AfterDialDigits":""
 "BusyRetryInterval":"5"
 "DialDelay":"1"
 "PhoneNumber":"123"
 "RetriesOnBusy":"10"
 "RetriesOnRna":"10"
 "RingsToWait":"10"
 "RnaRetryInterval":"1"
 "SendCount":"false"
 "WaitConnect":"false"
 "MediaSwitchObjectId":"7b092808-d815-4c0b-a10d-d02d3f5090b8"
 "PhoneSystemURI":"/vmrest/phonesystems/7b092808-d815-4c0b-a10d-d02d3f5090b8"
 "ObjectId":"6215dce7-cf4a-469a-8722-035b6228ba3d"
 "Active":"false"
 "DeviceName":"Pager"
 "DisplayName":"Pager"
 "MaxBody":"512"
 "MaxSubject":"64"
 "SubscriberObjectId":"9375d893-c8eb-437b-90bf-7de4b1d0c3e8"
 "UserURI":"/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8"
 "SendCallerId":"false"
 "Undeletable":"true"
 "SuccessRetryInterval":"1"
 "RetriesOnSuccess":"0"
 "EventList":"NewUrgentFaxUrgentDispatchMessage"
 "ScheduleSetObjectId":"1f360ab8-076e-4cb5-bfde-ef7d3805f037"InitialDelay":"12"
 "VoiceMessage":"false"
 "UrgentOnly":"false"
 "RepeatInterval":"1"
 "RepeatNotify":"true",
 "FailDeviceObjectId":"c5ce04c1-e76e-4075-97f9-471ac49b7e85"
}
```

```
Response Code: 200
```

#### Create Pager
                              	 Device

The mandatory
                                    		  parameters are: PhoneNumber, DisplayName, and MediaSwitchObjectId.

```
POST: https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/pagerdevices
```

```
<PagerDevice>
   <PhoneNumber>12334</PhoneNumber>
   <DisplayName>Newpager</DisplayName>
   <MediaSwitchObjectId>8adf6869-4afc-4455-9fd5-d05b68ca6630</MediaSwitchObjectId>
</PagerDevice>
```

The following is
                                    		  the response from the above *POST* request and the actual response will depend
                                    		  upon the information given by you:

```
Response Code: 201
```

JSON Example

```
POST https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/pagerdevices
Accept: application/json
Content-type:  application/json
Connection: keep-alive
```

```
{
  "DisplayName":"New Pager",
  "PhoneNumber":"1234",
  "MediaSwitchObjectId":"ae63574f-2aaf-4c28-8973-bfa8e3b1dd1c"
}
```

The following is the response from the above *POST* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 201
/vmrest/users/<user-objectid>/notificationdevices/pagerdevices/84e72420-615e-4d94-b1df-f1317906cce3
```

The phone system ID is mandatory to create pager device. URI to get ID
                                    		  for phone system:

```
https://<connection-server>/vmrest/phonesystems
```

### Phone
                           	 Devices

```
GET https://<connection-server>/vmrest/users/<user-objectid>
```

From above URI get notification devices URI:

```
https://<connection-server>/vmrest/users/<user-objectid>/usernotificationdevices
```

#### Listing Phone
                              	 Device

```
GET:https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/phonedevices/<phone_objectid>
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
Response code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/phonedevices/<phone_objectid>
Accept: application/json
Content-type:  application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 200
```

#### Create Phone
                              	 Device

The mandatory fields are
                                    		  DisplayName, PhoneNumber, and MediaSwitchObjectId.

```
POST https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/phonedevices
```

```
<PhoneDevice>
  <DisplayName>Work Phone1</DisplayName>
  <PhoneNumber>123</PhoneNumber>
  <MediaSwitchObjectId>ae63574f-2aaf-4c28-8973-bfa8e3b1dd1c</MediaSwitchObjectId>
</PhoneDevice>
```

The following is the response from the above *POST* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 201
```

JSON Example

```
POST https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/phonedevices
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

```
{
  "DisplayName":"Work Phone1",
  "PhoneNumber":"123",
  "MediaSwitchObjectId":"ae63574f-2aaf-4c28-8973-bfa8e3b1dd1c"
}
```

The following is the response from the above *POST* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 201
```

URI to get ID for phone system:

```
https://<connection-server>/vmrest/phonesystems
```

#### Update Phone
                              	 Device

```
PUT:https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/phonedevices/<phone_objectid>
<PhoneDevice>
  <RetriesOnBusy>10</RetriesOnBusy>
  <RetriesOnRna>10</RetriesOnRna>
  <RingsToWait>10</RingsToWait>
  <RnaRetryInterval>1</RnaRetryInterval>
</PhoneDevice>
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response code: 204
```

To activate notification device, the <PhoneNumber> parameter is
                                    		  mandatory. The <RepeatInterval> parameter is mandatory to enable repeat
                                    		  notify. The phone devices are of 3 types: Work phone, Home phone, and Mobile
                                    		  phone. You have to provide phone device object id to edit any of the 3 devices.

JSON Example

```
PUT https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/phonedevices/<phone_objectid>
Accept: application/json
Content-type:  application/json
Connection: keep-alive
```

```
{
  "FailDeviceObjectId":"c5ce04c1-e76e-4075-97f9-471ac49b7e85"
}
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response code: 204
```

#### Delete Phone
                              	 Device

```
DELETE https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/phonedevices/<phone_objectid>
```

The following is the response from the above *DELETE* request and the
                                    		  actual response will depend upon the information given by you:

```
Response code: 204
```

JSON Example

```
DELETE https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/phonedevices/<phone_objectid>
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

The following is the response from the above *DELETE* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### SMTP
                           	 Device

#### Listing SMTP
                              	 Device

```
GET:https://<Connection-server>/vmrest/user/notificationdevices/smtpdevices
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
Response code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/user/notificationdevices/smtpdevices
Accept: application/json
Content-type:  application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

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
   "SendPcaLink": "false",
   "Undeletable": "true",
   "HeaderText": "Texoma_Header",
   "FooterText": "Texoma_Footer"
}
```

```
Response Code: 200
```

#### Update SMTP
                              	 Device

```
GET:https://<Connection-server>/vmrest/user/notificationdevices/smtpdevices/<smtpDeviceObjectId>
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
Response code: 204
```

```
<SmtpDevice>
  <SmtpAddress>John@cisco.com</SmtpAddress>
  <HeaderText>Texoma_Header</HeaderText>
  <FooterText>Texoma_Footer</FooterText>
</SmtpDevice>
```

JSON Example

```
PUT https://<connection-server>/vmrest/user/notificationdevices/smtpdevices/<smtpDeviceObjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

```
{   
  "SmtpAddress": "John@cisco.com",
  "HeaderText": "Texoma_Header",
  "FooterText": "Texoma_Footer"
}
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response code: 204
```

### About HTML
                           	 Notification Devices (in Cisco Unity Connection 9.0(1) and Later)

Cisco Unity Connection Provisioning
                              		Interface (CUPI) API allows users to view list of Html Notification Devices, a
                              		specific notification device or modify an existing HTML Notification Device.

#### Listing HTML
                              	 Notification Devices

The following is an example of
                                    		  the GET request that lists the HTML notification devices for the users:

```
GET /vmrest/users/notificationdevices/htmldevices
```

The following is an example of the response from the above *GET*
                                    		  request and the actual response will depend upon the information given by you:

```
<HtmlDevices total="3">
  <HtmlDevice>
  <URI>/vmrest/users/5786019c-f962-4b86-8103-a01755b9993c/notificationdevices/htmldevices/d7044a91-b3b5-4e5a-9d08-eca2235660fd</URI>
  <Active>false</Active>
  <DeviceName>HTML</DeviceName>
  <DisableMobileNumberFromPCA>false</DisableMobileNumberFromPCA>
  <DisplayName>HTML_Missed_Call</DisplayName>
  <NotificationTemplateID>f37de0e3-c070-4d7e-bb98-5b8b1911ed27</NotificationTemplateID>
  <ObjectId>d7044a91-b3b5-4e5a-9d08-eca2235660fd</ObjectId>
  <Undeletable>true</Undeletable>
  <SubscriberObjectId>5786019c-f962-4b86-8103-a01755b9993c</SubscriberObjectId>
  <UserURI>/vmrest/users/5786019c-f962-4b86-8103-a01755b9993c</UserURI>
  <DisableTemplateSelectionFromPCA>false</DisableTemplateSelectionFromPCA>
  <AllowVoiceMailAsAttachment>false</AllowVoiceMailAsAttachment>
  <MessageCountInSummary>10</MessageCountInSummary>
  <EventList>NewMissedCall</EventList>
  <ScheduleSetObjectId>48993a7c-2732-4217-8abc-893604fa16b6</ScheduleSetObjectId>
  <SendScheduledNotificationAt/>
  </HtmlDevice>
 </HtmlDevices>
```

#### Listing an HTML
                              	 Notification Device for Users

The following is an example of
                                    		  the GET request that lists a particular html notification device for the end
                                    		  users represented by <deviceid>:

```
GET /vmrest/user/notificationdevices/htmldevices/<deviceid>
```

The following is the response from the above *GET* request and the
                                    		  actual result will depend upon the information has been provided by you:

```
<HtmlDevice>
   <URI>/vmrest/user/notificationdevices/htmldevices/8660c5af-b544-47cc-93eb-93f4923bc03b</URI>
   <Active>false</Active>
   <CallbackNumber>1234</CallbackNumber>
   <DeviceName>HTML</DeviceName>
   <DisableMobileNumberFromPCA>false</DisableMobileNumberFromPCA>
   <DisableTemplateSelectionFromPCA>false</DisableTemplateSelectionFromPCA>
   <DisplayName>HTML</DisplayName>
   <NotificationTemplateID>75825d74-bf4f-4af3-bf84-6226389a8611
   </NotificationTemplateID>
   <ObjectId>8660c5af-b544-47cc-93eb-93f4923bc03b</ObjectId>
   <PhoneNumber />
   <SmtpAddress />
   <Undeletable>true</Undeletable>
   <SubscriberObjectId>a880bb22-0df1-45aa-893e-895ebf2d3652
   </SubscriberObjectId>
   <UserURI>/vmrest/users</UserURI>
   <EventList>NewVoiceMail</EventList>
   <ScheduleSetObjectId>1fb3df1c-6ff6-4876-996d-59052126f1fa
   </ScheduleSetObjectId>
   <InitialDelay>0</InitialDelay>
   <RepeatInterval>0</RepeatInterval>
   <RepeatNotify>false</RepeatNotify>
  </HtmlDevice>
```

#### Modifying an HTML
                              	 Notification Device for Users

The following is an example of
                                    		  the PUT request that modifies the HTML notification device for the users as
                                    		  represented by <deviceid>:

```
PUT /vmrest/users/notificationdevices/htmldevices/<deviceid>
```

The input for the PUT request will be XML or JSON as per HtmlDevice
                                    		  schema. The output for this request returns the successful response code.

#### Modifying an HTML
                              	 Notification Device to Apply HTML Notification Template

The following is an example of
                                    		  the PUT request that modifies the HTML notification device as represented by
                                    		  <deviceid>:

```
PUT /vmrest/users/notificationdevices/htmldevices/<deviceobjectid>

 <HtmlDevice>
   <NotificationTemplateID>103c4514-db6e-489b-bc08-e9e131b60099</NotificationTemplateID>
 </HtmlDevice>
```

#### Configuring an
                              	 HTML-Based Notification Template with an HTML Notification Device

This PUT request allow users to
                                    		  apply an HTML-based notification template with an HTML notification device. The
                                    		  user can perform this action if the template selection rights are given by
                                    		  administrator. The following is an example of PUT request:

```
PUT /vmrest/users/notificationdevices/htmldevices/<deviceobjectid>
```

This API will modify a particular HTML notification device for the end
                                    		  users as represented by <deviceobjectid>.

#### Configuring
                              	 Schedule Notification

Cisco Unity Connection allows you
                                 		to receive schedule notification tag in 24 hours format (hh:mm) using
                                 		<SendScheduledNotificationAt>. You can configure multiple notifications
                                 		using comma in the separated values. The schedules mentioned in this tag would
                                 		overwrite all the existing schedules. In order to delete all existing
                                 		schedules, provide an empty <SendScheduledNotificationAt> tag.

##### Listing Schedule
                                 	 Notification

The following is an example of
                                       		  the GET request that lists the HTML notification devices for the users:

```
GET vmrest/users/<user-object-id>/notificationdevices/htmldevices/<device-object-id>
```

The following is an example of the response from the above *GET*
                                       		  request and the actual response will depend upon the information given by you:

```
<HtmlDevice>
  <URI>/vmrest/users/a3ab2df0-f16c-405f-afdf-394495acf000/notificationdevices/htmldevices/856c8ce9-d7dd-4623-888b-8d14874061af</URI>
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
GET vmrest/users/<user-object-id>/notificationdevices/htmldevices/<device-object-id>?jsopn=1
```

```
{
    {
      "URI":"/vmrest/users/707c291f-95d8-4353-9d8c-2439722f4c25/notificationdevices/htmldevices/49d04c39-f899-445c-a939810d66b30e38",
      "Active":"false",
      "DeviceName":"HTML",
      "DisableMobileNumberFromPCA":"false",
      "DisplayName":"HTML",
      "ObjectId":"49d04c39-f899-445c-a939-810d66b30e38",
      "Undeletable":"true",
      "SubscriberObjectId":"707c291f-95d8-4353-9d8c-2439722f4c25",
      "UserURI":"/vmrest/users/707c291f-95d8-4353-9d8c2439722f4c25",
      "DisableTemplateSelectionFromPCA":"false",
      "AllowVoiceMailAsAttachment":"false",
      "EventList":"NewVoiceMail",
      "ScheduleSetObjectId":"a6fec625-58e1-4a2c-8950-829ee307d81a",
      "SendScheduledNotificationAt":"12:50"
    }
}
```

```
Response Code: 200 OK
```

##### Modifying Schedule
                                 	 Notification

The following is an example of
                                       		  the PUT request that modifies the Schedule notification for the user as
                                       		  represented by <SendScheduledNotificationAt>:

```
PUT vmrest/users/<user-object-id>/notificationdevices/htmldevices/<device-object-id>
```

```
Response Code: 204 OK
<HtmlDevice>
  <URI>/vmrest/users/a3ab2df0-f16c-405f-afdf-394495acf000/notificationdevices/htmldevices/856c8ce9-d7dd-4623-888b-8d14874061af</URI>
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
PUT vmrest/users/<user-object-id>/notificationdevices/htmldevices/<device-object-id>?jsonp=1
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

The following is an example of the PUT request that deletes all the
                                       		  existing schedules by representing the <SendScheduledNotificationAt> tag
                                       		  empty:

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

### Explanation of
                           	 Data Fields

Values:

- true:Enable the
                                                      						  device

- false:Do not
                                                      						  enable the notification device

Possible values:

- All Voice
                                                      						  messages: NewVoiceMail

- All voice
                                                      						  message urgent only: NewUrgentVoiceMail

- Dispatch
                                                      						  message: DispatchMessage

- Dispatch message
                                                      						  urgent only: UrgentDispatchMessage

- Fax message:
                                                      						  NewFax

- Fax message
                                                      						  urgent only: NewUrgentFax

- Calendar
                                                      						  Appointments: CalendarAppointment

- Calendar
                                                      						  Meetings: CalendarMeeting

Default value: NewVoiceMail.

Values:

- false:Enable
                                                      						  Outdial Number From Cisco PCA (Default value)

- True:Disable
                                                      						  Outdial Number From Cisco PCA

- true:Disable

- false:enable

Default value is false.

false: Don't Allow notifier to send voice mail recording
                                                						with the notification true: Allow notifier to send voice mail recording with
                                                						the notification Default value is false.

```
https://<Connectio-server>/vmrest/notificationtemplates
```

Possible values:

- true: For
                                                      						  default HTML Device

- false:For other
                                                      						  userdefined HTML Devices

### Enum Type

| GET https://<connection-server>/vmrest/users/<user-object> |
|---|

| GET https://<connection-server>/vmrest/users/<user-objectid>/usernotificationdevices |
|---|

| PUT:https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/pagerdevices/<pagerobjectid> |
|---|

| <PagerDevice>
  <RetriesOnBusy>4</RetriesOnBusy>
  <RetriesOnRna>4</RetriesOnRna>
  <RetriesToWait>10</RetriesToWait>
  <BusyRetryInterval>5</BusyRetryInterval>
  <RnaRetryInterval>15</RnaRetryInterval>
</PagerDevice> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/pagerdevices/<pagerobjectid>
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| {
  "FailDeviceObjectId":"c5ce04c1-e76e-4075-97f9-471ac49b7e85"
} |
|---|

| Response Code: 204 |
|---|

| Note | To activate notification device <PhoneNumber> parameter is
                                             			 mandatory and <RepeatInterval > parameter is mandatory to enable repeat
                                             			 notify. The provided values can be changed and possible values are given in the
                                             			 Explanation of Fields: Pager and Phone table. |
|---|---|

| GET https://<connection-server>/vmrest/users/<users>/<user-objectid>/notificationdevices/pagerdevices/<pagerobjectId>
Accept: application/json
Connection: keep-alive |
|---|

| {
 URI":"/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/notificationdevices/pagerdevices/6215dce7-cf4a-469a-8722-035b6228ba3d"
 "TransmitForcedAuthorizationCode":"false"
 "AfterDialDigits":""
 "BusyRetryInterval":"5"
 "DialDelay":"1"
 "PhoneNumber":"123"
 "RetriesOnBusy":"10"
 "RetriesOnRna":"10"
 "RingsToWait":"10"
 "RnaRetryInterval":"1"
 "SendCount":"false"
 "WaitConnect":"false"
 "MediaSwitchObjectId":"7b092808-d815-4c0b-a10d-d02d3f5090b8"
 "PhoneSystemURI":"/vmrest/phonesystems/7b092808-d815-4c0b-a10d-d02d3f5090b8"
 "ObjectId":"6215dce7-cf4a-469a-8722-035b6228ba3d"
 "Active":"false"
 "DeviceName":"Pager"
 "DisplayName":"Pager"
 "MaxBody":"512"
 "MaxSubject":"64"
 "SubscriberObjectId":"9375d893-c8eb-437b-90bf-7de4b1d0c3e8"
 "UserURI":"/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8"
 "SendCallerId":"false"
 "Undeletable":"true"
 "SuccessRetryInterval":"1"
 "RetriesOnSuccess":"0"
 "EventList":"NewUrgentFaxUrgentDispatchMessage"
 "ScheduleSetObjectId":"1f360ab8-076e-4cb5-bfde-ef7d3805f037"InitialDelay":"12"
 "VoiceMessage":"false"
 "UrgentOnly":"false"
 "RepeatInterval":"1"
 "RepeatNotify":"true",
 "FailDeviceObjectId":"c5ce04c1-e76e-4075-97f9-471ac49b7e85"
} |
|---|

| Response Code: 200 |
|---|

| POST: https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/pagerdevices |
|---|

| <PagerDevice>
   <PhoneNumber>12334</PhoneNumber>
   <DisplayName>Newpager</DisplayName>
   <MediaSwitchObjectId>8adf6869-4afc-4455-9fd5-d05b68ca6630</MediaSwitchObjectId>
</PagerDevice> |
|---|

| Response Code: 201 |
|---|

| POST https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/pagerdevices
Accept: application/json
Content-type:  application/json
Connection: keep-alive |
|---|

| {
  "DisplayName":"New Pager",
  "PhoneNumber":"1234",
  "MediaSwitchObjectId":"ae63574f-2aaf-4c28-8973-bfa8e3b1dd1c"
} |
|---|

| Response Code: 201
/vmrest/users/<user-objectid>/notificationdevices/pagerdevices/84e72420-615e-4d94-b1df-f1317906cce3 |
|---|

| https://<connection-server>/vmrest/phonesystems |
|---|

| GET https://<connection-server>/vmrest/users/<user-objectid> |
|---|

| https://<connection-server>/vmrest/users/<user-objectid>/usernotificationdevices |
|---|

| GET:https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/phonedevices/<phone_objectid> |
|---|

| Response code: 200 |
|---|

| GET https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/phonedevices/<phone_objectid>
Accept: application/json
Content-type:  application/json
Connection: keep-alive |
|---|

| Response Code: 200 |
|---|

| POST https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/phonedevices |
|---|

| <PhoneDevice>
  <DisplayName>Work Phone1</DisplayName>
  <PhoneNumber>123</PhoneNumber>
  <MediaSwitchObjectId>ae63574f-2aaf-4c28-8973-bfa8e3b1dd1c</MediaSwitchObjectId>
</PhoneDevice> |
|---|

| Response Code: 201 |
|---|

| POST https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/phonedevices
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| {
  "DisplayName":"Work Phone1",
  "PhoneNumber":"123",
  "MediaSwitchObjectId":"ae63574f-2aaf-4c28-8973-bfa8e3b1dd1c"
} |
|---|

| Response Code: 201 |
|---|

| https://<connection-server>/vmrest/phonesystems |
|---|

| PUT:https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/phonedevices/<phone_objectid>
<PhoneDevice>
  <RetriesOnBusy>10</RetriesOnBusy>
  <RetriesOnRna>10</RetriesOnRna>
  <RingsToWait>10</RingsToWait>
  <RnaRetryInterval>1</RnaRetryInterval>
</PhoneDevice> |
|---|

| Response code: 204 |
|---|

| PUT https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/phonedevices/<phone_objectid>
Accept: application/json
Content-type:  application/json
Connection: keep-alive |
|---|

| {
  "FailDeviceObjectId":"c5ce04c1-e76e-4075-97f9-471ac49b7e85"
} |
|---|

| Response code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/phonedevices/<phone_objectid> |
|---|

| Response code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/users/<user-objectid>/notificationdevices/phonedevices/<phone_objectid>
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| Response Code: 204 |
|---|

| GET:https://<Connection-server>/vmrest/user/notificationdevices/smtpdevices |
|---|

| Response code: 200 |
|---|

| GET https://<connection-server>/vmrest/user/notificationdevices/smtpdevices
Accept: application/json
Content-type:  application/json
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
   "SendPcaLink": "false",
   "Undeletable": "true",
   "HeaderText": "Texoma_Header",
   "FooterText": "Texoma_Footer"
} |
|---|

| Response Code: 200 |
|---|

| GET:https://<Connection-server>/vmrest/user/notificationdevices/smtpdevices/<smtpDeviceObjectId> |
|---|

| Response code: 204 |
|---|

| <SmtpDevice>
  <SmtpAddress>John@cisco.com</SmtpAddress>
  <HeaderText>Texoma_Header</HeaderText>
  <FooterText>Texoma_Footer</FooterText>
</SmtpDevice> |
|---|

| PUT https://<connection-server>/vmrest/user/notificationdevices/smtpdevices/<smtpDeviceObjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| {   
  "SmtpAddress": "John@cisco.com",
  "HeaderText": "Texoma_Header",
  "FooterText": "Texoma_Footer"
} |
|---|

| Response code: 204 |
|---|

| GET /vmrest/users/notificationdevices/htmldevices |
|---|

| <HtmlDevices total="3">
  <HtmlDevice>
  <URI>/vmrest/users/5786019c-f962-4b86-8103-a01755b9993c/notificationdevices/htmldevices/d7044a91-b3b5-4e5a-9d08-eca2235660fd</URI>
  <Active>false</Active>
  <DeviceName>HTML</DeviceName>
  <DisableMobileNumberFromPCA>false</DisableMobileNumberFromPCA>
  <DisplayName>HTML_Missed_Call</DisplayName>
  <NotificationTemplateID>f37de0e3-c070-4d7e-bb98-5b8b1911ed27</NotificationTemplateID>
  <ObjectId>d7044a91-b3b5-4e5a-9d08-eca2235660fd</ObjectId>
  <Undeletable>true</Undeletable>
  <SubscriberObjectId>5786019c-f962-4b86-8103-a01755b9993c</SubscriberObjectId>
  <UserURI>/vmrest/users/5786019c-f962-4b86-8103-a01755b9993c</UserURI>
  <DisableTemplateSelectionFromPCA>false</DisableTemplateSelectionFromPCA>
  <AllowVoiceMailAsAttachment>false</AllowVoiceMailAsAttachment>
  <MessageCountInSummary>10</MessageCountInSummary>
  <EventList>NewMissedCall</EventList>
  <ScheduleSetObjectId>48993a7c-2732-4217-8abc-893604fa16b6</ScheduleSetObjectId>
  <SendScheduledNotificationAt/>
  </HtmlDevice>
 </HtmlDevices> |
|---|

| GET /vmrest/user/notificationdevices/htmldevices/<deviceid> |
|---|

| <HtmlDevice>
   <URI>/vmrest/user/notificationdevices/htmldevices/8660c5af-b544-47cc-93eb-93f4923bc03b</URI>
   <Active>false</Active>
   <CallbackNumber>1234</CallbackNumber>
   <DeviceName>HTML</DeviceName>
   <DisableMobileNumberFromPCA>false</DisableMobileNumberFromPCA>
   <DisableTemplateSelectionFromPCA>false</DisableTemplateSelectionFromPCA>
   <DisplayName>HTML</DisplayName>
   <NotificationTemplateID>75825d74-bf4f-4af3-bf84-6226389a8611
   </NotificationTemplateID>
   <ObjectId>8660c5af-b544-47cc-93eb-93f4923bc03b</ObjectId>
   <PhoneNumber />
   <SmtpAddress />
   <Undeletable>true</Undeletable>
   <SubscriberObjectId>a880bb22-0df1-45aa-893e-895ebf2d3652
   </SubscriberObjectId>
   <UserURI>/vmrest/users</UserURI>
   <EventList>NewVoiceMail</EventList>
   <ScheduleSetObjectId>1fb3df1c-6ff6-4876-996d-59052126f1fa
   </ScheduleSetObjectId>
   <InitialDelay>0</InitialDelay>
   <RepeatInterval>0</RepeatInterval>
   <RepeatNotify>false</RepeatNotify>
  </HtmlDevice> |
|---|

| PUT /vmrest/users/notificationdevices/htmldevices/<deviceid> |
|---|

| PUT /vmrest/users/notificationdevices/htmldevices/<deviceobjectid>

 <HtmlDevice>
   <NotificationTemplateID>103c4514-db6e-489b-bc08-e9e131b60099</NotificationTemplateID>
 </HtmlDevice> |
|---|

| PUT /vmrest/users/notificationdevices/htmldevices/<deviceobjectid> |
|---|

| GET vmrest/users/<user-object-id>/notificationdevices/htmldevices/<device-object-id> |
|---|

| <HtmlDevice>
  <URI>/vmrest/users/a3ab2df0-f16c-405f-afdf-394495acf000/notificationdevices/htmldevices/856c8ce9-d7dd-4623-888b-8d14874061af</URI>
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

| GET vmrest/users/<user-object-id>/notificationdevices/htmldevices/<device-object-id>?jsopn=1 |
|---|

| {
    {
      "URI":"/vmrest/users/707c291f-95d8-4353-9d8c-2439722f4c25/notificationdevices/htmldevices/49d04c39-f899-445c-a939810d66b30e38",
      "Active":"false",
      "DeviceName":"HTML",
      "DisableMobileNumberFromPCA":"false",
      "DisplayName":"HTML",
      "ObjectId":"49d04c39-f899-445c-a939-810d66b30e38",
      "Undeletable":"true",
      "SubscriberObjectId":"707c291f-95d8-4353-9d8c-2439722f4c25",
      "UserURI":"/vmrest/users/707c291f-95d8-4353-9d8c2439722f4c25",
      "DisableTemplateSelectionFromPCA":"false",
      "AllowVoiceMailAsAttachment":"false",
      "EventList":"NewVoiceMail",
      "ScheduleSetObjectId":"a6fec625-58e1-4a2c-8950-829ee307d81a",
      "SendScheduledNotificationAt":"12:50"
    }
} |
|---|

| Response Code: 200 OK |
|---|

| PUT vmrest/users/<user-object-id>/notificationdevices/htmldevices/<device-object-id> |
|---|

| Response Code: 204 OK
<HtmlDevice>
  <URI>/vmrest/users/a3ab2df0-f16c-405f-afdf-394495acf000/notificationdevices/htmldevices/856c8ce9-d7dd-4623-888b-8d14874061af</URI>
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

| PUT vmrest/users/<user-object-id>/notificationdevices/htmldevices/<device-object-id>?jsonp=1 |
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

| Device Name | Data Type | Operations | Comments |
|---|---|---|---|
| Device Name | String(12) | Read Only | Device name of HTML notification device. |
| Display Name | String(64) | Read Only | The preferred text name of the notification
                                             					 device to be used when displaying entries in the administrative console, e.g.
                                             					 Cisco Unity Connection Administration. For example, "Home Phone," Pager 2,"
                                             					 "Work Phone, " etc. |
| Active | Boolean | Read Only | Enable notification device. Values: true:Enable the
                                                      						  device false:Do not
                                                      						  enable the notification device |
| EventList | String | Read/Write | By default it is NewVoiceMail. Possible values: All Voice
                                                      						  messages: NewVoiceMail All voice
                                                      						  message urgent only: NewUrgentVoiceMail Dispatch
                                                      						  message: DispatchMessage Dispatch message
                                                      						  urgent only: UrgentDispatchMessage Fax message:
                                                      						  NewFax Fax message
                                                      						  urgent only: NewUrgentFax Calendar
                                                      						  Appointments: CalendarAppointment Calendar
                                                      						  Meetings: CalendarMeeting Default value: NewVoiceMail. Note To keep value of this field blank, enter "None" value
                                                            						  for the field. | Note | To keep value of this field blank, enter "None" value
                                                            						  for the field. |
| Note | To keep value of this field blank, enter "None" value
                                                            						  for the field. |
| SmtpAddress | String(320) | Read Only | SMTP address to be notified. |
| ObjectId | String(36) | Read Only | Unique identifier of Notification Device |
| DisableMobileNumberFromPCA | Boolean | Read Only | Disable Outdial Number From Cisco PCA Values: false:Enable
                                                      						  Outdial Number From Cisco PCA (Default value) True:Disable
                                                      						  Outdial Number From Cisco PCA |
| CallbackNumber | Integer | Read Only | Outdial Number |
| SubscriberObjectID | String(36) | Read Only | The unique identifier of the Subscriber
                                             					 object to which this notification device belongs. |
| ScheduleSetObjectId | String(36) | Read Only | The unique identifier of the Schedule |
| DisableTemplateSelectionFromPCA | Boolean | Read Only | Disable HTML Template selection From Cisco
                                             					 PCA true:Disable false:enable Default value is false. |
| AllowVoiceMailAsAttachement | Boolean | Read Only | A flag indicating whether Cisco Unity
                                             					 Connection will allow notifier to send voice mail recording with the
                                             					 notification. false: Don't Allow notifier to send voice mail recording
                                                						with the notification true: Allow notifier to send voice mail recording with
                                                						the notification Default value is false. |
| NotificationTemplateID | String(36) | Read Only | The unique identifier of the Notification
                                             					 Template object which this notification device is using for HTML based
                                             					 notification This URI can be used to fetch NotificationTemplateID https://<Connectio-server>/vmrest/notificationtemplates | https://<Connectio-server>/vmrest/notificationtemplates |
| https://<Connectio-server>/vmrest/notificationtemplates |
| PhoneNumber | String | Read/Write | The phone number to dial, including the
                                             					 trunk access code (if any), of the device. |
| Undeletable | Boolean | Read Only | flag indicating whether HTML cannot be
                                             					 deleted or not. Possible values: true: For
                                                      						  default HTML Device false:For other
                                                      						  userdefined HTML Devices |
| SendScheduledNotificationAt | Integer | Read/Write | A tag that is use to receive schedule
                                             					 notifications in 24 hours format (hh:mm). You can configure multiple
                                             					 notifications using comma in the separated values. |

| Note | To keep value of this field blank, enter "None" value
                                                            						  for the field. |
|---|---|

| https://<Connectio-server>/vmrest/notificationtemplates |
|---|

| Name | Value | Description |
|---|---|---|
| SystemGreeting | 0 | System greeting - Cisco Unity Connection
                                             					 plays a prerecorded greeting along with the recorded name of the subscriber
                                             					 (for example, "Sorry, <subscriber name> is not available"). If the
                                             					 subscriber does not have a recorded name, Cisco Unity Connection plays the
                                             					 subscriber extension instead. When a greeting is enabled but not recorded,
                                             					 Cisco Unity Connection plays a prerecorded system greeting. |
| RecordedGreeting | 1 | Recorded greeting - use a personal
                                             					 recording for the call handler (or subscriber). This can be recorded over the
                                             					 phone or from the Cisco Unity Connection Administration and CPCA administrative
                                             					 interfaces on the call handler/subscriber. |
| NoGreeting | 2 | No greeting is played. |