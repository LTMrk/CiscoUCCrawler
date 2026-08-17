---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cuc-api-user-mailbox-api-html-beaf674171
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_cuc_api_user-mailbox-api.html
retrieved_at: 2026-08-17T03:47:56.776419+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Mailbox API

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Mailbox API

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- User Mailbox API

Links to Other API pages: Cisco_Unity_Connection_APIs

## Mailbox
                        	 API

To get object ID for message
                              		  aging policy, use URI

```
GET https://<connection server>/vmrest/messageagingpolicies
```

```
GET https://<connection server>/vmrest/users/<userobjectid>/mailboxattributes
```

## Listing the
                        	 Mailbox Details of a User

```
GET https://<connection-server>/vmrest/users/<userobjectid>/mailboxattributes
```

The following is the response from the *GET* request and the actual
                              		  response will depend upon the information given by you:

```
<MailboxAttributes>
  <ByteSize>0</ByteSize>
  <MessageAgingPolicyObjectId>efb2f81f-32c5-4ed6-ba6b-d85260012d5c</MessageAgingPolicyObjectId>
  <Mounted>true</Mounted>
  <NotificationType>0</NotificationType>
  <SendReadReceipts>false</SendReadReceipts>
  <NumMessages>0</NumMessages>
  <Send>1024</Send>
  <Receive>1024</Receive>
  <Warn>1024</Warn>
</MailboxAttributes>
```

```
Response Code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/users/<userobjectid>/mailboxattributes
Accept: application/json
Connection: keep-alive
```

The following is the response from the *GET* request and the actual
                              		  response will depend upon the information given by you:

```
{
  "ByteSize":"0",
  "MessageAgingPolicyObjectId":"efb2f81f-32c5-4ed6-ba6b-d85260012d5c",
  "Mounted": "true",
  "NotificationType":"0",
  "SendReadReceipts":"false",
  "NumMessages":"0",
  "ReceiveQuota":"1024",
  "SendQuota":"1024",
  "WarningQuota":"1024"
}
```

```
Response Code: 200
```

## Updating Mailbox
                        	 Quota

Request Body: for use system
                              		  settings

```
<UserTemplate>
  <ReceiveQuota>-2</ReceiveQuota>
  <SendQuota>-2</SendQuota>
  <WarningQuota>-2</WarningQuota>
</UserTemplate>
```

The following is the response from the *PUT* request for use system
                              		  settings and the actual response will depend upon the information given by you:

```
Response Code: 204
```

Request Body: for custom system maximum settings

```
<UserTemplate>
  <ReceiveQuota>-1</ReceiveQuota>
  <SendQuota>-1</SendQuota>
  <WarningQuota>-1</WarningQuota>
</UserTemplate>
```

The following is the response from the *PUT* request for custom system
                              		  maximum settings and the actual response will depend upon the information given
                              		  by you:

```
Response Code: 204
```

Request Body: for custom settings

```
<UserTemplate>
  <ReceiveQuota>1048576</ReceiveQuota>
  <SendQuota>1048576</SendQuota>
  <WarningQuota>1048576</WarningQuota>
</UserTemplate>
```

The following is the response from the *PUT* request for custom
                              		  settings and the actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To change mailbox quota, do the following:

