---
doc_id: help-webex-com-en-us-article-kwekcg-dba0b9eb96
source_url: https://help.webex.com/en-us/article/kwekcg
retrieved_at: 2026-11-02T13:11:25.277993+00:00
---

The Cisco IP Manager Assistant (Cisco IPMA) feature enables managers and their assistants
        to work together more effectively. Cisco IPMA supports two modes of operation: proxy line
        support and shared line support. Both modes support multiple calls per line for the
        manager.

In the shared-line mode, the manager and assistant share a directory number. The assistant
        handles calls for a manager on the shared directory number. When a manager receives a call,
        both the manager's phone and the assistant's phone will ring.

In proxy-line mode, the assistant is assigned an alternate directory number to manage calls
        on behalf of the manager. The assistant must log in to the Assistant service on their phone
        to activate this functionality. Proxy-line mode supports more features than shared-line
        mode, including call routing, intercepting.

Cisco Desk Phone 9811 and 9841 support only the IPMA Assistant service.

Cisco Desk Phone 9841, 9851, 9861 and Cisco Video Phone 8875 support both the IPMA
          Assistant and Manager services.

## Identify your IPMA service mode

### Manager phone

The Status Window on a manager phone in shared-line mode shows only a bell icon for the DND
        indicator. The phone in proxy-line mode has more indicators.

### Assistant phone

Identify the IPMA service mode in Assistant Console. Follow the steps in Identifying the Mode on the Assistant Console .

## (Assistant) Proxy-line Mode

As an assistant, you can handle calls either on your phone or in Assistant Console .

If you are using Cisco IPMA in proxy-line mode, log in to the Assistant service on your phone
      to handle calls for your manager.

### Log in to Assistant Service

If you are using the phone for the first time, you need to log in to the Assistant Service
        to access the Cisco IPMA features.

Before you begin

Your administrator has configured Cisco IPMA service on your phone.

Access the Assistant Service in one of the following ways based on your phone
          model:

Navigate to Settings > Network and services > Custom services > Assistant service .

Do any of the following:

- Tap the Assistant Service soft button on your phone home
                page. The name of the button may vary with configurations.

- Navigate to Settings > Custom services > Assistant service . The service name may vary with configurations.

Enter your user ID and PIN, then select Submit .

After logging in, the list of managers that you support appears in the Manager
          Status Page and the status window appears on the phone Home page.

### Check the status of your managers

In Manager Status Page, you can view a list of managers that you support along with the
        status of their extension lines that you proxy. See the following table for the line status
        indicators.

On your phone, press Settings .

If prompted, enter the password to access the Settings menu. You can get the password from your administrator.

Navigate to Network and services > Custom services > Assistant service .

The service name may vary with configurations.

View the status of your manager's line.

### Handle calls for your managers

The IPMA softkeys on the Manager Status Page enables you to easily proxy your managers'
        calls.

When an incoming call to your manager alerts, the Manager Status Page prompts up with the
        softkeys.

If you have calls on your phone when a call to your manager alerts, you can also exist the
        Manager Status Page and use the softkeys in the All calls list to
        answer, divert, or transfer calls for your manager.

For more
                  information about manager settings, see Configure manager settings .

Answers an incoming call for the corresponding manager.

Immediately diverts a ringing, connected or on-hold call to the corresponding
                  manager (by default) or to another preset number.

To set the divert target to a directory number, press AsstSett , then press Set Divert Target , then enter the number.

Sends a ringing, connected, or on-hold call to that manager's voice mail.

Takes you offline.

When you are offline and there is another assistant configured for the manager,
                  that assistant becomes the active assistant for the manager.

If no other assistants are available, calls for the manager will not be filtered
                  or diverted, and will ring at the manager's phone.

When the primary assistant goes offline or logs out, the manager's phone and
                    call status are shown on the phone of the next available assistant, which
                    becomes the primary assistant.

On your phone, go to Settings .

If prompted, enter the password to access the Settings menu. You can get the password from your administrator.

Navigate to Network and services > Custom services > Assistant service .

The service name may vary with configurations.

In Manager Status Page , perform the desired actions based on
          your phone model:

Select the manager's line and press the desired softkey
            available on the phone. To show more softkeys, press the More ( .... ) softkey.

Tap More in the manager's line and select the desired option.

### Configure manager settings

