---
doc_id: help-webex-com-en-us-article-nwwodwp-configure-office-hours-for-9800-8875-control-hub-59e28b4530
source_url: https://help.webex.com/en-us/article/nwwodwp/Configure-Office-Hours-for-9800/8875-(Control-Hub)
retrieved_at: 2026-11-02T13:05:43.610468+00:00
---

## Overview

Two power-saving options are available on the phone to reduce power consumption during
          periods of inactivity.

Display Off Mode

When the Office Hours feature is enabled, the phone turns off its display according to
          the configured schedule. Users can light up the display by pressing any key on the phone.

Deep Sleep Mode

In Deep Sleep Mode, the phone automatically powers down during the designated periods.
          You can choose to enable Deep Sleep Mode exclusively for non-workdays, or for both
          non-workdays and non-working hours on workdays.

To wake up the phone, perform the appropriate action for your phone model:

- Press the Select button on the Navigation Cluster.

- Tap the Home button.

- Press the Power button.

While in Deep Sleep Mode, no calls, including emergency calls, can be made on the
              phone; and the Action button on the top-right of the device isn't accessible.

Phones in deep sleep show as Offline (Deep Sleep) in Control
        Hub.

Display Off

Deep Sleep

(Controlled by phone)

Cisco Smart Power

(Deep Sleep controlled by switch)

## Enable your phone to manage its own power modes

By default, the Office Hours feature is enabled on your phone. The
        default office hours are set to 7:00 to 19:00 from Monday to Friday. The phone turns off the
        screen outside of the designated hours. You can customize working hours, workdays, and the
        power-saving modes — Display Off and Deep Sleep.

From the customer view in Control Hub , go to Devices , and then select your phone.

Select All configurations .

Navigate to Phone > Office Hours .

Customize working hours and workdays to reflect the business hours of your users.

Enabled : By default,  the Office Hours feature is enabled.
                If set to False, your phone won't enter power saving mode.

Workdays : The default workdays are Monday through Friday.
                Change the workdays as needed.

Working Hours Start and Working Hours
                  End : The default working hours are set to 7:00 to 19:00. Change the
                setting as needed.

For more information about the parameters, see Parameters for Office
              Hours .

Configure the settings for Display Off Mode for both working hours and non-working
          hours.

Cisco Desk Phone 9811 doesn't support Display Off Mode.

In Office Hours > Display Off : By default, the phone
                display remains on during working hours. To enable the phone to enter Display Off
                Mode when inactive, select timeout period from the list.

Outside Office Hours > Display Off Idle Timeout : Set the
                timeout period in minutes for the phone to automatically turn off the screen after
                being awakened during Display Off Mode.

Outside Office Hours > LED Indicator In Display Off Mode :
                This setting determines whether to turn off the Front Arc LED when the phone enters
                Display Off Mode, both during or outside office hours. By default, the Front Arc LED
                remains illuminated after the phone enters Display Off Mode. When set to disabled,
                the Front Arc LED is off in Display Off Mode.

For more information about the parameters, see Parameters for Office
              Hours .

Configure the settings for Deep Sleep Mode for the 9800 Series phones.

Deep Sleep Mode on Cisco Video Phone 8875 and Cisco Desk Phone 9811 can only be enabled by Cisco switches through the smart power feature. To
                  configure the smart power settings, follow the steps in Allow Cisco switches to manage power modes for your phones (smart power) .

A random timer is applied on top of the specified power-on and power-off times to
                  avoid sudden surges in power demand or network traffic. The phone powers off with
                  a random delay of 0 to 10 minutes after the specified power-off time, and powers
                  on 0 to 60 minutes before the specified power-on time, randomly. Contact Cisco
                  Technical Assistance Center (TAC) if you want to modify the random timer.

Deep Sleep Enabled : Enable this feature to allow the phone
                to power off outside office hours.

Phone Off Time After Working Hour End : Set the timeout
                period for the phone to automatically power off after the time specified in the Working Hours End field. The default setting is 60
                minutes.

Phone On Time Before Working Hour Start : Set the timeout
                period for the phone to wake up from Deep Sleep Mode before the time specified in
                the Working Hours Start field. The default setting is 60
                minutes.

