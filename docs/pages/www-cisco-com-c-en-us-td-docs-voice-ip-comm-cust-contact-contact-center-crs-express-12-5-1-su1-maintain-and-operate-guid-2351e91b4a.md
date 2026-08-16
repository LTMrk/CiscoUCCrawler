---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su1-maintain-and-operate-guid-2351e91b4a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su1/maintain_and_operate/guide/uccx_b_1251su1admin-and-operations-guide/uccx_b_12_5_2admin-and-operations-guide_chapter_0111.html
retrieved_at: 2026-08-16T21:38:34.367497+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)SU1

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)SU1

Updated: January 31, 2021

Chapter: Telephony and Media Provision

## Chapter: Telephony and Media Provision

# Telephony and Media Provision

## Unified CCX Telephony and Media

The Unified CCX system uses a telephony resource called
                              		  Computer Telephony Interface (CTI) ports to accept incoming calls and to place
                              		  outbound calls. The Unified CCX system uses the following media resources to
                              		  provide interactive services for calls:

Unified CM Telephony—The Unified CCX Engine uses the Unified CM
                                    				Telephony subsystem to send and receive calls from the Unified CM by interfacing with
                                    				the CTI Manager through the Unified CM Telephony client.

Cisco Media Termination (CMT)—The CMT channels provide media
                                    				terminations in the Unified CCX for Unified CM Telephony Call Contacts.
                                    				These channels enable the Unified CCX to play media to the connected party.
                                    				DTMF digits are received out of band by the Unified CM Telephony subsystem.

MRCP Automated Speech Recognition (MRCP ASR)—The ASR media
                                    				resource allows callers to use speech to navigate menus and to provide other
                                    				information to Unified CCX applications.

MRCP Text-To-Speech (MRCP TTS)—The TTS media resource enables
                                    				Unified CCX applications to play back documents to callers as speech.

Media resources are licensed and sold as Unified IP IVR ports.
                                                				  Although you can provision more channels than you are licensed for, licensing
                                                				  is enforced at run-time. If more channels are provisioned than licensed, the
                                                				  system will not accept the extra calls, because doing so would violate your
                                                				  licensing agreements.

The Unified CCX system uses groups to share telephony and media resources among different
                              		  applications:

Call control groups allow you to control how the system
                                    				uses CTI ports. For example, you can reserve more ports for higher-priority
                                    				applications or provide access to fewer ports for applications with less
                                    				traffic.

Media resource groups allow you to share media resources
                                    				among different applications. For example, you can share ASR media resource
                                    				groups with applications that collect caller information and applications that
                                    				transfer calls to specific extensions.

The Unified CCX system also uses triggers , which are specified signals that invoke application
                              		  scripts in response to incoming contacts.

### Media Termination
                           	 Groups

Media
                                 		  termination groups are associated with CTI port groups.

For Unified CM deployment, you can create and use additional CTI port groups as required.

If a CTI
                                 		  port group is selected to support media termination and if the number of
                                 		  channels are identical to both groups, the CTI port group is automatically
                                 		  created in the background. This auto creation feature eliminates the manual CTI
                                 		  port group creation process.

If you
                                 		  choose to override media termination, the call control channel chooses the
                                 		  media termination automatically. If you want to select a new dialog group, you
                                 		  can have more than one media termination option. The options are used in the
                                 		  order that is displayed in the drop-down list.

### Channels Required to
                           	 Process Calls

Unified CCX
                                 		  needs two types of channels to process calls:

A call control
                                          				  channel , which is provisioned through the Unified CM Telephony subsystem
                                       				and corresponds to CTI port resources in Unified CM.

A media
                                          				  channel , which is provisioned through either the CMT subsystem or the MRCP
                                       				subsystem and corresponds to the kernel resources for handling the media voice
                                       				path with the caller.

MRCP channels
                                                   				  also correspond to additional resources on the MRCP server for performing
                                                   				  speech recognition.

Unified CCX
                                 		  needs access to a channel of each type to successfully process a call. However,
                                 		  the capabilities of the two channel types are not identical.

For
                                 		  example, consider a Unified CCX system provisioned with a single Unified CM
                                 		  Telephony call control channel (that is, a CTI port) and a single CMT channel.
                                 		  The system can handle one call at a time; when that call terminates, the system
                                 		  must reinitialize the channel resources before it can accept another call.

However,
                                 		  the time each channel takes to reinitialize is not equal—CMT channels take more
                                 		  time to reinitialize than CTI ports. For example:

The Unified CM
                                       				Telephony call control channel may take approximately 1 millisecond to
                                       				reinitialize.

The CMT channel
                                       				may take approximately 200 milliseconds to reinitialize.

This
                                 		  example implies that the system will not be able to accept a new incoming call
                                 		  for 200 milliseconds after the first call terminates; although the Unified CM
                                 		  Telephony channel is available after one millisecond, the CMT channel is not
                                 		  and Unified CCX needs both channels to process a call.

Such a
                                 		  delay can become an issue when a Unified CCX system is experiencing a high load
                                 		  condition or needs to handle a burst of incoming calls. Consequently, CMT
                                 		  channels require a higher channel count provisioning.

Tip

To provision
                                             			 Unified CCX systems to handle burst calls equally among all required resources,
                                             			 you must configure approximately 10 percentage more CMT channels than CTI
                                             			 ports, and approximately 10 percentage more MRCP channels than ASR licenses.

### Provision Telephony and Media Resources

To provision telephony and media resources, complete the
                                 		  following tasks:

Step 1

Provision the Unified CM Telephony subsystem.

Unified CM Telephony subsystem controls telephony resources for
                                             				Unified CCX system.

Step 2

Provision the CiscoMedia subsystem.

CiscoMedia subsystem controls CMT media resources for Unified CCX
                                             				system.

Step 3

Provision the MRCPASR subsystem.

MRCPASR subsystem controls ASR media resources for Unified CCX
                                             				system.

Step 4

Provision the MRCP TTS subsystem.

MRCP TTS subsystem controls TTS media resources for Unified CCX
                                             				system.

## Provision Unified CM
                        	 Telephony Subsystem

The Unified
                              		  CM Telephony subsystem is the subsystem of the Unified CCXEngine that sends
                              		  and receives call-related messages from the Unified CM CTI Manager through the
                              		  Unified CM Telephony client. To enable your Unified CCX server to handle Cisco
                              		  Unified Communications requests, you must provision the Unified CM Telephony
                              		  subsystem. The Unified CM Telephony subsystem is available in all the Unified
                              		  CCX license packages.

In previous versions of Unified CCX, it was necessary to configure Unified CM Telephony information using Unified CM. In Unified
                                          CCX, Unified CM Telephony configuration tasks are performed directly through Unified CCX Administration web pages.

To
                              		  provision the Unified CM Telephony subsystem, complete the following tasks:

Step 1

Configure a
                                       			 Unified CM Telephony Provider, if not already configured. Specify the server on
                                       			 which Unified CM CTI
                                       			 Manager is running, and provide a Unified CM user ID and password.

Step 2

Provision
                                       			 Unified CM Telephony call control groups.

Unified CM
                                          				Telephony call control groups pool together a series of CTI ports, which the
                                          				system then uses to serve calls as they arrive at the Unified CCX server.

Step 3

Provision a
                                       			 Unified CM Telephony trigger.

Unified CM
                                          				Telephony triggers invoke application scripts in response to incoming contacts.

Step 4

Resynchronize
                                       			 Unified CM Telephony versions.

### Resynchronize Cisco JTAPI Client

During the resynchronizing process, an additional check
                                 		  ensures that the Unified CM Telephony Client (also known as the Cisco JTAPI
                                 		  Client) are the same between the clients installed on the Unified CCX node and
                                 		  the Cisco Unified CM. If the Unified CCX detects a mismatch, the system
                                 		  downloads and installs the required version of Cisco JTAPI Client.

To resynchronize and view the status of Cisco JTAPI client,
                                 		  complete the following steps.

Step 1

Choose Subsystems > Cisco
                                                				  Unified CM Telephony > Cisco JTAPI
                                                				  Resync from the Unified CCX Administration menu bar.

Step 2

The Cisco JTAPI Resync web page opens, displaying the status of
                                          			 Cisco JTAPI Client resynchronization.

At this point, if there is an incompatible version, it
                                             				automatically downloads the new client.

### Resynchronize
                           	 Unified CM Telephony Data

This
                                 		  resynchronizing process ensures that the Unified CM Telephony user, the call
                                 		  control groups, and the triggers match the data of Unified CM being used.

To
                                 		  resynchronize the Unified CM Telephony data, complete the following steps.

From the Unified
                                          			 CCX Administration menu bar, choose Subsystems > Cisco Unified CM
                                                				  Telephony > Data Synchronization .

The Cisco
                                             				Unified CM Telephony Data Synchronization web page opens after
                                             				resynchronization, displaying the Data Resync status of Unified CM Telephony
                                             				Port Groups and Unified CM Telephony Triggers.

### Configure Unified CM
                           	 Telephony Provider

The
                                 		  Unified CM Telephony Provider web page is a read-only page that displays the
                                 		  latest configured information.

Caution

Some setups may
                                             			 prevent the Unified CM directory administrator from creating new Unified CM
                                             			 Telephony providers in a multiserver configuration. If this setup applies to
                                             			 you, be sure to delete preexisting Unified CM Telephony providers before
                                             			 creating new Unified CM Telephony providers. For example, if the Unified CM
                                             			 Telephony provider prefix is cmtelephony and you have a two-server configuration
                                             			 ( node_id1 and node_id2 ), you must delete both cmtelephony_<node_id1> and cmtelephony_<node_id2> . If you do not verify and
                                             			 delete preexisting Unified CM Telephony providers, the Unified CM Telephony
                                             			 subsystem issues an error and will not allow you to create Unified CM Telephony
                                             			 providers from the Unified CM Telephony Provider Configuration web page.

Step 1

Choose Subsystems > Cisco Unified CM
                                                				  Telephony > Provider from the Unified CCX
                                          			 Administration menu bar.

The Cisco
                                             				Unified CM Telephony Provider web page opens.

The following table describes the read-only fields displayed in the Unified CM Telephony Provider Configuration web page.

Field Heading

Description

Primary Unified CM Telephony Provider

IP address of the Server, running Unified CM CTI Manager in the cluster. This is usually the first CTI Manager or Cisco Unified
                                                         CM Telephony Provider selected by the Unified CCX user for Unified CM Telephony subsystem using System > Cisco Unified CM Configuration web page.

Secondary Unified CM Telephony Provider

IP address of the second Server, running Unified CM CTI Manager in the cluster. This is usually the second CTI Manager or
                                                         Cisco Unified CM Telephony Provider selected by the Unified CCX user for Unified CM Telephony subsystem using System > Cisco Unified CM Configuration web page.

If you have selected only one Unified CM Telephony provider, this field will be blank.

User Prefix

User prefix for the Unified CM user IDs created in Unified CM.

Step 2

To modify the
                                          			 Unified CM Telephony subsystem, click Modify
                                             				Cisco Unified CM Telephony Provider Information icon that displays
                                          			 in the tool bar in the upper left corner of the window. The Cisco Unified CM
                                          			 Configuration web page opens.

### Add New Call Control
                           	 Group

The Unified CCX system uses Unified CM Telephony call control groups to create a series of CTI ports. The system uses the
                                 CTI ports to serve calls as they arrive at or depart from the Unified CCX server. You can create multiple Unified CM Telephony
                                 call control groups to share and limit the resources that are used by specific applications.

To configure a new Unified CM Telephony call control group,
                                 		  complete the following steps.

Step 1

From the Unified CCX Administration menu bar, choose Subsystems > Unified CM
                                                				  Telephony > Call Control Group .

The Cisco Unified CM Telephony Call Control Group Configuration
                                             				web page opens, which displays the existing Unified CM Telephony Call Control
                                             				Group information, if any.

Step 2

Click the Add New icon that is displayed in the tool bar in the upper left corner of the window or the Add New button at the bottom of the window to create a new CTI port. The Cisco Unified CM Telephony Call Control Group Configuration
                                          web page opens.

You can create only one call control group of the Outbound type, in which the number of CTI ports must be always equal to
                                                         or greater than the licensed Outbound IVR ports.

Create the CTI ports through the Publisher for both nodes in a HA over WAN deployment.

Step 3

Use this web page to specify the following information:

Group Information

Group ID

Corresponds to the trunk group number reported to Cisco
                                                         							 Unified Intelligent Contact Management Enterprise (Unified ICME) when the
                                                         							 Unified CCX server is part of the Unified ICME solution. The value for this
                                                         							 field is automatically generated.

Description

Description of the Group ID. Press the Tab key to automatically populate the Description
                                                         							 field.

Group Information (continued)

Number of CTI Ports

Number of CTI ports assigned to the call control group. This is a mandatory field.

If you have a Premium
                                                         							 license with an Outbound license, you can create only one Outbound call control
                                                         							 group with a minimum licensed number of IVR ports or more. The number of CTI
                                                         							 ports for an outbound type of call control group can be modified but not below
                                                         							 the licensed ports for Outbound IVR. This rule does not apply to inbound type
                                                         							 call control groups. You can continue to create more inbound type call control
                                                         							 groups.

Media Termination Support

Enables the auto-creation of media termination groups.
                                                         							 This is a mandatory field.

Yes = Provides automatic media termination if the CTI
                                                         							 port group is successful.

No = Media termination port group is not created
                                                         							 (default).

Group Type

Select the group type for the call control group using this radio button. The choices are Inbound and Outbound. This is a
                                                         mandatory field and Inbound radio button is enabled by default. You cannot change the group type from Outbound to Inbound
                                                         and conversely. The Outbound type call control group will be displayed only if you have uploaded the Outbound license on top
                                                         of the premium license in your Unified CCX.

Directory Number Information

Device Name Prefix

The Device Name Prefix (DNP) given to all of the CTI ports in this group. This is a mandatory field.

The CTI ports for this port group are restricted to a maximum of 5 characters and has the following format:

<deviceprefix> _ <directoryno>

For example, if the Device Name Prefix is CTP and the starting Directory Number is 7000, the CTI port that is created in Unified
                                                         CM can have the device name CTP_7000.

Select Server for Telephony Port Group Configuration (displayed only in a HA over WAN deployment).

Select Server

This field is displayed only in a HA over WAN deployment
                                                         							 and it displays the different Unified CCX nodes that are available in a HA over
                                                         							 WAN deployment in a drop-down list.

In a HA over WAN setup, you need to configure directory information along with Unified CM-specific information for the ports
                                                         in each node. Once you select a node, all configuration details displayed below this field will be specific to the selected
                                                         node only. So, if you update any node-specific parameters (below the Select Server field), it will be applicable only to the ports specific to the selected node. But, if you update any configuration data
                                                         above the Select Server field, it will be applicable for the ports in both the nodes except for the Number of s field.

After you configure the data for the selected node and click Add or Update , the updated configuration information will be saved. For detailed information on behavior in HA over WAN scenario, refer
                                                         to the Solution Design Guide for
                                                                  				  Cisco Unified Contact Center Express https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_implementation_design_guides_list.html . In case of LAN deployment, this field is not displayed, as the same configuration data will be applicable for both the nodes
                                                         in the cluster.

Directory Number Information

Starting Directory Number

