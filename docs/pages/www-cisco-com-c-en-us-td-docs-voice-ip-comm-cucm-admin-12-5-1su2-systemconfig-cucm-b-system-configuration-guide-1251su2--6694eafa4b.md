---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su2-systemconfig-cucm-b-system-configuration-guide-1251su2--6694eafa4b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU2/systemConfig/cucm_b_system-configuration-guide-1251su2/cucm_b_system-configuration-guide-for-cisco-1251su2_chapter_010000.html
retrieved_at: 2026-08-16T17:44:24.750462+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: July 31, 2025

Chapter: Configure Partitions

## Chapter: Configure Partitions

# Configure Partitions

## Partitions
                        	 Overview

Partitions are logical groups of any of the following:

Route patterns

Directory numbers (DNs)

Translation patterns

Transformation patterns

Universal resource indicators (URIs)

Hunt pilots

Partitions facilitate call routing by dividing the route plan into logical subsets that are based on similar accessibility
                              requirements, organization, location, and call type.

## Calling Search Space Overview

A Calling Search Space (CSS) is a prioritized list of partitions. Calling Search Spaces determine the call destinations that
                           are available for a caller to call. The call destination must be in a partition that is available to the caller's calling
                           search space, or the caller cannot call that destination. You can assign calling search spaces to directory numbers and to
                           devices such as phones and gateways.

If a calling search space is assigned both to the caller's phone and to the caller's directory number, the system concatenates
                           the two to provide the CSS for the caller.

You can use partitions and calling search spaces to organize your system according to call privileges. For example, you could:

Limit some employees from placing long-distance calls

Limit a lobby phone from place a direct call to the CEO

## Class of Service

You can use partitions and calling search spaces (CSS) to configure classes of service. The table below provides an example
                              of   partitions and calling search spaces that you can create for classes of service that provide PSTN access to:

Emergency calls

Local calls

National calls

International dialing

Base_CSS

Base_PT

—

—

Emergency

On-net

LocalPSTN_CSS

PSTN_Local_PT

—

—

Emergency

On-net

Local

NationalPSTN_CSS

PSTN_Local_PT

PSTN_National_PT

—

Emergency

On-net

Local

National

InternationalPSTN_CSS

PSTN_Local_PT

PSTN_National_PT

PSTN_Intl_PT

Emergency

On-net

Local

National

International

Devices automatically register with a calling search space such as Base_CSS. This allows all devices to dial both on-net and
                              emergency off-net numbers. You must assign the remaining calling search spaces to the directory number on the user device
                              profile to provide local 7-digit or local 10-digit, national, and international dialing capabilities.

## Partition Configuration Task Flow

Step 1

Configure Partitions

Configure partitions to create a logical groupings of system resources with similar reachability characteristics.

Step 2

Configure Calling Search Spaces

Configure the partitions that calling devices search when they are attempting to complete a call.

### Configure Partitions

Configure partitions to create a logical group of system resources with similar reachability characteristics. You can create
                                 partitions for any of the following:

Route patterns

Directory numbers (DNs)

Translation patterns

Transformation patterns

Universal resource indicators (URIs)

Hunt pilots

Partitions facilitate call
                                 		  routing by dividing the route plan into logical subsets that are based on
                                 		  organization, location, and call type. You can configure multiple partitions.

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

#### Partition Name Guidelines

The list of partitions in a calling search space is limited to a maximum of 1024 characters. This means that the maximum number
                                    of partitions in a CSS varies depending on the length of the partition names. Use the following table to determine the maximum
                                    number of partitions that you can add to a calling search space if partition names are of fixed length.

Partition
                                                					 Name Length

Maximum
                                                					 Number of Partitions

2 characters

340

3 characters

256

4 characters

204

5 characters

172

...

...

10
                                                					 characters

92

15
                                                					 characters

64

### Configure Calling
                           	 Search Spaces

