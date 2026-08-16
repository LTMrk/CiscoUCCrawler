---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su3-cucm-b-feature-configuration-guide-for-cisco1251su3-cuc-dafd8c7de4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU3/cucm_b_feature-configuration-guide-for-cisco1251su3/cucm_b_feature-configuration-guide-for-cisco1251su3_chapter_0111011.html
retrieved_at: 2026-08-16T17:08:35.447956+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

Updated: July 31, 2025

Chapter: Configure Logical Partitioning

## Chapter: Configure Logical Partitioning

# Configure Logical Partitioning

## Logical Partitioning Overview

With logical partitioning, you can support PSTN and VoIP calls on a single system while meeting regulatory requirements for
                           call separation. For example, under regulatory constraints in India, all calls that are received from or sent to an external
                           phone must be handed off to and carried by a local or long-distance service provider over the full length of the connection,
                           with the applicable toll charges. You can create a single Unified Communications Manager cluster that routes calls appropriately
                           to the PSTN or the VoIP network according to the caller's location and the phone number being called.

logical partitioning defines which sets of VoIP devices are allowed to communicate with each other. Users do not have to remember
                           to use one line for PSTN and one line for VoIP. Phones making off-net calls are only allowed to talk to a PSTN gateway. It's
                           like having two networks to separately handle your VoIP and PSTN calls, but without the expense of dual infrastructure.

## Logical Partitioning Configuration Task Flow

Step 1

Enable Logical Partitioning

Enable Logical Partitioning.

Step 2

To Configure Geolocations , perform the following subtasks:

- Create Geolocations

- Assign Geolocations

- Set the Default Geolocation

Configuring geolocations is a two-step process: defining locations and assigning them to devices. You also can set the default
                                          location to be used by all devices in the cluster.

Step 3

Configure a Logical Partitioning Default Policy

Set up a default policy for devices that are not associated with a geolocation or geolocation filter. The policy allows
                                          or denies PSTN calls between these devices.

Step 4

Configure Devices to Avoid Logical Partitioning Checks

You can specifically exempt devices and device pools from the partitioning checks.

Step 5

To Configure Geolocation Filters , perform the following subtasks:

- Create Geolocation Filter Rules

- Assign Geolocation Filters

- Set the Default Geolocation Filter

Logical partitioning assigns a unique identifier to each device based on its location. When one device calls another, these
                                          identifiers are used to determine whether the call is allowed and what routing is appropriate. You can choose which fields
                                          are used to create this identifier. For example, you can apply different policies based on the room or floor within a building.

Step 6

Define a Set of Logical Partitioning Policy Records

Define a set of logical partitioning policies for allowing or denying calls between geolocations. Before calls between geolocations
                                          are allowed to proceed, the system checks to be sure that calls are allowed between the specified geolocations based on these
                                          policies.

Step 7

(Optional) Enable Location Conveyance

Configure location conveyance if you want to communicate geolocation information about devices across clusters.

### Enable Logical Partitioning

Step 1

From Cisco Unified CM Administration, choose System > Enterprise Parameters .

Step 2

For the Enable Logical Parititioning enterprise parameter,  choose True from the drop-down list.

Step 3

Click Save .

### Configure Geolocations

Configuring geolocations is a two-step process: defining locations and assigning them to devices. You also can set the default
                                 location to be used by all devices in the cluster.

Step 1

Create Geolocations

Configure geolocations to specify geographic locations. These are used to associate
                                             
                                             devices with regulatory features such as logical
                                             partitioning.
                                             Geolocations are used in policy decisions, such as in-country regulations.

Step 2

Assign Geolocations

Assign a geolocation to a device or device pool.

Step 3

Set the Default Geolocation

Specify a default geolocation for all devices and device pools in this cluster.

#### Create Geolocations

Step 1

From Cisco Unified CM Administration, choose System > Geolocation Configuration .

Step 2

Click Add New .

Step 3

Enter a Name for the geolocation.

Step 4

Configure the fields on the Geolocation Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 5

Click Save .

Step 6

Repeat this procedure to create additional geolocations.

#### Assign Geolocations

Assign a geolocation to a device or device pool.

