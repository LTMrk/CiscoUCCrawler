---
doc_id: help-webex-com-en-us-article-n0pf1t7-3652684028
source_url: https://help.webex.com/en-us/article/n0pf1t7
retrieved_at: 2026-11-02T13:11:52.140167+00:00
---

## Make a call with speed dial

- 9811 / 9841 / 9851 / 9861

- 8875 / 9871

Once added, speed dials and BLF with speed dials are available in the following
          locations:

- On the line keys of your phone or the connected Key Expansion Module (KEM)

The speed dial list displays both basic speed dials and BLF with speed dials. In
                the list, the BLF with speed dials work as basic speed dials and don't show the
                monitored line status.

Before you begin

Speed dial numbers have been added to your phone.

Do any of the following actions as needed:

Place a call with the primary line in the following ways:

- Press the line key assigned to the speed dial on the phone or a connected
                  KEM.

- Press the Down navigation key to open the speed dials list, then enter the speed
                  dial index number on the keypad.

- Press the Down navigation key to open the speed dials list, select the desired
                  speed dial using the navigation keys, then press Call .

- Press the Down navigation key to open the speed dials list, select the desired
                speed dial, then press the extension line key you want to use.

- Press the extension line key you want to use, then press the line key assigned to
                the speed dial.

You can find your speed dials or BLF with speed dials in the pull-down speed dial list or
        on the Speed dials tab.

If multiple lines are configured, select the line you want to use for the call. Otherwise,
        the primary line is used.

Before you begin

Speed dial numbers have been added to your phone.

Follow the steps that are applicable to the configuration on your phone:

- Swipe down from the top of the screen to open the speed dials list.

- Tap a speed dial button to call the associated extension.

- Tap the line that you want to use on the Home screen or on the Lines tab.

- Swipe down from the top of the screen to open the speed dials list.

- Tap a speed dial button to call the associated extension.

- Press the line key with speed dial to place a call with the primary line.

- Select the line key that you want to use and then press the line key with speed
                dial on KEM

## Check speed dial status

The following tables list the status indicators for BLF with speed dial on different phone
        models.

LED off

The monitored line is in idle mode.

You can press the line key to call the speed dial number.

Solid amber

Alerting

A call is alerting on the monitored line.

The alerting status is only available on phones that are registered with Cisco
                    BroadWorks or Webex Calling.

Solid red

The monitored line is on a call.

If you press the line key, a call is placed to the speed dial number. You’ll hear
                  a busy tone or be redirected to the voicemail depending on the configuration on
                  your coworker's line.

Solid red

The monitored line is set to Do Not Disturb (DND).

The calls to the line don't alert.

The DND status of the monitored line is only available on phones that are
                    registered with Cisco Unified Communications Manager.

LED off

The server can't retrieve the status information of the monitored line.

The unrecognized status is only available on phones that are registered with
                    Cisco BroadWorks or Webex Calling.

LED off

The server can't retrieve the status information of the monitored line.

The unknown status is only available on phones that are registered with Cisco
                    Unified Communications Manager.

LED off

The Local DND status is only available on phones that are registered with Cisco
                    Unified Communications Manager.

The monitored line is in idle mode.

You can tap the shortcut to call the speed dial number.

Alerting

A call is alerting on the monitored line.

The alerting status is only available on phones that are registered with Cisco
                    BroadWorks or Webex Calling.

The monitored line is on a call.

If you tap the shortcut, a call is placed to the speed dial number. You’ll hear a
                  busy tone or be redirected to the voicemail depending on the configuration on the
                  monitored line.

The monitored line is set to Do Not Disturb (DND).

The calls to the line don't alert.

The DND status is only available on phones that are registered with Cisco
                    Unified Communications Manager.

The server can't retrieve the status information of the monitored line.

The unrecognized status is only available on phones that are registered with
                    Cisco BroadWorks or Webex Calling.

The server can't retrieve the status information of the monitored line.

The unknown status is only available on phones that are registered with Cisco
                    Unified Communications Manager.

The Local DND status is only available on phones that are registered with Cisco
                    Unified Communications Manager.

For more information about the BLF with both speed dial and call pickup, see Answer calls for your coworkers (on Unified CM) or Answer calls for your coworkers (on BroadWorks or Webex Calling).

