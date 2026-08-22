---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg400-vg400-scg-configuring-supplementary-call-features-html-df5416b48d
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg400/vg400-scg/configuring-supplementary-call-features.html
retrieved_at: 2026-08-22T01:19:04.238105+00:00
---

Cisco VG400 Voice Gateway Software Configuration Guide

# Cisco VG400 Voice Gateway Software Configuration Guide

Updated: August 27, 2024

Chapter: Configuring Supplementary Call Features

## Chapter: Configuring Supplementary Call Features

# Configuring Supplementary Call Features

## Feature History

Feature or Enhancement

Cisco IOS XE Release

Feature Description

Supplementary call features

Cisco IOS XE 16.12.1

The following call features are supported from Cisco IOS XE 16.12.1:

Call forward all and cancel forward all

Call forward no answer/busy

Call waiting and cancel call waiting

Directed call park

Directed call pickup

Call pickup group

Call pickup local

Last number redial

Unattended and attended call transfer

Three-way conference

Drop last conferee

AMWI tones for voicemail

Inband signaling for DTMF

T.38 fax

Enhanced call features

Cisco IOS XE 17.15.1a

The following call features are supported from Cisco IOS XE 17.15.1a:

Forward all to voice mail

Hunt group login and logout

Toggle between calls

Call Back

## Feature Access Codes

Feature access codes, also known as star codes, are a specific combination of digits that give you access to advanced calling
                           features. FACs consist of a prefix and a code, and each code is programmed to give you access to a specific supplementary
                           service. For example, if you enter the code, **4 .

Analog phones do not have soft keys, and the required supplementary service features are invoked through FAC. Thus, you need
                           to first configure the FAC before you can configure the call features. If you do not perform this configuration first, the
                           whole FAC digits are sent to the CUCM as is and the FAC is not translated to a format that the CUCM can understand to enable
                           the corresponding call feature.

## Configure Feature Access Codes

To enable and use FACs that activate specific call features, perform these procedures. After you enable FAC, each call feature
                           is associated with a default FAC value. You need not configure FAC for each call feature explicitly. You need to configure
                           the FAC for a call feature only when you want to assign a different prefix or a code for the call feature.

By default, FAC is disabled if you’re using an image earlier than Cisco IOS XE 17.15.1a. In this case, you must perform these
                                       steps. If you’re using Cisco IOS XE 17.15.1a or a later version, FAC is auto enabled with Auto Configuration.

Enable Device Control Session Application if you have not enabled Auto Configuration.

Enable Feature Access Codes and use the show command to view the code for each call feature.

Configure the call features using the appropriate CLI.

## Enable Feature Access Codes

Perform these steps to configure Feature Access Codes (FACs) for analog phones connected to your Cisco Voice Gateway.

### SUMMARY STEPS

- enable

- configure terminal

- dsapp line

- feature access code

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enables privileged EXEC mode. Enter your password, if prompted.

Step 2

configure terminal

### Example:

```
Device# configure terminal
```

Enters the global configuration mode.

Step 3

dsapp line

### Example:

```
Device(config)# dsapp line
```

Enters the DSAPP Line configuration mode.

Step 4

feature access code

### Example:

```
Device(config-dsappline)# feature access-code
```

Enables the voice gateway to translate the FACs dialed by analog phone users into a format that CUCM understands, thereby
                                          allowing the invocation of supplementary services like call forward, call waiting, call pickup, etc.

## View Feature Access Codes

To view the FAC for each of the call feature, run the show dsapp line feature codes command. Make a note of this list before you configure the call features.

### SUMMARY STEPS

- show dsapp line feature codes

### DETAILED STEPS

show dsapp line feature codes

### Example:

```
Device# show dsapp line feature codes
dsapp line feature access-code
prefix *#
call forward all *#1
call forward cancel *#2
pickup local *#5
pickup group *#7
pickup direct *#6
cancel-call-waiting **4
last-redial *#3
```

