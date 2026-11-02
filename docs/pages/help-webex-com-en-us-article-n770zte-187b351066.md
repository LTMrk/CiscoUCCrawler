---
doc_id: help-webex-com-en-us-article-n770zte-187b351066
source_url: https://help.webex.com/en-us/article/n770zte
retrieved_at: 2026-11-02T13:06:07.006645+00:00
---

## Feature line keys and softkeys

Configure feature line keys and feature softkeys for your phones so the users can access the features easily on the phone.

### Feature Line keys

On Cisco Desk Phone 9811, 9841, 9851, and 9861, a feature line key displays as a separate line on the phone. In this way, users can
        quickly use the assigned feature by pressing the line key button.

On Cisco Desk Phone 9871 and Cisco Video Phone 8875, a feature line key displays as a separate line on the right part of the phone home screen. Typically, the feature line keys display underneath the phone lines.

### Feature softkeys

On Cisco Desk Phone 9811, 9841, 9851, and 9861, a feature softkey displays at the bottom of the phone home screen or on a specific
        screen (for example, in-call screen). Users can press the dedicated softkey button to
        perform an action or access a feature.

On Cisco Desk Phone 9871 and Cisco Video Phone 8875, a feature softkey displays as a soft button on the left part of phone home screen or at the bottom of a specific screen (for example, in-call screen). Users can tap the soft button to perform an action or access a feature.

Barge

Remote in use

When the Barge button is configured, it shows on the in-call screen of a shared line.

Call

On Hook

Calls

Off Hook With Feature

Call back

On Hook

Ring Out

Connected Transfer

Use the Call Back (CallBack) softkey in the softkey template to control the button.

Call park

Connected

Call pickup

On Hook

Off Hook

Conference

Conf

Connected

DND

DND off

On Hook

Off Hook

Off Hook With Feature

Ring In

Ring Out

Connected

On Hold

Connected Transfer

Connected Conference

Digits After First

Use the Toggle Do Not Disturb (DND) softkey in the softkey template to control the button.

End call

Ring Out

Connected

Connected Transfer

Connected Conference

FWD all

FWD off

Forward all

Forward off

Group pickup

On Hook

Off Hook

Hold

Hunt group in/out

HG in/out

MCID

Report caller

Meet Me

On Hook

Off Hook

Messages

On Hook

New call

On Hold

Remote in Use

If you want to enable the softkey for the connected call state, see Enable the New call softkey for the phone connected state .

Other pickup

On Hook

Off Hook

Participants

Participant

Connected

Recents

Always displays when the phone is registered.

You can configure the button position using the Recents (Recents) softkey in the softkey template.

Redial

On Hook

Off Hook

Resume

Settings

You can configure the button position using the Applications (Apps) softkey in the softkey template.

Speed dial

Transfer

Connected

Connected Transfer

Connected Conference

Use the Transfer (Trnsfer) softkey in the softkey template to control the button.

## Configure feature softkeys with a softkey template

You can use softkey templates to configure the feature buttons displayed on the phone user interface. Using Cisco Unified Communications Manager Administration, you can set up a template and apply it to phones. Cisco Unified Communications Manager supports the Standard User and Standard Feature softkey template.

An application that supports softkeys has one or more standard softkey templates associated with it. You can apply a standard template to phones or create a new template based on a standard one and modify the settings.

Cisco Unified Communications Manager allows you to configure any softkey in a softkey template, but unsupported softkeys don't display on the phone.

The Call , Contacts , Recents , and Settings softkeys always display on the phone home screen. You can't change the position of the Call softkey.

In Cisco Unified Communications Manager Administration, select Device > Device Settings > Softkey Template .

Perform the following steps to create a new softkey template; otherwise, proceed to the next step.

Click Add New .

Select a default template and click Copy .

Enter a new name for the template in the Softkey Template Name field.

Click Save .

Perform the following steps to add softkeys to an existing template.

Click Find and enter the search criteria.

Select the required existing template.

Check the Default Softkey Template check box to designate this softkey template as the default softkey template.

Choose Configure Softkey Layout from the Related Links drop-down list in the upper right corner and click Go .

From the Select a Call State to Configure drop-down list, choose the call state for which you want the softkey to display.

From the Unselected Softkeys list, choose the softkey to add and click the right arrow to move the softkey to the Selected Softkeys list. Use the up and down arrows to change the position of the new softkeys.

Repeat the Step 6 and 7 to configure the softkey in additional call states.

Click Save .

What to do next

Apply the softkey template to a phone.

## Apply a softkey template to a phone

