---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-api-user-greetings-html-b238a837ab
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m-cupi_api_user-greetings.html
retrieved_at: 2026-08-17T03:47:52.841883+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Greetings

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Greetings

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- User Greetings

Links to Other API pages: Cisco_Unity_Connection_APIs

## Greetings
                        	 API

The following URI can be used to
                           		view the user template object ID:

```
GET https://<connection-server>/vmrest/users/<user-objectid>
```

From the above URI, get the call handler object ID:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>
```

The following URI can be used to view the greetings:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings
```

The following URI can be used to view the alternate greeting:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Alternate
```

The following URI can be used to view the busy greeting:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Busy
```

The following URI can be used to view the error greeting:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Error
```

The following URI can be used to view the closed greeting:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Off%20Hours
```

The following URI can be used to view the standard greeting:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Standard
```

The following URI can be used to view the holiday greeting:

```
GET https://<connection-server>/vmrest/callhandlers/<CallhandlerObjectId>/greetings/Holiday
```

### Updating Fields of
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

#### Explanation of
                              	 Data Fields

Values can be:

- false: Caller
                                                         						  input enabled during greeting

- true: Caller
                                                         						  input ignored during greeting

Default Value: false

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

Greeting Type

- 1.Alternate -
                                                         						  can be used for a variety of special situations, such as vacations, leave of
                                                         						  absence, or a holiday. An alternate greeting overrides all other greetings.

- 2.Busy - plays
                                                         						  when the extension is busy. A busy greeting overrides the standard, off hours,
                                                         						  and internal greetings.

- 3.Error - plays
                                                         						  when a caller attempts to dial an extension that does not exist on the system
                                                         						  during a greeting.

- 4.Internal -
                                                         						  plays to internal callers only. An internal greeting overrides the standard and
                                                         						  off hours greetings.

- 5.Off hours -
                                                         						  plays during the closed (nonbusiness) hours defined for the active schedule. An
                                                         						  off hours greeting overrides the standard greeting, and thus limits the
                                                         						  standard greeting to the open hours defined for the active schedule.

- 6.Standard -
                                                         						  plays at all times unless overridden by another greeting. You cannot disable
                                                         						  the standard greeting.

- 7.Holiday -
                                                         						  plays when holiday schedule is encountered unless overridden by an alternate
                                                         						  greeting.

| GET https://<connection-server>/vmrest/users/<user-objectid> |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId> |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Alternate |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Busy |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Error |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Off%20Hours |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Standard |
|---|

| GET https://<connection-server>/vmrest/callhandlers/<CallhandlerObjectId>/greetings/Holiday |
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

| Parameter | Data Type | Operations | Comments |
|---|---|---|---|
| ObjectId | String(36) | Read Only | Unique identifier of the directory entry. |
| CallHandlerObjectId | String(36) | Read Only | The unique identifier of the call handler
                                                					 object to which this greeting rule belongs. |
| IgnoreDigits | Boolean | Read/Write | A flag indicating whether Cisco Unity
                                                					 Connection takes action in response to touchtone keys pressed by callers during
                                                					 the greeting. Values can be: false: Caller
                                                         						  input enabled during greeting true: Caller
                                                         						  input ignored during greeting Default Value: false |
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
| TimeExpires | Data Time(8) | Read/Write | The date and time when the greeting rule
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
| AfterGreetingTargetConverstion | String(64) | Read/Write | The name of the conversation to which the
                                                					 caller is routed. |
| AfterGreetingTargetHandlerObjectId | String(36) | Read/Write | The unique identifier of the specific
                                                					 object to send along to the target conversation. |
| PlayRecordMessagePrompt | Integer(2) | Read/Write | A flag indicating whether the "Record your
                                                					 message at the tone…" prompt prior to recording a message. Values can be: 0: System will
                                                         						  not play the "Record your message at the tone…" prompt prior to recording a
                                                         						  message. 1: System will
                                                         						  play the "Record your message at the tone…" prompt prior to recording a
                                                         						  message. Default Value: 1 |
| EnableTransfer | Boolean | Read/Write | A flag indicating when an extension is
                                                					 dialed at the greeting and the extension is not available whether to transfer
                                                					 to another extension. Default value: 0 Values can be: 0: User cannot
                                                         						  be transferred to another extension. 1: User can "be
                                                         						  transferred to another extension." Greeting Type 1.Alternate -
                                                         						  can be used for a variety of special situations, such as vacations, leave of
                                                         						  absence, or a holiday. An alternate greeting overrides all other greetings. 2.Busy - plays
                                                         						  when the extension is busy. A busy greeting overrides the standard, off hours,
                                                         						  and internal greetings. 3.Error - plays
                                                         						  when a caller attempts to dial an extension that does not exist on the system
                                                         						  during a greeting. 4.Internal -
                                                         						  plays to internal callers only. An internal greeting overrides the standard and
                                                         						  off hours greetings. 5.Off hours -
                                                         						  plays during the closed (nonbusiness) hours defined for the active schedule. An
                                                         						  off hours greeting overrides the standard greeting, and thus limits the
                                                         						  standard greeting to the open hours defined for the active schedule. 6.Standard -
                                                         						  plays at all times unless overridden by another greeting. You cannot disable
                                                         						  the standard greeting. 7.Holiday -
                                                         						  plays when holiday schedule is encountered unless overridden by an alternate
                                                         						  greeting. |