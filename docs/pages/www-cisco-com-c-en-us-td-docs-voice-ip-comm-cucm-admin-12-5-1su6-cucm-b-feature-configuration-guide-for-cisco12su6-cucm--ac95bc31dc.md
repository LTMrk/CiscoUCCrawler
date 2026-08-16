---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su6-cucm-b-feature-configuration-guide-for-cisco12su6-cucm--ac95bc31dc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU6/cucm_b_feature-configuration-guide-for-cisco12su6/cucm_b_feature-configuration-guide-for-cisco1251su3_chapter_0100111.html
retrieved_at: 2026-08-16T16:37:49.905010+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: October 8, 2025

Chapter: BLF Presence

## Chapter: BLF Presence

# BLF Presence

## BLF Presence
                        	 Overview

The Busy Lamp Field (BLF) presence feature allows a user who is a watcher to monitor the real-time
                           		status of another user at a directory number or Session Initiation Protocol
                           		(SIP) uniform resource identifier (URI) from the device of the watcher.

- BLF and SpeedDial buttons

- Missed call, placed call,
                                 		  or received call lists in the directories window

- Shared directories, such as
                                 		  the corporate directory

Call lists
                           		and directories display the BLF status for existing entries. When you configure
                           		BLF and SpeedDial buttons, the BLF presence entity appears as a speed dial on the
                           		device of the watcher.

To view
                           		the status of a BLF presence entity, watchers send BLF presence requests to Cisco Unified
                              		  Communications Manager . After administrators configure BLF presence
                           		features, real-time status icons appear on the watcher device to indicate
                           		whether the BLF presence entity is on the phone, is not on the phone, the status
                           		is unknown, and so on.

Extension
                           		mobility users can use BLF presence features on phones with extension mobility
                           		support.

BLF
                           		presence group authorization ensures that only authorized watchers can access
                           		the BLF presence status for a destination. Because the administrator ensures
                           		that the watcher is authorized to monitor the destination when a BLF or Speed Dial
                           		is configured, BLF presence group authorization does not apply to BLF or Speed
                           		Dials.

## BLF Presence
                        	 Prerequisites

- Configure the phones that
                                 			 you want to use with the BLF presence feature.

- Configure the SIP trunks
                                 			 that you want to use with the BLF presence feature.

## BLF Presence
                        	 Configuration Task Flow

### Before you begin

Review BLF Presence Prerequisites

Step 1

Configure and
                                       			 synchronize cluster-wide enterprise parameters for Busy Lamp Field (BLF). See Configure/Synchronize Cluster-Wide Enterprise Parameters for BLF .

Step 2

Configure
                                       			 cluster-wide service parameters for BLF. See Configure Cluster-Wide Service Parameters for BLF .

Step 3

Configure BLF
                                       			 presence groups. See Configure BLF Presence Groups .

Step 4

To associate
                                       			 BLF presence group with devices and users, perform the following subtasks:

- Associate BLF presence
                                          				groups with phones. See Associate BLF Presence Groups with Phone .

- Associate BLF presence
                                          				groups with SIP trunks. See Associate BLF Presence Groups with SIP Trunk .

- Associate BLF presence
                                          				groups with an end user. See Associate BLF Presence Groups with End User .

- Associate BLF presence
                                          				groups with an application user. See Associate BLF Presence Groups with Application User .

Step 5

Accept BLF
                                       			 presence requests from external trunks and applications. See Accept BLF Presence Requests from External Trunks and Applications .

Step 6

Configure
                                       			 Calling Search Space. See Configure a Calling Search Space for Presence Requests .

Step 7

Configure a
                                       			 phone button template for BLF and SpeedDial buttons. See Configure a Phone Button Template for BLF and SpeedDial Buttons .

Step 8

Associate
                                       			 button template with a device. See Associate Button Template with a Device .

Step 9

Configure user
                                       			 device profile. See Configure User Device Profile .

### Configure/Synchronize Cluster-Wide Enterprise Parameters for
                           	 BLF

Use enterprise parameters for  default configuration that apply to all devices and services in the same cluster. A cluster
                                 consists of a set of Cisco Unified Communications Managers that share the same database. When you install a new Cisco Unified
                                 Communications Manager, it uses the enterprise parameters to set the initial values of its device defaults.

Step 1

From Cisco Unified CM Administration, choose System > Enterprise Parameters .

Step 2

Configure the fields in the Enterprise Parameters Configuration window. For more information on the fields and their configuration options, see Online Help.

Tip

For details about an enterprise parameter, click the parameter name or the question mark that appears in the Enterprise Parameter Configuration window.

Step 3

Click Save .

Step 4

(Optional) Click Apply Config to synchronize cluster-wide parameters.

Step 5

Click OK .

### Configure
                           	 Cluster-Wide Service Parameters for BLF

You can configure one or multiple services available in the Service Parameter Configuration window for BLF.

#### Before you begin

Configure/Synchronize Cluster-Wide Enterprise Parameters for BLF

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, choose the server where you
                                          			 want to configure the parameter.

Step 3

Configure the fields in the Service Parameters Configuration window. For more information on the fields and their configuration options, see Online Help.

Tip

For details about the service parameters, click the parameter name or the question mark that appears in the Service Parameter Configuration window.

Step 4

Click Save .

### Configure BLF
                           	 Presence Groups

You can use BLF presence groups to control the destinations that watchers can monitor. To configure a BLF presence group,
                                 create the group in Cisco Unified Communications Manager Administration and assign one or more destinations and watchers to the same group.

When you add a new BLF presence group, Unified Communications Manager defines all group relationships for the new group with the default cluster field as the initial permission fields. To apply
                                 different permissions, configure new permissions between the new group and existing groups for each permission that you want
                                 to change.

The system
                                             			 always allows BLF presence requests within the same BLF presence group.

To view the status of a presence entity, watchers send presence requests to Unified Communications Manager . The system requires watchers to be authorized to initiate status requests for a presence entity with these requirements:

The watcher
                                       				BLF presence group be authorized to obtain the status for the presence entity
                                       				presence group, whether inside or outside of the cluster.

Unified CM must be authorized to accept BLF presence requests from an external presence server or application.

#### Before you begin