Enable Audible Alert (Optional): If set to True, the phone
                plays audio tone to alert the user before it enters Deep Sleep Mode.

Idle Timeout : Set timeout period for the phone to enter Deep
                Sleep Mode.

For more information about the parameters, see Parameters for Office
              Hours .

Select Next .

Review your changes and select Apply .

Select Close to close the page.

## Allow Cisco switches to manage power modes for your phones (smart power)

The smart power feature allows Cisco Smart Switches to put your phone into Deep Sleep
          Mode and wake it up based on the office hours configured in Control Hub.

Before you begin

Your phone uses Power over Ethernet (PoE) as the power source. If a power cube is
            connected, the smart power feature is automatically disabled.

Your phone is connected to a Cisco Smart Switch C9350 with IOS XE 17.18.2 or later.

To use the smart power feature, you must first enable the Office Hours
              feature on your phone .

From the customer view in Control Hub , go to Devices , and then
          select your phone.

Select All configurations .

Navigate to the Phone > Office Hours > Office Hours > Outside Office Hours > Smart Power .

Configure the following parameters:

- False (Default): Disables smart power.

- Non-work Day Only : Enables smart power only on
                  non-working days.

- All Days : Enables smart power always, on both work days
                  and non-work days.

A security secret is required for the smart power domain. Contact Cisco Technical
                  Assistance Center (TAC) to add your secret.

For more information about these parameters, see Parameters for Office
              Hours .

Select Next .

Review your changes and select Apply .

Select Close to close the page.

## Parameters for Office Hours

Default: True

Options: False, True

8875

9841

9851

9861

9871

Set this option to True to enable the Office Hours feature for your
                  phones. The Office Hours feature is designed to minimize power consumption during
                  inactivity periods.

You can configure the phone to automatically turn off the screen (Display Off
                  Mode) or power off (Deep Sleep Mode) outside of the designated working periods.

Default: Disabled

Options: Disabled, In 1 minute, In 5 minutes, In 30 minutes

8875

9841

9851

9861

9871

Enable or disable Display Off Mode during office
                  hours. This feature is disabled by default, keeping the phone screen always on
                  during office hours. To enable this feature, select a timeout duration from the
                  available options. For example, if set to "In 5 minutes", the phone screen will
                  automatically turn off after 5 minutes of inactivity.

The LED indicator follows the setting found in Outside Office Hours > Display Off > LED Indicator In Display Off Mode .

When smart power isn't applied, the Deep Sleep settings work with
                  the office hours settings to determine the deep sleep schedule on 9841, 9851,
                  9861, and 9871.

When smart power is applied, the switch also uses these
                  settings to control the deep sleep mode on all applicable phones.

Default: False

Options: False, Non-work Day Only, All Days

9841

9851

9861

9871

Enable or disable Deep Sleep Mode on the phone. When enabled, this feature
                  automatically powers off the phone outside of the designated office hours.

This option works only when the Office Hours is enabled.

When set to False , the phone will not enter Deep Sleep
                  Mode.

When set to Non-work Day Only , the phone will power off
                  exclusively on non-workdays. For the specified workdays, the phone will only turn
                  off the screen outside of the specified working hours.

When set to All Days , the phone will power off during both
                  non-workdays and non-working hours on workdays.

Set working hours for workdays using the Working Hour
                    Start and Working Hour End fields.

Default: 60

Options: 0 - 360

8875

9811

9841

9851

9861

9871

Set the timeout period, in minutes, for the phone to automatically power off
                  after the time specified in the Working Hours End field. If
                  you want the phone to enter Deep Sleep Mode immediately after working hours, set
                  it to 0.

When the smart power feature is applied, the switch uses this
                    setting to control the phone's power mode.

Default: 60

Options: 0 - 360

8875

9811

9841

9851

9861

9871

Set the timeout period for the phone to wake up from Deep Sleep Mode before the
                  time specified in the Working Hours Start field. If you
                  want the phone to wake up until working hours start, set it to 0.

When the smart power feature is applied, the switch uses this
                    setting to control the phone's power mode.

Default: False

Options: False, True

8875

9811

9841

9851

9861

9871

