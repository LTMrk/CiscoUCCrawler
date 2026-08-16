---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-cucm-b-feature-configuration-guide-for-15-cucm-m-configure-device-327fb14221
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/cucm_b_feature-configuration-guide-for-15/cucm_m_configure-device-mobility-1251.html
retrieved_at: 2026-08-16T16:02:38.137391+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: March 26, 2026

Chapter: Device Mobility

## Chapter: Device Mobility

# Device Mobility

## Device Mobility Overview

Device mobility lets mobile users roam between sites, taking on the site-specific settings of the local site. When this feature
                              is configured, Cisco Unified Communications Manager matches the IP address of a roaming device to IP subnets in the Device Mobility configuration to determine the physical location
                              of the device so that an appropriate device pool can be assigned. The settings from this dynamically-assigned device pool
                              override the settings in the Phone Configuration for that device and ensure that voice quality and allocation of resources
                              are appropriate for the new phone location.

For roaming mobile devices, this feature provides a more efficient use of network resources:

When a mobile user moves to another location, call admission control (CAC) can ensure video and audio quality with the appropriate
                                    bandwidth allocations for that location.

When a mobile user makes a PSTN call, the phone is routed to the local gateway. Otherwise, PSTN calls would first be routed
                                    back to the home site over IP WAN connections, and then on to a PSTN gateway at the home site.

When a mobile user calls the home location, Cisco Unified Communications Manager can assign the appropriate codec for the region.

### Site-Specific Settings

For roaming devices, Cisco Unified Communications Manager overwrites the following device pool parameters from the device configuration with values from the dynamically assigned device
                              pool:

Date/Time Group

Region

Location

Network Locale

SRST Reference

Connection Monitor Duration

Physical Location

Device Mobility Group

Media Resource Group List

When networks span geographic locations outside the United States, you can configure device mobility groups to allow phone
                              users to use their configured dial plan no matter where they roam. When a device is roaming but remains in the same device
                              mobility group, Cisco Unified Communications Manager also overwrites the following device pool parameters:

AAR Group

AAR Calling Search Space

Device Calling Search Space

When the phone returns to its home location, the system disassociates the roaming device pool, downloads the configuration
                              settings for home location, and resets the device. The device registers with the home location configuration settings.

### Configuration

This feature needs to be enabled at both the system-level, and at the device level. At the system level, this feature uses
                              the following components:

Physical Location—The physical location of the device pool. During registration, the system matches the device registration
                                    location to a subnet in the Device Mobility Info in order to assign an appropriate device pool.

Device Pool—Location-specific device settings such as media resources, regions, and SRST references. For roaming devices,
                                    the system assigns the device pool that matches that device’s physical location.

Device Mobility Group—A logical group of sites with similar dialing patterns. For example, an enterprise with a worldwide
                                    network might set up groups that represent individual countries. The device mobility group setting determines whether the
                                    device is moved within the same geographical entity, primarily to allow users to keep their own dial plans.

Device Mobility Info—This info contains the subnets that the system provides for roaming devices, and the device pools that
                                    the system can assign to roaming devices that register to one of those subnets.

At the device level, the feature must be turned on for devices to use this feature.

### Device Pool Assignment

This section describes how Unified Communications Manager assigns device pools when device mobility is enabled. Depending on whether the device is roaming, the device may be assigned
                                 a device pool in the local site, or it may use the device pool from its home site.

Following initialization, the device mobility feature operates according to the following process:

A phone device record gets created for an IP phone that is provisioned to be mobile, and the phone gets assigned to a device
                                       pool. The phone registers with Unified Communications Manager , and an IP address gets assigned as part of the registration process.

Unified Communications Manager compares the IP address of the device to the subnets that are configured for device mobility in the Device Mobility Info
                                       Configuration window. The best match uses the largest number of bits in the IP subnet mask (longest match rule). For example,
                                       the IP address 9.9.8.2 matches the subnet 9.9.8.0/24 rather than the subnet 9.9.0.0/16.

If the device pool in the phone record matches the device pool in the matching subnet, the system considers the phone to be
                                       in its home location, and the phone retains the parameters of its home device pool.

