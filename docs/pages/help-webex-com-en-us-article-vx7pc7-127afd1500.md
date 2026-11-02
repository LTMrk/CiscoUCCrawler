---
doc_id: help-webex-com-en-us-article-vx7pc7-127afd1500
source_url: https://help.webex.com/en-us/article/vx7pc7
retrieved_at: 2026-11-02T13:10:20.820980+00:00
---

## Action button on 9800 Series

The Action button is the red button located at the top-right of the phone.
      It allows users to quickly access designated services, such as emergency or custom services.
      You can custom the button to initiate events that suit your specific use cases.

The custom options for the Action button on Cisco Desk Phone 9800 Series require specific PhoneOS firmware support. See the following table for details:

### Configure the Action button for emergency calls

The Action button for emergency calls ensures quick and easy access to critical assistance
        in workspaces.

Access the phone administration web page.

Select Voice > Phone .

Navigate to the Action Button section and configure the
          following parameters to link the Action button with an emergency service.

Action Button Function : Select Emergency
                  Call .

Action Button Service Destination : Enter the phone number or
                the URI of the emergency service.

Action Button Service Name (Optional): Specify a name for
                the service associated with the action trigger. This name will be displayed in the
                on-screen message when the user presses the button, indicating which event will be
                initiated. If no name is specified, Emergency call will be used as the
                display name.

Dial Out Delay : Set the timeout period (in seconds) for the
                phone to initiate an emergency call after the trigger is detected. The default value
                is 5 seconds. If set to 0, the call is placed immediately upon detecting the
                trigger.

Service Trigger Select a trigger
                from the list: Single Press , Long
                  Press , or Press 3 Times .

Silent Emergency Call (Optional): By default, the emergency
                call functions as a two-way call, similar to other outgoing calls. When silent
                emergency call is enabled, the audio is silent on the caller side to avoid drawing
                attention during the onging call. Only the call recipient can end the silent
                emergency call.

During a silent emergency call, the screen on phone 9811 and 9841 will freeze,
                while the screen on phone 9851, 9861, and 9871 will be turned off. All other
                functions are inaccessible. The phone restores normal operation after the recipient
                ends the call.

Allow Silent
                  Emergency Call Retrieval (Optional): Enable this feature if you allow
                users to press any key to restore normal phone operation while maintaining the
                emergency call. The call audio remains silent unless the user increases the speaker
                volume using the Volume key.

For more details about these parameters, see Parameters for the Action
              button .

You can also configure these parameters in the phone configuration XML file (cfg.xml)
            by entering the following
            strings:

When done, click Submit All Changes .

### Associate the Action button with a custom service

When you associate the Action button with a custom service, the
        phone users can access the service by the designated trigger, such as a single press, long
        press, or triple presses on the button.

Access the phone administration web page.

Select Voice > Phone .

Navigate to the Action Button section and configure the following parameters to associate the Action button with a service.

Action Button Function : Select Custom .

Action Button Service Name (Optional): Specify a name for the service associated with the trigger. This name
                will be displayed in the on-screen message when the user presses the button,
                indicating which service will be triggered. When no name is specified, Custom
                  service will be used as the display name.

Action Button Service Destination :
                Enter the URL of the custom service. The URL must start with http:// or https:// , for example, https://10.11.20.159/path/service.xml .

Custom Content Field (Optional): If
                you want to enable the phone to send an HTTP Post request when the Action button is
                pressed, enter the HTTP data such as method, header, and post content, with a
                maximum length of 1024 characters.

For POST script examples and the syntax, see HTTP Post request for the
                  Action button .

Dial Out Delay : Set the timeout
                period, in seconds, for the phone to initiate an event after detecting the trigger.
                The default value is 5 seconds. When set to 0, the event is initiated immediately
                upon trigger detection.

Service Secret (Optional): Enter
                the authentication secret, token or password if your custom service requires
                authentication to access it. The entered secret is displayed as a masked string and
                can be referenced using the macro $SS in Custom Content
                  Field and Action Button Service
                Destination .

Service Trigger Select a trigger
                from the list: Single Press , Long
                  Press , or Press 3 Times .

Silent Emergency Call (Optional): If you have included a
                  phone number or dialing URI in the service destination, enabling this feature will
                  silent emergency calls.

By default, the emergency call functions as a two-way call, similar to other
                  outgoing calls. When set to enabled, the audio is silent on the caller side to
                  avoid drawing attention during the onging call. Only the call recipient can end
                  the call.

During a silent emergency call, the screen on phone 9811 and 9841 will freeze,
                  while the screen on phone 9851, 9861, and 9871 will be turned off. All other
                  functions are inaccessible. The phone restores normal operation after the
                  recipient ends the call.

For more details about these parameters, see Parameters for the Action
              button .

You can also configure these parameters in the phone configuration XML file (cfg.xml)
            by entering the following
            strings:

When done, click Submit All Changes .

### Configure a single trigger for multiple events

A single trigger for multiple events allows one action on the action button to initiate
        several related processes simultaneously. This feature enhances responsiveness, reduces
        complexity, and ensures seamless workflow execution across applications.

Access the phone administration web page.

Select Voice > Phone .

Navigate to the Action Button section and configure the
          following parameters to associate the Action button with a service.

Action Button Function : Select Custom .

Action Button Service Destination : Enter the phone number
                  to call and the XML service URL in this format:

tel:<phonenumber or SIP URI> +
                  <serviceURL>

The URL must start with http:// or https:// .

Example: tel:1234 + https://10.11.20.159/path/service.xml

Action Button Service
                  Name (Optional): Specify a name for the service associated with the
                action trigger. This name will be displayed in the on-screen message when the user
                presses the button, indicating which service will be triggered. When no name is
                specified, Custom
                  service will be used as the display name.

Custom Content Field (Optional): If you want to enable the
                phone to send an HTTP Post request when the Action button is pressed, enter the HTTP
                data such as method, header, and post content, with a maximum length of 1024
                characters.

For POST script examples and the syntax, see HTTP Post request for the
                  Action button .

Dial Out Delay : Set the timeout
                period, in seconds, for the phone to initiate an event after detecting the trigger.
                The default value is 5 seconds. When set to 0, the event is initiated immediately
                upon trigger detection.

Service Secret (Optional): Enter
                the authentication secret, token or password if your custom service requires
                authentication to access it. The entered secret is displayed as a masked string and
                can be referenced using the macro $SS in Custom Content
                  Field and Action Button Service
                Destination .

Silent Emergency Call (Optional): If you have included a
                  phone number or dialing URI in the service destination, enabling this feature will
                  silent emergency calls.

By default, the emergency call functions as a two-way call, similar to other
                  outgoing calls. When set to enabled, the audio is silent on the caller side to
                  avoid drawing attention during the onging call. Only the call recipient can end
                  the call.

During a silent emergency call, the screen on phone 9811 and 9841 will freeze,
                  while the screen on phone 9851, 9861, and 9871 will be turned off. All other
                  functions are inaccessible. The phone restores normal operation after the
                  recipient ends the call.

Allow Silent
                  Emergency Call Retrieval (Optional): Enable this feature if you allow
                users to press any key to restore normal phone operation while maintaining the
                emergency call. The call audio remains silent unless the user increases the speaker
                volume using the Volume key.

For more details about these parameters, see Parameters for the Action
              button .

You can also configure these parameters in the phone configuration XML file (cfg.xml)
            by entering the following
            strings:

When done, click Submit All Changes .

### Configure multiple triggers

You can configure the Action button to connect to multiple services and assign each service
        with its own trigger. For example, a long press on the Action button places a call to the
        designated emergency agent; a single short press on the button post a notification to the
        phones within the corporation.

Access the phone administration web page.

Select Voice > Phone .

Navigate to the Action Button section and select MultiTrigger in the Service Trigger field.

Based on your use cases, configure the parameters in the desired trigger
          sections.

Action Button Function : Select the service that phone users
                can access via the trigger.

Action Button Service Name (Optional): Specify a name for the service associated with the trigger. This name
                will be displayed in the on-screen message when the user presses the button,
                indicating which service will be triggered. When no name is specified, Custom
                  service will be used as the display name.

Action Button Service Destination :
                Enter the URL of the custom service. The URL must start with http:// or https:// , for example, https://10.11.20.159/path/service.xml .

Custom Content Field (Optional): If
                you want to enable the phone to send an HTTP Post request when the Action button is
                pressed, enter the HTTP data such as method, header, and post content, with a
                maximum length of 1024 characters.

For POST script examples and the syntax, see HTTP Post request for the
                  Action button .

Service Secret (Optional): Enter
                the authentication secret, token or password if your custom service requires
                authentication to access it. The entered secret is displayed as a masked string and
                can be referenced using the macro $SS in Custom Content
                  Field and Action Button Service
                Destination .

Dial Out Delay : Set the timeout
                period, in seconds, for the phone to initiate an event after detecting the trigger.
                The default value is 5 seconds. When set to 0, the event is initiated immediately
                upon trigger detection.

Silent Emergency Call (Optional): If you have set the
                  Action button for emergency calls, enabling this feature will silent emergency
                  calls.

By default, the emergency call functions as a two-way call, similar to other
                  outgoing calls. When set to enabled, the audio is silent on the caller side to
                  avoid drawing attention during the onging call. Only the call recipient can end
                  the call.

During a silent emergency call, the screen on phone 9811 and 9841 will freeze, while the screen on
                  phone 9851, 9861, and 9871 will be turned off. All other functions are
                  inaccessible. The phone restores normal operation after the recipient ends the
                  call.

Allow Silent
                  Emergency Call Retrieval (Optional): Enable this feature if you allow
                users to press any key to restore normal phone operation while maintaining the
                emergency call. The call audio remains silent unless the user increases the speaker
                volume using the Volume key.

This parameter is located in the Action Button section.

For more details about these parameters, see Parameters for the Action
              button .

You can also configure these parameters in the phone configuration XML file (cfg.xml)
            by entering the following
            strings:

When done, click Submit All Changes .

### References

#### Parameters for the Action button

The following parameters are located in the Action Button section in
        the Voice > Phone tab.

Default: Off

Options: Off, Emergency Call, Custom

You can configure the button with a specific service.

- Off : When set to Off, the Action button for single
                      service on the phone will not function.

- Emergency Call : Users can use the Action button to
                      place an emergency call, if configured.

- Custom : Users can use the Action button to access the
                      custom service, if configured.

When you set the field to Emergency Call or Custom , make sure that you enter the service
                    destination in the Action Button Service Destination field. Or, the phone will display a configuration error.

Default: Empty

Optionally specify a name for the service associated with the Action button.
                    This name will be displayed in the on-screen message when the user presses the
                    button, indicating which service will be triggered.

If you don't specify a name, the default name will be Emergency call, Silent
                    emergency call, or Custom action based on your selection in the Action Button Function field.

Default: Empty

Provide the service destination in one of the following formats based on the
                    service assigned to the Action button:

For emergency call services, enter a telephone number or the URI of
                        emergency service.

When configure the button for a custom service, enter the service URL. The
                        URL must start with http:// or https:// . For example, https://10.11.20.159/path/service.xml .

To configure the button to initiate multiple events with a single trigger,
                        enter tel:<phonenumber or SIP URL> + <Service
                          RUL> . Example : tel:1234 +
                          https://10.11.20.159/path/service.xml .

Calling SIP URIs is also supported. Enter the URI in the format of tel: sip 4567@co.webex.com

If you enable the Action button without setting a valid service destination,
                    the user on the phone will see a message prompting for configuration. After the
                    user closes this notification, the warning icon will persist in the header of
                    the phone screen until the button is properly configured or disabled.

Phone numbers cannot be used as destinations for custom services. If you
                      configure the Action Button as Custom and enter a phone
                      number as the service destination, an alert message will display on the phone
                      indicating that the button is unconfigured. Instead, you can add a phone
                      number in this format tel:<phone number> , for
                      example, tel:1234 .

Default: Empty

This setting works only when the Action Button
                        Function is set to Custom .

Enter the HTTP data such as method, header, and post content, with a maximum
                    length of 1024 characters. When configured, the phone sends an HTTP Post request
                    when the Action is pressed.

You can also use other macros such as $MA, $SN.

For POST script examples and the syntax, see HTTP Post request for the Action button .

Default: Empty

A service secret can be an authentication secret, token or password. The
                    entered secret is displayed as a masked string and can be referenced using the
                    macro $SS in Custom Content Field and Action Button Service Destination .

Default: Single Press

Options: Single Press, Long Press, Press 3 times,
                  MultiTrigger

Choose how users can place an emergency call or initiate a custom service using
                    the phone's Action button.

Single Press : Press the Action button to trigger the
                    associated call or service.

Long Press : Press the Action button down for at least 2
                    seconds to trigger the associated call or service.

Press 3 times : Press the Action button three times with
                    intervals of one second between each press to trigger the associated call or
                    service.

MultiTrigger :
                    Select this option to associate multiple triggers and events to the Action
                    button. Then, go to the MultiTrigger - Single Press , MultiTrigger - Long Press , and MultiTrigger
                      - Press Three Times sections to configure the specific
                    settings.

Default: 5

Options: 0 - 30

Set the timeout period, in seconds, for the phone to initiate an emergency call
                    or a custom action after the Action button is pressed.

Set it to 0 if you prefer the phone to place the call or initiate an event
                    immediately upon detecting the trigger, as specified by a single press, long
                    press, or triple presses on the button.

Default: Disabled

Options: Enabled, Disabled

Silent emergency call is designed for discreet assistance in dangerous
                    situations. It enables users to seek help without making any noise.

When enabled, users are able to place one-way calls with the Action button.

After the silent emergency call is placed, only the other party can end the
                        call. To avoid drawing attention during the ongoing call, the screen on
                        phone 9811 and 9841 will freeze, while
                        the screen on phone 9851, 9861, and 9871 will be turned off. The phone locks all
                          functions during a silent emergency call, by default. To allow users to
                          restore normal phone operation while maintaining the silent emergency
                          call, enable the Allow Silent Emergency Call
                            Retrieval feature.

When disabled, the emergency call functions as a two-way call, similar to
                        other outgoing calls.

Default: No

Options: Yes, No

Controls whether users can retrieve phone functionality during a silent
                    emergency call. By default, once a silent emergency call is initiated, the phone
                    locks all functions until the call recipient ends the call.

When this parameter is set to Yes , users can press any
                    key to restore normal phone operation while maintaining the emergency call. The
                    call audio remains silent unless the user increases the volume using the Volume
                    key.

The parameters in the following table are available in the MultiTrigger - Single
          Press , MultiTrigger - Long Press , and MultiTrigger - Press Three Times sections on the Voice > Phone tab.

Default: Off

Options: Off, Emergency Call, Custom

Select the service that phone users can access via the service trigger.

- Off : When set to Off, the action trigger will not
                      function.

- Emergency Call : Users can place a call to the
                      designated emergency number via the action trigger.

When you set the field to Emergency Call or Custom , make sure that you enter the proper service
                        destination in the Action Button Service Destination field. Or, the phone will display a configuration error.

Default: Empty

Optionally specify a name for the service associated with the action trigger.
                    This name will be displayed in the on-screen message when the user presses the
                    button, indicating which service will be triggered.

If you don't specify a name, the default name will be Emergency call, Silent
                    emergency call, or Custom action based on your selection in the Action Button Function field.

Default: Empty

Provide the phone number, the URI for emergency call, or the URL for the custom
                    service.

If you enter a service URL, the URL must start with http:// or https:// .

Example: https://10.11.20.159/path/service.xml .

Phone numbers cannot be used as destinations for custom services. If you
                      configure the Action Button as Custom and enter a phone
                      number as the service destination, an alert message will display on the phone
                      indicating that the button is unconfigured. Instead, you can add a phone
                      number in this format tel:<phone number> , for
                      example, tel:1234 .

Default: Empty

This setting works only when the Action Button
                        Function is set to Custom .

