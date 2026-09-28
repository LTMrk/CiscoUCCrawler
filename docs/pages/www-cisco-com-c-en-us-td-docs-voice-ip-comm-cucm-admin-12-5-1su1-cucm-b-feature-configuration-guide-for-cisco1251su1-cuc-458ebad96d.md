---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su1-cucm-b-feature-configuration-guide-for-cisco1251su1-cuc-458ebad96d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU1/cucm_b_feature-configuration-guide-for-cisco1251SU1/cucm_b_feature-configuration-guide-for-cisco1251SU2_chapter_010100.html
retrieved_at: 2026-08-16T17:18:11.640596+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

Updated: July 31, 2025

Chapter: Call Back

## Chapter: Call Back

# Call Back

## Call Back
                        	 Overview

The CallBack feature allows you to receive notification when a busy extension is available to receive calls.

You can activate Call Back for a destination phone that is within the same Unified Communications Manager cluster as your phone or on a remote Private Integrated Network Exchange (PINX) over QSIG trunks or QSIG-enabled intercluster
                              trunks.

To receive
                              		  CallBack notification, press the CallBack softkey or feature button while
                              		  receiving a busy or ringback tone. You can activate Call Back during reorder
                              		  tone, which is triggered when the No Answer timer expires.

### Suspend/Resume

The Call Back
                              		  feature enables the system to suspend the call completion service if the user
                              		  who originated Call Back is busy. When the originating user then becomes
                              		  available, the call completion service resumes for that user.

## Call Back
                        	 Prerequisites

To use the Call
                              		  Back feature, the destination phone must be in one of the following locations:

In the same Unified Communications Manager cluster as the user phone

On a remote PINX over QSIG trunks

On a remote PINX over QSIG-enabled intercluster trunks

If you want to use
                              		  non-English phone locales or country-specific tones, you must install locales.

The following
                                    				devices support the Call Back feature:

Cisco
                                          					 Unified IP Phones 6900, 7900, 8900, and 9900 Series (except 6901 and 6911)

Cisco IP Phones 7800 and 8800 Series

Cisco VGC
                                          					 Phone (uses the Cisco VG248 Gateway)

Cisco
                                          					 Analog Telephone Adapter (ATA) 186 and 188

Busy
                                          					 Subscriber for Cisco VG224 endpoints

No Answer
                                          					 for Cisco VG224 endpoints

A CTI route
                                    				point that forwards calls to any of the supported phones.

## Call Back
                        	 Configuration Task Flow

Complete one of
                              		  the task flows depending on whether your phone supports softkey or buttons.

Use this table
                              		  to determine whether to configure the CallBack softkey or the button for the
                              		  Call Back supported IP phones.

Cisco
                                          					 Phone Model

CallBack
                                          					 Softkey

CallBack
                                          					 Button

Cisco
                                          					 Unified IP Phone 6900 Series (except 6901 and 6911)

X

X

Cisco
                                          					 Unified IP Phone 7900 Series

X

Cisco IP
                                          					 Phone 7800 and 8800 Series

X

X

Cisco
                                          					 Unified IP Phone 8900 Series

X

X

Cisco
                                          					 Unified IP Phone 9900 Series

X

X

Cisco IP
                                          					 Communicator

X

### Before you begin

Review Call Back Prerequisites .

Step 1

Configure Softkey Template for CallBack

Perform this
                                          				step to add CallBack softkey to template and configure the softkey using the
                                          				Common Device Configuration or phone.

Step 2

Configure CallBack Button

Perform this
                                          				step to add and configure the CallBack button to a phone.

### Configure Softkey Template for CallBack

CallBack softkey has the following call states:

On Hook

Ring Out

Connected Transfer

Use this procedure to make the CallBack softkey available:

#### Before you begin

Ensure your phone supports Call Back.

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

#### What to do next

Perform one the following procedures:

Associate CallBack Softkey Template with a Common Device Configuration

Associate CallBack Softkey Template with Phone

#### Associate CallBack
                              	 Softkey Template with a Common Device Configuration

Optional . There are two ways to associate a softkey template with a phone:

Add the softkey template to the Phone Configuration .