If the device pool in the phone record does not match the device pools in the matching subnet, the system considers the phone
                                       to be roaming. The following table describes possible scenarios for device mobility and the system responses.

Scenario

System Response

The physical location setting in the phone device pool matches the physical location setting in a device pool that is associated
                                                   with the matching subnet.

Although the phone may have moved from one subnet to another, the physical location and associated services have not changed.

The system does not consider the phone to be roaming, and the system uses the settings in the home location device pool.

The matching subnet has a single device pool that is assigned to it; the subnet device pool differs from the home location
                                                   device pool, and the physical locations differ.

The system considers the phone to be roaming. It reregisters with the parameters of the device pool for the matching subnet.

The physical locations differ, and the matching subnet has multiple device pools assigned to it.

The system considers the phone to be roaming. The new device pool gets assigned according to a round-robin rule. Each time
                                                   that a roaming device comes in to be registered for the subnet, the next device pool in the set of available device pools
                                                   gets assigned.

Physical location gets defined for the home device pool but is not defined for the device pools that are associated with the
                                                   matching subnet.

The physical location has not changed, so the phone remains registered in the home device pool.

Physical location that is not defined for the home device pool gets defined for the device pools that are associated with
                                                   the matching subnet.

The system considers the phone to be roaming to the defined physical location, and it registers with the parameters of the
                                                   device pool for the matching subnet.

A subnet gets updated or removed.

The rules for roaming and assigning device pools get applied by using the remaining subnets.

### Device Mobility Groups Operations Summary

You can use device mobility groups to determine when a device moves to another location within a geographic entity, so a user
                                 can use its own dial plan. For example, you can configure a device mobility group for the United States and another group
                                 for the United Kingdom. If a phone moves into a different mobility group (such as from the United States to the United Kingdom), Unified Communications Manager uses the Calling Search Space, AAR Group and AAR CSS from the phone record, and not from the roaming location.

If the device moves to another location with same mobility group (for example, Richardson, USA, to Boulder, USA), the CSS
                                 information gets taken from the roaming device pool settings. With this approach, if the user is dialing PSTN destinations,
                                 the user reaches the local gateway.

The following table describes the device pool parameters
                                 		  that the system uses for various scenarios.

Scenario

Parameters Used

A roaming device moves to another location in the same device
                                             					 mobility group.

Roaming Device Pool: yes

Location: Roaming device pool setting

Region: Roaming device pool setting

Media Resources Group List: Roaming device pool setting

Device CSS: Roaming device pool setting (Device Mobility CSS)

AAR Group: Roaming device pool setting

AAR CSS: Roaming device pool setting

A roaming device moves to another location in a different
                                             					 device mobility group.

Roaming Device Pool: yes

Location: Roaming device pool setting

Region: Roaming device pool setting

Media Resources Group List: Roaming device pool setting

Device CSS: Home location settings

AAR Group: Home location settings

AAR CSS: Home location settings

A device roams, and a device mobility group does not get
                                             					 defined for the home or roaming device pool.

Because the device is roaming, it takes the roaming device
                                             					 pool settings, including the Device Mobility Calling Search Space, AAR Calling
                                             					 Search Space, and AAR Group.

## Device Mobility Prerequisites

The phone must have a dynamic IP address to use device mobility. If a phone with a static IP address roams, Unified Communications Manager uses the configuration settings from its home location.

The Device Mobility feature requires you to set up device pools with site-specific settings. This chapter describes only the
                                    device pool settings that relate to device mobility. For more detailed information on configuring device pools, see the " Configure Device Pools " chapter in the System Configuration Guide for Cisco Unified Communications Manager .

Cisco Database Layer Monitor service must be running on the same node as the Cisco CallManager service.

Cisco TFTP service must be running on at least one node in the cluster.

Cisco Unified Communications Manager Locale Installer (if you want to use non-English phone locales or country-specific tones).

Any phone that runs either SCCP or SIP.

## Device Mobility Configuration Task Flow

Step 1

Enable device mobility at the device level by completing either of these tasks:

- Enable Device Mobility Clusterwide

- Enable Device Mobility for Individual Devices

