---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-cucm-b-feature-configuration-guide-for-15-cucm-mp-d811ea0d-00-do--9c602ddc84
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/cucm_b_feature-configuration-guide-for-15/cucm_mp_d811ea0d_00_do-not-disturb-12-0.html
retrieved_at: 2026-08-16T16:05:16.837297+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: March 26, 2026

Chapter: Do Not Disturb

## Chapter: Do Not Disturb

# Do Not Disturb

## Do Not Disturb
                        	 Overview

Do Not Disturb (DND)
                           		provides the following options:

Call Reject—This
                                 			 option specifies that the incoming call gets rejected. Depending on how you
                                 			 configure the DND Incoming Call Alert parameter, the phone may play a beep, or
                                 			 display a flash notification of the call.

- Ringer Off—This option
                              		  turns off the ringer, but incoming call information gets presented to the
                              		  device, so that the user can accept the call.

When DND is enabled,
                           		all new incoming calls with normal priority honor the DND settings for the
                           		device. High-priority calls, such as Cisco Emergency Responder (CER) calls, or
                           		calls with Multilevel Precedence and Preemption (MLPP), ring on the device.
                           		Also, when you enable DND, the Auto Answer feature gets disabled.

Users can activate
                           		Do Not Disturb on the phone in the following ways:

- Softkey

- Feature button

- Cisco Unified
                              		  Communications Self-Care Portal

### Phone
                              		  Behavior

When you enable Do
                              		  Not Disturb, the Cisco Unified IP Phone displays the message "Do Not Disturb
                                 			 is active" . Some Cisco Unified IP Phones display DND status icons. For
                              		  details on how individual phone models use Do Not Disturb, consult the user
                              		  guide for that particular phone model.

When you activate
                              		  DND, you can still receive incoming call notifications on the phone as
                              		  specified by the Incoming Call Alert settings in Cisco Unified Communications
                              		  Manager Administration, but the phone will not ring, except for high-priority
                              		  calls (such as Cisco Emergency Responder and MLPP calls). Also, if you enable
                              		  DND while the phone is ringing, the phone stops ringing.

### Status
                              		  Notifications

Do Not Disturb is
                              		  supported on both SIP and Cisco Skinny Call Control Protocol (SCCP) devices.

SIP phones use
                              		  the SIP PUBLISH method to signal a DND status change to Cisco Unified
                              		  Communications Manager. Cisco Unified Communications Manager uses a Remote-cc
                              		  REFER request to signal a DND status change to the SIP phone.

SCCP phones use
                              		  SCCP messaging to signal a DND status change to Cisco Unified Communications
                              		  Manager.

## Do Not Disturb
                        	 Configuration Task Flow

Step 1

Generate a Phone Feature List

Run a Phone
                                          				Feature List report from Cisco Unified Reporting to determine which phones
                                          				support Do Not Disturb.

Cisco
                                                      				  Unified IP Phones 7940 and 7960 that are running SIP use their own
                                                      				  backwards-compatible implementation of Do Not Disturb, which you configure on
                                                      				  the SIP Profile.

Step 2

Configure Busy Lamp Field Status

Step 3

Configure Do Not Disturb on a Common Phone Profile

Step 4

Apply Do Not Disturb Settings to the Phone .

Step 5

Depending on
                                       			 whether your phone uses softkeys or feature buttons, perform either of the
                                       			 following tasks:

- Configure a Do Not Disturb Feature Button

- Configure a Do Not Disturb Softkey

Add a Do Not
                                          				Disturb feature button or softkey to your phone.

### Configure Busy Lamp Field Status

You can configure how the BLF status depicts Do Not Disturb by setting the BLF Status Depects DND service parameter. To set the BLF status, do the following:

#### Before you begin

Busy Lamp Field (BLF) presence status for DND works only when all the registered devices for that shared line DN are set to
                                                   DND.

If you're using Jabber for iOS or Jabber for Android on the same DN, they are considered registered, even when they are not
                                                   registered but just configured.

Generate a Phone Feature List

Step 1

In Cisco
                                          			 Unified CM Administration, choose System > Service
                                                				  Parameters .

Step 2

Choose the Cisco
                                             				CallManager service for the server that you want to configure.

Step 3

In the
                                          			 Clusterwide Parameters (System - Presence) pane, specify one of the following
                                          			 values for the BLF
                                             				Status Depicts DND service parameter:

- True —If Do Not
                                             				Disturb is activated on the device, the BLF status indicator for the device or
                                             				line appearance reflects the Do Not Disturb state.

