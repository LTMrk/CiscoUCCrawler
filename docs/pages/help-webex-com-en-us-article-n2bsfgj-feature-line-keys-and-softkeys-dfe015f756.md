---
doc_id: help-webex-com-en-us-article-n2bsfgj-feature-line-keys-and-softkeys-dfe015f756
source_url: https://help.webex.com/en-us/article/n2bsfgj/Feature-line-keys-and-softkeys
retrieved_at: 2026-11-02T13:14:24.643575+00:00
---

## Programmable line keys

The following table lists the dedicated hard buttons and programmable line keys for the features available on the phone:

BLF with speed dial

BLF with call pickup

BLF with speed dial and call pickup

BLF call park

Supported

Calendar

Supported (9851 and 9861 only)

Call forward

Supported

Call park / Unpark

Supported

Conference

Supported (except 9811)

Contacts

Supported (except 9811)

Do not disturb

Supported

Favorite

Supported

Hold / Resume

Supported

Home

Supported (9871 and 8875 only)

Inert

Supported

Mute

Supported

Redial

Supported

Settings

Supported

Speed dial

Supported

Transfer

Supported

For more information about the Programmable Softkey (PSK), see Programmable softkeys configuration (BroadWorks) or Configure the Programmable Softkeys for 9800/8875 (Control Hub) .

## Enable the user to configure features on line keys

You can enable the user to configure features on line keys. The user can then add any of the configured features to the dedicated line keys.

Before you begin

Ensure that the line keys are not in the Inert mode.

(Optional) Disable the extension of a line key on which you allow users to configure the features.

If the Direct PLK Configuration feature is enabled, you don't need to disable the extension manually, skip the step.

Select Voice > Phone .

Select a line key.

Set the Extension to Disabled .

You can also disable the line key in the configuration file (cfg.xml):

```
<Extension_n_ ua="na">Disabled</Extension_n_>
```

where n is the extension number.

Select Voice > Att Console .

In the General section, configure the Customizable PLK Options parameter with the codes of your desired features. See details in the below table:

Speed dial

sd

BLF and Speed dial

sd;blf

BLF and Call pickup

blf;cp

BLF, Speed dial, and Call pickup

sd;blf;cp

Do not disturb

dnd

Redial

redial

Call forward

cfwd

The user does a long-press on an unassigned line key to see the feature list, then the user can then select a feature to add to the line key.

You can also configure this parameter in the configuration file (cfg.xml) with a string in this format:

```
<Customizable_PLK_Options ua="na">sd;blf;cp;dnd;</Customizable_PLK_Options>
```

Click Submit All Changes .

## Add an extended feature to a line Key

This topic provides a general idea on how to add a feature to a line key.  After the configuration, the phone user can press the configured line key to access the assigned feature.

Access the phone administration web page.

Select Voice > Phone .

Select a line key.

Set the Extension parameter to Disabled to disable the extension.

If the Direct PLK Configuration feature is disabled, you must disable the extension to add an extended function to the line key. If the feature is enabled, you can skip this step. For details, see Enable Direct PLK configuration .

In the Extended Function parameter, enter a string in this format:

where fnc= <configuration code> means that the function is the configuration code related feature.

You can also configure this parameter in the configuration file (cfg.xml). Enter a string in this format:

<Extended_Function_n_ ua="na">fnc= <configuration code> </Extended_Function_n_>

where n is the extension number.

For more information about the parameter, see Parameters for extended features on line keys .

For more information about the supported features, configuration codes and string syntax, see Configurable features on line keys .

Click Submit All Changes .

### Parameters for extended features on line keys

Extension

Assigns an extension number to a line key or disables the extension function on a line key.

The number of line keys varies with phone models. When assigned with an extension number, you can configure the line key as a telephony extension. You can assign the line key with extended functions, for example, speed dial, Busy Lamp Field, and call pickup.

By default, you don't need to disable the extension to assign the line key with extended functions. However, if the Direct PLK Configuration feature is disabled, you must disable the extension to achieve the assignment. For more information about how to enable the feature, Enable Direct PLK configuration .

Perform one of the following:

```
<Extension_1_ ua="na">1</Extension_1_>
<Extension_2_ ua="na">2</Extension_2_>
<Extension_3_ ua="na">3</Extension_3_>
<Extension_4_ ua="na">Disabled</Extension_4_>
```

- On the phone web interface, select a number or Disabled from the options.

Allowed values: Disabled|1|2|3|4, the allowed values vary with phones.

Default: n, where n is the line key number.

Extended Function

Used to assign extended functions to a line key on the phone. The supported features are listed in Configurable features on line keys .

Perform one of the following:

