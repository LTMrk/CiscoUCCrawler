---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su1-cucm-b-feature-configuration-guide-for-cisco1251su1-cuc-d3446987f7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU1/cucm_b_feature-configuration-guide-for-cisco1251SU1/cucm_b_feature-configuration-guide-for-cisco1251SU2_chapter_0100110.html
retrieved_at: 2026-08-16T17:19:28.790617+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

Updated: July 31, 2025

Chapter: Barge

## Chapter: Barge

# Barge

## Barge
                        	 Overview

Barge allows a user
                           		to be added to a remotely active call that is on a shared line. Remotely active
                           		calls for a line are the active (connected) calls that are made to or from
                           		another device that shares a directory number with the line.

If you configure
                           		party entrance tone, a tone plays on the phone when a basic call changes to a
                           		barged call or cbarged call. In addition, a different tone plays when a party
                           		leaves the multiparty call.

Phones support Barge in the following conference modes:

Built-in conference bridge at the phone that is barged—This mode uses the Barge softkey. Most Cisco Unified IP Phones include
                                 the built-in conference bridge capability.

Shared conference bridge—This mode uses the cBarge softkey.

By pressing the Barge or cBarge softkey in the remote-in-use call state, the user is added to the call with all parties, and
                           all parties receive a barge beep tone (if configured). If Barge fails, the original call remains active. If no conference
                           bridge is available (built-in or shared), the barge request gets rejected, and a message displays on the Barge initiator device.
                           When network or Unified Communications Manager failure occurs, the Barge call is preserved.

For a list of Cisco Unified IP Phones that support Barge, log in to Cisco Unified Reporting and run the Unified CM Phone Feature
                           List report. Make sure to select Built In Bridge as the feature. For details, see Generate a Phone Feature List .

### Single-Button
                              		  Barge and Single-Button cBarge

The Single-Button
                              		  Barge and Single-Button cBarge features allow a user to press the shared-line
                              		  button of the remotely active call, to be added to the call. All parties
                              		  receive a barge beep tone (if configured). If barge fails, the original call
                              		  remains active.

Phones support Single-Button Barge and Single-Button cBarge in two conference modes:

Built-in conference bridge at the phone that is barged—This mode uses the Single-Button Barge feature.

Shared conference bridge—This mode uses the Single-Button cBarge feature.

By pressing the
                              		  shared-line button of the remote-in-use call, the user is added to the call
                              		  with all parties, and all parties receive a barge beep tone (if configured). If
                              		  barge fails, the original call remains active. If no conference bridge is
                              		  available (built-in or shared), the barge request gets rejected, and a message
                              		  is displayed at the Barge initiator device.

### Built-In
                           	 Conference

When the user
                              		presses the Barge softkey or a shared-line button, a Barge call is set up by
                              		using the built-in conference bridge, if available. A built-in conference
                              		bridge is advantageous because neither a media interruption nor display changes
                              		to the original call occur when the Barge is being set up.

### Shared
                           	 Conference

When the user
                              		presses the cBarge softkey, or a shared-line button, a barge call is set up by
                              		using the shared conference bridge, if available. The original call is split
                              		and then joined at the conference bridge, which causes a brief media
                              		interruption. The call information for all parties changes to "Barge" . The
                              		barged call becomes a conference call with the barge target device as the
                              		conference controller. It can add more parties to the conference or can drop
                              		any party. When any party releases the call, the remaining two parties
                              		experience a brief interruption and then get reconnected as a point-to-point
                              		call, which releases the shared conference resource.

### Built-In and
                           	 Shared Conference Differences

Feature

Barge with Built-In Conference

Barge with Shared Conference

Yes

No

A media break occurs during barge setup.

No

Yes

If configured, a user receives a barge setup tone.

Yes

Yes

Text displays at the barge initiator phone.

To barge XXX

To Conference

Text displays at the target phone.

To/From Other

To Conference

Text displays at the other phones.

To/From Target

To Conference

Bridge supports a second barge setup to an already barged
                                                						call.

No

Yes

Initiator releases the call.

No media interruption occurs for the two original parties.

Media break occurs to release the shared conference bridge
                                                						when only two parties remain and to reconnect the remaining parties as a
                                                						point-to-point call.

Target releases the call.

Media break occurs to reconnect initiator with the other
                                                						party as a point-to-point call.