- False —If Do Not
                                             				Disturb is activated on the device, the BLF status indicator for the device or
                                             				line appearance reflects the actual device state.

#### What to do next

Perform one of the
                                 		  following procedures:

Configure Do Not Disturb on a Common Phone Profile

Apply Do Not Disturb Settings to the Phone

### Configure Do Not Disturb on a Common Phone Profile

Common Phone Profiles allow you to configure Do Not Disturb settings and then apply those settings to a group of phones in
                                 your network that use that profile.

#### Before you begin

Configure Busy Lamp Field Status

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Common Phone Profile .

Step 2

From the DND Option drop-down list, choose how you want the Do Not Disturb feature to handle incoming calls.

- Call Reject —No incoming call information gets presented to the user. Depending on how you configure the DND Incoming Call Alert parameter,
                                             the phone may play a beep or display a flash notification of the call.

- Ringer Off —This option turns off the ringer, but incoming call information gets presented to the device, so the user can accept the
                                             call.

For mobile phones and dual-mode phones, you can only choose the Call Reject option.

Step 3

From the Incoming Call Alert drop-down list, choose how you want to alert phone users of incoming calls while Do Not Disturb is turned on.

- Disable —Both beep and flash notification of a call are for disabled. If you configured the DND Ringer Off option, incoming call information
                                             still gets displayed. However, for the DND Call Reject option, no call alerts display, and no information gets sent to the
                                             device.

- Flash Only —The phone flashes for incoming calls.

- Beep Only —The phone displays a flash alert for incoming calls.

Step 4

Click Save .

### Apply Do Not
                           	 Disturb Settings to the Phone

This procedure
                                 		  describes how to apply Do Not Disturb settings on your Cisco Unified IP Phones.
                                 		  You can apply DND settings through the Phone Configuration window in Cisco
                                 		  Unified CM Administration, or you can apply DND settings to a Common Phone
                                 		  Profile and then apply that profile to your phone.

#### Before you begin

If you are using a Common Phone Profile, complete Configure Do Not Disturb on a Common Phone Profile .

Otherwise, complete Configure Busy Lamp Field Status

Step 1

From Cisco
                                          			 Unified CM Administration, choose Device > Phone

Step 2

Click Find and select the phone on which you want to configure Do Not Disturb.

Step 3

If you want to apply Do Not Disturb settings from a Common Phone Profile, from the Common Phone Profile drop-down list, choose the profile on which you have configured Do Not Disturb.

Step 4

Check the Do Not
                                             				Disturb check box to enable Do Not Disturb on the phone.

Step 5

In the DND Option drop-down list, specify from the following options how you want the DND feature to handle incoming calls.

- Call Reject —No incoming call information gets presented to the user. Depending on the configuration, the phone either plays a beep or
                                             displays a flash notification.

- Ringer Off —Incoming call information gets presented to the device so that the user can accept the call, but the ringer is turned off.

- Use Common Profile Setting —The Do Not Disturb setting for the Common Phone Profile that is specified for this device gets used.

Step 6

In the DND Incoming Call Alert drop-down list, specify from the following options how you want the phone to display an incoming call when DND is turned
                                          on.

- None —The DND Incoming Call Alert setting from the Common Phone Profile gets used for this device.

- Disable —For DND Ringer Off, both beep and flash notifications are disabled, but incoming call information is still displayed. For
                                             Call Reject, beep and flash notifications are disabled, and no incoming call information gets passed to the device.

- Beep only —For incoming calls, the phone plays a beep tone only.

- Flash only —For incoming calls, the phone displays a flash alert.

Step 7

Click Save .

#### What to do next

Complete either of the following procedures:

Configure a Do Not Disturb Feature Button

Configure a Do Not Disturb Softkey

### Configure a Do Not Disturb Feature Button

Follow these steps to add a Do Not Disturb feature button to your Cisco Unified IP Phone.

Step 1

Configure Phone Button Template for Do Not Disturb

Create a phone button template that includes the Do Not Disturb button.

Step 2

Associate a Button Template with a Phone

Associate the Do Not Disturb button template to a phone.

#### Configure Phone Button Template for Do Not Disturb

Follow this procedure to configure a phone button template that includes the Do Not Disturb button.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Phone Button Template .

Step 2

Click Find to display list of supported phone templates.

Step 3

Perform the following steps if you want to create a new phone button template; otherwise, proceed to the next step.

Select a default template for the model of phone and click Copy .

In the Phone Button Template Information field, enter a new name for the template.

Click Save .

Step 4

Perform the following steps if you want to add phone buttons to an existing template.

Click Find and enter the search criteria.

Choose an existing template.