On your phone, you can configure IPMA settings for your manager. The status changes for
        Filter, Do Not Disturb, and Divert Calls will sync to the Status Window on your manager's
        phone.

See the following table for the available settings:

Toggles the filter On and Off . When
                  set to On , then the filter rules configured in the Filter
                  Mode apply.

Use the Assistant Console to configure filters for a manager. For more
                  information, see Assistant Console .

Toggles between Exclusive and Inclusive .

Exclusive —Calls matching the phone numbers in the
                      filter list are sent to the assistant; the remaining calls are sent to the
                      manager.

Inclusive —Calls matching the phone numbers in the
                      filter list are sent to the manager; the remaining calls are sent to the
                      assistant.

In Assistant Console, you can use the wildcard characters X for a single
                  digit and * for a string of digits at the beginning or end of a number
                  only.

Turns on or off the Do not disturb (DND) mode on the manager's phone.

If the manager changes the DND status on their phone, the status displayed here
                  changes accordingly.

The number to which calls are diverted, if the Divert Calls field is set
                  to On .

By default, calls are diverted to the corresponding assistant's phone unless
                  another Directory Number is configured here.

On your phone, go to Settings .

If prompted, enter the password to access the Settings menu. You can get the password from your administrator.

Navigate to Network and services > Custom services > Assistant service .

The service name may vary with configurations.

In Manager Status Page , perform the action based on your phone
          model:

- Use the Up and Down keys in Navigation Cluster to highlight the desired manager's
                line and press the Select softkey.

- Use the Up and Down keys to highlight the desired setting and press the Select softkey to change the setting.

- On the manager's line, tap More > Select .

- Tap the desired setting to change it.

To exit the status page, select Exit .

### Configure assistant settings

Use the Assistant Settings page to configure status update display, sorting and diverting
        target. This page also composites of useful softkeys.

Toggles between Enabled and Disabled .

When set to Enabled , you can view the manager's real-time
                  status updates even when you are on a call. It's useful to know if the manager's
                  line is busy or idle before diverting a call.

Toggles between Enabled and Disabled .

When set to Enabled , the Manager Status Page is sorted
                  based on new call events. While the status page stays static when this field is
                  set to Disabled .

When the Divert All field is set to On for a manager, incoming calls to that manager are
                  diverted to the preset divert target. The divert target can be either the selected
                  manager (by default) or another directory number.

Enter the directory number if you want to change the default target.

Changes the toggle settings or opens a setting.

The Manager Status Page, by default, refreshes when a manager's status changes or
                  when there's a new call for a manager.

StpUpdt disables automatic refresh, and StrUpdt enables it.

If you have a long list of supported managers, we recommend disabling automatic
                  refresh to prevent losing your place while scrolling or missing important status
                  updates.

Exits the Assistant Settings screen and returns to the Manager Status Page.

Logs you out of the IPMA service. If no other assistant is available to your
                  manager after you log out, the status window on the manager's phone will display Assistant Watch - Off .

To log in, see Log in to Assistant Service .

On your phone, go to Settings .

If prompted, enter the password to access the Settings menu. You can get the password from your administrator.

Navigate to Network and services > Custom services > Assistant service .

The service name may vary with configurations.

In Manager Status Page , perform the action based on your phone
          model:

- Press the More ( ... ) softkey until you see AsstSett .
                Then press AsstSett to open the settings menu.

- Use the Up and Down key on the Navigation Cluster to highlight the desired setting
                and press Select to make a change.

- On any manager's line, tap More > AsstSett .

- Tap Select in the desired setting to change it.

Select Exit when you complete your changes.

### Assistant Console

You can use Assistant Console to configure the IPMA service and handle calls.

Go to the following links for the guide on using Assistant Console:

- Getting Started with the Assistant Console

- Using the Assistant Console to Handle Calls

## (Manager) Proxy-line Mode

As a manager, you are logged in automatically to the Manager Assistant feature unless you are
      configured to use Cisco Extension Mobility.

### Use the Status Window

The Status Window on your phone home screen displays the status for assistant watch, calls,
        DND, and call filter.

There are two areas within the Status Window:

Assistant Watch area—The top part of the status window displaying the assistant status
            and call status.

- Assistant and Features area—The largest portion of the status window displaying icons to
          indicate the presence of an active assistant and the on/off status of your features.

The Status Window is not visible when you are using your phone to place or receive
              calls.

