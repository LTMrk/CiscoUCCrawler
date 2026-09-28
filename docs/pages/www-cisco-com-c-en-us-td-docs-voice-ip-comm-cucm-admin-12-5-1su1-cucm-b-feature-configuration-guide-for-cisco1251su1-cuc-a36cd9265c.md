---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su1-cucm-b-feature-configuration-guide-for-cisco1251su1-cuc-a36cd9265c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU1/cucm_b_feature-configuration-guide-for-cisco1251SU1/cucm_b_feature-configuration-guide-for-cisco1251SU2_chapter_011001.html
retrieved_at: 2026-08-16T17:18:32.558684+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

Updated: July 31, 2025

Chapter: Intercom

## Chapter: Intercom

# Intercom

## Intercom
                        	 Overview

Intercom is a type
                           		of phone line that combines the functionality of a traditional line and a speed
                           		dial. With an intercom line, a user can call the intercom line of another user,
                           		which answers automatically to one-way audio whisper. The recipient can then
                           		acknowledge the whispered call and initiate a two-way intercom call.

You can use
                           		an intercom line to dial any other intercom line in the intercom partition, or
                           		you can preconfigure the line to target an intercom line outside the intercom
                           		partition.

Intercom
                           		allows a user to place a call to a predefined target. The called destination
                           		answers the call automatically in speakerphone mode with mute activated. This
                           		sets up a one-way voice path between the initiator and the destination, so the
                           		initiator can deliver a short message, regardless of whether the called party
                           		is busy or idle.

To ensure that the voice of the called party does not get sent back to the caller when the intercom call is automatically
                           answered, Unified Communications Manager implements whisper intercom. Whisper intercom ensures that only one-way audio exists from the caller to the called party.
                           The called party must manually press a key to talk to the caller.

An auto-answer tone
                           		indicates the beginning of the whisper intercom state for both the sender and
                           		the recipient.

### Intercom and
                           	 Default Devices

Each intercom line
                                 		  needs a default device. The intercom line is displayed only on the designated default device.

When the
                                 		  administrator assigns an intercom line to a device, the system sets the device
                                 		  as the default device for the intercom line if not set previously. The
                                 		  administrator can modify the default device for the intercom line. When the
                                 		  administrator changes the default device to a different device, the intercom
                                 		  line gets removed from the original device, even though the intercom line may
                                 		  still be assigned to the original device.

You can assign an
                                 		  intercom line to a device profile. Only when a user uses a device profile to
                                 		  log in to the default device that matches the default device of the intercom
                                 		  line does the intercom line become available. Otherwise, no intercom line is
                                 		  displayed when the user logs in.

## Intercom
                        	 Prerequisites

The intercom feature has the following system requirements:

Cisco Unified IP Phone s Firmware Release 8.3(1) or later

## Intercom
                        	 Configuration Task Flow

### Before you begin

Review Intercom Prerequisites .

Step 1

Configure Intercom Partition

Step 2

Configure an Intercom Calling Search Space

Step 3

Configure an Intercom Translation Pattern

Step 4

Configure an Intercom Directory Number

Step 5

Intercom Line and Speed Dial Configuration

### Configure Intercom
                           	 Partition

#### Before you begin

Ensure the phone
                                 		  model supports the Intercom feature for a particular release and device pack Generate a Phone Feature List

Step 1

From Cisco Unified CM Administration, choose Call Routing > Intercom > Intercom Route Partition .

The Find and List Intercom Partitions window appears.

Step 2

Click Add New .

An Add New Intercom Partition window appears.

Step 3

Under the Intercom Partition Information section, in the Name box, enter the name and description of the
                                          			 intercom partition that you want to add.

To enter multiple partitions, use one line for each partition entry. You can enter up to 75 partitions; the names and descriptions
                                                         can have up to a total of 1475 characters. The partition name cannot exceed 50 characters. Use a comma (,) to separate the
                                                         partition name and description on each line. If a description is not entered, Unified Communications Manager uses the partition name as the description.