Media break occurs to release the shared conference bridge
                                                						when only two parties remain and to reconnect the remaining parties as a
                                                						point-to-point call.

Other party releases the call.

All three parties get released.

Media break occurs to release the shared conference bridge
                                                						when only two parties remain and to reconnect the remaining parties as a
                                                						point-to-point call.

Target puts call on hold and performs Direct Transfer, Join,
                                                						or Call Park.

Initiator gets released.

Initiator and the other party remain connected.

## Barge
                        	 Configuration Task Flow

Step 1

Configure Softkey Template for Built-In Conferencing

Step 2

Configure Softkey Template for Shared Conferencing

Step 3

To Associate a Softkey Template with Common Device Configuration ,
                                       			 complete the following subtasks:

- Add a Softkey Template to Common Device Configuration

- Associate Common Device Configuration with Phone

Step 4

Associate Softkey Template with Phone

Step 5

Configure Barge for Built-In Conferencing

Step 6

Configure Barge for Shared Conferencing

Step 7

Associate User with Device

### Configure Softkey
                           	 Template for Built-In Conferencing

Configure a softkey template for Barge and assign the Barge softkey to that template. You can configure the Barge softkey
                                 in the Remote In Use call state.

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

- Add a Softkey Template to Common Device Configuration

- Associate Common Device Configuration with Phone

### Configure Softkey
                           	 Template for Shared Conferencing

Configure a softkey template for shared conferencing  and assign the cBarge softkey to that template. You can configure the
                                 cBarge softkey in the Remote In Use call state.

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

### Associate Softkey
                           	 Template with Phone

Step 1

From Cisco
                                             				Unified CM Administration, choose Device > Phone .

Step 2

Find the phone
                                          			 to which you want to add the softkey template.

Step 3

Perform one of
                                          			 the following tasks:

From the Common Device Configuration drop-down
                                                				  list, choose the common device configuration that contains the required softkey
                                                				  template.

In the Softkey Template drop-down list, choose
                                                				  the softkey template that contains the Barge or cBarge softkey.

Step 4

Click Save .

### Associate a Softkey Template with Common Device Configuration

Optional . There are two ways to associate a softkey template with a phone:

Add the softkey template to the Phone Configuration .

Add the softkey template to the Common Device Configuration .

The procedures in this section describe how to associate the softkey template with a Common Device Configuration . Follow these procedures if your system uses a Common Device Configuration to apply configuration options to phones. This is the most commonly used method for making a softkey template available to
                                 phones.

To use the alternative method, see Associate Softkey Template with Phone .

Step 1

Add a Softkey Template to Common Device Configuration

Step 2

Associate a Common Device Configuration with a Phone

#### Add a Softkey
                              	 Template to Common Device Configuration

##### Before you begin

Perform one or both of the following as needed:

Configure Softkey Template for Built-In Conferencing

Configure Softkey Template for Shared Conferencing

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

#### Associate Common
                              	 Device Configuration with Phone

##### Before you begin

Configure Softkey Template for Built-In Conferencing

Configure Softkey Template for Shared Conferencing

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

##### What to do next

Configure Barge for Built-In Conferencing

Configure Barge for Shared Conferencing

### Configure Barge
                           	 for Built-In Conferencing

Most Cisco Unified IP Phones include the built-in conference bridge capability; that is, these Cisco IP Phones have an internal
                                 DSP that acts as a small conference bridge to support the barge feature. It can support only a maximum of three parties that
                                 include the phone itself. Starting from firmware version 11.x, Cisco IP Phone 8800 Series have the capability to daisy chain
                                 the built-in bridge (BIB) feature.

Step 1

From Cisco Unified CM Administration, choose System > Service
                                                				  Parameters and set the Built In Bridge Enable clusterwide service parameter to On .

Step 2

Set the Party
                                             			 Entrance Tone clusterwide service parameter to True (required for tones) or
                                          			 configure the Party Entrance Tone field in the Directory Number Configuration window.

Step 3

Set the Single
                                             			 Button Barge/CBarge Policy to Barge .

Step 4

Set the Allow
                                             			 Barge When Ringing service parameter to True .

Step 5

Click Save .

### Configure Barge
                           	 for Shared Conferencing

Step 1

