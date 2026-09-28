---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-api-user-pwd-pin-setting-html-5390954ed4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_cupi-api-user-pwd-pin-setting.html
retrieved_at: 2026-08-17T03:48:50.955757+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Password PIN
	 Settings

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Password PIN
	 Settings

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- User Password PIN
                     	 Settings

## User Password and
                        	 PIN Settings API

### Listing User PIN
                           	 Settings

```
GET https://<Connection-server>/vmrest/users/<user-objectid>/credential/pin
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
<Credential>
  <URI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/credential/pin</URI>
  <UserObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</UserObjectId>
  <CredentialType>4</CredentialType>
  <Credentials/>
  <IsPrimary>false</IsPrimary>
  <CantChange>false</CantChange>
  <DoesntExpire>true</DoesntExpire>
  <TimeChanged>2013-03-05 11:24:33.344</TimeChanged>
  <HackCount>5</HackCount>
  <Locked>true</Locked>
  <TimeLastHack>2013-03-11 10:23:30.581</TimeLastHack>
  <TimeLockout>2013-03-05 11:24:33.344</TimeLockout>
  <Alias>Texoma</Alias>
  <CredMustChange>true</CredMustChange>
  <CredentialPolicyObjectId>a97ff291-8e60-475a-b7ee-e956ae83a730</CredentialPolicyObjectId>
  <Hacked>false</Hacked>
  <ObjectId>3f6f1cb0-3b00-45b5-91fd-d8553737eec7</ObjectId>
  <EncryptionType>3</EncryptionType>
</Credential>
```

```
Response Code: 200
```

### Listing User
                           	 Password Settings

```
GET https://<Connection-server>/vmrest/users/<user-objectid>/credential/password
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
<Credential>
  <URI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/credential/password</URI>
  <UserObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</UserObjectId>
  <CredentialType>3</CredentialType>
  <Credentials/>
  <IsPrimary>false</IsPrimary>
  <CantChange>false</CantChange>
  <DoesntExpire>true</DoesntExpire>
  <TimeChanged>2013-03-05 11:24:33.344</TimeChanged>
  <HackCount>5</HackCount>
  <Locked>true</Locked>
  <TimeLastHack>2013-03-11 10:23:30.581</TimeLastHack>
  <TimeLockout>2013-03-05 11:24:33.344</TimeLockout>
  <Alias>Texoma</Alias>
  <CredMustChange>true</CredMustChange>
  <CredentialPolicyObjectId>a97ff291-8e60-475a-b7ee-e956ae83a730</CredentialPolicyObjectId>
  <Hacked>false</Hacked>
  <ObjectId>3f6f1cb0-3b00-45b5-91fd-d8553737eec7</ObjectId>
  <EncryptionType>3</EncryptionType>
</Credential>
```

```
Response Code: 200
```

JSON Example

```
GET https://<Connection-server>/vmrest/users/<user-objectid>/credential/password 
Accept: application/json
Content-type:  application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
{
  “URI”: “/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/credential/password”
  “UserObjectId”: “9375d893-c8eb-437b-90bf-7de4b1d0c3e8”
  “CredentialType”: “3”
  “Credentials”
  “IsPrimary”: “false”
  “CantChange”: “false”
  “DoesntExpire”: “true”
  “TimeChanged”: “2013-03-05 11:24:33.344”
  “HackCount”: “5”
  “Locked”: “true”
  “TimeLastHack”: “2013-03-11 10:23:30.581”
  “TimeLockout”: “2013-03-05 11:24:33.344”
  “Alias”: “Texoma”
  “CredMustChange”: “true”
  “CredentialPolicyObjectId”: “a97ff291-8e60-475a-b7ee-e956ae83a730”
  “Hacked”: “false”
  “ObjectId”: “3f6f1cb0-3b00-45b5-91fd-d8553737eec7”
  “EncryptionType”: “3”
}
```

```
Response Code: 200
```