Step 4

Click Save .

Step 5

Locate the
                                          			 partition that you want to configure.

Step 6

Configure the
                                          			 fields in the Intercom Partition Configuration field area. See the online help
                                          			 for more information about the fields and their configuration options.

Step 7

Click Save .

The Intercom Partition
                                                				  Configuration window appears.

Step 8

Enter the
                                          			 appropriate settings. For detailed information about the Intercom Partition
                                          			 Configuration parameters, see online help.

Step 9

Click Save .

Step 10

Click Apply
                                             				Config .

### Configure an
                           	 Intercom Calling Search Space

#### Before you begin

Configure Intercom Partition

Step 1

In the menu
                                          			 bar, choose Call
                                                				  Routing > Intercom > Intercom Calling Search
                                                				  Space .

Step 2

Click the Add New .

Step 3

Configure the fields in the Intercom Calling Search Space field area. For more information on the fields and their configuration options, see Online Help.

Step 4

Click Save .

### Configure an
                           	 Intercom Translation Pattern

#### Before you begin

Configure an Intercom Calling Search Space

Step 1

Choose Call
                                                				  Routing > Intercom > Intercom Translation
                                                				  Pattern .

The Find
                                                				  and List Intercom Translation Patterns window appears.

Step 2

Perform one of
                                          			 the followings tasks:

To copy an existing intercom translation pattern, locate the partition to configure, click Copy eside the intercom translation pattern to copy.

To add a new intercom translation pattern, click the Add New .

Step 3

Configure the fields in the Intercom Translation Pattern Configuration field area. For more information on the fields and their configuration options, see Online Help.

Step 4

Click Save .

Ensure that
                                             				the intercom translation pattern that uses the selected partition, route
                                             				filter, and numbering plan combination is unique. if you receive an error that
                                             				indicates duplicate entries, check the route pattern or hunt pilot, translation
                                             				pattern, directory number, call park number, call pickup number, or meet-me
                                             				number configuration windows.

The Intercom Translation
                                                				  Pattern Configuration window displays the newly configured intercom
                                             				translation pattern.

### Configure an
                           	 Intercom Directory Number

You can assign
                                 		  patterns to intercom directory numbers; for example, 352XX. To avoid user
                                 		  confusion, when you assign a pattern to an intercom directory number, add text
                                 		  or digits to these intercom DN configuration fields, Line Text Label, Display
                                 		  (Internal Caller ID), and External Phone Number Mask. These fields are
                                 		  displayed for an intercom directory number only after you add the intercom
                                 		  directory number and you associate the intercom directory number with a phone.

For example, add
                                 		  the username to the line text label and internal caller ID, and add the outside
                                 		  line number to the external number mask, when the calling information is
                                 		  displayed, it says John Chan, not 352XX.

Step 1

Choose Call
                                                				  Routing > Intercom > Intercom Directory
                                                				  Number .

The Find
                                                				  and List Intercom Directory Numbers window is displayed.

Step 2

To locate a
                                          			 specific intercom directory number, enter search criteria and click Find.

Step 3

Perform one of
                                          			 the followings tasks:

To add an intercom directory number, click Add New .

To update
                                                				  an intercom directory number, click the intercom directory number to update.

The Intercom Directory Number Configuration window
                                             				displayed.

Step 4

Configure the fields in the Intercom Directory Number Configuration field area. For more information on the fields and their configuration options, see Online Help.

Step 5

Click Save .

Step 6

Click Apply
                                             				Config .

Step 7

Click Reset
                                             				Phone .

Step 8

Restart
                                          			 devices.

During the
                                             				restart, the system may drop calls on gateways.

### Intercom Line and
                           	 Speed Dial Configuration

#### Before you begin

Configure an Intercom Directory Number

Step 1

Choose Device > Device
                                                				  Settings > Phone Button Template and add the
                                          			 intercom line to an existing phone button template or create a new template.

The intercom
                                                         				  line cannot be configured as the primary line.

