---
doc_id: help-webex-com-en-us-article-mxwa8f-8029c7a58e
source_url: https://help.webex.com/en-us/article/mxwa8f
retrieved_at: 2026-11-02T13:08:04.387237+00:00
---

## Customize the Action button

The custom options for the Action button on Cisco Desk Phone 9800 Series require specific PhoneOS firmware support. See the following table for details:

Log in to Cisco Unified Communications Manager Administration.

Do one of the following actions as needed:

- To configure all deployed phones, go to System > Enterprise Phone Configuration .

- To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile .

- To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page.

The configuration follows a hierarchical structure:

- Individual device settings take precedence over settings in the common phone
                  profile and enterprise level

- Common phone profile settings override enterprise-level settings

Customize the Action button settings with the following parameters based on your use
          cases.

There are three groups of parameters for the Action button, each corresponding to a
              service with a unique trigger. If a service trigger is specified in multiple groups,
              the settings in Group 1 take priority over those in Group 2 and 3, while Group 2 takes
              priority over Group 3.

Configure the following parameters:

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

Configure the following parameters:

Action Button Function : Select Custom .

Action Button Service Destination :
                Enter the URL of the custom service. The URL must start with http:// or https:// , for example, https://10.11.20.159/path/service.xml .

Action Button Service Name (Optional): Specify a name for the service associated with the trigger. This name
                will be displayed in the on-screen message when the user presses the button,
                indicating which service will be triggered. When no name is specified, Custom
                  service will be used as the display name.

Custom Content Field (Optional): If
                you want to enable the phone to send an HTTP Post request when the Action button is
                pressed, enter the HTTP data such as method, header, and post content, with a
                maximum length of 1024 characters.

For POST script examples and the syntax, see HTTP Post request for the Action button .

Dial Out Delay : Set the timeout
                period, in seconds, for the phone to initiate an event after detecting the trigger.
                The default value is 5 seconds. When set to 0, the event is initiated immediately
                upon trigger detection.

Service Trigger Select a trigger
                from the list: Single Press , Long
                  Press , or Press 3 Times .

Service Secret (Optional): Enter
                the authentication secret, token or password if your custom service requires
                authentication to access it. The entered secret is displayed as a masked string and
                can be referenced using the macro $SS in Custom Content
                  Field and Action Button Service
                Destination .

Set the parameters in each group respectively. See the
              Emergency calls and Custom services sections above.

Configure the following parameters
              to assign multiple events to a trigger:

Action Button Function : Select Custom .

Action Button Service Destination : Enter the phone number
                  to call and the XML service URL in this format:

tel:<phonenumber or SIP URI> +
                  <serviceURL>

The URL must start with http:// or https:// .

Example: tel:1234 + https://10.11.20.159/path/service.xml

Action Button Service Name (Optional): Specify a name for the service associated with the trigger. This name
                will be displayed in the on-screen message when the user presses the button,
                indicating which service will be triggered. When no name is specified, Custom
                  service will be used as the display name.

Custom Content Field (Optional): If
                you want to enable the phone to send an HTTP Post request when the Action button is
                pressed, enter the HTTP data such as method, header, and post content, with a
                maximum length of 1024 characters.

For POST script examples and the syntax, see HTTP Post request for the Action button .

Dial Out Delay : Set the timeout
                period, in seconds, for the phone to initiate an event after detecting the trigger.
                The default value is 5 seconds. When set to 0, the event is initiated immediately
                upon trigger detection.

Service Trigger Select a trigger
                from the list: Single Press , Long
                  Press , or Press 3 Times .

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

For more information about these parameters, see Parameters for the Action
            button .

Select Save .

Select Apply Config .

## References

### Parameters for the Action button

The parameters are available in Enterprise Phone Configuration, Common Phone Profile, and
        individual phone configuration.

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

If you are not allowed to input a URL including ampersand (&), use %26 as a
                    replacement. For example, enter http://1.2.3.4/phone?a=1%26b=2%26c=3 instead of http://1.2.3.4/phone?a=1&b=2&c=3 .

Default: Empty

This setting works only when the Action Button
                        Function is set to Custom .

Enter the HTTP data such as method, header, and post content, with a maximum
                    length of 1024 characters. When configured, the phone sends an HTTP Post request
                    when the Action is pressed.

If the service requires
                  authentication to access, make sure to enter the authentication secret in the Service Secret field. In the HTTP data, use the macro $SS as a reference to Service Secret.

For examples and the syntax, see HTTP Post request for the Action
                    button .