Enable or disable the phone to play audio tone to alert the user before it enters
                  Deep Sleep Mode.

Default: 30

Options: 1 - 60

8875

9811

9841

9851

9861

9871

This setting applies to the following two scenarios:

Ten minutes
                      before the scheduled deep sleep, a message pops up to notify the user that the
                      phone will power off in ten minutes, and a countdown starts. When it times
                      out, the phone powers off.

During the countdown period, if there is a
                      system activity such as an incoming call, firmware upgrade, or provisioning
                      resync, the countdown will restart. For example, if you have set this field to
                      20, the countdown will restart in 20 minutes after the activity completes. If
                      the phone restarts or its configuration is changed during the countdown, the
                      power-off notification appears again after the restart, and the countdown
                      continues.

After the specified idle timeout period, the phone displays a
                      power-off notification. The countdown shown in the notification is based on
                      the configured idle timeout value.

Examples

If you set the idle timeout to more than 10 minutes (for example, 20
                            minutes), a message appears after the phone has been idle for 20
                            minutes, notifying the user that the phone will power off in 10
                            minutes.

If you set the idle timeout to less than 10 minutes (for example, 6
                            minutes), a message appears after the phone has been idle for 6 minutes,
                            notifying the user that the phone will power off in 6 minutes.

During the countdown period, if there is a system activity such as
                      an incoming call, firmware upgrade, or provisioning resync, the countdown will
                      restart. For example, if you have set this field to 20, the countdown will
                      restart in 20 minutes after the activity completes.

The following notes apply to both scenarios described above.

If a user interacts with the phone during the countdown period — such as
                          by answering or declining calls, or pressing keys — the phone will remain
                          active and will not enter Deep Sleep Mode for the rest of the day.

When the smart power feature is applied, the switch uses this
                    setting to control the phone's power mode.

Default: 5

Options: 1 - 60

8875

9841

9851

9861

9871

Set the timeout period in minutes for the phone to automatically turn off the
                  screen after being awakened during Display Off Mode.

Default: Enabled

Options: Enabled, Disabled

8875

9841

9851

9861

9871

This field is available in the Outside Office Hours section.

This setting determines whether to turn off the Front Arc LED on 9800 Series or
                  the Home button LED on 8875 when the phone enters Display Off Mode, both during or
                  outside office hours. By default (Enabled), the LED remains illuminated after the
                  phone enters Display Off Mode. When set to disabled, the LED is off in Display Off
                  Mode.

Supported only on phones powered by Power over
                  Ethernet (PoE).

8875

9811

9841

9851

9861

9871

The smart power domain that the phone belongs to. Max 128 characters.

A security secret is required for the smart power domain. Please contact the
                    Cisco Technical Assistance Center (TAC) to add your secret.

Default: False

Options: False, Non-work Day Only, All Days

8875

9811

9841

9851

9861

9871

Enable or disable the smart power feature. By default, smart power is disabled.
                    Set it to Non-work Day Only or All Days as needed to enable this feature.

The setting is effective only when a valid domain and security secret are
                    provided.

Default: Monday through Friday

8875

9811

9841

9851

9861

9871

Customize the workdays by selecting the desired days.

During non-workdays, the phone will automatically turn off the screen. By
                  default, workdays are set from Monday to Friday.

This setting also applies to Deep Sleep Mode, if enabled. If you choose to enable
                  Deep Sleep Mode exclusively for non-workdays, the phone will power off during
                  those days. If you enable Deep Sleep Mode for all days, the phone will power off
                  during non-working hours on workdays and throughout non-workdays.

Set working hours for workdays using the Working Hours
                    Start and Working Hours End fields.

Default: 19:00

8875

9811

9841

9851

9861

9871

Set the end time for working hours using the 24-hour format. Outside of the
                  specified working hours, the phone will automatically turn off the screen, or
                  enter Deep Sleep Mode only when Deep Sleep Enabled is set
                  to All Days .

Examples: 09:00 for 09:00 am; 17:30 for 05:30 pm

Ensure that the interval between the start and end time longer than 60
                    minutes.

Default: 07:00

8875

9811

9841

9851

9861

9871

