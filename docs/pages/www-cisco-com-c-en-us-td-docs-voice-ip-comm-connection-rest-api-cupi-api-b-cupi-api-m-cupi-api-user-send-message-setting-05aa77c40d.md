---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-api-user-send-message-setting-05aa77c40d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_cupi-api-user-send-message-setting.html
retrieved_at: 2026-08-17T03:48:34.049205+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Send Message
	 Settings

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Send Message
	 Settings

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- User Send Message
                     	 Settings

Links to Other API pages: Cisco_Unity_Connection_APIs

## Send Message
                        	 Settings API

### Listing the Send
                           	 Message Settings

The following URI can be used to
                                 		  get the Send Message Settings API of user:

```
GET https://<connection-server>/vmrest/users/<user-objectid>
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
<User>
  <AddressMode>0</AddressMode>
  <SendBroadcastMsg>true</SendBroadcastMsg>
  <UpdateBroadcastMsg>true</UpdateBroadcastMsg>
  <NameConfirmation>false</NameConfirmation>
  <ContinuousAddMode>false</ContinuousAddMode>
  <SendMessageOnHangup>2</SendMessageOnHangup>
</User>
```

```
Response Code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/users/<user-objectid>
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
{
  “AddressMode”: “0”
  “SendBroadcastMsg”: “true”
  “UpdateBroadcastMsg”: “true”
  “NameConfirmation”: “false”
  “ContinuousAddMode”: “false”
  “SendMessageOnHangup”: “2”
}
```

```
Response Code: 200
```

### Update Send
                           	 Message Settings

```
PUT https://<connection-server>/vmrest/users/<user-objectid>
```

```
<User>
  <AddressMode>0</AddressMode>
  <SendBroadcastMsg>true</SendBroadcastMsg>
  <UpdateBroadcastMsg>true</UpdateBroadcastMsg>
  <NameConfirmation>false</NameConfirmation>
  <ContinuousAddMode>false</ContinuousAddMode>
  <SendMessageOnHangup>2</SendMessageOnHangup>
</User>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

```
PUT https://<connection-server>/vmrest/users/<user-objectid>
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

```
{
  "AddressMode":"2",
  "UpdateBroadcastMsg":"true"
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Explanation of
                           	 Data Fields

Values:

- 0: Cannot send
                                                      						  broadcast messages.

- 1: Can send
                                                      						  broadcast messages.

Default value: False

- 0: Spelling the
                                                      						  Last Name Then First Name

- 1: Entering the
                                                      						  extension

- 2: Spelling the
                                                      						  First Name Then Last Name

- 0: Discard
                                                      						  Message

- 1: Send Message

- 2: Save Message
                                                      						  as Draft

| GET https://<connection-server>/vmrest/users/<user-objectid> |
|---|

| <User>
  <AddressMode>0</AddressMode>
  <SendBroadcastMsg>true</SendBroadcastMsg>
  <UpdateBroadcastMsg>true</UpdateBroadcastMsg>
  <NameConfirmation>false</NameConfirmation>
  <ContinuousAddMode>false</ContinuousAddMode>
  <SendMessageOnHangup>2</SendMessageOnHangup>
</User> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/users/<user-objectid>
Accept: application/json
Connection: keep-alive |
|---|

| {
  “AddressMode”: “0”
  “SendBroadcastMsg”: “true”
  “UpdateBroadcastMsg”: “true”
  “NameConfirmation”: “false”
  “ContinuousAddMode”: “false”
  “SendMessageOnHangup”: “2”
} |
|---|

| Response Code: 200 |
|---|

| PUT https://<connection-server>/vmrest/users/<user-objectid> |
|---|

| <User>
  <AddressMode>0</AddressMode>
  <SendBroadcastMsg>true</SendBroadcastMsg>
  <UpdateBroadcastMsg>true</UpdateBroadcastMsg>
  <NameConfirmation>false</NameConfirmation>
  <ContinuousAddMode>false</ContinuousAddMode>
  <SendMessageOnHangup>2</SendMessageOnHangup>
</User> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/users/<user-objectid>
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| {
  "AddressMode":"2",
  "UpdateBroadcastMsg":"true"
} |
|---|

| Response Code: 204 |
|---|

| Parameter | Data Type | Values |
|---|---|---|
| SendBroadcastMsg | Boolean | User Can Send Broadcast Messages to Users
                                             					 on This Server Values: 0: Cannot send
                                                      						  broadcast messages. 1: Can send
                                                      						  broadcast messages. Default value: False |
| UpdateBroadcastMsg | Boolean | User Can Update Broadcast Messages Stored
                                             					 on This Server |
| AddressMode | Integer | Address mode options. 0: Spelling the
                                                      						  Last Name Then First Name 1: Entering the
                                                      						  extension 2: Spelling the
                                                      						  First Name Then Last Name |
| NameConfirmation | Boolean | Confirm Recipient by Name |
| ContinuousAddMode | Boolean | Continue Adding Names after Each Recipient.
                                             					 Default value: False |
| UseDynamicNameSearchWeight | Boolean | Automatically Add Recipients to Addressing
                                             					 Priority List |
| EnableSaveDraft | Boolean | Allow Users to Save Draft Messages |
| RetainUrgentMessageFlag | Boolean | Retain Urgency Flag When Forwarding or
                                             					 Replying to Messages |
| SendMessageOnHangup | Integer | Allow addressing a message or discard
                                             					 Message or save Message as draft on hanging. 0: Discard
                                                      						  Message 1: Send Message 2: Save Message
                                                      						  as Draft |