On Cisco Unified Communications Manager Administration, choose Device > Phone .

Click Find to display the list of configured phones.

Choose the phone to which you want to add the phone button template.

In the Softkey Template drop-down list, choose the template that contains the new feature button.

Click Save .

A message prompts for clicking Reset to update the phone settings.

Click Reset .

## Configure feature line keys with a phone button template

You can use the Phone Button Template on Cisco Unified Communications Manager Administration to configure the feature line keys for different features. Each feature line key takes up
        a line position. You can change the order of the feature.

On Cisco Unified Communications Manager Administration, choose Device > Device Settings > Phone Button Template .

Click Find to display list of supported phone templates.

Perform the following steps if you want to create a new phone button template; otherwise, proceed to the next step.

Select a default template for the model of phone and click Copy .

In the Phone Button Template Information field, enter a new name for the template.

Click Save .

Perform the following steps if you want to add phone buttons to an existing template.

Click Find and enter the search criteria.

Choose an existing template.

From the Line drop-down list, choose feature that you want to add to the template.

Click Save .

Perform one of the following tasks:

- Click Apply
              Config if you modified a template that is already associated with devices
            to restart the devices.

- If you created a new button template, associate the template with the devices and then restart them.

## Apply a button template to a phone

On Cisco Unified Communications Manager Administration, choose Device > Phone .

Click Find to display the list of configured phones.

Choose the phone to which you want to add the phone button template.

In the Phone Button Template drop-down list, choose the phone
          button template that contains the new feature button.

Click Save .

A message prompts for clicking Reset to update the phone
          settings.

Click Reset .

## Configure BLF (Speed Dial and pickup)

You can configure the Busy Lamp Field (BLF) feature to allow the users to monitor the call status of a directory number associated with a speed-dial button on the phone.

When the BLF key is configured with call pickup disabled, the users can monitor the in-use state of the monitored line. The users can also place a call to the monitored line by using the BLF key.

When the BLF key is configured with call pickup enabled, the users can monitor the in-use state and the alerting state of the monitored line. When the monitored line is alerting, the users can pick up the monitored line's alerting call by using the BLF key.

The indicators on the BLF line key vary with different phone models and status. See the following articles for details:

- Use speed dials on your phone

- Answer calls for your coworkers

For more information about how to set up the BLF speed dial and BLF call pickup in Cisco Unified Communications Manager, see Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1) or later .

Add a new call pickup group:

In the Cisco Unified Communications Manager Administration, select Call Routing > Call Pickup Group .

Click Add New .

Configured the required fields Call Pickup Group Name and Call Pickup Group Number in the Call Pickup Group Information section.

Click Save .

The Associated Call Pickup Group Information window appears. In the Current Associated Call Pickup Groups section, ensure that the new call pickup group number is selected.

In the Find Pickup Numbers by Numbers/Partition section, add more existing call pickup groups to associate with the new call pickup group.

Click Save .

Assign the new call pickup group to a directory number:

Select Call Routing > Directory Number .

Find and open a directory number.

In the Call Forward and Call Pickup Settings section, select the new call pickup group from the Call Pickup Group drop-down list.

Click Save .

Click Apply Config .

Configure BLF speed dial and call pickup for the directory number:

Select Device > Phone .

Locate the phone that you will set up.

In the left Association section, click Modify Button Items .

Select and add the item Add a new BLF SD from the Unassigned Associated Items to the Associated Items section.

Click Save .

Navigate to the Association section of the phone, click Add a new BLF SD .

The Busy Lamp Field Speed Dial Configuration window appears.

Find and select the configured directory number from the Directory Number drop-down list, and enter a label for the directory number.

Check the Call Pickup check box to use the BLF speed dial and call pickup.  Then the users can answer incoming calls for the monitored line.

To make sure that the call pickup feature works, the primary line of the monitoring phone must be in the same call pickup group as the monitored directory number.

Click Save .

## Enable or disable BLF audio notification

You can enable or disable the audio notification of incoming calls for the Busy Lamp Field (BLF) monitored line in different situations.

In Unified Communications Manager Administration, select System > Service Parameter .

Select a node from the Server drop-down list.

Select Cisco CallManager from the Service drop-down list.

In the Clusterwide Parameters (Device - Phone) section, configure the following parameters:

Default value: Default .

Default value: Default .

In the Clusterwide Parameters(System - Presence) section, configure the parameter BLF Status Depicts DND .

- True : The monitoring BLF key can show the DND status of the monitored line.

- False (default): The monitoring BLF key doesn't show the DND status of the monitored line, and can only show the busy or idle status of it.

