---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7800-english-ag-pa2d-b-7800-mpp-ag-new-pa2d-b-7800-mpp-ag-new-cha-255b50599e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7800/english/AG/pa2d_b_7800_mpp_ag_new/pa2d_b_7800_mpp_ag_new_chapter_010100.html
retrieved_at: 2026-08-21T23:21:41.319467+00:00
---

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide for Release 11.3(1) and Later

# Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide for Release 11.3(1) and Later

Updated: November 21, 2019

Chapter: Voicemail Configuration

## Chapter: Voicemail Configuration

# Voicemail Configuration

## Configure Voicemail

You can configure the internal or external phone number or URL for the voicemail system. If you use an external voicemail
                              service, the number must include any digits required to dial out and any required area code.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Voice > Phone .

In the General section, enter the Voice Mail Number that is a phone number or URL to check the voicemail.

```
<Voice_Mail_Number ua="na">123</Voice_Mail_Number>
```

Default: Empty

Click Submit All Changes .

### Configure Voicemail for An Extension

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Voice > Ext(n) , where (n) is the number of an extension.

In the Call Feature Settings section, configure the parameters Voice Mail Server , Voice Mail Subscribe Interval (optional), and Voice Mail Enable as described in Parameters for Voicemail Server and Message Waiting .

Click Submit All Changes .

The phone reboots.

### Configure the Message Waiting Indicator

You can configure the Message Waiting Indicator for a specific extension on the phone. The Message Waiting Indicator lights
                                 based on the presence of new voicemail messages in the mailbox.

You can enable the indicator at the top of your IP phone to light when one or more voicemails are left. This light can show
                                 if a message is waiting.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Voice > Ext(n) , where (n) is the number of an extension.

In the Call Feature Settings section, configure the parameter Message Waiting and relevant parameters as described in Parameters for Voicemail Server and Message Waiting .

Click Submit All Changes .

#### Parameters for Voicemail Server and Message Waiting

The following table describes the Call Feature Settings for Voicemail and Message Waiting .

Parameter

Description

Voice Mail Server

Identifies the SpecVM server for the phone, generally the IP address, and port number of the VM server.

Perform one of the following:

In the phone configuration file (cfg.xml), enter a string in this format:

```
<Voice_Mail_Server_1_ ua="na"></Voice_Mail_Server_1_>
```

In the phone web page, enter the IP address of the voicemail server.

Default: Empty

Voice Mail Subscribe Interval

The expiration time, in seconds, of a subscription to a voicemail server.

Perform one of the following:

In the phone configuration file (cfg.xml), enter a string in this format:

```
<Voice_Mail_Subscribe_Interval_1_ ua="na">86400</Voice_Mail_Subscribe_Interval_1_>
```

In the phone web page, enter an appropriate value.

Allowed values: An integer from 0 through 86400

If the value is set to 0, then the phone uses the default value instead.

Default: 86400

Voice Mail Enable

Enables or disables the subscription to the voicemail server for the specific extension.

Perform one of the following:

In the phone configuration file (cfg.xml), enter a string in this format:

```
<Voice_Mail_Enable_1_ ua="na">Yes</Voice_Mail_Enable_1_>
```

In the phone web interface, set this field to Yes or No to enable or disable the function.

Allowed values: Yes and No

Default: Yes

Message Waiting

Indicates whether the Message Waiting Indicator on the phone is lit. This parameter toggles a message from the SIP proxy to
                                                indicate if a message is waiting.

This parameter is valid when the parameters Voice Mail Server , Voice Mail Subscribe Interval , and Voice Mail Enable are configured.

Perform one of the following:

In the phone configuration file (cfg.xml), enter a string in this format:

```
<Message_Waiting_1_ ua="na">Yes</Message_Waiting_1_>
```

In the phone web interface, set this field to Yes or No to enable or disable the function.

Allowed values: Yes and No

Default: Yes

### Configure the Voicemail PLK on a Line Key