Enables device support through a clusterwide service parameter, or within the Phone Configuration window of an individual device.

Step 2

Configure a Physical Location

Set up the physical locations that you will assign to your device pools.

Step 3

Configure a Device Mobility Group

A device mobility group is a logical grouping of sites with similar dialing patterns.

Step 4

Configure a Device Pool for Device Mobility

Assign the physical location, device mobility group, and other device mobility-related information to device pools that will
                                          be used for device mobility.

Step 5

Configure Device Mobility Information

Assign the IP subnets where roaming devices can register and the device pools that can be assigned to those roaming devices.

### Enable Device Mobility Clusterwide

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, choose the node that is running the Cisco CallManager service.

Step 3

From the Service drop-down list, choose Cisco CallManager Service .

Step 4

Under Clusterwide Parameters (Device - Phone) , set the Device Mobility Mode service parameter to On .

Step 5

Click Save .

For devices that are already registered, you must restart the Cisco CallManager service for this new setting to be enabled.

#### What to do next

If you want to configure device mobility settings for an individual device, go to Enable Device Mobility for Individual Devices .

Otherwise, you can begin configuring the system for device mobility. Go to Configure a Physical Location .

### Enable Device Mobility for Individual Devices

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find and select the device that you want to configure.

Step 3

From the Device Mobility Mode drop-down list, choose one of the following:

- On —Device mobility is enabled for this device.

- Off —Device mobility is disabled for this device.

- Default —The device uses the setting of the Device Mobility Mode clusterwide service parameter. This is the default setting.

Step 4

Click Save .

### Configure a Physical Location

Step 1

From Cisco Unified CM Administration, choose System > Physical Location .

Step 2

Click Add New .

Step 3

Enter a Name for the location.

Step 4

Enter a Description for the location.

Step 5

Click Save .

### Configure a Device Mobility Group

Step 1

From Cisco Unified CM Administration, choose System > Device Mobility > Device Mobility Group .

Step 2

Click Add New .

Step 3

Enter a Name for the device mobility group.

Step 4

Enter a Description for the device mobility group.

Step 5

Click Save .

### Configure a Device
                           	 Pool for Device Mobility

Step 1

From Cisco Unified CM Administration, choose System > Device Pool .

Step 2

Do either of the following:

- Click Find and select an existing device pool.

- Click Add New to create a new device pool.

Step 3

Under Roaming Sensitive Settings , assign the parameters that you set up in the previous device mobility tasks:

- Physical Location —From the drop-down list, select the physical location that you set up for this device pool. Device mobility uses this location
                                             to assign a device pool for a roaming device.

- Device Mobility Group —From the drop-down list, select the device mobility group that you set up for this device pool.

Step 4

Under Device Mobility Related Information , configure the following device mobility-related fields. For more information on the fields and their configuration options, see Online Help.

- Device Mobility Calling Search Space —Select the CSS to be used by a roaming device that uses this device pool.

- AAR Calling Search Space —Select the calling search space for the device to use when automated alternate routing (AAR) is performed.

- AAR Group —If AAR is configured, select the AAR Group for this device.

- Calling Party Transformation CSS —Select the calling party transformation CSS for roaming devices that use this device pool.

The Calling Party Transformation CSS overrides the device level configuration for roaming devices, even if the Use Device Pool Calling Party Transformation CSS check box is unchecked in the Phone Configuration window.

The Called Party Transformation CSS setting is applied to the gateway rather than to the roaming device.

Step 5

Configure any remaining fields in the Device Pool Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 6

Click Save .

### Configure Device Mobility Information

Step 1

From Cisco Unified CM Administration, choose System > Device Mobility > Device Mobility Info .

Step 2

Click Add New .

Step 3

Enter a Name for the Device Mobibility Info.

Step 4

Enter the IP subnet details for roaming device registrations.

- If you are using IPv4 addresses for your mobile devices, complete the IPv4 subnet details.

- If you are using IPv6 addresses for your mobile devices, complete the IPv6 subnet details.

Step 5

Select the device pools that you want the system to assign for roaming devices that register to one of these subnets. Use
                                          the arrows to move the appropriate device pools from the Selected Device Pools list box to the Available Device Pools s list box.

