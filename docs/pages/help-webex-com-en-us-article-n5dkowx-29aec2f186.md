---
doc_id: help-webex-com-en-us-article-n5dkowx-29aec2f186
source_url: https://help.webex.com/en-us/article/n5dkowx
retrieved_at: 2026-11-02T13:11:29.378370+00:00
---

- 9841 / 9851 / 9861

- 9871 / 8875

This feature allows you to manage the mode-based forwarding of the specified features on a
        line key. You can manually switch the operating mode of Call Queues, Hunt Groups, and Auto
        Attendants on your phone. Hence, the incoming calls are effectively routed to different
        destinations based on the operating mode you've selected.

Before you begin

- Your administrator has configured a series of operating modes for the organization and
          locations.

- Your administrator configures five features for line keys and your phone screen displays
          up to five features with respective line keys.

Select a line key.

Do one of the following actions:

Press the Edit mode softkey to select an operating mode.

Press the Navigation cluster, up or down, to switch between the modes. The
                  current switch back mode is displayed on the right side of the mode name.

Press the Details softkey to view detailed time duration
                  of a mode.

Press the Manual on or Manual off softkey to specify how to switch back to the normal operation mode: automatically
                  or manually and then press Set .

For example, an operating mode <Mode name> Automatic switch will be changed
              to <Mode name> Manual switch after you press the Manual on softkey.
              It indicates that the operating mode retains until you manually switch back to a
              normal mode.

Press the Extend softkey to add time extension to an operating mode or retain
              the current operating mode.

Press the Navigation cluster (left or right) or press the < or > softkey to select
                      time extension in minutes. The minimum value is 30 minutes.

Press the Set softkey.

(Optional) After you extend an operating mode, the Extend softkey becomes Edit
                        extend . Press this softkey and then select Switch
                        manually . The current operating mode retains till you manually
                      switch back to a normal mode.

- Select Switch manually . The current operating mode retains till you
                manually switch back to a normal mode.

- You cannot extend an operating mode that needs to be switched manually back to
                  normal.

- When the current state is not in any mode period, the Extend softkey is
                  disabled.

Press the All features softkey for batch edit.

Press Batch edit to list all features except the ones with
                  mode-based forwarding disabled.

Press the Navigation cluster, up or down, to switch between the features, and
                  then press Select to select one or more features.
                  Alternatively, select All features .

Press the Edit mode softkey to select an operating
                  mode.

Only common operating modes will be displayed for batch edit. If there are no
                  common modes available, the phone displays an alert.

Press the Set softkey.

By default, the operating status is set to Switch manually for the mode you
              have selected during batch editing.

- Press the Revert mode softkey to return to the normal operating mode if
            this operating mode has a time extension or has been set to switch manually.

This feature allows you to manage the mode-based forwarding of the specified features on a
        line key. You can manually switch the operating mode of Call Queues, Hunt Groups, and Auto
        Attendants on your phone. Hence, the incoming calls are effectively routed to different
        destinations based on the operating mode you've selected.

Before you begin

- Your administrator has configured a series of operating modes for the organization and
          locations.

- Your administrator configures five features for line keys and your phone screen displays
          up to five features with respective line keys.

Press a line key.

Do one of the following actions:

Tap Edit mode .

Tap to select a mode. The current switch back mode is displayed on the right side
                  of the mode name.

Tap the blue exclamation mark icon next to the selected mode to view detailed
                  time duration of a mode.

Toggle Manual switch on or off to specify how to switch
                  back to the normal operation mode: automatically or manually and then tap Set .

For example, an operating mode <Mode name> Automatic switch will be changed
              to <Mode name> Manual switch after you press the Manual on softkey.
              It indicates that the operating mode retains until you manually switch back to a
              normal mode.

Tap Extend to add time extension to an operating mode or retain the current
              operating mode.

Tap < or > to select time
                      extension in minutes. The minimum value is 30 minutes.

Tap Set .

(Optional) After you extend an operating mode, the Extend menu becomes Edit
                        extend . Tap Edit extend and then tap Switch manually . The current operating mode retains
                      till you manually switch back to a normal mode.

- Tap Switch manually . The current operating mode retains till you manually
                switch back to a normal mode.

- You cannot extend an operating mode that needs to be switched manually back to
                  normal.

- When the current state is not in any mode period, the Extend softkey is disabled.

Tap All features for batch edit.

Select Batch edit to list all features except the ones
                  with mode-based forwarding disabled.

