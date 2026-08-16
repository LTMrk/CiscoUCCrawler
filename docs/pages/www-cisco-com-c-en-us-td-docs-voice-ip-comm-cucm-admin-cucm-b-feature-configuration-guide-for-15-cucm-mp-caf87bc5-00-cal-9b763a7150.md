---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-cucm-b-feature-configuration-guide-for-15-cucm-mp-caf87bc5-00-cal-9b763a7150
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/cucm_b_feature-configuration-guide-for-15/cucm_mp_caf87bc5_00_call-pickup-12-0.html
retrieved_at: 2026-08-16T16:04:21.585542+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: March 26, 2026

Chapter: Call Pickup

## Chapter: Call Pickup

# Call Pickup

## Call Pickup
                        	 Overview

The Call Pickup feature allows users to answer calls that come in on a directory number other than their own.

Consider a setup where phone A is the calling phone. Phone B and phone C are both associated with the same call pickup group.
                           If phone A calls phone B, phone B rings and phone C get the notification. To answer the call on phone C, the user must press
                           the Pickup softkey and answer the call to make the connection.

### Group Call Pickup
                           	 Overview

The Group Call Pickup feature allows users to pick up incoming calls in another group. Users must dial the appropriate call
                              pickup group number when this feature is activated from a Cisco Unified IP Phone. Users use the GPickUp softkey for this type of call pickup.

When a user invokes the Group Call Pickup phone feature while multiple calls are incoming to a pickup group, the user gets
                              connected to the incoming call that has been ringing the longest. Depending on the phone model, the users can either use the
                              Group Pickup programmable feature button or the Group Pickup softkey to pick up an incoming call. If Auto Group Call Pickup
                              is not enabled, the user must press the GPickUp softkey, dial the group number of another pickup group, and answer the call to make the connection.

Consider a setup where phone A is the calling phone and there are two call pickup groups namely, X and Y. Call pickup group
                              X is associated with phone B and phone C and call pickup group Y is associated with phone D. If phone A calls phone B, phone
                              B rings and phone C gets the notification. But phone D does not get any notification as it belongs to a pickup group that
                              is different from the one that phone B is associated with. To answer the call on phone D, the user must press the GPickup softkey, dial the group number of call pickup group X. Now phone D starts ringing and when the user answers the call on phone
                              D, phone A and phone D are connected.

### Other Group Pickup
                           	 Overview

The Other Group Pickup feature allows users to pick up incoming calls in a group that is associated with their own group.
                              The Unified Communications Manager automatically searches for the incoming call in the associated groups to make the call connection when the user activates
                              this feature from a Cisco Unified IP Phone. Users use the OPickUp softkey for this type of call pickup. If Auto Other Group Pickup is not enabled, the user must press the OPickUp and Answer
                              softkeys to make the call connection. Depending on the phone model, the users can either use the Call Pickup programmable
                              feature button or the Call Pickup softkey to pick up an incoming call.

When more than one associated group exists, the first associated group has the highest priority of answering calls for the
                              associated group. For example, groups A, B, and C associate with group X, the group A has the highest priority and the group
                              C has the lowest priority for answering calls. The group X picks up an incoming call in group A, though a call may have come
                              in group C before the incoming call in group A.

Each call pickup group can be associated with a maximum of 10 other call pickup groups.

Users can be assigned to only one call pickup group.

Multiple call pickup groups can exist within the same location, but each group name must be unique within that location.

### Directed Call
                           	 Pickup Overview

The Directed Call Pickup feature allows a user to pick up a ringing call on a DN directly by pressing the GPickUp or Group
                              Pickup softkeys and entering the directory number of the device that is ringing. If Auto Directed Call Pickup is not enabled,
                              the user must press the GPickUp softkey, dial the DN of the ringing phone, and answer the call that will now ring on the user
                              phone to make the connection. Unified Communications Manager uses the associated group mechanism to control the privilege of a user who wants to pick up an incoming call by using Directed
                              Call Pickup. The associated group of a user specifies one or more call pickup groups that are associated to the pickup group
                              to which the user belongs.

If a user wants to
                              		pick up a ringing call from a DN directly, the associated groups of the user
                              		must contain the pickup group to which the DN belongs. If two users belong to
                              		two different call pickup groups and the associated groups of the users do not
                              		contain the call pickup group of the other user, the users cannot invoke
                              		Directed Call Pickup to pick up calls from each other.

When the user
                              		invokes the Directed Call Pickup feature and enters a DN to pick up an incoming
                              		call, the user connects to the call that is incoming to the specified phone
                              		whether or not the call is the longest ringing call in the call pickup group to
                              		which the DN belongs. If multiple calls are ringing on a particular DN and the
                              		user invokes Directed Call Pickup to pick up a call from the DN, the user
                              		connects to the incoming call that has been ringing the specified DN the
                              		longest.

### BLF Call Pickup
                           	 Overview

The BLF Call Pickup feature allows Unified Communications Manager to notify a phone user when a call is waiting to be picked up from a BLF DN. The BLF call pickup initiator (the phone that
                              picks up the call) is selected as the next available line or as a specified line. To use a specified line, the line must remain
                              off hook before the BLF SD button is pressed. You can configure a hunt list member DN as the BLF DN to allow an incoming call
                              to a hunt list member to be picked up by the BLF call pickup initiator. The incoming call on the hunt list member can come
                              from the hunt list or be a directed call. The behavior in each case depends on how you configure call pickup for the hunt
                              list member DN, the BLF DN, and the hunt pilot number. When a Call Pickup occurs with the service parameter Auto Call Pickup
                              Enabled set to false, the phone must remain off hook or the user must press the answer key to pick up the call.

The BLF SD button on the phone can exist in any of the following states:

Idle—Indicates that no call exists on the BLF DN.

Busy—Indicates that at least one active call exists on the BLF DN, but no alerts exist.

Alert— Indicates by flashing that at least one incoming call exists on the BLF DN.

When there is an
                              		incoming call to the BLF DN, the BLF SD button flashes on the BLF call pickup
                              		initiator phone to indicate that an incoming call to the BLF DN exists. If Auto
                              		Call Pickup is configured, the user presses the BLF SD button on the call
                              		pickup initiator phone to pick up the incoming call. If auto call pickup is not
                              		configured, the phone must remain off hook, or the user must press the answer
                              		key to pick up the call.

## Call Pickup Configuration Task Flow

Step 1

Configure a Call Pickup Group

Call
                                                					 Pickup

Group Call
                                                					 Pickup

Other Call
                                                					 Pickup

Directed
                                                					 Call Pickup

BLF Call
                                                					 Pickup

You must
                                          				define groups with unique names and numbers.

Step 2

Assign a Call Pickup Group to Directory Numbers

Repeat this
                                          				procedure for each call pickup group that you create.

