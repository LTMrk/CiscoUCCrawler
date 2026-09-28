---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-14su1-cucm-b-bulk-administration-guide-14su1-cucm-b-bulk-administra-c66f37a34b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/14SU1/cucm_b_bulk-administration-guide-14SU1/cucm_b_bulk-administration-guide-1251su2_chapter_011.html
retrieved_at: 2026-08-21T09:08:02.528590+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: October 27, 2021

Chapter: Phone Template

## Chapter: Phone Template

# Phone Template

Cisco Unified Communications Manager Bulk Administration (BAT) gives the
                        		administrator a fast and efficient way to add, update, or delete large numbers
                        		of phones in batches, rather than performing individual updates through Cisco Unified Communications Manager Administration. You can use BAT to work with
                        		the following types of phones:

CiscoUnifiedIPPhones (all models)

CTI ports

H.323 clients

This chapter provides information about how to use BAT to work with
                        		phone templates and other IP telephony devices.

## Add Phones to Database

When you use BAT to add phones and other IP telephony devices in bulk to the Unified Communications Manager database, you can add multiple lines, services, and speed dials for each phone. You can also add CTI ports and H.323 clients.

- Use the BAT spreadsheet (BAT.xlt) and export the data to the CSV format

- Use a text editor to create a text file in CSV format (for experienced users)

Step 1

Choose Bulk
                                             				  Administration > Phones > Phone
                                             				  Template .

The Find and List Phone Templates window displays.

Step 2

Create a CSV data file to insert the phone templates.

Perform one of the following options:

Create a CSV data file using the BAT spreadsheet.

Create a CSV data file using a text editor as follows:

- Choose Bulk Administration > Phones > Phone File Format > Create File Format .

- Use a text editor
                                                   						and create the CSV data file for phones that follows the file format that you
                                                   						want to use.

- Choose Bulk
                                                         							 Administration > Phones > Phone File
                                                         							 Format > Add File Format to associate the text-based file format with the CSV data file.

Step 3

Choose Bulk
                                             				  Administration > Phones > Validate
                                             				  Phones .

Step 4

Choose Bulk Administration > phones > Insert phones to insert phone records into the Unified Communications Manager database.

## BAT Phone Templates

Use BAT phone templates to define the common phone attributes to add a group of new phones. Prior to creating the template,
                           make sure phone settings such as device pool, location, calling search space, button template and softkey templates have already
                           been configured in Unified Communications Manager Administration. You cannot create new settings in BAT.

### Find BAT Phone Template

Because you might have several phone templates, Unified Communications Manager lets you locate specific phone templates on the basis of criteria that you define.

During your work in a browser session, your find/list search preferences are stored in the cookies on the client machine.
                                             If you navigate to other menu items and return to this menu item, or if you close the browser and then reopen a new browser
                                             window, your Unified Communications Manager search preferences are retained until you modify your search.

Step 1

Choose Bulk
                                                				  Administration > Phones > Phone
                                                				  Template .

The Find and List Phone Templates window displays.
                                             				Use the two drop-down list boxes to search for a template.

Step 2

From the first Find Phone Templates where drop-down list box,
                                          			 choose one of the following criteria:

- Device
                                                				  Name

- Description

- Directory Number

- Directory URI

- Calling
                                                				  Search Space

- Device
                                                				  Pool

- Device
                                                				  Type

- Call
                                                				  Pickup Group

- LSC
                                                				  Status

- Authentication
                                                				  String

- Device
                                                				  Protocol

- Security
                                                				  Profile

- Common
                                                				  Device Configuration

Step 3

From the second Find Phone Template where drop-down list box,
                                          			 choose one of the following criteria:

- begins
                                                				  with

- contains

- is
                                                				  exactly

- ends
                                                				  with

- is
                                                				  empty

- is not
                                                				  empty

Step 4

Specify the appropriate search text, if applicable, and click Find .

Tip

To find all Phone Templates that are registered in the database,
                                                         				  click Find without entering any search text.

Step 5

From the list of records, click the device name that matches your
                                          			 search criteria.

### Create New BAT Phone Template

You can create new BAT phone templates. After you create a
                                 		  phone template, you can add lines, services, and speed dials.

Step 1

Choose Bulk
                                                				  Administration > Phones > Phone
                                                				  Template .

Step 2

Click Add New . The Add a New Phone Template window displays.

Step 3

From the Phone Type drop-down list, choose the phone model for which you are creating the template. Click Next .

Step 4

From the Select the Device Protocol drop-down list, choose the device protocol. Click Next .

The Phone Template Configuration window displays with fields and default entries for the chosen device type.

Step 5

In the Template Name field, enter a name for the
                                          			 template.

Step 6

In the Device Information area, enter the phone settings that this
                                          			 batch has in common.

Step 7

After you have entered all the settings for this BAT phone
                                          			 template, click Save .

#### Add or Update Phone Lines in BAT Template

You can add one or more lines to the BAT template or to update existing lines. The button template in use for the BAT template
                                    determines the number of lines that you can add or update. You can create a primary phone template that has multiple lines.
                                    Then, you can use the standard template to add phones with a single line or up to the number of lines in the standard template.
                                    All phones or user device profiles in this batch will use the settings that you choose.

Cisco recommends that you use alphanumeric characters for the line
                                    		  template value, so if numbers are given, a chance exists of this conflicting
                                    		  with an actual directory number. This would also avoid conflicts with features
                                    		  such as Call Pickup group number and Call Park number.

The maximum number of lines that display for a BAT template depends on
                                    		  the model and button template that you chose when you created the BAT phone
                                    		  template. For some CiscoUnifiedIPPhone models, you can also add
                                    		  CiscoUnifiedIPPhone services and speed dials to the template.

Step 1

Find the Phone Template to which you want to add the line.

Step 2

In the Phone Template Configuration window,
                                             			 click Line [1] Add a new DN , in the Associated Information area.

Step 3

Enter or choose the appropriate values for the line settings.

Step 4

Click Save .

Step 5

To add settings for any additional lines, repeat Step 2 through Step 4 .

To find existing line template, enter the appropriate search
                                                   				  criteria and click Find .

To add a new line template, click Add New .

#### Add or Update IP Services in BAT Template

You can subscribe CiscoUnifiedIPPhone services to the
                                    		  CiscoUnifiedIPPhone models that include this feature directly in the BAT
                                    		  template. To bulk subscribe users or phones to IP services, the IP services
                                    		  must have common service parameters and be subscribed through a phone template.
                                    		  You can not bulk subscribe IP services that have unique service parameters. For
                                    		  services with unique parameters, use the CSV file.

Step 1

Find the Phone Template to which you want add an IP service.

Step 2

From the Phone Template Configuration window,
                                             			 click Add a new SURL in the Associated Information area.

Step 3

In the Select a Service drop-down list box, choose a
                                             			 service to which you want all phones to be subscribed. The Service Description box displays details about
                                             			 the service that you choose.

Step 4

Click Next .

Step 5

In the Service Name field, modify the name of the
                                             			 service, if required.

Step 6

Associate the selected services or add more services to the
                                             			 template.

To associate these phone services to the phone template, click Save .

To add more services, repeat Step 3 through Step 6 .

To add all the services to the template, click Update .

Step 7

Close the popup window.

#### Add or Update Speed Dials in BAT Template

You can add and update speed dials in the BAT template for
                                    		  phones and Cisco VGC phones if the Phone Button Template provides speed-dial
                                    		  buttons. The Phone Button Template in use for the BAT template determines the
                                    		  number of available speed-dial buttons.

Step 1

Find the Phone Template to which you want to add speed dials.

Step 2

From the Phone Template Configuration window, do one of
                                             			 the following:

Click Add a new SD in the Associated Information area.

Choose Add/Update Speed Dials from the Related Links drop-down list box in the
                                                   				  upper, right-hand corner of the window.

Step 3

In the Speed Dial Settings area, enter the phone
                                             			 number, including any access or long-distance codes, in the Number field.

When you enter the phone number, it can be followed by Forced Authorized Code (FAC)/Client Matter Code (CMC) if applicable.
                                                            You can enter the Phone number, FAC, CMC either in sequence or separated by a comma (,). The Speed dial may include any PIN,
                                                            Password or any other digits to be sent as DTMF digits after the call is connected. If you require a pause while connecting
                                                            through speed dial, you can enter one or more comma (,) where each comma represents a pause of 2 seconds. DTMF digits will
                                                            be sent after the call is connected and the appropriate pause duration corresponding to the number of commas is entered.

Step 4

In the Label field, enter a label that corresponds to
                                             			 the speed-dial number.

Step 5

In the Abbreviated Dial Settings area, you can set
                                             			 abbreviated speed dials for applicable IP phone models. Repeat Step 3 .

Step 6

Click Save .

#### Add or Update Busy Lamp Field in BAT Template

You can add and update busy lamp filed speed dials in the
                                    		  BAT template for phones and Cisco VGC phones if the Phone Button Template
                                    		  provides speed-dial buttons. The Phone Button Template in use for the BAT
                                    		  template determines the number of available BLF SD buttons.

Step 1

Find the Phone Template to which you want to add speed dials.

Step 2

In the Phone Template Configuration window, do one of
                                             			 the following:

Click Add a new BLF SD in the Associated Information area.

Choose Add/Update Busy Lamp Field Speed Dials from the Related Links drop-down list in the upper, right-hand corner of the window.

Step 3

In the Speed Dial Settings area, enter the destination,
                                             			 including any access or long-distance codes, in the Destination field.

Step 4

Choose the directory number from the drop-down list. You can click Find to search for directory numbers.

Step 5

In the Label field, enter a label that corresponds to
                                             			 the BLF SD number.

Step 6

Click Save .

#### Add or Update Busy Lamp Field Directed Call Park in BAT Template

You can add and update busy lamp field (BLF) directed call
                                    		  park in the BAT template for phones and Cisco VGC phones if the Phone Button
                                    		  Template provides speed-dial buttons. The Phone Button Template in use for this
                                    		  BAT template determines the number of available BLF Directed Call Park buttons.

Step 1

Find the Phone Template to which you want to add BLF speed
                                             			 directed call park.

Step 2

In the Phone Template Configuration window, do one of
                                             			 the following:

Click Add a new BLF Directed Call Park in the Associated Information area.

Choose Add/Update BLF Directed Call Park from the Related Links drop-down list box in the
                                                   				  upper, right-hand corner of the window.

Step 3

In the Unassigned Busy Lamp Field/Directed Call Park Settings area, choose the directory number from the drop-down list. You can click Find to search for directory numbers.

Step 4

In the Label field, enter a label that corresponds to
                                             			 the BLF Directed Call Park number.

Step 5

Click Save .

#### Add or Update Intercom Template in BAT Template

You can add one or more Intercom templates to the BAT template, or update existing Intercom templates in the BAT template
                                    The button template in use for the BAT template determines the number of lines that you can add or update. You can create
                                    a standard phone template that has multiple lines. Then, you can use the standard template to add phones with a single line
                                    or up to the number of lines in the standard template. All phones or user device profiles in this batch will use the settings
                                    that you choose for the intercom template.

We recommend that you use alphanumeric characters for intercom template, so if numbers are given, a chance exists of this
                                    conflicting with an actual directory number. This would also avoid conflicts with features such as Call Pickup group number
                                    and Call Park number.

The maximum number of lines that display for a BAT template depends on
                                    		  model and button template that you chose when you created the BAT phone
                                    		  template. For some CiscoUnifiedIPPhone models, you can also add
                                    		  CiscoUnifiedIPPhone services and speed dials to the template.

Step 1

Find the Phone Template to which you want to add the intercom
                                             			 template.

Step 2

In the Phone Template Configuration window, click Intercom [1] - Add a new Intercom in the Associated Information area.

Step 3

Enter or choose the appropriate values for the intercom template
                                             			 settings.

Step 4

Click Save .

Step 5

To add settings for any additional intercom templates, repeat Step 2 through Step 4 .

Click Find and enter the appropriate search criteria and to find existing Intercom directory numbers.

In the Find and List Intercom Directory Number window, click Add New to add a new intercom directory number.

### Modify BAT Phone Templates

Step 1

Find the Phone Template that you want to modify.

Step 2

In the phone Template Configuration window, add, change, or
                                          			 remove settings in the template. See Table 1 for more information.

Step 3

After you have modified the settings to update the template, click Save .

#### What to do next

You can proceed to add or update lines, IP services, or speed dials
                                 		  for the BAT template.

### Copy BAT Phone Template

You can copy the properties of an existing phone template
                                 		  into a new phone template when you want to change only a few fields. The copy
                                 		  duplicates all the values that were specified in the original template.

Ensure that the new template that you create is the same device
                                             			 type as the original template, such as CiscoIPPhone 7975.

Step 1

Find the Phone Template that you want to copy.

Step 2

Copy the Phone Template. Do one of the following:

In the Phone Template Configuration window, verify
                                                				  that this is the template that you want to copy and click Copy .

In the Find and List Phone Templates window, click
                                                				  the icon in the Copy column that corresponds to the phone
                                                				  template that you want to copy.

To copy a template and all the lines associated with that
                                                				  template, in the Find and List Phone Templates window, click
                                                				  the icon in the Super Copy column that corresponds to
                                                				  the phone template with the lines that you want to copy.

Step 3

In the Template Name field, enter a name for the
                                          			 template.

#### Example:

Step 4

Update the fields as needed for the new template.

Step 5

Click Save .

#### What to do next

You can continue to add or update phone lines, IP services, and speed
                                 		  dials to the template.

### Delete BAT Phone Template

You can delete BAT phone templates.

Caution

If you submit a job that uses a particulate phone template and you
                                             			 delete that phone template, the job also gets deleted.

Step 1

Find the Phone Template that you want to delete.

Step 2

Delete the Phone Template. Do one of the following:

In the Phone Template Configuration window, verify
                                                				  that this is the template that you want to delete and click Delete .

In the Find and List Phone Templates window. check
                                                				  the check box next to the template that you want to delete and click Delete Selected .

Step 3

To delete the template, click OK . The template name disappears from the list
                                          			 of phone templates list on the Find and List Phone Templates window.

### BAT Phone Template
                           	 Field Descriptions

The following table provides descriptions of all possible fields that display when you add a BAT phone template for all IP
                                 telephony devices. Some device types do not require all the phone settings, and only some fields show the values that were
                                 configured in Unified Communications Manager Administration. Field names that have an asterisk in the BAT user interface require an entry. Treat fields that do not have
                                 an asterisk as optional.

Field

Description

Device Information

Device
                                             					 Trust Mode

Select
                                             					 whether the device is trusted or not trusted. You can configure this setting
                                             					 for analog phones using SCCP, and for some third-party endpoints.

Template
                                             					 Name

Enter the
                                             					 name for the template.

Description

Enter a
                                             					 description for the phone template that you want to create. The description can
                                             					 include up to 50 characters in any language, but it cannot include
                                             					 double-quotes ("), percentage sign ( % ), ampersand (&), back-slash ( \ ), or angle
                                             					 brackets (<>).

Requires Activation Code for Onboarding

Check this check box if you want to use activation codes, rather than autoregistration, to onboard phones that use this template.

This option is available only for phones that support activation codes.

DevicePool

Choose the
                                             					 device pool for this group of phones or ports.

For devices, a devicepool defines sets of common characteristics, such as region, date/time group, Unified Communications Manager group, and calling search space for auto-registration.

Common
                                             					 Device Configuration

Choose the
                                             					 common device configuration to which you want this phone assigned. The common
                                             					 device configuration includes the attributes (services or features) that are
                                             					 associated with a particular user. You configure the Common device
                                             					 configurations in the Common Device Configuration window.

To see the
                                             					 common device configuration settings, click the View Details link.

Phone Button
                                             					 Template

Choose the
                                             					 button template for all phones in this group. Button templates determine the
                                             					 button identity (line, speed dial) and the button location on the phone. Button
                                             					 templates include the expansion modules.

Softkey
                                             					 Template

Choose the
                                             					 softkey template to be used for all phones in this group.

Common Phone
                                             					 Profile

From the drop-down list, choose a common phone profile from the list of available common phone profiles.

Calling
                                             					 Search Space

Choose the
                                             					 calling search space for this group of phones/ports.

A calling
                                             					 search space specifies the collection of Route Partitions that are searched to
                                             					 determine how a dialed number should be routed.

AAR Calling
                                             					 Search Space

Choose the
                                             					 appropriate calling search space for the device to use when it performs
                                             					 automated alternate routing (AAR). The AAR calling search space specifies the
                                             					 collection of route partitions that are searched to determine how to route a
                                             					 collected (originating) number that is otherwise blocked due to insufficient
                                             					 bandwidth.

Media
                                             					 Resource Group List

Choose the
                                             					 media resource group list (MRGL) for this group of phones/ports.

An MRGL
                                             					 specifies a list of prioritized media resource groups. An application can
                                             					 choose required media resources from the available ones according to the order
                                             					 that is defined in the MRGL.

User Hold
                                             					 MOH Audio Source

Choose the
                                             					 user hold audio source for this group of phones/ports.

The user
                                             					 hold audio source identifies the audio source from which music is played when a
                                             					 user places a call on hold.

Network Hold
                                             					 MOH Audio Source

Choose the
                                             					 network hold audio source for this group of IP phones or ports.

The network
                                             					 hold audio source identifies the audio source from which music is played when
                                             					 the system places a call on hold, such as when the user transfers or parks a
                                             					 call.

Location

Choose the
                                             					 appropriate location for this group of IP phones or ports.

The location
                                             					 specifies the total bandwidth that is available for calls to and from this
                                             					 location. A location setting of None means that the locations feature does not
                                             					 keep track of the bandwidth that this CiscoIPPhone consumes.

AAR Group

Choose the
                                             					 automated alternate routing (AAR) group for this device. The AAR group provides
                                             					 the prefix digits that are used to route calls that are otherwise blocked due
                                             					 to insufficient bandwidth.

Set AAR
                                             					 Group to < None > to prevent rerouting blocked calls.

User
                                             					 Locale

Choose the
                                             					 country and language set that you want to associate with this group of IP
                                             					 phones.

This choice determines which cultural-dependent attributes exist for this user and which language displays for the user in
                                             the Unified Communications Manager user windows and phones.

Network
                                             					 Locale

Choose the
                                             					 network locale that you want to associate with this group of phones.

The
                                             					 Network Locale comprises a set of tones and cadences that Cisco gateways and
                                             					 phones use when they communicate with the PSTN and other networks in a specific
                                             					 geographical area.

Built In
                                             					 Bridge

Enable or disable the built-in conference bridge for the barge feature by using the Built In Bridge drop-down list (choose On , Off , or Default ).

Privacy

For each phone that wants Privacy, choose On in the Privacy drop-down list.

Device
                                             					 Mobility Mode

From the drop-down list, turn the device mobility feature on or off for this device or choose Default to use the default device mobility mode.

Click View Current Device Mobility Settings to display the
                                             					 current values of these device mobility parameters:

Cisco Unified Communications Manager Group

Roaming Device Pool

Location

Region

Network Locale

AAR Group

AAR Calling Search Space

Device Calling Search Space

Media Resource Group List

SRST

Owner User
                                             					 ID

Enter a
                                             					 user ID for the primary phone user.

Mobility
                                             					 User ID

(Dual-mode
                                             					 phones only)

From the drop-down list, choose the user ID of the person to whom this dual-mode phone is assigned.

The
                                                         						Mobility User ID configuration gets used for the Cisco Unified Mobility and
                                                         						Mobile Voice Access features for dual-mode phones.

The
                                                         						Owner User ID and Mobility User ID can differ.

Phone
                                             					 Personalization

From the drop-down list, enable or disable the personalization settings on the phone, or choose Default to use the phone personalization that is set in the Common Phone Profile. You can choose one of the following options:

Disabled —None of the personalization settings on the phone get activated.

Enabled —This setting accepts a personalized background image file, which is used for the phone screen; it accepts a preview image
                                                   file for temporary display; and it accepts a personalized tone file, so the default ring tone can be personalized.

Default —Use the phone personalization setting that is in the Common Phone Profile.

Services
                                             					 Provisioning

From the drop-down list, choose the Services Provisioning setting that you want to use from the following values:

Internal

External URLs

Both

Default: Internal

This
                                             					 parameter controls whether the phone uses the services provisioned from the
                                             					 configuration file (Internal), services received from the Services URLs
                                             					 (External URLs), or both. The External URLs option provides backward
                                             					 compatibility with third party provisioning servers. The Both option allows
                                             					 users to subscribe to the services specified in the configuration file while
                                             					 also appending services from an external provisioning server.

This is a
                                             					 required field.

Phone Load
                                             					 Name

Enter the
                                             					 custom phone load, if applicable.

Any
                                                         						value that is entered in this field overrides the default value for the chosen
                                                         						model.

For more information about CiscoIPPhone software and configuration, refer to the CiscoIPPhone Administration Guide for Unified Communications Manager , which is specific to the phone model.

Single
                                             					 Button Barge

From the drop-down list, enable or disable the Single Button Barge/cBarge feature for this device or choose Default to use the service parameter setting.

Off —This setting disables the Single Button Barge/cBarge feature; however, the regular Barge or cBarge features will still work.

Barge —This setting enables the Singe Button Barge feature.

cBarge —This setting enables the Single Button cBarge feature.

Default —This setting uses the Single Button Barge/cBarge setting that is in the service parameter.

Join
                                             					 Across Lines

From the drop-down list, enable or disable the Join Across Lines feature for this device or choose Default to use the service parameter setting.

Off —This setting disables the Join Across Lines feature.

On —This setting enables the Join Across Lines feature.

Default —Uses the Join Across Lines setting that is in the service parameter.

Use
                                             					 Trusted Relay Point

From the drop-down list, enable or disable whether Unified Communications Manager inserts a trusted relay point (TRP) device with this media endpoint. Choose one of the following values:

Default —If you choose this value, the device uses the Use Trusted Relay Point setting from the common device configuration with which
                                                   this device associates.

Off —Choose this value to disable the use of a TRP with this device. This setting overrides the Use Trusted Relay Point setting
                                                   in the common device configuration with which this device associates.

On —Choose this value to enable the use of a TRP with this device. This setting overrides the Use Trusted Relay Point setting
                                                   in the common device configuration with which this device associates.

A Trusted
                                             					 Relay Point (TRP) device designates an MTP or transcoder device that is labeled
                                             					 as Trusted Relay Point.

Unified Communications Manager places the TRP closest to the associated endpoint device if more than one resource is needed for the endpoint (for example,
                                             a transcoder or RSVPAgent).

If both
                                             					 TRP and MTP are required for the endpoint, TRP gets used as the required MTP.

BLF
                                             					 Audible Alert Setting (Phone Idle)

From the drop-down list, choose the BLF Audible Alert setting that you want to use from the following values:

On

Off

Default

This
                                             					 parameter provides an audible alert in addition to a visual alert on a phone
                                             					 that is currently idle when a call comes in to one of the lines that is
                                             					 monitored by way of a busy lamp field (BLF) button.

This is a
                                             					 required field.

BLF
                                             					 Audible Alert Setting (Phone Busy)

This
                                             					 parameter for this required field provides an audible alert in addition to a
                                             					 visual alert on a phone that is currently in use when a call comes in to one of
                                             					 the lines that is monitored by way of a busy lamp field (BLF) button.

From the drop-down list, choose the BLF Audible Alert setting that you want to use from the following values:

On

Off

Default

Always Use
                                             					 Prime Line

From the drop-down list, choose one of the following options:

Off —When the phone is idle and receives a call on any line, the phone user answers the call from the line on which the call is
                                                   received.

On —When the phone is idle (off-hook) and receives a call on any line, the primary line gets chosen for the call. Calls on other
                                                   lines continue to ring, and the phone user must select those other lines to answer these calls.

Default — Unified Communications Manager uses the configuration from the Always Use Prime Line service parameter, which supports the Cisco CallManager service.

Always Use
                                             					 Prime Line for Voice Message

From the drop-down list, choose one of the following options:

On —If the phone is idle, the primary line on the phone becomes the active line for retrieving voice messages when the phone
                                                   user presses the Messages button on the phone.

Off —If the phone is idle, pressing the Messages button on the phone automatically dials the voice-messaging system from the line
                                                   that has a voice message. Unified Communications Manager always selects the first line that has a voice message. If no line has a voice message, the primary line gets used when the
                                                   phone user presses the Messages button.

Default — Unified Communications Manager uses the configuration from the Always Use Prime Line for Voice Message service parameter, which supports the Cisco CallManager
                                                   service.

Geo
                                             					 Location

From the drop-down list, choose a geo location.

You can
                                             					 choose the Unspecified geo location, which designates that this
                                             					 device does not associate with a geo location.

You can
                                             					 also choose a geolocation that has been configured with the System > Geolocation
                                                   						  Configuration menu option.

Feature
                                             					 Control Policy

Choose the
                                             					 Feature Control Policy for this group of phones.

A feature
                                             					 control policy specifies the appearance of features and the associated softkeys
                                             					 that are displayed on the phone.

Device
                                             					 Security Mode

From the drop-down list, choose the mode that you want to set for the device:

Use System
                                                					 Default —The phone uses the value that you specified for the enterprise
                                             				  parameter, Device Security Mode.

Non-secure —No security features exist for the phone. A TCP connection opens to Unified Communications Manager .

Authenticated — Unified Communications Manager provides integrity and authentication for the phone. A TLS connection that uses NULL/SHA opens.

Encrypted — Unified Communications Manager provides integrity, authentication, and encryption for the phone. A TLS connection that uses AES128 / SHA opens.

This field
                                             					 displays only if the phone model supports authentication or encryption.

Retry
                                             					 Video Call as Audio

This check
                                             					 box applies only to video endpoints that receive a call. If this phone receives
                                             					 a call that does not connect as video, the call tries to connect as an audio
                                             					 call.

By
                                             					 default, the system checks this check box to specify that this device should
                                             					 immediately retry a video call as an audio call (if it cannot connect as a
                                             					 video call) prior to sending the call to call control for rerouting.

If you
                                             					 uncheck this check box, a video call that fails to connect as video does not
                                             					 try to establish as an audio call. The call then fails to call control, and
                                             					 call control routes the call via Automatic Alternate Routing (AAR) and / or route / hunt list.

Ignore
                                             					 Presentation Indicators (Internal Calls Only)

Check this check box to configure call display restrictions on a call-by-call basis. When this check box is checked, Unified Communications Manager ignores any presentation restriction that is received for internal calls.

Allow
                                             					 Control of Device from CTI

Check this
                                             					 check box to allow control of all CTI controllable devices from CTI.

You can enable or disable this check box based on CTI Controllable Device Type and Device Protocol.

Cisco dual-mode devices (Jabber) such as Android, iPhone, and iPad operating in WiFi mode are monitored through CTI and not
                                                         controlled. However, devices operating in GSM mode cannot be monitored or controlled.

Logged
                                             					 into Hunt Group

This check
                                             					 box, which gets checked by default for all phones, indicates that the phone is
                                             					 currently logged in to a hunt list (group). When the phone gets added to a hunt
                                             					 list, the administrator can log the user in or out by checking (and unchecking)
                                             					 this check box.

Users use
                                             					 the softkey on the phone to log their phone in or out of the hunt list.

Remote
                                             					 Device

If you are experiencing delayed connect times over SCCP to remote sites, check the Remote Device check box in the Phone Configuration
                                             window. Checking this check box tells Unified Communications Manager to allocate a buffer for the phone device when it registers
                                             and to bundle SCCP messages to the phone.

Because
                                             					 this feature consumes resources, be sure to check this check box only when you
                                             					 are experiencing signaling delays for phones that are running SCCP. Most users
                                             					 do not require this option.

Protected
                                             					 Device

Check this
                                             					 check box to designate a phone as "protected." This enables the phone to play a two-second tone
                                             					 notifying the user when a call is both encrypted and both phones are configured
                                             					 as protected devices. The tone plays for both parties when the call is
                                             					 answered. The tone does not play unless both phones are "protected" and the call occurs over encrypted media.

Tip

Hotline
                                             					 Device

Check this
                                             					 check box to make this device a Hotline device. Hotline devices can only
                                             					 connect to other Hotline devices. This feature is an extension of PLAR, which
                                             					 configures a phone to automatically dial one directory number when it goes
                                             					 off-hook. Hotline provides additional restrictions that you can apply to
                                             					 devices that use PLAR.

To
                                             					 implement Hotline, you must also create a softkey template without
                                             					 supplementary service softkeys, and apply it to the Hotline device.

Number Presentation Transformation

Caller ID for Calls from
                                                						This Phone

Calling Party
                                             					 Transformation CSS

From the drop-down list, choose the calling search space (CSS) that contains the calling party transformation pattern that
                                             you want to apply on the calling number when this phone initiates a call.

When this
                                             					 phone initiates a call, Unified Communications Manager transforms the calling
                                             					 party using the digit transformations that are configured on the matching
                                             					 calling party transformation pattern. This setting allows you to transform the
                                             					 calling party number before Unified Communications Manager routes the call. For
                                             					 example, a transformation pattern can change a phone extension to an E.164
                                             					 number. This setting is generally configured when users dial using a URI
                                             					 instead of digits. Unified Communications Manager allows calling party
                                             					 transformations on various patterns when users dial using digits; this setting
                                             					 provides similar transformation provision even when users dial using a URI.

Use Device Pool Calling
                                             					 Party Transformation CSS (Caller ID for Calls from This Phone)

Check this check box to use
                                             					 the Calling Party Transformation CSS that is configured at the device pool to
                                             					 which this phone belongs for transforming the calling party for calls that are
                                             					 initiated from this phone. At the device pool, the Calling Party Transformation
                                             					 CSS that is present under Phone Settings is used to transform the calling party
                                             					 for calls initiated from this phone.

Leave this check box
                                             					 unchecked to apply the Calling Party Transformation CSS setting that appears in
                                             					 this configuration window.

Remote Number Transformation

Calling Party
                                             					 Transformation CSS

From the drop-down list, choose the calling search space (CSS) that contains the calling party transformation pattern that
                                             you want to apply on the remote calling number for the calls that are received on this phone.

Unified
                                             					 Communications Manager transforms the remote calling number using the digit
                                             					 transformations that are configured on the matching calling party
                                             					 transformation pattern before presenting it to this device.

For
                                             					 example, a transformation pattern can change a remote number in E.164 format to
                                             					 a localized version.

Use this
                                             					 setting to transform the remote connected number for direct calls that are
                                             					 initiated from this phone. Use this setting also to transform a remote
                                             					 connected number after you invoke the feature irrespective of the direction of
                                             					 the call. The transformation of the remote connected number is controlled using
                                             					 the service parameter “Apply Transformations on Remote Number,” present under
                                             					 the Advanced section of Cisco Call Manager service. For more information, refer
                                             					 to the description for this parameter.

Use Device
                                             					 Pool Calling Party Transformation CSS (Device Mobility Related Information)

Check this
                                             					 check box to apply the Calling Party Transformation CSS that is configured at
                                             					 the device pool to which this phone belongs for transforming the remote calling
                                             					 and remote connected number. At the device pool, the Calling Party
                                             					 Transformation CSS present under Device Mobility Related Information section is
                                             					 used to transform the remote calling and remote connected number.

Leave this
                                             					 check box unchecked to apply the Calling Party Transformation CSS setting that
                                             					 appears in this configuration window for transforming the remote number.

Associated Mobility
                                                						Identity —These mobility fields are available only for Nokia S60
                                             					 device and Cisco Unified Mobile Communicator phones. Click the Add New Mobile Identity link to display the Mobile
                                             					 Identity Configuration page.

Name

Enter a
                                             					 name that identifies the mobile identity.

Destination Number

Enter the
                                             					 telephone number for the identity. Include the area code and any additional
                                             					 digits that are required to obtain an outside line. Maximum field length equals
                                             					 24 characters; individual characters can take the values 0-9, * , and # . Cisco recommends that you configure the caller ID of
                                             					 the smart phone destination.

Add the
                                             					 necessary translation pattern or route patterns to route the destination
                                             					 number.

Answer Too
                                             					 Soon Timer

Enter the
                                             					 minimum time in milliseconds that must pass before the mobile phone can be
                                             					 answered.

Range: 0 -
                                             					 10,000 milliseconds

Default:
                                             					 1,500 milliseconds

Answer Too
                                             					 Late Timer

Enter the
                                             					 maximum time in milliseconds that can pass before the mobile phone must be
                                             					 answered.

Range:
                                             					 10,000 - 300,000 milliseconds

Default:
                                             					 19,000 milliseconds

Delay
                                             					 Before Ringing Timer

Enter the
                                             					 time that elapses before the mobile phone rings when a call is transferred from
                                             					 the desktop phone.

Range: 0 -
                                             					 30,000 milliseconds

Default:
                                             					 4,000 milliseconds

Time of
                                             					 Day Access

From the drop-down list, choose a time-of-day access record to associate with this destination.

Time Zone

From the drop-down list, choose a time zone to use for this remote destination.

The time
                                                         						zone that you use for this remote destination is used by the time-of-day access
                                                         						feature to allow or block calls to this destination.

Mobile
                                             					 Phone

Check the
                                             					 check box if you want calls that are answered by the desktop phone to be sent
                                             					 to your mobile phone as the remote destination.

You must
                                                         						check this check box for Cisco Unified Mobility to work with this remote
                                                         						destination.

Enable
                                             					 Cisco Unified Mobility

Check the
                                             					 check box to allow an incoming call to ring your desktop phone and remote
                                             					 destination at the same time.

Associated Remote
                                                						Destinations — Click the Add a New Remote Destination link to display the Remote Destination Configuration page

Name

Enter a
                                             					 name that identifies the remote destination.

Destination Number

Enter the
                                             					 telephone number for the destination. Include the area code and any additional
                                             					 digits that are required to obtain an outside line. Maximum field length equals
                                             					 24 characters; individual characters can take the values 0-9, * , and # . Cisco recommends that you configure the caller ID of
                                             					 the remote destination.

Add the
                                             					 necessary translation pattern or route patterns to route the destination
                                             					 number.

Answer Too
                                             					 Soon Timer

Enter the
                                             					 minimum time in milliseconds that must pass before the mobile phone can be
                                             					 answered.

Range: 0 -
                                             					 10,000 milliseconds

Default:
                                             					 1,500 milliseconds

Answer Too
                                             					 Late Timer

Enter the
                                             					 maximum time in milliseconds that can pass before the mobile phone must be
                                             					 answered.

Range:
                                             					 10,000 - 300,000 milliseconds

Default:
                                             					 19,000 milliseconds

Delay
                                             					 Before Ringing Timer

Enter the
                                             					 time that elapses before the mobile phone rings when a call is transferred from
                                             					 the desktop phone.

Range: 0 -
                                             					 30,000 milliseconds

Default:
                                             					 4,000 milliseconds

Time of
                                             					 Day Access

From the drop-down list, choose a time-of-day access record to associate with this remote destination.

Time Zone

From the drop-down list, choose a time zone to use for this remote destination.

The time
                                                         						zone that you use for this remote destination is used by the time-of-day access
                                                         						feature to allow or block calls to this remote destination.

Mobile
                                             					 Phone

Check the
                                             					 check box if you want calls that are answered by the desktop phone to be sent
                                             					 to your mobile phone as the remote destination.

You must
                                                         						check this check box for Cisco Unified Mobility to work with this remote
                                                         						destination.

Enable
                                             					 Cisco Unified Mobility

Check the
                                             					 check box to allow an incoming call to ring your desktop phone and remote
                                             					 destination at the same time.

Protocol Specific
                                                						Information

Packet
                                             					 Capture Mode

From the drop-down list, choose the mode that you want to set for signal packet capture:

None —Choose None if you do not want to specify a mode.

Real-Time Mode —Use this mode for real-time signal packet capture.

Batch Processing Mode —Use this mode for batch processing signal packet capture mode.

Packet
                                             					 Capture Duration

Enter the
                                             					 time for packet capture in minutes. You can enter a maximum duration of 300
                                             					 minutes. The default duration specifies 60 minutes.

BLF
                                             					 Presence Group

Used with
                                             					 the BLF Presence feature, the phone that is running SIP or SCCP serves as a
                                             					 watcher because it requests status about the presence entity; for example,
                                             					 directory number, that is configured as a BLF speed dial button on the phone.

If you
                                             					 want the phone to receive the status of the presence entity, choose a BLF
                                             					 Presence group that is allowed to view the status of the Presence group that is
                                             					 applied to the directory number, as indicated in the BLF Presence Group
                                             					 Configuration window.

SIP Dial Rules

If required, choose the appropriate SIP dial rule. SIP dial
                                             					 rules provide local dial plans for Cisco IP phones 7940, and 7975 that are
                                             					 running SIP, so users do not have to press a key or wait for a timer before the
                                             					 call gets processed.

Leave the SIP Dial Rules field set to
                                             					 < None > if you do not want dial rules applied to the IP
                                             				  phone that is running SIP. This means the user will have to use the Dial
                                             				  softkey or wait for the timer to expire before the call gets processed.

Device
                                             					 Security Profile

For phones
                                             					 that are running SCCP or SIP, choose the security profile that you want to
                                             					 apply to the device.

All phones
                                             					 require that you apply a security profile. If the phone does not support
                                             					 security, choose a nonsecure profile.

MTP
                                             					 Preferred Originating Codec

From the drop-down list, choose the codec to use if a media termination point is required for SIP calls.

Rerouting
                                             					 Calling Search Space

From the drop-down list, choose a calling search space to use for rerouting.

The
                                             					 rerouting calling search space of the referrer gets used to find the route to
                                             					 the refer-to target. When the Refer fails due to the rerouting calling search
                                             					 space, the Refer Primitive rejects the request with the "405
                                                						Method Not Allowed" message.

The
                                             					 redirection (3xx) primitive and transfer feature also uses the rerouting
                                             					 calling search space to find the redirect-to or transfer-to target.

Out-of-Dialog Refer Calling Search Space

From the drop-down list, choose an out-of-dialog refer calling search space.

Unified Communications Manager uses the out-of-dialog (OOD) Refer Authorization calling search space (CSS) to authorize the SIP out-of-dialog Refer. The
                                             administrator can restrict the use of out-of-dialog Refer by configuring the OOD CSS of the Referrer. Refer Primitive rejects
                                             the OOD Refer request with a "403 Forbidden" message.

SUBSCRIBE
                                             					 Calling Search Space

Used with the Presence feature, the SUBSCRIBE Calling Search Space determines how Unified Communications Manager routes the subscription requests that come from the phone. From the drop-down list, choose the calling search space that
                                             you want to use for this purpose.

SIP
                                             					 Profile

Choose the
                                             					 default SIP profile or a specific profile that was previously created. SIP
                                             					 profiles provide specific SIP information for the phone such as default
                                             					 telephony event payload type, registration and keepalive timers, media ports,
                                             					 Iris, and dynamic DNS server addresses.

Digest
                                             					 User

Used with
                                             					 digest authentication (SIP security), choose an end user that you want to
                                             					 associate with the phone.

Ensure
                                             					 that you configured digest credentials for the user that you choose, as
                                             					 specified in the End User Configuration window.

After you
                                             					 save the phone configuration and reset the phone, the digest credentials for
                                             					 the user get added to the phone configuration file.

For more information on digest authentication, refer to the Cisco  Unified Communications Manager Security Guide .

Media
                                             					 Termination Point Required

Use this
                                             					 field to indicate whether a media termination point is used to implement
                                             					 features that H.323 does not support (such as hold and transfer).

Check the
                                             					 Media Termination Point Required check box if you want to use an MTP to
                                             					 implement features. Uncheck the Media Termination Point Required check box if
                                             					 you do not want to use an MTP to implement features.

Use this
                                             					 check box only for H.323 clients and those H.323 devices that do not support
                                             					 the H.245 empty capabilities set or if you want media streaming to terminate
                                             					 through a single source.

Unattended
                                             					 Port

Check this
                                             					 check box to indicate an unattended port on this device.

Require
                                             					 DTMF Reception

For phones
                                             					 that are running SIP and SCCP, check this check box to require DTMF reception
                                             					 for this phone.

RFC2833
                                             					 Disabled

For phones
                                             					 that are running SCCP, check this check box to disable RFC2833 support.

Certification Authority
                                                						Proxy Function (CAPF) Information (These parameters display only for
                                             					 devices with the capability to support authentication or encryption.)

Certificate Operation

From the drop-down list, choose the Certification Operation that you want to perform from the following options:

No Pending Operation —No pending Certification Operation lists exist for this device. Choosing this option disables the remaining CAPF fields.

Install/Upgrade —Install or upgrade a Certification Operation.

Delete —Delete a Certification Operation.

Troubleshoot —Troubleshoot a Certification Operation.

Authentication Mode

From the drop-down list, choose the Authentication Mode by which you want the phone to authenticate with CAPF during the certificate
                                             operation from the following options:

By Null String —Install/upgrade, delete, or troubleshoot a locally significant certificate without user intervention.

< None >

This
                                                         						option prompts you to specify a value for the Authentication Mode.

By Authentication String—Installs/upgrades, deletes, or troubleshoots a locally significant certificate only when the user
                                                   enters the CAPF authentication string on the phone.

By Existing Certificate (precedence to LSC)—Installs or upgrades, deletes, or troubleshoots a locally significant certificate
                                                   if a manufacture-installed certificate (MIC) or locally significant certificate (LSC) exists in the phone.

Before
                                                         						you choose this option, verify that a certificate exists in the phone. If you
                                                         						choose this option and no certificate exists in the phone, the operation fails.

By Existing Certificate (precedence to MIC)—Installs/upgrades, deletes, or troubleshoots a locally significant certificate
                                                   if a LSC or MIC exists in the phone.

Before
                                                         						you choose this option, verify that a certificate exists in the phone. If you
                                                         						choose this option and no certificate exists in the phone, the operation fails.

Authentication String

If you chose the By Authentication String option from the Authentication Mode drop-down list in the security profile, this setting applies. Manually enter a numeric string that contains 4 to 10 digits.
                                             To install, upgrade, or troubleshoot a locally significant certificate, the phone user or administrator must enter the authentication
                                             string on the phone.

Key Order

This field
                                             					 specifies the sequence of the key for CAPF. Select one of the following values
                                             					 from the drop-down list:

RSA Only

EC Only

EC Preferred, RSA
                                                      							 Backup

When you
                                                         						add a phone based on the value in Key Order , RSA Key Size , and EC Key Size fields, the device security profile is
                                                         						associated with the phone. If you select the EC Only value with the EC Key Size value of 256 bits then the device
                                                         						security profile appends with EC-256 value.

RSA Key
                                             					 Size (Bits)

From the drop-down list, choose one of the these values— 512 , 1024 , 2048 , 3072 , or 4096 .

Some
                                                         						phone models may fail to register if the RSA key length selected for the CallManager Certificate Purpose is greater than 2048. From the
                                                         						Unified CM Phone Feature List Report on the Cisco Unified Reporting Tool
                                                         						(CURT), you can check the 3072/4096 RSA key size support feature for the list
                                                         						of supported phone models.

EC Key
                                             					 Size (Bits)

From the drop-down list, choose one of the these values— 256 , 384 , or 521 .

Operation
                                             					 Completes By

This
                                             					 field, which supports the Install/Upgrade , Delete , and Troubleshoot Certificate Operation options, specifies
                                             				  the date and time in which you must complete the operation.

Certificate Operation Status

This field
                                             					 displays the progress of the certificate operation; for example, <operation
                                             					 type> pending, failed, or successful, where operating type equals the Install/Upgrade , Delete , or Troubleshoot Certificate Operation options. You cannot
                                             				  change the information that displays in this field.

Expansion Module
                                                						Information

Module 1

Choose the
                                             					 expansion module if it is installed in the phone.

Module1
                                             					 Load Name

Enter the
                                             					 firmware load for the first CiscoUnifiedIPPhone Expansion Module, if
                                             					 applicable. Leave this field blank to use the default load.

Module 2

Choose the
                                             					 expansion module if it is installed in the phone.

Module 2
                                             					 Load Name

Enter the
                                             					 firmware load for the second CiscoUnifiedIPPhone Expansion Module, if
                                             					 applicable. Leave this field blank to use the default load.

CiscoUnifiedIPPhone -
                                                						External Data Locations

Information

Enter the
                                             					 help text URL for the information button for CiscoUnifiedIPPhones.

Directory

Enter the
                                             					 URL of the directory server for CiscoUnifiedIPPhones.

Messages

Enter the
                                             					 voice-messaging access pilot number for CiscoUnified IPPhones.

Services

Enter the
                                             					 URL for the services menu for CiscoUnifiedIPPhones.

Authentication Server

Enter the
                                             					 URL that the phone uses to validate requests that are made to the phones web
                                             					 server. If you do not provide an authentication URL, the advanced features on
                                             					 the CiscoUnifiedIPPhone models that require authentication will not
                                             					 function. Leave this field blank to accept the default setting.

By default, this URL
                                             					 accesses a Cisco Unified Communications Self Care Portal window that was
                                             					 configured during installation.

Proxy
                                             					 Server

Enter the
                                             					 host and port (for example, proxy.cisco.com:80) that are used to proxy HTTP
                                             					 requests for access to non-local host addresses from the phones HTTP client.

If the
                                             					 phone receives a URL such as www.cisco.com in a service and the phone is not
                                             					 configured in the cisco.com domain, the phone uses the proxy server to access
                                             					 the URL. If the phone is configured in the cisco.com domain, the phone accesses
                                             					 the URL without using the proxy because it is in the same domain as the URL.

Leave this
                                             					 field blank to accept the default setting.

Idle

Enter the
                                             					 URL of the XML service that will appear as the idle display on the
                                             					 CiscoUnifiedIPPhone LCD screen when the Phone has not been used for the time
                                             					 that is specified in the Idle Timer field. For example, you can display a logo
                                             					 on the LCD screen when the phone has not been used for 5 minutes. Leave this
                                             					 field blank to use the default value.

Idle Timer

Enter the
                                             					 seconds that you want to elapse before the phone displays the URL that is
                                             					 specified in the Idle field. Leave this field blank to use the default value.

Secure
                                             					 Authentication URL

Enter the
                                             					 secure URL that the phone uses to validate requests that are made to the phone
                                             					 web server.

If you
                                                         						do not provide a Secure Authentication URL, the device uses the nonsecure URL.
                                                         						If you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities.

By
                                             					 default, this URL accesses a Cisco Unified CM User Options window that was
                                             					 configured during installation.

Leave this
                                             					 field blank to accept the default setting.

Maximum
                                             					 length: 255

Secure
                                             					 Directory URL

Enter the
                                             					 secure URL for the server from which the phone obtains directory information.
                                             					 This parameter specifies the URL that secured Cisco Unified IP Phones use when
                                             					 you press the Directory button.

If you
                                                         						do not provide a Secure Directory URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities.

Leave this
                                             					 field blank to accept the default setting.

Maximum
                                             					 length: 255

Secure
                                             					 Idle URL

Enter the
                                             					 secure URL for the information that displays on the Cisco Unified IP Phone
                                             					 display when the phone is idle, as specified in Idle Timer field. For example,
                                             					 you can display a logo on the LCD when the phone has not been used for 5
                                             					 minutes.

If you
                                                         						do not provide a Secure Idle URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities.

To accept
                                             					 the default setting, leave this field blank.

Maximum
                                             					 length: 255

Secure
                                             					 Information URL

Enter the
                                             					 secure URL for the server location where the Cisco Unified IP Phone can find
                                             					 help text information. This information displays when the user presses the
                                             					 information (i) button or the question mark (?) button.

If you
                                                         						do not provide a Secure Information URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities.

To accept
                                             					 the default setting, leave this field blank.

Maximum
                                             					 length: 255

Secure
                                             					 Messages URL

Enter the
                                             					 secure URL for the messages server. The Cisco Unified IP Phone contacts this
                                             					 URL when the user presses the Messages button.

If you
                                                         						do not provide a Secure Messages URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities.

To accept
                                             					 the default setting, leave this field blank.

Maximum
                                             					 length: 255

Secure
                                             					 Services URL

Enter the
                                             					 secure URL for Cisco Unified IP Phone services. The is the location that the
                                             					 secure Cisco Unified IP Phone contacts when the user presses the Services
                                             					 button.

If you
                                                         						do not provide a Secure Services URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities.

To accept
                                             					 the default setting, leave this field blank.

Maximum
                                             					 length: 255

Extension Mobility (Device
                                                						Profile) Information

Enable
                                             					 Extension Mobility

Check this
                                             					 check box to enable the extension mobility feature. Extension mobility allows a
                                             					 user to log in and out of a CiscoIPPhone.

Log Out
                                             					 Profile

Choose the profile that a phone should load when an extension mobility user logs out. You must configure logout profiles in Unified Communications Manager Administration.

Use
                                             					 Current Device Setting—This choice creates an autogenerated device profile as
                                             					 the default device profile.

Select a
                                             					 User Device Profile—This choice assigns a user device profile, which has
                                             					 already been defined, that becomes the default device profile for this device.

The chosen
                                             					 user device profile gets loaded onto the device when no user is logged in.

MultiLevel Precedence and
                                                						Preemption (MLPP) Information

MLPP
                                             					 Indication

If
                                             					 available, this setting specifies whether a device that is capable of playing
                                             					 precedence tones will use the capability when it places an MLPP precedence
                                             					 call.

From the drop-down list, choose a setting to assign to this device from the following options:

Default —This device inherits its MLPP indication setting from its device pool.

Off —This device does not send indication of an MLPP precedence call.

On —This device does send indication of an MLPP precedence call.

Do not
                                                         						configure a device with the following combination of settings: MLPP Indication
                                                         						is set to Off while MLPP Preemption is set to Forceful.

MLPP
                                             					 Preemption

If
                                             					 available, this setting specifies whether a device that is capable of
                                             					 preempting calls in progress will use the capability when it places an MLPP
                                             					 precedence call.

From the drop-down list, choose a setting to assign to this device from the following options:

Default —This device inherits its MLPP preemption setting from its device pool.

Disabled —This device does not preempt calls in progress when it places an MLPP precedence call.

Forceful —This device preempts calls in progress when it places an MLPP precedence call.

Do not
                                                         						configure a device with the following combination of settings: MLPP Indication
                                                         						is set to Off while MLPP Preemption is set to Forceful.

MLPP
                                             					 Domain (e.g., "0000FF" )

Enter a
                                             					 hexadecimal value for the MLPP domain that is associated with this device.
                                             					 Ensure that this field is blank or a value between 0 and FFFFFF.

H.323
                                             					 Device Information

Signaling
                                             					 Port

The value
                                             					 designates the H.225 signaling port that this device uses.

The
                                             					 default value specifies 1720. Valid values include 1 through 65535.

Retry
                                             					 Video Call as Audio

This check
                                             					 box applies only to video endpoints that receive a call. If this phone receives
                                             					 a call that does not connect as video, the call tries to connect as an audio
                                             					 call.

By
                                             					 default, the system checks this check box to specify that the sending device
                                             					 should immediately retry a video call that does not connect as an audio call
                                             					 prior to sending the call to call control for rerouting.

If you
                                             					 uncheck this check box, a video call that fails to connect as video fails to
                                             					 call control. At this point, call control reroutes the call within the route
                                             					 list. If Automatic Alternate Routing (AAR) is configured and enabled, call
                                             					 control also reroutes the call between route lists.

Wait for
                                             					 Far End H.245 Terminal Capability Set

By default, the system keeps this check box checked to specify that Unified Communications Manager should initiate capabilities exchange. This check box specifies that the Unified Communications Manager needs to receive the far-end H.245 Terminal Capability Set before it sends its H.245 Terminal Capability Set.

H.323
                                             					 Protocol Specific Information

SRTP
                                             					 Allowed

When this
                                             					 check box is checked, ensure that IPSec is configured in the network to provide
                                             					 end-to-end security. Failure to do so will expose keys and other information.

MTP
                                             					 Preferred Originating Codec

From the drop-down list, choose the codec to use if a media termination point is required for SIP calls.

Media
                                             					 Termination Point Required

Use this
                                             					 field to indicate whether a media termination point (MTP) is used to implement
                                             					 features that H.323 does not support (such as hold and transfer).

Check the
                                             					 Media Termination Point Required check box if you want to use a media
                                             					 termination point to implement features. Uncheck the Media Termination Point
                                             					 Required check box if you do not want to use a media termination point to
                                             					 implement features.

Use this
                                             					 check box only for H.323 clients and those H.323 devices that do not support
                                             					 the H.245 empty capabilities set or if you want media streaming to terminate
                                             					 through a single source.

If you
                                             					 check this check box to require an MTP and this device becomes the endpoint of
                                             					 a video call, the call works as audio only.

H.323
                                                						Information

Outgoing
                                             					 Caller ID Pattern

For
                                             					 incoming calls to the phone, enter the pattern, from 0 to 24 digits, that you
                                             					 want to use for caller ID.

Calling
                                             					 Party Selection

Choose one
                                             					 of the following options to specify which directory number is sent:

Originator —Send the directory number of the calling device.

First Redirect Number- —Send the directory number of the redirecting device.

Last Redirect Number —Send the directory number of the last device to redirect the call.

First Redirect Number(external) —Send the directory number of the redirecting device.

Last Redirect Number(external) —Send the directory number of the last device to redirect the call.

Calling
                                             					 Party Presentation

Choose
                                             					 whether the central office transmits or blocks caller ID:

Choose Allowed if you want the central office to send caller ID.

Choose Restricted if you do not want the central office to send caller ID.

Default displays the caller ID unless the caller ID was restricted in a previous level in the call stream.

Display IE
                                             					 Delivery

Check the
                                             					 check box to deliver the display information element (IE) in SETUP and CONNECT
                                             					 messages for the calling and called party name delivery service.

Redirecting Number IE Delivery—Outbound

Check this check box to include the Redirecting Number IE in the outgoing SETUP message from the Unified Communications Manager to indicate the first redirecting number and the redirecting reason of the call when the call is forwarded.

Uncheck
                                             					 the check box to exclude the first redirecting number and the redirecting
                                             					 reason from the outgoing SETUP message.

Use
                                             					 Redirecting Number IE for voice-messaging integration only. If your configured
                                             					 voice-messaging system supports Redirecting Number IE, check the check box.

Redirecting Number IE delivery—Inbound

Use
                                             					 Redirecting Number IE when you are integrating a voice-messaging system that
                                             					 supports Redirecting Number IE.

Check this check box to accept the Redirecting Number IE in the incoming SETUP message to the Unified Communications Manager .

Uncheck the check box to exclude the Redirecting Number IE in the incoming SETUP message to the Unified Communications Manager .

Gatekeeper
                                                						Information

Gatekeeper
                                             					 Name

Choose the gatekeeper for the gatekeeper-controlled H.323 device from the drop-down list.

If you
                                                         						do not choose the device, the system disables the E.164, Technology Prefix, and
                                                         						Zone fields.

You
                                                         						cannot change the device to a gatekeeper-controlled phone if more than one
                                                         						directory number is configured for the device.

E.164

Choose the
                                             					 E.164 address that is registered with the gatekeeper.

Ensure
                                                         						the H.323 client is configured as a gatekeeper-controlled device.

You must
                                                         						enter a value in this field for a gatekeeper-controlled H.323 client. You can
                                                         						enter only numbers (0-9) and special characters # and * in this field.

Technology
                                             					 Prefix

Enter the technology prefix to eliminate the need for entering the IP address for every Unified Communications Manager system when the gw-type-prefix command is configured. For example, you can enter 1#* in this field if you can use the following gw-type-prefix command on the gatekeeper:

gw-type-prefix 1#* default-technology.

You must
                                                         						enter a value in this field for a gatekeeper-controlled H.323 client. You can
                                                         						enter only numbers (0-9) and special characters # and * in this field.

Zone

On the gatekeeper, enter the specific zone with which Unified Communications Manager will register. The zone specifies the total bandwidth that is available for calls between this zone and another zone.

You must
                                                         						enter a value in this field for a gatekeeper-controlled phone. You can enter
                                                         						only letters, numbers, spaces, dashes, dots, and underscores in this field.

Gatekeeper
                                             					 Controlled H.323 Client

Check this
                                             					 check box to configure the H.323 client gatekeeper as a controlled gatekeeper.

Do Not
                                             					 Disturb (DND)

Do Not
                                             					 Disturb

Check this
                                             					 check box if you want DND to be enabled.

DND Option

From the drop-down list, choose a DND option from the following options:

None

Ringer Off

DND
                                             					 Incoming Call Alert

From the drop-down list, choose one of the following options:

None

Disable

Flash Only

Beep Only

Secure Shell
                                                						Information

Secure
                                             					 Shell User

Enter a
                                             					 user ID for the secure shell user. If the phone that you are configuring does
                                             					 not support secure shell access, this field does not display. Cisco Technical
                                             					 Assistance Center (TAC) uses secure shell for troubleshooting. Contact TAC for
                                             					 further assistance.

Secure
                                             					 Shell Password

Enter the
                                             					 password for a secure shell user. If the phone you are configuring does not
                                             					 support secure shell access, this field does not display. Contact TAC for
                                             					 further assistance.

Product-Specific
                                                						Configuration

Model-specific configuration fields defined by the device
                                             					 manufacturers

The device
                                             					 manufacturer specifies the model-specific fields under product-specific
                                             					 configuration. Because they are dynamically configured, they can change without
                                             					 notice.

To view
                                             					 field descriptions and help for product-specific configuration items, click the " ? " information
                                             					 icon to the right of the Product Specific Configuration heading to display
                                             					 help in a popup dialog box.

If you
                                             					 need more information, refer to the documentation for the specific device that
                                             					 you are configuring or contact the manufacturer.

### BAT Template Phone Line Field Descriptions

BAT phone template

Gateway template

UDP template

Remote destination template

Some device types do not require all the phone settings. Only some fields show the values that were configured in Unified Communications Manager Administration. Field names that have an asterisk in the BAT user interface require an entry. Treat fields that do not have
                                 an asterisk as optional.

Field

Description

Directory Number Information

Line Template Name

Enter a unique name for the line template.

Be aware that this field is available only when you are adding
                                             					 a line and not when you are updating an existing line.

Route Partition

Choose a route partition to which the directory number
                                             					 belongs.

The directory number can appear in more than one partition.

Description

Enter description for the line template. The description can
                                             					 include up to 50 characters in any language, but it cannot include
                                             					 double-quotes ("), percentage sign ( % ), ampersand
                                             					 ('), or angle brackets (<>).

Alerting Name

This name represents the name that displays during an alert to
                                             					 a shared directory number. For non-shared directory numbers, during alerts, the
                                             					 system uses the name that is entered in the Display field.

Alerting Name ASCII

This field provides the same information as the Alerting Name
                                             					 field, but you must limit input to ASCII characters. Devices that do not
                                             					 support Unicode (internationalized) characters display the content of the Alerting Name ASCII field.

Active

Checking this check box allows calls to this DN to be forwarded (if forwarding is configured). If check box is not checked, Unified Communications Manager ignores the DN.

Directory Number Settings

Voice Mail Profile

Choose this parameter to make the pilot number the same as the
                                             					 directory number for this line. This action proves useful if you do not have a
                                             					 voice-messaging server that is configured for this phone.

Calling Search Space

Choose partitions that are searched for numbers that are
                                             					 called from this directory number.

Changes cause an update of Pickup Group Names that are
                                                         						listed in the Call Pickup Group field. The setting
                                                         						applies to all devices that are using this directory number.

Presence Group

Used with the Presence feature, the directory number serves as
                                             					 the presence entity; that is, watchers request the status of the directory
                                             					 number, so the real-time status of the directory number displays on the device.

If you want the phone to receive the status of the presence
                                             					 entity, make sure that the Presence group of the watcher is allowed to view the
                                             					 status of the Presence group that is applied to the directory number, as
                                             					 indicated in the Presence Group Configuration window.

User Hold MOH Audio Source

Choose the music on hold audio source to be played when the
                                             					 user presses HOLD to place a call on hold.

Network Hold MOH Audio Source

Choose the music on hold audio source to be played when the
                                             					 system places a call on hold while the user transfers a call or initiates a
                                             					 conference or call park.

Auto Answer

Choose one of the following options to activate the Auto
                                             					 Answer feature for this directory number:

Auto Answer Off <Default>

Auto Answer with Headset

Auto Answer with Speakerphone

Make sure that the headset or speakerphone is not disabled
                                                         						when you choose Auto Answer with headset or Auto Answer with speakerphone .

Do not configure Auto Answer for devices that have shared
                                             					 lines.

AAR Settings —The settings in this row of
                                             					 fields specify treatment of calls for which insufficient bandwidth exists to
                                             					 reach the destination. Automated alternate routing (AAR) handles these calls
                                             					 that are routed to the AAR Destination Mask or Voice Mail.

AAR Voice Mail

Check this check box to use settings in the Voice Mail Profile
                                             					 Configuration window.

When this check box is checked, Unified Communications Manager ignores the settings in the Coverage/Destination box and Calling Search Space.

AAR Destination Mask

Use this setting instead of the external phone number mask to
                                             					 determine the AAR Destination to be dialed.

AAR CSS

Choose the appropriate calling search space for the device to
                                             					 use when it performs automated alternate routing (AAR). The AAR calling search
                                             					 space specifies the collection of route partitions that are searched to
                                             					 determine how to route a collected (originating) number that is otherwise
                                             					 blocked due to insufficient bandwidth.

AAR Group

Choose the automated alternate routing (AAR) group for this
                                             					 device. The AAR group provides the prefix digits that are used to route calls
                                             					 that are otherwise blocked due to insufficient bandwidth.

Set AAR Group to <None> to prevent rerouting blocked
                                             					 calls.

Retain this destination in the call forwarding history

Checking this check box allows the AAR leg of the call to be
                                             					 present in the Call History.

Visual Message Waiting Indicator Policy

Use this field to configure the handset lamp illumination
                                             					 policy. Choose one of the following options:

Use System Policy (The directory number refers to the service parameter "Message Waiting Lamp Policy" setting.)

Light and Prompt

Prompt Only

Light Only

None

Setting applies only to the current device unless you check
                                             					 the Update Shared Device Settings check box
                                             					 and click the Propagate Selected button. (The check box
                                             				  displays only if other devices share this directory number.)

Audible Message Waiting Indicator Policy

Use this field to configure an audible message waiting
                                             					 indicator policy. Choose one of the following options:

Off

On —When you select this option, you will receive a stutter dial tone when you take the handset off hook.

Default —When you select this option, the phone uses the default that was set at the system level.

Call Pickup Group Audio Alert Setting (Phone Idle)

This field determines the type of notification an incoming
                                             					 call sends to members of a call pickup group. If the called phone does not
                                             					 answer, the phones in the call pickup group that are idle will either hear a
                                             					 short ring (ring once) or hear nothing (disabled).

Use System Default —The value of this field gets determined by the setting of the Cisco CallManager service parameter Call Pickup Group Audio
                                                   Alert Setting of Idle Station.

Disable —No alert is sent to members of the call pickup group.

Ring Once —A short ring is sent to members of the call pickup group.

Call Pickup Group Audio Alert Setting (Phone Active)

This field determines the type of notification an incoming
                                             					 call sends to members of a call pickup group. If the called phone does not
                                             					 answer, the phones in the call pickup group that are busy will either hear a
                                             					 beep only or hear nothing (disabled).

Use System Default —The value of this field gets determined by the setting of the Cisco CallManager service parameter Call Pickup Group Audio
                                                   Alert Setting of Busy Station.

Disable —No alert is sent to member of the call pickup group.

Beep Only —A beep is sent to members of the call pickup group.

Recording Option

This field determines the recording option on the line
                                             					 appearance of an agent. By default, the recording option specifies Call
                                             					 Recording Disabled.

Choose one of the following options:

Call Recording Disabled —The calls that the agent makes on this line appearance are not recorded.

Automatic Call Recording Enabled —The calls that the agent makes on this line appearance are automatically recorded.

Application Invoked Call Recording Enabled —The calls that the agent makes on this line appearance are recorded if an application invokes calling recording.

When the recording option is set to either Automatic Call
                                             					 Recording Enabled or Application Invoked Call Recording Enabled, the line
                                             					 appearance can be associated with a recording profile.

When automatic recording is enabled, the application's
                                             					 recording requests get rejected.

Recording Profile

This field determines the recording profile on the line
                                             					 appearance of an agent.

Monitoring Calling Search Space

The monitoring calling search space of the supervisor line
                                             					 appearance must include the agent line or device partition to allow monitoring
                                             					 the agent.

Set the monitoring calling search space on the supervisor line
                                             					 appearance window. Choose an existing calling search space from the drop-down
                                             					 list box.

The default value specifies None.

Call Forward and Pickup Settings

Forward All Voice Mail

Check this check box if you want calls to forward to the
                                             					 number that you chose in the voice-mail profile.

Checking this check box makes the Forward All Destination field
                                             					 and Forward All Calling Search Space check box not
                                             					 relevant.

Forward All Destination

Enter the directory number or directory URI to which all calls are forwarded.

The setting applies to any dialable phone number, including
                                                         						an outside destination unless restricted, and to all devices that are using
                                                         						this directory number.

Forward All Calling Search Space

Choose the calling search space to use when calls are
                                             					 forwarded to the specified destination.

This setting applies to all devices that are using this
                                                         						directory number.

Secondary Calling Search Space for Forward All

Choose the secondary calling search space (CSS) from the
                                             					 drop-down list box.

Because Call Forwarding is a line-based feature, in cases
                                             					 where the device calling search space is unknown, the system uses only the line
                                             					 calling search space to forward the call. If the line calling search space is
                                             					 restrictive and not routable, the forward attempt fails.

Addition of a secondary calling search space for Call Forward All provides a solution to enable forwarding. The primary calling
                                             search space for Call Forward All and secondary calling search space for Call Forward All get concatenated (Primary CFA CSS + Secondary CFA CSS) when Call Forward All is processed. Unified Communications Manager uses this combination to validate the CFA destination and to forward the call.

Forward Busy Internal Voice Mail

Check this check box if you want calls from an internal number
                                             					 to be forwarded to a number that you chose in the voice-mail profile.

Checking this check box makes the Forward Busy Internal
                                             					 Destination field and Calling Search Space check box not relevant.

Forward Busy Internal Destination

Enter the directory number or directory URI to which an internal call is
                                             					 forwarded when the line is in use.

This setting applies to any internal, dialable phone number
                                                         						and to all devices that are using this directory number.

Forward Busy Internal Calling Search Space

Choose the calling search space to use when internal calls are
                                             					 forwarded to the specified destination.

This setting applies to all devices that are using this
                                                         						directory number.

Forward Busy External Voice Mail

Check this check box if you want calls from an external number
                                             					 to be forwarded to a number that you chose in the voice-mail profile.

Checking this check box makes the Forward Busy
                                                						External Destination field and Calling Search Space check box not
                                             					 relevant.

Forward Busy External Destination

Enter the directory number or directory URI to which an external call is
                                             					 forwarded when the line is in use.

This setting applies to any dialable external phone number,
                                                         						including an outside destination unless restricted, and to all devices that are
                                                         						using this directory number.

Forward Busy External Calling Search Space

Choose the calling search space to use when external calls are
                                             					 forwarded to the specified destination.

This setting applies to all devices that are using this
                                                         						directory number.

Forward No Answer Internal Voice Mail

Check this check box if you want calls from an internal number
                                             					 forwarded to the number that you chose in the voice-mail profile.

Checking this check box makes the Forward No Answer Internal Destination field and Calling Search Space check box not
                                             					 relevant.

Forward No Answer Internal Destination

Enter a directory number or directory URI to which an internal call is
                                             					 forwarded when the phone is not answered.

This setting applies to any internal, dialable phone number
                                                         						and to all devices that are using this directory number.

Forward No Answer Internal Calling Search Space

Choose the calling search space to use when internal calls are
                                             					 forwarding to the specified destination. The setting displays only if it is
                                             					 configured in the system.

This setting applies to all devices that are using this
                                                         						directory number.

Forward No Answer External Voice Mail

Check this check box if you want calls to forward to an
                                             					 external number that you chose in the voice-mail profile.

Checking this check box makes the Forward No Answer Externally Destination field and External Calling Search Space check box
                                             					 not relevant.

Forward No Answer External Destination

Enter a directory number or directory URI to which an external call is
                                             					 forwarded when the phone is not answered.

This setting applies to any external, dialable phone number,
                                                         						including an outside destination unless restricted, and to all devices that are
                                                         						using this directory number.

Forward No Answer External Calling Search Space

Choose the calling search space to use when external calls are
                                             					 forwarded to the specified destination. The setting displays only if it is
                                             					 configured in the system.

This setting applies to all devices that are using this
                                                         						directory number.

Forward No Coverage Internal Voice Mail

Check this check box if you want calls from an internal number
                                             					 forwarded to the number that you chose in the voice-mail profile.

Checking this check box makes the Forward No Answer Destination field and Calling Search Space check box not
                                             					 relevant.

Forward No Coverage Internal Destination

Enter a directory number or directory URI to which an internal call is
                                             					 forwarded when the phone has no coverage.

This setting applies to any internal, dialable phone number
                                                         						and to all devices that are using this directory number.

Forward No Coverage Internal Calling Search Space

Choose the calling search space to use when internal calls are
                                             					 forwarded to the specified destination. The setting displays only if it is
                                             					 configured in the system.

This setting applies to all devices that are using this
                                                         						directory number.

Forward No Coverage External Voice Mail

Check this check box if you want calls from an external number
                                             					 to be forwarded to the number that you chose in the voice-mail profile.

Checking this check box makes the Forward No Answer
                                                						Destination field and Calling Search Space check box not
                                             					 relevant.

Forward No Coverage External Destination

Enter a directory number or directory URI to which an external call is
                                             					 forwarded when the phone has no coverage.

This setting applies to any dialable phone number, which
                                                         						includes an outside destination unless restricted, and to all devices that are
                                                         						using this directory number.

Forward No Coverage External Calling Search Space

Choose the calling search space to use when external calls are
                                             					 forwarded to the specified destination. The setting displays only if it is
                                             					 configured in the system.

This setting applies to all devices that are using this
                                                         						directory number.

Forward on CTI Failure Voice Mail

The Forward on CTI Failure field applies
                                             					 only to CTI route points and CTI ports. The settings in this row specify the
                                             					 forwarding treatment for external calls to this CTI route point or CTI port if
                                             					 the CTI route point or CTI port fails.

Check this check box to use settings in the Voice Mail Profile Configuration window.

When this check box is checked, Unified Communications Manager ignores the settings in the Destination box and Calling Search Space. When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to forward to the voice-messaging system, you must uncheck
                                             the Voice Mail check box for external calls.

Forward on CTI Failure Destination

This setting specifies the directory number or directory URI to which an
                                             					 internal, nonconnected call is forwarded when an application that controls that
                                             					 directory number fails. Use any dialable phone number, including an outside
                                             					 destination.

When you enter a destination value for internal calls, the
                                             					 system automatically copies this value to the Destination field for external calls. If
                                             					 you want external calls to forward to a different destination, you must enter a
                                             					 different value in the Destination field for external calls.

Forward on CTI Failure Calling Search Space

This setting applies to all devices that are using this
                                             					 directory number.

When you choose a Calling Search Space for internal calls, the
                                             					 system automatically copies this setting to the Calling Search Space setting
                                             					 for external calls. If you want external calls to forward to a different
                                             					 calling search space, choose a different setting in the Calling Search Space
                                             					 for external calls.

No Answer Ring Duration

Enter the number of seconds to allow the call to ring before
                                             					 the system forwards the call to the Forward No Answer Destination.

Call Pickup Group

Choose a Pickup Group Name to specify the call pickup
                                             				  group, which can answer incoming calls to this directory number by dialing the
                                             				  appropriate pickup group number.

Park Monitoring

Park Monitoring Forward No Retrieve Destination External

When the parkee is an external party, then the call will be
                                             					 forwarded to the specified destination in the parker’s Park Monitoring Forward
                                             					 No Retrieve Destination External parameter. If the Park Monitoring Forward No Retrieve Destination External field value is empty, the parkee will be redirected to the parker’s line.

Park Monitoring Forward No Retrieve Destination Internal

When the parkee is an internal party, then the call will be
                                             					 forwarded to the specified destination in the parker’s Park Monitoring Forward
                                             					 No Retrieve Destination Internal parameter. If the Park Monitoring Forward No Retrieve Destination Internal field value is empty, the parkee will be redirected to the parker’s
                                             					 line.

Park Monitoring Reversion Timer

This parameter determines the number of seconds that Unified Communications Manager waits before prompting the user to retrieve a call that the user parked. This timer starts when the user presses the Park
                                             softkey on the phone, and a reminder is issued when the timer expires.

Default: 60 seconds

If you configure a non-zero value, this value overrides the
                                                         						value of this parameter set in the Service Parameters window. However, if
                                                         						you configure a value of 0 here, then the value in the Service Parameters window will be used.

Park Monitoring Forward No Retrieve Internal Voice Mail

Check this check box to use settings in the Voice Mail Profile Configuration window.

When this check box is checked, Unified Communications Manager ignores the settings in the Destination box and Calling Search Space.

Park Monitoring Forward No Retrieve Destination External Voice Mail

Check this check box to use settings in the Voice Mail Profile Configuration window.

When this check box is checked, Unified Communications Manager ignores the settings in the Destination box and Calling Search
                                                         Space.

Park Monitoring Forward No Retrieve External CSS

Choose the calling search space to apply to the directory
                                             					 number.

Park Monitoring Forward No Retrieve Internal CSS

Choose the calling search space to apply to the directory
                                             					 number.

Forward Unregistered Internal Voice Mail

This field applies to unregistered internal DN calls. The
                                             					 calls are rerouted to a specified Destination Number or Voice Mail.

Check this check box if you want calls from an unregistered
                                             					 internal number to be forwarded to a number that you chose in the voice-mail
                                             					 profile.

Checking this check box makes the Forward Unregistered Internal
                                                						Destination field and Calling Search Space drop-down list box
                                             					 not relevant.

Forward Unregistered Internal Destination

Enter the directory number to which an unregistered internal
                                             					 call is forwarded when the line is in use.

This setting applies to any internal, dialable phone number
                                             					 and to all devices that are using this directory number.

Forward Unregistered Internal CSS

Choose the calling search space to use when unregistered
                                             					 internal calls are forwarded to the specified destination.

This setting applies to all devices that are using this
                                             					 directory number.

Forward Unregistered External Voice Mail

This field applies to unregistered external DN calls. The
                                             					 calls are rerouted to a specified Destination Number or Voice Mail.

You must also specify the maximum number of forwards in the Service Parameters Configuration window
                                                         						for a Directory Number.

Forward Unregistered External Destination

Enter the directory number to which an external call is
                                             					 forwarded when the line is in use.

This setting applies to any dialable external phone number,
                                             					 including an outside destination unless restricted, and to all devices that are
                                             					 using this directory number.

Forward Unregistered External CSS

Choose the calling search space to use when external calls are
                                             					 forwarded to the specified destination.

This setting applies to all devices that are using this
                                             					 directory number.

Multilevel Precedence and Preemption Alternate Party Settings

Target (Destination)

Enter the number to which MLPP precedence calls should be
                                             					 directed if this directory number receives a precedence call and neither this
                                             					 number nor its call forward destination answers the precedence call.

Values can include numeric characters, pound
                                             					 ( # ), and asterisk ( * ).

MLPP Calling Search Space

From the drop-down list box, choose the calling search space
                                             					 to associate with the alternate party target (destination) number.

MLPP No Answer Ring Duration (Seconds)

Enter the number of seconds (between 4 and 30) after which an
                                             					 MLPP precedence call will get directed to the alternate party of this directory
                                             					 number if this directory number and its call forwarding destination have not
                                             					 answered the precedence call.

Leave this setting blank to use the value that is set in the Unified Communications Manager enterprise parameter, Precedence Alternate Party Timeout.

Line Settings for This Phone

Display (Internal Caller ID)

Use this field only if you do not want the directory number to
                                             					 show on the line appearance. Enter text that identifies this directory number
                                             					 for a line/phone combination.

Suggested entries include name of the boss, department, or
                                             					 other appropriate information to identify multiple directory numbers to
                                             					 secretary/assistant who monitors multiple directory numbers.

ASCII Display (Internal Caller ID)

This field provides the same information as the Display (Internal Caller ID) field, but
                                             					 you must limit input to ASCII characters. Devices that do not support Unicode
                                             					 (internationalized) characters display the content of the ASCII Display (Internal Caller ID) field.

Setting applies only to the current device unless you check
                                             					 the check box at right (Update Shared Device Settings) and click the Propagate Selected button. (The check
                                             					 box at right displays only if other devices share this directory number.)

Line Text Label

Enter text that identifies this directory number for a
                                             					 line/phone combination.

The default language specifies English

External Phone Number Mask

Enter the phone number (or mask) that is sent for Caller ID
                                             					 information when a call is placed from this line.

You can enter a maximum of 24 numbers and "X" characters. The Xs represent the directory number and
                                             					 must appear at the end of the pattern. For example, if you specify a mask of
                                             					 972813XXXX, an external call from extension 1234 displays a caller ID number of
                                             					 9728131234.

Visual Message Waiting Indicator Policy

Use this field to configure the handset lamp illumination
                                             					 policy. Choose one of the following options:

Use System Policy (The directory number refers to the service parameter "Message Waiting Lamp Policy" setting.)

Light and Prompt

Prompt Only

Light Only

None

Setting applies only to the current device unless you check
                                             					 the Update Shared Device Settings check box
                                             					 and click the Propagate Selected button. (The check box
                                             					 displays only if other devices share this directory number.)

Audible Message Waiting Indicator Policy

Use this field to configure an audible message waiting
                                             					 indicator policy. Choose one of the following options:

Off

On —When you select this option, you will receive a stutter dial tone when you take the handset off hook.

Default —When you select this option, the phone uses the default that was set at the system level.

Ring Setting (Phone Idle)

Choose the ring setting for the line appearance when an
                                             					 incoming call is received and no other active calls exist on that device.
                                             					 Choose one of the following options:

Use system default

Disable

Flash only

Ring once

Ring

Ring Setting (Phone Active)

Choose the ring setting that is used when this phone has
                                             					 another active call on a different line. Choose one of the following options:

Use system default

Disable

Flash only

Ring once

Ring

Beep only

Call Pickup Group Audio Alert Setting (Phone Idle)

This field determines the type of notification an incoming
                                             					 call sends to members of a call pickup group. If the called phone does not
                                             					 answer, the phones in the call pickup group that are idle will either hear a
                                             					 short ring (ring once) or hear nothing (disabled).

Use System Default —The value of this field gets determined by the setting of the Cisco CallManager service parameter Call Pickup Group Audio
                                                   Alert Setting of Idle Station.

Disable —No alert is sent to members of the call pickup group.

Ring Once —A short ring is sent to members of the call pickup group.

Call Pickup Group Audio Alert Setting (Phone Active)

This field determines the type of notification an incoming
                                             					 call sends to members of a call pickup group. If the called phone does not
                                             					 answer, the phones in the call pickup group that are busy will either hear a
                                             					 beep only or hear nothing (disabled).

Use System Default —The value of this field gets determined by the setting of the Cisco CallManager service parameter Call Pickup Group Audio
                                                   Alert Setting of Busy Station.

Disable —No alert is sent to member of the call pickup group.

Beep Only —A beepis sent to members of the call pickup group.

Recording Option

This field determines the recording option on the line
                                             					 appearance of an agent. By default, the recording option specifies Call
                                             					 Recording Disabled.

Choose one of the following options:

Call Recording Disabled —The calls that the agent makes on this line appearance are not recorded.

Automatic Call Recording Enabled —The calls that the agent makes on this line appearance are automatically recorded.

Application Invoked Call Recording Enabled —The calls that the agent makes on this line appearance are recorded if an application invokes calling recording.

When the recording option is set to either Automatic Call
                                             					 Recording Enabled or Application Invoked Call Recording Enabled, the line
                                             					 appearance can be associated with a recording profile.

When automatic recording is enabled, the application’s
                                             					 recording requests get rejected.

Recording Profile

This field determines the recording profile on the line
                                             					 appearance of an agent. Choose an existing recording profile from the drop-down
                                             					 list box. To create a recording profile, use the Device > Device
                                                   						  Settings > Recording Profile menu
                                             					 option.

The default value specifies None.

Monitoring Calling Search Space

The monitoring calling search space of the supervisor line
                                             					 appearance must include the agent line or device partition to allow monitoring
                                             					 the agent.

Set the monitoring calling search space on the supervisor line
                                             					 appearance window. Choose an existing calling search space from the drop-down
                                             					 list box.

The default value specifies None.

Log Missed Calls

This check box allows you to turn this feature on or off. If the check box displays as checked (turned on), which is the default
                                             for this setting, Unified Communications Manager logs missed calls in the call history for that directory number on the phone.

Forward All CSS Activation Policy

Select one of the following options from the drop-down list
                                             					 box:

Use System Default

With Configured CSS

With Activating Device/Line CSS

If you select the With Configured CSS option, the Forward All
                                             					 Calling Search Space that is explicitly configured in the Directory Number Configuration window
                                             					 controls the forward all activation and call forwarding. If the Forward All
                                             					 Calling Search Space is set to None, no CSS gets configured for Forward All. A
                                             					 forward all activation attempt to any directory number with a partition will
                                             					 fail. No change in the Forward All Calling Search Space and Secondary Calling
                                             					 Search Space for Forward All occurs during the forward all activation.

If you prefer to utilize the combination of the Directory
                                             					 Number Calling Search Space and Device Calling Search Space without explicitly
                                             					 configuring a Forward All Calling Search Space, select With Activating
                                             					 Device/Line CSS for the Calling Search Space Activation Policy. With this
                                             					 option, when Forward All is activated from the phone, the Forward All Calling
                                             					 Search Space and Secondary Calling Search Space for Forward All automatically
                                             					 gets populated with the Directory Number Calling Search Space and Device
                                             					 Calling Search Space for the activating device.

Hold Reversion Ring Duration (seconds)

Enter a number from 0 to 1200 (inclusive) to specify the wait
                                             					 time in seconds before issuing a reverted call alert to the holding party
                                             					 phone.

If you enter a value of 0, Unified Communications Manager does not invoke the reverted call feature for a held call.

Hold Reversion Notification Interval (seconds)

Enter a number from 0 to 1200 (inclusive) to specify the
                                             					 interval time in seconds for sending periodic reminder alerts to the holding
                                             					 party phone.

If you enter a value of 0, Unified Communications Manager does not send reminder alerts.

Party Entrance Tone

Choose one of the following options from the drop-down list
                                             					 box:

Default —Use the value that you configured in the Party Entrance Tone service parameter.

On —A tone plays on the phone when a basic call changes to a multi party call; that is, a barge call, cBarge call, ad hoc conference,
                                                   meet-me conference, or a joined call. In addition, a different tone plays when a party leaves the multi party call. If the
                                                   controlling device, that is, the originator of the multi party call has a built-in bridge, the tone gets played to all parties
                                                   if you choose On for the controlling device. When the controlling device, for example, the conference controller, no longer
                                                   remains present on the call or if the controlling device cannot play the tone, Unified Communications Manager does not play the tone even if you choose On.

Off —A tone does not play on the phone when a basic call changes to a multi party call.

Multiple Call/Call Waiting Settings

Maximum Number of Calls

You can configure up to 184 calls for a line on a device in a
                                             					 cluster, with the limiting factor being the device. As you configure the number
                                             					 of calls for one line, the calls that are available for another line decrease.

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
                                             					 will get forwarded if Call Forward Busy is set). If this line is shared, be
                                             					 aware that all the lines must be busy before incoming calls get rejected.

Use this field in conjunction with Maximum Number of Calls for
                                             					 CTI route points. The default specifies 4500 calls.

Forwarded Call Information Display for This
                                                						Device

Caller Name

Check this check box to include the caller name in the display
                                             					 when a forwarded call is received. Default leaves this check box checked.

Caller Number

Check this check box to include the caller number in the
                                             					 display when a forwarded call is received.

Redirected Number

Check this check box to include the redirected number in the
                                             					 display when a forwarded call is received.

Dialed Number

Check this check box to include the dialed number in the
                                             					 display when a forwarded call is received. The default setting leaves this
                                             					 check box checked.

Directory URI Fields

URI (1-5) on Directory Number

Enter a directory URI to associate with the directory number for this phone. Follow the username@host format. Enter a username
                                             of up to 47 alphanumeric characters. For the host address, enter an IPv4 address or fully qualified domain name. You can associate
                                             up to five directory URIs to a single directory number.

URI (1-5) Route Partition on Directory Number

Enter the partition on which the directory URI belongs. If you do not want to restrict access to the directory URI, leave
                                             the field blank.

URI (1-5) Is Primary on Directory Number

Enter a ' t ' (True) to indicate that this directory URI is the primary directory URI for this extension. Otherwise, enter an ' f' (False) to indicate that this is not the primary directory URI for this extension.

You can associate up to five directory URIs to a single directory number, but you must select a single primary directory
                                                         URI.

### BAT Template Field Descriptions to Add Intercom Template

The following table provides descriptions of all possible fields that display when you add an Intercom template in a BAT phone,
                                 gateway, or UDP template. Some device types do not require all the phone settings. Only some fields show the values that were
                                 configured in Unified Communications Manager Administration. Field names that have an asterisk in the BAT user interface require an entry. Treat fields that do not have
                                 an asterisk as optional.

Field

Description

Intercom Directory Number Information

Intercom Template Name

Enter a unique name for the intercom template.

Route Partition

Choose a route partition to which the directory number
                                             					 belongs.

The directory number can appear in more than one partition.

Description

Enter a description of the directory number and route
                                             					 partition. The description can include up to 50 characters in any language, but
                                             					 it cannot include double-quotes (""), percentage sign
                                             					 ( % ), ampersand ('), or angle brackets
                                             					 (<>).

Display (Internal Caller ID)

Use this field only if you do not want the directory number to
                                             					 show on the line appearance. Enter text that identifies this directory number
                                             					 for a line/phone combination.

Suggested entries include name of the boss, department, or
                                             					 other appropriate information to identify multiple directory numbers to a
                                             					 secretary or assistant who monitors multiple directory numbers.

ASCII Display (Internal Caller ID)

This field provides the same information as the Display (Internal Caller ID) field, but
                                             					 you must limit input to ASCII characters. Devices that do not support Unicode
                                             					 (internationalized) characters display the content of the ASCII Display (Internal Caller ID) field.

Setting applies only to the current device unless you check
                                             					 the check box at right (Update Shared Device Settings) and click the Propagate Selected button. (The check box at right displays only if
                                             					 other devices share this directory number.)

Line Text Label

Enter text that identifies this directory number for a
                                             					 line/phone combination.

The default language specifies English

Alerting Name

This name represents the name that displays during an alert to
                                             					 a shared directory number. For non-shared directory numbers, during alerts, the
                                             					 system uses the name that is entered in the Display field.

Alerting Name ASCII

This field provides the same information as the Alerting Name
                                             					 field, but you must limit input to ASCII characters. Devices that do not
                                             					 support Unicode (internationalized) characters display the content of the Alerting Name ASCII field.

Speed Dial

Enter the number that you want the system to dial when the
                                             					 user presses the speed-dial button. You can enter digits 0 through 9, * , # , and + , which is the international escape
                                             					 character.

External Phone Number Mask

Enter the phone number (or mask) that is sent for Caller ID
                                             					 information when a call is placed from this line.

You can enter a maximum of 24 numbers and "X" characters. The Xs represent the directory number and
                                             					 must appear at the end of the pattern. For example, if you specify a mask of
                                             					 972813XXXX, an external call from extension 1234 displays a caller ID number of
                                             					 9728131234.

Intercom Directory Number Settings

Calling Search Space

From the drop-down list box, choose the appropriate calling
                                             					 search space. A calling search space comprises a collection of partitions that
                                             					 are searched for numbers that are called from this directory number. The value
                                             					 that you choose applies to all devices that are using this directory number.

Presence Group

Configure this field with the presence feature.

From the drop-down list box, choose a Presence Group for this
                                             					 directory number. The selected group specifies the devices, end users, and
                                             					 application users that can monitor this directory number.

Auto Answer

Choose one of the following options to activate the auto
                                             					 answer feature for this directory number:

- Auto
                                                   					 Answer Off <Default>

- Auto Answer
                                                   					 with Headset

- Auto Answer
                                                   					 with Speakerphone

Do not configure auto answer for devices that have shared
                                                         						lines.

Default Activated Device

From the drop-down list box, choose a default activated device
                                             					 for this directory number. The selected device specifies the phone on which
                                             					 this directory number is activated by default. The drop-down list box lists
                                             					 only devices that support intercom.

You must specify a default activated device for this
                                                         						intercom directory number to be active as an intercom line.

If an intercom DN is specified in a device profile that is
                                                         						configured for Cisco Extension Mobility, that intercom DN will display as an
                                                         						intercom line only when a user logs in to the specified default activated
                                                         						device by using that device profile, as long as the device supports the
                                                         						intercom feature.

### Create Phone CSV Data File Using BAT Spreadsheet

Use the BAT spreadsheet to create the CSV data file. You can define
                                 		  the file format within the spreadsheet, and the BAT spreadsheet uses the data
                                 		  file formats to display the fields for the CSV data file.

If you enter a comma in one of the fields, BAT.xlt encloses that
                                             			 field entry in double quotes when you export to BAT format.

If you enter a blank row in the BAT spreadsheet, the system treats
                                             			 the empty row as the end of the file and does not convert data that is entered
                                             			 after a blank line to the BAT format.

You can use the dummy MAC address option when adding CTI ports. This option gives a unique device name to each CTI port in
                                 the form of dummy MAC addresses that you can manually update later using the or the UnifiedCM Auto-Register phone Tool. Do not use the dummy MAC address option for H.323 clients, VGC phones, or VGC
                                 virtual phones.

The dummy MAC address option automatically generates dummy MAC
                                 		  addresses in the following format:

XXXXXXXXXXXX

where X represents any 12-character, hexadecimal (0-9 and A-F) number.

Attention

The number of lines and speed dials that you define for phones in
                                             			 the BAT spreadsheet must not exceed the numbers that are defined in the BAT
                                             			 phone template, otherwise, an error occurs when you attempt to insert the CSV
                                             			 data file and BAT template.

After you have finished editing all the fields in the BAT spreadsheet,
                                 		  you can export the content to a CSV formatted data file. A default filename is
                                 		  assigned to the exported CSV formatted data file:

<tabname>-<timestamp>.txt

where <tabname> represents the type of input file that
                                 		  you created, such as phones, and <timestamp> represents the precise date and time
                                 		  that the file was created.

You can rename the CSV formatted data file after you save the exported
                                 		  file to your local workstation.

You cannot upload a CSV filename that contains a comma (for example, abcd,e.txt) to the server.

Step 1

To open the BAT spreadsheet, locate and double-click the BAT.xlt
                                          			 file

Step 2

When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities.

Step 3

To display the phones options, click the Phones tab at the bottom of the spreadsheet.

Step 4

Choose the radio button for one of the following device types:

The device type that you select determines the validation criteria
                                             				for data in the BAT spreadsheet.

Phones

CTI Port

H.323 Client

VGC Phones

VGC Virtual Phones

Cisco IP Communicator Phone

Step 5

Choose the device and line fields to appear in the BAT spreadsheet
                                          			 for each phone. Do the following:

Click Create File Format .

To choose the device fields, click a device field name in
                                                				  the Device Field box and then click the arrow to move
                                                				  the field to the Selected Device Fields box.

A CSV data file must include MAC Address/Device Name and Description ; therefore, these fields
                                                   					 always remain selected.

Tip

To select a range of items in the list, hold down the Shift key. To select random field
                                                               						names, hold down the Ctrl key and click field names.

Click a line field name in the Line Field box and click the arrow to move
                                                				  the field to the Selected Line Fields box.

Tip

To change the order of the items in the Selected Line and Device boxes, choose an item and use
                                                               						the up and down arrows to move the field up or down in the list.

A message asks whether you want to overwrite the existing CSV
                                                				  format. Click Create to modify the CSV data file format.

Click OK .

Step 6

Scroll to the right to locate the Number of Phone Lines box and enter the number
                                          			 of lines for the phone.

The number of lines you enter must not exceed the number of lines that are configured in the BAT template.

Step 7

For phones, you must enter the number of speed-dial buttons in the Maximum Number of Speed Dials box.

The number of speed dials you enter must not exceed the number of speed dials that are configured in the BAT template.

Step 8

Enter the number of Busy Lamp Field (BLF) speed-dial buttons in
                                          			 the Maximum Number of BLF Speed Dials box.

Step 9

Enter data for an individual phone on each line in the
                                          			 spreadsheet.

Complete all mandatory fields and any relevant, optional fields. Each column heading specifies the length of the field and
                                             whether it is required or optional. See online help for phone field descriptions.

Step 10

If you did not enter the MAC address for each phone, check the Create Dummy MAC Address check box.

Attention

Do not use the dummy MAC address option for H.323 clients, VGC
                                                         				  phones, or VGC virtual phones.

Step 11

To transfer the data from the BAT Excel spreadsheet into a CSV
                                          			 formatted data file, click Export to BAT Format .

Tip

For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 phones window in BAT.

### Phone Field
                           	 Descriptions in BAT Spreadsheet

The
                                 		  following table provides descriptions of the phone fields that are available
                                 		  for adding device and line details in a CSV data file.

Field

Description

Device Fields

MAC
                                             					 Address/Device Name

Enter the
                                             					 MAC address for phones, VGC virtual phones, and VGC phones. Enter a unique
                                             					 identifier (Device Name) for the CTI port or H.323 client. You can check the Create Dummy MAC Addresses check box to
                                             					 automatically generate unique device identifiers.

Description

Enter a
                                             					 description such as "Conference
                                                						Room A" or "John
                                                						Smith" that identifies the phone or device. The description can include up
                                             					 to 50 characters in any language, but it cannot include double-quotes ( " ), percentage sign
                                             					 ( % ),
                                             					 ampersand (&), back-slash ( \ ), or angle brackets (<>).

Media
                                             					 Resource Group List

Enter the
                                             					 media resource group list (MRGL) for this group of phones/ports.

An MRGL
                                             					 specifies a list of prioritized media resource groups. An application can
                                             					 choose required media resources from the available ones according to the order
                                             					 that is defined in the MRGL.

User Hold
                                             					 Audio Source

Enter the
                                             					 user hold audio source that this group of IP phones or CTI ports should use.

The user
                                             					 hold audio source identifies the audio source from which music is played when a
                                             					 user places a call on hold.

Network Hold
                                             					 MOH Audio Source

Enter the
                                             					 network hold audio source that this group of IP phones or CTI ports should use.

The network
                                             					 hold audio source identifies the audio source from which music is played when
                                             					 the system places a call on hold, such as when the user transfers or parks a
                                             					 call.

User Locale

Enter the
                                             					 country and language set that you want to associate with this group of IP
                                             					 phones.

This choice determines which cultural-dependent attributes exist for this user and which language displays for the user in
                                             the Unified Communications Manager user windows and phones.

Network
                                             					 Locale

Enter the
                                             					 network locale that you want to associate with this group of phones.

The Network
                                             					 Locale comprises a set of tones and cadences that Cisco gateways and phones use
                                             					 when they communicate with the PSTN and other networks in a specific
                                             					 geographical area.

Softkey
                                             					 Template

Enter the
                                             					 softkey template to be used for all phones in this group.

Common Phone
                                             					 Profile

From the
                                             					 drop-down list box, choose a common phone profile from the list of available
                                             					 common phone profiles.

Device
                                             					 Presence Group

Used with
                                             					 the Presence feature, the phone that is running SIP or SCCP serves as a watcher
                                             					 because it requests status about the presence entity; for example, directory
                                             					 number, that is configured as a BLF speed dial button on the phone.

If you want
                                             					 the phone to receive the status of the presence entity, choose a Presence Group
                                             					 that is allowed to view the status of the Presence Group that is applied to the
                                             					 directory number, as indicated in the Presence Group Configuration window.

Phone Load
                                             					 Name

Enter the
                                             					 custom phone load, if applicable.

Any value
                                                         						that is entered in this field overrides the default value for the chosen phone.

Value does
                                             					 not apply for CTI ports.

Security
                                             					 Profile

Enter the security profile that you want to apply to the device. If the phone does not support the profile that you choose, Unified Communications Manager does not allow you to apply the configuration.

All phones
                                             					 require that you apply a security profile. If the phone does not support
                                             					 security, choose a nonsecure profile.

Device
                                             					 SUBSCRIBE CSS

Used with the presence feature, the SUBSCRIBE Calling Search Space determines how Unified Communications Manager routes the subscription requests that come from the phone. Enter the calling search space that you want to use for this purpose.

E.164

Choose the
                                             					 E.164 address that is registered with the gatekeeper.

Ensure
                                                         						the H.323 client is configured as a gatekeeper-controlled device.

You must
                                                         						enter a value in this field for a gatekeeper-controlled H.323 client. You can
                                                         						enter only numbers (0-9) and special characters # and * in this field.

UserID

Enter the
                                             					 user ID for the phone user.

Media
                                             					 Resource Group List

This list
                                             					 provides a prioritized grouping of media resource groups. An application
                                             					 chooses the required media resource, such as a Music On Hold server, from among
                                             					 the available media resources according to the priority order that is defined
                                             					 in a Media Resource List.

AAR
                                             					 Calling Search Space

Enter the
                                             					 appropriate calling search space for the device to use when it performs
                                             					 automated alternate routing (AAR). The AAR calling search space specifies the
                                             					 collection of route partitions that are searched to determine how to route a
                                             					 collected (originating) number that is otherwise blocked due to insufficient
                                             					 bandwidth.

MLPP
                                             					 Domain

Enter a
                                             					 hexadecimal value for the MLPP domain that is associated with this device.
                                             					 Ensure that this value is blank or a value between 0 and FFFFFF

MLPP
                                             					 Indication

If
                                             					 available, this setting specifies whether a device that is capable of playing
                                             					 precedence tones will use the capability when it places an MLPP precedence
                                             					 call.

- Default —This
                                                				  device inherits its MLPP indication setting from its device pool.

- Off —This device
                                                				  does not handle nor process indication of an MLPP precedence call.

- On —This device
                                                				  does handle and process indication of an MLPP precedence call.

MLPP
                                             					 Preemption

If
                                             					 available, this setting specifies whether a device that is capable of
                                             					 preempting calls in progress will use the capability when it places an MLPP
                                             					 precedence call.

- Default —This
                                                				  device inherits its MLPP indication setting from its device pool.

- Off —This device
                                                				  does not handle nor process indication of an MLPP precedence call.

- On —This device
                                                				  does handle and process indication of an MLPP precedence call.

Signal
                                             					 Packet Capture Mode

Enter the
                                             					 mode that you want to set for signal packet capture:

- None —Choose None
                                                				  if you do not want to specify a mode.

- Real-Time Mode —Use
                                                				  this mode for real-time signal packet capture.

- Batch Processing
                                                   					 Mode —Use this mode for batch processing signal packet capture mode.

Packet
                                             					 Capture Duration

Enter the
                                             					 time for packet capture in minutes. You can enter a maximum duration of 300
                                             					 minutes.

Authentication String

Enter a
                                             					 numeric string that contains 4 to 10 digits. To install, upgrade, or
                                             					 troubleshoot a locally significant certificate, the phone user or administrator
                                             					 must enter the authentication string on the phone.

Ignore
                                             					 Presentation Indicator

Enter Yes or No to configure call display restrictions on a call-by-call basis. When this check box is checked, Unified Communications Manager ignores any presentation restriction that is received for internal calls.

SIP
                                             					 Profile

Enter the
                                             					 default SIP profile or a specific profile that was previously created. SIP
                                             					 profiles provide specific SIP information for the phone such as default
                                             					 telephony event payload type, registration and keep alive timers, media ports,
                                             					 Iris, and dynamic DNS server addresses.

Digest
                                             					 User

Used with
                                             					 digest authentication (SIP security), choose an end user that you want to
                                             					 associate with the phone.

Ensure
                                             					 that you configured digest credentials for the user that you choose, as
                                             					 specified in the End User Configuration window.

After you
                                             					 save the phone configuration and reset the phone, the digest credentials for
                                             					 the user get added to the phone configuration file.

Log Out
                                             					 Profile

Enter the profile that a phone should load when an extension mobility user logs out. You must configure logout profiles in Unified Communications Manager Administration.

Use Current Device
                                                					 Setting —This choice creates an autogenerated device profile as the
                                             				  default device profile.

Select a User Device
                                                					 Profile —This choice assigns a user device profile, which has already
                                             				  been defined, that becomes the default device profile for this device.

The chosen
                                             					 user device profile gets loaded onto the device when no user is logged in.

SIPCodec_MTPPreferredOrigCodec

Enter the
                                             					 codec to use if a media termination point is required for SIP calls.

Dial Rules

If required, enter the appropriate SIP dial rule. SIP dial
                                             					 rules provide local dial plans for Cisco Unified IP Phones 7940, and 7975 that
                                             					 run SIP, so users do not have to press a key or wait for a timer before the
                                             					 call gets processed.

Leave the SIP Dial Rules field set to <None> if you do
                                             					 not want dial rules applied to the IP phone that is running SIP. This means the
                                             					 user must use the Dial softkey or wait for the timer to expire before the call
                                             					 gets processed.

CSS
                                             					 Reroute

Enter a
                                             					 calling search space to use for rerouting.

The system
                                             					 uses the rerouting calling search space of the referrer to find the route to
                                             					 the refer-to target. When the Refer fails due to the rerouting calling search
                                             					 space, the Refer Primitive rejects the request with the "405
                                                						Method Not Allowed" message.

The
                                             					 redirection (3xx) primitive and transfer feature also uses the rerouting
                                             					 calling search space to find the redirect-to or transfer-to target.

Common
                                             					 Phone Configuration

Enter the
                                             					 common phone configuration to which you want this phone assigned. The common
                                             					 phone configuration includes the attributes (services or features) that are
                                             					 associated with a particular user.

Calling
                                             					 Search Space Refer

Enter an
                                             					 out-of-dialog refer calling search space.

Unified Communications Manager uses the out-of-dialog (OOD) Refer Authorization calling search space (CSS) to authorize the SIP out-of-dialog Refer. The
                                             administrator can restrict the use of out-of-dialog Refer by configuring the OOD CSS of the Referrer. Refer Primitive rejects
                                             the OOD Refer request with a "403 Forbidden" message.

Certificate Operation

Enter the
                                             					 Certification Operation that you want to perform from the following options:

- No Pending
                                                   					 Operation —No pending Certification Operation lists exist for this
                                                				  device. Choosing this option disables the remaining CAPF fields.

- Install/Upgrade —Install or upgrade a Certification
                                                				  Operation.

- Delete —Delete a
                                                				  Certification Operation

- Troubleshoot —Troubleshoot a Certification Operation.

Certificate Operation Completion Time

This
                                             					 field, which supports the Install/Upgrade, Delete, and Troubleshoot Certificate
                                             					 Operation options, specifies the date and time in which you must complete the
                                             					 operation.

Secure
                                             					 Shell User

Enter a
                                             					 user ID for the secure shell user. If the phone that you are configuring does
                                             					 not support secure shell access, this field does not display. Cisco Technical
                                             					 Assistance Center (TAC) uses secure shell for troubleshooting. Contact TAC for
                                             					 further assistance.

Secure
                                             					 Shell Password

Enter the
                                             					 password for a secure shell user. If the phone that you are configuring does
                                             					 not support secure shell access, this field does not display. Contact TAC for
                                             					 further assistance.

Device
                                             					 Pool

Enter the
                                             					 appropriate device pool.

The device
                                             					 pool specifies a collection of properties for this device that includes
                                             					 Communications Manager Group, Date/Time Group, Region, and Calling Search Space
                                             					 for auto registration of devices.

Built-in
                                             					 Bridge

Enter On,
                                             					 Off, or Default to enable or disable the built-in conference bridge for the
                                             					 barge feature.

Calling
                                             					 Search Space

Enter the
                                             					 appropriate calling search space. A calling search space comprises a collection
                                             					 of partitions that are searched for numbers that are called from this phone
                                             					 number. The value that you choose applies to all devices that are using this
                                             					 phone number.

Location

Choose the
                                             					 appropriate location for this phone. A location setting of Hub_None means that
                                             					 the locations feature does not keep track of the bandwidth that this phone
                                             					 consumes.

Module 1

Enter the
                                             					 appropriate expansion module or none.

Module 1
                                             					 Load Name

Enter the
                                             					 custom software for the appropriate expansion module, if applicable.

The value
                                             					 that you enter overrides the default value for the current model. Ensure the
                                             					 firmware load matches the module load.

Module 2

Enter the
                                             					 appropriate expansion module or none.

Module 2
                                             					 Load Name

Enter the
                                             					 custom software for the second expansion module, if applicable.

The value
                                             					 that you enter overrides the default value for the current model. Ensure the
                                             					 firmware load matches the module load.

Phone
                                             					 Template

Enter the
                                             					 phone template name that you created for this type of bulk transaction.

Authentication Server

Enter the
                                             					 URL that the phone uses to validate requests that are made to the phones web
                                             					 server. If you do not provide an authentication URL, the advanced features on
                                             					 the CiscoUnifiedIPPhones that require authentication will not function.
                                             					 Leave this field blank to accept the default setting.

By default, this URL
                                             					 accesses a CiscoUnifiedIPPhone Self Care Portal window that was configured
                                             					 during installation.

Proxy
                                             					 Server

Enter the
                                             					 host and port (for example, proxy.cisco.com:80) that are used to proxy HTTP
                                             					 requests for access to non-local host addresses from the phones HTTP client.

If the
                                             					 phone receives a URL such as www.cisco.com in a service and the phone is not
                                             					 configured in the cisco.com domain, the phone uses the proxy server to access
                                             					 the URL. If the phone is configured in the cisco.com domain, the phone accesses
                                             					 the URL without using the proxy because it is in the same domain as the URL.

Idle

Enter the
                                             					 URL of the XML service that will appear as the idle display on the
                                             					 CiscoUnifiedIPPhone LCD screen when the phone has not been used for the time
                                             					 that is specified in the Idle Time field.

For
                                             					 example, you can display a logo on the LCD screen when the phone has not been
                                             					 used for 5 minutes.

Idle Timer

Enter the
                                             					 seconds that you want to elapse before the phone displays the URL that is
                                             					 specified in the Idle field.

Secure
                                             					 Authentication URL

Enter the
                                             					 secure URL that the phone uses to validate requests that are made to the phone
                                             					 web server.

If you
                                                         						do not provide a Secure Authentication URL, the device uses the nonsecure URL.
                                                         						If you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities.

By default, this URL
                                             					 accesses a CiscoUnifiedIPPhone Self Care Portal window that was configured
                                             					 during installation.

Leave this
                                             					 field blank to accept the default setting.

Maximum
                                             					 length: 255

Secure
                                             					 Directory URL

Enter the
                                             					 secure URL for the server from which the phone obtains directory information.
                                             					 This parameter specifies the URL that secured Cisco Unified IP Phones use when
                                             					 you press the Directory button.

If you
                                                         						do not provide a Secure Directory URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities.

Leave this
                                             					 field blank to accept the default setting.

Maximum
                                             					 length: 255

Secure
                                             					 Idle URL

Enter the
                                             					 secure URL for the information that displays on the Cisco Unified IP Phone
                                             					 display when the phone is idle, as specified in Idle Timer field. For example,
                                             					 you can display a logo on the LCD when the phone has not been used for 5
                                             					 minutes.

If you
                                                         						do not provide a Secure Idle URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities.

To accept
                                             					 the default setting, leave this field blank.

Maximum
                                             					 length: 255

Secure
                                             					 Information URL

Enter the
                                             					 secure URL for the server location where the Cisco Unified IP Phone can find
                                             					 help text information. This information displays when the user presses the
                                             					 information (i) button or the question mark ( ? ) button.

If you
                                                         						do not provide a Secure Information URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities.

To accept
                                             					 the default setting, leave this field blank.

Maximum
                                             					 length: 255

Secure
                                             					 Messages URL

Enter the
                                             					 secure URL for the messages server. The Cisco Unified IP Phone contacts this
                                             					 URL when the user presses the Messages button.

If you
                                                         						do not provide a Secure Messages URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities.

To accept
                                             					 the default setting, leave this field blank.

Maximum
                                             					 length: 255

Secure
                                             					 Services URL

Enter the
                                             					 secure URL for Cisco Unified IP Phone services. The is the location that the
                                             					 secure Cisco Unified IP Phone contacts when the user presses the Services
                                             					 button.

If you
                                                         						do not provide a Secure Services URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities.

To accept
                                             					 the default setting, leave this field blank.

Maximum
                                             					 length: 255

Hotline
                                             					 Device

Enter ‘T’
                                             					 or ‘F’. Hotline devices can only connect to other Hotline devices. This feature
                                             					 is an extension of PLAR, which configures a phone to automatically dial one
                                             					 directory number when it goes off-hook. Hotline provides additional
                                             					 restrictions that you can apply to devices that use PLAR.

To
                                             					 implement Hotline, you must also create a softkey template without
                                             					 supplementary service softkeys, and apply it to the Hotline device.

Owner User
                                             					 ID

Enter a
                                             					 user ID for the primary phone user.

Common
                                             					 Phone Profile

Enter the
                                             					 common phone profile to which you want this phone assigned. The common phone
                                             					 profile includes the attributes (services or features) that are associated with
                                             					 a particular user.

Device
                                             					 Mobility Mode

Turn the
                                             					 device mobility feature on or off for this device or enter Default to use the
                                             					 default device mobility mode.

DND Option

Choose a
                                             					 DND option from the following options:

- None

- Ringer Off

DND
                                             					 Incoming Call Alert

Enter one
                                             					 of the following options:

- None

- Disable

- Flash Only

- Beep Only

Privacy

Enter one
                                             					 of the following options:

- On

- Off

- Default

Use
                                             					 Trusted Relay Point

Enter one
                                             					 of the following options:

- Default

- Off

- On

Information

Enter the
                                             					 help text URL for the information button for CiscoUnifiedIPPhones.

Directory

Enter the
                                             					 URL of the directory server for CiscoUnifiedIPPhones.

Messages

Enter the
                                             					 voice-messaging access pilot number for CiscoUnified IPPhones.

Services

Enter the
                                             					 URL for the services menu for CiscoUnifiedIPPhones.

Calling
                                             					 Party Transformation CSS

This
                                             					 setting allows you to localize the calling party number on the device. Make
                                             					 sure that the Calling Party Transformation CSS that you enter contains the
                                             					 calling party transformation pattern that you want to assign to this device

Single
                                             					 Button Barge

Enter one
                                             					 of the following options:

- Off —This setting
                                                				  disables the Single Button Barge/cBarge feature; however, the regular Barge or
                                                				  cBarge features will still work.

- Barge —This setting
                                                				  enables the Singe Button Barge feature.

- cBarge —This
                                                				  setting enables the Single Button cBarge feature.

- Default —This
                                                				  setting uses the Single Button Barge/cBarge setting that is in the service
                                                				  parameter.

Join
                                             					 Across Lines

Enter one
                                             					 of the following options:

- Off —This setting
                                                				  disables the Join Across Lines feature.

- On —This setting
                                                				  enables the Join Across Lines feature.

- Default —Uses the
                                                				  Join Across Lines setting that is in the service parameter.

BLF
                                             					 Audible Alert Setting (Phone Idle)

Enter the
                                             					 BLF Audible Alert setting that you want to use from the following values:

- On

- Off

- Default

For this
                                             					 required field, this parameter provides an audible alert in addition to a
                                             					 visual alert on a phone that is currently idle when a call comes in to one of
                                             					 the lines that is monitored by way of a busy line field (BLF) button.

BLF
                                             					 Audible Alert Setting (Phone Busy)

For this
                                             					 required field, enter the BLF Audible Alert setting that you want to use from
                                             					 the following values:

- On

- Off

- Default

Always Use
                                             					 Prime Line

Enter the
                                             					 Always Use Prime Line setting that you want to use from the following values:

- On

- Off

- Default

Always Use
                                             					 Prime Line for Voice Message

Enter the
                                             					 Always Use Prime Line for Voice Message setting that you want to use from the
                                             					 following values:

- On

- Off

- Default

Services
                                             					 Provisioning

For this
                                             					 required field, enter one of the following values:

- Internal

- External URLs

- Both

- Default: Internal

Phone
                                             					 Personalization

Enter one
                                             					 of the following values:

- Disabled —None of
                                                				  the personalization settings on the phone get activated.

- Enabled —This
                                                				  setting accepts a personalized background image file, which is used for the
                                                				  phone screen; it accepts a preview image file for temporary display; and it
                                                				  accepts a personalized tone file, so the default ring tone can be personalized.

- Default —Use the
                                                				  phone personalization setting that is in the Common Phone Profile.

Mobility
                                             					 Identity Name

Enter a
                                             					 name that identifies the remote destination.

Mobility
                                             					 Identity Destination Number

Enter the
                                             					 telephone number for the destination. Include the area code and any additional
                                             					 digits that are required to obtain an outside line. Maximum field length equals
                                             					 24 characters; individual characters can take the values 0-9, * , and # . Cisco recommends that you configure the caller ID of
                                             					 the remote destination.

Add the
                                             					 necessary translation pattern or route patterns to route the destination
                                             					 number.

Mobility
                                             					 Identity Answer Too Soon Timer

Enter the
                                             					 minimum time in milliseconds that must pass before the mobile phone can be
                                             					 answered.

Range: 0 -
                                             					 10,000 milliseconds

Default:
                                             					 1,500 milliseconds

Mobility
                                             					 Identity Answer Too Late Timer

Enter the
                                             					 maximum time in milliseconds that can pass before the mobile phone must be
                                             					 answered.

Range:
                                             					 10,000 - 300,000 milliseconds

Default:
                                             					 19,000 milliseconds

Mobility
                                             					 Identity Delay Before Ringing Cell

Enter the
                                             					 time that elapses before the mobile phone rings when a call is transferred from
                                             					 the desktop phone.

Range: 0 -
                                             					 30,000 milliseconds

Default:
                                             					 4,000 milliseconds

Mobility
                                             					 Identity Time of Day Access

Enter a
                                             					 time-of-day access record to associate with this remote destination.

Mobility
                                             					 Identity Time Zone

Enter a
                                             					 time zone to use for this remote destination.

The time
                                                         						zone that you use for this remote destination is used by the time-of-day access
                                                         						feature to allow or block calls to this remote destination.

Mobility
                                             					 Identity Enable Mobile Connect

Enter ‘T’
                                             					 or ‘F’ in this field to allow or disallow an incoming call to ring your desktop
                                             					 phone and remote destination at the same time.

Mobile
                                             					 Smart Client Profile

Mobile
                                             					 Smart Client Profile is the Smart Client for smart client devices and dual-mode
                                             					 phones.

Enter "Standard
                                                						Cisco Unified Mobile Communicator Profile" in this field to enable Cisco
                                             					 Unified Mobile Communicator. Leave it blank to disable it.

Geo
                                             					 Location

Enter the
                                             					 geo location that you want to associate with the phone.

Enter "unspecified" if you do not want to associate the phone to any
                                             					 geo location.

Feature
                                             					 Control Policy

Enter the
                                             					 Feature Control Policy for this group of phones.

A feature
                                             					 control policy specifies the appearance of features and the associated softkeys
                                             					 that are displayed on the phone.

Line Fields
                                                						(Optional)

Directory
                                             					 Number

Enter the
                                             					 directory number, up to 24 digits and special characters, for the phone.

Route
                                             					 Partition

Enter a
                                             					 route partition to which the directory number belongs.

The
                                                         						directory number can appear in more than one partition.

Display

Enter the
                                             					 text that you want to display on the called party phone display, such as the
                                             					 user name (John Smith) or phone location (Conference Room 1).

If this
                                                         						filed is left blank, the system uses the value that is entered in the Directory
                                                         						Number field.

The
                                                         						default language specifies English.

Line Text
                                             					 Label

Enter text
                                             					 that identifies this directory number for a line/phone combination.

The
                                                         						default language specifies English

Voice Mail
                                             					 Profile

Enter this
                                             					 parameter to make the pilot number the same as the directory number for this
                                             					 line. This action proves useful if you do not have a voice-messaging server
                                             					 that is configured for this phone.

Line
                                             					 Calling Search Space

Enter
                                             					 partitions that are searched for numbers that are called from this directory
                                             					 number.

Changes
                                                         						cause an update of Pickup Group Names that are listed in the Call Pickup Group field. The setting applies to all
                                                         						devices that use this directory number.

AAR Group

Enter the
                                             					 automated alternate routing (AAR) group for this device. The AAR group provides
                                             					 the prefix digits that are used to route calls that are otherwise blocked due
                                             					 to insufficient bandwidth.

Set AAR
                                             					 Group to <None> to prevent rerouting blocked calls.

Forward
                                             					 All CSS

Enter the
                                             					 calling search space to use when a call is forwarded to the specified
                                             					 destination.

This
                                                         						setting applies to all devices that are using this directory number.

Secondary
                                             					 CSS for Forward All

Enter the
                                             					 secondary calling search space (CSS).

Forward
                                             					 All Destination

Enter the
                                             					 directory number or directory URI to which all calls get forwarded.

This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number.

Forward
                                             					 Busy External CSS

Enter the
                                             					 calling search space to use when a call from an external number gets forwarded
                                             					 to the specified destination.

This
                                                         						setting applies to all devices that are using this directory number.

Forward
                                             					 Busy Internal CSS

Enter the
                                             					 calling search space to use when a call from an internal number gets forwarded
                                             					 to the specified destination.

This
                                                         						setting applies to all devices that are using this directory number.

Forward
                                             					 Busy Destination External

Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 external number gets forwarded when the line is in use.

This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number.

Forward
                                             					 Busy Destination Internal

Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 internal number gets forwarded when the line is in use.

This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number.

Forward No
                                             					 Answer External CSS

Enter the
                                             					 calling search space to use when a call from an external number gets forwarded
                                             					 to the specified destination. The setting displays only if it is configured in
                                             					 the system.

This
                                                         						setting applies to all devices that are using this directory number.

Forward No
                                             					 Answer Internal CSS

Enter the
                                             					 calling search space to use when a call from an internal number gets forwarded
                                             					 to the specified destination. The setting displays only if it is configured in
                                             					 the system.

This
                                                         						setting applies to all devices that are using this directory number.

Forward No
                                             					 Answer External Destination

Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 external number gets forwarded when the phone is not answered.

This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number.

Forward No
                                             					 Answer Internal Destination

Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 internal number gets forwarded when the phone is not answered.

This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number.

Forward No
                                             					 Coverage External CSS

Enter the
                                             					 calling search space to use when a call from an external number gets forwarded
                                             					 to the specified destination. The setting displays only if it is configured in
                                             					 the system.

This
                                                         						setting applies to all devices that are using this directory number.

Forward No
                                             					 Coverage Internal CSS

Enter the
                                             					 calling search space to use when a call from an internal number gets forwarded
                                             					 to the specified destination. The setting displays only if it is configured in
                                             					 the system.

This
                                                         						setting applies to all devices that are using this directory number.

Forward No
                                             					 Coverage External Destination

Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 external number gets forwarded when the phone does not have coverage.

This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number.

Forward No
                                             					 Coverage Internal Destination

Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 internal number gets forwarded when the phone does not have coverage.

This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number.

Calling
                                             					 Search Space Forward on Failure External/Internal

(CTI ports
                                             					 only) Enter the calling search space to use when a call from an internal or
                                             					 external call gets forwarded to the specified destination. The setting appears
                                             					 only if it is configured in the system.

This
                                                         						setting applies to all devices that are using this directory number.

Forward on
                                             					 Failure Destination External/Internal

(CTI ports
                                             					 only) Enter the directory number or directory URI to which a call coming from
                                             					 an internal or an external number should get forwarded when a phone or CTI
                                             					 application fails.

Forward on
                                             					 CTI Failure Destination

This
                                             					 setting specifies the directory number to which an internal nonconnected call
                                             					 gets forwarded when an application that controls that directory number fails.
                                             					 Use any dialable phone number, including an outside destination.

When you
                                             					 enter a destination value for internal calls, the system automatically copies
                                             					 this value to the Destination field for external calls. If you want external
                                             					 calls to forward to a different destination, you must enter a different value
                                             					 in the Destination field for external calls.

Forward on
                                             					 CTI Failure Calling Search Space

This
                                             					 setting applies to all devices that are using this directory number.

When you
                                             					 choose a Calling Search Space for internal calls, the system automatically
                                             					 copies this setting to the Calling Search Space setting for external calls. If
                                             					 you want external calls to forward to a different calling search space, choose
                                             					 a different setting in the Calling Search Space for external calls.

Call
                                             					 Pickup Group

Choose a
                                             					 Pickup Group Name to specify the call pickup group, which can answer incoming
                                             					 calls to this directory number by dialing the appropriate pickup group number.

External
                                             					 Phone Number Mask

Enter the
                                             					 phone number (or mask) that is sent for Caller ID information when a call is
                                             					 placed from this line.

You can
                                             					 enter a maximum of 24 numbers and "X" characters. The Xs represent the directory number and must appear at the end of
                                             					 the pattern. For example, if you specify a mask of 972813XXXX, an external call
                                             					 from extension 1234 displays a caller ID number of 9728131234.

Forward No
                                             					 Answer Ring Duration (CFNA)

Enter the
                                             					 number of seconds to allow the call to ring before forwarding the call to the
                                             					 Forward No Answer Destination.

Target
                                             					 Destination (MLPP)

Enter the
                                             					 number to which MLPP precedence calls should be directed if this directory
                                             					 number receives a precedence call and neither this number nor its call forward
                                             					 destination answers the precedence call.

Values can
                                             					 include numeric characters, pound ( # ),and asterisk ( * ).

Calling
                                             					 Search Space (MLPP)

Enter the
                                             					 calling search space to associate with the alternate party target (destination)
                                             					 number.

No Answer
                                             					 Ring Duration (MLPP)

Enter the
                                             					 time, seconds (between 4 and 30), after which an MLPP precedence call will be
                                             					 directed to this directory number’s alternate party if this directory number
                                             					 and its call forwarding destination have not answered the precedence call.

Leave this setting blank to use the value that is set in the Unified Communications Manager enterprise parameter, Precedence Alternate Party Timeout.

Maximum
                                             					 Number of Calls

You can
                                             					 configure up to 200 calls for a line on a device in a cluster, with the
                                             					 limiting factor being the device. As you configure the number of calls for one
                                             					 line, the calls that are available for another line decrease.

The
                                             					 default specifies 4. If the phone does not allow multiple calls for each line,
                                             					 the default specifies 2.

For CTI
                                             					 route points, you can configure up to 10,000 calls for each port. The default
                                             					 specifies 5000 calls. Use this field in conjunction with the Busy Trigger field.

Busy
                                             					 Trigger

This
                                             					 setting, which works in conjunction with Maximum Number of Calls and Call
                                             					 Forward Busy, determines the maximum number of calls to be presented at the
                                             					 line. If maximum number of calls is set for 50 and the busy trigger is set to
                                             					 40, incoming call 41 gets rejected with a busy cause (and will get forwarded if
                                             					 Call Forward Busy is set). If this line is shared, be aware that all the lines
                                             					 must be busy before incoming calls get rejected.

Use this
                                             					 field in conjunction with Maximum Number of Calls for CTI route points. The
                                             					 default specifies 4500 calls.

Alerting
                                             					 Name

This name
                                             					 represents the name that displays during an alert to a shared directory number.
                                             					 For non-shared directory numbers, during alerts, the system uses the name that
                                             					 is entered in the Display field.

Alerting
                                             					 Name ASCII

This field
                                             					 provides the same information as the Alerting Name field, but you must limit
                                             					 input to ASCII characters. Devices that do not support Unicode
                                             					 (internationalized) characters display the content of the Alerting Name ASCII field.

Auto
                                             					 Answer

Enter one
                                             					 of the following options to activate the Auto Answer feature for this directory
                                             					 number:

- Auto Answer Off
                                                   					 <Default>

- Auto Answer with
                                                   					 Headset

- Auto Answer with
                                                   					 Speakerphone

Make
                                                         						sure that the headset or speakerphone is not disabled when you choose Auto
                                                         						Answer with headset or Auto Answer with speakerphone.

Do not
                                             					 configure Auto Answer for devices that have shared lines.

Route
                                             					 Filter

Enter a
                                             					 name in the Route Filter Name field. The name can contain up to 50 alphanumeric
                                             					 characters and can contain any combination of spaces, periods (.), hyphens (-),
                                             					 and underscore characters ( _ ). Ensure each route filter name is unique to the
                                             					 route plan.

Use
                                                         						concise and descriptive names for your route filters. The
                                                         						CompanynameLocationCalltype format usually provides enough detail and is short
                                                         						enough to enable you to quickly and easily identify a route filter. For
                                                         						example, CiscoDallasMetro identifies a route filter for toll free, inter-local
                                                         						access and transport area (LATA) calls from the Cisco office in Dallas.

Dial Plan

Enter a
                                             					 dial plan; for example, North American Numbering Plan.

Line User
                                             					 Hold MOH Audio Source

Enter the
                                             					 audio source to use for music on hold (MOH) when a user initiates a hold
                                             					 action.

Line
                                             					 Network Hold MOH Audio Source

Enter the
                                             					 audio source to use for music on hold (MOH) when the network initiates a hold
                                             					 action.

Ring
                                             					 Setting (Phone Active)

Enter the
                                             					 ring setting that is used when this phone has another active call on a
                                             					 different line. Choose one of the following options:

- Use system default

- Disable

- Flash only

- Ring once

- Ring

- Beep only

Ring
                                             					 Setting (Phone Idle)

Enter the
                                             					 ring setting for the line appearance when an incoming call is received and no
                                             					 other active calls exist on that device. Choose one of the following options:

- Use system default

- Disable

- Flash only

- Ring once

- Ring

E.164

Enter the
                                             					 E.164 address that is registered with the gatekeeper.

Ensure
                                                         						the H.323 client is configured as a gatekeeper-controlled device.

You must
                                                         						enter a value in this field for a gatekeeper-controlled H.323 client. You can
                                                         						enter only numbers (0-9) and special characters # and * in this field.

AAR
                                             					 Destination Mask

Enter the
                                             					 setting to use instead of the external phone number mask to determine the AAR
                                             					 Destination to be dialed.

Forward
                                             					 Unregistered Internal Destination

Enter the
                                             					 directory number to which an unregistered internal call is forwarded when the
                                             					 line is in use.

This
                                             					 setting applies to any internal, dialable phone number and to all devices that
                                             					 are using this directory number.

Forward
                                             					 Unregistered Internal CSS

Enter the
                                             					 calling search space to use when unregistered internal calls are forwarded to
                                             					 the specified destination.

This
                                             					 setting applies to all devices that are using this directory number.

Forward
                                             					 Unregistered External Destination

Enter the
                                             					 directory number to which an external call is forwarded when the line is in
                                             					 use.

This
                                             					 setting applies to any dialable external phone number, including an outside
                                             					 destination unless restricted, and to all devices that are using this directory
                                             					 number.

Forward
                                             					 Unregistered External CSS

Enter the
                                             					 calling search space to use when external calls are forwarded to the specified
                                             					 destination.

This
                                             					 setting applies to all devices that are using this directory number.

Audible
                                             					 Message Waiting Indicator Policy

Use this
                                             					 field to configure an audible message waiting indicator policy. Enter one of
                                             					 the following options:

- Off

- On —When you enter
                                                				  this option, you will receive a stutter dial tone when you take the handset off
                                                				  hook.

- Default —When you
                                                				  enter this option, the phone uses the default that was set at the system level.

Call
                                             					 Pickup Group Audio Alert Setting (Phone Idle)

This field
                                             					 determines the type of notification an incoming call sends to members of a call
                                             					 pickup group. If the called phone does not answer, the phones in the call
                                             					 pickup group that are idle will either hear a short ring (ring once) or hear
                                             					 nothing (disabled).

- Use System
                                                   					 Default —The value of this field gets determined by the setting of the
                                                				  Cisco CallManager service parameter Call Pickup Group Audio Alert Setting of
                                                				  Idle Station.

- Disable —No alert
                                                				  is sent to members of the call pickup group.

- Ring Once —A short
                                                				  ring is sent to members of the call pickup group.

Call
                                             					 Pickup Group Audio Alert Setting (Phone Active)

This field
                                             					 determines the type of notification an incoming call sends to members of a call
                                             					 pickup group. If the called phone does not answer, the phones in the call
                                             					 pickup group that are busy will either hear a beep or hear nothing (disabled).

- Use System
                                                   					 Default —The value of this field gets determined by the setting of the
                                                				  Cisco CallManager service parameter Call Pickup Group Audio Alert Setting of
                                                				  Busy Station.

- Disable —No alert
                                                				  is sent to member of the call pickup group.

- Beep Only —A beep
                                                				  is sent to members of the call pickup group.

Call
                                             					 Recording Option

This field
                                             					 determines the recording option on the line appearance of an agent. By default,
                                             					 the recording option specifies Call Recording Disabled.

Enter one
                                             					 of the following options:

- Call Recording
                                                   					 Disabled —The calls that the agent makes on this line appearance are
                                                				  not recorded.

- Automatic Call Recording
                                                   					 Enabled —The calls that the agent makes on this line appearance are
                                                				  automatically recorded.

- Application Invoked Call
                                                   					 Recording Enabled —The calls that the agent makes on this line
                                                				  appearance are recorded if an application invokes calling recording.

When the
                                             					 recording option is set to either Automatic Call Recording Enabled or
                                             					 Application Invoked Call Recording Enabled, the line appearance can be
                                             					 associated with a recording profile.

When
                                             					 automatic recording is enabled, the application's recording requests get
                                             					 rejected.

Recording
                                             					 Profile

This field
                                             					 determines the recording profile on the line appearance of an agent.

Monitoring
                                             					 Calling Search Space

The
                                             					 monitoring calling search space of the supervisor line appearance must include
                                             					 the agent line or device partition to allow monitoring the agent.

Enter the
                                             					 monitoring calling search space on the supervisor line appearance window.

The
                                             					 default value specifies None.

Forward
                                             					 All CSS Activation Policy

Enter one
                                             					 of the following options:

- Use System Default

- With Configured
                                                   					 CSS

Party
                                             					 Entrance Tone

Enter one
                                             					 of the following Party Entrance Tone options:

- Default —Use the
                                                				  value that you configured in the Party Entrance Tone service parameter.

- On —A tone plays on the phone when a basic call changes to a multi-party call; that is, a barge call, cBarge call, ad hoc conference,
                                                meet-me conference, or a joined call. In addition, a different tone plays when a party leaves the multi-party call. If the
                                                controlling device, that is, the originator of the multi-party call has a built-in bridge, the tone gets played to all parties
                                                if you choose On for the controlling device. When the controlling device, for example, the conference controller, is no longer
                                                present on the call or if the controlling device cannot play the tone, Unified Communications Manager does not play the tone
                                                even if you choose On.

- Off —A tone does
                                                				  not play on the phone when a basic call changes to a multi-party call.

Park
                                             					 Monitor Forward No Retrieve Ext Destination

When the
                                             					 parkee is an external party, then the call will be forwarded to the specified
                                             					 destination in the parker’s Park Monitoring Forward No Retrieve Destination
                                             					 External parameter. If the Forward No Retrieve Destination External field value
                                             					 is empty, the parkee will be redirected to the parker’s line.

Park
                                             					 Monitor Forward No Retrieve Int Destination

When the
                                             					 parkee is an internal party, then the call will be forwarded to the specified
                                             					 destination in the parker’s Park Monitoring Forward No Retrieve Destination
                                             					 Internal parameter. If the Forward No Retrieve Destination Internal is empty,
                                             					 the parkee will be redirected to the parker’s line.

Park
                                             					 Monitor Forward No Retrieve Int Voice Mail

This
                                             					 setting uses the settings in the Voice Mail Profile Configuration window.

With this setting, Unified Communications Manager ignores the settings in the Destination box and Calling Search Space.

Park
                                             					 Monitor Forward No Retrieve Ext Voice Mail

This
                                             					 setting uses the settings in the Voice Mail Profile Configuration window.

With this setting, Unified Communications Manager ignores the settings in the Destination box and Calling Search Space.

Park
                                             					 Monitor Forward No Retrieve Ext CSS

Choose the
                                             					 calling search space to apply to the directory number.

Park
                                             					 Monitor Forward No Retrieve Int CSS

Choose the
                                             					 calling search space to apply to the directory number.

Park
                                             					 Monitor Reversion Timer

This parameter determines the number of seconds that Unified Communications Manager waits before prompting the user to retrieve a call that the user parked. This timer starts when the user presses the Park
                                             softkey on the phone, and a reminder is issued when the timer expires.

Default:
                                             					 60 seconds

If you
                                             					 configure a non-zero value, this value overrides the value of this parameter
                                             					 set in the Service Parameters window. However, if you configure a value of 0
                                             					 here, then the value in the Service Parameters window will be used.

Log Missed
                                             					 Calls

This field allows you to turn this feature on or off. Enter ‘T’ to enable Unified Communications Manager to log missed calls in the call history for that directory number on the phone. Enter ‘F’ to disable this feature.

URI (1-5)
                                             					 on Directory Number

Enter a
                                             					 directory URI to associate with the directory number for this phone. Follow the
                                             					 username@host format. Enter a username of up to 47 alphanumeric characters. For
                                             					 the host address, enter an IPv4 address or fully qualified domain name. You can
                                             					 associate up to five directory URIs to a single directory number.

URI (1-5)
                                             					 Route Partition on Directory Number

Enter the
                                             					 partition on which the directory URI belongs. If you do not want to restrict
                                             					 access to the directory URI, leave the field blank.

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

Enterprise
                                             					 Add to Local Route Partition

Enter a
                                             					 't' to add this enterprise alternate number to a local route partition. Enter
                                             					 'f' to leave the E.164 number off of local routing.

Enterprise
                                             					 Advertise via globally

Enter a
                                             					 't' to enable ILS to advertise this alternate number to rest of the ILS
                                             					 network. Enter an 'f' if you don't want ILS to advertise this number.

Enterprise
                                             					 Is Urgent

Enter a
                                             					 't' to classify routing for this alternate number as urgent.

By default, if the dial plan contains overlapping route patterns Unified Communications Manager does not route the call until
                                             the interdigit timer expires (even if a possible route exists for the dialed digits). This setting guards against learned
                                             numbers that overlap with statically configured directory numbers and number patterns by allowing Unified Communications Manager
                                             to choose the best match of all available routes for the dial string.

When you mark the number as urgent priority, Unified Communications Manager routes the call as soon as it finds a match between
                                             the dialed digits and an available route, without waiting for the interdigit timer to expire (for example, the T302 Timer
                                             service parameter).

Enterprise
                                             					 Number Mask

Enter the number mask to apply to the directory number. Unified Communications Manager applies the mask to create an enterprise
                                             alternate number that is an alias of this directory number.

Enterprise
                                             					 Route Partition

Enter the
                                             					 local route partition to which you want to assign this enterprise alternate
                                             					 number.

+E.164 Add
                                             					 to Local Route Partition

Enter a
                                             					 't' to add this E.164 alternate number to a local route partition. Enter 'f' to
                                             					 leave the E.164 number off of local routing.

+E.164
                                             					 Advertise via globally

Enter a
                                             					 't' to enable ILS to advertise this alternate number to rest of the ILS
                                             					 network. Enter an 'f' if you don't want ILS to advertise this number.

+E.164 Is
                                             					 Urgent

Enter a
                                             					 't' to classify routing for this alternate number as urgent.

By default, if the dial plan contains overlapping route patterns Unified Communications Manager does not route the call until
                                             the interdigit timer expires (even if a possible route exists for the dialed digits). This setting guards against learned
                                             numbers that overlap with statically configured directory numbers and number patterns by allowing Unified Communications Manager
                                             to choose the best match of all available routes for the dial string.

When you mark the number as urgent priority, Unified Communications Manager routes the call as soon as it finds a match between
                                             the dialed digits and an available route, without waiting for the interdigit timer to expire (for example, the T302 Timer
                                             service parameter).

+E.164
                                             					 Number Mask

Enter the number mask to apply to the directory number. Unified Communications Manager applies the mask to create an +E.164
                                             alternate number that is an alias of this directory number.

+E.164
                                             					 Route Partition

Enter the
                                             					 local route partition to which you want to assign this +E.164 alternate number.

Intercom Fields
                                                						(Optional)

Intercom
                                             					 Directory Number

Enter a
                                             					 dialable phone number. Values can include numeric characters and route pattern
                                             					 wildcards and special characters except for (.) and ( @ ).

The
                                             					 directory number that you enter can appear in more than one partition.

At the
                                             					 beginning of the directory number, enter \+ if you want to use the international escape
                                             					 character + . For this field, \+ does not represent a wildcard; instead, entering \+ represents a dialed digit.

Intercom
                                             					 Route Partition

Enter the
                                             					 partition to which the directory number belongs. Make sure that the directory
                                             					 number that you enter in the Intercom Directory Number field is unique within
                                             					 the partition that you choose.

The
                                                         						directory number can appear in more than one partition.

Description

Enter a
                                             					 description of the directory number and route partition.

Alerting
                                             					 Name

Enter a
                                             					 name that you want to display on the phone of the caller.

This
                                             					 setting, which supports the Identification Services for the QSIG protocol,
                                             					 applies to shared and nonshared directory numbers.

Alerting
                                             					 Name ASCII

This field
                                             					 provides the same information as the Alerting Name field, but you must limit
                                             					 input to ASCII characters. Devices that do not support Unicode
                                             					 (internationalized) characters display the content of the Alerting Name ASCII
                                             					 field.

Intercom Directory Number
                                                						Settings

Calling
                                             					 Search Space

Enter the
                                             					 appropriate calling search space. A calling search space comprises a collection
                                             					 of partitions that are searched for numbers that are called from this directory
                                             					 number. The value that you choose applies to all devices that are using this
                                             					 directory number.

Intercom
                                             					 Presence Group

Enter a
                                             					 Presence Group for this directory number. The selected group specifies the
                                             					 devices, end users, and application users that can monitor this directory
                                             					 number.

Intercom
                                             					 Display

Leave this
                                             					 field blank to have the system display the extension.

Use a
                                             					 maximum of 30 alphanumeric characters. Typically, use the user name or the
                                             					 directory number (if using the directory number, the person receiving the call
                                             					 may not see the proper identity of the caller).

Intercom
                                             					 ASCII Display

This field
                                             					 provides the same information as the Display (Internal Caller ID) field, but
                                             					 you must limit input to ASCII characters. Devices that do not support Unicode
                                             					 (internationalized) characters display the content of the ASCII Display (Internal Caller ID) field.

Intercom
                                             					 Line Text Label

Use this
                                             					 field only if you do not want the intercom directory number to show on the line
                                             					 appearance. Enter text that identifies this directory number for a line/phone
                                             					 combination.

Intercom
                                             					 Speed Dial

Enter the
                                             					 number that you want the system to dial when the user presses the speed-dial
                                             					 button. You can enter digits 0 through 9, * , # , and + , which is the international escape character.

Intercom
                                             					 External Phone Number Mask

Enter the
                                             					 phone number (or mask) that is used to send Caller ID information when a call
                                             					 is placed from this line.

You can
                                             					 enter a maximum of 24 number, the international escape character +, and "X" characters. The Xs represent the directory number and must appear at the end of
                                             					 the pattern. For example, if you specify a mask of 972813XXXX, an external call
                                             					 from extension 1234 displays a caller ID number of 9728131234.

Intercom
                                             					 Caller Name

Enter ‘T’
                                             					 to enable the caller name to display upon call forward. Enter ‘F’ to disable
                                             					 it.

Intercom
                                             					 Caller Number

Enter ‘T’
                                             					 to enable the caller number to display upon call forward. Enter ‘F’ to disable
                                             					 it.

Intercom
                                             					 Call Recording Option

Enter one
                                             					 of the following options:

- Call Recording
                                                   					 Disabled —The calls that the agent makes on this line appearance are
                                                				  not recorded.

- Automatic Call Recording
                                                   					 Enabled —The calls that the agent makes on this line appearance are
                                                				  automatically recorded.

- Application Invoked Call
                                                   					 Recording Enabled —The calls that the agent makes on this line
                                                				  appearance are recorded if an application invokes calling recording.

Intercom
                                             					 Recording Profile

Enter the
                                             					 recording profile on the line appearance of an agent.

Intercom
                                             					 Monitoring Calling Search Space

The
                                             					 monitoring calling search space of the supervisor line appearance must include
                                             					 the agent line or device partition to allow monitoring the agent.

Enter an
                                             					 existing calling search space.

The
                                             					 default value specifies None.

Auto
                                             					 Answer

Enter one
                                             					 of the following options to activate the auto answer feature for this directory
                                             					 number:

- Auto Answer Off
                                                   					 <Default>

- Auto Answer with
                                                   					 Headset

- Auto Answer with
                                                   					 Speakerphone

Do not
                                                         						configure auto answer for devices that have shared lines.

## Update Jabber Device

Cisco Unified Communications Manager Bulk Administration (BAT) gives the administrator an easy and efficient way to rename
                           the auto provisioned Cisco Jabber devices created during LDAP synchronization in batches using the Cisco Unified CM Administration
                           user interface.

### Rename Jabber Devices

#### Before you begin

All Cisco Jabber devices should exist in Unified CM server already.

You must have a data file in text (.txt) format that contains the list of old Cisco Jabber device names that you wish to rename
                                       with the new Cisco Jabber device names.

If the value of the field includes a comma, ensure that this field is enclosed within double quotes.

Step 1

Choose Bulk Administration > Phones > Update Jabber Device .

Step 2

In the Jabber Device Information section, from the File Name drop-down list, choose the text file that you uploaded.

Step 3

In the Job Information area, enter the Job description.

Step 4

Choose a method to update the device names. Do one of the following:

Select Run Immediately to update the device names immediately.

Select Run Later to insert the device names later.

Step 5

To create a job for updating the device names, click Submit .

| Step 1 | Choose Bulk
                                             				  Administration > Phones > Phone
                                             				  Template . The Find and List Phone Templates window displays. |
|---|---|
| Step 2 | Create a CSV data file to insert the phone templates. Perform one of the following options: Create a CSV data file using the BAT spreadsheet. Create a CSV data file using a text editor as follows: Choose Bulk Administration > Phones > Phone File Format > Create File Format . Use a text editor
                                                   						and create the CSV data file for phones that follows the file format that you
                                                   						want to use. Choose Bulk
                                                         							 Administration > Phones > Phone File
                                                         							 Format > Add File Format to associate the text-based file format with the CSV data file. |
| Step 3 | Choose Bulk
                                             				  Administration > Phones > Validate
                                             				  Phones . |
| Step 4 | Choose Bulk Administration > phones > Insert phones to insert phone records into the Unified Communications Manager database. |

| Note | During your work in a browser session, your find/list search preferences are stored in the cookies on the client machine.
                                             If you navigate to other menu items and return to this menu item, or if you close the browser and then reopen a new browser
                                             window, your Unified Communications Manager search preferences are retained until you modify your search. |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > Phones > Phone
                                                				  Template . The Find and List Phone Templates window displays.
                                             				Use the two drop-down list boxes to search for a template. |
|---|---|
| Step 2 | From the first Find Phone Templates where drop-down list box,
                                          			 choose one of the following criteria: Device
                                                				  Name Description Directory Number Directory URI Calling
                                                				  Search Space Device
                                                				  Pool Device
                                                				  Type Call
                                                				  Pickup Group LSC
                                                				  Status Authentication
                                                				  String Device
                                                				  Protocol Security
                                                				  Profile Common
                                                				  Device Configuration |
| Step 3 | From the second Find Phone Template where drop-down list box,
                                          			 choose one of the following criteria: begins
                                                				  with contains is
                                                				  exactly ends
                                                				  with is
                                                				  empty is not
                                                				  empty |
| Step 4 | Specify the appropriate search text, if applicable, and click Find . Tip To find all Phone Templates that are registered in the database,
                                                         				  click Find without entering any search text. A list of discovered templates displays. | Tip | To find all Phone Templates that are registered in the database,
                                                         				  click Find without entering any search text. |
| Tip | To find all Phone Templates that are registered in the database,
                                                         				  click Find without entering any search text. |
| Step 5 | From the list of records, click the device name that matches your
                                          			 search criteria. The window displays the phone template that you choose. |

| Tip | To find all Phone Templates that are registered in the database,
                                                         				  click Find without entering any search text. |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > Phones > Phone
                                                				  Template . |
|---|---|
| Step 2 | Click Add New . The Add a New Phone Template window displays. |
| Step 3 | From the Phone Type drop-down list, choose the phone model for which you are creating the template. Click Next . |
| Step 4 | From the Select the Device Protocol drop-down list, choose the device protocol. Click Next . The Phone Template Configuration window displays with fields and default entries for the chosen device type. |
| Step 5 | In the Template Name field, enter a name for the
                                          			 template. The name can contain up to 50 alphanumeric characters. |
| Step 6 | In the Device Information area, enter the phone settings that this
                                          			 batch has in common. Some phone models and device types do not have all the attributes that the table lists. See, the phone model documentation
                                          for information on all the attributes. |
| Step 7 | After you have entered all the settings for this BAT phone
                                          			 template, click Save . |

| Step 1 | Find the Phone Template to which you want to add the line. |
|---|---|
| Step 2 | In the Phone Template Configuration window,
                                             			 click Line [1] Add a new DN , in the Associated Information area. The Line Template Configuration window displays. |
| Step 3 | Enter or choose the appropriate values for the line settings. |
| Step 4 | Click Save . |
| Step 5 | To add settings for any additional lines, repeat Step 2 through Step 4 . If you choose Back to Find/List from the Related
                                                				Links drop-down list box in the upper, right, corner of
                                             			 the Line Template Configuration window, the Find and List Line Template window displays. To find existing line template, enter the appropriate search
                                                   				  criteria and click Find . To add a new line template, click Add New . |

| Step 1 | Find the Phone Template to which you want add an IP service. |
|---|---|
| Step 2 | From the Phone Template Configuration window,
                                             			 click Add a new SURL in the Associated Information area. A popup window displays. In this window, you can subscribe
                                             			 to CiscoUnifiedIPPhone services that are available. |
| Step 3 | In the Select a Service drop-down list box, choose a
                                             			 service to which you want all phones to be subscribed. The Service Description box displays details about
                                             			 the service that you choose. |
| Step 4 | Click Next . |
| Step 5 | In the Service Name field, modify the name of the
                                             			 service, if required. |
| Step 6 | Associate the selected services or add more services to the
                                             			 template. To associate these phone services to the phone template, click Save . To add more services, repeat Step 3 through Step 6 . To add all the services to the template, click Update . After you are done adding or updating services for the
                                             			 selected template, proceed to the next step. |
| Step 7 | Close the popup window. |

| Step 1 | Find the Phone Template to which you want to add speed dials. |
|---|---|
| Step 2 | From the Phone Template Configuration window, do one of
                                             			 the following: Click Add a new SD in the Associated Information area. Choose Add/Update Speed Dials from the Related Links drop-down list box in the
                                                   				  upper, right-hand corner of the window. A popup window displays. In this window, you can designate
                                             			 speed-dial buttons for CiscoUnifiedIPPhones and expansion modules. |
| Step 3 | In the Speed Dial Settings area, enter the phone
                                             			 number, including any access or long-distance codes, in the Number field. Note When you enter the phone number, it can be followed by Forced Authorized Code (FAC)/Client Matter Code (CMC) if applicable.
                                                            You can enter the Phone number, FAC, CMC either in sequence or separated by a comma (,). The Speed dial may include any PIN,
                                                            Password or any other digits to be sent as DTMF digits after the call is connected. If you require a pause while connecting
                                                            through speed dial, you can enter one or more comma (,) where each comma represents a pause of 2 seconds. DTMF digits will
                                                            be sent after the call is connected and the appropriate pause duration corresponding to the number of commas is entered. | Note | When you enter the phone number, it can be followed by Forced Authorized Code (FAC)/Client Matter Code (CMC) if applicable.
                                                            You can enter the Phone number, FAC, CMC either in sequence or separated by a comma (,). The Speed dial may include any PIN,
                                                            Password or any other digits to be sent as DTMF digits after the call is connected. If you require a pause while connecting
                                                            through speed dial, you can enter one or more comma (,) where each comma represents a pause of 2 seconds. DTMF digits will
                                                            be sent after the call is connected and the appropriate pause duration corresponding to the number of commas is entered. |
| Note | When you enter the phone number, it can be followed by Forced Authorized Code (FAC)/Client Matter Code (CMC) if applicable.
                                                            You can enter the Phone number, FAC, CMC either in sequence or separated by a comma (,). The Speed dial may include any PIN,
                                                            Password or any other digits to be sent as DTMF digits after the call is connected. If you require a pause while connecting
                                                            through speed dial, you can enter one or more comma (,) where each comma represents a pause of 2 seconds. DTMF digits will
                                                            be sent after the call is connected and the appropriate pause duration corresponding to the number of commas is entered. |
| Step 4 | In the Label field, enter a label that corresponds to
                                             			 the speed-dial number. |
| Step 5 | In the Abbreviated Dial Settings area, you can set
                                             			 abbreviated speed dials for applicable IP phone models. Repeat Step 3 . |
| Step 6 | Click Save . BAT inserts the speed-dial settings in the template and the
                                             			 popup window closes. |

| Note | When you enter the phone number, it can be followed by Forced Authorized Code (FAC)/Client Matter Code (CMC) if applicable.
                                                            You can enter the Phone number, FAC, CMC either in sequence or separated by a comma (,). The Speed dial may include any PIN,
                                                            Password or any other digits to be sent as DTMF digits after the call is connected. If you require a pause while connecting
                                                            through speed dial, you can enter one or more comma (,) where each comma represents a pause of 2 seconds. DTMF digits will
                                                            be sent after the call is connected and the appropriate pause duration corresponding to the number of commas is entered. |
|---|---|

| Step 1 | Find the Phone Template to which you want to add speed dials. |
|---|---|
| Step 2 | In the Phone Template Configuration window, do one of
                                             			 the following: Click Add a new BLF SD in the Associated Information area. Choose Add/Update Busy Lamp Field Speed Dials from the Related Links drop-down list in the upper, right-hand corner of the window. A popup window displays. In this window, you can designate
                                             			 busy lamp field speed-dial (BLF SD) buttons for CiscoUnifiedIPPhones and
                                             			 expansion modules. |
| Step 3 | In the Speed Dial Settings area, enter the destination,
                                             			 including any access or long-distance codes, in the Destination field. |
| Step 4 | Choose the directory number from the drop-down list. You can click Find to search for directory numbers. |
| Step 5 | In the Label field, enter a label that corresponds to
                                             			 the BLF SD number. |
| Step 6 | Click Save . BAT inserts the BLF SD settings in the template, and the
                                             			 popup window closes. |

| Step 1 | Find the Phone Template to which you want to add BLF speed
                                             			 directed call park. |
|---|---|
| Step 2 | In the Phone Template Configuration window, do one of
                                             			 the following: Click Add a new BLF Directed Call Park in the Associated Information area. Choose Add/Update BLF Directed Call Park from the Related Links drop-down list box in the
                                                   				  upper, right-hand corner of the window. A popup window displays. In this window, you can designate
                                             			 BLF Directed Call Park buttons for CiscoUnifiedIPPhones and expansion
                                             			 modules. |
| Step 3 | In the Unassigned Busy Lamp Field/Directed Call Park Settings area, choose the directory number from the drop-down list. You can click Find to search for directory numbers. |
| Step 4 | In the Label field, enter a label that corresponds to
                                             			 the BLF Directed Call Park number. |
| Step 5 | Click Save . BAT inserts the BLF Directed Call Park settings in the
                                             			 template, and the popup window closes. |

| Step 1 | Find the Phone Template to which you want to add the intercom
                                             			 template. |
|---|---|
| Step 2 | In the Phone Template Configuration window, click Intercom [1] - Add a new Intercom in the Associated Information area. The Intercom Template Configuration window displays. |
| Step 3 | Enter or choose the appropriate values for the intercom template
                                             			 settings. |
| Step 4 | Click Save . BAT adds the intercom template to the phone template
                                             			 configuration. |
| Step 5 | To add settings for any additional intercom templates, repeat Step 2 through Step 4 . If you choose Back to Find/List from the Related Links drop-down list box in the upper, right, corner of the Intercom Template Configuration window, the Find and List Intercom Directory Number window displays. Note If you choose Back to Find/List from the Related Links drop-down list box in the upper, right, corner of the Intercom Template Configuration window, the Find and List Intercom Directory Number window displays. Click Find and enter the appropriate search criteria and to find existing Intercom directory numbers. In the Find and List Intercom Directory Number window, click Add New to add a new intercom directory number. | Note | If you choose Back to Find/List from the Related Links drop-down list box in the upper, right, corner of the Intercom Template Configuration window, the Find and List Intercom Directory Number window displays. |
| Note | If you choose Back to Find/List from the Related Links drop-down list box in the upper, right, corner of the Intercom Template Configuration window, the Find and List Intercom Directory Number window displays. |

| Note | If you choose Back to Find/List from the Related Links drop-down list box in the upper, right, corner of the Intercom Template Configuration window, the Find and List Intercom Directory Number window displays. |
|---|---|

| Step 1 | Find the Phone Template that you want to modify. |
|---|---|
| Step 2 | In the phone Template Configuration window, add, change, or
                                          			 remove settings in the template. See Table 1 for more information. |
| Step 3 | After you have modified the settings to update the template, click Save . |

| Note | Ensure that the new template that you create is the same device
                                             			 type as the original template, such as CiscoIPPhone 7975. |
|---|---|

| Step 1 | Find the Phone Template that you want to copy. |
|---|---|
| Step 2 | Copy the Phone Template. Do one of the following: In the Phone Template Configuration window, verify
                                                				  that this is the template that you want to copy and click Copy . In the Find and List Phone Templates window, click
                                                				  the icon in the Copy column that corresponds to the phone
                                                				  template that you want to copy. To copy a template and all the lines associated with that
                                                				  template, in the Find and List Phone Templates window, click
                                                				  the icon in the Super Copy column that corresponds to
                                                				  the phone template with the lines that you want to copy. |
| Step 3 | In the Template Name field, enter a name for the
                                          			 template. The name can contain up to 50 alphanumeric characters. Example: Sales_7975. |
| Step 4 | Update the fields as needed for the new template. See Table 1 for more information. |
| Step 5 | Click Save . The template that is added to BAT displays in the Phone
                                          			 Templates column on the left. |

| Caution | If you submit a job that uses a particulate phone template and you
                                             			 delete that phone template, the job also gets deleted. |
|---|---|

| Step 1 | Find the Phone Template that you want to delete. |
|---|---|
| Step 2 | Delete the Phone Template. Do one of the following: In the Phone Template Configuration window, verify
                                                				  that this is the template that you want to delete and click Delete . In the Find and List Phone Templates window. check
                                                				  the check box next to the template that you want to delete and click Delete Selected . A message displays that asks you to confirm the delete operation. |
| Step 3 | To delete the template, click OK . The template name disappears from the list
                                          			 of phone templates list on the Find and List Phone Templates window. |

| Field | Description |
|---|---|
| Device Information |
| Device
                                             					 Trust Mode | Select
                                             					 whether the device is trusted or not trusted. You can configure this setting
                                             					 for analog phones using SCCP, and for some third-party endpoints. |
| Template
                                             					 Name | Enter the
                                             					 name for the template. |
| Description | Enter a
                                             					 description for the phone template that you want to create. The description can
                                             					 include up to 50 characters in any language, but it cannot include
                                             					 double-quotes ("), percentage sign ( % ), ampersand (&), back-slash ( \ ), or angle
                                             					 brackets (<>). |
| Requires Activation Code for Onboarding | Check this check box if you want to use activation codes, rather than autoregistration, to onboard phones that use this template. Note This option is available only for phones that support activation codes. | Note | This option is available only for phones that support activation codes. |
| Note | This option is available only for phones that support activation codes. |
| DevicePool | Choose the
                                             					 device pool for this group of phones or ports. For devices, a devicepool defines sets of common characteristics, such as region, date/time group, Unified Communications Manager group, and calling search space for auto-registration. |
| Common
                                             					 Device Configuration | Choose the
                                             					 common device configuration to which you want this phone assigned. The common
                                             					 device configuration includes the attributes (services or features) that are
                                             					 associated with a particular user. You configure the Common device
                                             					 configurations in the Common Device Configuration window. To see the
                                             					 common device configuration settings, click the View Details link. |
| Phone Button
                                             					 Template | Choose the
                                             					 button template for all phones in this group. Button templates determine the
                                             					 button identity (line, speed dial) and the button location on the phone. Button
                                             					 templates include the expansion modules. |
| Softkey
                                             					 Template | Choose the
                                             					 softkey template to be used for all phones in this group. |
| Common Phone
                                             					 Profile | From the drop-down list, choose a common phone profile from the list of available common phone profiles. |
| Calling
                                             					 Search Space | Choose the
                                             					 calling search space for this group of phones/ports. A calling
                                             					 search space specifies the collection of Route Partitions that are searched to
                                             					 determine how a dialed number should be routed. |
| AAR Calling
                                             					 Search Space | Choose the
                                             					 appropriate calling search space for the device to use when it performs
                                             					 automated alternate routing (AAR). The AAR calling search space specifies the
                                             					 collection of route partitions that are searched to determine how to route a
                                             					 collected (originating) number that is otherwise blocked due to insufficient
                                             					 bandwidth. |
| Media
                                             					 Resource Group List | Choose the
                                             					 media resource group list (MRGL) for this group of phones/ports. An MRGL
                                             					 specifies a list of prioritized media resource groups. An application can
                                             					 choose required media resources from the available ones according to the order
                                             					 that is defined in the MRGL. |
| User Hold
                                             					 MOH Audio Source | Choose the
                                             					 user hold audio source for this group of phones/ports. The user
                                             					 hold audio source identifies the audio source from which music is played when a
                                             					 user places a call on hold. |
| Network Hold
                                             					 MOH Audio Source | Choose the
                                             					 network hold audio source for this group of IP phones or ports. The network
                                             					 hold audio source identifies the audio source from which music is played when
                                             					 the system places a call on hold, such as when the user transfers or parks a
                                             					 call. |
| Location | Choose the
                                             					 appropriate location for this group of IP phones or ports. The location
                                             					 specifies the total bandwidth that is available for calls to and from this
                                             					 location. A location setting of None means that the locations feature does not
                                             					 keep track of the bandwidth that this CiscoIPPhone consumes. |
| AAR Group | Choose the
                                             					 automated alternate routing (AAR) group for this device. The AAR group provides
                                             					 the prefix digits that are used to route calls that are otherwise blocked due
                                             					 to insufficient bandwidth. Set AAR
                                             					 Group to < None > to prevent rerouting blocked calls. |
| User
                                             					 Locale | Choose the
                                             					 country and language set that you want to associate with this group of IP
                                             					 phones. This choice determines which cultural-dependent attributes exist for this user and which language displays for the user in
                                             the Unified Communications Manager user windows and phones. |
| Network
                                             					 Locale | Choose the
                                             					 network locale that you want to associate with this group of phones. The
                                             					 Network Locale comprises a set of tones and cadences that Cisco gateways and
                                             					 phones use when they communicate with the PSTN and other networks in a specific
                                             					 geographical area. |
| Built In
                                             					 Bridge | Enable or disable the built-in conference bridge for the barge feature by using the Built In Bridge drop-down list (choose On , Off , or Default ). |
| Privacy | For each phone that wants Privacy, choose On in the Privacy drop-down list. |
| Device
                                             					 Mobility Mode | From the drop-down list, turn the device mobility feature on or off for this device or choose Default to use the default device mobility mode. Click View Current Device Mobility Settings to display the
                                             					 current values of these device mobility parameters: Cisco Unified Communications Manager Group Roaming Device Pool Location Region Network Locale AAR Group AAR Calling Search Space Device Calling Search Space Media Resource Group List SRST |
| Owner User
                                             					 ID | Enter a
                                             					 user ID for the primary phone user. |
| Mobility
                                             					 User ID (Dual-mode
                                             					 phones only) | From the drop-down list, choose the user ID of the person to whom this dual-mode phone is assigned. Note The
                                                         						Mobility User ID configuration gets used for the Cisco Unified Mobility and
                                                         						Mobile Voice Access features for dual-mode phones. Note The
                                                         						Owner User ID and Mobility User ID can differ. | Note | The
                                                         						Mobility User ID configuration gets used for the Cisco Unified Mobility and
                                                         						Mobile Voice Access features for dual-mode phones. | Note | The
                                                         						Owner User ID and Mobility User ID can differ. |
| Note | The
                                                         						Mobility User ID configuration gets used for the Cisco Unified Mobility and
                                                         						Mobile Voice Access features for dual-mode phones. |
| Note | The
                                                         						Owner User ID and Mobility User ID can differ. |
| Phone
                                             					 Personalization | From the drop-down list, enable or disable the personalization settings on the phone, or choose Default to use the phone personalization that is set in the Common Phone Profile. You can choose one of the following options: Disabled —None of the personalization settings on the phone get activated. Enabled —This setting accepts a personalized background image file, which is used for the phone screen; it accepts a preview image
                                                   file for temporary display; and it accepts a personalized tone file, so the default ring tone can be personalized. Default —Use the phone personalization setting that is in the Common Phone Profile. |
| Services
                                             					 Provisioning | From the drop-down list, choose the Services Provisioning setting that you want to use from the following values: Internal External URLs Both Default: Internal This
                                             					 parameter controls whether the phone uses the services provisioned from the
                                             					 configuration file (Internal), services received from the Services URLs
                                             					 (External URLs), or both. The External URLs option provides backward
                                             					 compatibility with third party provisioning servers. The Both option allows
                                             					 users to subscribe to the services specified in the configuration file while
                                             					 also appending services from an external provisioning server. This is a
                                             					 required field. |
| Phone Load
                                             					 Name | Enter the
                                             					 custom phone load, if applicable. Note Any
                                                         						value that is entered in this field overrides the default value for the chosen
                                                         						model. For more information about CiscoIPPhone software and configuration, refer to the CiscoIPPhone Administration Guide for Unified Communications Manager , which is specific to the phone model. | Note | Any
                                                         						value that is entered in this field overrides the default value for the chosen
                                                         						model. |
| Note | Any
                                                         						value that is entered in this field overrides the default value for the chosen
                                                         						model. |
| Single
                                             					 Button Barge | From the drop-down list, enable or disable the Single Button Barge/cBarge feature for this device or choose Default to use the service parameter setting. Off —This setting disables the Single Button Barge/cBarge feature; however, the regular Barge or cBarge features will still work. Barge —This setting enables the Singe Button Barge feature. cBarge —This setting enables the Single Button cBarge feature. Default —This setting uses the Single Button Barge/cBarge setting that is in the service parameter. |
| Join
                                             					 Across Lines | From the drop-down list, enable or disable the Join Across Lines feature for this device or choose Default to use the service parameter setting. Off —This setting disables the Join Across Lines feature. On —This setting enables the Join Across Lines feature. Default —Uses the Join Across Lines setting that is in the service parameter. |
| Use
                                             					 Trusted Relay Point | From the drop-down list, enable or disable whether Unified Communications Manager inserts a trusted relay point (TRP) device with this media endpoint. Choose one of the following values: Default —If you choose this value, the device uses the Use Trusted Relay Point setting from the common device configuration with which
                                                   this device associates. Off —Choose this value to disable the use of a TRP with this device. This setting overrides the Use Trusted Relay Point setting
                                                   in the common device configuration with which this device associates. On —Choose this value to enable the use of a TRP with this device. This setting overrides the Use Trusted Relay Point setting
                                                   in the common device configuration with which this device associates. A Trusted
                                             					 Relay Point (TRP) device designates an MTP or transcoder device that is labeled
                                             					 as Trusted Relay Point. Unified Communications Manager places the TRP closest to the associated endpoint device if more than one resource is needed for the endpoint (for example,
                                             a transcoder or RSVPAgent). If both
                                             					 TRP and MTP are required for the endpoint, TRP gets used as the required MTP. |
| BLF
                                             					 Audible Alert Setting (Phone Idle) | From the drop-down list, choose the BLF Audible Alert setting that you want to use from the following values: On Off Default This
                                             					 parameter provides an audible alert in addition to a visual alert on a phone
                                             					 that is currently idle when a call comes in to one of the lines that is
                                             					 monitored by way of a busy lamp field (BLF) button. This is a
                                             					 required field. |
| BLF
                                             					 Audible Alert Setting (Phone Busy) | This
                                             					 parameter for this required field provides an audible alert in addition to a
                                             					 visual alert on a phone that is currently in use when a call comes in to one of
                                             					 the lines that is monitored by way of a busy lamp field (BLF) button. From the drop-down list, choose the BLF Audible Alert setting that you want to use from the following values: On Off Default |
| Always Use
                                             					 Prime Line | From the drop-down list, choose one of the following options: Off —When the phone is idle and receives a call on any line, the phone user answers the call from the line on which the call is
                                                   received. On —When the phone is idle (off-hook) and receives a call on any line, the primary line gets chosen for the call. Calls on other
                                                   lines continue to ring, and the phone user must select those other lines to answer these calls. Default — Unified Communications Manager uses the configuration from the Always Use Prime Line service parameter, which supports the Cisco CallManager service. |
| Always Use
                                             					 Prime Line for Voice Message | From the drop-down list, choose one of the following options: On —If the phone is idle, the primary line on the phone becomes the active line for retrieving voice messages when the phone
                                                   user presses the Messages button on the phone. Off —If the phone is idle, pressing the Messages button on the phone automatically dials the voice-messaging system from the line
                                                   that has a voice message. Unified Communications Manager always selects the first line that has a voice message. If no line has a voice message, the primary line gets used when the
                                                   phone user presses the Messages button. Default — Unified Communications Manager uses the configuration from the Always Use Prime Line for Voice Message service parameter, which supports the Cisco CallManager
                                                   service. |
| Geo
                                             					 Location | From the drop-down list, choose a geo location. You can
                                             					 choose the Unspecified geo location, which designates that this
                                             					 device does not associate with a geo location. You can
                                             					 also choose a geolocation that has been configured with the System > Geolocation
                                                   						  Configuration menu option. |
| Feature
                                             					 Control Policy | Choose the
                                             					 Feature Control Policy for this group of phones. A feature
                                             					 control policy specifies the appearance of features and the associated softkeys
                                             					 that are displayed on the phone. |
| Device
                                             					 Security Mode | From the drop-down list, choose the mode that you want to set for the device: Use System
                                                					 Default —The phone uses the value that you specified for the enterprise
                                             				  parameter, Device Security Mode. Non-secure —No security features exist for the phone. A TCP connection opens to Unified Communications Manager . Authenticated — Unified Communications Manager provides integrity and authentication for the phone. A TLS connection that uses NULL/SHA opens. Encrypted — Unified Communications Manager provides integrity, authentication, and encryption for the phone. A TLS connection that uses AES128 / SHA opens. This field
                                             					 displays only if the phone model supports authentication or encryption. |
| Retry
                                             					 Video Call as Audio | This check
                                             					 box applies only to video endpoints that receive a call. If this phone receives
                                             					 a call that does not connect as video, the call tries to connect as an audio
                                             					 call. By
                                             					 default, the system checks this check box to specify that this device should
                                             					 immediately retry a video call as an audio call (if it cannot connect as a
                                             					 video call) prior to sending the call to call control for rerouting. If you
                                             					 uncheck this check box, a video call that fails to connect as video does not
                                             					 try to establish as an audio call. The call then fails to call control, and
                                             					 call control routes the call via Automatic Alternate Routing (AAR) and / or route / hunt list. |
| Ignore
                                             					 Presentation Indicators (Internal Calls Only) | Check this check box to configure call display restrictions on a call-by-call basis. When this check box is checked, Unified Communications Manager ignores any presentation restriction that is received for internal calls. |
| Allow
                                             					 Control of Device from CTI | Check this
                                             					 check box to allow control of all CTI controllable devices from CTI. You can enable or disable this check box based on CTI Controllable Device Type and Device Protocol. Note Cisco dual-mode devices (Jabber) such as Android, iPhone, and iPad operating in WiFi mode are monitored through CTI and not
                                                         controlled. However, devices operating in GSM mode cannot be monitored or controlled. | Note | Cisco dual-mode devices (Jabber) such as Android, iPhone, and iPad operating in WiFi mode are monitored through CTI and not
                                                         controlled. However, devices operating in GSM mode cannot be monitored or controlled. |
| Note | Cisco dual-mode devices (Jabber) such as Android, iPhone, and iPad operating in WiFi mode are monitored through CTI and not
                                                         controlled. However, devices operating in GSM mode cannot be monitored or controlled. |
| Logged
                                             					 into Hunt Group | This check
                                             					 box, which gets checked by default for all phones, indicates that the phone is
                                             					 currently logged in to a hunt list (group). When the phone gets added to a hunt
                                             					 list, the administrator can log the user in or out by checking (and unchecking)
                                             					 this check box. Users use
                                             					 the softkey on the phone to log their phone in or out of the hunt list. |
| Remote
                                             					 Device | If you are experiencing delayed connect times over SCCP to remote sites, check the Remote Device check box in the Phone Configuration
                                             window. Checking this check box tells Unified Communications Manager to allocate a buffer for the phone device when it registers
                                             and to bundle SCCP messages to the phone. Because
                                             					 this feature consumes resources, be sure to check this check box only when you
                                             					 are experiencing signaling delays for phones that are running SCCP. Most users
                                             					 do not require this option. |
| Protected
                                             					 Device | Check this
                                             					 check box to designate a phone as "protected." This enables the phone to play a two-second tone
                                             					 notifying the user when a call is both encrypted and both phones are configured
                                             					 as protected devices. The tone plays for both parties when the call is
                                             					 answered. The tone does not play unless both phones are "protected" and the call occurs over encrypted media. Tip For a detailed description of the secure-tone feature and the
                                                      					 configuration requirements, see the Cisco
                                                         						Unity Connection System Administration Guide . | Tip | For a detailed description of the secure-tone feature and the
                                                      					 configuration requirements, see the Cisco
                                                         						Unity Connection System Administration Guide . |
| Tip | For a detailed description of the secure-tone feature and the
                                                      					 configuration requirements, see the Cisco
                                                         						Unity Connection System Administration Guide . |
| Hotline
                                             					 Device | Check this
                                             					 check box to make this device a Hotline device. Hotline devices can only
                                             					 connect to other Hotline devices. This feature is an extension of PLAR, which
                                             					 configures a phone to automatically dial one directory number when it goes
                                             					 off-hook. Hotline provides additional restrictions that you can apply to
                                             					 devices that use PLAR. To
                                             					 implement Hotline, you must also create a softkey template without
                                             					 supplementary service softkeys, and apply it to the Hotline device. |
| Number Presentation Transformation |
| Caller ID for Calls from
                                                						This Phone |
| Calling Party
                                             					 Transformation CSS | From the drop-down list, choose the calling search space (CSS) that contains the calling party transformation pattern that
                                             you want to apply on the calling number when this phone initiates a call. When this
                                             					 phone initiates a call, Unified Communications Manager transforms the calling
                                             					 party using the digit transformations that are configured on the matching
                                             					 calling party transformation pattern. This setting allows you to transform the
                                             					 calling party number before Unified Communications Manager routes the call. For
                                             					 example, a transformation pattern can change a phone extension to an E.164
                                             					 number. This setting is generally configured when users dial using a URI
                                             					 instead of digits. Unified Communications Manager allows calling party
                                             					 transformations on various patterns when users dial using digits; this setting
                                             					 provides similar transformation provision even when users dial using a URI. |
| Use Device Pool Calling
                                             					 Party Transformation CSS (Caller ID for Calls from This Phone) | Check this check box to use
                                             					 the Calling Party Transformation CSS that is configured at the device pool to
                                             					 which this phone belongs for transforming the calling party for calls that are
                                             					 initiated from this phone. At the device pool, the Calling Party Transformation
                                             					 CSS that is present under Phone Settings is used to transform the calling party
                                             					 for calls initiated from this phone. Leave this check box
                                             					 unchecked to apply the Calling Party Transformation CSS setting that appears in
                                             					 this configuration window. |
| Remote Number Transformation |
| Calling Party
                                             					 Transformation CSS | From the drop-down list, choose the calling search space (CSS) that contains the calling party transformation pattern that
                                             you want to apply on the remote calling number for the calls that are received on this phone. Unified
                                             					 Communications Manager transforms the remote calling number using the digit
                                             					 transformations that are configured on the matching calling party
                                             					 transformation pattern before presenting it to this device. For
                                             					 example, a transformation pattern can change a remote number in E.164 format to
                                             					 a localized version. Use this
                                             					 setting to transform the remote connected number for direct calls that are
                                             					 initiated from this phone. Use this setting also to transform a remote
                                             					 connected number after you invoke the feature irrespective of the direction of
                                             					 the call. The transformation of the remote connected number is controlled using
                                             					 the service parameter “Apply Transformations on Remote Number,” present under
                                             					 the Advanced section of Cisco Call Manager service. For more information, refer
                                             					 to the description for this parameter. |
| Use Device
                                             					 Pool Calling Party Transformation CSS (Device Mobility Related Information) | Check this
                                             					 check box to apply the Calling Party Transformation CSS that is configured at
                                             					 the device pool to which this phone belongs for transforming the remote calling
                                             					 and remote connected number. At the device pool, the Calling Party
                                             					 Transformation CSS present under Device Mobility Related Information section is
                                             					 used to transform the remote calling and remote connected number. Leave this
                                             					 check box unchecked to apply the Calling Party Transformation CSS setting that
                                             					 appears in this configuration window for transforming the remote number. |
|  |  |
| Associated Mobility
                                                						Identity —These mobility fields are available only for Nokia S60
                                             					 device and Cisco Unified Mobile Communicator phones. Click the Add New Mobile Identity link to display the Mobile
                                             					 Identity Configuration page. |
| Name | Enter a
                                             					 name that identifies the mobile identity. |
| Destination Number | Enter the
                                             					 telephone number for the identity. Include the area code and any additional
                                             					 digits that are required to obtain an outside line. Maximum field length equals
                                             					 24 characters; individual characters can take the values 0-9, * , and # . Cisco recommends that you configure the caller ID of
                                             					 the smart phone destination. Add the
                                             					 necessary translation pattern or route patterns to route the destination
                                             					 number. |
| Answer Too
                                             					 Soon Timer | Enter the
                                             					 minimum time in milliseconds that must pass before the mobile phone can be
                                             					 answered. Range: 0 -
                                             					 10,000 milliseconds Default:
                                             					 1,500 milliseconds |
| Answer Too
                                             					 Late Timer | Enter the
                                             					 maximum time in milliseconds that can pass before the mobile phone must be
                                             					 answered. Range:
                                             					 10,000 - 300,000 milliseconds Default:
                                             					 19,000 milliseconds |
| Delay
                                             					 Before Ringing Timer | Enter the
                                             					 time that elapses before the mobile phone rings when a call is transferred from
                                             					 the desktop phone. Range: 0 -
                                             					 30,000 milliseconds Default:
                                             					 4,000 milliseconds |
| Time of
                                             					 Day Access | From the drop-down list, choose a time-of-day access record to associate with this destination. |
| Time Zone | From the drop-down list, choose a time zone to use for this remote destination. Note The time
                                                         						zone that you use for this remote destination is used by the time-of-day access
                                                         						feature to allow or block calls to this destination. | Note | The time
                                                         						zone that you use for this remote destination is used by the time-of-day access
                                                         						feature to allow or block calls to this destination. |
| Note | The time
                                                         						zone that you use for this remote destination is used by the time-of-day access
                                                         						feature to allow or block calls to this destination. |
| Mobile
                                             					 Phone | Check the
                                             					 check box if you want calls that are answered by the desktop phone to be sent
                                             					 to your mobile phone as the remote destination. Note You must
                                                         						check this check box for Cisco Unified Mobility to work with this remote
                                                         						destination. | Note | You must
                                                         						check this check box for Cisco Unified Mobility to work with this remote
                                                         						destination. |
| Note | You must
                                                         						check this check box for Cisco Unified Mobility to work with this remote
                                                         						destination. |
| Enable
                                             					 Cisco Unified Mobility | Check the
                                             					 check box to allow an incoming call to ring your desktop phone and remote
                                             					 destination at the same time. |
| Associated Remote
                                                						Destinations — Click the Add a New Remote Destination link to display the Remote Destination Configuration page |
| Name | Enter a
                                             					 name that identifies the remote destination. |
| Destination Number | Enter the
                                             					 telephone number for the destination. Include the area code and any additional
                                             					 digits that are required to obtain an outside line. Maximum field length equals
                                             					 24 characters; individual characters can take the values 0-9, * , and # . Cisco recommends that you configure the caller ID of
                                             					 the remote destination. Add the
                                             					 necessary translation pattern or route patterns to route the destination
                                             					 number. |
| Answer Too
                                             					 Soon Timer | Enter the
                                             					 minimum time in milliseconds that must pass before the mobile phone can be
                                             					 answered. Range: 0 -
                                             					 10,000 milliseconds Default:
                                             					 1,500 milliseconds |
| Answer Too
                                             					 Late Timer | Enter the
                                             					 maximum time in milliseconds that can pass before the mobile phone must be
                                             					 answered. Range:
                                             					 10,000 - 300,000 milliseconds Default:
                                             					 19,000 milliseconds |
| Delay
                                             					 Before Ringing Timer | Enter the
                                             					 time that elapses before the mobile phone rings when a call is transferred from
                                             					 the desktop phone. Range: 0 -
                                             					 30,000 milliseconds Default:
                                             					 4,000 milliseconds |
| Time of
                                             					 Day Access | From the drop-down list, choose a time-of-day access record to associate with this remote destination. |
| Time Zone | From the drop-down list, choose a time zone to use for this remote destination. Note The time
                                                         						zone that you use for this remote destination is used by the time-of-day access
                                                         						feature to allow or block calls to this remote destination. | Note | The time
                                                         						zone that you use for this remote destination is used by the time-of-day access
                                                         						feature to allow or block calls to this remote destination. |
| Note | The time
                                                         						zone that you use for this remote destination is used by the time-of-day access
                                                         						feature to allow or block calls to this remote destination. |
| Mobile
                                             					 Phone | Check the
                                             					 check box if you want calls that are answered by the desktop phone to be sent
                                             					 to your mobile phone as the remote destination. Note You must
                                                         						check this check box for Cisco Unified Mobility to work with this remote
                                                         						destination. | Note | You must
                                                         						check this check box for Cisco Unified Mobility to work with this remote
                                                         						destination. |
| Note | You must
                                                         						check this check box for Cisco Unified Mobility to work with this remote
                                                         						destination. |
| Enable
                                             					 Cisco Unified Mobility | Check the
                                             					 check box to allow an incoming call to ring your desktop phone and remote
                                             					 destination at the same time. |
| Protocol Specific
                                                						Information |
| Packet
                                             					 Capture Mode | From the drop-down list, choose the mode that you want to set for signal packet capture: None —Choose None if you do not want to specify a mode. Real-Time Mode —Use this mode for real-time signal packet capture. Batch Processing Mode —Use this mode for batch processing signal packet capture mode. |
| Packet
                                             					 Capture Duration | Enter the
                                             					 time for packet capture in minutes. You can enter a maximum duration of 300
                                             					 minutes. The default duration specifies 60 minutes. |
| BLF
                                             					 Presence Group | Used with
                                             					 the BLF Presence feature, the phone that is running SIP or SCCP serves as a
                                             					 watcher because it requests status about the presence entity; for example,
                                             					 directory number, that is configured as a BLF speed dial button on the phone. If you
                                             					 want the phone to receive the status of the presence entity, choose a BLF
                                             					 Presence group that is allowed to view the status of the Presence group that is
                                             					 applied to the directory number, as indicated in the BLF Presence Group
                                             					 Configuration window. |
| SIP Dial Rules | If required, choose the appropriate SIP dial rule. SIP dial
                                             					 rules provide local dial plans for Cisco IP phones 7940, and 7975 that are
                                             					 running SIP, so users do not have to press a key or wait for a timer before the
                                             					 call gets processed. Leave the SIP Dial Rules field set to
                                             					 < None > if you do not want dial rules applied to the IP
                                             				  phone that is running SIP. This means the user will have to use the Dial
                                             				  softkey or wait for the timer to expire before the call gets processed. |
| Device
                                             					 Security Profile | For phones
                                             					 that are running SCCP or SIP, choose the security profile that you want to
                                             					 apply to the device. All phones
                                             					 require that you apply a security profile. If the phone does not support
                                             					 security, choose a nonsecure profile. |
| MTP
                                             					 Preferred Originating Codec | From the drop-down list, choose the codec to use if a media termination point is required for SIP calls. |
| Rerouting
                                             					 Calling Search Space | From the drop-down list, choose a calling search space to use for rerouting. The
                                             					 rerouting calling search space of the referrer gets used to find the route to
                                             					 the refer-to target. When the Refer fails due to the rerouting calling search
                                             					 space, the Refer Primitive rejects the request with the "405
                                                						Method Not Allowed" message. The
                                             					 redirection (3xx) primitive and transfer feature also uses the rerouting
                                             					 calling search space to find the redirect-to or transfer-to target. |
| Out-of-Dialog Refer Calling Search Space | From the drop-down list, choose an out-of-dialog refer calling search space. Unified Communications Manager uses the out-of-dialog (OOD) Refer Authorization calling search space (CSS) to authorize the SIP out-of-dialog Refer. The
                                             administrator can restrict the use of out-of-dialog Refer by configuring the OOD CSS of the Referrer. Refer Primitive rejects
                                             the OOD Refer request with a "403 Forbidden" message. |
| SUBSCRIBE
                                             					 Calling Search Space | Used with the Presence feature, the SUBSCRIBE Calling Search Space determines how Unified Communications Manager routes the subscription requests that come from the phone. From the drop-down list, choose the calling search space that
                                             you want to use for this purpose. |
| SIP
                                             					 Profile | Choose the
                                             					 default SIP profile or a specific profile that was previously created. SIP
                                             					 profiles provide specific SIP information for the phone such as default
                                             					 telephony event payload type, registration and keepalive timers, media ports,
                                             					 Iris, and dynamic DNS server addresses. |
| Digest
                                             					 User | Used with
                                             					 digest authentication (SIP security), choose an end user that you want to
                                             					 associate with the phone. Ensure
                                             					 that you configured digest credentials for the user that you choose, as
                                             					 specified in the End User Configuration window. After you
                                             					 save the phone configuration and reset the phone, the digest credentials for
                                             					 the user get added to the phone configuration file. For more information on digest authentication, refer to the Cisco  Unified Communications Manager Security Guide . |
| Media
                                             					 Termination Point Required | Use this
                                             					 field to indicate whether a media termination point is used to implement
                                             					 features that H.323 does not support (such as hold and transfer). Check the
                                             					 Media Termination Point Required check box if you want to use an MTP to
                                             					 implement features. Uncheck the Media Termination Point Required check box if
                                             					 you do not want to use an MTP to implement features. Use this
                                             					 check box only for H.323 clients and those H.323 devices that do not support
                                             					 the H.245 empty capabilities set or if you want media streaming to terminate
                                             					 through a single source. |
| Unattended
                                             					 Port | Check this
                                             					 check box to indicate an unattended port on this device. |
| Require
                                             					 DTMF Reception | For phones
                                             					 that are running SIP and SCCP, check this check box to require DTMF reception
                                             					 for this phone. |
| RFC2833
                                             					 Disabled | For phones
                                             					 that are running SCCP, check this check box to disable RFC2833 support. |
| Certification Authority
                                                						Proxy Function (CAPF) Information (These parameters display only for
                                             					 devices with the capability to support authentication or encryption.) |
| Certificate Operation | From the drop-down list, choose the Certification Operation that you want to perform from the following options: No Pending Operation —No pending Certification Operation lists exist for this device. Choosing this option disables the remaining CAPF fields. Install/Upgrade —Install or upgrade a Certification Operation. Delete —Delete a Certification Operation. Troubleshoot —Troubleshoot a Certification Operation. |
| Authentication Mode | From the drop-down list, choose the Authentication Mode by which you want the phone to authenticate with CAPF during the certificate
                                             operation from the following options: By Null String —Install/upgrade, delete, or troubleshoot a locally significant certificate without user intervention. < None > Note This
                                                         						option prompts you to specify a value for the Authentication Mode. By Authentication String—Installs/upgrades, deletes, or troubleshoots a locally significant certificate only when the user
                                                   enters the CAPF authentication string on the phone. By Existing Certificate (precedence to LSC)—Installs or upgrades, deletes, or troubleshoots a locally significant certificate
                                                   if a manufacture-installed certificate (MIC) or locally significant certificate (LSC) exists in the phone. Note Before
                                                         						you choose this option, verify that a certificate exists in the phone. If you
                                                         						choose this option and no certificate exists in the phone, the operation fails. By Existing Certificate (precedence to MIC)—Installs/upgrades, deletes, or troubleshoots a locally significant certificate
                                                   if a LSC or MIC exists in the phone. Note Before
                                                         						you choose this option, verify that a certificate exists in the phone. If you
                                                         						choose this option and no certificate exists in the phone, the operation fails. | Note | This
                                                         						option prompts you to specify a value for the Authentication Mode. | Note | Before
                                                         						you choose this option, verify that a certificate exists in the phone. If you
                                                         						choose this option and no certificate exists in the phone, the operation fails. | Note | Before
                                                         						you choose this option, verify that a certificate exists in the phone. If you
                                                         						choose this option and no certificate exists in the phone, the operation fails. |
| Note | This
                                                         						option prompts you to specify a value for the Authentication Mode. |
| Note | Before
                                                         						you choose this option, verify that a certificate exists in the phone. If you
                                                         						choose this option and no certificate exists in the phone, the operation fails. |
| Note | Before
                                                         						you choose this option, verify that a certificate exists in the phone. If you
                                                         						choose this option and no certificate exists in the phone, the operation fails. |
| Authentication String | If you chose the By Authentication String option from the Authentication Mode drop-down list in the security profile, this setting applies. Manually enter a numeric string that contains 4 to 10 digits.
                                             To install, upgrade, or troubleshoot a locally significant certificate, the phone user or administrator must enter the authentication
                                             string on the phone. |
| Key Order | This field
                                             					 specifies the sequence of the key for CAPF. Select one of the following values
                                             					 from the drop-down list: RSA Only EC Only EC Preferred, RSA
                                                      							 Backup Note When you
                                                         						add a phone based on the value in Key Order , RSA Key Size , and EC Key Size fields, the device security profile is
                                                         						associated with the phone. If you select the EC Only value with the EC Key Size value of 256 bits then the device
                                                         						security profile appends with EC-256 value. | Note | When you
                                                         						add a phone based on the value in Key Order , RSA Key Size , and EC Key Size fields, the device security profile is
                                                         						associated with the phone. If you select the EC Only value with the EC Key Size value of 256 bits then the device
                                                         						security profile appends with EC-256 value. |
| Note | When you
                                                         						add a phone based on the value in Key Order , RSA Key Size , and EC Key Size fields, the device security profile is
                                                         						associated with the phone. If you select the EC Only value with the EC Key Size value of 256 bits then the device
                                                         						security profile appends with EC-256 value. |
| RSA Key
                                             					 Size (Bits) | From the drop-down list, choose one of the these values— 512 , 1024 , 2048 , 3072 , or 4096 . Note Some
                                                         						phone models may fail to register if the RSA key length selected for the CallManager Certificate Purpose is greater than 2048. From the
                                                         						Unified CM Phone Feature List Report on the Cisco Unified Reporting Tool
                                                         						(CURT), you can check the 3072/4096 RSA key size support feature for the list
                                                         						of supported phone models. | Note | Some
                                                         						phone models may fail to register if the RSA key length selected for the CallManager Certificate Purpose is greater than 2048. From the
                                                         						Unified CM Phone Feature List Report on the Cisco Unified Reporting Tool
                                                         						(CURT), you can check the 3072/4096 RSA key size support feature for the list
                                                         						of supported phone models. |
| Note | Some
                                                         						phone models may fail to register if the RSA key length selected for the CallManager Certificate Purpose is greater than 2048. From the
                                                         						Unified CM Phone Feature List Report on the Cisco Unified Reporting Tool
                                                         						(CURT), you can check the 3072/4096 RSA key size support feature for the list
                                                         						of supported phone models. |
| EC Key
                                             					 Size (Bits) | From the drop-down list, choose one of the these values— 256 , 384 , or 521 . |
| Operation
                                             					 Completes By | This
                                             					 field, which supports the Install/Upgrade , Delete , and Troubleshoot Certificate Operation options, specifies
                                             				  the date and time in which you must complete the operation. |
| Certificate Operation Status | This field
                                             					 displays the progress of the certificate operation; for example, <operation
                                             					 type> pending, failed, or successful, where operating type equals the Install/Upgrade , Delete , or Troubleshoot Certificate Operation options. You cannot
                                             				  change the information that displays in this field. |
| Expansion Module
                                                						Information |
| Module 1 | Choose the
                                             					 expansion module if it is installed in the phone. |
| Module1
                                             					 Load Name | Enter the
                                             					 firmware load for the first CiscoUnifiedIPPhone Expansion Module, if
                                             					 applicable. Leave this field blank to use the default load. |
| Module 2 | Choose the
                                             					 expansion module if it is installed in the phone. |
| Module 2
                                             					 Load Name | Enter the
                                             					 firmware load for the second CiscoUnifiedIPPhone Expansion Module, if
                                             					 applicable. Leave this field blank to use the default load. |
| CiscoUnifiedIPPhone -
                                                						External Data Locations |
| Information | Enter the
                                             					 help text URL for the information button for CiscoUnifiedIPPhones. |
| Directory | Enter the
                                             					 URL of the directory server for CiscoUnifiedIPPhones. |
| Messages | Enter the
                                             					 voice-messaging access pilot number for CiscoUnified IPPhones. |
| Services | Enter the
                                             					 URL for the services menu for CiscoUnifiedIPPhones. |
| Authentication Server | Enter the
                                             					 URL that the phone uses to validate requests that are made to the phones web
                                             					 server. If you do not provide an authentication URL, the advanced features on
                                             					 the CiscoUnifiedIPPhone models that require authentication will not
                                             					 function. Leave this field blank to accept the default setting. By default, this URL
                                             					 accesses a Cisco Unified Communications Self Care Portal window that was
                                             					 configured during installation. |
| Proxy
                                             					 Server | Enter the
                                             					 host and port (for example, proxy.cisco.com:80) that are used to proxy HTTP
                                             					 requests for access to non-local host addresses from the phones HTTP client. If the
                                             					 phone receives a URL such as www.cisco.com in a service and the phone is not
                                             					 configured in the cisco.com domain, the phone uses the proxy server to access
                                             					 the URL. If the phone is configured in the cisco.com domain, the phone accesses
                                             					 the URL without using the proxy because it is in the same domain as the URL. Leave this
                                             					 field blank to accept the default setting. |
| Idle | Enter the
                                             					 URL of the XML service that will appear as the idle display on the
                                             					 CiscoUnifiedIPPhone LCD screen when the Phone has not been used for the time
                                             					 that is specified in the Idle Timer field. For example, you can display a logo
                                             					 on the LCD screen when the phone has not been used for 5 minutes. Leave this
                                             					 field blank to use the default value. |
| Idle Timer | Enter the
                                             					 seconds that you want to elapse before the phone displays the URL that is
                                             					 specified in the Idle field. Leave this field blank to use the default value. |
| Secure
                                             					 Authentication URL | Enter the
                                             					 secure URL that the phone uses to validate requests that are made to the phone
                                             					 web server. Note If you
                                                         						do not provide a Secure Authentication URL, the device uses the nonsecure URL.
                                                         						If you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. By
                                             					 default, this URL accesses a Cisco Unified CM User Options window that was
                                             					 configured during installation. Leave this
                                             					 field blank to accept the default setting. Maximum
                                             					 length: 255 | Note | If you
                                                         						do not provide a Secure Authentication URL, the device uses the nonsecure URL.
                                                         						If you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Note | If you
                                                         						do not provide a Secure Authentication URL, the device uses the nonsecure URL.
                                                         						If you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Secure
                                             					 Directory URL | Enter the
                                             					 secure URL for the server from which the phone obtains directory information.
                                             					 This parameter specifies the URL that secured Cisco Unified IP Phones use when
                                             					 you press the Directory button. Note If you
                                                         						do not provide a Secure Directory URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. Leave this
                                             					 field blank to accept the default setting. Maximum
                                             					 length: 255 | Note | If you
                                                         						do not provide a Secure Directory URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Note | If you
                                                         						do not provide a Secure Directory URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Secure
                                             					 Idle URL | Enter the
                                             					 secure URL for the information that displays on the Cisco Unified IP Phone
                                             					 display when the phone is idle, as specified in Idle Timer field. For example,
                                             					 you can display a logo on the LCD when the phone has not been used for 5
                                             					 minutes. Note If you
                                                         						do not provide a Secure Idle URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. To accept
                                             					 the default setting, leave this field blank. Maximum
                                             					 length: 255 | Note | If you
                                                         						do not provide a Secure Idle URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Note | If you
                                                         						do not provide a Secure Idle URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Secure
                                             					 Information URL | Enter the
                                             					 secure URL for the server location where the Cisco Unified IP Phone can find
                                             					 help text information. This information displays when the user presses the
                                             					 information (i) button or the question mark (?) button. Note If you
                                                         						do not provide a Secure Information URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. To accept
                                             					 the default setting, leave this field blank. Maximum
                                             					 length: 255 | Note | If you
                                                         						do not provide a Secure Information URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Note | If you
                                                         						do not provide a Secure Information URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Secure
                                             					 Messages URL | Enter the
                                             					 secure URL for the messages server. The Cisco Unified IP Phone contacts this
                                             					 URL when the user presses the Messages button. Note If you
                                                         						do not provide a Secure Messages URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. To accept
                                             					 the default setting, leave this field blank. Maximum
                                             					 length: 255 | Note | If you
                                                         						do not provide a Secure Messages URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Note | If you
                                                         						do not provide a Secure Messages URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Secure
                                             					 Services URL | Enter the
                                             					 secure URL for Cisco Unified IP Phone services. The is the location that the
                                             					 secure Cisco Unified IP Phone contacts when the user presses the Services
                                             					 button. Note If you
                                                         						do not provide a Secure Services URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. To accept
                                             					 the default setting, leave this field blank. Maximum
                                             					 length: 255 | Note | If you
                                                         						do not provide a Secure Services URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Note | If you
                                                         						do not provide a Secure Services URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Extension Mobility (Device
                                                						Profile) Information |
| Enable
                                             					 Extension Mobility | Check this
                                             					 check box to enable the extension mobility feature. Extension mobility allows a
                                             					 user to log in and out of a CiscoIPPhone. |
| Log Out
                                             					 Profile | Choose the profile that a phone should load when an extension mobility user logs out. You must configure logout profiles in Unified Communications Manager Administration. Use
                                             					 Current Device Setting—This choice creates an autogenerated device profile as
                                             					 the default device profile. Select a
                                             					 User Device Profile—This choice assigns a user device profile, which has
                                             					 already been defined, that becomes the default device profile for this device. The chosen
                                             					 user device profile gets loaded onto the device when no user is logged in. |
| MultiLevel Precedence and
                                                						Preemption (MLPP) Information |
| MLPP
                                             					 Indication | If
                                             					 available, this setting specifies whether a device that is capable of playing
                                             					 precedence tones will use the capability when it places an MLPP precedence
                                             					 call. From the drop-down list, choose a setting to assign to this device from the following options: Default —This device inherits its MLPP indication setting from its device pool. Off —This device does not send indication of an MLPP precedence call. On —This device does send indication of an MLPP precedence call. Note Do not
                                                         						configure a device with the following combination of settings: MLPP Indication
                                                         						is set to Off while MLPP Preemption is set to Forceful. | Note | Do not
                                                         						configure a device with the following combination of settings: MLPP Indication
                                                         						is set to Off while MLPP Preemption is set to Forceful. |
| Note | Do not
                                                         						configure a device with the following combination of settings: MLPP Indication
                                                         						is set to Off while MLPP Preemption is set to Forceful. |
| MLPP
                                             					 Preemption | If
                                             					 available, this setting specifies whether a device that is capable of
                                             					 preempting calls in progress will use the capability when it places an MLPP
                                             					 precedence call. From the drop-down list, choose a setting to assign to this device from the following options: Default —This device inherits its MLPP preemption setting from its device pool. Disabled —This device does not preempt calls in progress when it places an MLPP precedence call. Forceful —This device preempts calls in progress when it places an MLPP precedence call. Note Do not
                                                         						configure a device with the following combination of settings: MLPP Indication
                                                         						is set to Off while MLPP Preemption is set to Forceful. | Note | Do not
                                                         						configure a device with the following combination of settings: MLPP Indication
                                                         						is set to Off while MLPP Preemption is set to Forceful. |
| Note | Do not
                                                         						configure a device with the following combination of settings: MLPP Indication
                                                         						is set to Off while MLPP Preemption is set to Forceful. |
| MLPP
                                             					 Domain (e.g., "0000FF" ) | Enter a
                                             					 hexadecimal value for the MLPP domain that is associated with this device.
                                             					 Ensure that this field is blank or a value between 0 and FFFFFF. |
| H.323
                                             					 Device Information |
| Signaling
                                             					 Port | The value
                                             					 designates the H.225 signaling port that this device uses. The
                                             					 default value specifies 1720. Valid values include 1 through 65535. |
| Retry
                                             					 Video Call as Audio | This check
                                             					 box applies only to video endpoints that receive a call. If this phone receives
                                             					 a call that does not connect as video, the call tries to connect as an audio
                                             					 call. By
                                             					 default, the system checks this check box to specify that the sending device
                                             					 should immediately retry a video call that does not connect as an audio call
                                             					 prior to sending the call to call control for rerouting. If you
                                             					 uncheck this check box, a video call that fails to connect as video fails to
                                             					 call control. At this point, call control reroutes the call within the route
                                             					 list. If Automatic Alternate Routing (AAR) is configured and enabled, call
                                             					 control also reroutes the call between route lists. |
| Wait for
                                             					 Far End H.245 Terminal Capability Set | By default, the system keeps this check box checked to specify that Unified Communications Manager should initiate capabilities exchange. This check box specifies that the Unified Communications Manager needs to receive the far-end H.245 Terminal Capability Set before it sends its H.245 Terminal Capability Set. |
| H.323
                                             					 Protocol Specific Information |
| SRTP
                                             					 Allowed | When this
                                             					 check box is checked, ensure that IPSec is configured in the network to provide
                                             					 end-to-end security. Failure to do so will expose keys and other information. |
| MTP
                                             					 Preferred Originating Codec | From the drop-down list, choose the codec to use if a media termination point is required for SIP calls. |
| Media
                                             					 Termination Point Required | Use this
                                             					 field to indicate whether a media termination point (MTP) is used to implement
                                             					 features that H.323 does not support (such as hold and transfer). Check the
                                             					 Media Termination Point Required check box if you want to use a media
                                             					 termination point to implement features. Uncheck the Media Termination Point
                                             					 Required check box if you do not want to use a media termination point to
                                             					 implement features. Use this
                                             					 check box only for H.323 clients and those H.323 devices that do not support
                                             					 the H.245 empty capabilities set or if you want media streaming to terminate
                                             					 through a single source. If you
                                             					 check this check box to require an MTP and this device becomes the endpoint of
                                             					 a video call, the call works as audio only. |
| H.323
                                                						Information |
| Outgoing
                                             					 Caller ID Pattern | For
                                             					 incoming calls to the phone, enter the pattern, from 0 to 24 digits, that you
                                             					 want to use for caller ID. |
| Calling
                                             					 Party Selection | Choose one
                                             					 of the following options to specify which directory number is sent: Originator —Send the directory number of the calling device. First Redirect Number- —Send the directory number of the redirecting device. Last Redirect Number —Send the directory number of the last device to redirect the call. First Redirect Number(external) —Send the directory number of the redirecting device. Last Redirect Number(external) —Send the directory number of the last device to redirect the call. |
| Calling
                                             					 Party Presentation | Choose
                                             					 whether the central office transmits or blocks caller ID: Choose Allowed if you want the central office to send caller ID. Choose Restricted if you do not want the central office to send caller ID. Default displays the caller ID unless the caller ID was restricted in a previous level in the call stream. |
| Display IE
                                             					 Delivery | Check the
                                             					 check box to deliver the display information element (IE) in SETUP and CONNECT
                                             					 messages for the calling and called party name delivery service. |
| Redirecting Number IE Delivery—Outbound | Check this check box to include the Redirecting Number IE in the outgoing SETUP message from the Unified Communications Manager to indicate the first redirecting number and the redirecting reason of the call when the call is forwarded. Uncheck
                                             					 the check box to exclude the first redirecting number and the redirecting
                                             					 reason from the outgoing SETUP message. Use
                                             					 Redirecting Number IE for voice-messaging integration only. If your configured
                                             					 voice-messaging system supports Redirecting Number IE, check the check box. |
| Redirecting Number IE delivery—Inbound | Use
                                             					 Redirecting Number IE when you are integrating a voice-messaging system that
                                             					 supports Redirecting Number IE. Check this check box to accept the Redirecting Number IE in the incoming SETUP message to the Unified Communications Manager . Uncheck the check box to exclude the Redirecting Number IE in the incoming SETUP message to the Unified Communications Manager . |
| Gatekeeper
                                                						Information |
| Gatekeeper
                                             					 Name | Choose the gatekeeper for the gatekeeper-controlled H.323 device from the drop-down list. Note If you
                                                         						do not choose the device, the system disables the E.164, Technology Prefix, and
                                                         						Zone fields. Note You
                                                         						cannot change the device to a gatekeeper-controlled phone if more than one
                                                         						directory number is configured for the device. | Note | If you
                                                         						do not choose the device, the system disables the E.164, Technology Prefix, and
                                                         						Zone fields. | Note | You
                                                         						cannot change the device to a gatekeeper-controlled phone if more than one
                                                         						directory number is configured for the device. |
| Note | If you
                                                         						do not choose the device, the system disables the E.164, Technology Prefix, and
                                                         						Zone fields. |
| Note | You
                                                         						cannot change the device to a gatekeeper-controlled phone if more than one
                                                         						directory number is configured for the device. |
| E.164 | Choose the
                                             					 E.164 address that is registered with the gatekeeper. Note Ensure
                                                         						the H.323 client is configured as a gatekeeper-controlled device. Note You must
                                                         						enter a value in this field for a gatekeeper-controlled H.323 client. You can
                                                         						enter only numbers (0-9) and special characters # and * in this field. | Note | Ensure
                                                         						the H.323 client is configured as a gatekeeper-controlled device. | Note | You must
                                                         						enter a value in this field for a gatekeeper-controlled H.323 client. You can
                                                         						enter only numbers (0-9) and special characters # and * in this field. |
| Note | Ensure
                                                         						the H.323 client is configured as a gatekeeper-controlled device. |
| Note | You must
                                                         						enter a value in this field for a gatekeeper-controlled H.323 client. You can
                                                         						enter only numbers (0-9) and special characters # and * in this field. |
| Technology
                                             					 Prefix | Enter the technology prefix to eliminate the need for entering the IP address for every Unified Communications Manager system when the gw-type-prefix command is configured. For example, you can enter 1#* in this field if you can use the following gw-type-prefix command on the gatekeeper: gw-type-prefix 1#* default-technology. Note You must
                                                         						enter a value in this field for a gatekeeper-controlled H.323 client. You can
                                                         						enter only numbers (0-9) and special characters # and * in this field. | Note | You must
                                                         						enter a value in this field for a gatekeeper-controlled H.323 client. You can
                                                         						enter only numbers (0-9) and special characters # and * in this field. |
| Note | You must
                                                         						enter a value in this field for a gatekeeper-controlled H.323 client. You can
                                                         						enter only numbers (0-9) and special characters # and * in this field. |
| Zone | On the gatekeeper, enter the specific zone with which Unified Communications Manager will register. The zone specifies the total bandwidth that is available for calls between this zone and another zone. Note You must
                                                         						enter a value in this field for a gatekeeper-controlled phone. You can enter
                                                         						only letters, numbers, spaces, dashes, dots, and underscores in this field. | Note | You must
                                                         						enter a value in this field for a gatekeeper-controlled phone. You can enter
                                                         						only letters, numbers, spaces, dashes, dots, and underscores in this field. |
| Note | You must
                                                         						enter a value in this field for a gatekeeper-controlled phone. You can enter
                                                         						only letters, numbers, spaces, dashes, dots, and underscores in this field. |
| Gatekeeper
                                             					 Controlled H.323 Client | Check this
                                             					 check box to configure the H.323 client gatekeeper as a controlled gatekeeper. |
| Do Not
                                             					 Disturb (DND) |
| Do Not
                                             					 Disturb | Check this
                                             					 check box if you want DND to be enabled. |
| DND Option | From the drop-down list, choose a DND option from the following options: None Ringer Off |
| DND
                                             					 Incoming Call Alert | From the drop-down list, choose one of the following options: None Disable Flash Only Beep Only |
| Secure Shell
                                                						Information |
| Secure
                                             					 Shell User | Enter a
                                             					 user ID for the secure shell user. If the phone that you are configuring does
                                             					 not support secure shell access, this field does not display. Cisco Technical
                                             					 Assistance Center (TAC) uses secure shell for troubleshooting. Contact TAC for
                                             					 further assistance. |
| Secure
                                             					 Shell Password | Enter the
                                             					 password for a secure shell user. If the phone you are configuring does not
                                             					 support secure shell access, this field does not display. Contact TAC for
                                             					 further assistance. |
| Product-Specific
                                                						Configuration |
| Model-specific configuration fields defined by the device
                                             					 manufacturers | The device
                                             					 manufacturer specifies the model-specific fields under product-specific
                                             					 configuration. Because they are dynamically configured, they can change without
                                             					 notice. To view
                                             					 field descriptions and help for product-specific configuration items, click the " ? " information
                                             					 icon to the right of the Product Specific Configuration heading to display
                                             					 help in a popup dialog box. If you
                                             					 need more information, refer to the documentation for the specific device that
                                             					 you are configuring or contact the manufacturer. |

| Note | This option is available only for phones that support activation codes. |
|---|---|

| Note | The
                                                         						Mobility User ID configuration gets used for the Cisco Unified Mobility and
                                                         						Mobile Voice Access features for dual-mode phones. |
|---|---|

| Note | The
                                                         						Owner User ID and Mobility User ID can differ. |
|---|---|

| Note | Any
                                                         						value that is entered in this field overrides the default value for the chosen
                                                         						model. |
|---|---|

| Note | Cisco dual-mode devices (Jabber) such as Android, iPhone, and iPad operating in WiFi mode are monitored through CTI and not
                                                         controlled. However, devices operating in GSM mode cannot be monitored or controlled. |
|---|---|

| Tip | For a detailed description of the secure-tone feature and the
                                                      					 configuration requirements, see the Cisco
                                                         						Unity Connection System Administration Guide . |
|---|---|

| Note | The time
                                                         						zone that you use for this remote destination is used by the time-of-day access
                                                         						feature to allow or block calls to this destination. |
|---|---|

| Note | You must
                                                         						check this check box for Cisco Unified Mobility to work with this remote
                                                         						destination. |
|---|---|

| Note | The time
                                                         						zone that you use for this remote destination is used by the time-of-day access
                                                         						feature to allow or block calls to this remote destination. |
|---|---|

| Note | You must
                                                         						check this check box for Cisco Unified Mobility to work with this remote
                                                         						destination. |
|---|---|

| Note | This
                                                         						option prompts you to specify a value for the Authentication Mode. |
|---|---|

| Note | Before
                                                         						you choose this option, verify that a certificate exists in the phone. If you
                                                         						choose this option and no certificate exists in the phone, the operation fails. |
|---|---|

| Note | Before
                                                         						you choose this option, verify that a certificate exists in the phone. If you
                                                         						choose this option and no certificate exists in the phone, the operation fails. |
|---|---|

| Note | When you
                                                         						add a phone based on the value in Key Order , RSA Key Size , and EC Key Size fields, the device security profile is
                                                         						associated with the phone. If you select the EC Only value with the EC Key Size value of 256 bits then the device
                                                         						security profile appends with EC-256 value. |
|---|---|

| Note | Some
                                                         						phone models may fail to register if the RSA key length selected for the CallManager Certificate Purpose is greater than 2048. From the
                                                         						Unified CM Phone Feature List Report on the Cisco Unified Reporting Tool
                                                         						(CURT), you can check the 3072/4096 RSA key size support feature for the list
                                                         						of supported phone models. |
|---|---|

| Note | If you
                                                         						do not provide a Secure Authentication URL, the device uses the nonsecure URL.
                                                         						If you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
|---|---|

| Note | If you
                                                         						do not provide a Secure Directory URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
|---|---|

| Note | If you
                                                         						do not provide a Secure Idle URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
|---|---|

| Note | If you
                                                         						do not provide a Secure Information URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
|---|---|

| Note | If you
                                                         						do not provide a Secure Messages URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
|---|---|

| Note | If you
                                                         						do not provide a Secure Services URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
|---|---|

| Note | Do not
                                                         						configure a device with the following combination of settings: MLPP Indication
                                                         						is set to Off while MLPP Preemption is set to Forceful. |
|---|---|

| Note | Do not
                                                         						configure a device with the following combination of settings: MLPP Indication
                                                         						is set to Off while MLPP Preemption is set to Forceful. |
|---|---|

| Note | If you
                                                         						do not choose the device, the system disables the E.164, Technology Prefix, and
                                                         						Zone fields. |
|---|---|

| Note | You
                                                         						cannot change the device to a gatekeeper-controlled phone if more than one
                                                         						directory number is configured for the device. |
|---|---|

| Note | Ensure
                                                         						the H.323 client is configured as a gatekeeper-controlled device. |
|---|---|

| Note | You must
                                                         						enter a value in this field for a gatekeeper-controlled H.323 client. You can
                                                         						enter only numbers (0-9) and special characters # and * in this field. |
|---|---|

| Note | You must
                                                         						enter a value in this field for a gatekeeper-controlled H.323 client. You can
                                                         						enter only numbers (0-9) and special characters # and * in this field. |
|---|---|

| Note | You must
                                                         						enter a value in this field for a gatekeeper-controlled phone. You can enter
                                                         						only letters, numbers, spaces, dashes, dots, and underscores in this field. |
|---|---|

| Field | Description |
|---|---|
| Directory Number Information |
| Line Template Name | Enter a unique name for the line template. Be aware that this field is available only when you are adding
                                             					 a line and not when you are updating an existing line. |
| Route Partition | Choose a route partition to which the directory number
                                             					 belongs. Note The directory number can appear in more than one partition. | Note | The directory number can appear in more than one partition. |
| Note | The directory number can appear in more than one partition. |
| Description | Enter description for the line template. The description can
                                             					 include up to 50 characters in any language, but it cannot include
                                             					 double-quotes ("), percentage sign ( % ), ampersand
                                             					 ('), or angle brackets (<>). |
| Alerting Name | This name represents the name that displays during an alert to
                                             					 a shared directory number. For non-shared directory numbers, during alerts, the
                                             					 system uses the name that is entered in the Display field. |
| Alerting Name ASCII | This field provides the same information as the Alerting Name
                                             					 field, but you must limit input to ASCII characters. Devices that do not
                                             					 support Unicode (internationalized) characters display the content of the Alerting Name ASCII field. |
| Active | Checking this check box allows calls to this DN to be forwarded (if forwarding is configured). If check box is not checked, Unified Communications Manager ignores the DN. |
| Directory Number Settings |
| Voice Mail Profile | Choose this parameter to make the pilot number the same as the
                                             					 directory number for this line. This action proves useful if you do not have a
                                             					 voice-messaging server that is configured for this phone. |
| Calling Search Space | Choose partitions that are searched for numbers that are
                                             					 called from this directory number. Note Changes cause an update of Pickup Group Names that are
                                                         						listed in the Call Pickup Group field. The setting
                                                         						applies to all devices that are using this directory number. | Note | Changes cause an update of Pickup Group Names that are
                                                         						listed in the Call Pickup Group field. The setting
                                                         						applies to all devices that are using this directory number. |
| Note | Changes cause an update of Pickup Group Names that are
                                                         						listed in the Call Pickup Group field. The setting
                                                         						applies to all devices that are using this directory number. |
| Presence Group | Used with the Presence feature, the directory number serves as
                                             					 the presence entity; that is, watchers request the status of the directory
                                             					 number, so the real-time status of the directory number displays on the device. If you want the phone to receive the status of the presence
                                             					 entity, make sure that the Presence group of the watcher is allowed to view the
                                             					 status of the Presence group that is applied to the directory number, as
                                             					 indicated in the Presence Group Configuration window. |
| User Hold MOH Audio Source | Choose the music on hold audio source to be played when the
                                             					 user presses HOLD to place a call on hold. |
| Network Hold MOH Audio Source | Choose the music on hold audio source to be played when the
                                             					 system places a call on hold while the user transfers a call or initiates a
                                             					 conference or call park. |
| Auto Answer | Choose one of the following options to activate the Auto
                                             					 Answer feature for this directory number: Auto Answer Off <Default> Auto Answer with Headset Auto Answer with Speakerphone Note Make sure that the headset or speakerphone is not disabled
                                                         						when you choose Auto Answer with headset or Auto Answer with speakerphone . Do not configure Auto Answer for devices that have shared
                                             					 lines. | Note | Make sure that the headset or speakerphone is not disabled
                                                         						when you choose Auto Answer with headset or Auto Answer with speakerphone . |
| Note | Make sure that the headset or speakerphone is not disabled
                                                         						when you choose Auto Answer with headset or Auto Answer with speakerphone . |
| AAR Settings —The settings in this row of
                                             					 fields specify treatment of calls for which insufficient bandwidth exists to
                                             					 reach the destination. Automated alternate routing (AAR) handles these calls
                                             					 that are routed to the AAR Destination Mask or Voice Mail. |
| AAR Voice Mail | Check this check box to use settings in the Voice Mail Profile
                                             					 Configuration window. Note When this check box is checked, Unified Communications Manager ignores the settings in the Coverage/Destination box and Calling Search Space. | Note | When this check box is checked, Unified Communications Manager ignores the settings in the Coverage/Destination box and Calling Search Space. |
| Note | When this check box is checked, Unified Communications Manager ignores the settings in the Coverage/Destination box and Calling Search Space. |
| AAR Destination Mask | Use this setting instead of the external phone number mask to
                                             					 determine the AAR Destination to be dialed. |
| AAR CSS | Choose the appropriate calling search space for the device to
                                             					 use when it performs automated alternate routing (AAR). The AAR calling search
                                             					 space specifies the collection of route partitions that are searched to
                                             					 determine how to route a collected (originating) number that is otherwise
                                             					 blocked due to insufficient bandwidth. |
| AAR Group | Choose the automated alternate routing (AAR) group for this
                                             					 device. The AAR group provides the prefix digits that are used to route calls
                                             					 that are otherwise blocked due to insufficient bandwidth. Set AAR Group to <None> to prevent rerouting blocked
                                             					 calls. |
| Retain this destination in the call forwarding history | Checking this check box allows the AAR leg of the call to be
                                             					 present in the Call History. |
| Visual Message Waiting Indicator Policy | Use this field to configure the handset lamp illumination
                                             					 policy. Choose one of the following options: Use System Policy (The directory number refers to the service parameter "Message Waiting Lamp Policy" setting.) Light and Prompt Prompt Only Light Only None Setting applies only to the current device unless you check
                                             					 the Update Shared Device Settings check box
                                             					 and click the Propagate Selected button. (The check box
                                             				  displays only if other devices share this directory number.) |
| Audible Message Waiting Indicator Policy | Use this field to configure an audible message waiting
                                             					 indicator policy. Choose one of the following options: Off On —When you select this option, you will receive a stutter dial tone when you take the handset off hook. Default —When you select this option, the phone uses the default that was set at the system level. |
| Call Pickup Group Audio Alert Setting (Phone Idle) | This field determines the type of notification an incoming
                                             					 call sends to members of a call pickup group. If the called phone does not
                                             					 answer, the phones in the call pickup group that are idle will either hear a
                                             					 short ring (ring once) or hear nothing (disabled). Use System Default —The value of this field gets determined by the setting of the Cisco CallManager service parameter Call Pickup Group Audio
                                                   Alert Setting of Idle Station. Disable —No alert is sent to members of the call pickup group. Ring Once —A short ring is sent to members of the call pickup group. |
| Call Pickup Group Audio Alert Setting (Phone Active) | This field determines the type of notification an incoming
                                             					 call sends to members of a call pickup group. If the called phone does not
                                             					 answer, the phones in the call pickup group that are busy will either hear a
                                             					 beep only or hear nothing (disabled). Use System Default —The value of this field gets determined by the setting of the Cisco CallManager service parameter Call Pickup Group Audio
                                                   Alert Setting of Busy Station. Disable —No alert is sent to member of the call pickup group. Beep Only —A beep is sent to members of the call pickup group. |
| Recording Option | This field determines the recording option on the line
                                             					 appearance of an agent. By default, the recording option specifies Call
                                             					 Recording Disabled. Choose one of the following options: Call Recording Disabled —The calls that the agent makes on this line appearance are not recorded. Automatic Call Recording Enabled —The calls that the agent makes on this line appearance are automatically recorded. Application Invoked Call Recording Enabled —The calls that the agent makes on this line appearance are recorded if an application invokes calling recording. When the recording option is set to either Automatic Call
                                             					 Recording Enabled or Application Invoked Call Recording Enabled, the line
                                             					 appearance can be associated with a recording profile. When automatic recording is enabled, the application's
                                             					 recording requests get rejected. |
| Recording Profile | This field determines the recording profile on the line
                                             					 appearance of an agent. |
| Monitoring Calling Search Space | The monitoring calling search space of the supervisor line
                                             					 appearance must include the agent line or device partition to allow monitoring
                                             					 the agent. Set the monitoring calling search space on the supervisor line
                                             					 appearance window. Choose an existing calling search space from the drop-down
                                             					 list box. The default value specifies None. |
| Call Forward and Pickup Settings |
| Forward All Voice Mail | Check this check box if you want calls to forward to the
                                             					 number that you chose in the voice-mail profile. Checking this check box makes the Forward All Destination field
                                             					 and Forward All Calling Search Space check box not
                                             					 relevant. |
| Forward All Destination | Enter the directory number or directory URI to which all calls are forwarded. Note The setting applies to any dialable phone number, including
                                                         						an outside destination unless restricted, and to all devices that are using
                                                         						this directory number. | Note | The setting applies to any dialable phone number, including
                                                         						an outside destination unless restricted, and to all devices that are using
                                                         						this directory number. |
| Note | The setting applies to any dialable phone number, including
                                                         						an outside destination unless restricted, and to all devices that are using
                                                         						this directory number. |
| Forward All Calling Search Space | Choose the calling search space to use when calls are
                                             					 forwarded to the specified destination. Note This setting applies to all devices that are using this
                                                         						directory number. | Note | This setting applies to all devices that are using this
                                                         						directory number. |
| Note | This setting applies to all devices that are using this
                                                         						directory number. |
| Secondary Calling Search Space for Forward All | Choose the secondary calling search space (CSS) from the
                                             					 drop-down list box. Because Call Forwarding is a line-based feature, in cases
                                             					 where the device calling search space is unknown, the system uses only the line
                                             					 calling search space to forward the call. If the line calling search space is
                                             					 restrictive and not routable, the forward attempt fails. Addition of a secondary calling search space for Call Forward All provides a solution to enable forwarding. The primary calling
                                             search space for Call Forward All and secondary calling search space for Call Forward All get concatenated (Primary CFA CSS + Secondary CFA CSS) when Call Forward All is processed. Unified Communications Manager uses this combination to validate the CFA destination and to forward the call. |
| Forward Busy Internal Voice Mail | Check this check box if you want calls from an internal number
                                             					 to be forwarded to a number that you chose in the voice-mail profile. Checking this check box makes the Forward Busy Internal
                                             					 Destination field and Calling Search Space check box not relevant. |
| Forward Busy Internal Destination | Enter the directory number or directory URI to which an internal call is
                                             					 forwarded when the line is in use. Note This setting applies to any internal, dialable phone number
                                                         						and to all devices that are using this directory number. | Note | This setting applies to any internal, dialable phone number
                                                         						and to all devices that are using this directory number. |
| Note | This setting applies to any internal, dialable phone number
                                                         						and to all devices that are using this directory number. |
| Forward Busy Internal Calling Search Space | Choose the calling search space to use when internal calls are
                                             					 forwarded to the specified destination. Note This setting applies to all devices that are using this
                                                         						directory number. | Note | This setting applies to all devices that are using this
                                                         						directory number. |
| Note | This setting applies to all devices that are using this
                                                         						directory number. |
| Forward Busy External Voice Mail | Check this check box if you want calls from an external number
                                             					 to be forwarded to a number that you chose in the voice-mail profile. Checking this check box makes the Forward Busy
                                                						External Destination field and Calling Search Space check box not
                                             					 relevant. |
| Forward Busy External Destination | Enter the directory number or directory URI to which an external call is
                                             					 forwarded when the line is in use. Note This setting applies to any dialable external phone number,
                                                         						including an outside destination unless restricted, and to all devices that are
                                                         						using this directory number. | Note | This setting applies to any dialable external phone number,
                                                         						including an outside destination unless restricted, and to all devices that are
                                                         						using this directory number. |
| Note | This setting applies to any dialable external phone number,
                                                         						including an outside destination unless restricted, and to all devices that are
                                                         						using this directory number. |
| Forward Busy External Calling Search Space | Choose the calling search space to use when external calls are
                                             					 forwarded to the specified destination. Note This setting applies to all devices that are using this
                                                         						directory number. | Note | This setting applies to all devices that are using this
                                                         						directory number. |
| Note | This setting applies to all devices that are using this
                                                         						directory number. |
| Forward No Answer Internal Voice Mail | Check this check box if you want calls from an internal number
                                             					 forwarded to the number that you chose in the voice-mail profile. Checking this check box makes the Forward No Answer Internal Destination field and Calling Search Space check box not
                                             					 relevant. |
| Forward No Answer Internal Destination | Enter a directory number or directory URI to which an internal call is
                                             					 forwarded when the phone is not answered. Note This setting applies to any internal, dialable phone number
                                                         						and to all devices that are using this directory number. | Note | This setting applies to any internal, dialable phone number
                                                         						and to all devices that are using this directory number. |
| Note | This setting applies to any internal, dialable phone number
                                                         						and to all devices that are using this directory number. |
| Forward No Answer Internal Calling Search Space | Choose the calling search space to use when internal calls are
                                             					 forwarding to the specified destination. The setting displays only if it is
                                             					 configured in the system. Note This setting applies to all devices that are using this
                                                         						directory number. | Note | This setting applies to all devices that are using this
                                                         						directory number. |
| Note | This setting applies to all devices that are using this
                                                         						directory number. |
| Forward No Answer External Voice Mail | Check this check box if you want calls to forward to an
                                             					 external number that you chose in the voice-mail profile. Checking this check box makes the Forward No Answer Externally Destination field and External Calling Search Space check box
                                             					 not relevant. |
| Forward No Answer External Destination | Enter a directory number or directory URI to which an external call is
                                             					 forwarded when the phone is not answered. Note This setting applies to any external, dialable phone number,
                                                         						including an outside destination unless restricted, and to all devices that are
                                                         						using this directory number. | Note | This setting applies to any external, dialable phone number,
                                                         						including an outside destination unless restricted, and to all devices that are
                                                         						using this directory number. |
| Note | This setting applies to any external, dialable phone number,
                                                         						including an outside destination unless restricted, and to all devices that are
                                                         						using this directory number. |
| Forward No Answer External Calling Search Space | Choose the calling search space to use when external calls are
                                             					 forwarded to the specified destination. The setting displays only if it is
                                             					 configured in the system. Note This setting applies to all devices that are using this
                                                         						directory number. | Note | This setting applies to all devices that are using this
                                                         						directory number. |
| Note | This setting applies to all devices that are using this
                                                         						directory number. |
| Forward No Coverage Internal Voice Mail | Check this check box if you want calls from an internal number
                                             					 forwarded to the number that you chose in the voice-mail profile. Checking this check box makes the Forward No Answer Destination field and Calling Search Space check box not
                                             					 relevant. |
| Forward No Coverage Internal Destination | Enter a directory number or directory URI to which an internal call is
                                             					 forwarded when the phone has no coverage. Note This setting applies to any internal, dialable phone number
                                                         						and to all devices that are using this directory number. | Note | This setting applies to any internal, dialable phone number
                                                         						and to all devices that are using this directory number. |
| Note | This setting applies to any internal, dialable phone number
                                                         						and to all devices that are using this directory number. |
| Forward No Coverage Internal Calling Search Space | Choose the calling search space to use when internal calls are
                                             					 forwarded to the specified destination. The setting displays only if it is
                                             					 configured in the system. Note This setting applies to all devices that are using this
                                                         						directory number. | Note | This setting applies to all devices that are using this
                                                         						directory number. |
| Note | This setting applies to all devices that are using this
                                                         						directory number. |
| Forward No Coverage External Voice Mail | Check this check box if you want calls from an external number
                                             					 to be forwarded to the number that you chose in the voice-mail profile. Checking this check box makes the Forward No Answer
                                                						Destination field and Calling Search Space check box not
                                             					 relevant. |
| Forward No Coverage External Destination | Enter a directory number or directory URI to which an external call is
                                             					 forwarded when the phone has no coverage. Note This setting applies to any dialable phone number, which
                                                         						includes an outside destination unless restricted, and to all devices that are
                                                         						using this directory number. | Note | This setting applies to any dialable phone number, which
                                                         						includes an outside destination unless restricted, and to all devices that are
                                                         						using this directory number. |
| Note | This setting applies to any dialable phone number, which
                                                         						includes an outside destination unless restricted, and to all devices that are
                                                         						using this directory number. |
| Forward No Coverage External Calling Search Space | Choose the calling search space to use when external calls are
                                             					 forwarded to the specified destination. The setting displays only if it is
                                             					 configured in the system. Note This setting applies to all devices that are using this
                                                         						directory number. | Note | This setting applies to all devices that are using this
                                                         						directory number. |
| Note | This setting applies to all devices that are using this
                                                         						directory number. |
| Forward on CTI Failure Voice Mail | The Forward on CTI Failure field applies
                                             					 only to CTI route points and CTI ports. The settings in this row specify the
                                             					 forwarding treatment for external calls to this CTI route point or CTI port if
                                             					 the CTI route point or CTI port fails. Check this check box to use settings in the Voice Mail Profile Configuration window. When this check box is checked, Unified Communications Manager ignores the settings in the Destination box and Calling Search Space. When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to forward to the voice-messaging system, you must uncheck
                                             the Voice Mail check box for external calls. |
| Forward on CTI Failure Destination | This setting specifies the directory number or directory URI to which an
                                             					 internal, nonconnected call is forwarded when an application that controls that
                                             					 directory number fails. Use any dialable phone number, including an outside
                                             					 destination. When you enter a destination value for internal calls, the
                                             					 system automatically copies this value to the Destination field for external calls. If
                                             					 you want external calls to forward to a different destination, you must enter a
                                             					 different value in the Destination field for external calls. |
| Forward on CTI Failure Calling Search Space | This setting applies to all devices that are using this
                                             					 directory number. When you choose a Calling Search Space for internal calls, the
                                             					 system automatically copies this setting to the Calling Search Space setting
                                             					 for external calls. If you want external calls to forward to a different
                                             					 calling search space, choose a different setting in the Calling Search Space
                                             					 for external calls. |
| No Answer Ring Duration | Enter the number of seconds to allow the call to ring before
                                             					 the system forwards the call to the Forward No Answer Destination. |
| Call Pickup Group | Choose a Pickup Group Name to specify the call pickup
                                             				  group, which can answer incoming calls to this directory number by dialing the
                                             				  appropriate pickup group number. |
| Park Monitoring |
| Park Monitoring Forward No Retrieve Destination External | When the parkee is an external party, then the call will be
                                             					 forwarded to the specified destination in the parker’s Park Monitoring Forward
                                             					 No Retrieve Destination External parameter. If the Park Monitoring Forward No Retrieve Destination External field value is empty, the parkee will be redirected to the parker’s line. |
| Park Monitoring Forward No Retrieve Destination Internal | When the parkee is an internal party, then the call will be
                                             					 forwarded to the specified destination in the parker’s Park Monitoring Forward
                                             					 No Retrieve Destination Internal parameter. If the Park Monitoring Forward No Retrieve Destination Internal field value is empty, the parkee will be redirected to the parker’s
                                             					 line. |
| Park Monitoring Reversion Timer | This parameter determines the number of seconds that Unified Communications Manager waits before prompting the user to retrieve a call that the user parked. This timer starts when the user presses the Park
                                             softkey on the phone, and a reminder is issued when the timer expires. Default: 60 seconds Note If you configure a non-zero value, this value overrides the
                                                         						value of this parameter set in the Service Parameters window. However, if
                                                         						you configure a value of 0 here, then the value in the Service Parameters window will be used. | Note | If you configure a non-zero value, this value overrides the
                                                         						value of this parameter set in the Service Parameters window. However, if
                                                         						you configure a value of 0 here, then the value in the Service Parameters window will be used. |
| Note | If you configure a non-zero value, this value overrides the
                                                         						value of this parameter set in the Service Parameters window. However, if
                                                         						you configure a value of 0 here, then the value in the Service Parameters window will be used. |
| Park Monitoring Forward No Retrieve Internal Voice Mail | Check this check box to use settings in the Voice Mail Profile Configuration window. Note When this check box is checked, Unified Communications Manager ignores the settings in the Destination box and Calling Search Space. | Note | When this check box is checked, Unified Communications Manager ignores the settings in the Destination box and Calling Search Space. |
| Note | When this check box is checked, Unified Communications Manager ignores the settings in the Destination box and Calling Search Space. |
| Park Monitoring Forward No Retrieve Destination External Voice Mail | Check this check box to use settings in the Voice Mail Profile Configuration window. Note When this check box is checked, Unified Communications Manager ignores the settings in the Destination box and Calling Search
                                                         Space. | Note | When this check box is checked, Unified Communications Manager ignores the settings in the Destination box and Calling Search
                                                         Space. |
| Note | When this check box is checked, Unified Communications Manager ignores the settings in the Destination box and Calling Search
                                                         Space. |
| Park Monitoring Forward No Retrieve External CSS | Choose the calling search space to apply to the directory
                                             					 number. |
| Park Monitoring Forward No Retrieve Internal CSS | Choose the calling search space to apply to the directory
                                             					 number. |
| Forward Unregistered Internal Voice Mail | This field applies to unregistered internal DN calls. The
                                             					 calls are rerouted to a specified Destination Number or Voice Mail. Check this check box if you want calls from an unregistered
                                             					 internal number to be forwarded to a number that you chose in the voice-mail
                                             					 profile. Checking this check box makes the Forward Unregistered Internal
                                                						Destination field and Calling Search Space drop-down list box
                                             					 not relevant. |
| Forward Unregistered Internal Destination | Enter the directory number to which an unregistered internal
                                             					 call is forwarded when the line is in use. This setting applies to any internal, dialable phone number
                                             					 and to all devices that are using this directory number. |
| Forward Unregistered Internal CSS | Choose the calling search space to use when unregistered
                                             					 internal calls are forwarded to the specified destination. This setting applies to all devices that are using this
                                             					 directory number. |
| Forward Unregistered External Voice Mail | This field applies to unregistered external DN calls. The
                                             					 calls are rerouted to a specified Destination Number or Voice Mail. Note You must also specify the maximum number of forwards in the Service Parameters Configuration window
                                                         						for a Directory Number. | Note | You must also specify the maximum number of forwards in the Service Parameters Configuration window
                                                         						for a Directory Number. |
| Note | You must also specify the maximum number of forwards in the Service Parameters Configuration window
                                                         						for a Directory Number. |
| Forward Unregistered External Destination | Enter the directory number to which an external call is
                                             					 forwarded when the line is in use. This setting applies to any dialable external phone number,
                                             					 including an outside destination unless restricted, and to all devices that are
                                             					 using this directory number. |
| Forward Unregistered External CSS | Choose the calling search space to use when external calls are
                                             					 forwarded to the specified destination. This setting applies to all devices that are using this
                                             					 directory number. |
| Multilevel Precedence and Preemption Alternate Party Settings |
| Target (Destination) | Enter the number to which MLPP precedence calls should be
                                             					 directed if this directory number receives a precedence call and neither this
                                             					 number nor its call forward destination answers the precedence call. Values can include numeric characters, pound
                                             					 ( # ), and asterisk ( * ). |
| MLPP Calling Search Space | From the drop-down list box, choose the calling search space
                                             					 to associate with the alternate party target (destination) number. |
| MLPP No Answer Ring Duration (Seconds) | Enter the number of seconds (between 4 and 30) after which an
                                             					 MLPP precedence call will get directed to the alternate party of this directory
                                             					 number if this directory number and its call forwarding destination have not
                                             					 answered the precedence call. Leave this setting blank to use the value that is set in the Unified Communications Manager enterprise parameter, Precedence Alternate Party Timeout. |
| Line Settings for This Phone |
| Display (Internal Caller ID) | Use this field only if you do not want the directory number to
                                             					 show on the line appearance. Enter text that identifies this directory number
                                             					 for a line/phone combination. Suggested entries include name of the boss, department, or
                                             					 other appropriate information to identify multiple directory numbers to
                                             					 secretary/assistant who monitors multiple directory numbers. |
| ASCII Display (Internal Caller ID) | This field provides the same information as the Display (Internal Caller ID) field, but
                                             					 you must limit input to ASCII characters. Devices that do not support Unicode
                                             					 (internationalized) characters display the content of the ASCII Display (Internal Caller ID) field. Setting applies only to the current device unless you check
                                             					 the check box at right (Update Shared Device Settings) and click the Propagate Selected button. (The check
                                             					 box at right displays only if other devices share this directory number.) |
| Line Text Label | Enter text that identifies this directory number for a
                                             					 line/phone combination. Note The default language specifies English | Note | The default language specifies English |
| Note | The default language specifies English |
| External Phone Number Mask | Enter the phone number (or mask) that is sent for Caller ID
                                             					 information when a call is placed from this line. You can enter a maximum of 24 numbers and "X" characters. The Xs represent the directory number and
                                             					 must appear at the end of the pattern. For example, if you specify a mask of
                                             					 972813XXXX, an external call from extension 1234 displays a caller ID number of
                                             					 9728131234. |
| Visual Message Waiting Indicator Policy | Use this field to configure the handset lamp illumination
                                             					 policy. Choose one of the following options: Use System Policy (The directory number refers to the service parameter "Message Waiting Lamp Policy" setting.) Light and Prompt Prompt Only Light Only None Setting applies only to the current device unless you check
                                             					 the Update Shared Device Settings check box
                                             					 and click the Propagate Selected button. (The check box
                                             					 displays only if other devices share this directory number.) |
| Audible Message Waiting Indicator Policy | Use this field to configure an audible message waiting
                                             					 indicator policy. Choose one of the following options: Off On —When you select this option, you will receive a stutter dial tone when you take the handset off hook. Default —When you select this option, the phone uses the default that was set at the system level. |
| Ring Setting (Phone Idle) | Choose the ring setting for the line appearance when an
                                             					 incoming call is received and no other active calls exist on that device.
                                             					 Choose one of the following options: Use system default Disable Flash only Ring once Ring |
| Ring Setting (Phone Active) | Choose the ring setting that is used when this phone has
                                             					 another active call on a different line. Choose one of the following options: Use system default Disable Flash only Ring once Ring Beep only |
| Call Pickup Group Audio Alert Setting (Phone Idle) | This field determines the type of notification an incoming
                                             					 call sends to members of a call pickup group. If the called phone does not
                                             					 answer, the phones in the call pickup group that are idle will either hear a
                                             					 short ring (ring once) or hear nothing (disabled). Use System Default —The value of this field gets determined by the setting of the Cisco CallManager service parameter Call Pickup Group Audio
                                                   Alert Setting of Idle Station. Disable —No alert is sent to members of the call pickup group. Ring Once —A short ring is sent to members of the call pickup group. |
| Call Pickup Group Audio Alert Setting (Phone Active) | This field determines the type of notification an incoming
                                             					 call sends to members of a call pickup group. If the called phone does not
                                             					 answer, the phones in the call pickup group that are busy will either hear a
                                             					 beep only or hear nothing (disabled). Use System Default —The value of this field gets determined by the setting of the Cisco CallManager service parameter Call Pickup Group Audio
                                                   Alert Setting of Busy Station. Disable —No alert is sent to member of the call pickup group. Beep Only —A beepis sent to members of the call pickup group. |
| Recording Option | This field determines the recording option on the line
                                             					 appearance of an agent. By default, the recording option specifies Call
                                             					 Recording Disabled. Choose one of the following options: Call Recording Disabled —The calls that the agent makes on this line appearance are not recorded. Automatic Call Recording Enabled —The calls that the agent makes on this line appearance are automatically recorded. Application Invoked Call Recording Enabled —The calls that the agent makes on this line appearance are recorded if an application invokes calling recording. When the recording option is set to either Automatic Call
                                             					 Recording Enabled or Application Invoked Call Recording Enabled, the line
                                             					 appearance can be associated with a recording profile. When automatic recording is enabled, the application’s
                                             					 recording requests get rejected. |
| Recording Profile | This field determines the recording profile on the line
                                             					 appearance of an agent. Choose an existing recording profile from the drop-down
                                             					 list box. To create a recording profile, use the Device > Device
                                                   						  Settings > Recording Profile menu
                                             					 option. The default value specifies None. |
| Monitoring Calling Search Space | The monitoring calling search space of the supervisor line
                                             					 appearance must include the agent line or device partition to allow monitoring
                                             					 the agent. Set the monitoring calling search space on the supervisor line
                                             					 appearance window. Choose an existing calling search space from the drop-down
                                             					 list box. The default value specifies None. |
| Log Missed Calls | This check box allows you to turn this feature on or off. If the check box displays as checked (turned on), which is the default
                                             for this setting, Unified Communications Manager logs missed calls in the call history for that directory number on the phone. |
| Forward All CSS Activation Policy | Select one of the following options from the drop-down list
                                             					 box: Use System Default With Configured CSS With Activating Device/Line CSS If you select the With Configured CSS option, the Forward All
                                             					 Calling Search Space that is explicitly configured in the Directory Number Configuration window
                                             					 controls the forward all activation and call forwarding. If the Forward All
                                             					 Calling Search Space is set to None, no CSS gets configured for Forward All. A
                                             					 forward all activation attempt to any directory number with a partition will
                                             					 fail. No change in the Forward All Calling Search Space and Secondary Calling
                                             					 Search Space for Forward All occurs during the forward all activation. If you prefer to utilize the combination of the Directory
                                             					 Number Calling Search Space and Device Calling Search Space without explicitly
                                             					 configuring a Forward All Calling Search Space, select With Activating
                                             					 Device/Line CSS for the Calling Search Space Activation Policy. With this
                                             					 option, when Forward All is activated from the phone, the Forward All Calling
                                             					 Search Space and Secondary Calling Search Space for Forward All automatically
                                             					 gets populated with the Directory Number Calling Search Space and Device
                                             					 Calling Search Space for the activating device. |
| Hold Reversion Ring Duration (seconds) | Enter a number from 0 to 1200 (inclusive) to specify the wait
                                             					 time in seconds before issuing a reverted call alert to the holding party
                                             					 phone. If you enter a value of 0, Unified Communications Manager does not invoke the reverted call feature for a held call. |
| Hold Reversion Notification Interval (seconds) | Enter a number from 0 to 1200 (inclusive) to specify the
                                             					 interval time in seconds for sending periodic reminder alerts to the holding
                                             					 party phone. If you enter a value of 0, Unified Communications Manager does not send reminder alerts. |
| Party Entrance Tone | Choose one of the following options from the drop-down list
                                             					 box: Default —Use the value that you configured in the Party Entrance Tone service parameter. On —A tone plays on the phone when a basic call changes to a multi party call; that is, a barge call, cBarge call, ad hoc conference,
                                                   meet-me conference, or a joined call. In addition, a different tone plays when a party leaves the multi party call. If the
                                                   controlling device, that is, the originator of the multi party call has a built-in bridge, the tone gets played to all parties
                                                   if you choose On for the controlling device. When the controlling device, for example, the conference controller, no longer
                                                   remains present on the call or if the controlling device cannot play the tone, Unified Communications Manager does not play the tone even if you choose On. Off —A tone does not play on the phone when a basic call changes to a multi party call. |
| Multiple Call/Call Waiting Settings |
| Maximum Number of Calls | You can configure up to 184 calls for a line on a device in a
                                             					 cluster, with the limiting factor being the device. As you configure the number
                                             					 of calls for one line, the calls that are available for another line decrease. The default specifies 4. If the phone does not allow multiple
                                             					 calls for each line, the default specifies 2. For CTI route points, you can configure up to 10,000 calls for
                                             					 each port. The default specifies 5000 calls. Use this field in conjunction with the Busy Trigger field. |
| Busy Trigger | This setting, which works in conjunction with Maximum Number
                                             					 of Calls and Call Forward Busy, determines the maximum number of calls to be
                                             					 presented at the line. If maximum number of calls is set for 50 and the busy
                                             					 trigger is set to 40, incoming call 41 gets rejected with a busy cause (and
                                             					 will get forwarded if Call Forward Busy is set). If this line is shared, be
                                             					 aware that all the lines must be busy before incoming calls get rejected. Use this field in conjunction with Maximum Number of Calls for
                                             					 CTI route points. The default specifies 4500 calls. |
| Forwarded Call Information Display for This
                                                						Device |
| Caller Name | Check this check box to include the caller name in the display
                                             					 when a forwarded call is received. Default leaves this check box checked. |
| Caller Number | Check this check box to include the caller number in the
                                             					 display when a forwarded call is received. |
| Redirected Number | Check this check box to include the redirected number in the
                                             					 display when a forwarded call is received. |
| Dialed Number | Check this check box to include the dialed number in the
                                             					 display when a forwarded call is received. The default setting leaves this
                                             					 check box checked. |
| Directory URI Fields |
| URI (1-5) on Directory Number | Enter a directory URI to associate with the directory number for this phone. Follow the username@host format. Enter a username
                                             of up to 47 alphanumeric characters. For the host address, enter an IPv4 address or fully qualified domain name. You can associate
                                             up to five directory URIs to a single directory number. Note Within Cisco Unified CM Administration, you can enter directory URIs with embedded double quotes or commas. However, when
                                                      you use Bulk Administration to import a csv file that contains directory URIs with embedded double quotes and commas, you
                                                      must use enclose the entire directory URI in double quotes and escape the embedded double quotes with a double quote. For
                                                      example, the Jared, "Jerry",Smith@test.com directory URI must be input as "Jared,""Jerry"",Smith@test.com" in the csv file. | Note | Within Cisco Unified CM Administration, you can enter directory URIs with embedded double quotes or commas. However, when
                                                      you use Bulk Administration to import a csv file that contains directory URIs with embedded double quotes and commas, you
                                                      must use enclose the entire directory URI in double quotes and escape the embedded double quotes with a double quote. For
                                                      example, the Jared, "Jerry",Smith@test.com directory URI must be input as "Jared,""Jerry"",Smith@test.com" in the csv file. |
| Note | Within Cisco Unified CM Administration, you can enter directory URIs with embedded double quotes or commas. However, when
                                                      you use Bulk Administration to import a csv file that contains directory URIs with embedded double quotes and commas, you
                                                      must use enclose the entire directory URI in double quotes and escape the embedded double quotes with a double quote. For
                                                      example, the Jared, "Jerry",Smith@test.com directory URI must be input as "Jared,""Jerry"",Smith@test.com" in the csv file. |
| URI (1-5) Route Partition on Directory Number | Enter the partition on which the directory URI belongs. If you do not want to restrict access to the directory URI, leave
                                             the field blank. |
| URI (1-5) Is Primary on Directory Number | Enter a ' t ' (True) to indicate that this directory URI is the primary directory URI for this extension. Otherwise, enter an ' f' (False) to indicate that this is not the primary directory URI for this extension. Note You can associate up to five directory URIs to a single directory number, but you must select a single primary directory
                                                         URI. | Note | You can associate up to five directory URIs to a single directory number, but you must select a single primary directory
                                                         URI. |
| Note | You can associate up to five directory URIs to a single directory number, but you must select a single primary directory
                                                         URI. |

| Note | The directory number can appear in more than one partition. |
|---|---|

| Note | Changes cause an update of Pickup Group Names that are
                                                         						listed in the Call Pickup Group field. The setting
                                                         						applies to all devices that are using this directory number. |
|---|---|

| Note | Make sure that the headset or speakerphone is not disabled
                                                         						when you choose Auto Answer with headset or Auto Answer with speakerphone . |
|---|---|

| Note | When this check box is checked, Unified Communications Manager ignores the settings in the Coverage/Destination box and Calling Search Space. |
|---|---|

| Note | The setting applies to any dialable phone number, including
                                                         						an outside destination unless restricted, and to all devices that are using
                                                         						this directory number. |
|---|---|

| Note | This setting applies to all devices that are using this
                                                         						directory number. |
|---|---|

| Note | This setting applies to any internal, dialable phone number
                                                         						and to all devices that are using this directory number. |
|---|---|

| Note | This setting applies to all devices that are using this
                                                         						directory number. |
|---|---|

| Note | This setting applies to any dialable external phone number,
                                                         						including an outside destination unless restricted, and to all devices that are
                                                         						using this directory number. |
|---|---|

| Note | This setting applies to all devices that are using this
                                                         						directory number. |
|---|---|

| Note | This setting applies to any internal, dialable phone number
                                                         						and to all devices that are using this directory number. |
|---|---|

| Note | This setting applies to all devices that are using this
                                                         						directory number. |
|---|---|

| Note | This setting applies to any external, dialable phone number,
                                                         						including an outside destination unless restricted, and to all devices that are
                                                         						using this directory number. |
|---|---|

| Note | This setting applies to all devices that are using this
                                                         						directory number. |
|---|---|

| Note | This setting applies to any internal, dialable phone number
                                                         						and to all devices that are using this directory number. |
|---|---|

| Note | This setting applies to all devices that are using this
                                                         						directory number. |
|---|---|

| Note | This setting applies to any dialable phone number, which
                                                         						includes an outside destination unless restricted, and to all devices that are
                                                         						using this directory number. |
|---|---|

| Note | This setting applies to all devices that are using this
                                                         						directory number. |
|---|---|

| Note | If you configure a non-zero value, this value overrides the
                                                         						value of this parameter set in the Service Parameters window. However, if
                                                         						you configure a value of 0 here, then the value in the Service Parameters window will be used. |
|---|---|

| Note | When this check box is checked, Unified Communications Manager ignores the settings in the Destination box and Calling Search Space. |
|---|---|

| Note | When this check box is checked, Unified Communications Manager ignores the settings in the Destination box and Calling Search
                                                         Space. |
|---|---|

| Note | You must also specify the maximum number of forwards in the Service Parameters Configuration window
                                                         						for a Directory Number. |
|---|---|

| Note | The default language specifies English |
|---|---|

| Note | Within Cisco Unified CM Administration, you can enter directory URIs with embedded double quotes or commas. However, when
                                                      you use Bulk Administration to import a csv file that contains directory URIs with embedded double quotes and commas, you
                                                      must use enclose the entire directory URI in double quotes and escape the embedded double quotes with a double quote. For
                                                      example, the Jared, "Jerry",Smith@test.com directory URI must be input as "Jared,""Jerry"",Smith@test.com" in the csv file. |
|---|---|

| Note | You can associate up to five directory URIs to a single directory number, but you must select a single primary directory
                                                         URI. |
|---|---|

| Field | Description |
|---|---|
| Intercom Directory Number Information |
| Intercom Template Name | Enter a unique name for the intercom template. |
| Route Partition | Choose a route partition to which the directory number
                                             					 belongs. Note The directory number can appear in more than one partition. | Note | The directory number can appear in more than one partition. |
| Note | The directory number can appear in more than one partition. |
| Description | Enter a description of the directory number and route
                                             					 partition. The description can include up to 50 characters in any language, but
                                             					 it cannot include double-quotes (""), percentage sign
                                             					 ( % ), ampersand ('), or angle brackets
                                             					 (<>). |
| Display (Internal Caller ID) | Use this field only if you do not want the directory number to
                                             					 show on the line appearance. Enter text that identifies this directory number
                                             					 for a line/phone combination. Suggested entries include name of the boss, department, or
                                             					 other appropriate information to identify multiple directory numbers to a
                                             					 secretary or assistant who monitors multiple directory numbers. |
| ASCII Display (Internal Caller ID) | This field provides the same information as the Display (Internal Caller ID) field, but
                                             					 you must limit input to ASCII characters. Devices that do not support Unicode
                                             					 (internationalized) characters display the content of the ASCII Display (Internal Caller ID) field. Setting applies only to the current device unless you check
                                             					 the check box at right (Update Shared Device Settings) and click the Propagate Selected button. (The check box at right displays only if
                                             					 other devices share this directory number.) |
| Line Text Label | Enter text that identifies this directory number for a
                                             					 line/phone combination. Note The default language specifies English | Note | The default language specifies English |
| Note | The default language specifies English |
| Alerting Name | This name represents the name that displays during an alert to
                                             					 a shared directory number. For non-shared directory numbers, during alerts, the
                                             					 system uses the name that is entered in the Display field. |
| Alerting Name ASCII | This field provides the same information as the Alerting Name
                                             					 field, but you must limit input to ASCII characters. Devices that do not
                                             					 support Unicode (internationalized) characters display the content of the Alerting Name ASCII field. |
| Speed Dial | Enter the number that you want the system to dial when the
                                             					 user presses the speed-dial button. You can enter digits 0 through 9, * , # , and + , which is the international escape
                                             					 character. |
| External Phone Number Mask | Enter the phone number (or mask) that is sent for Caller ID
                                             					 information when a call is placed from this line. You can enter a maximum of 24 numbers and "X" characters. The Xs represent the directory number and
                                             					 must appear at the end of the pattern. For example, if you specify a mask of
                                             					 972813XXXX, an external call from extension 1234 displays a caller ID number of
                                             					 9728131234. |
| Intercom Directory Number Settings |
| Calling Search Space | From the drop-down list box, choose the appropriate calling
                                             					 search space. A calling search space comprises a collection of partitions that
                                             					 are searched for numbers that are called from this directory number. The value
                                             					 that you choose applies to all devices that are using this directory number. |
| Presence Group | Configure this field with the presence feature. From the drop-down list box, choose a Presence Group for this
                                             					 directory number. The selected group specifies the devices, end users, and
                                             					 application users that can monitor this directory number. |
| Auto Answer | Choose one of the following options to activate the auto
                                             					 answer feature for this directory number: Auto
                                                   					 Answer Off <Default> Auto Answer
                                                   					 with Headset Auto Answer
                                                   					 with Speakerphone Note Do not configure auto answer for devices that have shared
                                                         						lines. | Note | Do not configure auto answer for devices that have shared
                                                         						lines. |
| Note | Do not configure auto answer for devices that have shared
                                                         						lines. |
| Default Activated Device | From the drop-down list box, choose a default activated device
                                             					 for this directory number. The selected device specifies the phone on which
                                             					 this directory number is activated by default. The drop-down list box lists
                                             					 only devices that support intercom. Note You must specify a default activated device for this
                                                         						intercom directory number to be active as an intercom line. Note If an intercom DN is specified in a device profile that is
                                                         						configured for Cisco Extension Mobility, that intercom DN will display as an
                                                         						intercom line only when a user logs in to the specified default activated
                                                         						device by using that device profile, as long as the device supports the
                                                         						intercom feature. | Note | You must specify a default activated device for this
                                                         						intercom directory number to be active as an intercom line. | Note | If an intercom DN is specified in a device profile that is
                                                         						configured for Cisco Extension Mobility, that intercom DN will display as an
                                                         						intercom line only when a user logs in to the specified default activated
                                                         						device by using that device profile, as long as the device supports the
                                                         						intercom feature. |
| Note | You must specify a default activated device for this
                                                         						intercom directory number to be active as an intercom line. |
| Note | If an intercom DN is specified in a device profile that is
                                                         						configured for Cisco Extension Mobility, that intercom DN will display as an
                                                         						intercom line only when a user logs in to the specified default activated
                                                         						device by using that device profile, as long as the device supports the
                                                         						intercom feature. |

| Note | The directory number can appear in more than one partition. |
|---|---|

| Note | The default language specifies English |
|---|---|

| Note | Do not configure auto answer for devices that have shared
                                                         						lines. |
|---|---|

| Note | You must specify a default activated device for this
                                                         						intercom directory number to be active as an intercom line. |
|---|---|

| Note | If an intercom DN is specified in a device profile that is
                                                         						configured for Cisco Extension Mobility, that intercom DN will display as an
                                                         						intercom line only when a user logs in to the specified default activated
                                                         						device by using that device profile, as long as the device supports the
                                                         						intercom feature. |
|---|---|

| Note | If you enter a comma in one of the fields, BAT.xlt encloses that
                                             			 field entry in double quotes when you export to BAT format. If you enter a blank row in the BAT spreadsheet, the system treats
                                             			 the empty row as the end of the file and does not convert data that is entered
                                             			 after a blank line to the BAT format. |
|---|---|

| Attention | The number of lines and speed dials that you define for phones in
                                             			 the BAT spreadsheet must not exceed the numbers that are defined in the BAT
                                             			 phone template, otherwise, an error occurs when you attempt to insert the CSV
                                             			 data file and BAT template. |
|---|---|

| Note | You cannot upload a CSV filename that contains a comma (for example, abcd,e.txt) to the server. |
|---|---|

| Step 1 | To open the BAT spreadsheet, locate and double-click the BAT.xlt
                                          			 file |
|---|---|
| Step 2 | When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities. |
| Step 3 | To display the phones options, click the Phones tab at the bottom of the spreadsheet. |
| Step 4 | Choose the radio button for one of the following device types: The device type that you select determines the validation criteria
                                             				for data in the BAT spreadsheet. Phones CTI Port H.323 Client VGC Phones VGC Virtual Phones Cisco IP Communicator Phone The spreadsheet displays options that are available for the
                                          			 chosen device. For example, when you choose phones, fields for the number of
                                          			 phone lines and the number of speed dials display. |
| Step 5 | Choose the device and line fields to appear in the BAT spreadsheet
                                          			 for each phone. Do the following: Click Create File Format . To choose the device fields, click a device field name in
                                                				  the Device Field box and then click the arrow to move
                                                				  the field to the Selected Device Fields box. A CSV data file must include MAC Address/Device Name and Description ; therefore, these fields
                                                   					 always remain selected. Tip To select a range of items in the list, hold down the Shift key. To select random field
                                                               						names, hold down the Ctrl key and click field names. Click a line field name in the Line Field box and click the arrow to move
                                                				  the field to the Selected Line Fields box. Tip To change the order of the items in the Selected Line and Device boxes, choose an item and use
                                                               						the up and down arrows to move the field up or down in the list. A message asks whether you want to overwrite the existing CSV
                                                				  format. Click Create to modify the CSV data file format. Click OK . New columns for the selected fields display in the BAT
                                                				  spreadsheet in the order that you specified. | Tip | To select a range of items in the list, hold down the Shift key. To select random field
                                                               						names, hold down the Ctrl key and click field names. | Tip | To change the order of the items in the Selected Line and Device boxes, choose an item and use
                                                               						the up and down arrows to move the field up or down in the list. |
| Tip | To select a range of items in the list, hold down the Shift key. To select random field
                                                               						names, hold down the Ctrl key and click field names. |
| Tip | To change the order of the items in the Selected Line and Device boxes, choose an item and use
                                                               						the up and down arrows to move the field up or down in the list. |
| Step 6 | Scroll to the right to locate the Number of Phone Lines box and enter the number
                                          			 of lines for the phone. Note The number of lines you enter must not exceed the number of lines that are configured in the BAT template. | Note | The number of lines you enter must not exceed the number of lines that are configured in the BAT template. |
| Note | The number of lines you enter must not exceed the number of lines that are configured in the BAT template. |
| Step 7 | For phones, you must enter the number of speed-dial buttons in the Maximum Number of Speed Dials box. Note The number of speed dials you enter must not exceed the number of speed dials that are configured in the BAT template. After you enter the number, columns display for each
                                          			 speed-dial number. | Note | The number of speed dials you enter must not exceed the number of speed dials that are configured in the BAT template. |
| Note | The number of speed dials you enter must not exceed the number of speed dials that are configured in the BAT template. |
| Step 8 | Enter the number of Busy Lamp Field (BLF) speed-dial buttons in
                                          			 the Maximum Number of BLF Speed Dials box. After you enter the number, columns display for each BLF
                                          			 speed-dial number. |
| Step 9 | Enter data for an individual phone on each line in the
                                          			 spreadsheet. Complete all mandatory fields and any relevant, optional fields. Each column heading specifies the length of the field and
                                             whether it is required or optional. See online help for phone field descriptions. |
| Step 10 | If you did not enter the MAC address for each phone, check the Create Dummy MAC Address check box. Attention Do not use the dummy MAC address option for H.323 clients, VGC
                                                         				  phones, or VGC virtual phones. | Attention | Do not use the dummy MAC address option for H.323 clients, VGC
                                                         				  phones, or VGC virtual phones. |
| Attention | Do not use the dummy MAC address option for H.323 clients, VGC
                                                         				  phones, or VGC virtual phones. |
| Step 11 | To transfer the data from the BAT Excel spreadsheet into a CSV
                                          			 formatted data file, click Export to BAT Format . Tip For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 phones window in BAT. The system saves the file with the default filename: <tabname>-<timestamp>.txt to your choice of a folder on your local workstation. | Tip | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 phones window in BAT. |
| Tip | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 phones window in BAT. |

| Tip | To select a range of items in the list, hold down the Shift key. To select random field
                                                               						names, hold down the Ctrl key and click field names. |
|---|---|

| Tip | To change the order of the items in the Selected Line and Device boxes, choose an item and use
                                                               						the up and down arrows to move the field up or down in the list. |
|---|---|

| Note | The number of lines you enter must not exceed the number of lines that are configured in the BAT template. |
|---|---|

| Note | The number of speed dials you enter must not exceed the number of speed dials that are configured in the BAT template. |
|---|---|

| Attention | Do not use the dummy MAC address option for H.323 clients, VGC
                                                         				  phones, or VGC virtual phones. |
|---|---|

| Tip | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 phones window in BAT. |
|---|---|

| Field | Description |
|---|---|
| Device Fields |
| MAC
                                             					 Address/Device Name | Enter the
                                             					 MAC address for phones, VGC virtual phones, and VGC phones. Enter a unique
                                             					 identifier (Device Name) for the CTI port or H.323 client. You can check the Create Dummy MAC Addresses check box to
                                             					 automatically generate unique device identifiers. |
| Description | Enter a
                                             					 description such as "Conference
                                                						Room A" or "John
                                                						Smith" that identifies the phone or device. The description can include up
                                             					 to 50 characters in any language, but it cannot include double-quotes ( " ), percentage sign
                                             					 ( % ),
                                             					 ampersand (&), back-slash ( \ ), or angle brackets (<>). |
| Media
                                             					 Resource Group List | Enter the
                                             					 media resource group list (MRGL) for this group of phones/ports. An MRGL
                                             					 specifies a list of prioritized media resource groups. An application can
                                             					 choose required media resources from the available ones according to the order
                                             					 that is defined in the MRGL. |
| User Hold
                                             					 Audio Source | Enter the
                                             					 user hold audio source that this group of IP phones or CTI ports should use. The user
                                             					 hold audio source identifies the audio source from which music is played when a
                                             					 user places a call on hold. |
| Network Hold
                                             					 MOH Audio Source | Enter the
                                             					 network hold audio source that this group of IP phones or CTI ports should use. The network
                                             					 hold audio source identifies the audio source from which music is played when
                                             					 the system places a call on hold, such as when the user transfers or parks a
                                             					 call. |
| User Locale | Enter the
                                             					 country and language set that you want to associate with this group of IP
                                             					 phones. This choice determines which cultural-dependent attributes exist for this user and which language displays for the user in
                                             the Unified Communications Manager user windows and phones. |
| Network
                                             					 Locale | Enter the
                                             					 network locale that you want to associate with this group of phones. The Network
                                             					 Locale comprises a set of tones and cadences that Cisco gateways and phones use
                                             					 when they communicate with the PSTN and other networks in a specific
                                             					 geographical area. |
| Softkey
                                             					 Template | Enter the
                                             					 softkey template to be used for all phones in this group. |
| Common Phone
                                             					 Profile | From the
                                             					 drop-down list box, choose a common phone profile from the list of available
                                             					 common phone profiles. |
| Device
                                             					 Presence Group | Used with
                                             					 the Presence feature, the phone that is running SIP or SCCP serves as a watcher
                                             					 because it requests status about the presence entity; for example, directory
                                             					 number, that is configured as a BLF speed dial button on the phone. If you want
                                             					 the phone to receive the status of the presence entity, choose a Presence Group
                                             					 that is allowed to view the status of the Presence Group that is applied to the
                                             					 directory number, as indicated in the Presence Group Configuration window. |
| Phone Load
                                             					 Name | Enter the
                                             					 custom phone load, if applicable. Note Any value
                                                         						that is entered in this field overrides the default value for the chosen phone. Value does
                                             					 not apply for CTI ports. | Note | Any value
                                                         						that is entered in this field overrides the default value for the chosen phone. |
| Note | Any value
                                                         						that is entered in this field overrides the default value for the chosen phone. |
| Security
                                             					 Profile | Enter the security profile that you want to apply to the device. If the phone does not support the profile that you choose, Unified Communications Manager does not allow you to apply the configuration. All phones
                                             					 require that you apply a security profile. If the phone does not support
                                             					 security, choose a nonsecure profile. |
| Device
                                             					 SUBSCRIBE CSS | Used with the presence feature, the SUBSCRIBE Calling Search Space determines how Unified Communications Manager routes the subscription requests that come from the phone. Enter the calling search space that you want to use for this purpose. |
| E.164 | Choose the
                                             					 E.164 address that is registered with the gatekeeper. Note Ensure
                                                         						the H.323 client is configured as a gatekeeper-controlled device. Note You must
                                                         						enter a value in this field for a gatekeeper-controlled H.323 client. You can
                                                         						enter only numbers (0-9) and special characters # and * in this field. | Note | Ensure
                                                         						the H.323 client is configured as a gatekeeper-controlled device. | Note | You must
                                                         						enter a value in this field for a gatekeeper-controlled H.323 client. You can
                                                         						enter only numbers (0-9) and special characters # and * in this field. |
| Note | Ensure
                                                         						the H.323 client is configured as a gatekeeper-controlled device. |
| Note | You must
                                                         						enter a value in this field for a gatekeeper-controlled H.323 client. You can
                                                         						enter only numbers (0-9) and special characters # and * in this field. |
| UserID | Enter the
                                             					 user ID for the phone user. |
| Media
                                             					 Resource Group List | This list
                                             					 provides a prioritized grouping of media resource groups. An application
                                             					 chooses the required media resource, such as a Music On Hold server, from among
                                             					 the available media resources according to the priority order that is defined
                                             					 in a Media Resource List. |
| AAR
                                             					 Calling Search Space | Enter the
                                             					 appropriate calling search space for the device to use when it performs
                                             					 automated alternate routing (AAR). The AAR calling search space specifies the
                                             					 collection of route partitions that are searched to determine how to route a
                                             					 collected (originating) number that is otherwise blocked due to insufficient
                                             					 bandwidth. |
| MLPP
                                             					 Domain | Enter a
                                             					 hexadecimal value for the MLPP domain that is associated with this device.
                                             					 Ensure that this value is blank or a value between 0 and FFFFFF |
| MLPP
                                             					 Indication | If
                                             					 available, this setting specifies whether a device that is capable of playing
                                             					 precedence tones will use the capability when it places an MLPP precedence
                                             					 call. Default —This
                                                				  device inherits its MLPP indication setting from its device pool. Off —This device
                                                				  does not handle nor process indication of an MLPP precedence call. On —This device
                                                				  does handle and process indication of an MLPP precedence call. |
| MLPP
                                             					 Preemption | If
                                             					 available, this setting specifies whether a device that is capable of
                                             					 preempting calls in progress will use the capability when it places an MLPP
                                             					 precedence call. Default —This
                                                				  device inherits its MLPP indication setting from its device pool. Off —This device
                                                				  does not handle nor process indication of an MLPP precedence call. On —This device
                                                				  does handle and process indication of an MLPP precedence call. |
| Signal
                                             					 Packet Capture Mode | Enter the
                                             					 mode that you want to set for signal packet capture: None —Choose None
                                                				  if you do not want to specify a mode. Real-Time Mode —Use
                                                				  this mode for real-time signal packet capture. Batch Processing
                                                   					 Mode —Use this mode for batch processing signal packet capture mode. |
| Packet
                                             					 Capture Duration | Enter the
                                             					 time for packet capture in minutes. You can enter a maximum duration of 300
                                             					 minutes. |
| Authentication String | Enter a
                                             					 numeric string that contains 4 to 10 digits. To install, upgrade, or
                                             					 troubleshoot a locally significant certificate, the phone user or administrator
                                             					 must enter the authentication string on the phone. |
| Ignore
                                             					 Presentation Indicator | Enter Yes or No to configure call display restrictions on a call-by-call basis. When this check box is checked, Unified Communications Manager ignores any presentation restriction that is received for internal calls. |
| SIP
                                             					 Profile | Enter the
                                             					 default SIP profile or a specific profile that was previously created. SIP
                                             					 profiles provide specific SIP information for the phone such as default
                                             					 telephony event payload type, registration and keep alive timers, media ports,
                                             					 Iris, and dynamic DNS server addresses. |
| Digest
                                             					 User | Used with
                                             					 digest authentication (SIP security), choose an end user that you want to
                                             					 associate with the phone. Ensure
                                             					 that you configured digest credentials for the user that you choose, as
                                             					 specified in the End User Configuration window. After you
                                             					 save the phone configuration and reset the phone, the digest credentials for
                                             					 the user get added to the phone configuration file. |
| Log Out
                                             					 Profile | Enter the profile that a phone should load when an extension mobility user logs out. You must configure logout profiles in Unified Communications Manager Administration. Use Current Device
                                                					 Setting —This choice creates an autogenerated device profile as the
                                             				  default device profile. Select a User Device
                                                					 Profile —This choice assigns a user device profile, which has already
                                             				  been defined, that becomes the default device profile for this device. The chosen
                                             					 user device profile gets loaded onto the device when no user is logged in. |
| SIPCodec_MTPPreferredOrigCodec | Enter the
                                             					 codec to use if a media termination point is required for SIP calls. |
| Dial Rules | If required, enter the appropriate SIP dial rule. SIP dial
                                             					 rules provide local dial plans for Cisco Unified IP Phones 7940, and 7975 that
                                             					 run SIP, so users do not have to press a key or wait for a timer before the
                                             					 call gets processed. Leave the SIP Dial Rules field set to <None> if you do
                                             					 not want dial rules applied to the IP phone that is running SIP. This means the
                                             					 user must use the Dial softkey or wait for the timer to expire before the call
                                             					 gets processed. |
| CSS
                                             					 Reroute | Enter a
                                             					 calling search space to use for rerouting. The system
                                             					 uses the rerouting calling search space of the referrer to find the route to
                                             					 the refer-to target. When the Refer fails due to the rerouting calling search
                                             					 space, the Refer Primitive rejects the request with the "405
                                                						Method Not Allowed" message. The
                                             					 redirection (3xx) primitive and transfer feature also uses the rerouting
                                             					 calling search space to find the redirect-to or transfer-to target. |
| Common
                                             					 Phone Configuration | Enter the
                                             					 common phone configuration to which you want this phone assigned. The common
                                             					 phone configuration includes the attributes (services or features) that are
                                             					 associated with a particular user. |
| Calling
                                             					 Search Space Refer | Enter an
                                             					 out-of-dialog refer calling search space. Unified Communications Manager uses the out-of-dialog (OOD) Refer Authorization calling search space (CSS) to authorize the SIP out-of-dialog Refer. The
                                             administrator can restrict the use of out-of-dialog Refer by configuring the OOD CSS of the Referrer. Refer Primitive rejects
                                             the OOD Refer request with a "403 Forbidden" message. |
| Certificate Operation | Enter the
                                             					 Certification Operation that you want to perform from the following options: No Pending
                                                   					 Operation —No pending Certification Operation lists exist for this
                                                				  device. Choosing this option disables the remaining CAPF fields. Install/Upgrade —Install or upgrade a Certification
                                                				  Operation. Delete —Delete a
                                                				  Certification Operation Troubleshoot —Troubleshoot a Certification Operation. |
| Certificate Operation Completion Time | This
                                             					 field, which supports the Install/Upgrade, Delete, and Troubleshoot Certificate
                                             					 Operation options, specifies the date and time in which you must complete the
                                             					 operation. |
| Secure
                                             					 Shell User | Enter a
                                             					 user ID for the secure shell user. If the phone that you are configuring does
                                             					 not support secure shell access, this field does not display. Cisco Technical
                                             					 Assistance Center (TAC) uses secure shell for troubleshooting. Contact TAC for
                                             					 further assistance. |
| Secure
                                             					 Shell Password | Enter the
                                             					 password for a secure shell user. If the phone that you are configuring does
                                             					 not support secure shell access, this field does not display. Contact TAC for
                                             					 further assistance. |
| Device
                                             					 Pool | Enter the
                                             					 appropriate device pool. The device
                                             					 pool specifies a collection of properties for this device that includes
                                             					 Communications Manager Group, Date/Time Group, Region, and Calling Search Space
                                             					 for auto registration of devices. |
| Built-in
                                             					 Bridge | Enter On,
                                             					 Off, or Default to enable or disable the built-in conference bridge for the
                                             					 barge feature. |
| Calling
                                             					 Search Space | Enter the
                                             					 appropriate calling search space. A calling search space comprises a collection
                                             					 of partitions that are searched for numbers that are called from this phone
                                             					 number. The value that you choose applies to all devices that are using this
                                             					 phone number. |
| Location | Choose the
                                             					 appropriate location for this phone. A location setting of Hub_None means that
                                             					 the locations feature does not keep track of the bandwidth that this phone
                                             					 consumes. |
| Module 1 | Enter the
                                             					 appropriate expansion module or none. |
| Module 1
                                             					 Load Name | Enter the
                                             					 custom software for the appropriate expansion module, if applicable. The value
                                             					 that you enter overrides the default value for the current model. Ensure the
                                             					 firmware load matches the module load. |
| Module 2 | Enter the
                                             					 appropriate expansion module or none. |
| Module 2
                                             					 Load Name | Enter the
                                             					 custom software for the second expansion module, if applicable. The value
                                             					 that you enter overrides the default value for the current model. Ensure the
                                             					 firmware load matches the module load. |
| Phone
                                             					 Template | Enter the
                                             					 phone template name that you created for this type of bulk transaction. |
| Authentication Server | Enter the
                                             					 URL that the phone uses to validate requests that are made to the phones web
                                             					 server. If you do not provide an authentication URL, the advanced features on
                                             					 the CiscoUnifiedIPPhones that require authentication will not function.
                                             					 Leave this field blank to accept the default setting. By default, this URL
                                             					 accesses a CiscoUnifiedIPPhone Self Care Portal window that was configured
                                             					 during installation. |
| Proxy
                                             					 Server | Enter the
                                             					 host and port (for example, proxy.cisco.com:80) that are used to proxy HTTP
                                             					 requests for access to non-local host addresses from the phones HTTP client. If the
                                             					 phone receives a URL such as www.cisco.com in a service and the phone is not
                                             					 configured in the cisco.com domain, the phone uses the proxy server to access
                                             					 the URL. If the phone is configured in the cisco.com domain, the phone accesses
                                             					 the URL without using the proxy because it is in the same domain as the URL. |
| Idle | Enter the
                                             					 URL of the XML service that will appear as the idle display on the
                                             					 CiscoUnifiedIPPhone LCD screen when the phone has not been used for the time
                                             					 that is specified in the Idle Time field. For
                                             					 example, you can display a logo on the LCD screen when the phone has not been
                                             					 used for 5 minutes. |
| Idle Timer | Enter the
                                             					 seconds that you want to elapse before the phone displays the URL that is
                                             					 specified in the Idle field. |
| Secure
                                             					 Authentication URL | Enter the
                                             					 secure URL that the phone uses to validate requests that are made to the phone
                                             					 web server. Note If you
                                                         						do not provide a Secure Authentication URL, the device uses the nonsecure URL.
                                                         						If you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. By default, this URL
                                             					 accesses a CiscoUnifiedIPPhone Self Care Portal window that was configured
                                             					 during installation. Leave this
                                             					 field blank to accept the default setting. Maximum
                                             					 length: 255 | Note | If you
                                                         						do not provide a Secure Authentication URL, the device uses the nonsecure URL.
                                                         						If you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Note | If you
                                                         						do not provide a Secure Authentication URL, the device uses the nonsecure URL.
                                                         						If you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Secure
                                             					 Directory URL | Enter the
                                             					 secure URL for the server from which the phone obtains directory information.
                                             					 This parameter specifies the URL that secured Cisco Unified IP Phones use when
                                             					 you press the Directory button. Note If you
                                                         						do not provide a Secure Directory URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. Leave this
                                             					 field blank to accept the default setting. Maximum
                                             					 length: 255 | Note | If you
                                                         						do not provide a Secure Directory URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Note | If you
                                                         						do not provide a Secure Directory URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Secure
                                             					 Idle URL | Enter the
                                             					 secure URL for the information that displays on the Cisco Unified IP Phone
                                             					 display when the phone is idle, as specified in Idle Timer field. For example,
                                             					 you can display a logo on the LCD when the phone has not been used for 5
                                             					 minutes. Note If you
                                                         						do not provide a Secure Idle URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. To accept
                                             					 the default setting, leave this field blank. Maximum
                                             					 length: 255 | Note | If you
                                                         						do not provide a Secure Idle URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Note | If you
                                                         						do not provide a Secure Idle URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Secure
                                             					 Information URL | Enter the
                                             					 secure URL for the server location where the Cisco Unified IP Phone can find
                                             					 help text information. This information displays when the user presses the
                                             					 information (i) button or the question mark ( ? ) button. Note If you
                                                         						do not provide a Secure Information URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. To accept
                                             					 the default setting, leave this field blank. Maximum
                                             					 length: 255 | Note | If you
                                                         						do not provide a Secure Information URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Note | If you
                                                         						do not provide a Secure Information URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Secure
                                             					 Messages URL | Enter the
                                             					 secure URL for the messages server. The Cisco Unified IP Phone contacts this
                                             					 URL when the user presses the Messages button. Note If you
                                                         						do not provide a Secure Messages URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. To accept
                                             					 the default setting, leave this field blank. Maximum
                                             					 length: 255 | Note | If you
                                                         						do not provide a Secure Messages URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Note | If you
                                                         						do not provide a Secure Messages URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Secure
                                             					 Services URL | Enter the
                                             					 secure URL for Cisco Unified IP Phone services. The is the location that the
                                             					 secure Cisco Unified IP Phone contacts when the user presses the Services
                                             					 button. Note If you
                                                         						do not provide a Secure Services URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. To accept
                                             					 the default setting, leave this field blank. Maximum
                                             					 length: 255 | Note | If you
                                                         						do not provide a Secure Services URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Note | If you
                                                         						do not provide a Secure Services URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Hotline
                                             					 Device | Enter ‘T’
                                             					 or ‘F’. Hotline devices can only connect to other Hotline devices. This feature
                                             					 is an extension of PLAR, which configures a phone to automatically dial one
                                             					 directory number when it goes off-hook. Hotline provides additional
                                             					 restrictions that you can apply to devices that use PLAR. To
                                             					 implement Hotline, you must also create a softkey template without
                                             					 supplementary service softkeys, and apply it to the Hotline device. |
| Owner User
                                             					 ID | Enter a
                                             					 user ID for the primary phone user. |
| Common
                                             					 Phone Profile | Enter the
                                             					 common phone profile to which you want this phone assigned. The common phone
                                             					 profile includes the attributes (services or features) that are associated with
                                             					 a particular user. |
| Device
                                             					 Mobility Mode | Turn the
                                             					 device mobility feature on or off for this device or enter Default to use the
                                             					 default device mobility mode. |
| DND Option | Choose a
                                             					 DND option from the following options: None Ringer Off |
| DND
                                             					 Incoming Call Alert | Enter one
                                             					 of the following options: None Disable Flash Only Beep Only |
| Privacy | Enter one
                                             					 of the following options: On Off Default |
| Use
                                             					 Trusted Relay Point | Enter one
                                             					 of the following options: Default Off On |
| Information | Enter the
                                             					 help text URL for the information button for CiscoUnifiedIPPhones. |
| Directory | Enter the
                                             					 URL of the directory server for CiscoUnifiedIPPhones. |
| Messages | Enter the
                                             					 voice-messaging access pilot number for CiscoUnified IPPhones. |
| Services | Enter the
                                             					 URL for the services menu for CiscoUnifiedIPPhones. |
| Calling
                                             					 Party Transformation CSS | This
                                             					 setting allows you to localize the calling party number on the device. Make
                                             					 sure that the Calling Party Transformation CSS that you enter contains the
                                             					 calling party transformation pattern that you want to assign to this device |
| Single
                                             					 Button Barge | Enter one
                                             					 of the following options: Off —This setting
                                                				  disables the Single Button Barge/cBarge feature; however, the regular Barge or
                                                				  cBarge features will still work. Barge —This setting
                                                				  enables the Singe Button Barge feature. cBarge —This
                                                				  setting enables the Single Button cBarge feature. Default —This
                                                				  setting uses the Single Button Barge/cBarge setting that is in the service
                                                				  parameter. |
| Join
                                             					 Across Lines | Enter one
                                             					 of the following options: Off —This setting
                                                				  disables the Join Across Lines feature. On —This setting
                                                				  enables the Join Across Lines feature. Default —Uses the
                                                				  Join Across Lines setting that is in the service parameter. |
| BLF
                                             					 Audible Alert Setting (Phone Idle) | Enter the
                                             					 BLF Audible Alert setting that you want to use from the following values: On Off Default For this
                                             					 required field, this parameter provides an audible alert in addition to a
                                             					 visual alert on a phone that is currently idle when a call comes in to one of
                                             					 the lines that is monitored by way of a busy line field (BLF) button. |
| BLF
                                             					 Audible Alert Setting (Phone Busy) | For this
                                             					 required field, enter the BLF Audible Alert setting that you want to use from
                                             					 the following values: On Off Default |
| Always Use
                                             					 Prime Line | Enter the
                                             					 Always Use Prime Line setting that you want to use from the following values: On Off Default |
| Always Use
                                             					 Prime Line for Voice Message | Enter the
                                             					 Always Use Prime Line for Voice Message setting that you want to use from the
                                             					 following values: On Off Default |
| Services
                                             					 Provisioning | For this
                                             					 required field, enter one of the following values: Internal External URLs Both Default: Internal |
| Phone
                                             					 Personalization | Enter one
                                             					 of the following values: Disabled —None of
                                                				  the personalization settings on the phone get activated. Enabled —This
                                                				  setting accepts a personalized background image file, which is used for the
                                                				  phone screen; it accepts a preview image file for temporary display; and it
                                                				  accepts a personalized tone file, so the default ring tone can be personalized. Default —Use the
                                                				  phone personalization setting that is in the Common Phone Profile. |
| Mobility
                                             					 Identity Name | Enter a
                                             					 name that identifies the remote destination. |
| Mobility
                                             					 Identity Destination Number | Enter the
                                             					 telephone number for the destination. Include the area code and any additional
                                             					 digits that are required to obtain an outside line. Maximum field length equals
                                             					 24 characters; individual characters can take the values 0-9, * , and # . Cisco recommends that you configure the caller ID of
                                             					 the remote destination. Add the
                                             					 necessary translation pattern or route patterns to route the destination
                                             					 number. |
| Mobility
                                             					 Identity Answer Too Soon Timer | Enter the
                                             					 minimum time in milliseconds that must pass before the mobile phone can be
                                             					 answered. Range: 0 -
                                             					 10,000 milliseconds Default:
                                             					 1,500 milliseconds |
| Mobility
                                             					 Identity Answer Too Late Timer | Enter the
                                             					 maximum time in milliseconds that can pass before the mobile phone must be
                                             					 answered. Range:
                                             					 10,000 - 300,000 milliseconds Default:
                                             					 19,000 milliseconds |
| Mobility
                                             					 Identity Delay Before Ringing Cell | Enter the
                                             					 time that elapses before the mobile phone rings when a call is transferred from
                                             					 the desktop phone. Range: 0 -
                                             					 30,000 milliseconds Default:
                                             					 4,000 milliseconds |
| Mobility
                                             					 Identity Time of Day Access | Enter a
                                             					 time-of-day access record to associate with this remote destination. |
| Mobility
                                             					 Identity Time Zone | Enter a
                                             					 time zone to use for this remote destination. Note The time
                                                         						zone that you use for this remote destination is used by the time-of-day access
                                                         						feature to allow or block calls to this remote destination. | Note | The time
                                                         						zone that you use for this remote destination is used by the time-of-day access
                                                         						feature to allow or block calls to this remote destination. |
| Note | The time
                                                         						zone that you use for this remote destination is used by the time-of-day access
                                                         						feature to allow or block calls to this remote destination. |
| Mobility
                                             					 Identity Enable Mobile Connect | Enter ‘T’
                                             					 or ‘F’ in this field to allow or disallow an incoming call to ring your desktop
                                             					 phone and remote destination at the same time. |
| Mobile
                                             					 Smart Client Profile | Mobile
                                             					 Smart Client Profile is the Smart Client for smart client devices and dual-mode
                                             					 phones. Enter "Standard
                                                						Cisco Unified Mobile Communicator Profile" in this field to enable Cisco
                                             					 Unified Mobile Communicator. Leave it blank to disable it. |
| Geo
                                             					 Location | Enter the
                                             					 geo location that you want to associate with the phone. Enter "unspecified" if you do not want to associate the phone to any
                                             					 geo location. |
| Feature
                                             					 Control Policy | Enter the
                                             					 Feature Control Policy for this group of phones. A feature
                                             					 control policy specifies the appearance of features and the associated softkeys
                                             					 that are displayed on the phone. |
| Line Fields
                                                						(Optional) |
| Directory
                                             					 Number | Enter the
                                             					 directory number, up to 24 digits and special characters, for the phone. |
| Route
                                             					 Partition | Enter a
                                             					 route partition to which the directory number belongs. Note The
                                                         						directory number can appear in more than one partition. | Note | The
                                                         						directory number can appear in more than one partition. |
| Note | The
                                                         						directory number can appear in more than one partition. |
| Display | Enter the
                                             					 text that you want to display on the called party phone display, such as the
                                             					 user name (John Smith) or phone location (Conference Room 1). Note If this
                                                         						filed is left blank, the system uses the value that is entered in the Directory
                                                         						Number field. Note The
                                                         						default language specifies English. | Note | If this
                                                         						filed is left blank, the system uses the value that is entered in the Directory
                                                         						Number field. | Note | The
                                                         						default language specifies English. |
| Note | If this
                                                         						filed is left blank, the system uses the value that is entered in the Directory
                                                         						Number field. |
| Note | The
                                                         						default language specifies English. |
| Line Text
                                             					 Label | Enter text
                                             					 that identifies this directory number for a line/phone combination. Note The
                                                         						default language specifies English | Note | The
                                                         						default language specifies English |
| Note | The
                                                         						default language specifies English |
| Voice Mail
                                             					 Profile | Enter this
                                             					 parameter to make the pilot number the same as the directory number for this
                                             					 line. This action proves useful if you do not have a voice-messaging server
                                             					 that is configured for this phone. |
| Line
                                             					 Calling Search Space | Enter
                                             					 partitions that are searched for numbers that are called from this directory
                                             					 number. Note Changes
                                                         						cause an update of Pickup Group Names that are listed in the Call Pickup Group field. The setting applies to all
                                                         						devices that use this directory number. | Note | Changes
                                                         						cause an update of Pickup Group Names that are listed in the Call Pickup Group field. The setting applies to all
                                                         						devices that use this directory number. |
| Note | Changes
                                                         						cause an update of Pickup Group Names that are listed in the Call Pickup Group field. The setting applies to all
                                                         						devices that use this directory number. |
| AAR Group | Enter the
                                             					 automated alternate routing (AAR) group for this device. The AAR group provides
                                             					 the prefix digits that are used to route calls that are otherwise blocked due
                                             					 to insufficient bandwidth. Set AAR
                                             					 Group to <None> to prevent rerouting blocked calls. |
| Forward
                                             					 All CSS | Enter the
                                             					 calling search space to use when a call is forwarded to the specified
                                             					 destination. Note This
                                                         						setting applies to all devices that are using this directory number. | Note | This
                                                         						setting applies to all devices that are using this directory number. |
| Note | This
                                                         						setting applies to all devices that are using this directory number. |
| Secondary
                                             					 CSS for Forward All | Enter the
                                             					 secondary calling search space (CSS). |
| Forward
                                             					 All Destination | Enter the
                                             					 directory number or directory URI to which all calls get forwarded. Note This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. | Note | This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. |
| Note | This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. |
| Forward
                                             					 Busy External CSS | Enter the
                                             					 calling search space to use when a call from an external number gets forwarded
                                             					 to the specified destination. Note This
                                                         						setting applies to all devices that are using this directory number. | Note | This
                                                         						setting applies to all devices that are using this directory number. |
| Note | This
                                                         						setting applies to all devices that are using this directory number. |
| Forward
                                             					 Busy Internal CSS | Enter the
                                             					 calling search space to use when a call from an internal number gets forwarded
                                             					 to the specified destination. Note This
                                                         						setting applies to all devices that are using this directory number. | Note | This
                                                         						setting applies to all devices that are using this directory number. |
| Note | This
                                                         						setting applies to all devices that are using this directory number. |
| Forward
                                             					 Busy Destination External | Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 external number gets forwarded when the line is in use. Note This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. | Note | This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. |
| Note | This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. |
| Forward
                                             					 Busy Destination Internal | Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 internal number gets forwarded when the line is in use. Note This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. | Note | This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. |
| Note | This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. |
| Forward No
                                             					 Answer External CSS | Enter the
                                             					 calling search space to use when a call from an external number gets forwarded
                                             					 to the specified destination. The setting displays only if it is configured in
                                             					 the system. Note This
                                                         						setting applies to all devices that are using this directory number. | Note | This
                                                         						setting applies to all devices that are using this directory number. |
| Note | This
                                                         						setting applies to all devices that are using this directory number. |
| Forward No
                                             					 Answer Internal CSS | Enter the
                                             					 calling search space to use when a call from an internal number gets forwarded
                                             					 to the specified destination. The setting displays only if it is configured in
                                             					 the system. Note This
                                                         						setting applies to all devices that are using this directory number. | Note | This
                                                         						setting applies to all devices that are using this directory number. |
| Note | This
                                                         						setting applies to all devices that are using this directory number. |
| Forward No
                                             					 Answer External Destination | Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 external number gets forwarded when the phone is not answered. Note This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. | Note | This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. |
| Note | This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. |
| Forward No
                                             					 Answer Internal Destination | Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 internal number gets forwarded when the phone is not answered. Note This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. | Note | This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. |
| Note | This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. |
| Forward No
                                             					 Coverage External CSS | Enter the
                                             					 calling search space to use when a call from an external number gets forwarded
                                             					 to the specified destination. The setting displays only if it is configured in
                                             					 the system. Note This
                                                         						setting applies to all devices that are using this directory number. | Note | This
                                                         						setting applies to all devices that are using this directory number. |
| Note | This
                                                         						setting applies to all devices that are using this directory number. |
| Forward No
                                             					 Coverage Internal CSS | Enter the
                                             					 calling search space to use when a call from an internal number gets forwarded
                                             					 to the specified destination. The setting displays only if it is configured in
                                             					 the system. Note This
                                                         						setting applies to all devices that are using this directory number. | Note | This
                                                         						setting applies to all devices that are using this directory number. |
| Note | This
                                                         						setting applies to all devices that are using this directory number. |
| Forward No
                                             					 Coverage External Destination | Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 external number gets forwarded when the phone does not have coverage. Note This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. | Note | This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. |
| Note | This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. |
| Forward No
                                             					 Coverage Internal Destination | Enter the
                                             					 directory number or directory URI to which a call that is coming from an
                                             					 internal number gets forwarded when the phone does not have coverage. Note This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. | Note | This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. |
| Note | This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. |
| Calling
                                             					 Search Space Forward on Failure External/Internal | (CTI ports
                                             					 only) Enter the calling search space to use when a call from an internal or
                                             					 external call gets forwarded to the specified destination. The setting appears
                                             					 only if it is configured in the system. Note This
                                                         						setting applies to all devices that are using this directory number. | Note | This
                                                         						setting applies to all devices that are using this directory number. |
| Note | This
                                                         						setting applies to all devices that are using this directory number. |
| Forward on
                                             					 Failure Destination External/Internal | (CTI ports
                                             					 only) Enter the directory number or directory URI to which a call coming from
                                             					 an internal or an external number should get forwarded when a phone or CTI
                                             					 application fails. |
| Forward on
                                             					 CTI Failure Destination | This
                                             					 setting specifies the directory number to which an internal nonconnected call
                                             					 gets forwarded when an application that controls that directory number fails.
                                             					 Use any dialable phone number, including an outside destination. When you
                                             					 enter a destination value for internal calls, the system automatically copies
                                             					 this value to the Destination field for external calls. If you want external
                                             					 calls to forward to a different destination, you must enter a different value
                                             					 in the Destination field for external calls. |
| Forward on
                                             					 CTI Failure Calling Search Space | This
                                             					 setting applies to all devices that are using this directory number. When you
                                             					 choose a Calling Search Space for internal calls, the system automatically
                                             					 copies this setting to the Calling Search Space setting for external calls. If
                                             					 you want external calls to forward to a different calling search space, choose
                                             					 a different setting in the Calling Search Space for external calls. |
| Call
                                             					 Pickup Group | Choose a
                                             					 Pickup Group Name to specify the call pickup group, which can answer incoming
                                             					 calls to this directory number by dialing the appropriate pickup group number. |
| External
                                             					 Phone Number Mask | Enter the
                                             					 phone number (or mask) that is sent for Caller ID information when a call is
                                             					 placed from this line. You can
                                             					 enter a maximum of 24 numbers and "X" characters. The Xs represent the directory number and must appear at the end of
                                             					 the pattern. For example, if you specify a mask of 972813XXXX, an external call
                                             					 from extension 1234 displays a caller ID number of 9728131234. |
| Forward No
                                             					 Answer Ring Duration (CFNA) | Enter the
                                             					 number of seconds to allow the call to ring before forwarding the call to the
                                             					 Forward No Answer Destination. |
| Target
                                             					 Destination (MLPP) | Enter the
                                             					 number to which MLPP precedence calls should be directed if this directory
                                             					 number receives a precedence call and neither this number nor its call forward
                                             					 destination answers the precedence call. Values can
                                             					 include numeric characters, pound ( # ),and asterisk ( * ). |
| Calling
                                             					 Search Space (MLPP) | Enter the
                                             					 calling search space to associate with the alternate party target (destination)
                                             					 number. |
| No Answer
                                             					 Ring Duration (MLPP) | Enter the
                                             					 time, seconds (between 4 and 30), after which an MLPP precedence call will be
                                             					 directed to this directory number’s alternate party if this directory number
                                             					 and its call forwarding destination have not answered the precedence call. Leave this setting blank to use the value that is set in the Unified Communications Manager enterprise parameter, Precedence Alternate Party Timeout. |
| Maximum
                                             					 Number of Calls | You can
                                             					 configure up to 200 calls for a line on a device in a cluster, with the
                                             					 limiting factor being the device. As you configure the number of calls for one
                                             					 line, the calls that are available for another line decrease. The
                                             					 default specifies 4. If the phone does not allow multiple calls for each line,
                                             					 the default specifies 2. For CTI
                                             					 route points, you can configure up to 10,000 calls for each port. The default
                                             					 specifies 5000 calls. Use this field in conjunction with the Busy Trigger field. |
| Busy
                                             					 Trigger | This
                                             					 setting, which works in conjunction with Maximum Number of Calls and Call
                                             					 Forward Busy, determines the maximum number of calls to be presented at the
                                             					 line. If maximum number of calls is set for 50 and the busy trigger is set to
                                             					 40, incoming call 41 gets rejected with a busy cause (and will get forwarded if
                                             					 Call Forward Busy is set). If this line is shared, be aware that all the lines
                                             					 must be busy before incoming calls get rejected. Use this
                                             					 field in conjunction with Maximum Number of Calls for CTI route points. The
                                             					 default specifies 4500 calls. |
| Alerting
                                             					 Name | This name
                                             					 represents the name that displays during an alert to a shared directory number.
                                             					 For non-shared directory numbers, during alerts, the system uses the name that
                                             					 is entered in the Display field. |
| Alerting
                                             					 Name ASCII | This field
                                             					 provides the same information as the Alerting Name field, but you must limit
                                             					 input to ASCII characters. Devices that do not support Unicode
                                             					 (internationalized) characters display the content of the Alerting Name ASCII field. |
| Auto
                                             					 Answer | Enter one
                                             					 of the following options to activate the Auto Answer feature for this directory
                                             					 number: Auto Answer Off
                                                   					 <Default> Auto Answer with
                                                   					 Headset Auto Answer with
                                                   					 Speakerphone Note Make
                                                         						sure that the headset or speakerphone is not disabled when you choose Auto
                                                         						Answer with headset or Auto Answer with speakerphone. Do not
                                             					 configure Auto Answer for devices that have shared lines. | Note | Make
                                                         						sure that the headset or speakerphone is not disabled when you choose Auto
                                                         						Answer with headset or Auto Answer with speakerphone. |
| Note | Make
                                                         						sure that the headset or speakerphone is not disabled when you choose Auto
                                                         						Answer with headset or Auto Answer with speakerphone. |
| Route
                                             					 Filter | Enter a
                                             					 name in the Route Filter Name field. The name can contain up to 50 alphanumeric
                                             					 characters and can contain any combination of spaces, periods (.), hyphens (-),
                                             					 and underscore characters ( _ ). Ensure each route filter name is unique to the
                                             					 route plan. Note Use
                                                         						concise and descriptive names for your route filters. The
                                                         						CompanynameLocationCalltype format usually provides enough detail and is short
                                                         						enough to enable you to quickly and easily identify a route filter. For
                                                         						example, CiscoDallasMetro identifies a route filter for toll free, inter-local
                                                         						access and transport area (LATA) calls from the Cisco office in Dallas. | Note | Use
                                                         						concise and descriptive names for your route filters. The
                                                         						CompanynameLocationCalltype format usually provides enough detail and is short
                                                         						enough to enable you to quickly and easily identify a route filter. For
                                                         						example, CiscoDallasMetro identifies a route filter for toll free, inter-local
                                                         						access and transport area (LATA) calls from the Cisco office in Dallas. |
| Note | Use
                                                         						concise and descriptive names for your route filters. The
                                                         						CompanynameLocationCalltype format usually provides enough detail and is short
                                                         						enough to enable you to quickly and easily identify a route filter. For
                                                         						example, CiscoDallasMetro identifies a route filter for toll free, inter-local
                                                         						access and transport area (LATA) calls from the Cisco office in Dallas. |
| Dial Plan | Enter a
                                             					 dial plan; for example, North American Numbering Plan. |
| Line User
                                             					 Hold MOH Audio Source | Enter the
                                             					 audio source to use for music on hold (MOH) when a user initiates a hold
                                             					 action. |
| Line
                                             					 Network Hold MOH Audio Source | Enter the
                                             					 audio source to use for music on hold (MOH) when the network initiates a hold
                                             					 action. |
| Ring
                                             					 Setting (Phone Active) | Enter the
                                             					 ring setting that is used when this phone has another active call on a
                                             					 different line. Choose one of the following options: Use system default Disable Flash only Ring once Ring Beep only |
| Ring
                                             					 Setting (Phone Idle) | Enter the
                                             					 ring setting for the line appearance when an incoming call is received and no
                                             					 other active calls exist on that device. Choose one of the following options: Use system default Disable Flash only Ring once Ring |
| E.164 | Enter the
                                             					 E.164 address that is registered with the gatekeeper. Note Ensure
                                                         						the H.323 client is configured as a gatekeeper-controlled device. Note You must
                                                         						enter a value in this field for a gatekeeper-controlled H.323 client. You can
                                                         						enter only numbers (0-9) and special characters # and * in this field. | Note | Ensure
                                                         						the H.323 client is configured as a gatekeeper-controlled device. | Note | You must
                                                         						enter a value in this field for a gatekeeper-controlled H.323 client. You can
                                                         						enter only numbers (0-9) and special characters # and * in this field. |
| Note | Ensure
                                                         						the H.323 client is configured as a gatekeeper-controlled device. |
| Note | You must
                                                         						enter a value in this field for a gatekeeper-controlled H.323 client. You can
                                                         						enter only numbers (0-9) and special characters # and * in this field. |
| AAR
                                             					 Destination Mask | Enter the
                                             					 setting to use instead of the external phone number mask to determine the AAR
                                             					 Destination to be dialed. |
| Forward
                                             					 Unregistered Internal Destination | Enter the
                                             					 directory number to which an unregistered internal call is forwarded when the
                                             					 line is in use. This
                                             					 setting applies to any internal, dialable phone number and to all devices that
                                             					 are using this directory number. |
| Forward
                                             					 Unregistered Internal CSS | Enter the
                                             					 calling search space to use when unregistered internal calls are forwarded to
                                             					 the specified destination. This
                                             					 setting applies to all devices that are using this directory number. |
| Forward
                                             					 Unregistered External Destination | Enter the
                                             					 directory number to which an external call is forwarded when the line is in
                                             					 use. This
                                             					 setting applies to any dialable external phone number, including an outside
                                             					 destination unless restricted, and to all devices that are using this directory
                                             					 number. |
| Forward
                                             					 Unregistered External CSS | Enter the
                                             					 calling search space to use when external calls are forwarded to the specified
                                             					 destination. This
                                             					 setting applies to all devices that are using this directory number. |
| Audible
                                             					 Message Waiting Indicator Policy | Use this
                                             					 field to configure an audible message waiting indicator policy. Enter one of
                                             					 the following options: Off On —When you enter
                                                				  this option, you will receive a stutter dial tone when you take the handset off
                                                				  hook. Default —When you
                                                				  enter this option, the phone uses the default that was set at the system level. |
| Call
                                             					 Pickup Group Audio Alert Setting (Phone Idle) | This field
                                             					 determines the type of notification an incoming call sends to members of a call
                                             					 pickup group. If the called phone does not answer, the phones in the call
                                             					 pickup group that are idle will either hear a short ring (ring once) or hear
                                             					 nothing (disabled). Use System
                                                   					 Default —The value of this field gets determined by the setting of the
                                                				  Cisco CallManager service parameter Call Pickup Group Audio Alert Setting of
                                                				  Idle Station. Disable —No alert
                                                				  is sent to members of the call pickup group. Ring Once —A short
                                                				  ring is sent to members of the call pickup group. |
| Call
                                             					 Pickup Group Audio Alert Setting (Phone Active) | This field
                                             					 determines the type of notification an incoming call sends to members of a call
                                             					 pickup group. If the called phone does not answer, the phones in the call
                                             					 pickup group that are busy will either hear a beep or hear nothing (disabled). Use System
                                                   					 Default —The value of this field gets determined by the setting of the
                                                				  Cisco CallManager service parameter Call Pickup Group Audio Alert Setting of
                                                				  Busy Station. Disable —No alert
                                                				  is sent to member of the call pickup group. Beep Only —A beep
                                                				  is sent to members of the call pickup group. |
| Call
                                             					 Recording Option | This field
                                             					 determines the recording option on the line appearance of an agent. By default,
                                             					 the recording option specifies Call Recording Disabled. Enter one
                                             					 of the following options: Call Recording
                                                   					 Disabled —The calls that the agent makes on this line appearance are
                                                				  not recorded. Automatic Call Recording
                                                   					 Enabled —The calls that the agent makes on this line appearance are
                                                				  automatically recorded. Application Invoked Call
                                                   					 Recording Enabled —The calls that the agent makes on this line
                                                				  appearance are recorded if an application invokes calling recording. When the
                                             					 recording option is set to either Automatic Call Recording Enabled or
                                             					 Application Invoked Call Recording Enabled, the line appearance can be
                                             					 associated with a recording profile. When
                                             					 automatic recording is enabled, the application's recording requests get
                                             					 rejected. |
| Recording
                                             					 Profile | This field
                                             					 determines the recording profile on the line appearance of an agent. |
| Monitoring
                                             					 Calling Search Space | The
                                             					 monitoring calling search space of the supervisor line appearance must include
                                             					 the agent line or device partition to allow monitoring the agent. Enter the
                                             					 monitoring calling search space on the supervisor line appearance window. The
                                             					 default value specifies None. |
| Forward
                                             					 All CSS Activation Policy | Enter one
                                             					 of the following options: Use System Default With Configured
                                                   					 CSS |
| Party
                                             					 Entrance Tone | Enter one
                                             					 of the following Party Entrance Tone options: Default —Use the
                                                				  value that you configured in the Party Entrance Tone service parameter. On —A tone plays on the phone when a basic call changes to a multi-party call; that is, a barge call, cBarge call, ad hoc conference,
                                                meet-me conference, or a joined call. In addition, a different tone plays when a party leaves the multi-party call. If the
                                                controlling device, that is, the originator of the multi-party call has a built-in bridge, the tone gets played to all parties
                                                if you choose On for the controlling device. When the controlling device, for example, the conference controller, is no longer
                                                present on the call or if the controlling device cannot play the tone, Unified Communications Manager does not play the tone
                                                even if you choose On. Off —A tone does
                                                				  not play on the phone when a basic call changes to a multi-party call. |
| Park
                                             					 Monitor Forward No Retrieve Ext Destination | When the
                                             					 parkee is an external party, then the call will be forwarded to the specified
                                             					 destination in the parker’s Park Monitoring Forward No Retrieve Destination
                                             					 External parameter. If the Forward No Retrieve Destination External field value
                                             					 is empty, the parkee will be redirected to the parker’s line. |
| Park
                                             					 Monitor Forward No Retrieve Int Destination | When the
                                             					 parkee is an internal party, then the call will be forwarded to the specified
                                             					 destination in the parker’s Park Monitoring Forward No Retrieve Destination
                                             					 Internal parameter. If the Forward No Retrieve Destination Internal is empty,
                                             					 the parkee will be redirected to the parker’s line. |
| Park
                                             					 Monitor Forward No Retrieve Int Voice Mail | This
                                             					 setting uses the settings in the Voice Mail Profile Configuration window. With this setting, Unified Communications Manager ignores the settings in the Destination box and Calling Search Space. |
| Park
                                             					 Monitor Forward No Retrieve Ext Voice Mail | This
                                             					 setting uses the settings in the Voice Mail Profile Configuration window. With this setting, Unified Communications Manager ignores the settings in the Destination box and Calling Search Space. |
| Park
                                             					 Monitor Forward No Retrieve Ext CSS | Choose the
                                             					 calling search space to apply to the directory number. |
| Park
                                             					 Monitor Forward No Retrieve Int CSS | Choose the
                                             					 calling search space to apply to the directory number. |
| Park
                                             					 Monitor Reversion Timer | This parameter determines the number of seconds that Unified Communications Manager waits before prompting the user to retrieve a call that the user parked. This timer starts when the user presses the Park
                                             softkey on the phone, and a reminder is issued when the timer expires. Default:
                                             					 60 seconds If you
                                             					 configure a non-zero value, this value overrides the value of this parameter
                                             					 set in the Service Parameters window. However, if you configure a value of 0
                                             					 here, then the value in the Service Parameters window will be used. |
| Log Missed
                                             					 Calls | This field allows you to turn this feature on or off. Enter ‘T’ to enable Unified Communications Manager to log missed calls in the call history for that directory number on the phone. Enter ‘F’ to disable this feature. |
| URI (1-5)
                                             					 on Directory Number | Enter a
                                             					 directory URI to associate with the directory number for this phone. Follow the
                                             					 username@host format. Enter a username of up to 47 alphanumeric characters. For
                                             					 the host address, enter an IPv4 address or fully qualified domain name. You can
                                             					 associate up to five directory URIs to a single directory number. Note Within
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
                                             					 Route Partition on Directory Number | Enter the
                                             					 partition on which the directory URI belongs. If you do not want to restrict
                                             					 access to the directory URI, leave the field blank. |
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
| Enterprise
                                             					 Add to Local Route Partition | Enter a
                                             					 't' to add this enterprise alternate number to a local route partition. Enter
                                             					 'f' to leave the E.164 number off of local routing. |
| Enterprise
                                             					 Advertise via globally | Enter a
                                             					 't' to enable ILS to advertise this alternate number to rest of the ILS
                                             					 network. Enter an 'f' if you don't want ILS to advertise this number. |
| Enterprise
                                             					 Is Urgent | Enter a
                                             					 't' to classify routing for this alternate number as urgent. By default, if the dial plan contains overlapping route patterns Unified Communications Manager does not route the call until
                                             the interdigit timer expires (even if a possible route exists for the dialed digits). This setting guards against learned
                                             numbers that overlap with statically configured directory numbers and number patterns by allowing Unified Communications Manager
                                             to choose the best match of all available routes for the dial string. When you mark the number as urgent priority, Unified Communications Manager routes the call as soon as it finds a match between
                                             the dialed digits and an available route, without waiting for the interdigit timer to expire (for example, the T302 Timer
                                             service parameter). |
| Enterprise
                                             					 Number Mask | Enter the number mask to apply to the directory number. Unified Communications Manager applies the mask to create an enterprise
                                             alternate number that is an alias of this directory number. |
| Enterprise
                                             					 Route Partition | Enter the
                                             					 local route partition to which you want to assign this enterprise alternate
                                             					 number. |
| +E.164 Add
                                             					 to Local Route Partition | Enter a
                                             					 't' to add this E.164 alternate number to a local route partition. Enter 'f' to
                                             					 leave the E.164 number off of local routing. |
| +E.164
                                             					 Advertise via globally | Enter a
                                             					 't' to enable ILS to advertise this alternate number to rest of the ILS
                                             					 network. Enter an 'f' if you don't want ILS to advertise this number. |
| +E.164 Is
                                             					 Urgent | Enter a
                                             					 't' to classify routing for this alternate number as urgent. By default, if the dial plan contains overlapping route patterns Unified Communications Manager does not route the call until
                                             the interdigit timer expires (even if a possible route exists for the dialed digits). This setting guards against learned
                                             numbers that overlap with statically configured directory numbers and number patterns by allowing Unified Communications Manager
                                             to choose the best match of all available routes for the dial string. When you mark the number as urgent priority, Unified Communications Manager routes the call as soon as it finds a match between
                                             the dialed digits and an available route, without waiting for the interdigit timer to expire (for example, the T302 Timer
                                             service parameter). |
| +E.164
                                             					 Number Mask | Enter the number mask to apply to the directory number. Unified Communications Manager applies the mask to create an +E.164
                                             alternate number that is an alias of this directory number. |
| +E.164
                                             					 Route Partition | Enter the
                                             					 local route partition to which you want to assign this +E.164 alternate number. |
| Intercom Fields
                                                						(Optional) |
| Intercom
                                             					 Directory Number | Enter a
                                             					 dialable phone number. Values can include numeric characters and route pattern
                                             					 wildcards and special characters except for (.) and ( @ ). The
                                             					 directory number that you enter can appear in more than one partition. At the
                                             					 beginning of the directory number, enter \+ if you want to use the international escape
                                             					 character + . For this field, \+ does not represent a wildcard; instead, entering \+ represents a dialed digit. |
| Intercom
                                             					 Route Partition | Enter the
                                             					 partition to which the directory number belongs. Make sure that the directory
                                             					 number that you enter in the Intercom Directory Number field is unique within
                                             					 the partition that you choose. Note The
                                                         						directory number can appear in more than one partition. | Note | The
                                                         						directory number can appear in more than one partition. |
| Note | The
                                                         						directory number can appear in more than one partition. |
| Description | Enter a
                                             					 description of the directory number and route partition. |
| Alerting
                                             					 Name | Enter a
                                             					 name that you want to display on the phone of the caller. This
                                             					 setting, which supports the Identification Services for the QSIG protocol,
                                             					 applies to shared and nonshared directory numbers. |
| Alerting
                                             					 Name ASCII | This field
                                             					 provides the same information as the Alerting Name field, but you must limit
                                             					 input to ASCII characters. Devices that do not support Unicode
                                             					 (internationalized) characters display the content of the Alerting Name ASCII
                                             					 field. |
| Intercom Directory Number
                                                						Settings |
| Calling
                                             					 Search Space | Enter the
                                             					 appropriate calling search space. A calling search space comprises a collection
                                             					 of partitions that are searched for numbers that are called from this directory
                                             					 number. The value that you choose applies to all devices that are using this
                                             					 directory number. |
| Intercom
                                             					 Presence Group | Enter a
                                             					 Presence Group for this directory number. The selected group specifies the
                                             					 devices, end users, and application users that can monitor this directory
                                             					 number. |
| Intercom
                                             					 Display | Leave this
                                             					 field blank to have the system display the extension. Use a
                                             					 maximum of 30 alphanumeric characters. Typically, use the user name or the
                                             					 directory number (if using the directory number, the person receiving the call
                                             					 may not see the proper identity of the caller). |
| Intercom
                                             					 ASCII Display | This field
                                             					 provides the same information as the Display (Internal Caller ID) field, but
                                             					 you must limit input to ASCII characters. Devices that do not support Unicode
                                             					 (internationalized) characters display the content of the ASCII Display (Internal Caller ID) field. |
| Intercom
                                             					 Line Text Label | Use this
                                             					 field only if you do not want the intercom directory number to show on the line
                                             					 appearance. Enter text that identifies this directory number for a line/phone
                                             					 combination. |
| Intercom
                                             					 Speed Dial | Enter the
                                             					 number that you want the system to dial when the user presses the speed-dial
                                             					 button. You can enter digits 0 through 9, * , # , and + , which is the international escape character. |
| Intercom
                                             					 External Phone Number Mask | Enter the
                                             					 phone number (or mask) that is used to send Caller ID information when a call
                                             					 is placed from this line. You can
                                             					 enter a maximum of 24 number, the international escape character +, and "X" characters. The Xs represent the directory number and must appear at the end of
                                             					 the pattern. For example, if you specify a mask of 972813XXXX, an external call
                                             					 from extension 1234 displays a caller ID number of 9728131234. |
| Intercom
                                             					 Caller Name | Enter ‘T’
                                             					 to enable the caller name to display upon call forward. Enter ‘F’ to disable
                                             					 it. |
| Intercom
                                             					 Caller Number | Enter ‘T’
                                             					 to enable the caller number to display upon call forward. Enter ‘F’ to disable
                                             					 it. |
| Intercom
                                             					 Call Recording Option | Enter one
                                             					 of the following options: Call Recording
                                                   					 Disabled —The calls that the agent makes on this line appearance are
                                                				  not recorded. Automatic Call Recording
                                                   					 Enabled —The calls that the agent makes on this line appearance are
                                                				  automatically recorded. Application Invoked Call
                                                   					 Recording Enabled —The calls that the agent makes on this line
                                                				  appearance are recorded if an application invokes calling recording. |
| Intercom
                                             					 Recording Profile | Enter the
                                             					 recording profile on the line appearance of an agent. |
| Intercom
                                             					 Monitoring Calling Search Space | The
                                             					 monitoring calling search space of the supervisor line appearance must include
                                             					 the agent line or device partition to allow monitoring the agent. Enter an
                                             					 existing calling search space. The
                                             					 default value specifies None. |
| Auto
                                             					 Answer | Enter one
                                             					 of the following options to activate the auto answer feature for this directory
                                             					 number: Auto Answer Off
                                                   					 <Default> Auto Answer with
                                                   					 Headset Auto Answer with
                                                   					 Speakerphone Note Do not
                                                         						configure auto answer for devices that have shared lines. | Note | Do not
                                                         						configure auto answer for devices that have shared lines. |
| Note | Do not
                                                         						configure auto answer for devices that have shared lines. |

| Note | Any value
                                                         						that is entered in this field overrides the default value for the chosen phone. |
|---|---|

| Note | Ensure
                                                         						the H.323 client is configured as a gatekeeper-controlled device. |
|---|---|

| Note | You must
                                                         						enter a value in this field for a gatekeeper-controlled H.323 client. You can
                                                         						enter only numbers (0-9) and special characters # and * in this field. |
|---|---|

| Note | If you
                                                         						do not provide a Secure Authentication URL, the device uses the nonsecure URL.
                                                         						If you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
|---|---|

| Note | If you
                                                         						do not provide a Secure Directory URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
|---|---|

| Note | If you
                                                         						do not provide a Secure Idle URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
|---|---|

| Note | If you
                                                         						do not provide a Secure Information URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
|---|---|

| Note | If you
                                                         						do not provide a Secure Messages URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
|---|---|

| Note | If you
                                                         						do not provide a Secure Services URL, the device uses the nonsecure URL. If you
                                                         						provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
|---|---|

| Note | The time
                                                         						zone that you use for this remote destination is used by the time-of-day access
                                                         						feature to allow or block calls to this remote destination. |
|---|---|

| Note | The
                                                         						directory number can appear in more than one partition. |
|---|---|

| Note | If this
                                                         						filed is left blank, the system uses the value that is entered in the Directory
                                                         						Number field. |
|---|---|

| Note | The
                                                         						default language specifies English. |
|---|---|

| Note | The
                                                         						default language specifies English |
|---|---|

| Note | Changes
                                                         						cause an update of Pickup Group Names that are listed in the Call Pickup Group field. The setting applies to all
                                                         						devices that use this directory number. |
|---|---|

| Note | This
                                                         						setting applies to all devices that are using this directory number. |
|---|---|

| Note | This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. |
|---|---|

| Note | This
                                                         						setting applies to all devices that are using this directory number. |
|---|---|

| Note | This
                                                         						setting applies to all devices that are using this directory number. |
|---|---|

| Note | This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. |
|---|---|

| Note | This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. |
|---|---|

| Note | This
                                                         						setting applies to all devices that are using this directory number. |
|---|---|

| Note | This
                                                         						setting applies to all devices that are using this directory number. |
|---|---|

| Note | This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. |
|---|---|

| Note | This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. |
|---|---|

| Note | This
                                                         						setting applies to all devices that are using this directory number. |
|---|---|

| Note | This
                                                         						setting applies to all devices that are using this directory number. |
|---|---|

| Note | This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. |
|---|---|

| Note | This
                                                         						setting applies to any dialable phone number, including an outside destination
                                                         						unless restricted, and to all devices that are using this directory number. |
|---|---|

| Note | This
                                                         						setting applies to all devices that are using this directory number. |
|---|---|

| Note | Make
                                                         						sure that the headset or speakerphone is not disabled when you choose Auto
                                                         						Answer with headset or Auto Answer with speakerphone. |
|---|---|

| Note | Use
                                                         						concise and descriptive names for your route filters. The
                                                         						CompanynameLocationCalltype format usually provides enough detail and is short
                                                         						enough to enable you to quickly and easily identify a route filter. For
                                                         						example, CiscoDallasMetro identifies a route filter for toll free, inter-local
                                                         						access and transport area (LATA) calls from the Cisco office in Dallas. |
|---|---|

| Note | Ensure
                                                         						the H.323 client is configured as a gatekeeper-controlled device. |
|---|---|

| Note | You must
                                                         						enter a value in this field for a gatekeeper-controlled H.323 client. You can
                                                         						enter only numbers (0-9) and special characters # and * in this field. |
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

| Note | The
                                                         						directory number can appear in more than one partition. |
|---|---|

| Note | Do not
                                                         						configure auto answer for devices that have shared lines. |
|---|---|

| Step 1 | Choose Bulk Administration > Phones > Update Jabber Device . |
|---|---|
| Step 2 | In the Jabber Device Information section, from the File Name drop-down list, choose the text file that you uploaded. |
| Step 3 | In the Job Information area, enter the Job description. |
| Step 4 | Choose a method to update the device names. Do one of the following: Select Run Immediately to update the device names immediately. Select Run Later to insert the device names later. |
| Step 5 | To create a job for updating the device names, click Submit . To schedule or activate this job, use the Job Scheduler option in the Bulk Administration main menu. |