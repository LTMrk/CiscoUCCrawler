---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-6d96141ded
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_0101001.html
retrieved_at: 2026-08-16T17:32:23.271759+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Software-Based Endpoints

## Chapter: Configure Software-Based Endpoints

# Configure Software-Based Endpoints

## Software-Based Endpoint Configuration

Complete the tasks in this chapter to configure software-based endpoints such as CTI ports, H.323 clients, and Cisco IP Communicator.

## Configure CTI
                        	 Ports

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Add New .

Step 3

From the Phone Type drop down list, select CTI Port and
                                       			 click Next .

Step 4

Configure the fields in the Phone Configuration window. See the Related
                                       			 Topics section for more information about the fields and their configuration
                                       			 options.

Step 5

Click Save .

### CTI Port
                           	 Settings

#### Number Presentation Transformation

Field

Description

Device Name

Specifies the name for the CTI Port that is automatically
                                             						populated based on the Owner User ID.

The format of the device name is CTIRD<OwnerUserID> by default.

This field is editable. The device name can comprise up to
                                             						15 characters. Valid characters include letters, numbers, dashes, dots
                                             						(periods), spaces, and underscores.

Description

Enter a text description of the CTI Port.

This field can contain up to 128 characters. You can use all
                                             						characters except quotes (“), close angle bracket (>), open angle bracket
                                             						(<), backslash (\), ampersand (&), and percent sign (%).

Device Pool

Choose the device pool to which you want the CTI Port
                                             						assigned. The device pool defines sets of common characteristics for devices,
                                             						such as region, date/time group, and softkey template.

To see the Device Pool configuration settings, click the
                                             						View Details link.

Common Device Configuration

Choose the Common Device Configuration to which you want the
                                             						CTI Port assigned.

To see the Common Device Configuration settings, click the
                                             						View Details link.

Common Phone Profile

From the drop-down list box, choose a common phone profile
                                             						from the list of available common phone profiles.

To see the Common Phone Profile settings, click the View
                                             						Details link.

Calling Search Space

From the drop-down list, choose the calling search space or
                                             						leave the calling search space as the default of <None>.

AAR Calling Search Space

From the drop-down list, choose the appropriate calling
                                             						search space for the device to use when it performs automated alternate routing
                                             						(AAR) or leave the calling search space as the default of <None>.

Media Resource Group List

Choose the appropriate Media Resource Group List. A Media
                                             						Resource Group List comprises a prioritized grouping of media resource groups.

If you choose <None> , Cisco Unified CM uses
                                             						the Media Resource Group List that is defined in the device pool.

User Hold MOH Audio Source

From the drop-down list, choose the audio source to use for
                                             						music on hold (MOH) when a user initiates a hold action.

Network Hold MOH Audio Source

From the drop-down list, choose the audio source to use for
                                             						MOH when the network initiates a hold action.

Location

From the drop-down list, choose the location that is
                                             						associated with the phones and gateways in the device pool.

AAR Group

User Locale

From the drop-down list box, choose the user locale that is
                                             						associated with the CTI Port. The user locale identifies a set of detailed
                                             						information to support users, including language and font.

If no user locale is specified, Cisco Unified CM uses the
                                             						user locale that is associated with the device pool.

Network Locale

From the drop-down list box, choose the network locale that
                                             						is associated with the CTI Port. The network locale contains a definition of
                                             						the tones and cadences that the phone in a specific geographic area uses.

If no network locale is specified, Cisco Unified CM uses the
                                             						user locale that is associated with the device pool.

Privacy

For Privacy, choose On in the Privacy drop-down list box.

Owner

Owner User ID

From the drop-down list box, choose the user ID of the
                                             						assigned CTI Port user. The user ID gets recorded in the call detail record
                                             						(CDR) for all calls made from this device. Assigning a user ID to the device
                                             						also moves the device from “Unassigned Devices” to “Users” in the License Usage
                                             						Report.

Join Across Lines

From the drop-down list box, enable or disable the Join
                                             						Across Lines feature for this device or choose Default to use the service parameter
                                             						setting.

Use Trusted Relay Point

Choose one of the following values:

Off—Choose this value to disable the use of a Trusted
                                                   							 Relay Point (TRP) with this device. This setting overrides the Use Trusted
                                                   							 Relay Point setting in the common device configuration with which this device
                                                   							 associates.

