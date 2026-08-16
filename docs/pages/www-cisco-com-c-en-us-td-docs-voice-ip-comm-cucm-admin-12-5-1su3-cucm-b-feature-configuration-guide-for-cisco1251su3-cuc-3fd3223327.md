---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su3-cucm-b-feature-configuration-guide-for-cisco1251su3-cuc-3fd3223327
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU3/cucm_b_feature-configuration-guide-for-cisco1251su3/cucm_b_feature-configuration-guide-for-cisco1251su3_chapter_011101.html
retrieved_at: 2026-08-16T17:06:29.694697+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

Updated: July 31, 2025

Chapter: Call Park and Directed Call

## Chapter: Call Park and Directed Call

# Call Park and Directed Call

## Call Park Overview

The Call Park feature allows you to place a call on hold so that it can be retrieved from another phone in the Unified Communications Manager system (for example, a phone in another office or in a conference room). If you are on an active call, you can park the call
                              to a call park extension by pressing the Park softkey. Another phone in your system can then dial the call park extension
                              to retrieve the call.

You can define
                              		either a single directory number or a range of directory numbers for use as
                              		Call Park extension numbers. You can park only one call at each Call Park
                              		extension number.

The Call Park feature works within a Unified Communications Manager cluster, and each Unified Communications Manager node in a cluster must have Call Park extension numbers defined. You can define either a single directory number or a range
                              of directory numbers for use as Call Park extension numbers. Ensure that the directory number or range of numbers is unique.
                              If you use the same park ranges on different partitions, ensure that the users have only one partition in their CSS to be
                              able to park and retrieve the calls. Having multiple partitions may lead to incorrect partition selection.

Users can dial the assigned route pattern (for example, a route pattern for an intercluster trunk could be 80XX) and the Call
                              Park number (for example, 8022) to retrieve parked calls from another Unified Communications Manager cluster. You must ensure that calling search spaces and partitions are properly configured. Call Park works across clusters.

Valid Call Park extension numbers comprise integers and the wildcard character X. You can configure a maximum of XX in a Call
                              Park extension number (for example, 80XX), which provides up to 100 Call Park extension numbers. When a call gets parked,
                              the Unified Communications Manager chooses the next Call Park extension number that is available and displays that number on the phone.

### Park Monitoring

Park Monitoring is an optional Call Park feature where Cisco Unified Communications Manager monitors the status of a parked
                              call until a timer expires. After the timer expires, the call is forwarded to  a preassigned number, sent to voicemail, or
                              returned to the call parker. You can apply park monitoring to phone lines and to hunt pilots.

## Call Park
                        	 Prerequisites

If you
                              		  are using call park across clusters, you must have partitions and calling
                              		  search spaces configured.

Phone
                                          					 Model

Supported
                                          					 in Softkey Template

Supported
                                          					 in Phone Button Template

Cisco Unified IP Phone s 6900 series (except 6901 and 6911)

X

X

Cisco IP Phone 7800 Series

X

X

Cisco Unified IP Phone s 7900 series (except 7921, 7925, 7936, 7937)

X

Cisco IP Phone 8800 Series

X

X

Cisco Unified IP Phone s 8900 series

X

X

Cisco Unified IP Phone s 9900 series

X

X

Cisco Unified IP Phone s 7900 series (except 7906, 7911, 7921, 7925, 7936, 7937)

X

You can
                                          			 configure Call Park on any line (except line 1) or button by using the
                                          			 programmable line key feature.

## Call Park
                        	 Configuration Task Flow

### Before you begin

Review Call Park Prerequisites

Step 1

Configure Clusterwide Call Park

Step 2

Configure a Partition for Call Park

Create a
                                          				partition to add a Call Park Number

Step 3

Configure a Call Park Number

Step 4

Configure a Softkey Template for Call Park

Add the Park
                                          				softkey to a softkey template.

Step 5

To Associate a Softkey Template with a Common Device Configuration ,
                                       			 complete the following subtasks:

- Add a Softkey Template to a Common Device Configuration

- Associate a Common Device Configuration with a Phone

Optional. To make the softkey template available to phones, you must complete either this step or the following step. Follow this step
                                          if your system uses a Common Device Configuration to apply configuration options to phones. This is the most commonly used method for making a softkey template available to
                                          phones.

Step 6

Associate a Softkey with a Phone

Optional. Use this procedure either as an alternative to associating the softkey template with the Common Device Configuration, or
                                          in conjunction with the Common Device Configuration. Use this procedure in conjunction with the Common Device Configuration
                                          if you need assign a softkey template that overrides the assignment in the Common Device Configuration or any other default
                                          softkey assignment.

Step 7

To Configure Call Park Button ,
                                       			 complete the following subtasks:

- Configure a Phone Button Template for Call Park

- Associate a Button Template with a Phone

Step 8

Configure Park Monitoring

Complete this
                                          				optional task flow to add Park Monitoring to your Call Park configuration.

### Configure
                           	 Clusterwide Call Park

Step 1

Choose System > Service
                                                				  Parameters .

Step 2

Select the
                                          			 desired node as Server and the service as Cisco
                                             				CallManager (active).

Step 3

Click the Advanced .

The advanced service parameters are displayed in the window.

Step 4

In Clusterwide Parameter(Feature- General) section set the Enable cluster-wide Call
                                             				  Park Number/Ranges to True .

The default value is False. This parameter determines
                                             				  whether the Call Park feature is implemented clusterwide or restricted to a
                                             				  specific Unified CM node.

Step 5

Set the Call Park Display Timer for each server in a
                                          				  cluster that has the Cisco CallManager service and Call Park configured.

The
                                             				  default is 10 seconds. This parameter determines how long a Call Park number
                                             				  displays on the phone that parked the call.

Step 6

Set the Call Park Reversion Timer for each server in a cluster that has the Unified Communications Manager service and Call Park configured.

The default is 60 seconds. This parameter determines the time that a call remains parked. When this timer expires, the parked
                                             call returns to the device that parked the call. If a hunt group member parks a call that comes through a hunt pilot, the
                                             call goes back to the hunt pilot when the Call Park Reversion Timer expires.

If you enter a Call Park Reversion Timer value that is less than the Call Park Display Timer, Call Park numbers may not display
                                                         on the phone.

Step 7

Click Save .

Step 8

Restart all Unified Communications Manager and CTI Manager services.

### Configure a
                           	 Partition for Call Park

Configure
                                 		  partitions to create a logical grouping of directory numbers (DNs) and route
                                 		  patterns with similar reachability characteristics. Partitions facilitate call
                                 		  routing by dividing the route plan into logical subsets that are based on
                                 		  organization, location, and call type. You can configure multiple partitions.

#### Before you begin

(Optional) Configure Clusterwide Call Park

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Partition .

Step 2

Click Add
                                             				New to create a new partition.

Step 3

In
                                          			 the Partition
                                             				Name, Description field, enter a name for the partition that is
                                          			 unique to the route plan.

Step 4

Enter a
                                          			 comma (,) after the partition name and enter a description of the partition on
                                          			 the same line.

Step 5

To create
                                          			 multiple partitions, use one line for each partition entry.

Step 6

From the Time
                                             				Schedule drop-down list, choose a time schedule to associate with
                                          			 this partition.

Step 7

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

Step 8

Click Save .

### Configure a Call
                           	 Park Number

If you want to use
                                 		  Call Park across servers in a cluster, you must configure Call Park extension
                                 		  numbers on each server.

Ensure that each Call Park directory number, partition, and range is unique within the Unified Communications Manager . Each Unified Communications Manager to which devices are registered requires its own unique Call Park directory number and range. Cisco Unified Communications Manager Administration does not validate the Call Park numbers or range that you use to configure Call Park. To help identify invalid numbers or
                                 ranges and potential range overlaps, use the Unified Communications Manager Dialed Number Analyzer tool.

#### Before you begin

Configure a Partition for Call Park

Step 1

Choose Call
                                                				  Routing > Call Park .

Step 2

Perform one of
                                          			 the following tasks:

To add a
                                                   					 new Call Park number, click Add New .

To copy a
                                                   					 Call Park number, find the Call Park number or range of numbers and then click
                                                   					 the Copy icon.

To update
                                                   					 a Call Park number, find the Call Park number or range of numbers.

Step 3

Configure the fields in the Call Park configuration fields. See Call Park Configuration Fields for more information about the fields and their configuration options.

Step 4

To save the
                                          			 new or changed Call Park numbers in the database, click Save.

#### Call Park Configuration Fields

Field

Description

Call Park Number/Range

Enter the Call Park extension number. You can enter digits or
                                                					 the wildcard character X (the system allows one or two Xs). For example, enter
                                                					 5555 to define a single Call Park extension number of 5555 or enter 55XX to
                                                					 define a range of Call Park extension numbers from 5500 to 5599.

You can create a maximum of 100 Call Park numbers with one
                                                            						call park range definition. Make sure that the call park numbers are unique.

You cannot overlap call park numbers between Unified Communications Manager servers. Ensure that each Unified Communications Manager server has its own number range.

