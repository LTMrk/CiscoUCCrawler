---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-for-end-user-b-cupi-api-for-end-user-b-cupi-api-20e8812ce0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API_for_End_User/b_CUPI_API_for_End_User/b_CUPI_API_for_End_User_chapter_011000.html
retrieved_at: 2026-08-21T08:05:58.068575+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

Updated: January 24, 2019

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- TransferOptions API

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- TransferOptions API

# Cisco Unity Connection Provisioning Interface (CUPI) API -- TransferOptions API

## Cisco Unity Connection Provisioning Interface (CUPI) API -- TransferOptions API

## Transfer Options API

Every user with a mailbox has an associated call handler, and thus transfer options. Transfer Options are also referred to
                           as Transfer Rules. Every user and call handler has three types of transfer options:

Standard

Off Hours

Alternate

TimeExpires is the field that determines if a transfer option is enabled or disabled. To enable a transfer option, TimeExpires must be
                           set to a future date, which is the date on which the transfer option will expire (be disabled). To disable a transfer option,
                           simply set TimeExpires to a date in the past. Also, if TimeExpires is set to null that means it is enabled indefinitely, however,
                           the currently CUPI offers no ability to set this field to null. TimeExpires is always treated as GMT. Any required timezone
                           conversion is the responsibility of the client. Action is the field that determines if the transfer option will transfer calls
                           to an extension or directly to the greetings. The Action field is a custom type. A value of 0 denotes that the call will be
                           sent directly to the greetings. A value of 1 denotes that the call will be transferred to an extension.

Several settings are specific to how the transfer option should transfer the call (assuming that the Action is set to 1):

TransferType: Determines whether the transfer will be released (a value of 0) or supervised (a value of 1).

Extension: Indicates the extension that the call will transfer to.

TransferRings: is the number of times Connection will ring the extension before it considers the call a ring-no-answer (RNA), and pulls
                                 the call back to play the greeting. This value is only used when the TransferType is set to 1 (a supervised transfer).

UsePrimaryExtension is a boolean that is a bit of an oddity. When the value is set to true, the Extension is set to the primary extension of
                           the user. However, note the following caveat when using this field: if UsePrimaryExtension is set to true and the Extension
                           field is set to a value in the same PUT, an error will be thrown. Because setting UsePrimaryExtension to true causes the Extension
                           field to be set to a specific value, you cannot also explicitly set the Extension field in the same PUT; one or the other
                           can occur, but not both. An error will also be thrown if UsePrimaryExtension is set to false and no value is given for the
                           Extension field in the same PUT. In other words, if you set UsePrimaryExtension to false, you must provide a new Extension
                           in the same PUT.

PersonalCallTransfer is a boolean that determines whether personal call transfer rules will be used instead of the basic transfer rules. If PersonalCallTransfer
                           is set to true, then instead of using any of the settings of this transfer rule, the call will be sent to the personal call
                           transfer rules of the user to be acted on. If PersonalCallTransfer is set to false, then the basic transfer rule is used.
                           If you are using personal call transfer rules, set this to true; otherwise, leave it set to false.

### Listing

The settings on each transfer option can be read by the following GET command:

```
GET /vmrest/user/transferoptions/{transfer option type}
```

Which would produce a response similar to the following:

```
200
OK
<?xml version="1.0" encoding="UTF-8"?>
<TransferOption>
  <TransferOptionType>{transfer option type}</TransferOptionType>
  <Action>1</Action>
  <Extension>5555</Extension>
  <TimeExpires>1972-01-01 00:00:00.0</TimeExpires>
  <TransferRings>4</TransferRings>
  <TransferType>0</TransferType>
  <UsePrimaryExtension>true</UsePrimaryExtension>
  <PersonalCallTransfer>false</PersonalCallTransfer>
</TransferOption>
```

Every user and call handler has three transfer options:

Standard

Off Hours

Alternate

Each transfer option can be accessed through a GET request:

```
GET /vmrest/user/transferoptions/Standard
GET /vmrest/user/transferoptions/Off%20Hours
GET /vmrest/user/transferoptions/Alternate
```

TimeExpires is the field that determines if a transfer option is enabled or disabled. To enable a transfer option, TimeExpires must be
                                 set to a future date, which is the date that the transfer option will expire (be disabled). To disable a transfer option,
                                 simply set TimeExpires to a date in the past. Also, if TimeExpires is set to null that means it is enabled indefinitely (however,
                                 note that currently CUPI offers no ability to set this field to null).

TimeExpires is always treated as GMT. Any required time zone conversion is the responsibility of the client.

Action is the field that determines if the transfer option will transfer calls to an extension or directly to the greetings. The
                                 Action field is a custom type. A value of 0 denotes that the call will be sent directly to the greetings. A value of 1 denotes
                                 that the call will be transferred to an extension.

Several settings are specific to how the transfer option should transfer the call (assuming that the Action is set to 1):

TransferType

Extension

TransferRings

TransferType determines whether the transfer will be released (a value of 0) or supervised (a value of 1).

Extension indicates the extension that the call will transfer to.

TransferRings is the number of times Connection will ring the extension before it considers the call a ring-no-answer (RNA), and pulls
                                 the call back to play the greeting. This value is only used when the TransferType is set to 1 (a supervised transfer).

