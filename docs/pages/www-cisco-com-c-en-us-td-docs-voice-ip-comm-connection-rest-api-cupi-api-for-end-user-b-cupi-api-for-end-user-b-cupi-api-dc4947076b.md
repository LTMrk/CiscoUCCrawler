---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-for-end-user-b-cupi-api-for-end-user-b-cupi-api-dc4947076b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API_for_End_User/b_CUPI_API_for_End_User/b_CUPI_API_for_End_User_chapter_010111.html
retrieved_at: 2026-08-21T08:05:53.770905+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

Updated: January 24, 2019

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- SystemConfiguration API

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- SystemConfiguration API

# Cisco Unity Connection Provisioning Interface (CUPI) API -- SystemConfiguration API

## System Configuration API

### JSON Example

There is no symmetry between the administrator CUPI URI's for configuration values and the end user access to configuration
                              values. Anything that an end user needs to have read access to has its own URI that an end user can get to. End users cannot
                              get to configuration values directly; for example, they cannot use the /vmrest/configurationvalue URI. If they attempt to
                              use it, they get access denied. A client using an end user's credentials may need to know some information about the system.
                              Currently the information involves two configuration values that an administrator can set:

System.Messaging.CumiAccessSecureMessageAttachments

System.Messaging.CumiAllowSecureMessageHeaders

Both settings need to be exposed to end users, but end users cannot access configuration values directly. To resolve this
                              issue, we created a way to expose some system values an end user client may need to see using the following URI. Listing System
                              Configuration

```
GET http://<connection-server>/vmrest/systemconfiguration
```

The following is the response from the *GET* request and the actual response will depend upon the information given by you:

```
<SystemConfiguration>
  <SecureMessageHeaders>true</SecureMessageHeaders>
  <SecureMessageAttachmentDownload>false</SecureMessageAttachmentDownload>
  <RecordingMaxLength>1200000</RecordingMaxLength>
  <DisableCopyVoiceMessage>false</DisableCopyVoiceMessage>
  <ConfirmDeleteMessage>1</ConfirmDeleteMessage>
</SystemConfiguration>
```

```
Response Code: 200
```

```
GET https://<connection-server>/vmrest/systemconfiguration
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

The following is the response from the *GET* request and the actual response will depend upon the information given by you:

```
{
  "SecureMessageHeaders": "true",
  "SecureMessageAttachmentDownload": "false",
  "RecordingMaxLength": "1200000",
  "DisableCopyVoiceMessage": "false",
  "ConfirmDeleteMessage": "1"
}
```

This URI can be accessed by any authenticated user, including an end user.

## Explanation of Data Fields

Parameter

Operations

Data Type

Comments

SecureMessageHeaders

Boolean

Read/Write

Flag indicating message has secure headers or not.

Possible values:

true

false

Default value:true

SecureMessageAttachmentDownload

Boolean

Read/Write

Flag indicating whether to have secured download of message attachment or not.

Possible values:

true

false

Default value:true

RecordingMaxLength

Integer

Read/Write

It specifies maximum length of recording of message.

Possible values: 0-3600000 Default value:1200000

DisableCopyVoiceMessage

Boolean

Read/Write

Flag indicating to copy voice message or not.

Possible values:

true

false

ConfirmDeleteMessage

Integer

Read/Write

Possible values:0-2

Default value:1

Topic 2.1

| Parameter | Operations | Data Type | Comments |
|---|---|---|---|
| SecureMessageHeaders | Boolean | Read/Write | Flag indicating message has secure headers or not. Possible values: true false Default value:true |
| SecureMessageAttachmentDownload | Boolean | Read/Write | Flag indicating whether to have secured download of message attachment or not. Possible values: true false Default value:true |
| RecordingMaxLength | Integer | Read/Write | It specifies maximum length of recording of message. Possible values: 0-3600000 Default value:1200000 |
| DisableCopyVoiceMessage | Boolean | Read/Write | Flag indicating to copy voice message or not. Possible values: true false |
| ConfirmDeleteMessage | Integer | Read/Write | Possible values:0-2 Default value:1 |