Configure Cluster-Wide Service Parameters for BLF

Step 1

From Cisco Unified CM Administration, choose System > BLF Presence Group .

Step 2

Configure the fields in the BLF Presence Group Configuration window. See BLF Presence Group Fields for BLF for details about the fields and their configuration options.

Use the Default Inter-Presence Group Subscription service parameter for the Cisco CallManager service. It sets the clusterwide permissions parameter for BLF presence groups
                                                         to allow subscription or disallow subscription. This field enables administrators to set a system default and configure BLF
                                                         presence group relationships by using the default field for the cluster.

Step 3

Click Save .

The permissions that you configure for a BLF presence group
                                                         				  appear in the BLF Presence Group Relationship pane. Permissions
                                                         				  that use the system default permission field for the group-to-group
                                                         				  relationship do not appear.

#### What to do next

Associate BLF
                                 		  presence group with devices and users by performing the following subtasks:

#### BLF Presence Group
                              	 Fields for BLF

Presence
                                    		  authorization works with BLF presence groups. The following table describes the
                                    		  BLF presence group configuration fields.

Field

Description

Name

Enter
                                                						the name of the BLF presence group that you want to configure. For example,
                                                						Executive_Group.

Description

Enter a
                                                						description for the BLF presence group that you are configuring.

Modify
                                                						Relationship to Other Presence Groups

Select
                                                						one or more BLF presence groups to configure the permission fields for the
                                                						named group to the selected groups.

Subscription Permission

For the
                                                						selected BLF presence groups, choose one of the following options from the
                                                						drop-down list:

- Use System
                                                      							 Default —Set the permissions field to the Default Inter-Presence
                                                   						  Group Subscription clusterwide service parameter field (Allow Subscription or
                                                   						  Disallow Subscription).

- Allow
                                                      							 Subscription —Allow members in the named group to view the
                                                   						  real-time status of members in the selected groups.

- Disallow
                                                      							 Subscription —Block members in the named group from viewing the
                                                   						  real-time status of members in the selected groups.

The
                                                						permissions that you configure appear in the BLF Presence Group relationship
                                                						pane when you click Save . All groups that use system default permission
                                                						field do not appear.

### BLF Presence Group
                           	 Association with Devices and Users

Perform
                                 		  the following procedures to apply a BLF presence group to the phone, SIP trunk,
                                 		  phone that is running SIP, phone that is running SCCP, directory number,
                                 		  application user (for application users that are sending presence requests over
                                 		  the SIP trunk), and end user.

The
                                             			 system allows presence requests between members in the same BLF presence group.

#### Associate BLF
                              	 Presence Groups with Phone

You can use BLF presence for phones and trunks when the phones and trunks have permission to send and receive presence requests.

Cisco Unified Communications Manager handles the  BLF presence requests for Cisco Unified Communications Manager users, whether
                                    inside or outside the cluster. For a Cisco Unified Communications Manager watcher that sends a BLF presence request through
                                    the phone, Cisco Unified Communications Manager responds with the BLF presence status if the phone and BLF presence entity
                                    are colocated

##### Before you begin

Configure BLF Presence Groups

Step 1

In the Cisco Unified CM Administration, choose Device > Phone ,
                                             			 and click Add New .

Step 2

From the Phone Type drop-down list, select the type of
                                             			 phone that you want to associate BLF presence group to.

Step 3

Click Next .

Step 4

Configure the fields in the Phone Configuration window. See the online help
                                             			 for information about the fields and their configuration options.

From the SUBSCRIBE Calling Search Space drop-down
                                                            				  list, select a SUBSCRIBE calling search space to use for presence requests for
                                                            				  the phone. All calling search spaces that you configure in Cisco Unified
                                                            				  Communications Manager Administration appear in the SUBSCRIBE Calling Search Space drop-down
                                                            				  list. If you do not select a different calling search space for the end user
                                                            				  from the drop-down list, the value of this field applies the default value as None . To configure a SUBSCRIBE calling
                                                            				  search space specifically for this purpose, configure a calling search space as
                                                            				  you configure all calling search spaces.

Step 5

Click Save .

##### What to do next

Associate BLF presence group with devices and users by performing the following subtasks:

Associate BLF Presence Groups with SIP Trunk

Associate BLF Presence Groups with End User

Associate BLF Presence Groups with Application User

#### Associate BLF
                              	 Presence Groups with SIP Trunk

If digest authentication is not configured for the SIP trunk, you can configure the trunk to accept incoming subscriptions,
                                    but application-level authorization cannot be initiated, and Unified CM accepts all incoming requests before performing group
                                    authorization. When digest authentication is used with application-level authorization, Unified CM also authenticates the
                                    credentials of the application that is sending the BLF presence requests.

When there is a BLF presence request for a device that exists outside of the cluster, Unified Communications Manager queries the external device through the SIP trunk. If the watcher has permission to monitor the external device, the SIP
                                    trunk sends the BLF presence request to the external device, and returns BLF presence status to the watcher.

Tip

To use BLF presence group authorization with incoming presence
                                                			 requests on a SIP trunk, configure a presence group for the trunk, such as
                                                			 External_Presence_Serv_Group1, and configure the appropriate permissions to
                                                			 other groups inside the cluster.

If you configure both levels of authorization for SIP trunk
                                    		  presence requests, the BLF presence group for the SIP trunk gets used only when
                                    		  no BLF presence group is identified in the incoming request for the
                                    		  application.

##### Before you begin

Configure BLF Presence Groups

Step 1

From Cisco Unified CM Administration, choose Device > Trunk , and click Add New .

Step 2

From the Trunk
                                                				Type drop-down list, select the type of phone that you want to associate
                                             			 BLF presence group.

Step 3

Click Next .

Step 4

Configure the
                                             			 fields in the Trunk
                                                				Configuration window. See the online help for information about the
                                             			 fields and their configuration options.

To authorize the Unified CM system to accept incoming BLF presence requests from the SIP trunk, check the Accept Presence Subscription check box in the SIP Trunk Security Profile Configuration window. To block incoming presence requests on a SIP trunk, uncheck
                                                            the check box. When you allow SIP trunk BLF presence requests, Unified CM accepts requests from the SIP user agent (SIP proxy
                                                            server or external BLF presence server) that connects to the trunk. Consider digest authentication as optional when Unified
                                                            CM is configured to accept BLF presence requests from a SIP trunk.

