---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-api-user-caller-input-html-45332bbf12
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_cupi_api_user-caller-input.html
retrieved_at: 2026-08-17T03:47:48.562494+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Caller Input

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Caller Input

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- User Caller Input

Links to Other API pages: Cisco_Unity_Connection_APIs

## Caller Inputs
                        	 API

To get the caller input URI, follow
                           		the steps given below:

```
GET https://<connection-server>/vmrest/users/<user-objectid>
```

From above URI get the call handler URI:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>
```

To edit caller inputs, you need to get the menu entries:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/menuentries
```

### Listing Caller
                           	 Inputs

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/menuentries/<key>
```

The following is the response from the above *GET* request and the
                              		actual response will depend upon the information given by you:

```
<MenuEntry>
  <URI>/vmrest/handlers/callhandlers/287cdcc0-9f77-48e0-a7b1-0f9b1a5ac842/menuentries/1</URI>
  <CallHandlerObjectId>287cdcc0-9f77-48e0-a7b1-0f9b1a5ac842</CallHandlerObjectId>
  <CallhandlerURI>/vmrest/handlers/callhandlers/287cdcc0-9f77-48e0-a7b1-0f9b1a5ac842</CallhandlerURI>
  <TouchtoneKey>1</TouchtoneKey>
  <Locked>false</Locked>
  <Action>7</Action>
  <TargetConversation>BroadcastMessageAdministrator</TargetConversation>
  <ObjectId>d2a363af-d3f6-46cf-81c9-5ad48d2dccd7</ObjectId>
  <DisplayName>abc</DisplayName>
  <TransferType>0</TransferType>
  <TransferRings>9</TransferRings>
</MenuEntry>
```

JSON Example

```
GET https://<Connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/menuentries/4
Accept: application/json
Connection:  keep-alive
```

```
{
  "URI":"/vmrest/handlers/callhandlers/43bb6590-e9e3-43ca-972e-e3e158a96126/menuentries/4"
  "CallHandlerObjectId":"43bb6590-e9e3-43ca-972e-e3e158a96126"
  "CallhandlerURI":"/vmrest/handlers/callhandlers/43bb6590-e9e3-43ca-972e-e3e158a96126"
  "TouchtoneKey":"4"
  "Locked":"false"
  "Action":"2"
  "TargetConversation":"AD"
  "TargetHandlerObjectId":"80b1b22b-2fd8-458e-abd1-294e83a9ec55"
  "ObjectId":"a164d69a-5d0a-4c07-b2e2-d972448950db"
}
```

```
Response code: 200
```

### Updating Caller
                           	 Input Parameters

The following is an example of the
                              		PUT request that updates caller input parameters:

```
PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>
<Callhandler>
  <OneKeyDelay>9999</OneKeyDelay>
  <EnablePrependDigits>true</EnablePrependDigits>
  <PrependDigits>4545</PrependDigits>
</Callhandler>
```

The following is the response from the above *PUT* request and the
                              		actual response will depend upon the information given by you:

```
Response Code: 204
```

### Updating Caller
                           	 Input Keys

The following is an example of
                                 		  the PUT request that updates the call input keys:

```
PUT https://<connection-server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/menuentries
```

The following is an example of the PUT request that edits the call
                                 		  input keys for (*):

```
PUT https://<connection-server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/menuentries/*
Request Body:
<MenuEntry>
    <Locked>true</Locked>
</MenuEntry>
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

Example 1: Edit call actions

```
Request Body:
<MenuEntry>
    <Action>7</Action>
    <TransferType>1</TransferType>
    <TransferNumber>2344</TransferNumber>
    <TransferRings>4</TransferRings>
</MenuEntry>
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

Example 2: Edit Call Handler The following is an example of the
                                 		  PUT request that shows the call handler object ID:

```
PUT https://<connection-server>/vmrest/handlers/callhandlers
Request Body:
<MenuEntry>
    <Action>2</Action>
    <TargetConversation>PHGreeting</TargetConversation>       
    <TargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</TargetHandlerObjectId> 
</MenuEntry>
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

Example 3: Interview handler

```
Request Body:
<MenuEntry>
    <Action>2</Action>
    <TargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</TargetHandlerObjectId>  
</MenuEntry>
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

Example 4: Directory handler

```
Request Body:
<MenuEntry>
    <Action>2</Action>
    <TargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</TargetHandlerObjectId>  
</MenuEntry>
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

Example 5: Conversation

```
Request Body: for broadcast message administrator
</MenuEntry>
    <Action>2</Action>
    <TargetConversation>BroadcastMessageAdministrator</TargetConversation>
</MenuEntry>
```

The following is the response from the *PUT* request for broadcast
                                 		  message administrator and the actual response will depend upon the information
                                 		  given by you:

```
Response Code: 204
```