Add the
                                          				softkey template to the Common Device Configuration .

The
                                    		  procedures in this section describe how to associate the softkey template with
                                    		  a Common
                                       			 Device Configuration . Follow these procedures if your system uses a Common
                                       			 Device Configuration to apply configuration options to phones. This
                                    		  is the most commonly used method for making a softkey template available to
                                    		  phones.

To use the alternative method, see Associate CallBack Softkey Template with Phone .

Step 1

Add CallBack Softkey Template to the Common Device Configuration

Perform this step to add CallBack softkey template to the Common Device Configuration.

Step 2

Associate a Common Device Configuration with a Phone

Perform this step to link the CallBack softkey Common Device Configuration to a phone.

##### Add CallBack Softkey Template to the Common Device Configuration

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

##### Associate a Common Device Configuration with a Phone

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

#### Associate CallBack Softkey Template with Phone

Optional: Use this procedure either as an alternative to associating the softkey template with the Common Device Configuration,
                                    or in conjunction with the Common Device Configuration. Use this procedure in conjunction with the Common Device Configuration
                                    if you need to assign a softkey template that overrides the assignment in the Common Device Configuration or any other default
                                    softkey assignment.

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

### Configure CallBack Button

The procedures in this section describe how to configure the CallBack button.

Step 1

Configure Phone Button Template for Call Back

Perform this step to assign CallBack button features to line or speed dial keys.

Step 2

Associate a Button Template with a Phone

Perform this step to configure the CallBack button for a phone.

#### Configure Phone Button Template for Call Back

Follow this procedure when you want to assign features to line or speed dial keys.

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

#### Associate a
                              	 Button Template with a Phone

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

## Call Back Interactions

Feature

Interaction

Call
                                          						Forward

Calls that are made from CallBack notification screen will override all the Call Forward configured values on the target DN.
                                          The calls should be made before CallBack recall timer expires otherwise the calls will not override the Call Forward configured
                                          values.

CallBack
                                          						notification with phones running SIP

CallBack notification works  differently  only for Cisco Unified IP
                                          						Phones 7960 and 7940. All other SIP phones and all SCCP phones support on-hook and off-hook notification.

The only way that Unified Communications Manager knows when a line on a SIP 7960 or 7940 phone becomes available is by monitoring an incoming SIP INVITE message that Unified Communications Manager receives from the phone. After the phone sends the SIP INVITE to Unified Communications Manager and the phone goes on-hook, Unified Communications Manager sends an audio and CallBack notification screen to the Cisco Unified IP Phone 7960 and 7940 (SIP) user.

Do Not Disturb (DND)

CallBack would work normally in case or when DND-Reject is set to Off at the 
                                          originating or the terminating end. The behavior differs only when DND-Reject is set to On .

DND-Reject On on Originating end —User A calls User B and invokes Call Back. User A goes on DND-R. After User B is available, the CallBack notification will
                                                still be displayed to User A. That is, user will still be notified with the availability of the other party irrespective of
                                                the DND status.

DND-Reject On on Terminating end —User A calls User B, and User B has set DND-Reject to On . User A will get a fast busy tone. User A can initiate CallBack on a busy endpoint. If User B is still on DND-Reject and
                                                goes Offhook and Onhook, User A will get a notification "User B is available now but on DND-R" , and it will not show the Dial option. If User A does not choose to cancel, CallBack will still monitor User B until User
                                                B  sets DND-Reject to Off .

Cisco
                                          						Extension Mobility

When a
                                          						Cisco Extension Mobility user logs in or logs out, any active call completion
                                          						that is associated with Call Back is automatically canceled. If a called phone
                                          						is removed from the system after Call Back is activated on the phone, the
                                          						caller receives a reorder tone after pressing the Dial softkey. The user may
                                          						cancel or reactivate Call Back.

## Call Back Restrictions

Feature

Restriction

Call Back with video across CUBE

The Call Back feature does not work for video calls when the call is placed between two Unified CM clusters that are connected
                                       via CUBE with qsig-enabled SIP trunks. For additional detail, see CSCun46243.

SIP Trunks