Enter the HTTP data such as method, header, and post content, with a maximum
                    length of 1024 characters. When configured, the phone sends an HTTP Post request
                    when the Action is pressed.

You can use macros in the HTTP data, such as $MA, $SN.

For POST script examples and the syntax, see HTTP Post requests for
                    the Action button .

Default: Empty

A service secret can be an authentication secret, token or password. The
                    entered secret is displayed as a masked string and can be referenced using the
                    macro $SS in Custom Content Field and Action Button Service Destination .

Default: 5

Options: 0 - 30

Set the timeout period, in seconds, for the phone to initiate an emergency call
                    or a custom action after the Action button is pressed.

Set it to 0 if you prefer the phone to place the call or initiate an event
                    immediately upon detecting the trigger, as specified by a single press, long
                    press, or triple presses on the button.

Default: Disabled

Options: Enabled, Disabled

Silent emergency call is designed for discreet assistance in dangerous
                    situations. It enables users to seek help without making any noise.

When enabled, users are able to place one-way calls with the Action button.

After the silent emergency call is placed, only the other party can end the
                        call. To avoid drawing attention during the ongoing call, the screen on
                        phone 9811 and 9841 will freeze, while
                        the screen on phone 9851, 9861, and 9871 will be turned off. The phone locks all
                          functions during a silent emergency call, by default. To allow users to
                          restore normal phone operation while maintaining the silent emergency
                          call, enable the Allow Silent Emergency Call
                            Retrieval feature.

When disabled, the emergency call functions as a two-way call, similar to
                        other outgoing calls.

#### HTTP Post request for the Action button

The Action button on Cisco Desk Phone 9800 Series can be configured to trigger XML applications through HTTP Post requests.

In Custom Content Field , enter the request script. You can specify
        either XML or JSON content type and include macros in the request. For example, $SS can be added to the script to retrieve the authentication secret,
        token, or password provided in the Service Secret field.

The following examples are in XML and JSON:

```
Sample #1: XML
--method POST
--header 'Content-Type: application/xml'
--header 'Authorization: Bearer username:$SS'
--body '<MetaData><Trigger>True</Trigger><Description>This is for HTTP POST XML</Description></MetaData>' 

Sample #2: JSON
--method POST
--header 'Content-Type: application/json'
--header 'Authorization: $SS'
--body '{"events":[{"evtid":"12345", "parameters": {"trigger":true}, "Description":"This is for HTTP POST JSON"}]}'
```

The following example is for an HTTP Post request.

```
--method POST
--header 'Content-Type: application/xml'
--body '<MetaData><Trigger>True</Trigger><Description>This is for HTTP POST XML</Description></MetaData>'
```

$PN

$PSN

## Office Hours

The Office Hours feature lets phones automatically power on, power off, or turn off the
        display based on a set schedule, helping organizations save energy, reduce costs, and
        optimize device performance. The information in this section applies to Cisco Desk Phone 9800 Series and Cisco Video Phone 8875 registered with Cisco BroadWorks.

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

Display Off

Deep Sleep

(Controlled by phone)

Cisco Smart Power

(Deep Sleep controlled by switch)

### Enable your phone to manage its own power modes

By default, the Office Hours feature is enabled on your phone. The
        default office hours are set to 7:00 to 19:00 from Monday to Friday. The phone turns off the
        screen outside of the designated hours. You can customize working hours, workdays, and the
        power-saving modes — Display Off and Deep Sleep.

Access the phone administration web page.

Select Voice > Phone .

Customize working hours and workdays to reflect the business hours of your users.

Cisco Desk Phone 9811 doesn't support Display Off Mode.

Office Hours Enabled : By default, the Office Hours feature
                is enabled. If disabled, your phone won't enter power saving mode.

Workdays : The default workdays are Monday through Friday.
                Change the workdays as needed.

Working Hours Start and Working Hours
                  End : The default working hours are set to 7:00 to 19:00. Change the
                setting as needed.

Display Off In Office Hours : By default, the phone display
                remains on during working hours. To enable the phone to enter Display Off Mode when
                inactive, select timeout period from the list.

For more information about these parameters, see Parameters for Office Hours .

Configure the settings for Deep Sleep Mode for the 9800 Series phones.

Deep Sleep Mode on Cisco Video Phone 8875 and Cisco Desk Phone 9811 can only be enabled by Cisco switches through the smart power feature. To configure
              the smart power settings, follow the steps in Allow Cisco switches to manage power modes for your phone (smart power) .

Deep Sleep Enabled : Enable this feature to allow the phone
                to power off outside office hours.

Enable Audible Alert (Optional): If set to True, the phone
                plays audio tone to alert the user before it enters Deep Sleep Mode.

Phone Off Time After Working Hour End : Set the timeout
                period for the phone to automatically power off after the time specified in the Working Hours End field. The default setting is 60
                minutes.

Phone On Time Before Working Hour Start : Set the timeout
                period for the phone to wake up from Deep Sleep Mode before the time specified in
                the Working Hours Start field. The default setting is 60
                minutes.

Random Early Wakeup : Set the time interval for the phone to
                wake up before its regular schedule. It helps distribute the load of connection and
                registration requests when a large number of phones power on simultaneously.

Random Delay to Sleep : Set a time interval for the phone to
                enter Deep Sleep Mode after its scheduled power-off time.

Idle Timeout : Sets timeout period for the phone to enter
                Deep Sleep Mode.

For more information about these parameters, see Parameters for Office Hours .

Configure the settings for Display Off Mode outside office hours.

Handset LED in Display Off Mode (Video Phone 8875): Controls whether the handset LED lights up to notify users of phone statuses in Display Off mode. When disabled, the handset LED is off. When enabled, its indication behavior is the same as when the display is on. This setting works only when the LED Indicator In Display Off Mode parameter is set to Enabled.

Line Key and Top 360 LED in Display Off Mode (Cisco Desk Phone 9841, 9851, 9861, and 9871): Controls whether the LEDs light up to notify users of phone statuses in Display Off mode. When disabled, both the Line Key LEDs on phone and Key Expansion Module (KEM) and Top 360 LEDs are off. When the corresponding LED is enabled, its indication behavior is the same as when the display is on. This setting works only when the LED Indicator In Display Off Mode parameter is set to Enabled.

LED Indicator In Display Off Mode : This setting determines
                whether to turn off the Front Arc LED when the phone enters Display Off Mode, both
                during or outside office hours. By default, the Front Arc LED remains illuminated
                after the phone enters Display Off Mode. When set to disabled, the Front Arc LED is
                off in Display Off Mode.

Idle Timeout : Set the timeout period in minutes for the
                phone to automatically turn off the screen after being awakened during Display Off
                Mode.

For more information about these parameters, see Parameters for Office Hours .

When done, click Submit All Changes .

### Allow Cisco switches to manage power modes for your phone (smart power)

The smart power feature allows Cisco Smart Switches to manage the phone's power modes via
          Power over Ethernet (PoE).

You can choose to let the switch manage the phone's power modes based on the schedules
          configured on the switch. The following table shows how the smart power settings interact
          with the phone's own Deep Sleep and Display Off settings configured in the phone's calling
          system.

Smart power is disabled. The phone follows the power saving configuration set on
                  its calling system.

Smart power is enabled only on non-work days.

On non-work days, the phone follows the display off and deep sleep schedules
                  configured on its calling system.

The switch wakes the phone from deep sleep following the phone's schedule.

Smart power is always enabled.

Smart power is always enabled.

The phone follows the display off and deep sleep schedules set on its calling
                  system.

The switch wakes the phone from deep sleep following the phone's schedule.

Smart power is always enabled.

Before you begin

Your phone uses Power over Ethernet (PoE) as the power source. If a power cube is
            connected, the smart power feature is automatically disabled.

Your phone is connected to a Cisco Smart Switch C9350 with IOS XE 17.18.2 or later.

- To use the Smart Power feature, you must first enable the Office Hours
            feature on your phone .

Access the phone administration web page.

Select Voice > Phone .

Go to the Outside Office Hours Smart Power section, and
          configure the following parameters:

Smart Power Enabled : Enable the smart power feature. The
                available options are:

- False (Default): Disables smart power.

- Non-work Day Only : Enables smart power only on
                  non-working days.

- All Days : Enables smart power always, on both work days
                  and non-work days.

- Domain : Enter the smart power domain that the phone belongs
              to.

- Secret : Enter the password (shared secret) used for
              communication between the phone and the switch.

- Smart Power Override : Specify whether the
              switch can manage power modes based on the schedules configured on the switch,
              overriding the phone's configurations in the calling system.

You can also use the configuration XML file (cfg.xml) to customize the Settings menu. See the
            following
            example:

When done, click Submit All Changes .

### Parameters for Office Hours

The Office Hours parameters are available on the Voice > Phone tab on the phone administration web page.

Default: True

Options: False, True

8875

9841

9851

9861

9871

Set this field to True to enable the Office Hours
                  feature for Cisco Desk Phone 9800 Series.

The Office Hours feature is
                  designed to minimize power usage during inactivity periods on the phone. You can
                  configure the phone to automatically turn off the screen (Display Off Mode) or
                  power off (Deep Sleep Mode) outside of the designated working periods.

You
                  can configure this parameter in the phone configuration XML file (cfg.xml) by
                  entering a string in this format:

Default: Monday through Friday

8875

9811

9841

9851

9861

9871

Customize the workdays by specifying the desired days.

During
                  non-workdays, the phone will automatically turn off the screen. By default,
                  workdays are set from Monday to Friday.

This setting also applies to Deep
                  Sleep Mode, if enabled. If you choose to enable Deep Sleep Mode exclusively for
                  non-workdays, the phone will power off during those days. If you enable Deep Sleep
                  Mode for all days, the phone will power off during both non-workdays and
                  non-working hours on workdays.

Set working hours for workdays using the Working Hours Start and Working Hours
                    End fields.

You can configure this parameter in the phone
                  configuration XML file (cfg.xml) by entering a string in this
                  format:

Default: 07:00

8875

9811

9841

9851

9861

9871

Set the start time for working hours using the 24-hour format. Outside of
                  the specified working hours, the phone will automatically turn off the screen, or
                  enter Deep Sleep Mode only when Deep Sleep Enabled is set
                  to All Days .

Examples: 09:00 for 09:00 am; 17:30 for
                  05:30 pm

You can configure this parameter in the phone configuration XML
                  file (cfg.xml) by entering a string in this
                  format:

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

Examples: 09:00 for 09:00 am; 17:30 for
                  05:30 pm

Ensure that the interval between the start
                  and end time longer than 60 minutes.

You can configure this parameter in
                  the phone configuration XML file (cfg.xml) by entering a string in this
                  format:

Default: Disabled

Options: Disabled, In 1 minute, In 5 minutes, In 30 minutes

8875

9841

9851

9861

9871

The LED indicator follows the setting found in Outside Office Hours Display Off > LED Indicator In Display Off Mode .

You can configure this parameter in the phone configuration
                  XML file (cfg.xml) by entering a string in this
                  format:

When smart power isn't applied, the Deep Sleep settings work with the office
                    hours settings to determine the deep sleep schedule on 9841, 9851, 9861, and
                    9871.

When smart power is applied and Smart Power Override is disabled, the switch
                    also uses these settings to control the deep sleep mode on all applicable
                    phones.

Default: False

Options: False, Non-work Day Only, All Days

9841

9851

9861

9871

Enable or disable Deep Sleep Mode on the phone. When enabled, this feature
                  automatically powers off the phone outside of the designated office hours.

This option works only when the Office Hours is enabled.

When set to False , the phone will not enter Deep
                  Sleep Mode.

When set to Non-work Day Only , the phone
                  will power off exclusively on non-workdays. For the specified workdays, the phone
                  will turn off the screen outside of the specified working hours.

When set to All Days , the phone will power off during both
                  non-workdays and non-working hours on workdays.

Set working hours for
                  workdays using the Working Hours Start and Working Hours End fields.

You can configure this
                  parameter in the phone configuration XML file (cfg.xml) by entering a string in
                  this format:

Default: False

Options: False, True

8875

9811

9841

9851

9861

9871

Enable or disable the phone to play audio tone to alert the user before it
                  enters Deep Sleep Mode.

You can configure this parameter in the phone
                  configuration XML file (cfg.xml) by entering a string in this
                  format:

The smart power feature uses this setting to control the
                    phone's power mode only when Smart Power Override is
                    disabled.

Default: 60

Options: 0 - 360

8875

9811

9841

9851

9861

9871

Set the timeout period for the phone to wake up from Deep Sleep Mode before
                  the time specified in the Working Hours Start field. If you
                  want the phone to wake up until working hours start, set it to 0.

You can
                  configure this parameter in the phone configuration XML file (cfg.xml) by entering
                  a string in this
                  format:

The smart power feature uses this setting to control the
                    phone's power mode only when Smart Power Override is
                    disabled.

Default: 60

Options: 0 - 360

8875

9811

9841

9851

9861

9871

Set the timeout period for the phone to automatically power off after the
                  time specified in the Working Hours End field. If you want
                  the phone to enter Deep Sleep Mode immediately after working hours, set it to
                  0.

You can configure this parameter in the phone configuration XML file
                  (cfg.xml) by entering a string in this
                  format:

The smart power feature uses this setting to control the
                    phone's power mode only when Smart Power Override is
                    disabled.

Default: 60

Options: 0 - 60

8875

9811

9841

9851

9861

9871

Set the time interval for the phone to wake up before its regular schedule.
                  It helps distribute the load of connection and registration requests when a large
                  number of phones power on simultaneously.

The actual wakeup time is
                  calculated as: Working Hours Start - Phone On Time Before Working Hour Start -
                  Random Early Wakeup

Example

If the following values are set
                  as:

- Working Hours Start: 8:00 am

- Phone On Time Before Working Hour Start: 30 mins

- Random Early Wakeup: 60 mins

the phone can randomly wake from Deep Sleep Mode at anytime between 6:30 am
                  7:30 am.

You can configure this parameter in the phone configuration XML
                  file (cfg.xml) by entering a string in this
                  format:

The smart power feature uses this setting to control the
                    phone's power mode only when Smart Power Override is
                    disabled.

Default: 10

Options: 0 - 10

8875

9811

9841

9851

9861

9871

Set a time interval for the phone to enter Deep Sleep Mode after its
                  scheduled power-off time.

The actual sleep time is calculated as: Working
                  Hours End + Phone Off Time After Working Hour End + Random Delay to
                    Sleep

Example

If the following values are set:

- Working Hours End: 5:00 pm

- Phone Off Time After Working Hour End: 30 mins

- Random Delay to Sleep: 10 mins

the phone can randomly power off at anytime between 5:30 pm and 5:40
                  pm.

You can configure this parameter in the phone configuration XML file
                  (cfg.xml) by entering a string in this
                  format:

The smart power feature uses this setting to control the
                    phone's power mode only when Smart Power Override is
                    disabled.

(for Deep Sleep Mode)

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

If a user interacts with the phone during the countdown period, such as
                          answering or declining calls or pressing keys, the phone will not enter
                          Deep Sleep Mode for the rest of the day.

The smart power feature uses this setting to control the
                    phone's power mode only when Smart Power Override is
                    disabled.

You can configure this parameter in the phone configuration XML file
                  (cfg.xml) by entering a string in this format:

Default: Disabled

Options: Enabled, Disabled

8875

Controls whether the handset LED lights up to notify users of phone statuses in Display Off mode. When disabled, the handset LED is off. When enabled, its indication behavior is the same as when the display is on.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

This setting works only when the LED Indicator In Display Off Mode parameter is set to Enabled.

Default: Disabled

Options: Disabled, Enable Line Key LED, Enable Top 360 LED, Enable both Line Key and Top 360 LED

9841

9851

9861

9871

Controls whether the LEDs light up to notify users of phone statuses in Display Off mode. When disabled, both the Line Key LEDs on phone and Key Expansion Module (KEM) and Top 360 LEDs are off. When the corresponding LED is enabled, its indication behavior is the same as when the display is on.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