On—Choose this value to enable the use of a TRP with
                                                   							 this device. This setting overrides the Use Trusted Relay Point setting in the
                                                   							 common device configuration with which this device associates.

Default—If you choose this value, the device uses the
                                                   							 Use Trusted Relay Point setting from the common device configuration with which
                                                   							 this device associates.

Always Use Prime Line

From the drop-down list box, choose one of the following
                                             						options:

Off—When the phone is idle and receives a call on any
                                                   							 line, the phone user answers the call from the line on which the call is
                                                   							 received.

On—When the phone is idle (off hook) and receives a call
                                                   							 on any line, the primary line gets chosen for the call. Calls on other lines
                                                   							 continue to ring, and the phone user must select those other lines to answer
                                                   							 these calls.

Default—Cisco Unified Communications Manager uses the
                                                   							 configuration from the Always Use Prime Line service parameter, which supports
                                                   							 the Cisco CallManager service.

Always Use Prime Line for Voice Message

From the drop-down list box, choose one of the following
                                             						options:

Off—If the phone is idle, pressing the Messages button
                                                   							 on the phone automatically dials the voice-messaging system from the line that
                                                   							 has a voice message. Cisco Unified Communications Manager always selects the
                                                   							 first line that has a voice message. If no line has a voice message, the
                                                   							 primary line gets used when the phone user presses the Messages button.

On—If the phone is idle, the primary line on the phone
                                                   							 becomes the active line for retrieving voice messages when the phone user
                                                   							 presses the Messages button on the phone

Default—Cisco Unified Communications Manager uses the
                                                   							 configuration from the Always Use Prime Line for Voice Message service
                                                   							 parameter, which supports the Cisco CallManager service.

Geolocation

From the drop-down list box, choose a geolocation.

You can choose the Unspecified geolocation, which designates
                                             						that this device does not associate with a geolocation.

You can also choose a geolocation that has been configured
                                             						with the System > Geolocation
                                                   							 Configuration menu option.

Ignore Presentation Indicators (internal calls only)

Check this check box to configure call display restrictions
                                             						on a call-by-call basis. When this check box is checked, Cisco Unified
                                             						Communications Manager ignores any presentation restriction that is received
                                             						for internal calls.

Use this configuration in combination with the calling line
                                             						ID presentation and connected line ID presentation configuration at the
                                             						translation pattern level. Together, these settings allow you to configure call
                                             						display restrictions to selectively present or block calling and/or connected
                                             						line display information for each call.

Logged into Hunt Group

When the CTI port gets added to a hunt list, the
                                             						administrator can log the user in or out by checking (and unchecking) this
                                             						check box.

Users use the softkey on the phone to log their phone in or
                                             						out of the hunt list.

Remote Device

Check this box to allocate a buffer for the device when it
                                             						registers and to bundle SCCP messages to the phone.

Tip

Because this feature consumes resources, be sure to check
                                                         						  this check box only when you are experiencing signaling delays.

Field

Description

Calling Party Transformation CSS

This setting allows you to localize the calling party number on the device. Make sure that the Calling Party Transformation
                                             CSS that you choose contains the calling party transformation pattern that you want to assign to this device.

Use Device Pool Calling Party Transformation CSS

To use the Calling Party Transformation CSS that is configured in the device pool that is assigned to this device, check this
                                             check box. If you do not check this check box, the device uses the Calling Party Transformation CSS that you configured in
                                             the Trunk Configuration window.

Field

Description

Calling Party Transformation CSS

From the drop-down list box, choose the calling search space (CSS) that contains the calling party transformation pattern
                                             that you want to apply on the remote calling number for calls received on this device.

Use Device Pool Calling Party Transformation CSS

Check this check box to apply the Calling Party Transformation CSS configured at the device pool to which this device belongs
                                             to transform the remote calling and remote connected number.

Field

Description

BLF Presence Group

From the drop-down list box, choose a Busy Lamp Field (BLF) presence group for the end user. The selected group specifies
                                             the destinations that the end user can monitor

The default value for BLF Presence Group specifies Standard Presence group, configured with installation. BLF Presence Groups
                                             that are configured in Cisco Unified Administration also appear in the drop-down list box.

Device Security Profile

Choose the security profile to apply to the device.

You must apply a security profile to all devices that are configured in Cisco Unified Communications Manager Administration.

SUBSCRIBE Calling Search Space