Step 6

Click Save .

### View Roaming Device Pool Parameters

Use the following procedure to view and verify the current device mobility settings for a device.

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Enter search criteria and click Find to find the device with device mobility mode enabled.

Step 3

Click View Current Device Mobility Settings next to the Device Mobility Mode field.

The  roaming device pool settings appear. If the device is not roaming, the home location settings appear.

## Device Mobility Interactions

Feature

Interaction

Calling Party Normalization

Calling party normalization enhances the dialing
                                          		  capabilities of some phones and improves call-back functionality when a call is
                                          		  routed to multiple geographical locations; that is, the feature ensures that
                                          		  the called party can return a call without the need to modify the directory
                                          		  number in the call log directories on the phone. Additionally, calling party
                                          		  normalization allows you to globalize and localize phone numbers, so the
                                          		  appropriate calling number presentation is displayed on the phone.

Roaming

When a device is roaming in the same device mobility group, Unified Communications Manager uses the device mobility CSS to reach the local gateway. If a user sets call forward all (CFA) at the phone, the CFA CSS
                                          is set to None, and the CFA CSS activation policy is set to With Activating Device/Line CSS, then the following behaviors
                                          will occur, depending on the device location:

The Device CSS and Line CSS are used as the CFA CSS when the
                                                				device is in its home location.

If the device is roaming within the same device mobility group,
                                                				the device mobility CSS from the roaming device pool and the line CSS are used
                                                				as the CFA CSS.

If the device is roaming within a different device mobility group,
                                                				the Device CSS and Line CSS are used as the CFA CSS.

## Device Mobility
                        	 Restrictions

Restriction

Description

IP Address

The device mobility feature depends on the IPv4 address or IPv6 address of the device that registers with Unified Communications Manager .

The
                                                						  phone must have a dynamic IPv4 address or IPv6 address to use the device mobility.

If the
                                                						  device is assigned an IP address by using network address translation (NAT) or
                                                						  port address translation (PAT), the IP address that is provided during
                                                						  registration may not match the actual IP address of the device.

If the Cisco IP phone supports IPv4-Only Stack or
                                                						  IPv6-Only Stack, then the phone gets re-associated either with IPv4 or IPv6
                                                						  Device Mobility Information, based on the IP addressing mode preference
                                                						  defined. For example, when a phone is defined with IPv6 preference but has no
                                                						  matching Device Mobility Information (IPv6 subnet and mask size), then it is
                                                						  associated with IPv4. When you add matching IPv6 Device Mobility Information,
                                                						  then the phone gets re-associated with IPv6 Device Mobility Information.

| Note | Cisco Unified Communications Manager always uses the Communications Manager Group setting from the phone record. The device always registers to its home location Cisco Unified Communications Manager server even when roaming. When a phone is roaming, only network location settings such as bandwidth allocation, media resource
                                       allocation, region configuration, and AAR group get changed. |
|---|---|

| Scenario | System Response |
|---|---|
| The physical location setting in the phone device pool matches the physical location setting in a device pool that is associated
                                                   with the matching subnet. Note Although the phone may have moved from one subnet to another, the physical location and associated services have not changed. | Note | Although the phone may have moved from one subnet to another, the physical location and associated services have not changed. | The system does not consider the phone to be roaming, and the system uses the settings in the home location device pool. |
| Note | Although the phone may have moved from one subnet to another, the physical location and associated services have not changed. |
| The matching subnet has a single device pool that is assigned to it; the subnet device pool differs from the home location
                                                   device pool, and the physical locations differ. | The system considers the phone to be roaming. It reregisters with the parameters of the device pool for the matching subnet. |
| The physical locations differ, and the matching subnet has multiple device pools assigned to it. | The system considers the phone to be roaming. The new device pool gets assigned according to a round-robin rule. Each time
                                                   that a roaming device comes in to be registered for the subnet, the next device pool in the set of available device pools
                                                   gets assigned. |
| Physical location gets defined for the home device pool but is not defined for the device pools that are associated with the
                                                   matching subnet. | The physical location has not changed, so the phone remains registered in the home device pool. |