This setting works only when the LED Indicator In Display Off Mode parameter is set to Enabled.

Default: Enabled

Options: Enabled, Disabled

8875

9811

9841

9851

9861

9871

This setting determines whether to turn off the Front Arc LED on 9800 Series
                  or the Home button LED on 8875 when the phone enters Display Off Mode, both during
                  or outside office hours. By default (Enabled), the LED remains illuminated after
                  the phone enters Display Off Mode. When set to disabled, the LED is off in Display
                  Off Mode.

You can configure this parameter in the phone configuration XML
                  file (cfg.xml) by entering a string in this
                  format:

(for Display Off Mode outside
                  office hours)

Default: 5

Options: 1 - 60

9811

9841

9851

9861

9871

This field is available in the Outside Office Hours Display
                    Off section.

Set the timeout period in minutes for the phone
                  to automatically turn off the screen after being awakened during Display Off
                  Mode.

You can configure this parameter in the phone configuration XML file
                  (cfg.xml) by entering a string in this
                  format:

Supported only on phones powered by Power over
                  Ethernet (PoE).

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

You can configure this parameter in the phone configuration XML file
                  (cfg.xml) by entering a string in this format:

8875

9811

9841

9851

9861

9871

The smart power domain that the phone belongs to. Max 128 characters.

You can configure this parameter in the phone configuration XML file
                  (cfg.xml) by entering a string in this format:

8875

9811

9841

9851

9861

9871

The password (shared secret) used for communication between the phone and the
                    switch. Max 128 characters.

You can configure this parameter in the phone configuration XML file
                  (cfg.xml) by entering a string in this format:

Default: No

Options: Yes, No

8875

9811

9841

9851

9861

9871

This setting determines whether the switch can override the phone's
                    power-saving configuration set by the calling system.

- No : The phone follows the power-saving configuration
                      set by its calling system.

- Yes : The switch fully controls the phone’s power
                      modes, overriding the configuration set by the phone's calling system.

You can configure this parameter in the phone configuration XML file
                  (cfg.xml) by entering a string in this format:

## Enable hoteling on a phone

When you enable the hoteling feature of BroadSoft on the phone, the user can sign in to the
        phone as a guest. After the guest sign out of the phone, the user will switch back to the
        host user.

You can also enable hoteling service from the server. For more information, see Cisco BroadWorks Partner Configuration Guide .

When you enable hoteling:

A phone with multiple lines displays Hoteling softkey on the phone home screen for each line that
            has hoteling enabled.

A phone with multiple lines displays Guest
              in softkey on the phone home screen for each line that has hoteling
            enabled. You see this line when you press More ( … ) next to the line.

- A phone with single line displays Guest in softkey on the phone
          home screen.

Before you begin

On the server:

- Enable hoteling service for the host user and the guest user. For more information, see Cisco BroadWorks Partner Configuration Guide .

- Set the Guest in password.

Access the phone administration web page.

Select Voice > Ext [n] (where [n] is the extension number).

In the Call Feature Settings section, set Enable
            Broadsoft Hoteling parameter to Yes .

You can configure this parameter in the phone configuration XML file (cfg.xml) by
            entering a string in this format:

```
<Enable_Broadsoft_Hoteling_1_ua="na">Yes</Enable_Broadsoft_Hoteling_1>
```

Options: Yes and No

Default: No

Set the amount of time (in seconds) in Hoteling Subscription
            Expires paramter that specifies how often the phone sends the SUBSCRIBE
          message.

You can configure this parameter in the phone configuration XML file (cfg.xml) by
            entering a string in this format:

```
<Hoteling_Subscription_Expires_1_ua="na">3600</Hoteling_Subscription_Expires_1>
```

Valid values: An integer from 10 through 86400

Default: 3600

When the parameter is set to 0, the default 3600 is used.

Click Submit All Changes .

## Phone settings sync

### DND and call forward status sync

You can configure the settings on the phone administration web page to enable status synchronization of Do Not Disturb (DND) and call forward between the phone and the server.

There are two ways to synchronize the feature status:

Feature Key Synchronization (FKS)

XSI Synchronization

FKS uses SIP messages to communicate the feature status. XSI Synchronization uses HTTP messages. If both FKS and XSI synchronization are enabled, FKS takes precedent over XSI synchronization. See the table below for how FKS interacts with XSI synchronization.

Feature Key Sync

XSI DND Enabled

XSI CFWD Enabled

DND Sync

CFWD Sync

Yes

Yes

Yes

Yes (SIP)

Yes (SIP)

Yes

No

No

Yes (SIP)

Yes (SIP)

Yes

No

Yes

Yes (SIP)

Yes (SIP)

No

Yes

Yes

Yes (HTTP)

Yes (HTTP)

No

No

Yes

No

Yes (HTTP)

No

Yes

No

Yes (HTTP)

No

No

No

No

No

No

#### Enable DND and Call Forward status sync with Feature Key Sync (FKS)

When you enable the Feature Key Synchronization (FKS), the settings of call forward and do not disturb (DND) on the server are synchronized to the phone. The changes in DND and call forward settings made on the phone will also be synchronized to the server.

When FKS is enabled on a line,  the line get the DND and Call Forward settings from the server and doesn't sync with the settings on Voice > User tab.

Access the phone administration web page.

Select Voice > Ext [n] (where [n] is the extension number).

In the Call Feature Settings section, set the Feature Key Sync field to Yes .

Click Submit All Changes .

#### Enable call forward status sync via XSI service

When call forward sync is enabled, the settings related to call forward on the server are synchronized to the phone. The changes in call forward settings made on the phone will also be synchronized to the server.

Before you begin

Configure the XSI host server and the corresponding credentials on the Voice > Ext (n) tab.

When using Login Credentials for XSI server authentication, enter XSI Host Server , Login User ID , and Login Password in the XSI Line Service section.

When using SIP Credentials for XSI server authentication, enter XSI Host Server and Login User ID in the XSI Line Service section, and Auth ID and Password in the Subscriber Information section.

Disable Feature Key Sync (FKS) in Call Feature Settings section from Voice > Ext (n) .

Access the phone administration web page.

Select Voice > Ext [n] (where [n] is the extension number).

In the XSI Line Service section, set the CFWD Enable parameter to Yes .

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<CFWD_Enable_1_ ua="na">Yes</CFWD_Enable_1_>
```

Options: Yes and No

Default: No

Click Submit All Changes .

#### Enable DND status sync via XSI service

When do not disturb (DND) sync is enabled, the DND setting on the server is synchronized to the phone. The changes in DND setting made on the phone will also be synchronized to the server.

Before you begin

Configure the XSI host server and the corresponding credentials on the Voice > Ext (n) tab.

When using Login Credentials for XSI server authentication, enter XSI Host Server , Login User ID , and Login Password in the XSI Line Service section.

When using SIP Credentials for XSI server authentication, enter XSI Host Server and Login User ID in the XSI Line Service section, and Auth ID and Password in the Subscriber Information section.

Disable Feature Key Synchronization (FKS) in Call Feature Settings section from Voice > Ext (n) .

Select Voice > Ext [n] (where [n] is the extension number).

In the XSI Line Service section, set the DND Enable parameter to Yes .

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<DND_Enable_1_ ua="na">Yes</DND_Enable_1_>
```

Options: Yes and No

Default: No

Click Submit All Changes .

## Configure conference settings for phones

The following sections provide information on how to configure the conference service for your phones.

### Enable conference service

Enable the conference service for your phones so that users can initiate or join multiple-way calls using their phone lines.

Access the phone administration web page.

To enable conference service for the phone do the following:

Select Voice > Phone .

Under Supplementary Services , choose Yes for the Conference Serv parameter.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<Conference_Serv ua="na">Yes</Conference_Serv>
```

Options: Yes and No

Default: Yes

Specify the conference bridge URL for your desired line:

Select Voice > Ext(n)

Enter the Conference Bridge URL in this format:

```
user@IPaddress:port
```

Click Submit All Changes .

## Enable Webex calendar service

If you want to enable the phone to have the ability to join Webex calendar meetings, do the following:

Before you begin

Your phone has been registered to Webex Calling.

Access the phone administration web page.

Select Voice > Phone .

In the Webex section, set the field Calendar Enable .

Set Yes or No to enable or disable the Webex calendar service on the phone.

Options: Yes|No; Default: Yes

You can also configure the parameters in the configuration file (cfg.xml) by entering the strings in this format:

```
<Webex_Calendar_Enable ua="na">Yes</Webex_Calendar_Enable>
```

Click Submit All Changes .

## Enable call recording with SIP REC

You can enable call recording on a phone so that your user can record an active call. The
        recording mode configured on the server controls the display of the recording softkeys for
        each phone. In the Programmable Softkeys section, by default, the
        following strings are added in the Connected Key List and Conferencing Key List fields. crdstart;crdstop;crdpause;crdresume

Always

No softkeys available.

Your user can't control recording from the phone. Recording starts automatically
                  when a call is connected.

PauseRec

ResRec

When call is connected, user can pause the recording and resume the
                  recording.

Record

PauseRec

ResRec

When a call is connected, recording starts automatically but the recording is not
                  saved until the user presses the Record softkey. Your user
                  sees a message when recording state changes.

On Demand with User Initiated Start

Record

PauseRec

StopRec

ResRec

The recording only starts when your user presses the Record softkey. Your user sees a message when recording state
                  changes.

No recording softkeys are available, hence user will not be able to record
                  calls.

Access the phone administration web page.

Select Voice > Phone .

In the Supplementary Services section, click Yes or click No to enable or disable the Call Recording Serv parameter.

You can configure this parameter in the phone configuration XML file (cfg.xml) by
            entering a string in this format:

Options: Yes and No

Default:
            No

Click Submit All Changes .

## Configure multicast paging

You can set up multicast paging to allow users to send paging messages to other phones. The page can go to all phones or a group of phones in the same network. Any phone in the group can initiate a multicast paging session. The page is received only by the phones that are set to listen for the paging group.

A phone can be added to up to10 paging groups. Each paging group has a unique multicast port and number. The phones within a paging group must subscribe to the same multicast IP address, port, and multicast number.

You configure the priority for the incoming page from a specific group. When a phone is active and an important page must be played, the user hears the page on the active audio path.

When multiple paging sessions occur, they are answered in chronological order. After the active page ends, the next page is automatically answered. When do not disturb (DND) applies to all lines on a phone instead of a specific line, the phone ignores any incoming paging.

You can specify a codec for the paging to use. The supported codecs are G711a, G711u, G722, and G729. If you don't specify the codec, paging uses G711u by default.

You can also enable phones to receive pages from a server to optionally display an image or other UI elements. With this feature, an XML service can be invoked during a multicast paging. To enable this feature, configure the parameter XML Application Service URL and add " xmlapp=yes " in the paging group scripts from Voice > Phone . For more information about the parameters, see XML applications configuration for phones on BroadWorks and Parameters for multiple paging group .

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code. To configure each parameter, see the syntax of the string in Parameters for multiple paging group .

Before you begin

- Make sure that your network supports multicast so that all devices in the same paging group are able to receive paging.

- For Wi-Fi networks, enable and properly configure the access point for multicast.

- Make sure that all the phones in a paging group are in the same network.

Access the phone administration web page.

Select Voice > Phone .

Go to the Multiple Paging Group Parameters section.

Enter multicast paging scripts as defined in the following table of Parameters for multiple paging group .

Click Submit All Changes .

### Parameters for multiple paging group

The following table defines the function and usage of the multiple paging group parameters in the phone administration page.

It also defines the syntax of the string that is added in the phone configuration file (cfg.xml) to configure a parameter.

Enter a string to configure the phone to listen for and initiate multicast paging. You can add a phone to up to 10 paging groups. Enter the script in this format:

pggrp=<multicast-address>:<port>;<name=group_name>;<num=multicast_number>; <listen=boolean_value>;<pri=priority_level>;<codec=codec_name>;

Example script :

pggrp=224.168.168.168:34560;name=Group_1;num=800;listen=yes;pri=1;

pggrp=<multicast-address>:<port>;<name=group_name>;<num=multicast_number>; <listen=boolean_value>;<pri=priority_level>;<codec=codec_name>;<xmlapp=boolean_value>;<timeout=seconds>

Example script :

pggrp=224.168.168.168:34560;name=Group_1;num=800;listen=yes;pri=1;xmlap- p=yes;timeout=3600;

Make sure that you set the same multicast IP address and port for all the phones within a paging group. Otherwise, the phones can't receive paging.

- Paging group name (name)—Optionally enter the name of the paging group. The name helps you identify the paging group the phone is in when you have multiple paging groups.

- Multicast number (num)—Specify the number for the phone to listen for multicast paging and initiate a multicast paging session. Assign the same multicast number to all the phones within the group. The number must comply to the dial plan specified for the line to initiate a multicast.

- Listen status (listen)—Specify whether the phone listens for paging from this group. Set this parameter to yes to make the phone listen for the paging. Otherwise, set it to no , or don't include this parameter in the script.

0: Paging takes precedent over phone call. When the phone is on an active call, an incoming paging places the active call on hold. The call resumes when the paging ends.

1 : When the phone receives an incoming paging on an active call, the user hears the mix of the paging and the call.

2 : The user is alerted with the paging tone when receiving an incoming paging on an active line. The incoming paging isn't answered unless the active call is put on hold or ends.

3 : The phone ignores the incoming paging without any alert when the phone is on an active call.

- Audio codec (codec)—Optionally specify the audio codec for the multicast paging to use. The supported codecs are G711a, G711u, G722, and G729. If you don't specify the codec or don't include the codec parameter in the script, the phone uses G711u codec.

Make sure that the parameter XML Application Service URL in XML services is configured, see XML services for details.

In the XML URL, the macro MCASTADDR must be configured to distinguish it from the normal multicast paging. For example, http(s)://<url>?mcast=$MCASTADDR

Typically, the XML application ends after the timeout is reached, in regardless of the paging call. If the paging call is still active, only the XML application ends.

A new paging closes the XML application of the last paging, if the XML application is not closed when the last paging ended.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

<Group_1_Paging_Script ua="na">pggrp=224.168.168.168:34560;name=Group_1; num=800;listen=yes;pri=1;codec=g722;xmlap- p=yes;timeout=3600;</Group_1_Paging_Script>

Default: Empty

## Configure a phone to answer pages automatically

The paging feature enables a user to directly contact another user by phone. If the phone of the person being paged has been configured to answer pages automatically, the phone does not ring. Instead, a direct connection between the two phones is automatically established when paging is initiated.

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code.

Before you begin

Access the phone administration web page.

Select Voice > User .

In the Supplementary Services section, choose Yes for the Auto Answer Page parameter.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<Auto_Answer_Page ua="na">Yes</Auto_Answer_Page>
```

Options: Yes and No

Default: Yes

Click Submit All Changes .

## Prepare your wallpaper and logo images

To get the best experience, keep the following tips in mind when choosing or designing your images:

- Avoid using clustered images that can make it hard for you to identify phone lines on the home screen. Simplicity is key when selecting wallpapers.

- Ensure that your chosen wallpapers match your phone's color scheme. Opt for wallpapers that complement either the dark or light color palettes. Dark images are best suited for dark mode, while light images work well for light mode.

- Avoid using high contrast images as wallpapers. The extreme contrast can make it challenging to see the logo and other screen elements against the background.

- Avoid using dynamic images as wallpapers.

- The logo displays on the phone screen only, and it doesn't display on the KEM screen. When multiple lines are configured on Cisco Desk Phone 9841, 9851, and 9861, the logo and the logo setting in the Settings menu are unavailable.

- To use custom wallpaper on phones with Key Expansion Modules (KEM) attached, prepare both phone wallpaper and KEM wallpaper.

Cisco Desk Phone 9851: 190x125

Cisco Desk Phone 9861: 380x250