Call Back is
                                       				not supported over SIP trunks but is supported over QSIG-enabled SIP trunks.

Supported characters for name or number of calling or called party

Call Back only supports
                                       			 spaces and digits 0 through 9 for the name or number of the calling or called
                                       			 party. To work with CallBack, the name or number of the calling or called party
                                       			 cannot contain a pound sign (#) or asterisk (*).

Voicemail

You cannot
                                       				activate Call Back if you forward all calls to Voice-Messaging System.

## Call Back Troubleshooting

This section
                              		  describes the problems, possible causes, and solutions for various scenarios,
                              		  and error messages that are displayed on the IP phone for Call Back.

### Unplug/Reset Phone After Pressing CallBack Softkey but Before CallBack Occurs

#### Problem

You have unplugged or
                                 		  reset the phone after pressing the CallBack Softkey but before activating
                                 		  CallBack.

#### Possible Cause

Unified Communications Manager cancels the Call Back activation.

#### Solution

After the caller phone registers, the caller phone does not display the Call Back activation window
                                 		  after the reset. The caller must press the CallBack Softkey to view the
                                 		  active Call Back service. CallBack notification occurs on the phone.

### Caller Misses to View Availability Notification Before Phone Reset

#### Problem

In an intracluster
                                 		  or intercluster Call Back scenario, a caller initiates Call Back for a user,
                                 		  for example, User B, who is unavailable. When User B becomes available, the
                                 		  availability notification screen displays on the caller phone, and a tone
                                 		  plays. The caller misses the availability notification for some reason, and the
                                 		  phone resets.

The caller
                                 		  contacts a different user, User C, for example, and presses the CallBack
                                 		  softkey because User C appears busy. The replace/retain screen displays on the
                                 		  caller phone, but the screen does not state that the availability notification
                                 		  already occurred for User B.

#### Possible Cause

The user reset the
                                 		  phone.

#### Solution

After a phone reset but not during an active call, review the Call
                                 		  Back notifications on the phone. Press the CallBack softkey.

### Call Back Error
                           	 Messages

#### CallBack Is Not
                              	 Active

##### Problem

The following error message is displayed:

```
CallBack is not active. Press Exit to quit this screen.
```

##### Possible
                                    		  Cause

User pressed the
                                    		  CallBack softkey during the idle state.

##### Solution

Follow the
                                    		  recommended action provided in the error message.

#### CallBack Is
                              	 Already Active

##### Problem

The following error message is displayed:

```
CallBack is already active on xxxx. Press OK to activate on yyyy. Press Exit to quit this screen.
```

##### Possible
                                    		  Cause

A user tried to
                                    		  activate Call Back, but it is already active.

##### Problem

Follow the
                                    		  recommended action provided in the error message.

#### CallBack Cannot Be
                              	 Activated

##### Problem

The following error message is displayed:

```
CallBack cannot be activated for xxxx.
```

##### Possible
                                    		  Cause

When a user tried to activate Call Back, either the extension is not available in Unified Communications Manager database or there is no QSIG route to the destination (that is, the extension belongs to remote Proxy which is connected
                                    via non-QSIG trunk), and the extension is not found in the database.

##### Solution

The user must try
                                    		  again, or the administrator must add the directory number to the Cisco Unified
                                    		  CM Administration.

#### Key Not Active

##### Problem

During a call, the CallBack softkey displays on the phone and the user presses the CallBack softkey before the phone rings.
                                    But, the following error message is displayed on the phone:

```
Key Not Active
```

##### Possible Cause

User may not be pressing the CallBack softkey at the appropriate time.

##### Solution

Users must press the CallBack softkey after a ringing or busy signal
                                    		  is received. Pressing the softkey at the wrong time may cause an error message
                                    		  to display on the phone.

| Note | Call Back
                                       		  supports Suspend/Resume CallBack notification for both intracluster and
                                       		  intercluster QSIG trunks or QSIG-enabled intercluster trunks. |
|---|---|

| Cisco
                                          					 Phone Model | CallBack
                                          					 Softkey | CallBack
                                          					 Button |
|---|---|---|
| Cisco
                                          					 Unified IP Phone 6900 Series (except 6901 and 6911) | X | X |
| Cisco
                                          					 Unified IP Phone 7900 Series | X |  |
| Cisco IP
                                          					 Phone 7800 and 8800 Series | X | X |
| Cisco
                                          					 Unified IP Phone 8900 Series | X | X |
| Cisco
                                          					 Unified IP Phone 9900 Series | X | X |
| Cisco IP
                                          					 Communicator | X |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Softkey Template for CallBack | Perform this
                                          				step to add CallBack softkey to template and configure the softkey using the
                                          				Common Device Configuration or phone. |
| Step 2 | Configure CallBack Button | Perform this
                                          				step to add and configure the CallBack button to a phone. |

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
| Step 1 | Add CallBack Softkey Template to the Common Device Configuration | Perform this step to add CallBack softkey template to the Common Device Configuration. |
| Step 2 | Associate a Common Device Configuration with a Phone | Perform this step to link the CallBack softkey Common Device Configuration to a phone. |

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

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Phone Button Template for Call Back | Perform this step to assign CallBack button features to line or speed dial keys. |
| Step 2 | Associate a Button Template with a Phone | Perform this step to configure the CallBack button for a phone. |

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

| Feature | Interaction |
|---|---|
| Call
                                          						Forward | Calls that are made from CallBack notification screen will override all the Call Forward configured values on the target DN.
                                          The calls should be made before CallBack recall timer expires otherwise the calls will not override the Call Forward configured
                                          values. |
| CallBack
                                          						notification with phones running SIP | CallBack notification works  differently  only for Cisco Unified IP
                                          						Phones 7960 and 7940. All other SIP phones and all SCCP phones support on-hook and off-hook notification. The only way that Unified Communications Manager knows when a line on a SIP 7960 or 7940 phone becomes available is by monitoring an incoming SIP INVITE message that Unified Communications Manager receives from the phone. After the phone sends the SIP INVITE to Unified Communications Manager and the phone goes on-hook, Unified Communications Manager sends an audio and CallBack notification screen to the Cisco Unified IP Phone 7960 and 7940 (SIP) user. |
| Do Not Disturb (DND) | CallBack would work normally in case or when DND-Reject is set to Off at the 
                                          originating or the terminating end. The behavior differs only when DND-Reject is set to On . DND-Reject On on Originating end —User A calls User B and invokes Call Back. User A goes on DND-R. After User B is available, the CallBack notification will
                                                still be displayed to User A. That is, user will still be notified with the availability of the other party irrespective of
                                                the DND status. DND-Reject On on Terminating end —User A calls User B, and User B has set DND-Reject to On . User A will get a fast busy tone. User A can initiate CallBack on a busy endpoint. If User B is still on DND-Reject and
                                                goes Offhook and Onhook, User A will get a notification "User B is available now but on DND-R" , and it will not show the Dial option. If User A does not choose to cancel, CallBack will still monitor User B until User
                                                B  sets DND-Reject to Off . |
| Cisco
                                          						Extension Mobility | When a
                                          						Cisco Extension Mobility user logs in or logs out, any active call completion
                                          						that is associated with Call Back is automatically canceled. If a called phone
                                          						is removed from the system after Call Back is activated on the phone, the
                                          						caller receives a reorder tone after pressing the Dial softkey. The user may
                                          						cancel or reactivate Call Back. |

| Feature | Restriction |
|---|---|
| Call Back with video across CUBE | The Call Back feature does not work for video calls when the call is placed between two Unified CM clusters that are connected
                                       via CUBE with qsig-enabled SIP trunks. For additional detail, see CSCun46243. |
| SIP Trunks | Call Back is
                                       				not supported over SIP trunks but is supported over QSIG-enabled SIP trunks. |
| Supported characters for name or number of calling or called party | Call Back only supports
                                       			 spaces and digits 0 through 9 for the name or number of the calling or called
                                       			 party. To work with CallBack, the name or number of the calling or called party
                                       			 cannot contain a pound sign (#) or asterisk (*). |
| Voicemail | You cannot
                                       				activate Call Back if you forward all calls to Voice-Messaging System. |