---
doc_id: help-webex-com-en-us-article-n22c0wy-2379e2a3b4
source_url: https://help.webex.com/en-us/article/n22c0wy
retrieved_at: 2026-11-02T13:07:59.642769+00:00
---

The custom options for the Action button on Cisco Desk Phone 9800 Series require specific PhoneOS firmware support. See the following table for details:

## Configure the Action button for emergency calls

The Action button for emergency calls ensures quick and easy access to critical assistance
        in workspaces.

From the customer view in Control Hub , go to Devices , and then
          select your phone.

Select All configurations .

Navigate to the Phone section and select Action
            Button .

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

During a silent emergency call, the screen on phone 9811 and 9841 will freeze, while the screen on
                phone 9851, 9861, and 9871 will be turned off. All other functions are inaccessible.
                The phone restores normal operation after the recipient ends the call.

Allow Silent
                  Emergency Call Retrieval (Optional): Enable this feature if you allow
                users to press any key to restore normal phone operation while maintaining the
                emergency call. The call audio remains silent unless the user increases the speaker
                volume using the Volume key.

For more details about these parameters, see Parameters for the Action button .

Select Next .

Review your changes and select Apply .

Select Close to close the page.

## Configure the Action button for a custom service

When you associate the Action button with a custom service, the
        phone users can access the service by the designated trigger, such as a single press, long
        press, or triple presses on the button.

From the customer view in Control Hub , go to Devices , and then select your phone.

Select All configurations .

Navigate to the Phone section and select Action Button .

Configure the following parameters to associate the Action button with a custom
          service.

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

For POST script examples and the syntax, see HTTP Post request for the Action
                  button .

Dial Out Delay : Set the timeout
                period, in seconds, for the phone to initiate an event after detecting the trigger.
                The default value is 5 seconds. When set to 0, the event is initiated immediately
                upon trigger detection.

Service Trigger Select a trigger
                from the list: Single Press , Long
                  Press , or Press 3 Times .

For more details about these parameters, see Parameters for the Action button .

Select Next .

Review your changes and select Apply .

Select Close to close the page.

## Configure a single trigger for multiple events

A single trigger for multiple events allows one action on the action button to initiate
        several related processes simultaneously. This feature enhances responsiveness, reduces
        complexity, and ensures seamless workflow execution across applications.

From the customer view in Control Hub , go to Devices , and then
          select your phone.

Select All configurations .

Navigate to the Phone section and select Action
            Button .

Configure the following parameters to enable the Action button to trigger multiple
          events at a time.

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

For POST script examples and the syntax, see HTTP Post request for the Action
                  button .

Dial Out Delay : Set the timeout period, in seconds, for the
                phone to initiate an event after detecting the trigger. The default value is 5
                seconds. When set to 0, the event is initiated immediately upon trigger
                detection.

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

During a silent emergency call, the screen on phone 9811 and 9841 will freeze, while the screen on
                  phone 9851, 9861, and 9871 will be turned off. All other functions are
                  inaccessible. The phone restores normal operation after the recipient ends the
                  call.

Allow Silent
                  Emergency Call Retrieval (Optional): Enable this feature if you allow
                users to press any key to restore normal phone operation while maintaining the
                emergency call. The call audio remains silent unless the user increases the speaker
                volume using the Volume key.

For more details about these parameters, see Parameters for the Action button .

Select Next .

Review your changes and select Apply .

Select Close to close the page.

## Configure multiple triggers

You can configure the Action button to connect to multiple services and assign each service with its own trigger. For example, a long press on the Action button places a call to the designated emergency agent; a single short press on the button post a notification to the phones within the corporation.

From the customer view in Control Hub , go to Devices , and then select your phone.

Select All configurations .

Navigate to the Phone section and select Action Button .

Set Service Trigger to MultiTrigger .

When the MultiTrigger option is selected, only the
                  settings in the Service Trigger MultiTrigger section will
                  be applied, while the settings related to Action button outside that section will
                  be ignored.