```
Request Body: for caller system transfer
<MenuEntry>
    <Action>2</Action>
    <TargetConversation>SystemTransfer</TargetConversation>
</MenuEntry>
```

The following is the response from the *PUT* request for caller system
                                 		  transfer and the actual response will depend upon the information given by you:

```
Response Code: 204
```

```
Request Body: for greeting administrator
<MenuEntry>
    <Action>2</Action>
    <TargetConversation>GreetingAdministrator</TargetConversation>
</MenuEntry>
```

The following is the response from the *PUT* request for greeting
                                 		  administrator and the actual response will depend upon the information given by
                                 		  you:

```
Response Code: 204
```

```
Request Body: for sign in
<MenuEntry>
    <Action>2</Action>
    <TargetConversation>SubSignIn</TargetConversation>
</MenuEntry>
```

The following is the response from the *PUT* request for sign in and
                                 		  the actual response will depend upon the information given by you:

```
Response Code: 204
```

```
Request Body: for user system transfer
<MenuEntry>
    <Action>2</Action>
    <TargetConversation>SubSysTransfer</TargetConversation>
</MenuEntry>
```

The following is the response from the *PUT* request for user system
                                 		  transfer and the actual response will depend upon the information given by you:

```
Response Code: 204
```

Example 4: Users with Mailbox