Step 5

From the Line drop-down list, choose 
                                             			 feature that you want  to add to the template.

Step 6

Click Save .

Step 7

Perform one
                                             			 of the following tasks:

- Click Apply Config if you modified a template that is already associated with devices to restart the devices.

- If you created a new softkey template, associate the template with the devices and then restart them.

#### Associate Button
                              	 Template with Phone

##### Before you begin

Configure Phone Button Template for Do Not Disturb

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find to display the list of configured phones.

Step 3

Choose the
                                             			 phone to which you want to add the phone button template.

Step 4

In the Phone
                                                				Button Template drop-down list, choose the phone button template
                                             			 that contains the new feature button.

Step 5

Click Save .

### Configure a Do Not Disturb
                           	 Softkey

Optional. If your phone uses softkeys, perform the tasks in the following task flow to add a Do Not Disturb
                                 		  softkey to the phone.

Step 1

Configure Softkey Template for Do Not Disturb

Create a softkey template that includes the Do Not Disturb softkey.

Step 2

Perform either  of the following procedures:

- Associate a Softkey Template with a Common Device Configuration

- Associate Softkey Template with a Phone

You can associate the softkey to a Common Device Configuration and then associate that configuration to a group of  phones,
                                             or you can associate the softkey template directly to a phone.

#### Configure Softkey Template for Do Not Disturb

Perform these steps to configure a softkey template that includes the Do Not Disturb softkey.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Softkey Template .

Step 2

Perform the following steps to create a new softkey template; otherwise, proceed to the next step.

Click Add New .

Select a default template and click Copy .

Enter a new name for the template in the Softkey Template Name field.

Click Save .

Step 3

Perform the following steps to add softkeys to an existing template.

Click Find and enter the search criteria.

Select the required existing template.

Step 4

Check the Default Softkey Template check box to designate this softkey template as the default softkey template.

If you
                                                            				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                            designation.

Step 5

Choose Configure Softkey Layout from the Related Links drop-down list in the upper right
                                             			 corner and click Go .

Step 6

From the Select
                                                				a Call State to Configure drop-down list, choose the call state for
                                             			 which you want the softkey to display.

Step 7

From the Unselected Softkeys list, choose the softkey to add and click the right arrow to move the softkey to the Selected Softkeys list. Use the up and down arrows
                                             			 to change the position of the new softkey.

Step 8

Repeat the previous step to display the softkey in additional call states.

Step 9

Click Save .

Step 10

Perform one
                                             			 of the following tasks:

- Click Apply Config if you modified a template that is already associated with devices to restart the devices.

- If you created a new softkey template, associate the template with the devices and then restart them. For more information,
                                                see Add a Softkey Template to a Common Device Configuration and Associate a Softkey Template with a Phone sections.

##### What to do next

Perform one of the following procedures to add the softkey template to a phone.

Associate a Softkey Template with a Common Device Configuration

Associate Softkey Template with a Phone

#### Associate a Softkey Template with a Common Device Configuration

When you associate the Do Not Disturb (DND) softkey template to a Common Device Configuration you can add the DND softkey
                                    to a group of Cisco Unified IP Phones that use that Common Device Configuration.

##### Before you begin

Configure Softkey Template for Do Not Disturb

Step 1

Add Softkey Template to Common Device Configuration

Associate the DND softkey template to a Common Device Configuration.

Step 2

Associate Common Device Configuration with Phone

Add the DND softkey to a phone by associating the Common Device Configuration to the phone.

##### Add Softkey Template to Common Device Configuration

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Common Device Configuration .

Step 2

Perform the following steps to create a new Common Device Configuration and associate the softkey template with it; otherwise,
                                                proceed to the next step.

Click Add New .

Enter a name for the Common Device Configuration in the Name field.

Click Save .

Step 3

Perform the following steps to add the softkey template to an existing Common Device Configuration.

Click Find and enter the search criteria.

Click an existing Common Device Configuration.

Step 4

In the Softkey Template drop-down list, choose the softkey
                                                			 template that contains the softkey that you want to make available.

Step 5

Click Save .

Step 6

Perform one
                                                			 of the following tasks:

- If you modified a Common Device Configuration that is already associated with devices, click Apply Config to restart the devices.

- If you created a new Common Device Configuration, associate the configuration with devices and then restart them.

##### Associate Common Device Configuration with Phone

###### Before you begin

Associate a Softkey Template with a Common Device Configuration

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find and select the phone device to add the softkey template.

Step 3

From the Common Device Configuration drop-down list, choose
                                                				  the common device configuration that contains the new softkey template.