Supported with the Presence feature, the SUBSCRIBE calling search space determines how Cisco Unified Communications Manager
                                             routes presence requests that come from the end user. This setting allows you to apply a calling search space separate from
                                             the call-processing search space for presence (SUBSCRIBE) requests for the end user.

From the drop-down list, choose the SUBSCRIBE calling search space to use for presence requests for the end user. All calling
                                             search spaces that you configure in Cisco Unified Communications Manager Administration display in the SUBSCRIBE Calling Search
                                             Space drop-down list.

If you do not select a different calling search space for the end user from the drop-down list, the SUBSCRIBE calling search
                                             space defaults to None.

To configure a SUBSCRIBE calling search space specifically for this purpose, you can configure a calling search space as you
                                             do all calling search spaces.

Unattended Port

Check this check box to indicate an unattended port on this device.

Field

Description

MLPP Domain

From the drop-down list, choose an Multilevel Precedence and Preemption (MLPP) domain to associate with this device. If you
                                             leave this field blank, this device inherits its MLPP domain from the value that is set for the device pool. If the device
                                             pool does not have an MLPP Domain setting, this device inherits its MLPP Domain from the value that is set for the MLPP Domain
                                             Identifier enterprise parameter.

The default value for MLPP Domain specifies None.

Confidential Access Mode

From the drop-down list box, select one of the following options to set the Confidential Access Level mode:

Fixed—Confidential Access Level value has higher precedence over call completion.

Variable—Call completion has higher precedence over CAL level.

Confidential Access Level

Select the appropriate Confidential Access Level value from the drop-down list box.

Field

Description

Do Not Disturb

Check this check box to enable Do Not Disturb on the remote device.

DND Option

When you enable DND, Call Reject option specifies that no incoming call information gets presented to the user. Depending
                                             on how you configure the DND Incoming Call Alert parameter, the device may play a beep or display a flash notification of
                                             the call.

DND Incoming Call Alert

When you enable the DND Ringer Off or Call Reject option, this parameter specifies how a call displays on the device.

From the drop-down list, choose one of the following options:

None—This option specifies that the DND Incoming Call Alert setting from the Common Phone Profile window gets used for this
                                                   device

Disable—This option disables both beep and flash notification of a call, but, for the DND Ringer Off option, incoming call
                                                   information still gets displayed. For the DND Call Reject option, no call alerts display, and no information gets sent to
                                                   the device.

Beep Only—For an incoming call, this option causes the device to play a beep tone only.

Flash Only—For an incoming call, this option causes the device to display a flash alert.

## Configure an H.323
                        	 Client

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Add New .

Step 3

From the Phone Type drop down list, select H.323 Client
                                       			 and click Next .

Step 4

Configure the fields in the Phone Configuration window. See the Related
                                       			 Topics section for more information about the fields and their configuration
                                       			 options.

Step 5

Click Save .

### H.323 Client Settings

## Configure Cisco IP Communicator

Cisco IP Communicator is a software-based application that allows users to place and receive phone calls by using their personal
                              computers. It provides the same functionality as a full-featured Cisco Unified IP Phone. Cisco IP Communicator depends upon
                              the Cisco Unified Communications Manager call-processing system to provide telephony features and voice-over-IP capabilities.
                              You administer Cisco IP Communicator as a phone device by using the Cisco Unified Communications Manager Administration Phone
                              Configuration window.

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Add New .

Step 3

From the Phone Type drop down list, select Cisco IP Communicator and
                                       			 click Next .

Step 4

From the Select the device protocol drop-down list, select either SCCP or SIP and
                                       			 click Next .

Step 5

Configure the  following mandatory fields in the Phone Configuration window.

Device Name —enter a name to identify the Cisco IP Communicator device.

Device Pool –—choose the device pool to which you want this phone assigned. The
                                                device pool defines sets of common characteristics for devices,
                                                such as region, date/time group, and softkey template.

Phone Button Template —choose the appropriate phone button template. The phone button
                                                template determines the configuration of buttons on a phone and
                                                identifies which feature (line, speed dial, and so on) is used for
                                                each button.

Owner User ID —from the drop-down list box, choose the user ID of the assigned
                                                phone user.

Device Security Profile –—choose the security profile to apply to the device.

You can use default configuration for the remaining fields. See the online help for more information about the fields and
                                          their configuration options.

Step 6

Click Save .

Step 7

In the Association area, click Line [1] - Add a new DN .

Step 8

In the Directory Number field, enter the directory number that you want to associate with the phone.

Step 9