### Update
                           	 Password/PIN Settings

For PIN:

```
PUT https://<Connection-server>/vmrest/users/<user-objectid>/credential/pin
```

For Password:

```
PUT https://<Connection-server>/vmrest/users/<user-objectid>/credential/password
```

```
<Credential>
  <Locked>false</Locked>
  <DoesntExpire>true</DoesntExpire>
  <CredMustChange>true</CredMustChange>
  <CredentialPolicyObjectId>43e16996-57c6-46c4-86c0-f37d2edf0385</CredentialPolicyObjectId>
</Credential>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Unlock
                           	 Password/PIN Settings

A user's PIN is the password that a user must enter over the phone to
                                 		  sign into their mailbox to listen or send new messages by phone. To change a
                                 		  user's PIN you need the object ID of the user. A user's password is the web
                                 		  application password that is required to interact with web applications, such
                                 		  as the Cisco PCA or the Inbox applications.

For Password:

```
PUT https://<Connection-server>/vmrest/users/<user-objectid>/credential/password
```

For PIN:

```
PUT https://<Connection-server>/vmrest/users/<user-objectid>/credential/pin
```

```
<Credential>
  <HackCount>0</HackCount>
  <TimeHacked></TimeHacked>
</Credential>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example:

To Unlock Password:

```
PUT https://<Connection-server>/vmrest/users/<user-objectid>/credential/password 
Accept: application/json
Content-type:  application/json
Connection: keep-alive
Response Body:
{
  "HackCount":"0",
  "TimeHacked":""
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### To Unlock Password

```
PUT https://<Connection-server>/vmrest/users/<user-objectid>/credential/password 
Accept: application/json
Content-type:  application/json
Connection: keep-alive
Response Body:
{
  "HackCount":"0",
  "TimeHacked":""
}
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                 by you:

```
Response Code: 204
```

### Change
                           	 Password/PIN

For Password: PUT

```
https://<Connection-server>/vmrest/users/<user-objectid>/credential/password
```

For PIN:

```
PUT https://<Connection-server>/vmrest/users/<user-objectid>/credential/pin
```