Default: Empty

A service secret can be an authentication secret, token or password. The
                    entered secret is displayed as a masked string and can be referenced using the
                    macro $SS in Custom Content Field and Action Button Service Destination .

Default: Single Press

Options: Single Press, Long Press, Press 3 times

Choose how users can place an emergency call or initiate a custom service using
                    the phone's Action button.

Single Press : Press the Action button to trigger the
                    associated call or service.

Long Press : Press the Action button down for at least 2
                    seconds to trigger the associated call or service.

Press 3 times : Press the Action button three times with
                    intervals of less than 2 seconds between each press to trigger the associated
                    call or service.

Don't repeat a trigger across multiple services, as the parameters with lower
                    priority will not function. The priority order, from highest to lowest, is as
                    follows: Group 1, Group 2, Group 3.

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

### HTTP Post request for the Action button

The Action button on Cisco Desk Phone 9800 Series can be configured to trigger XML applications through HTTP Post requests.

In Custom Content Field , enter your customized request script. You
        can specify either XML or JSON content type and include macros in the request. For example, $SS can be added to the script to retrieve the authentication secret,
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

Cisco Unified Communications Manager (UCM) requires percent encoding for the reserved
          characters in accordance with RFC 3986.

The following script is an example using percent-encoded strings.

```
--method POST
--header %27Content-Type: application/xml%27
--body %27%3cMetaData%3e%3cTrigger%3eTrue%3c/Trigger%3e%3cDescription%3eThis is for HTTP POST XML%3c/Description%3e%3c/MetaData%3e%27
```

| Feature | Required firmware version |
|---|---|
| Emergency call | PhoneOS 3.0.1 and later |
| Custom service | PhoneOS 3.2.1 and later |
| Multiple triggers | PhoneOS 3.3.1 and later |
| HTTP Post | PhoneOS 3.3.1 and later |
| Multiple events on a single trigger | PhoneOS 3.4.1 and later |

| 1 | Log in to Cisco Unified Communications Manager Administration. |
|---|---|
| 2 | Do one of the following actions as needed: To configure all deployed phones, go to System > Enterprise Phone Configuration . To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile . To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page. The configuration follows a hierarchical structure: Individual device settings take precedence over settings in the common phone
                  profile and enterprise level Common phone profile settings override enterprise-level settings |
| 3 | Customize the Action button settings with the following parameters based on your use
          cases. There are three groups of parameters for the Action button, each corresponding to a
              service with a unique trigger. If a service trigger is specified in multiple groups,
              the settings in Group 1 take priority over those in Group 2 and 3, while Group 2 takes
              priority over Group 3. Emergency calls Configure the following parameters: Action Button Function : Select Emergency
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
                volume using the Volume key. Custom services Configure the following parameters: Action Button Function : Select Custom . Action Button Service Destination :
                Enter the URL of the custom service. The URL must start with http:// or https:// , for example, https://10.11.20.159/path/service.xml . Action Button Service Name (Optional): Specify a name for the service associated with the trigger. This name
                will be displayed in the on-screen message when the user presses the button,
                indicating which service will be triggered. When no name is specified, Custom
                  service will be used as the display name. Custom Content Field (Optional): If
                you want to enable the phone to send an HTTP Post request when the Action button is
                pressed, enter the HTTP data such as method, header, and post content, with a
                maximum length of 1024 characters. For POST script examples and the syntax, see HTTP Post request for the Action button . Dial Out Delay : Set the timeout
                period, in seconds, for the phone to initiate an event after detecting the trigger.
                The default value is 5 seconds. When set to 0, the event is initiated immediately
                upon trigger detection. Service Trigger Select a trigger
                from the list: Single Press , Long
                  Press , or Press 3 Times . Service Secret (Optional): Enter
                the authentication secret, token or password if your custom service requires
                authentication to access it. The entered secret is displayed as a masked string and
                can be referenced using the macro $SS in Custom Content
                  Field and Action Button Service
                Destination . Multiple triggers Set the parameters in each group respectively. See the
              Emergency calls and Custom services sections above. A single trigger for multiple events Configure the following parameters
              to assign multiple events to a trigger: Action Button Function : Select Custom . Action Button Service Destination : Enter the phone number
                  to call and the XML service URL in this format: tel:<phonenumber or SIP URI> +
                  <serviceURL> The URL must start with http:// or https:// . Example: tel:1234 + https://10.11.20.159/path/service.xml Action Button Service Name (Optional): Specify a name for the service associated with the trigger. This name
                will be displayed in the on-screen message when the user presses the button,
                indicating which service will be triggered. When no name is specified, Custom
                  service will be used as the display name. Custom Content Field (Optional): If
                you want to enable the phone to send an HTTP Post request when the Action button is
                pressed, enter the HTTP data such as method, header, and post content, with a
                maximum length of 1024 characters. For POST script examples and the syntax, see HTTP Post request for the Action button . Dial Out Delay : Set the timeout
                period, in seconds, for the phone to initiate an event after detecting the trigger.
                The default value is 5 seconds. When set to 0, the event is initiated immediately
                upon trigger detection. Service Trigger Select a trigger
                from the list: Single Press , Long
                  Press , or Press 3 Times . Service Secret (Optional): Enter
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
                volume using the Volume key. For more information about these parameters, see Parameters for the Action
            button . |