Step 5

Click Save .

##### What to do next

Associate BLF presence group with devices and users by performing the following subtasks:

Associate BLF Presence Groups with Phone

Associate BLF Presence Groups with End User

Associate BLF Presence Groups with Application User

#### Associate BLF
                              	 Presence Groups with End User

An administrator associates BLF presence groups with end user for user directories and call lists and to configure extension
                                    mobility settings.

##### Before you begin

Configure BLF Presence Groups

Step 1

In the Cisco Unified CM Administration, choose User Management > End
                                                   				  User , and click Add New .

Step 2

Configure the fields in the End User Configuration window. See the online
                                             			 help for information about the fields and their configuration options.

Step 3

Click Save .

##### What to do next

Associate BLF presence group with devices and users by performing the following subtasks:

Associate BLF Presence Groups with Phone

Associate BLF Presence Groups with SIP Trunk

Associate BLF Presence Groups with Application User

#### Associate BLF
                              	 Presence Groups with Application User

An administrator associates BLF Presence groups with an application user  for external applications. These external applications
                                    send BLF presence requests that is SIP trunk or home on a proxy server which is connected on SIP trunk. For example, Web Dial,
                                    Meeting Place, conference servers, and presence servers.

##### Before you begin

Configure BLF Presence Groups

Step 1

In the Cisco Unified CM Administration, choose User
                                                   				  Management > Application User ,
                                             			 and click Add New .

Step 2

Configure the fields in the Application User Configuration window. See the
                                             			 online help for information about the fields and their configuration options.

Step 3

Click Save .

##### What to do next

Associate BLF presence group with devices and users by performing the following subtasks:

Associate BLF Presence Groups with Phone

Associate BLF Presence Groups with SIP Trunk

Associate BLF Presence Groups with End User

### Accept BLF
                           	 Presence Requests from External Trunks and Applications

To allow BLF presence requests from outside the cluster, configure the system to accept BLF presence requests from the external
                                 trunk or application. You can assign BLF presence groups to trunks and applications outside the cluster to invoke BLF presence
                                 group authorization.

Step 1

From Cisco Unified CM Administration, choose Device > Trunk , and click Add New .

Step 2

To allow BLF presence requests from a SIP trunk, check the Accept Presence Subscription check box in the SIP Trunk Security Profile Configuration window.

Step 3

To enable application-level authorization for a SIP trunk
                                          			 application in addition to trunk-level authorization, check the following check
                                          			 boxes in the SIP Trunk Security Profile Configuration window:

Enable Digest Authentication

Enable Application Level Authorization

You cannot check Enable Application Level Authorization unless Enable Digest Authentication is checked.

Step 4

Apply the profile to the trunk. Click Reset so that the changes to the trunk can
                                          			 take effect.

If you checked Enable Application Level Authorization ,
                                                         				  check the Accept Presence Subscription check box in
                                                         				  the Application User Configuration window for
                                                         				  the application.

### Configure a Calling
                           	 Search Space for Presence Requests

The
                                 		  SUBSCRIBE Calling Search space option allows you to apply a calling search
                                 		  space separate from the call-processing Calling Search Space for BLF presence
                                 		  requests. Select a different calling search space for presence requests, else
                                 		  the SUBSCRIBE Calling Search Space selects the None default option. The SUBSCRIBE Calling Search
                                 		  Space that is associated with an end user is used for extension mobility
                                 		  calls.

You
                                 		  apply the SUBSCRIBE Calling Search Space to the SIP trunk, phone, or end user.
                                 		  The SUBSCRIBE Calling Search Space that is associated with an end user is used
                                 		  for extension mobility calls.

#### Before you begin

Accept BLF Presence Requests from External Trunks and Applications

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Calling Search Space .

Step 2

In the Calling Search Space configuration window,
                                          			 choose the calling search space from the SUBSCRIBE Calling Search Space drop-down list.

Step 3

Click Add
                                             				New .

Step 4

In the Name field, enter a name.

Step 5

(Optional) In the Description field, enter a description to identify the calling search space.

Step 6

From the Available Partitions list, select one or
                                          			 multiple partitions, and click the arrow keys.

Step 7

(Optional) To add or remove a partition from the Selected Partitions list, click the arrow keys next to the list box.

Step 8

Click Save .

All calling search spaces that you configure in Cisco Unified Communications Manager Administration appear in the SUBSCRIBE Calling Search Space drop-down list in the Trunk Configuration or Phone Configuration window.

### Configure a Phone
                           	 Button Template for BLF and SpeedDial Buttons

You can
                                 		  configure BLF and SpeedDial buttons for a phone or user device profile. After you
                                 		  apply the template to the phone or device profile (and save the phone or device
                                 		  profile configuration), the Add a new BLF SD link appears in the Association Information pane in Cisco Unified
                                 		  Communications Administration.

If the template
                                             			 does not support BLF and SpeedDials, the Add a new BLF SD link appears in the Unassigned Associated Items pane.

When an administrator decides to add or change a BLF and SpeedDial button
                                 		  for a SIP URI, the administrator ensures that the watcher is authorized to
                                 		  monitor that destination. If the system uses a SIP trunk to reach a SIP URI BLF
                                 		  target, the BLF presence group associated with the SIP trunk applies.

#### Before you begin

Configure a Calling Search Space for Presence Requests

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Phone Button Template .

Step 2

Click the Add
                                             				New button.

Step 3

In the Button
                                             				Template Name field, enter a name for the template.

Step 4

From the Phone
                                             				Button Template drop-down list, select a template of phone button.

Step 5

Click Copy to create a new button template based on the
                                          			 layout of the selected button template.

Step 6

Click Save .

### Associate Button
                           	 Template with a Device

You configure BLF and SpeedDial buttons for a phone or user device profile. The BLF value does not have to be on the cluster.
                                 For information on the Busy Lamp Field (BLF) status icons that display on the phone, see the Cisco Unified IP Phone documentation that supports your phone. To identify whether your phone supports BLF presence, see the Cisco Unified IP Phone documentation that supports your phone and this version of Unified Communications Manager .