Step 4

Click Save .

Step 5

Click Reset to update the phone settings.

#### Associate Softkey Template with a Phone

Perform this procedure if you have configured a softkey template with the Do Not Disturb softkey and you want to associate
                                    that softkey template to a phone.

##### Before you begin

Configure Softkey Template for Do Not Disturb

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find to select the phone to add the softkey template.

Step 3

From the Softkey Template drop-down list, choose the template that contains the new softkey.

Step 4

Click Save .

Step 5

Press Reset to update the phone settings.

## Do Not Disturb Interactions and Restrictions

This section provides information about Do Not Disturb interactions and restrictions.

### Interactions

The following
                                 		  table describes feature interactions with the Do Not Disturb (DND) feature.
                                 		  Unless otherwise stated, the interactions apply to both the DND Ringer Off and
                                 		  the DND Call Reject option.

Feature

Interaction with Do Not Disturb

Call
                                             						Forward All

On Cisco
                                             						Unified IP Phones, the message that indicates that the Do Not Disturb (DND)
                                             						feature is active takes priority over the message that indicates that the user
                                             						has new voice messages. However, the message that indicates that the Call
                                             						Forward All feature is active has a higher priority than DND.

Park
                                             						Reversion

For
                                             						locally parked calls, Park Reversion overrides DND. If Phone A has DND turned
                                             						on, and a call is parked, the park reversion to Phone A occurs and Phone A
                                             						rings.

For
                                             						remotely parked calls, DND overrides Park Reversion:

If
                                                   							 Phone A activates DND Ringer Off and shares a line with Phone A-prime, when
                                                   							 Phone A-prime parks the call, park reversion on Phone A honors the DND settings
                                                   							 and does not ring.

If Phone A activated DND Call Reject, the park reversion is not presented to Phone A.

Pickup

For
                                             						locally placed Pickup requests, Pickup overrides DND. If Phone A has DND turned
                                             						on, and has initiated any type of Pickup, the Pickup call presents normally,
                                             						and Phone A rings.

For
                                             						remotely placed Pickup requests, DND overrides Pickup as follows:

If
                                                   							 Phone A is in DND Ringer Off mode and shares a line with Phone A-prime, when
                                                   							 Phone A-prime initiates Pickup, the Pickup call to Phone A honors the DND
                                                   							 settings and Phone A does not ring.

If
                                                   							 Phone A is in DND Call Reject mode, the Pickup call is not presented to Phone
                                                   							 A.

Hold
                                             						Reversion and Intercom

Hold
                                             						Reversion and Intercom override DND, and the call gets presented normally.

MLPP and
                                             						CER

Multilevel Precedence and Preemption (phones that are running SCCP) and Cisco Emergency Responder calls override DND. Multilevel
                                             Precedence and Preemption and Cisco Emergency Responder calls get presented normally, and the phone ring is supported on both
                                             SCCP and SIP.

Call
                                             						Back

For the
                                             						originating side, callback overrides DND. When the activating device is on DND
                                             						mode, the callback notification (both audio and visual) is still presented to
                                             						the user.

For the
                                             						terminating side, DND overrides callback as follows:

When the terminating side is on DND Ringer Off, the Callback Available screen is sent after the terminating side goes off
                                                   hook and on hook.

When the terminating side is on DND Call Reject, and is available, a new screen is sent to the activating device as "<DirectoryNumber>
                                                   has become available but is on DND-R" if the activating device is in same cluster. Callback available notification is sent
                                                   only after the terminating side disables DND Call Reject.

Pickup
                                             						Notification

For the
                                             						DND Ringer Off option, only visual notification gets presented to the device.

For the
                                             						DND Call Reject option, no notification gets presented to the device.

Hunt
                                             						List

If a
                                             						device in a Hunt List has DND Ringer Off activated, the call is still presented
                                             						to the user. However, the DND Incoming Call Alert settings would still apply.

If a
                                             						device in a Hunt List has DND Call Reject activated, any calls to that Hunt
                                             						List will go to the next member and will not get sent to this device.

Extension Mobility

For
                                             						Extension Mobility, the device profile settings include DND incoming call alert
                                             						and DND status. When a user logs in and enables DND, the DND incoming call
                                             						alert and DND status settings get saved, and these settings get used when the
                                             						user logs in again.

### Restrictions

Some restrictions apply to DND usage, depending on the phone or device type in use.

The following phone models and devices that are running SCCP support only the DND Ringer Off option:

Cisco Unified IP Phone 7940

Cisco Unified IP Phone 7960

Cisco IP Communicator