```
PUT https://<connection-server>/vmrest/users/<userobjectid>/mailboxattributes
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

```
{
  "ReceiveQuota":"104345",
  "SendQuota":"104345",
  "WarningQuota":"104345"
}
```

The following is the response from the above *PUT* request and the
                              		  actual response will depend upon the information given by you:

```
Response Code: 204
```

## Explanation of
                        	 Data Fields

Possible values:

- 2: The default
                                                   						  system quota is assigned.

- 1: The quota is
                                                   						  unlimited.

1- n : Limit in bytes which is integral multiple of 1024
                                             						bytes.

Possible values:

- 2: The default
                                                   						  system quota is assigned.

- 1: The quota is
                                                   						  unlimited.

1- n : Limit in bytes which is integral multiple of 1024
                                             						bytes.

Possible values:

- 2: The default
                                                   						  system quota is assigned.

- 1: The quota is
                                                   						  unlimited.

- 1- n : Limit in
                                                   						  bytes. which is integral multiple of 1024 bytes

Possible values:

- false: Disable

- true: Enable

Default value: false

Possible value:

- false: unMounted

- true: Mounted

Default value: true

Possible value:

- false: Classical
                                                   						  - marking a message unread, read and back to unread will turn the notification
                                                   						  (mwi) on, off and back on.

- true: Modern -
                                                   						  once a message has been touched (read) then it will not trigger notifications
                                                   						  each time the message is marked unread and read again.

Default Value: false

| GET https://<connection server>/vmrest/messageagingpolicies |
|---|

| GET https://<connection server>/vmrest/users/<userobjectid>/mailboxattributes |
|---|

| GET https://<connection-server>/vmrest/users/<userobjectid>/mailboxattributes |
|---|

| <MailboxAttributes>
  <ByteSize>0</ByteSize>
  <MessageAgingPolicyObjectId>efb2f81f-32c5-4ed6-ba6b-d85260012d5c</MessageAgingPolicyObjectId>
  <Mounted>true</Mounted>
  <NotificationType>0</NotificationType>
  <SendReadReceipts>false</SendReadReceipts>
  <NumMessages>0</NumMessages>
  <Send>1024</Send>
  <Receive>1024</Receive>
  <Warn>1024</Warn>
</MailboxAttributes> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/users/<userobjectid>/mailboxattributes
Accept: application/json
Connection: keep-alive |
|---|

| {
  "ByteSize":"0",
  "MessageAgingPolicyObjectId":"efb2f81f-32c5-4ed6-ba6b-d85260012d5c",
  "Mounted": "true",
  "NotificationType":"0",
  "SendReadReceipts":"false",
  "NumMessages":"0",
  "ReceiveQuota":"1024",
  "SendQuota":"1024",
  "WarningQuota":"1024"
} |
|---|

| Response Code: 200 |
|---|

| <UserTemplate>
  <ReceiveQuota>-2</ReceiveQuota>
  <SendQuota>-2</SendQuota>
  <WarningQuota>-2</WarningQuota>
</UserTemplate> |
|---|

| Response Code: 204 |
|---|

| <UserTemplate>
  <ReceiveQuota>-1</ReceiveQuota>
  <SendQuota>-1</SendQuota>
  <WarningQuota>-1</WarningQuota>
</UserTemplate> |
|---|

| Response Code: 204 |
|---|

| <UserTemplate>
  <ReceiveQuota>1048576</ReceiveQuota>
  <SendQuota>1048576</SendQuota>
  <WarningQuota>1048576</WarningQuota>
</UserTemplate> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/users/<userobjectid>/mailboxattributes
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| {
  "ReceiveQuota":"104345",
  "SendQuota":"104345",
  "WarningQuota":"104345"
} |
|---|

| Response Code: 204 |
|---|

| Note | Above all values are in bytes and in Cisco Unity Connection
                                          			 Administration, it takes values in MB. |
|---|---|

| Field Name | Data Types | Operation | Description |
|---|---|---|---|
| Send | Integer | Read/Write | Send limit mailbox size (in bytes).
                                          					 (Max:2048 MB) Possible values: 2: The default
                                                   						  system quota is assigned. 1: The quota is
                                                   						  unlimited. 1- n : Limit in bytes which is integral multiple of 1024
                                             						bytes. |
| Warning | Integer | Read/Write | Warning limit mailbox size (in bytes).
                                          					 Maximum size can be 2048 MB. Possible values: 2: The default
                                                   						  system quota is assigned. 1: The quota is
                                                   						  unlimited. 1- n : Limit in bytes which is integral multiple of 1024
                                             						bytes. |
| Receive | Integer | Read/Write | Receive limit mailbox size (in bytes).
                                          					 Maximum size can be 2048 MB. Possible values: 2: The default
                                                   						  system quota is assigned. 1: The quota is
                                                   						  unlimited. 1- n : Limit in
                                                   						  bytes. which is integral multiple of 1024 bytes |
| SendReadReceipts | Boolean | Read/Write | A flag indicating whether the mailbox
                                          					 created with this subscriber allows the system to send read receipts on its
                                          					 behalf. Possible values: false: Disable true: Enable Default value: false |
| ByteSize | Integer | Read Only | The total size, in bytes, of all voice
                                          					 messages for the current user. |
| Mounted | Boolean | Read Only | A flag indicating whether the mailbox store
                                          					 is mounted. Possible value: false: unMounted true: Mounted Default value: true |
| NotificationType | Integer | Read/Write | The notification type to use for this
                                          					 mailbox created Possible value: false: Classical
                                                   						  - marking a message unread, read and back to unread will turn the notification
                                                   						  (mwi) on, off and back on. true: Modern -
                                                   						  once a message has been touched (read) then it will not trigger notifications
                                                   						  each time the message is marked unread and read again. Default Value: false |
| NumMessages | Integer | Read Only | The total number of new messages, read
                                          					 messages, and messages that have been marked deleted |
| MessageAgingPolicyObjectId | String (36) | Read/Write | Object ID of a message aging policy |