The call park range is selected from the list of servers
                                                            						where the call originates. For example, if phoneA (registered to nodeA) calls
                                                            						phone B (registered to nodeB) and the phoneB user presses Park, phoneB
                                                            						requires a call park range in the CSS that resides on nodeA. In a multinode
                                                            						environment where phones and gateways communicate with various nodes and where
                                                            						calls that originate from any server may need to be parked, the phones require
                                                            						a CSS that contains call park ranges from all servers.

Description

Provide a brief description of this call park number. The
                                                					 description can include up to 50 characters in any language, but it cannot
                                                					 include double-quotes (“), percentage sign (%), ampersand (&), or angle
                                                					 brackets (<>).

Partition

If you want to use a partition to restrict access to the call
                                                					 park numbers, choose the desired partition from the drop-down list. If you do
                                                					 not want to restrict access to the call park numbers, choose <None> for
                                                					 the partition.

Make sure that the combination of call park extension number and partition is unique within the Unified Communications Manager .

Unified Communications Manager

Using the drop-down list, choose the Cisco Unified Communications Manager to which these call park numbers apply.

### Configure a
                           	 Softkey Template for Call Park

Use this
                                 		  procedure to make the Park softkey available.

Park softkey has the following call states:

On Hook

Ring Out

Connected Transfer

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

### Associate a Softkey Template with a Common Device Configuration

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

To use the alternative method, see the section Associate a Softkey Template with a Phone .

Step 1

Add a Softkey Template to a Common Device Configuration

Step 2

Associate a Common Device Configuration with a Phone

#### Add a Softkey
                              	 Template to a Common Device Configuration

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

#### Associate a Common Device Configuration with a Phone

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

### Associate a Softkey
                           	 with a Phone

Optional . Use this procedure as an alternative to associating the softkey template with the Common Device Configuration. This procedure
                                 also works in conjunction with the Common Device Configuration. You can use it when you need to assign a softkey template
                                 that overrides the assignment in the Common Device Configuration or any other default softkey assignment.

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

### Configure Call
                           	 Park Button

#### Configure a Phone
                              	 Button Template for Call Park

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

#### Associate a Button
                              	 Template with a Phone

##### Before you begin

Configure a Phone Button Template for Call Park

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

### Configure Park
                           	 Monitoring

Complete these optional tasks to add Park Monitoring to your Call Park configuration.

#### Before you begin

Park Monitoring is supported on only a subset of phones that support Call Park. The following Cisco Unified IP Phones support
                                 Park Monitoring:

Cisco IP Phone 8811

Cisco IP Phone 8841

Cisco IP Phone 8845

Cisco IP Phone 8851

Cisco IP Phone 8851NR

Cisco IP Phone 8861

Cisco IP Phone 8865

Cisco IP Phone 8865NR

Cisco Unified IP Phone 8961

Cisco Unified IP Phone 9951

Cisco Unified IP Phone 9971

Step 1

Configure Park Monitoring System Timers

Configure system-level timers for the Park Monitoring feature.

Step 2

Configure Park Monitoring for Hunt Pilots

Step 3

Configure Park Monitoring for a Directory Number

Step 4

Configure Park Monitoring via Universal Line Template

If you have an LDAP directory sync configured, you can use universal line templates  to provision directory number settings
                                             for multiple users with park monitoring configured.

#### Configure Park Monitoring System Timers

Use this procedure to configure system-level timers for the Park Monitoring feature.

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, select the publisher node.

Step 3

From the Service drop-down list, select Cisco CallManager .

Step 4

Configure values for the following service parameters:

Park Monitoring Reversion Timer —The number of seconds that Cisco Unified Communications Manager waits before prompting the user to retrieve a parked call.
                                                      For individual phone lines, this setting can be overridden by the same setting in the Directory Number Configuration window. When the call park reversion timer expires, the call will be forwarded to the hunt pilot.

Park Monitoring Periodic Reversion Timer —The number of seconds between reversion attempts when a call has been parked. Cisco Unified Communications Manager prompts
                                                      the user about the parked call by ringing, beeping, or flashing the parker's phone. When the park monitoring reversion timer
                                                      expires, the call will be forwarded to the parked party and not the hunt pilot.

Park Monitoring Forward No Retrieve Timer —The number of seconds that park reminder notifications occur before the parked call is forwarded to the Park Monitoring Forward No Retrieve destination specified in the call parker's Directory Number configuration. When park monitoring forward no retrieve timer
                                                      expires, the call will be forwarded to the hunt pilot.

For additional details on these fields, see the service parameter online help.

Step 5

Click Save .

##### What to do next

Use any of these optional tasks to assign how expired timers get handled for individual phones lines and hunt pilots:

Configure Park Monitoring for Hunt Pilots

Configure Park Monitoring for a Directory Number

Configure Park Monitoring via Universal Line Template

#### Configure Park
                              	 Monitoring for Hunt Pilots

If your
                                    		  deployment uses hunt pilots, use this optional procedure to assign a Park
                                    		  Monitoring destination to a hunt pilot.

For general information on setting up hunt pilots, see the "Configure Hunt Pilots" chapter of the System Configuration Guide for Cisco Unified Communications Manager .

##### Before you begin

Configure Park Monitoring System Timers

Step 1

From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Hunt Pilot .

Step 2

Click Find and select the hunt pilot on which you want to
                                             			 configure a Park Monitoring destination.

Step 3

In the Park
                                                				Monitoring No Retrieve Destination field, assign a Destination directory number and Calling Search Space .

Step 4

Complete any remaining fields in the Hunt Pilot Configuration window. For more information on the fields and their configuration options, see Online Help.

Step 5

Click Save.

#### Configure Park
                              	 Monitoring for a Directory Number

Use this procedure
                                    		  to assign a Park Monitoring destination for an individual phone line. You can
                                    		  forward calls to another number, send to voicemail, or return to the call
                                    		  parker.

The following
                                                			 tools are available to provision settings for multiple phone lines:

Use a
                                                      				  universal line template to provision park monitoring settings for multiple
                                                      				  phone lines via an LDAP directory sync. For details, see Configure Park Monitoring via Universal Line Template .

Use the Bulk Administration Tool to import a CSV file with settings for a large number of phone lines. For more information,
                                                      see the Bulk Administration Guide for Cisco Unified Communications Manager .

##### Before you begin

Configure Park Monitoring System Timers

Step 1

From Cisco Unified CM Administration, choose Call Routing > Directory Number .

Step 2

Click Find and select the directory number that you want
                                             			 to configure.

Step 3

Enter values
                                             			 for the following Park
                                                				Monitoring fields:

Park Monitoring Forward No Retrieve Destination
                                                         						External —When the Park Monitoring Forward No Retrieve Timer
                                                      					 expires, and the parkee is an external party, the call is forwarded either to
                                                      					 voicemail or to a specified directory number. If this field s empty, the call
                                                      					 is redirected to the call parker’s line.

Park Monitoring Forward No Retrieve Destination
                                                         						Internal —When the Park Monitoring Forward No Retrieve Timer
                                                      					 expires, and the parkee is an internal party, the call is forwarded either to
                                                      					 voicemail or to a specified directory number. If this field s empty, the call
                                                      					 is redirected to the call parker’s line.

Park Monitor Reversion Timer —The number of seconds
                                                      					 that Cisco Unified Communications Manager waits before prompting the user to
                                                      					 retrieve a call parked on this phone line. If the value is 0 or empty, then
                                                      					 Cisco Unified Communications Manager uses the value of the Park Monitor Reversion Timer service parameter.

Step 4

Complete any remaining fields in the Directory Number Configuration window. For more information on the fields and their configuration options, see Online Help.

Step 5

Click Save .

#### Configure Park
                              	 Monitoring via Universal Line Template

Use this procedure
                                    		  to assign park monitoring settings to a universal line template. If you have an
                                    		  LDAP directory sync configured, you can use the universal line template
                                    		  configuration to provision directory number settings with park monitoring
                                    		  configured for multiple users.

##### Before you begin

Configure Park Monitoring System Timers

Step 1

From Cisco Unified CM Administration, choose User Management > User Phone/Add > Universal Line Template .

Step 2

Perform one of
                                             			 the following steps:

Click Find and select an existing template.

Click Add New to create a new template.

Step 3

Expand the Park
                                                				Monitoring Settings section and complete the fields. For field
                                             			 descriptions, see Park Monitoring Settings for Universal Line Templates .

Step 4

Click Save .

##### What to do next

To apply the universal line template to individual directory numbers, you must assign the template to a user profile, feature
                                    group template, and LDAP directory sync. When the sync occurs, the template settings get applied to the phone lines that are
                                    a part of the sync. For LDAP setup, see the "Configure End Users" chapters in the System Configuration Guide for Cisco Unified Communications Manager .

##### Park Monitoring Settings for Universal Line Templates

The following table contains the Park Monitoring fields in the Universal Line Template Configuration window of Cisco Unified Communications Manager.

Field

Description

Forward Destination for External Calls When Not Retrieved

When the person whose call is parked is an external party and the Park Monitoring Forward No Retrieve Timer expires, the system sends the call to one of these destinations:

Voicemail —Uses the configuration in Voice Mail Profile to determine where to send the call.

Revert to Originator —Returns the call to the call parker.