Displays whether FAC is enabled and the feature codes for the call features. By default, the FAC has ‘**’ prefix which can
                                          be changed in the CLI. You can also change the default FAC in the sub-mode.

## Configure Call Features

This section contains information and tasks for configuring supplementary call features such as call transfer and forward,
                           conferencing, toggle between calls, and more.

### Call Transfer

The Call Transfer feature allows you to redirect a connected call from your phone to another number. After the call is transferred,
                              your call is disconnected and the transferred call is established as a new call connection. A Call Transfer status includes:

Hookflash: A hookflash is a brief interruption in the loop as the system places the active call on hold.

On hook: This option completes the call transfer.

This feature is supported from Cisco IOS XE 16.12.1. See this table to learn about the call transfer actions.

State

Action

Result

Response on FXS Line

Active call

Controller hookflash

Held call

Second dial tone

Held call and outgoing dialed, alerting, and active call

Controller on hook

Held call and active call transferred

Transfer

### Configure Call Transfer

### SUMMARY STEPS

- enable

- configure terminal

- application

- service dsapp

- param callWaiting TRUE

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode. Enter your password, if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters the global configuration mode.

Step 3

application

#### Example:

```
Device(config)# application
```

Enters the Application Configuration mode.

Step 4

service dsapp

#### Example:

```
Device(config-app)# service dsapp
```

Enables the DSAPP service.

Step 5

param callWaiting TRUE

#### Example:

```
Device(app-global)# param callWaiting TRUE
```

Enables the Call Waiting feature.

#### Sample Configuration

```
Device> enable
Device# configure terminal
Device(config)# application
Device(config-app)# service dsapp
Device(app-global)# param callWaiting TRUE
```

### Three-Way Conference

A Three-Way Conference feature allows you to add a third party to an existing call, thereby creating a conference call. This
                              can be done by first placing the current call on hold, dialing the new party, and then connecting both calls together. Thus,
                              a three-way conference call allows three people to participate in a single phone session.

This feature is supported from Cisco IOS XE 16.12.1. See the table describes the three-way conference action.

State

Action

Result

Active Call

First party hookflash

Held call

First party held and second party active

Active call hookflash

First and second calls are bridged

Three-way conference

Controller on hook

Both call legs torn down

Three-way conference

First called party on hook

Call between controller and first called party terminated. Call between controller and second called party remains active.

Three-way conference

Second called party on hook

Call between controller and second called party terminated. Call between controller and first called party remains active.

Three-way conference

Controller hookflash

Call between controller and second called party terminated, call between controller and first called party remains.

### Configure Three Way Conference

### SUMMARY STEPS

- enable

- configure terminal

- application

- service dsapp

- param callConference TRUE

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode. Enter your password, if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters the global configuration mode.

Step 3

application

#### Example:

```
Device(config)# application
```

Enters the Application Configuration mode.

Step 4

service dsapp

#### Example:

```
Device(config-app)# service dsapp
```

Enables the DSAPP service.

Step 5

param callConference TRUE

#### Example:

```
Device(app-global)# param callConference TRUE
```

Enables the Call Conferencing feature.

#### Sample Configuration

```
Device> enable
Device# configure terminal
Device(config)# application
Device(config-app)# service dsapp
Device(app-global)# param callConference TRUE
```

### Configure Forward to Voice Mail

This feature allows a phone user to forward all calls to their voice mail system. This feature is a subset of the Call Forward
                                 All feature, which allows a phone user to direct all calls to a specified directory number.

To configure this call feature, perform these steps:

### SUMMARY STEPS

- enable

- configure terminal

- dsapp line feature voice-mail <voicemail-number>

- forward-to-voicemail <keypad-character>

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode. Enter your password, if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters the global configuration mode.

Step 3

dsapp line feature voice-mail <voicemail-number>

#### Example:

```
Device(config)# dsapp line feature voice-mail 8356934859
```

Enables forward to voicemail. Here, voicemail-number is the voice mail number where the call should be forwarded. The maximum
                                             length for this keyword is 11.