From Cisco Unified CM Administration, choose System > Service
                                                				  Parameters and set the Built In Bridge Enable clusterwide service parameter to On .

Step 2

Set the Party
                                             			 Entrance Tone clusterwide service parameter to True (required for tones) or
                                          			 configure the Party Entrance Tone field in the Directory Number Configuration window.

Step 3

Set the Single
                                             			 Button Barge/CBarge Policy to cBarge .

Step 4

Set the Allow
                                             			 Barge When Ringing service parameter to True.

Step 5

Click Save .

### Associate User
                           	 with Device

#### Before you begin

Perform one or both of the following:

Configure Barge for Built-In Conferencing

Configure Barge for Shared Conferencing

Step 1

From Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > End User .

Step 2

Specify the
                                          			 appropriate filters in the Find
                                             				User Where field to and then click Find to retrieve a list of users.

Step 3

Select the
                                          			 user from the list.

Step 4

Locate the Device
                                             				Information section.

Step 5

Click Device
                                             				Association .

Step 6

Find and
                                          			 select the CTI remote device.

Step 7

To complete
                                          			 the association, click Save
                                             				Selected/Changes .

Step 8

From Related Links drop-down list, choose Back to User , and then click Go .

## Barge
                        	 Interactions

Feature

Interaction

cBarge

Cisco
                                          						recommends that you assign either the Barge or cBarge softkey to a softkey
                                          						template. By having only one of these softkeys for each device, you can prevent
                                          						confusion for users and avoid potential performance issues.

Call
                                          						Park

When the
                                          						target parks the call, the barge initiator gets released (if using the built-in
                                          						bridge), or the barge initiator and the other party remain connected (if using
                                          						the shared conference).

Join

When the
                                          						target joins the call with another call, the barge initiator gets released (if
                                          						using the built-in bridge), or the barge initiator and the other party remain
                                          						connected (if using the shared conference).

Private
                                          						Line Automatic Ringdown (PLAR)

A Barge,
                                          						cBarge, or Single-Button Barge initiator can barge into a call through a shared
                                          						line that is configured for Barge and Private Line Automatic Ringdown (PLAR).
                                          						The initiator can barge into the call if the barge target uses the
                                          						preconfigured number that is associated with the PLAR line while on the call.
                                          						Cisco Unified Communications Manager does not send the barge invocation to the
                                          						PLAR line before connecting the barge call, so the barge occurs regardless of
                                          						the state of the PLAR destination.

To make
                                          						Barge, cBarge, or Single-Button Barge function with PLAR, you must configure
                                          						Barge, cBarge, or Single-Button Barge. In addition, you must configure the PLAR
                                          						destination, a directory number that is used specifically for PLAR.

## Barge
                        	 Restrictions

Restriction

Description

Additional callers

The Barge initiator cannot
                                          			 conference in additional callers.

Computer Telephony Interface (CTI)

CTI does not support Barge
                                          			 through APIs that TAPI and JTAPI applications invoke. CTI generates events for
                                          			 Barge when it is invoked manually from an IP phone by using the Barge or cBarge
                                          			 softkey.

G.711 codec

The original call requires
                                          			 G.711 codec. If G.711 is not available, use cBarge instead.

Cisco Unified IP Phones

You can assign a softkey
                                          			 template that contains the Barge softkey to any IP phone that uses softkeys;
                                          			 however, some IP phones do not support the Barge feature.

Encryption

If you configure encryption
                                          			 for Cisco Unified IP Phones 7960 and 7940, those encrypted devices cannot
                                          			 accept a barge request when they are participating in an encrypted call. When
                                          			 the call is encrypted, the barge attempt fails. A tone plays on the phone to
                                          			 indicate that the Barge failed.

Maximum number of calls

If the number of
                                          			 shared-line users in the conference is equal to or greater than the
                                          			 configuration for the Maximum Number of Calls setting for the device from which
                                          			 you are attempting to barge, the phone displays the message, Error: Past Limit .

## Barge
                        	 Troubleshooting

### No Conference
                           	 Bridge Available

When the Barge
                                 		  softkey is pressed, the message No Conference Bridge Available is
                                 		  displayed on the IP phone.

The Built In
                                    		  Bridge field in the Phone Configuration window for the target phone is not set
                                 		  properly.

To resolve the
                                 		  problem, perform the following steps:

- From Cisco Unified
                                    			 CM Administration, choose Device > Phone and click Find
                                       				the phone to find the phone configuration of the phone that is
                                    			 having the problem.

- Set the Built In Bridge field to On .

- Click Update .

- Reset the phone.

### Error: Past
                           	 Limit

The phone displays
                                 		  the message, Error: Past Limit .

The number of
                                 		  shared-line users in the conference is equal to or greater than the
                                 		  configuration for the Maximum Number of Calls field for the device from which
                                 		  you are attempting to barge.

- Go to Service
                                       				Parameter Configuration window and locate the Clusterwide Parameters
                                       			 (Feature - Conference) section. Increase the value of Maximum Ad Hoc Conference parameter as required.

- Check the Maximum Number
                                       			 of Calls value for the shared lines on the device from which you are
                                    			 attempting to barge and increase the value as required.

| Note | To display the softkey option for both Barge and cBarge, disable the Privacy option in Unified Communications Manager user interface for those devices that have shared line appearances. |
|---|---|

| Feature | Barge with Built-In Conference | Barge with Shared Conference |
|---|---|---|
| The standard softkey template includes the Barge/cBarge
                                                						softkey. Note If the single button Barge/cBarge feature is enabled,
                                                            						  the softkey is not used. | Note | If the single button Barge/cBarge feature is enabled,
                                                            						  the softkey is not used. | Yes | No |
| Note | If the single button Barge/cBarge feature is enabled,
                                                            						  the softkey is not used. |
| A media break occurs during barge setup. | No | Yes |
| If configured, a user receives a barge setup tone. | Yes | Yes |
| Text displays at the barge initiator phone. | To barge XXX | To Conference |
| Text displays at the target phone. | To/From Other | To Conference |
| Text displays at the other phones. | To/From Target | To Conference |
| Bridge supports a second barge setup to an already barged
                                                						call. | No | Yes |
| Initiator releases the call. | No media interruption occurs for the two original parties. | Media break occurs to release the shared conference bridge
                                                						when only two parties remain and to reconnect the remaining parties as a
                                                						point-to-point call. |
| Target releases the call. | Media break occurs to reconnect initiator with the other
                                                						party as a point-to-point call. | Media break occurs to release the shared conference bridge
                                                						when only two parties remain and to reconnect the remaining parties as a
                                                						point-to-point call. |
| Other party releases the call. | All three parties get released. | Media break occurs to release the shared conference bridge
                                                						when only two parties remain and to reconnect the remaining parties as a
                                                						point-to-point call. |
| Target puts call on hold and performs Direct Transfer, Join,
                                                						or Call Park. | Initiator gets released. | Initiator and the other party remain connected. |

| Note | If the single button Barge/cBarge feature is enabled,
                                                            						  the softkey is not used. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Softkey Template for Built-In Conferencing | Add the Barge
                                       			 softkey to a softkey template. Follow this procedure when you are configuring
                                       			 barge for built-in conference bridges. |
| Step 2 | Configure Softkey Template for Shared Conferencing | Add the
                                       			 cBarge softkey to a softkey template. Follow this procedure when you are
                                       			 configuring barge for shared conference bridges. |
| Step 3 | To Associate a Softkey Template with Common Device Configuration ,
                                       			 complete the following subtasks: Add a Softkey Template to Common Device Configuration Associate Common Device Configuration with Phone | Optional. To
                                       			 make the softkey template available to phones, you must complete either this
                                       			 step or the following step. Follow this step if your system uses a Common
                                       			 Device Configuration to apply configuration options to phones. This is the most
                                       			 commonly used method for making a softkey template available to phones. |
| Step 4 | Associate Softkey Template with Phone | Optional. Use
                                       			 this procedure either as an alternative to associating the softkey template
                                       			 with the Common Device Configuration, or in conjunction with the Common Device
                                       			 Configuration. Use this procedure in conjunction with the Common Device
                                       			 Configuration if you need assign a softkey template that overrides the
                                       			 assignment in the Common Device Configuration or any other default softkey. |
| Step 5 | Configure Barge for Built-In Conferencing | Configure
                                       			 barge for built-in conference bridges. |
| Step 6 | Configure Barge for Shared Conferencing | Configure
                                       			 barge for shared conference bridges. |
| Step 7 | Associate User with Device | Associate
                                       			 users with devices. |

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