#### Before you begin

Configure a Phone Button Template for BLF and SpeedDial Buttons

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Device Profile .

Step 2

Enter the search parameters to find the configured phone button
                                          			 templates, and click Find .

Step 3

Click one of the records.

Step 4

From the Phone Button Template list, select a
                                          			 configured phone button template.

Step 5

(Optional) Modify the values of the configured device.

Step 6

Click Save .

### Configure User
                           	 Device Profile

See the "BLF Presence
                                    			 with Extension Mobility" section of BLF Presence Interactions for details.

#### Before you begin

Associate Button Template with a Device

Step 1

In the Cisco
                                          			 Unified CM Administration, choose Device > Device
                                                				  Settings > Device Profile .

Step 2

Click Add
                                             				New .

Step 3

Configure the
                                          			 fields in Device
                                             				Profile Configuration window. See the online help for information
                                          			 about the fields and their configuration options.

If the
                                                         				  phone button template that you applied to the phone or device profile does not
                                                         				  support BLF and SpeedDials, the link does not appear in the Association Information pane, but appears in the Unassigned Associated Items pane.

Step 4

Click Save .

## BLF Presence
                        	 Interactions

Presence
                                          						BLF with DNs on H.323 phones when the H.323 phone device serves as presence entity

When the
                                          						H.323 phone is in the RING IN state, the BLF status gets reported as Busy. For
                                          						the presence entities of phones that are running either SCCP or SIP and that are
                                          						in the RING IN state, the BLF status gets reported as Idle.

Presence
                                          						BLF with DNs on H.323 phones when the H.323 phone device serves as presence entity

When the
                                          						H.323 phone is not connected to Cisco Unified
                                             						  Communications Manager for any reason, such as the Ethernet cable is
                                          						unplugged from the phone, the BLF status gets reported as Idle all the time.
                                          						For presence entities of phones that are running either SCCP or SIP and that are not
                                          						connected to Cisco Unified
                                             						  Communications Manager , the BLF status gets reported as Unknown.

BLF Presence with Extension Mobility

When you configure BLF and SpeedDial buttons in a user
                                          						device profile in Cisco Unified
                                             						  Communications Manager Administration , a phone that supports Cisco
                                             						  Extension Mobility displays BLF presence status on the BLF and SpeedDial
                                          						buttons after you log in to the device.

When the extension mobility user logs out, a phone
                                          						that supports Cisco
                                             						  Extension Mobility displays BLF presence status on the BLF and SpeedDial
                                          						buttons for the logout profile that is configured.

## BLF Presence
                        	 Restrictions

Restriction

Description

SIP Presence

Cisco Unified Communications Manager Assistant does not support SIP presence.

BLF
                                          				Presence Requests

Cisco Unified Communications Manager Administration rejects BLF presence requests to a directory number that is associated with a hunt pilot.

BLF on
                                          				Call List Feature

The BLF on
                                          				call list feature is not supported on the Cisco Unified IP Phone 7940 and Cisco
                                          				Unified IP Phone 7960.

BLF and SpeedDials

The administrator ensures that the watcher is authorized to monitor the destination when configuring a BLF and SpeedDial.
                                          BLF presence group authorization does not apply to BLF and SpeedDials.

BLF presence group authorization does not apply to any directory number or SIP URI that is configured as a BLF and Speed Dial
                                                      that appears in a call list for phones that are running SIP.

If there is an overlapping DN, where there is the same extension in different partitions, the presence notifications are selected
                                          based on the order of the partitions configured within the SUBSCRIBE CSS assigned to the device.

For example, two BLF speed dials are configured on a phone.

Extension 1234 in the "internal" partition

Extension 1234 in the "external" partition

Whichever partition is listed first within the SUBSCRIBE CSS is the one that will provide BLF presence to the subscribed devices.

BLF Presence
                                          				Authorization

For Cisco Unified IP Phone s with multiple lines, the phone uses the cached information that is associated with the line directory number for missed
                                          and placed calls to determine BLF presence authorization. If this call information is not present, the phone uses the primary
                                          line as the subscriber for BLF presence authorization. For BLF and SpeedDial buttons on Cisco Unified IP Phone s with multiple lines, the phone uses the first available line as the subscriber.

Cisco Unified IP
                                          				  Phone

When a user monitors a directory number that is configured for Cisco Unified IP Phone s 7960 and 7940 that are running SIP, the system displays a status icon for ‘not on the phone’ on the watcher device when
                                          the presence entity is off-hook (but not in a call connected state). These phones do not detect an off-hook status. For all
                                          other phone types, the system displays the status icon for ‘on the phone’ on the watcher device for an off-hook condition
                                          at the presence entity.

SIP Trunks

BLF presence
                                          				requests and responses must route to SIP trunks or routes that are associated
                                          				with SIP trunks. The system rejects BLF presence requests routing to MGCP and H323
                                          				trunk devices.

BLF Presence-supported Phones that are running SIP

For BLF presence-supported phones that are running SIP, you can
                                          				configure directory numbers or SIP URIs as BLF and SpeedDial buttons. For BLF
                                          				presence-supported phones that are running SCCP, you can only configure
                                          				directory numbers as BLF and SpeedDial buttons.

Phones that are running SIP

For phones that are running SIP, BLF presence group authorization
                                          				also does not apply to any directory number or SIP URI that is configured as a
                                          				BLF and Speed Dial that appears in a call list.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure and
                                       			 synchronize cluster-wide enterprise parameters for Busy Lamp Field (BLF). See Configure/Synchronize Cluster-Wide Enterprise Parameters for BLF . | Configure BLF
                                       			 options that apply to all devices and services in the same cluster. You can
                                       			 synchronize enterprise-parameter configuration changes with the configured
                                       			 devices in the least-intrusive manner. For example, a reset or restart may not
                                       			 be required on some affected devices. |
| Step 2 | Configure
                                       			 cluster-wide service parameters for BLF. See Configure Cluster-Wide Service Parameters for BLF . | Configure
                                       			 presence service parameters to configure different services on selected servers
                                       			 in Cisco Unified
                                          				Communications Manager Administration . |