Step 2

From the Button
                                             				Information area, from Feature drop-down list, choose Intercom .

Step 3

From the Button
                                             				Information area, from Feature drop-down list, choose Speed
                                             				Dial .

You can
                                                         				  configure the intercom line with a predefined destination (speed dial) to allow
                                                         				  fast access.

Step 4

Click Save .

Step 5

Click Apply
                                             				Config .

## Intercom
                        	 Interactions

Feature

Interaction

Bulk
                                          						Administration Tool

The Unified Communications Manager administrator can use the Bulk Administration Tool to add many intercom users at once instead of adding users individually. For more information, see Bulk Administration Guide for Cisco Unified Communications Manager .

Barge

When the intercom destination is a barge target, the Cisco Unified IP Phone can still support whisper intercom.

When the destination caller chooses to talk to the intercom
                                          						caller by pressing the intercom button, the original call is put on hold, and
                                          						the barge initiator is released.

Do Not
                                          						Disturb (DND)

The intercom call will override DND on the destination phone.

Call
                                          						Preservation

When a call is preserved, the end user must hang up before the phone can reregister with Unified Communications Manager .

When the
                                          						intercom call is in whisper mode, it represents a one-way medium, and the
                                          						terminating side might have no user at all; therefore, only the intercom call
                                          						in talkback mode will get preserved. (Whisper intercom will not get preserved.)

Cisco
                                          						Unified Survivable Remote Site Telephony (SRST)

When Cisco Unified IP Phone s register with SRST, the phones do not register intercom lines; therefore, the feature will not be available when the phones
                                          are registered with SRST.

Cisco
                                          						Unified Communications Manager Assistant

With the Unified Communications Manager Assistant Configuration Wizard, Cisco Unified Communications Manager Assistant configuration takes less time and eliminates errors. The partitions, calling search spaces, route point, and translation
                                          pattern automatically get created when the administrator successfully runs and completes the configuration wizard.

CTI

You can use CTI/JTAPI/TSP to set or modify the preconfigured target directory number for an intercom line. You will receive
                                          notification if the target directory number is updated or reconfigured through Cisco Unified Communications Manager Administration .

Be aware that CTI/JTAPI/TSP is backward compatible if the
                                          						intercom line is not configured to be controlled by the application. If the
                                          						intercom line is configured in the application user list, you may have to make
                                          						changes and test the compatibility.

Cisco
                                          						Extension Mobility

The intercom feature interacts with Cisco Extension Mobility. The system presents an intercom line to a user who uses Cisco
                                          Extension Mobility to log in to a phone that supports the feature if the device profile that the user uses to log in has an
                                          intercom line that is provisioned. The phone must be the default device for that intercom line.

Internet
                                          						Protocol Version 6 (IPv6)

Intercom can support phones with an IP Addressing Mode of IPv4
                                          						Only or IPv4 and IPv6. During an intercom call, the talkback mode establishes
                                          						media streams with the same IP version as the media stream that is used when
                                          						the caller initiates intercom.

Intercom directory numbers (lines)

Intercom directory numbers (lines) are restricted to one device per intercom line. Cisco Extension Mobility is widely used;
                                          mobile users need the intercom feature but need it to be available only on a single device. You can assign intercom lines
                                          to either a regular device or to an extension mobility profile, but the system needs to enforce that an intercom line gets
                                          associated to either a regular device or to an extension mobility profile.

Extension mobility profile

An
                                          						extension mobility profile can be used on more than one phone simultaneously,
                                          						use the Default Activated Device field in the Intercom Directory Number Configuration window ( Cisco Unified CM
                                                							 Administration > Call Routing > Intercom > ntercom Directory Number
                                                							 Configuration ) to specify which device can display
                                          						this intercom line. Intercom lines that are not used for Extension Mobility
                                          						also require configuration of the Default Activated Device field.

## Intercom
                        	 Restrictions

The
                              		  following restrictions apply to the Intercom feature:

Feature