Make sure to configure at least one trigger when the MultiTrigger option is selected.

Go to Action Button > Service Trigger MultiTrigger and select your desired trigger from the available options - Single Press , Long Press , and Press 3 times .

Configure the following parameters for your selected trigger:

Action Button Function : Select the service that phone users
                can access via the trigger.

Action Button Service Destination : Enter phone number or the
                URI of the service.

Action Button Service Name (Optional): Specify a name for
                the service associated with the action trigger. This name will be displayed in the
                on-screen message when the user presses the button, indicating which service will be
                triggered. If no name is specified, the default name will be Emergency call, Silent
                emergency call, or Custom action based on your selection in the Action
                  Button Function field.

Custom Content Field (Optional): If
                you want to enable the phone to send an HTTP Post request when the Action button is
                pressed, enter the HTTP data such as method, header, and post content, with a
                maximum length of 1024 characters.

For POST script examples and the syntax, see HTTP Post request for the Action
                  button .

Dial Out Delay : Set the timeout period, in seconds, for the
                phone to initiate an event after detecting the trigger. The default value is 5
                seconds. When set to 0, the event is initiated immediately upon trigger
                detection.

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

This parameter is located at Action Button > Allow Silent Emergency Call Retrieval .

For more details about these parameters, see Parameters for the Action button .

Repeat Step 5 to 6 to configure more triggers.

Select Next .

Review your changes and select Apply .

Select Close to close the page.

## References

### Parameters for the Action button

The parameters for the Action button can be found in the configurations at device,
        location, and organization level.

For more information about how to configure phone settings at location and organization
        level, see Configure Cisco Desk Phone 9800 Series on Control Hub .

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

For more information about a single trigger for multiple events, see Configure a single trigger for multiple events .

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

Optionally specify a name for the service associated with the Action button.
                    This name will be displayed in the on-screen message when the user presses the
                    button, indicating which service will be triggered.

If you don't specify a name, the default name will be Emergency call, Silent
                    emergency call, or Custom action based on your selection in the Action Button Function field.

Default: No

Options: Yes, No

Controls whether users can retrieve phone functionality during a silent
                    emergency call. By default, once a silent emergency call is initiated, the phone
                    locks all functions until the call recipient ends the call.

When this parameter is set to Yes , users can press any
                    key to restore normal phone operation while maintaining the emergency call. The
                    call audio remains silent unless the user increases the volume using the Volume
                    key.

Default: Empty

This setting works only when the Action Button
                        Function is set to Custom .

Enter the HTTP data such as method, header, and post content, with a maximum
                    length of 1024 characters. When configured, the phone sends an HTTP Post request
                    when the Action is pressed.

You can use macros in the HTTP data, such as $MA, $SN.

For POST script examples and the syntax, see HTTP Post request for the Action button .

Default: 5

Options: 0 - 30

Set the timeout period, in seconds, for the phone to initiate an emergency call
                    or a custom action after the Action button is pressed.

Set it to 0 if you prefer the phone to place the call or initiate an event
                    immediately upon detecting the trigger, as specified by a single press, long
                    press, or triple presses on the button.

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
                    button. Go to the Service Trigger MultiTrigger section to
                    select a trigger and configure the specific settings.

For detailed information about multiple triggers, see Configure multiple triggers .

This setting works only when Service Trigger is set to MultiTrigger .

Choose a trigger from the available options to open and configure the
                  settings.

For detailed information about multiple triggers, see Configure multiple triggers .

For details about the MultiTrigger parameters, see Parameters for MultiTrigger .

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

Optionally specify a name for the service associated with the action trigger.
                    This name will be displayed in the on-screen message when the user presses the
                    button, indicating which service will be triggered.

If you don't specify a name, the default name will be Emergency call, Silent
                    emergency call, or Custom action based on your selection in the Action Button Function field.

Default: Empty

This setting works only when the Action Button
                        Function is set to Custom .