Cisco Desk Phone 9871: 494x325 / 418x275

Cisco Video Phone 8875: 380x250

You don't need to create a separate thumbnail image for the
                  logo. The system automatically scales the logo image to fit the dimensions of the
                  thumbnail.

Cisco Desk Phone 9851: 480x240

Cisco Desk Phone 9861: 800x480

Cisco Desk Phone 9871: 1280x720

Cisco Desk Phone 9800 Key Expansion Module: 480x800

Cisco Video Phone 8875: 1024x600

Cisco Desk Phone 9851: 100x56

Cisco Desk Phone 9861: 150x90

Cisco Desk Phone 9871: 228x128

Cisco Video Phone 8875: 180x100

Choose your desired logo and wallpaper images.

Format the images to meet the required specifications as described in the table above.

Rename the wallpaper image files in this format:

- For phone wallpaper and KEM wallpaper images, use wallpaper-xxx.png .
              Replace xxx with your desired name. For example, wallpaper-blue.png , wallpaper-darkgreen.png .

- For phone wallpaper thumbnail images, use thumbnail-xxx.png . Replace xxx with your desired name. For example, thumbnail-blue.png , thumbnail-darkgreen.png .

- The system cannot utilize wallpaper files that are named using different patterns. However, for the logo file, you have the flexibility to name it as per your requirements.

- Make sure that the phone wallpaper and KEM wallpaper have the same filename. Otherwise, the system will fail to load the KEM wallpaper and use the system default wallpaper for KEM.

- For the xxx in the filename, do not use special characters. Only use letters and numbers.

- Thumbnail images for logo and KEM wallpapers are not required.

### Customize wallpaper and logo on phone web page

You can choose a predefined system wallpaper, and customize wallpaper and logo on the phone administration web page.

Access the phone administration web page.

Select Voice > User .

Navigate to the Screen section and configure the following parameters to customize the phone screen.

Default: Violet Dark

Options: Cyan Dark, Purple Dark, Blue Dark, Violet Dark, Blue Light, Violet Light, CustWallpaper <n>

Selects the wallpaper for the phone's home screen and the color theme for its user interface.

To select a custom wallpaper from the list, make sure that the relevant parameter Custom Wallpaper Download URL [n] ( n represents the sequence number) is configured correctly.

The phone user can change the setting in the phone's settings menu.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

<Appearance ua="na">CustWallpaper 1</Appearance>

Enter the string in this format:

serv=<URL_Address>;image= <Wallpaper_Filename> ;[thumbnail= <Thumbnail_Filename> ;][kem= <KEM_Wallpaper_Filename> ;][theme= <light/dark> ;]

Where:

- serv : The URL address of the server where the image files are stored. To remove the wallpapers, just leave the field empty.

- image : The custom wallpaper image that will display on the phone screen.

- thumbnail : The thumbnail of the specified image. If the field isn't configured or the phone fails to fetch the image, the phone will display a dark or light image instead.

- kem : The custom wallpaper image that will display on the KEM screen. If the field isn't configured or the phone fails to fetch the image, then the KEM will use Violet Light or Violet Dark as the custom wallpaper.

- theme : The default theme of the specified images. If the field isn't configured or is configured incorrectly, the theme will be light.

Example 1:

serv=http://10.74.51.12/wallpaper/;image=wallpaper-sun.png;thumbnail=thumbnail-sun.png;kem=kem-wallpaper-sun.png;theme=dark;

Example 2:

The example shows that only the image and theme are configured in the string. The image of thumbnail will be a dark image, and the custom wallpaper of KEM will be Violet Dark.

serv=http://10.74.51.12/wallpaper/;image=wallpaper-sun.png;theme=dark;

Example 3:

You can also add a subpath for the "image", "thumbnail", and "kem":

serv=http://10.74.51.12/wallpaper/;image= <Wallpaper_Subpath>/ wallpaper-sun.png;thumbnail= <Thumbnail_Subpath>/ thumbnail-sun.png;kem= <KEM_Subpath>/ kem-wallpaper-sun.png;theme=dark;

- The maximum number of the custom wallpapers on Cisco Desk Phone 9851 is limited to 10. For other models (such as, 9861/9871/8875), the maximum number is 20.

- To remove the custom wallpaper, clear the download URL and leave the parameter empty.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

<Custom_Wallpaper_Download_URL_1 ua="na">serv=http://10.74.51.12/wallpaper/;image=wallpaper-sun.png;thumbnail=thumbnail-sun.png;kem=kem-wallpaper-sun.png;theme=dark;</Custom_Wallpaper_Download_URL_1>

Options: Yes, No

Before the parameter is set to Yes , make sure that the relevant parameter Logo URL is configured correctly.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

<Logo_Enable ua="na">Yes</Logo_Enable>

To remove the specified logo, make sure to leave the parameter empty.

Only one logo can be applied for the phones.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

<Logo_URL ua="na">http://10.74.51.12/mylogo/logo.png</Logo_URL>

Click Submit All Changes .

(Optional) To check the download status of the images, select Info > Download Status , and then navigate to the Screen Status section.

## Enable inline call label or session

You can enable the feature to automatically minimize a call window to an inline call label. In the inline call label itself, you can still view the call session information, such as the caller or callee name, contact number, call duration, call state. The minimized call windows make sure that you can view status of other lines, BLF/SD features, and the current call information.

Call windows that support the inline call label feature (or auto collapsed):

- Incoming call

- Single call

- All calls list

- New call (if you return to the home screen)

This feature is only available on the following phone models that have multiple lines:

- Cisco Desk Phone 9841

- Cisco Desk Phone 9851

- Cisco Desk Phone 9861

For the inline call label or session, the users can press the line key to restore it to a full call window, where more information is provided.

When users press the Home softkey on a call window, the call window will be minimized to the inline call label automatically. This behavior is also applicable when the users return to the home screen from the New call screen.

If Key Expansion Module (KEM) is attached to the phone with a line configured on KEM line key, the call session information can display on the KEM line label itself . Due to the width limitation of KEM, the caller name doesn't display on the KEM line label itself when the call is connected.

Access the phone administration web page.

Select Voice > User .

In the Supplementary Services section, select Yes for the parameter Auto Collapse Into Line Key .

To disable the feature, select No .

You can also configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

<Auto_Collapse_Into_Line_Key ua="rw">Yes</Auto_Collapse_Into_Line_Key>

Default: No .

Click Submit All Changes .

## Manage the Settings menu visibility

Customize the phone's Settings menu to display only the menu items you want users to
        access.

By default, all menu items are visible on the phone. When you hide certain menu items, the
        index numbers of the remaining items will adjust automatically.

The custom settings take effect only on phones that have completed registration. On
          phones not yet onboarded to a calling system, all menu items remain visible.

Access the phone administration web page.

Click Voice > Phone .

In the Menu Customization section, set the desired menu items to
          Show or Hide.

The availability of menu items may vary by phone model. If all the child items are hidden, the parent menu is also hidden.

Click Submit All Changes to apply the changes.

## Set the phone to always display the multi-line interface

The Always Use Multi-line Mode parameter is only available on Cisco
        Desk Phone 9841, 9851, and 9861. It ensures a consistent user experience by forcing the
        phone to always display the multi-line layout.

By default, the phone displays the multi-line interface only when multiple lines or other
        line key features are configured. When Always Use Multi-line Mode is enabled, the phone uses
        the multi-line layout even if only a single line is configured.

Access the phone administration web page.

Click Voice > Phone .

In the Miscellaneous Line Key Settings section, set the Always Use Multi-line Mode filed to Enabled .

You can also use the configuration XML file (cfg.xml) to customize the Settings menu.
            See the following example:

```
<Always_Use_Multi-line_Mode ua="na">Disabled</Always_Use_Multi-line_Mode>
```

Click Submit All Changes to apply the changes.

## Enable xAPI on your phones

xAPI is a set of APIs used to monitor, manage, and control PhoneOS-based devices. In this
          release, we are introducing xAPI as a new option for customers and partners to manage
          phones and build custom solutions. Customers and partners can access xAPI through HTTP or
          HTTPS.

Cisco Desk Phone 9811 doesn't support this feature on PhoneOS
          4.0.1 or earlier.

The following features are now supported on phones registered to Webex Calling, Cisco
          Unified CM, or Cisco BroadWorks:

Retrieve basic device information and status, and subscribe to phone events

Perform device reboot and factory reset

Simulate hard key presses and screen touch operations

Capture device screens

Initiate calls

For information about the supported xAPIs and the related documentation, see https://phoneos.cisco.com .

Before you begin

Your phone is running PhoneOS 3.5 or a later version.

Prepare an HTTP client and HTTP server for feedback collection.

Access the phone administration web page.

Select Voice > System .

In the System Configuration section, and configure the following
          parameters:

Enable Web Server : Set this field to Yes .

Enable Protocol : Choose the protocol to use — Http or Https — based on your
                server’s configuration.

Web Server Port : Specify 443 as the
                port number that the web server will use for incoming connections.

You can also use the configuration XML file (cfg.xml) to customize the Settings menu.
            See the following
            example:

```
<Enable_Web_Server ua="na">Yes</Enable_Web_Server>
<Enable_Protocol ua="na">Https</Enable_Protocol>
<!-- available options: Http|Https -->
<Enable_Direct_Action_Url ua="na">Yes</Enable_Direct_Action_Url>
<Web_Server_Port ua="na">443</Web_Server_Port>
```

Provide the xAPI administrator credentials in the phone configuration file
          (cfg.xml).

Only authorized administrators can remotely manage phones using xAPIs. Enter the
            username and password in the following format:

```
<xAPI_Admin_User_Name>admin_username</xAPI_Admin_User_Name>
<xAPI_Admin_Password>admin_password</xAPI_Admin_Password>
```

When done, click Submit All Changes .

## Ringtone settings

Ringtone settings let you manage how the phone alerts users to incoming calls. You can
      customize ringtones and assign them to specific lines or extensions. This helps users easily
      distinguish between personal, shared, or priority calls.

### Assign a ringtone to a line

By default, all lines on the phone
        use the same ringtone for incoming call alerts. You can configure a different ringtone for
        an individual line or extension so that incoming calls on that line use a designated ring
        pattern. Assigning different ringtones to different lines helps users identify which line is
        receiving a call and manage calls more efficiently.

Users can also change the ringtone on the phone if they have access to the settings.
        Changes made on the phone sync to the phone administration web page.

Access the phone administration web page.

Select Voice > Ext [n] .

In the Call Feature
            Settings section, select a ringtone in the Default
            Ring drop-down list.

If No Ring is selected, the phone doesn't ring for incoming
            calls on that line.

You can also configure this parameter in the configuration file (cfg.xml) by entering a
            string in this format:

Example of using a built-in ringtone: <Default_Ring_3_
              ua="rw">2</Default_Ring_3_>

Example of using a custom ringtone: <Default_Ring_3_ ua="rw">Custom
              1</Default_Ring_3_>

When configuring ringtone using the configuration file, refer to the Ringtone list for the ringtone mapping. If
            you assign an unconfigured custom ringtone to a line, the line uses the default built-in
            ringtone ( 1 ). For instructions on configuring custom ringtones,
            see Configure custom ringtones .

Click Submit All
            Changes .

### Customize the built-in ringtone patterns

Your phone includes built-in ringtones with default patterns. You can customize
        these ringtones by adjusting their cadence to create distinctive ring patterns that meet
        organizational requirements or improve call identification and management.

Use a
        ringtone script to configure the characteristics of each ringtone. When the phone receives
        SIP Alert-INFO message and the message format is correct, then the phone plays the specified
        ringtone. Otherwise, the phone plays the default ringtone.

The ringtone script uses
        the following syntax :

The ringtone name displayed on the phone. The name
            is also used in the SIP Alert-Info header of an incoming INVITE request to instruct the
            phone to play the corresponding ringtone. The name must contain only characters that are
            valid in a URL.

The index of the waveform or the ringtone audio
            file stored locally on the phone. For example, w=file://Mellow.rwb , w=3 .

The built-in waveforms are:

1 = Classic phone with mechanical bell

2 = Typical phone ring

3 = Classic ring tone

4 = Wide-band frequency sweep signal

The
            options range from 1 to 9. See the following table for the pattern
            definitions:

The cadence ID can be set to 0 when w = 3 or 4 . Setting c = 0 uses the ringtone
              file’s natural duration as the on‑time.

Access the phone administration web page.

Select Voice > Phone .

In the Ringtone section, change the cadence of the ringtones and change the Silent Ring
            Duration setting, if needed.

Silent Ring Duration controls the duration of the silent ring. For example, if the
            parameter is set to 20 seconds, the phone plays the silent ring for 20 seconds then
            sends 480 response to INVITE message.

You can also configure this parameter in the configuration file (cfg.xml) by entering a
            string in this format:

Click Submit All
            Changes .

What to do next

Assign the ringtone to a
        line

### Configure custom ringtones

Your phone supports up to 10 custom ringtones. When configured, users can assign them to
          individual lines on the phone.

In the ringtone list on the phone, new custom ringtones display (Not
            installed) next to the ringtone name until they are played or applied to a
          line.

Before you begin

Make sure your ringtone files meet these requirements:

File formats:

.raw : 8 kHz mono G.711 μ-law, no header

.rwb : 16 kHz mono 16-bit linear PCM, no header

Maximum file size: 960 KB

The phone must have network access to the server hosting the ringtone files.

Access the phone administration web page.

Select Voice > Phone .

In the Ringtone section, enter the URL of your ringtone files in
          the Custom Ringtone Download URL 1 - 10 fields.

The supported protocols for these URLs are http, https, and tftp.

Click Submit All
            Changes .

The phone reboots automatically to load the custom ringtones.

After the phone boots up, go to Voice > Ext [n] .

In the Call Feature Settings section,
          select the custom ringtone in the Default Ring drop-down
          list.

Click Submit All Changes .

You can also configure custom ringtones in the configuration file (cfg.xml) by entering
            a string in this
            format:

```
<Custom_Ringtone_Download_URL_1 ua="na"/>http://10.70.50.200/ringtone/calculation.rwb</Custom_Ringtone_Download_URL_1>
<Default_Ring_3_ ua="rw">Custom 1</Default_Ring_3_>
```

| Feature | Required firmware version |
|---|---|
| Emergency call | PhoneOS 3.0.1 and later |
| Custom service | PhoneOS 3.2.1 and later |
| Multiple triggers | PhoneOS 3.3.1 and later |
| HTTP Post | PhoneOS 3.3.1 and later |
| Multiple events on a single trigger | PhoneOS 3.4.1 and later |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | Navigate to the Action Button section and configure the
          following parameters to link the Action button with an emergency service. Action Button Function : Select Emergency
                  Call . Action Button Service Destination : Enter the phone number or
                the URI of the emergency service. Action Button Service Name (Optional): Specify a name for
                the service associated with the action trigger. This name will be displayed in the
                on-screen message when the user presses the button, indicating which event will be
                initiated. If no name is specified, Emergency call will be used as the
                display name. Dial Out Delay : Set the timeout period (in seconds) for the
                phone to initiate an emergency call after the trigger is detected. The default value
                is 5 seconds. If set to 0, the call is placed immediately upon detecting the
                trigger. Service Trigger Select a trigger
                from the list: Single Press , Long
                  Press , or Press 3 Times . Silent Emergency Call (Optional): By default, the emergency
                call functions as a two-way call, similar to other outgoing calls. When silent
                emergency call is enabled, the audio is silent on the caller side to avoid drawing
                attention during the onging call. Only the call recipient can end the silent
                emergency call. During a silent emergency call, the screen on phone 9811 and 9841 will freeze,
                while the screen on phone 9851, 9861, and 9871 will be turned off. All other
                functions are inaccessible. The phone restores normal operation after the recipient
                ends the call. Allow Silent
                  Emergency Call Retrieval (Optional): Enable this feature if you allow
                users to press any key to restore normal phone operation while maintaining the
                emergency call. The call audio remains silent unless the user increases the speaker
                volume using the Volume key. For more details about these parameters, see Parameters for the Action
              button . You can also configure these parameters in the phone configuration XML file (cfg.xml)
            by entering the following
            strings: |