- In the phone configuration file with XML(cfg.xml), enter a string that represents the assigned feature.

- On the phone web interface, specify the functions that apply to the line key.

Default: Empty

## Configurable features on line keys

The following table lists the supported features that can be configured on the line keys.

Busy lamp field (BLF) and Speed dial

blf+sd

Makes a call with the speed dial to the monitored line.

String Syntax:

```
fnc=blf+sd;sub=<BLF_URI>;usr=$USER@$PROXY;
or
fnc=blf+sd;sub=<BLF_URI>;ext=$USER@$PROXY;
```

Users can long press the line key to set up the feature on the phone.

BLF and Call pickup

blf+cp

Answers incoming calls for the monitored line.

String Syntax:

```
fnc=blf+cp;sub=<BLF_URI>;usr=$USER@$PROXY;
or
fnc=blf+cp;sub=<BLF_URI>;ext=$USER@$PROXY;
```

Users can long press the line key to set up the feature on the phone.

BLF, Speed dial, and Call pickup

blf+sd+cp

Calls the monitored line or answers incoming calls for the monitored line.

String Syntax:

```
fnc=blf+sd+cp;sub=<BLF_URI>;usr=$USER@$PROXY;
or
fnc=blf+sd+cp;sub=<BLF_URI>;ext=$USER@$PROXY;
```

Users can long press the line key to set up the feature on the phone.

BLF Call park

prk

Parks a call on hold and receives the call for the monitored line.

String Syntax:

```
fnc=prk;sub=<BLF_URI>;usr=$USER@$PROXY;
or
fnc=prk;sub=<BLF_URI>;ext=$USER@$PROXY;
```

Ensure that the parameter BLF Callpark On Line Key Enable (under Voice > Att Console > General ) is set to Yes .

Call forward

cfwd

Turns off call forward or opens call forward settings.

String Syntax:

```
fnc=cfwd[;nme= <display_name> ]
```

Users can long press the line key to set up the feature on the phone.

Call park

prk

Parks a call on hold and receives the call from another phone.

String Syntax:

```
fnc=prk;sub=$USER@$PROXY;nme= <display_name> ;vid= <n> [;orbit=<DN>]
```

Where:

- fnc=prk means function=call park

- sub is the SIP URI of the monitored park slot.

- nme is the name displayed on the phone for the call park line key.

- vid is the extension ID. The values of $USER and $PROXY are retrieved from the specified extension. If vid is missing in the function string, the values of $USER and $PROXY are retrieved from extension 1.

- orbit is the directory number to which the call is parked.

Do not disturb

dnd

Shows the information of the ongoing call.

String Syntax:

```
fnc=dnd[;nme= <softkey_display_name> ]
```

Users can long press the line key to set up the feature on the phone.

Inert

inert

Shuts down the line key to completely disable it. The line key is unavailable when it is in the Inert mode.

The line key can still be registered when it's in the inert mode.

String Syntax:

```
fnc=inert;
```

Redial

redial

Calls the most recently dialed phone number.

String Syntax:

```
fnc=redial;
```

Users can long press the line key to set up the feature on the phone.

Speed dial

sd

Dials the specified speed dial number.

String Syntax:

```
fnc=sd;ext=<number>@$PROXY[;vid=<n>][;nme=<softkey_display_name>]
```

- fnc=sd means function=speed dial

- ext is the speed-dial number that the line key dials out.

- vid is the line index of the phone. It's an optional string.

- nme is the name displayed on the phone for the speed-dial line key. It's an optional string.

Users can long press the line key to set up the feature on the phone.

Speed dial (SIP URI call or meeting)

sd

Dials the specified SIP URI for placing a call or joining a personal room meeting.

String syntax:

```
fnc=sd;user=<SIP_URI>;nme= <display_name> ]
```

Users can long press the line key to set up the feature on the phone.

## Configure Busy Lamp Field (BLF)

As an administrator, you can configure the BLF key with speed dial and call pickup for your users. The BLF keys allow users to monitor their coworkers' lines. When BLF keys are configured with both call pickup and speed dial, users can use the BLF keys to either answer calls for the monitored lines or call the monitored line with one button, or both.

The indicators on the monitoring lines vary with configurations. See the following articles for details:

- Use speed dials on your phone

- Answer calls for your coworkers

### Configure the phone to monitor multiple users' lines

If the phone is registered to a BroadWorks server, you can configure the phone to monitor the entire BLF list. The phone assigns available line keys in sequence to monitor the BLF list entries, and starts showing the status of the monitored lines on the BLF keys.

You can also configure the parameters in the phone configuration file with XML (cfg.xml). To configure each parameter, see the syntax of the string in the following table of Parameters for monitoring multiple users' lines .