When you configure the voicemail number, ensure it is real phone number. If the number you specify is not valid, the FAC dial-out
                                             forward-to-voicemail (**4) fails because CUCM cannot detect the validity of the number you specified.

Step 4

forward-to-voicemail <keypad-character>

#### Example:

```
Device(config-dsappline-fac)# forward-to-voicemail **6
```

This step is optional, and you need not perform this step if you chose the default value of **4. In this command syntax, the
                                             keypad-character is the string that a user needs to dial through their phone keypad. If you wish to change this default value,
                                             run this command and enter the new value from your phone keypad.

To cancel the forward to voicemail functionality, run the cancel call forward all command.

#### Sample Configuration - Configure voice mail

```
enable
configure terminal
dsapp line feature voice-mail 5698759384
end
```

Example: Sample Configuration - Configure FAC

```
enable
configure terminal
dsapp line feature access-code
forward-to-voicemail **4
end
!
```

### Hunt Group Login and Logout

Hunt groups are used to pool together a group of lines, so that when CUCM receives an incoming call, it chooses a line in
                              the hunt group that is not busy to route the call. Hunt groups help CUCM to efficiently distribute simultaneous incoming calls
                              on specific lines that are part of that group. For example, if a call center receives multiple calls at once, hunt groups
                              help route the calls to the first available line in a given hunt group.

Hunt group login and logout allows you to toggle between logging in and logging out of the hunt group on an analog phone by
                              using feature access codes. For example, if a user in a call center goes off hook and hears the dial tone on an analog phone,
                              they then press the feature access code and hear a confirmation tone. The analog phone, once registered to the CUCM and when
                              the Logged Into Hunt Group setting is enabled, logs in to the hunt group, and routes the incoming calls to the first available phone in the hunt group.
                              If the Logged Into Hunt Group setting is not enabled, the user needs to dial the hunt-group FAC to log in their analog phone to the hunt group after registering
                              successfully.

The user can, at the end of their workday, logout of the hunt group using the same feature access code so that no more calls
                              are received on that line.

### Configure Hunt Group Login and Logout

To configure hunt group login and logout, perform these steps:

### SUMMARY STEPS

- enable

- configure terminal

- dsapp line feature access-code

- hunt-group login-logout <keypad-character>

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode. Enter your password, if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters the global configuration mode.

Step 3

dsapp line feature access-code

#### Example:

```
Device(config)# dsapp line feature access-code
```

Enters the dsapp feature access code mode and configures the hunt group login and logout feature.

Step 4

hunt-group login-logout <keypad-character>

This is an optional step and needs to be performed if you want to change the FAC for enabling hunt group login and logout.
                                             In this command syntax, the keypad-character is the string that a user needs to dial through their phone keypad. The default
                                             value for this feature is **8.

#### Sample Configuration

```
enable
configure terminal
dsapp line feature access-code
 hunt-group login-logout **8
end
!
```

### Toggle Between Calls

The Toggle Between Calls feature allows a user, while on a call with one party (A), to place the call on hold, dial a number
                              to connect to a second call (B), and then switch back to the original connection (A) if needed, before connecting both parties.

After the user connects to A and before transferring the call, the user can press the Hold or Resume button to toggle between
                              the two calls. This allows the user to consult privately with A and B before completing the transfer.

For example, in a call center, a technical support agent can use this feature to place a call on hold, call their manager,
                              and brief the manager about an issue or a case before switching back to the original caller.

#### Toggle Between Calls Workflow

The sequence of placing a call on hold is summarized in the following steps:

User A and user B are active with a call.

By pressing hookflash, user A initiates a call hold.

SIP sends a call hold indication to user B.

User A can now initiate another active call (user C) or transfer the active call (call transfer).

This table specifies the possible scenarios or workflows when you toggle between calls, the action that needs to be performed,
                                 and the expected result for each scenario.

State

Action

Result

Response to FXS Line

Active call

Hookflash

Call placed on hold for the remote caller

Second dial tone for the FXS phone

Call on hold

Hookflash