```
<Credential>
  <Credentials>ciscfo1234</Credentials>
</Credential>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example:

To Update PIN

```
PUT https://<Connection-server>/vmrest/users/<user-objectid>/credential/pin
Accept: application/json
Content-type:  application/json
Connection: keep-alive
Response Body:
{
  "Credentials":"cisco1234"
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

- true

- false

Default value: false

Possible values:

- false: User can
                                                      						  change credential

- true: User
                                                      						  cannot change credential

Default Value: false

Possible values:

- true

- false

Default Value :true

Possible values:

- true

- false

Default value: false

Default value: 0

Possible Values:

- true

- false

Default Value: false

Possible values:(0-5)

- UNKNOWN: 0

- HASH_MD5: 1

- HASH_SHA1: 2

- HASH_IMS: 3

- REVERSIBLE: 4

- NONE: 5

Default Value: 0

- 4- for PIN

- 3- for Password

| GET https://<Connection-server>/vmrest/users/<user-objectid>/credential/pin |
|---|

| <Credential>
  <URI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/credential/pin</URI>
  <UserObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</UserObjectId>
  <CredentialType>4</CredentialType>
  <Credentials/>
  <IsPrimary>false</IsPrimary>
  <CantChange>false</CantChange>
  <DoesntExpire>true</DoesntExpire>
  <TimeChanged>2013-03-05 11:24:33.344</TimeChanged>
  <HackCount>5</HackCount>
  <Locked>true</Locked>
  <TimeLastHack>2013-03-11 10:23:30.581</TimeLastHack>
  <TimeLockout>2013-03-05 11:24:33.344</TimeLockout>
  <Alias>Texoma</Alias>
  <CredMustChange>true</CredMustChange>
  <CredentialPolicyObjectId>a97ff291-8e60-475a-b7ee-e956ae83a730</CredentialPolicyObjectId>
  <Hacked>false</Hacked>
  <ObjectId>3f6f1cb0-3b00-45b5-91fd-d8553737eec7</ObjectId>
  <EncryptionType>3</EncryptionType>
</Credential> |
|---|

| Response Code: 200 |
|---|

| GET https://<Connection-server>/vmrest/users/<user-objectid>/credential/password |
|---|

| <Credential>
  <URI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/credential/password</URI>
  <UserObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</UserObjectId>
  <CredentialType>3</CredentialType>
  <Credentials/>
  <IsPrimary>false</IsPrimary>
  <CantChange>false</CantChange>
  <DoesntExpire>true</DoesntExpire>
  <TimeChanged>2013-03-05 11:24:33.344</TimeChanged>
  <HackCount>5</HackCount>
  <Locked>true</Locked>
  <TimeLastHack>2013-03-11 10:23:30.581</TimeLastHack>
  <TimeLockout>2013-03-05 11:24:33.344</TimeLockout>
  <Alias>Texoma</Alias>
  <CredMustChange>true</CredMustChange>
  <CredentialPolicyObjectId>a97ff291-8e60-475a-b7ee-e956ae83a730</CredentialPolicyObjectId>
  <Hacked>false</Hacked>
  <ObjectId>3f6f1cb0-3b00-45b5-91fd-d8553737eec7</ObjectId>
  <EncryptionType>3</EncryptionType>
</Credential> |
|---|

| Response Code: 200 |
|---|

| GET https://<Connection-server>/vmrest/users/<user-objectid>/credential/password 
Accept: application/json
Content-type:  application/json
Connection: keep-alive |
|---|

| {
  “URI”: “/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/credential/password”
  “UserObjectId”: “9375d893-c8eb-437b-90bf-7de4b1d0c3e8”
  “CredentialType”: “3”
  “Credentials”
  “IsPrimary”: “false”
  “CantChange”: “false”
  “DoesntExpire”: “true”
  “TimeChanged”: “2013-03-05 11:24:33.344”
  “HackCount”: “5”
  “Locked”: “true”
  “TimeLastHack”: “2013-03-11 10:23:30.581”
  “TimeLockout”: “2013-03-05 11:24:33.344”
  “Alias”: “Texoma”
  “CredMustChange”: “true”
  “CredentialPolicyObjectId”: “a97ff291-8e60-475a-b7ee-e956ae83a730”
  “Hacked”: “false”
  “ObjectId”: “3f6f1cb0-3b00-45b5-91fd-d8553737eec7”
  “EncryptionType”: “3”
} |
|---|

| Response Code: 200 |
|---|

| PUT https://<Connection-server>/vmrest/users/<user-objectid>/credential/pin |
|---|

| PUT https://<Connection-server>/vmrest/users/<user-objectid>/credential/password |
|---|

| <Credential>
  <Locked>false</Locked>
  <DoesntExpire>true</DoesntExpire>
  <CredMustChange>true</CredMustChange>
  <CredentialPolicyObjectId>43e16996-57c6-46c4-86c0-f37d2edf0385</CredentialPolicyObjectId>
</Credential> |
|---|

| Response Code: 204 |
|---|

| PUT https://<Connection-server>/vmrest/users/<user-objectid>/credential/password |
|---|

| PUT https://<Connection-server>/vmrest/users/<user-objectid>/credential/pin |
|---|

| <Credential>
  <HackCount>0</HackCount>
  <TimeHacked></TimeHacked>
</Credential> |
|---|

| Response Code: 204 |
|---|

| PUT https://<Connection-server>/vmrest/users/<user-objectid>/credential/password 
Accept: application/json
Content-type:  application/json
Connection: keep-alive
Response Body:
{
  "HackCount":"0",
  "TimeHacked":""
} |
|---|

| Response Code: 204 |
|---|

| PUT https://<Connection-server>/vmrest/users/<user-objectid>/credential/password 
Accept: application/json
Content-type:  application/json
Connection: keep-alive
Response Body:
{
  "HackCount":"0",
  "TimeHacked":""
} |
|---|

| Response Code: 204 |
|---|

| https://<Connection-server>/vmrest/users/<user-objectid>/credential/password |
|---|

| PUT https://<Connection-server>/vmrest/users/<user-objectid>/credential/pin |
|---|

| <Credential>
  <Credentials>ciscfo1234</Credentials>
</Credential> |
|---|

| Response Code: 204 |
|---|

| PUT https://<Connection-server>/vmrest/users/<user-objectid>/credential/pin
Accept: application/json
Content-type:  application/json
Connection: keep-alive
Response Body:
{
  "Credentials":"cisco1234"
} |
|---|

| Response Code: 204 |
|---|

| Field Name | Data Type | Operation | Description |
|---|---|---|---|
| Locked | Boolean | Read/Write | A flag indicating whether access to the
                                             					 user account associated with this set of credentials is locked. Possible values: true false Default value: false |
| CantChange | Boolean | Read/Write | A flag indicating whether the user can set
                                             					 this credential. Possible values: false: User can
                                                      						  change credential true: User
                                                      						  cannot change credential Default Value: false |
| CredMustChange | Boolean | Read/Write | A flag indicating whether the user must
                                             					 change their credentials (PIN or password) at the next login. Possible values: true false Default Value :true |
| DoesntExpire | Boolean | Read/Write | A flag indicating whether this user
                                             					 credential will expire, and therefore the user must change the credential
                                             					 periodically. However, if the credential does not expire (value = "true"), the
                                             					 user still may change the credential (if allowed by CantChange). Possible values: true false Default value: false |
| CredentialPolicyObjectId | String(36) | Read/Write | The unique identifier of the CredentialPolicy object that is associated with this credential. Value for this parameter can
                                             be fetched from the objectid parameter. Response of the following URI: GET: https://<conection-server>/vmrest/credentialpolicies. |
| TimeChanged | datetime(8) | Read/Write | The unique identifier of the CredentialPolicy object that is associated with this credential. Value for this parameter can
                                             be fetched from the objectid parameter. Response of the following URI: GET: https://<conection-server>/vmrest/credentialpolicies. |
| HackCount | Integer(4) | Read/Write | The number of logon attempted that failed
                                             					 due to invalid credentials. The Unity system or external authentication
                                             					 provider determined that the credentials supplied as part of a user logon
                                             					 attempt were invalid. Default value: 0 |
| TimeLastHack | datetime(8) | Read/Write | The date and time of the last logon attempt
                                             					 with an invalid user credential. |
| TimeLockout | datetime(8) | Read/Write | The date and time that the credential was
                                             					 locked by an administrator. |
| TimeHacked | datetime(8) | Read/Write | The date and time that the credential was
                                             					 locked due to too many hacks. The date and time is recorded in this column
                                             					 whenever a user credential is locked due to too many hacks based on the
                                             					 credential policy. |
| ObjectId | String (36) | Read Only | Unique identifier for the password/pin |
| Credentials | String(256) | Read/Write | The PIN or password, for a user. The
                                             					 credentials are stored in an encrypted format. |
| Alias | String(64) | Read/Write | A unique text name of the user. |
| Hacked | Boolean | Read/Write | A flag indicating whether access to the
                                             					 user account associated with this set of credentials is locked due too many
                                             					 hack attempts. Possible Values: true false Default Value: false |
| EncryptionType | Integer | Read/Write | Type of encryption that was used to
                                             					 generate the credentials. Possible values:(0-5) UNKNOWN: 0 HASH_MD5: 1 HASH_SHA1: 2 HASH_IMS: 3 REVERSIBLE: 4 NONE: 5 Default Value: 0 |
| CredentialType | CredentialType | Read/Write | The type of credential such as password,
                                             					 PIN, Windows or Domino credential. 4- for PIN 3- for Password |