| Step 3 | Configure BLF
                                       			 presence groups. See Configure BLF Presence Groups . | Configure BLF
                                       			 presence groups to control the destinations that watchers can monitor. |
| Step 4 | To associate
                                       			 BLF presence group with devices and users, perform the following subtasks: Associate BLF presence
                                          				groups with phones. See Associate BLF Presence Groups with Phone . Associate BLF presence
                                          				groups with SIP trunks. See Associate BLF Presence Groups with SIP Trunk . Associate BLF presence
                                          				groups with an end user. See Associate BLF Presence Groups with End User . Associate BLF presence
                                          				groups with an application user. See Associate BLF Presence Groups with Application User . | Apply a BLF
                                       			 presence group to a directory number, SIP trunk, phone that is running SIP,
                                       			 phone that is running SCCP, application user (for application users that are
                                       			 sending presence requests over the SIP trunk), or end user. |
| Step 5 | Accept BLF
                                       			 presence requests from external trunks and applications. See Accept BLF Presence Requests from External Trunks and Applications . | To
                                       			 enable application-level authorization for a SIP trunk application in addition
                                       			 to trunk-level authorization. |
| Step 6 | Configure
                                       			 Calling Search Space. See Configure a Calling Search Space for Presence Requests . | Apply a
                                       			 SUBSCRIBE Calling Search Space to the SIP trunk, phone, or end user. The
                                       			 SUBSCRIBE Calling Search Space determines how Cisco Unified
                                          				Communications Manager routes presence requests that come from the
                                       			 trunk or the phone. Calling search spaces determine the partitions that calling
                                       			 devices search when they are attempting to complete a call. If you do not
                                       			 select a different calling search space for presence requests, the SUBSCRIBE
                                       			 Calling Search Space selects the default option, which is None . |
| Step 7 | Configure a
                                       			 phone button template for BLF and SpeedDial buttons. See Configure a Phone Button Template for BLF and SpeedDial Buttons . | Configure a
                                       			 phone button template for BLF and SpeedDial buttons for a phone, or user device
                                       			 profile. Note If the
                                                   				template does not support BLF and SpeedDials, the Add
                                                      				  a new BLF SD link appears in the Unassigned Associated Items pane. | Note | If the
                                                   				template does not support BLF and SpeedDials, the Add
                                                      				  a new BLF SD link appears in the Unassigned Associated Items pane. |
| Note | If the
                                                   				template does not support BLF and SpeedDials, the Add
                                                      				  a new BLF SD link appears in the Unassigned Associated Items pane. |
| Step 8 | Associate
                                       			 button template with a device. See Associate Button Template with a Device . | Use a
                                       			 button template with a configured device for the BLF presence. |
| Step 9 | Configure user
                                       			 device profile. See Configure User Device Profile . | Configure the
                                       			 user device profiles for BLF presence. |

| Note | If the
                                                   				template does not support BLF and SpeedDials, the Add
                                                      				  a new BLF SD link appears in the Unassigned Associated Items pane. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Enterprise Parameters . |
|---|---|
| Step 2 | Configure the fields in the Enterprise Parameters Configuration window. For more information on the fields and their configuration options, see Online Help. Tip For details about an enterprise parameter, click the parameter name or the question mark that appears in the Enterprise Parameter Configuration window. | Tip | For details about an enterprise parameter, click the parameter name or the question mark that appears in the Enterprise Parameter Configuration window. |
| Tip | For details about an enterprise parameter, click the parameter name or the question mark that appears in the Enterprise Parameter Configuration window. |
| Step 3 | Click Save . |
| Step 4 | (Optional) Click Apply Config to synchronize cluster-wide parameters. The Apply Configuration Information dialog box appears. |
| Step 5 | Click OK . |

| Tip | For details about an enterprise parameter, click the parameter name or the question mark that appears in the Enterprise Parameter Configuration window. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose the server where you
                                          			 want to configure the parameter. |
| Step 3 | Configure the fields in the Service Parameters Configuration window. For more information on the fields and their configuration options, see Online Help. Tip For details about the service parameters, click the parameter name or the question mark that appears in the Service Parameter Configuration window. | Tip | For details about the service parameters, click the parameter name or the question mark that appears in the Service Parameter Configuration window. |
| Tip | For details about the service parameters, click the parameter name or the question mark that appears in the Service Parameter Configuration window. |
| Step 4 | Click Save . Note The Default
                                                      				Inter-Presence Group Subscription parameter does not apply to BLF and SpeedDials. | Note | The Default
                                                      				Inter-Presence Group Subscription parameter does not apply to BLF and SpeedDials. |
| Note | The Default
                                                      				Inter-Presence Group Subscription parameter does not apply to BLF and SpeedDials. |

| Tip | For details about the service parameters, click the parameter name or the question mark that appears in the Service Parameter Configuration window. |
|---|---|

| Note | The Default
                                                      				Inter-Presence Group Subscription parameter does not apply to BLF and SpeedDials. |
|---|---|

| Note | The system
                                             			 always allows BLF presence requests within the same BLF presence group. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > BLF Presence Group . |
|---|---|
| Step 2 | Configure the fields in the BLF Presence Group Configuration window. See BLF Presence Group Fields for BLF for details about the fields and their configuration options. Note Use the Default Inter-Presence Group Subscription service parameter for the Cisco CallManager service. It sets the clusterwide permissions parameter for BLF presence groups
                                                         to allow subscription or disallow subscription. This field enables administrators to set a system default and configure BLF
                                                         presence group relationships by using the default field for the cluster. | Note | Use the Default Inter-Presence Group Subscription service parameter for the Cisco CallManager service. It sets the clusterwide permissions parameter for BLF presence groups
                                                         to allow subscription or disallow subscription. This field enables administrators to set a system default and configure BLF
                                                         presence group relationships by using the default field for the cluster. |
| Note | Use the Default Inter-Presence Group Subscription service parameter for the Cisco CallManager service. It sets the clusterwide permissions parameter for BLF presence groups
                                                         to allow subscription or disallow subscription. This field enables administrators to set a system default and configure BLF
                                                         presence group relationships by using the default field for the cluster. |