Cisco Unified IP Phones 7940 and 7960 that run SIP use their own implementation of Do Not Disturb, which is backward compatible.

The following phone models and devices support only the DND Call Reject option:

Mobile devices (dual mode)

Remote Destination Profile

Cisco Unified Mobile Communicator

## Do Not Disturb Troubleshooting

This section
                              		  provides troubleshooting information for Cisco Unified IP Phones (SCCP and
                              		  SIP).

For SIP phones,
                              		  use the following information for troubleshooting:

debugs: sip-dnd, sip-messages, dnd-settings

show: config, dnd-settings

sniffer traces

For SCCP phones,
                              		  use the following information for troubleshooting:

debug: jvm all info

sniffer traces

### Troubleshooting Errors

The following
                              		  table describes how to troubleshoot errors with Do No Disturb.

Symptom

Actions

DND
                                          						softkey does not display

or

DND
                                          						feature button does not display

Verify that the softkey or button template for this phone includes DND.

Capture a sniffer trace and verify that the phone gets the correct softkey or button template.

Verify that the phone firmware is Version 8.3(1) or later.

BLF
                                          						speed dial does not show DND status

Verify that the BLF DND is set to enabled in Enterprise parameters.

Capture a sniffer trace and verify that the phone gets the
                                                							 correct notification message.

Verify that the phone firmware is Version 8.3(1) or later.

DND changes are not reflected on the monitoring device.

Check if the BOT/TCT devices are shared line devices with the DND state set to OFF . If the status is set to ON , changes to the DND status on other shared lines will not be reflected.

Make sure the DND status on the BOT/TCT devices is set to OFF to reflect changes in the DND status on the line you want to monitor.

| Note | You can also
                                    		enable or disable the feature on a per-phone basis from within Cisco Unified
                                    		Communications Manager. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Generate a Phone Feature List | Run a Phone
                                          				Feature List report from Cisco Unified Reporting to determine which phones
                                          				support Do Not Disturb. Note Cisco
                                                      				  Unified IP Phones 7940 and 7960 that are running SIP use their own
                                                      				  backwards-compatible implementation of Do Not Disturb, which you configure on
                                                      				  the SIP Profile. | Note | Cisco
                                                      				  Unified IP Phones 7940 and 7960 that are running SIP use their own
                                                      				  backwards-compatible implementation of Do Not Disturb, which you configure on
                                                      				  the SIP Profile. |
| Note | Cisco
                                                      				  Unified IP Phones 7940 and 7960 that are running SIP use their own
                                                      				  backwards-compatible implementation of Do Not Disturb, which you configure on
                                                      				  the SIP Profile. |
| Step 2 | Configure Busy Lamp Field Status | Configure the
                                       			 Busy Lamp Field status service parameter. |
| Step 3 | Configure Do Not Disturb on a Common Phone Profile | Optional.
                                       			 Configure Do Not Disturb against a Common Phone Profile. The profile allows you
                                       			 to apply Do Not Disturb settings to a group of phones in your network. |
| Step 4 | Apply Do Not Disturb Settings to the Phone . | Apply Do Not
                                       			 Disturb settings to the phone. |
| Step 5 | Depending on
                                       			 whether your phone uses softkeys or feature buttons, perform either of the
                                       			 following tasks: Configure a Do Not Disturb Feature Button Configure a Do Not Disturb Softkey | Add a Do Not
                                          				Disturb feature button or softkey to your phone. |

| Note | Cisco
                                                      				  Unified IP Phones 7940 and 7960 that are running SIP use their own
                                                      				  backwards-compatible implementation of Do Not Disturb, which you configure on
                                                      				  the SIP Profile. |
|---|---|

| Note | Busy Lamp Field (BLF) presence status for DND works only when all the registered devices for that shared line DN are set to
                                                   DND. If you're using Jabber for iOS or Jabber for Android on the same DN, they are considered registered, even when they are not
                                                   registered but just configured. |
|---|---|

| Step 1 | In Cisco
                                          			 Unified CM Administration, choose System > Service
                                                				  Parameters . |
|---|---|
| Step 2 | Choose the Cisco
                                             				CallManager service for the server that you want to configure. |
| Step 3 | In the
                                          			 Clusterwide Parameters (System - Presence) pane, specify one of the following
                                          			 values for the BLF
                                             				Status Depicts DND service parameter: True —If Do Not
                                             				Disturb is activated on the device, the BLF status indicator for the device or
                                             				line appearance reflects the Do Not Disturb state. False —If Do Not
                                             				Disturb is activated on the device, the BLF status indicator for the device or
                                             				line appearance reflects the actual device state. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Common Phone Profile . |