Call is active

FXS line connects to the call

Call on hold and an active call

Hookflash

Active and call on hold are swapped

FXS line connects to the held call

Call on hold and an active call

On hook

Active call is dropped

The call that is held is active and a reminder ring is seen on the FXS line.

Call on hold and an active call

Call on hold goes on hook

Call on hold is dropped

No response

Call on hold and an active call

Active call goes on hook

Active call is dropped

Silence or no response. Reconnects to held call after the value you specify for <disc-toggle-time> expires.

### Toggle Between Calls and Feature Mode

To configure the Toggle between calls feature, you must first enable Feature Mode. This mode refers to a setting that allows
                              you to configure call routing based on different operating modes, essentially defining how calls are handled depending on
                              specific situations. Feature Mode also provides enhanced call-control mode capability on analog ports on Cisco voice gateways.

In a toggle between calls call flow, after a user establishes a second call, the user in the basic call mode performs a hookflash
                              to get the first dial tone, then dials an extension number to connect to a second call. When the second call is established,
                              the user performs a hookflash to get a feature tone, which is a special dial tone used to indicate feature mode. Then, the
                              user dials the FAC for this call feature.

By default, the feature mode is disabled in the voice gateways. Ensure this mode is enabled before you configure Toggle between
                              calls. Else, this feature does not work.

### Configure Toggle Between Calls

To configure Toggle between calls, perform these steps.

### SUMMARY STEPS

- enable

- configure terminal

- dsapp line call-control mode feature

- toggle-between-calls <keypad character>

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode. Enter your password, if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters the global configuration mode.

Step 3

dsapp line call-control mode feature

#### Example:

```
Device(config)#  dsapp line call-control mode feature
```

Enables the feature mode.

Step 4

toggle-between-calls <keypad character>

#### Example:

```
Device(config-dsappline-fmcode)#  toggle-between-calls #3e
```

This is an optional step if you want to configure the FAC for the toggle between calls feature. Enter the FAC you want to
                                             configure instead of the keypad character mentioned in this command syntax.

In this example, #3 is the FAC you set to enable the Toggle between calls feature.

#### Sample Configuration

```
Device(config)#dsapp line call-control mode feature
Device (config-dsappline-fmcode)#?
DSAPPLINE feature access-code configuration commands:
conference            Select call forward all feature
default               Set a command to its defaults
exit                  Exit from dsappline feature access code mode
no                    Negate a command or set its defaults
toggle-between-calls  Select code for toggle between two calls
transfer              Select code for transfer
```

### Call Back

The Call Back feature allows a caller to request a Call Back if a call is made to a busy phone or a no-answering phone.

When a caller dials an extension of another user and hears the ring back or busy tone, the caller activates callback by pressing
                              the corresponding feature access code – for example – (pound)#1. The caller hears a confirmation tone and put the phone onhook.
                              CUCM then monitors the calling and called phones and once both phones are onhook, the call manager triggers the callback tone
                              on the calling phone. If the caller picks up, then the other end also begins to ring. If the caller does not answer the phone,
                              the ringing times out and call back is cancelled.

This feature is supported only if the voice gateways that the calling and called phones are connected to, are in the same
                                          CUCM cluster. At a given point in time, only one active call back is supported.

### Configure Call Back

To configure the Call Back feature and the Call Back settings, perform these steps.

### SUMMARY STEPS

- enable

- configure terminal

- dsapp line feature callback

- In the dspapp line feature callback mode, specify the callback parameters by specifying the values for these keywords:

- On the CUCM UI, choose System > Service Parameters .

- From the Service drop-down list, choose the Cisco CallManager (Active) service.

- Ensure the Call Back Enabled Flag option is set to True on Clusterwide Parameters (Feature – Call Back) the screen.

- Restart the Cisco CallManager service for this parameter change to take effect.

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode. Enter your password, if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters the global configuration mode.

Step 3

dsapp line feature callback

#### Example:

```
Device (configure)# dsapp line feature ?
access-code Specify the format of the feature access code
Callback    Specify callback parameters
```

