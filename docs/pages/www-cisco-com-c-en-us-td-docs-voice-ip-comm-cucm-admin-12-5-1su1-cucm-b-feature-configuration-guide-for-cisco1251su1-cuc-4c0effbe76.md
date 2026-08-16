---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su1-cucm-b-feature-configuration-guide-for-cisco1251su1-cuc-4c0effbe76
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU1/cucm_b_feature-configuration-guide-for-cisco1251SU1/cucm_b_feature-configuration-guide-for-cisco1251SU2_chapter_0101000.html
retrieved_at: 2026-08-16T17:19:37.110835+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

Updated: July 31, 2025

Chapter: Call Display Restrictions

## Chapter: Call Display Restrictions

# Call Display Restrictions

## Call Display
                        	 Restrictions Overview

Cisco Unified
                              		  Communications Manager provides flexible configuration options that allow and
                              		  also restrict the display of the number and name information for both calling and
                              		  connected users. You can restrict connected numbers and names independently of each other.

You can configure connected number and name restrictions on the SIP trunk level or on a call-by-call basis. The SIP trunk
                              level configuration overrides a call-by-call configuration.

For example, in a
                              		  hotel environment, you may want to see the display information for calls that
                              		  are made between a guest room and the front desk. However, for calls between
                              		  guest rooms, you can restrict the call information to display on either phone.

## Call Display
                        	 Restrictions Configuration Task Flow

### Before you begin

Review Call Display Restrictions Interactions

Step 1

Generate a Phone Feature List

Step 2

Configure Partitions for Call Display Restrictions

Step 3

Configure Calling Search Spaces for Call Display Restrictions .

Step 4

Configure the Service Parameter for Connected Number Display Restriction .

Step 5

Configure Translation Patterns .

Step 6

Configure Phones for Call Display Restrictions

Step 7

Configure the PSTN Gateway for Call Display Restrictions

Step 8

Optional. Configure Call Display Restrictions on SIP Trunks

### Configure Partitions for Call Display Restrictions

Configure
                                 		  partitions to create a logical grouping of directory numbers (DNs) and route
                                 		  patterns with similar reachability characteristics. Partitions facilitate call
                                 		  routing by dividing the route plan into logical subsets that are based on
                                 		  organization, location, and call type. You can configure multiple partition

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

### Configure Calling Search Spaces for Call Display Restrictions

Configure
                                 			 calling search spaces to identify the partitions that calling devices can
                                 			 search when they attempt to complete a call. 
                                 		   Create calling search spaces for rooms, the front desk, other hotel extensions, the PSTN, and the room park range (for
                                 call park).

#### Before you begin

Configure Partitions for Call Display Restrictions

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

### Configure the
                           	 Service Parameter for Connected Number Display Restriction

The
                                 		  connected number display restriction restricts the connected line ID
                                 		  display to dialed digits only. This option addresses customer privacy
                                 		  issues as well as connected number displays that are meaningless to phone
                                 		  users.

#### Before you begin

Configure Calling Search Spaces for Call Display Restrictions

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

Select the
                                          			 server where the Cisco CallManager service runs, and then select the Cisco
                                          			 CallManager service.

Step 3

Set the Always
                                             				Display Original Dialed Number service parameter to True to enable this feature.

The default
                                             				value is False .

Step 4

(Optional) Set the Name
                                             				Display for Original Dialed Number When Translated service
                                          			 parameter.

The default
                                             				field shows the alerting name of the original dialed number before
                                             				translation. You can change this parameter to show the alerting name of the
                                             				dialed number after translation. This parameter is not applicable if the Always Display Original Number service parameter is
                                             				set to False .

Step 5

Click Save .

### Configure
                           	 Translation Patterns

Unified Communications Manager uses translation patterns to manipulate dialed digits before it routes a call. In some cases, the system does not use the
                                 dialed number. In other cases, the public switched telephone network (PSTN) does not recognize the dialed number. For the
                                 Call Display Restrictions feature, calls are routed through different translation patterns before the calls are extended to
                                 the actual device.