Step 1

From Cisco Unified CM Administration, choose one of the following menu items:

- Device > Phone

- Device > Trunk

- Device > Gateway

- System > Device Pool

Step 2

Perform one of the following tasks:

- Click Find to modify the settings for an existing device or device pool. Enter search criteria, and then choose an existing device or
                                                device pool from the resulting list.

- Click Add New to add a new device or device pool. For devices, choose device types and protocols as needed and click Next .

Step 3

From the Geolocation drop-down list, choose a geolocation that you configured.

Step 4

Click Save .

#### Set the Default Geolocation

Specify a default geolocation for all devices and device pools in this cluster.

Step 1

From Cisco Unified CM Administration, choose System > Enterprise Parameters .

Step 2

From the Default Geolocation drop-down list, choose a Geolocation that you configured. The default value is Unspecified .

Step 3

Click Save .

Step 4

Click Apply Config .

Step 5

(Optional) If you need to override this default for a specific device or device pool, enter the value on either the Device Configuration or Device Pool Configuration window, and then click Save .

### Configure a
                           	 Logical Partitioning Default Policy

Set up a default policy for devices that are not associated with a geolocation or geolocation filter. The policy allows
                                 or denies PSTN calls between these devices.

Step 1

From Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > Logical Partitioning Policy
                                                				  Configuration

Step 2

Click Add
                                             				New .

Step 3

Configure the fields on the Logical Partition Policy Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 4

Click Save .

If a policy that contained the value Allow is then later changed
                                                         				  to Deny, then it remains Deny. The opposite is also true. A policy previously
                                                         				  set to Deny, later changed to Allow is an Allow. The Cisco Unified
                                                               						Reporting > Geolocation Policy
                                                               						Report can help you identify policies that overlap.

### Configure Devices to Avoid Logical Partitioning Checks

You can specifically exempt devices and device pools from the partitioning checks.

Step 1

From Cisco Unified CM Administration, choose one of the following menu items:

- Device > Phone

- Device > Trunk

- Device > Gateway

- System > Device Pool

Step 2

Perform one of the following tasks:

- Click Find to modify the settings for an existing device or device pool. Enter search criteria and then choose an existing device or
                                             device pool from the resulting list.

- Click Add New to add a new device or device pool. For devices, choose device types and protocols as needed and click Next .

Step 3

From the Geolocation drop-down list, choose Unspecified .

Step 4

Click Save .

### Configure Geolocation Filters

Logical partitioning assigns a unique identifier to each device based on its location. When one device calls another, these
                                 identifiers are used to determine whether the call is allowed and what routing is appropriate. You can choose which fields
                                 are used to create this identifier. For example, you can apply different policies based on the room or floor within a building.

Step 1

Create Geolocation Filter Rules

Geolocation filters allow you to specify which fields are used to create a geolocation identifier. This feature is used to
                                             make policy decisions on a subset of the geolocation objects.

Step 2

Assign Geolocation Filters

Step 3

Set the Default Geolocation Filter

Configure the Default Geolocation Filter enterprise parameter to specify a default geolocation filter for a cluster. This
                                             parameter determines the default
                                             geolocation filter setting for all devices and device pools that are not associated with a geolocation filter.

#### Create Geolocation Filter Rules

Step 1

From Cisco Unified CM Administration, choose System > Geolocation Filter .

Step 2

Click Add New .

Step 3

Enter a Name and Description for the filter.

Step 4

Check the check boxes that correspond to the items you want to use for logical partitioning decisions.

Step 5

Configure the fields on the Geolocation Filter Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 6

Click Save .

Step 7

Repeat these steps to create additional geolocation filters.

#### Assign Geolocation Filters

Step 1

From Cisco Unified CM Administration, choose one of the following menu items:

- Device > Phone

- Device > Trunk

- Device > Gateway

- System > Device Pool

Step 2

Perform one of the following tasks:

- Click Find to modify the settings for an existing device or device pool. Enter search criteria and then choose an existing device or
                                                device pool from the resulting list.

- Click Add New to add a new device or device pool. For devices, choose device types and protocols as needed and click Next .

Step 3