Step 3

Create
                                       			 another call pickup group and associate it with the BLF call pickup group that
                                       			 you created in Step 1 . You can associate a call pickup group with multiple BLF DN
                                       			 call pickup groups.

Perform this
                                          				step if you are configuring BLF Call Pickup.

You do not
                                                      				  always need to create another call pickup group. For example, you can have a
                                                      				  single call pickup group that includes both the initiator DN and the
                                                      				  destination DN. In such cases, associate the BLF call pickup group with itself.

Step 4

Configure Partitions for Call Pickup

You must
                                          				complete this procedure for directed call pickup. It is optional for other
                                          				types of call pickup.

Step 5

Configure Calling Search Space

You must
                                          				complete this procedure for directed all pickup. It is optional for other types
                                          				of call pickup.

Step 6

Assign a Call Pickup Group to Hunt Pilots

(Optional). Assign a call pickup group to a hunt pilot DN so that users can pick up calls that are alerting in the line group members.
                                          Hunt lists that are assigned to a call pickup group can use Call Pickup, Group Call pickup, BLF Call Pickup, Other Group Pickup,
                                          and Directed call pickup.

Step 7

Configure notifications:

- Configure Call Pickup Notification

- Configure Call Pickup Notification for a Directory Number

- Configure BLF Call Pickup Notification

Step 8

Configure
                                       			 Directed Call Pickup:

- Configure a Time Period

- Configure Time Schedule

- Associate a Time Schedule with a Partition

Before you
                                          				configure directed call pickup, you must configure partitions and calling
                                          				search spaces. With directed call pickup, the calling search space of the user
                                          				who requests the Directed Call Pickup feature must contain the partition of the
                                          				DN from which the user wants to pick up a call.

Time periods
                                          				and time schedules specify the times when members in the associated group are
                                          				available to accept calls.

Step 9

Configure automatic call answering:

- Configure Auto Call Pickup

- Configure BLF Auto Pickup

(Optional). Enable automatic call answering and configure timers for automatic call answering.

Step 10

Configure
                                       			 phone button templates:

- Configure Call Pickup Phone Button Template

- Associate Call Pickup Button Template with Phone

- Configure BLF Speed Dial Number for the BLF Call Pickup Initiator

Configure phone button templates for any of the call pickup features that you want to use:

Speed Dial BLF

Call Pickup

Group Call Pickup

Other Group Pickup

For Directed
                                          				Call Pickup, use the Group Call Pickup button.

Step 11

Configure Softkeys for Call Pickup

- Configure a Softkey Template for Call Pickup

- Associate a Softkey Template with a Common Device Configuration

- Associate a Softkey Template with a Phone

Configure softkeys for any of the call pickup features that you want to use:

Call Pickup (Pickup)

Group Call Pickup (GPickup)

Other Group Pickup (OPickup)

For
                                          				Directed Call Pickup, use the Group Call Pickup softkey.

### Configure a Call
                           	 Pickup Group

Step 1

From Cisco Unified CM Administration, choose Call Routing > Call Pickup Group .

Step 2

Click Add
                                             				New .

Step 3

Configure the fields in the Call Pickup Group Configuration window. For more information on the fields and their configuration options, see Online Help.

### Assign a Call
                           	 Pickup Group to Directory Numbers

#### Before you begin

Configure a Call Pickup Group

Step 1

Choose Device > Phone or Call
                                                				  Routing > Directory Number .

Step 2

Enter the appropriate search criteria to find the phone or
                                          			 directory number that you want to assign to a call pickup group and click Find.

A list of phones or directory numbers that match the search
                                             				criteria displays.

Step 3

Choose the phone or directory number to which you want to assign a
                                          			 call pickup group.

Step 4

From the Association Information list in the Phone Configuration window, choose the directory
                                          			 number to which the call pickup group will be assigned.

Step 5

From the Call Pickup Group drop-down list that displays
                                          			 in the Call Forward and Call Pickup Settings area, choose the desired call
                                          			 pickup group.

Step 6

To save the changes in the database, click Save.

#### What to do next

Configure Partitions for Call Pickup

Configure Calling Search Space

### Configure
                           	 Partitions for Call Pickup

You can restrict
                                 		  access to call pickup groups by assigning a partition to the call pickup group
                                 		  number. When this configuration is used, only the phones that have a calling
                                 		  search space that includes the partition with the call pickup group number can
                                 		  participate in that call pickup group. Make sure that the combination of
                                 		  partition and group number is unique throughout the system. You can create
                                 		  multiple partitions.

If you assign call
                                 		  pickup group numbers to a partition, only those phones that can dial numbers in
                                 		  that partition can use the call pickup group. If partitions represent tenants
                                 		  in a multitenant configuration, make sure that you assign the pickup groups to
                                 		  the appropriate partition for each tenant.

#### Before you begin

Assign a Call Pickup Group to Directory Numbers

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Partition .

Step 2

In
                                          			 the Partition
                                             				Name, Description field, enter a name for the partition that is
                                          			 unique to the route plan.

Step 3

Enter a
                                          			 comma (,) after the partition name and enter a description of the partition on
                                          			 the same line.

Step 4

To create
                                          			 multiple partitions, use one line for each partition entry.

Step 5

From the Time
                                             				Schedule drop-down list, choose a time schedule to associate with
                                          			 this partition.

Step 6

Select one
                                          			 of the following radio buttons to configure the Time
                                             				Zone :

- Originating
                                                				  Device —When you select this radio button, the system compares the
                                             				time zone of the calling device to the Time Schedule to determine whether the partition is
                                             				available is available to receive an incoming call.

- Specific Time
                                                				  Zone —After you select this radio button, choose a time zone from
                                             				the drop-down list. The system compares the chosen time zone to the Time Schedule to determine whether the partition is
                                             				available is available to receive an incoming call.

Step 7

Click Save .

### Configure Calling
                           	 Search Space

A calling
                                 		  search space is an ordered list of route partitions that are typically
                                 		  assigned to devices. Calling search spaces determine the partitions that
                                 		  calling devices can search when they are attempting to complete a call.

#### Before you begin

Configure Partitions for Call Pickup

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Calling Search Space .

Step 2

Click Add New .

Step 3

In the Name field, enter a name.

Ensure that
                                             				each calling search space name is unique to the system. The name can include up
                                             				to 50 alphanumeric characters and can contain any combination of spaces,
                                             				periods (.), hyphens (-), and underscore characters (_).

Step 4

In the Description field, enter a description.