You can configure the voicemail PLK on a line key for the users to monitor a specified voicemail account of a user or a group.

The voicemail PLK can monitor both the voicemail of an extension and the voicemail account of another user or a group. Monitoring
                                 the voicemail of another user or a group requires the support from the SIP proxy.

For example, if the users belong to a customer service group, this feature allows the users to monitor both their voicemails
                                 and their group's voicemails.

If you add speed dial for the same line key, the users can press the line key to make a speed dial to the assigned extension.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Voice > Phone .

Select a Line Key on which to configure the voicemail PLK.

(Optional) Set the Extension parameter to Disabled to disable the extension.

If the Direct PLK Configuration feature is disabled, you must disable the extension to configure the voicemail PLK on the
                                                         line key. If the feature is enabled, you can skip this step. For details, see Enable Direct PLK Configuration .

You can also configure this parameter in the phone configuration file (cfg.xml). The parameter is line-specific. Enter a string
                                             in this format:

```
<Extension_ n _ ua="na">Disabled</Extension_ n _>
```

where n is the extension number.

In the Extended Function parameter, enter a string in this format:

For MWI only:

```
fnc=mwi;sub=group_vm@domain;vid=1;nme=Group;
```

For MWI + Speed Dial:

```
fnc=mwi+sd;ext=8000@domain;sub=group_vm@domain;vid=1;nme=Group;
```

For MWI + speed dial + DTMF:

```
fnc=mwi+sd;ext=8000 ,4085283300#,123456#@domain;sub=group_vm@domain;vid=1;nme=Group;
```

For more information about the string syntax, see String Syntax for Voicemail PLK .

You can also configure this parameter in the phone configuration file (cfg.xml). The parameter is line-specific. Enter a string
                                             in this format:

```
<Extended_Function_2_ ua="na">mwi+sd;ext=8000 ,4085283300#,123456#@domain;
sub=group_vm@domain;vid=1;nme=Group;</Extended_Function_2_>
```

In the General section, add mwi or mwi;sd in the parameter Customizable PLK Options .

Parameter in the configuration file (cfg.xml):

```
<Customizable_PLK_Options ua="na">mwi;sd</Customizable_PLK_Options>
```

After the configuration, users can configure the corresponding features on the line key.

Click Submit All Changes .

#### String Syntax for Voicemail PLK

The following table describes the string syntax associated with the voicemail Programmable Line Key (PLK) configured in the
                                    phone web interface.

String

Description

fnc

Specifies the function of the key. You can use the PLK for only MWI or the combination of MWI and speed dial.

Valid values: mwi|mwi+sd

mwi: Enables voicemail account monitoring.

mwi+sd: Enables voicemail account monitoring and speed dial. If used, you must configure "ext" . Otherwise, speed dial doesn't function.

Example: fnc=mwi+sd;

Type: Mandatory

sub

Specifies the SIP URI of a voicemail account that the PLK monitors.

The voicemail account can be the voicemail account of the user of an extension on the phone or a voicemail account of a group.

For example, the user ID of extension 1 is 4085289931. The related voicemail account is 4085289931@example.com. The user belongs
                                                to a customer group whose voicemail account is 4085283300@example.com.

In this example, the value can be 4085289931@example.com. If the SIP proxy allows the group member to monitor the group's
                                                voicemail, the value can be 4085283300@example.com.

Examples:

sub=4085283300@example.com;

sub=4085283300@$PROXY;

Type: Mandatory

vid

The extension ID with which the voicemail PLK associates.

The voicemail PLK associates with an extension of the phone to generate the SIP messages based on the extension user ID and
                                                proxy.

Specifically, the voicemail PLK generates the From and Contact headers based on the associated extension user ID and proxy.
                                                Then it sends a SUBSCRIBE message to the specified SIP URI.

If the string is missing, the PLK associates with extension 1.

Example: vid=2;

Type: Optional

ext