From the Geolocation Filter drop-down list, choose a geolocation filter that you configured.

Step 4

Click Save .

#### Set the Default Geolocation Filter

Step 1

From Cisco Unified CM Administration, choose System > Enterprise Parameters .

Step 2

From the Default Geolocation drop-down list, choose a Geolocation that you configured. The default value is Unspecified .

Step 3

Click Save .

Step 4

Click Apply Config .

Step 5

(Optional) If you need to override this default for a specific device or device pool, specify the default geolocation filter value on
                                             either the Device Configuration or Device Pool Configuration window, and then click Save .

### Define a Set of Logical Partitioning Policy Records

Define a set of logical partitioning policies for allowing or denying calls between geolocations. Before calls between geolocations
                                 are allowed to proceed, the system checks to be sure that calls are allowed between the specified geolocations based on these
                                 policies.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Logical Partitioning Policy Configuration .

Step 2

Perform one of the following tasks:

- Click Find to modify the settings for an existing logical partitioning policy. Enter search criteria and then choose an existing logical
                                             partitioning policy from the resulting list.

- Click Add New to add a new logical partitioning policy.

Step 3

Configure the fields on the Logical Partitioning Policy Configuration window. For more information on the fields and their configuration options, see the system Online Help.

If any policy is left blank without any configuration values, it will become a blank geolocation policy and configuring a
                                                         Logical Policy for a specific Device Type with the blank Logical Partitioning configurations makes Unified Communications Manager add the policy value (Allow or Deny) in the configured device type.

Step 4

Click Save .

### Enable Location Conveyance

Step 1

From Cisco Unified CM Administration, choose Device > Trunk .

Step 2

Do one of the following:

- Click Find and select an existing trunk.

- Click Add New to configure a new trunk.

Step 3

Complete the fields in the Trunk Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 4

In the Geolocation Information area, select a Geolocation and Geolocation Filter .

Step 5

To enable Location Conveyance, check the Send Geolocation Information check box.

Step 6

Click Save .

## Logical Partitioning Interactions

Feature

Interaction

Ad Hoc Conference, Join, Join Across Lines, Call Forwarding, Call Transfer

Logical partitioning handling does not take place in the
                                          following circumstances:

When all participants are VoIP phones.

When the geolocation or geolocation filter does not associate with a device.

Barge, cBarge, and Remote Resume

Logical partitioning handling does not take place in the following circumstances:

When both the caller and the callee devices are VoIP phones, logical partitioning policy checks are ignored.

For the participants in cBarge/Barge, no logical partitioning policy checking exists, and you cannot prevent logical-partitioning-denied
                                                scenarios.

Cisco Unified Mobility

Logical
                                          		  partitioning handling does not take place in the following circumstances:

Geolocation or
                                                				geolocation filter does not associate with the involved devices.

No logical
                                                				partitioning support exists when a dual-mode phone is used.

CTI Handling

Logical partitioning handling does not take place in the
                                          		  following circumstances:

When a geolocation or geolocation filter does not associate with
                                                				any device, handling does not occur.

When all the involved devices specify VoIP phones, handling does not occur.

Extension Mobility

Logical partitioning handling does not take place in the following circumstances:

A geolocation or geolocation filter does not associate with a VoIP phone that is logged on to Cisco Extension Mobility , nor does it associate with the calling party or called party device.

The VoIP phone that is logged on to Cisco Extension Mobility calls or receives a call from a VoIP phone.

Meet-Me Conference

Logical partitioning handling does not take place in the
                                          following circumstances:

When all participants are VoIP phones, handling does not occur.

When geolocation or geolocation filter does not associate with a device, no policy check takes place for that device.

Route Lists and Hunt Pilots

Logical partitioning handling does not take place in the following circumstances:

When both the calling party and called party devices are VoIP phones, handling does not occur.

All devices must associate with both a geolocation and geolocation filter. If any device does not associate with both geolocation
                                                and geolocation filter, handling does not occur.

Shared Line

Logical partitioning handling does not take place in the following circumstances:

When both the caller and the callee devices are VoIP phones, no handling occurs.

When geolocation or geolocation filter does not associate with any device, no handling occurs.