Configures the Call Back feature.

Step 4

In the dspapp line feature callback mode, specify the callback parameters by specifying the values for these keywords:

Step 5

On the CUCM UI, choose System > Service Parameters .

Step 6

From the Service drop-down list, choose the Cisco CallManager (Active) service.

Step 7

Ensure the Call Back Enabled Flag option is set to True on Clusterwide Parameters (Feature – Call Back) the screen.

Step 8

Restart the Cisco CallManager service for this parameter change to take effect.

#### Sample Configuration

```
enable
configure terminal
dsapp line feature callback
activation-key #1
ringing-timeout 40
end
!
```

| Feature or Enhancement | Cisco IOS XE Release | Feature Description |
|---|---|---|
| Supplementary call features | Cisco IOS XE 16.12.1 | The following call features are supported from Cisco IOS XE 16.12.1: Call forward all and cancel forward all Call forward no answer/busy Call waiting and cancel call waiting Directed call park Directed call pickup Call pickup group Call pickup local Last number redial Unattended and attended call transfer Three-way conference Drop last conferee AMWI tones for voicemail Inband signaling for DTMF T.38 fax |
| Enhanced call features | Cisco IOS XE 17.15.1a | The following call features are supported from Cisco IOS XE 17.15.1a: Forward all to voice mail Hunt group login and logout Toggle between calls Call Back |

| Note | By default, FAC is disabled if you’re using an image earlier than Cisco IOS XE 17.15.1a. In this case, you must perform these
                                       steps. If you’re using Cisco IOS XE 17.15.1a or a later version, FAC is auto enabled with Auto Configuration. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password, if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters the global configuration mode. |
| Step 3 | dsapp line Example: Device(config)# dsapp line | Enters the DSAPP Line configuration mode. |
| Step 4 | feature access code Example: Device(config-dsappline)# feature access-code | Enables the voice gateway to translate the FACs dialed by analog phone users into a format that CUCM understands, thereby
                                          allowing the invocation of supplementary services like call forward, call waiting, call pickup, etc. |

| Command or Action | Purpose |
|---|---|
| show dsapp line feature codes Example: Device# show dsapp line feature codes
dsapp line feature access-code
prefix *#
call forward all *#1
call forward cancel *#2
pickup local *#5
pickup group *#7
pickup direct *#6
cancel-call-waiting **4
last-redial *#3 | Displays whether FAC is enabled and the feature codes for the call features. By default, the FAC has ‘**’ prefix which can
                                          be changed in the CLI. You can also change the default FAC in the sub-mode. |

| State | Action | Result | Response on FXS Line |
|---|---|---|---|
| Active call | Controller hookflash | Held call | Second dial tone |
| Held call and outgoing dialed, alerting, and active call | Controller on hook | Held call and active call transferred | Transfer |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password, if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters the global configuration mode. |
| Step 3 | application Example: Device(config)# application | Enters the Application Configuration mode. |
| Step 4 | service dsapp Example: Device(config-app)# service dsapp | Enables the DSAPP service. |
| Step 5 | param callWaiting TRUE Example: Device(app-global)# param callWaiting TRUE | Enables the Call Waiting feature. |

| State | Action | Result |
|---|---|---|
| Active Call | First party hookflash | Held call |
| First party held and second party active | Active call hookflash | First and second calls are bridged |
| Three-way conference | Controller on hook | Both call legs torn down |
| Three-way conference | First called party on hook | Call between controller and first called party terminated. Call between controller and second called party remains active. |
| Three-way conference | Second called party on hook | Call between controller and second called party terminated. Call between controller and first called party remains active. |
| Three-way conference | Controller hookflash | Call between controller and second called party terminated, call between controller and first called party remains. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password, if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters the global configuration mode. |
| Step 3 | application Example: Device(config)# application | Enters the Application Configuration mode. |
| Step 4 | service dsapp Example: Device(config-app)# service dsapp | Enables the DSAPP service. |
| Step 5 | param callConference TRUE Example: Device(app-global)# param callConference TRUE | Enables the Call Conferencing feature. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password, if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters the global configuration mode. |
| Step 3 | dsapp line feature voice-mail <voicemail-number> Example: Device(config)# dsapp line feature voice-mail 8356934859 | Enables forward to voicemail. Here, voicemail-number is the voice mail number where the call should be forwarded. The maximum
                                             length for this keyword is 11. When you configure the voicemail number, ensure it is real phone number. If the number you specify is not valid, the FAC dial-out
                                             forward-to-voicemail (**4) fails because CUCM cannot detect the validity of the number you specified. |
