---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-cucm-b-bulk-administration-guide-1251-cucm-b-bulk-administra-87004e9fbf
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1/cucm_b_bulk-administration-guide-1251/cucm_b_bulk-administration-guide-1251_chapter_0100011.html
retrieved_at: 2026-08-21T18:00:02.087528+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: March 4, 2020

Chapter: Manage User Device
	 Profiles

## Chapter: Manage User Device
	 Profiles

# Manage User Device
                     	 Profiles

This chapter
                        		provides information about managing user device profiles. The User Device
                        		Profiles (UDP) option in Cisco Unified Communications
                           		  Manager Bulk Administration (BAT) allows you to add or delete large
                        		numbers of user device profiles. In addition, you can add or update lines for
                        		user device profiles. The system uses UDPs in conjunction with the extension
                        		mobility feature.

## Add User Device Profiles

When you use BAT to add user device profiles to the Cisco Unified Communications Manager database, you can add multiple lines
                              		  and other features.

Choose from two options for creating a CSV data file for user
                              		  device profiles:

Use the BAT spreadsheet (BAT.xlt) and export the data to the CSV format.

Use a text editor to create a text file in CSV format (for experienced users).

Step 1

Choose Bulk
                                             				  Administration > User Device
                                             				  Profiles > User Device Profile
                                             				  Template .

Step 2

Create the CSV data file by following the steps for one of these
                                       			 options.

BAT Spreadsheet option

Open the BAT spreadsheet and create the CSV data file.

Text Editor option

Choose Create UDP File Format . The UDP File Format Query window displays.

Use a text editor and create the CSV data file for user device profiles that follows the file format that you want to use.

Choose Add File Format . The Add File Format Configuration window displays.

Step 3

Choose Validate User Device Profiles .

Step 4

Choose Insert User Device Profiles .

### Create User Device Profile CSV Data Files Using BAT Spreadsheet

You can create the CSV data file for adding new user device
                                 		  profiles using the BAT spreadsheet. When you use the BAT spreadsheet to add new
                                 		  user device profiles, you can define the file format within the spreadsheet.
                                 		  The spreadsheet uses the data file formats to display the fields for the CSV
                                 		  data file.

After you have finished editing all the fields in the BAT spreadsheet,
                                 		  you can export the content to a CSV formatted data file. The file is saved to C:\XLSDataFiles or to your choice of another
                                 		  existing folder on your local workstation and is assigned a default filename:

<tabname>-<timestamp>.txt

where <tabname> represents the type of input file that
                                 		  you created, such as phones, and <timestamp> represents the precise date and time
                                 		  that the file was created.

Step 1

Download the BAT.xlt file from the Cisco Unified Communications Manager server.

Step 2

Open the BAT spreadsheet. When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities.

Step 3

To display the User Device Profiles options, click the User Device Profile tab at the bottom of the
                                          			 spreadsheet.

Step 4

To choose the device and line fields that you can define for each
                                          			 user device profile, click Create File Format . The Field Selection popup window displays.

Step 5

To choose the device fields, click a device field name in the Device Field box, and then click the arrow to
                                          			 move the field to the Selected Device Fields box.

A CSV data file must include Device Profile Name and Description ; therefore, these fields always
                                             				remain selected.

Tip

You can select a range of items in the list by holding down the Shift key. To select random field names,
                                                         				  hold down the Ctrl key and click field names.

Step 6

Click a line field name in the Line Field box and click the arrow to move the
                                          			 field to the Selected Line Fields box.

Tip

You can change the order of the items in the Selected Line and Device boxes. Choose an item and use the
                                                         				  up arrow to move the field closer to the beginning of the list or chose the
                                                         				  down arrow to move the item to the end of the list.

Step 7

To modify the CSV data file format, click Create . A message asks whether you want to
                                          			 overwrite the existing CSV format. Click OK .

Step 8

To locate the Number of Phone Lines box, scroll to the
                                          			 right.

Step 9

You must enter the number of speed-dial buttons in the Number of Speed Dials box. After you enter the
                                          			 number, columns display for each speed-dial number.

Do not exceed the number of speed dials that are configured in
                                                         				  the User Device Profile template, or an error will result when you insert the
                                                         				  CSV data file and UDP template.

Step 10

Enter data for an individual user device profile on each line in
                                          			 the spreadsheet. Complete all mandatory fields and any relevant optional
                                          			 fields.

Step 11

To transfer the data from the BAT Excel spreadsheet into a CSV
                                          			 formatted data file, click Export to BAT Format .

The system saves the file using the default filename <tabname>-<timestamp>.txt to C:\XLSDataFiles\ or to your choice of another
                                             				existing folder on your local workstation.

For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert User Device Profiles window in BAT.

#### What to do next

Upload the CSV file to Cisco Unified Communications Manager server.

### User Device Profile
                           	 Fields Descriptions in BAT Spreadsheet

The
                                 		  following table describes all the user device profile fields in the BAT
                                 		  spreadsheet.

Field

Description

Device Fields (Mandatory
                                                						Fields)

Device
                                             					 Profile Name

Enter a
                                             					 unique identifier for the device profile name.

Description