|---|---|
| Step 2 | From the DND Option drop-down list, choose how you want the Do Not Disturb feature to handle incoming calls. Call Reject —No incoming call information gets presented to the user. Depending on how you configure the DND Incoming Call Alert parameter,
                                             the phone may play a beep or display a flash notification of the call. Ringer Off —This option turns off the ringer, but incoming call information gets presented to the device, so the user can accept the
                                             call. Note For mobile phones and dual-mode phones, you can only choose the Call Reject option. | Note | For mobile phones and dual-mode phones, you can only choose the Call Reject option. |
| Note | For mobile phones and dual-mode phones, you can only choose the Call Reject option. |
| Step 3 | From the Incoming Call Alert drop-down list, choose how you want to alert phone users of incoming calls while Do Not Disturb is turned on. Disable —Both beep and flash notification of a call are for disabled. If you configured the DND Ringer Off option, incoming call information
                                             still gets displayed. However, for the DND Call Reject option, no call alerts display, and no information gets sent to the
                                             device. Flash Only —The phone flashes for incoming calls. Beep Only —The phone displays a flash alert for incoming calls. |
| Step 4 | Click Save . |

| Note | For mobile phones and dual-mode phones, you can only choose the Call Reject option. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose Device > Phone |
|---|---|
| Step 2 | Click Find and select the phone on which you want to configure Do Not Disturb. |
| Step 3 | If you want to apply Do Not Disturb settings from a Common Phone Profile, from the Common Phone Profile drop-down list, choose the profile on which you have configured Do Not Disturb. |
| Step 4 | Check the Do Not
                                             				Disturb check box to enable Do Not Disturb on the phone. |
| Step 5 | In the DND Option drop-down list, specify from the following options how you want the DND feature to handle incoming calls. Call Reject —No incoming call information gets presented to the user. Depending on the configuration, the phone either plays a beep or
                                             displays a flash notification. Ringer Off —Incoming call information gets presented to the device so that the user can accept the call, but the ringer is turned off. Use Common Profile Setting —The Do Not Disturb setting for the Common Phone Profile that is specified for this device gets used. Note For 7940/7960 phones that are running SCCP, you can only choose the Ringer Off option. For mobile devices and dual-mode phones,
                                                      you can only choose the Call Reject option. When you activate DND Call Reject on a mobile device or dual-mode phone, no call
                                                      information gets presented to the device. | Note | For 7940/7960 phones that are running SCCP, you can only choose the Ringer Off option. For mobile devices and dual-mode phones,
                                                      you can only choose the Call Reject option. When you activate DND Call Reject on a mobile device or dual-mode phone, no call
                                                      information gets presented to the device. |
| Note | For 7940/7960 phones that are running SCCP, you can only choose the Ringer Off option. For mobile devices and dual-mode phones,
                                                      you can only choose the Call Reject option. When you activate DND Call Reject on a mobile device or dual-mode phone, no call
                                                      information gets presented to the device. |
| Step 6 | In the DND Incoming Call Alert drop-down list, specify from the following options how you want the phone to display an incoming call when DND is turned
                                          on. None —The DND Incoming Call Alert setting from the Common Phone Profile gets used for this device. Disable —For DND Ringer Off, both beep and flash notifications are disabled, but incoming call information is still displayed. For
                                             Call Reject, beep and flash notifications are disabled, and no incoming call information gets passed to the device. Beep only —For incoming calls, the phone plays a beep tone only. Flash only —For incoming calls, the phone displays a flash alert. |
| Step 7 | Click Save . |

| Note | For 7940/7960 phones that are running SCCP, you can only choose the Ringer Off option. For mobile devices and dual-mode phones,
                                                      you can only choose the Call Reject option. When you activate DND Call Reject on a mobile device or dual-mode phone, no call
                                                      information gets presented to the device. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Phone Button Template for Do Not Disturb | Create a phone button template that includes the Do Not Disturb button. |
| Step 2 | Associate a Button Template with a Phone | Associate the Do Not Disturb button template to a phone. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Phone Button Template . |
|---|---|
| Step 2 | Click Find to display list of supported phone templates. |
| Step 3 | Perform the following steps if you want to create a new phone button template; otherwise, proceed to the next step. Select a default template for the model of phone and click Copy . In the Phone Button Template Information field, enter a new name for the template. Click Save . |
| Step 4 | Perform the following steps if you want to add phone buttons to an existing template. Click Find and enter the search criteria. Choose an existing template. |
| Step 5 | From the Line drop-down list, choose 
                                             			 feature that you want  to add to the template. |