The display position of the Status Window varies with phone models:

9811/9841: Not supported

9851/9861: In the lower-right section on the Home screen

9871/8875: In the upper-left section on the Home screen. You can drag it to any
              position on the Home screen.

Assistant Watch - On/Off

Displays the status of Assistant Watch for your line.

If Assistant Watch is On , the message displays the call
                  status on your assistant proxy line when there's an alerting or connected call. If
                  it is Off , the Status Window doesn't display the call
                  status.

You can change the status by using the Set Watch softkey
                  on your phone.

Assistant Available

Displays the availability of the assistant.

The status changes when the assistant goes online and offline.

Assistant Unavailable

Filter On

Displays the status of the call filter that was configured.

When the filter is turned on, the calls matching the phone numbers in the filter
                  list are sent to the assistant (Exclusive mode) or to the manager (Inclusive mode)
                  depending on the filter mode specified.

Filter Off

DND Off

Displays the Do Not Disturb (DND) status.

When DND is turned on, all call alerts are silent, except for Intercom calls.

DND On

Divert All enabled

Displays the status of call diverting.

When set to enabled, all calls are sent to the manager or to the specified divert
                  target.

Divert All disabled

### Handle calls

Cisco IPMA offers a series of softkeys for you to easily handle calls and collaborate with
        your assistant. The softkeys are available on the home screen and All calls screen.

If Assistant Watch is turned on,
                  the Status Window displays the call status when there's an alerting or connected
                  call on your assistant proxy line. If it is turned off , the Status Window doesn't
                  display the call status.

Follow these steps based on your use scenario and phone model:

To answer or decline an alerting call, select Answer or Decline accordingly.

To redirect, intercept, or transfer a call,

Press the More ( .... ) softkey and then press the
                desired softkey.

Tap More and then tap the desired option.

### Configure your Cisco IPMA settings

In the Assistant service page on your phone, you can select your
        assistant, change the filter settings, and set call diverting target.

Toggles the filter On and Off . When
                  set to On , then the filter rules configured in the Filter
                  Mode apply.

Your assistant can configure the filter list in the Assistant Console.

Toggles between Exclusive and Inclusive .

Exclusive —Calls matching the phone numbers in the
                      filter list are sent to the assistant; the remaining calls are sent to the
                      manager.

Inclusive —Calls matching the phone numbers in the
                      filter list are sent to the manager; the remaining calls are sent to the
                      assistant.

Displays your current assistant and allows you to select your assistant if you
                  have multiple assistants.

If you have multiple assistants available, you can select one of them in the list
                  to work as the active assistant. If you have only one assistant, this field only
                  displays your assistant name.

Toggles alert tone On and Off . When
                  set to On , incoming calls trigger an audio alert on your
                  phone.

Access the Assistant Service in one of the following ways based on your phone
          model:

Navigate to Settings > Network and services > Custom services > Assistant service .

Locate and tap the Assistant
              service soft button on the home screen.

The service name may vary with configurations.

In the Assistant service page, change the filter settings or
          update the divert target.

Use the Up and Down keys in Navigation
            Cluster to highlight the menu item and then press the Select softkey to change the setting.

Tap Select on a
            menu item.

## (Assistant) Shared-line Mode

You must log in to the Assistant Service to
        access the features. Calls to your manager will automatically ring on your phone. On your
        phone, you can handle calls on your manager's behalf in the following ways:

- Answering calls

- Diverting calls to your manager or another preset number

- Transferring calls to your manager's voice messaging system

### View the manager's status

You can identify the manager's status by the Do Not Disturb (DND) status in the status
        window.

Manager has turned off DND.

Manager has turned on DND.

### IPMA softkeys

Use the softkeys on your phone to handle calls on behalf of your manager.

Redirect : Redirects a call to the manager or to another preset
            number.

TransVM : Sends a ringing or connected call to the manager's
            voice mail.

Intercom : Initiates or answers intercom calls. This softkey is
            available only when configured.

### Assistant Console

The Assistant Console application helps assistants to handle calls for managers more
        effectively. You can use the Assistant Console to:

- Place, answer, divert, transfer, end, or hold a call

- Add conference participants to a call

- Perform speed dialing

- Do directory searches

- Open an intercom line to your manager

- Monitor manager call activity

- Change manager features and settings

- Customize your call-handling tools

- Key in numbers on a virtual keypad in response to interactive voice systems