| 4 | When done, click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | Navigate to the Action Button section and configure the following parameters to associate the Action button with a service. Action Button Function : Select Custom . Action Button Service Name (Optional): Specify a name for the service associated with the trigger. This name
                will be displayed in the on-screen message when the user presses the button,
                indicating which service will be triggered. When no name is specified, Custom
                  service will be used as the display name. Action Button Service Destination :
                Enter the URL of the custom service. The URL must start with http:// or https:// , for example, https://10.11.20.159/path/service.xml . Custom Content Field (Optional): If
                you want to enable the phone to send an HTTP Post request when the Action button is
                pressed, enter the HTTP data such as method, header, and post content, with a
                maximum length of 1024 characters. For POST script examples and the syntax, see HTTP Post request for the
                  Action button . Dial Out Delay : Set the timeout
                period, in seconds, for the phone to initiate an event after detecting the trigger.
                The default value is 5 seconds. When set to 0, the event is initiated immediately
                upon trigger detection. Service Secret (Optional): Enter
                the authentication secret, token or password if your custom service requires
                authentication to access it. The entered secret is displayed as a masked string and
                can be referenced using the macro $SS in Custom Content
                  Field and Action Button Service
                Destination . Service Trigger Select a trigger
                from the list: Single Press , Long
                  Press , or Press 3 Times . Silent Emergency Call (Optional): If you have included a
                  phone number or dialing URI in the service destination, enabling this feature will
                  silent emergency calls. By default, the emergency call functions as a two-way call, similar to other
                  outgoing calls. When set to enabled, the audio is silent on the caller side to
                  avoid drawing attention during the onging call. Only the call recipient can end
                  the call. During a silent emergency call, the screen on phone 9811 and 9841 will freeze,
                  while the screen on phone 9851, 9861, and 9871 will be turned off. All other
                  functions are inaccessible. The phone restores normal operation after the
                  recipient ends the call. For more details about these parameters, see Parameters for the Action
              button . You can also configure these parameters in the phone configuration XML file (cfg.xml)
            by entering the following
            strings: |
| 4 | When done, click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | Navigate to the Action Button section and configure the
          following parameters to associate the Action button with a service. Action Button Function : Select Custom . Action Button Service Destination : Enter the phone number
                  to call and the XML service URL in this format: tel:<phonenumber or SIP URI> +
                  <serviceURL> The URL must start with http:// or https:// . Example: tel:1234 + https://10.11.20.159/path/service.xml Action Button Service
                  Name (Optional): Specify a name for the service associated with the
                action trigger. This name will be displayed in the on-screen message when the user
                presses the button, indicating which service will be triggered. When no name is
                specified, Custom
                  service will be used as the display name. Custom Content Field (Optional): If you want to enable the
                phone to send an HTTP Post request when the Action button is pressed, enter the HTTP
                data such as method, header, and post content, with a maximum length of 1024
                characters. For POST script examples and the syntax, see HTTP Post request for the
                  Action button . Dial Out Delay : Set the timeout
                period, in seconds, for the phone to initiate an event after detecting the trigger.
                The default value is 5 seconds. When set to 0, the event is initiated immediately
                upon trigger detection. Service Secret (Optional): Enter
                the authentication secret, token or password if your custom service requires
                authentication to access it. The entered secret is displayed as a masked string and
                can be referenced using the macro $SS in Custom Content
                  Field and Action Button Service
                Destination . Silent Emergency Call (Optional): If you have included a
                  phone number or dialing URI in the service destination, enabling this feature will
                  silent emergency calls. By default, the emergency call functions as a two-way call, similar to other
                  outgoing calls. When set to enabled, the audio is silent on the caller side to
                  avoid drawing attention during the onging call. Only the call recipient can end
                  the call. During a silent emergency call, the screen on phone 9811 and 9841 will freeze,
                  while the screen on phone 9851, 9861, and 9871 will be turned off. All other
                  functions are inaccessible. The phone restores normal operation after the
                  recipient ends the call. Allow Silent
                  Emergency Call Retrieval (Optional): Enable this feature if you allow
                users to press any key to restore normal phone operation while maintaining the
                emergency call. The call audio remains silent unless the user increases the speaker
                volume using the Volume key. For more details about these parameters, see Parameters for the Action
              button . You can also configure these parameters in the phone configuration XML file (cfg.xml)
            by entering the following
            strings: |
| 4 | When done, click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | Navigate to the Action Button section and select MultiTrigger in the Service Trigger field. |
| 4 | Based on your use cases, configure the parameters in the desired trigger
          sections. The following parameters are available in these sections - MultiTrigger -
            Single Press , MultiTrigger - Long Press , and MultiTrigger - Press Three Times . Action Button Function : Select the service that phone users
                can access via the trigger. Action Button Service Name (Optional): Specify a name for the service associated with the trigger. This name
                will be displayed in the on-screen message when the user presses the button,
                indicating which service will be triggered. When no name is specified, Custom
                  service will be used as the display name. Action Button Service Destination :
                Enter the URL of the custom service. The URL must start with http:// or https:// , for example, https://10.11.20.159/path/service.xml . Custom Content Field (Optional): If
                you want to enable the phone to send an HTTP Post request when the Action button is
                pressed, enter the HTTP data such as method, header, and post content, with a
                maximum length of 1024 characters. For POST script examples and the syntax, see HTTP Post request for the
                  Action button . Service Secret (Optional): Enter
                the authentication secret, token or password if your custom service requires
                authentication to access it. The entered secret is displayed as a masked string and
                can be referenced using the macro $SS in Custom Content
                  Field and Action Button Service
                Destination . Dial Out Delay : Set the timeout
                period, in seconds, for the phone to initiate an event after detecting the trigger.
                The default value is 5 seconds. When set to 0, the event is initiated immediately
                upon trigger detection. Silent Emergency Call (Optional): If you have set the
                  Action button for emergency calls, enabling this feature will silent emergency
                  calls. By default, the emergency call functions as a two-way call, similar to other
                  outgoing calls. When set to enabled, the audio is silent on the caller side to
                  avoid drawing attention during the onging call. Only the call recipient can end
                  the call. During a silent emergency call, the screen on phone 9811 and 9841 will freeze, while the screen on
                  phone 9851, 9861, and 9871 will be turned off. All other functions are
                  inaccessible. The phone restores normal operation after the recipient ends the
                  call. Allow Silent
                  Emergency Call Retrieval (Optional): Enable this feature if you allow
                users to press any key to restore normal phone operation while maintaining the
                emergency call. The call audio remains silent unless the user increases the speaker
                volume using the Volume key. This parameter is located in the Action Button section. For more details about these parameters, see Parameters for the Action
              button . You can also configure these parameters in the phone configuration XML file (cfg.xml)
            by entering the following
            strings: |
| 5 | When done, click Submit All Changes . |

| Parameter | Default and options | Description |
|---|---|---|
| Action Button Function | Default: Off Options: Off, Emergency Call, Custom | You can configure the button with a specific service. Off : When set to Off, the Action button for single
                      service on the phone will not function. Emergency Call : Users can use the Action button to
                      place an emergency call, if configured. Custom : Users can use the Action button to access the
                      custom service, if configured. When you set the field to Emergency Call or Custom , make sure that you enter the service
                    destination in the Action Button Service Destination field. Or, the phone will display a configuration error. |
| Action Button Service Name | Default: Empty | Optionally specify a name for the service associated with the Action button.
                    This name will be displayed in the on-screen message when the user presses the
                    button, indicating which service will be triggered. If you don't specify a name, the default name will be Emergency call, Silent
                    emergency call, or Custom action based on your selection in the Action Button Function field. |
| Action Button Service Destination | Default: Empty | Provide the service destination in one of the following formats based on the
                    service assigned to the Action button: For emergency call services, enter a telephone number or the URI of
                        emergency service. When configure the button for a custom service, enter the service URL. The
                        URL must start with http:// or https:// . For example, https://10.11.20.159/path/service.xml . To configure the button to initiate multiple events with a single trigger,
                        enter tel:<phonenumber or SIP URL> + <Service
                          RUL> . Example : tel:1234 +
                          https://10.11.20.159/path/service.xml . Calling SIP URIs is also supported. Enter the URI in the format of tel: sip 4567@co.webex.com If you enable the Action button without setting a valid service destination,
                    the user on the phone will see a message prompting for configuration. After the
                    user closes this notification, the warning icon will persist in the header of
                    the phone screen until the button is properly configured or disabled. Phone numbers cannot be used as destinations for custom services. If you
                      configure the Action Button as Custom and enter a phone
                      number as the service destination, an alert message will display on the phone
                      indicating that the button is unconfigured. Instead, you can add a phone
                      number in this format tel:<phone number> , for
                      example, tel:1234 . |
| Custom Content Field | Default: Empty | This setting works only when the Action Button
                        Function is set to Custom . Enter the HTTP data such as method, header, and post content, with a maximum
                    length of 1024 characters. When configured, the phone sends an HTTP Post request
                    when the Action is pressed. You can also use other macros such as $MA, $SN. For POST script examples and the syntax, see HTTP Post request for the Action button . |
| Service Secret | Default: Empty | A service secret can be an authentication secret, token or password. The
                    entered secret is displayed as a masked string and can be referenced using the
                    macro $SS in Custom Content Field and Action Button Service Destination . |
| Service Trigger | Default: Single Press Options: Single Press, Long Press, Press 3 times,
                  MultiTrigger | Choose how users can place an emergency call or initiate a custom service using
                    the phone's Action button. Single Press : Press the Action button to trigger the
                    associated call or service. Long Press : Press the Action button down for at least 2
                    seconds to trigger the associated call or service. Press 3 times : Press the Action button three times with
                    intervals of one second between each press to trigger the associated call or
                    service. MultiTrigger :
                    Select this option to associate multiple triggers and events to the Action
                    button. Then, go to the MultiTrigger - Single Press , MultiTrigger - Long Press , and MultiTrigger
                      - Press Three Times sections to configure the specific
                    settings. |
| Dial Out Delay | Default: 5 Options: 0 - 30 | Set the timeout period, in seconds, for the phone to initiate an emergency call
                    or a custom action after the Action button is pressed. Set it to 0 if you prefer the phone to place the call or initiate an event
                    immediately upon detecting the trigger, as specified by a single press, long
                    press, or triple presses on the button. |
| Silent Emergency Call | Default: Disabled Options: Enabled, Disabled | Silent emergency call is designed for discreet assistance in dangerous
                    situations. It enables users to seek help without making any noise. When enabled, users are able to place one-way calls with the Action button. After the silent emergency call is placed, only the other party can end the
                        call. To avoid drawing attention during the ongoing call, the screen on
                        phone 9811 and 9841 will freeze, while
                        the screen on phone 9851, 9861, and 9871 will be turned off. The phone locks all
                          functions during a silent emergency call, by default. To allow users to
                          restore normal phone operation while maintaining the silent emergency
                          call, enable the Allow Silent Emergency Call
                            Retrieval feature. When disabled, the emergency call functions as a two-way call, similar to
                        other outgoing calls. |
| Allow
                  Silent Emergency Call Retrieval | Default: No Options: Yes, No | Controls whether users can retrieve phone functionality during a silent
                    emergency call. By default, once a silent emergency call is initiated, the phone
                    locks all functions until the call recipient ends the call. When this parameter is set to Yes , users can press any
                    key to restore normal phone operation while maintaining the emergency call. The
                    call audio remains silent unless the user increases the volume using the Volume
                    key. |

| Parameter | Default and options | Description |
|---|---|---|
| Action Button Function | Default: Off Options: Off, Emergency Call, Custom | Select the service that phone users can access via the service trigger. Off : When set to Off, the action trigger will not
                      function. Emergency Call : Users can place a call to the
                      designated emergency number via the action trigger. Custom : Users can access the designated service via
                      the action trigger. When you set the field to Emergency Call or Custom , make sure that you enter the proper service
                        destination in the Action Button Service Destination field. Or, the phone will display a configuration error. |
| Action Button Service Name | Default: Empty | Optionally specify a name for the service associated with the action trigger.
                    This name will be displayed in the on-screen message when the user presses the
                    button, indicating which service will be triggered. If you don't specify a name, the default name will be Emergency call, Silent
                    emergency call, or Custom action based on your selection in the Action Button Function field. |
| Action Button Service Destination | Default: Empty | Provide the phone number, the URI for emergency call, or the URL for the custom
                    service. If you enter a service URL, the URL must start with http:// or https:// . Example: https://10.11.20.159/path/service.xml . Phone numbers cannot be used as destinations for custom services. If you
                      configure the Action Button as Custom and enter a phone
                      number as the service destination, an alert message will display on the phone
                      indicating that the button is unconfigured. Instead, you can add a phone
                      number in this format tel:<phone number> , for
                      example, tel:1234 . |
| Custom Content Field | Default: Empty | This setting works only when the Action Button
                        Function is set to Custom . Enter the HTTP data such as method, header, and post content, with a maximum
                    length of 1024 characters. When configured, the phone sends an HTTP Post request
                    when the Action is pressed. You can use macros in the HTTP data, such as $MA, $SN. For POST script examples and the syntax, see HTTP Post requests for
                    the Action button . |
| Service Secret | Default: Empty | A service secret can be an authentication secret, token or password. The
                    entered secret is displayed as a masked string and can be referenced using the
                    macro $SS in Custom Content Field and Action Button Service Destination . |
| Dial Out Delay | Default: 5 Options: 0 - 30 | Set the timeout period, in seconds, for the phone to initiate an emergency call
                    or a custom action after the Action button is pressed. Set it to 0 if you prefer the phone to place the call or initiate an event
                    immediately upon detecting the trigger, as specified by a single press, long
                    press, or triple presses on the button. |
| Silent Emergency Call | Default: Disabled Options: Enabled, Disabled | Silent emergency call is designed for discreet assistance in dangerous
                    situations. It enables users to seek help without making any noise. When enabled, users are able to place one-way calls with the Action button. After the silent emergency call is placed, only the other party can end the
                        call. To avoid drawing attention during the ongoing call, the screen on
                        phone 9811 and 9841 will freeze, while
                        the screen on phone 9851, 9861, and 9871 will be turned off. The phone locks all
                          functions during a silent emergency call, by default. To allow users to
                          restore normal phone operation while maintaining the silent emergency
                          call, enable the Allow Silent Emergency Call
                            Retrieval feature. When disabled, the emergency call functions as a two-way call, similar to
                        other outgoing calls. |

| Macro name | Macro expansion |
|---|---|
| #DEVICENAME# | The device name displayed in the calling system; for
                example, SEP845A3EC21288 |
| $MA | MAC address using lowercase hex digits
                (000e08aabbcc). |
| $MCASTADDR | Address of multicast paging application. |
| $PN $PSN | Product Name; for example, DP-9851, DP-9871. |
| $SN | Serial Number string; for example,
                FVH28022D0T. |
| $SS | Service secret required to access an XML
                application. |

| Feature | 8875 | 9811 | 9841 | 9851 | 9861 | 9871 |
|---|---|---|---|---|---|---|
| Display Off | Yes | No | Yes | Yes | Yes | Yes |
| Deep Sleep (Controlled by phone) | No | No | Yes | Yes | Yes | Yes |
| Cisco Smart Power (Deep Sleep controlled by switch) | Yes | Yes | Yes | Yes | Yes | Yes |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | Customize working hours and workdays to reflect the business hours of your users. Cisco Desk Phone 9811 doesn't support Display Off Mode. Office Hours Enabled : By default, the Office Hours feature
                is enabled. If disabled, your phone won't enter power saving mode. Workdays : The default workdays are Monday through Friday.
                Change the workdays as needed. Working Hours Start and Working Hours
                  End : The default working hours are set to 7:00 to 19:00. Change the
                setting as needed. Display Off In Office Hours : By default, the phone display
                remains on during working hours. To enable the phone to enter Display Off Mode when
                inactive, select timeout period from the list. For more information about these parameters, see Parameters for Office Hours . |