## Logical Partitioning Restrictions

Restriction

Description

Barge/cBarge

Barge/cBarge does not occur; the call instance is dropped.

For the participants in cBarge/Barge, no logical partitioning
                                          				policy checking exists, and you cannot prevent logical-partitioning-denied
                                          				scenarios.

BLF Presence

BLF Presence notifications are not checked for
                                          				a logical partitioning policy.

Cisco Extension Mobility

When Cisco Extension Mobility logs in to a phone in a different geolocation, outgoing PSTN calls can occur when Local Route Groups are
                                          				configured.
                                          			 Incoming PSTN calls are not placed to the phone but receive a
                                          				reorder tone.

Cisco Unified MeetingPlace

The system does not support the logical
                                          				partitioning feature for calls that involve Cisco Unified MeetingPlace or Cisco
                                          				Unified MeetingPlace Express.

Conferences

The logical partitioning checks are not supported for
                                          				participants across conferences in conference chaining.

For example, meet-me and adhoc chained conferences can have
                                          				participants that are logical partitioning denied.

H.225 gatekeeper-controlled trunk

Cisco Unified Communications Manager does not communicate geolocation
                                          				information over a H.225 gatekeeper-controlled trunk.

H.323 and MGCP Gateways

Cisco Unified Communications Manager does not communicate geolocation info
                                          				to H.323 or MGCP gateways.

Communication to a SIP gateway can be disabled through the SIP trunk
                                          				check box.

Mobility Cell Pickup

Logical partitioning deny handling takes
                                          				place after call is answered on the mobile phone.

The logical partitioning policy check does not occur before the
                                          				call is placed to the mobile phone (as it happens for a basic SNR call). The
                                          				system checks the logical partitioning policy after the mobile phone answers the call.

Q.SIG intercluster trunk

Intercluster trunks (ICT) with the Q.SIG protocol are not allowed to
                                          				communicate geolocation inforomation for the caller or receiving device. The ICT
                                          				configuration for "Send Geolocation Information" is disabled when the Q.SIG
                                          				tunneled protocol is selected.

Reorder Tones

No reorder tone (fast busy tone) is provided on IOS H.323 and SIP gateways upon
                                          				release of connected calls due to logical partitioning policies.

Shared Line Active Call

For a restricted logical partitioning scenario, the shared line
                                          				drops the active call information for the duration of the call, even if a feature moves the shared-line call to the allowed
                                          category.

User Agent Server

The logical partitioning policy checks in the logical
                                          				partitioning-aware cluster that receives this geolocation may cancel the call
                                          				if  the policy is denied.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Enable Logical Partitioning | Enable Logical Partitioning. |
| Step 2 | To Configure Geolocations , perform the following subtasks: Create Geolocations Assign Geolocations Set the Default Geolocation | Configuring geolocations is a two-step process: defining locations and assigning them to devices. You also can set the default
                                          location to be used by all devices in the cluster. |
| Step 3 | Configure a Logical Partitioning Default Policy | Set up a default policy for devices that are not associated with a geolocation or geolocation filter. The policy allows
                                          or denies PSTN calls between these devices. |
| Step 4 | Configure Devices to Avoid Logical Partitioning Checks | You can specifically exempt devices and device pools from the partitioning checks. |
| Step 5 | To Configure Geolocation Filters , perform the following subtasks: Create Geolocation Filter Rules Assign Geolocation Filters Set the Default Geolocation Filter | Logical partitioning assigns a unique identifier to each device based on its location. When one device calls another, these
                                          identifiers are used to determine whether the call is allowed and what routing is appropriate. You can choose which fields
                                          are used to create this identifier. For example, you can apply different policies based on the room or floor within a building. |
| Step 6 | Define a Set of Logical Partitioning Policy Records | Define a set of logical partitioning policies for allowing or denying calls between geolocations. Before calls between geolocations
                                          are allowed to proceed, the system checks to be sure that calls are allowed between the specified geolocations based on these
                                          policies. |
| Step 7 | (Optional) Enable Location Conveyance | (Optional) Configure location conveyance if you want to communicate geolocation information about devices across clusters. |