Click Save .

Select Device > Phone .

Locate the phone that you will set up.

In the Device Information section, set the following parameters:

BLF Audible Alert Setting (Phone Idle) : Select On or Off to enable or disable the
                audible alert sounds when no current call exists on the BLF monitored phone.

Default value: Default . The configuration of the parameter BLF Pickup Audio Alert Setting of Idle Station in Service
                Parameter determines the alert option.

BLF Audible Alert Setting (Phone Busy) : Select On or Off to enable or disable the
                audible alert sounds when at least one active call exists on the BLF monitored line,
                but no call pickup alerts exist.

Default value: Default . The configuration of the parameter BLF Pickup Audio Alert Setting of Busy Station in Service
                Parameter determines the alert option.

Click Save .

Click Apply Config .

## Enable the New call softkey for the phone connected state

Before the PhoneOS 3.5 release (including 3.4 and earlier versions), the New call softkey is always positioned in the third place when the phone is in the connected call state. Meanwhile, other softkeys (except for the first and second softkeys) will shift to subsequent positions.

From the PhoneOS 3.5 release, the softkey doesn't display on the phone screen by default during the connected state. To enable the softkey during the state, set the New Call Softkey for Connected Call State field to "Enabled" in Unified CM. Note that the New call softkey is controlled by this field instead of the softkey template.

Do one of the following actions from Cisco Unified CM Administration:

Choose Device > Phone , and locate the phone that you want to set up.

Choose Device > Device Settings > Common Phone Profile , and locate the profile that you want to set up.

Choose System > Enterprise Phone Configuration .

The precedence order is: Phone > Common phone profile > Enterprise phone configuration.

Set up the field New Call Softkey for Connected Call State .

- Disabled (default): The New call softkey doesn't display when the phone is in the connected call state.

- Enabled: The New call softkey can display when the phone is in the connected call state.

Click Save .

| Feature name | Description |
|---|---|
| BLF with Call Park | Use the Call Park BLF feature in the phone button template to control this shortcut. |
| BLF with Call Pickup | Use the Speed Dial BLF feature in the phone button template and enable the checkbox Call Pickup in the Busy Lamp Field Speed Dial Configuration window to control this shortcut. |
| BLF with Speed Dial | Use the Speed Dial BLF feature in the phone button template to control this shortcut. |
| Call Park | Use the Call Park feature in the phone button template
                to control this shortcut. |
| Call Pickup | Use the Call Pickup feature in the phone button template
                to control this shortcut. |
| DND | Use the Do Not Disturb feature in the phone button template to control this shortcut. |
| Group Pickup | Use the Group Call Pickup feature in the phone button
                template to control this shortcut. |
| Hunt Group | Use the Hunt Group Logout feature in the phone button template to control this shortcut. |
| Intercom | Use the Intercom feature in the phone button template to control this shortcut. |
| Malicious Call Identification | Use the Malicious Call Identification feature in the
                phone button template to control this shortcut. |
| Meet Me | Use the Meet Me Conference feature in the phone button template to control this shortcut. |
| Other Pickup | Use the Other Pickup feature in the phone button
                template to control this shortcut. |
| Privacy | Use the Privacy feature in the phone button template to control this shortcut. |
| Queue Status | Use the Queue Status feature in the phone button template to control this shortcut. |
| Redial | Use the Redial feature in the phone button template to control this shortcut. |
| Speed Dial | Use the Speed Dial feature in the phone button template to control this shortcut. |
| XSI Service | Use the Service URL feature in the phone button template to control this shortcut. |

| Feature button label | Phone state | Description |
|---|---|---|
| Barge | Remote in use | Use the Barge or Conference Barge softkey in the softkey template to control the button. When the Barge button is configured, it shows on the in-call screen of a shared line. |
| Call | On Hook | Always displays at the first position when the phone is registered, regardless
                of its position in the softkey template. Its corresponding template option is **NewCall (NewCall) . |
| Calls | Off Hook With Feature | If the phone has held call(s), the softkey displays in the Transfer or Conference screen when the user tries to transfer a call or create a conference. |
| Call back | On Hook Ring Out Connected Transfer | Use the Call Back (CallBack) softkey in the softkey template to control the button. |
| Call park | Connected | Use the Park (Park) softkey in the softkey template to control the
                button. |
| Call pickup | On Hook Off Hook | Use the Pick Up (PickUp) softkey in the softkey template to control the
                button. |