| Step 1 | From Cisco
                                             				Unified CM Administration, choose Device > Phone . The Find
                                             				and List Phones window is displayed. |
|---|---|
| Step 2 | Find the phone
                                          			 to which you want to add the softkey template. |
| Step 3 | Perform one of
                                          			 the following tasks: From the Common Device Configuration drop-down
                                                				  list, choose the common device configuration that contains the required softkey
                                                				  template. In the Softkey Template drop-down list, choose
                                                				  the softkey template that contains the Barge or cBarge softkey. |
| Step 4 | Click Save . A
                                          			 dialog box is displayed with a message to press Reset to update the phone settings. |

| Step 1 | Add a Softkey Template to Common Device Configuration |
|---|---|
| Step 2 | Associate a Common Device Configuration with a Phone |

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

| Step 1 | From Cisco Unified CM Administration, choose System > Service
                                                				  Parameters and set the Built In Bridge Enable clusterwide service parameter to On . Note If this
                                                      				parameter is set to Off , configure barge for each phone by setting the Built in Bridge field in the Phone
                                                         				  Configuration window. | Note | If this
                                                      				parameter is set to Off , configure barge for each phone by setting the Built in Bridge field in the Phone
                                                         				  Configuration window. |
|---|---|---|---|
| Note | If this
                                                      				parameter is set to Off , configure barge for each phone by setting the Built in Bridge field in the Phone
                                                         				  Configuration window. |
| Step 2 | Set the Party
                                             			 Entrance Tone clusterwide service parameter to True (required for tones) or
                                          			 configure the Party Entrance Tone field in the Directory Number Configuration window. |
| Step 3 | Set the Single
                                             			 Button Barge/CBarge Policy to Barge . Note If this
                                                      				parameter is set to Off , configure single-button barge for each phone by
                                                      				setting the Single Button Barge field in the Phone
                                                         				  Configuration window. | Note | If this
                                                      				parameter is set to Off , configure single-button barge for each phone by
                                                      				setting the Single Button Barge field in the Phone
                                                         				  Configuration window. |
| Note | If this
                                                      				parameter is set to Off , configure single-button barge for each phone by
                                                      				setting the Single Button Barge field in the Phone
                                                         				  Configuration window. |
| Step 4 | Set the Allow
                                             			 Barge When Ringing service parameter to True . |
| Step 5 | Click Save . |

| Note | If this
                                                      				parameter is set to Off , configure barge for each phone by setting the Built in Bridge field in the Phone
                                                         				  Configuration window. |
|---|---|

| Note | If this
                                                      				parameter is set to Off , configure single-button barge for each phone by
                                                      				setting the Single Button Barge field in the Phone
                                                         				  Configuration window. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Service
                                                				  Parameters and set the Built In Bridge Enable clusterwide service parameter to On . Note If this
                                                      				parameter is set to Off , configure cBarge for each phone by setting the Built in Bridge field in the Phone
                                                         				  Configuration window. | Note | If this
                                                      				parameter is set to Off , configure cBarge for each phone by setting the Built in Bridge field in the Phone
                                                         				  Configuration window. |
|---|---|---|---|
| Note | If this
                                                      				parameter is set to Off , configure cBarge for each phone by setting the Built in Bridge field in the Phone
                                                         				  Configuration window. |
| Step 2 | Set the Party
                                             			 Entrance Tone clusterwide service parameter to True (required for tones) or
                                          			 configure the Party Entrance Tone field in the Directory Number Configuration window. |
| Step 3 | Set the Single
                                             			 Button Barge/CBarge Policy to cBarge . Note If this
                                                      				parameter is set to Off , configure Single-button cBarge for each phone by
                                                      				setting the Single Button cBarge field in the Phone
                                                         				  Configuration window. | Note | If this
                                                      				parameter is set to Off , configure Single-button cBarge for each phone by
                                                      				setting the Single Button cBarge field in the Phone
                                                         				  Configuration window. |
| Note | If this
                                                      				parameter is set to Off , configure Single-button cBarge for each phone by
                                                      				setting the Single Button cBarge field in the Phone
                                                         				  Configuration window. |
| Step 4 | Set the Allow
                                             			 Barge When Ringing service parameter to True. |
| Step 5 | Click Save . |

