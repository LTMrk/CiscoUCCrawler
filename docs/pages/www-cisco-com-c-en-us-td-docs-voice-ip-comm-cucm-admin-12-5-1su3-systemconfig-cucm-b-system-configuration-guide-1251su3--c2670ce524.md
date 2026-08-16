---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su3-systemconfig-cucm-b-system-configuration-guide-1251su3--c2670ce524
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU3/systemConfig/cucm_b_system-configuration-guide-1251su3/cucm_mp_a5ae4725_00_autoregistration-configuration12-0.html
retrieved_at: 2026-08-16T17:42:59.721395+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

Updated: July 31, 2025

Chapter: Configure Autoregistration

## Chapter: Configure Autoregistration

# Configure Autoregistration

## Autoregistration
                        	 Overview

Autoregistration allows Unified Communications Manager to automatically assign directory numbers to new phones when you plug those phones in to your network.

Autoregistration is
                              		  enabled on secure mode now. This enhancement provides greater security for your
                              		  system because you can secure your cluster while provisioning new phones. It
                              		  also simplifies the registration process because you don't have to disable
                              		  cluster security to register new phones.

If you create a
                              		  device pool that allows only 911 (emergency) and 0 (operator) calls, you can
                              		  use that to prevent unauthorized endpoints from connecting to your network when
                              		  autoregistration is enabled. New endpoints can register to this pool, but their
                              		  access is limited. Unauthorized access by rogue devices that continuously boot
                              		  in and attempt to register to your network is prevented. You can move a phone
                              		  that has auto-registered to a new location and assign it to a different device
                              		  pool without affecting its directory number.

The system doesn't know whether the new phones that are auto-registering are running SIP or SCCP, so you must specify this
                              when you enable autoregistration. Devices that support both SIP and SCCP (such as Cisco IP Phones 7911, 7940, 7941, 7960,
                              7961) auto-register with the protocol that is specified in the enterprise parameter called Auto Registration Phone Protocol.

Devices that support only a single protocol will auto-register with that protocol. The Auto Registration Phone Protocol setting
                              is ignored. For example, any Cisco IP Phones that support SCCP only will autoregister with SCCP even if the Auto Registration
                              Phone Protocol parameter is set to SIP.

We recommend that
                              		  you use autoregistration to add fewer than 100 phones to your network. To add
                              		  more than 100 phones, use the Bulk Administration Tool (BAT). For more
                              		  information, see Cisco Unified
                                 			 Communications Manager Bulk Administration Guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

## Configure
                        	 Autoregistration Task Flow

Enabling
                              		  autoregistration carries a security risk. Enable autoregistration only for
                              		  brief periods while you add new endpoints to the network.

Step 1

Configure a Partition for Autoregistration

Configure a
                                          				route partition to use specifically for autoregistration to limit
                                          				auto-registered phones to internal calls only.

Step 2

Configure a Calling Search Space for Autoregistration

Configure a
                                          				calling search space to use specifically for autoregistration to limit
                                          				auto-registered phones to internal calls only.

Step 3

Configure a Device Pool for Autoregistration

Create a
                                          				device pool that uses the calling search space that is configured for
                                          				autoregistration.

Step 4

Set the Device Protocol Type for Autoregistration

Step 5

Enable Autoregistration

Enable
                                          				autoregistration on the node to use for autoregistration and set the Auto-registration Cisco Unified Communications Manager Group parameter to enable autoregistration for the Cisco Unified Communications Manager group that is to
                                          				be used for autoregistration.

Step 6

Disable Autoregistration

Disable
                                          				autoregistration for the node as soon as you are finished registering new
                                          				devices.

Step 7

Reuse Autoregistration Numbers

Optional.
                                          				Autoregistration numbers for devices that have been disabled can be reused.
                                          				When you reset the range of autoregistration directory numbers, you force the
                                          				system to search again from the starting number. Available directory numbers
                                          				are reused.

