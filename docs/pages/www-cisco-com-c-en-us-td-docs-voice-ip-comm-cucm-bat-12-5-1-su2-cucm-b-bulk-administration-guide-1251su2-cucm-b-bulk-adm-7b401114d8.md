---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-su2-cucm-b-bulk-administration-guide-1251su2-cucm-b-bulk-adm-7b401114d8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1_SU2/cucm_b_bulk-administration-guide-1251su2/cucm_b_bulk-administration-guide-1251su2_chapter_01010.html
retrieved_at: 2026-08-21T08:46:19.415585+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: February 3, 2020

Chapter: Phone Line Addition and Updates

## Chapter: Phone Line Addition and Updates

# Phone Line Addition and Updates

This chapter provides information to update line attributes for a specific group of devices or
                        		user device profiles using the Update Lines option. Lines for a phone and a user
                        		device profile get updated at the same time when both are part of the query
                        		result.

When a phone is deleted from the Cisco Unified Communications Manager database, the directory number remains in the
                                    		  database. To manage these orphan directory numbers, you can use the Update Lines option to search for unassigned directory
                                    		numbers and delete or update these directory numbers.

You can add lines to a group of existing phones or user device
                        		profiles in the Cisco Unified Communications Manager database. When you use the template to add new
                        		lines, you cannot change phone services or speed dials. Cisco Unified Communications Manager Bulk Administration (BAT) ignores those fields
                        		on the template when you add lines to existing devices.

## Update Phone Lines Using Query

You can update phone lines using query.

Choose Bulk
                                             				  Administration > Phones > Add/Update
                                             				  Lines > Update Lines or Bulk
                                             				  Administration > User Device
                                             				  Profiles > Add/Update Lines > Update
                                             				  Lines .

The Update Lines Query window displays.

You can update all lines by not specifying a query. Skip to Phone Line Update Field Descriptions .

From the first Find Line where drop-down list box, choose one
                                       			 of the following criteria:

- Directory Number

- Route Pattern

- Line Description

- Calling Search Space
                                             				  (Phone)

- Calling Search Space
                                             				  (Line)

- Device Pool

- Device Description

- Line Position

- Unassigned DN

To locate and delete orphaned directory numbers, use "unassigned DN."

From the second Find Line where drop-down list box, choose
                                          				one of the following criteria:

- begins with

- contains

- is exactly

- ends with

- is empty

- is not empty

In the search field list box, choose or enter the value that you
                                       			 want to locate.

### Example:

To find all lines that are registered in the database, click Find without entering any search text.

To further define your query and to add multiple filters, check
                                       			 the Search Within Results check box, choose AND or OR from the drop-down box, and repeat 2 and 3 .

To display the records that are going to be affected, click Find .

A list of discovered lines displays by

- Pattern/Directory
                                             				  Number

- Partition

- Description

Click Next .

If you want to change the type of query, click Back .

Specify the setting that you want to update for all the records
                                       			 that you have defined in your query.

In the Value field for the checked parameter, enter
                                       			 the new value or choose a value from the list box.

In the Job Information area, enter the Job
                                       			 description.

Choose an insert method. Do one of the following:

Click Run Immediately to insert lines
                                             				  immediately.

Click Run Later to insert at a later time.

To create a job for inserting the phone records, click Submit .

## Phone Line Update Field Descriptions

The following table provides the field descriptions for
                              		  updating line details.

Values that display in some fields display from Unified Communications Manager . You must configure these values by using Unified Communications Manager Administration.

Field

Description

Route Partition

Choose a partition. A partition indicates the route partition
                                          					 to which the directory number belongs.

The directory number can appear in more than one partition.

Calling Search Space (Line)

Choose the partitions that are searched for numbers that are
                                          					 called from this directory number.

Changes cause an update of the Pickup Group Names that are
                                                      						listed in the Call Pickup Group field. The setting
                                                      						applies to all devices that are using this directory number.

Calling Search Space Forward All

Choose the calling search space to use when a call is
                                          					 forwarded to the specified destination.

This setting applies to all devices that are using this
                                                      						directory number.

Forward All Destination

Enter the directory number to which all calls are forwarded.

This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number.

Forward All to Voice Mail

Check this check box to forward all calls to the number that
                                          					 you chose in the voice-messaging profile.

Checking this check box makes the values in the Forward All
                                          					 Destination field and Calling Search Space check box not relevant.

Calling Search Space Forward Busy External

Choose the calling search space to use when a call from an
                                          					 external number is forwarded to the specified destination.

This setting applies to all devices that are using this
                                                      						directory number.

Park Monitoring Forward No Retrieve Destination External

When the parkee is an external party, then the call will be
                                          					 forwarded to the specified destination in the parker'’s Park Monitoring Forward
                                          					 No Retrieve Destination External parameter. If the Forward No Retrieve Destination External field value is empty, the parkee will be redirected to the parker’s line.

Park Monitoring Forward No Retrieve Destination Internal

When the parkee is an internal party, then the call will be
                                          					 forwarded to the specified destination in the parker’s Park Monitoring Forward
                                          					 No Retrieve Destination Internal parameter. If the Forward No Retrieve Destination Internal is empty, the parkee will be redirected to the parker’s line.

Park Monitoring Forward No Retrieve Internal Voice Mail

Check this check box to use settings in the Voice Mail Profile Configuration window.

When this check box is checked, Unified Communications Manager ignores the settings in the Destination box and Calling Search Space.

Park Monitoring Forward No Retrieve External Voice Mail

Check this check box to use settings in the Voice Mail Profile
                                          					 Configuration window.

When this check box is checked, Unified Communications Manager ignores the settings in the Destination box and Calling Search Space.

Park Monitoring Forward No Retrieve External CSS

Choose the calling search space to apply to the directory
                                          					 number.

Park Monitoring Forward No Retrieve Internal CSS

Choose the calling search space to apply to the directory
                                          					 number.

Park Monitoring Reversion Timer

This parameter determines the number of seconds that Unified Communications Manager waits before prompting the user to retrieve a call that the user parked. This timer starts when the user presses the Park
                                          softkey on the phone, and a reminder is issued when the timer expires.

Default: 60 seconds

If you configure a non-zero value, this value overrides the
                                          					 value of this parameter set in the Service Parameters window. However, if you
                                          					 configure a value of 0 here, then the value in the Service Parameters window will be used.

Log Missed Calls

This check box allows you to turn this feature on or off. If the check box displays as checked (turned on), which is the default
                                          for this setting, Unified Communications Manager logs missed calls in the call history for that directory number on the phone.

Party Entrance Tone

Choose one of the following options from the drop-down list
                                          					 box:

- Default—Use the
                                             						value that you configured in the Party Entrance Tone service parameter.

- On—A tone plays on the phone when a basic call changes to a multi-party call; that is, a barge call, cBarge call, ad hoc conference,
                                             meet-me conference, or a joined call. In addition, a different tone plays when a party leaves the multi-party call. If the
                                             controlling device, that is, the originator of the multi-party call has a built-in bridge, the tone gets played to all parties
                                             if you choose On for the controlling device. When the controlling device, for example, the conference controller, is no longer
                                             present on the call or if the controlling device cannot play the tone, Unified Communications Manager does not play the tone even if you choose On.