Restrictions

Hold

The system does not allow intercom calls to be placed on
                                          						hold.

Call Forwarding

Intercom calls cannot be forwarded.

Transfer

The system does not allow an intercom call to be
                                          						transferred.

iDivert

The system does not allow an intercom call to be diverted.

Call Pickup/Directed Call Pickup

The call pickup groups do not include intercom calls.

DND

Intercom overrides Do Not Disturb (DND).

Bandwidth

If sufficient bandwidth does not exist, the intercom call
                                          						fails.

Call Target

If two intercom calls are directed to a target, the first
                                          						one goes through; the second fails with a busy tone.

Barge and cBarge

Intercom does not work with Barge and cBarge.

Conferencing

The system does not allow intercom calls to be in
                                          						conference.

Monitoring and Recording

When an active call is being monitored or recorded, the user
                                          						cannot receive nor place intercom calls.

Video

Video is not supported with intercom.

Intercom Partition

An intercom partition assigned to an item such as calling
                                          						search space or to a route pattern cannot be deleted.

Intercom Calling Search Spaces

Intercom calling search spaces that devices, lines (DNs),
                                          						translation patterns, or other items are using cannot be deleted.

## Intercom Troubleshooting

### Busy Tone When
                           	 Dialing Out of Intercom Line

#### Problem

Phone plays busy
                                 		  tone when user is dialing out of intercom line.

#### Possible
                                 		  Cause

The DN is not in
                                 		  the same intercom partition as the calling number.

#### Solution

Ensure that the DN is in the same intercom partition as the calling number.

f it is, ensure that the dialed-out DN is configured on another phone and that the phone is registered with the same Unified Communications Manager cluster.

### Intercom Calls cannot use Talkback with Speaker, Handset or Headset

#### Problem

User cannot go
                                 		  into talkback mode for intercom calls by using headset, handset, or speaker.

#### Possible
                                 		  Cause

This situation
                                 		  exists by design. The only way to go into the connected state for intercom
                                 		  calls is by pressing the corresponding line button.

#### Solution

User can end call
                                 		  by using speaker, handset, or headset.

### Troubleshooting SCCP

#### Intercom Lines Not
                              	 Showing Up on Phone

##### Problem

Intercom lines do
                                    		  not display on the phone.

##### Possible
                                    		  Cause

The phone version
                                    		  may be earlier than 8.3(1), or the button template may not be assigned to the
                                    		  phone.

##### Solution

Check the phone version. Ensure that it is 8.3(1) or later.

Determine whether the button template is assigned to the phone.

Capture the sniffer trace between Cisco Unified Communications Manager and the phone. In the button template response, see
                                          whether intercom lines get sent to the phone (button definition = Ox17).

#### Intercom Lines Not Showing Up When Phone Falls Back to SRST

##### Problem

A phone that was configured with Unified Communications Manager Release 6.0(x) or later, includes two intercom lines. Unified Communications Manager stops and falls back to SRST. The intercom lines do not display.

##### Possible
                                    		  Cause

The SCCP version
                                    		  of SRST does not support SCCP Version 12.

##### Solution

Check the SCCP Version of SRST. If SRST supports SCCP Version 12, it will support intercom lines.

If SRST supports SCCP Version 12, capture a sniffer trace and ensure that the button template that the phone sent includes
                                          intercom lines.

### Troubleshooting SIP

#### Debug Phones That
                              	 Are Running SIP

Use this debug
                                    		  command: Debug sip-messages sip-task gsmfsmIsm sip-adapter .

#### Configuration of
                              	 Phones That Are Running SIP

Show
                                       			 config —The command on the phone is displayed if intercom lines are
                                    		  configured as regular lines with featureid-->23.

### Cisco Extension
                           	 Mobility User Is Logged In But Intercom Line Does Not Display

#### Problem

The Cisco
                                 		  Extension Mobility user is logged in to a phone, but the user intercom line
                                 		  does not display.

#### Possible
                                 		  Cause