Specifies a speed dial number or a SIP URI if the key uses both MWI and speed dial functions (fnc=mwi+sd).

The speed dial number is used to place a call for the voicemail messages.

Example: ext=8000;

To bypass the voicemail login session during a speed dial from the key, you can input the  DTMF characters (including voicemail
                                                account ID and PIN) in the string.

Example: ext=8000 ,4085283300#,123456#@$PROXY;

Where: "4085283300" is the voicemail account ID, "123456" is the PIN.

We don't recommend that you add the PIN to the speed dial string.

A space is required between the speed dial number (8000) and the DTMF characters (,4085283300#,123456#).

A comma (,) in the speed dial characters means a 2-second pause.

For more information about the speed dial string, see DTMF Wait and Pause Parameters .

Type: Optional

nme

Name displayed on the phone for the key.

If this string is missing, the value will be the user part of the "sub" field. For example, "4085283300" .

Example: nme=Group

Type: Optional

### Configure the Voicemail PLK on the Phone

You can configure the voicemail Programmable Line Key (PLK) on the phone. The maximum number of voicemail PLKs is ten. The
                                 voicemail PLK can monitor the voicemail account of a phone or monitor a voicemail account that isn't configured on the phone.

#### Before you begin

Make sure that one of the following situations are met:

The Extension parameter under the Line Key (n) section from Voice > Phone is set to Disabled .

The Direct PLK Configuration feature is enabled. In this case, you don't need to disable the extension of a line key. For
                                       more information about how to enable the feature, see Enable Direct PLK Configuration .

On the phone, press the line key that you want to configure as an voicemail PLK
                                          					for 2 seconds.

Click MWI or MWI + Speed dial in
                                          					the Select feature screen.

In the Define MWI screen, set up the parameters as described in the following table.

Parameter Name

Description and Default Value

Label

The label of the PLK. For example, VM 3300. If this parameter is missing, the key displays the name part of the User ID parameter.

This parameter is optional.

User ID

The SIP address of a voicemail account. For example, 4085283300@$PROXY.

This parameter is mandatory.

Number

The speed dial number or the SIP URI. For example, 8000 ,3300#,123456#

Click Save .

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the General section, enter the Voice Mail Number that is a phone number or URL to check the voicemail. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Voice_Mail_Number ua="na">123</Voice_Mail_Number> Default: Empty |
| Step 3 | Click Submit All Changes . The phone reboots. |

| Step 1 | Select Voice > Ext(n) , where (n) is the number of an extension. |
|---|---|
| Step 2 | In the Call Feature Settings section, configure the parameters Voice Mail Server , Voice Mail Subscribe Interval (optional), and Voice Mail Enable as described in Parameters for Voicemail Server and Message Waiting . |
| Step 3 | Click Submit All Changes . The phone reboots. |

| Step 1 | Select Voice > Ext(n) , where (n) is the number of an extension. |
|---|---|
| Step 2 | In the Call Feature Settings section, configure the parameter Message Waiting and relevant parameters as described in Parameters for Voicemail Server and Message Waiting . |
| Step 3 | Click Submit All Changes . The phone reboots. |

| Parameter | Description |
|---|---|
| Voice Mail Server | Identifies the SpecVM server for the phone, generally the IP address, and port number of the VM server. Perform one of the following: In the phone configuration file (cfg.xml), enter a string in this format: <Voice_Mail_Server_1_ ua="na"></Voice_Mail_Server_1_> In the phone web page, enter the IP address of the voicemail server. Default: Empty |
| Voice Mail Subscribe Interval | The expiration time, in seconds, of a subscription to a voicemail server. Perform one of the following: In the phone configuration file (cfg.xml), enter a string in this format: <Voice_Mail_Subscribe_Interval_1_ ua="na">86400</Voice_Mail_Subscribe_Interval_1_> In the phone web page, enter an appropriate value. Allowed values: An integer from 0 through 86400 If the value is set to 0, then the phone uses the default value instead. Default: 86400 |
| Voice Mail Enable | Enables or disables the subscription to the voicemail server for the specific extension. Perform one of the following: In the phone configuration file (cfg.xml), enter a string in this format: <Voice_Mail_Enable_1_ ua="na">Yes</Voice_Mail_Enable_1_> In the phone web interface, set this field to Yes or No to enable or disable the function. Allowed values: Yes and No Default: Yes |
| Message Waiting | Indicates whether the Message Waiting Indicator on the phone is lit. This parameter toggles a message from the SIP proxy to
                                                indicate if a message is waiting. This parameter is valid when the parameters Voice Mail Server , Voice Mail Subscribe Interval , and Voice Mail Enable are configured. Perform one of the following: In the phone configuration file (cfg.xml), enter a string in this format: <Message_Waiting_1_ ua="na">Yes</Message_Waiting_1_> In the phone web interface, set this field to Yes or No to enable or disable the function. Allowed values: Yes and No Default: Yes |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | Select a Line Key on which to configure the voicemail PLK. |
| Step 3 | (Optional) Set the Extension parameter to Disabled to disable the extension. Note If the Direct PLK Configuration feature is disabled, you must disable the extension to configure the voicemail PLK on the
                                                         line key. If the feature is enabled, you can skip this step. For details, see Enable Direct PLK Configuration . You can also configure this parameter in the phone configuration file (cfg.xml). The parameter is line-specific. Enter a string
                                             in this format: <Extension_ n _ ua="na">Disabled</Extension_ n _> where n is the extension number. | Note | If the Direct PLK Configuration feature is disabled, you must disable the extension to configure the voicemail PLK on the
                                                         line key. If the feature is enabled, you can skip this step. For details, see Enable Direct PLK Configuration . |
| Note | If the Direct PLK Configuration feature is disabled, you must disable the extension to configure the voicemail PLK on the
                                                         line key. If the feature is enabled, you can skip this step. For details, see Enable Direct PLK Configuration . |
| Step 4 | In the Extended Function parameter, enter a string in this format: For MWI only: fnc=mwi;sub=group_vm@domain;vid=1;nme=Group; For MWI + Speed Dial: fnc=mwi+sd;ext=8000@domain;sub=group_vm@domain;vid=1;nme=Group; For MWI + speed dial + DTMF: fnc=mwi+sd;ext=8000 ,4085283300#,123456#@domain;sub=group_vm@domain;vid=1;nme=Group; For more information about the string syntax, see String Syntax for Voicemail PLK . You can also configure this parameter in the phone configuration file (cfg.xml). The parameter is line-specific. Enter a string
                                             in this format: <Extended_Function_2_ ua="na">mwi+sd;ext=8000 ,4085283300#,123456#@domain;
sub=group_vm@domain;vid=1;nme=Group;</Extended_Function_2_> |
| Step 5 | In the General section, add mwi or mwi;sd in the parameter Customizable PLK Options . Parameter in the configuration file (cfg.xml): <Customizable_PLK_Options ua="na">mwi;sd</Customizable_PLK_Options> After the configuration, users can configure the corresponding features on the line key. |
| Step 6 | Click Submit All Changes . |

| Note | If the Direct PLK Configuration feature is disabled, you must disable the extension to configure the voicemail PLK on the
                                                         line key. If the feature is enabled, you can skip this step. For details, see Enable Direct PLK Configuration . |
|---|---|

| String | Description |
|---|---|
| fnc | Specifies the function of the key. You can use the PLK for only MWI or the combination of MWI and speed dial. Valid values: mwi\|mwi+sd mwi: Enables voicemail account monitoring. mwi+sd: Enables voicemail account monitoring and speed dial. If used, you must configure "ext" . Otherwise, speed dial doesn't function. Example: fnc=mwi+sd; Type: Mandatory |
| sub | Specifies the SIP URI of a voicemail account that the PLK monitors. The voicemail account can be the voicemail account of the user of an extension on the phone or a voicemail account of a group. For example, the user ID of extension 1 is 4085289931. The related voicemail account is 4085289931@example.com. The user belongs
                                                to a customer group whose voicemail account is 4085283300@example.com. In this example, the value can be 4085289931@example.com. If the SIP proxy allows the group member to monitor the group's
                                                voicemail, the value can be 4085283300@example.com. Examples: sub=4085283300@example.com; sub=4085283300@$PROXY; Type: Mandatory |
| vid | The extension ID with which the voicemail PLK associates. The voicemail PLK associates with an extension of the phone to generate the SIP messages based on the extension user ID and
                                                proxy. Specifically, the voicemail PLK generates the From and Contact headers based on the associated extension user ID and proxy.
                                                Then it sends a SUBSCRIBE message to the specified SIP URI. If the string is missing, the PLK associates with extension 1. Example: vid=2; Type: Optional |
| ext | Specifies a speed dial number or a SIP URI if the key uses both MWI and speed dial functions (fnc=mwi+sd). The speed dial number is used to place a call for the voicemail messages. Example: ext=8000; To bypass the voicemail login session during a speed dial from the key, you can input the  DTMF characters (including voicemail
                                                account ID and PIN) in the string. Example: ext=8000 ,4085283300#,123456#@$PROXY; Where: "4085283300" is the voicemail account ID, "123456" is the PIN. Note We don't recommend that you add the PIN to the speed dial string. A space is required between the speed dial number (8000) and the DTMF characters (,4085283300#,123456#). A comma (,) in the speed dial characters means a 2-second pause. For more information about the speed dial string, see DTMF Wait and Pause Parameters . Type: Optional | Note | We don't recommend that you add the PIN to the speed dial string. |
| Note | We don't recommend that you add the PIN to the speed dial string. |
| nme | Name displayed on the phone for the key. If this string is missing, the value will be the user part of the "sub" field. For example, "4085283300" . Example: nme=Group Type: Optional |

| Note | We don't recommend that you add the PIN to the speed dial string. |
|---|---|

| Step 1 | On the phone, press the line key that you want to configure as an voicemail PLK
                                          					for 2 seconds. |
|---|---|
| Step 2 | Click MWI or MWI + Speed dial in
                                          					the Select feature screen. |
| Step 3 | In the Define MWI screen, set up the parameters as described in the following table. Parameter Name Description and Default Value Label The label of the PLK. For example, VM 3300. If this parameter is missing, the key displays the name part of the User ID parameter. This parameter is optional. User ID The SIP address of a voicemail account. For example, 4085283300@$PROXY. This parameter is mandatory. Number The speed dial number or the SIP URI. For example, 8000 ,3300#,123456# | Parameter Name | Description and Default Value | Label | The label of the PLK. For example, VM 3300. If this parameter is missing, the key displays the name part of the User ID parameter. This parameter is optional. | User ID | The SIP address of a voicemail account. For example, 4085283300@$PROXY. This parameter is mandatory. | Number | The speed dial number or the SIP URI. For example, 8000 ,3300#,123456# |
| Parameter Name | Description and Default Value |
| Label | The label of the PLK. For example, VM 3300. If this parameter is missing, the key displays the name part of the User ID parameter. This parameter is optional. |
| User ID | The SIP address of a voicemail account. For example, 4085283300@$PROXY. This parameter is mandatory. |
| Number | The speed dial number or the SIP URI. For example, 8000 ,3300#,123456# |
| Step 4 | Click Save . |

| Parameter Name | Description and Default Value |
|---|---|
| Label | The label of the PLK. For example, VM 3300. If this parameter is missing, the key displays the name part of the User ID parameter. This parameter is optional. |
| User ID | The SIP address of a voicemail account. For example, 4085283300@$PROXY. This parameter is mandatory. |
| Number | The speed dial number or the SIP URI. For example, 8000 ,3300#,123456# |