| Step 6 | Click Save . |
| Step 7 | Perform one
                                             			 of the following tasks: Click Apply Config if you modified a template that is already associated with devices to restart the devices. If you created a new softkey template, associate the template with the devices and then restart them. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find to display the list of configured phones. |
| Step 3 | Choose the
                                             			 phone to which you want to add the phone button template. |
| Step 4 | In the Phone
                                                				Button Template drop-down list, choose the phone button template
                                             			 that contains the new feature button. |
| Step 5 | Click Save . A
                                             			 dialog box is displayed with a message to press Reset to update the phone settings. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Softkey Template for Do Not Disturb | Create a softkey template that includes the Do Not Disturb softkey. |
| Step 2 | Perform either  of the following procedures: Associate a Softkey Template with a Common Device Configuration Associate Softkey Template with a Phone | You can associate the softkey to a Common Device Configuration and then associate that configuration to a group of  phones,
                                             or you can associate the softkey template directly to a phone. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Softkey Template . |
|---|---|
| Step 2 | Perform the following steps to create a new softkey template; otherwise, proceed to the next step. Click Add New . Select a default template and click Copy . Enter a new name for the template in the Softkey Template Name field. Click Save . |
| Step 3 | Perform the following steps to add softkeys to an existing template. Click Find and enter the search criteria. Select the required existing template. |
| Step 4 | Check the Default Softkey Template check box to designate this softkey template as the default softkey template. Note If you
                                                            				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                            designation. | Note | If you
                                                            				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                            designation. |
| Note | If you
                                                            				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                            designation. |
| Step 5 | Choose Configure Softkey Layout from the Related Links drop-down list in the upper right
                                             			 corner and click Go . |
| Step 6 | From the Select
                                                				a Call State to Configure drop-down list, choose the call state for
                                             			 which you want the softkey to display. |
| Step 7 | From the Unselected Softkeys list, choose the softkey to add and click the right arrow to move the softkey to the Selected Softkeys list. Use the up and down arrows
                                             			 to change the position of the new softkey. |
| Step 8 | Repeat the previous step to display the softkey in additional call states. |
| Step 9 | Click Save . |
| Step 10 | Perform one
                                             			 of the following tasks: Click Apply Config if you modified a template that is already associated with devices to restart the devices. If you created a new softkey template, associate the template with the devices and then restart them. For more information,
                                                see Add a Softkey Template to a Common Device Configuration and Associate a Softkey Template with a Phone sections. |

| Note | If you
                                                            				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                            designation. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Add Softkey Template to Common Device Configuration | Associate the DND softkey template to a Common Device Configuration. |
| Step 2 | Associate Common Device Configuration with Phone | Add the DND softkey to a phone by associating the Common Device Configuration to the phone. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Common Device Configuration . |
|---|---|
| Step 2 | Perform the following steps to create a new Common Device Configuration and associate the softkey template with it; otherwise,
                                                proceed to the next step. Click Add New . Enter a name for the Common Device Configuration in the Name field. Click Save . |
| Step 3 | Perform the following steps to add the softkey template to an existing Common Device Configuration. Click Find and enter the search criteria. Click an existing Common Device Configuration. |
| Step 4 | In the Softkey Template drop-down list, choose the softkey
                                                			 template that contains the softkey that you want to make available. |
| Step 5 | Click Save . |
| Step 6 | Perform one
                                                			 of the following tasks: If you modified a Common Device Configuration that is already associated with devices, click Apply Config to restart the devices. If you created a new Common Device Configuration, associate the configuration with devices and then restart them. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find and select the phone device to add the softkey template. |
| Step 3 | From the Common Device Configuration drop-down list, choose
                                                				  the common device configuration that contains the new softkey template. |
| Step 4 | Click Save . |
| Step 5 | Click Reset to update the phone settings. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find to select the phone to add the softkey template. |
| Step 3 | From the Softkey Template drop-down list, choose the template that contains the new softkey. |
| Step 4 | Click Save . |
| Step 5 | Press Reset to update the phone settings. |

| Feature | Interaction with Do Not Disturb |
|---|---|
| Call
                                             						Forward All | On Cisco
                                             						Unified IP Phones, the message that indicates that the Do Not Disturb (DND)
                                             						feature is active takes priority over the message that indicates that the user
                                             						has new voice messages. However, the message that indicates that the Call
                                             						Forward All feature is active has a higher priority than DND. |