Default
                                    			 Activated Device is configured incorrectly.

#### Solution

Check that the Default Activated Device is configured on the intercom directory number.

Check that the Default Activated Device matches the device to which the user is logged in.

### Intercom Line
                           	 Fails to Display on Phone

#### Problem

An intercom line
                                 		  has been configured and assigned to a phone but fails to display on the phone.

#### Possible
                                 		  Cause

Default Activated
                                 		  Device value is set to the intercom line of this device.

#### Solution

If the
                                 		  configuration has been done, reset the phone.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Intercom Partition | To add a new
                                       			 Intercom partition or configure an existing partition. |
| Step 2 | Configure an Intercom Calling Search Space | To add a new
                                       			 Intercom Calling Search Space. |
| Step 3 | Configure an Intercom Translation Pattern | To add a new
                                       			 Intercom Translation Pattern or to configure an existing Intercom Translation
                                       			 Pattern . |
| Step 4 | Configure an Intercom Directory Number | To add or
                                       			 update an Intercom Directory Number. |
| Step 5 | Intercom Line and Speed Dial Configuration | Configure
                                       			 Intercom Line and Speed Dial. |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Intercom > Intercom Route Partition . The Find and List Intercom Partitions window appears. |
|---|---|
| Step 2 | Click Add New . An Add New Intercom Partition window appears. |
| Step 3 | Under the Intercom Partition Information section, in the Name box, enter the name and description of the
                                          			 intercom partition that you want to add. Note To enter multiple partitions, use one line for each partition entry. You can enter up to 75 partitions; the names and descriptions
                                                         can have up to a total of 1475 characters. The partition name cannot exceed 50 characters. Use a comma (,) to separate the
                                                         partition name and description on each line. If a description is not entered, Unified Communications Manager uses the partition name as the description. | Note | To enter multiple partitions, use one line for each partition entry. You can enter up to 75 partitions; the names and descriptions
                                                         can have up to a total of 1475 characters. The partition name cannot exceed 50 characters. Use a comma (,) to separate the
                                                         partition name and description on each line. If a description is not entered, Unified Communications Manager uses the partition name as the description. |
| Note | To enter multiple partitions, use one line for each partition entry. You can enter up to 75 partitions; the names and descriptions
                                                         can have up to a total of 1475 characters. The partition name cannot exceed 50 characters. Use a comma (,) to separate the
                                                         partition name and description on each line. If a description is not entered, Unified Communications Manager uses the partition name as the description. |
| Step 4 | Click Save . |
| Step 5 | Locate the
                                          			 partition that you want to configure. Intercom Partition Configuration window is displayed |
| Step 6 | Configure the
                                          			 fields in the Intercom Partition Configuration field area. See the online help
                                          			 for more information about the fields and their configuration options. |
| Step 7 | Click Save . The Intercom Partition
                                                				  Configuration window appears. |
| Step 8 | Enter the
                                          			 appropriate settings. For detailed information about the Intercom Partition
                                          			 Configuration parameters, see online help. |
| Step 9 | Click Save . |
| Step 10 | Click Apply
                                             				Config . |

| Note | To enter multiple partitions, use one line for each partition entry. You can enter up to 75 partitions; the names and descriptions
                                                         can have up to a total of 1475 characters. The partition name cannot exceed 50 characters. Use a comma (,) to separate the
                                                         partition name and description on each line. If a description is not entered, Unified Communications Manager uses the partition name as the description. |
|---|---|

| Step 1 | In the menu
                                          			 bar, choose Call
                                                				  Routing > Intercom > Intercom Calling Search
                                                				  Space . |
|---|---|
| Step 2 | Click the Add New . |
| Step 3 | Configure the fields in the Intercom Calling Search Space field area. For more information on the fields and their configuration options, see Online Help. |
| Step 4 | Click Save . |

| Step 1 | Choose Call
                                                				  Routing > Intercom > Intercom Translation
                                                				  Pattern . The Find
                                                				  and List Intercom Translation Patterns window appears. |