Before you begin

Ensure that the phone is registered to a BroadWorks server.

You set up a BLF list for a user of the phone on the BroadWorks server.

Ensure that the monitored lines on the BLF keys are not in the Inert mode.

Access the administration web interface.

Select Voice > Att Console .

Configure BLF List URI , Use Line Keys For BLF List , BLF List , and BLF Label Display Mode as described in the following table of Parameters for monitoring multiple users' lines .

Click Submit All Changes .

#### Parameters for monitoring multiple users' lines

The following table defines the function and usage of the BLF parameters in the General section under the Voice > Att Console tab in the phone web interface. It also defines the syntax of the string that is added in the phone configuration file with XML (cfg.xml) to configure a parameter.

Parameter

Description and default value

The Uniform Resource Identifier (URI) of the Busy Lamp Field (BLF) list that you have set up for a user of the phone, on the BroadWorks server.

This field is only applicable if the phone is registered to a BroadWorks server. The BLF list is the list of users whose lines the phone is allowed to monitor.

The BLF List URI must be specified in the format <URI_name>@<server> . The BLF List URI specified must be the same as the value configured for the List URI: sip parameter on the BroadWorks server.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

<BLF_List_URI ua="na">MonitoredUsersList@sipurash22.com</BLF_List_URI>

On the phone web interface, specify the BLF list that is defined on the BroadSoft server.

Default: Blank

Controls whether the phone uses its line keys to monitor the BLF list, when monitoring of the BLF list is active.

This setting only has significance when BLF List is set to Show .

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

<Use_Line_Keys_For_BLF_List ua="na">Yes</Use_Line_Keys_For_BLF_List>

On the phone web interface, set this field to Yes to use the unregistered lines to monitor the BLF list entries. Set it to No to prevent the line keys from being used for monitoring the BLF list entries.

Default: No

Determines whether to show or hide the BLF list on the line key.

When set to Show , the phone assigns available line keys in sequence, to monitor the BLF list entries. The labels of the BLF list keys show the names of the monitored users and the status of the monitored lines.

This setting only has significance when BLF List URI is configured.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

<BLF_List ua="rw">Show</BLF_List>

On the phone web interface, set this field to Show or Hide to activate or deactivate the BLF monitoring feature.

Allowed values: Show|Hide

Default: Show

BLF Label Display Mode

Specifies how the BLF entries are displayed on the line keys. The options are: Name , Ext (extension number), and Both .

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

<BLF_Label_Display_Mode ua="na">Name</BLF_Label_Display_Mode>

On the phone web interface, select an option from the list.

Allowed values: Name|Ext|Both

Default: Name

### Configure a line to monitor a specific user's line

You can configure
		  busy lamp field on a phone line when a user needs to monitor a coworker's
		  availability to handle calls.

You can configure the busy lamp field to work with any combination of speed dial or call pickup. For example, busy lamp field and speed dial, busy lamp field and call pickup, or busy lamp field with both speed dial and call pickup. But speed dial alone requires a different configuration.

You can also configure the parameters in the phone configuration file with XML (cfg.xml). To configure each parameter, see the syntax of the string in the table of Parameters for monitoring a specific line .

Before you begin

Ensure that the line key on which to configure a busy lamp field is not in the Inert mode.

Access the phone administration web page.

Select Voice > Phone .

Select a line key on which to configure a busy lamp field.

Configure the Extension , Extended Function , fields as defined in the following table of Parameters for monitoring a specific line .

Click Submit All Changes .

#### Parameters for monitoring a specific line

The following table defines the function and usage of the Busy Lamp Field (BLF) parameters in the Line Key (n) sections under the Voice > Phone tab in the phone web interface. It also defines the syntax of the string that is added in the phone configuration file with XML (cfg.xml) to configure a parameter.

Parameter

Description and default value

Extension

Assigns an extension number to a line key or disables the extension function on a line key.

The number of line keys varies with phone models. When assigned with an extension number, you can configure the line key as a telephony extension.

When you need to assign the line key with extended functions (for example, speed dial, BLF, call pickup) while the Direct PLK Configuration feature is disabled, you can either enable the feature or set the Extension parameter to "Disabled".

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

<Extension_1_ ua="na">1</Extension_1_>

<Extension_2_ ua="na">2</Extension_2_>

<Extension_3_ ua="na">3</Extension_3_>

<Extension_4_ ua="na">4</Extension_4_>

On the phone web interface, set the parameter to Disabled to monitor another line on the line key.

Allowed values: Disabled|1|2|3|4, the allowed values vary with phones.

Default: n, where n is the line key number.

Extended Function

This parameter functions only on the lines with the Extension parameter set to Disabled .

