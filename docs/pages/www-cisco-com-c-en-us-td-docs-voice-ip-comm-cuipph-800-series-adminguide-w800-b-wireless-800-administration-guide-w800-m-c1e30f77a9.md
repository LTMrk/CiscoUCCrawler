---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-800-series-adminguide-w800-b-wireless-800-administration-guide-w800-m-c1e30f77a9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/800-series/adminguide/w800_b_wireless-800-administration-guide/w800_m_configuration-on-a-mobile-device.html
retrieved_at: 2026-08-21T09:58:44.981468+00:00
---

Cisco Wireless Phone 840 and 860 Administration Guide for Cisco Unified Communications Manager

# Cisco Wireless Phone 840 and 860 Administration Guide for Cisco Unified Communications Manager

Updated: August 13, 2026

Chapter: Cisco app configuration

## Chapter: Cisco app configuration

# Cisco app configuration

## Cisco app configuration overview

Configure the Cisco apps and their settings as required by your organization. To configure the Cisco apps, you can:

Use an Enterprise Mobility Management (EMM) application (Recommended for multiple phones)

Use the Cisco Wireless Phone Configuration Management tool (Recommended for multiple phones if you don't have an EMM application )

Use the Settings menu for each app directly on the phone (Recommended only for a small number of phones)

### Enterprise Mobility Management application interface

The following Cisco apps are on the Google Play Store. You can configure these apps through an Enterprise Mobility Management (EMM) application .

Emergency

Push to Talk (PTT)

Battery Life

Buttons

Barcode

Custom Settings

Call Quality Settings

Web API

The Barcode, Buttons, Call Quality Settings, and Custom Settings apps are OEMConfig apps. To configure these apps, your EMM
                                          must support the OEMConfig enhanced schema. If necessary, consult with your EMM support for assistance.

#### Program the Enterprise Mobility Management application

The Cisco Wireless Phone 840 and 860 is designed for environments that deploy mobile devices using an Enterprise Mobility Management (EMM) application solution such as Cisco Meraki Systems Manager . Your EMM application allows you to group devices so that you can manage them independently.

For specific directions on how to use Cisco Meraki Systems Manager to group phones, see the technical documentation .

##### Before you begin

Configure your EMM application with your domain certificate.

Link the phones to an existing or new Android for Work account to manage access to apps in the Google Play Store, including
                                          Cisco apps.

Step 1

Sign in to the EMM application .

Step 2

Set up an Android for Work account, which allows you to sequester the phones from external access and provide only those apps
                                             which your organization requires.

Step 3

Create a configuration profile that contains payloads for each configuration area required.

We recommend that you set the following minimal settings.

Restrictions : Enable use of the camera and allow app installation.

Android Restrictions :

System settings : Prevent Android Debug Bridge (ADB) access.

System settings : Prevent installation of apps from unknown sources.

Permissions : Auto grant all permissions. For more information on how Android 13 manages Cisco application permissions differently compared
                                                                        to Android 10, see Android 13 App Permissions .

Android System Apps : Specify the allowed list of Cisco apps that you download to the EMM application from Google Play Store.

Android Wallpaper : If needed, lock screen message.

Wi-Fi Profile : Configure Wi-Fi settings.

Step 4

Add an Android Enterprise Owner Account to identify the administrator who manages the phone profile.

Ensure that the account isn’t a local EMM application account, but an Android Enterprise Owner Account.

Step 5

Create identifying tags so that you can separate phones into corresponding groups.

Set groups and tags as a payload under the Profiles console. Set the Device Configuration option as Targets. However, at this point, the device only knows that it’s a certain model with a certain serial number and MAC address. After
                                                            enrollment, you can assign device tags with more granularity. You can group devices by specific owners, keywords, or device
                                                            types, depending on the desired groupings.

Step 6

Use the full name of the Cisco app (com.cisco.xxxx) to download the desired Cisco apps from the Google Play Store.

The app and the settings download to the Profile console. Each app is automatically added to the list and the app settings added as payloads.

Step 7

Configure the Cisco apps with the key-value pairs.

The key-value pairs should have downloaded with the app. Check the key-value pairs to be sure of accuracy and configure any
                                                            settings. If any key-value pairs don’t download, manually add them.

Step 8

In the EMM application console, approve the apps for distribution.

Step 9

Configure the Android Kiosk Mode to include the apps that you want.

Kiosk Mode is a launcher for the phone UI. Only approved apps are available to select for the opening screen.

### Cisco Wireless Phone Configuration Management tool for Cisco app configuration

If you are not using an Enterprise Mobility Management (EMM) application to configure the Cisco app settings, you can configure the settings for each of these Cisco apps in the Cisco Wireless Phone Configuration Management tool .

Barcode

Battery Life

Buttons

Custom Settings

PTT

Emergency

Call Quality Settings

Web API

The settings and defaults for these apps in the Cisco Wireless Phone Configuration Management tool are the same as they are on the phones.

We recommend that you disallow the Allow Notification Shade Settings Gear in the Custom Settings app in Cisco Wireless Phone Configuration Management tool . Otherwise, users can easily open apps that aren't on the Smart Launcher.

### Access the Cisco app settings on the phone

If you are not using an Enterprise Mobility Management (EMM) application or the Cisco Wireless Phone Configuration Management tool to configure the Cisco app settings, you can access the settings for each Cisco app on the phone.

Step 1

From the phone, tap the desired Cisco app.

The Buttons , Call Quality Settings , Custom Settings , and Web API apps open directly to their settings page.

Step 2

For the Barcode , Battery Life , Emergency , and PTT apps, tap the Overflow menu.

Step 3

Tap Settings .

## Emergency app

The Emergency app and Panic Button include features to monitor and alarm for emergency situations. These features are useful in lone worker environments or
                           where organizations require extra security. How you program these features depends on what type of situation you anticipate.

The Emergency app uses an accelerometer to monitor the personal motion of the phone user. If configured, the app can alarm or send emergency
                                 calls to indicate that the user is under some type of physical duress due to lack of movement, tilt, or shaking of the phone.
                                 You can configure each type of motion monitoring with varying degrees of sensitivity and amount of time to activate the warning.

The Panic Button produces a loud or silent alarm and, if programmed, instantaneously calls a preprogrammed emergency number. By default, the
                                 red button on the top of the phone is set as the Panic Button . There is also a soft Panic Button in the Emergency app.

If enabled, users may change the button actions with the Buttons app. If desired, you can disable a user's ability to change the default Panic Button in the Buttons app.

Caution

The reliability of the Emergency app and Panic Button depends on the functionality and reliability of your organization's infrastructure. The infrastructure includes the wireless
                                       LAN, the LAN, the call server, the central provisioning server, the server hosting location services, the central security
                                       system and its servers, the correct configuration of the handsets, correct installation and configuration management server,
                                       and thorough training of personnel.

We assume no responsibility and shall not be liable for any of the above dependency factors. In addition, please be aware
                                       that the Panic Button and Emergency app should not be your sole solution to any of your safety concerns and are not a substitute for safe practices and procedures.

### Emergency app configuration

You can configure the following Emergency app settings.

Motion sensor

Panic button

Emergency call

Emergency tone

#### Send emergency event notifications

If your system interfaces with a third-party security application, you can also send an emergency event notification when
                                    the alarm state triggers and cancels.

To identify the location of an alerting phone, the Emergency app must use the Web API app to interface with a method to locate the phone. Typically, they use a type of location services that use the SSID and
                                                AP location to identify the phone’s location.

Both a trigger event and a cancel event for an Emergency or Panic Button alarm send a notification to the URL.

Step 1

From the Web API settings, choose Device event notifications > Add new notification URL .

Step 2

Enter a descriptive notification name and URL of the security application.

Step 3

Check the box beside Emergency events as the type of event you are sending to this URL.

#### Motion sensor

When an Emergency motion alarm is triggered, the phone displays a warning screen for a configurable number of seconds. If
                                    the user does not cancel the warning, the alarm state occurs and, if configured, the phone places an emergency call.

The motion detectors function accurately only when the phone is secured to the body. The user is not able to turn off the
                                    Emergency application without turning off the phone. Configure the Snooze option to allow temporary suspension of Emergency
                                    monitoring. Emergency monitoring is also suspended when the phone is connected to the USB charger.

The three conditions of motion are:

No movement —the phone remains still for a configurable number of seconds, potentially indicating that the user is not moving. A certain
                                          amount of motion is normal, even when sitting, but no motion at all can indicate that a person is unable to move due to unconsciousness
                                          or being restrained.

Tilt —the phone is not vertical for a configurable number of seconds, indicating that the user has fallen or is in some other position
                                          than sitting, standing, or walking. The tilt condition may indicate that the user is leaning over to pick up something.

Running —the phone detects shaking, which may indicate that the user is moving quickly or suffering a seizure.

Based on your organization's needs and environmental conditions, you can configure all phones with the same settings, or you
                                    can configure the phones in groups or individually.

The user has no control over these settings, so you must configure the settings to provide the most secure response without
                                    annoying the user with excessive warnings.

##### Motion sensor settings

Use the following settings to configure the motion sensor.

Field

Field type or choices

Default

Description

Monitoring

On

Off

Off

Enables Emergency motion monitoring.

Enable this setting to allow any of the motion settings to trigger an alarm.

No movement sensitivity

Disabled

Level 1 (lowest)

Level 2

Level 2

Level 2

Level 2

Level 2

Level 7 (highest)

Disabled

Sets the degree of motionlessness or lack of any type of movement of the phone to trigger an alarm.

Level 1 is the least sensitive. An alarm triggers a warning if the user is moving some, but below the normal threshold.

Level 7 is the most sensitive. An alarm triggers if the user is almost completely still.

No movement timeout (seconds)

Integer 10–300

30

Sets the length of time in seconds that the user would have to maintain the configured degree of stillness (or a more severe
                                                   degree).

Tilt sensitivity

Disabled

Level 1 (lowest)

Level 2

Level 2

Level 2

Level 2

Level 2

Level 7 (highest)

Disabled

Sets the nonvertical position of the phone that is required to trigger an alarm.

Level 1 is the least sensitive. An alarm triggers if the user is nearly prone.

Level 7 is the most sensitive. An alarm triggers if the user was leaning somewhat.

Tilt timeout (seconds)

Integer 10–300

10

Sets the length of time in seconds that the user would have to maintain the configured degree of tilt (or a more severe degree).

Running sensitivity

Disabled

Level 1 (lowest)

Level 2

Level 2

Level 2

Level 2

Level 2

Level 7 (highest)

Disabled

Sets the amount of shaking of the phone that is required to trigger an alarm.

Level 1 is the least sensitive. An alarm triggers if there is quite a bit of jostling.

Level 7 is the most sensitive. An alarm triggers if the user walks quickly or runs.

Running timeout (seconds)

Integer 10–60

10

Sets the length of time in seconds that the user would have to maintain the configured degree of shaking (or a more severe
                                                   degree).

Snooze timeout (seconds)

Integer 0–300

0

The Snooze feature allows the user to temporarily suspend Emergency motion monitoring. To activate this feature, set the timeout
                                                   in seconds 1–300. By default, the Snooze feature is disabled (set to 0).

Warning timeout (seconds)

Integer 10–60

10

Sets the warning timeout in seconds. This is the amount of time between the trigger of the warning and the alarm state. In
                                                   the alarm state, an emergency call might be placed or an alarm is sent to an external security application.

#### Panic Button settings

When the user activates an enabled Panic Button, an alarm displays on the phone until the user cancels it. By default, the
                                    Panic Button is disabled.

Use the following settings to configure the Panic Button.

Field

Field type or choices

Default

Description

Panic button

Disabled

Long press

Two short presses

Two short or one long press

Disabled

Defines the sequence that the user uses to trigger the Panic Button alarm.

You can also disable the Panic Button alarm from this setting.

Panic button silent alarm

On

Off

On

Enables the silent alarm, which disables the loud local alarm that sounds when a user triggers the Panic Button . If the user is under duress, a silent alarm doesn't alert the assailant.

Panic button alarm timeout

Integer 5–30

5

Sets the amount of time, in seconds, to time out the panic alarm.

##### Sample Panic Button configuration options

You can set the Panic Button to perform various actions based on the user's needs.

Option

Description

Settings

Local panic alarm without an emergency phone call

Allows the user to alert people nearby with a loud alarm, but does not place an emergency call.

The loud alarm helps people to locate the user, or scares away any potential threats.

Set the Panic button silent alarm to Off.

Set the Emergency call to Off.

Silent duress alarm with or without an emergency phone call

Allows the user to silently send an alarm signal for help.

If the user also must place an emergency call, you can turn off the speakerphone option to maintain the silence.

If the Panic Button automatically pushes an alert to an external security application, you do not need to set an emergency
                                                   call.

Set the Panic button silent alarm to On.

Set the Emergency call to either On or Off.

If necessary, set the Emergency dial force speaker to Off.

Incapacitation panic alarm with an emergency phone call

Allows an incapacitated user to place an emergency call.

An incapacitated user may not be able to hold the phone to their ear. To ensure that both parties can hear the phone call
                                                   audio, set the alarm to be silent and turn on the forced speakerphone option.

Set the Panic button silent alarm to On.

Set the Emergency call to On.

Set the Emergency dial force speaker to On.

#### Emergency call settings

You can configure the Panic Button to place an emergency call when the user activates the Panic Button. By default, the emergency
                                    call is disabled.

Use the following settings to configure emergency calls.

Field

Field type or choices

Default

Description

Emergency call

On

Off

Off

Enables the phone to call the emergency number configured in Emergency dial number , if the user triggers the Panic Button or an Emergency motion alarm.

Emergency dial force speaker

On

Off

On

Enables the speakerphone when the phone places an emergency call. This setting allows the user to be in handsfree mode in
                                                case they can't hold the phone to their ear.

Emergency dial number

Any valid TN

911

911

Defines the number that the phone dials when the user triggers the Panic Button or an Emergency motion alarm.

You must configure and enable the other related settings for the emergency call to occur.

Follow any dial plan rules when you enter the emergency dial number.

#### Emergency tone settings

You can set the emergency warning and alarm tones from the list of available phone ringtones.

Use the following settings to configure the emergency tones.

Field

Field type or choices

Default

Description

Warning tone

Default notification sound

None

List of available warning tones

Default (Pixie Dust)

Configures the tone to play during a warning period. This tone plays at a gradually increasing volume. Tones play even if
                                                the user silences the handset.

There is no warning period for the Panic Button; it goes straight to the alarm state.

Alarm tone

Default alarm sound

None

List of available alarm tones

Default (Cesium)

Configures the tone to play when a Panic Button press or Emergency alarm triggers. This tone plays at a high volume. Tones
                                                play even if the user silences the handset.

### Emergency app and Panic Button training

Ensure that you train your users about how to use the Emergency app and Panic Button within your organization. Use the following list as a guide:

Monitoring

Which motion detection sensors are active? What is the degree of sensitivity? What is the timeout? How long is the warning
                                             state?

What happens when an alarm is triggered? Is there an emergency call? Is there an external security application, and if so,
                                             what does it do?

Is the Snooze option configured? If so, for how long?

Panic Button

How do you activate the Panic Button? With a long press, two short presses, or either?

If you press the Panic Button, will the phone place an emergency call?

If you press the Panic Button, will it sound an alarm through the speakerphone?

If the phone places an emergency call, does the audio come through the speakerphone?

## Push to Talk app

The Push to Talk ( PTT ) app is a radio multicast app, where the phones can operate in a group broadcast mode, like walkie-talkies.

For the PTT functionality to work on your network, you must enable the multicast feature on your access points. For detailed information,
                              see the Cisco Wireless Phone 840 and 860 Deployment Guide .

By default, PTT is disabled. As an administrator, you:

Enable or disable PTT mode.

Subscribe users to some or all the 25 available channels to receive, and optionally transmit, broadcasts.

### User settings for Push to Talk

The user controls the following Push to Talk ( PTT ) settings on the phone.

Field

Field type or choices

Default

Description

PTT volume

Integer 0–100

20

Controls the volume percentage of the PTT volume.

Default channel

Channel 1 - ALL

Channels that have both Channel can transmit and Channel subscription Admin settings set to Yes

Channel 1 - ALL

The user sets their default channel. The default channel is the channel that broadcasts when the user presses the programmed PTT button or the Talk button in the PTT app.

A user can set a channel as their default channel only if they are subscribed to the channel and are able to transmit on the
                                             channel.

### Admin settings for Push to Talk

Use the following Admin settings to configure Push to Talk ( PTT ).

Field

Field type or choices

Default

Description

Enable PTT

On

Off

Off

PTT must be enabled for it to be activated on the selected handsets.

Allow PTT transmission when phone is locked

On

Off

Off

From release 1.3(0) onward, you can set PTT to transmit even if the phone is locked.

Username

Text

Anonymous

This is the caller ID that displays on the broadcast. Usually set at Device or Group level. If nothing is entered, the default
                                             is Anonymous .

Multicast address

Domain name or IP address

224.0.1.116

Defines the multicast address for broadcast traffic.

Codec

G.711Mu

G.726

G.726

Defines the codec.

Channel setup

You can set up to 25 PTT channels. By default, the Channel #1 label defaults to ALL, and its transmit and subscription options
                                             are set to Yes.

Use the following Channel setup settings to configure the desired PTT channels.

Field

Field type or choices

Default

Description

Channel # n label

String

For Channel # 1: ALL

For Channel #2-25: Blank

Allows you to enter a label for the channel.

You can enter a label with more than 15 characters, but a long label truncates when it displays on the handset.

Channel can transmit

Yes

No

For Channel # 1 - ALL: Yes

For Channel #2-25: No

Enables a user to transmit on the channel.

Channel subscription

Yes

No

For Channel # 1 - ALL: Yes

For Channel #2-25: No.

Subscribes a user to the channel so that they can receive broadcasts.

## Battery Life app

By default, battery monitoring is disabled. When you enable battery life monitoring, the Battery Life app dashboard displays the following:

Battery serial number

Battery capacity

Temperature

Health

Charging status

Voltage

Battery type

Charge cycle completed

A low battery warning notification displays on the screen if the percentage of remaining battery life is below the set Low battery threshold .

As administrator, you can also enable sound and vibration for the low battery alarm.

The Cisco Wireless Phone 860 and Cisco Wireless Phone 860S have an internal secondary battery, which operates the phone during
                                          a hot swap. The Battery Life app dashboard displays the general status of the internal battery. For more information about the secondary battery, you
                                          can tap Open additional metrics and options .

The The Cisco Wireless Phone 840 and 840S do not have an internal battery.

For 1.7(0) or later, if the number of charge cycles exceed the specified maximum count, you receive a notification to replace
                              the battery. Make sure to replace the battery immediately after you receive a notification for better performance.

### User settings for Battery Life

The user controls the following Battery Life settings.

Alarm volume

Integer 0–100

50

Controls the volume percentage of the low battery alarm.

This is a user-controlled setting.

### Admin settings for Battery Life

Use the following Admin settings to configure the Battery Life app.

Field

Field type or choices

Default

Description

Alarm volume

Integer 0–100

50

Controls the volume percentage of the low battery alarm.

This is a user-controlled setting.

Enable battery monitoring

On

Off

Off

Enables or disables battery monitoring. When disabled, the low battery alarm does not sound and the battery life details such
                                             as the serial number, capacity, temperature, and charging status do not display.

Vibrate

On

Off

Off

Causes the phone to vibrate if the battery alarm is active and battery monitoring is enabled.

Sound

On

Off

Off

Enables sound for the battery alarm, if the battery alarm is active and battery monitoring is enabled.

Alarm tone

Default alarm sound

None

List of available alarm tones

Default (Cesium)

Defines the battery alarm tone.

Low battery threshold

15%

20%

15%

Defines the percentage of remaining battery life to trigger the alarm.

Snooze time

1 min

2 min

3 min

4 min

5 min

2 min

Defines the number of minutes the alarm is silenced when the user snoozes the battery life alarm.

## Buttons app

The Buttons app allows you to program the buttons on their phone. You can disable user control for all buttons or for specific buttons.
                           For example, you can disable user control of the Programmable Emergency button, to ensure that users can always access that feature.

### Programmable buttons

The following illustrations and table show the programmable buttons on the phone.

The programmable buttons for the Cisco Wireless Phone 840 and Cisco Wireless Phone 860 are not in the same location. Also, the Cisco Wireless Phone 840 and 840S don't have a Fingerprint button.

Callout

Programmable button

1

Left button

2

Right button

3

Top

4

Volume up

5

Volume down

6

Fingerprint—For Cisco Wireless Phone 860 and 860S only.

### Buttons settings

Through the Buttons app settings, you can:

Enable or disable the user's ability to change some or all programmable buttons.

Change the default programmable button actions.

Use the following settings to configure the buttons.

Default

Enabled

Disabled

Enabled

Enables the user to change the Left button .

No action

Home key

Back key

Menu key

PTT

Emergency

Volume up

Volume down

Run application

Open URL

Scanner (for 800S phones only)

Custom 1

Custom 2

Custom 3

Custom 4

For phones with a barcode scanner: Scanner

For phones without a barcode scanner: No action

Allows the user to control the button action if you enable Left button user assigned .

Enabled

Disabled

Enabled

Enables the user to change the Right button .

No action

Home key

Back key

Menu key

PTT

Emergency

Volume up

Volume down

Run application

Open URL

Scanner (for 800S phones only)

Custom 1

Custom 2

Custom 3

Custom 4

PTT

Allows the user to control the button action if you enable Right button user assigned .

Enabled

Disabled

Enabled

Enables the user to change the Top button.

No action

Home key

Back key

Menu key

PTT

Emergency

Volume up

Volume down

Run application

Open URL

Scanner (for 800S phones only)

Custom 1

Custom 2

Custom 3

Custom 4

Emergency

Allows the user to control the button action if you enable Top button user assigned .

Fingerprint button user assigned

Enabled

Disabled

Enabled

For Cisco Wireless Phone 860 and Cisco Wireless Phone 860S only.

Enables the user to change the Fingerprint button.

No action

Home key

Back key

Menu key

PTT

Emergency

Volume up

Volume down

Run application

Open URL

Scanner (for 800S phones only)

Fingerprint

Custom 1

Custom 2

Custom 3

Custom 4

Fingerprint

For Cisco Wireless Phone 860 and Cisco Wireless Phone 860S only.

Allows the user to control the button action if you enable Fingerprint button user assigned .

Volume up button user assigned

Enabled

Disabled

Enabled

Enables the user to change the Volume up button.

No action

Home key

Back key

Menu key

PTT

Emergency

Volume up

Volume down

Run application

Open URL

Scanner (for 800S phones only)

Custom 1

Custom 2

Custom 3

Volume up

Allows the user to control the button action if you enable Volume up button user assigned .

Volume down button user assigned

Enabled

Disabled

Enabled

Enables the user to change the Volume down button.

No action

Home key

Back key

Menu key

PTT

Emergency

Volume up

Volume down

Run application

Open URL

Scanner (for 800S phones only)

Custom 1

Custom 2

Custom 3

Volume down

Allows the user to control the button action if you enable Volume down button user assigned .

### Set a button to run an application

You can configure a programmable button to open any app that is on the phone.

In the Enterprise Mobility Management (EMM) application , specify both the app package name and the app activity name in the configuration string:

```
<package name>/<package name>.<activity name>
```

When you include the app activity name, it allows you to push that configuration to the phones before you install the named
                                 app on the phones.

If you use only the app package name and the app is not yet on the phone, the Buttons app can't apply that setting. When you do install the app later, and the user presses the button, the app will not launch.

Step 1

In the EMM application, select Run application .

Step 2

Enter the package name of the app and the activity name of the screen within the app.

For example, the package name for the Cisco Phone app is com.cisco.phone . The package name plus the dialer activity name is com.cisco.phone/com.cisco.phone.activities.Dialer .

### Answer and end calls using the hardware buttons

For release 1.10(3) or later, you can answer and disconnect the calls by pressing the hardware buttons instead of using the
                              on-screen controls. By default, this feature doesn’t come enabled. So, you have to turn it on manually using the Buttons application.

#### Set a button to answer a call

To set a button to answer a call:

Step 1

Access the Buttons app.

Step 2

In the Buttons settings menu, select the button that you want to use to answer a call.

Step 3

Choose Custom in the resulting action menu.

Step 4

In the Enter custom intent popup window that appears enter one of the following strings in the Action down field (field text is case-sensitive):

To send the audio to the phone’s earpiece (shown in the screenshot above):

```
com.cisco.intent.action.ANSWER_CALL_EP
```

To use the phone as a speakerphone:

```
com.cisco.intent.action.ANSWER_CALL_SP
```

To send the audio to a wired headset:

```
com.cisco.intent.action.ANSWER_CALL_HS
```

Step 5

Leave the remaining fields empty.

Step 6

Tap OK to save your settings.

#### Set a button to end or decline a call

To set a button to end the current call or decline an incoming call:

Step 1

Access the Buttons app.

Step 2

In the Buttons settings menu, select the button that you want to answer a call.

Step 3

Choose Custom in the resulting action menu.

Step 4

In the Enter custom intent popup window that appears enter the following string in the Action down field (field text is case-sensitive):

```
com.cisco.intent.action.DECLINE_CALL
```

Step 5

Leave the remaining fields empty.

Step 6

Tap OK to save your settings.

### Turn ON and OFF flaslight using the hardware buttons

For release 1.10(3) or later, you can turn ON and OFF the flashlight by pressing the hardware buttons.

#### Set a button to control the flashlight

To set a button to turn the flashlight on when the button is pressed and held, and turn the flashlight off when the button
                                    is released:

Step 1

Access the Buttons app.

Step 2

In the Buttons settings menu, select the button you that you want to control the flashlight.

Step 3

Choose Custom in the resulting action menu.

Step 4

In the Enter custom intent popup window that appears enter the following in the Action down and Action up fields (field text is case-sensitive):

```
com.cisco.intent.action.FLASHLIGHT_ONOFF
```

Step 5

In the Extras for action down field enter the following:

```
boolean:flashlight=true
```

Step 6

In the Extras for action up field enter the following:

```
boolean:flashlight=false
```

Step 7

Tap OK to save your settings.

#### Set a button to toggle the flashlight

To set a button to toggle the flashlight on and off:

Step 1

Access the Buttons app.

Step 2

In the Buttons settings menu, select the button you that you want to control the flashlight.

Step 3

Choose Custom in the resulting action menu.

Step 4

In the Enter custom intent popup window that appears enter the following in the Action down and Action up fields (field text is case-sensitive):

```
com.cisco.intent.action.FLASHLIGHT_ONOFF
```

Step 5

Leave the remaining fields empty.

Step 6

Tap OK to save your settings.

### Cisco app package names

The following are the package names for the Cisco apps.

Cisco app

Cisco app package name

Barcode

com.cisco.barcode.service

Battery Life

com.cisco.batterylife

Buttons

com.cisco.buttons

Call Quality Settings

com.cisco.callquality

Cisco Phone

com.cisco.phone

Custom Settings

com.cisco.customsettings

Diagnostics

com.cisco.diagnostics

Emergency

com.cisco.emergency

Logging

com.cisco.logging

PTT

com.cisco.ptt

System Updater

com.cisco.sysupdater

Sound Stage

com.cisco.soundstage

Web API

com.cisco.webapi

The Smart Launcher and Device Policy Controller apps are not on the Google store and are available only through the Cisco
                                             Wireless Phone Configuration Management tool.

## Barcode app

The Cisco Wireless Phone 840S and Cisco Wireless Phone 860S have a built-in barcode scanner. The Cisco Wireless Phone 840 and Cisco Wireless Phone 860 don't have a barcode scanner.

By default, the barcode scanner is enabled along with all supported symbologies. As an administrator, you control the General settings , Default settings , and ScanFlex settings of the Barcode app.

As an administrator, you can:

Enable and disable barcode scanning.

Decide which symbologies to deploy.

Set audible acknowledgments of a scan.

Set the intensity of the scan light.

Set the Enter key to move to the next field to be populated by scanning.

Enable automatic enter of carriage return.

Test scan barcodes before you give the phones to users.

### Barcode symbologies

The Cisco Wireless Phone 840S and 860S barcode scanners support the following barcode symbologies.

Aztec

Codabar

Interleaved 2 of 5

CCA EAN-128

Code 11

ISBT-128

CCA EAN-13

Code 128

ISBT-128 Con

CCA EAN-8

Code 32

Macro PDF

CCA GS1 DataBar Expanded

Code 39 Full ASCII

Macro QR

CCA GS1 DataBar Limited

Code 39 Trioptic

Matrix 2 of 5

CCA GS1 DataBar-14

Code 93

Micro PDF

CCA UPC-A

DataMatrix

Micro QR

CCA UPC-E

EAN-128

MSI

CCB EAN-128

EAN-13

PDF-417

CCB EAN-13

EAN-13 + 2 Supplemental

QR Code

CCB EAN-8

EAN-13 + 5 supplemental EAN-8

UPC-A

CCB GS1 DataBar Expanded

EAN-8

UPC-A + 2 Supplemental

CCB GS1 DataBar Limited

EAN-8 + 2 Supplemental

UPC-A + 5 supplemental

CCB GS1 DataBar-14

EAN-8 + 5 supplemental

UPC-E0

CCB UPC-A

GS1 128

UPC-E0 + 2 Supplemental

CCB UPC-E

GS1 DataBar Expanded

UPC-E0 + 5 supplemental

CCC EAN-128

GS1 DataBar Limited

GS1 DataBar-14

Han Xin

### General settings for the Barcode app

Use the following settings to enable or disable the barcode scanner and configure general scan settings such as sounds and
                                 vibration.

Default

On

Off

On

Enables the barcode scanner.

Allow scan on screen lock (Only for Cisco Wireless Phone 860 only (from version 2.1(0) and later)

On

Off

On

Allows barcode scanning while the phone is locked.

0.5 seconds to 9.9 seconds

5

Sets the amount of time for the decode session timeout.

On

Off

On

Sets the phone to vibrate on scan.

On

Off

On

Sets the phone to produce a sound on scan.

Low pitch single beep

Low pitch double beep

High pitch double beep

Low pitch single beep

Sets the barcode scan tone.

5

Sets the illumination power of the barcode scanner.

Allow URL redirection to browser (Only for Cisco Wireless Phone 860 only (from version 2.1(0) and later)

On

Off

On

Allows URL redirction.

### Default settings for the Barcode app

You can set the following default settings for the Barcode app.

#### Data manipulation settings

Use the following settings to configure any rules about how to manipulate the scanned data, such as automatically adding or
                                 striping data.

Default

Enable AIM codes or symbol id

Disable

Enable AIM codes

Enable symbol id

Disable

Prefixes AIM code or symbol id before data.

The AIM code is an industry standard 3-character identifier that provides information about the symbology that is generated
                                             by the decoder of a scanner. The code is prepended to the scanned barcode and may be employed by keyboard injection and the
                                             data sent through the intent.

Automatic carriage return

On

Off

Off

Adds an Enter when inject text to an input field.

Automatic Tab

On

Off

Off

Adds a Tab at the end of an injected barcode value.

Trim barcode data

On

Off

Off

Removes any trailing or leading whitespaces from a scanned barcode data.

Strip characters from left

Integer

0

Strips this number of characters from the left (as displayed on screen) of the barcode data.

Only positive integers allowed.

Strip characters from right

Integer

0

Strips this number of characters from the right (as displayed on screen) of the barcode data.

Only positive integers allowed.

Prepend String

Prepends a string to the scanned barcode data.

Append String

Appends a string to the scanned barcode data.

#### Custom intent settings

Use the following settings to configure any custom intent settings.

Default

Disable

Stat activity

Start service

Start foreground service

Send broadcast

Disable

Choose intent delivery method.

Intent action

String

Enter intent action.

Enter intent category.

#### Symbology settings

Use the following settings to enable or disable individual barcode symbologies and their related settings. By default all
                                 supported symbologies are enabled.

The following table describes the default settings for the Aztec symbology.

Default

On

Off

ON

Enables or disables the symbology.

Regular

Inverse

Both

Regular

Sets the decoding.

The following table describes the default settings for the Codabar symbology.

Default

On

Off

ON

Enables or disables the symbology.

5

Sets the Codabar length.

On

Off

OFF

Strips start and stop characters.

The following table describes the default settings for the Code 11 symbology.

Default

Code 11

On

Off

ON

Enables or disables the symbology.

Code 11 check digit verification

Disable check digits

One check digit

Two check digits

Disable check digits

Enables or disables check digit verification.

On

Off

OFF

Enables or disables transmit.

To transmit, enable verification.

The following table describes the default settings for the Code 32 symbology.

Default

On

Off

ON

Enables or disables the symbology.

Enable Code 39 to enable Code 32.

The following table describes the default settings for the Code 39 symbology.

Default

On

Off

ON

Enables or disables the symbology.

Enable Code 39 to enable Code 32.

Enable Code 39 check digit verification

On

Off

OFF

Enables or disables check digit verification.

Enable transmit Code 39 check digit

On

Off

OFF

Enables or disables transmit.

Enable Code 39 full ASCII conversion

On

Off

OFF

Enables or disables full ASCII conversion.

The following table describes the default settings for the Code 93 symbology.

Default

On

Off

ON

Enables or disables the symbology.

The following table describes the default settings for the Code 128 symbology.

Default

On

Off

ON

Enables or disables the symbology.

The following table describes the default settings for the Data Matrix symbology.

Default

On

Off

ON

Enables or disables the symbology.

Never

Mirror

Both

Never

Sets mirror images.

Regular

Inverse

Both

Regular

Sets decoding.

The following table describes the default settings for the EAN 8 symbology.

Default

On

Off

ON

Enables or disables the symbology.

On

Off

OFF

Enables or disables conversion to EAN 13.

On

Off

OFF

Enables or disables transmit.

The following table describes the default settings for the EAN 13 symbology.

Default

On

Off

ON

Enables or disables the symbology.

The following table describes the default settings for the GS1 DataBar symbology.

Default

On

Off

ON

Enables or disables the symbology.

On

Off

ON

On

Off

ON

On

Off

ON

The following table describes the default settings for the GS1 128 symbology.

Default

On

Off

ON

Enables or disables the symbology.

The following table describes the default settings for the Han Xin symbology.

Default

On

Off

ON

Enables or disables the symbology.

The following table describes the default settings for the Interleaved 2 of 5 symbology.

Default

On

Off

ON

Enables or disables the symbology.

Enable Interleaved 2 of 5 quiet zone

On

Off

OFF

Enables or disables quiet zone.

Disable

USS

OPCC

Disable

Enables or disables check digit verification.

Enable transmit Interleaved 2 of 5 check digit

On

Off

OFF

Enables or disables transmit.

One discrete length

Two discrete lengths

Length within range

Any length

One discrete length

Governs the usage of the two integer fields that follow. For Two discrete lengths and Length within range , it does not matter which value is in which field.

Set Interleaved 2 of 5 length 1 (0 to 55)

14

Applicable for all scheme choices except Any length , which ignores it.

Default value applies only to One discrete length .

Set Interleaved 2 of 5 length 2 (0 to 55)

0–55

0

Applicable for Two discrete lengths and Length within range only.

The following table describes the default settings for the ISBT 128 symbology.

Default

On

Off

ON

Enables International Society of Blood Transfusion (ISBT) 128 symbology.

Disable

Enable

Autodiscriminate

Disable

Disable ISBT Concatenation: The device does not concatenate pairs of ISBT codes it encounters.

Enable ISBT Concatenation: There must be two ISBT codes for the device to decode and perform concatenation. The device does
                                             not decode single ISBT symbols.

Autodiscriminate ISBT Concatenation: The device decodes and concatenates pairs of ISBT codes immediately. If only a single
                                             ISBT symbol is present, the device must decode the symbol the number of times set via ISBT Concatenation Redundancy before
                                             transmitting its data to confirm that there is no additional ISBT symbol.

On

Off

ON

If you enable ISBT Concatenation, enable Check ISBT Table to concatenate only those pairs found in this table.

10

With ISBT Concatenation set to Autodiscriminate, this option sets the number of times the device must decode an ISBT symbol
                                             before determining that there is no additional symbol.

The following table describes the default settings for the Matrix 2 of 5 symbology.

Default

On

Off

ON

Enables or disables the symbology.

On

Off

OFF

Enable transmit Matrix 2 of 5 check digit

On

Off

OFF

Enables or disables transmit.

The following table describes the default settings for the Micro PDF symbology.

Default

On

Off

ON

Enables or disables the symbology.

The following table describes the default settings for the Micro QR symbology.

Default

On

Off

ON

Enables or disables the symbology.

The following table describes the default settings for the MSI Plessey symbology.

Default

On

Off

ON

Enables or disables the symbology.

One Digit

Two Digits

One digit

On

Off

OFF

Enables or disables transmit.

MOD 10/MOD11

MOD 10/MOD10

MOD 10/MOD10

The following table describes the default settings for the PDF 417 symbology.

Default

On

Off

ON

Enables or disables the symbology.

The following table describes the default settings for the QR symbology.

Default

On

Off

ON

Enables or disables the symbology.

Regular

Inverse

Both

Regular

Sets decoding.

The following table describes the default settings for the UPC-A symbology.

Enable EAN/UPC supplementals per option in Administrative settings to enable supplementals for UPC-A or UPC-E or both.

Default

On

Off

ON

Enables or disables the symbology.

On

Off

ON

Enables or disables transmit.

No preamble:0

System character

System character and country code

System character

Sets transmit preamble.

The following table describes the default settings for the UPC-E symbology.

Enable EAN/UPC supplementals per option in Administrative settings to enable supplementals for UPC-A or UPC-E or both.

Default

On

Off

ON

Enables or disables the symbology.

Enable transmit UPC-E check digit

On

Off

ON

Enables or disables transmit.

No preamble

System character

System character and country code

System character

Sets transmit preamble.

Enable convert UPCE to UPCA

On

Off

OFF

Enables or disables conversion.

The following table describes the default settings 1D barcode.

Default

Inverse 1D Decoding

Dark on light

Light on dark

Either

Dark on light

Sets decoding.

The following table describes supplemental symbology settings.

Default

Supplemental setting for UPCA, UPCE and EAN barcodes

Disable

Enable

Disable

Enables or disables supplemental setting.

The following table describes more symbology settings.

Default

Disable

Enable

Disable

Global to both EAN 8 and EAN 13.

Dark on light

Either

Light on dark

Dark on light

Sets polarity.

#### Replace control characters settings

As needed, use the following replace control character settings to replace certain ASCII0-31 control character keys in a barcode
                                 string with a space or punctuation.

Default

Use control character

SPACE

List of Latin punctuation or symbols

SPACE

The following table lists the control characters that you can replace with a space or punctuation.

Control character

Control character decimal

NULL (NUL)

0

Start of Header (SOH)

1

Start of Text (STX)

2

End of Text (ETX)

3

End of Transmission (EOT)

4

Enquiry (ENQ)

5

Acknowledge (ACK)

6

Bell (BEL)

7

Backspace (BS)

8

Horizontal Tab (HT)

9

Line Feed (LF)

10

Vertical Tab (VT)

11

Form Feed (FF)

12

Carriage Return (CR)

13

Shift Out (SO)

14

Shift In (SI)

15

Data Link Escape (DLE)

16

Data Control 1 (DC1)

17

Data Control 2 (DC2)

18

Data Control 3 (DC3)

19

Data Control 4 (DC4)

20

Negative ACK (NAK)

21

Synchronize (SYN)

22

End Text Block (ETB)

23

Cancel (CAN)

24

End Message (EM)

25

Substitute (SUB)

26

Escape (ESC)

27

File Separator (FS)

28

Group Separator (GS)

29

Record Separator (RS)

30

Unit Separator (US)

31

The following table lists the punction that you can use to replace control characters.

Latin punctuation or symbol

Description

### ScanFlex

The Barcode service uses ScanFlex, a feature that allows the Barcode service to support custom data manipulation for individual
                                 applications.

Using the barcode settings and the Enterprise Mobility Management (EMM) application interface, you can group applications using barcode service into profiles which contain the exact package names that the
                                 app developers provide. Within each profile, you can enable required symbologies and configure custom data manipulation settings.
                                 When the given app is identified in the foreground, the barcode scanner only scans the symbologies that you program for that
                                 identified app.

ScanFlex allows custom intents to provide more specificity. For custom intents to function, the third-party application must
                                 be in the foreground. Some common intent delivery methods are:

Start activity

Start service

Start foreground service

Send broadcast

Custom intents and keyboard emulation use the manipulated barcode data.

#### ScanFlex settings

Set the following for each ScanFlex application or activity that you add.

Default

String

Enter a name for the application or activity.

If more than one name, use a comma to separate names.

Set desired symbology settings for the application or activity.

Select desired symbologies, and set their data manipulation and custom intent settings.

Select desired symbologies, and set custom actions and parameters.

#### Actions for advanced data formatting

In the ScanFlex Advanced data formatting settings, you can set the scanner to perform up to ten different actions on a scanned string. You can set the actions to
                                    happen in any order, and you may repeat an action if needed.

Each action has two parameters that are associated with it: parameter 1 and parameter 2. The parameter fields may not be necessary
                                    for some actions.

The following table describes actions that move the cursor.

Action

Cursor action description

Directions for parameters

Move forward

Move the cursor forward by n spots.

Enter n in Parameter 1.

Move back

Move the cursor backward by n spots.

Enter n in Parameter 1.

Move to beginning

Move the cursor to the beginning of the string.

No parameter required.

Move to end

Move the cursor to the end of the string.

No parameter required.

Move to beginning of sub-string

Move the cursor to the beginning of a sub-string.

Enter the sub-string in Parameter 1.

Move to the end of sub-string

Move the cursor to the end of a sub-string.

Enter the sub-string in Parameter 1.

The following table describes actions that don't move the cursor.

Action

Action description

Directions for parameters

Trim whitespace

Remove leading or trailing whitespaces.

No parameter required.

Remove all whitespace

Remove all whitespaces.

No parameter required.

Remove all leading zeros

Remove leading zeros on the left of the string.

No parameter required.

Pad zeros at beginning

Add n zeros at the beginning.

Enter n in Parameter 1.

Replace first sub-string

Replace the first encountered sub-string in the scanned string.

Enter the sub-string that you want to replace in Parameter 1, and enter the new sub-string in Parameter 2.

Replace all sub-strings

Replace all encountered sub-string in the scanned string.

Enter the sub-string that you want to replace in Parameter 1, and enter the new sub-string in Parameter 2.

Remove characters

Remove characters encountered in the string.

Enter the character in Parameter 1.

Add text

Add text

Enter the text in Parameter 1.

Add code

Add character as integer code.

Enter integer code of the desired character in Parameter 1.

Add tab

Add a Tab from the current position of cursor.

ScanFlex uses a built-in pause after Tab; therefore, you do not need to manually add a pause.

No parameter required.

Add enter

Add an Enter at the current position of the cursor.

ScanFlex uses a built-in pause after Enter; therefore, you do not need to manually add a pause.

No parameter required.

### Test scan a barcode

Before you use the barcode scanner for the first time, check that the scanner is properly configured to scan your barcode
                                 type.

#### Before you begin

Use the small tab to remove the plastic cover on the barcode scanner.

Use the Buttons app to program a button as the Scanner .

By default, the top-left button of the Cisco Wireless Phone 860S is set to Scanner .

By default, the bottom-left button of the Cisco Wireless Phone 840S is set to Scanner .

Step 1

Access the Barcode app.

Step 2

Tap the Overflow menu.

Step 3

Tap Test scan .

Step 4

From the Barcode screen, tap the barcode scanner button.

Step 5

Point the barcode reader 1–18 inches (2.5–46 centimeters) from the barcode that you want to scan.

Step 6

Press and hold the programmed Scanner button with the light shining across the entire barcode symbol until the light turns off and you hear a beep.

Step 7

Tap the barcode search button to find data about the scanned barcode.

## Custom Settings app

The Custom Settings app provides phone control settings. It includes:

User restrictions, where you can grant or restrict access to certain phone settings for the phone user.

General administrative phone settings, such as time, device, sleep, touch, sound, and wallpaper settings.

### User restrictions in Custom Settings

By default, all the user restrictions are on, which means that users can control these settings on their phones. If you don't
                                 want users to control certain settings, you can change these settings to Off.

#### User restrictions for Wi-Fi and airplane mode

The following table describes the user restriction settings that are related to Wi-Fi and airplane mode.

Allow Wi-Fi toggle

Allow Internet Toggle (Only For Cisco Wireless Phone 860 only (from version 2.1(0) and later)

On

Off

On

If enabled, and if the Allow quick settings tiles is enabled, the user can enable or disable Wi-Fi in the quick settings tiles.

If the Allow quick settings tiles is disabled, all the quick settings tiles are not available.

On

Off

On

If enabled, and if the Allow quick settings tiles is enabled, the user can enable or disable Airplane mode in the quick settings tiles.

If the Allow quick settings tiles is disabled, the Airplane mode quick settings tile is not available.

#### User restrictions for quick settings tiles

The following table describes the user restriction settings that are related to the quick settings tiles.

Allow quick settings tiles

On

Off

On

If enabled, all enabled quick setting tiles are accessible to the end user.

If disabled, all quick setting tiles are inaccessible to the end user.

Wi-Fi

Internet (Only for Cisco Wireless Phone 860 only (from version 2.1(0) and later)

On

Off

On

If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile.

If disabled, the quick setting tile is hidden and can't be added.

Bluetooth

On

Off

On

If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile.

If disabled, the quick setting tile is hidden and can't be added.

Do not disturb

On

Off

On

If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile.

If disabled, the quick setting tile is hidden and can't be added.

Flashlight

On

Off

On

If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile.

If disabled, the quick setting tile is hidden and can't be added.

Rotation lock

Auto rotate (Only for Cisco Wireless Phone 860 only (from version 2.1(0) and later)

On

Off

On

If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile.

If disabled, the quick setting tile is hidden and can't be added.

Battery saver

On

Off

On

If enabled and if the Allow quick settings tiles is enabled, the user can control this quick setting tile.

If disabled, the quick setting tile is hidden and can't be added.

Mobile data

On

Off

On

If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile.

If disabled, the quick setting tile is hidden and can't be added.

Airplane mode

On

Off

On

If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile.

If disabled, the quick setting tile is hidden and can't be added.

Cast

Screen cast (Only for Cisco Wireless Phone 860 only (from version 2.1(0) and later)

On

Off

On

If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile.

If disabled, the quick setting tile is hidden and can't be added.

High touch

On

Off

On

If enabled and if the Allow quick settings tiles is enabled, the user can control this quick setting tile.

If disabled, the quick setting tile is hidden and can't be added.

Hotspot

On

Off

On

If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile.

If disabled, the quick setting tile is hidden and can't be added.

Night light

On

Off

On

If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile.

If disabled, the quick setting tile is hidden and can't be added.

Location

On

Off

On

If enabled and if the Allow quick settings tiles is enabled, the user can control this quick setting tile.

If disabled, the quick setting tile is hidden and can't be added.

Color inversion (Only for Cisco Wireless Phone 860 only (from version 2.1(0) and later)

On

Off

On

If enabled and if the Allow quick settings tiles is enabled, the user can control this quick setting tile.

If disabled, the quick setting tile is hidden and can't be added.

Data saver

On

Off

On

If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile.

If disabled, the quick setting tile is hidden and can't be added.

Dark theme

On

Off

On

Available from release 1.3(0) onward, the Dark theme setting changes the display from dark text on a light background, to light text on a dark background.

If enabled and if the Allow quick settings tiles is enabled, the user can control this quick setting tile.

If disabled, the quick setting tile is hidden and can't be added.

Nearby share

Quick share (Only for Cisco Wireless Phone 860 only (from version 2.1(0) and later)

On

Off

On

Available from release 1.3(0) onward, Nearby share is an Android platform setting that enables phones to share files, links, and pictures with other devices within a certain
                                             range.

If enabled and if the Allow quick settings tiles is enabled, the user can control this quick setting tile.

If disabled, the quick setting tile is hidden and can't be added.

For Cisco Wireless Phone 860 Only (version 2.1(0) and later)

On

Off

On

On

Off

On

Enables control of smart devices connected to the Google Home app.

On

Off

On

Opens screen recording options.

On

Off

On

On

Off

On

Launches the Camera app to scan a QR code.

On

Off

On

Allows a user to modify how colors display on their phone and are useful for a vision impaired user or for the user who want
                                             to set their display to grayscale.

To access Android Color correction, navigate to Settings > Accessibility > Color and motion > Color correction.

On

Off

On

On

Off

On

#### User restrictions for notification shade settings gear

The following table describes the user restriction setting that is related to the settings gear in the notification shade.

On

Off

On

If enabled, the user can make Android settings changes through the gear in the notification shade.

If disabled, the Android settings gear in the notification shade is not accessible to the user.

If you are using a Smart Launcher to restrict user access to certain apps and settings, we recommend that you disallow this
                                                         setting through the Cisco Wireless Phone Configuration Management tool . Otherwise, users can easily open apps that aren't on the Smart Launcher.

Allow manage notification settings button (Only for Cisco Wireless Phone 860 only (from version 2.1(0) and later)

On

Off

On

#### User restrictions for time

The following table describes the user restriction settings that are related to time.

On

Off

On

If enabled, the user can manually change the time zone on the phone from Settings > System > Date & Time .

If disabled, the user cannot manually change the time zone on the phone.

On

Off

On

If enabled, the user can manually change the time format on the phone from Settings > System > Date & Time .

If disabled, the user cannot manually change the time format on the phone.

On

Off

On

Not applicable for Wi-Fi enabled phones.

#### User restrictions for emergency calls

The following table describes the user restriction setting that is related to emergency calls from the lock screen.

On

Off

On

If enabled, displays the EMERGENCY button when the phone screen is locked.

Regardless of whether you enable or disable this setting, a RETURN to CALL button is present if the phone is in a call and locked.

#### User restrictions for lock screen proximity sensor

The following table describes the user restriction setting that is related to the lock screen proximity sensor.

Lock screen proximity detection

On

Off

On

If enabled, the phone screen automatically locks when the user covers the proximity sensor. This prevents accidental input
                                             when a user puts the phone in a pocket.

### More Custom Settings

Some of the Custom Settings allow you to give users control of certain phone settings from the Android settings menu. You
                                 are also able to enable or disable certain settings, or set a specific value at the Enterprise Mobility Management (EMM) application or Cisco Wireless Phone Configuration Management tool level.

Consider the following when you configure the Custom Settings:

If you set a value in the EMM application , users can't change it on the Custom Settings menu, but they may be able to change it on the Android settings menu. The changed
                                       value reflects in the Custom Settings menu but the EMM application could override the changed value at any time.

If you set a value in the Cisco Wireless Phone Configuration Management tool , users can't change it on the Custom Settings menu, or on the Android settings menu.

If you set a Custom Setting to:

User controlled , it allows the user to control the setting from the Android settings menu. In this case, the Android setting menu takes precedence
                                             over the Custom Setting.

Enable , the user could disable it in the Android menu. The changed value reflects in the Custom Settings menu but the EMM application could override the changed value at any time.

Disable , the user could enable it in the Android menu. The changed value reflects in the Custom Settings menu but the EMM application could override the changed value at any time.

If you use a secure launcher, users can't access the Android settings menu even if you set a Custom Setting to User controlled .

#### Time

Use the following settings to configure custom time settings.

NTP server address

2.android.pool.ntp.org

The Network Time Protocol (NTP) domain name or IP address.

Deploy a local time server for phones that are not connected to the internet and therefore getting their time from Google
                                             or some other cloud server.

From release 1.5(0), you can also define a server in DHCP option 42 to provide NTP service in case the NTP server isn't available.

Time zone

Choice

Unset/deferred

A drop-down list of all the available time zones. Unset/deferred does not set a time zone through this configuration remotely.

Caution

The time zone settings are listed by country/region/city and also have a number setting under Etc. (Etc/GMT+/- ##). However,
                                                         the number values (for example, –2 or +2) are reversed from usual GMT time designations. Your setting for Etc/GMT+2 transposes
                                                         into the actual setting of GMT-2). Therefore, we recommend that you use the country/region/city option whenever possible.

Time format

Unset/deferred

12 hours

24 hours

Unset/deferred

Automatic time zone

On

Off

On

Enables or disables automatic time zone.

On

Off

On

#### Device info

Use the following settings to configure custom device information settings.

On

Off

Off

If enabled, provides four text fields for more information about the user who is assigned this phone. This information appears
                                             in the phone notifications and on a locked screen.

First parameter for device information notification

Second parameter for device information notification

Third parameter for device information notification

Fourth parameter for device information notification

#### Device name

Use the following setting to configure a custom name for the device.

String

Allows you to set the Android device name. This is useful when you use an Enterprise Mobility Management (EMM) application to configure the phones.

#### Battery

Use the following settings to configure custom battery settings.

Battery optimization allow list

Android Battery Saver mode curtails functionality to conserve the battery life. However, it also reduces functionality by
                                             turning off apps that you might want to remain operational. Apps that you add to this list remain operational when the user
                                             turns on the phone's Battery Saver mode.

Caution

Apps that you add to this list increase battery usage by staying awake. Ensure that users have extra batteries available.

Allow battery saver

On

Off

On

If enabled, allows the user to turn battery saver mode on or off.

Battery saver mode can have a significant impact on what apps are available or functioning.

Battery percentage

User controlled

Enable

Disable

User controlled

User controlled: makes the Battery percentage Android setting available for the user to show or hide the battery percentage in the phone status bar.

Enable and Disable: make the Battery percentage Android setting unavailable to users and allow the EMM application to control the setting.

Enable displays the battery percentage on the status bar.

Disable means that the battery percentage doesn't display on the phone.

#### Keyboard

Use the following setting to configure the keyboard Google voice typing setting.

On

Off

On

Enables or disables Google voice typing.

#### Sleep

Use the following setting to configure the sleep setting.

User controlled

15 seconds

30 seconds

1 minute

5 minutes

10 minutes

30 minutes

User controlled

Sets the amount of time before the screen times out after inactivity.

User controlled allows users to control the sleep settings available in the Android settings menu.

#### Display

Allows certain display settings available in the Android settings menu to be controlled by an EMM application or by the end user.

Use the following settings to configure custom display settings.

Display size

User controlled

Small

Default

Large

User controlled

Sets the display size, which includes all interface elements such as text and images.

For the Cisco Wireless Phone 840 and 840S , the large display size is not currently available, so if you choose this option, the phone uses the default display size.

Font size

User controlled

Small

Default

Large

Largest

User controlled

Sets the font size.

System navigation

User controlled

Gesture navigation

2-button navigation

3-button navigation

User controlled

Sets the system navigation.

For the Cisco Wireless Phone 840 and 840S , 2-button navigation is not currently available, so if you choose this option, the phone uses the 3-button navigation.

Auto-rotate screen

User controlled

Enable

Disable

User controlled

User controlled: makes the Auto-rotate screen Android setting available for users to turn automatic screen rotation on or off.

Enable and Disable: make the Auto-rotate screen Android setting unavailable to users and allow the EMM application to control the setting.

Enable turns on automatic screen rotation.

Disable means that automatic screen rotation is not available.

#### Touch

Allows certain touch settings available in the Android settings menu to be controlled by an EMM application or by the end user.

Use the following settings to configure custom touch settings.

User controlled

Enable

Disable

User controlled

Tones available on the phone or custom tones that are programmed in an EMM application .

User controlled

Enable

Disable

User controlled

Percussive sounds available on the phone or in an EMM application .

User controlled

Enable

Disable

User controlled

A vibration when the user taps the phone touchscreen.

#### Sounds

Use the following settings to configure custom sound settings.

Ringtones

List of available ringtones

All

Select the system ringtone sounds that you want to be available.

Default ringtone

Default ringtone

List of available ringtones

Default (Flutey Phone)

Must be enabled on the Ringtones list.

Notification sounds

List of available notification sounds

All

Select the system notification sounds that you want to be available.

Default notification sound

Default notification sound

List of available notification sounds

Default (Pixie Dust)

Must be enabled on the Notification sounds list.

Alarm sounds

List of available alarm sounds

All

Select the system alarm sounds that you want to be available.

Default alarm sound

Default alarm sound

List of available alarm sounds

Default (Cesium)

Must be enabled on the Alarm sounds list.

Using CUCM, you can download more ringtones, notification sounds, and alarm sounds. The downloaded ringtones and sounds will
                                             appear in their respective list.

#### Camera

Use the following setting to configure the jump to camera setting.

Jump to camera

Quickly open camera (Only For Cisco Wireless Phone 860 only (from version 2.1(0) and later)

User controlled

Enable

Disable

User controlled

Allows certain camera settings available in the Android settings menu to be controlled by an EMM application or by the end user. Permits the user to set the Jump to camera Android setting.

User controlled implies the Android settings value takes precedence.

#### Wallpaper

Use the following settings to configure custom wallpaper settings.

String

Not configured

Enter the complete file path starting with the exact location of the image file—where is it stored on the phone.

Example /sdcard/<name_of_image_file> .

String

Not configured

Enter the complete file path.

Using CUCM, you can download more wallpapers for Lock screen and Home screen. The downloaded wallpapers will appear in their
                                             respective list.

#### Admin reboot command

Use the following settings to configure custom admin reboot command settings.

Reboot command ID

String

Sets reboot command ID.

Reboot schedule type

Timer

When next plugged-in

Timer

Sets when to schedule reboot.

#### Timer reboot configuration

Use the following settings to configure custom timer reboot settings.

Immediately (0 minutes)

1 minute

5 minutes

10 minutes

15 minutes

30 minutes

1 hours

2 hours

3 hours

4 hours

6 hours

8 hours

12 hours

Immediately (0 minutes)

Sets time until first automatic reboot attempt.

None

1

2

3

4

6

8

12

Unlimited

None

Sets the number of times to allow a user to delay the reboot attempt.

1 minute

5 minutes

10 minutes

15 minutes

30 minutes

1 hours

2 hours

3 hours

4 hours

6 hours

8 hours

12 hours

1 minute

Sets the time to delay the reboot attempt.

## Call Quality Settings app

Call quality settings are automatically set in the phone. However, if your support personnel direct you to adjust a setting
                           such as the Wi-Fi band or channels, you can do so with the Call Quality Settings app.

By default, all Wi-Fi band options and band channels are enabled. Make sure to enable at least one band and channel, other
                           wise the phone loses connection and does not function.

Caution

Review the bands and channels in use at the intended location before you make any changes. If you select the wrong band or
                                       channels, you can permanently disconnect phones from the network. Contact Cisco TAC if incorrect band selection disables the
                                       phones. Finally, you may need to manually reset factory defaults to the phones.

### Wi-Fi information

The Call Quality Settings app displays information about the Wi-Fi access point connection to the phone. This Wi-Fi information may help you to troubleshoot
                                 call quality issues.

SSID

Service Set Identifier (SSID) is the unique name that identifies the wireless network.

AP name

Access point (AP) name displays the name of the AP.

BSSID

Basic Service Set Identifier (BSSID) is the MAC of the radio MAC + SSID.

Channel

Channel displays the AP radio channel.

RSSI

Noise

Noise indicates the level of background noise in the environment.

CU

Channel utilization (CU) shows how busy the channel is.

### Call Quality Settings

You can configure the following Call Quality Settings as required.

#### Wi-Fi low RSSI threshold

If Cisco TAC instructs you, use the following setting to change the threshold for the Wi-Fi low Received Signal Strength Indicator
                                 (RSSI).

Field

Field type or choices

Default

Description

Wi-Fi Low RSSI threshold

Integer –55 to –100

–67

Voice quality can degrade if the Wi-Fi signal is too weak. The RSSI changes as the user moves closer to or away from the connected
                                             AP. The RSSI threshold value setting is the RSSI level at or below which the phone seeks a better AP. The phone uses many
                                             attributes of an AP to determine if it is a good candidate including the current load on the AP, the available bandwidth on
                                             the AP, and channel. Sometimes the best AP may have an RSSI value lower than other candidates.

Caution

Consult Cisco TAC before you change the RSSI threshold value.

#### Channel selection

Use the following settings to select Wi-Fi bands.

Field

Field type or choices

Default

Description

Auto

Enabled

Disabled

Enabled

When enabled:

The phone uses any available band or channel.

You can’t select a specific band or channel.

The phone ignores, but does not forget, your individual channel preferences.

When disabled, you can select which band to enable and select specific channels within each band.

You can't disable both Wi-Fi bands at the same time.

2.4 GHz Wi-Fi band

Enabled

Disabled

Enabled

If enabled:

The phone uses any available channel in the 2.4 GHz band.

You can enable or disable specific channels within 2.4 GHz band.

5 GHz Wi-Fi band

Enabled

Disabled

Enabled

If enabled:

The phone uses any available channel in the 5 GHz band.

You can enable or disable specific channels within 5 GHz subbands. Each subband includes a group of channels.

Use the following settings to select 2.4 GHz channels.

Field

Field type or choices

Default

Description

Channel 1 (2412 MHz)

On

Off

On

Enables channel.

Channel 2 (2417 MHz)

On

Off

On

Enables channel.

Channel 3 (2422 MHz)

On

Off

On

Enables channel.

Channel 4 (2427 MHz)

On

Off

On

Enables channel.

Channel 5 (2432 MHz)

On

Off

On

Enables channel.

Channel 6 (2437 MHz)

On

Off

On

Enables channel.

Channel 7 (2442 MHz)

On

Off

On

Enables channel.

Channel 8 (2447 MHz)

On

Off

On

Enables channel.

Channel 9 (2452 MHz)

On

Off

On

Enables channel.

Channel 10 (2457 MHz)

On

Off

On

Enables channel.

Channel 11 (2462 MHz)

On

Off

On

Enables channel.

Channel 12 (2467 MHz)

On

Off

On

Enables channel.

Channel 13 (2472 MHz)

On

Off

On

Enables channel.

Channel 14 (2484 MHz)

On

Off

On

Enables channel.

Use the following settings to select 5.0 GHz channels.

Field

Field type or choices

Default

Description

Channel 36 (5180 MHz)

On

Off

On

Enables channel.

Channel 40 (5200 MHz)

On

Off

On

Enables channel.

Channel 44 (5220 MHz)

On

Off

On

Enables channel.

Channel 48 (5140 MHz)

On

Off

On

Enables channel.

Channel 52 DFS (5260 MHz)

On

Off

On

Enables channel.

Channel 56 DFS (5280 MHz)

On

Off

On

Enables channel.

Channel 60 DFS (5300 MHz)

On

Off

On

Enables channel.

Channel 64 DFS (5320 MHz)

On

Off

On

Enables channel.

Channel 100 DFS (5500 MHz)

On

Off

On

Enables channel.

Channel 104 DFS (5520 MHz)

On

Off

On

Enables channel.

Channel 108 DFS (5540 MHz)

On

Off

On

Enables channel.

Channel 112 DFS (5560 MHz)

On

Off

On

Enables channel.

Channel 116 DFS (5580 MHz)

On

Off

On

Enables channel.

Channel 120 DFS (5600 MHz)

On

Off

On

Enables channel.

Channel 124 DFS (5620 MHz)

On

Off

On

Enables channel.

Channel 128 DFS (5640 MHz)

On

Off

On

Enables channel.

Channel 132 DFS (5660 MHz)

On

Off

On

Enables channel.

Channel 136 DFS (5680 MHz)

On

Off

On

Enables channel.

Channel 140 DFS (5700 MHz)

On

Off

On

Enables channel.

Channel 144 DFS (5720 MHz)

On

Off

On

Enables channel.

Channel 149 (5745 MHz)

On

Off

On

Enables channel.

Channel 153 (5765 MHz)

On

Off

On

Enables channel.

Channel 157 (5785 MHz)

On

Off

On

Enables channel.

Channel 161 (5805 MHz)

On

Off

On

Enables channel.

Channel 165 (5825 MHz)

On

Off

On

Enables channel.

#### Wi-Fi preferences

Use the following settings to select Wi-Fi preferences.

Field

Field type or choices

Default

Description

FT

Preferred

Not preferred

Preferred

Fast Transition (FT)

CCKM

Preferred

Not preferred

Preferred

Cisco Centralized Key Management (CCKM)

CAC

ON

OFF

OFF

Call Admission Control (CAC)

## Diagnostics app

Diagnostics application allows administrator to perform diagnostics tests quickly and efficiently to verify phone’s hardware
                              components.

As an administrator, you can:

Perfom individual tests for the following features:

Audio

Battery

Buttons

Camera

Display

NFC

Sensor

Touchscreen

Vibration

Wi-Fi

View Test Results

Reset Test Results

Generate QRCode

View information such as Software Versions, Android Version, Device Serial, Wi-Fi Mac Address, Device Model, and Battery Serial.

## Sound Stage app

The sound stage app prevents the users from accidentally muting the phone and missing critical phone calls or alerts. This
                           app will override and ignore volume changes made by the user or third-party applications that conflict with the admin settings.
                           Volume Profile configurations typically provided by EMM. It also controls volume on alerts and notifications from third-party
                           applications.

Allows control of volume and can be set it to lower levels during night Shifts from 7PM- 7AM or any customer set time. Controls
                           volume on Cisco applications such as WebAPI, Battery Life and PTT which have independent volume setting. Controls volume levels,
                           low or high, based on customer needs when connected to a power charger. Allows volume control when entering or exiting Quiet
                           zones within the hospital like Neonatal Intensive Care Unit (NICU). This can be set both manual using the phone UI or automatic
                           by scanning a pre-programmed NFC card placed at entrance and exits. This feature has the capability to program NFC cards using
                           Android Beam.

### Admin Settings for Sound Stage

Use the following Admin settings to configure the Sound Stage app.

Field

Field type or choices

Default

Description

Enable Sound Stage

On

Off

Off

Enables Sound Stage app.

If the Enable Sound Stage is disabled, all the admin settings tiles are not available.

Enable sound profile switch

On

Off

Off

If the Enable Sound Stage tile is enabled, you can enable or disable Enable sound profile switch .

Enable normal profile

On

Off

Off

If the Enable Sound Stage tile is enabled, you can enable or disable Enable normal profile .

Enable loud profile

On

Off

Off

If the Enable Sound Stage tile is enabled, you can enable or disable Enable loud profile .

Enable soft profile

On

Off

Off

If the Enable Sound Stage tile is enabled, you can enable or disable Enable soft profile .

Enable silent profile

On

Off

Off

If the Enable Sound Stage tile is enabled, you can enable or disable Enable silent profile .

Enable personal profile

On

Off

Off

If the Enable Sound Stage tile is enabled, you can enable or disable Enable personal profile .

Persist active profile notification

On

Off

Off

If the Enable Sound Stage tile is enabled, you can enable or disable Persist active profile notification .

Switch profiles silently

On

Off

Off

If the Enable Sound Stage tile is enabled, you can enable or disable Switch profiles silently .

### Audio profiles

You can access Audio profiles only if the Enable Sound Stage tile is enabled under Settings > Admin settings .

Sound stage app has four types of standard audio profiles, they are Normal , Loud , Soft , and Silent . Each profile contains a default a minimum and a maximum volume level that the phone can be set for that media type. However,
                                 you may use Personal Profile .

You can also customize any of the audio profiles as required, by changing the the volume level for alarm, media, ringer, in-call,
                                 and apps as applicable.

### Change the audio profile

You can change the audio profile only if the Enable Sound Stage tile is enabled in Settings > Admin settings . By default normal profile will be activated.

The audio profile could also be changed by scanning a programmed NFC tag without the phone open.

To change the audio profile:

Step 1

Access the Sound Stage app.

Step 2

Tap the Change button for the active audio profile.

Step 3

Choose one of the following audio profiles.

- Normal

- Loud

- Soft

- Silent

- Personal

### Profile switch rules

You can set up profile switch rules based on behavior (charging) or time.

Behavior Based: Allows you to set up profile switch rule that automatically switches audio profile to desired profile when a mobile phone
                                 is charging. You can set up behavior based profile switch rule by enabling Charging tile in Settings > Profile switch rules .

Time Based: Allows you to set up profile switch rule that automatically switches audio profile to desired profile at a specified time.
                                 You can specify four different time based profile switch rules. You can set up the time based profile switch rule by tapping
                                 on any of the four time slots in Settings > Profile switch rules > TIME BASED and specify the time and desired audio profile.

If you have set up both behavior based and time based profile switch rules, the high priority will be behavior based.

You can set up the charging based profile switch rules, only if Charging tile is enabled in Settings > Profile switch rules . You can also set up the time based profile switch rules.

To change the Switch to profile:

Step 1

Access the Sound Stage app.

Step 2

Tap the Overflow menu.

Step 3

Select Settings > Profile switch rules .

Step 4

Tap Charging .

Step 5

Choose one of the following Switch to options .

- Normal

- Loud

- Soft

- Silent

- Personal

## Web API app

Developers use the Web API app to interface with external services and provide links to frequently used websites. Web API allows you to configure the
                              phones to integrate with an XML application.

The following table describes the Web API settings.

Field

Field type or choices

Default

Description

Enable Web API

On

Off

Off

Enables or disables Web API.

Enable Web access

On

Off

Off

Enables or disables Web access.

Data format

XML

JSON

XML

Sets the data format. XML is the only supported format.

### Phone state polling

You can set the following phone state polling parameters.

Field

Field type or choices

Default

Description

Username

String

Defines the username that the phone requires to authenticate polling.

Password

String

Defines the password that the phone requires to authenticate polling.

Respond mode

Requester

URL

Requester

Defines the method for sending the requested polling data.

If the Respond mode is requester, the response is automatically sent to the HTTP server running at the address where the request was made.

URL

String

When the Respond mode is set as URL, this field defines the URL of a valid HTTP server that gets the response.

You must enter the URL. This can be a different address than the requester.

### Push settings

When you configure push settings, consider that when a phone receives a push request, it reacts differently based on the following:

If a phone is in a call and receives a push with a priority of High, Important, or Normal, the phone accepts the push but
                                       does nothing.

If a phone receives a push request when it is in Do Not Disturb (DND) with:

Total Silence—The phone does not make any sound and only displays visual notification. The phone stays in Total Silence mode
                                             after the push request.

Alarms Only and Priority Only—The phone changes mode to Normal, presents visual notification, and plays the notification sound.
                                             The phone stays in Normal mode after the push request.

Use the following settings to configure push settings.

Field

Field type or choices

Default

Description

Username

String

Defines the username for the Web API to do any kind of push.

Password

String

Defines the password for the Web API to do any kind of push.

Push alert priority

All

Critical

High

Important

Normal

None

All

Sets the priority for messages from the app. Only messages with the selected priority level display.

All—Allows all priority push messages.

Critical—Allows only critical push messages.

High—Allows only high priority push messages.

Important—Allows only important push messages.

Normal—Allows only normal push messages.

None—Discards all push messages.

Server root URL

Defines the URL of the application server. This root URL is combined with the phone address and sent to the phone’s browser.

For example, if the application server root URL is http://172.24.128.85:8080/sampleapps and the relative URL is /examples/sample.html , the URL that is sent to the web browser on the phone is http://172.24.128.85:8080/sampleapps/examples/sample.html .

The URL can be either HTTP or HTTPS.

Enable notification ringtone

On

Off

Off

Defines whether a notification ringtone sound plays when a phone receives a push message.

The notification sound that plays is set by the user in the phone Settings > Sound > Default notification sound .

Web API volume

0–100

50

Sets the volume for the push ringtone.

### Push request notifications

Each push request alert that appears in the notification drawer includes a View Alert option and a triangular exclamation icon. The color of the icon varies according to the priority of the alert:

Critical: Red

High: Orange

Important: Yellow

Normal: Green

If you receive multiple push requests, the notifications in the notification drawer are grouped by priority. The groups display
                                 in descending order with Critical on top and Normal at the bottom and they indicate the number of alerts of each priority
                                 received.

If you reboot the phone, it does not automatically clear critical alerts. After you reboot a pin protected phone, if there
                                 is an uncleared critical push request, a pop-up dialog with a message Unlock the phone to view critical alerts appears.

### Web application shortcuts

The Web API app allows you to configure the phones to integrate with an XML application. You can configure up to 12 web application
                                 shortcuts. Enter the following fields for each of the desired web application shortcuts.

Field

Field type or choices

Default

Description

Shortcut title

String

Defines a title for the web application shortcut.

The title displays in the widget box on the phone after you reboot the phone.

Shortcut URL

String

Defines the application URL. You can enter any URL available to the phones.

### Place web application shortcuts on launcher screen

For easy access to web application shortcuts, place the shortcuts on the phone launcher screen. Once you place a shortcut
                                 on the launcher screen, you can tap the shortcut to open the web application in a browser.

Step 1

Long press the home screen.

Step 2

Tap Widgets .

Step 3

Touch and hold the shortcut.

Step 4

Drag the shortcut to the desired location on a launcher screen.

### Device event notifications

You can configure the phones to send notifications of the following phone events to a defined URL.

All events

Cisco Phone events such as phone state changes, incoming or outgoing calls, or SIP registration.

Emergency events

To edit an existing event URL, delete it and reenter the information with the new URL name or address.

Use the following settings to configure event notifications.

Field

Field type or choices

Default

Description

Notification name

String

Defines a descriptive label for the event.

Notification URL

String

Defines the URL for the event.

None

On

Off

On

By default, there are no notification events.

All

On

Off

Off

Sends notifications about all phone events when enabled.

Cisco Phone events: Outgoing

On

Off

Off

Sends notifications about all outgoing phone events when enabled.

Cisco Phone events: Incoming

On

Off

Off

Sends notifications about all incoming phone events when enabled.

Cisco Phone events: State Change

On

Off

Off

Sends notifications about all phone state change events when enabled.

Cisco Phone events: Login/out

On

Off

Off

Sends notifications about all phone login and logout events when enabled.

Cisco Phone events: Registration

On

Off

Off

Sends notifications about all phone registration events when enabled.

Cisco Phone events: Unregistration

On

Off

Off

Sends notifications about all phone unregistration events when enabled.

Emergency events

On

Off

Off

Sends notifications about all Emergency events when enabled.

| Note | The Barcode, Buttons, Call Quality Settings, and Custom Settings apps are OEMConfig apps. To configure these apps, your EMM
                                          must support the OEMConfig enhanced schema. If necessary, consult with your EMM support for assistance. |
|---|---|

| Step 1 | Sign in to the EMM application . |
|---|---|
| Step 2 | Set up an Android for Work account, which allows you to sequester the phones from external access and provide only those apps
                                             which your organization requires. |
| Step 3 | Create a configuration profile that contains payloads for each configuration area required. Note We recommend that you set the following minimal settings. Restrictions : Enable use of the camera and allow app installation. Android Restrictions : System settings : Prevent Android Debug Bridge (ADB) access. System settings : Prevent installation of apps from unknown sources. Permissions : Auto grant all permissions. For more information on how Android 13 manages Cisco application permissions differently compared
                                                                        to Android 10, see Android 13 App Permissions . Android System Apps : Specify the allowed list of Cisco apps that you download to the EMM application from Google Play Store. Android Wallpaper : If needed, lock screen message. Wi-Fi Profile : Configure Wi-Fi settings. | Note | We recommend that you set the following minimal settings. Restrictions : Enable use of the camera and allow app installation. Android Restrictions : System settings : Prevent Android Debug Bridge (ADB) access. System settings : Prevent installation of apps from unknown sources. Permissions : Auto grant all permissions. For more information on how Android 13 manages Cisco application permissions differently compared
                                                                        to Android 10, see Android 13 App Permissions . Android System Apps : Specify the allowed list of Cisco apps that you download to the EMM application from Google Play Store. Android Wallpaper : If needed, lock screen message. Wi-Fi Profile : Configure Wi-Fi settings. |
| Note | We recommend that you set the following minimal settings. Restrictions : Enable use of the camera and allow app installation. Android Restrictions : System settings : Prevent Android Debug Bridge (ADB) access. System settings : Prevent installation of apps from unknown sources. Permissions : Auto grant all permissions. For more information on how Android 13 manages Cisco application permissions differently compared
                                                                        to Android 10, see Android 13 App Permissions . Android System Apps : Specify the allowed list of Cisco apps that you download to the EMM application from Google Play Store. Android Wallpaper : If needed, lock screen message. Wi-Fi Profile : Configure Wi-Fi settings. |
| Step 4 | Add an Android Enterprise Owner Account to identify the administrator who manages the phone profile. Note Ensure that the account isn’t a local EMM application account, but an Android Enterprise Owner Account. | Note | Ensure that the account isn’t a local EMM application account, but an Android Enterprise Owner Account. |
| Note | Ensure that the account isn’t a local EMM application account, but an Android Enterprise Owner Account. |
| Step 5 | Create identifying tags so that you can separate phones into corresponding groups. Note Set groups and tags as a payload under the Profiles console. Set the Device Configuration option as Targets. However, at this point, the device only knows that it’s a certain model with a certain serial number and MAC address. After
                                                            enrollment, you can assign device tags with more granularity. You can group devices by specific owners, keywords, or device
                                                            types, depending on the desired groupings. | Note | Set groups and tags as a payload under the Profiles console. Set the Device Configuration option as Targets. However, at this point, the device only knows that it’s a certain model with a certain serial number and MAC address. After
                                                            enrollment, you can assign device tags with more granularity. You can group devices by specific owners, keywords, or device
                                                            types, depending on the desired groupings. |
| Note | Set groups and tags as a payload under the Profiles console. Set the Device Configuration option as Targets. However, at this point, the device only knows that it’s a certain model with a certain serial number and MAC address. After
                                                            enrollment, you can assign device tags with more granularity. You can group devices by specific owners, keywords, or device
                                                            types, depending on the desired groupings. |
| Step 6 | Use the full name of the Cisco app (com.cisco.xxxx) to download the desired Cisco apps from the Google Play Store. Note The app and the settings download to the Profile console. Each app is automatically added to the list and the app settings added as payloads. | Note | The app and the settings download to the Profile console. Each app is automatically added to the list and the app settings added as payloads. |
| Note | The app and the settings download to the Profile console. Each app is automatically added to the list and the app settings added as payloads. |
| Step 7 | Configure the Cisco apps with the key-value pairs. Note The key-value pairs should have downloaded with the app. Check the key-value pairs to be sure of accuracy and configure any
                                                            settings. If any key-value pairs don’t download, manually add them. | Note | The key-value pairs should have downloaded with the app. Check the key-value pairs to be sure of accuracy and configure any
                                                            settings. If any key-value pairs don’t download, manually add them. |
| Note | The key-value pairs should have downloaded with the app. Check the key-value pairs to be sure of accuracy and configure any
                                                            settings. If any key-value pairs don’t download, manually add them. |
| Step 8 | In the EMM application console, approve the apps for distribution. |
| Step 9 | Configure the Android Kiosk Mode to include the apps that you want. Note Kiosk Mode is a launcher for the phone UI. Only approved apps are available to select for the opening screen. | Note | Kiosk Mode is a launcher for the phone UI. Only approved apps are available to select for the opening screen. |
| Note | Kiosk Mode is a launcher for the phone UI. Only approved apps are available to select for the opening screen. |

| Note | We recommend that you set the following minimal settings. Restrictions : Enable use of the camera and allow app installation. Android Restrictions : System settings : Prevent Android Debug Bridge (ADB) access. System settings : Prevent installation of apps from unknown sources. Permissions : Auto grant all permissions. For more information on how Android 13 manages Cisco application permissions differently compared
                                                                        to Android 10, see Android 13 App Permissions . Android System Apps : Specify the allowed list of Cisco apps that you download to the EMM application from Google Play Store. Android Wallpaper : If needed, lock screen message. Wi-Fi Profile : Configure Wi-Fi settings. |
|---|---|

| Note | Ensure that the account isn’t a local EMM application account, but an Android Enterprise Owner Account. |
|---|---|

| Note | Set groups and tags as a payload under the Profiles console. Set the Device Configuration option as Targets. However, at this point, the device only knows that it’s a certain model with a certain serial number and MAC address. After
                                                            enrollment, you can assign device tags with more granularity. You can group devices by specific owners, keywords, or device
                                                            types, depending on the desired groupings. |
|---|---|

| Note | The app and the settings download to the Profile console. Each app is automatically added to the list and the app settings added as payloads. |
|---|---|

| Note | The key-value pairs should have downloaded with the app. Check the key-value pairs to be sure of accuracy and configure any
                                                            settings. If any key-value pairs don’t download, manually add them. |
|---|---|

| Note | Kiosk Mode is a launcher for the phone UI. Only approved apps are available to select for the opening screen. |
|---|---|

| Note | We recommend that you disallow the Allow Notification Shade Settings Gear in the Custom Settings app in Cisco Wireless Phone Configuration Management tool . Otherwise, users can easily open apps that aren't on the Smart Launcher. |
|---|---|

| Step 1 | From the phone, tap the desired Cisco app. The Buttons , Call Quality Settings , Custom Settings , and Web API apps open directly to their settings page. |
|---|---|
| Step 2 | For the Barcode , Battery Life , Emergency , and PTT apps, tap the Overflow menu. |
| Step 3 | Tap Settings . |

| Note | If enabled, users may change the button actions with the Buttons app. If desired, you can disable a user's ability to change the default Panic Button in the Buttons app. |
|---|---|

| Caution | The reliability of the Emergency app and Panic Button depends on the functionality and reliability of your organization's infrastructure. The infrastructure includes the wireless
                                       LAN, the LAN, the call server, the central provisioning server, the server hosting location services, the central security
                                       system and its servers, the correct configuration of the handsets, correct installation and configuration management server,
                                       and thorough training of personnel. We assume no responsibility and shall not be liable for any of the above dependency factors. In addition, please be aware
                                       that the Panic Button and Emergency app should not be your sole solution to any of your safety concerns and are not a substitute for safe practices and procedures. |
|---|---|

| Note | To identify the location of an alerting phone, the Emergency app must use the Web API app to interface with a method to locate the phone. Typically, they use a type of location services that use the SSID and
                                                AP location to identify the phone’s location. |
|---|---|

| Step 1 | From the Web API settings, choose Device event notifications > Add new notification URL . |
|---|---|
| Step 2 | Enter a descriptive notification name and URL of the security application. |
| Step 3 | Check the box beside Emergency events as the type of event you are sending to this URL. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Monitoring | On Off | Off | Enables Emergency motion monitoring. Enable this setting to allow any of the motion settings to trigger an alarm. |
| No movement sensitivity | Disabled Level 1 (lowest) Level 2 Level 2 Level 2 Level 2 Level 2 Level 7 (highest) | Disabled | Sets the degree of motionlessness or lack of any type of movement of the phone to trigger an alarm. Level 1 is the least sensitive. An alarm triggers a warning if the user is moving some, but below the normal threshold. Level 7 is the most sensitive. An alarm triggers if the user is almost completely still. |
| No movement timeout (seconds) | Integer 10–300 | 30 | Sets the length of time in seconds that the user would have to maintain the configured degree of stillness (or a more severe
                                                   degree). |
| Tilt sensitivity | Disabled Level 1 (lowest) Level 2 Level 2 Level 2 Level 2 Level 2 Level 7 (highest) | Disabled | Sets the nonvertical position of the phone that is required to trigger an alarm. Level 1 is the least sensitive. An alarm triggers if the user is nearly prone. Level 7 is the most sensitive. An alarm triggers if the user was leaning somewhat. |
| Tilt timeout (seconds) | Integer 10–300 | 10 | Sets the length of time in seconds that the user would have to maintain the configured degree of tilt (or a more severe degree). |
| Running sensitivity | Disabled Level 1 (lowest) Level 2 Level 2 Level 2 Level 2 Level 2 Level 7 (highest) | Disabled | Sets the amount of shaking of the phone that is required to trigger an alarm. Level 1 is the least sensitive. An alarm triggers if there is quite a bit of jostling. Level 7 is the most sensitive. An alarm triggers if the user walks quickly or runs. |
| Running timeout (seconds) | Integer 10–60 | 10 | Sets the length of time in seconds that the user would have to maintain the configured degree of shaking (or a more severe
                                                   degree). |
| Snooze timeout (seconds) | Integer 0–300 | 0 | The Snooze feature allows the user to temporarily suspend Emergency motion monitoring. To activate this feature, set the timeout
                                                   in seconds 1–300. By default, the Snooze feature is disabled (set to 0). |
| Warning timeout (seconds) | Integer 10–60 | 10 | Sets the warning timeout in seconds. This is the amount of time between the trigger of the warning and the alarm state. In
                                                   the alarm state, an emergency call might be placed or an alarm is sent to an external security application. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Panic button | Disabled Long press Two short presses Two short or one long press | Disabled | Defines the sequence that the user uses to trigger the Panic Button alarm. You can also disable the Panic Button alarm from this setting. |
| Panic button silent alarm | On Off | On | Enables the silent alarm, which disables the loud local alarm that sounds when a user triggers the Panic Button . If the user is under duress, a silent alarm doesn't alert the assailant. |
| Panic button alarm timeout | Integer 5–30 | 5 | Sets the amount of time, in seconds, to time out the panic alarm. |

| Option | Description | Settings |
|---|---|---|
| Local panic alarm without an emergency phone call | Allows the user to alert people nearby with a loud alarm, but does not place an emergency call. The loud alarm helps people to locate the user, or scares away any potential threats. | Set the Panic button silent alarm to Off. Set the Emergency call to Off. |
| Silent duress alarm with or without an emergency phone call | Allows the user to silently send an alarm signal for help. If the user also must place an emergency call, you can turn off the speakerphone option to maintain the silence. If the Panic Button automatically pushes an alert to an external security application, you do not need to set an emergency
                                                   call. | Set the Panic button silent alarm to On. Set the Emergency call to either On or Off. If necessary, set the Emergency dial force speaker to Off. |
| Incapacitation panic alarm with an emergency phone call | Allows an incapacitated user to place an emergency call. An incapacitated user may not be able to hold the phone to their ear. To ensure that both parties can hear the phone call
                                                   audio, set the alarm to be silent and turn on the forced speakerphone option. | Set the Panic button silent alarm to On. Set the Emergency call to On. Set the Emergency dial force speaker to On. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Emergency call | On Off | Off | Enables the phone to call the emergency number configured in Emergency dial number , if the user triggers the Panic Button or an Emergency motion alarm. |
| Emergency dial force speaker | On Off | On | Enables the speakerphone when the phone places an emergency call. This setting allows the user to be in handsfree mode in
                                                case they can't hold the phone to their ear. |
| Emergency dial number | Any valid TN 911 | 911 | Defines the number that the phone dials when the user triggers the Panic Button or an Emergency motion alarm. You must configure and enable the other related settings for the emergency call to occur. Follow any dial plan rules when you enter the emergency dial number. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Warning tone | Default notification sound None List of available warning tones | Default (Pixie Dust) | Configures the tone to play during a warning period. This tone plays at a gradually increasing volume. Tones play even if
                                                the user silences the handset. Note There is no warning period for the Panic Button; it goes straight to the alarm state. | Note | There is no warning period for the Panic Button; it goes straight to the alarm state. |
| Note | There is no warning period for the Panic Button; it goes straight to the alarm state. |
| Alarm tone | Default alarm sound None List of available alarm tones | Default (Cesium) | Configures the tone to play when a Panic Button press or Emergency alarm triggers. This tone plays at a high volume. Tones
                                                play even if the user silences the handset. |

| Note | There is no warning period for the Panic Button; it goes straight to the alarm state. |
|---|---|

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| PTT volume | Integer 0–100 | 20 | Controls the volume percentage of the PTT volume. |
| Default channel | Channel 1 - ALL Channels that have both Channel can transmit and Channel subscription Admin settings set to Yes | Channel 1 - ALL | The user sets their default channel. The default channel is the channel that broadcasts when the user presses the programmed PTT button or the Talk button in the PTT app. A user can set a channel as their default channel only if they are subscribed to the channel and are able to transmit on the
                                             channel. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable PTT | On Off | Off | PTT must be enabled for it to be activated on the selected handsets. |
| Allow PTT transmission when phone is locked | On Off | Off | From release 1.3(0) onward, you can set PTT to transmit even if the phone is locked. |
| Username | Text | Anonymous | This is the caller ID that displays on the broadcast. Usually set at Device or Group level. If nothing is entered, the default
                                             is Anonymous . |
| Multicast address | Domain name or IP address | 224.0.1.116 | Defines the multicast address for broadcast traffic. |
| Codec | G.711Mu G.726 | G.726 | Defines the codec. |
| Channel setup |  |  | You can set up to 25 PTT channels. By default, the Channel #1 label defaults to ALL, and its transmit and subscription options
                                             are set to Yes. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Channel # n label | String | For Channel # 1: ALL For Channel #2-25: Blank | Allows you to enter a label for the channel. Note You can enter a label with more than 15 characters, but a long label truncates when it displays on the handset. | Note | You can enter a label with more than 15 characters, but a long label truncates when it displays on the handset. |
| Note | You can enter a label with more than 15 characters, but a long label truncates when it displays on the handset. |
| Channel can transmit | Yes No | For Channel # 1 - ALL: Yes For Channel #2-25: No | Enables a user to transmit on the channel. |
| Channel subscription | Yes No | For Channel # 1 - ALL: Yes For Channel #2-25: No. | Subscribes a user to the channel so that they can receive broadcasts. |

| Note | You can enter a label with more than 15 characters, but a long label truncates when it displays on the handset. |
|---|---|

| Note | The Cisco Wireless Phone 860 and Cisco Wireless Phone 860S have an internal secondary battery, which operates the phone during
                                          a hot swap. The Battery Life app dashboard displays the general status of the internal battery. For more information about the secondary battery, you
                                          can tap Open additional metrics and options . The The Cisco Wireless Phone 840 and 840S do not have an internal battery. |
|---|---|

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Alarm volume | Integer 0–100 | 50 | Controls the volume percentage of the low battery alarm. This is a user-controlled setting. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Alarm volume | Integer 0–100 | 50 | Controls the volume percentage of the low battery alarm. This is a user-controlled setting. |
| Enable battery monitoring | On Off | Off | Enables or disables battery monitoring. When disabled, the low battery alarm does not sound and the battery life details such
                                             as the serial number, capacity, temperature, and charging status do not display. |
| Vibrate | On Off | Off | Causes the phone to vibrate if the battery alarm is active and battery monitoring is enabled. |
| Sound | On Off | Off | Enables sound for the battery alarm, if the battery alarm is active and battery monitoring is enabled. |
| Alarm tone | Default alarm sound None List of available alarm tones | Default (Cesium) | Defines the battery alarm tone. |
| Low battery threshold | 15% 20% | 15% | Defines the percentage of remaining battery life to trigger the alarm. |
| Snooze time | 1 min 2 min 3 min 4 min 5 min | 2 min | Defines the number of minutes the alarm is silenced when the user snoozes the battery life alarm. |

| Note | The programmable buttons for the Cisco Wireless Phone 840 and Cisco Wireless Phone 860 are not in the same location. Also, the Cisco Wireless Phone 840 and 840S don't have a Fingerprint button. |
|---|---|

| Callout | Programmable button |
|---|---|
| 1 | Left button |
| 2 | Right button |
| 3 | Top |
| 4 | Volume up |
| 5 | Volume down |
| 6 | Fingerprint—For Cisco Wireless Phone 860 and 860S only. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Left button user assigned | Enabled Disabled | Enabled | Enables the user to change the Left button . |
| Left button | No action Home key Back key Menu key PTT Emergency Volume up Volume down Run application Open URL Scanner (for 800S phones only) Custom 1 Custom 2 Custom 3 Custom 4 | For phones with a barcode scanner: Scanner For phones without a barcode scanner: No action | Allows the user to control the button action if you enable Left button user assigned . |
| Right button user assigned | Enabled Disabled | Enabled | Enables the user to change the Right button . |
| Right button | No action Home key Back key Menu key PTT Emergency Volume up Volume down Run application Open URL Scanner (for 800S phones only) Custom 1 Custom 2 Custom 3 Custom 4 | PTT | Allows the user to control the button action if you enable Right button user assigned . |
| Top button user assigned | Enabled Disabled | Enabled | Enables the user to change the Top button. |
| Top | No action Home key Back key Menu key PTT Emergency Volume up Volume down Run application Open URL Scanner (for 800S phones only) Custom 1 Custom 2 Custom 3 Custom 4 | Emergency | Allows the user to control the button action if you enable Top button user assigned . |
| Fingerprint button user assigned | Enabled Disabled | Enabled | For Cisco Wireless Phone 860 and Cisco Wireless Phone 860S only. Enables the user to change the Fingerprint button. |
| Fingerprint | No action Home key Back key Menu key PTT Emergency Volume up Volume down Run application Open URL Scanner (for 800S phones only) Fingerprint Custom 1 Custom 2 Custom 3 Custom 4 | Fingerprint | For Cisco Wireless Phone 860 and Cisco Wireless Phone 860S only. Allows the user to control the button action if you enable Fingerprint button user assigned . |
| Volume up button user assigned | Enabled Disabled | Enabled | Enables the user to change the Volume up button. |
| Volume up | No action Home key Back key Menu key PTT Emergency Volume up Volume down Run application Open URL Scanner (for 800S phones only) Custom 1 Custom 2 Custom 3 | Volume up | Allows the user to control the button action if you enable Volume up button user assigned . |
| Volume down button user assigned | Enabled Disabled | Enabled | Enables the user to change the Volume down button. |
| Volume down | No action Home key Back key Menu key PTT Emergency Volume up Volume down Run application Open URL Scanner (for 800S phones only) Custom 1 Custom 2 Custom 3 | Volume down | Allows the user to control the button action if you enable Volume down button user assigned . |

| Note | If you use only the app package name and the app is not yet on the phone, the Buttons app can't apply that setting. When you do install the app later, and the user presses the button, the app will not launch. |
|---|---|

| Step 1 | In the EMM application, select Run application . |
|---|---|
| Step 2 | Enter the package name of the app and the activity name of the screen within the app. For example, the package name for the Cisco Phone app is com.cisco.phone . The package name plus the dialer activity name is com.cisco.phone/com.cisco.phone.activities.Dialer . |

| Note | You cannot use the same button to answer and end the calls. |
|---|---|

| Step 1 | Access the Buttons app. |
|---|---|
| Step 2 | In the Buttons settings menu, select the button that you want to use to answer a call. |
| Step 3 | Choose Custom in the resulting action menu. Note Make sure not to choose Custom1 - 4. | Note | Make sure not to choose Custom1 - 4. |
| Note | Make sure not to choose Custom1 - 4. |
| Step 4 | In the Enter custom intent popup window that appears enter one of the following strings in the Action down field (field text is case-sensitive): To send the audio to the phone’s earpiece (shown in the screenshot above): com.cisco.intent.action.ANSWER_CALL_EP To use the phone as a speakerphone: com.cisco.intent.action.ANSWER_CALL_SP To send the audio to a wired headset: com.cisco.intent.action.ANSWER_CALL_HS Note If the phone is connected to a Bluetooth headset the audio will automatically route to the headset regardless of which string
                                                         is entered above. | Note | If the phone is connected to a Bluetooth headset the audio will automatically route to the headset regardless of which string
                                                         is entered above. |
| Note | If the phone is connected to a Bluetooth headset the audio will automatically route to the headset regardless of which string
                                                         is entered above. |
| Step 5 | Leave the remaining fields empty. |
| Step 6 | Tap OK to save your settings. |

| Note | Make sure not to choose Custom1 - 4. |
|---|---|

| Note | If the phone is connected to a Bluetooth headset the audio will automatically route to the headset regardless of which string
                                                         is entered above. |
|---|---|

| Step 1 | Access the Buttons app. |
|---|---|
| Step 2 | In the Buttons settings menu, select the button that you want to answer a call. |
| Step 3 | Choose Custom in the resulting action menu. Note Make sure not to choose Custom1 - 4. | Note | Make sure not to choose Custom1 - 4. |
| Note | Make sure not to choose Custom1 - 4. |
| Step 4 | In the Enter custom intent popup window that appears enter the following string in the Action down field (field text is case-sensitive): com.cisco.intent.action.DECLINE_CALL |
| Step 5 | Leave the remaining fields empty. |
| Step 6 | Tap OK to save your settings. |

| Note | Make sure not to choose Custom1 - 4. |
|---|---|

| Step 1 | Access the Buttons app. |
|---|---|
| Step 2 | In the Buttons settings menu, select the button you that you want to control the flashlight. |
| Step 3 | Choose Custom in the resulting action menu. Note Make sure not to choose Custom1 - 4. | Note | Make sure not to choose Custom1 - 4. |
| Note | Make sure not to choose Custom1 - 4. |
| Step 4 | In the Enter custom intent popup window that appears enter the following in the Action down and Action up fields (field text is case-sensitive): com.cisco.intent.action.FLASHLIGHT_ONOFF |
| Step 5 | In the Extras for action down field enter the following: boolean:flashlight=true |
| Step 6 | In the Extras for action up field enter the following: boolean:flashlight=false |
| Step 7 | Tap OK to save your settings. |

| Note | Make sure not to choose Custom1 - 4. |
|---|---|

| Step 1 | Access the Buttons app. |
|---|---|
| Step 2 | In the Buttons settings menu, select the button you that you want to control the flashlight. |
| Step 3 | Choose Custom in the resulting action menu. Note Make sure not to choose Custom1 - 4. | Note | Make sure not to choose Custom1 - 4. |
| Note | Make sure not to choose Custom1 - 4. |
| Step 4 | In the Enter custom intent popup window that appears enter the following in the Action down and Action up fields (field text is case-sensitive): com.cisco.intent.action.FLASHLIGHT_ONOFF |
| Step 5 | Leave the remaining fields empty. |
| Step 6 | Tap OK to save your settings. |

| Note | Make sure not to choose Custom1 - 4. |
|---|---|

| Cisco app | Cisco app package name |
|---|---|
| Barcode | com.cisco.barcode.service |
| Battery Life | com.cisco.batterylife |
| Buttons | com.cisco.buttons |
| Call Quality Settings | com.cisco.callquality |
| Cisco Phone | com.cisco.phone |
| Custom Settings | com.cisco.customsettings |
| Diagnostics | com.cisco.diagnostics |
| Emergency | com.cisco.emergency |
| Logging | com.cisco.logging |
| PTT | com.cisco.ptt |
| System Updater | com.cisco.sysupdater |
| Sound Stage | com.cisco.soundstage |
| Web API | com.cisco.webapi |

| Note | The Smart Launcher and Device Policy Controller apps are not on the Google store and are available only through the Cisco
                                             Wireless Phone Configuration Management tool. |
|---|---|

| Aztec | Codabar | Interleaved 2 of 5 |
|---|---|---|
| CCA EAN-128 | Code 11 | ISBT-128 |
| CCA EAN-13 | Code 128 | ISBT-128 Con |
| CCA EAN-8 | Code 32 | Macro PDF |
| CCA GS1 DataBar Expanded | Code 39 Full ASCII | Macro QR |
| CCA GS1 DataBar Limited | Code 39 Trioptic | Matrix 2 of 5 |
| CCA GS1 DataBar-14 | Code 93 | Micro PDF |
| CCA UPC-A | DataMatrix | Micro QR |
| CCA UPC-E | EAN-128 | MSI |
| CCB EAN-128 | EAN-13 | PDF-417 |
| CCB EAN-13 | EAN-13 + 2 Supplemental | QR Code |
| CCB EAN-8 | EAN-13 + 5 supplemental EAN-8 | UPC-A |
| CCB GS1 DataBar Expanded | EAN-8 | UPC-A + 2 Supplemental |
| CCB GS1 DataBar Limited | EAN-8 + 2 Supplemental | UPC-A + 5 supplemental |
| CCB GS1 DataBar-14 | EAN-8 + 5 supplemental | UPC-E0 |
| CCB UPC-A | GS1 128 | UPC-E0 + 2 Supplemental |
| CCB UPC-E | GS1 DataBar Expanded | UPC-E0 + 5 supplemental |
| CCC EAN-128 | GS1 DataBar Limited |  |
|  | GS1 DataBar-14 |  |
|  | Han Xin |  |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable barcode scanner | On Off | On | Enables the barcode scanner. |
| Allow scan on screen lock (Only for Cisco Wireless Phone 860 only (from version 2.1(0) and later) | On Off | On | Allows barcode scanning while the phone is locked. |
| Decode session timeout | 0.5 seconds to 9.9 seconds | 5 | Sets the amount of time for the decode session timeout. |
| Vibrate on scan | On Off | On | Sets the phone to vibrate on scan. |
| Sound on scan | On Off | On | Sets the phone to produce a sound on scan. |
| Barcode tone | Low pitch single beep Low pitch double beep High pitch double beep | Low pitch single beep | Sets the barcode scan tone. |
| Illumination power | 0–10 | 5 | Sets the illumination power of the barcode scanner. |
| Allow URL redirection to browser (Only for Cisco Wireless Phone 860 only (from version 2.1(0) and later) | On Off | On | Allows URL redirction. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable AIM codes or symbol id | Disable Enable AIM codes Enable symbol id | Disable | Prefixes AIM code or symbol id before data. The AIM code is an industry standard 3-character identifier that provides information about the symbology that is generated
                                             by the decoder of a scanner. The code is prepended to the scanned barcode and may be employed by keyboard injection and the
                                             data sent through the intent. |
| Automatic carriage return | On Off | Off | Adds an Enter when inject text to an input field. |
| Automatic Tab | On Off | Off | Adds a Tab at the end of an injected barcode value. |
| Trim barcode data | On Off | Off | Removes any trailing or leading whitespaces from a scanned barcode data. |
| Strip characters from left | Integer | 0 | Strips this number of characters from the left (as displayed on screen) of the barcode data. Only positive integers allowed. |
| Strip characters from right | Integer | 0 | Strips this number of characters from the right (as displayed on screen) of the barcode data. Only positive integers allowed. |
| Prepend String | String |  | Prepends a string to the scanned barcode data. |
| Append String | String |  | Appends a string to the scanned barcode data. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Intent delivery method | Disable Stat activity Start service Start foreground service Send broadcast | Disable | Choose intent delivery method. |
| Intent action | String |  | Enter intent action. |
| Intent category | String |  | Enter intent category. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable Aztec | On Off | ON | Enables or disables the symbology. |
| Aztec decoding | Regular Inverse Both | Regular | Sets the decoding. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable Codabar | On Off | ON | Enables or disables the symbology. |
| Codabar length | 0–55 | 5 | Sets the Codabar length. |
| Enable Codabar NOTIS editing | On Off | OFF | Strips start and stop characters. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Code 11 | On Off | ON | Enables or disables the symbology. |
| Code 11 check digit verification | Disable check digits One check digit Two check digits | Disable check digits | Enables or disables check digit verification. |
| Enable transmit code 11 Check Digit | On Off | OFF | Enables or disables transmit. To transmit, enable verification. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Code 32 | On Off | ON | Enables or disables the symbology. Enable Code 39 to enable Code 32. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable Code 39 | On Off | ON | Enables or disables the symbology. Enable Code 39 to enable Code 32. |
| Enable Code 39 check digit verification | On Off | OFF | Enables or disables check digit verification. |
| Enable transmit Code 39 check digit | On Off | OFF | Enables or disables transmit. |
| Enable Code 39 full ASCII conversion | On Off | OFF | Enables or disables full ASCII conversion. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable Code 93 | On Off | ON | Enables or disables the symbology. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable Code 128 | On Off | ON | Enables or disables the symbology. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable Data Matrix | On Off | ON | Enables or disables the symbology. |
| Data Matrix mirror images | Never Mirror Both | Never | Sets mirror images. |
| Data Matrix decoding | Regular Inverse Both | Regular | Sets decoding. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable EAN 8 | On Off | ON | Enables or disables the symbology. |
| Enable convert EAN 8 to EAN 13 | On Off | OFF | Enables or disables conversion to EAN 13. |
| Enable transmit EAN 8 check digit | On Off | OFF | Enables or disables transmit. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable EAN 13 | On Off | ON | Enables or disables the symbology. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable GS1 DataBar 14 | On Off | ON | Enables or disables the symbology. |
| Enable GS1 DataBar composite CCA CCB, and CCC | On Off | ON |  |
| Enable GS1 DataBar Expanded | On Off | ON |  |
| Enable GS1 DataBar Limited | On Off | ON |  |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable GS1-128 | On Off | ON | Enables or disables the symbology. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable Han Xin code | On Off | ON | Enables or disables the symbology. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable Interleaved 2 of 5 | On Off | ON | Enables or disables the symbology. |
| Enable Interleaved 2 of 5 quiet zone | On Off | OFF | Enables or disables quiet zone. |
| Interleaved 2 of 5 check digit verification | Disable USS OPCC | Disable | Enables or disables check digit verification. |
| Enable transmit Interleaved 2 of 5 check digit | On Off | OFF | Enables or disables transmit. |
| Interleaved 2 of 5 length type | One discrete length Two discrete lengths Length within range Any length | One discrete length | Governs the usage of the two integer fields that follow. For Two discrete lengths and Length within range , it does not matter which value is in which field. |
| Set Interleaved 2 of 5 length 1 (0 to 55) | 0–55 | 14 | Applicable for all scheme choices except Any length , which ignores it. Default value applies only to One discrete length . |
| Set Interleaved 2 of 5 length 2 (0 to 55) | 0–55 | 0 | Applicable for Two discrete lengths and Length within range only. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable ISBT 128 | On Off | ON | Enables International Society of Blood Transfusion (ISBT) 128 symbology. |
| Select an option for concatenating pairs of ISTB code types | Disable Enable Autodiscriminate | Disable | Disable ISBT Concatenation: The device does not concatenate pairs of ISBT codes it encounters. Enable ISBT Concatenation: There must be two ISBT codes for the device to decode and perform concatenation. The device does
                                             not decode single ISBT symbols. Autodiscriminate ISBT Concatenation: The device decodes and concatenates pairs of ISBT codes immediately. If only a single
                                             ISBT symbol is present, the device must decode the symbol the number of times set via ISBT Concatenation Redundancy before
                                             transmitting its data to confirm that there is no additional ISBT symbol. |
| Enable check ISBT table | On Off | ON | If you enable ISBT Concatenation, enable Check ISBT Table to concatenate only those pairs found in this table. |
| ISTB concatenation redundancy | 2 to 20 | 10 | With ISBT Concatenation set to Autodiscriminate, this option sets the number of times the device must decode an ISBT symbol
                                             before determining that there is no additional symbol. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable Matrix 2 of 5 | On Off | ON | Enables or disables the symbology. |
| Enable Matrix 2 of 5 check digit | On Off | OFF |  |
| Enable transmit Matrix 2 of 5 check digit | On Off | OFF | Enables or disables transmit. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable Micro PDF | On Off | ON | Enables or disables the symbology. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable Micro QR | On Off | ON | Enables or disables the symbology. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| MSI Plessey | On Off | ON | Enables or disables the symbology. |
| Number of MSI check digits | One Digit Two Digits | One digit |  |
| Enable transmit MSI check digit | On Off | OFF | Enables or disables transmit. |
| MSI check digit algorithm | MOD 10/MOD11 MOD 10/MOD10 | MOD 10/MOD10 |  |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable PDF 417 | On Off | ON | Enables or disables the symbology. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable QR | On Off | ON | Enables or disables the symbology. |
| QR decoding | Regular Inverse Both | Regular | Sets decoding. |

| Note | Enable EAN/UPC supplementals per option in Administrative settings to enable supplementals for UPC-A or UPC-E or both. |
|---|---|

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable UPC-A | On Off | ON | Enables or disables the symbology. |
| Enable transmit UPC-A check digit | On Off | ON | Enables or disables transmit. |
| Transmit UPC-A preamble | No preamble:0 System character System character and country code | System character | Sets transmit preamble. |

| Note | Enable EAN/UPC supplementals per option in Administrative settings to enable supplementals for UPC-A or UPC-E or both. |
|---|---|

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable UPC-E | On Off | ON | Enables or disables the symbology. |
| Enable transmit UPC-E check digit | On Off | ON | Enables or disables transmit. |
| Transmit UPC-E preamble | No preamble System character System character and country code | System character | Sets transmit preamble. |
| Enable convert UPCE to UPCA | On Off | OFF | Enables or disables conversion. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Inverse 1D Decoding | Dark on light Light on dark Either | Dark on light | Sets decoding. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Supplemental setting for UPCA, UPCE and EAN barcodes | Disable Enable | Disable | Enables or disables supplemental setting. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| EAN/UPC supplementals | Disable Enable | Disable | Global to both EAN 8 and EAN 13. |
| Polarity (all 1-D barcodes) | Dark on light Either Light on dark | Dark on light | Sets polarity. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Replace n | Use control character SPACE List of Latin punctuation or symbols | SPACE | Replaces control character [ n ] with a space or a punctuation. You can also choose to use the control character itself. |

| Control character | Control character decimal |
|---|---|
| NULL (NUL) | 0 |
| Start of Header (SOH) | 1 |
| Start of Text (STX) | 2 |
| End of Text (ETX) | 3 |
| End of Transmission (EOT) | 4 |
| Enquiry (ENQ) | 5 |
| Acknowledge (ACK) | 6 |
| Bell (BEL) | 7 |
| Backspace (BS) | 8 |
| Horizontal Tab (HT) | 9 |
| Line Feed (LF) | 10 |
| Vertical Tab (VT) | 11 |
| Form Feed (FF) | 12 |
| Carriage Return (CR) | 13 |
| Shift Out (SO) | 14 |
| Shift In (SI) | 15 |
| Data Link Escape (DLE) | 16 |
| Data Control 1 (DC1) | 17 |
| Data Control 2 (DC2) | 18 |
| Data Control 3 (DC3) | 19 |
| Data Control 4 (DC4) | 20 |
| Negative ACK (NAK) | 21 |
| Synchronize (SYN) | 22 |
| End Text Block (ETB) | 23 |
| Cancel (CAN) | 24 |
| End Message (EM) | 25 |
| Substitute (SUB) | 26 |
| Escape (ESC) | 27 |
| File Separator (FS) | 28 |
| Group Separator (GS) | 29 |
| Record Separator (RS) | 30 |
| Unit Separator (US) | 31 |

| Latin punctuation or symbol | Description |
|---|---|
| ! | Exclamation point |
| " | Quotation mark |
| # | Number sign |
| $ | Dollar sign |
| % | Percent sign |
| & | Ampersand |
| ' | Apostrophe |
| ( | Left parenthesis |
| ) | Right parenthesis |
| * | Asterisk |
| + | Plus sign |
| , | Comma |
| - | Hyphen-Minus |
| . | Full stop or period |
| / | Forward slash or Solidus |
| : | Colon |
| ; | Semicolon |
| < | Less-than sign |
| = | Equal sign |
| > | Greater-than sign |
| ? | Question mark |
| @ | Commercial at symbol |
| [ | Left square bracket |
| \ | Black slash or Reverse solidus |
| ] | Right square bracket |
| ^ | Tent, control, or Circumflex accent |
| _ | Underline, underscore, or low line |
| ` | Grave accent |
| { | Left curly bracket |
| \| | Pipe, or Vertical line |
| } | Right curly bracket |
| ~ | Tilde |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Application or activity name(s) | String |  | Enter a name for the application or activity. If more than one name, use a comma to separate names. |
| Symbology settings for application(s) entered above |  |  | Set desired symbology settings for the application or activity. |
| Format data |  |  | Select desired symbologies, and set their data manipulation and custom intent settings. |
| Advanced data formatting |  |  | Select desired symbologies, and set custom actions and parameters. |

| Action | Cursor action description | Directions for parameters |
|---|---|---|
| Move forward | Move the cursor forward by n spots. | Enter n in Parameter 1. |
| Move back | Move the cursor backward by n spots. | Enter n in Parameter 1. |
| Move to beginning | Move the cursor to the beginning of the string. | No parameter required. |
| Move to end | Move the cursor to the end of the string. | No parameter required. |
| Move to beginning of sub-string | Move the cursor to the beginning of a sub-string. | Enter the sub-string in Parameter 1. |
| Move to the end of sub-string | Move the cursor to the end of a sub-string. | Enter the sub-string in Parameter 1. |

| Action | Action description | Directions for parameters |
|---|---|---|
| Trim whitespace | Remove leading or trailing whitespaces. | No parameter required. |
| Remove all whitespace | Remove all whitespaces. | No parameter required. |
| Remove all leading zeros | Remove leading zeros on the left of the string. | No parameter required. |
| Pad zeros at beginning | Add n zeros at the beginning. | Enter n in Parameter 1. |
| Replace first sub-string | Replace the first encountered sub-string in the scanned string. | Enter the sub-string that you want to replace in Parameter 1, and enter the new sub-string in Parameter 2. |
| Replace all sub-strings | Replace all encountered sub-string in the scanned string. | Enter the sub-string that you want to replace in Parameter 1, and enter the new sub-string in Parameter 2. |
| Remove characters | Remove characters encountered in the string. | Enter the character in Parameter 1. |
| Add text | Add text | Enter the text in Parameter 1. |
| Add code | Add character as integer code. | Enter integer code of the desired character in Parameter 1. |
| Add tab | Add a Tab from the current position of cursor. Note ScanFlex uses a built-in pause after Tab; therefore, you do not need to manually add a pause. | Note | ScanFlex uses a built-in pause after Tab; therefore, you do not need to manually add a pause. | No parameter required. |
| Note | ScanFlex uses a built-in pause after Tab; therefore, you do not need to manually add a pause. |
| Add enter | Add an Enter at the current position of the cursor. Note ScanFlex uses a built-in pause after Enter; therefore, you do not need to manually add a pause. | Note | ScanFlex uses a built-in pause after Enter; therefore, you do not need to manually add a pause. | No parameter required. |
| Note | ScanFlex uses a built-in pause after Enter; therefore, you do not need to manually add a pause. |

| Note | ScanFlex uses a built-in pause after Tab; therefore, you do not need to manually add a pause. |
|---|---|

| Note | ScanFlex uses a built-in pause after Enter; therefore, you do not need to manually add a pause. |
|---|---|

| Note | By default, the top-left button of the Cisco Wireless Phone 860S is set to Scanner . By default, the bottom-left button of the Cisco Wireless Phone 840S is set to Scanner . |
|---|---|

| Step 1 | Access the Barcode app. |
|---|---|
| Step 2 | Tap the Overflow menu. |
| Step 3 | Tap Test scan . |
| Step 4 | From the Barcode screen, tap the barcode scanner button. |
| Step 5 | Point the barcode reader 1–18 inches (2.5–46 centimeters) from the barcode that you want to scan. |
| Step 6 | Press and hold the programmed Scanner button with the light shining across the entire barcode symbol until the light turns off and you hear a beep. The Barcode type and the Scanned barcode data appear on the Barcode screen. The barcode search button is enabled. |
| Step 7 | Tap the barcode search button to find data about the scanned barcode. The search results appear in the default browser on your phone. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Allow Wi-Fi toggle Allow Internet Toggle (Only For Cisco Wireless Phone 860 only (from version 2.1(0) and later) | On Off | On | If enabled, and if the Allow quick settings tiles is enabled, the user can enable or disable Wi-Fi in the quick settings tiles. If the Allow quick settings tiles is disabled, all the quick settings tiles are not available. |
| Allow airplane mode toggle | On Off | On | If enabled, and if the Allow quick settings tiles is enabled, the user can enable or disable Airplane mode in the quick settings tiles. If the Allow quick settings tiles is disabled, the Airplane mode quick settings tile is not available. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Allow quick settings tiles | On Off | On | If enabled, all enabled quick setting tiles are accessible to the end user. If disabled, all quick setting tiles are inaccessible to the end user. |
| Wi-Fi Internet (Only for Cisco Wireless Phone 860 only (from version 2.1(0) and later) | On Off | On | If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile. If disabled, the quick setting tile is hidden and can't be added. |
| Bluetooth | On Off | On | If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile. If disabled, the quick setting tile is hidden and can't be added. |
| Do not disturb | On Off | On | If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile. If disabled, the quick setting tile is hidden and can't be added. |
| Flashlight | On Off | On | If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile. If disabled, the quick setting tile is hidden and can't be added. |
| Rotation lock Auto rotate (Only for Cisco Wireless Phone 860 only (from version 2.1(0) and later) | On Off | On | If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile. If disabled, the quick setting tile is hidden and can't be added. |
| Battery saver | On Off | On | If enabled and if the Allow quick settings tiles is enabled, the user can control this quick setting tile. If disabled, the quick setting tile is hidden and can't be added. |
| Mobile data | On Off | On | If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile. If disabled, the quick setting tile is hidden and can't be added. |
| Airplane mode | On Off | On | If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile. If disabled, the quick setting tile is hidden and can't be added. |
| Cast Screen cast (Only for Cisco Wireless Phone 860 only (from version 2.1(0) and later) | On Off | On | If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile. If disabled, the quick setting tile is hidden and can't be added. |
| High touch | On Off | On | If enabled and if the Allow quick settings tiles is enabled, the user can control this quick setting tile. If disabled, the quick setting tile is hidden and can't be added. |
| Hotspot | On Off | On | If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile. If disabled, the quick setting tile is hidden and can't be added. |
| Night light | On Off | On | If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile. If disabled, the quick setting tile is hidden and can't be added. |
| Location | On Off | On | If enabled and if the Allow quick settings tiles is enabled, the user can control this quick setting tile. If disabled, the quick setting tile is hidden and can't be added. |
| Invert colors Color inversion (Only for Cisco Wireless Phone 860 only (from version 2.1(0) and later) | On Off | On | If enabled and if the Allow quick settings tiles is enabled, the user can control this quick setting tile. If disabled, the quick setting tile is hidden and can't be added. |
| Data saver | On Off | On | If enabled, and if the Allow quick settings tiles is enabled, the user can control this quick setting tile. If disabled, the quick setting tile is hidden and can't be added. |
| Dark theme | On Off | On | Available from release 1.3(0) onward, the Dark theme setting changes the display from dark text on a light background, to light text on a dark background. If enabled and if the Allow quick settings tiles is enabled, the user can control this quick setting tile. If disabled, the quick setting tile is hidden and can't be added. |
| Nearby share Quick share (Only for Cisco Wireless Phone 860 only (from version 2.1(0) and later) | On Off | On | Available from release 1.3(0) onward, Nearby share is an Android platform setting that enables phones to share files, links, and pictures with other devices within a certain
                                             range. If enabled and if the Allow quick settings tiles is enabled, the user can control this quick setting tile. If disabled, the quick setting tile is hidden and can't be added. |
| For Cisco Wireless Phone 860 Only (version 2.1(0) and later) |
| Alarm | On Off | On | Opens the Google Clock app to set an alarm or access other Clock functions. |
| Device Control | On Off | On | Enables control of smart devices connected to the Google Home app. |
| Screen record | On Off | On | Opens screen recording options. |
| Extra dim | On Off | On | Enables users to dim the screen when working in low-light environments. |
| QR scan | On Off | On | Launches the Camera app to scan a QR code. |
| Color correction | On Off | On | Allows a user to modify how colors display on their phone and are useful for a vision impaired user or for the user who want
                                             to set their display to grayscale. To access Android Color correction, navigate to Settings > Accessibility > Color and motion > Color correction. This quick settings tile allows a user to toggle Color correction on or off. |
| Live caption | On Off | On | Provides real-time captions for media playback. This parameter may be unavailable even if it is enabled in the app. To make
                                          this feature available, navigate to Android Settings > Accessibility > Captions > Live Captions > Download. |
| Calculator | On Off | On | Launches the Google Calculator app. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Allow notification shade settings gear | On Off | On | If enabled, the user can make Android settings changes through the gear in the notification shade. If disabled, the Android settings gear in the notification shade is not accessible to the user. Note If you are using a Smart Launcher to restrict user access to certain apps and settings, we recommend that you disallow this
                                                         setting through the Cisco Wireless Phone Configuration Management tool . Otherwise, users can easily open apps that aren't on the Smart Launcher. | Note | If you are using a Smart Launcher to restrict user access to certain apps and settings, we recommend that you disallow this
                                                         setting through the Cisco Wireless Phone Configuration Management tool . Otherwise, users can easily open apps that aren't on the Smart Launcher. |
| Note | If you are using a Smart Launcher to restrict user access to certain apps and settings, we recommend that you disallow this
                                                         setting through the Cisco Wireless Phone Configuration Management tool . Otherwise, users can easily open apps that aren't on the Smart Launcher. |
| Allow manage notification settings button (Only for Cisco Wireless Phone 860 only (from version 2.1(0) and later) | On Off | On | If enabled, manages the notification settings. |

| Note | If you are using a Smart Launcher to restrict user access to certain apps and settings, we recommend that you disallow this
                                                         setting through the Cisco Wireless Phone Configuration Management tool . Otherwise, users can easily open apps that aren't on the Smart Launcher. |
|---|---|

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Allow time zone configuration | On Off | On | If enabled, the user can manually change the time zone on the phone from Settings > System > Date & Time . If disabled, the user cannot manually change the time zone on the phone. |
| Allow time format configuration | On Off | On | If enabled, the user can manually change the time format on the phone from Settings > System > Date & Time . If disabled, the user cannot manually change the time format on the phone. |
| Allow automatic time zone toggle | On Off | On | Not applicable for Wi-Fi enabled phones. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Allow emergency call button on lockscreen | On Off | On | If enabled, displays the EMERGENCY button when the phone screen is locked. Note Regardless of whether you enable or disable this setting, a RETURN to CALL button is present if the phone is in a call and locked. | Note | Regardless of whether you enable or disable this setting, a RETURN to CALL button is present if the phone is in a call and locked. |
| Note | Regardless of whether you enable or disable this setting, a RETURN to CALL button is present if the phone is in a call and locked. |

| Note | Regardless of whether you enable or disable this setting, a RETURN to CALL button is present if the phone is in a call and locked. |
|---|---|

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Lock screen proximity detection | On Off | On | If enabled, the phone screen automatically locks when the user covers the proximity sensor. This prevents accidental input
                                             when a user puts the phone in a pocket. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| NTP server address | String | 2.android.pool.ntp.org | The Network Time Protocol (NTP) domain name or IP address. Deploy a local time server for phones that are not connected to the internet and therefore getting their time from Google
                                             or some other cloud server. Note From release 1.5(0), you can also define a server in DHCP option 42 to provide NTP service in case the NTP server isn't available. | Note | From release 1.5(0), you can also define a server in DHCP option 42 to provide NTP service in case the NTP server isn't available. |
| Note | From release 1.5(0), you can also define a server in DHCP option 42 to provide NTP service in case the NTP server isn't available. |
| Time zone | Choice | Unset/deferred | A drop-down list of all the available time zones. Unset/deferred does not set a time zone through this configuration remotely. Caution The time zone settings are listed by country/region/city and also have a number setting under Etc. (Etc/GMT+/- ##). However,
                                                         the number values (for example, –2 or +2) are reversed from usual GMT time designations. Your setting for Etc/GMT+2 transposes
                                                         into the actual setting of GMT-2). Therefore, we recommend that you use the country/region/city option whenever possible. | Caution | The time zone settings are listed by country/region/city and also have a number setting under Etc. (Etc/GMT+/- ##). However,
                                                         the number values (for example, –2 or +2) are reversed from usual GMT time designations. Your setting for Etc/GMT+2 transposes
                                                         into the actual setting of GMT-2). Therefore, we recommend that you use the country/region/city option whenever possible. |
| Caution | The time zone settings are listed by country/region/city and also have a number setting under Etc. (Etc/GMT+/- ##). However,
                                                         the number values (for example, –2 or +2) are reversed from usual GMT time designations. Your setting for Etc/GMT+2 transposes
                                                         into the actual setting of GMT-2). Therefore, we recommend that you use the country/region/city option whenever possible. |
| Time format | Unset/deferred 12 hours 24 hours | Unset/deferred | Unset/deferred does not set a time format through this configuration remotely. |
| Automatic time zone | On Off | On | Enables or disables automatic time zone. |
| Allow location to set time ( For Cisco Wireless Phone 860 only (from version 2.1(0) and later) | On Off | On | Enables to set time for a location. |

| Note | From release 1.5(0), you can also define a server in DHCP option 42 to provide NTP service in case the NTP server isn't available. |
|---|---|

| Caution | The time zone settings are listed by country/region/city and also have a number setting under Etc. (Etc/GMT+/- ##). However,
                                                         the number values (for example, –2 or +2) are reversed from usual GMT time designations. Your setting for Etc/GMT+2 transposes
                                                         into the actual setting of GMT-2). Therefore, we recommend that you use the country/region/city option whenever possible. |
|---|---|

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Display device info | On Off | Off | If enabled, provides four text fields for more information about the user who is assigned this phone. This information appears
                                             in the phone notifications and on a locked screen. |
| Device info 1 | String |  | First parameter for device information notification |
| Device info 2 | String |  | Second parameter for device information notification |
| Device info 3 | String |  | Third parameter for device information notification |
| Device info 4 | String |  | Fourth parameter for device information notification |

| Field | Field type | Default | Description |
|---|---|---|---|
| Device name | String |  | Allows you to set the Android device name. This is useful when you use an Enterprise Mobility Management (EMM) application to configure the phones. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Battery optimization allow list | Comma-delimited list of package names |  | Android Battery Saver mode curtails functionality to conserve the battery life. However, it also reduces functionality by
                                             turning off apps that you might want to remain operational. Apps that you add to this list remain operational when the user
                                             turns on the phone's Battery Saver mode. Caution Apps that you add to this list increase battery usage by staying awake. Ensure that users have extra batteries available. | Caution | Apps that you add to this list increase battery usage by staying awake. Ensure that users have extra batteries available. |
| Caution | Apps that you add to this list increase battery usage by staying awake. Ensure that users have extra batteries available. |
| Allow battery saver | On Off | On | If enabled, allows the user to turn battery saver mode on or off. Battery saver mode can have a significant impact on what apps are available or functioning. |
| Battery percentage | User controlled Enable Disable | User controlled | User controlled: makes the Battery percentage Android setting available for the user to show or hide the battery percentage in the phone status bar. Enable and Disable: make the Battery percentage Android setting unavailable to users and allow the EMM application to control the setting. Enable displays the battery percentage on the status bar. Disable means that the battery percentage doesn't display on the phone. |

| Caution | Apps that you add to this list increase battery usage by staying awake. Ensure that users have extra batteries available. |
|---|---|

| Field | Field choices | Default | Description |
|---|---|---|---|
| Google™ voice typing | On Off | On | Enables or disables Google voice typing. |

| Field | Field choices | Default | Description |
|---|---|---|---|
| Time to sleep after inactivity | User controlled 15 seconds 30 seconds 1 minute 5 minutes 10 minutes 30 minutes | User controlled | Sets the amount of time before the screen times out after inactivity. User controlled allows users to control the sleep settings available in the Android settings menu. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Display size | User controlled Small Default Large | User controlled | Sets the display size, which includes all interface elements such as text and images. Note For the Cisco Wireless Phone 840 and 840S , the large display size is not currently available, so if you choose this option, the phone uses the default display size. | Note | For the Cisco Wireless Phone 840 and 840S , the large display size is not currently available, so if you choose this option, the phone uses the default display size. |
| Note | For the Cisco Wireless Phone 840 and 840S , the large display size is not currently available, so if you choose this option, the phone uses the default display size. |
| Font size | User controlled Small Default Large Largest | User controlled | Sets the font size. |
| System navigation | User controlled Gesture navigation 2-button navigation 3-button navigation | User controlled | Sets the system navigation. Note For the Cisco Wireless Phone 840 and 840S , 2-button navigation is not currently available, so if you choose this option, the phone uses the 3-button navigation. | Note | For the Cisco Wireless Phone 840 and 840S , 2-button navigation is not currently available, so if you choose this option, the phone uses the 3-button navigation. |
| Note | For the Cisco Wireless Phone 840 and 840S , 2-button navigation is not currently available, so if you choose this option, the phone uses the 3-button navigation. |
| Auto-rotate screen | User controlled Enable Disable | User controlled | User controlled: makes the Auto-rotate screen Android setting available for users to turn automatic screen rotation on or off. Enable and Disable: make the Auto-rotate screen Android setting unavailable to users and allow the EMM application to control the setting. Enable turns on automatic screen rotation. Disable means that automatic screen rotation is not available. |

| Note | For the Cisco Wireless Phone 840 and 840S , the large display size is not currently available, so if you choose this option, the phone uses the default display size. |
|---|---|

| Note | For the Cisco Wireless Phone 840 and 840S , 2-button navigation is not currently available, so if you choose this option, the phone uses the 3-button navigation. |
|---|---|

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Dialpad tones | User controlled Enable Disable | User controlled | Tones available on the phone or custom tones that are programmed in an EMM application . |
| Touch sounds | User controlled Enable Disable | User controlled | Percussive sounds available on the phone or in an EMM application . |
| Vibrate on tap | User controlled Enable Disable | User controlled | A vibration when the user taps the phone touchscreen. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Ringtones | List of available ringtones | All | Select the system ringtone sounds that you want to be available. |
| Default ringtone | Default ringtone List of available ringtones | Default (Flutey Phone) | Must be enabled on the Ringtones list. |
| Notification sounds | List of available notification sounds | All | Select the system notification sounds that you want to be available. |
| Default notification sound | Default notification sound List of available notification sounds | Default (Pixie Dust) | Must be enabled on the Notification sounds list. |
| Alarm sounds | List of available alarm sounds | All | Select the system alarm sounds that you want to be available. |
| Default alarm sound | Default alarm sound List of available alarm sounds | Default (Cesium) | Must be enabled on the Alarm sounds list. |

| Note | Using CUCM, you can download more ringtones, notification sounds, and alarm sounds. The downloaded ringtones and sounds will
                                             appear in their respective list. |
|---|---|

| Field | Field choices | Default | Description |
|---|---|---|---|
| Jump to camera Quickly open camera (Only For Cisco Wireless Phone 860 only (from version 2.1(0) and later) | User controlled Enable Disable | User controlled | Allows certain camera settings available in the Android settings menu to be controlled by an EMM application or by the end user. Permits the user to set the Jump to camera Android setting. User controlled implies the Android settings value takes precedence. |

| Field | Field type | Default | Description |
|---|---|---|---|
| Lock screen wallpaper | String | Not configured | Enter the complete file path starting with the exact location of the image file—where is it stored on the phone. Example /sdcard/<name_of_image_file> . |
| Home screen wallpaper | String | Not configured | Enter the complete file path. |

| Note | Using CUCM, you can download more wallpapers for Lock screen and Home screen. The downloaded wallpapers will appear in their
                                             respective list. |
|---|---|

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Reboot command ID | String |  | Sets reboot command ID. |
| Reboot schedule type | Timer When next plugged-in | Timer | Sets when to schedule reboot. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Time until first automatic reboot attempt | Immediately (0 minutes) 1 minute 5 minutes 10 minutes 15 minutes 30 minutes 1 hours 2 hours 3 hours 4 hours 6 hours 8 hours 12 hours | Immediately (0 minutes) | Sets time until first automatic reboot attempt. |
| Number of times to allow delaying reboot attempt | None 1 2 3 4 6 8 12 Unlimited | None | Sets the number of times to allow a user to delay the reboot attempt. |
| Time to delay reboot attempt for | 1 minute 5 minutes 10 minutes 15 minutes 30 minutes 1 hours 2 hours 3 hours 4 hours 6 hours 8 hours 12 hours | 1 minute | Sets the time to delay the reboot attempt. |

| Caution | Review the bands and channels in use at the intended location before you make any changes. If you select the wrong band or
                                       channels, you can permanently disconnect phones from the network. Contact Cisco TAC if incorrect band selection disables the
                                       phones. Finally, you may need to manually reset factory defaults to the phones. |
|---|---|

| Field | Description |
|---|---|
| SSID | Service Set Identifier (SSID) is the unique name that identifies the wireless network. |
| AP name | Access point (AP) name displays the name of the AP. |
| BSSID | Basic Service Set Identifier (BSSID) is the MAC of the radio MAC + SSID. |
| Channel | Channel displays the AP radio channel. |
| RSSI | Received Signal Strength Indicator (RSSI) is the strength of the signal connecting the phone and access point. |
| Noise | Noise indicates the level of background noise in the environment. |
| CU | Channel utilization (CU) shows how busy the channel is. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Wi-Fi Low RSSI threshold | Integer –55 to –100 | –67 | Voice quality can degrade if the Wi-Fi signal is too weak. The RSSI changes as the user moves closer to or away from the connected
                                             AP. The RSSI threshold value setting is the RSSI level at or below which the phone seeks a better AP. The phone uses many
                                             attributes of an AP to determine if it is a good candidate including the current load on the AP, the available bandwidth on
                                             the AP, and channel. Sometimes the best AP may have an RSSI value lower than other candidates. Caution Consult Cisco TAC before you change the RSSI threshold value. | Caution | Consult Cisco TAC before you change the RSSI threshold value. |
| Caution | Consult Cisco TAC before you change the RSSI threshold value. |

| Caution | Consult Cisco TAC before you change the RSSI threshold value. |
|---|---|

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Auto | Enabled Disabled | Enabled | When enabled: The phone uses any available band or channel. You can’t select a specific band or channel. The phone ignores, but does not forget, your individual channel preferences. When disabled, you can select which band to enable and select specific channels within each band. You can't disable both Wi-Fi bands at the same time. |
| 2.4 GHz Wi-Fi band | Enabled Disabled | Enabled | If enabled: The phone uses any available channel in the 2.4 GHz band. You can enable or disable specific channels within 2.4 GHz band. |
| 5 GHz Wi-Fi band | Enabled Disabled | Enabled | If enabled: The phone uses any available channel in the 5 GHz band. You can enable or disable specific channels within 5 GHz subbands. Each subband includes a group of channels. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Channel 1 (2412 MHz) | On Off | On | Enables channel. |
| Channel 2 (2417 MHz) | On Off | On | Enables channel. |
| Channel 3 (2422 MHz) | On Off | On | Enables channel. |
| Channel 4 (2427 MHz) | On Off | On | Enables channel. |
| Channel 5 (2432 MHz) | On Off | On | Enables channel. |
| Channel 6 (2437 MHz) | On Off | On | Enables channel. |
| Channel 7 (2442 MHz) | On Off | On | Enables channel. |
| Channel 8 (2447 MHz) | On Off | On | Enables channel. |
| Channel 9 (2452 MHz) | On Off | On | Enables channel. |
| Channel 10 (2457 MHz) | On Off | On | Enables channel. |
| Channel 11 (2462 MHz) | On Off | On | Enables channel. |
| Channel 12 (2467 MHz) | On Off | On | Enables channel. |
| Channel 13 (2472 MHz) | On Off | On | Enables channel. |
| Channel 14 (2484 MHz) | On Off | On | Enables channel. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Channel 36 (5180 MHz) | On Off | On | Enables channel. |
| Channel 40 (5200 MHz) | On Off | On | Enables channel. |
| Channel 44 (5220 MHz) | On Off | On | Enables channel. |
| Channel 48 (5140 MHz) | On Off | On | Enables channel. |
| Channel 52 DFS (5260 MHz) | On Off | On | Enables channel. |
| Channel 56 DFS (5280 MHz) | On Off | On | Enables channel. |
| Channel 60 DFS (5300 MHz) | On Off | On | Enables channel. |
| Channel 64 DFS (5320 MHz) | On Off | On | Enables channel. |
| Channel 100 DFS (5500 MHz) | On Off | On | Enables channel. |
| Channel 104 DFS (5520 MHz) | On Off | On | Enables channel. |
| Channel 108 DFS (5540 MHz) | On Off | On | Enables channel. |
| Channel 112 DFS (5560 MHz) | On Off | On | Enables channel. |
| Channel 116 DFS (5580 MHz) | On Off | On | Enables channel. |
| Channel 120 DFS (5600 MHz) | On Off | On | Enables channel. |
| Channel 124 DFS (5620 MHz) | On Off | On | Enables channel. |
| Channel 128 DFS (5640 MHz) | On Off | On | Enables channel. |
| Channel 132 DFS (5660 MHz) | On Off | On | Enables channel. |
| Channel 136 DFS (5680 MHz) | On Off | On | Enables channel. |
| Channel 140 DFS (5700 MHz) | On Off | On | Enables channel. |
| Channel 144 DFS (5720 MHz) | On Off | On | Enables channel. |
| Channel 149 (5745 MHz) | On Off | On | Enables channel. |
| Channel 153 (5765 MHz) | On Off | On | Enables channel. |
| Channel 157 (5785 MHz) | On Off | On | Enables channel. |
| Channel 161 (5805 MHz) | On Off | On | Enables channel. |
| Channel 165 (5825 MHz) | On Off | On | Enables channel. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| FT | Preferred Not preferred | Preferred | Fast Transition (FT) |
| CCKM Note This parameter is not available for Cisco Wireless Phone 860 from version 2.1(0) and later | Note | This parameter is not available for Cisco Wireless Phone 860 from version 2.1(0) and later | Preferred Not preferred | Preferred | Cisco Centralized Key Management (CCKM) |
| Note | This parameter is not available for Cisco Wireless Phone 860 from version 2.1(0) and later |
| CAC Note This parameter is not available for Cisco Wireless Phone 860 from version 2.1(0) and later | Note | This parameter is not available for Cisco Wireless Phone 860 from version 2.1(0) and later | ON OFF | OFF | Call Admission Control (CAC) |
| Note | This parameter is not available for Cisco Wireless Phone 860 from version 2.1(0) and later |

| Note | This parameter is not available for Cisco Wireless Phone 860 from version 2.1(0) and later |
|---|---|

| Note | This parameter is not available for Cisco Wireless Phone 860 from version 2.1(0) and later |
|---|---|

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable Sound Stage | On Off | Off | Enables Sound Stage app. If the Enable Sound Stage is disabled, all the admin settings tiles are not available. |
| Enable sound profile switch | On Off | Off | If the Enable Sound Stage tile is enabled, you can enable or disable Enable sound profile switch . |
| Enable normal profile | On Off | Off | If the Enable Sound Stage tile is enabled, you can enable or disable Enable normal profile . |
| Enable loud profile | On Off | Off | If the Enable Sound Stage tile is enabled, you can enable or disable Enable loud profile . |
| Enable soft profile | On Off | Off | If the Enable Sound Stage tile is enabled, you can enable or disable Enable soft profile . |
| Enable silent profile | On Off | Off | If the Enable Sound Stage tile is enabled, you can enable or disable Enable silent profile . |
| Enable personal profile | On Off | Off | If the Enable Sound Stage tile is enabled, you can enable or disable Enable personal profile . |
| Persist active profile notification | On Off | Off | If the Enable Sound Stage tile is enabled, you can enable or disable Persist active profile notification . |
| Switch profiles silently | On Off | Off | If the Enable Sound Stage tile is enabled, you can enable or disable Switch profiles silently . |

| Note | The audio profile could also be changed by scanning a programmed NFC tag without the phone open. |
|---|---|

| Step 1 | Access the Sound Stage app. |
|---|---|
| Step 2 | Tap the Change button for the active audio profile. |
| Step 3 | Choose one of the following audio profiles. Normal Loud Soft Silent Personal |

| Note | If you have set up both behavior based and time based profile switch rules, the high priority will be behavior based. |
|---|---|

| Note |  |
|---|---|

| Step 1 | Access the Sound Stage app. |
|---|---|
| Step 2 | Tap the Overflow menu. |
| Step 3 | Select Settings > Profile switch rules . |
| Step 4 | Tap Charging . |
| Step 5 | Choose one of the following Switch to options . Normal Loud Soft Silent Personal |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Enable Web API | On Off | Off | Enables or disables Web API. |
| Enable Web access | On Off | Off | Enables or disables Web access. |
| Data format | XML JSON | XML | Sets the data format. XML is the only supported format. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Username | String |  | Defines the username that the phone requires to authenticate polling. |
| Password | String |  | Defines the password that the phone requires to authenticate polling. |
| Respond mode | Requester URL | Requester | Defines the method for sending the requested polling data. If the Respond mode is requester, the response is automatically sent to the HTTP server running at the address where the request was made. |
| URL | String |  | When the Respond mode is set as URL, this field defines the URL of a valid HTTP server that gets the response. You must enter the URL. This can be a different address than the requester. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Username | String |  | Defines the username for the Web API to do any kind of push. |
| Password | String |  | Defines the password for the Web API to do any kind of push. |
| Push alert priority | All Critical High Important Normal None | All | Sets the priority for messages from the app. Only messages with the selected priority level display. All—Allows all priority push messages. Critical—Allows only critical push messages. High—Allows only high priority push messages. Important—Allows only important push messages. Normal—Allows only normal push messages. None—Discards all push messages. |
| Server root URL |  |  | Defines the URL of the application server. This root URL is combined with the phone address and sent to the phone’s browser. For example, if the application server root URL is http://172.24.128.85:8080/sampleapps and the relative URL is /examples/sample.html , the URL that is sent to the web browser on the phone is http://172.24.128.85:8080/sampleapps/examples/sample.html . The URL can be either HTTP or HTTPS. |
| Enable notification ringtone | On Off | Off | Defines whether a notification ringtone sound plays when a phone receives a push message. The notification sound that plays is set by the user in the phone Settings > Sound > Default notification sound . |
| Web API volume | 0–100 | 50 | Sets the volume for the push ringtone. |

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Shortcut title | String |  | Defines a title for the web application shortcut. The title displays in the widget box on the phone after you reboot the phone. |
| Shortcut URL | String |  | Defines the application URL. You can enter any URL available to the phones. |

| Step 1 | Long press the home screen. |
|---|---|
| Step 2 | Tap Widgets . |
| Step 3 | Touch and hold the shortcut. |
| Step 4 | Drag the shortcut to the desired location on a launcher screen. |

| Note | To edit an existing event URL, delete it and reenter the information with the new URL name or address. |
|---|---|

| Field | Field type or choices | Default | Description |
|---|---|---|---|
| Notification name | String |  | Defines a descriptive label for the event. |
| Notification URL | String |  | Defines the URL for the event. |
| None | On Off | On | By default, there are no notification events. |
| All | On Off | Off | Sends notifications about all phone events when enabled. |
| Cisco Phone events: Outgoing | On Off | Off | Sends notifications about all outgoing phone events when enabled. |
| Cisco Phone events: Incoming | On Off | Off | Sends notifications about all incoming phone events when enabled. |
| Cisco Phone events: State Change | On Off | Off | Sends notifications about all phone state change events when enabled. |
| Cisco Phone events: Login/out | On Off | Off | Sends notifications about all phone login and logout events when enabled. |
| Cisco Phone events: Registration | On Off | Off | Sends notifications about all phone registration events when enabled. |
| Cisco Phone events: Unregistration | On Off | Off | Sends notifications about all phone unregistration events when enabled. |
| Emergency events | On Off | Off | Sends notifications about all Emergency events when enabled. |