| Physical location that is not defined for the home device pool gets defined for the device pools that are associated with
                                                   the matching subnet. | The system considers the phone to be roaming to the defined physical location, and it registers with the parameters of the
                                                   device pool for the matching subnet. |
| A subnet gets updated or removed. | The rules for roaming and assigning device pools get applied by using the remaining subnets. |

| Note | Although the phone may have moved from one subnet to another, the physical location and associated services have not changed. |
|---|---|

| Note | If no device mobility information entries match the device IP address, the device uses the home location device pool settings. |
|---|---|

| Scenario | Parameters Used |
|---|---|
| A roaming device moves to another location in the same device
                                             					 mobility group. | Roaming Device Pool: yes Location: Roaming device pool setting Region: Roaming device pool setting Media Resources Group List: Roaming device pool setting Device CSS: Roaming device pool setting (Device Mobility CSS) AAR Group: Roaming device pool setting AAR CSS: Roaming device pool setting |
| A roaming device moves to another location in a different
                                             					 device mobility group. | Roaming Device Pool: yes Location: Roaming device pool setting Region: Roaming device pool setting Media Resources Group List: Roaming device pool setting Device CSS: Home location settings AAR Group: Home location settings AAR CSS: Home location settings |
| A device roams, and a device mobility group does not get
                                             					 defined for the home or roaming device pool. | Because the device is roaming, it takes the roaming device
                                             					 pool settings, including the Device Mobility Calling Search Space, AAR Calling
                                             					 Search Space, and AAR Group. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Enable device mobility at the device level by completing either of these tasks: Enable Device Mobility Clusterwide Enable Device Mobility for Individual Devices | Enables device support through a clusterwide service parameter, or within the Phone Configuration window of an individual device. |
| Step 2 | Configure a Physical Location | Set up the physical locations that you will assign to your device pools. |
| Step 3 | Configure a Device Mobility Group | A device mobility group is a logical grouping of sites with similar dialing patterns. |
| Step 4 | Configure a Device Pool for Device Mobility | Assign the physical location, device mobility group, and other device mobility-related information to device pools that will
                                          be used for device mobility. |
| Step 5 | Configure Device Mobility Information | Assign the IP subnets where roaming devices can register and the device pools that can be assigned to those roaming devices. |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose the node that is running the Cisco CallManager service. |
| Step 3 | From the Service drop-down list, choose Cisco CallManager Service . |
| Step 4 | Under Clusterwide Parameters (Device - Phone) , set the Device Mobility Mode service parameter to On . |
| Step 5 | Click Save . For devices that are already registered, you must restart the Cisco CallManager service for this new setting to be enabled. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find and select the device that you want to configure. |
| Step 3 | From the Device Mobility Mode drop-down list, choose one of the following: On —Device mobility is enabled for this device. Off —Device mobility is disabled for this device. Default —The device uses the setting of the Device Mobility Mode clusterwide service parameter. This is the default setting. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Physical Location . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Enter a Name for the location. |
| Step 4 | Enter a Description for the location. |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Device Mobility > Device Mobility Group . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Enter a Name for the device mobility group. |
| Step 4 | Enter a Description for the device mobility group. |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Device Pool . |
|---|---|
| Step 2 | Do either of the following: Click Find and select an existing device pool. Click Add New to create a new device pool. |
| Step 3 | Under Roaming Sensitive Settings , assign the parameters that you set up in the previous device mobility tasks: Physical Location —From the drop-down list, select the physical location that you set up for this device pool. Device mobility uses this location
                                             to assign a device pool for a roaming device. Device Mobility Group —From the drop-down list, select the device mobility group that you set up for this device pool. |