Enter the HTTP data such as method, header, and post content, with a maximum
                    length of 1024 characters. When configured, the phone sends an HTTP Post request
                    when the Action is pressed.

You can use macros in the HTTP data, such as $MA, $SN.

For POST script examples and the syntax, see HTTP Post request for the Action
                    button .

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
                        the screen on phone 9851, 9861, and 9871 will be turned off.

The phone locks all
                          functions during a silent emergency call, by default. To allow users to
                          restore normal phone operation while maintaining the silent emergency
                          call, enable the Allow Silent Emergency Call
                            Retrieval feature.

When disabled, the emergency call functions as a two-way call, similar to
                        other outgoing calls.

### HTTP Post request for the Action button

The Action button on Cisco Desk Phone 9800 Series can be configured to trigger XML applications through HTTP Post requests.

In Custom Content Field , enter the request script. You can specify
        either XML or JSON content type and include macros in the request.

The following examples are in XML and JSON:

```
Sample #1: XML
--method POST
--header 'Content-Type: application/xml'
--body '<MetaData><Trigger>True</Trigger><Description>This is for HTTP POST XML</Description></MetaData>' 

Sample #2: JSON
--method POST
--header 'Content-Type: application/json'
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

### Macro variables supported in XML URLs

You can use macro variables in XML URLs. The following macro variables are supported:

User ID—UID1, UID2 to UIDn

Display name—DISPLAYNAME1, DISPLAYNAME2 to DISPLAYNAMEn

Auth ID—AUTHID1, AUTHID2 to AUTHIDn

Proxy—PROXY1, PROXY2 to PROXYn

MAC Address using lowercase hex digits—MA

Product Name—PN

Product Series Number—PSN

Serial Number—SERIAL_NUMBER

$SA through $SD are recognized as arguments to the optional resync URL
                    qualifier, --key.

SWVER

Software version string. For example,

PHONEOS.3-2-1-0104-37

HWVER

Hardware version string. For example, 2.0.1

PRVST

Provisioning State (a numeric string):

-1 = explicit resync request

0 = power-up resync

1 = periodic resync

2 = resync failed, retry attempt

UPGST

Upgrade State (a numeric string):

1 = first upgrade attempt

2 = upgrade failed, retry attempt

UPGERR

Result message (ERR) of previous upgrade attempt; for example http_get failed.

PRVTMR

Seconds since last resync attempt.

UPGTMR

Seconds since last upgrade attempt.

REGTMR1

Seconds since Line 1 lost registration with SIP server.

REGTMR2

Seconds since Line 2 lost registration with SIP server.

UPGCOND

Legacy macro name.

SCHEME

File access scheme, one of TFTP, HTTP, or HTTPS, as obtained after parsing resync or upgrade URL.

SERV

Request target server host name, as obtained after parsing resync or upgrade URL.

SERVIP

Request target server IP address, as obtained after parsing resync or upgrade URL, possibly following DNS lookup.

PORT

Request target UDP/TCP port, as obtained after parsing resync or upgrade URL.

PATH

Request target file path, as obtained after parsing resync or upgrade URL.

ERR

Result message of resync or upgrade attempt. Only useful in generating result syslog messages. The value is preserved in the UPGERR variable in the case of upgrade attempts.

UIDn

The contents of the Line n UserID configuration parameter.

If unit is customized, value=1, otherwise 0.

Customization status is viewable on Web UI Info page.

Phone number of first connected, ringing, or inbound call. If there are multiple calls, the data associated with the first call found is provided.

| Feature | Required firmware version |
|---|---|
| Emergency call | PhoneOS 3.0.1 and later |
| Custom service | PhoneOS 3.2.1 and later |
| Multiple triggers | PhoneOS 3.3.1 and later |
| HTTP Post | PhoneOS 3.3.1 and later |
| Multiple events on a single trigger | PhoneOS 3.4.1 and later |

| 1 | From the customer view in Control Hub , go to Devices , and then
          select your phone. |
|---|---|
| 2 | Select All configurations . |
| 3 | Navigate to the Phone section and select Action
            Button . |
| 4 | Configure the following parameters: Action Button Function : Select Emergency
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
                emergency call. During a silent emergency call, the screen on phone 9811 and 9841 will freeze, while the screen on
                phone 9851, 9861, and 9871 will be turned off. All other functions are inaccessible.
                The phone restores normal operation after the recipient ends the call. Allow Silent
                  Emergency Call Retrieval (Optional): Enable this feature if you allow
                users to press any key to restore normal phone operation while maintaining the
                emergency call. The call audio remains silent unless the user increases the speaker
                volume using the Volume key. For more details about these parameters, see Parameters for the Action button . |
| 5 | Select Next . |
| 6 | Review your changes and select Apply . |
| 7 | Select Close to close the page. |

| 1 | From the customer view in Control Hub , go to Devices , and then select your phone. |
|---|---|
| 2 | Select All configurations . |
| 3 | Navigate to the Phone section and select Action Button . |
| 4 | Configure the following parameters to associate the Action button with a custom
          service. Action Button Function : Select Custom . Action Button Service Destination :
                Enter the URL of the custom service. The URL must start with http:// or https:// , for example, https://10.11.20.159/path/service.xml . Action Button Service Name (Optional): Specify a name for the service associated with the trigger. This name
                will be displayed in the on-screen message when the user presses the button,
                indicating which service will be triggered. When no name is specified, Custom
                  service will be used as the display name. Custom Content Field (Optional): If
                you want to enable the phone to send an HTTP Post request when the Action button is
                pressed, enter the HTTP data such as method, header, and post content, with a
                maximum length of 1024 characters. For POST script examples and the syntax, see HTTP Post request for the Action
                  button . Dial Out Delay : Set the timeout
                period, in seconds, for the phone to initiate an event after detecting the trigger.
                The default value is 5 seconds. When set to 0, the event is initiated immediately
                upon trigger detection. Service Trigger Select a trigger
                from the list: Single Press , Long
                  Press , or Press 3 Times . For more details about these parameters, see Parameters for the Action button . |
| 5 | Select Next . |
| 6 | Review your changes and select Apply . |
| 7 | Select Close to close the page. |

| 1 | From the customer view in Control Hub , go to Devices , and then
          select your phone. |
|---|---|
| 2 | Select All configurations . |
| 3 | Navigate to the Phone section and select Action
            Button . |
| 4 | Configure the following parameters to enable the Action button to trigger multiple
          events at a time. Action Button Function : Select Custom . Action Button Service Destination : Enter the phone number
                  to call and the XML service URL in this format: tel:<phonenumber or SIP URI> +
                  <serviceURL> The URL must start with http:// or https:// . Example: tel:1234 + https://10.11.20.159/path/service.xml Action Button Service
                  Name (Optional): Specify a name for the service associated with the
                action trigger. This name will be displayed in the on-screen message when the user
                presses the button, indicating which service will be triggered. When no name is
                specified, Custom
                  service will be used as the display name. Custom Content Field (Optional): If you want to enable the
                phone to send an HTTP Post request when the Action button is pressed, enter the HTTP
                data such as method, header, and post content, with a maximum length of 1024
                characters. For POST script examples and the syntax, see HTTP Post request for the Action
                  button . Dial Out Delay : Set the timeout period, in seconds, for the
                phone to initiate an event after detecting the trigger. The default value is 5
                seconds. When set to 0, the event is initiated immediately upon trigger
                detection. Service Trigger Select a trigger
                from the list: Single Press , Long
                  Press , or Press 3 Times . Silent Emergency Call (Optional): If you have included a
                  phone number or dialing URI in the service destination, enabling this feature will
                  silent emergency calls. By default, the emergency call functions as a two-way call, similar to other
                  outgoing calls. When set to enabled, the audio is silent on the caller side to
                  avoid drawing attention during the onging call. Only the call recipient can end
                  the call. During a silent emergency call, the screen on phone 9811 and 9841 will freeze, while the screen on
                  phone 9851, 9861, and 9871 will be turned off. All other functions are
                  inaccessible. The phone restores normal operation after the recipient ends the
                  call. Allow Silent
                  Emergency Call Retrieval (Optional): Enable this feature if you allow
                users to press any key to restore normal phone operation while maintaining the
                emergency call. The call audio remains silent unless the user increases the speaker
                volume using the Volume key. For more details about these parameters, see Parameters for the Action button . |
| 5 | Select Next . |
| 6 | Review your changes and select Apply . |
| 7 | Select Close to close the page. |

| 1 | From the customer view in Control Hub , go to Devices , and then select your phone. |
|---|---|
| 2 | Select All configurations . |
| 3 | Navigate to the Phone section and select Action Button . |
| 4 | Set Service Trigger to MultiTrigger . When the MultiTrigger option is selected, only the
                  settings in the Service Trigger MultiTrigger section will
                  be applied, while the settings related to Action button outside that section will
                  be ignored. Make sure to configure at least one trigger when the MultiTrigger option is selected. |
| 5 | Go to Action Button > Service Trigger MultiTrigger and select your desired trigger from the available options - Single Press , Long Press , and Press 3 times . |
| 6 | Configure the following parameters for your selected trigger: Action Button Function : Select the service that phone users
                can access via the trigger. Action Button Service Destination : Enter phone number or the
                URI of the service. Action Button Service Name (Optional): Specify a name for
                the service associated with the action trigger. This name will be displayed in the
                on-screen message when the user presses the button, indicating which service will be
                triggered. If no name is specified, the default name will be Emergency call, Silent
                emergency call, or Custom action based on your selection in the Action
                  Button Function field. Custom Content Field (Optional): If
                you want to enable the phone to send an HTTP Post request when the Action button is
                pressed, enter the HTTP data such as method, header, and post content, with a
                maximum length of 1024 characters. For POST script examples and the syntax, see HTTP Post request for the Action
                  button . Dial Out Delay : Set the timeout period, in seconds, for the
                phone to initiate an event after detecting the trigger. The default value is 5
                seconds. When set to 0, the event is initiated immediately upon trigger
                detection. Silent Emergency Call (Optional): If you have set the
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
                volume using the Volume key. This parameter is located at Action Button > Allow Silent Emergency Call Retrieval . For more details about these parameters, see Parameters for the Action button . |
| 7 | Repeat Step 5 to 6 to configure more triggers. |
| 8 | Select Next . |
| 9 | Review your changes and select Apply . |
| 10 | Select Close to close the page. |

| Parameter | Default and options | Description |
|---|---|---|
| Action Button Function | Default: Off Options: Off, Emergency Call, Custom | You can configure the button with a specific service. Off : When set to Off, the Action button for single
                      service on the phone will not function. Emergency Call : Users can use the Action button to
                      place an emergency call, if configured. Custom : Users can use the Action button to access the
                      custom service, if configured. When you set the field to Emergency Call or Custom , make sure that you enter the service
                    destination in the Action Button Service Destination field. Or, the phone will display a configuration error. |
| Action Button Service Destination | Default: Empty | Provide the service destination in one of the following formats based on the
                    service assigned to the Action button: For emergency call services, enter a telephone number or the URI of
                        emergency service. When configure the button for a custom service, enter the service URL. The
                        URL must start with http:// or https:// . For example, https://10.11.20.159/path/service.xml . To configure the button to initiate multiple events with a single trigger,
                        enter tel:<phonenumber or SIP URL> + <Service
                          RUL> . Example : tel:1234 +
                          https://10.11.20.159/path/service.xml . Calling SIP URIs is also supported. Enter the URI in the format of tel: sip 4567@co.webex.com For more information about a single trigger for multiple events, see Configure a single trigger for multiple events . If you enable the Action button without setting a valid service destination,
                    the user on the phone will see a message prompting for configuration. After the
                    user closes this notification, the warning icon will persist in the header of
                    the phone screen until the button is properly configured or disabled. Phone numbers cannot be used as destinations for custom services. If you
                      configure the Action Button as Custom and enter a phone
                      number as the service destination, an alert message will display on the phone
                      indicating that the button is unconfigured. Instead, you can add a phone
                      number in this format tel:<phone number> , for
                      example, tel:1234 . |
| Action Button Service Name | Default: Empty | Optionally specify a name for the service associated with the Action button.
                    This name will be displayed in the on-screen message when the user presses the
                    button, indicating which service will be triggered. If you don't specify a name, the default name will be Emergency call, Silent
                    emergency call, or Custom action based on your selection in the Action Button Function field. |
| Allow
                  Silent Emergency Call Retrieval | Default: No Options: Yes, No | Controls whether users can retrieve phone functionality during a silent
                    emergency call. By default, once a silent emergency call is initiated, the phone
                    locks all functions until the call recipient ends the call. When this parameter is set to Yes , users can press any
                    key to restore normal phone operation while maintaining the emergency call. The
                    call audio remains silent unless the user increases the volume using the Volume
                    key. |
| Custom Content Field | Default: Empty | This setting works only when the Action Button
                        Function is set to Custom . Enter the HTTP data such as method, header, and post content, with a maximum
                    length of 1024 characters. When configured, the phone sends an HTTP Post request
                    when the Action is pressed. You can use macros in the HTTP data, such as $MA, $SN. For POST script examples and the syntax, see HTTP Post request for the Action button . |
| Dial Out Delay | Default: 5 Options: 0 - 30 | Set the timeout period, in seconds, for the phone to initiate an emergency call
                    or a custom action after the Action button is pressed. Set it to 0 if you prefer the phone to place the call or initiate an event
                    immediately upon detecting the trigger, as specified by a single press, long
                    press, or triple presses on the button. |
| Service Trigger | Default: Single Press Options: Single Press, Long Press, Press 3 times,
                  MultiTrigger | Choose how users can place an emergency call or initiate a custom service using
                    the phone's Action button. Single Press : Press the Action button to trigger the
                    associated call or service. Long Press : Press the Action button down for at least 2
                    seconds to trigger the associated call or service. Press 3 times : Press the Action button three times with
                    intervals of one second between each press to trigger the associated call or
                    service. MultiTrigger :
                    Select this option to associate multiple triggers and events to the Action
                    button. Go to the Service Trigger MultiTrigger section to
                    select a trigger and configure the specific settings. For detailed information about multiple triggers, see Configure multiple triggers . |
| Service Trigger MultiTrigger | Options: Single Press, Long Press, Press 3 times | This setting works only when Service Trigger is set to MultiTrigger . Choose a trigger from the available options to open and configure the
                  settings. For detailed information about multiple triggers, see Configure multiple triggers . For details about the MultiTrigger parameters, see Parameters for MultiTrigger . |
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

| Parameter | Default and options | Description |
|---|---|---|
| Action Button Function | Default: Off Options: Off, Emergency Call, Custom | Select the service that phone users can access via the service trigger. Off : When set to Off, the action trigger will not
                      function. Emergency Call : Users can place a call to the
                      designated emergency number via the action trigger. Custom : Users can access the designated service via
                      the action trigger. When you set the field to Emergency Call or Custom , make sure that you enter the proper service
                        destination in the Action Button Service Destination field. Or, the phone will display a configuration error. |
| Action Button Service Destination | Default: Empty | Provide the phone number, the URI for emergency call, or the URL for the custom
                    service. If you enter a service URL, the URL must start with http:// or https:// . Example: https://10.11.20.159/path/service.xml . Phone numbers cannot be used as destinations for custom services. If you
                      configure the Action Button as Custom and enter a phone
                      number as the service destination, an alert message will display on the phone
                      indicating that the button is unconfigured. Instead, you can add a phone
                      number in this format tel:<phone number> , for
                      example, tel:1234 . |
| Action Button Service Name | Default: Empty | Optionally specify a name for the service associated with the action trigger.
                    This name will be displayed in the on-screen message when the user presses the
                    button, indicating which service will be triggered. If you don't specify a name, the default name will be Emergency call, Silent
                    emergency call, or Custom action based on your selection in the Action Button Function field. |
| Custom Content Field | Default: Empty | This setting works only when the Action Button
                        Function is set to Custom . Enter the HTTP data such as method, header, and post content, with a maximum
                    length of 1024 characters. When configured, the phone sends an HTTP Post request
                    when the Action is pressed. You can use macros in the HTTP data, such as $MA, $SN. For POST script examples and the syntax, see HTTP Post request for the Action
                    button . |
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

| Macro Name | Macro Expansion |
|---|---|
| $ | The form $$ expands to a single $ character. |
| A through P | Replaced by general-purpose parameters GPP_A through GPP_P. |
| SA through SD | Replaced by special purpose parameters GPP_SA through GPP_SD. These parameters
                hold keys or passwords used in provisioning. $SA through $SD are recognized as arguments to the optional resync URL
                    qualifier, --key. |
| MA | MAC address using lowercase hex digits (000e08aabbcc). |
| MAU | MAC address using uppercase hex digits (000E08AABBCC). |
| MAC | MAC address using lowercase hex digits with a colon to separate hex digit pairs (00:0e:08:aa:bb:cc). |
| PN | Product Name; for example, Video Phone 8875, Desk Phone 9851. |
| PSN | Product Series Number; for example, 8875, 9841, 9861 |
| SN | Serial Number string; for example, 88012BA01234. |
| CCERT | SSL Client Certificate status, installed or not installed. |
| IP | IP address of the phone within its local subnet; for example, 192.168.1.100. |
| EXTIP | External IP of the phone, as seen on the internet; for example, 66.43.16.52. |
| SWVER | Software version string. For example, PHONEOS.3-2-1-0104-37 |
| HWVER | Hardware version string. For example, 2.0.1 |
| PRVST | Provisioning State (a numeric string): -1 = explicit resync request 0 = power-up resync 1 = periodic resync 2 = resync failed, retry attempt |
| UPGST | Upgrade State (a numeric string): 1 = first upgrade attempt 2 = upgrade failed, retry attempt |
| UPGERR | Result message (ERR) of previous upgrade attempt; for example http_get failed. |
| PRVTMR | Seconds since last resync attempt. |
| UPGTMR | Seconds since last upgrade attempt. |
| REGTMR1 | Seconds since Line 1 lost registration with SIP server. |
| REGTMR2 | Seconds since Line 2 lost registration with SIP server. |
| UPGCOND | Legacy macro name. |
| SCHEME | File access scheme, one of TFTP, HTTP, or HTTPS, as obtained after parsing resync or upgrade URL. |
| SERV | Request target server host name, as obtained after parsing resync or upgrade URL. |
| SERVIP | Request target server IP address, as obtained after parsing resync or upgrade URL, possibly following DNS lookup. |
| PORT | Request target UDP/TCP port, as obtained after parsing resync or upgrade URL. |
| PATH | Request target file path, as obtained after parsing resync or upgrade URL. |
| ERR | Result message of resync or upgrade attempt. Only useful in generating result syslog messages. The value is preserved in the UPGERR variable in the case of upgrade attempts. |
| UIDn | The contents of the Line n UserID configuration parameter. |
| ISCUST | If unit is customized, value=1, otherwise 0. Customization status is viewable on Web UI Info page. |
| INCOMINGNAME | Name associated with first connected, ringing, or inbound call. |
| REMOTENUMBER | Phone number of first connected, ringing, or inbound call. If there are multiple calls, the data associated with the first call found is provided. |
| DISPLAYNAMEn | The contents of the Line N Display Name configuration parameter. |
| AUTHIDn | The contents of the Line N auth ID configuration parameter. |