For information about how to use Assistant Console, go to the following sections in Cisco Unified Communications Manager Assistant User
            Guide for Cisco Unified Communications Manager :

- Getting Started with the Assistant Console

- Using the Assistant Console to Handle Calls

- Configuring Manager Features

## (Manager) Shared-line Mode

In the shared-line mode, you and your assistant are assigned the same directory number, and
        your assistant uses the shared number to handle calls for you.

You can use the IPMA softkeys on your phone to divert, transfer, and generally handle
        active calls:

Redirect : Redirects a call to the assistant or to another phone
            number that has been set up as the divert target. You or your assistant can change this
            target from the Manager Configuration window.

TransVM : Sends a call immediately from your phone to your voice
            mail.

Intercom : Initiates or answers intercom calls. This softkey is
            available only when configured.

### Mute the Ringer on Your Phone

The Do Not Disturb (DND) feature disables the ringer for all lines on the phone, except for
        Intercom calls. Your DND status is visible to your assistant so that they can handle your
        calls based on your availability.

To mute the ringer on your phone,

Press the DND softkey to toggle DND on or
        off.

Tap the DND soft button on your phone to
        toggle DND on or off.

| 1 | Access the Assistant Service in one of the following ways based on your phone
          model: Navigate to Settings > Network and services > Custom services > Assistant service . Do any of the following: Tap the Assistant Service soft button on your phone home
                page. The name of the button may vary with configurations. Navigate to Settings > Custom services > Assistant service . The service name may vary with configurations. |
|---|---|
| 2 | Enter your user ID and PIN, then select Submit . After logging in, the list of managers that you support appears in the Manager
          Status Page and the status window appears on the phone Home page. |

| Indicator | Status |
|---|---|
|  | Idle |
|  | Off hook |
|  | Dialing |
|  | In a call or a call is ringing. |
|  | Hold |
|  | Unknown |

| 1 | On your phone, press Settings . |
|---|---|
| 2 | If prompted, enter the password to access the Settings menu. You can get the password from your administrator. |
| 3 | Navigate to Network and services > Custom services > Assistant service . The service name may vary with configurations. |
| 4 | View the status of your manager's line. |

| Softkey | Description |
|---|---|
| Select | Takes you to the manager settings for the selected manager. For more
                  information about manager settings, see Configure manager settings . |
| Answer | Answers an incoming call for the corresponding manager. |
| Exit | Exits the Manager Status Page and takes you to the Custom services
                menu. |
| Redirect | Immediately diverts a ringing, connected or on-hold call to the corresponding
                  manager (by default) or to another preset number. To set the divert target to a directory number, press AsstSett , then press Set Divert Target , then enter the number. |
| TransfVM | Sends a ringing, connected, or on-hold call to that manager's voice mail. |
| InterCom | Enables you to speak to a manager on an intercom line. |
| GoOffLine | Takes you offline. When you are offline and there is another assistant configured for the manager,
                  that assistant becomes the active assistant for the manager. If no other assistants are available, calls for the manager will not be filtered
                  or diverted, and will ring at the manager's phone. When the primary assistant goes offline or logs out, the manager's phone and
                    call status are shown on the phone of the next available assistant, which
                    becomes the primary assistant. |
| AsstSett | Takes you to the Assistant Settings, where you configure various settings. For
                more information about the settings, see Configure assistant settings . |

| 1 | On your phone, go to Settings . |
|---|---|
| 2 | If prompted, enter the password to access the Settings menu. You can get the password from your administrator. |
| 3 | Navigate to Network and services > Custom services > Assistant service . The service name may vary with configurations. |
| 4 | In Manager Status Page , perform the desired actions based on
          your phone model: Select the manager's line and press the desired softkey
            available on the phone. To show more softkeys, press the More ( .... ) softkey. Tap More in the manager's line and select the desired option. |

| Field | Description |
|---|---|
| Filter | Toggles the filter On and Off . When
                  set to On , then the filter rules configured in the Filter
                  Mode apply. Use the Assistant Console to configure filters for a manager. For more
                  information, see Assistant Console . |
| Filter Mode | Toggles between Exclusive and Inclusive . Exclusive —Calls matching the phone numbers in the
                      filter list are sent to the assistant; the remaining calls are sent to the
                      manager. Inclusive —Calls matching the phone numbers in the
                      filter list are sent to the manager; the remaining calls are sent to the
                      assistant. In Assistant Console, you can use the wildcard characters X for a single
                  digit and * for a string of digits at the beginning or end of a number
                  only. |