| Conference Conf | Connected | Use the Conference (Confrn) softkey in the softkey template to control the button. |
| DND DND off | On Hook Off Hook Off Hook With Feature Ring In Ring Out Connected On Hold Connected Transfer Connected Conference Digits After First | Use the Toggle Do Not Disturb (DND) softkey in the softkey template to control the button. |
| End call | Ring Out Connected Connected Transfer Connected Conference | Use the End Call (EndCall) softkey in the softkey template to control this button. You can't specify its position. |
| FWD all FWD off Forward all Forward off | On Hook | Use the Forward All (CfwdAll) softkey in the softkey template to control the button. |
| Group pickup | On Hook Off Hook | Use the Group Pick Up (GPickUp) softkey in the softkey template to
                control this soft button. |
| Hold | Connected | Use the Hold (Hold) softkey in the softkey template to control this soft button. You can't specify its position. |
| Hunt group in/out HG in/out | On Hook | Use the HLog (HLog) softkey in the softkey template to control the button. |
| MCID Report caller | Connected | Use the Toggle Malicious Call Trace (MCID) softkey in the softkey
                template to control the button. |
| Meet Me | On Hook Off Hook | Use the Meet Me (MeetMe) softkey in the softkey template to control the button. |
| Messages | On Hook | Use the Messages (Messages) softkey in the softkey template to control the button. |
| New call | On Hold Remote in Use | Use the NewCall (NewCall) softkey in the softkey template to control the button. If you want to enable the softkey for the connected call state, see Enable the New call softkey for the phone connected state . |
| Other pickup | On Hook Off Hook | Use the Other Pickup (oPickup) softkey in the softkey template to
                control this soft button. |
| Participants Participant | Connected | Use the Conference List (ConfList) softkey in the softkey template to control the button. |
| Recents | On Hook | Always displays when the phone is registered. You can configure the button position using the Recents (Recents) softkey in the softkey template. |
| Redial | On Hook Off Hook | Use the Redial (Redial) softkey in the softkey template to control the button. |
| Resume | On Hold | It's a mandatory softkey in the template. You can't configure it. |
| Settings | On Hook | You can configure the button position using the Applications (Apps) softkey in the softkey template. |
| Speed dial | Off Hook | Provides access to the speed dial list while transferring a call or add a
                participant to a conference call. |
| Transfer | Connected Connected Transfer Connected Conference | Use the Transfer (Trnsfer) softkey in the softkey template to control the button. |

| 1 | In Cisco Unified Communications Manager Administration, select Device > Device Settings > Softkey Template . |
|---|---|
| 2 | Perform the following steps to create a new softkey template; otherwise, proceed to the next step. Click Add New . Select a default template and click Copy . Enter a new name for the template in the Softkey Template Name field. Click Save . |
| 3 | Perform the following steps to add softkeys to an existing template. Click Find and enter the search criteria. Select the required existing template. |
| 4 | Check the Default Softkey Template check box to designate this softkey template as the default softkey template. |
| 5 | Choose Configure Softkey Layout from the Related Links drop-down list in the upper right corner and click Go . |
| 6 | From the Select a Call State to Configure drop-down list, choose the call state for which you want the softkey to display. |
| 7 | From the Unselected Softkeys list, choose the softkey to add and click the right arrow to move the softkey to the Selected Softkeys list. Use the up and down arrows to change the position of the new softkeys. |
| 8 | Repeat the Step 6 and 7 to configure the softkey in additional call states. |
| 9 | Click Save . |

| 1 | On Cisco Unified Communications Manager Administration, choose Device > Phone . |
|---|---|
| 2 | Click Find to display the list of configured phones. |
| 3 | Choose the phone to which you want to add the phone button template. |
| 4 | In the Softkey Template drop-down list, choose the template that contains the new feature button. |
| 5 | Click Save . A message prompts for clicking Reset to update the phone settings. |
| 6 | Click Reset . |

| 1 | On Cisco Unified Communications Manager Administration, choose Device > Device Settings > Phone Button Template . |
|---|---|
| 2 | Click Find to display list of supported phone templates. |
| 3 | Perform the following steps if you want to create a new phone button template; otherwise, proceed to the next step. Select a default template for the model of phone and click Copy . In the Phone Button Template Information field, enter a new name for the template. Click Save . |
| 4 | Perform the following steps if you want to add phone buttons to an existing template. Click Find and enter the search criteria. Choose an existing template. |
| 5 | From the Line drop-down list, choose feature that you want to add to the template. |
| 6 | Click Save . |
| 7 | Perform one of the following tasks: Click Apply
              Config if you modified a template that is already associated with devices
            to restart the devices. If you created a new button template, associate the template with the devices and then restart them. |