|---|---|
| Step 2 | Perform one of
                                          			 the followings tasks: To copy an existing intercom translation pattern, locate the partition to configure, click Copy eside the intercom translation pattern to copy. To add a new intercom translation pattern, click the Add New . |
| Step 3 | Configure the fields in the Intercom Translation Pattern Configuration field area. For more information on the fields and their configuration options, see Online Help. |
| Step 4 | Click Save . Ensure that
                                             				the intercom translation pattern that uses the selected partition, route
                                             				filter, and numbering plan combination is unique. if you receive an error that
                                             				indicates duplicate entries, check the route pattern or hunt pilot, translation
                                             				pattern, directory number, call park number, call pickup number, or meet-me
                                             				number configuration windows. The Intercom Translation
                                                				  Pattern Configuration window displays the newly configured intercom
                                             				translation pattern. |

| Step 1 | Choose Call
                                                				  Routing > Intercom > Intercom Directory
                                                				  Number . The Find
                                                				  and List Intercom Directory Numbers window is displayed. |
|---|---|
| Step 2 | To locate a
                                          			 specific intercom directory number, enter search criteria and click Find. A list
                                          			 of intercom directory numbers that match the search criteria displayed. |
| Step 3 | Perform one of
                                          			 the followings tasks: To add an intercom directory number, click Add New . To update
                                                				  an intercom directory number, click the intercom directory number to update. The Intercom Directory Number Configuration window
                                             				displayed. |
| Step 4 | Configure the fields in the Intercom Directory Number Configuration field area. For more information on the fields and their configuration options, see Online Help. |
| Step 5 | Click Save . |
| Step 6 | Click Apply
                                             				Config . |
| Step 7 | Click Reset
                                             				Phone . |
| Step 8 | Restart
                                          			 devices. During the
                                             				restart, the system may drop calls on gateways. |

| Step 1 | Choose Device > Device
                                                				  Settings > Phone Button Template and add the
                                          			 intercom line to an existing phone button template or create a new template. Note The intercom
                                                         				  line cannot be configured as the primary line. | Note | The intercom
                                                         				  line cannot be configured as the primary line. |
|---|---|---|---|
| Note | The intercom
                                                         				  line cannot be configured as the primary line. |
| Step 2 | From the Button
                                             				Information area, from Feature drop-down list, choose Intercom . |
| Step 3 | From the Button
                                             				Information area, from Feature drop-down list, choose Speed
                                             				Dial . Note You can
                                                         				  configure the intercom line with a predefined destination (speed dial) to allow
                                                         				  fast access. | Note | You can
                                                         				  configure the intercom line with a predefined destination (speed dial) to allow
                                                         				  fast access. |
| Note | You can
                                                         				  configure the intercom line with a predefined destination (speed dial) to allow
                                                         				  fast access. |
| Step 4 | Click Save . |
| Step 5 | Click Apply
                                             				Config . |

| Note | The intercom
                                                         				  line cannot be configured as the primary line. |
|---|---|

| Note | You can
                                                         				  configure the intercom line with a predefined destination (speed dial) to allow
                                                         				  fast access. |
|---|---|

| Feature | Interaction |
|---|---|
| Bulk
                                          						Administration Tool | The Unified Communications Manager administrator can use the Bulk Administration Tool to add many intercom users at once instead of adding users individually. For more information, see Bulk Administration Guide for Cisco Unified Communications Manager . |
| Barge | When the intercom destination is a barge target, the Cisco Unified IP Phone can still support whisper intercom. When the destination caller chooses to talk to the intercom
                                          						caller by pressing the intercom button, the original call is put on hold, and
                                          						the barge initiator is released. |
| Do Not
                                          						Disturb (DND) | The intercom call will override DND on the destination phone. |
| Call
                                          						Preservation | When a call is preserved, the end user must hang up before the phone can reregister with Unified Communications Manager . When the
                                          						intercom call is in whisper mode, it represents a one-way medium, and the
                                          						terminating side might have no user at all; therefore, only the intercom call
                                          						in talkback mode will get preserved. (Whisper intercom will not get preserved.) |