### Configure a Partition for Autoregistration

Configure a route partition to use specifically for autoregistration to limit auto-registered phones to internal calls only.

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

#### What to do next

Configure a Calling Search Space for Autoregistration

### Configure a
                           	 Calling Search Space for Autoregistration

Configure a
                                 		  calling search space to use specifically for autoregistration to limit
                                 		  auto-registered phones to internal calls only.

#### Before you begin

Configure a Partition for Autoregistration

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

#### What to do next

Configure a Device Pool for Autoregistration

### Configure a Device Pool for Autoregistration

You can use the Default device pool for autoregistration or configure separate device pools for SIP and SCCP  devices to use
                                 for autoregistration.

To configure the Default device pool for autoregistration, assign the Default Cisco Unified Communications Manager Group and the autoregistration calling search space (CSS) to the Default device pool. If you choose to configure a separate
                                 default device pool for SIP and SCCP  devices, use the default device pool values.

#### Before you begin

Configure a Calling Search Space for Autoregistration

Step 1

From Cisco Unified Communications Manager Administration , choose System > Device Pool .

Step 2

To modify the Default device pool for autoregistration, perform the following actions:

Click Find , then select Default from the list of device pools.

In the Device Pool Configuration window, select the CSS  to be used for autoregistration in the Calling Search Space for Auto-registration field, then click Save .

Step 3

To create a new device pool for autoregistration, perform the following actions:

Click Add New .

In the Device Pool Configuration window, enter a unique name for the device pool.

You can enter up to 50 characters, which include alphanumeric characters, periods (.), hyphens (-), underscores (_), and blank
                                                   spaces.

Set the following fields to match the Default device pool. See the online help for field descriptions.

In Cisco Unified Communications Manager Group , select Default .

In Date/Time Group , select CMLocal

In Region , select Default .

Select the CSS  to be used for autoregistration in the Calling Search Space for Auto-registration field, then click Save .

#### What to do next

Set the Device Protocol Type for Autoregistration

### Set the Device Protocol Type for Autoregistration

If you have SIP and SCCP devices to auto-register, you must first set the Auto Registration Phone Protocol parameter to SCCP
                                 and install all the devices that are running SCCP. Then change the Auto Registration Phone Protocol parameter to SIP and auto-register
                                 all the devices that are running SIP.

#### Before you begin

Configure a Device Pool for Autoregistration

Step 1

In Cisco Unified Communications Manager Administration , select System > Enterprise Parameters .

Step 2

In the Enterprise Parameters Configuration window, select either SCCP or SIP in the Auto Registration Phone Protocol drop-down list, then click Save .

#### What to do next

Enable Autoregistration

### Enable Autoregistration

When you enable autoregistration, you must specify a range of directory numbers that get assigned to the new endpoints as
                                 they connect to the network. As each  new endpoint connects, the next available directory number is assigned. After all the
                                 available autoregistration directory numbers are used up, no more endpoints can auto-register.

New endpoints auto-register with the first Unified Communications Manager node in the group that has the Auto-Registration Cisco Unified Communications Manager Group setting enabled. That node then automatically assigns each auto-registered endpoint to a default device pool according to
                                 the device type.

#### Before you begin

Create a device pool, calling search space, and route partition  that restricts the access of devices that are auto-registering
                                       to allow only internal calls.

Ensure that directory numbers are available in the autoregistration range.

Ensure that there are enough license points available to register the new phones.

Check that the correct phone image names for SIP and SCCP appear on the Device Defaults Configuration window. Although most of the common device configuration files should be available on the TFTP server, make sure that the
                                       configuration files for your devices are there.

Ensure that the Cisco TFTP server is up and running and that the DHCP option for TFTP specifies the correct server.

Step 1

From Cisco Unified Communications Manager Administration , select System > Cisco Unified CM , then click Find in the Find and List Cisco Unified Communications Managers window.