Enter a
                                             					 description such as "Conference
                                                						Room A" or "John
                                                						Smith" to help identify the phone or device. The description can include up
                                             					 to 50 characters in any language, but it cannot include double-quotes ( " ), percentage sign
                                             					 ( % ),
                                             					 ampersand (&), back-slash ( \ ), or angle brackets (<>).

Device Fields (Optional
                                                						Fields)

User Locale

Enter the
                                             					 country and language set that you want to associate with this group of IP
                                             					 phones.

This choice
                                             					 determines which cultural-dependent attributes exist for this user and which
                                             					 language displays for the user in the Cisco Unified Communications
                                                						Manager user windows and phones.

Softkey
                                             					 Template

Enter the
                                             					 softkey template to be used for all phones in this group.

User ID

Enter the
                                             					 user ID for the phone user.

Login User
                                             					 ID

Enter the
                                             					 login user ID for a default profile.

If the user
                                             					 device profile is used as a logout profile, specify the login user ID that will
                                             					 be associated with the phone. After the user logs out from this user device
                                             					 profile, the phone will automatically log in to this login user ID.

User Hold
                                             					 Audio Source

Enter the
                                             					 user hold audio source that this group of IP phones or CTI ports should use.

The user
                                             					 hold audio source identifies the audio source from which music is played when a
                                             					 user places a call on hold.

Phone
                                             					 Template

Enter the
                                             					 phone template name that you want to associate with this user device profile.

MLPP
                                             					 Indication

This setting
                                             					 specifies whether a device that is capable of playing precedence tones will use
                                             					 the capability when it places an MLPP precedence call.

MLPP
                                             					 Preemption

If
                                             					 available, this setting specifies whether a device that is capable of
                                             					 preempting calls in progress will use the capability when it places an MLPP
                                             					 precedence call.

Always Use
                                             					 Prime Line

Enter one of
                                             					 the following options:

- Off—When the phone is idle
                                                						and receives a call on any line, the phone user answers the call from the line
                                                						on which the call is received.

- On—When the phone is idle
                                                						(offhook) and receives a call on any line, the primary line gets chosen for the
                                                						call. Calls on other lines continue to ring, and the phone user must select
                                                						those other lines to answer these calls.

- Default— Cisco Unified Communications Manager uses the
                                                						configuration from the Always Use Prime Line service parameter, which supports
                                                						the Cisco CallManager service.

Always Use
                                             					 Prime Line for Voice Message

Enter one of
                                             					 the following options:

- On—If the phone is idle, the
                                                						primary line on the phone becomes the active line for retrieving voice messages
                                                						when the phone user presses the Messages button on the phone.

- Off—If the phone is idle,
                                                						pressing the Messages button on the phone automatically dials the
                                                						voice-messaging system from the line that has a voice message. Cisco Unified
                                                   						  Communications Manager always selects the first line that has a voice
                                                						message. If no line has a voice message, the primary line gets used when the
                                                						phone user presses the Messages button.

- Default— Cisco Unified Communications Manager uses the
                                                						configuration from the Always Use Prime Line for Voice Message service
                                                						parameter, which supports the Cisco CallManager service.

MLPP
                                             					 Domain

Enter a
                                             					 hexadecimal value for the MLPP domain associated with this device. Must be
                                             					 blank or a value between 0 and FFFFFF.

Feature
                                             					 Control Policy

Choose the
                                             					 Feature Control Policy for this group of phones.

A feature
                                             					 control policy specifies the appearance of features and the associated softkeys
                                             					 that are displayed on the phone.

Extension
                                             					 Mobility Cross Cluster CSS

The
                                             					 Extension Mobility Cross Cluster CSS setting gets used as the device CSS of the
                                             					 remote phone when the user selects this device profile during EMCC login.

Line Fields (Optional
                                                						Fields)

Directory
                                             					 Number

Enter the
                                             					 directory number for the phone.

Route
                                             					 Partition

Choose a
                                             					 route partition to which the directory number belongs.

The
                                             					 directory number can appear in more than one partition.

Display

Enter the
                                             					 text that you want to display on the called party’s phone display, such as the
                                             					 user name (John Smith) or phone location (Conference Room 1).

If this
                                             					 filed is left blank the system uses the value that is entered in the Directory
                                             					 Number field.

The
                                             					 default language specifies English.

Forward
                                             					 All CSS

Choose the
                                             					 calling search space to use when a call is forwarded to the specified
                                             					 destination.

This
                                             					 setting applies to all devices that are using this directory number.

Forward
                                             					 All Destination

Enter the
                                             					 directory number or directory URI to which all calls are forwarded.

This
                                             					 setting applies to any dialable phone number, including an outside destination
                                             					 unless restricted, and to all devices that are using this directory number.

Forward
                                             					 Busy External CSS

Choose the
                                             					 calling search space to use when a call from an external number is forwarded to
                                             					 the specified destination.

This
                                             					 setting applies to all devices that are using this directory number.

Forward
                                             					 Busy Internal CSS

Choose the
                                             					 calling search space to use when a call from an internal number is forwarded to
                                             					 the specified destination.

This
                                             					 setting applies to all devices that are using this directory number.

Forward
                                             					 Busy Destination External

Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 external number is forwarded when the line is in use.

This
                                             					 setting applies to any dialable phone number, including an outside destination
                                             					 unless restricted, and to all devices that are using this directory number.

Forward
                                             					 Busy Destination Internal

Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 internal number is forwarded when the line is in use.

This
                                             					 setting applies to any dialable phone number, including an outside destination
                                             					 unless restricted, and to all devices that are using this directory number.

Calling
                                             					 Search Space Forward No Answer External

Choose the
                                             					 calling search space to use when a call from an external number is forwarded to
                                             					 the specified destination. The setting displays only if it is configured in the
                                             					 system.

This
                                             					 setting applies to all devices that are using this directory number.

Forward No
                                             					 Answer Internal CSS

Choose the
                                             					 calling search space to use a call from an internal number is forwarded to the
                                             					 specified destination. The setting displays only if it is configured in the
                                             					 system.

This
                                             					 setting applies to all devices that are using this directory number.

Forward No
                                             					 Answer External Destination

Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 external number is forwarded when the phone is not answered.

This
                                             					 setting applies to any dialable phone number, including an outside destination
                                             					 unless restricted, and to all devices that are using this directory number.

Forward No
                                             					 Answer Internal Destination

Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 internal number is forwarded when the phone is not answered.

This
                                             					 setting applies to any dialable phone number, including an outside destination
                                             					 unless restricted, and to all devices that are using this directory number.

Forward No
                                             					 Coverage External CSS

Enter the
                                             					 calling search space to use when a call from an external number is forwarded to
                                             					 the specified destination. The setting displays only if it is configured in the
                                             					 system.

This
                                             					 setting applies to all devices that are using this directory number.

Forward No
                                             					 Coverage Internal CSS

Enter the
                                             					 calling search space to use when a call from an internal number is forwarded to
                                             					 the specified destination. The setting displays only if it is configured in the
                                             					 system.

This
                                             					 setting applies to all devices that are using this directory number.

Forward No
                                             					 Coverage External Destination

Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 external number is forwarded when the phone does not have coverage.

This
                                             					 setting applies to any dialable phone number, including an outside destination
                                             					 unless restricted, and to all devices that are using this directory number.

Forward No
                                             					 Coverage Internal Destination

Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 internal number is forwarded when the phone does not have coverage.

This
                                             					 setting applies to any dialable phone number, including an outside destination
                                             					 unless restricted, and to all devices that are using this directory number.

Calling
                                             					 Search Space Forward on Failure External/Internal

(CTI ports
                                             					 only) Enter the calling search space to use when a call from an internal or
                                             					 external call is forwarded to the specified destination. The setting appears
                                             					 only if it is configured in the system.

This
                                             					 setting applies to all devices that are using this directory number.

Forward on
                                             					 Failure Destination External/Internal

(CTI ports
                                             					 only) Enter the directory number or directory URI to which a call coming from
                                             					 an internal or an external number should be forwarded when a phone or CTI
                                             					 application fails.

Call
                                             					 Forward No Answer Ring Duration

Enter the
                                             					 number of seconds (between 1 and 300) to allow the call to ring, before
                                             					 forwarding the call to the destination number entered in the Forward No Answer
                                             					 Destination field.

Leave this
                                             					 field blank to use the value that is set in the Cisco Unified
                                                						Communications Manager service parameter, Forward No Answer Timer.

Route
                                             					 Filter

Enter a
                                             					 name in the Route Filter Name field. The name can contain up to 50 alphanumeric
                                             					 characters and can contain any combination of spaces, periods (.), hyphens (-),
                                             					 and underscore characters ( _ ). Ensure each route filter name is unique to the
                                             					 route plan.

Use
                                             					 concise and descriptive names for your route filters. The
                                             					 CompanynameLocationCalltype format usually provides a sufficient level of
                                             					 detail and is short enough to enable you to quickly and easily identify a route
                                             					 filter. For example, CiscoDallasMetro identifies a route filter for toll free,
                                             					 inter-local access and transport area (LATA) calls from the Cisco office in
                                             					 Dallas.

Party
                                             					 Entrance Tone

Enter one
                                             					 of the following options:

- Default—Use the value that
                                                						you configured in the Party Entrance Tone service parameter.

- On—A tone plays on the
                                                						phone when a basic call changes to a multi-party call; that is, a barge call,
                                                						cBarge call, ad hoc conference, meet-me conference, or a joined call. In
                                                						addition, a different tone plays when a party leaves the multi-party call. If
                                                						the controlling device, that is, the originator of the multi-party call has a
                                                						built-in bridge, the tone gets played to all parties if you choose On for the
                                                						controlling device. When the controlling device, for example, the conference
                                                						controller, is no longer present on the call or if the controlling device
                                                						cannot play the tone, Cisco Unified Communications Manager does not play the
                                                						tone even if you choose On.

- Off—A tone does not play on
                                                						the phone when a basic call changes to a multi-party call.

Log Missed
                                             					 Calls

This field
                                             					 allows you to turn this feature on or off. Enter ‘T’ to enable Cisco Unified
                                                						Communications Manager to log missed calls in the call history for
                                             					 that directory number on the phone. Enter ‘F’ to disable this feature.

Park
                                             					 Monitoring Forward No Retrieve Destination External

When the
                                             					 parkee is an external party, then the call will be forwarded to the specified
                                             					 destination in the parker’s Park Monitoring Forward No Retrieve Destination
                                             					 External parameter. If the Forward No Retrieve Destination External field value
                                             					 is empty, the parkee will be redirected to the parker’s line.

Park
                                             					 Monitoring Forward No Retrieve Destination Internal

When the
                                             					 parkee is an internal party, then the call will be forwarded to the specified
                                             					 destination in the parker’s Park Monitoring Forward No Retrieve Destination
                                             					 Internal parameter. If the Forward No Retrieve Destination Internal is empty,
                                             					 the parkee will be redirected to the parker’s line.

Park
                                             					 Monitoring Forward No Retrieve Internal Voice Mail

This
                                             					 setting uses the settings in the Voice Mail Profile Configuration window.

When this
                                             					 check box is checked, Cisco Unified Communications Manager ignores the settings
                                             					 in the Destination box and Calling Search Space.

Park
                                             					 Monitoring Forward No Retrieve External Voice Mail

This
                                             					 setting uses the settings in the Voice Mail Profile Configuration window.

When this
                                             					 check box is checked, Cisco Unified Communications Manager ignores the settings
                                             					 in the Destination box and Calling Search Space.

Park
                                             					 Monitoring Forward No Retrieve External CSS

Choose the
                                             					 calling search space to apply to the directory number.

Park
                                             					 Monitoring Forward No Retrieve Internal CSS

Choose the
                                             					 calling search space to apply to the directory number.

Park
                                             					 Monitoring Reversion Timer

This
                                             					 parameter determines the number of seconds that Cisco Unified Communications Manager waits before
                                             					 prompting the user to retrieve a call that the user parked. This timer starts
                                             					 when the user presses the Park softkey on the phone, and a reminder is issued
                                             					 when the timer expires.

Default:
                                             					 60 seconds

If you
                                             					 configure a non-zero value, this value overrides the value of this parameter
                                             					 set in the Service Parameters window. However, if you configure
                                             					 a value of 0 here, then the value in the Service Parameters window will be
                                             					 used.

E164

Always use
                                             					 a unique E.164 number. Do not use null value.

Voice Mail
                                             					 Profile

Enter this
                                             					 parameter to make the pilot number the same as the directory number for this
                                             					 line. This action proves useful if you do not have a voice-messaging server
                                             					 configured for this phone.

Line
                                             					 Calling Search Space

Enter
                                             					 partitions that are searched for numbers that are called from this directory
                                             					 number.

Changes
                                                         						cause an update of the call pickup names that are listed in the Call Pickup Group field. The setting applies to all
                                                         						devices that are using this directory number.

AAR Group

Enter the
                                             					 automated alternate routing (AAR) group for this device. The AAR group provides
                                             					 the prefix digits that are used to route calls that are otherwise blocked due
                                             					 to insufficient bandwidth.

Set AAR
                                             					 Group to <None> to prevent rerouting blocked calls.

Line User
                                             					 Hold Audio Source

Enter the
                                             					 music on hold audio source to be played when the user presses Hold and places a
                                             					 call on hold.

Line
                                             					 Network Hold Audio Source

Enter the
                                             					 music on hold audio source to be played when the system places a call on hold
                                             					 while the user transfers a call or initiates a conference or call park.

Auto
                                             					 Answer

Enter one
                                             					 of the following values to activate the Auto Answer feature for this directory
                                             					 number:

- Auto Answer Off
                                                						<Default>

- Auto Answer with Headset

- Auto Answer with
                                                						Speakerphone (Intercom)

Make
                                                         						sure that the headset or speakerphone is not disabled when you choose Auto
                                                         						Answer with Headset or Auto Answer with Speakerphone.

No Answer
                                             					 Ring Duration (CFNA)

Enter the
                                             					 number of seconds to allow the call to ring before forwarding the call to the
                                             					 Forward No Answer Destination.

Call
                                             					 Pickup Group

Enter the
                                             					 Pickup Group Name to specify the call pickup group, which can answer incoming
                                             					 calls to this line by dialling the appropriate pickup group number.

To use the
                                             					 BAT phone template entry, leave this field blank.

Target
                                             					 Destination (MLPP)

Enter the
                                             					 number to which MLPP precedence calls should be directed if this directory
                                             					 number receives a precedence call and neither this number nor its call forward
                                             					 destination answers the precedence call.

Values can
                                             					 include numeric characters, pound ( # ) ,and asterisk ( * ).

Target CSS
                                             					 (MLPP)

From the
                                             					 drop-down list box, choose the calling search space to associate with the
                                             					 alternate party target (destination) number.

No Answer
                                             					 Ring Duration (MLPP)

Enter the
                                             					 number of seconds (between 4 and 30) after which an MLPP precedence call will
                                             					 be directed to this directory number’s alternate party if this directory number
                                             					 and its call forwarding destination have not answered the precedence call.

Leave this
                                             					 setting blank to use the value that is set in the Cisco Unified
                                                						Communications Manager enterprise parameter, Precedence Alternate
                                             					 Party Timeout.

Line Text
                                             					 Label

Enter text
                                             					 that identifies this directory number for a line/phone combination.

The
                                             					 default text specifies English

External
                                             					 Phone Number Mask

Enter the
                                             					 phone number (or mask) that is sent for Caller ID information when a call is
                                             					 placed from this line.

You can
                                             					 enter a maximum of 30 numbers and "X" characters. The Xs represent the directory number and must appear at the end of
                                             					 the pattern. For example, if you specify a mask of 972813XXXX, an external call
                                             					 from extension 1234 displays a caller ID number of 9728131234.

Maximum
                                             					 Number of Calls

You can
                                             					 configure up to 200 calls for a line on a device in a cluster, with the
                                             					 limiting factor being the device. As you configure the number of calls for one
                                             					 line, the calls available for another line decrease.

The
                                             					 default specifies 4. If the phone does not allow multiple calls for each line,
                                             					 the default specifies 2.

For CTI
                                             					 route points, you can configure up to 10,000 calls for each port. The default
                                             					 specifies 5000 calls. Use this field in conjunction with the Busy Trigger
                                             					 field.

Busy
                                             					 Trigger

This
                                             					 setting, which works in conjunction with Maximum Number of Calls and Call
                                             					 Forward Busy, determines the maximum number of calls to be presented at the
                                             					 line. If maximum number of calls is set for 50 and the busy trigger is set to
                                             					 40, then incoming call 41 gets rejected with a busy cause (and will get
                                             					 forwarded if Call Forward Busy is set). If this line is shared, all the lines
                                             					 must be busy before incoming calls get rejected.

Use this
                                             					 field in conjunction with Maximum Number of Calls for CTI route points. The
                                             					 default specifies 4500 calls.

Message
                                             					 Waiting Lamp Policy

Use this
                                             					 field to configure the handset lamp illumination policy. Choose one of the
                                             					 following options:

- Use System Policy (The
                                                						directory number refers to the service parameter "Message Waiting Lamp Policy" setting.)

- Light and Prompt

- Prompt Only

- Light Only

- None

Ring
                                             					 Setting (Phone Idle)

Choose the
                                             					 ring setting for the line appearance when an incoming call is received and no
                                             					 other active calls exist on that device. Choose one of the following options:

- Use system default

- Disable

- Flash only

- Ring once

- Ring

The "Disable 
                                                            						" or "Flash only" setting options apply only for the handset.
                                                         						The led light on the phone button line will still flash.

Ring
                                             					 Setting (Phone Active)

Choose the
                                             					 ring setting that is used when this phone has another active call on a
                                             					 different line. Choose one of the following options:

- Use system default

- Disable

- Flash only

- Ring once

- Ring

- Beep only

The "Disable 
                                                            						" or "Flash only" setting options apply only for the handset.
                                                         						The led light on the phone button line will still flash.

URI (1-5)
                                             					 on Directory Number

Enter a
                                             					 directory URI to associate with the directory number for this phone. Follow the
                                             					 username@host format. Enter a username of up to 47 alphanumeric characters. For
                                             					 the host address, enter an IPv4 address or fully qualified domain name.

Within
                                                         						Cisco Unified CM Administration, you can enter directory URIs with embedded
                                                         						double quotes or commas. However, when you use Bulk Administration to import a
                                                         						csv file that contains directory URIs with embedded double quotes and commas,
                                                         						you must use enclose the entire directory URI in double quotes and escape the
                                                         						embedded double quotes with a double quote. For example, the Jared,
                                                         						"Jerry",Smith@test.com directory URI must be input as
                                                         						"Jared,""Jerry"",Smith@test.com" in the csv file.

URI (1-5)
                                             					 on Route Partition

Enter the
                                             					 partition on which the directory URI belongs. If you do not want to restrict
                                             					 access to the directory URI, leave the field blank

URI (1-5)
                                             					 Is Primary on Directory Number

Enter a
                                             					 ' t ' (True) to
                                             					 indicate that this directory URI is the primary directory URI for this
                                             					 extension. Otherwise, enter an ' f' (False) to indicate that this is not the primary
                                             					 directory URI for this extension.

You can
                                                         						associate up to five directory URIs to a single directory number, but you must
                                                         						select a single primary directory URI.

## Topics Related to User Device Profiles

| Step 1 | Choose Bulk
                                             				  Administration > User Device
                                             				  Profiles > User Device Profile
                                             				  Template . The Find and List UDP Templates window displays. |
|---|---|
| Step 2 | Create the CSV data file by following the steps for one of these
                                       			 options. BAT Spreadsheet option Open the BAT spreadsheet and create the CSV data file. Text Editor option Choose Create UDP File Format . The UDP File Format Query window displays. Use a text editor and create the CSV data file for user device profiles that follows the file format that you want to use. Choose Add File Format . The Add File Format Configuration window displays. |
| Step 3 | Choose Validate User Device Profiles . The User Device Profiles Validation window displays. |
| Step 4 | Choose Insert User Device Profiles . The User Device Profiles Insert Configuration window
                                       			 displays. |

| Step 1 | Download the BAT.xlt file from the Cisco Unified Communications Manager server. |
|---|---|
| Step 2 | Open the BAT spreadsheet. When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities. |
| Step 3 | To display the User Device Profiles options, click the User Device Profile tab at the bottom of the
                                          			 spreadsheet. |
| Step 4 | To choose the device and line fields that you can define for each
                                          			 user device profile, click Create File Format . The Field Selection popup window displays. |
| Step 5 | To choose the device fields, click a device field name in the Device Field box, and then click the arrow to
                                          			 move the field to the Selected Device Fields box. A CSV data file must include Device Profile Name and Description ; therefore, these fields always
                                             				remain selected. Tip You can select a range of items in the list by holding down the Shift key. To select random field names,
                                                         				  hold down the Ctrl key and click field names. | Tip | You can select a range of items in the list by holding down the Shift key. To select random field names,
                                                         				  hold down the Ctrl key and click field names. |
| Tip | You can select a range of items in the list by holding down the Shift key. To select random field names,
                                                         				  hold down the Ctrl key and click field names. |
| Step 6 | Click a line field name in the Line Field box and click the arrow to move the
                                          			 field to the Selected Line Fields box. Tip You can change the order of the items in the Selected Line and Device boxes. Choose an item and use the
                                                         				  up arrow to move the field closer to the beginning of the list or chose the
                                                         				  down arrow to move the item to the end of the list. | Tip | You can change the order of the items in the Selected Line and Device boxes. Choose an item and use the
                                                         				  up arrow to move the field closer to the beginning of the list or chose the
                                                         				  down arrow to move the item to the end of the list. |
| Tip | You can change the order of the items in the Selected Line and Device boxes. Choose an item and use the
                                                         				  up arrow to move the field closer to the beginning of the list or chose the
                                                         				  down arrow to move the item to the end of the list. |
| Step 7 | To modify the CSV data file format, click Create . A message asks whether you want to
                                          			 overwrite the existing CSV format. Click OK . New columns for the selected fields display in the BAT
                                          			 spreadsheet in the order that you specified. |
| Step 8 | To locate the Number of Phone Lines box, scroll to the
                                          			 right. The number of lines that you specify here must not exceed the
                                          			 number of lines that are configured in the BAT template or an error will result
                                          			 when you insert the CSV data file and UDP template. |
| Step 9 | You must enter the number of speed-dial buttons in the Number of Speed Dials box. After you enter the
                                          			 number, columns display for each speed-dial number. Note Do not exceed the number of speed dials that are configured in
                                                         				  the User Device Profile template, or an error will result when you insert the
                                                         				  CSV data file and UDP template. | Note | Do not exceed the number of speed dials that are configured in
                                                         				  the User Device Profile template, or an error will result when you insert the
                                                         				  CSV data file and UDP template. |
| Note | Do not exceed the number of speed dials that are configured in
                                                         				  the User Device Profile template, or an error will result when you insert the
                                                         				  CSV data file and UDP template. |
| Step 10 | Enter data for an individual user device profile on each line in
                                          			 the spreadsheet. Complete all mandatory fields and any relevant optional
                                          			 fields. Each column heading specifies the length of the field and whether
                                          			 it is required or optional. See Table 1 for field descriptions. |
| Step 11 | To transfer the data from the BAT Excel spreadsheet into a CSV
                                          			 formatted data file, click Export to BAT Format . The system saves the file using the default filename <tabname>-<timestamp>.txt to C:\XLSDataFiles\ or to your choice of another
                                             				existing folder on your local workstation. Note For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert User Device Profiles window in BAT. | Note | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert User Device Profiles window in BAT. |
| Note | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert User Device Profiles window in BAT. |

| Tip | You can select a range of items in the list by holding down the Shift key. To select random field names,
                                                         				  hold down the Ctrl key and click field names. |
|---|---|

| Tip | You can change the order of the items in the Selected Line and Device boxes. Choose an item and use the
                                                         				  up arrow to move the field closer to the beginning of the list or chose the
                                                         				  down arrow to move the item to the end of the list. |
|---|---|

| Note | Do not exceed the number of speed dials that are configured in
                                                         				  the User Device Profile template, or an error will result when you insert the
                                                         				  CSV data file and UDP template. |
|---|---|

| Note | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert User Device Profiles window in BAT. |
|---|---|

| Field | Description |
|---|---|
| Device Fields (Mandatory
                                                						Fields) |
| Device
                                             					 Profile Name | Enter a
                                             					 unique identifier for the device profile name. |
| Description | Enter a
                                             					 description such as "Conference
                                                						Room A" or "John
                                                						Smith" to help identify the phone or device. The description can include up
                                             					 to 50 characters in any language, but it cannot include double-quotes ( " ), percentage sign
                                             					 ( % ),
                                             					 ampersand (&), back-slash ( \ ), or angle brackets (<>). |
| Device Fields (Optional
                                                						Fields) |
| User Locale | Enter the
                                             					 country and language set that you want to associate with this group of IP
                                             					 phones. This choice
                                             					 determines which cultural-dependent attributes exist for this user and which
                                             					 language displays for the user in the Cisco Unified Communications
                                                						Manager user windows and phones. |
| Softkey
                                             					 Template | Enter the
                                             					 softkey template to be used for all phones in this group. |
| User ID | Enter the
                                             					 user ID for the phone user. |
| Login User
                                             					 ID | Enter the
                                             					 login user ID for a default profile. If the user
                                             					 device profile is used as a logout profile, specify the login user ID that will
                                             					 be associated with the phone. After the user logs out from this user device
                                             					 profile, the phone will automatically log in to this login user ID. |
| User Hold
                                             					 Audio Source | Enter the
                                             					 user hold audio source that this group of IP phones or CTI ports should use. The user
                                             					 hold audio source identifies the audio source from which music is played when a
                                             					 user places a call on hold. |
| Phone
                                             					 Template | Enter the
                                             					 phone template name that you want to associate with this user device profile. |
| MLPP
                                             					 Indication | This setting
                                             					 specifies whether a device that is capable of playing precedence tones will use
                                             					 the capability when it places an MLPP precedence call. |
| MLPP
                                             					 Preemption | If
                                             					 available, this setting specifies whether a device that is capable of
                                             					 preempting calls in progress will use the capability when it places an MLPP
                                             					 precedence call. |
| Always Use
                                             					 Prime Line | Enter one of
                                             					 the following options: Off—When the phone is idle
                                                						and receives a call on any line, the phone user answers the call from the line
                                                						on which the call is received. On—When the phone is idle
                                                						(offhook) and receives a call on any line, the primary line gets chosen for the
                                                						call. Calls on other lines continue to ring, and the phone user must select
                                                						those other lines to answer these calls. Default— Cisco Unified Communications Manager uses the
                                                						configuration from the Always Use Prime Line service parameter, which supports
                                                						the Cisco CallManager service. |
| Always Use
                                             					 Prime Line for Voice Message | Enter one of
                                             					 the following options: On—If the phone is idle, the
                                                						primary line on the phone becomes the active line for retrieving voice messages
                                                						when the phone user presses the Messages button on the phone. Off—If the phone is idle,
                                                						pressing the Messages button on the phone automatically dials the
                                                						voice-messaging system from the line that has a voice message. Cisco Unified
                                                   						  Communications Manager always selects the first line that has a voice
                                                						message. If no line has a voice message, the primary line gets used when the
                                                						phone user presses the Messages button. Default— Cisco Unified Communications Manager uses the
                                                						configuration from the Always Use Prime Line for Voice Message service
                                                						parameter, which supports the Cisco CallManager service. |
| MLPP
                                             					 Domain | Enter a
                                             					 hexadecimal value for the MLPP domain associated with this device. Must be
                                             					 blank or a value between 0 and FFFFFF. |
| Feature
                                             					 Control Policy | Choose the
                                             					 Feature Control Policy for this group of phones. A feature
                                             					 control policy specifies the appearance of features and the associated softkeys
                                             					 that are displayed on the phone. |
| Extension
                                             					 Mobility Cross Cluster CSS | The
                                             					 Extension Mobility Cross Cluster CSS setting gets used as the device CSS of the
                                             					 remote phone when the user selects this device profile during EMCC login. |
| Line Fields (Optional
                                                						Fields) |
| Directory
                                             					 Number | Enter the
                                             					 directory number for the phone. |
| Route
                                             					 Partition | Choose a
                                             					 route partition to which the directory number belongs. The
                                             					 directory number can appear in more than one partition. |
| Display | Enter the
                                             					 text that you want to display on the called party’s phone display, such as the
                                             					 user name (John Smith) or phone location (Conference Room 1). If this
                                             					 filed is left blank the system uses the value that is entered in the Directory
                                             					 Number field. The
                                             					 default language specifies English. |
| Forward
                                             					 All CSS | Choose the
                                             					 calling search space to use when a call is forwarded to the specified
                                             					 destination. This
                                             					 setting applies to all devices that are using this directory number. |
| Forward
                                             					 All Destination | Enter the
                                             					 directory number or directory URI to which all calls are forwarded. This
                                             					 setting applies to any dialable phone number, including an outside destination
                                             					 unless restricted, and to all devices that are using this directory number. |
| Forward
                                             					 Busy External CSS | Choose the
                                             					 calling search space to use when a call from an external number is forwarded to
                                             					 the specified destination. This
                                             					 setting applies to all devices that are using this directory number. |
| Forward
                                             					 Busy Internal CSS | Choose the
                                             					 calling search space to use when a call from an internal number is forwarded to
                                             					 the specified destination. This
                                             					 setting applies to all devices that are using this directory number. |
| Forward
                                             					 Busy Destination External | Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 external number is forwarded when the line is in use. This
                                             					 setting applies to any dialable phone number, including an outside destination
                                             					 unless restricted, and to all devices that are using this directory number. |
| Forward
                                             					 Busy Destination Internal | Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 internal number is forwarded when the line is in use. This
                                             					 setting applies to any dialable phone number, including an outside destination
                                             					 unless restricted, and to all devices that are using this directory number. |
| Calling
                                             					 Search Space Forward No Answer External | Choose the
                                             					 calling search space to use when a call from an external number is forwarded to
                                             					 the specified destination. The setting displays only if it is configured in the
                                             					 system. This
                                             					 setting applies to all devices that are using this directory number. |
| Forward No
                                             					 Answer Internal CSS | Choose the
                                             					 calling search space to use a call from an internal number is forwarded to the
                                             					 specified destination. The setting displays only if it is configured in the
                                             					 system. This
                                             					 setting applies to all devices that are using this directory number. |
| Forward No
                                             					 Answer External Destination | Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 external number is forwarded when the phone is not answered. This
                                             					 setting applies to any dialable phone number, including an outside destination
                                             					 unless restricted, and to all devices that are using this directory number. |
| Forward No
                                             					 Answer Internal Destination | Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 internal number is forwarded when the phone is not answered. This
                                             					 setting applies to any dialable phone number, including an outside destination
                                             					 unless restricted, and to all devices that are using this directory number. |
| Forward No
                                             					 Coverage External CSS | Enter the
                                             					 calling search space to use when a call from an external number is forwarded to
                                             					 the specified destination. The setting displays only if it is configured in the
                                             					 system. This
                                             					 setting applies to all devices that are using this directory number. |
| Forward No
                                             					 Coverage Internal CSS | Enter the
                                             					 calling search space to use when a call from an internal number is forwarded to
                                             					 the specified destination. The setting displays only if it is configured in the
                                             					 system. This
                                             					 setting applies to all devices that are using this directory number. |
| Forward No
                                             					 Coverage External Destination | Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 external number is forwarded when the phone does not have coverage. This
                                             					 setting applies to any dialable phone number, including an outside destination
                                             					 unless restricted, and to all devices that are using this directory number. |
| Forward No
                                             					 Coverage Internal Destination | Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 internal number is forwarded when the phone does not have coverage. This
                                             					 setting applies to any dialable phone number, including an outside destination
                                             					 unless restricted, and to all devices that are using this directory number. |
| Calling
                                             					 Search Space Forward on Failure External/Internal | (CTI ports
                                             					 only) Enter the calling search space to use when a call from an internal or
                                             					 external call is forwarded to the specified destination. The setting appears
                                             					 only if it is configured in the system. This
                                             					 setting applies to all devices that are using this directory number. |
| Forward on
                                             					 Failure Destination External/Internal | (CTI ports
                                             					 only) Enter the directory number or directory URI to which a call coming from
                                             					 an internal or an external number should be forwarded when a phone or CTI
                                             					 application fails. |
| Call
                                             					 Forward No Answer Ring Duration | Enter the
                                             					 number of seconds (between 1 and 300) to allow the call to ring, before
                                             					 forwarding the call to the destination number entered in the Forward No Answer
                                             					 Destination field. Leave this
                                             					 field blank to use the value that is set in the Cisco Unified
                                                						Communications Manager service parameter, Forward No Answer Timer. |
| Route
                                             					 Filter | Enter a
                                             					 name in the Route Filter Name field. The name can contain up to 50 alphanumeric
                                             					 characters and can contain any combination of spaces, periods (.), hyphens (-),
                                             					 and underscore characters ( _ ). Ensure each route filter name is unique to the
                                             					 route plan. Use
                                             					 concise and descriptive names for your route filters. The
                                             					 CompanynameLocationCalltype format usually provides a sufficient level of
                                             					 detail and is short enough to enable you to quickly and easily identify a route
                                             					 filter. For example, CiscoDallasMetro identifies a route filter for toll free,
                                             					 inter-local access and transport area (LATA) calls from the Cisco office in
                                             					 Dallas. |
| Party
                                             					 Entrance Tone | Enter one
                                             					 of the following options: Default—Use the value that
                                                						you configured in the Party Entrance Tone service parameter. On—A tone plays on the
                                                						phone when a basic call changes to a multi-party call; that is, a barge call,
                                                						cBarge call, ad hoc conference, meet-me conference, or a joined call. In
                                                						addition, a different tone plays when a party leaves the multi-party call. If
                                                						the controlling device, that is, the originator of the multi-party call has a
                                                						built-in bridge, the tone gets played to all parties if you choose On for the
                                                						controlling device. When the controlling device, for example, the conference
                                                						controller, is no longer present on the call or if the controlling device
                                                						cannot play the tone, Cisco Unified Communications Manager does not play the
                                                						tone even if you choose On. Off—A tone does not play on
                                                						the phone when a basic call changes to a multi-party call. |
| Log Missed
                                             					 Calls | This field
                                             					 allows you to turn this feature on or off. Enter ‘T’ to enable Cisco Unified
                                                						Communications Manager to log missed calls in the call history for
                                             					 that directory number on the phone. Enter ‘F’ to disable this feature. |
| Park
                                             					 Monitoring Forward No Retrieve Destination External | When the
                                             					 parkee is an external party, then the call will be forwarded to the specified
                                             					 destination in the parker’s Park Monitoring Forward No Retrieve Destination
                                             					 External parameter. If the Forward No Retrieve Destination External field value
                                             					 is empty, the parkee will be redirected to the parker’s line. |
| Park
                                             					 Monitoring Forward No Retrieve Destination Internal | When the
                                             					 parkee is an internal party, then the call will be forwarded to the specified
                                             					 destination in the parker’s Park Monitoring Forward No Retrieve Destination
                                             					 Internal parameter. If the Forward No Retrieve Destination Internal is empty,
                                             					 the parkee will be redirected to the parker’s line. |
| Park
                                             					 Monitoring Forward No Retrieve Internal Voice Mail | This
                                             					 setting uses the settings in the Voice Mail Profile Configuration window. When this
                                             					 check box is checked, Cisco Unified Communications Manager ignores the settings
                                             					 in the Destination box and Calling Search Space. |
| Park
                                             					 Monitoring Forward No Retrieve External Voice Mail | This
                                             					 setting uses the settings in the Voice Mail Profile Configuration window. When this
                                             					 check box is checked, Cisco Unified Communications Manager ignores the settings
                                             					 in the Destination box and Calling Search Space. |
| Park
                                             					 Monitoring Forward No Retrieve External CSS | Choose the
                                             					 calling search space to apply to the directory number. |
| Park
                                             					 Monitoring Forward No Retrieve Internal CSS | Choose the
                                             					 calling search space to apply to the directory number. |
| Park
                                             					 Monitoring Reversion Timer | This
                                             					 parameter determines the number of seconds that Cisco Unified Communications Manager waits before
                                             					 prompting the user to retrieve a call that the user parked. This timer starts
                                             					 when the user presses the Park softkey on the phone, and a reminder is issued
                                             					 when the timer expires. Default:
                                             					 60 seconds If you
                                             					 configure a non-zero value, this value overrides the value of this parameter
                                             					 set in the Service Parameters window. However, if you configure
                                             					 a value of 0 here, then the value in the Service Parameters window will be
                                             					 used. |
| E164 | Always use
                                             					 a unique E.164 number. Do not use null value. |
| Voice Mail
                                             					 Profile | Enter this
                                             					 parameter to make the pilot number the same as the directory number for this
                                             					 line. This action proves useful if you do not have a voice-messaging server
                                             					 configured for this phone. |
| Line
                                             					 Calling Search Space | Enter
                                             					 partitions that are searched for numbers that are called from this directory
                                             					 number. Note Changes
                                                         						cause an update of the call pickup names that are listed in the Call Pickup Group field. The setting applies to all
                                                         						devices that are using this directory number. | Note | Changes
                                                         						cause an update of the call pickup names that are listed in the Call Pickup Group field. The setting applies to all
                                                         						devices that are using this directory number. |
| Note | Changes
                                                         						cause an update of the call pickup names that are listed in the Call Pickup Group field. The setting applies to all
                                                         						devices that are using this directory number. |
| AAR Group | Enter the
                                             					 automated alternate routing (AAR) group for this device. The AAR group provides
                                             					 the prefix digits that are used to route calls that are otherwise blocked due
                                             					 to insufficient bandwidth. Set AAR
                                             					 Group to <None> to prevent rerouting blocked calls. |
| Line User
                                             					 Hold Audio Source | Enter the
                                             					 music on hold audio source to be played when the user presses Hold and places a
                                             					 call on hold. |
| Line
                                             					 Network Hold Audio Source | Enter the
                                             					 music on hold audio source to be played when the system places a call on hold
                                             					 while the user transfers a call or initiates a conference or call park. |
| Auto
                                             					 Answer | Enter one
                                             					 of the following values to activate the Auto Answer feature for this directory
                                             					 number: Auto Answer Off
                                                						<Default> Auto Answer with Headset Auto Answer with
                                                						Speakerphone (Intercom) Note Make
                                                         						sure that the headset or speakerphone is not disabled when you choose Auto
                                                         						Answer with Headset or Auto Answer with Speakerphone. | Note | Make
                                                         						sure that the headset or speakerphone is not disabled when you choose Auto
                                                         						Answer with Headset or Auto Answer with Speakerphone. |
| Note | Make
                                                         						sure that the headset or speakerphone is not disabled when you choose Auto
                                                         						Answer with Headset or Auto Answer with Speakerphone. |
| No Answer
                                             					 Ring Duration (CFNA) | Enter the
                                             					 number of seconds to allow the call to ring before forwarding the call to the
                                             					 Forward No Answer Destination. |
| Call
                                             					 Pickup Group | Enter the
                                             					 Pickup Group Name to specify the call pickup group, which can answer incoming
                                             					 calls to this line by dialling the appropriate pickup group number. To use the
                                             					 BAT phone template entry, leave this field blank. |
| Target
                                             					 Destination (MLPP) | Enter the
                                             					 number to which MLPP precedence calls should be directed if this directory
                                             					 number receives a precedence call and neither this number nor its call forward
                                             					 destination answers the precedence call. Values can
                                             					 include numeric characters, pound ( # ) ,and asterisk ( * ). |
| Target CSS
                                             					 (MLPP) | From the
                                             					 drop-down list box, choose the calling search space to associate with the
                                             					 alternate party target (destination) number. |
| No Answer
                                             					 Ring Duration (MLPP) | Enter the
                                             					 number of seconds (between 4 and 30) after which an MLPP precedence call will
                                             					 be directed to this directory number’s alternate party if this directory number
                                             					 and its call forwarding destination have not answered the precedence call. Leave this
                                             					 setting blank to use the value that is set in the Cisco Unified
                                                						Communications Manager enterprise parameter, Precedence Alternate
                                             					 Party Timeout. |
| Line Text
                                             					 Label | Enter text
                                             					 that identifies this directory number for a line/phone combination. The
                                             					 default text specifies English |
| External
                                             					 Phone Number Mask | Enter the
                                             					 phone number (or mask) that is sent for Caller ID information when a call is
                                             					 placed from this line. You can
                                             					 enter a maximum of 30 numbers and "X" characters. The Xs represent the directory number and must appear at the end of
                                             					 the pattern. For example, if you specify a mask of 972813XXXX, an external call
                                             					 from extension 1234 displays a caller ID number of 9728131234. |
| Maximum
                                             					 Number of Calls | You can
                                             					 configure up to 200 calls for a line on a device in a cluster, with the
                                             					 limiting factor being the device. As you configure the number of calls for one
                                             					 line, the calls available for another line decrease. The
                                             					 default specifies 4. If the phone does not allow multiple calls for each line,
                                             					 the default specifies 2. For CTI
                                             					 route points, you can configure up to 10,000 calls for each port. The default
                                             					 specifies 5000 calls. Use this field in conjunction with the Busy Trigger
                                             					 field. |
| Busy
                                             					 Trigger | This
                                             					 setting, which works in conjunction with Maximum Number of Calls and Call
                                             					 Forward Busy, determines the maximum number of calls to be presented at the
                                             					 line. If maximum number of calls is set for 50 and the busy trigger is set to
                                             					 40, then incoming call 41 gets rejected with a busy cause (and will get
                                             					 forwarded if Call Forward Busy is set). If this line is shared, all the lines
                                             					 must be busy before incoming calls get rejected. Use this
                                             					 field in conjunction with Maximum Number of Calls for CTI route points. The
                                             					 default specifies 4500 calls. |
| Message
                                             					 Waiting Lamp Policy | Use this
                                             					 field to configure the handset lamp illumination policy. Choose one of the
                                             					 following options: Use System Policy (The
                                                						directory number refers to the service parameter "Message Waiting Lamp Policy" setting.) Light and Prompt Prompt Only Light Only None |
| Ring
                                             					 Setting (Phone Idle) | Choose the
                                             					 ring setting for the line appearance when an incoming call is received and no
                                             					 other active calls exist on that device. Choose one of the following options: Use system default Disable Flash only Ring once Ring Note The "Disable 
                                                            						" or "Flash only" setting options apply only for the handset.
                                                         						The led light on the phone button line will still flash. | Note | The "Disable 
                                                            						" or "Flash only" setting options apply only for the handset.
                                                         						The led light on the phone button line will still flash. |
| Note | The "Disable 
                                                            						" or "Flash only" setting options apply only for the handset.
                                                         						The led light on the phone button line will still flash. |
| Ring
                                             					 Setting (Phone Active) | Choose the
                                             					 ring setting that is used when this phone has another active call on a
                                             					 different line. Choose one of the following options: Use system default Disable Flash only Ring once Ring Beep only Note The "Disable 
                                                            						" or "Flash only" setting options apply only for the handset.
                                                         						The led light on the phone button line will still flash. | Note | The "Disable 
                                                            						" or "Flash only" setting options apply only for the handset.
                                                         						The led light on the phone button line will still flash. |
| Note | The "Disable 
                                                            						" or "Flash only" setting options apply only for the handset.
                                                         						The led light on the phone button line will still flash. |
| URI (1-5)
                                             					 on Directory Number | Enter a
                                             					 directory URI to associate with the directory number for this phone. Follow the
                                             					 username@host format. Enter a username of up to 47 alphanumeric characters. For
                                             					 the host address, enter an IPv4 address or fully qualified domain name. Note Within
                                                         						Cisco Unified CM Administration, you can enter directory URIs with embedded
                                                         						double quotes or commas. However, when you use Bulk Administration to import a
                                                         						csv file that contains directory URIs with embedded double quotes and commas,
                                                         						you must use enclose the entire directory URI in double quotes and escape the
                                                         						embedded double quotes with a double quote. For example, the Jared,
                                                         						"Jerry",Smith@test.com directory URI must be input as
                                                         						"Jared,""Jerry"",Smith@test.com" in the csv file. | Note | Within
                                                         						Cisco Unified CM Administration, you can enter directory URIs with embedded
                                                         						double quotes or commas. However, when you use Bulk Administration to import a
                                                         						csv file that contains directory URIs with embedded double quotes and commas,
                                                         						you must use enclose the entire directory URI in double quotes and escape the
                                                         						embedded double quotes with a double quote. For example, the Jared,
                                                         						"Jerry",Smith@test.com directory URI must be input as
                                                         						"Jared,""Jerry"",Smith@test.com" in the csv file. |
| Note | Within
                                                         						Cisco Unified CM Administration, you can enter directory URIs with embedded
                                                         						double quotes or commas. However, when you use Bulk Administration to import a
                                                         						csv file that contains directory URIs with embedded double quotes and commas,
                                                         						you must use enclose the entire directory URI in double quotes and escape the
                                                         						embedded double quotes with a double quote. For example, the Jared,
                                                         						"Jerry",Smith@test.com directory URI must be input as
                                                         						"Jared,""Jerry"",Smith@test.com" in the csv file. |
| URI (1-5)
                                             					 on Route Partition | Enter the
                                             					 partition on which the directory URI belongs. If you do not want to restrict
                                             					 access to the directory URI, leave the field blank |
| URI (1-5)
                                             					 Is Primary on Directory Number | Enter a
                                             					 ' t ' (True) to
                                             					 indicate that this directory URI is the primary directory URI for this
                                             					 extension. Otherwise, enter an ' f' (False) to indicate that this is not the primary
                                             					 directory URI for this extension. Note You can
                                                         						associate up to five directory URIs to a single directory number, but you must
                                                         						select a single primary directory URI. | Note | You can
                                                         						associate up to five directory URIs to a single directory number, but you must
                                                         						select a single primary directory URI. |
| Note | You can
                                                         						associate up to five directory URIs to a single directory number, but you must
                                                         						select a single primary directory URI. |

| Note | Changes
                                                         						cause an update of the call pickup names that are listed in the Call Pickup Group field. The setting applies to all
                                                         						devices that are using this directory number. |
|---|---|

| Note | Make
                                                         						sure that the headset or speakerphone is not disabled when you choose Auto
                                                         						Answer with Headset or Auto Answer with Speakerphone. |
|---|---|

| Note | The "Disable 
                                                            						" or "Flash only" setting options apply only for the handset.
                                                         						The led light on the phone button line will still flash. |
|---|---|

| Note | The "Disable 
                                                            						" or "Flash only" setting options apply only for the handset.
                                                         						The led light on the phone button line will still flash. |
|---|---|

| Note | Within
                                                         						Cisco Unified CM Administration, you can enter directory URIs with embedded
                                                         						double quotes or commas. However, when you use Bulk Administration to import a
                                                         						csv file that contains directory URIs with embedded double quotes and commas,
                                                         						you must use enclose the entire directory URI in double quotes and escape the
                                                         						embedded double quotes with a double quote. For example, the Jared,
                                                         						"Jerry",Smith@test.com directory URI must be input as
                                                         						"Jared,""Jerry"",Smith@test.com" in the csv file. |
|---|---|

| Note | You can
                                                         						associate up to five directory URIs to a single directory number, but you must
                                                         						select a single primary directory URI. |
|---|---|