| Step 3 | Click Save . Note The permissions that you configure for a BLF presence group
                                                         				  appear in the BLF Presence Group Relationship pane. Permissions
                                                         				  that use the system default permission field for the group-to-group
                                                         				  relationship do not appear. | Note | The permissions that you configure for a BLF presence group
                                                         				  appear in the BLF Presence Group Relationship pane. Permissions
                                                         				  that use the system default permission field for the group-to-group
                                                         				  relationship do not appear. |
| Note | The permissions that you configure for a BLF presence group
                                                         				  appear in the BLF Presence Group Relationship pane. Permissions
                                                         				  that use the system default permission field for the group-to-group
                                                         				  relationship do not appear. |

| Note | Use the Default Inter-Presence Group Subscription service parameter for the Cisco CallManager service. It sets the clusterwide permissions parameter for BLF presence groups
                                                         to allow subscription or disallow subscription. This field enables administrators to set a system default and configure BLF
                                                         presence group relationships by using the default field for the cluster. |
|---|---|

| Note | The permissions that you configure for a BLF presence group
                                                         				  appear in the BLF Presence Group Relationship pane. Permissions
                                                         				  that use the system default permission field for the group-to-group
                                                         				  relationship do not appear. |
|---|---|

| Field | Description |
|---|---|
| Name | Enter
                                                						the name of the BLF presence group that you want to configure. For example,
                                                						Executive_Group. |
| Description | Enter a
                                                						description for the BLF presence group that you are configuring. |
| Modify
                                                						Relationship to Other Presence Groups | Select
                                                						one or more BLF presence groups to configure the permission fields for the
                                                						named group to the selected groups. |
| Subscription Permission | For the
                                                						selected BLF presence groups, choose one of the following options from the
                                                						drop-down list: Use System
                                                      							 Default —Set the permissions field to the Default Inter-Presence
                                                   						  Group Subscription clusterwide service parameter field (Allow Subscription or
                                                   						  Disallow Subscription). Allow
                                                      							 Subscription —Allow members in the named group to view the
                                                   						  real-time status of members in the selected groups. Disallow
                                                      							 Subscription —Block members in the named group from viewing the
                                                   						  real-time status of members in the selected groups. The
                                                						permissions that you configure appear in the BLF Presence Group relationship
                                                						pane when you click Save . All groups that use system default permission
                                                						field do not appear. |

| Note | The
                                             			 system allows presence requests between members in the same BLF presence group. |
|---|---|

| Step 1 | In the Cisco Unified CM Administration, choose Device > Phone ,
                                             			 and click Add New . The Add a New Phone window appears. |
|---|---|
| Step 2 | From the Phone Type drop-down list, select the type of
                                             			 phone that you want to associate BLF presence group to. |
| Step 3 | Click Next . |
| Step 4 | Configure the fields in the Phone Configuration window. See the online help
                                             			 for information about the fields and their configuration options. Note From the SUBSCRIBE Calling Search Space drop-down
                                                            				  list, select a SUBSCRIBE calling search space to use for presence requests for
                                                            				  the phone. All calling search spaces that you configure in Cisco Unified
                                                            				  Communications Manager Administration appear in the SUBSCRIBE Calling Search Space drop-down
                                                            				  list. If you do not select a different calling search space for the end user
                                                            				  from the drop-down list, the value of this field applies the default value as None . To configure a SUBSCRIBE calling
                                                            				  search space specifically for this purpose, configure a calling search space as
                                                            				  you configure all calling search spaces. | Note | From the SUBSCRIBE Calling Search Space drop-down
                                                            				  list, select a SUBSCRIBE calling search space to use for presence requests for
                                                            				  the phone. All calling search spaces that you configure in Cisco Unified
                                                            				  Communications Manager Administration appear in the SUBSCRIBE Calling Search Space drop-down
                                                            				  list. If you do not select a different calling search space for the end user
                                                            				  from the drop-down list, the value of this field applies the default value as None . To configure a SUBSCRIBE calling
                                                            				  search space specifically for this purpose, configure a calling search space as
                                                            				  you configure all calling search spaces. |
| Note | From the SUBSCRIBE Calling Search Space drop-down
                                                            				  list, select a SUBSCRIBE calling search space to use for presence requests for
                                                            				  the phone. All calling search spaces that you configure in Cisco Unified
                                                            				  Communications Manager Administration appear in the SUBSCRIBE Calling Search Space drop-down
                                                            				  list. If you do not select a different calling search space for the end user
                                                            				  from the drop-down list, the value of this field applies the default value as None . To configure a SUBSCRIBE calling
                                                            				  search space specifically for this purpose, configure a calling search space as
                                                            				  you configure all calling search spaces. |
| Step 5 | Click Save . |

| Note | From the SUBSCRIBE Calling Search Space drop-down
                                                            				  list, select a SUBSCRIBE calling search space to use for presence requests for
                                                            				  the phone. All calling search spaces that you configure in Cisco Unified
                                                            				  Communications Manager Administration appear in the SUBSCRIBE Calling Search Space drop-down
                                                            				  list. If you do not select a different calling search space for the end user
                                                            				  from the drop-down list, the value of this field applies the default value as None . To configure a SUBSCRIBE calling
                                                            				  search space specifically for this purpose, configure a calling search space as
                                                            				  you configure all calling search spaces. |
|---|---|

| Tip | To use BLF presence group authorization with incoming presence
                                                			 requests on a SIP trunk, configure a presence group for the trunk, such as
                                                			 External_Presence_Serv_Group1, and configure the appropriate permissions to
                                                			 other groups inside the cluster. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Trunk , and click Add New . |
|---|---|
| Step 2 | From the Trunk
                                                				Type drop-down list, select the type of phone that you want to associate
                                             			 BLF presence group. The
                                             			 value in the Device
                                                				Protocol drop-down list populates automatically. |
