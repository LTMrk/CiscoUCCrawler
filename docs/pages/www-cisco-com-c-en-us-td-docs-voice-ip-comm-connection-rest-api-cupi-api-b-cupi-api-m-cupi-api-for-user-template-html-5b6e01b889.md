---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-api-for-user-template-html-5b6e01b889
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m-cupi-api-for-user-template.html
retrieved_at: 2026-08-17T03:49:15.475832+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API for User Template

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API for User Template

# Cisco Unity Connection Provisioning Interface (CUPI) API for User Template

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- User Template Caller
                        	 Inputs

### User Template
                           	 Caller Inputs

The following URI can be used to
                                 		  view the user template object ID:

```
GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>
```

From the above URI, get the call handler primary template object ID:

```
GET https://<connection-server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>
```

#### Updating Caller
                              	 Input Parameters

The following is
                                    		  an example of the PUT request that updates caller input parameters:

```
PUT https://<connection-server>/vmrest/handlers/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/menuentries
```

All the parameters
                                    		  for caller inputs are present in callhandlerprimarytemplate.

```
Request Body:
<CallhandlerPrimaryTemplate>
    <OneKeyDelay>9999</OneKeyDelay>
    <EnablePrependDigits>true</EnablePrependDigits>
    <PrependDigits>4545</PrependDigits>
</CallhandlerPrimaryTemplate>
```

The following is
                                    		  the response from the above *PUT* request and the actual response will depend
                                    		  upon the information given by you:

```
Response Code: 204
```

#### Updating Caller
                              	 Input Keys

The following is an example of
                                    		  the PUT request that updates the call input keys:

```
PUT
https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/menuentries
```

The following is an example of the PUT request that edits the call
                                    		  input keys:

```
PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/menuentries/*
```

where "*" is the touchtone key ID.

```
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

Example 2: Edit Call Handler

```
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

To get the call handler object ID:

```
GET https://<connection-server>/vmrest/handlers/callhandlers
```

Example 3: Interview handler

```
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

To get the Interview Handler object ID:

```
https://<connection-server>/vmrest/handlers/interviewhandlers
```

Example 4: Directory handler

```
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

To get the Directory Handler object ID:

```
https://<connection-server>/vmrest/handlers/directoryhandlers
```

Example 5: Conversation

Request Body: for broadcast message administrator

```
<MenuEntry>
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

Request Body: for caller system transfer

```
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

Request Body: for greeting administrator

```
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

Request Body: for sign in

```
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

Request Body: for user system transfer

```
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
PUT https://<connection-server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/menuentries/4
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

```
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

#### Explanation of
                              	 Data Fields

We recommend a value of 1,500 milliseconds (one and one-half
                                                   						seconds).

- This option
                                                                     								is unavailable if Ignore Caller Input is enabled on the Greetings page.

- OneKeyDelay
                                                                     								can only accept integer with value 0 through 10000

Default value: false.

Values can be:

- False: Unlocked
                                                         						  - Additional dialing after this choice is entered is allowed

- True: Locked -
                                                         						  Additional dialing is ignored

Default value: false.

- 0: Release to
                                                         						  switch

- 1: Supervise
                                                         						  transfer

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- User Template Greetings API

### User Template
                           	 Greetings APIs

The following URI can be used to
                                 		  view the user template object ID:

```
GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>
```

From the above URI, get the call handler primary template object ID:

```
GET https://<connection-
    server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>
```

The following URI can be used to view the greetings:

```
GET https://<connection- 
    server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId 
    >/usertemplategreetings
```

The following URI can be used to view the alternate greeting:

```
GET https://<connection-
    server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId
    >/usertemplategreetings/Alternate
```

The following URI can be used to view the busy greeting:

```
GET https://<connection-
    server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId
    >/usertemplategreetings/Busy
```

The following URI can be used to view the error greeting:

```
GET https://<connection-
    server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId
    >/usertemplategreetings/Error
```

The following URI can be used to view the closed greeting:

```
GET https://<connection-
    server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId
    >/usertemplategreetings/Off%20Hours
```

The following URI can be used to view the standard greeting:

```
GET https://<connection-
    server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId
    >/usertemplategreetings/Standard
```

The following URI can be used to view the holiday greeting:

```
GET https://<connection-
    server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId
    >/usertemplategreetings/Holiday
```

#### Updating Fields of
                              	 Greeting

```
PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Alternate
```

Request Body: Enable greeting

```
<Greeting>
  <EnableTransfer>true</EnableTransfer>
</Greeting>
```

The following is the response from the *PUT* request to enable
                                    		  greeting and the actual response will depend upon the information given by you:

```
Response Code: 204
```

Request Body: enable with no end date

```
<Greeting>
  <EnableTransfer>true</EnableTransfer>
  <TimeExpires></TimeExpires>
</Greeting>
```

The following is the response from the *PUT* request to enable with no
                                    		  end date and the actual response will depend upon the information given by you:

```
Response Code: 204
```

Request Body: enable until

```
<Greeting>
  <EnableTransfer>true</EnableTransfer>
  <TimeExpires>2014-12-31 05:30:00.000</TimeExpires>
</Greeting>
```

The following is the response from the *PUT* request to enable until
                                    		  and the actual response will depend upon the information given by you:

```
Response Code: 204
```

Request Body: edit caller hears

```
<Greeting>
  <PlayWhat>2</PlayWhat>
  <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt>  
</Greeting>
```

The following is the response from the *PUT* request to edit caller
                                    		  hears and the actual response will depend upon the information given by you:

```
Response Code: 204
```

Request Body: enable ignore caller inputs

```
<Greeting>
  <IgnoreDigits>true</IgnoreDigits>
</Greeting>
```

The following is the response from the *PUT* request to enable ignore
                                    		  caller inputs and the actual response will depend upon the information given by
                                    		  you:

```
Response Code: 204
```

Request Body: enable allow transfers to numbers not associated with
                                    		  users or call handlers

```
<Greeting>
  <IgnoreDigits>false</IgnoreDigits>
  <EnableTransfer>true</EnableTransfer>
</Greeting>
```

The following is the response from the *PUT* request to enable allow
                                    		  transfers to numbers not associated with users or call handlers and the actual
                                    		  response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

```
PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Alternate
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

```
{
  "EnableTransfer":"true","IgnoreDigits":"false"
}
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

#### Changing after
                              	 Greeting Actions

By default all the handlers must have tenant specific handlers

Example 1: Change Call Actions

```
Request Body:
<UserTemplateGreeting>
    <AfterGreetingAction>8</AfterGreetingAction>
</UserTemplateGreeting>
```

The following is the response from the *PUT* request and the actual
                                    		  response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To change call actions, do the following:

```
PUT https://<connection-server>/vmrest/callhandlerprimarytemplates/6bcd837d-f1cf-43c2-b199-85b457858a16/usertemplategreetings/Alternate
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

```
Request Body:
{

   "AfterGreetingAction":"8"

}
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

Example 2: Change Call Handler

```
Request Body:
<UserTemplateGreeting>
    <AfterGreetingAction>2</AfterGreetingAction>
    <AfterGreetingTargetConversation>PHTransfer</AfterGreetingTargetConversation>
    <AfterGreetingTargetHandlerObjectId>ee065a6a-3f95-4b4d-bbbd-98cb2d4c0aa9</AfterGreetingTargetHandlerObjectId>
</UserTemplateGreeting>
```

The following is the response from the *PUT* request and the actual
                                    		  response will depend upon the information given by you:

```
Response Code: 204
```

```
GET https://<connection-server>/vmrest/handlers/callhandlers
```

Example 3: Change Interview handler

```
Request Body:
<UserTemplateGreeting>
    <AfterGreetingAction>2</AfterGreetingAction>
    <AfterGreetingTargetConversation>PHInterview</AfterGreetingTargetConversation>
    <AfterGreetingTargetHandlerObjectId>2f6a0058-7535-48ac-abcd-c4b41d13f47e</AfterGreetingTargetHandlerObjectId>
</UserTemplateGreeting>
```

The following is the response from the *PUT* request and the actual
                                    		  response will depend upon the information given by you:

```
Response Code: 204
```

```
GET https://<connection-server>/vmrest/handlers/interviewhandler
```

Example 4: Change Directory handler

```
Request Body:
<UserTemplateGreeting>
    <AfterGreetingAction>2</AfterGreetingAction>
    <AfterGreetingTargetConversation>AD</AfterGreetingTargetConversation>
    <AfterGreetingTargetHandlerObjectId>1f1941a5-3bb7-47ee-96f9-78691cd8ad43</AfterGreetingTargetHandlerObjectId>
</UserTemplateGreeting>
```

The following is the response from the *PUT* request and the actual
                                    		  response will depend upon the information given by you:

```
Response Code: 204
```

```
GET https://<connection-server>/vmrest/handlers/directoryhandler
```

Example 5: Change Conversation

```
Request Body: for broadcast message administrator
<UserTemplateGreeting>
    <AfterGreetingAction>2</AfterGreetingAction>
    <AfterGreetingTargetConversation>BroadcastMessageAdministrator</AfterGreetingTargetConversation>
</UserTemplateGreeting>
```

The following is the response from the *PUT* request for broadcast
                                    		  message administrator and the actual response will depend upon the information
                                    		  given by you:

```
Response Code: 204
```

```
Request Body: for caller system transfer
<UserTemplateGreeting>

   <AfterGreetingAction>2</AfterGreetingAction>
   <AfterGreetingTargetConversation>SystemTransfer</AfterGreetingTargetConversation>

</UserTemplateGreeting>
```

The following is the response from the *PUT* request for caller system
                                    		  transfer and the actual response will depend upon the information given by you:

```
Response Code: 204
```

```
Request Body: for greeting administrator
<UserTemplateGreeting>

   <AfterGreetingAction>2</AfterGreetingAction>
   <AfterGreetingTargetConversation>GreetingsAdministrator</AfterGreetingTargetConversation>

</UserTemplateGreeting>
```

The following is the response from the *PUT* request for greeting
                                    		  administrator and the actual response will depend upon the information given by
                                    		  you:

```
Response Code: 204
```

```
Request Body: for sign in
<UserTemplateGreeting>

   <AfterGreetingAction>2</AfterGreetingAction>
   <AfterGreetingTargetConversation>SubSignIn</AfterGreetingTargetConversation>

</UserTemplateGreeting>
```

The following is the response from the *PUT* request for sign in and
                                    		  the actual response will depend upon the information given by you:

```
Response Code: 204
Request Body: for user system transfer
<UserTemplateGreeting>
    <AfterGreetingAction>2</AfterGreetingAction>
    <AfterGreetingTargetConversation>SubSysTransfer</AfterGreetingTargetConversation>
</UserTemplateGreeting>
```

The following is the response from the *PUT* request for user system
                                    		  transfer and the actual response will depend upon the information given by you:

```
Response Code: 204
```

Example 6: Change user with Mailbox

```
<UserTemplateGreeting>
    <AfterGreetingAction>2</AfterGreetingAction>
    <AfterGreetingTargetConversation>PHTransfer</AfterGreetingTargetConversation>
    <AfterGreetingTargetHandlerObjectId>92a9008d-9e18-4cd1-8e3c-10df32295cd8</AfterGreetingTargetHandlerObjectId>
</UserTemplateGreeting>
```

The following is the response from the *PUT* request and the actual
                                    		  response will depend upon the information given by you:

```
Response Code: 204
```

#### Changing Caller
                              	 Option

```
<UserTemplateGreeting>
    <EnAltGreetDontRingPhone>true</EnAltGreetDontRingPhone>
    <EnAltGreetPreventSkip>true</EnAltGreetPreventSkip>
    <EnAltGreetPreventMsg>true</EnAltGreetPreventMsg>
</UserTemplateGreeting>
```

The following is the response from the *PUT* request and the actual
                                    		  response will depend upon the information given by you:

```
Response Code: 204
```

#### Creating
                              	 Greeting

The following URI can be used to
                                    		  add greetings:

```
POST https://<connection-
server>/vmrest/callhandlerprimarytemplates/<Callhandlerprimarytempl
atesObjectId>/usertemplategreetings/Alternate/greetingstreamfiles
```

The following is the response from the *POST* request and the actual
                                    		  response will depend upon the information given by you:

```
Response Code: 201
```

#### Save Video
                              	 Greetings

Unity Connection allows you to
                                    		  save video greetings using both GET and PUT requests.

Example of GET Request

```
GET http://<connection-server>/vmrest/Callhandlersprimarytemplates/<callhandlerobjectid>/usertemplates/Greetings/<GreetingType>/GreetingStreamFiles/<language>/video
```

The following is the response of the above GET command and the output
                                    		  may vary depending on your inputs.

```
Response: 200
<CallControl>
    <resourceId>aad91d6d-aeca-4a72-8069-b656efb3041f.wav</resourceId>
    <sessionId>570146ed1504cb1</sessionId>
</CallControl
```

JSON Example

```
Request 
GET  vmrest/handlers/callhandlers/30600b21-1a4c-47a3-a078-8078984e5376/greetings/Standard/greetingstreamfiles/1033/video
Accept: application/json
User-Agent: Java/1.6.0_17
Host: <connection-server>
Connection: keep-alive
authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg=
```

```
Response
HTTP/1.1 200
Content-Type: application/json
Date: Fri, 15 Jan 2010 15:14:11 GMT
Server:
{ “resourceId” :” aad91d6d-aeca-4a72-8069-b656efb3041f.wav”, “sessionId” : ”570146ed1504cb1”}
```

Example of PUT Request

```
PUT http://<connection-server>/vmrest/Callhandlersprimarytemplates/<callhandlerobjectid>/usertemplates/Greetings/<GreetingType>/GreetingStreamFiles/<language>/video
```

```
<CallControl>
     <resourceId>aad91d6d-aeca-4a72-8069-b656efb3041f.wav</resourceId>
     <sessionId>570146ed1504cb1</sessionId>
</CallControl>
```

```
Response: 204 OK
```

JSON Example

```
Request 
PUT  vmrest/handlers/callhandlers/30600b21-1a4c-47a3-a078-8078984e5376/greetings/Standard/greetingstreamfiles/1033/video
Content-Type: application/json
Accept: application/json
Host: <connection-server>
Connection: keep-alive
authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==

{ “resourceId” :” aad91d6d-aeca-4a72-8069-b656efb3041f.wav”, “sessionId” : ”570146ed1504cb1”}
```

```
Response :
HTTP/1.1 204
Content-Type: application/json
Date: Fri, 15 Jan 2010 15:14:11 GMT
Server:
```

#### Explanation of
                              	 Data Fields

Values can be:

- False: Caller
                                                         						  input enabled during greeting

- True: Caller
                                                         						  input ignored during greeting

Default Value: False

Default Value: 0 Default Values can be:

- Call handler - 1
                                                         						  (recording)

- Subscriber - 0
                                                         						  (system)

Default Value:2 Values can be:

- 0: Do wait
                                                         						  without receiving caller input and do not replay greeting.

- 1 or greater:
                                                         						  Wait this number of seconds without receiving any input from the caller before
                                                         						  playing the greeting again.

Default Value: 0 Values can be:

- 0: Do not
                                                         						  reprompt - Cisco Unity Connection will play the greeting once and then the
                                                         						  after-greeting action is taken.

- 1 or greater:
                                                         						  Number of times to reprompt.

Values can be:

- 1: Hang up

- 2. for other
                                                         						  actions with object id (call handler, interview handler, directory handler)

- 4. Take Message

- 6. Restart
                                                         						  greeting

- 8: Route from
                                                         						  next call routing rule.

Values can be:

- 0: System will
                                                         						  not play the "Record your message at the tone…" prompt prior to recording a
                                                         						  message.

- 1: System will
                                                         						  play the "Record your message at the tone…" prompt prior to recording a
                                                         						  message.

Default Value: 1

Default value: 0 Values can be:

- 0: User cannot
                                                         						  be transferred to another extension.

- 1: User can "be
                                                         						  transferred to another extension."

Values:

- true : Personal
                                                         						  Video Recording is enabled.

- false : Personal
                                                         						  Video Recording is not enabled.

Default value : false

Values:

- true : Callers
                                                         						  will be prompted with a tone before recording their video message.

- false : Callers
                                                         						  will not be prompted with a tone before recording their video message.

Default value : false

This flag is editable only when the flag
                                                   						EnablePersonalVideoRecording is set to True.

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- User Template Mailbox

### Updating Mailbox
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

### Updating Mailbox Store

Get the mailbox store object ID from the following URI:

```
GET https://<connection-server>/vmrest/voicemailboxstores
Request Body:
<UserTemplate>
    <MailboxStoreObjectId>9dfffae1-eae2-4eab-abe9-7b0773881d54</MailboxStoreObjectId>
</UserTemplates>
```

The following is the response from the *PUT* request and the actual response will depend upon the information given by you:

```
Response Code: 204
```

Input should be in bytes, that is multiple of 1024.

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- User Template Message
                        	 Settings

### User Template Message Settings

Administrator can use this API to create/update/delete/fetch the message settings. All the parameters of message settings
                                 are present in call handler primary template.

```
GET https://<connection server>/vmrestvmrest/usertemplates/<usertemplateobjectid>
```

From the above URI get the call handler primary template URI:

```
GET https://<connection-
    server>/vmrestvmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>
```

### Updating Message
                           	 Settings

The following is an example of
                                 		  the PUT request that updates message settings:

```
PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>
```

```
<Callhandler>
  <EditMsg>true</EditMsg>
  <MaxMsgLen>1000</MaxMsgLen>
  <AfterMessageAction>1</AfterMessageAction>
  <SendUrgentMsg>2</SendUrgentMsg>
  <UseCallLanguage>false</UseCallLanguage>
  <SendSecureMsg>false</SendSecureMsg
  <SendPrivateMsg>1</SendPrivateMsg>
  <PlayAfterMessage>2</PlayAfterMessage>
</Callhandler>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

```
PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

```
{
  "AfterMessageAction":"2",
  "AfterMessageTargetConversation":"SystemTransfer"
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response code: 204
```

### Updating after
                           	 Message Actions

Example 1: Call Handler

```
PUT
https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>
```

```
<Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>PHGreeting</AfterMessageTargetConversation>      
  <AfterMessageTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</AfterMessageTargetHandlerObjectId> 
</Callhandler>
```

The following is an example of the GET request that shows the call
                                 		  handler object ID:

```
GET https://<connection-server>/vmrest/handlers/callhandlers
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

Example 2: Interview Handler

```
<Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</AfterMessageTargetHandlerObjectId>
  <AfterMessageTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</AfterMessageTargetHandlerObjectId>
</Callhandler>
```

The following is an example of the GET request that shows the
                                 		  interview handler template object ID:

```
GET https://<connection-server>/vmrest/handlers/interviewhandlers
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

Example 3: Directory Handler

```
<Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>AD</AfterMessageTargetConversation>
  <AfterMessageTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</AfterMessageTargetHandlerObjectId>  
</Callhandler>
```

The following is an example of the GET request that shows the
                                 		  interview handler template object ID:

```
GET https://<connection-server>/vmrest/handlers/directoryhandlers
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

Example 4: Conversation

Request Body: for broadcast message administrator

```
<Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>BroadcastMessageAdministrator</AfterMessageTargetConversation>
</Callhandler>
```

The following is the response from the *PUT* request for broadcast
                                 		  message administrator and the actual response will depend upon the information
                                 		  given by you:

```
Response Code: 204
```

Request Body: for caller system transfer

```
<Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>SystemTransfer</AfterMessageTargetConversation>
</Callhandler>
```

The following is the response from the *PUT* request for caller system
                                 		  transfer and the actual response will depend upon the information given by you:

```
Response Code: 204
```

Request Body: for greeting administrator

```
<Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>GreetingAdministrator</AfterMessageTargetConversation>
</Callhandler>
```

The following is the response from the *PUT* request for greeting
                                 		  administrator and the actual response will depend upon the information given by
                                 		  you:

```
Response Code: 204
```

For sign in

```
<Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>SubSignIn</AfterMessageTargetConversation>
</Callhandler>
```

The following is the response from the *PUT* request for sign in and
                                 		  the actual response will depend upon the information given by you:

```
Response Code: 204
```

For system transfer:

```
Request Body:
<CallhandlerPrimaryTemplate>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>SubSysTransfer</AfterMessageTargetConversation>
</CallhandlerPrimaryTemplate>
```

The following is the response from the *PUT* request for user system
                                 		  transfer and the actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

```
PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive
Request Body:
{
  "AfterMessageAction":"2",
  "AfterMessageTargetConversation":"SystemTransfer"
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Explanation of Data Fields

Parameter

Ojects

Data Type

Comments

MaxMsgLen

Integer

Read/Write

The maximum recording length (in seconds) for messages left by unidentified callers.

Default value : 300 Range: 1-3600

EditMsg

Boolean

Read/Write

Allows callers to be prompted to listen to, add to, rerecord, or delete their messages.

Values can be:

False: Callers cannot edit messages

True: Callers can edit messages

Default value: True

UseDefaultLanguage

Boolean

Read/Write

Values can be:

False: The language is the default language defined for the call handler template.

True: The language is derived from the location to which this call handler template belongs.

Default value: False

UseCallLanguage

Boolean

Read/Write

This flag allows that language to be the language used by handlers in the system to play prompts for users.

Values can be:

False: Do not use the language specified by the system call routing rule to play prompts for users

True: Use the language specified by the system call routing rule to play prompts for users

Default value: False

SendUrgentMsg

Integer

Read/Write

A flag indicating whether an unidentified caller can mark a message as "urgent."

Values can be:

0: Never - messages left by unidentified calls are never marked urgent.

1: Always - all messages left by unidentified callers are marked urgent.

2: Ask - Cisco Unity Connection asks unidentified callers whether to mark their messages urgent.

SendPrivateMsg

Integer

Read/Write

Determines if an outside caller can mark their message as private.

Values can be:

0: Never - No messages are marked private.

1: Always - All messages are marked private.

2: Ask - Ask the outside caller if they wish to mark the message as private.

SendSecureMsg

Boolean

Read/Write

A flag indicating whether an unidentified caller can mark a message as "secure."

Values can be:

0: Never - messages left by unidentified calls are never marked secure.

1: Always - all messages left by unidentified callers are marked secure.

PlayAfterMessage

Integer

Read/Write

Indicates whether the Sent Message Prompt Recording referenced by Post Greeting

Values can be:

0: Do not play recording

1: System default recording

2: Play recording

AfterMessageAction

Integer

Read/Write

AfterMessageAction can only accept integer with value 1 or 8 or 2

Values can be:

1: Hang up

8: Route from next call routing rule.

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Message Action Template

### Message Action Template

To edit a message action template, you must get the URI for message action from:

```
GET https://<connection server>/vmrestvmrest/usertemplates/<usertemplateobjectid>
```

Message action URI:

```
GET https://<connection 
server>/vmrestvmrest/usertemplates/<usertemplateobjectid>/usertemplatemessageactions/<usertempl
atemessageactionsobjectid>
```

### Updating Message Action

```
Request URI
PUT https://<connection server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplatemessageactions/<objectid>
Request Body:
<UserTemplateMessageAction>
    <VoicemailAction>3</VoicemailAction>
    <RelayAddress>%texoma%@tenant.com</RelayAddress> 
</UserTemplateMessageAction>
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                 by you:

```
Response Code: 204
```

JSON Example

To update message actions, do the following:

```
Request URI:
PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplatemessageactions/<objectid>
Accept: application/json
Content-type: application/json
Connection: keep-alive
Request Body:
{
    "VoicemailAction":"3"
    "RelayAddress":"texoma@tenant.com"
}
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                 by you:

```
Response Code: 204
```

For relay message and accept and relay message option relay address is mandatory and relay address must be correct for e.g.:
                                             tenant@cisco.com In the same way all other actions can be edited like: Voicemail Action, Email Action, Fax Action and Delivery
                                             Receipt Action

### Explanation of Data Fields

Parameter

Data Types

Operation

Comments

VoicemailAction

Integer

Read/Write

The action to take for voicemail messages.

Values can be:

0: Reject the Message

1: Accept the Message

2: Relay the Message

3: Accept and Relay the Message

For 2 and 3, values have to provide RelayAddress.

EmailAction

Integer

Read/Write

The action to take for email messages.

Values can be:

0: Reject the Message

1: Accept the Message

2: Relay the Message

3: Accept and Relay the Message

For 2 and 3, values have to provide RelayAddress.

FaxAction

Integer

Read/Write

The action to take for fax messages.

Values can be:

0: Reject the Message

1: Accept the Message

2: Relay the Message

3: Accept and Relay the Message

For 2 and 3, values have to provide RelayAddress.

DeliveryReceiptAction

Integer

Read/Write

The action to take for delivery receipt messages.

Values can be:

0: Reject the Message

1: Accept the Message

2: Relay the Message

3: Accept and Relay the Message

For 2 and 3, values have to provide RelayAddress.

RelayAddress

String (320)

Read/Write

Select the address to which system relays voicemail, email, fax, or delivery receipts when Connection is configured to relay
                                             that message type. This field is not editable unless you have selected Relay the Message or Accept and Relay the Message as
                                             the message action for one or more message types.

In order to configure Connection to relay messages, you must first configure an SMTP Smart Host on the System Settings > SMTP
                                                         Configuration > Smart Host page. Enter a combination of text and tokens that Connection replaces with a value from the user
                                                         profile. (For example, Connection replaces %Alias% with the alias from each user profile when editing the corresponding user.)

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- User Template Notification
                        	 Devices

### User Template Notification Devices

The following URI can be used to view the user template object ID:

```
GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>
```

From the above URI, get the notification devices object ID:

```
https://<connectionserver>/vmrest/usertemplates/<usertemplateobjectid>/usertemplatenotificationdevices
```

### Pager

The following URI can be used to view the pager device by using user template notification device object ID:

```
GET https://<connection-
    server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplatenotificationdevices/usertemplatepagerdevic
    es/<usertemplatenotificationdeviceobjectId>
Request Body: Updating Pager
<UserTemplatePagerDevice>
    <Active>true</Active>    
    <DisplayName>Pager1</DisplayName>
    <InitialDelay>1</InitialDelay>
    <RepeatNotify>true</RepeatNotify> 
    <RepeatInterval>1</RepeatInterval>
    <EventList>AllMessage</EventList> 
    <RetriesOnBusy>4</RetriesOnBusy>
    <BusyRetryInterval>5</BusyRetryInterval>
    <RetriesOnRna>4</RetriesOnRna>
    <RnaRetryInterval>15</RnaRetryInterval>
    <RetriesOnSuccess>0</RetriesOnSuccess>
</UserTemplatePagerDevice>
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                 by you:

```
Response Code: 204
```

To activate notification device <PhoneNumber> parameter is mandatory and <RepeatInterval > parameter is mandatory to enable
                                             repeat notify. The provide values can be changed and values are given in above table.

JSON Example

To view pager devices, do the following:

```
GET https://<connectionserver>/vmrestvmrest/usertemplates/<usertemplateobjectid>/usertemplatenotificationdevices/
usertemplatepagerdevices/<usertemplatenotificationdeviceobjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                 by you:

```
{
    "URI":"/vmrest/usertemplates/6164ac2d-e8ec-441a-93a0-95f8e18a655c/usertemplatenotificationdevices/usertemplatepagerdevices/ad6bdb87-7ab6-4a2a-b4fb-5dae6fd6804c"
    "TransmitForcedAuthorizationCode":"false"
    "BusyRetryInterval":"5"
    "DialDelay":"1"
    "RetriesOnBusy":"4"
    "RetriesOnRna":"4"
    "RingsToWait":"4"
    "RnaRetryInterval":"15"
    "SendCount":"true"
    "WaitConnect":"true"
    "MediaSwitchObjectId":"0ad0b88c-4a70-4cf7-913e-d5d7a921caca"
    "PhoneSystemURI":"/vmrest/phonesystems/0ad0b88c-4a70-4cf7-913e-d5d7a921caca"
    "ObjectId":"ad6bdb87-7ab6-4a2a-b4fb-5dae6fd6804c"
    "Active":"false"
    "DeviceName":"Pager"
    "DisplayName":"Pager"
    "MaxBody":"512"
    "MaxSubject":"64"
    "SubscriberObjectId":"6164ac2d-e8ec-441a-93a0-95f8e18a655c"
    "UserURI":"/vmrest/users/6164ac2d-e8ec-441a-93a0-95f8e18a655c"
    "SendCallerId":"true"
    "Undeletable":"true"
    "SuccessRetryInterval":"1"
    "RetriesOnSuccess":"0"
    "EventList":"NewVoiceMail"
    "ScheduleSetObjectId":"5fc5a5d7-eaf6-4f4d-80cf-f76f3893ac0e"
    "InitialDelay":"0"
    "RepeatInterval":"0"
    "RepeatNotify":"false"
}
```

```
Response Code: 200
```

#### Explanation of Fields: Pager

Parameter

Data Type

Operation

Comments

Active

Boolean

Read/Write

Enable notification device.

Default value: False

DisplayName

String

Read/Write

Name of notification device

DeviceName

String

Read Only

Device name of notification device which can’t be changed.

FailDeviceObjectId

String

Read/Write

Have to provide notification device object id.

To move back to “Do nothing option”, don’t provide any object Id in this parameter.

EventList

String

Read/Write

Values can be:

All messages: AllMessage

All message urgent only: AllUrgentMessage

All Voice messages: NewVoiceMail

All voice message urgent only: NewUrgentVoiceMai

Dispatch messages: DispatchMessage

Dispatch message urgent only: UrgentDispatchMessage

Fax messages: NewFax

Fax messages urgent only: NewUrgentFax

All voice messages and fax message urgent only: NewUrgentFax,NewVoiceMail

All voice message urgent only and fax message: NewUrgentFax,NewUrgentVoiceMail

Fax message and all voice message: NewFax,NewVoiceMail

PhoneNumber

Integer

Read/Write

To activate notification device phone number is mandatory.

AfterDialDigits

String (32)

Read/Write

The extra digits (if any) that Cisco Unity Connection will dial after the phone number. For numeric pagers, the extra digits
                                                are shown on the pager display.

DialDelay

Integer

InitialDelay

Integer

Read/Write

The amount of time (in minutes) from the time a message is received until the message notification triggers (if the message
                                                matches the criteria).

Default Value: 0 Range: 0-120

RingsToWait

Integer

Read/Write

The number of rings Cisco Unity Connection will wait before hanging up if the device does not answer.

Default value: 4 Range: 1-100

RetriesOnBusy

Integer

Read/Write

The number of times Cisco Unity Connection will retry the notification device if it is busy.

Default value: 4 Range: 0-100

BusyRetryInterval

Integer

Read/Write

The amount of time (in minutes) Cisco Unity Connection will wait between tries if the device is busy.

Default value: 5 Range: 1-100

RetriesOnRna

Integer

Read/Write

The number of times Cisco Unity Connection will retry the notification device if the device does not answer.

Default value: 4 Range: 0-100

RnaRetryInterval

Integer

Read/Write

The amount of time (in minutes) Cisco Unity Connection will wait between tries if the device does not answer.

Default value: 15 Range: 1-100

RetriesOnSuccess

Integer

Read/Write

The number of times Cisco Unity Connection will retry the notification device if it is successful.

Default value: 0 Range: 0-100

SuccessRetryInterval

Integer

Read/Write

The amount of time (in minutes) Cisco Unity Connection will wait between tries if the device is successful.

Default value: 1 Range: 1-100

MediaSwitchObjectid

String

Read/Write

The unique identifier of the MediaSwitch objects to use for notification.

### Phone Devices

Phone devices are of 3 types: work phone, home phone and mobile phone. You have to provide phone device object id to edit
                                 any of the 3 devices. All the parameters are same as of pager except 1. That is <PromptForId>true</PromptForId>. The following
                                 URI can be used to view the phone device using user template notification object ID:

```
GET https://<connection-
    server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplatenotificationdevices/usertemplatephonedevic
    es/<usertemplatenotificationdeviceobjectId>
```

### HTML Devices

The following URI can be used to view the html devices using user template notification object ID:

```
GET https://<connection-
    server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplatenotificationdevices/usertemplatehtmldevic
    es/<usertemplatenotificationdeviceobjectId>
Request Body: To update an HTML Device
<UserTemplateHtmlDevice>
    <Active>truee</Active>   
    <SmtpAddress>tenant@cisco.com</SmtpAddress>
    <DisableMobileNumberFromPCA>false</DisableMobileNumberFromPCA>
    <HeaderText>erwr</HeaderText>
</UserTemplateHtmlDevice>
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                 by you:

```
Response Code: 204
```

To activate the SmtpAddress parameter is mandatory.

#### Explanation of Fields: HTML Device

Parameter

Data Type

Operation

Comment

DeviceName

String

Read/Write

Device name of HTML notification device.

EventList

String

Read/Write

By default it is NewVoiceMail.

SmtpAddress

String

Read/Write

SMTP address to be notified.

NotificationTemplateID

String

Read/Write

HTML notification templates.

DisableMobileNumberFromPCA

Boolean

Read/Write

Disable Outdial Number From Cisco PCA.

Default value: False

CallbackNumber

Integer

Read/Write

Outdial number.

DisableTemplateSelectionFromPCA

Boolean

Read/Write

Disable HTML Template selection From Cisco PCA.

Default value: False

### SMTP Devices

The following URI can be used to view the SMTP devices using user template notification object ID:

```
GET https://<connection server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplatenotificationdevices/usertemplatesmtpdevices/<usertemplatenotificationdeviceobjectId>
Request Body: SMTP Devices
<UserTemplateSmtpDevice>
<StaticText>ritu</StaticText>
<Active>true</Active>
<DeviceName>SMTP</DeviceName>
 <SendCallerId>false</SendCallerId>
<SendPcaLink>true</SendPcaLink>
<Undeletable>true</Undeletable>
<HeaderText>erwr</HeaderText>
<FooterText>efs</FooterText>
<EventList>AllMessage, CalendarAppointment,CalendarMeeting</EventList>
</UserTemplateSmtpDevice>
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                 by you:

```
Response Code: 204
```

#### Explanation of fields: SMTP Devices

Parameter

Data Type

Operation

Comment

Active

Boolean

Read/Write

Enable SMTP notification device. SMTP address is mandatory to enable it.

Default value: False

SmtpAddress

String

Read/Write

SMTP address to be notified.

InitialDelay

Integer

Read/Write

Delay before the First Notification Attempt

RepeatNotify

Boolean

Read/Write

Repeat Notification if there are Still New Messages.

Default value: False

RepeatInterval

Integer

Read/Write

Notification Repeat Interval

EventList

String

Read/Write

Values can be:

All messages: AllMessage

All message urgent only: AllUrgentMessage

All Voice messages: NewVoiceMail

All voice message urgent only: NewUrgentVoiceMai

Dispatch messages: DispatchMessage

Dispatch message urgent only: UrgentDispatchMessage

Fax messages: NewFax

Fax messages urgent only: NewUrgentFax

All voice messages and fax message urgent only: NewUrgentFax,NewVoiceMail

All voice message urgent only and fax message: NewUrgentFax,NewUrgentVoiceMail

Fax message and all voice message: NewFax,NewVoiceMail

Calendar Appointment: CalendarAppointment

Calendar meeting: CalendarMeeting

PhoneNumbe

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

Message text

FooterText

String

Read/Write

Message footer

SendCallerId

Boolean

Read/Write

Include Message Information in Message Text.

Default value: True

SendCount

Boolean

Read/Write

Include Message Count in Message Text.

Default value: True

SendPcaLink

Boolean

Read/Write

Include a Link to the Cisco Unity Connection Web Inbox in Message Text.

Default value: False

### Creating a new Notification device

The following URI can be used to create a pager device:

```
POST https://<connection-
    server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplatenotificationdevic
    es/usertemplatepagerdevices
Request Body:
<UserTemplateNotificationDevice>
    <DisplayName>Newpager</DisplayName>
    <MediaSwitchObjectId>8adf6869-4afc-4455-9fd5-d05b68ca6630</MediaSwitchObjectId>
</UserTemplateNotificationDevice>
```

he following is the response from the above *POST* request and the actual response will depend upon the information given
                                 by you:

```
Response Code: 201
```

```
/vmrest/usertemplates/<objectid>/usertemplatenotificationdevices/<objectid>
```

Phone system Id is mandatory to create pager device.

## Cisco Unity Connection Provisioning Interface (CUPI) API -- User Template Phone Menu

### User Template Phone Menu

The following URI can be used to view the user template object ID:

```
GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>
```

### Updating Phone
                           	 menu fields

```
Request Body:
<UserTemplate>
    <PromptVolume>50</PromptVolume>
    <PromptSpeed>100</PromptSpeed>
    <IsClockMode24Hour>false</IsClockMode24Hour>
    <ConversationTui>SubMenu</ConversationTui>
    <MessageLocatorSortOrder>1</MessageLocatorSortOrder>
    <JumpToMessagesOnLogin>false</JumpToMessagesOnLogin>
</UserTemplate>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Updating
                           	 Conversation fields

Example 1: Edit call actions

```
<User>
  <ExitAction>1</ExitAction>
</User>
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

Example 2: Edit call handler

```
<User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>PHTransfer</ExitTargetConversation>
  <ExitTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</ExitTargetHandlerObjectId>
</User>
```

The following URI can be used to view call handler template object ID:

```
GET https://<connection-server>/vmrest/handlers/callhandlers
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

Example 3: Interview handler

```
<User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>PHInterview</ExitTargetConversation>
  <ExitTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</ExitTargetHandlerObjectId>
</User>
```

The following is an example of the GET request that shows the
                                 		  interview handler template object ID:

```
GET https://<connection-server>/vmrest/handlers/interviewhandlers
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

Example 4: Directory handler

The following is an example of the GET request that shows the
                                 		  directory handler template object ID:

```
GET https://<connection-server>/vmrest/handlers/directoryhandlers
```

```
<User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>AD</ExitTargetConversation>
  <ExitTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</ExitTargetHandlerObjectId> 
</User>
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

Example 5: Conversation

Request Body: for broadcast message administrator

```
<User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>BroadcastMessageAdministrator</ExitTargetConversation>
</UserTemplate>
```

The following is the response from the *PUT* request for broadcast
                                 		  message administrator and the actual response will depend upon the information
                                 		  given by you:

```
Response Code: 204
```

Request Body: for caller system transfer

```
<User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>SystemTransfer</ExitTargetConversation>
</User>
```

The following is the response from the *PUT* request for caller system
                                 		  transfer and the actual response will depend upon the information given by you:

```
Response Code: 204
```

Request Body: for greeting administrator

```
<User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>GreetingAdministrator</ExitTargetConversation>
</User>
```

The following is the response from the *PUT* request for greeting
                                 		  administrator and the actual response will depend upon the information given by
                                 		  you:

```
Response Code: 204
```

Request Body: for sign in

```
<UserTemplate>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>SubSignIn</ExitTargetConversation>
</UserTemplate>
```

The following is the response from the *PUT* request for sign in and
                                 		  the actual response will depend upon the information given by you:

```
Response Code: 204
```

Request Body: for user system transfer

```
<User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>SubSysTransfer</ExitTargetConversation>
</User>
```

The following is the response from the *PUT* request for user system
                                 		  transfer and the actual response will depend upon the information given by you:

```
Response Code: 204
```

Example 6: Users with Mailbox

```
<User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>PHTransfer</ExitTargetConversation> 
  <ExitTargetHandlerObjectId>71cb381b-fd16-4ba8-8a1d-e71684e57b0e</ExitTargetHandlerObjectId>
</User>
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example To set exit action, do the following:

```
PUT https://<connection-server>/vmrest/users/<userobjectid>
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

```
{
  "ExitAction":"2",
  "ExitTargetConversation":"SubSysTransfer"
}
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

### Explanation of Data Fields

- False: Full

- 50: Medium

- 100: High

- 100: Normal

- 150: Fast

- 200: Fastest

- False: 12-Hour Clock (12:00 AM - 11:59 PM)

- SubMenu_Alternate_Custom: Custom keypad mapping1

- SubMenu_Alternate_Custom1: Custom keypad mapping1

- SubMenu_AlternateN: Alternate Keypad Mapping(N)

- SubMenu_AlternateS: Alternate Keypad Mapping(S)

- SubMenu_AlternateX: Alternate Keypad Mapping (X)

- SubMenuOpt1: Optional conversation1

- SubMenu_AlternateI: Standard Conversation

- 2: First In, First Out

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Playback Message
                        	 Settings

### Playback Message
                           	 Settings

The following URI can be used to
                                 		  view the user template object ID:

```
GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>
```

#### Edit
                              	 Parameters

```
Request Body:
<UserTemplate>
    <Volume>50</Volume>
    <Speed>100</Speed>
    <SayTotalNew>true</SayTotalNew>
    <SayTotalNewVoice>true</SayTotalNewVoice>
    <SayTotalNewEmail>false</SayTotalNewEmail>
    <SayTotalNewFax>false</SayTotalNewFax>
    <SayTotalReceipts>false</SayTotalReceipts>
    <SayTotalSaved>true</SayTotalSaved>
    <SayTotalDraftMsg>false</SayTotalDraftMsg>
    <MessageTypeMenu>false</MessageTypeMenu>
    <NewMessageSortOrder>2</NewMessageSortOrder>
    <SaveMessageOnHangup>1</SaveMessageOnHangup>
    <DeletedMessageSortOrder>1</DeletedMessageSortOrder>
    <SaySender>true</SaySender>
    <SaySenderExtension>false</SaySenderExtension> 
    <SayAni>true</SayAni>
    <SayMsgNumber>true</SayMsgNumber>
    <SayTimestampBefore>true</SayTimestampBefore>
    <AutoAdvanceMsgs>false</AutoAdvanceMsgs>
    <ConfirmDeleteMessage>true</ConfirmDeleteMessage>
</UserTemplate>
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

- for new message:
                                                      				  <NewMessageSortOrder>2</NewMessageSortOrder>

- for saved message:
                                                      				  <SaveMessageSortOrder>1</SaveMessageSortOrder>

- for deleted message:
                                                      				  <DeletedMessageSortOrder>1</DeletedMessageSortOrder>

All the possible values for above three parameters are given in the
                                    		  table.

#### Explanation of
                              	 Data Fields

Possible values:

- 25: Low

- 50: Medium

- 100: High

Default value: 50

- 50: Slow

- 100: Normal

- 150: Fast

- 200: Fastest

Default value: 100

Possible Values:

- false: New

- true: Saved

Default Value: false

Possible values:

- 1: Newest First

- 2: Oldest First

Default Value: 1

Possible values:

- 1: Newest First

- 2: Oldest First

Default Value: 2

Possible values:

- 1: Newest First

- 2: Oldest First

Default Value: 2

## Cisco Unity Connection Provisioning Interface (CUPI) API -- User Template Post Greeting Recordings

### User Template Post
                           	 Greeting Recordings

The following URI can be used to
                                 		  view the user template object ID:

```
GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>
```

From the above UR, get the call handler primary template object ID:

```
GET https://<connection-server>/vmrestvmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>
```

### Update Post
                           	 Greeting Recording Settings

```
Request Body:
<CallhandlerPrimaryTemplate>
    <PlayPostGreetingRecording>1</PlayPostGreetingRecording>
</CallhandlerPrimaryTemplate>
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To update post greeting recording settings, do the following:

```
Request URI:
PUT https://<connection-server>/vmrest/callhandlerprimarytemplates/<ObjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive
Request Body:
{
    "PlayPostGreetingRecording":"1"
}
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

### Explanation of Data Fields

- 0: Do Not Play Recording

- 1: Play Recording to All Callers

- 2: Play Recording Only to Unidentified Callers

Object Id of post greeting.

## Cisco Unity Connection Provisioning Interface (CUPI) API -- Send Message Settings

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- User Template Transfer
                        	 Rules

### Transfer Rules
                           	 API

Administrator can use this API to
                                 		  create/update/delete/fetch the transfer rules. Various attributes of transfer
                                 		  rules can also be updated using this API. The following are the examples to
                                 		  access various types of transfer rules:

To view call handler primary
                                       				templates of a particular user template use the URI:

```
GET https://<connection-server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>
```

From call handler primary template use the URI to view transfer
                                       				options:

```
vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/transferoptions
```

To view the alternate transfer rule use the URI:

```
GET https://<connection-server>/vmrestvmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/transferoptions/Alternate
```

To view closed transfer rule use the URI:

```
GET https://<connection-server>/vmrestvmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/transferoptions/Off%20Hours
```

To view standard transfer rule use the URI:

```
GET https://<connection-server>/vmrestvmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/transferoptions/Standard
```

#### Viewing the
                              	 Alternate Transfer Rule

The following is an example of
                                    		  the GET request that lists the details of alternate transfer rule:

```
GET https://<connection-server>/vmrestvmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/transferoptions/Alternate
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<TransferOption>
<URI>/vmrest/callhandlerprimarytemplates/45e0a6f4-43c4-472a-8ffb-f6124aa549d0/transferoptions/Alternate</URI>
<CallHandlerObjectId>45e0a6f4-43c4-472a-8ffb-f6124aa549d0</CallHandlerObjectId>
<CallhandlerURI>/vmrest/callhandlerprimarytemplates/45e0a6f4-43c4-472a-8ffb-f6124aa549d0</CallhandlerURI>
<TransferOptionType>Alternate</TransferOptionType>
<Action>1</Action>
<RnaAction>1</RnaAction>
<TimeExpires>1972-01-01 00:00:00.0</TimeExpires>
<TransferAnnounce>false</TransferAnnounce>
<TransferConfirm>false</TransferConfirm>
<TransferDtDetect>false</TransferDtDetect>
<TransferHoldingMode>0</TransferHoldingMode>
<TransferIntroduce>false</TransferIntroduce>
<TransferRings>4</TransferRings>
<TransferScreening>false</TransferScreening>
<TransferType>0</TransferType>
<MediaSwitchObjectId>221ee752-5147-4326-9990-d4a138674f9e</MediaSwitchObjectId>
<PhoneSystemURI>/vmrest/phonesystems/221ee752-5147-4326-9990-d4a138674f9e</PhoneSystemURI>
<UsePrimaryExtension>true</UsePrimaryExtension>
<PlayTransferPrompt>true</PlayTransferPrompt>
<PersonalCallTransfer>false</PersonalCallTransfer>
<Enabled>false</Enabled>
</TransferOption>
```

```
Response Code: 200
```

JSON Example

To view the alternate transfer rule, do the following:

```
Request URI:
GET https://<connection-server>/vmrest/callhandlerprimarytemplates/<callhandlerprimarytemplatesobjectid>/transferoptions
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
"@total":"3"
"TransferOption":[
{
"URI":"/vmrest/callhandlerprimarytemplates/02dcae3e-2e7c-4997-a36e-0f5276281078/transferoptions/Alternate"
"CallHandlerObjectId":"02dcae3e-2e7c-4997-a36e-0f5276281078"
"CallhandlerURI":"/vmrest/callhandlerprimarytemplates/02dcae3e-2e7c-4997-a36e-0f5276281078"
"TransferOptionType":"Alternate"
"Action":"1"
"RnaAction":"1"
"TransferAnnounce":"false"
"TransferConfirm":"false"
"TransferDtDetect":"false"
"TransferHoldingMode":"0"
"TransferIntroduce":"false"
"TransferRings":"4"
"TransferScreening":"false"
"TransferType":"0"
"MediaSwitchObjectId":"7c654c70-e76c-4e47-b8f6-fa92cec6755e"
"PhoneSystemURI":"/vmrest/phonesystems/7c654c70-e76c-4e47-b8f6-fa92cec6755e"
"UsePrimaryExtension":"true"
"PlayTransferPrompt":"true"
"PersonalCallTransfer":"false"
"Enabled":"true"
}
{
"URI":"/vmrest/callhandlerprimarytemplates/02dcae3e-2e7c-4997-a36e-0f5276281078/transferoptions/Off%20Hours"
"CallHandlerObjectId":"02dcae3e-2e7c-4997-a36e-0f5276281078"
"CallhandlerURI":"/vmrest/callhandlerprimarytemplates/02dcae3e-2e7c-4997-a36e-0f5276281078"
"TransferOptionType":"Off Hours"
"Action":"1"
"RnaAction":"1"
"TransferAnnounce":"false"
"TransferConfirm":"false"
"TransferDtDetect":"false"
"TransferHoldingMode":"0"
"TransferIntroduce":"false"
"TransferRings":"4"
"TransferScreening":"false"
"TransferType":"0"
"MediaSwitchObjectId":"7c654c70-e76c-4e47-b8f6-fa92cec6755e"
"PhoneSystemURI":"/vmrest/phonesystems/7c654c70-e76c-4e47-b8f6-fa92cec6755e"
"UsePrimaryExtension":"true"
"PlayTransferPrompt":"true"
"PersonalCallTransfer":"false"
"Enabled":"true"
}
{
"URI":"/vmrest/callhandlerprimarytemplates/02dcae3e-2e7c-4997-a36e-0f5276281078/transferoptions/Standard"
"CallHandlerObjectId":"02dcae3e-2e7c-4997-a36e-0f5276281078"
"CallhandlerURI":"/vmrest/callhandlerprimarytemplates/02dcae3e-2e7c-4997-a36e-0f5276281078"
"TransferOptionType":"Standard"
"Action":"1"
"RnaAction":"1"
"TransferAnnounce":"false"
"TransferConfirm":"false"
"TransferDtDetect":"false"
"TransferHoldingMode":"0"
"TransferIntroduce":"false"
"TransferRings":"4"
"TransferScreening":"false"
"TransferType":"0"
"MediaSwitchObjectId":"7c654c70-e76c-4e47-b8f6-fa92cec6755e"
"PhoneSystemURI":"/vmrest/phonesystems/7c654c70-e76c-4e47-b8f6-fa92cec6755e"
"UsePrimaryExtension":"true"
"PlayTransferPrompt":"true"
"PersonalCallTransfer":"false"
"Enabled":"true"
}
]
}
```

```
Response Code: 200
```

#### Updating Transfer
                              	 Option

The following is an example of
                                    		  the GET request that updates the transfer option:

```
GET https://<connection-server>/vmrestvmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/transferoptions/Alternate
```

```
<TransferOption>
<Action>0</Action>
<TimeExpires>1972-01-01 00:00:00.0</TimeExpires>
<TransferAnnounce>false</TransferAnnounce>
<TransferConfirm>false</TransferConfirm>
<TransferHoldingMode>0</TransferHoldingMode>
<TransferIntroduce>false</TransferIntroduce>
<TransferRings>4</TransferRings>
<TransferScreening>false</TransferScreening>
<TransferType>0</TransferType>
</TransferOption>
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To update the transfer rule, do the following:

```
Request URI:
PUT https://<connection-server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/transferoptions/Alternate
Accept: application/json
Content-type: application/json
Connection: keep-alive
Request Body:
{
"Action":"1",
"TransferAnnounce":"false",
"TransferConfirm":"false",
"TransferHoldingMode":"0",
"TransferIntroduce":"false",
"TransferRings":"4",
"TransferScreening":"false",
"TransferType":"0"
}
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

Use the following code snippet to change action to "Enable with no end
                                    		  date":

```
<TransferOption>
<Enabled>true</Enabled>
<TimeExpires></TimeExpires>
</TransferOption>
```

#### Explanation of
                              	 Data Fields

Possible values:

- true

- false

Default value: false

Values can be:

- 0: Greeting

- 1: Extension

Values:

- 0: Release to Switch

- 1: Supervise Transfer

Applies only when the "TransferType" column is set to supervised (1). This value should never be less than 2 for a supervised
                                                transfer. Possible Values: 2-20 Default value: 4

Values:

- false: System will not play the "Wait while I transfer your call" prompt prior to transfer.

- true: System will play the "Wait while I transfer your call" prompt prior to transfer.

Default value: true

Applies only when the "TransferType" column is set to supervised (1). Values:

- 0: Send callers to voicemail.

- 1: Put callers on hold without asking.

- 2: Ask callers to hold.

Requires a "TransferType" of supervised (1). Values:

- false: Do not say "Transferring call" when the subscriber answers the phone

- true: Say "Transferring call" when the subscriber answers the phone

Default value: false

Requires a "TransferType" of supervised (1). This functionality is normally used when a single extension number is being shared
                                                by multiple subscribers or a scenario where the subscriber who is the message recipient takes calls for more than one dialed
                                                extension. The introduction alerts the subscriber who answers that the call is for the call handler. Default value: false

Requires a "TransferType" of supervised (1). Typically this is used in conjunction with the call screening option ("TransferScreening"
                                                column) enabled. This combination enables the subscriber to hear the name of the caller and then decide if they want to take
                                                the call or not. Values:

- false: Transfer confirm disabled

- true: Transfer confirm enabled

Default value: false

Normally this column is used along with "TransferConfirm" to allow the subscriber to screen calls. Values:

- false: Call screening disabled

- true: Ask and record caller name

Default value: false

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- User Template

### User Templates
                           	 API

Administrator can use this API to
                                 		  create/update/delete/fetch the user template. Various attributes of user
                                 		  template can also be updated using this API.

#### Listing the User
                              	 Templates

The request can be used to fetch
                                    		  the list of all user templates. It can also be used to fetch the list of user
                                    		  templates based on specific partition object ID, COS objec t ID, mailbox store
                                    		  object ID, phone system, call handler object ID.

```
GET https://<connection-server>/vmrest/usertemplates
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<UserTemplates total="1">
    <UserTemplate>
    <URI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-2b13f76bf631</URI>
    <ObjectId>c2056af2-bed7-4a0d-9039-2b13f76bf631</ObjectId>
    <TenantObjectId>fe6541fb-b42c-44f2-8404-ded14cbf7438</TenantObjectId>
    <UseDefaultLanguage>true</UseDefaultLanguage>
    <UseDefaultTimeZone>true</UseDefaultTimeZone>
    <Alias>Texoma_User_Template1</Alias>
    <City/>
    <State/>
    <Country>US</Country>
    <PostalCode/>
    <Manager/>
    <Building/>
    <Address/>
    <DisplayName>Texoma_User_Template1</DisplayName>
    <BillingId/>
    <TimeZone>190</TimeZone>
    <CreationTime>2012-12-26 13:04:28.9</CreationTime>
    <CosObjectId>0ef61610-a729-4b0d-9476-cab095028db3</CosObjectId>
    <CosURI>/vmrest/coses/0ef61610-a729-4b0d-9476-cab095028db3</CosURI>
    <Language>1033</Language>
    <LocationObjectId>27a67e01-bcb4-4012-8b1b-f0a08b736087</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/27a67e01-b
    cb4-4012-8b1b-f0a08b736087</LocationURI>
    <AddressMode>0</AddressMode>
    <ClockMode>0</ClockMode>
    <ConversationTui>SubMenu</ConversationTui>
    <GreetByName>true</GreetByName>
    <ListInDirectory>true</ListInDirectory>
    <IsVmEnrolled>true</IsVmEnrolled>
    <SayCopiedNames>true</SayCopiedNames>
    <SayDistributionList>true</SayDistributionList>
    <SayMsgNumber>true</SayMsgNumber>
    <SaySender>true</SaySender>
    <SayTimestampAfter>true</SayTimestampAfter>
    <SayTimestampBefore>false</SayTimestampBefore>
    <SayTotalNew>false</SayTotalNew>
    <SayTotalNewEmail>false</SayTotalNewEmail>
    <SayTotalNewFax>false</SayTotalNewFax>
    <SayTotalNewVoice>true</SayTotalNewVoice>
    <SayTotalReceipts>false</SayTotalReceipts>
    <SayTotalSaved>true</SayTotalSaved>
    <Speed>100</Speed>
    <MediaSwitchObjectId>b6df8cb3-b3ce-4797-84f3-5559049df8e8</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/b6df8cb3-b3ce-4797-84f3-
    5559049df8e8</PhoneSystemURI>
    <Undeletable>false</Undeletable>
    <UseBriefPrompts>false</UseBriefPrompts>
    <Volume>50</Volume>
    <EnAltGreetDontRingPhone>false</EnAltGreetDontRingPhone>
    <EnAltGreetPreventSkip>false</EnAltGreetPreventSkip>
    <EnAltGreetPreventMsg>false</EnAltGreetPreventMsg>
    <EncryptPrivateMessages>false</EncryptPrivateMessages>
    <DeletedMessageSortOrder>2</DeletedMessageSortOrder>
    <SayAltGreetWarning>false</SayAltGreetWarning>
    <SaySenderExtension>false</SaySenderExtension>
    <SayAni>false</SayAni>
    <ExitCallActionObjectId>0463e49b-cde4-4c30-877c-acfe25966a42</ExitCallActionObjectId> 
    <CallAnswerTimeout>4</CallAnswerTimeout>
    <CallHandlerObjectId>83c9b890-6659-4c0f-8be6-8a1a85efee7e</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/callhandlerprimarytemplates/83c9b890-6659-4c0f-8be6-8a1a85efee7e</CallhandlerURI>
    <DisplayNameRule>1</DisplayNameRule>
    <DoesntExpire>false</DoesntExpire>
    <CantChange>false</CantChange>
    <MailboxStoreObjectId>e983490d-78a5-45aa-b9a0-31f51460a5bd</MailboxStoreObjectId>
    <SavedMessageStackOrder>1234567</SavedMessageStackOrder>
    <NewMessageStackOrder>1234567</NewMessageStackOrder>
    <MessageLocatorSortOrder>1</MessageLocatorSortOrder>
    <SavedMessageSortOrder>2</SavedMessageSortOrder>
    <NewMessageSortOrder>1</NewMessageSortOrder>
    <MessageTypeMenu>false</MessageTypeMenu>
    <EnablePersonalRules>true</EnablePersonalRules>
    <RecordUnknownCallerName>true</RecordUnknownCallerName>
    <RingPrimaryPhoneFirst>false</RingPrimaryPhoneFirst>
    <PromptSpeed>100</PromptSpeed>
    <ExitAction>2</ExitAction>
    <ExitTargetConversation>PHGreeting</ExitTargetConversation>
    <ExitTargetHandlerObjectId>063956f9-c5ca-4e8b-be67-
    ff945a8a5d99</ExitTargetHandlerObjectId>
    <RepeatMenu>1</RepeatMenu>
    <FirstDigitTimeout>5000</FirstDigitTimeout>
    <InterdigitDelay>3000</InterdigitDelay>
    <PromptVolume>50</PromptVolume>
    <DelayAfterGreeting>0</DelayAfterGreeting>
    <AddressAfterRecord>false</AddressAfterRecord>
    <ConfirmDeleteMessage>false</ConfirmDeleteMessage>
    <ConfirmDeleteDeletedMessage>false</ConfirmDeleteDeletedMessage>
    <ConfirmDeleteMultipleMessages>true</ConfirmDeleteMultipleMessages>
    <IsClockMode24Hour>false</IsClockMode24Hour>
    <RouteNDRToSender>true</RouteNDRToSender>
    <NotificationType>0</NotificationType>
    <SendReadReceipts>1</SendReadReceipts>
    <ReceiveQuota>-2</ReceiveQuota>
    <SendQuota>-2</SendQuota>
    <WarningQuota>-2</WarningQuota>
    <IsSetForVmEnrollment>true</IsSetForVmEnrollment>
    <VoiceNameRequired>false</VoiceNameRequired>
    <SendBroadcastMsg>false</SendBroadcastMsg>
    <UpdateBroadcastMsg>false</UpdateBroadcastMsg>
    <ConversationVui>VuiStart</ConversationVui>
    <SpeechCompleteTimeout>0</SpeechCompleteTimeout>
    <SpeechIncompleteTimeout>750</SpeechIncompleteTimeout>
    <UseVui>false</UseVui>
    <SkipPasswordForKnownDevice>false</SkipPasswordForKnownDevice>
    <JumpToMessagesOnLogin>true</JumpToMessagesOnLogin>
    <EnableMessageLocator>false</EnableMessageLocator>
    <MessageAgingPolicyObjectId>6780a194-6efd-4311-819f-
    494a082bb093</MessageAgingPolicyObjectId>
    <MessageAgingPolicyURI>/vmrest/messageagingpolicies/6780a194-6efd-4311-819f-
    494a082bb093</MessageAgingPolicyURI>
    <AssistantRowsPerPage>5</AssistantRowsPerPage>
    <InboxMessagesPerPage>20</InboxMessagesPerPage>
    <InboxAutoRefresh>15</InboxAutoRefresh>
    <InboxAutoResolveMessageRecipients>true</InboxAutoResolveMessageRecipients>
    <PcaAddressBookRowsPerPage>5</PcaAddressBookRowsPerPage>
    <ReadOnly>false</ReadOnly>
    <EnableTts>true</EnableTts>
    <ConfirmationConfidenceThreshold>60</ConfirmationConfidenceThreshold>
    <AnnounceUpcomingMeetings>60</AnnounceUpcomingMeetings>
    <SpeechConfidenceThreshold>40</SpeechConfidenceThreshold>
    <SpeechSpeedVsAccuracy>50</SpeechSpeedVsAccuracy>
    <SpeechSensitivity>50</SpeechSensitivity>
    <EnableVisualMessageLocator>false</EnableVisualMessageLocator>
    <ContinuousAddMode>false</ContinuousAddMode>
    <NameConfirmation>false</NameConfirmation>
    <CommandDigitTimeout>1500</CommandDigitTimeout>
    <SaveMessageOnHangup>false</SaveMessageOnHangup>
    <SendMessageOnHangup>1</SendMessageOnHangup>
    <SkipForwardTime>5000</SkipForwardTime>
    <SkipReverseTime>5000</SkipReverseTime>
    <UseShortPollForCache>false</UseShortPollForCache>
    <SearchByExtensionSearchSpaceObjectId>2e0da21b-54e4-4b51-9f09-
    960049a5e806</SearchByExtensionSearchSpaceObjectId>
    <SearchByExtensionSearchSpaceURI>/vmrest/searchspaces/2e0da21b-54e4-4b51-9f09-
    960049a5e806</SearchByExtensionSearchSpaceURI>
    <SearchByNameSearchSpaceObjectId>2e0da21b-54e4-4b51-9f09-960049a5e806</SearchByNameSearchSpaceObjectId>
    <SearchByNameSearchSpaceURI>/vmrest/searchspaces/2e0da21b-54e4-4b51-9f09-960049a5e806</SearchByNameSearchSpaceURI>
    <PartitionObjectId>c6ff147e-c32c-4ade-8f12-46427c795c21</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/c6ff147e-c32c-4ade-8f12-46427c795c21</PartitionURI>
    <UseDynamicNameSearchWeight>false</UseDynamicNameSearchWeight>
    <LdapType>0</LdapType>
    <EnableMessageBookmark>false</EnableMessageBookmark>
    <SayTotalDraftMsg>false</SayTotalDraftMsg>
    <EnableSaveDraft>false</EnableSaveDraft>
    <RetainUrgentMessageFlag>false</RetainUrgentMessageFlag>
    <SayMessageLength>false</SayMessageLength>
    <CreateSmtpProxyFromCorp>false</CreateSmtpProxyFromCorp>
    <AutoAdvanceMsgs>false</AutoAdvanceMsgs>
    <SaySenderAfter>false</SaySenderAfter>
    <SaySenderExtensionAfter>false</SaySenderExtensionAfter>
    <SayMsgNumberAfter>false</SayMsgNumberAfter>
    <SayAniAfter>false</SayAniAfter>
    <SayMessageLengthAfter>false</SayMessageLengthAfter>
    <UserTemplateRolesURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-
    2b13f76bf631/usertemplateroles</UserTemplateRolesURI>
    <UserTemplateNotificationDevicesURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-2b13f76bf631/usertemplatenotificationdevices</UserTemplateNotificationDevicesURI>
    <TemplateExternalServiceAccountsURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-2b13f76bf631/templateexternalserviceaccounts</TemplateExternalServiceAccountsURI>
    <UserTemplateWebPasswordURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-90392b13f76bf631/credential/password</UserTemplateWebPasswordURI>
    <UserTemplateVoicePinURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-
    2b13f76bf631/credential/pin</UserTemplateVoicePinURI>
    <UserTemplateMessageActionURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-
    2b13f76bf631/usertemplatemessageactions</UserTemplateMessageActionURI>