A calling
                                 		  search space is an ordered list of route partitions that are typically
                                 		  assigned to devices. Calling search spaces determine the partitions that
                                 		  calling devices can search when they are attempting to complete a call.

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

## Partition Interactions and Restrictions

Delete a Partition

Ensure that you complete one of the following tasks, before you delete a partition:

Assign a different partition to any calling search spaces, devices, or other items that are using the partition that you want
                                             to delete.

Delete the calling search spaces, devices, or other items that are using the partition that you want to delete.

Check carefully to ensure that you are deleting the correct partition, because you cannot retrieve deleted partitions. If
                                       you accidentally delete a partition, you must rebuild it.

Translation Patterns

A translation pattern contains digit manipulations and is assigned to a partition. When a call matches the translation pattern,
                                       Unified CM performs the translation and then reroutes the call using the calling search space that the translation pattern
                                       specifies. For details on translation patterns, see the Configure Call Routing chapter.

Time of Day Routing

Configure a schedule for when a partition is available to accept incoming calls. For details on configuring time of day routing,
                                       see the Configure Call Routing chapter.

Logical Partitioning

Optional : Allows you split your internal VoIP network from your external network with gateway and trunk access. Logical partitioning
                                       is optional for most deployments, but is mandatory in countries such as India where regulations mandate that all calls that
                                       leave the internal network go to a local PSTN gateway. For details on Configuring Logical Partitioning, refer to the " Configure Logical Partitioning " section in the Feature Configuration Guide for Cisco Unified Communications Manager .

| Calling Search Space | Route Partition 1 | Route Partition 2 | Route Partition 3 | Capabilities |
|---|---|---|---|---|
| Base_CSS | Base_PT | — | — | Emergency On-net |
| LocalPSTN_CSS | PSTN_Local_PT | — | — | Emergency On-net Local |
| NationalPSTN_CSS | PSTN_Local_PT | PSTN_National_PT | — | Emergency On-net Local National |
| InternationalPSTN_CSS | PSTN_Local_PT | PSTN_National_PT | PSTN_Intl_PT | Emergency On-net Local National International |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Partitions | Configure partitions to create a logical groupings of system resources with similar reachability characteristics. |
| Step 2 | Configure Calling Search Spaces | Configure the partitions that calling devices search when they are attempting to complete a call. |

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

| Partition
                                                					 Name Length | Maximum
                                                					 Number of Partitions |
|---|---|
| 2 characters | 340 |
| 3 characters | 256 |
| 4 characters | 204 |
| 5 characters | 172 |
| ... | ... |
| 10
                                                					 characters | 92 |
| 15
                                                					 characters | 64 |

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

| Function or Action | Restriction |
|---|---|
| Delete a Partition | Ensure that you complete one of the following tasks, before you delete a partition: Assign a different partition to any calling search spaces, devices, or other items that are using the partition that you want
                                             to delete. Delete the calling search spaces, devices, or other items that are using the partition that you want to delete. Check carefully to ensure that you are deleting the correct partition, because you cannot retrieve deleted partitions. If
                                       you accidentally delete a partition, you must rebuild it. |
| Translation Patterns | A translation pattern contains digit manipulations and is assigned to a partition. When a call matches the translation pattern,
                                       Unified CM performs the translation and then reroutes the call using the calling search space that the translation pattern
                                       specifies. For details on translation patterns, see the Configure Call Routing chapter. |
| Time of Day Routing | Configure a schedule for when a partition is available to accept incoming calls. For details on configuring time of day routing,
                                       see the Configure Call Routing chapter. |
| Logical Partitioning | Optional : Allows you split your internal VoIP network from your external network with gateway and trunk access. Logical partitioning
                                       is optional for most deployments, but is mandatory in countries such as India where regulations mandate that all calls that
                                       leave the internal network go to a local PSTN gateway. For details on Configuring Logical Partitioning, refer to the " Configure Logical Partitioning " section in the Feature Configuration Guide for Cisco Unified Communications Manager . |