---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-api-user-transfer-rule-html-d5b06206ef
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_cupi-api-user-transfer-rule.html
retrieved_at: 2026-08-17T03:48:42.354726+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Transfer Rules

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Transfer Rules

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- User Transfer Rules

## Transfer Rule
                        	 API

First get the call handler URI of
                              		  a particular user: GET

```
https://<Connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>
```

From call handler URI get for transfer options: GET

```
https://<Connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/transferoptions
```

For alternate transfer rule: GET

```
https://<Connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/transferoptions/Alternate
```

For closed transfer rule: GET

```
https://<Connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/transferoptions/Off%20Hours
```

For Standard transfer rule: GET

```
https://<Connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/transferoptions/Standard
```

### Listing All
                           	 Transfer Rules

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/transferoptions
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
<TransferOptions total="2">
  <TransferOption>
    <URI>/vmrest/callhandlerprimarytemplates/939d4d12-cec8-4fee-ae47-fbf0cf20c33e/transferoptions/Off%20Hours</URI>
    <CallHandlerObjectId>939d4d12-cec8-4fee-ae47-fbf0cf20c33e</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/939d4d12-cec8-4fee-ae47-fbf0cf20c33e</CallhandlerURI>
    <TransferOptionType>Off Hours</TransferOptionType>
    <Action>0</Action>
    <RnaAction>1</RnaAction>
    <TransferAnnounce>false</TransferAnnounce>
    <TransferConfirm>false</TransferConfirm>
    <TransferDtDetect>false</TransferDtDetect>
    <TransferHoldingMode>0</TransferHoldingMode>
    <TransferIntroduce>false</TransferIntroduce>
    <TransferRings>4</TransferRings>
    <TransferScreening>false</TransferScreening>
    <TransferType>0</TransferType>
    <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/ec1e2636-fc14-44fc-8cda-d6c1a3d61150</PhoneSystemURI>
    <UsePrimaryExtension>true</UsePrimaryExtension>
    <PlayTransferPrompt>true</PlayTransferPrompt>
    <PersonalCallTransfer>false</PersonalCallTransfer>
    <Enabled>true</Enabled>
   </TransferOption>
   <TransferOption>
    <URI>/vmrest/handlers/callhandlers/939d4d12-cec8-4fee-ae47-fbf0cf20c33e/transferoptions/Standard</URI>
    <CallHandlerObjectId>939d4d12-cec8-4fee-ae47-fbf0cf20c33e</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/939d4d12-cec8-4fee-ae47-fbf0cf20c33e</CallhandlerURI>
    <TransferOptionType>Standard</TransferOptionType>
    <Action>0</Action>
    <RnaAction>1</RnaAction>
    <TransferAnnounce>false</TransferAnnounce>
    <TransferConfirm>false</TransferConfirm>
    <TransferDtDetect>false</TransferDtDetect>
    <TransferHoldingMode>0</TransferHoldingMode>
    <TransferIntroduce>false</TransferIntroduce>
    <TransferRings>4</TransferRings>
    <TransferScreening>false</TransferScreening>
    <TransferType>0</TransferType>
    <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/ec1e2636-fc14-44fc-8cda-d6c1a3d61150</PhoneSystemURI>
    <UsePrimaryExtension>true</UsePrimaryExtension>
    <PlayTransferPrompt>true</PlayTransferPrompt>
    <PersonalCallTransfer>false</PersonalCallTransfer>
    <Enabled>true</Enabled>
   </TransferOption>
  </TransferOptions>
```

```
Response Code: 200
```

### Viewing the
                           	 Alternate Transfer Rule

The following is an example of
                                 		  the GET request that lists the details of alternate transfer rule:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/transferoptions/Alternate
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
<TransferOption>
  <URI>/vmrest/callhandlerprimarytemplates/45e0a6f4-43c4-472a-8ffb-f6124aa549d0/transferoptions/Alternate</URI>
  <CallHandlerObjectId>45e0a6f4-43c4-472a-8ffb-f6124aa549d0</CallHandlerObjectId>
  <CallhandlerURI>/vmrest/handlers/callhandlers/45e0a6f4-43c4-472a-8ffb-f6124aa549d0</CallhandlerURI>
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
GET https://<connection-server>/vmrest/handlers/<callhandlerObjectId>/transferoptions/Alternate
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
{
  "URI":"/vmrest/handlers/callhandlers/43bb6590-e9e3-43ca-972e-e3e158a96126/transferoptions/Alternate"
  "CallHandlerObjectId":"43bb6590-e9e3-43ca-972e-e3e158a96126"
  "CallhandlerURI":"/vmrest/handlers/callhandlers/43bb6590-e9e3-43ca-972e-e3e158a96126"
  "TransferOptionType":"Alternate"
  "Action":"0"
  "RnaAction":"1"
  "TimeExpires":"1972-01-01 00:00:00.0"
  "TransferAnnounce":"false"
  "TransferConfirm":"false"
  "TransferDtDetect":"false"
  "TransferHoldingMode":"0"
  "TransferIntroduce":"false"
  "TransferRings":"4"
  "TransferScreening":"false"
  "TransferType":"0"
  "MediaSwitchObjectId":"e912b134-1bd0-45f9-baae-9f1e096ae3b9"
  "PhoneSystemURI":"/vmrest/phonesystems/e912b134-1bd0-45f9-baae-9f1e096ae3b9"
  "UsePrimaryExtension":"true"
  "PlayTransferPrompt":"true"
  "PersonalCallTransfer":"false"
  "Enabled":"false"
}
```