Click Save .

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . The Find and List Phones window appears. |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the Phone Type drop down list, select CTI Port and
                                       			 click Next . The Phone Configuration window appears. |
| Step 4 | Configure the fields in the Phone Configuration window. See the Related
                                       			 Topics section for more information about the fields and their configuration
                                       			 options. |
| Step 5 | Click Save . |

| Field | Description |
|---|---|
| Device Name | Specifies the name for the CTI Port that is automatically
                                             						populated based on the Owner User ID. The format of the device name is CTIRD<OwnerUserID> by default. This field is editable. The device name can comprise up to
                                             						15 characters. Valid characters include letters, numbers, dashes, dots
                                             						(periods), spaces, and underscores. |
| Description | Enter a text description of the CTI Port. This field can contain up to 128 characters. You can use all
                                             						characters except quotes (“), close angle bracket (>), open angle bracket
                                             						(<), backslash (\), ampersand (&), and percent sign (%). |
| Device Pool | Choose the device pool to which you want the CTI Port
                                             						assigned. The device pool defines sets of common characteristics for devices,
                                             						such as region, date/time group, and softkey template. To see the Device Pool configuration settings, click the
                                             						View Details link. |
| Common Device Configuration | Choose the Common Device Configuration to which you want the
                                             						CTI Port assigned. To see the Common Device Configuration settings, click the
                                             						View Details link. |
| Common Phone Profile | From the drop-down list box, choose a common phone profile
                                             						from the list of available common phone profiles. To see the Common Phone Profile settings, click the View
                                             						Details link. |
| Calling Search Space | From the drop-down list, choose the calling search space or
                                             						leave the calling search space as the default of <None>. |
| AAR Calling Search Space | From the drop-down list, choose the appropriate calling
                                             						search space for the device to use when it performs automated alternate routing
                                             						(AAR) or leave the calling search space as the default of <None>. |
| Media Resource Group List | Choose the appropriate Media Resource Group List. A Media
                                             						Resource Group List comprises a prioritized grouping of media resource groups. If you choose <None> , Cisco Unified CM uses
                                             						the Media Resource Group List that is defined in the device pool. |
| User Hold MOH Audio Source | From the drop-down list, choose the audio source to use for
                                             						music on hold (MOH) when a user initiates a hold action. |
| Network Hold MOH Audio Source | From the drop-down list, choose the audio source to use for
                                             						MOH when the network initiates a hold action. |
| Location | From the drop-down list, choose the location that is
                                             						associated with the phones and gateways in the device pool. |
| AAR Group | Choose the automated alternate routing
                                          					 (AAR) group for this device. The AAR group provides the prefix digits that are
                                          					 used to route calls that are otherwise blocked due to insufficient bandwidth.
                                          					 If no AAR group is specified, Cisco Unified CM uses the AAR group that is
                                          					 associated with Device Pool or Line. |
| User Locale | From the drop-down list box, choose the user locale that is
                                             						associated with the CTI Port. The user locale identifies a set of detailed
                                             						information to support users, including language and font. If no user locale is specified, Cisco Unified CM uses the
                                             						user locale that is associated with the device pool. |
| Network Locale | From the drop-down list box, choose the network locale that
                                             						is associated with the CTI Port. The network locale contains a definition of
                                             						the tones and cadences that the phone in a specific geographic area uses. If no network locale is specified, Cisco Unified CM uses the
                                             						user locale that is associated with the device pool. |