Step 2

Select the Cisco Unified Communications Manager in the   cluster to use for autoregistration.

appears.

Step 3

In the Cisco Unified CM Configuration widow, configure the autoregistration parameters for the node in the Auto-registration Information section, then click Save . For more information on the fields and their configuration options, see the system Online Help.

Select the universal device template to use for autoregistration from the drop-down list.

If no universal device template is created for autoregistration, you can select Default Universal Device Template . Make sure that the selected template specifies the device pool that is to be used for autoregistration from User Management > User/Phone Add > Universal Device Template .

Select the universal line template to use for autoregistration from the drop-down list.

If no universal line template is created for autoregistration, you can select Default Universal Line Template .  Make sure that the selected template specifies the calling search space and the route partition that are to be used for
                                                   autoregistration from User Management > User/Phone Add > Universal Line Template .

Enter the starting and ending directory numbers in to the Starting Directory Number and Ending Directory Number fields.

Setting the starting and ending directory numbers to the same value disables autoregistration.

Uncheck Auto-registration Disabled on this Cisco Unified Communications Manager to enable autoregistration for this node.

Always enable or disable autoregistration on only the selected Unified Communications Manager node. If you switch the autoregistration function to another node in the cluster, you must reconfigure the Unified Communications Manager nodes, the Default Unified Communications Manager group, and the default device pools that you used.

Step 4

Select System > Cisco Unified CM Group , then click Find in the Find and List Cisco Unified Communications Manager Groups window.

Step 5

Select the Unified Communications Manager group to enable for autoregistration.

In most cases, the name of this group is Default . You can choose a different Cisco Unified Communications Manager group. The group must have at least one node selected.

Step 6

In the Cisco Unified CM Group Configuration window for that group, select Auto-registration Cisco Unified Communications Manager Group to enable autoregistration for  the group, then click Save .

Tip

Ensure that the Selected Cisco Unified Communications Managers list contains the node that you configured for autoregistration. Use the arrows to move the node to appear in the list. The Unified Communications Manager nodes get selected in the order in which they are listed. Save your changes.

Step 7

Install the devices that you want to auto-register.

### Disable Autoregistration

Disable autoregistration for the node as soon as you are finished registering new devices.

#### Before you begin

Enable Autoregistration

Step 1

In Cisco Unified Communications Manager Administration , select System > Cisco Unified CM , then click Find in the Find and List Cisco Unified CM window.

Step 2

Select the Cisco Unified Communications Manager from   the list of nodes.

Step 3

In the Cisco Unified CM Configuration widow for the selected node, check the Auto-registration Disabled on this Cisco Unified Communications Manager check box to disable autoregistration for this node, then click Save .

Tip

Setting the same value in the Starting Directory Number and Ending Directory Number fields also disables autoregistration.

#### What to do next

Optional. If you manually changed the directory number of an auto-registered device, or if you delete that device from the
                                 database, you can reuse the directory number. For details, see Reuse Autoregistration Numbers .

### Reuse Autoregistration Numbers

When you connect a new device to the network, the system assigns the next available autoregistration directory number to that
                                 device. If you manually change the directory number of an auto-registered device, or if you delete that device from the database,
                                 the autoregistration directory number of that device can be reused.

When a device attempts to auto-register, the system searches the range of autoregistration numbers that you specified and
                                 tries to find the next available directory number to assign to the device. It begins the search with the next directory number
                                 in sequence after the last one that was assigned. If it reaches the ending directory number in the range, the system continues
                                 to search from the starting directory number in the range.

You can reset the range of autoregistration directory numbers and force the system to search from the starting number in the
                                 range.

Step 1

In Cisco Unified Communications Manager Administration , select System > Cisco Unified Communications Manager

Step 2

Select the Cisco Unified Communications Manager to reset for autoregistration.

Step 3

Write down the current settings in the Starting Directory Number and Ending Directory Number fields.