| Cisco
                                          						Unified Survivable Remote Site Telephony (SRST) | When Cisco Unified IP Phone s register with SRST, the phones do not register intercom lines; therefore, the feature will not be available when the phones
                                          are registered with SRST. |
| Cisco
                                          						Unified Communications Manager Assistant | With the Unified Communications Manager Assistant Configuration Wizard, Cisco Unified Communications Manager Assistant configuration takes less time and eliminates errors. The partitions, calling search spaces, route point, and translation
                                          pattern automatically get created when the administrator successfully runs and completes the configuration wizard. |
| CTI | You can use CTI/JTAPI/TSP to set or modify the preconfigured target directory number for an intercom line. You will receive
                                          notification if the target directory number is updated or reconfigured through Cisco Unified Communications Manager Administration . Be aware that CTI/JTAPI/TSP is backward compatible if the
                                          						intercom line is not configured to be controlled by the application. If the
                                          						intercom line is configured in the application user list, you may have to make
                                          						changes and test the compatibility. |
| Cisco
                                          						Extension Mobility | The intercom feature interacts with Cisco Extension Mobility. The system presents an intercom line to a user who uses Cisco
                                          Extension Mobility to log in to a phone that supports the feature if the device profile that the user uses to log in has an
                                          intercom line that is provisioned. The phone must be the default device for that intercom line. |
| Internet
                                          						Protocol Version 6 (IPv6) | Intercom can support phones with an IP Addressing Mode of IPv4
                                          						Only or IPv4 and IPv6. During an intercom call, the talkback mode establishes
                                          						media streams with the same IP version as the media stream that is used when
                                          						the caller initiates intercom. |
| Intercom directory numbers (lines) | Intercom directory numbers (lines) are restricted to one device per intercom line. Cisco Extension Mobility is widely used;
                                          mobile users need the intercom feature but need it to be available only on a single device. You can assign intercom lines
                                          to either a regular device or to an extension mobility profile, but the system needs to enforce that an intercom line gets
                                          associated to either a regular device or to an extension mobility profile. |
| Extension mobility profile | An
                                          						extension mobility profile can be used on more than one phone simultaneously,
                                          						use the Default Activated Device field in the Intercom Directory Number Configuration window ( Cisco Unified CM
                                                							 Administration > Call Routing > Intercom > ntercom Directory Number
                                                							 Configuration ) to specify which device can display
                                          						this intercom line. Intercom lines that are not used for Extension Mobility
                                          						also require configuration of the Default Activated Device field. |

| Feature | Restrictions |
|---|---|
| Hold | The system does not allow intercom calls to be placed on
                                          						hold. |
| Call Forwarding | Intercom calls cannot be forwarded. |
| Transfer | The system does not allow an intercom call to be
                                          						transferred. |
| iDivert | The system does not allow an intercom call to be diverted. |
| Call Pickup/Directed Call Pickup | The call pickup groups do not include intercom calls. |
| DND | Intercom overrides Do Not Disturb (DND). |
| Bandwidth | If sufficient bandwidth does not exist, the intercom call
                                          						fails. |
| Call Target | If two intercom calls are directed to a target, the first
                                          						one goes through; the second fails with a busy tone. |
| Barge and cBarge | Intercom does not work with Barge and cBarge. |
| Conferencing | The system does not allow intercom calls to be in
                                          						conference. |
| Monitoring and Recording | When an active call is being monitored or recorded, the user
                                          						cannot receive nor place intercom calls. |
| Video | Video is not supported with intercom. |
| Intercom Partition | An intercom partition assigned to an item such as calling
                                          						search space or to a route pattern cannot be deleted. |
| Intercom Calling Search Spaces | Intercom calling search spaces that devices, lines (DNs),
                                          						translation patterns, or other items are using cannot be deleted. |