| Step 1 | From Cisco Unified CM Administration, choose System > Enterprise Parameters . |
|---|---|
| Step 2 | For the Enable Logical Parititioning enterprise parameter,  choose True from the drop-down list. |
| Step 3 | Click Save . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Create Geolocations | Configure geolocations to specify geographic locations. These are used to associate
                                             
                                             devices with regulatory features such as logical
                                             partitioning.
                                             Geolocations are used in policy decisions, such as in-country regulations. |
| Step 2 | Assign Geolocations | Assign a geolocation to a device or device pool. |
| Step 3 | Set the Default Geolocation | Specify a default geolocation for all devices and device pools in this cluster. |

| Step 1 | From Cisco Unified CM Administration, choose System > Geolocation Configuration . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Enter a Name for the geolocation. |
| Step 4 | Configure the fields on the Geolocation Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 5 | Click Save . |
| Step 6 | Repeat this procedure to create additional geolocations. |

| Step 1 | From Cisco Unified CM Administration, choose one of the following menu items: Device > Phone Device > Trunk Device > Gateway System > Device Pool |
|---|---|
| Step 2 | Perform one of the following tasks: Click Find to modify the settings for an existing device or device pool. Enter search criteria, and then choose an existing device or
                                                device pool from the resulting list. Click Add New to add a new device or device pool. For devices, choose device types and protocols as needed and click Next . |
| Step 3 | From the Geolocation drop-down list, choose a geolocation that you configured. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Enterprise Parameters . |
|---|---|
| Step 2 | From the Default Geolocation drop-down list, choose a Geolocation that you configured. The default value is Unspecified . |
| Step 3 | Click Save . |
| Step 4 | Click Apply Config . |
| Step 5 | (Optional) If you need to override this default for a specific device or device pool, enter the value on either the Device Configuration or Device Pool Configuration window, and then click Save . |

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > Logical Partitioning Policy
                                                				  Configuration |
|---|---|
| Step 2 | Click Add
                                             				New . |
| Step 3 | Configure the fields on the Logical Partition Policy Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 4 | Click Save . Note If a policy that contained the value Allow is then later changed
                                                         				  to Deny, then it remains Deny. The opposite is also true. A policy previously
                                                         				  set to Deny, later changed to Allow is an Allow. The Cisco Unified
                                                               						Reporting > Geolocation Policy
                                                               						Report can help you identify policies that overlap. | Note | If a policy that contained the value Allow is then later changed
                                                         				  to Deny, then it remains Deny. The opposite is also true. A policy previously
                                                         				  set to Deny, later changed to Allow is an Allow. The Cisco Unified
                                                               						Reporting > Geolocation Policy
                                                               						Report can help you identify policies that overlap. |
| Note | If a policy that contained the value Allow is then later changed
                                                         				  to Deny, then it remains Deny. The opposite is also true. A policy previously
                                                         				  set to Deny, later changed to Allow is an Allow. The Cisco Unified
                                                               						Reporting > Geolocation Policy
                                                               						Report can help you identify policies that overlap. |

| Note | If a policy that contained the value Allow is then later changed
                                                         				  to Deny, then it remains Deny. The opposite is also true. A policy previously
                                                         				  set to Deny, later changed to Allow is an Allow. The Cisco Unified
                                                               						Reporting > Geolocation Policy
                                                               						Report can help you identify policies that overlap. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose one of the following menu items: Device > Phone Device > Trunk Device > Gateway System > Device Pool |
|---|---|
| Step 2 | Perform one of the following tasks: Click Find to modify the settings for an existing device or device pool. Enter search criteria and then choose an existing device or
                                             device pool from the resulting list. Click Add New to add a new device or device pool. For devices, choose device types and protocols as needed and click Next . |
| Step 3 | From the Geolocation drop-down list, choose Unspecified . |
| Step 4 | Click Save . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Create Geolocation Filter Rules | Geolocation filters allow you to specify which fields are used to create a geolocation identifier. This feature is used to
                                             make policy decisions on a subset of the geolocation objects. |