| Do not disturb | Turns on or off the Do not disturb (DND) mode on the manager's phone. If the manager changes the DND status on their phone, the status displayed here
                  changes accordingly. |
| Divert Calls | Toggles between On and Off . When
                set to On , all the calls to the manager will be automatically redirected to
                the assistant or to the directory number set in Set Divert
                  Target . |
| Set Divert Target | The number to which calls are diverted, if the Divert Calls field is set
                  to On . By default, calls are diverted to the corresponding assistant's phone unless
                  another Directory Number is configured here. |
| Alert Tone | Toggles alert tone On and Off .
                When set to On , calls to the manager trigger an audio alert
                on the manager's phone. |

| 1 | On your phone, go to Settings . |
|---|---|
| 2 | If prompted, enter the password to access the Settings menu. You can get the password from your administrator. |
| 3 | Navigate to Network and services > Custom services > Assistant service . The service name may vary with configurations. |
| 4 | In Manager Status Page , perform the action based on your phone
          model: Use the Up and Down keys in Navigation Cluster to highlight the desired manager's
                line and press the Select softkey. Use the Up and Down keys to highlight the desired setting and press the Select softkey to change the setting. On the manager's line, tap More > Select . Tap the desired setting to change it. |
| 5 | To exit the status page, select Exit . |

| Field | Description |
|---|---|
| CallPlaneOverWrite | Toggles between Enabled and Disabled . When set to Enabled , you can view the manager's real-time
                  status updates even when you are on a call. It's useful to know if the manager's
                  line is busy or idle before diverting a call. |
| SmartSorting | Toggles between Enabled and Disabled . When set to Enabled , the Manager Status Page is sorted
                  based on new call events. While the status page stays static when this field is
                  set to Disabled . |
| SetDivertTarget | When the Divert All field is set to On for a manager, incoming calls to that manager are
                  diverted to the preset divert target. The divert target can be either the selected
                  manager (by default) or another directory number. Enter the directory number if you want to change the default target. |

| Field | Description |
|---|---|
| Select | Changes the toggle settings or opens a setting. |
| StpUpdt/StrUpdt | The Manager Status Page, by default, refreshes when a manager's status changes or
                  when there's a new call for a manager. StpUpdt disables automatic refresh, and StrUpdt enables it. If you have a long list of supported managers, we recommend disabling automatic
                  refresh to prevent losing your place while scrolling or missing important status
                  updates. |
| Exit | Exits the Assistant Settings screen and returns to the Manager Status Page. |
| LogOut | Logs you out of the IPMA service. If no other assistant is available to your
                  manager after you log out, the status window on the manager's phone will display Assistant Watch - Off . To log in, see Log in to Assistant Service . |

| 1 | On your phone, go to Settings . |
|---|---|
| 2 | If prompted, enter the password to access the Settings menu. You can get the password from your administrator. |
| 3 | Navigate to Network and services > Custom services > Assistant service . The service name may vary with configurations. |
| 4 | In Manager Status Page , perform the action based on your phone
          model: Press the More ( ... ) softkey until you see AsstSett .
                Then press AsstSett to open the settings menu. Use the Up and Down key on the Navigation Cluster to highlight the desired setting
                and press Select to make a change. On any manager's line, tap More > AsstSett . Tap Select in the desired setting to change it. |
| 5 | Select Exit when you complete your changes. |

| Message | Description |
|---|---|
| Assistant Watch - On/Off | Displays the status of Assistant Watch for your line. If Assistant Watch is On , the message displays the call
                  status on your assistant proxy line when there's an alerting or connected call. If
                  it is Off , the Status Window doesn't display the call
                  status. You can change the status by using the Set Watch softkey
                  on your phone. |
| Call from <Caller ID> | An incoming call was redirected to your assistant and is currently ringing on
                your assistant's phone. You can intercept the call. |
| <Caller ID> and <a
                timer> | The assistant answered the incoming call. The timer begins when the assistant
                answers the call. You can intercept the call, if needed. |
| Filtering Down | Call filtering feature is unavailable. |