Set the start time for working hours using the 24-hour format. Outside of the
                  specified working hours, the phone will automatically turn off the screen, or
                  enter Deep Sleep Mode only when Deep Sleep Enabled is set
                  to All Days .

Examples: 09:00 for 09:00 am; 17:30 for 05:30 pm

| Feature | 8875 | 9811 | 9841 | 9851 | 9861 | 9871 |
|---|---|---|---|---|---|---|
| Display Off | Yes | No | Yes | Yes | Yes | Yes |
| Deep Sleep (Controlled by phone) | No | No | Yes | Yes | Yes | Yes |
| Cisco Smart Power (Deep Sleep controlled by switch) | Yes | Yes | Yes | Yes | Yes | Yes |

| 1 | From the customer view in Control Hub , go to Devices , and then select your phone. |
|---|---|
| 2 | Select All configurations . |
| 3 | Navigate to Phone > Office Hours . |
| 4 | Customize working hours and workdays to reflect the business hours of your users. Enabled : By default,  the Office Hours feature is enabled.
                If set to False, your phone won't enter power saving mode. Workdays : The default workdays are Monday through Friday.
                Change the workdays as needed. Working Hours Start and Working Hours
                  End : The default working hours are set to 7:00 to 19:00. Change the
                setting as needed. For more information about the parameters, see Parameters for Office
              Hours . |
| 5 | Configure the settings for Display Off Mode for both working hours and non-working
          hours. Cisco Desk Phone 9811 doesn't support Display Off Mode. In Office Hours > Display Off : By default, the phone
                display remains on during working hours. To enable the phone to enter Display Off
                Mode when inactive, select timeout period from the list. Outside Office Hours > Display Off Idle Timeout : Set the
                timeout period in minutes for the phone to automatically turn off the screen after
                being awakened during Display Off Mode. Outside Office Hours > LED Indicator In Display Off Mode :
                This setting determines whether to turn off the Front Arc LED when the phone enters
                Display Off Mode, both during or outside office hours. By default, the Front Arc LED
                remains illuminated after the phone enters Display Off Mode. When set to disabled,
                the Front Arc LED is off in Display Off Mode. For more information about the parameters, see Parameters for Office
              Hours . |
| 6 | Configure the settings for Deep Sleep Mode for the 9800 Series phones. Deep Sleep Mode on Cisco Video Phone 8875 and Cisco Desk Phone 9811 can only be enabled by Cisco switches through the smart power feature. To
                  configure the smart power settings, follow the steps in Allow Cisco switches to manage power modes for your phones (smart power) . A random timer is applied on top of the specified power-on and power-off times to
                  avoid sudden surges in power demand or network traffic. The phone powers off with
                  a random delay of 0 to 10 minutes after the specified power-off time, and powers
                  on 0 to 60 minutes before the specified power-on time, randomly. Contact Cisco
                  Technical Assistance Center (TAC) if you want to modify the random timer. Deep Sleep Enabled : Enable this feature to allow the phone
                to power off outside office hours. Phone Off Time After Working Hour End : Set the timeout
                period for the phone to automatically power off after the time specified in the Working Hours End field. The default setting is 60
                minutes. Phone On Time Before Working Hour Start : Set the timeout
                period for the phone to wake up from Deep Sleep Mode before the time specified in
                the Working Hours Start field. The default setting is 60
                minutes. Enable Audible Alert (Optional): If set to True, the phone
                plays audio tone to alert the user before it enters Deep Sleep Mode. Idle Timeout : Set timeout period for the phone to enter Deep
                Sleep Mode. For more information about the parameters, see Parameters for Office
              Hours . |
| 7 | Select Next . |
| 8 | Review your changes and select Apply . |
| 9 | Select Close to close the page. |

| 1 | From the customer view in Control Hub , go to Devices , and then
          select your phone. |
|---|---|
| 2 | Select All configurations . |
| 3 | Navigate to the Phone > Office Hours > Office Hours > Outside Office Hours > Smart Power . |
| 4 | Configure the following parameters: Enabled : Enable the smart power feature. The available
              options are: False (Default): Disables smart power. Non-work Day Only : Enables smart power only on
                  non-working days. All Days : Enables smart power always, on both work days
                  and non-work days. Domain : Enter the smart power domain that
              the phone belongs to. A security secret is required for the smart power domain. Contact Cisco Technical
                  Assistance Center (TAC) to add your secret. For more information about these parameters, see Parameters for Office
              Hours . |