| Park
                                             						Reversion | For
                                             						locally parked calls, Park Reversion overrides DND. If Phone A has DND turned
                                             						on, and a call is parked, the park reversion to Phone A occurs and Phone A
                                             						rings. For
                                             						remotely parked calls, DND overrides Park Reversion: If
                                                   							 Phone A activates DND Ringer Off and shares a line with Phone A-prime, when
                                                   							 Phone A-prime parks the call, park reversion on Phone A honors the DND settings
                                                   							 and does not ring. If Phone A activated DND Call Reject, the park reversion is not presented to Phone A. |
| Pickup | For
                                             						locally placed Pickup requests, Pickup overrides DND. If Phone A has DND turned
                                             						on, and has initiated any type of Pickup, the Pickup call presents normally,
                                             						and Phone A rings. For
                                             						remotely placed Pickup requests, DND overrides Pickup as follows: If
                                                   							 Phone A is in DND Ringer Off mode and shares a line with Phone A-prime, when
                                                   							 Phone A-prime initiates Pickup, the Pickup call to Phone A honors the DND
                                                   							 settings and Phone A does not ring. If
                                                   							 Phone A is in DND Call Reject mode, the Pickup call is not presented to Phone
                                                   							 A. |
| Hold
                                             						Reversion and Intercom | Hold
                                             						Reversion and Intercom override DND, and the call gets presented normally. |
| MLPP and
                                             						CER | Multilevel Precedence and Preemption (phones that are running SCCP) and Cisco Emergency Responder calls override DND. Multilevel
                                             Precedence and Preemption and Cisco Emergency Responder calls get presented normally, and the phone ring is supported on both
                                             SCCP and SIP. |
| Call
                                             						Back | For the
                                             						originating side, callback overrides DND. When the activating device is on DND
                                             						mode, the callback notification (both audio and visual) is still presented to
                                             						the user. For the
                                             						terminating side, DND overrides callback as follows: When the terminating side is on DND Ringer Off, the Callback Available screen is sent after the terminating side goes off
                                                   hook and on hook. When the terminating side is on DND Call Reject, and is available, a new screen is sent to the activating device as "<DirectoryNumber>
                                                   has become available but is on DND-R" if the activating device is in same cluster. Callback available notification is sent
                                                   only after the terminating side disables DND Call Reject. |
| Pickup
                                             						Notification | For the
                                             						DND Ringer Off option, only visual notification gets presented to the device. For the
                                             						DND Call Reject option, no notification gets presented to the device. |
| Hunt
                                             						List | If a
                                             						device in a Hunt List has DND Ringer Off activated, the call is still presented
                                             						to the user. However, the DND Incoming Call Alert settings would still apply. If a
                                             						device in a Hunt List has DND Call Reject activated, any calls to that Hunt
                                             						List will go to the next member and will not get sent to this device. |
| Extension Mobility | For
                                             						Extension Mobility, the device profile settings include DND incoming call alert
                                             						and DND status. When a user logs in and enables DND, the DND incoming call
                                             						alert and DND status settings get saved, and these settings get used when the
                                             						user logs in again. Note When a user who is logged in to Extension Mobility modifies the DND incoming call alert or DND status settings, this action
                                                      does not affect the actual device settings. | Note | When a user who is logged in to Extension Mobility modifies the DND incoming call alert or DND status settings, this action
                                                      does not affect the actual device settings. |
| Note | When a user who is logged in to Extension Mobility modifies the DND incoming call alert or DND status settings, this action
                                                      does not affect the actual device settings. |

| Note | When a user who is logged in to Extension Mobility modifies the DND incoming call alert or DND status settings, this action
                                                      does not affect the actual device settings. |
|---|---|

| Note | Cisco Unified IP Phones 7940 and 7960 that run SIP use their own implementation of Do Not Disturb, which is backward compatible. |
|---|---|

| Symptom | Actions |
|---|---|
| DND
                                          						softkey does not display or DND
                                          						feature button does not display | Verify that the softkey or button template for this phone includes DND. Capture a sniffer trace and verify that the phone gets the correct softkey or button template. Verify that the phone firmware is Version 8.3(1) or later. |
| BLF
                                          						speed dial does not show DND status | Verify that the BLF DND is set to enabled in Enterprise parameters. Capture a sniffer trace and verify that the phone gets the
                                                							 correct notification message. Verify that the phone firmware is Version 8.3(1) or later. |
| DND changes are not reflected on the monitoring device. | Check if the BOT/TCT devices are shared line devices with the DND state set to OFF . If the status is set to ON , changes to the DND status on other shared lines will not be reflected. Make sure the DND status on the BOT/TCT devices is set to OFF to reflect changes in the DND status on the line you want to monitor. |