</UserTemplate>
</UserTemplates>
```

```
Response Code: 200
```

JSON Example

To view the list of user templates, do the following:

```
Request URI:
GET https://<connection-server>/vmrest/usertemplates
Accept: application/json
Content_type: application/json
Connection: keep_alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
  "@total":"1"
  "UserTemplate":\[
  {
    "URI":"/vmrest/usertemplates/6164ac2d-e8ec-441a-93a0-95f8e18a655c"
    "ObjectId":"6164ac2d-e8ec-441a-93a0-95f8e18a655c"
    "TenantObjectId": "fe6541fb-b42c-44f2-8404-ded14cbf7438"
    "UseDefaultLanguage":"true"
    "UseDefaultTimeZone":"true"
    "Alias":"voicemailusertemplate"
    "DisplayName":"Voice Mail User Template"
    "TimeZone":"190"
    "CreationTime":"2013-02-25T09:39:25Z"
    "CosObjectId":"0b59d616-6434-443a-95aa-00b9d7315d54"
    "CosURI":"/vmrest/coses/0b59d616-6434-443a-95aa-00b9d7315d54"
    "Language":"1033"
    "LocationObjectId":"cff1347e-87af-4409-bead-d1970625f82e"
    "LocationURI":"/vmrest/locations/connectionlocations/cff1347e-87af-4409-bead-d1970625f82e"
    "AddressMode":"0"
    "ClockMode":"0"
    "ConversationTui":"SubMenu"
    "GreetByName":"true"
    "ListInDirectory":"true"
    "IsVmEnrolled":"true"
    "SayCopiedNames":"true"
    "SayDistributionList":"true"
    "SayMsgNumber":"true"
    "SaySender":"true"
    "SayTimestampAfter":"true"
    "SayTimestampBefore":"false"
    "SayTotalNew":"false"
    "SayTotalNewEmail":"false"
    "SayTotalNewFax":"false"
    "SayTotalNewVoice":"true"
    "SayTotalReceipts":"false"
    "SayTotalSaved":"true"
    "Speed":"100"
    "MediaSwitchObjectId":"0ad0b88c-4a70-4cf7-913e-d5d7a921caca"
    "PhoneSystemURI":"/vmrest/phonesystems/0ad0b88c-4a70-4cf7-913e-d5d7a921caca"
    "Undeletable":"true"
    "UseBriefPrompts":"false"
    "Volume":"50"
    "EnAltGreetDontRingPhone":"false"
    "EnAltGreetPreventSkip":"false"
    "EnAltGreetPreventMsg":"false"
    "EncryptPrivateMessages":"false"
    "DeletedMessageSortOrder":"2"
    "SayAltGreetWarning":"false"
    "SaySenderExtension":"false"
    "SayAni":"false"
    "ExitCallActionObjectId":"38f2eab0-a78c-49a2-8aee-ff562844d5db"
    "CallAnswerTimeout":"4"
    "CallHandlerObjectId":"6bcd837d-f1cf-43c2-b199-85b457858a16"
    "CallhandlerURI":"/vmrest/callhandlerprimarytemplates/6bcd837d-f1cf-43c2-b199-
    85b457858a16"
    "DisplayNameRule":"1"
    "DoesntExpire":"false"
    "CantChange":"false"
    "MailboxStoreObjectId":"02089c75-e8a2-4724-a570-9bed7768e716"
    "SavedMessageStackOrder":"1234567"
    "NewMessageStackOrder":"1234567"
    "MessageLocatorSortOrder":"1"
    "SavedMessageSortOrder":"2"
    "NewMessageSortOrder":"1"
    "MessageTypeMenu":"false"
    "EnablePersonalRules":"true"
    "RecordUnknownCallerName":"true"
    "RingPrimaryPhoneFirst":"false"
    "PromptSpeed":"100"
    "ExitAction":"2"
    "ExitTargetConversation":"PHGreeting"
    "ExitTargetHandlerObjectId":"1e0bc010-d9aa-4e1a-b001-a1b40f028d4f"
    "RepeatMenu":"1"
    "FirstDigitTimeout":"5000"
    "InterdigitDelay":"3000"
    "PromptVolume":"50"
    "DelayAfterGreeting":"0"
    "AddressAfterRecord":"false"
    "ConfirmDeleteMessage":"false"
    "ConfirmDeleteDeletedMessage":"false"
    "ConfirmDeleteMultipleMessages":"true"
    "IsClockMode24Hour":"false"
    "RouteNDRToSender":"true"
    "NotificationType":"0"
    "SendReadReceipts":"1"
    "ReceiveQuota":"-2"
    "SendQuota":"-2"
    "WarningQuota":"-2"
    "IsSetForVmEnrollment":"true"
    "VoiceNameRequired":"false"
    "SendBroadcastMsg":"false"
    "UpdateBroadcastMsg":"false"
    "ConversationVui":"VuiStart"
    "SpeechCompleteTimeout":"0"
    "SpeechIncompleteTimeout":"750"
    "UseVui":"false"
    "SkipPasswordForKnownDevice":"false"
    "JumpToMessagesOnLogin":"true"
    "EnableMessageLocator":"false"
    "MessageAgingPolicyObjectId":"adac77f4-8a77-430d-8836-
    0fc9aef3fef5"
    "MessageAgingPolicyURI":"/vmrest/messageagingpolicies/adac77f4-8a77-430d-8836-0fc9aef3fef5"
    "AssistantRowsPerPage":"5"
    "InboxMessagesPerPage":"20"
    "InboxAutoRefresh":"15"
    "InboxAutoResolveMessageRecipients":"true"
    "PcaAddressBookRowsPerPage":"5"
    "ReadOnly":"false"
    "EnableTts":"true"
    "ConfirmationConfidenceThreshold":"60"
    "AnnounceUpcomingMeetings":"60"
    "SpeechConfidenceThreshold":"40"
    "SpeechSpeedVsAccuracy":"50"
    "SpeechSensitivity":"50"
    "EnableVisualMessageLocator":"false"
    "ContinuousAddMode":"false"
    "NameConfirmation":"false"
    "CommandDigitTimeout":"1500"
    "SaveMessageOnHangup":"false"
    "SendMessageOnHangup":"1"
    "SkipForwardTime":"5000"
    "SkipReverseTime":"5000"
    "UseShortPollForCache":"false"
    "SearchByExtensionSearchSpaceObjectId":"2e836e16-f715-4a18-bb7c-
    ee5e33281706"
    "SearchByExtensionSearchSpaceURI":"/vmrest/searchspaces/2e836e16-f715-4a18-bb7c-
    ee5e33281706"
    "SearchByNameSearchSpaceObjectId":"2e836e16-f715-4a18-bb7c-ee5e33281706"
    "SearchByNameSearchSpaceURI":"/vmrest/searchspaces/2e836e16-f715-4a18-bb7c-
    ee5e33281706"
    "PartitionObjectId":"97bf6afe-346e-4275-967e-43c50be79d32"
    "PartitionURI":"/vmrest/partitions/97bf6afe-346e-4275-967e-43c50be79d32"
    "UseDynamicNameSearchWeight":"false"
    "LdapType":"0"
    "EnableMessageBookmark":"false"
    "SayTotalDraftMsg":"false"
    "EnableSaveDraft":"false"
    "RetainUrgentMessageFlag":"false"
    "SayMessageLength":"false"
    "CreateSmtpProxyFromCorp":"false"
    "AutoAdvanceMsgs":"false"
    "SaySenderAfter":"false"
    "SaySenderExtensionAfter":"false"
    "SayMsgNumberAfter":"false"
    "SayAniAfter":"false"
    "SayMessageLengthAfter":"false"
    "UserTemplateRolesURI":"/vmrest/usertemplates/6164ac2d-e8ec-441a-93a0-
    95f8e18a655c/usertemplateroles"
    "UserTemplateNotificationDevicesURI":"/vmrest/usertemplates/6164ac2d-e8ec-441a-93a0-
    95f8e18a655c/usertemplatenotificationdevices"
    "TemplateExternalServiceAccountsURI":"/vmrest/usertemplates/6164ac2d-e8ec-441a-93a0-
    95f8e18a655c/templateexternalserviceaccounts"
    "UserTemplateWebPasswordURI":"/vmrest/usertemplates/6164ac2d-e8ec-441a-93a0-
    95f8e18a655c/credential/password"
    "UserTemplateVoicePinURI":"/vmrest/usertemplates/6164ac2d-e8ec-441a-93a0-
    95f8e18a655c/credential/pin"
    "UserTemplateMessageActionURI":"/vmrest/usertemplates/6164ac2d-e8ec-441a-93a0-
    95f8e18a655c/usertemplatemessageactions"
}
\]
}
```

```
Response Code: 200
```

##### Listing Specific
                                 	 Tenant Related User Templates by System Administrator

In Cisco Unity Connection 10.5(2)
                                       		  and later, the system administrator can use TenantObjectID to list the specific
                                       		  tenant related user templates using the following URI:

```
GET https://<connection-server>/vmrest/usertemplates?query=(TenantObjectId is <Tenant-ObjectId>)
```

To get the TenantObjectID, use the following URI:

```
GET https://<connection-server>/vmrest/tenants
```

#### Viewing the
                              	 Details of Specific User Template

The following is an example of
                                    		  the GET request that lists the details of specific user template represented by
                                    		  the provided value of object ID:

```
GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectId>
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<UserTemplate>
    <URI> /vmrest/usertemplates/c8af2544-2bc9-44fa-b713-e80f306cf781 </URI>
    <ObjectId>c8af2544-2bc9-44fa-b713-e80f306cf781</ObjectId>
    <UseDefaultLanguage>true</UseDefaultLanguage>
    <UseDefaultTimeZone>true</UseDefaultTimeZone>
    <Alias>NewCiscoTemplate2</Alias>
    <City/>
    <State/>
    <Country>US</Country>
    <PostalCode/>
    <Department/>
    <Manager/>
    <Building/>
    <Address/>
    <DisplayName>testmonica</DisplayName>
    <BillingId/>
    <TimeZone>190</TimeZone>
    <CreationTime>2012-06-26 05:02:22.05</CreationTime>
    <CosObjectId>7be9b3f3-1200-403f-984a-04c07b7c5a7b</CosObjectId>
    <CosURI>/vmrest/coses/7be9b3f3-1200-403f-984a-04c07b7c5a7b</CosURI>
    <Language>1033</Language>
    <LocationObjectId>6d4ff2e5-3f26-4a19-b2fa-beca79b4c5e9 </LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/6d4ff2e5-3f26-4a19-b2fa-
    beca79b4c5e9</LocationURI>
    <AddressMode>0</AddressMode>
    <ClockMode>0</ClockMode>
    <ConversationTui>SubMenu</ConversationTui>
    <GreetByName>true</GreetByName>
    <ListInDirectory>true</ListInDirectory>
    <IsVmEnrolled>true</IsVmEnrolled>
    <SayCopiedNames>true</SayCopiedNames>
    <SayDistributionList>true</SayDistributionList>
    <SayMsgNumber>true</SayMsgNumber>
    <SaySender>true</SaySender>
    <SayTimestampAfter>true</SayTimestampAfter>
    <SayTimestampBefore>false</SayTimestampBefore>
    <SayTotalNew>false</SayTotalNew>
    <SayTotalNewEmail>false</SayTotalNewEmail>
    <SayTotalNewFax>false</SayTotalNewFax>
    <SayTotalNewVoice>true</SayTotalNewVoice>
    <SayTotalReceipts>false</SayTotalReceipts>
    <SayTotalSaved>true</SayTotalSaved>
    <Speed>100</Speed>
    <MediaSwitchObjectId>1fb12b1c-cf14-4634-b73d-9b9c58ecdf68</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/1fb12b1c-cf14-4634-b73d-
    9b9c58ecdf68</PhoneSystemURI>
    <Undeletable>false</Undeletable>
    <UseBriefPrompts>false</UseBriefPrompts>
    <Volume>50</Volume>
    <EnAltGreetDontRingPhone>false</EnAltGreetDontRingPhone>
    <EnAltGreetPreventSkip>false</EnAltGreetPreventSkip>
    <EnAltGreetPreventMsg>false</EnAltGreetPreventMsg>
    <EncryptPrivateMessages>false</EncryptPrivateMessages>
    <DeletedMessageSortOrder>2</DeletedMessageSortOrder>
    <SayAltGreetWarning>false</SayAltGreetWarning>
    <SaySenderExtension>false</SaySenderExtension>
    <SayAni>false</SayAni>
    <ExitCallActionObjectId>27cbb3a8-f040-4ee9-9686-620c43e3d725</ExitCallActionObjectId>
    <CallAnswerTimeout>4</CallAnswerTimeout>
    <CallHandlerObjectId>9a5ac35a-0df8-4ebb-8e19-77f936dfd263</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/callhandlerprimarytemplates/9a5ac35a-0df8-4ebb-8e19-
    77f936dfd263</CallhandlerURI>
    <DisplayNameRule>1</DisplayNameRule>
    <DoesntExpire>false</DoesntExpire>
    <CantChange>false</CantChange>
    <MailboxStoreObjectId>cfc43112-601b-4764-ba92-b0220e9d7f23</MailboxStoreObjectId>
    <SavedMessageStackOrder>1234567</SavedMessageStackOrder>
    <NewMessageStackOrder>1234567</NewMessageStackOrder>
    <MessageLocatorSortOrder>1</MessageLocatorSortOrder>
    <SavedMessageSortOrder>2</SavedMessageSortOrder>
    <NewMessageSortOrder>1</NewMessageSortOrder>
    <MessageTypeMenu>false</MessageTypeMenu>
    <EnablePersonalRules>true</EnablePersonalRules>
    <RecordUnknownCallerName>true</RecordUnknownCallerName>
    <RingPrimaryPhoneFirst>false</RingPrimaryPhoneFirst>
    <PromptSpeed>100</PromptSpeed>
    <ExitAction>2</ExitAction>
    <ExitTargetConversation>PHTransfer</ExitTargetConversation>
    <ExitTargetHandlerObjectId>7ae69f21-1c99-4cc1-96c3-a1bbe11fd4ca</ExitTargetHandlerObjectId>
    <RepeatMenu>1</RepeatMenu>
    <FirstDigitTimeout>5000</FirstDigitTimeout>
    <InterdigitDelay>3000</InterdigitDelay>
    <PromptVolume>50</PromptVolume>
    <AddressAfterRecord>false</AddressAfterRecord>
    <ConfirmDeleteMessage>false</ConfirmDeleteMessage>
    <ConfirmDeleteDeletedMessage>false</ConfirmDeleteDeletedMessage>
    <ConfirmDeleteMultipleMessages>true</ConfirmDeleteMultipleMessages>
    <IsClockMode24Hour>false</IsClockMode24Hour>
    <RouteNDRToSender>true</RouteNDRToSender>
    <NotificationType>0</NotificationType>
    <SendReadReceipts>0</SendReadReceipts>   
    <ReceiveQuota>-1</ReceiveQuota>
    <SendQuota>-1</SendQuota>
    <WarningQuota>-1</WarningQuota> 
    <IsSetForVmEnrollment>true</IsSetForVmEnrollment>
    <VoiceNameRequired>false</VoiceNameRequired>
    <SendBroadcastMsg>true</SendBroadcastMsg>
    <UpdateBroadcastMsg>false</UpdateBroadcastMsg>
    <ConversationVui>VuiStart</ConversationVui>
    <SpeechCompleteTimeout>0</SpeechCompleteTimeout>
    <SpeechIncompleteTimeout>750</SpeechIncompleteTimeout>
    <UseVui>false</UseVui>
    <SkipPasswordForKnownDevice>false</SkipPasswordForKnownDevice>
    <JumpToMessagesOnLogin>true</JumpToMessagesOnLogin>
    <EnableMessageLocator>false</EnableMessageLocator>
    <MessageAgingPolicyObjectId>2e02eca6-270b-4b7f-a153-
    f03ea74d403d</MessageAgingPolicyObjectId>
    <MessageAgingPolicyURI>/vmrest/messageagingpolicies/2e02eca6-270b-4b7f-a153-
    f03ea74d403d</MessageAgingPolicyURI>
    <AssistantRowsPerPage>5</AssistantRowsPerPage>
    <InboxMessagesPerPage>20</InboxMessagesPerPage>
    <InboxAutoRefresh>15</InboxAutoRefresh>
    <InboxAutoResolveMessageRecipients>true</InboxAutoResolveMessageRecipients>
    <PcaAddressBookRowsPerPage>5</PcaAddressBookRowsPerPage>
    <ReadOnly>false</ReadOnly>
    <EnableTts>true</EnableTts>
    <ConfirmationConfidenceThreshold>60</ConfirmationConfidenceThreshold>
    <AnnounceUpcomingMeetings>60</AnnounceUpcomingMeetings>
    <SpeechConfidenceThreshold>40</SpeechConfidenceThreshold>
    <SpeechSpeedVsAccuracy>50</SpeechSpeedVsAccuracy>
    <SpeechSensitivity>50</SpeechSensitivity>
    <EnableVisualMessageLocator>false</EnableVisualMessageLocator>
    <ContinuousAddMode>false</ContinuousAddMode>
    <NameConfirmation>false</NameConfirmation>
    <CommandDigitTimeout>1500</CommandDigitTimeout>
    <SaveMessageOnHangup>false</SaveMessageOnHangup>
    <SendMessageOnHangup>1</SendMessageOnHangup>
    <SkipForwardTime>5000</SkipForwardTime>
    <SkipReverseTime>5000</SkipReverseTime>
    <UseShortPollForCache>false</UseShortPollForCache>
    <SearchByExtensionSearchSpaceObjectId>25e2e004-c194-4593-9961-
    bdcaf5dd7189</SearchByExtensionSearchSpaceObjectId>
    <SearchByExtensionSearchSpaceURI>/vmrest/searchspaces/25e2e004-c194-4593-9961-
    bdcaf5dd7189</SearchByExtensionSearchSpaceURI>
    <SearchByNameSearchSpaceObjectId>25e2e004-c194-4593-9961-
    bdcaf5dd7189</SearchByNameSearchSpaceObjectId>
    <SearchByNameSearchSpaceURI>/vmrest/searchspaces/25e2e004-c194-4593-9961-
    bdcaf5dd7189</SearchByNameSearchSpaceURI>
    <PartitionObjectId>12101df7-ecd2-4a48-b5b9-9a96b5f85a25</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/12101df7-ecd2-4a48-b5b9-9a96b5f85a25</PartitionURI>
    <UseDynamicNameSearchWeight>false</UseDynamicNameSearchWeight>
    <LdapType>0</LdapType>
    <EnableMessageBookmark>false</EnableMessageBookmark>
    <SayTotalDraftMsg>false</SayTotalDraftMsg>
    <EnableSaveDraft>false</EnableSaveDraft>
    <RetainUrgentMessageFlag>false</RetainUrgentMessageFlag>
    <SayMessageLength>false</SayMessageLength>
    <CreateSmtpProxyFromCorp>false</CreateSmtpProxyFromCorp>
    <AutoAdvanceMsgs>false</AutoAdvanceMsgs>
    <SaySenderAfter>false</SaySenderAfter>
    <SaySenderExtensionAfter>false</SaySenderExtensionAfter>
    <SayMsgNumberAfter>false</SayMsgNumberAfter>
    <SayAniAfter>false</SayAniAfter>
    <SayMessageLengthAfter>false</SayMessageLengthAfter>
    <UserTemplateRolesURI>/vmrest/usertemplates/c8af2544-2bc9-44fa-b713-
    e80f306cf781/usertemplateroles</UserTemplateRolesURI>
    <UserTemplateNotificationDevicesURI>/vmrest/usertemplates/c8af2544-2bc9-44fa-b713-
    e80f306cf781/usertemplatenotificationdevices</UserTemplateNotificationDevicesURI>
    <UserTemplateWebPasswordURI>/vmrest/usertemplates/c8af2544-2bc9-44fa-b713-
    e80f306cf781/credential/password</UserTemplateWebPasswordURI>
    <UserTemplateVoicePinURI>/vmrest/usertemplates/c8af2544-2bc9-44fa-b713-
    e80f306cf781/credential/pin</UserTemplateVoicePinURI>
    <UserTemplateMessageActionURI>/vmrest/usertemplates/c8af2544-2bc9-44fa-b713-
    e80f306cf781/usertemplatemessageactions</UserTemplateMessageActionURI>
</UserTemplate>
```

```
Response Code: 200
```

JSON Example

To view the particular user template, do the following:

```
Request URI:
GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectId>
Accept: application/json
Content_type: application/json
Connection: keep_alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
    "URI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-099afef0604d"
    "ObjectId":"a46d269a-6614-485b-8649-099afef0604d"
    "UseDefaultLanguage":"true"
    "UseDefaultTimeZone":"true"
    "Alias":"voicemailusertemplate"
    "DisplayName":"Voice Mail User Template"
    "TimeZone":"190"
    "CreationTime":"2013-02-21T11:39:11Z"
    "CosObjectId":"c93854b3-c59f-44e7-a6a9-0a6e17578672"
    "CosURI":"/vmrest/coses/c93854b3-c59f-44e7-a6a9-0a6e17578672"
    "Language":"1033"
    "LocationObjectId":"830e1a2d-8e90-459f-88f7-700497ba975c"
    "LocationURI":"/vmrest/locations/connectionlocations/830e1a2d-8e90-459f-88f7-
     700497ba975c"
    "AddressMode":"0"
    "ClockMode":"0"
    "ConversationTui":"SubMenu"
    "GreetByName":"true"
    "ListInDirectory":"true"
    "IsVmEnrolled":"true"
    "SayCopiedNames":"true"
    "SayDistributionList":"true"
    "SayMsgNumber":"true"
    "SaySender":"true"
    "SayTimestampAfter":"true"
    "SayTimestampBefore":"false"
    "SayTotalNew":"false"
    "SayTotalNewEmail":"false"
    "SayTotalNewFax":"false"
    "SayTotalNewVoice":"true"
    "SayTotalReceipts":"false"
    "SayTotalSaved":"true"
    "Speed":"100"
    "MediaSwitchObjectId":"caf093ef-5e7b-47dd-9db7-9df360d2923e"
    "PhoneSystemURI":"/vmrest/phonesystems/caf093ef-5e7b-47dd-9db7-9df360d2923e"
    "Undeletable":"true"
    "UseBriefPrompts":"false"
    "Volume":"50"
    "EnAltGreetDontRingPhone":"false"
    "EnAltGreetPreventSkip":"false"
    "EnAltGreetPreventMsg":"false"
    "EncryptPrivateMessages":"false"
    "DeletedMessageSortOrder":"2"
    "SayAltGreetWarning":"false"
    "SaySenderExtension":"false"
    "SayAni":"false"
    "ExitCallActionObjectId":"ecc8570c-c0da-493e-a520-b125529cfee1"
    "CallAnswerTimeout":"4"
    "CallHandlerObjectId":"f4f87905-c20a-4df3-b20e-446c1798df19"
    "CallhandlerURI":"/vmrest/callhandlerprimarytemplates/f4f87905-c20a-4df3-b20e-
    446c1798df19"
    "DisplayNameRule":"1"
    "DoesntExpire":"false"
    "CantChange":"false"
    "MailboxStoreObjectId":"90e5847b-3a87-4c92-a753-eda6ea0fdb4c"
    "SavedMessageStackOrder":"1234567"
    "NewMessageStackOrder":"1234567"
    "MessageLocatorSortOrder":"1"
    "SavedMessageSortOrder":"2"
    "NewMessageSortOrder":"1"
    "MessageTypeMenu":"false"
    "EnablePersonalRules":"true"
    "RecordUnknownCallerName":"true"
    "RingPrimaryPhoneFirst":"false"
    "PromptSpeed":"100"
    "ExitAction":"2"
    "ExitTargetConversation":"PHGreeting"
    "ExitTargetHandlerObjectId":"d085ebc6-99ac-46a5-92f3-d26f52701585"
    "RepeatMenu":"1"
    "FirstDigitTimeout":"5000"
    "InterdigitDelay":"3000"
    "PromptVolume":"50"
    "AddressAfterRecord":"false"
    "ConfirmDeleteMessage":"false"
    "ConfirmDeleteDeletedMessage":"false"
    "ConfirmDeleteMultipleMessages":"true"
    "IsClockMode24Hour":"false"
    "RouteNDRToSender":"true"
    "NotificationType":"0"
    "SendReadReceipts":"1"
    "ReceiveQuota":"-2"
    "SendQuota":"-2"
    "WarningQuota":"-2"
    "IsSetForVmEnrollment":"true"
    "VoiceNameRequired":"false"
    "SendBroadcastMsg":"false"
    "UpdateBroadcastMsg":"false"
    "ConversationVui":"VuiStart"
    "SpeechCompleteTimeout":"0"
    "SpeechIncompleteTimeout":"750"
    "UseVui":"false"
    "SkipPasswordForKnownDevice":"false"
    "JumpToMessagesOnLogin":"true"
    "EnableMessageLocator":"false"
    "MessageAgingPolicyObjectId":"12b765a8-a67b-47f6-8ede-3e02aea9f4fe"
    "MessageAgingPolicyURI":"/vmrest/messageagingpolicies/12b765a8-a67b-47f6-8ede-
    3e02aea9f4fe"
    "AssistantRowsPerPage":"5"
    "InboxMessagesPerPage":"20"
    "InboxAutoRefresh":"15"
    "InboxAutoResolveMessageRecipients":"true"
    "PcaAddressBookRowsPerPage":"5"
    "ReadOnly":"false"
    "EnableTts":"true"
    "ConfirmationConfidenceThreshold":"60"
    "AnnounceUpcomingMeetings":"60"
    "SpeechConfidenceThreshold":"40"
    "SpeechSpeedVsAccuracy":"50"
    "SpeechSensitivity":"50"
    "EnableVisualMessageLocator":"false"
    "ContinuousAddMode":"false"
    "NameConfirmation":"false"
    "CommandDigitTimeout":"1500"
    "SaveMessageOnHangup":"false"
    "SendMessageOnHangup":"1"
    "SkipForwardTime":"5000"
    "SkipReverseTime":"5000"
    "UseShortPollForCache":"false"
    "SearchByExtensionSearchSpaceObjectId":"7aaf45b8-ab06-4dda-af16-378b04a95912"
    "SearchByExtensionSearchSpaceURI":"/vmrest/searchspaces/7aaf45b8-ab06-4dda-af16-
    378b04a95912"
    "SearchByNameSearchSpaceObjectId":"7aaf45b8-ab06-4dda-af16-378b04a95912"
    "SearchByNameSearchSpaceURI":"/vmrest/searchspaces/7aaf45b8-ab06-4dda-af16-
    378b04a95912"
    "PartitionObjectId":"9c010254-1493-4e1a-9e47-fe2494792744"
    "PartitionURI":"/vmrest/partitions/9c010254-1493-4e1a-9e47-fe2494792744"
    "UseDynamicNameSearchWeight":"false"
    "LdapType":"0"
    "EnableMessageBookmark":"false"
    "SayTotalDraftMsg":"false"
    "EnableSaveDraft":"false"
    "RetainUrgentMessageFlag":"false"
    "SayMessageLength":"false"
    "CreateSmtpProxyFromCorp":"false"
    "AutoAdvanceMsgs":"false"
    "SaySenderAfter":"false"
    "SaySenderExtensionAfter":"false"
    "SayMsgNumberAfter":"false"
    "SayAniAfter":"false"
    "SayMessageLengthAfter":"false"
    "UserTemplateRolesURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/usertemplateroles"
    "UserTemplateNotificationDevicesURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/usertemplatenotificationdevices"
    "TemplateExternalServiceAccountsURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/templateexternalserviceaccounts"
    "UserTemplateWebPasswordURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/credential/password"
    "UserTemplateVoicePinURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/credential/pin"
    "UserTemplateMessageActionURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/usertemplatemessageactions"
}
```

```
Response Code: 200
```

#### Viewing the
                              	 Details of the User Templates Based on Partition Object ID

The following is an example of
                                    		  the GET request that lists the details of specific user template represented by
                                    		  the provided value of partition object ID:

```
GET https://<connection-server>/vmrest/usertemplates?query=(PartitionObjectId%20is%20<PartitionObjectId>)
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<UserTemplate>
    <URI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-2b13f76bf631</URI>
    <ObjectId>c2056af2-bed7-4a0d-9039-2b13f76bf631</ObjectId>
    <UseDefaultLanguage>true</UseDefaultLanguage>
    <UseDefaultTimeZone>true</UseDefaultTimeZone>
    <Alias>Texoma_User_Template1</Alias>
    <City/>
    <State/>
    <Country>US</Country>
    <PostalCode/>
    <Manager/>
    <Building/>
    <Address/>
    <DisplayName>Texoma_User_Template1</DisplayName>
    <BillingId/>
    <TimeZone>190</TimeZone>
    <CreationTime>2012-12-26 13:04:28.9</CreationTime>
    <CosObjectId>0ef61610-a729-4b0d-9476-cab095028db3</CosObjectId>
    <CosURI>/vmrest/coses/0ef61610-a729-4b0d-9476-cab095028db3</CosURI>
    <Language>1033</Language>
    <LocationObjectId>27a67e01-bcb4-4012-8b1b-f0a08b736087</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/27a67e01-bcb4-4012-8b1b-
    f0a08b736087</LocationURI>
    <AddressMode>0</AddressMode>
    <ClockMode>0</ClockMode>
    <ConversationTui>SubMenu</ConversationTui>
    <GreetByName>true</GreetByName>
    <ListInDirectory>true</ListInDirectory>
    <IsVmEnrolled>true</IsVmEnrolled>
    <SayCopiedNames>true</SayCopiedNames>
    <SayDistributionList>true</SayDistributionList>
    <SayMsgNumber>true</SayMsgNumber>
    <SaySender>true</SaySender>
    <SayTimestampAfter>true</SayTimestampAfter>
    <SayTimestampBefore>false</SayTimestampBefore>
    <SayTotalNew>false</SayTotalNew>
    <SayTotalNewEmail>false</SayTotalNewEmail>
    <SayTotalNewFax>false</SayTotalNewFax>
    <SayTotalNewVoice>true</SayTotalNewVoice>
    <SayTotalReceipts>false</SayTotalReceipts>
    <SayTotalSaved>true</SayTotalSaved>
    <Speed>100</Speed>
    <MediaSwitchObjectId>b6df8cb3-b3ce-4797-84f3-5559049df8e8</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/b6df8cb3-b3ce-4797-84f3-
    5559049df8e8</PhoneSystemURI>
    <Undeletable>false</Undeletable> 
    <UseBriefPrompts>false</UseBriefPrompts>
    <Volume>50</Volume> 
    <EnAltGreetDontRingPhone>false</EnAltGreetDontRingPhone>
    <EnAltGreetPreventSkip>false</EnAltGreetPreventSkip>
    <EnAltGreetPreventMsg>false</EnAltGreetPreventMsg>
    <EncryptPrivateMessages>false</EncryptPrivateMessages>
    <DeletedMessageSortOrder>2</DeletedMessageSortOrder>
    <SayAltGreetWarning>false</SayAltGreetWarning> 
    <SaySenderExtension>false</SaySenderExtension>
    <SayAni>false</SayAni> 
    <ExitCallActionObjectId>0463e49b-cde4-4c30-877c-acfe25966a42</ExitCallActionObjectId>
    <CallAnswerTimeout>4</CallAnswerTimeout>
    <CallHandlerObjectId>83c9b890-6659-4c0f-8be6-8a1a85efee7e</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/callhandlerprimarytemplates/83c9b890-6659-4c0f-8be6-
    8a1a85efee7e</CallhandlerURI>
    <DisplayNameRule>1</DisplayNameRule>
    <DoesntExpire>false</DoesntExpire>
    <CantChange>false</CantChange>
    <MailboxStoreObjectId>e983490d-78a5-45aa-b9a0-31f51460a5bd</MailboxStoreObjectId>
    <SavedMessageStackOrder>1234567</SavedMessageStackOrder>
    <NewMessageStackOrder>1234567</NewMessageStackOrder>
    <MessageLocatorSortOrder>1</MessageLocatorSortOrder>
    <SavedMessageSortOrder>2</SavedMessageSortOrder>
    <NewMessageSortOrder>1</NewMessageSortOrder>
    <MessageTypeMenu>false</MessageTypeMenu>
    <EnablePersonalRules>true</EnablePersonalRules>
    <RecordUnknownCallerName>true</RecordUnknownCallerName>
    <RingPrimaryPhoneFirst>false</RingPrimaryPhoneFirst>
    <PromptSpeed>100</PromptSpeed>
    <ExitAction>2</ExitAction>
    <ExitTargetConversation>PHGreeting</ExitTargetConversation>
    <ExitTargetHandlerObjectId>063956f9-c5ca-4e8b-be67-
    ff945a8a5d99</ExitTargetHandlerObjectId>
    <RepeatMenu>1</RepeatMenu>
    <FirstDigitTimeout>5000</FirstDigitTimeout>
    <InterdigitDelay>3000</InterdigitDelay>
    <PromptVolume>50</PromptVolume>
    <DelayAfterGreeting>0</DelayAfterGreeting>
    <AddressAfterRecord>false</AddressAfterRecord>
    <ConfirmDeleteMessage>false</ConfirmDeleteMessage>
    <ConfirmDeleteDeletedMessage>false</ConfirmDeleteDeletedMessage>
    <ConfirmDeleteMultipleMessages>true</ConfirmDeleteMultipleMessages>
    <IsClockMode24Hour>false</IsClockMode24Hour>
    <RouteNDRToSender>true</RouteNDRToSender>
    <NotificationType>0</NotificationType>
    <SendReadReceipts>1</SendReadReceipts>
    <ReceiveQuota>-2</ReceiveQuota>
    <SendQuota>-2</SendQuota>
    <WarningQuota>-2</WarningQuota>
    <IsSetForVmEnrollment>true</IsSetForVmEnrollment>
    <VoiceNameRequired>false</VoiceNameRequired>
    <SendBroadcastMsg>false</SendBroadcastMsg>
    <UpdateBroadcastMsg>false</UpdateBroadcastMsg>
    <ConversationVui>VuiStart</ConversationVui>
    <SpeechCompleteTimeout>0</SpeechCompleteTimeout>
    <SpeechIncompleteTimeout>750</SpeechIncompleteTimeout>
    <UseVui>false</UseVui>
    <SkipPasswordForKnownDevice>false</SkipPasswordForKnownDevice>
    <JumpToMessagesOnLogin>true</JumpToMessagesOnLogin>
    <EnableMessageLocator>false</EnableMessageLocator>
    <MessageAgingPolicyObjectId>6780a194-6efd-4311-819f-
    494a082bb093</MessageAgingPolicyObjectId>
    <MessageAgingPolicyURI>/vmrest/messageagingpolicies/6780a194-6efd-4311-819f-
    494a082bb093</MessageAgingPolicyURI>
    <AssistantRowsPerPage>5</AssistantRowsPerPage>
    <InboxMessagesPerPage>20</InboxMessagesPerPage>
    <InboxAutoRefresh>15</InboxAutoRefresh>
    <InboxAutoResolveMessageRecipients>true</InboxAutoResolveMessageRecipients>
    <PcaAddressBookRowsPerPage>5</PcaAddressBookRowsPerPage>
    <ReadOnly>false</ReadOnly>
    <EnableTts>true</EnableTts>
    <ConfirmationConfidenceThreshold>60</ConfirmationConfidenceThreshold>
    <AnnounceUpcomingMeetings>60</AnnounceUpcomingMeetings>
    <SpeechConfidenceThreshold>40</SpeechConfidenceThreshold>
    <SpeechSpeedVsAccuracy>50</SpeechSpeedVsAccuracy>
    <SpeechSensitivity>50</SpeechSensitivity>
    <EnableVisualMessageLocator>false</EnableVisualMessageLocator>
    <ContinuousAddMode>false</ContinuousAddMode> 
    <NameConfirmation>false</NameConfirmation> 
    <CommandDigitTimeout>1500</CommandDigitTimeout> 
    <SaveMessageOnHangup>false</SaveMessageOnHangup> 
    <SendMessageOnHangup>1</SendMessageOnHangup> 
    <SkipForwardTime>5000</SkipForwardTime> 
    <SkipReverseTime>5000</SkipReverseTime> 
    <UseShortPollForCache>false</UseShortPollForCache> 
    <SearchByExtensionSearchSpaceObjectId>2e0da21b-54e4-4b51-9f09-
    960049a5e806</SearchByExtensionSearchSpaceObjectId> 
    <SearchByExtensionSearchSpaceURI>/vmrest/searchspaces/2e0da21b-54e4-4b51-9f09-
    960049a5e806</SearchByExtensionSearchSpaceURI> 
    <SearchByNameSearchSpaceObjectId>2e0da21b-54e4-4b51-9f09-
    960049a5e806</SearchByNameSearchSpaceObjectId> 
    <SearchByNameSearchSpaceURI>/vmrest/searchspaces/2e0da21b-54e4-4b51-9f09-
    960049a5e806</SearchByNameSearchSpaceURI>
   <PartitionObjectId>c6ff147e-c32c-4ade-8f12-46427c795c21</PartitionObjectId> 
   <PartitionURI>/vmrest/partitions/c6ff147e-c32c-4ade-8f12-46427c795c21</PartitionURI> 
   <UseDynamicNameSearchWeight>false</UseDynamicNameSearchWeight> 
   <LdapType>0</LdapType> 
   <EnableMessageBookmark>false</EnableMessageBookmark> 
   <SayTotalDraftMsg>false</SayTotalDraftMsg> 
   <EnableSaveDraft>false</EnableSaveDraft> 
   <RetainUrgentMessageFlag>false</RetainUrgentMessageFlag> 
   <SayMessageLength>false</SayMessageLength> 
   <CreateSmtpProxyFromCorp>false</CreateSmtpProxyFromCorp> 
   <AutoAdvanceMsgs>false</AutoAdvanceMsgs> 
   <SaySenderAfter>false</SaySenderAfter> 
   <SaySenderExtensionAfter>false</SaySenderExtensionAfter> 
   <SayMsgNumberAfter>false</SayMsgNumberAfter> 
   <SayAniAfter>false</SayAniAfter> 
   <SayMessageLengthAfter>false</SayMessageLengthAfter> 
   <UserTemplateRolesURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-
   2b13f76bf631/usertemplateroles</UserTemplateRolesURI> 
   <UserTemplateNotificationDevicesURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-
   2b13f76bf631/usertemplatenotificationdevices</UserTemplateNotificationDevicesURI> 
   <TemplateExternalServiceAccountsURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-
   2b13f76bf631/templateexternalserviceaccounts</TemplateExternalServiceAccountsURI> 
   <UserTemplateWebPasswordURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-
   2b13f76bf631/credential/password</UserTemplateWebPasswordURI> 
   <UserTemplateVoicePinURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-
   2b13f76bf631/credential/pin</UserTemplateVoicePinURI> 
   <UserTemplateMessageActionURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-
   2b13f76bf631/usertemplatemessageactions</UserTemplateMessageActionURI>