#### Before you begin

Configure the Service Parameter for Connected Number Display Restriction

Step 1

From Cisco Unified CM Administration, choose Call Routing > Translation Pattern .

Step 2

Configure the fields in the Translation Pattern Configuration window. See Translation Pattern Fields for Call Display Restrictions for more information about the fields and their configuration options.

Step 3

Click Save .

#### Translation Pattern Fields for Call Display Restrictions

Enter the translation pattern, including numbers and wildcards. Do not use spaces. For example, for the NANP, enter 9.@ for
                                                typical local access or 8XXX for a typical private network numbering plan.

Valid characters include the uppercase characters A, B, C, and D and \+, which represents the international escape character
                                                +.

Enter a description for the translation pattern. The description can include up to 50 characters in any language, but it cannot
                                                include double quotes ("), percentage sign (%), ampersand (&), or angle brackets (<>).

From the drop-down list, choose the partition to associate with this translation pattern.

From the drop-down list,
                                                			 choose one of the following options:

- Default —Choose this option
                                                   				if you do not want to change the presentation of the calling line ID.

- Allowed —Choose this option if you want to display the phone number of the calling party.

- Restricted —Choose this option if you want Cisco Unified Communications Manager to block the
                                                   				display of the calling party phone number.

From the drop-down list,
                                                			 choose one of the following options:

- Default —Choose this option
                                                   				if you do not want to change the presentation of the calling name.

- Allowed —Choose this option if you want to display the name of the calling party.

- Restricted —Choose this option if you want Cisco Unified Communications Manager to block the
                                                   				display of the calling name.

From the drop-down list,
                                                			 choose one of the following options:

- Default —Choose this option
                                                   				if you do not want to change the presentation of the connected line ID.

- Allowed —Choose this option if you want to display the phone number of the connected party.

- Restricted —Choose this option if you want Cisco Unified Communications Manager to block the
                                                   				display of the connected party phone number.

From the drop-down list,
                                                			 choose one of the following options:

- Default —Choose this option
                                                   				if you do not want to change the presentation of the connected name.

- Allowed —Choose this option if you want to display the name of the connected party.

- Restricted —Choose this option if you want Cisco Unified Communications Manager to block the
                                                   				display of the connected name.

### Configure Phones
                           	 for Call Display Restrictions

Use this
                                 		  procedure to associate phones with the partitions and the calling search spaces
                                 		  used for call display restrictions.

#### Before you begin

Configure Translation Patterns

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Perform one of
                                          			 the following tasks:

To modify
                                                				  the fields for an existing phone, enter search criteria and choose a phone from
                                                				  the resulting list. The Phone Configuration window appears.

To add a
                                                				  new phone, click Add New .

The Add a New Phone window appears.

Step 3

From the Calling Search Space drop-down list, choose the
                                          			 calling search space that you want the system to use when it determines how to
                                          			 route a dialed number.

Step 4

Check
                                          			 the Ignore
                                             				presentation indicators (internal calls only) check box to ignore
                                          			 any presentation restriction on internal calls.

Step 5

Click Save .

Step 6

To associate the added phone to a directory number, choose Device > Phone ,
                                          			 enter search parameters to search the phone that you added.

Step 7

In the Find and List Phones window, click the phone name.

Step 8

From the Association pane, click the phone name to add
                                          			 or modify the directory number.

Step 9

In the Directory Number Configuration window, add or
                                          			 modify the value of directory number in the Directory Number text box, and select a value
                                          			 in the Route Partition drop-down list.

Step 10

Click Save .

#### Phone
                                 		  Configuration Example

Configure phone A
                                 		  (Room-1) with partition P_Room and device/line calling search space
                                 		  CSS_FromRoom

{ P_Phones,
                                 		  CSS_FromRoom} : 221/Room-1

Configure phone B
                                 		  (Room-2) with partition P_Room and device/line calling search space
                                 		  CSS_FromRoom

{ P_Phones,
                                 		  CSS_FromRoom} : 222/Room-2

Configure phone C
                                 		  (Front Desk-1) with partition P_FrontDesk and device/line calling search space

CSS_FromFrontDesk
                                 		  and Ignore Presentation Indicators check box enabled

{ P_FrontDesk,
                                 		  CSS_FromFrontDesk, IgnorePresentationIndicators set} : 100/Reception

Configure phone D
                                 		  (Front Desk-2) with partition P_FrontDesk and device/line calling search space

CSS_FromFrontDesk
                                 		  and Ignore Presentation Indicators check box enabled

{ P_FrontDesk,
                                 		  CSS_FromFrontDesk, IgnorePresentationIndicators set} : 200/Reception

Configure phone E
                                 		  (Club) with partition P_Club and calling search space CSS_FromClub

{ P_Club,
                                 		  CSS_FromClub) : 300/Club

### Configure the PSTN
                           	 Gateway for Call Display Restrictions

Associate the PSTN gateway with the partitions and the calling search spaces that you want to use for call display restrictions.

#### Before you begin

Configure Phones for Call Display Restrictions

Step 1

In Cisco Unified
                                             				CM Administration , choose Device > Gateway .

Step 2

Enter search
                                          			 criteria and choose the PSTN gateway from the resulting list.

Step 3

From the Calling Search Space drop-down list, choose the
                                          			 calling search space that you want the system to use when it determines how to
                                          			 route an incoming call from the PSTN.

Step 4

Click Save and Reset to apply the configuration changes.

Step 5

(Optional) To associate the available trunk or gateway, in Cisco Unified Communications Manager Administration , choose SIP Route Pattern , and select a SIP trunk or route list from the SIP Trunk/Route List drop-down list.

#### Gateway
                                 		  Configuration Example

Configure PSTN
                                 		  Gateway E with route pattern P_PSTN and calling search space CSS_FromPSTN

{CSS_FromPSTN},
                                 		  RoutePattern {P_PSTN}

### Configure Call
                           	 Display Restrictions on SIP Trunks

You can configure
                                 		  connected number and name restrictions on the SIP trunk level. The SIP
                                 		  trunk-level configuration overrides call-by-call configuration.

#### Before you begin

(Optional) Configure the PSTN Gateway for Call Display Restrictions

Step 1

From Cisco Unified CM Administration, choose Device > Trunk .

Step 2

Enter search
                                          			 criteria and click Find .

Step 3

Select the
                                          			 name of the trunk that you want to update.

Step 4

Configure the fields in the SIP Trunk Configuration window. See SIP Trunk Fields for Call Display Restrictions for more information about the fields and their configuration options.

Step 5

Click Save .

#### SIP Trunk Fields for Call Display Restrictions

From the drop-down list,
                                                			 choose one of the following options:

Default —Choose this option if you do not want to change the presentation of the calling line ID.

Allowed —Choose this option if you want to display the phone number of the calling party.

Restricted —Choose this option if you want Cisco Unified Communications Manager to block the display of the calling party phone number.

From the drop-down list,
                                                			 choose one of the following options:

Default —Choose this option if you do not want to change the presentation of the calling name.

Allowed —Choose this option if you want to display the name of the calling party.

Restricted —Choose this option if you want Cisco Unified Communications Manager to block the display of the calling name.

From the drop-down list, choose the calling search space to associate with this translation pattern.

From the drop-down list, choose one of the following options:

Default —Choose this option if you do not want to change the presentation of the connected line ID.

Allowed —Choose this option if you want to display the phone number of the connected party.

Restricted —Choose this option if you want Cisco Unified Communications Manager to block the display of the connected party phone number.

From the drop-down list, choose one of the following options:

Default —Choose this option if you do not want to change the presentation of the connected name.

Allowed —Choose this option if you want to display the name of the connected party.

Restricted —Choose this option if you want Cisco Unified Communications Manager to block the display of the connected name.

## Call Display
                        	 Restrictions Interactions

This
                              		  section describes how the Call Display Restrictions feature interacts with Cisco Unified
                                 			 Communications Manager applications and call processing features.

Call Park

When you use the Call Display Restrictions feature with Call
                                       					 Park, you must configure an associated translation pattern for each individual
                                       					 call park number to preserve the Call Display Restrictions feature. You cannot
                                       					 configure a single translation pattern to cover a range of call park numbers.

Consider the following scenario as an example:

The
                                             						  system administrator creates a call park range of 77x and places it in a
                                             						  partition called P_ParkRange. (The phones in the guest rooms can see that the
                                             						  P_ParkRange partition is made visible to the phones in the guest rooms by
                                             						  inclusion of it in the calling search space of the phones [CSS_FromRoom]).

The
                                             						  administrator configures a separate translation pattern for each call park
                                             						  directory number and configures the display fields to Restricted. (In the
                                             						  current scenario, the administrator creates translations patterns for 770, 771,
                                             						  772...779.)

For
                                                         							 the Call Display Restrictions feature to work correctly, the administrator must
                                                         							 configure separate translation patterns and not a single translation pattern
                                                         							 for a range of numbers (such as 77x or 77[0-9]).

Room-1
                                             						  calls Room-2.

Room-2
                                             						  answers the call, and Room-1 parks the call.

When
                                             						  Room-1 retrieves the call, Room-2 does not see Room-1 call information display.

Conference
                                       					 List

When you use Call Display Restrictions, you restrict the display
                                       					 information for the list of participants in a conference.

Conference
                                       					 and Voice Mail

When you use Call Display Restrictions with features, such as
                                       					 conference and voice mail, the call information display on the phones reflects
                                       					 that status. For example, when the conference feature is invoked, the call
                                       					 information display shows To Conference . When voice mail is accessed by
                                       					 choosing the Messages button, the call information display shows To Voicemail .

Extension
                                       					 Mobility

To use Call Display Restrictions with Extension Mobility, enable
                                       					 the Ignore Presentation Indicators (internal calls only) parameter in both the Cisco Unified
                                          						Communications Manager Administration Phone Configuration window and
                                       					 the Cisco Unified
                                          						Communications Manager Administration Device Profile Configuration
                                       					 window.

When you enable Call Display Restrictions with Extension
                                       					 Mobility, the presentation or restriction of the call information depends on
                                       					 the line profile that is associated with the user who is logged in to the
                                       					 device. The configuration that is entered in the user device profile
                                       					 (associated with the user) overrides the configuration that is entered in the
                                       					 phone configuration (of the phone that is enabled for Extension Mobility).

Call
                                       					 Forwarding

The
                                       					 Connected Number Display restriction applies to all calls that originate in the
                                       					 system. When this value is set to True , this field interacts with existing Cisco Unified Communications Manager applications,
                                       					 features, and call processing. This value applies to all calls that terminate
                                       					 inside or outside the system. The Connected Number Display is updated to show
                                       					 the modified number or redirected number when a call is routed to a Call
                                       					 Forward All or Call Forward Busy destination, or gets redirected through a call
                                       					 transfer or CTI application.

## Call Display
                        	 Restrictions Feature Restrictions

Translation Patterns—Duplicate entries are not allowed in translation patterns.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Generate a Phone Feature List | Generate a
                                       			 report to identify endpoints that support the Call Display Restrictions
                                       			 feature. |
| Step 2 | Configure Partitions for Call Display Restrictions | Configure
                                       			 partitions to create a logical grouping of directory numbers (DN) and route
                                       			 patterns with similar reachability characteristics. For example, in a hotel
                                       			 environment, you can a configure a partition for dialing between rooms, and a
                                       			 partition for dialing the public switched telephone network (PSTN). |
| Step 3 | Configure Calling Search Spaces for Call Display Restrictions . | Configure
                                       			 calling search spaces to identify the partitions that calling devices can
                                       			 search when they attempt to complete a call. Create calling search spaces for
                                       			 rooms, the front desk, other hotel extensions, the PSTN, and the room park
                                       			 range (for call park). |
| Step 4 | Configure the Service Parameter for Connected Number Display Restriction . | Configure the
                                       			 service parameter to display the connected line ID as dialed digits only. |
| Step 5 | Configure Translation Patterns . | Configure
                                       			 translation patterns with different levels of display restrictions. |
| Step 6 | Configure Phones for Call Display Restrictions | Associate
                                       			 endpoints with the partitions and the calling search spaces that you want to
                                       			 use for call display restrictions. |
| Step 7 | Configure the PSTN Gateway for Call Display Restrictions | Associate the
                                       			 PSTN gateway with the partitions and the calling search spaces that you want to
                                       			 use for call display restrictions. |
| Step 8 | Optional. Configure Call Display Restrictions on SIP Trunks | Use this
                                       			 procedure to configure connected number and name restrictions on the SIP trunk
                                       			 level. The SIP trunk level configuration overrides call-by-call configuration. |

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

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | Select the
                                          			 server where the Cisco CallManager service runs, and then select the Cisco
                                          			 CallManager service. |
| Step 3 | Set the Always
                                             				Display Original Dialed Number service parameter to True to enable this feature. The default
                                             				value is False . |
| Step 4 | (Optional) Set the Name
                                             				Display for Original Dialed Number When Translated service
                                          			 parameter. The default
                                             				field shows the alerting name of the original dialed number before
                                             				translation. You can change this parameter to show the alerting name of the
                                             				dialed number after translation. This parameter is not applicable if the Always Display Original Number service parameter is
                                             				set to False . |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Translation Pattern . |
|---|---|
| Step 2 | Configure the fields in the Translation Pattern Configuration window. See Translation Pattern Fields for Call Display Restrictions for more information about the fields and their configuration options. |
| Step 3 | Click Save . |

| Field | Description |
|---|---|
| Translation Pattern | Enter the translation pattern, including numbers and wildcards. Do not use spaces. For example, for the NANP, enter 9.@ for
                                                typical local access or 8XXX for a typical private network numbering plan. Valid characters include the uppercase characters A, B, C, and D and \+, which represents the international escape character
                                                +. |
| Description | Enter a description for the translation pattern. The description can include up to 50 characters in any language, but it cannot
                                                include double quotes ("), percentage sign (%), ampersand (&), or angle brackets (<>). |
| Partition | From the drop-down list, choose the partition to associate with this translation pattern. |
| Calling Search Space | From the drop-down list, choose the calling search space to associate with this translation pattern. |
| Calling Line ID Presentation | From the drop-down list,
                                                			 choose one of the following options: Default —Choose this option
                                                   				if you do not want to change the presentation of the calling line ID. Allowed —Choose this option if you want to display the phone number of the calling party. Restricted —Choose this option if you want Cisco Unified Communications Manager to block the
                                                   				display of the calling party phone number. |
| Calling Name Presentation | From the drop-down list,
                                                			 choose one of the following options: Default —Choose this option
                                                   				if you do not want to change the presentation of the calling name. Allowed —Choose this option if you want to display the name of the calling party. Restricted —Choose this option if you want Cisco Unified Communications Manager to block the
                                                   				display of the calling name. |
| Connected Line ID Presentation | From the drop-down list,
                                                			 choose one of the following options: Default —Choose this option
                                                   				if you do not want to change the presentation of the connected line ID. Allowed —Choose this option if you want to display the phone number of the connected party. Restricted —Choose this option if you want Cisco Unified Communications Manager to block the
                                                   				display of the connected party phone number. |
| Connected Name Presentation | From the drop-down list,
                                                			 choose one of the following options: Default —Choose this option
                                                   				if you do not want to change the presentation of the connected name. Allowed —Choose this option if you want to display the name of the connected party. Restricted —Choose this option if you want Cisco Unified Communications Manager to block the
                                                   				display of the connected name. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Perform one of
                                          			 the following tasks: To modify
                                                				  the fields for an existing phone, enter search criteria and choose a phone from
                                                				  the resulting list. The Phone Configuration window appears. To add a
                                                				  new phone, click Add New . The Add a New Phone window appears. |
| Step 3 | From the Calling Search Space drop-down list, choose the
                                          			 calling search space that you want the system to use when it determines how to
                                          			 route a dialed number. |
| Step 4 | Check
                                          			 the Ignore
                                             				presentation indicators (internal calls only) check box to ignore
                                          			 any presentation restriction on internal calls. |
| Step 5 | Click Save . The phone is added to the database. |
| Step 6 | To associate the added phone to a directory number, choose Device > Phone ,
                                          			 enter search parameters to search the phone that you added. |
| Step 7 | In the Find and List Phones window, click the phone name. The Phone Configuration window appears. |
| Step 8 | From the Association pane, click the phone name to add
                                          			 or modify the directory number. The Directory Number Configuration window appears. |
| Step 9 | In the Directory Number Configuration window, add or
                                          			 modify the value of directory number in the Directory Number text box, and select a value
                                          			 in the Route Partition drop-down list. |
| Step 10 | Click Save . |

| Step 1 | In Cisco Unified
                                             				CM Administration , choose Device > Gateway . |
|---|---|
| Step 2 | Enter search
                                          			 criteria and choose the PSTN gateway from the resulting list. The Gateway
                                             				Configuration window appears. |
| Step 3 | From the Calling Search Space drop-down list, choose the
                                          			 calling search space that you want the system to use when it determines how to
                                          			 route an incoming call from the PSTN. |
| Step 4 | Click Save and Reset to apply the configuration changes. |
| Step 5 | (Optional) To associate the available trunk or gateway, in Cisco Unified Communications Manager Administration , choose SIP Route Pattern , and select a SIP trunk or route list from the SIP Trunk/Route List drop-down list. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Trunk . The Find and List Trunks window appears. |
|---|---|
| Step 2 | Enter search
                                          			 criteria and click Find . |
| Step 3 | Select the
                                          			 name of the trunk that you want to update. |
| Step 4 | Configure the fields in the SIP Trunk Configuration window. See SIP Trunk Fields for Call Display Restrictions for more information about the fields and their configuration options. |
| Step 5 | Click Save . |

| Field | Description |
|---|---|
| Calling Line ID Presentation | From the drop-down list,
                                                			 choose one of the following options: Default —Choose this option if you do not want to change the presentation of the calling line ID. Allowed —Choose this option if you want to display the phone number of the calling party. Restricted —Choose this option if you want Cisco Unified Communications Manager to block the display of the calling party phone number. |
| Calling Name Presentation | From the drop-down list,
                                                			 choose one of the following options: Default —Choose this option if you do not want to change the presentation of the calling name. Allowed —Choose this option if you want to display the name of the calling party. Restricted —Choose this option if you want Cisco Unified Communications Manager to block the display of the calling name. |
| Calling Search Space | From the drop-down list, choose the calling search space to associate with this translation pattern. |

| Field | Description |
|---|---|
| Connected Line ID Presentation | From the drop-down list, choose one of the following options: Default —Choose this option if you do not want to change the presentation of the connected line ID. Allowed —Choose this option if you want to display the phone number of the connected party. Restricted —Choose this option if you want Cisco Unified Communications Manager to block the display of the connected party phone number. |
| Connected Name Presentation | From the drop-down list, choose one of the following options: Default —Choose this option if you do not want to change the presentation of the connected name. Allowed —Choose this option if you want to display the name of the connected party. Restricted —Choose this option if you want Cisco Unified Communications Manager to block the display of the connected name. |

| Feature | Interaction |
|---|---|
| Call Park | When you use the Call Display Restrictions feature with Call
                                       					 Park, you must configure an associated translation pattern for each individual
                                       					 call park number to preserve the Call Display Restrictions feature. You cannot
                                       					 configure a single translation pattern to cover a range of call park numbers. Consider the following scenario as an example: The
                                             						  system administrator creates a call park range of 77x and places it in a
                                             						  partition called P_ParkRange. (The phones in the guest rooms can see that the
                                             						  P_ParkRange partition is made visible to the phones in the guest rooms by
                                             						  inclusion of it in the calling search space of the phones [CSS_FromRoom]). The
                                             						  administrator configures a separate translation pattern for each call park
                                             						  directory number and configures the display fields to Restricted. (In the
                                             						  current scenario, the administrator creates translations patterns for 770, 771,
                                             						  772...779.) Note For
                                                         							 the Call Display Restrictions feature to work correctly, the administrator must
                                                         							 configure separate translation patterns and not a single translation pattern
                                                         							 for a range of numbers (such as 77x or 77[0-9]). Room-1
                                             						  calls Room-2. Room-2
                                             						  answers the call, and Room-1 parks the call. When
                                             						  Room-1 retrieves the call, Room-2 does not see Room-1 call information display. See Call Park and Directed Call
                                       					 Park | Note | For
                                                         							 the Call Display Restrictions feature to work correctly, the administrator must
                                                         							 configure separate translation patterns and not a single translation pattern
                                                         							 for a range of numbers (such as 77x or 77[0-9]). |
| Note | For
                                                         							 the Call Display Restrictions feature to work correctly, the administrator must
                                                         							 configure separate translation patterns and not a single translation pattern
                                                         							 for a range of numbers (such as 77x or 77[0-9]). |
| Conference
                                       					 List | When you use Call Display Restrictions, you restrict the display
                                       					 information for the list of participants in a conference. See Ad Hoc Conferencing |
| Conference
                                       					 and Voice Mail | When you use Call Display Restrictions with features, such as
                                       					 conference and voice mail, the call information display on the phones reflects
                                       					 that status. For example, when the conference feature is invoked, the call
                                       					 information display shows To Conference . When voice mail is accessed by
                                       					 choosing the Messages button, the call information display shows To Voicemail . |
| Extension
                                       					 Mobility | To use Call Display Restrictions with Extension Mobility, enable
                                       					 the Ignore Presentation Indicators (internal calls only) parameter in both the Cisco Unified
                                          						Communications Manager Administration Phone Configuration window and
                                       					 the Cisco Unified
                                          						Communications Manager Administration Device Profile Configuration
                                       					 window. When you enable Call Display Restrictions with Extension
                                       					 Mobility, the presentation or restriction of the call information depends on
                                       					 the line profile that is associated with the user who is logged in to the
                                       					 device. The configuration that is entered in the user device profile
                                       					 (associated with the user) overrides the configuration that is entered in the
                                       					 phone configuration (of the phone that is enabled for Extension Mobility). |
| Call
                                       					 Forwarding | The
                                       					 Connected Number Display restriction applies to all calls that originate in the
                                       					 system. When this value is set to True , this field interacts with existing Cisco Unified Communications Manager applications,
                                       					 features, and call processing. This value applies to all calls that terminate
                                       					 inside or outside the system. The Connected Number Display is updated to show
                                       					 the modified number or redirected number when a call is routed to a Call
                                       					 Forward All or Call Forward Busy destination, or gets redirected through a call
                                       					 transfer or CTI application. |

| Note | For
                                                         							 the Call Display Restrictions feature to work correctly, the administrator must
                                                         							 configure separate translation patterns and not a single translation pattern
                                                         							 for a range of numbers (such as 77x or 77[0-9]). |
|---|---|