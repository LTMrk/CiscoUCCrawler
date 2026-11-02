---
doc_id: help-webex-com-en-us-article-1hrvr5-1c2f1a974a
source_url: https://help.webex.com/en-us/article/1hrvr5
retrieved_at: 2026-11-02T13:10:04.395589+00:00
---

The custom options for the Action button on Cisco Desk Phone 9800 Series require specific PhoneOS firmware support. See the following table for details:

## Configure the Action button for emergency calls

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

## Associate the Action button with a custom service

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

## Configure a single trigger for multiple events

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

## Configure multiple triggers

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

## References

### Parameters for the Action button

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

### HTTP Post request for the Action button

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