| Privacy | For Privacy, choose On in the Privacy drop-down list box. |
| Owner | Select User or Anonymous (Public/Shared Space, for the
                                          					 owner type. |
| Owner User ID | From the drop-down list box, choose the user ID of the
                                             						assigned CTI Port user. The user ID gets recorded in the call detail record
                                             						(CDR) for all calls made from this device. Assigning a user ID to the device
                                             						also moves the device from “Unassigned Devices” to “Users” in the License Usage
                                             						Report. |
| Join Across Lines | From the drop-down list box, enable or disable the Join
                                             						Across Lines feature for this device or choose Default to use the service parameter
                                             						setting. |
| Use Trusted Relay Point | Choose one of the following values: Off—Choose this value to disable the use of a Trusted
                                                   							 Relay Point (TRP) with this device. This setting overrides the Use Trusted
                                                   							 Relay Point setting in the common device configuration with which this device
                                                   							 associates. On—Choose this value to enable the use of a TRP with
                                                   							 this device. This setting overrides the Use Trusted Relay Point setting in the
                                                   							 common device configuration with which this device associates. Default—If you choose this value, the device uses the
                                                   							 Use Trusted Relay Point setting from the common device configuration with which
                                                   							 this device associates. |
| Always Use Prime Line | From the drop-down list box, choose one of the following
                                             						options: Off—When the phone is idle and receives a call on any
                                                   							 line, the phone user answers the call from the line on which the call is
                                                   							 received. On—When the phone is idle (off hook) and receives a call
                                                   							 on any line, the primary line gets chosen for the call. Calls on other lines
                                                   							 continue to ring, and the phone user must select those other lines to answer
                                                   							 these calls. Default—Cisco Unified Communications Manager uses the
                                                   							 configuration from the Always Use Prime Line service parameter, which supports
                                                   							 the Cisco CallManager service. |
| Always Use Prime Line for Voice Message | From the drop-down list box, choose one of the following
                                             						options: Off—If the phone is idle, pressing the Messages button
                                                   							 on the phone automatically dials the voice-messaging system from the line that
                                                   							 has a voice message. Cisco Unified Communications Manager always selects the
                                                   							 first line that has a voice message. If no line has a voice message, the
                                                   							 primary line gets used when the phone user presses the Messages button. On—If the phone is idle, the primary line on the phone
                                                   							 becomes the active line for retrieving voice messages when the phone user
                                                   							 presses the Messages button on the phone Default—Cisco Unified Communications Manager uses the
                                                   							 configuration from the Always Use Prime Line for Voice Message service
                                                   							 parameter, which supports the Cisco CallManager service. |
| Geolocation | From the drop-down list box, choose a geolocation. You can choose the Unspecified geolocation, which designates
                                             						that this device does not associate with a geolocation. You can also choose a geolocation that has been configured
                                             						with the System > Geolocation
                                                   							 Configuration menu option. |
| Ignore Presentation Indicators (internal calls only) | Check this check box to configure call display restrictions
                                             						on a call-by-call basis. When this check box is checked, Cisco Unified
                                             						Communications Manager ignores any presentation restriction that is received
                                             						for internal calls. Use this configuration in combination with the calling line
                                             						ID presentation and connected line ID presentation configuration at the
                                             						translation pattern level. Together, these settings allow you to configure call
                                             						display restrictions to selectively present or block calling and/or connected
                                             						line display information for each call. |
| Logged into Hunt Group | When the CTI port gets added to a hunt list, the
                                             						administrator can log the user in or out by checking (and unchecking) this
                                             						check box. Users use the softkey on the phone to log their phone in or
                                             						out of the hunt list. |
| Remote Device | Check this box to allocate a buffer for the device when it
                                             						registers and to bundle SCCP messages to the phone. Tip Because this feature consumes resources, be sure to check
                                                         						  this check box only when you are experiencing signaling delays. | Tip | Because this feature consumes resources, be sure to check
                                                         						  this check box only when you are experiencing signaling delays. |
| Tip | Because this feature consumes resources, be sure to check
                                                         						  this check box only when you are experiencing signaling delays. |

| Tip | Because this feature consumes resources, be sure to check
                                                         						  this check box only when you are experiencing signaling delays. |
|---|---|

| Field | Description |
|---|---|
| Calling Party Transformation CSS | This setting allows you to localize the calling party number on the device. Make sure that the Calling Party Transformation
                                             CSS that you choose contains the calling party transformation pattern that you want to assign to this device. |
| Use Device Pool Calling Party Transformation CSS | To use the Calling Party Transformation CSS that is configured in the device pool that is assigned to this device, check this
                                             check box. If you do not check this check box, the device uses the Calling Party Transformation CSS that you configured in
                                             the Trunk Configuration window. |

| Field | Description |
|---|---|
| Calling Party Transformation CSS | From the drop-down list box, choose the calling search space (CSS) that contains the calling party transformation pattern
                                             that you want to apply on the remote calling number for calls received on this device. |
| Use Device Pool Calling Party Transformation CSS | Check this check box to apply the Calling Party Transformation CSS configured at the device pool to which this device belongs
                                             to transform the remote calling and remote connected number. |

| Field | Description |
|---|---|
| BLF Presence Group | From the drop-down list box, choose a Busy Lamp Field (BLF) presence group for the end user. The selected group specifies
                                             the destinations that the end user can monitor The default value for BLF Presence Group specifies Standard Presence group, configured with installation. BLF Presence Groups
                                             that are configured in Cisco Unified Administration also appear in the drop-down list box. |
| Device Security Profile | Choose the security profile to apply to the device. You must apply a security profile to all devices that are configured in Cisco Unified Communications Manager Administration. |
| SUBSCRIBE Calling Search Space | Supported with the Presence feature, the SUBSCRIBE calling search space determines how Cisco Unified Communications Manager
                                             routes presence requests that come from the end user. This setting allows you to apply a calling search space separate from
                                             the call-processing search space for presence (SUBSCRIBE) requests for the end user. From the drop-down list, choose the SUBSCRIBE calling search space to use for presence requests for the end user. All calling
                                             search spaces that you configure in Cisco Unified Communications Manager Administration display in the SUBSCRIBE Calling Search
                                             Space drop-down list. If you do not select a different calling search space for the end user from the drop-down list, the SUBSCRIBE calling search
                                             space defaults to None. To configure a SUBSCRIBE calling search space specifically for this purpose, you can configure a calling search space as you
                                             do all calling search spaces. |
| Unattended Port | Check this check box to indicate an unattended port on this device. |

| Field | Description |
|---|---|
| MLPP Domain | From the drop-down list, choose an Multilevel Precedence and Preemption (MLPP) domain to associate with this device. If you
                                             leave this field blank, this device inherits its MLPP domain from the value that is set for the device pool. If the device
                                             pool does not have an MLPP Domain setting, this device inherits its MLPP Domain from the value that is set for the MLPP Domain
                                             Identifier enterprise parameter. The default value for MLPP Domain specifies None. |
| Confidential Access Mode | From the drop-down list box, select one of the following options to set the Confidential Access Level mode: Fixed—Confidential Access Level value has higher precedence over call completion. Variable—Call completion has higher precedence over CAL level. |
| Confidential Access Level | Select the appropriate Confidential Access Level value from the drop-down list box. |

| Field | Description |
|---|---|
| Do Not Disturb | Check this check box to enable Do Not Disturb on the remote device. |
| DND Option | When you enable DND, Call Reject option specifies that no incoming call information gets presented to the user. Depending
                                             on how you configure the DND Incoming Call Alert parameter, the device may play a beep or display a flash notification of
                                             the call. |
| DND Incoming Call Alert | When you enable the DND Ringer Off or Call Reject option, this parameter specifies how a call displays on the device. From the drop-down list, choose one of the following options: None—This option specifies that the DND Incoming Call Alert setting from the Common Phone Profile window gets used for this
                                                   device Disable—This option disables both beep and flash notification of a call, but, for the DND Ringer Off option, incoming call
                                                   information still gets displayed. For the DND Call Reject option, no call alerts display, and no information gets sent to
                                                   the device. Beep Only—For an incoming call, this option causes the device to play a beep tone only. Flash Only—For an incoming call, this option causes the device to display a flash alert. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . The Find and List Phones window appears. |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the Phone Type drop down list, select H.323 Client
                                       			 and click Next . The Phone Configuration window appears. |
| Step 4 | Configure the fields in the Phone Configuration window. See the Related
                                       			 Topics section for more information about the fields and their configuration
                                       			 options. |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . The Find and List Phones window appears. |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the Phone Type drop down list, select Cisco IP Communicator and
                                       			 click Next . |
| Step 4 | From the Select the device protocol drop-down list, select either SCCP or SIP and
                                       			 click Next . The Phone Configuration window appears. |
| Step 5 | Configure the  following mandatory fields in the Phone Configuration window. Device Name —enter a name to identify the Cisco IP Communicator device. Device Pool –—choose the device pool to which you want this phone assigned. The
                                                device pool defines sets of common characteristics for devices,
                                                such as region, date/time group, and softkey template. Phone Button Template —choose the appropriate phone button template. The phone button
                                                template determines the configuration of buttons on a phone and
                                                identifies which feature (line, speed dial, and so on) is used for
                                                each button. Owner User ID —from the drop-down list box, choose the user ID of the assigned
                                                phone user. Device Security Profile –—choose the security profile to apply to the device. You can use default configuration for the remaining fields. See the online help for more information about the fields and
                                          their configuration options. |
| Step 6 | Click Save . |
| Step 7 | In the Association area, click Line [1] - Add a new DN . |
| Step 8 | In the Directory Number field, enter the directory number that you want to associate with the phone. |
| Step 9 | Click Save . |