| Step 2 | Assign Geolocation Filters |  |
| Step 3 | Set the Default Geolocation Filter | Configure the Default Geolocation Filter enterprise parameter to specify a default geolocation filter for a cluster. This
                                             parameter determines the default
                                             geolocation filter setting for all devices and device pools that are not associated with a geolocation filter. |

| Step 1 | From Cisco Unified CM Administration, choose System > Geolocation Filter . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Enter a Name and Description for the filter. |
| Step 4 | Check the check boxes that correspond to the items you want to use for logical partitioning decisions. |
| Step 5 | Configure the fields on the Geolocation Filter Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 6 | Click Save . |
| Step 7 | Repeat these steps to create additional geolocation filters. |

| Step 1 | From Cisco Unified CM Administration, choose one of the following menu items: Device > Phone Device > Trunk Device > Gateway System > Device Pool |
|---|---|
| Step 2 | Perform one of the following tasks: Click Find to modify the settings for an existing device or device pool. Enter search criteria and then choose an existing device or
                                                device pool from the resulting list. Click Add New to add a new device or device pool. For devices, choose device types and protocols as needed and click Next . |
| Step 3 | From the Geolocation Filter drop-down list, choose a geolocation filter that you configured. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Enterprise Parameters . |
|---|---|
| Step 2 | From the Default Geolocation drop-down list, choose a Geolocation that you configured. The default value is Unspecified . |
| Step 3 | Click Save . |
| Step 4 | Click Apply Config . |
| Step 5 | (Optional) If you need to override this default for a specific device or device pool, specify the default geolocation filter value on
                                             either the Device Configuration or Device Pool Configuration window, and then click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Logical Partitioning Policy Configuration . |
|---|---|
| Step 2 | Perform one of the following tasks: Click Find to modify the settings for an existing logical partitioning policy. Enter search criteria and then choose an existing logical
                                             partitioning policy from the resulting list. Click Add New to add a new logical partitioning policy. |
| Step 3 | Configure the fields on the Logical Partitioning Policy Configuration window. For more information on the fields and their configuration options, see the system Online Help. Note If any policy is left blank without any configuration values, it will become a blank geolocation policy and configuring a
                                                         Logical Policy for a specific Device Type with the blank Logical Partitioning configurations makes Unified Communications Manager add the policy value (Allow or Deny) in the configured device type. | Note | If any policy is left blank without any configuration values, it will become a blank geolocation policy and configuring a
                                                         Logical Policy for a specific Device Type with the blank Logical Partitioning configurations makes Unified Communications Manager add the policy value (Allow or Deny) in the configured device type. |
| Note | If any policy is left blank without any configuration values, it will become a blank geolocation policy and configuring a
                                                         Logical Policy for a specific Device Type with the blank Logical Partitioning configurations makes Unified Communications Manager add the policy value (Allow or Deny) in the configured device type. |
| Step 4 | Click Save . |

| Note | If any policy is left blank without any configuration values, it will become a blank geolocation policy and configuring a
                                                         Logical Policy for a specific Device Type with the blank Logical Partitioning configurations makes Unified Communications Manager add the policy value (Allow or Deny) in the configured device type. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Trunk . |
|---|---|
| Step 2 | Do one of the following: Click Find and select an existing trunk. Click Add New to configure a new trunk. |
| Step 3 | Complete the fields in the Trunk Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 4 | In the Geolocation Information area, select a Geolocation and Geolocation Filter . |
| Step 5 | To enable Location Conveyance, check the Send Geolocation Information check box. |
| Step 6 | Click Save . |

| Feature | Interaction |
|---|---|
| Ad Hoc Conference, Join, Join Across Lines, Call Forwarding, Call Transfer | Logical partitioning handling does not take place in the
                                          following circumstances: When all participants are VoIP phones. When the geolocation or geolocation filter does not associate with a device. |
| Barge, cBarge, and Remote Resume | Logical partitioning handling does not take place in the following circumstances: When both the caller and the callee devices are VoIP phones, logical partitioning policy checks are ignored. For the participants in cBarge/Barge, no logical partitioning policy checking exists, and you cannot prevent logical-partitioning-denied
                                                scenarios. |