</UserTemplate>
```

```
Response Code: 200
```

JSON Example

To view the details of the user templates based on partition object
                                    		  ID, do the following:

```
Request URI:
GET https://<connection-server>/vmrest/usertemplates?query=(PartitionObjectId%20is%20<PartitionObjectId>)
Accept: application/json
Content_type: application/json
Connection: keep_alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
    "URI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-099afef0604d"
    "ObjectId":"a46d269a-6614-485b-8649-099afef0604d"
    "UseDefaultLanguage":"true"
    "UseDefaultTimeZone":"true"
    "Alias":"voicemailusertemplate"
    "DisplayName":"Voice Mail User Template"
    "TimeZone":"190"
    "CreationTime":"2013-02-21T11:39:11Z"
    "CosObjectId":"c93854b3-c59f-44e7-a6a9-0a6e17578672"
    "CosURI":"/vmrest/coses/c93854b3-c59f-44e7-a6a9-0a6e17578672"
    "Language":"1033"
    "LocationObjectId":"830e1a2d-8e90-459f-88f7-700497ba975c"
    "LocationURI":"/vmrest/locations/connectionlocations/830e1a2d-8e90-459f-88f7-
    700497ba975c"
    "AddressMode":"0"
    "ClockMode":"0"
    "ConversationTui":"SubMenu"
    "GreetByName":"true"
    "ListInDirectory":"true"
    "IsVmEnrolled":"true"
    "SayCopiedNames":"true"
    "SayDistributionList":"true"
    "SayMsgNumber":"true"
    "SaySender":"true"
    "SayTimestampAfter":"true"
    "SayTimestampBefore":"false"
    "SayTotalNew":"false"
    "SayTotalNewEmail":"false"
    "SayTotalNewFax":"false"
    "SayTotalNewVoice":"true"
    "SayTotalReceipts":"false"
    "SayTotalSaved":"true"
    "Speed":"100"
    "MediaSwitchObjectId":"caf093ef-5e7b-47dd-9db7-9df360d2923e"
    "PhoneSystemURI":"/vmrest/phonesystems/caf093ef-5e7b-47dd-9db7-9df360d2923e"
    "Undeletable":"true"
    "UseBriefPrompts":"false"
    "Volume":"50"
    "EnAltGreetDontRingPhone":"false"
    "EnAltGreetPreventSkip":"false"
    "EnAltGreetPreventMsg":"false"
    "EncryptPrivateMessages":"false"
    "DeletedMessageSortOrder":"2"
    "SayAltGreetWarning":"false"
    "SaySenderExtension":"false"
    "SayAni":"false"
    "ExitCallActionObjectId":"ecc8570c-c0da-493e-a520-b125529cfee1"
    "CallAnswerTimeout":"4"
    "CallHandlerObjectId":"f4f87905-c20a-4df3-b20e-446c1798df19"
    "CallhandlerURI":"/vmrest/callhandlerprimarytemplates/f4f87905-c20a-4df3-b20e-
    446c1798df19"
    "DisplayNameRule":"1"
    "DoesntExpire":"false"
    "CantChange":"false"
    "MailboxStoreObjectId":"90e5847b-3a87-4c92-a753-eda6ea0fdb4c"
    "SavedMessageStackOrder":"1234567"
    "NewMessageStackOrder":"1234567"
    "MessageLocatorSortOrder":"1"
    "SavedMessageSortOrder":"2"
    "NewMessageSortOrder":"1"
    "MessageTypeMenu":"false"
    "EnablePersonalRules":"true"
    "RecordUnknownCallerName":"true"
    "RingPrimaryPhoneFirst":"false"
    "PromptSpeed":"100"
    "ExitAction":"2"
    "ExitTargetConversation":"PHGreeting"
    "ExitTargetHandlerObjectId":"d085ebc6-99ac-46a5-92f3-d26f52701585"
    "RepeatMenu":"1"
    "FirstDigitTimeout":"5000"
    "InterdigitDelay":"3000"
    "PromptVolume":"50"
    "AddressAfterRecord":"false"
    "ConfirmDeleteMessage":"false"
    "ConfirmDeleteDeletedMessage":"false"
    "ConfirmDeleteMultipleMessages":"true"
    "IsClockMode24Hour":"false"
    "RouteNDRToSender":"true"
    "NotificationType":"0"
    "SendReadReceipts":"1"
    "ReceiveQuota":"-2"
    "SendQuota":"-2"
    "WarningQuota":"-2"
    "IsSetForVmEnrollment":"true"
    "VoiceNameRequired":"false"
    "SendBroadcastMsg":"false"
    "UpdateBroadcastMsg":"false"
    "ConversationVui":"VuiStart"
    "SpeechCompleteTimeout":"0"
    "SpeechIncompleteTimeout":"750"
    "UseVui":"false"
    "SkipPasswordForKnownDevice":"false"
    "JumpToMessagesOnLogin":"true"
    "EnableMessageLocator":"false"
    "MessageAgingPolicyObjectId":"12b765a8-a67b-47f6-8ede-3e02aea9f4fe"
    "MessageAgingPolicyURI":"/vmrest/messageagingpolicies/12b765a8-a67b-47f6-8ede-
    3e02aea9f4fe"
    "AssistantRowsPerPage":"5"
    "InboxMessagesPerPage":"20"
    "InboxAutoRefresh":"15"
    "InboxAutoResolveMessageRecipients":"true"
    "PcaAddressBookRowsPerPage":"5"
    "ReadOnly":"false"
    "EnableTts":"true"
    "ConfirmationConfidenceThreshold":"60"
    "AnnounceUpcomingMeetings":"60"
    "SpeechConfidenceThreshold":"40"
    "SpeechSpeedVsAccuracy":"50"
    "SpeechSensitivity":"50"
    "EnableVisualMessageLocator":"false"
    "ContinuousAddMode":"false"
    "NameConfirmation":"false"
    "CommandDigitTimeout":"1500"
    "SaveMessageOnHangup":"false"
    "SendMessageOnHangup":"1"
    "SkipForwardTime":"5000"
    "SkipReverseTime":"5000"
    "UseShortPollForCache":"false"
    "SearchByExtensionSearchSpaceObjectId":"7aaf45b8-ab06-4dda-af16-378b04a95912"
    "SearchByExtensionSearchSpaceURI":"/vmrest/searchspaces/7aaf45b8-ab06-4dda-af16-378b04a95912"
    "SearchByNameSearchSpaceObjectId":"7aaf45b8-ab06-4dda-af16-
    378b04a95912"
    "SearchByNameSearchSpaceURI":"/vmrest/searchspaces/7aaf45b8-ab06-4dda-af16-
    378b04a95912"
    "PartitionObjectId":"9c010254-1493-4e1a-9e47-fe2494792744"
    "PartitionURI":"/vmrest/partitions/9c010254-1493-4e1a-9e47-fe2494792744"
    "UseDynamicNameSearchWeight":"false"
    "LdapType":"0"
    "EnableMessageBookmark":"false"
    "SayTotalDraftMsg":"false"
    "EnableSaveDraft":"false"
    "RetainUrgentMessageFlag":"false"
    "SayMessageLength":"false"
    "CreateSmtpProxyFromCorp":"false"
    "AutoAdvanceMsgs":"false"
    "SaySenderAfter":"false"
    "SaySenderExtensionAfter":"false"
    "SayMsgNumberAfter":"false"
    "SayAniAfter":"false"
    "SayMessageLengthAfter":"false"
    "UserTemplateRolesURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/usertemplateroles"
    "UserTemplateNotificationDevicesURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/usertemplatenotificationdevices"
    "TemplateExternalServiceAccountsURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/templateexternalserviceaccounts"
    "UserTemplateWebPasswordURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/credential/password"
    "UserTemplateVoicePinURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/credential/pin"
    "UserTemplateMessageActionURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/usertemplatemessageactions"
}
```

```
Response Code: 200
```

Same way user templates can be viewed for particular COS object ID, mailbox store object ID, phone system and call handler
                                                object ID.

- PartitionObjectId can be viewed from https://<connection-server>/vmrest/partitions

- COSObjectId : https://<connection-server>/vmrest/coses

- PhoneSystem : https://<connection-server>/vmrest/phonesystems

#### Creating a User
                              	 Template

The request can be used to create
                                    		  the User Template. It can be used to create the User Template with specific
                                    		  Partition Object ID, COS, MailboxStoreObjectId, Phone System. The following is
                                    		  an example of the POST request that creates a new user template:

```
POST https://<connection-server>/vmrest/usertemplates?templateAlias=voicemailusertemplate
Request Body:
<UserTemplate>
    <Alias>ABC_user template</Alias>
    <DisplayName>ABC@user template</DisplayName>
</UserTemplate>
```

The following is the response from the above *POST* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 201
```

JSON Example

To create user template:

```
POST https://<connection-server>/vmrest/usertemplates?templateAlias=voicemailusertemplate
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "Alias":"voicemailusertemplate1",
    "DisplayName":"Voice Mail User Template 1"
}
```

The following is the response from the above *POST* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 201
```

#### Creating a User
                              	 Template with Specific Partition Object ID

The request can be used to create
                                    		  the User Template. It can be used to create the User Template with specific
                                    		  Partition Object ID, COS, MailboxStoreObjectId, Phone System. The following is
                                    		  an example of the POST request that creates a new user template:

```
POST https://<connection-server>/vmrest/usertemplates?templateAlias=voicemailusertemplate
Request Body:
<UserTemplate>
    <Alias>ABCs_user template</Alias>
    <DisplayName>ABCs@user template</DisplayName>
    <PartitionObjectId>00c25bc8-d3d0-45ec-a786-fcf7a35593cf</PartitionObjectId>
</UserTemplate>
```

The following is the response from the above *POST* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 201
```

JSON Example

To create user template with specific partition ID, do the following:

```
Request URI:
POST https://<connection-server>/vmrest/usertemplates?templateAlias=<TemplatealiasName> 
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "Alias":"voicemailusertemplate12",
    "DisplayName":"Voice Mail User Templater12",
    "PartitionObjectId":"be52d373-25c4-416c-81c1-b82479061192"
}
```

The following is the response from the above *POST* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 201
```

#### Updating Fields
                              	 of User Templates

The request can be used to update
                                    		  the fields of a user template. It can be used to update Alias, Display Name,
                                    		  Time Zone, Language, COS, Partition Object ID, Phone System and Basic Setting
                                    		  fields of a user template. The following is an example of the PUT request that
                                    		  updates a user template:

```
PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>
Request Body:
<UserTemplate>
    <Alias>ABCD_user template</Alias>
    <UseDefaultLanguage>true</UseDefaultLanguage>
    <Language>1033</Language>
    <UseDefaultTimeZone>true</UseDefaultTimeZone>
    <TimeZone>190</TimeZone>
    <CosObjectId>6f054167-6f6c-4ed5-a498-1776337871ee</CosObjectId> 
    <MediaSwitchObjectId>221ee752-5147-4326-9990-d4a138674f9e</MediaSwitchObjectId> 
</UserTemplate>
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To update fields of a user template:

```
PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "Alias":"ABC_user template",
    "DisplayName":"Auser template",
    "UseDefaultLanguage":"false",
    "TimeZone":"190",
    "MediaSwitchObjectId":"caf093ef-5e7b-47dd-9db7-9df360d2923e",
    "CosObjectId":"c93854b3-c59f-44e7-a6a9-0a6e17578672"
}
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

#### Update Country
                              	 Code of the User Template

To view the country code, use the
                                    		  following URI:

```
GET https://<connection-server>/vmrest/languagemap
```

And to check language check; use last 2 characters of language check
                                    		  to change the country code.

The following is an example of the PUT request that updates the
                                    		  country code of a user template:

```
PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>
Request Body:
<UserTemplate>
    <Country>SA</Country>
</UserTemplate>
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To update the country code of a user template, do the following:

```
Request URI:
PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "Country":"XY"
}
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

#### Update Language of
                              	 User Template

To view the language code, use
                                    		  the following URI:

```
PUT https://<connection-server>/vmrest/languagemap
```

And check language code; use that language code to change language of
                                    		  user template.

The following is an example of the PUT request that updates the
                                    		  language of a user template:

```
PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>
Request Body:
<UserTemplate>
    <Language>1025</Language>
</UserTemplate>
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To update the language of a user template, do the following:

```
Request URI:
PUT https://<connection-server>/vmrest/usertemplates/< usertemplateobjectid >
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "Language":"1025"
}
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

#### Delete the User
                              	 Template

The following is an example of
                                    		  the DELETE request that can be used to delete a user template:

```
DELETE https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>
```

```
Response Code: 204
```

JSON Example

To delete a user template, do the following:

```
Request URI:
DELETE https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
```

```
Response Code: 204
```

#### Updating Password
                              	 Settings and Changing Passwords

Example 1: Updating voicemail password The following is an
                                    		  example of the PUT request that can be used to update the voicemail password:

```
PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/credential/pin
Request Body:
<UserTemplateCredential>
    <Credentials>142536</Credentials> 
</UserTemplateCredential>
```

The following is the response from the above *PUT* request for
                                    		  updating credentials and the actual response will depend upon the information
                                    		  given by you:

```
Response Code: 204
```

JSON Example

To update the credentials, do the following:

```
Request URI:
PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/credential/pin
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "Credentials":"10255"
}
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

Example 2: To update the fields The following is the response
                                    		  from the above *PUT* request for updating fields and the actual response will
                                    		  depend upon the information given by you:

```
Request Body:
<UserTemplateCredential>
    <DoesntExpire>true</DoesntExpire>
    <Locked>false</Locked>
    <CantChange>false</CantChange> 
    <CredMustChange>false</CredMustChange>
    <CredentialPolicyObjectId>58f0dc20-f8fc-467d-a648-b5ffbba87dd9</CredentialPolicyObjectId> 
</UserTemplateCredential>
```

```
Response Code: 204
```

```
GET https://<connection-server>/vmrest /authenticationrules
```

Example 3: Updating web application password The following is an
                                    		  example of the PUT request that can be used to update the web application
                                    		  password:

```
PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/credential/password
Request Body:
<UserTemplateCredential>
    <Credentials>Cisco123</Credentials> 
</UserTemplateCredential>
```

The following is the response from the above *PUT* request for
                                    		  updating credentials and the actual response will depend upon the information
                                    		  given by you:

```
Response Code: 204
```

JSON Example

To update the credentials, do the following:

```
Request URI:
PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/credential/password
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "Credentials":"10255",
    "CantChange":"false",
    "DoesntExpire":"true",
    "Locked":"false",
    "CredMustChange":"false",
    "CredentialPolicyObjectId":"7b282b66-73b1-4989-9d94-3d105b6ef5e8"
}
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

The following is the response from the above *PUT* request for
                                    		  updating fields and the actual response will depend upon the information given
                                    		  by you:

```
Request Body:
<UserTemplateCredential>
    <DoesntExpire>true</DoesntExpire>
    <Locked>false</Locked>
    <CantChange>false</CantChange> 
    <CredMustChange>false</CredMustChange>
    <CredentialPolicyObjectId>58f0dc20-f8fc-467d-a648-b5ffbba87dd9</CredentialPolicyObjectId> 
</UserTemplateCredential>
```

```
Response Code: 204
```

```
GET https://<connection-server>/vmrest /authenticationrules
```

#### Adding or Deleting
                              	 Roles

To view the roles object ID use
                                    		  the following URI:

```
GET https://<connection-server>/vmrest/roles
```

Example 1: Adding the roles The following is an example of the
                                    		  POST request that can be used to add the roles:

```
PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplateroles
Request Body:
<UserTemplateRole>
    <RoleObjectId>4f077e4e-61c7-4ce8-a58a-2c4bc6089319</RoleObjectId>
</UserTemplateRole>
```

The following is the response from the above *POST* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 201
```

JSON Example

To add the roles, do the following:

```
Request URI:
POST https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplateroles
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "RoleObjectId":"04d0f1ef-a8c6-454a-8cf0-0e8db7bb2b15"
}
```

The following is the response from the above *POST* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 201
```

Example 2: Viewing roles of user template The following is an
                                    		  example of the GET request that can be used to view the roles:

```
GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplateroles
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<UserTemplateRole>
    <URI>/vmrest/usertemplates/d8054a3a-6c09-4a25-9880-
    6589d2f1dc85/usertemplateroles/973e143e-af15-4ef4-a7c1-5fafd9cc53d4</URI>
    <ObjectId>973e143e-af15-4ef4-a7c1-5fafd9cc53d4</ObjectId>
    <UserObjectId>d8054a3a-6c09-4a25-9880-6589d2f1dc85</UserObjectId>
    <UserURI>/vmrest/users/d8054a3a-6c09-4a25-9880-6589d2f1dc85</UserURI>
    <RoleObjectId>ba166947-41e8-4ec9-ad14-03658d91240e</RoleObjectId>
    <RoleURI>/vmrest/roles/ba166947-41e8-4ec9-ad14-03658d91240e</RoleURI>
    <RoleName>Audit Administrator</RoleName>
    <Alias>ABCD_user template</Alias>