## Manage speed dials in user portals

The way you manage speed dials depends on the calling system your phone is registered
        with.

Webex Calling : User Hub

Unified CM (UCM) : Self Care
              Portal

Cisco BroadWorks : No user portal for adding speed dials

### Configure speed dials in User Hub

Speed dials offer one-key access to contacts through the phone or Key Expansion Module
        (KEMs). This feature is only supported on devices that display speed dials on line keys
        configured as Open. Appearance may vary by phone model.

Sign in to User Hub .

Go to Settings > Calling > Call Settings .

In Speed Dial section, click Add speed
            dial .

Add a speed dial by choosing the following options:

- Select Organization Directory .

- Select Custom contacts

If you have selected Organization directory , perform the
          following steps:

Select a phone number from the drop-down.

If you wish you override the default label, click Override line key
                label check-box and add a Preferred label , which
              will be displayed on the phone.

If you have selected Custom contact , perform the following
          steps:

Enter Line key label , a name of the speed dial.

Enter Phone number to dial.

Click Save .

A speed dial is created. From Actions ellipses icon you
          can edit, delete, or reorder the speed dials. The updates will show on the open lines on
          the phone within seconds.

### Manage speed dials in Self Care Portal

If your phone is registered with Cisco Unified Communications Manager, you can manage speed
        dials with the web-based Cisco Unified Communications Self Care Portal.

Log in to Cisco Unified Communications Self Care Portal.

Choose Phones > Phone Settings > Speed Dial Numbers .

Do the following to add a speed dial:

- If your phones are linked, click Add New Speed
            Dial .

- If your phones are not linked, click your phone and then click Add New
              Speed Dial .

Enter the following information:

- Number/URI : Search for the contact to add or directly enter
              the phone number or URI of the contact.

- Label (Description) : Provide a name for the speed dial.

- Speed Dial : Enter an index number ranging from 1 to 199. The
              index number determines the display order in the speed dial list and on the phone and
              KEM line keys. Lower numbers appear before higher numbers. We recommend assigning
              consecutive numbers for more efficient use of the line keys.

Click Save .

To edit a speed dial, click .

To remove a speed dial, click .

#### Tips for special speed dial numbers

When you dial a number on your phone, you enter a series of digits. When you set up a speed dial number, it must contain all the digits you need to make the call. For example, if you need to dial 9 to get an outside line, you enter the number 9 and then the number you want to dial.

You can also add other dialed digits to the number. Examples of additional digits include a meeting access code, an extension, a voicemail password, an authorization code, and a billing code.

The dial string can contain the following characters:

0 to 9