```
Request Body:
<MenuEntry>
    <Action>2</Action>
    <TargetConversation>PHTransfer</TargetConversation> 
    <TargetHandlerObjectId>71cb381b-fd16-4ba8-8a1d-e71684e57b0e</TargetHandlerObjectId>
</MenuEntry>
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

For conversation, do the following:

```
Request URI:
PUT https://<connection-server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/menuentries/4
Accept: application/json
Content-type: application/json
Connection: keep-alive
Request Body:
{
    "Action":"2",
    "TargetConversation":"SubSignIn"
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Explanation of
                           	 Data Fields

We recommend a value of 1,500 milliseconds (one and one-half
                                                						seconds).

- This option
                                                                  								is unavailable if Ignore Caller Input is enabled on the Greetings page.

- OneKeyDelay
                                                                  								can only accept integer with value 0 through 10000

Possible values:

- true

- false

Default value: false.

Values can be: • false: Unlocked - Additional dialing after
                                                						this choice is entered is allowed • true: Locked - Additional dialing is
                                                						ignored Default value: false.

Default value: 0

Possible Values:

- 0: Release to
                                                      						  switch

- 1: Supervise
                                                      						  transfer

Default Value: 0 TransferRings Integer Read/Write Applies
                                                						only when the "TransferType" column is set to supervised (1). This value should
                                                						never be less than 2 for a supervised transfer. Possible value: 2-20 Default
                                                						value: 4

| Note | <Prepend Digits> parameter must be having digits only
                                          		  (extension parameter) |
|---|---|

| PUT https://<connection-server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/menuentries |
|---|

| PUT https://<connection-server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/menuentries/*
Request Body:
<MenuEntry>
    <Locked>true</Locked>
</MenuEntry> |
|---|

| Response Code: 204 |
|---|

| Values | Parameters |
|---|---|
| 0 | Ignore |
| 1 | Hang Up |
| 4 | Take Message |
| 5 | Skip Greeting |
| 6 | Restart Greeting |
| 7 | Transfer to alternate contact number |
| 8 | Route from next call routing rule |

| Request Body:
<MenuEntry>
    <Action>7</Action>
    <TransferType>1</TransferType>
    <TransferNumber>2344</TransferNumber>
    <TransferRings>4</TransferRings>
</MenuEntry> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/callhandlers
Request Body:
<MenuEntry>
    <Action>2</Action>
    <TargetConversation>PHGreeting</TargetConversation>       
    <TargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</TargetHandlerObjectId> 
</MenuEntry> |
|---|

| Response Code: 204 |
|---|

| Request Body:
<MenuEntry>
    <Action>2</Action>
    <TargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</TargetHandlerObjectId>  
</MenuEntry> |
|---|

| Response Code: 204 |
|---|

| Request Body:
<MenuEntry>
    <Action>2</Action>
    <TargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</TargetHandlerObjectId>  
</MenuEntry> |
|---|

| Response Code: 204 |
|---|

| Request Body: for broadcast message administrator
</MenuEntry>
    <Action>2</Action>
    <TargetConversation>BroadcastMessageAdministrator</TargetConversation>
</MenuEntry> |
|---|

| Response Code: 204 |
|---|

| Request Body: for caller system transfer
<MenuEntry>
    <Action>2</Action>
    <TargetConversation>SystemTransfer</TargetConversation>
</MenuEntry> |
|---|

| Response Code: 204 |
|---|

| Request Body: for greeting administrator
<MenuEntry>
    <Action>2</Action>
    <TargetConversation>GreetingAdministrator</TargetConversation>
</MenuEntry> |
|---|

| Response Code: 204 |
|---|

| Request Body: for sign in
<MenuEntry>
    <Action>2</Action>
    <TargetConversation>SubSignIn</TargetConversation>
</MenuEntry> |
|---|

| Response Code: 204 |
|---|

| Request Body: for user system transfer
<MenuEntry>
    <Action>2</Action>
    <TargetConversation>SubSysTransfer</TargetConversation>
</MenuEntry> |
|---|

| Response Code: 204 |
|---|

| Request Body:
<MenuEntry>
    <Action>2</Action>
    <TargetConversation>PHTransfer</TargetConversation> 
    <TargetHandlerObjectId>71cb381b-fd16-4ba8-8a1d-e71684e57b0e</TargetHandlerObjectId>
</MenuEntry> |
|---|

| Response Code: 204 |
|---|

| Request URI:
PUT https://<connection-server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/menuentries/4
Accept: application/json
Content-type: application/json
Connection: keep-alive
Request Body:
{
    "Action":"2",
    "TargetConversation":"SubSignIn"
} |
|---|

| Response Code: 204 |
|---|

| Parameter | Data Type | Operations | Comments |
|---|---|---|---|
| OneKeyDelay | Integer | Read/Write | Indicate the amount of time that System
                                             					 waits for additional input after callers press a single key that is not locked.
                                             					 If there is no input within this time, system performs the action assigned to
                                             					 the single key. We recommend a value of 1,500 milliseconds (one and one-half
                                                						seconds). Note This option
                                                                  								is unavailable if Ignore Caller Input is enabled on the Greetings page. OneKeyDelay
                                                                  								can only accept integer with value 0 through 10000 | Note | This option
                                                                  								is unavailable if Ignore Caller Input is enabled on the Greetings page. OneKeyDelay
                                                                  								can only accept integer with value 0 through 10000 |
| Note | This option
                                                                  								is unavailable if Ignore Caller Input is enabled on the Greetings page. OneKeyDelay
                                                                  								can only accept integer with value 0 through 10000 |
| ObjectId | String(36) | Read Only | Unique Id for menu entry. |
| EnablePrependDigits | Boolean | Read/Write | To simulate abbreviated extensions by using
                                             					 prepended digits for call handlers and user mailboxes. When such digits are
                                             					 defined, they are prepended to any extension that a caller dials while
                                             					 listening to the greeting for the call handler or user mailbox. Possible values: true false Default value: false. |
| PrependDigits | Integer | Read/Write | Digits that are prepended to any extension
                                             					 that a caller dials while listening to the greeting of the user. |
| MenuEntriesURI | String(36) | Read Only | Parameters for caller input keys are
                                             					 present in menu entries URI. Note For # touchtone key, symbol %23 is used in the URI. | Note | For # touchtone key, symbol %23 is used in the URI. |
| Note | For # touchtone key, symbol %23 is used in the URI. |
| TouchtoneKey | String(1) | Read Only | Indicates the phone keypad key to which the
                                             					 settings apply. |
| Locked | Boolean | Read/Write | A locked menu entry does not allow
                                             					 additional dialing after this choice is entered. Values can be: • false: Unlocked - Additional dialing after
                                                						this choice is entered is allowed • true: Locked - Additional dialing is
                                                						ignored Default value: false. |
| Action | Integer | Read/Write | Takes values from 0-8. See table for
                                             					 values. Default value: 0 |
| CallHandlerObjectId | String(36) | Read Only | Menu entries can only belong to call
                                             					 handlers. No other object can own a menu entry. |
| TargetConversation | String(36) | Read/Write | The name of the conversation to which the
                                             					 caller is routed. |
| TargetHandlerObjectId | String(36) | Read/Write | The unique identifier of the specific
                                             					 object to send along to the target conversation. |
| TransferNumber | Integer | Read/Write | Extension to which call is transferred. |
| DisplayName | String(24) | Read/Write | Descriptive name of the handler being used. |
| TransferType | Integer | Read/Write | The type of call transfer Cisco Unity
                                             					 Connection will perform - supervised or unsupervised (also referred to as
                                             					 "Release to Switch" transfer). Possible Values: 0: Release to
                                                      						  switch 1: Supervise
                                                      						  transfer Default Value: 0 TransferRings Integer Read/Write Applies
                                                						only when the "TransferType" column is set to supervised (1). This value should
                                                						never be less than 2 for a supervised transfer. Possible value: 2-20 Default
                                                						value: 4 |

| Note | This option
                                                                  								is unavailable if Ignore Caller Input is enabled on the Greetings page. OneKeyDelay
                                                                  								can only accept integer with value 0 through 10000 |
|---|---|

| Note | For # touchtone key, symbol %23 is used in the URI. |
|---|---|