- Off—A tone does
                                             						not play on the phone when a basic call changes to a multi-party call.

Calling Search Space Forward Busy Internal

Choose the calling search space to use when a call from an
                                          					 internal number is forwarded to the specified destination.

This setting applies to all devices that are using this
                                                      						directory number.

Forward Busy Destination External

Enter the directory number to which a call that is coming from
                                          					 an external number is forwarded when the line is in use.

This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number.

Forward Busy Destination Internal

Enter the directory number to which a call that is coming from
                                          					 an internal number is forwarded when the line is in use.

This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number.

Forward Busy to Voice Mail External

Check this check box to forward calls from an external number
                                          					 to the number that you chose in the voice-messaging profile when the line is in
                                          					 use.

Checking this check box makes the values in the Forward Busy Destination field and
                                          					 Calling Search Space check box not relevant.

Forward Busy to Voice Mail Internal

Check this check box to forward calls from an internal number
                                          					 to the number that you chose in the voice-messaging profile when the line is in
                                          					 use.

Checking this check box makes the values in the Forward Busy Destination field and
                                          					 Calling Search Space check box not relevant.

Calling Search Space Forward No Answer External

Choose the calling search space to use when a call from an
                                          					 external number is forwarded to the specified destination. The setting displays
                                          					 only if it is configured in the system.

This setting applies to all devices that are using this
                                                      						directory number.

Calling Search Space Forward No Answer Internal

Choose the calling search space to use when a call from an
                                          					 internal number is forwarded to the specified destination. The setting displays
                                          					 only if it is configured in the system.

This setting applies to all devices that are using this
                                                      						directory number.

Forward No Answer Destination External

Enter the directory number to which a call that is coming from
                                          					 an external number is forwarded when the phone is not answered.

This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number.

Forward No Answer Destination Internal

Enter the directory number to which a call that is coming from
                                          					 an internal number is forwarded when the phone is not answered.

This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number.

Forward No Answer to Voice Mail External

Check this check box to forward unanswered calls from an
                                          					 external number to the number that you chose in the voice-messaging profile.

Checking this check box makes the values in the Forward No Answer Destination field and
                                          					 Calling Search Space check box not relevant.

Forward No Answer to Voice Mail Internal

Check this check box to forward unanswered calls from an
                                          					 internal number to the number that you chose in the voice-messaging profile.

Checking this check box makes the values in the Forward No Answer Destination field and
                                          					 Calling Search Space check box not relevant.

Calling Search Space Forward No Coverage External

Choose the calling search space to use when a call from an
                                          					 external number is forwarded to the specified destination. The setting displays
                                          					 only if it is configured in the system.

This setting applies to all devices that are using this
                                                      						directory number.

Calling Search Space Forward No Coverage Internal

Choose the calling search space to use when a call from an
                                          					 internal number is forwarded to the specified destination. The setting displays
                                          					 only if it is configured in the system.

This setting applies to all devices that are using this
                                                      						directory number.

Forward No Coverage Destination External

Enter the directory number to which a call that is coming from
                                          					 an external number is forwarded when the phone does not have coverage.

This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number.

Forward No Coverage Destination Internal

Enter the directory number to which a call that is coming from
                                          					 an internal number is forwarded when the phone does not have coverage.

This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number.

Forward No Coverage to Voice Mail External

Check this check box to forward calls from an external number
                                          					 to the number that you chose in the voice-messaging profile when the phone does
                                          					 not have coverage.

Checking this check box makes the values in the Forward No Answer Destination field and
                                          					 Calling Search Space check box not relevant.

Forward No Coverage to Voice Mail Internal

Check this check box to forward calls from an external number
                                          					 to the number that you chose in the voice-messaging profile when the phone does
                                          					 not have coverage.

Checking this check box makes the values in the Forward No Answer Destination field and
                                          					 Calling Search Space check box not relevant.

Calling Search Space Forward on Failure External/Internal

(CTI ports only) Choose the calling search space to use when a
                                          					 call from an internal or external call is forwarded to the specified
                                          					 destination. The setting appears only if it is configured in the system.

This setting applies to all devices that are using this
                                                      						directory number.

Forward on Failure Destination External/Internal

(CTI ports only) Enter the directory number to which a call
                                          					 that is coming from an internal or an external number should be forwarded when
                                          					 a phone or CTI application fails.

Forward on Failure to Voice Mail External/Internal

(CTI ports only) Check this check box to forward failed calls
                                          					 from external or internal numbers to the number that you chose in the
                                          					 voice-messaging profile.

Call Forward No Answer Ring Duration

Enter the number of seconds (between 1 and 300) to allow the
                                          					 call to ring, before forwarding the call to the destination number that is
                                          					 entered in the Forward No Answer Destination field.

Leave this field blank to use the value that is set in the Unified Communications Manager service parameter, Forward No Answer Timer.

User Hold Audio Source

Choose the music on hold audio source that plays when the user
                                          					 presses the Hold button or softkey to put a call on
                                          					 hold.

Network Hold Audio Source

Choose the music on hold audio source that plays when the
                                          					 system places a call on hold such as when user transfers a call or initiates a
                                          					 conference or call park.

Auto Answer

Choose this parameter if you want all lines that are updated here to use the auto answer feature. With auto answer, Unified Communications Manager automatically answers calls when a headset is in use. A zip tone plays to alert the user that an incoming call connected.

Voice Mail Profile

Choose this parameter to make the pilot number the same as the
                                          					 directory number for this line. This choice proves useful if you do not have a
                                          					 voice-messaging server that is configured for this phone.

Ring Setting When Idle

Choose the type of ring for an incoming call on a phone.

Ring Setting when Active

Choose the type of ring for an incoming call on a phone, which
                                          					 is used when this phone has another active call on a different line.

Call Pickup Group Name

Choose a Pickup Group Name to specify the call pickup group,
                                          					 which can answer incoming calls to this directory number by dialing the
                                          					 appropriate pickup group number.

AAR Group

Choose the automated alternate routing (AAR) group for this
                                          					 device. The AAR group provides the prefix digits that are used to route calls
                                          					 that are otherwise blocked due to insufficient bandwidth.

To prevent rerouting blocked calls, set AAR Group to
                                          					 <None>.

Target (Destination)

Enter the number to which MLPP precedence calls should be
                                          					 directed if this directory number receives a precedence call and neither this
                                          					 number nor its call forward destination answers the precedence call.