To forward calls to another number, input the other number in the text box.

If no option is selected, the call returns to the call parker.

Calling Search Space for Forwarding External Calls When Not Retrieved

If you have configured parked calls to be redirected to a configured number, select the calling search space for the forward
                                                   destination.

Forward Destination for Internal Calls When Not Retrieved

When the person whose call is parked is an internal party and the Park Monitoring Forward No Retrieve Timer expires, the system sends the call to one of these destinations:

Voicemail —Uses the configuration in Voice Mail Profile to determine where to send the call.

Revert to Originator —Returns the call to the call parker.

To forward calls to another number, input the other number in the text box.

If no option is selected, the call returns to the call parker.

Calling Search Space for Forwarding Internal Calls When Not Retrieved

If you have configured parked calls to be redirected to a configured number, select the calling search space for the forward
                                                   destination.

Park Monitor Reversion Timer (seconds)

This timer determines the number of seconds
                                                   that Unified Communications Manager waits before prompting the user
                                                   to retrieve a call that the user parked. This timer starts when the
                                                   user presses the Park softkey on the phone, and a reminder is
                                                   issued when the timer expires. The default value is 60
                                                   seconds.

## Call Park
                        	 Interactions

Feature

Interaction

CTI
                                          						Applications

CTI
                                          						applications access call park functionality, including monitoring activity on
                                          						call park DNs. To monitor a call park DN, add an application or end user that
                                          						is associated with the CTI application to the Standard CTI Allow Call Park
                                          						Monitoring user group.

Music On
                                          						Hold

Music On Hold allows users to place calls on hold with music that a streaming source provides. The Music On Hold audio source
                                          for Call Park is selected by the setting of the Network Hold MOH Audio Source setting within the Phone Configuration window. If you do not choose an audio source within the device configuration, Cisco Unified CM uses the audio source that
                                          is defined in the device pool or the system default if the device pool does not specify an audio source ID.

Route
                                          						Plan Report

The route plan report displays the patterns and directory numbers that are configured in Unified Communications Manager . Use the route plan report to look for overlapping patterns and directory numbers before assigning a directory number to
                                          Call Park.

Calling
                                          						Search Space and Partitions

Assign
                                          						the call park directory number or range to a partition to limit call park
                                          						access to users on the basis of the device calling search space.

Immediate Divert

Call
                                          						Park supports Immediate Divert (iDivert or Divert softkey). For example, user A
                                          						calls user B, and user B parks the call. User B retrieves the call and then
                                          						decides to send the call to a voice-messaging mailbox by pressing the iDivert
                                          						or Divert softkey. User A receives the voice mail greeting of user B.

Barge

Barge with Call Park–The target phone (the phone that is being barged upon) controls the call. The barge initiator "piggybacks" on the target phone. The target phone includes most of the common features, even when the target is being barged; therefore,
                                                the barge initiator has no feature access. When the target parks a call, the barge initiator then must release its call (the
                                                barge).

cBarge with Call Park–The target and barge initiator act as peers. The cBarge feature uses a conference bridge, which causes
                                                it to function like a MeetMe conference. Both phones (target and barge initiator) have full access to their features.

Directed
                                          						Call Park

We
                                          						recommend that you do not configure both Directed Call Park and the Park
                                          						softkey for Call Park, but the possibility exists to configure both. If you
                                          						configure both, ensure that the call park and directed call park numbers do not
                                          						overlap.

QSIG
                                          						Intercluster Trunks

When a
                                          						user parks a call across a QSIG intercluster trunk or a QSIG gateway trunk, the
                                          						caller who has been parked (the parkee) does not see the To parked number
                                          						message. The phone continues to display the original connected number. The call
                                          						has been parked, and the user who parked the call can retrieve it. When the
                                          						call is retrieved from the parked state, the call continues, but the caller who
                                          						was parked does not see the newly connected number.

## Call Park
                        	 Restrictions

Feature

Restriction

Call Park

Unified Communications Manager can park only one call at each call park extension number.

Shared Line

For shared line devices across nodes, the line registers to
                                          						the node on which the device registers first. For example, if a device from
                                          						subscriber2 registers first and the line is created in subscriber2 and the
                                          						publisher node, the line belongs to subscriber2. Each node must be configured
                                          						with the call park number.

Backup

To achieve failover or fallback, configure call park numbers
                                          						on the publisher node and subscriber nodes. With this configuration, when the
                                          						primary node is down, the line device association gets changed to the secondary
                                          						node, and the secondary node call park number gets used.

Directed Call Park

If a directed call park (or call park) is initiated from a
                                          						shared line and the call is not retrieved from any device, the parked call does
                                          						not always get reverted to the recipient in the shared line (parker).

Conference

When a conference call is set up between both the shared line and the caller on park reversion or park reversion fails causing
                                          a two-party call (between the other shared line and caller). The reason is that, on park reversion, Unified Communications Manager extends the call to both devices sharing the line and tries to add either party in conference (party already in conference
                                          or party that hit the park). If the party attempts to add the party who is already in the conference first, then the park
                                          reversion fails. When park reversion fails, the shared line can still barge into the call as usual.

Delete
                                          						Server

If any call park numbers are configured for Unified Communications Manager on a node that is being deleted in the Server Configuration window ( System > Server ), the node deletion fails. Before you can delete the node, you must delete the call park numbers in Cisco Unified Communications Manager Administration .

## Troubleshooting Call Park

### User Cannot Park
                           	 Calls

#### Problem

User cannot park calls. When the user presses the Park softkey or
                                 		  feature button, the call does not get parked.

#### Solution

Ensure that a unique call park number is assigned to each Unified Communications Manager in the cluster.

The partition that is assigned to the call park number does not match the partition that is assigned to the phone directory
                                 number. For more information on partition, see the System Configuration Guide for Cisco Unified Communications Manager .

### Call Park Number
                           	 is Not Displayed Long Enough

#### Problem

The call park number is not displayed long enough for the user.

#### Solution

Set the Call Park Display Timer to a longer duration. See Configure Clusterwide Call Park for more information about the Timer.

## Directed Call Park
                        	 Overview

Directed Call Park
                           		allows a user to transfer a call to an available user-selected directed call
                           		park number. Configured Directed Call Park numbers exist cluster-wide. You can
                           		configure phones that support the directed call park Busy Lamp Field (BLF) to
                           		monitor the busy or idle status of specific directed call park numbers. Users
                           		can also use the BLF to speed dial a directed call park number.

Unified Communications Manager can park only one call at each directed call park number. To retrieve a parked call, a user must dial a configured retrieval
                           prefix followed by the directed call park number at which the call is parked.

## Directed Call Park Prerequisites

Make sure that the phones in your deployment support Directed Call Park. For a list of  supported phones, run the Phone Feature List report from Cisco Unified Reporting, selecting Assisted Directed Call Park as the feature. For details, see Generate a Phone Feature List .

## Directed Call Park
                        	 Configuration Task Flow

### Before you begin

Review Directed Call Park Prerequisites

Step 1

Configure ClusterWide Directed Call Park

To configure
                                          				clusterwide parameter for directed call park.

Step 2

Configure a Directed Call Park Number

Step 3

Configure BLF/Directed Call Park Buttons

Configure a
                                          				phone button template for BLF/Directed Call Park.

Step 4

Synchronize Directed Call Park with Affected Devices

### Configure
                           	 ClusterWide Directed Call Park

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

To set the timer, update the Call Park Reversion
                                             				  Timer fields in the  Clusterwide Parameter(Feature- General) section.

The default is 60 seconds. This parameter determines the time that a call
                                             				  remains parked. When this timer expires, the parked call returns to the device
                                             				  that parked the call or to  another specified number, depending on what you configure in the Directed Call Park Configuration window.

### Configure a
                           	 Directed Call Park Number

#### Before you begin

Ensure that each directed call park directory number, partition, and range is unique within the Unified Communications Manager . Before you begin, generate a route plan report. If the Park softkey is also activated (not recommended), ensure that no
                                 overlap exists between call park numbers and directed call park numbers. If reversion number is not configured, the call reverts
                                 to the parker (parking party) after the Call Park Reversion Timer expires.

Configure ClusterWide Directed Call Park

Step 1

Choose Call
                                                				  Routing > Directed Call Park .

Step 2

Perform one of
                                          			 the following tasks:

To add a
                                                   					 new directed call park number, click Add New .

To copy a
                                                   					 directed call park number, find the directed call park number or range of
                                                   					 numbers and then click the Copy icon.

To update
                                                   					 a directed call park number, find the directed call park number or range of
                                                   					 numbers.

The directed call park number configuration window is
                                             				displayed.

Step 3

Configure the fields in the Directed Call Park settings area. See Directed Call Park Configuration Settings for more information about the fields and their configuration options.

Step 4

To save the
                                          			 new or changed call park numbers in the database, click Save.

If you update a directed call park number, Unified Communications Manager reverts any call that is parked on that number only after the Call Park Reversion Timer expires.

Step 5

Click Apply
                                             				Config .

The Apply
                                                				  Configuration Information dialog is displayed.

Step 6

Click OK.

Step 7