Used to assign extended functions to a line on the phone. The supported functions are:

BLF with Call Pickup

Example: fnc=blf+cp;sub=BLF_List_URI@$PROXY;ext=user_ID@$PROXY

BLF with Speed Dial

Example: fnc=blf+sd;sub=BLF_List_URI@$PROXY;ext=user_ID@$PROXY

BLF with Speed Dial and Call Pickup

Example: fnc=blf+sd+cp;sub=BLF_List_URI@$PROXY;ext=user_ID@$PROXY

Where, user_ID represents the ID of the monitored phone.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

<Extended_Function_1_>fnc=blf;sub=BLF_List_URI@$PROXY;ext=user_ID@$PROXY</Extended_Function_1_>

In the phone web interface, configure the parameter with a valid syntax to enable monitoring another user or extension using the line.

Default: Empty

## Add BLF call park on a line key

You can add the call park feature on a specific line key to use only a single button to park or unpark a call for a monitored user.

This topic is for Cisco Desk Phone 9800 Series registered to BroadWorks.

Select Voice > Att Console > General .

Select Yes for the parameter BLF Callpark On Line Key Enable .

To disable the feature, select No .

You can also configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<BLF_Callpark_On_Line_Key_Enable ua=”na“>Yes</BLF_Callpark_On_Line_Key_Enable>
```

Default: No .

Navigate to Voice > Phone and select a line key.

(Optional) Set the Extension parameter to Disabled .

If the Direct PLK Configuration feature is enabled, you don't need to disable the extension manually, skip the step.

You can also configure the parameter in the configuration file (cfg.xml). The parameter is line-specific. Enter a string in the following format:

```
<Extension_2_ ua="na">Disabled</Extension_2_>
```

Enter the string in the following format in the Extended Function field:

```
fnc=prk;sub=BLF_URI;usr=$USER@$PROXY;
or
fnc=prk;sub=BLF_URI;ext=$USER@$PROXY;
```

- fnc=prk means feature is call park

- sub— the URI to which the SUBSCRIBE message is sent. This name must be identical to the name defined in the BLF List URI.

- usr— the call park extension that the BLF monitors.

Click Submit All Changes .

## Add Call Park shortcut to an idle extension

You can add call park to an idle extension to enable the user to temporarily store and retrieve calls. Call Park is supported on private lines and shared lines. When configured, the user can park and unpark a call through the extension.

Access the phone administration web page.

Select Voice > Att Console > General .

Select No for the parameter BLF Callpark On Line Key Enable to disable the Busy Lamp Field (BLF) Call Park feature on the phone.

Select Voice > Phone .

Select a line key.

(Optional) Set the Extension parameter to Disabled .

If the Direct PLK Configuration feature is enabled, you don't need to disable the extension manually, skip the step.

You can also configure the parameter in the configuration file (cfg.xml). The parameter is line-specific. Enter a string in the following format:

```
<Extension_2_ ua="na">Disabled</Extension_2_>
```

In the Extended Function parameter, enter a string in this format:

For a private line, enter

```
fnc=prk;sub=$USER@$PROXY;nme=callpark;vid=1;
```

For a shared line, enter

```
fnc=prk;sub=$USER@$PROXY;nme=callpark;orbit=<DN of shared line>;vid=1;
```

Where,

fnc=prk means function=call park

sub is the SIP URI of the monitored park slot.

nme is the name displayed on the phone for the call park line key.

orbit is the DN of the shared line.

vid is the extension ID. The values of $USER and $PROXY are retrieved from the specified extension. If vid is missing in the function string, the values of $USER and $PROXY are retrieved from extension 1.

You can also configure the line-specific parameter in the configuration file (cfg.xml). Enter a string in the following format:

```
<Extended_Function_2_ ua="na">fnc=prk;sub=$USER@$PROXY;nme=callpark;vid=1;</Extended_Function_2_>
```

Click Submit
				All Changes .

## Enable Direct PLK configuration

Before you begin

You can directly perform Programmable Line Key (PLK) configurations on a line key, which means you don't need to disable the extension function of a line key. If you disable the Direct PLK Configuration feature, you must disable the line extension to achieve PLK configurations.

Select Voice > Phone .

In the Miscellaneous Line Key Settings section, set the Enable Direct PLK Configuration parameter to Yes .

You can also configure the parameter in the phone configuration file (cfg.xml) with the following XML string:

```
<Enable_Direct_PLK_Configuration ua="na">Yes</Enable_Direct_PLK_Configuration>
```

Allowed values: Yes and No

Default value: Yes

If you set the parameter to "No", the extension of a line key must be disabled for the PLK configuration.

Select Voice > Ext [n] (where [n] is the extension number).

In the Proxy and Registration section, ensure that the Proxy parameter is empty.

You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format:

```
<Proxy_n_ ua="na"></Proxy_n_>
```

In the Subscriber Information section, ensure that the User ID parameter is empty.

```
<User_ID_n_ ua="na"></User_ID_n_>
```

Click Submit All Changes .

## Shut down a line key

You can shut down a line key by setting the Inert mode for it from the phone web page. When the line key is in the Inert mode, the line key LED is disabled, Busy Lamp Field (BLF) doesn't work on the line key, no icon or text displays next to the line key, and the line key button is not responsive, long-press configuration is disabled. In a word, the line key configured with the Inert mode is completely unavailable for the phone users.

A line key on the phone can still be registered when it's in the inert mode.

Disable the line key that will use the Inert mode. Do any of the following actions on the phone web page:

You can also disable the line key in the configuration file (cfg.xml):

```
<Extension_n_ ua="na">Disabled</Extension_n_>
```

If the Direct PLK Configuration feature is enabled, you don't need to disable the extension manually, skip the step.

You can also disable the line key in the configuration file (cfg.xml):

```
<Line_Enable_n_ ua="na">No</Line_Enable_n_>
```

Set the Inert mode for the specific line key.

Select Voice > Phone .

Select the target line key.

In the Extended Function parameter, enter a string in this format:

```
fnc=inert;
```

You can also configure this parameter in the phone configuration file (cfg.xml). The parameter is line-specific. Enter a string in this format:

```
<Extended_Function_n_ ua="na">fnc=inert;</Extended_Function_n_>
```

where n is the extension number.

Click Submit All Changes .

| Feature name | Hard button | PLK |
|---|---|---|
| BLF with speed dial BLF with call pickup BLF with speed dial and call pickup BLF call park |  | Supported |
| Calendar | Supported (9851 and 9861 only) |  |
| Call forward |  | Supported |
| Call park / Unpark |  | Supported |
| Conference | Supported (except 9811) |  |
| Contacts | Supported (except 9811) |  |
| Do not disturb |  | Supported |
| Favorite | Supported |  |
| Hold / Resume | Supported |  |
| Home | Supported (9871 and 8875 only) |  |
| Inert |  | Supported |
| Mute | Supported |  |
| Redial |  | Supported |
| Settings | Supported |  |
| Speed dial |  | Supported |
| Transfer | Supported |  |

| 1 | (Optional) Disable the extension of a line key on which you allow users to configure the features. If the Direct PLK Configuration feature is enabled, you don't need to disable the extension manually, skip the step. Select Voice > Phone . Select a line key. Set the Extension to Disabled . You can also disable the line key in the configuration file (cfg.xml): <Extension_n_ ua="na">Disabled</Extension_n_> where n is the extension number. |
|---|---|
| 2 | Select Voice > Att Console . |
| 3 | In the General section, configure the Customizable PLK Options parameter with the codes of your desired features. See details in the below table: Table 2. Configurable features on line keys Feature String Speed dial sd BLF and Speed dial sd;blf BLF and Call pickup blf;cp BLF, Speed dial, and Call pickup sd;blf;cp Do not disturb dnd Redial redial Call forward cfwd The user does a long-press on an unassigned line key to see the feature list, then the user can then select a feature to add to the line key. You can also configure this parameter in the configuration file (cfg.xml) with a string in this format: <Customizable_PLK_Options ua="na">sd;blf;cp;dnd;</Customizable_PLK_Options> | Feature | String | Speed dial | sd | BLF and Speed dial | sd;blf | BLF and Call pickup | blf;cp | BLF, Speed dial, and Call pickup | sd;blf;cp | Do not disturb | dnd | Redial | redial | Call forward | cfwd |
| Feature | String |
| Speed dial | sd |
| BLF and Speed dial | sd;blf |
| BLF and Call pickup | blf;cp |
| BLF, Speed dial, and Call pickup | sd;blf;cp |
| Do not disturb | dnd |
| Redial | redial |
| Call forward | cfwd |
| 4 | Click Submit All Changes . |

| Feature | String |
|---|---|
| Speed dial | sd |
| BLF and Speed dial | sd;blf |
| BLF and Call pickup | blf;cp |
| BLF, Speed dial, and Call pickup | sd;blf;cp |
| Do not disturb | dnd |
| Redial | redial |
| Call forward | cfwd |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | Select a line key. |
| 4 | Set the Extension parameter to Disabled to disable the extension. If the Direct PLK Configuration feature is disabled, you must disable the extension to add an extended function to the line key. If the feature is enabled, you can skip this step. For details, see Enable Direct PLK configuration . |
| 5 | In the Extended Function parameter, enter a string in this format: fnc= <configuration code> where fnc= <configuration code> means that the function is the configuration code related feature. You can also configure this parameter in the configuration file (cfg.xml). Enter a string in this format: <Extended_Function_n_ ua="na">fnc= <configuration code> </Extended_Function_n_> where n is the extension number. For more information about the parameter, see Parameters for extended features on line keys . For more information about the supported features, configuration codes and string syntax, see Configurable features on line keys . |
| 6 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Extension | Assigns an extension number to a line key or disables the extension function on a line key. The number of line keys varies with phone models. When assigned with an extension number, you can configure the line key as a telephony extension. You can assign the line key with extended functions, for example, speed dial, Busy Lamp Field, and call pickup. By default, you don't need to disable the extension to assign the line key with extended functions. However, if the Direct PLK Configuration feature is disabled, you must disable the extension to achieve the assignment. For more information about how to enable the feature, Enable Direct PLK configuration . Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Extension_1_ ua="na">1</Extension_1_>
<Extension_2_ ua="na">2</Extension_2_>
<Extension_3_ ua="na">3</Extension_3_>
<Extension_4_ ua="na">Disabled</Extension_4_> On the phone web interface, select a number or Disabled from the options. Allowed values: Disabled\|1\|2\|3\|4, the allowed values vary with phones. Default: n, where n is the line key number. |
| Extended Function | Used to assign extended functions to a line key on the phone. The supported features are listed in Configurable features on line keys . Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string that represents the assigned feature. On the phone web interface, specify the functions that apply to the line key. Default: Empty |

| Feature | Configuration Code (fnc=) | Description and string syntax |
|---|---|---|
| Busy lamp field (BLF) and Speed dial | blf+sd | Makes a call with the speed dial to the monitored line. String Syntax: fnc=blf+sd;sub=<BLF_URI>;usr=$USER@$PROXY;
or
fnc=blf+sd;sub=<BLF_URI>;ext=$USER@$PROXY; Users can long press the line key to set up the feature on the phone. |
| BLF and Call pickup | blf+cp | Answers incoming calls for the monitored line. String Syntax: fnc=blf+cp;sub=<BLF_URI>;usr=$USER@$PROXY;
or
fnc=blf+cp;sub=<BLF_URI>;ext=$USER@$PROXY; Users can long press the line key to set up the feature on the phone. |
| BLF, Speed dial, and Call pickup | blf+sd+cp | Calls the monitored line or answers incoming calls for the monitored line. String Syntax: fnc=blf+sd+cp;sub=<BLF_URI>;usr=$USER@$PROXY;
or
fnc=blf+sd+cp;sub=<BLF_URI>;ext=$USER@$PROXY; Users can long press the line key to set up the feature on the phone. |
| BLF Call park | prk | Parks a call on hold and receives the call for the monitored line. String Syntax: fnc=prk;sub=<BLF_URI>;usr=$USER@$PROXY;
or
fnc=prk;sub=<BLF_URI>;ext=$USER@$PROXY; Ensure that the parameter BLF Callpark On Line Key Enable (under Voice > Att Console > General ) is set to Yes . |
| Call forward | cfwd | Turns off call forward or opens call forward settings. String Syntax: fnc=cfwd[;nme= <display_name> ] Users can long press the line key to set up the feature on the phone. |
| Call park | prk | Parks a call on hold and receives the call from another phone. String Syntax: fnc=prk;sub=$USER@$PROXY;nme= <display_name> ;vid= <n> [;orbit=<DN>] Where: fnc=prk means function=call park sub is the SIP URI of the monitored park slot. nme is the name displayed on the phone for the call park line key. vid is the extension ID. The values of $USER and $PROXY are retrieved from the specified extension. If vid is missing in the function string, the values of $USER and $PROXY are retrieved from extension 1. orbit is the directory number to which the call is parked. |
| Do not disturb | dnd | Shows the information of the ongoing call. String Syntax: fnc=dnd[;nme= <softkey_display_name> ] Users can long press the line key to set up the feature on the phone. |
| Inert | inert | Shuts down the line key to completely disable it. The line key is unavailable when it is in the Inert mode. The line key can still be registered when it's in the inert mode. String Syntax: fnc=inert; |
| Redial | redial | Calls the most recently dialed phone number. String Syntax: fnc=redial; Users can long press the line key to set up the feature on the phone. |
| Speed dial | sd | Dials the specified speed dial number. String Syntax: fnc=sd;ext=<number>@$PROXY[;vid=<n>][;nme=<softkey_display_name>] Where, fnc=sd means function=speed dial ext is the speed-dial number that the line key dials out. vid is the line index of the phone. It's an optional string. nme is the name displayed on the phone for the speed-dial line key. It's an optional string. Users can long press the line key to set up the feature on the phone. |
| Speed dial (SIP URI call or meeting) | sd | Dials the specified SIP URI for placing a call or joining a personal room meeting. String syntax: fnc=sd;user=<SIP_URI>;nme= <display_name> ] Users can long press the line key to set up the feature on the phone. |

| 1 | Access the administration web interface. |
|---|---|
| 2 | Select Voice > Att Console . |
| 3 | Configure BLF List URI , Use Line Keys For BLF List , BLF List , and BLF Label Display Mode as described in the following table of Parameters for monitoring multiple users' lines . |
| 4 | Click Submit All Changes . |

| Parameter | Description and default value |
|---|---|
| BLF List URI | The Uniform Resource Identifier (URI) of the Busy Lamp Field (BLF) list that you have set up for a user of the phone, on the BroadWorks server. This field is only applicable if the phone is registered to a BroadWorks server. The BLF list is the list of users whose lines the phone is allowed to monitor. The BLF List URI must be specified in the format <URI_name>@<server> . The BLF List URI specified must be the same as the value configured for the List URI: sip parameter on the BroadWorks server. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <BLF_List_URI ua="na">MonitoredUsersList@sipurash22.com</BLF_List_URI> On the phone web interface, specify the BLF list that is defined on the BroadSoft server. Default: Blank |
| Use Line Keys For BLF List | Controls whether the phone uses its line keys to monitor the BLF list, when monitoring of the BLF list is active. This setting only has significance when BLF List is set to Show . Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Use_Line_Keys_For_BLF_List ua="na">Yes</Use_Line_Keys_For_BLF_List> On the phone web interface, set this field to Yes to use the unregistered lines to monitor the BLF list entries. Set it to No to prevent the line keys from being used for monitoring the BLF list entries. Default: No |
| BLF List | Determines whether to show or hide the BLF list on the line key. When set to Show , the phone assigns available line keys in sequence, to monitor the BLF list entries. The labels of the BLF list keys show the names of the monitored users and the status of the monitored lines. This setting only has significance when BLF List URI is configured. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <BLF_List ua="rw">Show</BLF_List> On the phone web interface, set this field to Show or Hide to activate or deactivate the BLF monitoring feature. Allowed values: Show\|Hide Default: Show |
| BLF Label Display Mode | Specifies how the BLF entries are displayed on the line keys. The options are: Name , Ext (extension number), and Both . Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <BLF_Label_Display_Mode ua="na">Name</BLF_Label_Display_Mode> On the phone web interface, select an option from the list. Allowed values: Name\|Ext\|Both Default: Name |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | Select a line key on which to configure a busy lamp field. |
| 4 | Configure the Extension , Extended Function , fields as defined in the following table of Parameters for monitoring a specific line . |
| 5 | Click Submit All Changes . |

| Parameter | Description and default value |
|---|---|
| Extension | Assigns an extension number to a line key or disables the extension function on a line key. The number of line keys varies with phone models. When assigned with an extension number, you can configure the line key as a telephony extension. When you need to assign the line key with extended functions (for example, speed dial, BLF, call pickup) while the Direct PLK Configuration feature is disabled, you can either enable the feature or set the Extension parameter to "Disabled". Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Extension_1_ ua="na">1</Extension_1_> <Extension_2_ ua="na">2</Extension_2_> <Extension_3_ ua="na">3</Extension_3_> <Extension_4_ ua="na">4</Extension_4_> On the phone web interface, set the parameter to Disabled to monitor another line on the line key. Allowed values: Disabled\|1\|2\|3\|4, the allowed values vary with phones. Default: n, where n is the line key number. |
| Extended Function | This parameter functions only on the lines with the Extension parameter set to Disabled . Used to assign extended functions to a line on the phone. The supported functions are: BLF with Call Pickup Example: fnc=blf+cp;sub=BLF_List_URI@$PROXY;ext=user_ID@$PROXY BLF with Speed Dial Example: fnc=blf+sd;sub=BLF_List_URI@$PROXY;ext=user_ID@$PROXY BLF with Speed Dial and Call Pickup Example: fnc=blf+sd+cp;sub=BLF_List_URI@$PROXY;ext=user_ID@$PROXY Where, user_ID represents the ID of the monitored phone. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Extended_Function_1_>fnc=blf;sub=BLF_List_URI@$PROXY;ext=user_ID@$PROXY</Extended_Function_1_> In the phone web interface, configure the parameter with a valid syntax to enable monitoring another user or extension using the line. Default: Empty |

| 1 | Select Voice > Att Console > General . |
|---|---|
| 2 | Select Yes for the parameter BLF Callpark On Line Key Enable . To disable the feature, select No . You can also configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <BLF_Callpark_On_Line_Key_Enable ua=”na“>Yes</BLF_Callpark_On_Line_Key_Enable> Default: No . |
| 3 | Navigate to Voice > Phone and select a line key. |
| 4 | (Optional) Set the Extension parameter to Disabled . If the Direct PLK Configuration feature is enabled, you don't need to disable the extension manually, skip the step. You can also configure the parameter in the configuration file (cfg.xml). The parameter is line-specific. Enter a string in the following format: <Extension_2_ ua="na">Disabled</Extension_2_> |
| 5 | Enter the string in the following format in the Extended Function field: fnc=prk;sub=BLF_URI;usr=$USER@$PROXY;
or
fnc=prk;sub=BLF_URI;ext=$USER@$PROXY; Where, fnc=prk means feature is call park sub— the URI to which the SUBSCRIBE message is sent. This name must be identical to the name defined in the BLF List URI. usr— the call park extension that the BLF monitors. |
| 6 | Click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Att Console > General . |
| 3 | Select No for the parameter BLF Callpark On Line Key Enable to disable the Busy Lamp Field (BLF) Call Park feature on the phone. |
| 4 | Select Voice > Phone . |
| 5 | Select a line key. |
| 6 | (Optional) Set the Extension parameter to Disabled . If the Direct PLK Configuration feature is enabled, you don't need to disable the extension manually, skip the step. You can also configure the parameter in the configuration file (cfg.xml). The parameter is line-specific. Enter a string in the following format: <Extension_2_ ua="na">Disabled</Extension_2_> |
| 7 | In the Extended Function parameter, enter a string in this format: For a private line, enter fnc=prk;sub=$USER@$PROXY;nme=callpark;vid=1; For a shared line, enter fnc=prk;sub=$USER@$PROXY;nme=callpark;orbit=<DN of shared line>;vid=1; Where, fnc=prk means function=call park sub is the SIP URI of the monitored park slot. nme is the name displayed on the phone for the call park line key. orbit is the DN of the shared line. vid is the extension ID. The values of $USER and $PROXY are retrieved from the specified extension. If vid is missing in the function string, the values of $USER and $PROXY are retrieved from extension 1. You can also configure the line-specific parameter in the configuration file (cfg.xml). Enter a string in the following format: <Extended_Function_2_ ua="na">fnc=prk;sub=$USER@$PROXY;nme=callpark;vid=1;</Extended_Function_2_> |
| 8 | Click Submit
				All Changes . |

| 1 | Select Voice > Phone . |
|---|---|
| 2 | In the Miscellaneous Line Key Settings section, set the Enable Direct PLK Configuration parameter to Yes . You can also configure the parameter in the phone configuration file (cfg.xml) with the following XML string: <Enable_Direct_PLK_Configuration ua="na">Yes</Enable_Direct_PLK_Configuration> Allowed values: Yes and No Default value: Yes If you set the parameter to "No", the extension of a line key must be disabled for the PLK configuration. |
| 3 | Select Voice > Ext [n] (where [n] is the extension number). |
| 4 | In the Proxy and Registration section, ensure that the Proxy parameter is empty. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Proxy_n_ ua="na"></Proxy_n_> where n is the extension number. |
| 5 | In the Subscriber Information section, ensure that the User ID parameter is empty. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <User_ID_n_ ua="na"></User_ID_n_> where n is the extension number. |
| 6 | Click Submit All Changes . |

| 1 | Disable the line key that will use the Inert mode. Do any of the following actions on the phone web page: Set Extension to Disabled for the specific line key on the Voice > Phone tab. You can also disable the line key in the configuration file (cfg.xml): <Extension_n_ ua="na">Disabled</Extension_n_> where n is the extension number. If the Direct PLK Configuration feature is enabled, you don't need to disable the extension manually, skip the step. Set Line Enable to No for the specific line key on the Voice > Ext(n) . You can also disable the line key in the configuration file (cfg.xml): <Line_Enable_n_ ua="na">No</Line_Enable_n_> where n is the extension number. |
|---|---|
| 2 | Set the Inert mode for the specific line key. Select Voice > Phone . Select the target line key. In the Extended Function parameter, enter a string in this format: fnc=inert; where fnc=inert means function=inert. You can also configure this parameter in the phone configuration file (cfg.xml). The parameter is line-specific. Enter a string in this format: <Extended_Function_n_ ua="na">fnc=inert;</Extended_Function_n_> where n is the extension number. Click Submit All Changes . |