A unique phone
                                                         							 number. The Starting Directory Number contains numerals, and can have an
                                                         							 asterisk (*) or a hash (#), or both as a prefix or a suffix. To support E.164
                                                         							 compliance, Unified CCX allows you to add the plus sign (+) before the
                                                         							 directory number. The specified number of ports will be created starting from
                                                         							 the value specified in this field. The Directory Number that you enter can
                                                         							 appear in more than one partition. This is a mandatory field.

Device Pool

Set of common characteristics for devices, such as
                                                         							 region, date/time group, softkey template, and MLPP information to which you
                                                         							 want to assign this phone.

In a HA over WAN setup, you need to configure directory
                                                         							 information along with Unified CM-specific information for the ports in each
                                                         							 node. Once you select a node, all configuration details displayed below this
                                                         							 field will be specific to the selected node only. So, if you update any
                                                         							 node-specific parameters (below the Select Server field), it will be
                                                         							 applicable only to the ports specific to the selected node. But, if you update
                                                         							 any configuration data above the Select Server field, it will be
                                                         							 applicable for the ports in both the nodes except for the Number of CTI Ports field.

DN Calling Search Space

A collection of partitions that are searched to
                                                         							 determine how a dialed number should be routed. The calling search space for
                                                         							 the device and the calling search space for the directory number get used
                                                         							 together. The directory number calling search space takes precedence over the
                                                         							 device calling search space.

For more information, see the System Configuration Guide for Cisco Unified Communications Manager .

Location

The Cisco Unified Communications phone location setting
                                                         							 specifies the total bandwidth that is available for calls to and from this
                                                         							 location. A location setting of HUB_NONE means that the location feature does not
                                                         							 keep track of the bandwidth that this Cisco Unified Communications phone
                                                         							 consumes.

Advanced Directory Number Information (only
                                                         							 available if you click Show More )

Directory Number (continued)

Alerting Name ASCII

This information is automatically populated based on the
                                                         							 configuration in the Unified CM setup and displays the ASCII name filed used in
                                                         							 one of the following situations:

If the device is not capable of handling the Unicode strings

If the locals on endpoint devices do not match

If the Unicode string is not specified

Redirect Calling Search Space

A collection of partitions that are searched to
                                                         							 determine how a redirected call is routed.

Redirect Calling Search Space options:

DN Calling Search Space— This option enables the CTI port to use its directory number CSS when performing a redirect transfer.

Calling Party— This option enables the CTI port to use the calling party's CSS when performing a redirect / consult transfer.

Redirect Party— This option enables the CTI port to use the CTI port's CSS to control the redirect.

Media Resource Group List

A prioritized grouping of media resource groups. An
                                                         							 application chooses the required media resource, such as a Music On Hold
                                                         							 server, from the available media resources according to the priority order that
                                                         							 is defined in a Media Resource Group List.

If you choose <none>, Unified CM uses the Media
                                                         							 Resource Group that is defined in the device pool.

Directory Number Setting

Voice Mail Profile

A list of profiles defined in the Voice Mail Profile
                                                         							 Configuration.

The first option is <None>, which is the current
                                                         							 default Voice Mail Profile that is configured in the Voice Mail Profile
                                                         							 Configuration.

Presence Group

See the Cisco Unified
                                                                  				  Communications Manager Administration Guide for detailed information on how to configure presence groups.

Require DTMF Reception

A Unified CM radio button to determine if DTMF reception
                                                         							 is required. Yes is selected by default. If you select No, a warning message is
                                                         							 displayed.

AAR Group

Automated Alternate Routing (AAR) group for this device.
                                                         							 The AAR group provides the prefix digits that are used to route calls that are
                                                         							 otherwise blocked due to insufficient bandwidth. An AAR group setting of
                                                         							 <None> specifies that no rerouting of blocked calls will be attempted.

User Hold Audio Source

Audio source heard by the caller when the Unified CCX
                                                         							 Script places the caller on Hold by using the Hold Step (when you press the
                                                         							 hold key).

Network Hold Audio Source

Audio source heard by the caller when Unified CCX performs a Consult Transfer (when Unified CCX calls an agent). Use this
                                                         entry for the .wav file (for example, a .wav file playing a ringback tone) to be played to the caller during this Consult
                                                         Transfer.

Call Forward and Pickup Settings

Call Pickup Group

The number that can be dialed to answer calls to this
                                                         							 directory number in the specified partition.

Display

Use a maximum of 30 alphanumeric characters. Typically,
                                                         							 use the user name or the directory number (if you use the directory number, the
                                                         							 person receiving the call may not see the proper identity of the caller).

Leave this field blank to have the system display the
                                                         							 extension.

External Phone Number Mask

Phone number (or mask) that is used to send Caller ID
                                                         							 information when a call is placed from this line.

You can enter a maximum of 24 number, the international
                                                         							 escape character +, *, # and "X" characters. The X characters represent the
                                                         							 directory number and must appear at the end of the pattern. For example, if you
                                                         							 specify a mask of 972813XXXX, an external call from extension 1234 displays a
                                                         							 caller ID number of 9728131234.

Step 4

Click Add or Save .

The Unified CM Telephony Call Control Group Configuration summary web page opens. The corresponding CTI ports are created
                                             in the Unified CM Telephony call control group. The new call control group appears in the list of call control groups in the
                                             Cisco Unified CM Telephony Call Control Group Configuration web page.

### Add Unified CM
                           	 Telephony Trigger

You must
                                 		  configure Unified CM Telephony triggers to invoke application scripts in
                                 		  response to incoming contacts. A Unified CM Telephony trigger responds to calls
                                 		  that arrive on a specific route point by selecting telephony and media
                                 		  resources to serve the call and invoking an application script to handle the
                                 		  call. The Unified CM Telephony triggers are available with all Unified CCX
                                 		  license packages.

Unified CM
                                 		  Telephony trigger settings include:

Session information, such as the application to associate with the trigger, Maximum Number of sessions allowed, and the Idle Timeout
                                       value.

CTI information, such as a CTI port device and CTI route points for each call Unified CCX simultaneously places or accepts.

Directory Number information, such as the Voice Mail Profile and Calling Search Space.

Call Forward and Pickup instructions.

To add and
                                 		  configure a Unified CM Telephony trigger, complete the following steps.

Step 1

From the Unified
                                          			 CCX Administration menu bar, choose Subsystems > Cisco Unified CM
                                                				  Telephony > Triggers .

The Unified CM
                                             				Telephony Trigger Configuration web page opens displaying the following fields.

Field

Description

Route
                                                         							 Point

Available CTI route point, which is the directory number
                                                         							 associated with the trigger.

Application

Application name to associate with the trigger.

Sessions

Maximum number of simultaneous calls that the trigger can
                                                         							 handle.

Enabled

True
                                                         							 if the trigger is enabled; False if the trigger is disabled.

If you try to
                                                         				  delete a trigger associated with an outbound call control group, then the
                                                         				  campaigns associated with the trigger become invalid and the application also
                                                         				  gets deleted. In such cases, when you click the Delete icon or button, a dialog box opens to confirm your action. Click OK if you want to delete the trigger and
                                                         				  disassociate the campaigns associated with it. If you delete a trigger and
                                                         				  navigate to the Campaign Configuration web page, you will also see an alert
                                                         				  regarding the missing trigger association for that campaign.

Step 2

Click the Add
                                             				New icon that is displayed in the tool bar in the upper left corner
                                          			 of the window or the Add
                                             				New button that is displayed at the bottom of the window.

The Unified CM
                                             				Telephony Trigger Configuration web page opens.

Step 3

Use this web
                                          			 page to specify the following mandatory fields:

Field

Description

Directory Information

Directory Number

A
                                                         							 unique phone number. To support E.164 compliance, Unified CCX allows you to add
                                                         							 a plus sign (+) before the agent extension or a route point directory number
                                                         							 followed by 15 characters which consist of numerals and the following special
                                                         							 characters: uppercase letter X, hash (#), square brackets ([ ]), hyphen (-),
                                                         							 and asterisk (*).

Supports only route point directory numbers and Finesse agent and supervisor extensions.

+1234 and 1234 are two different directory numbers.

The square brackets ([ ]) enclose a range of values.

For more information, see the "Wildcards and Special Characters in Route Patterns and Hunt Pilots" section in the System Configuration Guide for Cisco Unified Communications Manager .

Examples:

Valid directory numbers—+1223* or *#12#*

Invalid directory numbers—91X+ or +-12345

Use of two(2) wildcard CTI Route Points that overlap
                                                                     								with each other is not supported. For example, Route Point 1: 123XXXX and Route
                                                                     								Point 2: 1234XXX overlap with one another and is not supported.

However, a wildcard CTI Route point can overlap with
                                                                     								a full DID (best match pattern) that doesn't contain a wildcard. For example,
                                                                     								Route Point 1: 123XXXX and Route Point 2: 1234567 is supported.

Trigger Information

Language

Choose the default language to associate with the incoming call
                                                         							 when the application is started from this drop-down menu.

To
                                                                     								add a Language option, click Edit button. The User Prompt dialog box opens. Enter
                                                                     								a locale string value and click OK . The User Prompt dialog box closes, and the name
                                                                     								of the language opens in the Language field in the Unified CM Telephony
                                                                     								Configuration web page.

Application Name

From
                                                         							 the drop-down menu, choose the application to associate with the trigger.

Device Name

A
                                                         							 unique identifier for this device, consisting of alphanumeric characters, dots,
                                                         							 dashes, or underscores.

Description

A
                                                         							 descriptive name for the CTI route point.

Call
                                                         							 Control Group

Choose the call control group to associate with the trigger from
                                                         							 this drop-down menu. For Outbound IVR Dialer, you must select the call control
                                                         							 group from Outbound type call control group list. The route point should be
                                                         							 created on Unified CM. Once you assign the Outbound group for a trigger, you
                                                         							 cannot change it to an Inbound group and vice versa.

Advanced Configuration (available only if you click Show More ).

Advanced Trigger
                                                            								Information

Enabled

Radio buttons to choose the required option:

Yes— enable the trigger (default)

No— disable the trigger.

Maximum Number of Sessions

The
                                                         							 maximum number of simultaneous calls that this trigger can handle. The number
                                                         							 is actually governed by the Unified CM (10,000 for each separate line). However in Unified CCX, this number is
                                                         							 restricted to the maximum number of sessions. Any call after this number is
                                                         							 exceeded gets the busy tone.

Idle
                                                         							 Timeout (in ms)

The
                                                         							 number of milliseconds (ms) the system should wait before rejecting the Unified
                                                         							 CM Telephony request for this trigger.

Override Media Termination

Radio buttons to choose the required options:

Yes— Override media
                                                         							 termination.

No— Enable media
                                                         							 termination (default).

If
                                                         							 you select Yes, two panes open:

Selected Dialog Groups displays the default or selected group.

Available Dialog Groups lists the configured dialog.

CTI Route Point
                                                            								Information

Alerting Name ASCII

This
                                                         							 information is automatically populated based on the configuration in the
                                                         							 Unified CM setup and displays the ASCII name filed used in one of the following
                                                         							 situations:

If the device is not capable of handling the Unicode strings

If the locals on endpoint devices do not match

If the Unicode string is not specified

Device Pool

The
                                                         							 device pool to which you want to assign this route point. A device pool defines
                                                         							 sets of common characteristics for devices, such as region, date/time group,
                                                         							 softkey template, and MLPP information.

Location

The
                                                         							 total bandwidth that is available for calls to/from this location. A location
                                                         							 setting of HUB_NONE indicates that the locations feature does not keep
                                                         							 track of the bandwidth used by this route point.

Directory Number Settings

Partition

The
                                                         							 partition to which the Directory Number belongs. The Directory Number field
                                                         							 value must be unique within the partition that you choose.

If
                                                         							 you do not want to restrict access to the Directory Number, select < None > as the
                                                         							 partition setting.

Voice Mail Profile

A
                                                         							 list of profiles defined in the Voice Mail Profile Configuration.

The
                                                         							 first option is < None >, which is the current default Voice Mail Profile
                                                         							 that is configured in the Voice Mail Profile Configuration.

Calling Search Space

A
                                                         							 collection of partitions that are searched for numbers that are called from
                                                         							 this directory number. The specified value applies to all devices that use this
                                                         							 directory number.

For
                                                         							 example, assume you have two calling search spaces: Building and PSTN. Building
                                                         							 only allows users to call within the building, while PSTN allows users to call
                                                         							 both in and outside the building. You could assign the phone to the Building
                                                         							 calling search space and the line on your phone to the PSTN calling search
                                                         							 space. For more information, see the System Configuration Guide for Cisco Unified Communications Manager .

Calling Search Space for Redirect

By
                                                         							 default, Cisco Unified Communications Manager uses the original calling party's
                                                         							 calling search space (CSS) to process the redirected call from a Unified CCX
                                                         							 Trigger to a Unified CCX CTI Port. This default behavior requires the partition
                                                         							 of the Unified CCX CTI ports to be a member of the original calling party's CSS
                                                         							 even if the partition of the CTI Route Point/Unified CCX Trigger is accessible
                                                         							 to the calling device's CSS and the CSS of the CTI Route Point/Unified CCX
                                                         							 Trigger contains the partition of the Unified CCX CTI Ports.

You
                                                         							 can modify this behavior using the drop-down list to instruct Cisco Unified
                                                         							 Communications Manager which CSS to use when redirecting the call from the CTI
                                                         							 Route Point to the CTI Port.

Calling Search Space for Redirect options:

Default
                                                                  									 Calling Search Space— CSS of the calling device

Calling
                                                                  									 Address Search Space— CSS of the calling device

Route
                                                                  									 Point Address Search Space— CSS of the CTI Route Point (Trigger)

Presence Group

A
                                                         							 list of groups to integrate the device with the iPass server. The device/line
                                                         							 information is provided for integrating applications.

Call Forward and Pickup
                                                            								Settings

Forward Busy

Check one of the following options:

Voice Mail— Check this
                                                         							 box to use settings in the Voice Mail Profile Configuration window.

When this box is checked, Unified CM ignores the settings in the
                                                                     								Destination box and Calling Search Space.

Destination— To use any
                                                         							 disable phone number, including an outside destination.

Calling Search Space— To apply the above setting all devices that are using this directory number.

For limiting the number of calls per application in Unified CCX system, see the Unified CM Telephony Triggers for Unified CCX Queuing section.

Display

Use
                                                         							 a maximum of 30 alphanumeric characters. Typically, use the user name or the
                                                         							 directory number (if using the directory number, the person receiving the call
                                                         							 may not see the proper identity of the caller). Leave this field blank to have
                                                         							 the system display an extension.

External Phone Number Mask

Phone number (or mask) that is used to send Caller ID
                                                         							 information when a call is placed from this line.

You
                                                         							 can enter a maximum of 24 number, the international escape character +, *, #
                                                         							 and "X" characters. The X characters represent the directory number and must
                                                         							 appear at the end of the pattern. For example, if you specify a mask of
                                                         							 972813XXXX, an external call from extension 1234 displays a caller ID number of
                                                         							 9728131234.

Step 4

Click Add or Save to save the changes. The specified route point
                                          			 is created on the Unified CM.

The Unified CM
                                             				Telephony Trigger Configuration web page opens and displays the new Unified CM
                                             				Telephony trigger.

## Additional Unified CM Telephony Information

This section includes the following topics:

Unified CM Telephony Triggers for Unified CCX Queuing

Unified CM Telephony Information Resynchronization

### Unified CM Telephony
                           	 Triggers for Unified CCX Queuing

When
                                 		  limiting the number of calls per application in Unified CCX applications, you
                                 		  need to take care to coordinate the Unified CM Telephony trigger Maximum Number
                                 		  of Sessions limit with the Media Group session limit.

For
                                 		  example, if you are using Unified CCX for queuing calls and set the Unified CM
                                 		  Telephony trigger Maximum Number of Sessions limit on Unified CCX to 4 and set
                                 		  the Call Forward and Pickup Settings to send the fifth call to voice mail. To
                                 		  make this happen, you must configure the Media Group Session Limit to the
                                 		  identical setting (4). This will cause Unified CM to forward the next incoming
                                 		  call to voice mail (once the CTI New Call Accept timer setting expires).

The
                                 		  disadvantage of this approach is that you need to define more media groups for
                                 		  each application and you cannot share the same set of media groups across
                                 		  multiple applications.

### Unified CM Telephony
                           	 Information Resynchronization

If the Unified CM Telephony information (Unified CM Telephony users, CTI ports, triggers, SRTP) in the Unified CM is missing
                                 or not in sync with Unified CCX data, choose Subsystems > Cisco Unified CM Telephony > Data Resync from the Unified CCX Administration menu bar. Unified CCX checks whether:

The Unified CM
                                       				Telephony users exist in Unified CM.

All the ports
                                       				belonging to the Port Group exist in Unified CM.

The port group's
                                       				data is in sync with Ports data in Unified CM.

The ports'
                                       				association to users are correct.

The route point
                                       				exists in Unified CM.

The triggers
                                       				data is in sync with the Route Point data in the Unified CM.

The route points
                                       				have been associated with all the Unified CM Telephony users in Unified CM.

The Unified CM configuration is in sync with Unified CCX for SRTP.

Unified CCX
                                 		  synchronizes the data by:

Creating any
                                       				missing users

Creating any
                                       				missing ports

Modifying
                                       				out-of-sync ports

Associating CTI Ports to Unified CM Telephony users. (For example, associating CTI Ports created for Node 1 to the Unified
                                       CM Telephony User for Node 1, and so on.)

Creating any
                                       				missing route points

Modifying
                                       				out-of-sync route points

Associating
                                       				route points to all the Unified CM Telephony users.

Modifying Unified CM configuration, such as user roles and CAPF profiles for JTAPI telephony users to match SRTP configuration.

## Cisco Media
                        	 Subsystem

The Cisco
                           		Media subsystem is a subsystem of the Unified CCX Engine. The Cisco Media
                           		subsystem manages the CMT media resource. CMT channels are required for Unified
                           		CCX to be able to play or record media.

The Cisco
                           		Media subsystem uses dialog groups to
                           		organize and share resources among applications. A dialog group is a pool of dialog channels in which each channel is used to perform dialog
                              		  interactions with a caller, during which the caller responds to automated
                           		prompts by pressing buttons on a touch-tone phone.

The built-in
                                       		  grammars and grammar options that are supported by Unified CCX when using an
                                       		  MRCP dialog channel is determined by the MRCP speech software you purchase. See
                                       		  the software vendor for information about what built-in grammars and features
                                       		  are supported.

To enable
                           		your Unified CCX applications to handle simple DTMF-based dialog interactions
                           		with customers, you must provision the Cisco Media subsystem to configure CMT
                           		dialog groups.

Caution

All media
                                       		  termination strings begin with auto and contain
                                       		  the same ID as the call control group—not the CMT dialog group. If the default
                                       		  media termination is configured and the ID differs, follow the procedure
                                       		  provided in the Add CMT Dialog
                                          			 Control Group .

### Add CMT Dialog
                           	 Control Group

To add a
                                 		  CMT dialog control group, complete the following steps.

Step 1

From the Unified
                                          			 CCX Administration menu bar, choose Subsystems > Cisco
                                                				  Media .

The Cisco Media Termination Dialog Group Configuration web page opens. Any preconfigured entry is listed on this page with
                                             the following information:

Field

Description

GroupID

The unique Group ID associated with the media.

Description

CMT group description.

The ID in this field need not necessarily match the CMT group ID.

Channels

Number of channels associated with the group.

Step 2

Click Add
                                             				New icon at the top or Add
                                             				New button at the bottom of the window. The Cisco Media Termination
                                          			 Dialog Group Configuration web page opens.

By default, a
                                                         				  Unified CM Telephony Call Control Group with Group ID 0 is created.

Step 3

Use this web
                                          			 page to specify the following fields.

Field

Description

Group
                                                         							 ID

A
                                                         							 Group ID value unique within all media group identifiers, including ASR group
                                                         							 identifiers. This is a mandatory field.

Description

Description for the Cisco Media Termination Dialog group.

Number
                                                         							 of Licensed IVR ports

Number
                                                         							 of licensed IVR ports. Display only.

Maximum Number Of Channels

Maximum number of channels associated with this group. This is a
                                                         							 mandatory field.

You
                                                                     								can specify any value for Maximum Number Of Channels, but restrictions are
                                                                     								placed on the system when a call is made. This restriction is imposed by the
                                                                     								number of licensed IVR ports on your system. This is a mandatory field.

Step 4

Click Add icon that displays in the tool bar in the upper
                                          			 left corner of the window or the Add button that displays at the bottom of the
                                          			 window.

The CMT Dialog
                                             				Group Configuration web page opens, displaying the new CMT dialog group.

You are now
                                             				ready to provision MRCP ASR and MRCP TTS subsystems.

## ASR and TTS in Unified CCX

### Prepare to Provision
                           	 ASR/TTS

It is the
                                 		  responsibility of the customer to perform the following tasks:

Order ASR/TTS speech servers from Cisco-supported vendors.

Work with the ASR/TTS vendor to size the solutions.

Provision, install, and configure the ASR/TTS vendor software on a different server (in the same LAN) and not where the Unified
                                       CCX runs.  (see the Unified CCX Compatibility related information, located at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html .).

Before uploading a ASR/TTS script to Unified CCX Administration, validate the script against the capabilities and specifications
                                       supported by the ASR/TTS vendor.

### Provision of MRCP ASR Subsystem

The MRCP ASR subsystem allows users to navigate through a menu
                              		of options by speaking instead of pressing keys on a touch-tone telephone. When
                              		a user calls local directory assistance, for example, ASR can prompt the user
                              		to say the city and state in which to locate the information, then connect the
                              		user to an appropriate operator.

To provision the MRCP ASR subsystem, define the following
                              		information:

MRCP ASR Providers —Information about the vendor of your
                                    			 speech server, including the number of licenses and the grammar type.

MRCP ASR Servers —Information about the ASR server’s name,
                                    			 port location, and available languages.

MRCP ASR Groups — Information about the MRCP ASR dialog
                                    			 control groups and associated locales, which enable Unified CCX applications to
                                    			 use speech recognition.

#### Provision MRCP ASR
                              	 Providers

Use the
                                    		  MRCP ASR Provider Configuration web page to specify information about the
                                    		  vendor of your speech server.

Step 1

From the Unified
                                             			 CCX Administration menu bar, choose Subsystem > MRCP
                                                   				  ASR > MRCP ASR Providers .

The MRCP ASR
                                                				Provider Configuration web page opens, displaying the list of currently
                                                				configured MRCP providers, licenses, and the corresponding status.

Step 2

Click Add
                                                				New icon that displays in the tool bar in the upper left corner of
                                             			 the window or the Add
                                                				New button that is displayed at the bottom of the window.

The MRCP ASR
                                                				Provider Configuration web page opens.

Step 3

Specify the
                                             			 following mandatory fields:

Field

Description

Provider Name

Enter
                                                            							 the name of the MRCP ASR provider supported by Unified CCX.

Number
                                                            							 of Provider Licenses

The
                                                            							 number of ASR port licenses purchased from the ASR vendor.

Grammar Variant

Vendor-specific grammar setting. Valid options:

Nuance Open Speech Recognizer servers version 9.0 and above (OSR 3.1.x)

Nuance 11.x and below version ASR servers (Nuance)

IBM WVS ASR servers (2003 SISR)

Step 4

Click Add icon in the tool bar in the upper left corner of
                                             			 the window or the Add button that displays at the bottom of this
                                             			 window to apply changes.

After you update MRCP ASR/TTS Providers, Servers, and Groups, the corresponding provider needs to be refreshed for changes
                                                            to take effect. The Unified CCX Engine does not need to be restarted. However, during a Refresh, Unified CM Telephony triggers
                                                            using affected groups will fall back to the dialog group that is configured and the MRCP Provider being refreshed will go
                                                            NOT_CONFIGURED until the reload is complete.

Your changes
                                                				appear in the MRCP ASR Providers List page. You are now ready to provision MRCP
                                                				ASR Servers.

If you delete
                                                            				  an ASR/TTS provider and all of its associated servers and then create a new
                                                            				  ASR/TTS provider, its status might become IN_SERVICE immediately, even before
                                                            				  you create any servers for it. In this situation, click Refresh for that ASR/TTS provider, or click Refresh All. These actions change the status of the
                                                            				  ASR/TTS provider to NOT_CONFIGURED.

#### Provision MRCP ASR Servers

Use the MRCP ASR Server Configuration web page to specify information about the speech server's name, port location, and available
                                    language.

You must have an MRCP ASR Provider defined before you can provision an MRCP ASR Server.

Step 1

From the Unified CCX Administration menu bar, choose Subsystem > MRCP ASR > MRCP ASR Servers .

The MRCP ASR Server Configuration web page opens, displaying a list of previously configured servers, if applicable with the
                                                following information:

Column

Description

Computer Name

Hostname or IP address in which the ASR server software is installed.

ASR server deployment over WAN is not supported in Unified CCX. The ASR server should be in the same LAN where Unified CCX
                                                                        is. You need to specify the ASR server hostname or IP address that is local with the Unified CCX node while installing the
                                                                        ASR server software in this field.

Provider

The MRCP ASR Provider to which this server is associated.

Port

The default TCP port number that is used to connect to a MRCP server.

OSR 3.1.x—4900 for MRCPv1 and 5060 for MRCPv2

2003 SISR—554

Nuance—554

Status

Status or state of the subsystem.

Step 2

Click Add New icon that is displayed in the tool bar in the upper, left corner of the window or the Add New button that is displayed at the bottom of the window to provision a new MRCP ASR Server.

The MRCP ASR Server Configuration web page opens.

Step 3

Use this web page to specify the following fields.

Field

Description

Server Name

Hostname or IP address of the server where the MRCP ASR server software is installed.

Provider Name

Select the name of the MRCP ASR Provider to which this server is associated from this drop-down list.

Port Number

The default TCP port number that is used to connect to a MRCP server. Though the default value is shown as 4900. You need
                                                            to provide any one of the following values in this field based on the TCP provider or grammar variant you have selected while
                                                            configuring an MRCP ASR provider:

OSR 3.1.x—4900 for MRCPv1 and 5060 for MRCPv2

2003 SISR—554

Nuance—554

Locales

Languages supported by the ASR Provider. Select a language (or multiple languages) from the drop-down list and click Add Language ; the selected language appears with a check box in the Enabled Languages list.

Use the check box to enable or disable a language.

Step 4

Click Add to apply changes.

Your changes appear in the MRCP ASR Server list web page. You are now ready to provision MRCP ASR Groups.

#### Provision MRCP ASR Dialog Groups

Use the MRCP Groups Configuration web page to specify
                                    		  information about MRCP ASR dialog control groups, which enable Unified CCX
                                    		  applications to use speech recognition.

You must have a MRCP ASR Provider defined before you can provision a
                                                			 MRCP ASR Group. Also, you should configure MRCP ASR Servers for the specific
                                                			 MRCP Provider before configuring the MRCP ASR Groups. This allows users to
                                                			 configure languages for the groups based on the languages supported by the
                                                			 configured servers.

Step 1

From the Unified CCX Administration menu bar, choose Subsystem > MRCP
                                                   				  ASR > MRCP ASR Dialog Groups .

The MRCP ASR Dialog Group Configuration web page opens to display a list of preconfigured entries, if applicable with the
                                                following information:

Field

Description

Group ID

Identifier for the group.

Description

Description of this dialog group.

Provider

Name of the MRCP ASR provider.

Channels

Maximum number of sessions.

This web page also displays the Number of Licensed IVR
                                                				Channels.

Step 2

Click Add New icon that displays in the tool bar in
                                             			 the upper, left corner of the window or the Add New button that displays at the bottom of
                                             			 the window to provision a MRCP ASR Group.

The MRCP ASR Dialog Group Configuration web page opens.

Step 3

Use this web page to specify the following fields:

Field

Description

Group ID

Associated group ID.

Description

Description of this dialog group.

Tip

Number Of Provider Licenses

Display only.

Number Of Licensed IVR Ports

Display only.

Maximum Number Of sessions

Maximum number of sessions associated with this dialog
                                                            							 group.

You can assign any value for Maximum Number Of
                                                                        								Channels, but restrictions are placed on the system when a call is made. This
                                                                        								restriction is imposed by the number of licensed IVR ports on your system.

Caution

Under heavy load, calls that utilize a channel from an
                                                                        								MRCP ASR Dialog Control Group, might have a reduced call completion rate as the
                                                                        								MRCP channels used by calls can take some additional time to clean up all the
                                                                        								sessions set up with MRCP resources. To address this situation, you can
                                                                        								overprovision the value of this field by a factor of 1.2 or by an additional 20
                                                                        								percent. For example, if your application requires 100 MRCP ASR channels, modify the value in this field to be 120
                                                                        MRCP ASR channels.

Provider Name

Select a MRCP Provider name from the drop-down list that
                                                            							 contains a list of all previously defined provider names.

Enabled Languages

Select the languages that you wish to configure for this
                                                            							 group from the list displayed.

The displayed languages represent the locales configured
                                                            							 for all MRCP ASR servers for the specified provider. If there are no MRCP ASR
                                                            							 servers configured, no languages are displayed. In this case, you must update the group configuration once MRCP ASR
                                                            servers have been configured for
                                                            							 the specified provider.

Step 4

Click Add to apply changes.

Your changes appear in the MRCP ASR Groups list web page.

### MRCP TTS Subsystem

The MRCP TTS subsystem converts plain text (UNICODE) into
                              		spoken words to provide a user with information, or prompt a user to respond to
                              		an action.

For example, a company might use TTS to read back a
                              		customer's name, address, and telephone number for verification before the
                              		company ships a requested product to the customer's location. Or a
                              		customer might dial into a pre-designated phone number, access a voice portal,
                              		and listen to the latest weather report or stock quotes. TTS can also convert
                              		email text to speech and play it back to the customer over telephone.

To provision the MRCP TTS subsystem, define the following
                              		information:

MRCP TTS Providers —Information about the vendor of your TTS
                                    			 system.

If you delete an ASR/TTS provider and all of its associated
                                                				servers and then create a new ASR/TTS provider, its status might become
                                                				IN_SERVICE immediately, even before you create any servers for it. In this
                                                				situation, click Refresh for that ASR/TTS provider, or click Refresh All. These
                                                				actions change the status of the ASR/TTS provider to NOT_CONFIGURED.

MRCP TTS Servers —Information about the TTS server's
                                    			 name, port location, and available languages.

MRCP TTS Default Genders —Information about the default gender
                                    			 setting for the Locales specified during TTS Server provisioning.

You will need at least one MRCP TTS Provider for each vendor requiring
                                          		  TTS server installation.

#### Provision MRCP TTS Providers

Use the MRCP TTS Providers Configuration web page to specify
                                    		  information about the vendor of your TTS server.

After you update MRCP ASR/TTS Providers, Servers, and Groups, the
                                                			 corresponding provider needs to be refreshed for changes to take effect. The
                                                			 Unified CCX Engine does not need to be restarted. However, during a Refresh,
                                                			 Unified CM Telephony triggers using affected groups will fall back to the
                                                			 dialog group that is configured and the MRCP Provider being refreshed will go
                                                			 NOT_CONFIGURED until the reload is complete.

Step 1

From the Unified CCX Administration menu bar, choose Subsystems > MRCP
                                                   				  TTS > MRCP TTS Provider .

The MRCP TTS Provider Configuration web page opens. If providers
                                                				are already configured, this page lists the provider name and corresponding
                                                				status.

Step 2

Click Add New icon that displays in the tool bar in
                                             			 the upper, left corner of the window or the Add New button that displays at the bottom of
                                             			 the window.

Use this web page to specify the MRCP TTS Provider supported by
                                                				Unified CCX.

The MRCP TTS Provider Configuration web page reopens. The Provider
                                                				Name drop-down list displays the existing MRCP TTS Providers. Choose the MRCP
                                                				TTS Provider supported by Unified CCX from this list.

Support for High Availability and remote servers is available
                                                            				  only in multiple-server deployments.

Step 3

Click Add to apply changes.

Your changes appear in the MRCP TTS Provider Configuration web
                                                				page. You are now ready to provision MRCP TTS Servers.

##### Configure Default
                                 	 TTS Provider for Unified CCX System

Optionally, you can configure a default TTS provider. The Unified CCX Prompt Manager uses the default TTS provider for rendering
                                       TTS prompts if a TTS provider is not configured in the TTS Prompt. This usually happens in the case of VXML applications.
                                       For additional information on supported VXML tags for Unified CCX, see Cisco Unified Contact
                                                				  Center Express Getting Started with Scripts and for supported grammars see Cisco Unified Contact
                                                				  Center Express Editor Step Reference Guide .

To
                                       		  configure a default TTS provider, follow these steps.

Step 1

Choose System > System
                                                      				  Parameters .

Step 2

In the Default
                                                			 TTS Provider drop down list below Media Parameters section, select the provider
                                                			 you wish to be the system default. You must select only a preconfigured TTS
                                                			 provider as the Default TTS Provider.

If you are deploying an VXML applications and the only TTS functionality you need is to play pre-recorded .wav files, select the Cisco LiteSSMLProcessor option as the Default TTS Provider. This option allows you to run SSML that has .wav file references in them.

Step 3

Click Update .

#### Provision MRCP TTS
                              	 Servers

Use the
                                    		  MRCP TTS Servers Configuration web page to configure the TTS server's name,
                                    		  port location, and available languages.

You need
                                    		  at least one MRCP TTS Server associated with each configured provider.

You must have an MRCP TTS Provider defined before you can provision an MRCP TTS Server.

Step 1

From the Unified
                                             			 CCX Administration menu bar, choose Subsystems > MRCP
                                                   				  TTS > MRCP TTS Server .

The MRCP TTS
                                                				Server Configuration web page opens, displaying a list of previously configured
                                                				servers, if applicable, with the following information:

Column

Description

Computer Name

Hostname or IP address of the server in which the TTS server software is installed.

TTS server deployment over WAN is not supported in Unified CCX. In other words, the TTS server should be in the same LAN where
                                                                        Unified CCX is. Thus, you need to specify the TTS server hostname or IP address that is local with the Unified CCX node while
                                                                        installing the TTS server software in this field.

Port

TCP port number used to connect to an MRCP server. Following are the different TCP Provider names:

MRCP Server

Nuance Vocalizer

Scansoft Realspeak

Provider

The
                                                            							 MRCP TTS Provider to which this server is associated.

Status

Status
                                                            							 or state of the subsystem.

Step 2

Click Add MRCP
                                                				TTS Server icon that displays in the tool bar in the upper, left
                                             			 corner of the window or the Add
                                                				New button that displays at the bottom of the window to provision a
                                             			 new MRCP ASR Server.

The MRCP TTS
                                                				Server Configuration web page opens.

Step 3

Specify the
                                             			 following fields:

Field

Description

Server
                                                            							 Name

Hostname or IP address of the server the MRCP TTS server software is installed.

Provider Name

Select
                                                            							 the name of the MRCP TTS Provider to which this server is associated from this
                                                            							 drop-down list.

Port
                                                            							 Number

The default TCP port number used to connect to a MRCP TTS server. The port number is automatically displayed based on the
                                                            provider or grammar variant that you have selected while configuring an MRCP TTS provider. Following are the different TCP
                                                            Provider names along with their port numbers:

MRCP Server—554

Nuance Vocalizer—4900 for MRCPv1 and 5060 for MRCPv2

Scansoft Realspeak—4900

Locales

Languages supported by the TTS Provider. Select a language (or
                                                            							 multiple languages) from the drop-down list and click Add Language ; the selected language appears in the
                                                            							 Enabled Language list.

Use
                                                                        								the check box to disable/enable a language.

Step 4

Click Add to apply changes.

Your changes
                                                				appear in the MRCP TTS Server Configuration web page. You are now ready to
                                                				provision MRCP TTS Default Genders.

Whenever a new language is added for an MRCP Server—and if this is the first instance of this language being added for the
                                                            corresponding MRCP Provider—then the default gender for that locale and for the specified provider is set to Neutral. You
                                                            should check the MRCP Locales page to review the default genders that are set automatically per locale per provider. Default
                                                            genders are used when a prompt for a specific locale is used without specifying any gender.

#### Provision MRCP TTS Default Genders

Use the MRCP TTS Default Genders Configuration web page to
                                    		  configure the default gender settings per Locale per Provider. TTS uses default
                                    		  genders when a prompt for a specific locale is used without specifying the
                                    		  gender.

Step 1

From the Unified CCX Administration menu bar, choose Subsystems > MRCP
                                                   				  TTS > MRCP TTS Default Genders .

The MRCP TTS Default Gender Configuration web page opens,
                                                				displaying the default genders currently configured for each locale for every
                                                				MRCP TTS Provider that is currently configured.

Step 2

Optionally, change the default gender setting for each locale for
                                             			 each provider.

The Locale radio button has the Male, Female, or Neutral
                                                            				  options. By default, the "Default Gender" is set to "Neutral" unless configured explicitly.

Step 3

Click Update to apply changes.

The system updates the default gender setting for each Locale per
                                                				Provider.

| Note | Media resources are licensed and sold as Unified IP IVR ports.
                                                				  Although you can provision more channels than you are licensed for, licensing
                                                				  is enforced at run-time. If more channels are provisioned than licensed, the
                                                				  system will not accept the extra calls, because doing so would violate your
                                                				  licensing agreements. |
|---|---|

| Note | For Unified CM deployment, you can create and use additional CTI port groups as required. |
|---|---|

| Note | MRCP channels
                                                   				  also correspond to additional resources on the MRCP server for performing
                                                   				  speech recognition. |
|---|---|

| Tip | To provision
                                             			 Unified CCX systems to handle burst calls equally among all required resources,
                                             			 you must configure approximately 10 percentage more CMT channels than CTI
                                             			 ports, and approximately 10 percentage more MRCP channels than ASR licenses. |
|---|---|

| Step 1 | Provision the Unified CM Telephony subsystem. Unified CM Telephony subsystem controls telephony resources for
                                             				Unified CCX system. |
|---|---|
| Step 2 | Provision the CiscoMedia subsystem. CiscoMedia subsystem controls CMT media resources for Unified CCX
                                             				system. |
| Step 3 | Provision the MRCPASR subsystem. MRCPASR subsystem controls ASR media resources for Unified CCX
                                             				system. |
| Step 4 | Provision the MRCP TTS subsystem. MRCP TTS subsystem controls TTS media resources for Unified CCX
                                             				system. |

| Note | In previous versions of Unified CCX, it was necessary to configure Unified CM Telephony information using Unified CM. In Unified
                                          CCX, Unified CM Telephony configuration tasks are performed directly through Unified CCX Administration web pages. |
|---|---|

| Step 1 | Configure a
                                       			 Unified CM Telephony Provider, if not already configured. Specify the server on
                                       			 which Unified CM CTI
                                       			 Manager is running, and provide a Unified CM user ID and password. |
|---|---|
| Step 2 | Provision
                                       			 Unified CM Telephony call control groups. Unified CM
                                          				Telephony call control groups pool together a series of CTI ports, which the
                                          				system then uses to serve calls as they arrive at the Unified CCX server. |
| Step 3 | Provision a
                                       			 Unified CM Telephony trigger. Unified CM
                                          				Telephony triggers invoke application scripts in response to incoming contacts. |
| Step 4 | Resynchronize
                                       			 Unified CM Telephony versions. |

| Step 1 | Choose Subsystems > Cisco
                                                				  Unified CM Telephony > Cisco JTAPI
                                                				  Resync from the Unified CCX Administration menu bar. |
|---|---|
| Step 2 | The Cisco JTAPI Resync web page opens, displaying the status of
                                          			 Cisco JTAPI Client resynchronization. At this point, if there is an incompatible version, it
                                             				automatically downloads the new client. |

| From the Unified
                                          			 CCX Administration menu bar, choose Subsystems > Cisco Unified CM
                                                				  Telephony > Data Synchronization . The Cisco
                                             				Unified CM Telephony Data Synchronization web page opens after
                                             				resynchronization, displaying the Data Resync status of Unified CM Telephony
                                             				Port Groups and Unified CM Telephony Triggers. |
|---|

| Caution | Some setups may
                                             			 prevent the Unified CM directory administrator from creating new Unified CM
                                             			 Telephony providers in a multiserver configuration. If this setup applies to
                                             			 you, be sure to delete preexisting Unified CM Telephony providers before
                                             			 creating new Unified CM Telephony providers. For example, if the Unified CM
                                             			 Telephony provider prefix is cmtelephony and you have a two-server configuration
                                             			 ( node_id1 and node_id2 ), you must delete both cmtelephony_<node_id1> and cmtelephony_<node_id2> . If you do not verify and
                                             			 delete preexisting Unified CM Telephony providers, the Unified CM Telephony
                                             			 subsystem issues an error and will not allow you to create Unified CM Telephony
                                             			 providers from the Unified CM Telephony Provider Configuration web page. |
|---|---|

| Step 1 | Choose Subsystems > Cisco Unified CM
                                                				  Telephony > Provider from the Unified CCX
                                          			 Administration menu bar. The Cisco
                                             				Unified CM Telephony Provider web page opens. The following table describes the read-only fields displayed in the Unified CM Telephony Provider Configuration web page. Field Heading Description Primary Unified CM Telephony Provider IP address of the Server, running Unified CM CTI Manager in the cluster. This is usually the first CTI Manager or Cisco Unified
                                                         CM Telephony Provider selected by the Unified CCX user for Unified CM Telephony subsystem using System > Cisco Unified CM Configuration web page. Secondary Unified CM Telephony Provider IP address of the second Server, running Unified CM CTI Manager in the cluster. This is usually the second CTI Manager or
                                                         Cisco Unified CM Telephony Provider selected by the Unified CCX user for Unified CM Telephony subsystem using System > Cisco Unified CM Configuration web page. Note If you have selected only one Unified CM Telephony provider, this field will be blank. User Prefix User prefix for the Unified CM user IDs created in Unified CM. | Field Heading | Description | Primary Unified CM Telephony Provider | IP address of the Server, running Unified CM CTI Manager in the cluster. This is usually the first CTI Manager or Cisco Unified
                                                         CM Telephony Provider selected by the Unified CCX user for Unified CM Telephony subsystem using System > Cisco Unified CM Configuration web page. | Secondary Unified CM Telephony Provider | IP address of the second Server, running Unified CM CTI Manager in the cluster. This is usually the second CTI Manager or
                                                         Cisco Unified CM Telephony Provider selected by the Unified CCX user for Unified CM Telephony subsystem using System > Cisco Unified CM Configuration web page. Note If you have selected only one Unified CM Telephony provider, this field will be blank. | Note | If you have selected only one Unified CM Telephony provider, this field will be blank. | User Prefix | User prefix for the Unified CM user IDs created in Unified CM. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Field Heading | Description |
| Primary Unified CM Telephony Provider | IP address of the Server, running Unified CM CTI Manager in the cluster. This is usually the first CTI Manager or Cisco Unified
                                                         CM Telephony Provider selected by the Unified CCX user for Unified CM Telephony subsystem using System > Cisco Unified CM Configuration web page. |
| Secondary Unified CM Telephony Provider | IP address of the second Server, running Unified CM CTI Manager in the cluster. This is usually the second CTI Manager or
                                                         Cisco Unified CM Telephony Provider selected by the Unified CCX user for Unified CM Telephony subsystem using System > Cisco Unified CM Configuration web page. Note If you have selected only one Unified CM Telephony provider, this field will be blank. | Note | If you have selected only one Unified CM Telephony provider, this field will be blank. |
| Note | If you have selected only one Unified CM Telephony provider, this field will be blank. |
| User Prefix | User prefix for the Unified CM user IDs created in Unified CM. |
| Step 2 | To modify the
                                          			 Unified CM Telephony subsystem, click Modify
                                             				Cisco Unified CM Telephony Provider Information icon that displays
                                          			 in the tool bar in the upper left corner of the window. The Cisco Unified CM
                                          			 Configuration web page opens. |

| Field Heading | Description |
|---|---|
| Primary Unified CM Telephony Provider | IP address of the Server, running Unified CM CTI Manager in the cluster. This is usually the first CTI Manager or Cisco Unified
                                                         CM Telephony Provider selected by the Unified CCX user for Unified CM Telephony subsystem using System > Cisco Unified CM Configuration web page. |
| Secondary Unified CM Telephony Provider | IP address of the second Server, running Unified CM CTI Manager in the cluster. This is usually the second CTI Manager or
                                                         Cisco Unified CM Telephony Provider selected by the Unified CCX user for Unified CM Telephony subsystem using System > Cisco Unified CM Configuration web page. Note If you have selected only one Unified CM Telephony provider, this field will be blank. | Note | If you have selected only one Unified CM Telephony provider, this field will be blank. |
| Note | If you have selected only one Unified CM Telephony provider, this field will be blank. |
| User Prefix | User prefix for the Unified CM user IDs created in Unified CM. |

| Note | If you have selected only one Unified CM Telephony provider, this field will be blank. |
|---|---|

| Step 1 | From the Unified CCX Administration menu bar, choose Subsystems > Unified CM
                                                				  Telephony > Call Control Group . The Cisco Unified CM Telephony Call Control Group Configuration
                                             				web page opens, which displays the existing Unified CM Telephony Call Control
                                             				Group information, if any. |
|---|---|
| Step 2 | Click the Add New icon that is displayed in the tool bar in the upper left corner of the window or the Add New button at the bottom of the window to create a new CTI port. The Cisco Unified CM Telephony Call Control Group Configuration
                                          web page opens. Note You can create only one call control group of the Outbound type, in which the number of CTI ports must be always equal to
                                                         or greater than the licensed Outbound IVR ports. Create the CTI ports through the Publisher for both nodes in a HA over WAN deployment. | Note | You can create only one call control group of the Outbound type, in which the number of CTI ports must be always equal to
                                                         or greater than the licensed Outbound IVR ports. Create the CTI ports through the Publisher for both nodes in a HA over WAN deployment. |
| Note | You can create only one call control group of the Outbound type, in which the number of CTI ports must be always equal to
                                                         or greater than the licensed Outbound IVR ports. Create the CTI ports through the Publisher for both nodes in a HA over WAN deployment. |
| Step 3 | Use this web page to specify the following information: Page Area Field Description Group Information Group ID Corresponds to the trunk group number reported to Cisco
                                                         							 Unified Intelligent Contact Management Enterprise (Unified ICME) when the
                                                         							 Unified CCX server is part of the Unified ICME solution. The value for this
                                                         							 field is automatically generated. Note If a Stop icon appears beside the Group ID (on the Cisco Unified CM Call Control Group Configuration list page), it indicates
                                                                  that the data is invalid or out of sync with Unified CM data; if a Head icon appears, the group is valid. Description Description of the Group ID. Press the Tab key to automatically populate the Description
                                                         							 field. Group Information (continued) Number of CTI Ports Number of CTI ports assigned to the call control group. This is a mandatory field. If you have a Premium
                                                         							 license with an Outbound license, you can create only one Outbound call control
                                                         							 group with a minimum licensed number of IVR ports or more. The number of CTI
                                                         							 ports for an outbound type of call control group can be modified but not below
                                                         							 the licensed ports for Outbound IVR. This rule does not apply to inbound type
                                                         							 call control groups. You can continue to create more inbound type call control
                                                         							 groups. Note If this field is set to <n> , the system creates <n> ports for each Unified CCX Engine node (node in which Unified CCX Engine component is enabled). Media Termination Support Enables the auto-creation of media termination groups.
                                                         							 This is a mandatory field. Yes = Provides automatic media termination if the CTI
                                                         							 port group is successful. No = Media termination port group is not created
                                                         							 (default). Group Type Select the group type for the call control group using this radio button. The choices are Inbound and Outbound. This is a
                                                         mandatory field and Inbound radio button is enabled by default. You cannot change the group type from Outbound to Inbound
                                                         and conversely. The Outbound type call control group will be displayed only if you have uploaded the Outbound license on top
                                                         of the premium license in your Unified CCX. Directory Number Information Device Name Prefix The Device Name Prefix (DNP) given to all of the CTI ports in this group. This is a mandatory field. The CTI ports for this port group are restricted to a maximum of 5 characters and has the following format: <deviceprefix> _ <directoryno> For example, if the Device Name Prefix is CTP and the starting Directory Number is 7000, the CTI port that is created in Unified
                                                         CM can have the device name CTP_7000. Select Server for Telephony Port Group Configuration (displayed only in a HA over WAN deployment). Select Server This field is displayed only in a HA over WAN deployment
                                                         							 and it displays the different Unified CCX nodes that are available in a HA over
                                                         							 WAN deployment in a drop-down list. In a HA over WAN setup, you need to configure directory information along with Unified CM-specific information for the ports
                                                         in each node. Once you select a node, all configuration details displayed below this field will be specific to the selected
                                                         node only. So, if you update any node-specific parameters (below the Select Server field), it will be applicable only to the ports specific to the selected node. But, if you update any configuration data
                                                         above the Select Server field, it will be applicable for the ports in both the nodes except for the Number of s field. Note You need to ensure that the values in Number of s field for both the nodes are the same. If you modify this field, the number of ports is modified for the selected node only
                                                                  as the device pool selection for both nodes could be different in a HA over WAN deployment. If you click Add before updating this value for either of the node, the port group for that node will be marked with a red cross in the main
                                                                  Cisco Unified CM Telephony Call Control Group Configuration web page to signify the fact that the number of ports between
                                                                  the two nodes is different and the other node should also be updated. In such a scenario, click the hyperlink for the node
                                                                  that is tagged in red; and from the Cisco Unified CM Telephony Call Control Group Configuration page for the selected node,
                                                                  update the value in the Number of CTI Ports field and click Update to ensure the number of CTI ports for both the nodes are the same. After you configure the data for the selected node and click Add or Update , the updated configuration information will be saved. For detailed information on behavior in HA over WAN scenario, refer
                                                         to the Solution Design Guide for
                                                                  				  Cisco Unified Contact Center Express https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_implementation_design_guides_list.html . In case of LAN deployment, this field is not displayed, as the same configuration data will be applicable for both the nodes
                                                         in the cluster. Directory Number Information Starting Directory Number A unique phone
                                                         							 number. The Starting Directory Number contains numerals, and can have an
                                                         							 asterisk (*) or a hash (#), or both as a prefix or a suffix. To support E.164
                                                         							 compliance, Unified CCX allows you to add the plus sign (+) before the
                                                         							 directory number. The specified number of ports will be created starting from
                                                         							 the value specified in this field. The Directory Number that you enter can
                                                         							 appear in more than one partition. This is a mandatory field. Note When a pattern is used as a Directory Number, the phone display and the caller ID display on the dialed phone will contain
                                                                  characters other than digits. To avoid this, provide a value for Display (Internal Caller ID), Line Text Label, and External
                                                                  Phone Number Mask. Device Pool Set of common characteristics for devices, such as
                                                         							 region, date/time group, softkey template, and MLPP information to which you
                                                         							 want to assign this phone. Note The support for having multiple device pools associated with the call control group(s) has been withdrawn in Unified CCX.
                                                                  Manually assign a single device pool to each call control group if you have multiple device pools associated with call control
                                                                  group(s) in an older version of Unified CCX. In a HA over WAN setup, you need to configure directory
                                                         							 information along with Unified CM-specific information for the ports in each
                                                         							 node. Once you select a node, all configuration details displayed below this
                                                         							 field will be specific to the selected node only. So, if you update any
                                                         							 node-specific parameters (below the Select Server field), it will be
                                                         							 applicable only to the ports specific to the selected node. But, if you update
                                                         							 any configuration data above the Select Server field, it will be
                                                         							 applicable for the ports in both the nodes except for the Number of CTI Ports field. Note You need to ensure that the values in Number of CTI Ports field for both the nodes are the same. If you modify this field, the number of ports is modified for the selected node only
                                                                  as the device pool selection for both nodes could be different in a HA over WAN deployment. If you click Add before updating this value for either of the node, the port group for that node will be marked with a red cross in the main
                                                                  Cisco Unified CM Telephony Call Control Group Configuration web page to signify the fact that the number of ports between
                                                                  the two nodes is different and the other node should also be updated. In such a scenario, click the hyperlink for the node
                                                                  that is tagged in red; and from the Cisco Unified CM Telephony Call Control Group Configuration page for the selected node,
                                                                  update the value in the Number of CTI Ports field and click Update to ensure the number of CTI ports for both the nodes are the same. DN Calling Search Space A collection of partitions that are searched to
                                                         							 determine how a dialed number should be routed. The calling search space for
                                                         							 the device and the calling search space for the directory number get used
                                                         							 together. The directory number calling search space takes precedence over the
                                                         							 device calling search space. For more information, see the System Configuration Guide for Cisco Unified Communications Manager . Location The Cisco Unified Communications phone location setting
                                                         							 specifies the total bandwidth that is available for calls to and from this
                                                         							 location. A location setting of HUB_NONE means that the location feature does not
                                                         							 keep track of the bandwidth that this Cisco Unified Communications phone
                                                         							 consumes. Advanced Directory Number Information (only
                                                         							 available if you click Show More ) Directory Number (continued) Alerting Name ASCII This information is automatically populated based on the
                                                         							 configuration in the Unified CM setup and displays the ASCII name filed used in
                                                         							 one of the following situations: If the device is not capable of handling the Unicode strings If the locals on endpoint devices do not match If the Unicode string is not specified Redirect Calling Search Space A collection of partitions that are searched to
                                                         							 determine how a redirected call is routed. Redirect Calling Search Space options: Note DN Calling Search Space is deprecated. Use Calling Party or Redirect Party instead. DN Calling Search Space— This option enables the CTI port to use its directory number CSS when performing a redirect transfer. Calling Party— This option enables the CTI port to use the calling party's CSS when performing a redirect / consult transfer. Redirect Party— This option enables the CTI port to use the CTI port's CSS to control the redirect. Media Resource Group List A prioritized grouping of media resource groups. An
                                                         							 application chooses the required media resource, such as a Music On Hold
                                                         							 server, from the available media resources according to the priority order that
                                                         							 is defined in a Media Resource Group List. If you choose <none>, Unified CM uses the Media
                                                         							 Resource Group that is defined in the device pool. Directory Number Setting Voice Mail Profile A list of profiles defined in the Voice Mail Profile
                                                         							 Configuration. The first option is <None>, which is the current
                                                         							 default Voice Mail Profile that is configured in the Voice Mail Profile
                                                         							 Configuration. Presence Group See the Cisco Unified
                                                                  				  Communications Manager Administration Guide for detailed information on how to configure presence groups. Require DTMF Reception A Unified CM radio button to determine if DTMF reception
                                                         							 is required. Yes is selected by default. If you select No, a warning message is
                                                         							 displayed. AAR Group Automated Alternate Routing (AAR) group for this device.
                                                         							 The AAR group provides the prefix digits that are used to route calls that are
                                                         							 otherwise blocked due to insufficient bandwidth. An AAR group setting of
                                                         							 <None> specifies that no rerouting of blocked calls will be attempted. User Hold Audio Source Audio source heard by the caller when the Unified CCX
                                                         							 Script places the caller on Hold by using the Hold Step (when you press the
                                                         							 hold key). Network Hold Audio Source Audio source heard by the caller when Unified CCX performs a Consult Transfer (when Unified CCX calls an agent). Use this
                                                         entry for the .wav file (for example, a .wav file playing a ringback tone) to be played to the caller during this Consult
                                                         Transfer. Call Forward and Pickup Settings Call Pickup Group The number that can be dialed to answer calls to this
                                                         							 directory number in the specified partition. Display Use a maximum of 30 alphanumeric characters. Typically,
                                                         							 use the user name or the directory number (if you use the directory number, the
                                                         							 person receiving the call may not see the proper identity of the caller). Leave this field blank to have the system display the
                                                         							 extension. External Phone Number Mask Phone number (or mask) that is used to send Caller ID
                                                         							 information when a call is placed from this line. You can enter a maximum of 24 number, the international
                                                         							 escape character +, *, # and "X" characters. The X characters represent the
                                                         							 directory number and must appear at the end of the pattern. For example, if you
                                                         							 specify a mask of 972813XXXX, an external call from extension 1234 displays a
                                                         							 caller ID number of 9728131234. | Page Area | Field | Description | Group Information | Group ID | Corresponds to the trunk group number reported to Cisco
                                                         							 Unified Intelligent Contact Management Enterprise (Unified ICME) when the
                                                         							 Unified CCX server is part of the Unified ICME solution. The value for this
                                                         							 field is automatically generated. Note If a Stop icon appears beside the Group ID (on the Cisco Unified CM Call Control Group Configuration list page), it indicates
                                                                  that the data is invalid or out of sync with Unified CM data; if a Head icon appears, the group is valid. | Note | If a Stop icon appears beside the Group ID (on the Cisco Unified CM Call Control Group Configuration list page), it indicates
                                                                  that the data is invalid or out of sync with Unified CM data; if a Head icon appears, the group is valid. | Description | Description of the Group ID. Press the Tab key to automatically populate the Description
                                                         							 field. | Group Information (continued) | Number of CTI Ports | Number of CTI ports assigned to the call control group. This is a mandatory field. If you have a Premium
                                                         							 license with an Outbound license, you can create only one Outbound call control
                                                         							 group with a minimum licensed number of IVR ports or more. The number of CTI
                                                         							 ports for an outbound type of call control group can be modified but not below
                                                         							 the licensed ports for Outbound IVR. This rule does not apply to inbound type
                                                         							 call control groups. You can continue to create more inbound type call control
                                                         							 groups. Note If this field is set to <n> , the system creates <n> ports for each Unified CCX Engine node (node in which Unified CCX Engine component is enabled). | Note | If this field is set to <n> , the system creates <n> ports for each Unified CCX Engine node (node in which Unified CCX Engine component is enabled). | Media Termination Support | Enables the auto-creation of media termination groups.
                                                         							 This is a mandatory field. Yes = Provides automatic media termination if the CTI
                                                         							 port group is successful. No = Media termination port group is not created
                                                         							 (default). | Group Type | Select the group type for the call control group using this radio button. The choices are Inbound and Outbound. This is a
                                                         mandatory field and Inbound radio button is enabled by default. You cannot change the group type from Outbound to Inbound
                                                         and conversely. The Outbound type call control group will be displayed only if you have uploaded the Outbound license on top
                                                         of the premium license in your Unified CCX. | Directory Number Information | Device Name Prefix | The Device Name Prefix (DNP) given to all of the CTI ports in this group. This is a mandatory field. The CTI ports for this port group are restricted to a maximum of 5 characters and has the following format: <deviceprefix> _ <directoryno> For example, if the Device Name Prefix is CTP and the starting Directory Number is 7000, the CTI port that is created in Unified
                                                         CM can have the device name CTP_7000. | Select Server for Telephony Port Group Configuration (displayed only in a HA over WAN deployment). |  | Select Server | This field is displayed only in a HA over WAN deployment
                                                         							 and it displays the different Unified CCX nodes that are available in a HA over
                                                         							 WAN deployment in a drop-down list. In a HA over WAN setup, you need to configure directory information along with Unified CM-specific information for the ports
                                                         in each node. Once you select a node, all configuration details displayed below this field will be specific to the selected
                                                         node only. So, if you update any node-specific parameters (below the Select Server field), it will be applicable only to the ports specific to the selected node. But, if you update any configuration data
                                                         above the Select Server field, it will be applicable for the ports in both the nodes except for the Number of s field. Note You need to ensure that the values in Number of s field for both the nodes are the same. If you modify this field, the number of ports is modified for the selected node only
                                                                  as the device pool selection for both nodes could be different in a HA over WAN deployment. If you click Add before updating this value for either of the node, the port group for that node will be marked with a red cross in the main
                                                                  Cisco Unified CM Telephony Call Control Group Configuration web page to signify the fact that the number of ports between
                                                                  the two nodes is different and the other node should also be updated. In such a scenario, click the hyperlink for the node
                                                                  that is tagged in red; and from the Cisco Unified CM Telephony Call Control Group Configuration page for the selected node,
                                                                  update the value in the Number of CTI Ports field and click Update to ensure the number of CTI ports for both the nodes are the same. After you configure the data for the selected node and click Add or Update , the updated configuration information will be saved. For detailed information on behavior in HA over WAN scenario, refer
                                                         to the Solution Design Guide for
                                                                  				  Cisco Unified Contact Center Express https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_implementation_design_guides_list.html . In case of LAN deployment, this field is not displayed, as the same configuration data will be applicable for both the nodes
                                                         in the cluster. | Note | You need to ensure that the values in Number of s field for both the nodes are the same. If you modify this field, the number of ports is modified for the selected node only
                                                                  as the device pool selection for both nodes could be different in a HA over WAN deployment. If you click Add before updating this value for either of the node, the port group for that node will be marked with a red cross in the main
                                                                  Cisco Unified CM Telephony Call Control Group Configuration web page to signify the fact that the number of ports between
                                                                  the two nodes is different and the other node should also be updated. In such a scenario, click the hyperlink for the node
                                                                  that is tagged in red; and from the Cisco Unified CM Telephony Call Control Group Configuration page for the selected node,
                                                                  update the value in the Number of CTI Ports field and click Update to ensure the number of CTI ports for both the nodes are the same. | Directory Number Information | Starting Directory Number | A unique phone
                                                         							 number. The Starting Directory Number contains numerals, and can have an
                                                         							 asterisk (*) or a hash (#), or both as a prefix or a suffix. To support E.164
                                                         							 compliance, Unified CCX allows you to add the plus sign (+) before the
                                                         							 directory number. The specified number of ports will be created starting from
                                                         							 the value specified in this field. The Directory Number that you enter can
                                                         							 appear in more than one partition. This is a mandatory field. Note When a pattern is used as a Directory Number, the phone display and the caller ID display on the dialed phone will contain
                                                                  characters other than digits. To avoid this, provide a value for Display (Internal Caller ID), Line Text Label, and External
                                                                  Phone Number Mask. | Note | When a pattern is used as a Directory Number, the phone display and the caller ID display on the dialed phone will contain
                                                                  characters other than digits. To avoid this, provide a value for Display (Internal Caller ID), Line Text Label, and External
                                                                  Phone Number Mask. | Device Pool | Set of common characteristics for devices, such as
                                                         							 region, date/time group, softkey template, and MLPP information to which you
                                                         							 want to assign this phone. Note The support for having multiple device pools associated with the call control group(s) has been withdrawn in Unified CCX.
                                                                  Manually assign a single device pool to each call control group if you have multiple device pools associated with call control
                                                                  group(s) in an older version of Unified CCX. In a HA over WAN setup, you need to configure directory
                                                         							 information along with Unified CM-specific information for the ports in each
                                                         							 node. Once you select a node, all configuration details displayed below this
                                                         							 field will be specific to the selected node only. So, if you update any
                                                         							 node-specific parameters (below the Select Server field), it will be
                                                         							 applicable only to the ports specific to the selected node. But, if you update
                                                         							 any configuration data above the Select Server field, it will be
                                                         							 applicable for the ports in both the nodes except for the Number of CTI Ports field. Note You need to ensure that the values in Number of CTI Ports field for both the nodes are the same. If you modify this field, the number of ports is modified for the selected node only
                                                                  as the device pool selection for both nodes could be different in a HA over WAN deployment. If you click Add before updating this value for either of the node, the port group for that node will be marked with a red cross in the main
                                                                  Cisco Unified CM Telephony Call Control Group Configuration web page to signify the fact that the number of ports between
                                                                  the two nodes is different and the other node should also be updated. In such a scenario, click the hyperlink for the node
                                                                  that is tagged in red; and from the Cisco Unified CM Telephony Call Control Group Configuration page for the selected node,
                                                                  update the value in the Number of CTI Ports field and click Update to ensure the number of CTI ports for both the nodes are the same. | Note | The support for having multiple device pools associated with the call control group(s) has been withdrawn in Unified CCX.
                                                                  Manually assign a single device pool to each call control group if you have multiple device pools associated with call control
                                                                  group(s) in an older version of Unified CCX. | Note | You need to ensure that the values in Number of CTI Ports field for both the nodes are the same. If you modify this field, the number of ports is modified for the selected node only
                                                                  as the device pool selection for both nodes could be different in a HA over WAN deployment. If you click Add before updating this value for either of the node, the port group for that node will be marked with a red cross in the main
                                                                  Cisco Unified CM Telephony Call Control Group Configuration web page to signify the fact that the number of ports between
                                                                  the two nodes is different and the other node should also be updated. In such a scenario, click the hyperlink for the node
                                                                  that is tagged in red; and from the Cisco Unified CM Telephony Call Control Group Configuration page for the selected node,
                                                                  update the value in the Number of CTI Ports field and click Update to ensure the number of CTI ports for both the nodes are the same. | DN Calling Search Space | A collection of partitions that are searched to
                                                         							 determine how a dialed number should be routed. The calling search space for
                                                         							 the device and the calling search space for the directory number get used
                                                         							 together. The directory number calling search space takes precedence over the
                                                         							 device calling search space. For more information, see the System Configuration Guide for Cisco Unified Communications Manager . | Location | The Cisco Unified Communications phone location setting
                                                         							 specifies the total bandwidth that is available for calls to and from this
                                                         							 location. A location setting of HUB_NONE means that the location feature does not
                                                         							 keep track of the bandwidth that this Cisco Unified Communications phone
                                                         							 consumes. | Advanced Directory Number Information (only
                                                         							 available if you click Show More ) | Directory Number (continued) | Alerting Name ASCII | This information is automatically populated based on the
                                                         							 configuration in the Unified CM setup and displays the ASCII name filed used in
                                                         							 one of the following situations: If the device is not capable of handling the Unicode strings If the locals on endpoint devices do not match If the Unicode string is not specified | Redirect Calling Search Space | A collection of partitions that are searched to
                                                         							 determine how a redirected call is routed. Redirect Calling Search Space options: Note DN Calling Search Space is deprecated. Use Calling Party or Redirect Party instead. DN Calling Search Space— This option enables the CTI port to use its directory number CSS when performing a redirect transfer. Calling Party— This option enables the CTI port to use the calling party's CSS when performing a redirect / consult transfer. Redirect Party— This option enables the CTI port to use the CTI port's CSS to control the redirect. | Note | DN Calling Search Space is deprecated. Use Calling Party or Redirect Party instead. | Media Resource Group List | A prioritized grouping of media resource groups. An
                                                         							 application chooses the required media resource, such as a Music On Hold
                                                         							 server, from the available media resources according to the priority order that
                                                         							 is defined in a Media Resource Group List. If you choose <none>, Unified CM uses the Media
                                                         							 Resource Group that is defined in the device pool. | Directory Number Setting | Voice Mail Profile | A list of profiles defined in the Voice Mail Profile
                                                         							 Configuration. The first option is <None>, which is the current
                                                         							 default Voice Mail Profile that is configured in the Voice Mail Profile
                                                         							 Configuration. | Presence Group | See the Cisco Unified
                                                                  				  Communications Manager Administration Guide for detailed information on how to configure presence groups. | Require DTMF Reception | A Unified CM radio button to determine if DTMF reception
                                                         							 is required. Yes is selected by default. If you select No, a warning message is
                                                         							 displayed. | AAR Group | Automated Alternate Routing (AAR) group for this device.
                                                         							 The AAR group provides the prefix digits that are used to route calls that are
                                                         							 otherwise blocked due to insufficient bandwidth. An AAR group setting of
                                                         							 <None> specifies that no rerouting of blocked calls will be attempted. | User Hold Audio Source | Audio source heard by the caller when the Unified CCX
                                                         							 Script places the caller on Hold by using the Hold Step (when you press the
                                                         							 hold key). | Network Hold Audio Source | Audio source heard by the caller when Unified CCX performs a Consult Transfer (when Unified CCX calls an agent). Use this
                                                         entry for the .wav file (for example, a .wav file playing a ringback tone) to be played to the caller during this Consult
                                                         Transfer. | Call Forward and Pickup Settings | Call Pickup Group | The number that can be dialed to answer calls to this
                                                         							 directory number in the specified partition. | Display | Use a maximum of 30 alphanumeric characters. Typically,
                                                         							 use the user name or the directory number (if you use the directory number, the
                                                         							 person receiving the call may not see the proper identity of the caller). Leave this field blank to have the system display the
                                                         							 extension. | External Phone Number Mask | Phone number (or mask) that is used to send Caller ID
                                                         							 information when a call is placed from this line. You can enter a maximum of 24 number, the international
                                                         							 escape character +, *, # and "X" characters. The X characters represent the
                                                         							 directory number and must appear at the end of the pattern. For example, if you
                                                         							 specify a mask of 972813XXXX, an external call from extension 1234 displays a
                                                         							 caller ID number of 9728131234. |
| Page Area | Field | Description |
| Group Information | Group ID | Corresponds to the trunk group number reported to Cisco
                                                         							 Unified Intelligent Contact Management Enterprise (Unified ICME) when the
                                                         							 Unified CCX server is part of the Unified ICME solution. The value for this
                                                         							 field is automatically generated. Note If a Stop icon appears beside the Group ID (on the Cisco Unified CM Call Control Group Configuration list page), it indicates
                                                                  that the data is invalid or out of sync with Unified CM data; if a Head icon appears, the group is valid. | Note | If a Stop icon appears beside the Group ID (on the Cisco Unified CM Call Control Group Configuration list page), it indicates
                                                                  that the data is invalid or out of sync with Unified CM data; if a Head icon appears, the group is valid. |
| Note | If a Stop icon appears beside the Group ID (on the Cisco Unified CM Call Control Group Configuration list page), it indicates
                                                                  that the data is invalid or out of sync with Unified CM data; if a Head icon appears, the group is valid. |
| Description | Description of the Group ID. Press the Tab key to automatically populate the Description
                                                         							 field. |
| Group Information (continued) | Number of CTI Ports | Number of CTI ports assigned to the call control group. This is a mandatory field. If you have a Premium
                                                         							 license with an Outbound license, you can create only one Outbound call control
                                                         							 group with a minimum licensed number of IVR ports or more. The number of CTI
                                                         							 ports for an outbound type of call control group can be modified but not below
                                                         							 the licensed ports for Outbound IVR. This rule does not apply to inbound type
                                                         							 call control groups. You can continue to create more inbound type call control
                                                         							 groups. Note If this field is set to <n> , the system creates <n> ports for each Unified CCX Engine node (node in which Unified CCX Engine component is enabled). | Note | If this field is set to <n> , the system creates <n> ports for each Unified CCX Engine node (node in which Unified CCX Engine component is enabled). |
| Note | If this field is set to <n> , the system creates <n> ports for each Unified CCX Engine node (node in which Unified CCX Engine component is enabled). |
| Media Termination Support | Enables the auto-creation of media termination groups.
                                                         							 This is a mandatory field. Yes = Provides automatic media termination if the CTI
                                                         							 port group is successful. No = Media termination port group is not created
                                                         							 (default). |
| Group Type | Select the group type for the call control group using this radio button. The choices are Inbound and Outbound. This is a
                                                         mandatory field and Inbound radio button is enabled by default. You cannot change the group type from Outbound to Inbound
                                                         and conversely. The Outbound type call control group will be displayed only if you have uploaded the Outbound license on top
                                                         of the premium license in your Unified CCX. |
| Directory Number Information | Device Name Prefix | The Device Name Prefix (DNP) given to all of the CTI ports in this group. This is a mandatory field. The CTI ports for this port group are restricted to a maximum of 5 characters and has the following format: <deviceprefix> _ <directoryno> For example, if the Device Name Prefix is CTP and the starting Directory Number is 7000, the CTI port that is created in Unified
                                                         CM can have the device name CTP_7000. |
| Select Server for Telephony Port Group Configuration (displayed only in a HA over WAN deployment). |
|  | Select Server | This field is displayed only in a HA over WAN deployment
                                                         							 and it displays the different Unified CCX nodes that are available in a HA over
                                                         							 WAN deployment in a drop-down list. In a HA over WAN setup, you need to configure directory information along with Unified CM-specific information for the ports
                                                         in each node. Once you select a node, all configuration details displayed below this field will be specific to the selected
                                                         node only. So, if you update any node-specific parameters (below the Select Server field), it will be applicable only to the ports specific to the selected node. But, if you update any configuration data
                                                         above the Select Server field, it will be applicable for the ports in both the nodes except for the Number of s field. Note You need to ensure that the values in Number of s field for both the nodes are the same. If you modify this field, the number of ports is modified for the selected node only
                                                                  as the device pool selection for both nodes could be different in a HA over WAN deployment. If you click Add before updating this value for either of the node, the port group for that node will be marked with a red cross in the main
                                                                  Cisco Unified CM Telephony Call Control Group Configuration web page to signify the fact that the number of ports between
                                                                  the two nodes is different and the other node should also be updated. In such a scenario, click the hyperlink for the node
                                                                  that is tagged in red; and from the Cisco Unified CM Telephony Call Control Group Configuration page for the selected node,
                                                                  update the value in the Number of CTI Ports field and click Update to ensure the number of CTI ports for both the nodes are the same. After you configure the data for the selected node and click Add or Update , the updated configuration information will be saved. For detailed information on behavior in HA over WAN scenario, refer
                                                         to the Solution Design Guide for
                                                                  				  Cisco Unified Contact Center Express https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_implementation_design_guides_list.html . In case of LAN deployment, this field is not displayed, as the same configuration data will be applicable for both the nodes
                                                         in the cluster. | Note | You need to ensure that the values in Number of s field for both the nodes are the same. If you modify this field, the number of ports is modified for the selected node only
                                                                  as the device pool selection for both nodes could be different in a HA over WAN deployment. If you click Add before updating this value for either of the node, the port group for that node will be marked with a red cross in the main
                                                                  Cisco Unified CM Telephony Call Control Group Configuration web page to signify the fact that the number of ports between
                                                                  the two nodes is different and the other node should also be updated. In such a scenario, click the hyperlink for the node
                                                                  that is tagged in red; and from the Cisco Unified CM Telephony Call Control Group Configuration page for the selected node,
                                                                  update the value in the Number of CTI Ports field and click Update to ensure the number of CTI ports for both the nodes are the same. |
| Note | You need to ensure that the values in Number of s field for both the nodes are the same. If you modify this field, the number of ports is modified for the selected node only
                                                                  as the device pool selection for both nodes could be different in a HA over WAN deployment. If you click Add before updating this value for either of the node, the port group for that node will be marked with a red cross in the main
                                                                  Cisco Unified CM Telephony Call Control Group Configuration web page to signify the fact that the number of ports between
                                                                  the two nodes is different and the other node should also be updated. In such a scenario, click the hyperlink for the node
                                                                  that is tagged in red; and from the Cisco Unified CM Telephony Call Control Group Configuration page for the selected node,
                                                                  update the value in the Number of CTI Ports field and click Update to ensure the number of CTI ports for both the nodes are the same. |
| Directory Number Information | Starting Directory Number | A unique phone
                                                         							 number. The Starting Directory Number contains numerals, and can have an
                                                         							 asterisk (*) or a hash (#), or both as a prefix or a suffix. To support E.164
                                                         							 compliance, Unified CCX allows you to add the plus sign (+) before the
                                                         							 directory number. The specified number of ports will be created starting from
                                                         							 the value specified in this field. The Directory Number that you enter can
                                                         							 appear in more than one partition. This is a mandatory field. Note When a pattern is used as a Directory Number, the phone display and the caller ID display on the dialed phone will contain
                                                                  characters other than digits. To avoid this, provide a value for Display (Internal Caller ID), Line Text Label, and External
                                                                  Phone Number Mask. | Note | When a pattern is used as a Directory Number, the phone display and the caller ID display on the dialed phone will contain
                                                                  characters other than digits. To avoid this, provide a value for Display (Internal Caller ID), Line Text Label, and External
                                                                  Phone Number Mask. |
| Note | When a pattern is used as a Directory Number, the phone display and the caller ID display on the dialed phone will contain
                                                                  characters other than digits. To avoid this, provide a value for Display (Internal Caller ID), Line Text Label, and External
                                                                  Phone Number Mask. |
| Device Pool | Set of common characteristics for devices, such as
                                                         							 region, date/time group, softkey template, and MLPP information to which you
                                                         							 want to assign this phone. Note The support for having multiple device pools associated with the call control group(s) has been withdrawn in Unified CCX.
                                                                  Manually assign a single device pool to each call control group if you have multiple device pools associated with call control
                                                                  group(s) in an older version of Unified CCX. In a HA over WAN setup, you need to configure directory
                                                         							 information along with Unified CM-specific information for the ports in each
                                                         							 node. Once you select a node, all configuration details displayed below this
                                                         							 field will be specific to the selected node only. So, if you update any
                                                         							 node-specific parameters (below the Select Server field), it will be
                                                         							 applicable only to the ports specific to the selected node. But, if you update
                                                         							 any configuration data above the Select Server field, it will be
                                                         							 applicable for the ports in both the nodes except for the Number of CTI Ports field. Note You need to ensure that the values in Number of CTI Ports field for both the nodes are the same. If you modify this field, the number of ports is modified for the selected node only
                                                                  as the device pool selection for both nodes could be different in a HA over WAN deployment. If you click Add before updating this value for either of the node, the port group for that node will be marked with a red cross in the main
                                                                  Cisco Unified CM Telephony Call Control Group Configuration web page to signify the fact that the number of ports between
                                                                  the two nodes is different and the other node should also be updated. In such a scenario, click the hyperlink for the node
                                                                  that is tagged in red; and from the Cisco Unified CM Telephony Call Control Group Configuration page for the selected node,
                                                                  update the value in the Number of CTI Ports field and click Update to ensure the number of CTI ports for both the nodes are the same. | Note | The support for having multiple device pools associated with the call control group(s) has been withdrawn in Unified CCX.
                                                                  Manually assign a single device pool to each call control group if you have multiple device pools associated with call control
                                                                  group(s) in an older version of Unified CCX. | Note | You need to ensure that the values in Number of CTI Ports field for both the nodes are the same. If you modify this field, the number of ports is modified for the selected node only
                                                                  as the device pool selection for both nodes could be different in a HA over WAN deployment. If you click Add before updating this value for either of the node, the port group for that node will be marked with a red cross in the main
                                                                  Cisco Unified CM Telephony Call Control Group Configuration web page to signify the fact that the number of ports between
                                                                  the two nodes is different and the other node should also be updated. In such a scenario, click the hyperlink for the node
                                                                  that is tagged in red; and from the Cisco Unified CM Telephony Call Control Group Configuration page for the selected node,
                                                                  update the value in the Number of CTI Ports field and click Update to ensure the number of CTI ports for both the nodes are the same. |
| Note | The support for having multiple device pools associated with the call control group(s) has been withdrawn in Unified CCX.
                                                                  Manually assign a single device pool to each call control group if you have multiple device pools associated with call control
                                                                  group(s) in an older version of Unified CCX. |
| Note | You need to ensure that the values in Number of CTI Ports field for both the nodes are the same. If you modify this field, the number of ports is modified for the selected node only
                                                                  as the device pool selection for both nodes could be different in a HA over WAN deployment. If you click Add before updating this value for either of the node, the port group for that node will be marked with a red cross in the main
                                                                  Cisco Unified CM Telephony Call Control Group Configuration web page to signify the fact that the number of ports between
                                                                  the two nodes is different and the other node should also be updated. In such a scenario, click the hyperlink for the node
                                                                  that is tagged in red; and from the Cisco Unified CM Telephony Call Control Group Configuration page for the selected node,
                                                                  update the value in the Number of CTI Ports field and click Update to ensure the number of CTI ports for both the nodes are the same. |
| DN Calling Search Space | A collection of partitions that are searched to
                                                         							 determine how a dialed number should be routed. The calling search space for
                                                         							 the device and the calling search space for the directory number get used
                                                         							 together. The directory number calling search space takes precedence over the
                                                         							 device calling search space. For more information, see the System Configuration Guide for Cisco Unified Communications Manager . |
| Location | The Cisco Unified Communications phone location setting
                                                         							 specifies the total bandwidth that is available for calls to and from this
                                                         							 location. A location setting of HUB_NONE means that the location feature does not
                                                         							 keep track of the bandwidth that this Cisco Unified Communications phone
                                                         							 consumes. |
| Advanced Directory Number Information (only
                                                         							 available if you click Show More ) |
| Directory Number (continued) | Alerting Name ASCII | This information is automatically populated based on the
                                                         							 configuration in the Unified CM setup and displays the ASCII name filed used in
                                                         							 one of the following situations: If the device is not capable of handling the Unicode strings If the locals on endpoint devices do not match If the Unicode string is not specified |
| Redirect Calling Search Space | A collection of partitions that are searched to
                                                         							 determine how a redirected call is routed. Redirect Calling Search Space options: Note DN Calling Search Space is deprecated. Use Calling Party or Redirect Party instead. DN Calling Search Space— This option enables the CTI port to use its directory number CSS when performing a redirect transfer. Calling Party— This option enables the CTI port to use the calling party's CSS when performing a redirect / consult transfer. Redirect Party— This option enables the CTI port to use the CTI port's CSS to control the redirect. | Note | DN Calling Search Space is deprecated. Use Calling Party or Redirect Party instead. |
| Note | DN Calling Search Space is deprecated. Use Calling Party or Redirect Party instead. |
| Media Resource Group List | A prioritized grouping of media resource groups. An
                                                         							 application chooses the required media resource, such as a Music On Hold
                                                         							 server, from the available media resources according to the priority order that
                                                         							 is defined in a Media Resource Group List. If you choose <none>, Unified CM uses the Media
                                                         							 Resource Group that is defined in the device pool. |
| Directory Number Setting | Voice Mail Profile | A list of profiles defined in the Voice Mail Profile
                                                         							 Configuration. The first option is <None>, which is the current
                                                         							 default Voice Mail Profile that is configured in the Voice Mail Profile
                                                         							 Configuration. |
| Presence Group | See the Cisco Unified
                                                                  				  Communications Manager Administration Guide for detailed information on how to configure presence groups. |
| Require DTMF Reception | A Unified CM radio button to determine if DTMF reception
                                                         							 is required. Yes is selected by default. If you select No, a warning message is
                                                         							 displayed. |
| AAR Group | Automated Alternate Routing (AAR) group for this device.
                                                         							 The AAR group provides the prefix digits that are used to route calls that are
                                                         							 otherwise blocked due to insufficient bandwidth. An AAR group setting of
                                                         							 <None> specifies that no rerouting of blocked calls will be attempted. |
| User Hold Audio Source | Audio source heard by the caller when the Unified CCX
                                                         							 Script places the caller on Hold by using the Hold Step (when you press the
                                                         							 hold key). |
| Network Hold Audio Source | Audio source heard by the caller when Unified CCX performs a Consult Transfer (when Unified CCX calls an agent). Use this
                                                         entry for the .wav file (for example, a .wav file playing a ringback tone) to be played to the caller during this Consult
                                                         Transfer. |
| Call Forward and Pickup Settings | Call Pickup Group | The number that can be dialed to answer calls to this
                                                         							 directory number in the specified partition. |
| Display | Use a maximum of 30 alphanumeric characters. Typically,
                                                         							 use the user name or the directory number (if you use the directory number, the
                                                         							 person receiving the call may not see the proper identity of the caller). Leave this field blank to have the system display the
                                                         							 extension. |
| External Phone Number Mask | Phone number (or mask) that is used to send Caller ID
                                                         							 information when a call is placed from this line. You can enter a maximum of 24 number, the international
                                                         							 escape character +, *, # and "X" characters. The X characters represent the
                                                         							 directory number and must appear at the end of the pattern. For example, if you
                                                         							 specify a mask of 972813XXXX, an external call from extension 1234 displays a
                                                         							 caller ID number of 9728131234. |
| Step 4 | Click Add or Save . The Unified CM Telephony Call Control Group Configuration summary web page opens. The corresponding CTI ports are created
                                             in the Unified CM Telephony call control group. The new call control group appears in the list of call control groups in the
                                             Cisco Unified CM Telephony Call Control Group Configuration web page. |

| Note | You can create only one call control group of the Outbound type, in which the number of CTI ports must be always equal to
                                                         or greater than the licensed Outbound IVR ports. Create the CTI ports through the Publisher for both nodes in a HA over WAN deployment. |
|---|---|

| Page Area | Field | Description |
|---|---|---|
| Group Information | Group ID | Corresponds to the trunk group number reported to Cisco
                                                         							 Unified Intelligent Contact Management Enterprise (Unified ICME) when the
                                                         							 Unified CCX server is part of the Unified ICME solution. The value for this
                                                         							 field is automatically generated. Note If a Stop icon appears beside the Group ID (on the Cisco Unified CM Call Control Group Configuration list page), it indicates
                                                                  that the data is invalid or out of sync with Unified CM data; if a Head icon appears, the group is valid. | Note | If a Stop icon appears beside the Group ID (on the Cisco Unified CM Call Control Group Configuration list page), it indicates
                                                                  that the data is invalid or out of sync with Unified CM data; if a Head icon appears, the group is valid. |
| Note | If a Stop icon appears beside the Group ID (on the Cisco Unified CM Call Control Group Configuration list page), it indicates
                                                                  that the data is invalid or out of sync with Unified CM data; if a Head icon appears, the group is valid. |
| Description | Description of the Group ID. Press the Tab key to automatically populate the Description
                                                         							 field. |
| Group Information (continued) | Number of CTI Ports | Number of CTI ports assigned to the call control group. This is a mandatory field. If you have a Premium
                                                         							 license with an Outbound license, you can create only one Outbound call control
                                                         							 group with a minimum licensed number of IVR ports or more. The number of CTI
                                                         							 ports for an outbound type of call control group can be modified but not below
                                                         							 the licensed ports for Outbound IVR. This rule does not apply to inbound type
                                                         							 call control groups. You can continue to create more inbound type call control
                                                         							 groups. Note If this field is set to <n> , the system creates <n> ports for each Unified CCX Engine node (node in which Unified CCX Engine component is enabled). | Note | If this field is set to <n> , the system creates <n> ports for each Unified CCX Engine node (node in which Unified CCX Engine component is enabled). |
| Note | If this field is set to <n> , the system creates <n> ports for each Unified CCX Engine node (node in which Unified CCX Engine component is enabled). |
| Media Termination Support | Enables the auto-creation of media termination groups.
                                                         							 This is a mandatory field. Yes = Provides automatic media termination if the CTI
                                                         							 port group is successful. No = Media termination port group is not created
                                                         							 (default). |
| Group Type | Select the group type for the call control group using this radio button. The choices are Inbound and Outbound. This is a
                                                         mandatory field and Inbound radio button is enabled by default. You cannot change the group type from Outbound to Inbound
                                                         and conversely. The Outbound type call control group will be displayed only if you have uploaded the Outbound license on top
                                                         of the premium license in your Unified CCX. |
| Directory Number Information | Device Name Prefix | The Device Name Prefix (DNP) given to all of the CTI ports in this group. This is a mandatory field. The CTI ports for this port group are restricted to a maximum of 5 characters and has the following format: <deviceprefix> _ <directoryno> For example, if the Device Name Prefix is CTP and the starting Directory Number is 7000, the CTI port that is created in Unified
                                                         CM can have the device name CTP_7000. |
| Select Server for Telephony Port Group Configuration (displayed only in a HA over WAN deployment). |
|  | Select Server | This field is displayed only in a HA over WAN deployment
                                                         							 and it displays the different Unified CCX nodes that are available in a HA over
                                                         							 WAN deployment in a drop-down list. In a HA over WAN setup, you need to configure directory information along with Unified CM-specific information for the ports
                                                         in each node. Once you select a node, all configuration details displayed below this field will be specific to the selected
                                                         node only. So, if you update any node-specific parameters (below the Select Server field), it will be applicable only to the ports specific to the selected node. But, if you update any configuration data
                                                         above the Select Server field, it will be applicable for the ports in both the nodes except for the Number of s field. Note You need to ensure that the values in Number of s field for both the nodes are the same. If you modify this field, the number of ports is modified for the selected node only
                                                                  as the device pool selection for both nodes could be different in a HA over WAN deployment. If you click Add before updating this value for either of the node, the port group for that node will be marked with a red cross in the main
                                                                  Cisco Unified CM Telephony Call Control Group Configuration web page to signify the fact that the number of ports between
                                                                  the two nodes is different and the other node should also be updated. In such a scenario, click the hyperlink for the node
                                                                  that is tagged in red; and from the Cisco Unified CM Telephony Call Control Group Configuration page for the selected node,
                                                                  update the value in the Number of CTI Ports field and click Update to ensure the number of CTI ports for both the nodes are the same. After you configure the data for the selected node and click Add or Update , the updated configuration information will be saved. For detailed information on behavior in HA over WAN scenario, refer
                                                         to the Solution Design Guide for
                                                                  				  Cisco Unified Contact Center Express https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_implementation_design_guides_list.html . In case of LAN deployment, this field is not displayed, as the same configuration data will be applicable for both the nodes
                                                         in the cluster. | Note | You need to ensure that the values in Number of s field for both the nodes are the same. If you modify this field, the number of ports is modified for the selected node only
                                                                  as the device pool selection for both nodes could be different in a HA over WAN deployment. If you click Add before updating this value for either of the node, the port group for that node will be marked with a red cross in the main
                                                                  Cisco Unified CM Telephony Call Control Group Configuration web page to signify the fact that the number of ports between
                                                                  the two nodes is different and the other node should also be updated. In such a scenario, click the hyperlink for the node
                                                                  that is tagged in red; and from the Cisco Unified CM Telephony Call Control Group Configuration page for the selected node,
                                                                  update the value in the Number of CTI Ports field and click Update to ensure the number of CTI ports for both the nodes are the same. |
| Note | You need to ensure that the values in Number of s field for both the nodes are the same. If you modify this field, the number of ports is modified for the selected node only
                                                                  as the device pool selection for both nodes could be different in a HA over WAN deployment. If you click Add before updating this value for either of the node, the port group for that node will be marked with a red cross in the main
                                                                  Cisco Unified CM Telephony Call Control Group Configuration web page to signify the fact that the number of ports between
                                                                  the two nodes is different and the other node should also be updated. In such a scenario, click the hyperlink for the node
                                                                  that is tagged in red; and from the Cisco Unified CM Telephony Call Control Group Configuration page for the selected node,
                                                                  update the value in the Number of CTI Ports field and click Update to ensure the number of CTI ports for both the nodes are the same. |
| Directory Number Information | Starting Directory Number | A unique phone
                                                         							 number. The Starting Directory Number contains numerals, and can have an
                                                         							 asterisk (*) or a hash (#), or both as a prefix or a suffix. To support E.164
                                                         							 compliance, Unified CCX allows you to add the plus sign (+) before the
                                                         							 directory number. The specified number of ports will be created starting from
                                                         							 the value specified in this field. The Directory Number that you enter can
                                                         							 appear in more than one partition. This is a mandatory field. Note When a pattern is used as a Directory Number, the phone display and the caller ID display on the dialed phone will contain
                                                                  characters other than digits. To avoid this, provide a value for Display (Internal Caller ID), Line Text Label, and External
                                                                  Phone Number Mask. | Note | When a pattern is used as a Directory Number, the phone display and the caller ID display on the dialed phone will contain
                                                                  characters other than digits. To avoid this, provide a value for Display (Internal Caller ID), Line Text Label, and External
                                                                  Phone Number Mask. |
| Note | When a pattern is used as a Directory Number, the phone display and the caller ID display on the dialed phone will contain
                                                                  characters other than digits. To avoid this, provide a value for Display (Internal Caller ID), Line Text Label, and External
                                                                  Phone Number Mask. |
| Device Pool | Set of common characteristics for devices, such as
                                                         							 region, date/time group, softkey template, and MLPP information to which you
                                                         							 want to assign this phone. Note The support for having multiple device pools associated with the call control group(s) has been withdrawn in Unified CCX.
                                                                  Manually assign a single device pool to each call control group if you have multiple device pools associated with call control
                                                                  group(s) in an older version of Unified CCX. In a HA over WAN setup, you need to configure directory
                                                         							 information along with Unified CM-specific information for the ports in each
                                                         							 node. Once you select a node, all configuration details displayed below this
                                                         							 field will be specific to the selected node only. So, if you update any
                                                         							 node-specific parameters (below the Select Server field), it will be
                                                         							 applicable only to the ports specific to the selected node. But, if you update
                                                         							 any configuration data above the Select Server field, it will be
                                                         							 applicable for the ports in both the nodes except for the Number of CTI Ports field. Note You need to ensure that the values in Number of CTI Ports field for both the nodes are the same. If you modify this field, the number of ports is modified for the selected node only
                                                                  as the device pool selection for both nodes could be different in a HA over WAN deployment. If you click Add before updating this value for either of the node, the port group for that node will be marked with a red cross in the main
                                                                  Cisco Unified CM Telephony Call Control Group Configuration web page to signify the fact that the number of ports between
                                                                  the two nodes is different and the other node should also be updated. In such a scenario, click the hyperlink for the node
                                                                  that is tagged in red; and from the Cisco Unified CM Telephony Call Control Group Configuration page for the selected node,
                                                                  update the value in the Number of CTI Ports field and click Update to ensure the number of CTI ports for both the nodes are the same. | Note | The support for having multiple device pools associated with the call control group(s) has been withdrawn in Unified CCX.
                                                                  Manually assign a single device pool to each call control group if you have multiple device pools associated with call control
                                                                  group(s) in an older version of Unified CCX. | Note | You need to ensure that the values in Number of CTI Ports field for both the nodes are the same. If you modify this field, the number of ports is modified for the selected node only
                                                                  as the device pool selection for both nodes could be different in a HA over WAN deployment. If you click Add before updating this value for either of the node, the port group for that node will be marked with a red cross in the main
                                                                  Cisco Unified CM Telephony Call Control Group Configuration web page to signify the fact that the number of ports between
                                                                  the two nodes is different and the other node should also be updated. In such a scenario, click the hyperlink for the node
                                                                  that is tagged in red; and from the Cisco Unified CM Telephony Call Control Group Configuration page for the selected node,
                                                                  update the value in the Number of CTI Ports field and click Update to ensure the number of CTI ports for both the nodes are the same. |
| Note | The support for having multiple device pools associated with the call control group(s) has been withdrawn in Unified CCX.
                                                                  Manually assign a single device pool to each call control group if you have multiple device pools associated with call control
                                                                  group(s) in an older version of Unified CCX. |
| Note | You need to ensure that the values in Number of CTI Ports field for both the nodes are the same. If you modify this field, the number of ports is modified for the selected node only
                                                                  as the device pool selection for both nodes could be different in a HA over WAN deployment. If you click Add before updating this value for either of the node, the port group for that node will be marked with a red cross in the main
                                                                  Cisco Unified CM Telephony Call Control Group Configuration web page to signify the fact that the number of ports between
                                                                  the two nodes is different and the other node should also be updated. In such a scenario, click the hyperlink for the node
                                                                  that is tagged in red; and from the Cisco Unified CM Telephony Call Control Group Configuration page for the selected node,
                                                                  update the value in the Number of CTI Ports field and click Update to ensure the number of CTI ports for both the nodes are the same. |
| DN Calling Search Space | A collection of partitions that are searched to
                                                         							 determine how a dialed number should be routed. The calling search space for
                                                         							 the device and the calling search space for the directory number get used
                                                         							 together. The directory number calling search space takes precedence over the
                                                         							 device calling search space. For more information, see the System Configuration Guide for Cisco Unified Communications Manager . |
| Location | The Cisco Unified Communications phone location setting
                                                         							 specifies the total bandwidth that is available for calls to and from this
                                                         							 location. A location setting of HUB_NONE means that the location feature does not
                                                         							 keep track of the bandwidth that this Cisco Unified Communications phone
                                                         							 consumes. |
| Advanced Directory Number Information (only
                                                         							 available if you click Show More ) |
| Directory Number (continued) | Alerting Name ASCII | This information is automatically populated based on the
                                                         							 configuration in the Unified CM setup and displays the ASCII name filed used in
                                                         							 one of the following situations: If the device is not capable of handling the Unicode strings If the locals on endpoint devices do not match If the Unicode string is not specified |
| Redirect Calling Search Space | A collection of partitions that are searched to
                                                         							 determine how a redirected call is routed. Redirect Calling Search Space options: Note DN Calling Search Space is deprecated. Use Calling Party or Redirect Party instead. DN Calling Search Space— This option enables the CTI port to use its directory number CSS when performing a redirect transfer. Calling Party— This option enables the CTI port to use the calling party's CSS when performing a redirect / consult transfer. Redirect Party— This option enables the CTI port to use the CTI port's CSS to control the redirect. | Note | DN Calling Search Space is deprecated. Use Calling Party or Redirect Party instead. |
| Note | DN Calling Search Space is deprecated. Use Calling Party or Redirect Party instead. |
| Media Resource Group List | A prioritized grouping of media resource groups. An
                                                         							 application chooses the required media resource, such as a Music On Hold
                                                         							 server, from the available media resources according to the priority order that
                                                         							 is defined in a Media Resource Group List. If you choose <none>, Unified CM uses the Media
                                                         							 Resource Group that is defined in the device pool. |
| Directory Number Setting | Voice Mail Profile | A list of profiles defined in the Voice Mail Profile
                                                         							 Configuration. The first option is <None>, which is the current
                                                         							 default Voice Mail Profile that is configured in the Voice Mail Profile
                                                         							 Configuration. |
| Presence Group | See the Cisco Unified
                                                                  				  Communications Manager Administration Guide for detailed information on how to configure presence groups. |
| Require DTMF Reception | A Unified CM radio button to determine if DTMF reception
                                                         							 is required. Yes is selected by default. If you select No, a warning message is
                                                         							 displayed. |
| AAR Group | Automated Alternate Routing (AAR) group for this device.
                                                         							 The AAR group provides the prefix digits that are used to route calls that are
                                                         							 otherwise blocked due to insufficient bandwidth. An AAR group setting of
                                                         							 <None> specifies that no rerouting of blocked calls will be attempted. |
| User Hold Audio Source | Audio source heard by the caller when the Unified CCX
                                                         							 Script places the caller on Hold by using the Hold Step (when you press the
                                                         							 hold key). |
| Network Hold Audio Source | Audio source heard by the caller when Unified CCX performs a Consult Transfer (when Unified CCX calls an agent). Use this
                                                         entry for the .wav file (for example, a .wav file playing a ringback tone) to be played to the caller during this Consult
                                                         Transfer. |
| Call Forward and Pickup Settings | Call Pickup Group | The number that can be dialed to answer calls to this
                                                         							 directory number in the specified partition. |
| Display | Use a maximum of 30 alphanumeric characters. Typically,
                                                         							 use the user name or the directory number (if you use the directory number, the
                                                         							 person receiving the call may not see the proper identity of the caller). Leave this field blank to have the system display the
                                                         							 extension. |
| External Phone Number Mask | Phone number (or mask) that is used to send Caller ID
                                                         							 information when a call is placed from this line. You can enter a maximum of 24 number, the international
                                                         							 escape character +, *, # and "X" characters. The X characters represent the
                                                         							 directory number and must appear at the end of the pattern. For example, if you
                                                         							 specify a mask of 972813XXXX, an external call from extension 1234 displays a
                                                         							 caller ID number of 9728131234. |

| Note | If a Stop icon appears beside the Group ID (on the Cisco Unified CM Call Control Group Configuration list page), it indicates
                                                                  that the data is invalid or out of sync with Unified CM data; if a Head icon appears, the group is valid. |
|---|---|

| Note | If this field is set to <n> , the system creates <n> ports for each Unified CCX Engine node (node in which Unified CCX Engine component is enabled). |
|---|---|

| Note | You need to ensure that the values in Number of s field for both the nodes are the same. If you modify this field, the number of ports is modified for the selected node only
                                                                  as the device pool selection for both nodes could be different in a HA over WAN deployment. If you click Add before updating this value for either of the node, the port group for that node will be marked with a red cross in the main
                                                                  Cisco Unified CM Telephony Call Control Group Configuration web page to signify the fact that the number of ports between
                                                                  the two nodes is different and the other node should also be updated. In such a scenario, click the hyperlink for the node
                                                                  that is tagged in red; and from the Cisco Unified CM Telephony Call Control Group Configuration page for the selected node,
                                                                  update the value in the Number of CTI Ports field and click Update to ensure the number of CTI ports for both the nodes are the same. |
|---|---|

| Note | When a pattern is used as a Directory Number, the phone display and the caller ID display on the dialed phone will contain
                                                                  characters other than digits. To avoid this, provide a value for Display (Internal Caller ID), Line Text Label, and External
                                                                  Phone Number Mask. |
|---|---|

| Note | The support for having multiple device pools associated with the call control group(s) has been withdrawn in Unified CCX.
                                                                  Manually assign a single device pool to each call control group if you have multiple device pools associated with call control
                                                                  group(s) in an older version of Unified CCX. |
|---|---|

| Note | You need to ensure that the values in Number of CTI Ports field for both the nodes are the same. If you modify this field, the number of ports is modified for the selected node only
                                                                  as the device pool selection for both nodes could be different in a HA over WAN deployment. If you click Add before updating this value for either of the node, the port group for that node will be marked with a red cross in the main
                                                                  Cisco Unified CM Telephony Call Control Group Configuration web page to signify the fact that the number of ports between
                                                                  the two nodes is different and the other node should also be updated. In such a scenario, click the hyperlink for the node
                                                                  that is tagged in red; and from the Cisco Unified CM Telephony Call Control Group Configuration page for the selected node,
                                                                  update the value in the Number of CTI Ports field and click Update to ensure the number of CTI ports for both the nodes are the same. |
|---|---|

| Note | DN Calling Search Space is deprecated. Use Calling Party or Redirect Party instead. |
|---|---|

| Step 1 | From the Unified
                                          			 CCX Administration menu bar, choose Subsystems > Cisco Unified CM
                                                				  Telephony > Triggers . The Unified CM
                                             				Telephony Trigger Configuration web page opens displaying the following fields. Field Description Route
                                                         							 Point Available CTI route point, which is the directory number
                                                         							 associated with the trigger. Application Application name to associate with the trigger. Sessions Maximum number of simultaneous calls that the trigger can
                                                         							 handle. Enabled True
                                                         							 if the trigger is enabled; False if the trigger is disabled. Note If you try to
                                                         				  delete a trigger associated with an outbound call control group, then the
                                                         				  campaigns associated with the trigger become invalid and the application also
                                                         				  gets deleted. In such cases, when you click the Delete icon or button, a dialog box opens to confirm your action. Click OK if you want to delete the trigger and
                                                         				  disassociate the campaigns associated with it. If you delete a trigger and
                                                         				  navigate to the Campaign Configuration web page, you will also see an alert
                                                         				  regarding the missing trigger association for that campaign. | Field | Description | Route
                                                         							 Point | Available CTI route point, which is the directory number
                                                         							 associated with the trigger. | Application | Application name to associate with the trigger. | Sessions | Maximum number of simultaneous calls that the trigger can
                                                         							 handle. | Enabled | True
                                                         							 if the trigger is enabled; False if the trigger is disabled. | Note | If you try to
                                                         				  delete a trigger associated with an outbound call control group, then the
                                                         				  campaigns associated with the trigger become invalid and the application also
                                                         				  gets deleted. In such cases, when you click the Delete icon or button, a dialog box opens to confirm your action. Click OK if you want to delete the trigger and
                                                         				  disassociate the campaigns associated with it. If you delete a trigger and
                                                         				  navigate to the Campaign Configuration web page, you will also see an alert
                                                         				  regarding the missing trigger association for that campaign. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Field | Description |
| Route
                                                         							 Point | Available CTI route point, which is the directory number
                                                         							 associated with the trigger. |
| Application | Application name to associate with the trigger. |
| Sessions | Maximum number of simultaneous calls that the trigger can
                                                         							 handle. |
| Enabled | True
                                                         							 if the trigger is enabled; False if the trigger is disabled. |
| Note | If you try to
                                                         				  delete a trigger associated with an outbound call control group, then the
                                                         				  campaigns associated with the trigger become invalid and the application also
                                                         				  gets deleted. In such cases, when you click the Delete icon or button, a dialog box opens to confirm your action. Click OK if you want to delete the trigger and
                                                         				  disassociate the campaigns associated with it. If you delete a trigger and
                                                         				  navigate to the Campaign Configuration web page, you will also see an alert
                                                         				  regarding the missing trigger association for that campaign. |
| Step 2 | Click the Add
                                             				New icon that is displayed in the tool bar in the upper left corner
                                          			 of the window or the Add
                                             				New button that is displayed at the bottom of the window. The Unified CM
                                             				Telephony Trigger Configuration web page opens. |
| Step 3 | Use this web
                                          			 page to specify the following mandatory fields: Field Description Directory Information Directory Number A
                                                         							 unique phone number. To support E.164 compliance, Unified CCX allows you to add
                                                         							 a plus sign (+) before the agent extension or a route point directory number
                                                         							 followed by 15 characters which consist of numerals and the following special
                                                         							 characters: uppercase letter X, hash (#), square brackets ([ ]), hyphen (-),
                                                         							 and asterisk (*). Supports only route point directory numbers and Finesse agent and supervisor extensions. Note +1234 and 1234 are two different directory numbers. The square brackets ([ ]) enclose a range of values. For more information, see the "Wildcards and Special Characters in Route Patterns and Hunt Pilots" section in the System Configuration Guide for Cisco Unified Communications Manager . Examples: Valid directory numbers—+1223* or *#12#* Invalid directory numbers—91X+ or +-12345 Note Use of two(2) wildcard CTI Route Points that overlap
                                                                     								with each other is not supported. For example, Route Point 1: 123XXXX and Route
                                                                     								Point 2: 1234XXX overlap with one another and is not supported. However, a wildcard CTI Route point can overlap with
                                                                     								a full DID (best match pattern) that doesn't contain a wildcard. For example,
                                                                     								Route Point 1: 123XXXX and Route Point 2: 1234567 is supported. Trigger Information Language Choose the default language to associate with the incoming call
                                                         							 when the application is started from this drop-down menu. Note To
                                                                     								add a Language option, click Edit button. The User Prompt dialog box opens. Enter
                                                                     								a locale string value and click OK . The User Prompt dialog box closes, and the name
                                                                     								of the language opens in the Language field in the Unified CM Telephony
                                                                     								Configuration web page. Application Name From
                                                         							 the drop-down menu, choose the application to associate with the trigger. Device Name A
                                                         							 unique identifier for this device, consisting of alphanumeric characters, dots,
                                                         							 dashes, or underscores. Description A
                                                         							 descriptive name for the CTI route point. Call
                                                         							 Control Group Choose the call control group to associate with the trigger from
                                                         							 this drop-down menu. For Outbound IVR Dialer, you must select the call control
                                                         							 group from Outbound type call control group list. The route point should be
                                                         							 created on Unified CM. Once you assign the Outbound group for a trigger, you
                                                         							 cannot change it to an Inbound group and vice versa. Advanced Configuration (available only if you click Show More ). Advanced Trigger
                                                            								Information Enabled Radio buttons to choose the required option: Yes— enable the trigger (default) No— disable the trigger. Maximum Number of Sessions The
                                                         							 maximum number of simultaneous calls that this trigger can handle. The number
                                                         							 is actually governed by the Unified CM (10,000 for each separate line). However in Unified CCX, this number is
                                                         							 restricted to the maximum number of sessions. Any call after this number is
                                                         							 exceeded gets the busy tone. Idle
                                                         							 Timeout (in ms) The
                                                         							 number of milliseconds (ms) the system should wait before rejecting the Unified
                                                         							 CM Telephony request for this trigger. Override Media Termination Radio buttons to choose the required options: Yes— Override media
                                                         							 termination. No— Enable media
                                                         							 termination (default). If
                                                         							 you select Yes, two panes open: Selected Dialog Groups displays the default or selected group. Available Dialog Groups lists the configured dialog. CTI Route Point
                                                            								Information Alerting Name ASCII This
                                                         							 information is automatically populated based on the configuration in the
                                                         							 Unified CM setup and displays the ASCII name filed used in one of the following
                                                         							 situations: If the device is not capable of handling the Unicode strings If the locals on endpoint devices do not match If the Unicode string is not specified Device Pool The
                                                         							 device pool to which you want to assign this route point. A device pool defines
                                                         							 sets of common characteristics for devices, such as region, date/time group,
                                                         							 softkey template, and MLPP information. Location The
                                                         							 total bandwidth that is available for calls to/from this location. A location
                                                         							 setting of HUB_NONE indicates that the locations feature does not keep
                                                         							 track of the bandwidth used by this route point. Directory Number Settings Partition The
                                                         							 partition to which the Directory Number belongs. The Directory Number field
                                                         							 value must be unique within the partition that you choose. If
                                                         							 you do not want to restrict access to the Directory Number, select < None > as the
                                                         							 partition setting. Voice Mail Profile A
                                                         							 list of profiles defined in the Voice Mail Profile Configuration. The
                                                         							 first option is < None >, which is the current default Voice Mail Profile
                                                         							 that is configured in the Voice Mail Profile Configuration. Calling Search Space A
                                                         							 collection of partitions that are searched for numbers that are called from
                                                         							 this directory number. The specified value applies to all devices that use this
                                                         							 directory number. For
                                                         							 example, assume you have two calling search spaces: Building and PSTN. Building
                                                         							 only allows users to call within the building, while PSTN allows users to call
                                                         							 both in and outside the building. You could assign the phone to the Building
                                                         							 calling search space and the line on your phone to the PSTN calling search
                                                         							 space. For more information, see the System Configuration Guide for Cisco Unified Communications Manager . Calling Search Space for Redirect By
                                                         							 default, Cisco Unified Communications Manager uses the original calling party's
                                                         							 calling search space (CSS) to process the redirected call from a Unified CCX
                                                         							 Trigger to a Unified CCX CTI Port. This default behavior requires the partition
                                                         							 of the Unified CCX CTI ports to be a member of the original calling party's CSS
                                                         							 even if the partition of the CTI Route Point/Unified CCX Trigger is accessible
                                                         							 to the calling device's CSS and the CSS of the CTI Route Point/Unified CCX
                                                         							 Trigger contains the partition of the Unified CCX CTI Ports. You
                                                         							 can modify this behavior using the drop-down list to instruct Cisco Unified
                                                         							 Communications Manager which CSS to use when redirecting the call from the CTI
                                                         							 Route Point to the CTI Port. Calling Search Space for Redirect options: Default
                                                                  									 Calling Search Space— CSS of the calling device Calling
                                                                  									 Address Search Space— CSS of the calling device Route
                                                                  									 Point Address Search Space— CSS of the CTI Route Point (Trigger) Presence Group A
                                                         							 list of groups to integrate the device with the iPass server. The device/line
                                                         							 information is provided for integrating applications. Call Forward and Pickup
                                                            								Settings Forward Busy Check one of the following options: Voice Mail— Check this
                                                         							 box to use settings in the Voice Mail Profile Configuration window. Note When this box is checked, Unified CM ignores the settings in the
                                                                     								Destination box and Calling Search Space. Destination— To use any
                                                         							 disable phone number, including an outside destination. Calling Search Space— To apply the above setting all devices that are using this directory number. Note For limiting the number of calls per application in Unified CCX system, see the Unified CM Telephony Triggers for Unified CCX Queuing section. Display Use
                                                         							 a maximum of 30 alphanumeric characters. Typically, use the user name or the
                                                         							 directory number (if using the directory number, the person receiving the call
                                                         							 may not see the proper identity of the caller). Leave this field blank to have
                                                         							 the system display an extension. External Phone Number Mask Phone number (or mask) that is used to send Caller ID
                                                         							 information when a call is placed from this line. You
                                                         							 can enter a maximum of 24 number, the international escape character +, *, #
                                                         							 and "X" characters. The X characters represent the directory number and must
                                                         							 appear at the end of the pattern. For example, if you specify a mask of
                                                         							 972813XXXX, an external call from extension 1234 displays a caller ID number of
                                                         							 9728131234. | Field | Description | Directory Information | Directory Number | A
                                                         							 unique phone number. To support E.164 compliance, Unified CCX allows you to add
                                                         							 a plus sign (+) before the agent extension or a route point directory number
                                                         							 followed by 15 characters which consist of numerals and the following special
                                                         							 characters: uppercase letter X, hash (#), square brackets ([ ]), hyphen (-),
                                                         							 and asterisk (*). Supports only route point directory numbers and Finesse agent and supervisor extensions. Note +1234 and 1234 are two different directory numbers. The square brackets ([ ]) enclose a range of values. For more information, see the "Wildcards and Special Characters in Route Patterns and Hunt Pilots" section in the System Configuration Guide for Cisco Unified Communications Manager . Examples: Valid directory numbers—+1223* or *#12#* Invalid directory numbers—91X+ or +-12345 Note Use of two(2) wildcard CTI Route Points that overlap
                                                                     								with each other is not supported. For example, Route Point 1: 123XXXX and Route
                                                                     								Point 2: 1234XXX overlap with one another and is not supported. However, a wildcard CTI Route point can overlap with
                                                                     								a full DID (best match pattern) that doesn't contain a wildcard. For example,
                                                                     								Route Point 1: 123XXXX and Route Point 2: 1234567 is supported. | Note | +1234 and 1234 are two different directory numbers. The square brackets ([ ]) enclose a range of values. For more information, see the "Wildcards and Special Characters in Route Patterns and Hunt Pilots" section in the System Configuration Guide for Cisco Unified Communications Manager . | Note | Use of two(2) wildcard CTI Route Points that overlap
                                                                     								with each other is not supported. For example, Route Point 1: 123XXXX and Route
                                                                     								Point 2: 1234XXX overlap with one another and is not supported. However, a wildcard CTI Route point can overlap with
                                                                     								a full DID (best match pattern) that doesn't contain a wildcard. For example,
                                                                     								Route Point 1: 123XXXX and Route Point 2: 1234567 is supported. | Trigger Information | Language | Choose the default language to associate with the incoming call
                                                         							 when the application is started from this drop-down menu. Note To
                                                                     								add a Language option, click Edit button. The User Prompt dialog box opens. Enter
                                                                     								a locale string value and click OK . The User Prompt dialog box closes, and the name
                                                                     								of the language opens in the Language field in the Unified CM Telephony
                                                                     								Configuration web page. | Note | To
                                                                     								add a Language option, click Edit button. The User Prompt dialog box opens. Enter
                                                                     								a locale string value and click OK . The User Prompt dialog box closes, and the name
                                                                     								of the language opens in the Language field in the Unified CM Telephony
                                                                     								Configuration web page. | Application Name | From
                                                         							 the drop-down menu, choose the application to associate with the trigger. | Device Name | A
                                                         							 unique identifier for this device, consisting of alphanumeric characters, dots,
                                                         							 dashes, or underscores. | Description | A
                                                         							 descriptive name for the CTI route point. | Call
                                                         							 Control Group | Choose the call control group to associate with the trigger from
                                                         							 this drop-down menu. For Outbound IVR Dialer, you must select the call control
                                                         							 group from Outbound type call control group list. The route point should be
                                                         							 created on Unified CM. Once you assign the Outbound group for a trigger, you
                                                         							 cannot change it to an Inbound group and vice versa. | Advanced Configuration (available only if you click Show More ). | Advanced Trigger
                                                            								Information | Enabled | Radio buttons to choose the required option: Yes— enable the trigger (default) No— disable the trigger. | Maximum Number of Sessions | The
                                                         							 maximum number of simultaneous calls that this trigger can handle. The number
                                                         							 is actually governed by the Unified CM (10,000 for each separate line). However in Unified CCX, this number is
                                                         							 restricted to the maximum number of sessions. Any call after this number is
                                                         							 exceeded gets the busy tone. | Idle
                                                         							 Timeout (in ms) | The
                                                         							 number of milliseconds (ms) the system should wait before rejecting the Unified
                                                         							 CM Telephony request for this trigger. | Override Media Termination | Radio buttons to choose the required options: Yes— Override media
                                                         							 termination. No— Enable media
                                                         							 termination (default). If
                                                         							 you select Yes, two panes open: Selected Dialog Groups displays the default or selected group. Available Dialog Groups lists the configured dialog. | CTI Route Point
                                                            								Information | Alerting Name ASCII | This
                                                         							 information is automatically populated based on the configuration in the
                                                         							 Unified CM setup and displays the ASCII name filed used in one of the following
                                                         							 situations: If the device is not capable of handling the Unicode strings If the locals on endpoint devices do not match If the Unicode string is not specified | Device Pool | The
                                                         							 device pool to which you want to assign this route point. A device pool defines
                                                         							 sets of common characteristics for devices, such as region, date/time group,
                                                         							 softkey template, and MLPP information. | Location | The
                                                         							 total bandwidth that is available for calls to/from this location. A location
                                                         							 setting of HUB_NONE indicates that the locations feature does not keep
                                                         							 track of the bandwidth used by this route point. | Directory Number Settings | Partition | The
                                                         							 partition to which the Directory Number belongs. The Directory Number field
                                                         							 value must be unique within the partition that you choose. If
                                                         							 you do not want to restrict access to the Directory Number, select < None > as the
                                                         							 partition setting. | Voice Mail Profile | A
                                                         							 list of profiles defined in the Voice Mail Profile Configuration. The
                                                         							 first option is < None >, which is the current default Voice Mail Profile
                                                         							 that is configured in the Voice Mail Profile Configuration. | Calling Search Space | A
                                                         							 collection of partitions that are searched for numbers that are called from
                                                         							 this directory number. The specified value applies to all devices that use this
                                                         							 directory number. For
                                                         							 example, assume you have two calling search spaces: Building and PSTN. Building
                                                         							 only allows users to call within the building, while PSTN allows users to call
                                                         							 both in and outside the building. You could assign the phone to the Building
                                                         							 calling search space and the line on your phone to the PSTN calling search
                                                         							 space. For more information, see the System Configuration Guide for Cisco Unified Communications Manager . | Calling Search Space for Redirect | By
                                                         							 default, Cisco Unified Communications Manager uses the original calling party's
                                                         							 calling search space (CSS) to process the redirected call from a Unified CCX
                                                         							 Trigger to a Unified CCX CTI Port. This default behavior requires the partition
                                                         							 of the Unified CCX CTI ports to be a member of the original calling party's CSS
                                                         							 even if the partition of the CTI Route Point/Unified CCX Trigger is accessible
                                                         							 to the calling device's CSS and the CSS of the CTI Route Point/Unified CCX
                                                         							 Trigger contains the partition of the Unified CCX CTI Ports. You
                                                         							 can modify this behavior using the drop-down list to instruct Cisco Unified
                                                         							 Communications Manager which CSS to use when redirecting the call from the CTI
                                                         							 Route Point to the CTI Port. Calling Search Space for Redirect options: Default
                                                                  									 Calling Search Space— CSS of the calling device Calling
                                                                  									 Address Search Space— CSS of the calling device Route
                                                                  									 Point Address Search Space— CSS of the CTI Route Point (Trigger) | Presence Group | A
                                                         							 list of groups to integrate the device with the iPass server. The device/line
                                                         							 information is provided for integrating applications. | Call Forward and Pickup
                                                            								Settings | Forward Busy | Check one of the following options: Voice Mail— Check this
                                                         							 box to use settings in the Voice Mail Profile Configuration window. Note When this box is checked, Unified CM ignores the settings in the
                                                                     								Destination box and Calling Search Space. Destination— To use any
                                                         							 disable phone number, including an outside destination. Calling Search Space— To apply the above setting all devices that are using this directory number. Note For limiting the number of calls per application in Unified CCX system, see the Unified CM Telephony Triggers for Unified CCX Queuing section. | Note | When this box is checked, Unified CM ignores the settings in the
                                                                     								Destination box and Calling Search Space. | Note | For limiting the number of calls per application in Unified CCX system, see the Unified CM Telephony Triggers for Unified CCX Queuing section. | Display | Use
                                                         							 a maximum of 30 alphanumeric characters. Typically, use the user name or the
                                                         							 directory number (if using the directory number, the person receiving the call
                                                         							 may not see the proper identity of the caller). Leave this field blank to have
                                                         							 the system display an extension. | External Phone Number Mask | Phone number (or mask) that is used to send Caller ID
                                                         							 information when a call is placed from this line. You
                                                         							 can enter a maximum of 24 number, the international escape character +, *, #
                                                         							 and "X" characters. The X characters represent the directory number and must
                                                         							 appear at the end of the pattern. For example, if you specify a mask of
                                                         							 972813XXXX, an external call from extension 1234 displays a caller ID number of
                                                         							 9728131234. |
| Field | Description |
| Directory Information |
| Directory Number | A
                                                         							 unique phone number. To support E.164 compliance, Unified CCX allows you to add
                                                         							 a plus sign (+) before the agent extension or a route point directory number
                                                         							 followed by 15 characters which consist of numerals and the following special
                                                         							 characters: uppercase letter X, hash (#), square brackets ([ ]), hyphen (-),
                                                         							 and asterisk (*). Supports only route point directory numbers and Finesse agent and supervisor extensions. Note +1234 and 1234 are two different directory numbers. The square brackets ([ ]) enclose a range of values. For more information, see the "Wildcards and Special Characters in Route Patterns and Hunt Pilots" section in the System Configuration Guide for Cisco Unified Communications Manager . Examples: Valid directory numbers—+1223* or *#12#* Invalid directory numbers—91X+ or +-12345 Note Use of two(2) wildcard CTI Route Points that overlap
                                                                     								with each other is not supported. For example, Route Point 1: 123XXXX and Route
                                                                     								Point 2: 1234XXX overlap with one another and is not supported. However, a wildcard CTI Route point can overlap with
                                                                     								a full DID (best match pattern) that doesn't contain a wildcard. For example,
                                                                     								Route Point 1: 123XXXX and Route Point 2: 1234567 is supported. | Note | +1234 and 1234 are two different directory numbers. The square brackets ([ ]) enclose a range of values. For more information, see the "Wildcards and Special Characters in Route Patterns and Hunt Pilots" section in the System Configuration Guide for Cisco Unified Communications Manager . | Note | Use of two(2) wildcard CTI Route Points that overlap
                                                                     								with each other is not supported. For example, Route Point 1: 123XXXX and Route
                                                                     								Point 2: 1234XXX overlap with one another and is not supported. However, a wildcard CTI Route point can overlap with
                                                                     								a full DID (best match pattern) that doesn't contain a wildcard. For example,
                                                                     								Route Point 1: 123XXXX and Route Point 2: 1234567 is supported. |
| Note | +1234 and 1234 are two different directory numbers. The square brackets ([ ]) enclose a range of values. For more information, see the "Wildcards and Special Characters in Route Patterns and Hunt Pilots" section in the System Configuration Guide for Cisco Unified Communications Manager . |
| Note | Use of two(2) wildcard CTI Route Points that overlap
                                                                     								with each other is not supported. For example, Route Point 1: 123XXXX and Route
                                                                     								Point 2: 1234XXX overlap with one another and is not supported. However, a wildcard CTI Route point can overlap with
                                                                     								a full DID (best match pattern) that doesn't contain a wildcard. For example,
                                                                     								Route Point 1: 123XXXX and Route Point 2: 1234567 is supported. |
| Trigger Information |
| Language | Choose the default language to associate with the incoming call
                                                         							 when the application is started from this drop-down menu. Note To
                                                                     								add a Language option, click Edit button. The User Prompt dialog box opens. Enter
                                                                     								a locale string value and click OK . The User Prompt dialog box closes, and the name
                                                                     								of the language opens in the Language field in the Unified CM Telephony
                                                                     								Configuration web page. | Note | To
                                                                     								add a Language option, click Edit button. The User Prompt dialog box opens. Enter
                                                                     								a locale string value and click OK . The User Prompt dialog box closes, and the name
                                                                     								of the language opens in the Language field in the Unified CM Telephony
                                                                     								Configuration web page. |
| Note | To
                                                                     								add a Language option, click Edit button. The User Prompt dialog box opens. Enter
                                                                     								a locale string value and click OK . The User Prompt dialog box closes, and the name
                                                                     								of the language opens in the Language field in the Unified CM Telephony
                                                                     								Configuration web page. |
| Application Name | From
                                                         							 the drop-down menu, choose the application to associate with the trigger. |
| Device Name | A
                                                         							 unique identifier for this device, consisting of alphanumeric characters, dots,
                                                         							 dashes, or underscores. |
| Description | A
                                                         							 descriptive name for the CTI route point. |
| Call
                                                         							 Control Group | Choose the call control group to associate with the trigger from
                                                         							 this drop-down menu. For Outbound IVR Dialer, you must select the call control
                                                         							 group from Outbound type call control group list. The route point should be
                                                         							 created on Unified CM. Once you assign the Outbound group for a trigger, you
                                                         							 cannot change it to an Inbound group and vice versa. |
| Advanced Configuration (available only if you click Show More ). |
| Advanced Trigger
                                                            								Information |
| Enabled | Radio buttons to choose the required option: Yes— enable the trigger (default) No— disable the trigger. |
| Maximum Number of Sessions | The
                                                         							 maximum number of simultaneous calls that this trigger can handle. The number
                                                         							 is actually governed by the Unified CM (10,000 for each separate line). However in Unified CCX, this number is
                                                         							 restricted to the maximum number of sessions. Any call after this number is
                                                         							 exceeded gets the busy tone. |
| Idle
                                                         							 Timeout (in ms) | The
                                                         							 number of milliseconds (ms) the system should wait before rejecting the Unified
                                                         							 CM Telephony request for this trigger. |
| Override Media Termination | Radio buttons to choose the required options: Yes— Override media
                                                         							 termination. No— Enable media
                                                         							 termination (default). If
                                                         							 you select Yes, two panes open: Selected Dialog Groups displays the default or selected group. Available Dialog Groups lists the configured dialog. |
| CTI Route Point
                                                            								Information |
| Alerting Name ASCII | This
                                                         							 information is automatically populated based on the configuration in the
                                                         							 Unified CM setup and displays the ASCII name filed used in one of the following
                                                         							 situations: If the device is not capable of handling the Unicode strings If the locals on endpoint devices do not match If the Unicode string is not specified |
| Device Pool | The
                                                         							 device pool to which you want to assign this route point. A device pool defines
                                                         							 sets of common characteristics for devices, such as region, date/time group,
                                                         							 softkey template, and MLPP information. |
| Location | The
                                                         							 total bandwidth that is available for calls to/from this location. A location
                                                         							 setting of HUB_NONE indicates that the locations feature does not keep
                                                         							 track of the bandwidth used by this route point. |
| Directory Number Settings |
| Partition | The
                                                         							 partition to which the Directory Number belongs. The Directory Number field
                                                         							 value must be unique within the partition that you choose. If
                                                         							 you do not want to restrict access to the Directory Number, select < None > as the
                                                         							 partition setting. |
| Voice Mail Profile | A
                                                         							 list of profiles defined in the Voice Mail Profile Configuration. The
                                                         							 first option is < None >, which is the current default Voice Mail Profile
                                                         							 that is configured in the Voice Mail Profile Configuration. |
| Calling Search Space | A
                                                         							 collection of partitions that are searched for numbers that are called from
                                                         							 this directory number. The specified value applies to all devices that use this
                                                         							 directory number. For
                                                         							 example, assume you have two calling search spaces: Building and PSTN. Building
                                                         							 only allows users to call within the building, while PSTN allows users to call
                                                         							 both in and outside the building. You could assign the phone to the Building
                                                         							 calling search space and the line on your phone to the PSTN calling search
                                                         							 space. For more information, see the System Configuration Guide for Cisco Unified Communications Manager . |
| Calling Search Space for Redirect | By
                                                         							 default, Cisco Unified Communications Manager uses the original calling party's
                                                         							 calling search space (CSS) to process the redirected call from a Unified CCX
                                                         							 Trigger to a Unified CCX CTI Port. This default behavior requires the partition
                                                         							 of the Unified CCX CTI ports to be a member of the original calling party's CSS
                                                         							 even if the partition of the CTI Route Point/Unified CCX Trigger is accessible
                                                         							 to the calling device's CSS and the CSS of the CTI Route Point/Unified CCX
                                                         							 Trigger contains the partition of the Unified CCX CTI Ports. You
                                                         							 can modify this behavior using the drop-down list to instruct Cisco Unified
                                                         							 Communications Manager which CSS to use when redirecting the call from the CTI
                                                         							 Route Point to the CTI Port. Calling Search Space for Redirect options: Default
                                                                  									 Calling Search Space— CSS of the calling device Calling
                                                                  									 Address Search Space— CSS of the calling device Route
                                                                  									 Point Address Search Space— CSS of the CTI Route Point (Trigger) |
| Presence Group | A
                                                         							 list of groups to integrate the device with the iPass server. The device/line
                                                         							 information is provided for integrating applications. |
| Call Forward and Pickup
                                                            								Settings |
| Forward Busy | Check one of the following options: Voice Mail— Check this
                                                         							 box to use settings in the Voice Mail Profile Configuration window. Note When this box is checked, Unified CM ignores the settings in the
                                                                     								Destination box and Calling Search Space. Destination— To use any
                                                         							 disable phone number, including an outside destination. Calling Search Space— To apply the above setting all devices that are using this directory number. Note For limiting the number of calls per application in Unified CCX system, see the Unified CM Telephony Triggers for Unified CCX Queuing section. | Note | When this box is checked, Unified CM ignores the settings in the
                                                                     								Destination box and Calling Search Space. | Note | For limiting the number of calls per application in Unified CCX system, see the Unified CM Telephony Triggers for Unified CCX Queuing section. |
| Note | When this box is checked, Unified CM ignores the settings in the
                                                                     								Destination box and Calling Search Space. |
| Note | For limiting the number of calls per application in Unified CCX system, see the Unified CM Telephony Triggers for Unified CCX Queuing section. |
| Display | Use
                                                         							 a maximum of 30 alphanumeric characters. Typically, use the user name or the
                                                         							 directory number (if using the directory number, the person receiving the call
                                                         							 may not see the proper identity of the caller). Leave this field blank to have
                                                         							 the system display an extension. |
| External Phone Number Mask | Phone number (or mask) that is used to send Caller ID
                                                         							 information when a call is placed from this line. You
                                                         							 can enter a maximum of 24 number, the international escape character +, *, #
                                                         							 and "X" characters. The X characters represent the directory number and must
                                                         							 appear at the end of the pattern. For example, if you specify a mask of
                                                         							 972813XXXX, an external call from extension 1234 displays a caller ID number of
                                                         							 9728131234. |
| Step 4 | Click Add or Save to save the changes. The specified route point
                                          			 is created on the Unified CM. The Unified CM
                                             				Telephony Trigger Configuration web page opens and displays the new Unified CM
                                             				Telephony trigger. |

| Field | Description |
|---|---|
| Route
                                                         							 Point | Available CTI route point, which is the directory number
                                                         							 associated with the trigger. |
| Application | Application name to associate with the trigger. |
| Sessions | Maximum number of simultaneous calls that the trigger can
                                                         							 handle. |
| Enabled | True
                                                         							 if the trigger is enabled; False if the trigger is disabled. |

| Note | If you try to
                                                         				  delete a trigger associated with an outbound call control group, then the
                                                         				  campaigns associated with the trigger become invalid and the application also
                                                         				  gets deleted. In such cases, when you click the Delete icon or button, a dialog box opens to confirm your action. Click OK if you want to delete the trigger and
                                                         				  disassociate the campaigns associated with it. If you delete a trigger and
                                                         				  navigate to the Campaign Configuration web page, you will also see an alert
                                                         				  regarding the missing trigger association for that campaign. |
|---|---|

| Field | Description |
|---|---|
| Directory Information |
| Directory Number | A
                                                         							 unique phone number. To support E.164 compliance, Unified CCX allows you to add
                                                         							 a plus sign (+) before the agent extension or a route point directory number
                                                         							 followed by 15 characters which consist of numerals and the following special
                                                         							 characters: uppercase letter X, hash (#), square brackets ([ ]), hyphen (-),
                                                         							 and asterisk (*). Supports only route point directory numbers and Finesse agent and supervisor extensions. Note +1234 and 1234 are two different directory numbers. The square brackets ([ ]) enclose a range of values. For more information, see the "Wildcards and Special Characters in Route Patterns and Hunt Pilots" section in the System Configuration Guide for Cisco Unified Communications Manager . Examples: Valid directory numbers—+1223* or *#12#* Invalid directory numbers—91X+ or +-12345 Note Use of two(2) wildcard CTI Route Points that overlap
                                                                     								with each other is not supported. For example, Route Point 1: 123XXXX and Route
                                                                     								Point 2: 1234XXX overlap with one another and is not supported. However, a wildcard CTI Route point can overlap with
                                                                     								a full DID (best match pattern) that doesn't contain a wildcard. For example,
                                                                     								Route Point 1: 123XXXX and Route Point 2: 1234567 is supported. | Note | +1234 and 1234 are two different directory numbers. The square brackets ([ ]) enclose a range of values. For more information, see the "Wildcards and Special Characters in Route Patterns and Hunt Pilots" section in the System Configuration Guide for Cisco Unified Communications Manager . | Note | Use of two(2) wildcard CTI Route Points that overlap
                                                                     								with each other is not supported. For example, Route Point 1: 123XXXX and Route
                                                                     								Point 2: 1234XXX overlap with one another and is not supported. However, a wildcard CTI Route point can overlap with
                                                                     								a full DID (best match pattern) that doesn't contain a wildcard. For example,
                                                                     								Route Point 1: 123XXXX and Route Point 2: 1234567 is supported. |
| Note | +1234 and 1234 are two different directory numbers. The square brackets ([ ]) enclose a range of values. For more information, see the "Wildcards and Special Characters in Route Patterns and Hunt Pilots" section in the System Configuration Guide for Cisco Unified Communications Manager . |
| Note | Use of two(2) wildcard CTI Route Points that overlap
                                                                     								with each other is not supported. For example, Route Point 1: 123XXXX and Route
                                                                     								Point 2: 1234XXX overlap with one another and is not supported. However, a wildcard CTI Route point can overlap with
                                                                     								a full DID (best match pattern) that doesn't contain a wildcard. For example,
                                                                     								Route Point 1: 123XXXX and Route Point 2: 1234567 is supported. |
| Trigger Information |
| Language | Choose the default language to associate with the incoming call
                                                         							 when the application is started from this drop-down menu. Note To
                                                                     								add a Language option, click Edit button. The User Prompt dialog box opens. Enter
                                                                     								a locale string value and click OK . The User Prompt dialog box closes, and the name
                                                                     								of the language opens in the Language field in the Unified CM Telephony
                                                                     								Configuration web page. | Note | To
                                                                     								add a Language option, click Edit button. The User Prompt dialog box opens. Enter
                                                                     								a locale string value and click OK . The User Prompt dialog box closes, and the name
                                                                     								of the language opens in the Language field in the Unified CM Telephony
                                                                     								Configuration web page. |
| Note | To
                                                                     								add a Language option, click Edit button. The User Prompt dialog box opens. Enter
                                                                     								a locale string value and click OK . The User Prompt dialog box closes, and the name
                                                                     								of the language opens in the Language field in the Unified CM Telephony
                                                                     								Configuration web page. |
| Application Name | From
                                                         							 the drop-down menu, choose the application to associate with the trigger. |
| Device Name | A
                                                         							 unique identifier for this device, consisting of alphanumeric characters, dots,
                                                         							 dashes, or underscores. |
| Description | A
                                                         							 descriptive name for the CTI route point. |
| Call
                                                         							 Control Group | Choose the call control group to associate with the trigger from
                                                         							 this drop-down menu. For Outbound IVR Dialer, you must select the call control
                                                         							 group from Outbound type call control group list. The route point should be
                                                         							 created on Unified CM. Once you assign the Outbound group for a trigger, you
                                                         							 cannot change it to an Inbound group and vice versa. |
| Advanced Configuration (available only if you click Show More ). |
| Advanced Trigger
                                                            								Information |
| Enabled | Radio buttons to choose the required option: Yes— enable the trigger (default) No— disable the trigger. |
| Maximum Number of Sessions | The
                                                         							 maximum number of simultaneous calls that this trigger can handle. The number
                                                         							 is actually governed by the Unified CM (10,000 for each separate line). However in Unified CCX, this number is
                                                         							 restricted to the maximum number of sessions. Any call after this number is
                                                         							 exceeded gets the busy tone. |
| Idle
                                                         							 Timeout (in ms) | The
                                                         							 number of milliseconds (ms) the system should wait before rejecting the Unified
                                                         							 CM Telephony request for this trigger. |
| Override Media Termination | Radio buttons to choose the required options: Yes— Override media
                                                         							 termination. No— Enable media
                                                         							 termination (default). If
                                                         							 you select Yes, two panes open: Selected Dialog Groups displays the default or selected group. Available Dialog Groups lists the configured dialog. |
| CTI Route Point
                                                            								Information |
| Alerting Name ASCII | This
                                                         							 information is automatically populated based on the configuration in the
                                                         							 Unified CM setup and displays the ASCII name filed used in one of the following
                                                         							 situations: If the device is not capable of handling the Unicode strings If the locals on endpoint devices do not match If the Unicode string is not specified |
| Device Pool | The
                                                         							 device pool to which you want to assign this route point. A device pool defines
                                                         							 sets of common characteristics for devices, such as region, date/time group,
                                                         							 softkey template, and MLPP information. |
| Location | The
                                                         							 total bandwidth that is available for calls to/from this location. A location
                                                         							 setting of HUB_NONE indicates that the locations feature does not keep
                                                         							 track of the bandwidth used by this route point. |
| Directory Number Settings |
| Partition | The
                                                         							 partition to which the Directory Number belongs. The Directory Number field
                                                         							 value must be unique within the partition that you choose. If
                                                         							 you do not want to restrict access to the Directory Number, select < None > as the
                                                         							 partition setting. |
| Voice Mail Profile | A
                                                         							 list of profiles defined in the Voice Mail Profile Configuration. The
                                                         							 first option is < None >, which is the current default Voice Mail Profile
                                                         							 that is configured in the Voice Mail Profile Configuration. |
| Calling Search Space | A
                                                         							 collection of partitions that are searched for numbers that are called from
                                                         							 this directory number. The specified value applies to all devices that use this
                                                         							 directory number. For
                                                         							 example, assume you have two calling search spaces: Building and PSTN. Building
                                                         							 only allows users to call within the building, while PSTN allows users to call
                                                         							 both in and outside the building. You could assign the phone to the Building
                                                         							 calling search space and the line on your phone to the PSTN calling search
                                                         							 space. For more information, see the System Configuration Guide for Cisco Unified Communications Manager . |
| Calling Search Space for Redirect | By
                                                         							 default, Cisco Unified Communications Manager uses the original calling party's
                                                         							 calling search space (CSS) to process the redirected call from a Unified CCX
                                                         							 Trigger to a Unified CCX CTI Port. This default behavior requires the partition
                                                         							 of the Unified CCX CTI ports to be a member of the original calling party's CSS
                                                         							 even if the partition of the CTI Route Point/Unified CCX Trigger is accessible
                                                         							 to the calling device's CSS and the CSS of the CTI Route Point/Unified CCX
                                                         							 Trigger contains the partition of the Unified CCX CTI Ports. You
                                                         							 can modify this behavior using the drop-down list to instruct Cisco Unified
                                                         							 Communications Manager which CSS to use when redirecting the call from the CTI
                                                         							 Route Point to the CTI Port. Calling Search Space for Redirect options: Default
                                                                  									 Calling Search Space— CSS of the calling device Calling
                                                                  									 Address Search Space— CSS of the calling device Route
                                                                  									 Point Address Search Space— CSS of the CTI Route Point (Trigger) |
| Presence Group | A
                                                         							 list of groups to integrate the device with the iPass server. The device/line
                                                         							 information is provided for integrating applications. |
| Call Forward and Pickup
                                                            								Settings |
| Forward Busy | Check one of the following options: Voice Mail— Check this
                                                         							 box to use settings in the Voice Mail Profile Configuration window. Note When this box is checked, Unified CM ignores the settings in the
                                                                     								Destination box and Calling Search Space. Destination— To use any
                                                         							 disable phone number, including an outside destination. Calling Search Space— To apply the above setting all devices that are using this directory number. Note For limiting the number of calls per application in Unified CCX system, see the Unified CM Telephony Triggers for Unified CCX Queuing section. | Note | When this box is checked, Unified CM ignores the settings in the
                                                                     								Destination box and Calling Search Space. | Note | For limiting the number of calls per application in Unified CCX system, see the Unified CM Telephony Triggers for Unified CCX Queuing section. |
| Note | When this box is checked, Unified CM ignores the settings in the
                                                                     								Destination box and Calling Search Space. |
| Note | For limiting the number of calls per application in Unified CCX system, see the Unified CM Telephony Triggers for Unified CCX Queuing section. |
| Display | Use
                                                         							 a maximum of 30 alphanumeric characters. Typically, use the user name or the
                                                         							 directory number (if using the directory number, the person receiving the call
                                                         							 may not see the proper identity of the caller). Leave this field blank to have
                                                         							 the system display an extension. |
| External Phone Number Mask | Phone number (or mask) that is used to send Caller ID
                                                         							 information when a call is placed from this line. You
                                                         							 can enter a maximum of 24 number, the international escape character +, *, #
                                                         							 and "X" characters. The X characters represent the directory number and must
                                                         							 appear at the end of the pattern. For example, if you specify a mask of
                                                         							 972813XXXX, an external call from extension 1234 displays a caller ID number of
                                                         							 9728131234. |

| Note | +1234 and 1234 are two different directory numbers. The square brackets ([ ]) enclose a range of values. For more information, see the "Wildcards and Special Characters in Route Patterns and Hunt Pilots" section in the System Configuration Guide for Cisco Unified Communications Manager . |
|---|---|

| Note | Use of two(2) wildcard CTI Route Points that overlap
                                                                     								with each other is not supported. For example, Route Point 1: 123XXXX and Route
                                                                     								Point 2: 1234XXX overlap with one another and is not supported. However, a wildcard CTI Route point can overlap with
                                                                     								a full DID (best match pattern) that doesn't contain a wildcard. For example,
                                                                     								Route Point 1: 123XXXX and Route Point 2: 1234567 is supported. |
|---|---|

| Note | To
                                                                     								add a Language option, click Edit button. The User Prompt dialog box opens. Enter
                                                                     								a locale string value and click OK . The User Prompt dialog box closes, and the name
                                                                     								of the language opens in the Language field in the Unified CM Telephony
                                                                     								Configuration web page. |
|---|---|

| Note | When this box is checked, Unified CM ignores the settings in the
                                                                     								Destination box and Calling Search Space. |
|---|---|

| Note | For limiting the number of calls per application in Unified CCX system, see the Unified CM Telephony Triggers for Unified CCX Queuing section. |
|---|---|

| Note | The built-in
                                       		  grammars and grammar options that are supported by Unified CCX when using an
                                       		  MRCP dialog channel is determined by the MRCP speech software you purchase. See
                                       		  the software vendor for information about what built-in grammars and features
                                       		  are supported. |
|---|---|

| Caution | All media
                                       		  termination strings begin with auto and contain
                                       		  the same ID as the call control group—not the CMT dialog group. If the default
                                       		  media termination is configured and the ID differs, follow the procedure
                                       		  provided in the Add CMT Dialog
                                          			 Control Group . |
|---|---|

| Step 1 | From the Unified
                                          			 CCX Administration menu bar, choose Subsystems > Cisco
                                                				  Media . The Cisco Media Termination Dialog Group Configuration web page opens. Any preconfigured entry is listed on this page with
                                             the following information: Field Description GroupID The unique Group ID associated with the media. Description CMT group description. Note The ID in this field need not necessarily match the CMT group ID. Channels Number of channels associated with the group. | Field | Description | GroupID | The unique Group ID associated with the media. | Description | CMT group description. Note The ID in this field need not necessarily match the CMT group ID. | Note | The ID in this field need not necessarily match the CMT group ID. | Channels | Number of channels associated with the group. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Field | Description |
| GroupID | The unique Group ID associated with the media. |
| Description | CMT group description. Note The ID in this field need not necessarily match the CMT group ID. | Note | The ID in this field need not necessarily match the CMT group ID. |
| Note | The ID in this field need not necessarily match the CMT group ID. |
| Channels | Number of channels associated with the group. |
| Step 2 | Click Add
                                             				New icon at the top or Add
                                             				New button at the bottom of the window. The Cisco Media Termination
                                          			 Dialog Group Configuration web page opens. Note By default, a
                                                         				  Unified CM Telephony Call Control Group with Group ID 0 is created. | Note | By default, a
                                                         				  Unified CM Telephony Call Control Group with Group ID 0 is created. |
| Note | By default, a
                                                         				  Unified CM Telephony Call Control Group with Group ID 0 is created. |
| Step 3 | Use this web
                                          			 page to specify the following fields. Field Description Group
                                                         							 ID A
                                                         							 Group ID value unique within all media group identifiers, including ASR group
                                                         							 identifiers. This is a mandatory field. Description Description for the Cisco Media Termination Dialog group. Number
                                                         							 of Licensed IVR ports Number
                                                         							 of licensed IVR ports. Display only. Maximum Number Of Channels Maximum number of channels associated with this group. This is a
                                                         							 mandatory field. Note You
                                                                     								can specify any value for Maximum Number Of Channels, but restrictions are
                                                                     								placed on the system when a call is made. This restriction is imposed by the
                                                                     								number of licensed IVR ports on your system. This is a mandatory field. | Field | Description | Group
                                                         							 ID | A
                                                         							 Group ID value unique within all media group identifiers, including ASR group
                                                         							 identifiers. This is a mandatory field. | Description | Description for the Cisco Media Termination Dialog group. | Number
                                                         							 of Licensed IVR ports | Number
                                                         							 of licensed IVR ports. Display only. | Maximum Number Of Channels | Maximum number of channels associated with this group. This is a
                                                         							 mandatory field. Note You
                                                                     								can specify any value for Maximum Number Of Channels, but restrictions are
                                                                     								placed on the system when a call is made. This restriction is imposed by the
                                                                     								number of licensed IVR ports on your system. This is a mandatory field. | Note | You
                                                                     								can specify any value for Maximum Number Of Channels, but restrictions are
                                                                     								placed on the system when a call is made. This restriction is imposed by the
                                                                     								number of licensed IVR ports on your system. This is a mandatory field. |
| Field | Description |
| Group
                                                         							 ID | A
                                                         							 Group ID value unique within all media group identifiers, including ASR group
                                                         							 identifiers. This is a mandatory field. |
| Description | Description for the Cisco Media Termination Dialog group. |
| Number
                                                         							 of Licensed IVR ports | Number
                                                         							 of licensed IVR ports. Display only. |
| Maximum Number Of Channels | Maximum number of channels associated with this group. This is a
                                                         							 mandatory field. Note You
                                                                     								can specify any value for Maximum Number Of Channels, but restrictions are
                                                                     								placed on the system when a call is made. This restriction is imposed by the
                                                                     								number of licensed IVR ports on your system. This is a mandatory field. | Note | You
                                                                     								can specify any value for Maximum Number Of Channels, but restrictions are
                                                                     								placed on the system when a call is made. This restriction is imposed by the
                                                                     								number of licensed IVR ports on your system. This is a mandatory field. |
| Note | You
                                                                     								can specify any value for Maximum Number Of Channels, but restrictions are
                                                                     								placed on the system when a call is made. This restriction is imposed by the
                                                                     								number of licensed IVR ports on your system. This is a mandatory field. |
| Step 4 | Click Add icon that displays in the tool bar in the upper
                                          			 left corner of the window or the Add button that displays at the bottom of the
                                          			 window. The CMT Dialog
                                             				Group Configuration web page opens, displaying the new CMT dialog group. You are now
                                             				ready to provision MRCP ASR and MRCP TTS subsystems. |

| Field | Description |
|---|---|
| GroupID | The unique Group ID associated with the media. |
| Description | CMT group description. Note The ID in this field need not necessarily match the CMT group ID. | Note | The ID in this field need not necessarily match the CMT group ID. |
| Note | The ID in this field need not necessarily match the CMT group ID. |
| Channels | Number of channels associated with the group. |

| Note | The ID in this field need not necessarily match the CMT group ID. |
|---|---|

| Note | By default, a
                                                         				  Unified CM Telephony Call Control Group with Group ID 0 is created. |
|---|---|

| Field | Description |
|---|---|
| Group
                                                         							 ID | A
                                                         							 Group ID value unique within all media group identifiers, including ASR group
                                                         							 identifiers. This is a mandatory field. |
| Description | Description for the Cisco Media Termination Dialog group. |
| Number
                                                         							 of Licensed IVR ports | Number
                                                         							 of licensed IVR ports. Display only. |
| Maximum Number Of Channels | Maximum number of channels associated with this group. This is a
                                                         							 mandatory field. Note You
                                                                     								can specify any value for Maximum Number Of Channels, but restrictions are
                                                                     								placed on the system when a call is made. This restriction is imposed by the
                                                                     								number of licensed IVR ports on your system. This is a mandatory field. | Note | You
                                                                     								can specify any value for Maximum Number Of Channels, but restrictions are
                                                                     								placed on the system when a call is made. This restriction is imposed by the
                                                                     								number of licensed IVR ports on your system. This is a mandatory field. |
| Note | You
                                                                     								can specify any value for Maximum Number Of Channels, but restrictions are
                                                                     								placed on the system when a call is made. This restriction is imposed by the
                                                                     								number of licensed IVR ports on your system. This is a mandatory field. |

| Note | You
                                                                     								can specify any value for Maximum Number Of Channels, but restrictions are
                                                                     								placed on the system when a call is made. This restriction is imposed by the
                                                                     								number of licensed IVR ports on your system. This is a mandatory field. |
|---|---|

| Note | Only G.711 codec is supported for ASR/TTS integrations. |
|---|---|

| Note | For more information on supported speech servers for Unified CCX, see the Unified CCX Compatibility related information, located
                                                at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html . |
|---|---|

| Step 1 | From the Unified
                                             			 CCX Administration menu bar, choose Subsystem > MRCP
                                                   				  ASR > MRCP ASR Providers . The MRCP ASR
                                                				Provider Configuration web page opens, displaying the list of currently
                                                				configured MRCP providers, licenses, and the corresponding status. |
|---|---|
| Step 2 | Click Add
                                                				New icon that displays in the tool bar in the upper left corner of
                                             			 the window or the Add
                                                				New button that is displayed at the bottom of the window. The MRCP ASR
                                                				Provider Configuration web page opens. |
| Step 3 | Specify the
                                             			 following mandatory fields: Field Description Provider Name Enter
                                                            							 the name of the MRCP ASR provider supported by Unified CCX. Number
                                                            							 of Provider Licenses The
                                                            							 number of ASR port licenses purchased from the ASR vendor. Grammar Variant Vendor-specific grammar setting. Valid options: Nuance Open Speech Recognizer servers version 9.0 and above (OSR 3.1.x) Nuance 11.x and below version ASR servers (Nuance) IBM WVS ASR servers (2003 SISR) | Field | Description | Provider Name | Enter
                                                            							 the name of the MRCP ASR provider supported by Unified CCX. | Number
                                                            							 of Provider Licenses | The
                                                            							 number of ASR port licenses purchased from the ASR vendor. | Grammar Variant | Vendor-specific grammar setting. Valid options: Nuance Open Speech Recognizer servers version 9.0 and above (OSR 3.1.x) Nuance 11.x and below version ASR servers (Nuance) IBM WVS ASR servers (2003 SISR) |
| Field | Description |
| Provider Name | Enter
                                                            							 the name of the MRCP ASR provider supported by Unified CCX. |
| Number
                                                            							 of Provider Licenses | The
                                                            							 number of ASR port licenses purchased from the ASR vendor. |
| Grammar Variant | Vendor-specific grammar setting. Valid options: Nuance Open Speech Recognizer servers version 9.0 and above (OSR 3.1.x) Nuance 11.x and below version ASR servers (Nuance) IBM WVS ASR servers (2003 SISR) |
| Step 4 | Click Add icon in the tool bar in the upper left corner of
                                             			 the window or the Add button that displays at the bottom of this
                                             			 window to apply changes. Note After you update MRCP ASR/TTS Providers, Servers, and Groups, the corresponding provider needs to be refreshed for changes
                                                            to take effect. The Unified CCX Engine does not need to be restarted. However, during a Refresh, Unified CM Telephony triggers
                                                            using affected groups will fall back to the dialog group that is configured and the MRCP Provider being refreshed will go
                                                            NOT_CONFIGURED until the reload is complete. Your changes
                                                				appear in the MRCP ASR Providers List page. You are now ready to provision MRCP
                                                				ASR Servers. Note If you delete
                                                            				  an ASR/TTS provider and all of its associated servers and then create a new
                                                            				  ASR/TTS provider, its status might become IN_SERVICE immediately, even before
                                                            				  you create any servers for it. In this situation, click Refresh for that ASR/TTS provider, or click Refresh All. These actions change the status of the
                                                            				  ASR/TTS provider to NOT_CONFIGURED. | Note | After you update MRCP ASR/TTS Providers, Servers, and Groups, the corresponding provider needs to be refreshed for changes
                                                            to take effect. The Unified CCX Engine does not need to be restarted. However, during a Refresh, Unified CM Telephony triggers
                                                            using affected groups will fall back to the dialog group that is configured and the MRCP Provider being refreshed will go
                                                            NOT_CONFIGURED until the reload is complete. | Note | If you delete
                                                            				  an ASR/TTS provider and all of its associated servers and then create a new
                                                            				  ASR/TTS provider, its status might become IN_SERVICE immediately, even before
                                                            				  you create any servers for it. In this situation, click Refresh for that ASR/TTS provider, or click Refresh All. These actions change the status of the
                                                            				  ASR/TTS provider to NOT_CONFIGURED. |
| Note | After you update MRCP ASR/TTS Providers, Servers, and Groups, the corresponding provider needs to be refreshed for changes
                                                            to take effect. The Unified CCX Engine does not need to be restarted. However, during a Refresh, Unified CM Telephony triggers
                                                            using affected groups will fall back to the dialog group that is configured and the MRCP Provider being refreshed will go
                                                            NOT_CONFIGURED until the reload is complete. |
| Note | If you delete
                                                            				  an ASR/TTS provider and all of its associated servers and then create a new
                                                            				  ASR/TTS provider, its status might become IN_SERVICE immediately, even before
                                                            				  you create any servers for it. In this situation, click Refresh for that ASR/TTS provider, or click Refresh All. These actions change the status of the
                                                            				  ASR/TTS provider to NOT_CONFIGURED. |

| Field | Description |
|---|---|
| Provider Name | Enter
                                                            							 the name of the MRCP ASR provider supported by Unified CCX. |
| Number
                                                            							 of Provider Licenses | The
                                                            							 number of ASR port licenses purchased from the ASR vendor. |
| Grammar Variant | Vendor-specific grammar setting. Valid options: Nuance Open Speech Recognizer servers version 9.0 and above (OSR 3.1.x) Nuance 11.x and below version ASR servers (Nuance) IBM WVS ASR servers (2003 SISR) |

| Note | After you update MRCP ASR/TTS Providers, Servers, and Groups, the corresponding provider needs to be refreshed for changes
                                                            to take effect. The Unified CCX Engine does not need to be restarted. However, during a Refresh, Unified CM Telephony triggers
                                                            using affected groups will fall back to the dialog group that is configured and the MRCP Provider being refreshed will go
                                                            NOT_CONFIGURED until the reload is complete. |
|---|---|

| Note | If you delete
                                                            				  an ASR/TTS provider and all of its associated servers and then create a new
                                                            				  ASR/TTS provider, its status might become IN_SERVICE immediately, even before
                                                            				  you create any servers for it. In this situation, click Refresh for that ASR/TTS provider, or click Refresh All. These actions change the status of the
                                                            				  ASR/TTS provider to NOT_CONFIGURED. |
|---|---|

| Note | You must have an MRCP ASR Provider defined before you can provision an MRCP ASR Server. |
|---|---|

| Step 1 | From the Unified CCX Administration menu bar, choose Subsystem > MRCP ASR > MRCP ASR Servers . The MRCP ASR Server Configuration web page opens, displaying a list of previously configured servers, if applicable with the
                                                following information: Column Description Computer Name Hostname or IP address in which the ASR server software is installed. Note ASR server deployment over WAN is not supported in Unified CCX. The ASR server should be in the same LAN where Unified CCX
                                                                        is. You need to specify the ASR server hostname or IP address that is local with the Unified CCX node while installing the
                                                                        ASR server software in this field. Provider The MRCP ASR Provider to which this server is associated. Port The default TCP port number that is used to connect to a MRCP server. OSR 3.1.x—4900 for MRCPv1 and 5060 for MRCPv2 2003 SISR—554 Nuance—554 Status Status or state of the subsystem. | Column | Description | Computer Name | Hostname or IP address in which the ASR server software is installed. Note ASR server deployment over WAN is not supported in Unified CCX. The ASR server should be in the same LAN where Unified CCX
                                                                        is. You need to specify the ASR server hostname or IP address that is local with the Unified CCX node while installing the
                                                                        ASR server software in this field. | Note | ASR server deployment over WAN is not supported in Unified CCX. The ASR server should be in the same LAN where Unified CCX
                                                                        is. You need to specify the ASR server hostname or IP address that is local with the Unified CCX node while installing the
                                                                        ASR server software in this field. | Provider | The MRCP ASR Provider to which this server is associated. | Port | The default TCP port number that is used to connect to a MRCP server. OSR 3.1.x—4900 for MRCPv1 and 5060 for MRCPv2 2003 SISR—554 Nuance—554 | Status | Status or state of the subsystem. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Column | Description |
| Computer Name | Hostname or IP address in which the ASR server software is installed. Note ASR server deployment over WAN is not supported in Unified CCX. The ASR server should be in the same LAN where Unified CCX
                                                                        is. You need to specify the ASR server hostname or IP address that is local with the Unified CCX node while installing the
                                                                        ASR server software in this field. | Note | ASR server deployment over WAN is not supported in Unified CCX. The ASR server should be in the same LAN where Unified CCX
                                                                        is. You need to specify the ASR server hostname or IP address that is local with the Unified CCX node while installing the
                                                                        ASR server software in this field. |
| Note | ASR server deployment over WAN is not supported in Unified CCX. The ASR server should be in the same LAN where Unified CCX
                                                                        is. You need to specify the ASR server hostname or IP address that is local with the Unified CCX node while installing the
                                                                        ASR server software in this field. |
| Provider | The MRCP ASR Provider to which this server is associated. |
| Port | The default TCP port number that is used to connect to a MRCP server. OSR 3.1.x—4900 for MRCPv1 and 5060 for MRCPv2 2003 SISR—554 Nuance—554 |
| Status | Status or state of the subsystem. |
| Step 2 | Click Add New icon that is displayed in the tool bar in the upper, left corner of the window or the Add New button that is displayed at the bottom of the window to provision a new MRCP ASR Server. The MRCP ASR Server Configuration web page opens. |
| Step 3 | Use this web page to specify the following fields. Field Description Server Name Hostname or IP address of the server where the MRCP ASR server software is installed. Provider Name Select the name of the MRCP ASR Provider to which this server is associated from this drop-down list. Port Number The default TCP port number that is used to connect to a MRCP server. Though the default value is shown as 4900. You need
                                                            to provide any one of the following values in this field based on the TCP provider or grammar variant you have selected while
                                                            configuring an MRCP ASR provider: OSR 3.1.x—4900 for MRCPv1 and 5060 for MRCPv2 2003 SISR—554 Nuance—554 Locales Languages supported by the ASR Provider. Select a language (or multiple languages) from the drop-down list and click Add Language ; the selected language appears with a check box in the Enabled Languages list. Note Use the check box to enable or disable a language. | Field | Description | Server Name | Hostname or IP address of the server where the MRCP ASR server software is installed. | Provider Name | Select the name of the MRCP ASR Provider to which this server is associated from this drop-down list. | Port Number | The default TCP port number that is used to connect to a MRCP server. Though the default value is shown as 4900. You need
                                                            to provide any one of the following values in this field based on the TCP provider or grammar variant you have selected while
                                                            configuring an MRCP ASR provider: OSR 3.1.x—4900 for MRCPv1 and 5060 for MRCPv2 2003 SISR—554 Nuance—554 | Locales | Languages supported by the ASR Provider. Select a language (or multiple languages) from the drop-down list and click Add Language ; the selected language appears with a check box in the Enabled Languages list. Note Use the check box to enable or disable a language. | Note | Use the check box to enable or disable a language. |
| Field | Description |
| Server Name | Hostname or IP address of the server where the MRCP ASR server software is installed. |
| Provider Name | Select the name of the MRCP ASR Provider to which this server is associated from this drop-down list. |
| Port Number | The default TCP port number that is used to connect to a MRCP server. Though the default value is shown as 4900. You need
                                                            to provide any one of the following values in this field based on the TCP provider or grammar variant you have selected while
                                                            configuring an MRCP ASR provider: OSR 3.1.x—4900 for MRCPv1 and 5060 for MRCPv2 2003 SISR—554 Nuance—554 |
| Locales | Languages supported by the ASR Provider. Select a language (or multiple languages) from the drop-down list and click Add Language ; the selected language appears with a check box in the Enabled Languages list. Note Use the check box to enable or disable a language. | Note | Use the check box to enable or disable a language. |
| Note | Use the check box to enable or disable a language. |
| Step 4 | Click Add to apply changes. Your changes appear in the MRCP ASR Server list web page. You are now ready to provision MRCP ASR Groups. |

| Column | Description |
|---|---|
| Computer Name | Hostname or IP address in which the ASR server software is installed. Note ASR server deployment over WAN is not supported in Unified CCX. The ASR server should be in the same LAN where Unified CCX
                                                                        is. You need to specify the ASR server hostname or IP address that is local with the Unified CCX node while installing the
                                                                        ASR server software in this field. | Note | ASR server deployment over WAN is not supported in Unified CCX. The ASR server should be in the same LAN where Unified CCX
                                                                        is. You need to specify the ASR server hostname or IP address that is local with the Unified CCX node while installing the
                                                                        ASR server software in this field. |
| Note | ASR server deployment over WAN is not supported in Unified CCX. The ASR server should be in the same LAN where Unified CCX
                                                                        is. You need to specify the ASR server hostname or IP address that is local with the Unified CCX node while installing the
                                                                        ASR server software in this field. |
| Provider | The MRCP ASR Provider to which this server is associated. |
| Port | The default TCP port number that is used to connect to a MRCP server. OSR 3.1.x—4900 for MRCPv1 and 5060 for MRCPv2 2003 SISR—554 Nuance—554 |
| Status | Status or state of the subsystem. |

| Note | ASR server deployment over WAN is not supported in Unified CCX. The ASR server should be in the same LAN where Unified CCX
                                                                        is. You need to specify the ASR server hostname or IP address that is local with the Unified CCX node while installing the
                                                                        ASR server software in this field. |
|---|---|

| Field | Description |
|---|---|
| Server Name | Hostname or IP address of the server where the MRCP ASR server software is installed. |
| Provider Name | Select the name of the MRCP ASR Provider to which this server is associated from this drop-down list. |
| Port Number | The default TCP port number that is used to connect to a MRCP server. Though the default value is shown as 4900. You need
                                                            to provide any one of the following values in this field based on the TCP provider or grammar variant you have selected while
                                                            configuring an MRCP ASR provider: OSR 3.1.x—4900 for MRCPv1 and 5060 for MRCPv2 2003 SISR—554 Nuance—554 |
| Locales | Languages supported by the ASR Provider. Select a language (or multiple languages) from the drop-down list and click Add Language ; the selected language appears with a check box in the Enabled Languages list. Note Use the check box to enable or disable a language. | Note | Use the check box to enable or disable a language. |
| Note | Use the check box to enable or disable a language. |

| Note | Use the check box to enable or disable a language. |
|---|---|

| Note | You must have a MRCP ASR Provider defined before you can provision a
                                                			 MRCP ASR Group. Also, you should configure MRCP ASR Servers for the specific
                                                			 MRCP Provider before configuring the MRCP ASR Groups. This allows users to
                                                			 configure languages for the groups based on the languages supported by the
                                                			 configured servers. |
|---|---|

| Step 1 | From the Unified CCX Administration menu bar, choose Subsystem > MRCP
                                                   				  ASR > MRCP ASR Dialog Groups . The MRCP ASR Dialog Group Configuration web page opens to display a list of preconfigured entries, if applicable with the
                                                following information: Field Description Group ID Identifier for the group. Description Description of this dialog group. Provider Name of the MRCP ASR provider. Channels Maximum number of sessions. This web page also displays the Number of Licensed IVR
                                                				Channels. | Field | Description | Group ID | Identifier for the group. | Description | Description of this dialog group. | Provider | Name of the MRCP ASR provider. | Channels | Maximum number of sessions. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Field | Description |
| Group ID | Identifier for the group. |
| Description | Description of this dialog group. |
| Provider | Name of the MRCP ASR provider. |
| Channels | Maximum number of sessions. |
| Step 2 | Click Add New icon that displays in the tool bar in
                                             			 the upper, left corner of the window or the Add New button that displays at the bottom of
                                             			 the window to provision a MRCP ASR Group. The MRCP ASR Dialog Group Configuration web page opens. |
| Step 3 | Use this web page to specify the following fields: Field Description Group ID Associated group ID. Description Description of this dialog group. Tip Include languages that will be used by
                                                                     							 this Group to the description. Doing so will provide insight into the languages
                                                                     							 this Group uses when you set up the dialog group in the Unified CM Telephony
                                                                     							 trigger configuration. This also ensures that the locales used by the
                                                                     							 application configured in the Unified CM Telephony trigger match the locales
                                                                     							 supported by the MRCP ASR dialog group being selected. Number Of Provider Licenses Display only. Number Of Licensed IVR Ports Display only. Maximum Number Of sessions Maximum number of sessions associated with this dialog
                                                            							 group. Note You can assign any value for Maximum Number Of
                                                                        								Channels, but restrictions are placed on the system when a call is made. This
                                                                        								restriction is imposed by the number of licensed IVR ports on your system. Caution Under heavy load, calls that utilize a channel from an
                                                                        								MRCP ASR Dialog Control Group, might have a reduced call completion rate as the
                                                                        								MRCP channels used by calls can take some additional time to clean up all the
                                                                        								sessions set up with MRCP resources. To address this situation, you can
                                                                        								overprovision the value of this field by a factor of 1.2 or by an additional 20
                                                                        								percent. For example, if your application requires 100 MRCP ASR channels, modify the value in this field to be 120
                                                                        MRCP ASR channels. Provider Name Select a MRCP Provider name from the drop-down list that
                                                            							 contains a list of all previously defined provider names. Enabled Languages Select the languages that you wish to configure for this
                                                            							 group from the list displayed. The displayed languages represent the locales configured
                                                            							 for all MRCP ASR servers for the specified provider. If there are no MRCP ASR
                                                            							 servers configured, no languages are displayed. In this case, you must update the group configuration once MRCP ASR
                                                            servers have been configured for
                                                            							 the specified provider. | Field | Description | Group ID | Associated group ID. | Description | Description of this dialog group. Tip Include languages that will be used by
                                                                     							 this Group to the description. Doing so will provide insight into the languages
                                                                     							 this Group uses when you set up the dialog group in the Unified CM Telephony
                                                                     							 trigger configuration. This also ensures that the locales used by the
                                                                     							 application configured in the Unified CM Telephony trigger match the locales
                                                                     							 supported by the MRCP ASR dialog group being selected. | Tip | Include languages that will be used by
                                                                     							 this Group to the description. Doing so will provide insight into the languages
                                                                     							 this Group uses when you set up the dialog group in the Unified CM Telephony
                                                                     							 trigger configuration. This also ensures that the locales used by the
                                                                     							 application configured in the Unified CM Telephony trigger match the locales
                                                                     							 supported by the MRCP ASR dialog group being selected. | Number Of Provider Licenses | Display only. | Number Of Licensed IVR Ports | Display only. | Maximum Number Of sessions | Maximum number of sessions associated with this dialog
                                                            							 group. Note You can assign any value for Maximum Number Of
                                                                        								Channels, but restrictions are placed on the system when a call is made. This
                                                                        								restriction is imposed by the number of licensed IVR ports on your system. Caution Under heavy load, calls that utilize a channel from an
                                                                        								MRCP ASR Dialog Control Group, might have a reduced call completion rate as the
                                                                        								MRCP channels used by calls can take some additional time to clean up all the
                                                                        								sessions set up with MRCP resources. To address this situation, you can
                                                                        								overprovision the value of this field by a factor of 1.2 or by an additional 20
                                                                        								percent. For example, if your application requires 100 MRCP ASR channels, modify the value in this field to be 120
                                                                        MRCP ASR channels. | Note | You can assign any value for Maximum Number Of
                                                                        								Channels, but restrictions are placed on the system when a call is made. This
                                                                        								restriction is imposed by the number of licensed IVR ports on your system. | Caution | Under heavy load, calls that utilize a channel from an
                                                                        								MRCP ASR Dialog Control Group, might have a reduced call completion rate as the
                                                                        								MRCP channels used by calls can take some additional time to clean up all the
                                                                        								sessions set up with MRCP resources. To address this situation, you can
                                                                        								overprovision the value of this field by a factor of 1.2 or by an additional 20
                                                                        								percent. For example, if your application requires 100 MRCP ASR channels, modify the value in this field to be 120
                                                                        MRCP ASR channels. | Provider Name | Select a MRCP Provider name from the drop-down list that
                                                            							 contains a list of all previously defined provider names. | Enabled Languages | Select the languages that you wish to configure for this
                                                            							 group from the list displayed. The displayed languages represent the locales configured
                                                            							 for all MRCP ASR servers for the specified provider. If there are no MRCP ASR
                                                            							 servers configured, no languages are displayed. In this case, you must update the group configuration once MRCP ASR
                                                            servers have been configured for
                                                            							 the specified provider. |
| Field | Description |
| Group ID | Associated group ID. |
| Description | Description of this dialog group. Tip Include languages that will be used by
                                                                     							 this Group to the description. Doing so will provide insight into the languages
                                                                     							 this Group uses when you set up the dialog group in the Unified CM Telephony
                                                                     							 trigger configuration. This also ensures that the locales used by the
                                                                     							 application configured in the Unified CM Telephony trigger match the locales
                                                                     							 supported by the MRCP ASR dialog group being selected. | Tip | Include languages that will be used by
                                                                     							 this Group to the description. Doing so will provide insight into the languages
                                                                     							 this Group uses when you set up the dialog group in the Unified CM Telephony
                                                                     							 trigger configuration. This also ensures that the locales used by the
                                                                     							 application configured in the Unified CM Telephony trigger match the locales
                                                                     							 supported by the MRCP ASR dialog group being selected. |
| Tip | Include languages that will be used by
                                                                     							 this Group to the description. Doing so will provide insight into the languages
                                                                     							 this Group uses when you set up the dialog group in the Unified CM Telephony
                                                                     							 trigger configuration. This also ensures that the locales used by the
                                                                     							 application configured in the Unified CM Telephony trigger match the locales
                                                                     							 supported by the MRCP ASR dialog group being selected. |
| Number Of Provider Licenses | Display only. |
| Number Of Licensed IVR Ports | Display only. |
| Maximum Number Of sessions | Maximum number of sessions associated with this dialog
                                                            							 group. Note You can assign any value for Maximum Number Of
                                                                        								Channels, but restrictions are placed on the system when a call is made. This
                                                                        								restriction is imposed by the number of licensed IVR ports on your system. Caution Under heavy load, calls that utilize a channel from an
                                                                        								MRCP ASR Dialog Control Group, might have a reduced call completion rate as the
                                                                        								MRCP channels used by calls can take some additional time to clean up all the
                                                                        								sessions set up with MRCP resources. To address this situation, you can
                                                                        								overprovision the value of this field by a factor of 1.2 or by an additional 20
                                                                        								percent. For example, if your application requires 100 MRCP ASR channels, modify the value in this field to be 120
                                                                        MRCP ASR channels. | Note | You can assign any value for Maximum Number Of
                                                                        								Channels, but restrictions are placed on the system when a call is made. This
                                                                        								restriction is imposed by the number of licensed IVR ports on your system. | Caution | Under heavy load, calls that utilize a channel from an
                                                                        								MRCP ASR Dialog Control Group, might have a reduced call completion rate as the
                                                                        								MRCP channels used by calls can take some additional time to clean up all the
                                                                        								sessions set up with MRCP resources. To address this situation, you can
                                                                        								overprovision the value of this field by a factor of 1.2 or by an additional 20
                                                                        								percent. For example, if your application requires 100 MRCP ASR channels, modify the value in this field to be 120
                                                                        MRCP ASR channels. |
| Note | You can assign any value for Maximum Number Of
                                                                        								Channels, but restrictions are placed on the system when a call is made. This
                                                                        								restriction is imposed by the number of licensed IVR ports on your system. |
| Caution | Under heavy load, calls that utilize a channel from an
                                                                        								MRCP ASR Dialog Control Group, might have a reduced call completion rate as the
                                                                        								MRCP channels used by calls can take some additional time to clean up all the
                                                                        								sessions set up with MRCP resources. To address this situation, you can
                                                                        								overprovision the value of this field by a factor of 1.2 or by an additional 20
                                                                        								percent. For example, if your application requires 100 MRCP ASR channels, modify the value in this field to be 120
                                                                        MRCP ASR channels. |
| Provider Name | Select a MRCP Provider name from the drop-down list that
                                                            							 contains a list of all previously defined provider names. |
| Enabled Languages | Select the languages that you wish to configure for this
                                                            							 group from the list displayed. The displayed languages represent the locales configured
                                                            							 for all MRCP ASR servers for the specified provider. If there are no MRCP ASR
                                                            							 servers configured, no languages are displayed. In this case, you must update the group configuration once MRCP ASR
                                                            servers have been configured for
                                                            							 the specified provider. |
| Step 4 | Click Add to apply changes. Your changes appear in the MRCP ASR Groups list web page. |

| Field | Description |
|---|---|
| Group ID | Identifier for the group. |
| Description | Description of this dialog group. |
| Provider | Name of the MRCP ASR provider. |
| Channels | Maximum number of sessions. |

| Field | Description |
|---|---|
| Group ID | Associated group ID. |
| Description | Description of this dialog group. Tip Include languages that will be used by
                                                                     							 this Group to the description. Doing so will provide insight into the languages
                                                                     							 this Group uses when you set up the dialog group in the Unified CM Telephony
                                                                     							 trigger configuration. This also ensures that the locales used by the
                                                                     							 application configured in the Unified CM Telephony trigger match the locales
                                                                     							 supported by the MRCP ASR dialog group being selected. | Tip | Include languages that will be used by
                                                                     							 this Group to the description. Doing so will provide insight into the languages
                                                                     							 this Group uses when you set up the dialog group in the Unified CM Telephony
                                                                     							 trigger configuration. This also ensures that the locales used by the
                                                                     							 application configured in the Unified CM Telephony trigger match the locales
                                                                     							 supported by the MRCP ASR dialog group being selected. |
| Tip | Include languages that will be used by
                                                                     							 this Group to the description. Doing so will provide insight into the languages
                                                                     							 this Group uses when you set up the dialog group in the Unified CM Telephony
                                                                     							 trigger configuration. This also ensures that the locales used by the
                                                                     							 application configured in the Unified CM Telephony trigger match the locales
                                                                     							 supported by the MRCP ASR dialog group being selected. |
| Number Of Provider Licenses | Display only. |
| Number Of Licensed IVR Ports | Display only. |
| Maximum Number Of sessions | Maximum number of sessions associated with this dialog
                                                            							 group. Note You can assign any value for Maximum Number Of
                                                                        								Channels, but restrictions are placed on the system when a call is made. This
                                                                        								restriction is imposed by the number of licensed IVR ports on your system. Caution Under heavy load, calls that utilize a channel from an
                                                                        								MRCP ASR Dialog Control Group, might have a reduced call completion rate as the
                                                                        								MRCP channels used by calls can take some additional time to clean up all the
                                                                        								sessions set up with MRCP resources. To address this situation, you can
                                                                        								overprovision the value of this field by a factor of 1.2 or by an additional 20
                                                                        								percent. For example, if your application requires 100 MRCP ASR channels, modify the value in this field to be 120
                                                                        MRCP ASR channels. | Note | You can assign any value for Maximum Number Of
                                                                        								Channels, but restrictions are placed on the system when a call is made. This
                                                                        								restriction is imposed by the number of licensed IVR ports on your system. | Caution | Under heavy load, calls that utilize a channel from an
                                                                        								MRCP ASR Dialog Control Group, might have a reduced call completion rate as the
                                                                        								MRCP channels used by calls can take some additional time to clean up all the
                                                                        								sessions set up with MRCP resources. To address this situation, you can
                                                                        								overprovision the value of this field by a factor of 1.2 or by an additional 20
                                                                        								percent. For example, if your application requires 100 MRCP ASR channels, modify the value in this field to be 120
                                                                        MRCP ASR channels. |
| Note | You can assign any value for Maximum Number Of
                                                                        								Channels, but restrictions are placed on the system when a call is made. This
                                                                        								restriction is imposed by the number of licensed IVR ports on your system. |
| Caution | Under heavy load, calls that utilize a channel from an
                                                                        								MRCP ASR Dialog Control Group, might have a reduced call completion rate as the
                                                                        								MRCP channels used by calls can take some additional time to clean up all the
                                                                        								sessions set up with MRCP resources. To address this situation, you can
                                                                        								overprovision the value of this field by a factor of 1.2 or by an additional 20
                                                                        								percent. For example, if your application requires 100 MRCP ASR channels, modify the value in this field to be 120
                                                                        MRCP ASR channels. |
| Provider Name | Select a MRCP Provider name from the drop-down list that
                                                            							 contains a list of all previously defined provider names. |
| Enabled Languages | Select the languages that you wish to configure for this
                                                            							 group from the list displayed. The displayed languages represent the locales configured
                                                            							 for all MRCP ASR servers for the specified provider. If there are no MRCP ASR
                                                            							 servers configured, no languages are displayed. In this case, you must update the group configuration once MRCP ASR
                                                            servers have been configured for
                                                            							 the specified provider. |

| Tip | Include languages that will be used by
                                                                     							 this Group to the description. Doing so will provide insight into the languages
                                                                     							 this Group uses when you set up the dialog group in the Unified CM Telephony
                                                                     							 trigger configuration. This also ensures that the locales used by the
                                                                     							 application configured in the Unified CM Telephony trigger match the locales
                                                                     							 supported by the MRCP ASR dialog group being selected. |
|---|---|

| Note | You can assign any value for Maximum Number Of
                                                                        								Channels, but restrictions are placed on the system when a call is made. This
                                                                        								restriction is imposed by the number of licensed IVR ports on your system. |
|---|---|

| Caution | Under heavy load, calls that utilize a channel from an
                                                                        								MRCP ASR Dialog Control Group, might have a reduced call completion rate as the
                                                                        								MRCP channels used by calls can take some additional time to clean up all the
                                                                        								sessions set up with MRCP resources. To address this situation, you can
                                                                        								overprovision the value of this field by a factor of 1.2 or by an additional 20
                                                                        								percent. For example, if your application requires 100 MRCP ASR channels, modify the value in this field to be 120
                                                                        MRCP ASR channels. |
|---|---|

| Note | If you delete an ASR/TTS provider and all of its associated
                                                				servers and then create a new ASR/TTS provider, its status might become
                                                				IN_SERVICE immediately, even before you create any servers for it. In this
                                                				situation, click Refresh for that ASR/TTS provider, or click Refresh All. These
                                                				actions change the status of the ASR/TTS provider to NOT_CONFIGURED. |
|---|---|

| Note | You will need at least one MRCP TTS Provider for each vendor requiring
                                          		  TTS server installation. |
|---|---|

| Note | After you update MRCP ASR/TTS Providers, Servers, and Groups, the
                                                			 corresponding provider needs to be refreshed for changes to take effect. The
                                                			 Unified CCX Engine does not need to be restarted. However, during a Refresh,
                                                			 Unified CM Telephony triggers using affected groups will fall back to the
                                                			 dialog group that is configured and the MRCP Provider being refreshed will go
                                                			 NOT_CONFIGURED until the reload is complete. |
|---|---|

| Step 1 | From the Unified CCX Administration menu bar, choose Subsystems > MRCP
                                                   				  TTS > MRCP TTS Provider . The MRCP TTS Provider Configuration web page opens. If providers
                                                				are already configured, this page lists the provider name and corresponding
                                                				status. |
|---|---|
| Step 2 | Click Add New icon that displays in the tool bar in
                                             			 the upper, left corner of the window or the Add New button that displays at the bottom of
                                             			 the window. Use this web page to specify the MRCP TTS Provider supported by
                                                				Unified CCX. The MRCP TTS Provider Configuration web page reopens. The Provider
                                                				Name drop-down list displays the existing MRCP TTS Providers. Choose the MRCP
                                                				TTS Provider supported by Unified CCX from this list. Note Support for High Availability and remote servers is available
                                                            				  only in multiple-server deployments. | Note | Support for High Availability and remote servers is available
                                                            				  only in multiple-server deployments. |
| Note | Support for High Availability and remote servers is available
                                                            				  only in multiple-server deployments. |
| Step 3 | Click Add to apply changes. Your changes appear in the MRCP TTS Provider Configuration web
                                                				page. You are now ready to provision MRCP TTS Servers. |

| Note | Support for High Availability and remote servers is available
                                                            				  only in multiple-server deployments. |
|---|---|

| Step 1 | Choose System > System
                                                      				  Parameters . |
|---|---|
| Step 2 | In the Default
                                                			 TTS Provider drop down list below Media Parameters section, select the provider
                                                			 you wish to be the system default. You must select only a preconfigured TTS
                                                			 provider as the Default TTS Provider. Note If you are deploying an VXML applications and the only TTS functionality you need is to play pre-recorded .wav files, select the Cisco LiteSSMLProcessor option as the Default TTS Provider. This option allows you to run SSML that has .wav file references in them. | Note | If you are deploying an VXML applications and the only TTS functionality you need is to play pre-recorded .wav files, select the Cisco LiteSSMLProcessor option as the Default TTS Provider. This option allows you to run SSML that has .wav file references in them. |
| Note | If you are deploying an VXML applications and the only TTS functionality you need is to play pre-recorded .wav files, select the Cisco LiteSSMLProcessor option as the Default TTS Provider. This option allows you to run SSML that has .wav file references in them. |
| Step 3 | Click Update . |

| Note | If you are deploying an VXML applications and the only TTS functionality you need is to play pre-recorded .wav files, select the Cisco LiteSSMLProcessor option as the Default TTS Provider. This option allows you to run SSML that has .wav file references in them. |
|---|---|

| Note | You must have an MRCP TTS Provider defined before you can provision an MRCP TTS Server. |
|---|---|

| Step 1 | From the Unified
                                             			 CCX Administration menu bar, choose Subsystems > MRCP
                                                   				  TTS > MRCP TTS Server . The MRCP TTS
                                                				Server Configuration web page opens, displaying a list of previously configured
                                                				servers, if applicable, with the following information: Column Description Computer Name Hostname or IP address of the server in which the TTS server software is installed. Note TTS server deployment over WAN is not supported in Unified CCX. In other words, the TTS server should be in the same LAN where
                                                                        Unified CCX is. Thus, you need to specify the TTS server hostname or IP address that is local with the Unified CCX node while
                                                                        installing the TTS server software in this field. Port TCP port number used to connect to an MRCP server. Following are the different TCP Provider names: MRCP Server Nuance Vocalizer Scansoft Realspeak Provider The
                                                            							 MRCP TTS Provider to which this server is associated. Status Status
                                                            							 or state of the subsystem. | Column | Description | Computer Name | Hostname or IP address of the server in which the TTS server software is installed. Note TTS server deployment over WAN is not supported in Unified CCX. In other words, the TTS server should be in the same LAN where
                                                                        Unified CCX is. Thus, you need to specify the TTS server hostname or IP address that is local with the Unified CCX node while
                                                                        installing the TTS server software in this field. | Note | TTS server deployment over WAN is not supported in Unified CCX. In other words, the TTS server should be in the same LAN where
                                                                        Unified CCX is. Thus, you need to specify the TTS server hostname or IP address that is local with the Unified CCX node while
                                                                        installing the TTS server software in this field. | Port | TCP port number used to connect to an MRCP server. Following are the different TCP Provider names: MRCP Server Nuance Vocalizer Scansoft Realspeak | Provider | The
                                                            							 MRCP TTS Provider to which this server is associated. | Status | Status
                                                            							 or state of the subsystem. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Column | Description |
| Computer Name | Hostname or IP address of the server in which the TTS server software is installed. Note TTS server deployment over WAN is not supported in Unified CCX. In other words, the TTS server should be in the same LAN where
                                                                        Unified CCX is. Thus, you need to specify the TTS server hostname or IP address that is local with the Unified CCX node while
                                                                        installing the TTS server software in this field. | Note | TTS server deployment over WAN is not supported in Unified CCX. In other words, the TTS server should be in the same LAN where
                                                                        Unified CCX is. Thus, you need to specify the TTS server hostname or IP address that is local with the Unified CCX node while
                                                                        installing the TTS server software in this field. |
| Note | TTS server deployment over WAN is not supported in Unified CCX. In other words, the TTS server should be in the same LAN where
                                                                        Unified CCX is. Thus, you need to specify the TTS server hostname or IP address that is local with the Unified CCX node while
                                                                        installing the TTS server software in this field. |
| Port | TCP port number used to connect to an MRCP server. Following are the different TCP Provider names: MRCP Server Nuance Vocalizer Scansoft Realspeak |
| Provider | The
                                                            							 MRCP TTS Provider to which this server is associated. |
| Status | Status
                                                            							 or state of the subsystem. |
| Step 2 | Click Add MRCP
                                                				TTS Server icon that displays in the tool bar in the upper, left
                                             			 corner of the window or the Add
                                                				New button that displays at the bottom of the window to provision a
                                             			 new MRCP ASR Server. The MRCP TTS
                                                				Server Configuration web page opens. |
| Step 3 | Specify the
                                             			 following fields: Field Description Server
                                                            							 Name Hostname or IP address of the server the MRCP TTS server software is installed. Provider Name Select
                                                            							 the name of the MRCP TTS Provider to which this server is associated from this
                                                            							 drop-down list. Port
                                                            							 Number The default TCP port number used to connect to a MRCP TTS server. The port number is automatically displayed based on the
                                                            provider or grammar variant that you have selected while configuring an MRCP TTS provider. Following are the different TCP
                                                            Provider names along with their port numbers: MRCP Server—554 Nuance Vocalizer—4900 for MRCPv1 and 5060 for MRCPv2 Scansoft Realspeak—4900 Locales Languages supported by the TTS Provider. Select a language (or
                                                            							 multiple languages) from the drop-down list and click Add Language ; the selected language appears in the
                                                            							 Enabled Language list. Note Use
                                                                        								the check box to disable/enable a language. | Field | Description | Server
                                                            							 Name | Hostname or IP address of the server the MRCP TTS server software is installed. | Provider Name | Select
                                                            							 the name of the MRCP TTS Provider to which this server is associated from this
                                                            							 drop-down list. | Port
                                                            							 Number | The default TCP port number used to connect to a MRCP TTS server. The port number is automatically displayed based on the
                                                            provider or grammar variant that you have selected while configuring an MRCP TTS provider. Following are the different TCP
                                                            Provider names along with their port numbers: MRCP Server—554 Nuance Vocalizer—4900 for MRCPv1 and 5060 for MRCPv2 Scansoft Realspeak—4900 | Locales | Languages supported by the TTS Provider. Select a language (or
                                                            							 multiple languages) from the drop-down list and click Add Language ; the selected language appears in the
                                                            							 Enabled Language list. Note Use
                                                                        								the check box to disable/enable a language. | Note | Use
                                                                        								the check box to disable/enable a language. |
| Field | Description |
| Server
                                                            							 Name | Hostname or IP address of the server the MRCP TTS server software is installed. |
| Provider Name | Select
                                                            							 the name of the MRCP TTS Provider to which this server is associated from this
                                                            							 drop-down list. |
| Port
                                                            							 Number | The default TCP port number used to connect to a MRCP TTS server. The port number is automatically displayed based on the
                                                            provider or grammar variant that you have selected while configuring an MRCP TTS provider. Following are the different TCP
                                                            Provider names along with their port numbers: MRCP Server—554 Nuance Vocalizer—4900 for MRCPv1 and 5060 for MRCPv2 Scansoft Realspeak—4900 |
| Locales | Languages supported by the TTS Provider. Select a language (or
                                                            							 multiple languages) from the drop-down list and click Add Language ; the selected language appears in the
                                                            							 Enabled Language list. Note Use
                                                                        								the check box to disable/enable a language. | Note | Use
                                                                        								the check box to disable/enable a language. |
| Note | Use
                                                                        								the check box to disable/enable a language. |
| Step 4 | Click Add to apply changes. Your changes
                                                				appear in the MRCP TTS Server Configuration web page. You are now ready to
                                                				provision MRCP TTS Default Genders. Note Whenever a new language is added for an MRCP Server—and if this is the first instance of this language being added for the
                                                            corresponding MRCP Provider—then the default gender for that locale and for the specified provider is set to Neutral. You
                                                            should check the MRCP Locales page to review the default genders that are set automatically per locale per provider. Default
                                                            genders are used when a prompt for a specific locale is used without specifying any gender. | Note | Whenever a new language is added for an MRCP Server—and if this is the first instance of this language being added for the
                                                            corresponding MRCP Provider—then the default gender for that locale and for the specified provider is set to Neutral. You
                                                            should check the MRCP Locales page to review the default genders that are set automatically per locale per provider. Default
                                                            genders are used when a prompt for a specific locale is used without specifying any gender. |
| Note | Whenever a new language is added for an MRCP Server—and if this is the first instance of this language being added for the
                                                            corresponding MRCP Provider—then the default gender for that locale and for the specified provider is set to Neutral. You
                                                            should check the MRCP Locales page to review the default genders that are set automatically per locale per provider. Default
                                                            genders are used when a prompt for a specific locale is used without specifying any gender. |

| Column | Description |
|---|---|
| Computer Name | Hostname or IP address of the server in which the TTS server software is installed. Note TTS server deployment over WAN is not supported in Unified CCX. In other words, the TTS server should be in the same LAN where
                                                                        Unified CCX is. Thus, you need to specify the TTS server hostname or IP address that is local with the Unified CCX node while
                                                                        installing the TTS server software in this field. | Note | TTS server deployment over WAN is not supported in Unified CCX. In other words, the TTS server should be in the same LAN where
                                                                        Unified CCX is. Thus, you need to specify the TTS server hostname or IP address that is local with the Unified CCX node while
                                                                        installing the TTS server software in this field. |
| Note | TTS server deployment over WAN is not supported in Unified CCX. In other words, the TTS server should be in the same LAN where
                                                                        Unified CCX is. Thus, you need to specify the TTS server hostname or IP address that is local with the Unified CCX node while
                                                                        installing the TTS server software in this field. |
| Port | TCP port number used to connect to an MRCP server. Following are the different TCP Provider names: MRCP Server Nuance Vocalizer Scansoft Realspeak |
| Provider | The
                                                            							 MRCP TTS Provider to which this server is associated. |
| Status | Status
                                                            							 or state of the subsystem. |

| Note | TTS server deployment over WAN is not supported in Unified CCX. In other words, the TTS server should be in the same LAN where
                                                                        Unified CCX is. Thus, you need to specify the TTS server hostname or IP address that is local with the Unified CCX node while
                                                                        installing the TTS server software in this field. |
|---|---|

| Field | Description |
|---|---|
| Server
                                                            							 Name | Hostname or IP address of the server the MRCP TTS server software is installed. |
| Provider Name | Select
                                                            							 the name of the MRCP TTS Provider to which this server is associated from this
                                                            							 drop-down list. |
| Port
                                                            							 Number | The default TCP port number used to connect to a MRCP TTS server. The port number is automatically displayed based on the
                                                            provider or grammar variant that you have selected while configuring an MRCP TTS provider. Following are the different TCP
                                                            Provider names along with their port numbers: MRCP Server—554 Nuance Vocalizer—4900 for MRCPv1 and 5060 for MRCPv2 Scansoft Realspeak—4900 |
| Locales | Languages supported by the TTS Provider. Select a language (or
                                                            							 multiple languages) from the drop-down list and click Add Language ; the selected language appears in the
                                                            							 Enabled Language list. Note Use
                                                                        								the check box to disable/enable a language. | Note | Use
                                                                        								the check box to disable/enable a language. |
| Note | Use
                                                                        								the check box to disable/enable a language. |

| Note | Use
                                                                        								the check box to disable/enable a language. |
|---|---|

| Note | Whenever a new language is added for an MRCP Server—and if this is the first instance of this language being added for the
                                                            corresponding MRCP Provider—then the default gender for that locale and for the specified provider is set to Neutral. You
                                                            should check the MRCP Locales page to review the default genders that are set automatically per locale per provider. Default
                                                            genders are used when a prompt for a specific locale is used without specifying any gender. |
|---|---|

| Step 1 | From the Unified CCX Administration menu bar, choose Subsystems > MRCP
                                                   				  TTS > MRCP TTS Default Genders . The MRCP TTS Default Gender Configuration web page opens,
                                                				displaying the default genders currently configured for each locale for every
                                                				MRCP TTS Provider that is currently configured. |
|---|---|
| Step 2 | Optionally, change the default gender setting for each locale for
                                             			 each provider. Note The Locale radio button has the Male, Female, or Neutral
                                                            				  options. By default, the "Default Gender" is set to "Neutral" unless configured explicitly. | Note | The Locale radio button has the Male, Female, or Neutral
                                                            				  options. By default, the "Default Gender" is set to "Neutral" unless configured explicitly. |
| Note | The Locale radio button has the Male, Female, or Neutral
                                                            				  options. By default, the "Default Gender" is set to "Neutral" unless configured explicitly. |
| Step 3 | Click Update to apply changes. The system updates the default gender setting for each Locale per
                                                				Provider. |

| Note | The Locale radio button has the Male, Female, or Neutral
                                                            				  options. By default, the "Default Gender" is set to "Neutral" unless configured explicitly. |
|---|---|