Tap to select one or more features. Alternatively, tap All
                    features .

Tap Edit mode to select an operating mode.

Only common operating modes will be displayed for batch edit. If there are no
                  common modes available, the phone displays an alert.

Tap Set .

By default, the operating status is set to Switch manually for the mode you
              have selected during batch editing.

- Tap Revert to return to the normal operating mode if this operating mode
            has a time extension or has been set to switch manually.

## LED colors and icons

On 9841, 9851, and 9861, your phone screen displays features with line keys illuminate to
        indicate the operating mode status. On 9871 and 8875, the features are displayed together
        with status icons. The following table describes the default operating modes, the associated
        LED colors displayed on the line keys, and status icons.

Color

Line keys  (9841, 9851, and 9861)

Description

Green (steady)

Normal operating mode

The current routing follows the normal operating mode, even if in some periods
                  there is no operating mode configured by your administrator. The feature's
                  operating mode switches automatically under the following circumstances:

- The current mode reaches its end time.

- A higher precedence mode reaches its start time.

Amber (steady)

Automatic switch back exception (Start early)

You have switched the feature to an operating mode before its start time. This
                  mode runs as an exception until its start time is reached. At this point, the mode
                  automatically switches the feature back to normal operation.

Automatic switch back exception (Extended)

You have extended the operating mode before it reaches its end time. This mode
                  runs as an exception until the extension end time is reached. That is, the mode's
                  end time plus an extension of up to 12 hours. At this point, the mode
                  automatically switches the feature back to normal operation.

Automatic switch back exception (Exception)

You have switched the feature to another operating mode that is running in its
                  scheduled time, but the original operating mode takes precedence. The mode runs as
                  an exception until its end time is reached. At this point, the mode automatically
                  switches the feature back to normal operation.

For example, there are Mode A (8 AM to 5 PM) and Mode B (12 PM to 1 PM). The
                  administrator sets Mode B to have precedence over Mode A. Hence, the system
                  operates in Mode B from 12 PM to 1 PM. If you switch Mode B to Mode A during this
                  period, this exception occurs. In this exception state, Mode A remains active
                  until 5 PM.

Red (steady)

Manual switch back exception (Switch manually)

You have switched the operating mode or extended the mode for manual switch back.
                  The operating mode runs as an exception until you manually switches the feature
                  back to normal operation or a different mode.

Gray (Off)

Mode-based fwd disabled

One of the following scenarios occurs:

- There is no operating mode associated with the feature.

- Mode-based forwarding is disabled.

- Your phone doesn’t receive a response from the server.

Unrecognized

| 1 | Select a line key. |
|---|---|
| 2 | Do one of the following actions: Press the Edit mode softkey to select an operating mode. Press the Navigation cluster, up or down, to switch between the modes. The
                  current switch back mode is displayed on the right side of the mode name. Press the Details softkey to view detailed time duration
                  of a mode. Press the Manual on or Manual off softkey to specify how to switch back to the normal operation mode: automatically
                  or manually and then press Set . For example, an operating mode <Mode name> Automatic switch will be changed
              to <Mode name> Manual switch after you press the Manual on softkey.
              It indicates that the operating mode retains until you manually switch back to a
              normal mode. Press the Extend softkey to add time extension to an operating mode or retain
              the current operating mode. Select Specify duration to add time extension to an operating mode. Press the Navigation cluster (left or right) or press the < or > softkey to select
                      time extension in minutes. The minimum value is 30 minutes. Press the Set softkey. (Optional) After you extend an operating mode, the Extend softkey becomes Edit
                        extend . Press this softkey and then select Switch
                        manually . The current operating mode retains till you manually
                      switch back to a normal mode. Select Switch manually . The current operating mode retains till you
                manually switch back to a normal mode. You cannot extend an operating mode that needs to be switched manually back to
                  normal. When the current state is not in any mode period, the Extend softkey is
                  disabled. Press the All features softkey for batch edit. Press Batch edit to list all features except the ones with
                  mode-based forwarding disabled. Press the Navigation cluster, up or down, to switch between the features, and
                  then press Select to select one or more features.
                  Alternatively, select All features . Press the Edit mode softkey to select an operating
                  mode. Only common operating modes will be displayed for batch edit. If there are no
                  common modes available, the phone displays an alert. Press the Set softkey. By default, the operating status is set to Switch manually for the mode you
              have selected during batch editing. Press the Revert mode softkey to return to the normal operating mode if
            this operating mode has a time extension or has been set to switch manually. |