Step 4

Click Auto-registration Disabled on this Cisco Unified Communications Manager , then click Save .

New phones cannot auto-register while autoregistration is disabled.

Step 5

Set the Starting Directory Number and Ending Directory Number fields to their previous values, then click Save .

Tip

You could  set the fields  to new values.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure a Partition for Autoregistration | Configure a
                                          				route partition to use specifically for autoregistration to limit
                                          				auto-registered phones to internal calls only. |
| Step 2 | Configure a Calling Search Space for Autoregistration | Configure a
                                          				calling search space to use specifically for autoregistration to limit
                                          				auto-registered phones to internal calls only. |
| Step 3 | Configure a Device Pool for Autoregistration | Create a
                                          				device pool that uses the calling search space that is configured for
                                          				autoregistration. |
| Step 4 | Set the Device Protocol Type for Autoregistration | Use
                                       			 this procedure to set the protocol to SCCP or SIP to match the type of phones
                                       			 you are auto-registering. |
| Step 5 | Enable Autoregistration | Enable
                                          				autoregistration on the node to use for autoregistration and set the Auto-registration Cisco Unified Communications Manager Group parameter to enable autoregistration for the Cisco Unified Communications Manager group that is to
                                          				be used for autoregistration. |
| Step 6 | Disable Autoregistration | Disable
                                          				autoregistration for the node as soon as you are finished registering new
                                          				devices. |
| Step 7 | Reuse Autoregistration Numbers | Optional.
                                          				Autoregistration numbers for devices that have been disabled can be reused.
                                          				When you reset the range of autoregistration directory numbers, you force the
                                          				system to search again from the starting number. Available directory numbers
                                          				are reused. |

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

| Step 1 | From Cisco Unified Communications Manager Administration , choose System > Device Pool . |
|---|---|
| Step 2 | To modify the Default device pool for autoregistration, perform the following actions: Click Find , then select Default from the list of device pools. In the Device Pool Configuration window, select the CSS  to be used for autoregistration in the Calling Search Space for Auto-registration field, then click Save . |
| Step 3 | To create a new device pool for autoregistration, perform the following actions: Click Add New . In the Device Pool Configuration window, enter a unique name for the device pool. You can enter up to 50 characters, which include alphanumeric characters, periods (.), hyphens (-), underscores (_), and blank
                                                   spaces. Set the following fields to match the Default device pool. See the online help for field descriptions. In Cisco Unified Communications Manager Group , select Default . In Date/Time Group , select CMLocal In Region , select Default . Select the CSS  to be used for autoregistration in the Calling Search Space for Auto-registration field, then click Save . |

| Step 1 | In Cisco Unified Communications Manager Administration , select System > Enterprise Parameters . |
|---|---|
| Step 2 | In the Enterprise Parameters Configuration window, select either SCCP or SIP in the Auto Registration Phone Protocol drop-down list, then click Save . |

| Step 1 | From Cisco Unified Communications Manager Administration , select System > Cisco Unified CM , then click Find in the Find and List Cisco Unified Communications Managers window. |
|---|---|
| Step 2 | Select the Cisco Unified Communications Manager in the   cluster to use for autoregistration. appears. |
| Step 3 | In the Cisco Unified CM Configuration widow, configure the autoregistration parameters for the node in the Auto-registration Information section, then click Save . For more information on the fields and their configuration options, see the system Online Help. Select the universal device template to use for autoregistration from the drop-down list. If no universal device template is created for autoregistration, you can select Default Universal Device Template . Make sure that the selected template specifies the device pool that is to be used for autoregistration from User Management > User/Phone Add > Universal Device Template . Select the universal line template to use for autoregistration from the drop-down list. If no universal line template is created for autoregistration, you can select Default Universal Line Template .  Make sure that the selected template specifies the calling search space and the route partition that are to be used for
                                                   autoregistration from User Management > User/Phone Add > Universal Line Template . Enter the starting and ending directory numbers in to the Starting Directory Number and Ending Directory Number fields. Setting the starting and ending directory numbers to the same value disables autoregistration. Uncheck Auto-registration Disabled on this Cisco Unified Communications Manager to enable autoregistration for this node. Always enable or disable autoregistration on only the selected Unified Communications Manager node. If you switch the autoregistration function to another node in the cluster, you must reconfigure the Unified Communications Manager nodes, the Default Unified Communications Manager group, and the default device pools that you used. |