UsePrimaryExtension is a boolean that is a bit of an oddity. When the value is set to true, the Extension is set to the primary extension of
                                 the user. However, note the following caveat when using this field: if UsePrimaryExtension is set to true and the Extension
                                 field is set to a value in the same PUT, an error will be thrown. Because setting UsePrimaryExtension to true causes the Extension
                                 field to be set to a specific value, you cannot also explicitly set the Extension field in the same PUT; one or the other
                                 can occur, but not both. An error will also be thrown if UsePrimaryExtension is set to false and no value is given for the
                                 Extension field in the same PUT. In other words, if you set UsePrimaryExtension to false, you must provide a new Extension
                                 in the same PUT.

PersonalCallTransfer is a boolean that determines whether personal call transfer rules will be used instead of the basic transfer rules. If PersonalCallTransfer
                                 is set to true, then instead of using any of the settings of this transfer rule, the call will be sent to the personal call
                                 transfer rules of the user to be acted on. If PersonalCallTransfer is set to false, then the basic transfer rule is used.
                                 If you are using personal call transfer rules, set this to true; otherwise, leave it set to false. It's that simple.

### Updating

To enable the Alternate transfer option until March 9, 2020, you would use the following PUT request:

```
PUT https://fmstest4.cisco.com/vmrest/user/transferoptions/Alternate

<?xml version="1.0" encoding="UTF-8"?>
<TransferOption>
  <TimeExpires>2020-03-09 00:00:00.0</TimeExpires>
</TransferOption>
```

To disable the Alternate transfer option you would do a PUT request with the TimeExpires field set to a date in the past as
                                 in this example:

```
PUT https://fmstest4.cisco.com/vmrest/user/transferoptions/Alternate

<?xml version="1.0" encoding="UTF-8"?>
<TransferOption>
  <TimeExpires>1976-03-09 00:00:00.0</TimeExpires>
</TransferOption>
```

### Disable the Alternate Transfer Option

To disable the alternate transfer option, use the PUT request with the TimeExpires field set to a date in the past as in this
                                 example:

```
PUT https://<connection-server>/vmrest/user/transferoptions/Alternate 
<TransferOption>
  <TimeExpires>1976-03-09 00:00:00.0</TimeExpires>
</TransferOption>
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                 by you:

```
Response Code: 204
```

Call Holding User access to the call holding setting is controlled by the user's class of service. The transfer option setting
                                 that controls call holding is TransferHoldingMode. It is a custom type that can be set to not hold (a value of 0), always
                                 put the call on hold when the extension is busy (a value of 1), or ask the caller if they wish to hold (a value of 2). Holding
                                 is applicable only when TransferType is set to supervised (a value of 1). For example, if you wanted to set the alternate
                                 transfer option to always put the call on hold you would make the following PUT request:

```
PUT https://<connection-server>/vmrest/user/transferoptions/Alternate 
<TransferOption>
  <TransferHoldingMode>1</TransferHoldingMode>
</TransferOption>
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                 by you:

```
Response Code: 204
```

### Call Screening

User access to the call screening options is controlled by the user's class of service. There are four settings on a transfer
                                 option that control screening. They are all booleans. The various screening options are applicable only when TransferType
                                 is set to supervised (a value of 1).

TransferAnnounce indicates whether the transfer should be announced to the user when they answer the phone, via a simple pre-recorded
                                       prompt.

TransferConfirm indicates whether the user is prompted to accept the transfer or not. If the user does not accept the transfer,
                                       the caller is taken to the user's greeting.

TransferIntroduce indicates whether the user hears for whom the transfer was intended when he or she answers the phone.

TransferScreening indicates whether the caller is asked to speak his or her name before being transferred. The name spoken
                                       is then played back to the user when he or she answers the phone.

For example, if you wanted to turn on all of the screening options for the alternate transfer option you would make the following
                                 PUT request:

```
PUT https://<connection-server>/vmrest/user/transferoptions/Alternate 
Request Body:
<TransferOption>
  <TransferAnnounce>true</TransferAnnounce>
  <TransferConfirm>true</TransferConfirm>
  <TransferIntroduce>true</TransferIntroduce>
  <TransferScreening>true</TransferScreening>
</TransferOption>
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                 by you:

```
Response Code: 204
```

| GET /vmrest/user/transferoptions/{transfer option type} |
|---|

| 200
OK
<?xml version="1.0" encoding="UTF-8"?>
<TransferOption>
  <TransferOptionType>{transfer option type}</TransferOptionType>
  <Action>1</Action>
  <Extension>5555</Extension>
  <TimeExpires>1972-01-01 00:00:00.0</TimeExpires>
  <TransferRings>4</TransferRings>
  <TransferType>0</TransferType>
  <UsePrimaryExtension>true</UsePrimaryExtension>
  <PersonalCallTransfer>false</PersonalCallTransfer>
</TransferOption> |
|---|

| GET /vmrest/user/transferoptions/Standard
GET /vmrest/user/transferoptions/Off%20Hours
GET /vmrest/user/transferoptions/Alternate |
|---|

| PUT https://fmstest4.cisco.com/vmrest/user/transferoptions/Alternate

<?xml version="1.0" encoding="UTF-8"?>
<TransferOption>
  <TimeExpires>2020-03-09 00:00:00.0</TimeExpires>
</TransferOption> |
|---|

| PUT https://fmstest4.cisco.com/vmrest/user/transferoptions/Alternate

<?xml version="1.0" encoding="UTF-8"?>
<TransferOption>
  <TimeExpires>1976-03-09 00:00:00.0</TimeExpires>
</TransferOption> |
|---|