| Step 4 | forward-to-voicemail <keypad-character> Example: Device(config-dsappline-fac)# forward-to-voicemail **6 | This step is optional, and you need not perform this step if you chose the default value of **4. In this command syntax, the
                                             keypad-character is the string that a user needs to dial through their phone keypad. If you wish to change this default value,
                                             run this command and enter the new value from your phone keypad. Note To cancel the forward to voicemail functionality, run the cancel call forward all command. | Note | To cancel the forward to voicemail functionality, run the cancel call forward all command. |
| Note | To cancel the forward to voicemail functionality, run the cancel call forward all command. |

| Note | To cancel the forward to voicemail functionality, run the cancel call forward all command. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password, if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters the global configuration mode. |
| Step 3 | dsapp line feature access-code Example: Device(config)# dsapp line feature access-code | Enters the dsapp feature access code mode and configures the hunt group login and logout feature. |
| Step 4 | hunt-group login-logout <keypad-character> | This is an optional step and needs to be performed if you want to change the FAC for enabling hunt group login and logout.
                                             In this command syntax, the keypad-character is the string that a user needs to dial through their phone keypad. The default
                                             value for this feature is **8. |

| State | Action | Result | Response to FXS Line |
|---|---|---|---|
| Active call | Hookflash | Call placed on hold for the remote caller | Second dial tone for the FXS phone |
| Call on hold | Hookflash | Call is active | FXS line connects to the call |
| Call on hold and an active call | Hookflash | Active and call on hold are swapped | FXS line connects to the held call |
| Call on hold and an active call | On hook | Active call is dropped | The call that is held is active and a reminder ring is seen on the FXS line. |
| Call on hold and an active call | Call on hold goes on hook | Call on hold is dropped | No response |
| Call on hold and an active call | Active call goes on hook | Active call is dropped | Silence or no response. Reconnects to held call after the value you specify for <disc-toggle-time> expires. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password, if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters the global configuration mode. |
| Step 3 | dsapp line call-control mode feature Example: Device(config)#  dsapp line call-control mode feature | Enables the feature mode. |
| Step 4 | toggle-between-calls <keypad character> Example: Device(config-dsappline-fmcode)#  toggle-between-calls #3e | This is an optional step if you want to configure the FAC for the toggle between calls feature. Enter the FAC you want to
                                             configure instead of the keypad character mentioned in this command syntax. In this example, #3 is the FAC you set to enable the Toggle between calls feature. |

| Note | This feature is supported only if the voice gateways that the calling and called phones are connected to, are in the same
                                          CUCM cluster. At a given point in time, only one active call back is supported. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password, if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters the global configuration mode. |
| Step 3 | dsapp line feature callback Example: Device (configure)# dsapp line feature ?
access-code Specify the format of the feature access code
Callback    Specify callback parameters | Configures the Call Back feature. |
| Step 4 | In the dspapp line feature callback mode, specify the callback parameters by specifying the values for these keywords: |  |
| Step 5 | On the CUCM UI, choose System > Service Parameters . |  |
| Step 6 | From the Service drop-down list, choose the Cisco CallManager (Active) service. |  |
| Step 7 | Ensure the Call Back Enabled Flag option is set to True on Clusterwide Parameters (Feature – Call Back) the screen. |  |
| Step 8 | Restart the Cisco CallManager service for this parameter change to take effect. |  |