| Step 4 | Select System > Cisco Unified CM Group , then click Find in the Find and List Cisco Unified Communications Manager Groups window. |
| Step 5 | Select the Unified Communications Manager group to enable for autoregistration. In most cases, the name of this group is Default . You can choose a different Cisco Unified Communications Manager group. The group must have at least one node selected. |
| Step 6 | In the Cisco Unified CM Group Configuration window for that group, select Auto-registration Cisco Unified Communications Manager Group to enable autoregistration for  the group, then click Save . Tip Ensure that the Selected Cisco Unified Communications Managers list contains the node that you configured for autoregistration. Use the arrows to move the node to appear in the list. The Unified Communications Manager nodes get selected in the order in which they are listed. Save your changes. | Tip | Ensure that the Selected Cisco Unified Communications Managers list contains the node that you configured for autoregistration. Use the arrows to move the node to appear in the list. The Unified Communications Manager nodes get selected in the order in which they are listed. Save your changes. |
| Tip | Ensure that the Selected Cisco Unified Communications Managers list contains the node that you configured for autoregistration. Use the arrows to move the node to appear in the list. The Unified Communications Manager nodes get selected in the order in which they are listed. Save your changes. |
| Step 7 | Install the devices that you want to auto-register. |

| Tip | Ensure that the Selected Cisco Unified Communications Managers list contains the node that you configured for autoregistration. Use the arrows to move the node to appear in the list. The Unified Communications Manager nodes get selected in the order in which they are listed. Save your changes. |
|---|---|

| Note | You can proceed to reconfigure the auto-registered phones and assign them to their permanent device pools. The directory number
                                          that is  assigned to the phone does not change when you change the phone location. |
|---|---|

| Note | To register phones of a different type, change the device protocol type and install those devices before disabling autoregistration. |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Administration , select System > Cisco Unified CM , then click Find in the Find and List Cisco Unified CM window. |
|---|---|
| Step 2 | Select the Cisco Unified Communications Manager from   the list of nodes. |
| Step 3 | In the Cisco Unified CM Configuration widow for the selected node, check the Auto-registration Disabled on this Cisco Unified Communications Manager check box to disable autoregistration for this node, then click Save . Tip Setting the same value in the Starting Directory Number and Ending Directory Number fields also disables autoregistration. | Tip | Setting the same value in the Starting Directory Number and Ending Directory Number fields also disables autoregistration. |
| Tip | Setting the same value in the Starting Directory Number and Ending Directory Number fields also disables autoregistration. |

| Tip | Setting the same value in the Starting Directory Number and Ending Directory Number fields also disables autoregistration. |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Administration , select System > Cisco Unified Communications Manager |
|---|---|
| Step 2 | Select the Cisco Unified Communications Manager to reset for autoregistration. |
| Step 3 | Write down the current settings in the Starting Directory Number and Ending Directory Number fields. |
| Step 4 | Click Auto-registration Disabled on this Cisco Unified Communications Manager , then click Save . New phones cannot auto-register while autoregistration is disabled. |
| Step 5 | Set the Starting Directory Number and Ending Directory Number fields to their previous values, then click Save . Tip You could  set the fields  to new values. | Tip | You could  set the fields  to new values. |
| Tip | You could  set the fields  to new values. |

| Tip | You could  set the fields  to new values. |
|---|---|