```
Response Code: 200
```

### Updating Transfer
                           	 Option

The following is an example of
                                 		  the PUT request that updates the transfer option:

```
PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/transferoptions/Alternate
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
PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/transferoptions/Alternate
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

```
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

### Explanation of
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

| https://<Connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId> |
|---|

| https://<Connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/transferoptions |
|---|

| https://<Connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/transferoptions/Alternate |
|---|

| https://<Connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/transferoptions/Off%20Hours |
|---|

| https://<Connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/transferoptions/Standard |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/transferoptions |
|---|

| <TransferOptions total="2">
  <TransferOption>
    <URI>/vmrest/callhandlerprimarytemplates/939d4d12-cec8-4fee-ae47-fbf0cf20c33e/transferoptions/Off%20Hours</URI>
    <CallHandlerObjectId>939d4d12-cec8-4fee-ae47-fbf0cf20c33e</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/939d4d12-cec8-4fee-ae47-fbf0cf20c33e</CallhandlerURI>
    <TransferOptionType>Off Hours</TransferOptionType>
    <Action>0</Action>
    <RnaAction>1</RnaAction>
    <TransferAnnounce>false</TransferAnnounce>
    <TransferConfirm>false</TransferConfirm>
    <TransferDtDetect>false</TransferDtDetect>
    <TransferHoldingMode>0</TransferHoldingMode>
    <TransferIntroduce>false</TransferIntroduce>
    <TransferRings>4</TransferRings>
    <TransferScreening>false</TransferScreening>
    <TransferType>0</TransferType>
    <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/ec1e2636-fc14-44fc-8cda-d6c1a3d61150</PhoneSystemURI>
    <UsePrimaryExtension>true</UsePrimaryExtension>
    <PlayTransferPrompt>true</PlayTransferPrompt>
    <PersonalCallTransfer>false</PersonalCallTransfer>
    <Enabled>true</Enabled>
   </TransferOption>
   <TransferOption>
    <URI>/vmrest/handlers/callhandlers/939d4d12-cec8-4fee-ae47-fbf0cf20c33e/transferoptions/Standard</URI>
    <CallHandlerObjectId>939d4d12-cec8-4fee-ae47-fbf0cf20c33e</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/939d4d12-cec8-4fee-ae47-fbf0cf20c33e</CallhandlerURI>
    <TransferOptionType>Standard</TransferOptionType>
    <Action>0</Action>
    <RnaAction>1</RnaAction>
    <TransferAnnounce>false</TransferAnnounce>
    <TransferConfirm>false</TransferConfirm>
    <TransferDtDetect>false</TransferDtDetect>
    <TransferHoldingMode>0</TransferHoldingMode>
    <TransferIntroduce>false</TransferIntroduce>
    <TransferRings>4</TransferRings>
    <TransferScreening>false</TransferScreening>
    <TransferType>0</TransferType>
    <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/ec1e2636-fc14-44fc-8cda-d6c1a3d61150</PhoneSystemURI>
    <UsePrimaryExtension>true</UsePrimaryExtension>
    <PlayTransferPrompt>true</PlayTransferPrompt>
    <PersonalCallTransfer>false</PersonalCallTransfer>
    <Enabled>true</Enabled>
   </TransferOption>
  </TransferOptions> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/transferoptions/Alternate |
|---|

| <TransferOption>
  <URI>/vmrest/callhandlerprimarytemplates/45e0a6f4-43c4-472a-8ffb-f6124aa549d0/transferoptions/Alternate</URI>
  <CallHandlerObjectId>45e0a6f4-43c4-472a-8ffb-f6124aa549d0</CallHandlerObjectId>
  <CallhandlerURI>/vmrest/handlers/callhandlers/45e0a6f4-43c4-472a-8ffb-f6124aa549d0</CallhandlerURI>
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

| GET https://<connection-server>/vmrest/handlers/<callhandlerObjectId>/transferoptions/Alternate
Accept: application/json
Connection: keep-alive |
|---|

| {
  "URI":"/vmrest/handlers/callhandlers/43bb6590-e9e3-43ca-972e-e3e158a96126/transferoptions/Alternate"
  "CallHandlerObjectId":"43bb6590-e9e3-43ca-972e-e3e158a96126"
  "CallhandlerURI":"/vmrest/handlers/callhandlers/43bb6590-e9e3-43ca-972e-e3e158a96126"
  "TransferOptionType":"Alternate"
  "Action":"0"
  "RnaAction":"1"
  "TimeExpires":"1972-01-01 00:00:00.0"
  "TransferAnnounce":"false"
  "TransferConfirm":"false"
  "TransferDtDetect":"false"
  "TransferHoldingMode":"0"
  "TransferIntroduce":"false"
  "TransferRings":"4"
  "TransferScreening":"false"
  "TransferType":"0"
  "MediaSwitchObjectId":"e912b134-1bd0-45f9-baae-9f1e096ae3b9"
  "PhoneSystemURI":"/vmrest/phonesystems/e912b134-1bd0-45f9-baae-9f1e096ae3b9"
  "UsePrimaryExtension":"true"
  "PlayTransferPrompt":"true"
  "PersonalCallTransfer":"false"
  "Enabled":"false"
} |
|---|

| Response Code: 200 |
|---|

| PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/transferoptions/Alternate |
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

| PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/transferoptions/Alternate
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| {
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