The
                                             				description can include up to 50 characters in any language, but it cannot
                                             				include double-quotes ("), percentage sign (%), ampersand (&), back-slash
                                             				(\), or angle brackets (<>).

Step 5

From the Available Partitions drop-down list, perform one of
                                          			 the following steps:

- For a single partition,
                                             				select that partition.

- For multiple partitions,
                                             				hold down the Control (CTRL) key, then select the appropriate
                                             				partitions.

Step 6

Select the
                                          			 down arrow between the boxes to move the partitions to the Selected Partitions field.

Step 7

(Optional) Change the priority of selected partitions by using the arrow keys to the right
                                          			 of the Selected Partitions box.

Step 8

Click Save .

### Assign a Call
                           	 Pickup Group to Hunt Pilots

Only hunt lists
                                 		  that are assigned to a call pickup group can use Call Pickup, Group Call
                                 		  Pickup, BLF Call Pickup, Other Group Pickup, and Directed Call Pickup. Follow
                                 		  these steps to assign a call pickup group to hunt pilots:

#### Before you begin

Configure Calling Search Space

Step 1

From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Hunt Pilot .

Step 2

Enter the
                                          			 appropriate search criteria to find the hunt pilot that you want to assign to a
                                          			 call pickup group and click Find . A list of hunt pilots that match the search
                                          			 criteria appears.

Step 3

Choose the
                                          			 hunt pilot to which you want to assign a call pickup group.

Step 4

From the Call Pickup Group drop-down list that appears in the Hunt Forward Settings area, choose the desired call pickup group.

Step 5

Click Save .

### Configure Call
                           	 Pickup Notification

You can configure
                                 		  Call Pickup Notification at the system level, call pickup group level, or
                                 		  individual phone level.

#### Before you begin

Assign a Call Pickup Group to Hunt Pilots

Step 1

Configure Call Pickup Notification for a Call Pickup Group

To allow the
                                             				original called party to pick up the call prior to the audio and/or visual
                                             				alert being sent to the pickup group.

Step 2

Configure Call Pickup Notification for a Directory Number

Step 3

Configure BLF Call Pickup Notification

#### Configure Call
                              	 Pickup Notification for a Call Pickup Group

##### Before you begin

Assign a Call Pickup Group to Hunt Pilots

Step 1

From Cisco Unified CM Administration, choose Call Routing > Call Pickup Group .

Step 2

Configure the fields in the Call Pickup Group Notification Settings section in the Call Pickup Group Configuration window. See Call Pickup Notification Fields for Call Pickup for details about the fields and their configuration options.

Refer to Call Pickup Interactions and Restrictions for feature interactions and restrictions that will affect your Call Pickup configuration.

##### Call
                                 	 Pickup Notification Fields for Call Pickup

Field

Description

Call Pickup Group
                                                      				  Notification Policy

From the drop-down list, select the notification policy.
                                                      				  The available are options are No Alert, Audio Alert, Visual Alert, and Audio
                                                      				  and Visual Alert.

Call Pickup Group
                                                      				  Notification Timer

Enter the seconds of delay (integer in the range of 1 to
                                                      				  300) between the time that the call first comes into the original called party
                                                      				  and the time that the notification to the rest of the call pickup group is
                                                      				  sent.

Calling Party
                                                      				  Information

Check the check box if you want the visual notification message to
                                                      				  the call pickup group to include identification of the calling party. The
                                                      				  system only makes this setting available when the Call Pickup Group
                                                      				  Notification Policy is set to Visual Alert or Audio and Visual Alert.

The notification is sent only to the primary line of a device.

Called Party
                                                      				  Information

Check the check box if you want the visual notification message to
                                                      				  the call pickup group to include identification of the original called party.
                                                      				  The system makes this setting available when the Call Pickup Group Notification
                                                      				  Policy is set to Visual Alert or Audio and Visual Alert.

#### Configure Call
                              	 Pickup Notification for a Directory Number

Perform these
                                    		  steps to configure the type of audio notification that is provided when a phone
                                    		  is idle or in use.

##### Before you begin

Configure Call Pickup Notification for a Call Pickup Group

Step 1

From Cisco Unified CM Administration, choose Call Routing > Directory Number .

Step 2

Enter the
                                             			 search criteria and click Find .

Step 3

Click the
                                             			 directory number for which you want to configure the Call Pickup Notification.

Step 4

Choose a
                                             			 device name in the Associated Devices pane and click the Edit
                                                				Line Appearance button.

Step 5

From the Call
                                                				Pickup Group Audio Alert Setting(Phone Idle) drop-down list, choose
                                             			 one of the following:

Use System Default

Disable

Ring Once

Step 6

From the Call
                                                				Pickup Group Audio Alert Setting(Phone Active) drop-down list,
                                             			 choose one of the following:

Use System Default

Disable

Beep Only

Step 7

Click Save .

#### Configure BLF Call
                              	 Pickup Notification

##### Before you begin

Configure Call Pickup Notification for a Directory Number

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, choose the server that is running the Cisco CallManager service.

Step 3

From the Service drop-down list, choose Cisco CallManager .

Step 4

Configure the fields from Clusterwide Parameters (Device - Phone section in the Service Parameter Configuration window. See Service Parameter Fields for BLF Call Pickup Notification for more information about the fields and their configuration options.

##### Service Parameter Fields for BLF Call Pickup Notification

Field

Description

Call Pickup Group Audio Alert Setting of Idle Station

This parameter determines the kind of audio notification that is provided when a phone is idle (not in use) and it needs to
                                                   be alerted regarding an incoming call on its Call Pickup Group. Valid values are as follows:

Disable

Ring Once

Call Pickup Group Audio Alert Setting of Busy Station

This parameter determines the kind of audio notification that is provided when a phone is busy (in use) and it needs to be
                                                   alerted regarding an incoming call on its Call Pickup Group. Valid values are as follows:

Disable

Beep Only

BLF Pickup Group Audio Alert Setting of Idle Station

This parameter determines the kind of audio notification that is provided when a phone is idle and it needs to be alerted
                                                   regarding an incoming call on the BLF Pickup Button. Valid values are as follows:

No Ring

Ring Once

BLF Pickup Group Audio Alert Setting of Busy Station

This parameter determines the kind of audio notification that is provided when a phone is busy and it needs to be alerted
                                                   regarding an incoming call on the BLF Pickup Button. Valid values are as follows:

No Ring

Beep Only

### Configure Directed Call
                           	 Pickup

Step 1

Configure a Time Period

Step 2

Configure Time Schedule

Step 3

Associate a Time Schedule with a Partition

#### Configure a Time
                              	 Period

Use this procedure to define time periods. You can define a start time and an end time, and  
                                    			 also specify repetition interval either as days of the week or a specified date on the yearly calendar.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Time Period .

Step 2

Configure the fields in the Time Period Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 3

Click Save .

#### Configure Time
                              	 Schedule

##### Before you begin

Configure a Time Period

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Time Schedule .

Step 2

Configure the fields in the Time Schedule Configuration window. For more information on the fields and their configuration options, see Online Help.

#### Associate a Time
                              	 Schedule with a Partition

Associate time
                                    		  schedules with partitions to determine where calling devices search when they
                                    		  are attempting to complete a call during a particular time of day.

##### Before you begin

Configure Time Schedule

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Partition .

Step 2

From the Time Schedule drop-down list, choose a time schedule to
                                             			 associate with this partition.

Step 3

Click Save .

### Configure Automatic Call Answering

Step 1

Configure Auto Call Pickup

You can automate call pickup, group pickup, other group pickup, directed call pickup, and BLF call pickup. If you do not enable
                                             automatic call answering, users must press additional softkeys or dial group numbers to complete the connection.

Step 2

Configure BLF Auto Pickup

#### Configure Auto
                              	 Call Pickup

Auto call pickup connects the user to an incoming call. When the user presses the softkey on the phone, Unified Communications Manager locates the incoming call in the group and completes the call connection. You can automate call pickup, group pickup, other
                                    group pickup, directed call pickup, and BLF call pickup. If you do not enable automatic call answering, users must press additional
                                    softkeys or dial group numbers to complete the connection.

##### Before you begin

Associate a Time Schedule with a Partition

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, choose the server that is running the Cisco CallManager service.

Step 3

From the Service drop-down list, choose Cisco CallManager .

Step 4

In the Clusterwide Parameters (Feature – Call Pickup) section, select True or False from the Auto
                                                				Call Pickup Enabled drop-down list to enable or disable automatic
                                             			 call answering for call pickup groups.

Step 5

If the Auto
                                                				Call Pickup Enabled service parameter is False, enter a value from
                                             			 12 to 300 in the Call
                                                				Pickup No Answer Timer field. This parameter controls the time that
                                             			 a call takes to get restored if the call is picked up but not answered by using
                                             			 call pickup, group call pickup, or other group call pickup.

Step 6

In the Pickup
                                                				Locating Timer field, enter a value from 1 to 5. This service
                                             			 parameter specifies the maximum time, in seconds, for Cisco Unified
                                             			 Communications Manager to identify all alerting calls from all nodes in the
                                             			 cluster. This information is then used to help ensure that the call that has
                                             			 been waiting longest in the queue is delivered to the next user who presses the
                                             			 PickUp, GPickUp, or OPickUp softkey.

Step 7

Click Save .

#### Configure BLF Auto
                              	 Pickup

##### Before you begin

Configure Auto Call Pickup

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, choose the server that is running the Cisco CallManager service.

Step 3

From the Service drop-down list, choose Cisco CallManager .

Step 4

Configure
                                             			 values for the following clusterwide service parameters.

BLF Pickup Audio Alert Setting of Idle Station—Select True or False from the drop-down list to enable or disable automatic call answering for call pickup groups. The default value for this
                                                      service parameter is False.

BLF Pickup Audio Alert Setting of Busy Station—If the Auto Call Pickup Enabled service parameter is False, enter a value
                                                      from 12 to 300 (inclusive). This parameter controls the time that a call takes to get restored if the call is picked up but
                                                      not answered by using call pickup, group call pickup, or other group call pickup.

### Configure Call Pickup  Phone Buttons

Step 1

Configure Call Pickup Phone Button Template

Add Call Pickup feature to the phone button template.

Step 2

Associate Call Pickup Button Template with Phone

Step 3

Configure BLF Speed Dial Number for the BLF Call Pickup Initiator

#### Configure Call
                              	 Pickup Phone Button Template

Follow these steps
                                    		  to add Call Pickup feature to the phone button template.

##### Before you begin

Configure Automatic Call Answering

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

#### Associate Call
                              	 Pickup Button Template with Phone

##### Before you begin

Configure Call Pickup Phone Button Template

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

#### Configure BLF
                              	 Speed Dial Number for the BLF Call Pickup Initiator

##### Before you begin

Associate Call Pickup Button Template with Phone

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Select the
                                             			 phone that you want to use as the BLF call pickup initiator.

Step 3

In the Association pane, Add a
                                                				new BLF SD link.

Step 4

Select a Directory Number (BLF DN) that should be monitored
                                             			 by the BLF SD button.

Step 5

Check the Call
                                                				Pickup check box to use the BLF SD button for BLF Call Pickup
                                             			 and BLF Speed Dial. If you do not check this check box, the BLF SD button will
                                             			 be used only for BLF Speed Dial.

Step 6

Click Save .

### Configure Softkeys for Call Pickup

By default, the softkeys for Call Pickup are not available on a phone. You must configure a softkey template for any softkey
                                             to appear on the phone and be able to use it.

Step 1

Configure a Softkey Template for Call Pickup

Add the Pickup, GPickup, and OPickup softkeys to a softkey template.

Step 2

To Associate a Softkey Template with a Common Device Configuration , complete the following subtasks:

- Add a Softkey Template to Common Device Configuration

- Associate a Common Device Configuration with a Phone

Optional . To make the softkey template available to phones, you must complete either this step or the following step. Follow this
                                             step if your system uses a Common Device Configuration to apply configuration options to phones. This is the most commonly
                                             used method for making a softkey template available to phones.

Step 3

Associate a Softkey Template with a Phone

Optional . Use this procedure either as an alternative to associating the softkey template with the Common Device Configuration, or
                                             in conjunction with the Common Device Configuration. Use this procedure in conjunction with the Common Device Configuration
                                             if you need assign a softkey template that overrides the assignment in the Common Device Configuration or any other default
                                             softkey.

#### Configure a
                              	 Softkey Template for Call Pickup

Use this procedure to make the following call pickup softkeys available:

Softkey

Description

Call States

Call Pickup ( Pickup )

Allows you to answer a call on another extension in your group.

On Hook

Off Hook

Group Call Pickup ( GPickup )

Allows you to answer a call on extension outside your group.

On Hook

Off Hook

Other Group Pickup ( OPickup )

Allows you to answer a call ringing in another group that is associated with your group.

On Hook

Off Hook

##### Before you begin

Configure Call Pickup Phone Buttons

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

Perform one of the following tasks:

Associate a Softkey Template with a Common Device Configuration

Associate a Softkey Template with a Phone

#### Associate a
                              	 Softkey Template with a Common Device Configuration

Optional . There are two ways to associate a softkey template with a phone:

Add the softkey template to the Phone Configuration .

Add the softkey template to the Common Device Configuration .

The procedures in
                                    		  this section describe how to associate the softkey template with a Common
                                       			 Device Configuration . Follow these procedures if your system uses a Common
                                       			 Device Configuration to apply configuration options to phones. This
                                    		  is the most commonly used method for making a softkey template available to
                                    		  phones.

To use the alternative method, see Associate a Softkey Template with a Phone .

Step 1

Add a Softkey Template to Common Device Configuration

Step 2

Associate a Common Device Configuration with a Phone

##### Add a Softkey
                                 	 Template to Common Device Configuration

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

#### Associate a
                              	 Softkey Template with a Phone

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find to select the phone to add the softkey template.

Step 3

From the Softkey Template drop-down list, choose the template that contains the new softkey.

Step 4

Click Save .

## Call Pickup Interactions

Feature

Interaction

Route
                                          						Plan Report

The route plan report displays the patterns and DNs that are configured in Unified Communications Manager . Use the route plan report to look for overlapping patterns and DNs before assigning a DN to call pickup group.

Calling
                                          						search space and partitions

Assigning a partition to the Call Pickup Group number limits
                                          						call pickup access to users on the basis of the device calling search space.

Time of
                                          						Day (TOD)

Time of
                                          						Day (TOD) parameter for members in the associated group enable them to accept
                                          						calls within the same time period as their own group. TOD associates a time
                                          						stamp to the calling search space and partition.

Call
                                          						Accounting

When a call pickup occurs
                                          						  through auto call pickup, the system generates two call detail records (CDRs).
                                          						  One CDR applies to the original call that is cleared, and another CDR applies
                                          						  to the requesting call that is connected.

When a call pickup occurs
                                          						  via non-auto call pickup, the system generates one call detail record, which
                                          						  applies to the requesting call that is connected.

A CDR search returns all
                                          						  CDRs that match a specific time range and other search criteria. You can also
                                          						  search for a type of call that is associated with a particular CDR. The search
                                          						  result displays a call type field that indicates whether the call is a pickup
                                          						  call.

Call Forwarding

When a call pickup occurs with the service parameter Auto
                                          						Call Pickup Enabled set to false, the call forward that is configured on the
                                          						phone gets ignored when one of the pickup softkeys is pressed. If the call
                                          						pickup requestor does not answer the call, the original call gets restored
                                          						after the pickup no answer timer expires.

## Call Pickup
                        	 Restrictions

Restriction

Description

Different phone lines to different call pickup groups

Although
                                          						you can assign different lines on a phone to different call pickup groups,
                                          						Cisco does not recommend this setup because it can be confusing to users.

Call
                                          						Pickup Group Number

You
                                                							 cannot delete a call pickup group number when it is assigned to a line or DN.
                                                							 To determine which lines are using the call pickup group number, use Dependency
                                                							 Records in Call Pickup Configuration window. To delete a call
                                                							 pickup group number, reassign a new call pickup group number to each line or
                                                							 DN.

When
                                                							 you update a call pickup group number, Cisco Unified Communications Manager
                                                							 automatically updates all directory numbers that are assigned to that call
                                                							 pickup group.

SIP
                                          						Phones

The
                                                							 system does not support Call Pickup Notification on a few Cisco Unified IP
                                                							 Phones that run SIP.

Call
                                                							 Pickup Notification is only supported on licensed, third-party phones that run
                                                							 SIP.

Directed
                                          						Call Pickup

If a
                                                							 device that belongs to a hunt list rings due to a call that was made by calling
                                                							 the hunt pilot number, users cannot use the Directed Call Pickup feature to
                                                							 pick up such a call.

Users cannot pick up calls to a DN that belongs to a line group
                                                							 by using the Directed Call Pickup feature.

BLF
                                          						Pickup

The
                                          						system does not support Call Pickup Notification on a few Cisco Unified IP
                                          						Phones that run SIP.

Incoming Calling Party International Number Prefix - Phone

If you
                                          						have configured a prefix in the "Incoming Calling Party International Number Prefix - Phone 
                                             						" service parameter, and an international call is placed
                                          						to a member in the Call Pickup Group, the prefix does not get invoked in the
                                          						calling party field if the call gets picked up by another member of the Call
                                          						Pickup Group.

| Note | The longest
                                       		alerting call (longest ringing time) gets picked up first if multiple incoming
                                       		calls occur in that group. For other group call pickup, priority takes
                                       		precedence over the ringing time if multiple associated pickup groups are
                                       		configured. |
|---|---|

| Note | Each call pickup group can be associated with a maximum of 10 other call pickup groups. Users can be assigned to only one call pickup group. Multiple call pickup groups can exist within the same location, but each group name must be unique within that location. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure a Call Pickup Group | Configure a
                                       			 call pickup group for each of the call pickup features that you want to use: Call
                                                					 Pickup Group Call
                                                					 Pickup Other Call
                                                					 Pickup Directed
                                                					 Call Pickup BLF Call
                                                					 Pickup You must
                                          				define groups with unique names and numbers. |
| Step 2 | Assign a Call Pickup Group to Directory Numbers | Assign each
                                       			 of the call pickup groups that you created to the directory numbers that are
                                       			 associated with phones on which you want to enable call pickup. Directory
                                       			 numbers must be assigned to a call pickup group to use this feature. Repeat this
                                          				procedure for each call pickup group that you create. |
| Step 3 | Create
                                       			 another call pickup group and associate it with the BLF call pickup group that
                                       			 you created in Step 1 . You can associate a call pickup group with multiple BLF DN
                                       			 call pickup groups. | Perform this
                                          				step if you are configuring BLF Call Pickup. Note You do not
                                                      				  always need to create another call pickup group. For example, you can have a
                                                      				  single call pickup group that includes both the initiator DN and the
                                                      				  destination DN. In such cases, associate the BLF call pickup group with itself. | Note | You do not
                                                      				  always need to create another call pickup group. For example, you can have a
                                                      				  single call pickup group that includes both the initiator DN and the
                                                      				  destination DN. In such cases, associate the BLF call pickup group with itself. |
| Note | You do not
                                                      				  always need to create another call pickup group. For example, you can have a
                                                      				  single call pickup group that includes both the initiator DN and the
                                                      				  destination DN. In such cases, associate the BLF call pickup group with itself. |
| Step 4 | Configure Partitions for Call Pickup | Configure
                                       			 partitions to create a logical grouping of directory numbers (DN) with similar
                                       			 reachability characteristics. You can use partitions to restrict access to call
                                       			 pickup groups. If you assign call pickup group numbers to a partition, only
                                       			 those phones that can dial numbers in that partition can use the call pickup
                                       			 group. You must
                                          				complete this procedure for directed call pickup. It is optional for other
                                          				types of call pickup. |
| Step 5 | Configure Calling Search Space | If you
                                       			 configure partitions, you must also configure calling search spaces. Configure
                                       			 calling search spaces to identify the partitions that calling devices can
                                       			 search when they attempt to complete a call. You must
                                          				complete this procedure for directed all pickup. It is optional for other types
                                          				of call pickup. |
| Step 6 | Assign a Call Pickup Group to Hunt Pilots | (Optional). Assign a call pickup group to a hunt pilot DN so that users can pick up calls that are alerting in the line group members.
                                          Hunt lists that are assigned to a call pickup group can use Call Pickup, Group Call pickup, BLF Call Pickup, Other Group Pickup,
                                          and Directed call pickup. |
| Step 7 | Configure notifications: Configure Call Pickup Notification Configure Call Pickup Notification for a Directory Number Configure BLF Call Pickup Notification | (Optional). Configure notifications when other members of a pickup group receive a call. You can configure audio or visual notifications,
                                       or both. |
| Step 8 | Configure
                                       			 Directed Call Pickup: Configure a Time Period Configure Time Schedule Associate a Time Schedule with a Partition | Before you
                                          				configure directed call pickup, you must configure partitions and calling
                                          				search spaces. With directed call pickup, the calling search space of the user
                                          				who requests the Directed Call Pickup feature must contain the partition of the
                                          				DN from which the user wants to pick up a call. Time periods
                                          				and time schedules specify the times when members in the associated group are
                                          				available to accept calls. |
| Step 9 | Configure automatic call answering: Configure Auto Call Pickup Configure BLF Auto Pickup | (Optional). Enable automatic call answering and configure timers for automatic call answering. |
| Step 10 | Configure
                                       			 phone button templates: Configure Call Pickup Phone Button Template Associate Call Pickup Button Template with Phone Configure BLF Speed Dial Number for the BLF Call Pickup Initiator | Configure phone button templates for any of the call pickup features that you want to use: Speed Dial BLF Call Pickup Group Call Pickup Other Group Pickup For Directed
                                          				Call Pickup, use the Group Call Pickup button. |
| Step 11 | Configure Softkeys for Call Pickup Configure a Softkey Template for Call Pickup Associate a Softkey Template with a Common Device Configuration Associate a Softkey Template with a Phone | Configure softkeys for any of the call pickup features that you want to use: Call Pickup (Pickup) Group Call Pickup (GPickup) Other Group Pickup (OPickup) For
                                          				Directed Call Pickup, use the Group Call Pickup softkey. |

| Note | You do not
                                                      				  always need to create another call pickup group. For example, you can have a
                                                      				  single call pickup group that includes both the initiator DN and the
                                                      				  destination DN. In such cases, associate the BLF call pickup group with itself. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Call Pickup Group . The Find and List Call Pickup Groups window appears. |
|---|---|
| Step 2 | Click Add
                                             				New . The Call
                                             				Pickup Group Configuration window appears. |
| Step 3 | Configure the fields in the Call Pickup Group Configuration window. For more information on the fields and their configuration options, see Online Help. |

| Step 1 | Choose Device > Phone or Call
                                                				  Routing > Directory Number . |
|---|---|
| Step 2 | Enter the appropriate search criteria to find the phone or
                                          			 directory number that you want to assign to a call pickup group and click Find. A list of phones or directory numbers that match the search
                                             				criteria displays. |
| Step 3 | Choose the phone or directory number to which you want to assign a
                                          			 call pickup group. |
| Step 4 | From the Association Information list in the Phone Configuration window, choose the directory
                                          			 number to which the call pickup group will be assigned. |
| Step 5 | From the Call Pickup Group drop-down list that displays
                                          			 in the Call Forward and Call Pickup Settings area, choose the desired call
                                          			 pickup group. |
| Step 6 | To save the changes in the database, click Save. |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Partition . |
|---|---|
| Step 2 | In
                                          			 the Partition
                                             				Name, Description field, enter a name for the partition that is
                                          			 unique to the route plan. Partition
                                          			 names can contain alphanumeric characters, as well as spaces, hyphens (-), and
                                          			 underscore characters (_). See the online help for guidelines about partition
                                          			 names. |
| Step 3 | Enter a
                                          			 comma (,) after the partition name and enter a description of the partition on
                                          			 the same line. The
                                          			 description can contain up to 50 characters in any language, but it cannot
                                          			 include double quotes ("), percentage sign (%), ampersand (&), backslash
                                          			 (\), angle brackets (<>), or square brackets ([ ]). If you do
                                          			 not enter a description, Cisco Unified Communications Manager automatically
                                          			 enters the partition name in this field. |
| Step 4 | To create
                                          			 multiple partitions, use one line for each partition entry. |
| Step 5 | From the Time
                                             				Schedule drop-down list, choose a time schedule to associate with
                                          			 this partition. The time
                                          			 schedule specifies when the partition is available to receive incoming calls.
                                          			 If you choose None , the partition remains active at all times. |
| Step 6 | Select one
                                          			 of the following radio buttons to configure the Time
                                             				Zone : Originating
                                                				  Device —When you select this radio button, the system compares the
                                             				time zone of the calling device to the Time Schedule to determine whether the partition is
                                             				available is available to receive an incoming call. Specific Time
                                                				  Zone —After you select this radio button, choose a time zone from
                                             				the drop-down list. The system compares the chosen time zone to the Time Schedule to determine whether the partition is
                                             				available is available to receive an incoming call. |
| Step 7 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Calling Search Space . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | In the Name field, enter a name. Ensure that
                                             				each calling search space name is unique to the system. The name can include up
                                             				to 50 alphanumeric characters and can contain any combination of spaces,
                                             				periods (.), hyphens (-), and underscore characters (_). |
| Step 4 | In the Description field, enter a description. The
                                             				description can include up to 50 characters in any language, but it cannot
                                             				include double-quotes ("), percentage sign (%), ampersand (&), back-slash
                                             				(\), or angle brackets (<>). |
| Step 5 | From the Available Partitions drop-down list, perform one of
                                          			 the following steps: For a single partition,
                                             				select that partition. For multiple partitions,
                                             				hold down the Control (CTRL) key, then select the appropriate
                                             				partitions. |
| Step 6 | Select the
                                          			 down arrow between the boxes to move the partitions to the Selected Partitions field. |
| Step 7 | (Optional) Change the priority of selected partitions by using the arrow keys to the right
                                          			 of the Selected Partitions box. |
| Step 8 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Hunt Pilot . |
|---|---|
| Step 2 | Enter the
                                          			 appropriate search criteria to find the hunt pilot that you want to assign to a
                                          			 call pickup group and click Find . A list of hunt pilots that match the search
                                          			 criteria appears. |
| Step 3 | Choose the
                                          			 hunt pilot to which you want to assign a call pickup group. |
| Step 4 | From the Call Pickup Group drop-down list that appears in the Hunt Forward Settings area, choose the desired call pickup group. |
| Step 5 | Click Save . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Call Pickup Notification for a Call Pickup Group | To allow the
                                             				original called party to pick up the call prior to the audio and/or visual
                                             				alert being sent to the pickup group. |
| Step 2 | Configure Call Pickup Notification for a Directory Number | To configure
                                          			 the type of audio alert to be provided when phone is idle or has an active
                                          			 call. |
| Step 3 | Configure BLF Call Pickup Notification |  |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Call Pickup Group . The Call Pickup Group window appears. |
|---|---|
| Step 2 | Configure the fields in the Call Pickup Group Notification Settings section in the Call Pickup Group Configuration window. See Call Pickup Notification Fields for Call Pickup for details about the fields and their configuration options. Note Refer to Call Pickup Interactions and Restrictions for feature interactions and restrictions that will affect your Call Pickup configuration. | Note | Refer to Call Pickup Interactions and Restrictions for feature interactions and restrictions that will affect your Call Pickup configuration. |
| Note | Refer to Call Pickup Interactions and Restrictions for feature interactions and restrictions that will affect your Call Pickup configuration. |

| Note | Refer to Call Pickup Interactions and Restrictions for feature interactions and restrictions that will affect your Call Pickup configuration. |
|---|---|

| Field | Description |
|---|---|
| Call Pickup Group
                                                      				  Notification Policy | From the drop-down list, select the notification policy.
                                                      				  The available are options are No Alert, Audio Alert, Visual Alert, and Audio
                                                      				  and Visual Alert. |
| Call Pickup Group
                                                      				  Notification Timer | Enter the seconds of delay (integer in the range of 1 to
                                                      				  300) between the time that the call first comes into the original called party
                                                      				  and the time that the notification to the rest of the call pickup group is
                                                      				  sent. |
| Calling Party
                                                      				  Information | Check the check box if you want the visual notification message to
                                                      				  the call pickup group to include identification of the calling party. The
                                                      				  system only makes this setting available when the Call Pickup Group
                                                      				  Notification Policy is set to Visual Alert or Audio and Visual Alert. Note The notification is sent only to the primary line of a device. | Note | The notification is sent only to the primary line of a device. |
| Note | The notification is sent only to the primary line of a device. |
| Called Party
                                                      				  Information | Check the check box if you want the visual notification message to
                                                      				  the call pickup group to include identification of the original called party.
                                                      				  The system makes this setting available when the Call Pickup Group Notification
                                                      				  Policy is set to Visual Alert or Audio and Visual Alert. |

| Note | The notification is sent only to the primary line of a device. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Directory Number . The Find and List Directory Numbers window appears. |
|---|---|
| Step 2 | Enter the
                                             			 search criteria and click Find . |
| Step 3 | Click the
                                             			 directory number for which you want to configure the Call Pickup Notification. The Directory Number Configuration window appears. |
| Step 4 | Choose a
                                             			 device name in the Associated Devices pane and click the Edit
                                                				Line Appearance button. The Directory Number Configuration window refreshes to
                                             			 show the line appearance for this DN on the device that you choose. |
| Step 5 | From the Call
                                                				Pickup Group Audio Alert Setting(Phone Idle) drop-down list, choose
                                             			 one of the following: Use System Default Disable Ring Once |
| Step 6 | From the Call
                                                				Pickup Group Audio Alert Setting(Phone Active) drop-down list,
                                             			 choose one of the following: Use System Default Disable Beep Only |
| Step 7 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose the server that is running the Cisco CallManager service. |
| Step 3 | From the Service drop-down list, choose Cisco CallManager . |
| Step 4 | Configure the fields from Clusterwide Parameters (Device - Phone section in the Service Parameter Configuration window. See Service Parameter Fields for BLF Call Pickup Notification for more information about the fields and their configuration options. |

| Field | Description |
|---|---|
| Call Pickup Group Audio Alert Setting of Idle Station | This parameter determines the kind of audio notification that is provided when a phone is idle (not in use) and it needs to
                                                   be alerted regarding an incoming call on its Call Pickup Group. Valid values are as follows: Disable Ring Once |
| Call Pickup Group Audio Alert Setting of Busy Station | This parameter determines the kind of audio notification that is provided when a phone is busy (in use) and it needs to be
                                                   alerted regarding an incoming call on its Call Pickup Group. Valid values are as follows: Disable Beep Only |
| BLF Pickup Group Audio Alert Setting of Idle Station | This parameter determines the kind of audio notification that is provided when a phone is idle and it needs to be alerted
                                                   regarding an incoming call on the BLF Pickup Button. Valid values are as follows: No Ring Ring Once |
| BLF Pickup Group Audio Alert Setting of Busy Station | This parameter determines the kind of audio notification that is provided when a phone is busy and it needs to be alerted
                                                   regarding an incoming call on the BLF Pickup Button. Valid values are as follows: No Ring Beep Only |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure a Time Period | Configure
                                          			 time period for members of the associated groups to your group. |
| Step 2 | Configure Time Schedule | Configure
                                          			 time schedule for members of the associated groups to your group. |
| Step 3 | Associate a Time Schedule with a Partition | Associate time schedules with partitions to determine where calling devices search when they are attempting to complete a
                                          call during a particular time of a day. |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Time Period . |
|---|---|
| Step 2 | Configure the fields in the Time Period Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 3 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Time Schedule . |
|---|---|
| Step 2 | Configure the fields in the Time Schedule Configuration window. For more information on the fields and their configuration options, see Online Help. |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Partition . |
|---|---|
| Step 2 | From the Time Schedule drop-down list, choose a time schedule to
                                             			 associate with this partition. The time schedule specifies when the partition is available
                                             			 to receive incoming calls. If you choose None , the partition remains active at all
                                             			 times. |
| Step 3 | Click Save . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Auto Call Pickup | You can automate call pickup, group pickup, other group pickup, directed call pickup, and BLF call pickup. If you do not enable
                                             automatic call answering, users must press additional softkeys or dial group numbers to complete the connection. |
| Step 2 | Configure BLF Auto Pickup |  |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose the server that is running the Cisco CallManager service. |
| Step 3 | From the Service drop-down list, choose Cisco CallManager . |
| Step 4 | In the Clusterwide Parameters (Feature – Call Pickup) section, select True or False from the Auto
                                                				Call Pickup Enabled drop-down list to enable or disable automatic
                                             			 call answering for call pickup groups. |
| Step 5 | If the Auto
                                                				Call Pickup Enabled service parameter is False, enter a value from
                                             			 12 to 300 in the Call
                                                				Pickup No Answer Timer field. This parameter controls the time that
                                             			 a call takes to get restored if the call is picked up but not answered by using
                                             			 call pickup, group call pickup, or other group call pickup. |
| Step 6 | In the Pickup
                                                				Locating Timer field, enter a value from 1 to 5. This service
                                             			 parameter specifies the maximum time, in seconds, for Cisco Unified
                                             			 Communications Manager to identify all alerting calls from all nodes in the
                                             			 cluster. This information is then used to help ensure that the call that has
                                             			 been waiting longest in the queue is delivered to the next user who presses the
                                             			 PickUp, GPickUp, or OPickUp softkey. |
| Step 7 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose the server that is running the Cisco CallManager service. |
| Step 3 | From the Service drop-down list, choose Cisco CallManager . |
| Step 4 | Configure
                                             			 values for the following clusterwide service parameters. BLF Pickup Audio Alert Setting of Idle Station—Select True or False from the drop-down list to enable or disable automatic call answering for call pickup groups. The default value for this
                                                      service parameter is False. BLF Pickup Audio Alert Setting of Busy Station—If the Auto Call Pickup Enabled service parameter is False, enter a value
                                                      from 12 to 300 (inclusive). This parameter controls the time that a call takes to get restored if the call is picked up but
                                                      not answered by using call pickup, group call pickup, or other group call pickup. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Call Pickup Phone Button Template | Add Call Pickup feature to the phone button template. |
| Step 2 | Associate Call Pickup Button Template with Phone |  |
| Step 3 | Configure BLF Speed Dial Number for the BLF Call Pickup Initiator |  |

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

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Select the
                                             			 phone that you want to use as the BLF call pickup initiator. |
| Step 3 | In the Association pane, Add a
                                                				new BLF SD link. The Busy
                                                				Lamp Field Speed Dial Configuration window appears. |
| Step 4 | Select a Directory Number (BLF DN) that should be monitored
                                             			 by the BLF SD button. |
| Step 5 | Check the Call
                                                				Pickup check box to use the BLF SD button for BLF Call Pickup
                                             			 and BLF Speed Dial. If you do not check this check box, the BLF SD button will
                                             			 be used only for BLF Speed Dial. |
| Step 6 | Click Save . |

| Note | By default, the softkeys for Call Pickup are not available on a phone. You must configure a softkey template for any softkey
                                             to appear on the phone and be able to use it. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure a Softkey Template for Call Pickup | Add the Pickup, GPickup, and OPickup softkeys to a softkey template. |
| Step 2 | To Associate a Softkey Template with a Common Device Configuration , complete the following subtasks: Add a Softkey Template to Common Device Configuration Associate a Common Device Configuration with a Phone | Optional . To make the softkey template available to phones, you must complete either this step or the following step. Follow this
                                             step if your system uses a Common Device Configuration to apply configuration options to phones. This is the most commonly
                                             used method for making a softkey template available to phones. |
| Step 3 | Associate a Softkey Template with a Phone | Optional . Use this procedure either as an alternative to associating the softkey template with the Common Device Configuration, or
                                             in conjunction with the Common Device Configuration. Use this procedure in conjunction with the Common Device Configuration
                                             if you need assign a softkey template that overrides the assignment in the Common Device Configuration or any other default
                                             softkey. |

| Softkey | Description | Call States |
|---|---|---|
| Call Pickup ( Pickup ) | Allows you to answer a call on another extension in your group. | On Hook Off Hook |
| Group Call Pickup ( GPickup ) | Allows you to answer a call on extension outside your group. | On Hook Off Hook |
| Other Group Pickup ( OPickup ) | Allows you to answer a call ringing in another group that is associated with your group. | On Hook Off Hook |

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

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find to select the phone to add the softkey template. |
| Step 3 | From the Softkey Template drop-down list, choose the template that contains the new softkey. |
| Step 4 | Click Save . |

| Feature | Interaction |
|---|---|
| Route
                                          						Plan Report | The route plan report displays the patterns and DNs that are configured in Unified Communications Manager . Use the route plan report to look for overlapping patterns and DNs before assigning a DN to call pickup group. |
| Calling
                                          						search space and partitions | Assigning a partition to the Call Pickup Group number limits
                                          						call pickup access to users on the basis of the device calling search space. |
| Time of
                                          						Day (TOD) | Time of
                                          						Day (TOD) parameter for members in the associated group enable them to accept
                                          						calls within the same time period as their own group. TOD associates a time
                                          						stamp to the calling search space and partition. |
| Call
                                          						Accounting | When a call pickup occurs
                                          						  through auto call pickup, the system generates two call detail records (CDRs).
                                          						  One CDR applies to the original call that is cleared, and another CDR applies
                                          						  to the requesting call that is connected. When a call pickup occurs
                                          						  via non-auto call pickup, the system generates one call detail record, which
                                          						  applies to the requesting call that is connected. A CDR search returns all
                                          						  CDRs that match a specific time range and other search criteria. You can also
                                          						  search for a type of call that is associated with a particular CDR. The search
                                          						  result displays a call type field that indicates whether the call is a pickup
                                          						  call. |
| Call Forwarding | When a call pickup occurs with the service parameter Auto
                                          						Call Pickup Enabled set to false, the call forward that is configured on the
                                          						phone gets ignored when one of the pickup softkeys is pressed. If the call
                                          						pickup requestor does not answer the call, the original call gets restored
                                          						after the pickup no answer timer expires. |

| Restriction | Description |
|---|---|
| Different phone lines to different call pickup groups | Although
                                          						you can assign different lines on a phone to different call pickup groups,
                                          						Cisco does not recommend this setup because it can be confusing to users. |
| Call
                                          						Pickup Group Number | You
                                                							 cannot delete a call pickup group number when it is assigned to a line or DN.
                                                							 To determine which lines are using the call pickup group number, use Dependency
                                                							 Records in Call Pickup Configuration window. To delete a call
                                                							 pickup group number, reassign a new call pickup group number to each line or
                                                							 DN. When
                                                							 you update a call pickup group number, Cisco Unified Communications Manager
                                                							 automatically updates all directory numbers that are assigned to that call
                                                							 pickup group. |
| SIP
                                          						Phones | The
                                                							 system does not support Call Pickup Notification on a few Cisco Unified IP
                                                							 Phones that run SIP. Call
                                                							 Pickup Notification is only supported on licensed, third-party phones that run
                                                							 SIP. |
| Directed
                                          						Call Pickup | If a
                                                							 device that belongs to a hunt list rings due to a call that was made by calling
                                                							 the hunt pilot number, users cannot use the Directed Call Pickup feature to
                                                							 pick up such a call. Users cannot pick up calls to a DN that belongs to a line group
                                                							 by using the Directed Call Pickup feature. |
| BLF
                                          						Pickup | The
                                          						system does not support Call Pickup Notification on a few Cisco Unified IP
                                          						Phones that run SIP. |
| Incoming Calling Party International Number Prefix - Phone | If you
                                          						have configured a prefix in the "Incoming Calling Party International Number Prefix - Phone 
                                             						" service parameter, and an international call is placed
                                          						to a member in the Call Pickup Group, the prefix does not get invoked in the
                                          						calling party field if the call gets picked up by another member of the Call
                                          						Pickup Group. |