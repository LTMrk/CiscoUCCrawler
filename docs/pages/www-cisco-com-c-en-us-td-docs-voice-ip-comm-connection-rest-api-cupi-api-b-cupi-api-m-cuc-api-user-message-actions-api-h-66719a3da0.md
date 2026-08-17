---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cuc-api-user-message-actions-api-h-66719a3da0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_cuc_api_user-message-actions-api.html
retrieved_at: 2026-08-17T03:48:00.682452+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Message Actions
	 API

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Message Actions
	 API

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- User Message Actions
                     	 API

Links to Other API pages: Cisco_Unity_Connection_APIs

## Message Actions
                        	 API

### Listing Message
                           	 Actions

First hit the URI:

```
GET https://<connection-server>/vmrest/users/<user-objectid>
```

Then, fetch the following URI from the response body:

```
https://<connection-server>/vmrest/users/<user-objectid>/messagehandlers/<object Id>
```

The following is the response from the *GET* request and the actual
                                 		  response will depend upon the information given by you:

```
<MessageHandler>
<URI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/messagehandlers/583722c8-e93b-42f0-8052-b75aa1ededb8</URI>
  <ObjectId>583722c8-e93b-42f0-8052-b75aa1ededb8</ObjectId>
  <SubscriberObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</SubscriberObjectId>
  <UserURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8</UserURI>
  <RelayAddress>Texoma@cisco.com</RelayAddress>
  <VoicemailAction>2</VoicemailAction>
  <EmailAction>2</EmailAction>
  <FaxAction>2</FaxAction>
  <DeliveryReceiptAction>1</DeliveryReceiptAction>
</MessageHandler>
```

```
Response Code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/users/<objectid>/messagehandlers/<object Id>
Accept: application/json
Connection:  keep-alive
```

The following is the response from the *GET* request and the actual
                                 		  response will depend upon the information given by you: Response Body:

```
{
  "URI":"/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/messagehandlers/583722c8-e93b-42f0-8052-b75aa1ededb8"
  "ObjectId":"583722c8-e93b-42f0-8052-b75aa1ededb8"
  "SubscriberObjectId":"9375d893-c8eb-437b-90bf-7de4b1d0c3e8"
  "UserURI":"/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8"
  "RelayAddress":Texoma@cisco.com
  "VoicemailAction":"2"
  "EmailAction":"2"
  "FaxAction":"2"
  "DeliveryReceiptAction":"1"
}
```

```
Response Code: 200
```

### Update Message
                           	 Actions

First hit the URI:

```
https://<connection-server>/vmrest/users/<user-objectid>
```

Then fetch the following URI from the response body:

```
https://<connection-server>/vmrest/users/<user-objectid>/messagehandlers/<object Id>
```

```
<MessageHandler>
  <VoicemailAction>2</VoicemailAction>
  <EmailAction>2</EmailAction>
  <FaxAction>2</FaxAction>
  <DeliveryReceiptAction>1</DeliveryReceiptAction>
  <RelayAddress>cguii@10.com</RelayAddress>
</MessageHandler>
```

```
Response code: 204
```

JSON Example

```
PUT https://<connection-server>/vmrest/users/<objectid>/messagehandlers/<object Id>
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

```
{
  "EmailAction":"2",
  "FaxAction":"2",
  "DeliveryReceiptAction":"1",
  "RelayAddress":"john@cisco.com"
}
```

```
Response code: 204
```

### Explanation of
                           	 Data Fields

Default value: 1

Default value: 1

Default value: 1

Default value: 1

Email Action, Fax Action, Delivery Receipt Action, and Voicemail
                                 		  Action can take the following values:

- 0 - Reject the message

- 1 - Accept the message

- 2 - Relay the message

- 3 - Accept and relay the
                                       			 message

| GET https://<connection-server>/vmrest/users/<user-objectid> |
|---|

| https://<connection-server>/vmrest/users/<user-objectid>/messagehandlers/<object Id> |
|---|

| <MessageHandler>
<URI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/messagehandlers/583722c8-e93b-42f0-8052-b75aa1ededb8</URI>
  <ObjectId>583722c8-e93b-42f0-8052-b75aa1ededb8</ObjectId>
  <SubscriberObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</SubscriberObjectId>
  <UserURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8</UserURI>
  <RelayAddress>Texoma@cisco.com</RelayAddress>
  <VoicemailAction>2</VoicemailAction>
  <EmailAction>2</EmailAction>
  <FaxAction>2</FaxAction>
  <DeliveryReceiptAction>1</DeliveryReceiptAction>
</MessageHandler> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/users/<objectid>/messagehandlers/<object Id>
Accept: application/json
Connection:  keep-alive |
|---|

| {
  "URI":"/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/messagehandlers/583722c8-e93b-42f0-8052-b75aa1ededb8"
  "ObjectId":"583722c8-e93b-42f0-8052-b75aa1ededb8"
  "SubscriberObjectId":"9375d893-c8eb-437b-90bf-7de4b1d0c3e8"
  "UserURI":"/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8"
  "RelayAddress":Texoma@cisco.com
  "VoicemailAction":"2"
  "EmailAction":"2"
  "FaxAction":"2"
  "DeliveryReceiptAction":"1"
} |
|---|

| Response Code: 200 |
|---|

| https://<connection-server>/vmrest/users/<user-objectid> |
|---|

| https://<connection-server>/vmrest/users/<user-objectid>/messagehandlers/<object Id> |
|---|

| <MessageHandler>
  <VoicemailAction>2</VoicemailAction>
  <EmailAction>2</EmailAction>
  <FaxAction>2</FaxAction>
  <DeliveryReceiptAction>1</DeliveryReceiptAction>
  <RelayAddress>cguii@10.com</RelayAddress>
</MessageHandler> |
|---|

| Response code: 204 |
|---|

| PUT https://<connection-server>/vmrest/users/<objectid>/messagehandlers/<object Id>
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| {
  "EmailAction":"2",
  "FaxAction":"2",
  "DeliveryReceiptAction":"1",
  "RelayAddress":"john@cisco.com"
} |
|---|

| Response code: 204 |
|---|

| Parameter | Data Type | Operations | Description |
|---|---|---|---|
| DeliveryReceiptAction | Integer | Read/Write | The action to take for delivery receipt
                                             					 messages. Possible values are given just below the table. Default value: 1 |
| EmailAction | Integer | Read/Write | The action to take for email messages.
                                             					 Possible values are given just below the table. Default value: 1 |
| FaxAction | Integer | Read/Write | The action to take for fax messages.
                                             					 Possible values are given just below the table. Default value: 1 |
| ObjectId | String(36) | Read Only | The primary key for this table. A globally
                                             					 unique system-generated identifier for a MessageHandler object |
| RelayAddress | String(320) | Read/Write | The SMTP address to which messages should
                                             					 be relayed |
| SubscriberObjectId | String(36) | Read Only | The unique identifier of the Subscriber
                                             					 object to which this message handler belongs. |
| VoicemailAction | Integer | Read/Write | The action to take for voicemail messages.
                                             					 Possible values are given just below the table. Default value: 1 |