| Step 3 | Click Next . |
| Step 4 | Configure the
                                             			 fields in the Trunk
                                                				Configuration window. See the online help for information about the
                                             			 fields and their configuration options. Note To authorize the Unified CM system to accept incoming BLF presence requests from the SIP trunk, check the Accept Presence Subscription check box in the SIP Trunk Security Profile Configuration window. To block incoming presence requests on a SIP trunk, uncheck
                                                            the check box. When you allow SIP trunk BLF presence requests, Unified CM accepts requests from the SIP user agent (SIP proxy
                                                            server or external BLF presence server) that connects to the trunk. Consider digest authentication as optional when Unified
                                                            CM is configured to accept BLF presence requests from a SIP trunk. | Note | To authorize the Unified CM system to accept incoming BLF presence requests from the SIP trunk, check the Accept Presence Subscription check box in the SIP Trunk Security Profile Configuration window. To block incoming presence requests on a SIP trunk, uncheck
                                                            the check box. When you allow SIP trunk BLF presence requests, Unified CM accepts requests from the SIP user agent (SIP proxy
                                                            server or external BLF presence server) that connects to the trunk. Consider digest authentication as optional when Unified
                                                            CM is configured to accept BLF presence requests from a SIP trunk. |
| Note | To authorize the Unified CM system to accept incoming BLF presence requests from the SIP trunk, check the Accept Presence Subscription check box in the SIP Trunk Security Profile Configuration window. To block incoming presence requests on a SIP trunk, uncheck
                                                            the check box. When you allow SIP trunk BLF presence requests, Unified CM accepts requests from the SIP user agent (SIP proxy
                                                            server or external BLF presence server) that connects to the trunk. Consider digest authentication as optional when Unified
                                                            CM is configured to accept BLF presence requests from a SIP trunk. |
| Step 5 | Click Save . |

| Note | To authorize the Unified CM system to accept incoming BLF presence requests from the SIP trunk, check the Accept Presence Subscription check box in the SIP Trunk Security Profile Configuration window. To block incoming presence requests on a SIP trunk, uncheck
                                                            the check box. When you allow SIP trunk BLF presence requests, Unified CM accepts requests from the SIP user agent (SIP proxy
                                                            server or external BLF presence server) that connects to the trunk. Consider digest authentication as optional when Unified
                                                            CM is configured to accept BLF presence requests from a SIP trunk. |
|---|---|

| Step 1 | In the Cisco Unified CM Administration, choose User Management > End
                                                   				  User , and click Add New . The End User Configuration window appears. |
|---|---|
| Step 2 | Configure the fields in the End User Configuration window. See the online
                                             			 help for information about the fields and their configuration options. |
| Step 3 | Click Save . |

| Step 1 | In the Cisco Unified CM Administration, choose User
                                                   				  Management > Application User ,
                                             			 and click Add New . The Application User Configuration window appears. |
|---|---|
| Step 2 | Configure the fields in the Application User Configuration window. See the
                                             			 online help for information about the fields and their configuration options. |
| Step 3 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Trunk , and click Add New . The Trunk Configuration window appears. |
|---|---|
| Step 2 | To allow BLF presence requests from a SIP trunk, check the Accept Presence Subscription check box in the SIP Trunk Security Profile Configuration window. |
| Step 3 | To enable application-level authorization for a SIP trunk
                                          			 application in addition to trunk-level authorization, check the following check
                                          			 boxes in the SIP Trunk Security Profile Configuration window: Enable Digest Authentication Enable Application Level Authorization Note You cannot check Enable Application Level Authorization unless Enable Digest Authentication is checked. | Note | You cannot check Enable Application Level Authorization unless Enable Digest Authentication is checked. |
| Note | You cannot check Enable Application Level Authorization unless Enable Digest Authentication is checked. |
| Step 4 | Apply the profile to the trunk. Click Reset so that the changes to the trunk can
                                          			 take effect. Note If you checked Enable Application Level Authorization ,
                                                         				  check the Accept Presence Subscription check box in
                                                         				  the Application User Configuration window for
                                                         				  the application. | Note | If you checked Enable Application Level Authorization ,
                                                         				  check the Accept Presence Subscription check box in
                                                         				  the Application User Configuration window for
                                                         				  the application. |
| Note | If you checked Enable Application Level Authorization ,
                                                         				  check the Accept Presence Subscription check box in
                                                         				  the Application User Configuration window for
                                                         				  the application. |

| Note | You cannot check Enable Application Level Authorization unless Enable Digest Authentication is checked. |
|---|---|

| Note | If you checked Enable Application Level Authorization ,
                                                         				  check the Accept Presence Subscription check box in
                                                         				  the Application User Configuration window for
                                                         				  the application. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Calling Search Space . |
|---|---|
| Step 2 | In the Calling Search Space configuration window,
                                          			 choose the calling search space from the SUBSCRIBE Calling Search Space drop-down list. |
| Step 3 | Click Add
                                             				New . |
| Step 4 | In the Name field, enter a name. |
| Step 5 | (Optional) In the Description field, enter a description to identify the calling search space. |
| Step 6 | From the Available Partitions list, select one or
                                          			 multiple partitions, and click the arrow keys. The
                                          			 selected partitions appear in the Selected Partitions list. |
| Step 7 | (Optional) To add or remove a partition from the Selected Partitions list, click the arrow keys next to the list box. |
| Step 8 | Click Save . All calling search spaces that you configure in Cisco Unified Communications Manager Administration appear in the SUBSCRIBE Calling Search Space drop-down list in the Trunk Configuration or Phone Configuration window. |

| Note | If the template
                                             			 does not support BLF and SpeedDials, the Add a new BLF SD link appears in the Unassigned Associated Items pane. |
|---|---|

| Note | You do not need to configure BLF presence groups or
                                          		  the Default Inter-Presence Group Subscription parameter for BLF and SpeedDials. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Phone Button Template . |
|---|---|
| Step 2 | Click the Add
                                             				New button. The Phone
                                             				Button Template Configuration window appears. |
| Step 3 | In the Button
                                             				Template Name field, enter a name for the template. |
| Step 4 | From the Phone
                                             				Button Template drop-down list, select a template of phone button. |
| Step 5 | Click Copy to create a new button template based on the
                                          			 layout of the selected button template. |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Device Profile . |
|---|---|
| Step 2 | Enter the search parameters to find the configured phone button
                                          			 templates, and click Find . The records matching all the search criteria appear. |
| Step 3 | Click one of the records. The Device Profile Configuration window appears. |
| Step 4 | From the Phone Button Template list, select a
                                          			 configured phone button template. |