</UserTemplateRole>
```

```
Response Code: 200
```

JSON Example

To view the roles, do the following:

```
Request URI:
GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplateroles
Accept: application/json
Content_type: application/json
Connection: keep_alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
  "@total":"1"
  "UserTemplateRole":
  {
    "URI":"/vmrest/usertemplates/a9272189-720b-44b3-86e0-
    df7ef519599c/usertemplateroles/167b7661-ee8b-4c83-8867-decb88ec0c1c"
    "ObjectId":"167b7661-ee8b-4c83-8867-decb88ec0c1c"
    "UserObjectId":"a9272189-720b-44b3-86e0-df7ef519599c"
    "UserURI":"/vmrest/users/a9272189-720b-44b3-86e0-df7ef519599c"
    "RoleObjectId":"04d0f1ef-a8c6-454a-8cf0-0e8db7bb2b15"
    "RoleURI":"/vmrest/roles/04d0f1ef-a8c6-454a-8cf0-0e8db7bb2b15"
    "RoleName":"Help Desk Administrator"
    "Alias":"tenant005_usertemplate_1"
  }
}
```

```
Response Code: 200
```

Example 3: Delete role of user template The following is an
                                    		  example of the DELETE request that can be used to view the roles:

```
DELETE https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplateroles/<usertemplaterolesId>
```

The following is the response from the above *DELETE* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To delete role of user template, do the following:

```
Request URI:
DELETE https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplateroles/<usertemplateroleid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
```

The following is the response from the above *DELETE* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

#### Explanation of
                              	 Data Fields

- False: The
                                                         						  language is the default language defined for the user template.

- True: The
                                                         						  language is derived from the location to which this user template belongs.

Default value: False

- False: The time
                                                         						  zone is the default time zone defined for the user template.

- True: The time
                                                         						  zone is derived from the location to which this user template belongs.

Default value: False

Possible options are:

- 0=LastNameFirst

- 1=Extension

- 2=FirstNameFirst

Possible options are:

- 0=SystemDefaultClock

- 1=HourClock12

- 2=HourClock24

Values can be:

- False: Do not
                                                         						  play the name.

- True: Play the
                                                         						  recorded voice name.

Default value: True

Possible values can be:

- False: Do not
                                                         						  list the subscriber in the phone directory.

- True: List the
                                                         						  subscriber in the phone directory.

Default value: True

Values can be:

- False: The
                                                         						  enrollment conversation is not played for the subscriber when they login.

- True: The
                                                         						  enrollment conversation is played for the subscriber when they login.

Default value: True

Values can be:

- False: Do not
                                                         						  announce copied names.

- True: Announce
                                                         						  copied names.

Default value: True

Values can be:

- False: Do not
                                                         						  announce the distribution list.

- True: Announce
                                                         						  the distribution list.

Default value: True

Values can be:

- False: Do not
                                                         						  play the message number.

- True: Play the
                                                         						  message number.

Default value: True

Values can be:

- False: Do not
                                                         						  announce the sender.

- True: Announce
                                                         						  the sender.

Default value: True

Values can be:

- False: Do not
                                                         						  announce the timestamp after each message is played.

- True: Announce
                                                         						  the timestamp after each message is played.

Default value: True

Values can be:

- False: Do not
                                                         						  announce the timestamp before each message is played.

- True Announce
                                                         						  the timestamp before each message is played.

Default value: False

Values can be:

- False: Do not
                                                         						  announce total number of new messages.

- True: Announce
                                                         						  the total number of new messages in the subscriber mailbox.

Default value: False

Values can be:

- False: Do not
                                                         						  announce total number of new e-mail messages.

- True: Announce
                                                         						  the total number of new e-mail messages in the subscriber mailbox.

Default value: False

Values can be:

- False: Do not
                                                         						  announce total number of new fax messages.

- True: Announce
                                                         						  the total number of new fax messages in the subscriber mailbox.

Default value: False

Values can be:

- False: Do not
                                                         						  announce total number of new voice messages.

- True: Announce
                                                         						  the total number of new voice messages in the subscriber mailbox.

Default value: True

Values can be:

- False: Do not
                                                         						  announce total number of new receipts.

- True: Announce
                                                         						  the total number of new receipts in the subscriber mailbox.

Default value: False

Values can be:

- False: Do not
                                                         						  announce total number of saved messages.

- True: Announce
                                                         						  the total number of saved messages in the subscriber mailbox.

Default value: True

Default value: False

Values can be:

- False: Ring the
                                                         						  phone.

- True: Send the
                                                         						  caller to the alternate greeting.

Default value: False

Values can be:

- False: If
                                                         						  alternate greeting is active, callers cannot skip the greeting\

- True: If
                                                         						  alternate greeting is active, callers can skip the greeting.

Default value: False

Values can be:

- False: If
                                                         						  alternate greeting is active, callers can leave a message for the subscriber

- True: If
                                                         						  alternate greeting is active, callers cannot leave a message for the
                                                         						  subscriber.

Default value: False

Values can be:

- False: Do not
                                                         						  encrypt private messages.

- True: Encrypt
                                                         						  private messages.

Default value: False

Values can be:

- False: Do not
                                                         						  notify the subscriber that their alternate greeting is turned on.

- True: Notify the
                                                         						  subscriber when they login if their alternate greeting is turned on.

Default value: False

Values can be:

- False: Do not
                                                         						  play the extension information of the subscriber who sent the message.

- True: After
                                                         						  playing the sender's voice name, play the primary extension information of the
                                                         						  subscriber who sent the message.

Default value: False

Default value: False

Values can be:

- False: The user
                                                         						  credential will automatically expire. The expiration of the credential is
                                                         						  controlled by the value of the column tbl_CredentialPolicy->MaxDays.

- True: The user
                                                         						  credential will not automatically expire.

Default value: False

Values can be:

- False: User is
                                                         						  allowed to change their credential.

- True: User
                                                         						  cannot change their credential.

Default value: False

- Urgent voice
                                                         						  messages

- Non-urgent voice
                                                         						  messages

- Urgent fax
                                                         						  messages

- Non-urgent fax
                                                         						  messages

- Urgent e-mail
                                                         						  messages

- Non-urgent
                                                         						  e-mail messages

- Receipts and
                                                         						  notices

- Urgent voice
                                                         						  messages

- Non-urgent voice
                                                         						  messages* Urgent fax messages

- Non-urgent fax
                                                         						  messages

- Urgent e-mail
                                                         						  messages

- Non-urgent
                                                         						  e-mail messages

- Receipts and
                                                         						  notices

Values can be:

- False: Do not
                                                         						  play message type menu.

- True: Play
                                                         						  message type menu.

Default value: False

Values can be:

- False: Call
                                                         						  routing rules disabled for subscriber.

- 1: Call routing
                                                         						  rules enabled for subscriber.

- True: Call
                                                         						  routing rules enabled for subscriber.

Default value: True

Default value: True

Default value: False

Values can be:

- False: Prompt
                                                         						  subscriber to address message before recording.

- True: Prompt
                                                         						  subscriber to address message after recording.

Default value: False

Values can be:

- False: system
                                                         						  will not request confirmation from a subscriber before proceeding with a
                                                         						  deletion of a single new or saved message.

- True: system
                                                         						  will request confirmation from a subscriber before proceeding with a deletion
                                                         						  of a single new or saved message.

Default value: False

Values can be:

- False: System
                                                         						  does not prompt the subscriber to choose, and instead permanently deletes the
                                                         						  type of messages you specify: either deleted voice messages or all deleted
                                                         						  messages (voice, fax, and e-mail, as applicable).

- True: System
                                                         						  allows the subscriber to choose which messages they want to delete; subscriber
                                                         						  can either delete their deleted voice messages or delete all of their deleted
                                                         						  messages.

Default value: True

Values can be:

- False: 12-Hour
                                                         						  clock - The subscriber hears message timestamps in the time format of a 12-hour
                                                         						  clock. For example, a subscriber will hear 1:00 PM when listening to the
                                                         						  timestamp of a message left at 1:00 PM.

- True: 24-Hour
                                                         						  clock - The subscriber hears message timestamps in the time format of a 24-hour
                                                         						  clock. For example, a subscriber will hear 13:00 when listening to the
                                                         						  timestamp of a message left at 1:00 PM.

Default value: False

Values can be:

- 0: Disable

- 1: Enable

Values can be:

- 1: The quota is
                                                         						  unlimited.

- 2: The default
                                                         						  system quota is assigned.

Values can be:

- 1: The quota is
                                                         						  unlimited.

- 2: The default
                                                         						  system quota is assigned.

Values can be:

- 1: The quota is
                                                         						  unlimited.

- 2: The default
                                                         						  system quota is assigned.

Values can be:

- False: Cannot
                                                         						  send broadcast messages.

- True: Can send
                                                         						  broadcast messages.

Default value: False

Values can be:

- False: Cannot
                                                         						  update broadcast messages.

- True: Can update
                                                         						  broadcast messages.

Default value: False

Values can be:

- False: Speech
                                                         						  recognition conversation is not default conversation for the subscriber.

- True: Speech
                                                         						  recognition conversation is the default conversation for the subscriber.

Default value: False

Default value: False

Values can be:

- False:
                                                         						  Subscriber conversation does not jump directly to first message in the message
                                                         						  stack after subscriber sign-in.

- True: Subscriber
                                                         						  conversation jumps directly to the first message in the message stack after
                                                         						  subscriber sign-in.

Default value: True

Values can be:

- False: Message
                                                         						  locator feature is disabled for subscriber.

- True: Message
                                                         						  locator feature is enabled for subscriber.

Default value: False

Values can be:

- False: TTS is
                                                         						  disabled for the subscriber.

- True: TTS is
                                                         						  enabled for the subscriber

Default value: True

Values can be:

- False: Visual
                                                         						  message locator feature disabled for subscriber.

- True: Visual
                                                         						  message locator feature enabled for subscriber.

Default value: False

Values can be:

- False: Unity
                                                         						  Connection prompts subscribers to press 1 to add more recipients.

- True: Unity
                                                         						  Connection does not prompt subscribers to press 1 to add more recipients.
                                                         						  Instead, subscribers continue entering recipient names or extensions (as
                                                         						  applicable) until they indicate that they have completed addressing.

Default value: False

Values can be:

- False: No voice
                                                         						  name played.

- True: Voice name
                                                         						  of subscriber or DL is played.

Default value: False

Default value: 1500 Range: 250-5000

Values can be:

- False: Message
                                                         						  is marked new again.

- True: Message is
                                                         						  marked read.

Default value: False

Default Value: 5000 Range: 1000-60000

Default Value: 5000 Range: 1000-60000

Values can be:

- False: The
                                                         						  subscriber's polling cycle is determined by the system default polling cycle.
                                                         						  (default value) (System configuration setting "Normal Calendar Caching Poll
                                                         						  Interval").

- True: The
                                                         						  shorter "power user" polling cycle is used. (System configuration setting
                                                         						  "Short Calendar Caching Poll Interval").

Default value: False

Values can be:

- False: Message
                                                         						  Bookmark feature is disabled for subscriber.

- True: Message
                                                         						  Bookmark feature is enabled for subscriber.

Default value: False

Values can be:

- False: Do not
                                                         						  announce total number of draft messages.

- True: Announce
                                                         						  the total number of draft messages in the subscriber mailbox.

Default value: False

Values can be:

- False: Do not
                                                         						  save draft messages.

- True: Save draft
                                                         						  messages.

Default value: False

Default value: False

Default value: False

Values can be:

- False: Do not
                                                         						  automatically skip to the next message after playing the after message menu
                                                         						  once.

- True: Do
                                                         						  advanced automatically to the next message after playing the after message menu
                                                         						  once.

Default value: False

Default value: False

Default value: False

Default value: False

Default value: False

Default value: False

| GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid> |
|---|

| GET https://<connection-server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId> |
|---|

| PUT https://<connection-server>/vmrest/handlers/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/menuentries |
|---|

| Request Body:
<CallhandlerPrimaryTemplate>
    <OneKeyDelay>9999</OneKeyDelay>
    <EnablePrependDigits>true</EnablePrependDigits>
    <PrependDigits>4545</PrependDigits>
</CallhandlerPrimaryTemplate> |
|---|

| Response Code: 204 |
|---|

| Note | <PrependDigit> parameter must be having digits only
                                                			 (extension parameter) |
|---|---|

| Values | Parameters |
|---|---|
| 0 | Ignore |
| 1 | Hang Up |
| 4 | Take Message |
| 5 | Skip Greeting |
| 6 | Restart Greeting |
| 7 | Transfer to alternate contact number |
| 8 | Route from next call routing rule |

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
| EnablePrependDigits | Boolean | Read/Write | To simulate abbreviated extensions by using
                                                					 prepended digits for call handlers and user mailboxes. When such digits are
                                                					 defined, they are prepended to any extension that a caller dials while
                                                					 listening to the greeting for the call handler or user mailbox. Default value: false. |
| PrependDigits | Integer | Read/Write | Digits that are prepended to any extension
                                                					 that a caller dials while listening to the greeting of the user. |
| MenuEntriesURI | String(36) | Read Only | Parameters for caller input keys are
                                                					 present in menu entries URI. |
| TouchtoneKey | String(1) | Read Only | Indicates the phone keypad key to which the
                                                					 settings apply. |
| Locked | Boolean | Read/Write | A locked menu entry does not allow
                                                					 additional dialing after this choice is entered. Values can be: False: Unlocked
                                                         						  - Additional dialing after this choice is entered is allowed True: Locked -
                                                         						  Additional dialing is ignored Default value: false. |
| Action | Integer | Read/Write | Takes values from 0-8. See table for
                                                					 values. |
| CallHandlerObjectId | String(36) | Read Only | Menu entries can only belong to call
                                                					 handlers. No other object can own a menu entry. |
| TargetConversation | String(36) | Read/Write | The name of the conversation to which the
                                                					 caller is routed. |
| TargetHandlerObjectId | String(36) | Read/Write | The unique identifier of the specific
                                                					 object to send along to the target conversation. |
| TransferNumber | Integer | Read/Write | Extension to which call is transferred. |
| TransferType | Integer | Read/Write | Values can be: 0: Release to
                                                         						  switch 1: Supervise
                                                         						  transfer |
| TransferRings | Integer | Read/Write | Applies only when the "TransferType" column
                                                					 is set to supervised (1). This value should never be less than 2 for a
                                                					 supervised transfer. |

| Note | This option
                                                                     								is unavailable if Ignore Caller Input is enabled on the Greetings page. OneKeyDelay
                                                                     								can only accept integer with value 0 through 10000 |
|---|---|

| GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid> |
|---|

| GET https://<connection-
    server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId> |
|---|

| GET https://<connection- 
    server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId 
    >/usertemplategreetings |
|---|

| GET https://<connection-
    server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId
    >/usertemplategreetings/Alternate |
|---|

| GET https://<connection-
    server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId
    >/usertemplategreetings/Busy |
|---|

| GET https://<connection-
    server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId
    >/usertemplategreetings/Error |
|---|

| GET https://<connection-
    server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId
    >/usertemplategreetings/Off%20Hours |
|---|

| GET https://<connection-
    server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId
    >/usertemplategreetings/Standard |
|---|

| GET https://<connection-
    server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId
    >/usertemplategreetings/Holiday |
|---|

| PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Alternate |
|---|

| <Greeting>
  <EnableTransfer>true</EnableTransfer>
</Greeting> |
|---|

| Response Code: 204 |
|---|

| <Greeting>
  <EnableTransfer>true</EnableTransfer>
  <TimeExpires></TimeExpires>
</Greeting> |
|---|

| Response Code: 204 |
|---|

| <Greeting>
  <EnableTransfer>true</EnableTransfer>
  <TimeExpires>2014-12-31 05:30:00.000</TimeExpires>
</Greeting> |
|---|

| Response Code: 204 |
|---|

| <Greeting>
  <PlayWhat>2</PlayWhat>
  <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt>  
</Greeting> |
|---|

| Response Code: 204 |
|---|

| <Greeting>
  <IgnoreDigits>true</IgnoreDigits>
</Greeting> |
|---|

| Response Code: 204 |
|---|

| <Greeting>
  <IgnoreDigits>false</IgnoreDigits>
  <EnableTransfer>true</EnableTransfer>
</Greeting> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Alternate
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| {
  "EnableTransfer":"true","IgnoreDigits":"false"
} |
|---|

| Response Code: 204 |
|---|

| Request Body:
<UserTemplateGreeting>
    <AfterGreetingAction>8</AfterGreetingAction>
</UserTemplateGreeting> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/callhandlerprimarytemplates/6bcd837d-f1cf-43c2-b199-85b457858a16/usertemplategreetings/Alternate
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| Request Body:
{

   "AfterGreetingAction":"8"

} |
|---|

| Response Code: 204 |
|---|

| Note | Values used for changing call actions are - 1,4,6,8 |
|---|---|

| Request Body:
<UserTemplateGreeting>
    <AfterGreetingAction>2</AfterGreetingAction>
    <AfterGreetingTargetConversation>PHTransfer</AfterGreetingTargetConversation>
    <AfterGreetingTargetHandlerObjectId>ee065a6a-3f95-4b4d-bbbd-98cb2d4c0aa9</AfterGreetingTargetHandlerObjectId>
</UserTemplateGreeting> |
|---|

| Response Code: 204 |
|---|

| Note | For attempt transfer use PHTransfer and for go directly to
                                                			 greetings use PHGreeting and AfterGreetingTargetHandlerObjectId can be viewed
                                                			 from URI: |
|---|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers |
|---|

| Request Body:
<UserTemplateGreeting>
    <AfterGreetingAction>2</AfterGreetingAction>
    <AfterGreetingTargetConversation>PHInterview</AfterGreetingTargetConversation>
    <AfterGreetingTargetHandlerObjectId>2f6a0058-7535-48ac-abcd-c4b41d13f47e</AfterGreetingTargetHandlerObjectId>
</UserTemplateGreeting> |
|---|

| Response Code: 204 |
|---|

| Note | AfterGreetingTargetHandlerObjectId can be viewed from URI: |
|---|---|

| GET https://<connection-server>/vmrest/handlers/interviewhandler |
|---|

| Request Body:
<UserTemplateGreeting>
    <AfterGreetingAction>2</AfterGreetingAction>
    <AfterGreetingTargetConversation>AD</AfterGreetingTargetConversation>
    <AfterGreetingTargetHandlerObjectId>1f1941a5-3bb7-47ee-96f9-78691cd8ad43</AfterGreetingTargetHandlerObjectId>
</UserTemplateGreeting> |
|---|

| Response Code: 204 |
|---|

| Note | AfterGreetingTargetHandlerObjectId can be viewed from URI: |
|---|---|

| GET https://<connection-server>/vmrest/handlers/directoryhandler |
|---|

| Request Body: for broadcast message administrator
<UserTemplateGreeting>
    <AfterGreetingAction>2</AfterGreetingAction>
    <AfterGreetingTargetConversation>BroadcastMessageAdministrator</AfterGreetingTargetConversation>
</UserTemplateGreeting> |
|---|

| Response Code: 204 |
|---|

| Request Body: for caller system transfer
<UserTemplateGreeting>

   <AfterGreetingAction>2</AfterGreetingAction>
   <AfterGreetingTargetConversation>SystemTransfer</AfterGreetingTargetConversation>

</UserTemplateGreeting> |
|---|

| Response Code: 204 |
|---|

| Request Body: for greeting administrator
<UserTemplateGreeting>

   <AfterGreetingAction>2</AfterGreetingAction>
   <AfterGreetingTargetConversation>GreetingsAdministrator</AfterGreetingTargetConversation>

</UserTemplateGreeting> |
|---|

| Response Code: 204 |
|---|

| Request Body: for sign in
<UserTemplateGreeting>

   <AfterGreetingAction>2</AfterGreetingAction>
   <AfterGreetingTargetConversation>SubSignIn</AfterGreetingTargetConversation>

</UserTemplateGreeting> |
|---|

| Response Code: 204
Request Body: for user system transfer
<UserTemplateGreeting>
    <AfterGreetingAction>2</AfterGreetingAction>
    <AfterGreetingTargetConversation>SubSysTransfer</AfterGreetingTargetConversation>
</UserTemplateGreeting> |
|---|

| Response Code: 204 |
|---|

| <UserTemplateGreeting>
    <AfterGreetingAction>2</AfterGreetingAction>
    <AfterGreetingTargetConversation>PHTransfer</AfterGreetingTargetConversation>
    <AfterGreetingTargetHandlerObjectId>92a9008d-9e18-4cd1-8e3c-10df32295cd8</AfterGreetingTargetHandlerObjectId>
</UserTemplateGreeting> |
|---|

| Response Code: 204 |
|---|

| <UserTemplateGreeting>
    <EnAltGreetDontRingPhone>true</EnAltGreetDontRingPhone>
    <EnAltGreetPreventSkip>true</EnAltGreetPreventSkip>
    <EnAltGreetPreventMsg>true</EnAltGreetPreventMsg>
</UserTemplateGreeting> |
|---|

| Response Code: 204 |
|---|

| POST https://<connection-
server>/vmrest/callhandlerprimarytemplates/<Callhandlerprimarytempl
atesObjectId>/usertemplategreetings/Alternate/greetingstreamfiles |
|---|

| Response Code: 201 |
|---|

| GET http://<connection-server>/vmrest/Callhandlersprimarytemplates/<callhandlerobjectid>/usertemplates/Greetings/<GreetingType>/GreetingStreamFiles/<language>/video |
|---|

| Response: 200
<CallControl>
    <resourceId>aad91d6d-aeca-4a72-8069-b656efb3041f.wav</resourceId>
    <sessionId>570146ed1504cb1</sessionId>
</CallControl |
|---|

| Request 
GET  vmrest/handlers/callhandlers/30600b21-1a4c-47a3-a078-8078984e5376/greetings/Standard/greetingstreamfiles/1033/video
Accept: application/json
User-Agent: Java/1.6.0_17
Host: <connection-server>
Connection: keep-alive
authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg= |
|---|

| Response
HTTP/1.1 200
Content-Type: application/json
Date: Fri, 15 Jan 2010 15:14:11 GMT
Server:
{ “resourceId” :” aad91d6d-aeca-4a72-8069-b656efb3041f.wav”, “sessionId” : ”570146ed1504cb1”} |
|---|

| PUT http://<connection-server>/vmrest/Callhandlersprimarytemplates/<callhandlerobjectid>/usertemplates/Greetings/<GreetingType>/GreetingStreamFiles/<language>/video |
|---|

| <CallControl>
     <resourceId>aad91d6d-aeca-4a72-8069-b656efb3041f.wav</resourceId>
     <sessionId>570146ed1504cb1</sessionId>
</CallControl> |
|---|

| Response: 204 OK |
|---|

| Request 
PUT  vmrest/handlers/callhandlers/30600b21-1a4c-47a3-a078-8078984e5376/greetings/Standard/greetingstreamfiles/1033/video
Content-Type: application/json
Accept: application/json
Host: <connection-server>
Connection: keep-alive
authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==

{ “resourceId” :” aad91d6d-aeca-4a72-8069-b656efb3041f.wav”, “sessionId” : ”570146ed1504cb1”} |
|---|

| Response :
HTTP/1.1 204
Content-Type: application/json
Date: Fri, 15 Jan 2010 15:14:11 GMT
Server: |
|---|

| Parameter | Data Type | Operations | Comments |
|---|---|---|---|
| CallHandlerObjectId | String(36) | Read Only | The unique identifier of the call handler
                                                					 object to which this greeting rule belongs. |
| IgnoreDigits | Boolean | Read/Write | A flag indicating whether Cisco Unity
                                                					 Connection takes action in response to touchtone keys pressed by callers during
                                                					 the greeting. Values can be: False: Caller
                                                         						  input enabled during greeting True: Caller
                                                         						  input ignored during greeting Default Value: False |
| PlayWhat | Integer(2) | Read/Write | The source for the greeting when this
                                                					 greeting is active. Default Value: 0 Default Values can be: Call handler - 1
                                                         						  (recording) Subscriber - 0
                                                         						  (system) |
| RepromptDelay | Integer(2) | Read/Write | The amount of time (in seconds) that Cisco
                                                					 Unity Connection waits without receiving any input from a caller before Cisco
                                                					 Unity Connection prompts the caller again. Default Value:2 Values can be: 0: Do wait
                                                         						  without receiving caller input and do not replay greeting. 1 or greater:
                                                         						  Wait this number of seconds without receiving any input from the caller before
                                                         						  playing the greeting again. |
| Reprompts | Integer(2) | Read/Write | The number of times to reprompt a caller.
                                                					 After the number of times indicated here, Cisco Unity Connection performs the
                                                					 after-greeting action. Default Value: 0 Values can be: 0: Do not
                                                         						  reprompt - Cisco Unity Connection will play the greeting once and then the
                                                         						  after-greeting action is taken. 1 or greater:
                                                         						  Number of times to reprompt. |
| TimeExpires | DateTime(8) | Read/Write | The date and time when the greeting rule
                                                					 expires. The greeting rule is considered not expired (enabled), if the value is
                                                					 NULL or a future date. The greeting rule is considered expired (disabled), the
                                                					 value is in the past. |
| GreetingType | String(12) | Read Only | The type of greeting, e.g. "Standard," "Off
                                                					 Hours," "Busy," etc. |
| AfterGreetingAction | Integer(2) | Read/Write | AfterMessageAction can only accept integer
                                                					 with value 1, 2, 4, 6, 8 Values can be: 1: Hang up 2. for other
                                                         						  actions with object id (call handler, interview handler, directory handler) 4. Take Message 6. Restart
                                                         						  greeting 8: Route from
                                                         						  next call routing rule. |
| AfterGreetingActionObjectId | String(36) | Read/Write | The unique identifier of the CallAction
                                                					 object that determines what action Cisco Unity Connection will take on the call
                                                					 after the greeting is played. |
| PlayRecordMessagePromp | Integer(2) | Read/Write | A flag indicating whether the "Record your
                                                					 message at the tone…" prompt prior to recording a message. Values can be: 0: System will
                                                         						  not play the "Record your message at the tone…" prompt prior to recording a
                                                         						  message. 1: System will
                                                         						  play the "Record your message at the tone…" prompt prior to recording a
                                                         						  message. Default Value: 1 |
| EnableTransfer | Boolean | Read/Write | A flag indicating when an extension is
                                                					 dialed at the greeting and the extension is not available whether to transfer
                                                					 to another extension. Default value: 0 Values can be: 0: User cannot
                                                         						  be transferred to another extension. 1: User can "be
                                                         						  transferred to another extension." |
| EnablePersonalVideoRecording | Boolean | Read/Write | A flag indicating whether the personal
                                                					 video recording of the user will be used. Values: true : Personal
                                                         						  Video Recording is enabled. false : Personal
                                                         						  Video Recording is not enabled. Default value : false |
| PlayRecordVideoMessagePrompt | Boolean | Read/Write | A flag indicating whether Cisco Unity
                                                					 Connection will prompt callers to wait for a tone before recording their video
                                                					 message. Values: true : Callers
                                                         						  will be prompted with a tone before recording their video message. false : Callers
                                                         						  will not be prompted with a tone before recording their video message. Default value : false This flag is editable only when the flag
                                                   						EnablePersonalVideoRecording is set to True. |
| EnAltGreetDontRingPhone | Boolean | Read/Write | Transfer Callers to Greeting without
                                                					 Ringing User's Phone |
| EnAltGreetPreventSkip | Boolean | Read/Write | Prevent Callers from Skipping the User's
                                                					 Greeting |
| EnAltGreetPreventMsg | Boolean | Read/Write | Prevent Callers from Leaving Messages |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

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

| GET https://<connection-server>/vmrest/voicemailboxstores
Request Body:
<UserTemplate>
    <MailboxStoreObjectId>9dfffae1-eae2-4eab-abe9-7b0773881d54</MailboxStoreObjectId>
</UserTemplates> |
|---|

| Response Code: 204 |
|---|

| Note | Input should be in bytes, that is multiple of 1024. |
|---|---|

| GET https://<connection server>/vmrestvmrest/usertemplates/<usertemplateobjectid> |
|---|

| GET https://<connection-
    server>/vmrestvmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId> |
|---|

| PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId> |
|---|

| <Callhandler>
  <EditMsg>true</EditMsg>
  <MaxMsgLen>1000</MaxMsgLen>
  <AfterMessageAction>1</AfterMessageAction>
  <SendUrgentMsg>2</SendUrgentMsg>
  <UseCallLanguage>false</UseCallLanguage>
  <SendSecureMsg>false</SendSecureMsg
  <SendPrivateMsg>1</SendPrivateMsg>
  <PlayAfterMessage>2</PlayAfterMessage>
</Callhandler> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| {
  "AfterMessageAction":"2",
  "AfterMessageTargetConversation":"SystemTransfer"
} |
|---|

| Response code: 204 |
|---|

| PUT
https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId> |
|---|

| <Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>PHGreeting</AfterMessageTargetConversation>      
  <AfterMessageTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</AfterMessageTargetHandlerObjectId> 
</Callhandler> |
|---|

| Response Code: 204 |
|---|

| <Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</AfterMessageTargetHandlerObjectId>
  <AfterMessageTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</AfterMessageTargetHandlerObjectId>
</Callhandler> |
|---|

| GET https://<connection-server>/vmrest/handlers/interviewhandlers |
|---|

| Response Code: 204 |
|---|

| <Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>AD</AfterMessageTargetConversation>
  <AfterMessageTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</AfterMessageTargetHandlerObjectId>  
</Callhandler> |
|---|

| GET https://<connection-server>/vmrest/handlers/directoryhandlers |
|---|

| Response Code: 204 |
|---|

| <Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>BroadcastMessageAdministrator</AfterMessageTargetConversation>
</Callhandler> |
|---|

| Response Code: 204 |
|---|

| <Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>SystemTransfer</AfterMessageTargetConversation>
</Callhandler> |
|---|

| Response Code: 204 |
|---|

| <Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>GreetingAdministrator</AfterMessageTargetConversation>
</Callhandler> |
|---|

| Response Code: 204 |
|---|

| <Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>SubSignIn</AfterMessageTargetConversation>
</Callhandler> |
|---|

| Response Code: 204 |
|---|

| Request Body:
<CallhandlerPrimaryTemplate>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>SubSysTransfer</AfterMessageTargetConversation>
</CallhandlerPrimaryTemplate> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive
Request Body:
{
  "AfterMessageAction":"2",
  "AfterMessageTargetConversation":"SystemTransfer"
} |
|---|

| Response Code: 204 |
|---|

| Parameter | Ojects | Data Type | Comments |
|---|---|---|---|
| MaxMsgLen | Integer | Read/Write | The maximum recording length (in seconds) for messages left by unidentified callers. Default value : 300 Range: 1-3600 |
| EditMsg | Boolean | Read/Write | Allows callers to be prompted to listen to, add to, rerecord, or delete their messages. Values can be: False: Callers cannot edit messages True: Callers can edit messages Default value: True |
| UseDefaultLanguage | Boolean | Read/Write | Values can be: False: The language is the default language defined for the call handler template. True: The language is derived from the location to which this call handler template belongs. Default value: False |
| UseCallLanguage | Boolean | Read/Write | This flag allows that language to be the language used by handlers in the system to play prompts for users. Values can be: False: Do not use the language specified by the system call routing rule to play prompts for users True: Use the language specified by the system call routing rule to play prompts for users Default value: False |
| SendUrgentMsg | Integer | Read/Write | A flag indicating whether an unidentified caller can mark a message as "urgent." Values can be: 0: Never - messages left by unidentified calls are never marked urgent. 1: Always - all messages left by unidentified callers are marked urgent. 2: Ask - Cisco Unity Connection asks unidentified callers whether to mark their messages urgent. |
| SendPrivateMsg | Integer | Read/Write | Determines if an outside caller can mark their message as private. Values can be: 0: Never - No messages are marked private. 1: Always - All messages are marked private. 2: Ask - Ask the outside caller if they wish to mark the message as private. |
| SendSecureMsg | Boolean | Read/Write | A flag indicating whether an unidentified caller can mark a message as "secure." Values can be: 0: Never - messages left by unidentified calls are never marked secure. 1: Always - all messages left by unidentified callers are marked secure. |
| PlayAfterMessage | Integer | Read/Write | Indicates whether the Sent Message Prompt Recording referenced by Post Greeting Values can be: 0: Do not play recording 1: System default recording 2: Play recording |
| AfterMessageAction | Integer | Read/Write | AfterMessageAction can only accept integer with value 1 or 8 or 2 Values can be: 1: Hang up 8: Route from next call routing rule. |

| GET https://<connection server>/vmrestvmrest/usertemplates/<usertemplateobjectid> |
|---|

| GET https://<connection 
server>/vmrestvmrest/usertemplates/<usertemplateobjectid>/usertemplatemessageactions/<usertempl
atemessageactionsobjectid> |
|---|

| Request URI
PUT https://<connection server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplatemessageactions/<objectid>
Request Body:
<UserTemplateMessageAction>
    <VoicemailAction>3</VoicemailAction>
    <RelayAddress>%texoma%@tenant.com</RelayAddress> 
</UserTemplateMessageAction> |
|---|

| Response Code: 204 |
|---|

| Request URI:
PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplatemessageactions/<objectid>
Accept: application/json
Content-type: application/json
Connection: keep-alive
Request Body:
{
    "VoicemailAction":"3"
    "RelayAddress":"texoma@tenant.com"
} |
|---|

| Response Code: 204 |
|---|

| Note | For relay message and accept and relay message option relay address is mandatory and relay address must be correct for e.g.:
                                             tenant@cisco.com In the same way all other actions can be edited like: Voicemail Action, Email Action, Fax Action and Delivery
                                             Receipt Action |
|---|---|

| Parameter | Data Types | Operation | Comments |
|---|---|---|---|
| VoicemailAction | Integer | Read/Write | The action to take for voicemail messages. Values can be: 0: Reject the Message 1: Accept the Message 2: Relay the Message 3: Accept and Relay the Message For 2 and 3, values have to provide RelayAddress. |
| EmailAction | Integer | Read/Write | The action to take for email messages. Values can be: 0: Reject the Message 1: Accept the Message 2: Relay the Message 3: Accept and Relay the Message For 2 and 3, values have to provide RelayAddress. |
| FaxAction | Integer | Read/Write | The action to take for fax messages. Values can be: 0: Reject the Message 1: Accept the Message 2: Relay the Message 3: Accept and Relay the Message For 2 and 3, values have to provide RelayAddress. |
| DeliveryReceiptAction | Integer | Read/Write | The action to take for delivery receipt messages. Values can be: 0: Reject the Message 1: Accept the Message 2: Relay the Message 3: Accept and Relay the Message For 2 and 3, values have to provide RelayAddress. |
| RelayAddress | String (320) | Read/Write | Select the address to which system relays voicemail, email, fax, or delivery receipts when Connection is configured to relay
                                             that message type. This field is not editable unless you have selected Relay the Message or Accept and Relay the Message as
                                             the message action for one or more message types. Note In order to configure Connection to relay messages, you must first configure an SMTP Smart Host on the System Settings > SMTP
                                                         Configuration > Smart Host page. Enter a combination of text and tokens that Connection replaces with a value from the user
                                                         profile. (For example, Connection replaces %Alias% with the alias from each user profile when editing the corresponding user.) | Note | In order to configure Connection to relay messages, you must first configure an SMTP Smart Host on the System Settings > SMTP
                                                         Configuration > Smart Host page. Enter a combination of text and tokens that Connection replaces with a value from the user
                                                         profile. (For example, Connection replaces %Alias% with the alias from each user profile when editing the corresponding user.) |
| Note | In order to configure Connection to relay messages, you must first configure an SMTP Smart Host on the System Settings > SMTP
                                                         Configuration > Smart Host page. Enter a combination of text and tokens that Connection replaces with a value from the user
                                                         profile. (For example, Connection replaces %Alias% with the alias from each user profile when editing the corresponding user.) |

| Note | In order to configure Connection to relay messages, you must first configure an SMTP Smart Host on the System Settings > SMTP
                                                         Configuration > Smart Host page. Enter a combination of text and tokens that Connection replaces with a value from the user
                                                         profile. (For example, Connection replaces %Alias% with the alias from each user profile when editing the corresponding user.) |
|---|---|

| GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid> |
|---|

| https://<connectionserver>/vmrest/usertemplates/<usertemplateobjectid>/usertemplatenotificationdevices |
|---|

| GET https://<connection-
    server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplatenotificationdevices/usertemplatepagerdevic
    es/<usertemplatenotificationdeviceobjectId>
Request Body: Updating Pager
<UserTemplatePagerDevice>
    <Active>true</Active>    
    <DisplayName>Pager1</DisplayName>
    <InitialDelay>1</InitialDelay>
    <RepeatNotify>true</RepeatNotify> 
    <RepeatInterval>1</RepeatInterval>
    <EventList>AllMessage</EventList> 
    <RetriesOnBusy>4</RetriesOnBusy>
    <BusyRetryInterval>5</BusyRetryInterval>
    <RetriesOnRna>4</RetriesOnRna>
    <RnaRetryInterval>15</RnaRetryInterval>
    <RetriesOnSuccess>0</RetriesOnSuccess>
</UserTemplatePagerDevice> |
|---|

| Response Code: 204 |
|---|

| Note | To activate notification device <PhoneNumber> parameter is mandatory and <RepeatInterval > parameter is mandatory to enable
                                             repeat notify. The provide values can be changed and values are given in above table. |
|---|---|

| GET https://<connectionserver>/vmrestvmrest/usertemplates/<usertemplateobjectid>/usertemplatenotificationdevices/
usertemplatepagerdevices/<usertemplatenotificationdeviceobjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| {
    "URI":"/vmrest/usertemplates/6164ac2d-e8ec-441a-93a0-95f8e18a655c/usertemplatenotificationdevices/usertemplatepagerdevices/ad6bdb87-7ab6-4a2a-b4fb-5dae6fd6804c"
    "TransmitForcedAuthorizationCode":"false"
    "BusyRetryInterval":"5"
    "DialDelay":"1"
    "RetriesOnBusy":"4"
    "RetriesOnRna":"4"
    "RingsToWait":"4"
    "RnaRetryInterval":"15"
    "SendCount":"true"
    "WaitConnect":"true"
    "MediaSwitchObjectId":"0ad0b88c-4a70-4cf7-913e-d5d7a921caca"
    "PhoneSystemURI":"/vmrest/phonesystems/0ad0b88c-4a70-4cf7-913e-d5d7a921caca"
    "ObjectId":"ad6bdb87-7ab6-4a2a-b4fb-5dae6fd6804c"
    "Active":"false"
    "DeviceName":"Pager"
    "DisplayName":"Pager"
    "MaxBody":"512"
    "MaxSubject":"64"
    "SubscriberObjectId":"6164ac2d-e8ec-441a-93a0-95f8e18a655c"
    "UserURI":"/vmrest/users/6164ac2d-e8ec-441a-93a0-95f8e18a655c"
    "SendCallerId":"true"
    "Undeletable":"true"
    "SuccessRetryInterval":"1"
    "RetriesOnSuccess":"0"
    "EventList":"NewVoiceMail"
    "ScheduleSetObjectId":"5fc5a5d7-eaf6-4f4d-80cf-f76f3893ac0e"
    "InitialDelay":"0"
    "RepeatInterval":"0"
    "RepeatNotify":"false"
} |
|---|

| Response Code: 200 |
|---|

| Parameter | Data Type | Operation | Comments |
|---|---|---|---|
| Active | Boolean | Read/Write | Enable notification device. Default value: False |
| DisplayName | String | Read/Write | Name of notification device |
| DeviceName | String | Read Only | Device name of notification device which can’t be changed. |
| FailDeviceObjectId | String | Read/Write | Have to provide notification device object id. To move back to “Do nothing option”, don’t provide any object Id in this parameter. |
| EventList | String | Read/Write | Values can be: All messages: AllMessage All message urgent only: AllUrgentMessage All Voice messages: NewVoiceMail All voice message urgent only: NewUrgentVoiceMai Dispatch messages: DispatchMessage Dispatch message urgent only: UrgentDispatchMessage Fax messages: NewFax Fax messages urgent only: NewUrgentFax All voice messages and fax message urgent only: NewUrgentFax,NewVoiceMail All voice message urgent only and fax message: NewUrgentFax,NewUrgentVoiceMail Fax message and all voice message: NewFax,NewVoiceMail |
| PhoneNumber | Integer | Read/Write | To activate notification device phone number is mandatory. |
| AfterDialDigits | String (32) | Read/Write | The extra digits (if any) that Cisco Unity Connection will dial after the phone number. For numeric pagers, the extra digits
                                                are shown on the pager display. |
| DialDelay | Integer |  | The amount of time (in seconds) Cisco Unity Connection will wait after detecting a successful call before dialing specified
                                             additional digits (if any). Additional digits are contained in AfterDialDigits. |
| InitialDelay | Integer | Read/Write | The amount of time (in minutes) from the time a message is received until the message notification triggers (if the message
                                                matches the criteria). Default Value: 0 Range: 0-120 |
| RingsToWait | Integer | Read/Write | The number of rings Cisco Unity Connection will wait before hanging up if the device does not answer. Default value: 4 Range: 1-100 |
| RetriesOnBusy | Integer | Read/Write | The number of times Cisco Unity Connection will retry the notification device if it is busy. Default value: 4 Range: 0-100 |
| BusyRetryInterval | Integer | Read/Write | The amount of time (in minutes) Cisco Unity Connection will wait between tries if the device is busy. Default value: 5 Range: 1-100 |
| RetriesOnRna | Integer | Read/Write | The number of times Cisco Unity Connection will retry the notification device if the device does not answer. Default value: 4 Range: 0-100 |
| RnaRetryInterval | Integer | Read/Write | The amount of time (in minutes) Cisco Unity Connection will wait between tries if the device does not answer. Default value: 15 Range: 1-100 |
| RetriesOnSuccess | Integer | Read/Write | The number of times Cisco Unity Connection will retry the notification device if it is successful. Default value: 0 Range: 0-100 |
| SuccessRetryInterval | Integer | Read/Write | The amount of time (in minutes) Cisco Unity Connection will wait between tries if the device is successful. Default value: 1 Range: 1-100 |
| MediaSwitchObjectid | String | Read/Write | The unique identifier of the MediaSwitch objects to use for notification. |

| GET https://<connection-
    server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplatenotificationdevices/usertemplatephonedevic
    es/<usertemplatenotificationdeviceobjectId> |
|---|

| GET https://<connection-
    server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplatenotificationdevices/usertemplatehtmldevic
    es/<usertemplatenotificationdeviceobjectId>
Request Body: To update an HTML Device
<UserTemplateHtmlDevice>
    <Active>truee</Active>   
    <SmtpAddress>tenant@cisco.com</SmtpAddress>
    <DisableMobileNumberFromPCA>false</DisableMobileNumberFromPCA>
    <HeaderText>erwr</HeaderText>
</UserTemplateHtmlDevice> |
|---|

| Response Code: 204 |
|---|

| Note | To activate the SmtpAddress parameter is mandatory. |
|---|---|

| Parameter | Data Type | Operation | Comment |
|---|---|---|---|
| DeviceName | String | Read/Write | Device name of HTML notification device. |
| EventList | String | Read/Write | By default it is NewVoiceMail. |
| SmtpAddress | String | Read/Write | SMTP address to be notified. |
| NotificationTemplateID | String | Read/Write | HTML notification templates. |
| DisableMobileNumberFromPCA | Boolean | Read/Write | Disable Outdial Number From Cisco PCA. Default value: False |
| CallbackNumber | Integer | Read/Write | Outdial number. |
| DisableTemplateSelectionFromPCA | Boolean | Read/Write | Disable HTML Template selection From Cisco PCA. Default value: False |

| GET https://<connection server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplatenotificationdevices/usertemplatesmtpdevices/<usertemplatenotificationdeviceobjectId>
Request Body: SMTP Devices
<UserTemplateSmtpDevice>
<StaticText>ritu</StaticText>
<Active>true</Active>
<DeviceName>SMTP</DeviceName>
 <SendCallerId>false</SendCallerId>
<SendPcaLink>true</SendPcaLink>
<Undeletable>true</Undeletable>
<HeaderText>erwr</HeaderText>
<FooterText>efs</FooterText>
<EventList>AllMessage, CalendarAppointment,CalendarMeeting</EventList>
</UserTemplateSmtpDevice> |
|---|

| Response Code: 204 |
|---|

| Parameter | Data Type | Operation | Comment |
|---|---|---|---|
| Active | Boolean | Read/Write | Enable SMTP notification device. SMTP address is mandatory to enable it. Default value: False |
| SmtpAddress | String | Read/Write | SMTP address to be notified. |
| InitialDelay | Integer | Read/Write | Delay before the First Notification Attempt |
| RepeatNotify | Boolean | Read/Write | Repeat Notification if there are Still New Messages. Default value: False |
| RepeatInterval | Integer | Read/Write | Notification Repeat Interval |
| EventList | String | Read/Write | Values can be: All messages: AllMessage All message urgent only: AllUrgentMessage All Voice messages: NewVoiceMail All voice message urgent only: NewUrgentVoiceMai Dispatch messages: DispatchMessage Dispatch message urgent only: UrgentDispatchMessage Fax messages: NewFax Fax messages urgent only: NewUrgentFax All voice messages and fax message urgent only: NewUrgentFax,NewVoiceMail All voice message urgent only and fax message: NewUrgentFax,NewUrgentVoiceMail Fax message and all voice message: NewFax,NewVoiceMail Calendar Appointment: CalendarAppointment Calendar meeting: CalendarMeeting |
| PhoneNumbe | Integer | Read/Write | From which number SMTP notification is sent. |
| HeaderText | String | Read/Write | Message Header |
| StaticText | String | Read/Write | Message text |
| FooterText | String | Read/Write | Message footer |
| SendCallerId | Boolean | Read/Write | Include Message Information in Message Text. Default value: True |
| SendCount | Boolean | Read/Write | Include Message Count in Message Text. Default value: True |
| SendPcaLink | Boolean | Read/Write | Include a Link to the Cisco Unity Connection Web Inbox in Message Text. Default value: False |

| POST https://<connection-
    server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplatenotificationdevic
    es/usertemplatepagerdevices
Request Body:
<UserTemplateNotificationDevice>
    <DisplayName>Newpager</DisplayName>
    <MediaSwitchObjectId>8adf6869-4afc-4455-9fd5-d05b68ca6630</MediaSwitchObjectId>
</UserTemplateNotificationDevice> |
|---|

| Response Code: 201 |
|---|

| /vmrest/usertemplates/<objectid>/usertemplatenotificationdevices/<objectid> |
|---|

| GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid> |
|---|

| Request Body:
<UserTemplate>
    <PromptVolume>50</PromptVolume>
    <PromptSpeed>100</PromptSpeed>
    <IsClockMode24Hour>false</IsClockMode24Hour>
    <ConversationTui>SubMenu</ConversationTui>
    <MessageLocatorSortOrder>1</MessageLocatorSortOrder>
    <JumpToMessagesOnLogin>false</JumpToMessagesOnLogin>
</UserTemplate> |
|---|

| Response Code: 204 |
|---|

| <User>
  <ExitAction>1</ExitAction>
</User> |
|---|

| Response Code: 204 |
|---|

| <User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>PHTransfer</ExitTargetConversation>
  <ExitTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</ExitTargetHandlerObjectId>
</User> |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers |
|---|

| Response Code: 204 |
|---|

| <User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>PHInterview</ExitTargetConversation>
  <ExitTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</ExitTargetHandlerObjectId>
</User> |
|---|

| GET https://<connection-server>/vmrest/handlers/interviewhandlers |
|---|

| Response Code: 204 |
|---|

| GET https://<connection-server>/vmrest/handlers/directoryhandlers |
|---|

| <User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>AD</ExitTargetConversation>
  <ExitTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</ExitTargetHandlerObjectId> 
</User> |
|---|

| Response Code: 204 |
|---|

| <User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>BroadcastMessageAdministrator</ExitTargetConversation>
</UserTemplate> |
|---|

| Response Code: 204 |
|---|

| <User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>SystemTransfer</ExitTargetConversation>
</User> |
|---|

| Response Code: 204 |
|---|

| <User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>GreetingAdministrator</ExitTargetConversation>
</User> |
|---|

| Response Code: 204 |
|---|

| <UserTemplate>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>SubSignIn</ExitTargetConversation>
</UserTemplate> |
|---|

| Response Code: 204 |
|---|

| <User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>SubSysTransfer</ExitTargetConversation>
</User> |
|---|

| Response Code: 204 |
|---|

| <User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>PHTransfer</ExitTargetConversation> 
  <ExitTargetHandlerObjectId>71cb381b-fd16-4ba8-8a1d-e71684e57b0e</ExitTargetHandlerObjectId>
</User> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/users/<userobjectid>
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| {
  "ExitAction":"2",
  "ExitTargetConversation":"SubSysTransfer"
} |
|---|

| Response Code: 204 |
|---|

| Parameters | Values |
|---|---|
| useBriefPrompts | *True: Brief False: Full |
| PromptVolume | *25: Low 50: Medium 100: High |
| PromptSpeed | *50: Slow 100: Normal 150: Fast 200: Fastest |
| IsClockMode24Hour | *True: 24-Hour Clock (00:00 - 23:59) False: 12-Hour Clock (12:00 AM - 11:59 PM) |
| ConversationTUI | *SubMenu: Classic Conversation SubMenu_Alternate_Custom: Custom keypad mapping1 SubMenu_Alternate_Custom1: Custom keypad mapping1 SubMenu_AlternateN: Alternate Keypad Mapping(N) SubMenu_AlternateS: Alternate Keypad Mapping(S) SubMenu_AlternateX: Alternate Keypad Mapping (X) SubMenuOpt1: Optional conversation1 SubMenu_AlternateI: Standard Conversation |
| MessageLocatorSortOrde | *1: Last In, First Out 2: First In, First Out |

| Note | PromptVolume and PromptSpeed parameters must be of the same range
                                             			 given in the table. |
|---|---|

| GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid> |
|---|

| Request Body:
<UserTemplate>
    <Volume>50</Volume>
    <Speed>100</Speed>
    <SayTotalNew>true</SayTotalNew>
    <SayTotalNewVoice>true</SayTotalNewVoice>
    <SayTotalNewEmail>false</SayTotalNewEmail>
    <SayTotalNewFax>false</SayTotalNewFax>
    <SayTotalReceipts>false</SayTotalReceipts>
    <SayTotalSaved>true</SayTotalSaved>
    <SayTotalDraftMsg>false</SayTotalDraftMsg>
    <MessageTypeMenu>false</MessageTypeMenu>
    <NewMessageSortOrder>2</NewMessageSortOrder>
    <SaveMessageOnHangup>1</SaveMessageOnHangup>
    <DeletedMessageSortOrder>1</DeletedMessageSortOrder>
    <SaySender>true</SaySender>
    <SaySenderExtension>false</SaySenderExtension> 
    <SayAni>true</SayAni>
    <SayMsgNumber>true</SayMsgNumber>
    <SayTimestampBefore>true</SayTimestampBefore>
    <AutoAdvanceMsgs>false</AutoAdvanceMsgs>
    <ConfirmDeleteMessage>true</ConfirmDeleteMessage>
</UserTemplate> |
|---|

| Response Code: 204 |
|---|

| Note | To sort the message type: for new message:
                                                      				  <NewMessageSortOrder>2</NewMessageSortOrder> for saved message:
                                                      				  <SaveMessageSortOrder>1</SaveMessageSortOrder> for deleted message:
                                                      				  <DeletedMessageSortOrder>1</DeletedMessageSortOrder> |
|---|---|

| Parameter | Data Type | Operation | Description |
|---|---|---|---|
| Volume | Integer | Read/Write | The audio volume expressed as a percentage that Cisco Unity Connection uses to play back message. The range can vary from
                                             0 to 100. Possible values: 25: Low 50: Medium 100: High Default value: 50 |
| Speed | Integer | Read/Write | The audio speed system uses to play back messages to the subscriber. The range can vary from 0 to 200. 50: Slow 100: Normal 150: Fast 200: Fastest Default value: 100 |
| SaveMessageOnHangup | Boolean | Read/Write | A flag indicating when hanging up while listening to a new message, whether the message is marked new again or is marked read. Possible Values: false: New true: Saved Default Value: false |
| NewMessageSortOrder | Integer | Read/Write | The order in which Cisco Unity Connection will sort new messages. Possible values: 1: Newest First 2: Oldest First Default Value: 1 |
| SavedMessageSortOrder | Integer | Read/Write | The order in which Cisco Unity Connection will sort saved messages.. Possible values: 1: Newest First 2: Oldest First Default Value: 2 |
| DeletedMessageSortOrder | Integer | Read/Write | The order in which Cisco Unity Connection presents deleted messages to the subscriber. Possible values: 1: Newest First 2: Oldest First Default Value: 2 |

| Note | Volume and Speed parameters must be of the same range given in
                                                			 the table. |
|---|---|

| GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid> |
|---|

| GET https://<connection-server>/vmrestvmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId> |
|---|

| Request Body:
<CallhandlerPrimaryTemplate>
    <PlayPostGreetingRecording>1</PlayPostGreetingRecording>
</CallhandlerPrimaryTemplate> |
|---|

| Response Code: 204 |
|---|

| Request URI:
PUT https://<connection-server>/vmrest/callhandlerprimarytemplates/<ObjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive
Request Body:
{
    "PlayPostGreetingRecording":"1"
} |
|---|

| Response Code: 204 |
|---|

| Parameters | Values |
|---|---|
| PlayPostGreetingRecording | 0: Do Not Play Recording 1: Play Recording to All Callers 2: Play Recording Only to Unidentified Callers |
| PostGreetingRecordingObjectId | Object Id of post greeting. |

| GET https://<connection-server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId> |
|---|

| vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/transferoptions |
|---|

| GET https://<connection-server>/vmrestvmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/transferoptions/Alternate |
|---|

| GET https://<connection-server>/vmrestvmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/transferoptions/Off%20Hours |
|---|

| GET https://<connection-server>/vmrestvmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/transferoptions/Standard |
|---|

| GET https://<connection-server>/vmrestvmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/transferoptions/Alternate |
|---|

| <TransferOption>
<URI>/vmrest/callhandlerprimarytemplates/45e0a6f4-43c4-472a-8ffb-f6124aa549d0/transferoptions/Alternate</URI>
<CallHandlerObjectId>45e0a6f4-43c4-472a-8ffb-f6124aa549d0</CallHandlerObjectId>
<CallhandlerURI>/vmrest/callhandlerprimarytemplates/45e0a6f4-43c4-472a-8ffb-f6124aa549d0</CallhandlerURI>
<TransferOptionType>Alternate</TransferOptionType>
<Action>1</Action>
<RnaAction>1</RnaAction>
<TimeExpires>1972-01-01 00:00:00.0</TimeExpires>
<TransferAnnounce>false</TransferAnnounce>
<TransferConfirm>false</TransferConfirm>
<TransferDtDetect>false</TransferDtDetect>
<TransferHoldingMode>0</TransferHoldingMode>
<TransferIntroduce>false</TransferIntroduce>
<TransferRings>4</TransferRings>
<TransferScreening>false</TransferScreening>
<TransferType>0</TransferType>
<MediaSwitchObjectId>221ee752-5147-4326-9990-d4a138674f9e</MediaSwitchObjectId>
<PhoneSystemURI>/vmrest/phonesystems/221ee752-5147-4326-9990-d4a138674f9e</PhoneSystemURI>
<UsePrimaryExtension>true</UsePrimaryExtension>
<PlayTransferPrompt>true</PlayTransferPrompt>
<PersonalCallTransfer>false</PersonalCallTransfer>
<Enabled>false</Enabled>
</TransferOption> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/callhandlerprimarytemplates/<callhandlerprimarytemplatesobjectid>/transferoptions
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| {
"@total":"3"
"TransferOption":[
{
"URI":"/vmrest/callhandlerprimarytemplates/02dcae3e-2e7c-4997-a36e-0f5276281078/transferoptions/Alternate"
"CallHandlerObjectId":"02dcae3e-2e7c-4997-a36e-0f5276281078"
"CallhandlerURI":"/vmrest/callhandlerprimarytemplates/02dcae3e-2e7c-4997-a36e-0f5276281078"
"TransferOptionType":"Alternate"
"Action":"1"
"RnaAction":"1"
"TransferAnnounce":"false"
"TransferConfirm":"false"
"TransferDtDetect":"false"
"TransferHoldingMode":"0"
"TransferIntroduce":"false"
"TransferRings":"4"
"TransferScreening":"false"
"TransferType":"0"
"MediaSwitchObjectId":"7c654c70-e76c-4e47-b8f6-fa92cec6755e"
"PhoneSystemURI":"/vmrest/phonesystems/7c654c70-e76c-4e47-b8f6-fa92cec6755e"
"UsePrimaryExtension":"true"
"PlayTransferPrompt":"true"
"PersonalCallTransfer":"false"
"Enabled":"true"
}
{
"URI":"/vmrest/callhandlerprimarytemplates/02dcae3e-2e7c-4997-a36e-0f5276281078/transferoptions/Off%20Hours"
"CallHandlerObjectId":"02dcae3e-2e7c-4997-a36e-0f5276281078"
"CallhandlerURI":"/vmrest/callhandlerprimarytemplates/02dcae3e-2e7c-4997-a36e-0f5276281078"
"TransferOptionType":"Off Hours"
"Action":"1"
"RnaAction":"1"
"TransferAnnounce":"false"
"TransferConfirm":"false"
"TransferDtDetect":"false"
"TransferHoldingMode":"0"
"TransferIntroduce":"false"
"TransferRings":"4"
"TransferScreening":"false"
"TransferType":"0"
"MediaSwitchObjectId":"7c654c70-e76c-4e47-b8f6-fa92cec6755e"
"PhoneSystemURI":"/vmrest/phonesystems/7c654c70-e76c-4e47-b8f6-fa92cec6755e"
"UsePrimaryExtension":"true"
"PlayTransferPrompt":"true"
"PersonalCallTransfer":"false"
"Enabled":"true"
}
{
"URI":"/vmrest/callhandlerprimarytemplates/02dcae3e-2e7c-4997-a36e-0f5276281078/transferoptions/Standard"
"CallHandlerObjectId":"02dcae3e-2e7c-4997-a36e-0f5276281078"
"CallhandlerURI":"/vmrest/callhandlerprimarytemplates/02dcae3e-2e7c-4997-a36e-0f5276281078"
"TransferOptionType":"Standard"
"Action":"1"
"RnaAction":"1"
"TransferAnnounce":"false"
"TransferConfirm":"false"
"TransferDtDetect":"false"
"TransferHoldingMode":"0"
"TransferIntroduce":"false"
"TransferRings":"4"
"TransferScreening":"false"
"TransferType":"0"
"MediaSwitchObjectId":"7c654c70-e76c-4e47-b8f6-fa92cec6755e"
"PhoneSystemURI":"/vmrest/phonesystems/7c654c70-e76c-4e47-b8f6-fa92cec6755e"
"UsePrimaryExtension":"true"
"PlayTransferPrompt":"true"
"PersonalCallTransfer":"false"
"Enabled":"true"
}
]
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrestvmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/transferoptions/Alternate |
|---|

| <TransferOption>
<Action>0</Action>
<TimeExpires>1972-01-01 00:00:00.0</TimeExpires>
<TransferAnnounce>false</TransferAnnounce>
<TransferConfirm>false</TransferConfirm>
<TransferHoldingMode>0</TransferHoldingMode>
<TransferIntroduce>false</TransferIntroduce>
<TransferRings>4</TransferRings>
<TransferScreening>false</TransferScreening>
<TransferType>0</TransferType>
</TransferOption> |
|---|

| Response Code: 204 |
|---|

| Request URI:
PUT https://<connection-server>/vmrest/callhandlerprimarytemplates/<CallhandlerprimarytemplatesObjectId>/transferoptions/Alternate
Accept: application/json
Content-type: application/json
Connection: keep-alive
Request Body:
{
"Action":"1",
"TransferAnnounce":"false",
"TransferConfirm":"false",
"TransferHoldingMode":"0",
"TransferIntroduce":"false",
"TransferRings":"4",
"TransferScreening":"false",
"TransferType":"0"
} |
|---|

| Response Code: 204 |
|---|

| <TransferOption>
<Enabled>true</Enabled>
<TimeExpires></TimeExpires>
</TransferOption> |
|---|

| Note | Same way closed transfer rule can be edited and for standard
                                                			 transfer rule status cannot be updated. |
|---|---|

| Parameter | Data Type | Operations | Comments |
|---|---|---|---|
| TransferOptionType | String(64) | Read Only | The type of transfer option, e.g. "Standard," "Off Hours," or "Alternate." |
| Enabled | Boolean | Read/Write | To enable transfer rules. Possible values: true false Default value: false |
| TimeExpires | DateTime | Read/Write | The date and time when this transfer option expires. If the transfer rule is enabled, the value is NULL or a date in the future.
                                             If the transfer rule is disable, the value is a past date. |
| Actions | Integer | Read/Write | A flag indicating whether Cisco Unity Connection transfers the call to the call handler greeting or attempts to transfer the
                                             call to an extension. Values can be: 0: Greeting 1: Extension |
| TransferType | Integer | Read/Write | The type of call transfer Cisco Unity Connection will perform - supervised or unsupervised (also referred to as "Release to
                                             Switch" transfer). Values: 0: Release to Switch 1: Supervise Transfer |
| TransferRings | Integer | Read/Write | The number of times the extension rings before Cisco Unity Connection considers it a "ring no answer" and plays the subscriber
                                             or handler greeting. Applies only when the "TransferType" column is set to supervised (1). This value should never be less than 2 for a supervised
                                                transfer. Possible Values: 2-20 Default value: 4 |
| PlayTransferPrompt | Boolean | Read/Write | Enables "Wait While I Transfer Your Call" Prompt. Values: false: System will not play the "Wait while I transfer your call" prompt prior to transfer. true: System will play the "Wait while I transfer your call" prompt prior to transfer. Default value: true |
| TransferHoldingMode | Integer | Read/Write | The action Cisco Unity Connection will take when the extension is busy. Applies only when the "TransferType" column is set to supervised (1). Values: 0: Send callers to voicemail. 1: Put callers on hold without asking. 2: Ask callers to hold. |
| TransferAnnounce | Boolean | Read/Write | A flag indicating whether Cisco Unity Connection plays "transferring call" when the subscriber answers the phone. Requires a "TransferType" of supervised (1). Values: false: Do not say "Transferring call" when the subscriber answers the phone true: Say "Transferring call" when the subscriber answers the phone Default value: false |
| TransferIntroduce | Boolean | Read/Write | A flag indicating whether Cisco Unity Connection will say "call for <recorded name of the call handler>" when the subscriber
                                             answers the phone. Requires a "TransferType" of supervised (1). This functionality is normally used when a single extension number is being shared
                                                by multiple subscribers or a scenario where the subscriber who is the message recipient takes calls for more than one dialed
                                                extension. The introduction alerts the subscriber who answers that the call is for the call handler. Default value: false |
| TransferConfirm | Boolean | Read/Write | A flag indicating whether Cisco Unity Connection prompts the subscriber to accept or refuse a call ("Press 1 to take the call
                                             or 2 and I'll take a message"). If the call is accepted, it is transferred to the subscriber phone. If the call is refused,
                                             Cisco Unity Connection plays the applicable subscriber greeting. Requires a "TransferType" of supervised (1). Typically this is used in conjunction with the call screening option ("TransferScreening"
                                                column) enabled. This combination enables the subscriber to hear the name of the caller and then decide if they want to take
                                                the call or not. Values: false: Transfer confirm disabled true: Transfer confirm enabled Default value: false |
| TransferScreening | Boolean | Read/Write | Requires a "TransferType" of supervised (1). Normally this column is used along with "TransferConfirm" to allow the subscriber to screen calls. Values: false: Call screening disabled true: Ask and record caller name Default value: false |

| GET https://<connection-server>/vmrest/usertemplates |
|---|

| <UserTemplates total="1">
    <UserTemplate>
    <URI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-2b13f76bf631</URI>
    <ObjectId>c2056af2-bed7-4a0d-9039-2b13f76bf631</ObjectId>
    <TenantObjectId>fe6541fb-b42c-44f2-8404-ded14cbf7438</TenantObjectId>
    <UseDefaultLanguage>true</UseDefaultLanguage>
    <UseDefaultTimeZone>true</UseDefaultTimeZone>
    <Alias>Texoma_User_Template1</Alias>
    <City/>
    <State/>
    <Country>US</Country>
    <PostalCode/>
    <Manager/>
    <Building/>
    <Address/>
    <DisplayName>Texoma_User_Template1</DisplayName>
    <BillingId/>
    <TimeZone>190</TimeZone>
    <CreationTime>2012-12-26 13:04:28.9</CreationTime>
    <CosObjectId>0ef61610-a729-4b0d-9476-cab095028db3</CosObjectId>
    <CosURI>/vmrest/coses/0ef61610-a729-4b0d-9476-cab095028db3</CosURI>
    <Language>1033</Language>
    <LocationObjectId>27a67e01-bcb4-4012-8b1b-f0a08b736087</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/27a67e01-b
    cb4-4012-8b1b-f0a08b736087</LocationURI>
    <AddressMode>0</AddressMode>
    <ClockMode>0</ClockMode>
    <ConversationTui>SubMenu</ConversationTui>
    <GreetByName>true</GreetByName>
    <ListInDirectory>true</ListInDirectory>
    <IsVmEnrolled>true</IsVmEnrolled>
    <SayCopiedNames>true</SayCopiedNames>
    <SayDistributionList>true</SayDistributionList>
    <SayMsgNumber>true</SayMsgNumber>
    <SaySender>true</SaySender>
    <SayTimestampAfter>true</SayTimestampAfter>
    <SayTimestampBefore>false</SayTimestampBefore>
    <SayTotalNew>false</SayTotalNew>
    <SayTotalNewEmail>false</SayTotalNewEmail>
    <SayTotalNewFax>false</SayTotalNewFax>
    <SayTotalNewVoice>true</SayTotalNewVoice>
    <SayTotalReceipts>false</SayTotalReceipts>
    <SayTotalSaved>true</SayTotalSaved>
    <Speed>100</Speed>
    <MediaSwitchObjectId>b6df8cb3-b3ce-4797-84f3-5559049df8e8</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/b6df8cb3-b3ce-4797-84f3-
    5559049df8e8</PhoneSystemURI>
    <Undeletable>false</Undeletable>
    <UseBriefPrompts>false</UseBriefPrompts>
    <Volume>50</Volume>
    <EnAltGreetDontRingPhone>false</EnAltGreetDontRingPhone>
    <EnAltGreetPreventSkip>false</EnAltGreetPreventSkip>
    <EnAltGreetPreventMsg>false</EnAltGreetPreventMsg>
    <EncryptPrivateMessages>false</EncryptPrivateMessages>
    <DeletedMessageSortOrder>2</DeletedMessageSortOrder>
    <SayAltGreetWarning>false</SayAltGreetWarning>
    <SaySenderExtension>false</SaySenderExtension>
    <SayAni>false</SayAni>
    <ExitCallActionObjectId>0463e49b-cde4-4c30-877c-acfe25966a42</ExitCallActionObjectId> 
    <CallAnswerTimeout>4</CallAnswerTimeout>
    <CallHandlerObjectId>83c9b890-6659-4c0f-8be6-8a1a85efee7e</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/callhandlerprimarytemplates/83c9b890-6659-4c0f-8be6-8a1a85efee7e</CallhandlerURI>
    <DisplayNameRule>1</DisplayNameRule>
    <DoesntExpire>false</DoesntExpire>
    <CantChange>false</CantChange>
    <MailboxStoreObjectId>e983490d-78a5-45aa-b9a0-31f51460a5bd</MailboxStoreObjectId>
    <SavedMessageStackOrder>1234567</SavedMessageStackOrder>
    <NewMessageStackOrder>1234567</NewMessageStackOrder>
    <MessageLocatorSortOrder>1</MessageLocatorSortOrder>
    <SavedMessageSortOrder>2</SavedMessageSortOrder>
    <NewMessageSortOrder>1</NewMessageSortOrder>
    <MessageTypeMenu>false</MessageTypeMenu>
    <EnablePersonalRules>true</EnablePersonalRules>
    <RecordUnknownCallerName>true</RecordUnknownCallerName>
    <RingPrimaryPhoneFirst>false</RingPrimaryPhoneFirst>
    <PromptSpeed>100</PromptSpeed>
    <ExitAction>2</ExitAction>
    <ExitTargetConversation>PHGreeting</ExitTargetConversation>
    <ExitTargetHandlerObjectId>063956f9-c5ca-4e8b-be67-
    ff945a8a5d99</ExitTargetHandlerObjectId>
    <RepeatMenu>1</RepeatMenu>
    <FirstDigitTimeout>5000</FirstDigitTimeout>
    <InterdigitDelay>3000</InterdigitDelay>
    <PromptVolume>50</PromptVolume>
    <DelayAfterGreeting>0</DelayAfterGreeting>
    <AddressAfterRecord>false</AddressAfterRecord>
    <ConfirmDeleteMessage>false</ConfirmDeleteMessage>
    <ConfirmDeleteDeletedMessage>false</ConfirmDeleteDeletedMessage>
    <ConfirmDeleteMultipleMessages>true</ConfirmDeleteMultipleMessages>
    <IsClockMode24Hour>false</IsClockMode24Hour>
    <RouteNDRToSender>true</RouteNDRToSender>
    <NotificationType>0</NotificationType>
    <SendReadReceipts>1</SendReadReceipts>
    <ReceiveQuota>-2</ReceiveQuota>
    <SendQuota>-2</SendQuota>
    <WarningQuota>-2</WarningQuota>
    <IsSetForVmEnrollment>true</IsSetForVmEnrollment>
    <VoiceNameRequired>false</VoiceNameRequired>
    <SendBroadcastMsg>false</SendBroadcastMsg>
    <UpdateBroadcastMsg>false</UpdateBroadcastMsg>
    <ConversationVui>VuiStart</ConversationVui>
    <SpeechCompleteTimeout>0</SpeechCompleteTimeout>
    <SpeechIncompleteTimeout>750</SpeechIncompleteTimeout>
    <UseVui>false</UseVui>
    <SkipPasswordForKnownDevice>false</SkipPasswordForKnownDevice>
    <JumpToMessagesOnLogin>true</JumpToMessagesOnLogin>
    <EnableMessageLocator>false</EnableMessageLocator>
    <MessageAgingPolicyObjectId>6780a194-6efd-4311-819f-
    494a082bb093</MessageAgingPolicyObjectId>
    <MessageAgingPolicyURI>/vmrest/messageagingpolicies/6780a194-6efd-4311-819f-
    494a082bb093</MessageAgingPolicyURI>
    <AssistantRowsPerPage>5</AssistantRowsPerPage>
    <InboxMessagesPerPage>20</InboxMessagesPerPage>
    <InboxAutoRefresh>15</InboxAutoRefresh>
    <InboxAutoResolveMessageRecipients>true</InboxAutoResolveMessageRecipients>
    <PcaAddressBookRowsPerPage>5</PcaAddressBookRowsPerPage>
    <ReadOnly>false</ReadOnly>
    <EnableTts>true</EnableTts>
    <ConfirmationConfidenceThreshold>60</ConfirmationConfidenceThreshold>
    <AnnounceUpcomingMeetings>60</AnnounceUpcomingMeetings>
    <SpeechConfidenceThreshold>40</SpeechConfidenceThreshold>
    <SpeechSpeedVsAccuracy>50</SpeechSpeedVsAccuracy>
    <SpeechSensitivity>50</SpeechSensitivity>
    <EnableVisualMessageLocator>false</EnableVisualMessageLocator>
    <ContinuousAddMode>false</ContinuousAddMode>
    <NameConfirmation>false</NameConfirmation>
    <CommandDigitTimeout>1500</CommandDigitTimeout>
    <SaveMessageOnHangup>false</SaveMessageOnHangup>
    <SendMessageOnHangup>1</SendMessageOnHangup>
    <SkipForwardTime>5000</SkipForwardTime>
    <SkipReverseTime>5000</SkipReverseTime>
    <UseShortPollForCache>false</UseShortPollForCache>
    <SearchByExtensionSearchSpaceObjectId>2e0da21b-54e4-4b51-9f09-
    960049a5e806</SearchByExtensionSearchSpaceObjectId>
    <SearchByExtensionSearchSpaceURI>/vmrest/searchspaces/2e0da21b-54e4-4b51-9f09-
    960049a5e806</SearchByExtensionSearchSpaceURI>
    <SearchByNameSearchSpaceObjectId>2e0da21b-54e4-4b51-9f09-960049a5e806</SearchByNameSearchSpaceObjectId>
    <SearchByNameSearchSpaceURI>/vmrest/searchspaces/2e0da21b-54e4-4b51-9f09-960049a5e806</SearchByNameSearchSpaceURI>
    <PartitionObjectId>c6ff147e-c32c-4ade-8f12-46427c795c21</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/c6ff147e-c32c-4ade-8f12-46427c795c21</PartitionURI>
    <UseDynamicNameSearchWeight>false</UseDynamicNameSearchWeight>
    <LdapType>0</LdapType>
    <EnableMessageBookmark>false</EnableMessageBookmark>
    <SayTotalDraftMsg>false</SayTotalDraftMsg>
    <EnableSaveDraft>false</EnableSaveDraft>
    <RetainUrgentMessageFlag>false</RetainUrgentMessageFlag>
    <SayMessageLength>false</SayMessageLength>
    <CreateSmtpProxyFromCorp>false</CreateSmtpProxyFromCorp>
    <AutoAdvanceMsgs>false</AutoAdvanceMsgs>
    <SaySenderAfter>false</SaySenderAfter>
    <SaySenderExtensionAfter>false</SaySenderExtensionAfter>
    <SayMsgNumberAfter>false</SayMsgNumberAfter>
    <SayAniAfter>false</SayAniAfter>
    <SayMessageLengthAfter>false</SayMessageLengthAfter>
    <UserTemplateRolesURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-
    2b13f76bf631/usertemplateroles</UserTemplateRolesURI>
    <UserTemplateNotificationDevicesURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-2b13f76bf631/usertemplatenotificationdevices</UserTemplateNotificationDevicesURI>
    <TemplateExternalServiceAccountsURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-2b13f76bf631/templateexternalserviceaccounts</TemplateExternalServiceAccountsURI>
    <UserTemplateWebPasswordURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-90392b13f76bf631/credential/password</UserTemplateWebPasswordURI>
    <UserTemplateVoicePinURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-
    2b13f76bf631/credential/pin</UserTemplateVoicePinURI>
    <UserTemplateMessageActionURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-
    2b13f76bf631/usertemplatemessageactions</UserTemplateMessageActionURI>
</UserTemplate>
</UserTemplates> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/usertemplates
Accept: application/json
Content_type: application/json
Connection: keep_alive |
|---|

| {
  "@total":"1"
  "UserTemplate":\[
  {
    "URI":"/vmrest/usertemplates/6164ac2d-e8ec-441a-93a0-95f8e18a655c"
    "ObjectId":"6164ac2d-e8ec-441a-93a0-95f8e18a655c"
    "TenantObjectId": "fe6541fb-b42c-44f2-8404-ded14cbf7438"
    "UseDefaultLanguage":"true"
    "UseDefaultTimeZone":"true"
    "Alias":"voicemailusertemplate"
    "DisplayName":"Voice Mail User Template"
    "TimeZone":"190"
    "CreationTime":"2013-02-25T09:39:25Z"
    "CosObjectId":"0b59d616-6434-443a-95aa-00b9d7315d54"
    "CosURI":"/vmrest/coses/0b59d616-6434-443a-95aa-00b9d7315d54"
    "Language":"1033"
    "LocationObjectId":"cff1347e-87af-4409-bead-d1970625f82e"
    "LocationURI":"/vmrest/locations/connectionlocations/cff1347e-87af-4409-bead-d1970625f82e"
    "AddressMode":"0"
    "ClockMode":"0"
    "ConversationTui":"SubMenu"
    "GreetByName":"true"
    "ListInDirectory":"true"
    "IsVmEnrolled":"true"
    "SayCopiedNames":"true"
    "SayDistributionList":"true"
    "SayMsgNumber":"true"
    "SaySender":"true"
    "SayTimestampAfter":"true"
    "SayTimestampBefore":"false"
    "SayTotalNew":"false"
    "SayTotalNewEmail":"false"
    "SayTotalNewFax":"false"
    "SayTotalNewVoice":"true"
    "SayTotalReceipts":"false"
    "SayTotalSaved":"true"
    "Speed":"100"
    "MediaSwitchObjectId":"0ad0b88c-4a70-4cf7-913e-d5d7a921caca"
    "PhoneSystemURI":"/vmrest/phonesystems/0ad0b88c-4a70-4cf7-913e-d5d7a921caca"
    "Undeletable":"true"
    "UseBriefPrompts":"false"
    "Volume":"50"
    "EnAltGreetDontRingPhone":"false"
    "EnAltGreetPreventSkip":"false"
    "EnAltGreetPreventMsg":"false"
    "EncryptPrivateMessages":"false"
    "DeletedMessageSortOrder":"2"
    "SayAltGreetWarning":"false"
    "SaySenderExtension":"false"
    "SayAni":"false"
    "ExitCallActionObjectId":"38f2eab0-a78c-49a2-8aee-ff562844d5db"
    "CallAnswerTimeout":"4"
    "CallHandlerObjectId":"6bcd837d-f1cf-43c2-b199-85b457858a16"
    "CallhandlerURI":"/vmrest/callhandlerprimarytemplates/6bcd837d-f1cf-43c2-b199-
    85b457858a16"
    "DisplayNameRule":"1"
    "DoesntExpire":"false"
    "CantChange":"false"
    "MailboxStoreObjectId":"02089c75-e8a2-4724-a570-9bed7768e716"
    "SavedMessageStackOrder":"1234567"
    "NewMessageStackOrder":"1234567"
    "MessageLocatorSortOrder":"1"
    "SavedMessageSortOrder":"2"
    "NewMessageSortOrder":"1"
    "MessageTypeMenu":"false"
    "EnablePersonalRules":"true"
    "RecordUnknownCallerName":"true"
    "RingPrimaryPhoneFirst":"false"
    "PromptSpeed":"100"
    "ExitAction":"2"
    "ExitTargetConversation":"PHGreeting"
    "ExitTargetHandlerObjectId":"1e0bc010-d9aa-4e1a-b001-a1b40f028d4f"
    "RepeatMenu":"1"
    "FirstDigitTimeout":"5000"
    "InterdigitDelay":"3000"
    "PromptVolume":"50"
    "DelayAfterGreeting":"0"
    "AddressAfterRecord":"false"
    "ConfirmDeleteMessage":"false"
    "ConfirmDeleteDeletedMessage":"false"
    "ConfirmDeleteMultipleMessages":"true"
    "IsClockMode24Hour":"false"
    "RouteNDRToSender":"true"
    "NotificationType":"0"
    "SendReadReceipts":"1"
    "ReceiveQuota":"-2"
    "SendQuota":"-2"
    "WarningQuota":"-2"
    "IsSetForVmEnrollment":"true"
    "VoiceNameRequired":"false"
    "SendBroadcastMsg":"false"
    "UpdateBroadcastMsg":"false"
    "ConversationVui":"VuiStart"
    "SpeechCompleteTimeout":"0"
    "SpeechIncompleteTimeout":"750"
    "UseVui":"false"
    "SkipPasswordForKnownDevice":"false"
    "JumpToMessagesOnLogin":"true"
    "EnableMessageLocator":"false"
    "MessageAgingPolicyObjectId":"adac77f4-8a77-430d-8836-
    0fc9aef3fef5"
    "MessageAgingPolicyURI":"/vmrest/messageagingpolicies/adac77f4-8a77-430d-8836-0fc9aef3fef5"
    "AssistantRowsPerPage":"5"
    "InboxMessagesPerPage":"20"
    "InboxAutoRefresh":"15"
    "InboxAutoResolveMessageRecipients":"true"
    "PcaAddressBookRowsPerPage":"5"
    "ReadOnly":"false"
    "EnableTts":"true"
    "ConfirmationConfidenceThreshold":"60"
    "AnnounceUpcomingMeetings":"60"
    "SpeechConfidenceThreshold":"40"
    "SpeechSpeedVsAccuracy":"50"
    "SpeechSensitivity":"50"
    "EnableVisualMessageLocator":"false"
    "ContinuousAddMode":"false"
    "NameConfirmation":"false"
    "CommandDigitTimeout":"1500"
    "SaveMessageOnHangup":"false"
    "SendMessageOnHangup":"1"
    "SkipForwardTime":"5000"
    "SkipReverseTime":"5000"
    "UseShortPollForCache":"false"
    "SearchByExtensionSearchSpaceObjectId":"2e836e16-f715-4a18-bb7c-
    ee5e33281706"
    "SearchByExtensionSearchSpaceURI":"/vmrest/searchspaces/2e836e16-f715-4a18-bb7c-
    ee5e33281706"
    "SearchByNameSearchSpaceObjectId":"2e836e16-f715-4a18-bb7c-ee5e33281706"
    "SearchByNameSearchSpaceURI":"/vmrest/searchspaces/2e836e16-f715-4a18-bb7c-
    ee5e33281706"
    "PartitionObjectId":"97bf6afe-346e-4275-967e-43c50be79d32"
    "PartitionURI":"/vmrest/partitions/97bf6afe-346e-4275-967e-43c50be79d32"
    "UseDynamicNameSearchWeight":"false"
    "LdapType":"0"
    "EnableMessageBookmark":"false"
    "SayTotalDraftMsg":"false"
    "EnableSaveDraft":"false"
    "RetainUrgentMessageFlag":"false"
    "SayMessageLength":"false"
    "CreateSmtpProxyFromCorp":"false"
    "AutoAdvanceMsgs":"false"
    "SaySenderAfter":"false"
    "SaySenderExtensionAfter":"false"
    "SayMsgNumberAfter":"false"
    "SayAniAfter":"false"
    "SayMessageLengthAfter":"false"
    "UserTemplateRolesURI":"/vmrest/usertemplates/6164ac2d-e8ec-441a-93a0-
    95f8e18a655c/usertemplateroles"
    "UserTemplateNotificationDevicesURI":"/vmrest/usertemplates/6164ac2d-e8ec-441a-93a0-
    95f8e18a655c/usertemplatenotificationdevices"
    "TemplateExternalServiceAccountsURI":"/vmrest/usertemplates/6164ac2d-e8ec-441a-93a0-
    95f8e18a655c/templateexternalserviceaccounts"
    "UserTemplateWebPasswordURI":"/vmrest/usertemplates/6164ac2d-e8ec-441a-93a0-
    95f8e18a655c/credential/password"
    "UserTemplateVoicePinURI":"/vmrest/usertemplates/6164ac2d-e8ec-441a-93a0-
    95f8e18a655c/credential/pin"
    "UserTemplateMessageActionURI":"/vmrest/usertemplates/6164ac2d-e8ec-441a-93a0-
    95f8e18a655c/usertemplatemessageactions"
}
\]
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/usertemplates?query=(TenantObjectId is <Tenant-ObjectId>) |
|---|

| GET https://<connection-server>/vmrest/tenants |
|---|

| GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectId> |
|---|

| <UserTemplate>
    <URI> /vmrest/usertemplates/c8af2544-2bc9-44fa-b713-e80f306cf781 </URI>
    <ObjectId>c8af2544-2bc9-44fa-b713-e80f306cf781</ObjectId>
    <UseDefaultLanguage>true</UseDefaultLanguage>
    <UseDefaultTimeZone>true</UseDefaultTimeZone>
    <Alias>NewCiscoTemplate2</Alias>
    <City/>
    <State/>
    <Country>US</Country>
    <PostalCode/>
    <Department/>
    <Manager/>
    <Building/>
    <Address/>
    <DisplayName>testmonica</DisplayName>
    <BillingId/>
    <TimeZone>190</TimeZone>
    <CreationTime>2012-06-26 05:02:22.05</CreationTime>
    <CosObjectId>7be9b3f3-1200-403f-984a-04c07b7c5a7b</CosObjectId>
    <CosURI>/vmrest/coses/7be9b3f3-1200-403f-984a-04c07b7c5a7b</CosURI>
    <Language>1033</Language>
    <LocationObjectId>6d4ff2e5-3f26-4a19-b2fa-beca79b4c5e9 </LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/6d4ff2e5-3f26-4a19-b2fa-
    beca79b4c5e9</LocationURI>
    <AddressMode>0</AddressMode>
    <ClockMode>0</ClockMode>
    <ConversationTui>SubMenu</ConversationTui>
    <GreetByName>true</GreetByName>
    <ListInDirectory>true</ListInDirectory>
    <IsVmEnrolled>true</IsVmEnrolled>
    <SayCopiedNames>true</SayCopiedNames>
    <SayDistributionList>true</SayDistributionList>
    <SayMsgNumber>true</SayMsgNumber>
    <SaySender>true</SaySender>
    <SayTimestampAfter>true</SayTimestampAfter>
    <SayTimestampBefore>false</SayTimestampBefore>
    <SayTotalNew>false</SayTotalNew>
    <SayTotalNewEmail>false</SayTotalNewEmail>
    <SayTotalNewFax>false</SayTotalNewFax>
    <SayTotalNewVoice>true</SayTotalNewVoice>
    <SayTotalReceipts>false</SayTotalReceipts>
    <SayTotalSaved>true</SayTotalSaved>
    <Speed>100</Speed>
    <MediaSwitchObjectId>1fb12b1c-cf14-4634-b73d-9b9c58ecdf68</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/1fb12b1c-cf14-4634-b73d-
    9b9c58ecdf68</PhoneSystemURI>
    <Undeletable>false</Undeletable>
    <UseBriefPrompts>false</UseBriefPrompts>
    <Volume>50</Volume>
    <EnAltGreetDontRingPhone>false</EnAltGreetDontRingPhone>
    <EnAltGreetPreventSkip>false</EnAltGreetPreventSkip>
    <EnAltGreetPreventMsg>false</EnAltGreetPreventMsg>
    <EncryptPrivateMessages>false</EncryptPrivateMessages>
    <DeletedMessageSortOrder>2</DeletedMessageSortOrder>
    <SayAltGreetWarning>false</SayAltGreetWarning>
    <SaySenderExtension>false</SaySenderExtension>
    <SayAni>false</SayAni>
    <ExitCallActionObjectId>27cbb3a8-f040-4ee9-9686-620c43e3d725</ExitCallActionObjectId>
    <CallAnswerTimeout>4</CallAnswerTimeout>
    <CallHandlerObjectId>9a5ac35a-0df8-4ebb-8e19-77f936dfd263</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/callhandlerprimarytemplates/9a5ac35a-0df8-4ebb-8e19-
    77f936dfd263</CallhandlerURI>
    <DisplayNameRule>1</DisplayNameRule>
    <DoesntExpire>false</DoesntExpire>
    <CantChange>false</CantChange>
    <MailboxStoreObjectId>cfc43112-601b-4764-ba92-b0220e9d7f23</MailboxStoreObjectId>
    <SavedMessageStackOrder>1234567</SavedMessageStackOrder>
    <NewMessageStackOrder>1234567</NewMessageStackOrder>
    <MessageLocatorSortOrder>1</MessageLocatorSortOrder>
    <SavedMessageSortOrder>2</SavedMessageSortOrder>
    <NewMessageSortOrder>1</NewMessageSortOrder>
    <MessageTypeMenu>false</MessageTypeMenu>
    <EnablePersonalRules>true</EnablePersonalRules>
    <RecordUnknownCallerName>true</RecordUnknownCallerName>
    <RingPrimaryPhoneFirst>false</RingPrimaryPhoneFirst>
    <PromptSpeed>100</PromptSpeed>
    <ExitAction>2</ExitAction>
    <ExitTargetConversation>PHTransfer</ExitTargetConversation>
    <ExitTargetHandlerObjectId>7ae69f21-1c99-4cc1-96c3-a1bbe11fd4ca</ExitTargetHandlerObjectId>
    <RepeatMenu>1</RepeatMenu>
    <FirstDigitTimeout>5000</FirstDigitTimeout>
    <InterdigitDelay>3000</InterdigitDelay>
    <PromptVolume>50</PromptVolume>
    <AddressAfterRecord>false</AddressAfterRecord>
    <ConfirmDeleteMessage>false</ConfirmDeleteMessage>
    <ConfirmDeleteDeletedMessage>false</ConfirmDeleteDeletedMessage>
    <ConfirmDeleteMultipleMessages>true</ConfirmDeleteMultipleMessages>
    <IsClockMode24Hour>false</IsClockMode24Hour>
    <RouteNDRToSender>true</RouteNDRToSender>
    <NotificationType>0</NotificationType>
    <SendReadReceipts>0</SendReadReceipts>   
    <ReceiveQuota>-1</ReceiveQuota>
    <SendQuota>-1</SendQuota>
    <WarningQuota>-1</WarningQuota> 
    <IsSetForVmEnrollment>true</IsSetForVmEnrollment>
    <VoiceNameRequired>false</VoiceNameRequired>
    <SendBroadcastMsg>true</SendBroadcastMsg>
    <UpdateBroadcastMsg>false</UpdateBroadcastMsg>
    <ConversationVui>VuiStart</ConversationVui>
    <SpeechCompleteTimeout>0</SpeechCompleteTimeout>
    <SpeechIncompleteTimeout>750</SpeechIncompleteTimeout>
    <UseVui>false</UseVui>
    <SkipPasswordForKnownDevice>false</SkipPasswordForKnownDevice>
    <JumpToMessagesOnLogin>true</JumpToMessagesOnLogin>
    <EnableMessageLocator>false</EnableMessageLocator>
    <MessageAgingPolicyObjectId>2e02eca6-270b-4b7f-a153-
    f03ea74d403d</MessageAgingPolicyObjectId>
    <MessageAgingPolicyURI>/vmrest/messageagingpolicies/2e02eca6-270b-4b7f-a153-
    f03ea74d403d</MessageAgingPolicyURI>
    <AssistantRowsPerPage>5</AssistantRowsPerPage>
    <InboxMessagesPerPage>20</InboxMessagesPerPage>
    <InboxAutoRefresh>15</InboxAutoRefresh>
    <InboxAutoResolveMessageRecipients>true</InboxAutoResolveMessageRecipients>
    <PcaAddressBookRowsPerPage>5</PcaAddressBookRowsPerPage>
    <ReadOnly>false</ReadOnly>
    <EnableTts>true</EnableTts>
    <ConfirmationConfidenceThreshold>60</ConfirmationConfidenceThreshold>
    <AnnounceUpcomingMeetings>60</AnnounceUpcomingMeetings>
    <SpeechConfidenceThreshold>40</SpeechConfidenceThreshold>
    <SpeechSpeedVsAccuracy>50</SpeechSpeedVsAccuracy>
    <SpeechSensitivity>50</SpeechSensitivity>
    <EnableVisualMessageLocator>false</EnableVisualMessageLocator>
    <ContinuousAddMode>false</ContinuousAddMode>
    <NameConfirmation>false</NameConfirmation>
    <CommandDigitTimeout>1500</CommandDigitTimeout>
    <SaveMessageOnHangup>false</SaveMessageOnHangup>
    <SendMessageOnHangup>1</SendMessageOnHangup>
    <SkipForwardTime>5000</SkipForwardTime>
    <SkipReverseTime>5000</SkipReverseTime>
    <UseShortPollForCache>false</UseShortPollForCache>
    <SearchByExtensionSearchSpaceObjectId>25e2e004-c194-4593-9961-
    bdcaf5dd7189</SearchByExtensionSearchSpaceObjectId>
    <SearchByExtensionSearchSpaceURI>/vmrest/searchspaces/25e2e004-c194-4593-9961-
    bdcaf5dd7189</SearchByExtensionSearchSpaceURI>
    <SearchByNameSearchSpaceObjectId>25e2e004-c194-4593-9961-
    bdcaf5dd7189</SearchByNameSearchSpaceObjectId>
    <SearchByNameSearchSpaceURI>/vmrest/searchspaces/25e2e004-c194-4593-9961-
    bdcaf5dd7189</SearchByNameSearchSpaceURI>
    <PartitionObjectId>12101df7-ecd2-4a48-b5b9-9a96b5f85a25</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/12101df7-ecd2-4a48-b5b9-9a96b5f85a25</PartitionURI>
    <UseDynamicNameSearchWeight>false</UseDynamicNameSearchWeight>
    <LdapType>0</LdapType>
    <EnableMessageBookmark>false</EnableMessageBookmark>
    <SayTotalDraftMsg>false</SayTotalDraftMsg>
    <EnableSaveDraft>false</EnableSaveDraft>
    <RetainUrgentMessageFlag>false</RetainUrgentMessageFlag>
    <SayMessageLength>false</SayMessageLength>
    <CreateSmtpProxyFromCorp>false</CreateSmtpProxyFromCorp>
    <AutoAdvanceMsgs>false</AutoAdvanceMsgs>
    <SaySenderAfter>false</SaySenderAfter>
    <SaySenderExtensionAfter>false</SaySenderExtensionAfter>
    <SayMsgNumberAfter>false</SayMsgNumberAfter>
    <SayAniAfter>false</SayAniAfter>
    <SayMessageLengthAfter>false</SayMessageLengthAfter>
    <UserTemplateRolesURI>/vmrest/usertemplates/c8af2544-2bc9-44fa-b713-
    e80f306cf781/usertemplateroles</UserTemplateRolesURI>
    <UserTemplateNotificationDevicesURI>/vmrest/usertemplates/c8af2544-2bc9-44fa-b713-
    e80f306cf781/usertemplatenotificationdevices</UserTemplateNotificationDevicesURI>
    <UserTemplateWebPasswordURI>/vmrest/usertemplates/c8af2544-2bc9-44fa-b713-
    e80f306cf781/credential/password</UserTemplateWebPasswordURI>
    <UserTemplateVoicePinURI>/vmrest/usertemplates/c8af2544-2bc9-44fa-b713-
    e80f306cf781/credential/pin</UserTemplateVoicePinURI>
    <UserTemplateMessageActionURI>/vmrest/usertemplates/c8af2544-2bc9-44fa-b713-
    e80f306cf781/usertemplatemessageactions</UserTemplateMessageActionURI>
</UserTemplate> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectId>
Accept: application/json
Content_type: application/json
Connection: keep_alive |
|---|

| {
    "URI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-099afef0604d"
    "ObjectId":"a46d269a-6614-485b-8649-099afef0604d"
    "UseDefaultLanguage":"true"
    "UseDefaultTimeZone":"true"
    "Alias":"voicemailusertemplate"
    "DisplayName":"Voice Mail User Template"
    "TimeZone":"190"
    "CreationTime":"2013-02-21T11:39:11Z"
    "CosObjectId":"c93854b3-c59f-44e7-a6a9-0a6e17578672"
    "CosURI":"/vmrest/coses/c93854b3-c59f-44e7-a6a9-0a6e17578672"
    "Language":"1033"
    "LocationObjectId":"830e1a2d-8e90-459f-88f7-700497ba975c"
    "LocationURI":"/vmrest/locations/connectionlocations/830e1a2d-8e90-459f-88f7-
     700497ba975c"
    "AddressMode":"0"
    "ClockMode":"0"
    "ConversationTui":"SubMenu"
    "GreetByName":"true"
    "ListInDirectory":"true"
    "IsVmEnrolled":"true"
    "SayCopiedNames":"true"
    "SayDistributionList":"true"
    "SayMsgNumber":"true"
    "SaySender":"true"
    "SayTimestampAfter":"true"
    "SayTimestampBefore":"false"
    "SayTotalNew":"false"
    "SayTotalNewEmail":"false"
    "SayTotalNewFax":"false"
    "SayTotalNewVoice":"true"
    "SayTotalReceipts":"false"
    "SayTotalSaved":"true"
    "Speed":"100"
    "MediaSwitchObjectId":"caf093ef-5e7b-47dd-9db7-9df360d2923e"
    "PhoneSystemURI":"/vmrest/phonesystems/caf093ef-5e7b-47dd-9db7-9df360d2923e"
    "Undeletable":"true"
    "UseBriefPrompts":"false"
    "Volume":"50"
    "EnAltGreetDontRingPhone":"false"
    "EnAltGreetPreventSkip":"false"
    "EnAltGreetPreventMsg":"false"
    "EncryptPrivateMessages":"false"
    "DeletedMessageSortOrder":"2"
    "SayAltGreetWarning":"false"
    "SaySenderExtension":"false"
    "SayAni":"false"
    "ExitCallActionObjectId":"ecc8570c-c0da-493e-a520-b125529cfee1"
    "CallAnswerTimeout":"4"
    "CallHandlerObjectId":"f4f87905-c20a-4df3-b20e-446c1798df19"
    "CallhandlerURI":"/vmrest/callhandlerprimarytemplates/f4f87905-c20a-4df3-b20e-
    446c1798df19"
    "DisplayNameRule":"1"
    "DoesntExpire":"false"
    "CantChange":"false"
    "MailboxStoreObjectId":"90e5847b-3a87-4c92-a753-eda6ea0fdb4c"
    "SavedMessageStackOrder":"1234567"
    "NewMessageStackOrder":"1234567"
    "MessageLocatorSortOrder":"1"
    "SavedMessageSortOrder":"2"
    "NewMessageSortOrder":"1"
    "MessageTypeMenu":"false"
    "EnablePersonalRules":"true"
    "RecordUnknownCallerName":"true"
    "RingPrimaryPhoneFirst":"false"
    "PromptSpeed":"100"
    "ExitAction":"2"
    "ExitTargetConversation":"PHGreeting"
    "ExitTargetHandlerObjectId":"d085ebc6-99ac-46a5-92f3-d26f52701585"
    "RepeatMenu":"1"
    "FirstDigitTimeout":"5000"
    "InterdigitDelay":"3000"
    "PromptVolume":"50"
    "AddressAfterRecord":"false"
    "ConfirmDeleteMessage":"false"
    "ConfirmDeleteDeletedMessage":"false"
    "ConfirmDeleteMultipleMessages":"true"
    "IsClockMode24Hour":"false"
    "RouteNDRToSender":"true"
    "NotificationType":"0"
    "SendReadReceipts":"1"
    "ReceiveQuota":"-2"
    "SendQuota":"-2"
    "WarningQuota":"-2"
    "IsSetForVmEnrollment":"true"
    "VoiceNameRequired":"false"
    "SendBroadcastMsg":"false"
    "UpdateBroadcastMsg":"false"
    "ConversationVui":"VuiStart"
    "SpeechCompleteTimeout":"0"
    "SpeechIncompleteTimeout":"750"
    "UseVui":"false"
    "SkipPasswordForKnownDevice":"false"
    "JumpToMessagesOnLogin":"true"
    "EnableMessageLocator":"false"
    "MessageAgingPolicyObjectId":"12b765a8-a67b-47f6-8ede-3e02aea9f4fe"
    "MessageAgingPolicyURI":"/vmrest/messageagingpolicies/12b765a8-a67b-47f6-8ede-
    3e02aea9f4fe"
    "AssistantRowsPerPage":"5"
    "InboxMessagesPerPage":"20"
    "InboxAutoRefresh":"15"
    "InboxAutoResolveMessageRecipients":"true"
    "PcaAddressBookRowsPerPage":"5"
    "ReadOnly":"false"
    "EnableTts":"true"
    "ConfirmationConfidenceThreshold":"60"
    "AnnounceUpcomingMeetings":"60"
    "SpeechConfidenceThreshold":"40"
    "SpeechSpeedVsAccuracy":"50"
    "SpeechSensitivity":"50"
    "EnableVisualMessageLocator":"false"
    "ContinuousAddMode":"false"
    "NameConfirmation":"false"
    "CommandDigitTimeout":"1500"
    "SaveMessageOnHangup":"false"
    "SendMessageOnHangup":"1"
    "SkipForwardTime":"5000"
    "SkipReverseTime":"5000"
    "UseShortPollForCache":"false"
    "SearchByExtensionSearchSpaceObjectId":"7aaf45b8-ab06-4dda-af16-378b04a95912"
    "SearchByExtensionSearchSpaceURI":"/vmrest/searchspaces/7aaf45b8-ab06-4dda-af16-
    378b04a95912"
    "SearchByNameSearchSpaceObjectId":"7aaf45b8-ab06-4dda-af16-378b04a95912"
    "SearchByNameSearchSpaceURI":"/vmrest/searchspaces/7aaf45b8-ab06-4dda-af16-
    378b04a95912"
    "PartitionObjectId":"9c010254-1493-4e1a-9e47-fe2494792744"
    "PartitionURI":"/vmrest/partitions/9c010254-1493-4e1a-9e47-fe2494792744"
    "UseDynamicNameSearchWeight":"false"
    "LdapType":"0"
    "EnableMessageBookmark":"false"
    "SayTotalDraftMsg":"false"
    "EnableSaveDraft":"false"
    "RetainUrgentMessageFlag":"false"
    "SayMessageLength":"false"
    "CreateSmtpProxyFromCorp":"false"
    "AutoAdvanceMsgs":"false"
    "SaySenderAfter":"false"
    "SaySenderExtensionAfter":"false"
    "SayMsgNumberAfter":"false"
    "SayAniAfter":"false"
    "SayMessageLengthAfter":"false"
    "UserTemplateRolesURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/usertemplateroles"
    "UserTemplateNotificationDevicesURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/usertemplatenotificationdevices"
    "TemplateExternalServiceAccountsURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/templateexternalserviceaccounts"
    "UserTemplateWebPasswordURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/credential/password"
    "UserTemplateVoicePinURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/credential/pin"
    "UserTemplateMessageActionURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/usertemplatemessageactions"
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/usertemplates?query=(PartitionObjectId%20is%20<PartitionObjectId>) |
|---|

| <UserTemplate>
    <URI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-2b13f76bf631</URI>
    <ObjectId>c2056af2-bed7-4a0d-9039-2b13f76bf631</ObjectId>
    <UseDefaultLanguage>true</UseDefaultLanguage>
    <UseDefaultTimeZone>true</UseDefaultTimeZone>
    <Alias>Texoma_User_Template1</Alias>
    <City/>
    <State/>
    <Country>US</Country>
    <PostalCode/>
    <Manager/>
    <Building/>
    <Address/>
    <DisplayName>Texoma_User_Template1</DisplayName>
    <BillingId/>
    <TimeZone>190</TimeZone>
    <CreationTime>2012-12-26 13:04:28.9</CreationTime>
    <CosObjectId>0ef61610-a729-4b0d-9476-cab095028db3</CosObjectId>
    <CosURI>/vmrest/coses/0ef61610-a729-4b0d-9476-cab095028db3</CosURI>
    <Language>1033</Language>
    <LocationObjectId>27a67e01-bcb4-4012-8b1b-f0a08b736087</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/27a67e01-bcb4-4012-8b1b-
    f0a08b736087</LocationURI>
    <AddressMode>0</AddressMode>
    <ClockMode>0</ClockMode>
    <ConversationTui>SubMenu</ConversationTui>
    <GreetByName>true</GreetByName>
    <ListInDirectory>true</ListInDirectory>
    <IsVmEnrolled>true</IsVmEnrolled>
    <SayCopiedNames>true</SayCopiedNames>
    <SayDistributionList>true</SayDistributionList>
    <SayMsgNumber>true</SayMsgNumber>
    <SaySender>true</SaySender>
    <SayTimestampAfter>true</SayTimestampAfter>
    <SayTimestampBefore>false</SayTimestampBefore>
    <SayTotalNew>false</SayTotalNew>
    <SayTotalNewEmail>false</SayTotalNewEmail>
    <SayTotalNewFax>false</SayTotalNewFax>
    <SayTotalNewVoice>true</SayTotalNewVoice>
    <SayTotalReceipts>false</SayTotalReceipts>
    <SayTotalSaved>true</SayTotalSaved>
    <Speed>100</Speed>
    <MediaSwitchObjectId>b6df8cb3-b3ce-4797-84f3-5559049df8e8</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/b6df8cb3-b3ce-4797-84f3-
    5559049df8e8</PhoneSystemURI>
    <Undeletable>false</Undeletable> 
    <UseBriefPrompts>false</UseBriefPrompts>
    <Volume>50</Volume> 
    <EnAltGreetDontRingPhone>false</EnAltGreetDontRingPhone>
    <EnAltGreetPreventSkip>false</EnAltGreetPreventSkip>
    <EnAltGreetPreventMsg>false</EnAltGreetPreventMsg>
    <EncryptPrivateMessages>false</EncryptPrivateMessages>
    <DeletedMessageSortOrder>2</DeletedMessageSortOrder>
    <SayAltGreetWarning>false</SayAltGreetWarning> 
    <SaySenderExtension>false</SaySenderExtension>
    <SayAni>false</SayAni> 
    <ExitCallActionObjectId>0463e49b-cde4-4c30-877c-acfe25966a42</ExitCallActionObjectId>
    <CallAnswerTimeout>4</CallAnswerTimeout>
    <CallHandlerObjectId>83c9b890-6659-4c0f-8be6-8a1a85efee7e</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/callhandlerprimarytemplates/83c9b890-6659-4c0f-8be6-
    8a1a85efee7e</CallhandlerURI>
    <DisplayNameRule>1</DisplayNameRule>
    <DoesntExpire>false</DoesntExpire>
    <CantChange>false</CantChange>
    <MailboxStoreObjectId>e983490d-78a5-45aa-b9a0-31f51460a5bd</MailboxStoreObjectId>
    <SavedMessageStackOrder>1234567</SavedMessageStackOrder>
    <NewMessageStackOrder>1234567</NewMessageStackOrder>
    <MessageLocatorSortOrder>1</MessageLocatorSortOrder>
    <SavedMessageSortOrder>2</SavedMessageSortOrder>
    <NewMessageSortOrder>1</NewMessageSortOrder>
    <MessageTypeMenu>false</MessageTypeMenu>
    <EnablePersonalRules>true</EnablePersonalRules>
    <RecordUnknownCallerName>true</RecordUnknownCallerName>
    <RingPrimaryPhoneFirst>false</RingPrimaryPhoneFirst>
    <PromptSpeed>100</PromptSpeed>
    <ExitAction>2</ExitAction>
    <ExitTargetConversation>PHGreeting</ExitTargetConversation>
    <ExitTargetHandlerObjectId>063956f9-c5ca-4e8b-be67-
    ff945a8a5d99</ExitTargetHandlerObjectId>
    <RepeatMenu>1</RepeatMenu>
    <FirstDigitTimeout>5000</FirstDigitTimeout>
    <InterdigitDelay>3000</InterdigitDelay>
    <PromptVolume>50</PromptVolume>
    <DelayAfterGreeting>0</DelayAfterGreeting>
    <AddressAfterRecord>false</AddressAfterRecord>
    <ConfirmDeleteMessage>false</ConfirmDeleteMessage>
    <ConfirmDeleteDeletedMessage>false</ConfirmDeleteDeletedMessage>
    <ConfirmDeleteMultipleMessages>true</ConfirmDeleteMultipleMessages>
    <IsClockMode24Hour>false</IsClockMode24Hour>
    <RouteNDRToSender>true</RouteNDRToSender>
    <NotificationType>0</NotificationType>
    <SendReadReceipts>1</SendReadReceipts>
    <ReceiveQuota>-2</ReceiveQuota>
    <SendQuota>-2</SendQuota>
    <WarningQuota>-2</WarningQuota>
    <IsSetForVmEnrollment>true</IsSetForVmEnrollment>
    <VoiceNameRequired>false</VoiceNameRequired>
    <SendBroadcastMsg>false</SendBroadcastMsg>
    <UpdateBroadcastMsg>false</UpdateBroadcastMsg>
    <ConversationVui>VuiStart</ConversationVui>
    <SpeechCompleteTimeout>0</SpeechCompleteTimeout>
    <SpeechIncompleteTimeout>750</SpeechIncompleteTimeout>
    <UseVui>false</UseVui>
    <SkipPasswordForKnownDevice>false</SkipPasswordForKnownDevice>
    <JumpToMessagesOnLogin>true</JumpToMessagesOnLogin>
    <EnableMessageLocator>false</EnableMessageLocator>
    <MessageAgingPolicyObjectId>6780a194-6efd-4311-819f-
    494a082bb093</MessageAgingPolicyObjectId>
    <MessageAgingPolicyURI>/vmrest/messageagingpolicies/6780a194-6efd-4311-819f-
    494a082bb093</MessageAgingPolicyURI>
    <AssistantRowsPerPage>5</AssistantRowsPerPage>
    <InboxMessagesPerPage>20</InboxMessagesPerPage>
    <InboxAutoRefresh>15</InboxAutoRefresh>
    <InboxAutoResolveMessageRecipients>true</InboxAutoResolveMessageRecipients>
    <PcaAddressBookRowsPerPage>5</PcaAddressBookRowsPerPage>
    <ReadOnly>false</ReadOnly>
    <EnableTts>true</EnableTts>
    <ConfirmationConfidenceThreshold>60</ConfirmationConfidenceThreshold>
    <AnnounceUpcomingMeetings>60</AnnounceUpcomingMeetings>
    <SpeechConfidenceThreshold>40</SpeechConfidenceThreshold>
    <SpeechSpeedVsAccuracy>50</SpeechSpeedVsAccuracy>
    <SpeechSensitivity>50</SpeechSensitivity>
    <EnableVisualMessageLocator>false</EnableVisualMessageLocator>
    <ContinuousAddMode>false</ContinuousAddMode> 
    <NameConfirmation>false</NameConfirmation> 
    <CommandDigitTimeout>1500</CommandDigitTimeout> 
    <SaveMessageOnHangup>false</SaveMessageOnHangup> 
    <SendMessageOnHangup>1</SendMessageOnHangup> 
    <SkipForwardTime>5000</SkipForwardTime> 
    <SkipReverseTime>5000</SkipReverseTime> 
    <UseShortPollForCache>false</UseShortPollForCache> 
    <SearchByExtensionSearchSpaceObjectId>2e0da21b-54e4-4b51-9f09-
    960049a5e806</SearchByExtensionSearchSpaceObjectId> 
    <SearchByExtensionSearchSpaceURI>/vmrest/searchspaces/2e0da21b-54e4-4b51-9f09-
    960049a5e806</SearchByExtensionSearchSpaceURI> 
    <SearchByNameSearchSpaceObjectId>2e0da21b-54e4-4b51-9f09-
    960049a5e806</SearchByNameSearchSpaceObjectId> 
    <SearchByNameSearchSpaceURI>/vmrest/searchspaces/2e0da21b-54e4-4b51-9f09-
    960049a5e806</SearchByNameSearchSpaceURI>
   <PartitionObjectId>c6ff147e-c32c-4ade-8f12-46427c795c21</PartitionObjectId> 
   <PartitionURI>/vmrest/partitions/c6ff147e-c32c-4ade-8f12-46427c795c21</PartitionURI> 
   <UseDynamicNameSearchWeight>false</UseDynamicNameSearchWeight> 
   <LdapType>0</LdapType> 
   <EnableMessageBookmark>false</EnableMessageBookmark> 
   <SayTotalDraftMsg>false</SayTotalDraftMsg> 
   <EnableSaveDraft>false</EnableSaveDraft> 
   <RetainUrgentMessageFlag>false</RetainUrgentMessageFlag> 
   <SayMessageLength>false</SayMessageLength> 
   <CreateSmtpProxyFromCorp>false</CreateSmtpProxyFromCorp> 
   <AutoAdvanceMsgs>false</AutoAdvanceMsgs> 
   <SaySenderAfter>false</SaySenderAfter> 
   <SaySenderExtensionAfter>false</SaySenderExtensionAfter> 
   <SayMsgNumberAfter>false</SayMsgNumberAfter> 
   <SayAniAfter>false</SayAniAfter> 
   <SayMessageLengthAfter>false</SayMessageLengthAfter> 
   <UserTemplateRolesURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-
   2b13f76bf631/usertemplateroles</UserTemplateRolesURI> 
   <UserTemplateNotificationDevicesURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-
   2b13f76bf631/usertemplatenotificationdevices</UserTemplateNotificationDevicesURI> 
   <TemplateExternalServiceAccountsURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-
   2b13f76bf631/templateexternalserviceaccounts</TemplateExternalServiceAccountsURI> 
   <UserTemplateWebPasswordURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-
   2b13f76bf631/credential/password</UserTemplateWebPasswordURI> 
   <UserTemplateVoicePinURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-
   2b13f76bf631/credential/pin</UserTemplateVoicePinURI> 
   <UserTemplateMessageActionURI>/vmrest/usertemplates/c2056af2-bed7-4a0d-9039-
   2b13f76bf631/usertemplatemessageactions</UserTemplateMessageActionURI>
</UserTemplate> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/usertemplates?query=(PartitionObjectId%20is%20<PartitionObjectId>)
Accept: application/json
Content_type: application/json
Connection: keep_alive |
|---|

| {
    "URI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-099afef0604d"
    "ObjectId":"a46d269a-6614-485b-8649-099afef0604d"
    "UseDefaultLanguage":"true"
    "UseDefaultTimeZone":"true"
    "Alias":"voicemailusertemplate"
    "DisplayName":"Voice Mail User Template"
    "TimeZone":"190"
    "CreationTime":"2013-02-21T11:39:11Z"
    "CosObjectId":"c93854b3-c59f-44e7-a6a9-0a6e17578672"
    "CosURI":"/vmrest/coses/c93854b3-c59f-44e7-a6a9-0a6e17578672"
    "Language":"1033"
    "LocationObjectId":"830e1a2d-8e90-459f-88f7-700497ba975c"
    "LocationURI":"/vmrest/locations/connectionlocations/830e1a2d-8e90-459f-88f7-
    700497ba975c"
    "AddressMode":"0"
    "ClockMode":"0"
    "ConversationTui":"SubMenu"
    "GreetByName":"true"
    "ListInDirectory":"true"
    "IsVmEnrolled":"true"
    "SayCopiedNames":"true"
    "SayDistributionList":"true"
    "SayMsgNumber":"true"
    "SaySender":"true"
    "SayTimestampAfter":"true"
    "SayTimestampBefore":"false"
    "SayTotalNew":"false"
    "SayTotalNewEmail":"false"
    "SayTotalNewFax":"false"
    "SayTotalNewVoice":"true"
    "SayTotalReceipts":"false"
    "SayTotalSaved":"true"
    "Speed":"100"
    "MediaSwitchObjectId":"caf093ef-5e7b-47dd-9db7-9df360d2923e"
    "PhoneSystemURI":"/vmrest/phonesystems/caf093ef-5e7b-47dd-9db7-9df360d2923e"
    "Undeletable":"true"
    "UseBriefPrompts":"false"
    "Volume":"50"
    "EnAltGreetDontRingPhone":"false"
    "EnAltGreetPreventSkip":"false"
    "EnAltGreetPreventMsg":"false"
    "EncryptPrivateMessages":"false"
    "DeletedMessageSortOrder":"2"
    "SayAltGreetWarning":"false"
    "SaySenderExtension":"false"
    "SayAni":"false"
    "ExitCallActionObjectId":"ecc8570c-c0da-493e-a520-b125529cfee1"
    "CallAnswerTimeout":"4"
    "CallHandlerObjectId":"f4f87905-c20a-4df3-b20e-446c1798df19"
    "CallhandlerURI":"/vmrest/callhandlerprimarytemplates/f4f87905-c20a-4df3-b20e-
    446c1798df19"
    "DisplayNameRule":"1"
    "DoesntExpire":"false"
    "CantChange":"false"
    "MailboxStoreObjectId":"90e5847b-3a87-4c92-a753-eda6ea0fdb4c"
    "SavedMessageStackOrder":"1234567"
    "NewMessageStackOrder":"1234567"
    "MessageLocatorSortOrder":"1"
    "SavedMessageSortOrder":"2"
    "NewMessageSortOrder":"1"
    "MessageTypeMenu":"false"
    "EnablePersonalRules":"true"
    "RecordUnknownCallerName":"true"
    "RingPrimaryPhoneFirst":"false"
    "PromptSpeed":"100"
    "ExitAction":"2"
    "ExitTargetConversation":"PHGreeting"
    "ExitTargetHandlerObjectId":"d085ebc6-99ac-46a5-92f3-d26f52701585"
    "RepeatMenu":"1"
    "FirstDigitTimeout":"5000"
    "InterdigitDelay":"3000"
    "PromptVolume":"50"
    "AddressAfterRecord":"false"
    "ConfirmDeleteMessage":"false"
    "ConfirmDeleteDeletedMessage":"false"
    "ConfirmDeleteMultipleMessages":"true"
    "IsClockMode24Hour":"false"
    "RouteNDRToSender":"true"
    "NotificationType":"0"
    "SendReadReceipts":"1"
    "ReceiveQuota":"-2"
    "SendQuota":"-2"
    "WarningQuota":"-2"
    "IsSetForVmEnrollment":"true"
    "VoiceNameRequired":"false"
    "SendBroadcastMsg":"false"
    "UpdateBroadcastMsg":"false"
    "ConversationVui":"VuiStart"
    "SpeechCompleteTimeout":"0"
    "SpeechIncompleteTimeout":"750"
    "UseVui":"false"
    "SkipPasswordForKnownDevice":"false"
    "JumpToMessagesOnLogin":"true"
    "EnableMessageLocator":"false"
    "MessageAgingPolicyObjectId":"12b765a8-a67b-47f6-8ede-3e02aea9f4fe"
    "MessageAgingPolicyURI":"/vmrest/messageagingpolicies/12b765a8-a67b-47f6-8ede-
    3e02aea9f4fe"
    "AssistantRowsPerPage":"5"
    "InboxMessagesPerPage":"20"
    "InboxAutoRefresh":"15"
    "InboxAutoResolveMessageRecipients":"true"
    "PcaAddressBookRowsPerPage":"5"
    "ReadOnly":"false"
    "EnableTts":"true"
    "ConfirmationConfidenceThreshold":"60"
    "AnnounceUpcomingMeetings":"60"
    "SpeechConfidenceThreshold":"40"
    "SpeechSpeedVsAccuracy":"50"
    "SpeechSensitivity":"50"
    "EnableVisualMessageLocator":"false"
    "ContinuousAddMode":"false"
    "NameConfirmation":"false"
    "CommandDigitTimeout":"1500"
    "SaveMessageOnHangup":"false"
    "SendMessageOnHangup":"1"
    "SkipForwardTime":"5000"
    "SkipReverseTime":"5000"
    "UseShortPollForCache":"false"
    "SearchByExtensionSearchSpaceObjectId":"7aaf45b8-ab06-4dda-af16-378b04a95912"
    "SearchByExtensionSearchSpaceURI":"/vmrest/searchspaces/7aaf45b8-ab06-4dda-af16-378b04a95912"
    "SearchByNameSearchSpaceObjectId":"7aaf45b8-ab06-4dda-af16-
    378b04a95912"
    "SearchByNameSearchSpaceURI":"/vmrest/searchspaces/7aaf45b8-ab06-4dda-af16-
    378b04a95912"
    "PartitionObjectId":"9c010254-1493-4e1a-9e47-fe2494792744"
    "PartitionURI":"/vmrest/partitions/9c010254-1493-4e1a-9e47-fe2494792744"
    "UseDynamicNameSearchWeight":"false"
    "LdapType":"0"
    "EnableMessageBookmark":"false"
    "SayTotalDraftMsg":"false"
    "EnableSaveDraft":"false"
    "RetainUrgentMessageFlag":"false"
    "SayMessageLength":"false"
    "CreateSmtpProxyFromCorp":"false"
    "AutoAdvanceMsgs":"false"
    "SaySenderAfter":"false"
    "SaySenderExtensionAfter":"false"
    "SayMsgNumberAfter":"false"
    "SayAniAfter":"false"
    "SayMessageLengthAfter":"false"
    "UserTemplateRolesURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/usertemplateroles"
    "UserTemplateNotificationDevicesURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/usertemplatenotificationdevices"
    "TemplateExternalServiceAccountsURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/templateexternalserviceaccounts"
    "UserTemplateWebPasswordURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/credential/password"
    "UserTemplateVoicePinURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/credential/pin"
    "UserTemplateMessageActionURI":"/vmrest/usertemplates/a46d269a-6614-485b-8649-
    099afef0604d/usertemplatemessageactions"
} |
|---|

| Response Code: 200 |
|---|

| Note | Same way user templates can be viewed for particular COS object ID, mailbox store object ID, phone system and call handler
                                                object ID. PartitionObjectId can be viewed from https://<connection-server>/vmrest/partitions COSObjectId : https://<connection-server>/vmrest/coses PhoneSystem : https://<connection-server>/vmrest/phonesystems |
|---|---|

| POST https://<connection-server>/vmrest/usertemplates?templateAlias=voicemailusertemplate
Request Body:
<UserTemplate>
    <Alias>ABC_user template</Alias>
    <DisplayName>ABC@user template</DisplayName>
</UserTemplate> |
|---|

| Response Code: 201 |
|---|

| POST https://<connection-server>/vmrest/usertemplates?templateAlias=voicemailusertemplate
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "Alias":"voicemailusertemplate1",
    "DisplayName":"Voice Mail User Template 1"
} |
|---|

| Response Code: 201 |
|---|

| POST https://<connection-server>/vmrest/usertemplates?templateAlias=voicemailusertemplate
Request Body:
<UserTemplate>
    <Alias>ABCs_user template</Alias>
    <DisplayName>ABCs@user template</DisplayName>
    <PartitionObjectId>00c25bc8-d3d0-45ec-a786-fcf7a35593cf</PartitionObjectId>
</UserTemplate> |
|---|

| Response Code: 201 |
|---|

| Note | Get partition object Id from " https://<connection-server>/vmrest/partitions " . In same way users templates can be created
                                             using specific COS object ID, MailboxStoreObjectId, Phone System. |
|---|---|

| Request URI:
POST https://<connection-server>/vmrest/usertemplates?templateAlias=<TemplatealiasName> 
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "Alias":"voicemailusertemplate12",
    "DisplayName":"Voice Mail User Templater12",
    "PartitionObjectId":"be52d373-25c4-416c-81c1-b82479061192"
} |
|---|

| Response Code: 201 |
|---|

| PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>
Request Body:
<UserTemplate>
    <Alias>ABCD_user template</Alias>
    <UseDefaultLanguage>true</UseDefaultLanguage>
    <Language>1033</Language>
    <UseDefaultTimeZone>true</UseDefaultTimeZone>
    <TimeZone>190</TimeZone>
    <CosObjectId>6f054167-6f6c-4ed5-a498-1776337871ee</CosObjectId> 
    <MediaSwitchObjectId>221ee752-5147-4326-9990-d4a138674f9e</MediaSwitchObjectId> 
</UserTemplate> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "Alias":"ABC_user template",
    "DisplayName":"Auser template",
    "UseDefaultLanguage":"false",
    "TimeZone":"190",
    "MediaSwitchObjectId":"caf093ef-5e7b-47dd-9db7-9df360d2923e",
    "CosObjectId":"c93854b3-c59f-44e7-a6a9-0a6e17578672"
} |
|---|

| Response Code: 204 |
|---|

| GET https://<connection-server>/vmrest/languagemap |
|---|

| PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>
Request Body:
<UserTemplate>
    <Country>SA</Country>
</UserTemplate> |
|---|

| Response Code: 204 |
|---|

| Request URI:
PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "Country":"XY"
} |
|---|

| Response Code: 204 |
|---|

| Note | Country code must only have 2 character codes. |
|---|---|

| PUT https://<connection-server>/vmrest/languagemap |
|---|

| PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>
Request Body:
<UserTemplate>
    <Language>1025</Language>
</UserTemplate> |
|---|

| Response Code: 204 |
|---|

| Request URI:
PUT https://<connection-server>/vmrest/usertemplates/< usertemplateobjectid >
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "Language":"1025"
} |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid> |
|---|

| Response Code: 204 |
|---|

| Request URI:
DELETE https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/credential/pin
Request Body:
<UserTemplateCredential>
    <Credentials>142536</Credentials> 
</UserTemplateCredential> |
|---|

| Response Code: 204 |
|---|

| Note | Voicemail should be in numeric only. |
|---|---|

| Request URI:
PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/credential/pin
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "Credentials":"10255"
} |
|---|

| Response Code: 204 |
|---|

| Request Body:
<UserTemplateCredential>
    <DoesntExpire>true</DoesntExpire>
    <Locked>false</Locked>
    <CantChange>false</CantChange> 
    <CredMustChange>false</CredMustChange>
    <CredentialPolicyObjectId>58f0dc20-f8fc-467d-a648-b5ffbba87dd9</CredentialPolicyObjectId> 
</UserTemplateCredential> |
|---|

| Response Code: 204 |
|---|

| Note | Updating fields can be done only when "CredMustChange" parameter
                                                			 is false and in order to change authentication rule and to view authentication
                                                			 rule use the following URI: |
|---|---|

| GET https://<connection-server>/vmrest /authenticationrules |
|---|

| PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/credential/password
Request Body:
<UserTemplateCredential>
    <Credentials>Cisco123</Credentials> 
</UserTemplateCredential> |
|---|

| Response Code: 204 |
|---|

| Note | Web password should be in alphanumeric only. |
|---|---|

| Request URI:
PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/credential/password
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "Credentials":"10255",
    "CantChange":"false",
    "DoesntExpire":"true",
    "Locked":"false",
    "CredMustChange":"false",
    "CredentialPolicyObjectId":"7b282b66-73b1-4989-9d94-3d105b6ef5e8"
} |
|---|

| Response Code: 204 |
|---|

| Request Body:
<UserTemplateCredential>
    <DoesntExpire>true</DoesntExpire>
    <Locked>false</Locked>
    <CantChange>false</CantChange> 
    <CredMustChange>false</CredMustChange>
    <CredentialPolicyObjectId>58f0dc20-f8fc-467d-a648-b5ffbba87dd9</CredentialPolicyObjectId> 
</UserTemplateCredential> |
|---|

| Response Code: 204 |
|---|

| Note | Updating fields can be done only when "CredMustChange" parameter
                                                			 is false and in order to change authentication rule and to view authentication
                                                			 rule use the following URI: |
|---|---|

| GET https://<connection-server>/vmrest /authenticationrules |
|---|

| GET https://<connection-server>/vmrest/roles |
|---|

| PUT https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplateroles
Request Body:
<UserTemplateRole>
    <RoleObjectId>4f077e4e-61c7-4ce8-a58a-2c4bc6089319</RoleObjectId>
</UserTemplateRole> |
|---|

| Response Code: 201 |
|---|

| Request URI:
POST https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplateroles
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "RoleObjectId":"04d0f1ef-a8c6-454a-8cf0-0e8db7bb2b15"
} |
|---|

| Response Code: 201 |
|---|

| GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplateroles |
|---|

| <UserTemplateRole>
    <URI>/vmrest/usertemplates/d8054a3a-6c09-4a25-9880-
    6589d2f1dc85/usertemplateroles/973e143e-af15-4ef4-a7c1-5fafd9cc53d4</URI>
    <ObjectId>973e143e-af15-4ef4-a7c1-5fafd9cc53d4</ObjectId>
    <UserObjectId>d8054a3a-6c09-4a25-9880-6589d2f1dc85</UserObjectId>
    <UserURI>/vmrest/users/d8054a3a-6c09-4a25-9880-6589d2f1dc85</UserURI>
    <RoleObjectId>ba166947-41e8-4ec9-ad14-03658d91240e</RoleObjectId>
    <RoleURI>/vmrest/roles/ba166947-41e8-4ec9-ad14-03658d91240e</RoleURI>
    <RoleName>Audit Administrator</RoleName>
    <Alias>ABCD_user template</Alias>
</UserTemplateRole> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplateroles
Accept: application/json
Content_type: application/json
Connection: keep_alive |
|---|

| {
  "@total":"1"
  "UserTemplateRole":
  {
    "URI":"/vmrest/usertemplates/a9272189-720b-44b3-86e0-
    df7ef519599c/usertemplateroles/167b7661-ee8b-4c83-8867-decb88ec0c1c"
    "ObjectId":"167b7661-ee8b-4c83-8867-decb88ec0c1c"
    "UserObjectId":"a9272189-720b-44b3-86e0-df7ef519599c"
    "UserURI":"/vmrest/users/a9272189-720b-44b3-86e0-df7ef519599c"
    "RoleObjectId":"04d0f1ef-a8c6-454a-8cf0-0e8db7bb2b15"
    "RoleURI":"/vmrest/roles/04d0f1ef-a8c6-454a-8cf0-0e8db7bb2b15"
    "RoleName":"Help Desk Administrator"
    "Alias":"tenant005_usertemplate_1"
  }
} |
|---|

| Response Code: 200 |
|---|

| DELETE https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplateroles/<usertemplaterolesId> |
|---|

| Response Code: 204 |
|---|

| Request URI:
DELETE https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/usertemplateroles/<usertemplateroleid>
Accept: application/json
Content_type: application/json
Connection: keep_alive |
|---|

| Response Code: 204 |
|---|

| Parameter | Data Type | Operations | Comments |
|---|---|---|---|
| Alias | String(64) | Read/Write | A unique text name for addressable objects:
                                                					 Global Users, Contacts, DistributionLists, and PersonalGroups. |
| Display Name | String(64) | Read/Write | Enter a descriptive name for the user
                                                					 template. |
| ObjectId | String(36) | Read-Only | Specifies a globally unique,
                                                					 system-generated identifier for a UserSubscriber object. |
| TenantObjectId | String(36) | Read-Only | The unique identifier of the tenant to
                                                					 which the user template belongs. This field is reflected in the response only
                                                					 if the user template belongs to a particular tenant. |
| UseDefaultLanguage | Boolean | Read/Write | Possible values can be: False: The
                                                         						  language is the default language defined for the user template. True: The
                                                         						  language is derived from the location to which this user template belongs. Default value: False |
| UseDefaultTimeZone | Boolean | Read/Write | Possible values can be: False: The time
                                                         						  zone is the default time zone defined for the user template. True: The time
                                                         						  zone is derived from the location to which this user template belongs. Default value: False |
| City | String(64) | Read/Write | Enter the city. (optional) |
| State | String(64) | Read/Write | Enter the state. (optional) |
| Country | String(2) | Read/Write | Enter the country. (optional) |
| PostalCode | String(40) | Read/Write | Enter the Postal code (optional) |
| Department | String(64) | Read/Write | Enter the users department. (optional) |
| Manager | String(64) | Read/Write | Enter the name of the manager. (optional) |
| Address | String(64) | Read/Write | Enter the user address .(optional) |
| BillingId | String(32) | Read/Write | Billing ID can be used for
                                                					 organization-specific information, such as accounting information, department
                                                					 names, or project codes. |
| TimeZone | Integer | Read/Write | Select the desired time zone for the user,
                                                					 or check the Use System Default Time Zone check box. |
| CreationTime | DateTime | Read-Only | The date and time the user template was
                                                					 created. |
| CosObjectId | String(36) | Read/Write | The unique identifier of the COS (Class of
                                                					 Service) object to which this user template account is associated. |
| Language | Integer | Read/Write | Select Use System Default Language or
                                                					 select a language from the list |
| VoiceName | String | Read/Write | Wav file that contains recorded name. |
| LocationObjectId | String(36) | Read-Only | The unique identifier of the LocationVMS
                                                					 object to which this user belongs. |
| AddressMode | Integer | Default | The default method the subscriber will use
                                                					 to address messages to other subscribers. Possible options are: 0=LastNameFirst 1=Extension 2=FirstNameFirst |
| ClockMode | Integer | Read-Only | The time format used for the message
                                                					 timestamps that the subscriber hears when they listen to their messages over
                                                					 the phone. Possible options are: 0=SystemDefaultClock 1=HourClock12 2=HourClock24 |
| ConversationTUI | String(36) | Read-Only | The name of the conversation the subscriber
                                                					 uses to set up, send, and retrieve messages. |
| GreetByName | Boolean | Read-Only | A flag indicating whether the subscriber
                                                					 hears his/her name when they log into their mailbox over the phone. Values can be: False: Do not
                                                         						  play the name. True: Play the
                                                         						  recorded voice name. Default value: True |
| ListInDirectory | Boolean | Read/Write | A flag indicating whether system should
                                                					 list the subscriber in the phone directory for outside callers. Possible values can be: False: Do not
                                                         						  list the subscriber in the phone directory. True: List the
                                                         						  subscriber in the phone directory. Default value: True |
| IsVmEnrolled | Boolean | Read/Write | A flag indicating whether system plays the
                                                					 enrollment conversation (record a voice name, indicate if they are listed in
                                                					 the directory, etc.) for the subscriber when they login. Values can be: False: The
                                                         						  enrollment conversation is not played for the subscriber when they login. True: The
                                                         						  enrollment conversation is played for the subscriber when they login. Default value: True |
| SayCopiedNames | Boolean | Read/Write | A flag indicating whether system announces
                                                					 the "copied" names during message playback for a subscriber. Values can be: False: Do not
                                                         						  announce copied names. True: Announce
                                                         						  copied names. Default value: True |
| SayDistributionList | Boolean | Read/Write | A flag indicating whether system announces
                                                					 the distribution list that sends a message, if applicable. Values can be: False: Do not
                                                         						  announce the distribution list. True: Announce
                                                         						  the distribution list. Default value: True |
| SayMsgNumber | Boolean | Read/Write | A flag indicating whether system announces
                                                					 the position of each message in the stack (i.e., 'Message 1', 'Message 2'
                                                					 ,etc.) during message playback for the subscriber. Values can be: False: Do not
                                                         						  play the message number. True: Play the
                                                         						  message number. Default value: True |
| SaySender | Boolean | Read/Write | A flag indicating whether system announces
                                                					 the sender of a message during message playback for the subscriber. Values can be: False: Do not
                                                         						  announce the sender. True: Announce
                                                         						  the sender. Default value: True |
| SayTimeStampAfter | Boolean | Read/Write | A flag indicating whether system announces
                                                					 the timestamp after it plays back each message for the subscriber. Values can be: False: Do not
                                                         						  announce the timestamp after each message is played. True: Announce
                                                         						  the timestamp after each message is played. Default value: True |
| SayTimeStampBefore | Boolean | Read/Write | A flag indicating whether system announces
                                                					 the timestamp before it plays back each for the subscriber. Values can be: False: Do not
                                                         						  announce the timestamp before each message is played. True Announce
                                                         						  the timestamp before each message is played. Default value: False |
| SayTotalNew | Boolean | Read/Write | A flag indicating whether system announces
                                                					 the total number of new messages in the subscriber mailbox. Values can be: False: Do not
                                                         						  announce total number of new messages. True: Announce
                                                         						  the total number of new messages in the subscriber mailbox. Default value: False |
| SayTotalNewEmail | Boolean | Read/Write | A flag indicating whether system announces
                                                					 the total number of new e-mail messages in the subscriber mailbox. Values can be: False: Do not
                                                         						  announce total number of new e-mail messages. True: Announce
                                                         						  the total number of new e-mail messages in the subscriber mailbox. Default value: False |
| SayTotalNewFax | Boolean | Read/Write | A flag indicating whether system announces
                                                					 the total number of new fax messages in the subscriber mailbox. Values can be: False: Do not
                                                         						  announce total number of new fax messages. True: Announce
                                                         						  the total number of new fax messages in the subscriber mailbox. Default value: False |
| SayTotalNewVoice | Boolean | Read/Write | A flag indicating whether system announces
                                                					 the total number of new voice messages in the subscriber mailbox. Values can be: False: Do not
                                                         						  announce total number of new voice messages. True: Announce
                                                         						  the total number of new voice messages in the subscriber mailbox. Default value: True |
| SayTotalReceipts | Boolean | Read/Write | A flag indicating whether system announces
                                                					 the total number of new receipts in the subscriber mailbox. Values can be: False: Do not
                                                         						  announce total number of new receipts. True: Announce
                                                         						  the total number of new receipts in the subscriber mailbox. Default value: False |
| SayTotalSaved | Boolean | Read/Write | A flag indicating whether system announces
                                                					 the total number of saved messages in the subscriber mailbox. Values can be: False: Do not
                                                         						  announce total number of saved messages. True: Announce
                                                         						  the total number of saved messages in the subscriber mailbox. Default value: True |
| Speed | Integer | Read/Write | The audio speed system uses to play back
                                                					 messages to the subscriber. Range: 0-200. |
| MediaSwitchObjectId | String(36) | Read-Only | The unique identifier of the MediaSwitch
                                                					 object Cisco Unity Connection uses for subscriber Telephone Record and Playback
                                                					 (TRAP) sessions and to dial MWI on or off requests when the Cisco Unity
                                                					 Connection system has dual switch integration. |
| Undeletable | Boolean | Read/Write | Tells whether it can be deleted by
                                                					 administrator or not. |
| UseBriefPrompts | Boolean | Read/Write | A flag indicating whether the subscriber
                                                					 hears brief or full phone menus when accessing system over the phone. Default value: False |
| Volume | Integer | Read/Write | The audio volume expressed as a percentage
                                                					 that Cisco Unity Connection uses to play back message. Range: 0-100 |
| EnAltGreetDontRingPhone | Boolean | Read-Only | A flag indicating whether a caller is
                                                					 prevented from being transferred to the subscriber phone when the subscriber
                                                					 alternate greeting is turned on. Values can be: False: Ring the
                                                         						  phone. True: Send the
                                                         						  caller to the alternate greeting. Default value: False |
| EnAltGreetPreventSkip | Boolean | Read-Only | A flag indicating whether callers can skip
                                                					 the greeting while it is playing when the alternate greeting is turned on. Values can be: False: If
                                                         						  alternate greeting is active, callers cannot skip the greeting\ True: If
                                                         						  alternate greeting is active, callers can skip the greeting. Default value: False |
| EnAltGreetPreventMsg | Boolean | Read-Only | A flag indicating whether callers can leave
                                                					 a message after the greeting when the subscriber alternate greeting is turned
                                                					 on. Values can be: False: If
                                                         						  alternate greeting is active, callers can leave a message for the subscriber True: If
                                                         						  alternate greeting is active, callers cannot leave a message for the
                                                         						  subscriber. Default value: False |
| EncryptPrivateMessages | Boolean | Read-Only | A flag indicating whether system encrypts
                                                					 messages from the subscriber that are marked private. Values can be: False: Do not
                                                         						  encrypt private messages. True: Encrypt
                                                         						  private messages. Default value: False |
| DeletedMessageSortOrder | Integer | Read-Only | The order in which system presents deleted
                                                					 messages to the subscriber. |
| SayAltGreetWarning | Boolean | Read-Only | A flag indicating whether Cisco Unity
                                                					 Connection notifies the subscriber when they login via the phone (plays
                                                					 conversation) or CPCA (displays a warning banner) if their alternate greeting
                                                					 is turned on. Values can be: False: Do not
                                                         						  notify the subscriber that their alternate greeting is turned on. True: Notify the
                                                         						  subscriber when they login if their alternate greeting is turned on. Default value: False |
| SaySenderExtension | Boolean | Read-Only | A flag indicating whether Cisco Unity
                                                					 Connection during message playback, plays the primary extension information of
                                                					 the subscriber who sent the message after playing the sender's voice name. Values can be: False: Do not
                                                         						  play the extension information of the subscriber who sent the message. True: After
                                                         						  playing the sender's voice name, play the primary extension information of the
                                                         						  subscriber who sent the message. Default value: False |
| SayAni | Boolean | Read-Only | A flag indicating whether Cisco Unity
                                                					 Connection plays the Automatic Number Identification (ANI) information during
                                                					 message playback for voice messages from unidentified callers. Default value: False |
| ExitCallActionObjectId | String(36) | Read-Only | The unique identifier of the CallAction
                                                					 object that is taken when a caller exits the subscriber conversation by
                                                					 pressing the * key or timing out. |
| CallAnswerTimeout | Integer | Read/Write | The number of rings to wait for a
                                                					 subscriber destination to answer before the call is forwarded to the
                                                					 subscriber's primary phone. |
| CallHandlerObjectId | String(36) | Read-Only | The unique identifier of the primary
                                                					 CallHandler object for the subscriber. |
| DisplayNameRule | Integer | Read/Write | The format for generating the user display
                                                					 name. |
| DoesntExpire | Boolean | Read/Write | A flag indicating whether or not the user
                                                					 credential will automatically expire (and the user required to change the
                                                					 credential upon its expiration) based on a defined schedule. Regardless, the
                                                					 user still may change the credential (if allowed by CantChange). Values can be: False: The user
                                                         						  credential will automatically expire. The expiration of the credential is
                                                         						  controlled by the value of the column tbl_CredentialPolicy->MaxDays. True: The user
                                                         						  credential will not automatically expire. Default value: False |
| CantChange | Boolean | Read-Only | A flag indicating whether the user can
                                                					 set/change their credential (i.e., the credential specified by the associated
                                                					 credential policy). Values can be: False: User is
                                                         						  allowed to change their credential. True: User
                                                         						  cannot change their credential. Default value: False |
| MailboxStoreObjectId | String(36) | Read-Only | The unique identifier of the MailboxStore
                                                					 object where a mailbox is created for a new subscriber created with this
                                                					 template. |
| SavedMessageStackOrder | String(36) | Read/Write | The order in which system plays the
                                                					 following types of saved messages: Urgent voice
                                                         						  messages Non-urgent voice
                                                         						  messages Urgent fax
                                                         						  messages Non-urgent fax
                                                         						  messages Urgent e-mail
                                                         						  messages Non-urgent
                                                         						  e-mail messages Receipts and
                                                         						  notices |
| NewMessageStackOrder | String(36) | Read/Write | The order in which system plays the
                                                					 following types new messages: Urgent voice
                                                         						  messages Non-urgent voice
                                                         						  messages* Urgent fax messages Non-urgent fax
                                                         						  messages Urgent e-mail
                                                         						  messages Non-urgent
                                                         						  e-mail messages Receipts and
                                                         						  notices |
| MessageLocatorSortOrder | Integer | Read/Write | The order in which system will sort
                                                					 messages when the "Message Locator" feature is enabled. |
| SavedMessageSortOrder | Integer | Read/Write | The order in which system will sort saved
                                                					 messages. |
| NewMessageSortOrder | Integer | Read/Write | The order in which system will sort new
                                                					 messages. |
| MessageTypeMenu | Boolean | Read/Write | A flag indicating whether system plays the
                                                					 message type menu when the subscriber logs on to system over the phone. Values can be: False: Do not
                                                         						  play message type menu. True: Play
                                                         						  message type menu. Default value: False |
| EnablePersonalRules | Boolena | Read/Write | A flag indicating whether a subscriber's
                                                					 personal rules are enabled. Subscribers can use this setting to disable all
                                                					 personal rules at once. Values can be: False: Call
                                                         						  routing rules disabled for subscriber. 1: Call routing
                                                         						  rules enabled for subscriber. True: Call
                                                         						  routing rules enabled for subscriber. Default value: True |
| ForcedAuthorizationCode | String(36) | Read-Only | A valid authorization code that is entered
                                                					 prior to extending calls to classes of dialed numbers, for example, external,
                                                					 toll and international calls. |
| RecordUnknownCallerName | Boolean | Read/Write | A flag indicating whether a caller should
                                                					 be promoted to record his/her name if Unity does not receive caller id. Default value: True |
| RingPrimaryPhoneFirst | Boolean | Read/Write | A flag indicating whether a subscriber's
                                                					 primary phone should be rung before trying other destinations in a personal
                                                					 group. Default value: False |
| PromptSpeed | Integer | Read/Write | The audio speed system uses to play back
                                                					 prompts to the subscriber. |
| ExitAction | Integer | Read/Write | Type of call action to take, e.g., hang-up,
                                                					 go to another object, etc. |
| ExitTargetConversation | String(64) | Read/Write | The name of the conversation to which the
                                                					 caller is routed. |
| ExitTargetHandlerObjectId | String(36) | Read-Only | The unique identifier of the specific
                                                					 object to send along to the target conversation. |
| RepeatMenu | Integer | Read/Write | The number of times to repeat a menu in
                                                					 TUI. Possible range 0-250 |
| FirstDigitTimeout | Integer | Read/Write | The amount of time to wait (in
                                                					 milliseconds) for first digits when collecting touch tones. Range: 500-10000. |
| InterdigitDelay | Integer | Read-Only | The amount of time to wait (in
                                                					 milliseconds) for input between touch tones when collecting digits in TUI.
                                                					 Range: 1000-10000 |
| PromptVolume | Integer | Read/Write | The volume level for playback of system
                                                					 prompts. Range: 0-100. |
| DelayAfterGreeting | Integer | Read/Write | The amount of time (in milliseconds) Cisco
                                                					 Unity Connection will delay after playing greeting. Range: 0-50000. |
| ClientMatterCode | String(40) | Read-Only | The client matter code to transmit to Call
                                                					 Manger when a phone number is dialed on an outbound call. The CMC is entered
                                                					 after a phone number is dialed so that the customer can assign account or
                                                					 billing codes to the call. Whether or not the CMC will be transmitted is
                                                					 dictated by a setting on outbound call. The subscriber's CMC is used only if
                                                					 the outbound call doesn't have its own CMC. |
| AddressAfterRecord | Boolean | Read/Write | A flag indicating whether the subscriber
                                                					 will be prompted to address message before or after it is recorded. Values can be: False: Prompt
                                                         						  subscriber to address message before recording. True: Prompt
                                                         						  subscriber to address message after recording. Default value: False |
| ConfirmDeleteMessage | Boolean | Read/Write | A flag indicating whether system will
                                                					 request confirmation from a subscriber before proceeding with a deletion of a
                                                					 single new or saved message. Values can be: False: system
                                                         						  will not request confirmation from a subscriber before proceeding with a
                                                         						  deletion of a single new or saved message. True: system
                                                         						  will request confirmation from a subscriber before proceeding with a deletion
                                                         						  of a single new or saved message. Default value: False |
| ConfirmDeleteMultipleMessage | Boolean | Read/Write | A flag indicating whether system allows the
                                                					 subscriber to choose which message they want to delete or whether system
                                                					 permanently deletes the specified type of messages. A change what system does
                                                					 when subscribers press 3 > 2 > 2 from the Main menu to permanently delete
                                                					 multiple deleted messages at once. Values can be: False: System
                                                         						  does not prompt the subscriber to choose, and instead permanently deletes the
                                                         						  type of messages you specify: either deleted voice messages or all deleted
                                                         						  messages (voice, fax, and e-mail, as applicable). True: System
                                                         						  allows the subscriber to choose which messages they want to delete; subscriber
                                                         						  can either delete their deleted voice messages or delete all of their deleted
                                                         						  messages. Default value: True |
| PabLastImported | String(36) | Read-Only | The date and time when the personal address
                                                					 book was last imported from a groupware package into the personal groups for a
                                                					 user. |
| IsClockMode24Hour | Boolean | Read/Write | The time format used for the message
                                                					 timestamps that the subscriber hears when they listen to their messages over
                                                					 the phone. Values can be: False: 12-Hour
                                                         						  clock - The subscriber hears message timestamps in the time format of a 12-hour
                                                         						  clock. For example, a subscriber will hear 1:00 PM when listening to the
                                                         						  timestamp of a message left at 1:00 PM. True: 24-Hour
                                                         						  clock - The subscriber hears message timestamps in the time format of a 24-hour
                                                         						  clock. For example, a subscriber will hear 13:00 when listening to the
                                                         						  timestamp of a message left at 1:00 PM. Default value: False |
| RouteNDRToSender | Boolean | Read/Write | For an undeliverable message, whether NDR
                                                					 messages will appear in the subscriber mailbox or are deleted by the system. |
| NotificationType | Integer | Read/Write | The notification type to use for this
                                                					 mailbox created. |
| SendReadReceipts | Integer | Read/Write | A flag indicating whether the mailbox
                                                					 created with this subscriber allows the system to send read receipts on its
                                                					 behalf. Values can be: 0: Disable 1: Enable |
| SendQuota | Integer | Read/Write | The mailbox size (in bytes) send limit.
                                                					 (2048 MB) Values can be: 1: The quota is
                                                         						  unlimited. 2: The default
                                                         						  system quota is assigned. |
| WarningQuota | Integer | Read/Write | The mailbox size (in bytes) warning limit.
                                                					 (2048 MB) Values can be: 1: The quota is
                                                         						  unlimited. 2: The default
                                                         						  system quota is assigned. |
| ReceiveQuota | Integer | Read/Write | The mailbox size (in bytes) receive limit.
                                                					 (2048 MB) Values can be: 1: The quota is
                                                         						  unlimited. 2: The default
                                                         						  system quota is assigned. |
| MailboxDn | String(36) | Read-Only | The distinguished name of the mailbox. |
| SynchScheduleObjectId | String(36) | Read-Only | The unique identifiers of the Schedule
                                                					 object to use for synchronization Calendar information from groupware (such as
                                                					 Exchange). |
| IsSetForVmEnrollment | Boolean | Read-Only | Temporary placeholder until IsVmEnrolled
                                                					 can be phased out. |
| SendBroadcastMsg | Boolean | Read/Write | A flag indicating whether the subscriber
                                                					 may send broadcast messages. Values can be: False: Cannot
                                                         						  send broadcast messages. True: Can send
                                                         						  broadcast messages. Default value: False |
| UpdateBroadcastMsg | Boolean | Read/Write | A flag indicating whether the subscriber
                                                					 has the ability to update broadcast messages that are active or will be active
                                                					 in the future. Values can be: False: Cannot
                                                         						  update broadcast messages. True: Can update
                                                         						  broadcast messages. Default value: False |
| ConversationVUI | Boolean | Read/Write | The VUI conversation assigned to the
                                                					 subscriber. |
| SpeechCompleteTimeout | Integer | Read-Only | Specifies the required length of silence
                                                					 (in milliseconds) following user speech before the recognizer finalizes a
                                                					 result. |
| SpeechIncompleteTimeout | Integer | Read-Only | Specifies the required length of silence
                                                					 (in milliseconds) from when the speech prior to the silence matches an active
                                                					 grammar. |
| UseVui | Boolean | Read/Write | A flag indicating whether the speech
                                                					 recognition conversation is the default conversation for the subscriber. Values can be: False: Speech
                                                         						  recognition conversation is not default conversation for the subscriber. True: Speech
                                                         						  recognition conversation is the default conversation for the subscriber. Default value: False |
| SkipPasswordForKnownDevice | Boolean | Read/Write | A flag indicating whether the subscriber
                                                					 will be asked for his/her PIN when attempting to sign-in from a known device. Default value: False |
| JumpToMessagesOnLogin | Boolean | Read/Write | A flag indicating whether the subscriber
                                                					 conversation jumps directly to the first message in the message stack after
                                                					 subscriber sign-in. Values can be: False:
                                                         						  Subscriber conversation does not jump directly to first message in the message
                                                         						  stack after subscriber sign-in. True: Subscriber
                                                         						  conversation jumps directly to the first message in the message stack after
                                                         						  subscriber sign-in. Default value: True |
| EnableMessageLocator | Boolean | Read/Write | A flag indicating whether the message
                                                					 locator feature is enabled for the subscriber. Values can be: False: Message
                                                         						  locator feature is disabled for subscriber. True: Message
                                                         						  locator feature is enabled for subscriber. Default value: False |
| MessageAgingPolicyObjectId | String(36) | Read-Only | The unique identifier of the
                                                					 MessageAgingPolicy object that applies to the mailbox created for a new
                                                					 subscriber created with this template. |
| AssistantRowsPerPage | Integer | Read-Only | This controls the number of entries to
                                                					 display per page for all tables in the Unity Assistant, e.g. the Private List
                                                					 Members table. |
| InboxMessagesPerPage | Integer | Read-Only | The number of messages Unity Inbox displays
                                                					 in a page. |
| InboxAutoRefresh | Integer | Read-Only | The rate (in minutes) at which Unity Inbox
                                                					 performs a refresh. |
| InboxAutoResolveMessageRecipients | Integer | Read-Only | A flag indicating whether Cisco Unity
                                                					 Connection automatically resolves a recipient address entered in the To, Cc or
                                                					 Bcc fields to a subscriber or distribution list. Known as the "AutoResolve"
                                                					 feature. |
| PcaAddressBookRowsPerPage | Integer | Read-Only | Controls the number of matching entries the
                                                					 Address Book displays per page, when a search is performed. The Address Book is
                                                					 used across multiple PCA applications and so this setting applies globally. |
| PcaHomePage | String(36) | Read-Only | The Home Page is the first page that is
                                                					 displayed after logging in to the PCA. |
| EnableTts | Boolean | Read/Write | A flag indicating whether TTS is enabled
                                                					 for the subscriber. Only relevant if TTS enabled in User's COS also. Values can be: False: TTS is
                                                         						  disabled for the subscriber. True: TTS is
                                                         						  enabled for the subscriber Default value: True |
| ConfirmationConfidenceThreshold | Integer | Read-Only | Voice Recognition Confirmation Confidence
                                                					 Threshold. |
| AnnounceUpcomingMeetings | Integer | Read-Only | The amount ahead of time, in minutes, that
                                                					 Connection will warn the subscriber of upcoming meetings when the subscriber
                                                					 calls into the system. |
| SpeechConfidenceThreshold | Integer | Read-Only | When the engine matches a spoken phrase, it
                                                					 associates a confidence level with that conclusion. This parameter determines
                                                					 what confidence level should be considered a successful match. A higher value
                                                					 means the engine is will report fewer successful matches, but it will be more
                                                					 confident in the matches that it reports. Range: 0-100. |
| SpeechSpeedVsAccuracy | Integer | Read-Only | Sets accuracy and performance of speech. |
| SpeechSensitivity | Integer | Read-Only | A variable level of sound sensitivity that
                                                					 enables the speech engine to filter out background noise and not mistake it for
                                                					 speech. |
| EnableVisualMessageLocator | Boolean | Read/Write | A flag indicating whether the visual
                                                					 message locator feature is enabled for the subscriber. The visual message
                                                					 locator feature presents a list of messages on the subscriber's IP phone
                                                					 display for the subscriber to select from visually. Values can be: False: Visual
                                                         						  message locator feature disabled for subscriber. True: Visual
                                                         						  message locator feature enabled for subscriber. Default value: False |
| ContinuousAddMode | Boolean | Read/Write | A flag indicating whether when addressing,
                                                					 after entering one recipient name, whether the subscriber is asked to enter
                                                					 another name or assume the subscriber is finished adding names and is ready to
                                                					 move on to recording the message or applying message options. Values can be: False: Unity
                                                         						  Connection prompts subscribers to press 1 to add more recipients. True: Unity
                                                         						  Connection does not prompt subscribers to press 1 to add more recipients.
                                                         						  Instead, subscribers continue entering recipient names or extensions (as
                                                         						  applicable) until they indicate that they have completed addressing. Default value: False |
| NameConfirmation | Boolean | Read/Write | Whether voice name of the user or
                                                					 distribution list is played or not. Values can be: False: No voice
                                                         						  name played. True: Voice name
                                                         						  of subscriber or DL is played. Default value: False |
| CommandDigitTimeout | Integer(4) | Read-Only | The amount of time (in milliseconds)
                                                					 between digits on a multiple digit menu command entry (i.e. different than the
                                                					 inter digit timeout that is used for strings of digits such as extensions and
                                                					 transfer strings). Default value: 1500 Range: 250-5000 |
| SaveMessageOnHangup | Boolean | Read/Write | A flag indicating when hanging up while
                                                					 listening to a new message, whether the message is marked new again or is
                                                					 marked read. Values can be: False: Message
                                                         						  is marked new again. True: Message is
                                                         						  marked read. Default value: False |
| SkipForwardTime | Integer(4) | Read-Only | Indicates the amount of time (in
                                                					 milliseconds) to jump forward when skipping ahead in a voice or TTS message
                                                					 using either DTMF or voice commands while reviewing messages. Default Value: 5000 Range: 1000-60000 |
| SkipReverseTime | Integer(4) | Read-Only | Indicates the amount of time (in
                                                					 milliseconds) to jump backward when skipping in reverse in a voice or TTS
                                                					 message using either DTMF or voice commands while reviewing messages. Default Value: 5000 Range: 1000-60000 |
| UseShortPollForCache | Boolean | Read-Only | A flag indicating whether the user's
                                                					 polling cycle for retrieving calendar information will be the shorter "power
                                                					 user" polling cycle. Values can be: False: The
                                                         						  subscriber's polling cycle is determined by the system default polling cycle.
                                                         						  (default value) (System configuration setting "Normal Calendar Caching Poll
                                                         						  Interval"). True: The
                                                         						  shorter "power user" polling cycle is used. (System configuration setting
                                                         						  "Short Calendar Caching Poll Interval"). Default value: False |
| SearchByExtensionSearchSpaceObjectId | String(36) | Read-Only | The unique identifier of the SearchSpace
                                                					 which is used to limit the visibility to dialable/addressable objects when
                                                					 searching by extension (dial string). |
| SearchByNameSearchSpaceObjectId | String(36) | Read-Only | The unique identifier of the SearchSpace
                                                					 which is used to limit the visibility to dilatable/addressable objects when
                                                					 searching by name (character string). |
| PartitionObjectId | String(36) | Read/Write | The unique identifier of the Partition to
                                                					 which a subscriber's DtmfAccessId created with this template will be assigned. |
| UseDynamicNameSearchWeight | Boolean | Read-Only | Use dynamic name search weight. When this
                                                					 user addresses objects, the name search weight for those objects will
                                                					 automatically be incremented. |
| LdapCcmPkid | String(36) | Read/Write | The pkid of associated end user in the
                                                					 sleeping SeaDragon database. |
| LdapType | Integer | Read-Only | The LDAP configuration information for the
                                                					 user. |
| FaxServerObjectId | String(36) | Read-Only | The unique identifier of the FaxServer
                                                					 object for the subscriber. |
| LdapCcmUserId | String(36) | Read-Only | The userid of associated end user in the
                                                					 sleeping SeaDragon database. |
| XferString | String(36) | Read-Only | Alternate transfer option. |
| EnableMessageBookmark | Boolean | Read/Write | A flag indicating whether Message Bookmark
                                                					 is enabled for the subscriber. Values can be: False: Message
                                                         						  Bookmark feature is disabled for subscriber. True: Message
                                                         						  Bookmark feature is enabled for subscriber. Default value: False |
| SayTotalDraftMsg | Boolean | Read/Write | A flag indicating whether Cisco Unity
                                                					 Connection announces the total number of draft messages in the subscriber
                                                					 mailbox. Values can be: False: Do not
                                                         						  announce total number of draft messages. True: Announce
                                                         						  the total number of draft messages in the subscriber mailbox. Default value: False |
| EnableSaveDraft | Boolean | Read/Write | A flag indicating whether the save draft
                                                					 message feature is enabled for the subscriber. Values can be: False: Do not
                                                         						  save draft messages. True: Save draft
                                                         						  messages. Default value: False |
| RetainUrgentMessageFlag | Boolean | Read/Write | Urgent message flag on a message is
                                                					 retained for both reply and forward message actions. Default value: False |
| SayMessageLength | Boolean | Read/Write | A flag indicating whether Cisco Unity
                                                					 Connection announces the length of each message during message playback. Default value: False |
| CreateSmtpProxyFromCorp | Boolean | Read/Write | SMTP proxy address matching the corporate
                                                					 e-mail address created for user. |
| AutoAdvanceMsgs | Boolean | Read-Only | A flag indicating that the conversation
                                                					 will, during playback, advance to the next message in the playback stack
                                                					 automatically after it is done playing the after message menu. Values can be: False: Do not
                                                         						  automatically skip to the next message after playing the after message menu
                                                         						  once. True: Do
                                                         						  advanced automatically to the next message after playing the after message menu
                                                         						  once. Default value: False |
| SaySenderAfter | Boolean | Read-Only | This flag works exactly the same as the
                                                					 SaySender flag on a user, except the conversation plays the sender in the
                                                					 message footer. Default value: False |
| SaySenderExtensionAfter | Boolean | Read-Only | This flag works exactly the same as the
                                                					 SaySenderExtension flag on a user, except the conversation plays the sender's
                                                					 extension in the message footer. Default value: False |
| SayMsgNumberAfter | Boolean | Read-Only | This flag works exactly the same as the
                                                					 SayMsgNumber flag on a user, except the conversation plays the message number
                                                					 in the message footer. Default value: False |
| SayAniAfter | Boolean | Read-Only | This flag works exactly the same as the
                                                					 SayAni flag on a user, except the conversation plays the ani in the message
                                                					 footer. Default value: False |
| SayMessageLengthAfter | Boolean | Read-Only | This flag works exactly the same as the
                                                					 SayMessageLength flag on a user, except the conversation plays the message
                                                					 length in the message footer. Default value: False |