| 5 | Select Next . |
| 6 | Review your changes and select Apply . |
| 7 | Select Close to close the page. |

| Parameter | Default and options | Supported models | Description |
|---|---|---|---|
| Office Hours |
| Enabled | Default: True Options: False, True | 8875 9841 9851 9861 9871 | Set this option to True to enable the Office Hours feature for your
                  phones. The Office Hours feature is designed to minimize power consumption during
                  inactivity periods. You can configure the phone to automatically turn off the screen (Display Off
                  Mode) or power off (Deep Sleep Mode) outside of the designated working periods. |
| In Office Hours > Display Off | Default: Disabled Options: Disabled, In 1 minute, In 5 minutes, In 30 minutes | 8875 9841 9851 9861 9871 | Enable or disable Display Off Mode during office
                  hours. This feature is disabled by default, keeping the phone screen always on
                  during office hours. To enable this feature, select a timeout duration from the
                  available options. For example, if set to "In 5 minutes", the phone screen will
                  automatically turn off after 5 minutes of inactivity. The LED indicator follows the setting found in Outside Office Hours > Display Off > LED Indicator In Display Off Mode . |
| Outside Office Hours > Deep Sleep When smart power isn't applied, the Deep Sleep settings work with
                  the office hours settings to determine the deep sleep schedule on 9841, 9851,
                  9861, and 9871. When smart power is applied, the switch also uses these
                  settings to control the deep sleep mode on all applicable phones. |
| Deep Sleep Enabled | Default: False Options: False, Non-work Day Only, All Days | 9841 9851 9861 9871 | Enable or disable Deep Sleep Mode on the phone. When enabled, this feature
                  automatically powers off the phone outside of the designated office hours. This option works only when the Office Hours is enabled. When set to False , the phone will not enter Deep Sleep
                  Mode. When set to Non-work Day Only , the phone will power off
                  exclusively on non-workdays. For the specified workdays, the phone will only turn
                  off the screen outside of the specified working hours. When set to All Days , the phone will power off during both
                  non-workdays and non-working hours on workdays. Set working hours for workdays using the Working Hour
                    Start and Working Hour End fields. |
| Phone Off Time After Working Hour End | Default: 60 Options: 0 - 360 | 8875 9811 9841 9851 9861 9871 | Set the timeout period, in minutes, for the phone to automatically power off
                  after the time specified in the Working Hours End field. If
                  you want the phone to enter Deep Sleep Mode immediately after working hours, set
                  it to 0. When the smart power feature is applied, the switch uses this
                    setting to control the phone's power mode. |
| Phone On Time Before Working Hour Start | Default: 60 Options: 0 - 360 | 8875 9811 9841 9851 9861 9871 | Set the timeout period for the phone to wake up from Deep Sleep Mode before the
                  time specified in the Working Hours Start field. If you
                  want the phone to wake up until working hours start, set it to 0. When the smart power feature is applied, the switch uses this
                    setting to control the phone's power mode. |
| Enable Audible Alert | Default: False Options: False, True | 8875 9811 9841 9851 9861 9871 | Enable or disable the phone to play audio tone to alert the user before it enters
                  Deep Sleep Mode. |