| 4 | Configure the settings for Deep Sleep Mode for the 9800 Series phones. Deep Sleep Mode on Cisco Video Phone 8875 and Cisco Desk Phone 9811 can only be enabled by Cisco switches through the smart power feature. To configure
              the smart power settings, follow the steps in Allow Cisco switches to manage power modes for your phone (smart power) . Deep Sleep Enabled : Enable this feature to allow the phone
                to power off outside office hours. Enable Audible Alert (Optional): If set to True, the phone
                plays audio tone to alert the user before it enters Deep Sleep Mode. Phone Off Time After Working Hour End : Set the timeout
                period for the phone to automatically power off after the time specified in the Working Hours End field. The default setting is 60
                minutes. Phone On Time Before Working Hour Start : Set the timeout
                period for the phone to wake up from Deep Sleep Mode before the time specified in
                the Working Hours Start field. The default setting is 60
                minutes. Random Early Wakeup : Set the time interval for the phone to
                wake up before its regular schedule. It helps distribute the load of connection and
                registration requests when a large number of phones power on simultaneously. Random Delay to Sleep : Set a time interval for the phone to
                enter Deep Sleep Mode after its scheduled power-off time. Idle Timeout : Sets timeout period for the phone to enter
                Deep Sleep Mode. For more information about these parameters, see Parameters for Office Hours . |
| 5 | Configure the settings for Display Off Mode outside office hours. Handset LED in Display Off Mode (Video Phone 8875): Controls whether the handset LED lights up to notify users of phone statuses in Display Off mode. When disabled, the handset LED is off. When enabled, its indication behavior is the same as when the display is on. This setting works only when the LED Indicator In Display Off Mode parameter is set to Enabled. Line Key and Top 360 LED in Display Off Mode (Cisco Desk Phone 9841, 9851, 9861, and 9871): Controls whether the LEDs light up to notify users of phone statuses in Display Off mode. When disabled, both the Line Key LEDs on phone and Key Expansion Module (KEM) and Top 360 LEDs are off. When the corresponding LED is enabled, its indication behavior is the same as when the display is on. This setting works only when the LED Indicator In Display Off Mode parameter is set to Enabled. LED Indicator In Display Off Mode : This setting determines
                whether to turn off the Front Arc LED when the phone enters Display Off Mode, both
                during or outside office hours. By default, the Front Arc LED remains illuminated
                after the phone enters Display Off Mode. When set to disabled, the Front Arc LED is
                off in Display Off Mode. Idle Timeout : Set the timeout period in minutes for the
                phone to automatically turn off the screen after being awakened during Display Off
                Mode. For more information about these parameters, see Parameters for Office Hours . |
| 6 | When done, click Submit All Changes . |

| Smart Power | Smart Power Override | Description |
|---|---|---|
| Disabled | Yes / No | Smart power is disabled. The phone follows the power saving configuration set on
                  its calling system. |
| Enabled for non-work day only | No | Smart power is enabled only on non-work days. On non-work days, the phone follows the display off and deep sleep schedules
                  configured on its calling system. The switch wakes the phone from deep sleep following the phone's schedule. |
| Yes | Smart power is always enabled. Since Smart Power Override is set to Yes,
                the switch manages the phone's display off and deep sleep modes based on the
                schedules configured on the switch. The phone's own settings in its calling system
                are overridden. |
| Enabled for all days | No | Smart power is always enabled. The phone follows the display off and deep sleep schedules set on its calling
                  system. The switch wakes the phone from deep sleep following the phone's schedule. |
| Yes | Smart power is always enabled. Since Smart Power Override is set to Yes,
                the switch manages the phone's display off and deep sleep modes based on the
                schedules configured on the switch. The phone's own settings in its calling system
                are overridden. |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | Go to the Outside Office Hours Smart Power section, and
          configure the following parameters: Smart Power Enabled : Enable the smart power feature. The
                available options are: False (Default): Disables smart power. Non-work Day Only : Enables smart power only on
                  non-working days. All Days : Enables smart power always, on both work days
                  and non-work days. Domain : Enter the smart power domain that the phone belongs
              to. Secret : Enter the password (shared secret) used for
              communication between the phone and the switch. Smart Power Override : Specify whether the
              switch can manage power modes based on the schedules configured on the switch,
              overriding the phone's configurations in the calling system. You can also use the configuration XML file (cfg.xml) to customize the Settings menu. See the
            following
            example: For more
          information about these parameters, see Parameters for Office Hours . |
| 4 | When done, click Submit All Changes . |

| Parameter | Default and options | Supported models | Description |
|---|---|---|---|
| Office Hours |
| Office Hours Enabled | Default: True Options: False, True | 8875 9841 9851 9861 9871 | Set this field to True to enable the Office Hours
                  feature for Cisco Desk Phone 9800 Series. The Office Hours feature is
                  designed to minimize power usage during inactivity periods on the phone. You can
                  configure the phone to automatically turn off the screen (Display Off Mode) or
                  power off (Deep Sleep Mode) outside of the designated working periods. You
                  can configure this parameter in the phone configuration XML file (cfg.xml) by
                  entering a string in this format: <Office_Hours_Enabled
                  ua="na">True</Office_Hours_Enabled> |
| Work Days | Default: Monday through Friday | 8875 9811 9841 9851 9861 9871 | Customize the workdays by specifying the desired days. During
                  non-workdays, the phone will automatically turn off the screen. By default,
                  workdays are set from Monday to Friday. This setting also applies to Deep
                  Sleep Mode, if enabled. If you choose to enable Deep Sleep Mode exclusively for
                  non-workdays, the phone will power off during those days. If you enable Deep Sleep
                  Mode for all days, the phone will power off during both non-workdays and
                  non-working hours on workdays. Set working hours for workdays using the Working Hours Start and Working Hours
                    End fields. You can configure this parameter in the phone
                  configuration XML file (cfg.xml) by entering a string in this
                  format: <Work_Days
                  ua="na">Monday\|Tuesday\|Wednesday\|Thursday\|Friday</Work_Days> |
| Working Hours Start | Default: 07:00 | 8875 9811 9841 9851 9861 9871 | Set the start time for working hours using the 24-hour format. Outside of
                  the specified working hours, the phone will automatically turn off the screen, or
                  enter Deep Sleep Mode only when Deep Sleep Enabled is set
                  to All Days . Examples: 09:00 for 09:00 am; 17:30 for
                  05:30 pm You can configure this parameter in the phone configuration XML
                  file (cfg.xml) by entering a string in this
                  format: <Working_Hours_Start
                  ua="na">06:00</Working_Hours_Start> |
| Working Hours End | Default: 19:00 | 8875 9811 9841 9851 9861 9871 | Set the end time for working hours using the 24-hour format. Outside of the
                  specified working hours, the phone will automatically turn off the screen, or
                  enter Deep Sleep Mode only when Deep Sleep Enabled is set
                  to All Days . Examples: 09:00 for 09:00 am; 17:30 for
                  05:30 pm Ensure that the interval between the start
                  and end time longer than 60 minutes. You can configure this parameter in
                  the phone configuration XML file (cfg.xml) by entering a string in this
                  format: <Working_Hours_End
                  ua="na">21:00</Working_Hours_End> |
| Display Off In Office Hours | Default: Disabled Options: Disabled, In 1 minute, In 5 minutes, In 30 minutes | 8875 9841 9851 9861 9871 | The LED indicator follows the setting found in Outside Office Hours Display Off > LED Indicator In Display Off Mode . You can configure this parameter in the phone configuration
                  XML file (cfg.xml) by entering a string in this
                  format: <Display_Off_In_Office_Hours
                  ua="na">Disabled</Display_Off_In_Office_Hours> |
| Outside Office Hours Deep Sleep When smart power isn't applied, the Deep Sleep settings work with the office
                    hours settings to determine the deep sleep schedule on 9841, 9851, 9861, and
                    9871. When smart power is applied and Smart Power Override is disabled, the switch
                    also uses these settings to control the deep sleep mode on all applicable
                    phones. |
| Deep Sleep Enabled | Default: False Options: False, Non-work Day Only, All Days | 9841 9851 9861 9871 | Enable or disable Deep Sleep Mode on the phone. When enabled, this feature
                  automatically powers off the phone outside of the designated office hours. This option works only when the Office Hours is enabled. When set to False , the phone will not enter Deep
                  Sleep Mode. When set to Non-work Day Only , the phone
                  will power off exclusively on non-workdays. For the specified workdays, the phone
                  will turn off the screen outside of the specified working hours. When set to All Days , the phone will power off during both
                  non-workdays and non-working hours on workdays. Set working hours for
                  workdays using the Working Hours Start and Working Hours End fields. You can configure this
                  parameter in the phone configuration XML file (cfg.xml) by entering a string in
                  this format: <Deep_Sleep_Enabled ua="na">Non-work Day
                  Only</Deep_Sleep_Enabled> |
| Enable Audible Alert | Default: False Options: False, True | 8875 9811 9841 9851 9861 9871 | Enable or disable the phone to play audio tone to alert the user before it
                  enters Deep Sleep Mode. You can configure this parameter in the phone
                  configuration XML file (cfg.xml) by entering a string in this
                  format: <Enable_Audible_Alert
                  ua="na">False</Enable_Audible_Alert> The smart power feature uses this setting to control the
                    phone's power mode only when Smart Power Override is
                    disabled. |
| Phone On Time Before Working Hour Start (mins) | Default: 60 Options: 0 - 360 | 8875 9811 9841 9851 9861 9871 | Set the timeout period for the phone to wake up from Deep Sleep Mode before
                  the time specified in the Working Hours Start field. If you
                  want the phone to wake up until working hours start, set it to 0. You can
                  configure this parameter in the phone configuration XML file (cfg.xml) by entering
                  a string in this
                  format: <Phone_On_Time_Before_Working_Hour_Start__mins_
                  ua="na">12</Phone_On_Time_Before_Working_Hour_Start__mins_> The smart power feature uses this setting to control the
                    phone's power mode only when Smart Power Override is
                    disabled. |
| Phone Off Time After Working Hour End (mins) | Default: 60 Options: 0 - 360 | 8875 9811 9841 9851 9861 9871 | Set the timeout period for the phone to automatically power off after the
                  time specified in the Working Hours End field. If you want
                  the phone to enter Deep Sleep Mode immediately after working hours, set it to
                  0. You can configure this parameter in the phone configuration XML file
                  (cfg.xml) by entering a string in this
                  format: <Phone_Off_Time_After_Working_Hour_End__mins_
                  ua="na">12</Phone_Off_Time_After_Working_Hour_End__mins_> The smart power feature uses this setting to control the
                    phone's power mode only when Smart Power Override is
                    disabled. |
| Random Early Wakeup (mins) | Default: 60 Options: 0 - 60 | 8875 9811 9841 9851 9861 9871 | Set the time interval for the phone to wake up before its regular schedule.
                  It helps distribute the load of connection and registration requests when a large
                  number of phones power on simultaneously. The actual wakeup time is
                  calculated as: Working Hours Start - Phone On Time Before Working Hour Start -
                  Random Early Wakeup Example If the following values are set
                  as: Working Hours Start: 8:00 am Phone On Time Before Working Hour Start: 30 mins Random Early Wakeup: 60 mins the phone can randomly wake from Deep Sleep Mode at anytime between 6:30 am
                  7:30 am. You can configure this parameter in the phone configuration XML
                  file (cfg.xml) by entering a string in this
                  format: <Random_Early_Wakeup__mins_
                  ua="na">60</Random_Early_Wakeup__mins_> The smart power feature uses this setting to control the
                    phone's power mode only when Smart Power Override is
                    disabled. |
| Random Delay to Sleep (mins) | Default: 10 Options: 0 - 10 | 8875 9811 9841 9851 9861 9871 | Set a time interval for the phone to enter Deep Sleep Mode after its
                  scheduled power-off time. The actual sleep time is calculated as: Working
                  Hours End + Phone Off Time After Working Hour End + Random Delay to
                    Sleep Example If the following values are set: Working Hours End: 5:00 pm Phone Off Time After Working Hour End: 30 mins Random Delay to Sleep: 10 mins the phone can randomly power off at anytime between 5:30 pm and 5:40
                  pm. You can configure this parameter in the phone configuration XML file
                  (cfg.xml) by entering a string in this
                  format: <Random_Delay_to_sleep_mins_
                  ua="na">10</Random_Delay_to_sleep_mins_mins_> The smart power feature uses this setting to control the
                    phone's power mode only when Smart Power Override is
                    disabled. |
| Idle Timeout (mins) (for Deep Sleep Mode) | Default: 30 Options: 1 - 60 | 8875 9811 9841 9851 9861 9871 | This setting applies to the following two scenarios: Before the phone enters a scheduled Deep Sleep Mode Ten minutes
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
                      restart in 20 minutes after the activity completes. The following notes apply to both scenarios described above. If a user interacts with the phone during the countdown period, such as
                          answering or declining calls or pressing keys, the phone will not enter
                          Deep Sleep Mode for the rest of the day. The smart power feature uses this setting to control the
                    phone's power mode only when Smart Power Override is
                    disabled. You can configure this parameter in the phone configuration XML file
                  (cfg.xml) by entering a string in this format: <Idle_Timeout__mins_
                  ua="na">52</Idle_Timeout__mins_> |
| Outside Office Hours Display
                  Off |
| Handset LED in Display Off Mode | Default: Disabled Options: Enabled, Disabled | 8875 | Controls whether the handset LED lights up to notify users of phone statuses in Display Off mode. When disabled, the handset LED is off. When enabled, its indication behavior is the same as when the display is on. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Handset_LED_In_Display_Off_Mode ua="na">Disabled</Handset_LED_In_Display_Off_Mode> This setting works only when the LED Indicator In Display Off Mode parameter is set to Enabled. |
| Line Key and Top 360 LED in Display Off Mode | Default: Disabled Options: Disabled, Enable Line Key LED, Enable Top 360 LED, Enable both Line Key and Top 360 LED | 9841 9851 9861 9871 | Controls whether the LEDs light up to notify users of phone statuses in Display Off mode. When disabled, both the Line Key LEDs on phone and Key Expansion Module (KEM) and Top 360 LEDs are off. When the corresponding LED is enabled, its indication behavior is the same as when the display is on. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Line_Key_and_Top_360_LED_In_Display_Off_Mode ua="na">Disabled</Line_Key_and_Top_360_LED_In_Display_Off_Mode> This setting works only when the LED Indicator In Display Off Mode parameter is set to Enabled. |
| LED Indicator In Display Off Mode | Default: Enabled Options: Enabled, Disabled | 8875 9811 9841 9851 9861 9871 | This setting determines whether to turn off the Front Arc LED on 9800 Series
                  or the Home button LED on 8875 when the phone enters Display Off Mode, both during
                  or outside office hours. By default (Enabled), the LED remains illuminated after
                  the phone enters Display Off Mode. When set to disabled, the LED is off in Display
                  Off Mode. You can configure this parameter in the phone configuration XML
                  file (cfg.xml) by entering a string in this
                  format: <LED_Indicator_In_Display_Off_Mode
                  ua="na">Enabled</LED_Indicator_In_Display_Off_Mode> |
| Idle Timeout (mins) (for Display Off Mode outside
                  office hours) | Default: 5 Options: 1 - 60 | 9811 9841 9851 9861 9871 | This field is available in the Outside Office Hours Display
                    Off section. Set the timeout period in minutes for the phone
                  to automatically turn off the screen after being awakened during Display Off
                  Mode. You can configure this parameter in the phone configuration XML file
                  (cfg.xml) by entering a string in this
                  format: <Display_Off_Idle_Timeout__mins_
                  ua="na">5</Display_Off_Idle_Timeout__mins_> |