| Step 5 | (Optional) Modify the values of the configured device. |
| Step 6 | Click Save . |

| Step 1 | In the Cisco
                                          			 Unified CM Administration, choose Device > Device
                                                				  Settings > Device Profile . |
|---|---|
| Step 2 | Click Add
                                             				New . The Device
                                             				Profile Configuration window appears. |
| Step 3 | Configure the
                                          			 fields in Device
                                             				Profile Configuration window. See the online help for information
                                          			 about the fields and their configuration options. Note If the
                                                         				  phone button template that you applied to the phone or device profile does not
                                                         				  support BLF and SpeedDials, the link does not appear in the Association Information pane, but appears in the Unassigned Associated Items pane. | Note | If the
                                                         				  phone button template that you applied to the phone or device profile does not
                                                         				  support BLF and SpeedDials, the link does not appear in the Association Information pane, but appears in the Unassigned Associated Items pane. |
| Note | If the
                                                         				  phone button template that you applied to the phone or device profile does not
                                                         				  support BLF and SpeedDials, the link does not appear in the Association Information pane, but appears in the Unassigned Associated Items pane. |
| Step 4 | Click Save . |

| Note | If the
                                                         				  phone button template that you applied to the phone or device profile does not
                                                         				  support BLF and SpeedDials, the link does not appear in the Association Information pane, but appears in the Unassigned Associated Items pane. |
|---|---|

| Feature | Interaction |
|---|---|
| Presence
                                          						BLF with DNs on H.323 phones when the H.323 phone device serves as presence entity | When the
                                          						H.323 phone is in the RING IN state, the BLF status gets reported as Busy. For
                                          						the presence entities of phones that are running either SCCP or SIP and that are
                                          						in the RING IN state, the BLF status gets reported as Idle. |
| Presence
                                          						BLF with DNs on H.323 phones when the H.323 phone device serves as presence entity | When the
                                          						H.323 phone is not connected to Cisco Unified
                                             						  Communications Manager for any reason, such as the Ethernet cable is
                                          						unplugged from the phone, the BLF status gets reported as Idle all the time.
                                          						For presence entities of phones that are running either SCCP or SIP and that are not
                                          						connected to Cisco Unified
                                             						  Communications Manager , the BLF status gets reported as Unknown. |
| BLF Presence with Extension Mobility | When you configure BLF and SpeedDial buttons in a user
                                          						device profile in Cisco Unified
                                             						  Communications Manager Administration , a phone that supports Cisco
                                             						  Extension Mobility displays BLF presence status on the BLF and SpeedDial
                                          						buttons after you log in to the device. When the extension mobility user logs out, a phone
                                          						that supports Cisco
                                             						  Extension Mobility displays BLF presence status on the BLF and SpeedDial
                                          						buttons for the logout profile that is configured. |

| Restriction | Description |
|---|---|
| SIP Presence | Cisco Unified Communications Manager Assistant does not support SIP presence. |
| BLF
                                          				Presence Requests | Cisco Unified Communications Manager Administration rejects BLF presence requests to a directory number that is associated with a hunt pilot. |
| BLF on
                                          				Call List Feature | The BLF on
                                          				call list feature is not supported on the Cisco Unified IP Phone 7940 and Cisco
                                          				Unified IP Phone 7960. |
| BLF and SpeedDials | The administrator ensures that the watcher is authorized to monitor the destination when configuring a BLF and SpeedDial.
                                          BLF presence group authorization does not apply to BLF and SpeedDials. Note BLF presence group authorization does not apply to any directory number or SIP URI that is configured as a BLF and Speed Dial
                                                      that appears in a call list for phones that are running SIP. If there is an overlapping DN, where there is the same extension in different partitions, the presence notifications are selected
                                          based on the order of the partitions configured within the SUBSCRIBE CSS assigned to the device. For example, two BLF speed dials are configured on a phone. Extension 1234 in the "internal" partition Extension 1234 in the "external" partition Whichever partition is listed first within the SUBSCRIBE CSS is the one that will provide BLF presence to the subscribed devices. | Note | BLF presence group authorization does not apply to any directory number or SIP URI that is configured as a BLF and Speed Dial
                                                      that appears in a call list for phones that are running SIP. |
| Note | BLF presence group authorization does not apply to any directory number or SIP URI that is configured as a BLF and Speed Dial
                                                      that appears in a call list for phones that are running SIP. |
| BLF Presence
                                          				Authorization | For Cisco Unified IP Phone s with multiple lines, the phone uses the cached information that is associated with the line directory number for missed
                                          and placed calls to determine BLF presence authorization. If this call information is not present, the phone uses the primary
                                          line as the subscriber for BLF presence authorization. For BLF and SpeedDial buttons on Cisco Unified IP Phone s with multiple lines, the phone uses the first available line as the subscriber. |
| Cisco Unified IP
                                          				  Phone | When a user monitors a directory number that is configured for Cisco Unified IP Phone s 7960 and 7940 that are running SIP, the system displays a status icon for ‘not on the phone’ on the watcher device when
                                          the presence entity is off-hook (but not in a call connected state). These phones do not detect an off-hook status. For all
                                          other phone types, the system displays the status icon for ‘on the phone’ on the watcher device for an off-hook condition
                                          at the presence entity. |
| SIP Trunks | BLF presence
                                          				requests and responses must route to SIP trunks or routes that are associated
                                          				with SIP trunks. The system rejects BLF presence requests routing to MGCP and H323
                                          				trunk devices. |
| BLF Presence-supported Phones that are running SIP | For BLF presence-supported phones that are running SIP, you can
                                          				configure directory numbers or SIP URIs as BLF and SpeedDial buttons. For BLF
                                          				presence-supported phones that are running SCCP, you can only configure
                                          				directory numbers as BLF and SpeedDial buttons. |
| Phones that are running SIP | For phones that are running SIP, BLF presence group authorization
                                          				also does not apply to any directory number or SIP URI that is configured as a
                                          				BLF and Speed Dial that appears in a call list. |

| Note | BLF presence group authorization does not apply to any directory number or SIP URI that is configured as a BLF and Speed Dial
                                                      that appears in a call list for phones that are running SIP. |
|---|---|