If you are using BLF to monitor directed Call Park numbers, click Restart Devices on the Directed Call Park Configuration window. This step is optional if you are using change notification.

#### Directed Call Park
                              	 Configuration Settings

Field

Description

Number

Enter
                                                						the directed call park number. You can enter digits (0-9) or the wildcard
                                                						character ([], - , *, ^, #) and X (the system allows one or two Xs). For
                                                						example, enter 5555 to define a single call park number of 5555 or enter 55XX
                                                						to define a range of directed call park extension numbers from 5500 to 5599.
                                                						Make sure that the directed call park numbers are unique and that they do not
                                                						overlap with call park numbers.

Description

Provide
                                                						a brief description of this directed call park number or range. The description
                                                						can include up to 50 characters in any language, but it cannot include double
                                                						quotation marks (“), percentage sign (%), ampersand (&), or angle brackets
                                                						(<>) and tabs.

Partition

If you
                                                						want to use a partition to restrict access to the directed call park numbers,
                                                						choose the desired partition from the drop-down list. If you do not want to
                                                						restrict access to the directed call park numbers, leave the partition as the
                                                						default of <None>.

Make sure that the combination of directed call park number and partition is unique within Unified Communications Manager .

Reversion Number

Enter
                                                						the number to which you want the parked call to return if not retrieved, or
                                                						leave the field blank.

A
                                                            						  reversion number can comprise digits only; you cannot use wildcards.

Reversion Calling Search Space

Using
                                                						the drop-down list, choose the calling search space or leave the calling search
                                                						space as the default of <None>.

Retrieval Prefix

For this
                                                						required field, enter the prefix for retrieving a parked call. The system needs
                                                						the retrieval prefix to distinguish between an attempt to retrieve a parked
                                                						call and an attempt to initiate a directed park.

### Configure
                           	 BLF/Directed Call Park Buttons

#### Before you begin

Configure ClusterWide Directed Call Park

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Phone Button Template .

Step 2

After the
                                          			 configuration window displays, click the Add a
                                             				new BLF Directed Call Park link in the Association Information
                                          			 pane.

The link does not display in the Association Information pane if the phone button template that you applied to the phone or
                                                         device profile does not support BLF/Directed Call Park.

Step 3

Configure the fields in the BLF/Directed Call Park fields area. See BLF/Directed Call Park Configuration Fields for more information about the fields and their configuration options.

Step 4

After you
                                          			 complete the configuration, click Save and close the window.

The directory
                                             				numbers are displayed in the Association Information pane of the Phone
                                             				Configuration Window.

#### BLF/Directed Call
                              	 Park Configuration Fields

Field

Description

Directory
                                                					 Number

The Directory Number drop-down list displays a list of Directed Call Park number that exist in the Unified Communications Manager database.

For phones
                                                					 that are running SCCP or phones that are running SIP, choose the number (and
                                                					 corresponding partition, if it is displayed) that you want the system to dial
                                                					 when the user presses the speed-dial button; for example, 6002 in 3. Directory
                                                					 numbers that display without specific partitions belong to the default
                                                					 partition.

Label

Enter the
                                                					 text that you want to display for the BLF/Directed Call Park button.

This field
                                                					 supports internationalization. If your phone does not support
                                                					 internationalization, the system uses the text that displays in the Label ASCII
                                                					 field.

Label
                                                					 ASCII

Enter the
                                                					 text that you want to display for the BLF/Directed Call Park button.

The ASCII
                                                					 label represents the noninternationalized version of the text that you enter in
                                                					 the Label field. If the phone does not support internationalization, the system
                                                					 uses the text that displays in this field.

### Synchronize
                           	 Directed Call Park with Affected Devices

Step 1

Choose Call
                                                				  Routing > Directed Call Park .

The Find
                                                				  and List Directed Call Parks window is displayed.

Step 2

Choose the
                                          			 search criteria to use.

Step 3

Click Find.

The window
                                             				displays a list of directed call parks that match the search criteria.

Step 4

Click the
                                          			 directed call park to which you want to synchronize applicable devices.
                                          			 The Directed Call
                                             				Park Configuration window is displayed.

Step 5

Make any
                                          			 additional configuration changes.

Step 6

Click Save.

Step 7

Click Apply
                                             				Config .

The Apply
                                                				  Configuration Information dialog is displayed.

Step 8

Click OK.

## Directed Call Park
                        	 Interactions

The following
                              		  table describes feature interactions with the Directed Call Park feature.

Feature

Interaction

Music On
                                          						Hold

The Music On Hold Audio Source for directed call park is assigned via the Default Network Hold MOH Audio Source service parameter. To assign the parameter:

From Cisco Unified CM Administration, choose System > Service Parameters .

From the Server drop-down list, choose a Unified Communications Manger cluster node.

From the Service drop-down list, select Cisco CallManager .

Under Clusterwide Paramters (Service) , assign a MOH audio source to the Default Network Hold MOH Audio Source ID parameter. The default is 1 .

Click Save .

Calling
                                          						Search Space and Partitions

Assign
                                          						the Directed Call Park Directory number or range to a partition to limit
                                          						Directed Call Park access to users on the basis of the device calling search
                                          						space.

Immediate Divert

Directed
                                          						call park supports Immediate Divert (iDivert or Divert softkey). For example,
                                          						user A calls user B, and user B parks the call. User B retrieves the call and
                                          						then decides to send the call to a voice-messaging mailbox by pressing the
                                          						iDivert or Divert softkey. User A receives the voicemail greeting of user B.

Barge

Barge with Directed Call Park–The target phone (the phone that is being barged upon) controls the call. The barge initiator "piggybacks" on the target phone. The target phone includes most of the common features, even when the target is being barged; therefore,
                                                the barge initiator has no feature access. When the target parks a call by using directed call park, the barge initiator then
                                                must release its call (the barge).

cBarge with Directed Call Park–The target and barge initiator act as peers. The cBarge feature uses a conference bridge that
                                                makes it behave like to a meet-me conference. Both phones (target and barge initiator) retain full access to their features.

Call
                                          						Park

We
                                          						recommend that you do not configure both directed call park and the Park
                                          						softkey for call park, but the possibility exists to configure both. If you
                                          						configure both, ensure that the call park and directed call park numbers do not
                                          						overlap.

A caller
                                          						who has been parked (the parkee) by using the directed call park feature
                                          						cannot, while parked, use the standard call park feature.

## Directed Call Park
                        	 Restrictions

Feature

Restriction

Directed Call Park number

Unified Communications Manager one party can park only one call at each Directed Call Park number.

You cannot delete a
                                          			 Directed Call Park number that a device is configured to monitor (using the BLF
                                          			 button). A message indicates that the Directed Call Park number or range cannot
                                          			 be deleted because it is in use. To determine which devices are using the
                                          			 number, click the Dependency Records link on the Directed Call Park
                                             			 Configuration window.

Standard Call Park Feature

A caller who has been
                                          			 parked (the parkee) by using the Directed Call Park feature cannot, while
                                          			 parked, use the standard call park feature.

Directed Call Park Feature

We recommend that you do not press both the Transfer and Directed Call Park buttons simultaneously, as this may result in
                                          both DPark and Transfer failures.

Directed Call Park BLF

The Directed Call Park BLF
                                          			 cannot monitor a range of Directed Call Park numbers. A user can monitor only
                                          			 individual Directed Call Park numbers by using the Directed Call Park BLF. For
                                          			 example, if you configure a Directed Call Park number range 8X, you cannot use
                                          			 the Directed Call Park BLF to monitor that whole range of 80 to 89.

Directed Call Park for phones that are running SIP

The following limitations apply to Directed Call Park for phones that are running SIP:

Directed Call Park gets invoked by using the Transfer softkey on Cisco Unified IP Phones 7940 and 7960 that are running SIP.

The system does not support directed call park when the Blind Transfer softkey is used on Cisco Unified IP Phones 7940 and
                                                7960 that are running SIP.

The system does not support directed call park BLF on Cisco Unified IP Phones 7940 and 7960 that are running SIP, and third-party
                                                phones that are running SIP.

## Troubleshooting Directed Call Park

### User Cannot
                           	 Retrieve Parked Calls

User
                                 		  cannot retrieve parked calls. After dialing the directed call park number to
                                 		  retrieve a parked call, the user receives a busy tone, and the IP phone
                                 		  displays the message, “Park Slot Unavailable”.

Ensure
                                 		  that the user dials the retrieval prefix followed by the directed call park
                                 		  number.

### User Cannot Park
                           	 Calls

User
                                 		  cannot park calls. After the Transfer softkey (or Transfer button if available)
                                 		  is pressed and the directed call park number is dialed, the call does not get
                                 		  parked.

Ensure that the
                                 		  partition that is assigned to the call park number matches the partition that
                                 		  is assigned to the phone directory number. Ensure that the partition and
                                 		  calling search space are configured correctly for the device. For more
                                 		  information about the partition, see the System
                                    			 Configuration Guide for Cisco Unified Communications Manager .

### User Receives a
                           	 Reorder Tone After the Reversion Timer Expires

User
                                 		  cannot park calls. The user receives a reorder tone after the reversion timer
                                 		  expires.

Ensure
                                 		  that the user presses the Transfer softkey (or Transfer button if available)
                                 		  before dialing the directed call park number, and then presses the Transfer
                                 		  softkey (or Transfer button) again or goes on hook after dialing the directed
                                 		  call park number. Because directed call park is a transfer function, the
                                 		  directed call park number cannot be dialed alone.

You can complete
                                             			 the transfer only by going on hook rather than pressing the Transfer softkey
                                             			 (or Transfer button) a second time if the Transfer On-hook Enabled service
                                             			 parameter is set to True.

### User Receives a
                           	 Reorder Tone or Announcement

User
                                 		  cannot park calls. After pressing the Transfer softkey (or Transfer button if
                                 		  available) and dialing the directed call park number, the user receives a
                                 		  reorder tone or announcement.

Ensure
                                 		  that the dialed number is configured as a directed call park number.

### User Cannot Park a
                           	 Call at a Number Within The Range

After
                                 		  configuring a range of directed call park numbers, the user cannot park a call
                                 		  at a number within the range.

Review
                                 		  the syntax for entering a range of directed call park numbers. If incorrect
                                 		  syntax is used, the system may appear to configure the range when it actually
                                 		  does not.

### Parked Calls
                           	 Revert Too Quickly

Parked calls revert too quickly.

Set the Call Park Reversion Timer to a longer duration.

### Park Slot
                           	 Unavailable

User
                                 		  cannot park calls. After pressing the Transfer softkey (or Transfer button if
                                 		  available) and dialing the directed call park number, the user receives a busy
                                 		  tone, and the IP phone displays the message, “Park Slot Unavailable".

Ensure
                                 		  that the dialed directed call park number is not already occupied by a parked
                                 		  call or park the call on a different directed call park number.

### Parked Calls Do
                           	 Not Revert to the Parked Call Number

Parked
                                 		  calls do not revert to the number that parked the call.

Check
                                 		  the configuration of the directed call park number to ensure that it is
                                 		  configured to revert to the number that parked the call rather than to a
                                 		  different directory number.

### Number or Range
                           	 Cannot Be Deleted Because It Is in Use

When an
                                 		  attempt is made to delete a directed call park number or range, a message
                                 		  displays that indicates that the number or range cannot be deleted because it
                                 		  is in use.

You
                                 		  cannot delete a directed call park number that a device is configured to
                                 		  monitor (by using the BLF button). To determine which devices are using the
                                 		  number, click the Dependency Records link in the Directed Call Park
                                 		  Configuration window.

| Phone
                                          					 Model | Supported
                                          					 in Softkey Template | Supported
                                          					 in Phone Button Template |
|---|---|---|
| Cisco Unified IP Phone s 6900 series (except 6901 and 6911) | X | X |
| Cisco IP Phone 7800 Series | X | X |
| Cisco Unified IP Phone s 7900 series (except 7921, 7925, 7936, 7937) | X |  |
| Cisco IP Phone 8800 Series | X | X |
| Cisco Unified IP Phone s 8900 series | X | X |
| Cisco Unified IP Phone s 9900 series | X | X |
| Cisco Unified IP Phone s 7900 series (except 7906, 7911, 7921, 7925, 7936, 7937) |  | X |

| Note | You can
                                          			 configure Call Park on any line (except line 1) or button by using the
                                          			 programmable line key feature. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Clusterwide Call Park | (Optional). Configure Call Park for the entire cluster, or use the procedure in step 3 to configure Call Park on servers within the cluster |
| Step 2 | Configure a Partition for Call Park | Create a
                                          				partition to add a Call Park Number |
| Step 3 | Configure a Call Park Number | Configure a
                                       			 Call Park Number to use Call Park across servers in a cluster. |
| Step 4 | Configure a Softkey Template for Call Park | Add the Park
                                          				softkey to a softkey template. |
| Step 5 | To Associate a Softkey Template with a Common Device Configuration ,
                                       			 complete the following subtasks: Add a Softkey Template to a Common Device Configuration Associate a Common Device Configuration with a Phone | Optional. To make the softkey template available to phones, you must complete either this step or the following step. Follow this step
                                          if your system uses a Common Device Configuration to apply configuration options to phones. This is the most commonly used method for making a softkey template available to
                                          phones. |
| Step 6 | Associate a Softkey with a Phone | Optional. Use this procedure either as an alternative to associating the softkey template with the Common Device Configuration, or
                                          in conjunction with the Common Device Configuration. Use this procedure in conjunction with the Common Device Configuration
                                          if you need assign a softkey template that overrides the assignment in the Common Device Configuration or any other default
                                          softkey assignment. |
| Step 7 | To Configure Call Park Button ,
                                       			 complete the following subtasks: Configure a Phone Button Template for Call Park Associate a Button Template with a Phone |  |
| Step 8 | Configure Park Monitoring | Complete this
                                          				optional task flow to add Park Monitoring to your Call Park configuration. |

| Step 1 | Choose System > Service
                                                				  Parameters . |
|---|---|
| Step 2 | Select the
                                          			 desired node as Server and the service as Cisco
                                             				CallManager (active). |
| Step 3 | Click the Advanced . The advanced service parameters are displayed in the window. |
| Step 4 | In Clusterwide Parameter(Feature- General) section set the Enable cluster-wide Call
                                             				  Park Number/Ranges to True . The default value is False. This parameter determines
                                             				  whether the Call Park feature is implemented clusterwide or restricted to a
                                             				  specific Unified CM node. |
| Step 5 | Set the Call Park Display Timer for each server in a
                                          				  cluster that has the Cisco CallManager service and Call Park configured. The
                                             				  default is 10 seconds. This parameter determines how long a Call Park number
                                             				  displays on the phone that parked the call. |
| Step 6 | Set the Call Park Reversion Timer for each server in a cluster that has the Unified Communications Manager service and Call Park configured. The default is 60 seconds. This parameter determines the time that a call remains parked. When this timer expires, the parked
                                             call returns to the device that parked the call. If a hunt group member parks a call that comes through a hunt pilot, the
                                             call goes back to the hunt pilot when the Call Park Reversion Timer expires. Note If you enter a Call Park Reversion Timer value that is less than the Call Park Display Timer, Call Park numbers may not display
                                                         on the phone. | Note | If you enter a Call Park Reversion Timer value that is less than the Call Park Display Timer, Call Park numbers may not display
                                                         on the phone. |
| Note | If you enter a Call Park Reversion Timer value that is less than the Call Park Display Timer, Call Park numbers may not display
                                                         on the phone. |
| Step 7 | Click Save . |
| Step 8 | Restart all Unified Communications Manager and CTI Manager services. |

| Note | If you enter a Call Park Reversion Timer value that is less than the Call Park Display Timer, Call Park numbers may not display
                                                         on the phone. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Partition . |
|---|---|
| Step 2 | Click Add
                                             				New to create a new partition. |
| Step 3 | In
                                          			 the Partition
                                             				Name, Description field, enter a name for the partition that is
                                          			 unique to the route plan. Partition
                                          			 names can contain alphanumeric characters, as well as spaces, hyphens (-), and
                                          			 underscore characters (_). See the online help for guidelines about partition
                                          			 names. |
| Step 4 | Enter a
                                          			 comma (,) after the partition name and enter a description of the partition on
                                          			 the same line. The
                                          			 description can contain up to 50 characters in any language, but it cannot
                                          			 include double quotes ("), percentage sign (%), ampersand (&), backslash
                                          			 (\), angle brackets (<>), or square brackets ([ ]). If you do
                                          			 not enter a description, Cisco Unified Communications Manager automatically
                                          			 enters the partition name in this field. |
| Step 5 | To create
                                          			 multiple partitions, use one line for each partition entry. |
| Step 6 | From the Time
                                             				Schedule drop-down list, choose a time schedule to associate with
                                          			 this partition. The time
                                          			 schedule specifies when the partition is available to receive incoming calls.
                                          			 If you choose None , the partition remains active at all times. |
| Step 7 | Select one
                                          			 of the following radio buttons to configure the Time
                                             				Zone : Originating
                                                				  Device —When you select this radio button, the system compares the
                                             				time zone of the calling device to the Time Schedule to determine whether the partition is
                                             				available is available to receive an incoming call. Specific Time
                                                				  Zone —After you select this radio button, choose a time zone from
                                             				the drop-down list. The system compares the chosen time zone to the Time Schedule to determine whether the partition is
                                             				available is available to receive an incoming call. |
| Step 8 | Click Save . |

| Step 1 | Choose Call
                                                				  Routing > Call Park . |
|---|---|
| Step 2 | Perform one of
                                          			 the following tasks: To add a
                                                   					 new Call Park number, click Add New . To copy a
                                                   					 Call Park number, find the Call Park number or range of numbers and then click
                                                   					 the Copy icon. To update
                                                   					 a Call Park number, find the Call Park number or range of numbers. The
                                          			 Call Park number configuration window displays. |
| Step 3 | Configure the fields in the Call Park configuration fields. See Call Park Configuration Fields for more information about the fields and their configuration options. |
| Step 4 | To save the
                                          			 new or changed Call Park numbers in the database, click Save. |

| Field | Description |
|---|---|
| Call Park Number/Range | Enter the Call Park extension number. You can enter digits or
                                                					 the wildcard character X (the system allows one or two Xs). For example, enter
                                                					 5555 to define a single Call Park extension number of 5555 or enter 55XX to
                                                					 define a range of Call Park extension numbers from 5500 to 5599. Note You can create a maximum of 100 Call Park numbers with one
                                                            						call park range definition. Make sure that the call park numbers are unique. Note You cannot overlap call park numbers between Unified Communications Manager servers. Ensure that each Unified Communications Manager server has its own number range. Note The call park range is selected from the list of servers
                                                            						where the call originates. For example, if phoneA (registered to nodeA) calls
                                                            						phone B (registered to nodeB) and the phoneB user presses Park, phoneB
                                                            						requires a call park range in the CSS that resides on nodeA. In a multinode
                                                            						environment where phones and gateways communicate with various nodes and where
                                                            						calls that originate from any server may need to be parked, the phones require
                                                            						a CSS that contains call park ranges from all servers. | Note | You can create a maximum of 100 Call Park numbers with one
                                                            						call park range definition. Make sure that the call park numbers are unique. | Note | You cannot overlap call park numbers between Unified Communications Manager servers. Ensure that each Unified Communications Manager server has its own number range. | Note | The call park range is selected from the list of servers
                                                            						where the call originates. For example, if phoneA (registered to nodeA) calls
                                                            						phone B (registered to nodeB) and the phoneB user presses Park, phoneB
                                                            						requires a call park range in the CSS that resides on nodeA. In a multinode
                                                            						environment where phones and gateways communicate with various nodes and where
                                                            						calls that originate from any server may need to be parked, the phones require
                                                            						a CSS that contains call park ranges from all servers. |
| Note | You can create a maximum of 100 Call Park numbers with one
                                                            						call park range definition. Make sure that the call park numbers are unique. |
| Note | You cannot overlap call park numbers between Unified Communications Manager servers. Ensure that each Unified Communications Manager server has its own number range. |
| Note | The call park range is selected from the list of servers
                                                            						where the call originates. For example, if phoneA (registered to nodeA) calls
                                                            						phone B (registered to nodeB) and the phoneB user presses Park, phoneB
                                                            						requires a call park range in the CSS that resides on nodeA. In a multinode
                                                            						environment where phones and gateways communicate with various nodes and where
                                                            						calls that originate from any server may need to be parked, the phones require
                                                            						a CSS that contains call park ranges from all servers. |
| Description | Provide a brief description of this call park number. The
                                                					 description can include up to 50 characters in any language, but it cannot
                                                					 include double-quotes (“), percentage sign (%), ampersand (&), or angle
                                                					 brackets (<>). |
| Partition | If you want to use a partition to restrict access to the call
                                                					 park numbers, choose the desired partition from the drop-down list. If you do
                                                					 not want to restrict access to the call park numbers, choose <None> for
                                                					 the partition. Note Make sure that the combination of call park extension number and partition is unique within the Unified Communications Manager . | Note | Make sure that the combination of call park extension number and partition is unique within the Unified Communications Manager . |
| Note | Make sure that the combination of call park extension number and partition is unique within the Unified Communications Manager . |
| Unified Communications Manager | Using the drop-down list, choose the Cisco Unified Communications Manager to which these call park numbers apply. |

| Note | You can create a maximum of 100 Call Park numbers with one
                                                            						call park range definition. Make sure that the call park numbers are unique. |
|---|---|

| Note | You cannot overlap call park numbers between Unified Communications Manager servers. Ensure that each Unified Communications Manager server has its own number range. |
|---|---|

| Note | The call park range is selected from the list of servers
                                                            						where the call originates. For example, if phoneA (registered to nodeA) calls
                                                            						phone B (registered to nodeB) and the phoneB user presses Park, phoneB
                                                            						requires a call park range in the CSS that resides on nodeA. In a multinode
                                                            						environment where phones and gateways communicate with various nodes and where
                                                            						calls that originate from any server may need to be parked, the phones require
                                                            						a CSS that contains call park ranges from all servers. |
|---|---|

| Note | Make sure that the combination of call park extension number and partition is unique within the Unified Communications Manager . |
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

| Step 1 | Add a Softkey Template to a Common Device Configuration |
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
| Step 5 | Press Reset to update the phone settings. |

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
| Step 1 | Configure Park Monitoring System Timers | Configure system-level timers for the Park Monitoring feature. |
| Step 2 | Configure Park Monitoring for Hunt Pilots | Optional. If you have hunt pilots deployed, assign a Park Monitoring destination to a hunt pilot. |
| Step 3 | Configure Park Monitoring for a Directory Number | Assign a Park Monitoring destination for an individual phone line. |
| Step 4 | Configure Park Monitoring via Universal Line Template | If you have an LDAP directory sync configured, you can use universal line templates  to provision directory number settings
                                             for multiple users with park monitoring configured. |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, select the publisher node. |
| Step 3 | From the Service drop-down list, select Cisco CallManager . |
| Step 4 | Configure values for the following service parameters: Park Monitoring Reversion Timer —The number of seconds that Cisco Unified Communications Manager waits before prompting the user to retrieve a parked call.
                                                      For individual phone lines, this setting can be overridden by the same setting in the Directory Number Configuration window. When the call park reversion timer expires, the call will be forwarded to the hunt pilot. Park Monitoring Periodic Reversion Timer —The number of seconds between reversion attempts when a call has been parked. Cisco Unified Communications Manager prompts
                                                      the user about the parked call by ringing, beeping, or flashing the parker's phone. When the park monitoring reversion timer
                                                      expires, the call will be forwarded to the parked party and not the hunt pilot. Park Monitoring Forward No Retrieve Timer —The number of seconds that park reminder notifications occur before the parked call is forwarded to the Park Monitoring Forward No Retrieve destination specified in the call parker's Directory Number configuration. When park monitoring forward no retrieve timer
                                                      expires, the call will be forwarded to the hunt pilot. Note For additional details on these fields, see the service parameter online help. | Note | For additional details on these fields, see the service parameter online help. |
| Note | For additional details on these fields, see the service parameter online help. |
| Step 5 | Click Save . |

| Note | For additional details on these fields, see the service parameter online help. |
|---|---|

| Note | For general information on setting up hunt pilots, see the "Configure Hunt Pilots" chapter of the System Configuration Guide for Cisco Unified Communications Manager . |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Hunt Pilot . |
|---|---|
| Step 2 | Click Find and select the hunt pilot on which you want to
                                             			 configure a Park Monitoring destination. |
| Step 3 | In the Park
                                                				Monitoring No Retrieve Destination field, assign a Destination directory number and Calling Search Space . |
| Step 4 | Complete any remaining fields in the Hunt Pilot Configuration window. For more information on the fields and their configuration options, see Online Help. |
| Step 5 | Click Save. |

| Note | The following
                                                			 tools are available to provision settings for multiple phone lines: Use a
                                                      				  universal line template to provision park monitoring settings for multiple
                                                      				  phone lines via an LDAP directory sync. For details, see Configure Park Monitoring via Universal Line Template . Use the Bulk Administration Tool to import a CSV file with settings for a large number of phone lines. For more information,
                                                      see the Bulk Administration Guide for Cisco Unified Communications Manager . |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Directory Number . |
|---|---|
| Step 2 | Click Find and select the directory number that you want
                                             			 to configure. |
| Step 3 | Enter values
                                             			 for the following Park
                                                				Monitoring fields: Park Monitoring Forward No Retrieve Destination
                                                         						External —When the Park Monitoring Forward No Retrieve Timer
                                                      					 expires, and the parkee is an external party, the call is forwarded either to
                                                      					 voicemail or to a specified directory number. If this field s empty, the call
                                                      					 is redirected to the call parker’s line. Park Monitoring Forward No Retrieve Destination
                                                         						Internal —When the Park Monitoring Forward No Retrieve Timer
                                                      					 expires, and the parkee is an internal party, the call is forwarded either to
                                                      					 voicemail or to a specified directory number. If this field s empty, the call
                                                      					 is redirected to the call parker’s line. Park Monitor Reversion Timer —The number of seconds
                                                      					 that Cisco Unified Communications Manager waits before prompting the user to
                                                      					 retrieve a call parked on this phone line. If the value is 0 or empty, then
                                                      					 Cisco Unified Communications Manager uses the value of the Park Monitor Reversion Timer service parameter. |
| Step 4 | Complete any remaining fields in the Directory Number Configuration window. For more information on the fields and their configuration options, see Online Help. |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose User Management > User Phone/Add > Universal Line Template . |
|---|---|
| Step 2 | Perform one of
                                             			 the following steps: Click Find and select an existing template. Click Add New to create a new template. |
| Step 3 | Expand the Park
                                                				Monitoring Settings section and complete the fields. For field
                                             			 descriptions, see Park Monitoring Settings for Universal Line Templates . |
| Step 4 | Click Save . |

| Field | Description |
|---|---|
| Forward Destination for External Calls When Not Retrieved | When the person whose call is parked is an external party and the Park Monitoring Forward No Retrieve Timer expires, the system sends the call to one of these destinations: Voicemail —Uses the configuration in Voice Mail Profile to determine where to send the call. Revert to Originator —Returns the call to the call parker. To forward calls to another number, input the other number in the text box. If no option is selected, the call returns to the call parker. |
| Calling Search Space for Forwarding External Calls When Not Retrieved | If you have configured parked calls to be redirected to a configured number, select the calling search space for the forward
                                                   destination. |
| Forward Destination for Internal Calls When Not Retrieved | When the person whose call is parked is an internal party and the Park Monitoring Forward No Retrieve Timer expires, the system sends the call to one of these destinations: Voicemail —Uses the configuration in Voice Mail Profile to determine where to send the call. Revert to Originator —Returns the call to the call parker. To forward calls to another number, input the other number in the text box. If no option is selected, the call returns to the call parker. |
| Calling Search Space for Forwarding Internal Calls When Not Retrieved | If you have configured parked calls to be redirected to a configured number, select the calling search space for the forward
                                                   destination. |
| Park Monitor Reversion Timer (seconds) | This timer determines the number of seconds
                                                   that Unified Communications Manager waits before prompting the user
                                                   to retrieve a call that the user parked. This timer starts when the
                                                   user presses the Park softkey on the phone, and a reminder is
                                                   issued when the timer expires. The default value is 60
                                                   seconds. Note If you select 0 for the timer then phone
                                                            lines that use this template will use the value of the Park
                                                               Monitor Reversion Timer cluster-wide service parameter. | Note | If you select 0 for the timer then phone
                                                            lines that use this template will use the value of the Park
                                                               Monitor Reversion Timer cluster-wide service parameter. |
| Note | If you select 0 for the timer then phone
                                                            lines that use this template will use the value of the Park
                                                               Monitor Reversion Timer cluster-wide service parameter. |

| Note | If you select 0 for the timer then phone
                                                            lines that use this template will use the value of the Park
                                                               Monitor Reversion Timer cluster-wide service parameter. |
|---|---|

| Feature | Interaction |
|---|---|
| CTI
                                          						Applications | CTI
                                          						applications access call park functionality, including monitoring activity on
                                          						call park DNs. To monitor a call park DN, add an application or end user that
                                          						is associated with the CTI application to the Standard CTI Allow Call Park
                                          						Monitoring user group. |
| Music On
                                          						Hold | Music On Hold allows users to place calls on hold with music that a streaming source provides. The Music On Hold audio source
                                          for Call Park is selected by the setting of the Network Hold MOH Audio Source setting within the Phone Configuration window. If you do not choose an audio source within the device configuration, Cisco Unified CM uses the audio source that
                                          is defined in the device pool or the system default if the device pool does not specify an audio source ID. |
| Route
                                          						Plan Report | The route plan report displays the patterns and directory numbers that are configured in Unified Communications Manager . Use the route plan report to look for overlapping patterns and directory numbers before assigning a directory number to
                                          Call Park. |
| Calling
                                          						Search Space and Partitions | Assign
                                          						the call park directory number or range to a partition to limit call park
                                          						access to users on the basis of the device calling search space. |
| Immediate Divert | Call
                                          						Park supports Immediate Divert (iDivert or Divert softkey). For example, user A
                                          						calls user B, and user B parks the call. User B retrieves the call and then
                                          						decides to send the call to a voice-messaging mailbox by pressing the iDivert
                                          						or Divert softkey. User A receives the voice mail greeting of user B. |
| Barge | Barge with Call Park–The target phone (the phone that is being barged upon) controls the call. The barge initiator "piggybacks" on the target phone. The target phone includes most of the common features, even when the target is being barged; therefore,
                                                the barge initiator has no feature access. When the target parks a call, the barge initiator then must release its call (the
                                                barge). cBarge with Call Park–The target and barge initiator act as peers. The cBarge feature uses a conference bridge, which causes
                                                it to function like a MeetMe conference. Both phones (target and barge initiator) have full access to their features. |
| Directed
                                          						Call Park | We
                                          						recommend that you do not configure both Directed Call Park and the Park
                                          						softkey for Call Park, but the possibility exists to configure both. If you
                                          						configure both, ensure that the call park and directed call park numbers do not
                                          						overlap. |
| QSIG
                                          						Intercluster Trunks | When a
                                          						user parks a call across a QSIG intercluster trunk or a QSIG gateway trunk, the
                                          						caller who has been parked (the parkee) does not see the To parked number
                                          						message. The phone continues to display the original connected number. The call
                                          						has been parked, and the user who parked the call can retrieve it. When the
                                          						call is retrieved from the parked state, the call continues, but the caller who
                                          						was parked does not see the newly connected number. |

| Feature | Restriction |
|---|---|
| Call Park | Unified Communications Manager can park only one call at each call park extension number. |
| Shared Line | For shared line devices across nodes, the line registers to
                                          						the node on which the device registers first. For example, if a device from
                                          						subscriber2 registers first and the line is created in subscriber2 and the
                                          						publisher node, the line belongs to subscriber2. Each node must be configured
                                          						with the call park number. |
| Backup | To achieve failover or fallback, configure call park numbers
                                          						on the publisher node and subscriber nodes. With this configuration, when the
                                          						primary node is down, the line device association gets changed to the secondary
                                          						node, and the secondary node call park number gets used. |
| Directed Call Park | If a directed call park (or call park) is initiated from a
                                          						shared line and the call is not retrieved from any device, the parked call does
                                          						not always get reverted to the recipient in the shared line (parker). |
| Conference | When a conference call is set up between both the shared line and the caller on park reversion or park reversion fails causing
                                          a two-party call (between the other shared line and caller). The reason is that, on park reversion, Unified Communications Manager extends the call to both devices sharing the line and tries to add either party in conference (party already in conference
                                          or party that hit the park). If the party attempts to add the party who is already in the conference first, then the park
                                          reversion fails. When park reversion fails, the shared line can still barge into the call as usual. |
| Delete
                                          						Server | If any call park numbers are configured for Unified Communications Manager on a node that is being deleted in the Server Configuration window ( System > Server ), the node deletion fails. Before you can delete the node, you must delete the call park numbers in Cisco Unified Communications Manager Administration . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure ClusterWide Directed Call Park | To configure
                                          				clusterwide parameter for directed call park. |
| Step 2 | Configure a Directed Call Park Number | To add, copy,
                                       			 and update a single Directed Call Park extension number or range of extension
                                       			 numbers. |
| Step 3 | Configure BLF/Directed Call Park Buttons | Configure a
                                          				phone button template for BLF/Directed Call Park. |
| Step 4 | Synchronize Directed Call Park with Affected Devices | Synchronize
                                       			 Directed Call Park with Affected Devices |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | To set the timer, update the Call Park Reversion
                                             				  Timer fields in the  Clusterwide Parameter(Feature- General) section. The default is 60 seconds. This parameter determines the time that a call
                                             				  remains parked. When this timer expires, the parked call returns to the device
                                             				  that parked the call or to  another specified number, depending on what you configure in the Directed Call Park Configuration window. |

| Step 1 | Choose Call
                                                				  Routing > Directed Call Park . |
|---|---|
| Step 2 | Perform one of
                                          			 the following tasks: To add a
                                                   					 new directed call park number, click Add New . To copy a
                                                   					 directed call park number, find the directed call park number or range of
                                                   					 numbers and then click the Copy icon. To update
                                                   					 a directed call park number, find the directed call park number or range of
                                                   					 numbers. The directed call park number configuration window is
                                             				displayed. |
| Step 3 | Configure the fields in the Directed Call Park settings area. See Directed Call Park Configuration Settings for more information about the fields and their configuration options. |
| Step 4 | To save the
                                          			 new or changed call park numbers in the database, click Save. If you update a directed call park number, Unified Communications Manager reverts any call that is parked on that number only after the Call Park Reversion Timer expires. |
| Step 5 | Click Apply
                                             				Config . The Apply
                                                				  Configuration Information dialog is displayed. |
| Step 6 | Click OK. |
| Step 7 | If you are using BLF to monitor directed Call Park numbers, click Restart Devices on the Directed Call Park Configuration window. This step is optional if you are using change notification. |

| Field | Description |
|---|---|
| Number | Enter
                                                						the directed call park number. You can enter digits (0-9) or the wildcard
                                                						character ([], - , *, ^, #) and X (the system allows one or two Xs). For
                                                						example, enter 5555 to define a single call park number of 5555 or enter 55XX
                                                						to define a range of directed call park extension numbers from 5500 to 5599.
                                                						Make sure that the directed call park numbers are unique and that they do not
                                                						overlap with call park numbers. |
| Description | Provide
                                                						a brief description of this directed call park number or range. The description
                                                						can include up to 50 characters in any language, but it cannot include double
                                                						quotation marks (“), percentage sign (%), ampersand (&), or angle brackets
                                                						(<>) and tabs. |
| Partition | If you
                                                						want to use a partition to restrict access to the directed call park numbers,
                                                						choose the desired partition from the drop-down list. If you do not want to
                                                						restrict access to the directed call park numbers, leave the partition as the
                                                						default of <None>. Note Make sure that the combination of directed call park number and partition is unique within Unified Communications Manager . | Note | Make sure that the combination of directed call park number and partition is unique within Unified Communications Manager . |
| Note | Make sure that the combination of directed call park number and partition is unique within Unified Communications Manager . |
| Reversion Number | Enter
                                                						the number to which you want the parked call to return if not retrieved, or
                                                						leave the field blank. Note A
                                                            						  reversion number can comprise digits only; you cannot use wildcards. | Note | A
                                                            						  reversion number can comprise digits only; you cannot use wildcards. |
| Note | A
                                                            						  reversion number can comprise digits only; you cannot use wildcards. |
| Reversion Calling Search Space | Using
                                                						the drop-down list, choose the calling search space or leave the calling search
                                                						space as the default of <None>. |
| Retrieval Prefix | For this
                                                						required field, enter the prefix for retrieving a parked call. The system needs
                                                						the retrieval prefix to distinguish between an attempt to retrieve a parked
                                                						call and an attempt to initiate a directed park. |

| Note | Make sure that the combination of directed call park number and partition is unique within Unified Communications Manager . |
|---|---|

| Note | A
                                                            						  reversion number can comprise digits only; you cannot use wildcards. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Phone Button Template . |
|---|---|
| Step 2 | After the
                                          			 configuration window displays, click the Add a
                                             				new BLF Directed Call Park link in the Association Information
                                          			 pane. Note The link does not display in the Association Information pane if the phone button template that you applied to the phone or
                                                         device profile does not support BLF/Directed Call Park. | Note | The link does not display in the Association Information pane if the phone button template that you applied to the phone or
                                                         device profile does not support BLF/Directed Call Park. |
| Note | The link does not display in the Association Information pane if the phone button template that you applied to the phone or
                                                         device profile does not support BLF/Directed Call Park. |
| Step 3 | Configure the fields in the BLF/Directed Call Park fields area. See BLF/Directed Call Park Configuration Fields for more information about the fields and their configuration options. |
| Step 4 | After you
                                          			 complete the configuration, click Save and close the window. The directory
                                             				numbers are displayed in the Association Information pane of the Phone
                                             				Configuration Window. |

| Note | The link does not display in the Association Information pane if the phone button template that you applied to the phone or
                                                         device profile does not support BLF/Directed Call Park. |
|---|---|

| Field | Description |
|---|---|
| Directory
                                                					 Number | The Directory Number drop-down list displays a list of Directed Call Park number that exist in the Unified Communications Manager database. For phones
                                                					 that are running SCCP or phones that are running SIP, choose the number (and
                                                					 corresponding partition, if it is displayed) that you want the system to dial
                                                					 when the user presses the speed-dial button; for example, 6002 in 3. Directory
                                                					 numbers that display without specific partitions belong to the default
                                                					 partition. |
| Label | Enter the
                                                					 text that you want to display for the BLF/Directed Call Park button. This field
                                                					 supports internationalization. If your phone does not support
                                                					 internationalization, the system uses the text that displays in the Label ASCII
                                                					 field. |
| Label
                                                					 ASCII | Enter the
                                                					 text that you want to display for the BLF/Directed Call Park button. The ASCII
                                                					 label represents the noninternationalized version of the text that you enter in
                                                					 the Label field. If the phone does not support internationalization, the system
                                                					 uses the text that displays in this field. Note If you enter text in the Label ASCII field that differs from the text in the Label field, Cisco Unified Communications Manager Administration accepts the configuration for both fields, even though the text differs. | Note | If you enter text in the Label ASCII field that differs from the text in the Label field, Cisco Unified Communications Manager Administration accepts the configuration for both fields, even though the text differs. |
| Note | If you enter text in the Label ASCII field that differs from the text in the Label field, Cisco Unified Communications Manager Administration accepts the configuration for both fields, even though the text differs. |

| Note | If you enter text in the Label ASCII field that differs from the text in the Label field, Cisco Unified Communications Manager Administration accepts the configuration for both fields, even though the text differs. |
|---|---|

| Step 1 | Choose Call
                                                				  Routing > Directed Call Park . The Find
                                                				  and List Directed Call Parks window is displayed. |
|---|---|
| Step 2 | Choose the
                                          			 search criteria to use. |
| Step 3 | Click Find. The window
                                             				displays a list of directed call parks that match the search criteria. |
| Step 4 | Click the
                                          			 directed call park to which you want to synchronize applicable devices.
                                          			 The Directed Call
                                             				Park Configuration window is displayed. |
| Step 5 | Make any
                                          			 additional configuration changes. |
| Step 6 | Click Save. |
| Step 7 | Click Apply
                                             				Config . The Apply
                                                				  Configuration Information dialog is displayed. |
| Step 8 | Click OK. |

| Feature | Interaction |
|---|---|
| Music On
                                          						Hold | The Music On Hold Audio Source for directed call park is assigned via the Default Network Hold MOH Audio Source service parameter. To assign the parameter: From Cisco Unified CM Administration, choose System > Service Parameters . From the Server drop-down list, choose a Unified Communications Manger cluster node. From the Service drop-down list, select Cisco CallManager . Under Clusterwide Paramters (Service) , assign a MOH audio source to the Default Network Hold MOH Audio Source ID parameter. The default is 1 . Click Save . Note For detailed information on adding MOH audio sources to the system, refer to the "Configure Music On Hold" section of this
                                                   guide. | Note | For detailed information on adding MOH audio sources to the system, refer to the "Configure Music On Hold" section of this
                                                   guide. |
| Note | For detailed information on adding MOH audio sources to the system, refer to the "Configure Music On Hold" section of this
                                                   guide. |
| Calling
                                          						Search Space and Partitions | Assign
                                          						the Directed Call Park Directory number or range to a partition to limit
                                          						Directed Call Park access to users on the basis of the device calling search
                                          						space. |
| Immediate Divert | Directed
                                          						call park supports Immediate Divert (iDivert or Divert softkey). For example,
                                          						user A calls user B, and user B parks the call. User B retrieves the call and
                                          						then decides to send the call to a voice-messaging mailbox by pressing the
                                          						iDivert or Divert softkey. User A receives the voicemail greeting of user B. |
| Barge | Barge with Directed Call Park–The target phone (the phone that is being barged upon) controls the call. The barge initiator "piggybacks" on the target phone. The target phone includes most of the common features, even when the target is being barged; therefore,
                                                the barge initiator has no feature access. When the target parks a call by using directed call park, the barge initiator then
                                                must release its call (the barge). cBarge with Directed Call Park–The target and barge initiator act as peers. The cBarge feature uses a conference bridge that
                                                makes it behave like to a meet-me conference. Both phones (target and barge initiator) retain full access to their features. |
| Call
                                          						Park | We
                                          						recommend that you do not configure both directed call park and the Park
                                          						softkey for call park, but the possibility exists to configure both. If you
                                          						configure both, ensure that the call park and directed call park numbers do not
                                          						overlap. A caller
                                          						who has been parked (the parkee) by using the directed call park feature
                                          						cannot, while parked, use the standard call park feature. |

| Note | For detailed information on adding MOH audio sources to the system, refer to the "Configure Music On Hold" section of this
                                                   guide. |
|---|---|

| Feature | Restriction |
|---|---|
| Directed Call Park number | Unified Communications Manager one party can park only one call at each Directed Call Park number. You cannot delete a
                                          			 Directed Call Park number that a device is configured to monitor (using the BLF
                                          			 button). A message indicates that the Directed Call Park number or range cannot
                                          			 be deleted because it is in use. To determine which devices are using the
                                          			 number, click the Dependency Records link on the Directed Call Park
                                             			 Configuration window. |
| Standard Call Park Feature | A caller who has been
                                          			 parked (the parkee) by using the Directed Call Park feature cannot, while
                                          			 parked, use the standard call park feature. |
| Directed Call Park Feature | We recommend that you do not press both the Transfer and Directed Call Park buttons simultaneously, as this may result in
                                          both DPark and Transfer failures. |
| Directed Call Park BLF | The Directed Call Park BLF
                                          			 cannot monitor a range of Directed Call Park numbers. A user can monitor only
                                          			 individual Directed Call Park numbers by using the Directed Call Park BLF. For
                                          			 example, if you configure a Directed Call Park number range 8X, you cannot use
                                          			 the Directed Call Park BLF to monitor that whole range of 80 to 89. |
| Directed Call Park for phones that are running SIP | The following limitations apply to Directed Call Park for phones that are running SIP: Directed Call Park gets invoked by using the Transfer softkey on Cisco Unified IP Phones 7940 and 7960 that are running SIP. The system does not support directed call park when the Blind Transfer softkey is used on Cisco Unified IP Phones 7940 and
                                                7960 that are running SIP. The system does not support directed call park BLF on Cisco Unified IP Phones 7940 and 7960 that are running SIP, and third-party
                                                phones that are running SIP. |

| Note | You can complete
                                             			 the transfer only by going on hook rather than pressing the Transfer softkey
                                             			 (or Transfer button) a second time if the Transfer On-hook Enabled service
                                             			 parameter is set to True. |
|---|---|