| Outside Office Hours Smart
                  Power Supported only on phones powered by Power over
                  Ethernet (PoE). |
| Smart Power Enabled | Default: False Options: False, Non-work Day Only, All Days | 8875 9811 9841 9851 9861 9871 | Enable or disable the smart power feature. By default, smart power is disabled.
                    Set it to Non-work Day Only or All Days as needed to enable this feature. The setting is effective only when a valid domain and security secret are
                    provided. You can configure this parameter in the phone configuration XML file
                  (cfg.xml) by entering a string in this format: <SmartPower_Enabled
                  ua="na">All Days</SmartPower_Enabled> |
| Domain | Default: Empty | 8875 9811 9841 9851 9861 9871 | The smart power domain that the phone belongs to. Max 128 characters. You can configure this parameter in the phone configuration XML file
                  (cfg.xml) by entering a string in this format: <SmartPower_Domain
                  ua="na">5</SmartPower_Domain> |
| Secret | Default: Empty | 8875 9811 9841 9851 9861 9871 | The password (shared secret) used for communication between the phone and the
                    switch. Max 128 characters. You can configure this parameter in the phone configuration XML file
                  (cfg.xml) by entering a string in this format: <SmartPower_Secret
                  ua="na">*******</SmartPower_Secret> |
| Smart Power Override | Default: No Options: Yes, No | 8875 9811 9841 9851 9861 9871 | This setting determines whether the switch can override the phone's
                    power-saving configuration set by the calling system. No : The phone follows the power-saving configuration
                      set by its calling system. Yes : The switch fully controls the phone’s power
                      modes, overriding the configuration set by the phone's calling system. You can configure this parameter in the phone configuration XML file
                  (cfg.xml) by entering a string in this format: <SmartPower_Override
                  ua="na">No</SmartPower_Override> |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Ext [n] (where [n] is the extension number). |
| 3 | In the Call Feature Settings section, set Enable
            Broadsoft Hoteling parameter to Yes . You can configure this parameter in the phone configuration XML file (cfg.xml) by
            entering a string in this format: <Enable_Broadsoft_Hoteling_1_ua="na">Yes</Enable_Broadsoft_Hoteling_1> Options: Yes and No Default: No |
| 4 | Set the amount of time (in seconds) in Hoteling Subscription
            Expires paramter that specifies how often the phone sends the SUBSCRIBE
          message. You can configure this parameter in the phone configuration XML file (cfg.xml) by
            entering a string in this format: <Hoteling_Subscription_Expires_1_ua="na">3600</Hoteling_Subscription_Expires_1> Valid values: An integer from 10 through 86400 Default: 3600 When the parameter is set to 0, the default 3600 is used. |
| 5 | Click Submit All Changes . |

| Feature Key Sync | XSI DND Enabled | XSI CFWD Enabled | DND Sync | CFWD Sync |
|---|---|---|---|---|
| Yes | Yes | Yes | Yes (SIP) | Yes (SIP) |
| Yes | No | No | Yes (SIP) | Yes (SIP) |
| Yes | No | Yes | Yes (SIP) | Yes (SIP) |
| No | Yes | Yes | Yes (HTTP) | Yes (HTTP) |
| No | No | Yes | No | Yes (HTTP) |
| No | Yes | No | Yes (HTTP) | No |
| No | No | No | No | No |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Ext [n] (where [n] is the extension number). |
| 3 | In the Call Feature Settings section, set the Feature Key Sync field to Yes . |
| 4 | Click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Ext [n] (where [n] is the extension number). |
| 3 | In the XSI Line Service section, set the CFWD Enable parameter to Yes . You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <CFWD_Enable_1_ ua="na">Yes</CFWD_Enable_1_> Options: Yes and No Default: No |
| 4 | Click Submit All Changes . |

| 1 | Select Voice > Ext [n] (where [n] is the extension number). |
|---|---|
| 2 | In the XSI Line Service section, set the DND Enable parameter to Yes . You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <DND_Enable_1_ ua="na">Yes</DND_Enable_1_> Options: Yes and No Default: No |
| 3 | Click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | To enable conference service for the phone do the following: Select Voice > Phone . Under Supplementary Services , choose Yes for the Conference Serv parameter. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Conference_Serv ua="na">Yes</Conference_Serv> Options: Yes and No Default: Yes |
| 3 | Specify the conference bridge URL for your desired line: Select Voice > Ext(n) Enter the Conference Bridge URL in this format: user@IPaddress:port |
| 4 | Click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | In the Webex section, set the field Calendar Enable . Set Yes or No to enable or disable the Webex calendar service on the phone. Options: Yes\|No; Default: Yes You can also configure the parameters in the configuration file (cfg.xml) by entering the strings in this format: <Webex_Calendar_Enable ua="na">Yes</Webex_Calendar_Enable> |
| 4 | Click Submit All Changes . |

| Recording Mode in Server | Recording Softkeys Available on the Phone |
|---|---|
| Always | No softkeys available. Your user can't control recording from the phone. Recording starts automatically
                  when a call is connected. |
| Always with Pause/Resume | PauseRec ResRec When call is connected, user can pause the recording and resume the
                  recording. |
| On Demand | Record PauseRec ResRec When a call is connected, recording starts automatically but the recording is not
                  saved until the user presses the Record softkey. Your user
                  sees a message when recording state changes. |
| On Demand with User Initiated Start | Record PauseRec StopRec ResRec The recording only starts when your user presses the Record softkey. Your user sees a message when recording state
                  changes. |
| Never | No recording softkeys are available, hence user will not be able to record
                  calls. |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | In the Supplementary Services section, click Yes or click No to enable or disable the Call Recording Serv parameter. You can configure this parameter in the phone configuration XML file (cfg.xml) by
            entering a string in this format: <Call_Recording_Serv
            ua="na">Yes</Call_Recording_Serv> Options: Yes and No Default:
            No |
| 4 | Click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | Go to the Multiple Paging Group Parameters section. |
| 4 | Enter multicast paging scripts as defined in the following table of Parameters for multiple paging group . |
| 5 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Group 1 Paging Script – Group 10 Paging Script | Enter a string to configure the phone to listen for and initiate multicast paging. You can add a phone to up to 10 paging groups. Enter the script in this format: Multicast paging : pggrp=<multicast-address>:<port>;<name=group_name>;<num=multicast_number>; <listen=boolean_value>;<pri=priority_level>;<codec=codec_name>; Example script : pggrp=224.168.168.168:34560;name=Group_1;num=800;listen=yes;pri=1; Multicast paging with XML application support : pggrp=<multicast-address>:<port>;<name=group_name>;<num=multicast_number>; <listen=boolean_value>;<pri=priority_level>;<codec=codec_name>;<xmlapp=boolean_value>;<timeout=seconds> Example script : pggrp=224.168.168.168:34560;name=Group_1;num=800;listen=yes;pri=1;xmlap- p=yes;timeout=3600; Multicast IP address (multicast-address) and port (port)—Enter the multicast IP address and the port specified on your paging server. The port number must be unique for each group and an even number within 1000 and 65534. Make sure that you set the same multicast IP address and port for all the phones within a paging group. Otherwise, the phones can't receive paging. Paging group name (name)—Optionally enter the name of the paging group. The name helps you identify the paging group the phone is in when you have multiple paging groups. Multicast number (num)—Specify the number for the phone to listen for multicast paging and initiate a multicast paging session. Assign the same multicast number to all the phones within the group. The number must comply to the dial plan specified for the line to initiate a multicast. Listen status (listen)—Specify whether the phone listens for paging from this group. Set this parameter to yes to make the phone listen for the paging. Otherwise, set it to no , or don't include this parameter in the script. Priority (pri)—Specify priority between paging and phone call. If you don't specify the priority or don't include this parameter in the script, the phone uses priority 1 . The four priority levels are: 0: Paging takes precedent over phone call. When the phone is on an active call, an incoming paging places the active call on hold. The call resumes when the paging ends. 1 : When the phone receives an incoming paging on an active call, the user hears the mix of the paging and the call. 2 : The user is alerted with the paging tone when receiving an incoming paging on an active line. The incoming paging isn't answered unless the active call is put on hold or ends. 3 : The phone ignores the incoming paging without any alert when the phone is on an active call. Audio codec (codec)—Optionally specify the audio codec for the multicast paging to use. The supported codecs are G711a, G711u, G722, and G729. If you don't specify the codec or don't include the codec parameter in the script, the phone uses G711u codec. XML application (xmlapp)—Specify whether the phone contacts the XML application server when it receives audio over paging group. Set this parameter to Yes to make the phone invoke the XML application from multicast paging. Otherwise, set it to no . Make sure that the parameter XML Application Service URL in XML services is configured, see XML services for details. In the XML URL, the macro MCASTADDR must be configured to distinguish it from the normal multicast paging. For example, http(s)://<url>?mcast=$MCASTADDR Timeout—Optionally specify the timeout (in seconds) for the XML application messages that display on the phone screen. If the parameter is not configured, the XML application messages disappear along with the paging. Typically, the XML application ends after the timeout is reached, in regardless of the paging call. If the paging call is still active, only the XML application ends. A new paging closes the XML application of the last paging, if the XML application is not closed when the last paging ended. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Group_1_Paging_Script ua="na">pggrp=224.168.168.168:34560;name=Group_1; num=800;listen=yes;pri=1;codec=g722;xmlap- p=yes;timeout=3600;</Group_1_Paging_Script> Default: Empty |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > User . |
| 3 | In the Supplementary Services section, choose Yes for the Auto Answer Page parameter. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Auto_Answer_Page ua="na">Yes</Auto_Answer_Page> Options: Yes and No Default: Yes |
| 4 | Click Submit All Changes . |

| Image | Supported format (Unified CM) | Recommended dimensions (pixels) | Description |
|---|---|---|---|
| Logo | PNG | Cisco Desk Phone 9851: 190x125 Cisco Desk Phone 9861: 380x250 Cisco Desk Phone 9871: 494x325 / 418x275 Cisco Video Phone 8875: 380x250 | Images that don't match the recommended dimensions will be scaled
                  proportionally. You don't need to create a separate thumbnail image for the
                  logo. The system automatically scales the logo image to fit the dimensions of the
                  thumbnail. |
| Wallpaper | Cisco Desk Phone 9851: 480x240 Cisco Desk Phone 9861: 800x480 Cisco Desk Phone 9871: 1280x720 Cisco Desk Phone 9800 Key Expansion Module: 480x800 Cisco Video Phone 8875: 1024x600 | Images that don't match the recommended dimensions may be scaled to fit the
                phone screen, which may cause the image to become distorted. |
| Wallpaper thumbnail | Cisco Desk Phone 9851: 100x56 Cisco Desk Phone 9861: 150x90 Cisco Desk Phone 9871: 228x128 Cisco Video Phone 8875: 180x100 | Images that don't match the recommended dimensions may cause certain issues on
                the phone. |

| Phone Model | Maximum size per image | Maximum number of images | Limit size |
|---|---|---|---|
| Cisco Desk Phone 9851 | 250KB | 10 | 250KB x 10 |
| Cisco Desk Phone 9861 | 1MB | 20 | 1MB x 20 |
| Cisco Desk Phone 9871 | 1MB | 20 | 1MB x 20 |
| Cisco Video Phone 8875 | 1MB | 20 | 1MB x 20 |

| 1 | Choose your desired logo and wallpaper images. |
|---|---|
| 2 | Format the images to meet the required specifications as described in the table above. |
| 3 | Rename the wallpaper image files in this format: For phone wallpaper and KEM wallpaper images, use wallpaper-xxx.png .
              Replace xxx with your desired name. For example, wallpaper-blue.png , wallpaper-darkgreen.png . For phone wallpaper thumbnail images, use thumbnail-xxx.png . Replace xxx with your desired name. For example, thumbnail-blue.png , thumbnail-darkgreen.png . The system cannot utilize wallpaper files that are named using different patterns. However, for the logo file, you have the flexibility to name it as per your requirements. Make sure that the phone wallpaper and KEM wallpaper have the same filename. Otherwise, the system will fail to load the KEM wallpaper and use the system default wallpaper for KEM. For the xxx in the filename, do not use special characters. Only use letters and numbers. Thumbnail images for logo and KEM wallpapers are not required. |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > User . |