Values can include numeric characters,
                                          					 pound( # ), and asterisk ( * ).

MLPP Calling Search Space

From the drop-down list box, choose the calling search space
                                          					 to associate with the alternate party target (destination) number.

MLPP No Answer Ring Duration

Enter the number of seconds (between 4 and 30) after which an
                                          					 MLPP precedence call will be directed to the alternate party for this directory
                                          					 number if this directory number and its call forwarding destination have not
                                          					 answered the precedence call.

Leave this setting blank to use the value that is set in the Unified Communications Manager enterprise parameter, Precedence Alternate Party Timeout.

External Phone Number Mask

Enter the phone number (or mask) that is sent for Caller ID
                                          					 information when a call is placed from this line.

You can enter a maximum of 30 numbers and "X" characters. The Xs represent the directory number and
                                          					 must appear at the end of the pattern. For example, if you specify a mask of
                                          					 972813XXXX, an external call from extension 1234 displays a caller ID number of
                                          					 9728131234.

Maximum Number of Calls

You can configure up to 184 calls for a line on a device in a
                                          					 cluster, with the limiting factor being the device. As you configure the number
                                          					 of calls for one line, the calls available for another line decrease.

The default specifies 4. If the phone does not allow multiple
                                          					 calls for each line, the default specifies 2.

For CTI route points, you can configure up to 10,000 calls for
                                          					 each port. The default specifies 5000 calls.

Use this field in conjunction with the Busy Trigger field.

Busy Trigger

This setting, which works in conjunction with Maximum Number
                                          					 of Calls and Call Forward Busy, determines the maximum number of calls to be
                                          					 presented at the line. If maximum number of calls is set for 50 and the busy
                                          					 trigger is set to 40, incoming call 41 gets rejected with a busy cause (and
                                          					 will get forwarded if Call Forward Busy is set). If this line is shared,
                                          					 incoming calls do not get rejected unless all the lines are busy.

Use this field in conjunction with Maximum Number of Calls for
                                          					 CTI route points. The default specifies 4500 calls.

## Add Phone Lines to Existing Phones and UDPs

You can add lines to exiting phones and UDP templates.

### Before you begin

- You must have a BAT
                                 			 template for this transaction.

- You must have a CSV data
                                 			 file for this transaction.

Choose Bulk Administration > Phones > Add/Update Lines > Add Lines .

In the File Name field, choose the CSV data file that
                                       			 you created for this bulk transaction.

In the Phone Template Name field, choose the BAT
                                       			 phone template to use for this bulk transaction.

If you are changing the phone settings for existing phones in the
                                       			 template, check the Update the existing phone button template check box.

In the Job Information area, enter the Job description.

Choose an insert method. Do one of the following:

Click Run Immediately to insert the phone
                                             				  records immediately.

Click Run Later to insert the phone records at a
                                             				  later time.

To create a job for adding lines to existing phones and UDPs,
                                       			 click Submit .

## Add Phone Lines to Existing Phones Using BAT Spreadsheet

You can create a CSV data file using the BAT spreadsheet to
                              		  add phone lines to existing phones.

After you have finished adding lines in the BAT spreadsheet, you can
                              		  export the content to a CSV formatted data file. A default filename is assigned
                              		  to the exported CSV formatted data file:

<tabname>-<timestamp>.txt

where <tabname> represents the type of input file that
                              		  you created, such as phones, and <timestamp> represents the precise date and time
                              		  that the file was created.

The system saves the file to C:\XLSDataFiles\ , or you can save the file to
                              		  another existing folder on your local workstation. You can rename the CSV
                              		  formatted data file after you save the exported file to your local workstation.
                              		  If you enter a comma in one of the fields, BAT.xlt encloses that field entry in
                              		  double quotes when you export to BAT format.

You cannot upload a CSV filename that contains a comma (for example, abcd,e.txt) to the Unified Communications Manager server.

If you enter a blank row in the spreadsheet, the system treats the
                                          			 empty row as the end of the file. Data that is entered after a blank line does
                                          			 not get converted to the BAT format.

To open the BAT Spreadsheet, locate and double-click the BAT.xlt
                                       			 file.

When prompted, click Enable Macros to use the spreadsheet
                                       			 capabilities.

To display the fields, click the Add Lines tab at the bottom of the
                                       			 spreadsheet.

Select the Phones radio button to add lines to a phone.

You can choose to add lines to a User Device Profile by
                                                      				  selecting the User Device Profile radio button.

Enter data for an individual phone on each line in the
                                       			 spreadsheet.

To transfer the data from the BAT Excel spreadsheet into a CSV
                                       			 formatted data file, click Export to BAT Format .

For information on how to read the exported CSV data file, click
                                                      				  the link to View Sample File in the Insert
                                                         					 phones window in BAT.

## Phone Line Field Descriptions for Line Additions Using BAT Spreadsheet

The following table provides the field descriptions when you
                              		  add lines using the BAT spreadsheet.

Field

Description

MAC Address

Enter the MAC address for phones, VGC virtual phones, and VGC
                                          					 phones. Enter a unique identifier for CTI ports and H.323 clients.

Line Index

Enter a number between 1 and 34 for the line index of a phone.

Directory Number

Enter a directory number, up to 24 numerals and special
                                          					 characters, for this line.

Display

Enter the text that you want to display on the called party’s
                                          					 phone display, such as the user name (John Smith) or phone location (Conference
                                          					 Room 1).

If this field is left blank the system uses the value that
                                                      						is entered in the Directory Number field.

The default language specifies English.

Line Text Label

Enter text that identifies this directory number for a
                                          					 line/phone combination.

The default language specifies English

Forward Busy External

Enter the directory number or directory URI to which a call that is coming from
                                          					 an external number is forwarded when the line is in use.

This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number.

Forward No Answer External

Enter the directory number or directory URI to which a call that is coming from
                                          					 an external number is forwarded when the phone is not answered.

This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number.

Forward No Coverage External

Enter the directory number or directory URI to which a call that is coming from
                                          					 an external number is forwarded when the phone does not have coverage.

This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number.

Forward Busy Internal

Enter the directory number or directory URI to which a call that is coming from
                                          					 an internal number is forwarded when the line is in use.

This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number.

Forward No Answer Internal

Enter the directory number or directory URI to which a call that is coming from
                                          					 an internal number is forwarded when the phone is not answered.

This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number.

Forward No Coverage Internal

Enter the directory number or directory URI to which a call that is coming from
                                          					 an internal number is forwarded when the phone does not have coverage.

This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number.

Call Pickup Group

Enter a Pickup Group Name to specify the call pickup group,
                                          					 which can answer incoming calls to this line by dialing the appropriate pickup
                                          					 group number.

Park Monitoring Forward No Retrieve Destination External

When the parkee is an external party, then the call will be
                                          					 forwarded to the specified destination in the parker’s Park Monitoring Forward
                                          					 No Retrieve Destination External parameter. If the Forward No Retrieve Destination External field value is empty, the parkee will be redirected to the parker’s line.

Park Monitoring Forward No Retrieve Destination Internal

When the parkee is an internal party, then the call will be
                                          					 forwarded to the specified destination in the parker’s Park Monitoring Forward
                                          					 No Retrieve Destination Internal parameter. If the Forward No Retrieve Destination Internal is empty, the parkee will be redirected to the parker’s line.

Park Monitoring Reversion Timer

This parameter determines the number of seconds that Unified Communications Manager waits before prompting the user to retrieve a call that the user parked. This timer starts when the user presses the Park softkey on the phone, and a reminder is issued when the timer expires.

Default: 60 seconds

If you configure a non-zero value, this value overrides the
                                          					 value of this parameter set in the Service Parameters window. However, if you
                                          					 configure a value of 0 here, then the value in the Service Parameters window
                                          					 will be used.

Park Monitoring Forward No Retrieve Internal Voice Mail

This setting uses the settings in the Voice Mail Profile Configuration window.

When this check box is checked, Unified Communications Manager ignores the settings in the Destination box and Calling Search Space.

Park Monitoring Forward No Retrieve External Voice Mail

This setting uses the settings in the Voice Mail Profile Configuration window.

When this check box is checked, Unified Communications Manager ignores the settings in the Destination box and Calling Search Space.

Park Monitoring Forward No Retrieve External CSS

Choose the calling search space to apply to the directory
                                          					 number.

Park Monitoring Forward No Retrieve Internal CSS

Choose the calling search space to apply to the directory
                                          					 number.

Log Missed Calls

This field allows you to turn this feature on or off. Enter ‘T’ to enable Unified Communications Manager to log missed calls in the call history for that directory number on the phone. Enter ‘F’ to disable this feature.

Party Entrance Tone

Enter one of the following Party Entrance Tone options:

- Default—Use the
                                             						value that you configured in the Party Entrance Tone service parameter.

- On—A tone plays on the phone when a basic call changes to a multi-party call; that is, a barge call, cBarge call, ad hoc conference,
                                             meet-me conference, or a joined call. In addition, a different tone plays when a party leaves the multi-party call. If the
                                             controlling device, that is, the originator of the multi-party call has a built-in bridge, the tone gets played to all parties
                                             if you choose On for the controlling device. When the controlling device, for example, the conference controller, is no longer
                                             present on the call or if the controlling device cannot play the tone, Unified Communications Manager does not play the tone even if you choose On.

- Off—A tone does
                                             						not play on the phone when a basic call changes to a multi-party call.

URI on Directory Number

Enter a directory URI that you want to associate with the directory number for this phone. Follow the username@host format.
                                          Enter a username of up to 47 alphanumeric characters. For the host address, enter an IPv4 address or fully qualified domain
                                          name.

You can associate up to five directory URIs to a single directory number, but you must select one primary directory URI.

URI Route Partition on Directory Number

Enter the partition on which the directory URI belongs. If you do not want to restrict access to the directory URI, leave
                                          the field blank.

URI Is Primary on Directory Number

Enter a ‘t’ (True) to indicate that this directory URI is the primary directory URI for this extension. Otherwise, enter an ‘f’ (False) to indicate that this is not the primary directory URI for this extension.

You can associate up to five directory URIs to a single directory number, but you must select one primary directory URI.

Enterprise Add to Local Route Partition

Enter a 't' to add this enterprise alternate number to a local route partition. Enter 'f' to leave the E.164 number off of
                                          local routing.

Enterprise Advertise via globally

Enter a 't' to enable ILS to advertise this alternate number to rest of the ILS network. Enter an 'f' if you don't want ILS
                                          to advertise this number.

Enterprise Is Urgent

Enter a 't' to classify routing for this alternate number as urgent.

By default, if the dial plan contains overlapping route patterns Unified Communications Manager does not route the call until
                                          the interdigit timer expires (even if a possible route exists for the dialed digits). This setting guards against learned
                                          numbers that overlap with statically configured directory numbers and number patterns by allowing Unified Communications Manager
                                          to choose the best match of all available routes for the dial string.

When you mark the number as urgent priority, Unified Communications Manager routes the call as soon as it finds a match between
                                          the dialed digits and an available route, without waiting for the interdigit timer to expire (for example, the T302 Timer
                                          service parameter).

Enterprise Number Mask

Enter the number mask to apply to the directory number. Unified Communications Manager applies the mask to create an enterprise
                                          alternate number that is an alias of this directory number.

Enterprise Route Partition

Enter the local route partition to which you want to assign this enterprise alternate number.

+E.164 Add to Local Route Partition

Enter a 't' to add this E.164 alternate number to a local route partition. Enter 'f' to leave the E.164 number off of local
                                          routing.

+E.164 Advertise via globally

Enter a 't' to enable ILS to advertise this alternate number to rest of the ILS network. Enter an 'f' if you don't want ILS
                                          to advertise this number.

+E.164 Is Urgent

Enter a 't' to classify routing for this alternate number as urgent.

By default, if the dial plan contains overlapping route patterns Unified Communications Manager does not route the call until
                                          the interdigit timer expires (even if a possible route exists for the dialed digits). This setting guards against learned
                                          numbers that overlap with statically configured directory numbers and number patterns by allowing Unified Communications Manager
                                          to choose the best match of all available routes for the dial string.

When you mark the number as urgent priority, Unified Communications Manager routes the call as soon as it finds a match between
                                          the dialed digits and an available route, without waiting for the interdigit timer to expire (for example, the T302 Timer
                                          service parameter).

+E.164 Number Mask

Enter the number mask to apply to the directory number. Unified Communications Manager applies the mask to create an +E.164
                                          alternate number that is an alias of this directory number.

+E.164 Route Partition

Enter the local route partition to which you want to assign this +E.164 alternate number.

| Note | When a phone is deleted from the Cisco Unified Communications Manager database, the directory number remains in the
                                    		  database. To manage these orphan directory numbers, you can use the Update Lines option to search for unassigned directory
                                    		numbers and delete or update these directory numbers. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Phones > Add/Update
                                             				  Lines > Update Lines or Bulk
                                             				  Administration > User Device
                                             				  Profiles > Add/Update Lines > Update
                                             				  Lines . The Update Lines Query window displays. Note You can update all lines by not specifying a query. Skip to Phone Line Update Field Descriptions . | Note | You can update all lines by not specifying a query. Skip to Phone Line Update Field Descriptions . |
|---|---|---|---|
| Note | You can update all lines by not specifying a query. Skip to Phone Line Update Field Descriptions . |
| Step 2 | From the first Find Line where drop-down list box, choose one
                                       			 of the following criteria: Directory Number Route Pattern Line Description Calling Search Space
                                             				  (Phone) Calling Search Space
                                             				  (Line) Device Pool Device Description Line Position Unassigned DN Call Pickup Group Note To locate and delete orphaned directory numbers, use "unassigned DN." From the second Find Line where drop-down list box, choose
                                          				one of the following criteria: begins with contains is exactly ends with is empty is not empty | Note | To locate and delete orphaned directory numbers, use "unassigned DN." |
| Note | To locate and delete orphaned directory numbers, use "unassigned DN." |
| Step 3 | In the search field list box, choose or enter the value that you
                                       			 want to locate. Example: You can choose the Route Partition from the list or enter a range
                                       			 of directory numbers. Tip To find all lines that are registered in the database, click Find without entering any search text. | Tip | To find all lines that are registered in the database, click Find without entering any search text. |
| Tip | To find all lines that are registered in the database, click Find without entering any search text. |
| Step 4 | To further define your query and to add multiple filters, check
                                       			 the Search Within Results check box, choose AND or OR from the drop-down box, and repeat 2 and 3 . |
| Step 5 | To display the records that are going to be affected, click Find . A list of discovered lines displays by Pattern/Directory
                                             				  Number Partition Description |
| Step 6 | Click Next . The Update Lines window shows the type of query that
                                       			 you chose at the top. Tip If you want to change the type of query, click Back . | Tip | If you want to change the type of query, click Back . |
| Tip | If you want to change the type of query, click Back . |
| Step 7 | Specify the setting that you want to update for all the records
                                       			 that you have defined in your query. You can choose multiple parameters to update. See Phone Line Update Field Descriptions for field descriptions. |
| Step 8 | In the Value field for the checked parameter, enter
                                       			 the new value or choose a value from the list box. |
| Step 9 | In the Job Information area, enter the Job
                                       			 description. |
| Step 10 | Choose an insert method. Do one of the following: Click Run Immediately to insert lines
                                             				  immediately. Click Run Later to insert at a later time. |
| Step 11 | To create a job for inserting the phone records, click Submit . To schedule this job, activate this job, or both, use the Job Configuration window. |

| Note | You can update all lines by not specifying a query. Skip to Phone Line Update Field Descriptions . |
|---|---|

| Note | To locate and delete orphaned directory numbers, use "unassigned DN." |
|---|---|

| Tip | To find all lines that are registered in the database, click Find without entering any search text. |
|---|---|

| Tip | If you want to change the type of query, click Back . |
|---|---|

| Field | Description |
|---|---|
| Route Partition | Choose a partition. A partition indicates the route partition
                                          					 to which the directory number belongs. Note The directory number can appear in more than one partition. | Note | The directory number can appear in more than one partition. |
| Note | The directory number can appear in more than one partition. |
| Calling Search Space (Line) | Choose the partitions that are searched for numbers that are
                                          					 called from this directory number. Note Changes cause an update of the Pickup Group Names that are
                                                      						listed in the Call Pickup Group field. The setting
                                                      						applies to all devices that are using this directory number. | Note | Changes cause an update of the Pickup Group Names that are
                                                      						listed in the Call Pickup Group field. The setting
                                                      						applies to all devices that are using this directory number. |
| Note | Changes cause an update of the Pickup Group Names that are
                                                      						listed in the Call Pickup Group field. The setting
                                                      						applies to all devices that are using this directory number. |
| Calling Search Space Forward All | Choose the calling search space to use when a call is
                                          					 forwarded to the specified destination. Note This setting applies to all devices that are using this
                                                      						directory number. | Note | This setting applies to all devices that are using this
                                                      						directory number. |
| Note | This setting applies to all devices that are using this
                                                      						directory number. |
| Forward All Destination | Enter the directory number to which all calls are forwarded. Note This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. | Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Forward All to Voice Mail | Check this check box to forward all calls to the number that
                                          					 you chose in the voice-messaging profile. Checking this check box makes the values in the Forward All
                                          					 Destination field and Calling Search Space check box not relevant. |
| Calling Search Space Forward Busy External | Choose the calling search space to use when a call from an
                                          					 external number is forwarded to the specified destination. Note This setting applies to all devices that are using this
                                                      						directory number. | Note | This setting applies to all devices that are using this
                                                      						directory number. |
| Note | This setting applies to all devices that are using this
                                                      						directory number. |
| Park Monitoring Forward No Retrieve Destination External | When the parkee is an external party, then the call will be
                                          					 forwarded to the specified destination in the parker'’s Park Monitoring Forward
                                          					 No Retrieve Destination External parameter. If the Forward No Retrieve Destination External field value is empty, the parkee will be redirected to the parker’s line. |
| Park Monitoring Forward No Retrieve Destination Internal | When the parkee is an internal party, then the call will be
                                          					 forwarded to the specified destination in the parker’s Park Monitoring Forward
                                          					 No Retrieve Destination Internal parameter. If the Forward No Retrieve Destination Internal is empty, the parkee will be redirected to the parker’s line. |
| Park Monitoring Forward No Retrieve Internal Voice Mail | Check this check box to use settings in the Voice Mail Profile Configuration window. When this check box is checked, Unified Communications Manager ignores the settings in the Destination box and Calling Search Space. |
| Park Monitoring Forward No Retrieve External Voice Mail | Check this check box to use settings in the Voice Mail Profile
                                          					 Configuration window. When this check box is checked, Unified Communications Manager ignores the settings in the Destination box and Calling Search Space. |
| Park Monitoring Forward No Retrieve External CSS | Choose the calling search space to apply to the directory
                                          					 number. |
| Park Monitoring Forward No Retrieve Internal CSS | Choose the calling search space to apply to the directory
                                          					 number. |
| Park Monitoring Reversion Timer | This parameter determines the number of seconds that Unified Communications Manager waits before prompting the user to retrieve a call that the user parked. This timer starts when the user presses the Park
                                          softkey on the phone, and a reminder is issued when the timer expires. Default: 60 seconds If you configure a non-zero value, this value overrides the
                                          					 value of this parameter set in the Service Parameters window. However, if you
                                          					 configure a value of 0 here, then the value in the Service Parameters window will be used. |
| Log Missed Calls | This check box allows you to turn this feature on or off. If the check box displays as checked (turned on), which is the default
                                          for this setting, Unified Communications Manager logs missed calls in the call history for that directory number on the phone. |
| Party Entrance Tone | Choose one of the following options from the drop-down list
                                          					 box: Default—Use the
                                             						value that you configured in the Party Entrance Tone service parameter. On—A tone plays on the phone when a basic call changes to a multi-party call; that is, a barge call, cBarge call, ad hoc conference,
                                             meet-me conference, or a joined call. In addition, a different tone plays when a party leaves the multi-party call. If the
                                             controlling device, that is, the originator of the multi-party call has a built-in bridge, the tone gets played to all parties
                                             if you choose On for the controlling device. When the controlling device, for example, the conference controller, is no longer
                                             present on the call or if the controlling device cannot play the tone, Unified Communications Manager does not play the tone even if you choose On. Off—A tone does
                                             						not play on the phone when a basic call changes to a multi-party call. |
| Calling Search Space Forward Busy Internal | Choose the calling search space to use when a call from an
                                          					 internal number is forwarded to the specified destination. Note This setting applies to all devices that are using this
                                                      						directory number. | Note | This setting applies to all devices that are using this
                                                      						directory number. |
| Note | This setting applies to all devices that are using this
                                                      						directory number. |
| Forward Busy Destination External | Enter the directory number to which a call that is coming from
                                          					 an external number is forwarded when the line is in use. Note This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. | Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Forward Busy Destination Internal | Enter the directory number to which a call that is coming from
                                          					 an internal number is forwarded when the line is in use. Note This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. | Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Forward Busy to Voice Mail External | Check this check box to forward calls from an external number
                                          					 to the number that you chose in the voice-messaging profile when the line is in
                                          					 use. Checking this check box makes the values in the Forward Busy Destination field and
                                          					 Calling Search Space check box not relevant. |
| Forward Busy to Voice Mail Internal | Check this check box to forward calls from an internal number
                                          					 to the number that you chose in the voice-messaging profile when the line is in
                                          					 use. Checking this check box makes the values in the Forward Busy Destination field and
                                          					 Calling Search Space check box not relevant. |
| Calling Search Space Forward No Answer External | Choose the calling search space to use when a call from an
                                          					 external number is forwarded to the specified destination. The setting displays
                                          					 only if it is configured in the system. Note This setting applies to all devices that are using this
                                                      						directory number. | Note | This setting applies to all devices that are using this
                                                      						directory number. |
| Note | This setting applies to all devices that are using this
                                                      						directory number. |
| Calling Search Space Forward No Answer Internal | Choose the calling search space to use when a call from an
                                          					 internal number is forwarded to the specified destination. The setting displays
                                          					 only if it is configured in the system. Note This setting applies to all devices that are using this
                                                      						directory number. | Note | This setting applies to all devices that are using this
                                                      						directory number. |
| Note | This setting applies to all devices that are using this
                                                      						directory number. |
| Forward No Answer Destination External | Enter the directory number to which a call that is coming from
                                          					 an external number is forwarded when the phone is not answered. Note This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. | Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Forward No Answer Destination Internal | Enter the directory number to which a call that is coming from
                                          					 an internal number is forwarded when the phone is not answered. Note This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. | Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Forward No Answer to Voice Mail External | Check this check box to forward unanswered calls from an
                                          					 external number to the number that you chose in the voice-messaging profile. Checking this check box makes the values in the Forward No Answer Destination field and
                                          					 Calling Search Space check box not relevant. |
| Forward No Answer to Voice Mail Internal | Check this check box to forward unanswered calls from an
                                          					 internal number to the number that you chose in the voice-messaging profile. Checking this check box makes the values in the Forward No Answer Destination field and
                                          					 Calling Search Space check box not relevant. |
| Calling Search Space Forward No Coverage External | Choose the calling search space to use when a call from an
                                          					 external number is forwarded to the specified destination. The setting displays
                                          					 only if it is configured in the system. Note This setting applies to all devices that are using this
                                                      						directory number. | Note | This setting applies to all devices that are using this
                                                      						directory number. |
| Note | This setting applies to all devices that are using this
                                                      						directory number. |
| Calling Search Space Forward No Coverage Internal | Choose the calling search space to use when a call from an
                                          					 internal number is forwarded to the specified destination. The setting displays
                                          					 only if it is configured in the system. Note This setting applies to all devices that are using this
                                                      						directory number. | Note | This setting applies to all devices that are using this
                                                      						directory number. |
| Note | This setting applies to all devices that are using this
                                                      						directory number. |
| Forward No Coverage Destination External | Enter the directory number to which a call that is coming from
                                          					 an external number is forwarded when the phone does not have coverage. Note This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. | Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Forward No Coverage Destination Internal | Enter the directory number to which a call that is coming from
                                          					 an internal number is forwarded when the phone does not have coverage. Note This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. | Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Forward No Coverage to Voice Mail External | Check this check box to forward calls from an external number
                                          					 to the number that you chose in the voice-messaging profile when the phone does
                                          					 not have coverage. Checking this check box makes the values in the Forward No Answer Destination field and
                                          					 Calling Search Space check box not relevant. |
| Forward No Coverage to Voice Mail Internal | Check this check box to forward calls from an external number
                                          					 to the number that you chose in the voice-messaging profile when the phone does
                                          					 not have coverage. Checking this check box makes the values in the Forward No Answer Destination field and
                                          					 Calling Search Space check box not relevant. |
| Calling Search Space Forward on Failure External/Internal | (CTI ports only) Choose the calling search space to use when a
                                          					 call from an internal or external call is forwarded to the specified
                                          					 destination. The setting appears only if it is configured in the system. Note This setting applies to all devices that are using this
                                                      						directory number. | Note | This setting applies to all devices that are using this
                                                      						directory number. |
| Note | This setting applies to all devices that are using this
                                                      						directory number. |
| Forward on Failure Destination External/Internal | (CTI ports only) Enter the directory number to which a call
                                          					 that is coming from an internal or an external number should be forwarded when
                                          					 a phone or CTI application fails. |
| Forward on Failure to Voice Mail External/Internal | (CTI ports only) Check this check box to forward failed calls
                                          					 from external or internal numbers to the number that you chose in the
                                          					 voice-messaging profile. |
| Call Forward No Answer Ring Duration | Enter the number of seconds (between 1 and 300) to allow the
                                          					 call to ring, before forwarding the call to the destination number that is
                                          					 entered in the Forward No Answer Destination field. Note Leave this field blank to use the value that is set in the Unified Communications Manager service parameter, Forward No Answer Timer. | Note | Leave this field blank to use the value that is set in the Unified Communications Manager service parameter, Forward No Answer Timer. |
| Note | Leave this field blank to use the value that is set in the Unified Communications Manager service parameter, Forward No Answer Timer. |
| User Hold Audio Source | Choose the music on hold audio source that plays when the user
                                          					 presses the Hold button or softkey to put a call on
                                          					 hold. |
| Network Hold Audio Source | Choose the music on hold audio source that plays when the
                                          					 system places a call on hold such as when user transfers a call or initiates a
                                          					 conference or call park. |
| Auto Answer | Choose this parameter if you want all lines that are updated here to use the auto answer feature. With auto answer, Unified Communications Manager automatically answers calls when a headset is in use. A zip tone plays to alert the user that an incoming call connected. |
| Voice Mail Profile | Choose this parameter to make the pilot number the same as the
                                          					 directory number for this line. This choice proves useful if you do not have a
                                          					 voice-messaging server that is configured for this phone. |
| Ring Setting When Idle | Choose the type of ring for an incoming call on a phone. |
| Ring Setting when Active | Choose the type of ring for an incoming call on a phone, which
                                          					 is used when this phone has another active call on a different line. |
| Call Pickup Group Name | Choose a Pickup Group Name to specify the call pickup group,
                                          					 which can answer incoming calls to this directory number by dialing the
                                          					 appropriate pickup group number. |
| AAR Group | Choose the automated alternate routing (AAR) group for this
                                          					 device. The AAR group provides the prefix digits that are used to route calls
                                          					 that are otherwise blocked due to insufficient bandwidth. To prevent rerouting blocked calls, set AAR Group to
                                          					 <None>. |
| Target (Destination) | Enter the number to which MLPP precedence calls should be
                                          					 directed if this directory number receives a precedence call and neither this
                                          					 number nor its call forward destination answers the precedence call. Values can include numeric characters,
                                          					 pound( # ), and asterisk ( * ). |
| MLPP Calling Search Space | From the drop-down list box, choose the calling search space
                                          					 to associate with the alternate party target (destination) number. |
| MLPP No Answer Ring Duration | Enter the number of seconds (between 4 and 30) after which an
                                          					 MLPP precedence call will be directed to the alternate party for this directory
                                          					 number if this directory number and its call forwarding destination have not
                                          					 answered the precedence call. Leave this setting blank to use the value that is set in the Unified Communications Manager enterprise parameter, Precedence Alternate Party Timeout. |
| External Phone Number Mask | Enter the phone number (or mask) that is sent for Caller ID
                                          					 information when a call is placed from this line. You can enter a maximum of 30 numbers and "X" characters. The Xs represent the directory number and
                                          					 must appear at the end of the pattern. For example, if you specify a mask of
                                          					 972813XXXX, an external call from extension 1234 displays a caller ID number of
                                          					 9728131234. |
| Maximum Number of Calls | You can configure up to 184 calls for a line on a device in a
                                          					 cluster, with the limiting factor being the device. As you configure the number
                                          					 of calls for one line, the calls available for another line decrease. The default specifies 4. If the phone does not allow multiple
                                          					 calls for each line, the default specifies 2. For CTI route points, you can configure up to 10,000 calls for
                                          					 each port. The default specifies 5000 calls. Use this field in conjunction with the Busy Trigger field. |
| Busy Trigger | This setting, which works in conjunction with Maximum Number
                                          					 of Calls and Call Forward Busy, determines the maximum number of calls to be
                                          					 presented at the line. If maximum number of calls is set for 50 and the busy
                                          					 trigger is set to 40, incoming call 41 gets rejected with a busy cause (and
                                          					 will get forwarded if Call Forward Busy is set). If this line is shared,
                                          					 incoming calls do not get rejected unless all the lines are busy. Use this field in conjunction with Maximum Number of Calls for
                                          					 CTI route points. The default specifies 4500 calls. |

| Note | The directory number can appear in more than one partition. |
|---|---|

| Note | Changes cause an update of the Pickup Group Names that are
                                                      						listed in the Call Pickup Group field. The setting
                                                      						applies to all devices that are using this directory number. |
|---|---|

| Note | This setting applies to all devices that are using this
                                                      						directory number. |
|---|---|

| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
|---|---|

| Note | This setting applies to all devices that are using this
                                                      						directory number. |
|---|---|

| Note | This setting applies to all devices that are using this
                                                      						directory number. |
|---|---|

| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
|---|---|

| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
|---|---|

| Note | This setting applies to all devices that are using this
                                                      						directory number. |
|---|---|

| Note | This setting applies to all devices that are using this
                                                      						directory number. |
|---|---|

| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
|---|---|

| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
|---|---|

| Note | This setting applies to all devices that are using this
                                                      						directory number. |
|---|---|

| Note | This setting applies to all devices that are using this
                                                      						directory number. |
|---|---|

| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
|---|---|

| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
|---|---|

| Note | This setting applies to all devices that are using this
                                                      						directory number. |
|---|---|

| Note | Leave this field blank to use the value that is set in the Unified Communications Manager service parameter, Forward No Answer Timer. |
|---|---|

| Step 1 | Choose Bulk Administration > Phones > Add/Update Lines > Add Lines . The Phone Add Lines window displays. |
|---|---|
| Step 2 | In the File Name field, choose the CSV data file that
                                       			 you created for this bulk transaction. |
| Step 3 | In the Phone Template Name field, choose the BAT
                                       			 phone template to use for this bulk transaction. |
| Step 4 | If you are changing the phone settings for existing phones in the
                                       			 template, check the Update the existing phone button template check box. The user phone information also gets updated when this check box
                                       			 is checked. |
| Step 5 | In the Job Information area, enter the Job description. |
| Step 6 | Choose an insert method. Do one of the following: Click Run Immediately to insert the phone
                                             				  records immediately. Click Run Later to insert the phone records at a
                                             				  later time. |
| Step 7 | To create a job for adding lines to existing phones and UDPs,
                                       			 click Submit . To schedule, this job, activate this job, or both, use the Job Configuration window. |

| Note | You cannot upload a CSV filename that contains a comma (for example, abcd,e.txt) to the Unified Communications Manager server. If you enter a blank row in the spreadsheet, the system treats the
                                          			 empty row as the end of the file. Data that is entered after a blank line does
                                          			 not get converted to the BAT format. |
|---|---|

| Step 1 | To open the BAT Spreadsheet, locate and double-click the BAT.xlt
                                       			 file. |
|---|---|
| Step 2 | When prompted, click Enable Macros to use the spreadsheet
                                       			 capabilities. |
| Step 3 | To display the fields, click the Add Lines tab at the bottom of the
                                       			 spreadsheet. |
| Step 4 | Select the Phones radio button to add lines to a phone. Note You can choose to add lines to a User Device Profile by
                                                      				  selecting the User Device Profile radio button. | Note | You can choose to add lines to a User Device Profile by
                                                      				  selecting the User Device Profile radio button. |
| Note | You can choose to add lines to a User Device Profile by
                                                      				  selecting the User Device Profile radio button. |
| Step 5 | Enter data for an individual phone on each line in the
                                       			 spreadsheet. Complete all mandatory fields and any relevant optional fields.
                                       			 Each column heading specifies the length of the field and whether it is
                                       			 required or optional. See Table 1 for field descriptions. |
| Step 6 | To transfer the data from the BAT Excel spreadsheet into a CSV
                                       			 formatted data file, click Export to BAT Format . Tip For information on how to read the exported CSV data file, click
                                                      				  the link to View Sample File in the Insert
                                                         					 phones window in BAT. The system saves the file to C:\XLSDataFiles\ with the default filename <tabname>-<timestamp>.txt , or you can
                                       			 use Browse to save the file to another existing folder
                                       			 on your local workstation. | Tip | For information on how to read the exported CSV data file, click
                                                      				  the link to View Sample File in the Insert
                                                         					 phones window in BAT. |
| Tip | For information on how to read the exported CSV data file, click
                                                      				  the link to View Sample File in the Insert
                                                         					 phones window in BAT. |

| Note | You can choose to add lines to a User Device Profile by
                                                      				  selecting the User Device Profile radio button. |
|---|---|

| Tip | For information on how to read the exported CSV data file, click
                                                      				  the link to View Sample File in the Insert
                                                         					 phones window in BAT. |
|---|---|

| Field | Description |
|---|---|
| MAC Address | Enter the MAC address for phones, VGC virtual phones, and VGC
                                          					 phones. Enter a unique identifier for CTI ports and H.323 clients. |
| Line Index | Enter a number between 1 and 34 for the line index of a phone. |
| Directory Number | Enter a directory number, up to 24 numerals and special
                                          					 characters, for this line. |
| Display | Enter the text that you want to display on the called party’s
                                          					 phone display, such as the user name (John Smith) or phone location (Conference
                                          					 Room 1). Note If this field is left blank the system uses the value that
                                                      						is entered in the Directory Number field. Note The default language specifies English. | Note | If this field is left blank the system uses the value that
                                                      						is entered in the Directory Number field. | Note | The default language specifies English. |
| Note | If this field is left blank the system uses the value that
                                                      						is entered in the Directory Number field. |
| Note | The default language specifies English. |
| Line Text Label | Enter text that identifies this directory number for a
                                          					 line/phone combination. Note The default language specifies English | Note | The default language specifies English |
| Note | The default language specifies English |
| Forward Busy External | Enter the directory number or directory URI to which a call that is coming from
                                          					 an external number is forwarded when the line is in use. Note This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. | Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Forward No Answer External | Enter the directory number or directory URI to which a call that is coming from
                                          					 an external number is forwarded when the phone is not answered. Note This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. | Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Forward No Coverage External | Enter the directory number or directory URI to which a call that is coming from
                                          					 an external number is forwarded when the phone does not have coverage. Note This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. | Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Forward Busy Internal | Enter the directory number or directory URI to which a call that is coming from
                                          					 an internal number is forwarded when the line is in use. Note This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. | Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Forward No Answer Internal | Enter the directory number or directory URI to which a call that is coming from
                                          					 an internal number is forwarded when the phone is not answered. Note This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. | Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Forward No Coverage Internal | Enter the directory number or directory URI to which a call that is coming from
                                          					 an internal number is forwarded when the phone does not have coverage. Note This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. | Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Call Pickup Group | Enter a Pickup Group Name to specify the call pickup group,
                                          					 which can answer incoming calls to this line by dialing the appropriate pickup
                                          					 group number. |
| Park Monitoring Forward No Retrieve Destination External | When the parkee is an external party, then the call will be
                                          					 forwarded to the specified destination in the parker’s Park Monitoring Forward
                                          					 No Retrieve Destination External parameter. If the Forward No Retrieve Destination External field value is empty, the parkee will be redirected to the parker’s line. |
| Park Monitoring Forward No Retrieve Destination Internal | When the parkee is an internal party, then the call will be
                                          					 forwarded to the specified destination in the parker’s Park Monitoring Forward
                                          					 No Retrieve Destination Internal parameter. If the Forward No Retrieve Destination Internal is empty, the parkee will be redirected to the parker’s line. |
| Park Monitoring Reversion Timer | This parameter determines the number of seconds that Unified Communications Manager waits before prompting the user to retrieve a call that the user parked. This timer starts when the user presses the Park softkey on the phone, and a reminder is issued when the timer expires. Default: 60 seconds If you configure a non-zero value, this value overrides the
                                          					 value of this parameter set in the Service Parameters window. However, if you
                                          					 configure a value of 0 here, then the value in the Service Parameters window
                                          					 will be used. |
| Park Monitoring Forward No Retrieve Internal Voice Mail | This setting uses the settings in the Voice Mail Profile Configuration window. When this check box is checked, Unified Communications Manager ignores the settings in the Destination box and Calling Search Space. |
| Park Monitoring Forward No Retrieve External Voice Mail | This setting uses the settings in the Voice Mail Profile Configuration window. When this check box is checked, Unified Communications Manager ignores the settings in the Destination box and Calling Search Space. |
| Park Monitoring Forward No Retrieve External CSS | Choose the calling search space to apply to the directory
                                          					 number. |
| Park Monitoring Forward No Retrieve Internal CSS | Choose the calling search space to apply to the directory
                                          					 number. |
| Log Missed Calls | This field allows you to turn this feature on or off. Enter ‘T’ to enable Unified Communications Manager to log missed calls in the call history for that directory number on the phone. Enter ‘F’ to disable this feature. |
| Party Entrance Tone | Enter one of the following Party Entrance Tone options: Default—Use the
                                             						value that you configured in the Party Entrance Tone service parameter. On—A tone plays on the phone when a basic call changes to a multi-party call; that is, a barge call, cBarge call, ad hoc conference,
                                             meet-me conference, or a joined call. In addition, a different tone plays when a party leaves the multi-party call. If the
                                             controlling device, that is, the originator of the multi-party call has a built-in bridge, the tone gets played to all parties
                                             if you choose On for the controlling device. When the controlling device, for example, the conference controller, is no longer
                                             present on the call or if the controlling device cannot play the tone, Unified Communications Manager does not play the tone even if you choose On. Off—A tone does
                                             						not play on the phone when a basic call changes to a multi-party call. |
| URI on Directory Number | Enter a directory URI that you want to associate with the directory number for this phone. Follow the username@host format.
                                          Enter a username of up to 47 alphanumeric characters. For the host address, enter an IPv4 address or fully qualified domain
                                          name. Note You can associate up to five directory URIs to a single directory number, but you must select one primary directory URI. | Note | You can associate up to five directory URIs to a single directory number, but you must select one primary directory URI. |
| Note | You can associate up to five directory URIs to a single directory number, but you must select one primary directory URI. |
| URI Route Partition on Directory Number | Enter the partition on which the directory URI belongs. If you do not want to restrict access to the directory URI, leave
                                          the field blank. |
| URI Is Primary on Directory Number | Enter a ‘t’ (True) to indicate that this directory URI is the primary directory URI for this extension. Otherwise, enter an ‘f’ (False) to indicate that this is not the primary directory URI for this extension. Note You can associate up to five directory URIs to a single directory number, but you must select one primary directory URI. | Note | You can associate up to five directory URIs to a single directory number, but you must select one primary directory URI. |
| Note | You can associate up to five directory URIs to a single directory number, but you must select one primary directory URI. |
| Enterprise Add to Local Route Partition | Enter a 't' to add this enterprise alternate number to a local route partition. Enter 'f' to leave the E.164 number off of
                                          local routing. |
| Enterprise Advertise via globally | Enter a 't' to enable ILS to advertise this alternate number to rest of the ILS network. Enter an 'f' if you don't want ILS
                                          to advertise this number. |
| Enterprise Is Urgent | Enter a 't' to classify routing for this alternate number as urgent. By default, if the dial plan contains overlapping route patterns Unified Communications Manager does not route the call until
                                          the interdigit timer expires (even if a possible route exists for the dialed digits). This setting guards against learned
                                          numbers that overlap with statically configured directory numbers and number patterns by allowing Unified Communications Manager
                                          to choose the best match of all available routes for the dial string. When you mark the number as urgent priority, Unified Communications Manager routes the call as soon as it finds a match between
                                          the dialed digits and an available route, without waiting for the interdigit timer to expire (for example, the T302 Timer
                                          service parameter). |
| Enterprise Number Mask | Enter the number mask to apply to the directory number. Unified Communications Manager applies the mask to create an enterprise
                                          alternate number that is an alias of this directory number. |
| Enterprise Route Partition | Enter the local route partition to which you want to assign this enterprise alternate number. |
| +E.164 Add to Local Route Partition | Enter a 't' to add this E.164 alternate number to a local route partition. Enter 'f' to leave the E.164 number off of local
                                          routing. |
| +E.164 Advertise via globally | Enter a 't' to enable ILS to advertise this alternate number to rest of the ILS network. Enter an 'f' if you don't want ILS
                                          to advertise this number. |
| +E.164 Is Urgent | Enter a 't' to classify routing for this alternate number as urgent. By default, if the dial plan contains overlapping route patterns Unified Communications Manager does not route the call until
                                          the interdigit timer expires (even if a possible route exists for the dialed digits). This setting guards against learned
                                          numbers that overlap with statically configured directory numbers and number patterns by allowing Unified Communications Manager
                                          to choose the best match of all available routes for the dial string. When you mark the number as urgent priority, Unified Communications Manager routes the call as soon as it finds a match between
                                          the dialed digits and an available route, without waiting for the interdigit timer to expire (for example, the T302 Timer
                                          service parameter). |
| +E.164 Number Mask | Enter the number mask to apply to the directory number. Unified Communications Manager applies the mask to create an +E.164
                                          alternate number that is an alias of this directory number. |
| +E.164 Route Partition | Enter the local route partition to which you want to assign this +E.164 alternate number. |

| Note | If this field is left blank the system uses the value that
                                                      						is entered in the Directory Number field. |
|---|---|

| Note | The default language specifies English. |
|---|---|

| Note | The default language specifies English |
|---|---|

| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
|---|---|

| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
|---|---|

| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
|---|---|

| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
|---|---|

| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
|---|---|

| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
|---|---|

| Note | You can associate up to five directory URIs to a single directory number, but you must select one primary directory URI. |
|---|---|

| Note | You can associate up to five directory URIs to a single directory number, but you must select one primary directory URI. |
|---|---|