| Icon | Description |
|---|---|
| Assistant Available | Displays the availability of the assistant. The status changes when the assistant goes online and offline. |
| Assistant Unavailable |
| Filter On | Displays the status of the call filter that was configured. When the filter is turned on, the calls matching the phone numbers in the filter
                  list are sent to the assistant (Exclusive mode) or to the manager (Inclusive mode)
                  depending on the filter mode specified. |
| Filter Off |
| DND Off | Displays the Do Not Disturb (DND) status. When DND is turned on, all call alerts are silent, except for Intercom calls. |
| DND On |
| Divert All enabled | Displays the status of call diverting. When set to enabled, all calls are sent to the manager or to the specified divert
                  target. |
| Divert All disabled |

| Softkey | Description |
|---|---|
| Answer | Answers an incoming call. |
| Redirect | Redirects a call to your assistant. |
| Intercept | Intercepts a call when it's ringing or connected on your assistant
                phone. |
| TrnsfVM | Transfers a call to your voice mail. |
| Set Watch | Turns on or off the Assistant Watch feature. If Assistant Watch is turned on,
                  the Status Window displays the call status when there's an alerting or connected
                  call on your assistant proxy line. If it is turned off , the Status Window doesn't
                  display the call status. |

| Follow these steps based on your use scenario and phone model: To answer or decline an alerting call, select Answer or Decline accordingly. To redirect, intercept, or transfer a call, Press the More ( .... ) softkey and then press the
                desired softkey. Tap More and then tap the desired option. |
|---|

| Filed | Description |
|---|---|
| Filter | Toggles the filter On and Off . When
                  set to On , then the filter rules configured in the Filter
                  Mode apply. Your assistant can configure the filter list in the Assistant Console. |
| Filter Mode | Toggles between Exclusive and Inclusive . Exclusive —Calls matching the phone numbers in the
                      filter list are sent to the assistant; the remaining calls are sent to the
                      manager. Inclusive —Calls matching the phone numbers in the
                      filter list are sent to the manager; the remaining calls are sent to the
                      assistant. |
| Assistant | Displays your current assistant and allows you to select your assistant if you
                  have multiple assistants. If you have multiple assistants available, you can select one of them in the list
                  to work as the active assistant. If you have only one assistant, this field only
                  displays your assistant name. |
| Alert Tone | Toggles alert tone On and Off . When
                  set to On , incoming calls trigger an audio alert on your
                  phone. |

| 1 | Access the Assistant Service in one of the following ways based on your phone
          model: Navigate to Settings > Network and services > Custom services > Assistant service . Locate and tap the Assistant
              service soft button on the home screen. The service name may vary with configurations. |
|---|---|
| 2 | In the Assistant service page, change the filter settings or
          update the divert target. Use the Up and Down keys in Navigation
            Cluster to highlight the menu item and then press the Select softkey to change the setting. Tap Select on a
            menu item. |

## Figuras

![The Status Window in shared-line mode](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/488001-489000/488082.png)

![The Status Window in proxy-line mode](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/488001-489000/488081.png)

![For 9811, 9841,9851, and 9861](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/489001-490000/489180.png)

![the Settings hard key](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/300001-400000/370001-380000/371001-372000/371845.jpg)

![Icon for 9871 and 8875 for common topics](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/485001-486000/485950.png)

![the icon for an idle line](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/488001-489000/488083.png)

![the icon for off-hook line](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/488001-489000/488079.png)

![the icon for dialing](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/488001-489000/488078.png)

![the icon for active calls](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/482001-483000/482647.png)

![the icon for held calls](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/482001-483000/482648.png)

![the icon for an unknown line status](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/488001-489000/488080.png)

![The More button on the "New call" screen after tapping a line on Desk Phone 9871](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/483001-484000/484030.png)

![the icon for IPMA Call Filter On](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/488001-489000/488065.png)

![the icon for IPMA Assistant Watch Off](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/488001-489000/488064.png)

![the icon for IPMA Call Filter On](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/488001-489000/488063.png)

![the icon for IPMA Call Filter Off](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/488001-489000/488062.png)

![the icon for IPMA DND Off](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/488001-489000/488061.png)

![the icon for IPMA DND On](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/488001-489000/488060.png)

![the icon for IPMA Divert All is On](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/488001-489000/488067.png)

![the icon for IPMA Divert All is Off](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/488001-489000/488066.png)

![For 9841, 9851, and 9861 phones](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/483001-484000/483151.png)