| 3 | Navigate to the Screen section and configure the following parameters to customize the phone screen. Parameter Default Description Appearance Default: Violet Dark Options: Cyan Dark, Purple Dark, Blue Dark, Violet Dark, Blue Light, Violet Light, CustWallpaper <n> Selects the wallpaper for the phone's home screen and the color theme for its user interface. To select a custom wallpaper from the list, make sure that the relevant parameter Custom Wallpaper Download URL [n] ( n represents the sequence number) is configured correctly. The phone user can change the setting in the phone's settings menu. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Appearance ua="na">CustWallpaper 1</Appearance> Custom Wallpaper Download URL n (1 – 20) Empty Specifies the download URL of the custom wallpaper. The scheme can be HTTP, HTTPs, or TFTP. Enter the string in this format: serv=<URL_Address>;image= <Wallpaper_Filename> ;[thumbnail= <Thumbnail_Filename> ;][kem= <KEM_Wallpaper_Filename> ;][theme= <light/dark> ;] Where: serv : The URL address of the server where the image files are stored. To remove the wallpapers, just leave the field empty. image : The custom wallpaper image that will display on the phone screen. thumbnail : The thumbnail of the specified image. If the field isn't configured or the phone fails to fetch the image, the phone will display a dark or light image instead. kem : The custom wallpaper image that will display on the KEM screen. If the field isn't configured or the phone fails to fetch the image, then the KEM will use Violet Light or Violet Dark as the custom wallpaper. theme : The default theme of the specified images. If the field isn't configured or is configured incorrectly, the theme will be light. Example 1: serv=http://10.74.51.12/wallpaper/;image=wallpaper-sun.png;thumbnail=thumbnail-sun.png;kem=kem-wallpaper-sun.png;theme=dark; Example 2: The example shows that only the image and theme are configured in the string. The image of thumbnail will be a dark image, and the custom wallpaper of KEM will be Violet Dark. serv=http://10.74.51.12/wallpaper/;image=wallpaper-sun.png;theme=dark; Example 3: You can also add a subpath for the "image", "thumbnail", and "kem": serv=http://10.74.51.12/wallpaper/;image= <Wallpaper_Subpath>/ wallpaper-sun.png;thumbnail= <Thumbnail_Subpath>/ thumbnail-sun.png;kem= <KEM_Subpath>/ kem-wallpaper-sun.png;theme=dark; The maximum number of the custom wallpapers on Cisco Desk Phone 9851 is limited to 10. For other models (such as, 9861/9871/8875), the maximum number is 20. To remove the custom wallpaper, clear the download URL and leave the parameter empty. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Custom_Wallpaper_Download_URL_1 ua="na">serv=http://10.74.51.12/wallpaper/;image=wallpaper-sun.png;thumbnail=thumbnail-sun.png;kem=kem-wallpaper-sun.png;theme=dark;</Custom_Wallpaper_Download_URL_1> Logo Enable No Options: Yes, No Enables or disables the appearance of the logo on the phone home screen. If enabled, the date and time on the home screen will be replaced by the specified logo. Before the parameter is set to Yes , make sure that the relevant parameter Logo URL is configured correctly. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Logo_Enable ua="na">Yes</Logo_Enable> Logo URL Empty Specifies the download URL of the logo that will be displayed on the phone home screen. To remove the specified logo, make sure to leave the parameter empty. Only one logo can be applied for the phones. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Logo_URL ua="na">http://10.74.51.12/mylogo/logo.png</Logo_URL> | Parameter | Default | Description | Appearance | Default: Violet Dark Options: Cyan Dark, Purple Dark, Blue Dark, Violet Dark, Blue Light, Violet Light, CustWallpaper <n> | Selects the wallpaper for the phone's home screen and the color theme for its user interface. To select a custom wallpaper from the list, make sure that the relevant parameter Custom Wallpaper Download URL [n] ( n represents the sequence number) is configured correctly. The phone user can change the setting in the phone's settings menu. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Appearance ua="na">CustWallpaper 1</Appearance> | Custom Wallpaper Download URL n (1 – 20) | Empty | Specifies the download URL of the custom wallpaper. The scheme can be HTTP, HTTPs, or TFTP. Enter the string in this format: serv=<URL_Address>;image= <Wallpaper_Filename> ;[thumbnail= <Thumbnail_Filename> ;][kem= <KEM_Wallpaper_Filename> ;][theme= <light/dark> ;] Where: serv : The URL address of the server where the image files are stored. To remove the wallpapers, just leave the field empty. image : The custom wallpaper image that will display on the phone screen. thumbnail : The thumbnail of the specified image. If the field isn't configured or the phone fails to fetch the image, the phone will display a dark or light image instead. kem : The custom wallpaper image that will display on the KEM screen. If the field isn't configured or the phone fails to fetch the image, then the KEM will use Violet Light or Violet Dark as the custom wallpaper. theme : The default theme of the specified images. If the field isn't configured or is configured incorrectly, the theme will be light. Example 1: serv=http://10.74.51.12/wallpaper/;image=wallpaper-sun.png;thumbnail=thumbnail-sun.png;kem=kem-wallpaper-sun.png;theme=dark; Example 2: The example shows that only the image and theme are configured in the string. The image of thumbnail will be a dark image, and the custom wallpaper of KEM will be Violet Dark. serv=http://10.74.51.12/wallpaper/;image=wallpaper-sun.png;theme=dark; Example 3: You can also add a subpath for the "image", "thumbnail", and "kem": serv=http://10.74.51.12/wallpaper/;image= <Wallpaper_Subpath>/ wallpaper-sun.png;thumbnail= <Thumbnail_Subpath>/ thumbnail-sun.png;kem= <KEM_Subpath>/ kem-wallpaper-sun.png;theme=dark; The maximum number of the custom wallpapers on Cisco Desk Phone 9851 is limited to 10. For other models (such as, 9861/9871/8875), the maximum number is 20. To remove the custom wallpaper, clear the download URL and leave the parameter empty. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Custom_Wallpaper_Download_URL_1 ua="na">serv=http://10.74.51.12/wallpaper/;image=wallpaper-sun.png;thumbnail=thumbnail-sun.png;kem=kem-wallpaper-sun.png;theme=dark;</Custom_Wallpaper_Download_URL_1> | Logo Enable | No Options: Yes, No | Enables or disables the appearance of the logo on the phone home screen. If enabled, the date and time on the home screen will be replaced by the specified logo. Before the parameter is set to Yes , make sure that the relevant parameter Logo URL is configured correctly. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Logo_Enable ua="na">Yes</Logo_Enable> | Logo URL | Empty | Specifies the download URL of the logo that will be displayed on the phone home screen. To remove the specified logo, make sure to leave the parameter empty. Only one logo can be applied for the phones. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Logo_URL ua="na">http://10.74.51.12/mylogo/logo.png</Logo_URL> |
| Parameter | Default | Description |
| Appearance | Default: Violet Dark Options: Cyan Dark, Purple Dark, Blue Dark, Violet Dark, Blue Light, Violet Light, CustWallpaper <n> | Selects the wallpaper for the phone's home screen and the color theme for its user interface. To select a custom wallpaper from the list, make sure that the relevant parameter Custom Wallpaper Download URL [n] ( n represents the sequence number) is configured correctly. The phone user can change the setting in the phone's settings menu. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Appearance ua="na">CustWallpaper 1</Appearance> |
| Custom Wallpaper Download URL n (1 – 20) | Empty | Specifies the download URL of the custom wallpaper. The scheme can be HTTP, HTTPs, or TFTP. Enter the string in this format: serv=<URL_Address>;image= <Wallpaper_Filename> ;[thumbnail= <Thumbnail_Filename> ;][kem= <KEM_Wallpaper_Filename> ;][theme= <light/dark> ;] Where: serv : The URL address of the server where the image files are stored. To remove the wallpapers, just leave the field empty. image : The custom wallpaper image that will display on the phone screen. thumbnail : The thumbnail of the specified image. If the field isn't configured or the phone fails to fetch the image, the phone will display a dark or light image instead. kem : The custom wallpaper image that will display on the KEM screen. If the field isn't configured or the phone fails to fetch the image, then the KEM will use Violet Light or Violet Dark as the custom wallpaper. theme : The default theme of the specified images. If the field isn't configured or is configured incorrectly, the theme will be light. Example 1: serv=http://10.74.51.12/wallpaper/;image=wallpaper-sun.png;thumbnail=thumbnail-sun.png;kem=kem-wallpaper-sun.png;theme=dark; Example 2: The example shows that only the image and theme are configured in the string. The image of thumbnail will be a dark image, and the custom wallpaper of KEM will be Violet Dark. serv=http://10.74.51.12/wallpaper/;image=wallpaper-sun.png;theme=dark; Example 3: You can also add a subpath for the "image", "thumbnail", and "kem": serv=http://10.74.51.12/wallpaper/;image= <Wallpaper_Subpath>/ wallpaper-sun.png;thumbnail= <Thumbnail_Subpath>/ thumbnail-sun.png;kem= <KEM_Subpath>/ kem-wallpaper-sun.png;theme=dark; The maximum number of the custom wallpapers on Cisco Desk Phone 9851 is limited to 10. For other models (such as, 9861/9871/8875), the maximum number is 20. To remove the custom wallpaper, clear the download URL and leave the parameter empty. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Custom_Wallpaper_Download_URL_1 ua="na">serv=http://10.74.51.12/wallpaper/;image=wallpaper-sun.png;thumbnail=thumbnail-sun.png;kem=kem-wallpaper-sun.png;theme=dark;</Custom_Wallpaper_Download_URL_1> |
| Logo Enable | No Options: Yes, No | Enables or disables the appearance of the logo on the phone home screen. If enabled, the date and time on the home screen will be replaced by the specified logo. Before the parameter is set to Yes , make sure that the relevant parameter Logo URL is configured correctly. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Logo_Enable ua="na">Yes</Logo_Enable> |
| Logo URL | Empty | Specifies the download URL of the logo that will be displayed on the phone home screen. To remove the specified logo, make sure to leave the parameter empty. Only one logo can be applied for the phones. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Logo_URL ua="na">http://10.74.51.12/mylogo/logo.png</Logo_URL> |
| 4 | Click Submit All Changes . |
| 5 | (Optional) To check the download status of the images, select Info > Download Status , and then navigate to the Screen Status section. |

| Parameter | Default | Description |
|---|---|---|
| Appearance | Default: Violet Dark Options: Cyan Dark, Purple Dark, Blue Dark, Violet Dark, Blue Light, Violet Light, CustWallpaper <n> | Selects the wallpaper for the phone's home screen and the color theme for its user interface. To select a custom wallpaper from the list, make sure that the relevant parameter Custom Wallpaper Download URL [n] ( n represents the sequence number) is configured correctly. The phone user can change the setting in the phone's settings menu. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Appearance ua="na">CustWallpaper 1</Appearance> |
| Custom Wallpaper Download URL n (1 – 20) | Empty | Specifies the download URL of the custom wallpaper. The scheme can be HTTP, HTTPs, or TFTP. Enter the string in this format: serv=<URL_Address>;image= <Wallpaper_Filename> ;[thumbnail= <Thumbnail_Filename> ;][kem= <KEM_Wallpaper_Filename> ;][theme= <light/dark> ;] Where: serv : The URL address of the server where the image files are stored. To remove the wallpapers, just leave the field empty. image : The custom wallpaper image that will display on the phone screen. thumbnail : The thumbnail of the specified image. If the field isn't configured or the phone fails to fetch the image, the phone will display a dark or light image instead. kem : The custom wallpaper image that will display on the KEM screen. If the field isn't configured or the phone fails to fetch the image, then the KEM will use Violet Light or Violet Dark as the custom wallpaper. theme : The default theme of the specified images. If the field isn't configured or is configured incorrectly, the theme will be light. Example 1: serv=http://10.74.51.12/wallpaper/;image=wallpaper-sun.png;thumbnail=thumbnail-sun.png;kem=kem-wallpaper-sun.png;theme=dark; Example 2: The example shows that only the image and theme are configured in the string. The image of thumbnail will be a dark image, and the custom wallpaper of KEM will be Violet Dark. serv=http://10.74.51.12/wallpaper/;image=wallpaper-sun.png;theme=dark; Example 3: You can also add a subpath for the "image", "thumbnail", and "kem": serv=http://10.74.51.12/wallpaper/;image= <Wallpaper_Subpath>/ wallpaper-sun.png;thumbnail= <Thumbnail_Subpath>/ thumbnail-sun.png;kem= <KEM_Subpath>/ kem-wallpaper-sun.png;theme=dark; The maximum number of the custom wallpapers on Cisco Desk Phone 9851 is limited to 10. For other models (such as, 9861/9871/8875), the maximum number is 20. To remove the custom wallpaper, clear the download URL and leave the parameter empty. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Custom_Wallpaper_Download_URL_1 ua="na">serv=http://10.74.51.12/wallpaper/;image=wallpaper-sun.png;thumbnail=thumbnail-sun.png;kem=kem-wallpaper-sun.png;theme=dark;</Custom_Wallpaper_Download_URL_1> |
| Logo Enable | No Options: Yes, No | Enables or disables the appearance of the logo on the phone home screen. If enabled, the date and time on the home screen will be replaced by the specified logo. Before the parameter is set to Yes , make sure that the relevant parameter Logo URL is configured correctly. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Logo_Enable ua="na">Yes</Logo_Enable> |
| Logo URL | Empty | Specifies the download URL of the logo that will be displayed on the phone home screen. To remove the specified logo, make sure to leave the parameter empty. Only one logo can be applied for the phones. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Logo_URL ua="na">http://10.74.51.12/mylogo/logo.png</Logo_URL> |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > User . |
| 3 | In the Supplementary Services section, select Yes for the parameter Auto Collapse Into Line Key . To disable the feature, select No . You can also configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Auto_Collapse_Into_Line_Key ua="rw">Yes</Auto_Collapse_Into_Line_Key> Default: No . |
| 4 | Click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Click Voice > Phone . |
| 3 | In the Menu Customization section, set the desired menu items to
          Show or Hide. The availability of menu items may vary by phone model. If all the child items are hidden, the parent menu is also hidden. You can also use the configuration XML file (cfg.xml) to customize the Settings menu. See the following example: |
| 4 | Click Submit All Changes to apply the changes. |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Click Voice > Phone . |
| 3 | In the Miscellaneous Line Key Settings section, set the Always Use Multi-line Mode filed to Enabled . You can also use the configuration XML file (cfg.xml) to customize the Settings menu.
            See the following example: <Always_Use_Multi-line_Mode ua="na">Disabled</Always_Use_Multi-line_Mode> |
| 4 | Click Submit All Changes to apply the changes. |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > System . |
| 3 | In the System Configuration section, and configure the following
          parameters: Enable Web Server : Set this field to Yes . Enable Protocol : Choose the protocol to use — Http or Https — based on your
                server’s configuration. Web Server Port : Specify 443 as the
                port number that the web server will use for incoming connections. You can also use the configuration XML file (cfg.xml) to customize the Settings menu.
            See the following
            example: <Enable_Web_Server ua="na">Yes</Enable_Web_Server>
<Enable_Protocol ua="na">Https</Enable_Protocol>
<!-- available options: Http\|Https -->
<Enable_Direct_Action_Url ua="na">Yes</Enable_Direct_Action_Url>
<Web_Server_Port ua="na">443</Web_Server_Port> |
| 4 | Provide the xAPI administrator credentials in the phone configuration file
          (cfg.xml). Only authorized administrators can remotely manage phones using xAPIs. Enter the
            username and password in the following format: <xAPI_Admin_User_Name>admin_username</xAPI_Admin_User_Name>
<xAPI_Admin_Password>admin_password</xAPI_Admin_Password> |
| 5 | When done, click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Ext [n] . |
| 3 | In the Call Feature
            Settings section, select a ringtone in the Default
            Ring drop-down list. If No Ring is selected, the phone doesn't ring for incoming
            calls on that line. You can also configure this parameter in the configuration file (cfg.xml) by entering a
            string in this format: Example of using a built-in ringtone: <Default_Ring_3_
              ua="rw">2</Default_Ring_3_> Example of using a custom ringtone: <Default_Ring_3_ ua="rw">Custom
              1</Default_Ring_3_> When configuring ringtone using the configuration file, refer to the Ringtone list for the ringtone mapping. If
            you assign an unconfigured custom ringtone to a line, the line uses the default built-in
            ringtone ( 1 ). For instructions on configuring custom ringtones,
            see Configure custom ringtones . |
| 4 | Click Submit All
            Changes . |

| Cadence option | Pattern definition | Timing (seconds) |
|---|---|---|
| c=1 | 60(2/4) | 2.0 ON / 4.0 OFF |
| c=2 | 60(.3/.2,1/.2,.3/4) | 0.3 ON / 0.2 OFF, 1.0 ON / 0.2 OFF, 0.3 ON / 4.0 OFF |
| c=3 | 60(.8/.4,.8/4) | 0.8 ON / 0.4 OFF, 0.8 ON / 4.0 OFF |
| c=4 | 60(.4/.2,.3/.2,.8/4) | 0.4 ON / 0.2 OFF, 0.3 ON / 0.2 OFF, 0.8 ON / 4.0 OFF |
| c=5 | 60(.2/.2,.2/.2,.2/.2,1/4) | 0.2 ON / 0.2 OFF, 0.2 ON / 0.2 OFF, 0.2 ON / 0.2 OFF, 1.0 ON / 4.0
                    OFF |
| c=6 | 60(.2/.4,.2/.4,.2/4) | 0.2 ON / 0.4 OFF, 0.2 ON / 0.4 OFF, 0.2 ON / 4.0 OFF |
| c=7 | 60(4.5/4) | 4.5 ON / 4.0 OFF |
| c=8 | 60(0.25/9.75) | 0.25 ON / 9.75 OFF |
| c=9 | 60(.4/.2,.4/2) | 0.4 ON / 0.2 OFF, 0.4 ON / 2.0 OFF |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | In the Ringtone section, change the cadence of the ringtones and change the Silent Ring
            Duration setting, if needed. Silent Ring Duration controls the duration of the silent ring. For example, if the
            parameter is set to 20 seconds, the phone plays the silent ring for 20 seconds then
            sends 480 response to INVITE message. You can also configure this parameter in the configuration file (cfg.xml) by entering a
            string in this format: |
| 4 | Click Submit All
            Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | In the Ringtone section, enter the URL of your ringtone files in
          the Custom Ringtone Download URL 1 - 10 fields. The supported protocols for these URLs are http, https, and tftp. |
| 4 | Click Submit All
            Changes . The phone reboots automatically to load the custom ringtones. |
| 5 | After the phone boots up, go to Voice > Ext [n] . |
| 6 | In the Call Feature Settings section,
          select the custom ringtone in the Default Ring drop-down
          list. |
| 7 | Click Submit All Changes . You can also configure custom ringtones in the configuration file (cfg.xml) by entering
            a string in this
            format: <Custom_Ringtone_Download_URL_1 ua="na"/>http://10.70.50.200/ringtone/calculation.rwb</Custom_Ringtone_Download_URL_1>
<Default_Ring_3_ ua="rw">Custom 1</Default_Ring_3_> |

## Figuras

![For 9811, 9841,9851, and 9861](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/489001-490000/489180.png)

![for 9871](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/483001-484000/483152.png)

![For 8875](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/489001-490000/489178.png)

![For 9841, 9851, and 9861 phones](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/483001-484000/483151.png)