| Cisco Unified Mobility | Logical
                                          		  partitioning handling does not take place in the following circumstances: Geolocation or
                                                				geolocation filter does not associate with the involved devices. No logical
                                                				partitioning support exists when a dual-mode phone is used. |
| CTI Handling | Logical partitioning handling does not take place in the
                                          		  following circumstances: When a geolocation or geolocation filter does not associate with
                                                				any device, handling does not occur. When all the involved devices specify VoIP phones, handling does not occur. |
| Extension Mobility | Logical partitioning handling does not take place in the following circumstances: A geolocation or geolocation filter does not associate with a VoIP phone that is logged on to Cisco Extension Mobility , nor does it associate with the calling party or called party device. The VoIP phone that is logged on to Cisco Extension Mobility calls or receives a call from a VoIP phone. |
| Meet-Me Conference | Logical partitioning handling does not take place in the
                                          following circumstances: When all participants are VoIP phones, handling does not occur. When geolocation or geolocation filter does not associate with a device, no policy check takes place for that device. |
| Route Lists and Hunt Pilots | Logical partitioning handling does not take place in the following circumstances: When both the calling party and called party devices are VoIP phones, handling does not occur. All devices must associate with both a geolocation and geolocation filter. If any device does not associate with both geolocation
                                                and geolocation filter, handling does not occur. |
| Shared Line | Logical partitioning handling does not take place in the following circumstances: When both the caller and the callee devices are VoIP phones, no handling occurs. When geolocation or geolocation filter does not associate with any device, no handling occurs. |

| Restriction | Description |
|---|---|
| Barge/cBarge | Barge/cBarge does not occur; the call instance is dropped. For the participants in cBarge/Barge, no logical partitioning
                                          				policy checking exists, and you cannot prevent logical-partitioning-denied
                                          				scenarios. |
| BLF Presence | BLF Presence notifications are not checked for
                                          				a logical partitioning policy. |
| Cisco Extension Mobility | When Cisco Extension Mobility logs in to a phone in a different geolocation, outgoing PSTN calls can occur when Local Route Groups are
                                          				configured.
                                          			 Incoming PSTN calls are not placed to the phone but receive a
                                          				reorder tone. |
| Cisco Unified MeetingPlace | The system does not support the logical
                                          				partitioning feature for calls that involve Cisco Unified MeetingPlace or Cisco
                                          				Unified MeetingPlace Express. |
| Conferences | The logical partitioning checks are not supported for
                                          				participants across conferences in conference chaining. For example, meet-me and adhoc chained conferences can have
                                          				participants that are logical partitioning denied. |
| H.225 gatekeeper-controlled trunk | Cisco Unified Communications Manager does not communicate geolocation
                                          				information over a H.225 gatekeeper-controlled trunk. |
| H.323 and MGCP Gateways | Cisco Unified Communications Manager does not communicate geolocation info
                                          				to H.323 or MGCP gateways. Communication to a SIP gateway can be disabled through the SIP trunk
                                          				check box. |
| Mobility Cell Pickup | Logical partitioning deny handling takes
                                          				place after call is answered on the mobile phone. The logical partitioning policy check does not occur before the
                                          				call is placed to the mobile phone (as it happens for a basic SNR call). The
                                          				system checks the logical partitioning policy after the mobile phone answers the call. |
| Q.SIG intercluster trunk | Intercluster trunks (ICT) with the Q.SIG protocol are not allowed to
                                          				communicate geolocation inforomation for the caller or receiving device. The ICT
                                          				configuration for "Send Geolocation Information" is disabled when the Q.SIG
                                          				tunneled protocol is selected. |
| Reorder Tones | No reorder tone (fast busy tone) is provided on IOS H.323 and SIP gateways upon
                                          				release of connected calls due to logical partitioning policies. |
| Shared Line Active Call | For a restricted logical partitioning scenario, the shared line
                                          				drops the active call information for the duration of the call, even if a feature moves the shared-line call to the allowed
                                          category. |
| User Agent Server | The logical partitioning policy checks in the logical
                                          				partitioning-aware cluster that receives this geolocation may cancel the call
                                          				if  the policy is denied. |