| 1 | Press a line key. |
|---|---|
| 2 | Do one of the following actions: Tap Edit mode . Tap to select a mode. The current switch back mode is displayed on the right side
                  of the mode name. Tap the blue exclamation mark icon next to the selected mode to view detailed
                  time duration of a mode. Toggle Manual switch on or off to specify how to switch
                  back to the normal operation mode: automatically or manually and then tap Set . For example, an operating mode <Mode name> Automatic switch will be changed
              to <Mode name> Manual switch after you press the Manual on softkey.
              It indicates that the operating mode retains until you manually switch back to a
              normal mode. Tap Extend to add time extension to an operating mode or retain the current
              operating mode. Tap Specify duration to add time extension to an operating mode. Tap < or > to select time
                      extension in minutes. The minimum value is 30 minutes. Tap Set . (Optional) After you extend an operating mode, the Extend menu becomes Edit
                        extend . Tap Edit extend and then tap Switch manually . The current operating mode retains
                      till you manually switch back to a normal mode. Tap Switch manually . The current operating mode retains till you manually
                switch back to a normal mode. You cannot extend an operating mode that needs to be switched manually back to
                  normal. When the current state is not in any mode period, the Extend softkey is disabled. Tap All features for batch edit. Select Batch edit to list all features except the ones
                  with mode-based forwarding disabled. Tap to select one or more features. Alternatively, tap All
                    features . Tap Edit mode to select an operating mode. Only common operating modes will be displayed for batch edit. If there are no
                  common modes available, the phone displays an alert. Tap Set . By default, the operating status is set to Switch manually for the mode you
              have selected during batch editing. Tap Revert to return to the normal operating mode if this operating mode
            has a time extension or has been set to switch manually. |

| Color | Line keys  (9841, 9851, and 9861) | Status icons (9871 and 8875) | Operating Mode Status | Description |
|---|---|---|---|---|
| Green (steady) |  |  | Normal operating mode | The current routing follows the normal operating mode, even if in some periods
                  there is no operating mode configured by your administrator. The feature's
                  operating mode switches automatically under the following circumstances: The current mode reaches its end time. A higher precedence mode reaches its start time. |
| Amber (steady) |  |  | Automatic switch back exception (Start early) | You have switched the feature to an operating mode before its start time. This
                  mode runs as an exception until its start time is reached. At this point, the mode
                  automatically switches the feature back to normal operation. |
| Automatic switch back exception (Extended) | You have extended the operating mode before it reaches its end time. This mode
                  runs as an exception until the extension end time is reached. That is, the mode's
                  end time plus an extension of up to 12 hours. At this point, the mode
                  automatically switches the feature back to normal operation. |
| Automatic switch back exception (Exception) | You have switched the feature to another operating mode that is running in its
                  scheduled time, but the original operating mode takes precedence. The mode runs as
                  an exception until its end time is reached. At this point, the mode automatically
                  switches the feature back to normal operation. For example, there are Mode A (8 AM to 5 PM) and Mode B (12 PM to 1 PM). The
                  administrator sets Mode B to have precedence over Mode A. Hence, the system
                  operates in Mode B from 12 PM to 1 PM. If you switch Mode B to Mode A during this
                  period, this exception occurs. In this exception state, Mode A remains active
                  until 5 PM. |
| Red (steady) |  |  | Manual switch back exception (Switch manually) | You have switched the operating mode or extended the mode for manual switch back.
                  The operating mode runs as an exception until you manually switches the feature
                  back to normal operation or a different mode. |
| Gray (Off) |  |  | Mode-based fwd disabled | One of the following scenarios occurs: There is no operating mode associated with the feature. Mode-based forwarding is disabled. Your phone doesn’t receive a response from the server. |
|  | Unrecognized |

## Figuras

![Operating mode line key with green LED](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/491001-492000/491941.png)

![Operating mode with green status icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/491001-492000/491942.png)

![Operating mode line key with amber LED](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/491001-492000/491943.png)

![Operating mode with amber status icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/491001-492000/491944.png)

![Operating mode line key with red LED](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/491001-492000/491945.png)

![Operating mode with red status icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/491001-492000/491946.png)

![Operating mode line key with LED off](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/491001-492000/491947.png)

![Operating mode with Disabled status icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/491001-492000/491948.png)

![Operating mode with Unrecognized status icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/491001-492000/491949.png)