| Step 4 | Under Device Mobility Related Information , configure the following device mobility-related fields. For more information on the fields and their configuration options, see Online Help. Device Mobility Calling Search Space —Select the CSS to be used by a roaming device that uses this device pool. AAR Calling Search Space —Select the calling search space for the device to use when automated alternate routing (AAR) is performed. AAR Group —If AAR is configured, select the AAR Group for this device. Calling Party Transformation CSS —Select the calling party transformation CSS for roaming devices that use this device pool. Note The Calling Party Transformation CSS overrides the device level configuration for roaming devices, even if the Use Device Pool Calling Party Transformation CSS check box is unchecked in the Phone Configuration window. The Called Party Transformation CSS setting is applied to the gateway rather than to the roaming device. | Note | The Calling Party Transformation CSS overrides the device level configuration for roaming devices, even if the Use Device Pool Calling Party Transformation CSS check box is unchecked in the Phone Configuration window. The Called Party Transformation CSS setting is applied to the gateway rather than to the roaming device. |
| Note | The Calling Party Transformation CSS overrides the device level configuration for roaming devices, even if the Use Device Pool Calling Party Transformation CSS check box is unchecked in the Phone Configuration window. The Called Party Transformation CSS setting is applied to the gateway rather than to the roaming device. |
| Step 5 | Configure any remaining fields in the Device Pool Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 6 | Click Save . |

| Note | The Calling Party Transformation CSS overrides the device level configuration for roaming devices, even if the Use Device Pool Calling Party Transformation CSS check box is unchecked in the Phone Configuration window. The Called Party Transformation CSS setting is applied to the gateway rather than to the roaming device. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Device Mobility > Device Mobility Info . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Enter a Name for the Device Mobibility Info. |
| Step 4 | Enter the IP subnet details for roaming device registrations. If you are using IPv4 addresses for your mobile devices, complete the IPv4 subnet details. If you are using IPv6 addresses for your mobile devices, complete the IPv6 subnet details. |
| Step 5 | Select the device pools that you want the system to assign for roaming devices that register to one of these subnets. Use
                                          the arrows to move the appropriate device pools from the Selected Device Pools list box to the Available Device Pools s list box. |
| Step 6 | Click Save . For more information on the fields and their configuration options, see Online Help. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Enter search criteria and click Find to find the device with device mobility mode enabled. |
| Step 3 | Click View Current Device Mobility Settings next to the Device Mobility Mode field. The  roaming device pool settings appear. If the device is not roaming, the home location settings appear. |

| Feature | Interaction |
|---|---|
| Calling Party Normalization | Calling party normalization enhances the dialing
                                          		  capabilities of some phones and improves call-back functionality when a call is
                                          		  routed to multiple geographical locations; that is, the feature ensures that
                                          		  the called party can return a call without the need to modify the directory
                                          		  number in the call log directories on the phone. Additionally, calling party
                                          		  normalization allows you to globalize and localize phone numbers, so the
                                          		  appropriate calling number presentation is displayed on the phone. |
| Roaming | When a device is roaming in the same device mobility group, Unified Communications Manager uses the device mobility CSS to reach the local gateway. If a user sets call forward all (CFA) at the phone, the CFA CSS
                                          is set to None, and the CFA CSS activation policy is set to With Activating Device/Line CSS, then the following behaviors
                                          will occur, depending on the device location: The Device CSS and Line CSS are used as the CFA CSS when the
                                                				device is in its home location. If the device is roaming within the same device mobility group,
                                                				the device mobility CSS from the roaming device pool and the line CSS are used
                                                				as the CFA CSS. If the device is roaming within a different device mobility group,
                                                				the Device CSS and Line CSS are used as the CFA CSS. |

| Restriction | Description |
|---|---|
| IP Address | The device mobility feature depends on the IPv4 address or IPv6 address of the device that registers with Unified Communications Manager . The
                                                						  phone must have a dynamic IPv4 address or IPv6 address to use the device mobility. If the
                                                						  device is assigned an IP address by using network address translation (NAT) or
                                                						  port address translation (PAT), the IP address that is provided during
                                                						  registration may not match the actual IP address of the device. If the Cisco IP phone supports IPv4-Only Stack or
                                                						  IPv6-Only Stack, then the phone gets re-associated either with IPv4 or IPv6
                                                						  Device Mobility Information, based on the IP addressing mode preference
                                                						  defined. For example, when a phone is defined with IPv6 preference but has no
                                                						  matching Device Mobility Information (IPv6 subnet and mask size), then it is
                                                						  associated with IPv4. When you add matching IPv6 Device Mobility Information,
                                                						  then the phone gets re-associated with IPv6 Device Mobility Information. |