Pound (#)

Asterisk (*)

Comma (,)—This is the pause character, and gives a 2 second delay in the dialing. You
            can have several commas in a row. For example, two commas (,,) represent a pause of 4
            seconds.

The rules for dial strings are:

- Use the comma (,) to separate the parts of the dial string.

- An authorization code must always precede a billing code in the speed-dial string.

- A single comma is required between the authorization code and the billing code in the string.

- A speed-dial label is required for speed dials with authorization codes and additional digits.

Before you configure the speed dial, try to dial the digits manually at least once to
        ensure that the digit sequence is correct.

Your phone does not save the authorization code, billing code, or extra digits from the speed dial in the call history. If you try to redial a number after you connect to a speed-dial destination, the phone prompts you to enter any required authorization code, billing code, or additional digits manually.

To set up a speed dial number to call a person at a specific extension, and if you need an authorization code and billing code, consider the following requirements:

- You need to dial 9 for an outside line.

- You want to call 5556543 .

- You need to input the authorization code 1234 .

- You need to input the billing code 9876 .

- You must wait for 4 seconds.

- After the call connects, you must dial the extension 56789# .

In this scenario, the speed-dial number is 95556543,1234,9876,,56789# .

The maximum number of speed dials allowed depends on the number of supported lines on
            your phone and the connected KEMs.

## Manage speed dials on the phone

The Speed dials list may include entries added on the phone and
        those added through the web-based user portal or admin portal.

On phones registered with Webex Calling or Cisco Unified CM, you can edit or remove
              only speed dials added from the phone. These speed dials don’t sync with the portals
              and may be overridden by configurations from the portals.

On phones registered with BroadWorks, the speed dial changes sync between the phone
              and the admin portal.

- 9811 / 9841 / 9851 / 9861

- 8875 / 9871

### Assign a speed dial to a line key

You can add a speed-dial number on any idle line key on the phone or on the connected KEMs.
        After you configure the speed dial, you can press the line key to call the associated
        number.

Long-press an available line key to open the speed dial setup page.

Choose an option from the list. The available options depend on the calling system that
          your phone is registered with.

- To only assign a speed-dial number on the line key, select Create Speed
                  dial and enter the required information.

- To monitor a line and also speed dial the monitored line, select Create
                  BLF + Speed dial , and then enter or select a user ID.

- To monitor a line, speed dial the monitored line, and also answer incoming calls
                to the monitored line, select Create BLF + Speed dial + Call
                  pickup , and then enter or select a user ID.

You can manually enter the user ID or select a user ID from the user ID list, if
                available.

To switch between number and alphabet
                  inputs, press 123 or ABC .

- Press Save .

### Edit speed dials

An updated list of speed dials makes your communication more efficient. You can edit the
        existing speed dial on a line key, or replace it with another.

Long-press the line key configured with a speed dial.

Select an options to edit the speed dial information or replace it with another feature.

The availability of these options vary from phone settings and the calling system that
            it is registered with.

- Edit speed dial

- Edit BLF + Speed dial

- Edit BLF + Speed dial + Call pickup

- Replace with speed dial

- Replace with BLF + Speed dial + Call pickup

Update the speed dial with the desired information.

Select Save .

### Remove speed dials from your phone

When a speed-dial number is no longer a frequently used contact, remove it from the designated line key.

Long-press the line key configured with a speed dial.

Select Remove .

Confirm the removal when prompted.

You can add, edit, and remove speed dials in the speed dial list only on phones that are
        registered with Cisco Unified Communications Manager . The speed dials you add are for
        dialing purposes only and don't support Busy Lamp Field (BLF) functionality.

Speed dials will be added after the last configured line key. If the last line on the phone
        (without a KEM) or on the last connected KEM has already been configured, no additional
        speed dials can be added to the phone. The maximum number of speed dials allowed depends on
        the number of supported lines on your phone and the connected KEMs.

You can edit and remove only the speed dials added locally on the phone. Speed dials
              added remotely through the Self Care Portal or by your administrator on Cisco Unified
              Communication Manager cannot be edited or removed directly on the phone.

The speed dials you’ve added on the phone can be overwritten by the line key feature
              configured by the administrator for the same position.

Swipe down from the top of any screen on the phone to open the speed dials list.

Do one of the following actions as needed:

- Tap Add speed dial or Add ,
                  depending on the option available.

- Enter the contact name and phone number, then tap Save .

- Long-press the speed dial in the list and then select Edit speed
                    dial .

- Change the information as needed and tap Save .

- Long-press the speed dial in the list and then select Remove .

- Tap Remove to confirm the removal.

| Do any of the following actions as needed: Place a call with the primary line in the following ways: Press the line key assigned to the speed dial on the phone or a connected
                  KEM. Press the Down navigation key to open the speed dials list, then enter the speed
                  dial index number on the keypad. Press the Down navigation key to open the speed dials list, select the desired
                  speed dial using the navigation keys, then press Call . Place a call with a specific line in the following ways: Press the Down navigation key to open the speed dials list, select the desired
                speed dial, then press the extension line key you want to use. Press the extension line key you want to use, then press the line key assigned to
                the speed dial. |
|---|

| Use the primary line | Use a specific line |
|---|---|
|  |  |

| Follow the steps that are applicable to the configuration on your phone: To use the primary line Swipe down from the top of the screen to open the speed dials list. Tap a speed dial button to call the associated extension. To use a specific line on a phone with multiple lines Tap the line that you want to use on the Home screen or on the Lines tab. Swipe down from the top of the screen to open the speed dials list. Tap a speed dial button to call the associated extension. To call a speed dial assigned to a line key on the Key Expansion Module
              (KEM) Press the line key with speed dial to place a call with the primary line. Select the line key that you want to use and then press the line key with speed
                dial on KEM |
|---|

| Icon (9811 / 9841) | Icon (9851) | Icon (9861) | Line key LED | Status | Description |
|---|---|---|---|---|---|
|  |  |  | LED off | Idle | The monitored line is in idle mode. You can press the line key to call the speed dial number. |
|  |  |  | Solid amber | Alerting | A call is alerting on the monitored line. The alerting status is only available on phones that are registered with Cisco
                    BroadWorks or Webex Calling. |
|  |  |  | Solid red | In use | The monitored line is on a call. If you press the line key, a call is placed to the speed dial number. You’ll hear
                  a busy tone or be redirected to the voicemail depending on the configuration on
                  your coworker's line. |
|  |  |  | Solid red | DND | The monitored line is set to Do Not Disturb (DND). The calls to the line don't alert. The DND status of the monitored line is only available on phones that are
                    registered with Cisco Unified Communications Manager. |
|  |  |  | LED off | Unrecognized | The server can't retrieve the status information of the monitored line. The unrecognized status is only available on phones that are registered with
                    Cisco BroadWorks or Webex Calling. |
|  |  |  | LED off | Unknown | The server can't retrieve the status information of the monitored line. The unknown status is only available on phones that are registered with Cisco
                    Unified Communications Manager. |
|  |  |  | LED off | Local DND | The DND is enabled on the local phone. The BLF speed dial key doesn't show any
                status of the monitored line, including idle status. The Local DND status is only available on phones that are registered with Cisco
                    Unified Communications Manager. |

| Icon | Status | Description |
|---|---|---|
|  | Idle | The monitored line is in idle mode. You can tap the shortcut to call the speed dial number. |
|  | Alerting | A call is alerting on the monitored line. The alerting status is only available on phones that are registered with Cisco
                    BroadWorks or Webex Calling. |
|  | In use | The monitored line is on a call. If you tap the shortcut, a call is placed to the speed dial number. You’ll hear a
                  busy tone or be redirected to the voicemail depending on the configuration on the
                  monitored line. |
|  | DND | The monitored line is set to Do Not Disturb (DND). The calls to the line don't alert. The DND status is only available on phones that are registered with Cisco
                    Unified Communications Manager. |
|  | Unrecognized | The server can't retrieve the status information of the monitored line. The unrecognized status is only available on phones that are registered with
                    Cisco BroadWorks or Webex Calling. |
|  | Unknown | The server can't retrieve the status information of the monitored line. The unknown status is only available on phones that are registered with Cisco
                    Unified Communications Manager. |
|  | Local DND | The DND is enabled on the local phone. The BLF speed dial key doesn't show any
                status of the monitored line, including idle status. The Local DND status is only available on phones that are registered with Cisco
                    Unified Communications Manager. |

| 1 | Sign in to User Hub . |
|---|---|
| 2 | Go to Settings > Calling > Call Settings . |
| 3 | In Speed Dial section, click Add speed
            dial . |
| 4 | Add a speed dial by choosing the following options: Select Organization Directory . Select Custom contacts |
| 5 | If you have selected Organization directory , perform the
          following steps: Select a phone number from the drop-down. If you wish you override the default label, click Override line key
                label check-box and add a Preferred label , which
              will be displayed on the phone. |
| 6 | If you have selected Custom contact , perform the following
          steps: Enter Line key label , a name of the speed dial. Enter Phone number to dial. |
| 7 | Click Save . A speed dial is created. From Actions ellipses icon you
          can edit, delete, or reorder the speed dials. The updates will show on the open lines on
          the phone within seconds. |

| 1 | Log in to Cisco Unified Communications Self Care Portal. |
|---|---|
| 2 | Choose Phones > Phone Settings > Speed Dial Numbers . |
| 3 | Do the following to add a speed dial: If your phones are linked, click Add New Speed
            Dial . If your phones are not linked, click your phone and then click Add New
              Speed Dial . |
| 4 | Enter the following information: Number/URI : Search for the contact to add or directly enter
              the phone number or URI of the contact. Label (Description) : Provide a name for the speed dial. Speed Dial : Enter an index number ranging from 1 to 199. The
              index number determines the display order in the speed dial list and on the phone and
              KEM line keys. Lower numbers appear before higher numbers. We recommend assigning
              consecutive numbers for more efficient use of the line keys. |
| 5 | Click Save . |
| 6 | To edit a speed dial, click . |
| 7 | To remove a speed dial, click . |

| 1 | Long-press an available line key to open the speed dial setup page. |
|---|---|
| 2 | Choose an option from the list. The available options depend on the calling system that
          your phone is registered with. If your phone is registered with BroadWorks or Webex Calling, do one of the
            following actions as needed: To only assign a speed-dial number on the line key, select Create Speed
                  dial and enter the required information. To monitor a line and also speed dial the monitored line, select Create
                  BLF + Speed dial , and then enter or select a user ID. To monitor a line, speed dial the monitored line, and also answer incoming calls
                to the monitored line, select Create BLF + Speed dial + Call
                  pickup , and then enter or select a user ID. You can manually enter the user ID or select a user ID from the user ID list, if
                available. If your phone is registered with the Unified CM, do the following: Enter the contact name and phone number. To switch between number and alphabet
                  inputs, press 123 or ABC . Press Save . |

| 1 | Long-press the line key configured with a speed dial. |
|---|---|
| 2 | Select an options to edit the speed dial information or replace it with another feature. The availability of these options vary from phone settings and the calling system that
            it is registered with. Edit speed dial Edit BLF + Speed dial Edit BLF + Speed dial + Call pickup Replace with speed dial Replace with BLF + Speed dial + Call pickup |
| 3 | Update the speed dial with the desired information. |
| 4 | Select Save . |

| 1 | Long-press the line key configured with a speed dial. |
|---|---|
| 2 | Select Remove . |
| 3 | Confirm the removal when prompted. |

| 1 | Swipe down from the top of any screen on the phone to open the speed dials list. |
|---|---|
| 2 | Do one of the following actions as needed: Add a speed dial Tap Add speed dial or Add ,
                  depending on the option available. Enter the contact name and phone number, then tap Save . Update a speed dial Long-press the speed dial in the list and then select Edit speed
                    dial . Change the information as needed and tap Save . Remove a speed dial Long-press the speed dial in the list and then select Remove . Tap Remove to confirm the removal. |

## Figuras

![the graphic for using the primary line to call a speed dial](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/475001-476000/475861.png)

![the graphic for using a specific line to call a speed dial](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/475001-476000/475869.png)

![the icon of BLF with speed dial](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/478001-479000/478708.png)

![the icon of BLF with speed dial idel](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/478001-479000/478714.png)

![the line key in the not-configured status](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/478001-479000/478723.png)

![the icon of BLF with speed dial alerting](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/478001-479000/478710.png)

![the icon of BLF with speed dial alerting](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/478001-479000/478715.png)

![the icon for BLF speed dial alerting](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473710.png)

![the line key with an incoming call alerting](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/478001-479000/478725.png)

![the icon of BLF with speed dial in use](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/478001-479000/478709.png)

![the icon of BLF with speed dial in use](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/478001-479000/478716.png)

![the icon for BLF speed dial in use](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473711.png)

![the line key in the busy status](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/478001-479000/478726.png)

![the icon of BLF with speed dial DND](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/478001-479000/478711.png)

![the icon of BLF with speed dial DND](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/478001-479000/478717.png)

![the icon for BLF speed dial DND state](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473712.png)

![The BLF Uncognized icon for 9841](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/482001-483000/482198.png)

![BLF Unrecognized icon for 9851, 9861, and 9871](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/482001-483000/482199.png)

![the icon of speed dial](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/478001-479000/478713.png)

![the icon of speed dial](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/478001-479000/478719.png)

![the icon for BLF speed dial unregistered](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473713.png)

![Add speed dial button](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/495001-496000/495356.png)

![Select phone number to add as a speed dial](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/495001-496000/495357.jpg)

![Adding a custom contact as speed dial](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/495001-496000/495358.jpg)

![Manage Speed dials](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/495001-496000/495359.png)

![the Edit icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/474001-475000/474131.png)

![the Delete icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/474001-475000/474232.png)