| Idle Timeout | Default: 30 Options: 1 - 60 | 8875 9811 9841 9851 9861 9871 | This setting applies to the following two scenarios: Before the phone enters a scheduled Deep Sleep Mode Ten minutes
                      before the scheduled deep sleep, a message pops up to notify the user that the
                      phone will power off in ten minutes, and a countdown starts. When it times
                      out, the phone powers off. During the countdown period, if there is a
                      system activity such as an incoming call, firmware upgrade, or provisioning
                      resync, the countdown will restart. For example, if you have set this field to
                      20, the countdown will restart in 20 minutes after the activity completes. If
                      the phone restarts or its configuration is changed during the countdown, the
                      power-off notification appears again after the restart, and the countdown
                      continues. After being awakened manually or by a configured restart during Deep Sleep
                      Mode After the specified idle timeout period, the phone displays a
                      power-off notification. The countdown shown in the notification is based on
                      the configured idle timeout value. Examples If you set the idle timeout to more than 10 minutes (for example, 20
                            minutes), a message appears after the phone has been idle for 20
                            minutes, notifying the user that the phone will power off in 10
                            minutes. If you set the idle timeout to less than 10 minutes (for example, 6
                            minutes), a message appears after the phone has been idle for 6 minutes,
                            notifying the user that the phone will power off in 6 minutes. During the countdown period, if there is a system activity such as
                      an incoming call, firmware upgrade, or provisioning resync, the countdown will
                      restart. For example, if you have set this field to 20, the countdown will
                      restart in 20 minutes after the activity completes. The following notes apply to both scenarios described above. If a user interacts with the phone during the countdown period — such as
                          by answering or declining calls, or pressing keys — the phone will remain
                          active and will not enter Deep Sleep Mode for the rest of the day. When the smart power feature is applied, the switch uses this
                    setting to control the phone's power mode. |
| Outside Office Hours > Display Off |
| Display Off Idle Timeout | Default: 5 Options: 1 - 60 | 8875 9841 9851 9861 9871 | Set the timeout period in minutes for the phone to automatically turn off the
                  screen after being awakened during Display Off Mode. |
| LED Indicator In Display Off Mode | Default: Enabled Options: Enabled, Disabled | 8875 9841 9851 9861 9871 | This field is available in the Outside Office Hours section. This setting determines whether to turn off the Front Arc LED on 9800 Series or
                  the Home button LED on 8875 when the phone enters Display Off Mode, both during or
                  outside office hours. By default (Enabled), the LED remains illuminated after the
                  phone enters Display Off Mode. When set to disabled, the LED is off in Display Off
                  Mode. |
| Outside Office Hours > Smart Power Supported only on phones powered by Power over
                  Ethernet (PoE). |
| Domain | Default: Empty | 8875 9811 9841 9851 9861 9871 | The smart power domain that the phone belongs to. Max 128 characters. A security secret is required for the smart power domain. Please contact the
                    Cisco Technical Assistance Center (TAC) to add your secret. |
| Enabled | Default: False Options: False, Non-work Day Only, All Days | 8875 9811 9841 9851 9861 9871 | Enable or disable the smart power feature. By default, smart power is disabled.
                    Set it to Non-work Day Only or All Days as needed to enable this feature. The setting is effective only when a valid domain and security secret are
                    provided. |
| Office Hours |
| Work Days | Default: Monday through Friday | 8875 9811 9841 9851 9861 9871 | Customize the workdays by selecting the desired days. During non-workdays, the phone will automatically turn off the screen. By
                  default, workdays are set from Monday to Friday. This setting also applies to Deep Sleep Mode, if enabled. If you choose to enable
                  Deep Sleep Mode exclusively for non-workdays, the phone will power off during
                  those days. If you enable Deep Sleep Mode for all days, the phone will power off
                  during non-working hours on workdays and throughout non-workdays. Set working hours for workdays using the Working Hours
                    Start and Working Hours End fields. |
| Office Hours > Working Hours |
| Working Hours End | Default: 19:00 | 8875 9811 9841 9851 9861 9871 | Set the end time for working hours using the 24-hour format. Outside of the
                  specified working hours, the phone will automatically turn off the screen, or
                  enter Deep Sleep Mode only when Deep Sleep Enabled is set
                  to All Days . Examples: 09:00 for 09:00 am; 17:30 for 05:30 pm Ensure that the interval between the start and end time longer than 60
                    minutes. |
| Working Hours Start | Default: 07:00 | 8875 9811 9841 9851 9861 9871 | Set the start time for working hours using the 24-hour format. Outside of the
                  specified working hours, the phone will automatically turn off the screen, or
                  enter Deep Sleep Mode only when Deep Sleep Enabled is set
                  to All Days . Examples: 09:00 for 09:00 am; 17:30 for 05:30 pm |

## Figuras

![For 9811, 9841,9851, and 9861](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/489001-490000/489180.png)

![for 9871](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/483001-484000/483152.png)

![For 8875](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/489001-490000/489178.png)