| Note | If this
                                                      				parameter is set to Off , configure cBarge for each phone by setting the Built in Bridge field in the Phone
                                                         				  Configuration window. |
|---|---|

| Note | If this
                                                      				parameter is set to Off , configure Single-button cBarge for each phone by
                                                      				setting the Single Button cBarge field in the Phone
                                                         				  Configuration window. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > End User . |
|---|---|
| Step 2 | Specify the
                                          			 appropriate filters in the Find
                                             				User Where field to and then click Find to retrieve a list of users. |
| Step 3 | Select the
                                          			 user from the list. The End
                                             				User Configuration window appears. |
| Step 4 | Locate the Device
                                             				Information section. |
| Step 5 | Click Device
                                             				Association . The User
                                             				Device Association window appears. |
| Step 6 | Find and
                                          			 select the CTI remote device. |
| Step 7 | To complete
                                          			 the association, click Save
                                             				Selected/Changes . |
| Step 8 | From Related Links drop-down list, choose Back to User , and then click Go . The End User Configuration window appears, and the associated device that you chose appears in the Controlled Devices pane. |

| Feature | Interaction |
|---|---|
| cBarge | Cisco
                                          						recommends that you assign either the Barge or cBarge softkey to a softkey
                                          						template. By having only one of these softkeys for each device, you can prevent
                                          						confusion for users and avoid potential performance issues. Note You
                                                   						can enable Single-Button Barge or Single-Button cBarge for a device, but not
                                                   						both. | Note | You
                                                   						can enable Single-Button Barge or Single-Button cBarge for a device, but not
                                                   						both. |
| Note | You
                                                   						can enable Single-Button Barge or Single-Button cBarge for a device, but not
                                                   						both. |
| Call
                                          						Park | When the
                                          						target parks the call, the barge initiator gets released (if using the built-in
                                          						bridge), or the barge initiator and the other party remain connected (if using
                                          						the shared conference). |
| Join | When the
                                          						target joins the call with another call, the barge initiator gets released (if
                                          						using the built-in bridge), or the barge initiator and the other party remain
                                          						connected (if using the shared conference). |
| Private
                                          						Line Automatic Ringdown (PLAR) | A Barge,
                                          						cBarge, or Single-Button Barge initiator can barge into a call through a shared
                                          						line that is configured for Barge and Private Line Automatic Ringdown (PLAR).
                                          						The initiator can barge into the call if the barge target uses the
                                          						preconfigured number that is associated with the PLAR line while on the call.
                                          						Cisco Unified Communications Manager does not send the barge invocation to the
                                          						PLAR line before connecting the barge call, so the barge occurs regardless of
                                          						the state of the PLAR destination. To make
                                          						Barge, cBarge, or Single-Button Barge function with PLAR, you must configure
                                          						Barge, cBarge, or Single-Button Barge. In addition, you must configure the PLAR
                                          						destination, a directory number that is used specifically for PLAR. |

| Note | You
                                                   						can enable Single-Button Barge or Single-Button cBarge for a device, but not
                                                   						both. |
|---|---|

| Restriction | Description |
|---|---|
| Additional callers | The Barge initiator cannot
                                          			 conference in additional callers. |
| Computer Telephony Interface (CTI) | CTI does not support Barge
                                          			 through APIs that TAPI and JTAPI applications invoke. CTI generates events for
                                          			 Barge when it is invoked manually from an IP phone by using the Barge or cBarge
                                          			 softkey. |
| G.711 codec | The original call requires
                                          			 G.711 codec. If G.711 is not available, use cBarge instead. |
| Cisco Unified IP Phones | You can assign a softkey
                                          			 template that contains the Barge softkey to any IP phone that uses softkeys;
                                          			 however, some IP phones do not support the Barge feature. |
| Encryption | If you configure encryption
                                          			 for Cisco Unified IP Phones 7960 and 7940, those encrypted devices cannot
                                          			 accept a barge request when they are participating in an encrypted call. When
                                          			 the call is encrypted, the barge attempt fails. A tone plays on the phone to
                                          			 indicate that the Barge failed. |
| Maximum number of calls | If the number of
                                          			 shared-line users in the conference is equal to or greater than the
                                          			 configuration for the Maximum Number of Calls setting for the device from which
                                          			 you are attempting to barge, the phone displays the message, Error: Past Limit . |