| 4 | Select Save . |
| 5 | Select Apply Config . |

| Parameter | Default and options | Description |
|---|---|---|
| Action Button Function 1~3 | Default: Off Options: Off, Emergency Call, Custom | You can configure the button with a specific service. Off : When set to Off, the Action button for single
                      service on the phone will not function. Emergency Call : Users can use the Action button to
                      place an emergency call, if configured. Custom : Users can use the Action button to access the
                      custom service, if configured. When you set the field to Emergency Call or Custom , make sure that you enter the service
                    destination in the Action Button Service Destination field. Or, the phone will display a configuration error. |
| Action Button Service Name 1~3 | Default: Empty | Optionally specify a name for the service associated with the Action button.
                    This name will be displayed in the on-screen message when the user presses the
                    button, indicating which service will be triggered. If you don't specify a name, the default name will be Emergency call, Silent
                    emergency call, or Custom action based on your selection in the Action Button Function field. |
| Action Button Service Destination 1~3 | Default: Empty | Provide the service destination in one of the following formats based on the
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
                      example, tel:1234 . If you are not allowed to input a URL including ampersand (&), use %26 as a
                    replacement. For example, enter http://1.2.3.4/phone?a=1%26b=2%26c=3 instead of http://1.2.3.4/phone?a=1&b=2&c=3 . |
| Custom Content Field 1~3 | Default: Empty | This setting works only when the Action Button
                        Function is set to Custom . Enter the HTTP data such as method, header, and post content, with a maximum
                    length of 1024 characters. When configured, the phone sends an HTTP Post request
                    when the Action is pressed. If the service requires
                  authentication to access, make sure to enter the authentication secret in the Service Secret field. In the HTTP data, use the macro $SS as a reference to Service Secret. For examples and the syntax, see HTTP Post request for the Action
                    button . |
| Service Secret 1~3 | Default: Empty | A service secret can be an authentication secret, token or password. The
                    entered secret is displayed as a masked string and can be referenced using the
                    macro $SS in Custom Content Field and Action Button Service Destination . |
| Service Trigger 1~3 | Default: Single Press Options: Single Press, Long Press, Press 3 times | Choose how users can place an emergency call or initiate a custom service using
                    the phone's Action button. Single Press : Press the Action button to trigger the
                    associated call or service. Long Press : Press the Action button down for at least 2
                    seconds to trigger the associated call or service. Press 3 times : Press the Action button three times with
                    intervals of less than 2 seconds between each press to trigger the associated
                    call or service. Don't repeat a trigger across multiple services, as the parameters with lower
                    priority will not function. The priority order, from highest to lowest, is as
                    follows: Group 1, Group 2, Group 3. |
| Dial Out Delay 1~3 | Default: 5 Options: 0 - 30 | Set the timeout period, in seconds, for the phone to initiate an emergency call
                    or a custom action after the Action button is pressed. Set it to 0 if you prefer the phone to place the call or initiate an event
                    immediately upon detecting the trigger, as specified by a single press, long
                    press, or triple presses on the button. |
| Silent Emergency Call 1~3 | Default: Disabled Options: Enabled, Disabled | Silent emergency call is designed for discreet assistance in dangerous
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

| Character | Percent encoding |
|---|---|
| & | %26 |
| ' | %27 |
| " | %22 |
| < | %3c |
| > | %3e |

| Macro name | Macro expansion |
|---|---|
| #DEVICENAME# | The device name displayed in the calling system. For example,
                SEP845A3EC21288 |
| $SS | Service Secret which presents a masked string in the phone configuration page,
                such as authentication secret, token, or password. |