| 1 | On Cisco Unified Communications Manager Administration, choose Device > Phone . |
|---|---|
| 2 | Click Find to display the list of configured phones. |
| 3 | Choose the phone to which you want to add the phone button template. |
| 4 | In the Phone Button Template drop-down list, choose the phone
          button template that contains the new feature button. |
| 5 | Click Save . A message prompts for clicking Reset to update the phone
          settings. |
| 6 | Click Reset . |

| 1 | Add a new call pickup group: In the Cisco Unified Communications Manager Administration, select Call Routing > Call Pickup Group . Click Add New . Configured the required fields Call Pickup Group Name and Call Pickup Group Number in the Call Pickup Group Information section. Click Save . The Associated Call Pickup Group Information window appears. In the Current Associated Call Pickup Groups section, ensure that the new call pickup group number is selected. In the Find Pickup Numbers by Numbers/Partition section, add more existing call pickup groups to associate with the new call pickup group. Click Save . |
|---|---|
| 2 | Assign the new call pickup group to a directory number: Select Call Routing > Directory Number . Find and open a directory number. In the Call Forward and Call Pickup Settings section, select the new call pickup group from the Call Pickup Group drop-down list. Click Save . Click Apply Config . |
| 3 | Configure BLF speed dial and call pickup for the directory number: Select Device > Phone . Locate the phone that you will set up. In the left Association section, click Modify Button Items . Select and add the item Add a new BLF SD from the Unassigned Associated Items to the Associated Items section. Click Save . Navigate to the Association section of the phone, click Add a new BLF SD . The Busy Lamp Field Speed Dial Configuration window appears. Find and select the configured directory number from the Directory Number drop-down list, and enter a label for the directory number. Check the Call Pickup check box to use the BLF speed dial and call pickup.  Then the users can answer incoming calls for the monitored line. To make sure that the call pickup feature works, the primary line of the monitoring phone must be in the same call pickup group as the monitored directory number. Click Save . |

| 1 | In Unified Communications Manager Administration, select System > Service Parameter . |
|---|---|
| 2 | Select a node from the Server drop-down list. |
| 3 | Select Cisco CallManager from the Service drop-down list. |
| 4 | In the Clusterwide Parameters (Device - Phone) section, configure the following parameters: BLF Pickup Audio Alert Setting of Idle Station : Select Play Tone or Disable to enable or
              disable the audio alert when the BLF monitored phone receives an incoming call and the
              phone is idle. Default value: Default . BLF Pickup Audio Alert Setting of Busy Station : Select Play Tone or Disable to enable or
              disable the audio alert when the BLF monitored line receives an incoming call and the
              phone is busy. Default value: Default . |
| 5 | In the Clusterwide Parameters(System - Presence) section, configure the parameter BLF Status Depicts DND . True : The monitoring BLF key can show the DND status of the monitored line. False (default): The monitoring BLF key doesn't show the DND status of the monitored line, and can only show the busy or idle status of it. |
| 6 | Click Save . |
| 7 | Select Device > Phone . |
| 8 | Locate the phone that you will set up. |
| 9 | In the Device Information section, set the following parameters: BLF Audible Alert Setting (Phone Idle) : Select On or Off to enable or disable the
                audible alert sounds when no current call exists on the BLF monitored phone. Default value: Default . The configuration of the parameter BLF Pickup Audio Alert Setting of Idle Station in Service
                Parameter determines the alert option. BLF Audible Alert Setting (Phone Busy) : Select On or Off to enable or disable the
                audible alert sounds when at least one active call exists on the BLF monitored line,
                but no call pickup alerts exist. Default value: Default . The configuration of the parameter BLF Pickup Audio Alert Setting of Busy Station in Service
                Parameter determines the alert option. |
| 10 | Click Save . |
| 11 | Click Apply Config . |

| 1 | Do one of the following actions from Cisco Unified CM Administration: To set up the feature for a specific phone: Choose Device > Phone , and locate the phone that you want to set up. To set up the feature for a group of phones: Choose Device > Device Settings > Common Phone Profile , and locate the profile that you want to set up. To set up the feature for all phones: Choose System > Enterprise Phone Configuration . The precedence order is: Phone > Common phone profile > Enterprise phone configuration. |
|---|---|
| 2 | Set up the field New Call Softkey for Connected Call State . Disabled (default): The New call softkey doesn't display when the phone is in the connected call state. Enabled: The New call softkey can display when the phone is in the connected call state. |
| 3 | Click Save . |