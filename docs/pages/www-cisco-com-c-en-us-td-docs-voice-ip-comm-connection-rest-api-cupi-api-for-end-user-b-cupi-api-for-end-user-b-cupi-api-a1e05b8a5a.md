---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-for-end-user-b-cupi-api-for-end-user-b-cupi-api-a1e05b8a5a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API_for_End_User/b_CUPI_API_for_End_User/b_CUPI_API_for_End_User_chapter_01101.html
retrieved_at: 2026-08-21T08:05:12.194421+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

Updated: January 18, 2019

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- End User API

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- End User API

# Cisco Unity Connection Provisioning Interface (CUPI) API -- End User API

## End User API

Cisco Personal Communication Assistant users that are also called end users can use this API to perform the following operations:

Update transfer options (basic transfer rules), unified messaging account passwords (Connection 8.5 and later), external services
                                    account passwords (Connection 8.0), and user passwords and PINs.

Record greetings and voice names.

Create, read, update, and delete private lists and private list members, alternate names, and user-defined alternate extensions

Read SMTP proxy addresses, basic user information (for example, alias, display name, and DTMF access ID), class of service
                                    information, and administrator-defined alternate extensions.

To access all of the APIs mentioned in this document, the end user must login using his/her credentials.

Listing the Details of End User

The request can be used to fetch the end user's details. It provides basic details of an end user.

```
GET https://<connection-server>/vmrest/user
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                              by you:

```
<User>
  <FirstName>Texoma_</FirstName>
  <LastName>1113</LastName>
  <Alias>Texoma_1113</Alias>
  <DisplayName>Texoma_ 1113</DisplayName>
  <VoiceFileURI>/vmrest/user/voicename</VoiceFileURI>
  <ListInDirectory>true</ListInDirectory>
  <DtmfAccessId>1113</DtmfAccessId>
  <SmtpAddress>texoma_1113@texoma.com</SmtpAddress>
  <EmailAddress>texoma_1113@texoma.com</EmailAddress>
</User>
```

```
Response Code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/user
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                              by you:

```
{
  "FirstName": "Texoma_",
  "LastName": "1113",
  "Alias": "Texoma_1113",
  "DisplayName": "Texoma_ 1113",
  "VoiceFileURI": "/vmrest/user/voicename",
  "ListInDirectory": "true",
  "DtmfAccessId": "1113",
  "SmtpAddress": texoma_1113@texoma.com
  "EmailAddress": texoma_1113@texoma.cisco.com
}
```

```
Response Code: 200
```

### Updating Details of the End User

This request can be used to update the end user's details where only the ListInDirectory field can be updated.

```
PUT https://<connection-server>/vmrest/user/<userObjectid>
```

```
<User>
  <ListInDirectory>true</ListInDirectory>
</User>
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                 by you:

```
Response Code: 204
```

JSON Example

```
PUT https://<connection-server>/vmrest/user/<userObjectid>
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

```
{
  "ListInDirectory": "true
}
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                 by you:

```
Response Code: 204
```

### Explanation of Data Fields

Parameter

Operations

Data Type

Comments

First Name

Read Only

String

The first name (i.e., givenName) of this user.

Last Name

Read Only

String

The last name (i.e., surname or family name) of this user, by which a user is commonly known.

Alias

Read Only

String

A unique text name for User. Users enter the alias to sign in to the Cisco Personal Communications Assistant (Cisco PCA).

DisplayName

Read Only

String

Descriptive name for the user.

VoiceFileURI

Read Only

String

Specifies the URI of voice file.

ListInDirectory

Read/Write

Boolean

A flag indicating whether Cisco Unity Connection should list the subscriber in the phone directory for outside callers.

Values: •false:Do not list in Directory •true: List in directory Default Value: true.

DTMFAccessId

Read Only

String

The DTMF access id (i.e., extension) of the subscriber.

SMTPAddress

Read Only

String

The full SMTP address for the user

EmailAddress

Read Only

String

The corporate email address of the user.

| GET https://<connection-server>/vmrest/user |
|---|

| <User>
  <FirstName>Texoma_</FirstName>
  <LastName>1113</LastName>
  <Alias>Texoma_1113</Alias>
  <DisplayName>Texoma_ 1113</DisplayName>
  <VoiceFileURI>/vmrest/user/voicename</VoiceFileURI>
  <ListInDirectory>true</ListInDirectory>
  <DtmfAccessId>1113</DtmfAccessId>
  <SmtpAddress>texoma_1113@texoma.com</SmtpAddress>
  <EmailAddress>texoma_1113@texoma.com</EmailAddress>
</User> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/user
Accept: application/json
Connection: keep-alive |
|---|

| {
  "FirstName": "Texoma_",
  "LastName": "1113",
  "Alias": "Texoma_1113",
  "DisplayName": "Texoma_ 1113",
  "VoiceFileURI": "/vmrest/user/voicename",
  "ListInDirectory": "true",
  "DtmfAccessId": "1113",
  "SmtpAddress": texoma_1113@texoma.com
  "EmailAddress": texoma_1113@texoma.cisco.com
} |
|---|

| Response Code: 200 |
|---|

| PUT https://<connection-server>/vmrest/user/<userObjectid> |
|---|

| <User>
  <ListInDirectory>true</ListInDirectory>
</User> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/user/<userObjectid>
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| {
  "ListInDirectory": "true
} |
|---|

| Response Code: 204 |
|---|

| Parameter | Operations | Data Type | Comments |
|---|---|---|---|
| First Name | Read Only | String | The first name (i.e., givenName) of this user. |
| Last Name | Read Only | String | The last name (i.e., surname or family name) of this user, by which a user is commonly known. |
| Alias | Read Only | String | A unique text name for User. Users enter the alias to sign in to the Cisco Personal Communications Assistant (Cisco PCA). |
| DisplayName | Read Only | String | Descriptive name for the user. |
| VoiceFileURI | Read Only | String | Specifies the URI of voice file. |
| ListInDirectory | Read/Write | Boolean | A flag indicating whether Cisco Unity Connection should list the subscriber in the phone directory for outside callers. Values: •false:Do not list in Directory •true: List in directory Default Value: true. |
| DTMFAccessId | Read Only | String | The DTMF access id (i.e., extension) of the subscriber. |
| SMTPAddress | Read Only | String | The full SMTP address for the user |
| EmailAddress | Read Only | String | The corporate email address of the user. |